---
name: github-oss-contribute
description: |
  开源贡献全程导航：从选 Issue 到 PR 被合并的全流程引导。
  自动分析目标仓库规则（CONTRIBUTING、CI、Branch Protection、AI Policy），
  提供 Fork/Clone/Branch 操作指导、PR 质量自检（反 AI Slop）、CI 失败诊断、
  Review 反馈处理、等待期策略建议。支持 GitHub MCP 自动化操作。
  触发词：开源贡献、第一次贡献、提 PR、first contribution、contribute、
  找个 issue 做、提交 PR、PR 被拒了怎么办、CI 红了、review 意见。
---

# 开源贡献导航

从选 Issue 到 PR 合并的全流程贡献助手。面向贡献者视角，与 oss-prep（建仓库）、oss-ops（管项目）形成完整开源工具链。

## 核心理念

- **贡献者视角**：帮你以贡献者身份参与开源项目，而不是维护者
- **动态适配**：每个仓库规则不同，AI 实时分析目标仓库的具体要求
- **质量优先**：2025-2026 年 AI Slop 泛滥，确保贡献不被当成低质量 PR 秒拒
- **全程引导**：不只教怎么提 PR，还管 CI 红了、Review 意见、等待策略
- **安全意识**：不泄露敏感信息，遵守安全规范

---

## 前置条件

1. **GitHub MCP** 已连接 — 调用 `get_me` 验证认证状态。详见 `references/mcp-tools.md`
2. **Git** 已安装并配置好用户名和邮箱：
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"
   ```
3. **GitHub CLI（gh）** 已安装（作为 MCP 替代方案）— 运行 `gh auth login` 完成认证

如未满足，提示用户先完成配置。

---

## GitHub MCP 工具速查

常用工具：`get_file_contents`、`search_issues`、`fork_repository`、`create_pull_request`、`pull_request_read`（查 PR 状态/审查/评论/文件）、`issue_read`、`add_issue_comment`

> 完整工具清单见 `references/mcp-tools.md`。所有操作均可通过 GitHub CLI 或网页替代。

---

## 工作流程总览

```
Phase 1: 侦察 — 分析目标仓库的规则和文化
    ↓
Phase 2: 选题 — 找到适合的 Issue
    ↓
Phase 3: 准备 — Fork、Clone、创建分支、本地开发环境
    ↓
Phase 4: 开发 — 写代码 + 质量自检 + Commit 规范
    ↓
Phase 5: 提交 — 创建高质量 PR
    ↓
