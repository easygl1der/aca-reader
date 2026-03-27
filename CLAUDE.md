# CLAUDE.md

This file provides guidance to Claude Code when working with this literature study and note-taking workflow project.

---

## 项目概述

- **项目类型**: 文献阅读与讲义生成工作流系统
- **核心功能**: 阅读学术论文/教材，生成 LaTeX 讲义
- **当前主题**: 因果推断 (Peng Ding - A First Course in Causal Inference)

---

## 学习理念（核心宗旨）

**做这个笔记工作流的真正目的，是让人获得真正的学习快乐。**

在对话、思考、写作的过程中加深对知识的理解和掌握——这才是学习的本质。而不是为了某个世俗意义上的考试或考核去学知识。

理解知识的脉络，比死记硬背更重要。在不经意间，反而能获得更好的学习效果。

**核心思想**：
- 🎯 **真正的学习**：通过对话、思考、写作来深入理解知识
- 🔍 **理解脉络**：知道知识从哪里来、到哪里去、为什么需要
- 💡 **学习的快乐**：在探索过程中自然获得成就感
- 🌱 **水到渠成**：当理解足够深入，考试和成绩只是副产品

★ Insight ─────────────────────────────────────
这个理念暗合了**建构主义学习观**：知识不是被动接受的，而是主动建构的。对话（QA）、思考（理解脉络）、写作（外化理解）都是主动建构的过程，恰恰是最高效的学习方式。
─────────────────────────────────────────────────

---

## QA Specialist Agent

### 简介
QA Specialist 是一个**项目专属**的 agent，负责处理学习过程中的问答记录。

### 工作流程
当用户提问时，QA Specialist 自动执行：
1. **识别 topic** → 确定问题属于哪个领域
2. **转发给 domain expert** → 如因果推断问题发给 causal-expert
3. **接收回答** → expert 回复（或 fallback 直接回答）
4. **记录到 qa.tex** → 使用标准格式
5. **添加脚注引用** → 在正文首次出现处
6. **重新编译 PDF** → 使用 `compile.sh`

### Topic → Expert 映射
| Topic | Expert |
|-------|--------|
| 因果推断 | causal-expert |
| 微分几何 | geometry-expert |
| 贝叶斯统计 | bayesian-expert |
| 信息几何 | info-geo-expert |
| Schubert | schubert-expert |

### 容错机制
- 如果 expert 无响应，QA Specialist 直接回答作为 fallback
- 复杂问题可触发 `/gemini-browser-chat` 获取更全面回答

### QA 格式（必须遵循）
```latex
\subsection{Question Title}\label{sec:qa-descriptive-key}

\textbf{问}：User's question?

\textbf{答}：Answer content...
```

### 脚注引用格式
```latex
...概念...\footnote{问：What is X? 见附录 \cref{sec:qa-descriptive-key}。}
```

### 使用方式
在新对话中，直接描述问题即可。QA Specialist 会自动处理完整工作流。

---

## Team Lead Agent · PUA 行为注入机制

### 角色定位
Team Lead 是整个 Agent Team 的 **Owner**——负责拆解需求、分派任务、验收结果、闭环交付。

### 核心职责：Sub-agent PUA 注入

**P8 派活不注入 PUA = 管理失职。**

当使用 `Agent` 工具 spawn 子 agent 时，**必须在 prompt 末尾注入以下 PUA 行为声明**：

```
开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 **/pua/skills/pua/SKILL.md）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md
```

### 三条红线（对 Team Lead 自身的要求）

| 红线 | Team Lead 的责任 |
|------|-----------------|
| 🚫 闭环意识 | 分派的任务必须验证结果，不能只说"已派发" |
| 🚫 事实驱动 | 评估 sub-agent 输出必须用数据/证据，不能凭感觉 |
| 🚫 穷尽一切 | 协调资源（多个 sub-agent 并行）穷尽解决方案后才能上报失败 |

