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
        ├─ book for the third part of the judgment template process, you can merge it into the second part. Yes, you can merge it into the second template. Because this guidelines is based on the textbooks I wrote before, including the differential geometry and causal inference materials. But in reality, the general approach may not be limited to these two textbooks, which can only serve as examples. So for general use, you still need to identify what exactly it is. Actually, your third and second parts can be combined.类 + 无特殊定义 → Exercise（大写）
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

### 4.1 通用模板（通用教材）

通用模板是默认格式，适用于**未在笔记 LaTeX 中定义特殊 exercise 环境的教材**。

#### 通用格式模板

```latex
\begin{Exercise}{\cref{exr:X-Y} Exercise X-Y \cite{bookkey}}\label{exr:X-Y}
习题内容。
\end{Exercise}
```

#### 格式说明

| 位置 | 内容 | 示例 |
|------|------|------|
| `exr:X-Y` | 标签 = 教材章-题号 | `exr:5-1` |
| `Exercise X-Y` | 第二括号第一部分：教材编号 | `Exercise 5-1` |
| `\cite{bookkey}` | 第二括号第二部分：bibtex 引用 | `\cite{Ding2024}` |

#### 第二括号结构

```
{\ref{exr:5-1} Exercise 5-1 \cite{Ding2024}}
 └─①─┘  └────②─────┘  └────③─────┘
   ① 引用标签          ② 教材编号        ③ bibtex 引用
```

#### 标签命名

- 格式：`exr:{章号}-{题号}`
- 来源：跟随教材原书编号
- 示例：`exr:5-1`, `exr:3-7`, `exr:2-15`

#### 难题标记（可选）

若教材中该题标记为星号（可选/难题），在编号后加 `*`：

```latex
\begin{Exercise}{\ref{exr:5-10*} Exercise 5-10* \cite{Ding2024}}\label{exr:5-10*}
% 难题内容
\end{Exercise}
```

#### 分部题目

多问时使用 `enumerate` 环境：

```latex
\begin{Exercise}{\ref{exr:5-3} Exercise 5-3 \cite{Ding2024}}\label{exr:5-3}
题目描述...

\begin{enumerate}
  \item 第一小问
  \item 第二小问
\end{enumerate}
\end{Exercise}
```

#### 两种放置风格

**风格 A：分节放置**（每节末放置该节习题）

```latex
\subsection*{5-1 节练习}

\begin{Exercise}{\ref{exr:5-1} Exercise 5-1 \cite{Ding2024}}\label{exr:5-1}
习题内容...
\end{Exercise}
```

**风格 B：章末放置**（所有习题集中在章末）

```latex
\section{习题}\label{sec:chapter5-exercises}

\begin{Exercise}{\ref{exr:5-1} Exercise 5-1 \cite{Ding2024}}\label{exr:5-1}
习题内容...
\end{Exercise}

% 更多习题...

\section*{5-2 节}
% 后续章节内容...
```

---

### 4.2 do Carmo 模板（微分几何）

do Carmo 教材使用**小写** `exercise` 环境，格式略有不同。

#### 格式模板

```latex
\begin{exercise}{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}
习题内容（英文原文）。
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
of the disk is called a cycloid (见 \cref{fig:cycloid}，教材 Figure 1-7).
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

#### 格式要点

| 要点 | 说明 |
|------|------|
| 环境 | `exercise`（小写） |
| 第二括号 | `{章节, 题号 — do Carmo, Exercise 章节, 题号}` |
| 内容语言 | 英文原文（直接引用教材） |
| 难题标记 | 题号后加 `*` |
| 图片引用 | `\cref{fig:标签}` |

#### 错误示例

❌ **错误：中文标题**
```latex
\begin{exercise}{1-2, 1 — do Carmo, 习题1-2, 1}  % 不要用中文
```

❌ **错误：缺少来源**
```latex
\begin{exercise}{1-2, 1}  % 缺少 do Carmo 引用
```

❌ **错误：用 footnote 代替**
```latex
\begin{exercise}{1-2, 1}\footnote{do Carmo, Exercise 1-2, 1}  % 不要用 footnote
```

#### 分节练习标记

```latex
\subsection*{1-2 节练习}
```

---

### 4.3 其他已知模板

对于已在笔记 LaTeX 中定义 exercise 环境的教材，格式跟随笔记定义。

**Peng Ding 模板（因果推断）**：

```latex
\begin{Exercise}{\ref{exr:5-1} Covariate balance in the CRE}\label{exr:5-1}
证明 \eqref{eq:balance-discrete-CRE}：...
\end{Exercise}
```

格式要点：
- 环境：`Exercise`（大写）
- 第二括号：`{\ref{标签} 英文标题}`
- 标签：`exr:{章号}-{题号}`
- 公式引用：**必须用 `\eqref{}`**

---

### 4.4 标签来源优先级

| 来源 | 位置 | 如何处理 |
|------|------|----------|
| **tag 文件**（优先） | `PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex` | 直接使用文件中的 `\label{}` |
| **transcript 文件** | `PDFs/<教材>/transcript/<书名>.md` | 根据教材编号手动创建标签 `exr:章-题号` |

**tag 文件处理流程**：
```
1. 读取 PDFs/<教材>/arXiv-xxx/chapters/chapterXX.tex
2. 搜索 \label{exr:...} 获取已有标签
3. 直接使用对应标签
```

**仅有 transcript 时**：
```
1. 提取教材章节编号（如 "5-1", "3-7"）
2. 创建标签 exr:章-题号
3. 在笔记 LaTeX 中定义对应标签
```

---

## 五、⭐ 硬编码引用处理（核心规范）

> **⚠️ 极其重要**：习题中出现的硬编码编号（如 `(5.2)`、`Example 4.1.3`、`Figure 3-1`）如果不转成引用，读者无法知道这些编号指向什么内容。

### 硬编码类型与处理方式

| 硬编码类型 | 示例 | 处理方式 |
|-----------|------|----------|
| 公式引用 | `(5.2)`, `式 (5.2)` | 找到对应公式，替换为 `\eqref{eq:xxx}` |
| 图表引用 | `Figure 3-1`, `图 4.2` | 找到对应图片，替换为 `\cref{fig:xxx}` |
| 章节/例题引用 | `Example 4.1.3`, `Section 5.2` | 找到对应章节，替换为 `\cref{sec:xxx}` 或 `\cref{exa:xxx}` |
| 其他习题引用 | `Exercise 5.1` | 替换为 `\cref{exr:5-1}` |

### 处理流程

**Step 1: 识别硬编码引用**

读取习题文本，找出所有硬编码编号模式：

```
- (X.Y) 或 式 (X.Y) → 公式引用
- Example X.Y → 例题引用
- Figure X.Y → 图片引用
- Exercise X.Y → 其他习题引用
- Section X.Y → 章节引用
```

**Step 2: 在教材中定位**

根据编号在教材（tag 文件或 transcript）中找到对应的公式/图片/章节/例题。

**Step 3: 在笔记中查找是否已存在**

搜索笔记 LaTeX 文件，检查对应 label 是否已存在：

```bash
# 检查公式标签
grep -n "\\\\label{eq:" notes/*/chapter*.tex

# 检查图表标签
grep -n "\\\\label{fig:" notes/*/chapter*.tex
```

**Step 4: 添加或引用**

| 情况 | 操作 |
|------|------|
| 笔记中已存在标签 | 直接使用 `\cref{}` 或 `\eqref{}` 替换硬编码编号 |
| 笔记中不存在 | 将对应内容（公式/图片/章节摘要）添加到笔记中，再引用 |

**Step 5: 替换硬编码**

```latex
% 处理前（❌ 硬编码）
For Example 4.1.3, verify equations (4.1.4)-(4.1.8).

