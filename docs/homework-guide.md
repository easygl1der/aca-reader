# 作业专家指南 (Homework Expert Guide)

**适用对象**: homework-expert, writing-expert, qa-specialist
**最后更新**: 2026-04-08

---

## 一、角色定义

### 核心职责

1. **作业解析**：从 PDF 或教材中提取作业题目
2. **内容关联**：在教材 transcript / tex 中找到对应内容
3. **引用补全**：如果作业引用了教材内容（公式/定理/图片），补充完整内容
4. **双格式生成**：同时生成 Obsidian markdown 和 LaTeX tex 两种格式
5. **解答撰写**：使用 proof / solution 环境撰写解答

### 一体化工作流

```
Part 1: 生成习题
         ↓
Part 2: 做习题（补充背景 → 撰写解答 → QA 检查）
         ↓
Part 3: 双格式输出（Obsidian + LaTeX）
```

---

## 二、双轨输出路径

| 格式 | 存储位置 | 说明 |
|------|----------|------|
| **Obsidian** | Google Drive `/My Drive/homework/<课程名>/hw<N>.md` | Markdown + callout |
| **LaTeX** | iCloud workflow `/homework/<学科>/homework-one.tex` 等 | .tex 格式 |

### 输出文件命名

```
Obsidian: hw1.md, hw2.md, ...
LaTeX:    homework-one.tex, homework-two.tex, ...
```

---

## 三、Obsidian Callout 格式

### Callout 类型

| 类型 | 标签 | 用途 |
|------|------|------|
| 作业题 | `> [!exr]` | 作业题目 |
| 定理 | `> [!thm]` | 定理内容 |
| 定义 | `> [!definition]` | 定义内容 |
| 例题 | `> [!example]` | 被引用的教材内容 |
| 说明 | `> [!note]` | 信息说明 |
| 背景 | `> [!info]` | 说明信息 |
| 解答 | `\begin proof}` ... `\end proof}` | 解答（LaTeX 语法） |
| 提示 | `> [!hint]` | 提示 |
| 评论 | `> [!remark]` | 评论 |

### Proof 环境（Obsidian Markdown 中使用 LaTeX 语法）

````markdown
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
````

### Obsidian 格式规则

1. **`> [!exr]` 里面只有习题题目**，不包含被引用内容
2. **被引用的内容在外部**用 `> [!example]` / `> [!thm]` 等 callout 补充
3. **每个题目单独一个 callout block**
4. **Proof 环境在 callout 外部**使用 `\begin proof}` 和 `\end proof}`

---

## 四、LaTeX 模板选择

### 双模板支持

| 模板 | 名称 | 适用场景 | 文档类 |
|------|------|----------|--------|
| **AkexStar** | 默认 | 纯数学/理论作业 | `homework.cls` (基于 amsart) |
| **Jacky-Lzx** | Cleese | 涉及代码的作业 | `article` |

> **默认使用 AkexStar 模板**。如果作业包含代码，询问用户是否切换到 Jacky-Lzx 模板。

### 模板文件位置

```
AkexStar: /tmp/LaTeX-Homework-Template/
Jacky-Lzx: /tmp/template.LaTeX.homework/
```

---

## 五、AkexStar 模板（默认）

### 文档类

```latex
\documentclass{homework}
\usepackage[UTF8]{ctex}  % 中文支持
```

### 核心命令

| 命令 | 用途 |
|------|------|
| `\question` | 题目环境 |
| `\begin{shaded}...\end{shaded}` | 题目背景框 |
| `\img<label>[width]{caption}{files}` | 图片 |
| `\tbl<label>{caption}{content}` | 表格 |
| `\cite{...}` | 文献引用 |

### Question 环境

```latex
\begin{shaded}
\question % 自动编号
题目内容...
\end{shaded}

答案直接写在 shaded 环境外部。
```

### 图片与表格

```latex
\img<fig:1>[0.4]{Caption text}{image.png}

\tbl<tbl:1>{Table Caption}{
  Header 1 & Header 2 \\
  Row 1 Col 1 & Row 1 Col 2
}
```

### 代码环境

```latex
\lstinputlisting[language=Python, caption={...}, label=lst:1]{code/prog.py}
```

---

### 预定义环境

