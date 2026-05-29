# 阶段 3：AI 大纲生成

## 目的

基于精读笔记，生成章节骨架（~30% 填充度），为后续初稿写作提供结构框架。

## 输入

- `close-reading-notes.md`（阶段 1+2 输出）
- 目标章节编号和主题

## 输出

`chapter-outline.tex` — 包含：
- 章节标题和引言
- 各节标题和段落骨架
- 预分配的 label
- 附录标记

## 执行步骤

### Step 1：分析章节结构

根据精读笔记，分析章节的逻辑结构：

```
核心问题 → 引入概念 → 核心定理 → 应用/例子 → 小结
```

### Step 2：设计章节骨架

遵循 **Stein 动机优先风格**：

#### 引言（Introduction）
- **动机段落**（1-2 段）：为什么需要这个章节？解决什么问题？
- **历史脉络**（可选）：重要人物和贡献
- **本章结构**（最后一段）：概览各节内容

#### Section 5.1: [名称]

**动机引入**（2-3 句）：
```
[动机] 在进入正题之前，我们需要理解...
这引导我们提出一个核心问题：...
```

**定义框架**：
```latex
\section{[节标题]}\label{sec:5-1}

在前几章中，我们学习了...然而，这引出了一个根本性的困难...
```

#### Section 5.2: [核心内容]

**定理框架**（带编号 label）：
```latex
\subsection{[小节标题]}\label{sec:5-2}

\textbf{核心问题}：...

\begin{Theorem}[5.1]\label.thm:5-1}
% 定理内容骨架（完整条件-结论）
\end{Theorem}
```

**证明策略**（不写完整证明）：
```
证明思路：首先...，然后...，最后...
完整证明见附录 \cref{sec:appendix-5-2-proof}。
```

#### Section 5.3: [应用/例子]

```latex
\begin{Example}[称重例子]\label{ex:5-3}
% 例子背景和设定
% 计算框架
\end{Example}
```

### Step 3：预分配 Label

为所有即将使用的内容预分配 label：

| 类型 | 格式 | 示例 |
|------|------|------|
| 方程 | `eq:{描述}` | `eq:balance-CRE` |
| 定理 | `thm:{章节}-{编号}` | `thm:5-1` |
| 定义 | `def:{章节}-{编号}` | `def:5-1` |
| 示例 | `ex:{章节}-{编号}` | `ex:5-1` |
| 章节 | `sec:{章节}-{名称}` | `sec:5-1-intro` |
| 附录证明 | `sec:appendix-{内容}` | `sec:appendix-5-2-proof` |

### Step 4：标记附录内容

```latex
% 在正文中用脚注标记
...的核心结论由下式给出%
\addtocounter{footnote}{1}\addtextsuperscript{\thefootnote}{\arabic{footnote}}
现证明如下...%
\end{Proof}
\stepcounter{footnote}%
```

更简单的方式：在证明结尾标注
```latex
\begin{Proof}
证明内容...
\end{Proof}
\par\_notes{完整证明见附录 \cref{sec:appendix-5-2-proof}。}
```

### Step 5：生成 LaTeX 骨架

输出 `chapter-outline.tex`：

```latex
% !TEX root = ../[topic]-notes.tex

\chapter{章节标题}\label{ch:5}

\section{引言}\label{sec:5-intro}

% 动机背景
[~30% 填充：动机段落、历史脉络]

\section{第一节标题}\label{sec:5-1}

\subsection{小节标题}\label{sec:5-1-1}

% 定义框架
\begin{Definition}[5.1]\label{def:5-1}
定义内容骨架...
\end{Definition}

\section{第二节标题}\label{sec:5-2}

\subsection{核心定理}\label{sec:5-2-1}

\begin{Theorem}[5.1]\label/thm:5-1}
定理内容骨架（条件-结论）...
\end{Theorem}

% 证明框架
\begin{Proof}
证明思路：首先...，然后...，最后...
\ done
\par\_notes{完整证明见附录 \cref{sec:appendix-5-2-proof}。}
\end{Proof}

\section{第三节标题}\label{sec:5-3}

\begin{Example}[5.1]\label{ex:5-1}
例子设定和计算框架...
\end{Example}

\section{小结}\label{sec:5-summary}

% 总结段落

% 附录标记
\par\_notes{主要定理的完整证明见附录 \crefrange{sec:appendix-5-2}{sec:appendix-5-3}。}
```

## 填充度控制

| 部分 | 填充度 | 说明 |
|------|--------|------|
| 引言动机 | 40% | 完整的动机叙述，但可简化历史细节 |
| 定义骨架 | 30% | 完整定义结构，定义内容可简化 |
| 定理骨架 | 50% | 完整条件-结论，证明留空或简略 |
| 例子骨架 | 30% | 例子结构完整，计算过程可简化 |
| 小结 | 40% | 总结要点完整，细节可省略 |

## Label 命名规范

遵循 `docs/label-reference.md`：

```latex
% 章节级别
\label{ch:{chapter}}           % 章节
\label{sec:{chapter}-{name}}   % 小节

% 内容级别
\label{def:{chapter}-{num}}     % 定义
\label/thm:{chapter}-{num}}    % 定理
\label{prop:{chapter}-{num}}    % 命题
\label{cor:{chapter}-{num}}     % 推论
\label{ex:{chapter}-{num}}      % 示例
\label{eq:{descriptive-name}}   % 方程
\label{lim:{descriptive-name}} % 极限定理

% 附录级别
\label{sec:appendix-{topic}}   % 附录章节
```

## 验证

完成大纲后，确认：
- [ ] 引言包含完整动机
- [ ] 所有 section 有标题和 label
- [ ] 所有定理/定义/示例有编号和 label
- [ ] 附录内容已标记
- [ ] Label 命名符合规范
- [ ] 文件可直接编译（无缺失引用）

## 下一步

输出传递给 **阶段 4：AI 初稿 V1**
