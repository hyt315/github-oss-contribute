# 反 AI Slop 深度指南与质量自检

> 帮助开源贡献者在充分借助 AI 助手加速开发的同时，严守代码质量、原理自证与社区贡献伦理。

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

## 中文速查：提 PR 前三问

1. **讲得清吗**：每一处改动，用户本人能说清为什么这样改、为什么不用别的办法。
2. **验证过吗**：项目有测试就补回归测试并在本地跑通；没有测试就给出可复现的前后对比（命令和输出）。没跑过的不要写“已测试”。
3. **够小吗**：只改 Issue 需要的部分，不顺手重命名、格式化无关代码或加依赖。

## 各项目 AI 政策差异（2026-11-08 核对）

政策差别很大，一定读目标仓库自己的规定。几个代表：

| 项目 | 立场 | 要点 | 来源 |
|---|---|---|---|
| QEMU、Zig、Gentoo、NetBSD | 禁止或基本禁止 | 不接受 AI 生成的贡献（NetBSD 需核心团队事先批准） | [QEMU](https://www.qemu.org/docs/master/devel/code-provenance.html)、[Zig](https://ziglang.org/code-of-conduct/)、[Gentoo](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)、[NetBSD](https://www.netbsd.org/developers/commit-guidelines.html) |
| Linux 内核 | 有条件允许 | 需透明说明；AI 不得添加 `Signed-off-by`，DCO 只能由人签 | [coding-assistants](https://docs.kernel.org/process/coding-assistants.html) |
| curl | 有条件允许 | 按常规标准审 AI 辅助代码；提交虚假 AI 安全报告者直接封禁 | [CONTRIBUTE.md](https://github.com/curl/curl/blob/master/docs/CONTRIBUTE.md) |
| Homebrew | 有条件允许 | 必须披露；Review 必须本人回答、不能用 AI 写回复；非维护者同时最多 1 个 AI 辅助 PR；不得把 AI 列为作者或在 trailer 里署名 | [How to open a PR](https://docs.brew.sh/How-To-Open-a-Homebrew-Pull-Request) |
| Ghostty | 有条件允许 | 必须披露；低质量 AI 贡献者会被公开列入名单 | [AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md) |
| Debian | 中立 | 2026-08-30 投票结果：既不支持也不禁止 | [公告](https://lists.debian.org/debian-devel-announce/2026/08/msg00005.html) |

`Assisted-by` 等 trailer 的写法各项目相反（有的要求、有的禁止），按目标仓库规定，没有规定就在 PR 描述里用一句话说明。
