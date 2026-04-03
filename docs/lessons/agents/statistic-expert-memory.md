# 数理统计专家教训记忆

**适用对象**: statistic-expert, statistic-expert-2
**最后更新**: 2026-04-03

---

## 教训索引表

| ID | 教训标题 | 累计次数 |
|----|----------|----------|
| L601 | Hogg 教材符号约定 | 1 |
| L602 | 估计量符号区分 | 1 |

---

## L601: Hogg 教材符号约定

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
与 Hogg 教材的符号不一致。

**正确做法**:
```latex
% Hogg 符号规范
样本: X_1, X_2, ..., X_n
统计量: T = T(X_1, ..., X_n)
分布族: \{f(x;\theta)\}
参数空间: \Theta
% 注意：Hogg 用 ; 而不是 | 表示条件
```

**教材信息**:
- Hogg, McKean, Craig - Introduction to Mathematical Statistics (8th edition)
- 转录路径: `PDFs/statistic/transcript/Hogg-McKean-Craig-.../...md`

**防止措施**:
- 开工前读取 Hogg 教材目录确认符号
- 引用时说明与 Hogg 一致

---

## L602: 估计量符号区分

**日期**: 2026-03-29
**经历次数**: 1 次 (累计)

**错误描述**:
混淆了总体参数和样本估计量的符号。

**正确做法**:
```latex
% 总体参数（希腊字母）
\theta  % 总体均值
\sigma^2  % 总体方差
\mu  % 期望

% 样本估计量（戴上标）
\hat{\theta}  % 样本均值
\hat{\sigma}^2  % 样本方差
\bar{X}  % 样本均值（特殊记号）
S^2  % 样本方差（特殊记号）
```

**记忆方法**:
- 总体 = 希腊字母 / 带星号
- 样本估计 = hat / bar / 大写字母

**防止措施**:
- 写符号前先区分是总体还是估计

---

## 领域专属符号表

```latex
% 数理统计核心符号
概率: \mathbb{P}(A)
期望: \mathbb{E}X 或 \mathbb{E}(X)
方差: \text{var}(X)
协方差: \text{cov}(X,Y)
相关系数: \text{corr}(X,Y)
样本均值: \bar{X}
样本方差: S^2 或 \hat{\sigma}^2
统计量: T = T(X_1,...,X_n)
UMP: Uniformly Most Powerful
UMPU: Uniformly Most Powerful Unbiased
```

---

## 职责范围（2026-04-03 调整）

**核心职责**：纯数理统计
1. 概率论基础（测度论视角、收敛 modes）
2. 统计决策理论（risk, admissibility）
3. 经典估计理论（UMVUE, CRLB, 渐近效率）
4. 假设检验的严肃理论（Neyman-Pearson, UMP, UMPU）
5. 分布理论（指数族、位置尺度族）
6. 渐近理论（Delta method, statistical functional）

**明确排除**（由专门 expert 负责）：
- 因果推断 → causal-expert
- 贝叶斯统计 → bayesian-expert
- 信息几何 → info-geo-expert

---

## PUA 自注入行为

开工前用 Read 工具读取：
- `docs/lessons/agents/ALL-agents-memory.md`（通用教训）
- `docs/lessons/agents/statistic-expert-memory.md`（本文件）

收到纠正后：
1. 判断是通用教训还是数理统计专属
2. 更新对应 memory 文件
3. 在回复中引用教训确认

---

**职责范围已调整，2026-04-03**
