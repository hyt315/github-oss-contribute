# 沟通礼仪与评论模板

## 原则

| 原则 | 说明 |
|------|------|
| **先搜索再提问** | 先搜现有 Issue／PR 和文档，避免重复 |
| **给足上下文** | 环境、版本、复现步骤、你已经试过什么 |
| **尊重时间** | 维护者多是志愿者。CONTRIBUTING 写了响应周期就按它等，没写至少等一周再提醒 |
| **就事论事** | 讨论技术，不评价人 |
| **接受拒绝** | 方案被否时理解原因，不换个渠道重提同一改动 |
| **本人回复** | Review 问题由用户本人理解后回答。有的项目（如 Homebrew）明确禁止用 AI 写 Review 回复；下面的模板只是结构参考，要改成用户自己的话 |

认领前先看 CONTRIBUTING：有的项目不做 assign，直接提 PR 即可；只有有写权限的人能指派，你在 Issue 下评论过之后才能被指派。

## 模板（填好花括号，删掉不适用的句子）

### 认领 Issue / 说明方案

```markdown
Hi! I'd like to work on this. My plan:

1. {root cause or what needs to change}
2. {files likely touched}
3. {how I'll verify it: test or reproduction}

Does this direction look right? Happy to adjust.
```

### 已按 Review 修改

```markdown
Thanks for the review! Addressed in {commit_sha}:
- {change 1}
- {change 2}
```

### 不同意 Review 意见

```markdown
Thanks for the suggestion on {topic}. I went with {approach_a} because {technical reason or constraint}.
Would {alternative} work as a middle ground, or would you still prefer {approach_b}? Happy to go either way.
```

### 温和提醒（等够时间后）

```markdown
Hi @{maintainer}, a gentle ping on this PR when you have time.
{只在属实时写：CI is green and the earlier review comments are addressed.}
Thanks!
```

### 无关的 CI 失败

```markdown
`{test_name}` failed in CI, but it looks unrelated to this change ({reason}; it also fails on main in {run link}).
Locally `{test command}` passes. Could someone re-run the job when convenient?
```
