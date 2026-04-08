# Minimax Nonparametric Two-Sample Test under Adversarial Losses

Rong Tang University of Illinois Urbana-Champaign

Yun Yang University of Illinois Urbana-Champaign

# Abstract

In this paper, we consider the problem of twosample hypothesis testing that aims at detecting the difference between two probability densities based on finite samples. The proposed test statistic is constructed by first truncating a sample version of a negative Besov norm and then normalizing it. Here, the negative Besov norm is the norm associated with a Besov space with negative exponent, and is shown to be closely related to a class of commonly used adversarial losses (or integral probability metrics) with smooth discriminators. Theoretically, we characterize the optimal detection boundary of two-sample testing in terms of the dimensionalities and smoothness levels of the underlying densities and the discriminator class defining the adversarial loss. We also show that the proposed approach can simultaneously attain the optimal detection boundary under many common adversarial losses, including those induced by the $\ell _ { 1 }$ , $\ell _ { 2 }$ distances and Wasserstein distances. Our numerical experiments show that the proposed test procedure tends to exhibit higher power and robustness in difference detection than existing state-of-the-art competitors.

The problem of two-sample hypothesis testing, which aims at determining whether two underlying probability densities are significantly different based on their samples, has been a central topic in statistics and machine learning. Many classic two-sample tests follow parametric approaches, which are designed based on prior information about the parametric form of the underlying distributions, like Gaussianity. Examples of classic parametric two-sample tests include Pearson’s chi-squared test (Pearson, 1900), Student’s $t$ -test (Student, 1908) and Hotelling’s two-sample test (Hotelling, 1931).

# 1 Introduction

On the other hand, nonparametric two-sample test procedures avoid making any restrictive parametric assumptions on the distributions, and therefore tends to be more robust while less efficient when the parametric assumption indeed holds. There are rich literatures regarding the nonparametric two-sample testing problem. Nonparametric comparison for one-dimensional samples was done in the minimax sense in $\ell _ { 2 }$ distance by Ingster (1986) via a $\chi ^ { 2 }$ -type test statistic. Butucea and Tribouley (2006) proposed a minimax univariate two-sample testing procedure in $\ell _ { 2 }$ and $\ell _ { \infty }$ distances based on the wavelet expansion, and the proposed procedure is adaptive to the smoothness of the underlying densities. Multivariate nonparametric two-sample testing problems have also been investigated in the literature. Friedman and Rafsky (1979) used the idea of minimal spanning tree (MST) to generalize the univariate test. Xing et al. (2019) addresses the problem of comparing probability density distributions by establishing a connection with interaction testing, and they propose a minimax optimal penalized likelihood ratio test for conducting interaction testing in this scenario. Gretton et al. (2012a); Li and Yuan (2019); Gretton et al. (2009a, 2012b) proposed two-sample tests based on Maximum Mean Discrepancy (MMD). In particular, Li and Yuan (2019) showed that two-sample tests via Gaussian kernel embedding with an appropriately chosen scaling parameter can attain the minimax optimal rate $n ^ { - \frac { 2 \alpha } { 4 \alpha + d } }$ in $\ell _ { 2 }$ loss for $\alpha$ -smooth $d$ -dimensional densities. Other nonparametric approaches for two-sample testing include Schilling (1986); Henze (1988); Liu and Modarres (2011); Biswas and Ghosh (2014); Wang et al. (2021).

The test statistics for nonparametric two-sample tests are usually constructed based on finite-sample surrogates to some metrics quantifying the discrepancy between the two populations, including the $\ell _ { p }$ distance (Györfi and Van Der Meulen, 1991), Wasserstein distance (Ramdas et al., 2017) and Maximum Mean Discrepancy (MMD, Gretton et al., 2012a, 2009b; Li and Yuan, 2019). These metrics can all be embraced into a general family of discrepancy measures on distributions, called adversarial losses, which are also called integral probability metrics (IPM) in the probability literature, defined as

$$
d _ { \mathcal { F } } ( p , q ) = \operatorname* { s u p } _ { f \in \mathcal { F } } \Big | \int _ { \mathcal { X } } f ( x ) \mathrm { d } p ( x ) - \int _ { \mathcal { X } } f ( x ) \mathrm { d } q ( x ) \Big | ,
$$

where $\mathcal { X } \subset \mathbb { R } ^ { d }$ denotes the data space, and $\mathcal { F }$ is the discriminator class composed of a subset of all Borel-measurable functions. Note that if the discriminator class satisfies ${ \mathcal { F } } = - { \mathcal { F } }$ , then it is not necessary to take the absolute value inside (1) . Different choices of $\mathcal { F }$ leads to different adversarial losses. However, except for some special cases such as when $\mathcal { F }$ is the unit ball of a reproducing kernel Hilbert space (RKHS) (Li and Yuan, 2019; Sriperumbudur et al., 2010) or the dimensionality $d$ equals to one (Del Barrio et al., 1999), the adversarial loss in (1) lacks a closed-form expression. For practical computations, we need to numerically solve the optimization problem of maximizing the difference over the discriminator class.

In this work, we consider a broad class of adversarial losses indexed by a smoothness (level) parameter $\gamma \in \mathsf { \Gamma } [ 0 , \infty )$ , which are shown to equivalent to the negative Besov norms. Here, the negative Besov norm is the norm associated with a Besov space (Triebel, 2006, 2010) with negative exponent. Since the smoothness parameter $\gamma$ can be interpreted as the weights that penalize the high-order wavelet coefficients (high frequency components) in the wavelet expansion of the difference between the two distributions of concern, we propose to approximate the population level negative Besov norm by truncating its empirical version (c.f. Lemma 2). By further normalizing this truncated finite-sample surrogate to the negative Besov norm, we define a set of test statistics that are asymptotically standard normal under the null hypothesis and tends to infinity in the presence of any significant difference between the two distributions. In addition, when the populations of concern have $d$ -dimensional densities that are at least $\alpha$ -smooth, for some suitably chosen penalizing weights (i.e., the exponent of the negative Besov norm), the constructed tests can detect the distributional difference at our derived optimal separation rate $O ( n ^ { - \frac { 2 ( \alpha + \gamma ) } { 4 \alpha + d } } + n ^ { - \frac { 1 } { 2 } } )$ up to inessential logarithmic terms, simultaneously under all adversarial losses with $\gamma$ -smooth $( \gamma \in [ 0 , \infty ] )$ discriminators, which includes the commonly-used $\ell _ { 1 } , \ell _ { 2 }$ distances and the 1-Wasserstein distance (Santambrogio, 2015; Villani, 2009) as special cases. The result also rigorously verifies conventional wisdom that testing is usually easier than estimation, as our derived rate for testing is smaller than the minimax rate for estimation $O ( n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } + n ^ { - \frac { 1 } { 2 } } )$ (Uppal et al., 2019) under the same loss functions. Empirically, we compare our approach with the state-of-the-art nonparametric twosample test based on MMD with Gaussian kernels; it turns out that our approach outperforms the Gaussian-MMD test in terms of both detection power and robustness to hyperparameters.

The rest of the paper is organized as follows. In Section 2, we give a brief introduction to the adversarial loss. In Section 3, we show the equivalence between a class of representative adversarial losses and the negative Besov norm. We also provide an empirical surrogate to the negative Besov norm based on finite samples in Section 4. In

Section 5, we first derive the minimax rate of nonparametric two-sample testing under adversarial losses, and then propose a minimax-optimal test procedure based on the empirical surrogate from Section 4. Simulations and a real data application are included in Section 6 and 7.

# 2 Adversarial losses

Many recent machine learning studies employ the adversarial loss as an alternative to the conventional $\ell _ { p }$ distances for characterizing the closeness between probability measures (Arjovsky et al., 2017; Tolstikhin et al., 2017). The adversarial loss defined in (1) can realize a large family of probability metrics by suitably choosing the discriminator class $\mathcal { F }$ . We focus on the following adversarial losses where $\mathcal { F }$ is the unit ball within the Sobolev-2 class or Hölder class, denoted as $\mathscr { W } _ { 1 } ^ { \gamma } ( \Omega )$ and $\mathscr { C } _ { 1 } ^ { \gamma } ( \Omega )$ respectively, with smoothness level $\gamma \geq 0$ (the formal definition of $\mathscr { W } _ { 1 } ^ { \gamma } ( \Omega )$ and $\mathscr { C } _ { 1 } ^ { \gamma } ( \Omega )$ can be found in the supplementary material), for which the corresponding metrics are respectively denoted as $d _ { \gamma } ^ { W } ( \cdot , \cdot )$ and $d _ { \gamma } ^ { H } ( \cdot , \cdot )$ .

Adversarial losses are more suitable to characterize discrepancies between nearly singular distributions, such as those arising from high-dimensional data with low-dimensional structures, than many conventional metrics including the $\ell _ { p }$ distances due to their robustness against distribution perturbations. In particular, the metric $d _ { \gamma } ^ { W }$ (or $d _ { \gamma } ^ { H }$ ) becomes stronger as $\gamma$ decreases. By taking $\gamma = 0$ , $d _ { \gamma } ^ { W }$ and $d _ { \gamma } ^ { H }$ are equivalent to the $\ell _ { 2 }$ and $\ell _ { 1 }$ distance, respectively; by taking $\gamma = 1$ , the metric $d _ { \gamma } ^ { H }$ corresponds to the 1-Wasserstein distance (Santambrogio, 2015). The smoothness parameter $\gamma$ controls the sensitivity of the metric to oscillations: a smaller $\gamma$ makes $d _ { \gamma } ^ { W } , d _ { \gamma } ^ { H }$ more sensitive to high frequency components of the density. For example, consider a $d$ -dimensional random variable $X$ with support lying close to a low dimensional submanifold. More specifically, we consider the following probabilistic model

$$
p ( X | z ) = \mathcal { N } ( G ( z ) , \sigma ^ { 2 } I _ { d } ) , \qquad z \sim \mathcal { N } ( 0 , I _ { \bar { d } } ) ,
$$

with $d > \bar { d }$ . Model (2) is commonly employed in generative modelling literature for learning data generators for the images of objects (Kingma and Welling, 2013; Doersch, 2016), where the latent variable $z$ can be interpreted as (low dimensional) global characteristics such as camera projection, lighting condition, texture, object position and orientation. Suppose we translate the mean parameter of the conditional distribution of $X$ along a direction inside the normal space of the underlying submanifold $\mathcal { M } = \{ G ( z ) : z \in \overset { \cdot } { \mathbb { R } ^ { d } } \}$ at point $G ( z )$ by a tiny amount $u > 0$ , that is, we consider the following conditional distribution: $p ( X ^ { \prime } | z ) = \mathcal { N } ( G ( z ) + \omega ( z ) \cdot u , \sigma ^ { 2 } I _ { d } )$ , where $\omega ( z )$ is a unit vector perpendicular to the tangent space of $\mathcal { M }$ at $G ( z )$ (see Figure 1 for an illustration). In this example, the Wasserstein distance between marginal distributions of $X$ and $X ^ { \prime }$ is of order $O ( | u | )$ regardless of the order of $\sigma$ ; while the corresponding $\ell _ { p }$ distance can be of order $O ( 1 )$ given that $| u / \sigma | = O ( 1 )$ . This suggests that when used as a discrepancy measure for distribution estimation, the $\ell _ { p }$ distance is much more sensitive to oscillations and support mismatching. As a consequence, the detection boundary under the $\ell _ { p }$ distance will be extremely large for nearly singular distributions. This is because some "physically close" distributions that are difficult to distinguish may have large $\ell _ { p }$ distances due to their supports not perfectly aligning with the support of the original data. On the other hand, the adversarial loss with smoother discriminator class honestly quantifies the amount of support mismatch and therefore more suitable for quantifying the discrepancy between nearly singular distributions.

![](images/8ed2e80b0a79ed225764aa532afcc1933df5822dd00b568fa7196558b5f16a4a.jpg)  
Figure 1: The figure shows the random samples from the distribution of $X$ (Blue points) and $X ^ { \prime }$ (Orange points) with $d = 2$ , $\bar { d } = 1$ , $G ( z ) = ( z , z )$ , $u = 0 . 3$ and $\sigma = 0 . 1$ . We can see that the shape and the location of the two scatter plots are quite similar, yet the $\ell _ { p }$ distance is quite large due to the support mismatching.

# 3 Wavelet Transform and Besov Norm

The wavelet transform is a powerful exploratory data analysis tool that can efficiently represent signals with slowly varying trend and abrupt changes interrupting smooth regions. Roughly speaking, a wavelet is a rapidly decaying wave like oscillation that exists for a finite duration. Commonly-used wavelets includes Haar wavelet (Triebel, 2010), Meyer wavelet (Triebel, 2006; Meyer, 1992), Daubechies wavelet (Daubechies, 1988), etc. One of the key concepts in wavelet transform is the scaling, which refers to the process of stretching or shrinking the wavelet along the features. A stretched wavelet helps in capturing the slowly varying trends in a signal; while a shrinking wavelet helps in detecting the abrupt changes.

Concretely, let $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ denote the set of all square integrable functions on $\mathbb { R } ^ { d }$ . It is possible to define a complete orthonormal basis $\{ \overline { { \Psi } } _ { j } \} _ { j \ge 0 }$ for $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ so that: the set of level zero basis $\overline { { \Psi } } _ { 0 }$ is formed by shifting some compact scaling function; for any $j \in \mathbb { N } ^ { + }$ , the set of level $j$ basis $\overline { { \Psi } } _ { j }$ is obtained by shifting some compact wavelet function and scaling it by a factor of $2 ^ { - ( j - 1 ) }$ ; and any function $p \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ can

be uniquely expressed as

$$
p ( x ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } p _ { \psi } \psi ( x ) \quad \mathrm { w i t h } \quad p _ { \psi } = \int _ { \mathbb { R } ^ { d } } \psi ( x ) p ( x ) \mathrm { d } x .
$$

Further detail is included in Appendix B. As described above, for $\psi \in \Psi _ { j }$ , when the level $j$ is small, the wavelet coefficient $p _ { \psi }$ can capture general trends of the function $p ( \cdot )$ ; on the contrary, with a large level $j$ , the wavelet coefficient $p _ { \psi }$ can capture abrupt changes/oscillations. Therefore, for a smooth function $p ( \cdot )$ not containing large and abrupt oscillations, the wavelet coefficient $p _ { \psi }$ tends to be small for those $\psi$ corresponding to a large level basis. To formally quantify such function oscillations, we can use the so-called Besov norm with exponent $s$ , defined for a smooth level $s \in [ 0 , \infty )$ and $l , m \in \mathbb { N } ^ { + }$ as follows:

$$
\| p \| _ { B _ { l , m } ^ { s } } : = \bigg [ \sum _ { j = 0 } ^ { \infty } 2 ^ { j m ( s + \frac { d } { 2 } - \frac { d } { l } ) } \big ( \sum _ { \psi \in \overline { { \Psi } } _ { j } } | p _ { \psi } | ^ { l } \big ) ^ { \frac { m } { l } } \bigg ] ^ { \frac { 1 } { m } } .
$$

We can correspondingly define the Besov space $B _ { l , m } ^ { s } ( \mathbb { R } ^ { d } )$ as a subspace of $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ equipped with the norm $\| \cdot \| _ { B _ { l , m } ^ { s } }$ . The Besov space is closely related to the Sobolev space: when $l = m = 2$ , the Besov space $B _ { 2 , 2 } ^ { s } ( \mathbb { R } ^ { d } )$ is equivalent to the Sobolev-2 space $\mathcal { W } ^ { s } ( \mathbb { R } ^ { d } )$ ; when $l = m = \infty$ , the Besov space $B _ { \infty , \infty } ^ { s } ( \mathbb { R } ^ { d } )$ is equivalent to the Hölder space $\mathcal { C } ^ { s } ( \mathbb { R } ^ { d } )$ .

Apart from quantifying the smoothness level of a function, by allowing a negative exponent $s$ inside (3), the Besov norm can be used to measure the difference of two functions. In particular, by choosing $l = m = 2$ , $s = - \gamma$ , we can obtain the following distance between two probability density functions $p , q \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ ,

$$
\| p - q \| _ { B _ { 2 , 2 } ^ { - \gamma } } = \Big [ \sum _ { j = 0 } ^ { \infty } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \overline { { \Psi } } _ { j } } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \Big ] ^ { \frac { 1 } { 2 } } .
$$

We call the norm in (4) the negative Besov norm with exponent $\gamma ~ \in ~ [ 0 , \infty )$ . The decaying level $\gamma$ controls the sensitivity of the metric to abrupt changes. By taking $\gamma = 0$ and $l = m = 2$ , we attain the conventional $\ell _ { 2 }$ loss (i.e., $\begin{array} { r } { \big [ \int _ { \mathbb { R } ^ { d } } ( p ( x ) - q ( x ) ) ^ { 2 } \mathrm { d } x \big ] ^ { \frac { 1 } { 2 } } ) } \end{array}$ . However, as described in Section 2, the $\ell _ { 2 }$ distance is sensitive to small wiggles/oscialltions, and may not be suitable for cases where we are also concerned about the slowly varying trends. On the other hand, by choosing a positive $\gamma$ , the influence of high level wavelet coefficients (high frequency component) is controlled by the weight $2 ^ { - 2 j \gamma }$ . The following Lemma shows that the negative Besov norm is equivalent to the adversarial loss with the discriminator class being the Sobolev-2 space.

Lemma 1. For probability density functions $p , q \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ and $\gamma \geq 0$ , we have

$$
c d _ { \gamma } ^ { W } ( p , q ) \leq \left\| p - q \right\| _ { \mathcal { B } _ { 2 , 2 } ^ { - \gamma } } \leq C d _ { \gamma } ^ { W } ( p , q ) ,
$$

where positive constants c and $C$ only depend on $\gamma , d .$

# 4 Empirical Surrogate to Squared Negative Besov Norm

The adversarial loss, even though conceptual appealing, may suffer from lacking a closed-form expression for computations. According to Lemma 1, the adversarial loss $d _ { \gamma } ^ { W }$ is equivalent to the negative Besov norm $\| \cdot \| _ { B _ { 2 , 2 } ^ { - \gamma } }$ with exponent $\gamma$ , up to some multiplicative constant. However, the negative Besov norm is a sum of an infinite series, and can not be computed in a finite number of operations. To this end, we restrict our attention to distributions supported on a bounded domain $\Omega \subset \mathbb { R } ^ { d }$ with smooth densities. Denote by $\mathscr { W } _ { L } ^ { u , \alpha } ( \Omega )$ the subset of $\alpha$ th order Sobolev-2 space $W _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ so that each function is uniformly bounded by $L$ and supported on $\Omega$ , that is,

$$
\begin{array} { c } { { \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega ) = \big \{ p \in \mathcal { W } _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } ) : \operatorname* { s u p } _ { x \in \Omega } \vert p ( x ) \vert \leq L , } } \\ { { \operatorname { s u p p } ( p ) \subset \Omega \big \} , \quad \alpha > 0 . } } \end{array}
$$

Note that here the uniform boundness of the density function is only a technique artifact to simplify the proof, so that magnitudes of high-order (empirical) wavelet coefficients can be properly bounded; it also trivially holds for Hölder smooth density functions. The compactness of the support of the density is for ensuring that only finitely many wavelet coefficients are non-vanishing at a given scale. Consider densities $p , q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , we further choose to truncate the wavelet expansion at a finite level $J$ to attain a best accuracy versus efficiency trade-off, where $J$ is an integer depending on the sample size and smoothness level $\alpha$ that will be chosen later. This leads to the following approximation to the squared negative Besov norm:

$$
\| p - q \| _ { \widehat { B } _ { 2 , 2 } ^ { - \gamma } } ^ { 2 } = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } ,
$$

where $\Psi _ { j } = \{ \psi \in \overline { { \Psi } } _ { j } \ : \ \operatorname { s u p p } ( \psi ) \cap \Omega \neq \emptyset \}$ for $j \geq 0$ . 1 Given the wavelet coefficients $\{ p _ { \psi } , q _ { \psi } \} _ { \psi \in \Psi _ { j } , j \in \mathbb { N } }$ , (5) can be computed in $O ( 2 ^ { d J } )$ number of operations. In statistical applications, the wavelet coefficients are not directly computable, but instead two sets of i.i.d samples $X ^ { ( n ) } =$ $\{ X _ { 1 } , \cdot \cdot \cdot , X _ { n } \} \sim p$ and $Y ^ { ( m ) } = \{ Y _ { 1 } , \cdot \cdot \cdot , { \bar { Y } } _ { m } \} \sim q$ are available. Based on the definition $p _ { \psi } ~ = ~ \mathbb { E } _ { p } [ \psi ( X ) ]$ of the wavelet coefficient, we can estimate $p _ { \psi }$ by replacing the population level expectation with the empirical mean ${ \widehat { p } } _ { \psi } ~ = ~ n ^ { - 1 } \sum _ { i = 1 } ^ { n } \psi ( X _ { i } )$ . However, it is not hard to see bthat $\widehat { p } _ { \psi } ^ { 2 }$ is a biased estimator of $p _ { \psi } ^ { 2 }$ . We then correct for bthe bias and use instead the $U$ -statistic to approximate $p _ { \psi } ^ { 2 }$ which leads to the following statistic that forms an unbiased

estimator to (5),

