#!/usr/bin/env python3
"""validate_contribution.py - 提 PR 前的本地贡献分支预检

在「你的贡献仓库」里运行（不是本技能包目录）。只读：只调用 git rev-parse /
git log / git diff 等查询命令，不改任何文件、配置或远端。零依赖（Python 3.10+ 标准库）。

只检查「本分支相对上游基线新增的内容」，不扫描整个上游仓库，避免误报：
  1. 分支：不在 main/master、不在 detached HEAD
  2. 基线：能找到上游基线（upstream/HEAD、origin/HEAD、upstream/main ……）
  3. DCO：基线之后每个提交都有 Signed-off-by，且其中一行邮箱与作者邮箱一致
  4. 提交标题：符合 Conventional Commits 1.0.0 格式（仅提示，很多项目不要求）
  5. 新增行（+ 行）中无凭据样式字符串、无个人绝对路径

结果：凭据 / 个人路径 = error（FAIL）；其余 = warning（不阻断，请对照目标仓库的 CONTRIBUTING）。

用法：
  python /path/to/github-oss-contribute/scripts/validate_contribution.py [repo_dir]
      [--base upstream/main] [--quick] [--json]

  --base   指定上游基线（默认按 upstream/HEAD、origin/HEAD、upstream/main、
           upstream/master、origin/main、origin/master 依次查找）
  --quick  只查分支与提交信息，跳过新增内容扫描
  --json   机读输出
退出码：0 = PASS，1 = FAIL，2 = 不是 git 仓库或参数错误
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

BASE_CANDIDATES = (
    "upstream/HEAD",
    "origin/HEAD",
    "upstream/main",
    "upstream/master",
    "origin/main",
    "origin/master",
)

# 拼接写法，避免本文件被凭据扫描器误报
SECRET_PATTERNS = (
    (re.compile(r"\b" + "gh" + r"[pousr]_[A-Za-z0-9]{36,}"), "GitHub token（ghp_/gho_/ghu_/ghs_/ghr_）"),
    (re.compile(r"\b" + "github" + r"_pat_[A-Za-z0-9_]{22,}"), "GitHub fine-grained PAT"),
    (re.compile(r"\b" + "sk-" + r"ant-[A-Za-z0-9_-]{20,}"), "Anthropic API key"),
    (re.compile(r"\b" + "sk-" + r"(?:proj-)?[A-Za-z0-9_-]{20,}"), "OpenAI 风格 API key"),
    (re.compile(r"\b" + "AK" + r"IA[0-9A-Z]{16}"), "AWS access key ID"),
    (re.compile(r"\b" + "xox" + r"[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile("-----BEGIN " + r"(?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----"), "私钥"),
)
PERSONAL_PATH_PATTERNS = (
    (re.compile(r"[A-Za-z]:\\" + r"Users\\[^\\\s\"']+\\"), "Windows 个人目录"),
    (re.compile(r"/" + r"home/[A-Za-z0-9._-]+/"), "Linux 个人目录"),
    (re.compile(r"/" + r"Users/[A-Za-z0-9._-]+/"), "macOS 个人目录"),
)
CONVENTIONAL_RE = re.compile(r"^[a-z]+(\([^()\r\n]+\))?!?: \S")
SIGNOFF_RE = re.compile(r"^Signed-off-by:\s*.+<([^>]+)>\s*$", re.M | re.I)
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz", ".mp4"}


def git(repo: Path, *args: str) -> tuple[int, str]:
    proc = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=False)
    return proc.returncode, proc.stdout


def find_base(repo: Path, explicit: str | None) -> str | None:
    for ref in ([explicit] if explicit else BASE_CANDIDATES):
        code, _ = git(repo, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
        if code == 0:
            return ref
    return None


def check(repo: Path, base_ref: str | None = None, quick: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    code, out = git(repo, "rev-parse", "--is-inside-work-tree")
    if code != 0 or out.strip() != "true":
        return {"status": "ERROR", "target": str(repo), "errors": ["不是 git 工作区"],
                "warnings": [], "passed": []}

    # 1. 分支
    _, branch = git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    branch = branch.strip()
    if branch == "HEAD":
        warnings.append("[分支] 处于 detached HEAD，先 git switch -c fix/xxx 建特性分支")
    elif branch in ("main", "master"):
        warnings.append(f"[分支] 当前在 {branch}，请从特性分支（如 fix/xxx）提 PR")
    else:
        passed.append(f"[分支] {branch}")

    # 2. 基线
    base = find_base(repo, base_ref)
    if not base:
        warnings.append("[基线] 找不到上游基线：先 git remote add upstream <上游地址> && git fetch upstream，"
                        "或用 --base 指定；以下只检查 HEAD 一个提交")
        rev_range = ["-1", "HEAD"]
        diff_range = ["HEAD~1", "HEAD"] if git(repo, "rev-parse", "--verify", "--quiet", "HEAD~1")[0] == 0 else None
    else:
        _, mb = git(repo, "merge-base", base, "HEAD")
        mb = mb.strip()
        rev_range = [f"{mb}..HEAD"]
        diff_range = [mb, "HEAD"]
        passed.append(f"[基线] {base}")

    # 3 + 4. 逐个提交
    sep = "\x1e"
    _, log = git(repo, "log", "--no-merges", f"--format=%h%x1f%ae%x1f%s%x1f%B{sep}", *rev_range)
    commits = [c.strip("\n") for c in log.split(sep) if c.strip()]
    if not commits:
        warnings.append("[提交] 相对基线没有新提交")
    for raw in commits:
        sha, email, subject, body = (raw.split("\x1f", 3) + ["", "", ""])[:4]
        signoffs = [e.lower() for e in SIGNOFF_RE.findall(body)]
        if not signoffs:
            warnings.append(f"[DCO] {sha} 缺 Signed-off-by（若项目要求 DCO：git commit --amend -s，"
                            "多个提交用 git rebase --signoff <基线>）")
        elif email.lower() not in signoffs:
            warnings.append(f"[DCO] {sha} 的 Signed-off-by 邮箱与作者邮箱 {email} 不一致")
        if not CONVENTIONAL_RE.match(subject):
            warnings.append(f"[提交标题] {sha} 「{subject}」不是 Conventional Commits 格式（仅当项目要求时需要改）")
    if commits and not any(w.startswith(("[DCO]", "[提交标题]")) for w in warnings):
        passed.append(f"[提交] {len(commits)} 个提交均已签署且标题规范")

    # 5. 新增内容扫描
    if not quick and diff_range:
        _, diff = git(repo, "diff", "--no-color", "--unified=0", "--no-ext-diff", *diff_range)
        current = ""
        hits = 0
        for line in diff.splitlines():
            if line.startswith("+++ "):
                current = line[6:] if line.startswith("+++ b/") else line[4:]
                continue
            if not line.startswith("+") or Path(current).suffix.lower() in BINARY_SUFFIXES:
                continue
            for pattern, label in SECRET_PATTERNS + PERSONAL_PATH_PATTERNS:
                if pattern.search(line):
                    hits += 1
                    errors.append(f"[新增内容] {current}: {label}")
                    break
        if not hits:
            passed.append("[新增内容] 未发现凭据或个人路径")

    return {
        "status": "FAIL" if errors else "PASS",
        "target": str(repo),
        "branch": branch,
        "base": base,
        "mode": "quick" if quick else "full",
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="提 PR 前的本地贡献分支预检（只读）")
    parser.add_argument("target", nargs="?", default=".", help="贡献仓库路径（默认当前目录）")
    parser.add_argument("--base", help="上游基线，如 upstream/main")
    parser.add_argument("--quick", action="store_true", help="跳过新增内容扫描")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--read-only", action="store_true", help=argparse.SUPPRESS)  # 旧参数，始终只读
    args = parser.parse_args(argv)

    repo = Path(args.target).resolve()
    if not repo.is_dir():
        print(f"不是目录: {repo}", file=sys.stderr)
        return 2
    report = check(repo, args.base, args.quick)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"{repo}（{report.get('mode', '-')}）: {report['status']}")
        for item in report["passed"]:
            print(f"  [+] {item}")
        for item in report["warnings"]:
            print(f"  [!] {item}")
        for item in report["errors"]:
            print(f"  [x] {item}")
    return {"PASS": 0, "FAIL": 1}.get(report["status"], 2)


if __name__ == "__main__":
    sys.exit(main())
