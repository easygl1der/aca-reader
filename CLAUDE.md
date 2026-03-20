# CLAUDE.md

This file provides guidance to Claude Code when working with this literature study and note-taking workflow project.

---

## 项目概述

- **项目类型**: 文献阅读与讲义生成工作流系统
- **核心功能**: 阅读学术论文/教材，生成 LaTeX 讲义
- **当前主题**: 因果推断 (Peng Ding - A First Course in Causal Inference)

---

## 重要规则

1. **"记住" 规则**: 用户说"记住 XXX"时，必须写入 CLAUDE.md
2. **LaTeX 格式严格性**: 禁止 Markdown 格式，必须使用纯 LaTeX（详见 `docs/latex-style.md`）
3. **先读原文再写笔记**: 禁止凭想象编写数学证明
4. **作业路径**: `/Users/yueyh/Library/CloudStorage/GoogleDrive-easyglider458@gmail.com/My Drive/homework`
5. **作业模板**: 使用 `> [!exr]` callout 格式，每个题目单独一个 block。参考 `离散数学/hw2.md`
6. **Unicode 禁止规则**: 写作 markdown/LaTeX 时，禁止使用 n₁ 等 unicode 下标，必须使用 `$n_1$` 格式
7. **Tex 优先规则**: 查看教材时，如果有 .tex 版本则优先使用（因为有更好的 label/cref 引用跳转功能）
8. **引用 equation 必须完整**: 习题中如果要求 "Verify (3.7)" 或 "Show that (X.Y)"，必须查找并写出完整的 equation 内容，不能只写编号

---

## 写作风格

### 数学符号习惯

**用户偏好（必须遵循）：**

| 概念 | 符号 |
|------|------|
| 概率 | `\mathbb{P}(A)` |
| 期望（单变量） | `\mathbb{E}X` |
| 期望（多变量） | `\mathbb{E}(XY)` |
| 方差 | `\text{var}` |
| 协方差 | `\text{cov}` |
| 相关系数 | `\text{corr}` |
| 独立性 | `$A \Perp B$` |
| 示性函数 | `\mathbb{I}(X \in A)` 或 `\mathbb{I}_A(X)` 或 `\mathbb{I}(a \leq X < b)` |

详见 `docs/latex-style.md` 的"数学符号习惯"章节。

### 语言风格
- **英文文献**：尽量保持英文原文叙述（用语、习惯、单词层面）
- **中文叙述**：专业名词保持用英文，加括号标注原文
  - 例如：potential outcomes（潜在结果）、causal effect（因果效应）

### 内容风格
**必须模仿 Stein《傅里叶分析》《复分析》的 motivation 风格**（详细指南见 `docs/stein-writing-style.md`）：

- **动机优先**: 每个概念/定理引入前，先解释"为什么需要它"和"它从哪里来"
- **历史脉络**: 注重概念的起源和发展历史
- **有机联系**: 强调不同数学领域之间的相互关联
- **叙事流畅**: 定义→命题→证明之间有连贯的叙述，避免干巴巴的罗列
- **循序渐进**: 从简单到复杂，不过早引入技术细节

---

## 快速参考

### Label 和引用
- 命名规范：\label{def:名称}
- 引用方式：\cref{标签名}
- 详细规则：见 `docs/label-reference.md`

### 文献定理引用格式
当引用文献中的定理/引理/猜想时，必须标出原文献的编号：
- 格式：`\cite[ Theorem 1.1]{Gr}`
- 示例：`Graham Positivity Theorem {\cite[ Theorem 1.1]{Gr}}`
- Conjecture 引用：`Samuel 猜想 {\cite[Conjecture 1.2]{Sa}}`
- Section 引用：`\cite[Section 3]{GX2025}`

### 目录结构
- 标准结构：notes/<主题>/<主题>-notes.tex
- 多 Part 书籍：notes/<主题>/<书籍名>/
- 详细规范：见 `docs/structure.md`

