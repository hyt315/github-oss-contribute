# DCO 签署、CLA 协议与 Commit 签名实战指南

> 应对开源项目 DCO (Signed-off-by) 检查、CLA-assistant 授权与 GPG/SSH 提交签名。

---

## 目录

- [一、什么是 Developer Certificate of Origin (DCO)](#一什么是-developer-certificate-of-origin-dco)
- [二、提交时带上 DCO 签名（-s 参数）](#二提交时带上-dco-签名-s-参数)
- [三、补救漏签名的 Commit（解决 DCO Check Failed）](#三补救漏签名的-commit解决-dco-check-failed)
- [四、CLA (Contributor License Agreement) 授权流程](#四cla-contributor-license-agreement-授权流程)
- [五、配置现代 SSH Commit 签名（Verified 绿标）](#五配置现代-ssh-commit-签名verified-绿标)

---

## 一、什么是 Developer Certificate of Origin (DCO)

Linux 内核、CNCF（Kubernetes、Prometheus）、Node.js 等顶级开源项目要求所有提交必须包含 DCO 声明。它证明代码完全由你编写或你有合法授权提供给开源项目，符合开源许可证要求。

DCO 表现为 Commit 消息末尾的这一行：
```text
Signed-off-by: Real Name <user@example.com>
```

---

## 二、提交时带上 DCO 签名（-s 参数）

日常提交时只需在 `git commit` 后加上 `-s` 标志：
```bash
# 必须先确保 git config user.name 和 email 正确
git config user.name "Your Name"
git config user.email "your_email@example.com"

# 使用 -s 自动追加 Signed-off-by
git commit -s -m "feat(parser): add support for json lines format"
```

---

## 三、补救漏签名的 Commit（解决 DCO Check Failed）

若 PR 报 `DCO Check Failed: Commit xxx is not signed off`：

### 场景 A：仅最近的单次 Commit 漏签
```bash
git commit --amend -s --no-edit
git push --force-with-lease origin feat/my-branch
```

### 场景 B：历史多个 Commit 漏签
```bash
# N 为本次 PR 包含的 commit 总数（如最近 3 个）
git rebase -i HEAD~3

# 在弹出的交互编辑器中，将需要补签的 commit 前的 pick 改为 edit（或 reword）
# 保存并退出

# 对每个停下来的 commit 执行：
git commit --amend -s --no-edit
git rebase --continue

# 批量完成后推送
git push --force-with-lease origin feat/my-branch
```

---

## 四、CLA (Contributor License Agreement) 授权流程

部分企业支持的开源项目（如 Google、Microsoft、Apache）使用 CLA Assistant 机器人：
1. 提交 PR 后，`cla-assistant` 会在 PR 下发表自动评论并提供授权链接；
2. 点击链接，使用你的 GitHub 账号登录并阅读贡献者协议；
3. 点击 **I Agree** 签署协议；
4. 页面刷新后，PR 中的 CLA 状态会自动变为绿标通过。

---

## 五、配置现代 SSH Commit 签名（Verified 绿标）

GitHub 现已原生支持使用日常的 SSH 密钥对 Commit 进行加密签名：

```bash
# 1. 告诉 Git 使用 SSH 作为签名格式
git config --global gpg.format ssh

# 2. 指定你的 SSH 公钥路径（如 id_ed25519.pub）
git config --global user.signingkey ~/.ssh/id_ed25519.pub

# 3. 配置默认自动签名所有 commit
git config --global commit.gpgsign true

# 4. 在 GitHub Settings -> SSH and GPG keys 中
# 点击 New SSH key，Key type 选择 "Signing Key"，粘贴公钥内容保存
```
以后每次提交，GitHub 上都会显示权威的 **Verified** 徽章！
