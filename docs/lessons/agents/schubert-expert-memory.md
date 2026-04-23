# Schubert 演算专家教训记忆

**适用对象**: schubert-expert
**最后更新**: 2026-03-31

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L501 | Schubert 多项式符号约定 | 1 |
| L502 | Bruhat 顺序的表示 | 1 |
| L503 | 文献引用标注规范 | 1 |
| L504 | $I(\tau)$ 公式必须核对原论文 | 1 |
| L505 | Schubert 笔记排版——长公式必须拆解 | 1 |
| L506 | Schubert 多项式符号强制约定 | 1 |
| L507 | 多项式变量必须用 `\mathbf` 和下划线格式 | 1 |
| L508 | grep 模式匹配中的反斜杠转义陷阱 | 1 |
| L509 | sed 替换破坏文件换行结构 | 1 |
| L510 | Team Lead 不应擅自派活 | 1 |
| L511 | 第一次出现的概念必须补充定义 | 1 |
| L512 | Chapter 5 量子双重 Schubert 符号规范 | 1 |
| L513 | rewrite chapter 导致 qa.tex 1300 行内容被删除 | 1 |
| L514 | Chapter 8 Billey 定理与 Pipe Dreams 符号规范 | 1 |

---

## L512: Chapter 5 量子双重 Schubert 符号规范

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
Chapter 5 中 `x; y` 写成裸变量而非 `\mathbf{x}; \mathbf{y}`，如 `\mathfrak{S}_u(x; y)` 而不是 `\mathfrak{S}_u(\mathbf{x}; \mathbf{y})`。

**正确做法**:
```latex
% 错误 ❌
\mathfrak{S}_u(x; y) \cdot \mathfrak{S}_v(x; z)

% 正确 ✅
\mathfrak{S}_u(\mathbf{x}; \mathbf{y}) \cdot \mathfrak{S}_v(\mathbf{x}; \mathbf{z})
```

**符号强制规范（L506 补充）**:
| 类型 | 正确写法 | 禁止 |
|------|----------|------|
| 单重 Schubert | `\mathfrak{S}_u(\mathbf{x})` | `S_w(x)`, `S_u(x)` |
| 双重 Schubert | `\mathfrak{S}_w(\mathbf{x}; \mathbf{y})` | `S_w(x;y)` |
| 三重 Schubert | `\mathfrak{S}_w(\mathbf{x}; \mathbf{y}; \mathbf{z})` | 任何不带 `\mathfrak` 的写法 |
| 量子参数 | `q_k`（下标） | `q1`, `qk` |
| 变量下标 | `x_1`, `y_2`（下划线） | `x1`, `y2`（无下划线） |

**检查命令**:
```bash
grep -n "S_[a-z](" notes/Schubert-Polynomials/chapters/chapter*.tex
grep -n "\\mathfrak{S}_[a-z_]*{[^}]*}[^;]*;" notes/Schubert-Polynomials/chapters/chapter*.tex
```

**防止措施**:
- 写多项式前先检查符号规范表
- 每次编译后用 grep 抽查
- 经验教训：参考 schubert-expert-memory.md 中的符号规范（L506, L507）

---

## L501: Schubert 多项式符号约定

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了 Schubert 多项式的不同符号风格。

**正确做法**:
```latex
% Schubert 多项式
\mathfrak{S}_w  % 标准符号
S_w  % 简写（需说明）
% Schubert cell
X_w^\circ  % 开胞
X_w  % 闭包
```

**引用来源**:
- Macdonald - Schubert Polynomials
- Fulton - Young Tableaux

**防止措施**:
- 明确说明符号来源
- 引用原文献编号

---

## L502: Bruhat 顺序的表示

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
Bruhat 顺序符号不一致。

**正确做法**:
```latex
% Bruhat 顺序
u \leq w  % 偏序关系
u < w  % 严格不等（差一个 inversion）
\ell(w)  % w 的长度（inversions 个数）

% 性质：u \leq w 当且仅当每个 k 都有 u_k \leq w_k
```