---

## 主题进度

### 因果推断
- 书籍: A First Course in Causal Inference (Peng Ding)
- 笔记: `notes/A-First-Course-in-Causal-Inference/`
- 状态: 1-4章 ✅，5-18章 ⭕

### 微分几何
- 书籍: Do Carmo - Differential Geometry
- 笔记: `notes/differential-geometry/do-carmo-curves-surfaces/`
- 状态: Chapter 1-2 ✅

### 贝叶斯统计
- 书籍: Bayesian Data Analysis (Gelman et al.)
- 笔记: `notes/bayesian/`

### 信息几何
- 书籍: Amari - Information Geometry and Its Applications
- 笔记: `notes/information-geometry/`

---

## Git 提交习惯

**原则**: 每次更新了能跑通的内容就 commit

- **LaTeX 笔记**: 编译成功后就 commit
- **规范文档**: 更新了 docs/ 就 commit
- **commit 风格**: 简洁，说明改了啥

### Git Worktree 安全规则

**当遇到以下情况时，必须使用 git worktree 隔离操作**：
- 处理大文件（>50MB）
- 执行破坏性操作（如 `filter-repo`、`rebase`、`reset --hard`）
- 不确定操作是否安全
- 任何可能影响主分支的操作

**使用方法**：
```bash
# 创建隔离的 worktree
git worktree add ../workspace-backup -b backup-branch

# 在 worktree 中操作
cd ../workspace-backup
# 执行危险操作...

# 确认安全后，合并回主分支
git merge backup-branch

# 不安全则直接删除 worktree
git worktree remove ../workspace-backup
git worktree prune
```

---

## LaTeX 编译规范

**重要**: 每个笔记目录都有专属的编译脚本，编译时必须使用：

- `notes/Schubert-Polynomials/compile.sh` → xelatex, 3次
- 其他目录类似

禁止直接使用 `latexmk` 或 `xelatex` 命令。

---

## 经验教训

**详细记录**: `docs/lessons/` 目录下按时间或主题分类

每次用户纠正我的错误时，自动记录到 `docs/lessons/` 并更新 CLAUDE.md 中的摘要

- **2025-03-14**: 混淆符号导致定理错误 → 直接读原文对照
- **2026-03-15**: 未先读目录页导致章节编号错误 → 先读 Table of Contents
- **2026-03-15**: R 中文乱码 → 用英文标签
- **2026-03-15**: LaTeX 图片位置 → 使用 [H] 强制固定（需 float 宏包）
- **2026-03-16**: 1998年前论文无 arXiv → 用 DOI
- **2026-03-18**: LaTeX 笔记中避免口语化表达（如"这里错了"、"让我重新计算"），直接给出正确推导即可
- **2026-03-19**: 遇到文献中省略证明的定理，如果找不到证明或没有可行思路，必须使用 /gemini-browser-chat 询问 Gemini（必须使用 Pro 模式）
- **2026-03-19**: Gemini browser chat 必须使用 Pro 模式

---

## ⚠️ Git 大文件处理禁止规则

**禁止使用 git 处理大文件（>50MB）**，包括但不限于：

- ❌ `git filter-repo` 重写历史
- ❌ `git lfs track` / `git lfs install` / 任何 git lfs 命令
- ❌ `git add` 大文件后配合 commit
- ⚠️ **绝对禁止使用 git-lfs**

**原因（2026-03-19 血泪教训）**：

1. `git filter-repo --path A --path B` 是**白名单模式**，会删除 A、B 之外所有文件的 git 历史
2. `git lfs` 在 `git add` 后会**删除本地大文件**，只保留 134 bytes 的指针
3. 超过 100MB 的文件**无法 push 到 GitHub**（会被 pre-receive hook 拒绝）
4. push 失败后，如果执行了 `git add` + `git commit`，本地大文件已被 lfs 删除，无法恢复

