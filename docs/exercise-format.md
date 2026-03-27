# 习题格式规范

## 概述

不同笔记模板使用不同的习题格式：

| 模板 | 习题格式 | 说明 |
|------|----------|------|
| **book 模板** (do Carmo) | `exercise` 环境，`{章节编号, 题号 — do Carmo, ...}` | 见本规范 §1 |
| **因果推断模板** (Peng Ding) | `Exercise` 环境，`{\ref{标签} 英文标题}` | 见本规范 §2 |
| **其他模板** | 各自格式 | 详见对应笔记规范 |

---

## §1 Book 模板 (do Carmo)

本节定义 **book 模板**（do Carmo 微分几何笔记）中的习题引用格式。

### 格式模板

```latex
\begin{exercise}{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}
习题内容原文（英文）。
\end{exercise}
```

---

## 格式说明

### 1. 环境名称
使用 `exercise` 环境（已定义在文档宏中）。

### 2. 参数格式
```
{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}
```

**示例**：
- 教材第1-2节，第1题：`{1-2, 1 — do Carmo, Exercise 1-2, 1}`
- 教材第1-3节，第5题：`{1-3, 5 — do Carmo, Exercise 1-3, 5}`

### 3. 题目标注
- 难题用 `*` 标记：如 `{1-3, 8* — do Carmo, Exercise 1-3, 8}`
- 题目标题放在花括号内，格式为：`{... — do Carmo, Exercise ...}`

### 4. 公式格式
- **短公式**：用行内公式 `$...$`，如 `$\alpha(t) = (a\cos t, a\sin t, bt)$`
- **长公式**：用行间公式 `\[ ... \]`，如
  ```latex
  \[
  \alpha(t) = \left(\frac{3at}{1+t^3}, \frac{3at^2}{1+t^3}\right).
  \]
  ```
- **判断标准**：公式超过一行、或包含复杂分式/根号，应使用行间公式

### 5. 中文注解
- **英文原文**：直接引用 do Carmo 教材原文，不翻译
- **中文补充**：在 `\end{exercise}` 之后可加中文注解（可选）
- **图片引用**：使用 `\cref{fig:标签}` 引用图片，如 `见 \cref{fig:cycloid}，教材 Figure 1-7`

---

## 正确示例

```latex
\begin{exercise}{1-2, 1 — do Carmo, Exercise 1-2, 1}
Find a parametrized curve $\alpha(t)$ whose trace is the circle
$x^2 + y^2 = 1$ such that $\alpha(t)$ runs clockwise around
the circle with $\alpha(0) = (0, 1)$.
\end{exercise}
```

```latex
\begin{exercise}{1-3, 2 — do Carmo, Exercise 1-3, 2}
A circular disk of radius 1 in the plane $xy$ rolls without slipping
along the $x$ axis. The figure described by a point of the circumference
of the disk is called a cycloid (见 \cref{fig:cycloid}，教材 Figure 1-7)。
\begin{enumerate}
\item[a.] Obtain a parametrized curve $\alpha: \mathbb{R} \to \mathbb{R}^2$
the trace of which is the cycloid, and determine its singular points.
\item[b.] Compute the arc length of the cycloid corresponding to
a complete rotation of the disk.
\end{enumerate}
\end{exercise}
```

```latex
\begin{exercise}{1-4, 2* — do Carmo, Exercise 1-4, 2}
A plane $P$ contained in $\mathbb{R}^3$ is given by the equation
$ax + by + cz + d = 0$. Show that the vector $v = (a, b, c)$ is
perpendicular to the plane and that $|d| / \sqrt{a^2 + b^2 + c^2}$
measures the distance from the plane to the origin $(0, 0, 0)$.
\end{exercise}
```

---

## 错误示例

❌ **错误：中文标题**
```latex
\begin{exercise}{1-2, 1 — do Carmo, 习题1-2, 1}  % 不要用中文
```

❌ **错误：缺少 do Carmo 引用**
```latex
\begin{exercise}{1-2, 1}  % 缺少来源
```

❌ **错误：footnote 格式**
```latex
\begin{exercise}{1-2, 1}\footnote{do Carmo, Exercise 1-2, 1}  % 不要用 footnote
```

---

## 分部题目格式

当题目包含多个小问时，使用 `enumerate` 环境：