**记忆方法**:
- $\leq$ 表示可以通过向右移动到达
- 长度 = inversion 个数

**防止措施**:
- 写 Bruhat 顺序时注明长度函数

---

## L503: 文献引用标注规范

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
Lemma/Theorem/Corollary 环境中的定理引用缺少原文献编号标注。

**正确做法**:
```latex
% 正确格式：定理名 + 原文编号 + \cite{}
\begin{Lemma}[Lemma 2.2 {\cite[ Lemma 2.2]{GX2025}}]
\label{def:Lemma22}
...
\end{Lemma}

% Theorem 格式
\begin{Theorem}[Graham Positivity Theorem {\cite[ Theorem 3.2]{Gr}}]
\label{def:GrahamPositivity}
...
\end{Theorem}

% Corollary 格式
\begin{Corollary}[Corollary 1.2: Kirillov 猜想 {\cite[Conjecture 1]{kirillov2007}}]
\label{cor:Kirillov}
...
\end{Corollary}
```

**引用规范清单**:
| 定理类型 | 格式要求 |
|----------|----------|
| Lemma | `\begin{Lemma}[Lemma X.Y {\cite[ Lemma X.Y]{KEY}}]` |
| Theorem | `\begin{Theorem}[名称 {\cite[ Theorem X.Y]{KEY}}]` |
| Corollary | `\begin{Corollary}[名称 {\cite[ Corollary X.Y]{KEY}}]` |
| Proposition | `\begin{Proposition}[名称 {\cite[ Proposition X.Y]{KEY}}]` |

**常见引用 key**:
- `GX2025` — Gao & Xiong (2025) - Triple Schubert Positivity
- `Sa` — Samuel (2024) - Molev-Sagan Formula
- `KM` — Kirillov & Maeno (1996) - Quantum Double Schubert
- `Gr` — Graham (2001) - Positivity in Equivariant Schubert Calculus
- `anderson2023` — Anderson & Fulton - Equivariant Cohomology

**防止措施**:
- 每次写 Lemma/Theorem/Corollary 前，先确认原文献编号
- 用 grep 检查是否有遗漏引用

---

## 领域专属符号表

```latex
% Schubert 演算核心符号
Flag Variety: Fl_n(\mathbb{C})
Schubert 多项式: \mathfrak{S}_w
Bruhat 顺序: u \leq w
长度函数: \ell(w)
Schubert 细胞: X_w^\circ
Stanley 对称函数: F_y
Grothendieck 多项式: \mathfrak{G}_w
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/schubert-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是 Schubert 专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认

---

## L504: $I(\tau)$ 公式必须核对原论文

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
schubert-expert-3 将 $I(\tau) = \{y_j - t_i\}$ 误认为是置换 $\tau$ 的普通反转集，实际上这是 GX2025 论文中专门定义的集合，用于限定展开系数的多项式结构。

**正确做法**:
- 论文中定义的特殊集合（如 $I(\tau)$）有专门含义，不能望文生义
- 发现疑似错误的公式时，先查阅原始论文确认
- GX2025 原文明确给出 $I(\tau) = \{y_j - t_i \mid 1 \leq i,j \leq n\}$

**论文位置**:
`PDFs/quantum-schubert/GaoXiong-TripleSchubertPositivity.pdf`

**防止措施**:
- 任何核心公式先查原文
- 笔记引用 ≠ 原创，发现存疑立即核实

---

## L505: Schubert 笔记排版——长公式必须拆解

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
在 qa.tex 中，一个涉及 Schubert 类相交的链式表达公式太长（87.9pt overfull）：
```latex
$$\overline{B^-uB/B} \cap \overline{B^-vB/B} \xrightarrow{\text{横截性}} \text{良定义的交点数} \xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w$$
```

**正确做法**:
```latex
\begin{align}
\overline{B^-uB/B} \cap \overline{B^-vB/B}
&\xrightarrow{\text{横截性}} \text{良定义的交点数} \label{eq:geo-to-integer} \\
&\xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \label{eq:integer-to-cohomology} \\
&\xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w \label{eq:cohomology-to-polynomial}
\end{align}
```

**Schubert 笔记排版高危模式**:
1. 涉及 Schubert 细胞闭包 $\overline{B^-wB/B}$ 的相交表达式
2. 涉及 $\xrightarrow{\text{...}}$ 链式翻译
3. 涉及 $\sum_w$ 多重求和

**检查命令**:
```bash
# 编译后立即检查 overfull hbox
grep -i "overfull\|hbox" schubert-positivity-notes.log
```

**修复记录**:
- 87.9pt too wide (line 1030) → 用 align 拆解为 3 行 ✅

**防止措施**:
- 写完长公式后立即编译检查
- 涉及 Schubert 类的复杂表达式优先用 align 拆解

---

## L506: Schubert 多项式符号强制约定

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
用户指出笔记中存在 `S_w(x)` 这种不规范的写法——既没有 `\mathfrak`，也没有 `\mathbf`。

**正确做法**:
```latex
% 一重 Schubert 多项式（单变量集）
\mathfrak{S}_u(\mathbf{x})    % ✅ 正确
\mathfrak{S}_w(\mathbf{x})    % ✅ 正确

