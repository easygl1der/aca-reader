# 写作指南

本文档是笔记写作的**唯一权威参考**，整合了 LaTeX 格式规范、Stein 写作风格、Example 使用规范等所有写作要求。

---

## 第一部分：LaTeX 格式规范

### 禁止使用
- ❌ Markdown 列表（`-`、`1.`）
- ❌ Markdown 加粗（`**text**`）
- ❌ Markdown 斜体（`*text*`）
- ❌ Markdown 代码块（`````）
- ❌ `\bm` 命令：向量用 `\mathbf`，矩阵用 `\boldsymbol`

### 中文标点
- **引号**：使用 ``` `` '' ```（反引号 + 单引号），而非中文弯引号
  - 示例：`` ``因果推断'' ``` 渲染为 **"因果推断"**

### 必须使用
- ✅ `\begin{enumerate}...\end{enumerate}` 或 `\begin{itemize}...\end{itemize}`
- ✅ `\textbf{text}`
- ✅ `\textit{text}`
- ✅ `\begin{verbatim}...\end{verbatim}` 或 `\texttt{text}`

### Theorem 环境
- **禁止在 Definition/Theorem 环境中使用 itemize**，使用 enumerate 替代
- 条件之间用分号分隔

### 脚注
- 使用 `\footnote{}` 添加说明

### Theorem Style 定义
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

### Proof 环境（无编号但支持可选标题）
```latex
\newtheorem*{Proof}{证明}

\begin{Proof}[Neyman 1923 定理]
证明内容...
\end{Proof}
```
- 使用 `*` 的 `\newtheorem*` 创建无编号环境
- 支持 `[]` 可选参数作为证明标题

### 习题环境
```latex
\newtheorem{Exercise}{练习}[chapter]

\begin{Exercise}{题目描述}
题目内容...
\end{Exercise}
```

---

## 第二部分：数学符号习惯

### 概率、期望、方差、协方差

**用户的个人习惯（优先级最高）：**

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

### 符号一致性检查 ⚠️

**全笔记符号必须统一**。除了上述符号习惯外，还需检查同一概念在不同位置是否使用不同符号：

**必须避免的符号混用：**
| 概念 | ✅ 统一 | ❌ 混用示例 |
|------|---------|------------|
| 概率 | `\mathbb{P}` | `P`, `Pr`, `p` |
| 期望 | `\mathbb{E}` | `E`, `Exp` |
| 方差 | `\text{var}` | `Var`, `var` |
| 协方差 | `\text{cov}` | `Cov`, `cov` |
| 示性函数 | `\mathbb{I}` | `I`, `1_` |
| p 值 | `\text{p}_{}` | `p-value`, `pvalue` |
| 独立性 | `\Perp` | `⊥`, `⟂` |
| 向量 | `\mathbf{x}` | `\bm{x}`, `\vec{x}` |
| 矩阵 | `\boldsymbol{X}` | `\bm{X}` |

**检查方法**：在 `chapters/` 和 `appendix/` 目录下搜索可能的不一致符号：
```bash
# 检查 P( vs \mathbb{P}(
grep -rn "P(" --include="*.tex" notes/<topic>/ | grep -v "mathbb"

# 检查 var( vs \text{var}(
grep -rn "var(" --include="*.tex" notes/<topic>/ | grep -v "text{var"

# 检查 \bm{（禁止）
grep -rn "\\bm{" --include="*.tex" notes/<topic>/
```

**注意**：在 R 代码的 `verbatim` 环境中（如 `\begin{verbatim}...\end{verbatim}`）的符号不受此限制。

---

## 第三部分：Example 环境使用规范（动机优先原则）

**核心思想**：例子是理解的润滑剂——在引入新概念前先用例子说明"为什么需要它"，在定理后展示"如何使用它"。

### 使用原则

| 类型 | 位置 | 目的 |
|------|------|------|
| **动机型** | 概念定义**之前** | 展示为什么需要这个概念 |
| **应用型** | 概念定义**之后** | 展示如何使用这个概念 |
| **演示型** | 定理**之后** | 展示理论的实际应用 |

