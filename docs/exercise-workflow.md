# 教材习题笔记补充工作流

## 支持的教材模板

| 模板 | 教材示例 | 习题环境 | 标题格式 | 内容语言 |
|------|----------|----------|----------|----------|
| **do Carmo** | 微分几何 | `exercise` | `{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}` | 英文原文 |
| **Peng Ding** | 因果推断 | `Exercise` | `{\ref{标签} 英文标题}` | 中文描述 + `\eqref{}` 引用 |
| **通用** | 其他教材 | `Exercise` | `{\ref{标签} 英文标题}` | 中文或英文 |

---

## 工作流

### Step 1: 检测教材类型

根据笔记目录检测教材模板：

```
notes/differential-geometry/do-carmo-curves-surfaces/  → do Carmo 模板
notes/A-First-Course-in-Causal-Inference/            → Peng Ding 模板
notes/<其他>/                                       → 通用模板
```

### Step 2: 查找习题来源（优先级）

1. **tag 文件**：优先检查是否有 `.tex` 源文件（包含 `\label{}` 和 `\ref{}`）
   - 优点：公式标签清晰，引用关系自动保留
   - 位置：`PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex`

2. **transcript 文件**：如果没有 tag 文件，使用 minerU 转录的 markdown
   - 位置：`PDFs/<教材>/transcript/<书名>.md`
   - 缺点：没有 label/ref，需要手动添加

### Step 3: 提取习题内容

从教材 transcript 中识别习题章节：
- 标题模式：`# X.Y Homework Problems`、`## Homework Problems`、`# Exercises`
- 内容模式：`\paragraph{标题}` 或 题号列表

### Step 4: 格式化习题

根据教材类型应用对应格式。

---

## do Carmo 模板格式

### 习题环境
```latex
\subsection*{2-2 节练习}

\begin{exercise}{2-2, 1 — do Carmo, Exercise 2-2, 1}
Show that the cylinder $\{(x,y,z)\in \mathbb{R}^3;x^2 +y^2 = 1\}$ is a regular surface...
\end{exercise}
```

### 格式规范
- **环境**：`exercise`（小写）
- **标题参数**：`{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}`
- **内容语言**：英文原文（直接引用教材）
- **难题标记**：题号后加 `*`，如 `{2-2, 5* — do Carmo, Exercise 2-2, 5}`
- **多问格式**：使用 `enumerate` 环境

### 正确示例
```latex
\begin{exercise}{2-2, 7 — do Carmo, Exercise 2-2, 7}
Let $f(x, y, z) = (x + y + z - 1)^2$.
\begin{enumerate}
  \item[a.] Locate the critical points and critical values of $f$.
  \item[b.] For what values of $c$ is the set $f(x, y, z) = c$ a regular surface?
\end{enumerate}
\end{exercise}
```

---

## Peng Ding 模板格式

### 习题环境
```latex
\section{习题}\label{sec:chapter5-exercises}

\begin{Exercise}{\ref{exr:5-1} Covariate balance in the CRE}\label{exr:5-1}
证明 \eqref{eq:balance-discrete-CRE}：在 CRE 下，
\[
\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0.
\]
\end{Exercise}
```

### 格式规范
- **环境**：`Exercise`（大写）
- **标题参数**：`{\ref{标签} 英文标题}`
- **标签命名**：`exr:{章号}-{题号}`
- **公式引用**：必须用 `\eqref{eq:标签}` 引用教材公式
- **内容语言**：
  - 理论题：优先中文描述
  - 计算题：可中文
  - 专有名词：保留英文

### 正确示例
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

### 标签命名参考

| 习题 | 标签 |
|------|------|
| 5.1 | `exr:5-1` |
| 5.2 | `exr:5-2` |
| 3.7 | `exr:3-7` |

---

## 公式标签发现流程

### 从 tag 文件中发现

1. 读取 `PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex`
2. 搜索 `\label{eq:...}` 获取所有公式标签
3. 搜索 `\ref{hw::...}` 获取习题引用的公式
4. 建立映射关系

### 从 transcript 发现

1. 读取 `PDFs/<教材>/transcript/<书名>.md`
2. 查找 "Problem X.Y" 或 "Exercise X.Y" 模式
3. 提取公式，手动分配标签

### 常见公式标签模式

| 教材 | 标签模式 | 示例 |
|------|----------|------|
| Peng Ding | `eq::{描述}` | `eq::balance-discrete-CRE` |
| do Carmo | 无标签（不引用） | — |

---

## 用户指令

用户可以使用以下指令：

| 指令 | 说明 |
|------|------|
| `生成第 X 章习题` | 提取并格式化第 X 章习题 |
| `用英文输出习题` | 内容使用英文原文 |
| `检查标签引用` | 验证所有 `\eqref{}` 是否正确 |

---

## 质量检查清单

- [ ] 习题编号与教材一致
- [ ] 公式引用 `\eqref{}` 指向正确标签
- [ ] 标签命名 `exr:{章号}-{题号}` 规范
- [ ] 中文专有名词保留英文
- [ ] 编译无错误
