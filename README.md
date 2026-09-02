# 🚀 GitHub OSS Contribute / 开源贡献导航

<div align="center">

**面向全球开发者的开源贡献全程智能导航：从选 Issue 到 PR 成功合并，涵盖 Fork 同步、Rebase 冲突消解、DCO 签名、反 AI Slop 质量自检与 CI 诊断。**

**Interactive end-to-end guide for open-source contributors — from finding issues to getting PRs merged, featuring Git conflict resolution, DCO signing, anti-AI slop quality gates, and CI diagnosis.**

[![Validate](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-contribute?sort=semver)](https://github.com/hyt315/github-oss-contribute/releases/latest)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-contribute?style=social)](https://github.com/hyt315/github-oss-contribute/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

![GitHub OSS Contribute workflow: recon, select issue, prepare fork, develop with DCO, submit PR, and track to merge](assets/social-preview.png)

---

## 📖 这是什么？

想参与开源项目，却常常被这些现实门槛阻挡？
- 找到心仪的项目，不知道如何挑选适合新手的 `good first issue`，甚至留言认领后迟迟没有回音；
- 在本地开发时直接把代码写在 `main` 分支上，当上游更新后产生复杂冲突（Merge Conflicts）手足无措；
- 提交 PR 后，因为忘记加 `-s` 导致 CNCF/Linux 项目的 `DCO Check Failed` 亮红标；
- 借助 AI 辅助写代码，却因提交了无实质价值的格式微调或无法自证原理，被维护者误判为“AI 垃圾（AI Slop）”遭到拒审；
- CI 挂了不知如何看日志排查，收到刁钻的 Review 意见不知如何得体回应。

**`github-oss-contribute`** 是一个专为开源贡献者打造的 **AI 全程导航元技能**。它从贡献者视角出发，覆盖从 **侦察规则 → 选题认领 → Fork 与分支隔离 → 编码与 DCO 签名 → 高质量 PR 提交 → CI 诊断与 Review 协同** 的六大完整阶段，帮助你以最受维护者欢迎的专业姿态完成开源贡献！

---

## ✨ 核心特性

| 贡献阶段 | 覆盖功能与操作 | 带来价值与质量门禁 |
|---|---|---|
| 🔍 **Phase 1: 侦察与规则对齐** | 深度分析目标仓库的 CONTRIBUTING、Rulesets 分支保护、Merge Queue 与 AI 贡献政策 | 告别盲目提交，精准对齐社区维护习惯 |
| 🎯 **Phase 2: 选题与认领意向** | 智能检索 `good first issue`，提供中英文礼貌认领文案，防范公开泄露漏洞 | 避免重复劳动，建立良好的第一印象 |
| 🍴 **Phase 3: Fork 与分支隔离** | 配置 `upstream` 远程仓库、创建独立特性分支、**Rebase 冲突消解四步法** | 保持主干干净，轻松解决代码冲突 |
| 💻 **Phase 4: 编码与 DCO 签名** | Conventional Commits 规范、**DCO (`-s`) 签署与批量补签**、`gpg.format ssh` 签名 | 轻松通过自动化开源许可与签名门禁 |
| 📝 **Phase 5: 反 AI Slop PR 提交** | **反 AI Slop 三大自证（原理自证/测试自证/最小改动）**、PR 模板与前后对比证据 | 提交高通过率、有说服力的高质量 PR |
| 🚦 **Phase 6: CI 诊断与 Review 协同** | Actions 报错四步排查、Flaky Test 对比、Review 意见礼貌回复与温和催单策略 | 陪伴直至代码成功合并 (Merged) |

---

## 📊 开源贡献六阶段全程架构

```
[输入: 用户指示想要参与开源 / 挑选 Issue / 提交 PR / 解决冲突 / 回复 Review]
                                       │
     [Phase 1: 仓库侦察与规则对齐] ────> 读 references/mcp-tools.md 与 security-guide.md
                                       │
     [Phase 2: 选题与留言认领] ────────> 读 references/first-timer-tips.md 与 communication-etiquette.md
                                       │
     [Phase 3: Fork 与分支隔离] ───────> 读 references/git-fork-and-conflict-guide.md (Upstream + Rebase)
                                       │
     [Phase 4: 编码自测与 DCO 签名] ───> 读 references/commit-conventions.md 与 dco-cla-and-signing.md
                                       │
     [Phase 5: 高质量 PR 证据闭环] ────> 读 references/ai-slop-guide.md (反 AI Slop 三大自证准则)
                                       │
     [Phase 6: 跟踪、CI 诊断与合并] ───> 读 references/ci-troubleshooting.md 与 git-errors.md
```

---

## 🛡️ 2026 AI 辅助贡献伦理与反 AI Slop 自检

为了保护开源生态的纯洁性，并确保你的 PR 快速被维护者合并，提交前必须满足 **三大自证铁律**：

```
                    ┌──────────────────────────────────────────────┐
                    │    2026 贡献者 Human-in-the-Loop 自检三大铁律 │
                    └──────────────────────┬───────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
【1. 原理自证 (Comprehension)】    【2. 测试自证 (Testing Proof)】     【3. 最小范围 (Minimal Scope)】
 • 能清晰解释每一行代码设计考量    • 本地终端完整跑通新增单测断言      • 拒绝顺带做格式化/重命名
 • 维护者提问能给出充分技术回答    • 提供前后对比结果或动图证据        • 保持 PR Diff 极简与聚焦
```

---

## 📚 实战案例演示

三个端到端可复核实战案例，详见 [examples/README.md](examples/README.md)：
1. [从零开始的第一次文档修正](examples/README.md#示例一第一次贡献文档微调)
2. [Bug 修复与 CI 失败排查](examples/README.md#示例二bug-修复与-ci-排查)
3. [处理 Review 意见并完成合并](examples/README.md#示例三处理-review-意见并合并)

---

## 🚀 快速开始

这是一个标准的 AI Agent Skill —— 安装到你的 AI 助手后即可直接使用。

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

把下面这段话直接复制发送给你的 AI 助手，它会自动完成安装：

> 请安装 github-oss-contribute 技能：克隆 `https://github.com/hyt315/github-oss-contribute` 到你的 skills 目录（如 `~/.claude/skills/github-oss-contribute`、`~/.agents/skills/github-oss-contribute` 或 `~/.cursor/skills/github-oss-contribute`），并确认安装成功。以后我要「参与开源项目 / 找 Issue / 提 PR / 解决 Git 冲突 / 配置 DCO 签名 / 应对 Review」时，按 SKILL.md 的流程引导我完成。

### 方式 B：GitHub CLI 2.90+（一行命令）

```bash
gh skill install hyt315/github-oss-contribute github-oss-contribute --agent claude-code --scope user
```

### 方式 C：多平台手动安装

| 平台 | 用户级安装路径 | 项目级安装路径 |
|---|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute` | `.claude/skills/github-oss-contribute` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` | `.agents/skills/github-oss-contribute` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute` | `.cursor/skills/github-oss-contribute` |
| **通用 Agents** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` | `.agents/skills/github-oss-contribute` |

### 方式 D：本地运行回归自测

```powershell
# 运行结构校验
node scripts/validate-skill.mjs

# 运行自动化回归自测
python scripts/selftest.py

# 用 skill-doctor 审查
python path/to/skill-doctor/scripts/audit.py . --dynamic
```

---

## 🔒 权限与安全原则

- **严格只读默认**：侦察公开仓库无需任何 Token，仅分析公开数据并提供操作指导；
- **确认门禁保护**：所有 Fork、Push、创建 PR 等外部写操作，必须经用户确认后执行；
- **凭据零采集**：绝不在聊天中索取 Token，绝不修改全局 Git 凭据配置；
- **安全防泄露**：提交前自动扫描代码，严防私有密钥或未披露的 0-day 漏洞泄露。

---

## 📥 下载与获取

| 方式 | 命令 / 链接 |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-contribute.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-contribute.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-contribute` |
| **ZIP 压缩包** | [下载 ZIP](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.zip) |
| **Tar 归档** | [下载 Tar](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.tar.gz) |
| **单文件 (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-contribute/main/SKILL.md` |

---

## 📖 深度参考手册导读

| 参考文档 | 核心内容 | 推荐阅读时机 | 预估耗时 |
|---|---|---|---|
| 🍴 [**Fork 与冲突消解指南 (`git-fork-and-conflict-guide.md`)**](references/git-fork-and-conflict-guide.md) | Upstream 配置、分支隔离与 Rebase 冲突消解四步法 | 准备开发分支或遇到 Git 冲突时 | 4 分钟 |
| ✍️ [**DCO、CLA 与签名指南 (`dco-cla-and-signing.md`)**](references/dco-cla-and-signing.md) | DCO `-s` 签署、批量补签名命令与 SSH Commit 签名 | 提交代码或被 DCO 检查拦截时 | 4 分钟 |
| 🛡️ [**反 AI Slop 质量准则 (`ai-slop-guide.md`)**](references/ai-slop-guide.md) | 2026 贡献者三大自证铁律（原理/测试/最小范围）与 PR 描述规范 | 起草 PR 描述与提交前自检时 | 4 分钟 |
| 🚦 [**CI 失败自诊断指南 (`ci-troubleshooting.md`)**](references/ci-troubleshooting.md) | Actions 报错定位、本地复现与 Flaky Test 处理 | PR 的 GitHub Actions 亮红标时 | 4 分钟 |
| 💬 [**沟通与礼仪模板 (`communication-etiquette.md`)**](references/communication-etiquette.md) | 认领 Issue、回复 Review 意见与温和催单中英文文案 | 与维护者沟通交流时 | 3 分钟 |
| 📋 [**Commit 规范 (`commit-conventions.md`)**](references/commit-conventions.md) | Conventional Commits 常用类型与 Angular 规范示例 | 编写提交信息时 | 3 分钟 |
| 💡 [**首次贡献技巧 (`first-timer-tips.md`)**](references/first-timer-tips.md) | 寻找优质新手任务（good first issue）与评估仓库活跃度 | 寻找适合的开源项目时 | 3 分钟 |
| 🔧 [**Git 错误速查 (`git-errors.md`)**](references/git-errors.md) | 常见 Git 报错排查速查表与一键修复命令 | 遇到本地 Git 报错时 | 3 分钟 |
| 🔑 [**MCP 工具与 API 映射 (`mcp-tools.md`)**](references/mcp-tools.md) | 平台 MCP 工具与公开 REST API 回退方案 | 调用平台能力时 | 3 分钟 |
| 🔒 [**安全检查指南 (`security-guide.md`)**](references/security-guide.md) | 敏感凭据防泄露检查与应急处理 | 提交前安全自检时 | 3 分钟 |

---

## 📁 文件结构

```
github-oss-contribute/
├── SKILL.md                          # 核心技能定义、渐进式调度中枢与 6 大贡献阶段
├── README.md                         # 中文说明文档
├── README.en.md                      # 英文说明文档
├── CHANGELOG.md                      # 版本发布记录
├── LICENSE                           # MIT 开源许可证
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 社区贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── CONTRIBUTORS.md                   # 贡献者名单
├── manifest.json                     # 技能元数据清单
├── agents/                           # 多 Agent 平台元数据
├── assets/                           # 门面配图与预览图
├── examples/                         # 三大实战案例
├── scripts/
│   ├── validate-skill.mjs            # 结构与安全校验脚本
│   └── selftest.py                   # 自动化回归自测脚本
└── references/                       # 10 本深度贡献手册
    ├── git-fork-and-conflict-guide.md # Upstream 配置与 Rebase 冲突消解
    ├── dco-cla-and-signing.md        # DCO 签署、补签与 SSH Commit 签名
    ├── ai-slop-guide.md              # 2026 贡献者三大自证与反 AI Slop 准则
    ├── ci-troubleshooting.md         # CI 报错四步排查与 Flaky 处理
    ├── communication-etiquette.md    # 认领、Review 与催单全场景文案
    ├── commit-conventions.md         # Conventional Commits 规范
    ├── first-timer-tips.md           # 首次贡献技巧与 Issue 挑选
    ├── git-errors.md                 # 常见 Git 报错速查表
    ├── mcp-tools.md                  # MCP 工具映射与 API 回退
    └── security-guide.md             # 敏感凭据安全防泄露
```

---

## ❓ 常见问题 (FAQ)

- **Q: 为什么提交 PR 必须配置 upstream 而不是直接在 local main 开发？**  
  A: 如果直接在 local main 开发，一旦上游仓库更新，你的 main 分支就会与官方主干历史发生分叉和混乱。创建独立的 `feat/xxx` 特性分支，可使主干随时保持与官方同步，变基（Rebase）冲突处理更加清晰。
- **Q: 为什么我的 PR 被 DCO 拦截了？该怎么补救？**  
  A: CNCF 和 Linux 等项目要求每个 commit 必须带 `Signed-off-by` 签名。运行 `git commit --amend -s --no-edit` 即可为最近的 commit 补签名，然后 `git push --force-with-lease` 刷新 PR。
- **Q: 借助 AI 辅助写代码提交开源，会被维护者判定为违规吗？**  
  A: 绝大多数项目欢迎高质量的贡献，无论是否借助 AI。但维护者反感的是“未经测试、自己都看不懂的无脑搬运代码（AI Slop）”。只要做到**原理自证、提供测试断言、遵守最小改动范围**，你的 PR 会极受欢迎！

---

## 🤝 参与贡献

欢迎提交 Issue 与 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。如果这个技能对你有帮助，欢迎在 GitHub 上点个 [Star ⭐](https://github.com/hyt315/github-oss-contribute/stargazers)！

---

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

---

> 🌏 **English: [README.en.md](./README.en.md)**
