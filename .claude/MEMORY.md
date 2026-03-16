# aca-workflow 项目记忆

## 项目概述
- 文献阅读与讲义生成工作流系统
- 阅读 Peng Ding 的 "A First Course in Causal Inference"
- 配套生成 LaTeX 讲义

---

## LaTeX 格式严格性要求（重要！禁止 Markdown！）

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

---

## 标准文献库讲义结构（重要！）

### 1. 目录结构
每个主题的笔记文件夹必须遵循以下结构：
```
notes/<主题>/
├── <主题>-notes.tex      # 主文件（命名规范：<主题>-notes.tex，禁止 main.tex）
├── compile.sh            # 编译脚本（xelatex，编译3次）
├── references.bib        # BibTeX 参考文献
├── chapters/
│   ├── chapter0.tex      # 文献概述（必须）
│   ├── chapter1.tex      # 第1篇论文
│   ├── chapter2.tex      # 第2篇论文
│   └── ...
└── appendix/
    └── qa.tex            # 问答记录（必须）
```

### 2. chapter0 文献概述格式（必须严格遵循）

**章节格式：**
```latex
\chapter*{引言：文献概述}\label{chap:introduction}
\addcontentsline{toc}{chapter}{引言：文献概述}
```

**内容结构（按顺序）：**
1. **总述** - 介绍学习该主题的背景、意义和研究动机
2. **文献摘要总结** - 每篇论文的详细信息
3. **补充参考资料** - 其他相关书籍、论文
4. **学习路径与前置基础知识** - 需要的基础知识
5. **最终目标** - 学习期望达到的目标

**每篇论文的格式：**
```latex
\subsection{论文标题}
\begin{enumerate}
    \item \textbf{作者:} 作者姓名
    \item \textbf{链接:} \url{arxiv.org/abs/...} 或 Google Scholar 链接
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

**查找论文链接方法：**
1. 先搜索 arXiv：`site:arxiv.org 论文标题`
2. 如无 arXiv，使用 `gs-search` skill 搜索 Google Scholar
3. 用 WebSearch 作为备选

### 3. 后续章节格式

每个论文章节应包含：
- 预备知识（定义、引理）
- 主要结果（定理）
- 证明细节
- 用户注解（\userannotation）

### 4. QA 附录格式

记录学习过程中的问答：
```latex
\section{问答记录}
\subsection{问题标题}
\textbf{问题:} ...?
\textbf{回答:} ...
```

### 5. Label 和 Cross-reference 规范

**命名规范：**
- 定理：\label{def:TheoremXX}
- 引理：\label{def:LemmaXX}
- 定义：\label{def:名称}
- 章节：\label{sec:名称}

**引用方式：**
- 必须使用 \cref{标签名}（需要 cleveref 宏包）
- 禁止使用硬编码数字引用

### 6. LaTeX 格式规范

**禁止在 Definition/Theorem 环境中使用 itemize**，使用 enumerate 替代。

**脚注：**
- 使用 \footnote{} 添加说明

---

## 微分几何 (Differential Geometry)

### 教材
- **Do Carmo - Differential Geometry of Curves and Surfaces**
  - Part I: Curves (Chapter 1-2)
  - Part II: Surfaces (Chapter 3-4)

### 笔记目录结构
```
notes/differential-geometry/
└── do-carmo-curves-surfaces/           # 一个 part = 一本书
    ├── do-carmo-curves-surfaces-notes.tex  # 主文件
    ├── compile.sh                         # 编译脚本
    ├── chapters/
    │   ├── chapter1.tex                  # Chapter 1: Curves
    │   └── chapter2.tex                  # Chapter 2: Regular Surfaces
    └── appendix/
        └── qa.tex                        # 问答记录
