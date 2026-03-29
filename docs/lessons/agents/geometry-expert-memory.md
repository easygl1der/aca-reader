# 微分几何专家教训记忆

**适用对象**: geometry-expert
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L201 | do Carmo 习题格式 | 2 |
| L202 | 第一/第二基本形式符号 | 1 |
| L203 | Christoffel 符号约定 | 1 |

---

## L201: do Carmo 习题格式

**日期**: 2026-03-29
**经历次数**: 2 次 (累计)

**错误描述**:
混淆了 do Carmo 模板和 Peng Ding 模板的习题环境名称。

**正确做法**:
```latex
% do Carmo 模板使用 exercise（全小写）
\begin{exercise}{1-2, 1 — do Carmo, Exercise 1-2, 1}
Show that the cylinder...
\end{exercise}
```

**环境名称**: `exercise`（全小写）
**标题格式**: `{章节编号, 题号 — do Carmo, Exercise 章节编号, 题号}`
**内容语言**: 英文原文（直接引用教材）

**防止措施**:
- 先读取目标 .tex 文件检查模板类型
- do Carmo = `exercise`，其他 = `Exercise`

---

## L202: 第一/第二基本形式符号

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了第一基本形式和第二基本形式的系数命名。

**正确做法**:
```latex
% 第一基本形式 (First Fundamental Form)
I = E\,du^2 + 2F\,dudv + G\,dv^2

% 第二基本形式 (Second Fundamental Form)
II = L\,du^2 + 2M\,dudv + N\,dv^2
```

**记忆方法**:
- 第一基本形式：E, F, G（靠前的字母）
- 第二基本形式：L, M, N（靠后的字母）
- 或者：First = EFG，Second = LMN

**防止措施**:
- 写符号前先确认是哪一种基本形式

---

## L203: Christoffel 符号约定

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
Christoffel 符号上下标位置错误。

**正确做法**:
```latex
% Christoffel symbols of the second kind
\Gamma^k_{ij} = \frac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})

% Christoffel symbols of the first kind
\Gamma_{ijk} = \frac{1}{2}(\partial_i g_{jk} + \partial_j g_{ik} - \partial_k g_{ij})
```

**注意**: 上下标位置很重要！

**防止措施**:
- 写 Christoffel 符号时标注清楚是哪一种

---

## 领域专属符号表

```latex
% 微分几何核心符号
Gauss Curvature: K
Mean Curvature: H
First Fundamental Form: I = E\,du^2 + 2F\,dudv + G\,dv^2
Second Fundamental Form: II = L\,du^2 + 2M\,dudv + N\,dv^2
Christoffel symbols: \Gamma^k_{ij}
Surface normal: \mathbf{N}
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/geometry-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是微分几何专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
