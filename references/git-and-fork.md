# Fork 同步、Rebase 冲突消解与 CI 排查

> 适用任务：配置 `upstream`、建特性分支、同步上游、处理 Rebase 冲突与常见 Git 报错、诊断失败的 CI。Fork、推送与强推均需用户确认。

## 1. Fork 与特性分支隔离

永远不要直接在 Fork 的 `main`/`master` 上改代码提 PR，否则上游更新后主干分叉很难清理：

```bash
# 1. 配置上游远程（origin 是你的 Fork，upstream 是官方主仓）
git remote add upstream https://github.com/<upstream-owner>/<repo>.git
git fetch upstream

# 2. 基于最新上游切独立特性分支
git switch -c fix/<short-name> upstream/main
```

## 2. 同步上游与 Rebase 冲突消解

优先用 `rebase` 而不是 `merge` 同步上游，保持提交历史干净（仅对自己独占的特性分支使用 `--force-with-lease`）：

```bash
git fetch upstream
git rebase upstream/main
# 推送刷新 PR（安全强推，避免覆盖他人提交）
git push --force-with-lease origin fix/<short-name>
```

### 冲突消解四步法
1. `git status` 查看 `both modified` 冲突文件；
2. 逐文件处理冲突标记（注意：**rebase 期间 `ours` 是上游新提交，`theirs` 是你自己的提交**，与 `merge` 相反）；
3. 解决并本地跑通测试后：`git add <冲突文件>` → `git rebase --continue`（**绝不要在冲突解决中途直接 `git commit`**）；
4. 若变基弄乱：进行中用 `git rebase --abort`；已完成则用 `git reflog` 找到变基前 commit 恢复。

## 3. 常见 Git 报错速查

- **`non-fast-forward`（来自 `origin`）**：rebase 后历史已改写，确认是自己的特性分支后用 `git push --force-with-lease`。
- **误改未暂存文件想撤销**：`git restore <file>`（**不可恢复**，先用 `git diff <file>` 确认）。
- **忘记切分支直接提交到了本地 `main`**：先 `git switch -c fix/<name>` 保留提交，再切回 `main` 用 `git reset --hard upstream/main` 还原。

## 4. CI 失败四步排查

1. **拿真实日志**：`gh pr checks <num>` 查看失败项，`gh run view <run-id> --log-failed` 拉取失败日志（Fork PR 首次提交可能停在等待维护者点击 Approve and run，不等于代码报错）。
2. **区分问题归属**：看是你的改动引发（Lint/格式化/单测/类型检查），还是上游已有故障或 Flaky Test（对比主干最新 CI 状态）。
3. **本地复现并最小修复**：按仓库 `CONTRIBUTING.md` 或 workflow 里的命令在本地跑通相同版本环境后再提交。
4. **Fork PR 拿不到 Secrets**：若失败原因是缺少维护者私有密钥（如云凭证/发布 token），说明这是安全隔离机制，在 PR 评论里注明即可，不要试图绕过。