**定理类**（编号共享，按章节）：
```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem*{theorem*}{Theorem}    % 无编号版本

\newtheorem{exercise}[theorem]{Exercise}
\newtheorem{problem}[theorem]{Problem}
```

**定义类**：
```latex
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
```

**评论类**：
```latex
\newtheorem*{remark}{Remark}
\newtheorem*{note}{Note}
\newtheorem*{observation}{Observation}
```

**解答环境**：
```latex
\newtheorem*{solution}{Solution}
\newtheorem*{proof*}{Proof}
```

### Exercise 格式（LaTeX）

```latex
\begin{exercise}{5-1}\label{exr:5-1}
\textbf{Section 5.1} — \emph{Covariate Balance} \cite[Section 5.1]{Ding2024}

证明在 CRE 下，协变量平衡...

\begin{proof}
证明内容...
\end{proof}
\end{exercise}
```

### 格式规则

- **Exercise 标签**：`exr:{章号}-{题号}`，如 `exr:5-1`
- **引用标注**：每个 exercise 标题后加 `\cite[来源]{bookkey}`
- **解答**：使用 `\begin proof}` 或 `\begin solution}` 环境
- **Theorem/Definition 等**：如果补充背景知识，使用对应环境

---

## 五、引用处理（核心规范）

### 核心规则

> **⚠️ 极其重要**：
> - 如果引用教材中的**公式/定理/图片**，必须把**完整内容**写到 homework 中
> - **禁止只写 `\cref{xxx}` / `\eqref{xxx}`**，因为 homework 是独立文件
> - 引用教材内容时，必须加 `\cite{bookkey}` 说明来源

### 引用类型与处理

| 类型 | 示例 | 处理方式 |
|------|------|----------|
| **公式引用** | `(5.2)`、`式 (5.2)` | 找到公式，**完整写出**公式内容 + `\cite{bookkey}` |
| **定理引用** | `Theorem 4.1` | 找到定理，**完整写出**定理内容 + `\cite{bookkey}` |
| **引理引用** | `Lemma 3.2` | 找到引理，**完整写出**引理内容 + `\cite{bookkey}` |
| **图片引用** | `Figure 3-1` | 找到图片，**复制图片或描述** + `\cite{bookkey}` |
| **章节引用** | `Section 5.2` | 如果内容太大，在附录简要说明 + `\cite{bookkey}` |
| **例题引用** | `Example 4.1.3` | 找到例题，**完整写出**例题内容 + `\cite{bookkey}` |

### 处理示例

**处理前（教材原文）**：
```
Prove that (5.2) holds under CRE.
```

**处理后（写入 homework）**：
````latex
\begin{exercise}{5-1}\label{exr:5-1}
\textbf{Section 5.1} — \emph{Covariate Balance} \cite[Section 5.1]{Ding2024}

证明在 CRE 下，协变量平衡。

\begin{equation}
\label{eq:5-2-balance}
\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0.
\end{equation}
\ SOURCE: \cite[Section 5.2, Equation (5.2)]{Ding2024}

\begin{proof}
证明内容...
\end{proof}
\end{exercise}
````

### 附录处理

如果引用的章节内容太大，可以放在附录：

```latex
\section*{附录：教材引用}\label{sec:appendix}

\subsection*{Example 4.1.3 的完整内容}
\noindent\textbf{Example 4.1.3}\ \cite[Example 4.1.3]{bookkey}

% 完整内容...
```

---

## 六、作业来源与处理

### 两种来源

| 来源 | 说明 | 处理方式 |
|------|------|----------|
| **教材习题** | 老师在教材上勾的习题 | 从教材 transcript/tex 提取 |
| **PDF 作业** | 老师发的 PDF 文件 | 用 mineru 或 pymupdf 扫描提取 |

### 来源 1: 教材习题

```
Step 1: 确定教材范围（老师勾了哪些章节）
Step 2: 从教材 transcript/tex 中找到对应习题
Step 3: 按格式规范写入 homework
```

### 来源 2: PDF 作业

```
Step 1: 用 mineru 或 pymupdf 扫描 PDF
Step 2: 提取作业文本
Step 3: 如果有题号，从教材找到对应习题
Step 4: 按格式规范写入 homework
```

### Double Check

