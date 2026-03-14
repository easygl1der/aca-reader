---
name: latex-notes
description: 生成 LaTeX 格式的学习讲义，包含用户注解、问题、Stein 风格的 motivation 写作
user-invocable: true
---

# LaTeX 讲义生成 Skill

## 功能

1. 根据阅读进度生成对应章节的 .tex 文件
2. 在定义/命题/证明之间插入用户注解
3. 记录问答内容到附录
4. 生成 main.tex 整合所有章节
5. 交叉引用支持

## 使用方式

- "帮我更新第3章第2节的讲义"
- "把这个问题和解答加到讲义里"
- "生成 main.tex"

## 讲义风格

参考 Stein 的写作风格：
- 动机驱动：先解释为什么需要这个概念
- 与已有知识关联
- 清晰的叙事流程
- 不是干巴巴的定义定理证明，而是有"为什么"的解释

## 文件结构

```
notes/
├── main.tex              % 主文件
├── chapters/
│   ├── chapter1.tex
│   ├── chapter2.tex
│   └── chapter3.tex
└── appendix/
    └── qa.tex
```

## LaTeX 格式规范（必须遵守）

### main.tex 必要包

```latex
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}           % 图片
\usepackage{hyperref}           % 超链接
\usepackage{geometry}           % 页面布局

% Theorem 环境定义（使用 amsthm）
\theoremstyle{plain}
\newtheorem{Definition}{定义}[chapter]
\newtheorem{Theorem}[Definition]{定理}
\newtheorem{Lemma}[Definition]{引理}
\newtheorem{Corollary}[Definition]{推论}
\newtheorem{Proposition}[Definition]{命题}
\newtheorem{Example}{例}[chapter]
\newtheorem{Remark}{注}[chapter]
```

### 定义/定理环境使用规则

**【重要】禁止在 Definition/Theorem 环境中使用 itemize！**

错误示例：
```latex
\begin{Definition}
\begin{itemize}
  \item 条件1
  \item 条件2
\end{itemize}
\end{Definition}
```

正确示例（使用 enumerate 或 description）：
```latex
\begin{Definition}[完全随机实验]
设有 $n$ 个样本，其中 $n_1$ 个被分配到治疗组。完全随机实验满足以下条件：
\begin{enumerate}
  \item 每个个体被分配到治疗组的概率为 $n_1/n$；
  \item 治疗组总人数固定为 $n_1$；
  \item 个体之间相互独立。
\end{enumerate}
\end{Definition}
```

或者使用 description：
```latex
\begin{Definition}
完全随机实验（Completely Randomized Experiment）满足：
\begin{description}
  \item[概率] 每个个体被分配到治疗组的概率为 $n_1/n$；
  \item[人数] 治疗组总人数固定为 $n_1$；
  \item[独立性] 个体之间相互独立。
\end{description}
\end{Definition}
```

### 图片使用

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/chapter3/example.pdf}
  \caption{图示说明}
  \label{fig:example}
\end{figure}
```

### 用户注解格式

使用自定义命令：

```latex
\newcommand{\userannotation}[2]{%
  \begin{trivlist}
    \item[\textbf{用户注解:}] #1
    \textit{#2}
  \end{trivlist}
}

% 使用方式
\userannotation{为什么需要学生化统计量？}{当治疗组和对照组的方差差异较大时...}
```

## 用户注解格式

在定理/定义/证明之间插入：

% === 用户注解 ===
% 问题：为什么需要引入这个概念？
% 解答：...
% 关联：与第2章的XX定理有关联
% ===

或者使用 \userannotation 命令。
