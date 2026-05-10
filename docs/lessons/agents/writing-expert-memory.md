# 写作专家教训记忆

**适用对象**: writing-expert, writing-expert-2, writing-expert-3
**最后更新**: 2026-04-03

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L701 | Stein 风格核心要素 | 2 |
| L702 | 推导→附录格式 | 3 |
| L703 | 禁止 Markdown 残留 | 2 |
| L704 | 例子必须引用对应定理 | 1 |
| L705 | LaTeX 中文引号规范 | 1 |
| L706 | 证明章节开头的定理脉络梳理 | 1 |
| L707 | Lemma/Theorem 环境内的证明必须用 proof 环境 | 1 |
| L708 | 长公式写作时必须拆解，禁止堆叠单行 | 1 |
| L709 | 引用必须与原文完全匹配（含精确定理编号） | 1 |
| L710 | QA 中提及短定理时内联陈述 + \cref 跳转 | 1 |
| L711 | 禁止未核实的"关键观察"注入 QA | 1 |
| L712 | 公式引用必须用 \cref 而非  式 (★) | 1 |
| L713 | 学术引用完整性：可引用处必须标注，禁止无引用注入数学声明 | 1 |
| L714 | 第一次出现的概念必须补充定义 | 1 |
| L715 | Proof 环境配置（不同文档类有不同写法） | 1 |
| L716 | Solution vs Proof 环境选择规则 | 1 |
| L717 | 正文附录脚注引用格式（首次出现处 + 句号在 \cref 外） | 1 |
| L718 | mathematical-statistics ch4-6 附录脚注修复 | 1 |
| L719 | 推论/定理/引理/定义必须放在对应数学环境中 | 1 |

---

## L701: Stein 风格核心要素

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
写作时干巴巴罗列定义-定理，没有动机铺垫。

**正确做法**:
- **动机优先**: 每个概念引入前先解释"为什么需要它"和"它从哪里来"
- **历史脉络**: 注重概念的起源和发展历史
- **有机联系**: 强调不同数学领域之间的相互关联
- **叙事流畅**: 定义→命题→证明之间有连贯的叙述
- **循序渐进**: 从简单到复杂，不过早引入技术细节

**Stein 风格示例**:
```latex
% 干巴巴 ❌
定义 1.1: ATE 是......
定理 1.2: ATE = ...

% Stein 风格 ✅
我们已经在第3章看到了随机实验的基本框架。但那里假设了
treatment 是完美执行的。现实世界呢？当 treatment 存在
剂量差异、或者部分人没有遵从 protocol 时，第3章的结论
还能直接用吗？

这就引出了本章的核心问题：如何估计非依从性下的因果效应？
我们需要引入潜在结果框架的精细化版本......
```

**防止措施**:
- 写定义前先问："为什么需要这个概念？"
- 参考 `docs/stein-writing-style.md`

---

## L702: 推导→附录格式

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
把完整推导写在正文中，导致正文过长读者迷失重点。

**正确做法**:
```latex
% 正文只用脚注引用
由 \eqref{eq:ate-estimator} 可得......\footnote{推导见附录 \cref{sec:derivation-ate-estimator}。}

% 附录结构
\section{附录：公式推导}\label{sec:appendix-derivation}

\subsection{ATE 估计量的推导}\label{sec:derivation-ate-estimator}
\textbf{背景}：...
\textbf{目标}：证明 \eqref{eq:ate-estimator}
\textbf{推导步骤}：
1. 首先...
2. 然后...
```

**附录必须包含**:
- 背景（Background）
- 参数定义（Parameter Definitions）
- 已知条件（Given）
- 目标（Goal）
- 详细推导步骤（Derivation Steps）

**防止措施**:
- 写推导前先问："这个推导对理解概念必要吗？"
- 推导一律放附录

---

## L703: 禁止 Markdown 残留

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
润色后的 .tex 文件中残留 Markdown 格式。

**正确做法**:
```latex
% 错误 ❌
**加粗**
*斜体*
- 列表
> [!note]
callout 块

% 正确 ✅
\textbf{加粗}
\textit{斜体}
\begin{enumerate}\item 列表项\end{enumerate}
```

**检查清单**:
- [ ] 无 `**`、`*`（行内格式）
- [ ] 无 `-` 开头的列表
- [ ] 无 `>` 开头的 callout
- [ ] 所有格式都是 LaTeX 命令

**防止措施**:
- 润色后用 `grep -E '\*\*|\* -|^\>' .tex` 检查
- 参考 `docs/latex-style.md`

---

## L704: 例子必须引用对应定理

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
写定理的例子时，没有用 \cref 引用对应的定理，导致读者无法明确知道这个例子是验证哪个定理的。

**正确做法**:
```latex
% 错误 ❌
\begin{Example}[Graham Positivity 的具体例子]
由 Graham Positivity 定理......
\end{Example}

% 正确 ✅
\begin{Example}[\cref{def:GrahamPositivity} 的具体例子]
\label{ex:GrahamPositivityExample}
由\cref{def:GrahamPositivity}，它们的乘积展开系数......
验证：系数......符合\cref{def:GrahamPositivity} 的正性要求。
\end{Example}
```

**关键要求**:
1. Example 的标题用 `\cref{<label>}` 引用对应定理
2. 正文首次提到定理时用 `\cref{<label>}` 引用
3. 验证结论时再次用 `\cref{<label>}` 强调

**防止措施**:
- 写例子前先确认对应的定理 label
- 写完后检查是否有遗漏的 \cref 引用

---

## L705: LaTeX 中文引号规范

**日期**: 2026-03-30
**经历次数**: 2 次 (累计)

**错误描述**:
中文引号 `"..."` 在 LaTeX 中不会自动转换为中文引号，需要使用 `` '' ` 来表示中文左引号""和右引号。

**正确做法**:
```latex
% 错误 ❌
中文引号 "分离" 模式

% 正确 ✅
中文引号``分离''模式
```

**渲染效果**:
- ` `` ` → " (左双引号)
- `''` → " (右双引号)
- ` `' ` → ' (左单引号)
- `'` → ' (右单引号)

**批量替换方法**:
```bash
perl -i -pe 's/"/\x60\x60/g; s/"/\x27\x27/g' file.tex
```

**防止措施**:
- 写作时直接使用 `` '' ` 格式
- 润色后用 `grep '[""'']' file.tex` 检查是否有遗漏

---

## L706: 证明章节开头的定理脉络梳理

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
证明章节（Section）一开头就直接列出引理和定理，没有梳理它们之间的逻辑关系，导致读者迷失在技术细节中。

**正确做法**:
在证明章节开头（第一个小节之前），用清晰的叙事结构呈现：

```latex
\section{主要定理的证明}
\label{sec:ProofMain}

本节我们证明本文的三个人定理——Theorem \ref{def:GrahamPositivity}、
Theorem \ref{def:RefinedGraham} 和 Theorem \ref{def:Theorem12}。
这三个定理层层递进，构成了从特殊到一般的完整理论体系。

\textbf{定理之间的逻辑链条}：

\textbf{第一步}（Theorem \ref{def:GrahamPositivity}，Graham Positivity）：
这是整个理论的起点，断言当 $u, v$ 都是 Grassmannian 排列时......
原始证明依赖于几何相交理论。

