# CLAUDE.md — peng-ding-causal

> 丁鹏《A First Course in Causal Inference》教材 tex 源码

## 模板环境

### 证明环境 `myproof`

```tex
\begin{myproof}{Theorem}{\ref{eq:xxx}}
证明内容...
\end{myproof}
```

参数1：被证明对象的类型（Theorem / Lemma / Corollary 等）
参数2：被证明对象的 label 引用
结尾自动加 $\square$（黑色实心方块）

### 解答环境 `mysolution`（模板已定义但正文未使用）

```tex
\begin{mysolution}{Problem #1}
解答内容...
\end{mysolution}
```

### 定理类环境

直接使用，无需额外声明：

| 环境 | 计数器 |
|------|--------|
| `lemma` | lemma |
| `proposition` | proposition |
| `corollary` | corollary |
| `assumption` | assumption |
| `remark` | remark |
| `condition` | condition |

```tex
\begin lemma}\label lem:xxx}
...
\end lemma}
```

## 编译

```bash
./compile.sh
```

三次 xelatex + 一次 bibtex，确保引用和交叉引用正确。

## 目录结构

```
peng-ding-causal/
├── Causalinference.tex          # 主入口
├── causal.bib                   # 参考文献
├── krantz.cls                   # 出版社类文件
├── compile.sh                   # 编译脚本
├── chapters/                    # 各章 tex
├── figures/                     # 图片
└── frontmatter/                 # 前言、符号表等
```
