# Vibe Research Slides v3 - 需求文档

## Slide 制作要求

1. **主题**: Vibe Research - 基于 Claude Code 的自动化科研工作流
2. **页数**: 50-70 pages
3. **风格**: geek-light (白色背景 + cyan 强调色)
4. **字体**: Space Grotesk (标题) + JetBrains Mono (代码)
5. **动效**: reveal 动画，滚动吸附导航
6. **结构**: 每个 Skill 单独一页，包含名字、描述、使用场景、效果
7. **演讲时长**: 15-20 分钟 + 问答环节

---

## 完整结构 (约 60 pages)

| Slide | Type | Content | 详细内容 |
|-------|------|---------|----------|
| 1 | Title | Vibe Research | 基于 Claude Code 的自动化科研工作流 |
| 2 | Intro | What is Vibe Research | 核心定位：让研究者专注思考而非工具；设计哲学 |
| 3 | Problem | 学术研究痛点 | **痛点1**: AI 不读文献库，回答太 general；**痛点2**: 笔记风格不连贯，需要手动调整格式 |
| 4 | Solution | Skills 系统解决方案 | 24个技能分类，即插即用 |
| 5 | Philosophy | 设计哲学 | 自动化、一致性、可追溯 |
| 6 | Toolchain | 核心技术栈 | Claude Code + Obsidian + LaTeX + MinerU + Skills |
| 7 | Stats | **MiniMax 28亿 Tokens** | 持续迭代验证 |
| 8 | Section | Section 2 - Local AI | |
| 9 | Content | Claude Code Local | 代码执行、文件系统、工具调用、多模型支持 |
| 10 | Content | Skills 系统结构 | Skills 文件结构、24个Skills分类树 |
| 11 | Content | MinerU | PDF 高精度转 Markdown，保留公式图表 |
| 12 | Section | Section 3 - Memory System | |
| 13 | Content | Memory System | MEMORY.md (跨会话) + CLAUDE.md (项目规范) |
| 14 | Content | MEMORY.md | 跨会话持久记忆，进度追踪，经验教训 |
| 15 | Content | CLAUDE.md | 提示词引擎，写作风格，符号约定 |
| 16 | Section | Section 4 - Skills | |
| 17 | Content | Skill System Overview | 24个Skills分类总览 |
| 18 | Section | Section 5 - Reading & Notes | |
| 19 | Content | 阅读与笔记 Skills 概览 | 6个Skills：latex-notes, skim-jump, reading-progress, interactive-qa, obsidian-cli, literature-notes-template |
| 20 | Skill | latex-notes | Stein风格 motivation 写作，自动交叉引用 |
| 21 | Skill | skim-jump | PDF ↔ 笔记双向联动，Mac Skim集成 |
| 22 | Skill | reading-progress | 追踪阅读进度、问答记录到JSON |
| 23 | Skill | interactive-qa | 问答归档到 qa.tex，同步更新讲义 |
| 24 | Skill | obsidian-cli | Obsidian 命令行，笔记 CRUD |
| 25 | Skill | literature-notes-template | 文献笔记模板，元数据生成 |
| 26 | Section | Section 6 - Research & Citation | |
| 27 | Content | 研究与引用 Skills 概览 | 4个Skills：gs-search, paper-references-generator, literature-reference-manager, citation-bibliography-generator |
| 28 | Skill | gs-search | Google Scholar 搜索，标题/作者/年份/引用数 |
| 29 | Skill | paper-references-generator | CrossRef API 提取参考文献 → BibTeX |
| 30 | Skill | literature-reference-manager | 文献库扫描，批量 BibTeX 生成 |
| 31 | Skill | citation-bibliography-generator | APA/MLA/Chicago/IEEE/Harvard 多格式 |
| 32 | Section | Section 7 - Figure Extraction | |
| 33 | Content | 图表提取 Skills 概览 | 4个Skills |
| 34 | Skill | pdf-figure-extractor | 600 DPI 高清，Gemini Vision 边界框 |
| 35 | Skill | figure-extractor | 数学插图提取，400 DPI，断点续传 |
| 36 | Skill | gemini-image-analyzer | 图表内容提取，数学公式识别 |
| 37 | Skill | minimax-vision | OCR 识别，表格数据提取 |
| 38 | Section | Section 8 - Writing & Templates | |
| 39 | Content | 写作与模板 Skills 概览 | 4个Skills |
| 40 | Skill | beamer-chinese-presentation | Beamer 模板，结构化演讲稿 |
| 41 | Skill | homework-workflow | Google Drive 集成，规范化提交 |
| 42 | Skill | chapter0-template | 章节笔记框架，动机引入 |
| 43 | Skill | note-content-verifier | 公式一致性，引用完整性检查 |
| 44 | Section | Section 9 - Development & AI | |
| 45 | Content | 开发与AI Skills 概览 | 6个Skills |
| 46 | Skill | frontend-slides | HTML 演示生成，零依赖 |
| 47 | Skill | auto-commit-push | Git 自动提交，大文件检查 |
| 48 | Skill | latex-label-ref-verifier | \label 和 \ref 一致性检查 |
| 49 | Skill | latex-debug | LaTeX 编译错误诊断修复 |
| 50 | Skill | gemini-browser-chat | Playwright + Gemini Pro，复杂数学推理 |
| 51 | Skill | r-expert | 命令行 R，代码复现，统计可视化 |
| 52 | Section | Section 10 - Complete Workflow | |
| 53 | Content | 全流程图 | PDF → MinerU → Markdown → AI → 问答 → 笔记 → 讲义 |
| 54 | Content | 阅读阶段 | PDF → MinerU → 语义分割 → 逐章阅读 |
| 55 | Content | 笔记阶段 | 问答记录 → LaTeX → 编译 PDF → 归档 |
| 56 | Section | Section 11 - Real Cases | |
| 57 | Content | Schubert 演算案例 | 历史脉络：Schubert(1879)→Bernstein(1973)→Demazure(1974)→Lascoux-Schützenberger(1982) |
| 58 | Section | Section 12 - Subagent 概念 | |
| 59 | Content | Subagent 设想 | 每个文献库配置专属 Subagent |
| 60 | Content | Subagent 特性 | 独立记忆 + 个性化提示词 + 领域专长 |
| 61 | Content | Subagent 示例 | Schubert(几何+图片) / 统计学(代码+R) |
| 62 | Section | Section 13 - Future Work | |
| 63 | Content | Future Roadmap | 扩大文献库 / 自动化增强 / 工具集成 / 知识图谱 / 协作功能 |
| 64 | Content | Key Takeaways | 让研究者专注思考，而非工具 |
| 65 | Section | Section 13 - Summary | |
| 66 | Content | Skills 总览 | 24 Skills 5 大类一览 |
| 67 | Section | Q&A | |
| 68 | Content | 相关资源 | Vibe Research + Built with Claude Code |
| 69 | Ending | Thank You | |

