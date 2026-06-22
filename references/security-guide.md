# 安全实践指南

## 绝对不要提交的内容

- API 密钥、访问令牌（如 GitHub PAT、AWS Key）
- 数据库密码、连接字符串
- `.env` 文件、配置文件中的敏感信息
- 私钥文件（`.pem`、`.key`、`.p12`）
- 内部服务器地址、内部 API 端点

## 如果不小心提交了敏感信息

```bash
# 1. 立即撤销该密钥/令牌（最重要！在 GitHub/服务提供商设置中操作）
# 2. 从 Git 历史中移除（使用 git-filter-repo 或 BFG）
pip install git-filter-repo
git filter-repo --invert-paths --path .env
# 3. Force push
git push --force-with-lease origin fix/issue-123-description
# 4. 通知维护者（如果已经提了 PR）
```

> **注意**：仅仅删除文件并提交新 commit 是不够的——敏感信息仍然存在于 Git 历史中。必须用工具清除历史记录，并立即撤销泄露的凭证。

## 提交前检查

```bash
# 检查是否有敏感文件被暂存
git diff --cached --name-only | grep -iE '\.env|\.key|\.pem|secret|credential'

# 检查 diff 中是否有疑似密钥的字符串
git diff --cached | grep -iE 'api_key|secret|password|token|auth'
```

## 安全检查清单

1. **检查 `.gitignore`**：确保 `.env`、`*.key`、`*.pem` 等敏感文件已被忽略
2. **检查 diff**：`git diff --cached` 确认没有敏感信息
3. **检查文件列表**：`git diff --cached --name-only` 确认没有多余文件

## 常见安全错误

| 错误 | 后果 | 正确做法 |
|------|------|---------|
| 提交 `.env` 文件 | 泄露数据库密码、API 密钥 | 加入 `.gitignore`，提供 `.env.example` |
| 硬编码 API 密钥 | 密钥泄露，被滥用 | 使用环境变量 |
| 提交 `node_modules/` | 仓库膨胀，可能含敏感配置 | 加入 `.gitignore` |
| 提交 IDE 配置 | 可能含本地路径或密钥 | 加入 `.gitignore`（`.idea/`、`.vscode/`） |
| 提交日志文件 | 可能含用户数据或敏感信息 | 加入 `.gitignore` |

## 如果发现安全问题

如果在你贡献的过程中发现了项目的安全漏洞：
1. **不要在公开 Issue 中报告**——查看 `SECURITY.md` 中的安全报告流程
2. 通常需要私下联系维护者或使用 GitHub Security Advisories
3. 不要在 PR 中包含漏洞利用代码
