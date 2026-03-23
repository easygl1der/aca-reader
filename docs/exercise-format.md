# 习题格式规范

## 概述

本规范定义微分几何笔记（do Carmo Curves and Surfaces）中的习题引用格式。

---

## 格式模板

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

### 4. 习题内容
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
