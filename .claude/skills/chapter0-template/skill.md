# Chapter 0 模板 Skill

## 功能

为文献学习笔记生成 Chapter 0（文献概述），包含主题介绍和文献摘要总结。

## 触发条件

- 用户要求创建 chapter0
- 用户要求写文献概述
- 新建主题笔记时

## 格式要求（严格遵循！）

### 1. 章节格式

使用 `\chapter*{}` 配合 `\addcontentsline`：
```latex
\chapter*{引言：文献概述}\label{chap:introduction}
\addcontentsline{toc}{chapter}{引言：文献概述}
```

### 2. 内容结构（必须按顺序）

**第一部分：总述**
```latex
\section{总述}
介绍学习该主题的背景、意义和研究动机。
```

**第二部分：文献摘要总结**
```latex
\section{文献摘要总结}\label{sec:literature-summary}
\subsection{论文1标题}
\begin{enumerate}
    \item \textbf{作者:} 作者姓名
    \item \textbf{arXiv:} \url{https://arxiv.org/abs/xxxx.xxxxx}
    \item \textbf{年份:} 20XX
    \item \textbf{篇幅:} XX页
    \item \textbf{核心贡献:}
        \begin{itemize}
            \item 贡献点1
            \item 贡献点2
        \end{itemize}
    \item \textbf{摘要:} 摘要内容...
    \item \textbf{关键词:} 关键词1；关键词2；关键词3
\end{enumerate}
```

**第三部分：补充参考资料**
```latex
\section{补充参考资料}
列出其他相关的书籍、论文或学习资源。
```

**第四部分：学习路径与前置基础知识**
```latex
\section{学习路径与前置基础知识}
列出学习该主题需要的基础知识。
```

**第五部分：最终目标**
```latex
\section{最终目标}
说明学习完这些文献后期望达到的目标。
```

### 3. 论文格式（必须包含所有字段）

每篇论文必须包含以下字段（按顺序）：
- 作者
- 链接（优先 arXiv，如无则用 Google Scholar，使用 `\url{}`）
- 年份
- 篇幅（页数）
- 核心贡献（itemize 列表）
- 摘要
- 关键词（分号分隔）

**查找链接方法：**
1. 先搜索 arXiv 链接：`site:arxiv.org 论文标题`
2. 如无 arXiv，使用 `gs-search` skill 搜索 Google Scholar 获取链接
3. 使用 WebSearch 工具作为备选

**gs-search 使用方法：**
```bash
# 安装后，在需要时调用 skill
/skill gs-search 论文标题
```

## 使用方式

1. 用户说"创建 chapter0"或"写文献概述"
2. 根据 PDF 文件确定主题
3. 使用此模板生成 chapter0.tex

## 示例输出

```latex
\chapter*{引言：文献概述}\label{chap:introduction}
\addcontentsline{toc}{chapter}{引言：文献概述}

本学习资料旨在研究...

\section{总述}

介绍学习该主题的背景...

\section{文献摘要总结}\label{sec:literature-summary}

\subsection{论文标题}
\begin{enumerate}
    \item \textbf{作者:} 作者姓名
    \item \textbf{链接:} \url{https://arxiv.org/abs/xxxx.xxxxx} 或 \url{https://scholar.google.com/...}
    \item \textbf{年份:} 20XX
    \item \textbf{篇幅:} XX页
    \item \textbf{核心贡献:}
        \begin{itemize}
            \item 建立了...
            \item 证明了...
        \end{itemize}
    \item \textbf{摘要:} 本文研究了...
    \item \textbf{关键词:} 关键词1；关键词2；关键词3
\end{enumerate}

\section{补充参考资料}

\section{学习路径与前置基础知识}

\section{最终目标}
```

## 注意事项

- 使用 `\addcontentsline{toc}{chapter}{引言：文献概述}` 添加到目录
- 论文使用 `enumerate` 列出各项信息
- 核心贡献使用 `itemize` 列表
- arXiv 链接必须使用 `\url{}` 命令
- 关键词之间用分号（；）分隔
- 严格按照上述字段顺序
- **禁止使用 Markdown 格式！必须用 LaTeX enumerate/itemize**
