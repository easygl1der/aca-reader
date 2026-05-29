# 阶段 4：AI 初稿 V1

## 目的

基于大纲，生成完整的章节初稿（~100% 填充度），遵循 Stein 动机优先风格。

## 输入

- `chapter-outline.tex`（阶段 3 输出）
- `close-reading-notes.md`（精读笔记）
- 目标主题目录

## 输出

`drafts/v1_chapter{N}.tex` — 完整章节草稿

## 执行步骤

### Step 1：读取大纲和精读笔记

```bash
# 读取大纲
cat chapter-outline.tex

# 读取精读笔记
cat close-reading-notes.md
```

### Step 2：扩充引言

遵循 Stein 风格：

**结构**：
1. **开场句**（吸引读者）：引用/问题/物理现象
2. **动机段落**：为什么需要这个章节
3. **历史脉络**（可选）：重要人物和贡献
4. **与前章联系**：如何从前几章自然过渡
5. **本章结构**（最后）：概览各节内容

**示例框架**：
```latex
\section{引言}\label{sec:5-intro}

在第三章中，我们学习了潜在结果框架的基本概念...
然而，这一框架在实践中面临一个根本性困难：无法同时观测每个单元的
两种潜在结果...
\stepcounter{footnote}\addtocounter{footnote}{-1}\footnotesize%
\par\_notes{关于潜在结果的详细讨论见 \cref{sec:3-1}。}

\section{第一节标题}\label{sec:5-1}
```

### Step 3：扩充定义

**每个定义的写作模式**：
```latex
\begin{Definition}[5.1]\label{def:5-1}
\textbf{协变量平衡}（Covariate Balance）指的是...
\end{Definition}

% 定义后的动机说明
直观上，协变量平衡意味着处理组和对照组在协变量上的分布相似，
从而使得我们可以将组间差异归因于处理效应而非混淆因素。
```

**动机引入**（定义前）：
```latex
在正式定义协变量平衡之前，我们先考虑一个简单例子...

\begin{Example}[二元处理的协变量平衡]\label{ex:5-1}
设处理变量 $Z \in \{0, 1\}$，协变量 $X \in \mathbb{R}^p$...
\end{Example}

这个例子说明了：如果协变量不平衡，处理组和对照组的潜在结果分布可能
系统性地不同，从而导致因果推断的偏差。

这引导我们提出一个精确的数学定义...

\begin{Definition}[5.1]\label{def:5-1}
我们称处理组和对照组满足\textbf{协变量平衡}，如果...
\end{Definition}
```

### Step 4：扩充定理

**定理写作结构**：
```latex
\begin{Theorem}[5.1 — 协变量平衡与因果识别]\label/thm:5-1}
假设以下条件成立：
\begin{enumerate}
\item \textbf{强可忽略性}（Strong Ignorability）：
$(Y(1), Y(0)) \Perp Z \mid X$；
\item \textbf{重叠性}（Overlap）：对所有 $x$，$0 < \mathbb{P}(Z=1 \mid X=x) < 1$。
\end{enumerate}
则有
\begin{equation}\label{eq:5-1}
\mathbb{E}[Y(1) - Y(0)] = \mathbb{E}_X\big[\mathbb{E}(Y \mid Z=1, X) - \mathbb{E}(Y \mid Z=0, X)\big]。
\end{equation}
\end{Theorem}
```

**证明写作**：
```latex
\begin{Proof}
证明的关键思想是将期望按协变量条件化，然后利用强可忽略性交换潜在结果
和处理分配的顺序...

首先，根据全概率公式，
\[
\mathbb{E}[Y(1)] = \mathbb{E}_X\big[\mathbb{E}(Y(1) \mid X)\big]。
\tag*{\stepcounter{footnote}}
\]
由于 $\mathbb{E}(Y(1) \mid X) = \mathbb{E}(Y \mid Z=1, X)$，我们有...
\done
\par\Notes{完整证明见附录 \cref{sec:appendix-5-1}。}
\end{Proof}
```

