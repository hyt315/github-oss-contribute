---
name: github-oss-contribute
version: 2.0.0
description: |
  开源贡献全程智能导航：从选择 Issue 到 PR 成功合并的全流程引导。
  自动分析目标仓库规则（CONTRIBUTING、CI、Rulesets、AI Policy），
  提供 Fork/Clone/Branch 特性分支隔离、PR 质量自检（反 AI Slop）、DCO 签名、
  CI 失败诊断、Review 反馈处理与合并跟踪。支持官方 GitHub 连接、MCP、CLI 与网页回退。
  触发词：开源贡献、第一次贡献、提 PR、first contribution、contribute、找个 issue 做、提交 PR、PR 被拒了怎么办、CI 红了、review 意见。
---

# 开源贡献导航

从选题到 PR 合并的全流程贡献助手。面向贡献者视角，与 oss-prep（建项目）、oss-ops（管项目）形成完整的开源协作工具链闭环。

## 核心理念与铁律

- **贡献者视角**：帮助开发者以标准贡献者身份参与全球开源协作，遵守目标项目的维护规范；
- **渐进式披露原则（Progressive Disclosure）**：本入口作为总控调度器，具体各阶段详细决策、Git 冲突消解、DCO 签署、沟通模板，严格按需调阅对应的深度参考手册；
- **动态适配仓库规则**：优先遵循目标仓库根目录及改动路径下的 AGENTS.md、CONTRIBUTING.md、Rulesets 分支保护、DCO/CLA 与 AI Policy 要求；
- **质量优先与反 AI Slop**：坚持原理自证、测试自证与最小改动范围，拒绝无意义的格式微调与刷绿点提交；
- **读写分离与安全防泄露**：公开信息分析直接进行；Fork、Push、创建或更新 PR 必须获得用户明确确认；绝不提交私有密钥或未公开漏洞；
- **纯 Python 标准库零依赖**：辅助验证脚本严格基于 Python 3.10+ 标准库开发，100% 零第三方依赖、纯只读。

---

## 运行模式与授权优先级

公开仓库的规则分析、Issue 搜索与代码阅读无需任何 Token。只有在执行 Fork、Push 或创建 PR 时才需要 GitHub 授权。按以下优先级使用：

1. **平台官方 GitHub 连接器或 GitHub 官方远程 MCP（OAuth）**：由受信任界面完成授权；
2. **已认证的 GitHub CLI**：先运行 `gh auth status`，未登录时引导用户运行 `gh auth login --web`；
3. **GitHub 官方本地 MCP Server**：适合需要本地宿主或受控 toolsets 的环境；
4. **Fine-grained PAT**：仅在用户明确选择时使用，限定最小权限仓库与有效期，安全读取；
5. **公开 REST API / 网页**：作为只读或人工交接回退。

能力映射与回退方式详见 [references/mcp-tools.md](references/mcp-tools.md)。

---

## Reference Files

九本深度参考手册承载本技能的核心贡献资产。以下时机必须读取对应文件：

- Phase 1 侦察与规则时，先读 [references/mcp-tools.md](references/mcp-tools.md) 与 [references/security-guide.md](references/security-guide.md)：MCP 工具调用与敏感凭据防泄露检查；
- Phase 2 选题与认领时，先读 [references/first-timer-tips.md](references/first-timer-tips.md) 与 [references/communication-etiquette.md](references/communication-etiquette.md)：寻找适合的 Issue 与认领申请模板；
- Phase 3 Fork 与分支时，先读 [references/git-fork-and-conflict-guide.md](references/git-fork-and-conflict-guide.md)：Upstream 配置、特性分支隔离与 Rebase 冲突消解；
- Phase 4 编码与签名时，先读 [references/commit-conventions.md](references/commit-conventions.md) 与 [references/dco-cla-and-signing.md](references/dco-cla-and-signing.md)：Conventional Commits、DCO `-s` 签署与 `gpg.format ssh` 签名；
- Phase 5 提交前自检时，先读 [references/ai-slop-guide.md](references/ai-slop-guide.md)：反 AI Slop 三大自证铁律（原理、测试、最小范围）与 PR 描述规范；
- Phase 6 跟踪与协同修复时，先读 [references/ci-troubleshooting.md](references/ci-troubleshooting.md) 与 [references/git-errors.md](references/git-errors.md)：GitHub Actions 日志排查、Git 报错速查与 Review 意见处理。

---

## 贡献工作流程

```
Phase 1: 侦察 ──> 分析目标仓库规则、Rulesets、AI Policy、Merge Queue 与 Bot Reviewer
    ↓
Phase 2: 选题 ──> 筛选 good first issue，与维护者确认意向，排查 Private vulnerability reporting 避免公开讨论漏洞
    ↓
Phase 3: 准备 ──> Fork 仓库、配置 upstream remote、创建专属特性分支
    ↓
Phase 4: 开发 ──> 编码自测、反 AI Slop 自检、Conventional Commits 规范与 DCO/SSH 签名
    ↓
Phase 5: 提交 ──> 填写 PR 模板、关联 Fixes #123、附带充分测试与前后对比证据
    ↓
Phase 6: 跟踪 ──> CI 失败排查、Rebase 冲突消解、处理 Review 意见并跟进合并
```

---

## Phase 1: 侦察 — 分析目标仓库
先读 [references/mcp-tools.md](references/mcp-tools.md) 与 [references/security-guide.md](references/security-guide.md)，分析目标仓库的 CONTRIBUTING、Rulesets 分支保护、Merge Queue、Bot Reviewer 与 AI 贡献政策。

## Phase 2: 选题 — 寻找适合的 Issue
先读 [references/first-timer-tips.md](references/first-timer-tips.md) 与 [references/communication-etiquette.md](references/communication-etiquette.md)，筛选适合的待办任务，礼貌留言认领。若涉及安全漏洞需通过 Private vulnerability reporting 私有通道提报。

## Phase 3: 准备 — Fork 与分支隔离
先读 [references/git-fork-and-conflict-guide.md](references/git-fork-and-conflict-guide.md)，配置 `upstream` 远程仓库，从主干创建独立的 `feat/xxx` 或 `fix/xxx` 特性分支。

## Phase 4: 开发 — 编码、自测与 DCO 签名
先读 [references/commit-conventions.md](references/commit-conventions.md) 与 [references/dco-cla-and-signing.md](references/dco-cla-and-signing.md)，编写最小修改代码，执行本地自测，配置 `gpg.format ssh` 与 `git commit -s` 签名。

## Phase 5: 提交 — 高质量 PR 与证据闭环
先读 [references/ai-slop-guide.md](references/ai-slop-guide.md)，执行反 AI Slop 自检（原理自证、测试自证），规范填写 PR 模板并附带测试证据。

## Phase 6: 跟踪 — CI 诊断、Review 协同与合并
先读 [references/ci-troubleshooting.md](references/ci-troubleshooting.md) 与 [references/git-errors.md](references/git-errors.md)，排查 Actions 失败日志，协同消解变基冲突，礼貌回复维护者意见。

---

## 质量门禁与自测

- **改动本技能后**：运行 `node scripts/validate-skill.mjs` 做结构校验，运行 `python scripts/selftest.py` 做回归测试；
- **全维度静态审计**：运行 `python <skill-doctor>/scripts/audit.py . --dynamic` 确保 39 项规则 100% 全绿通过。
