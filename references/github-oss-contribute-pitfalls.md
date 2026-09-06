# github-oss-contribute 核心避坑库与官方规范基线

<!-- skill-doctor: allow-block SEC002 -->

> 本指南聚合 GitHub 官方 Pull Request 协作规范、Linux 基金会 DCO 认证要求、主流顶级开源社区反 AI Slop 准则与【冷门长尾探索池】中的生产级贡献故障，为从选题、分支管理到 PR 成功合并的全流程提供工业级避坑与合规基线。

---

## 目录

- 一、 官方规范与贡献准入基线 (Official Baselines)
- 二、 【冷门长尾探索池】极端特异性杀手坑 (Fringe Edge Cases & Killer Pitfalls)
- 三、 顶级开源项目对标与协作沟通礼仪 (Peer Projects & Communication)
- 四、 自动化质量核验探针与检测算法 (Safety Probes)

---

## 一、 官方规范与贡献准入基线

### 1. PR 自动关联与关闭 Issue 官方语法规范
- **官方触发机制**：GitHub 仅支持在 Pull Request 描述或 Commit 消息中使用特定关键字触发关联 Issue 的自动关闭：
  - 核心支持词：`Fixes`、`Fixed`、`Fix`、`Closes`、`Closed`、`Close`、`Resolves`、`Resolved`、`Resolve`。
- **🚨 常见格式死锁与陷阱**：
  - **陷阱 1：多 Issue 聚合简写失效**：
    - 错误写法：`Fixes #12, #34, #56`（GitHub 仅会关闭 #12，后面的 #34 和 #56 会被静默忽略）；
    - 正确写法：每个 Issue 必须显式携带动词，如 `Fixes #12, Closes #34, Resolves #56`。
  - **陷阱 2：跨仓库（Cross-Repository）语法**：
    - 若 Fork 提交解决的是上游另一个仓库的 Issue，必须使用完整限定名：`Fixes owner/repository#123`。
  - **陷阱 3：非默认分支不会触发自动关闭**：
    - 自动关闭仅在 PR 合并到目标仓库的**默认分支（Default Branch，如 main/master）**时生效；若 PR 合并到 `dev`、`v2.x` 等次级维护分支，Issue 不会被自动关闭，需人工跟进。
  - **陷阱 4：PR 标题放关键字**：
    - 严禁把 `Fixes #123` 写在 PR 标题中，这会导致查看 PR 列表时视觉杂乱，且某些自动化机器人解析标题时会产生语义异常；必须写在 PR 正文（Description）中。

### 2. DCO (Developer Certificate of Origin) 与 CLA 法律签署准则
- **DCO 规范（Linux 基金会标准）**：
  - 每一条提交必须包含符合 RFC 822 标准的签名行：`Signed-off-by: 真实姓名 <邮箱@example.com>`；
  - 必须使用 `git commit -s` 或 `git commit --signoff` 自动生成；
  - **关键合规基线**：签名中的邮箱必须与 Git 的 `user.email` 以及 GitHub 账号绑定的邮箱**100% 严格一致**，否则 DCO Bot 检查直接报错飘红。
- **DCO 失败后的救场方案**：
  - 单个提交漏签：`git commit --amend --signoff` 然后 `git push origin feat/xxx --force-with-lease`；
  - 多个提交漏签：`git rebase --signoff HEAD~N`（N 为提交数），消解冲突后 `--force-with-lease` 强制推送到特性分支。
- **CLA (Contributor License Agreement)**：
  - 项目方要求转让版权或显式许可协议（如 Apache CLA、Google CLA）；
  - 通常在首次提交 PR 后由 CLA Assistant Bot 自动发帖引导在线点击签署，签署后在 PR 评论中回复 `@cla-bot check` 重新触发验证。

### 3. Conventional Commits 与原子化提交 (Atomic Commits)
- **原子化提交原则**：一个 Commit 仅且只做一件完整的事情。严禁把“重构代码”、“修复 Bug”、“调整样式”和“升级依赖”混装在一个 Commit 中；
- **标准前缀语义**：
  - `feat`: 新增特性或用户可见功能；
  - `fix`: 修复已确认的 Bug；
  - `docs`: 文档变更；
  - `refactor`: 既不修复 Bug 也不添加特性的代码重构；
  - `perf`: 性能优化；
  - `test`: 补齐或重构自动化测试；
  - `chore`: 构建系统、依赖更新等工程辅助变动。
- **时态规范**：必须使用**现在时祈使语气**（如 `fix: handle null exception` 而非 `fixed` 或 `fixing`）。

---

## 二、 【冷门长尾探索池】极端特异性杀手坑

