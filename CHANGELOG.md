# Changelog

All notable changes to GitHub OSS Contribute are documented here.

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
