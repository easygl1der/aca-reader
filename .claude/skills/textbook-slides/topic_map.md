# Topic ↔ Chapter 映射 (topic_map.md)

> 由 topic-mapper agent 生成。

## Gauss-Markov PPT 详细映射

| 属性 | 值 |
|------|-----|
| **PPT 文件** | `Gauss-Markov.pptx` |
| **对应教材** | Chapter 04 (Gauss-Markov Theorem) |
| **PPT 路径** | `PDFs/applied-linear-regression/ALR/Gauss-Markov.pptx` |
| **教材路径** | `PDFs/applied-linear-regression/chapters/chapter04_gauss.tex` |
| **Slide 数量** | 20 张 |
| **核心内容** | BLUE, 最佳线性无偏估计, OLS 性质 |
| **跳过的内容** | 完整证明细节、 Homework 题目 |

### Slide → 教材详细映射

| Slide # | Slide 标题 | 教材来源 | 关键内容 |
|---------|-----------|---------|---------|
| 1 | Gauss-Markov Model | §4.1 标题 | Chapter 4 引言：Gauss-Markov 模型与定理 |
| 2 | Regression model | §4.1 (Assumption 4.1) | $Y = X\beta + \varepsilon$ 模型定义 |
| 3 | Linear model | §4.1 | 线性模型假设，固定设计矩阵 $X$ |
| 4 | Enables statistical inference | §4.1 | 为什么需要统计假设才能做统计推断 |
| 5 | Gauss-Markov | §4.1 (Assumption 4.1) | $E(\varepsilon) = 0$, $\cov(\varepsilon) = \sigma^2 I_n$ |
| 6 | OLS properties | §4.2, Theorem 4.1 | $E(\hat{\beta}) = \beta$ 无偏性 |
| 7 | OLS properties | §4.2, Theorem 4.1 | $\cov(\hat{\beta}) = \sigma^2(X^T X)^{-1}$ |
| 8 | OLS properties | §4.2, Lemma 4.1 | 投影矩阵 $H$ 和 $I_n - H$ 的性质 |
| 9 | Variance estimation | §4.3 | $\sigma^2$ 估计问题，残差平方和 RSS |
| 10 | Variance estimation | §4.3, Theorem 4.2 | $\hat{\sigma}^2 = \text{RSS}/(n-p)$ 无偏估计 |
| 11 | Revisit the sample variance formula | §4.3 | $E(\text{RSS}) = \sigma^2(n-p)$ 推导 |
| 12 | Revisit the pooled sample variance formula | §4.3 | 为什么用 $n-p$ 而不是 $n$ |
| 13 | Revisit the SSW (Sum of Squares Within) | §4.3 | $\hat{\varepsilon}^T \hat{\varepsilon}$ 与方差估计关系 |
| 14 | Gauss-Markov theorem | §4.4, Theorem 4.3 | BLUE 定义：最佳线性无偏估计 |
| 15 | Gauss-Markov theorem | §4.4 | $\cov(\tilde{\beta}) \succeq \cov(\hat{\beta})$ 含义 |
| 16 | Gauss-Markov theorem | §4.4 | 条件 (C1) 线性性，条件 (C2) 无偏性 |
| 17 | Gauss-Markov theorem: proof | §4.4, 证明 | 协方差分解：$\cov(\tilde{\beta} - \hat{\beta}) \succeq 0$ |
| 18 | Other | §4.4 扩展 | 无用回归子、子样本平均等 |
| 19 | If the Gauss-Markov model holds except for homoskedasticity, what changes? | §4.4 注 | 异方差情况下 OLS 不再 BLUE，需要 WLS |
| 20 | A modern Gauss-Markov Theorem? | §4.4 | 现代扩展：Lasso 等 penalized 方法 |

## 完整映射表（16 个 PPT）

| PPT 文件 | Topic | 对应章节 | Slide 数量 |
|----------|-------|---------|------------|
| OLS asymptotics.pptx | OLS 渐近性 | Ch03 / ChA3 | ~20 |
| Normal linear model.pptx | 正态线性模型 | Ch05 | ~25 |
| Gauss-Markov.pptx | BLUE | Ch04 | 20 |
| model checking.pptx | 模型诊断 | Ch13 | ~30 |
| overfitting.pptx | 过拟合 | Ch13 / Ch14 | ~20 |
| weighted OLS.pptx | 加权 OLS | Ch19 | ~15 |
| transformation.pptx | 变量变换 | Ch16 | ~20 |
| partial regression.pptx | 部分回归 | Ch07 (Frisch-Waugh-Lovell) | ~25 |
| GLM.pptx | 广义线性模型 | Ch23/25 | ~30 |
| logistic regression (binary).pptx | 二分类 Logit | Ch20/21 | ~25 |
| logistic regression (categorical).pptx | 多分类 Logit | Ch21 | ~25 |
| count outcomes.pptx | 计数模型 | Ch26 / GLM | ~20 |
| Lasso.pptx | Lasso | Ch15 | ~25 |
| ridge regression.pptx | Ridge 回归 | Ch14 | ~20 |
