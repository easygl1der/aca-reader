# LaTeX 检查专家教训记忆

**适用对象**: latex-checker
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L901 | Markdown 残留检查 | 2 |
| L902 | \bm 命令禁用检查 | 1 |
| L903 | Label/Ref 一致性检查 | 1 |
| L904 | Theorem 环境禁止 itemize | 1 |
| L905 | theorem 环境 \\begin/\\end 格式检查 | 1 |

---

## L905: theorem 环境 \begin/\end 格式检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
subagent 生成的 chapter5.tex 中，theorem 环境写成了 `\begin theorem}` 和 `\end theorem}` —— 中间有空格或缺少 `{`/`}`。

**正确做法**:
```latex
% 错误 ❌
\begin theorem}[...]
\end theorem}

% 正确 ✅
\begin theorem}[...]
\end theorem}
```

检查命令:
```bash
grep -n "begin theorem\|end theorem" notes/**/*.tex
# 或检查空格
grep -n "\\\\end theorem\}" notes/**/*.tex
```

**修复方法**:
```python
# Python 修复脚本
content = content.replace('\\{', '{')
content = content.replace('\\}', '}')
```

**防止措施**:
- 每次生成后立即检查 theorem 环境闭合: Markdown 残留检查

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
在 .tex 文件中发现了 Markdown 格式残留。

**检查命令**:
```bash
# 检查 Markdown 残留
grep -E '\*\*|\* -|^\>' notes/**/*.tex
# 或者
grep -n '\textbf{\underline{' notes/**/*.tex
```

**常见残留模式**:
```latex
% 加粗残留
**text**  →  \textbf{text}

% 斜体残留
*text*  →  \textit{text}

% 列表残留
- item  →  \item（需要 enumerate 环境）

% Callout 残留
> [!note]  →  \begin{note}...\end{note}
```

**防止措施**:
- 润色后立即检查
- 用脚本批量检测残留

---

## L902: \bm 命令禁用检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
使用了禁止的 `\bm{}` 命令。

**正确做法**:
```latex
% 错误 ❌
\bm{x}, \bm{\beta}, \bm{A}

% 正确 ✅
\mathbf{x}  % 向量
\boldsymbol{\beta}  % 矩阵
```

**检查命令**:
```bash
grep -n '\\\\bm{' notes/**/*.tex
```

**防止措施**:
- 记住：`\bm` 是禁止的
- 提示用户修正

---

## L903: Label/Ref 一致性检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
存在 `\ref{}` 或 `\cref{}` 引用了不存在的 label。

**检查方法**:
1. 提取所有 `\label{...}`
2. 提取所有 `\ref{...}` 和 `\cref{...}`
3. 核对引用是否有对应定义

**常见错误**:
```latex
% label 定义了但没用
\label{eq:balance-discrete-CRE}  % 定义了

% 引用时拼写错误
\eqref{eq:balance-discrete-CER}  % 拼写错误！

% ref 类型错误
\ref{fig:xxx}  % 应该是 \cref{fig:xxx}
```

**防止措施**:
- 编译检查警告
- 用脚本验证 label-ref 一致性

---

## L904: Theorem 环境禁止 itemize

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
在 Theorem/Definition 环境内使用了 itemize 列表。

**正确做法**:
```latex
% 错误 ❌
\begin{Theorem}
\begin{itemize}
\item 第一点
\item 第二点
\end{itemize}
\end{Theorem}

% 正确 ✅
\begin{Theorem}
条件如下：
\begin{enumerate}
\item 第一点
\item 第二点
\end{enumerate}
\end{Theorem}
```

**或者用纯叙述**:
```latex
\begin{Theorem}
If $X$ is normally distributed with mean $\mu$ and variance $\sigma^2$,
then the sample mean $\bar{X}$ satisfies......
\end{Theorem}
```

**防止措施**:
- Theorem 内用自然段落叙述
- 如需列表，用 enumerate 环境

---

## 核心检查清单

- [ ] 无 Markdown 残留（`**`、`*`、`-`、`>`）
- [ ] 无 `\bm{}` 命令
- [ ] 所有 `\ref{}`/`\cref{}` 都有对应 `\label{}`
- [ ] Theorem 环境内无 itemize
- [ ] 推导都在附录，正文有 `\footnote{}` 引用
- [ ] 符号约定一致

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/latex-checker-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是 LaTeX 检查专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
