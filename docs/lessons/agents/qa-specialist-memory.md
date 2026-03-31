# QA 记录专家教训记忆

**适用对象**: qa-specialist
**最后更新**: 2026-03-30

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L1001 | 错误 qa.tex 文件 | 3 |
| L1002 | QA 格式不规范 | 2 |
| L1003 | 脚注引用缺失 | 2 |
| L1004 | 脚注问题文本必须与 qa.tex 完全一致 | 1 |

---

## L1001: 错误 qa.tex 文件

**日期**: 2026-03-29
**经历次数**: 3 次 (累计)

**错误描述**:
把 QA 记录到了错误的 qa.tex 文件。

**正确做法**:
根据问题主题选择正确的 qa.tex：

| Topic | qa.tex 路径 |
|-------|-------------|
| 因果推断 | `notes/A-First-Course-in-Causal-Inference/appendix/qa.tex` |
| 微分几何 | `notes/differential-geometry/do-carmo-curves-surfaces/appendix/qa.tex` |
| 贝叶斯统计 | `notes/bayesian/appendix/qa.tex` |
| 信息几何 | `notes/information-geometry/appendix/qa.tex` |
| Schubert 演算 | `notes/Schubert-Polynomials/appendix/qa.tex` |
| 数理统计 | `notes/mathematical-statistics/appendix/qa.tex` |

**检查方法**:
- 开工前确认问题 topic
- 找到对应的 qa.tex 路径

**防止措施**:
- 先问用户问题属于哪个 topic
- 或者根据关键词判断

---

## L1002: QA 格式不规范

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
QA 格式不标准，缺少必要的 `\label{}` 或 `\textbf{}` 标记。

**正确格式**:
```latex
\subsection{问题标题}\label{sec:qa-xxx}
\textbf{问}：用户的问题是什么？
\textbf{答}：回答内容...
```

**错误示例**:
```latex
% 缺少 label ❌
\subsection{问题标题}
问：xxx？
答：xxx。

% 缺少 \textbf 标记 ❌
\subsection{问题标题}\label{sec:qa-xxx}
问：xxx？
答：xxx。
```

**防止措施**:
- 严格按照格式模板
- 检查 qa.tex 是否有对应 label

---

## L1003: 脚注引用缺失

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
记录 QA 后没在正文首次出现处添加脚注引用。

**正确做法**:
1. 在正文中首次出现该概念处添加：
```latex
......概念......\footnote{问：What is X? 见附录 \cref{sec:qa-xxx}。}
```

2. 脚注中必须包含：
- 问题内容（让读者知道这是什么）
- 见附录 + cref（让读者能跳转）

**防止措施**:
- QA 记录完成后检查正文
- 确认脚注引用已添加

---

## L1004: 脚注问题文本必须与 qa.tex 完全一致

**日期**: 2026-03-31
**经历次数**: 1 次 (累计)

**错误描述**:
脚注中的问题文本被截断或简化，与 qa.tex 中的完整问题文本不一致。读者在正文中看到的脚注问句不完整。

**正确做法**:
1. 写脚注时，从 qa.tex 中复制完整的 `\textbf{问}：...` 文本
2. 不能自己概括或截断
3. 脚注格式：`\footnote{问：[完整问题文本]见附录 \cref{sec:qa-xxx}。}`

**示例**：
```latex
% qa.tex 中
\textbf{问}：$\sigma(u)^T$ 是什么意思？上标 $T$ 代表什么？

% 脚注必须完全一致 ❌（错误：截断了）
\% footnote{问：$\sigma(u)^T$ 是什么意思？见附录...}

% 脚注必须完全一致 ✅（正确：完整复制）
\% footnote{问：$\sigma(u)^T$ 是什么意思？上标 $T$ 代表什么？见附录 \cref{sec:sigma-u-T}。}
```

**防止措施**:
- 写完脚注后，打开 qa.tex 对比 `\textbf{问}` 段落
- 确保文字完全一致，不做删减

---

## QA 格式模板

```latex
\subsection{标题}\label{sec:qa-xxx}
\textbf{问}：用户问题？
\textbf{答}：回答内容...
```

**脚注引用格式**:
```latex
% 在正文首次出现处
...概念...\footnote{问：What is X? 见附录 \cref{sec:qa-xxx}。}
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/qa-specialist-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是 QA 专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
