# GitHub MCP 工具速查

本技能使用以下 GitHub MCP 工具（按用途分组）。

> 注意：GitHub MCP server 已将多个读取类工具合并为通用工具 + `method` 参数，
> 例如 `pull_request_read` 替代了原来的 `get_pull_request`、`get_pull_request_files` 等。

| 类别 | 工具名 | 用途 |
|------|--------|------|
| **用户** | `get_me` | 获取已认证用户信息 |
| **仓库** | `get_file_contents` | 读取仓库文件或目录 |
| | `search_repositories` | 搜索仓库 |
| | `fork_repository` | Fork 仓库 |
| | `create_branch` | 创建新分支 |
| | `search_code` | 搜索代码 |
| | `list_commits` | 获取提交记录 |
| | `get_commit` | 获取单个提交详情 |
| | `create_or_update_file` | 创建或更新文件 |
| | `push_files` | 批量推送文件 |
| | `get_repository_tree` | 获取仓库目录树 |
| **Issue** | `issue_read` | 读取 Issue（method: `get` / `list`） |
| | `issue_write` | 创建或更新 Issue |
| | `search_issues` | 搜索 Issue 和 PR |
| | `list_issues` | 列出仓库 Issue |
| | `add_issue_comment` | 添加 Issue 评论 |
| | `get_label` | 获取标签信息 |
| **PR** | `pull_request_read` | 读取 PR（method: `get` / `get_files` / `get_status` / `get_reviews` / `get_comments`） |
| | `create_pull_request` | 创建 PR |
| | `list_pull_requests` | 列出仓库 PR |
| | `search_pull_requests` | 搜索 PR |
| | `update_pull_request` | 更新 PR（标题、描述、状态等） |
| | `update_pull_request_branch` | 更新 PR 分支（同步上游） |
| | `merge_pull_request` | 合并 PR |
| | `pull_request_review_write` | 提交 PR 审查 |
| | `add_reply_to_pull_request_comment` | 回复 PR 评论 |
| **安全** | `list_code_scanning_alerts` | 列出代码扫描警报 |
| | `get_code_scanning_alert` | 获取单个代码扫描警报 |
| | `list_secret_scanning_alerts` | 列出密钥扫描警报 |

## pull_request_read method 速查

| method 值 | 对应旧工具名 | 用途 |
|-----------|-------------|------|
| `get` | 原 `get_pull_request` | 获取 PR 详情 |
| `get_files` | 原 `get_pull_request_files` | 获取 PR 修改的文件 |
| `get_status` | 原 `get_pull_request_status` | 获取 PR CI 状态 |
| `get_reviews` | 原 `get_pull_request_reviews` | 获取 PR 审查记录 |
| `get_comments` | 原 `get_pull_request_comments` | 获取 PR 审查评论 |

## issue_read method 速查

| method 值 | 对应旧工具名 | 用途 |
|-----------|-------------|------|
| `get` | 原 `get_issue` | 获取单个 Issue 详情 |

> 如果 GitHub MCP 不可用，所有操作均可通过 GitHub CLI（`gh`）或网页完成。
