# LaTeX 检查专家教训记忆

**适用对象**: latex-checker
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L901 | Markdown 残留检查 | 2 |
| L902 | \bm 命令禁用检查 | 1 |
| L903 | Label/Ref 一致性检查 | 1 |
| L904 | Theorem 环境禁止 itemize | 1 |
| L905 | theorem 环境 \\begin/\\end 格式检查 | 1 |
| L906 | Overfull Hbox 排版问题检查 | 1 |
| L907 | 表格统一用三线表格式，禁止 resizebox | 1 |
| L908 | 中文引号规范检查 | 1 |
| L909 | 公式引用必须用 \cref 而非 \tag/式(★) | 1 |

---

## L906: Overfull Hbox 排版问题检查

**日期**: 2026-03-30
**经历次数**: 1 次

**错误描述**:
编译日志出现 `Overfull \hbox (Xpt too wide)` 警告，表示有内容超出页面边界。

**常见原因及修复**:
1. **超长公式（最常见）**: 用 `align`/`aligned` 环境拆解单行公式
2. **URL 太长**: 用 `\url{}` 包起来，或用 `\href{}{}` 缩短显示
3. **表格过宽**: 用 `resizebox` 或调整列宽
4. **itemize 内容过长**: 缩短文本或调整 `\setlength\itemsep{0pt}`

**检查命令**:
```bash
# 编译后检查 overfull hbox
grep -i "overfull\|hbox" schubert-positivity-notes.log

# 示例输出
# Overfull \hbox (96.06676pt too wide) in paragraph at lines 87--88
# Overfull \hbox (4.48712pt too wide) in paragraph at lines 689--690
# Overfull \hbox (87.8959pt too wide) detected at line 1030
```

**修复示例**:
```latex
% 错误 ❌：单行超长公式
$$\overline{B^-uB/B} \cap \overline{B^-vB/B} \xrightarrow{\text{横截性}} \text{良定义的交点数} \xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w$$

% 正确 ✅：拆解为 align 多行
\begin{align}
\overline{B^-uB/B} \cap \overline{B^-vB/B}
&\xrightarrow{\text{横截性}} \text{良定义的交点数} \label{eq:geo-to-integer} \\
&\xrightarrow{\text{Corollary 2.4}} \sum_w c^w_{u,v} \cdot [\overline{B^-wB/B}]_T \label{eq:integer-to-cohomology} \\
&\xrightarrow{\text{多项式代表元}} \mathfrak{S}_u \cdot \mathfrak{S}_v = \sum_w c^w_{u,v} \cdot \mathfrak{S}_w \label{eq:cohomology-to-polynomial}
\end{align}
```

**禁止使用的 hack**:
- ❌ `\sloppy`
- ❌ `\emergencystretch`
- ❌ 手动调整 `\textheight` 或 `\oddsidemargin`

**防止措施**:
- 每次编译后检查日志中的 `Overfull \hbox` 警告
- 超长公式立即拆解，不要留到后期
- 涉及 Schubert 类相交的长表达式特别容易超宽，优先拆分

---

## L905: theorem 环境 \begin/\end 格式检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
subagent 生成的 chapter5.tex 中，theorem 环境写成了 `\begin theorem}` 和 `\end theorem}` —— 中间有空格或缺少 `{`/`}`。

**正确做法**:
```latex
% 错误 ❌
\begin theorem}[...]
\end theorem}

% 正确 ✅
\begin theorem}[...]
\end theorem}
```

检查命令:
```bash
grep -n "begin theorem\|end theorem" notes/**/*.tex
# 或检查空格
grep -n "\\\\end theorem\}" notes/**/*.tex
```

**修复方法**:
```python
# Python 修复脚本
content = content.replace('\\{', '{')
content = content.replace('\\}', '}')
```

**防止措施**:
- 每次生成后立即检查 theorem 环境闭合: Markdown 残留检查

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
在 .tex 文件中发现了 Markdown 格式残留。

**检查命令**:
```bash
# 检查 Markdown 残留
grep -E '\*\*|\* -|^\>' notes/**/*.tex
# 或者
grep -n '\textbf{\underline{' notes/**/*.tex
```

