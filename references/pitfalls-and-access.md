# 常见坑速查与认证/权限边界

> 适用任务：排查高频开源贡献踩坑、确认只读侦察与写操作的 GitHub 认证方式。

## 1. 认证与工具能力边界

- **只读侦察**：`gh` 即使只读也需先登录（`gh auth login --web`）；不想登录时可用 `curl https://api.github.com/repos/<owner>/<repo>/...`（未认证 60 次/小时）或直接看网页。
- **写操作通道选择**：
  - **Fine-grained PAT 的硬限制**：无法在你**非成员**的公开仓库下发表评论或创建 PR，只能推到自己的 Fork；
  - 向他人仓库发评论、Fork 或创建 PR，统一使用**已登录的 `gh` CLI**、**官方 GitHub OAuth 连接器 / GitHub MCP**，或直接走网页端。
- **MCP 能力映射**：不写死单一工具清单，按平台实际提供的 GitHub 工具执行只读查询（查仓库/文件/Issue/PR/日志）与经确认的写操作；如启用官方 MCP，注意 `--lockdown-mode` 与只读工具集边界。

## 2. 开源贡献高频避坑

1. **在 Fork 的 `main` 上直接提 PR** → 切独立特性分支（`git switch -c fix/xxx upstream/main`），保持 `main` 只做上游镜像。
2. **用 `git merge upstream/main` 同步** → 会引入多余 merge commit 破坏线性历史，改用 `git fetch upstream && git rebase upstream/main`。
3. **DCO 检查失败** → 检查 `git log -1 --format="%ae"` 与 `Signed-off-by` 邮箱是否一致，用 `git commit --amend -s` 或 `git rebase --signoff` 补签。
4. **`Fixes #123` 合并后未自动关闭 Issue** → 仅在 PR 合并到**默认分支**且仓库未关闭自动关闭功能时生效；跨仓库需写 `Fixes owner/repo#123`。
5. **Fork PR 触发的 CI 停住或拿不到 Secrets** → 首次贡献者需等维护者点击 Approve and run，且 Fork PR 默认无上游 Secrets，属正常安全机制。
6. **被当成 AI Slop 直接关闭** → 动工前先读目标仓库 AI 政策，守住「讲得清、跑过测试、改动最小、如实披露」四条线。
7. **规则集（Rulesets）拒绝推送** → 上游的 Push Rulesets 会覆盖整个 Fork 网络，提早用 `gh api repos/<owner>/<repo>/rules/branches/<branch>` 查看签名、线性历史与必需检查要求。
