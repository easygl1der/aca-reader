# 习题专家指南 (Exercise Expert Guide)

**适用对象**: exercise-expert, exercise-expert-2, exercise-expert-3, exercise-expert-4
**最后更新**: 2026-04-08

---

## 一、角色定义

### 核心职责

1. **习题提取**：从教材（PDF/transcript）中识别并提取习题
2. **格式规范化**：按对应模板格式化为 LaTeX
3. **一体化生成**：知识点 + 习题同步生成，不分开两步
4. **标签校验**：确保 `\eqref{}` 引用正确

### 一体化工作流

当用户说"生成第X章笔记"时，**同时执行以下两步**：

**Part 1**: 生成章节知识点笔记
```
1. 读取对应章节的 arXiv tex 源文件（优先）或 transcript
2. 按模板格式生成笔记内容
3. 添加到 chapters/chapterX.tex
```

**Part 2**: 生成章节习题（自动执行，无需用户额外指令）
```
1. 从教材习题来源提取本章习题
2. 按模板格式格式化
3. 添加到章节末尾（在 %/ === 用户问答记录 ===% 之前）
4. 更新主文件 main.tex（如需要）
```

---

## 二、教材模板识别（优先级流程）

**核心原则**：先识别当前笔记 LaTeX 中**已定义的 exercise 环境**，再决定使用哪个。

### 识别流程

```
Step 1: 读取笔记的 LaTeX 主文件或 chapter 文件
        ↓
Step 2: 搜索 \begin{exercise} 或 \begin{Exercise}
        ↓
        ├─ 找到 \begin{exercise}（小写）
        │   → 使用 exercise 环境（小写）
        │
        ├─ 找到 \begin{Exercise}（大写）
        │   → 使用 Exercise 环境（大写）
        │
        └─ 都没找到
            ↓
Step 3: 检查 documentclass 和宏包定义
        ├─ book 类 + 无特殊定义 → Exercise（大写）
        └─ article 类 + 无特殊定义 → Exercise（大写）
```

### 支持的教材模板

| 教材 | 笔记位置 | 习题环境 | 标题格式 | 内容语言 |
|------|----------|----------|----------|----------|
| **do Carmo** | `notes/differential-geometry/do-carmo-curves-surfaces/` | `exercise`（小写） | `{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}` | 英文原文 |
| **Peng Ding** | `notes/A-First-Course-in-Causal-Inference/` | `Exercise`（大写） | `{\ref{标签} 英文标题}` | 中文描述 + `\eqref{}` 引用 |
| **其他教材** | 先检查笔记 LaTeX | **由笔记定义决定** | 同上 | 由笔记决定 |

**重要**：不要假设"其他教材都用大写 Exercise"。必须先读笔记 LaTeX，看它定义了哪个环境。

### 正确 vs 错误做法

```latex
% ❌ 错误：按目录名假设模板
notes/differential-geometry/ → exercise
notes/A-First-Course/ → Exercise
notes/其他/ → Exercise  % 不要这样假设！

% ✅ 正确：先读笔记 LaTeX 中的实际定义
% 读取 notes/其他教材/chapters/chapterX.tex
% 搜索 \begin{exercise} 或 \begin{Exercise}
% 使用笔记实际定义的环境
```

---

## 三、环境判断决策树

```
                    ┌─────────────────────────┐
                    │ 读取笔记 LaTeX 文件      │
                    └───────────┬─────────────┘
                                ↓
              ┌───────────────────────────────┐
              │ \begin{exercise} 存在？        │
              └───────────────┬───────────────┘
                    ┌─────────┴─────────┐
                    ↓                   ↓
                   是                  否
                    ↓                   ↓
              ┌─────────┐    ┌──────────────────────┐
              │exercise │    │ \begin{Exercise} 存在？│
              │(小写)   │    └──────────┬───────────┘
              └─────────┘       ┌────────┴────────┐
                                 ↓                 ↓
                                是                否
                                 ↓                 ↓
                          ┌──────────┐    ┌───────────────────┐
                          │Exercise  │    │检查 documentclass │
                          │(大写)    │    │和宏包定义         │
                          └──────────┘    └─────────┬─────────┘
                                          ┌─────────┴─────────┐
                                          ↓                   ↓
                                      有定义              无定义
                                          ↓                   ↓
                                    用定义的           用 Exercise(大写)
```

---

## 四、格式规范

### 4.1 do Carmo 模板（Book 模板）

#### 格式模板

```latex
\begin{exercise}{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}
习题内容原文（英文）。
\end{exercise}
```

#### 正确示例

```latex
\begin{exercise}{1-2, 1 — do Carmo, Exercise 1-2, 1}
Find a parametrized curve $\alpha(t)$ whose trace is the circle
$x^2 + y^2 = 1$ such that $\alpha(t)$ runs clockwise around
the circle with $\alpha(0) = (0, 1)$.
\end{exercise}
```

