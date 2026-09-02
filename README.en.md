# 🤝 GitHub OSS Contribute / github-oss-contribute

<div align="center">

**End-to-end open-source contribution guide from issue scouting to merged PR — reconnaissance before coding with explicit write-action authorization.**

**从选 Issue 到 PR 被合并的全流程引导：先读懂仓库规则，再建立最小改动，用真实验证和持续责任赢得维护者信任。**

[![Validate](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml/badge.svg)](https://github.com/hyt315/github-oss-contribute/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/hyt315/github-oss-contribute?sort=semver)](https://github.com/hyt315/github-oss-contribute/releases/latest)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-1f6feb)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/hyt315/github-oss-contribute?style=social)](https://github.com/hyt315/github-oss-contribute/stargazers)

[English](./README.en.md) | [中文](./README.md)

</div>

![GitHub OSS Contribute workflow: rules, issue, branch, build, pull request and review](assets/social-preview.png)

---

## 📖 What is this?

High-quality open-source contribution is not about "asking an AI to code and immediately opening a blind PR".

**`github-oss-contribute`** is an AI Agent Skill designed to place critical decision-making before coding: Does the project welcome this change? Has the issue already been claimed? What local CI and Rulesets exist? How should the change be verified? How do maintainers prefer to communicate? — all with **strict staged authorization before every external write action**.

A six-phase workflow ensures complete safety from **Reconnaissance → Issue Selection → Minimal Implementation → Verified PR → CI & Review Handling → Merged Retrospective**.

---

## ✨ Key Features

| Core Phase | Operations & Focus | Quality Gates & Value |
|---|---|---|
| 🔍 **Phase 1: Reconnaissance** | Scans README, CONTRIBUTING, Rulesets, CI matrix, DCO/CLA, and AI policies | Never assumes rules; identifies exact boundaries |
| 🎯 **Phase 2: Issue Selection** | Assesses scope, reproducibility, activity, and claim status | Communicates first; never hijacks claimed issues |
| 🛠️ **Phase 3: Minimal Development** | Suggests clean branches, minimal diffs, local test runs, and commit signatures | Touches no unrelated files; no fabricated test results |
| 📤 **Phase 4: Verified PR** | Drafts clear titles, issue context, test proof, and risk assessments | Creating PRs, comments, and pushes require explicit approval |
| 🩺 **Phase 5: CI & Review** | Analyzes failure logs, pinpoints root cause, handles Maintainer & Bot reviews | No spamming, no rushing; presents verifiable evidence |
| 🏆 **Phase 6: Retrospective** | Cleans up local/remote branches, consolidates learnings, scouts next tasks | Builds long-term open-source reputation |

---

## 📊 6-Phase Complete Pipeline Architecture

```
[Input: User wants to contribute to an open-source project]
                              │
     [Phase 1: Target Repository Reconnaissance] ──> CONTRIBUTING / Rulesets / AI Policy
                              │
     [Phase 2: Task Selection & Scoping] ─────────> Evaluate good-first-issues & claims
                              │
     [Phase 3: Minimal Verified Development] ─────> Minimal diff / Local test execution
                              │
     [Phase 4: Standardized PR Submission] ───────> Real reproduction & test evidence
                              │
     [Phase 5: CI Diagnostics & Review Triage] ───> Root cause logs & reviewer replies
                              │
     [Phase 6: Post-Merge Retrospective] ─────────> Branch cleanup & reputation building
```

---

## 📚 Real-World Walkthroughs

Three end-to-end verified examples, detailed in [examples/README.md](examples/README.md):
1. [First Contribution: Reconnaissance before claiming](examples/README.md#示例一第一次贡献)
2. [CI Failure: From raw logs to minimal fix](examples/README.md#示例二ci-失败诊断)
3. [Review Feedback: Updating code with test evidence](examples/README.md#示例三处理-review-反馈)

---

## 🚀 Quick Start

This is an AI Agent Skill — install it into your AI assistant and you're ready.

### Option A: Paste one sentence into any Agent (recommended, most universal)

Send this to your AI assistant and it will detect the platform and clone to the right skills directory:

> Please install the github-oss-contribute skill: clone `https://github.com/hyt315/github-oss-contribute` into your skills directory (e.g. `~/.claude/skills/github-oss-contribute`, `~/.agents/skills/github-oss-contribute`, or `~/.cursor/skills/github-oss-contribute`) and confirm it works. When I want to find open-source issues, open a PR, or fix CI failures, guide me through the 6-phase workflow.

### Option B: GitHub CLI 2.90+ (one command)

```bash
gh skill install hyt315/github-oss-contribute github-oss-contribute --agent claude-code --scope user
```

### Option C: Manual per-platform install

| Platform | User-level Path | Project-level Path |
|---|---|---|
| **Claude Code** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.claude/skills/github-oss-contribute` | `.claude/skills/github-oss-contribute` |
| **Codex** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` | `.agents/skills/github-oss-contribute` |
| **Cursor** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.cursor/skills/github-oss-contribute` | `.cursor/skills/github-oss-contribute` |
| **General Agents** | `git clone https://github.com/hyt315/github-oss-contribute.git ~/.agents/skills/github-oss-contribute` | `.agents/skills/github-oss-contribute` |

### Option D: Run local regression selftest

```powershell
python scripts/selftest.py
```

---

## 🔒 Permission Boundaries & Safety Principles

- **Zero-Token Reconnaissance**: Public repository rule analysis runs read-only without credentials;
- **Staged Approvals for Writes**: Forking, issue commenting, remote branch pushing, and PR opening require explicit approval;
- **Honest Evidence**: Zero fabricated test passes; adheres strictly to target repo's AI code disclosure guidelines.

---

## 📥 Download

| Method | Command / Link |
|---|---|
| **HTTPS** | `git clone https://github.com/hyt315/github-oss-contribute.git` |
| **SSH** | `git clone git@github.com:hyt315/github-oss-contribute.git` |
| **GitHub CLI** | `gh repo clone hyt315/github-oss-contribute` |
| **ZIP** | [Download ZIP](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.zip) |
| **Tarball** | [Download Tar](https://github.com/hyt315/github-oss-contribute/archive/refs/heads/main.tar.gz) |
| **Single file (SKILL.md)** | `curl -O https://raw.githubusercontent.com/hyt315/github-oss-contribute/main/SKILL.md` |

---

## 📁 File Structure

```
github-oss-contribute/
├── SKILL.md                          # Core skill definition and 6-phase workflow
├── README.md                         # Chinese documentation
├── README.en.md                      # English documentation
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── SUPPORT.md                        # Support channels
├── manifest.json                     # Skill manifest
├── agents/                           # Multi-agent metadata
├── examples/README.md                # 3 Verified end-to-end case studies
├── scripts/
│   ├── validate-skill.mjs            # Validator
│   ├── validate_repo.py              # Structure validator
│   └── selftest.py                   # Automated regression test runner
└── references/                       # Reconnaissance methods & PR guides
```

---

## ❓ FAQ

- **Q: What if my first PR gets rejected?**  
  A: Phases 1 and 2 guide you through reading CONTRIBUTING guidelines and choosing `good first issue` tasks, reducing the risk of rejection.
- **Q: What if the PR's CI turns red?**  
  A: Phase 5 parses CI raw logs, locates the exact failing assertion, and assists in drafting a minimal fix.
- **Q: Will it push code to remote repositories automatically?**  
  A: Never. All external actions (Fork, Push, PR) require explicit user approval.

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). If this skill helped you, please give it a [Star ⭐](https://github.com/hyt315/github-oss-contribute/stargazers)!

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

> 🌏 **中文版: [README.md](./README.md)**