```

### 第一章目录（Curves）
- 1-1 Introduction (p.1)
- 1-2 Parametrized Curves (p.2)
- 1-3 Regular Curves; Arc Length (p.6)
- 1-4 The Vector Product in R3 (p.12)
- 1-5 The Local Theory of Curves Parametrized by Arc Length (p.17)
- 1-6 The Local Canonical Form (p.28)
- 1-7 Global Properties of Plane Curves (p.31)

---

## 经验教训
- 2025-03-14: 混淆了4.1节（有限总体量）和4.2节（Neyman Theorem）中的符号，导致定理中使用错误。修正方法：直接读取原文原文对照。
- 2026-03-15: 读取 Do Carmo 微分几何教材时，没有先读取目录页（Table of Contents），导致章节编号错误（用了 1.1 而非 1-1）。修正方法：读取任何 PDF 书籍时，必须先读取目录页确认章节结构。
- 2026-03-15: R 语言绘图默认不支持中文，会显示乱码。修正方法：所有 R 图表必须使用英文标签。
- 2026-03-15: LaTeX 图片位置控制：使用 [H] 强制固定图片在当前插入位置（需加载 float 宏包）。

## 核心工作流

### 1. 阅读流程
1. 扫描阶段：解析 PDF，提取章节结构
2. 逐章阅读：用户选择章节，深入学习
3. 交互问答：用户提问，实时解答

### 2. 讲义生成
- 使用 Stein 写作风格：动机驱动、与已有知识关联
- LaTeX 格式规范（重要！）
  - 禁止在 Definition/Theorem 环境中使用 itemize
  - 使用 enumerate 替代
  - 条件之间用分号分隔
- 每章独立 .tex 文件，main.tex 整合

### 3. 问答机制（重要！）
**每次用户提问后，必须自动执行：**
1. ✅ 用口语化方式回答用户
2. ✅ 添加用户注解到 LaTeX 讲义（\userannotation）
3. ✅ 记录问题到 progress.json
4. ✅ 重新编译 PDF

### 4. 符号定义规则（重要！避免错误）
**生成讲义前必须：**
- 使用 `pdftotext` 提取原文相关章节内容
- 核对章节开头的符号定义
- 第一次出现的符号必须提前定义

**常见符号约定：**
- 带 hat (^) = 样本估计量（从数据计算）
- 不带 hat = 总体真值/有限总体量
- 例如：$\hat{\bar{Y}}(1)$ 是样本均值，$\bar{Y}(1)$ 是有限总体均值

### 5. Label 和 Cross-reference 规范（重要！）
**每次定义 Theorem、Lemma、Definition、Proposition 等环境时：**
1. 必须添加 `\label{xxx}`，格式为 `\label{标签名}`
2. 引用时必须使用 `\cref{标签名}`（需要先加载 cleveref 宏包）
3. 标签命名规范：
   - 定理：`thm:名称`，如 `\label_thm:neyman_theorem}`
   - 引理：`lemma:名称`
   - 定义：`def:名称`
   - 例子：`ex:名称`
   - 章节：`sec:名称`

**示例：**
```latex
\begin{Theorem}[Neyman's Theorem]\label_thm:neyman}
...
根据 \cref_thm:neyman}，...
```

## 文件结构
```
notes/
├── main.tex
├── chapters/
│   ├── chapter1.tex
│   ├── chapter2.tex
│   ├── chapter3.tex
│   └── chapter4.tex
└── appendix/
    └── qa.tex