% 处理后（✅ 引用）
For \cref{exa:4-1-3}, verify \eqref{eq:4-1-4}--\eqref{eq:4-1-8}.
```

### 处理示例

**示例：习题引用教材公式**

```latex
% 处理前
证明 (5.2) 给出的公式

% Step 1: 识别 (5.2) 是公式引用
% Step 2: 在教材/笔记中找到 eq:5-2-balance
% Step 3-4: 检查笔记，已存在
% Step 5: 替换

% 处理后
证明 \eqref{eq:5-2-balance} 给出的公式
```

**示例：习题引用例题**

```latex
% 处理前
For Example 4.1.3, verify equations (4.1.4)-(4.1.8).

% Step 1: 识别 Example 4.1.3 和 (4.1.4)-(4.1.8)
% Step 2: 在教材中定位
% Step 3: 检查笔记 — 例题 label 不存在，需要添加
% Step 4: 在笔记中添加 \label{exa:4-1-3}
% Step 5: 替换

% 处理后
For \cref{exa:4-1-3}, verify \eqref{eq:4-1-4}--\eqref{eq:4-1-8}.
```

---

## 六、质量检查清单

完成习题后，逐项检查：

- [ ] **⭐ 硬编码引用已替换**：所有 `(X.Y)`、`Example X.Y`、`Figure X.Y` 等已转为 `\cref{}` 或 `\eqref{}`
- [ ] **⭐ 引用目标存在**：每个引用在笔记中都能找到对应 label
- [ ] 习题编号与教材一致
- [ ] 标签命名 `exr:{章号}-{题号}` 规范
- [ ] exercise 环境大小写正确（do Carmo 用小写，其他用大写）
- [ ] 公式引用使用 `\eqref{}`，禁止硬编码
- [ ] 中文专有名词保留英文
- [ ] 编译无错误

### 编译验证命令

```bash
# 编译并检查错误
./compile.sh 2>&1 | grep -i "error\|warning"

# 检查是否有未解析的引用
grep -n "???" notes/*/chapters/chapter*.tex
```

---

## 七、教训索引

| ID | 教训 | 核心要点 | 累计次数 |
|----|------|---------|----------|
| L801 | 习题环境名称选择 | do Carmo 用 `exercise`，其他用 `Exercise` | 3 |
| L802 | 公式引用必须用 `\eqref{}` | 禁止硬编码编号 | 3 |
| L803 | 模板类型判断 | 读文件内容，不按目录名猜 | 2 |
| L804 | 习题编号与教材一致 | 保持原书编号 | 1 |

---

## 八、工作流程

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

## 九、用户指令

| 指令 | 说明 |
|------|------|
| `写作第 X 章` | 生成章节知识点笔记 **+ 习题**（一体化） |
| `生成第 X 章笔记` | 生成章节知识点笔记 **+ 习题**（一体化） |
| `生成第 X 章习题` | 单独提取并格式化第 X 章习题 |
| `补充习题内容` | 补充已有章节的习题 |
| `用英文输出习题` | 内容使用英文原文 |
| `检查标签引用` | 验证所有 `\eqref{}` 是否正确 |

---

## 十、相关文件

| 文件 | 用途 |
|------|------|
| `docs/exercise-workflow.md` | 工作流规范 |
| `docs/exercise-format.md` | 格式详细说明 |
| `docs/lessons/agents/exercise-expert-memory.md` | 教训 Memory |
| `docs/lessons/agents/ALL-agents-memory.md` | 通用教训 |
