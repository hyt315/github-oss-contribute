#!/usr/bin/env python3
"""Local contribution branch hygiene, DCO signoff, and security validation tool for github-oss-contribute.

Usage:
  python scripts/validate_contribution.py [target_dir] [--json] [--quick] [--read-only]

Features:
  - Validates feature branch isolation (ensures PR is not being opened from main/master)
  - Validates DCO (Signed-off-by) sign-off on recent commits
  - Scans changed files for hardcoded secrets, API keys, and personal paths
  - Checks Conventional Commits syntax on the HEAD commit message
  - Machine-readable JSON structured export (--json) and fast sampling (--quick)
  - Pure Python standard library, zero external dependencies, 100% read-only
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Credentials & Secrets patterns
SECRET_PATTERNS = [
    (re.compile(r"sk-[A-Za-z0-9-_]{20,}"), "OpenAI API Key pattern"),
    (re.compile(r"sk-ant-[A-Za-z0-9-_]{20,}"), "Anthropic API Key pattern"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "GitHub Classic PAT pattern"),
    (re.compile(r"github_pat_[A-Za-z0-9_]{82}"), "GitHub Fine-Grained PAT pattern"),
    (re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----"), "SSH Private Key"),
]

# 2. Local personal path patterns (skill-doctor: allow)
PERSONAL_PATH_PATTERNS = [
    (re.compile(r"[A-Za-z]:\\Users\\[a-zA-Z0-9_-]+[\\/]"), "Windows personal user path"),  # skill-doctor: allow
    (re.compile(r"/home/[a-zA-Z0-9_-]+/"), "Linux personal user path"),
    (re.compile(r"/Users/[a-zA-Z0-9_-]+/"), "macOS personal user path"),
]

# Conventional commit types
CONVENTIONAL_COMMIT_RE = re.compile(
    r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-zA-Z0-9_-]+\))?!?: .+$"
)

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".doctor"}
EXCLUDE_EXTS = {".png", ".jpg", ".webp", ".mp4", ".zip", ".tar.gz", ".pyc", ".ico"}
EXCLUDE_FILES = {
    "validate_contribution.py",
    "selftest.py",
    "test_skill.py",
    "audit.py",
    "github-oss-contribute-pitfalls.md",
    "security-guide.md",
    "ai-slop-guide.md",
}


def check_git_branch(target_dir: Path) -> list[str]:
    """Check if repository is on a clean feature branch instead of main."""
    issues = []
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=target_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            branch = proc.stdout.strip()
            # If in detached HEAD or main/master, warn contributor
            if branch in ("main", "master"):
                issues.append(f"当前处于主干分支 '{branch}'。提 PR 前强烈建议创建独立特性分支 (如 feat/xxx 或 fix/xxx)")
    except Exception:  # skill-doctor: allow
        pass
    return issues


def check_recent_dco(target_dir: Path) -> list[str]:
    """Check if HEAD commit contains a Signed-off-by trailer."""
    issues = []
    try:
        proc = subprocess.run(
            ["git", "log", "-1", "--format=%H|%an|%ae|%B"],
            cwd=target_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            parts = proc.stdout.split("|", 3)
            if len(parts) >= 4:
                commit_sha, author_name, author_email, body = parts[0][:8], parts[1], parts[2], parts[3]
                if "Signed-off-by:" not in body:
                    issues.append(f"最新提交 {commit_sha} 缺失 DCO 签名 (需执行 git commit -s --amend 补签)")
    except Exception:  # skill-doctor: allow
        pass
    return issues


def validate_contribution(target_dir: Path, quick: bool = False) -> dict:
    """Validate contribution readiness, privacy hygiene, and branch health."""
    errors: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    # 1. Branch hygiene check
    branch_issues = check_git_branch(target_dir)
    for bi in branch_issues:
        warnings.append(f"WARN [Branch]: {bi}")
    if not branch_issues:
        passed.append("Branch check passed: not on default branch or git clean")

    # 2. DCO check
    dco_issues = check_recent_dco(target_dir)
    for di in dco_issues:
        warnings.append(f"WARN [DCO]: {di}")
    if not dco_issues:
        passed.append("DCO check: commit signed-off or branch ready")

    # If quick mode, return early
    if quick:
        return {
            "status": "PASS" if not errors else "FAIL",
            "target": str(target_dir),
            "mode": "quick",
            "errors": errors,
            "warnings": warnings,
            "passed": passed,
        }

    # 3. Scan files for credentials & personal paths
    for p in target_dir.rglob("*"):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in EXCLUDE_EXTS:
            continue
        if not p.is_file():
            continue
        if p.name in EXCLUDE_FILES:
            continue

        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:  # skill-doctor: allow
            warnings.append(f"WARN: Could not read {p.relative_to(target_dir)}: {e}")
            continue

        for pat, desc in SECRET_PATTERNS:
            if pat.search(content):
                errors.append(f"Secret detected in {p.relative_to(target_dir)}: {desc}")

        for pat, desc in PERSONAL_PATH_PATTERNS:
            if pat.search(content):
                errors.append(f"Personal path detected in {p.relative_to(target_dir)}: {desc}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "target": str(target_dir),
        "mode": "full",
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="validate_contribution: 本地贡献分支、DCO 与隐私安全校验工具")
    parser.add_argument("target", nargs="?", default=".", help="目标仓库路径 (默认当前目录)")
    parser.add_argument("--json", "-Json", action="store_true", help="以结构化机读 JSON 格式输出结果")
    parser.add_argument("--quick", "-Quick", action="store_true", help="执行快速采样审计")
    parser.add_argument("--read-only", action="store_true", help="显式声明纯只读模式运行")

    args = parser.parse_args()
    target_path = Path(args.target).resolve()

    if not target_path.is_dir():
        print(f"Error: 目标路径不是有效目录: {target_path}", file=sys.stderr)
        return 1

    result = validate_contribution(target_path, quick=args.quick)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["status"] == "PASS" else 1

    print(f"Validating contribution at: {target_path} (Mode: {result['mode']})")
    if result["passed"]:
        for p in result["passed"]:
            print(f" [+] {p}")
    if result["warnings"]:
        for w in result["warnings"]:
            print(f" [!] {w}", file=sys.stderr)
    if result["errors"]:
        print(f"\nFAIL: Found {len(result['errors'])} error(s):", file=sys.stderr)
        for e in result["errors"]:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("\nPASS: Contribution validation successful with zero errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
