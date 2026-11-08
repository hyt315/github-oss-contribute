# 开源贡献常见坑

每条只写“症状 → 原因 → 怎么做”，细节链接到对应手册。GitHub 相关说法于 2026-11-08 对照官方文档核对。

## 1. 在 Fork 的 main 上直接改代码提 PR

- **症状**：PR 是 `你的Fork:main → 上游:main`；想同时修第二个问题时没有干净的起点；同步上游后 PR 里多出合并提交。
- **原因**：main 既当同步通道又当开发分支。
- **怎么做**：Fork 的 main 只用来跟上游同步，每个贡献从最新上游新开分支：`git switch -c fix/issue-123 upstream/main`。已经在 main 上提交了：先 `git switch -c fix/xxx` 把提交带到新分支，再处理 main。见 [git-fork-and-conflict-guide.md](git-fork-and-conflict-guide.md)。

## 2. 用 merge 同步上游

- **症状**：PR 里出现 `Merge branch 'main' of ...` 提交；要求线性历史的仓库（分支规则 “Require linear history”）不接受含合并提交的分支。
- **怎么做**：`git fetch upstream && git rebase upstream/main`，然后 `git push --force-with-lease`（只对自己的特性分支强推）。项目若明确要求 merge 同步，以项目为准。冲突处理见 [git-fork-and-conflict-guide.md](git-fork-and-conflict-guide.md)。

## 3. DCO 检查失败

- **症状**：PR 上 DCO 检查报某提交未签署。
- **原因**：提交没有 `Signed-off-by`，或签署邮箱与提交作者邮箱不一致（DCO GitHub App 比对的是提交作者邮箱）。
- **怎么做**：单个提交 `git commit --amend -s --no-edit`；多个提交 `git rebase --signoff upstream/main`；然后 `git push --force-with-lease`。DCO 只能由人签，AI 工具不能代签。见 [dco-cla-and-signing.md](dco-cla-and-signing.md)。

## 4. CLA 一直显示未签

- **原因**：各项目用的 CLA 系统不同；签署用的邮箱和提交作者邮箱对不上也会失败。
- **怎么做**：按 PR 里机器人评论操作（CLA Assistant 自动刷新；Linux Foundation EasyCLA 在评论 `/easycla` 重查）。见 [dco-cla-and-signing.md](dco-cla-and-signing.md)。

## 5. `Fixes #123` 没有关闭 Issue

- 关键字只在 **PR 描述** 或 **提交信息** 里生效（不区分大小写，可写 `Closes: #10`）。
- 多个 Issue 每个都要带关键字：`Fixes #12, fixes #34`，不能写成 `Fixes #12, #34`。
- 跨仓库写全名：`Fixes owner/repo#123`。
- PR 的目标分支不是默认分支时，关键字会被忽略。
- 仓库可以在设置里关掉“合并后自动关闭 Issue”，所以合并到默认分支也不一定关闭。
- 来源：[Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)。

## 6. Fork PR 的 CI 不跑或拿不到 Secrets

- **CI 显示 “Awaiting approval”**：默认首次贡献者的工作流需要维护者点 “Approve workflows to run”（仓库可改成其他策略）。不要反复推送催促。
- **需要凭据的 Job 失败**：来自 Fork 的 `pull_request` 工作流拿不到仓库 Secrets，`GITHUB_TOKEN` 只读。在 PR 里说明该 Job 依赖维护者凭据，不要想办法绕过。
- 排查步骤见 [ci-troubleshooting.md](ci-troubleshooting.md)。

## 7. 凭据或个人路径随提交推了上去

- **先做**：立刻吊销或轮换凭据。这是贡献者自己唯一能完全控制的一步，删文件、改历史都不能让已泄露的凭据失效。
- **然后**：通过私有渠道告诉维护者。PR 一旦创建，上游仓库的 `refs/pull/<编号>/head` 会保留那些提交，贡献者自己改写 Fork 的历史删不掉；彻底清理需要仓库所有者联系 GitHub Support。
- **预防**：推送前运行 `scripts/validate_contribution.py`，并逐个核对 `git diff --cached --name-status`。公开仓库默认开启推送保护，但它只拦已知格式的凭据。见 [security-guide.md](security-guide.md)。

## 8. 被当成 AI Slop 关闭

- **常见原因**：改动讲不清原理；声称修复却没有测试或复现；顺手大面积改格式、改命名；在陌生仓库批量改错字；Review 问题用 AI 生成的套话回答。
- **怎么做**：先读目标仓库的 AI 政策（不同项目从禁止到有条件允许都有），按 [ai-slop-guide.md](ai-slop-guide.md) 的三问自检，并按要求披露 AI 辅助。

## 9. 没沟通就提大改动

- 非 trivial 的改动先在 Issue 下说明方案，等维护者认可再写代码；已有人认领的不要抢。模板见 [communication-etiquette.md](communication-etiquette.md)。
- PR 描述写清：解决哪个 Issue、为什么这样改、怎么验证的（命令 + 结果）、还有什么限制。
