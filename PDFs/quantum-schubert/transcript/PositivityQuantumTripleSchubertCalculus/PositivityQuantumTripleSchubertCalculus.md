# Positivity in quantum triple Schubert calculus

2026 年 1 月 3 日

1 差分算子与约化字  
2 双舒伯特多项式的定义与例子  
3 双舒伯特多项式的乘积展开示例

# 差分算子与约化字

1. 线性差分算子定义对 $1 \leq i \leq n - 1$ , 定义 $P _ { n } = \mathbb { Z } [ x _ { 1 } , \ldots , x _ { n } ]$ 上的线性算子:

$$
(\partial_ {i} f) (x) = \frac {f (x _ {1} , \ldots , x _ {i} , x _ {i + 1} , \ldots , x _ {n}) - f (x _ {1} , \ldots , x _ {i + 1} , x _ {i} , \ldots , x _ {n})}{x _ {i} - x _ {i + 1}}
$$

2. 约化字对置换 $w \in S _ { n }$ , 其 约化字 是序列 $\mathbf { a } = ( a _ { 1 } , \ldots , a _ { p } )$ 满足:

$w = s _ { a _ { 1 } } \cdot \cdot \cdot s _ { a _ { p } }$ $\begin{array} { r } { \boldsymbol { s } _ { i } = \left( i , i + 1 \right) } \end{array}$ 为简单对换);  
$p = { \mathfrak { I } } ( w )$ (置换 $w$ 的长度).

3. 置换对应的差分算子 (良定义性) 对序列 $\mathbf { a } = ( a _ { 1 } , \ldots , a _ { p } )$ , 定义 $\partial _ { \mathbf { a } } = \partial _ { a _ { 1 } } \cdot \cdot \cdot \partial _ { a _ { p } }$ , 且:

# Proposition

1 若 $\mathbf { a } , \mathbf { b } \in R ( w )$ , 则 $\partial _ { \mathbf { a } } = \partial _ { \mathbf { b } }$ ;  
2 若 a 非约化, 则 $\partial _ { \mathbf { a } } = 0$ .

故 $\partial _ { w } = \partial _ { \mathbf { a } }$ (a 为 $w$ 的任意约化字) 是良定义的.

# 双舒伯特多项式: 定义与例子

# 定义 (双舒伯特多项式)

设 $x = ( x _ { 1 } , \ldots , x _ { n } ) , y = ( y _ { 1 } , \ldots , y _ { n } )$ , 基多项式:

$$
\mathfrak {S} _ {w _ {0}} (x, y) := \prod_ {i + j \leq n} (x _ {i} + y _ {j})
$$

对任意置换 $w \in S _ { n }$ , 双舒伯特多项式定义为:

$$
\mathfrak {S} _ {w} (x, y) = \partial_ {w ^ {- 1} w _ {0}} ^ {(x)} \mathfrak {S} _ {w _ {0}} (x, y)
$$

(∂(x) $( \partial _ { w ^ { - 1 } w _ { 0 } } ^ { ( x ) }$ -1w 是作用在 $x$ 变量上的差分算子).

我们在下一页给出具体的几个双舒伯特多项式的例子.

# 几个具体的双舒伯特多项式

# 例子 1 (S2 中的双舒伯特多项式)

<table><tr><td>置换 w∈S2</td><td>双舒伯特多项式 Sw(x,y)</td></tr><tr><td>id</td><td>(x1+y1)(x1+y2)(x2+y1)</td></tr><tr><td>s1=(1 2)</td><td>(x1+y1)(y1-y2)</td></tr></table>

# 例子 2 (S3 中的双舒伯特多项式)

<table><tr><td>置换w∈S3</td><td>双舒伯特多项式 Sw(x,y)</td></tr><tr><td>w0=321</td><td>(x1+y1)(x1+y2)(x1+y3)(x2+y1)(x2+y2)(x3+y1)</td></tr><tr><td>s2=(2 3)</td><td>(x1+y1)(x1+y2)(x1+y3)(x2+y1)(x3+y1)</td></tr><tr><td>s1s2=(1 2 3)</td><td>(x1+y1)(x1+y2)(x3+y1)(y1-y2)</td></tr></table>

# 双舒伯特多项式的乘积

我们尤其关注两个双舒伯特多项式乘积的展开. 事实上, 我们有如下的结果:

# 定理

对 $u , v \in S _ { n }$ , 双舒伯特多项式的乘积可展开为:

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; z) = \sum_ {w \in S _ {\infty}} c _ {u v} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

