# 多文献学习工作流 - 记忆

## 项目概述
- 主题：Schubert 多项式的 Positivity 问题
- 目标：尝试证明 Gao & Xiong 结果的量子版本

## 8篇文献

### 核心文献 (4篇 - Schubert)
1. **GaoXiong-TripleSchubertPositivity.pdf** - Graham Positivity of Triple Schubert Calculus (2025, 6页)
2. **MolevSagan-Formula-DoubleSchubert.pdf** - Molev-Sagan Type Formula (2024, 30页)
3. **KirillovMaeno-QuantumDoubleSchubert.pdf** - Quantum Double Schubert (1996, 52页)
4. **Mihalcea-QuantumSchubertPositivity.pdf** - Quantum Schubert Positivity (约2007, 15页)

### 参考书籍
- Anderson & Fulton - Equivariant Cohomology in Algebraic Geometry
- Li (2023) - Schubert Calculus: A Brief Introduction
- Li (2023) - Certain Identities on the Quantum Product of Schubert Classes
- Buch (2001) - Quantum Cohomology of Grassmannians

## 讲义结构

### 目录结构
```
notes/Schubert-Polynomials/
├── schubert-positivity-notes.tex  # 主文件
├── compile.sh                      # 编译脚本
├── references.bib                  # BibTeX 引用
├── chapters/
│   ├── chapter0.tex               # 文献概述
│   └── chapter1.tex               # GaoXiong 论文
└── appendix/
    └── qa.tex                     # 问答记录
```

### 命名规范
- 主文件：`<主题>-notes.tex`，如 `schubert-positivity-notes.tex`
- 不要用 `main.tex`

### LaTeX 模板

**compile.sh:**
```bash
#!/bin/bash
FILE="schubert-positivity-notes"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 运行 BibTeX ==="
bibtex ${FILE}.aux

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== 编译完成 ==="
ls -la ${FILE}.pdf
```

**主文件 (amsbook):**
- 使用 amsbook 文档类
- Theorem style: `\theoremstyle{definition}` (加粗左对齐)
- 使用 BibTeX 管理引用
- 定理环境独立计数器：`[chapter]`

### 格式规范

**Label 和引用：**
- 格式：\label{name}，如 `\label{def:名称}`
- 引用：\cref{name}，需要 cleveref 宏包

**句号格式：**
- 英文句点 + 空格："... ."

**脚注：**
- 使用 \footnote{} 添加说明

**定理环境：**
- 关键词加粗左对齐，使用 definition style

## 学习流程

1. **先有 Chapter 0**：介绍所有文献的主要信息
2. **文献引用**：首次出现的概念要引用原文位置
3. **QA 记录**：问答记录放在 appendix/qa.tex
4. **用户注解**：使用 \userannotation 命令

## QA 内容 (已补充)

1. Skew 除差算子与除差算子的关系（含 n=3, n=4 例子）
2. 逆除差算子的定义
3. 等变量子上同调类的定义
4. Lascoux-Schützenberger 型代表元
5. 双重与三重 Schubert 多项式的区别

## 符号说明

- **$S_\infty$**：所有有限置换的并集，即 $\bigcup_{n=1}^\infty S_n$