% 二重 Schubert 多项式（双变量集）
\mathfrak{S}_w(\mathbf{x}; \mathbf{y})  % ✅ 正确

% 禁止以下写法：
S_w(x)    % ❌ 没有 mathfrak
S_w(\mathbf{x})  % ❌ 没有 mathfrak
\mathfrak{S}_w(x)  % ❌ x 应该是 \mathbf{x}
```

**符号规范清单**:
| 类型 | 正确写法 | 禁止 |
|------|----------|------|
| 单重 Schubert | `\mathfrak{S}_u(\mathbf{x})` | `S_w(x)`, `S_u(x)` |
| 双重 Schubert | `\mathfrak{S}_w(\mathbf{x}; \mathbf{y})` | `S_w(x;y)` |
| 三重 Schubert | `\mathfrak{S}_w(\mathbf{x}; \mathbf{y}; \mathbf{z})` | 任何不带 `\mathfrak` 的写法 |

**检查命令**:
```bash
# 检查是否有 S_ 开头的不规范写法
grep -n "S_[a-z](" notes/Schubert-Polynomials/chapters/chapter*.tex
```

**教训**:
- 检查其他章节（chapter2-4）是否有类似问题
- 发现后立即修正

---

## L507: 多项式变量必须用 `\mathbf` 和下划线格式

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
在展开式中使用 `x1x2` 而不是正确的 LaTeX 格式 `x_1 x_2`，以及使用 `S_231(x; y)` 而不是 `\mathfrak{S}_{231}(\mathbf{x}; \mathbf{y})`。

**正确做法**:
```latex
% 错误 ❌
S_231(x; y) = x1x2 - x1y3 - x2y3 + y2y3

% 正确 ✅
\mathfrak{S}_{231}(\mathbf{x}; \mathbf{y}) = x_1 x_2 - x_1 y_3 - x_2 y_3 + y_2 y_3
```

**符号检查清单**:
1. `S_` → `\mathfrak{S}_`
2. `x1` → `x_1`（使用下划线）
3. `x;y` → `\mathbf{x}; \mathbf{y}`
4. 乘积 `x1x2` → `x_1 x_2`（变量之间加空格）

**修复记录**:
- Line 364: `S_{21}(x; y)` → `\mathfrak{S}_{21}(\mathbf{x}; \mathbf{y})` ✅
- 所有 `x_1x_2` → `x_1 x_2` ✅
- 所有 `x_1y_3` → `x_1 y_3` ✅

**防止措施**:
- 写多项式时立即检查下划线格式
- 编译后用 grep 检查是否有遗漏的格式问题

---

## L508: grep 模式匹配中的反斜杠转义陷阱

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
尝试用 `grep -n '\\b\\b\\b' qa.tex` 查找字面上的 `\b\b\b` 字符串（退格字符的文本表示），但 grep 找不到任何匹配。

**根因分析**:
1. `\b` 在正则表达式中是**退格符**（ASCII 8），不是字面上的反斜杠+b
2. 用 `grep '\\b\\b\\b'` 实际匹配的是三个连续的退格字符，而不是字面字符串 `\b\b\b`
3. 文件中实际的字符串是 `\b\b\b`（四个字符：反斜杠、b、反斜杠、b、反斜杠、b）

**正确做法**:
```bash
# 方法1: 使用 -F (fixed string) 避免正则转义
grep -nF '\b\b\b' qa.tex

