# 审阅报告：Robust Bayesian Inference on Riemannian Submanifolds

**作者**：Rong Tang, Y. Wu 等
**年份**：2023
**期刊**：Annals of Statistics（或同等级别期刊）
**PDF 路径**：`Tang-2023-RobustBayesianRiemannian.pdf`

---

## 一、摘要与研究问题

本论文研究了在黎曼流形（确切地说是指数族分布构成的黎曼子流形）上的**鲁棒贝叶斯推断**问题。作者考虑了数据生成分布偏离模型假设的 **contamination 污染模型**（即数据以小概率来自污染分布），并在此框架下研究后验分布的**收缩速率（posterior contraction rate）**。

核心研究问题：

- 当观测数据被 **gross-error contamination** 污染时，贝叶斯后验是否仍能可靠地收缩到真实分布？
- 在黎曼子流形上，鲁棒估计的收敛速率是多少？
- 如何在 Riemannian geometry 的框架下建立 **Hellinger 距离** 和 **KL 散度** 的后验收缩理论？

---

## 二、主要贡献

### 贡献一：建立了流形上的鲁棒贝叶斯理论框架

作者将经典的 **Huber 污染模型**（Huber 1964）与信息几何中的 **黎曼子流形** 框架相结合。在指数族分布的参数化子流形上，作者研究了以下污染模型：

$$
Z_i = (1 - \epsilon) \cdot P_0 + \epsilon \cdot Q_i, \quad Q_i \sim \Pi
$$

其中 $P_0$ 是真实分布（属于子流形 $\mathcal{M}$），$\epsilon$ 是污染率，$\Pi$ 是污染分布。

### 贡献二：给出了最优的后验收缩速率

作者证明了在适当的先验分布下（如 **sieve prior** 或 **dimensionally consistent prior**），后验分布在 Hellinger 度量下以速率

$$
O\left(\left(\frac{\log n}{n}\right)^{\frac{\alpha}{2\alpha + d}}\right)
$$

收缩，其中 $\alpha$ 是分布的光滑性参数，$d$ 是流形的维数。

### 贡献三：构造了自适应于光滑性参数的估计算法

论文构造了基于 **local Riemannian Fisher scoring** 的估计方法，能够自适应地选择带宽和光滑化参数，无需事先知道流形的曲率或分布的光滑性。

---

## 三、方法论

### 3.1 几何框架

- 将 $n$ 个 i.i.d. 观测的分布视为参数化子流形 $\mathcal{M} \subset \mathcal{P}$（概率分布空间）
- 使用 Fisher-Rao 度量和 Levi-Civita 连接定义测地线距离
- 定义 **Riemannian projection** 将污染分布投影回子流形

### 3.2 鲁棒损失函数

论文采用以下 **robust loss**：

$$
\rho_{\epsilon}(P, Q) = (1-\epsilon) D_{KL}(P \| Q) + \epsilon \cdot \text{TV}(P, Q)
$$

或等价的 Hellinger 型损失，并证明该损失与 Hellinger 度量在子流形上的限制是等价的。

### 3.3 后验收缩分析

关键工具：

- **Sieved posterior contraction**（Ghosal et al. 风格）推广到黎曼流形
- **Local bracketing entropy** 的几何界估计
- **黎曼几何版的 Le Cam 不等式** 和 **Fano 不等式** 用于下界证明

---

## 四、主要结果

### 定理 1（后验收缩上界）

> 假设先验满足支撑度条件和局部 Hellinger 支撑条件，则对任意 $\epsilon > 0$，后验分布满足
>
> $$
> \mathbb{E}_{P_0^n}\left[\Pi_n\left(B_{\epsilon}^{\text{Riem}}(P_0, \delta_n) \mid \mathbf{Z}\right)\right] \to 1
> $$
>
> 其中 $\delta_n = (n^{-1}\log n)^{1/(2+2\alpha)}$ 是收缩半径。

### 定理 2（自适应收缩率）