```latex
\begin{exercise}{1-3, 2 — do Carmo, Exercise 1-3, 2}
A circular disk of radius 1 in the plane $xy$ rolls without slipping
along the $x$ axis. The figure described by a point of the circumference
of the disk is called a cycloid (见 \cref{fig:cycloid}，教材 Figure 1-7)。
\begin{enumerate}
\item[a.] Obtain a parametrized curve $\alpha: \mathbb{R} \to \mathbb{R}^2$
the trace of which is the cycloid, and determine its singular points.
\item[b.] Compute the arc length of the cycloid corresponding to
a complete rotation of the disk.
\end{enumerate}
\end{exercise}
```

```latex
\begin{exercise}{1-4, 2* — do Carmo, Exercise 1-4, 2}
A plane $P$ contained in $\mathbb{R}^3$ is given by the equation
$ax + by + cz + d = 0$. Show that the vector $v = (a, b, c)$ is
perpendicular to the plane and that $|d| / \sqrt{a^2 + b^2 + c^2}$
measures the distance from the plane to the origin $(0, 0, 0)$.
\end{exercise}
```

#### 错误示例

❌ **错误：中文标题**
```latex
\begin{exercise}{1-2, 1 — do Carmo, 习题1-2, 1}  % 不要用中文
```

❌ **错误：缺少 do Carmo 引用**
```latex
\begin{exercise}{1-2, 1}  % 缺少来源
```

❌ **错误：footnote 格式**
```latex
\begin{exercise}{1-2, 1}\footnote{do Carmo, Exercise 1-2, 1}  % 不要用 footnote
```

#### 格式要点

| 要点 | 说明 |
|------|------|
| 环境名称 | `exercise`（小写） |
| 参数格式 | `{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}` |
| 内容语言 | 英文原文（直接引用教材） |
| 难题标记 | 题号后加 `*`，如 `{1-3, 8* — do Carmo, ...}` |
| 分部题目 | 使用 `enumerate` 环境 |
| 图片引用 | 使用 `\cref{fig:标签}` |

#### 公式格式

- **短公式**：行内公式 `$...$`
- **长公式**：行间公式 `\[ ... \]`
- **判断标准**：公式超过一行、或包含复杂分式/根号，应使用行间公式

#### 分部题目格式

```latex
\begin{exercise}{1-3, 3 — do Carmo, Exercise 1-3, 3}
Let $0A = 2a$ be the diameter of a circle $S^1$. Prove that:
\begin{enumerate}
\item[a.] The trace of $\alpha(t) = \left(\frac{2at^2}{1+t^2},
\frac{2at^3}{1+t^2}\right)$, $t \in \mathbb{R}$, is the cissoid
of Diocles (见 \cref{fig:cissoid}，教材 Figure 1-8).
\item[b.] The origin $(0,0)$ is a singular point of the cissoid.
\item[c.] As $t \to \infty$, $\alpha(t)$ approaches the line $x = 2a$ (asymptote).
\end{enumerate}
\end{exercise}
```

#### 分节练习标记

每个习题 section 结束后，用以下格式标记：

```latex
\subsection*{1-2 节练习}
```

---

### 4.2 Peng Ding 模板（因果推断）

#### 格式模板

```latex
\section{习题}\label{sec:chapter5-exercises}

\begin{Exercise}{\ref{exr:5-1} 英文标题}\label{exr:5-1}
习题内容（中英文均可，英文优先）。
\end{Exercise}
```

#### 正确示例

```latex
\begin{Exercise}{\ref{exr:5-1} Covariate balance in the CRE}\label{exr:5-1}
证明 \eqref{eq:balance-discrete-CRE}：在 CRE 下，
\[
\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right} = 0.
\]
\end{Exercise}
```

```latex
\begin{Exercise}{\ref{exr:5-3} Consequence of constant individual causal effects}\label{exr:5-3}
假设个体因果效应是常数 $\tau_i = \tau$（对所有 $i = 1, \ldots, n$）。考虑以下 $\tau$ 的加权估计量类：
\[
\hat\tau_w = \sum_{k=1}^K w_{[k]} \hat\tau_{[k]},
\]
其中权重 $w_{[k]}$ 对所有 $k$ 非负。

\begin{enumerate}
  \item 找出使 $\hat\tau_w$ 对 $\tau$ 无偏的 $w_{[k]}$ 条件。
  \item 在所有无偏估计量中，找出使 $\hat\tau_w$ 方差最小的权重。
\end{enumerate}
\end{Exercise}
```

```latex
\begin{Exercise}{\ref{exr:5-9} Data re-analyses}\label{exr:5-9}
重新分析第 4 章使用的 LaLonde 数据。

\begin{enumerate}
  \item 将实验视为按种族分层的 SRE，重新分析数据。
  \item 将实验视为按婚姻状况分层的 SRE，重新分析数据。
  \item 将实验视为按高中文凭指标分层的 SRE，重新分析数据。
\end{enumerate}
与 CRE 下的结果进行比较。
\end{Exercise}
```

#### 错误示例

❌ **错误：缺少标签引用**
```latex
\begin{Exercise}{5.1 Covariate balance}\label{exr:5-1}  % 缺少 \ref{}
```