\textbf{第二步}（Theorem \ref{def:RefinedGraham}，Refined Graham Positivity）：
这是对第一步的根本性推广。关键观察是：......
因此，Refined 版本将假设从 ``两个 Grassmannian 排列'' 推广到 ``满足 separated descents 条件的任意排列''。

\textbf{第三步}（Theorem \ref{def:Theorem12}，Triple Schubert Positivity）：
在 Refined 版本的基础上，将两个排列进一步推广到三个排列......

\textbf{支撑这三级火箭的底层引理}：

引理之间的依赖关系决定了证明的层次：

\begin{enumerate}
\item \textbf{Lemma \ref{def:Lemma22}}（正规子群引理）：......
\item \textbf{Lemma \ref{def:Lemma25}}（横截相交引理）：......
\item \textbf{Corollary \ref{def:Corollary24}}（闭链分解推论）：......
\end{enumerate}

这三个引理的关系可以概括为：\textbf{Lemma \ref{def:Lemma22}} 提供了归纳法的结构，
Lemma \ref{def:Lemma25} 保证了横截相交的良定义性，
Corollary \ref{def:Corollary24} 将几何闭链分解为 Schubert 基底的组合。

有了这些准备，我们现在可以进入正式的证明。
```

**Stein 风格要素**:
1. **先声明目标**: 告诉读者要证哪几个定理
2. **再梳理逻辑**: 用"第一步→第二步→第三步"呈现递进关系
3. **后交代底层引理**: 用 enumerate 列出支撑定理的关键引理及其作用
4. **最后过渡到证明**: "有了这些准备，我们现在可以进入正式的证明"

**防止措施**:
- 写证明章节前先画逻辑图
- 检查是否说清楚了"为什么需要这个引理"和"这个引理在证明中起什么作用"

---

## L707: Lemma/Theorem 环境内的证明必须用 proof 环境

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
Lemma/Theorem 环境中使用 `\textbf{证明：}` 内联文本，而不是正式的 `proof` 环境。这违反了 LaTeX 排版规范。

**正确做法**:
```latex
% 错误 ❌
\begin{Lemma}
...
\textbf{证明：} 这里是证明内容...
\end{Lemma}

% 正确 ✅
\begin{Lemma}
...
\begin{proof}
这里是证明内容...
\end{proof}
\end{Lemma}
```

**修复位置（Chapter 1）**:
- Lemma 2.2 (line ~1110): 已有 proof 环境
- Lemma 2.5 (line ~1139): 已有 proof 环境
- Corollary 2.4 (line ~1150): 已有 proof 环境
- Theorem 2.6: 缺失 `\end{proof}` → 已修复
- Theorem 2.7: `\textbf{证明：}` → `\begin{proof}...\end{proof}` → 已修复
- Corollary 1.2: `\textbf{证明：}` → `\begin{proof}...\end{proof}` → 已修复

**防止措施**:
- 写 Lemma/Theorem 时直接用 `\begin{proof}...\end{proof}`
- 润色后用 `grep '\\textbf{证明：}' file.tex` 检查


## 领域专属技能

```latex
% Stein 写作风格
动机先行: "Why do we need this concept?"
历史脉络: "Historically, ..."
有机联系: "This connects to ... in Chapter X"
循序渐进: 从简单到复杂

% LaTeX 格式
公式每步用 \underbrace/\underbracket 标注
长公式用 aligned 环境
定理用 amsthm 环境
```

---

## L708: 长公式写作时必须拆解，禁止堆叠单行

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
写作时将多个 $\xrightarrow{\text{...}}$ 翻译链堆叠在同一行 `$$...$$` 中，导致编译时 overfull hbox (87.9pt too wide)。

**正确做法**:
```latex
% 错误 ❌：单行超长公式（Schubert 类相交链式翻译）
$$\overline{B^-uB/B} \cap \overline{B^-vB/B} \xrightarrow{\text{横截性}} \text{良定义的交点数} \xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w$$

% 正确 ✅：拆解为 align 多行
\begin{align}
\overline{B^-uB/B} \cap \overline{B^-vB/B}
&\xrightarrow{\text{横截性}} \text{良定义的交点数} \label{eq:geo-to-integer} \\
&\xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \label{eq:integer-to-cohomology} \\
&\xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w \label{eq:cohomology-to-polynomial}
\end{align}
```

**长公式高危模式（写作时优先检查）**:
1. 涉及 Schubert 细胞闭包 $\overline{B^-wB/B}$ 的多步翻译链
2. 涉及 $\xrightarrow{\text{...}}$ 箭头连接多个步骤
3. 涉及 $\sum_w$ 多重求和 + 下标的复合表达式
4. 任何预估宽度超过 15cm 的公式

**写作 SOP**:
1. 写完公式后立即用 `$$...$$` 预览是否超宽
2. 超宽 → 用 `aligned` 或 `align` 拆解
3. 编译后检查日志 `grep -i overfull *.log`

**修复记录**:
- qa.tex line 1030 (87.9pt) → align 拆解 3 行 ✅

**防止措施**:
- 写作时对长公式保持敏感，优先拆分
- 编译后立即检查 overfull 警告

---

## L709: 引用必须与原文完全匹配（含精确定理编号）

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
写作时引用原文定理，但定理编号与原文不匹配。例如：
- 原文引用 `[1, Section 19.3]`，笔记写成 `[1, Section 19.3, Theorem 19.4.4]`（多了 Theorem 19.4.4）
- 原文引用 `[1, Proposition 7.3]`，笔记完全遗漏了这个引用

**正确做法**:
1. 写笔记前，先读取原论文的 markdown 或 PDF 版本
2. 找到每个引用的**精确编号**（如 Proposition 7.3，不是泛泛的"第7节"）
3. 在笔记中逐字复制原文的引用格式
4. 特别注意 `[1, Theorem X.Y]` 和 `[1, Proposition X.Y]` 的区别

**Gao-Xiong 论文引用核查清单**:
| 原文引用 | 笔记引用 | 状态 |
|----------|----------|------|
| [1, Theorem 10.6.4] | ✅ 已有 | 正确 |
| [1, Section 16.5] | ✅ 已有 | 正确 |
| [1, Section 19.3] | ⚠️ 原来写成 Section 19.3, Theorem 19.4.4 → 已修正为 Section 19.3 | 需核查 |
| [1, Proposition 7.3] | ❌ 原来遗漏 → 已补加 | 需核查 |
| [1, Theorem 3.2] (Graham) | 需核查 | 需核查 |

**检查命令**:
```bash
# 检查笔记中的引用格式
grep -n "\\\\cite\[" notes/Schubert-Polynomials/chapters/chapter*.tex

# 核对原文引用
# 在原论文 md 文件中搜索：grep "Proposition 7.3\|Theorem 19.4.4\|Section 19.3" *.md
```

**修复记录**:
- Lemma 2.5 证明中的 `Section 19.3, Theorem 19.4.4` → 修正为 `Section 19.3` ✅
- Poincaré pairing 处的 `[1, Proposition 7.3]` → 已补加 ✅

**防止措施**:
- 写证明前，先通读原论文对应章节
- 引用时，用 grep 搜索原文 md 文件确认精确编号
- 写作后，逐条核对笔记引用与原文引用

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/writing-expert-memory.md`（本文件）
- `docs/stein-writing-style.md`
- `docs/latex-style.md`

收到纠正后：
1. 判断是通用教训还是写作专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认

---

