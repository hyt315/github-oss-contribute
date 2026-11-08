# Security Policy

## Reporting a vulnerability

Report vulnerabilities through [GitHub Private Vulnerability Reporting](https://github.com/hyt315/github-oss-contribute/security/advisories/new).

Do not disclose exploit details, credentials, private repository data or personal information in a public Issue or pull request. If the private reporting form is unavailable, ask the maintainer to enable a private channel without including sensitive details.

## Skill safety requirements

GitHub OSS Contribute must never:

- ask a user to paste a PAT, API key or password into chat;
- search local configuration, shell history or a home directory for credentials;
- print, persist or commit credentials;
- fabricate reproduction steps, tests, benchmarks, CI results or maintainer approval;
- publish a security fix before the target project's private disclosure process allows it;
- push, comment, fork or create a PR without authorization for that exact external action.

If a credential is exposed, stop the affected workflow and revoke/rotate it first. Any history rewrite must be coordinated with the repository owner; see [references/security-guide.md](references/security-guide.md).

## Supported versions

Only the latest published release is actively supported.
