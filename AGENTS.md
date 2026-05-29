# AGENTS.md
> **⚠️ 每次开工必须先读本文件。** 本文件是索引，详细规范在 `.Codex/rules/` 和 `docs/`。

## ⚠️ 必须遵守的规则（每次必读）

**PDF 打开**：每次打开 PDF 必须用 Skim — `open -a Skim <file>`；跳转用 `/Applications/Skim.app/Contents/SharedSupport/displayline -r -g <line> "<pdf>" "<tex>"` 或 hook `~/.Codex/hooks/skim-jump.sh <line> [tex-file]`

**读 PDF 的正确方式（绝对规则！）**：永远先查 transcript 目录（`PDFs/<topic>/transcript/<论文名>/`）或 `chapters/` 下的 .tex 文件，**不要直接扫描 PDF**。PDF 只用于用户要我打开查看特定页/图、需要视觉确认、或 transcript 不存在时（用 `pages` 参数限制范围）。

**Playwright 缓存保护（绝对红线！）**：禁止清除 Playwright 浏览器缓存（`rm -rf ~/Library/Caches/ms-playwright/`），原因：会丢失 Google 账号登录状态导致 Gemini 无法使用。释放空间用 `pkill -f ms-playwright`。

**LaTeX 格式红线**：
- ❌ `\bm`（向量用 `\mathbf`，矩阵用 `\boldsymbol`）、`\I`（用 `\mathbb{I}`）、unicode 下标 `$n₁$` → `$n_1$`
- ✅ **空括号记号**：空的方括号写成 `[\cdot]`，空的圆括号写成 `(\cdot)` — 这是用户的符号习惯
- ❌ Markdown 语法、`\tag{}` 引用公式
- ✅ 必须 `\label{eq:名称}` + `\cref{eq:名称}`，详细规范见 `.Codex/rules/latex-tex.rules`

**Git 大文件禁止**：禁止 git 处理 >50MB 文件、`git lfs` / `filter-repo` / force push，规范见 `.Codex/rules/git-workflow.rules`

**编译规范**：必须用各目录的 `compile.sh`（xelatex, 3次），禁止直接用 `latexmk` / `xelatex`

**QA 记录（强制！）**：每次用户提问后：1. 口语化回答 → 2. **记录到 `appendix/qa.tex`** → 3. `\subsection{标题}\label{sec:qa-xxx}` + `\footnote{问：...？见附录 \cref{sec:qa-xxx}}` → 4. 重新编译。详细规范见 `.Codex/rules/qa-workflow.rules`

**引用补充规范（核心习惯！）**：当正文中引用了定理/定义但没有给出具体内容时，必须：查找源文件 → 提取内容 → 以 footnote 形式补充 → 加 `\footnote{详见 \cite[ Theorem X.Y]{key}}`

**数学问题调研**：自动使用 `/gemini-browser-chat` 进行深入调研，同时调研笔记上下文。

**写作任务强制路由**：prompt 含"生成第X章笔记"/"写 chapters/"/"润色 .tex"/"写作任务"时，必须用 `/writing-team` Skill 启动 Agent Team（主笔 + 评审，至少 2 轮互发消息讨论）。禁止单 agent 直接输出。按 `.Codex/writer-round-robin.json` 轮询选择 writer pair。

**章节写作一体化**："生成第X章笔记"时 → 知识点笔记 `chapters/chapterX.tex` + 习题 + 推导 `\footnote{推导见附录}`，详见 `docs/exercise-workflow.md`, `docs/stein-writing-style.md`

## 📚 规范文档索引

### `.Codex/rules/` — 自动加载规则

| 文件 | 作用域 | 内容 |
|------|--------|------|
| `latex-tex.rules` | 所有 .tex | LaTeX 语法、数学符号、引用规范 |
| `git-workflow.rules` | 全局 | Git 规范、大文件禁止 |
| `qa-workflow.rules` | 全局 | QA 记录流程、脚注格式 |
| `note-structure.rules` | notes/** | 目录结构、chapter0 格式 |

### `docs/` — 完整参考文档

| 文件 | 内容 |
|------|------|
| `docs/stein-writing-style.md` | Stein 写作风格 |
| `docs/learning-philosophy.md` | 学习理念 |
| `docs/team-lead-protocol.md` | Team Lead 协议 |
| `docs/hooks-subagent.md` | Hooks 与 Subagent 自动化 |
| `docs/progress.md` | 主题进度 |
| `docs/knowledge-profile.md` | 用户知识画像 |
| `docs/lessons/` | 教训记录（每次纠正错误后更新） |
| `.Codex/skills/web-style-learner/SKILL.md` | 网页风格分析 |
| `.Codex/skills/skim-proofread/SKILL.md` | Skim 跳转校验 |
| `.Codex/skills/lesson-capture/SKILL.md` | 经验教训主动记录 |

> **⚠️ 路径别名**：`~/Projects/aca-workflow/notes/Schubert-Polynomials/chapters/chapter5.tex` 是当前活跃章节。

## 🌐 网页风格学习系统
当用户分享 URL + "分析这个网页风格" → Playwright 截图+快照分析 → 保存到 `webpage/style-references/<网站名>/` → 更新 `docs/lessons/web-style-preferences.md`

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

## 📖 主题进度

| 主题 | 书籍 | 笔记路径 | 状态 |
|------|------|----------|------|
| 因果推断 | Peng Ding | `notes/A-First-Course-in-Causal-Inference/` | 1-4章 ✅ |
| 微分几何 | Do Carmo | `notes/differential-geometry/do-carmo-curves-surfaces/` | Ch1-7 ✅ |
| Schubert | 论文集 | `notes/Schubert-Polynomials/` | Ch0-8 ✅ |
| 贝叶斯 | BDA (Gelman) | `notes/bayesian/` | 进行中 |
| 信息几何 | Amari | `notes/information-geometry/` | 进行中 |

详见: `docs/progress.md`

## 🔧 教训记忆系统

每次用户纠正错误 → 记录到 `docs/lessons/` 并更新本表

| 日期 | 教训 |
|------|------|
| 2026-03-23 | 打开 PDF 默认用 Skim |
| 2026-03-29 | subagent 生成 `\begin theorem}` 缺少 `{` |
| 2026-03-29 | Agent 无响应 → 立即 respawn |
| 2026-03-29 | AGENTS.md 太长 → 重构为索引模式 |
| 2026-03-30 | 编译后必须检查 overfull hbox 警告 |
| 2026-03-31 | Proofread 时 AI 报告的问题需用户视觉确认 |
| 2026-03-31 | 统一用 `\cref` 而非 `\ref` |
| 2026-03-31 | "equivariant quantum cohomology" → "等变量子上同调" |
| 2026-04-13 | Step 1 中 $[ ]_{U_n}$ 改为 $[ ]_T$ — 需与约化流程记号一致 |

详见: `docs/lessons/`

## 🔧 Agent Memory System

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
| research-expert | `docs/lessons/agents/research-expert-memory.md` |

通用教训: `docs/lessons/agents/ALL-agents-memory.md`

## 📝 文献库

| 主题 | 路径 |
|------|------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/` |
| 微分几何 | `PDFs/differential-geometry/Do Carmo - Differential Geometry.md` |
| Quantum Schubert | `PDFs/quantum-schubert/` |
| Stein 系列 | `PDFs/Stein系列/` (需从 minerU 恢复) |

**PDF 命名**: `{姓}-{年份}-{简短标题}` — 详见 `docs/structure.md`