### Step 5：扩充示例

**示例写作结构**：
```latex
\begin{Example}[协变量平衡的数值例子]\label{ex:5-2}
考虑一个简单的研究：评估某药物对血压的效应。
\begin{enumerate}
\item \textbf{数据设定}：$n=100$ 名受试者，随机分配处理或对照...
\item \textbf{计算过程}：
首先，计算每层的协变量平衡...
然后，应用公式 \eqref{eq:5-1}...
\end{enumerate}
表 \ref{tab:5-1} 展示了主要结果。
\end{Example}

\par\Notes{完整计算过程见附录 \cref{sec:appendix-5-2}。}
```

### Step 6：添加小结

```latex
\section{小结}\label{sec:5-summary}

本章引入了协变量平衡的核心概念...
主要结果可概括为以下几个要点：

\begin{enumerate}
\item 协变量平衡是因果推断的基础性条件...
\item 定理 \ref/thm:5-1} 表明，在强可忽略性和重叠性下...
\item 实践中，协变量平衡可以通过...
\end{enumerate}

在下一章中，我们将学习如何通过...来评估和实现协变量平衡。
```

### Step 7：LaTeX 格式检查

完成后，使用以下 skill 验证：

| Skill | 检查内容 |
|-------|----------|
| `latex-writing-check` | 无 Markdown 格式 |
| `latex-label-ref-verifier` | label/ref 一致性 |
| `latex-debug` | 编译错误修复 |
| `note-content-verifier` | 内容与原文一致 |

```bash
# 运行格式检查
Skill latex-writing-check

# 运行引用检查
Skill latex-label-ref-verifier
```

### Step 8：保存到 drafts 目录

```bash
mkdir -p notes/<topic>/drafts
cp chapter{N}.tex notes/<topic>/drafts/v1_chapter{N}.tex
```

## 写作风格要点

### Stein 动机句式

| 场景 | Stein 句式 |
|------|-----------|
| 引入问题 | "The problem consists of..." |
| 引出概念 | "This leads us to..." |
| 关键观察 | "The key observation is..." |
| 自然问题 | "A natural question arises..." |
| 条件解释 | "A moment's reflection suggests..." |

### 符号规范（必须遵守）

| 概念 | ✅ 正确 | ❌ 错误 |
|------|---------|---------|
| 期望（单变量） | `\mathbb{E}X` | `\mathbb{E}[X]` |
| 期望（多变量） | `\mathbb{E}(XY)` | `\mathbb{E}X \cdot \mathbb{E}Y` |
| 方差 | `\text{var}(X)` | `\text{Var}(X)` |
| 协方差 | `\text{cov}(X,Y)` | `\text{Cov}(X,Y)` |
| 向量 | `\mathbf{x}` | `\bm{x}` |
| 矩阵 | `\boldsymbol{X}` | `\bm{X}` |
| 示性函数 | `\mathbb{I}(X \in A)` | `1_{X \in A}` |

### 禁止事项

- ❌ Markdown 格式（加粗、列表、代码块）
- ❌ `\bm` 命令
- ❌ 硬编码数字引用（使用 `\cref{}`）
- ❌ 在 Theorem 环境内使用 itemize（用 enumerate）
- ❌ Unicode 下标（如 $n_1$，用 $n_1$）

## 输出文件结构

```
drafts/
├── v1_chapter5.tex          # 完整初稿
├── latex-check-report.md    # 格式检查报告
└── label-ref-report.md      # 引用检查报告
```

## 验证清单

- [ ] 引言完整且动机明确
- [ ] 所有定义有动机说明
- [ ] 所有定理有完整条件和结论
- [ ] 证明有核心思路，完整证明在附录
- [ ] 示例有动机说明和完整计算
- [ ] 小结涵盖主要结果
- [ ] 符号使用正确
- [ ] 无 Markdown 格式
- [ ] label/ref 一致
- [ ] 可成功编译

## 下一步

传递给 **阶段 5：人工审阅**
