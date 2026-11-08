# Changelog

本项目采用 [Conventional Commits](https://www.conventionalcommits.org/) 格式记录变更。

## [2.2.0] - 2026-11-08

### Changed
- `SKILL.md` 改为“阶段路由表”（阶段 → 先读哪份手册 → 产出 → 需批准的写操作），删除与路由表重复的 Reference Files 列表和逐阶段段落；阶段 1 侦察命令内联。
- `scripts/validate_contribution.py` 重写：只检查本分支相对上游基线（自动识别 `upstream/HEAD`、`origin/HEAD` 等，或 `--base` 指定）新增的提交与新增行，不再扫描整个仓库；DCO 逐个提交检查并核对签署邮箱与作者邮箱；提交标题按 Conventional Commits 提示；凭据规则补全 `gho_/ghu_/ghs_/ghr_`、AWS、Slack 并加词边界防误报；处理 detached HEAD；非 git 目录退出码 2。
- 精简重复内容：`commit-conventions.md` 的 DCO/签名部分改为链接；`communication-etiquette.md` 两套重复模板合并为一套；`ai-slop-guide.md` 删除失效目录、中文段与英文正文统一口径；避坑库重写为 9 条“症状 → 原因 → 怎么做”，删除与脚本重复的探针代码。
- CI 改用 Python 3.12 + `actions/checkout@v7.0.1` + `actions/setup-python@v7.1.0`，不再依赖 Node（Node 20 已于 2026-04-30 停止维护）。

### Removed
- `scripts/selftest.py`、`scripts/validate-skill.mjs`、`tests/test_skill.py`，由 `scripts/validate.py`（唯一校验入口）和 `tests/` 下两组正向/负向测试取代。
- README 中指向不存在仓库 `skill-doctor` 的链接与命令。

### Fixed（对照 2026-11-08 官方文档核对）
- Fine-grained PAT 不能在用户非成员的公开仓库评论或开 PR，只能推到自己的 Fork；`gh` 即使只读也需要登录。
- Kubernetes 使用 CNCF CLA（EasyCLA，`/easycla` 重查），不是 DCO；Google 使用自有 CLA 系统；`@cla-bot check` 说法删除。
- DCO 检查比对的是提交作者邮箱，而非 GitHub 账号邮箱；多提交补签改用 `git rebase --signoff`（原 `reword` 步骤无效）。
- Conventional Commits：`perf` 不默认 patch；补充 `!` / `BREAKING CHANGE` → major。
- SSH 签名需 Git 2.34+；Verified 的例外（rebase/squash 合并、vigilant mode、本地 allowedSignersFile）；GPG 与 SSH 配置互相覆盖的提示。
- 冲突标记示例与 rebase 时 ours/theirs 互换说明；补充完成后的 rebase 用 reflog 恢复。
- Git 报错速查：non-fast-forward 来自 origin 而非 upstream；删除重复且相互矛盾的 unrelated histories 条目；`git checkout -- <file>` 改为带不可恢复警告的 `git restore`。
- 各项目 AI 政策并不统一（QEMU/Zig/Gentoo/NetBSD 禁止，Linux 内核/curl/Homebrew/Ghostty 有条件允许，Debian 中立），删除“数百个项目全面禁止”的说法。
- `Fixes #` 在非默认分支被忽略、仓库可关闭自动关闭 Issue；Fork PR 等待批准的按钮名；泄露凭据时贡献者无法清除上游 `refs/pull/*`，先吊销。
- 新增本地 MCP 默认浏览器登录、`--lockdown-mode`、`get_job_logs`、`code_security`/`secret_protection` 工具集名称。
- Hacktoberfest 2026 起不再统计 PR；“陌生仓库批量改错字”列为垃圾 PR 模式。
- README：示例锚点失效、“端到端可复核”“高通过率”等无法证实的说法、中英文全局 Git 配置描述不一致、重复分隔线。
- CHANGELOG 中 1.2.0 条目标题损坏，已修复并补上 1.2.1。

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

## [1.2.1] - 2026-08-22

### Changed

- Reference Files 表措辞修正（破折号空格），无功能变化。

## [1.2.0] - 2026-08-21

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
