# CLAUDE.md

> **⚠️ 每次开工必须先读本文件。** 本文件是索引，所有详细规范在 `docs/` 目录。

---

## 项目概述

- **项目类型**: 文献阅读与讲义生成工作流系统
- **核心功能**: 阅读学术论文/教材，生成 LaTeX 讲义
- **当前主题**: 因果推断 / Schubert 演算 / 微分几何 / 贝叶斯 / 信息几何

---

## ⚠️ 必须遵守的规则（每次必读）

### PDF 打开规则
- **每次打开 PDF 必须用 Skim**: `open -a Skim <file>`
- **Skim 跳转**: `displayline -r -g <line> "<pdf>" "<tex>"`
  - 示例: `displayline -r -g 650 "/path/file.pdf" "/path/chapter1.tex"`

### LaTeX 格式红线
- ❌ 禁止 Markdown 语法在 .tex 文件中: `**加粗**`, `*斜体*`, `- 列表`, `> [!note]`
- ❌ 禁止 `\bm` — 向量用 `\mathbf`，矩阵用 `\boldsymbol`
- ❌ 禁止 `\I` 自定义命令 — 必须用 `\mathbb{I}`
- ❌ 禁止 unicode 下标 `n₁` → 必须用 `$n_1$`
- ✅ 必须用纯 LaTeX: `\textbf{}`, `\textit{}`, `enumerate/itemize`
- 详见: `docs/latex-style.md`

### Git 大文件禁止
- ❌ 禁止 git 处理 >50MB 文件
- ❌ 禁止 `git lfs` / `filter-repo` / force push
- 详见: `docs/git-rules.md`

### 编译规范
- 必须使用各目录的 `compile.sh`（xelatex, 3次）
- 禁止直接用 `latexmk` / `xelatex`

### QA 记录（强制！）
每次用户提问后必须执行：
1. 口语化回答
2. **记录到 `appendix/qa.tex`**（强制！）
3. 使用 `\subsection{标题}\label{sec:qa-xxx}`
4. 正文用 `\footnote{问：...？见附录 \cref{sec:qa-xxx}}`
5. 重新编译 PDF
- 详见: `docs/qa-workflow.md`

### 章节写作一体化
用户说"生成第X章笔记"时，同时执行：
1. 生成知识点笔记 → `chapters/chapterX.tex`
2. 提取并格式化习题 → 同一文件末尾
3. 推导放附录 → 用 `\footnote{推导见附录 \cref{sec:appendix-chX}}`
- 详见: `docs/exercise-workflow.md`, `docs/stein-writing-style.md`

---

## 📚 规范文档索引

| 文件 | 内容 |
|------|------|
| `docs/latex-style.md` | LaTeX 格式规范、数学符号 |
| `docs/stein-writing-style.md` | Stein 写作风格、推导→附录规则 |
| `docs/exercise-format.md` | 习题格式 (book/Peng Ding 模板) |
| `docs/exercise-workflow.md` | 章节写作工作流 |
| `docs/obsidian-blocks.md` | Obsidian callout 块 |
| `docs/label-reference.md` | label/cref 引用规范 |
| `docs/structure.md` | 目录结构规范、文献库、PDF命名 |
| `docs/qa-workflow.md` | QA 记录工作流 |
| `docs/learning-philosophy.md` | 学习理念 |
| `docs/git-rules.md` | Git 规范 |
| `docs/team-lead-protocol.md` | Team Lead 协议、PUA 注入 |
| `docs/hooks-subagent.md` | Hooks 与 Subagent 自动化 |
| `docs/progress.md` | 主题进度 |

---

## 📁 目录结构

```
notes/<主题>/
├── <主题>-notes.tex      # 主入口
├── compile.sh            # 编译脚本
├── progress.json         # 阅读进度
├── chapters/chapter{0-N}.tex
└── appendix/qa.tex      # QA 记录
```

详细规范: `docs/structure.md`

---

## 📖 主题进度

| 主题 | 书籍 | 笔记路径 | 状态 |
|------|------|----------|------|
| 因果推断 | Peng Ding | `notes/A-First-Course-in-Causal-Inference/` | 1-4章 ✅ |
| 微分几何 | Do Carmo | `notes/differential-geometry/do-carmo-curves-surfaces/` | Ch1-7 ✅ |
| Schubert | 论文集 | `notes/Schubert-Polynomials/` | Ch0-2 ✅ |
| 贝叶斯 | BDA (Gelman) | `notes/bayesian/` | 进行中 |
| 信息几何 | Amari | `notes/information-geometry/` | 进行中 |

详见: `docs/progress.md`

---

## 🔧 教训记忆系统

每次用户纠正错误时 → 记录到 `docs/lessons/` 并更新本文件

| 日期 | 教训 |
|------|------|
| 2026-03-23 | 打开 PDF 默认用 Skim |
| 2026-03-29 | subagent 生成 `\begin theorem}` 缺少 `{` |
| 2026-03-29 | Agent 无响应 → 立即 respawn |
| 2026-03-29 | CLAUDE.md 太长导致 AI 忘记规则 → 重构为索引模式 |

详见: `docs/lessons/`

---

## 🔧 Agent Memory System

literature-experts 团队成员与教训 Memory 文件映射

| Agent | Memory 文件 |
|-------|-------------|
| causal-expert | `docs/lessons/agents/causal-expert-memory.md` |
| geometry-expert | `docs/lessons/agents/geometry-expert-memory.md` |
| bayesian-expert | `docs/lessons/agents/bayesian-expert-memory.md` |
| info-geo-expert | `docs/lessons/agents/info-geo-expert-memory.md` |
| schubert-expert | `docs/lessons/agents/schubert-expert-memory.md` |
| writing-expert | `docs/lessons/agents/writing-expert-memory.md` |
| latex-checker | `docs/lessons/agents/latex-checker-memory.md` |
| qa-specialist | `docs/lessons/agents/qa-specialist-memory.md` |
| exercise-expert | `docs/lessons/agents/exercise-expert-memory.md` |
| gemini-expert | `docs/lessons/agents/gemini-expert-memory.md` |

通用教训: `docs/lessons/agents/ALL-agents-memory.md`

---

## 📝 文献库

| 主题 | 路径 |
|------|------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/` |
| 微分几何 | `PDFs/differential-geometry/Do Carmo - Differential Geometry.md` |
| Stein 系列 | `PDFs/Stein系列/` (需从 minerU 恢复) |
| Quantum Schubert | `PDFs/quantum-schubert/` |

**PDF 命名**: `{姓}-{年份}-{简短标题}` — 详见 `docs/structure.md`