$$
\begin{array} { l } { \displaystyle T _ { \gamma , J } = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \left[ \frac { 1 } { n ( n - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } \psi ( X _ { i _ { 1 } } ) \psi ( X _ { i _ { 2 } } ) + \right. } \\ { \displaystyle \left. \frac { 1 } { m ( m - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } \psi ( Y _ { i _ { 1 } } ) \psi ( Y _ { i _ { 2 } } ) - \frac { 2 } { n m } \sum _ { i _ { 1 } , i _ { 2 } } \psi ( X _ { i _ { 1 } } ) \psi ( Y _ { i _ { 2 } } ) \right] . } \end{array}
$$

For brevity, we consider the balanced case where $c \ \leq$ $n / m \leq C$ for some constants $0 < c \le C < \infty$ , and express explicitly only the dependence on $n$ and not $m$ in our theoretical results. For general situations, the rate will only depend on the minimum of $n$ and $m$ .

The next lemma shows that by choosing a suitable truncation level $J$ , the statistic $T _ { \gamma , J }$ is a valid estimator to the squared Besov norm in the sense that (1) under the case where the two distributions $p , q$ are the same, $T _ { \gamma , J }$ converges to zero in probability; (2) when the two distributions are sufficiently separated, the ratio of the statistic and squared negative Besov norm converges to one in probability.

Lemma 2. For distributions $p , q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ . Suppose $c \leq n / m \leq C$ for some constants $0 < c \le C < \infty$ . For any $\gamma \geq 0$ , the statistic $T _ { \gamma , J }$ with $J = \lceil \log _ { 2 } ( n ^ { \frac { 2 } { 4 \alpha + d } } ) \rceil$ satisfy the following properties:

1. If $p = q$ , we have $T _ { \gamma , J } \ \xrightarrow { P } \ 0$ , where $\xrightarrow { P }$ means converging in probability;

2. If $d _ { \gamma } ^ { W } ( p , q ) \cdot ( n ^ { \frac { 2 ( \alpha + \gamma ) } { 4 \alpha + d } } \wedge n ^ { \frac { 1 } { 2 } } ) \cdot ( \log n ) ^ { - \frac { 1 } { 2 } } \to \infty ,$ , then we have γ,J∥p−q∥2 $\frac { T _ { \gamma , J } } { \Vert p - q \Vert _ { _ { B _ { 2 , 2 } ^ { - \gamma } } } ^ { 2 } } \stackrel { P } { \longrightarrow } 1$ P−→ 1.

The statistic $T _ { \gamma , J }$ can then be deployed to construct a test statistic for the two-sample hypothesis testing, which we describe in detail in the following section.

A commonly-used metric in literature for measuring the discrepancy between two distributions $p , q$ is the maximum mean discrepancy (MMD). With finite data, the squared MMD between $p , q$ is commonly approximated by the $U$ - statistic:

$$
\begin{array} { l } { \displaystyle { \cal T } _ { h } ^ { \mathrm { M M D } } = \frac { 1 } { n ( n - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } k _ { h } ( X _ { i _ { 1 } } , X _ { i _ { 2 } } ) } \\ { \displaystyle + \frac { 1 } { m ( m - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } k _ { h } ( Y _ { i _ { 1 } } , Y _ { i _ { 2 } } ) - \frac { 2 } { n m } \sum _ { i _ { 1 } , i _ { 2 } } k _ { h } ( X _ { i _ { 1 } } , Y _ { i _ { 2 } } ) , } \end{array}
$$

where $\begin{array} { r } { k _ { h } ( x , y ) = k ( \frac { x - y } { h } ) } \end{array}$ is a positive semi-definite kernel, typically chosen as a Gaussian kernel with bandwidth $h$ . It has been shown that for properly chosen bandwidth, $T _ { h } ^ { \mathrm { M M D } }$ can well approximate the squared $\ell _ { 2 }$ distance (Gretton et al., 2012a). Compared with $T _ { h } ^ { \mathrm { M M D } }$ , the statistic $T _ { \gamma , J }$ can represent a large class of metrics including the $\ell _ { 2 }$ distance by allowing different $\gamma$ . Computationally, due to the compactness of the wavelet function, for any $j \in \mathbb N$ and $X \in \Omega$ , there are only a constant number of $\psi ~ \in ~ \Psi _ { j }$ such that $\psi ( X ) \neq 0$ . Therefore, the statistic $T _ { \gamma , J }$ can be computed in ${ \cal O } ( n J + 2 ^ { d J } )$ number of operations: we need $O ( n J )$ number of operations for obtaining estimators of wavelet coefficients, and $O ( 2 ^ { d J } )$ number of operations to compute the truncated negative Besov norm given the wavelet coefficients. Plugging in the choice of $\bar { J } = \lceil \log _ { 2 } ( n ^ { \frac { 2 } { 4 \alpha + d } } ) \rceil$ , the dependence of the computational complexity of $T _ { \gamma , J }$ in $n$ is $O ( n \log n + n ^ { \frac { 2 d } { 4 \alpha + d } } )$ . While $T _ { h } ^ { \mathrm { M M D } }$ requires $O ( n ^ { 2 } )$ number of operations, which is larger than the number required by $T _ { \gamma , J }$ for $\alpha > 0$ . Moreover, by choosing a positive $\gamma$ the weights $2 ^ { - 2 \gamma j }$ penalize coefficients at high levels and reduce the variance of the statistic. Therefore, $T _ { \gamma , J }$ tends to be robust against the choice of sufficiently large $J$ ’s. In comparison, $\bar { T } _ { h } ^ { \mathrm { M M D } }$ is known to be sensitive to the choice of bandwidth $h$ : a bandwidth value which is too small leads to an estimation with small bias and large variance; while a large bandwidth leads to low variance at the expense of increased bias. It is also worth mentioning that when the populations of concern are $\alpha$ -smooth, the optimal choice of the bandwidth is given by $h = O ( n ^ { - { \frac { 2 } { 4 \alpha + d } } } )$ (Li and Yuan, 2019), which relates to the optimal choice of the truncation level $J$ in our proposed statistic through $2 ^ { - J } \asymp h$ Therefore, any rule for selecting the bandwidth in the MMD test with Gaussian kernel (e.g., the median heuristic, Arlot et al., 2019) can be deployed for selecting $J$ . Additionally, by rearranging the order of summations in the statistic $T _ { \gamma , J }$ , it actually corresponds to a special MMD test $\begin{array} { r } { k _ { \gamma , J } ( x , y ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( x ) \psi ( y ) } \end{array}$ et truncation:. So we can choice of the kernel (Gretton et al., 2012b).

# 5 Minimax Nonparametric Two-Sample Test

The two-sample test is a statistical hypothesis test used to determine whether two independent samples $X ^ { ( n ) }$ and $Y ^ { ( m ) }$ come from a common population. Let $p , q$ be two probability density functions in $\mathscr { W } _ { L } ^ { u , \alpha } ( \Omega )$ . To better quantify the power of a two-sample test, We consider the null hypothesis $\mathbb { H } _ { 0 } : p = q$ and a local alternative hypothesis that is increasingly closer to the null as data accrue:

$$
\mathbb { H } _ { 1 } ( \Delta _ { n } ; \mathcal { D } ) : \mathcal { D } ( p , q ) \ge \Delta _ { n } ,
$$

where $\mathcal { D }$ is some discrepancy measure. For a test $\Phi$ based on data $X ^ { ( n ) }$ , we can define its power as

$$
\mathrm { p o w e r } \big ( \Phi ; \mathbb { H } _ { 1 } ( \Delta _ { n } ; \mathcal { D } ) \big ) : = \operatorname* { i n f } _ { \stackrel { \scriptstyle p , q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega ) } { \mathcal { D } ( p , q ) \geq \Delta _ { n } } } P ( \Phi \mathrm { r e j e c t } \mathbb { H } _ { 0 } ) .
$$

Of particular interest here is the smallest separation $\Delta _ { n }$ from the null hypothesis that can be detected consistently in a minimax sense. We care about metrics $d _ { \gamma _ { 1 } } ^ { W }$ and $d _ { \gamma _ { 1 } } ^ { H }$ with $\gamma _ { 1 } \in [ 0 , \infty )$ . Note that by Sobolev embedding theorem (Adams and Fournier, 2003), $C _ { L } ^ { \gamma _ { 1 } } ( \Omega ) \subset \mathcal { W } _ { L _ { 1 } } ^ { \gamma _ { 1 } } ( \Omega )$ , and therefore $d _ { \gamma _ { 1 } } ^ { H } ( p , p _ { 0 } ) \lesssim d _ { \gamma _ { 1 } } ^ { W } ( p , p _ { 0 } )$ , which leads to

$$
\begin{array} { r } { \mathrm { p o w e r } \big ( \Phi ; \mathbb { H } _ { 1 } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { W } ) \big ) \le \mathrm { p o w e r } \big ( \Phi ; \mathbb { H } _ { 1 } ( c \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { H } ) \big ) , } \end{array}
$$

for some constant $c$ depend on $\Omega$ . We first provide a lower bound to the optimal detection boundary (or separation threshold) when $\mathcal { D } ( \cdot , \cdot )$ is chosen to be the adversarial loss $d _ { \gamma _ { 1 } } ^ { H }$ with Hölder smooth discriminators. Here again for the sake of simplicity, we consider the balanced case where $c \leq n / m \leq C$ for some constants $0 < c \le C < \infty$ and express explicitly only the dependence on $n$ .

Theorem 1. For any $\gamma _ { 1 } ~ \geq ~ 0 ;$ , if $\Delta _ { n } \ = \ o ( n ^ { - { \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } } \ \vee$ $\textstyle { \frac { 1 } { \sqrt { n } } } { \biggr ) } ^ { 2 }$ , then there exists some $\eta \in \mathsf { \Gamma } ( 0 , 1 )$ so that for any test $\Phi _ { n }$ based on data $X ^ { ( n ) }$ and $Y ^ { ( m ) }$ that has asymptotic significance level $\eta ,$ , i.e., $\begin{array} { r } { \operatorname* { l i m } _ { n  \infty } P ( \Phi _ { n } \mathrm { r e j e c t } \mathbb { H } _ { 0 } ) = \eta f o r } \end{array}$ any $p = q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , we have

$$
\operatorname* { l i m i n f } _ { n \to \infty } \mathrm { p o w e r } \big ( \Phi _ { n } ; \mathbb { H } _ { 1 } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { H } ) \big ) < 1 .
$$

A similar result holds when the discrepancy measure is chosen to be $d _ { \gamma _ { 1 } } ^ { W }$ (recall inequali (9)). ow we demonstrate $\gamma$ $J$ test statistic based on $T _ { \gamma , J }$ that simultaneously attains the optimal detection boundary (up to logarithmic term) for all the $d _ { \gamma _ { 1 } } ^ { H }$ and $d _ { \gamma _ { 1 } } ^ { W }$ metrics with $\gamma _ { 1 }$ ranging over $[ 0 , \infty )$ .

Given a specified significance level $\eta$ , to obtain an asymptotic $\eta$ -level test, we may proceed to reject $\mathbb { H } _ { 0 }$ if and only if $T _ { \gamma , J }$ exceeds the $\eta$ -upper quantile of its asymptotic distribution under $\mathbb { H } _ { 0 }$ . However, the asymptotic distribution of $T _ { \gamma , J }$ remains unknown. To obtain a “normalized” test statistic that is asymptotically standard normal under $\mathbb { H } _ { 0 }$ , we should estimate the variance of $T _ { \gamma , J }$ . Denote $\begin{array} { r } { r _ { n , m } = \frac { 2 } { n ( n - 1 ) } + \frac { 2 } { m ( m - 1 ) } + \frac { 4 } { m n } } \end{array}$ 4mn , a simple calculation yields that, under $\mathbb { H } _ { 0 }$ ,

$$
\begin{array} { r l } & { \mathrm { V a r } ( T _ { \gamma , J } ) = r _ { n m } \cdot \mathbb { E } \bigg [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( X ) \psi ( Y ) \Big ) ^ { 2 } } \\ & { \quad \quad - \left( \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( X ) \cdot q _ { \psi } \right) ^ { 2 } - } \\ & { \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( Y ) \cdot p _ { \psi } \Big ) ^ { 2 } + \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } p _ { \psi } q _ { \psi } \Big ) ^ { 2 } \bigg ] . } \end{array}
$$

Note that the last term in (10) is a higher-order term, so we only need to estimate the first three terms. To this end, we replace the population means with the empirical means and approximate the wavelet coefficients by their sample

versions, which leads to

$$
\begin{array} { r l } & { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } = r _ { n m } \cdot \bigg \{ \displaystyle \frac { 1 } { n m } \sum _ { i _ { 1 } , i _ { 2 } } \Big ( \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i _ { 1 } } ) \psi ( Y _ { i _ { 2 } } ) \Big ) ^ { 2 } } \\ & { - \displaystyle \frac { 1 } { n } \sum _ { i _ { 1 } = 1 } ^ { n } \Big [ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i _ { 1 } } ) \cdot \big ( \frac { 1 } { m } \sum _ { i _ { 2 } = 1 } ^ { m } \psi ( Y _ { i _ { 2 } } ) \big ) \Big ] ^ { 2 } } \\ & { - \displaystyle \frac { 1 } { m } \sum _ { i _ { 2 } = 1 } ^ { m } \Big [ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( Y _ { i _ { 2 } } ) \cdot \big ( \frac { 1 } { n } \sum _ { i _ { 1 } = 1 } ^ { n } \psi ( X _ { i _ { 1 } } ) \big ) \Big ] ^ { 2 } \bigg \} . } \end{array}
$$

However, we need to avoid a negative or zero estimate of the variance. To this end, we replace $\widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 }$ with a small value $1 / n ^ { 3 }$ whenever it is too small or negative. Namely, let $\widetilde { \mathcal { S } _ { \gamma , J } ^ { 2 } } = \operatorname* { m a x } ( \widehat { \mathcal { S } _ { \gamma , J } ^ { 2 } } , \frac { 1 } { n ^ { 3 } } )$ . Now we can define the following “normalized” test statistic:

$$
\widetilde { T } _ { \gamma , J } = \widetilde { \mathcal { S } } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } .
$$

The following theorem summarizes our main results on the validity and power of the test induced from the test statistic $\widetilde { T } _ { \gamma , J }$ .

Theorem 2. For $p , q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , consider test statistic $\widetilde { T } _ { \gamma , J }$ with $2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ and $\begin{array} { r } { 0 \leq \gamma \leq \frac { d } { 4 } } \end{array}$ ,

1. under $\mathbb { H } _ { 0 }$ , we have $\widetilde { T } _ { \gamma , J } \stackrel { d } { \to } N ( 0 , 1 )$ , where $\xrightarrow { d }$ means converging in distribution;

2. for any significance level $\eta \in ( 0 , 1 )$ , consider test $\Phi _ { \gamma , \eta } ^ { J }$ where $\mathbb { H } _ { 0 }$ is rejected if and only if $\widetilde { T } _ { \gamma , J }$ exceeds $z _ { \eta }$ , the upper $\eta$ -quantile of the standard normal distribution (i.e., $P ( Z \geq z _ { \eta } ) = \eta$ with $Z \in N ( 0 , 1 ) ,$ ). Let

$$
\delta _ { n } ( \gamma _ { 1 } ) = \left\{ \begin{array} { c c } { { n ^ { - \frac { 4 \alpha + 4 ( \gamma \wedge \gamma _ { 1 } ) } { 4 \alpha + d } } , } } & { { 0 < \gamma < \frac { d } { 4 } } } \\ { { \log n \cdot n ^ { - \frac { 4 \alpha } { 4 \alpha + d } } , } } & { { \gamma = 0 } } \\ { { \log n \cdot n ^ { - 1 + \frac { 4 ( \gamma - \gamma \wedge \gamma _ { 1 } ) } { 4 \alpha + d } } , } } & { { \gamma = \frac { d } { 4 } \ . } } \end{array} \right.
$$

then for any $\gamma _ { 1 } \geq 0$ and $\Delta _ { n }$ satisfies $\Delta _ { n } ^ { 2 } \cdot \delta _ { n } ( \gamma _ { 1 } ) ^ { - 1 } $ $\infty$ , we have $( l ) \widetilde { T } _ { \gamma , J } \ \overset { P } { \longrightarrow } + \infty$ given that $d _ { \gamma _ { 1 } } ^ { W } ( p , q ) \geq$ $\Delta _ { n }$ ; (2) the power defined in (8) satisfies

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { p o w e r } \big ( \Phi _ { \gamma , \eta } ^ { J } ; \mathbb { H } _ { 1 } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { W } ) \big ) = 1 .
$$

Theorem 2 suggests that (1) the test $\Phi _ { \gamma , \eta } ^ { J }$ has asymptotic level $\eta$ ; (2) for any $\begin{array} { r } { 0 < \gamma _ { 1 } < \frac { d } { 4 } } \end{array}$ , by choosing $\begin{array} { r } { \gamma _ { 1 } \leq \gamma < \frac { d } { 4 } } \end{array}$ the test $\Phi _ { \gamma , \eta } ^ { J }$ 4 4can attain the optimal detection boundary $n ^ { - \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } \vee \frac { 1 } { \sqrt { n } }$ under both $d _ { \gamma _ { 1 } } ^ { W }$ and $d _ { \gamma _ { 1 } } ^ { H }$ metrics (recall inequality (9)); the case for $\begin{array} { r } { \gamma _ { 1 } \geq \frac { d } { 4 } } \end{array}$ or $\gamma _ { 1 } = 0$ only introduces an extra logarithmic term. In particular, by taking $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ , the test $\Phi _ { \gamma , \eta } ^ { J }$ can simultaneously attain the optimal detection boundary up to a logarithmic term under $d _ { \gamma _ { 1 } } ^ { W }$ and $d _ { \gamma _ { 1 } } ^ { H }$ metrics with $\gamma _ { 1 }$ ranging over $[ 0 , \infty )$ .

Corollary 1. Consider test statistics $\widetilde { T } _ { \gamma , J }$ with $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ and $2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ . For any $\gamma _ { 1 } ~ \geq ~ 0$ , denote $\Delta _ { n } \ = \ ( \log n )$ · $\left( n ^ { - { \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } } \vee { \frac { 1 } { \sqrt { n } } } \right)$ , then for any significance level $\eta \in ( 0 , 1 )$ the associated test $\Phi _ { \frac { d } { 4 } , \eta } ^ { J }$ satisfies that

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { p o w e r } \big ( \Phi _ { \frac { d } { 4 } , \eta } ^ { J } ; \mathbb { H } _ { 1 } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { W } ) \big ) = 1 .
$$

In practice, rather than estimating the variance of $T _ { \gamma , J }$ , we can also estimate the testing threshold by bootstrap methods (Arcones and Gine, 1992; Efron, 1979) as the bootstrap threshold may be more accurate for small samples: we compute the statistics $T _ { \gamma , J }$ based on datasets randomly sampled from the joint sample $\{ X ^ { ( n ) } , Y ^ { ( m ) } \}$ , and then we evaluate the upper $\eta$ -quantile of the empirical distribution of $T _ { \gamma , J }$ based on the bootstrapping datasets.

Remark 1. The reason for considering Sobolev discriminators in constructing the test statistic is that, the norm $B _ { 2 , 2 } ^ { - \gamma }$ associated with $d _ { \gamma } ^ { W }$ has a nice squared form, which enables us to utilize techniques from $U$ -statistics for computation and theoretical analysis. Since we develop a matching lower bound for Hölder smooth discriminators, our result can be generalized to any adversarial loss with the discriminator class being an interpolation space between Sobolev-2 and Hölder space. Moreover, for $\gamma > d / 2$ , the Sobolev-2 space $B _ { 2 , 2 } ^ { \gamma } ( \mathbb { R } ^ { d } )$ coincides with the reproducing kernel Hilbert space (RKHS) generated by the Matérn kernel of order $\gamma - d / 2$ (Kanagawa et al., 2018), so the proposed statistics $T _ { \gamma , J }$ would be asymptotically equivalent to the Matérn kernel based MMD statistic with bandwidth $h \asymp 2 ^ { - J }$ . However, the most interesting case lies in $\begin{array} { r } { \gamma \leq \frac { d } { 4 } } \end{array}$ , as the optimal detection boundary is the parametric root- $n$ rate when $\begin{array} { r } { \gamma > \frac { d } { 4 } } \end{array}$ So increasing $\gamma$ above $\textstyle { \frac { d } { 4 } }$ leads to a weaker loss but has no improvement in the optimal detection rate.

Remark 2. Another closely related problem is the goodnessof-fit test. The goodness-of-fit test is a statistical hypothesis test used to determine whether the sample data fits a specified distribution $p _ { 0 }$ from an expected population (e.g. a population with a normal distribution). The two-sample test can also be used to do a goodness-of-fit test: a random sample $Z ^ { ( m ) }$ is first drawn from the known reference distribution $p _ { 0 }$ and then a two–sample test is performed on data sets $X ^ { ( n ) }$ and $Z ^ { ( m ) }$ . We can construct a minimax optimal nonparametric goodness-of-fit test in a similar way as the two-sample test, where the extra prior information of $p _ { 0 }$ is incorporated. Further detail is available in Appendix C.

Remark 3. The assumption about the compactness of the support of $p , q$ can be relaxed. For example, if $p , q$ have exponential decay tails, then we can consider $\Omega =$ $[ - c \log n , c \log n ]$ so that the probability mass outside of $\Omega$ is a negligible higher-order term, and it will only introduce extra logarithmic terms in the detection power.

# 6 Numerical Illustration

In this section, we aim at: (1) verifying empirically that the proposed test $\Phi _ { \gamma , \eta } ^ { J }$ has asymptotic significance level $\eta$ ; (2) evaluating the power of the proposed test and comparing it with the MMD test. We carry out our experiment using two hypothesis testing procedures: one is the test $\Phi _ { \gamma , \eta } ^ { J }$ with $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ as suggested in Theorem 2 and Corollary 1, where the wavelet basis is chosen to be the Haar wavelet3, the other one is the hypothesis test based on MMD with Gaussian kernel $k _ { h } ( x , y ) = \exp { \big ( - ( \| x - y \| / h ) ^ { 2 } \big ) }$ (Li and Yuan, 2019): $\mathbb { H } _ { 0 }$ is rejected if and only if $\widetilde { T } _ { h } ^ { \mathrm { M M D } } = T _ { h } ^ { \mathrm { M M D } } / \widehat { S } _ { \mathrm { M M D } }$ exceeds han estimator to the standard variance of $z _ { \eta }$ , where $T _ { h } ^ { \mathrm { M M D } }$ is defined in (7), and $T _ { h } ^ { \mathrm { M M D } }$ $\widehat { S } _ { \mathrm { M M D } }$ b for nor- is malizing the statistic, we denote the corresponding test by ΦMMDh,η . We then apply the two procedures to synthetic datasets. Specifically, let $\mu _ { 0 }$ be the uniform distribution on $[ 0 , 1 ] ^ { d }$ and $\begin{array} { r } { \mu _ { 1 } ( x ) = \prod _ { j = 1 } ^ { d } \nu ( x _ { j } ) } \end{array}$ be a $d$ -dimensional distribution with $\nu$ being beta distribution with shape parameters $\alpha = 2 . 5$ , $\beta = 2 . 5$ . Then we scale and translate the random variable $X \sim \mu _ { 1 }$ by the transform $Y = X / k + 0 . 5$ with $k \in \mathbb { R } ^ { + }$ , the corresponding distribution of $Y$ is denote by $\mu _ { 1 } ^ { [ k ] }$ . We set $\begin{array} { r } { p = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ 5 ] } } \end{array}$ and $\begin{array} { r } { q = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ k ] } } \end{array}$ with $k \in \{ 3 , 3 . 5 , 3 . 8 , 4 , \hat { 5 } \}$ .

