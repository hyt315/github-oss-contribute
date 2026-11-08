---
name: github-oss-contribute
version: 2.2.0
description: Use when the user wants to contribute to someone else's open-source GitHub project - choosing an Issue, reading the project's contribution rules and AI policy, forking and branching, syncing with upstream and resolving rebase conflicts, Conventional Commits, DCO sign-off, CLA, signed commits, pre-PR self-checks, writing the PR, fixing failing CI and answering review feedback. Fork, push, comment and PR creation are approval-gated. Triggers include 开源贡献、第一次贡献、提 PR、找个 issue 做、PR 被拒了怎么办、CI 红了、review 意见、DCO 失败、rebase 冲突、first contribution、contribute.
---

# 开源贡献导航

帮用户以贡献者身份给别人的开源项目提交一个能被合并的 PR：从选题到合并。只管“给别人的项目做贡献”；维护自己的项目用 `github-oss-ops`。

## 铁律

1. **目标仓库的规则优先**：AGENTS.md、CONTRIBUTING.md、PR 模板、AI 政策、DCO／CLA 要求，与本技能冲突时以目标仓库为准。
2. **默认只读**：读规则、搜 Issue、读代码、本地改代码和跑测试不需要批准。Fork、推送、在 Issue／PR 下评论、创建或更新 PR、改写已推送的历史，执行前逐项展示“做什么 + 具体内容 + 能否撤销”，得到用户明确确认后才做。
3. **用户是作者**：代码由用户理解并负责。用了 AI 辅助就按项目要求如实披露；用户讲不清改动原理或没跑过测试，就不提交。
4. **不碰凭据**：不让用户在聊天里贴 Token，不翻用户目录找凭据，不打印凭据。安全漏洞不公开提，走私有渠道。
5. **按需读手册**：先用下面的路由表找到阶段，只读对应的一两份手册。GitHub 界面名称以 2026-11-08 核对为准，和实际页面不一致时以页面为准。

## 阶段路由

| 阶段 | 用户想做的事 | 先读 | 产出 | 需批准的写操作 |
|---|---|---|---|---|
| 1 侦察 | 了解目标仓库规则、选访问方式 | [mcp-tools.md](references/mcp-tools.md) | 规则摘要（见下方侦察命令） | 无 |
| 2 选题 | 找适合的 Issue、认领 | [first-timer-tips.md](references/first-timer-tips.md)、[communication-etiquette.md](references/communication-etiquette.md) | 2–3 个候选 + 认领留言草稿 | 发认领评论 |
| 2 选题 | 发现的是安全漏洞 | [security-guide.md](references/security-guide.md) | 私有报告草稿 | 提交私有报告 |
| 3 准备 | Fork、配置 upstream、建分支、同步上游 | [git-fork-and-conflict-guide.md](references/git-fork-and-conflict-guide.md) | 本地特性分支 | Fork |
| 4 开发 | 写提交信息、DCO、CLA、签名提交 | [commit-conventions.md](references/commit-conventions.md)、[dco-cla-and-signing.md](references/dco-cla-and-signing.md) | 规范的本地提交 | 无 |
| 5 提交 | 提 PR 前自检、写 PR 描述 | [ai-slop-guide.md](references/ai-slop-guide.md)、[security-guide.md](references/security-guide.md) | 预检结果 + 事实卡 + PR 描述草稿 | 推送分支、创建 PR |
| 6 跟踪 | CI 失败、Review 意见、冲突、催合并 | [ci-troubleshooting.md](references/ci-troubleshooting.md)、[git-errors.md](references/git-errors.md)、[communication-etiquette.md](references/communication-etiquette.md) | 原因 + 修复 + 回复草稿 | 推送修复、强推、回复评论 |

任何阶段遇到常见坑（在 Fork 的 main 上提 PR、merge 污染历史、DCO 邮箱不一致、Fork PR 拿不到 Secrets、`Fixes #` 没生效）先查 [github-oss-contribute-pitfalls.md](references/github-oss-contribute-pitfalls.md)。

## 阶段 1：侦察命令（只读）

```bash
R=owner/repo
gh repo view $R --json defaultBranchRef,description,licenseInfo,hasDiscussionsEnabled
gh api repos/$R/contents/CONTRIBUTING.md -q .download_url     # 也查 .github/、docs/ 下的同名文件
gh api repos/$R/contents/AGENTS.md -q .download_url            # 不存在会返回 404，属正常
gh api repos/$R/rules/branches/<默认分支>                       # 对默认分支生效的规则（签名、线性历史、必需检查等）
gh api repos/$R/community/profile -q '.files | keys'           # 社区文件是否齐全
gh issue list -R $R --label "good first issue" --state open --limit 30 --json number,title,assignees,updatedAt
```

`gh` 即使只读也要先登录（`gh auth login --web`）。用户不想登录时，用 `curl https://api.github.com/repos/$R/...` 调同名公开接口（未认证每小时 60 次）或直接看网页。

要确认的事：贡献流程和测试命令、是否要求 DCO 或 CLA、是否要求签名提交、AI 辅助政策、分支命名和提交信息规范、是否用 Merge Queue。查不到的项写“未查”。

写操作的认证：Fine-grained PAT 不能在你不是成员的公开仓库评论或开 PR，只能推到自己的 Fork；上游评论和建 PR 用已登录的 `gh`、OAuth 连接器或网页。

## 阶段 5：提 PR 前预检

在用户的贡献仓库里运行（只读）：

```bash
python <本技能目录>/scripts/validate_contribution.py . --base upstream/main
```

它只检查本分支相对上游新增的内容：是否在特性分支、每个提交有无 Signed-off-by 且邮箱与作者一致、提交标题格式、新增行里有无凭据或个人绝对路径。凭据命中即 FAIL；其余是提示，按目标仓库要求取舍。

## 事实卡格式

提 PR 前给用户看一张事实卡，每一行写实测值，查不到写“未查”：

| 检查项 | 实测 | 要求（来自目标仓库） | 结论 |
|---|---|---|---|
| 分支 | `fix/typo-in-readme` | 非默认分支 | 通过 |
| DCO | 2/2 个提交已签署，邮箱一致 | CONTRIBUTING 要求 DCO | 通过 |
| 签名提交 | 未签名 | 规则集未要求 | 不需要 |
| 本地测试 | `npm test` 全部通过 | CONTRIBUTING 指定 `npm test` | 通过 |
| 新增内容 | 无凭据、无个人路径 | — | 通过 |
| 关联 Issue | `Fixes #123`，目标为默认分支 | — | 合并后自动关闭 |
| AI 披露 | PR 描述已注明 | 项目 AI 政策要求披露 | 通过 |

（表中数值是格式示例。）事实卡之后单列“待批准写操作”：推送到哪个远端分支、PR 标题和目标分支。用户确认哪项只做哪项，做完回读结果。

## 改动本技能后

```bash
python scripts/validate.py                 # 技能包自检：结构、版本一致、链接、凭据
python -m unittest discover tests          # 两个脚本的正向与负向测试
```