### 1. 直接从 Fork 的 `main/master` 分支提 PR 的“多重毁灭”陷阱
- **病症**：许多初学者 Fork 项目后，直接在自己 Fork 仓库的 `main` 分支上开始写代码，并以 `my-fork:main -> upstream:main` 发起 PR。
- **致命后果**：
  1. **后续无法继续贡献**：一旦 PR 处于审查挂起状态，贡献者如果想针对该仓库修另一个 Bug，由于本地 `main` 已经被污染，无法拉出干净分支；
  2. **“Sync Fork”污染爆炸**：维护者要求同步上游最新代码时，若在 GitHub 网页上点击“Sync fork”，GitHub 会向 `main` 分支自动提交一个 Merge Commit，导致当前的 PR 瞬间被上游几十个无关 Commit 污染，维护者直接拒绝审查；
  3. **Rebase 灾难**：在 `main` 上执行变基会导致本地和远程的分支历史完全分叉。
- **防御铁律**：
  - **永葆 Fork 的 `main` 分支纯净**：Fork 的 `main` 分支仅用于与 `upstream/main` 保持单向同步；
  - **每一次贡献都必须开独立分支**：严格从最新的 `upstream/main` 签出专属分支（如 `git checkout -b fix/issue-123 upstream/main`），严禁跨分支混用。

### 2. Upstream 同步与 Merge Commit 历史污染
- **病症**：当 upstream 有新改动导致 PR 出现冲突或脱节时，贡献者直接执行 `git merge upstream/main` 并 push。
- **后果**：
  - 在 PR 中凭空产生一个丑陋的 `Merge branch 'main' of github.com/...` 节点；
  - 若目标项目维护严格的线性提交历史（Linear History / Fast-forward），该 PR 将直接被 CI 门禁或规则集（Rulesets）阻断合并。
- **官方推荐标准化同步工作流**：
  ```bash
  # 1. 抓取上游最新变动
  git fetch upstream

  # 2. 在自己的特性分支上执行变基
  git checkout fix/my-feature
  git rebase upstream/main

  # 3. 遇到冲突，手动修改后标记并继续
  git add <冲突文件>
  git rebase --continue

  # 4. 安全推送到个人 Fork 远程仓库
  git push origin fix/my-feature --force-with-lease
  ```
  *(💡 技巧：配置 `git config --global rerere.enabled true` 开启冲突解决方案自动复用)*。

### 3. 反“AI Slop”与现代开源社区贡献准则（Anti-AI Slop Policies）
- **2025/2026 社区态势**：Linux Kernel、curl、Homebrew、Debian、QEMU、Zig 等数百个主流开源项目全面出台严厉的 Anti-AI Slop 政策，对未经真实环境运行自证、纯由 LLM 机械生成的 PR 实施**直接关闭、警告乃至封禁账号**。
- **维护者最痛恨的五大垃圾 PR 特征**：
  1. **虚构幻觉 Bug**：AI 自行凭空捏造一个根本不存在的“安全性漏洞”或边界异常，提出看似高级实则荒谬的修改；
  2. **地毯式无意义微调**：批量替换拼写、调整类型注解、格式化空格或重构变量命名，未带来任何实质功能改进却产生大面积 `git blame` 污染；
  3. **问及原理一问三不知**：维护者在 Review 中询问为什么这里要加这行判断，贡献者无法回答，只能再次把问题塞给 AI 复制一段冗长车轱辘话回复；
  4. **缺失回归单测**：声称修复了 Bug，但没有编写任何针对该场景的自动化测试用例；
  5. **机器越权签署 DCO**：法律上 AI 不能签署 DCO，所有 `Signed-off-by` 必须由对代码负全责的人类签署。
- **反 AI Slop 三大自证铁律**：
  - **原理自证**：在 PR 中用清晰的人类逻辑讲明白缺陷根因（Root Cause）与修复构想；
  - **测试自证**：必须提供确定性的单元测试用例或在真实环境下的前后对比复现截图/日志；
  - **最小侵入**：严格克制改动范围，禁止随意格式化无关代码。

### 4. Fork PR 的 GitHub Actions 权限壁垒与 CI 失败排查
- **机理与安全限制**：
  - 外部 Fork 发起的 PR，GitHub 默认**绝不传递任何 Repository Secrets**，防止恶意贡献者在 workflow 中注入代码窃取 Token；
  - 首次贡献者提交 PR 时，GitHub 默认挂起 CI，显示 `First-time contributors need a maintainer to approve running workflows`；