We first check the normality of the test statistic $\widetilde { T } _ { \gamma , J }$ and $\widetilde { T } _ { h } ^ { \mathrm { M M D } }$ under $\mathbb { H } _ { 0 }$ . With $n = 5 0$ e , we independently sample $2 n$ $p$   
sets $X ^ { ( n ) }$ and $Y ^ { ( n ) }$ . The bandwidth $h$ and truncation level $J$ are selected based on the median heuristic (Arlot et al., 2019; Garreau et al., 2017): define $H _ { n } = \mathrm { M e d i a n } ( \mathbb { I } z _ { i } -$ $Z _ { j } \parallel ^ { 2 } \mid 1 \leq i \leq j \leq 2 n )$ , where $Z = \{ Z _ { 1 } , Z _ { 2 } , \cdot \cdot \cdot , Z _ { 2 n } \} =$ $\{ X _ { } ^ { ( n ) } , Y ^ { ( n ) } \}$ . Following (Garreau et al., 2017), we set $h =$ $\sqrt { H _ { n } / 2 }$ , and similarly choose $J = \lceil \log _ { 2 } ( 1 / \sqrt { H _ { n } } ) + 1 \rceil$ . The corresponding bandwidth is around $h \ : = \ : 0 . 2 5$ , and truncation level is around $J = 3$ . The density and normal quantile-quantile (Q-Q) plots of the test statistics of concern based on 1000 replicates are shown in figure 2(a) and 2(b). We can see the density for $\widetilde { T } _ { \gamma , J }$ under $\mathbb { H } _ { 0 }$ is closer to the standard normal. In addition, the 1-Wasserstein distance between the distribution of the test statistics (under $\mathbb { H } _ { 0 }$ ) and standard normal is 0.2538 for $\widetilde { T } _ { h } ^ { \mathrm { M M D } }$ , and 0.2138 for $\widetilde { T } _ { \gamma , J }$ . Therefore, our method delivered better uncertainty quantification.

To assess the power of the proposed testing procedure. We sample $n = 5 0$ samples from $p$ and $\begin{array} { r } { q = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ k ] } } \end{array}$ with $k \in \{ 3 , 3 . 5 , 3 . 8 , 4 \}$ respectively. The selected bandwidth based on the median heuristic is also around $h = 0 . 2 5$ , and the truncation level is around $J = 3$ . The densities of the two test statistics of concern are given in Figure 2(c). We can see the density of $\widetilde { T } _ { \gamma , J }$ has a much heavier tail, that is, $\widetilde { T } _ { \gamma , J }$ tends to return a larger value that leads to the rejection of the null hypothesis. Moreover, we consider the powers (i.e., the probability that success to reject the null hypothesis) of the tests $\Phi _ { \gamma , \eta } ^ { J }$ and $\Phi _ { h , \eta } ^ { \mathrm { M M D } }$ with level of significance $\eta \in \{ 0 . 0 5 , 0 . 0 1 \}$ . The results are shown in Table 1, from whicthan n see that the test . Now we study th $\Phi _ { \gamma , \eta } ^ { J }$ has much larger powerssitivity of the hypothesis $\Phi _ { h , \eta } ^ { \mathrm { M M D } }$

<table><tr><td>k</td><td>Powers: 重 个 y，n η= 0.01 m=0.05</td></tr><tr><td>4 3.8</td><td>0.307 ± 0.016 0.416 ± 0.016 0.434 ± 0.020 0.548 ± 0.014</td></tr><tr><td>3.5</td><td>0.602 ± 0.013 0.711 ± 0.011</td></tr><tr><td>3</td><td>0.822 ± 0.012 0.891 ± 0.010 Powers: h,n 个</td></tr><tr><td>k 4</td><td>η= 0.01 n= 0.05 0.085 ± 0.011 0.163 ± 0.012</td></tr><tr><td>3.8</td><td>0.134 ± 0.008 0.246 ± 0.013</td></tr><tr><td>3.5</td><td>0.283 ± 0.013 0.440 ± 0.018</td></tr><tr><td>3</td><td>0.716 ± 0.009 0.837 ± 0.008</td></tr></table>

Table 1: Under $\begin{array} { r } { p = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ 5 ] } } \end{array}$ and $\begin{array} { r } { q = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ k ] } } \end{array}$ with $k \in \{ 3 , 3 . 5 , 3 . 8 , 4 \}$ , the table shows the powers for tests $\Phi _ { \gamma , \eta } ^ { J }$ and ΦMMD w ith $\gamma = 1 / 2$ , $J = 3$ , $h = 0 . 2 5$ and level of significance $\eta \in \{ 0 . 0 5 , 0 . 0 1 \}$ .

testing procedures to the hyperparameter. We in comparison the hypothesis testing procedure $\Phi _ { \eta } ^ { J } = \Phi _ { 0 , \eta } ^ { J }$ which means that we do not include the decaying factor $2 ^ { - 2 \gamma j }$ for the level $j$ of the wavelet in the proposed test statistic. Figure 3 shows the trends of the powers as the level of significance varies for different methods and hyperparameters. We can see that the tests $\Phi _ { \eta } ^ { J }$ and $\Phi _ { h , \eta } ^ { \mathrm { M M D } }$ exhibit similar patterns: both increasing and decreasing $J$ from the optimal level would lead to an obvious deteriorate in the performance. On the other hand, the test $\Phi _ { \gamma , \eta } ^ { J }$ with $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ is much more robust to large truncation levels: choosing an arbitrary $J$ from $\{ 3 , 4 \cdots , 7 \}$ outperforms the MMD test $\Phi _ { h , \eta } ^ { \mathrm { M M D } }$ with the bandwidth $h$ being selected through the median heuristic (i.e., $h = 0 . 2 5$ ).

# 7 Application

As shown in Lemmas 1 and 2, the statistic $T _ { \gamma , J }$ provides a reasonable metric for quantifying the distance between the underlying populations based on finite samples. Therefore, $T _ { \gamma , J }$ can be deployed in practical problems as an evaluation criterion for checking the goodness of model fit.

We consider the MNIST handwritten digit (LeCun et al., 1995) dataset, which is composed of $6 0 \mathrm { k }$ grey-scale images of handwritten digits $( 0 - 9 )$ , along with a test set of 10k images. A popular method for modelling and efficient sampling from the complex distribution ${ \mathcal { P } } ^ { * }$ over the handwritten digit is the variational autoencoder (VAE,

![](images/9008949d6d27f0aad3d67b06f9b20f91ba7e0406213a7e871df375a99d2a6a22.jpg)  
Figure 2: Densities and Normal quantile-quantile (Q-Q) plots of test statistics: blue curves correspond to $\widetilde { T } _ { h } ^ { \mathrm { M M D } }$ with $h = 0 . 2 5$ , red curves correspond to $\widetilde { T } _ { \gamma , J }$ with $J = 3$ and $\gamma = 1 / 2$ , black curve corresponds to the baseline of standard normal.

![](images/47b06a886c98eaf637c99d162291d4757f523b5e84e9eaa5b9646eff5909b4cd.jpg)  
Figure 3: For p = 12 µ0 + 12 µ[5]1 and q = 12 of significance var s for (1) test $\Phi _ { h , \eta } ^ { \mathrm { M M D } }$ $\begin{array} { r } { q = \frac { 1 } { 2 } \mu _ { 0 } + \frac { 1 } { 2 } \mu _ { 1 } ^ { [ k ] } } \end{array}$ 2 1  under different choices of bandwidth d with $k = 3 . 8$ . The figure illustrates the trends of powers as the level $h$ ; (2) t $\Phi _ { \eta } ^ { J } = \Phi _ { 0 , \eta } ^ { J }$ with different choic $\eta$ of truncation level $J$ ; (3) test $\Phi _ { \gamma , \eta } ^ { J }$ with $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ and different choices of truncation level $J$ . The cases for exhibit similar trends.

Kingma and Welling, 2013; Rezende et al., 2014). In plain language, VAE is a latent variable generative modelling approach that defines a joint density $p ( x , z )$ over the data space $\boldsymbol { \mathcal { X } } \subset \mathbb { R } ^ { D }$ and the latent space $\mathcal { Z } \subset \mathbb { R } ^ { d }$ by specifying a prior $\pi ( z )$ over latent variables and a conditional density (decoder) $p ( x | z )$ of data given latent variables. To avoid marginalizing out latent variables, VAE introduces a family of encoders $q ( z | x )$ for approximating the posterior of latent variables and jointly optimizing the so-called evidence lower bound (ELBO, Ormerod and Wand, 2010). The commonly-used choice of $\pi ( z )$ is the isotropic Gaussian distribution. In this experiment, we consider jointly optimizing the prior inside a mixture of Gaussian family $\begin{array} { r } { \{ \tilde { \mathcal { \alpha } } ( z ) = \frac { \overline { { 1 } } } { K } \sum _ { j = 1 } ^ { K } N ( \mu _ { j } , \sigma _ { j } ^ { 2 } I _ { d } ) | \mu _ { j } \in \mathbb { R } , \sigma _ { j } \in \mathbb { R } ^ { + } \} } \end{array}$ (Jiang et al., 2016; Tomczak and Welling, 2018). Of particular interest here is the choice of the hyperparameter $K \in \mathbb { N } ^ { + }$ : whether uses a mixture of Gaussian can outperform the standard Gaussian and what is the optimal choice of $K$ . To this end, let the latent dimension $d = 2$ and denote the fitted encoder and prior based on the training set as $\hat { q } _ { [ K ] } ( z | x )$ and $\widehat { \pi } _ { [ K ] } ( z )$ , respectively. Here the encoder and prior are modelled by neural networks, details are available in Appendix A. A good choice of prior family will result in a small distance between the marginal of the learned encoder $\mathbb { E } _ { \mathcal { P } ^ { * } } [ \widehat { q } _ { [ K ] } ( z | x ) ]$ and the prior $\widehat { \pi } _ { [ K ] } ( z )$ . Therefore, we sample b10k i.i.d data from $\mathbb { E } _ { \mathcal { P } ^ { * } } [ \widehat { q } _ { [ K ] } ( z | x ) ]$ by first randomly pick a data point $x$ b from the test set and sample $z$ from $\widehat { q } _ { [ K ] } ( z | x )$ , the obtaining data set is denote by $Z _ { 1 } ^ { ( n ) }$ with $n = 1 0 \mathrm { k \Omega }$ . Similarly, we sample data set $Z _ { 2 } ^ { ( n ) }$ from $\widehat { \pi } _ { [ K ] } ( z )$ . We record the value of $T _ { \gamma , J }$ with $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ and $J = 8$ for different choices of $K$ . As a comparison, we record the values of the negative test marginal log-likelihood (LL) (Burda et al., 2015; Tomczak and Welling, 2018), which is a commonly-used metric for quantitatively evaluating the VAE model. The results are shown in Figure 4.

According to the plot, the statistic $T _ { \gamma , J }$ decreases rapidly when $K$ increases from 1 to 10. As we can see in Figure 5, when $K = 1$ , where the fitted prior is a single mode normal distribution, the marginal of the fitted encoder has an obvious clustering structure. In contrast, when $K = 1 0$ , the fitted prior and marginal of the fitted encoder has a similar clustering structure. In addition, the trend of $T _ { \gamma , J }$ approaches a horizontal line when $K \geq 1 0$ . This is consistent with the fact that the dataset consists of 10 digits $\cdot _ { 0 } \cdot \mathrm { \ }$ to ‘9’. Interestingly, for this dataset our method correctly identified/learned the number of clusters, a key clustering tuning parameter usually set from domain knowledge. The trend of the negative test LL exhibits similar pattern as the statistic $T _ { \gamma , J }$ , while it is more computational demanding: we need 170s for computing the test LL using an NVIDIA-A100 GPU, while the statistic $T _ { \gamma , J }$ can be computed in 9s.

![](images/413a79947b0bf8eae08b8d52c5968c87b0f6061fd77e055414a3e3b3a844dbae.jpg)  
Figure 4: The statistic $T _ { \gamma , J }$ (black curve) and negative test marginal log-likelihood (red curve) as $K$ varies. For both metrics, a smaller value implies better performance.

![](images/538b27e9e0908f0577909929db6e57eddb43f5e0234044e1c707cebd2423e123.jpg)  
Figure 5: Random samples from the marginal of the fitted encoder and priors for different $K$ .

# 8 Conclusion

In this paper, we propose a minimax nonparametric twosample test that can simultaneously attain the optimal detection boundary under many common adversarial losses. We conducted experiments to show that in comparison to the conventional MMD test with Gaussian kernel, the proposed testing procedure tends to exhibit higher power and robustness against tuning parameters. In our theoretical analysis, the optimal choice of the truncation level $J$ depends on the smoothness $\alpha$ of the underlying population, which may be unknown in practical problems. The development of a datadriven adaptive test to the distribution smoothness level may be left to future research.

# References

Adams, R. A. and Fournier, J. J. (2003) Sobolev spaces. Elsevier.   
Arcones, M. A. and Gine, E. (1992) On the bootstrap of u and v statistics. The Annals of Statistics, 655–674.   
Arjovsky, M., Chintala, S. and Bottou, L. (2017) Wasserstein gan. URL: https://arxiv.org/abs/1701. 07875.   
Arlot, S., Celisse, A. and Harchaoui, Z. (2019) A kernel multiple change-point algorithm via model selection. Journal of Machine Learning Research, 20, 1–56. URL: http: //jmlr.org/papers/v20/16-155.html.   
Biswas, M. and Ghosh, A. K. (2014) A nonparametric two-sample test applicable to high dimensional data. Journal of Multivariate Analysis, 123, 160– 171. URL: https://www.sciencedirect.com/ science/article/pii/S0047259X13001966.   
Bouzebda, S. and Didi, S. (2017) Multivariate wavelet density and regression estimators for stationary and ergodic discrete time processes: Asymptotic results. Communications in Statistics - Theory and Methods, 46, 1367–1406. URL: https://doi.org/10.1080/ 03610926.2015.1019144.   
Burda, Y., Grosse, R. and Salakhutdinov, R. (2015) Importance weighted autoencoders. arXiv preprint arXiv:1509.00519.   
Butucea, C. and Tribouley, K. (2006) Nonparametric homogeneity tests. Journal of Statistical Planning and Inference, 136, 597–639. URL: https://www.sciencedirect.com/ science/article/pii/S0378375804003374.   
Cohen, A. (2003) Numerical analysis of wavelet methods. Elsevier.   
Daubechies, I. (1988) Orthonormal bases of compactly supported wavelets. Communications on pure and applied mathematics, 41, 909–996.   
Del Barrio, E., Cuesta-Albertos, J. A., Matrán, C. and Rodríguez-Rodríguez, J. M. (1999) Tests of goodness of fit based on the l2-wasserstein distance. Annals of Statistics, 1230–1239.   
Doersch, C. (2016) Tutorial on variational autoencoders. arXiv preprint arXiv:1606.05908.   
Efron, B. (1979) Bootstrap Methods: Another Look at the Jackknife. The Annals of Statistics, 7, 1 – 26. URL: https://doi.org/10.1214/aos/ 1176344552.

Evans, L. C. (2010) Partial differential equations. Providence, R.I.: American Mathematical Society.

Friedman, J. H. and Rafsky, L. C. (1979) Multivariate Generalizations of the Wald-Wolfowitz and Smirnov Two-Sample Tests. The Annals of Statistics, 7, 697 – 717. URL: https://doi.org/10.1214/aos/ 1176344722.

Garreau, D., Jitkrittum, W. and Kanagawa, M. (2017) Large sample analysis of the median heuristic. URL: https: //arxiv.org/abs/1707.07269.

Giné, E. and Nickl, R. (2015) Mathematical Foundations of Infinite-Dimensional Statistical Models. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press.

Gretton, A., Borgwardt, K. M., Rasch, M. J., Schölkopf, B. and Smola, A. (2012a) A kernel two-sample test. The Journal of Machine Learning Research, 13, 723–773.

Gretton, A., Fukumizu, K., Harchaoui, Z. and Sriperumbudur, B. K. (2009a) A fast, consistent kernel two-sample test. In Advances in Neural Information Processing Systems (eds. Y. Bengio, D. Schuurmans, J. Lafferty, C. Williams and A. Culotta), vol. 22. Curran Associates, Inc. URL: https://proceedings. neurips.cc/paper/2009/file/ 9246444d94f081e3549803b928260f56-Paper. pdf.

— (2009b) A fast, consistent kernel two-sample test. Advances in neural information processing systems, 22.

Gretton, A., Sejdinovic, D., Strathmann, H., Balakrishnan, S., Pontil, M., Fukumizu, K. and Sriperumbudur, B. K. (2012b) Optimal kernel choice for large-scale two-sample tests. In Advances in Neural Information Processing Systems (eds. F. Pereira, C. Burges, L. Bottou and K. Weinberger), vol. 25. Curran Associates, Inc. URL: https://proceedings. neurips.cc/paper/2012/file/ dbe272bab69f8e13f14b405e038deb64-Paper. pdf.

Györfi, L. and Van Der Meulen, E. C. (1991) A Consistent Goodness of Fit Test Based on the Total Variation Distance, 631–645. Dordrecht: Springer Netherlands. URL: https://doi.org/10.1007/ 978-94-011-3222-0_47.

Hall, P. (1984) Central limit theorem for integrated square error of multivariate nonparametric density estimators. Journal of Multivariate Analysis, 14, 1– 16. URL: https://www.sciencedirect.com/ science/article/pii/0047259X84900447.

Hall, P. and Heyde, C. (1980) Martingale Limit Theory and its Application. Academic Press.

Härdle, W., Kerkyacharian, G., Picard, D. and Tsybakov, A. (2012) Wavelets, approximation, and statistical applications, vol. 129. Springer Science & Business Media.

Henze, N. (1988) A multivariate two-sample test based on the number of nearest neighbor type coincidences. The Annals of Statistics, 16, 772–783.

Hotelling, H. (1931) The Generalization of Student’s Ratio. The Annals of Mathematical Statistics, 2, 360 – 378. URL: https://doi.org/10.1214/aoms/ 1177732979.

Hütter, J.-C. and Rigollet, P. (2021) Minimax estimation of smooth optimal transport maps. The Annals of Statistics, 49, 1166–1194.

Ingster, Y. I. (1986) An asymptotic minimax testing of nonparametric hypotheses on the density of the distribution of an independent sample. Journal of Soviet Mathematics.

— (1987) Minimax testing of nonparametric hypotheses on a distribution density in the $\$ 123$ metrics. Theory of Probability & Its Applications, 31, 333–337. URL: https://doi.org/10.1137/1131042.

Jiang, Z., Zheng, Y., Tan, H., Tang, B. and Zhou, H. (2016) Variational deep embedding: An unsupervised and generative approach to clustering. arXiv preprint arXiv:1611.05148.

Kanagawa, M., Hennig, P., Sejdinovic, D. and Sriperumbudur, B. K. (2018) Gaussian processes and kernel methods: A review on connections and equivalences. arXiv preprint arXiv:1807.02582.

Kingma, D. P. and Welling, M. (2013) Auto-encoding variational bayes. URL: https://arxiv.org/abs/ 1312.6114.

LeCun, Y., Jackel, L. D., Bottou, L., Cortes, C., Denker, J. S., Drucker, H., Guyon, I., Muller, U. A., Sackinger, E., Simard, P. et al. (1995) Learning algorithms for classification: A comparison on handwritten digit recognition. Neural networks: the statistical mechanics perspective, 261, 2.

Li, T. and Yuan, M. (2019) On the optimality of gaussian kernel based nonparametric tests against smooth alternatives. arXiv preprint arXiv:1909.03302.

Liu, Z. and Modarres, R. (2011) A triangle test for equality of distribution functions in high dimensions. Journal of Nonparametric Statistics, 23, 605–615.

URL: https://doi.org/10.1080/10485252.   
2010.485644.

Meyer, Y. (1992) Wavelets and Operators: Volume 1. No. 37. Cambridge university press.

Ormerod, J. T. and Wand, M. P. (2010) Explaining variational approximations. The American Statistician, 64, 140–153.

Pearson, K. (1900) X. on the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 50, 157–175.

Ramdas, A., García Trillos, N. and Cuturi, M. (2017) On wasserstein two-sample testing and related families of nonparametric tests. Entropy, 19, 47.

Rezende, D. J., Mohamed, S. and Wierstra, D. (2014) Stochastic backpropagation and approximate inference in deep generative models.

Santambrogio, F. (2015) Optimal Transport for Applied Mathematicians: Calculus of Variations, PDEs, and Modeling. Cham: Springer International Publishing.

Schilling, M. F. (1986) Multivariate two-sample tests based on nearest neighbors. Journal of the American Statistical Association, 81, 799–806.

Sriperumbudur, B. K., Gretton, A., Fukumizu, K., Schölkopf, B. and Lanckriet, G. R. (2010) Hilbert space embeddings and metrics on probability measures. The Journal of Machine Learning Research, 11, 1517–1561.

Student (1908) The probable error of a mean. Biometrika, 6, 1–25. URL: http://www.jstor.org/stable/ 2331554.

Tolstikhin, I., Bousquet, O., Gelly, S. and Schoelkopf, B. (2017) Wasserstein auto-encoders. URL: https:// arxiv.org/abs/1711.01558.

Tomczak, J. and Welling, M. (2018) Vae with a vampprior. In International Conference on Artificial Intelligence and Statistics, 1214–1223. PMLR.

Triebel, H. (2006) Theory of Function Spaces III. Basel: Birkhäuser Basel.

— (2010) Bases in function spaces, sampling, discrepancy, numerical integration, vol. 11. European Mathematical Society.

Uppal, A., Singh, S. and Póczos, B. (2019) Nonparametric density estimation & convergence rates for gans under besov ipm losses. Advances in neural information processing systems, 32.

Villani, C. (2009) Optimal Transport: Old and New. Berlin, Heidelberg: Springer Berlin Heidelberg.

Wang, J., Gao, R. and Xie, Y. (2021) Two-sample test using projected wasserstein distance. In 2021 IEEE International Symposium on Information Theory (ISIT). IEEE. URL: https://doi.org/10.1109% 2Fisit45174.2021.9518186.

Xing, X., Shang, Z., Du, P., Ma, P., Zhong, W. and Liu, J. S. (2019) Minimax nonparametric two-sample test under smoothing. URL: https://arxiv.org/abs/ 1911.02171.

# Appendix

