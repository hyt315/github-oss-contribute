# 沟通礼仪

## 与维护者沟通的原则

| 原则 | 说明 |
|------|------|
| **先搜索再提问** | 先搜索现有 Issue/PR 和文档，避免重复提问 |
| **清晰描述** | 提供足够的上下文：环境、版本、复现步骤 |
| **尊重时间** | 维护者通常是志愿者，不要催促或要求 |
| **就事论事** | 讨论技术问题，不要人身攻击 |
| **接受拒绝** | 如果方案被否，理解原因，不要纠缠 |
| **表达感谢** | 感谢维护者的审查和反馈 |

## 评论模板

### 认领 Issue

```markdown
Hi! I'd like to work on this issue. Could you assign it to me?
I plan to [简要说明方案]. Thanks!
```

### PR 被 Review 后

```markdown
Thanks for the review! I've addressed the feedback:
- [说明修改 1]
- [说明修改 2]

Let me know if there's anything else to adjust.
```

### 礼貌 Ping

```markdown
Hi! Just a friendly ping to check if there are any updates on this PR.
I'm happy to make any changes if needed. Thanks!
```

### 不同意 Review 意见时

```markdown
I understand your concern. However, I chose this approach because [技术理由].
Would [替代方案] work better? I'm open to suggestions.
```

### 方案沟通（在 Issue 下留言）

```markdown
Hi! I'd like to work on this issue. Here's my proposed approach:

1. [简要说明你的方案]
2. [涉及哪些文件]
3. [预计改动范围]

Does this approach sound good? I'm happy to adjust if needed.
```

---

## 2026 开源全场景中英文沟通模板库

### 1. 认领 Issue 申请文案
```markdown
Hi maintainers! 👋 I'd like to work on this issue. 

I plan to approach it by {brief_solution_summary}. Please let me know if this direction sounds good, and feel free to assign it to me. Thanks!
```

### 2. 赞同并已按 Review 意见修改
```markdown
Thanks for the great feedback! I have updated the code to address your suggestions in commit `{commit_hash}`:
- Refactored `{function_name}` to handle the edge case;
- Added a new unit test in `tests/test_xxx.py`.

Please take another look when you have time! 🙌
```

### 3. 对 Review 意见有不同技术见解时的建设性探讨
```markdown
Thank you for the review! Regarding your suggestion on `{topic}`:

The reason I initially chose `{approach_a}` instead of `{approach_b}` was because `{technical_rationale_or_constraint}`. 

Do you think `{alternative_solution}` would be a good middle ground, or do you still prefer `{approach_b}`? Happy to adjust based on your thoughts!
```

### 4. PR 持续未有回复时的温和提醒 (Gentle Ping)
```markdown
Hi @{maintainer_username}, friendly ping on this PR! 

All CI checks are currently green, and all previous review comments have been addressed. Whenever you have a moment to review, I'd appreciate your thoughts. Thank you for your time!
```
