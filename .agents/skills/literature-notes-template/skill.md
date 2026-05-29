# 文献库讲义生成 Skill

## 功能

为新的文献学习主题创建标准化的 LaTeX 讲义文件夹结构。

## 触发条件

- 用户要求创建新的文献笔记
- 用户要求新建主题讲义
- 用户要求建立文献库

## 工作流程

### Step 1: 创建目录结构

根据主题名称创建以下结构：
```
notes/<主题>/
├── <主题>-notes.tex      # 主文件
├── compile.sh            # 编译脚本
├── references.bib        # BibTeX 参考文献
├── chapters/
│   ├── chapter0.tex      # 文献概述
│   └── ...
└── appendix/
    └── qa.tex            # 问答记录
```

### Step 2: 生成主文件

创建 `<主题>-notes.tex`，必须包含：
- amsbook 或 article documentclass
- cleveref 宏包（用于 \cref）
- input chapters 和 appendix

### Step 3: 生成 compile.sh

```bash
#!/bin/bash
FILE="<主题>-notes"

for i in 1 2 3; do
    xelatex -interaction=nonstopmode "$FILE.tex" > /dev/null 2>&1
done

open -a Skim "$FILE.pdf"
```

### Step 4: 生成 chapter0

使用 `chapter0-template` skill 生成文献概述。

### Step 5: 生成 qa.tex

创建空的问答记录文件：
```latex
\chapter{问答记录}
\label{app:qa}

\section{问答记录}
\label{sec:qa}
```

## 命名规范（重要！）

- **主文件必须命名为 `<主题>-notes.tex`**，禁止使用 `main.tex`
- 主题名称使用连字符 `-` 连接，如 `schubert-positivity`、`information-geometry`
- 英文主题名

## 示例

用户说"创建信息几何的文献笔记"时：
1. 创建 `notes/information-geometry/`
2. 生成 `information-geometry-notes.tex`
3. 生成 `compile.sh`
4. 使用 chapter0-template 生成 `chapters/chapter0.tex`
5. 生成 `appendix/qa.tex`

## 注意事项

- 所有文献库讲义必须遵循 MEMORY.md 中的标准结构
- chapter0 的格式必须严格遵循模板
- 使用 \cref 而非硬编码数字引用
- 禁止在 Definition/Theorem 环境中使用 itemize

## LaTeX 格式严格性要求（重要！）

**在讲义笔记中，必须严格使用 LaTeX 格式，禁止任何 Markdown 格式！**

- ❌ 禁止使用 Markdown 列表（`-`、`1.`）
- ❌ 禁止使用 Markdown 加粗（`**text**`）
- ❌ 禁止使用 Markdown 斜体（`*text*`）
- ❌ 禁止使用 Markdown 代码块（```）

必须使用：
- ✅ `\begin{enumerate}...\end{enumerate}` 或 `\begin{itemize}...\end{itemize}`
- ✅ `\textbf{text}`
- ✅ `\textit{text}`
- ✅ `\begin{verbatim}...\end{verbatim}` 或 `\texttt{text}`