# 方法2: 使用 xxd 查看原始字节确认内容
sed -n '66p' qa.tex | xxd

# 方法3: 直接 sed 替换（不需要正则）
sed -i '' 's/\\b\\b\\b\\begin{itemize}/\begin{itemize}/g' qa.tex
```

**教训**:
- 当文件内容是字面的反斜杠字符时，用 `xxd` 或 `od` 确认原始字节
- 用 `-F` 选项搜索固定字符串比转义正则更可靠
- grep 的 `\b` 是正则的单词边界，不是退格符

**防止措施**:
- 搜索特殊字符前先用 `xxd` 确认内容
- 搜索反斜杠时用 `-F` 选项或 `grep -E` 加双反斜杠

---

## L509: sed 替换破坏文件换行结构

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
执行 `sed -i '' 's/\\b\\b\\b\\begin{itemize}/\begin{itemize}/g' qa.tex` 后，文件的所有换行被错误地移除，导致整个文件变成单行使后续编辑无法进行。

**根因分析**:
1. sed 替换命令中的 `s/old/new/g` 中的 `g` 是全局替换标志，本身不会影响换行
2. 但当替换模式与原文件中的多行内容交叉时，可能导致行合并
3. 更可能的原因：文件中 `\b\b\b` 实际跨越了换行符边界，或者 `\begin` 前后的换行被错误匹配

**正确做法**:
```bash
# 方法1: 先确认文件状态（用 wc -l 检查行数）
wc -l qa.tex  # 替换前记录

# 方法2: 用 perl 进行更精确的替换
perl -i -pe 's/\\b\\b\\b\\begin{itemize}/\begin{itemize}/g' qa.tex
perl -i -pe 's/\\e\\\\end{itemize}/\end{itemize}/g' qa.tex

# 方法3: 备份后编辑
cp qa.tex qa.tex.bak
sed -i '' '...' qa.tex
diff qa.tex qa.tex.bak  # 检查差异
```

**教训**:
- sed 的 `g` 替换不会自动去除换行，但替换模式可能意外匹配跨行内容
- 大规模替换前必须备份原文件
- 替换后立即检查 `wc -l` 确认行数没有异常变化

**防止措施**:
- 替换前备份文件
- 替换后立即 `wc -l` 验证行数
- 如果行数异常，用版本控制（git）恢复后再尝试更精确的替换方式

---

## L511: 第一次出现的概念必须补充定义

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
在正文中第一次引入某个数学概念（如 $\overline{\mathcal{M}}_{0,3}(X,d)$）时，没有同时给出定义，导致读者需要翻阅后才能理解。

**正确做法**:
1. **首次出现时添加脚注**：在概念首次出现的位置添加 `\footnote{问：[概念名称] 是什么？见附录 \cref{sec:qa-xxx}。}`
2. **在 qa.tex 中添加定义**：在附录中添加该概念的详细解释
3. **确保脚注包含问题文本**：脚注格式必须是"问：XXX是什么？见附录 \cref{sec:...}。"

**示例**:
```latex
% 错误 ❌
通过投影公式，将 $\overline{\mathcal{M}}_{0,3}(X,d)$ 上的曲线计数问题归约到...

