# 🚀 开源贡献导航 / OSS Contribute Guide

<div align="center">

**从选 Issue 到 PR 被合并的全流程 AI 贡献助手，帮你高质量参与开源项目**

**End-to-end AI contribution navigator — from picking an Issue to getting your PR merged**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.1-green.svg)]()
[![SKILL.md](https://img.shields.io/badge/Agent%20Skill-SKILL.md-green)](SKILL.md)

[English](#english) | [中文](#中文)

</div>

---

## 中文

## 📖 这是什么？

**开源贡献导航** 是一个 AI Agent Skill，专为想参与开源贡献的人设计。它自动分析目标仓库的规则（CONTRIBUTING、CI、分支保护、AI 策略），提供 Fork/Clone/Branch 操作指导，并在 PR 质量自检（反 AI Slop）、CI 失败诊断、Review 反馈处理等关键环节给出实时建议。

### ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎯 **智能选 Issue** | 自动分析目标仓库，帮你找到适合新手贡献的 Issue |
| 📋 **规则适配** | 读取目标仓库的 CONTRIBUTING.md、CI 配置、分支保护规则，动态调整建议 |
| 🛡️ **反 AI Slop** | PR 质量自检清单，确保贡献不被当成低质量 PR 秒拒 |
| 🔧 **CI 诊断** | CI 红了不慌，自动分析失败原因并给出修复建议 |
| 💬 **Review 处理** | 针对 Review 反馈给出具体回复建议，提高合并率 |
| 🌐 **MCP 自动化** | 支持 GitHub MCP 工具直接执行 Fork、创建 PR 等操作 |

---

## 🚀 快速开始

这是一个 AI Agent Skill，安装到任意 AI 编程助手后即可使用。

### 它能做什么？

一句话：**帮你以贡献者身份高质量参与开源项目。** 从选 Issue 开始，全程引导 Fork、分支管理、提交规范、PR 创建、CI 修复、Review 回复，直到 PR 被合并。

### 典型使用场景

- 想参与开源但不知道从哪开始 — 它帮你分析仓库、推荐适合的 Issue
- 提了 PR 被 CI 红了 — 它自动分析失败原因并给出修复方案
- 收到 Review 意见不知道怎么回 — 它生成专业回复草稿
- 不确定自己的 PR 质量够不够 — 它用反 AI Slop 清单帮你自检

### 怎么用

安装后直接告诉 AI 助手你想贡献哪个项目，Skill 会自动执行 **选 Issue → Fork/Clone → Branch → 编码 → 提交 → 创建 PR → CI 修复 → Review 回复 → 合并** 全流程引导。

---

## 📥 安装 / Installation

### 一行命令安装

| 平台 | 安装命令 |
|------|----------|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.codex/skills/github-oss-contribute` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute` |

> 安装后 Skill 会自动生效，无需额外配置。

---

## 📥 下载 / Download

### 源码下载

| 方式 | 命令 / 链接 |
|------|------------|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-contribute.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-contribute.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-contribute` |
| **ZIP 源码** | [下载 ZIP](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/master.zip) |
| **Tar 源码** | [下载 Tar](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/master.tar.gz) |

---

## 💡 核心理念

- **贡献者视角**：帮你以贡献者身份参与开源，而不是维护者
- **动态适配**：每个仓库规则不同，AI 实时分析目标仓库的具体要求
- **质量优先**：2025-2026 年 AI Slop 泛滥，确保贡献不被当成低质量 PR 秒拒
- **全程引导**：不只教怎么提 PR，还管 CI 红了、Review 意见、等待策略

---

## 📁 文件结构

```
github-oss-contribute/
├── SKILL.md                              # Skill 核心定义
├── README.md                             # 本文件
├── LICENSE                               # MIT 协议
├── .gitignore                            # Git 忽略规则
├── CONTRIBUTING.md                       # 贡献指南
├── CODE_OF_CONDUCT.md                    # 行为准则
├── SECURITY.md                           # 安全策略
├── .github/
│   ├── pull_request_template.md          # PR 模板
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.yml                # Bug 报告表单
│       ├── feature_request.yml           # 功能建议表单
│       ├── doc_improvement.yml           # 文档改进表单
│       └── config.yml                    # 模板选择器配置
└── references/                           # 参考文件
    ├── ai-slop-guide.md                  # 反 AI Slop 指南
    ├── commit-conventions.md             # 提交规范
    ├── communication-etiquette.md        # 沟通礼仪
    ├── first-timer-tips.md               # 新手建议
    ├── git-errors.md                     # Git 常见错误
    ├── mcp-tools.md                      # MCP 工具参考
    └── security-guide.md                 # 安全指南
```

---

## 🤝 贡献

请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 📄 许可

[MIT](LICENSE)

---

## English

## 📖 What is this?

**OSS Contribute Guide** is an AI Agent Skill designed for anyone who wants to contribute to open-source projects. It automatically analyzes the target repository's rules (CONTRIBUTING, CI, branch protection, AI policy), guides you through Fork/Clone/Branch operations, and provides real-time advice on PR quality checks (anti-AI Slop), CI failure diagnosis, and Review feedback handling.

### ✨ Core Features

| Feature | Description |
|---------|-------------|
| 🎯 **Smart Issue Picking** | Analyzes the target repo and finds beginner-friendly Issues |
| 📋 **Rule Adaptation** | Reads the repo's CONTRIBUTING.md, CI config, and branch protection rules to dynamically adjust advice |
| 🛡️ **Anti-AI Slop** | PR quality checklist to ensure your contribution isn't rejected as low-quality |
| 🔧 **CI Diagnosis** | Automatically analyzes CI failures and suggests fixes |
| 💬 **Review Handling** | Generates professional reply drafts for Review feedback |
| 🌐 **MCP Automation** | Supports GitHub MCP tools to directly execute Fork, create PR, and more |

---

## 🚀 Quick Start

This is an AI Agent Skill — install it in any AI coding assistant and it's ready to use.

### What it does

In one sentence: **helps you contribute to open-source projects with high quality.** From picking an Issue to Fork, branch management, commit conventions, PR creation, CI fixes, Review replies — full workflow guidance until your PR is merged.

### Common use cases

- Want to contribute to open-source but don't know where to start — it analyzes repos and recommends suitable Issues
- Your PR failed CI — it analyzes the failure and suggests fixes
- Received Review feedback and don't know how to reply — it generates professional response drafts
- Not sure if your PR quality is good enough — it runs an anti-AI Slop checklist for self-inspection

### How to use

Once installed, simply tell your AI assistant which project you want to contribute to. The Skill guides the full workflow: **Pick Issue → Fork/Clone → Branch → Code → Commit → Create PR → Fix CI → Reply to Review → Merge**.

---

## 📁 File Structure

```
github-oss-contribute/
├── SKILL.md                              # Core skill definition
├── README.md                             # This file
├── LICENSE                               # MIT License
├── .gitignore                            # Git ignore rules
├── CONTRIBUTING.md                       # Contribution guide
├── CODE_OF_CONDUCT.md                    # Code of conduct
├── SECURITY.md                           # Security policy
├── .github/
│   ├── pull_request_template.md          # PR template
│   └── ISSUE_TEMPLATE/                   # Issue templates
└── references/                           # Reference documents (7 files)
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)