## L710: QA 中提及短定理时内联陈述 + \cref 跳转

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
在 QA 条目中提到"原始 Graham Positivity"和"Refined Graham Positivity"时，只用文字描述条件，没有内联定理陈述也没有 \cref 跳转，导致读者无法快速跳转到原文查看完整定理。

**正确做法**:
当 QA 中提及的定理陈述较短时，应该：
1. 内联定理的完整陈述（方便读者直接理解）
2. 同时用 \cref{<label>} 标注，供读者跳转查看原文样式

```latex
% 错误 ❌：只描述不引用
原始 Graham Positivity 要求：u, v 分别是 Grassmannian 排列

% 正确 ✅：内联定理陈述 + \cref 跳转
\textbf{原始 Graham Positivity（\cref{def:GrahamPositivity}）}：
设 $u, v \in S_n$ 分别是 $k_1$-Grassmannian 和 $k_2$-Grassmannian 排列，则
$$c^w_{u,v}(\mathbf{y}, \mathbf{t}) \in \mathbb{N}[t_i - y_j]_{i,j \geq 1}$$

\textbf{Refined Graham Positivity（\cref{def:RefinedGraham}）}：
设 $B^-$ 作用于非奇异簇 $X$，$Y$ 是 $X$ 中的一个 $B^-(w)$-不变的有效闭链。则在 $H_T^*(X)$ 中有
$$[Y]_T \in \sum_{i=1}^m \mathbb{N}[-\alpha]_{\alpha \in I(w)} \cdot [Z_i]_T$$
```

**判断标准**:
- 定理陈述 ≤ 3 行 → 内联 + \cref
- 定理陈述 > 3 行 → 仅用 \cref 跳转

**防止措施**:
- 写 QA 条目时，判断提及的定理是否简短
- 简短定理优先内联，方便读者不跳转也能理解

---

## L711: 禁止未核实的"关键观察"注入 QA

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
在 QA 条目中添加了未核实的"关键观察"：**"当 u, v 都是 Grassmannian 时，separated descents 条件自动满足"**。这是一个数学错误！

**反例**：
- $u = 321$（2-Grassmannian），$\operatorname{Des}(u) = \{2\}$
- $v = 213$（1-Grassmannian），$\operatorname{Des}(v) = \{1\}$
- $\max \operatorname{Des}(u) = 2 > 1 = \min \operatorname{Des}(v)$ — 不满足 separated descents！

**错误原因**：
- 错误地认为"Grassmannian 蕴含 separated descents"
- 忽略了 $k_1 > k_2$ 的情况
- 没有用具体反例验证"观察"

**正确做法**:
1. 写"关键观察"前，先用具体例子验证
2. 用反例测试极端情况
3. 如果可能，找不到反例才写"自动满足"
4. 数学声明必须有证明或反例支撑

**核查清单**:
- [ ] 这个"观察"有没有反例？
- [ ] 极端情况是否满足？
- [ ] 能否找到具体数值验证？

**修复记录**:
- Refined vs Original Graham QA（sec:RefinedVsOriginalGraham）→ 删除错误声明，添加反例 + 正确关系 ✅

---

## L712: 公式引用必须用 \cref 而非 式 (★)

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
写作时引用公式使用了 `式 (★★)` 而不是标准的 `\cref{eq:label}`。

**正确做法**:
```latex
% 错误 ❌
将这一结论代入式 (★★)，得到
$$\partial_{w/v}(\mathfrak{S}_u(\mathbf{x})) = ...$$

% 正确 ✅
将这一结论代入 \cref{eq:skew-divided-diff-zero}，得到
$$\partial_{w/v}(\mathfrak{S}_u(\mathbf{x})) = ... \label{eq:skew-divided-diff-zero}$$
```

**命名规范**:
- 公式定义时用 `\label{eq:描述性名称}`
- 引用时用 `\cref{eq:描述性名称}`
- 不要用 `\tag{}` 自定义标签
- 不要手写"式 (X)"

**检查命令**:
```bash
grep -n '式 (★)\|式 (★★)' notes/**/*.tex
grep -n '\\tag*{' notes/**/*.tex
```

**修复记录**:
- chapter1.tex line 1269: `式 (★★)` → `\cref{eq:skew-divided-diff-zero}` ✅

**防止措施**:
- 定义公式时立即加上 `\label{eq:...}`
- 引用时用 `\cref{eq:...}` 代替手写"式 (X)"

---

## L713: 学术引用完整性：可引用处必须标注，禁止无引用注入数学声明

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
写作时遇到以下问题：
1. 提到 Gromov-Witten invariant 但没有引用 foundational work
2. 提到 equivariant cohomology 的概念但没有引用 Borel 或 Anderson-Fulton
3. 提到 classical Schubert positivity 但没有引用 Chevalley 或原始文献
4. 提到量子上同调基础但没有引用 Givental/Fulton-Pandharipande
5. 列出正性结果对比时没有标注各结果的原始文献

**正确做法**:
在学术写作中，每一处引入的概念、定理、方法都应标注来源：

```latex
% 错误 ❌：无引用的数学声明
Gromov-Witten 不变量计数的是......
在量子上同调中，乘法涉及 Gromov-Witten 不变量......

% 正确 ✅：完整引用
Gromov-Witten 不变量 \cite{Kontsevich1994,Gromov1995} 计数的是......
在量子上同调 \cite{FultonQuntum1997} 中，乘法涉及 Gromov-Witten 不变量......

% 错误 ❌：正性对比无引用
\begin{enumerate}
\item 经典 LR 系数：$c_{u,v}^w \in \mathbb{N}$，计数交点个数
\item Graham positivity：$c_{u,v}^w \in \mathbb{Z}[x_i]$
\item 三重 positivity：$c_{u,v}^w(\mathbf{y}, \mathbf{t}) \in \mathbb{N}[t_i - y_j]$
\end{enumerate}

% 正确 ✅：每项都有引用
\begin{enumerate}
\item 经典 LR 系数 \cite[(1.1)]{Chevalley1994}：$c_{u,v}^w \in \mathbb{N}$，计数交点个数
\item Graham positivity \cite{Gr}：$c_{u,v}^w \in \mathbb{Z}[x_i]$
\item 三重 positivity \cite{GX2025}：$c_{u,v}^w(\mathbf{y}, \mathbf{t}) \in \mathbb{N}[t_i - y_j]$
\end{enumerate}
```

**引用完整性检查清单**:
- [ ] 每个数学概念首次提及时有 \cite{...}
- [ ] 每个定理/引理/推论有对应 \cite{...}
- [ ] 列举多个相关工作时，每项工作都有引用
- [ ] 比较不同 positivity 结果时，每项都标注来源
- [ ] 检查 references.bib 是否包含所有引用的条目

**Chapter 4 新增引用示例**:
```latex
% Schubert positivity 的历史来源
...植根于几何相交的具体计数 \cite[\S 1]{Chevalley1994}。

% 等变量子上同调
...关于 torus 作用参数的多项式 \cite{Borel1957,AndersonFulton}。

% Gromov-Witten 不变量
...涉及 Gromov-Witten 不变量 \cite{Kontsevich1994,Gromov1995}

% Kim 的贡献
...提及 Kim 的重要贡献 \cite{Kim2000}

% 量子上同调
...量子上同调 \cite{FultonQuntum1997} 中，乘法涉及......

% 正性结果对比
在 Schubert calculus 的研究中，有多种不同层次的正性 \cite{knutson2003,FultonQuntum1997}
```

