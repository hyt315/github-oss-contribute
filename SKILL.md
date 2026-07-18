---
name: github-oss-contribute
version: 1.1.0
description: |
  开源贡献全程导航：从选 Issue 到 PR 被合并的全流程引导。
  自动分析目标仓库规则（CONTRIBUTING、CI、Branch Protection、AI Policy），
  提供 Fork/Clone/Branch 操作指导、PR 质量自检（反 AI Slop）、CI 失败诊断、
  Review 反馈处理、等待期策略建议和批准门禁。支持官方 GitHub 连接、MCP、CLI、网页与公开 API 回退。
  触发词：开源贡献、第一次贡献、提 PR、first contribution、contribute、
  找个 issue 做、提交 PR、PR 被拒了怎么办、CI 红了、review 意见。
---

# 开源贡献导航

从选 Issue 到 PR 合并的全流程贡献助手。面向贡献者视角，与 oss-prep（建仓库）、oss-ops（管项目）形成完整开源工具链。

## 核心理念

- **贡献者视角**：帮你以贡献者身份参与开源项目，而不是维护者
- **动态适配**：每个仓库规则不同，AI 实时分析目标仓库的具体要求
- **质量优先**：用仓库上下文、最小范围、真实验证和持续责任证明贡献质量，不批量制造低上下文 PR
- **全程引导**：不只教怎么提 PR，还管 CI 红了、Review 意见、等待策略
- **安全意识**：不泄露敏感信息，遵守安全规范
- **仓库规则优先**：目标仓库最接近改动目录的 AGENTS.md、CONTRIBUTING、模板、DCO/CLA 和 AI policy 高于通用建议
- **读写分离**：公开仓库侦察可以直接进行；Fork、评论、Push、创建或更新 PR 等外部写操作需要明确授权
- **真实证据**：不得伪造复现、测试、性能结果、维护者意见或人工审查
- **正确署名**：保留实际贡献者的 Git 作者身份；AI 披露或 Co-authored-by 遵守目标仓库规则和用户选择

---

## 前置条件

公开仓库的规则、Issue、PR 和 CI 侦察不需要认证。只在准备执行 Fork、评论、Push 或创建 PR 时检查写入能力。

1. **Git** 已安装。提交前检查当前仓库的用户名和邮箱；不要擅自修改全局配置：
   ```bash
   git config user.name
   git config user.email
   ```
   如未设置，询问用户希望使用的身份，并优先用仓库级 `git config user.name` / `git config user.email`。
2. **GitHub 写入能力**按优先级选择：平台官方 GitHub 连接或 GitHub 官方 MCP OAuth、已认证的 `gh`、官方本地 MCP、最小权限 fine-grained PAT、人工网页操作。
3. 不要求用户把 Token 发到聊天，不搜索用户目录或配置文件提取凭据，不打印或持久化 Token。

认证不可用时继续完成只读侦察、本地修改、测试、补丁和 PR 草稿；只暂停被阻塞的外部写入。

---

## GitHub MCP 工具速查

先查看当前平台实际暴露的 GitHub 能力，再按用途映射：仓库文件读取、Issue 搜索/评论、Fork、PR 创建/读取、Review、Actions 日志。工具名和参数会随 GitHub MCP 版本变化，不把某一套名字当成永久 API。

> 能力映射与回退方式见 `references/mcp-tools.md`。所有只读步骤均可通过公开 API 或网页完成；写操作可通过已认证的 GitHub CLI 或网页替代。

下文中的工具调用块是常见 GitHub MCP 形态的说明示例。执行时必须以当前宿主实际暴露的工具名、`method` 和参数 schema 为准。

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

### 1.1 确认范围与能力

先确认目标 `owner/repo` 和本轮边界。公开仓库侦察直接开始，不为读取公开信息索取认证。只有用户准备执行 Fork、评论、Push 或创建 PR 时，才检查当前平台是否已有官方 GitHub 连接、MCP OAuth 或 `gh auth status`。

### 1.2 读取仓库配置文件

通过当前平台的仓库文件读取能力、公开网页/API 或本地 clone 依次读取（文件可能不存在，记录缺失并继续）：

| 文件 | 路径 | 关注点 |
|------|------|--------|
| AGENTS.md | 仓库根目录与改动文件的父目录 | 对 AI Agent 生效的持久约束、测试命令和风格要求；越接近改动目录的文件优先 |
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

评估：最近合并时间、PR 响应与合并时间、贡献者数量、提交频率。样本不足时给出样本量与时间窗口，不把少量 PR 推导成稳定“接受率”。

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

**方式一：当前 GitHub 连接或 MCP 的 Issue 搜索能力**

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

> `good first issue` 只是候选信号，不等于允许直接开工。仍要检查是否被指派、是否有人认领、最近是否有维护者确认，以及验收条件是否清楚。

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

> 评论是外部写操作，先展示草稿并获得批准。等待时间遵循目标仓库活跃度和 CONTRIBUTING 指引，不用固定天数机械催促。
> 例外：typo 修复、文档小改可直接提 PR。

### 2.4 输出选题建议

为每个候选 Issue 给出评分和建议。

---

## Phase 3: 准备 — 搭建开发环境

### 3.1 Fork 仓库

Fork 会在用户账号下创建远程仓库。先展示目标上游、目标账号和后续用途，并获得批准。

**方式一：当前 GitHub 连接或 MCP 的 Fork 能力**
```
fork_repository: owner="{owner}" repo="{repo}"
```