**常见残留模式**:
```latex
% 加粗残留
**text**  →  \textbf{text}

% 斜体残留
*text*  →  \textit{text}

% 列表残留
- item  →  \item（需要 enumerate 环境）

% Callout 残留
> [!note]  →  \begin{note}...\end{note}
```

**防止措施**:
- 润色后立即检查
- 用脚本批量检测残留

---

## L902: \bm 命令禁用检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
使用了禁止的 `\bm{}` 命令。

**正确做法**:
```latex
% 错误 ❌
\bm{x}, \bm{\beta}, \bm{A}

% 正确 ✅
\mathbf{x}  % 向量
\boldsymbol{\beta}  % 矩阵
```

**检查命令**:
```bash
grep -n '\\\\bm{' notes/**/*.tex
```

**防止措施**:
- 记住：`\bm` 是禁止的
- 提示用户修正

---

## L903: Label/Ref 一致性检查

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
存在 `\ref{}` 或 `\cref{}` 引用了不存在的 label。

**检查方法**:
1. 提取所有 `\label{...}`
2. 提取所有 `\ref{...}` 和 `\cref{...}`
3. 核对引用是否有对应定义

**常见错误**:
```latex
% label 定义了但没用
\label{eq:balance-discrete-CRE}  % 定义了

% 引用时拼写错误
\eqref{eq:balance-discrete-CER}  % 拼写错误！

% ref 类型错误
\ref{fig:xxx}  % 应该是 \cref{fig:xxx}
```

**防止措施**:
- 编译检查警告
- 用脚本验证 label-ref 一致性

---

## L904: Theorem 环境禁止 itemize

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
在 Theorem/Definition 环境内使用了 itemize 列表。

**正确做法**:
```latex
% 错误 ❌
\begin{Theorem}
\begin{itemize}
\item 第一点
\item 第二点
\end{itemize}
\end{Theorem}

% 正确 ✅
\begin{Theorem}
条件如下：
\begin{enumerate}
\item 第一点
\item 第二点
\end{enumerate}
\end{Theorem}
```

**或者用纯叙述**:
```latex
\begin{Theorem}
If $X$ is normally distributed with mean $\mu$ and variance $\sigma^2$,
then the sample mean $\bar{X}$ satisfies......
\end{Theorem}
```

**防止措施**:
- Theorem 内用自然段落叙述
- 如需列表，用 enumerate 环境

---

## L907: 表格统一用三线表格式，禁止 resizebox

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
使用 `resizebox{\textwidth}{!}{...}` 让表格缩放到页面宽度，这会让表格看起来很奇怪、比例失调。

**正确做法**:
使用标准的 `\hline` 三线表，不使用 resizebox：
```latex
% 正确 ✅
\begin{center}
\begin{tabular}{ccllc}
$w$ & 一行数组 & Lehmer 码 & $\ell(w)$ & $\mathfrak{S}_w(\mathbf{x})$ \\
\hline
$123$ & $(1,2,3)$ & $(0,0,0)$ & $0$ & $1$ \\
$213$ & $(2,1,3)$ & $(1,0,0)$ & $1$ & $x_1$ \\
...
\end{tabular}
\end{center}

% 错误 ❌
\resizebox{\textwidth}{!}{\begin{tabular}...}
```

**三线表标准格式**:
1. 表格用 `center` 环境包裹
2. 使用 `\hline` 画横线（只有顶部、底部两条）
3. 不使用竖线
4. 列对齐用 `c`（居中）、`l`（左）、`r`（右）

**防止措施**:
- 禁止使用 `resizebox` 缩放表格
- 如果表格太宽，考虑调整列宽或减少列数，而不是缩放

---

## L908: 中文引号规范检查

**日期**: 2026-03-30
**经历次数**: 1 次 (累计)

**错误描述**:
中文引号 `"..."` 在 LaTeX 中不会自动转换为中文引号，需要使用 `` '' ` 来表示中文左引号""和右引号。

**正确做法**:
```latex
% 错误 ❌
中文引号"分离"模式