---

## 每一页详细内容

### Slide 1: Title
- Vibe Research
- 基于 Claude Code 的自动化科研工作流
- 报告人: 乐绎华 中山大学 数学学院 23 级
- 联系邮箱：yueyh@mail2.sysu.edu.cn
- 报告时长：15-20 分钟

---

### Slide 2: What is Vibe Research
**核心定位**：
- 将 AI 深度融入学术研究全流程
- 文献阅读 → 笔记整理 → 讲义生成

**设计哲学**：
- "让 AI 取代科研中的过于繁琐的重复性工作"
- "让学生、研究者专注思考，而非工具"

---

### Slide 3: Problem - 两个核心痛点

**痛点 1: AI 不读文献库**
- 网页端对话框的知识来源过于 general
- AI 不知道文献库已有的符号和技巧
- 不会引用文献库内容


**痛点 2: 笔记风格不连贯**
- 复制粘贴的回答可能不符合已有笔记的风格
- 希望开头讲背景、motivation、前置知识
- 希望风格统一：定理历史、前因后果
- 网页端 Gemini 每次要重新输入提示词

---

### Slide 4: Solution
- **CLAUDE.md**: 预先设定提示词，设置写作风格
- **MEMORY.md**: 跨会话记忆
- **Skills 系统**: 24个领域特定技能