### Example 环境格式

```latex
\begin{Example}[称重例子]
  令 $y = (y_1, \ldots, y_n)$ 为物体在秤上称量 $n$ 次的记录重量，
  $\theta = (\mu, \sigma^2)$ 为物体的真实重量和测量方差。
  ...
\end{Example}
 footnote{推导见附录 \cref{sec:xxx}。}
```

**重要规范**：
- Example 环境内**不写**"完整推导见附录"等文字
- 在 `\end{Example}` **之后**用 `\footnote{...}` 引用附录推导
- footnote 放在 Example 结束后立即引用，格式统一为：`\footnote{推导见附录 \cref{sec:xxx}。}`

### 与正文/附录的关系

- **Example**：放真正的例子（数值演示、应用场景、历史典故等），**不放推导摘要**
- **详细推导**：放附录，在 Example 结束后用 `\footnote{推导见附录 \cref{sec:xxx}}` 引用
- **★ Insight**：必要时在例子后加"★ Insight"总结要点

---

## 第四部分：Stein 写作风格

> 基于《Fourier Analysis: An Introduction》和《Complex Analysis》的写作和叙述风格分析

### 核心原则

**必须模仿 Stein《傅里叶分析》《复分析》的 motivation 风格**：

- **动机优先**: 每个概念/定理引入前，先解释"为什么需要它"和"它从哪里来"
- **历史脉络**: 注重概念的起源和发展历史
- **有机联系**: 强调不同数学领域之间的相互关联
- **叙事流畅**: 定义→命题→证明之间有连贯的叙述，避免干巴巴的罗列
- **循序渐进**: 从简单到复杂，不过早引入技术细节

### 动机引入的标准化模式

#### 模式一：从物理/实际问题出发

**适用场景**: 引入全新的数学概念

**写作结构**:
1. 描述可观察的物理现象或实际问题
2. 建立数学模型
3. 引出核心数学问题
4. 形式化定义

**示例** (Chapter 1 - 振动弦):
```
The problem consists of the study of the motion of a string fixed at its
end points and allowed to vibrate freely. We have in mind physical systems
such as the strings of a musical instrument.

Understanding the empirical facts behind these phenomena will motivate
our mathematical approach to vibrating strings.
```

#### 模式二：从已学内容自然推广

**适用场景**: 推广已有概念到更一般的情形

**写作结构**:
1. 回顾已学概念
2. 指出直接推广会遇到的困难
3. 引入新的条件/定义来解决困难
4. 解释为什么这个条件是"自然"的

**示例** (Chapter 5 - Fourier 变换):
```
We begin by extending the notion of integration to functions that are
defined on the whole real line.

Of course, this limit may not exist... A moment's reflection suggests
that the limit will exist if we impose on f enough decay as |x| tends
to infinity.
```

#### 模式三：从分类到一般化

**适用场景**: 引入函数类别

**写作结构**:
1. 从最具体的例子开始
2. 逐步放宽条件，引入更一般的类别
3. 给出每个类别的典型例子
4. 最终引入最一般的定义

#### 模式四：名人名言开场

**适用场景**: 每章开篇（复分析常用）

**结构**：
1. 引用数学家的原话/评述（通常 2-4 行）
2. 解释这段话与本章内容的关联
3. 概述本章结构

#### 模式五：跨领域连接

**适用场景**: 引入新主题

**结构**：
1. 说明这个主题与之前学过的内容的联系
2. 解释为什么这个应用是"natural"或"important"
3. 给出应用的具体例子

#### 模式六：分类渐进

**适用场景**: 引入多种相似概念

**结构**：
1. 先给出一个"一般原理"
2. 按某种顺序（从简单到复杂/从温和到严重）排列
3. 逐一解释每个类别

### 常用连接词和句式

#### 动机解释

