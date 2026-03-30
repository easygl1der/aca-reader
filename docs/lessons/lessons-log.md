
## 2026-03-31: bash heredoc 导致 LaTeX 命令损坏

**问题**：使用 `echo '...' >> file.tex` 或 heredoc 追加内容时，反斜杠 `\`，导致 `\textbf`、`\begin{itemize}` 等 LaTeX 命令被损坏（变成 `extbf`、`egin{itemize}`）。

**原因**：bash heredoc/echo 默认不处理反斜杠转义字符。

**解决方案**：
1. 使用 Python 写入文件，避免 bash 转义问题
2. 或在 heredoc 中使用单引号并确保内容不包含会转义的字符

**教训**：追加 LaTeX 内容到 .tex 文件时，优先使用 Python 而非 bash heredoc/echo。