---

### Slide 5: Philosophy
- **自动化**: 重复性工作交给 AI
- **一致性**: 符号、格式、引用规范化
- **可追溯**: 完整的知识演化路径

---

### Slide 6: Toolchain
- Claude Code: AI 能力核心
- MinerU: PDF → Markdown
- Obsidian: 知识管理
- LaTeX: 专业排版
- Skills: 领域特定工作流
- Git: 备份历史

---

### Slide 7: MiniMax Stats
- **28 亿+ Tokens** 累计调用
- 持续迭代验证工作流有效性

放上图片：/Users/yueyh/Projects/aca-workflow/figures/PixPin_2026-03-22_02-38-00.png

---

### Slide 9: Claude Code 

- skills
- subagent
- memory   
    - claude.md
    - memory.md
- history

---

### Slide 10: Skills 系统结构

**Skills 文件结构**：

```
~/.claude/skills/         # 全局 Skills 目录
└── 24 个 Skill 子目录
```

**24 Skills 5 大类**：

| 类别 | Skills |
|------|--------|
| **阅读与笔记 (6)** | latex-notes — LaTeX 讲义生成<br>skim-jump — PDF 双向联动<br>reading-progress — 阅读进度管理<br>interactive-qa — 交互式问答<br>obsidian-cli — Obsidian 命令行<br>literature-notes-template — 文献笔记模板 |
| **研究与引用 (4)** | gs-search — Google Scholar 搜索<br>paper-references-generator — CrossRef API 参考文献提取<br>literature-reference-manager — 文献库批量管理<br>citation-bibliography-generator — 多格式引用生成 |
| **图表提取 (4)** | pdf-figure-extractor — PDF 图表提取<br>figure-extractor — 数学插图提取<br>gemini-image-analyzer — 图表内容提取<br>minimax-vision — OCR 表格识别 |
| **写作与模板 (4)** | beamer-chinese-presentation — Beamer 演示文稿<br>homework-workflow — 作业规范化<br>chapter0-template — 章节笔记框架<br>note-content-verifier — 笔记校验 |
| **开发与AI (6)** | frontend-slides — HTML 演示生成<br>auto-commit-push — Git 自动提交<br>latex-label-ref-verifier — Label/Ref 检查<br>latex-debug — LaTeX 调试<br>gemini-browser-chat — Gemini 数学专家<br>r-expert — R 语言专家 |

---

### Slide 11: MinerU
**优势**：
- pdf转markdown
- 保留数学公式
- 自动提取图表
- 保留目录结构

示例：
```
.
├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics.pdf
└── transcript
    └── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics
        └── hybrid_ocr
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics.md
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_content_list.json
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_content_list_v2.json
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_layout.pdf
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_middle.json
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_model.json
            ├── Hogg-McKean-Craig-Introduction-to-Mathematical-Statistics_origin.pdf
            └── images
```

---

### Slide 13-15: Memory System

**MEMORY.md**:
- 跨会话持久记忆
- 项目进度追踪
- 经验教训归档
- 符号约定汇总

**CLAUDE.md**:
- 提示词引擎
- 写作风格规则
- 数学符号约定
- Git 提交习惯

---

### Slide 17: Skill System Overview

**5 大类 24 Skills**：
- 阅读与笔记 (6)
- 研究与引用 (4)
- 图表提取 (4)
- 写作与模板 (4)
- 开发与AI (6)

---

## Skills 详细说明

### 1. 阅读与笔记 Skills

#### Skill 01: latex-notes

| 项目 | 内容 |
|------|------|
| **描述** | 生成 LaTeX 格式学习讲义 |
| **使用场景** | 阅读学术论文时自动生成符合学术规范的讲义 |
| **效果** | Stein《傅里叶分析》风格 motivation 写作，自动交叉引用 |

```latex
% 用户注解命令
\newcommand{\userannotation}[2]{%
  \begin{trivlist}
    \item[\textbf{用户注解:}] #1
    \textit{#2}
  \end{trivlist}
}

% 定义环境禁止使用 itemize！
\begin{Definition}[完全随机实验]
设有 $n$ 个样本，其中 $n_1$ 个被分配到治疗组：
\begin{enumerate}
  \item 每个个体被分配到治疗组的概率为 $n_1/n$；
  \item 治疗组总人数固定为 $n_1$；
  \item 个体之间相互独立。
\end{enumerate}
\end{Definition}
```