Notations: We adopt the notations in the manuscript, and further introduce the following additional notations for the   
technical proofs. For $\alpha \in \mathbb { R }$ , the floor and ceiling functions are denoted by $\lfloor \alpha \rfloor$ and $\lceil \alpha \rceil$ , indicating rounding $\alpha$ to the   
next smaller and larger integer. For two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ to mean   
$a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n$ . In addition, $a _ { n } \asymp b _ { n }$ means that both   
$a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ hold. We use $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ to denote the set of square integrable functions on $\mathbb { R } ^ { d }$ . When no ambiguity $\nu$ may also us, we define $\nu$ nsity fund use or a multi-indexenote the mixed   
$\begin{array} { r } { a = ( a _ { 1 } , \cdots , a _ { d } ) \in \mathbb { N } _ { 0 } ^ { d } = \{ ( a _ { 1 } , \cdots , a _ { d } ) | \forall j \in [ d ] , a } \end{array}$ $a _ { j } \in \mathbb { N } _ { 0 } \}$ $\begin{array} { r } { | a | = \sum _ { k = 1 } ^ { d } a _ { j } } \end{array}$ $f ^ { ( a ) }$ $f$ $a$ $\alpha \in [ 0 , \infty )$ $\mathcal { C } ^ { \alpha } ( \Omega )$ $\alpha$   
(function) class (see e.g., Evans (2010)) equipped with the Hölder norm $\| \cdot \| _ { C ^ { \alpha } ( \Omega ) }$ :

$$
\| f \| _ { C ^ { \alpha } ( \Omega ) } = \sum _ { | a | = \lfloor \alpha \rfloor } \operatorname* { m a x } _ { x , y \in \Omega } \frac { | f ^ { ( a ) } ( x ) - f ^ { ( a ) } ( y ) | } { \| x - y \| ^ { \alpha - \lfloor \alpha \rfloor } } + \sum _ { | a | \leq \lfloor \alpha \rfloor } \operatorname* { m a x } _ { x \in \Omega } | f ^ { ( a ) } ( x ) | ,
$$

and let $\mathcal { C } _ { r } ^ { \alpha } ( \Omega ) : = \left\{ f : \Omega \to \mathbb { R } : \| f \| _ { \mathcal { C } ^ { \alpha } ( \Omega ) } \leq r \right\}$ . Similarly, we use the notation $\mathscr { W } ^ { \alpha } ( \Omega )$ to denote the $\alpha$ -smooth Sobolev(-2) class equipped with the Sobolev norm $\| \cdot \| _ { \mathcal { W } ^ { \alpha } ( \Omega ) }$ :

$$
\| f \| _ { \mathcal { W } ^ { \alpha } ( \Omega ) } = \sum _ { | a | = | \alpha | } \sqrt { \int _ { \Omega } \int _ { \Omega } \frac { | f ^ { ( a ) } ( x ) - f ^ { ( a ) } ( y ) | ^ { 2 } } { \| x - y \| ^ { 2 ( \alpha - | \alpha | ) + d } } \mathrm { d } x \mathrm { d } y } + \sum _ { | a | \le | \alpha | } \sqrt { \int _ { \Omega } | f ^ { ( a ) } ( x ) | ^ { 2 } \mathrm { d } x } ,
$$

and let $\mathcal { W } _ { r } ^ { \alpha } ( \Omega ) : = \{ f : \Omega  \mathbb { R } : \| f \| _ { \mathcal { W } ^ { \alpha } ( \Omega ) } \leq r \}$ . We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and reserve $\| \cdot \|$ for the $\ell _ { 2 }$ norm (that is, suppress the subscript when $p = 2$ ). For two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } = o ( b _ { n } )$ if $a _ { n } / b _ { n } \to 0$ ad $n$ increases. For two random sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } = o _ { p } ( b _ { n } )$ if $a _ { n } / b _ { n } \overset { P } { \longrightarrow } 0$ . For any positive integer $m$ , we use the shorthand $[ m ] : = \{ 1 , \cdots , m \}$ . Throughout, C, L c, C0, $L _ { 0 }$ , $c _ { 0 }$ , $C _ { 1 }$ , $L _ { 1 }$ , $c _ { 1 }$ ,. . . are generically used to denote positive constants whose values might change from one line to another, but are independent from everything else.

# A Implementation Details for the Real Data Application

Follow Kingma and Welling (2013), for our encoder, we use the multivariate Gaussian distribution, with the mean and covariance matrices parameterized by the outputs of a convolutional neural network with Probabilistic (tfp) Layers; the decoder is a multivariate Bernoulli whose probabilities are computed with a deconvolutional neural network. The specification of our models are described in Table 2. Note that the regularizer “KLDivergenceRegularizer” in the probabilistic layer of the encoder should contribute a “regularization” term to the final loss. Specifically, we are adding the KL divergence between the encoder and the prior to the loss, which is the KL term in the ELBO. Moreover, in the computation of the statistic $T _ { \gamma , J }$ , for consistency, we transform the data sets by setting $Z _ { 1 } ^ { ( n ) } = Z _ { 1 } ^ { ( n ) } - Z _ { \mathrm { m i n } } / ( Z _ { \mathrm { m a x } } - Z _ { \mathrm { m i n } } )$ and $Z _ { 2 } ^ { ( n ) } = Z _ { 2 } ^ { ( n ) } - Z _ { \mathrm { m i n } } / ( Z _ { \mathrm { m a x } } - Z _ { \mathrm { m i n } } )$ , where $Z _ { \mathrm { m a x } }$ and $Z _ { \mathrm { m i n } }$ 1 1  are the maximum and minimum of the joint dataset $\{ Z _ { 1 } ^ { ( n ) } , Z _ { 2 } ^ { ( n ) } \}$ through all the data points (by dimension). After the transformation, the data sets $Z _ { 1 } ^ { ( n ) }$ and $Z _ { 2 } ^ { ( n ) }$ are all included in $[ 0 , 1 ] ^ { d }$ . The code for reproducing the experiment is available in https://github.com/rtang1997/ Two_sample_test_adversarial.

Table 2: Network architecture and hyperparameters the encoder and decoder.   

<table><tr><td>Operation</td><td>Kernel</td><td>Strides</td><td>Feature maps</td><td>Activation</td></tr><tr><td>Decoder p(xlz) : z ∈ Rd</td><td colspan="4"></td></tr><tr><td>Fully connected</td><td></td><td></td><td>6×6×32</td><td>Leaky ReLU</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>13 ×13 × 64</td><td>Leaky ReLU</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>27×27×32</td><td>Leaky ReLU</td></tr><tr><td>Transposed convolution</td><td>2×2</td><td>1×1</td><td>28×28×1</td><td>Leaky ReLU</td></tr><tr><td>Probabilistic Layers: IndependentBernoulli</td><td colspan="4"></td></tr><tr><td>Encoder q(z|x)</td><td></td><td></td><td>28×28×1 28×28×1</td><td></td></tr><tr><td>Minus x by 0.5</td><td colspan="4"></td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>28×28×1 14 ×14 ×32</td><td>LeakyReLU</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>7×7×64</td><td>LeakyReLU</td></tr><tr><td>Fully connected</td><td></td><td></td><td>5</td><td>KLDivergenceRegularizer</td></tr><tr><td>Probabilistic Layers:MultivariateNomalTriL</td><td colspan="4"></td></tr><tr><td>Batch size</td><td colspan="4">128</td></tr><tr><td>Number of epochs</td><td colspan="4"></td></tr><tr><td>Number of training samples and test samples</td><td colspan="4">50 60k and 10k respectively.</td></tr></table>

# B Wavelet and Besov Function Space

In this section, we give a brief introduction to the wavelet and Besov function Space. Further details are available in Cohen (2003); Triebel (2006); Härdle et al. (2012). Let $\phi { \mathfrak { M } }$ and $\phi _ { \mathfrak { F } }$ be a compactly supported wavelet and scaling function, respectively, for example Daubechies wavelets (Bouzebda and Didi, 2017; Hütter and Rigollet, 2021). This implies that

$$
\left\{ \begin{array} { l l } { \psi _ { \mathfrak { F } } ( x - k ) } & { j = 0 , k \in \mathbb { Z } , } \\ { 2 ^ { ( j - 1 ) / 2 } \psi _ { \mathfrak { M } } ( 2 ^ { j - 1 } x - k ) , } & { j \in \mathbb { N } ^ { + } , k \in \mathbb { Z } , } \end{array} \right.
$$

is an orthonormal basis of $\mathcal { L } ^ { 2 } ( \mathbb { R } )$ . To obtain a basis of $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ for an integer $d > 1$ , set ${ \mathfrak { G } } = \{ { \mathfrak { F } } , { \mathfrak { M } } \} ^ { d } \setminus \{ ( { \mathfrak { F } } , \dots , { \mathfrak { F } } ) \}$ . Then for any multi-index $k \in  { \mathbb { Z } ^ { d } }$ , the level zero basis $\phi _ { k } ^ { [ d ] }$ is obtained by translating the $d$ -fold tensor product $\phi _ { \mathfrak { F } } ^ { \otimes d }$ by $k$ as $\begin{array} { r } { \phi _ { k } ^ { [ d ] } ( x ) = \prod _ { i = 1 } ^ { d } \phi _ { \mathfrak { F } } ( x _ { i } - k _ { i } ) } \end{array}$ for $x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { R } ^ { d }$ , and for any $j \geq 1$ , the level $j$ basis $\{ \psi _ { l j k } ^ { [ d ] } : l \in [ 2 ^ { d } - 1 ] \}$ with translation $k$ is any ordering of the following $2 ^ { d } - 1$ functions,

$$
\psi _ { g j k } ^ { [ d ] } ( x ) = 2 ^ { \frac { d ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { d } \phi _ { g _ { i } } ^ { [ d ] } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) , \quad \forall g \in \mathfrak { G } .
$$

This gives the orthornormal basis

$$
\left\{ \begin{array} { l l } { \phi _ { k } ^ { [ d ] } ( x ) , \quad j = 0 , l = 0 , k \in \mathbb { Z } ^ { d } , } \\ { \psi _ { l j k } ^ { [ d ] } ( x ) , \quad j \in \mathbb { N } ^ { + } , l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } , } \end{array} \right.
$$

for $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ . Denote $\overline { { \Psi } } _ { 0 } = \{ \phi _ { k } ^ { [ d ] } ( \cdot ) : k \in \mathbb { Z } ^ { d } \}$ as the set of level zero basis and $\overline { { \Psi } } _ { j } = \{ \psi _ { l j k } ^ { [ d ] } ( \cdot ) : l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } \}$ as the set of level $j$ basis for $j \in \mathbb { N } ^ { + }$ . We are then ready to define the Besov space $B _ { l , m } ^ { s } ( \mathbb { R } ^ { d } )$ consists of functions $f$ that admits the wavelet expansion

$$
f ( x ) = \sum _ { j \geq 0 } \sum _ { \psi \in \overline { { \Psi } } _ { j } } f _ { \psi } \psi ( x ) ,
$$

where $\begin{array} { r } { f _ { \psi } : = \int f ( x ) \psi ( x ) \mathrm { d } x } \end{array}$ , and is equipped with the norm

$$
\left\| f \right\| _ { B _ { p , q } ^ { s } } : = \left\| 2 ^ { j s } 2 ^ { d j \left( \frac { 1 } { 2 } - \frac { 1 } { p } \right) } \| f _ { j } \| _ { l } \right\| _ { m } ,
$$

with fj = {fψ}ψ∈Ψj .

The following Theorem collects the relationship between the Besov space, Hölder space and Sobolev-2 space.

Theorem 3. (Triebel, 2006; Giné and Nickl, 2015) Let $\alpha > 0$ , $\mathcal { W } ^ { \alpha } ( \mathbb { R } ^ { d } ) = B _ { 2 , 2 } ^ { \alpha } ( \mathbb { R } ^ { d } ) .$ . If $\alpha$ is not integer, then $C ^ { \alpha } ( \mathbb { R } ^ { d } ) =$ $B _ { \infty , \infty } ^ { \alpha } ( \mathbb { R } ^ { d } )$ ; if α is integer, then $B _ { 1 , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset C ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset B _ { \infty , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } )$ .

# C Goodness-of-fit Test

The goodness of fit test is a statistical hypothesis test used to determine whether the sample data fits a distribution from an expected population (e.g. a population with a normal distribution). Given data sets $X ^ { ( n ) } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ i.i.d interested in testing the null hypothesis sampled from an unknown distribution $p$ $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } } : p = p _ { 0 }$ . The goal is to check if . $X ^ { ( n ) }$ come from a distribution $p _ { 0 }$ , in other words, we are

As in the case of two-sample test, we restrict our attention to smooth densities $p , p _ { 0 } \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , and consider an alternative test

$$
\mathbb { H } _ { 1 } ^ { \mathrm { G o F } } ( \Delta _ { n } ; \mathcal { D } ) : \mathcal { D } ( p , p _ { 0 } ) \ge \Delta _ { n } ,
$$

where $\mathcal { D }$ is some discrepancy measure. Then for a test $\Phi$ based on data $X ^ { ( n ) }$ , the power of $\Phi$ is defined as

$$
\begin{array} { r } { \mathrm { p o w e r } \big ( \Phi ; \mathbb { H } _ { 1 } ^ { \mathrm { G o F } } ( \Delta _ { n } ; \mathcal { D } ) \big ) : = \operatorname* { i n f } _ { \stackrel { { p \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega ) } } { \mathcal { D } ( p , p _ { 0 } ) \geq \Delta _ { n } } } P ( \Phi \mathrm { r e j e c t } \mathbb { H } _ { 0 } ^ { \mathrm { G o F } } ) . } \end{array}
$$

Similar to the statistic $T _ { \gamma , J }$ , we can define the following statistic for approximating the squared negative Besov norm ∥p − p0∥2B−γ2,2 (Ω):

$$
T _ { \gamma , J } ^ { \mathrm { G o F } } = \frac { 1 } { n ( n - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } \Bigg \{ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \cdot \sum _ { \psi \in \Psi _ { j } } \left[ \left( \psi ( X _ { i _ { 1 } } ) - p _ { 0 \psi } \right) \left( \psi ( X _ { i _ { 2 } } ) - p _ { 0 \psi } \right) \right] \Bigg \} .
$$

As before, we normalize the statistic $T _ { \gamma , J } ^ { \mathrm { G o F } }$ to construct an optimal test statistic. Note that under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$

$$
\mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) = \frac { 2 } { n ( n - 1 ) } \mathbb { E } _ { X _ { 1 } , X _ { 2 } \sim p _ { 0 } } \bigg [ \Big ( \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \big ( \psi ( X _ { 1 } ) - p _ { 0 \psi } \big ) \cdot \big ( \psi ( X _ { 2 } ) - p _ { 0 \psi } \big ) \Big ) ^ { 2 } \bigg ] .
$$

It is then natural to consider estimating $\mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } )$ by $U$ -statistics:

$$
\begin{array} { l } { { \displaystyle \widehat { S } _ { \gamma , J } ^ { 2 } = \frac 2 { n ( n - 1 ) } \bigg \{ \frac 1 { n ( n - 1 ) } \sum _ { i _ { 1 } \neq i _ { 2 } } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i _ { 1 } } ) \psi ( X _ { i _ { 2 } } ) \right] ^ { 2 } } } \\ { { \displaystyle - \frac 2 n \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) p _ { 0 \psi } \right] ^ { 2 } + \left( \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } p _ { 0 \psi } ^ { 2 } \right) ^ { 2 } \bigg \} . } } \end{array}
$$

Similarly to the two-sample test, we slightly modify the variance estimator by considering

$$
\widetilde { S } _ { \gamma , J } ^ { 2 } = \operatorname* { m a x } ( \widehat { S } _ { \gamma , J } ^ { 2 } , \frac { 1 } { n ^ { 3 } } )
$$

to ensure the positiveness. In the end, we can define the test statistic

$$
\widetilde { T } _ { \gamma , J } ^ { \mathrm { G o F } } = \widetilde { S } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } ^ { \mathrm { G o F } } .
$$

The following theorem show the validity and power of the test induced from $\widetilde { T } _ { \gamma , J } ^ { \mathrm { G o F } }$ .

Theorem 4. Consider Test statistic $\widetilde { T } _ { \gamma , J } ^ { \mathrm { G o F } } w i t h 2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ and $\begin{array} { r } { 0 \leq \gamma \leq \frac { d } { 4 } } \end{array}$ , and level $\eta \in ( 0 , 1 )$

1. under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$ , we have $\widetilde { T } _ { \gamma , J } ^ { \mathrm { G o F } } \ \xrightarrow { d } { N } ( 0 , 1 )$

2. consider testhen for any $\Phi _ { \gamma , \eta , J } ^ { \mathrm { G o F } }$ wheand $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$ is rfies $\widetilde { T } _ { \gamma , J } ^ { \mathrm { G o F } }$ exceeds the $\eta$ -upper quantile of the standard normal, $\gamma _ { 1 } \geq 0$ $\Delta _ { n }$ $\Delta _ { n } ^ { 2 } \cdot \delta _ { n } ( \gamma _ { 1 } ) ^ { - 1 } \to \infty$

$$
\delta _ { n } ( \gamma _ { 1 } ) = \left\{ \begin{array} { c c } { n ^ { - \frac { 4 \alpha + 4 ( \gamma \wedge \gamma _ { 1 } ) } { 4 \alpha + d } } , } & { 0 < \gamma < \frac { d } { 4 } } \\ { \log n \cdot n ^ { - \frac { 4 \alpha } { 4 \alpha + d } } } & { \gamma = 0 } \\ { \log n \cdot n ^ { - 1 + \frac { 4 ( \gamma - \gamma \wedge \gamma _ { 1 } ) } { 4 \alpha + d } } , } & { \gamma = \frac { d } { 4 } , } \end{array} \right.
$$

we have

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { p o w e r } \big ( \Phi _ { \gamma , \eta , J } ^ { \mathrm { G o F } } ; \mathbb { H } _ { 1 } ^ { \mathrm { G o F } } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { W } ) \big ) = 1
$$

3. choose $\begin{array} { r } { \gamma = \frac { d } { 4 } } \end{array}$ , let $\Delta _ { n } = ( \log n ) \cdot \left( n ^ { - { \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } } \vee { \frac { 1 } { \sqrt { n } } } \right)$ √1n , then the associated test ΦGoFd ,η,J 4 satisfies that for any γ1 ≥ 0,

$$
\operatorname* { l i m } _ { n \to \infty } \mathrm { p o w e r } \big ( \Phi _ { \frac { d } { 4 } , \eta , J } ^ { \mathrm { G o F } } ; \mathbb { H } _ { 1 } ^ { \mathrm { G o F } } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { W } ) \big ) = 1 .
$$

Theorem 5. For any $\gamma _ { 1 } > 0$ , $i f \Delta _ { n } = o ( n ^ { - \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } \vee \frac { 1 } { \sqrt { n } } )$ , then there exists some $\eta \in ( 0 , 1 )$ so that for any test $\Phi _ { n }$ based on data $X ^ { ( n ) }$ that has asymptotically significance level $\eta$ , we have

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname* { i n f } _ { \mathrm { p o w e r } \left( \Phi _ { n } ; \mathbb { H } _ { 1 } ^ { \mathrm { G o F } } ( \Delta _ { n } ; d _ { \gamma _ { 1 } } ^ { H } ) \right) } < 1 .
$$

# D Proof for Goodness-of-fit Test

# D.1 Proof of Theorem 5

Since $p _ { 0 }$ is almost surely continuous, there exists $x _ { 0 } \in \Omega$ and $\delta , c > 0$ so that $p _ { 0 } ( x ) \geq c > 0$ for any $\| x - x _ { 0 } \| \leq \delta$ . So without loss of generality, we assume $[ 0 , 1 ] ^ { d } \subset \Omega$ and $p _ { 0 }$ is bounded away from zero in $[ 0 , 1 ] ^ { d }$ . We first consider the case when $d \geq 4 \gamma _ { 1 }$ . Then $\Delta _ { n } = n ^ { - { \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } }$ . Similar as the proof of Theorem 3 of Li and Yuan (2019), as proved in Ingster (1987), we only need to construct a set of density function $\{ p _ { \omega } \} _ { \omega \in \mathcal { W } }$ belong to $\mathcal { C } _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ with compact support and indexed by a multi-index $\omega$ so that

$$
\mathbb { E } _ { p _ { 0 } } \Big ( \frac { \frac { 1 } { | \mathcal { W } | } \sum _ { \omega \in \mathcal { W } } \prod _ { i = 1 } ^ { n } p _ { \omega } ( X _ { i } ) } { \prod _ { i = 1 } ^ { n } p _ { 0 } ( X _ { i } ) } \Big ) ^ { 2 } = O ( 1 ) ,
$$

and for any $\omega \in { \mathcal { W } }$

$$
d _ { \gamma _ { 1 } } ^ { H } ( p _ { 0 } , p _ { \omega } ) \gtrsim n ^ { - \frac { 2 ( \alpha + \gamma _ { 1 } ) } { 4 \alpha + d } } .
$$

To construct $p _ { \omega }$ satisfies above conditions, we set $m = \left\lceil n ^ { \frac { 2 } { 4 \alpha + d } } \right\rceil$ ,

$$
\mathcal { W } = \{ - 1 , 1 \} ^ { m ^ { d } } ,
$$

$$
\omega = \{ \omega _ { \xi } \} _ { \xi \in [ m ] ^ { d } } ,
$$

and

