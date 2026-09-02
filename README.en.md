# 🚀 GitHub OSS Contribute / Contributor Navigator

<div align="center">

**Interactive end-to-end guide for open-source contributors — from finding issues to getting PRs merged, featuring Git conflict resolution, DCO signing, anti-AI slop quality gates, and CI diagnosis.**

**面向全球开发者的开源贡献全程智能导航：从选 Issue 到 PR 成功合并，涵盖 Fork 同步、Rebase 冲突消解、DCO 签名、反 AI Slop 质量自检与 CI 诊断。**

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

## 📖 What is this?

Want to contribute to open-source projects, but stopped by these real-world barriers?
- Finding a project but not knowing how to select a beginner-friendly `good first issue`, or receiving no response after asking to be assigned;
- Developing directly on your local `main` branch, resulting in messy merge conflicts when upstream gets updated;
- Having your PR blocked with `DCO Check Failed` in CNCF/Linux projects because you forgot `-s` (`Signed-off-by`);
- Using AI assistants to code, but being rejected by maintainers because the submission lacked comprehension proof, testing, or was perceived as "AI Slop";
- Getting confused by cryptic GitHub Actions CI errors, or not knowing how to politely address nitpicky code reviews.

**`github-oss-contribute`** is an **AI-powered open-source contributor navigator**. Taking a contributor-first perspective, it guides you through 6 full phases: **Reconnaissance → Issue Selection & Claiming → Fork & Feature Branch Setup → Development & DCO Signing → High-Quality PR Submission → CI Diagnosis & Review Collaboration** to help you make contributions in the most maintainer-friendly and professional manner!

---

## ✨ Key Features

| Phase | Capabilities & Actions | Value & Guardrails |
|---|---|---|
| 🔍 **Phase 1: Recon & Policies** | Analyzes target repository CONTRIBUTING, Rulesets branch protection, Merge Queue, and AI policies | Aligns with community culture before writing code |
| 🎯 **Phase 2: Issue Selection & Claim** | Filters `good first issue`, drafts polite claim comments, prevents public vulnerability leaks | Avoids duplicated effort and makes a great first impression |
| 🍴 **Phase 3: Fork & Branch Isolation** | Configures `upstream` remote, isolates feature branches, **4-step Rebase conflict resolution** | Keeps branches clean and resolves Git conflicts smoothly |
| 💻 **Phase 4: Code & DCO Signing** | Conventional Commits, **DCO (`-s`) signing and retroactive batch sign-offs**, `gpg.format ssh` keys | Passes automated license and commit signature checks |
| 📝 **Phase 5: Anti-AI Slop PRs** | **Anti-AI Slop 3-Point Proof (Comprehension / Testing / Minimal Scope)**, PR template completion | Produces compelling PRs with high merge rates |
| 🚦 **Phase 6: CI Diagnosis & Reviews** | 4-step Actions log triage, Flaky test detection, polite review responses, gentle ping strategies | Accompanies you until the PR is merged |

---

## 📊 6-Phase Complete Contributor Journey Architecture

```
[Input: User wants to contribute to open source / pick an issue / submit a PR / resolve Git conflicts / respond to reviews]
                                              │
         [Phase 1: Recon & Repository Policies] ───> Read references/mcp-tools.md & security-guide.md
                                              │
         [Phase 2: Issue Selection & Claiming] ────> Read references/first-timer-tips.md & communication-etiquette.md
                                              │
         [Phase 3: Fork & Branch Isolation] ───────> Read references/git-fork-and-conflict-guide.md (Upstream + Rebase)
                                              │
         [Phase 4: Development & DCO Signing] ─────> Read references/commit-conventions.md & dco-cla-and-signing.md
                                              │
         [Phase 5: High-Quality PR & Proof] ───────> Read references/ai-slop-guide.md (Anti-AI Slop 3-Point Proof)
                                              │
         [Phase 6: CI Diagnosis, Review & Merge] ──> Read references/ci-troubleshooting.md & git-errors.md
```

---

## 🛡️ 2026 AI-Assisted Contribution Ethics & Anti-Slop Gates

To protect open-source quality and ensure your PR is quickly approved, satisfy these **3 core self-proof principles**:

