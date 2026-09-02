#!/usr/bin/env python3
"""github-oss-contribute 自测：验证技能文档结构完整、引用齐全、关键流程在位。

好夹具（本技能自身）：SKILL.md 存在且 frontmatter 合规、6 个 Phase 全在、
所有 references 文件被 SKILL.md 引用、统一启动脚本与示例入口在盘。
负向用例（临时构造）：缺 Phase / 引用不存在文件的同套校验，必须判 FAIL。
零依赖，仅 Python 标准库。

Run: python scripts/selftest.py   # 退出 0 = PASS，1 = FAIL"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
NAME_RE = r"^[a-z0-9]+(-[a-z0-9]+)*$"
PHASES = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"]


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

# 好夹具：本技能自身
if not SKILL.is_file():
    print("RESULT FAIL\n - SKILL.md missing")
    sys.exit(1)
text = SKILL.read_text(encoding="utf-8")
failures += check_skill_text(text, ROOT.name)

# 关键配套在盘
for p in ("scripts/validate-skill.mjs", "examples/README.md",
          "references/ai-slop-guide.md", "references/security-guide.md"):
    if not (ROOT / p).is_file():
        failures.append(f"missing file: {p}")

# 调研新增内容防回归（2026-08 复审采纳项）
for kw in ("Rulesets", "Merge Queue", "Bot Reviewer", "Private vulnerability reporting",
           "gpg.format ssh"):
    if kw not in text:
        failures.append(f"missing adopted keyword: {kw}")

# 负向用例：坏样本必须被同一套逻辑拒绝（name 不匹配 + 抽掉全部 Phase）
bad = "---\nname: bad-skill\ndescription: 触发词：贡献\n---\n\n无工作流正文。\n"
bad_root_failures = check_skill_text(bad, "github-oss-contribute")
if not any("Phase" in f for f in bad_root_failures):
    failures.append("negative: missing-phase sample NOT detected")

# 负向用例：孤儿引用检测必须生效（抽掉一个真实引用，让磁盘文件变孤儿）
no_ref_text = text.replace("references/ai-slop-guide.md", "ai-slop-guide")
orph = [f for f in check_skill_text(no_ref_text, ROOT.name) if "orphan" in f]
if not orph:
    failures.append("negative: orphan reference NOT detected")

print("RESULT " + ("PASS" if not failures else "FAIL"))
for f in failures:
    print(" -", f)
sys.exit(0 if not failures else 1)