---

#### Skill 02: skim-jump

| 项目 | 内容 |
|------|------|
| **描述** | PDF 与笔记双向联动 |
| **使用场景** | Mac 上用 Skim 阅读 PDF，想跳转到笔记对应位置 |
| **效果** | AI 模糊搜索定位到某一行，Cmd+Shift+点击跳转到笔记 |

```bash
# Skim displayline 跳转命令
/Applications/Skim.app/Contents/SharedSupport/displayline \
  -r -g [行号] "[PDF路径]" "[TeX源文件路径]"

# 示例：跳转到第 584 行
/Applications/Skim.app/Contents/SharedSupport/displayline \
  -r -g 584 "notes.pdf" "chapters/chapter1.tex"
```

---

#### Skill 03: reading-progress

| 项目 | 内容 |
|------|------|
| **描述** | 阅读进度管理 |
| **使用场景** | 追踪多章节书籍的阅读位置 |
| **效果** | 进度记录到 JSON 文件，问答记录，历史问题 |

```json
{
  "book": "A First Course in Causal Inference",
  "current_position": {
    "chapter": 3,
    "section": 2,
    "page": 45
  },
  "questions": [
    {
      "date": "2026-03-22",
      "chapter": 3,
      "question": "为什么需要引入潜在结果？",
      "answer": "..."
    }
  ]
}
```

---

#### Skill 04: interactive-qa

| 项目 | 内容 |
|------|------|
| **描述** | 交互式问答 |
| **使用场景** | 阅读中即时提问，回答记录到附录 |
| **效果** | AI 了解你的知识储备，调整叙述方式 |

```bash
# 每次问答后的自动 Git 提交
git add notes/ .claude/skills/reading-progress/progress.json
git commit -m "QA: 第3章 - 潜在结果定义"

# 或使用脚本
./scripts/commit_notes.sh "更新讲义"
```

---

#### Skill 05: obsidian-cli

| 项目 | 内容 |
|------|------|
| **描述** | Obsidian 命令行 |
| **使用场景** | 批量创建笔记、搜索、管理 |
| **效果** | 笔记 CRUD、属性管理 |

```bash
# 创建笔记
obsidian create name="新笔记" content="# Hello" template="Template"

# 搜索笔记
obsidian search query="因果推断" limit=10

# 追加内容
obsidian append file="笔记名" content="新行内容"

# 管理任务
obsidian tasks daily todo
```

---

#### Skill 06: literature-notes-template

| 项目 | 内容 |
|------|------|
| **描述** | 文献笔记模板 |
| **使用场景** | 开始阅读新文献时生成规范笔记 |
| **效果** | 元数据、符号约定、预设问题 |

```
notes/<主题>/
├── <主题>-notes.tex      # 主文件
├── compile.sh            # 编译脚本
├── references.bib        # BibTeX 参考文献
├── chapters/
│   ├── chapter0.tex      # 文献概述
│   └── chapter1.tex      # 第一章
└── appendix/
    └── qa.tex            # 问答记录
```

---

### 2. 研究与引用 Skills

#### Skill 07: gs-search

| 项目 | 内容 |
|------|------|
| **描述** | Google Scholar 搜索 |
| **使用场景** | 查找相关论文 |
| **效果** | 标题、作者、期刊、年份、引用数 |

```javascript
// Google Scholar DOM 抓取
const items = document.querySelectorAll('#gs_res_ccl .gs_r.gs_or');
const results = Array.from(items).map(item => ({
  title: item.querySelector('.gs_rt a')?.textContent,
  authors: item.querySelector('.gs_a')?.textContent,
  citedBy: item.querySelector('.gs_fl a[href*="cites"]')
    ?.textContent.match(/\d+/)?.[0] || '0'
}));
```

---

#### Skill 08: paper-references-generator

