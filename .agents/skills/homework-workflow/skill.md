# Homework Workflow Skill

## 功能

从 homework PDF 或教材中提取作业题目，生成双格式（Obsidian markdown + LaTeX tex）的作业笔记，并关联教材内容。

## 触发条件

- 用户说"读取作业"、"解析 homework"、"帮我看作业有哪些"
- 用户提供了 homework PDF 路径
- 用户要求生成作业笔记
- 用户说"做作业"、"写 homework"

---

## 工作流程

### Step 1: 确定作业来源

| 来源 | 说明 | 处理方式 |
|------|------|----------|
| **教材习题** | 老师在教材上勾的习题 | 从教材 transcript/tex 提取 |
| **PDF 作业** | 老师发的 PDF 文件 | 用 mineru 或 pymupdf 扫描提取 |

### Step 2: 检查教材 transcript / tex

**优先使用已有 .tex 或 .md 文件**，不要重复从 PDF 提取。

1. 搜索是否有对应教材的 transcript (.md) 或笔记 (.tex)：
   ```
   Glob: PDFs/<主题>/transcript/**/*.md
   Glob: notes/<主题>/**/*.tex
   ```

2. 如果有 .tex 文件 → 读取 .tex（更好的 `\label` / `\cref` 跳转）
3. 如果只有 .md 文件 → 读取 .md 转录本
4. **只有当没有 transcript 也没有 tex 时**，才从 PDF 解析

### Step 3: 解析 Homework PDF

使用 `pymupdf` (fitz) 提取 PDF 文本：

```python
import fitz
doc = fitz.open('/path/to/homework.pdf')
for page in doc:
    print(page.get_text())
```

### Step 4: 选择 LaTeX 模板

| 模板 | 适用场景 | 位置 |
|------|----------|------|
| **AkexStar**（默认） | 纯数学/理论作业 | `templates/LaTeX-Homework-Template/` |
| **Jacky-Lzx** | 涉及代码的作业 | `templates/template.LaTeX.homework/` |

> **默认使用 AkexStar 模板**。如果作业包含代码，询问用户是否切换到 Jacky-Lzx 模板。

### Step 5: 生成双格式作业

**同时生成两种格式**：

#### 5.1 Obsidian Markdown 格式

输出路径：`/My Drive/homework/<课程名>/hw<N>.md`

**Callout 类型**：
- `> [!exr]` — 作业题
- `> [!thm]` — 定理
- `> [!definition]` — 定义
- `> [!example]` — 被引用的教材内容
- `> [!note]` — 说明
- `> [!hint]` — 提示
- `\begin proof}` ... `\end proof}` — 解答

**格式规则**：
- `> [!exr]` 里面只有习题题目
- 被引用的背景内容在外部 callout 补充
- Proof 环境在 callout 外部

```markdown
> [!exr] Problem 5.1
> **Section 5.1** — *Covariate Balance*
>
> 证明在 CRE 下，协变量平衡...

> [!example] Referenced Equation: (5.2)
> 在 CRE 下，
> $$
> \mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0.
> $$
> 摘自 \cite[Section 5.2]{Ding2024}。

`\begin proof}`
证明内容...
`\end proof}`
```

#### 5.2 AkexStar 模板（默认）

```latex
\documentclass{homework}
\usepackage[UTF8]{ctex}
\usepackage{amsmath, amsthm, amssymb, bm, color, framed, graphicx, mathrsfs}

\author{姓名}
\class{课程名}
\date{\today}
\title{Homework-1}

\begin{document} \maketitile

\begin{shaded}
\question 题目内容...
\end{shaded}

% 答案直接写在 shaded 环境外部

\img<fig:1>[0.4]{Caption}{image.png}
\tbl<tbl:1>{Caption}{
  Header 1 & Header 2 \\
  Row 1 & Row 2
}
```

#### 5.3 Jacky-Lzx 模板（涉及代码时使用）

```latex
\documentclass[11pt]{article}
\input{structure.tex}
\input{code-style.tex}

\newcommand{\assignmentQuestionName}{Question}
\newcommand{\assignmentClass}{课程名}
\newcommand{\assignmentTitle}{Homework 1}
\newcommand{\assignmentAuthorName}{姓名}

\begin{document}
\maketitle

\begin{question}[20\%]{题目标题}
题目内容...

\begin{answer}
解答内容...
\end{answer}
\end{question}

% 代码示例
\begin{lstlisting}[language=Python, caption={...}, label=lst:1]
# code here
\end{lstlisting}
```

### Step 6: 引用处理（核心规范）

> **⚠️ 极其重要**：
> - 如果引用教材中的**公式/定理/图片**，必须把**完整内容**写到 homework 中
> - **禁止只写 `\cref{xxx}` / `\eqref{xxx}`**，因为 homework 是独立文件
> - 引用教材内容时，必须加 `\cite{bookkey}`

| 类型 | 处理方式 |
|------|----------|
| 公式引用 `(X.Y)` | 找到公式，完整写出内容 + `\cite{bookkey}` |
| 定理引用 `Theorem X.Y` | 找到定理，完整写出内容 + `\cite{bookkey}` |
| 图片引用 `Figure X.Y` | 找到图片，复制或描述 + `\cite{bookkey}` |
| 章节引用 `Section X.Y` | 如果太大，在附录简要说明 + `\cite{bookkey}` |

### Step 7: Double Check

> **⚠️ 必须核对**：生成的作业是否与老师布置的一致
> - 逐题核对题号、内容、要求
> - 如果发现不一致，标注或修正

---

## 输出路径

### Obsidian
```
/My Drive/homework/<课程名>/hw<N>.md
```

### LaTeX
```
/homework/<学科>/homework-<N>.tex
```

### 本地备份
```
notes/<主题>/homework/hw<N>.md
```

---

## Unicode 禁止规则

> **⚠️ 绝对禁止 Unicode 下标**

| 禁止 ❌ | 正确 ✅ |
|---------|---------|
| `n₁`, `n₀` | `$n_1$`, `$n_0$` |
| `x₁`, `x₂` | `$x_1$`, `$x_2$` |

---

## 注意事项

- 习题内容要完整提取，不能只提取标题
- 两个习题之间的内容都算第一个习题的
- `> [!exr]` 里面只有习题题目，被引用内容在外部 callout 补充
- 变量表格使用 markdown table 格式
- 数学公式使用 `$$...$$` 或 `$...$`
- **引用教材内容必须完整写出 + 加 `\cite{}`**
- **默认使用 AkexStar 模板，含代码时询问是否使用 Jacky-Lzx**
