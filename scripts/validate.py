#!/usr/bin/env python3
"""validate.py - github-oss-contribute 技能包自检（唯一校验入口）

只读、零依赖（Python 3.10+ 标准库）。检查的是本技能包自身，不访问网络、不读取目标仓库。
检查贡献分支请用 scripts/validate_contribution.py。

检查项：
  1. 必需文件在盘
  2. SKILL.md frontmatter 符合 Agent Skills 规范：只用 name / description / license /
     compatibility / metadata / allowed-tools；版本写在 metadata.version
  3. 版本号四处一致：SKILL.md、manifest.json、CHANGELOG.md 最新条目、.github/repository-metadata.yml；
     manifest.json 的 updated_at 等于 CHANGELOG 最新条目日期
  4. CHANGELOG 每个二级标题形如 `## [x.y.z] - YYYY-MM-DD`
  5. references/ 下每份手册都被 SKILL.md 引用（无孤儿）
  6. 所有 Markdown 本地链接可达
  7. references/ 不得写死 "SKILL.md Step N"（编号一改就失效）
  8. README 安装路径齐全，中英文 README 写明当前版本
  9. 文本文件中无凭据样式字符串（规则与 validate_contribution.py 共用一份）、无危险凭据指引
 10. 全部 Python 文件可被 ast 解析

用法：
  python scripts/validate.py          # 人读输出，退出码 0=通过 1=失败
  python scripts/validate.py --json   # 机读输出
"""

from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys
from urllib.parse import unquote

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from validate_contribution import SECRET_PATTERNS as _CONTRIB_SECRET_PATTERNS  # noqa: E402

SKILL_NAME = "github-oss-contribute"
ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "README.en.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CONTRIBUTORS.md",
    "manifest.json",
    "agents/openai.yaml",
    "examples/README.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/repository-metadata.yml",
)

README_FRAGMENTS = (
    f"~/.agents/skills/{SKILL_NAME}",
    f"~/.claude/skills/{SKILL_NAME}",
    f"~/.cursor/skills/{SKILL_NAME}",
    f"https://github.com/hyt315/{SKILL_NAME}/releases/latest",
    "examples/README.md",
)

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".py", ".mjs", ".js", ".txt", ".svg"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

# 凭据规则只维护一份（validate_contribution.py），避免两处各改各的
SECRET_PATTERNS = tuple(pattern for pattern, _label in _CONTRIB_SECRET_PATTERNS)
# Agent Skills 规范允许的 frontmatter 顶层字段（https://agentskills.io/specification）
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
UNSAFE_PATTERNS = (
    re.compile(r"Get-ChildItem\s+-Path\s+\$HOME\s+-Recurse", re.I),
    re.compile(r"print\s*\(\s*token\s*\)", re.I),
    re.compile(r"echo\s+\$GITHUB_(?:TOKEN|PERSONAL_ACCESS_TOKEN)"),
    re.compile(r"~/\.codex/skills/"),  # Codex 已改用 ~/.agents/skills
    re.compile(r"security@example\.com", re.I),
)

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CHANGELOG_HEADING_RE = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - (\d{4}-\d{2}-\d{2})\s*$")
STEP_REF_RE = re.compile(r"SKILL\.md\s*Step\s*\d", re.I)


