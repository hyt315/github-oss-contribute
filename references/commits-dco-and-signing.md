# Commit 规范、DCO/CLA、签名与 AI 披露

> 适用任务：编写规范提交信息、通过 DCO/CLA 检查、配置 SSH Commit 签名、按项目政策披露 AI 辅助。

## 1. Conventional Commits 速查（仅当目标仓库要求时套用）

格式：`<type>(<scope>): <简短祈使句描述>`（破坏性变更在类型后加 `!` 或在正文加 `BREAKING CHANGE:`）。
- 常用类型：`feat`（新功能）、`fix`（修复 Bug）、`docs`（文档）、`refactor`（重构）、`test`（测试）、`chore`（构建/杂项）、`perf`（性能）、`ci`（工作流）。
- `docs` / `refactor` / `perf` 不默认触发版本号递增，以目标仓库规则为准。

## 2. DCO（Signed-off-by）与 CLA

- **DCO 签署**：提交时加 `-s` 自动追加 `Signed-off-by: Name <email>`。**DCO 检查比对的是 commit 作者邮箱，不是 GitHub 账号邮箱**，两者必须一致。
- **补签漏签提交**：
  ```bash
  # 仅最近 1 个提交
  git commit --amend -s --no-edit
  # 基线之后的多个提交（Git 2.24+）
  git rebase --signoff upstream/main
  git push --force-with-lease
  ```
- **CLA 协议**：CNCF/Kubernetes 等项目使用 EasyCLA（评论 `/easycla` 重查），Google 等有自有 CLA 系统；签署时确保使用与 commit 作者一致的邮箱。

## 3. AI 辅助披露规范（2026 社区共识）

1. **`Signed-off-by` 只能由人签**：DCO 是法律责任声明，模型不能承担责任，绝不能替 AI 签或让 AI 冒充人类签署。
2. **不要滥用 `Co-authored-by` 标记 AI**：`Co-authored-by` 在 GitHub 上会把模型渲染成共同作者/贡献者，多数严谨开源项目反对把工具写成共同作者。
3. **透明披露方式（优先服从目标仓库政策）**：若项目要求在 commit 中标注，使用 `Assisted-by: <tool/model>` trailer（例如 `git commit -s --trailer "Assisted-by: Claude"`）；若项目无 trailer 规定，在 PR 描述中简明写清 AI 辅助了哪部分以及你如何逐行审查与测试。

## 4. SSH Commit 签名（Verified 绿标，Git 2.34+）

仅在目标仓库 Rulesets 要求签名提交或用户主动需要时配置（注意：改全局 `gpg.format` 会覆盖已有 GPG 配置，建议先只配当前仓库 `--local`）：

```bash
git config --local gpg.format ssh
git config --local user.signingkey ~/.ssh/id_ed25519.pub
git config --local commit.gpgsign true
```

随后在 GitHub **Settings → SSH and GPG keys → New SSH key** 添加同一公钥，Key type 选择 **Signing Key**。注意：上游以 Rebase/Squash 方式合并后，原提交的 Verified 标可能变化，属正常行为。
