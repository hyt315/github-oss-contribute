<div align="center">

# 🤝 GitHub OSS Contribute / 开源贡献导航

**从选 Issue 到 PR 被合并的全流程引导：先读懂仓库规则，再建立最小改动，用真实验证和持续责任赢得信任。**

**简体中文 · [English](./README.en.md)**

[![Validate](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-contribute?sort=semver)](https://github.com/hyt315/github-oss-contribute/releases)
[![Downloads](https://img.shields.io/github/downloads/hyt315/github-oss-contribute/total)](https://github.com/hyt315/github-oss-contribute/releases)
[![Contributors](https://img.shields.io/github/contributors/hyt315/github-oss-contribute)](CONTRIBUTORS.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/hyt315/github-oss-contribute?style=social)](https://github.com/hyt315/github-oss-contribute/stargazers)

</div>

![GitHub OSS Contribute workflow: rules, issue, branch, build, pull request and review](assets/social-preview.png)

---

## 📖 这是什么？

高质量开源贡献不是"让 AI 改完直接提 PR"。**GitHub OSS Contribute** 是一个 AI Agent Skill，把贡献者需要做的判断放到编码之前：项目是否接受这类改动、Issue 是否已被认领、仓库有哪些本地规则、怎样验证、维护者希望如何交流——并在**每个外部动作前明确权限边界**。六阶段全程引导：仓库侦察 → 选题 → 准备 → 开发 → 提交 → 跟踪（CI 诊断、Review 处理、等待策略、直到合并）。

### ✨ 核心特性

| 阶段 | Skill 会做什么 | 质量门禁 |
| --- | --- | --- |
| 仓库侦察 | 读取 README、CONTRIBUTING、AGENTS、**Rulesets**、CI、模板、DCO/CLA 和 AI policy | 不臆测不存在的规则 |
| 选择 Issue | 评估范围、复现性、活跃度、认领状态和维护者意图 | 大改先沟通，不抢已认领 Issue |
| 本地开发 | 建议分支、最小改动、测试与提交方案、**签名与 AI 披露** | 不动无关文件，不伪造测试结果 |
| PR 提交 | 生成清晰标题、问题/方案/验证/风险说明 | 创建 PR、评论和推送需用户授权 |
| CI 与 Review | 读取失败日志、定位根因、逐条处理反馈（含 **Bot Reviewer**） | 不刷屏、不催促、不隐藏 AI 使用 |
| 合并后 | 清理分支、复盘、寻找下一项贡献 | 不把一次合并当成维护者授权 |

---

## 📚 示例：三个可复核的端到端案例

1. [第一次贡献：先侦察再选 Issue](examples/README.md#示例一第一次贡献)
2. [CI 失败：从日志定位到最小修复](examples/README.md#示例二ci-失败诊断)
3. [Review 反馈：更新代码并给出证据](examples/README.md#示例三处理-review-反馈)

---

## 🚀 快速开始

> ✨ **一句话装进 AI Agent**：把下面这段话直接发给你的 AI 助手，它会自动完成安装——
>
> ```text
> 请安装 github-oss-contribute Skill：把 https://github.com/hyt315/github-oss-contribute 克隆到你的 skills 目录（Claude Code：~/.claude/skills/github-oss-contribute/；Codex：~/.agents/skills/github-oss-contribute/；Cursor：~/.cursor/skills/github-oss-contribute/），并确认 SKILL.md、references/、scripts/ 都在。以后我要「找开源 Issue 贡献 / 提 PR / 处理 CI 失败或 review 意见」时，按 SKILL.md 的六阶段流程引导我完成。
> ```

| 平台 | 用户级安装 |
| --- | --- |
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute` |
| **Codex / ChatGPT** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute` |

> 项目级安装把路径换成 `.claude/skills/`、`.agents/skills/`、`.cursor/skills/`（项目根目录）。新安装未发现时重启对应 Agent。

---

## 💬 触发方式

对 AI 说以下任意一类话，即会触发本技能：

- 「我想给开源项目做贡献」「找个 good first issue」
- 「帮我提个 PR」「第一次贡献要注意什么」
- 「我的 PR 的 CI 红了」「PR 被拒了怎么办」「review 意见怎么回」

## ⚙️ 前置条件

- **Git** 已安装（提交前核对仓库级 user.name / user.email）
- 公开仓库的侦察**无需任何认证**；只有 Fork / 评论 / Push / 建 PR 时才需要 GitHub 写入能力（官方连接、`gh`、MCP OAuth、fine-grained PAT 或网页手动操作，按此优先级）
- 不要求把 Token 发到聊天；认证不可用时只读侦察与本地工作照常进行，只暂停被阻塞的外部写入

## 📦 输出交付物

```text
📋 仓库侦察报告   —— 贡献规则/活跃度评级/AI Policy/DCO-CLA/注意事项
🎯 选题建议       —— 候选 Issue 评分 + 认领状态 + 先沟通草稿
🛠️ 开发与提交方案 —— 分支命名/最小改动/Commit 规范/签名与披露
📤 高质量 PR      —— 标题/描述/测试证据/AI 披露（按仓库模板）
🩺 CI 与 Review   —— 失败根因定位/逐条反馈处理/等待期策略/Merge Queue 说明
```

---

## 📥 下载 / 安装

```bash
# HTTPS
git clone https://github.com/hyt315/github-oss-contribute.git

# SSH
git clone git@github.com:hyt315/github-oss-contribute.git

# GitHub CLI
gh repo clone hyt315/github-oss-contribute

# ZIP
# https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.zip

# 单文件（仅 SKILL.md）
curl -O https://raw.githubusercontent.com/hyt315/github-oss-contribute/main/SKILL.md
```

---

## 📁 文件结构

```
github-oss-contribute/
├── SKILL.md                        # 技能入口（六阶段工作流）
├── references/
│   ├── ai-slop-guide.md            # 反 AI Slop 深度指南
│   ├── commit-conventions.md       # Commit 规范/DCO/签名
│   ├── communication-etiquette.md  # Review 沟通模板
│   ├── first-timer-tips.md         # 首次贡献者技巧与平台
│   ├── git-errors.md               # Git 报错速查表
│   ├── mcp-tools.md                # GitHub 能力映射与回退
│   └── security-guide.md           # 安全实践与泄露应急
├── scripts/
│   ├── validate-skill.mjs          # 结构校验（CI 用）
│   └── selftest.py                 # 回归测试（好夹具绿 + 负向被抓）
├── examples/README.md              # 三个端到端示例
├── agents/openai.yaml
├── LICENSE / CHANGELOG.md
├── README.md  /  README.en.md     # 双语说明（本文件为中文）
└── .github/                        # Issue/PR 模板 + CI(validate)
```

---

## ▶️ 快速使用

六阶段各自独立可用——你可能只卡在某个环节：

1. **侦察**：给出 `owner/repo`，产出仓库侦察报告（规则/活跃度/Rulesets/AI Policy）
2. **选题**：搜索并评估候选 Issue，输出选题建议与沟通草稿
3. **准备**：Fork → Clone → upstream → 功能分支 → 本地环境
4. **开发**：质量自检清单 → 安全实践 → Commit 规范 → 与上游同步
5. **提交**：push（含 force-with-lease 边界）→ 建 PR → 验证文件列表
6. **跟踪**：CI 诊断（含 Merge Queue）→ Review 处理（含 Bot Reviewer）→ 等待策略 → 合并后清理

---

## 🤝 贡献 / 反馈

- 报 Bug / 提建议：用仓库的 Issue 模板
- 贡献：见 [CONTRIBUTING.md](CONTRIBUTING.md)，改动前跑 `python scripts/selftest.py` 与 `node scripts/validate-skill.mjs`
- 漏洞报告：见 [SECURITY.md](SECURITY.md)（私有漏洞报告，勿走公开 Issue）

---

## 📜 License

[MIT](LICENSE) © 2026 hyt315

> 🌏 **English version: [README.en.md](./README.en.md)**