```

## 进度记录
- progress.json：机器可读
- progress.md：人类可读

## 已覆盖章节
- Chapter 1: 相关性、关联与 Yule-Simpson 悖论
- Chapter 2: 潜在结果框架
- Chapter 3: 随机实验与 FRT
- Chapter 4: 完全随机实验与 Neymanian 推断

## 经验教训
- 2025-03-14: 混淆了4.1节（有限总体量）和4.2节（Neyman Theorem）中的符号，导致定理中使用错误。修正方法：直接读取原文原文对照。
- 2026-03-15: 读取 Do Carmo 微分几何教材时，没有先读取目录页（Table of Contents），导致章节编号错误（用了 1.1 而非 1-1）。修正方法：读取任何 PDF 书籍时，必须先读取目录页确认章节结构。
- 2026-03-15: R 语言绘图默认不支持中文，会显示乱码。修正方法：所有 R 图表必须使用英文标签。
- 2026-03-15: LaTeX 图片位置控制：使用 [H] 强制固定图片在当前插入位置（需加载 float 宏包）。

### LaTeX 命名规范（重要！）
- **主文件**必须命名为 `<主题>-notes.tex`，禁止使用 `main.tex`
- 例如：`information-geometry-notes.tex`、`bayesian-analysis-notes.tex`

## 贝叶斯统计课程 (Probability and Inference)

### PDF 文件列表
```
PDFs/bayesian/
├── 01-three-steps.pdf          # Ch1: 贝叶斯数据分析三步骤
├── 02-single-parameter-models.pdf  # Ch2: 单参数模型
├── 03-multi-parameter-models.pdf   # Ch3: 多参数模型
├── 05-hierarchical-models.pdf      # Ch5: 分层模型
├── 06-model-checking.pdf            # Ch6: 模型检查
├── 10-bayesian-workflow.pdf        # Ch10: 贝叶斯工作流
├── 11-advanced-topics.pdf         # Ch11: 高级主题
├── Metropolis算法简要证明.pdf       # 补充：Metropolis算法证明
├── R语言实现抽样基础.pdf            # 补充：R语言抽样实现
├── p值补充.pdf                      # 补充：p值
└── 拒绝抽样补充.pdf                 # 补充：拒绝抽样
```

### 笔记文件夹
- `notes/bayesian/` - 贝叶斯课程讲义

## 信息几何 (Information Geometry)

### PDF 文件列表
```
PDFs/information-geometry/
├── Amari-Information-Geometry-and-Its-Applications.pdf  # 核心教材
├── Ay-Jost-Le-Schwachhofer-Information-Geometry.pdf    # 数学基础
├── Cover-Thomas-Elements-Information-Theory-GTM134.pdf  # 信息论基础
├── Pistone-Nonparametric-Information-Geometry.pdf       # 非参数IG
├── Pistone-Lecture-Orlicz-Spaces-Information-Geometry.pdf  # Orlicz空间
├── Streater-Quantum-Orlicz-Spaces-Information-Geometry.pdf  # 量子IG
├── Harper-Information-Geometry-Evolutionary-Game-Theory.pdf  # 进化博弈
├── Crooks-Thermodynamic-Length.pdf                        # 热力学长度
├── Tsallis-Generalized-Boltzmann-Gibbs-Statistics.pdf    # Tsallis统计
├── Lin-Zhang-Zhang-Reproducing-Kernel-Banach-Spaces.pdf # 再生核Banach空间
├── Dahl-Finsler-Geometry-Introduction.pdf               # Finsler几何
└── ... (共24个文件)
```

### 笔记文件夹
- `notes/information-geometry/` - 信息几何讲义

### 核心概念
- **Fisher信息度量**：概率分布空间的自然黎曼度量
- **对偶联络**：指数联络与混合联络
- **$\alpha$-联络族**：信息几何的核心结构

### 讲义目录结构
**【重要】一个 Part 对应一本书，Part 下包含该书的各个 Chapter**

```
notes/information-geometry/
├── information-geometry-notes.tex    # 主文件（不要用main.tex）
├── chapters/
│   └── chapter0.tex                  # 文献概述/导论
├── Amari-PartI/                      # Part I: Amari - 散度与对偶平坦结构
│   ├── part.tex                      # Part 简介
│   └── chapters/
│       └── chapter1.tex             # Chapter 1-4
├── Amari-PartII/                     # Part II: 对偶微分几何
├── Amari-PartIII/                    # Part III: 统计推断的信息几何
├── Amari-PartIV/                     # Part IV: 应用
└── appendix/
    └── qa.tex                        # 问答记录
```

### Part 划分（Amari《Information Geometry and Its Applications》）

| Part | 名称 | 章节 | 核心内容 |
|------|------|------|----------|
| Part I | 散度函数与对偶平坦黎曼结构 | Ch1-4 | 散度、指数族、Fisher信息 |
| Part II | 对偶微分几何入门 | Ch5-6 | 协触、对偶联络 |
| Part III | 统计推断的信息几何 | Ch7-10 | 渐近理论、EM算法 |
| Part IV | 信息几何应用 | Ch11-16 | 机器学习、神经网络、物理 |

## Schubert 多项式文献学习

### 8篇文献

**核心文献 (4篇):**
1. GaoXiong-TripleSchubertPositivity.pdf - Graham Positivity of Triple Schubert Calculus (2025, 6页)
2. MolevSagan-Formula-DoubleSchubert.pdf - Molev-Sagan Type Formula (2024, 30页)
3. KirillovMaeno-QuantumDoubleSchubert.pdf - Quantum Double Schubert (1996, 52页)
4. Mihalcea-QuantumSchubertPositivity.pdf - Quantum Schubert Positivity (约2007, 15页)

**参考书籍 (4篇):**
- Anderson & Fulton - Equivariant Cohomology in Algebraic Geometry
- Li (2023) - Schubert Calculus: A Brief Introduction
- Li (2023) - Certain Identities on the Quantum Product of Schubert Classes
- Buch (2001) - Quantum Cohomology of Grassmannians

### 讲义目录结构
```
notes/Schubert-Polynomials/
├── schubert-positivity-notes.tex  # 主文件
├── compile.sh                      # 编译脚本
├── references.bib                  # BibTeX
├── chapters/
│   ├── chapter0.tex               # 文献概述
│   └── chapter1.tex               # GaoXiong 论文
└── appendix/
    └── qa.tex                     # 问答记录
```

### LaTeX 规范

**命名规范：**
- 主文件：`<主题>-notes.tex`，不要用 `main.tex`

**句号格式：**
- 英文句点 + 空格："... ."

**Theorem Style:**
- 使用 `\theoremstyle{definition}` 使关键词加粗左对齐

### 格式规范

**Label 和引用：**
- 定义：\label{def:名称}
- 引用：\cref{def:名称}（需要 cleveref 宏包）

**脚注：**
- 使用 \footnote{} 添加说明（如 $S_\infty$ 的定义）
