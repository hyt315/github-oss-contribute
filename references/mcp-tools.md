# GitHub capability map

GitHub OSS Contribute can use a platform-provided GitHub connection, the [official GitHub MCP Server](https://github.com/github/github-mcp-server), GitHub CLI, public REST API or the website.

## Do not hardcode one tool inventory

GitHub MCP tools evolve. Some releases expose individual tools; others consolidate operations behind a general tool plus a `method` argument. Before using MCP:

1. inspect the tools actually exposed by the current host;
2. select the smallest capability for the task;
3. prefer read-only mode during repository reconnaissance;
4. enable only required toolsets or individual tools;
5. fall back to public API, local Git, `gh` or manual steps when a capability is absent.

## Capability mapping

| Need | Typical current capability | CLI / public fallback |
| --- | --- | --- |
| Current GitHub identity | user/context lookup | `gh api user`; not required for public reads |
| Repository files/tree | repository contents/tree read | clone, raw URL, REST Contents API |
| Search Issues/PRs | issue/search read | `gh issue list`, `gh search issues` |
| Read Issue and comments | issue read | `gh issue view` |
| Comment on Issue | issue comment/write | `gh issue comment` |
| Fork repository | repository fork | `gh repo fork` or website |
| Create branch/push files | Git/repository write | local Git push |
| Read PR files/checks/reviews | pull-request read, Actions read | `gh pr view`, `gh pr diff`, `gh pr checks` |
| Create/update PR | pull-request write | `gh pr create`, `gh pr edit` |
| Reply to Review | pull-request comment/review write | `gh api` or website |
| Read workflow logs | Actions list/get | `gh run view --log-failed` |
| Security alerts | code/secret scanning read | repository Security UI, if authorized |

Tool names such as `issue_read`, `pull_request_read`, `actions_get`, `create_pull_request` or their aliases may be present, but the skill must verify them instead of assuming them.

## Authentication

Public repository reconnaissance requires no credential. For writes, prefer:

1. official platform GitHub connector or remote MCP OAuth;
2. an already authenticated `gh` session;
3. official local GitHub MCP with a trusted secret input;
4. a repository-scoped fine-grained PAT with minimum permissions;
5. manual website handoff.

Never request a Token in chat, scan local configuration for one, or print it. Authentication failure blocks only the external action that needs authentication.

## Approval

Each of the following is a separate external action: Fork, Issue comment, Push, PR creation, Review reply and branch deletion. Show the exact target and content before acting. Approval for one does not authorize the others.

## Official server modes

The official GitHub MCP Server supports hosted remote access and a local server. It also supports read-only mode, toolsets and individual-tool allow-lists. Prefer read-only plus the smallest toolset for reconnaissance; expand only for the approved write.
