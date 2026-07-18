# Security guide for contributors

## Never commit

- access tokens, API keys, passwords or private keys;
- `.env` files containing real values;
- internal hosts, private repository data or customer information;
- generated logs, fixtures or screenshots containing personal data;
- third-party code or assets without known provenance and compatible terms.

## Before committing

Inspect the exact staged file list and diff. Do not print unrelated environment variables.

```bash
git diff --cached --name-status
git diff --cached --check
git diff --cached
```

Use the repository's secret scanner when one exists. Pattern searches are only a supplement and can produce false positives; review matches without copying secret values into logs or chat.

## If a credential is exposed

1. Stop pushing and stop any automation that may reuse it.
2. Revoke or rotate the credential immediately. Deleting the file is not sufficient.
3. Determine where it appeared: working tree, commit, PR diff, Actions log, artifact, release or chat.
4. Notify the target repository through its private security channel.
5. Coordinate history rewriting with the repository owner and collaborators.
6. Invalidate caches, artifacts or releases that still contain the value.
7. Verify the cleaned history before resuming work.

Do not run a generic `git filter-repo` or force-push recipe without resolving the exact affected paths, refs, forks and collaborators. History rewriting is disruptive and does not revoke a credential. Never force-push a protected/default branch without explicit repository-owner coordination.

## Security vulnerabilities in the target project

- Read the target repository's `SECURITY.md`.
- Use Private Vulnerability Reporting or the specified private channel.
- Do not first disclose the issue through a public Issue or ordinary PR.
- Do not publish exploit code, affected versions or a fix timeline without maintainer approval.
- Keep the scope limited to the authorized assessment; do not probe third-party systems.

## Pull-request safety checklist

```text
[ ] No credentials, private paths, private data or internal hosts.
[ ] Dependency and asset provenance is known.
[ ] Workflow permissions use least privilege.
[ ] Untrusted PR code is not executed with elevated secrets.
[ ] Security claims are backed by reproduction or primary documentation.
[ ] The target repository's disclosure policy is being followed.
```