| 项目 | 内容 |
|------|------|
| **描述** | 参考文献提取 |
| **使用场景** | 扫描 transcript 提取参考文献 |
| **效果** | CrossRef API 查询，生成 BibTeX |

```bash
# 使用方法
python paper_references_generator.py <md文件路径>

# CrossRef API 查询
https://api.crossref.org/works?query=<关键词>

# 输出 BibTeX
@article{author2023,
  author = {Author, First},
  title = {Paper Title},
  year = {2023},
  doi = {10.xxx/xxx}
}
```

---

#### Skill 09: literature-reference-manager

| 项目 | 内容 |
|------|------|
| **描述** | 文献库管理 |
| **使用场景** | 批量管理大量文献 |
| **效果** | 文献库扫描，批量 BibTeX |

```bash
# 扫描文献库
/文献引用管理器 bayesian

# 生成引用库
/文献引用管理器 bayesian --generate-bib

# 处理指定文献
/文献引用管理器 PDFs/bayesian/textbook/Book.pdf
```

---

#### Skill 10: citation-bibliography-generator

| 项目 | 内容 |
|------|------|
| **描述** | 多格式引用生成 |
| **使用场景** | 按期刊要求格式化 |
| **效果** | APA/MLA/Chicago/IEEE/Harvard |

```python
from scripts.citation_generator import CitationGenerator

gen = CitationGenerator(style='apa')
citation = gen.cite_book(
    authors=["Smith, John", "Doe, Jane"],
    title="Research Methods",
    year=2020,
    publisher="Academic Press"
)
print(citation)
# Output: Smith, J., & Doe, J. (2020). Research methods. Academic Press.
```

---

### 3. 图表提取 Skills

#### Skill 11: pdf-figure-extractor

| 项目 | 内容 |
|------|------|
| **描述** | PDF 图表提取 |
| **使用场景** | 提取论文中的 figure |
| **效果** | 600 DPI，Gemini Vision 边界框识别 |

```bash
# 快速提取 Chapter 2 figures
uv run figure_extractor.py --chapter 2

# 强制重刷
uv run figure_extractor.py --chapter 2 --force

# 仅裁剪模式
uv run figure_extractor.py --chapter 2 --crop-only
```

---

#### Skill 12: figure-extractor

| 项目 | 内容 |
|------|------|
| **描述** | 数学插图提取 |
| **使用场景** | 提取教材中的图表 |
| **效果** | 400 DPI，断点续传 |

```python
# Gemini 边界框识别
PROMPT = f"""看这张教材原图，找出以下 figures 的精确位置：
Figure: Figure X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字
- 四周留 0.02 边距"""

# 裁剪保存
crop = img.crop((int(W * x1), int(H * y1), int(W * x2), int(H * y2)))
crop.save(f"fig_{figure_id}.png", quality=95)
```

---

#### Skill 13: gemini-image-analyzer

| 项目 | 内容 |
|------|------|
| **描述** | 图像理解 |
| **使用场景** | 理解复杂图表含义 |
| **效果** | 数学公式识别，描述生成 |

```bash
# 分析本地图片
echo "请详细描述这张图片的所有内容" | gemini /path/to/image.png

# 分析网络图片
gemini "https://example.com/image.png"
```

---

#### Skill 14: minimax-vision

| 项目 | 内容 |
|------|------|
| **描述** | MiniMax 视觉理解 |
| **使用场景** | OCR、表格提取 |
| **效果** | 多语言支持 |

```bash
# 命令行分析
python3 ~/.claude/skills/minimax-vision/analyze.py /path/to/image.png

# 自定义问题
python3 ~/.claude/skills/minimax-vision/analyze.py \
  /path/to/image.png "这张图片有什么特别之处？"
```

---

### 4. 写作与模板 Skills

#### Skill 15: beamer-chinese-presentation

| 项目 | 内容 |
|------|------|
| **描述** | Beamer 演示文稿 |
| **使用场景** | 创建学术报告 |
| **效果** | SYPSTYLE/CambridgeUS 主题 |

