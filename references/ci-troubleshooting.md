# CI 失败自诊断与排查四步法

> 帮助贡献者精准排查 GitHub Actions CI 报错、本地复现与快速修复。

---

## 目录

- [一、CI 失败自排查四步流程](#一ci-失败自排查四步流程)
- [二、常见 CI 失败类别与快速解法](#二常见-ci-失败类别与快速解法)
- [三、Flaky Test（偶发性挂掉）处理策略](#三flaky-test偶发性挂掉处理策略)
- [四、更新 PR 并重新触发 CI](#四更新-pr-并重新触发-ci)

---

## 一、CI 失败自排查四步流程

```
Step 1: 定位失败 Job ──> PR 的 Checks 标签页点红色 Job，或 gh run view <run-id> --log-failed
    ↓
Step 2: 抓取核心报错 ──> 展开标红的 Run 步骤，搜索 FAIL / ERROR / AssertionError / Error:
    ↓
Step 3: 本地精准复现 ──> 在本地运行与 CI 相同的命令（npm test / pytest / cargo test）
    ↓
Step 4: 修复并推送 ────> 修复代码，自测通过后追加 commit 推送到 PR 分支
```

---

## 二、常见 CI 失败类别与快速解法

| 失败类别 | 典型报错信息 | 本地排查与解法 |
|---|---|---|
| **代码格式 / Lint 失败** | `prettier --check failed` / `flake8 failed` / `eslint error` | 在本地运行对应的格式化命令（如 `npm run format`、`ruff format .`、`cargo fmt`） |
| **单元测试断言失败** | `AssertionError: expected X but got Y` / `Test failed` | 根据报错行号定位，本地运行单测命令 `pytest tests/test_xxx.py` 进行调试 |
| **类型检查失败** | `tsc error TS2322` / `mypy: Incompatible types` | 修正缺失的类型注解或未处理的 `null` / `None` 分支 |
| **依赖安装 / 版本不匹配** | `ModuleNotFoundError` / `package not found` | 检查是否引入了新依赖但忘记更新 `package.json` / `requirements.txt` / `Cargo.toml` |
| **跨平台环境失败 (Linux/macOS/Windows)** | `
: command not found` / `path delimiter error` | 检查是否有 Windows CRLF 换行或反斜杠硬编码路径，统一使用标准库 Path 抽象 |

---

| **CI 一直不跑（显示等待批准）** | PR 上出现 “Awaiting approval” | 维护者需点 “Approve workflows to run”。首次贡献者默认需要批准，别反复推送催促 |
| **需要 Secrets 的 Job 失败** | 凭据为空、`401`、发布或部署步骤失败 | Fork 的 PR 拿不到仓库 Secrets，`GITHUB_TOKEN` 也只读。在 PR 里说明该 Job 依赖维护者凭据，不要试图绕过 |

## 三、Flaky Test（偶发性挂掉）处理策略

如果失败的测试与你修改的文件毫无关联，可能遇到了项目的偶发性不稳定测试（Flaky Test）：
1. **对比主分支状态**：查看目标仓库 `main` 分支最近的 CI 运行记录，确认该测试是否在 main 分支也偶尔挂掉；
2. **在 PR 中礼貌说明**：
   > “Notice that `test_network_timeout` failed in CI, but it seems unrelated to the docs changes in this PR. Locally all tests pass. Could someone help re-run the job?”
3. **维护者通常会协助点击 Re-run jobs**。

---

## 四、更新 PR 并重新触发 CI

修复完成后，直接推送即可自动触发新的 CI 构建：
```bash
# 只暂存相关文件，先核对清单
git add path/to/fixed_file
git diff --cached --name-status
git commit -s -m "fix(ci): format code and fix assertion in parser test"

# 推送到你的分支（PR 会自动刷新并重新跑 CI）
git push origin feat/my-branch
```
