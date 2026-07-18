# GitHub OSS Contribute examples

These examples show what the skill should produce before it performs any external write. Repository and Issue details are illustrative; the sequence and evidence requirements are normative.

## 示例一：第一次贡献

**Prompt**

```text
我想给 OWNER/REPO 做第一次贡献。先只读分析规则并推荐最多 3 个候选 Issue，不要 Fork、评论或创建 PR。
```

**Expected output**

```text
仓库规则：需要签署 DCO；提交使用 Conventional Commits；允许 AI 辅助但 PR 必须披露验证方式。
活跃度：最近 30 天合并 18 个 PR；维护者通常 2–4 天首次回复。

候选 #214 — Windows 文档路径错误
范围：小（1 个文档文件 + 链接检查）
状态：未指派；过去 14 天无认领评论
验收：Windows 路径可复制；链接检查通过
风险：低
下一步建议：先在 Issue 留一条简短认领评论。

待批准写操作：在 #214 发表评论。尚未 Fork。
```

## 示例二：CI 失败诊断

**Prompt**

```text
我的 PR #81 在 Linux 通过、Windows 失败。读取日志并给最小修复方案，先不要 Push。
```

**Expected output**

```text
失败 job：windows / link-check
首个根因：脚本把路径分隔符写死为 `/`
非根因：后续 12 个 snapshot failure 是连锁结果
最小修复：使用 path.join；只更新受影响的 2 个 snapshot
验证：node --test tests/path.test.js；再运行完整 npm test
不建议：跳过 Windows job、批量重写全部 snapshot

待批准写操作：无。用户确认改动后才编辑和 Push。
```

## 示例三：处理 Review 反馈

**Prompt**

```text
维护者要求补充回归测试并缩小改动范围。帮我更新方案和回复草稿。
```

**Expected output**

```text
反馈拆分：
1. 必须：增加空配置回归测试
2. 必须：移除无关格式化
3. 建议：说明兼容性范围

修改计划：恢复 4 个无关文件；增加 1 个失败优先测试；修复 1 个条件分支；运行目标测试和完整测试。

回复草稿：感谢指出。我已把 PR 缩回到配置为空的回归修复，恢复了无关格式化，并新增了先失败后通过的测试。验证结果：……

待批准写操作：Push 更新；发送 Review 回复。
```
