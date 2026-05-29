# Writing Team Skill

## Purpose

始终使用此 Skill 处理所有写作任务，启动 writer agent team 进行协作讨论，确保高质量章节笔记产出。

## Trigger

当用户 prompt 包含以下关键词时自动触发：
- "生成第X章笔记"
- "写" + "chapters/chapter"
- "润色" + ".tex"
- "写作任务"
- "生成章节笔记"

## Team Structure

### Writer Pair（Round-robin 轮询选择）

| Round | 主笔 (Primary) | 评审 (Reviewer) |
|-------|----------------|------------------|
| Round 1 | ch1-writer | ch1-writer-2 |
| Round 2 | ch2-writer | ch2-writer-2 |
| Round 3 | ch3-writer | ch3-writer-2 |
| Round 4 | ch1-writer | ch1-writer-2（循环） |

### 状态文件

- 位置：`.Codex/writer-round-robin.json`
- 每次任务完成后更新 `current_round`
- 格式：
```json
{
  "current_round": 1,
  "last_chapter": null,
  "writers": [
    {"name": "ch1-writer", "tasks": 0},
    {"name": "ch1-writer-2", "tasks": 0},
    {"name": "ch2-writer", "tasks": 0},
    {"name": "ch2-writer-2", "tasks": 0},
    {"name": "ch3-writer", "tasks": 0},
    {"name": "ch3-writer-2", "tasks": 0}
  ]
}
```

## Workflow

### Step 1: 读取状态文件

使用 Read 工具读取 `.Codex/writer-round-robin.json`，确定当前 Round 和 writer pair。

### Step 2: 识别章节编号

从用户 prompt 中提取章节编号（如"第3章"→ chapter3）。

### Step 3: Spawn Writer Team

使用 `Agent` 工具并行 spawn：
1. **Primary Writer**（主笔）- 负责起草
2. **Reviewer**（评审）- 负责挑战和审核

### Step 4: 协作讨论（至少 2 轮）

**第一轮**：
- Primary Writer 起草初稿
- Reviewer 阅读并提出质疑/挑战

**第二轮**：
- Primary Writer 回应挑战，修订版本
- Reviewer 最终确认或提出新问题

**最终轮**：
- Reviewer 给出最终评价
- Primary Writer 提交最终版本

### Step 5: Lead 汇总

Team Lead 收集最终版本，向用户交付。

## PUA 注入要求

Spawn sub-agent 时必须在 prompt 末尾注入：

```
开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 **/pua/skills/pua/SKILL.md）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md
```

## 强制要求

| 要求 | 说明 |
|------|------|
| 禁止主 agent 直接处理 | 写作任务必须路由到 Team |
| 必须互发消息讨论 | 成员之间至少 2 轮讨论 |
| 最终结论汇总 | Team Lead 负责端到端交付 |
| 遵循 round-robin | 按顺序轮换 writer pair |

## Writer Memory

所有 writer 共用：
- `docs/lessons/agents/writing-expert-memory.md`

## 输出位置

- 章节笔记：`notes/<主题>/chapters/chapter{X}.tex`
- QA 记录：`notes/<主题>/appendix/qa.tex`