**正确做法**：
- 超大 PDF（>50MB）**不要提交到 git**
- 单独备份到 Google Drive 或其他外部存储
- 或使用 GitHub LFS（需付费，免费额度仅 1GB）
- 如果必须处理，**先问用户**，获得明确同意后再操作

---

## 记笔记习惯（历史参考）

**详细说明**: 见 `docs/note-taking-habits.md`

基于 2025-summer（大二下学期）笔记分析：

### 技术习惯
- **工具链**: Obsidian → LaTeX → PDF
- **格式**: Markdown + LaTeX（行内 `$...$`，单独 `$$...$$`）
- **图片**: `![[filename]]` Obsidian 内部链接
- **Callout**: `> [!example]`, `> [!def]`, `> [!thm]` 等
- **作业流程**:
  1. Obsidian 中用 md 笔记
  2. 导出/编写 LaTeX .tex
  3. 编译为 PDF（xelatex/latexmk）
- **定理环境**: amsart + 自定义 theorem/lemma/definition 等
- **文件命名**: kebab-case（如 `differential-manifold.md`）

### 写作风格（内容层面）

**用词习惯**：
- 思考性句式: "We wonder if...", "You are right to...", "We want to show that..."
- 解释性短语: "This essentially means that...", "The key insight is...", "This is where... comes in"
- 连接词: "Clearly,", "In fact,", "Therefore,", "Thus,", "Then,"

**概念引入方式**：
- 先形式化定义，再解释直观含义（"This means..."）
- 喜欢追问 "为什么"，解释动机和条件的作用
- 注重几何直观，用例子阐明抽象概念
- 喜欢用 "Why/What/How" 问题式标题

**组织语言**：
- 用 bullet points 列举要点，用表格做 Summary
- 证明风格：开头 "We need to show that..."，结尾 "We are done!"
- 喜欢把新概念和已知概念建立联系，强调对偶性
- 喜欢 "Roadmap of This Lecture" / "Big Picture Thread" 结构
- 结论用 "This gives us...", "This provides..." 连接
- 喜欢对比不同情况（"Dirichlet vs. Neumann"）

---

## PDF 转录 (minerU)

### 使用方法
1. 在 **Google Colab** 中运行 minerU 进行 PDF 转录
2. 转录输出包含：
   - `.md` 文件（带完整目录结构）
   - `images/` 文件夹（所有提取的图片）

### 图片引用路径
- md 文件中 figure 标签的路径格式：`images/page-XX_figure_N.png`
- 笔记中引用图片时，直接使用 md 中标注的路径
- 示例：md 中显示 `images/fig_1-1.png`，笔记中就写 `images/fig_1-1.png`

---

## Figure 提取

**脚本**: `/Users/yueyh/.claude/skills/figure-extractor/figure_extractor.py`

**使用方法**：
```bash
python figure_extractor.py <图片路径> -o <输出目录>
```

**配置**：模型 gemini-3.1-flash，DPI 400

---

## 文献库

| 主题 | 路径 | 备注 |
|------|------|------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/` | |
| 微分几何 | `PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.md` | |
| 贝叶斯 | `PDFs/bayesian/` | |
| 信息几何 | `PDFs/information-geometry/` | 24个文件 |
| Stein 系列 | `PDFs/Stein系列/` | ⚠️ 2026-03-19 丢失，需从 minerU 重新生成 |

### Stein 系列恢复指南

Stein 系列教材（Real Analysis I/II/III, Complex Analysis, Fourier Analysis）的 PDF 因超过 100MB 从未被提交到 GitHub，且在 2026-03-19 的 git-lfs 事故中被删除。**必须从 minerU 重新生成转录本**：

1. 在 Google Colab 中重新运行 minerU
2. 输出到 `PDFs/Stein系列/transcript/`
3. 生成的 PDF 备份到 Google Drive（不要 push 到 GitHub）