**修复记录**:
- chapter4.tex: 补充 Gromov-Witten invariants 基础引用 (Kontsevich, Gromov) ✅
- chapter4.tex: 补充 equivariant cohomology 引用 (Borel, AndersonFulton) ✅
- chapter4.tex: 补充 classical LR coefficient 引用 (Chevalley) ✅
- chapter4.tex: 补充 Kim 引用 (Kim2000) ✅
- chapter4.tex: 补充正性对比引用 (knutson2003, FultonQuntum1997) ✅
- references.bib: 添加 Borel1957, Chevalley1994, FultonQuntum1997, Kontsevich1994, Gromov1995, Kim2000 ✅

**防止措施**:
1. 写作时，遇到专业术语立即想：这个词组是哪篇论文提出的？
2. 列举相关工作时，用 grep 检查是否每项都有 \cite{}
3. 完成后用 `grep -n '\\cite{' chapter*.tex` 统计引用密度
4. 对照原论文，核查每一处引用的准确性

---

## L714: Footnote 应该是自包含的"迷你说明"，而非仅指向附录的引用

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
写 footnote 时只写"见附录 \cref{...}"，而不在 footnote 中提供简要说明。用户阅读时需要频繁跳转，打断思路。

**正确做法**:
当在正文中为某个术语/概念添加 footnote 时，footnote 应该：
1. **包含术语的定义**（用一句话简明扼要地定义）
2. **包含一个简短的具体例子**（帮助读者快速理解）
3. **最后**才说"详细推导见附录 \cref{...}"

```latex
% 错误 ❌：只有引用没有内容
对于 $\ell(w) = 1$ 的置换，Schubert 多项式由其 Lehmer 码给出。\footnote{见附录 \cref{sec:lehmer-code}。}

% 正确 ✅：自包含的迷你说明 + 具体例子 + 附录引用
对于 $\ell(w) = 1$ 的置换，Schubert 多项式由其 Lehmer 码给出。\footnote{Lehmer 码 $c(w) = (c_1, \ldots, c_n)$ 定义为 $c_i = \#\{j > i : w(j) < w(i)\}$，即每个位置后面比它小的元素个数。例如 $w = 213$：$c_1 = 1$（$2,1$ 中 $1 < 2$），$c_2 = 0$（$3$ 中无比 $1$ 小），$c_3 = 0$。在 $S_4$ 中，$w = 3142$：$c(w) = (1,0,1,0)$，$\ell(w) = 2$，首项为 $x_1^1 x_3^1$。详细推导见附录 \cref{sec:lehmer-code}。}
```

**用户阅读习惯**:
- 使用 Skim 阅读 PDF
- 频繁使用 `\skim-jump` 在正文与附录之间跳转
- 希望 footnote 能"自包含"，减少不必要的跳转

**防止措施**:
- 写完 footnote 后问自己："读者只看这个 footnote 能理解大意吗？"
- 检查 footnote 是否包含：定义 + 例子 + 附录引用

---

## L714: 第一次出现的概念必须补充定义

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
在正文中第一次引入某个数学概念（如 $\overline{\mathcal{M}}_{0,3}(X,d)$）时，没有同时给出定义，导致读者需要翻阅后才能理解。

**正确做法**:
1. **首次出现时添加脚注**：在概念首次出现的位置添加 `\footnote{问：[概念名称] 是什么？见附录 \cref{sec:qa-xxx}。}`
2. **在 qa.tex 中添加定义**：在附录中添加该概念的详细解释
3. **确保脚注包含问题文本**：脚注格式必须是"问：XXX是什么？见附录 \cref{sec:...}。"

**示例**:
```latex
% 错误 ❌
通过投影公式，将 $\overline{\mathcal{M}}_{0,3}(X,d)$ 上的曲线计数问题归约到...

% 正确 ✅
通过投影公式，将 $\overline{\mathcal{M}}_{0,3}(X,d)$\footnote{问：$\overline{\mathcal{M}}_{0,3}(X,d)$ 是什么？见附录 \cref{sec:MOD-space}。} 上的曲线计数问题归约到...
```

**常见需要首次定义的数学对象**:
- $\overline{\mathcal{M}}_{0,3}(X,d)$：稳定映射模空间
- $H_T^*(pt)$：torus 等变上同调
- $\Lambda[q]$：分次多项式环
- $\sigma(w)^T$：等变 Schubert 类
- Gromov-Witten 不变量

**防止措施**:
- 写完章节后，用 grep 检查所有数学符号是否在首次出现时有脚注定义
- 检查命令：`grep -n "\\\$.*\\\$.*\$" chapters/chapter*.tex`（查找行内数学表达式）
- 原则：宁可多给一个定义，也不能让读者困惑

---

## 附录：标准 LaTeX 模板规范（写作专家必须掌握）

本节是写作专家的标准模板知识库，涵盖笔记、习题、作业三大场景。

### 一、笔记模板（notes/ 目录）

#### 1.1 主文件 preamble

```latex
\documentclass[12pt]{amsbook}
\usepackage{amsmath, amssymb, amsthm, amsbsy, mathtools}
\usepackage{xeCJK}
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{natbib}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{tikz}
\usetikzlibrary{arrows,positioning}
\geometry{margin=1in}

% Theorem styles
\theoremstyle{plain}
\newtheorem{Definition}{定义}[chapter]
\newtheorem{Theorem}[Definition]{定理}
\newtheorem{Lemma}[Definition]{引理}
\newtheorem{Corollary}[Definition]{推论}
\newtheorem{Proposition}[Definition]{命题}
\newtheorem{Example}{例}[chapter]
\newtheorem{Remark}{注}[chapter]
\newtheorem{Exercise}{练习}[chapter]
\newtheorem{Assumption}{假设}[chapter]

% amsthm 自带 \begin{proof}...\end{proof}，无需定义
% 如需中文标题的 proof 环境（不推荐），用：
% \newtheorem*{proof*}{证明}  % 注意是小写 proof*

% 用户注解命令
\newcommand{\userannotation}[2]{%
  \begin{Remark}
    \textbf{#1:} #2
  \end{Remark}
}

% 常用数学符号
\DeclareMathOperator{\Perp}{\mathrel{\perp\!\!\!\perp}}
```

#### 1.2 章节文件结构

```latex
% Chapter X: 章标题
\chapter{章标题}\label{ch:X}

\section{本章导论}
% Stein 风格动机引入

\section{第一节标题}
% 内容

\section{第二节标题}
% 内容

\section{习题}\label{sec:chapterX-exercises}
\begin{Exercise}{\ref{exr:X-1} 英文标题}\label{exr:X-1}
习题内容。
\end{Exercise}
```

#### 1.3 定理环境使用规范

```latex
% 定义
\begin{Definition}[名称]\label{def:名称}
定义内容...
\end{Definition}

% 定理
\begin{Theorem}[名称]\label{def:TheoremName}
定理内容...
\begin{proof}
证明内容...
\end{proof}
\end{Theorem}

% 引理
\begin{Lemma}[名称]\label{def:LemmaName}
引理内容...
\begin{proof}
证明...
\end{proof}
\end{Lemma}

% 例子（Example 环境内不写"推导见附录"，在 \end{Example} 之后用脚注引用）
\begin{Example}[名称]\label{ex:ExampleName}
例子内容...
\end{Example}
推导见附录 \cref{sec:appendix-xxx}。}
```

