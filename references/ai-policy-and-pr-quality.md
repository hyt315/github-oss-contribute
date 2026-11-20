# 反 AI Slop 质量门槛、安全自检与沟通原则

> 适用任务：挑选合适 Issue、提 PR 前质量与安全自检、撰写 PR 描述与回复 Review、向目标项目报告安全漏洞。

## 1. 选题与沟通原则（不套固定英文模板）

- **选对 Issue**：优先看带 `good first issue` / `help wanted`、近期有维护者活动、且尚无未关闭关联 PR 的 Issue；避免去陌生仓库批量改错字刷 PR（Hacktoberfest 自 2026 起也不再统计 PR，无意义微调会被当垃圾关闭）。
- **先沟通再写大改动**：新功能或跨模块重构先在 Issue/Discussion 确认设计方向；认领留言简明说明你的方案与预计范围即可，无需套长段客套模板。
- **回复 Review 礼仪**：逐条回应意见、改完后附上对应 commit hash；遇到分歧客观摆证据与权衡；超过 1–2 周无回应时最多礼貌提醒一次。

## 2. 反 AI Slop：提 PR 前三问（目标仓库 AI 政策优先）

各项目 AI 政策差异很大（如 QEMU/Zig/Gentoo/NetBSD 严格禁止，Linux 内核/curl/Homebrew/Ghostty 有条件允许，Debian 中立），动工前必先查 `AGENTS.md` / `CONTRIBUTING.md`。允许 AI 辅助时，提交前必须过三关：

1. **原理自证（Comprehension）**：你能用自己的话解释每一行改动为什么这么写，维护者追问细节时答得上来。
2. **测试自证（Testing Proof）**：在本地跑通相关测试与 lint，并在 PR 描述里给出真实复现/验证证据（命令输出或前后对比），不编造结果。
3. **最小范围（Minimal Scope）**：一个 PR 只解决一个问题，绝不顺手格式化无关文件、重命名变量或塞入未经请求的抽象。

## 3. 安全自检与漏洞披露

- **推送前必跑预检**：
  ```bash
  python <本技能目录>/scripts/validate_contribution.py . --base upstream/main
  ```
  新增行命中真实凭据或本机个人路径即 FAIL，必须先清理再推送。
- **若不慎把凭据推上了 PR**：贡献者无法删除上游仓库的 `refs/pull/*` 引用，**第一时间去对应平台吊销并轮换凭据**，再联系维护者清理。
- **发现目标项目安全漏洞**：绝不在公开 Issue 或 PR 讨论细节；先查目标仓库 `SECURITY.md`，优先走 GitHub Private Vulnerability Reporting（`Security & quality → Report a vulnerability`）。
