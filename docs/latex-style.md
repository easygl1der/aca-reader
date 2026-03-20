# LaTeX 格式规范

## 禁止使用
- ❌ Markdown 列表（`-`、`1.`）
- ❌ Markdown 加粗（`**text**`）
- ❌ Markdown 斜体（`*text*`）
- ❌ Markdown 代码块（```）

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
