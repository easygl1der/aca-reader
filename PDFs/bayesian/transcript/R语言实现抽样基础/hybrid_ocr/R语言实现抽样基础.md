# R语言实现抽样基础

# 离散型随机变量

已知 $P\left(X = x_{i}\right) = p_{i}, i = 1, \ldots, n$ 。根据以上概率分布抽取 100 个样本。

$$
\begin{array}{l} > x <   - c (\dots); p <   - c (\dots); n <   - l e n g t h (x) \\ > \text {i n d e x} <   - \text {s a m p l e} (1: n, 1 0 0, \text {r e p l a c e} = T, \text {p r o b} = p); x _ {\text {s a m p l e}} <   - x [ \text {i n d e x} ] \\ > x \_ s a m p l e <   - s a m p l e (x, 1 0 0, r e p l a c e = T, p r o b = p) \\ \end{array}
$$

# 连续型随机变量

已知 $X$ 密度函数为 $f(x)$ 。根据以上密度函数抽取 100 个样本。

在 $X$ 的支撑（取值范围，设为 $[a, b]$ ）内均匀地“打格子点”，即令 $a = x_{1} \leq \cdots \leq x_{n} = b$ ，且 $x_{i}$ 的间隔一样，并计算 $p_{i} = f(x_{i})$ ，然后按离散概率的抽样方式从 $x_{i}$ 中抽取 100 个样本即可。

# 连续型随机变量

$$
\begin{array}{l} P (X = x _ {i}) \approx P (x _ {i} \leq X \leq x _ {i} + \Delta x) = P (X \leq x _ {i} + \Delta x) - P (X \leq x _ {i}) = \\ F (x _ {i} + \Delta x) - F (x _ {i}) = F ^ {\prime} (\xi) \cdot \Delta x = f (\xi) \cdot \Delta x \approx f (x _ {i}) \Delta x \\ \end{array}
$$

$$
\xi \in [ x _ {i}, x _ {i} + \Delta x ]
$$

可见， $P(X = x_{i}) \propto f(x_{i})$ 。

# 例：从U(0,1)中抽取样本

> x<-seq(0, 1, length=500)   
> p<-rep(1/500, 500)   
> x_sample<-sample(x, 100, replace=T, prob=p)

注: p不一定需要是概率

> p<-rep(1, 500)

# 例：从N(0,1)中抽取样本

> x<-seq(-3, 3, length=500)   
> p<-dnorm(x, 0, 1)   
> x_sample<-sample(x, 100, replace=T, prob=p)

注：概率可以为密度函数的核

$> p<-exp(-0.5^{*}x^{\wedge}2)$

# 二维离散型随机向量

已知 $P\left(X = x_{i}, Y = y_{j}\right) = p_{ij}, i = 1, \ldots, I; j = 1, \ldots, J$ 。根据以上概率分布抽取 100 个样本。

把数据矩阵“拉直”为一个向量，即令 $P(Z = k) = P\big(X = x_{i}, Y = y_{j}\big), k = 1,2,\ldots,I \times J$ ，并记此概率为 $\tilde{p}_{k}$ 。然后按照离散型随机变量的方式抽取100个 $Z$ 的样本，并把 $k$ 对应回 $x_{i}$ 和 $y_{j}$ 即可。

# 二维离散型随机向量

$>\mathrm{x}<-\mathrm{c}(\ldots);\mathrm{y}<-\mathrm{c}(\ldots);\mathrm{l}<-\mathrm{length}(\mathrm{x});\mathrm{J}<-\mathrm{length}(\mathrm{y})$   
> $p<-matrix(..., nrow=1, ncol=J)$   
> p2<-as.vector(p) #注：按列拉直   
> index<-sample(1:(I*J), 100, replace=T, prob=p2)   
> index1<- (index-1)%%|+1; index2<- (index-1)%%|+1   
> data_sample<-cbind(x[index1], y[index2])

# 二维离散型随机向量

1. 计算 $X$ 的边缘概率，并记为 $p_{i + }$ 。按照 $p_{i + }$ 的概率从 $x_{i}$ 中抽取 100 个样本，记为 $x_{1}^{*}, \ldots, x_{100}^{*}$ 。  
2. 对 $k = 1, \ldots, 100$ , 计算条件概率 $P(Y = y_{j} | X = x_{k}^{*})$ , 并记为 $p_{j \mid k}^{*}$ 。按照 $p_{j \mid k}^{*}$ 的概率从 $y_{j}$ 中抽取壹个样本, 并记为 $y_{k}^{*}$ 。  
3. 样本 $(x_{1}^{*}, y_{1}^{*}), \ldots, (x_{100}^{*}, y_{100}^{*})$ 即为所得。

# 二维离散型随机向量

$>\mathrm{x}<-\mathrm{c}(\ldots);\quad \mathrm{y}<-\mathrm{c}(\ldots);\quad \mathrm{l}<-\mathrm{length}(\mathrm{x});\quad \mathrm{J}<-\mathrm{length}(\mathrm{y})$   
> p<-matrix(..., nrow=1, ncol=J); px<-rowSums(p)   
> index1<-sample(1:I, 100, replace=T, prob=px)   
> index2<-numeric(100)   
> for (i in 1:100) { index2[i]<-sample(1:J, 1, prob=p[index1[i],])}   
> data_sample<-cbind(x[index1], y[index2])

# 二维离散型随机向量

$>\mathrm{x}<-\mathrm{c}(\ldots);\quad \mathrm{y}<-\mathrm{c}(\ldots);\quad \mathrm{l}<-\mathrm{length}(\mathrm{x});\quad \mathrm{J}<-\mathrm{length}(\mathrm{y})$   
> p<-matrix(..., nrow=1, ncol=J); py<-colSums(p)   
> index2<-sample(1:J, 100, replace=T, prob=py)   
> index1<-numeric(100)   
> for (i in 1:100) { index1[i]<-sample(1:i, 1, prob=p[,index2[i]])}   
> data_sample<-cbind(x[index1], y[index2])

# 二维连续型随机向量

已知 $(X, Y)$ 的密度函数为 $f(x, y)$ 。根据以上概率分布抽取 100 个样本。

在 $(X, Y)$ 的支撑（取值范围，设为 $[a, b] \times [c, d]$ ）内均匀地“打格子点”，得 $(x_{i}, y_{j})$ ，并计算 $p_{ij} = f(x_{i}, y_{j})$ ，然后按二维离散概率的抽样方式从 $(x_{i}, y_{j})$ 中抽取100个样本即可。