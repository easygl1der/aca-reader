# LaTeX 格式规范

## 禁止使用
- ❌ Markdown 列表（`-`、`1.`）
- ❌ Markdown 加粗（`**text**`）
- ❌ Markdown 斜体（`*text*`）
- ❌ Markdown 代码块（```）
- ❌ `\bm` 命令：向量用 `\mathbf`，矩阵用 `\boldsymbol`

## 中文标点
- **引号**：使用 ``` `` '' ```（反引号 + 单引号），而非中文弯引号
  - 示例：`` ``因果推断'' ``` 渲染为 **"因果推断"**

## 必须使用
- ✅ `\begin{enumerate}...\end{enumerate}` 或 `\begin{itemize}...\end{itemize}`
- ✅ `\textbf{text}`
- ✅ `\textit{text}`
- ✅ `\begin{verbatim}...\end{verbatim}` 或 `\texttt{text}`

## Theorem 环境
- **禁止在 Definition/Theorem 环境中使用 itemize**，使用 enumerate 替代
- 条件之间用分号分隔

## 脚注
- 使用 `\footnote{}` 添加说明

## Theorem Style
```latex
\theoremstyle{definition}
\newtheorem{Definition}{定义}[chapter]
\newtheorem{Theorem}[Definition]{定理}
\newtheorem{Lemma}[Definition]{引理}
\newtheorem{Corollary}[Definition]{推论}
\newtheorem{Proposition}[Definition]{命题}
\newtheorem{Example}{例}[chapter]
\newtheorem{Remark}{注}[chapter]
```

## Example 环境使用规范（动机优先原则）

**核心思想**：例子是理解的润滑剂——在引入新概念前先用例子说明"为什么需要它"，在定理后展示"如何使用它"。

### 使用原则

| 类型 | 位置 | 目的 |
|------|------|------|
| **动机型** | 概念定义**之前** | 展示为什么需要这个概念 |
| **应用型** | 概念定义**之后** | 展示如何使用这个概念 |
| **演示型** | 定理**之后** | 展示理论的实际应用 |

### Stein 风格引入模式

参考 `docs/stein-writing-style.md`：

**模式一：从物理/实际问题出发**
1. 描述可观察的物理现象或实际问题
2. 建立数学模型
3. 引出核心数学问题
4. 形式化定义

**模式二：从已学内容自然推广**
1. 回顾已学概念
2. 指出直接推广会遇到的困难
3. 引入新的条件/定义来解决困难
4. 解释为什么这个条件是"自然"的

**模式三：分类渐进**
1. 先给出一个"一般原理"
2. 按从简单到复杂的顺序排列
3. 逐一解释每个类别

### Example 环境格式

```latex
\begin{Example}[称重例子]
  令 $y = (y_1, \ldots, y_n)$ 为物体在秤上称量 $n$ 次的记录重量，
  $\theta = (\mu, \sigma^2)$ 为物体的真实重量和测量方差。
  ...
\end{Example}
```

### 与正文/附录的关系

- **正文**：保持流畅叙述，例子作为"润滑剂"，用例子自然引出概念
- **详细推导**：放附录，用 `\footnote{推导见附录 \cref{sec:xxx}}` 引用
- **★ Insight**：必要时在例子后加"★ Insight"总结要点

## Proof 环境（无编号但支持可选标题）
```latex
\newtheorem*{Proof}{证明}

\begin{Proof}[Neyman 1923 定理]
证明内容...
\end{Proof}
```
- 使用 `*` 的 `\newtheorem*` 创建无编号环境
- 支持 `[]` 可选参数作为证明标题

## 习题环境
```latex
\newtheorem{Exercise}{练习}[chapter]

\begin{Exercise}{题目描述}
题目内容...
\end{Exercise}
```

## 数学符号习惯

### 概率、期望、方差、协方差

用户的个人习惯（优先级最高）：

| 概念 | 符号 | 说明 |
|------|------|------|
| 概率 | `\mathbb{P}(A)` | 黑板粗体 P |
| 期望 | `\mathbb{E}(X)` | 黑板粗体 E |
| 单变量期望 | `\mathbb{E}X` | 无括号 |
| 多变量期望 | `\mathbb{E}(XY)` | 有括号 |
| 方差 | `\text{var}` | 正体 var |
| 协方差 | `\text{cov}` | 正体 cov |
| 相关系数 | `\text{corr}` | 正体 corr |
| 独立性 | `$A \Perp B$` | 竖线符号 |
| 示性函数 | `\mathbb{I}` | 黑板粗体 I |
| p 值 | `\text{p}_{}` | 下标为空 |

**示例：**
```latex
% 概率
\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B \mid A)

% 期望（单个变量，无括号）
\mathbb{E}X = \sum_{x} x \cdot p_X(x)

% 期望（多个变量，有括号）
\mathbb{E}(XY) = \sum_{x}\sum_{y} xy \cdot p_{XY}(x,y)

% 方差
\text{var}(X) = \mathbb{E}[(X - \mathbb{E}X)^2]

% 协方差
\text{cov}(X, Y) = \mathbb{E}(XY) - \mathbb{E}X \cdot \mathbb{E}Y

% 相关系数
\text{corr}(X, Y) = \frac{\text{cov}(X, Y)}{\sqrt{\text{var}(X) \cdot \text{var}(Y)}}

% 独立性
A \Perp B \quad \text{当且仅当} \quad \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)

% 示性函数（三种写法均可）
\mathbb{I}_A(x) = \begin{cases} 1 & \text{if } x \in A \\ 0 & \text{if } x \notin A \end{cases}
\mathbb{I}(X \in [a,b]) = \mathbb{I}_{[a,b]}(X)
\mathbb{I}(a \leq X < b)

% p 值（使用 \text{p}_{}，下标为空）
\text{p}_{} = 0.03
```

## 文档模板

### 使用 amsbook
```latex
\documentclass[12pt]{amsbook}
\usepackage{xeCJK}
```

### xeCJK 字体配置
**先查看电脑上可用的字体：**
```bash
fc-list :lang zh
fc-list | grep -i "serif" | head -20
```

**常用配置：**
```latex
\setCJKmainfont{Noto Serif SC}
\setCJKsansfont{Noto Sans SC}
```
