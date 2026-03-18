# 目录结构与工作流

## 目录结构

### 每个主题的笔记文件夹
```
notes/<主题>/
├── <主题>-notes.tex      # 主文件（命名：<主题>-notes.tex，禁止 main.tex）
├── compile.sh            # 编译脚本
├── progress.json         # 阅读进度
├── chapters/
│   ├── chapter0.tex      # 文献概述（必须）
│   ├── chapter1.tex      # 第1章
│   └── ...
└── appendix/
    └── qa.tex           # 问答记录（必须）
```

### 多 Part 书籍结构（如 Do Carmo）
```
notes/differential-geometry/
├── differential-geometry-notes.tex    # 主入口
├── compile.sh
└── do-carmo-curves-surfaces/          # Part I
    ├── do-carmo-curves-surfaces-notes.tex
    └── chapters/chapter1.tex
```

### compile.sh 脚本规范
```bash
#!/bin/bash
FILE="causal-inference-notes"

for i in 1 2 3; do
    xelatex -interaction=nonstopmode "$FILE.tex" > /dev/null 2>&1
done

open -a Skim "$FILE.pdf"
```

---

## chapter0 文献概述格式

### 章节格式
```latex
\chapter*{引言：文献概述}\label{chap:introduction}
\addcontentsline{toc}{chapter}{引言：文献概述}
```

### 内容结构（按顺序）
1. **总述** - 介绍学习该主题的背景、意义和研究动机
2. **文献摘要总结** - 每篇论文的详细信息
3. **补充参考资料** - 其他相关书籍、论文
4. **学习路径与前置基础知识** - 需要的基础知识
5. **最终目标** - 学习期望达到的目标

### 每篇论文的格式
```latex
\subsection{论文标题}
\begin{enumerate}
    \item \textbf{作者:} 作者姓名
    \item \textbf{链接:} \url{arxiv.org/abs/...} 或 DOI
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

### 查找论文链接
1. 先搜索 arXiv：`site:arxiv.org 论文标题`
2. **优先使用 arXiv 链接**（如果有的话）
3. 如无 arXiv，使用 DOI 或 Google Scholar 链接
4. 注意：1998年以前的论文通常没有 arXiv 版本

---

## 用户注解命令

```latex
\newcommand{\userannotation}[2]{%
  \begin{Remark}
    \textbf{#1:} #2
  \end{Remark}
}
```

使用方式：
```latex
\userannotation{问题}{这是用户提问的内容}
\userannotation{思考}{这是用户的思考记录}
```

---

## 工作流

### 1. 阅读流程
1. 扫描阶段：解析 PDF，提取章节结构
2. 逐章阅读：用户选择章节，深入学习
3. 交互问答：用户提问，实时解答

### 2. 讲义生成
- 使用 Stein 写作风格：动机驱动、与已有知识关联
- 每章独立 .tex 文件，主文件用 `\include` 整合

### 3. 问答机制（每次用户提问后执行）
1. 用口语化方式回答用户
2. 添加用户注解到 LaTeX 讲义（\userannotation）
3. 记录问题到 progress.json
4. 重新编译 PDF
