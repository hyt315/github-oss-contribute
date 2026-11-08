# 常见 Git 错误速查

贡献过程中常遇到的 Git 错误和解决方法：

| 错误信息 | 原因 | 解决 |
|---------|------|------|
| `! [rejected] ... (non-fast-forward)` | 你推送的远端分支（通常是 origin 上你的 Fork）有本地没有的提交 | 刚 rebase 过：`git push --force-with-lease`；否则 `git pull --rebase origin <分支>` |
| `error: failed to push some refs` | 推送失败的总提示，真正原因在上一行 `! [rejected]` | 按上一行的具体报错处理 |
| `CONFLICT (content): Merge conflict` | 你和上游改了同一个文件的同一处 | 见 [git-fork-and-conflict-guide.md](git-fork-and-conflict-guide.md) 冲突消解四步法 |
| `You are in 'detached HEAD' state` | 切到了某个 commit 而非分支 | 要保留改动：`git switch -c fix/xxx`；否则 `git switch <分支>` |
| `fatal: refusing to merge unrelated histories` | 两边没有共同祖先，多半是 upstream 地址加错了 | `git remote -v` 核对 upstream；不要随手加 `--allow-unrelated-histories` |
| `Your branch is behind` | 本地落后远端 | 特性分支：`git fetch upstream && git rebase upstream/main` |
| `fatal: not a git repository` | 不在 git 仓库目录中 | `cd` 到正确的仓库目录 |
| `cannot rebase: You have unstaged changes` | 有未提交的修改 | `git stash` 后再 rebase，或 `git rebase --autostash upstream/main` |
| `error: pathspec '...' did not match` | 文件名拼写错误或文件不存在 | 检查文件名和路径 |
| `Permission denied (publickey)` | SSH 密钥未配置 | 配置 SSH 密钥或改用 HTTPS（`gh auth login` 可代为配置） |
| `error: Your local changes ... would be overwritten` | 本地有未提交的修改 | `git stash`；确定不要这些改动才用 `git restore <file>`（不可恢复） |
| `error: remote origin already exists` | 重复添加 remote | `git remote set-url origin <url>` |
| `error: src refspec ... does not match any` | 分支名拼写错误或分支不存在 | `git branch -a` 检查分支名 |
| `remote: Permission to owner/repo.git denied` | 推到了上游而不是你的 Fork | `git remote -v` 确认 origin 指向你的 Fork |