| 英文表达 | 中文含义 | 使用场景 |
|----------|----------|----------|
| The problem consists of... | 问题在于... | 引入新问题 |
| We begin with... | 我们从...开始 | 开始新话题 |
| This leads us to... | 这引导我们... | 引出下一步 |
| The key observation is... | 关键观察是... | 引出核心思路 |
| A natural question arises... | 一个自然的问题是... | 引出探索方向 |

#### 历史引用

| 英文表达 | 中文含义 |
|----------|----------|
| The sweeping development of... is due to... | ...的发展归功于... |
| ...was the first to... | ...是第一个...的人 |
| This idea was implicit in earlier work | 这个想法在前人的工作中已有隐含 |
| ...initiated by Euler | ...由欧拉开创 |
| ...transformed the subject by... | ...通过...改变了这个领域 |

#### 一般原理陈述

| 英文表达 | 中文含义 |
|----------|----------|
| There is a general principle... | 有一个一般原理... |
| The main theme is... | 主题是... |
| At the heart of... lies... | ...的核心是... |
| It is no exaggeration to say... | 毫不夸张地说... |

#### 条件解释

| 英文表达 | 中文含义 | 使用场景 |
|----------|----------|----------|
| A moment's reflection suggests... | 稍微思考一下就会想到... | 解释条件必要性 |
| It suffices to assume... | 只需假设... | 放宽条件 |
| For simplicity, we assume... | 为简单起见，我们假设... | 简化条件 |
| The reliance on... is a device that allows us to... | 依赖...是为了让我们能够... | 解释技术性选择的动机 |

#### 证明过渡

| 英文表达 | 中文含义 | 使用场景 |
|----------|----------|----------|
| We claim that... | 我们声称... | 提出论断 |
| It suffices to show that... | 只需证明... | 简化目标 |
| To prove this, we... | 为了证明这一点，我们... | 开始证明 |
| We are done. | 证明完毕。 | 结束证明 |

### 写作检查清单

在写笔记时，检查是否满足以下要求：

- [ ] **动机明确**: 开篇是否解释了"为什么需要这个概念？"
- [ ] **循序渐进**: 是否从简单例子逐步过渡到抽象定义？
- [ ] **历史脉络**: 是否提及概念的起源或相关数学家？
- [ ] **有机联系**: 是否与已学内容建立联系？
- [ ] **条件解释**: 是否解释了引入某个条件的原因？
- [ ] **叙事流畅**: 定义→命题→证明之间是否有过渡句？

---

## 第五部分：附录公式推导原则

### 核心思想

从学习数学知识的角度，**公式推导是必要学习的**；但在理解思想、了解脉络、抓住重点的目的下，**公式推导/定理证明反而不是最重要的**，所以可以放到附录。在正文中抓住重点，以防被过长的数学公式分散了注意力。

### 具体做法

1. **正文保持流畅**：在正文中只写核心公式、主要结论和关键思想，不写出完整推导步骤
2. **附录存放推导**：将完整推导（包括证明、演算、计算过程）放到附录章节
3. **添加引用标记**：在正文的公式处添加脚注引用，例如：
   ```latex
   后验均值由下式给出：\footnote{推导见附录 \cref{sec:beta-binomial-posterior-mean}}
   \[
   \mathbb{E}(\theta|y) = \frac{\alpha+y}{\alpha+\beta+n}
   \]
   ```

### 附录推导的标准结构

每个公式推导小节应包含：
- **背景（Background）**: 完整的上下文和动机
- **参数定义（Parameter Definitions）**: 所有符号的含义
- **已知条件（Given）**: 已知的分布、假设、条件
- **目标（Goal）**: 要证明什么/计算什么
- **详细推导步骤（Derivation Steps）**: 每一步都要有解释

---

## 参考来源

- **LaTeX 规范**: 本项目的 `docs/latex-style.md`
- **Stein 写作风格**: Stein, E. M., & Shakarchi, R. (2003). *Fourier Analysis: An Introduction*. Princeton University Press.
- **Stein 系列**:
  - Stein, E. M., & Shakarchi, R. (2003). *Complex Analysis*. Princeton University Press.
  - 书籍转录: `PDFs/Stein系列/transcript/`