**方式二：GitHub CLI**
```bash
gh repo fork {owner}/{repo} --clone
```

**方式三：网页** — 访问仓库页面，点击右上角 "Fork"。

### 3.2 Clone 到本地

```bash
# 默认保留完整历史，便于 blame、rebase 和依赖版本信息的测试脚本
git clone https://github.com/{你的用户名}/{repo}.git
cd {repo}

# 添加上游仓库
git remote add upstream https://github.com/{owner}/{repo}.git
git remote -v
```

> 只有在用户已经拥有可信代理并明确要求时才配置 Git 代理；不要写入猜测的本地端口。大型仓库可在确认不依赖历史后选择浅克隆。

### 3.3 创建功能分支

```bash
# 先同步最新代码
git fetch upstream
git checkout main
git merge upstream/main

# 创建功能分支
git checkout -b fix/issue-123-description
```

也可使用当前 GitHub 连接提供的分支创建能力。创建 Fork 或远程分支前先确认目标账号、上游仓库和分支名。

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

> AI 辅助不是问题本身；缺少上下文、理解、验证和责任才是质量风险。详见 `references/ai-slop-guide.md`。

**提交前必须确认**：

- [ ] 我理解这个 Issue 要解决什么问题
- [ ] 我理解我写的代码为什么能解决这个问题
- [ ] 改动范围是完成已接受目标所需的最小可审查范围（不存在通用行数上限）
- [ ] 没有引入不相关的修改
- [ ] 能解释每一处改动的理由
- [ ] 如果使用了 AI 辅助，我理解生成的代码逻辑
- [ ] 遵守了仓库的 AI Policy
- [ ] 没有引入不必要的依赖
- [ ] 没有硬编码密钥或敏感信息

**高风险质量信号**：

| 行为 | 为什么被拒 |
|------|-----------|
| 大量不相关的格式化修改 | 维护者需逐行审查 |
| 提交了自己不理解的代码 | Review 追问答不上来 |
| 一次性提交几千行代码 | 审查负担太重 |
| 声称测试通过但没有运行，或隐瞒失败 | 维护者无法信任验证结果 |
| 解决了一个不存在的问题 | 没看懂 Issue 就写代码 |
| 未检查认领状态就提交重复 PR | 浪费贡献者和维护者时间 |

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

Push 前展示远程名称、完整仓库 URL、精确分支和将要推送的提交；获得批准后执行。

```bash
git push origin fix/issue-123-description

# 如果被拒绝（non-fast-forward），先 rebase 再 push
git fetch upstream && git rebase upstream/main
git push origin fix/issue-123-description

# 如果之前已 push 过，rebase 后需要 force push
git push --force-with-lease origin fix/issue-123-description
```

> `--force-with-lease` 仍会改写远程分支。仅在确认 PR 的精确 head 分支、没有他人提交且用户批准后使用；禁止对默认分支使用。

### 5.2 创建 PR

创建 PR 前展示 base/head、标题、正文、文件列表、测试证据、已知风险和 AI 披露要求；这是独立于 Push 的外部写入批准点。

**方式一：当前 GitHub 连接或 MCP 的 PR 创建能力**
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

是否允许维护者修改 Fork 分支取决于目标项目习惯和分支中是否含有不应共享的工作。默认解释影响并让用户选择，不机械开启。

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
| 签名检查 | 核对 DCO/签名要求；修正提交后仅对精确 PR 分支使用 `git push --force-with-lease` |
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
| 活跃（每周有合并） | 参考近期同类 PR | 超过正常响应窗口后礼貌询问一次 |
| 一般（月均有合并） | 参考维护者公开节奏 | 补充新信息时再更新，避免无内容 ping |
| 不活跃（月+无合并） | 先判断项目状态 | 考虑换项目或保留 Fork，不持续催促 |

```
add_issue_comment: owner="{owner}" repo="{repo}" issue_number={PR编号} body="Hi! Just a friendly ping..."
```

**Stale Bot**：收到 stale 通知时，只有在仍计划继续且能提供状态或新证据时才回复；不要发送无内容评论只为重置计时器。

### 6.4 分支冲突处理

```bash
git fetch upstream
git rebase upstream/main
# 解决冲突 → git add → git rebase --continue
git push --force-with-lease origin fix/issue-123-description
```

也可使用当前 GitHub 连接的“更新 PR 分支”能力，但要先确认它会 merge 还是 rebase，并遵守目标项目策略。

### 6.5 Merge 策略

合并策略由维护者和仓库规则决定：Merge commit、Squash、Rebase 或 Merge queue 都可能使用。贡献者不应把自己的偏好写成项目默认。

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
| GitHub MCP 未连接 | 继续公开只读侦察和本地工作；外部写入改用已认证 CLI、官方连接或网页 |
| 仓库不存在或无权限 | 确认仓库名和权限 |
| Issue 已被分配 | 建议选其他 Issue |
| 本地环境搭建失败 | 查看 README 环境要求 |
| PR 被自动关闭 | 检查 Bot 规则（Stale Bot、格式检查） |
| 仓库不接受外部 PR | 建议换项目 |
| 不小心提交敏感信息 | 撤销凭证，用 git-filter-repo 清除历史 |
| CI 始终无法通过 | PR 中说明情况请求帮助 |
| Fork 与上游严重不同步 | 重新 Fork 或 `git rebase upstream/main` |