```latex
\documentclass[]{beamer}
\usetheme{CambridgeUS}
\usepackage{xeCJK}
\setCJKmainfont{Source Han Serif SC}

\begin{document}
\maketitle
\section{Section Name}
\begin{frame}
  \begin{block}{Block Title}content\end{block}
  \begin{alertblock}{Alert}important\end{alertblock}
\end{frame}
\end{document}
```

---

#### Skill 16: homework-workflow

| 项目 | 内容 |
|------|------|
| **描述** | 作业工作流 |
| **使用场景** | 规范化提交作业 |
| **效果** | Google Drive 集成，检查 |

```markdown
> [!exr] Problem 3.1
> **Section 3.2** — *Randomized Block Design*
>
> 完整习题内容...

> [!example] Referenced Background: Section 2.5
> 被引用的背景内容

> [!note] Data Information
> 数据变量说明...
```

---

#### Skill 17: chapter0-template

| 项目 | 内容 |
|------|------|
| **描述** | 章节模板 |
| **使用场景** | 开始新章节 |
| **效果** | 动机引入，定义/定理格式 |

```latex
\chapter*{引言：文献概述}\label{chap:introduction}
\addcontentsline{toc}{chapter}{引言：文献概述}

\section{总述}
介绍学习该主题的背景、意义和研究动机。

\section{文献摘要总结}
\subsection{论文标题}
\begin{enumerate}
    \item \textbf{作者:} 作者姓名
    \item \textbf{链接:} \url{https://arxiv.org/abs/xxxx}
    \item \textbf{核心贡献:}
        \begin{itemize}
            \item 贡献点1
            \item 贡献点2
        \end{itemize}
\end{enumerate}
```

---

#### Skill 18: note-content-verifier

| 项目 | 内容 |
|------|------|
| **描述** | 笔记校验 |
| **使用场景** | 提交前检查 |
| **效果** | 公式一致性，引用完整 |

```bash
# 检查 label 定义
grep -nE '\\\\label\{[^}]+\}' notes.tex | grep -v '^(eq:|rem:)'

# 检查 cref 引用
grep -nE '\\\\cref\{[^}]+\}' notes.tex

# 对照原论文验证编号
# Theorem 1.1 → label{def:thm:11}
```

---

### 5. 开发与AI Skills

#### Skill 19: frontend-slides

| 项目 | 内容 |
|------|------|
| **描述** | HTML 演示 |
| **使用场景** | 快速创建演示 |
| **效果** | 动画丰富，零依赖 |

```html
<!-- 单文件 HTML 演示 -->
<section class="slide" data-slide="1">
  <h1>标题</h1>
  <p class="reveal">渐入内容</p>
</section>

<style>
.slide { height: 100vh; overflow: hidden; }
.reveal { animation: fadeIn 1s ease-out; }
</style>
```

---

#### Skill 20: auto-commit-push

| 项目 | 内容 |
|------|------|
| **描述** | Git 自动提交 |
| **使用场景** | 保存工作时自动 commit |
| **效果** | 大文件检查，Co-Authored-By |

```bash
# 自动提交流程
git status --short
git add -A
git commit -m "更新讲义

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
git push origin main
```

---

#### Skill 21: latex-label-ref-verifier

| 项目 | 内容 |
|------|------|
| **描述** | LaTeX 引用检查 |
| **使用场景** | 检查 \label 和 \ref |
| **效果** | 发现悬空引用 |

```bash
# 提取所有 label 定义
grep -nE '\\\\label\{[^}]+\}' <笔记文件>

# 提取所有 cref 引用
grep -nE '\\\\cref\{[^}]+\}' <笔记文件>

# 对照原论文检查编号一致性
# 建立映射表：论文编号 → 笔记 label
```

---

#### Skill 22: latex-debug

| 项目 | 内容 |
|------|------|
| **描述** | LaTeX 调试 |
| **使用场景** | 修复编译错误 |
| **效果** | 标准流程诊断 |

```bash
# 编译检测
xelatex -interaction=nonstopmode main.tex

# 常见错误处理：
# - Undefined reference → 检查 label
# - Missing $ → 检查公式
# - Extra } → 检查括号配对

# 每次修复后提交
git add -A && git commit -m "fix: 修复 LaTeX 错误"
```

