# 写作专家教训记忆

**适用对象**: writing-expert, writing-expert-2, writing-expert-3
**最后更新**: 2026-03-30

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
**经历次数**: 1 次 (累计)

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
- ` '' ` → " (右双引号)
- ` `' ` → ' (左单引号)
- ` '' ` → ' (右单引号)

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
\begin{Proof}
这里是证明内容...
\end{Proof}
\end{Lemma}
```

**修复位置（Chapter 1）**:
- Lemma 2.2 (line ~1110): 已有 proof 环境
- Lemma 2.5 (line ~1139): 已有 proof 环境
- Corollary 2.4 (line ~1150): 已有 proof 环境
- Theorem 2.6: 缺失 `\end{Proof}` → 已修复
- Theorem 2.7: `\textbf{证明：}` → `\begin{Proof}...\end{Proof}` → 已修复
- Corollary 1.2: `\textbf{证明：}` → `\begin{Proof}...\end{Proof}` → 已修复

**防止措施**:
- 写 Lemma/Theorem 时直接用 `\begin{Proof}...\end{Proof}`
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
