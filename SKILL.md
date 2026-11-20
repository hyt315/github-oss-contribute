---
name: github-oss-contribute
description: "Use when contributing to someone else's open-source GitHub project: reading repo rules and AI policies, picking an Issue, forking and rebasing, DCO/CLA/SSH signing, AI disclosure, pre-PR self-checks, CI troubleshooting, and handling review feedback. Fork, push, comment, and PR creation are approval-gated. Triggers include 开源贡献、第一次贡献、提 PR、找个 issue 做、PR 被拒了怎么办、CI 红了、review 意见、DCO 失败、rebase 冲突、first contribution, contribute."
license: MIT
metadata:
  version: "2.3.0"
---

# 开源贡献导航

帮用户以贡献者身份向他人的开源项目提交一个干净、易合并的 PR：从侦察规则到最终合并。维护自己的项目请用 `github-oss-ops`。

## 铁律

1. **目标仓库规则优先**：`AGENTS.md`、`CONTRIBUTING.md`、PR 模板、AI 政策、DCO/CLA 与本技能冲突时，一律以目标仓库为准。
2. **默认只读，写操作逐项确认**：读规则、搜 Issue、本地改代码和跑测试无需批准；Fork、推送、评论、创建/更新 PR、强推改写历史前，逐项列明「做什么 + 具体内容 + 能否撤销」，获批哪项只做哪项。
3. **用户是作者**：代码必须由用户理解并负责。用了 AI 辅助就按项目政策如实披露（`Signed-off-by` 只能人签）；讲不清原理或未跑测试不提交。
4. **不碰凭据、不公开报漏洞**：不在聊天中索取 Token，不翻找本地凭据；发现安全漏洞一律走私有报告渠道。
5. **按需读手册**：查下方路由表，每个阶段只读对应的 1 份手册。

## 阶段路由

| 阶段 | 用户想做的事 | 先读 | 产出 | 需批准的写操作 |
|---|---|---|---|---|
| 1 侦察与避坑 | 了解目标仓库规则、认证方式、常见坑 | [pitfalls-and-access.md](references/pitfalls-and-access.md) | 规则摘要（见下方侦察命令） | 无 |
| 2 选题与质量 | 挑 Issue、反 AI Slop 自检、写 PR 描述、报安全漏洞、回复 Review | [ai-policy-and-pr-quality.md](references/ai-policy-and-pr-quality.md) | 候选 Issue / 事实卡 / PR 与回复草稿 | 发评论、提私有报告、创建 PR |
| 3 分支与排查 | Fork、配置 `upstream`、Rebase 冲突、Git 报错、CI 失败诊断 | [git-and-fork.md](references/git-and-fork.md) | 本地特性分支 / 修复方案 | Fork、推送、强推 |
| 4 提交与签名 | Conventional Commits、DCO/CLA、SSH 签名、AI 披露 trailer | [commits-dco-and-signing.md](references/commits-dco-and-signing.md) | 规范本地提交 | 无 |

## 阶段 1：侦察命令（只读）

```bash
R=owner/repo
gh repo view $R --json defaultBranchRef,description,licenseInfo,hasDiscussionsEnabled
gh api repos/$R/contents/CONTRIBUTING.md -q .download_url
gh api repos/$R/contents/AGENTS.md -q .download_url
gh api repos/$R/rules/branches/<默认分支>
gh issue list -R $R --label "good first issue" --state open --limit 30 --json number,title,assignees,updatedAt
```

> `gh` 即使只读也需先登录；不想登录时可用 `curl https://api.github.com/repos/$R/...` 或直接看网页。注意：Fine-grained PAT 不能在你非成员的公开仓库评论或开 PR，上游互动统一用已登录的 `gh`、OAuth 连接器或网页。

## 提 PR 前预检（必跑）

在贡献仓库根目录运行（只读）：

```bash
python <本技能目录>/scripts/validate_contribution.py . --base upstream/main
```

只检查本分支相对上游基线新增的提交与新增行（分支隔离、DCO 邮箱一致、Conventional Commits 提示、新增行无真实凭据或本机个人路径）。凭据或个人路径命中即 FAIL 并给出 `文件:行号`。

## 事实卡格式

提 PR 前展示实测事实卡（下表为格式示例，查不到写「未查」），文末单列「待批准写操作」：

| 检查项 | 实测 | 要求（目标仓库） | 结论 |
|---|---|---|---|
| 分支 | `fix/typo-in-readme` | 非默认分支 | 通过 |
| DCO / 签名 | 2/2 已签署，邮箱一致 | CONTRIBUTING 要求 DCO | 通过 |
| 本地测试 | `npm test` 通过 | CONTRIBUTING 指定命令 | 通过 |
| 新增内容 | 无凭据、无个人路径 | — | 通过 |
| AI 披露 | PR 描述已注明 | 按项目 AI 政策 | 通过 |

## 本技能包自检

```bash
python scripts/validate.py
python -m unittest discover tests -v
```
