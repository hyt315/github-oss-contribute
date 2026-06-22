# Commit 消息规范

## 方式一：Conventional Commits（最广泛使用）

```
<type>(<scope>): <简短描述>

<可选的详细说明>

<可选的关联信息>
Closes #123
```

### Type 类型速查

| Type | 说明 | 版本影响 |
|------|------|----------|
| `feat` | 新功能 | minor |
| `fix` | Bug 修复 | patch |
| `docs` | 文档变更 | — |
| `style` | 代码格式（不影响功能） | — |
| `refactor` | 重构 | — |
| `perf` | 性能优化 | patch |
| `test` | 测试相关 | — |
| `build` | 构建系统 | — |
| `ci` | CI 配置 | — |
| `chore` | 杂项 | — |
| `revert` | 撤销之前的 commit | — |

### 示例

```
fix(auth): resolve login crash with empty password field

The validation was missing a null check, causing a TypeError when
the password field was submitted empty.

Closes #123
```

## 方式二：DCO Signed-off-by

部分项目要求（如 Linux 内核、Spring）。如果仓库 CONTRIBUTING.md 要求 DCO：

```bash
# 单次 commit 签名
git commit -s -m "fix: resolve login crash"

# 补签名到已有 commit
git commit --amend -s --no-edit

# 批量补签名（多个 commit）
git rebase -i HEAD~3  # 对每个 commit 执行 amend -s
```

签名的 commit 消息会自动追加：
```
Signed-off-by: Your Name <your@email.com>
```

> DCO 是开发者原产地声明，表示你有权提交这些代码。与 CLA 不同，DCO 不需要签署协议，只需在 commit 中加 `-s` 标志。

## 方式三：GPG/SSH 签名

部分项目要求验证签名：

```bash
# 配置 GPG 签名
git config --global user.signingkey YOUR_GPG_KEY_ID
git config --global commit.gpgsign true

# 配置 SSH 签名（GitHub 支持）
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub

# 签名 commit
git commit -S -m "fix: resolve login crash"
```

## 方式四：Gitmoji（少数项目使用）

```
:bug: fix login crash with empty password
:sparkles: add dark mode support
:memo: update README installation guide
```

> 具体使用哪种方式，以 Phase 1 侦察到的仓库规则为准。