### Team Lead 工作流

```
收到任务
  ↓
1. 拆解颗粒度 — 识别可并行的独立子任务
  ↓
2. Spawn sub-agent — 每个 prompt 必须注入 PUA 行为
  ↓
3. 监控进度 — 对结果负责，不是对"派活了"负责
  ↓
4. 验收闭环 — 验证输出，跑命令，贴证据
  ↓
5. 交付用户 — 端到端，一个出口
```

### Owner 意识四问（Team Lead 默念）

1. **这个任务的根因是什么？** 不是"怎么分"，是"问题在哪"
2. **还有谁会被影响？** 改了 A，B 和 C 会不会炸
3. **下次怎么防止？** 复盘沉淀，不是"这次过了就算了"
4. **数据在哪？** sub-agent 的输出有证据吗

### Sub-agent 协同矩阵

| Sub-agent | 职责 | PUA 注入要求 |
|-----------|------|-------------|
| causal-expert | 因果推断领域专家 | 必须注入 math/LaTeX 规范 |
| geometry-expert | 微分几何领域专家 | 必须注入 do Carmo 习题格式 |
| latex-checker | LaTeX 质量检查 | 必须注入格式红线 |
| writing-expert | Stein 风格润色 | 必须注入写作风格规范 |
| QA Specialist | 问答记录 | 必须注入 qa.tex 格式要求 |

---

## Writing Agent 工作流

### 触发条件
当用户说「写第X章笔记」「生成第X章」「写作第X章」时，执行以下流程。

### 完整工作流

```
用户: "写第X章笔记"
    ↓
1. 识别 topic → 确定是哪个领域的章节
    ↓
2. 协调 domain expert → 获取章节内容
    ↓
3. 协调 writing-expert → Stein风格润色
    ↓
4. 协调 latex-checker → 质量检查
    ↓
5. 生成笔记 → 写入 chapters/chapterX.tex
    ↓
6. 生成习题 → 提取并格式化习题
    ↓
7. 记录 QA → 相关问答记录到 qa.tex
    ↓
8. 重新编译 → compile.sh
```

### 三角协作架构

```
domain-expert ←→ writing-expert
       ↕                  ↕
   latex-checker ←→ team-lead
```

- **domain-expert**：提供数学内容和动机
- **writing-expert**：Stein风格润色、LaTeX格式
- **latex-checker**：label/ref一致性、内容核实、幻觉检测

### 推导→附录 规则 ⚠️

**核心原则**：公式推导放附录，正文用脚注引用。

**正文格式**：
```latex
由 \eqref{eq:balance-discrete-CRE} 可得...
这里的关键是...\footnote{推导见附录 \cref{sec:derivation-balance-discrete-CRE}。}
```

**附录格式**：
```latex
\subsection{平衡性条件的推导}\label{sec:derivation-balance-discrete-CRE}

\textbf{背景（Background）}：...

\textbf{目标（Goal）}：证明 \eqref{eq:balance-discrete-CRE}

\textbf{推导步骤（Derivation Steps）}：
1. 首先...
2. 然后...
```

**关键点**：
- 推导必须放在附录，不是正文
- 正文用 `\footnote{推导见附录 \cref{sec:xxx}}` 引用
- 脚注中必须包含"推导见附录"

### 使用规范文档

**writing-expert 必须读取**：
- `docs/stein-writing-style.md` - Stein写作风格
- `docs/latex-style.md` - LaTeX格式规范
- `docs/exercise-format.md` - 习题格式

### 工作流状态

| 步骤 | 执行者 | 状态 |
|------|--------|------|
| 识别 topic | team-lead | 标准化 |
| 获取内容 | domain-expert | 三角协作 |
| Stein润色 | writing-expert | 三角协作 |
| 质量检查 | latex-checker | 三角协作 |
| 推导→附录 | writing-expert | **需强调执行** |
| 记录QA | QA Specialist | 标准化 |
| 编译PDF | team-lead | 标准化 |