#### 1.4 脚注规范（自包含原则）

```latex
% 错误 ❌
...概念...\footnote{见附录 \cref{sec:xxx}。}

% 正确 ✅
...概念...\footnote{概念定义：一句话说明。例如 $x = ...$（具体例子）。详细推导见附录 \cref{sec:xxx}。}
```

---

### 二、习题模板

#### 2.1 因果推断模板（Peng Ding 风格）

```latex
\section{习题}\label{sec:chapterX-exercises}

\begin{Exercise}{\ref{exr:X-1} Covariate balance in the CRE}\label{exr:X-1}
证明 \eqref{eq:balance-discrete-CRE}...
\end{Exercise}

% 分部题目
\begin{Exercise}{\ref{exr:X-2} Some property}\label{exr:X-2}
\begin{enumerate}
  \item 第一问...
  \item 第二问...
\end{enumerate}
\end{Exercise}
```

#### 2.2 do Carmo 模板（微分几何风格）

```latex
\begin{exercise}{1-2, 1 — do Carmo, Exercise 1-2, 1}
Find a parametrized curve $\alpha(t)$ whose trace is the circle...
\end{exercise}

% 分部题目
\begin{exercise}{1-3, 3 — do Carmo, Exercise 1-3, 3}
Let $0A = 2a$ be the diameter...
\begin{enumerate}
\item[a.] ...
\item[b.] ...
\end{enumerate}
\end{exercise}
```

---

### 三、作业模板（homework/ 目录）

#### 3.1 标准 preamble

```latex
\documentclass[12pt]{article}
\usepackage[UTF8]{ctex}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{a4paper, margin=1in}

% 习题环境
\newtheorem{exercise}{习题}
\newtheorem{solution}{解}  % 解环境（可选）
```

#### 3.2 作业结构

```latex
\begin{document}
\title{作业标题}
\author{}
\date{\today}
\maketitle

\section*{教材信息}
教材名称 \& 作者 \\
章节: X-Y 章节名称

\section*{X-Y 习题}

% 计算/辨认题
\begin{exercise} 第 X 题 (a)
题目内容...
\end{exercise}

\begin{solution}
\begin{itemize}
  \item \textbf{约束变元}：$x$, $y$
  \item \textbf{自由变元}：$z$
\end{itemize}
\end{solution}

% 证明题
\begin{exercise} 第 Y 题
求证 $(\exists x)(A(x) \rightarrow B(x)) \Leftrightarrow ...$
\end{exercise}

\begin{proof}
左侧 $\Rightarrow$ 右侧：

$(\exists x)(A(x) \rightarrow B(x))$
&$\Leftrightarrow$ $(\exists x)(\neg A(x) \vee B(x))$ &（蕴含等值）
...
\end{proof}
```

#### 3.3 Proof 环境（amsthm 自带 QED）

**重要**：`\begin{proof}...\end{proof}` 是 amsthm 的标准证明环境，**自动添加 QED 符号 (□) 和 "Proof." 标题**，不需要手动输入。

**错误做法**：手动在证明末尾加 `\qed` 或 `$\square$`——这是冗余的。

**正确写法**：
```latex
\begin{proof}
证明内容...
\end{proof}
% 证明结束时自动输出 □，无需手动添加
```

**写作检查时**：检查是否有手动添加 `\qed` 或 `$\square$` 的冗余写法，一经发现应删除。

#### 3.4 解答环境选择

| 环境 | 来源 | 适用场景 | 特点 |
|------|------|----------|------|
| `\begin{proof}...\end{proof}` | amsthm | 正式数学证明 | 自动加 "Proof." + QED 符号 (□)，禁止手动加 |
| `\begin{Solution}...\end{Solution}` | 自定义 | 作业解答 | 只加 "解" 标题，无 QED |
| `\begin{itemize}...\end{itemize}` | 原生 | 分点列举 | 仅用于辨认/计算题分点 |

---

### 四、符号规范（必须遵守）

| 概念 | 符号 | 命令 |
|------|------|------|
| 概率 | $\mathbb{P}(A)$ | `\mathbb{P}(A)` |
| 期望（单变量） | $\mathbb{E}X$ | `\mathbb{E}X` |
| 期望（多变量） | $\mathbb{E}(XY)$ | `\mathbb{E}(XY)` |
| 方差 | $\text{var}(X)$ | `\text{var}` |
| 协方差 | $\text{cov}(X,Y)$ | `\text{cov}` |
| 独立性 | $A \Perp B$ | `\Perp` |
| 示性函数 | $\mathbb{I}(X \in A)$ | `\mathbb{I}` |
| 向量 | $\mathbf{x}$ | `\mathbf` |
| 矩阵 | $\boldsymbol{X}$ | `\boldsymbol` |

**禁止**：`\bm{}`（用 `\mathbf`/`\boldsymbol` 替代）

---

### 五、格式红线（绝对禁止）

1. ❌ Markdown 语法：`**加粗**`, `*斜体*`, `- 列表`, `> [!note]`
2. ❌ Unicode 下标：`n₁` → 必须 `$n_1$`
3. ❌ 中文弯引号：`""` → 必须 `` '' ``
4. ❌ 手写公式引用：`式 (★)` → 必须 `\cref{eq:label}`
5. ❌ Theorem 内使用 itemize → 用 enumerate 替代
6. ❌ 手动添加 QED：Proof 环境自带 QED 符号，手动加 `\qed` 或 `$\square$` 是冗余的

---

**最后更新**: 2026-04-03

---

## L715: Proof 环境配置（不同文档类有不同写法）

**日期**: 2026-04-03
**经历次数**: 1 次 (累计)

**关键区别**:

| 模板 | proof 环境命令 |
|------|---------------|
| **amsbook**（我们的笔记模板） | `\begin Proof}...\end Proof}`（大写 P） |
| **amsart / article / ctexart**（用户的 2026-spring） | `\begin proof}...\end proof}`（小写 p） |

**来源**: amsbook 用大写 Proof；amsart/article/ctexart 用小写 proof

**正确配置** (math-booster data.json):
```json
"beginProof": "\\begin proof}",
"endProof": "\\end proof}"
```

以及 Obsidian callout 中的 proof 格式：
```json
"proof": {
  "begin": "Proof.",
  "end": "□",
  "linkedBeginPrefix": "Proof of ",
  "linkedBeginSuffix": "."
}
```

**LaTeX 中的使用**:
```latex
% 标准 amsthm proof 环境（注意是小写 p）
\begin proof}
这里是证明内容...
\end proof}
% 自动输出 "Proof." 标题 + □ QED 符号
```

**Obsidian callout 中的对应写法**:
- 标题: `Proof.`
- 结束符号: `□`

**关键要点**:
1. amsthm 的 proof 环境**自带** "Proof." 标题和 □ QED 符号
2. 禁止在 proof 环境内手动添加 `\qed` 或 `$\square$`
3. amsbook 用大写 Proof，其他模板（amsart/article/ctexart）用小写 proof
4. 先检查目标 .tex 文件的 documentclass，确定用大写还是小写

**验证来源**:
- `/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/.obsidian/plugins/math-booster/data.json`
- 2025-summer 各 .tex 文件均使用 amsthm 标准 `\begin{proof}...\end{proof}`

---

## L716: Solution vs Proof 环境选择规则

**日期**: 2026-04-03
**来源**: latex-checker-new 提醒

