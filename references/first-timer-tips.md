# 首次贡献者建议

## 选择第一个贡献

| 类型 | 难度 | 建议 |
|------|------|------|
| 文档 typo 修复 | 极低 | 只在你真正使用的项目里做；到陌生仓库批量改错字、改空格是典型的垃圾 PR |
| 文档补充 | 低 | 添加缺失的说明或示例 |
| Bug 修复（小） | 中 | 选择描述清晰、范围明确的 Issue |
| 测试补充 | 中 | 帮项目提高测试覆盖率 |
| 新功能 | 高 | 不建议作为第一次贡献 |

## 第一次贡献流程

1. 选择一个范围清楚、未被认领且近期仍有效的 Issue；`good first issue` 只是一个候选信号
2. 按仓库习惯决定是否先评论认领；评论前先确认不是无意义占位
3. Fork → Clone → 创建分支
4. 做最小必要的改动
5. 本地测试通过
6. 提交 PR，描述清晰
7. 耐心等待 Review

## 常见误区

| 误区 | 正确理解 |
|------|---------|
| "PR 改动越大越好" | 小而精的 PR 更容易被合并 |
| "不需要写测试" | 有测试的 PR 更容易被接受 |
| "维护者必须合并我的 PR" | 维护者有权拒绝，尊重他们的决定 |
| "AI 生成的代码可以直接提交" | 必须理解代码逻辑，遵守项目 AI Policy |
| "不需要提前沟通" | 非 trivial 改动建议先在 Issue 讨论 |
| "CI 红了等维护者处理" | 你的改动导致的失败由你修；Fork PR 拿不到 Secrets 的 Job 要说明情况 |
| "Hacktoberfest 期间多提 PR" | 2026 年起 Hacktoberfest 不再统计 PR，改为活动形式（[FAQ](https://hacktoberfest.com/questions)） |

## 发现入门 Issue

- 目标仓库的 `https://github.com/<owner>/<repo>/contribute` 页面（列出 good first issue 标签的 Issue）
- 仓库内搜索：`is:issue is:open label:"good first issue" no:assignee`
- 跨仓库：`gh search issues --label "good first issue" --state open --language <语言>`
- 第三方聚合：[goodfirstissue.dev](https://goodfirstissue.dev/)、[up-for-grabs.net](https://up-for-grabs.net/)

任何聚合结果都要回到原仓库核对：是否已有人认领或在做、维护者是否仍想要、验收条件是否清楚。
