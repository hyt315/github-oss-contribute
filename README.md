# GitHub OSS Contribute

[中文](#中文) · [English](#english)

[![Validate](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-contribute)](https://github.com/hyt315/github-oss-contribute/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/hyt315/github-oss-contribute/total)](https://github.com/hyt315/github-oss-contribute/releases)
[![Contributors](https://img.shields.io/github/contributors/hyt315/github-oss-contribute)](CONTRIBUTORS.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

面向第一次或长期参与开源的贡献者：先读懂仓库规则，再选择 Issue、建立最小改动、通过 CI 与 Review，避免制造没有上下文、没有验证的 AI PR。

```bash
git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute
```

[安装为 Agent Skill](#安装为-agent-skill) · [查看三个贡献示例](examples/README.md) · [下载最新版](https://github.com/hyt315/github-oss-contribute/releases/latest)

![GitHub OSS Contribute workflow: rules, issue, branch, build, pull request and review](assets/social-preview.png)

## 中文

### 它解决什么问题

高质量开源贡献不是“让 AI 改完然后直接提 PR”。贡献者需要先确认项目是否接受这类改动、Issue 是否已被认领、仓库有哪些本地规则、怎样验证，以及维护者希望如何交流。本 Skill 把这些判断放到编码之前，并在每个外部动作前明确权限边界。

| 阶段 | Skill 会做什么 | 质量门禁 |
| --- | --- | --- |
| 仓库侦察 | 读取 README、CONTRIBUTING、AGENTS、CI、模板、DCO/CLA 和 AI policy | 不臆测不存在的规则 |
| 选择 Issue | 评估范围、复现性、活跃度、认领状态和维护者意图 | 大改先沟通，不抢已认领 Issue |
| 本地开发 | 建议分支、最小改动、测试与提交方案 | 不动无关文件，不伪造测试结果 |
| PR 提交 | 生成清晰标题、问题/方案/验证/风险说明 | 创建 PR、评论和推送需用户授权 |
| CI 与 Review | 读取失败日志、定位根因、逐条处理反馈 | 不刷屏、不催促、不隐藏 AI 使用 |
| 合并后 | 清理分支、复盘、寻找下一项贡献 | 不把一次合并当成维护者授权 |

### 三个可复核示例

1. [第一次贡献：先侦察再选 Issue](examples/README.md#示例一第一次贡献)
2. [CI 失败：从日志定位到最小修复](examples/README.md#示例二ci-失败诊断)
3. [Review 反馈：更新代码并给出证据](examples/README.md#示例三处理-review-反馈)

### 安装为 Agent Skill

必须安装完整仓库；`SKILL.md` 会引用 `references/`。

| 平台 | 用户级安装 | 调用方式 |
| --- | --- | --- |
| ChatGPT（Codex 模式）/ Codex CLI | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` | 使用 `$github-oss-contribute`，或通过 `/skills` 选择 |
| Claude Code | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute` | 要求 Claude 使用 `github-oss-contribute` skill |
| Cursor | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute` | 要求 Cursor Agent 使用该 skill |

项目级安装可以使用 `.agents/skills/github-oss-contribute`、`.claude/skills/github-oss-contribute` 或 `.cursor/skills/github-oss-contribute`。新安装未发现时，重启对应 Agent。

Windows PowerShell：

```powershell
git clone https://github.com/hyt315/github-oss-contribute.git "$HOME\.agents\skills\github-oss-contribute"
```

### 下载

```bash
# HTTPS
git clone https://github.com/hyt315/github-oss-contribute.git

# SSH
git clone git@github.com:hyt315/github-oss-contribute.git

# GitHub CLI
gh repo clone hyt315/github-oss-contribute

# main 分支 ZIP
curl -L https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.zip -o github-oss-contribute-main.zip

# 只查看技能合同（单文件不是完整安装）
curl -L https://raw.githubusercontent.com/hyt315/github-oss-contribute/main/SKILL.md -o SKILL.md
```

浏览器入口：[最新 Release](https://github.com/hyt315/github-oss-contribute/releases/latest) · [main ZIP](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.zip)

### 五分钟开始

```text
使用 $github-oss-contribute 分析 https://github.com/OWNER/REPO。
先读取仓库规则、AI policy、CI 和当前 Issue 状态，推荐最多 3 个范围清晰且未被认领的候选项。
现在只做只读侦察，不要 Fork、评论、创建分支或 PR。
```

公开仓库侦察不需要 Token。需要 Fork、Push、评论或创建 PR 时，优先使用平台官方 GitHub 连接、GitHub 官方 MCP OAuth 或已登录的 `gh`，再考虑最小权限 fine-grained PAT。Skill 不会要求你把 Token 发进聊天，也不会扫描配置文件寻找 Token。

### 贡献伦理与署名

- 遵守目标仓库最接近改动目录的 `AGENTS.md`、`CONTRIBUTING.md`、模板、DCO/CLA 和 AI policy。
- 未经维护者认可，不发送大范围重构、纯格式化或“顺手修复”堆叠 PR。
- 不伪造 Issue 复现、测试结果、性能数据或人工审查。
- Git 作者应是实际提交者；AI 署名、Co-authored-by 或披露方式遵守目标仓库政策和用户选择。
- 安全漏洞进入目标仓库的私密披露渠道，不通过普通 PR 或公开 Issue 首次披露。

### 仓库结构与验证

- `SKILL.md`：六阶段贡献工作流。
- `references/`：质量、提交、沟通、Git、MCP 与安全参考。
- `examples/`：三个端到端示例。
- `scripts/validate-skill.mjs`：结构、链接、版本、安装路径和凭据静态检查。
- `.github/workflows/validate.yml`：PR 与主分支 CI。

```bash
node scripts/validate-skill.mjs
```

项目使用 [MIT License](LICENSE)。参与前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)、[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md) 和 [CONTRIBUTORS.md](CONTRIBUTORS.md)。

## English

GitHub OSS Contribute is an Agent Skill for reading a project's rules, choosing a well-scoped Issue, producing a minimal verified change, opening a maintainable PR and responding to CI or review feedback without low-context AI spam.

### Key behavior

- Public repository reconnaissance works without credentials.
- Forks, comments, pushes and pull requests require explicit user authorization.
- Repository-local instructions and contribution policies override generic advice.
- The skill never fabricates test results or searches local configuration for credentials.
- Three inspectable workflows live in [examples/README.md](examples/README.md).

### Install

```bash
# Codex / ChatGPT Codex mode
git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute

# Claude Code
git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute

# Cursor
git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute
```

Validate with `node scripts/validate-skill.mjs`. See the Chinese section for downloads, safety boundaries and the repository map.

### Sources

The workflow follows GitHub's documentation for [contributing to projects](https://docs.github.com/get-started/exploring-projects-on-github/contributing-to-a-project), [working with forks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks), [pull requests](https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and the [official GitHub MCP Server](https://github.com/github/github-mcp-server).
