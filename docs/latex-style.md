# LaTeX 格式规范

## 禁止使用
- ❌ Markdown 列表（`-`、`1.`）
- ❌ Markdown 加粗（`**text**`）
- ❌ Markdown 斜体（`*text*`）
- ❌ Markdown 代码块（```）

## 必须使用
- ✅ `\begin{enumerate}...\end{enumerate}` 或 `\begin{itemize}...\end{itemize}`
- ✅ `\textbf{text}`
- ✅ `\textit{text}`
- ✅ `\begin{verbatim}...\end{verbatim}` 或 `\texttt{text}`

## Theorem 环境
- **禁止在 Definition/Theorem 环境中使用 itemize**，使用 enumerate 替代
- 条件之间用分号分隔

## 脚注
- 使用 `\footnote{}` 添加说明

## Theorem Style
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

## 习题环境
```latex
\newtheorem{Exercise}{练习}[chapter]

\begin{Exercise}{题目描述}
题目内容...
\end{Exercise}
```

## 文档模板

### 使用 amsbook
```latex
\documentclass[12pt]{amsbook}
\usepackage{xeCJK}
```

### xeCJK 字体配置
**先查看电脑上可用的字体：**
```bash
fc-list :lang zh
fc-list | grep -i "serif" | head -20
```

**常用配置：**
```latex
\setCJKmainfont{Noto Serif SC}
\setCJKsansfont{Noto Sans SC}
```
