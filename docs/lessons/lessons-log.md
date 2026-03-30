
## 2026-03-31: bash heredoc 导致 LaTeX 命令损坏

**问题**：使用 `echo '...' >> file.tex` 或 heredoc 追加内容时，反斜杠 `\`，导致 `\textbf`、`\begin{itemize}` 等 LaTeX 命令被损坏（变成 `extbf`、`egin{itemize}`）。

**原因**：bash heredoc/echo 默认不处理反斜杠转义字符。

**解决方案**：
1. 使用 Python 写入文件，避免 bash 转义问题
2. 或在 heredoc 中使用单引号并确保内容不包含会转义的字符

**教训**：追加 LaTeX 内容到 .tex 文件时，优先使用 Python 而非 bash heredoc/echo。


## 2026-03-31: 添加附录解释后必须在正文中加 footnote 引用

**问题**：在 appendix 添加了解释，但漏了正文中某处的 footnote 引用。

**检查清单**：每次在 qa.tex 添加新内容后，必须检查：
1. 正文是否有多处提到这个概念？
2. 每处是否都已添加 footnote 引用？

**本次教训**：Gromov-Witten 不变量在正文第 15 行和第 237 行都出现了，我只给第 15 行加了 footnote，漏了第 237 行。

**正确流程**：
1. 在 appendix 添加解释
2. grep 正文中所有提到该概念的位置
3. 每个位置都要添加 ootnote{问：xxx？见附录 \cref{sec:xxx}。}
