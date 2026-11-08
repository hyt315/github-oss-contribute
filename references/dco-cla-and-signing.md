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

Linux 内核、Node.js、Spring 等项目要求每个提交带 DCO 声明，表示你有权按项目许可证提交这段代码（全文见 [developercertificate.org](https://developercertificate.org/)）。是否要求以目标仓库 CONTRIBUTING 为准；同属 CNCF 的项目也不统一，例如 Kubernetes 用的是 CNCF CLA（EasyCLA），不是 DCO。

DCO 必须由对代码负责的人本人签署，不能由 AI 工具代签。

DCO 表现为 Commit 消息末尾的这一行：
```text
Signed-off-by: Real Name <user@example.com>
```

---

## 二、提交时带上 DCO 签名（-s 参数）

日常提交时只需在 `git commit` 后加上 `-s` 标志：
```bash
# 先确认姓名和邮箱正确：DCO 检查要求 Signed-off-by 邮箱与提交作者邮箱一致
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
# 给基线之后的所有提交补签（Git 2.24+）
git fetch upstream
git rebase --signoff upstream/main

# 确认每个提交都有 Signed-off-by 后推送
git log upstream/main..HEAD --format='%h %s%n%(trailers:key=Signed-off-by)'
git push --force-with-lease origin feat/my-branch
```

---

## 四、CLA (Contributor License Agreement) 授权流程

CLA 是一份法律协议，各项目用的签署系统不同，以 PR 里机器人的评论为准：

| 系统 | 典型项目 | 签署方式 | 重新检查 |
|---|---|---|---|
| CLA Assistant | 很多中小项目 | 点评论里的链接，用 GitHub 登录，点 I Agree | 签完后状态自动更新 |
| EasyCLA（Linux Foundation） | Kubernetes 等 CNCF 项目 | 按评论链接签个人或公司 CLA | 在 PR 评论 `/easycla` |
| Google CLA | Google 开源项目 | 在 cla.developers.google.com 签署 | 签完后状态自动更新 |

注意：签 CLA 用的邮箱要和提交作者邮箱一致，否则机器人仍会报未签。公司员工可能需要走公司 CLA，先问雇主。

---

## 五、配置现代 SSH Commit 签名（Verified 绿标）

需要 Git 2.34+。GitHub 支持用 SSH 密钥签名提交：

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
之后的提交在 GitHub 上显示 **Verified**。几个例外：
- 维护者用 “Rebase and merge” 或 “Squash and merge” 合并时，GitHub 会生成新提交（新 SHA），你的原签名不会随之保留；
- 开了 vigilant mode 后，未签名的提交会标为 Unverified；
- 本地 `git log --show-signature` 要验证 SSH 签名，还需配置 `gpg.ssh.allowedSignersFile`。

用 GPG 时把第 1、2 步换成 `git config --global gpg.format openpgp` 和 `git config --global user.signingkey <GPG 密钥 ID>`，两种配置不要同时保留。