```
                    ┌────────────────────────────────────────────────────────┐
                    │    2026 Contributor Human-in-the-Loop 3-Point Proof    │
                    └───────────────────────────┬────────────────────────────┘
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                      ▼                                      ▼
【1. Comprehension Proof】             【2. Testing Proof】                   【3. Minimal Scope】
 • Explain every line of your design   • Run unit tests locally in terminal   • Refuse unrelated formatting/renames
 • Answer maintainer questions clearly • Provide before/after test evidence   • Keep PR diff minimal and focused
```

---

## 📚 Real-World Examples

Three end-to-end verified examples in [examples/README.md](examples/README.md):
1. [First-Time Documentation Contribution](examples/README.md#示例一第一次贡献文档微调)
2. [Bug Fixing and CI Triage](examples/README.md#示例二bug-修复与-ci-排查)
3. [Addressing Review Comments and Getting Merged](examples/README.md#示例三处理-review-意见并合并)

---

## 🚀 Quick Start

This is an AI Agent Skill — install it to your AI assistant to use it immediately.

### Option A: Paste one sentence into any Agent (recommended, universal)

Send this to your AI assistant and it will clone to the right skills directory:

> Please install the github-oss-contribute skill: clone `https://github.com/hyt315/github-oss-contribute` into your skills directory (e.g. `~/.claude/skills/github-oss-contribute`, `~/.agents/skills/github-oss-contribute`, or `~/.cursor/skills/github-oss-contribute`) and confirm it works. When I want to contribute to open source, pick an issue, submit a PR, resolve Git conflicts, configure DCO signing, or address reviews, guide me through the SKILL.md workflow.

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

### Option D: Run regression tests locally

```powershell
# Run structure validation
node scripts/validate-skill.mjs

# Run regression selftest
python scripts/selftest.py

# Run skill-doctor audit
python path/to/skill-doctor/scripts/audit.py . --dynamic
```

---

## 🔒 Permissions & Safety Principles

- **Strict Read-Only by Default**: Reconnaissance requires no tokens and only analyzes public repository data;
- **Explicit Write Confirmation**: Forking, pushing, and creating PRs require user confirmation;
- **Zero Credential Harvesting**: Never asks for tokens in chat and never alters global Git configs without permission;
- **Security & Secret Scanning**: Scans code prior to submission to prevent leaking credentials or 0-day vulnerabilities.

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

## 📖 In-Depth Technical References

| Reference Guide | Core Focus | When to Read | Estimated Time |
|---|---|---|---|
| 🍴 [**Fork & Conflict Resolution (`git-fork-and-conflict-guide.md`)**](references/git-fork-and-conflict-guide.md) | Upstream config, branch isolation, and 4-step Rebase conflict resolution | When setting up branches or resolving Git conflicts | 4 mins |
| ✍️ [**DCO, CLA & Signing Guide (`dco-cla-and-signing.md`)**](references/dco-cla-and-signing.md) | DCO `-s` sign-offs, batch retroactive signing, and SSH Commit keys | When committing code or blocked by DCO checks | 4 mins |
| 🛡️ [**Anti-AI Slop Quality Guide (`ai-slop-guide.md`)**](references/ai-slop-guide.md) | 2026 3-point self-proof (Comprehension/Testing/Scope) and PR writing | When drafting PRs and performing pre-commit checks | 4 mins |
| 🚦 [**CI Troubleshooting Guide (`ci-troubleshooting.md`)**](references/ci-troubleshooting.md) | Actions log triage, local reproduction, and Flaky test handling | When GitHub Actions checks fail on your PR | 4 mins |
| 💬 [**Communication & Etiquette (`communication-etiquette.md`)**](references/communication-etiquette.md) | Issue claiming, review replies, and gentle ping templates | When communicating with maintainers | 3 mins |
| 📋 [**Commit Conventions (`commit-conventions.md`)**](references/commit-conventions.md) | Conventional Commits standard types and examples | When writing commit messages | 3 mins |
| 💡 [**First-Timer Tips (`first-timer-tips.md`)**](references/first-timer-tips.md) | Finding `good first issue` and assessing project activity | When looking for projects to contribute to | 3 mins |
| 🔧 [**Git Errors Cheat Sheet (`git-errors.md`)**](references/git-errors.md) | Quick troubleshooting table for common Git errors | When encountering local Git errors | 3 mins |
| 🔑 [**MCP Tools & API Mapping (`mcp-tools.md`)**](references/mcp-tools.md) | Platform MCP tools and public REST API fallbacks | When invoking platform capabilities | 3 mins |
| 🔒 [**Security Guide (`security-guide.md`)**](references/security-guide.md) | Secret scanning and emergency leak response | During pre-commit security audits | 3 mins |

---

## 📁 File Structure

```
github-oss-contribute/
├── SKILL.md                          # Core skill definition, progressive dispatch & 6 contribution phases
├── README.md                         # Chinese documentation
├── README.en.md                      # English documentation
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guide
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── CONTRIBUTORS.md                   # Contributors list
├── manifest.json                     # Skill manifest
├── agents/                           # Multi-agent metadata
├── assets/                           # Media assets and social previews
├── examples/                         # Real-world examples
├── scripts/
│   ├── validate-skill.mjs            # Validation script
│   └── selftest.py                   # Automated regression test runner
└── references/                       # 10 In-depth contributor guides
    ├── git-fork-and-conflict-guide.md # Upstream config & Rebase conflict resolution
    ├── dco-cla-and-signing.md        # DCO sign-offs & SSH Commit signing
    ├── ai-slop-guide.md              # 2026 3-Point proof & anti-AI slop gates
    ├── ci-troubleshooting.md         # CI failure triage & Flaky test handling
    ├── communication-etiquette.md    # Issue claims, review replies & gentle pings
    ├── commit-conventions.md         # Conventional Commits standards
    ├── first-timer-tips.md           # Finding good first issues
    ├── git-errors.md                 # Common Git errors cheat sheet
    ├── mcp-tools.md                  # MCP tools mapping & API fallbacks
    └── security-guide.md             # Secret scanning & security checks
```

---

---

## 🌐 GitHub Open Source Lifecycle Suite

A complete, production-ready toolchain for open-source maintainers and contributors:

| Stage / Role | Recommended Skill | Core Mission & Capabilities | GitHub Repository |
|---|---|---|---|
| 📦 **Pre-Launch Prep** | [**`github-oss-prep`**](https://github.com/hyt315/github-oss-prep) | Automated repository scaffolding, bilingual READMEs, CI workflows, and compliance checks | [hyt315/github-oss-prep](https://github.com/hyt315/github-oss-prep) |
| 🩺 **Quality Doctor** | [**`skill-doctor`**](https://github.com/hyt315/skill-doctor) | 50+ industrial static rules + dynamic selftest runner for 100% reliable Agent Skills | [hyt315/skill-doctor](https://github.com/hyt315/skill-doctor) |
| ⚙️ **Post-Launch Ops** | [**`github-oss-ops`**](https://github.com/hyt315/github-oss-ops) | Issue triage, AI hallucination defense, PR review, GHSA vulnerability SOP, and multi-channel broadcasting | [hyt315/github-oss-ops](https://github.com/hyt315/github-oss-ops) |
| 🚀 **Contributor Navigator** | [**`github-oss-contribute`**](https://github.com/hyt315/github-oss-contribute) | End-to-end contributor guide: Fork syncing, Rebase conflict resolution, DCO signing, and anti-AI slop gates | [hyt315/github-oss-contribute](https://github.com/hyt315/github-oss-contribute) |

---

## ❓ FAQ

- **Q: Why must I configure upstream instead of developing directly on local main?**  
  A: If you code on local `main`, your branch history diverges when the upstream repo updates. Developing on feature branches like `feat/xxx` keeps your `main` clean and makes Rebase conflict resolution straightforward.
- **Q: Why was my PR blocked by DCO? How do I fix it?**  
  A: CNCF and Linux projects require `Signed-off-by` on every commit. Run `git commit --amend -s --no-edit` to add the signature to your latest commit, then `git push --force-with-lease` to update the PR.
- **Q: Will maintainers reject my PR if I used AI to help write code?**  
  A: Most maintainers welcome high-quality contributions regardless of tools used. What maintainers reject is untested code that contributors don't understand (AI Slop). As long as you provide **comprehension proof, test assertions, and minimal scope**, your PR will be warmly received!

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). If this skill helped you, please give it a [Star ⭐](https://github.com/hyt315/github-oss-contribute/stargazers)!

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

> 🌏 **中文版: [README.md](./README.md)**