---

## 重要规则

1. **"记住" 规则**: 用户说"记住 XXX"时，必须写入 CLAUDE.md
2. **LaTeX 格式严格性**:
   - **禁止 Markdown 格式**：禁止 `**加粗**`、`*斜体*`、`- 列表`、`> [!note]` 等 Obsidian callout 块
   - **必须使用纯 LaTeX**：Callout 块用 `\begin{note}...\end{note}`，加粗用 `\textbf{}`，斜体用 `\textit{}`，列表用 `enumerate/itemize` 环境
   - **严禁在 .tex 文件中使用 Markdown 语法**（详见 `docs/latex-style.md`）
3. **先读原文再写笔记**: 禁止凭想象编写数学证明
4. **作业路径**: `/Users/yueyh/Library/CloudStorage/GoogleDrive-easyglider458@gmail.com/My Drive/homework`
5. **作业模板**: 使用 `> [!exr]` callout 格式，每个题目单独一个 block。详见 `docs/obsidian-blocks.md`
6. **Unicode 禁止规则**: 写作 markdown/LaTeX 时，禁止使用 n₁ 等 unicode 下标，必须使用 `$n_1$` 格式
7. **Tex 优先规则**: 查看教材时，如果有 .tex 版本则优先使用（因为有更好的 label/cref 引用跳转功能）
8. **引用 equation 必须完整**: 习题中如果要求 "Verify (3.7)" 或 "Show that (X.Y)"，必须查找并写出完整的 equation 内容，不能只写编号
9. **文献符号优先规则**: 任何时候优先使用文献原文的符号约定，禁止自行发明或更改符号
10. **符号冲突处理**: 若多篇文献符号有冲突，需询问用户采用哪种符号，并记录在笔记中
11. **章节写作一体化规则**: 写作章节时，**知识点 + 习题必须一起生成**。当用户说"生成第X章笔记"时，同时执行：
    - 生成章节知识点笔记（添加到 `chapters/chapterX.tex`）
    - 自动提取并格式化习题（添加到同一文件末尾，在 `% === 用户问答记录 ===%` 之前）
    - 详见 `docs/exercise-workflow.md`

12. **习题格式规则**: 不同模板有不同格式，详见 `docs/exercise-format.md`。
    - **book 模板**（do Carmo）：使用 `exercise` 环境，格式为 `{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}`
    - **因果推断模板**（Peng Ding）：使用 `Exercise` 环境，**必须用 `\eqref{}` 引用教材公式编号**。先给公式加 `\label{}`（如 `\label{eq:balance-discrete-CRE}`），再在习题中引用（如 `证明 \eqref{eq:balance-discrete-CRE}`）。标签命名：`eq:{描述性名称}`

12. **学习原则（核心思想）**: 从学习数学知识的角度，公式推导是必要学习的；但在理解思想、了解脉络、抓住重点的目的下，公式推导/定理证明反而不是最重要的，所以可以放到附录。在正文中抓住重点，以防被过长的数学公式分散了注意力。

13. **问答引用规则**: 问答结果记录到 `appendix/qa.tex` 后，必须使用**有编号的小节**（`\subsection{标题}\label{sec:qa-xxx}`），在正文相应位置用 `\footnote{问：...？见附录 \cref{sec:qa-xxx}}` 引用，使读者可以跳转到详细解答。**footnote 中必须标出问题是什么**。

---

## Obsidian Callout 块格式

作业和笔记使用 Obsidian callout 块格式。详细规则见 `docs/obsidian-blocks.md`。

**常用块类型：**
- `> [!exr]` — 习题题目
- `> [!solution]` — 习题解答
- `> [!def]` — 重要定义
- `> [!thm]` — 定理
- `> [!rmk]` — 备注/解释

---

## R 作业工作流