> 存在一个 data-driven 的先验序列，使得后验以速率 $\asymp (n/\log n)^{-\alpha/(2\alpha+d)}$ 收缩，且无需知道 $\alpha$。

### 定理 3（下界）

> 任意贝叶斯估计器（无论先验如何）在污染模型下均无法以比上述速率更快地收敛，从而证明上界是最优的（minimax optimal）。

---

## 五、论文优势

### 优势一：问题的重要性

在现代统计中，数据通常具有低维流形结构（如图像位于某个嵌入流形上），而数据污染又是不可避免的现实问题。将鲁棒性与流形结构相结合的选题非常前沿，直接回应了 **distributional robustness** 与 **geometric statistics** 两个热点领域的交叉需求。

### 优势二：技术深度

论文的技术部分展示了深厚的几何概率和信息几何功底。将经典的 Ghosal-Ghosh-van der Vaart 后验收缩框架推广到黎曼流形需要大量技术工作：

- 建立了流形上的 **bracketing entropy** 理论
- 证明了几何版本的 **Bernstein-von Mises 定理**
- 给出了 **Riemannian Fisher information** 的精细估计

### 优势三：应用导向

论文不仅有理论，还有模拟实验验证了所提方法在 Sphere manifold（如方向统计数据）和 SPD manifold（如协方差矩阵数据）上的有效性。

### 优势四：与 Tang-Rong 2022 的承接关系

本论文与 Tang-Rong 2022 的 minimax 理论形成良好的系列化研究。2022 年的论文建立了 minimax 最优速率的下界，本论文则给出了达到该下界的贝叶斯构造（"贝叶斯版的最优估计器"），形成了完整的理论闭环。

---

## 六、主要不足与建议

### 不足一：适用范围过窄

目前仅考虑了 **指数族子流形**。更一般的黎曼流形（如非参数化流形）上的结果是否成立尚不清楚。建议在 Discussion 中补充对一般黎曼流形情形的展望。

### 不足二：污染分布的假设

假设污染分布 $\Pi$ 是**任意的（arbitrary）**，这个假设虽然最大化了鲁棒性，但可能过于悲观。在许多实际应用中，污染分布具有一定的结构（如也是低维的），此时更精细的分析可能得到更快的速率。

### 不足三：计算实现部分略显薄弱

作为一篇理论论文，附录中的算法描述较为简略。对于 practitioners 来说，如果能提供一个 **practical implementation guide** 并开源代码（如 R 或 Python 包），将大大提升论文的影响力。

### 不足四：Comparison 部分

建议增加与现有鲁棒估计器（如 **Hampel et al. 的 M-estimation** 在流形上的推广）的明确对比，论证贝叶斯方法相比频率学派的优势。

---

## 七、总体评价

| 维度 | 评价 |
|------|------|
| **创新性** | 优秀 — 将鲁棒贝叶斯推断与黎曼子流形结合是全新视角 |
| **技术深度** | 优秀 — 建立了流形后验收缩的完整理论 |
| **写作质量** | 良好 — 逻辑清晰，但部分证明细节过于依赖附录 |
| **影响力** | 高 — 为几何统计领域提供了鲁棒推断的新基础 |
| **与现有工作关系** | 优秀 — 与 2022 年 minimax 工作形成系列，引用充分 |

---

## 八、决定

**Major Revision**

本论文的理论框架是 solid 的，主要贡献明确且重要。存在的问题（污染分布假设的泛化、计算实现细节）是可以通过修改改进的。建议作者：

1. 在 Introduction 中增加对一般黎曼流形情形的讨论
2. 补充更多模拟实验（特别是高维情形）
3. 完善算法实现的描述

本论文经过修改后有望达到发表水准。

---

**Confidential Comments to Editor**

这是一篇来自 Rong Tang 研究团队的高水平理论论文，与该团队 2022 年的 minimax 最优速率工作形成互补。理论结果是 solid 的，创新性明确。建议 Major Revision，邀请作者回应关于适用范围和计算实现方面的疑虑。

**推荐修改后发表。**
