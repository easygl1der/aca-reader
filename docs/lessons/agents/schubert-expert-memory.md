# Schubert 演算专家教训记忆

**适用对象**: schubert-expert
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L501 | Schubert 多项式符号约定 | 1 |
| L502 | Bruhat 顺序的表示 | 1 |
| L503 | 文献引用标注规范 | 1 |

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