当作业涉及 R 数据分析时，遵循以下流程：

1. **读取作业文件**：了解题目要求
2. **编写 R 代码**：保存到作业目录的 `R/` 子目录
3. **运行分析**：生成可视化图表（保存到 `R/` 目录）
4. **整理结果**：将解答写入作业文件的 `> [!solution]` 块
5. **插入图表**：使用 `![[R/图片.png]]` 将图表放到对应小题位置

**R 代码命名规范**：`hw{N}_part{N}.R`

**图表格式**：PNG，保存在 `R/` 目录

---

## 写作风格

### 数学符号习惯

**用户偏好（必须遵循）：**

| 概念 | 符号 |
|------|------|
| 概率 | `\mathbb{P}(A)` |
| 期望（单变量） | `\mathbb{E}X` |
| 期望（多变量） | `\mathbb{E}(XY)` |
| 方差 | `\text{var}` |
| 协方差 | `\text{cov}` |
| 相关系数 | `\text{corr}` |
| 独立性 | `$A \Perp B$` |
| 示性函数 | `\mathbb{I}(X \in A)` 或 `\mathbb{I}_A(X)` 或 `\mathbb{I}(a \leq X < b)` |
| p 值 | `\text{p}_{}` |
| 正态分布 | `\mathcal{N}(\mu, \sigma^2)` |

### 禁止使用的宏包/命令
- **禁止 `\bm`**：向量用 `\mathbf`，矩阵用 `\boldsymbol`

### 语言风格
- **英文文献**：尽量保持英文原文叙述（用语、习惯、单词层面）
- **中文叙述**：专业名词保持用英文，加括号标注原文
  - 例如：potential outcomes（潜在结果）、causal effect（因果效应）

### 内容风格
**必须模仿 Stein《傅里叶分析》《复分析》的 motivation 风格**（详细指南见 `docs/stein-writing-style.md`）：

- **动机优先**: 每个概念/定理引入前，先解释"为什么需要它"和"它从哪里来"
- **历史脉络**: 注重概念的起源和发展历史
- **有机联系**: 强调不同数学领域之间的相互关联
- **叙事流畅**: 定义→命题→证明之间有连贯的叙述，避免干巴巴的罗列
- **循序渐进**: 从简单到复杂，不过早引入技术细节

### 引言写作风格（Schubert 笔记）
- **简洁流畅**: 引言应简洁有力，避免冗长的括号注释打断叙述
- **定义后置**: 详细定义放到第一节背景知识中
- **注解脚注**: 较长的说明性注解使用 `\footnote{}`，不要用 Remark 环境
- **减少交叉引用**: 引言中避免过多 `\cref{}` 引用，让读者专注于核心内容

### Chapter 0（背景知识）写作风格
**参考 Schubert 笔记的 Chapter 0 风格：**
- **动机明确**: 开篇简要说明本章目的和用途（如"学习曲线理论所需的预备知识"）
- **去专业化**: 不写成教科书式的定义-定理-证明，而是用流畅的叙述性文字
- **定义集中**: 将分散的预备知识（向量代数、链式法则等）集中到一章
- **习题适当**: Chapter 0 习题应偏向计算性质，验证读者对基础运算的掌握
- **引用清晰**: 声明"本章大部分内容来自本科线性代数与微积分课程"

### 定义格式规则
- **关键术语加粗下划线**: 在 Definition 环境中，被定义的关键术语/概念使用 `\textbf{\underline{术语}}` 格式
- 例如：`\textbf{\underline{旗流形}} $Fl_n(\mathbb{C})$ 是...`