```latex
\begin{exercise}{1-3, 3 — do Carmo, Exercise 1-3, 3}
Let $0A = 2a$ be the diameter of a circle $S^1$. Prove that:
\begin{enumerate}
\item[a.] The trace of $\alpha(t) = \left(\frac{2at^2}{1+t^2},
\frac{2at^3}{1+t^2}\right)$, $t \in \mathbb{R}$, is the cissoid
of Diocles (见 \cref{fig:cissoid}，教材 Figure 1-8).
\item[b.] The origin $(0,0)$ is a singular point of the cissoid.
\item[c.] As $t \to \infty$, $\alpha(t)$ approaches the line $x = 2a$ (asymptote).
\end{enumerate}
\end{exercise}
```

---

## 分节练习标记

每个习题 section 结束后，用以下格式标记：

```latex
\subsection*{1-2 节练习}
```

---

## 参考

- 章节编号：对应 do Carmo 教材的节号，如 `1-2` 表示第1章第2节
- 题号：教材中的实际习题编号
- 图片引用：使用 transcript md 文件中的图片标签

---

## §2 因果推断模板 (Peng Ding)

本节定义 **因果推断模板**（Peng Ding - A First Course in Causal Inference 笔记）中的习题格式。

### 格式模板

```latex
\section{习题}\label{sec:chapter5-exercises}

\begin{Exercise}{\ref{exr:5-1} 英文标题}\label{exr:5-1}
习题内容（中英文均可，英文优先）。
\end{Exercise}
```

### 格式说明

1. **环境名称**：使用 `Exercise` 环境（已定义在文档宏中，大写首字母）

2. **参数格式**：
   ```
   {\ref{标签} 英文标题}
   ```
   - `{\ref{exr:5-1} Covariate balance in the CRE}`

3. **标签命名规范**：`exr:{章号}-{题号}`，如 `exr:5-1`、`exr:5-7`

4. **习题标题**：使用教材原文的英文标题，保持学术规范性

5. **\textbf{公式引用规则}**：\textbf{必须用 `\eqref{}` 引用教材公式编号}，格式为 `\eqref{eq:标签}`

6. **内容语言**：
   - 理论题：优先使用英文原文描述
   - 计算/应用题：可使用中文描述题目背景
   - 公式：使用 LaTeX 行内或行间公式

### 正确示例

```latex
\begin{Exercise}{\ref{exr:5-1} Covariate balance in the CRE}\label{exr:5-1}
证明 \eqref{eq:balance-discrete-CRE}：在 CRE 下，
\[
\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0.
\]
\end{Exercise}
```

```latex
\begin{Exercise}{\ref{exr:5-3} Consequence of constant individual causal effects}\label{exr:5-3}
假设个体因果效应是常数 $\tau_i = \tau$（对所有 $i = 1, \ldots, n$）。考虑以下 $\tau$ 的加权估计量类：
\[
\hat\tau_w = \sum_{k=1}^K w_{[k]} \hat\tau_{[k]},
\]
其中权重 $w_{[k]}$ 对所有 $k$ 非负。

\begin{enumerate}
  \item 找出使 $\hat\tau_w$ 对 $\tau$ 无偏的 $w_{[k]}$ 条件。
  \item 在所有无偏估计量中，找出使 $\hat\tau_w$ 方差最小的权重。
\end{enumerate}
\end{Exercise}
```

### 错误示例

❌ **错误：缺少标签引用**
```latex
\begin{Exercise}{5.1 Covariate balance}\label{exr:5-1}  % 缺少 \ref{}
```

❌ **错误：标签格式错误**
```latex
\begin{Exercise}{\ref{ex:5.1} Covariate balance}\label{exr:5-1}  % 标签名不一致
```

❌ **错误：中文标题**
```latex
\begin{Exercise}{\ref{exr:5-1} CRE 中的协变量平衡}\label{exr:5-1}  % 不应用中文标题
```

### 分部题目格式

当题目包含多个小问时，使用 `enumerate` 环境：

```latex
\begin{Exercise}{\ref{exr:5-9} Data re-analyses}\label{exr:5-9}
重新分析第 4 章使用的 LaLonde 数据。

\begin{enumerate}
  \item 将实验视为按种族分层的 SRE，重新分析数据。
  \item 将实验视为按婚姻状况分层的 SRE，重新分析数据。
  \item 将实验视为按高中文凭指标分层的 SRE，重新分析数据。
\end{enumerate}
与 CRE 下的结果进行比较。
\end{Exercise}
```

### 参考

- 标签命名：`exr:{章号}-{题号}`（与 chapter4.tex 保持一致）
- 习题编号：对应教材章内习题编号（如 5.1, 5.2, ..., 5.9）
- 题目来源：Peng Ding 教材章后习题
