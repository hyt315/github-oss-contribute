# Changelog

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)；提交信息使用 [Conventional Commits](https://www.conventionalcommits.org/)。

## [2.3.0] - 2026-11-20

Major simplification & pre-PR scanner calibration release.

### Fixed

- **Calibrated personal path scanning in `validate_contribution.py`**: Ignored common placeholder usernames (`<user>`, `YourName`, `%USERNAME%`, `user`, `you`, `runner`, `ubuntu`, `Public`, `Shared`) so documentation and test examples no longer trigger false FAILs.
- **Expanded shared secret patterns**: Added detection for PKCS#8 private-key headers, Google `AIza`, Hugging Face `hf_`, npm `npm_`, PyPI `pypi-`, and URL-embedded credentials; skipped lockfile diffs (`package-lock.json`, `uv.lock`, etc.).
- **Added Markdown `#anchor` validation** to `scripts/validate.py` (previously skipped).

### Changed

- **Consolidated `references/` (11 fragmented files → 4 focused manuals)**: Merged into `git-and-fork.md`, `commits-dco-and-signing.md`, `ai-policy-and-pr-quality.md`, and `pitfalls-and-access.md`, removing bilingual duplication and fill-in-the-blank etiquette templates.
- **Updated 2026 AI disclosure guidance**: Clarified `Signed-off-by` (human-only) vs `Assisted-by:` trailer / PR description disclosure, warning against abusing `Co-authored-by` for AI tools.
- **Decoupled brittle release-ceremony checks** in `scripts/validate.py` and consolidated `.github/workflows/validate.yml` into a single Python `["3.10", "3.12"]` matrix job.
- **Streamlined bilingual READMEs**: Added `npx skills add hyt315/github-oss-contribute` alongside copy-to-AI installation and aligned the Open Source Lifecycle Suite.

### Removed

- `.github/repository-metadata.yml`, `CONTRIBUTORS.md`, and `examples/README.md` (redundant static files).

## [2.2.1] - 2026-11-12

- Prioritized `upstream/*` over `origin/*` in `validate_contribution.py`, failed fast on missing `--base`, switched to hunk-level diff parsing, moved `version` to `metadata.version`, and unified secret rules between `validate.py` and `validate_contribution.py`.

## [2.2.0] - 2026-11-08

- Converted `SKILL.md` to a phase routing table, rewrote `validate_contribution.py` to scan only newly added commits/lines, and fact-checked GitHub Docs & AI policies.

## [2.1.0] - 2026-09-06

- Added `validate_contribution.py`, pitfalls guide, and Fact Card format.

## [2.0.0] - 2026-09-02

- Added Fork/Rebase guide, DCO/CLA/SSH signing guide, CI troubleshooting, and anti-AI slop gates.

## [1.2.1] - 2026-08-22

- Added reference reading-time table.

## [1.2.0] - 2026-08-21

- Added Rulesets recon, verified commits, Merge Queue, and security disclosure guidance.

## [1.1.0] - 2026-07-18

- Reworked authentication around read-only recon and approval-gated writes.

## [1.0.2] - 2026-07-17

- Corrected source download links to `main`.

## [1.0.1] - 2026-06-22

- Replaced HTML anchors with Markdown headings.

## [1.0.0] - 2026-06-22

- Initial public release.