$$
\begin{array} { r l } & { p _ { \omega } ( x ) = p _ { 0 } ( x ) + \bigl ( \frac { 1 } { m } \bigr ) ^ { \alpha + \frac { d } { 2 } } \displaystyle \sum _ { \xi \in [ m - 1 ] ^ { d } } \omega _ { \xi } \cdot \phi _ { \xi } ( x ) } \\ & { \mathrm { w i t h } \quad \phi _ { \xi } ( x ) = m ^ { \frac { d } { 2 } } \cdot \displaystyle \prod _ { j = 1 } ^ { d } k ( m x _ { j } - \xi _ { j } ) } \\ & { \mathrm { w h e r e } \quad k ( t ) = \left\{ \begin{array} { l l } { \displaystyle - \exp \bigl ( - \frac { 1 } { 1 - ( 4 t - 1 ) ^ { 2 } } \bigr ) } & { 0 < t < \frac { 1 } { 2 } } \\ { \displaystyle - \exp \bigl ( - \frac { 1 } { 1 - ( 4 t - 3 ) ^ { 2 } } \bigr ) } & { \frac { 1 } { 2 } < t < 1 } \end{array} \right. } \end{array}
$$

Then we can check that $\{ p _ { \omega } \} _ { \omega \in \mathcal { W } } \subset C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ and $\cup _ { \omega \in \mathcal { W } } \mathrm { s u p p } ( p _ { \omega } ) \subset \Omega$ . Moreover, by equation (14) of Li and Yuan (2019), we have

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { 0 } } \bigg ( \frac { \frac { 1 } { | \mathcal { W } | } \sum _ { \omega \in \mathcal { W } } \prod _ { i = 1 } ^ { n } p _ { \omega } ( X _ { i } ) } { \prod _ { i = 1 } ^ { n } p _ { 0 } ( X _ { i } ) } \bigg ) ^ { 2 } \leq \exp \Big ( \frac { 1 } { 2 } m ^ { d } n ^ { 2 } m ^ { - 4 \alpha + 2 d } \underset { \xi \in [ m - 1 ] ^ { d } } { \operatorname* { m a x } } \big ( \int \phi _ { \xi } ^ { 2 } ( x ) / p _ { 0 } ( x ) \mathrm { d } x \big ) ^ { 2 } \Big ) } \\ & { \qquad = O ( 1 ) . } \end{array}
$$

Furthermore, for any $\omega \in { \mathcal { W } }$ , we have

$$
f _ { \omega } ( x ) = \big ( \frac { 1 } { m } \big ) ^ { \gamma _ { 1 } + \frac { d } { 2 } } \sum _ { \xi \in [ m - 1 ] ^ { d } } \omega _ { \xi } \cdot \phi _ { \xi } ( x ) \in \mathcal { C } _ { L _ { 1 } } ^ { \gamma _ { 1 } } ( \mathbb { R } ^ { d } ) ,
$$

and thus

$$
\begin{array} { r l } { d _ { \gamma _ { 1 } } ^ { H } ( p _ { 0 } , p _ { \omega } ) = } & { \underset { f \in C _ { 1 } ^ { \times } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \int f ( x ) \cdot \big ( p _ { \omega } ( x ) - p _ { 0 } ( x ) \big ) \mathrm { d } x } \\ & { \gtrsim \int f _ { \omega } ( x ) \cdot \big ( p _ { \omega } ( x ) - p _ { 0 } ( x ) \big ) \mathrm { d } x } \\ & { = \big ( \frac { 1 } { m } \big ) ^ { \gamma _ { 1 } + d + \alpha } { { \displaystyle \sum _ { \xi \in [ m - 1 ] ^ { d } } } } \underset { \xi \in [ m - 1 ] ^ { d } } { \sum } \omega _ { \xi } \cdot \omega _ { \xi _ { 1 } } \cdot \int \phi _ { \xi } ( x ) \cdot \phi _ { \xi _ { 1 } } ( x ) \mathrm { d } x } \\ & { = \big ( \frac { 1 } { m } \big ) ^ { \gamma _ { 1 } + d + \alpha } { \xi } { \in } \underset { \xi \in [ m - 1 ] ^ { d } } { \sum } \omega _ { \xi } ^ { 2 } \int \phi _ { \xi } ^ { 2 } ( x ) \mathrm { d } x } \\ & { \gtrsim m ^ { - ( \gamma _ { 1 } + \alpha ) } \asymp n ^ { - \frac { 2 ( \gamma _ { 1 } + \gamma _ { 1 } ) } { ( \alpha + \alpha ) } } . } \end{array}
$$

For the case $d < 4 \gamma _ { 1 }$ , we have $\textstyle \Delta _ { n } = { \frac { 1 } { \sqrt { n } } }$ . Consider

Then we have $\operatorname { s u p p } ( p ) \subset \Omega$ , and

$$
p ( x ) = p _ { 0 } ( x ) + \frac { 1 } { \sqrt { n } } \prod _ { j = 1 } ^ { d } k ( x _ { j } ) \in \mathcal { C } _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } ) .
$$

$$
\begin{array} { l } { d _ { \chi ^ { 2 } } ( p ( x ) , p _ { 0 } ( x ) ) = \displaystyle \int ( \frac { p ( x ) } { p _ { 0 } ( x ) } - 1 ) ^ { 2 } p _ { 0 } ( x ) \mathrm { d } x } \\ { \displaystyle \qquad = \int \frac { 1 } { n } \frac { \prod _ { j = 1 } ^ { d } k ^ { 2 } ( x _ { j } ) } { p _ { 0 } ( x ) } \mathrm { d } x } \\ { \displaystyle \qquad \lesssim \frac { 1 } { n } , } \end{array}
$$

and thus

$$
d _ { \chi ^ { 2 } } ( p ^ { \otimes n } ( x ) , p _ { 0 } ^ { \otimes n } ( x ) ) = { \cal O } ( 1 ) .
$$

Moreover, since $\begin{array} { r } { f ( x ) = \prod _ { j = 1 } ^ { d } k ( x _ { j } ) \in \mathcal { C } _ { L _ { 1 } } ^ { \gamma } ( \mathbb { R } ^ { d } ) } \end{array}$ , we have

$$
\begin{array} { l } { \displaystyle d _ { \gamma } ^ { H } ( p _ { 0 } , p ) \geq \int \prod _ { j = 1 } ^ { d } k ( x _ { j } ) \cdot ( p ( x ) - p _ { 0 } ( x ) ) \mathrm { d } x } \\ { \displaystyle = \int \frac { 1 } { \sqrt { n } } \cdot \prod _ { j = 1 } ^ { d } k ( x _ { j } ) ^ { 2 } \mathrm { d } x } \\ { \gtrsim \frac { 1 } { \sqrt { n } } . } \end{array}
$$

We can then get the desired conclusion by combining all pieces.

# D.2 Proof of Theorem 4

Throughout the proof, we use $X$ to denote the random variable sampled from $p$ , and $X _ { 1 } , X _ { 2 } , \cdots$ to denote independent random variables from $p$ . Without loss of generality, we assume $\Omega = [ 0 , 1 ] ^ { d }$ . The proof contains two part: one part is about the normality under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$ , another part is the power analysis. We first show the normality.

# D.2.1 Proof of the normality under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$

To begin with, we show $\widetilde { S } _ { \gamma , J } ^ { 2 }$ is a valid approximate for the variance of $T _ { \gamma , J } ^ { \mathrm { G o F } }$ though the following lemma.   
Lemma 3. Under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$ , the quantity $\frac { \widetilde { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) }$ converges in probability to 1 as n goes to infinity.

The proof of Lemma 3 is given in Section D.2.3. Write

$$
\widetilde { S } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } ^ { \mathrm { G o F } } = \frac { T _ { \gamma , J } ^ { \mathrm { G o F } } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } } + \left( \frac { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } } { \widetilde { S } _ { \gamma , J } } - 1 \right) \cdot \frac { T _ { \gamma , J } ^ { \mathrm { G o F } } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } } .
$$

By Lemma 3, we only need to prove that

$$
\frac { T _ { \gamma , J } ^ { \mathrm { G o F } } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } } \stackrel { d } {  } N ( 0 , 1 ) .
$$

Let

$$
H ( X _ { 1 } , X _ { 2 } ) = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \big ( \psi ( X _ { 1 } ) - p _ { 0 \psi } \big ) \cdot \big ( \psi ( X _ { 2 } ) - p _ { 0 \psi } \big ) .
$$

Then by a slight adaptation of the proof of Theorem 1 of Hall (1984), we have the following lemma.

Lemma 4. Suppose

$$
\frac { { \mathbb E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] } { n ^ { 2 } ( { \mathbb E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } \to 0 ;
$$

$$
\frac { \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] } { n ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } }  0 ;
$$

$$
\frac { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } { ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } \to 0 , w h e r e G ( x , y ) = \mathbb { E } [ H ( X , x ) H ( X , y ) ] .
$$

Then we have under $\mathbb { H } _ { 0 }$ , $\frac { T _ { \gamma , J } ^ { \mathrm { G o F } } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } } \stackrel { d } {  } N ( 0 , 1 ) .$

We first show statement (14). By equation (21) in the proof Lemma 3, we have

$$
\begin{array} { r } { \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] \gtrsim 2 ^ { J ( d - 4 \gamma ) } ; } \end{array}
$$

moreover, we can obtain

$$
\begin{array} { r l } & { \mathbb { E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] = \mathbb { E } \Big [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \big ( \psi ( X _ { 1 } ) - p _ { 0 \psi } \big ) \cdot \big ( \psi ( X _ { 2 } ) - p _ { 0 \psi } \big ) \Big ) ^ { 4 } \Big ] } \\ & { \qquad \lesssim \mathbb { E } \Big [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { 1 } ) \cdot \psi ( X _ { 2 } ) \big ) \Big ) ^ { 4 } \Big ] } \\ & { \qquad + \mathbb { E } \Big [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X ) \cdot p _ { 0 \psi } \big ) \Big ) ^ { 4 } \Big ] + \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } p _ { 0 \psi } ^ { 2 } \Big ) ^ { 4 } } \\ & { \qquad \lesssim 2 ^ { J ( 3 d - 8 \gamma ) } \cdot J , } \end{array}
$$

where the last inequality uses the bounds for terms $( A ) , ( C )$ in the proof of Lemma 3. So statement (14) holds by plugging in $2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ with $\alpha > 0$ .

Now we show statement (15). Let

$$
\widetilde { \Psi } _ { j } ( \psi ) = \big \{ \psi ^ { \prime } \in \Psi _ { j } : \operatorname { s u p p } ( \psi ) \cap \operatorname { s u p p } ( \psi ^ { \prime } ) \neq \emptyset \big \} .
$$

Then for any $j \geq j ^ { \prime }$ and $\psi \in \Psi _ { j ^ { \prime } }$ , we have

$$
\left| \widetilde { \Psi } _ { j } ( \psi ) \right| \lesssim 2 ^ { d ( j - j ^ { \prime } ) } .
$$

# We have

$$
\begin{array} { r l } & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { = \displaystyle { \mathbb { E } } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { = \displaystyle { \mathbb { E } } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad  \\ & & { = \displaystyle { \mathbb { E } } \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  = \displaystyle { \mathbb { E } } \quad \quad \quad \quad \quad \quad \quad  \end{array}
$$

Combined with (17), we can get the desired statement. The it remains to show statement (16). We have

$$
\begin{array} { r l } & { \quad \forall \{ \mathcal { G } ^ { ( 1 ) } ( X , X , Y ) \} } \\ & { = \mathbb { E } _ { X , Y } \left[ \left\{ \frac { \partial } { \partial X } \right\} \left( X , \nabla \xi , \xi , \xi , \xi , \xi , X , \xi \right) \right] \} ^ { - 1 } } \\ & { \quad = \mathbb { E } _ { X , Y , X } \left[ \left\{ \frac { \partial } { \partial X } \right\} \sum _ { i \leq \frac { 1 } { 2 } , \frac { 1 } { 2 } , \frac { 1 } { 2 } , \frac { 1 } { 2 } , \xi , \xi , \xi , \xi , \xi , \xi , \xi } \sum _ { j \leq i \leq j \leq j \leq j \leq j \leq j \leq j \leq j \leq j \leq j \leq k } \mathbb { E } _ { X , Z } \left[ \left\{ \mathcal { D } \xi ( X , \xi ) - \mathcal { D } _ { \Phi } \right\} \mathrm { i n i } \xi , \frac { 1 } { 2 } \exp \mathrm { \mathrm { i } \xi \cdot \mathcal { D } _ { \Phi } \cdot ( X , \xi ) } \right] \right. } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad }  \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times \quad \quad \quad \quad \quad } \\ &  = \mathbb { E } _  \end{array}
$$

where $( i i )$ uses the same strategy as in $( i )$ of inequality (18). We can then get the desired result by combining all pieces.

# D.2.2 Proof for the Power analysis

Since $p \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , we can write

$$
p = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } p _ { \psi } \psi ( x ) .
$$

For any $f \in \mathcal { W } _ { 1 } ^ { \gamma _ { 1 } } ( \mathbb { R } ^ { d } )$ and $\psi \in \Psi _ { j }$ ,denote $\begin{array} { r } { f _ { \psi } = \int f ( x ) \psi ( x ) \mathrm { d } x } \end{array}$ . We have

$$
\begin{array} { r l } & { \quad \underset { \underset { f \in \mathcal { W } _ { 1 } ^ { \epsilon } ( \{ \epsilon , h \} ) } { \sum \operatorname* { m a x } } } { \sum \operatorname* { m a x } } \int f \mathrm { d } \varphi _ { 0 } - \int f \mathrm { d } \varphi } \\ &  = \underset { \underset { f \in \mathcal { W } _ { 1 } ^ { \epsilon } ( \{ \epsilon , h \} ) \times \mathcal { Y } _ { 0 } ^ { \epsilon } ( \{ \epsilon , h \} ) } { \sum \sum } } { \sum } \sum _ { \{ \substack { \theta _ { 0 } < \theta _ { 0 } < \theta _ { 1 } \} \} \cdot \textit { F } _ { \Psi } } } \\ & { \quad \underset { \leq \underset { f \in \mathcal { W } _ { 1 } ^ { \epsilon } ( \{ \epsilon , h \} ) \times \mathcal { Y } _ { 0 } ^ { \epsilon } ( \{ \epsilon , h \} ) \times \mathcal { Y } _ { 0 } ^ { \epsilon } ( \{ \epsilon , h \} ) \times \mathcal { F } _ { \Psi } } { \sum \sum } } { \sum \big ( \underset { \eta _ { 0 } < \theta _ { 1 } \leq \theta _ { 1 } } { \sum } \big ) } \int _ { - 2 2 \theta _ { 1 } \times \theta _ { 1 } } { \sum } } \\ & { \quad \quad + \frac { 2 ^ { - \sqrt { \pi } \kappa _ { 1 } + \frac { 1 } { \alpha _ { 0 } } } } { \sqrt { \kappa _ { 1 } - \gamma _ { 0 } \epsilon _ { 0 } \epsilon _ { 0 } } } \left[ \underset { \epsilon \_ { f \in \mathcal { W } _ { 1 } ^ { \epsilon } ( \{ \epsilon , h \} ) \times \mathcal { Y } _ { 0 } ^ { \epsilon } ( \{ \epsilon , h \} ) } } { \sum \sum \sum \sqrt { \pi _ { 0 } + \frac { 1 } { \alpha _ { 0 } } } } \right] \underset { \leq \tau \leq \tau } { \sum \sum \operatorname* { m a x } } \int _ { \eta _ { 0 } \leq \tau } ^ { \infty } \sum _ { \tau \leq \tau \leq \tau } \mathcal { G } ^ { \theta \theta \theta - 1 } \int _ { 0 } ^ { \infty } } \\ &  \quad \leq \underset  \underset  f  \end{array}
$$

Then when $d _ { \gamma _ { 1 } } ( p _ { 0 } , p ) \geq \Delta _ { n }$ with $\Delta _ { n } ^ { 2 } \cdot \delta _ { n } ( \gamma _ { 1 } ) ^ { - 1 } \to \infty$ . We can obtain

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma _ { 1 } j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \gtrsim \Delta _ { n } ^ { 2 } .
$$

So if $\gamma _ { 1 } \geq \gamma$ , we have

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \gtrsim \Delta _ { n } ^ { 2 } ;
$$

and if $\gamma _ { 1 } < \gamma$ , we have

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \gtrsim \Delta _ { n } ^ { 2 } \cdot 2 ^ { - 2 J ( \gamma - \gamma _ { 1 } ) } ;
$$

Denote $\widetilde { \Delta } _ { n } = \Delta _ { n } ^ { 2 } \cdot 2 ^ { - 2 J ( \gamma - \gamma _ { 1 } \wedge \gamma ) }$ . To show the desired result, we only need to prove that when $\begin{array} { r } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } } \end{array}$ · $( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \stackrel { > } { \sim } \widetilde { \Delta } _ { n } , \widetilde { S } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } ^ { \mathrm { G o F } } \stackrel { P } { \longrightarrow } \infty .$ .

Note that we can rewrite the statistic T GoFγ,J as

$$
\begin{array} { r l } & { T _ { \gamma , J } ^ { \mathrm { G o F } } = \underbrace { \frac { 1 } { n ( n - 1 ) } \displaystyle \sum _ { i _ { 1 } \neq i _ { 2 } } \left\{ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \left( \psi ( X _ { i _ { 1 } } ) - p _ { \psi } \right) \cdot \left( \psi ( X _ { i _ { 2 } } ) - p _ { \psi } \right) \right\} } _ { ( A ^ { \prime } ) } } \\ & { + \underbrace { \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \left( p _ { \psi } - p _ { 0 \psi } \right) ^ { 2 } } _ { \psi \in \Psi _ { j } } + \underbrace { \frac { 2 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \left( p _ { \psi } - p _ { 0 \psi } \right) \cdot \left( \psi ( X _ { i } ) - p _ { \psi } \right) } _ { \psi \in \Psi _ { j } } . } \end{array}
$$

We first consider term $\left( A ^ { \prime } \right)$ , we have

$$
\mathbb { E } [ ( A ^ { \prime } ) ] = 0
$$

and

$$
\begin{array} { r l } { \mathrm { V a r } ( A ^ { \prime } ) = \frac { 2 } { n \langle n - 1 \rangle } \mathbb { E } \Big [ \displaystyle \Big ( \sum _ { j = 0 } ^ { 2 } - 2 ^ { 2 \nu _ { j } } \sum _ { \sigma \in \mathfrak { S } } \big ( \psi ( X _ { 1 } ) - p _ { \sigma } \big ) \cdot \big ( \psi ( X _ { 2 } ) - p _ { \sigma } \big ) \big ) ^ { 2 } \Big ] } & { } \\ { \leq \frac { 2 } { n \langle n - 1 \rangle } \mathbb { E } \Big [ \displaystyle \Big ( \sum _ { j = 0 } ^ { 4 } - 2 ^ { \nu _ { j } } \sum _ { \sigma \in \mathfrak { S } } \big ( X _ { 1 } \big ) \cdot \psi ( X _ { 2 } ) \big ) ^ { 2 } \Big ] } & { } \\ { \leq n ^ { - 2 } \cdot \displaystyle \sum _ { j = 0 } ^ { n } \sum _ { \sigma \in \mathfrak { S } _ { \sigma } ( \mathfrak { S } _ { \sigma } , \mathfrak { X _ { 2 } - \sigma } ) \leq n \leq 1 , \ldots , j = 2 } - 2 \langle n _ { 1 } + \lambda \rangle \gamma _ { \sigma } \cdot \Big ( \mathbb { E } _ { \rho _ { \sigma } } \big ( \psi _ { 1 } ( X ) \big ) ^ { 2 } \big ) ^ { \frac { n } { n } } } & { } \\ { \leq n ^ { - 2 } \cdot \displaystyle \sum _ { j = 0 } ^ { n } \sum _ { \sigma \in \mathfrak { S } _ { \sigma } ( \mathfrak { S } _ { \sigma } , \mathfrak { X _ { 2 } - \sigma } ) \leq n \leq 1 , \ldots , j = 2 } - 2 \langle n _ { 1 } + \lambda \rangle \gamma _ { \sigma } \cdot \Big ( \mathbb { E } _ { \rho _ { \sigma } } \big ( \psi _ { 1 } ( X ) \big ) ^ { 2 } \big ) ^ { \frac { n } { n } } } & { } \\  \leq n ^ { - 2 } \cdot \displaystyle \sum _ { j = 0 } ^ { n } \sum _ { \sigma \in \mathfrak { S } _ { \sigma } ( \mathfrak { S } _ { \sigma } , \mathfrak { X _ { 1 } - \sigma } ) \leq n \leq 1 } \gamma _ { \sigma } \Big ( 2 ^  -  \end{array}
$$

where $\widetilde { \Psi } _ { j } ( \psi )$ is defined in (23). The above inequality leads to

$$
{ \frac { ( A ^ { \prime } ) } { { \widetilde { \Delta } } _ { n } } } { \stackrel { P } { \longrightarrow } } 0 .
$$

For term $\left( B ^ { \prime } \right)$ , we have

$$
( B ^ { \prime } ) \gtrsim \widetilde { \Delta } _ { n } .
$$

For term $( C ^ { \prime } )$ , we have we have

$$
\mathbb { E } [ ( C ^ { \prime } ) ] = 0
$$

and

$$
\begin{array} { r l } { \operatorname { V a r } ( \mathcal { C } ) \leq \frac { 4 } { \pi } \frac { \lambda } { \alpha } \Bigg [ \Bigg ( \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } - 2 \alpha ^ { 2 } \alpha ^ { 2 } \alpha ^ { 2 } \alpha ^ { 3 } \beta _ { 1 } - ( \beta _ { 1 } - \alpha _ { 1 } ) \alpha ^ { 2 } \alpha ^ { 3 } \beta ( \Delta ) \Bigg ) ^ { 2 } \Bigg ] } \\ { - \frac { 4 } { \pi } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } 2 \ 2 \alpha ^ { 2 } \alpha ^ { 2 } \alpha ^ { 3 } \beta _ { 1 } \beta _ { 1 } \beta _ { 2 } \beta _ { 3 } \ \ \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \mathbb { P } } } ( \beta _ { 1 } , \ \gamma _ { 1 } ) \ \underset { \mathcal { C } \neq 0 } { \overset { \mathbb { P } } } ( \beta _ { 1 } , \gamma _ { 1 } ) \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \mathbb { P } } } ( \beta _ { 1 } ( \lambda ) \gamma _ { 1 } ) } \\  \leq \pi ^ { - 1 } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } 2 \ - 2 \alpha ^ { 3 } \alpha ^ { 2 } \alpha \alpha ^ { 3 } \beta _ { 1 } \beta _ { 1 } \beta _ { 2 } \ \alpha ^ { 3 } \underset { \mathcal { C } \neq 0 } { \overset { \sum } { \sum } } [ \alpha ( 1 ) \alpha ^ { 2 } ] \ \underset { \mathcal { C } \neq 0 } { \overset { \cdot } { \sum } } ( \gamma _ \end{array}
$$

Combining with the fact that $\begin{array} { r } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \gtrsim \widetilde \Delta _ { n } } \end{array}$ , we have

$$
\frac { \mathrm { V a r } ( \mathrm { C ^ { \prime } } ) } { \left( \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \right) ^ { 2 } } = o ( 1 ) ,
$$

which can lead to

$$
\frac { ( C ^ { \prime } ) } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } } \stackrel { P } { \longrightarrow } 0 .
$$

