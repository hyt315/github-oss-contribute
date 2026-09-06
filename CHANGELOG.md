# Changelog

本项目采用 [Conventional Commits](https://www.conventionalcommits.org/) 格式记录变更。

## [2.1.0] - 2026-09-06

### Added
- **开源贡献核心避坑库与官方规范基线 (`references/github-oss-contribute-pitfalls.md`)**：
  - 覆盖直接从 Fork 的 `main` 分支提 PR 的“多重毁灭”陷阱与独立特性分支隔离铁律；
  - 覆盖 `git merge upstream/main` 破坏线性历史机理与推荐的 `git fetch` + `git rebase` + `git rerere` 标准变基工作流；
  - 覆盖 2025/2026 顶级开源项目严厉的 Anti-AI Slop 政策，规范原理自证、测试自证与最小侵入准则；
  - 覆盖 DCO `Signed-off-by` 邮箱一致性匹配失败救场与 CLA 签署流程；
  - 覆盖 GitHub PR 自动关闭 Issue 语法规范（`Fixes #123`）与 Fork PR 的 Actions CI 权限壁垒。
- **本地贡献分支校验工具 (`scripts/validate_contribution.py`)**：
  - 支持 `--json` 结构化机读导出、`--quick` 快速采样与 `--read-only` 纯只读模式；
  - 自动检测当前是否在 main/master 默认分支、最新 commit 是否缺失 DCO 签名、是否存在敏感凭据或个人绝对路径。
- **开源贡献就绪事实卡 (Fact Card)**：在 `SKILL.md` 中规范标准 Markdown 分层事实卡（分支隔离、隐私安全、提交质量、法律合规、反 AI Slop、关联指引）。
- **标准 Pytest 测试入口 (`tests/test_skill.py`)**：提供标准测试套件入口，支持 CI 集成。

### Changed
- **指令工程全面升级 (Inline Action Directives)**：彻底消除 `SKILL.md` 中的“详见/可参考”弱引用，全量升级为 `👉 动作：先读 [文件]` 就近内联动作指令。
- **只读安全原则与授权提交铁律**：确立前期侦察 100% 纯只读 Zero-Mutation 纪律，Fork、Push 与 PR 创建明确声明须用户显式授权。
- **自测套件强化 (`scripts/selftest.py`)**：集成 Python 原生 `ast.parse` 静态语法解析门禁、避坑库深度断言、负向拦截夹具与 `validate_contribution.py --json` 联测。

## [2.0.0] - 2026-09-02

### 🌟 Major Upgrade: 全程开源贡献智能导航、Git 冲突消解、DCO 签名与反 AI Slop 质量门禁

- **渐进式调度架构重构**：`SKILL.md` 瘦身为轻量高信号调度中枢（99 行，~2100 tokens），严格按需索引 9 本参考手册；
- **上游 Fork 同步与 Rebase 冲突消解指南**：新增 `references/git-fork-and-conflict-guide.md`，覆盖 upstream remote 配置、特性分支隔离与 4 步冲突消解法；
- **DCO 签署、CLA 协议与 SSH Commit 签名实战**：新增 `references/dco-cla-and-signing.md`，提供 `-s` 补签名命令与 GPG/SSH Verified 绿标配置；
- **CI 失败自诊断与排查四步法**：新增 `references/ci-troubleshooting.md`，覆盖 GitHub Actions 日志分析、本地复现与 Flaky Test 处理；
- **2026 AI 辅助贡献伦理与反 AI Slop 准则升级**：升级 `references/ai-slop-guide.md`，确立原理自证、测试自证与最小改动范围三大铁律；
- **全场景沟通模板库扩充**：扩充 `references/communication-etiquette.md`，新增 Issue 认领、Review 探讨与温和催单文案；
- **门面与文档全面升级**：中英双语 README 达到 PREP 黄金规范标准。

] - 2026-08-21

### Added

- Rulesets reconnaissance: `gh api repos/<owner>/<repo>/rulesets` in Phase 1 — push rules apply to the entire fork network; check push rules, required reviews and commit signoff before forking.
- Verified-commit guidance: SSH signing config (GPG/SSH/S-MIME supported), plus a note on Sigstore keyless (gitsign) for CNCF-style projects.
- Merge Queue explanation in Phase 6: approved ≠ merged; the PR re-runs required checks in queue (`gh pr merge --auto`).
- Bot reviewer handling in Phase 6: treat Copilot/Graphite/Codacy feedback as lint, apply suggested changes manually.
- Security-vulnerability disclosure as a contribution path: never open public issues for vulnerabilities — use SECURITY.md or Private vulnerability reporting (`gh api .../private-vulnerability-reporting`).
- Hacktoberfest-season risk note when picking issues; expanded Conventional Commits type list (perf/build/ci) with "still 1.0.0" clarification.
- `scripts/selftest.py`: zero-dep regression (good fixture = this skill passes; negative fixtures = missing phases and orphan references must be detected). Fixes the missing regression entry found by skill-doctor audit.

### Changed

- AI Policy reconnaissance now also checks whether disclosure of AI assistance is required; Phase 4 checklist adds proactive AI-assistance disclosure, anchored by the curl maintainer's 2025 slop data (~20% slop submissions, ~5% valid security reports).
- Linked the previously orphaned `references/git-errors.md` from Phase 4.4 (caught by the new selftest).
- README rewritten to the split-file bilingual layout (README.md + README.en.md) with one-liner agent install, trigger phrases, prerequisites, deliverables and Stars badge.

## [1.1.0] - 2026-07-18

### Added

- Three end-to-end contribution examples covering reconnaissance, CI diagnosis and review feedback.
- Cross-platform static validator and GitHub Actions validation workflow.
- Agent metadata, repository metadata, contributor attribution and a social-preview asset.

### Changed

- Corrected Codex installation to `~/.agents/skills` and clarified ChatGPT/Codex naming.
- Made public read-only reconnaissance credential-free and moved GitHub authentication to the first authorized write.
- Strengthened repository-instruction discovery, AI disclosure, authorship and contribution-ethics rules.
- Rewrote the landing page around evidence, examples, downloads and a five-minute first run.

### Security

- Removed the fake security email and standardized private vulnerability reporting.
- Prohibited credential discovery, chat-based secret collection and unapproved external writes.

## [1.0.2] - 2026-07-18

- Corrected source download links to the main branch.

## [1.0.1] - 2026-07-18

- Replaced non-functional HTML anchors with Markdown headings.

## [1.0.0] - 2026-07-18

- Initial public release.