这个展开式的存在性和唯一性是 Lascoux 和 Schützenberger 在双定义舒伯特多项式时(1980) 就已经给出了.

# 具体的例子

我们给出两个简单的例子, 并观察它们展开式的各项系数.

例

$$
\mathfrak {S} _ {\mathrm {i d}} (x, y) \mathfrak {S} _ {s _ {1}} (x, z) = \left(y _ {1} - z _ {1}\right) \mathfrak {S} _ {\mathrm {i d}} (x, y) + \mathfrak {S} _ {s _ {1}} (x, y)
$$

例

$$
\mathfrak {S} _ {s _ {1}} (x, y) \mathfrak {S} _ {s _ {2}} (x, z) = \mathfrak {S} _ {s _ {1} s _ {2}} (x, y) + \mathfrak {S} _ {s _ {2} s _ {1}} (x, y) + (y _ {1} - z _ {1} + y _ {2} - z _ {2}) \mathfrak {S} _ {s _ {1}} (x, y)
$$

我们发现, 上述两个例子中, 右侧展开式的系数都是属于 $\mathbb { N } [ y _ { i } - z _ { j } ]$ . 事实上, 我们有如下的定理.

定理 (Yibo Gao, Rui Xiong)

对于 $u , v , w \in S _ { \infty }$ , 有 $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { z } ) \in \mathbb { N } [ y _ { i } - z _ { j } ] _ { i , j \geq 1 } .$

# 量子双舒伯特多项式: 生成函数

设 x = (x1, . . . , xn), y = (y1, . . . , yn) 为两组变量. 对 $k \geq 1$ , 我们首先定义 量子初等对称多项式的生成函数:

$$
\Delta_ {k} (t \mid x _ {1}, \dots , x _ {k}) := \sum_ {j = 0} ^ {k} t ^ {k - j} e _ {j} (x _ {1}, \dots , x _ {k} \mid q _ {1}, \dots , q _ {k - 1})
$$

其中 $e _ { j } ( x \mid q )$ 是量子初等对称多项式, 且该生成函数等价于三对角矩阵的行列式:

$$
\Delta_ {k} (t \mid x) = \det  \left( \begin{array}{c c c c} x _ {1} + t & q _ {1} & \ldots & 0 \\ - 1 & x _ {2} + t & \ddots & \vdots \\ \vdots & \ddots & \ddots & q _ {k - 1} \\ 0 & \ldots & - 1 & x _ {k} + t \end{array} \right)
$$

# 量子双舒伯特多项式的定义

接着, 我们可以定义 $S _ { n }$ 中最长置换对应的量子双舒伯特多项式:

# 定义 (Sn 的最长元的量子双舒伯特多项式)

对最长置换 $w _ { 0 } \in S _ { n }$ , 其对应的量子双舒伯特多项式为:

$$
\mathfrak {S} _ {w _ {0}} ^ {(q)} (x, y) = \prod_ {i = 1} ^ {n - 1} \Delta_ {i} \left(y _ {n - i} \mid x _ {1}, \dots , x _ {i}\right)
$$

基于上面的两个概念, 我们给出任意置换的量子双舒伯特多项式的定义:

# 定义 (量子双舒伯特多项式)

对任意置换 $w \in S _ { n }$ , 量子双舒伯特多项式定义为:

$$
\mathfrak {S} _ {w} ^ {(q)} (x, y) = \partial_ {w w _ {0}} ^ {(y)} \mathfrak {S} _ {w _ {0}} ^ {(q)} (x, y)
$$

其中 $\partial _ { w w _ { 0 } } ^ { ( y ) }$ 是作用在 $y$ 变量上的差分算子.