% 正确 ✅
通过投影公式，将 $\overline{\mathcal{M}}_{0,3}(X,d)$\footnote{问：$\overline{\mathcal{M}}_{0,3}(X,d)$ 是什么？见附录 \cref{sec:MOD-space}。} 上的曲线计数问题归约到...
```

**Schubert 演算中常见需要首次定义的对象**:
- $\overline{\mathcal{M}}_{0,3}(X,d)$：稳定映射模空间
- $H_T^*(pt)$：torus 等变上同调
- $\Lambda[q]$：分次多项式环
- $\sigma(w)^T$：等变 Schubert 类
- Gromov-Witten 不变量
- $QH_T^*(X)$：等变量子量子上同调

**防止措施**:
- 写完章节后，用 grep 检查所有数学符号是否在首次出现时有脚注定义
- 检查命令：`grep -n "\\\$.*\\\$.*\$" chapters/chapter*.tex`（查找行内数学表达式）
- 原则：宁可多给一个定义，也不能让读者困惑

---

## L513: rewrite chapter 导致 qa.tex 1300 行内容被删除

**日期**: 2026-04-08
**经历次数**: 1 次 (累计)

**错误描述**:
commit `7aee6ae07`（chore: update chapter5）重写 chapter5 时，意外将 qa.tex 从 1875 行压缩到 566 行，删除了 28 个精心撰写的 QA 条目（1309 行）。

**事故链条**:
1. `dfd5d29b5` — qa.tex 已有 1875 行，包含 28 个 QA 条目
2. `7aee6ae07` — update chapter5 时，agent 对 qa.tex 做了大幅重写
3. 结果：qa.tex 变成 566 行，删除了 1309 行内容

**被删内容清单**（28 个 QA 条目）:
- EQLR 系数的定义与意义
- Skew 除差算子与除差算子的关系
- 逆除差算子的定义
- 双重与三重 Schubert 多项式的区别
- 等变量子上同调类的定义
- Lascoux-Schützenberger 型代表元
- ET 为什么是奇数维球面的极限
- Torus 作用与分类空间 ET
- 等变量子上同调与量子同调的区别
- Hilbert 第十五问题与 Schubert 演算
- $S_\infty$ 的例子
- 量子上同调的定义
- Theorem 1.1 的例子：Triple Schubert Positivity
- Theorem 1.1 如何推出 Corollary 1.2
- Knutson-Tao (2003) 展开系数的几何意义
- Gao-Xiong 与 Knutson-Tao 解释的不同
- Graham Positivity 中 Grassmannian 限制的作用
- Littlewood-Richardson 系数为何非负
- 什么是 Schur 函数
- Graham Positivity 中展开系数的"非负性"含义
- 第一章第三节的定理脉络
- 几何相交如何翻译为代数展开系数
- Graham 定理为何依赖几何性质
- $B^-(w)$ 与 $B^-$ 的关系
- $\mathbb{N}[-\alpha]_{\alpha \in I(w)}$ 的含义
- ... 等等

**恢复方法**:
```bash
git show dfd5d29b5:notes/Schubert-Polynomials/appendix/qa.tex > notes/Schubert-Polynomials/appendix/qa.tex
```

**教训**:
1. **qa.tex 是高价值内容库** — rewrite 章节内容前，必须先 `git diff` 检查 qa.tex 状态
2. **rewrite 时用 grep 确认** — 搜所有 .tex 文件中对新内容的引用，确保没有遗漏
3. **commit 前必须确认** — `git diff` 只改了你意图改的文件
4. **qa.tex 应有独立 commit** — 不应与其他章节内容混在同一个 commit

**防止措施**:
- 每次 rewrite 章节前：
  1. `git status` 查看所有修改文件
  2. `wc -l` 确认 qa.tex 行数没有异常变化
  3. `git diff` 确认没有意外修改
- 每次 commit 后：
  1. 确认只改了目标文件
  2. 确认 qa.tex 行数没有大幅变化
