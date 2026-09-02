# 反 AI Slop 深度指南与质量自检

> 帮助开源贡献者在充分借助 AI 助手加速开发的同时，严守代码质量、原理自证与社区贡献伦理。

---

## 目录

- [一、为什么维护者警惕 AI Slop](#一为什么维护者警惕-ai-slop)
- [二、AI Slop 的典型反模式](#二ai-slop-的典型反模式)
- [三、2026 贡献者 Human-in-the-Loop 三大自证铁律](#2026-ai-辅助贡献自检与自证准则-human-in-the-loop)
- [四、高质量 PR 描述编写模板](#四高质量-pr-描述编写模板)
- [五、AI 辅助贡献的合规披露与 Git Trailers](#五ai-辅助贡献的合规披露与-git-trailers)

---

The problem is not the use of AI itself. The problem is sending maintainers work that lacks context, understanding, verification or ownership. This guide defines an evidence-based quality gate without inventing a universal “AI policy.”

## Target-repository policy comes first

Before changing code, inspect the target repository for:

- `AGENTS.md` and other agent instructions;
- `CONTRIBUTING.md`, PR templates and Issue templates;
- an explicit AI/LLM contribution policy;
- DCO, CLA, signing and authorship requirements;
- test, lint, formatting and generated-file commands;
- maintainer comments on the selected Issue.

If no AI policy exists, do not infer that AI is banned or that disclosure is required. The contributor remains responsible for accuracy, licensing, security and maintainability. Disclose AI assistance when the repository requests it or when the user chooses to do so.

## Evidence gate before a PR

### Problem ownership

- Reproduce the bug or cite the exact requested behavior.
- Confirm the Issue is open, current and not already claimed.
- Explain why the change belongs in this repository.
- For broad or architectural work, obtain maintainer direction first.

### Scope control

- Change only files needed for the accepted outcome.
- Separate refactors, formatting and dependency updates unless they are necessary.
- Prefer the smallest reviewable change; there is no universal line-count limit.
- Explain generated files and include the command that regenerates them.

### Understanding

- Be able to explain the changed behavior, main design choice and trade-offs.
- Verify API and dependency claims against primary documentation or repository code.
- Do not paste code whose license or provenance is unclear.
- Do not impersonate a maintainer, reviewer or another contributor.

### Verification

- Run the repository-prescribed tests and record exact commands and outcomes.
- Add a regression test when the change fixes reproducible behavior and the project accepts tests.
- Distinguish “not run,” “not available” and “passed.”
- Treat CI output as evidence; identify the first root failure before editing downstream symptoms.

### Communication

- State the problem, approach, verification and known limitations.
- Link the Issue using the repository's preferred closing syntax only when the PR should close it.
- Answer review comments directly and update the PR description when scope changes.
- Do not send empty pings, mass-produced Issues or near-identical PRs across projects.

## Red flags

| Red flag | Better response |
| --- | --- |
| Entire files rewritten without need | Restore unrelated lines and isolate the behavioral change |
| Claims that tests passed without logs or commands | Run the tests or mark them honestly as not run |
| Generic PR description | Describe the repository-specific problem and evidence |
| New dependency for a small helper | Check existing utilities and justify the dependency |
| Dozens of formatting changes | Revert them or move them to a separately approved PR |
| AI disclosure copied from another project | Follow this repository's actual policy |
| Security finding posted publicly | Stop and use the repository's private disclosure path |

## Pre-PR checklist

```text
Repository rules
[ ] I read the applicable AGENTS/CONTRIBUTING/templates/AI policy.
[ ] The Issue is current and not already claimed.
[ ] I followed DCO/CLA/signing/authorship requirements.

Scope and understanding
[ ] Every changed file is necessary for the accepted outcome.
[ ] I can explain the design choice and trade-offs.
[ ] Third-party code/data/assets have clear provenance and compatible terms.

Verification
[ ] I recorded exact test/lint/build commands and results.
[ ] I did not claim checks that were not run.
[ ] The diff contains no secrets, private paths or unrelated generated files.

Communication
[ ] The PR explains problem, approach, evidence and limitations.
[ ] AI assistance is disclosed if required by policy or chosen by the contributor.
[ ] The PR is ready for respectful follow-up and maintenance.
```

## If a maintainer rejects the contribution

1. Read the stated reason without arguing about intent.
2. Ask one focused clarification only if the requested outcome is unclear.
3. Reduce scope or provide missing evidence when the maintainer invites revision.
4. Close the PR when the project does not want the change.
5. Do not reopen, duplicate or move the same unsolicited change to another channel.

---

## 2026 AI 辅助贡献自检与自证准则 (Human-in-the-Loop)

在充分借助 AI 助手加速开发的同时，贡献者必须满足以下三大自检铁律，避免被维护者判定为无意义的 AI Slop：

### 1. 原理自证（Comprehension Proof）
- **核心标准**：提交的每一行代码、每一个参数、每一个正则，贡献者本人必须能够用人类自然语言清晰解释其工作原理与选型理由；
- **自问自答**：“如果维护者问我为什么这里要用这套逻辑而不是另一种，我能给出有说服力的回答吗？”

### 2. 测试自证（Testing Proof）
- **核心标准**：任何功能改动或 Bug 修复，必须附带真实的本地单元测试或复现脚本；
- **自问自答**：“我是否在本地终端完整跑通了新增测试，并断言其能够成功拦截历史 Bug？”

### 3. 最小范围（Minimal Scope）
- **核心标准**：严格聚焦目标 Issue，绝不在同一个 PR 中顺手做大范围的代码重命名、排版微调或添加无关依赖；
- **自问自答**：“这个 PR 的 Diff 是否做到了最小可行修改？”