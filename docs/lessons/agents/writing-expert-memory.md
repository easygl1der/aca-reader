# 写作专家教训记忆

**适用对象**: writing-expert, writing-expert-2, writing-expert-3
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L701 | Stein 风格核心要素 | 2 |
| L702 | 推导→附录格式 | 3 |
| L703 | 禁止 Markdown 残留 | 2 |
| L704 | 例子必须引用对应定理 | 1 |

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