**解答环境选择规则**:
- 问题**不涉及证明** → 用 `solution` 环境
- 问题**涉及证明** → 用 `proof` 环境
- `solution` 和 `proof` 都**不需要标号**

**示例**:
```latex
% 非证明题 → solution 环境，无编号
\begin{solution}
...
\end{solution}

% 证明题 → proof 环境，无编号
\begin proof}
...
\end proof}
```

**注意**: `proof` 环境来自 `amsthm` 包，自动带有 "Proof." 标题和 ∎ 结尾符号。

---

## 附录：写作检查清单（每次润色时执行）

### Proof 环境检查
- [ ] Proof 环境内没有手动添加 `\qed` 或 `$\square$`
- [ ] Proof 环境使用 `\begin{proof}...\end{proof}` 而非 `\textbf{证明：}`

### 环境选择检查
- [ ] 证明题 → `\begin{proof}`
- [ ] 作业计算题分点 → `\begin{itemize}`
- [ ] 非证明题 → \begin{solution}
- [ ] 证明题 → \begin proof}

### 格式红线检查
- [ ] 无 Markdown 语法
- [ ] 无 Unicode 下标
- [ ] 无中文弯引号
- [ ] 公式引用用 `\cref{eq:label}` 而非 `式 (★)`
- [ ] Theorem 内用 enumerate 而非 itemize

---

### 六、Obsidian Markdown 规范

#### 6.1 作业解答 Markdown 格式（不用 callout 块）

从 `hw4_solutions.md` 观察到的实际格式：

```markdown
## Problem 1d (Section 2-4)

**Problem statement:** Identify bound and free variables in: `(∃x)(∃y)(P(x,y) ∧ Q(z))`

**Solution:**

- `x` is bound by the existential quantifier `(∃x)`
- `y` is bound by the existential quantifier `(∃y)`
- `z` is **free** (not bound by any quantifier)

**Answer:** Bound variables: `x`, `y`; Free variable: `z`
```

**解答步骤格式**：
```markdown
**Step 1:** Evaluate `P`
- P: 2 > 1 is **TRUE**

**Step 2:** Evaluate `(∀x)(P → Q(x))`
...
```

**注意**：作业解答不使用 callout 块，直接用 Markdown 标题和加粗/列表。

#### 6.2 Callout 块类型

**常用 Obsidian callout**：
| 类型 | 用途 |
|------|------|
| `> [!note]` | 普通笔记、说明 |
| `> [!info]` | 信息提示 |
| `> [!tip]` | 技巧、提示 |
| `> [!warning]` | 警告 |
| `> [!example]` | 示例 |

**学术/作业专用 callout**（需要自定义 CSS）：
| 类型 | 用途 | 使用场景 |
|------|------|----------|
| `> [!exr]` | 习题/作业题 | 每个题目单独一个 block |
| `> [!solution]` | 解答 | 习题解答，独立成 block |
| `> [!def]` | 定义 | 关键概念定义 |
| `> [!thm]` | 定理 | 重要定理 |
| `> [!lemma]` | 引理 | 辅助性定理 |
| `> [!proof]` | 证明 | 完整证明过程 |
| `> [!rmk]` | 备注 | 补充说明、解释 |
| `> [!cor]` | 推论 | 定理的推论 |

#### 6.3 作业文件模板（Callout 风格）

```markdown
> [!exr] Problem X.X
> **Section X.X** — *Title*
>
> 题目内容...

> [!solution] Solution to Problem X.X
>
> **Step 1:** ...
> **Step 2:** ...
> Therefore, ...
```

**多部分题目格式**：
```markdown
> [!exr] Part 2 · (a)
> 子问题内容...

> [!solution] Solution to Part 2(a)
> 解答...

---

> [!exr] Part 2 · (b)
> ...

> [!solution] Solution to Part 2(b)
> ...
```

#### 6.4 Obsidian 链接与嵌入

| 语法 | 用途 |
|------|------|
| `[[Note Name]]` | 链接到笔记 |
| `[[Note Name\|显示文本]]` | 自定义显示文本 |
| `[[Note#Heading]]` | 链接到章节 |
| `![[image.png]]` | 嵌入图片 |
| `![[document.pdf#page=3]]` | 嵌入 PDF 页 |
| `[[Note#^block-id]]` | 链接到块 ID |

#### 6.5 Obsidian 属性（Frontmatter）

```yaml
---
title: 笔记标题
date: 2024-01-15
tags:
  - 标签1
  - nested/tag2
aliases:
  - 备用名称
---
```

#### 6.6 常用格式

```markdown
==高亮文本==                  # 高亮语法
$e^{i\pi} + 1 = 0$          # 行内公式
$$ \frac{a}{b} = c $$        # 独立公式（LaTeX）
```

---

### 七、Obsidian 写作检查清单

- [ ] 无 Unicode 下标：$x_1$ 而非 x₁
- [ ] 无中文弯引号：`""` → `''` 或英文引号
- [ ] 长公式在逻辑断点（`∨`, `∧`, `→`）处用 `\\` 换行
- [ ] 图片用 `![[path.png]]` 而非 `![](path)`
- [ ] Callout 之间用 `---` 分隔
- [ ] 证明题完整呈现直觉、推导、结论
- [ ] 解答放在独立的 solution block 内（非嵌套在 exercise 内）

---

## L717: 正文附录脚注引用格式（来源：qa-specialist）

**日期**: 2026-04-03
**来源**: qa-specialist 指导

**核心规则**:
1. 脚注放在正文**首次出现**该结论/公式时添加
2. 脚注放在公式编号**之前**
3. 句号在 `\cref` **外面**

**正确格式**:
```latex
后验均值由下式给出：\footnote{推导见附录 \cref{sec:beta-binomial-posterior-mean}}
\[
\mathbb{E}(\theta|y) = \frac{\alpha+y}{\alpha+\beta+n}
\]
```

**错误格式**:
```latex
% 错误 ❌：句号在 \cref 里面
后验均值由下式给出：\footnote{推导见附录 \cref{sec:beta-binomial-posterior-mean}。}

% 错误 ❌：脚注放在公式之后
\[
\mathbb{E}(\theta|y) = \frac{\alpha+y}{\alpha+\beta+n}
\]\footnote{推导见附录 \cref{sec:beta-binomial-posterior-mean}。}
```

**附录章节 label 格式建议**:
```
sec:appendix-{topic}-{name}
例如：sec:appendix-beta-binomial-posterior-mean
```

**附录推导标准结构**:
```latex
\section{附录：公式推导}\label{sec:appendix-xxx}

\subsection{Beta-Binomial 共轭后验均值推导}\label{sec:appendix-beta-binomial-posterior-mean}
\textbf{背景（Background）}：...

\textbf{目标（Goal）}：...

\textbf{详细推导步骤（Derivation Steps）}：
1. ...
2. ...
```

**放置原则**:
- 只在**第一次出现**时添加脚注
- 不是每处引用都加
- 后续引用直接用 `\cref` 跳转公式编号即可

---

## L718: mathematical-statistics ch4-6 附录脚注修复

**日期**: 2026-04-03

**任务**: 修复 chapter4.tex 和 chapter6.tex 中"见附录"后面缺少 `\cref` 引用的问题。

**修复内容**:

