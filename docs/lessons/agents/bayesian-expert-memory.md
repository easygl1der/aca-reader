# 贝叶斯统计专家教训记忆

**适用对象**: bayesian-expert
**最后更新**: 2026-03-29

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L301 | 后验分布符号约定 | 1 |
| L302 | 共轭先验的写法 | 1 |

---

## L301: 后验分布符号约定

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了先验、似然、后验的符号表示。

**正确做法**:
```latex
% 先验分布
\theta \sim \text{Beta}(\alpha, \beta)
p(\theta)

% 似然
p(y|\theta) = \binom{n}{y}\theta^y(1-\theta)^{n-y}

% 后验分布
p(\theta|y) \propto p(y|\theta)p(\theta)
\theta|y \sim \text{Beta}(\alpha + y, \beta + n - y)
```

**符号规范**:
- 先验: $p(\theta)$
- 似然: $p(y|\theta)$（注意条件竖线）
- 后验: $p(\theta|y)$

**防止措施**:
- 始终区分三种分布
- 引用 Gelman Bayesian Data Analysis 原书符号

---

## L302: 共轭先验的写法

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
写 Beta-Binomial 共轭时忘了注明参数更新公式。

**正确做法**:
```latex
% Beta-Binomial 共轭
\theta \sim \text{Beta}(\alpha, \beta)  % 先验
y|\theta \sim \text{Bin}(n, \theta)  % 似然
\theta|y \sim \text{Beta}(\alpha + y, \beta + n - y)  % 后验

% 后验均值
\mathbb{E}(\theta|y) = \frac{\alpha + y}{\alpha + \beta + n}
```

**防止措施**:
- 共轭先验要写完整的参数更新

---

## 领域专属符号表

```latex
% 贝叶斯统计核心符号
先验分布: p(\theta)
似然: p(y|\theta)
后验分布: p(\theta|y)
后验预测分布: p(\tilde{y}|y) = \int p(\tilde{y}|\theta)p(\theta|y)d\theta
共轭先验: Beta-Binomial, Dirichlet-Multinomial
```

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/bayesian-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是贝叶斯专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认