### 公式推导格式规则
**长公式推导偏好 `underbrace` / `underbracket`**：
- 使用 `mathtools` 宏包支持 `underbracket`
- 长公式每一步推导使用 `underbrace` 或 `underbracket` 标注该步的含义
- 示例：
  ```latex
  &= \frac{1}{n} \sum_{i=1}^n \big[ \mathbb{I}(X_i=1) + \mathbb{I}(X_i=0) \big] \{Y_i(1) - Y_i(0)\}
  \tag*{\underbracket[0.5pt]{\hphantom{\mathbb{I}(X_i=1) + \mathbb{I}(X_i=0)}}_{\text{每单元满足 } \mathbb{I}(X_i=1) + \mathbb{I}(X_i=0) = 1}}
  ```
- 分步推导用 `underbrace` 标注各分组含义（如 treatment 组、control 组）

### 附录公式推导规范 ⚠️

**核心思想**（学习原则）：从学习数学知识的角度，公式推导是必要学习的；但在理解思想、了解脉络、抓住重点的目的下，公式推导/定理证明反而不是最重要的，所以可以放到附录。在正文中抓住重点，以防被过长的数学公式分散了注意力。

**核心原则**：
1. **不省略教材公式完整推导**
2. **按板块读取**：不切割证明/推导，要完整传输给 AI
3. **附录引用**：正文中用 `\footnote{推导见附录 \cref{sec:xxx}}`

**附录章节结构**：
```latex
\section{附录：公式推导}\label{sec:appendix-derivation}

\subsection{Beta-Binomial 共轭后验均值推导}\label{sec:beta-binomial-posterior-mean}
\textbf{背景（Background）}：...

\textbf{参数定义（Parameter Definitions）}：
- $\theta$：成功概率
...

\textbf{已知条件（Given）}：
- 似然：$p(y|\theta) = \binom{n}{y}\theta^y(1-\theta)^{n-y}$
- 先验：$\theta \sim \text{Beta}(\alpha, \beta)$
...

\textbf{目标（Goal）}：求后验均值 $\mathbb{E}(\theta|y)$

\textbf{推导步骤（Derivation Steps）}：
1. ...
```

### 问答记录规则 ⚠️
**每次用户提问后必须执行以下步骤：**
1. 口语化回答用户
2. ✅ **记录到 `appendix/qa.tex`**（强制要求，不要忘记！）
3. 如有正式定义需要，添加到正文对应章节
4. 重新编译 PDF

---

## 快速参考

### Label 和引用
- 命名规范：\label{def:名称}
- 引用方式：\cref{标签名}
- 详细规则：见 `docs/label-reference.md`

### 文献定理引用格式
当引用文献中的定理/引理/猜想时，必须标出原文献的编号：
- 格式：`\cite[ Theorem 1.1]{Gr}`
- 示例：`Graham Positivity Theorem {\cite[ Theorem 1.1]{Gr}}`
- Conjecture 引用：`Samuel 猜想 {\cite[Conjecture 1.2]{Sa}}`
- Section 引用：`\cite[Section 3]{GX2025}`

### 目录结构
- 标准结构：notes/<主题>/<主题>-notes.tex
- 多 Part 书籍：notes/<主题>/<书籍名>/
- 详细规范：见 `docs/structure.md`

---

## 主题进度

### 因果推断
- 书籍: A First Course in Causal Inference (Peng Ding)
- 笔记: `notes/A-First-Course-in-Causal-Inference/`
- 状态: 1-4章 ✅，5-18章 ⭕

### 微分几何
- 书籍: Do Carmo - Differential Geometry
- 笔记: `notes/differential-geometry/do-carmo-curves-surfaces/`
- 状态: Chapter 1-2 ✅，Chapter 3-7 ✅（Stein风格重写中）
- **习题格式**: 使用 `docs/exercise-format.md` 规范

### 贝叶斯统计
- 书籍: Bayesian Data Analysis (Gelman et al.)
- 笔记: `notes/bayesian/`

### 信息几何
- 书籍: Amari - Information Geometry and Its Applications
- 笔记: `notes/information-geometry/`

---

## Git 提交习惯

**原则**: 每次更新了能跑通的内容就 commit