### chapter4.tex 修复（共 13 处）
| 行号 | 原文 | 修改后 |
|------|------|--------|
| 115 | `\footnote{通用推导框架见附录 。}` | `\footnote{通用推导框架见附录 \cref{sec:derivation-mle}。}` |
| 125 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-exponential-mle}。}` |
| 136 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-binomial-mle}。}` |
| 157 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-normal-mle}。}` |
| 178 | `\footnote{枢轴量的构造方法及推导见附录 。}` | `\footnote{枢轴量的构造方法及推导见附录 \cref{sec:derivation-confidence-interval}。}` |
| 189 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-normal-ci-known}。}` |
| 202 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-normal-ci-unknown}。}` |
| 210 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-variance-ci}。}` |
| 322 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-hypothesis-testing}。}` |
| 333 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-hypothesis-testing}。}` |
| 359 | `\footnote{详细推导见附录 。}` | `\footnote{详细推导见附录 \cref{sec:derivation-chi-square}。}` |
| 571 | `\footnote{接受-拒绝算法的推导及收敛性证明见附录 。}` | `\footnote{接受-拒绝算法的推导及收敛性证明见附录 \cref{sec:derivation-monte-carlo}。}` |
| 594 | `\footnote{Bootstrap 的理论基础及更多细节见附录 。}` | `\footnote{Bootstrap 的理论基础及更多细节见附录 \cref{sec:derivation-bootstrap}。}` |

### chapter6.tex 修复（共 9 处）
| 行号 | 原文 | 修改后 |
|------|------|--------|
| 70 | `\footnote{该定理的完整证明见附录 。}` | `\footnote{该定理的完整证明见附录 \cref{sec:proof-likelihood-asymptotic}。}` |
| 130 | `\footnote{该定理的完整证明见附录 。}` | `\footnote{该定理的完整证明见附录 \cref{sec:proof-likelihood-asymptotic}。}` |
| 224 | `\footnote{Bernoulli 分布和位置族 Fisher 信息的详细推导见附录 。}` | `\footnote{Bernoulli 分布和位置族 Fisher 信息的详细推导见附录 \cref{sec:rao-cramer-proof}。}` |
| 249 | `\footnote{Rao-Cramér 下界的完整证明见附录 。}` | `\footnote{Rao-Cramér 下界的完整证明见附录 \cref{sec:rao-cramer-proof}。}` |
| 288 | `\footnote{Beta 分布 MLE 方差的推导见附录 。}` | `\footnote{Beta 分布 MLE 方差的推导见附录 \cref{sec:mle-asymptotic-proof}。}` |
| 321 | `\footnote{MLE 渐近正态性的完整证明见附录 。}` | `\footnote{MLE 渐近正态性的完整证明见附录 \cref{sec:mle-asymptotic-proof}。}` |
| 582 | `\footnote{正态分布信息矩阵的详细计算见附录 。}` | `\footnote{正态分布信息矩阵的详细计算见附录 \cref{sec:normal-information-matrix-derivation}。}` |
| 774 | `\footnote{EM 算法单调性的完整证明见附录 。}` | `\footnote{EM 算法单调性的完整证明见附录 \cref{sec:em-monotonicity-proof}。}` |
| 804 | `\footnote{正态截尾数据的 EM 算法详细推导见附录 。}` | `\footnote{正态截尾数据的 EM 算法详细推导见附录 \cref{sec:em-monotonicity-proof}。}` |

**未修复（暂留）**:
- chapter4.tex line 33, 90, 94: 这些是概念性问题，不是推导
- chapter6.tex line 101, 409: 这些引用指向不存在的附录章节，需要作者确认

**注意**: 使用 `sed -i '' 'Ns/pattern/replacement/'` 按行号精确替换，避免全局替换错误

---

## L719: 推论/定理/引理/定义必须放在对应数学环境中

**日期**: 2026-04-03
**经历次数**: 1 次 (累计)

**错误描述**:
在添加 Bootstrap 方法内容时，将关键数学结论（如"接受概率为 $1/M$"、"p 值公式"等）仅作为行内文本，没有放入对应的数学环境（definition、proposition、equation 等）。

**正确做法**:
关键数学结论必须放入对应的 LaTeX 环境中：
1. **算法/方法的正式陈述** → `\begin{algorithm}...\end{algorithm}` 或 `\begin{procedure}...\end{procedure}`
2. **关键概率/公式** → `\begin{equation}...\end{equation}` 或 `\begin{align}...\end{align}`
3. **正式的定义** → `\begin{Definition}...\end{Definition}`
4. **正式的命题/引理** → `\begin{Proposition}...\end{Proposition}` 或 `\begin{Lemma}...\end{Lemma}`