Combined with the bounds for terms $( A ^ { \prime } ) , ( B ^ { \prime } )$ and $( C ^ { \prime } )$ , we can finally obtain

$$
\frac { T _ { \gamma , J } ^ { \mathrm { G o F } } } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } } \stackrel { P } { \longrightarrow } 1
$$

Now we provide bound to the term $\widetilde { S } _ { \gamma , J }$ . Recall that $| \widetilde { S } _ { \gamma , J } - \widehat { S } _ { \gamma , J } | \lesssim n ^ { - 3 }$ and equation (22), we consider

$$
\begin{array} { r l } & { \mathbb { E } [ \widehat { S } _ { 7 , r } ^ { 2 } ] = \frac { 2 } { n ( n - 1 ) } \displaystyle \sum _ { h = 0 } ^ { J } \displaystyle \sum _ { z = 0 } ^ { J } \displaystyle \sum _ { 0 \leq t \leq r _ { 1 } } \displaystyle \sum _ { s \geq 0 \leq t \leq r _ { 2 } } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \cdot ( \mathbb { E } _ { p } \big [ \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) \big ] - p _ { 0 \wedge \ s } p _ { 0 \cdot s } ) ^ { 2 } } \\ & { \qquad \lesssim n ^ { - 2 } \cdot \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { 0 \leq t \leq r _ { 1 } } \displaystyle \sum _ { j _ { 1 } \geq - j _ { 1 } } ^ { J } \sum _ { s \geq 0 \leq t \leq r _ { 2 } ( s ) } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \cdot ( \mathbb { E } \big [ \psi _ { 1 } ( X _ { 1 } ) \psi _ { 1 } ( X _ { 2 } ) \psi _ { 2 } ( X _ { 1 } ) \psi _ { 2 } ( X _ { 2 } ) \big ] + p  } \\ & { \qquad \lesssim n ^ { - 2 } \cdot \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { 0 \leq j = 1 } ^ { J } 2 ^ { 2 ( j _ { 2 } - j _ { 1 } + j _ { 2 } ) \gamma } \cdot \sum ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \cdot 2 ^ { 2 ( j _ { 1 } + j _ { 2 } ) } } \\ &  \qquad \lesssim  \displaystyle \sum _ { \eta = - 2 , \ \frac { J ( J - 2 \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot } } ^  - 2 \cdot \frac  J ( J - 2 \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \ \end{array}
$$

So we have

$$
\frac { \widehat { S } _ { \gamma , J } } { \widetilde { \Delta } _ { n } } \stackrel { P } {  } 0 ,
$$

which leads to

$$
\frac { \widehat { S } _ { \gamma , J } } { \widetilde { \Delta } _ { n } } \stackrel { P } { \longrightarrow } 0 .
$$

Combined with statement (20) and the fact that $\begin{array} { r } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - p _ { 0 \psi } ) ^ { 2 } \gtrsim \widetilde { \Delta } _ { n } } \end{array}$ , we can obtain the desired result.

# D.2.3 Proof of Lemma 3

Under $\mathbb { H } _ { 0 } ^ { \mathrm { G o F } }$ , we have

$$
\mathbb { E } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \left( \mathbb { E } _ { p } [ \psi ( X ) - p _ { 0 \psi } ] \right) ^ { 2 } = 0 ,
$$

and

$$
\begin{array} { r l } & { \Gamma _ { 1 } - \displaystyle \frac { 2 } { \alpha ( \gamma - 1 ) } \sum _ { k _ { 1 } , \lambda = \lambda \atop \alpha } ^ { \infty } \left[ \left( \sum _ { k = 0 } ^ { 2 \pi - \lambda \atop \alpha } \sum _ { \alpha \neq \alpha } \sum _ { \alpha = \beta } \left( \alpha \Re _ { 1 } ( - 2 \alpha ) \cdot ( \beta + 2 \alpha ) - \alpha \Re _ { 2 } ( \gamma - \beta \alpha ) \right) ^ { \prime } \right] ^ { \prime } \right] } \\ & { - \displaystyle \frac { 2 } { \alpha ( \gamma - 1 ) } \sum _ { \alpha = \beta - \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \left( \sum _ { k = 0 } ^ { 2 \pi - \lambda \atop \alpha } \sum _ { \alpha = \beta - \alpha } ^ { \zeta - 1 } \left( \beta \mathbb { E } _ { \alpha } \left[ - \mathbb { E } _ { \alpha } \left( \lambda \right) - \mathbb { E } _ { \alpha } \left( \lambda \right) - \mathbb { E } _ { \alpha } \left( \gamma \right) \right] \right) ^ { \prime } \right) } \\ & { \leq \frac { \alpha } { \alpha } \displaystyle \sum _ { \alpha \neq \alpha - 1 } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \Bigg [ \mathbb { E } _ { \alpha } \left[ \exp _ { \alpha } \left( \zeta \left( \alpha \right) \right) - \mathbb { E } _ { \alpha } \left( \gamma \right) \right] ^ { \prime } \Bigg ] ^ { \prime } } \\ &  \leq \frac { \alpha } { \alpha } \displaystyle \sum _ { \alpha \neq \alpha - 1 } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _ { \alpha \neq \alpha } ^ { \zeta - 1 } \sum _  \alpha \neq \alpha \end{array}
$$

where $( i )$ is obtained by taking $j _ { 1 } = j _ { 2 }$ , $( i i )$ uses the uniform boundedness of $p _ { 0 }$ that leads to $p _ { 0 \psi } = \mathbb { E } _ { p _ { 0 } } [ \psi ( X ) ] \lesssim 2 ^ { - \frac { d j } { 2 } }$ and $\begin{array} { r } { \sum _ { j = 0 } ^ { \infty } p _ { 0 \psi } ^ { 2 } \cdot 2 ^ { 2 j \alpha } = O ( 1 ) } \end{array}$ . Therefore, we can obtain

$$
\frac { \widetilde { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } = \frac { \widehat { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } + \frac { \widetilde { S } _ { \gamma , J } ^ { 2 } - \widehat { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } = \frac { \widehat { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } + o ( 1 ) ,
$$

and we only need to prove

$$
\frac { \widehat { S } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) } \stackrel { P } { \longrightarrow } 1 .
$$

Note that

$$
\begin{array} { r l } &  \frac { 2 } { \Delta x } \widetilde { S } _ { 2 , x } ^ { 2 } \equiv \frac { 2 } { \pi ( k \pi - 1 ) } \frac  \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { 2 \sqrt { n } \gamma _ { \ell } ( X _ { 1 } ) = \ell ( X _ { 2 } ) \Big \} ^ { 2 } } \\ & { \qquad - 2 \cdot ( \displaystyle \sum _ { m \in \mathbb { R } _ { 0 } } ^ { 2 } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { 2 \sqrt { n } \gamma _ { \ell } ( X _ { 1 } ) = \ell ( X _ { 2 } ) \setminus \ell = 1 } ) ^ { 2 } + ( \displaystyle \sum _ { m = 1 } ^ { 2 } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { 2 \sqrt { n } \gamma _ { \ell } ( X _ { 2 } ) = \ell ( X _ { 1 } ) } ) ^ { 2 } \Bigg | } \\ & { = \frac { 2 } { \pi ( k \pi - 1 ) } \displaystyle \sum _ { \ell = 0 } ^ { 1 } \displaystyle \sum _ { \gamma = 0 } ^ { 1 } \sum _ { \ell = 1 } ^ { 1 } \sum _ { \ell = 1 } ^ { 2 } \sum _ { \ell = 1 } ^ { 2 \sqrt { n } \gamma _ { \ell } ( X _ { 2 } ) = \ell } \sum _ { m \in \mathbb { R } _ { 0 } } ^ { - 2 \lambda _ { \ell } ( k \pi - 1 ) } \cdot ( ( \frac { 2 \lambda _ { m } [ \Gamma _ { \ell } ( X _ { 1 } \backslash ( X _ { 2 } ) \cap \mathcal { S } _ { 2 } ( X _ { 1 } ) ) ] ^ { 2 } } { \Gamma _ { \ell } ( X _ { 1 } \backslash \ell ) } ) ^ { 2 }  } \\ &  \qquad - 2 \mathfrak { u } _ { 0 } \sqrt { \alpha } \displaystyle \sum _ { \ell = 1 } ^ { 1 } \sum _ { \ell = 1 } ^  2 \sqrt { n } \gamma _  \ell \end{array}
$$

So the estimator $\widehat { S } _ { \gamma , J } ^ { 2 }$ is unbiased. Now we bound the variance of $\widehat { S } _ { \gamma , J } ^ { 2 }$ .

$$
\begin{array} { r l } & { \Big | \lesssim \frac { 1 } { n ^ { 2 } ( n - 2 ) ^ { 2 } } \Bigg \{ \underbrace { n ^ { - 2 } \cdot \mathbb { E } _ { X _ { 1 } , X _ { 2 } \sim \rho _ { 0 } } \bigg [ \bigg ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \mathcal { Y } _ { j } } \psi ( X _ { 1 } ) \psi ( X _ { 2 } ) \bigg ) ^ { 4 } \bigg ] } _ { ( A ) } } \\ & { \quad + \underbrace { n ^ { - 1 } \cdot \mathbb { E } _ { X _ { 2 } \sim \rho _ { 0 } } \bigg [ \bigg ( \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \displaystyle \sum _ { \psi _ { 1 } \in \mathcal { Y } _ { j _ { 1 } } } \displaystyle \sum _ { \psi _ { 2 } \in \mathcal { Y } _ { j _ { 2 } } } \mathbb { E } _ { p _ { 0 } } \big [ \psi _ { 1 } ( X _ { 1 } ) \psi _ { 2 } ( X _ { 1 } ) \big ] \psi _ { 1 } ( X _ { 2 } ) \psi _ { 2 } ( X _ { 2 } ) \big ) ^ { 2 } \bigg ] } _ { ( B ) } } \\ & { \quad + \underbrace { n ^ { - 1 } \cdot \mathbb { E } _ { P _ { 0 } } \bigg [ \bigg ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \mathcal { Y } _ { j } } \psi ( X ) \cdot p _ { 0 \psi } \bigg ) ^ { 4 } \bigg ] } _ { ( C ) } \Bigg \} . } \end{array}
$$

Let

$$
\widetilde { \Psi } _ { j } ( \psi ) = \big \{ \psi ^ { \prime } \in \Psi _ { j } : \operatorname { s u p p } ( \psi ) \cap \operatorname { s u p p } ( \psi ^ { \prime } ) \neq \emptyset \big \} .
$$

Then for any $j \geq j ^ { \prime }$ and $\psi \in \Psi _ { j ^ { \prime } }$ , we have

$$
\left| \widetilde { \Psi } _ { j } ( \psi ) \right| \lesssim 2 ^ { d ( j - j ^ { \prime } ) } .
$$

Therefore, we can bound term $( C )$ as

$$
\begin{array} { l } { \displaystyle ( C ) \leq \frac { 2 4 } { n } \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { \hat { \Phi } _ { 1 } \in \Psi _ { 1 } } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { \hat { \Psi } _ { 2 } \in \hat { \Psi } _ { 2 } ( \hat { \Psi } _ { 1 } ) } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { \hat { \Psi } _ { 3 } \in \hat { \Psi } _ { j _ { 3 } } ( \hat { \Psi } _ { 2 } ) } \sum _ { j _ { 4 } = j _ { 3 } } ^ { J } \sum _ { \hat { \Psi } _ { 4 } \in \hat { \Psi } _ { j _ { 4 } } ( \hat { \Psi } _ { j _ { 3 } } ) } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) _ { \gamma } } } \\ { \displaystyle \cdot \mathbb { E } _ { \mathbb { B } _ { p _ { 0 } } } [ \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) \psi _ { 3 } ( X ) ] \cdot \log _ { 1 } \cdot \mathbb { E } _ { 0 \Psi _ { 1 } } \cdot \mathbb { E } _ { 0 \Psi _ { 0 } } } \\ { \leq \frac { 2 4 } { n } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } 2 ^ { \hat { \Phi } _ { 1 } } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { j _ { 4 } = j _ { 3 } } ^ { J } \sum _ { j _ { 4 } = j _ { 3 } } ^ { J } 2 ^ { d ( j _ { 4 } - j _ { 3 } ) } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) _ { \gamma } } } \\  \displaystyle \cdot 2 ^  - d \hat { \Phi } _ { 4 } + \frac { J } { 2 } ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j  \end{array}
$$

Similarly, we can bound term $( B )$ as

$$
\begin{array} { r l }  \gamma _ { 1 } \xi \equiv \cdots \underbrace  \sum _ { j , k = 1 } ^ { n } \sum _ { i , j = 1 } ^ { n } \sum _ { k = 0 } ^ { n } \sum _ { i , j = 1 } ^ { n } \sum _ { k = 0 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \sum _  \ell \end{array}
$$

where the last inequality uses $d \geq 4 \gamma$ , and the $\log n$ term occurs at the boundary $d = 4 \gamma$ . For the term $( A )$ ,

$$
\begin{array} { l } { \displaystyle ( A ) \lesssim n ^ { - 2 } \cdot \sum _ { j _ { 1 } = 0 } ^ { J } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { \psi _ { 2 } \in \overline { { \Psi } } _ { j _ { 2 } } ( \psi _ { 1 } ) } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { \psi _ { 3 } \in \overline { { \Psi } } _ { j _ { 3 } } ( \psi _ { 2 } ) } \sum _ { j _ { 4 } = j _ { 3 } } ^ { J } \sum _ { \psi _ { 4 } \in \overline { { \Psi } } _ { j _ { 4 } } ( \psi _ { 3 } ) } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) } \gamma } \\ { \cdot \left( \mathbb { E } _ { p _ { 0 } } [ \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) \psi _ { 3 } ( X ) \psi _ { 4 } ( X ) ] \right) ^ { 2 } } \\ { \lesssim n ^ { - 2 } \cdot \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { j _ { 4 } = j _ { 3 } } ^ { J } 2 ^ { d j _ { 4 } } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) \gamma } \left( 2 ^ { - d j _ { 4 } } \cdot 2 ^ { \frac { d } { 2 } ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) } \right) ^ { 2 } } \\ { \lesssim \frac { J } { n ^ { 2 } } \cdot 2 ^ { J ( 3 d - 8 \gamma ) } . } \end{array}
$$

So, combine with the bound to terms $( A ) , ( B )$ , and $( C )$ and plug in $2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ , we have

$$
\mathrm { V a r } ( \widehat { S } _ { \gamma , J } ^ { 2 } ) = o \big ( n ^ { - 4 + \frac { 4 d - 1 6 \gamma } { 4 \alpha + d } } \big ) .
$$

Combined with the upper bound (21) to $\mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } )$ , we have

$$
\mathrm { V a r } ( \widehat { S } _ { \gamma , J } ^ { 2 } ) = o \Big ( ( \mathrm { V a r } ( T _ { \gamma , J } ^ { \mathrm { G o F } } ) ) ^ { 2 } \Big ) .
$$

Then combined with the unbiasedness of $\widehat { S } _ { \gamma } ^ { 2 }$ , we can obtain the desired conclusion.

# E Proof for Two-sample Test

# E.1 Proof of Theorem 1

The proof of Theorem 1 directly follows from the result of Theorem 5 and the argument of the proof of Theorem 5 in Li and Yuan (2019).

# E.2 Proof of Theorem 2

Throughout the proof, we denote

$$
\widetilde { \Psi } _ { j } ( \psi ) = \big \{ \psi ^ { \prime } \in \Psi _ { j } : \operatorname { s u p p } ( \psi ) \cap \operatorname { s u p p } ( \psi ^ { \prime } ) \neq \emptyset \big \} .
$$

We use $X$ , $Y$ to denote random variables from $p$ and $q$ respectively. We use $X _ { 1 } , X _ { 2 } , \cdots$ to denote independent random variables from $p$ ; and we use $Y _ { 1 } , Y _ { 2 } , \cdots$ to denote independent random variables from $q$ . Without loss of generality, we assume $\Omega = [ 0 , 1 ] ^ { d }$ . The proof contains two part: one part is about the normality under $\mathbb { H } _ { 0 }$ , another part is the power analysis. We first show the normality.

# E.2.1 Proof of the normality under $\mathbb { H } _ { 0 }$

Since $p , q \in \mathcal { W } _ { L } ^ { u , \alpha } ( \Omega )$ , we can write

$$
\begin{array} { l } { \displaystyle p = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } p _ { \psi } \psi ( x ) , } \\ { \displaystyle q = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } q _ { \psi } \psi ( x ) . } \end{array}
$$

Similar to the proof of Theorem 4, we first show $\widetilde { \mathcal { S } } _ { \gamma , J } ^ { 2 }$ is a valid approximate for the variance of $T _ { \gamma , J }$ though the following lemma.

Lemma 5. Under $\mathbb { H } _ { 0 }$ , the quantity $\frac { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \operatorname { V a r } ( T _ { \gamma , J } ) }$ converges in probability to 1 as n goes to infinity.

The proof of Lemma 5 is given in Section E.2.3. Write

$$
\widetilde { \mathcal { S } } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } = \frac { T _ { \gamma , J } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ) } } + \biggl ( \frac { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ) } } { \widetilde { \mathcal { S } } _ { \gamma , J } } - 1 \biggr ) \cdot \frac { T _ { \gamma , J } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ) } } .
$$

By Lemma 5, we only need to prove that

$$
\frac { T _ { \gamma , J } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ) } } \stackrel { d } {  } N ( 0 , 1 ) .
$$

Let

$$
{ \cal H } ( X _ { 1 } , X _ { 2 } ) = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \big ( \psi ( X _ { 1 } ) - q _ { \psi } \big ) \cdot \big ( \psi ( X _ { 2 } ) - q _ { \psi } \big ) .
$$

Without loss of generality, we can assume $n \geq m$ . Then under $\mathbb { H } _ { 0 }$ , we can rewrite

$$
\begin{array} { l } { { \displaystyle T _ { \gamma , J } = \frac { 2 } { n ( n - 1 ) } \sum _ { 1 \leq i _ { 1 } < i _ { 2 } \leq n } H ( X _ { i _ { 1 } } , X _ { i _ { 2 } } ) + \frac { 2 } { m ( m - 1 ) } \sum _ { 1 \leq w _ { 1 } < w _ { 2 } \leq m } H ( Y _ { w _ { 1 } } , Y _ { w _ { 2 } } ) - \frac { 2 } { n m } \sum _ { i = 1 } ^ { n } \sum _ { w = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) \} \mathrm { ~ a ~ n ~ d ~ } } } \\ { { \displaystyle \quad \quad = \sum _ { i = 2 } ^ { m } \sum _ { j = 1 } ^ { i - 1 } \left[ \frac { 2 } { n ( n - 1 ) } H ( X _ { i } , X _ { j } ) + \frac { 2 } { m ( m - 1 ) } H ( Y _ { i } , Y _ { j } ) - \frac { 2 } { n m } \big ( H ( X _ { i } , Y _ { j } ) + H ( X _ { j } , Y _ { i } ) \big ) \right] \mathrm { ~ a ~ n ~ d ~ } } } \\ { { \displaystyle \quad \quad + \sum _ { i = m + 1 } ^ { n } \left[ \sum _ { j = 1 } ^ { i - 1 } \frac { 2 } { n ( n - 1 ) } H ( X _ { i } , X _ { j } ) - \frac { 2 } { n m } \sum _ { j = 1 } ^ { m } H ( X _ { i } , Y _ { j } ) \big ) \right] - \frac { 2 } { n m } \sum _ { i = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) . } } \end{array}
$$

Then by a adaptation of the proof of Theorem 1 of Hall (1984), we have the following lemma.

Lemma 6. Suppose $\textstyle 0 < c \leq { \frac { n } { m } } \leq C < \infty$ for constants $c , C$ , and

$$
\frac { \frac { 2 } { n m } \sum _ { i = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) } { \sqrt { \operatorname { V a r } ( T _ { \gamma , J } ) } } = o _ { p } ( 1 ) ;
$$

$$
\frac { { \mathbb E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] } { n ^ { 2 } ( { \mathbb E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } \to 0 ;
$$

$$
\frac { \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] } { n ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } }  0 ;
$$

Then we have under $\mathbb { H } _ { 0 }$ , $\frac { T _ { \gamma , J } } { \sqrt { \mathrm { V a r } ( T _ { \gamma , J } ) } } \stackrel { d } {  } N ( 0 , 1 )$

Note that

$$
\mathbb { E } [ \frac { 2 } { n m } \sum _ { i = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) ] = 0
$$

and

$$
\begin{array} { l } { { \displaystyle \mathrm { V a r } \Big ( \frac { 2 } { n m } \sum _ { i = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) \Big ) \lesssim n ^ { - 3 } \mathrm { V a r } [ H ( X _ { 1 } , X _ { 2 } ) ] } } \\ { ~ \lesssim n ^ { - 3 } \cdot \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } 2 ^ { d j _ { 1 } } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } } \\ { ~ \lesssim \left\{ \begin{array} { l l } { \displaystyle n ^ { - 3 } \cdot \frac { 2 ^ { J ( d - 4 \gamma ) } - 2 ^ { \frac { J } { 2 } ( d - 4 \gamma ) } } { n ^ { - 3 } \cdot 2 ^ { d J } \cdot \cdot 1 } } & { \displaystyle \gamma > 0 } \\ { \displaystyle n ^ { - 3 } \cdot 2 ^ { d J } \cdot J } & { \displaystyle \gamma = 0 } \end{array} \right. }  \\ { { \displaystyle = o \big ( \mathrm { V a r } ( T _ { \gamma , j } ) \big ) } , } \end{array}
$$

where the last inequality uses (28). So combined with equations (14), (15) and (16) in the proof of Theorem 4. We can obtain the desired result.

# E.2.2 Proof for the Power analysis

Follow the proof of Theorem 4. When $d _ { \gamma _ { 1 } } ( p , q ) \geq \Delta _ { n }$ with $\Delta _ { n } ^ { 2 } \cdot \delta _ { n } ( \gamma _ { 1 } ) ^ { - 1 } \to \infty$ , we can obtain

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma _ { 1 } j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \stackrel { > } { \sim } \Delta _ { n } ^ { 2 } .
$$

So if $\gamma _ { 1 } \geq \gamma$ , we have

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \gtrsim \Delta _ { n } ^ { 2 } ;
$$

and if $\gamma _ { 1 } < \gamma$ , we have

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \gtrsim \Delta _ { n } ^ { 2 } \cdot 2 ^ { - 2 J ( \gamma - \gamma _ { 1 } ) } ;
$$

Denote $\begin{array} { r l r } { \widetilde \Delta _ { n } } & { { } = } & { \Delta _ { n } ^ { 2 } \mathrm { ~  ~ \cdot ~ } 2 ^ { - 2 J ( \gamma - \gamma _ { 1 } \wedge \gamma ) } } \end{array}$ . To show the desired result, we only need to prove that when $\begin{array} { r } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \gtrsim \widetilde { \Delta } _ { n } , \widetilde { \mathcal { S } } _ { \gamma , J } ^ { - 1 } T _ { \gamma , J } \stackrel { P } { \longrightarrow } \infty . } \end{array}$ .

