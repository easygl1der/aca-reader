# 文献阅读与讲义生成工作流 - 实现计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 创建一个模拟用户阅读文献、学习知识、生成个性化 LaTeX 讲义的工作流系统

**Architecture:** 这是一个基于 Claude Code 的对话式工作流，主要通过 skills 和对话交互来驱动 LaTeX 讲义生成。不需要复杂的后端，主要利用 Claude Code 的记忆系统和文件操作能力。

**Tech Stack:**
- Claude Code (对话、记忆、文件操作)
- Skills (PDF 解析、LaTeX 生成)
- Markdown (进度仪表盘)
- JSON (数据存储)
- LaTeX (讲义输出)

---

## Task 1: 创建项目结构和基础文件

**Files:**
- Create: `aca-workflow/README.md`
- Create: `aca-workflow/docs/plans/2026-03-05-literature-reading-workflow-design.md` (已存在)

**Step 1: 创建 README.md**

```markdown
# 文献阅读与讲义生成工作流

## 概述

一个模拟用户阅读文献、学习知识、生成个性化 LaTeX 讲义的工作流系统。

## 功能

- PDF 文献/教材解析
- 两阶段阅读流程（扫描 + 逐章）
- 交互式问答
- LaTeX 讲义生成（Stein 风格）
- 阅读记忆系统
- 进度仪表盘

## 使用方法

1. 加载 PDF 文件
2. 进行扫描阶段
3. 逐章阅读并提问
4. 查看生成的 LaTeX 讲义
5. 导出 PDF

## 项目结构

```
├── README.md
├── docs/
│   └── plans/
├── src/
│   └── skills/
└── config/
```

**Step 2: 提交**

```bash
git init
git add README.md docs/plans/2026-03-05-literature-reading-workflow-design.md
git commit -m "feat: 初始化项目结构"
```

---

## Task 2: 创建用户偏好配置文件

**Files:**
- Create: `aca-workflow/config/user-preferences.json`
- Create: `aca-workflow/config/user-preferences.md`

**Step 1: 创建 user-preferences.json**

```json
{
  "writing_style": {
    "reference_books": [
      "Stein - Complex Analysis",
      "Stein - Fourier Analysis"
    ],
    "characteristics": [
      "motivation-driven",
      "beginner-friendly",
      "clear narrative flow",
      "connecting concepts to prior knowledge"
    ]
  },
  "reading_habits": {
    "two_phase": true,
    "phase1_scanning": {
      "purpose": "了解整体框架、与已有知识的关联、需要先备的知识"
    },
    "phase2_detailed": {
      "chapter_overview_first": true,
      "distinguish_core_vs_detail": true,
      "mark_confusing_parts": true
    }
  },
  "latex_structure": {
    "one_file_per_chapter": true,
    "one_file_per_section": true,
    "main_file_integration": true,
    "include_user_annotations": true,
    "cross_references": true
  }
}
```

**Step 2: 创建 user-preferences.md**

```markdown
# 用户偏好配置

## 写作风格

- 参考书籍：Stein《复分析》《傅里叶分析》
- 特点：动机驱动、易于初学者、理解、清晰的叙事流程、将概念与已有知识关联

## 阅读习惯

- 两阶段阅读
  - 阶段一（扫描）：了解整体框架、与已有知识的关联、需要先备的知识
  - 阶段二（详细）：
    - 先看章节概览
    - 区分核心与细节
    - 标记困惑之处

## LaTeX 结构

- 每章一个文件
- 每节一个文件
- main.tex 整合
- 包含用户注解
- 交叉引用
```

**Step 3: 提交**

```bash
git add config/user-preferences.json config/user-preferences.md
git commit -m "feat: 添加用户偏好配置"
```

---

## Task 3: 创建阅读进度管理 Skills

**Files:**
- Create: `aca-workflow/.claude/skills/reading-progress/SKILL.md`
- Create: `aca-workflow/.claude/skills/reading-progress/progress.json`
- Create: `aca-workflow/.claude/skills/reading-progress/progress.md`

**Step 1: 创建 SKILL.md**

```yaml
---
name: reading-progress
description: 管理阅读进度，包括当前阅读位置、历史提问、章节状态
user-invocable: true
---

# 阅读进度管理 Skill

## 功能

