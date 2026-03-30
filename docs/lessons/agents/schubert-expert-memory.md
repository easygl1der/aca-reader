# Schubert 演算专家教训记忆

**适用对象**: schubert-expert
**最后更新**: 2026-03-30

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L501 | Schubert 多项式符号约定 | 1 |
| L502 | Bruhat 顺序的表示 | 1 |
| L503 | 文献引用标注规范 | 1 |
| L504 | $I(\tau)$ 公式必须核对原论文 | 1 |
| L505 | Schubert 笔记排版——长公式必须拆解 | 1 |

---

## L501: Schubert 多项式符号约定

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了 Schubert 多项式的不同符号风格。

**正确做法**:
```latex
% Schubert 多项式
\mathfrak{S}_w  % 标准符号
S_w  % 简写（需说明）
% Schubert cell
X_w^\circ  % 开胞
X_w  % 闭包
```

**引用来源**:
- Macdonald - Schubert Polynomials
- Fulton - Young Tableaux

**防止措施**:
- 明确说明符号来源
- 引用原文献编号

---

## L502: Bruhat 顺序的表示

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
Bruhat 顺序符号不一致。

**正确做法**:
```latex
% Bruhat 顺序
u \leq w  % 偏序关系
u < w  % 严格不等（差一个 inversion）
\ell(w)  % w 的长度（inversions 个数）

% 性质：u \leq w 当且仅当每个 k 都有 u_k \leq w_k
```

**记忆方法**:
- $\leq$ 表示可以通过向右移动到达
- 长度 = inversion 个数

**防止措施**:
- 写 Bruhat 顺序时注明长度函数

---

## L503: 文献引用标注规范

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
Lemma/Theorem/Corollary 环境中的定理引用缺少原文献编号标注。

**正确做法**:
```latex
% 正确格式：定理名 + 原文编号 + \cite{}
\begin{Lemma}[Lemma 2.2 {\cite[ Lemma 2.2]{GX2025}}]
\label{def:Lemma22}
...
\end{Lemma}

% Theorem 格式
\begin{Theorem}[Graham Positivity Theorem {\cite[ Theorem 3.2]{Gr}}]
\label{def:GrahamPositivity}
...
\end{Theorem}

% Corollary 格式
\begin{Corollary}[Corollary 1.2: Kirillov 猜想 {\cite[Conjecture 1]{kirillov2007}}]
\label{cor:Kirillov}
...
\end{Corollary}
```

**引用规范清单**:
| 定理类型 | 格式要求 |
|----------|----------|
| Lemma | `\begin{Lemma}[Lemma X.Y {\cite[ Lemma X.Y]{KEY}}]` |
| Theorem | `\begin{Theorem}[名称 {\cite[ Theorem X.Y]{KEY}}]` |
| Corollary | `\begin{Corollary}[名称 {\cite[ Corollary X.Y]{KEY}}]` |
| Proposition | `\begin{Proposition}[名称 {\cite[ Proposition X.Y]{KEY}}]` |

**常见引用 key**:
- `GX2025` — Gao & Xiong (2025) - Triple Schubert Positivity
- `Sa` — Samuel (2024) - Molev-Sagan Formula
- `KM` — Kirillov & Maeno (1996) - Quantum Double Schubert
- `Gr` — Graham (2001) - Positivity in Equivariant Schubert Calculus
- `anderson2023` — Anderson & Fulton - Equivariant Cohomology

**防止措施**:
- 每次写 Lemma/Theorem/Corollary 前，先确认原文献编号
- 用 grep 检查是否有遗漏引用

---

## 领域专属符号表

```latex
% Schubert 演算核心符号
Flag Variety: Fl_n(\mathbb{C})
Schubert 多项式: \mathfrak{S}_w
Bruhat 顺序: u \leq w
长度函数: \ell(w)
Schubert 细胞: X_w^\circ
Stanley 对称函数: F_y
Grothendieck 多项式: \mathfrak{G}_w
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/schubert-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是 Schubert 专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认

---

## L504: $I(\tau)$ 公式必须核对原论文

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
schubert-expert-3 将 $I(\tau) = \{y_j - t_i\}$ 误认为是置换 $\tau$ 的普通反转集，实际上这是 GX2025 论文中专门定义的集合，用于限定展开系数的多项式结构。

**正确做法**:
- 论文中定义的特殊集合（如 $I(\tau)$）有专门含义，不能望文生义
- 发现疑似错误的公式时，先查阅原始论文确认
- GX2025 原文明确给出 $I(\tau) = \{y_j - t_i \mid 1 \leq i,j \leq n\}$

**论文位置**:
`PDFs/quantum-schubert/GaoXiong-TripleSchubertPositivity.pdf`

**防止措施**:
- 任何核心公式先查原文
- 笔记引用 ≠ 原创，发现存疑立即核实

---

## L505: Schubert 笔记排版——长公式必须拆解

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
在 qa.tex 中，一个涉及 Schubert 类相交的链式表达公式太长（87.9pt overfull）：
```latex
$$\overline{B^-uB/B} \cap \overline{B^-vB/B} \xrightarrow{\text{横截性}} \text{良定义的交点数} \xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w$$
```

**正确做法**:
```latex
\begin{align}
\overline{B^-uB/B} \cap \overline{B^-vB/B}
&\xrightarrow{\text{横截性}} \text{良定义的交点数} \label{eq:geo-to-integer} \\
&\xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \label{eq:integer-to-cohomology} \\
&\xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w \label{eq:cohomology-to-polynomial}
\end{align}
```

**Schubert 笔记排版高危模式**:
1. 涉及 Schubert 细胞闭包 $\overline{B^-wB/B}$ 的相交表达式
2. 涉及 $\xrightarrow{\text{...}}$ 链式翻译
3. 涉及 $\sum_w$ 多重求和

**检查命令**:
```bash
# 编译后立即检查 overfull hbox
grep -i "overfull\|hbox" schubert-positivity-notes.log
```

**修复记录**:
- 87.9pt too wide (line 1030) → 用 align 拆解为 3 行 ✅

**防止措施**:
- 写完长公式后立即编译检查
- 涉及 Schubert 类的复杂表达式优先用 align 拆解