# 经典正性结果回顾

对 $u , v \in S _ { n }$

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; z) = \sum_ {w \in S _ {\infty}} c _ {u v} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

该式中的系数满足:

$$
c _ {u, v} ^ {w} (\mathbf {y}, \mathbf {z}) \in \mathbb {N} [ y _ {i} - z _ {j} ] _ {i, j \geq 1}
$$

# 研究目标: 量子双舒伯特多项式的正性猜想

基于上述结果, 我们猜测经典双舒伯特多项式的正性结果在量子的情形下依然成立:

# 量子双舒伯特多项式的正性

对 $u , v , w \in S _ { \infty }$ , 量子双舒伯特多项式的乘积展开:

$$
\mathfrak {S} _ {u} ^ {(q)} (x; y) \mathfrak {S} _ {v} ^ {(q)} (x; z) = \sum_ {w \in S _ {n}} c _ {u v} ^ {w, (q)} (y; z; q) \mathfrak {S} _ {w} ^ {(q)} (x; y)
$$

其系数满足 $c _ { u v } ^ { w , ( q ) } ( y ; z ; q ) \in \mathbb { N } [ y _ { i } - z _ { j } , q _ { k } ] _ { i , j \geq 1 , k \geq 1 } .$

# 双舒伯特多项式的几何对应

# 几何背景

设

$$
F I _ {n} = G L _ {n} (\mathbb {C}) / B
$$

为完全旗流形， $T \subset G L _ { n }$ 为极大代数环。

# Schubert 子簇

每个置换 $w \in S _ { n }$ 对应一个 Schubert 子簇

$$
X _ {w} = \overline {{B w B / B}} \subset F I _ {n}.
$$

其 T-等变上同调类

$$
\left[ X _ {w} \right] ^ {T} \in H _ {T} ^ {*} (F I _ {n})
$$

构成 $H _ { T } ^ { * } ( F I _ { n } )$ 的一组 Z[t]-基。

有标准同构

$$
H _ {T} ^ {*} (F I _ {n}) \cong \frac {\mathbb {Z} [ x _ {1} , \ldots , x _ {n} , y _ {1} , \ldots , y _ {n} ]}{\langle f (x) - f (y) \mid f \text {对 称} \rangle}.
$$

在该同构下：

$$
\boxed {[ X _ {w} ] ^ {T} \longleftrightarrow \mathfrak {S} _ {w} (x; y)}
$$

即：双舒伯特多项式是等变 Schubert 类的显式代表。

# 几何含义

考虑乘积

$$
\mathfrak {S} _ {u} (x; y) \cdot \mathfrak {S} _ {v} (x; t).
$$

几何上对应于：

$$
\left[ X _ {u} \right] ^ {T} \cdot \left[ X _ {v} \right] ^ {T}
$$

其中 T 与 T′ 是两个不同的等变结构。

展开式的几何意义

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; t) = \sum_ {w} c _ {u, v} ^ {w} (y, t) \mathfrak {S} _ {w} (x; t)
$$

等价于：

$$
\left[ X _ {u} \right] ^ {T} \cdot \left[ X _ {v} \right] ^ {T ^ {\prime}} = \sum_ {w} c _ {u, v} ^ {w} (y, t) \left[ X _ {w} \right] ^ {T ^ {\prime}}.
$$

系数 $c _ { u , v } ^ { w } ( y , t )$ 描述的是等变交在 Schubert 基下的分解。

# 系数正性的几何含义

# 正性猜想

$$
c _ {u, v} ^ {w} (y, t) \in \mathbb {N} [ t _ {i} - y _ {j} | i, j \geq 1 ]
$$

# 几何解释

。 $c _ { u , v } ^ { w } ( y , t )$ 是一个等变结构常数  
它描述 $X _ { u }$ 与 $X _ { v }$ 的等变交  
$t _ { i } - y _ { j }$ 是 $\tau \times \tau$ 在固定点处的权

# 正性意味着：

Schubert 子簇的等变交是有效代数循环  
等变局部化后，每个固定点贡献为非负权重

# 谢谢观看!