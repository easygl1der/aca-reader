# 习题专家教训记忆

**适用对象**: exercise-expert, exercise-expert-2, exercise-expert-3, exercise-expert-4
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L801 | 习题环境名称选择 | 3 |
| L802 | 公式引用必须用 \eqref{} | 3 |
| L803 | 模板类型判断 | 2 |
| L804 | 习题编号与教材一致 | 1 |

---

## L801: 习题环境名称选择

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
混淆了不同模板的习题环境名称。

**正确做法**:
先读取目标 `.tex` 文件，检查 documentclass 或主要 theorem 环境：

| 模板 | 书籍 | 环境名称 |
|------|------|----------|
| Peng Ding 模板 | A First Course in Causal Inference | `Exercise`（首字母大写） |
| do Carmo 模板 | Differential Geometry | `exercise`（全小写） |
| 通用/数学统计 | Hogg | `Exercise`（首字母大写） |

```latex
% do Carmo 模板
\begin{exercise}{1-2, 1 — do Carmo, Exercise 1-2, 1}
题目内容（英文原文）
\end{exercise}

% Peng Ding / 通用模板
\begin{Exercise}{\ref{exr:5-1} Consistency of OLS}\label{exr:5-1}
Show that \eqref{eq:ols-estimator} is consistent...
\end{Exercise}
```

**防止措施**:
- 开工前读取目标 .tex 文件
- 检查是否定义了 `exercise` 环境

---

## L802: 公式引用必须用 \eqref{}

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
在习题中硬编码公式编号（如"证明 (5.2)"）。

**正确做法**:
```latex
% 错误 ❌
证明 (5.2) 给出的公式

% 正确 ✅
证明 \eqref{eq:balance-discrete-CRE} 给出的公式

% 前提：公式需要有 label
\begin{equation}
\label{eq:balance-discrete-CRE}
...
\end{equation}
```

**Label 命名规范**:
- 公式: `eq:{描述性名称}`
- 习题: `exr:{章号}-{题号}`

**防止措施**:
- 写习题前先搜索相关的 `\label{}`
- 用 `\eqref{}` 替代硬编码编号

---

## L803: 模板类型判断

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
按目录名判断模板类型，而不是检查 .tex 文件内容。

**正确做法**:
**错误方法**（按目录）:
```latex
% 错误！不同模板混用
 notes/differential-geometry/do-carmo-*/ → exercise
 notes/A-First-Course-in-Causal-Inference/ → Exercise
```

**正确方法**（检查文件）:
```latex
% 先读取目标 .tex
% 如果定义了 exercise 环境 → exercise（全小写）
% 否则 → Exercise（首字母大写）
```

**防止措施**:
- 始终读取目标 .tex 文件
- 不要按目录名假设模板类型

---

## L804: 习题编号与教材一致

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
习题编号与教材原书不一致。

**正确做法**:
- 英文原文直接引用教材
- 编号保持原书编号（如 "Exercise 1.2.3"）
- 如果教材有子题，保持同样的层级结构

**防止措施**:
- 写习题前核对教材编号
- 参考教材目录

---

## 领域专属技能

```latex
% 模板判断流程
1. 读取目标 .tex 文件
2. 检查 \begin{exercise} 是否存在（do Carmo 用 exercise）
3. 如果没有，检查 documentclass
4. 默认用 Exercise（首字母大写）

% Label 命名
公式: eq:{描述性名称}
习题: exr:{章号}-{题号}
定理: def:{描述性名称}

% 一体化规则
知识点 + 习题必须一起生成（不是分开两步）
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/exercise-expert-memory.md`（本文件）
- `docs/exercise-format.md`
- `docs/exercise-workflow.md`

收到纠正后：
1. 判断是通用教训还是习题专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
