# 信息几何专家教训记忆

**适用对象**: info-geo-expert
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L401 | KL 散度的两种定义 | 1 |
| L402 | 指数族流形的参数化 | 1 |

---

## L401: KL 散度的两种定义

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了 KL 散度的两种方向（$D_{KL}(P\|Q)$ vs $D_{KL}(Q\|P)$）。

**正确做法**:
```latex
% KL(P||Q) - 向前散度
D_{KL}(P\|Q) = \int p(x) \log\frac{p(x)}{q(x)} dx

% KL(Q||P) - 向后散度（不同！）
D_{KL}(Q\|P) = \int q(x) \log\frac{q(x)}{p(x)} dx

% 性质：D_{KL}(P||Q) \neq D_{KL}(Q||P)（除非 P=Q）
```

**记忆方法**:
- 第一个参数是积分中的分子
- 方向很重要！

**防止措施**:
- 写 KL 散度时注明方向
- 引用 Amari 原书定义

---

## L402: 指数族流形的参数化

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了自然参数和均值参数。

**正确做法**:
```latex
% 指数族标准形式
p(x|\theta) = \exp(\theta^T T(x) - A(\theta))h(x)

% 自然参数空间
\theta \in \Theta  % 自然参数
\eta = \nabla A(\theta)  % 均值参数

% 对偶坐标系
F = \nabla A  % Legendre 变换
```

**防止措施**:
- 明确说明是哪组参数
- 引用 Amari 信息几何原书

---

## 领域专属符号表

```latex
% 信息几何核心符号
KL 散度: D_{KL}(p\|q)
黎曼度量: g_{ij}
指数族: p(x|\theta) = \exp(\theta^T T(x) - A(\theta))
自然梯度: \tilde{\nabla}f = G^{-1}\nabla f
e-平行联络: \nabla^{(e)}
m-平行联络: \nabla^{(m)}
双平行联络: \nabla^{(\alpha)}
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/info-geo-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是信息几何专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
