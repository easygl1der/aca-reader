# Team Config PUA 注入与三角协作更新

**Session ID:** efe8fd79-7fd0-405b-804b-99608da7fbd9
**Date:** 2026-03-29
**Total Messages:** 17 user inputs

---

## 用户需求与执行摘要

### 背景
用户发现 literature-experts 团队中 sub-agent 的 prompt 缺少 PUA 自注入机制，导致无法自我迭代改进。同样问题隔壁组 agent 一次就过，根因在于团队配置不完整。

### 用户输入序列

| # | 用户输入 |
|---|---------|
| 1 | hello |
| 2 | hello |
| 3 | 加载 PUA skill |
| 4 | What agent team do I have? |
| 5 | do they have memory for each expert |
| 6 | show me the causal-expert memory |
| 7 | where is the expert memory individually stored |
| 8 | what is the prompt for causal expert |
| 9 | add PUA injection to each, and complete the prompt with latex-checker, exercise-expert |
| 10 | yes, extend to all domain experts |
| 11 | commit these changes |
| 12 | auto-commit-push skill |
| 13 | backup the team config to project directory |
| 14 | chat-history-summarizer skill |

---

## 执行动作详情

### 1. 团队配置盘点

**发现的问题**：
- Team config 位于 `~/.claude/teams/literature-experts/config.json`
- 只有 `research-expert` 有 PUA 注入
- 其他 15 个 agents 全部缺失 PUA 自注入
- `causal-expert` 缺少 latex-checker 和 exercise-expert 协作说明

### 2. PUA 注入添加

**目标 agents**：15 个（除 research-expert 外全部）

```
causal-expert, causal-expert-2,
geometry-expert, bayesian-expert, info-geo-expert, schubert-expert,
statistic-expert, statistic-expert-2,
writing-expert, writing-expert-2, writing-expert-3,
exercise-expert, exercise-expert-2, exercise-expert-3,
latex-checker, qa-specialist
```

**注入内容**：
```
### PUA 自注入（必须执行）

开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md
  （用 Glob 搜索 **/pua-skills/skills/pua/SKILL.md）
```

### 3. 三角协作架构添加

**仅添加到 7 个 domain experts**：
- causal-expert ✅
- geometry-expert ✅
- bayesian-expert ✅
- info-geo-expert ✅
- schubert-expert ✅
- statistic-expert ✅
- statistic-expert-2 ✅

**三角协作架构内容**：
```
### 三角协作架构（必须遵循！）
domain-expert ←→ writing-expert
       ↕                  ↕
   latex-checker ←→ team-lead

**你的角色**：作为 domain-expert，提供数学内容和动机。

**协作流程**：
1. 用户提问 → 你回答（提供数学内容和动机）
2. → 交给 writing-expert 润色（Stein 风格）
3. → 交给 latex-checker 质量检查
4. → 最终输出

**latex-checker 检查项**：
- 禁止 Markdown 残留（\bm、\mathbb{I} 应用正确）
- 推导必须→附录
- Theorem 环境禁止 itemize

**exercise-expert 习题规范**：
- 必须用 \eqref{} 引用教材公式编号
- 禁止硬编码如 "证明 (5.2)"
- Label 命名：exr:{章号}-{题号}
```

### 4. causal-expert 额外补充

在 causal-expert 的三角协作架构中，增加了 causal-expert 特有的内容（exercise-expert 习题规范针对 Peng Ding 模板）

### 5. Git 提交

**变更文件**：
- `.claude/.qa_pending` — Skim path troubleshooting Q&A
- `notes/mathematical-statistics/mathematical-statistics-notes.pdf` — PDF 文件变更

**提交记录**：
```
[main 0ea90926] chore: add Skim path troubleshooting Q&A
```

### 6. 团队配置备份

**备份路径**：
```
.claude/teams-backup/literature-experts-config.json (95KB)
```

---

## 最终配置状态

| Agent | PUA 注入 | 三角协作 |
|-------|---------|---------|
| causal-expert | ✅ | ✅ |
| geometry-expert | ✅ | ✅ |
| bayesian-expert | ✅ | ✅ |
| info-geo-expert | ✅ | ✅ |
| schubert-expert | ✅ | ✅ |
| statistic-expert | ✅ | ✅ |
| statistic-expert-2 | ✅ | ✅ |
| writing-expert (×3) | ✅ | ❌ |
| exercise-expert (×4) | ✅ | ❌ |
| latex-checker | ✅ | ❌ |
| qa-specialist | ✅ | ❌ |
| research-expert (×2) | 已有 | ❌ |

---

## 教训总结

### 根因分析
- Team config 在 `~/.claude/teams/` 不在 git 内
- Agent prompt 模板未标准化，每个 agent 独立配置
- 缺少 PUA 自注入导致 agents 无法自我迭代

### 预防措施
1. 团队配置已备份到项目目录 `.claude/teams-backup/`
2. 所有 domain experts 已具备三角协作意识
3. PUA 自注入机制确保每次开工强制读取规范

### 待办
- [ ] 将 `~/.claude/teams/` 目录纳入版本控制（可选）
- [ ] 周期性同步团队配置到备份目录

---

## 文件清单

| 文件 | 路径 | 说明 |
|------|------|------|
| Team config backup | `.claude/teams-backup/literature-experts-config.json` | 完整团队配置备份 |
| Q&A pending | `.claude/.qa_pending` | Skim 问题解答 |
| Session log | `~/Desktop/Claude logs/claude-conversation-2026-03-29-efe8fd79.md` | 原始会话记录 |

---

*Summary extracted from conversation log on 2026-03-30*
