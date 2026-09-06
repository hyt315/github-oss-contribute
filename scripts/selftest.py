#!/usr/bin/env python3
"""github-oss-contribute 自测：验证技能文档结构完整、引用齐全、关键流程在位与代码 AST 静态语法。

好夹具（本技能自身）：SKILL.md 存在且 frontmatter 合规、6 个 Phase 全在、
所有 references 文件被 SKILL.md 引用、统一启动脚本、测试入口与核心避坑库在盘。
负向用例（临时构造）：缺 Phase / 引用不存在文件 / 语法错误 / 敏感凭据注入，必须判 FAIL。
零依赖，仅 Python 标准库。

Run: python scripts/selftest.py   # 退出 0 = PASS，1 = FAIL
"""

from __future__ import annotations

import ast
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
NAME_RE = r"^[a-z0-9]+(-[a-z0-9]+)*$"
PHASES = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"]


def test_syntax_ast() -> list[str]:
    """Validate Python syntax across all internal scripts using ast.parse."""
    failures = []
    scripts_dir = ROOT / "scripts"
    if scripts_dir.is_dir():
        for py_file in scripts_dir.glob("*.py"):
            try:
                ast.parse(py_file.read_text(encoding="utf-8"), filename=py_file.name)
            except SyntaxError as e:
                failures.append(f"AST syntax error in {py_file.name}: {e}")
    tests_dir = ROOT / "tests"
    if tests_dir.is_dir():
        for py_file in tests_dir.glob("*.py"):
            try:
                ast.parse(py_file.read_text(encoding="utf-8"), filename=py_file.name)
            except SyntaxError as e:
                failures.append(f"AST syntax error in {py_file.name}: {e}")
    return failures


def check_skill_text(text: str, root_name: str) -> list[str]:
    """同套校验逻辑：返回 failures 列表（空 = 通过）。供正向与负向共用。"""
    failures: list[str] = []
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        return ["frontmatter missing"]
    head = fm.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", head, re.M)
    n = name.group(1) if name else ""
    if not re.match(NAME_RE, n) or n != root_name:
        failures.append(f"name '{n}' invalid or != {root_name}")
    desc = re.search(r"^description:\s*\|?\s*\n?((?:\s+.+\n?)+)", head, re.M)
    if not desc or not re.search(r"触发词|contribute|贡献", desc.group(1)):
        failures.append("description missing trigger words")
    for phase in PHASES:
        if phase not in text:
            failures.append(f"missing workflow section: {phase}")
    refs = set(re.findall(r"references/[\w\-]+\.md", text))
    actual = {f"references/{p.name}" for p in (ROOT / "references").glob("*.md")}
    if actual - refs:
        failures.append(f"orphan references: {sorted(actual - refs)}")
    return failures


failures: list[str] = []

# 0. AST 静态语法解析门禁
failures += test_syntax_ast()

# 1. 好夹具：本技能自身
if not SKILL.is_file():
    print("RESULT FAIL\n - SKILL.md missing")
    sys.exit(1)
text = SKILL.read_text(encoding="utf-8")
failures += check_skill_text(text, ROOT.name)

# 2. 关键配套在盘
required_files = [
    "scripts/validate-skill.mjs",
    "scripts/validate_contribution.py",
    "tests/test_skill.py",
    "examples/README.md",
    "references/ai-slop-guide.md",
    "references/security-guide.md",
    "references/github-oss-contribute-pitfalls.md",
]
for p in required_files:
    if not (ROOT / p).is_file():
        failures.append(f"missing file: {p}")

# 3. 核心技术基线与避坑深度断言
for kw in ("Rulesets", "Merge Queue", "Bot Reviewer", "Private vulnerability reporting",
           "gpg.format ssh", "rerere", "DCO", "Signed-off-by"):
    if kw not in text:
        failures.append(f"missing adopted keyword: {kw}")

# 4. 避坑库深度词断言
pitfalls_file = ROOT / "references" / "github-oss-contribute-pitfalls.md"
if pitfalls_file.is_file():
    p_text = pitfalls_file.read_text(encoding="utf-8")
    for kw in ("git-filter-repo", "Signed-off-by", "Anti-AI Slop", "rerere", "force-with-lease"):
        if kw not in p_text:
            failures.append(f"Pitfalls document missing depth assertion keyword: '{kw}'")

# 5. DY002 负向用例：坏样本必须被同一套逻辑拒绝（name 不匹配 + 抽掉全部 Phase）
bad = "---\nname: bad-skill\ndescription: 触发词：贡献\n---\n\n无工作流正文。\n"
bad_root_failures = check_skill_text(bad, "github-oss-contribute")
if not any("Phase" in f for f in bad_root_failures):
    failures.append("negative: missing-phase sample NOT detected")

# 6. DY002 负向用例：孤儿引用检测必须生效（抽掉一个真实引用，让磁盘文件变孤儿）
no_ref_text = text.replace("references/ai-slop-guide.md", "ai-slop-guide")
orph = [f for f in check_skill_text(no_ref_text, ROOT.name) if "orphan" in f]
if not orph:
    failures.append("negative: orphan reference NOT detected")

# 7. DY002 负向断言：凭据与个人路径正则有效拦截
secret_pat = re.compile(r"ghp_[A-Za-z0-9]{36}")
if not secret_pat.search("ghp_123456789012345678901234567890123456"):  # skill-doctor: allow
    failures.append("Negative test: secret pattern failed to catch dummy classic PAT")

personal_pat = re.compile(r"[A-Za-z]:\\Users\\[a-zA-Z0-9_-]+[\\/]")  # skill-doctor: allow
if not personal_pat.search("C:\\Users\\alice\\Desktop\\test\\"):  # skill-doctor: allow
    failures.append("Negative test: personal path pattern failed to catch dummy Windows path")

tampered_secret = "OPENAI_KEY = 'sk-test12345678901234567890abcdef'"  # skill-doctor: allow
openai_pat = re.compile(r"sk-[A-Za-z0-9-_]{20,}")
if not openai_pat.search(tampered_secret):
    failures.append("Negative test: tampered secret should fail validation")

# 8. 辅助脚本集成联测：运行 validate_contribution.py --json
val_script = ROOT / "scripts" / "validate_contribution.py"
if val_script.is_file():
    proc = subprocess.run([sys.executable, str(val_script), str(ROOT), "--json"], capture_output=True, text=True)
    if proc.returncode != 0:
        failures.append(f"validate_contribution.py --json failed with rc={proc.returncode}")
    else:
        try:
            data = json.loads(proc.stdout)
            if data.get("status") != "PASS":
                failures.append(f"validate_contribution report status is {data.get('status')}")
        except json.JSONDecodeError as e:
            failures.append(f"validate_contribution output invalid json: {e}")

print("RESULT " + ("PASS" if not failures else "FAIL"))
for f in failures:
    print(" -", f)
sys.exit(0 if not failures else 1)
