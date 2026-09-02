# 🤝 GitHub OSS Contribute / 开源贡献导航

<div align="center">

**从选 Issue 到 PR 被合并的全流程引导：先读懂仓库规则，再建立最小改动，用真实验证和持续责任赢得维护者信任。**

**End-to-end open-source contribution guide from issue scouting to merged PR — reconnaissance before coding with explicit write-action authorization.**

[![Validate](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-contribute?sort=semver)](https://github.com/hyt315/github-oss-contribute/releases/latest)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-contribute?style=social)](https://github.com/hyt315/github-oss-contribute/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

![GitHub OSS Contribute workflow: rules, issue, branch, build, pull request and review](assets/social-preview.png)

---

## 📖 这是什么？

高质量开源贡献不是“让 AI 改完代码直接提 PR 碰运气”。

**`github-oss-contribute`** 是一个专为开发者与 AI Agent 打造的专业级开源贡献指引技能。它将贡献者需要做的关键判断前置到编码之前：目标项目是否接受此类改动、Issue 是否已被其他贡献者认领、仓库有哪些本地 CI 与 Rulesets 规则、如何进行真实验证、维护者希望如何沟通——并在**每一个外部写操作前执行严格的授权确认**。

从 **仓库侦察 → 选题定位 → 本地开发 → PR 提交 → CI 诊断与 Review 处理 → 合并复盘**，全流程六阶段保驾护航。

---

## ✨ 核心特性

| 核心阶段 | 覆盖功能与操作 | 带来价值与质量门禁 |
|---|---|---|
| 🔍 **Phase 1: 仓库侦察** | 读取 README、CONTRIBUTING、Rulesets、CI 矩阵、DCO/CLA 与 AI Policy | 不臆测不存在的规则，100% 摸清项目红线 |
| 🎯 **Phase 2: 选题定位** | 评估 Issue 范围、复现难度、活跃度与认领状态 | 大改先沟通，绝不抢他人已认领的 Issue |
| 🛠️ **Phase 3: 本地开发** | 建议规范分支、最小改动方案、真实自测、GPG 签名与 AI 披露 | 不动无关代码，严禁伪造测试结果 |
| 📤 **Phase 4: PR 提交** | 按仓库模板起草清晰标题、问题背景、测试证据与风险评估 | 每一条 PR 创建、评论与推送均需用户明确授权 |
| 🩺 **Phase 5: CI 与 Review** | 读取失败日志定位根因、逐条处理 Maintainer 与 Bot Reviewer 反馈 | 不刷屏、不催促，诚实给出修改证据 |
| 🏆 **Phase 6: 合并复盘** | 清理本地与远程分支、复盘贡献收获、探索下一个可贡献任务 | 建立长期良好的开源开发者信誉 |

---

## 📊 开源贡献六阶段全流程架构

```
[输入: 用户想要给某个开源项目贡献代码]
                         │
      [Phase 1: 目标仓库深度侦察] ──> 贡献准则 / AI 策略 / DCO 协议 / 活跃度
                         │
      [Phase 2: 选题评估与先沟通] ──> 匹配 good first issue，判断是否已被认领
                         │
      [Phase 3: 本地最小改动开发] ──> 规范分支 / 单元测试实跑 / 保持最小侵入
                         │
      [Phase 4: 规范化提 PR 交付] ──> 附带复现与测试证据 / 需用户显式授权
                         │
      [Phase 5: CI 诊断与 Review] ──> 诊断红标 CI / 逐条处理维护者与 Bot 反馈
                         │
      [Phase 6: 合并后复盘与清理] ──> 分支收尾，沉淀开源信誉与后续选题
```

---

## 📚 实战案例演示

三个端到端可复核实战案例，详见 [examples/README.md](examples/README.md)：
1. [第一次贡献：先侦察再选 Issue](examples/README.md#示例一第一次贡献)
2. [CI 失败：从日志定位到最小修复](examples/README.md#示例二ci-失败诊断)
3. [Review 反馈：更新代码并给出证据](examples/README.md#示例三处理-review-反馈)

---

## 🚀 快速开始

这是一个标准的 AI Agent Skill —— 安装到你的 AI 助手后即可直接使用。

### 方式 A：把一句话发给任意 Agent（最推荐、最通用）

把下面这段话直接复制发送给你的 AI 助手，它会自动完成安装：

> 请安装 github-oss-contribute 技能：克隆 `https://github.com/hyt315/github-oss-contribute` 到你的 skills 目录（如 `~/.claude/skills/github-oss-contribute`、`~/.agents/skills/github-oss-contribute` 或 `~/.cursor/skills/github-oss-contribute`），并确认安装成功。以后我要「找开源 Issue 贡献 / 提 PR / 处理 CI 失败或 review 意见」时，按 SKILL.md 的六阶段流程引导我完成。

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
python scripts/selftest.py
```

---

## 🔒 权限边界与安全原则

- **侦察无需任何 Token**：公开仓库的只读规则分析与代码阅读无需凭据；
- **写操作分阶段授权**：Fork 仓库、提交 Issue 评论、向远程 Push 分支、创建 PR 均需用户明确批准；
- **真实透明原则**：严禁伪造测试通过结果，遵守目标仓库的 AI 生成代码披露准则。

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

## 📁 文件结构

```
github-oss-contribute/
├── SKILL.md                          # 核心技能定义与六阶段贡献工作流
├── README.md                         # 中文说明文档
├── README.en.md                      # 英文说明文档
├── CHANGELOG.md                      # 版本发布记录
├── LICENSE                           # MIT 开源许可证
├── .gitignore                        # Git 忽略规则
├── CONTRIBUTING.md                   # 社区贡献指南
├── CODE_OF_CONDUCT.md                # 行为准则
├── SECURITY.md                       # 安全策略
├── SUPPORT.md                        # 支持渠道
├── manifest.json                     # 技能元数据清单
├── agents/                           # 多 Agent 平台元数据
├── examples/README.md                # 三个可复核的端到端案例
├── scripts/
│   ├── validate-skill.mjs            # 技能自检器
│   ├── validate_repo.py              # 结构与隐私安全验证器
│   └── selftest.py                   # 自动化回归自测脚本
└── references/                       # 侦察方法、PR 模板与 Review 指南
```

---

## ❓ 常见问题 (FAQ)

- **Q: 刚开始给大项目贡献代码，会不会被维护者拒绝？**  
  A: 技能在 Phase 1~2 会引导你先阅读 CONTRIBUTING 并选择标记有 `good first issue` 的任务，避免因不熟悉规范而被无情拒绝。
- **Q: PR 里的 CI 自动化测试红了怎么办？**  
  A: 技能在 Phase 5 会自动帮你抓取 CI 报错日志，定位具体报错行，并指导你编写针对性的最小修复代码。
- **Q: 它会擅自帮我直接把代码推送到别人的仓库吗？**  
  A: 绝不会。所有对外部的写操作（Fork、Push、PR）都严格处于用户确认门禁之内。

---

## 🤝 参与贡献

欢迎提交 Issue 与 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。如果这个技能对你有帮助，欢迎在 GitHub 上点个 [Star ⭐](https://github.com/hyt315/github-oss-contribute/stargazers)！

---

## 📄 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

---

> 🌏 **English: [README.en.md](./README.en.md)**
