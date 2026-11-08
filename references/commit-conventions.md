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
| `perf` | 性能优化 | — |
| `test` | 测试相关 | — |
| `build` | 构建系统 | — |
| `ci` | CI 配置 | — |
| `chore` | 杂项 | — |
| `revert` | 撤销之前的 commit | — |

规范本身只规定 `feat` → minor、`fix` → patch；类型后加 `!`（如 `feat!:`）或正文写 `BREAKING CHANGE:` 页脚 → major。其他类型没有默认版本影响，由项目自己的发版工具配置决定。来源：[Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。

### 示例

```
fix(auth): resolve login crash with empty password field

The validation was missing a null check, causing a TypeError when
the password field was submitted empty.

Closes #123
```

## DCO 签名与签名提交

项目要求 DCO（`git commit -s`）或签名提交（Verified）时，见 [dco-cla-and-signing.md](dco-cla-and-signing.md)。

## 另一种风格：Gitmoji（少数项目使用）

```
:bug: fix login crash with empty password
:sparkles: add dark mode support
:memo: update README installation guide
```

> 用哪种格式，以阶段 1 侦察到的目标仓库规则为准；没有规定时照着仓库最近的提交历史写。
