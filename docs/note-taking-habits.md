# 记笔记习惯总结

> 基于 2025-summer 大二下学期笔记分析

---

## 1. 笔记工具与环境

- **笔记软件**: Obsidian
- **格式**: Markdown + LaTeX
- **数学公式**: 行内 `$...$`，单独成行 `$$...$$`
- **图片嵌入**: `![[filename]]` 语法（Obsidian 内部链接）
- **Callout 语法**: 使用 Obsidian callout 组织内容
  - `> [!example]` 示例
  - `> [!def]` 定义
  - `> [!thm]` 定理
  - `> [!note]` 备注

---

## 2. 目录结构

### 按主题分类
```
2025-summer/
├── Subject Directories
│   ├── Algebra-Geometry/
│   ├── Riemannian-geometry/
│   ├── Lie-algebra/
│   ├── information-geometry/
│   └── ...
├── westlake-university/      # 课程材料
│   ├── homework/             # 作业目录
│   ├── information-geometry-1.md
│   └── ...
└── figures/                   # 图片资源
```

### 文件命名
- 使用 kebab-case（连字符）
- 示例: `differential-manifold.md`, `Orlicz-space.md`, `inner-product.md`

---

## 3. 写作业流程

### 典型工作流
1. **Obsidian 中做笔记** - 用 Markdown + LaTeX 记录推导过程
2. **导出为 LaTeX** - 从 Obsidian 导出或手动创建 `.tex` 文件
3. **编译 PDF** - 使用 `latexmk` 或 `xelatex`
4. **清理构建文件** - `.aux`, `.log`, `.toc` 等加入 `.gitignore`

### 作业目录结构
```
homework/
├── Orlicz-space.md      # Obsidian 笔记
├── Orlicz-space.tex     # 导出/手写的 LaTeX
├── Orlicz-space.pdf     # 编译后的 PDF
└── includes/            # 构建产物（gitignored）
    ├── Orlicz-space.aux
    ├── Orlicz-space.log
    └── ...
```

---

## 4. LaTeX 习惯

### 文档类
```latex
\documentclass{amsart}
```

### 常用宏包
- 数学: `amsmath`, `mathtools`, `amsthm`, `amssymb`, `bbm`, `mathrsfs`
- 图形: `graphicx`, `float`, `tikz`, `tikz-cd`, `pgfplots`, `mdframed`
- 列表: `enumitem`
- 字体: `xeCJK`（设置 `Noto Serif CJK SC`）
- 引用: `cleveref`

### 定理环境
```latex
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheoremlemma}[theorem]{Lemma}
\newtheoremCorollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

\theoremstyleRemark}
\newtheorem remark}[theorem]{Remark}
```

### 图片路径
```latex
\graphicspath{{F:/iCloudDrive/iCloud~md~obsidian/2025-summer/figures/}}
```

### 作者信息
```latex
\author{乐绎华, Yue Yihua}
\address{中山大学, Sun Yat-sen University}
\email{yueyh@mail2.sysu.cn}
```

---

## 5. 笔记内容风格

### 数学推导
- 详细推导步骤，不省略中间环节
- 使用 align 环境进行多行公式对齐
- 常用 `\begin{aligned} ... \end{aligned}`

### 例子
```markdown
> [!EXAMPLE] $\mathbb{P}^{n}$
> ![[1-differential-manifold-2025071022.png]]
> ![[2-differential-manifold-2025071022.png]]
```

### 定义
```markdown
> [!def] **Regular Surface**
> A subset $S \subset \mathbb{R}^3$ is called a **regular surface** if ...
```

---

## 6. Obsidian 配置

### 插件
- `obsidian-latex-suite` - LaTeX 快捷输入
- `math-booster` - 数学增强
- `easy-typing-obsidian` - 写作增强
- `AttachFlow` - 附件管理
- `better-export-pdf` - PDF 导出

### 字体设置
- 等宽字体: `Cascadia Code`, `Fira Code`, `LXGW Wenkai Mono`

---

## 7. 习惯总结

| 方面 | 习惯 |
|------|------|
| 笔记格式 | Markdown + LaTeX |
| 工具链 | Obsidian → LaTeX → PDF |
| 目录组织 | 按学科主题分类 |
| 作业流程 | md笔记 → tex导出 → 编译PDF |
| 定理环境 | amsart + 自定义定理样式 |
| 图片引用 | Obsidian 内部链接语法 |
| 构建管理 | gitignore 排除 .aux/.log/.toc |