❌ **错误：标签格式错误**
```latex
\begin{Exercise}{\ref{ex:5.1} Covariate balance}\label{exr:5-1}  % 标签名不一致
```

❌ **错误：中文标题**
```latex
\begin{Exercise}{\ref{exr:5-1} CRE 中的协变量平衡}\label{exr:5-1}  % 不应用中文标题
```

#### 格式要点

| 要点 | 说明 |
|------|------|
| 环境名称 | `Exercise`（大写，首字母大写） |
| 参数格式 | `{\ref{标签} 英文标题}` |
| 标签命名 | `exr:{章号}-{题号}` |
| 习题标题 | 使用教材原文的英文标题 |
| 公式引用 | **必须用 `\eqref{}`** |
| 内容语言 | 理论题优先英文，计算/应用题可用中文 |

---

### 4.3 通用模板

```latex
\section{习题}\label{sec:chapterX-exercises}

\begin{Exercise}{\ref{exr:X-1} 英文标题}\label{exr:X-1}
习题内容。
\end{Exercise}
```

格式同 Peng Ding 模板。

---

## 五、标签命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 公式 | `eq:{描述性名称}` | `eq:balance-discrete-CRE` |
| 习题 | `exr:{章号}-{题号}` | `exr:5-1`, `exr:3-7` |
| 定义 | `def:{描述性名称}` | `def:potential-outcome` |
| 定理 | `thm:{描述性名称}` | `thm:consistency-ols` |

### 标签命名参考（Peng Ding 模板）

| 习题 | 标签 |
|------|------|
| 5.1 | `exr:5-1` |
| 5.2 | `exr:5-2` |
| 3.7 | `exr:3-7` |

---

## 六、公式引用规则

### ❌ 错误做法

```latex
证明 (5.2) 给出的公式  % 硬编码编号
```

### ✅ 正确做法

```latex
证明 \eqref{eq:balance-discrete-CRE} 给出的公式
```

**前提**：公式需要有 `\label{}`

```latex
\begin{equation}
\label{eq:balance-discrete-CRE}
...
\end{equation}
```

---

## 七、习题来源优先级

### 1. tag 文件（优先）

- **位置**：`PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex`
- **优点**：公式标签清晰，引用关系自动保留

**发现流程**：
```
1. 读取 PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex
2. 搜索 \label{eq:...} 获取所有公式标签
3. 搜索 \ref{hw::...} 获取习题引用的公式
4. 建立映射关系
```

### 2. transcript 文件

- **位置**：`PDFs/<教材>/transcript/<书名>.md`
- **缺点**：没有 label/ref，需要手动添加

**识别模式**：
- 标题模式：`# X.Y Homework Problems`、`## Homework Problems`、`# Exercises`
- 内容模式：`\paragraph{标题}` 或 题号列表

---

## 八、质量检查清单

完成习题后，逐项检查：

- [ ] 习题编号与教材一致
- [ ] 公式引用 `\eqref{}` 指向正确标签
- [ ] 标签命名 `exr:{章号}-{题号}` 规范
- [ ] do Carmo 模板用 `exercise`（小写）
- [ ] Peng Ding 模板用 `Exercise`（大写）
- [ ] 中文专有名词保留英文
- [ ] 编译无错误

---

## 九、教训索引

| ID | 教训 | 核心要点 | 累计次数 |
|----|------|---------|----------|
| L801 | 习题环境名称选择 | do Carmo 用 `exercise`，其他用 `Exercise` | 3 |
| L802 | 公式引用必须用 `\eqref{}` | 禁止硬编码编号 | 3 |
| L803 | 模板类型判断 | 读文件内容，不按目录名猜 | 2 |
| L804 | 习题编号与教材一致 | 保持原书编号 | 1 |

---

## 十、工作流程

```
1. 读取 Memory 文件
   → docs/lessons/agents/exercise-expert-memory.md
   → docs/lessons/agents/ALL-agents-memory.md

2. 确定教材模板
   → 读取目标 .tex 文件，判断模板类型

3. 查找习题来源
   → 优先 tag 文件 → 其次 transcript

4. 提取并格式化
   → 按模板格式生成 LaTeX

5. 质量校验
   → 逐项检查清单

6. 更新 Memory
   → 记录重要决策和教训
```

---

## 十一、用户指令

| 指令 | 说明 |
|------|------|
| `写作第 X 章` | 生成章节知识点笔记 **+ 习题**（一体化） |
| `生成第 X 章笔记` | 生成章节知识点笔记 **+ 习题**（一体化） |
| `生成第 X 章习题` | 单独提取并格式化第 X 章习题 |
| `补充习题内容` | 补充已有章节的习题 |
| `用英文输出习题` | 内容使用英文原文 |
| `检查标签引用` | 验证所有 `\eqref{}` 是否正确 |

---

## 十二、相关文件

| 文件 | 用途 |
|------|------|
| `docs/exercise-workflow.md` | 工作流规范 |
| `docs/exercise-format.md` | 格式详细说明 |
| `docs/lessons/agents/exercise-expert-memory.md` | 教训 Memory |
| `docs/lessons/agents/ALL-agents-memory.md` | 通用教训 |