Note that we can rewrite the statistic $T _ { \gamma , J }$ as

$$
\begin{array} { r l } &  T _ { s , y } = \cfrac { 1 } { \kappa ( \omega - 1 ) } \displaystyle \sum _ { i , j ^ { \prime } \in \mathcal { S } } \{ \begin{array} { l l } { \sum _ { j ^ { \prime } \in \mathcal { S } } ^ { 2 - \nu _ { 2 } } \sum _ { s \in \mathcal { S } } ( \psi ( X _ { i } ) - p _ { s } ) \cdot ( \psi ( X _ { i + 2 } ) - p _ { s } ) \} } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { + \cfrac { 1 } { \kappa ( \omega - 1 ) } \displaystyle \sum _ { s \in \mathcal { S } } \{ \begin{array} { l l } { \sum _ { j ^ { \prime } \in \mathcal { S } } ^ { 2 - \nu _ { 2 } } \sum _ { s \in \mathcal { S } } ( \psi ( Y _ { s , x } ) - q _ { s } ) \cdot ( \psi ( Y _ { s , x } ) - q _ { s } ) \cdot ( \psi ( Y _ { s , x } ) - q _ { s } ) } \\ { \qquad } \\ { \quad } \\ { \quad } \\ { + \frac { \nu _ { 2 } } { \kappa ( \omega - 1 ) } \sum _ { s \in \mathcal { S } } ( p _ { s } - q _ { s } ) ^ { 2 } + \frac { 2 } { \kappa } \sum _ { i = 1 } ^ { n } \sum _ { s \in \mathcal { S } } 2 ^ { - 2 \nu _ { 2 } } \sum _ { s \in \mathcal { S } } ( p _ { s } - q _ { s } ) \cdot ( \psi ( X _ { i } ) - p _ { s } ) } \end{array} \} } \\ &  \quad + \frac { 2 } { \kappa } \displaystyle \sum _ { s \in \mathcal { S } } \sum _ { s \in \mathcal { S } } \frac { 1 } { \kappa ( \omega - 1 ) } \sum _ { s \in \mathcal { S } } \{ \begin{array} { l l } { 0 } \\ { 0 } \\  \frac { \kappa _ { 2 } } { \kappa ( \omega - 1 ) } \sum _ { s \in \mathcal { S } } 2 ^ { - 2 \nu _ { 2 } } \sum _ { s \in \mathcal { S } } ( q _ { s } - p _ { s } )  \end{array} \end{array} \end{array}
$$

By tracking the proof of Theorem 4 in Section D.2.2, it remains to show

$$
\frac { ( F ) } { { \widetilde { \Delta } } _ { n } } \overset { P } { \longrightarrow } 0 ,
$$

and

$$
\frac { \widehat { \mathcal { S } _ { \gamma , J } } } { \widetilde { \Delta } _ { n } } \stackrel { P } { \longrightarrow } 0 .
$$

Since

$$
E [ ( F ) ] = 0 ,
$$

and

$$
\begin{array} { r l } & { \mathrm { V a r } ( F ) = \displaystyle \frac { 4 } { n m } \cdot \mathbb { E } \bigg [ \bigg ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \big ( \psi ( X ) - p _ { \psi } \big ) \cdot \big ( \psi ( Y ) - q _ { \psi } \big ) \bigg ) ^ { 2 } \bigg ] } \\ & { \quad \quad \lesssim n ^ { - 2 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } 2 ^ { d j _ { 2 } } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \cdot 2 ^ { - 2 d j _ { 2 } } \cdot 2 ^ { d ( j _ { 1 } + j _ { 2 } ) } } \\ & { \quad \quad \lesssim \left\{ \begin{array} { l l } { \displaystyle n ^ { - 2 } \cdot \frac { 2 ^ { J ( d - 4 \gamma ) } - 1 } { 2 ^ { d - 4 \gamma } - 1 } } & { \gamma > 0 } \\ { \displaystyle n ^ { - 2 } \cdot 2 ^ { d J } \cdot \cdot J } & { \gamma = 0 } \end{array} \right. } \\ & { \quad \quad = o ( \widetilde { \Delta } _ { n } ^ { 2 } ) , } \end{array}
$$

which proves statement (26). Now we provide bound to the term $\widehat { \mathcal { S } } _ { \gamma , J }$ . Recall $\overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 }$ defined in equation (29), we have

$$
\begin{array} { r l } & { \mathbb { E } [ \hat { \mathcal { G } } _ { \tau } ^ { 2 } ] - \mathbb { E } [ \hat { \mathcal { G } } _ { \tau } ^ { 2 } ] \Big \vert } \\ & { \lesssim 2 \big ( \displaystyle \frac { 1 } { m ( n - 1 ) } + \frac { 1 } { m ( m - 1 ) } + \frac { 2 } { m n } \big ) } \\ & { \cdot \Big \{ \displaystyle \sum _ { \hat { \gamma } = 0 } ^ { \mathcal { J } } \sum _ { \hat { \sigma } = 0 } ^ { \mathcal { J } } 2 ^ { - 2 ( \hat { \sigma } _ { 1 } + \hat { \sigma } _ { 2 } ) \tau } \sum _ { \Phi _ { 1 } \in \mathcal { S } _ { 0 } } \sum _ { \Phi \in \mathcal { S } _ { 0 } } \Big [ \frac { 1 } { m } \cdot \mathbb { E } [ \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) ] \cdot \big ( q _ { \Phi _ { 1 } } q _ { \Phi _ { 2 } } + \mathbb { E } [ \hat { \psi } _ { 1 } ( Y ) \psi _ { 2 } ( Y ) ] \big ) } \\ & { \qquad + \displaystyle \frac { 1 } { n } \cdot \mathbb { E } [ \psi _ { 1 } ( Y ) \psi _ { 2 } ( Y ) ] \cdot \big ( p _ { \Phi _ { 1 } } p _ { \Phi _ { 2 } } + \mathbb { E } [ \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) ] \big ) \Big ] + \Big ( \displaystyle \sum _ { \hat { \gamma } = 0 } ^ { \mathcal { J } } \sum _ { \Phi \in \mathcal { S } _ { 0 } } 2 ^ { - 2 ( \hat { \gamma } - \hat { \sigma } _ { 2 } ) \tau } p _ { \Phi \notin \Phi } \Big ) ^ { 2 } } \\ &  \lesssim n ^ { - 3 } \displaystyle \sum _ { \hat { \gamma } = 0 } ^ { \mathcal { J } } \sum _ { \Phi = 1 } ^ { \mathcal { J } } [ 2 ^ { \Phi _ { 2 } } \cdot 2 ^ { - 2 ( \hat { \mu } + \hat { \sigma } _ { 2 } ) \tau } \cdot 2 ^ { - 2 \hat { \alpha } \hat { \mu } _ { 2 } } \cdot 2 ^  \hat { \alpha }  \end{array}
$$

Therefore, we only need to consider

$$
\begin{array} { r l } & { - 2 \frac { 1 } { 6 \omega ( k - 1 ) } + \frac { 1 } { 2 \omega ( k - 1 ) } + \frac { 1 } { 3 \omega ( k - 1 ) } + \frac { 2 } { \omega ( k ) } , ~ k = \left[ \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i } ^ { 2 } \cdots \cdots \right) \omega ( k ) \omega ( k ) \right] ^ { 2 } } \\ & { \quad - \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \cdots \right) \omega ( k ) \omega ( k ) \omega + \displaystyle \int _ { - \infty } ^ { 1 } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \cdots \right) } \\ & { \quad - 2 \frac { 1 } { \omega ( k - 1 ) } + \frac { 1 } { 2 \omega ( k - 1 ) } + \frac { 2 } { \omega ( k - 1 ) } , ~ k = \left[ \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \right) \omega ( k ) \right] ^ { 2 } + \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \right) \omega ( k ) \omega ( k ) \cdots } \\ & { \quad - 2 \frac { 1 } { \omega ( k - 1 ) } + \frac { 1 } { 2 \omega ( k - 1 ) } + \frac { 2 } { \omega ( k - 1 ) } , ~ k = \left[ \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \right) \omega ( k ) \right] ^ { 2 } } \\ &  \quad \leq \omega ^ { 2 } \leq \left[ \left( \frac { k ^ { 2 } } { 2 \omega ( k - 1 ) } \sum _ { i , j = 1 \atop i \neq j \neq i - 1 } ^ { 2 } \cdots \right) \omega ( k \end{array}
$$

which leads to statement (27). We can then obtain the desired result.

# E.2.3 Proof of Lemma 5

Under $\mathbb { H } _ { 0 }$ , we have

$$
\mathbb { E } ( T _ { \gamma , J } ) = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \left( p _ { \psi } - q _ { \psi } \right) ^ { 2 } = 0 ,
$$

and

$$
\begin{array} { r l } { \operatorname { S u r f } _ { \mathbf { x } \in \mathcal { R } _ { - 1 } } \left\{ \operatorname { S u r f } _ { \mathbf { x } \in \mathcal { R } _ { 1 } } \left( \left[ \begin{array} { l } { 1 } \\ { - 1 } \\ { \operatorname { S u r f } _ { \mathbf { x } \in \mathcal { R } _ { 1 } } \left( \frac { 1 } { \rho _ { 2 } } \right) } \\ { 1 } \end{array} \right] - \frac { 1 } { 2 \rho _ { 1 } } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \right\} \Bigg ] \right. } \\ { + \left. \exp _ { i - 1 } - \sum _ { k = 1 } ^ { n } \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \right\} \Bigg \} } \\  - \frac { 2 } { \rho _ { 1 } } \sum _ { i = 1 } ^ { n } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 } ^ { i - 1 } \exp _ { i , k = 1 }  \end{array}
$$

where the last inequality is obtained by using the same strategy as in (21). Therefore, we can obtain

$$
\frac { \widetilde { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ) } = \frac { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ) } + \frac { \widetilde { \mathcal { S } } _ { \gamma , J } ^ { 2 } - \widetilde { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ) } = \frac { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ) } + o ( 1 ) ,
$$

and we only need to prove

$$
\frac { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } } { \operatorname { V a r } ( T _ { \gamma , J } ) } \stackrel { P } { \longrightarrow } 1 .
$$

Denote

$$
\begin{array} { r l } { \overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 } = 2 \Big ( \frac { 1 } { n ( n - 1 ) } + \frac { 1 } { m ( m - 1 ) } + \frac { 2 } { m n } \Big ) \cdot \bigg \{ \frac { 1 } { n m } \displaystyle \sum _ { i _ { 1 } = 1 } ^ { n } \sum _ { i _ { 2 } = 1 } ^ { m } \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i _ { 1 } } ) \psi ( Y _ { i _ { 2 } } ) \Big ) ^ { 2 } } & { } \\ { \quad \quad \quad \quad - \frac { 1 } { n } \displaystyle \sum _ { i _ { 1 } = 1 } ^ { n } \Big [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i _ { 1 } } ) \cdot q _ { \psi } \Big ] ^ { 2 } - \frac { 1 } { m } \displaystyle \sum _ { i _ { 2 } = 1 } ^ { m } \Big [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( Y _ { i _ { 2 } } ) \cdot p _ { \psi } \Big ] } & { } \\ { \quad \quad \quad \quad + \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \cdot q _ { \psi } \cdot p _ { \psi } \Big ) ^ { 2 } \bigg \} . } \end{array}
$$

We now show that $\widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 }$ is close to $\overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 }$ . Note that

$$
\begin{array} { l } { \displaystyle \left| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot \left( \frac { 1 } { m } \sum _ { w = 1 } ^ { m } \psi ( Y _ { w } ) \right) \right] ^ { 2 } - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot q _ { \psi } \right] ^ { 2 } \right| } \\ { \displaystyle = \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot \left( \frac { 1 } { m } \sum _ { w = 1 } ^ { m } \psi ( Y _ { w } ) - q _ { \psi } \right) \right] \right. } \\ { \displaystyle \qquad \cdot \left. \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot \left( \frac { 1 } { m } \sum _ { w = 1 } ^ { m } \psi ( Y _ { w } ) + q _ { \psi } \right) \right] \right| } \end{array}
$$

Since for any $j \in \{ 0 , 1 , \cdots , J \}$ , $\psi ( Y ) \lesssim 2 ^ { \frac { d j } { 2 } }$ and by the uniform boundedness of $q$ , we have $\mathbb { E } _ { q } [ \psi ( Y ) ^ { 2 } ] = O ( 1 )$ and $\mathbb { E } _ { q } [ \psi ( Y ) ] = O ( 2 ^ { - \frac { d j } { 2 } } )$ . Then by Bernstein’s inequality and a union bound, we have it holds with probability at least $1 - n ^ { - 1 }$ that for any $j \in \{ 0 , 1 , \cdots , J \}$ and $\psi \in \Psi _ { j }$ ,

$$
{ \Big | } { \frac { 1 } { m } } \sum _ { w = 1 } ^ { m } \psi ( Y _ { w } ) - q _ { \psi } { \Big | } \lesssim { \sqrt { \frac { \log n } { n } } } + { \frac { \log n } { n } } \cdot 2 ^ { \frac { d j } { 2 } } .
$$

Therefore it holds with probability at least $1 - n ^ { - 1 }$ that

$$
\begin{array} { r l } & { \displaystyle | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot ( \frac { 1 } { m } \displaystyle \sum _ { u = 1 } ^ { m } \psi ( X _ { u } ) ) ] ^ { 2 } - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot q _ { \psi } ] ^ { 2 } | } \\ & { \lesssim \displaystyle \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } | \psi ( X _ { i } ) | \cdot ( \displaystyle \sqrt { \frac { \log n } { n } } + \frac { \log n } { n } \cdot 2 ^ { \frac { \lambda } { 2 } } ) ] } \\ & { \qquad \cdot \displaystyle [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } | \psi ( X _ { i } ) | \cdot ( \displaystyle \sqrt { \frac { \log n } { n } } + \frac { \log n } { n } \cdot 2 ^ { \frac { \lambda \psi } { 2 } } + 2 ^ { - \frac { \lambda \psi } { 2 } } ) ] } \\ &  \lesssim \displaystyle \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } } \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi _ { j } \geq \tilde { \Psi } _ { i } \geq \tilde { \Psi } _ { j } \atop \psi \in \Psi _ { j } } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } ( \frac { \log n } { n } + ( \frac { \log n } { n } ) ^ { 2 } 2 ^  \frac  \lambda ( j _  \end{array}
$$

Then we have

$$
\begin{array} { l }  { \displaystyle { E [ ( D ) ] \lesssim \sum _ { j _ { 2 } = 0 } ^ { J } \sum _ { j _ { 1 } \geq j _ { 2 } } ^ { J } 2 ^ { d j _ { 1 } } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } ) \gamma } \Big ( \frac { \log n } { n } + ( \frac { \log n } { n } ) ^ { 2 } 2 ^ { \frac { d ( j _ { 1 } + j _ { 2 } ) } { 2 } } + \sqrt { \frac { \log n } { n } } 2 ^ { - \frac { d } { 2 } j _ { 2 } } \Big ) \cdot 2 ^ { - d j _ { 1 } } \cdot 2 ^ { \frac { d ( j _ { 1 } + j _ { 2 } ) } { 2 } } } } \\ { { \displaystyle \quad = o \Big ( \frac { 2 ^ { J ( d - 4 \gamma ) } - 2 ^ { \frac { J } { 2 } ( d - 4 \gamma ) } } { 2 ^ { d - 4 \gamma } - 1 } \Big ) } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle \mathrm { V a r } ( D ) \lesssim n ^ { - 1 } \sum _ { j _ { 1 } = 0 } ^ { J } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { \psi _ { 2 } \in \Phi _ { j _ { 2 } } ( \psi _ { 1 } ) } \sum _ { \substack { j _ { 3 } = j _ { 2 } } } \sum _ { \psi _ { 3 } \in \tilde { \Psi } _ { j _ { 3 } } ( \psi _ { 2 } ) } \sum _ { \substack { j _ { 4 } = j _ { 3 } } } ^ { J } \sum _ { \substack { \psi _ { 4 } \in \tilde { \Psi } _ { j _ { 4 } } ( \psi _ { 3 } ) } } 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) } \gamma } }  \\ { { \displaystyle \quad \quad \cdot \left( \frac { \log n } { n } + ( \frac { \log n } { n } ) ^ { 2 } 2 ^ { \frac { a ( j _ { 1 } + j _ { 2 } ) } { 2 } } + \sqrt { \frac { \log n } { n } } 2 ^ { - \frac { a ^ { 2 } } { 2 ^ { j _ { 2 } } } } \right) ^ { 2 } . { \mathbb { E } } \big [ | \psi _ { 1 } ( X ) \psi _ { 2 } ( X ) \psi _ { 3 } ( X ) \psi _ { 4 } ( X ) | \big ] } } \\   \displaystyle \quad \lesssim n ^ { - 1 } \sum _ { j _ { 1 } = 0 } ^ { J } \sum _ { j _ { 2 } = j _ { 1 } } ^ { J } \sum _ { j _ { 3 } = j _ { 2 } } ^ { J } \sum _ { \substack { j _ { 4 } = j _ { 3 } } } ^ { J } 2 ^ { 2 \mathcal { I } _ { 4 } } \cdot 2 ^ { - 2 ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) \gamma } \cdot 2 ^ { - d j _ { 4 } } \cdot 2 ^  \frac { a ( j _ { 1 } + j _ { 2 } + j _ { 3 } + j _ { 4 } ) }  2 ^  - \frac  a  \end{array}
$$

Therefore, we can get

$$
\begin{array} { l } { \displaystyle \left. \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot \left( \frac { 1 } { m } \sum _ { w = 1 } ^ { m } \psi ( Y _ { w } ) \right) \right] ^ { 2 } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left[ \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { i } ) \cdot q _ { \psi } \right] ^ { 2 } \right. } \\ { \displaystyle = o _ { p } \Big ( \frac { 2 ^ { J ( d - 4 \gamma ) } - 2 ^ { \frac { J } { 2 } ( d - 4 \gamma ) } } { 2 ^ { d - 4 \gamma } - 1 } \Big ) . } \end{array}
$$

Similarly, we can show

$$
\begin{array} { r l } & { \bigg | \frac { 1 } { n } \displaystyle \sum _ { w = 1 } ^ { m } \Big [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( Y _ { w } ) \cdot \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \psi ( X _ { i } ) \Big ) \Big ] ^ { 2 } - \frac { 1 } { m } \displaystyle \sum _ { w = 1 } ^ { m } \Big [ \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( Y _ { w } ) \cdot p _ { \psi } \Big ] ^ { 2 } \bigg | } \\ & { = o _ { p } \Big ( \displaystyle \frac { 2 ^ { J ( d - 4 \gamma ) } - 2 ^ { \frac { J } { 2 } ( d - 4 \gamma ) } } { 2 ^ { d - 4 \gamma } - 1 } \Big ) . } \end{array}
$$

Moreover, we have

$$
\Big ( \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \cdot q _ { \psi } \cdot p _ { \psi } \Big ) ^ { 2 } = O ( 1 ) = o \Big ( \frac { 2 ^ { J ( d - 4 \gamma ) } - 2 ^ { \frac { J } { 2 } ( d - 4 \gamma ) } } { 2 ^ { d - 4 \gamma } - 1 } \Big ) .
$$

Then combined with the upper bound (28) to $\mathrm { V a r } ( T _ { \gamma , J } )$ , we have obtain

$$
\frac { \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } - \overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 } } { \mathrm { V a r } ( T _ { \gamma , J } ) } \overset { P } { \longrightarrow } 0 .
$$

Therefore, it remains to show

$$
\frac { \overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 } } { \operatorname { V a r } ( T _ { \gamma , J } ) } \overset { P } { \longrightarrow } 1 .
$$

Note that under $\mathbb { H } _ { 0 }$ ,

$$
\begin{array} { c } { { \displaystyle | \overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 } | = 2 \left( \frac 1 { n ( n - 1 ) } + \frac 1 { m ( m - 1 ) } + \frac 2 { m n } \right) \cdot \mathbb { E } \bigg [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( X ) \psi ( Y ) \Big ) ^ { 2 } } } \\ { { - \left( \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( X ) \cdot q _ { \psi } \right) ^ { 2 } - \left( \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } \psi ( Y ) \cdot p _ { \psi } \right) ^ { 2 } + \left( \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } p ( X ) \right) \cdot p _ { \psi } ( X ) \bigg ] } } \\ { { \mathrm { u n d e r } ^ { \mathbb { H } } _ { 0 } } } \\ { { = \displaystyle \sum _ { j = 0 } ^ { J } \left( \frac 1 { n ( n - 1 ) } + \frac 1 { m ( m - 1 ) } + \frac 2 { m n } \right) \cdot \mathbb { E } \bigg [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } ( \psi ( X _ { 1 } ) - p _ { \psi } ) ( \psi ( X _ { 2 } ) - p _ { \psi } ) ( \psi ( X _ { 2 } ) - p _ { \psi } ) ( \psi ( X ) + p _ { \psi } ) \Big ) ^ { 2 } } } \\ { { = \mathrm { V a r } ( T _ { \gamma , J } ) . } } \end{array}
$$

So the estimator S 2γ, is unbiased. Now we bound the variance of $\overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 }$

$$
\begin{array} { r l } & { \mathrm { V a r } ( \overline { { \mathcal { S } } } _ { \gamma , J } ^ { 2 } ) \lesssim n ^ { - 4 } \bigg \{ \frac { 1 } { n m } \cdot \mathbb { E } \Big [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X _ { 1 } ) \psi ( X _ { 2 } ) \Big ) ^ { 4 } \Big ] } \\ & { \qquad + \left( n ^ { - 1 } + m ^ { - 1 } \right) \cdot \mathbb { E } \Big [ \Big ( \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \displaystyle \sum _ { \psi \in \Psi _ { j } } \psi ( X ) \cdot p _ { \psi } \Big ) ^ { 4 } \Big ] \bigg \} \lesssim \frac { J } { n ^ { 6 } } 2 ^ { J ( 3 d - 8 \gamma ) } + \frac { J ^ { 2 } } { n ^ { 5 } } 2 ^ { J ( 2 d - 8 \gamma ) } } \end{array}
$$