def _iter_files(root: pathlib.Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            yield path


def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontmatter(text: str) -> dict[str, str] | None:
    """解析 frontmatter 的顶层键；metadata 下的子键展开为 "metadata.<key>"。缺失时返回 None。"""
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return None
    fields: dict[str, str] = {}
    parent = ""
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        indented = line.startswith((" ", "\t"))
        if indented and parent:
            fields[f"{parent}.{key.strip()}"] = value.strip().strip("\"'")
        elif not indented:
            parent = key.strip() if not value.strip() else ""
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def validate(root: pathlib.Path = ROOT) -> dict:
    errors: list[str] = []
    checks = 0

    def check(ok: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not ok:
            errors.append(message)

    # 1. 必需文件
    for rel in REQUIRED_FILES:
        check((root / rel).is_file(), f"缺少必需文件: {rel}")
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        return {"status": "FAIL", "checks": checks, "errors": errors}
    skill = _read(skill_path)

    # 2. frontmatter
    fm = _frontmatter(skill)
    check(fm is not None, "SKILL.md 缺少 YAML frontmatter")
    fm = fm or {}
    top_level = {key for key in fm if "." not in key}
    extra = sorted(top_level - SPEC_FIELDS)
    check(not extra, f"SKILL.md frontmatter 有 Agent Skills 规范外的顶层字段 {extra}（版本请写在 metadata.version）")
    check(fm.get("name") == SKILL_NAME, f"SKILL.md name 应为 {SKILL_NAME}，实际为 {fm.get('name')!r}")
    description = fm.get("description", "")
    check(0 < len(description) <= 1024, f"SKILL.md description 应为 1–1024 字符，实际 {len(description)}")
    version = fm.get("metadata.version", "")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), f"SKILL.md metadata.version 不是 x.y.z: {version!r}")

    # 3. 版本一致
    manifest: dict = {}
    try:
        manifest = json.loads(_read(root / "manifest.json"))
        check(manifest.get("version") == version,
              f"manifest.json 版本 {manifest.get('version')!r} 与 SKILL.md {version!r} 不一致")
        check(manifest.get("name") == SKILL_NAME, "manifest.json name 不一致")
    except (OSError, json.JSONDecodeError) as exc:
        check(False, f"manifest.json 无法解析: {exc}")

    changelog_path = root / "CHANGELOG.md"
    if changelog_path.is_file():
        headings = [line for line in _read(changelog_path).splitlines() if line.startswith("## ")]
        # 4. 标题格式
        for line in headings:
            check(bool(CHANGELOG_HEADING_RE.match(line)), f"CHANGELOG 标题格式不对: {line!r}")
        newest = CHANGELOG_HEADING_RE.match(headings[0]) if headings else None
        check(bool(newest) and newest.group(1) == version,
              f"CHANGELOG 最新条目应为 [{version}]")
        if newest:
            check(manifest.get("updated_at") == newest.group(2),
                  f"manifest.json updated_at {manifest.get('updated_at')!r} 应等于 CHANGELOG 最新日期 {newest.group(2)}")

    metadata_path = root / ".github/repository-metadata.yml"
    if metadata_path.is_file():
        check(f"tag: v{version}" in _read(metadata_path),
              f"repository-metadata.yml 的 release tag 应为 v{version}")

    # 5. 无孤儿手册
    cited = set(re.findall(r"references/([\w\-]+\.md)", skill))
    for ref in sorted((root / "references").glob("*.md")):
        check(ref.name in cited, f"SKILL.md 未引用 references/{ref.name}")

    for path in _iter_files(root):
        rel = path.relative_to(root).as_posix()
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = _read(path)

        # 6. 本地链接
        if path.suffix == ".md":
            for target in LINK_RE.findall(text):
                if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target, re.I):
                    continue
                local = unquote(target.split("#", 1)[0])
                if local:
                    check((path.parent / local).exists(), f"{rel}: 本地链接失效 {target}")

        # 7. 写死步骤编号
        if rel.startswith("references/"):
            check(not STEP_REF_RE.search(text), f"{rel}: 不要写死 'SKILL.md Step N'，改写为适用任务")

        # 9. 凭据与危险指引
        for pattern in SECRET_PATTERNS:
            check(not pattern.search(text), f"{rel}: 疑似凭据字符串")
        for pattern in UNSAFE_PATTERNS:
            check(not pattern.search(text), f"{rel}: 不安全的凭据指引")

        # 10. Python 语法
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=rel)
                check(True, "")
            except SyntaxError as exc:
                check(False, f"{rel}: 第 {exc.lineno} 行语法错误 {exc.msg}")

    # 8. README 安装路径
    readme_path = root / "README.md"
    if readme_path.is_file():
        readme = _read(readme_path)
        for fragment in README_FRAGMENTS:
            check(fragment in readme, f"README.md 缺少 {fragment}")
    for name in ("README.md", "README.en.md"):
        path = root / name
        if path.is_file() and version:
            check(f"v{version}" in _read(path), f"{name} 未写明当前版本 v{version}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "skill": SKILL_NAME,
        "version": version,
        "checks": checks,
        "errors": errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="github-oss-contribute 技能包自检（只读）")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--root", type=pathlib.Path, default=ROOT, help="技能包根目录")
    args = parser.parse_args(argv)

    report = validate(args.root.resolve())
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"{SKILL_NAME} v{report.get('version', '?')}: {report['status']}（{report['checks']} 项检查）")
        for err in report["errors"]:
            print(f"  - {err}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