> **⚠️ 必须核对**：生成的作业是否与老师布置的一致
> - 逐题核对题号、内容、要求
> - 如果发现不一致，标注或修正

---

## 七、Exercise 编号规范

### 标签命名

| 格式 | 示例 |
|------|------|
| `exr:{章}-{题号}` | `exr:5-1`, `exr:3-7` |

### Exercise 标题格式

```
\begin{exercise}{5-1}\label{exr:5-1}
\textbf{Section X.Y} — \emph{Title} \cite[来源]{bookkey}

题目内容...

\begin{proof}
解答...
\end{proof}
\end{exercise}
```

### 题号来源

- 优先使用**老师布置的原始题号**
- 如果老师只给章节范围，按教材原书题号
- 保持与 exercise-guide.md 一致的命名规范

---

## 八、环境支持

### QA Specialist 支持

- 习题解答中的疑问 → 记录到 `appendix/qa.tex`
- 使用 `\footnote{问：...？答：...。}` 格式
- 引用时 `\footnote{详见附录 \cref{sec:qa-xxx}。}`

### Footnote 格式

```latex
% 正文
这是正文内容\normalfont\index{条目}。

% QA 脚注
% 标注见 \cref{sec:qa-xxx}\footnote{问：...？答：...。详见 \cite[Section X.Y]{bookkey}。}
```

### Reference 与 Bibtex

- 所有引用教材内容必须加 `\cite{bookkey}`
- 在 homework 的 `.bib` 文件中添加对应条目
- 格式：`@book{bookkey, author={...}, title={...}, year={...}}`

---

## 九、Unicode 禁止规则

> **⚠️ 绝对禁止 Unicode 下标**

| 禁止 ❌ | 正确 ✅ |
|---------|---------|
| `n₁`, `n₀` | `$n_1$`, `$n_0$` |
| `x₁`, `x₂` | `$x_1$`, `$x_2$` |
| `₁`, `₀` | `$1$`, `$0$` |

---

## 十、工作流程

```
Step 1: 确定作业来源
         ↓
Step 2: 生成习题（双格式）
         ├─ Obsidian: homework/<课程>/hw<N>.md
         └─ LaTeX:    homework/<学科>/homework-<N>.tex

Step 3: 补充背景（如需要）
         ├─ 引用教材公式/定理 → 完整写出内容
         └─ 补充定义/引理 → 使用对应环境

Step 4: 撰写解答
         ├─ proof 环境（证明题）
         └─ solution 环境（计算/分析题）

Step 5: QA 检查
         ├─ double check 与老师布置一致
         └─ 记录疑问到 qa.tex

Step 6: 质量检查
         └─ 逐项检查清单
```

---

## 十一、质量检查清单

### 核心检查（不合格 = 禁止提交）

| 检查项 | 标准 |
|--------|------|
| **引用内容完整** | 所有 `(X.Y)`、`Theorem X.Y`、`Figure X.Y` 等已有完整内容 + `\cite{}` |
| **无空引用** | 不使用无内容的 `\cref{xxx}` / `\eqref{xxx}` |
| **Exercise 编号规范** | 标签 `exr:{章}-{题号}`，标题含 `\cite{来源}` |
| **解答环境正确** | 证明题用 `proof`，计算题用 `solution` |

### 格式检查

| 检查项 | 标准 |
|--------|------|
| Unicode 下标 | 使用 `$x_1$` 而非 `x₁` |
| Bibtex 引用 | 所有教材引用有对应 `\cite{}` |
| Footnote 格式 | 正确使用 `\footnote{...}` |

### 编译检查

```bash
# LaTeX 编译检查
./compile.sh 2>&1 | grep -i "error\|warning"

# 检查未解析引用
grep -n "??\|undefined reference" notes/*/homework/*.tex
```

---

## 十二、相关文件

| 文件 | 用途 |
|------|------|
| `docs/exercise-guide.md` | 习题格式指南 |
| `PDFs/<主题>/transcript/` | 教材转录本 |
| `PDFs/<主题>/**/*.tex` | 教材 tex 文件 |
| `PDFs/2025-summer/westlake-university/homework/includes/` | LaTeX 模板参考 |
| `notes/<主题>/homework/` | 本地 homework 备份 |