1. 记录当前阅读位置（第几章、哪一节）
2. 追踪每个章节的阅读状态（未读/在读/已读/有疑问）
3. 记录用户的提问历史
4. 展示阅读仪表盘

## 使用方式

- "我现在在读第3章第2节"
- "我不懂这个定理" - 自动记录问题位置
- "我的阅读进度怎么样了"
- "这一章我觉得很难"

## 数据存储

进度存储在 `reading-progress/progress.json` 和 `progress.md`

## 输出格式

生成进度仪表盘：
- JSON：机器可读
- Markdown：人类可读，可包含 Mermaid 图
```

**Step 2: 创建 progress.json 初始结构**

```json
{
  "current_position": {
    "chapter": null,
    "section": null,
    "page": null
  },
  "chapters": {},
  "questions": [],
  "sessions": []
}
```

**Step 3: 创建 progress.md 初始结构**

```markdown
# 阅读进度仪表盘

## 当前进度

未开始阅读

## 阅读历史

暂无

## 待解答问题

暂无
```

**Step 4: 提交**

```bash
git add .claude/skills/reading-progress/
git commit -m "feat: 添加阅读进度管理 skill"
```

---

## Task 4: 创建 PDF 解析 Skill

**Files:**
- Create: `aca-workflow/.claude/skills/pdf-reader/SKILL.md`

**Step 1: 创建 SKILL.md**

```yaml
---
name: pdf-reader
description: 解析 PDF 文献，提取章节结构，理解内容框架
user-invocable: true
---

# PDF 解析 Skill

## 功能

1. 读取 PDF 文件内容
2. 提取章节结构（章、节、小节标题）
3. 识别核心定理/定义
4. 生成章节概览

## 使用方式

- 加载 PDF："帮我解析这个 PDF"
- 查看结构："这本书的章节结构是什么"
- 章节概览："第3章讲了什么"

## 输出

- 章节结构树
- 每章的核心目标
- 核心定义/定理列表

## 注意事项

- 使用 OCR 或 PDF 解析工具读取内容
- 提取标题作为章节标记
- 识别数学定理和定义（通常有编号如 Theorem 1.1, Definition 2.3）
```

**Step 2: 提交**

```bash
git add .claude/skills/pdf-reader/
git commit -m "feat: 添加 PDF 解析 skill"
```

---

## Task 5: 创建 LaTeX 讲义生成 Skill

**Files:**
- Create: `aca-workflow/.claude/skills/latex-notes/SKILL.md`
- Create: `aca-workflow/.claude/skills/latex-notes/templates/main.tex`
- Create: `aca-workflow/.claude/skills/latex-notes/templates/chapter.tex`
- Create: `aca-workflow/.claude/skills/latex-notes/templates/section.tex`

**Step 1: 创建 SKILL.md**

```yaml
---
name: latex-notes
description: 生成 LaTeX 格式的学习讲义，包含用户注解、问题、Stein 风格的 motivation 写作
user-invocable: true
---

# LaTeX 讲义生成 Skill

## 功能

1. 根据阅读进度生成对应章节的 .tex 文件
2. 在定义/命题/证明之间插入用户注解
3. 记录问答内容到附录
4. 生成 main.tex 整合所有章节
5. 交叉引用支持

## 使用方式

- "帮我更新第3章第2节的讲义"
- "把这个问题和解答加到讲义里"
- "生成 main.tex"

## 讲义风格

参考 Stein 的写作风格：
- 动机驱动：先解释为什么需要这个概念
- 与已有知识关联
- 清晰的叙事流程
- 不是干巴巴的定义定理证明，而是有"为什么"的解释

## 文件结构

```
main.tex
├── chapters/chapter1/
│   ├── section1.tex
│   ├── section2.tex
│   └── ...
├── chapters/chapter2/
│   └── ...
└── appendix/qa.tex
```

## 用户注解格式

在定理/定义/证明之间插入：

```latex
% === 用户注解 ===
% 问题：为什么需要引入这个概念？
% 解答：...
% 关联：与第2章的XX定理有关联
% ===
```

**Step 2: 创建模板文件 main.tex**