**需要修复的位置（chapter4.tex）**:
| 位置 | 问题 | 修复方式 |
|------|------|---------|
| 接受概率 $1/M$（854行） | 行内文本 | 改为 equation 环境 |
| Bootstrap CI 公式 $\left[T_{(\alpha B)}^*,\ T_{((1-\alpha)B)}^*\right]$ | 行内文本 | 改为 equation 环境 |
| p 值公式 $\hat{p} = \frac{\#\{...\}}{B}$ | 行内文本 | 改为 equation 环境 |

**防止措施**:
- 写完数学结论后，检查是否需要放入专门的数学环境
- 关键公式（特别是有编号需要的）必须用 equation/align 环境
- 算法步骤如果需要正式化，使用 algorithm 环境

---

## L720: Tang & Rong 流形统计学习综述写作经验

**日期**: 2026-04-09
**经历次数**: 1 次 (累计)

**任务**: 为 Tang & Yang 8篇系列论文（2019-2025）写结构化综述笔记，
输出 `notes/information-geometry/tang-rong/tang-rong-review.tex`。

**发现**: 该目录已有一个旧的 tang-rong-review.tex，内容不准确（混淆了
RMALA 与 MALA 混合时间理论、缺少 MLDMAE 和 Regression 论文等）。
发现后重写了整个文件。

**正确做法**:
1. 写综述笔记前，先读取 `review.md` 转录文件（每篇论文目录都有）
2. 全面覆盖所有已读论文，不遗漏任何一篇
3. 对于重复主题的论文（如 Annals 2022 和 Regression 2025），
   明确说明后者对前者的推广关系
4. 独立检查文件内容的准确性

**防止措施**:
- 写综述笔记时，先 `ls review.md` 确认覆盖了所有论文
- 重写前先读取旧文件检查内容完整性
- 特别检查论文年份和 venue 标注的准确性

---

## L721: 综述文件编译技巧（standalone vs include）

**日期**: 2026-04-09
**经历次数**: 1 次 (累计)

**问题**: 章节文件（如 `tang-rong-review.tex`）只有 `\chapter{}`
没有 `\documentclass{}`，无法直接编译。

**正确做法（wrapper 方式）**:
```bash
# 在 compile.sh 中创建临时 wrapper 文件
cat > "$WRAPPER" << 'EOF'
\def\STANDALONE{}
\input{tang-rong-review.tex}
EOF
xelatex '\input{'"$WRAPPER"'}'
rm -f "$WRAPPER"
```
在 .tex 文件头部使用 `\ifdefined\STANDALONE` 条件包裹 preamble：
```latex
\ifdefined\STANDALONE
\documentclass[12pt]{amsbook}
\usepackage{...}
\begin{document}
\fi
\chapter{...}
...content...
\ifdefined\STANDALONE
\end{document}
\fi
```

**防止措施**:
- 写章节文件时就规划好 preamble（standalone 方式）
- 或者保持无 preamble，直接 include 到主文件编译

**最后更新**: 2026-05-10

---

## L725: Bayesian Ch9 写作教训：\mid vs | 条件记号是硬规则

**日期**: 2026-05-10
**来源**: Bayesian Chapter 9 (Decision Analysis) 主笔写作
**累计次数**: 1 次

**写作内容**:
- 决策分析章节，涵盖效用/损失函数、三种损失函数与最优估计、预验分析、层次决策与经验贝叶斯

**做得好的地方**:
1. **Stein 动机优先风格**：以"推断是描述性的，决策是规范性的"开场
2. **三种损失函数三定理结构**：清晰对照平方损失（后验均值）、绝对损失（后验中位数）、0-1 损失（后验众数）
3. **历史人物扩展**：Wald（极小极大）、Savage（主观期望效用公理化）、Raiffa/Schlaifer（实用化）各有具体贡献描述
4. **与前章的有机联系**：\S 9.1 末尾增加了"积分即决策"的洞察，连接 Ch3 的边际后验分布
5. **经验贝叶斯具体例子**：正态均值层次 shrinkage 公式配直观解释

**发现的问题（Reviewer Round 1 捕获）**:
1. **HIGH: `\mid` vs `|` 条件记号**：初稿中大量使用 `|` 作为条件记号（如 `p(\theta|y)`），reviewer 指出项目规范要求用 `\mid`（`p(\theta\mid y)`）。这是 writing-guide.md 中的硬规则。
2. **MEDIUM: Exercise label 语法**：`\begin{Exercise}{\ref{exr:ch9-1} 标题}` 将 `\ref{}` 放在了 title 参数内——应将 `\label{exr:ch9-1}` 放在 exercise body 内独立一行。
3. **MEDIUM: 损失矩阵权重**：`0.5` 作为裸数字不够清晰，应加 `0.5 \cdot L_{\text{conservative}}`。

**防止措施**:
- 写完初稿后，用 `grep -n '| y)\| | \theta)' chapter*.tex` 检查所有条件记号
- Exercise 环境：label 放 body 内，title 参数只含文字
- 矩阵元素中涉及权重的数值用 `\cdot` 或 `\times` 明确乘法关系

---

## L724: Chapter 21 (Instrumental Variable) 写作教训

**日期**: 2026-04-28
**来源**: ch21-writer 主笔 rewrite 因果推断 chapter21
**累计次数**: 1 次

**写作内容**:
- 工具变量（IV）章节，Part V 开篇
- 核心概念：CACE, LATE, 排除限制，单调性，ITT
- 弱工具变量问题与 FAR 置信集

**做得好的地方**:
1. **Stein 叙事风格**：从"无法假设可忽略性时怎么办"的问题出发，逐步引入 IV 思想
2. **Dorn 1953 引言**：使用"鼓励设计"视角，与书中原文一致
3. **四类依从者**：清晰解释 always taker, complier, defier, never taker
4. **三个核心假设**：随机性、单调性、排除限制，动机清晰
5. **CACE 识别定理**：定理 21.1 正确陈述，证明简洁
6. **弱 IV 问题**：指出比值估计量在 $\tau_D \approx 0$ 时的失效问题

**发现的问题**:
1. 最初用 `\begin{Lemma}` 包理论 21.1，应为 `\begin{Theorem}`
2. 最初用 `\itemize` 而非 `\enumerate` 列举例子
3. 需要添加 AngristImbensRubin:1996, ImbensAngrist:1994, Dorn:1953 引用

**防止措施**:
- 写完定理后检查环境名称是否与内容匹配
- 列举关键类型/步骤用 enumerate，不用 itemize
- 引用论文前检查 references.bib 是否存在对应条目

---

## L723: Chapter 29 书籍内容与任务描述不匹配

**日期**: 2026-04-26
**经历次数**: 1 次 (累计)

**错误描述**:
任务描述说 Chapter 29 涵盖"高维因果推断"和"LASSO在因果推断中的应用"，但书籍第29章实际内容是"Time-Varying Treatment and Confounding"（时间变动的处理变量与混淆）。

**书籍 Chapter 29 实际内容**:
1. 序列可忽略性（Sequential Ignorability）
2. g-公式与结果建模（g-formula）
3. 逆概率加权（IPW）
4. 边际结构模型（MSM）
5. 结构嵌套模型（SNM）

**高维/LASSO 内容实际位置**:
- LASSO 在第6章 rerandomization/regression adjustment 中首次提到
- 高维内容分散在第20章（overlap）和文献引用中
- Bloniarz et al. (2016), Wager et al. (2016) 等关于 LASSO 调整的论文出现在参考文献中

**正确做法**:
- 写作前必须读取 transcript 确认章节真实内容
- 不要假设任务描述与书籍内容一致
- 本章重点：高维动机只在 MSM/SNM 部分简短提及（LASSO 调整属于前沿文献，完整讨论超出本书范围）

---

## L722: Chapter 8 (Billey & Pipe Dreams) 审查教训

**日期**: 2026-04-23
**来源**: team-lead 委托的 chapter8.tex 审查任务
**累计次数**: 1 次

**审查结果**: B+（优秀，有小幅改进空间）

**做得好的地方**:
1. 历史脉络清晰：Billey 1999, Fomin-Kirillov 1994, Kostant 1963, Postnikov 2002 等引用准确
2. 动机过渡自然：开头指出"本章转向另一个核心主题"与第1章的 Graham positivity 形成对比
3. 有机联系充分：Section 8.5 明确梳理了与第1、3、4章的联系
4. 例子紧跟定理：Pipe Dream 定理后立即给出 $n=3, w=s_1s_2$ 的例子

**发现的问题**:

1. **Section 8.1.1 动机可以更强**
   - 现状：直接问"哪些 Schubert 簇是光滑的？"
   - 建议：先说明"即使 $X_w$ 整体奇异，我们能否在有理同伦意义下找到它的光滑代表？"再引出 Billey 发现

2. **Section 8.2 缺少"为什么需要 Kostant 多项式"的动机**
   - 现状：直接给出 Borel 同构 → 直接给 Kostant 多项式定义
   - 建议：先说明 Borel 同构没有给出 Schubert 类的显式公式，Kostant 多项式解决了这个问题

3. **轻微 overfull hbox 警告**（2-8pt，不影响理解）
   - 位置：lines 122-126, 162-166
   - 原因：`\text{Pipe Dream 1} & \text{Pipe Dream 2}` 表格造成
   - 处理：暂不修复，不影响阅读

4. **中文正文中 `\textbf` 使用不一致**
   - Line 160: `\textbf{bumpless pipe dream}` 建议改为 `\emph{bumpless pipe dream}` 或普通文本

**Stein 风格自检清单**:
- [x] 动机明确：每个概念引入前先解释"为什么需要它"
- [x] 历史脉络：注重概念的起源和发展历史
- [x] 有机联系：强调不同数学领域之间的相互关联
- [x] 叙事流畅：定义→命题→证明之间有连贯的叙述
- [x] 循序渐进：从简单到复杂，不过早引入技术细节
- [x] 连接前章：Section 8.5 明确梳理与第1、3、4章的联系

**防止措施**:
- 写完每个 Section 后，检查是否回答了"为什么需要这个概念"
- 检查是否在给出定义前先说明了现有工具的局限性
- 编译后检查 overfull hbox 警告
- 中文文本中谨慎使用 `\textbf`，优先用 `\emph` 或不加标记