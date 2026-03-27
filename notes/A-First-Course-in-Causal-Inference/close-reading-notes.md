# Close Reading Notes: Chapter 5 - Stratification and Post-Stratification

## 基本信息
- **主题**: Chapter 5 - Stratification and Post-Stratification in Randomized Experiments
- **字数**: ~3500 words
- **核心概念**: Covariate balance, Stratified Randomized Experiment (SRE), Post-stratification

## 动机背景

**这个章节解决什么问题？**

在完全随机实验（CRE）中，治疗分配完全由 chance 决定。这种设计在样本量趋于无穷时表现优异，但在有限样本中，治疗组和对照组可能在某些协变量上出现不平衡。

**历史脉络**：
- Box et al. (1978): "Block what you can and randomize what you cannot"
- Neyman (1923): 首次提出分层实验的方差公式
- Fisher (1935): 引入 Fisher 随机化检验

## 核心定义

### Definition 5.1: Stratified Randomized Experiment (SRE)

**原文**：
> 固定 $n_{[k]1}$ 或 $n_{[k]0}$（$k = 1, \dots, K$）。我们在离散的协变量 $X$ 的每一层内独立进行 CRE。

**动机**：为什么要引入这个定义？
- CRE 中，即使各层治疗组和对照组比例之差的期望为零，但单次实现中大概率不为零
- SRE 通过固定各层治疗分配数量，主动控制 covariate balance

**联系**：与之前哪个概念相关？
- 与 CRE（完全随机实验）是递进关系
- 与第 4 章的 potential outcomes 框架紧密联系

## 重要定理

### Theorem 5.1: Covariate Balance in CRE (Equation 5.2)

**完整内容**：
> 在 CRE 下，
> $$\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0, \quad \text{但} \quad \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \neq 0 \text{ 以高概率成立}.$$

**核心思想**：期望为零说明随机化保证了渐近公平性，但有限样本中的随机波动可能导致显著的不平衡。

**附录标记**：⚠️ 完整推导见附录

### Theorem 5.2: Variance Comparison (Equation 5.12, 5.4)

**完整内容**：
> CRE 下差值均值估计量的方差可以分解为层内方差和层间方差之和，SRE 消除了层间变异带来的额外方差。

**核心思想**：当协变量能预测潜在结果时，SRE 的效率增益来自层间变异的消除。

**附录标记**：⚠️ 完整推导见附录

## 关键公式

### Equation (5.2): Balance in Discrete CRE
$$\mathbb{E}\left( \frac{n_{[k]1}}{n_1} - \frac{n_{[k]0}}{n_0} \right) = 0$$
**含义**：在完全随机化下，各层治疗组和对照组比例之差的期望为零
**用途**：刻画随机化的渐近公平性

### Equation (5.6): Stratified Estimator
$$\hat\tau_\SRE = \sum_{k=1}^K \pi_{[k]} \hat\tau_{[k]}$$
**含义**：各层估计量的加权平均
**用途**：SRE 的点估计

### Equation (5.7): Variance of Stratified Estimator
$$\hat V_\SRE = \sum_{k=1}^K \pi_{[k]}^2 \left( \frac{\hat S_{[k]}^2(1)}{n_{[k]1}} + \frac{\hat S_{[k]}^2(0)}{n_{[k]0}} \right)$$
**含义**：保守方差估计量
**用途**：构建置信区间

### Equation (5.12): Variance Decomposition
$$\var_{\CRE}(\hat\tau) = \text{(层内项)} + \text{(层间项)}$$
**含义**：CRE 方差分解为层内和层间两部分
**用途**：证明 SRE 的效率增益

### Equation (5.13): Post-stratification Estimator
$$\hat\tau_\PS = \sum_{k=1}^K \pi_{[k]} \hat\tau_{[k]}$$
**含义**：后分层估计量，与 $\hat\tau_\SRE$ 形式相同
**用途**：CRE 分析中使用协变量

## 示例

### Example 5.1: Stratified Estimator (Line 2475)
**动机**：说明如何在 SRE 中估计 $\tau$

**设定**：
- $n$ 个单元，协变量 $X_i \in \{1, \dots, K\}$
- 各层内进行 CRE

**计算**：
$$\hat\tau_\SRE = \sum_{k=1}^K \pi_{[k]} \hat\tau_{[k]}$$

## 章节结构图

```
Section 5.1: 引言（Box 名言）
    ↓
Section 5.2: SRE 定义与记号
    ├── Definition 5.1: SRE
    └── eq:balance-discrete-CRE (5.2)
    ↓
Section 5.3: 层别平均因果效应
    ├── $\tau_{[k]}$, $\tau$
    └── eq:stratified-equal (5.3)
    ↓
Section 5.4: 层别化实验中的 FRT
    ├── 检验统计量选择
    ├── $t_\SRE$ 统计量
    └── Wilcoxon, K-S 统计量
    ↓
Section 5.5: Neymanian 推断
    ├── eq:5.8, eq:5.9, eq:5.10
    └── Wald 置信区间
    ↓
Section 5.6: SRE 与 CRE 比较
    ├── eq:5.12 (方差分解)
    └── eq:5.4 (效率增益)
    ↓
Section 5.7: CRE 中的后分层
    ├── eq:5.5 (条件分布)
    └── eq:5.13 (后分层估计量)
    ↓
Section 5.8: 实践中的问题
    └── $K$ 选择、重随机化预告
    ↓
Section 5.9: 本章小结
```

## 附录候选清单

| 内容 | 位置 | 原因 |
|------|------|------|
| eq:balance-discrete-CRE 推导 | Appendix | 多步代数运算 |
| SRE vs CRE 效率比较推导 | Appendix | eq:5.12, eq:5.4 完整推导 |
| Neymanian 方差公式推导 | Appendix | eq:5.8, eq:5.9 推导 |
| eq:condition-to-SRE 推导 | Appendix | 条件概率推导 |

## 习题清单

1. **exr:5-1**: 证明 eq:balance-discrete-CRE
2. **exr:5-2**: 证明 eq:stratified-equal
3. **exr:5-3**: 常数个体因果效应下的最优权重
4. **exr:5-4**: 证明 eq:difference
5. **exr:5-5**: 证明 eq:condition-to-SRE
6. **exr:5-6**: 更多 FRT 统计量
7. **exr:5-7**: Project STAR 数据 FRT 分析
8. **exr:5-8**: 多中心试验分析
9. **exr:5-9**: LaLonde 数据重新分析

## 与前章联系

- **Chapter 3**: Potential outcomes 框架
- **Chapter 4**: CRE 中的 Neymanian 和 Fisherian 推断
- **Chapter 5**: 在 CRE 基础上引入 SRE 解决 covariate imbalance

## 与后续章节联系

- **Chapter 6**: Rerandomization - SRE 和重随机化是使用协变量的两种互补方法
- **Chapter 7**: 倾向得分 - stratum propensity score 的推广
- **Chapter 11**: Covariate balance check - 后分层的延伸