- **LaTeX 笔记**: 编译成功后就 commit
- **规范文档**: 更新了 docs/ 就 commit
- **commit 风格**: 简洁，说明改了啥

### Git Worktree 安全规则

**当遇到以下情况时，必须使用 git worktree 隔离操作**：
- 处理大文件（>50MB）
- 执行破坏性操作（如 `filter-repo`、`rebase`、`reset --hard`）
- 不确定操作是否安全
- 任何可能影响主分支的操作

**使用方法**：
```bash
# 创建隔离的 worktree
git worktree add ../workspace-backup -b backup-branch

# 在 worktree 中操作
cd ../workspace-backup
# 执行危险操作...

# 确认安全后，合并回主分支
git merge backup-branch

# 不安全则直接删除 worktree
git worktree remove ../workspace-backup
git worktree prune
```

---

## LaTeX 编译规范

**重要**: 每个笔记目录都有专属的编译脚本，编译时必须使用：

- `notes/Schubert-Polynomials/compile.sh` → xelatex, 3次
- 其他目录类似

禁止直接使用 `latexmk` 或 `xelatex` 命令。

---

## 经验教训

**详细记录**: `docs/lessons/` 目录下按时间或主题分类

每次用户纠正我的错误时，自动记录到 `docs/lessons/` 并更新 CLAUDE.md 中的摘要

- **2025-03-14**: 混淆符号导致定理错误 → 直接读原文对照
- **2026-03-15**: 未先读目录页导致章节编号错误 → 先读 Table of Contents
- **2026-03-15**: R 中文乱码 → 用英文标签
- **2026-03-15**: LaTeX 图片位置 → 使用 [H] 强制固定（需 float 宏包）
- **2026-03-16**: 1998年前论文无 arXiv → 用 DOI
- **2026-03-18**: LaTeX 笔记中避免口语化表达（如"这里错了"、"让我重新计算"），直接给出正确推导即可
- **2026-03-19**: 遇到文献中省略证明的定理，如果找不到证明或没有可行思路，必须使用 /gemini-browser-chat 询问 Gemini（必须使用 Pro 模式）
- **2026-03-19**: Gemini browser chat 必须使用 Pro 模式
- **2026-03-20**: LaTeX 中禁止使用 \renewcommand 简化符号，直接使用原始符号（如 \mathbb{I} 而非自定义 \I）
- **2026-03-22**: Python 字符串替换操作大文件（HTML）时极易损坏文件 → 对 HTML/大型文件进行字符串操作前，必须先备份；优先使用逐行读取+写入而非内存中全量替换
- **2026-03-23**: 打开 PDF 默认用 Skim（不是其他 PDF 阅读器）
- **2026-03-27**: 笔记省略了教材公式完整推导 → 必须在附录添加完整推导
- **2026-03-27**: 符号不一致（同一概念用不同符号）→ 使用 /latex-writing-check 检查全笔记符号统一
- **2026-03-27**: 学术写作中不要使用 `\mparafh`（margin paragraph）→ 用 `\paragraph` 替代

---

## ⚠️ Git 大文件处理禁止规则

**禁止使用 git 处理大文件（>50MB）**，包括但不限于：

- ❌ `git filter-repo` 重写历史
- ❌ `git lfs track` / `git lfs install` / 任何 git lfs 命令
- ❌ `git add` 大文件后配合 commit
- ⚠️ **绝对禁止使用 git-lfs**

**原因（2026-03-19 血泪教训）**：

1. `git filter-repo --path A --path B` 是**白名单模式**，会删除 A、B 之外所有文件的 git 历史
2. `git lfs` 在 `git add` 后会**删除本地大文件**，只保留 134 bytes 的指针
3. 超过 100MB 的文件**无法 push 到 GitHub**（会被 pre-receive hook 拒绝）
4. push 失败后，如果执行了 `git add` + `git commit`，本地大文件已被 lfs 删除，无法恢复