Phase 6: 跟踪 — CI 诊断、Review 处理、等待策略、直到合并
```

每个 Phase 独立可用，用户可能只卡在某个环节。

---

## Phase 1: 侦察 — 分析目标仓库

> 用户提供仓库地址或名称后执行。

### 1.1 验证认证状态

```
get_me
```

### 1.2 读取仓库配置文件

使用 `get_file_contents` 依次读取（文件可能不存在，跳过即可）：

| 文件 | 路径 | 关注点 |
|------|------|--------|
| CONTRIBUTING.md | 根目录 / `docs/` / `.github/` | 贡献流程、分支策略、commit 规范 |
| CODE_OF_CONDUCT.md | 根目录 / `docs/` / `.github/` | 行为准则 |
| CODEOWNERS | `CODEOWNERS` / `.github/` / `docs/` | 谁负责审核哪些文件 |
| PR 模板 | `.github/pull_request_template.md` | PR 必须包含什么内容 |
| Issue 模板 | `.github/ISSUE_TEMPLATE/*.md` | Issue 报告格式要求 |
| AI Policy | CONTRIBUTING.md 中 / `docs/` / 独立文件 | 是否允许 AI 辅助 |
| CI 配置 | `.github/workflows/*.yml` | 有哪些自动检查 |
| DCO/CLA 要求 | CONTRIBUTING.md 中 / `.github/` | 是否需要 Signed-off-by |
| SECURITY.md | 根目录 / `.github/` / `docs/` | 安全漏洞报告方式 |
| LICENSE | 根目录 | 开源许可证类型 |
| README.md | 根目录 | 项目概述、技术栈、构建方式 |

### 1.3 分析仓库活跃度

```
search_issues: q="repo:{owner}/{repo} is:pr is:merged" sort=updated per_page=10
list_commits: owner="{owner}" repo="{repo}" per_page=10
```

评估：最近合并时间、平均 PR 合并时间、PR 接受率、贡献者数量、提交频率。

### 1.4 输出侦察报告

```
## 仓库侦察报告: {owner}/{repo}

### 贡献规则
- 分支策略: [从 CONTRIBUTING.md 提取]
- Commit 规范: [Conventional Commits / 其他 / 无要求]
- CI 检查: [列出主要的 workflow]
- AI Policy: [有/无，具体内容]
- DCO/CLA: [需要/不需要]
- 许可证: [MIT / Apache-2.0 / GPL / 其他]

### 仓库活跃度
- 最近合并: [X 天前]
- PR 平均合并时间: [约 X 天]
- 活跃度评级: 活跃 / 一般 / 不活跃

### 注意事项
- [AI 辅助代码的态度]
- [容易踩的坑]
- [建议的贡献方式]
```

---

## Phase 2: 选题 — 找到适合的 Issue

### 2.1 搜索适合的 Issue

**方式一：GitHub MCP 搜索**（推荐）

```
search_issues: q="repo:{owner}/{repo} is:issue is:open label:\"good first issue\"" sort=updated
search_issues: q="repo:{owner}/{repo} is:issue is:open label:\"help wanted\"" sort=updated
list_issues: owner="{owner}" repo="{repo}" state="open" sort="updated" per_page=20
issue_read: owner="{owner}" repo="{repo}" issue_number={编号}
```

**方式二：GitHub CLI**

```bash
gh issue list --repo {owner}/{repo} --label "good first issue" --state open
gh issue view {编号} --repo {owner}/{repo}
```

**方式三：外部工具**

> Good First Issue（goodfirstissue.dev）、CodeTriage、Up For Grabs 等，详见 `references/first-timer-tips.md`。

> **注意**：2025-2026 年 "good first issue" 标签被 AI Slop 大量滥用，维护者审查越来越严格。

### 2.2 评估 Issue 可行性

| 检查项 | 说明 |
|--------|------|
| Issue 描述是否清晰 | 能看懂要做什么？ |
| 是否有维护者补充说明 | 有人回复过？方向明确？ |
| 涉及的文件范围 | 改几个文件？用 `search_code` 定位 |
| 技术栈是否匹配 | 你的技能是否覆盖？ |
| 是否有人已在做 | 看评论是否有人声明了 "I'll work on this" |
| Issue 创建时间 | 太老的可能已过时 |

### 2.3 先沟通再动手（重要）

> 对于非 trivial 的改动，强烈建议先在 Issue 中说明你的方案。

```
add_issue_comment: owner="{owner}" repo="{repo}" issue_number={编号} body="..."
```

> 评论模板见 `references/communication-etiquette.md`。给维护者 2-3 天回复，收到确认后再写代码。
> 例外：typo 修复、文档小改可直接提 PR。

### 2.4 输出选题建议

为每个候选 Issue 给出评分和建议。

---

## Phase 3: 准备 — 搭建开发环境

### 3.1 Fork 仓库

**方式一：GitHub MCP**（推荐）
```
fork_repository: owner="{owner}" repo="{repo}"
```

**方式二：GitHub CLI**
```bash
gh repo fork {owner}/{repo} --clone -- --depth=1
```

**方式三：网页** — 访问仓库页面，点击右上角 "Fork"。

### 3.2 Clone 到本地

```bash
# 推荐：浅克隆（节省空间）
git clone --depth=1 https://github.com/{你的用户名}/{repo}.git
cd {repo}

# 添加上游仓库
git remote add upstream https://github.com/{owner}/{repo}.git
git remote -v
```

> 国内用户如遇连接超时，可配置 Git 代理（`git config --global http.proxy http://127.0.0.1:7897`）或使用 SSH 协议。

### 3.3 创建功能分支

```bash
# 先同步最新代码
git fetch upstream
git checkout main
git merge upstream/main

# 创建功能分支
git checkout -b fix/issue-123-description
```

或通过 MCP：`create_branch: owner="{你的用户名}" repo="{repo}" branch="fix/issue-123" from_branch="main"`

**分支命名规范**（如仓库无特殊要求）：

| 前缀 | 用途 | 示例 |
|------|------|------|
| `fix/` | Bug 修复 | `fix/issue-123-login-crash` |
| `feat/` | 新功能 | `feat/issue-456-dark-mode` |
| `docs/` | 文档修改 | `docs/issue-789-update-readme` |
| `refactor/` | 重构 | `refactor/issue-101-simplify-auth` |
| `test/` | 测试相关 | `test/issue-202-add-unit-tests` |

### 3.4 搭建本地开发环境

根据仓库 README 或 CONTRIBUTING 指引搭建环境，确保本地能跑通所有测试后再改代码。

---

## Phase 4: 开发 — 写代码 + 质量自检

### 4.1 代码质量自检清单

> 2025-2026 年 AI Slop 问题严重，详见 `references/ai-slop-guide.md`。

**提交前必须确认**：

- [ ] 我理解这个 Issue 要解决什么问题
- [ ] 我理解我写的代码为什么能解决这个问题
- [ ] 改动范围尽量小（<200 行最佳）
- [ ] 没有引入不相关的修改
- [ ] 能解释每一处改动的理由
- [ ] 如果使用了 AI 辅助，我理解生成的代码逻辑
- [ ] 遵守了仓库的 AI Policy
- [ ] 没有引入不必要的依赖
- [ ] 没有硬编码密钥或敏感信息

**AI Slop 红线（碰了就会被拒）**：

| 行为 | 为什么被拒 |
|------|-----------|
| 大量不相关的格式化修改 | 维护者需逐行审查 |
| 提交了自己不理解的代码 | Review 追问答不上来 |
| 一次性提交几千行代码 | 审查负担太重 |
| 不写测试或测试跑不过 | 说明没有本地验证 |
| 解决了一个不存在的问题 | 没看懂 Issue 就写代码 |
| 抢 "good first issue" 后提交低质量 PR | 被视为 AI Slop |

### 4.2 安全实践

提交前检查敏感信息，绝对不要提交 API 密钥、`.env` 文件、私钥等。

> 完整安全实践（含泄露应急处理、检查命令）见 `references/security-guide.md`。

### 4.3 Commit 消息规范

**最常用：Conventional Commits**

```
<type>(<scope>): <简短描述>

<可选的详细说明>

Closes #123
```

常用 type：`feat`（新功能）、`fix`（修复）、`docs`（文档）、`refactor`（重构）、`test`（测试）、`chore`（杂项）

> 完整 type 列表、DCO Signed-off-by、GPG/SSH 签名、Gitmoji 详见 `references/commit-conventions.md`。

**如果仓库要求 DCO**：`git commit -s -m "fix: ..."`（自动追加 `Signed-off-by`）

### 4.4 保持与上游同步

```bash
git fetch upstream
git rebase upstream/main
# 如有冲突：解决冲突 → git add <文件> → git rebase --continue
# 想放弃：git rebase --abort
```

### 4.5 提交前最终检查

```bash
npm test                    # 运行测试
npm run lint                # 运行 lint
git diff upstream/main      # 检查 diff
git diff --stat upstream/main  # 确认改动范围合理
```

---

## Phase 5: 提交 — 创建高质量 PR

### 5.1 Push 到 Fork

```bash
git push origin fix/issue-123-description

# 如果被拒绝（non-fast-forward），先 rebase 再 push
git fetch upstream && git rebase upstream/main
git push origin fix/issue-123-description

# 如果之前已 push 过，rebase 后需要 force push
git push --force-with-lease origin fix/issue-123-description
```

> `--force-with-lease` 比 `--force` 安全——远程有未看到的更新会拒绝推送。

### 5.2 创建 PR

**方式一：GitHub MCP**（推荐）
```
create_pull_request:
  owner: "{owner}"  repo: "{repo}"
  title: "fix(auth): resolve login crash (#123)"
  head: "{你的用户名}:fix/issue-123-description"
  base: "main"  draft: false  maintainer_can_modify: true
```

**方式二：GitHub CLI**
```bash
gh pr create --repo {owner}/{repo} --title "fix(auth): ..." --body "## 问题描述..." --base main
```

**方式三：网页** — GitHub 会提示 "Compare & pull request" 按钮。

### 5.3 验证 PR

```
pull_request_read: owner="{owner}" repo="{repo}" pull_number={PR编号} method="get"
pull_request_read: owner="{owner}" repo="{repo}" pull_number={PR编号} method="get_files"
```

确认文件改动符合预期，没有多余文件。

### 5.4 PR 描述最佳实践

如果仓库有 PR 模板，严格按模板填写。如果没有，确保包含：关联 Issue（`Closes #123`）、解决方案说明、改动类型、测试情况、AI 使用声明（如有要求）。

### 5.5 Draft PR

如果还没完全准备好，可先创建 Draft PR（MCP: `draft: true`，CLI: `gh pr create --draft`），早期让维护者看方向对不对。在网页上点 "Ready for review" 转为正式 PR。

### 5.6 开启 "Allow edits by maintainers"

创建 PR 时勾选此选项（MCP: `maintainer_can_modify: true`），让维护者能直接在你的分支上小修小补，加速合并。

### 5.7 Breaking Changes

如果引入了破坏性变更：
1. Conventional Commits 中用 `!` 标记：`feat(api)!: change response format`
2. PR 描述中详细说明：什么变了、为什么变、用户如何迁移
3. **必须先在 Issue 中讨论并获得维护者同意**

---

## Phase 6: 跟踪 — 直到 PR 被合并

### 6.1 CI 状态诊断

```
pull_request_read: owner="{owner}" repo="{repo}" pull_number={PR编号} method="get_status"
```

**CI 失败常见原因**：

| 失败类型 | 处理方式 |
|----------|---------|
| Lint 失败 | `npm run lint --fix` 或对应命令 |
| 测试失败 | 检查失败用例，修复 bug 或更新测试 |
| 构建失败 | 查看构建日志，检查依赖和类型 |
| 签名检查 | `git commit --amend -s --no-edit && git push -f` |
| Commit 格式 | `git commit --amend` 修改 message |
| 安全扫描 | 更新有漏洞的依赖版本 |
| 代码覆盖率 | 补充测试用例 |

**CI 没运行？** 首次贡献者的 PR 可能需要维护者手动批准 CI 运行——这是正常的。

### 6.2 Review 反馈处理

```
pull_request_read: owner="{owner}" repo="{repo}" pull_number={PR编号} method="get_reviews"
pull_request_read: owner="{owner}" repo="{repo}" pull_number={PR编号} method="get_comments"
```

| 状态 | 含义 | 你需要做什么 |
|------|------|-------------|
| **APPROVED** | 通过 | 等合并 |
| **CHANGES_REQUESTED** | 需修改 | 改完后重新 push |
| **COMMENTED** | 评论 | 回复讨论 |

**处理流程**：本地修改 → 提交 push → 在 PR 页面逐条回复 Reviewer。

> 回复技巧：逐条回复、不同意要礼貌说明理由、感谢 Reviewer 的时间。
> 更多模板见 `references/communication-etiquette.md`。

### 6.3 等待期策略

| 仓库活跃度 | 建议等待 | 之后怎么办 |
|-----------|---------|-----------|
| 活跃（每周有合并） | 7 天 | 礼貌 ping |
| 一般（月均有合并） | 14-21 天 | 礼貌 ping |
| 不活跃（月+无合并） | 30 天 | 考虑换项目 |

```
add_issue_comment: owner="{owner}" repo="{repo}" issue_number={PR编号} body="Hi! Just a friendly ping..."
```

**Stale Bot**：许多项目用 Stale Bot 自动关闭不活跃 PR（通常 30-60 天无活动）。收到 stale 通知后及时评论以重置计时器。

### 6.4 分支冲突处理

```bash
git fetch upstream
git rebase upstream/main
# 解决冲突 → git add → git rebase --continue
git push --force-with-lease origin fix/issue-123-description
```

或通过 MCP：`update_pull_request_branch`（注意：MCP 方式创建 merge commit，部分项目偏好 rebase）。

### 6.5 Merge 策略

维护者合并时选择策略：Merge commit（最常用）、Squash and merge、Rebase and merge、Merge queue。如果项目开启了 auto-merge，可在 PR 页面启用。

### 6.6 PR 被合并后

```bash
git checkout main && git pull upstream main
git branch -d fix/issue-123-description
git push origin --delete fix/issue-123-description
```

---

## 补充说明

- **多种贡献方式**：文档改进、Issue 报告、Review、测试、社区支持、设计、翻译都算贡献
- **Monorepo**：查看 CODEOWNERS，只改相关包，注意包间依赖

### 与 oss-prep / oss-ops 的关系

| 技能 | 视角 | 职责 |
|------|------|------|
| **oss-prep** | 维护者 | 建仓库：补齐社区文件、发布到 GitHub |
| **oss-ops** | 维护者 | 管项目：Issue 分流、PR 审查、发版 |
| **oss-contribute** | 贡献者 | 参与贡献：选 Issue → 提 PR → 被合并 |

### 异常处理

| 情况 | 处理 |
|------|------|
| GitHub MCP 未连接 | 提示连接或改用 CLI / 网页 |
| 仓库不存在或无权限 | 确认仓库名和权限 |
| Issue 已被分配 | 建议选其他 Issue |
| 本地环境搭建失败 | 查看 README 环境要求 |
| PR 被自动关闭 | 检查 Bot 规则（Stale Bot、格式检查） |
| 仓库不接受外部 PR | 建议换项目 |
| 不小心提交敏感信息 | 撤销凭证，用 git-filter-repo 清除历史 |
| CI 始终无法通过 | PR 中说明情况请求帮助 |
| Fork 与上游严重不同步 | 重新 Fork 或 `git rebase upstream/main` |
