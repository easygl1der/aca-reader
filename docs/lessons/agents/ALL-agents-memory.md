# 所有 Agent 通用教训记忆

**适用对象**: literature-experts 团队所有 agent
**最后更新**: 2026-03-31

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
| L012 | Team Lead 不应擅自派活 | 1 |
| L013 | Minor overfull hbox 不值得反复修复 | 1 |
| L014 | 图片/表格 overfull hbox 除非用户提示，否则不主动修复 | 1 |
| L015 | 引用文献时必须补充定理/定义/例子的具体内容 | 1 |
| L016 | 第一次出现的概念必须补充定义 | 1 |

---

## L015: 引用文献时必须补充定理/定义/例子的具体内容

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
当正文中引用了某个定理/定义/例子（如 `\cite{xxx}` 或直接引用某文献的 Theorem/Lemma），但没有给出该定理/定义/例子的具体内容时，读者需要翻书查找。

**正确做法**:
1. **查找源文件**：在 `PDFs/` 或 `PDFs/<topic>/transcript/` 目录下找到该文献的 PDF 或 markdown 转录文件
2. **提取内容**：从源文件中找到该定理/定义/例子的完整陈述
3. **添加到正文**：将内容以 footnote 或直接叙述的形式添加到引用位置
4. **引用原文**：在补充内容后加上 `\footnote{详见 \cite[ Theorem X.Y]{key}}`

**示例**：
```latex
% 原文本（只有引用，没有内容）
... 由 \cite[Lemma 2.3]{Mihalcea} 可知 ...

% 补充后
... 由 \cite[Lemma 2.3]{Mihalcea}\footnote{Lemma 2.3 (Mihalcea): [引理的完整陈述]。详见 \cite[ Lemma 2.3]{Mihalcea}。} 可知 ...
```

**常见缺口位置**：
- Chapter 4 中 Mihalcea §6 的 Lemma 6.4, Corollary 6.2, Eq. (1)(2)
- Chapter 4 中等变 Poincaré 对偶 (Lemma 2.3)
- Chapter 4 中投影公式 (Lemma 2.5, Anderson-Fulton)

**防止措施**:
- 每次引用文献时，检查是否有对应的完整陈述
- 如果只有引用没有内容，立即查找源文件补充

---

## L012: Team Lead 不应擅自派活

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
用户说"read schubert"（查看阅读进度），Team Lead 错误理解为了"继续学习下一文献"，擅自向 schubert-expert 下达新增 chapter5 的指令。

**正确做法**:
1. 用户问"read schubert" = 只是确认当前进度
2. 应先汇报 Chapter 0-4 完成状态，不主动派活
3. **先确认需求，再决定是否派活**

**防止措施**:
- 用户问状态 ≠ 用户给新任务
- 遇到模糊指令，先问清楚需求再行动
- Team Lead 的核心是协调，不是擅自决策

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

## L010: QA 记录时必须同步在正文中添加 footnote 引用

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
添加 QA 到 appendix/qa.tex 后，忘记在原文中对应的位置添加脚注引用。

**正确做法**:
1. 在 qa.tex 添加新章节 `\subsection{标题}\label{sec:qa-xxx}`
2. 在原文中对应位置添加脚注：`\footnote{问：...？见附录 \cref{sec:qa-xxx}。}`
3. 两者必须同步完成

**防止措施**:
- 添加 QA 时始终检查原文是否有对应脚注
- 建立 QA 问答对的双向链接意识

---

## L011: 知识画像集成（所有 Agent 必须遵守）

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**背景**:
用户提出需求：CodeEx 在回答科研问题时，应根据用户已有的知识水平决定语言层次和叙述方式。

**正确做法**:
Agent 开工检查流程：
1. 读取 `config/knowledge-profile.json`
2. 检查当前领域是否有记录
3. 如有 → 根据 level 调整回答深度
4. 如无且 strategy=lazy → 使用默认 level（beginner）
5. 交互后 → 更新 evidence 到 profile（如果 auto_update=true）

**Level 对应回答风格**：
- beginner: "让我从基础讲起..." 多用类比，定义所有术语
- acquainted: "你可能记得..." 简要回顾，逐步引入严格性
- familiar: 标准技术陈述
- proficient: "如你所知..." 可深入细节，处理复杂证明
- mastered: 前沿讨论，批判性分析

**防止措施**:
- 开工时先检查知识画像
- 交互中注意用户反馈，更新 evidence
- 详见 `docs/knowledge-profile.md`

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

---

## L013: Minor overfull hbox 不值得反复修复

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
latex-checker 报告 chapter4.tex 有 2 处 minor overfull hbox（6pt, 2pt），team-lead 在多方并发修改文件的情况下反复尝试手动修复，造成版本冲突和效率低下。

**正确做法**:
- < 10pt 的 minor overfull hbox 可以接受，不需要强制修复
- 团队协作中，多方并发修改文件时，应让流程走完而非追求完美细节
- 过度的微调浪费算力，应聚焦核心内容质量

**防止措施**:
- latex-checker 只报告 > 10pt 的严重 overfull hbox
- 10pt 以内属于可接受范围
- 团队 lead 应关注大局（内容质量），而非字间距微调

---

## L014: 图片/表格 overfull hbox 除非用户提示，否则不主动修复

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**经验描述**:
tikz 图片等导致的 overfull hbox 是排版正常现象，不需要主动修复。只有用户明确指出某处 overfull 需要修复时才处理。

**正确做法**:
- tikz 图片、表格等导致的 overfull hbox 不主动修复
- 等用户手动提醒再计入教训并修复
- latex-checker 应聚焦文字内容和 LaTeX 语法错误，不关注图片排版

**防止措施**:
- latex-checker 报告 overfull hbox 时注明"图片/表格原因"还是"文字原因"
- 用户未提示的图片 overfull 一律忽略

---

## L016: 第一次出现的概念必须补充定义

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
