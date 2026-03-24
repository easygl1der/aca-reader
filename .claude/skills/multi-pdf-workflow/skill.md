# 多文献学习工作流

## 概述

管理多篇相关文献的学习笔记，生成统一的 LaTeX 讲义。

## 功能

1. 扫描多篇 PDF 文献，提取结构和内容
2. 生成文献概述（Chapter 0）
3. 为每篇文献创建独立章节
4. 统一编译和版本管理

## 使用方式

### 初始化新主题

```bash
# 创建笔记目录结构
notes/
└── <主题名称>/
    ├── <主题>-notes.tex      # 主文件
    ├── compile.sh           # 编译脚本
    ├── chapters/
    │   ├── chapter0.tex      # 文献概述
    │   └── chapter1.tex      # 第1篇文献
    └── appendix/
        └── qa.tex            # 问答记录
```

### 添加新文献

1. 解析 PDF 内容
2. 创建新的 chapter 文件
3. 更新 main.tex

### 编译

```bash
cd notes/<主题>/
./compile.sh
```

## 模板

### compile.sh

```bash
#!/bin/bash
FILE="<主题>-notes"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译完成 ==="
ls -la ${FILE}.pdf
```

### 主文件 (amsbook)

```latex
\documentclass[12pt]{amsbook}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{xeCJK}
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{geometry}
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

% User annotation
\newcommand{\userannotation}[2]{%
  \begin{Remark}
    \textbf{#1:} #2
  \end{Remark}
}

\title{<主题>学习笔记}
\author{<作者>}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\input{chapters/chapter0}  % 文献概述
\input{chapters/chapter1}  % 第1篇文献
% 继续其他章节...

\appendix
\input{appendix/qa}

\end{document}
```

### Chapter 0 模板（文献概述）

```latex
\chapter*{引言：文献概述}
\addcontentsline{toc}{chapter}{引言：文献概述}
\label{chap:Intro}

\section{主题背景}

介绍本主题的背景和研究意义。

\section{文献总览}

\subsection{1. <文献1标题>}
\textbf{作者}: <作者> (<年份>) \\
\textbf{arXiv}: <编号> \\
\textbf{主要贡献}:
\begin{itemize}
\item 贡献1
\item 贡献2
\end{itemize}

\section{学习路径}

建议的学习顺序。

\section{最终目标}

学习本系列文献的最终目标。
```

## 工作流程

1. **收集文献**：将 PDF 放入 `PDFs/<主题>/` 目录
2. **解析文献**：使用 pdf-reader skill 解析每篇文献
3. **创建结构**：初始化笔记目录结构
4. **添加概述**：创建 chapter0 介绍所有文献
5. **逐篇学习**：为每篇文献创建章节并深入学习
6. **编译发布**：使用 compile.sh 编译生成 PDF