where the last inequality uses the bounds of terms $( A )$ and $( C )$ in the proof of Lemma 3. So plug in $2 ^ { J } \asymp n ^ { \frac { 2 } { 4 \alpha + d } }$ , we have

$$
\operatorname { V a r } ( { \widehat { \mathcal { S } } } _ { \gamma , J } ^ { 2 } ) = o { \left( n ^ { - 4 + { \frac { 4 d - 1 6 \gamma } { 4 \alpha + d } } } \right) } .
$$

Combined with the upper bound (28) to $\mathrm { V a r } ( T _ { \gamma , J } )$ , we have

$$
\operatorname { V a r } ( \widehat { \mathcal { S } } _ { \gamma , J } ^ { 2 } ) = o \Big ( ( \operatorname { V a r } ( T _ { \gamma , J } ) ) ^ { 2 } \Big ) .
$$

Then combined with the unbiasedness of $\widehat { \mathcal { S } _ { \gamma } ^ { 2 } }$ , we can obtain the desired conclusion.

# F Proof of Technical Results

# F.1 Proof of Lemma 1

For the left hand side, for any $f \in \mathcal { W } _ { 1 } ^ { \gamma _ { 1 } } ( \mathbb { R } ^ { d } )$ and $\boldsymbol { \psi } \in \overline { { \Psi } } _ { j }$ ,denote $\begin{array} { r } { f _ { \psi } = \int f ( x ) \psi ( x ) \mathrm { d } x } \end{array}$ . We have

$$
\begin{array} { r l } & { d _ { \gamma } ^ { W } ( p , q ) = \underset { f \in \mathcal { W } _ { 1 } ^ { \mathbb { N } } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \int f \mathrm { d } p - \int f \mathrm { d } q } \\ & { = \underset { f \in \mathcal { W } _ { 1 } ^ { \mathbb { N } } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \underset { j = 0 } { \overset { \sum } { \sum } } \underset { \psi \in \overline { { \mathbb { W } } } _ { 2 } } { \operatorname* { s u p } } ( p _ { \psi } - q _ { \psi } ) \cdot f _ { \psi } } \\ &  \lesssim \sqrt { \underset { j = 0 } { \overset { \sum } { \sum } } \underset { \psi \in \overline { { \mathbb { W } } } _ { j } ^ { \mathbb { S } } } { \sum } ( p _ { \psi \psi } - q _ { \psi } ) ^ { 2 } \cdot 2 ^ { - 2 \hat { \imath } \gamma } \underset { j \in \mathcal { W } _ { 1 } ^ { \mathbb { N } } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \underset { j = 0 } { \overset { \sum } { \sum } } \underset { \psi \in \overline { { \mathbb { W } } } _ { j } ^ { \mathbb { Z } } } { \sum ^ { 2 \hat { 2 } \hat { \imath } \gamma } } 2 ^ { 2 \hat { \imath } \gamma } \cdot f _ { \psi } ^ { 2 } } \\ & { \lesssim \sqrt { \underset { j = 0 } { \overset { \sum } { \sum } } \underset { \psi \in \overline { { \mathbb { W } } } _ { j } ^ { \mathbb { Z } } } { \sum ^ { - 2 \hat { \imath } \gamma } } 2 ^ { - 2 \hat { \imath } \gamma } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } = \lVert p - q \rVert _ { \mathcal { S } _ { 2 } ^ { - 2 \hat { \imath } } } . } \end{array}
$$

For the right hand side, consider

$$
f _ { \psi } = \frac { 2 ^ { - 2 j \gamma } ( p _ { \psi } - q _ { \psi } ) } { \sqrt { \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } }
$$

and $\textstyle f = \sum _ { j = 0 } ^ { \infty } f _ { \psi } \psi ( x )$ . We have

$$
\| f \| _ { \mathcal { B } _ { 2 , 2 } ^ { \gamma } } ^ { 2 } = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } 2 ^ { 2 j \gamma } \cdot f _ { \psi } ^ { 2 } = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } \frac { 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } { \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } = 1 .
$$

So we have

$$
\begin{array} { r l } { d _ { \gamma } ^ { W } ( p , q ) \gtrsim \displaystyle \int f \mathrm { d } p - \displaystyle \int f \mathrm { d } q } \\ { = \sum _ { j = 0 } ^ { \infty } \displaystyle \sum _ { \psi \in \mathbb { F } _ { q } } \left( p _ { \psi } - q _ { \psi } \right) \cdot f _ { \psi } } \\ { = \frac { \displaystyle \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } } 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } { \displaystyle \sqrt { \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } } } \\ { = \sqrt { \displaystyle \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } = \| p - q \| _ { B _ { 2 , 2 } ^ { - \gamma } } , } \end{array}
$$

# F.2 Proof of Lemma 2

For the first statement, under $\mathbb { H } _ { 0 }$ , we have

$$
\mathbb { E } ( T _ { \gamma , J } ) = \sum _ { j = 0 } ^ { J } 2 ^ { - 2 j \gamma } \sum _ { \psi \in \Psi _ { j } } \left( \mathbb { E } _ { p } [ \psi ( X ) - q _ { \psi } ] \right) ^ { 2 } = 0 ,
$$

and

$$
\begin{array} { c l } { { \displaystyle \mathrm { V a r } ( \mathcal { U } _ { \gamma , 0 } ) = ( \frac { 2 } { \sin ( \alpha - 1 ) } - \frac { 2 } { \sin ( \alpha - 1 ) } ) + \frac { 4 } { \sin ( \alpha ) } \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle \leq u ^ { - 2 } \sum _ { y = 0 , \alpha = 0 } ^ { 2 } \sum _ { \alpha ^ { 2 } = 0 ( \beta + 2 ) \setminus \alpha } \sum _ { \alpha ^ { 4 } \in \mathcal { E } _ { 1 } ^ { \prime } \in \mathcal { E } _ { 2 } ^ { \prime } } ( \mathrm { e } ( \mathcal { X } _ { 1 } ( x ) - q _ { \alpha } ) \cdot \big ( \mathrm { e } ( \mathcal { X } _ { 2 } ( x ) - q _ { \alpha } ) \big ) ^ { 2 } ) \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle \leq u ^ { - 2 } \sum _ { y = 0 , \alpha = 0 } ^ { 2 } \sum _ { \alpha ^ { 2 } = 0 ( \beta + 2 ) \setminus \alpha } \sum _ { \alpha ^ { 4 } \in \mathcal { E } _ { 1 } ^ { \prime } \in \mathcal { E } _ { 2 } ^ { \prime } } ( \mathrm { E } _ { \mathbb { P o } } [ \big ( \mathrm { b } ( x ) - q _ { \alpha } ) \cdot \big ( \mathrm { e } ( \mathcal { X } _ { 1 } ( x ) - q _ { \alpha } ) \big ) ^ { 2 } ]  } } \\ { { \displaystyle } } \\ { { \displaystyle } } \\ { { \displaystyle } } \\   \displaystyle = \alpha \geq \sum _ { \alpha ^ { 2 } = 0 , \alpha \geq 0 } ^ { 2 } \sum _ { \alpha ^ { 2 } = 0 } ^ { 2 } \mathcal { L } \mathbb { E } _ { \mathbb { P o } } ( \frac { 1 } { \alpha ^ { 2 } } ) \sum _ { \alpha ^ { 4 } \in \mathcal { E } _ { 1 } ^ { \prime } \in \mathcal { E } _ { 2 } ^ { \prime } } ( \mathrm { P o } _ { \alpha } \big [ \Theta _ { \alpha } ( x ) - \phi _ { \alpha } ( x ) \big ] - \end{array}
$$

where $( i )$ uses the same strategy as that for bounding term $( B )$ in the proof of Lemma 3. We can then get the first statement. For the second statement, by equation (19), we have

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \gtrsim d _ { \gamma } ^ { W } ( p , p _ { 0 } ) ,
$$

and

$$
\sum _ { j = J } ^ { \infty } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 \gamma j } \cdot ( p _ { \psi } - q _ { \psi } ) ^ { 2 } \lesssim n ^ { - \frac { 4 ( \alpha + \gamma ) } { 4 \alpha + d } } .
$$

Then by $d _ { \gamma } ^ { W } ( p , q ) \cdot n ^ { - \frac { 2 ( \alpha + \gamma ) } { 4 \alpha + d } } \to \infty$ , we only need to prove

$$
\frac { T _ { \gamma , J } } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } } 2 ^ { - 2 j \gamma } ( p _ { \psi } - q _ { \psi } ) ^ { 2 } } \stackrel { P } { \longrightarrow } 1 ,
$$

which directly follows from equation (20) and equation (26).

# F.3 Proof of Lemma 4

The proof is a slight adaptation of the proof of Theorem 1 of Hall (1984). We include it here for completeness. Set $\begin{array} { r } { Y _ { n i } \stackrel {  } { = } \sum _ { j = 1 } ^ { i - 1 } H ( \Breve { X _ { i } } , \boldsymbol { X _ { j } } ) } \end{array}$ . By applying Brown’s Martingale central limit theory. We only need to check two conditions

$$
s _ { n } ^ { - 2 } \sum _ { i = 2 } ^ { n } \mathbb { E } \Big \{ Y _ { n i } ^ { 2 } \mathbf { 1 } \big ( | Y _ { n i } | > \varepsilon s _ { n } \big ) \Big \}  0
$$

as $n \to \infty$ for each $\varepsilon > 0$ , where $s _ { n } ^ { 2 } = \mathbb { E } [ ( \sum _ { i \neq j } H ( X _ { i } , X _ { j } ) ) ^ { 2 } ]$ , and

$$
s _ { n } ^ { - 2 } V _ { n } ^ { 2 } \to 1
$$

as $n \to \infty$ , where

$$
V _ { n } ^ { 2 } = \sum _ { i = 2 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 2 } \mid X _ { 1 } , \cdot \cdot \cdot , X _ { i - 1 } ] .
$$

Since $H$ is symmetric and $\mathbb { E } [ H ( X _ { 1 } , X _ { 2 } ) | X _ { 1 } ] = 0$ , it has been shown in the proof of Theorem 1 of Hall (1984) that

$$
s _ { n } ^ { 2 } = { \frac { 1 } { 2 } } n ( n - 1 ) \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ,
$$

and

$$
\sum _ { i = 2 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 4 } ] \lesssim n ^ { 2 } \cdot \mathbb { E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] + n ^ { 3 } \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] ,
$$

which combines with conditions (14) and (15) can lead to $s _ { n } ^ { - 4 } \sum _ { i = 2 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 2 } ] \to 0$ that implies (33). Moreover, it’s shown in the proof of Theorem 1 of Hall (1984) that

$$
\begin{array} { r } { \mathbb { E } [ ( V _ { n } ^ { 2 } - s _ { n } ^ { 2 } ) ^ { 2 } ] \lesssim n ^ { 4 } \cdot \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] + n ^ { 3 } \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] , } \end{array}
$$

hich combines with conditions (15) and (16) leads to $s _ { n } ^ { - 4 } \mathbb { E } [ ( V _ { n } ^ { 2 } - s _ { n } ^ { 2 } ) ^ { 2 } ] \to 0$ that implies (34). Proof is completed.

# F.3.1 Proof of Lemma 6

The proof follows the proof of Theorem 1 of Hall (1984). Set

$$
\begin{array} { r } { \boldsymbol { \mathscr { s } } _ { i } = \left\{ \begin{array} { l l } { \sum _ { j = 1 } ^ { i - 1 } \left( \frac { 2 } { n ( n - 1 ) } H ( X _ { i } , X _ { j } ) + \frac { 2 } { m ( m - 1 ) } H ( Y _ { i } , Y _ { j } ) - \frac { 2 } { n m } \big ( H ( X _ { i } , Y _ { j } ) + H ( X _ { j } , Y _ { i } ) \big ) \right) } & { 2 \leq i \leq n } \\ { \sum _ { j = 1 } ^ { i - 1 } \frac { 2 } { n ( n - 1 ) } H ( X _ { i } , X _ { j } ) - \frac { 2 } { n m } \sum _ { j = 1 } ^ { m } H ( X _ { i } , Y _ { j } ) } & { m < i \leq n } \end{array} \right. . } \end{array}
$$

Set $\textstyle { \overline { { T } } } _ { \gamma , J } = \sum _ { i = 2 } ^ { n } Y _ { n i }$ . Then by the condition

$$
\frac { \frac { 2 } { n m } \sum _ { i = 1 } ^ { m } H ( X _ { i } , Y _ { i } ) } { \sqrt { \operatorname { V a r } ( T _ { \gamma , J } ) } } = o _ { p } ( 1 ) ,
$$

it remains to prove $\frac { \overline { { T } } _ { \gamma , J } } { \sqrt { \mathrm { V a r } ( \overline { { T } } _ { \gamma , J } ) } } \stackrel { d } {  } N ( 0 , 1 )$ d−→ N (0, 1). By applying Brown’s Martingale central limit theory (see for example Corollary 3.1 of Hall and Heyde (1980)). We only need to check the following two conditions:

$$
s _ { n } ^ { - 2 } \sum _ { i = 2 } ^ { n } \mathbb { E } \Big \{ Y _ { n i } ^ { 2 } \mathbf { 1 } \big ( | Y _ { n i } | > \varepsilon s _ { n } \big ) \Big \}  0
$$

as $n \to \infty$ for each $\varepsilon > 0$ , where $s _ { n } ^ { 2 } = \mathbb { E } [ ( \overline { { T } } _ { \gamma , J } ) ^ { 2 } ]$ , and

$$
s _ { n } ^ { - 2 } V _ { n } ^ { 2 } \to 1
$$

as $n \to \infty$ , where

$$
V _ { n } ^ { 2 } = \sum _ { i = 2 } ^ { m } \mathbb { E } [ Y _ { n i } ^ { 2 } \mid X _ { 1 } , \cdots , X _ { i - 1 } , Y _ { 1 } , \cdots , Y _ { i - 1 } ] + \sum _ { i = m + 1 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 2 } \mid X _ { 1 } , \cdots , X _ { i - 1 } , Y _ { 1 } , \cdots , Y _ { m } ] .
$$

Since

$$
\begin{array} { r l } {  { s _ { n } ^ { 2 } = \sum _ { i = 2 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 2 } ] } } \\ & { = \sum _ { i = 2 } ^ { m } \sum _ { j = 1 } ^ { i - 1 } \big ( \frac { 4 } { n ^ { 2 } ( n - 1 ) ^ { 2 } } + \frac { 4 } { m ^ { 2 } ( m - 1 ) ^ { 2 } } + \frac { 8 } { n ^ { 2 } m ^ { 2 } } \big ) \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } \\ & { \qquad + \sum _ { i = m + 1 } ^ { n } \big ( \sum _ { j = 1 } ^ { i - 1 } \frac { 4 } { n ^ { 2 } ( n - 1 ) ^ { 2 } } + \sum _ { j = 1 } ^ { m } \frac { 4 } { n ^ { 2 } m ^ { 2 } } \big ) \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } \\ & { = \big ( \frac { 2 } { n ( n - 1 ) } + \frac { 2 } { m ( m - 1 ) } + \frac { 4 ( m - 1 ) } { n m ^ { 2 } } \big ) \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] . } \end{array}
$$

Furthermore, since

$$
\begin{array} { r } { \mathbb { E } \big [ H ( X _ { 1 } , X _ { 2 } ) H ( X _ { 1 } , X _ { 3 } ) H ( X _ { 1 } , X _ { 4 } ) H ( X _ { 1 } , X _ { 5 } ) \big ] = \mathbb { E } \big [ H ( X _ { 1 } , X _ { 2 } ) H ^ { 3 } ( X _ { 1 } , X _ { 3 } ) \big ] = 0 , } \end{array}
$$

follow the proof of Theorem 1 of Hall (1984), we can obtain

$$
\begin{array} { r } { \mathbb { E } [ Y _ { n i } ^ { 4 } ] \lesssim n ^ { - 8 } \cdot i \cdot \mathbb { E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] + n ^ { - 8 } \cdot i ^ { 2 } \cdot \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] , } \end{array}
$$

whence

$$
s _ { n } ^ { - 4 } \sum _ { i = 2 } ^ { n } \mathbb { E } [ Y _ { n i } ^ { 4 } ] \lesssim \frac { \mathbb { E } [ H ^ { 4 } ( X _ { 1 } , X _ { 2 } ) ] } { n ^ { 2 } \cdot \big ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] \big ) ^ { 2 } } + \frac { \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] } { n \cdot \big ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] \big ) ^ { 2 } } \to 0 ,
$$

which implies condition (35). Write

$$
\begin{array} { r } { v _ { n i } = \left\{ \begin{array} { l l } { \mathbb { E } \left[ Y _ { n i } ^ { 2 } \mid X _ { 1 } , \cdots , X _ { i - 1 } , Y _ { 1 } , \cdots , Y _ { i - 1 } \right] , \quad 2 \leq i \leq m } \\ { \mathbb { E } \left[ Y _ { n i } ^ { 2 } \mid X _ { 1 } , \cdots , X _ { i - 1 } , Y _ { 1 } , \cdots , Y _ { m } \right] , \quad m + 1 \leq i \leq n . } \end{array} \right. } \end{array}
$$

Observe that when $i \leq m$

$$
\begin{array} { l } { { v _ { n i } = \displaystyle \sum _ { j = 1 } ^ { i - 1 } \sum _ { k = 1 } ^ { i - 1 } \Big [ \big ( \frac { 4 } { n ^ { 2 } ( n - 1 ) ^ { 2 } } + \frac { 4 } { n ^ { 2 } m ^ { 2 } } \big ) \cdot G ( X _ { j } , X _ { k } ) + \big ( \frac { 4 } { m ^ { 2 } ( m - 1 ) ^ { 2 } } + \frac { 4 } { n ^ { 2 } m ^ { 2 } } \big ) \cdot G ( Y _ { j } , Y _ { k } ) } } \\ { { \displaystyle \quad \quad - \big ( \frac { 4 } { n ^ { 2 } m ( n - 1 ) } + \frac { 4 } { m ^ { 2 } n ( m - 1 ) } \big ) \cdot \big ( G ( Y _ { j } , X _ { k } ) + G ( Y _ { k } , X _ { j } ) \big ) \Big ] , } } \end{array}
$$

and when $i > m$

$$
\begin{array} { r l r } {  { v _ { n i } = \sum _ { j = 1 } ^ { i - 1 } \sum _ { k = 1 } ^ { i - 1 } \frac { 4 } { n ^ { 2 } ( n - 1 ) ^ { 2 } } \cdot G ( X _ { j } , X _ { k } ) + \sum _ { j = 1 } ^ { m } \sum _ { k = 1 } ^ { m } \frac { 4 } { m ^ { 2 } ( m - 1 ) ^ { 2 } } \cdot G ( Y _ { j } , Y _ { k } ) } } \\ & { } & { \ - \sum _ { j = 1 } ^ { i - 1 } \sum _ { k = 1 } ^ { m } \frac { 8 } { n ^ { 2 } m ( n - 1 ) } + \frac { 8 } { m ^ { 2 } n ( m - 1 ) } \cdot G ( Y _ { k } , X _ { j } ) . } \end{array}
$$

Note that for $j _ { 1 } \leq k _ { 1 }$ and $j _ { 2 } \le k _ { 2 }$ ,

$$
\begin{array} { r } { \mathfrak { L } [ G ( X _ { j _ { 1 } } , X _ { k _ { 1 } } ) G ( X _ { j _ { 2 } } , X _ { k _ { 2 } } ) ] = \{ \begin{array} { c c } { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 1 } ) ] } & { j _ { 1 } = k _ { 1 } = j _ { 2 } = k _ { 2 } } \\ { ( \mathbb { E } [ G ( X _ { 1 } , X _ { 1 } ) ] ) ^ { 2 } = ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } & { j _ { 1 } = k _ { 1 } \stackrel {  } { j _ { 2 } } + j _ { 2 } = k _ { 2 } } \\ { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } & { j _ { 1 } = j _ { 2 } , k _ { 1 } = k _ { 2 } , j _ { 1 } < k _ { 2 } } \\ { 0 } & { \mathrm { o t h e r w i s e . } } \end{array}  } \end{array}
$$

We can write

$$
\begin{array} { l } { \displaystyle \mathbb { E } [ V _ { n } ^ { 4 } ] = \mathbb { E } \big [ \big ( \sum _ { i = 1 } ^ { n } v _ { n i } \big ) ^ { 2 } \big ] } \\ { \displaystyle \quad = C _ { n m 1 } \cdot \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 1 } ) ] + C _ { n m 2 } \cdot ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } + C _ { n m 3 } \cdot \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] . } \end{array}
$$

After some algebra, we can check that

$$
\begin{array} { c } { { C _ { n m 1 } \lesssim n ^ { - 5 } } } \\ { { C _ { n m 3 } \lesssim n ^ { - 4 } } } \\ { { \Big | \frac { C _ { n m 2 } } { \big ( \frac { 2 } { n ( n - 1 ) } + \frac { 2 } { m ( m - 1 ) } + \frac { 4 ( m - 1 ) } { n m ^ { 2 } } \big ) ^ { 2 } } - 1 \Big | = o ( 1 ) } } \end{array}
$$

Thus we have

$$
\begin{array} { r l } & { s _ { n } ^ { - 4 } \mathbb { E } ( V _ { n } ^ { 2 } - s _ { n } ^ { 2 } ) ^ { 2 } \Big | } \\ & { = \Big | \frac { \mathbb { E } [ V _ { n } ^ { 4 } ] } { s _ { n } ^ { 4 } } - 1 \Big | } \\ & { \lesssim \frac { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } { ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } + \frac { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 1 } ) ] } { n ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } + o ( 1 ) } \\ & { \lesssim \frac { \mathbb { E } [ G ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] } { ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } + \frac { \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) H ^ { 2 } ( X _ { 1 } , X _ { 3 } ) ] } { n ( \mathbb { E } [ H ^ { 2 } ( X _ { 1 } , X _ { 2 } ) ] ) ^ { 2 } } + o ( 1 ) } \\ & { = o ( 1 ) , } \end{array}
$$

which implies condition (36). Proof is completed.