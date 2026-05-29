---
name: lesson-capture
description: Use when team agents need to record or review lessons learned during Q&A sessions
---

# Lesson Capture Skill

## Overview

让 agent 团队在回答问题过程中稳定地**记录经验教训**到 markdown 文件的协议。

## 核心问题

**现状**：Agent 只在开工时读 memory，过程中不主动写。

**目标**：Agent 每回答 2-3 个问题后，主动识别新教训并写入文件。

## 协议

### 1. 开工时：读取教训文件

```
读取: docs/lessons/lessons-log.md
读取: docs/lessons/agents/ALL-agents-memory.md
读取: docs/lessons/agents/{agent-name}-memory.md
```

### 2. 回答问题后：评估是否值得记录

**触发条件**（满足任一）：
- 用户纠正了错误
- 发现新的模式/规律
- 解决了之前未解决的问题
- 识别到"不是问题"的问题（如今天的 Theorem 后等式、脚注在 Theorem 内）

### 3. 每 2-3 个问题后：主动检查

```python
# 检查计数器
if question_count % 3 == 0:
    问自己："有什么新教训要记录吗？"
```

### 4. 写入格式

```markdown
## YYYY-MM-DD: [简短标题]

**问题/场景**：[描述]

**教训**：[核心要点，1-2 句]

**检查清单**：
- [ ] 检查项 1
- [ ] 检查项 2
```

### 5. 写入位置

| 教训类型 | 目标文件 |
|---------|----------|
| 通用教训 | `docs/lessons/lessons-log.md` |
| 跨 agent 教训 | `docs/lessons/agents/ALL-agents-memory.md` |
| 专属 agent 教训 | `docs/lessons/agents/{name}-memory.md` |

## Agent Prompt 注入模板

在 agent 的 prompt 中添加：

```
### 经验教训记录协议（必须执行）

1. **开工时读取**：
   - `docs/lessons/lessons-log.md`
   - `docs/lessons/agents/ALL-agents-memory.md`
   - `docs/lessons/agents/{agent-name}-memory.md`

2. **回答问题后评估**：
   - 用户纠正了错误？→ 值得记录
   - 发现新模式？→ 值得记录
   - 解决了难题？→ 值得记录
   - 识别"不是问题"的问题？→ 值得记录

3. **每 3 个问题后主动检查**：
   - 问自己："有什么新教训？"
   - 有则写入对应文件

4. **写入后报告**：
   - 告诉 team-lead："已记录 X 条新教训到 ..."

## 经验教训文件位置

- 通用: `docs/lessons/lessons-log.md`
- 全 agent: `docs/lessons/agents/ALL-agents-memory.md`
- 个人: `docs/lessons/agents/{name}-memory.md`
```

## 稳定性保障

**计数器机制**：Agent 内部维护 `question_count`，每回答一个问题 +1，模 3 为 0 时主动检查。

**触发词提醒**：
- "记住" → 立即写入
- "教训" → 立即写入
- "经验" → 检查是否值得记录

## 示例

**场景**：用户纠正了 agent 说"行202孤立等式是问题"——实际上不是问题。

**记录**：
```markdown
## 2026-03-31: Proofread 时 AI 报告的问题需用户视觉确认

**问题**：AI 报告了 4 个问题，但经用户逐个确认后，只有 2 个是真正需要修复的。

**教训**：AI 报告 ≠ 必须修复，必须逐个跳转让用户视觉确认。

**检查清单**：
- Theorem 后的等式可能是正常表述，不是残留
- 脚注在 Theorem 内在 LaTeX 中是合法的
```
