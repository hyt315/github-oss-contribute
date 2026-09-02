# 上游 Fork 同步与 Rebase 冲突消解实战指南

> 帮助开源贡献者保持分支干净、同步上游最新变更并高效解决代码冲突。

---

## 目录

- [一、配置上游仓库（Upstream Remote）](#一配置上游仓库upstream-remote)
- [二、特性分支隔离原则（保持 main 纯洁）](#二特性分支隔离原则保持-main-纯洁)
- [三、同步上游分支最新变更](#三同步上游分支最新变更)
- [四、Rebase 冲突消解四步法](#四rebase-冲突消解四步法)
- [五、紧急救援：撤销错误的 Rebase](#五紧急救援撤销错误的-rebase)

---

## 一、配置上游仓库（Upstream Remote）

克隆你的个人 Fork 后，必须关联官方主仓库为 `upstream`：

```bash
# 1. 查看当前远程仓库（默认只有 origin）
git remote -v

# 2. 添加上游主仓库
git remote add upstream https://github.com/original-owner/original-repo.git

# 3. 再次确认远程仓库
git remote -v
# 应该看到 origin (你的 Fork) 和 upstream (官方主仓库)
```

---

## 二、特性分支隔离原则（保持 main 纯洁）

- **铁律**：**绝不要直接在本地 `main` 分支写代码并提交 PR**；
- **规范**：每次开发新功能或修复 Bug 时，从最新的 `upstream/main` 创建专属特性分支：
  ```bash
  # 确保拉取上游最新主干
  git fetch upstream main
  
  # 创建并切换到新分支
  git checkout -b feat/add-new-parser upstream/main
  # 或者
  git checkout -b fix/issue-456 upstream/main
  ```

---

## 三、同步上游分支最新变更

当你在开发过程中，官方主仓库已合并了其他开发者的 PR 时，按以下步骤同步：

```bash
# 1. 抓取上游最新提交
git fetch upstream

# 2. 在你的特性分支上执行变基（Rebase）
git checkout feat/my-feature
git rebase upstream/main

# 3. 推送到你的个人 Fork（若之前推过，需 --force-with-lease 保护性强推）
git push --force-with-lease origin feat/my-feature
```

---

## 四、Rebase 冲突消解四步法

如果在 `git rebase upstream/main` 时出现 `CONFLICT (content): Merge conflict in ...`：

### 第一步：查看冲突文件列表
```bash
git status
# 标红的 Both modified: path/to/file.py 即为冲突文件
```

### 第二步：编辑冲突文件消解标记
打开冲突文件，查找 Git 冲突分隔符：
```text
<<<<<<< HEAD (上游已合并的代码)
current_upstream_code()
=======
my_new_contributed_code()
>>>>>>> feat/my-feature (你提交的代码)
```
- 根据业务逻辑，保留正确的代码组合，删除 `<<<<<<<`、`=======`、`>>>>>>>` 冲突标记行。

### 第三步：标记解决并继续变基
```bash
# 暂存解决后的文件
git add path/to/file.py

# 继续完成变基（绝不要在此处执行 git commit！）
git rebase --continue
```
*(如果仍有后续 Commit 冲突，重复二、三步，直到提示 `Successfully rebased and updated`)*

### 第四步：推送更新
```bash
git push --force-with-lease origin feat/my-feature
```
GitHub 上的 PR 会自动更新，且不再提示冲突！

---

## 五、紧急救援：撤销错误的 Rebase

如果冲突修改混乱想完全推倒重来：
```bash
# 立即中止变基，恢复到执行 rebase 前的干净状态
git rebase --abort
```