% 正确 ✅
中文引号``分离''模式
```

**渲染效果**:
- ` `` ` → " (左双引号)
- `''` → " (右双引号)
- ` `' ` → ' (左单引号)
- `'` → ' (右单引号)

**检查命令**:
```bash
# 检查是否有中文引号残留
grep -n '[""'']' notes/**/*.tex
```

**防止措施**:
- 写作时直接使用正确格式
- 润色后用检查命令验证

---

## L909: 公式引用必须用 \cref 而非 \tag/式(★)

**日期**: 2026-03-30
**经历次数**: 1 次

**错误描述**:
正文引用公式时使用了 `式 (★★)` 而不是 `\cref{eq:label}`，或者用 `\tag{}` 自定义标签。

**正确做法**:
```latex
% 错误 ❌
将这一结论代入式 (★★)，得到
$$\partial_{w/v}(\mathfrak{S}_u(\mathbf{x})) = ...$$

% 正确 ✅
将这一结论代入 \cref{eq:skew-divided-diff-zero}，得到
$$\partial_{w/v}(\mathfrak{S}_u(\mathbf{x})) = ... \label{eq:skew-divided-diff-zero}$$
```

**命名规范**:
- 公式用 `\label{eq:描述性名称}` 定义
- 引用时用 `\cref{eq:描述性名称}`（自动判断类型）
- 不要用 `\tag{}` 自定义数字/符号标签

**检查命令**:
```bash
# 检查是否有式 (★) 残留
grep -n '式 (★)\|式 (★★)' notes/**/*.tex

# 检查是否有 \tag{} 残留
grep -n 'tag\*{' notes/**/*.tex
```

**防止措施**:
- 定义公式时立即加上 `\label{eq:...}`
- 引用时用 `\cref{eq:...}` 代替手写"式 (X)"
- 编译检查 cross-reference 警告

---

## L910: Equivariant Quantum Schubert Calculus 术语规范

**日期**: 2026-03-31
**经历次数**: 2 次 (累计)

**错误描述**:
错误地将 "Equivariant Quantum Schubert Calculus" 翻译为"等变量子量子上同调"。

**正确术语**:
```latex
% 错误 ❌
等变量子量子上同调

% 正确 ✅
等变量子上同调中的量子 Schubert 演算
```

**术语体系**:
| 英文 | 中文 |
|------|------|
| equivariant cohomology | 等变量子上同调 |
| quantum cohomology | 量子上同调 |
| Equivariant Quantum Schubert Calculus | 等变量子上同调中的量子 Schubert 演算 |

**检查命令**:
```bash
grep -n "等变量子量子上同调\|等变量量子上同调" notes/Schubert-Polynomials/chapters/*.tex
```

**防止措施**:
- 这是论文标题，应整体翻译为"等变量子上同调中的量子 Schubert 演算"
- 不要拆分为"等变量子量子上同调"

---

## L911: equivariant cohomology = 等变上同调

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
错误地将 "equivariant cohomology" 翻译为"等变量子上同调"。

**正确术语**:
```latex
% 错误 ❌
等变量子上同调（equivariant cohomology）

% 正确 ✅
等变上同调
```

**术语体系**:
| 英文 | 中文 |
|------|------|
| equivariant cohomology | 等变上同调 |
| quantum cohomology | 量子上同调 |
| Equivariant Quantum Schubert Calculus | 等变量子上同调中的量子 Schubert 演算 |

**防止措施**:
- "equivariant" 简称"等变"，不是"等变量"
- 第三种情形应称为"等变量子上同调中的量子 Schubert 演算"，不是"量子化等变上同调"

---

## 核心检查清单

- [ ] 无 Markdown 残留（`**`、`*`、`-`、`>`）
- [ ] 无 `\bm{}` 命令
- [ ] 所有 `\ref{}`/`\cref{}` 都有对应 `\label{}`
- [ ] Theorem 环境内无 itemize
- [ ] 推导都在附录，正文有 `\footnote{}` 引用
- [ ] 符号约定一致
- [ ] 中文引号使用 `` '' `` 格式

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/latex-checker-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是 LaTeX 检查专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