**正确做法**：
- 超大 PDF（>50MB）**不要提交到 git**
- 单独备份到 Google Drive 或其他外部存储
- 或使用 GitHub LFS（需付费，免费额度仅 1GB）
- 如果必须处理，**先问用户**，获得明确同意后再操作

---

## 记笔记习惯（历史参考）

**详细说明**: 见 `docs/note-taking-habits.md`

基于 2025-summer（大二下学期）笔记分析：

### 技术习惯
- **工具链**: Obsidian → LaTeX → PDF
- **格式**: Markdown + LaTeX（行内 `$...$`，单独 `$$...$$`）
- **图片**: `![[filename]]` Obsidian 内部链接
- **Callout**: `> [!example]`, `> [!def]`, `> [!thm]` 等
- **作业流程**:
  1. Obsidian 中用 md 笔记
  2. 导出/编写 LaTeX .tex
  3. 编译为 PDF（xelatex/latexmk）
- **定理环境**: amsart + 自定义 theorem/lemma/definition 等
- **文件命名**: kebab-case（如 `differential-manifold.md`）

### 写作风格（内容层面）

**用词习惯**：
- 思考性句式: "We wonder if...", "You are right to...", "We want to show that..."
- 解释性短语: "This essentially means that...", "The key insight is...", "This is where... comes in"
- 连接词: "Clearly,", "In fact,", "Therefore,", "Thus,", "Then,"

**概念引入方式**：
- 先形式化定义，再解释直观含义（"This means..."）
- 喜欢追问 "为什么"，解释动机和条件的作用
- 注重几何直观，用例子阐明抽象概念
- 喜欢用 "Why/What/How" 问题式标题

**组织语言**：
- 用 bullet points 列举要点，用表格做 Summary
- 证明风格：开头 "We need to show that..."，结尾 "We are done!"
- 喜欢把新概念和已知概念建立联系，强调对偶性
- 喜欢 "Roadmap of This Lecture" / "Big Picture Thread" 结构
- 结论用 "This gives us...", "This provides..." 连接
- 喜欢对比不同情况（"Dirichlet vs. Neumann"）

---

## PDF 转录 (minerU)

### 使用方法
1. 在 **Google Colab** 中运行 minerU 进行 PDF 转录
2. 转录输出包含：
   - `.md` 文件（带完整目录结构）
   - `images/` 文件夹（所有提取的图片）

### 图片引用路径
- md 文件中 figure 标签的路径格式：`images/page-XX_figure_N.png`
- 笔记中引用图片时，直接使用 md 中标注的路径
- 示例：md 中显示 `images/fig_1-1.png`，笔记中就写 `images/fig_1-1.png`

---

## Figure 提取

**脚本**: `/Users/yueyh/.claude/skills/figure-extractor/figure_extractor.py`

**使用方法**：
```bash
python figure_extractor.py <图片路径> -o <输出目录>
```

**配置**：模型 gemini-3.1-flash，DPI 400

---

## 文献库

| 主题 | 路径 | 备注 |
|------|------|------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/` | |
| 微分几何 | `PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.md` | |
| 贝叶斯 | `PDFs/bayesian/` | |
| 信息几何 | `PDFs/information-geometry/` | 24个文件 |
| Stein 系列 | `PDFs/Stein系列/` | ⚠️ 2026-03-19 丢失，需从 minerU 重新生成 |

### Stein 系列恢复指南

Stein 系列教材（Real Analysis I/II/III, Complex Analysis, Fourier Analysis）的 PDF 因超过 100MB 从未被提交到 GitHub，且在 2026-03-19 的 git-lfs 事故中被删除。**必须从 minerU 重新生成转录本**：

1. 在 Google Colab 中重新运行 minerU
2. 输出到 `PDFs/Stein系列/transcript/`
3. 生成的 PDF 备份到 Google Drive（不要 push 到 GitHub）
