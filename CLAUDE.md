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

---

## 快速参考

### Label 和引用
- 命名规范：\label{def:名称}
- 引用方式：\cref{标签名}
- 详细规则：见 `docs/label-reference.md`

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

---

## 记笔记习惯（历史参考）

**详细说明**: 见 `docs/note-taking-habits.md`

基于 2025-summer（大二下学期）笔记分析：

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

---

## 经验教训

**详细记录**: `docs/lessons/` 目录下按时间或主题分类

每次用户纠正我的错误时，自动记录到 `docs/lessons/` 并更新 CLAUDE.md 中的摘要

- **2025-03-14**: 混淆符号导致定理错误 → 直接读原文对照
- **2026-03-15**: 未先读目录页导致章节编号错误 → 先读 Table of Contents
- **2026-03-15**: R 中文乱码 → 用英文标签
- **2026-03-15**: LaTeX 图片位置 → 使用 [H] 强制固定（需 float 宏包）
- **2026-03-16**: 1998年前论文无 arXiv → 用 DOI

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

**脚本**: `/Users/yueyh/.claude/skills/figure_extractor.py`

**使用方法**：
```bash
python figure_extractor.py <图片路径> -o <输出目录>
```

**配置**：模型 gemini-3.1-flash，DPI 400

---

## 文献库

| 主题 | 路径 |
|------|------|
| 因果推断 | `PDFs/causal-inference/transcript/A First Course in Causal Inference - Peng Ding/` |
| 微分几何 | `PDFs/differential-geometry/Do Carmo - Differential Geometry of Curves and Surfaces.md` |
| 贝叶斯 | `PDFs/bayesian/` |
| 信息几何 | `PDFs/information-geometry/` (24个文件) |
