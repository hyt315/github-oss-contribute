# 常见 Git 错误速查

贡献过程中常遇到的 Git 错误和解决方法：

| 错误信息 | 原因 | 解决 |
|---------|------|------|
| `push rejected (non-fast-forward)` | 远程有你没有的更新 | `git pull --rebase upstream main` |
| `CONFLICT (content): Merge conflict` | 你和上游改了同一个文件的同一处 | 手动解决冲突 |
| `detached HEAD` | checkout 了 commit 而非分支 | `git checkout main` 回到分支 |
| `refusing to merge unrelated histories` | 两个仓库没有共同祖先 | 加 `--allow-unrelated-histories` |
| `Your branch is behind` | 本地落后远程 | `git pull --rebase` |
| `error: failed to push some refs` | 本地落后远程 | `git fetch upstream && git rebase upstream/main` |
| `fatal: not a git repository` | 不在 git 仓库目录中 | `cd` 到正确的仓库目录 |
| `Cannot rebase: You have unstaged changes` | 有未暂存的修改 | `git stash` 暂存后再 rebase |
| `error: pathspec 'file' did not match` | 文件名拼写错误或文件不存在 | 检查文件名和路径 |
| `fatal: refusing to merge unrelated histories` | Fork 仓库与上游没有共同祖先 | 确认正确添加了 upstream remote |
| `Permission denied (publickey)` | SSH 密钥未配置 | 配置 SSH 密钥或改用 HTTPS |
| `error: Your local changes would be overwritten` | 本地有未提交的修改 | `git stash` 或 `git checkout -- <file>` |
| `fatal: remote origin already exists` | 重复添加 remote | `git remote set-url origin <url>` |
| `error: src refspec does not match any` | 分支名拼写错误或分支不存在 | 检查分支名 `git branch -a` |
