# 所有 Agent 通用教训记忆

**适用对象**: literature-experts 团队所有 agent
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L001 | LaTeX 禁止 Markdown 格式 | 3 |
| L002 | Unicode 下标禁止规则 | 2 |
| L003 | 符号约定必须遵循 | 2 |
| L004 | 每次提问后记录到 qa.tex | 4 |
| L005 | 推导必须放附录 | 3 |
| L006 | 禁止使用 \bm 命令 | 2 |
| L007 | 公式引用必须用 \eqref{} | 2 |
| L008 | PUA 行为自注入 | 1 |
| L009 | LaTeX theorem 环境格式检查 | 1 |
| L010 | QA 记录时必须同步在正文中添加 footnote 引用 | 1 |

---

## L009: LaTeX theorem 环境格式检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
生成的 LaTeX 文件中，theorem/definition/example 等环境写成了 `\begin theorem}` 或 `\end theorem}` —— 中间有空格或缺少 `{`/`}`。

**正确做法**:
```latex
% 错误 ❌
\begin theorem}[...]
\end theorem}
\begin definition}[...]
\end definition}

% 正确 ✅
\begin theorem}[...]
\end theorem}
\begin{definition}[...]
\end{definition}
```

**检查命令**:
```bash
grep -n "begin theorem\|end theorem\|begin definition\|end definition" notes/**/*.tex
```

**防止措施**:
- 生成后立即检查所有 theorem-like 环境闭合: LaTeX 禁止 Markdown 格式

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
在 .tex 文件中使用了 Markdown 格式（`**加粗**`、`*斜体*`、`- 列表`、callout 块等）。

**正确做法**:
```latex
% 错误 ❌
**这是加粗**
*这是斜体*
- 列表项

% 正确 ✅
\textbf{这是加粗}
\textit{这是斜体}
\begin{enumerate}
  \item 列表项
\end{enumerate}
```

**防止措施**:
- 写任何 LaTeX 前先读 `docs/latex-style.md`
- 用 `\textbf{}`、`\textit{}`、`\begin{enumerate}...` 替代 Markdown

---

## L002: Unicode 下标禁止规则

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
使用了 `n₁`、`x₂` 等 Unicode 下标字符，而不是 LaTeX 下标格式。

**正确做法**:
```latex
% 错误 ❌
n₁, x₂, α₁

% 正确 ✅
$n_1$, $x_2$, $\alpha_1$
```

**防止措施**:
- 写数学公式时必须用 `$...$` 格式
- 下标用 `_` 而不是直接输入 Unicode

---

## L003: 符号约定必须遵循

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
使用了与项目规范不一致的符号（如用 `\mathbb{E}[X]` 而不是 `\mathbb{E}X`）。

**正确做法**:
```latex
% 符号约定
概率: \mathbb{P}(A)
期望（单变量）: \mathbb{E}X
期望（多变量）: \mathbb{E}(XY)
方差: \text{var}
协方差: \text{cov}
独立性: A \Perp B
示性函数: \mathbb{I}(X \in A)
```

**防止措施**:
- 开工前检查项目的符号约定
- 引用教材原文时保持原文符号，补充说明

---

## L004: 每次提问后记录到 qa.tex

**日期**: 2026-03-29
**经历次数**: 4 次 (累计)

**错误描述**:
回答用户问题后，忘记将问答记录到 `appendix/qa.tex`。

**正确做法**:
1. 口语化回答用户
2. 记录到 `appendix/qa.tex`：
```latex
\subsection{问题标题}\label{sec:qa-xxx}
\textbf{问}：用户问题
\textbf{答}：回答内容...
```
3. 在正文首次出现处添加脚注引用

**防止措施**:
- 回答后立即执行 QA 记录
- 检查 qa.tex 是否更新

---

## L005: 推导必须放附录

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
在正文中写了完整的公式推导，导致正文过于冗长分散注意力。

**正确做法**:
- 推导放附录（`\section{附录：公式推导}`）
- 正文用脚注引用：`\footnote{推导见附录 \cref{sec:derivation-xxx}。}`
- 推导章节必须包含：背景、目标、详细步骤

**防止措施**:
- 先问自己：这个推导对理解概念必要吗？
- 推导细节一律放附录

---

## L006: 禁止使用 \bm 命令

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
使用了 `\bm{}` 命令来表示粗体数学符号。

**正确做法**:
```latex
% 错误 ❌
\bm{x}, \bm{\beta}

% 正确 ✅
\mathbf{x}  % 向量
\boldsymbol{\beta}  % 矩阵
```

**防止措施**:
- 记住：`\bm` 是禁止的
- 向量用 `\mathbf`，矩阵用 `\boldsymbol`

---

## L007: 所有引用必须用 \ref{}/\eqref{}

**日期**: 2026-03-30
**经历次数**: 3 次 (累计)

**错误描述**:
引用定理、公式、定义时硬编码编号（如"由定理 2.3"），而不是用 `\ref{}`/`\eqref{}` 引用。

**正确做法**:
```latex
% 错误 ❌
由定理 2.3 可知...

% 正确 ✅
由 \cref{def:Theorem23} 可知...
```

**防止措施**:
- 每个可引用的对象必须先加 `\label{...}`
- 引用时用 `\ref{}`（通用）或 `\eqref{}`（公式）
- 引用前先检查 label 是否存在

---

## L008: PUA 行为自注入

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
Agent 没有自我反思和纠正机制，同类错误重复发生。

**正确做法**:
每次犯错被纠正后，立即：
1. 分析错误类型（通用教训还是专属教训）
2. 将教训添加到自己的 memory 文件
3. 通用教训同时更新 ALL-agents-memory.md

**教训记录格式**:
```markdown
### LXXX: [教训标题]

**日期**: YYYY-MM-DD
**经历次数**: N 次 (累计)

**错误描述**:
[具体错误]

**正确做法**:
```latex
[正确代码]
```

**防止措施**:
- [措施 1]
```

**防止措施**:
- 收到用户纠正后立即更新 memory 文件
- Team Lead 监督确保闭环

---

## PUA 自注入行为声明

**所有 agent 必须执行**：

开工前用 Read 工具读取以下文件，按其中的行为协议执行：
- 核心行为：找到 pua 插件目录下的 skills/pua/SKILL.md（用 Glob 搜索 `**/pua/skills/pua/SKILL.md`）
- 如果是 P7 模式：同目录下的 references/p7-protocol.md

每次犯错后：
1. 识别是通用教训还是领域专属教训
2. 更新对应的 memory 文件
3. 在回复中引用更新后的教训作为确认