---

#### Skill 23: gemini-browser-chat

| 项目 | 内容 |
|------|------|
| **描述** | Gemini Pro 数学专家 |
| **使用场景** | 复杂数学定理证明 |
| **效果** | Playwright 集成，Pro 模式 |

```javascript
// Playwright MCP 工作流
browser_navigate("https://gemini.google.com")

// 找到输入框
browser_type(element: "question input",
  ref: "e350",
  text: "Solve: 复杂数学问题",
  submit: true)

// 等待响应
browser_wait_for(text: "Gemini said", time: 15)
```

---

#### Skill 24: r-expert

| 项目 | 内容 |
|------|------|
| **描述** | R 语言专家 |
| **使用场景** | 复现教材 R 代码 |
| **效果** | 命令行运行，统计可视化 |

```r
library(dplyr)
library(ggplot2)

# 数据处理
df %>%
  filter(age > 28) %>%
  select(name, age, salary) %>%
  mutate(salary_bonus = salary * 1.1) %>%
  ggplot(aes(x = age, y = salary)) +
  geom_point() +
  geom_smooth(method = "lm")

# 统计检验
t.test(salary ~ group, data = df)
lm_model <- lm(outcome ~ age + treatment, data = df)
summary(lm_model)
```

---

## 全流程图

### Slide 53: 完整工作流
```
PDF → MinerU → Markdown → AI 阅读 → 问答 → 笔记 → 讲义
```

### Slide 54: 阅读阶段
```
PDF → MinerU → 语义分割 → 逐章阅读
```

### Slide 55: 笔记阶段
```
问答记录 → LaTeX → 编译 PDF → 归档
```

---

## 实际案例: Schubert 演算

**内容**:
- Schubert Polynomials 的 Positivity 问题
- 历史脉络：
  - Schubert (1879): 计数几何起源
  - Bernstein (1973): 拓扑观点
  - Demazure (1974): 泛性子群
  - Lascoux-Schützenberger (1982): Schubert 多项式

**链接**: https://github.com/easygl1der/aca-reader/blob/main/notes/Schubert-Polynomials/schubert-positivity-notes.pdf

---

## Future Work

- 📚 **扩大文献库**: 覆盖更多数学领域
- 🤖 **自动化增强**: 更多 AI 模型集成
- 🔗 **工具集成**: 深化现有工具链
- 📊 **知识图谱**: 构建概念关联网络
- 🌐 **协作功能**: 多用户协作支持

**目标**: 让研究者专注思考，而非工具

---

## 结尾页面

### Slide 66: Skills 总览
**24 Skills 5 大类一览**：
| 类别 | 数量 | Skills |
|------|------|--------|
| 阅读与笔记 | 6 | latex-notes, skim-jump, reading-progress, interactive-qa, obsidian-cli, literature-notes-template |
| 研究与引用 | 4 | gs-search, paper-references-generator, literature-reference-manager, citation-bibliography-generator |
| 图表提取 | 4 | pdf-figure-extractor, figure-extagger, gemini-image-analyzer, minimax-vision |
| 写作与模板 | 4 | beamer-chinese-presentation, homework-workflow, chapter0-template, note-content-verifier |
| 开发与AI | 6 | frontend-slides, auto-commit-push, latex-label-ref-verifier, latex-debug, gemini-browser-chat, r-expert |

---

### Slide 67: Q&A
- 问答环节
- 欢迎提出想法和建议

---

### Slide 68: 相关资源
- **Vibe Research** — 让学术研究更高效
- **Built with Claude Code**
- GitHub: https://github.com/easygl1der/aca-reader

---

### Slide 69: Thank You
- 感谢聆听
- 期待交流

---

## 修改记录

- 2026-03-22: 创建 v3 需求文档
- 2026-03-22: 添加完整工作流、Schubert 案例、Future Work
- 2026-03-22: 根据 conversation.md 补充每页详细内容、痛点分析、Skills 效果描述
- 2026-03-22: 为每个 Skill 页面添加代码示例（左右两栏布局）
- 2026-03-22: 在 Claude Code 后添加 Skills 系统结构页（含文件树和分类树）