```latex
\documentclass{book}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{xeCJK}
\usepackage{hyperref}

% Theorem environments
\newtheorem{定理}{定理}[chapter]
\newtheorem{定义}{定义}[chapter]
\newtheorem{引理}{引理}[chapter]
\newtheorem{推论}{推论}[chapter]

% User annotation command
\newcommand{\注解}[1]{\marginpar{#1}}

\title{学习讲义}
\author{用户}

\begin{document}

\maketitle
\tableofcontents

% Chapters will be included here
\input{chapters/chapter1/section1}
\input{chapters/chapter1/section2}
% ...

\appendix
\input{appendix/qa}

\end{document}
```

**Step 3: 创建章节模板 chapter.tex**

```latex
\chapter{第章标题}
\label{chap:chaptername}

% 章节概述
\section*{本章概述}
本章的核心目标是...

% Sections
\input{section1}
\input{section2}
```

**Step 4: 创建节模板 section.tex**

```latex
\section{节标题}
\label{sec:sectionname}

\subsection{背景与动机}
% 解释为什么需要这个概念

\subsection{主要内容}
% 定义、定理、证明

\subsection{与之前的关联}
% 与前面章节的联系
```

**Step 5: 提交**

```bash
git add .claude/skills/latex-notes/
git commit -m "feat: 添加 LaTeX 讲义生成 skill 和模板"
```

---

## Task 6: 创建对话式问答 Skill

**Files:**
- Create: `aca-workflow/.claude/skills/interactive-qa/SKILL.md`

**Step 1: 创建 SKILL.md**

```yaml
---
name: interactive-qa
description: 交互式问答，理解用户当前阅读位置，实时回答问题并同步更新讲义
user-invocable: true
---

# 交互式问答 Skill

## 功能

1. 理解用户当前阅读位置（哪章哪节哪个定理）
2. 实时回答用户问题
3. 区分两种输出风格：
   - 对话回答：让初学者能看懂
   - 讲义记录：Stein 风格的 motivation 写作
4. 自动更新进度和问题记录

## 使用方式

- "我不懂这个定理"
- "这个定理是干嘛的"
- "证明我没看懂"

## 对话风格 vs 讲义风格

- 对话：口语化、详细解释、举例说明
- 讲义：格式化、motivation驱动、与其他知识关联

## 自动更新

每次问答后：
1. 记录问题到 progress.json
2. 更新讲义对应的 .tex 文件
3. 添加用户注解块
```

**Step 2: 提交**

```bash
git add .claude/skills/interactive-qa/
git commit -m "feat: 添加交互式问答 skill"
```

---

## Task 7: 创建主工作流 Skill (Orchestrator)

**Files:**
- Create: `aca-workflow/.claude/skills/reading-workflow/SKILL.md`

**Step 1: 创建 SKILL.md**

```yaml
---
name: reading-workflow
description: 主工作流 - 协调扫描阶段、逐章阅读、问答、讲义生成
user-invocable: true
---

# 文献阅读主工作流

## 概述

这是主要的工作流入口，协调各个子模块。

## 工作流程

### 阶段一：扫描
1. 加载 PDF
2. 解析章节结构
3. 生成章节概览
4. 识别核心定理/定义

### 阶段二：逐章阅读
1. 用户选择章节
2. 展示章节概览和核心目标
3. 进入交互式问答模式
4. 实时更新讲义

### 阶段三：进度管理
1. 记录阅读位置
2. 更新进度仪表盘
3. 保存问答历史

## 使用方式

- "帮我加载这个 PDF"
- "开始扫描"
- "我要读第3章"
- "我的阅读进度如何"
- "生成讲义"
```

**Step 2: 提交**

```bash
git add .claude/skills/reading-workflow/
git commit -m "feat: 添加主工作流 skill"
```

---

## Task 8: 整合所有 Skills 并测试

**Step 1: 创建 .claude/config.json**

```json
{
  "skills": [
    "reading-workflow",
    "reading-progress",
    "pdf-reader",
    "latex-notes",
    "interactive-qa"
  ],
  "memory": {
    "enabled": true,
    "type": "user"
  }
}
```

**Step 2: 验证整体结构**

```bash
find . -type f -name "*.md" -o -name "*.json" -o -name "*.tex" | head -20
```

**Step 3: 提交**

```bash
git add .claude/config.json
git commit -m "feat: 整合所有 skills 配置"
```

---

## 执行方式

**Plan complete and saved to `docs/plans/2026-03-05-literature-reading-workflow-implementation.md`.**

**Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