- **排查指南**：
  - 遇到 CI 挂起，切勿反复无意义 Push 催促，耐心等待维护者人工审查后点击 Approve；
  - 若 CI 报错是因为缺少特定云端凭据（如发布测试），需确认目标项目的 CI 设计，在 PR 中礼貌向维护者说明该 Job 需要维护者上下文凭据支持。

### 5. 本地绝对路径与测试假凭据随 PR 泄漏
- **病症**：开发者在编写单测用例或配置文件时，为了本地跑通，写入了本地路径（如 `/Users/username/...` 或 `C:\Users\...`）或真实的个人测试 Token。
- **后果**：PR 一旦被提上去，整个 Git Commit 会被 GitHub 永久缓存在目标仓库的 Pull Request 对象库中，即使关闭 PR 也难以彻底抹去。
- **防御与清洗**：若不慎提交了凭据或敏感路径，推送到远程分支后必须立即在云平台轮转吊销 Token，并使用 `git-filter-repo` 彻底清洗提交历史。

---

## 三、 顶级开源项目对标与协作沟通礼仪

### 1. 选题、认领与避免“半路杀出（Drive-by PR）”
- **黄金原则**：重大修改必须先有 Issue 讨论达成共识，再提 PR；
- **认领礼仪**：
  - 在想要解决的 Issue 下留言询问：“Hi maintainers, I'd like to help fix this issue. Could you please assign it to me?”
  - 确认维护者同意或无其他人正在进行后，再投入实质编码，杜绝重复劳动。

### 2. PR 描述模板的专业填写规范
- **痛点与背景**：明确说明该 PR 解决了哪个已知 Issue（使用 `Fixes #xxx`）；
- **方案与权衡**：简述核心算法与为何采用当前方案，说明潜在的副作用；
- **验证与测试**：列出本地执行的测试命令与实测结果：
  ```markdown
  ### 🧪 Verification Steps
  1. Ran `npm test` / `pytest` -> 100% Passed.
  2. Tested edge case X with input Y -> returned expected Z.
  ```

### 3. Review 反馈的高效闭环协同
- **态度优先**：维护者的批评与修改建议是代码审查的常态，优先回复 “Thanks for the feedback!”；
- **精准回复**：逐条针对 Maintainer 的行内 Review 评论进行修改并推送，在对应评论下回复 “Updated in commit `<SHA>`”，最后点击 “Resolve conversation”；
- **拒绝傲慢辩护**：若确实认为维护者的方案存在隐患，用客观的性能基线（Benchmark）、官方文档链接或重现代码进行理性探讨。

---

## 四、 自动化质量核验探针与检测算法

作为 scripts/ 辅助工具的标准规范，以下核心探针在本地执行 100% 只读扫描：

### 1. DCO 签名与邮箱一致性核验探针 (Python 原生)
```python
import re
import subprocess
from pathlib import Path

def verify_dco_signoff(branch_range: str = "upstream/main..HEAD") -> list[str]:
    """验证分支内所有 commit 是否均携带合规的 Signed-off-by 且邮箱匹配。"""
    issues = []
    cmd = ["git", "log", branch_range, "--format=%H|%an|%ae|%B---COMMIT_SEP---"]
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
    if proc.returncode != 0:
        return [f"Git log failed: {proc.stderr}"]

    commits = proc.stdout.split("---COMMIT_SEP---")
    for raw in commits:
        if not raw.strip():
            continue
        parts = raw.split("|", 3)
        if len(parts) < 4:
            continue
        commit_sha, author_name, author_email, body = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
        
        # 检查是否包含 Signed-off-by
        dco_match = re.search(r"Signed-off-by:\s*(.*?)\s*<([^>]+)>", body)
        if not dco_match:
            issues.append(f"Commit {commit_sha[:8]} 缺失 DCO 签名 (Signed-off-by)")
        else:
            sign_email = dco_match.group(2).strip()
            if sign_email.lower() != author_email.lower():
                issues.append(f"Commit {commit_sha[:8]} DCO 邮箱 ({sign_email}) 与提交者邮箱 ({author_email}) 不一致")

    return issues
```

### 2. 特性分支隔离与禁在 main 提 PR 探针
```python
import subprocess

def check_branch_hygiene() -> list[str]:
    """检查当前是否处于干净的独立特性分支，杜绝直接在 main 提 PR。"""
    issues = []
    proc = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    curr_branch = proc.stdout.strip()
    
    if curr_branch in ("main", "master", "develop", "dev"):
        issues.append(f"当前处于主干分支 '{curr_branch}'！严禁直接从 main 分支提 PR，必须开独立特性分支 (如 feat/xxx 或 fix/xxx)")
        
    return issues
```
