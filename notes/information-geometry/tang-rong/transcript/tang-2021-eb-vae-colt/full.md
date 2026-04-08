# Minimax Rate of Distribution Estimation on Unknown Submanifold under Adversarial Losses

Rong Tang and Yun Yang

University of Illinois Urbana-Champaign

# Abstract

Statistical inference from high-dimensional data with low-dimensional structures has recently attracted lots of attention. In machine learning, deep generative modeling approaches implicitly estimate distributions of complex objects by creating new samples from the underlying distribution, and have achieved great success in generating synthetic realistic-looking images and texts. A key step in these approaches is the extraction of latent features or representations (encoding) that can be used for accurately reconstructing the original data (decoding). In other words, low-dimensional manifold structure is implicitly assumed and utilized in the distribution modeling and estimation. To understand the benefit of low-dimensional manifold structure in generative modeling, we build a general minimax framework for distribution estimation on unknown submanifold under adversarial losses, with suitable smoothness assumptions on the target distribution and the manifold. The established minimax rate elucidates how various problem characteristics, including intrinsic dimensionality of the data and smoothness levels of the target distribution and the manifold, affect the fundamental limit of high-dimensional distribution estimation. To prove the minimax upper bound, we construct an estimator based on a mixture of locally fitted generative models, which is motivated by the partition of unity technique from differential geometry and is necessary to cover cases where the underlying data manifold does not admit a global parametrization. We also propose a data-driven adaptive estimator that is shown to simultaneously attain within a logarithmic factor of the optimal rate over a large collection of distribution classes.

Keywords: adversarial training, generative model, distribution estimation, manifold, minimax rate, partition of unity.

# 1 Introduction

High-dimensional statistical models arise in various areas of science, including computer vision, astrophysics, social science, genetics, and computational biology, among others. In order to make the accompanied “large $D$ , small $n ^ { \prime \prime }$ inference problem solvable, or, in other words, guarantee the existence of a consistent estimator, some low-dimensional structural assumptions need to be imposed. Here $D$ refers to the ambient dimension of the problem and $n$ refers to the sample size. Sparsity, one common low-dimensional structure, assumes that only a small number $s$ ( $\ll n$ ) of dimensions contributes to the model, whereas the subset corresponds to these active dimensions is unknown. Popular sparsity motivated statistical methods, such as LASSO [Tibshirani, 1996], SCAD [Fan and Li, 2001] and MCP [Zhang, 2010], have received impressive success in various prediction related tasks in many applications. In other applications, all variables may collectively influence the model, but the variables themselves may exhibit some low-dimensional structure, such as lying on an unknown submanifold whose intrinsic dimension $d$ is much smaller than the ambient dimension $D$ , thus avoids the “curse of dimensionality”. For example, a manifold structure is naturally assumed and utilized in computer vision problems [Lui, 2012] such as face recognition, action recognition and visual tracking. Despite the high-dimensional appearance of the object image data represented as a matrix collecting all pixels levels, the vectorized pixel matrix usually lies on a low-dimensional manifold parameterized by global characteristics such as camera projection, lighting condition, texture, object position and orientation. In bioinformatics, protein-protein interaction networks are often assumed to lie on or near some low-dimensional manifold embedded in the high-dimensional unorganized observation space [You et al., 2010], since proteins interact with other proteins based on a limited number of biochemical and structural properties [Terradot et al., 2004].

In this paper, we consider the statistical problem of distribution estimation on an unknown sub-manifold embedded in an ambient Euclidean space, where the target distribution $\mu$ is implicitly defined through a (mixture of) generative model. In the machine learning literature, generative models, such as Generative Adversarial Network (GAN, Goodfellow et al. [2014], Li et al. [2015], Biau et al. [2020]), Wasserstein GAN (WGAN, Arjovsky et al. [2017]) and Wasserstein Auto-Encoder (WAE, Tolstikhin et al. [2019], Zhao et al. [2018]), have received great success in generating synthetic realisticlooking images and texts [Brock et al., 2018, van den Oord et al., 2016], which is an implicit manner of distribution estimation over complex data space. The success of these unsupervised machine learning methods for complex distribution estimation can be largely attributed to two key factors. First, these methods apply deep neural networks for extracting latent features or representations (i.e. encoding) that can be used for accurately reconstructing the original data (i.e. decoding). In other words, low-dimensional manifold structures are implicitly utilized in the distribution estimation via encoder-decoder pairs. The superior performance of these methods over classical fully nonparametric methods again reinforces the fact that complex objects such as images and texts, despite their highdimensional appearance, are low-dimensional in nature — they lie on some sub-manifold embedded in the original data space. Second, these methods are different from classical distribution estimation approach that aims at forming a parametric or nonparametric estimate of the probability density function at a point or the probability of a set; instead they fit a generative model that specifies a stochastic process whose simulated data look indistinguishable to real data. Methodology-wise, this generative modeling framework for distribution estimation automatically promotes low-dimensional data representation without explicitly estimating the unknown data manifold. Computation-wise, a best generative model can be naturally fitted by minimizing certain discrepancy measure between the real data and the synthetic data generated from the model. Moreover, sampling is often more useful and important than explicit distribution estimation in practical applications, as a known distribution (up to normalizing constant) may still require substantial effort to sample from (for example, sampling from Bayesian posteriors). A formal definition of a generative model is described in Section 2.2, where further details about comparisons with traditional explicit distribution estimation approaches are also discussed.

Despite the recent surge of works (see Section 1.1 for a selective review) on generative model learning, there is a lack of theoretical results quantifying the fundamental limit of these procedure to estimate a distribution supporting on an unknown manifold lying on a high-dimensional ambient Euclidean space and how various problem characteristics affect the limit. In this paper, we aim to close this gap by identifying the minimax rate of distribution estimation on unknown submanifold under adversarial losses. Here, an adversarial loss [Arjovsky et al., 2017, Singh et al., 2018, Tolstikhin et al., 2019, Liang, 2020] is defined as $\begin{array} { r } { d _ { \mathcal { F } } ( \mu _ { 1 } , \mu _ { 2 } ) = \operatorname* { s u p } _ { f \in \mathcal { F } } \vert \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu _ { 1 } - \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu _ { 2 } \vert } \end{array}$ , for two distributions $\mu _ { 1 }$ and $\mu _ { 2 }$ over data space $\mathcal { X }$ , where $\mathcal { F }$ is pre-specified set, called the discriminator class, composed of functions over $\mathcal { X }$ (c.f. Section 2.3 for further details). Popular choices of $\mathcal { F }$ includes Lipschitz continuous function class (WGAN, Arjovsky et al. [2017]), Sobolev function class (Sobolev GAN, Mroueh et al. [2017]) and reproducing kernel Hilbert space (MMD GAN, Li et al. [2017]). Note that conventional discrepancy measures such as $\ell _ { p }$ ( $p \geq 1$ ) distance, Hellinger distance and Kullback-Leibler (KL) divergence that are widely adopted in nonparametric density estimation theory [Tsybakov, 2009] are no longer applicable to define the risk in our context since the (implicitly) estimated distribution is not absolutely continuous with respect to the Lebesgue measure of the ambient data space $\mathcal { X }$ and may be singular to the estimation target, denoted as $\mu ^ { * }$ .

One distinct feature of our framework from the generative modeling literature in machine learning is that we do not require the unknown data manifold to admit a global parametrization (single chart). For example, for compact manifolds without boundary, such as the sphere, at least two parametrizations are needed in order to cover the whole surface. We avoid this stringent assumption, often implicitly assumed in existing methods, by the technique of partition of unity (c.f. Section 2.4 for details). Specifically, we show that the minimax rate under adversarial loss $d _ { \mathcal { F } }$ , whose discriminator class $\mathcal { F }$ has $\gamma \in ( 0 , \infty )$ smoothness level, scales with sample size $n$ as $^ 1 n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \beta \gamma } { d } }$ modulo logarithm terms, where $\beta \in ( 1 , \infty )$ is the smoothness of the manifold, $\alpha \in [ 0 , \beta - 1 ]$ the smoothness of the probability density function relative to the volume measure of the manifold, and recall that $d$ is the intrinsic dimension of the manifold. In the rate, the term $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } }$ is attributed to the risk of estimating an unknown $\alpha$ -smooth density when the $d$ -dimensional $\beta$ -smooth manifold is known under the same adversarial loss, and the term $n ^ { - \frac { \beta \gamma } { d } }$ to risk of estimating an unknown $\beta$ -smooth manifold. Note that when $\gamma = 1$ , the $n ^ { - \frac { \beta } { d } }$ term matches the minimax rate of estimating a $\beta$ -smooth manifold under the Hausdorff loss [Aamari and Levrard, 2019].

# 1.1 Related work

Generative model learning: In the machine learning literature, a generative modeling procedure aims to find a distribution $\mu$ in the generator class $\mathcal { D } _ { G }$ (c.f. Section 2.2 for a precise definition) that is closest to the target distribution $\mu ^ { * }$ over the data space $\mathbb { R } ^ { D }$ with respect to an adversarial loss defined by a discriminator class $\mathcal { F }$ composed of test functions (c.f. Section 2.3 for a precise definition), that is, solve the minimax optimization problem

$$
\operatorname* { i n f } _ { \mu \in { \mathcal { D } } _ { G } } d _ { { \mathcal { F } } } ( \mu , \mu ^ { * } ) = \operatorname* { i n f } _ { \mu \in { \mathcal { D } } _ { G } } \operatorname* { s u p } _ { f \in { \mathcal { F } } } \Big | \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu - \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu ^ { * } \Big | .
$$

In practice, we only have access to a finite number $n$ of i.i.d. samples $X _ { 1 : n } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ from $\mu ^ { * }$ . To estimate $\mu ^ { * }$ from $X _ { 1 : n }$ based on (1), we need a finite sample surrogate $\mathcal { I } ( f ; X _ { 1 : n } )$ (as a functional from $\mathcal { F }$ to $\mathbb { R }$ ) to approximate $\boldsymbol { \int f } ( \boldsymbol { x } ) \mathrm { d } \mu ^ { * }$ for any $f \in { \mathcal { F } }$ . In the generative adversarial network literature [Goodfellow et al., 2014, Li et al., 2015, Biau et al., 2020, Arjovsky et al., 2017, Tolstikhin et al., 2019, Zhao et al., 2018], $\mathcal { I } ( f ; X _ { 1 : n } )$ is often simply chosen as the empirical average $n ^ { - 1 } \sum _ { i = 1 } ^ { n } f ( X _ { i } )$ . Although the empirical average is easy to compute, it leads to statistical inefficiency in estimating the solution to problem (1) due to the failure of taking the smoothness of target distribution $\mu ^ { * }$ and test function $f$ into consideration. Liang [2020] and Singh et al. [2018] show that when $\mu ^ { * }$ admits an $\alpha$ -smooth density function relative to the Lebesgue measure on $[ 0 , 1 ] ^ { D }$ , test functions in the discriminator class are $\gamma$ -smooth, and $\mu ^ { * }$ belongs to the generator class $\mathcal { D } _ { G }$ (model correctly specified), then solving an empirical version of the minimax problem (1) with $\textstyle \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu ^ { * }$ being replaced by $\begin{array} { r } { \mathcal { I } ( f ; X _ { 1 : n } ) = \int f \mathrm { d } \widetilde { \mu } _ { n } } \end{array}$ , where ${ \widetilde { \mu } } _ { n }$ is a regularized estimator defined through kernel smoothning, leads to a better estimator of $\mu ^ { * }$ than simply replacing $\textstyle \int _ { \mathcal { X } } f ( x ) \mathrm { d } \mu ^ { * }$ with its empirical average. Furthermore, the resulting estimator attains the minimax optimal rate $n ^ { - \frac { \alpha + \gamma } { 2 \alpha + D } } \vee n ^ { - \frac { 1 } { 2 } }$ of learning an $\alpha$ -smooth density function on $[ 0 , 1 ] ^ { D }$ under the same adversarial loss $d _ { \mathcal { F } }$ . The non-parametric rate $n ^ { - \frac { \alpha + \gamma } { 2 \alpha + D } }$ may suffer from the curse of dimensionality as the ambient space dimension $D$ can be enormous in machine learning applications involving images and texts, for which their methods do not adapt to the underlying low-dimensional manifold structure.

Distribution estimation on manifold: Some literature [Ozakin and Gray, 2009, Berenfeld and Hoffmann, 2021] considers the problem of probability density estimation on an unknown manifold $\mathcal { M } ^ { * }$ , where the density function is defined as the Radon–Nikodym derivative of the underlying data distribution relative to the volume measure of the manifold. For example, Ozakin and Gray [2009] proposes a simple modification of the classical kernel density estimator (KDE) in the ambient space $\mathbb { R } ^ { D }$ for obtaining pointwise estimation of the density function on $\mathcal { M } ^ { * }$ . The authors show that with an optimal choice of the bandwidth parameter, the pointwise mean squared error of the resulting estimator only depends on the intrinsic dimension $d$ instead of the ambient dimension $\boldsymbol { D }$ . Berenfeld and Hoffmann [2021] investigates several non-parametric kernel methods with data-driven bandwidths that are adaptive to the unknown manifold structure. They show that, when the target density function is $\alpha$ -smooth and manifold $\mathcal { M } ^ { * }$ is $\beta$ -smooth (c.f. Section 2.4 for a precise definition), their estimator achieves an $n ^ { - \frac { \alpha \wedge ( \beta - 1 ) } { 2 ( \alpha \wedge ( \beta - 1 ) ) + d } }$ error bound under the maximal pointwise $\ell _ { p }$ loss over the manifold. They also illustrates that their procedure is asymptotically minimax optimal when $\beta \ge \alpha + 1$ . Unfortunately, the KDE procedures developed in Ozakin and Gray [2009] and Berenfeld and Hoffmann [2021] only recover density values at points lying on the unknown manifold $\mathcal { M } ^ { * }$ . Without the knowledge of the support of the manifold, their estimator can not be used to generate (approximate) samples from $\mathcal { M } ^ { * }$ , which limits their practical applicability. Along a different line, Genovese et al. [2012b] and Aamari and Levrard [2019] consider the problem of manifold estimation which corresponds to support estimation of $P$ . Genovese et al. [2012b] shows that under the strong assumption that observations are subject to perpendicular noises to the manifold, the minimax rate relative to the Hausdorff distance of estimating a boundaryless manifold is $n ^ { - \frac { 2 } { d + 2 } }$ . Aamari and Levrard [2019] shows that in the noise-free setting, the minimax rate of estimating a boundaryless $\beta$ -smooth( $\beta \geq 2$ ) manifold relative to the Hausdorff distance is $n ^ { - \frac { \beta } { d } }$ . However, the estimator constructed in these papers is an unstructured union of $d$ -dimensional balls in $\mathbb { R } ^ { D }$ . Consequently, their estimator does not recover the topology of $\mathcal { M } ^ { * }$ as the estimator based on generative model learning.

# 1.2 Organization

The rest of the paper is organized as follows. In Section 2, we review some important concepts, such as generative models, adversarial loss and Riemannian manifold, and setup the problem. In Section 3, we introduce our main result on the minimax rate, describe a construction of rate-optimal estimator based on a mixture of generative models, and propose a data-driven adaptive estimator. Roadmap for the proof of our main result is provided in Section 4. In Appendix A, we provide a brief review of Wavelets and Besov function space that are used in our estimator construction and analysis. In Appendix B, we describe a larger class of distributions explicitly defined via (mixture of) generative models, for which the same minimax rate applies. Some extensions of our results, including applications in two-sample tests and local distribution estimation constrained on compact sets are discussed in Appendix C. All technical results and proofs are collected in Appendices D, E and F.

# 2 Background and Problem Formulation

In this section, we begin with notation and a brief introduction to generative models. The advantages of using adversarial losses for error quantification in manifold distribution estimation over conventional discrepancy measures such as the total variation distance or KL divergence are then discussed. After that, we review the concept of partition of unity for the manifold, and give a specific construction of partition of unity for submanifolds embedded in ambient Euclidean spaces. We then formally setup the problem of distribution estimation on submanifold under adversarial losses.

# 2.1 Notation

We use ${ \bf 1 } _ { A }$ to denote the indicator function of a set $A$ so that $\mathbf { 1 } _ { A } ( x ) = 1$ if $x \in A$ and zero otherwise. For any positive integer $m$ , we use the shorthand $[ m ] : = \{ 1 , \cdots , m \}$ . For $\alpha \in \mathbb { R }$ , the floor and ceiling functions are denoted by $\lfloor \alpha \rfloor$ and $\lceil \alpha \rceil$ , indicating rounding $\alpha$ to the next smaller and larger integer. For two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ to mean $a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n$ . In addition, $a _ { n } \asymp b _ { n }$ means that both $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ hold. For a probability measure $\mu$ , the support $\operatorname { s u p p } ( \mu )$ of $\mu$ is defined as the complement of the largest open set on which $\mu$ vanishes. For a probability measure $\mu$ and a measurable set $\Omega$ , we use $\mu | _ { \Omega }$ to denote the restriction of $\mu$ on $\Omega$ . For two probability measures $\mu$ and $\nu$ where $\mu$ is absolutely continuous with respect to $\nu$ , we use $\frac { \mathrm { d } \mu } { \mathrm { d } \nu }$ to denote the Radon-Nikodym derivative of $\mu$ with respect to $\nu$ , and $\begin{array} { r } { D _ { \mathrm { K L } } ( \mu \vert \vert \nu ) = \int \log ( \frac { \mathrm { d } \mu } { \mathrm { d } \nu } ) \mathrm { d } \mu } \end{array}$ the KL divergence between them. We use ${ \mathcal { P } } ( \mathbb { R } ^ { d } )$ to denote the set of probability measures on $\mathbb { R } ^ { d }$ . When no ambiguity arises, for an absolutely continuous probability measure $\nu$ , we may also use $\nu$ to refer its density function.

We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and reserve $\| \cdot \|$ for the $\ell _ { 2 }$ norm (that is, suppress the subscript when $p = 2$ ). For a vector $x = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { D } )$ we use $x _ { i : j } = ( x _ { i } , x _ { i + 1 } , · · · , x _ { j } )$ to denote the vector composed of the $i$ to $j$ elements of $x$ . We use $\mathbf { 0 } _ { d }$ to denote the $d$ -dimensional all zero vector, and $\mathbb { B } _ { r } ( x )$ the closed ball centered at $x$ with radius $r$ (under the $\ell _ { 2 }$ distance) in the Euclidean space; in particular, we use $\mathbb { B } _ { r } ^ { d }$ to denote $\mathbb { B } _ { r } ( \mathbf { 0 } _ { d } )$ when no ambiguity may arise. For a measurable set $S$ , we use $S ^ { \circ }$ to denote the interior of $S$ and $\partial \cal S$ to denote the $^ 2$ boundary of $S$ . For a vector-valued function in several variables $f : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , we use $f _ { i }$ with $i \in \left\lfloor D \right\rfloor$ to denotes its $i$ th component and $\mathbf { J } _ { f } ( x )$ to denote the $D \times d$ Jacobian matrix of $f$ evaluated at point $x$ . For a scalar-valued multivariate function $f : \mathbb { R } ^ { d }  \mathbb { R }$ , we use $\operatorname { s u p p } ( f )$ to denote its support, defined as supp(f ) = {x ∈ Rd | f (x) > 0}, and kf kL = supx,y∈Rd, x6=y kx−yk2 |f(x)−f(y)| its Lipschitz constant (if the supreme is finite). For a measurable set $\Omega \subset \mathbb { R } ^ { d }$ , we use $f | _ { \Omega }$ to denote restriction of $f$ on $\Omega$ . For a multi-index $a = ( a _ { 1 } , \cdots , a _ { d } ) \in \mathbb { N } _ { 0 } ^ { d } = \{ ( a _ { 1 } , \cdots , a _ { d } ) | \forall j \in [ d ]$ , $a _ { j } \in  { \mathbb { N } } _ { 0 } \}$ , we define $\begin{array} { r } { | a | = \sum _ { k = 1 } ^ { d } a _ { j } } \end{array}$ and $\begin{array} { r } { a ! = \prod _ { i = 1 } ^ { d } a _ { i } ! } \end{array}$ . For two vectors $x , y \in \mathbb { R } ^ { d }$ , we use $( x - y ) ^ { a }$ to denote $\textstyle \prod _ { i = 1 } ^ { d } ( x _ { i } - y _ { i } ) ^ { a _ { i } }$ . For a function $f :  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$ , we use $f ^ { ( a ) }$ to denote its mixed partial derivative $\partial ^ { | a | } f / \partial x _ { 1 } ^ { a _ { 1 } } \cdot \cdot \cdot \partial x _ { d } ^ { a _ { d } }$ . We define the $\alpha$ -smooth Hölder (function) class (see e.g., Evans [2010]) with radius $r > 0$ over $\Omega$ as $C _ { r } ^ { \alpha } ( \Omega ) : = \{ f : \Omega \to \mathbb { R } | \| f \| _ { C ^ { \alpha } ( \Omega ) } =$ P|a|≤b $\begin{array} { r } { _ { x ] } \operatorname* { m a x } _ { x \in \Omega } \left| f ^ { ( a ) } ( x ) \right| + \sum _ { | a | = | \alpha | } \operatorname* { m a x } _ { x , y \in \Omega , x \neq y } \left| f ^ { ( a ) } ( x ) - f ^ { ( a ) } ( y ) \right| / \| x - y \| ^ { \alpha - | \alpha | } \leq r \} } \end{array}$ Similarly, we use $C _ { r } ^ { \alpha } ( \Omega ; \mathbb { R } ^ { D } ) = \left\{ f = ( f _ { 1 } , \ldots , f _ { D } ) : \Omega \to \mathbb { R } ^ { D } \big | \forall j \in [ D ] , \right. .$ $f _ { j } \in C _ { r } ^ { \alpha } ( \Omega ) \}$ to denote the vector valued function space counterpart. For an $f \in C _ { r } ^ { \alpha } ( \Omega ; \mathbb { R } ^ { D } )$ and a multi-index $a \in  { \mathbb { N } } _ { 0 } ^ { d }$ , we denote $f ^ { ( a ) }$ as the $\boldsymbol { D }$ dimensional vector whose $j$ -th component is the mixed partial derivative $[ f _ { j } ] ^ { ( a ) }$ of $f _ { j }$ for $j \in [ D ]$ .

# 2.2 Generative models

Mathematically, we define a generative model as a pair $( \nu , G )$ , where $\nu$ is a distribution on a low-dimensional latent space $\mathcal { Z } \subset \mathbb { R } ^ { d }$ , called generative distribution, that is easy to sample from; and $G : { \mathcal { Z } } \to \mathbb { R } ^ { D }$ is a map from $\mathcal { Z }$ to the data space $\mathbb { R } ^ { D }$ , called generative $m a p$ , so that if $Z \sim \nu$ , then $G ( Z ) \sim \mu$ . In order words, the target distribution $\mu$ can be expressed via the generative model $( \nu , G )$ via $\mu = G _ { \# } \nu$ , the 3pushforward measure of $\mu$ using map $G$ . The set ${ \mathcal { D } } _ { G } = \{ G _ { \# } \nu : \nu \in \Upsilon , G \in { \mathcal { G } } \}$ of all generative models $( \nu , G )$ with $\nu \in \Upsilon$ and $G \in { \mathcal { G } }$ for some distribution family $\Upsilon$ on $\mathcal { Z }$ and function class $\mathcal { G }$ (consists of maps from $\mathcal { Z }$ to $\mathbb { R } ^ { D }$ ) is called a generator class. In practice, $\Upsilon$ can be chosen to contain a single and simple distribution such as the standard Gaussian or uniform distribution, so that sampling from any generative model in $\mathcal { D } _ { G }$ is efficient and easy.

Defining an intrinsically low-dimensional distribution on a high-dimensional ambient space implicitly through a generative model enjoys multiple benefits. First, such a distribution is otherwise difficult to describe: on the one hand, it cannot be defined as usual through a density function as the distribution only admits a density function relative to the volume measure of the manifold, but not to the Lebesgue measure of the ambient space; on the other hand, the 4support of the distribution (i.e. the underlying manifold) is unknown, which further complicates the characterization. In comparison, a generative model captures the intrinsic low-dimensional structure of the distribution via transforming from a latent space $\mathcal { Z }$ , while the support of the distribution corresponds to the range of map $G$ . Consequently, a generative model learning procedure naturally decouples the distribution estimation problem into manifold learning (estimation of $G$ ) plus density estimation on the manifold (estimation of $\nu$ ). Second, in many applications generating samples from an underlying distribution is more important and useful than estimating the distribution. Moreover, summaries or functionals of a distribution can be easily calculated from sampling via Monte Carlo methods; while sampling can be extremely difficult even with the full knowledge of the distribution (for example, sampling from Bayesian posteriors). Third, map $G$ in the generative model can capture highly nonlinear structures that may lead to singularities (such as jumps and point mass) in the distribution and are hard to characterize via a density or distribution function. Last but not least, representing a distribution through a generative model has the computational benefit of facilitating efficient implementation, as functions tend to be easier to handle in optimization than distributions with constraints. In addition, generative models have the natural adversarial tranining framework of minimizing certain discrepancy measure between the empirical distributions of the real data and the generated synthetic data [Goodfellow et al., 2014].

# 2.3 Adversarial loss

Conventional discrepancy measures based on Radon–Nikodym derivatives relative to the Lebesgue measure are not suitable for characterizing the closeness between mutually singular probability measures on data space $\mathcal { X } = \mathbb { R } ^ { D }$ . For distributions with different supports, one commonly used class of discrepancy measures in the machine learning literature are adversarial losses, which are also known as integral probability metrics [Müller, 1997] in the probability literature. For a discriminator class $\mathcal { F }$ of of bounded and Borelmeasurable functions, the adversarial loss between probability measures $\mu$ and $\nu$ is defined as

$$
d _ { \mathcal { F } } ( \mu , \nu ) = \operatorname* { s u p } _ { f \in \mathcal { F } } \Big | \int _ { \mathbb { R } ^ { D } } f ( x ) \mathrm { d } \mu - \int _ { \mathbb { R } ^ { D } } f ( x ) \mathrm { d } \nu \Big | .
$$

If the discriminator class satisfies ${ \mathcal { F } } = - { \mathcal { F } }$ , then taking the absolute value inside the supreme of (2) is not necessary. Many common probability metrics can be realized as an adversarial loss. For example, the Wasserstein-1 metric corresponds to the choice of F = {all 1-Lipchitz functions}; the total variation metric corresponds to $\mathcal { F } = \{ \mathrm { a l l }$ measurable functions bounded by $1 \}$ ; and the maximum mean discrepancy (MMD, Gretton et al. [2012], Tolstikhin et al. [2017]) metric corresponds to $\mathcal { F }$ as the unit ball of a reproducing kernel Hilbert space.

Adversarial losses with suitable $\mathcal { F }$ are often adopted in formulating machine learning methods (e.g. WGAN and WAE) as $d _ { \mathcal { F } }$ can be numerically approximated by feeding empirical samples from $\mu$ and $\nu$ into a discriminator neural network. This computational ease is particularly beneficial for problems involving distributions that are implicitly defined through generative models where samples are relatively cheap to obtain. Theoretical-wise, since many distributional characteristics can be defined as an integral of some function $f$ with respect to the underlying probability measure, probability metrics based on the comparison of integrals are natural candidates for the discrepancy measure in finite-sample error analysis.

In this work, we focus on the following adversarial loss, whose discriminator class $\mathcal { F }$ is $C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , the unit ball of the $\gamma$ -smooth Hölder class with $\gamma > 0$ ,

$$
d _ { \gamma } ( \mu , \nu ) = \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big ( \int _ { \mathbb { R } ^ { D } } f ( x ) \mathrm { d } \mu - \int _ { \mathbb { R } ^ { D } } f ( x ) \mathrm { d } \nu \Big ) .
$$

Note that $d _ { \gamma }$ satisfies the triangle inequality and by the Weierstrass approximation theorem [Stone, 1948], $d _ { \gamma } ( \mu , \nu ) = 0$ if and only if $\mu = \nu$ . Consequently, $d _ { \gamma }$ is a valid metric over all probability measures on $\mathbb { R } ^ { D }$ . When restricted to distributions over a bounded set such as ball $\mathbb { B } _ { r } ^ { D }$ with radius $r$ , metric $d _ { \gamma }$ with $\gamma = 1$ is equivalent to the Wasserstein-1 metric. Moreover, metric $d _ { \gamma }$ becomes stronger as $\gamma$ decreases, and approaches the total variation metric $d _ { \mathrm { T V } }$ as $\gamma  0 _ { + }$ .

Deployed as the discrepancy measure for distribution estimation on unknown submanifolds, the smoothness parameter $\gamma$ in $d _ { \gamma }$ characterizes a trade-off between supporting manifold recovery and density estimation on the manifold. A smaller $\gamma$ makes $d _ { \gamma } ( \mu , \nu )$ more sensitive to the misalignment between the supports of $\mu$ and $\nu$ . To see this, define $\begin{array} { r } { \mathrm { { d i s t } } ( x , A ) = \operatorname* { i n f } _ { y \in A } \| x - y \| _ { 2 } } \end{array}$ as the distance from a point $x \in \mathbb { R } ^ { d }$ to a set $A \subset \mathbb { R } ^ { D }$ . Note that $\mathrm { d i s t } ( \cdot , A ) ^ { \gamma }$ belongs to $C ^ { \gamma } ( \mathbb { R } ^ { D } )$ for any $\gamma > 0$ . For two distributions $\mu$ and $\nu$ with bounded supports, we may take $f ( x ) = c \mathrm { d i s t } ( x , \mathrm { s u p p } ( \nu ) ) ^ { \gamma } - c \mathrm { d i s t } ( x , \mathrm { s u p p } ( \mu ) ) ^ { \gamma }$ for some sufficiently small constant $c$ such that $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , leading to

$$
\begin{array} { r } { d _ { \gamma } ^ { \mathtt { S } } ( \mu , \nu ) : = \mathbb { E } _ { \mu } \big [ \mathrm { d i s t } ( X , \operatorname { s u p p } ( \nu ) ) ^ { \gamma } \big ] + \mathbb { E } _ { \nu } \big [ \mathrm { d i s t } ( X , \operatorname { s u p p } ( \mu ) ) ^ { \gamma } \big ] \leq c ^ { - 1 } d _ { \gamma } ( \mu , \nu ) . } \end{array}
$$

Consequently, an upper bound of $d _ { \gamma }$ implies an error bound on the supporting manifold recovery through discrepancy measure $d _ { \gamma } ^ { \mathrm { s } }$ . As $\gamma$ tends to zero, $d _ { \gamma } ^ { \mathrm { S } } ( \mu , \nu )$ approaches $\mathbb { P } _ { \mu } \bigl ( X \ \notin \ \operatorname { s u p p } ( \nu ) \bigr ) + \mathbb { P } _ { \nu } \bigl ( X \ \notin \ \operatorname { s u p p } ( \mu ) \bigr )$ , which vanishes only if $\mu$ and $\nu$ have perfectly aligned supports. When $\gamma = 1$ , $\begin{array} { r } { \frac { 1 } { 2 } d _ { \gamma } ^ { \mathrm { S } } } \end{array}$ can be viewed as the limiting average Hausdorff

distance [Aydin et al., 2021],

$$
d _ { \Lambda \mathrm { H } } \big ( \{ Y _ { i } \} _ { i = 1 } ^ { m } , \ \{ Y _ { i } ^ { \prime } \} _ { i = 1 } ^ { m } \big ) = \frac { 1 } { 2 m } \sum _ { i = 1 } ^ { m } \operatorname* { m i n } _ { j \in [ m ] } \| Y _ { i } - Y _ { j } ^ { \prime } \| _ { 2 } + \frac { 1 } { 2 m } \sum _ { i = 1 } ^ { m } \operatorname* { m i n } _ { j \in [ m ] } \| Y _ { i } ^ { \prime } - Y _ { j } \| _ { 2 } ,
$$

as sample size $m$ tends to infinity, where $\{ Y _ { i } \} _ { i = 1 } ^ { m }$ and $\{ Y _ { i } ^ { \prime } \} _ { i = 1 } ^ { m }$ are i.i.d. samples from $\mu$ and $\nu$ , respectively.

# 2.4 Smooth submanifolds and partition of unity

Intuitively speaking, a manifold is a topological space that locally resembles the Euclidean space. A submanifold in the ambient space $\mathbb { R } ^ { D }$ can be viewed as a nonlinear “subspace”. Formally, a $\beta$ -smooth ( $\beta \geq 1$ ) $d$ -dimensional manifold $\mathcal { M }$ is defined as a topological space satisfying:

1. There exists an atlas on $\mathcal { M }$ consisting of a collection of $d$ -dimensional charts $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ covering $\mathcal { M }$ , that is, $\begin{array} { r } { \mathcal { M } = \bigcup _ { \lambda \in \Lambda } U _ { \lambda } } \end{array}$ .   
2. Each chart $^ { 5 } ( U , \varphi )$ in atlas $\mathcal { A }$ consists of a homeomorphism $\varphi : U \to { \widetilde { U } }$ , called coordinate map, from an open set $U \subset \mathcal { M }$ to an open set $\widetilde { U } \subset \mathbb { R } ^ { d }$ , that is, $\varphi$ is bijective and both $\varphi$ and $\varphi ^ { - 1 }$ are continuous maps.   
3. Any two charts $( U , \varphi )$ and $( V , \psi )$ in atlas $\mathcal { A }$ are compatible, meaning that the transition map $\varphi \circ \psi ^ { - 1 } : \psi ( U \cap V ) \to \varphi ( U \cap V )$ is an $\beta$ -smooth diffeomorphism.

The manifold structure is an intrinsic property that does not rely on the choice of the atlas. For a submanifold embedded in $\mathbb { R } ^ { D }$ , the second and third conditions can be combined into a single condition that the coordinate map $\varphi$ in each chart is a $\beta$ -smooth map when identified as a vector-valued function from subset $U$ of $\mathbb { R } ^ { D }$ to subset $\widetilde { U }$ of $\mathbb { R } ^ { d }$ . The $\alpha$ -smooth Hölder (function) class $C ^ { \alpha } ( { \mathcal { M } } )$ for $\alpha \in ( 0 , \beta ]$ over a $\beta$ -smooth manifold $\mathcal { M }$ consists of all functions $f : \mathcal { M }  \mathbb { R }$ whose localization $f \circ \varphi ^ { - 1 } : \varphi ( U ) \to \mathbb { R }$ to each local chart $( U , \varphi )$ is $\alpha$ -Hölder smooth in the usual Euclidean sense. From this definition, the coordinate map $\varphi$ in each chart $( U , \phi )$ belongs to $C ^ { \beta } ( U )$ by identifying $U$ as an embedded submanifold of $\mathcal { M }$ inheriting the same differentiable structure. Note that here for a $\beta$ -smooth submanifold, it is not meaningful to talk about functions with smoothness level $\alpha$ beyond $\beta$ since the definition of a higher-order smoothness level may not be compatible between charts if the atlas is at most $\beta$ -smooth.

Most generative model based distribution estimation procedures in the literature (e.g. Arjovsky et al. [2017], Mroueh et al. [2017], Li et al. [2017]) uses a single generative model $( \nu , G )$ in modeling the underlying data distribution. This implicitly requires the underlying submanifold $\mathcal { M }$ that supports the target distribution $\mu = G _ { \# } \nu$ to admit a global parametrization, or a single chart description. However, many commonly encountered manifolds such as spheres cannot be covered by a single chart in any of its representing atlas. One technical advance of the current paper is to allow multiple charts in the underlying data manifold representation through the mathematical technique of partition of unity as defined below.

Definition 1. A partition of unity on a $\beta$ -smooth manifold $\mathcal { M }$ is a collection of $\beta$ -smooth functions $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ on $\mathcal { M }$ so that

1. $0 \le \rho _ { \lambda } \le 1$ for all $\lambda \in \Lambda$ , and $\begin{array} { r } { \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( x ) = 1 } \end{array}$ for all $x \in \mathcal { M }$ .

2. Each point $x \in \mathcal { M }$ has a neighborhood which intersects $\operatorname { s u p p } ( \rho _ { \lambda } )$ for only finitely many $\lambda \in \Lambda$ .

Using the partition of unity, one can glue constructions in the local charts to form a global construction on the manifold. Such a global construction usually does not rely on the choice of the partition of unity. Conversely, the partition of unity enables the decomposition of a global estimation problem into local ones, which resembles the data localization in local (polynomial) regression [Loader, 2006, Bickel and Li, 2007]. A partition of unity can be constructed from any open cover $\{ U _ { \lambda } \} _ { \lambda \in \Lambda }$ of the manifold in a way where the partition $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ is indexed over the same set and $\operatorname { s u p p } ( \rho _ { \lambda } ) \subset U _ { \lambda }$ for any $\lambda \in \Lambda$ . Such a partition of unity is said to be subordinate to the open cover $\{ U _ { \lambda } \} _ { \lambda \in \Lambda }$ . When no ambiguity may arise, we also say that a partition of unity is subordinate to an atlas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ if it is subordinate to its incurred open cover $\{ U _ { \lambda } \} _ { \lambda \in \Lambda }$ . For a submanifold of $\mathbb { R } ^ { D }$ , any open cover of ambient space $\mathbb { R } ^ { D }$ induces a partition of unity on the submanifold. This leads to the following construction that will be used throughout the rest of the paper.

Assume $\mathcal { M }$ is contained in the closed ball $\mathbb { B } _ { L } ^ { D }$ for some sufficiently large radius $L$ , we construct a partition of unity of $\mathcal { M }$ as follows. Firstly, we find a set of points $a _ { 1 : M } = \{ a _ { 1 } , a _ { 2 } , \cdot \cdot \cdot , a _ { M } \}$ in $\mathbb { R } ^ { D }$ and a set of positive radii $r _ { 1 : M } = \{ r _ { 1 } , r _ { 2 } , \cdot \cdot \cdot , r _ { M } \}$ such that $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ forms a finite open cover of $\mathbb { B } _ { L } ^ { D }$ . Let $\chi : \mathbb { R } \to \lfloor 0 , \infty )$ denote the commonly used mollifier defined by $\chi ( t ) = e ^ { - 1 / t }$ for $t > 0$ and $\chi ( t ) = 0$ for $t \leq 0$ . For each $m \in [ M ]$ , we define a local partition function as

$$
\widetilde { \rho } _ { m } ( x ) = \frac { \chi ( r _ { m } - \| x - a _ { m } \| _ { 2 } ) } { \chi ( r _ { m } - \| x - a _ { m } \| _ { 2 } ) + \chi ( \| x - a _ { m } \| _ { 2 } - r _ { m } / 2 ) } , \quad x \in \mathbb { R } ^ { D } .
$$

It is straightforward to check that for each $m \in [ M ]$ , $\widetilde { \rho } _ { m } ( x ) \in C ^ { \infty } ( \mathbb { R } ^ { D } )$ , $\widetilde { \rho } _ { m } ( x ) = 1$ for $x \in B _ { r _ { m } / 2 } ( a _ { m } )$ , and $\widetilde { \rho } _ { m }$ vanishes outside $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ . Therefore, $\{ \rho _ { m } \} _ { m \in [ M ] }$ forms a partition of unity for $\mathcal { M }$ with $\begin{array} { r } { \rho _ { m } = \widetilde { \rho } _ { m } / \big ( \sum _ { m ^ { \prime } = 1 } ^ { M } \widetilde { \rho } _ { m ^ { \prime } } \big ) } \end{array}$ for $m \in [ M ]$ .

# 2.5 Smooth distributions on submanifold and generative model class

For a smooth submanifold $\mathcal { M }$ with atlas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ , one can define a distribution $\mu$ on $\mathcal { M }$ by specifying how it acts on all smooth functions $f \in C ^ { \beta } ( { \mathcal { M } } )$ through its expectation $\mathbb { E } _ { \mu } \lfloor f \rfloor$ (duality between distributions and bounded continuous functions). Specifically, the global characterization of $\mathbb { E } _ { \mu } | f |$ as an integral over $\mathcal { M }$ can be decomposed into local ones as in the following via a partition of unity argument [Do Carmo and Flaherty Francis, 1992] (second equality), and the local integrals can be characterized using charts (third equality):

$$
\mathbb { E } _ { \mu } [ f ] = \int _ { \mathcal { M } } f \mathrm { d } \mu = \sum _ { \lambda \in \Lambda } \int _ { U _ { \lambda } } f \mathrm { d } ( \rho _ { \lambda } \mu ) = \sum _ { \lambda \in \Lambda } \int _ { \varphi _ { \lambda } ( U _ { \lambda } ) } f \circ \varphi _ { \lambda } ^ { - 1 } \mathrm { d } \big [ ( \varphi _ { \lambda } ) _ { \# } ( \rho _ { \lambda } \mu ) \big ] ,
$$

where $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ is a partition of unity subordinate to atlas $\mathcal { A }$ , and $\rho _ { \lambda } \mu$ stands for the non-negative measure whose Radon-Nikodym derivative relative to $\mu$ is $\rho _ { \lambda }$ . In particular, if $\left( \varphi _ { \lambda } \right) _ { \# } ( \rho _ { \lambda } \mu )$ admits an $\alpha$ -smooth density function for $\alpha \in ( 0 , \beta - 1 ]$ relative to the Lebesgue measure on $\mathbb { R } ^ { d }$ for each $\lambda \in \Lambda$ , then $\mu$ is said to be an $\alpha$ -smooth distribution on $\mathcal { M }$ . Note that here similar to the definition of smooth functions on a $\beta$ -smooth manifold, it is not meaningful to talk about distributions with smoothness level beyond $\beta - 1$ since the change of measure formula (we have abused the notation of a measure to denote its density function),

$$
\begin{array} { r } { \big [ ( \varphi _ { 1 } ) _ { \# } \big ( \rho _ { 1 } \rho _ { 2 } \mu \big ) \big ] \left( \varphi _ { 1 } ( x ) \right) = \big [ ( \varphi _ { 2 } ) _ { \# } \big ( \rho _ { 1 } \rho _ { 2 } \mu \big ) \big ] \left( \varphi _ { 2 } ( x ) \right) \cdot \big | \operatorname* { d e t } \big ( \mathrm { d } [ \varphi _ { 2 } \circ \varphi _ { 1 } ^ { - 1 } ] _ { \# ( x ) } \big ) \big | , x \in U _ { 1 } \cap \Omega _ { \# } . } \end{array}
$$

may lead to incompatible smoothness definitions over the intersection of two charts $( U _ { 1 } , \varphi _ { 1 } )$ and $( U _ { 2 } , \varphi _ { 2 } )$ if the atlas is at most $\beta$ -smooth — the differential $^ 6 \mathrm { d } [ \varphi _ { 2 } \circ \varphi _ { 1 } ^ { - 1 } ] _ { y } : \mathbb { R } ^ { d }  \mathbb { R } ^ { d }$ at $y \in \varphi _ { 1 } ( U _ { 1 } \cap U _ { 2 } )$ of the transition map $\varphi _ { 2 } \circ \varphi _ { 1 } ^ { - 1 }$ is at most $( \beta - 1 )$ -smooth in $y$ . An $\alpha$ -smooth distribution on $\mathcal { M }$ can be equivalently defined as a distribution whose density function with respect to the volume measure of $\mathcal { M }$ exists and belongs to $C ^ { \alpha } ( { \mathcal { M } } )$ [Lee, 2013]. Consequently, the smoothness level of the distribution $\mu$ is an intrinsic quantity that does not reply on the choice of the partition of unity.

# 2.5.1 Smooth distributions on smooth compact submanifold

Now, we are in place to define the family of smooth distributions on smooth compact submanifold without boundaries on $\mathbb { R } ^ { D }$ as the set $\mathcal { P } ^ { * } = \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ with $d \leq D$ , $\beta > 1$ and $\alpha \in ( 0 , \beta - 1 ]$ composed of all probability measures $\mu \in \mathcal P ( \mathbb { R } ^ { D } )$ satisfying:

1. $\mu$ is an $\alpha$ -smooth distribution on a $\beta$ -smooth $d$ -dimensional compact submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ .   
2. The density $\mu$ relative to the volume measure of $\mathcal { M }$ is uniformly bounded from below by $1 / L ^ { * }$ on $\mathcal { M }$ .   
3. $\mathcal { M }$ is covered by an atlas $\mathcal { A } = \{ ( U _ { \lambda } , \phi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ on $\mathcal { M }$ such that: a) each chart $( U , \phi )$ in atlas $\mathcal { A }$ satisfies $\| \phi ^ { - 1 } \| _ { C ^ { \beta } ( \phi ( U ) ) } \leq L ^ { * }$ and $\| \mu \circ \phi ^ { - 1 } \| _ { C ^ { \alpha } ( \phi ( U ) ) } \leq L ^ { * } ;$ b) for any $z \in \phi ( U )$ , the Jacobian of $\phi ^ { - 1 } ( z )$ is full rank and all its singular values are lower bounded by $1 / L ^ { * }$ in absolute values. Moreover, for any $x \in \mathcal { M }$ , there exists a $\lambda \in \Lambda$ such that $U _ { \lambda }$ and $\phi _ { \lambda } ( U _ { \lambda } )$ covers $B _ { 1 / L ^ { * } } ( x ) \cap \mathcal { M }$ and $B _ { 1 / L ^ { * } } ( \phi _ { \lambda } ( x ) )$ respectively.

In Appendices B and C, we discuss extensions to manifolds with boundaries and unbounded manifolds.

Remark 1. A similar class of smooth distributions on submanifolds is also considered in Berenfeld and Hoffmann [2021], where their regularity of the manifold is characterized by the notion of reach7. In fact, for any $\beta$ -smooth $d$ -dimensional compact submanifold with reach uniformly bounded from below, one can always find an atlas $\mathcal { A }$ satisfying above conditions with a sufficiently large $L ^ { * }$ [Aamari and Levrard, 2019, Berenfeld and Hoffmann, 2021]. One particular choice of the local parametrization is the exponential map $^ { 8 }$ $\mathrm { e x p } _ { x }$ , and Condition 3 above holds if $\mathrm { e x p } _ { x }$ and $\mu \circ \exp _ { x }$ have the corresponding smoothness and the injectivity radius $^ { 9 }$ of $\mathcal { M }$ is lower bounded away from zero.

Remark 2. A manifold without boundary that is compact is called a closed manifold. Examples of closed submanifolds in $\mathbb { R } ^ { D }$ include a $d$ -dimensional sphere lying in a $( d + 1 )$ - dimensional affine subspace of $\mathbb { R } ^ { D }$ and a $d$ -dimensional torus $\mathbb { T } ^ { d }$ embedded in $\mathbb { R } ^ { D }$ that is diffeomorphic to the product of $d$ circles. Any closed submanifold requires at least two covering charts in its describing atlas since it is not homeomorphic to any open set of $\mathbb { R } ^ { d }$ . Mathematically, the Lusternik-Schnirelmann category [Fox, 1941, Cornea et al., 2003] of a topological manifold $\mathcal { M }$ can be used to provide a lower bound on the smallest number of charts to cover $\mathcal { M }$ . For example, the $d$ -dimensional sphere requires at least two charts (using the stereographic projection) and the $d$ -dimensional torus $\mathbb { T } ^ { d }$ cannot be covered with $d$ or fewer charts.

# 2.5.2 Distribution estimator class: mixture of generative models

To describe the statistical model for representing probability measures $\mu$ on unknown submanifolds, we consider two (mixture of) generative model classes, $S ^ { \mathrm { a p } } = S ^ { \mathrm { a p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ and $S _ { \nu _ { 0 } } ^ { \mathrm { a p } } = S _ { \nu _ { 0 } } ^ { \mathrm { a p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ , where $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ is a pre-specified open cover of $\mathbb { B } _ { L } ^ { D }$ that contains the submanifold. The first generative model class $S ^ { \mathrm { a p } }$ consists of mixtures of generative models with rejection sampling: $\begin{array} { r } { \mu = \sum _ { m = 1 } ^ { M } w _ { [ m ] } \mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) } \end{array}$ where $\{ \rho _ { m } \} _ { m \in [ M ] }$ is the partition of unity subordinate to ${ \mathcal { O } } _ { M }$ defined in Section 2.4, $\{ w _ { [ m ] } \} _ { m \in [ M ] }$ are non-negative mixing weights with $\begin{array} { r } { \sum _ { m = 1 } ^ { M } w _ { [ m ] } = 1 } \end{array}$ , and for any $m \in \lfloor M \rfloor$ : (1) each component of $G _ { [ m ] }$ is a $\beta$ -smooth function over $\mathbb { R } ^ { d }$ with $\beta$ -Hölder norm bounded by $L$ ; (2) $\nu _ { [ m ] }$ is an $\alpha$ -smooth probability density on $\mathbb { B } _ { 1 } ^ { d }$ with $\alpha$ -Hölder norm bounded by $L$ ; (3) $\mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } )$ denotes the probability measure induced by the data generating process where $X \sim [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ is accepted with probability $\rho _ { m } ( X ) \in [ 0 , 1 ]$ . To summarize, we have

$$
\begin{array} { r l } & { \mathcal { S } ^ { \mathrm { a p } } = \Bigl \{ \displaystyle \sum _ { m = 1 } ^ { M } w _ { [ m ] } \mathcal { A } \bigl ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } \bigr ) : \sum _ { m = 1 } ^ { M } w _ { [ m ] } = 1 ; \forall m \in [ M ] , 0 \le w _ { [ m ] } \le 1 ; } \\ & { \qquad G _ { [ m ] } \in C _ { L } ^ { \beta } \bigl ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } \bigr ) ; \nu _ { [ m ] } \in \mathcal { P } \bigl ( \mathbb { B } _ { 1 } ^ { d } \bigr ) \mathrm { ~ a n d ~ } \nu _ { [ m ] } \in C _ { L } ^ { \alpha } \bigl ( \mathbb { B } _ { 1 } ^ { d } \bigr ) \Bigr \} . } \end{array}
$$

The decomposition $\begin{array} { r } { \mu = \sum _ { \lambda \in \Lambda } \rho _ { \lambda } \mu } \end{array}$ of $\mu$ is the dual counterpart of definition (4) for expectation $\mathbb { E } _ { \mu } | f |$ through the partition of unity with $\Lambda \ : = \ : \lfloor M \rfloor$ . To avoid explicit estimation of the local densities $\nu _ { [ m ] }$ , we also consider a second generative model class $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$

$$
\begin{array} { r l r } & { } & { S _ { \nu _ { 0 } } ^ { \mathrm { a p } } = \Big \{ \displaystyle \sum _ { m = 1 } ^ { M } w _ { [ m ] } A ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) : \sum _ { m = 1 } ^ { M } w _ { [ m ] } = 1 ; \forall m \in [ M ] , 0 \le w _ { [ m ] } \le 1 ; } \\ & { } & { G _ { [ m ] } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } ) ; \nu _ { [ m ] } = \left( V _ { [ m ] } \right) _ { \# } \nu _ { 0 } \mathrm { a n d } V _ { [ m ] } \in C _ { L } ^ { \alpha + 1 } ( \mathbb { R } ^ { d } ) \Big \} , } \end{array}
$$

where $\nu _ { 0 }$ is a prespecified distribution on $\mathbb { B } _ { 1 } ^ { d }$ that is easy to sample from. In other words, $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ further replaces the local latent variable distribution $\nu _ { [ m ] }$ by a generative model be equivalently expressed as $( \nu _ { 0 } , V _ { [ m ] } )$ for each $m \in [ M ]$ with a common generative distribution $\begin{array} { r } { \mu = \sum _ { m = 1 } ^ { M } w _ { [ m ] } A ( [ G _ { [ m ] } \circ V _ { [ m ] } ] , \nu _ { 0 } , \rho _ { m } ) } \end{array}$ $\nu _ { 0 }$ , so that 0at is easy to generate can samples: first draw a categorical variable $V$ in $\lfloor M \rfloor$ with probabilities $\mathbb { P } ( V = m ) = w _ { [ m ] }$ for $m \in [ M ]$ ; then draw a sample $U$ from $\nu _ { 0 }$ and set $X = G _ { [ V ] } \circ V _ { [ V ] } ( U )$ ; finally, flip a coin and accept $X$ with probability $\rho _ { V } ( X )$ .

We will show in our main result (Theorem 1) that for smooth distributions on unknown closed submanifold with positive density, we are able to construct a minimax-optimal estimator (modulo logarithm terms) ${ \widehat { \mu } } \in S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ with $\nu _ { 0 }$ being the uniform distribution on $\mathbb { B } _ { 1 } ^ { d }$ (the uniform distribution can also be replaced with any other smooth distributions). While when the target distribution $\mu ^ { * }$ belongs to a more general (mixture of) generative model class $S ^ { * }$ as we considered in Theorem 2, which contains all distributions in ${ \mathcal { P } } ^ { * }$ and also distributions induced by a single generative model $( \nu ^ { * } , G ^ { * } ) ^ { 1 0 }$ with $\nu ^ { * }$ being smoothly decaying to zero around the boundary of its support, we will need the more flexible approximation family $S ^ { \mathrm { a p } }$ to cover $S ^ { * }$ .

# 3 Minimax Rate of Convergence

In this section, we establish the minimax rate of convergence for the adversarial risk on $\mu ^ { \ast } ~ \in ~ \mathcal { P } ^ { \ast }$ of distribution estimation on unknown submanifold with i.i.d. samples $X _ { 1 } , X _ { 2 } , \ldots , X _ { n } \sim \mu ^ { * }$ , and propose an optimal procedure based on learning a (mixture of) generative model in class $S ^ { \mathrm { a p } }$ (or $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ ) via minimizing a carefully constructed empirical surrogate risk. After that, we also provide a data-driven adaptive estimator that does not require prior knowledge about intrinsic dimension $d$ , manifold smoothness $\beta$ and distribution smoothness $\alpha$ .

The following theorem summarizes our main result on the minimax rate of convergence.

Theorem 1 (Minimax rate of distribution estimation). Fix $L ^ { * } > 0$ , $\gamma \geq 0$ , $0 \leq \alpha \leq \beta - 1$ , $\beta > 1$ , and $D , d \in \mathbb { N } ^ { + }$ with $D > d$ , write $\mathcal { P } ^ { * } = \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ , then

1. there exists a constant $L _ { 0 }$ such that when $L ^ { * } \ge L _ { 0 }$ , then

$$
\operatorname* { i n f } _ { \widehat { \mu } \in \mathcal { P } ( \mathbb { R } ^ { D } ) } \operatorname* { s u p } _ { \mu \in \mathcal { P } ^ { * } } \mathbb { E } \big [ d _ { \gamma } ( \widehat { \mu } , \mu ) \big ] \geq C n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \gamma \beta } { d } } ;
$$

2. there exist positive constants $L _ { 1 } , L _ { 2 }$ such that for any $L \ \geq \ L _ { 1 }$ and open cover $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ of $\mathbb { B } _ { L } ^ { D }$ with $\operatorname* { m a x } \{ r _ { 1 } , r _ { 2 } , \cdot \cdot \cdot , r _ { M } \} \leq L _ { 2 }$ , it holds that

$$
\operatorname* { i n f } _ { \widehat { \mu } \in S _ { \nu _ { 0 } } ^ { \operatorname * { m p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L ) } \operatorname* { s u p } _ { \mu \in \mathcal { P } ^ { * } } \mathbb { E } \left[ d _ { \gamma } ( \widehat { \mu } , \mu ) \right] \leq C \left( \frac { n } { \log n } \right) ^ { - \frac 1 2 } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \gamma \beta } { d } } ,
$$

where $\nu _ { 0 } = \mathrm { U n i f } ( \mathbb { B } _ { 1 } ^ { d } )$ and the infimum are both taken over all distribution estimators $\widehat { \mu }$ belonging to corresponding families based on data $X _ { 1 : n }$ .

We make several brief comments on the minimax rate from Theorem 1. First, the logarithmic terms appearing in the upper bound of Theorem 1 enable us to obtain a high probability bound for further bounding the expected loss. Second, the ambient space dimension $\boldsymbol { D }$ does not appear in the exponents of the minimax rate, so the problem of estimating a distribution on a low-dimensional submanifold does not suffer from the “curse of dimensionality” due to a large $D$ . Third, recall that the adversarial loss $d _ { \gamma }$ employed in this paper for distribution estimation captures two aspects of the data generating process: supporting manifold recovery and density estimation on the manifold (c.f. Section 2.3). Both of these two aspects are reflected in the derived minimax rate, as we describe in the following.

In fact, Aamari and Levrard [2019] proves the minimax optimal rate $n ^ { - \frac { \beta } { d } }$ of estimating a $d$ -dimensional $\beta$ -smooth submanifold under the Hausdorff distance, which is related to the third term $n ^ { - \frac { \gamma \beta } { d } }$ in our rate under $\gamma = 1$ . As we discussed in Section 2.3, our adversarial loss $d _ { \gamma }$ under $\gamma = 1$ can be interpreted as an average version of the Hausdorff distance. Therefore, term $n ^ { - \frac { \gamma \beta } { d } }$ is coming from estimating the unknown support of $\mu ^ { * }$ , or supporting manifold recovery (see Remark 3 for more discussions). Moreover, in absence of a low-dimensional submanifold structure, the derived rate reduces to the minimax rate $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } }$ (by taking $\beta = \infty$ ) of estimating a $\alpha$ -smooth density on $[ 0 , 1 ] ^ { d }$ , for $\alpha \in [ 0 , \infty )$ , proved in Liang [2020]. In another related work, Berenfeld and Hoffmann [2021] prove that a carefully constructed kernel density estimator achieves the rate $\scriptstyle n ^ { - \frac { \alpha } { 2 \alpha + d } }$ , $\mathrm { w h e n } ^ { \mathrm { 1 1 } } \alpha \in [ 0 , \beta - 1 ]$ , for the pointwise $\ell _ { p }$ loss of estimating a smooth density supported by an unknown $d$ -dimensional submanifold. Notice that their pointwise loss only concerns the density difference evaluated on the submanifold, which already uses the knowledge of the manifold in defining the loss, explaining why their rate does not involve a term like $n ^ { - \frac { \beta } { d } }$ due to supporting manifold estimation. According to these reasons, the second term $\textstyle n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$ in our rate can be interpreted as a consequence of smooth density estimation on the $d$ -dimensional submnaifold as if the manifold known, where the extra $\gamma$ in the exponent is due to the smoothness of the discriminator class (pointwise loss can be viewed as a discontinuous discriminator, or $\gamma = 0$ ).

Figure 1 depicts the three regimes of the problem characteristics identified by Theorem 1, defined by which of the three terms in the minimax rate $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \gamma \beta } { d } }$ dominates. From the diagram, there exist transitions at $\gamma = d / 2$ and $\gamma = \alpha d / [ 2 \alpha \beta + d ( \beta - 1 ) ]$ . When the discriminator smoothness level $\gamma$ satisfies $\gamma \geq d / 2$ so that the discriminator class is relatively small, the rate is the parametric root- $n$ rate $n ^ { - { \frac { 1 } { 2 } } }$ . When the discriminator smoothness level is moderate, or $\alpha d / [ 2 \alpha \beta + d ( \beta - 1 ) ] \leq \gamma < d / 2$ , the term $\textstyle n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$ due to $d$ -dimensional density estimation dominates the minimax rate. When $0 \leq \gamma < \alpha d / [ 2 \alpha \beta +$ $d ( \beta - 1 ) ]$ , the minimax rate becomes $n ^ { - \frac { \gamma \beta } { d } }$ since with a small $\gamma$ the adversarial loss $d _ { \gamma } ( \mu , \nu )$ between two distributions $\mu$ and $\nu$ tends to be more sensitive to the misalignment between their supports $\operatorname { s u p p } ( \mu )$ and $\operatorname { s u p p } ( \nu )$ than to the discrepancy between the probability mass allocations on their respective supports (c.f. Section 2.3). Overall, in the regime of $\gamma \leq d / 2$ , increasing $\gamma$ leads to a faster rate, while the evaluation metric becomes weaker. It is also worthwhile highlighting that the transition boundary $\gamma = d / 2$ between the parametric regime and the density estimation regime only depends on the discriminator smoothness $\gamma$ and intrinsic dimension $d$ , while the transition boundary $\gamma = \alpha d / [ 2 \alpha \beta + d ( \beta - 1 ) ]$ between the density estimation regime and the supporting manifold estimation regime depends on all problem characteristics $( \alpha , \beta , \gamma , d )$ except for the ambient dimension $\boldsymbol { D }$ — the transition threshold on $\gamma$ converges to $0$ as the manifold smoothness $\beta \to \infty$ and becomes $d / ( 2 \beta + d )$ if the distribution $\mu ^ { * }$ has the maximal (well-defined) smoothness degree $\alpha = \beta - 1$ .

![](images/09023b3fbc6e83646c98e67dd0de488ddcfb81ad8aab19335e7d4783dfb8867f.jpg)  
Figure 1: Diagram for the minimax rate $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \gamma \beta } { d } }$ for fixed $d \in \mathbb { N } ^ { + }$ and $\beta > 1$

Remark 3. Taking $\gamma = 0$ in Theorem 1 implies that $\begin{array} { r } { \operatorname* { i n f } _ { \widehat { \mu } } \operatorname* { s u p } _ { \mu \in \mathcal { P } ^ { * } } \mathbb { E } \left\lfloor d _ { \mathrm { T V } } ( \widehat { \mu } , \mu ) \right\rfloor } \end{array}$ is lower bounded away from zero, meaning that no estimator can consistently estimate $\mu ^ { * }$ relative to total variation metric. In addition, by Pinsker’s inequality, the minimax rate relative to the Jensen–Shannon (JS) divergence or KL divergence is also lower bounded away from zero. This lack of estimation consistency is due to the misalignment in supports between $\widehat { \mu }$ and $\mu ^ { * }$ , and theoretically explains the empirical findings made in [Arjovsky and Bottou, 2017, Goodfellow et al., 2014]: the training of the original GAN, which minimizes the JS divergence [Goodfellow et al., 2014] at the population level, tends to be unstable, while the training of GAN’s using some weaker discrepancy measures, such as the Wasserstein GAN [Arjovsky and Bottou, 2017] using the 1-Wasserstein distance (corresponding to $d _ { \gamma }$ with $\gamma = 1$ ), are more stable and the resulting generators are more accurate and reliable. In particular, Arjovsky and Bottou [2017] shows that, in the original GAN, when the support $\operatorname { s u p p } ( \mu ^ { * } )$ of target distribution $\mu ^ { * }$ lies on a low-dimensional manifold and does not perfectly aligned with the support $\operatorname { s u p p } ( \widehat { \mu } )$ of the output distribution $\widehat { \mu }$ from the generator class, then there always exists a perfect discriminator in the discriminator class that separates real samples and fake samples produced by the generator with $1 0 0 \%$ accuracy. As a consequence, $\widehat { \mu }$ tends to max out in a neighborhood around $\operatorname { s u p p } ( \mu ^ { * } )$ in the ambient space due to the exploding generator gradient whose expectation and variance are infinite as the discriminator becomes closer to optimality, leading to a notorious decrease in sample quality.

Remark 4. A more general setting adopted by some authors considers the deconvolution problem that allows the observed data to contain noises, that is, we observe a set of $n$ i.i.d. random samples $\{ Y _ { i } \} _ { i = 1 } ^ { n }$ generated from model $Y _ { i } = X _ { i } + \varepsilon _ { i }$ , where $\{ X _ { i } \} _ { i = 1 } ^ { n }$ are samples from the target distribution $\mu ^ { * }$ supported on an unknown $d$ -dimensional submanifold $\mathcal { M }$ in $\mathbb { R } ^ { D }$ , and $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are typically independent errors with a known distribution [Caillerie et al., 2011, Genovese et al., 2012a]. In this noisy setting, Caillerie et al. [2011] propose a modified kernel deconvolution estimator and show the convergence rate $O \big ( ( \log n ) ^ { - 1 } \big )$ under the 2-Wasserstein distance with various manifolds and various noise distributions (e.g. isotropic Gaussian noise or Gaussian noise “perpendicular" to the manifold). In addition, Genovese et al. [2012a] shows that when the error follows the standard $D$ - dimensional Gaussian distribution, the minimax rate of estimating manifold $\mathcal { M }$ under the Hausdorff distance is extremely slow: it is lower bounded by $O \big ( ( \log n ) ^ { - 1 } \big )$ . These results suggest that estimating a low-dimensional distribution or its supporting manifold based on noisy observations is an intrinsically hard problem, which is why we focus on the noiseless case in this paper. One way commonly adopted in the literature of circumventing this slow convergence is by assuming the noise variance $\sigma ^ { 2 }$ to decay with the same size. If we also allow isotropic Gaussian noise in the data with variance scales as $\sigma ^ { 2 } = O \left( n ^ { - 1 + \frac { 2 \beta } { d } } \right)$ , then Corollary 3 in Appendix F.4 shows that the estimation procedure via generative models developed in Section 3.1 has the same rate of convergence as if the samples are noiseless.

# 3.1 Minimax-optimal estimation via generative models

In this subsection, we describe an estimator $\widehat { \mu }$ constructed via generative models that achieves the minimax rate upper bound in Theorem 1. Generative model learning has recently become popular [Goodfellow et al., 2014, Li et al., 2015, Biau et al., 2020, Arjovsky et al., 2017, Tolstikhin et al., 2019, Zhao et al., 2018] due to its great practical success in generating new examples such as images and texts that are indistinguishable from real objects, and impressive computational scalability to complex and massive datasets. In the conventional framework, a single generative model $( \widetilde { \nu } , \widetilde { G } )$ is learned by solving the following minimax optimization problem,

$$
\widetilde { \mu } = \widetilde { G } _ { \# } \widetilde { \nu } = \underset { \mu \in { \mathcal D } _ { G } } { \arg \operatorname* { m i n } } \ \underset { f \in { \mathcal F } } { \operatorname* { s u p } } \bigg | \mathbb E _ { \mu } [ f ( x ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \bigg | ,
$$

where recall that ${ \mathcal { D } } _ { G } = \left\{ G _ { \# } \nu : \nu \in \Upsilon , G \in { \mathcal { G } } \right\}$ is a generic generator class and $\mathcal { F }$ is a generic discriminator class. Here the empirical average $n ^ { - 1 } \textstyle \sum _ { i = 1 } f ( X _ { i } )$ is a sample surrogate to the population level expectation $\mathbb { E } _ { \mu ^ { * } } [ f ]$ . A successful application of this procedure replies on the implicit assumption that the underlying data manifold $\mathcal { M }$ admits a single chart representation. In this work, we propose a new generative model learning procedure with two improvements — first, we employ mixtures of generative models in $S ^ { \mathrm { a p } }$ (or $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ ) to estimate distributions on those submanifolds that cannot be covered by a single chart; second, we use a regularized surrogate $\widehat { \mathcal { I } } ( f ) = \widehat { \mathcal { I } } ( f ; X _ { 1 : n } )$ to replace $n ^ { - 1 } \textstyle \sum _ { i = 1 } f ( X _ { i } )$ in (7), which improves the estimation accuracy by utilizing smoothness structures in $\mu ^ { * }$ and discriminator $f$ and thus mitigates overfitting.

Our procedure takes the form of

$$
\widehat { \mu } = \underset { \mu \in \mathcal { S } } { \arg \operatorname* { m i n } } \underset { f \in \mathcal { F } } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu } [ f ( X ) ] - \widehat { \mathcal { I } } ( f ) \Big | ,
$$

where $\boldsymbol { S }$ is the approximation family that will be chosen later. The main ingredient of our minimax upper bound proof is to bound $\begin{array} { r } { \operatorname* { s u p } _ { f \in { \mathcal { F } } } \left| { \mathbb { E } } _ { \mu ^ { * } } [ f ( X ) ] - \widehat { { \mathcal { I } } } ( f ) \right| } \end{array}$ since by the optimality of $\widehat { \mu }$ in (8) and the definition of adversarial loss $d _ { \gamma } ( \cdot , \cdot )$ , if the approximation family is correctly specified so that $\mu ^ { * } \in S$ , we have the following basic inequality

$$
\begin{array} { r l } & { \displaystyle { d _ { \mathcal { F } } ( \widehat { \mu } , \mu ^ { * } ) = \operatorname* { s u p } _ { f \in \mathcal { F } } \left| \mathbb { E } _ { \widehat { \mu } } [ f ( x ) ] - \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] \right| \leq \operatorname* { s u p } _ { f \in \mathcal { F } } \left| \mathbb { E } _ { \widehat { \mu } } [ f ( x ) ] - \widehat { \mathcal { I } } ( f ) \right| } } \\ & { \qquad \quad + \operatorname* { s u p } _ { f \in \mathcal { F } } \left| \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \widehat { \mathcal { I } } ( f ) \right| \leq 2 \operatorname* { s u p } _ { f \in \mathcal { F } } \left| \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \widehat { \mathcal { I } } ( f ) \right| . } \end{array}
$$

Therefore, the problem of finding an optimal estimator of $\mu ^ { * }$ boils down to the simultaneous estimation of functional $\mathbb { E } _ { \mu ^ { * } } [ f ( X ) ]$ for all $f \in { \mathcal { F } }$ with smallest worst case error. In this paper, we focus on the Hölder discriminator class $\mathcal { F } = \mathcal { C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ . Note that the empirical average ${ \widehat { \mathcal { T } } } _ { \mathrm { a v e } } ( f ) : = n ^ { - 1 } \sum _ { i = 1 } ^ { n } f ( X _ { i } )$ is not an optimal choice for $\widehat { \mathcal { I } } ( f )$ since the following two sided high probability bound of the supremum of empirical process (c.f. Lemma 13 in Appendix E)

$$
C _ { 1 } \sqrt { \frac { 1 } { n } } \vee \frac { n ^ { - \frac { \gamma } { d } } } { \log n } \leq \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \right| \leq C _ { 2 } \sqrt { \frac { \log n } { n } } \vee n ^ { - \frac { \gamma } { d } }
$$

implies its rate of convergence to be strictly worse than the optimal rate (modulo $\log n$ factors) $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \gamma \beta } { d } }$ ( $\beta > 1$ ) inferred by the minimax lower bound in Theorem 1, where the third term $n ^ { - \frac { \gamma \beta } { d } }$ is due to the estimation of unknown submanifold $\mathcal { M }$ and will disappear if $\mathcal { M }$ is known. It is worthwhile noting that despite the discriminator class ${ \mathcal { C } } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ being defined on $\mathbb { R } ^ { D }$ , the upper bound in (10) only depends on the intrinsic dimension $d$ of the support of $\mu ^ { * }$ , which is due to a covering argument. We provide two proofs to (10) in the appendix: one is based on the usual chaining technique in the empirical process theory; the other is based on embedding the discrimator space $C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ into Besov space $B _ { \infty , \infty } ^ { \alpha } ( \mathbb { R } ^ { D } )$ and truncating the wavelet expansion of $f$ to a proper degree (c.f. Appendix A for a brief review about Besov spaces and wavelet expansions). The first approach based on chaining is succinct and leads to a tighter bound (no $\log n$ factors), but not easily generalizable to analyze more complicated surrogate $\widehat { \mathcal { I } } ( f )$ beyond the empirical average; the second approach incurs extra $\log n$ factors and is technically more involved, but its proof is more insightful and motivates our improved surrogate $\widehat { \mathcal { I } } ( f )$ leading to a minimax-optimal (modulo $\log n$ factors) estimator $\widehat { \mu }$ .

The primary reason for the empirical average $\widehat { \mathcal { I } } _ { \mathrm { a v e } } ( f )$ not achieving the optimal bound for $\begin{array} { r } { \operatorname* { s u p } _ { f \in \mathcal { F } } \left| \mathbb { E } _ { \mu } [ f ( x ) ] - \widehat { \mathcal { I } } ( f ) \right| } \end{array}$ is that $\widehat { \mathcal { I } } _ { \mathrm { a v e } } ( f )$ does not utilize the smoothness structure on the true underlying distribution $\mu ^ { * }$ and submanifold $\mathcal { M }$ . In a nutshell, our improvements on surrogate $\widehat { \mathcal { I } }$ come from two sources:

1. we plug-in a smoothness regularized empirical distribution $\widetilde \nu$ to improve the estimation on the expectation $\mathbb { E } _ { \mu ^ { * } } [ f _ { \mathrm { h i g h } } ]$ of the high frequency part $f _ { \mathrm { h i g h } }$ of the discriminator $f = f _ { \mathrm { l o w } } + f _ { \mathrm { h i g h } }$ with $f _ { \mathrm { l o w } }$ denoting the low frequency part. This improvement reduces part of the $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \gamma } { d } }$ error in (10) to $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } }$ due to utilizing the $\alpha$ -smoothness of true distribution $\mu ^ { * }$ . Specifically, $\widetilde \nu$ is constructed by using partition of unity and truncating the wavelet expansion of localized empirical distributions (restricted to the open cover) to filter out the high frequency components that are unstable due to relatively high variances.

2. we add a higher-order correction term to account for the misalignment between the effective support of regularized distribution $\widetilde \nu$ and the support of true distribution $\mu ^ { * }$ , both having intrinsic dimension $d$ . This improvement reduces part of the $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \gamma } { d } }$ error in (10) to $n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \gamma \beta } { d } }$ due to utilizing the $\beta$ -smoothness of submanifold $\mathcal { M }$ ( $\beta \geq 1$ ). Specifically, this correction is constructed using partition of unity and compensating a remainder term from the Taylor expansion of discriminator $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ up to order $\lfloor \gamma \rfloor$ when estimating its expectation.

Combining these two modifications on $\widehat { \mathcal { I } }$ together improves the overall worst case error rate fr om n − 12 ∨ n − γd to n − 12 ∨ n − α + γ2 α + d ∨ n − γ βd .

To summarize, our proposed minimax-optimal estimator $\widehat { \mu }$ is constructed in three steps. Let $[ n ] = I _ { 1 } \cap I _ { 2 }$ be a random splitting of the data indices into two sets with $| I _ { 1 } | = \lceil n / 2 \rceil$ and $\left| I _ { 2 } \right| = n - \left| I _ { 1 } \right|$ . Let $( L , M )$ be sufficiently large positive constants and recall that $\{ \rho _ { m } \} _ { m \in [ M ] }$ is the partition of unity subordinate to the open cover $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ of $\mathbb { B } _ { L } ^ { D }$ constructed in Section 2.4.

Step 1: (Submanifold estimation) For each open set $\mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ }$ in the open cover ${ \mathcal { O } } _ { M }$ , we form estimators $\widehat { G } _ { [ m ] }$ and $\widehat { Q } _ { [ m ] }$ of a $1 2$ coordinate map $\varphi _ { m } : B _ { r _ { m } } ( a _ { m } ) ^ { \circ }  \mathbb { R } ^ { d }$ and its inverse $\varphi _ { m } ^ { - 1 }$ respectively by minimizing the squared reconstruction loss on samples $\{ X _ { i } : i \in I _ { 1 } \}$

$$
( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } ) = \underset { G \in \mathcal { G } , Q \in \mathcal { Q } } { \arg \operatorname* { m i n } } \left( \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| X _ { i } - G \circ Q ( X _ { i } ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } ( X _ { i } \in S _ { m } ^ { \dagger } ) \right) ,
$$

where $S _ { m } ^ { \dagger } = \mathbb { B } _ { r _ { m } + 0 . 5 / L } ( a _ { m } )$ is an enlargement of $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ for avoiding the technical issue due to the boundary of $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ , $\mathcal { G } = C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and $\mathcal { Q } = C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ . Let $\begin{array} { r } { \widehat { p } _ { m } = \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \mathbf { 1 } ( X _ { i } \in \mathcal { S } _ { m } ^ { \dagger } ) } \end{array}$ denote the sample frequency of falling into $S _ { m } ^ { \dagger }$ and let $\begin{array} { r } { \widehat { \mathbb { M } } = \{ m \in [ M ] : \widehat { p } _ { m } \geq \sqrt { \frac { \log n } { n } } \} } \end{array}$ .

Step 2: (Surrogate functional construction) For each m ∈ [M ], let ν[m],Q[m] be a smoothness regularized estimator of $\left( \widehat { Q } _ { [ m ] } \right) _ { \# } \left( \rho _ { m } \mu ^ { * } \right)$ by truncating a wavelet expansion to a finite degree. Let $J$ be the largest integer such that $2 ^ { J } \leq ( \frac { n } { \log n } ) ^ { \frac { 1 } { 2 \alpha + d } }$ , $\Pi _ { J } f$ denote the projection of any $f \in { \mathcal { F } }$ onto the first scale $J$ wavelet coefficients and $\Pi _ { J } ^ { \perp } f = f - \Pi _ { J } f$ . The precise definitions of $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ and $\Pi _ { J } f$ are available in Appendix A . We form a regularized estimator of localized expectation $\mathbb { E } _ { \mu ^ { * } } [ f ( X ) \rho _ { m } ( X ) ]$ using samples $\{ X _ { i } : i \in I _ { 2 } \}$ as follows. If $m \not \in { \widehat { \mathbb { M } } }$ , then define $\widehat { \mathcal { I } } _ { m } ( f ) = 0$ to avoid estimation degeneracy (see Section D.2 for more details); otherwise, define $\widehat { \mathcal { I } } _ { m } ( f ) = \widehat { \mathcal { I } } _ { m , s } ( f ) + \widehat { \mathcal { I } } _ { m , l } ( f ) + \widehat { \mathcal { I } } _ { m , h } ( f )$ , where

$$
\begin{array} { r l } & { \widehat { \mathcal { T } } _ { m , l } ( f ) = \displaystyle \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } ( \Pi _ { J } f ) \circ \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X _ { i } ) \rho _ { m } ( X _ { i } ) , } \\ & { \widehat { \mathcal { T } } _ { m , h } ( f ) = \mathbb { E } _ { \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } } \left[ ( \Pi _ { J } ^ { \perp } f ) \circ \widehat { G } _ { [ m ] } \right] , \quad \mathrm { a n d } } \\ & { \widehat { \mathcal { T } } _ { m , s } ( f ) = \displaystyle - \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \sum _ { j \in \mathbb { N } _ { 0 } ^ { D } } \frac { 1 } { j ! } f ^ { ( j ) } ( X _ { i } ) \left[ \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X _ { i } ) - X _ { i } \right] ^ { j } \rho _ { m } ( X _ { i } ) . } \end{array}
$$

The first two terms $\widehat { \mathcal { I } } _ { m , l } ( f )$ and $\widehat { \mathcal { I } } _ { m , h } ( f )$ together form a sample approximation to $\mathbb { E } _ { \mu ^ { * } } \bigl [ f \bigl ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \bigr ) \rho _ { m } ( X ) \bigr ) \bigr ]$ , where $\widehat { \mathcal { I } } _ { m , l } ( f )$ estimates the expectation of the low frequency components collected in $f _ { \mathrm { l o w } } = \Pi _ { J } f$ of $f$ and $\widehat { \mathcal { I } } _ { m , h } ( f )$ estimates the high frequency components collected in $f _ { \mathrm { h i g h } } = \Pi _ { J } ^ { \perp } f$ ; the third term $\widehat { \mathcal { I } } _ { m , s } ( f )$ corresponds to a (sample version of) higher-order smoothness correction to $\mathbb { E } _ { \mu ^ { * } } \bigl [ f \bigl ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \bigr ) \rho _ { m } ( X ) \bigr ) \bigr ]$ for approximating $\mathbb { E } _ { \mu ^ { * } } \bigl [ f ( X ) \rho _ { m } ( X ) \bigr ]$ . Finally, we construct a regularized estimator of $\mathbb { E } _ { \mu ^ { * } } [ f ( X ) ]$ as $\begin{array} { r } { \widehat { \mathcal { I } } ( f ) = \sum _ { m = 1 } ^ { M } \widehat { \mathcal { I } } _ { m } ( f ) } \end{array}$ .

Step 3: (Generative model estimation) Given an approximation family $\boldsymbol { S }$ , the estimator $\widehat { \mu }$ is defined as

$$
\widehat { \mu } = \underset { \mu \in { \cal S } } { \arg \operatorname* { m i n } } \ \underset { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big ( \mathbb { E } _ { \mu } \big [ f ( X ) \big ] - \widehat { \mathcal { I } } ( f ) \Big ) .
$$

In practice, we may also use the kernel density estimator with proper bandwidth to regularize the empirical distribution of local latent variables (c.f. Remark 8 in Appendix A) in step 2; however, the wavelet truncation is technically easier to analyze. The following theorem shows that the estimator $\widehat { \mu }$ in (13) can achieve a minimax-optimal rate (modulo logarithmic term) when the target distribution $\mu ^ { * }$ belongs to a larger generative model class $S ^ { * } = S ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ that contains the distribution family ${ \mathcal { P } } ^ { * }$ considered in Theorem 1 as a subset, where $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ forms a open cover for $\mathbb { B } _ { L } ^ { D }$ and for any distribution $\mu \in S ^ { * }$ and $m \in [ M ]$ , there exists a set ${ \widetilde { \cal S } } _ { m }$ containing $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ , such that $\mu | _ { \widetilde { S } _ { m } }$ can be written as a single generative model $( \nu _ { [ m ] } , G _ { [ m ] } )$ with an invertible and $\beta$ -smooth generative function $G _ { [ m ] } : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , and an $\alpha$ -smooth density $\nu _ { [ m ] } \in \mathcal { P } ( \mathbb { B } _ { 1 } ^ { d } )$ . The precise definition of $S ^ { * }$ is given in Appendix B. In particular, Lemma 8 in Appendix B shows that for a suitable choice of the open cover ${ \mathcal { O } } _ { M }$ , ${ \mathcal { P } } ^ { * }$ is a subset of $S ^ { * }$ ; moreover, the distribution estimator class $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ with $\nu _ { 0 }$ being $\operatorname { U n i f } ( \mathbb { B } _ { 1 } ^ { d } )$ is sufficient to cover ${ \mathcal { P } } ^ { * }$ , while we need the more flexible approximation family $S ^ { \mathrm { a p } }$ to cover the generative model class $S ^ { * }$ , thus the following theorem gives a stronger result than the upper bound in Theorem 1. See Lemma 8 in Appendix B for a precise relationship among these distribution classes. It is worth mentioning that our proof of Lemma 8 applies the Caffarelli’s global regularity theory [Theorem 12.50 of Villani, 2009, Caffarelli, 1996] from optimal transport theory to construct the generative maps $\{ V _ { [ m ] } \} _ { m = 1 } ^ { M }$ in the definition of class $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ (c.f. Remark 11 in in Appendix B for further details).

Theorem 2 (Minimax upper bound in generative model class). Let the approximation family $\boldsymbol { S }$ to be $S ^ { \mathrm { a p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ . Suppose $\mu ^ { * } \in { \mathcal { S } } ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ and $X _ { 1 : n }$ are i.i.d. samples from $\mu ^ { * }$ . If $D > d$ , $\gamma , \alpha \geq 0$ and $\beta > 1$ , then for any positive constant $c$ , there exist positive constants $c _ { 1 }$ and $n _ { 0 }$ such that when $n \geq n _ { 0 }$ , it holds with probability larger than $1 - n ^ { - c }$ that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big ( \mathbb { E } _ { \mu ^ { * } } \big [ f ( X ) \big ] - \sum _ { m = 1 } ^ { M } \widehat { \mathcal { T } } _ { m } ( f ) \Big ) \leq c _ { 1 } \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { 1 } { 2 } } \vee \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \gamma \beta } { d } } .
$$

As a result

$$
\mathbb { E } [ d _ { \gamma } ( \widehat { \mu } , \mu ^ { * } ) ] \leq C \left( \frac { n } { \log n } \right) ^ { - \frac { 1 } { 2 } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \gamma \beta } { d } } .
$$

Based on Lemma 8 and the first statement of Theorem 2, when the approximation family $\boldsymbol { S }$ is chosen to be $S _ { \nu _ { 0 } } ^ { \mathrm { a p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ with $\nu _ { 0 } = \mathrm { U n i f } ( \mathbb { B } _ { 1 } ^ { d } )$ , the estimator $\widehat { \mu }$ can achieve the minimax upper bound in Theorem 1 for a large enough constant $L$ and a suitable choice of the open cover ${ \mathcal { O } } _ { M }$ .

Remark 5. The most essential conditions in the definition of the generative model class $S ^ { * }$ for obtaining the minimax-optimal rate are the following: (1) the invertibility and the Hölder regularity of the generative functions $G _ { [ m ] }$ in each generative model, which enable us to obtain a feasible estimator $( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } )$ for reconstructing the data around $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ in Step 1 of the construction of $\widehat { \mu }$ ; (2) the Hölder regularity of reweighted densities $\nu _ { [ m ] } \cdot ( \rho _ { m } \circ G _ { [ m ] } )$ of the local variables over the entire space $\mathbb { R } ^ { d }$ , as this can lead to sufficiently high smoothness of $( \widehat { Q } _ { [ m ] } ) _ { \# } \big ( \rho _ { m } \mu ^ { * } \big )$ (with high probability) and thus enables us to construct a smoothness regularized estimator $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ to the density of $( \widehat { Q } _ { [ m ] } ) _ { \# } \big ( \rho _ { m } \mu ^ { * } \big )$ in Step 2 of the construction of $\widehat { \mu }$ . Moreover, our theoretical development relaxes the common assumption made in the manifold learning literature [e.g. Aamari and Levrard, 2019] on the smoothness of the underlying data submanifold from $C ^ { 2 }$ to $C ^ { \beta }$ with $\beta > 1$ .

Remark 6. A similar estimator can be constructed to achieve the same rate in Theorem 2 for estimating the constrained distribution $\mu ^ { * } \vert _ { K _ { 0 } } ^ { 1 3 }$ , where $K _ { 0 }$ is a fixed compact set and the intersection of $K _ { 0 }$ and $\mathcal { M } = \operatorname { s u p p } ( \mu ^ { * } )$ is away from the boundary of $\mathcal { M }$ if it exists. The main difference is that, in this case, after estimating a parametrization $( \widehat { G } , \widehat { Q } )$ of ${ \mathcal { M } } \cap K _ { 0 }$ , we need an extra step to estimate the support of $\widehat { Q } _ { \# } ( \mu ^ { * } | _ { K _ { 0 } } )$ before constructing a finite sample surrogate to $\mathbb { E } _ { \mu ^ { * } | _ { K } } [ f ( \widehat { G } \circ \widehat { Q } ( X ) ) ]$ . Further details are included in Appendices C.2 and F.3.

Remark 7. The surrogate functional $\widehat { \mathcal { I } } ( f )$ can also be used to construct a test statistic in the two sample hypothesis testing problem, where we reject the hypothesis $H _ { 0 } : \mu _ { 1 } = \mu _ { 2 }$ if supf∈C α+γ γ βd $\begin{array} { r } { \operatorname { v } _ { ( \mathbb { R } ^ { D } ) } \left( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) \right) \ge c \delta _ { n } ^ { * } \equiv c \left( \frac { n } { \log n } \right) ^ { - \frac { 1 } { 2 } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \gamma \rho } { d } } } \end{array}$ given two set of $n$ random samples $X _ { 1 : n }$ and $Y _ { 1 : n }$ independently obtained from two underlying distributions $\mu _ { 1 } , \mu _ { 2 } \in S ^ { * }$ , respectively. The test statistic can successfully detect any local alternatives that separate from the null by at least ${ \delta } _ { n } ^ { * }$ (up to a multiplicative constant) in the $d _ { \gamma }$ metric; see Appendix C.1 for further details.

# 3.2 Data-driven adaptive distribution estimation

Since the problem of adaptive estimation of the intrinsic dimensionality of (noisy) manifoldvalued data is a fairly well-studied topic [Camastra and Vinciarelli, 2002, Carter et al., 2009, Farahmand et al., 2007, Levina and Bickel, 2004, Little et al., 2009, Yang and Dunson, 2016], we may apply any of these methods to obtain a a high probability consistent estimator of $d$ beforehand. Therefore, we will only focus on the adaption of our estimator to the unknown manifold smoothness level $\beta ^ { * }$ and distribution smoothness level $\beta ^ { * }$ . Suppose the true smoothness levels $\beta ^ { * } \in [ \beta _ { \operatorname* { m i n } } , \beta _ { \operatorname* { m a x } } ]$ and $\alpha ^ { * } \in [ \alpha _ { \operatorname* { m i n } } , \alpha _ { \operatorname* { m a x } } ]$ , where $\alpha _ { \mathrm { m i n } } \geq 0$ and $\beta _ { \mathrm { m i n } } > 1$ . Choose discrete grids

$$
3 _ { 1 } = \{ \beta _ { \mathrm { m i n } } = \beta _ { 1 } < \cdot \cdot \cdot < \beta _ { N _ { 1 } } = \beta _ { \mathrm { m a x } } \} \mathrm { a n d } B _ { 2 } = \{ \alpha _ { \mathrm { m i n } } = \alpha _ { 1 } < \cdot \cdot \cdot < \alpha _ { N _ { 2 } } = \alpha _ { \mathrm { m a x } } \} ,
$$

where $\beta _ { j } - \beta _ { j - 1 } = c _ { 1 } / \log n$ and $\alpha _ { k } - \alpha _ { k - 1 } = c _ { 2 } / \log n$ for $j \in [ N _ { 1 } ]$ and $k \in [ N _ { 2 } ]$ . Recall that $\widehat { \mathbb { M } } = \{ m \in [ M ] : \widehat { p } _ { m } \geq \sqrt { \frac { \log n } { n } } \}$ from Section 3.1. For $m \in \widehat { \mathbb { M } }$ and $\beta _ { j } \in B _ { 1 }$ , let

$( \widehat { G } _ { [ m ] } ^ { \lfloor \beta _ { j } \rfloor } , \widehat { Q } _ { [ m ] } ^ { \lfloor \beta _ { j } \rfloor } )$ denote the submanifold estimator defined in equation (11) with $\beta = \beta _ { j }$ . Also let ${ \widehat { \beta } } _ { [ m ] }$ to be the maximal smoothness level in $B _ { 1 }$ that minimizes the reconstruction error, or

$$
\widehat { \beta } _ { [ m ] } = \operatorname* { m a x } \Big \{ \beta \in \mathcal { B } _ { 1 } : \sum _ { i \in I _ { 1 } } \| X _ { i } - \widehat { G } _ { [ m ] } ^ { [ \beta ] } \circ \widehat { Q } _ { [ m ] } ^ { [ \beta ] } ( X _ { i } ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } ( X _ { i } \in S _ { m } ^ { \dagger } ) = 0 \Big \} .
$$

For a fixed $\alpha _ { k } \in B _ { 2 }$ and $m \in \widehat { \mathbb { M } }$ , we use $\widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k } ] } ( f )$ , $\widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k } ] } ( f )$ and $\widehat { J } _ { m , s } ^ { \dagger } ( f )$ to denote the surrogate functionals $\widehat { \mathcal { I } } _ { m , h } ( f )$ , $\widehat { \mathcal { I } } _ { m , l } ( f )$ and $\widehat { J } _ { m , s } ( f )$ defined in (12) respectively with $\alpha = \alpha _ { k }$ and $( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } ) = \big ( \widehat { G } _ { [ m ] } ^ { [ \beta _ { [ m ] } ] } , \widehat { Q } _ { [ m ] } ^ { [ \beta _ { [ m ] } ] } \big )$ . The Lepski’s estimator [Lepskii, 1991] is then

$$
\widehat { \mu } ^ { \dagger } = \underset { \mu \in \mathcal { S } } { \arg \operatorname* { m i n } } \ \underset { f \in \mathcal { C } _ { 1 } ^ { \dagger } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big ( \mathbb { E } _ { \mu } \big [ f ( X ) \big ] - \sum _ { m \in \widehat { \mathbb { M } } } \big [ \widehat { \mathcal { I } } _ { m , h } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal { I } } _ { m , s } ^ { \dagger } ( f ) \big ] \Big ) ,
$$

where $\boldsymbol { S } = \boldsymbol { S } ^ { \mathrm { a p } } ( \boldsymbol { d } , D , \alpha _ { \mathrm { m a x } } , \beta _ { \mathrm { m a x } } , \mathcal { O } _ { M } , L )$ , and

$$
\begin{array} { r l } & { \widetilde { \nu } _ { [ m ] } = \operatorname* { m a x } \biggr \{ \alpha \in \mathcal { B } _ { 2 } : \mathrm { ~ f o r ~ a l l ~ } \alpha ^ { \prime } \leq \alpha , \alpha ^ { \prime } \in \mathcal { B } _ { 2 } , } \\ & { \qquad \quad \underset { f \in { \mathcal C } _ { 1 } ^ { \gamma } ( \mathbb R ^ { D } ) } { \operatorname* { s u p } } \biggr \lvert \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha ] } ( f ) - \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha ^ { \prime } ] } ( f ) - \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha ^ { \prime } ] } ( f ) \biggr \rvert \leq c _ { 0 } \sqrt { \frac { \log n } { n } } \vee \Big ( \frac { \log n } { n } \Big ) ^ { \frac { \alpha ^ { \prime } } { 2 \alpha } } } \end{array}
$$

The following corollary shows that such an estimator $\widehat { \mu } ^ { \dagger }$ simultaneously attains the optimal rate (within a possibly logarithmic factor) over all smoothness levels in the range $\beta ^ { * } \in [ \beta _ { \operatorname* { m i n } } , \beta _ { \operatorname* { m a x } } ]$ and $\alpha ^ { * } \in [ \alpha _ { \operatorname* { m i n } } , \alpha _ { \operatorname* { m a x } } ]$ .

Corollary 1. Suppose $\mu ^ { * } \in { \mathcal { S } } ^ { * } ( d , D , \alpha ^ { * } , \beta ^ { * } , \mathcal { O } _ { M } , L )$ . If $D > d$ , $\gamma \geq 0$ , $\beta ^ { * } \in [ \beta _ { \operatorname* { m i n } } , \beta _ { \operatorname* { m a x } } ]$ and $\alpha ^ { * } \in [ \alpha _ { \operatorname* { m i n } } , \alpha _ { \operatorname* { m a x } } ] \cap [ 0 , \beta ^ { * } - 1 ]$ , then there exists a positive constant $C$ such that

$$
\mathbb { E } \left[ d _ { \gamma } ( \widehat { \mu } ^ { \dagger } , \mu ^ { * } ) \right] \leq C \left( \frac { n } { \log n } \right) ^ { - \frac { 1 } { 2 } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha ^ { * } + \gamma } { 2 \alpha ^ { * } + d } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \gamma \beta ^ { * } } { d } } .
$$

# 4 Proof of Main Results

In this section, we prove the main results in Theorem 1 and Theorem 2. Proofs of other theorems and technical details are provided in the supplement.

# 4.1 Proof of minimax lower bound in Theorem 1

We use the standard Fano’s method and Le Cam’s method [Yu, 1997, Wainwright, 2019] to establish the minimax lower bound by identifying a subset of distributions within the considered distribution family $\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ that are statistically hard to distinguish. In a nutshell, the term $n ^ { - \frac { \gamma \beta } { d } }$ in the lower bound is obtained by fixing a smooth distribution $\nu _ { 0 }$ on $\mathbb { R } ^ { d }$ and consider a class of $\beta$ -smooth generative maps $G$ whose pushforward measures

$G _ { \# } \nu _ { 0 }$ constitute the candidate “hardest” distribution subset. Since the generative map $G$ determines the position and shape of the supporting submanifold, the term $n ^ { - \frac { \gamma \beta } { d } }$ reflects the statistical hardness of estimating an unknown $\beta$ -smooth submanifold. In contrast, the term $n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { 1 } { 2 } }$ in the lower bound is obtained by fixing the submanifold to be a $d$ -dimensional sphere $S ^ { d }$ (or any other smooth compact submanifold) and consider those distributions whose probability density functions $f$ relative to the volume measure of $S ^ { d }$ are α-smooth functions on the manifold, or f ∈ Cα(Sd). Therefore, the term n− α+γ2α+d ∨ n− 12 reflects the statistical hardness of estimating an unknown $\alpha$ -smooth density as if the submanifold is known.

# 4.1.1 Lower bound of n− γβd

Under the assumption that $\beta > 1$ , we only need to consider $\gamma \in [ 0 , 1 )$ . To see this, we show that otherwise $n ^ { - \frac { \gamma \beta } { d } }$ is always dominated by the other two terms $n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { 1 } { 2 } }$ in the minimax lower bound. In fact, if $\gamma \geq d / 2$ , then by $\beta > 1$ , we have $n ^ { - \frac { \gamma \beta } { d } } \leq n ^ { - \frac { 1 } { 2 } }$ ; if $1 \leq \gamma < d / 2$ , then using $\alpha \le \beta - 1$ we obtain the following sequence of inequalities

$$
n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } } \geq n ^ { - { \frac { \beta - 1 + \gamma } { 2 ( \beta - 1 ) + d } } } \geq n ^ { - { \frac { \beta - 1 + \gamma } { d } } } \geq n ^ { - { \frac { \gamma \beta } { d } } } ,
$$

where the last inequality is due to $\gamma \beta - ( \beta - 1 + \gamma ) = ( \beta - 1 ) ( \gamma - 1 ) \geq 0$ . Thus we focus on $\gamma \in [ 0 , 1 )$ below.

As mentioned before, we will construct a subset of distributions that are statistically hard to distinguish in the sense that their KL divergences to one same distribution (their average) is bounded by constant, while their mutual $d _ { \gamma }$ distances are at least $O \big ( n ^ { - \frac { \gamma \beta } { d } } \big )$ , s o that we may apply the standard reduction argument by reducing the estimation problem into a multiple testing problem, and use the Fano’s lemma (see for example, proposition 15.12 of Wainwright [2019]) to bound the multiple testing error from below. Specifically, let $\mathcal { M } _ { 0 } = \mathbb { S } _ { 2 } ^ { d } \times \mathbf { 0 } _ { D - d - 1 } = \left\{ x \in \mathbb { R } ^ { D } : \| x _ { 1 : ( d + 1 ) } \| ^ { 2 } = 2 \right.$ , $x _ { ( d + 2 ) : D } = { \bf 0 } _ { D - d - 1 } \}$ denote a $d$ - dimensional sphere with radius $\sqrt { 2 }$ embedded in $\mathbb { R } ^ { D }$ . Let $\mu _ { 0 }$ be the uniform distribution over $\mathcal { M } _ { 0 }$ , that is, the distribution whose probability density function relative to the volume measure of $\mathcal { M } _ { 0 }$ is constant, say $C ^ { - 1 }$ . Our constructed subset of “hardest” distributions is obtained by perturbing the support of $\mu _ { 0 }$ via adding small bumps, as summarized in the following lemma.

Lemma 1 (Hardest instances via manifold perturbation). Assume $\gamma < 1$ and $\beta > 1$ . There exist $H$ distributions $\{ \mu _ { h } \} _ { h = 1 } ^ { H } \subset \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ with $\log H \geq 4 n$ based on perturbing $\mu _ { 0 }$ such that:

1. $D _ { \mathrm { K L } } ( \mu _ { h } | | \bar { \mu } ) \leq \log 2$ holds for each $h \in [ H ]$ , where $\bar { \mu } = H ^ { - 1 } \sum _ { h = 1 } ^ { H } \mu _ { h }$ is the averaged distribution;

2. there exists a constant c only depending on $( d , \gamma )$ such that for any distinct pair

$$
h , \ell \in [ H ] , d _ { \gamma } ( \mu _ { h } , \mu _ { \ell } ) \geq c n ^ { - \frac { \gamma \beta } { d } } .
$$

Note that since the $\mu _ { h }$ ’s have non-overlapping supports, it is inevitable to consider the KL divergence between $\mu _ { h }$ and $\mu$ in property 1 of the lemma — $\mu _ { h }$ is absolutely continuous with respect to $\mu$ while the pairwise KL diverges, i.e. $D _ { \mathrm { K L } } ( \mu _ { h } \vert \vert \mu _ { \ell } ) = \infty$ for $h \neq \ell$ . Fortunately, this issue will not affect the application of Fano’s lemma. A proof of this lemma is provided in Section D.1.1 in the supplement. The construction of $\mu _ { h }$ is based on gluing two distributions together (any compact submanifold requires at least two patches to cover): the first part is a measure over a perturbed manifold of the upper area $\widetilde { \mathcal { M } } _ { 0 } \ : = \ : \left\{ x \in \mathbb { R } ^ { D } : x _ { 1 : d } \in \mathbb { B } _ { 1 } ^ { d } \right.$ , $x _ { d + 1 } = \sqrt { 2 - \| x _ { 1 : d } \| ^ { 2 } }$ , $x _ { ( d + 2 ) : D } = { \bf 0 } _ { D - d - 1 } \}$ of the sphere $\mathcal { M } _ { 0 }$ ; and the second part is the restriction of $\mu _ { 0 }$ onto the remaining spherical cap $\mathcal { M } _ { 0 } \backslash \widetilde { \mathcal { M } } _ { 0 }$ (see Figure 2 for an illustration). The measure in the first part is constructed via generative modeling where we fix a smooth distribution $\nu _ { 0 }$ over the $d$ -dimensional unit ball $\mathbb { B } _ { 1 } ^ { d }$ and construct the measure as the pushforward measure through a generative map. The generative map is constructed by adding small bumps to the fixed generative map $G _ { 0 } : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , $z \mapsto \left( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , \mathbf { 0 } _ { D - d - 1 } \right)$ with $[ G _ { 0 } ] _ { \# } \nu _ { 0 }$ being the uniform distribution over $\widetilde { \mathcal { M } } _ { 0 }$ , or the restriction of $\mu _ { 0 }$ over $\widetilde { \mathcal { M } } _ { 0 }$ . Property 1 in Lemma 1 can be satisfied by controlling the size of the bumps; and property 2 can be satisfied by maximally spreading the bumps to different locations on $\widetilde { \mathcal { M } } _ { 0 }$ .

![](images/bc5ef0cfce0a1a288915e9ccc99d46cf63a437608cedb2d5d1361b9cb947474d.jpg)  
Figure 2: Upper half of the unperturbed and perturbed manifolds ( $d = 2$ ) are shown; and the lower hemispheres are not displayed in the figures.

Return to the proof of the lower bound. We apply part 1 of Lemma 1 and Fano’s lemma (proposition 15.12 of Wainwright [2019]) to obtain that for any estimator $\widehat { h }$ based on i.i.d. observations $X _ { 1 : n }$ from $\mu _ { h }$ , the multiple testing error probability satisfies

$$
\mathbb { P } ( \widehat { h } \neq h ) \geq 1 - \frac { \log 2 + \frac { n } { H } \sum _ { h = 1 } ^ { H } D _ { \mathrm { K L } } ( \mu _ { h } | | \bar { \mu } ) } { \log H } \geq \frac { 1 } { 2 } .
$$

By using part 2 of Lemma 1, we further obtain

$$
\operatorname* { i n f } _ { \widehat { h } } \operatorname* { s u p } _ { h \in H } \mathbb { E } \big [ d _ { \gamma } ( \mu _ { \widehat { h } } , \mu _ { h } ) \big ] \geq \frac { 1 } { 2 } \operatorname* { i n f } _ { \stackrel { \ell \in [ H ] } { h \not = \ell } } d _ { \gamma } ( \mu _ { h } , \mu _ { \ell } ) \geq \frac { c } { 2 } n ^ { - \frac { \gamma \beta } { d } } .
$$

Finally, since $d _ { \gamma }$ satisfies the triangle inequality, by a standard reduction argument [Yang and Barron, 1999] from estimation to multiple testing, we have

$$
\operatorname* { i n f } _ { \widehat { \mu } } \operatorname* { s u p } _ { \mu \in { \cal P } ^ { * } } \mathbb { E } \big [ d _ { \gamma } ( \widehat { \mu } , \mu ) \big ] \geq \frac { 1 } { 2 } \operatorname* { i n f } _ { \widehat { h } } \operatorname* { s u p } _ { h \in { \cal H } } \mathbb { E } \big [ d _ { \gamma } ( \mu _ { \widehat { h } } , \mu _ { h } ) \big ] \geq \frac { c } { 4 } n ^ { - \frac { \gamma \beta } { d } } .
$$

# 4.2 Lower bound of $\textstyle n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$

Liang [2020] prove a lower bound $n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { 1 } { 2 } }$ for the minimax rate of $\alpha$ -smooth density estimation on $[ 0 , 1 ] ^ { d }$ under the adversarial loss $d _ { \gamma }$ . Our proof of lower bounds $\textstyle n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$ and $n ^ { - \frac { 1 } { 2 } }$ in this and next subsections are technically similar to that in [Liang, 2020] for proving nonparametric density estimation lower bounds based on constructing a subset of bumpy functions that are statistically hard to distinguish with respect to the concerned distance metric [Tsybakov, 2009], which is $d _ { \gamma }$ in our context. However, although the lower bounds appear the same, there is a non-trivial extension in our proof — we need to construct singular distributions supported on a compact (therefore boundariless) manifold instead of the ambient space which is flat. This requires us to use a carefully constructed generative map to: 1. pushforward bumpy distributions from $\mathbb { R } ^ { d }$ to $\mathbb { R } ^ { D }$ and to verify the resulting distributions to admit smooth density functions with respect to the volume measure of the manifold; 2. lift the discriminator in $\mathbb { R } ^ { d }$ discriminating the bumpy functions to one in the ambient space $\mathbb { R } ^ { D }$ discriminating singular distributions supporting on the manifold; both of which complicate the proof. The lemma below summarizes the constructed subset of “hardest” distributions obtained by perturbing the distribution $\mu _ { 0 }$ via adding small bumps on the submanifold $\mathcal { M } _ { 0 }$ (both defined in Section 4.1).

Lemma 2 (Hardest instances via density perturbation). Assume $\beta > 1$ . Then for any constant $b > 0$ , there exist $H ^ { \prime }$ distributions $\{ \mu _ { h } \} _ { h = 1 } ^ { H ^ { \prime } } \subset \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ with $\log H ^ { \prime } \geq$ $b ^ { d } n ^ { \frac { d } { 2 \alpha + d } }$ based on perturbing $\mu _ { 0 }$ such that for constants $( c _ { 1 } , c _ { 2 } )$ only depending on $d$ :

1. $D _ { \mathrm { K L } } ( \mu _ { h } \| \mu _ { \ell } ) \le c _ { 1 } b ^ { - 2 \alpha } n ^ { - \frac { 2 \alpha } { 2 \alpha + d } }$ holds for any distinct pair $h , \ell \in [ H ^ { \prime } ]$ ;   
2. $d _ { \gamma } ( \mu _ { h } , \mu _ { \ell } ) \geq c _ { 2 } b ^ { - ( \alpha + \gamma + d ) } n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } }$ holds for any distinct pair $h , \ell \in [ H ^ { \prime } ]$ .

A proof of this lemma is provided in Section D.1.2 in the supplement. The rest proof in this subsection is similar to that in Section 4.1.1. We apply above lemma and Fano’s

lemma to obtain

$$
\begin{array} { r l } & { \underset { \hat { \mu } _ { \hat { \mu } \in \mathcal { P } ^ { * } } } { \mathrm { n f ~ s u p ~ } } \mathbb { E } \left[ d _ { \gamma } ( \widehat { \mu } , \mu ) \right] \geq \frac { 1 } { 2 } \underset { h , \varepsilon \in [ \mu ] } { \operatorname* { i n f } } d _ { \gamma } ( \mu _ { h } , \mu _ { \ell } ) \cdot \left( 1 - \frac { \log 2 + \frac { n } { H ^ { 2 } } \sum _ { h , \ell = 1 } ^ { H } D _ { \mathrm { K L } } ( \mu _ { h } | | \mu _ { \ell } ) } { \log H } \right) } \\ & { \qquad \geq \frac { c _ { 2 } } { 2 } b ^ { - ( \alpha + \gamma + d ) } n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \cdot \left( 1 - \frac { \log 2 + c _ { 1 } b ^ { - 2 \alpha } n ^ { \frac { \alpha } { 2 \alpha + d } } } { b ^ { d } n ^ { \frac { \alpha } { 2 \alpha + d } } } \right) \geq c ^ { \prime } n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } , } \end{array}
$$

where the last step holds by choosing a sufficiently large constant $b$ .

# 4.3 Lower bound of $n ^ { - { \frac { 1 } { 2 } } }$

The $n ^ { - { \frac { 1 } { 2 } } }$ lower bound can be obtained by Le Cam’s method of reducing the estimation problem into a two-point hypothesis testing problem [Yu, 1997, Wainwright, 2019]. Our proof is based on adapting the proof of Liang [2020] for density estimation on $[ 0 , 1 ] ^ { d }$ to distribution estimation on the previously defined $d$ -dimensional sphere $\mathcal { M } _ { 0 }$ embedded in $\mathbb { R } ^ { D }$ .

The proof relies on the existence of two distributions $\mu _ { 0 }$ (uniform distribution) and $\mu _ { 1 }$ supported on $\mathcal { M } _ { 0 }$ with the following properties. For two distributions $\nu$ and $\mu$ such that $\nu$ is absolutely continuous with respect to $\mu$ , the chi-squared distance from $\nu$ to $\mu$ is defined as $\begin{array} { r } { d _ { \chi ^ { 2 } } ( \nu , \mu ) = \int \left( \frac { \mathrm { d } \nu } { \mathrm { d } \mu } - 1 \right) ^ { 2 } \mathrm { d } \mu } \end{array}$ .

Lemma 3 (Perturbation of uniform distribution). There exists two distributions $\mu _ { 0 }$ and $\mu _ { 1 }$ , both belonging to $\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ such that: 1. $\mu _ { 1 }$ is absolutely continuous with respect to $\mu _ { 0 }$ ; $\boldsymbol { \mathcal { Z } }$ . $d _ { \chi ^ { 2 } } ( \mu _ { 1 } , \mu _ { 0 } ) \leq { \textstyle \frac { 1 } { n } }$ ; 3. $\begin{array} { r } { d _ { \gamma } ( \mu _ { 1 } , \mu _ { 0 } ) \geq \frac { c } { \sqrt { n } } } \end{array}$ , where $c _ { 1 }$ is a constant only depending on $( d , \alpha , \gamma )$ .

A proof of this lemma is provided in Section D.1.3 in the supplement. For a distribution $\mu$ , let $\mu ^ { \otimes n }$ denote its $n$ -fold self-product. From the lemma and the tensorization property of $d _ { \chi ^ { 2 } }$ , we have

$$
d _ { \chi ^ { 2 } } \big ( \mu _ { 1 } ^ { \otimes n } , \mu _ { 0 } ^ { \otimes n } \big ) = \big ( 1 + d _ { \chi ^ { 2 } } ( \mu _ { 1 } , \mu _ { 0 } ) \big ) ^ { n } - 1 \leq \Big ( 1 + \frac { 1 } { n } \Big ) ^ { n } - 1 \leq e - 1 .
$$

Therefore, by Pinsker’s inequality and $D _ { \mathrm { K L } } ( \mu | | \nu ) \leq d _ { \chi ^ { 2 } } ( \mu , \nu )$ , we obtain that their total variation distance satisfies $\begin{array} { r } { d _ { \mathrm { T V } } \big ( \mu _ { 1 } ^ { \otimes n } , \mu _ { 0 } ^ { \otimes n } \big ) \leq \sqrt { \frac { e - 1 } { 2 } } } \end{array}$ . Finally, by Le Cam’s bound (see for example, Lemma 15.9 of Wainwright [2019]) we obtain

$$
\operatorname* { i n f } _ { \hat { \mu } } \operatorname* { s u p } _ { \mu \in \mathcal { P } ^ { * } } \mathbb { E } \big [ d _ { \gamma } ( \widehat { \mu } , \mu ) \big ] \geq d _ { \gamma } ( \mu _ { 1 } , \mu _ { 0 } ) \Big ( 1 - \sqrt { \frac { e - 1 } { 2 } } \Big ) \geq \Big ( 1 - \sqrt { \frac { e - 1 } { 2 } } \Big ) \frac { c } { \sqrt { n } } ,
$$

where the last step is due to Lemma 3.

# 4.4 Proof of minimax upper bound

We provide in this section the proof of the more general upper bound in Theorem 2. Lemma 15 in Appendix E.3 shows that $S ^ { * }$ is included in the approximation family $S ^ { \mathrm { a p } }$ . Recall that from the basic inequality (9), it suffices to show that

$$
\operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } \big [ f ( X ) \big ] - \widehat { \mathcal { I } } ( f ) \Big | \leq C \Big ( \frac { n } { \log n } \Big ) ^ { - \frac 1 2 } \vee \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \gamma \beta } { d } } ,
$$

where the regularized surrogate $\widehat { \mathcal { I } } ( f ) = \widehat { \mathcal { I } } _ { l } ( f ) + \widehat { \mathcal { I } } _ { h } ( f ) + \widehat { \mathcal { I } } _ { s } ( f )$ for approximating $\mathbb { E } _ { \mu ^ { * } } [ f ( X ) ]$ is composed of three terms:

$$
\widehat { \mathcal { T } } _ { l } ( \boldsymbol { f } ) = \sum _ { m = 1 } ^ { M } \widehat { \mathcal { T } } _ { m , l } ( \boldsymbol { f } ) , \quad \widehat { \mathcal { T } } _ { h } ( \boldsymbol { f } ) = \sum _ { m = 1 } ^ { M } \widehat { \mathcal { T } } _ { m , h } ( \boldsymbol { f } ) \quad \mathrm { a n d } \quad \widehat { \mathcal { T } } _ { s } ( \boldsymbol { f } ) = \sum _ { m = 1 } ^ { M } \widehat { \mathcal { T } } _ { m , s } ( \boldsymbol { f } ) ,
$$

where for each $m \in \lfloor M \rfloor$ corresponding to the index in the partition of unity, the triplet $( \widehat { \mathcal { I } } _ { m , l } ( f ) , \widehat { \mathcal { I } } _ { m , h } ( f ) , \widehat { \mathcal { I } } _ { m , s } ( f ) )$ is defined in (12) when ${ \widehat { p } } _ { m } > { \sqrt { \frac { \log n } { n } } }$ and otherwise we set $\widehat { \mathcal { T } } _ { m , l } ( f ) = \widehat { \mathcal { T } } _ { m , h } ( f ) = \widehat { \mathcal { T } } _ { m , s } ( f ) = 0$ . In particular, $\widehat { \mathcal { I } } _ { l } ( f )$ estimates the expectation of $\Pi _ { J } f$ that collects the low frequency components in the wavelet expansion of $f$ ; $\widehat { \mathcal { I } } _ { h } ( f )$ estimates the expectation of $\Pi _ { J } ^ { \perp } f$ that collects the high frequency component; and $\widehat { \mathcal { I } } _ { s } ( f )$ corresponds to a high-order smoothness correction due to the submanifold estimation error from the local coordinate map (and its inverse) estimator $\bigl ( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } \bigr )$ for $m \in [ M ]$ , defined in (11). We may similarly decompose the target functional into three terms as $\mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] = \mathcal { I } _ { l } ( f ) + \mathcal { I } _ { h } ( f ) + \mathcal { I } _ { s } ( f )$ , where

$$
\begin{array} { l l } { \displaystyle \mathcal { T } _ { l } ( f ) = \sum _ { m = 1 } ^ { M } \mathcal { T } _ { m , l } ( f ) } & { \mathrm { w i t h } \mathcal { T } _ { m , l } ( f ) = \mathbb { E } _ { \mu ^ { * } } \big [ \Pi _ { J } f \big ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \big ) \cdot \rho _ { m } ( X ) \big ] , } \\ { \displaystyle \mathcal { T } _ { h } ( f ) = \sum _ { m = 1 } ^ { M } \mathcal { T } _ { m , h } ( f ) } & { \mathrm { w i t h } \mathcal { T } _ { m , h } ( f ) = \mathbb { E } _ { \mu ^ { * } } \big [ \Pi _ { J } ^ { \perp } f \big ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \big ) \cdot \rho _ { m } ( X ) \big ] , } \\ { \displaystyle \mathcal { T } _ { s } ( f ) = \sum _ { m = 1 } ^ { M } \mathcal { T } _ { m , l } ( f ) } & { \mathrm { w i t h } \mathcal { T } _ { m , l } ( f ) = \mathbb { E } _ { \mu ^ { * } } \big [ f ( X ) \cdot \rho _ { m } ( X ) \big ] - \mathbb { E } _ { \mu ^ { * } } \big [ f \big ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \big ) \cdot \rho _ { m } ( X ) \big ] . } \end{array}
$$

Let $\begin{array} { r } { \mathbb { M } = \{ m \in [ M ] : \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } \} } \end{array}$ and recall $\begin{array} { r } { \widehat { \mathbb { M } } = \{ m \in [ M ] : \widehat { p } _ { m } \geq \sqrt { \frac { \log n } { n } } \} } \end{array}$ in the following proofs, we only consider $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$ . In fact, by applying Bernstein’s inequality for a binomial random variable and a union bound argument, for any constant $c$ , there exists a constant $n _ { 0 }$ such that when $n \geq n _ { 0 }$ , it holds with probability at least $1 - n ^ { - c }$ that for any $m \in [ M ]$ such that $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) < \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ or ${ \widehat { p } } _ { m } < { \sqrt { \frac { \log n } { n } } }$ ， ,

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] - \widehat { \mathcal { T } } _ { m } ( f ) \Big | = \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] \right| \leq 2 \sqrt { \frac { \log n } { n } } ,
$$

see Appendix D.2 for further detail. The following three lemmas show that $\widehat { \mathcal { I } } _ { m , l }$ , $\widehat { \mathcal { I } } _ { m , h }$ and $\widehat { \mathcal { I } } _ { m , s }$ are good estimators for ${ \mathcal { I } } _ { m , l }$ , $\mathcal { J } _ { m , h }$ and $\mathcal { I } _ { m , s }$ , respectively, for each $m \in \mathbb { M } \cap \widehat { \mathbb { M } }$ .

Lemma 4 (Low frequency components). With probability at least $1 - n ^ { - c }$ , for any $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$ , the functional $\mathcal { \hat { I } } _ { m , l } : C ^ { \gamma } ( \mathbb { R } ^ { D } )  \mathbb { R }$ defined in (12a) satisfies

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| { \widehat { \mathcal { I } } } _ { m , l } ( f ) - { \mathcal { I } } _ { m , l } ( f ) \right| \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } .
$$

Lemma 5 (High frequency components). With probability at least $1 - n ^ { - c }$ , for any $m \in \mathbb { M } \cap \widehat { \mathbb { M } }$ , the functional ${ \widehat { \mathcal { T } } } _ { m , h } : C ^ { \gamma } ( \mathbb { R } ^ { D } ) \to \mathbb { R }$ defined in (12b) satisfies

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \widehat { \mathcal { I } } _ { m , h } ( f ) - \mathcal { I } _ { m , h } ( f ) \right| \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } .
$$

Lemma 6 (Smoothness correction). With probability at least $1 - n ^ { - c }$ , for any $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$ , the functional $\widehat { \mathcal { T } } _ { m , s } : C ^ { \gamma } ( \mathbb { R } ^ { D } ) \to \mathbb { R }$ defined in (12c) satisfies

$$
\operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( { \mathbb { R } } ^ { D } ) } \big | \widehat { \mathcal { I } } _ { m , s } ( f ) - { \mathcal { I } } _ { m , s } ( f ) \big | \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta } { d } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \beta - 1 } { d } } .
$$

Proofs of these lemmas are provided in Sections D.2.2, D.2.3 and D.2.4 in the supplementary material. It is worthwhile mentioning that an important intermediate result used in the proof of Lemma 6 is the following lemma, which characterizes the estimation error of $\big ( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } \big )$ defined in step 1 of submanifold estimation in Section 3.1. Its proof, which is provided in Section D.2.1 in the supplementary material, is quite technical and involved, and uses many techniques from empirical process theory.

Lemma 7 (Submanifold estimation). For any fixed constant $\eta > 0$ , it holds with probability at least $1 - n ^ { - c }$ that,

$$
\mathbb { E } _ { \mu ^ { * } } \left[ \left\| X - \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \right\| _ { 2 } ^ { \eta } \rho _ { m } ( X ) \right] \leq C \left( \frac { \log n } { n } \right) \vee \left( \frac { \log n } { n } \right) ^ { \frac { \eta \beta } { d } } , \quad \forall m \in \mathbb { M } ,
$$

where the expectation is taken with respect to the randomness in $X$ (not the randomness in $\widehat { G } _ { [ m ] }$ and $\widehat { Q } _ { [ m ] , }$ .

By combining Lemmas 4, 5 and 6, we obtain

$$
\operatorname* { l p } _ { \gamma _ { \mathbb { R } ^ { D } } } \left. \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - { \widehat { \mathcal { I } } } ( f ) \right. \leq C M \left( { \frac { n } { \log n } } \right) ^ { - { \frac { 1 } { 2 } } } \vee \left( { \frac { n } { \log n } } \right) ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } } \vee \left( { \frac { n } { \log n } } \right) ^ { - { \frac { \gamma \beta } { d } } } \vee \left( { \frac { n } { \log n } } \right) ^ { \frac { 1 } { 2 } }
$$

γ+β−1   
Finally, under the assumption that $\beta \geq \alpha - 1$ , the last term $\left( { \frac { n } { \log n } } \right) ^ { - { \frac { \gamma + \beta - 1 } { d } } }$ above is always α+γ   
dominated by the second term $\left( { \frac { n } { \log n } } \right) ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$ , which completes the proof of the claimed

# 5 Discussion

In this paper, we studied the minimax rate of distribution estimation on unknown submanifold under adversarial losses, covering cases where the manifold, the density, and the discriminator class have various Hölder regularities. In conclusion, the minimax rate shows that the curse of dimensionality can be overcome for data with low intrinsic dimension, smooth density and regular support, which partly explains the empirical successes of generative model based approaches for generating realistic objects in real applications. Apart from the Hölder class, some other function spaces, such as Sobolev class and reproducing kernel Hilbert space may also be considered for the discriminator class when defining the adversarial loss, which we leave for future research. Moreover, the rate-optimal procedure developed in this study is mainly for the theoretical purpose of proving a minimax upper bound, and a modification towards it to make it computationally feasible may also be left to our future work.

# References

Theory of Function Spaces III. Birkhäuser Basel, Basel, 2006. URL https://link. springer.com/book/10.1007/3-7643-7582-5.   
E. Aamari and C. Levrard. Nonasymptotic rates for manifold, tangent space and curvature estimation. The Annals of Statistics, 47(1):177 – 204, 2019. doi: 10.1214/18-AOS1685. URL https://doi.org/10.1214/18-AOS1685.   
M. Arjovsky and L. Bottou. Towards principled methods for training generative adversarial networks, 2017.   
M. Arjovsky, S. Chintala, and L. Bottou. Wasserstein gan, 2017.   
O. U. Aydin, A. A. Taha, A. Hilbert, A. A. Khalil, I. Galinovic, J. B. Fiebach, D. Frey, and V. I. Madai. On the usage of average hausdorff distance for segmentation performance assessment: hidden error when used for ranking. European Radiology Experimental, 2021. doi: 10.1186/s41747-020-00200-2. URL https: //doi.org/10.1186/s41747-020-00200-2.   
C. Berenfeld and M. Hoffmann. Density estimation on an unknown submanifold. Electronic Journal of Statistics, 15(1):2179 – 2223, 2021. doi: 10.1214/21-EJS1826. URL https: //doi.org/10.1214/21-EJS1826.

G. Biau, B. Cadre, M. Sangnier, and U. Tanielian. Some theoretical properties of GANS. The Annals of Statistics, 48(3):1539 – 1566, 2020. doi: 10.1214/19-AOS1858. URL https://doi.org/10.1214/19-AOS1858.

P. J. Bickel and B. Li. Local polynomial regression on unknown manifolds. In Complex datasets and inverse problems, pages 177–186. Institute of Mathematical Statistics, 2007.

S. Bouzebda and S. Didi. Multivariate wavelet density and regression estimators for stationary and ergodic discrete time processes: Asymptotic results. Communications in Statistics - Theory and Methods, 46(3):1367–1406, 2017. doi: 10.1080/03610926.2015. 1019144. URL https://doi.org/10.1080/03610926.2015.1019144.   
A. Brock, J. Donahue, and K. Simonyan. Large scale gan training for high fidelity natural image synthesis, 2018.   
L. A. Caffarelli. Boundary regularity of maps with convex potentials–ii. Annals of Mathematics, 144(3):453–496, 1996. ISSN 0003486X. URL http://www.jstor.org/ stable/2118564.   
C. Caillerie, F. Chazal, J. Dedecker, and B. Michel. Deconvolution for the Wasserstein metric and geometric inference. Electronic Journal of Statistics, 5(none):1394 – 1423, 2011. doi: 10.1214/11-EJS646. URL https://doi.org/10.1214/11-EJS646.   
F. Camastra and A. Vinciarelli. Estimating the intrinsic dimension of data with a fractalbased method. IEEE Transactions on pattern analysis and machine intelligence, 24(10): 1404–1407, 2002.   
K. M. Carter, R. Raich, and A. O. Hero III. On local intrinsic dimension estimation and its applications. IEEE Transactions on Signal Processing, 58(2):650–663, 2009.   
O. Cornea, G. Lupton, J. Oprea, D. Tanré, et al. Lusternik-Schnirelmann category. Number 103. American Mathematical Soc., 2003.   
M. P. Do Carmo and J. Flaherty Francis. Riemannian geometry, volume 6. Springer, 1992.   
J. Eldering. Normally Hyperbolic Invariant Manifolds: The Noncompact Case. Atlantis Press, Paris, 2013.   
L. C. Evans. Partial differential equations. American Mathematical Society, Providence, R.I., 2010.   
J. Fan and R. Li. Variable selection via nonconcave penalized likelihood and its oracle properties. Journal of the American statistical Association, 96(456):1348–1360, 2001.   
A. M. Farahmand, C. Szepesvári, and J.-Y. Audibert. Manifold-adaptive dimension estimation. In Proceedings of the 24th international conference on Machine learning, pages 265–272, 2007.   
R. H. Fox. On the lusternik-schnirelmann category. Annals of Mathematics, 42(2):333–370, 1941.   
C. R. Genovese, M. Perone-Pacifico, I. Verdinelli, and L. Wasserman. Manifold estimation and singular deconvolution under Hausdorff loss. The Annals of Statistics, 40(2):941 – 963, 2012a. doi: 10.1214/12-AOS994. URL https://doi.org/10.1214/12-AOS994.   
C. R. Genovese, M. Perone-Pacifico, I. Verdinelli, and L. Wasserman. Minimax manifold estimation. Journal of Machine Learning Research, 13:1263–1291, 2012b.   
E. Giné and R. Nickl. Mathematical Foundations of Infinite-Dimensional Statistical Models. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2015. doi: 10.1017/CBO9781107337862.   
I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio. Generative adversarial networks, 2014.   
A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Schölkopf, and A. Smola. A kernel two-sample test. The Journal of Machine Learning Research, 13(1):723–773, 2012.   
W. Hoeffding. Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, 58(301):13–30, 1963. doi: 10.1080/01621459.1963. 10500830. URL https://www.tandfonline.com/doi/abs/10.1080/01621459.1963. 10500830.   
J.-C. Hütter and P. Rigollet. Minimax estimation of smooth optimal transport maps, 2020.   
J. M. Lee. Smooth manifolds. In Introduction to Smooth Manifolds, pages 1–31. Springer, 2013.   
O. Lepskii. On a problem of adaptive estimation in gaussian white noise. Theory of Probability & Its Applications, 35(3):454–466, 1991.   
E. Levina and P. Bickel. Maximum likelihood estimation of intrinsic dimension. Advances in neural information processing systems, 17, 2004.   
C. Li, W. Chang, Y. Cheng, Y. Yang, and B. Póczos. MMD GAN: towards deeper understanding of moment matching network. CoRR, abs/1705.08584, 2017. URL http://arxiv.org/abs/1705.08584.

Y. Li, K. Swersky, and R. Zemel. Generative moment matching networks, 2015.

T. Liang. How well generative adversarial networks learn distributions, 2020.

C. Loader. Local regression and likelihood. Springer Science & Business Media, 2006.

Y. M. Lui. Advances in matrix manifolds for computer vision. Image and Vision Computing, 30(6-7):380–388, 2012.

Y. Mroueh, C.-L. Li, T. Sercu, A. Raj, and Y. Cheng. Sobolev gan, 2017.

A. Müller. Integral probability metrics and their generating classes of functions. Advances in Applied Probability, 29(2):429–443, 1997.

A. Ozakin and A. Gray. Submanifold density estimation. In Y. Bengio, D. Schuurmans, J. Lafferty, C. Williams, and A. Culotta, editors, Advances in Neural Information Processing Systems, volume 22. Curran Associates, Inc., 2009. URL https://proceedings. neurips.cc/paper/2009/file/2ac2406e835bd49c70469acae337d292-Paper.pdf.

E. Parzen. On Estimation of a Probability Density Function and Mode. The Annals of Mathematical Statistics, 33(3):1065 – 1076, 1962. doi: 10.1214/aoms/1177704472. URL https://doi.org/10.1214/aoms/1177704472.

M. Raič. A multivariate Berry–Esseen theorem with explicit constants. Bernoulli, 25 (4A):2824–2853, Nov 2019. ISSN 1350-7265. doi: 10.3150/18-bej1072. URL http: //dx.doi.org/10.3150/18-BEJ1072.

S. Singh, A. Uppal, B. Li, C.-L. Li, M. Zaheer, and B. Póczos. Nonparametric density estimation under adversarial losses, 2018.

E. M. Stein. Singular Integrals and Differentiability Properties of Functions (PMS-30), Volume 30. Princeton university press, 2016.

M. H. Stone. The generalized weierstrass approximation theorem. Mathematics Magazine, 21(4):167–184, 1948. ISSN 0025570X, 19300980. URL http://www.jstor.org/stable/ 3029750.

L. Terradot, N. Durnell, M. Li, M. Li, J. Ory, A. Labigne, P. Legrain, F. Colland, and G. Waksman. Biochemical characterization of protein complexes from the helicobacter pylori protein interaction map: strategies for complex formation and evidence for novel

interactions within type iv secretion systems. Molecular & Cellular Proteomics, 3(8): 809–819, 2004.   
R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (Methodological), 58(1):267–288, 1996.   
I. Tolstikhin, B. K. Sriperumbudur, and K. Muandet. Minimax estimation of kernel mean embeddings. The Journal of Machine Learning Research, 18(1):3002–3048, 2017.   
I. Tolstikhin, O. Bousquet, S. Gelly, and B. Schoelkopf. Wasserstein auto-encoders, 2019.   
A. B. Tsybakov. Introduction to Nonparametric Estimation. Springer New York, New York, NY, 2009.   
A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu. Wavenet: A generative model for raw audio, 2016.   
C. Villani. Optimal Transport: Old and New. Springer Berlin Heidelberg, Berlin, Heidelberg, 2009.   
M. J. Wainwright. High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2019. doi: 10.1017/9781108627771.   
Y. Yang and A. Barron. Information-theoretic determination of minimax rates of convergence. Annals of Statistics, pages 1564–1599, 1999.   
Y. Yang and D. B. Dunson. Bayesian manifold regression. The Annals of Statistics, 44(2): 876–905, 2016.   
Z.-H. You, Y.-K. Lei, J. Gui, D.-S. Huang, and X. Zhou. Using manifold embedding for assessing and predicting protein interactions from high-throughput experimental data. Bioinformatics, 26(21):2744–2751, 2010.   
B. Yu. Assouad, fano, and le cam. In Festschrift for Lucien Le Cam, pages 423–435. Springer, 1997.   
C.-H. Zhang. Nearly unbiased variable selection under minimax concave penalty. The Annals of statistics, 38(2):894–942, 2010.   
S. Zhao, J. Song, and S. Ermon. Infovae: Information maximizing variational autoencoders, 2018.

# Appendix

Notations: We adopt the notations in the manuscript, and further introduce the following additional notations for the technical proofs. For two symmetric matrices $A$ and $B$ , we use $A \preccurlyeq B$ to mean that $B - A$ is a positive semi-definite matrix. We use $N ( \mathcal { F } , \widetilde { d } , \epsilon )$ to denote the $\epsilon$ -covering number of function space $\mathcal { F }$ with respect to pseudo-metric $\hat { d }$ . Throughout, $C$ , $c$ , $C _ { 0 }$ , $c _ { 0 }$ , $C _ { 1 }$ , $c _ { 1 }$ , $C _ { 2 }$ , $c _ { 2 } , . . .$ are generically used to denote positive constants whose values might change from one line to another, but are independent from everything else.

# A Wavelet and Besov Function Space

In this section, we give a brief introduction to the wavelet and Besov function Space, and then define the smoothness regularized empirical distribution $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ used in Step 2 of the construction of the minimax-optimal estimator $\widehat { \mu }$ in Section 3.1 based on wavelet expansion.

Let $\phi _ { \mathfrak { M } } \in C ^ { \varsigma } ( \mathbb { R } )$ and $\phi _ { \mathfrak { F } } \in \ C ^ { \zeta } ( \mathbb { R } )$ be a compactly supported wavelet and scaling function, respectively, for example Daubechies wavelets [Bouzebda and Didi, 2017, Hütter and Rigollet, 2020]. This implies that

$$
\begin{array} { r } { \Psi _ { k } ^ { j } = \left\{ \begin{array} { l l } { \psi _ { \mathfrak { F } } ( x - k ) } & { j = 0 , k \in \mathbb { Z } , } \\ { 2 ^ { ( j - 1 ) / 2 } \psi _ { \mathfrak { M } } ( 2 ^ { j - 1 } x - k ) , } & { j \in \mathbb { N } ^ { + } , k \in \mathbb { Z } , } \end{array} \right. } \end{array}
$$

is an orthonormal basis of ${ \mathcal { L } } ^ { 2 } ( \mathbb { R } )$ , where we use $\mathcal { L } ^ { 2 }$ to denote the set of square integrable functions. To obtain a basis of ${ \mathcal { L } } ^ { 2 } ( \mathbb { R } ^ { d } )$ for an integer $d > 1$ , set

$$
{ \mathfrak { G } } = \{ { \mathfrak { F } } , { \mathfrak { M } } \} ^ { d } \backslash \{ ( { \mathfrak { F } } , \dots , { \mathfrak { F } } ) \} .
$$

Then for any multi-index $k \in  { \mathbb { Z } ^ { d } }$ , the level zero basis $\phi _ { k } ^ { \left[ d \right] }$ is obtained by translating the $d$ -fold tensor product $\phi _ { \mathfrak { F } } ^ { \otimes d }$ by $k$ as $\begin{array} { r } { \phi _ { k } ^ { [ d ] } ( x ) = \prod _ { i = 1 } ^ { d } \phi _ { \mathfrak { F } } ( x _ { i } - k _ { i } ) } \end{array}$ for $x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { R } ^ { d }$ , and for any $j \geq 1$ , the level $j$ basis $\{ \psi _ { l j k } ^ { \lfloor d \rfloor } : l \in [ 2 ^ { d } - 1 ] \}$ with translation $k$ is any ordering of the following $2 ^ { d } - 1$ functions,

$$
\psi _ { k } ^ { j , g } ( x ) = 2 ^ { \frac { d ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { d } \phi _ { g _ { i } } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) , \quad \forall g \in \mathfrak { G } .
$$

When no ambiguity arises, we suppress the superscript $[ d ]$ in $\phi _ { k } ^ { [ d ] } ( x )$ and $\psi _ { l j k } ^ { [ d ] } ( x )$ for $x \in \mathbb { R } ^ { d }$ . This gives the orthornormal basis

$$
\Psi _ { k } ^ { j , l } = \left\{ \begin{array} { l l } { \phi _ { k } ( x ) , } & { j = 0 , l = 0 , k \in \mathbb { Z } ^ { d } , } \\ { \psi _ { l j k } ( x ) , } & { j \in \mathbb { N } ^ { + } , l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } . } \end{array} \right.
$$

Then let $1 \leq p , q \leq \infty$ , $s \geq 0$ and let the regularity of the above wavelets satisfy $\begin{array} { r } { \zeta > s \vee ( \frac { 2 d } { p } + \frac { d } { 2 } - s ) } \end{array}$ . We are then ready to define the Besov space $B _ { p , q } ^ { s } ( \mathbb { R } ^ { d } )$ consists of functions $f$ that admits the wavelet expansion

$$
f ( \boldsymbol { x } ) = \sum _ { k \in \mathbb { Z } ^ { d } } b _ { k } \phi _ { k } ( \boldsymbol { x } ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 1 } ^ { \infty } \sum _ { k \in \mathbb { Z } ^ { d } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) .
$$

and equipped with the norm

$$
\| f \| _ { B _ { p , q } ^ { s } } : = \bigg [ \Big ( \sum _ { k \in Z ^ { d } } | b _ { k } | ^ { p } \Big ) ^ { \frac { q } { p } } + \sum _ { j = 1 } ^ { \infty } 2 ^ { j q ( s + \frac { d } { 2 } - \frac { d } { p } ) } \sum _ { l \in [ 2 ^ { d } - 1 ] } \Big ( \sum _ { k \in Z ^ { d } } | f _ { l j k } | ^ { p } \Big ) ^ { \frac { q } { p } } \bigg ] ^ { \frac { 1 } { q } } < \infty .
$$

Moreover, for any positive integer $J$ , we use $\Pi _ { J } f$ to denote the projection of any $f \in$ $B _ { p , q } ^ { s } ( \mathbb { R } ^ { d } )$ onto the first scale $J$ wavelet coefficients, given by

$$
\Pi _ { J } f ( x ) = \sum _ { k \in \mathbb { Z } ^ { d } } b _ { k } \phi _ { k } ( x ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 1 } ^ { J } \sum _ { k \in \mathbb { Z } ^ { d } } f _ { l j k } \psi _ { l j k } ( x )
$$

and $\Pi _ { J } ^ { \perp } f = f - \Pi _ { J } f$ .

The following Theorem collects the relationship between the Besov space and Hölder space.

Theorem 3. (Theorem 1.122 of Tri [2006] and Proposition 4.3.30 of Giné and Nickl [2015]) Let $\alpha > 0$ , if $\alpha$ is not integer, then

$$
C ^ { \alpha } (  { \mathbb { R } } ^ { d } ) = B _ { \infty , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) ;
$$

if $\alpha$ is integer, then

$$
B _ { 1 , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset C ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset B _ { \infty , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) .
$$

Smoothness regularized empirical distribution based on wavelet expansion:

Suppose the target density $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( z )$ of $( \widehat { Q } _ { [ m ] } ) _ { \# } \big ( \rho _ { m } \mu ^ { * } \big )$ is $\alpha$ -smooth (which is true with high probability, see Lemma 11 for further detail), then it has the following wavelet expansion:

$$
\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { \ast } ( z ) = \sum _ { k \in \mathbb { S } } a _ { k } ^ { \widehat { Q } _ { [ m ] } } \phi _ { k } ( z ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { + \infty } \sum _ { k \in \mathbb { S } _ { l j } } \theta _ { l j k } ^ { \widehat { Q } _ { [ m ] } } \psi _ { l j k } ( z ) , \quad \mathrm { w i t h }
$$

$$
\mathbb { S } = \left\{ k \in \mathbb { Z } ^ { d } : \operatorname { s u p p } ( \phi _ { k } ) \cap [ - L , L ] ^ { d } \neq \emptyset \right\} ;
$$

$$
\mathbb { S } _ { l j } = \big \{ k \in \mathbb { Z } ^ { d } : \operatorname { s u p p } ( \psi _ { l j k } ) \cap [ - L , L ] ^ { d } \neq \emptyset \big \} ,
$$

where

$$
\begin{array} { r l } & { a _ { k } ^ { \widehat { Q } _ { [ m ] } } = \mathbb { E } _ { \mu ^ { * } } \left[ \phi _ { k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \right] ; } \\ & { \theta _ { l j k } ^ { \widehat { Q } _ { [ m ] } } = \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \right] . } \end{array}
$$

Here, the expectation is taken with respect to $X \sim \mu ^ { * }$ (not the randomness in $\widehat { Q } _ { [ m ] }$ ). The smoothness regularized estimator $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ corresponds to a truncated empirical version of $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * }$ by truncating the expansion at a finite level $J$ such that $2 ^ { J }$ is the largest integer not exceeding $\left( { \frac { n } { \log n } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ , and replacing the wavelet coefficients with their sample averages,

$$
\widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) = \sum _ { k \in \mathbb { S } } \widetilde { a } _ { k } ^ { \widehat { Q } _ { [ m ] } } \phi _ { k } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { k \in \mathbb { S } _ { l j } } \widetilde { \theta } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } \psi _ { l j k } ( y ) ,
$$

where

$$
\begin{array} { l } { { \displaystyle \widetilde { \boldsymbol { a } } _ { k } ^ { \widehat { Q } _ { [ m ] } } = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \phi _ { k } ( \widehat { Q } _ { [ m ] } ( \boldsymbol { X } _ { i } ) ) \cdot \boldsymbol { \rho } _ { m } ( \boldsymbol { X } _ { i } ) } ; } \\ { { \displaystyle \widetilde { \boldsymbol { \theta } } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( \boldsymbol { X } _ { i } ) ) \cdot \boldsymbol { \rho } _ { m } ( \boldsymbol { X } _ { i } ) } . } \end{array}
$$

Remark 8. Another possible choice of the smoothness regularized empirical distribution $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ is the kernel density estimator (KDE) for $( \widehat { Q } _ { [ m ] } ) _ { \# } \big ( \rho _ { m } \mu ^ { * } \big )$ that is easier to implement in practice. Specifically, we may choose any kernel function $k ( x ) \in C _ { c _ { 1 } } ^ { 1 + \alpha } ( \mathbb { R } )$ over $\mathbb { R }$ such that: (1) $\operatorname { s u p p } ( \bar { k } ( x ) ) \subset [ 0 , 1 ]$ ; (2) $\textstyle \int k ( x ) \mathrm { d } x \ = \ 1$ ; (3) for any $j \in \mathbb { N } ^ { + }$ with $j \ \leq \ \lceil \alpha \rceil$ , $\textstyle \int x ^ { j } k ( x ) \mathrm { d } x = 0$ . Then we define the KDE of $( \widehat { Q } _ { [ m ] } ) _ { \# } \big ( \rho _ { m } \mu ^ { * } \big )$ as

$$
\widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) = \frac { 1 } { h ^ { d } | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \bigg [ \Big \{ \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { [ m ] , j } ( X _ { i } ) - y _ { j } } { h } \Big ) \Big \} \cdot \rho _ { m } ( X _ { i } ) \bigg ] ,
$$

where bandwidth parameter $h = \left( { \textstyle { \frac { \log n } { n } } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ and $\widehat { Q } _ { [ m ] , j } ( X _ { i } )$ denotes the $j$ -th dimension of $\widehat { Q } _ { [ m ] } ( X _ { i } ) \in \mathbb R ^ { d }$ . We show in Appendix D.2.3 that such a KDE based regularization also leads to the same upper bound as in Lemma 5.

# B Generative Model Class of Target Distribution

In this section, we consider generative model classes that include the distribution class ${ \mathcal { P } } ^ { * }$ considered in Theorem 1 as a special case. Similar as the approximation family $S ^ { \mathrm { a p } }$ and $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ , we consider two (mixture of) generative model classes for the target distribution, $S ^ { * } = S ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ and $S _ { \nu _ { 0 } } ^ { * } = S _ { \nu _ { 0 } } ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ , where recall that ${ \mathcal { O } } _ { M } =$ $\{ S _ { m } = \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ forms a open cover for $\mathbb { B } _ { L } ^ { D }$ . The first generative model class $S ^ { * }$ consists of all probability measures $\mu \in \mathcal P ( \mathbb { R } ^ { D } )$ satisfying:

1. $\mu$ has a support contained in $\mathbb { B } _ { L } ^ { D }$ .

2. For any $m \in \lfloor M \rfloor$ , there exists a set $\widetilde { S } _ { m } \supseteq \mathbb { B } _ { r _ { m } + 1 / L } \big ( a _ { m } \big )$ such that

(a) there exists a map $G _ { [ m ] } \in C _ { L } ^ { \gamma } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ such that $\mu | _ { \widetilde { S } _ { m } } = [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ for some distribution $\nu _ { [ m ] } \in \mathcal { P } ( \mathbb { R } ^ { d } )$ supported on $\mathbb { B } _ { 1 } ^ { d }$ . Moreover, there exists $Q _ { [ m ] } \in$ $C _ { L } ^ { \gamma } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ such that $Q _ { [ m ] } \circ [ G _ { [ m ] } | _ { \mathbb { B } _ { 1 } ^ { d } } ] = \mathrm { i d } _ { \mathbb { B } _ { 1 } ^ { d } }$ , the identity map on $\mathbb { B } _ { 1 } ^ { d }$ .   
(b) $\nu _ { [ m ] }$ is absolutely continuously w.r.t. the Lebesgue measure with density also denoted as $\nu _ { [ m ] } : \mathbb { R } ^ { d } \to [ 0 , \infty )$ such that $\nu _ { [ m ] } | _ { \mathbb { B } _ { 1 } ^ { d } } \in C _ { L } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ and there exists $L _ { 0 }$ depending on m such that 0 ≤ L0 ≤ L and supz∈Bd1  log ν[m](z)(1−kzk2)L0 .   
(c) Either $G _ { [ m ] } ( \mathbb { B } _ { 1 } ^ { d } \setminus \mathbb { B } _ { 1 - \epsilon } ^ { d } ) \cap \mathbb { B } _ { r _ { m } } ( a _ { m } ) = \emptyset$ for some $\epsilon$ satisfying $0 < \log { \frac { 1 } { \epsilon } } \leq L$ or $\nu _ { [ m ] } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ .

Remark 9. If we choose $L _ { 0 } = 0$ for each $m \in [ M ]$ in point $2 ( \mathrm { b } )$ of the above assumption, it recovers the assumption in the distribution family ${ \mathcal { P } } ^ { * }$ , where the density of $\mu$ is $\alpha$ - smooth and bounded from above and below. The point $2 ( \mathrm { c } )$ guarantees that for any partition of unity $\{ \rho _ { m } \} _ { m \in [ M ] }$ subordinate to ${ \mathcal { O } } _ { M }$ , the probability measure of the latent variable reweighted by $\rho _ { m }$ , given by $\nu _ { [ m ] } \cdot ( \rho _ { m } \circ G _ { [ m ] } )$ is $\alpha$ -smooth on $\mathbb { R } ^ { d }$ . In particular, the assumption $G _ { [ m ] } ( \mathbb { B } _ { 1 } ^ { d } \setminus \mathbb { B } _ { 1 - \epsilon } ^ { d } ) \cap \mathbb { B } _ { r _ { m } } ( a _ { m } ) = \emptyset$ requires the support of $\mu$ to be boundaryless; on the other hand, the assumption $\nu _ { [ m ] } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ allows the manifold to have a boundary while the distribution should smoothly decay to zero around the boundary.

Remark 10. Given a partition of unity $\{ \rho _ { m } \} _ { m \in [ M ] }$ constructed based on the open over $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ of $\mathbb { B } _ { L } ^ { D }$ (see Section 2.4 for an example), if for any $m \in [ M ] , \widetilde { S } _ { m }$ contains $\mathbb { B } _ { r _ { m } } ( a _ { m } )$ , then $\{ \rho _ { m } \} _ { m \in [ M ] }$ is also a partition of unity of $\mathcal { M }$ subordinate to $\{ \widetilde { S } _ { m } \cap$ $\mathcal { M } \} _ { m \in [ M ] }$ . Lemma 15 in Appendix E.3 shows that the distribution $\mu \in S ^ { * }$ can be expressed as a mixture of generative model with rejection sampling: $\begin{array} { r } { \mu = \sum _ { m = 1 } ^ { M } w _ { [ m ] } \mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) } \end{array}$ where $\{ w _ { [ m ] } \} _ { m \in [ M ] }$ are the mixing weights given by $w _ { [ m ] } = \mathbb { E } _ { \mu } [ \rho _ { m } ( X ) ]$ for $m \in \lfloor M \rfloor$ , and recall $\mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } )$ is the probability measure induced by the data generating process where $X \sim [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ is accepted with probability $\rho _ { m } ( X ) \in [ 0 , 1 ]$ . Therefore, $S ^ { * }$ is included in the approximation family $S ^ { \mathrm { a p } }$ .

Given a prespecified latent space distribution $\nu _ { 0 }$ supported on $\mathbb { B } _ { 1 } ^ { d }$ , similar as the definition for the approximation family $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ , the second generative model class for the target distribution $S _ { \nu _ { 0 } } ^ { * }$ is defined as the set of all probability measures $\mu \in \mathcal P ( \mathbb { R } ^ { D } )$ that satisfy properties 1 and 2 above with $\nu _ { [ m ] } = \vert V _ { [ m ] } \vert _ { \# } \nu _ { 0 }$ for $m \in [ M ]$ , where $V _ { [ m ] } \in C _ { L } ^ { 1 + \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ and it can be similarly shown that $S _ { \nu _ { 0 } } ^ { * } \subset S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ .

Example (Manifold with global parametrization): The simplest example of distribution $\mu \in S ^ { * }$ considers a submanifold $\mathcal { M } \subset \mathbb { R } ^ { D }$ whose atlas $\mathcal { A }$ contains a single chart $( \mathcal { M } , \varphi )$ , that is, $\mathcal { M }$ admits a global parametrization $\varphi ^ { - 1 } : \mathbb { B } _ { 1 } ^ { d ^ { \cup } } \to { \mathcal { M } }$ . The smoothness level $\beta$ of $\mathcal { M }$ is the same as that of $\varphi ^ { - 1 }$ as a diffeomorphism between open set $\mathbb { B } _ { 1 } ^ { d ^ { \upsilon } } \subset \mathbb { R } ^ { d }$ and $\mathcal { M } \subset \mathbb { R } ^ { D }$ . For example, a $d$ -dimensional ball lying in a $d$ -dimensional affine subspace of $\mathbb { R } ^ { D }$ and a $d$ -dimensional half subspace of $\mathbb { R } ^ { D }$ are both submanifolds admitting global parametrization. The global parametrization presumption of a submanifold implies the existence of a boundary, which incurs notoriously technical complication. To address the boundary issue, we require the density function of $\varphi _ { \# } \mu$ to be $\alpha$ -smooth and smoothly decay to zero around the boundary $\partial \mathbb { B } _ { 1 } ^ { d }$ with polynomial tails $( 1 - \| z \| ) ^ { L _ { 0 } }$ for some positive constants $L _ { 0 }$ . Note that in this case, the approximation family $S _ { \nu _ { 0 } } ^ { \mathrm { a p } }$ is not sufficient to cover $\mu$ , as we need the more flexible approximation family $S ^ { \mathrm { a p } }$ containing a latent variable distribution whose density decay around the boundary of $\mathbb { B } _ { 1 } ^ { d }$ matches the polynomial tail $( 1 - \| z \| ) ^ { L _ { 0 } }$ for a possibly unknown $L _ { 0 }$ . One estimation framework to avoid the boundary issue for a manifold with boundary is to consider the restriction of $\mu$ on a compact subset $K _ { 0 }$ of $\mathcal { M }$ that is away from the boundary $\partial \mathcal { M }$ and we consider this framework in Appendix C.2.

Exaxmple (Smooth distributions on unknown compact smooth boundaryless submanifold): Another representative example considers an $\alpha$ -smooth distribution supported on a closed submanifold in $\mathbb { R } ^ { D }$ with density function bounded from above and below, that is, the distribution family ${ \mathcal { P } } ^ { * }$ considered in Theorem 1. Due to the assumption that the density function is bounded away from zero, the family $S _ { \nu _ { 0 } } ^ { * }$ with $\nu _ { 0 }$ being chosen as the uniform distribution on $\mathbb { B } _ { 1 } ^ { d }$ is sufficient to cover ${ \mathcal { P } } ^ { * }$ when the maximal radius $\{ r _ { m } \} _ { m \in [ M ] }$ of the open cover defining the partition of unity is sufficiently small. More specifically, we have the following lemma.

Lemma 8. For any constant $d , D \in \mathbb { N } ^ { + }$ and $\alpha , \beta , L ^ { * } \in \mathbb { R } ^ { + }$ with $d < D$ , $\beta > 1$ and $\alpha \leq$ $\beta - 1$ , there exist positive constants $\epsilon _ { \mathrm { 0 } }$ and $L$ such that for any $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ that forms a open cover for $\mathbb { B } _ { L } ^ { D }$ with $\operatorname* { m a x } \{ r _ { 1 } , r _ { 2 } , \cdot \cdot \cdot , r _ { m } \} \leq \epsilon _ { 0 }$ , it holds that $\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } ) \subset$ $S _ { \nu _ { 0 } } ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L ) \subset S ^ { * } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L )$ with $\nu _ { 0 }$ being the uniform distribution on $\mathbb { B } _ { 1 } ^ { d }$ . Thus we also have $\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } ) \subset S _ { \nu _ { 0 } } ^ { \mathrm { a p } } ( d , D , \alpha , \beta , \mathcal { O } _ { M } , L ) .$ .

Remark 11. The proof of Lemma 8 relies on the Caffarelli’s global regularity theory [Theorem 12.50 of Villani, 2009, Caffarelli, 1996] which states that for $\alpha$ -smooth probability densities $\mu _ { P } , \mu _ { Q }$ that are bounded from above and below on their supports, if their supports are regular enough, then the unique optimal transport map from $\mu _ { P }$ to $\mu _ { Q }$ is $( \alpha + 1 )$ -smooth. We first prove that ${ \mathcal { P } } ^ { * }$ is contained in $S ^ { * }$ where the density of the latent variables $\nu _ { [ m ] } \left( m \in [ M ] \right)$ in each local generative model are bounded away from zero, then we can use Caffarelli’s global regularity theory to obtain that $\nu _ { [ m ] }$ can be generated from $\nu _ { 0 }$ via an $( \alpha + 1 )$ -smooth transport map.

# C Extension of Main result

# C.1 Application in Two-Sample Test

One application of our construction in proving the minimax upper bound is in designing a test statistic for two sample hypothesis testing, which can be stated as follows. Suppose that we have two set of $n$ random samples: $X _ { 1 : n }$ and $Y _ { 1 : n }$ , independently obtained from two populations $\mu _ { 1 }$ and $\mu _ { 2 }$ over ambient space $\mathbb { R } ^ { D }$ , respectively. Assume both $\mu _ { 1 }$ and $\mu _ { 2 }$ have intrinsic dimensionality $d$ , or $\mu _ { 1 }$ , $\mu _ { 2 } \in S ^ { * }$ , we aim to test whether $\mu _ { 1 }$ and $\mu _ { 2 }$ are the same, i.e.,

$$
H _ { 0 } : \mu _ { 1 } = \mu _ { 2 } \quad \mathrm { v e r s u s } \quad H _ { 1 } : \mu _ { 1 } \neq \mu _ { 2 } .
$$

We propose the following test function (probability of rejecting the null) based on the regularized surrogate $\widehat { J } ( f )$ defined in Section 3.1 for estimating $\mathbb { E } _ { \mu } [ f ( X ) ]$ ,

$$
\Phi _ { \gamma , c } ( X _ { 1 : n } , Y _ { 1 : n } ) = \left\{ \begin{array} { r l } { 1 , } & { \qquad \mathrm { i f } \quad \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left| \widehat { \mathcal { T } } ( f ; X _ { 1 : n } ) - \widehat { \mathcal { T } } ( f ; Y _ { 1 : n } ) \right| } \\ & { \qquad \quad \geq c \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta } { d } } \vee \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { 2 } } ; } \\ { 0 , } & { \qquad \mathrm { o t h e r w i s e } , } \end{array} \right.
$$

where we estimate the distance $d _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } )$ between $\mu _ { 1 }$ and $\mu _ { 2 }$ by a natural estimator $\begin{array} { r } { \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \mathopen { } \mathclose \bgroup \left| \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) \aftergroup \egroup \right| } \end{array}$ , and reject the null if this estimator is larger than a threshold $\delta _ { n }$ corresponding to the statistical error of the estimator. To evaluate the power performance of the testing rule induced by $\Phi _ { \gamma , c } = \Phi _ { \gamma , c } ( X _ { 1 : n } , Y _ { 1 : n } )$ , we use the total error $\mathrm { E r r } ( \Phi _ { \gamma , c } , \delta _ { n } )$ of $\Phi _ { \gamma , c }$ under separation rate $\delta _ { n }$ ,

$$
\operatorname { E r r } ( \Phi _ { \gamma , c } , \delta _ { n } ) = \operatorname* { s u p } _ { \stackrel { \mu _ { 1 } , \mu _ { 2 } \in S ^ { * } } { \mu _ { 1 } = \mu _ { 2 } } } \mathbb { E } _ { \mu _ { 1 } , \mu _ { 2 } } ( \Phi _ { \gamma , c } ) + \operatorname* { s u p } _ { \stackrel { \mu _ { 1 } , \mu _ { 2 } \in S ^ { * } } { \mu _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } ) \geq \delta _ { n } } } \mathbb { E } _ { \mu _ { 1 } , \mu _ { 2 } } ( 1 - \Phi _ { \gamma , c } ) ,
$$

to measure the sum of expected (worst case) type I and type II errors of $\Phi _ { \gamma , c }$ in distinguishing two distributions in $S ^ { * }$ that are at least $\delta _ { n }$ away from each other in the $d _ { \gamma }$ metric, or testing against local alternatives $H _ { 1 n } : d _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } ) \geq \delta _ { n }$ . The following corollary shows that, the test rule $\Phi _ { \gamma , c }$ based on the estimator developed in Section 3.1 can detect with diminishing type I and type II errors any local alternatives that separate from the null by as small as $\begin{array} { r } { \delta _ { n } \asymp \delta _ { n } ^ { * } = \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta } { d } } \vee \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { 2 } } } \end{array}$ in the $d _ { \gamma }$ metric.

Corollary 2 (Two-sample test errors). For any positive constant $r$ and $\gamma$ , there exists constant $c _ { 0 } = c _ { 0 } ( r , \gamma )$ such that for any $c \geq c _ { 0 }$ , there exits $c _ { 1 } = c _ { 1 } ( r , \gamma , c )$ such that

$$
\mathrm { E r r } ( \Phi _ { \gamma , c } , c _ { 1 } \delta _ { n } ^ { * } ) \leq n ^ { - r } .
$$

# C.2 Estimation of Distribution Constrained on Compact Sets

Theorem 1 and 2 address the boundary issue of the support $\mathcal { M }$ of the target distribution $\mu \in S ^ { * }$ by assuming $\mathcal { M }$ to be boundaryless or $\mu$ to smoothly decay to zero around the boundary of $\mathcal { M }$ . Another case in which we can prevent the boundary issue is that we only care about $\mu$ constrained on a compact set $K _ { 0 }$ such that ${ \mathcal { M } } \cap K _ { 0 }$ is away from the boundary of $\mathcal { M }$ . Consider constants $L \in \mathbb { R } ^ { + } , d , D \in \mathbb { N } ^ { + }$ , and a compact set $K _ { 0 } \subset \mathbb { R } ^ { D }$ , define $\overline { { S } } ^ { * } ( d , D , \alpha , \beta , K _ { 0 } , L )$ to be the set of probability measure $\mu$ satisfying that

1. There exists a compact set $\widetilde { K } \supseteq K _ { 1 } = \{ x \in B _ { 1 / L } ( y ) : y \in K _ { 0 } \}$ such that $\mu | _ { \widetilde { K } } = G _ { \# } \nu$

2. Write $\Omega = \operatorname { s u p p } ( \nu )$ , it holds that

(a) $\begin{array} { r } { \bigcup _ { z \in \Omega , G ( z ) \in K _ { 1 } } B _ { 1 / L } ( z ) \subset \Omega ; } \end{array}$   
(b) $\nu$ is absolutely continuous with respect to the Lebesgue measure; for any $z \in \Omega$ , $| \log \nu ( z ) | \le L$ and $\nu \in C _ { L } ^ { \alpha } ( \Omega )$ , where we abuse the notation to use $\nu$ to denote its density function.

3. There exists $Q : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ such that

(a) For any $z \in \Omega$ , $Q ( G ( z ) ) = z$ ;   
(b) $Q \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ and $G \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ .

4. Write $K _ { r } = \{ x \in B _ { | r | / L } ( y ) : y \in K _ { 0 } \}$ for $r > 0$ and $K _ { r } = \{ x \in \mathbb { R } ^ { D } : B _ { | r | / L } ( x ) \subset$ $K _ { 0 } \}$ for $r < 0$ . For any $| r | \leq 1$ , it holds that $\left| \mathbb { P } _ { \nu } \big ( G ( z ) \in K _ { 0 } \big ) - \mathbb { P } _ { \nu } \big ( G ( z ) \in K _ { r } \big ) \right| \le$ $L \left| r \right|$ .

Remark 12. The assumptions that $\cup _ { z \in \Omega , G ( z ) \in K _ { 1 } } B _ { 1 / L } ( z ) \subset \Omega$ and $\begin{array} { r } { \left| \mathbb { P } _ { \nu } \mathopen { } \mathclose \bgroup \left( G ( z ) \aftergroup \egroup \right) \in K _ { 0 } \aftergroup \egroup \right) ~ - } \end{array}$ $\begin{array} { r } { \mathbb { P } _ { \nu } \big ( G ( z ) \in K _ { r } \big ) \big | = \frac { 1 } { \mathbb { P } _ { \mu } ( X \in \widetilde { K } ) } \cdot \big | \mathbb { P } _ { \mu } \big ( X \in K _ { 0 } \big ) - \mathbb { P } _ { \mu } \big ( X \in K _ { r } \big ) \big | \leq L \vert r \vert } \end{array}$ ensure that ${ \mathcal { M } } \cap K _ { 0 }$ is away from $\partial \mathcal { M }$ if it exists and the intersection of $\mathcal { M }$ with $\partial K _ { 0 }$ has measure 0 with respect to $\mu$ . Here we assume the support of $\mu$ has a global parametrization when constrained on $K _ { 0 }$ , while it can also adapt to the general case where the support of $\mu | _ { K _ { 0 } }$ has multiple charts by considering partition of $\begin{array} { r } { K _ { 0 } = \sum _ { m = 1 } ^ { M } K _ { [ m ] } } \end{array}$ and estimating each $\mu | _ { K _ { [ m ] } }$ .

Theorem 4. Fix $L > 0$ ; $\gamma \geq 0$ ; $0 \leq \alpha \leq \beta - 1$ ; $\beta > 1$ ; $D , d \in \mathbb { N } ^ { + }$ with $D > d$ ; $K _ { 0 } \subset \mathbb { R } ^ { D }$ be a compact set. Then there exists a surrogate functional $\widehat { \mathcal { T } } ^ { \circ } ( f ) = \widehat { \mathcal { T } } ^ { \circ } ( f ; X _ { 1 : n } )$ depends on data $X _ { 1 : n }$ , such that for any constant $c$ , there exists a constant $n _ { 0 }$ such that when $n \geq n _ { 0 }$ , for any target distribution $\mu ^ { * } \in \overline { { \mathcal { S } } } ^ { * } ( d , D , \alpha , \beta , K _ { 0 } , L )$ , it holds with probability larger than $1 - n ^ { - c }$ that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \widehat { \mathcal { T } } ^ { \circ } ( f ) - \int _ { K _ { 0 } } f ( x ) \mathrm { d } \mu ^ { \ast } \Big | \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \gamma \beta } { d } } .
$$

Thus if $\mathbb { P } _ { \mu ^ { * } } ( X \in K _ { 0 } ) \ge C _ { 1 } > 0$ , then there exists a distribution estimator $\widehat { \mu } ^ { \circ }$ so that

$$
\mathbb { E } [ d _ { \gamma } ( \widehat { \mu } ^ { \circ } , \mu ^ { * } | _ { K _ { 0 } } ) ] \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \gamma \beta } { d } } .
$$

# D Proofs of Remaining Results

In this section, we provide proofs for the remaining results in the main paper.

# D.1 Proofs of lemmas in Section 4.1 for minimax lower bound

In this subsection, we provide proofs for Lemmas 1, 2 and 3.

# D.1.1 Proof of Lemma 1

Recall that $\mathcal { M } _ { 0 } = \mathbb { S } _ { 2 } ^ { d } \times \mathbf { 0 } _ { D - d - 1 } = \{ x \in \mathbb { R } ^ { D } : \| x _ { 1 : d + 1 } \| ^ { 2 } = 2$ , $x _ { d + 2 : D } = \mathbf { 0 } _ { D - d - 1 } \}$ denotes the $d$ -dimensional sphere embedded in $\mathbb { R } ^ { D }$ and $\widetilde { \mathcal { M } } _ { 0 } = \{ x \in \mathbb { R } ^ { D } : x _ { 1 : d } \in \mathbb { B } _ { 1 } ^ { d }$ , $x _ { d + 1 } =$ $\sqrt { 2 - \| x _ { 1 : d } \| ^ { 2 } }$ , $x _ { d + 2 : D } = \mathbf { 0 } _ { D - d - 1 } \}$ denotes its middle area. $\mu _ { 0 }$ is the uniform distribution over $\mathcal { M } _ { 0 }$ . In addition, $\widetilde { \mathcal { M } } _ { 0 }$ admits a global parametrization $G _ { 0 } : \mathbb { B } _ { 1 } ^ { d } \to \widetilde { \mathcal { M } } _ { 0 }$ defined as $G _ { 0 } ( z ) = ( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , { \bf 0 } _ { D - d - 1 } )$ for $z \in \mathbb { B } _ { 1 } ^ { d }$ . Note that $G _ { 0 }$ is $\beta$ -smooth over $\mathbb { B } _ { 1 } ^ { d }$ with bounded Hölder norm. Let $\nu _ { 0 }$ denote the density function on $\mathbb { B } _ { 1 } ^ { d }$ so that $[ G _ { 0 } ] _ { \# } \nu _ { 0 }$ is the restriction of $\mu _ { 0 }$ on $\mathcal { \overline { { M } } } _ { 0 }$ , or

$$
\nu _ { 0 } ( z ) = \frac { 1 } { \widetilde C } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } , \quad \forall z \in \mathbb { B } _ { 1 } ^ { d } ,
$$

where recall that $\mathbf { J } _ { G }$ denotes the Jacobian matrix of $G$ and $\begin{array} { r } { \widetilde { C } = \int _ { \mathbb { B } _ { 1 } ^ { d } } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } \mathrm { d } z } \end{array}$ is the normalizing constant. Since $\widetilde { \mathcal { M } } _ { 0 }$ is a compact set, there exists positive constants $u _ { 1 } , a _ { 2 }$ so that for any $z \in \mathbb { B } _ { 1 } ^ { d }$ , $a _ { 1 } I _ { d } \prec \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) \prec { a _ { 2 } } I _ { d }$ . Therefore, $\nu _ { 0 }$ is an $\alpha$ -smooth density function with bounded Hölder norm on $\mathbb { B } _ { 1 } ^ { d }$ . Next we will add small bumps to function $G _ { 0 }$ to construct perturbations of $\breve { \mathscr { M } } _ { 0 }$ , whose unions with the spherical cap $\widetilde { \mathcal { M } } _ { 1 } : = \mathcal { M } _ { 0 } \setminus \widetilde { \mathcal { M } } _ { 0 }$ form our constructed perturbed $\beta$ -smooth manifolds with controlled Hölder norm.

Let $m = \lfloor b n ^ { \frac { 1 } { d } } \rfloor$ with tuning parameter $b$ to be determined later. Our constructed perturbed generative maps $G _ { \omega }$ are parametrized by a binary tensor $\omega = ( \omega _ { \xi } ) _ { \xi \in [ m ] ^ { d } } \in$ $\{ 0 , 1 \} ^ { [ m ] ^ { d } }$ indexed by all $d$ -dimensional grid points in $[ 1 , m ] ^ { d }$ . Here, subscript $\xi \in [ m ] ^ { d }$ indicates the coordinates of the grid points, and $\omega$ indicates the locations of the jumps. More specifically, let

$$
\begin{array} { r } { k ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \beta + 1 } t ^ { \beta + 1 } , \quad t \in ( 0 , 1 ) , } \\ { 0 , \quad \mathrm { ~ o . w . } } \end{array} \right. } \end{array}
$$

defines a localized bump function. For each $d$ -dimensional grid point $\xi = ( \xi _ { 1 } , \ldots , \xi _ { d } ) \in$

$[ m ] ^ { d }$ , let

$$
\psi _ { \xi } ( z ) = \prod _ { i = 1 } ^ { d } k \Big ( m \sqrt { \frac { d } { 2 } } z _ { i } + \frac { m } { 2 } - \xi _ { i } \Big ) , \quad \forall z \in \mathbb { B } _ { 1 } ^ { d } ,
$$

denote a localized bump function over $\mathbb { B } _ { 1 } ^ { d }$ whose support is contained in the following cube

$$
- \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { 1 } } { m } \sqrt { \frac { 2 } { d } } , ~ - \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { 1 } + 1 } { m } \sqrt { \frac { 2 } { d } } \biggr ] \times \dots \times \left[ - \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { d } } { m } \sqrt { \frac { 2 } { d } } , ~ - \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { d } + 1 } { m } \sqrt { \frac { 2 } { d } } \right]
$$

which has width $m ^ { - 1 } { \sqrt { 2 / d } }$ and is contained in $B _ { 3 / 4 } ^ { d }$ when $b \geq 9$ . For any $\omega = ( \omega _ { \xi } ) _ { \xi \in [ m ] ^ { d } } \in$ $\{ 0 , 1 \} ^ { [ m ] ^ { d } }$ , we define the multi-bump function

$$
g _ { \omega } ( z ) = \sum _ { \xi \in [ m ] ^ { d } } \frac { 1 } { m ^ { \beta } } \omega _ { \xi } \psi _ { \xi } ( z ) , \quad z \in \mathbb { B } _ { 1 } ^ { d } ,
$$

whose bumps correspond to the non-zero components of $\omega$ . Finally, we define $G _ { \omega } ( z ) =$ $G _ { 0 } ( z ) + ( { \bf 0 } _ { d } , g _ { \omega } ( z ) , { \bf 0 } _ { D - d - 1 } )$ for $z \in \mathbb { B } _ { 1 } ^ { d }$ as the perturbed generative map parametrized by $\omega \in \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ . It is straightforward to verify that there exists some constant $L$ , such that $m ^ { - \beta } \psi _ { \xi } ( z )$ belongs to $C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } )$ for any $\xi \in [ m ] ^ { d }$ , and for any $\omega \in \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ , $g _ { \omega }$ belongs to $C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } )$ and $G _ { \omega }$ belongs to $C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; \mathbb { R } ^ { D } )$ .

By Lemma 16 in Appendix E.4, which is a two-sided version of the Varshamov-Gilbert lemma [Tsybakov, 2009], there exists a subset $\{ \omega ^ { ( 1 ) } , \cdot \cdot \cdot , \omega ^ { ( H _ { 0 } ) } \} \subset \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ such that:

1. $\log { H _ { 0 } } \geq \frac { m ^ { d } } { 8 } - \log { 2 }$ ;   
2. for any $j , k \in [ H _ { 0 } ]$ with $j \neq k$ , the Hamming distance $\rho ( \boldsymbol { \omega } ^ { ( j ) } , \boldsymbol { \omega } ^ { ( k ) } )$ between $\boldsymbol { \omega } ^ { ( j ) }$ and $\boldsymbol { \omega } ^ { ( k ) }$ satisfies $\begin{array} { r } { \frac { m ^ { d } } { 4 } \leq \rho ( \omega ^ { ( j ) } , \omega ^ { ( k ) } ) \leq \frac { 3 m ^ { d } } { 4 } } \end{array}$ .

For each $\omega \in \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ , define $\bar { \omega } = 1 - \omega$ in the element-wise manner. We may expand the above $H _ { 0 }$ tensors into $H = 2 H _ { 0 }$ ones, ordered as

$$
\{ \omega ^ { ( 1 ) } , \cdots , \omega ^ { ( H ) } \} = \{ \omega ^ { ( 1 ) } , \cdots , \omega ^ { ( H _ { 0 } ) } , \bar { \omega } ^ { ( 1 ) } , \cdots , \bar { \omega } ^ { ( H _ { 0 } ) } \} .
$$

Then $\begin{array} { r } { \log H \geq \frac { m ^ { d } } { 8 } } \end{array}$ and for any $i , j \in [ H ]$ with $i \neq j$ , it holds that $\rho ( \omega ^ { ( i ) } , \omega ^ { ( j ) } ) \geq \frac { m ^ { d } } { 4 }$ . We do this expansion since we will use a key property later (c.f. proof of Lemma 9) that for any fixed index $\xi \in [ m ] ^ { d }$ , there are equal numbers of $0$ ’s and 1’s in the sequence $( \omega _ { \xi } ^ { ( 1 ) } , \cdots , \omega _ { \xi } ^ { ( H ) } )$ .

Next, for each $i \in | H |$ , let $\mathcal { M } _ { \omega ^ { ( i ) } } = G _ { \omega ^ { ( i ) } } ( \mathbb { B } _ { 1 } ^ { d } )$ denote the perturbed manifold from $G _ { \omega ^ { ( i ) } }$ . We define a perturbation to $\mu _ { 0 }$ by smoothly gluing together the restriction $\mu _ { 0 } | _ { \widetilde { \mathcal { M } } _ { 1 } }$ of $\mu _ { 0 }$ onto $\widetilde { \mathcal { M } } _ { 1 }$ and $\mu _ { \omega ^ { ( i ) } } : = [ G _ { \omega ^ { ( i ) } } ] | _ { \# } \nu _ { 0 }$ over $\mathcal { M } _ { \omega ^ { ( i ) } }$ as

$$
\mu _ { i } = \Big ( 1 - \frac { \widetilde C } { C } \Big ) \cdot \mu _ { 0 } \big | _ { \widetilde { \mathcal { M } } _ { 1 } } + \frac { \widetilde C } { C } \cdot \mu _ { \omega ^ { ( i ) } } ,
$$

where recall that $C ^ { - 1 }$ is the density function of the uniform distribution over $\mathcal { M } _ { 0 }$ so that $\widetilde C < C$ . Then $\mu _ { i }$ is supported over the manifold $\mathcal { M } _ { i } : = \widetilde { \mathcal { M } } _ { 1 } \cup \mathcal { M } _ { \omega ^ { ( i ) } }$ . Since $G _ { \omega ^ { ( i ) } } \in$ $C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } , \mathbb { R } ^ { D } )$ , $G _ { \omega ^ { ( i ) } } ^ { - 1 } ( x ) = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { d } )$ for $x \in \mathcal { M } _ { \omega ^ { ( i ) } }$ and by construction $G _ { \omega ^ { ( i ) } } ( z ) = G _ { 0 } ( z )$ for any $z \in \mathbb { B } _ { 1 } ^ { d } \setminus \mathbb { B } _ { 3 / 4 } ^ { d }$ , we have that $\mathcal { M } _ { i }$ is a compact $\beta$ -smooth submanifold. Furthermore, the density function of distribution $\mu _ { i }$ with respect to the volume measure of $\mathcal { M } _ { i }$ is given by

$$
\mu _ { i } ( \mathrm { d } x ) = \frac { 1 } { C } \mathbf { 1 } ( x \in \widetilde { \mathcal { M } _ { 1 } } ) + \frac { 1 } { C } \frac { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) ) } } { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { \omega ^ { ( i ) } } } ( x _ { 1 : d } ) ^ { T } \mathbf { J } _ { G _ { \omega ^ { ( i ) } } } ( x _ { 1 : d } ) ) } } \mathbf { 1 } ( x \in \mathcal { M } _ { \omega ^ { ( i ) } } ) , \forall x \in \mathcal { N }
$$

Note that functioHölder norm on $\begin{array} { r } { g _ { i } ( z ) : = \frac { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } } { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { \omega } ( i ) } ( z ) ^ { T } \mathbf { J } _ { G _ { \omega } ( i ) } ( z ) ) } } } \end{array}$ $\alpha$ -smooth function with bounded. Consequently, there exists a $\mathbb { B } _ { 1 } ^ { d }$ $g _ { i } ( z ) = 1$ $z \in \mathbb { B } _ { 1 } ^ { d } \setminus B _ { 3 / 4 } ^ { d }$   
constant $L _ { 1 }$ such that $\mu _ { i } ( \mathrm { d } x ) \in C _ { L _ { 1 } } ^ { \alpha } ( \mathcal { M } _ { i } ) ^ { 1 4 }$ , or equivalently, $\mu _ { i }$ is an $\alpha$ -smooth distribution   
on the $\beta$ -smooth manifold $\mathcal { M } _ { i }$ . Therefore, for sufficiently large $L ^ { * }$ , it holds that $\mu _ { i } \in$   
$\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ for any $i \in | H |$ .

Let $\begin{array} { r } { \bar { \mu } = \frac { 1 } { H } \sum _ { i = 1 } ^ { H } \mu _ { i } } \end{array}$ be the averaged distribution. The following lemma, whose proof is deferred to Section E.5, provides upper bounds to $D _ { \mathrm { K L } } ( \mu _ { i } \mid \mid \bar { \mu } )$ and lower bounds to the pairwise $d _ { \gamma }$ distances, which concludes the proof.

Lemma 9. Assume $\gamma < 1$ and $\beta > 1$ . For any $i \in [ H ]$ , it holds that $D _ { \mathrm { K L } } ( \mu _ { i } | | \bar { \mu } ) \leq \log 2$ .   
For any i, j ∈ [H] with i 6= j, it holds that dγ (µi, µj ) ≥ c1 m−γβ ≥ c2 n− γβd .

# D.1.2 Proof of Lemma 2

We adopt the same setting and notations as in the proof of Lemma 1 in Section D.1.1, where recall that $\mathcal { M } _ { 0 } = \mathbb { S } _ { 2 } ^ { d } \times \mathbf { 0 } _ { D - d - 1 }$ is the $d$ -dimensional sphere embedded in $\mathbb { R } ^ { D }$ and $\mu _ { 0 }$ is the uniform distribution on $\mathcal { M } _ { 0 }$ . In addition, we partition $\mathcal { M } _ { 0 }$ into its middle area $\widetilde { \mathcal { M } } _ { 0 }$ and the two remaining caps $\breve { \mathscr { M } } _ { 1 }$ , where $( \nu _ { 0 } , G _ { 0 } )$ is the generative model such that $[ G _ { 0 } ] _ { \# } \nu _ { 0 }$ is the restriction $\mu _ { 0 } | _ { \widetilde { \mathcal { M } } _ { 0 } }$ of $\mu _ { 0 }$ on $\widetilde { \mathcal { M } } _ { 0 }$ . Our construction of perturbed distributions on $\mathcal { M } _ { 0 }$ will be based on adding small bumps to the generative distribution $\nu _ { 0 }$ on the $d$ -dimensional unit ball $\mathbb { B } _ { 1 } ^ { d }$ .

Let $\widetilde { m } = \lfloor b n ^ { \frac { 1 } { 2 \alpha + d } } \rfloor$ . Define the following localized bump function

$$
\widetilde { k } ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \alpha \vee \gamma + 1 } t ^ { \alpha \vee \gamma + 1 } ( t - \frac { 1 } { 2 } ) , \quad t \in ( 0 , 1 ) } \\ { 0 , \quad \mathrm { o . w . } } \end{array} \right.
$$

so that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \widetilde { k } ( t ) \mathrm { d } t = 0 } \end{array}$ , and the corresponding localized bump function over $\mathbb { B } _ { 1 } ^ { d }$

$$
\widetilde { \psi } _ { \xi } ( z ) = \prod _ { i = 1 } ^ { d } \widetilde { k } \Big ( m \sqrt { \frac { d } { 2 } } z _ { i } + \frac { m } { 2 } - \xi _ { i } \Big ) , \quad \forall z \in \mathbb { B } _ { 1 } ^ { d } ,
$$

indexed by the $d$ -dimensional grid point $\xi = ( \xi _ { 1 } , \dots , \xi _ { d } ) \in [ \widetilde { m } ] ^ { d }$ . In addition, we define two function sets

$$
\begin{array} { l } { \displaystyle \Psi _ { \alpha } = \Big \{ g _ { \omega } ( z ) = \nu _ { 0 } ( z ) + b _ { 0 } \left( \frac { 1 } { \widetilde m } \right) ^ { \alpha } \sum _ { \xi \in [ \widetilde m ] ^ { d } } \omega _ { \xi } \widetilde \psi _ { \xi } ( z ) : ~ \omega = \{ \omega _ { \xi } \} _ { \xi \in [ \widetilde m ] ^ { d } } \in \{ 0 , 1 \} ^ { [ \widetilde m ] ^ { d } } \Big \} , } \\ { \displaystyle \Lambda _ { \gamma } = \Big \{ f _ { v } ( z ) = \left( \frac { 1 } { \widetilde m } \right) ^ { \gamma } \sum _ { \xi \in [ \widetilde m ] ^ { d } } v _ { \xi } \widetilde \psi _ { \xi } ( z ) : ~ v = \big \{ v _ { \xi } \big \} _ { \xi \in [ \widetilde m ] ^ { d } } \in \{ - 1 , 1 \} ^ { [ \widetilde m ] ^ { d } } \Big \} , } \end{array}
$$

where $b _ { 0 }$ is some constant to be determined later. $\Psi _ { \alpha }$ consists of all perturbed densities around $\nu _ { 0 }$ and $\Lambda _ { \gamma }$ serves as set of discriminators defined over $\mathbb { B } _ { 1 } ^ { d }$ for discriminating the densities in $\Psi _ { \alpha }$ . Since for any $\xi \in [ \widetilde { m } ] ^ { d }$ , the support $\operatorname { s u p p } ( \psi _ { \xi } )$ is contained in $\textstyle { \left[ - { \sqrt { \frac { 1 } { 2 d } } } + { \frac { \xi _ { 1 } } { m } } { \sqrt { \frac { 2 } { d } } } \right. }$ , $\begin{array} { r } { - \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { 1 } + 1 } { m } \sqrt { \frac { 2 } { d } } ] \times \cdot \cdot \cdot \times \big [ - \sqrt { \frac { 1 } { 2 d } } + \frac { \xi _ { d } } { m } \sqrt { \frac { 2 } { d } } } \end{array}$ , $- \sqrt { \textstyle { \frac { 1 } { 2 d } } } + \frac { \xi _ { d } + 1 } { m } \sqrt { \textstyle { \frac { 2 } { d } } } ]$ , which is further contained in $[ - \sqrt { \frac { 1 } { 2 d } } + \frac { 1 } { m } \sqrt { \frac { 2 } { d } }$ , ${ \sqrt { \textstyle { \frac { 1 } { 2 d } } } } + { \frac { 1 } { m } } { \sqrt { \textstyle { \frac { 2 } { d } } } } ] ^ { d }$ . Therefore, $\widetilde { \psi } _ { \xi }$ ’s with distinct indices $\xi$ ’s have disjoint supports and if $b \geq 9$ , then for each $g \in \Psi _ { \alpha }$ , we have: $g ( z ) = \nu _ { 0 } ( z )$ for all $z \in \mathbb { R } ^ { d } \backslash B _ { 3 / 4 } ^ { d }$ ; and $\begin{array} { r } { g ( z ) \geq \operatorname* { i n f } _ { z \in B _ { 3 / 4 } ^ { d } } \nu _ { 0 } ( z ) - b _ { 0 } b ^ { - \alpha } \operatorname* { s u p } _ { t \in ( 0 , 1 ) } | \widetilde { k } ( t ) | ^ { d } > 0 } \end{array}$ for all $z \in B _ { 3 / 4 } ^ { d }$ when $b _ { 0 }$ is sufficiently small, which makes $g$ non-negative. In addition, since $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \widetilde { k } ( t ) \mathrm { d } t = 0 } \end{array}$ , we have $\begin{array} { r } { \int _ { \mathbb { B } _ { 1 } ^ { d } } g ( z ) \mathrm { d } z = \int _ { \mathbb { B } _ { 1 } ^ { d } } \nu _ { 0 } ( z ) \mathrm { d } z = 1 } \end{array}$ . Therefore, all functions in $\Psi _ { \alpha }$ are valid probability density functions. Finally, it is straightforward to verify that there exist constants $( L _ { 1 } , L _ { 2 } )$ such that $g \in C _ { L _ { 1 } } ^ { \alpha } ( \mathbb { R } ^ { d } )$ and $f \in C _ { L _ { 2 } } ^ { \gamma } ( \mathbb { R } ^ { d } )$ for each $g \in \Psi _ { \alpha }$ and $f \in \Lambda _ { \gamma }$ .

For each $\omega \in \{ 0 , 1 \} ^ { m ^ { d } }$ , we define the following distribution over $\mathcal { M } _ { 0 }$ as

$$
\mu _ { \omega } = \Big ( 1 - \frac { \widetilde { C } } { C } \Big ) \cdot \mu _ { 0 } \lvert _ { \widetilde { \mathcal { M } } _ { 1 } } + \frac { \widetilde { C } } { C } \cdot [ G _ { 0 } ] _ { \# } g _ { \omega } ,
$$

where recall that $C$ is the surface area of $\mathbb { S } _ { 2 } ^ { d }$ and $\begin{array} { r } { { \widetilde { C } } = \int _ { \mathbb { B } _ { 1 } ^ { d } } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } \mathrm { d } z } \end{array}$ . Then $\mu _ { \omega }$ has the following density function with respect to the volume measure of $\mathcal { M } _ { 0 }$ ,

$$
\iota _ { \omega } ( \mathrm { d } x ) = \frac { 1 } { C } \mathbf { 1 } ( x \in \widetilde { \mathcal { M } } _ { 1 } ) + \frac { \widetilde C } { C } \cdot \frac { b _ { 0 } \left( \frac { 1 } { \widetilde \sigma } \right) ^ { \alpha } \sum _ { \xi \in [ \widetilde { m } ] ^ { d } } \omega _ { \xi } \widetilde \psi _ { \xi } ( x _ { 1 : d } ) } { \sqrt { \operatorname* { d e t } \left( \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) \right) } } \cdot \mathbf { 1 } ( x \in \widetilde { \mathcal { M } } _ { 0 } ) , ~ \forall x \in \mathcal { M } _ { 0 } .
$$

Since $\psi _ { \xi } ( z ) = 0$ for all $z \in \mathbb { B } _ { 1 } ^ { d } \backslash B _ { 3 / 4 } ^ { d }$ and $G _ { 0 }$ is infinitely-differentiable over the compact set $\mathbb { B } _ { 1 } ^ { d }$ with non-singular Jacobian $\mathbf { J } _ { G _ { 0 } }$ , there exists constant $L _ { 3 }$ such that for each $\omega \in [ 0 , 1 ] ^ { [ \widetilde { m } ] ^ { d } }$ the density function of $\mu _ { \omega }$ belongs to $C _ { L _ { 1 } } ^ { \alpha } ( \mathcal { M } _ { 0 } )$ , implying $\mu _ { \omega } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ for sufficiently large $L ^ { * }$ .

Next, we will pick up a subset $\left\{ \omega ^ { ( 0 ) } , \ldots , \omega ^ { ( H ^ { \prime } ) } \right\}$ of $[ \widetilde { m } ] ^ { d }$ such that the corresponding distributions $\left\{ \mu _ { h } : = \mu _ { \omega ^ { ( h ) } } \right\} _ { h = 1 } ^ { H ^ { \prime } }$ constitute the set of perturbed distributions in the lemma. Concretely, by the Varshamov-Gilbert lemma [Tsybakov, 2009], there exists a set {ω(0), · · · , ω(H0)} ⊂ {0, 1}[me ]d such that log H0 ≥ me d8 log 2 and the Hamming distance $\rho ( \omega ^ { ( j ) } , \omega ^ { ( k ) } ) \geq \frac { m ^ { d } } { 8 }$ for any distinct pair $j , k \in [ H ^ { \prime } ]$ . Therefore, for any distinct $j , k \in [ H ^ { \prime } ]$ , we have by our construction of $\mu _ { h }$ ’s that

$$
\begin{array} { r l r } {  { d _ { \gamma } ( \mu _ { j } , \mu _ { k } ) = \widetilde { \underline { { C } } } \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \int _ { \widetilde { \mathcal { M } } _ { 0 } } f ( x ) \cdot \big ( \mathrm { d } ( [ G _ { 0 } ] _ { \# } g _ { \omega ^ { ( j ) } } ) - \mathrm { d } ( [ G _ { 0 } ] _ { \# } g _ { \omega ^ { ( k ) } } ] \big ) } } \\ & { } & { \quad = \widetilde { \underline { { C } } } \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \int _ { \mathbb { R } _ { 1 } ^ { d } } f \circ G _ { 0 } ( z ) \cdot \big ( g _ { \omega ^ { ( j ) } } ( z ) - g _ { \omega ^ { ( k ) } } ( z ) \big ) \mathrm { d } z . } \end{array}
$$

Now since $G _ { 0 }$ is infinitely-differentiable over $\mathbb { B } _ { 1 } ^ { d }$ with bounded Hölder norm and the $d$ -dimensional discriminator class $\Lambda _ { \gamma } \subset C _ { L _ { 2 } } ^ { \gamma } ( \mathbb { B } _ { 1 } ^ { d } )$ , we have $c _ { 0 } ^ { - 1 } \Lambda _ { \gamma } \subset C _ { c _ { 0 } ^ { - 1 } L _ { 2 } } ^ { \gamma } ( \mathbb { B } _ { 1 } ^ { d } ) \subset C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) \circ$ $G _ { 0 } = \{ f \circ G _ { 0 } : f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) \}$ for some sufficiently small constant $c _ { 0 }$ , and

$$
\begin{array} { r l } & { \mathfrak { r } _ { \gamma } ( \mu _ { j } , \mu _ { k } ) \ge \displaystyle \frac { \widetilde { C } } { c _ { 0 } C } \cdot \operatorname* { s u p } _ { f \in \Lambda _ { 1 } } \int _ { \mathbb { R } _ { 1 } ^ { d } } f ( z ) \cdot \big ( g _ { \omega ( i ) } ( z ) - g _ { \omega ^ { ( k ) } } ( z ) \big ) \mathrm { d } z } \\ & { \quad \quad \quad = \displaystyle \frac { b _ { 0 } \widetilde { C } } { c _ { 0 } C } \cdot \Big ( \frac { 1 } { \widetilde { m } } \Big ) ^ { \alpha + \gamma } \cdot \underbrace { \operatorname* { s u p } _ { v \in \{ - 1 , 1 \} } \int _ { \mathbb { R } _ { 1 } ^ { d } } \Big \{ \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d } } v _ { \xi } \widetilde { \psi } _ { \xi } ( z ) \Big \} } \cdot \left\{ \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d } } ( \omega _ { \xi } ^ { ( j ) } - \omega _ { \xi } ^ { ( k ) } ) \cdot \widehat { \psi } ^ { \frac { \gamma } { i } } \right. } \\ &  \quad \quad \quad \quad = \displaystyle \frac { b _ { 0 } \widetilde { C } } { c _ { 0 } C } \cdot \Big ( \frac { 1 } { \widetilde { m } } \Big ) ^ { \alpha + \gamma } \cdot \underbrace { \operatorname* { s u p } _ { v \in \{ - 1 , 1 \} } \int _ { \mathbb { R } _ { 1 } ^ { d } } \Big \{ \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d } } v _ { \xi } \cdot ( \omega _ { \xi } ^ { ( j ) } - \omega _ { \xi } ^ { ( k ) } ) \cdot \widehat { \psi } _ { \xi } ^ { \frac { \gamma } { i } } ( z ) \Big \} } _ { v \in \{ - 1 , 1 \} ^ { i m ^ { d } } \} \mathrm { d } z } \\ &  \quad \quad \ge c ^ { \prime } \cdot \Big ( \frac { 1 } { \widetilde { m } } \Big ) ^ { \alpha + \gamma + d } \cdot \rho ( \omega ^ { ( j ) } , \omega ^  ( k  \end{array}
$$

for some constant $c ^ { \prime }$ . Moreover, we have

$$
\begin{array} { l } { \displaystyle _ { - } ( \mu _ { j } , \mu _ { k } ) = \frac { \widetilde { C } } { C } D _ { \mathrm { K L } } ( G _ { \# } g _ { \omega } , G _ { \# } g _ { \omega ^ { \prime } } ) } \\ { \displaystyle ~ = \frac { \widetilde { C } } { C } \int _ { \left[ - \sqrt { \frac { 1 } { 2 d } } , \sqrt { \frac { 1 } { 2 d } } + \sqrt { \frac { 2 } { d } } \frac { 1 } { \mu _ { \ast } } \right] ^ { d } } ^ { } - \log \bigg ( \underbrace { \frac { \nu _ { 0 } ( z ) + b _ { 0 } ( \frac 1 \widetilde { m } ) ^ { \alpha } \sum _ { \xi \in [ \widetilde m ] ^ { d } } \omega _ { \xi } ^ { ( k ) } \widetilde { \psi } _ { \xi } ( z ) } { \nu _ { 0 } ( z ) + b _ { 0 } ( \frac 1 \widetilde { m } ) ^ { \alpha } \sum _ { \xi \in [ \widetilde m ] ^ { d } } \omega _ { \xi } ^ { ( j ) } \widetilde { \psi } _ { \xi } ( z ) } } _ { : = 1 + u ( z ) } \bigg ) g _ { \omega ^ { ( j ) } } ( z ) } \end{array}
$$

For sufficiently large $b$ , we have $| u ( z ) | \leq 1 / 4$ over $\mathbb { B } _ { 1 } ^ { d }$ so that $- \log ( 1 + u ( z ) ) \leq u ^ { 2 } ( z ) - u ( z )$ . This leads to

$$
\begin{array} { l } { \displaystyle _ { j } , \mu _ { k } ) \le c ^ { \prime \prime } \Big ( \frac { 1 } { \widetilde m } \Big ) ^ { 2 \alpha } + c ^ { \prime \prime } b _ { 0 } \Big ( \frac { 1 } { \widetilde m } \Big ) ^ { \alpha } \displaystyle \int _ { [ - \sqrt { \frac { 1 } { 2 d } } ,  \sqrt { \frac { 1 } { 2 d } } + \sqrt { \frac { 2 } { d } } \frac { 1 } { m } ] ^ { d } } \{ \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d } } ( \omega _ { \xi } ^ { ( j ) } - \omega _ { \xi } ^ { ( k ) } ) \cdot \psi _ { \xi } ( z ) \} \mathrm { d } z } \\ { \displaystyle = c ^ { \prime \prime } \Big ( \frac { 1 } { \widetilde m } \Big ) ^ { 2 \alpha } = c ^ { \prime \prime } b ^ { - 2 \alpha } n ^ { - \frac { 2 \alpha } { 2 \alpha + d } } , } \end{array}
$$

for some constant $c ^ { \prime \prime }$ , where we used the fact that $\begin{array} { r } { \int _ { \mathbb { B } _ { 1 } ^ { d } } \psi _ { \xi } ( z ) \mathrm { d } z = 0 } \end{array}$ for any $\xi \in [ \widetilde { m } ] ^ { d }$ .

# D.1.3 Proof of Lemma 3

Define function $\bar { k } : \mathbb { R }  \mathbb { R }$ by

$$
\begin{array} { r } { \bar { k } ( z ) = \left\{ \begin{array} { l l } { \left( \sqrt { \frac { 1 } { 2 d } } - z \right) ^ { \alpha \lor \gamma + 1 } \left( z + \sqrt { \frac { 1 } { 2 d } } \right) ^ { \alpha \lor \gamma + 1 } z , } & { z \in \big [ - \sqrt { \frac { 1 } { 2 d } } , \sqrt { \frac { 1 } { 2 d } } \big ] , } \\ { 0 , \quad \mathrm { o . w . } } \end{array} \right. } \end{array}
$$

Then we have $\begin{array} { r } { \int _ { - \infty } ^ { \infty } k ( z ) \mathrm { d } z = 0 } \end{array}$ . For $z \in \mathbb { B } _ { 1 } ^ { d }$ , define

$$
\nu _ { 1 } ( z ) = \nu _ { 0 } ( z ) + \frac { c } { \sqrt { n } } \prod _ { j = 1 } ^ { d } \bar { k } ( z _ { j } ) ,
$$

where $\nu _ { 0 }$ is defined in the proof of Lemma $1$ in Section D.1.1 and $c$ is a constant. For sufficiently small $c$ , we have $\nu _ { 1 } ( z ) \geq 0$ , which combined with $\begin{array} { r } { \int _ { \mathbb { B } _ { 1 } ^ { d } } \nu _ { 1 } ( z ) \mathrm { d } z = 1 } \end{array}$ implies $\nu _ { 1 }$ to be a valid probability density function on $\mathbb { B } _ { 1 } ^ { d }$ . Moreover, there exists some sufficiently large constant $c _ { 1 }$ such that $\nu _ { 0 }$ , $\nu _ { 1 } \in C _ { c _ { 1 } } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ . Recall $G _ { 0 } : \mathbb { B } _ { 1 } ^ { d }  \mathbb { R } ^ { D }$ is the generative map defined as $G ( z ) = ( z , \sqrt { 2 - \| z \| ^ { 2 } } , { \bf 0 } _ { D - d - 1 } )$ for $z \in \mathbb { B } _ { 1 } ^ { d }$ , $\mathcal { M } _ { 0 } = \widetilde { \mathcal { M } } _ { 0 } \cap \widetilde { \mathcal { M } } _ { 1 }$ is the partition of manifold $\mathcal { M } _ { 0 }$ defined in Section D.1.1, and $\mu _ { 0 }$ is the uniform distribution on $\mathcal { M } _ { 0 }$ . Define another distribution on $\mathcal { M } _ { 0 }$ as

$$
\mu _ { 1 } = \Big ( 1 - \frac { \widetilde { C } } { C } \Big ) \cdot \mu _ { 0 } \lvert _ { \widetilde { \mathcal { M } } _ { 1 } } + \frac { \widetilde { C } } { C } \cdot [ G _ { 0 } ] _ { \# } \nu _ { 1 } .
$$

where $C$ , $\check { C }$ are the same normalizing constants defined in Section D.1.1. The density function of $\mu _ { 1 }$ with respect to the volume measure of $\mathcal { M } _ { 0 }$ is

$$
u _ { 1 } ( \mathrm { d } x ) = \frac { 1 } { C } \mathbf { 1 } ( x \in \widetilde { \mathcal { M } _ { 1 } } ) + \frac { \widetilde { C } } { C } \cdot \frac { \frac { c } { \sqrt { n } } \prod _ { j = 1 } ^ { d } \bar { k } ( x _ { j } ) } { \sqrt { \operatorname* { d e t } \left( \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( x _ { 1 : d } ) \right) } } \mathbf { 1 } ( x \in \widetilde { \mathcal { M } } _ { 0 } ) , \quad \forall x \in \mathcal { M } _ { 0 } .
$$

Then by $k ( z ) = 0$ when $| z | > { \sqrt { \frac { 1 } { d } } }$ , we can obtain that $\mu _ { 0 } , \mu _ { 1 } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ for sufficiently large $L ^ { * }$ . Moreover,

$$
\begin{array} { r l r } & { } & { d _ { \chi ^ { 2 } } ( \mu _ { 1 } , \mu _ { 0 } ) = \displaystyle \frac { \widetilde { C } } { C } d _ { \chi ^ { 2 } } \big ( [ G _ { 0 } ] _ { \# } \nu _ { 1 } , [ G _ { 0 } ] _ { \# } \nu _ { 0 } \big ) = \displaystyle \frac { \widetilde { C } } { C } d _ { \chi ^ { 2 } } \big ( \nu _ { 1 } , \nu _ { 0 } \big ) } \\ & { } & { \quad \quad \quad \quad = \displaystyle \frac { \widetilde { C } } { C } \int _ { \left[ - \sqrt { \frac { 1 } { 2 d } } , \ \sqrt { \frac { 1 } { 2 d } } \right] ^ { d } } \left( \frac { \nu _ { 1 } ( z ) } { \nu _ { 0 } ( z ) } - 1 \right) ^ { 2 } \nu _ { 0 } ( z ) \mathrm { d } z } \\ & { } & { \quad \quad \quad \quad \quad = \displaystyle \frac { \widetilde { C } } { C } \int _ { \left[ - \sqrt { \frac { 1 } { 2 d } } , \ \sqrt { \frac { 1 } { 2 d } } \right] ^ { d } } \frac { c ^ { 2 } } { n } \displaystyle \prod _ { j = 1 } ^ { d } \frac { \bar { k } ^ { 2 } ( z _ { j } ) } { \nu _ { 0 } ( z ) } \mathrm { d } z \leq \frac { 1 } { n } , } \end{array}
$$

for sufficiently small $c$ . Define discriminator $\begin{array} { r } { \bar { f } ( z ) = \sqrt { n } \left( \nu _ { 1 } ( z ) - \nu _ { 0 } ( z ) \right) = c \prod _ { j = 1 } ^ { d } \bar { k } ( z _ { j } ) } \end{array}$ . Since $G _ { 0 }$ is infinitely-differentiable with bounded higher-order derivative over $\mathbb { B } _ { 1 } ^ { d }$ , there

exist sufficiently small constants $( c _ { 1 } , c _ { 2 } )$ such that $c _ { 1 } f ( z ) \in C _ { c _ { 2 } } ^ { \gamma } ( \mathbb { R } ^ { d } ) \subset C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) \circ G _ { 0 } =$ $\{ f \circ G _ { 0 } : f \in C _ { 1 } ^ { \beta } ( \mathbb { R } ^ { D } ) \}$ . Therefore, we have

$$
\begin{array} { l } { d _ { \gamma } \bigl ( \mu _ { 1 } , \mu _ { 0 } \bigr ) = \underset { f \in C _ { \tau } ^ { \prime } (  { \mathbb { R } } ^ { D } ) } { \operatorname* { s u p } } \overline { { \frac { C } { C } } } \int _ {  { \mathbb { \widetilde { M } } } } f ( x ) \left( \mathrm { d } ( [ G _ { 0 } ] _ { \# } \nu _ { 1 } ] - \mathrm { d } [ G _ { 0 } ] _ { \# } \nu _ { 0 } \right) } \\ { \ \qquad \geq \underset { f \in C _ { \tau } ^ { \prime } (  { \mathbb { R } } ^ { D } ) } { \operatorname* { s u p } } \overline { { \frac { C } { C } } } \int _ {  { \mathbb { R } } _ { 1 } ^ { \pm } } f \circ G _ { 0 } ( z ) \cdot \bigl ( \nu _ { 1 } ( z ) - \nu _ { 0 } ( z ) \bigr ) \mathrm { d } z } \\ { \ \geq \frac { c _ { 1 } \widetilde C } { C } \sqrt { n } \int _ {  { \mathbb { R } } _ { 1 } ^ { \pm } } \bigl ( \nu _ { 1 } ( z ) - \nu _ { 0 } ( z ) \bigr ) ^ { 2 } \mathrm { d } z } \\ { \ = \frac { c _ { 1 } c ^ { 2 } \widetilde C } { C \sqrt { n } } \int _ {  { \mathbb { R } } _ { 1 } ^ { \pm } } \prod _ { j = 1 } ^ { d } \mathbb { E } ^ { 2 } ( z _ { j } ) \mathrm { d } z \geq \frac { c _ { 3 } } { \sqrt { n } } , } \end{array}
$$

for some constant $c _ { 3 }$ .

# D.2 Proofs of lemmas in Section 4.4 for minimax upper bound

In this subsection, we provide proofs for Lemmas 7, 4, 5 and 6. In the following proofs, we only consider those $m \in [ M ]$ such that $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ log n . In fact, by applying Bernstein’s inequality for a binomial random variable and a union bound argument, we obtain that, for any constant $c$ , there exits a constant $c _ { 1 }$ such that with probability at least $1 - n ^ { - c }$ ,

$$
\operatorname* { s u p } _ { m \in [ M ] } \big | \widehat { p } _ { m } - \mathbb { P } _ { \mu ^ { * } } \big ( X \in S _ { m } ^ { \dagger } \big ) \big | \leq c _ { 1 } \Big ( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \sqrt { \mathbb { P } _ { \mu ^ { * } } \big ( X \in S _ { m } ^ { \dagger } \big ) } \Big ) .
$$

Therefore, if Pµ∗ (X ∈ S†m) ≤ 12 q , then there exists some sufficiently large integer $n _ { 0 }$ such that when $n \geq n _ { 0 }$ , it holds with probability at least $1 - n ^ { - c }$ that ${ \widehat { p } } _ { m } < { \sqrt { \frac { \log n } { n } } }$ , which leads to

$$
\begin{array} { r l r } & { } & { \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] - \widehat { \mathcal { I } } _ { m } ( f ) \Big | \overset { ( i ) } { = } \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] \big | } \\ & { } & { \leq \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \leq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } , } \end{array}
$$

where we have used in step (i) the definition of $\widehat { \mathcal { I } } _ { m }$ that $\widehat { \mathcal { I } } _ { m } ( f ) \equiv 0$ if ${ \widehat { p } } _ { m } < { \sqrt { \frac { \log n } { n } } }$ . On the other hand, if ${ \widehat { p } } _ { m } < { \sqrt { \frac { \log n } { n } } }$ , then it holds with probability larger than $1 - n ^ { - c }$ that

$\mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \le 2 { \sqrt { \frac { \log n } { n } } }$ . Thus ${ \widehat { p } } _ { m } < { \sqrt { \frac { \log n } { n } } }$ can lead to

$$
\begin{array} { r l r } & { } & { \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] - \widehat { \mathcal { I } } _ { m } ( f ) \Big | = \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) \cdot \rho _ { m } ( X ) ] \big | } \\ & { } & { \leq \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \leq 2 \sqrt { \frac { \log n } { n } } . } \end{array}
$$

In the proofs, we consider a fixed $\mu ^ { * } \in S ^ { * }$ . From the definition of $S ^ { * }$ , we have that for each $m \in \lfloor M \rfloor$ , there exists $\widetilde { S } _ { m } \supseteq \mathbb { B } _ { r _ { m } + 1 / L } \big ( a _ { m } \big )$ such that $\mu ^ { * } | _ { \widetilde { S } _ { m } } = [ G _ { [ m ] } ^ { * } ] \# \nu _ { [ m ] } ^ { * }$ for some generative model pair $( \nu _ { [ m ] } ^ { * } , G _ { [ m ] } ^ { * } )$ satisfying the conditions in Section B. In particular, we use $Q _ { [ m ] } ^ { * }$ to denote the smooth extension of the inverse of $G _ { [ m ] } ^ { * } | _ { \mathbb { B } _ { 1 } ^ { d } }$ from submanifold $\mathcal { M }$ to the entire ambient space $\mathbb { R } ^ { D }$ therein. Recall equation (24), in the following proofs, we will abuse the notation to use $( \widehat { \mathcal { I } } _ { m , l } ( f ) , \widehat { \mathcal { I } } _ { m , h } ( f ) , \widehat { \mathcal { I } } _ { m , s } ( f ) )$ to denote the term in the right hand side of (12a), (12b) and (12c) respectively for any $m \in \mathbb { M } = \{ m \in [ M ] \ : \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \geq$ $\textstyle { \frac { 1 } { 2 } } { \sqrt { \frac { \log n } { n } } } \}$ , regardless of the value $\widehat { p } _ { m }$ , and we will show that $( \widehat { \mathcal { I } } _ { m , l } ( f ) , \widehat { \mathcal { I } } _ { m , h } ( f ) , \widehat { \mathcal { I } } _ { m , s } ( f ) )$ is close to $( \mathcal { I } _ { m , l } ( \boldsymbol { f } ) , \mathcal { I } _ { m , h } ( \boldsymbol { f } ) , \mathcal { I } _ { m , s } ( \boldsymbol { f } ) )$ for each $m \in \mathbb { M }$ .

# D.2.1 Proof of Lemma 7

Fix an $m \in \mathbb { M }$ . Recall $\mu ^ { * } | _ { \widetilde { S } _ { m } } = [ G _ { [ m ] } ^ { * } ] _ { \# } \nu _ { [ m ] } ^ { * }$ , where:

1. $G _ { [ m ] } ^ { * } | _ { \mathbb { B } _ { 1 } ^ { d } }$ has a smooth inverse $Q _ { [ m ] } ^ { \ast } \in C _ { L } ^ { \gamma } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ such that $Q _ { [ m ] } ^ { * } \circ [ G _ { [ m ] } ^ { * } | _ { \mathbb { B } _ { 1 } ^ { d } } ] = \mathrm { i d } _ { \mathbb { B } _ { 1 } ^ { d } }$ ; 2. $\nu _ { [ m ] } ^ { * }$ is a probability distribution supported on $\mathbb { B } _ { 1 } ^ { d }$ with $\alpha$ -smooth density function (also denoted by $\nu _ { [ m ] } ^ { * }$ ) satisfying $e ^ { - L } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } } \leq \nu _ { [ m ] } ^ { \ast } ( z ) \leq e ^ { L } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } }$ for all $z \in \mathbb { B } _ { 1 } ^ { d }$ for some $L _ { 0 } \geq 0$ .

Let $\widehat { f } _ { [ m ] } = \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } \circ G _ { [ m ] } ^ { \ast } : \mathbb { B } _ { 1 } ^ { d } \to \mathbb { R } ^ { D }$ . Then for any $\eta > 0$ , we have

$$
\begin{array} { r l } & { \quad \mathbb { E } _ { \mu ^ { * } } \bigl [ \| X - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \| _ { 2 } ^ { \eta } \rho _ { m } ( X ) \bigr ] } \\ & { = \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot \int \| x - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( x ) ) \| _ { 2 } ^ { \eta } \cdot \rho _ { m } ( x ) \mathrm { d } \bigl ( [ G _ { [ m ] } ^ { * } ] _ { \# } \nu _ { [ m ] } ^ { * } ( x ) \bigr ) } \\ & { \overset { ( i ) } { = } \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot \int _ { \mathbb { B } _ { 1 } ^ { d } } \| G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } ^ { \eta } \cdot \rho _ { m } \bigl ( G _ { [ m ] } ^ { * } ( z ) \bigr ) \cdot \nu _ { [ m ] } ^ { * } ( z ) \mathrm { d } z , } \end{array}
$$

where step (i) follows by applying the change of variable of $x = G _ { [ m ] } ^ { * } ( z )$ and $\nu _ { [ m ] } ^ { * }$ is supported on $\mathbb { B } _ { 1 } ^ { d }$ .

Let $\widetilde { n } = n \cdot \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } )$ , since we only consider those $m \in [ M ]$ such that $\mathbb { P } _ { \mu ^ { * } } ( X \in$ $\widetilde { S } _ { m } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } }$ (recall √ $\widetilde { S } _ { m } \supset \mathbb { B } _ { r _ { m } + 1 / L } ( a _ { m } ) \supset \mathbb { B } _ { r _ { m } + 1 / ( 2 L ) } ( a _ { m } ) = S _ { m } ^ { \dagger }$ and equation (23)), it holds that $\widetilde { n } \ge \frac { 1 } { 2 } \sqrt { n \log n }$ . Let $S _ { m } = \mathbb { B } _ { r _ { m } } ( a _ { m } )$ , we resort to the following lemma that provides an upper bound on $\Vert G _ { [ m ] } ^ { \ast } ( z ) - \widehat { f } _ { [ m ] } ( z ) \Vert _ { 2 }$ for all $z \in \mathbb { B } _ { 1 } ^ { d }$ such that $G _ { [ m ] } ^ { \ast } ( z ) \in S _ { m }$ .

Lemma 10. It holds with probability at least $1 - n ^ { - c }$ that for all $z \in \mathbb { B } _ { 1 } ^ { d }$ such that

$$
\begin{array} { c } { { G _ { [ m ] } ^ { \ast } ( z ) \in S _ { m } , } } \\ { { \displaystyle \qquad \| G _ { [ m ] } ^ { \ast } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } \leq C \operatorname* { m i n } \Big \{ \Big ( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } } } \Big ) ^ { \frac { \beta } { d } } , \Big ( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { \beta } { d + L _ { 0 } } } \Big \} . } } \end{array}
$$

A proof of this lemma is provided in Section E.8. Another way to state the lemma is that for some constant $c _ { 0 }$ , we have

$$
\| G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } \leq \left\{ \begin{array} { l l } { C \big ( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } } } \big ) ^ { \frac { \beta } { d } } } & { \mathrm { i f ~ } \| z \| _ { 2 } \leq 1 - \delta _ { n } ; } \\ { C \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { \beta } { d + L _ { 0 } } } } & { \mathrm { i f ~ } 1 - \delta _ { n } \leq \| z \| _ { 2 } \leq 1 , } \end{array} \right.
$$

where $\delta _ { n } = c _ { 0 } \Big ( \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { 1 } { d + L _ { 0 } } }$ . The increasing pointwise estimation error around the boundary of $\mathbb { B } _ { 1 } ^ { d }$ ecan be explained by less samples around the boundary — $\nu _ { [ m ] } ^ { * } ( z )$ has the decay rate $( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } }$ as $\| z \|$ approaches one. In addition, notice that, by the condition on $\nu _ { [ m ] } ^ { * }$ , for those $z$ satisfying $1 - \delta _ { n } \leq \| z \| _ { 2 } \leq 1$ we have $\begin{array} { r } { \nu _ { [ m ] } ^ { * } ( z ) \leq e ^ { L } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } } \leq C \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { L _ { 0 } } { d + L _ { 0 } } } } \end{array}$ . Combining these two properties with equation (25) and the fact that $\rho _ { m }$ is supported on $S _ { m } = \mathbb { B } _ { r _ { m } } ( a _ { m } )$ , we finally obtain that for any $\begin{array} { r } { \eta \in \left( 0 , \frac { d } { \beta } \right] } \end{array}$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \big [ \| X - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \| _ { 2 } ^ { \eta } \rho _ { m } ( X ) \big ] } \\ & { \leq C \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta \eta } { d } } \int _ { \| z \| _ { 2 } \leq 1 - \delta _ { n } } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } ( 1 - \frac { \eta \beta } { d } ) } \mathrm { d } z } \\ & { \qquad + C \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta \eta + L _ { 0 } } { d + L _ { 0 } } } \int _ { 1 - \delta _ { n } \leq \| z \| _ { 2 } \leq 1 } \mathrm { d } z } \\ & { \leq C \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta \eta } { d } } \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta \eta } { d } } , } \end{array}
$$

where in the last step we used the fact that $\log \widetilde { n } \leq \log n$ , $\beta \eta \leq d$ and $\widetilde { n } = n \cdot \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } )$ Since $S _ { m }$ e is a bounded set, we have that for any $\begin{array} { r } { \eta > { \frac { d } { \beta } } } \end{array}$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \bigl [ \| X - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \| _ { 2 } ^ { \eta } \rho _ { m } ( X ) \bigr ] } \\ & { \qquad \leq C _ { 1 } ^ { \eta - \frac { d } { \beta } } \mathbb { E } _ { \mu ^ { * } } \bigl [ \| X - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \| _ { 2 } ^ { \frac { d } { \beta } } \rho _ { m } ( X ) \bigr ] \leq C C _ { 1 } ^ { \eta - \frac { d } { \beta } } \frac { \log n } { n } . } \end{array}
$$

# D.2.2 Proof of Lemma 4

Let $\begin{array} { r } { \zeta = 1 + \gamma \vee \beta \vee \left( \frac { d } { 2 } - \gamma \right) \vee \left( \frac { d } { 2 } - \beta \right) } \end{array}$ ; $\phi _ { \mathfrak { M } } \in C ^ { \zeta } ( \mathbb { R } )$ and $\phi _ { \mathfrak { F } } \in C ^ { \varsigma } ( \mathbb { R } )$ be a compactly supported wavelet and scaling function, respectively, for example Daubechies wavelets [Bouzebda and Didi, 2017, Hütter and Rigollet, 2020]. Recall that any $f \in C ( \mathbb { R } ^ { D } )$ admits the following

$$
f ( \boldsymbol { x } ) = \underbrace { \sum _ { k \in \mathbb { Z } ^ { D } } b _ { k } \phi _ { k } ( \boldsymbol { x } ) + \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { J } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { J } f } + \underbrace { \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { J } ^ { \perp } f } ,
$$

where recall that for any multi-index $k \in \mathbb { Z } ^ { D }$ , the level zero basis $\phi _ { k } \in C ^ { \zeta } ( \mathbb { R } ^ { D } )$ is obtained by translating the $D$ -fold tensor product $\phi _ { \mathfrak { F } } ^ { \otimes D }$ by $k$ as $\begin{array} { r } { \phi _ { k } ( { \boldsymbol x } ) = \prod _ { i = 1 } ^ { D } \phi _ { \mathfrak { F } } ( x _ { i } - k _ { i } ) } \end{array}$ for $x = ( x _ { 1 } , \ldots , x _ { D } ) \in \mathbb { R } ^ { D }$ , and for any $j \geq 1$ , the level $j$ basis $\left\{ \psi _ { l j k } : l \in [ 2 ^ { D } - 1 ] \right\}$ with translation $k$ is any ordering of the following $2 ^ { D } - 1$ functions,

$$
\psi _ { k } ^ { j , g } ( x ) = 2 ^ { \frac { D ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { D } \phi _ { g _ { i } } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) , \quad \forall g \in G = \{ \mathfrak { F } , \mathfrak { M } \} ^ { D } \setminus \{ ( \mathfrak { F } , \dots , \mathfrak { F } ) \} .
$$

In addition, if $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , then it holds for all $k \in \mathbb { Z } ^ { D } , ~ j \in \mathbb { N } _ { 0 }$ and $l \in [ 2 ^ { D } - 1 ]$ that

$$
| b _ { k } | \leq C \quad { \mathrm { a n d } } \quad | f _ { l j k } | \leq C 2 ^ { - { \frac { D j } { 2 } } - j \gamma } .
$$

For ease of notation, we denote $f = f _ { 1 } + f _ { 2 }$ , where $f _ { 1 } = \Pi _ { J } f$ is the projection of $f$ onto the first $J$ level wavelet basis, and $f _ { 2 } = \Pi _ { J } ^ { \perp } f$ the collection of all remaining “higher-frequency” components. Using this notation, fix an $m \in \mathbb { M }$ , we can write

$$
\begin{array} { r l } & { \mathcal { T } _ { m , l } ( f ) = \mathbb { E } _ { \mu ^ { \star } } \bigl [ \rho _ { m } ( X ) \cdot f _ { 1 } \bigl ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \bigr ) \bigr ] } \\ & { \mathbb { E } _ { \mu ^ { \star } } \biggl [ \rho _ { m } ( X ) \biggr ( \underset { k \in \mathbb { Z } ^ { D } } { \sum } b _ { k } \phi _ { k } \bigl ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \bigr ) + \underset { l = 1 } { \overset { 2 ^ { D } - 1 } { \sum } } \underset { j = 1 } { \overset { J } { \sum } } \underset { k \in \mathbb { Z } ^ { D } } { \sum } f _ { l j k } \psi _ { l j k } \bigl ( \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } ( X ) \bigr ) \biggr ) \biggr ] , } \end{array}
$$

where the expectation is taken with respect to $X \sim \mu ^ { * }$ (not the randomness in $\widehat { G } _ { [ m ] }$ and $\widehat { Q } _ { [ m ] }$ ). Define

$$
\begin{array} { r l } & { \widetilde { \mathbb { S } } = \left\{ k \in \mathbb { Z } ^ { D } : \operatorname { s u p p } ( \phi _ { k } ) \cap \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } \circ G _ { [ m ] } ^ { \ast } ( \mathbb { B } _ { 1 } ^ { d } ) \neq \emptyset \right\} ; } \\ & { \widetilde { \mathbb { S } } _ { l j } = \left\{ k \in \mathbb { Z } ^ { D } : \operatorname { s u p p } ( \psi _ { l j k } ) \cap \widehat { G } _ { [ m ] } \circ \widehat { Q } _ { [ m ] } \circ G _ { [ m ] } ^ { \ast } ( \mathbb { B } _ { 1 } ^ { d } ) \neq \emptyset \right\} . } \end{array}
$$

Then there exists a constant $C$ such that $| \widetilde { \mathbb { S } } | \leq C$ . Moreover, by the Lipschitzness of $\hat { G } _ { [ m ] }$ $\hat { Q } _ { [ m ] }$ , $G _ { [ m ] } ^ { * }$ , and the fact that the support of $\psi _ { l j k }$ is contained in $\mathbb { B } _ { 2 ^ { - j } C _ { 0 } } \left( 2 ^ { 1 - j } k \right)$ for some

finite constant $C _ { 0 }$ , we can get that $| \widetilde { \mathbb { S } } _ { l j } | \le C 2 ^ { d j }$ . Under this notation, we have

$$
\begin{array} { r l } & { \displaystyle \widehat { \mathcal { T } } _ { m , l } ( f ) - \mathcal { T } _ { m , l } ( f ) \Big | = \bigg | \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } f _ { 1 } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \big ) \cdot \rho _ { m } ( X _ { i } ) - \mathbb { E } _ { \mu ^ { \star } } \big [ f _ { 1 } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \big ) } \\ & { \displaystyle \leq \sum _ { k \in \widehat { \mathbb { S } } } | b _ { k } | \cdot \big | \mathbb { E } _ { \mu ^ { \star } } \big [ \widehat { G } _ { [ m ] } ( \widehat { G } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ( X ) \big ] - \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \phi _ { k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \big ) \cdot \rho _ { m } ( X _ { i } ) } \\ & { \quad \quad + \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = 1 } ^ { J } \sum _ { k \in \widehat { \mathbb { S } } _ { \theta } } | f _ { j k k } | \cdot \Big | \mathbb { E } _ { \mu ^ { \star } } \Big [ \psi _ { l j k } \big ( \widehat { G } _ { [ m ] } ( \widehat { G } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ( X ) \big ] } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } \psi _ { l j k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \big ) \cdot \rho _ { m } ( X _ { i } ) \Big | . } \end{array}
$$

By a similar union bound argument plus Bernstein’s inequality as the proof of (43), we obtain that with probability at least $1 - n ^ { - c }$ ,

$$
\begin{array} { r l } { } & { \underset { \leq \widehat { \Theta } } { \operatorname* { l u p } } \left| \mathbb { E } _ { \mu ^ { * } } \left[ \phi _ { k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ( X ) \right] - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } \phi _ { k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \big ) \cdot \rho _ { m } ( X _ { i } ) \right| \leq C _ { 1 } \sqrt { \frac { 1 } { i } } } \\ & { \mathrm { ~ n d ~ } \left| \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ( X ) \right] - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } \psi _ { l j k } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \big ) \cdot \rho _ { m } ( X _ { i } ) \right| } \\ & { \qquad \leq C _ { 1 } \bigg ( \displaystyle \frac { \log n } { n } \cdot 2 ^ { \frac { D j } { 2 } } + \sqrt { \frac { \log n } { n } } \sqrt { \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } ^ { 2 } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ^ { 2 } ( X ) \right] } \bigg ) } \end{array}
$$

holds for all $1 \leq l \leq 2 ^ { D } - 1$ , $1 \le j \le J$ , $k \in \widetilde { \mathbb { S } } _ { l j }$ , where the second inequality used the property that $\| \psi _ { l j k } \| _ { \infty } \leq C 2 ^ { \frac { D _ { \mathcal { I } } } { 2 } }$ so that the right hand side contains the term $2 ^ { \frac { D j } { 2 } }$ . By combining these two inequalities with inequality (27) and using $\begin{array} { r } { 2 ^ { d J } \leq ( \frac { n } { \log n } ) ^ { \frac { d } { 2 \alpha + d } } } \end{array}$ and $| f _ { l j k } | \le C 2 ^ { - \frac { D j } 2 - j \gamma }$ , we obtain that with probability at least $1 - n ^ { - c }$ ,

$$
\begin{array} { r l } & { \underset { j \in \mathcal { C } _ { 1 } } { \operatorname* { s u p } } | \widehat { J } _ { n , 0 } ( f ) - \widehat { J } _ { n , 0 } ( f ) | } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { 2 n - \gamma _ { 0 } } { 2 n + \lambda } } } \\ & { \qquad + C \sqrt { \frac { \log n } { n } } \cdot \underset { t = 1 } { \overset { 2 p = 1 } { \sum ^ { n } } } \underset { j = 1 } { \overset { 2 p = - 1 } { \sum } } \underset { k \in \mathbb { Z } _ { 1 } } { \overset { \gamma } { \sum } } \underset { k \in \mathbb { Z } _ { 2 } } { \overset { \varepsilon } { \sum } } \sqrt { \underset { k \in \left[ \widehat { \psi } _ { j k } ^ { 2 } \left( \widehat { G } _ { | m | } ( \widehat { G } _ { | m | } ( X ) ) \right) \cdot \widehat { \rho } _ { m } ^ { 2 } ( X ) \right] } } } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { 2 n + \gamma _ { 0 } } { 2 n + \lambda } } } \\ & { \qquad + C \sqrt { \frac { \log n } { n } } \cdot \underset { t = 1 } { \overset { 2 p = - 1 } { \sum } } \underset { j = 1 } { \overset { 2 p = - 1 } } { \overset { 2 p = - 1 } { \sum } } \underset { k \in \mathbb { Z } _ { 2 } } { \overset { \varepsilon } { \sum } } \int _ { k \in \mathbb { Z } _ { 3 } } ^ { \widehat { \varepsilon } } \left[ \underset { \xi \in \left[ \widehat { \psi } _ { j k } ^ { 2 } \left( \widehat { G } _ { | m | } ( \widehat { G } _ { | m | } ( X ) ) \right) \cdot \widehat { \rho } _ { m } ^ { 2 } ( X ) \right] } \right. } \end{array}
$$

Since for any $x \in G _ { [ m ] } ^ { * } ( \mathbb { B } _ { 1 } ^ { d } )$ , there are at most constant many $k$ ’s in $\widetilde { \mathbb { S } } _ { l j }$ such that $\psi _ { l j k } \bigl ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( x ) ) \neq 0$ and $\| \psi _ { l j k } \| _ { \infty } \leq C 2 ^ { \frac { D j } { 2 } }$ , we obtain

$$
\mathbb { E } _ { \mu ^ { * } } \Big [ \sum _ { k \in \widetilde { \mathbb { S } } _ { l j } } \psi _ { l j k } ^ { 2 } \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \big ) \cdot \rho _ { m } ^ { 2 } ( X ) \Big ] \leq C 2 ^ { D j } .
$$

Putting all pieces together, we get that with probability at least $1 - n ^ { - c }$ ,

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left| \widehat { \mathcal { T } } _ { m , l } ( f ) - \mathcal { I } _ { m , l } ( f ) \right| } \\ & { \le C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { 2 \alpha + \gamma \wedge d } { 2 \alpha + d } } + C \sqrt { \frac { \log n } { n } } \cdot \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { J } 2 ^ { j \left( \frac { d } { 2 } - \gamma \right) } } \\ & { \le C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } , } \end{array}
$$

where we have used $2 ^ { J } \leq \left( { \frac { n } { \log n } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ in the last step.

# D.2.3 Proof of Lemma 5

Fix an m ∈ M, let ν ∗[m],Q[m] $\nu _ { _ { [ m ] , } \widehat { Q } _ { [ m ] } } ^ { \ast } \ = \ [ \widehat { Q } _ { [ m ] } ] _ { \# } ( \rho _ { m } \mu ^ { \ast } )$ denote the nonnegative measure (not necessarily a probability measure) obtained as the pushforward measure of $\rho _ { m } \mu ^ { * }$ via map $\widehat { Q } _ { [ m ] }$ , or the measure such that for any test function $g \in C ( \mathbb { R } ^ { D } )$ , the following identity holds,

$$
\int g ( z ) \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( z ) \mathrm { d } z = \mathbb { E } _ { \mu ^ { * } } \bigl [ g ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \bigr ] .
$$

As we will show, the smoothness regularized estimator ν[m],Q attempts to approximate ν ∗[m],Qb[m e b[m]]. This motivates us to study the regularity of ν∗[m],Qb[m] fi s the form of the density function (also de following lemma associated with $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } )$ measure $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * }$ , and shows $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { \ast } \in C _ { C _ { 0 } } ^ { \alpha } ( \mathbb { R } ^ { d } )$ for some sufficiently large constant . As a consequence, we can control the growth of its wavelet expansion coefficients in our analysis to follow. A proof of the lemma is provided in Section E.10.

Lemma 11. Let $\widehat { l } _ { [ m ] } = \widehat { Q } _ { [ m ] } \circ G _ { [ m ] } ^ { * }$ and $\Omega _ { m } = \{ z \in \mathbb { B } _ { 1 } ^ { d } : G _ { [ m ] } ^ { \ast } ( z ) \in \mathbb { B } _ { r _ { m } } ( a _ { m } ) \}$ . Then for all sufficiently large $n$ , it holds with probability at least $1 - n ^ { - c }$ that

1. $\widehat { l } _ { [ m ] }$ is invertible over $\Omega _ { m }$ . If we denote its inverse as $\widehat { l } _ { [ m ] } ^ { - 1 }$ , then $\widehat { l } _ { [ m ] } ^ { - 1 } \in C _ { C _ { 0 } } ^ { \alpha + 1 } \widehat { ( l _ { [ m ] } } ( \Omega _ { m } ) ; \mathbb { R } ^ { d } )$ for some constant $C _ { 0 }$ ;

2. ν ∗[m],Qb[m] admits a density function as

$$
\begin{array} { r } { \iota _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( x ) = \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) \cdot \nu _ { [ m ] } ^ { * } ( \widehat { l } _ { [ m ] } ^ { - 1 } ( x ) ) \cdot \rho _ { m } \big ( G _ { [ m ] } ^ { * } ( \widehat { l } _ { [ m ] } ^ { - 1 } ( x ) ) \big ) \cdot \Big ( \mathrm { d e t } \big ( \mathbf { J } _ { \widehat { l } _ { [ m ] } ^ { - 1 } ( x ) } ^ { T } \mathbf { J } _ { \widehat { l } _ { [ m ] } ^ { - 1 } } ( x ) \big ) \Big ) ^ { \frac { 1 } { 2 } } , } \end{array}
$$

for all $x \in \widehat { l } _ { [ m ] } ( \Omega _ { m } )$ and zero elsewhere. Moreover, the density function belongs to $C _ { C _ { 1 } } ^ { \alpha } ( \mathbb { R } ^ { d } )$ for some constant $C _ { 1 }$ .

Smoothness regularized estimator ν[m],Q[m] constructed based on Wavelet expansion: Note that the support of ν∗[m],Q[m] is contained in $[ - L , L ] ^ { d }$ (since $\widehat { Q } _ { [ m ] } \in$ $C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) )$ , we have the following wavelet expansion,

$$
\begin{array} { r l } & { \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( z ) = \displaystyle \sum _ { k \in \mathbb { S } } a _ { k } ^ { \widehat { Q } _ { [ m ] } } \phi _ { k } ( z ) + \displaystyle \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \displaystyle \sum _ { j = 0 } ^ { + \infty } \displaystyle \sum _ { k \in \mathbb { S } _ { l j } } \theta _ { l j k } ^ { \widehat { Q } _ { [ m ] } } \psi _ { l j k } ( z ) , \quad \mathrm { w i t h } } \\ & { \quad \quad \quad \quad \mathbb { S } = \big \{ k \in \mathbb { Z } ^ { d } : \operatorname { s u p p } ( \phi _ { k } ) \cap [ - L , L ] ^ { d } \neq \emptyset \big \} ; } \\ & { \quad \quad \quad \mathbb { S } _ { l j } = \big \{ k \in \mathbb { Z } ^ { d } : \operatorname { s u p p } ( \psi _ { l j k } ) \cap [ - L , L ] ^ { d } \neq \emptyset \big \} , } \end{array}
$$

where

$$
\begin{array} { r l } & { a _ { k } ^ { \widehat { Q } _ { [ m ] } } = \mathbb { E } _ { \mu ^ { * } } \left[ \phi _ { k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \right] ; } \\ & { \theta _ { l j k } ^ { \widehat { Q } _ { [ m ] } } = \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \right] . } \end{array}
$$

Here, the expectation is taken with respect to $X \sim \mu ^ { * }$ (not the randomness in $\widehat { Q } _ { [ m ] }$ ). According to Lemma 11, we have ν∗[m],Q[m] $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { \ast } \in C _ { C _ { 1 } } ^ { \alpha } ( \mathbb R ^ { d } )$ ∈ C αC (Rd), which implies for all $k \in  { \mathbb { Z } ^ { d } } , \ j \in  { \mathbb { N } } _ { 0 }$ and $l \in [ 2 ^ { d } - 1 ]$ ,

$$
\begin{array} { r } { | a _ { k } ^ { \widehat { Q } _ { [ m ] } } | \leq C \quad \mathrm { a n d } \quad | \theta _ { l j k } ^ { \widehat { Q } _ { [ m ] } } | \leq C 2 ^ { - \frac { d j } { 2 } - j \alpha } . } \end{array}
$$

Recall that the smoothness regularized estimator $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } }$ corresponds to a truncated empirical version of ν∗[m],Q[m] by truncating the expansion at a finite level $J$ such that $2 ^ { J }$ is the largest integer not exceeding $\left( { \frac { n } { \log n } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ , and replacing the wavelet coefficients with their sample averages,

where

$$
\widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) = \sum _ { k \in \mathbb { S } } \widetilde { a } _ { k } ^ { \widehat { Q } _ { [ m ] } } \phi _ { k } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { k \in \mathbb { S } _ { l j } } \widetilde { \theta } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } \psi _ { l j k } ( y ) ,
$$

$$
\begin{array} { l } { { \displaystyle \widetilde { \boldsymbol { a } } _ { k } ^ { \widehat { Q } _ { [ m ] } } = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \phi _ { k } ( \widehat { Q } _ { [ m ] } ( \boldsymbol { X } _ { i } ) ) \cdot \boldsymbol { \rho } _ { m } ( \boldsymbol { X } _ { i } ) } ; } \\ { { \displaystyle \widetilde { \boldsymbol { \theta } } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( \boldsymbol { X } _ { i } ) ) \cdot \boldsymbol { \rho } _ { m } ( \boldsymbol { X } _ { i } ) } . } \end{array}
$$

Note that from

$$
\begin{array} { r l } & { \displaystyle \left. \phi _ { k } ( z ) \right. \le C , \quad \displaystyle \int \phi _ { k } ^ { 2 } ( z ) \mathrm { d } z = 1 ; \quad \mathrm { a n d } } \\ & { \displaystyle \left. \psi _ { l j k } ( z ) \right. \le c 2 ^ { \frac { d j } 2 } , \quad \displaystyle \int \psi _ { l j k } ^ { 2 } ( z ) \mathrm { d } z = 1 , \quad \forall z \in \mathbb { R } ^ { d } , } \end{array}
$$

and $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { \ast } \in C _ { C _ { 1 } } ^ { \alpha } ( \mathbb R ^ { d } )$ , we can get

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \bigl [ \phi _ { k } ^ { 2 } ( \widetilde Q _ { [ m ] } ( X ) ) \cdot \rho _ { m } ^ { 2 } ( X ) \bigr ] \leq C _ { 1 } \displaystyle \int \phi _ { k } ^ { 2 } ( z ) \cdot \nu _ { [ m ] , \widehat Q _ { [ m ] } } ^ { * } ( z ) { \mathrm { d } } z \leq C _ { 2 } , \quad \mathrm { a n d } } \\ & { \mathbb { E } _ { \mu ^ { * } } \bigl [ \psi _ { l j k } ^ { 2 } ( \widehat Q _ { [ m ] } ( X ) ) \rho _ { m } ^ { 2 } ( X ) \bigr ] \leq C _ { 1 } \displaystyle \int \psi _ { l j k } ^ { 2 } ( z ) \cdot \nu _ { [ m ] , \widehat Q _ { [ m ] } } ^ { * } ( z ) { \mathrm { d } } z \leq C _ { 2 } . } \end{array}
$$

In addition since each additive component satisfies $| \phi _ { k } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \cdot \rho _ { m } ( X _ { i } ) | \leq C _ { 0 }$ and $| \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \cdot \rho _ { m } ( X _ { i } ) | \leq C 2 ^ { \frac { d J } { 2 } } \leq C _ { 0 } \sqrt { n }$ for all $j \in [ J ]$ , we can apply the Bernstein inequality plus a simple union bound argument similar to the proof of (43) to obtain that with probability at least $1 - n ^ { - c }$ (note that since $\widehat { Q } _ { [ m ] }$ is constructed from data in $I _ { 1 }$ , it is independent of the data in $I _ { 2 }$ ),

$$
\begin{array} { r } { \underset { k \in \mathbb { S } } { \operatorname* { s u p } } \left| \underbrace { \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \phi _ { k } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \cdot \rho _ { m } ( X _ { i } ) } _ { \widehat { a } _ { k } ^ { \widehat { Q } _ { [ m ] } } } - \underbrace { \mathbb { E } _ { \mu ^ { * } } \big [ \phi _ { k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \big ] } _ { \widehat { a } _ { k } ^ { \widehat { Q } _ { [ m ] } } } \right| \leq C \sqrt { \frac { \log } { n } } } \\ { \underset { j _ { k } \in \mathbb { S } _ { j _ { j } } ^ { d } } { \operatorname* { s u p } } \left| \underbrace { \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \cdot \rho _ { m } ( X _ { i } ) } _ { \widehat { b } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } } - \underbrace { \mathbb { E } _ { \mu ^ { * } } \big [ \psi _ { l j k } ( \widehat { Q } _ { [ m ] } ( X ) ) \cdot \rho _ { m } ( X ) \big ] } _ { \widehat { e } _ { l j k } ^ { \widehat { Q } _ { [ m ] } } } \right| \leq C \sqrt { \frac { \log } { n } } } \end{array}
$$

Recall that from our constructions we have ( $f _ { 2 } = \Pi _ { J } ^ { \perp } f$ )

$$
\begin{array} { r l } & { \mathcal { T } _ { m , h } ( f ) = \mathbb { E } _ { \mu ^ { * } } \bigl [ f _ { 2 } \bigl ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \bigr ) \cdot \rho _ { m } ( X ) \bigr ] } \\ & { \qquad = \displaystyle \int \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \cdot \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( z ) \mathrm { d } z ; } \\ & { \mathcal { \widehat { I } } _ { m , h } ( f ) = \displaystyle \int f _ { 2 } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \widehat { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( z ) \mathrm { d } z } \\ & { \qquad = \displaystyle \int \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { + \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \cdot \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \widehat { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( z ) \mathrm { d } z . } \end{array}
$$

Now we expand the two measures relative to the wavelet basis, take the difference, and

apply inequality (31) to obtain that with probability at least $1 - n ^ { - c }$ ,

$$
\begin{array} { r l } & { \quad \underset { f \in \mathcal { C } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { B } ) } { \operatorname* { s u p } } |  \mathcal { T } _ { m , h } ( f ) - \widehat { \mathcal { T } } _ { m , h } ( f ) |  } \\ & { \leq C \sqrt { \frac { \log n } { n } } \underset { t = 1 } { \overset { 2 ^ { D } - 1 } { \sum } } \underset { j = 1 } { \overset { \leq ^ { \infty } } \sum } \underset { 1 } { \overset { \leq ^ { \infty } } \sum } \underset { k \in \mathcal { S } _ { k \in \mathbb { Z } ^ { D } } } { \sum } \underset { l ^ { f } \leq 0 } { \sum } \underset { k \in \mathcal { Z } ^ { D } } { \sum } | f _ { l j k } | \cdot \displaystyle \int | \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \phi _ { k ^ { \prime } } ( z ) | \mathrm { d } z } \\ &  \quad + C \sqrt { \frac { \log n } { n } } \underset { \underset { l = 1 } { \overset { 2 ^ { D } - 1 } { \sum } } } { \overset { \leq ^ { \infty } } \underset { j = 1 } { \overset { \leq } } \underset { j = 1 } { \overset { \leq } } \underset { j = 1 } { \overset { \leq } } \underset { k ^ { \prime } = 0 } { \overset { \leq } } \underset { j = 1 } { \overset { \leq } } \underset { k ^ { \prime } = 0 } { \overset { \leq } } \underset { l ^ { f } \geq 0 } { \sum } \underset { k \in \mathcal { S } _ { l ^ { \prime } , j ^ { \prime } } \leq \mathbb { E } \underset { k \in \mathbb { Z } ^ { D } } { \sum } } [ f _ { l j k } | \cdot \displaystyle \int | \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \psi _ { l j ^ { \prime } k ^ { \prime } } ( z ) |   \mathrm { d } z  } \\ &  \quad +  \underset { l = 1 } { \overset { 2 ^ { D } - 1 } { \sum } } \underset { j = 1 }  \overset { + \infty } \end{array}
$$

For the first term, since for any $z \in \mathbb { R } ^ { d }$ , there exists a constant $C$ such that $\begin{array} { r } { \sum _ { k ^ { \prime } \in \mathbb { S } } \left| \phi _ { k ^ { \prime } } ( z ) \right| \leq } \end{array}$ $C$ and $\begin{array} { r } { \sum _ { k \in \mathbb { Z } ^ { D } } | \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) | \leq C 2 ^ { \frac { D _ { j } } { 2 } } } \end{array}$ (each $\phi _ { k }$ or $\psi _ { l j k }$ is compactly supported), we can get

$$
\begin{array} { r l } & { \sqrt { \displaystyle \frac { \log n } { n } } \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { + \infty } \sum _ { k ^ { \prime } \in \mathbb S } \sum _ { k \in \mathbb Z ^ { D } } \left. f _ { l j k } \right. \cdot \displaystyle \int \left. \psi _ { l j k } ( \widehat G _ { [ m ] } ( z ) ) \cdot \phi _ { k ^ { \prime } } ( z ) \right. \mathrm { d } z } \\ & { \le C \sqrt \displaystyle \frac { \log n } { n } \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { + \infty } 2 ^ { - j \gamma } \sum _ { k ^ { \prime } \in \mathbb S } \int \left. \phi _ { k ^ { \prime } } ( z ) \right. \mathrm { d } z } \\ & { \le C _ { 1 } \sqrt \displaystyle \frac { \log n } { n } \sum _ { j = J + 1 } ^ { + \infty } 2 ^ { - j \gamma } \le C _ { 2 } \left( \displaystyle \frac { \log n } { n } \right) ^ { \frac 1 2 + \frac { \gamma } { 2 \alpha + d } } , } \end{array}
$$

where in the first inequality we used the bound $| f _ { l j k } | \le C 2 ^ { - \frac { D j } { 2 } - j \gamma }$

Similarly, for the second term, using the additional fact that for any $z \in \mathbb { R } ^ { d }$ , there exists a constant $C$ such that $\begin{array} { r } { \sum _ { k ^ { \prime } \in \mathbb { S } _ { l ^ { \prime } j ^ { \prime } } } | \psi _ { l ^ { \prime } j ^ { \prime } k ^ { \prime } } ( z ) | \le C 2 ^ { \frac { d j } { 2 } } } \end{array}$ (each $\psi _ { l ^ { \prime } j ^ { \prime } k ^ { \prime } }$ is compactly supported), we have

$$
\begin{array} { r l } & { \sqrt { \displaystyle \frac { \log n } { n } } \sum _ { i = 1 } ^ { 2 ^ { p } - 1 } \displaystyle \sum _ { j = 2 + 1 } ^ { 2 \delta - 1 } \displaystyle \sum _ { i ^ { - } = 1 } ^ { j } \sum _ { j = 0 } ^ { \zeta } \sum _ { k \in \mathbb { Z } _ { k , j } ^ { \prime } \colon k \in \mathbb { Z } ^ { 2 } } | f _ { i j k } | \cdot \displaystyle \int \left| \psi _ { i j k } ( \widehat G _ { [ m ] } ( z ) ) \cdot \psi _ { i ^ { p } , j ^ { s } ( z } ) \right| \mathrm { d } z } \\ & { \leq C \sqrt { \displaystyle \frac { \log n } { n } } \displaystyle \sum _ { i = 1 } ^ { 2 ^ { p } - 1 } \displaystyle \sum _ { j = 2 + 1 } ^ { \infty } \sum _ { i ^ { - } = 1 } ^ { 2 ^ { d - } - 1 } \displaystyle \sum _ { j = 0 } ^ { j } \sum _ { k \in \mathbb { Z } _ { k , j ^ { \prime } } } ^ { - 2 - \delta - 1 } \displaystyle \sum _ { j = 2 } ^ { - \delta - j } \displaystyle \sum _ { k \in \mathcal { Z } ^ { p } } \left| \psi _ { i j k } ( \widehat G _ { [ m ] } ( z ) ) \right| \cdot | \psi _ { i ^ { p } j k ^ { r } } ( z ) | \mathrm { d } z } \\ & { \leq C _ { 1 } \sqrt { \displaystyle \frac { \log n } { n } } \displaystyle \sum _ { i = 1 } ^ { 2 ^ { p } - 1 } \displaystyle \sum _ { j = 2 + 1 } ^ { \infty } \sum _ { i ^ { - } = 1 } ^ { 2 ^ { d - } 1 } \displaystyle \sum _ { j = 0 } ^ { j } \displaystyle \sum _ { k ^ { \prime } \in \mathbb { Z } _ { k , j ^ { \prime } } } ^ { - 2 } \displaystyle \sum _ { i ^ { \prime } \in \mathbb { Z } _ { k , j ^ { \prime } } } ^ { - 1 } \displaystyle \sum _ { j = 1 } ^ { \lfloor \psi _ { i j k ^ { \prime } } ( z ) \rfloor } | \mathrm { d } z } \\ &  \leq C _ { 2 } \sqrt { \displaystyle \frac { \log n } { n } } \displaystyle \sum _  i = 2  \end{array}
$$

where in the first inequality we used the bound $| f _ { l j k } | \le C 2 ^ { - \frac { D j } { 2 } - j \gamma }$ .

For the third term, we similarly get

$$
\begin{array} { r l } & { \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = J + 1 } ^ { + \infty } \displaystyle \sum _ { \substack { l ^ { \prime } = J + 1 } } ^ { 2 ^ { d - 1 } } \displaystyle \sum _ { j ^ { \prime } = J + 1 } ^ { + \infty } \displaystyle \sum _ { k ^ { \prime } \in \mathbb S _ { t ^ { \prime } j ^ { \prime } k } } \displaystyle \sum _ { k \in \mathbb Z ^ { D } } \left| f _ { l j k } \right| \cdot | \theta _ { l ^ { \prime } j ^ { \prime } k ^ { \prime } } ^ { \widehat { Q } _ { [ m ] } } | \cdot \displaystyle \int \left| \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \cdot \psi _ { \nu j ^ { \prime } k ^ { \prime } } ( z ) \right| \mathrm { d } z } \\ & { \leq C \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = J + 1 } ^ { + \infty } \displaystyle \sum _ { l ^ { \prime } = 1 } ^ { 2 ^ { d - 1 } } \displaystyle \sum _ { j ^ { \prime } = J + 1 } ^ { + \infty } 2 ^ { - \frac { D _ { l } ^ { \prime } } { 2 } - j ^ { \prime } } \cdot 2 ^ { - \frac { d _ { l ^ { \prime } } ^ { \prime } } { 2 } - j ^ { \prime } \alpha } \displaystyle \int \sum _ { k \in \mathbb Z ^ { D } } \left| \psi _ { l j k } ( \widehat { G } _ { [ m ] } ( z ) ) \right| \displaystyle \sum _ { k ^ { \prime } \in \mathbb S _ { t ^ { \prime } j ^ { \prime } } } | \psi _ { l ^ { \prime } j ^ { \prime } k ^ { \prime } } ( z ) | } \\ & { \leq C _ { 1 } \displaystyle \sum _ { j = J + 1 } ^ { + \infty } \displaystyle \sum _ { j ^ { \prime } = J + 1 } ^ { + \infty } 2 ^ { - j ^ { \prime } } \cdot 2 ^ { - j ^ { \prime } \alpha } \leq C _ { 2 } \displaystyle ( \frac { \log n } { n } ) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } , } \end{array}
$$

where in the first inequality we used the bound $| f _ { l j k } | \le C 2 ^ { - \frac { D j } { 2 } - j \gamma }$ and $| \theta _ { l ^ { \prime } j ^ { \prime } k ^ { \prime } } ^ { \widehat { Q } _ { [ m ] } } | \leq C 2 ^ { - \frac { d j ^ { \prime } } { 2 } - j ^ { \prime } \alpha }$ Putting all pieces together, we can reach the desired inequality.

Smoothness regularized estimator ν[m],Q constructed based on kernel density estimation: Note that for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ and $\boldsymbol { x } \in \mathbb { R } ^ { D }$

$$
\begin{array} { r l } & { f _ { 2 } ( x ) = \Pi _ { J } ^ { \perp } f ( x ) = \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( x ) } \\ & { \qquad \stackrel { ( i ) } { \le } C \displaystyle \sum _ { j = J + 1 } ^ { \infty } 2 ^ { - j \gamma } \le C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \gamma } { 2 \alpha + d } } , } \end{array}
$$

where $( i )$ uses that the support of $\psi _ { l j k }$ is contained in $B _ { 2 ^ { - j } C _ { 0 } } ( 2 ^ { 1 - j } k )$ , $\| \psi _ { l j k } \| _ { \infty } \leq C _ { 0 } 2 ^ { \frac { D _ { \mathcal { I } } } { 2 } }$ and $\left| f _ { l j k } \right| \le C _ { 0 } 2 ^ { - \frac { D j } { 2 } - j \gamma }$ . We claim that it suffices to show that with probability $1 - n ^ { - c }$

$$
\int \big | \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( z ) - \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( z ) \big | \mathrm { d } z \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha } { 2 \alpha + d } } .
$$

Indeed, under (32), we have for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ ,

$$
\begin{array} { r l } & { | \widehat { \mathcal { T } } _ { m , h } ( f ) - \mathcal { T } _ { m , h } ( f ) | } \\ & { = \Big | \displaystyle \int f _ { 2 } ( \widehat { G } _ { [ m ] } ( y ) ) \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) \mathrm { d } y - \int f _ { 2 } ( \widehat { G } _ { [ m ] } ( y ) ) \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( y ) \mathrm { d } y \Big | } \\ & { \le \operatorname* { s u p } _ { x \in \mathbb { R } ^ { D } } | f _ { 2 } ( x ) | \displaystyle \int \big | \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) - \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( y ) \big | \mathrm { d } y } \\ & { \le C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } . } \end{array}
$$

Now we prove claim (32) by following the standard analysis for kernel density estimator [Parzen, 1962]. Recall

$$
\widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) = \frac { 1 } { h ^ { d } | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \bigg [ \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { [ m ] , j } ( X _ { i } ) - y _ { j } } { h } \Big ) \Big ) \cdot \rho _ { m } ( X _ { i } ) \bigg ] ,
$$

since $\operatorname { s u p p } ( { \bar { k } } ) \subset [ 0 , 1 ]$ and $\widehat { Q } _ { [ m ] } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ , we have for any $y \notin [ - L - 1 , L + 1 ] ^ { d }$ , $\widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) = \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { \ast } ( y ) = 0$ . Thus we only need to show that with probability $1 - n ^ { - c }$ , for any $y \in [ - L - 1 , L + 1 ] ^ { d }$ ,

$$
\left| \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) - \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( y ) \right| \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha } { 2 \alpha + d } } .
$$

Firstly, we bound the difference between the expectation of $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y )$ and $\nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ^ { * } ( y )$

$$
\begin{array} { r l } & { \mathbb { E } _ { \sigma } ( \mathbb { E } _ { \sigma } ( \frac { 1 } { N } , \frac { 1 } { N } \widetilde { \mathbf { f } } _ { \sigma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } , ( \lambda ) - \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ) ) \cdot \boldsymbol { \hat { \sigma } } _ { \gamma , \eta } ( \lambda ) ) } \\ & { = - 2 \gamma _ { \sigma } \langle X \in \mathbb { S } _ { \sigma } \cdot \mathcal { P } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ) ) ) \cdot ( \mathrm { d e s s } \cdot ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ) ) ) ) ^ { 2 } ) \cdot ( \mathrm { d e s } \cdot ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ( \widetilde { \mathcal { G } } _ { \gamma , \eta } ^ { \lambda } ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ( \mathcal { G } _ { \gamma , \eta } ^ { \lambda } ) ) ) ^ { 2 } ) ) ^ { 2 } ) \cdot  } \\ &   \frac { 1 } { N } \sum _ { \gamma ^ { \prime } } \langle X \in \mathbb { S } _ { \sigma } \cdot \mathcal { G } _ { \gamma , \eta } ^ { \lambda } [ \nu _ { \gamma , \eta } ^   \end{array}
$$

where $( i )$ uses $\mu ^ { * } | _ { \tilde { S } _ { m } } = [ G _ { [ m ] } ^ { * } ] \# \nu _ { [ m ] } ^ { * }$ ; $( i i )$ let $t = ( t _ { 1 } , t _ { 2 } , \cdot \cdot \cdot , t _ { d } )$ with $\begin{array} { r } { t _ { j } = \frac { z _ { j } - y _ { j } } { h } } \end{array}$ , $\nu ^ { \circ } ( y ) =$ $\nu _ { [ m ] } ^ { * } ( \widehat { l } _ { [ m ] } ^ { - 1 } ( y ) ) \cdot \rho _ { m } \big ( G _ { [ m ] } ^ { * } ( \widehat { l } _ { [ m ] } ^ { - 1 } ( y ) ) \big ) \cdot \Big ( \operatorname* { d e t } \big ( \mathbf { J } _ { \widehat { l } _ { [ m ] } ^ { - 1 } ( y ) } ^ { T } \mathbf { J } _ { \widehat { l } _ { [ m ] } ^ { - 1 } } ( y ) \big ) \Big ) ^ { \frac { 1 } { 2 } }$ and uses the fact $\textstyle \int k ( t ) \mathrm { d } t = 1$ ; $( i i i )$ uses the conclusion of Lemma 11 and the fact that $k$ is compactly supported; $( i i i i )$ uses $\begin{array} { r } { \int x ^ { j } k ( x ) = 0 } \end{array}$ for $j \in [ [ \alpha ] ]$ . Then it remains to bound the difference between $\widetilde \nu _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y )$

and its expectation. Since for any $y \in [ - L - 1 , L + 1 ] ^ { d }$ ,

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { l ^ { 2 d } } \int \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ^ { 2 } \Big ( \frac { \hat { Q } _ { [ m ] , j } ( X ) - y _ { j } } { h } \Big ) \Big ) \cdot \rho _ { m } ^ { 2 } ( X ) \mathrm { d } \mu ^ { * } } \\ & { = \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } ) } \\ & { \displaystyle \int _ { z \in \mathbb { B } _ { \sqrt { d h } } ( y ) } \frac { 1 } { h ^ { 2 d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ^ { 2 } \big ( \frac { z _ { j } - y _ { j } } { h } \big ) \Big ) \cdot \nu _ { [ m ] } ^ { * } ( \widehat { l _ { [ m ] } } ( z ) ) \cdot \rho _ { m } ^ { 2 } \big ( G _ { [ m ] } ^ { * } ( \widehat { l _ { [ m ] } } ( z ) ) \big ) \cdot \Big ( \mathrm { d e t } \big ( \displaystyle \prod _ { \widehat { l _ { [ m ] } } ( z ) } ^ { T } \mathbb { J } _ { \widehat { l _ { [ m ] } } } ( z ) } \\ & { \le C \frac { 1 } { h ^ { d } } , } \end{array}
$$

and for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ ,

$$
\frac { 1 } { h ^ { d } } \cdot \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat Q _ { [ m ] , j } ( x ) - y _ { j } } { h } \Big ) \Big ) \cdot \rho _ { m } ( x ) \leq C \frac { 1 } { h ^ { d } } .
$$

Now let $\mathcal { N } _ { \frac { 1 } { n ^ { 2 } } } \subset [ - L - 1 , L + 1 ] ^ { d }$ be a $\textstyle { \frac { 1 } { n ^ { 2 } } }$ -covering set $[ - L - 1 , L + 1 ] ^ { d }$ , where $| N _ { \frac { 1 } { n ^ { 2 } } } | \leq C n ^ { 2 d }$ then by a similar union bound argument plus Bernstein’s inequality as the proof of (43), it holds with probability at least $1 - n ^ { - c }$ that for any y ∈ N 1 , it satisfies that

$$
| \mathbb { E } _ { \mu ^ { * } } [ \frac { 1 } { h ^ { d } } \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { [ m ] , j } ( X ) - \widetilde { y } _ { j } } { h } \Big ) ) \cdot \rho _ { m } ( X ) ] - \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( \widetilde { y } ) | \leq C \sqrt { \frac { \log n } { n } } h ^ { - \frac { d } { 2 } } + \frac { \log n } { n } h
$$

Then by the uniformly Lipschitzness of $k ( x )$ and $h = \left( { \frac { \log n } { n } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ , it holds with probability at least $1 - n ^ { - c }$ that

$$
\begin{array} { l } { \displaystyle \operatorname* { s u p } _ { y \in [ - L - 1 , L + 1 ] ^ { d } } \bigg | \mathbb { E } _ { \mu ^ { * } } \left[ \frac { 1 } { h ^ { d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { [ m ] , j } ( X ) - y _ { j } } { h } \Big ) \Big ) \cdot \rho _ { m } ( X ) \right] - \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( y ) \bigg | } \\ { \displaystyle \leq \operatorname* { s u p } _ { \widetilde { y } \in \mathbb { N } _ { \frac { 1 } { n ^ { 2 } } } } \bigg | \mathbb { E } _ { \mu ^ { * } } \left[ \frac { 1 } { h ^ { d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { [ m ] , j } ( X ) - \widetilde { y } _ { j } } { h } \Big ) \Big ) \cdot \rho _ { m } ( X ) \right] - \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } ( \widetilde { y } ) \bigg | + C h ^ { - 1 - d } \frac { 1 } { \overline { { n ^ { 2 } } } } } \\ { \displaystyle \leq C _ { 1 } \big ( \displaystyle \frac { \log n } { n } \big ) ^ { \frac { \alpha } { 2 \alpha + d } } . } \end{array}
$$

We can then obtain the desired result by putting all pieces together.

# D.2.4 Proof of Lemma 6

For any $m \in \mathbb { M }$ , by applying the Taylor expansion to any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , we obtain that

$$
\begin{array} { r l } & { \underset { f \in { \cal C } _ { 1 } ^ { \ast } ( { \mathbb { R } ^ { D } } ) } { \operatorname* { s u p } } \bigg | \underset { { \textstyle \sum \mu ^ { \ast } } \left[ f \left( X \right) \cdot \rho _ { m } \left( X \right) \right] - \textstyle \mathbb { E } _ { \mu ^ { \ast } } \left[ f \left( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) \right) \cdot \rho _ { m } \left( X \right) \right] } { \operatorname* { s u p } } } \\ & { \qquad + \underset { { \textstyle \sum \mu \in \mathbb { N } _ { 0 } ^ { D } } } { \sum } \mathbb { E } _ { \mu ^ { \ast } } \Big [ \frac { 1 } { j ! } f ^ { ( j ) } ( X ) \left[ \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) - X \right] ^ { j } \rho _ { m } ( X ) \Big ] \bigg | } \\ & { \qquad \quad \overset { { \mathrm { \scriptsize ~ i ~ } \sum | j | \leq | \gamma | } } { \leq } } \\ & { \leq C \mathbb { E } _ { \mu ^ { \ast } } \big [ \| \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) - X \| _ { 2 } ^ { \gamma } \rho _ { m } ( X ) \big ] \leq C \left( \frac { \log n } { n } \right) \vee \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta } { d } } } \end{array}
$$

holds with probability at least $1 - n ^ { - c }$ with respect to the randomness in $( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } )$ (or samples from $I _ { 1 }$ ), where the last inequality is due to Lemma 7. In the rest of the proof, we restrict ourselves to the high probability event where the inequality in Lemma 7 holds for any $\eta \in [ | 2 \gamma | ]$ .

Since $- \hat { \mathcal { I } } _ { m , s } ( f )$ is the sample version (samples from $I _ { 2 }$ ) of the sum in the second line of (33), it remains to derive a high probability bound to

$$
\begin{array} { r l } { V _ { n } ( j ) : = \displaystyle \operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( { \mathbb { R } } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } \big [ f ^ { ( j ) } ( X ) \left( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) - X \right) ^ { j } \rho _ { m } ( X ) \big ] } & { } \\ { \quad \quad \quad - \displaystyle \operatorname* { l } _ { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } f ^ { ( j ) } ( X _ { i } ) \left( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \right) ^ { j } \rho _ { m } ( X _ { i } ) \Big | , } \end{array}
$$

for each $j \in \mathbb { N } _ { 0 } ^ { D }$ and $1 \leq | j | \leq \lfloor \gamma \rfloor$ . Note that we can bound the second moment of the supreme (over $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) )$ of each term inside the sum above as

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \Big [ \underset { f \in C _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | f ^ { ( j ) } ( X _ { i } ) \big | ^ { 2 } \cdot \big | \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \big ) ^ { j } \big | ^ { 2 } \rho _ { m } ^ { 2 } ( X _ { i } ) \Big ] } \\ & { \leq C \mathbb { E } _ { \mu ^ { * } } \big [ \| \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X ) ) - X \| _ { 2 } ^ { 2 \| j \| } \rho _ { m } ( X ) \big ] \leq C _ { 1 } \Big ( \frac { \log n } { n } \Big ) \vee \Big ( \frac { \log n } { n } \Big ) ^ { \frac { 2 \| j \| \beta } { d } } , } \end{array}
$$

where the last step is due to Lemma 7. In addition, each term is almost surely bounded by a constant $C _ { 0 }$ . Therefore, we can apply the Talagrand concentration inequality to obtain that for all $t \geq 0$ ,

$$
\mathbb { P } \Bigg \{ V _ { n } ( j ) \geq \mathbb { E } _ { \mu ^ { * } } [ V _ { n } ( j ) ] + C \sqrt { \frac { t } { n } } \cdot \Big [ \sqrt { \frac { \log n } { n } } \vee \Big ( \frac { \log n } { n } \Big ) ^ { \frac { | j | \beta } { d } } \Big ] + \frac { C t } { n } \Bigg \} \leq 2 e ^ { - t } .
$$

Therefore, with probability at least $1 - n ^ { - c }$ , it holds that

$$
V _ { n } ( j ) \leq \mathbb { E } _ { \mu ^ { * } } [ V _ { n } ( j ) ] + C \sqrt { \frac { \log n } { n } } \cdot \Bigl [ \sqrt { \frac { \log n } { n } } \vee \Bigl ( \frac { \log n } { n } \Bigr ) ^ { \frac { | j | \beta } { d } } \Bigr ] .
$$

It remains to bound the expectation $\mathbb { E } _ { \mu ^ { * } } [ V _ { n } ( j ) ]$ , which by the standard symmetrization argument, satisfies

$$
\cdot [ V _ { n } ( j ) ] \leq \frac { 2 } { \sqrt { | I _ { 2 } | } } \mathbb { E } \bigg [ \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \smash { \prime } } ( \mathbb { R } ^ { D } ) } \bigg | \frac { 1 } { \sqrt { | I _ { 2 } | } } \sum _ { i \in I _ { 2 } } \varepsilon _ { i } f ^ { ( j ) } ( X _ { i } ) \left( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \right) ^ { j } \rho _ { m } ( X _ { i } ) \bigg | \bigg ] ,
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. Rademacher random variables, i.e. $\mathbb { P } ( \varepsilon _ { i } = 1 ) = \mathbb { P } ( \varepsilon _ { i } = - 1 ) = 0 . 5$

Since given $\{ X _ { i } \} _ { i \in I _ { 1 } \cup I _ { 2 } }$ , the stochastic process inside the supreme is a sub-Gaussian process with intrinsic metric

$$
\begin{array} { r l } & { \displaystyle \ d _ { n , j } ( f , \widetilde { f } ) = \sqrt { \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \left[ \big ( f ^ { ( j ) } ( X _ { i } ) - \widetilde { f } ^ { ( j ) } ( X _ { i } ) \big ) \cdot \big ( \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \big ) ^ { j } \cdot \rho _ { m } ( X _ { i } ) \right] ^ { 2 } } } \\ & { \le C \left( \displaystyle \operatorname* { s u p } _ { z \in \mathbb { B } _ { 1 } ^ { d } } \big | f ^ { ( j ) } ( G _ { [ m ] } ^ { * } ( z ) ) - \widetilde { f } ^ { ( j ) } ( G _ { [ m ] } ^ { * } ( z ) ) \big | \right) \cdot \sqrt { \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \| \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \| _ { 2 } ^ { 2 | j | } \cdot \rho _ { m } ^ { 2 } } } \end{array}
$$

We then state the following lemma for bounding the covering entropy of smooth functions with respect to metrics that only concern evaluations of functions in lowdimensional submanifolds. Its proof is provided in Section E.11.

Lemma 12. Let $\mathcal { X } _ { G } = \left\{ \boldsymbol { x } \in \mathbb { R } ^ { D } : \ \boldsymbol { x } = G ( \boldsymbol { z } ) , \boldsymbol { z } \in \mathbb { B } _ { 1 } ^ { d } \right\}$ be a $d$ -dimensional submanifold induced by a Lipschitz continuous map $G : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , then it holds for any $\widetilde { \gamma } > 0$ that

$$
\begin{array} { r } { \log N \big ( C _ { 1 } ^ { \widetilde { \gamma } } ( \mathbb { R } ^ { D } ) , \| \cdot \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } , \epsilon \big ) \leq C \epsilon ^ { - \frac { d } { \widetilde { \gamma } } } , \quad \forall \epsilon > 0 , } \end{array}
$$

where $N ( \mathcal { F } , \widetilde { d } , \epsilon )$ denotes the $\epsilon$ -covering number of function space $\mathcal { F }$ with respect to pseudometric $\hat { d }$ , and $\| f \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } = \operatorname* { s u p } _ { x \in \mathcal { X } _ { G } } \left| f ( x ) \right|$ denotes the functional supreme norm constrained on set $\chi _ { G }$ .

Let $\begin{array} { r } { \mathcal { K } _ { j } = \sqrt { \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \left\| \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) - X _ { i } \right\| _ { 2 } ^ { 2 | j | } \cdot \rho _ { m } ( X _ { i } ) ^ { 2 } } } \end{array}$ . From Lemma 12, we can get

$$
\log N \big ( C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) , d _ { n , j } , \epsilon \big ) \leq C \Big ( \frac { \mathcal { K } _ { j } } { \epsilon } \Big ) ^ { \frac { d } { \gamma - | j | } } , \quad \forall \epsilon > 0 ,
$$

where we used the fact that for all $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , $f ^ { ( j ) }$ belongs to $C _ { 1 } ^ { \gamma - | j | } ( \mathbb { R } ^ { D } )$ . By Dudley’s entropy integral bound for bounding the expectation of the supreme of sub-Gaussian processes (see for example, Theorem 5.22 of Wainwright [2019]), we obtain

$$
\mathbb { E } _ { \mu ^ { * } } [ V _ { n } ( j ) ] \leq C \mathbb { E } _ { \mu ^ { * } } \left[ \operatorname* { m i n } _ { \delta \in [ 0 , 1 ] } \left\{ \delta + \frac { 1 } { \sqrt { n } } \int _ { \delta } ^ { \kappa _ { j } } \left( \frac { { K } _ { j } } { \epsilon } \right) ^ { \frac { d } { 2 ( \gamma - | j | ) } } \mathrm { d } \epsilon \right\} \right] .
$$

By choosing $\delta = { \mathcal { K } } _ { j } \cdot \left( n ^ { - { \frac { \gamma - | j | } { d } } } \vee { \frac { \log n } { \sqrt { n } } } \right)$ log n √n , we obtain

$$
\mathbb { E } _ { \mu ^ { * } } [ V _ { n } ( j ) ] \leq C \left[ \left( \frac { \log n } { n } \right) ^ { \frac { | j | \beta } { d } } \vee \sqrt { \frac { \log n } { n } } \right] \cdot \Big [ n ^ { - \frac { \gamma - | j | } { d } } \vee \frac { \log n } { \sqrt { n } } \Big ] ,
$$

where the last step used the fact that

$$
\mathbb { E } [ K _ { j } ] \leq { \sqrt { \mathbb { E } [ K _ { j } ^ { 2 } ] } } = { \sqrt { \mathbb { E } \left[ \left\| { \widehat { G } } ( { \widehat { Q } } ( X ) ) - X \right\| _ { 2 } ^ { 2 \vert j \vert } \rho _ { m } ^ { 2 } ( X ) \right] } } \leq C \left( { \frac { \log n } { n } } \right) ^ { \frac { \vert j \vert \beta } { d } } \vee { \sqrt { \frac { \log n } { n } } }
$$

according to Lemma 7. Finally, putting all pieces together, we obtain by a simple union bound over all $j \in \mathbb { N } _ { 0 } ^ { D }$ , $1 \leq | j | \leq \lfloor \gamma \rfloor$ (at most $C D ^ { \lfloor \gamma \rfloor }$ many) that with probability at least $1 - c _ { 1 } n ^ { - c _ { 2 } }$ ,

$$
\begin{array} { r l } & { \underset { j \in \mathbb { N } _ { 0 } ^ { D } } { \operatorname* { s u p } } V _ { n } ( j ) \leq C \underset { \stackrel { j \in \mathbb { N } _ { 0 } ^ { D } } { 1 \leq | j | \leq | \gamma | } } { \operatorname* { s u p } } \left[ \left( \frac { \log n } { n } \right) ^ { \frac { | j | \beta } { d } } \vee \sqrt { \frac { \log n } { n } } \right] \cdot \left[ n ^ { - \frac { \gamma - | j | } { d } } \vee \frac { \log n } { \sqrt { n } } \right] } \\ & { \qquad \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \beta + \gamma - 1 } { d } } \vee \sqrt { \frac { \log n } { n } } . } \end{array}
$$

# E Technical Results and Proofs

In this subsection, we collect all technical results used in the proofs and their proofs.

# E.1 Lemma 13 and its proof

Lemma 13. There exists a constant $C _ { 1 }$ such that for any $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ , it holds with probability larger than $1 - n ^ { - 1 }$ that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \Big | } \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) { \Big | } \leq C _ { 1 } \left( { \sqrt { \frac { \log n } { n } } } \vee n ^ { - { \frac { \gamma } { d } } } \right) .
$$

Moreover, there exist $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ and constant $C _ { 2 }$ such that

$$
\mathbb { E } \Bigg [ \operatorname* { s u p } _ { f \in { C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \Big | \Bigg ] \geq C _ { 2 } \Big ( \sqrt { \frac { 1 } { n } } \vee \frac { n ^ { - \frac { \gamma } { d } } } { \log n } \Big ) .
$$

Proof. We first prove the upper bound. We provide two proofs here: one is based on the usual chaining technique in the empirical process theory; the other is based on embedding the discrimator space $C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ into Besov space $B _ { \infty , \infty } ^ { \alpha } ( \mathbb { R } ^ { D } )$ and truncating the wavelet expansion of $f$ to a proper degree.

• Proof based on chaining technique: Firstly by standard symmetrization argument,

it satisfies

$$
\mathbb { E } _ { \mu ^ { * } } \Bigg [ \operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \Big | \Bigg ] \leq \frac { 2 } { \sqrt { n } } \mathbb { E } \Bigg [ \operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } f ( X _ { i } ) \Big | \Bigg ]
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. Rademacher random variables. Given $\{ X _ { i } \} _ { i \in [ n ] }$ , the stochastic process inside the supreme is a sub-Gaussian process with intrinsic metric

$$
d _ { n } ( f , { \widetilde { f } } ) = { \sqrt { { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } ( f ( X _ { i } ) - { \widetilde { f } } ( X _ { i } ) ) ^ { 2 } } } \leq \operatorname* { s u p } _ { x \in \operatorname { s u p p } ( \mu ^ { * } ) } | f ( x ) - { \widetilde { f } } ( x ) | .
$$

By Lemma 8, there exist a constant $M$ and $\beta$ -smooth functions $\{ G _ { [ m ] } \} _ { m \in [ M ] }$ such that $\begin{array} { r } { \operatorname { s u p p } ( \mu ^ { * } ) \subset \bigcup _ { m = 1 } ^ { M } G _ { [ m ] } ( \mathbb { B } _ { 1 } ^ { d } ) } \end{array}$ . Therefore by Lemma 12, we can get

$$
\log N \big ( C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) , d _ { n } , \epsilon \big ) \leq C \Big ( \frac { 1 } { \epsilon } \Big ) ^ { \frac { d } { \gamma } } , \quad \forall \epsilon > 0 .
$$

By Dudley’s entropy integral bound for bounding the expectation of the supreme of sub-Gaussian processes, we obtain

$$
\mathbb { E } \left[ \operatorname* { s u p } _ { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \Big | \right] \leq C \operatorname* { m i n } _ { \delta \in [ 0 , 1 ] } \Bigg \{ \delta + \frac { 1 } { \sqrt { n } } \int _ { \delta } ^ { 1 } \left( \frac { 1 } { \epsilon } \right) ^ { \frac { d } { 2 \gamma } } \mathrm { d } \epsilon \Bigg \} .
$$

By choosing $\delta = n ^ { - \frac { \gamma } { d } } \vee \frac { \log n } { \sqrt { n } }$ log n √n , we obtain

$$
\mathbb { E } \Bigg [ \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \Big | \Bigg ] \leq C \Big [ n ^ { - \frac { \gamma } { d } } \vee \frac { \log n } { \sqrt { n } } \Big ] .
$$

Then by Talagrand concentration inequality, similar as the proof for Lemma 6 in Section D.2.4, we can obtain that it holds with probability at least $1 - n ^ { - 1 }$ that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left. \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \right. \leq C _ { 1 } \left[ n ^ { - \frac { \gamma } { d } } \vee \frac { \log n } { \sqrt { n } } \right] .
$$

• Proof based on Wavelet expansion: Recall $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ admits the following wavelet expansion

$$
f ( \boldsymbol { x } ) = \underbrace { \sum _ { k \in \mathbb { Z } ^ { D } } b _ { k } \phi _ { k } ( \boldsymbol { x } ) + \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { J } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { J } f } + \underbrace { \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { J } ^ { \perp } f } ,
$$

and here we choose $J$ to be the largest integer such that $\begin{array} { r } { 2 ^ { J } \leq \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { d } } } \end{array}$ . Then it holds

for all $k \in \mathbb { Z } ^ { D } , ~ j \in \mathbb { N } _ { 0 }$ and $l \in [ 2 ^ { D } - 1 ]$ that

$$
| b _ { k } | \leq C \quad { \mathrm { a n d } } \quad | f _ { l j k } | \leq C 2 ^ { - { \frac { D j } { 2 } } - j \gamma } .
$$

We can then write

$$
\begin{array} { r l } { \displaystyle \operatorname* { s u p } _ { \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \Big | \leq \displaystyle \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Pi _ { J } f ( X _ { i } ) \Big | } & { { } } \\ { + \displaystyle \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big [ \big | \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } ^ { \perp } f ( X ) ] \big | + \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Pi _ { J } ^ { \perp } f ( X _ { i } ) \Big | \Big ] . } & { { } } \end{array}
$$

Let $\mathcal { M } = \operatorname { s u p p } ( \mu ^ { * } )$ , define

$$
\begin{array} { r l } & { \widetilde { \mathbb { S } } = \big \{ k \in \mathbb { Z } ^ { D } : \operatorname { s u p p } ( \phi _ { k } ) \cap \mathcal { M } \neq \emptyset \big \} ; } \\ & { \widetilde { \mathbb { S } } _ { l j } = \big \{ k \in \mathbb { Z } ^ { D } : \operatorname { s u p p } ( \psi _ { l j k } ) \cap \mathcal { M } \neq \emptyset \big \} . } \end{array}
$$

Then there exists a constant $C$ such that $| \widetilde { \mathbb { S } } | \leq C$ . Moreover, as by Lemma 8, $\mathcal { M } \subset \bigcup _ { m = 1 } ^ { M } G _ { [ m ] } ( \mathbb { B } _ { 1 } ^ { d } )$ for some $\beta$ -smooth functions $\{ G _ { [ m ] } \} _ { m \in [ M ] }$ and the support of $\psi _ { l j k }$ is contained in $\mathbb { B } _ { 2 ^ { - j } C _ { 0 } } \left( 2 ^ { 1 - j } k \right)$ for some finite constant $C _ { 0 }$ , we can get that $| \widetilde { \mathbb { S } } _ { l j } | \le C 2 ^ { d j }$ .

Under this notation, we have

$$
\begin{array} { r l } & { \underset { f \in { \cal C } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } f ( X ) ] - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \Pi _ { J } f ( X _ { i } ) \Big | } \\ & { \le \displaystyle \sum _ { k \in \widetilde { \mathbb { S } } } \big | b _ { k } \big | \cdot \Big | \mathbb { E } _ { \mu ^ { * } } \big [ \phi _ { k } \big ( X \big ) \big ] - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \phi _ { k } \big ( X _ { i } \big ) \Big | } \\ & { \quad \quad + \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = 1 } ^ { J } \displaystyle \sum _ { k \in \widetilde { \mathbb { S } } _ { i j } } \big | f _ { l j k } \big | \cdot \Big | \mathbb { E } _ { \mu ^ { * } } \big [ \psi _ { l j k } ( X ) \big ] - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \psi _ { l j k } ( X _ { i } ) \Big | . } \end{array}
$$

By a similar union bound argument plus Bernstein’s inequality as the proof of (43), we obtain that with probability at least $1 - n ^ { - 1 }$ ,

$$
\begin{array} { r l } & { \underset { k \in \widetilde { \mathbb { S } } } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu ^ { * } } [ \phi _ { k } ( X ) ] - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \phi _ { k } ( X _ { i } ) \Big | \le C _ { 1 } \sqrt { \frac { \log n } { n } } , } \\ & { \mathrm { a n d ~ } \Big | \mathbb { E } _ { \mu ^ { * } } [ \psi _ { l j k } ( X ) ] - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \psi _ { l j k } ( X _ { i } ) \Big | \le C _ { 1 } \bigg ( \frac { \log n } { n } \cdot 2 ^ { \frac { D / } { 2 } } + \sqrt { \frac { \log n } { n } } \sqrt { \mathbb { E } _ { \mu ^ { * } } \big [ \psi _ { l j k } ^ { 2 } ( X ) \big ] } \bigg ) } \end{array}
$$

holds for all $1 \leq l \leq 2 ^ { D } - 1$ , $1 \le j \le J$ , $k \in \tilde { \mathbb { S } } _ { l j }$ , where the second inequality used the property that $\| \psi _ { l j k } \| _ { \infty } \leq C 2 ^ { \frac { D _ { j } } { 2 } }$ so that the right hand side contains the term $2 ^ { \frac { D j } { 2 } }$ . By combining these two inequalities with inequality (35) and using $2 ^ { d J } \leq \frac { n } { \log n }$

and $| f _ { l j k } | \le C 2 ^ { - \frac { D j } { 2 } - j \gamma }$ , we obtain that with probability at least $1 - n ^ { - 1 }$ ,

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left| \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } f ( X ) ] - \frac { 1 } { n } \overset { n } { \underset { i = 1 } { \sum } } \Pi _ { J } f ( X _ { i } ) \right| } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma _ { \mathrm { e } } } { d } } + C \sqrt { \frac { \log n } { n } } \cdot \overset { 2 ^ { D - 1 } } { \underset { l = 1 } { \sum } } \overset { J } { \underset { j = 1 } { \sum } } 2 ^ { - \frac { D _ { j } } { 2 } - j \gamma } \underset { k \in \widetilde { \widetilde { \widetilde { g } } } _ { i j } } { \sum } \sqrt { \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } ^ { 2 } ( X ) \right] } } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma _ { \mathrm { e } } \sqrt { d } } { d } } + C \sqrt { \frac { \log n } { n } } \cdot \overset { 2 ^ { D - 1 } } { \underset { l = 1 } { \sum } } \underset { j = 1 } { \sum } 2 ^ { - \frac { D _ { j } } { 2 } - j \gamma + \frac { d _ { j } } { 2 } } \sqrt { \underset { k \in \widetilde { \widetilde { g } } _ { i j } } { \sum } \mathbb { E } _ { \mu ^ { * } } \left[ \psi _ { l j k } ^ { 2 } ( X ) \right] } . } \end{array}
$$

Since for any $x \in \mathcal { M }$ , there are at most constant many $k$ ’s in $\widetilde { \mathbb { S } } _ { l j }$ such that $\psi _ { l j k } ( x ) \neq 0$ and $\| \psi _ { l j k } \| _ { \infty } \leq C 2 ^ { \frac { D j } { 2 } }$ , we obtain

$$
\mathbb { E } _ { \mu ^ { * } } \Big [ \sum _ { k \in \widetilde { \mathbb { S } } _ { l j } } \psi _ { l j k } ^ { 2 } ( X ) \Big ] \leq C 2 ^ { D j } .
$$

Then we get that with probability at least $1 - n ^ { - 1 }$ ,

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left| \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } f ( X ) ] - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \Pi _ { J } f ( X _ { i } ) \right| } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \times d } { d } } + C \sqrt { \frac { \log n } { n } } \cdot \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { J } 2 ^ { j \left( \frac { d } { 2 } - \gamma \right) } } \\ & { \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma } { d } } , } \end{array}
$$

where we have used $\begin{array} { r } { 2 ^ { J } \leq \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { d } } } \end{array}$ in the last step. It remains to bound

$$
\begin{array} { r l } & { \underset { f \in \mathcal { C } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left[ \left| \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } ^ { \perp } f ( X ) ] \right| + \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Pi _ { J } ^ { \perp } f ( X _ { i } ) \right| \right] } \\ & { \le \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = J + 1 } ^ { \infty } \sum _ { k \in \widetilde { \mathfrak { S } } _ { l } } \left| f _ { l j k } \right| \cdot \left[ \left| \mathbb { E } _ { \mu ^ { * } } [ \psi _ { l j k } ( X ) ] \right| + \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \psi _ { l j k } ( X _ { i } ) \right| \right] } \\ & { \le C \displaystyle \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \displaystyle \sum _ { j = J + 1 } ^ { \infty } 2 ^ { - \frac { D j } { 2 } - j \gamma } \displaystyle \operatorname* { s u p } _ { x \in M } \big [ \displaystyle \sum _ { k \in \widetilde { \mathfrak { S } } _ { l } } \psi _ { l j k } ( x ) \big ] . } \end{array}
$$

Then by the bound $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { M } } \big [ \sum _ { k \in \widetilde { \mathbb { S } } _ { l j } } \psi _ { l j k } ( x ) \big ] \leq C 2 ^ { - \frac { D _ { j } } { 2 } } } \end{array}$ , we can obtain

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left[ \left| \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } ^ { \perp } f ( X ) ] \right| + \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Pi _ { J } ^ { \perp } f ( X _ { i } ) \right| \right] } \\ & { \leq C \underset { j = J + 1 } { \sum ^ { \infty } } 2 ^ { - j \gamma } \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma } { d } } . } \end{array}
$$

Putting all pieces together, we can obtain it holds with probability at least $1 - n ^ { - 1 }$ that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) \right| \leq C \sqrt { \frac { \log n } { n } } + C \bigl ( \frac { \log n } { n } \bigr ) ^ { \frac { \gamma } { d } } .
$$

The desired upper bound then follows from the bounds derived by the above two methods. We then prove the lower bound. Consider $\mathcal { M } = \{ x = ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { D } ) : \| x _ { 1 : d + 1 } \| ^ { 2 } =$ $1 , x _ { d + 2 : D } = \mathbf { 0 } _ { D - d - 1 } \}$ and $\mu ^ { * }$ being uniform distribution on $\mathcal { M }$ , then $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ .

• Proof for the rate $n ^ { - \frac { \gamma } { d } } \cdot ( \log n ) ^ { - 1 }$ : To prove the desired result, we will construct function $f ^ { * } ( \cdot ; X _ { 1 : n } ) \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ depend on the data $X _ { 1 : n }$ so that

$$
\left| \mathbb { E } _ { \mu ^ { * } } [ f ^ { * } ( X ; X _ { 1 : n } ) ] - n ^ { - 1 } \sum _ { i = 1 } ^ { n } f ^ { * } ( X _ { i } ; X _ { 1 : n } ) \right| \geq C n ^ { - { \frac { \gamma } { d } } } \cdot ( \log n ) ^ { - 1 }
$$

with high probability. The function $f ^ { * } ( \cdot ; X _ { 1 : n } )$ is constructed as follows: let

$$
\begin{array} { r } { k ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \gamma + 1 } t ^ { \gamma + 1 } , \quad t \in ( 0 , 1 ) , } \\ { 0 , \quad \mathrm { ~ o . w . } } \end{array} \right. } \end{array}
$$

Then choose $m = c _ { 0 } n ^ { \frac { 1 } { d } }$ for a large enough constant $c _ { 0 }$ and define

$$
f ^ { * } ( y ; X _ { 1 : n } ) = \frac { 1 } { m ^ { \gamma } \cdot \log n } \cdot \sum _ { i = 1 } ^ { n } \sigma _ { i } ( y ) ,
$$

with

$$
\sigma _ { i } ( y ) = \prod _ { j = 1 } ^ { D } k \big ( m ( y _ { j } - X _ { i , j } + \frac { 1 } { 2 m } ) \big ) ,
$$

where $X _ { i , j }$ and $y _ { j }$ denote the $j$ -th dimension of vectors $X _ { i }$ and $y$ respectively. Then we have the following lemma which implies the desired result.

Lemma 14. There exist constant $c _ { 1 } , c _ { 2 }$ so that it holds with probability larger than $\textstyle { 1 - { \frac { 1 } { n } } }$ that

$$
\begin{array} { r l } & { f ^ { * } ( \cdot ; X _ { 1 : n } ) \in C _ { c _ { 1 } } ^ { \gamma } ( \mathbb { R } ^ { D } ) ; } \\ & { \left| \mathbb { E } _ { \mu ^ { * } } [ f ^ { * } ( X ; X _ { 1 : n } ) ] - n ^ { - 1 } \sum _ { i = 1 } ^ { n } f ^ { * } ( X _ { i } ; X _ { 1 : n } ) \right| \geq c _ { 2 } n ^ { - \frac { \gamma } { d } } \cdot ( \log n ) ^ { - 1 } . } \end{array}
$$

the for $n ^ { - \frac { 1 } { 2 } }$ $\chi : \mathbb { R } \to \mathbb { R }$ $\chi ( t ) = e ^ { - 1 / t }$ $t > 0$ $\chi ( t ) = 0$ $t \leq 0$ $x \in \mathbb { R } ^ { D }$ $\begin{array} { r } { f ( \boldsymbol { x } ) = \sum _ { j = 1 } ^ { D } x _ { j } \cdot \frac { \chi ( 3 / 2 - \| \boldsymbol { x } \| _ { 2 } ) } { \chi ( 3 / 2 - \| \boldsymbol { x } \| _ { 2 } ) + \chi ( \| \boldsymbol { x } \| _ { 2 } - 1 ) } } \end{array}$ Then

$$
\mathbb { E } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) - \mathbb { E } _ { \mu ^ { * } } [ f ( X ) ] \right| = \frac { 1 } { \sqrt { n } } \mathbb { E } \left| \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { D } X _ { i , j } \right| .
$$

Define $\widetilde { Y }$ to be the random variable $\begin{array} { r } { \widetilde { Y } = \sum _ { j = 1 } ^ { D } Y _ { j } } \end{array}$ where $Y = ( Y _ { 1 } , Y _ { 2 } , \cdot \cdot \cdot , Y _ { D } )$ is a random vector from $\mu ^ { * }$ . Then $\mathbb { E } ( \widetilde { Y } ) = 0$ and $\sigma ^ { 2 } = \mathbb { E } [ \widetilde { Y } ^ { 2 } ] > 0$ . So we have

$$
\begin{array} { r l } & { \frac { 1 } { \sqrt n } \mathbb { E } \Big | \displaystyle \frac { 1 } { \sqrt n } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { D } X _ { i , j } \Big | } \\ & { = \displaystyle \frac { 1 } { \sqrt n } \int _ { 0 } ^ { + \infty } \mathbb { P } \Big ( \Big | \displaystyle \frac { 1 } { \sqrt n } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { D } X _ { i , j } \Big | \geq t \Big ) d t } \\ & { \geq \displaystyle \frac { 1 } { \sqrt n } \mathbb { P } \Big ( \Big | \displaystyle \frac { 1 } { \sqrt n } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { D } X _ { i , j } \Big | \geq 1 \Big ) } \\ & { \stackrel { ( i ) } { \geq } \displaystyle \frac { 1 } { \sqrt n } \Big ( \mathbb { P } ( - 1 \leq N ( 0 , \sigma ^ { 2 } ) \leq 1 ) - \displaystyle \frac { C } { \sqrt n } \Big ) \geq \frac { C _ { 1 } } { \sqrt n } , } \end{array}
$$

where inequality (i) is due to Berry-Essen theorem [Raič, 2019]. Proof is completed.

# E.2 Proof of Lemma 14

We first show the smoothness of $f ^ { * } ( \cdot ; X _ { 1 : n } )$ . Recall $m = c _ { 0 } n ^ { \frac { 1 } { d } }$ where $c _ { 0 }$ is a large enough constant so that

$$
\operatorname* { s u p } _ { x \in \mathcal { M } } \left[ \mu ^ { * } \Big ( \prod _ { j = 1 } ^ { D } \big [ x _ { j } - \frac { 2 } { m } , x _ { j } + \frac { 2 } { m } \big ] \Big ) \right] \leq \frac { 1 } { n } .
$$

For any multi-index $a \in \mathbb { N } _ { 0 } ^ { D }$ with $| a | \le \gamma$ , it holds that $\textstyle \operatorname { s u p p } \big ( \prod _ { j = 1 } ^ { D } k ^ { ( a _ { j } ) } ( y _ { j } ) \big ) \subset [ 0 , 1 ] ^ { D }$ and thus $\begin{array} { r } { \operatorname { s u p p } \bigl ( \sigma _ { i } ( y ) \bigr ) \subset \mathcal { A } _ { i } = \prod _ { j = 1 } ^ { D } \big [ - X _ { i , j } - \frac { 1 } { 2 m } , X _ { i , j } + \frac { 1 } { 2 m } \big ] } \end{array}$ . So for any $y \in \mathcal { M }$ , if there exists $i , k \in [ n ]$ so that $\sigma _ { i } ( y ) \neq 0$ and $\sigma _ { k } ( y ) \neq 0$ , then $\begin{array} { r } { X _ { k } \in \prod _ { j = 1 } ^ { D } \left[ X _ { i , j } - \frac { 1 } { m } , X _ { i , j } + \frac { 1 } { m } \right] } \end{array}$ . We claim that it suffices to show that it holds with probability at least $1 - n ^ { - 1 }$ that for any $y \in \mathcal { M }$ ,

$$
{ \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \mathbf { 1 } { \Big ( } X _ { i } \in \prod _ { j = 1 } ^ { D } \left[ y _ { j } - { \frac { 1 } { m } } , y _ { j } + { \frac { 1 } { m } } \right] { \Big ) } \leq C \cdot { \frac { \log n } { n } } .
$$

Indeed, under the above statement, it holds that for any $y \in \mathcal { M }$ and multi-index $a \in \mathbb { N } _ { 0 } ^ { D }$ with $| a | \le \gamma$ ,

$$
\left| \left\{ k \in [ n ] : y \in \operatorname { s u p p } \bigl ( \sigma _ { k } ^ { ( a ) } \bigr ) \right\} \right| \leq C \cdot \log n ,
$$

and hence $f ^ { * } ( \cdot ; X _ { 1 : n } ) \in C _ { c _ { 1 } } ^ { \gamma } ( \mathbb { R } ^ { D } )$ for a constant $c _ { 1 }$ . Now we prove equation (36). Let $\mathcal { N } _ { \frac { 1 } { n } }$ denotes the minimal $n ^ { - 1 }$ -covering set of $\mathcal { M }$ , then $| { \mathcal { N } } _ { \frac { 1 } { n } } | \leq C n ^ { d }$ . Since

$$
\operatorname* { s u p } _ { x \in \mathcal { M } } \left[ \mu ^ { * } \Big ( \prod _ { j = 1 } ^ { D } \big [ x _ { j } - \frac { 2 } { m } , x _ { j } + \frac { 2 } { m } \big ] \Big ) \right] \leq \frac { \log n } { n } ,
$$

by a similar union bound argument plus Bernstein’s inequality as the proof of (43), we can get it holds with probability at least $1 - n ^ { - 1 }$ that for any $\widetilde { y } \in \mathcal N _ { \frac { 1 } { n } }$

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } \bigg ( X _ { i } \in \prod _ { j = 1 } ^ { D } \big [ \widetilde { y } _ { j } - \frac { 2 } { m } , \widetilde { y } _ { j } + \frac { 2 } { m } \big ] \bigg ) \leq C \cdot \frac { \log n } { n } .
$$

Thus for any $y \in \mathcal { M }$ , there exists y ∈ N 1 so that

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } \bigg ( X _ { i } \in \prod _ { j = 1 } ^ { D } \big [ y _ { j } - \frac { 1 } { m } , y _ { j } + \frac { 1 } { m } \big ] \bigg ) \leq \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } \bigg ( X _ { i } \in \prod _ { j = 1 } ^ { D } \big [ \widetilde { y } _ { j } - \frac { 2 } { m } , \widetilde { y } _ { j } + \frac { 2 } { m } \big ] \bigg ) \leq C \cdot \frac { \ln 2 } { n } ,
$$

The proof for the first statement is then completed. For the second statement,

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ^ { * } ( X _ { i } ; X _ { 1 : n } ) - \mathbb { E } [ f ( X _ { \smash { i } } ; X _ { 1 : n } ) ] } \\ & { \displaystyle = ( \log n ) ^ { - 1 } \Big [ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \frac { 1 } { m ^ { \gamma } } \sigma _ { j } ( X _ { i } ) - \mathbb { E } \big [ \sum _ { j = 1 } ^ { n } \frac { 1 } { m ^ { \gamma } } \sigma _ { j } ( X ) \big ] \Big ] } \\ & { \displaystyle \geq \frac { 1 } { m ^ { \gamma } \cdot \log n } \Big [ \sum _ { j = 1 } ^ { n } \big ( \frac { 1 } { n } \sigma _ { j } ( X _ { j } ) - \mu ^ { * } ( A _ { j } ) \mathbb { E } _ { \mu ^ { * } \mid A _ { j } } \big [ \sigma _ { j } ( X ) \big ] \big ) \Big ] } \\ & { \displaystyle \geq C n ^ { - \frac { \gamma } { 4 } } ( \log n ) ^ { - 1 } \operatorname* { i n f } \left[ \Big ( k \big ( \frac { 1 } { 2 } \big ) \Big ) ^ { D } - \mathbb { E } _ { Y \sim \mu ^ { * } \mid A _ { \lambda } } \Big [ \prod _ { i = 1 } ^ { D } k \big ( m ( Y _ { i } - X _ { i } , i - \frac { 1 } { 2 m } ) \big ) \Big ] \right] , } \end{array}
$$

where the last inequality uses the fact $\textstyle \mu ^ { * } ( { \mathcal { A } } _ { j } ) \leq { \frac { 1 } { n } }$ and $m = c _ { 0 } n ^ { \frac { 1 } { d } }$ . The desired conclusion then follows from the fact that $\mu ^ { * }$ is uniform distribution on $\mathcal { M }$ and function $k ( t )$ achieves its unique maximum at point $\begin{array} { r } { t = \frac { 1 } { 2 } } \end{array}$ .

# E.3 Lemma 15 and its proof

Lemma 15. For any probability measure µ in the generative model class $S ^ { * } = S ^ { * } ( D , d , \alpha , \beta , \mathcal { O } _ { M } , L )$ defined in Appendix $B$ , where the property $\boldsymbol { \mathcal { Z } }$ of $S ^ { * }$ is satisfied with pairs $( \nu _ { [ m ] } , G _ { [ m ] } )$ for $m \in \lfloor M \rfloor$ , then $\mu$ can be expressed as a mixture of generative model with rejection sampling:

$$
\mu = \sum _ { m = 1 } ^ { M } w _ { [ m ] } \mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) ,
$$

where (1) $\{ w _ { [ m ] } \} _ { m \in [ M ] }$ are the mixing weights given by $w _ { [ m ] } = \mathbb { E } _ { \mu } [ \rho _ { m } ( X ) ]$ for $m \in \lfloor M \rfloor$ and $\{ \rho _ { m } \} _ { m \in [ M ] }$ is the partition of unity subordinate to ${ \mathcal { O } } _ { M }$ defined in Section 2.4; (2) $\mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } )$ is the probability measure induced by the data generating process where $X \sim [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ is accepted with probability $\rho _ { m } ( X ) \in [ 0 , 1 ]$ .

Proof. For each $m \in [ M ]$ , since the partition of unity $\{ \rho _ { m } \} _ { m \in [ M ] }$ is subordinate to the open cover $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in M }$ , by $\mathbb { B } _ { r _ { m } } ( a _ { m } ) \subset \widetilde { S } _ { m }$ , we have $\operatorname { s u p p } ( \rho _ { m } ) \subset \widetilde { S } _ { m }$ for any $m \in [ M ]$ . Then by the property that $\mu | _ { \widetilde { S } _ { m } } = [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ ,

$$
w _ { [ m ] } = \int \rho _ { m } \mathrm { d } \mu = \mathbb { P } ( X \in \widetilde { S } _ { m } ) \int \rho _ { m } \mathrm { d } \bigl ( [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] } \bigr ) = \mathbb { P } ( X \in \widetilde { S } _ { m } ) \int \mathrm { d } \bigl ( \rho _ { m } [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] } \bigr ) = 0 .
$$

where recall that for any measure $\nu$ , $\rho _ { m } \nu$ stands for the measure whose Radon-Nikodym derivative relative to $\nu$ is $\rho _ { m }$ . Therefore, by the definition of $\mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } )$ , we have that for any measurable function $f : \mathbb { R } ^ { D }  \mathbb { R }$ ,

$$
\begin{array} { r l r } & { } & { \displaystyle { \int } f \mathrm { d } \mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) = \frac { \mathbb { P } ( X \in \widetilde { S } _ { m } ) } { w _ { [ m ] } } \int f \mathrm { d } \big ( \rho _ { m } [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] } \big ) } \\ & { } & { \displaystyle = \frac { \mathbb { P } ( X \in \widetilde { S } _ { m } ) } { w _ { [ m ] } } \int f \rho _ { m } \mathrm { d } \big ( [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] } \big ) . } \end{array}
$$

Moreover, we have, by using the partition of unity $\{ \rho _ { m } \} _ { m \in [ M ] }$ , that

$$
\int f \mathrm { d } \mu = \sum _ { m = 1 } ^ { M } \int f \rho _ { m } \mathrm { d } \mu = \sum _ { m = 1 } ^ { M } \mathbb { P } ( X \in \widetilde { S } _ { m } ) \int f \rho _ { m } \mathrm { d } \bigl ( [ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] } \bigr ) .
$$

By combining the two preceding displays, we obtain $\begin{array} { r } { \mu = \sum _ { m = 1 } ^ { M } w _ { [ m ] } \mathcal { A } ( G _ { [ m ] } , \nu _ { [ m ] } , \rho _ { m } ) } \end{array}$

# E.4 Lemma 16 and its proof

Lemma 16. There exists a set $\{ \omega ^ { ( 1 ) } , \cdot \cdot \cdot , \omega ^ { ( H ) } \} \subset \{ 0 , 1 \} ^ { [ m ^ { d } ] }$ such that $\log H \geq { \frac { m ^ { d } } { 8 } } - \log 2$ and for any $j , k \in [ H ]$ and $j \neq k$ it holds that $\begin{array} { r } { \frac { m ^ { d } } { 4 } \le \rho ( \omega ^ { ( j ) } , \omega ^ { ( k ) } ) \le \frac { 3 m ^ { d } } { 4 } } \end{array}$ 4 , where $\rho ( \omega , \omega ^ { \prime } )$ denotes the Hamming distance between $\omega$ and $\omega ^ { \prime }$ on the hypercube.

Proof. The proof of Lemma 8 is a simple modification of the proof of the Varshamov-Gilbert lemma [Tsybakov, 2009]. We include it here for completeness. Let $\{ \boldsymbol { \omega } ^ { ( 1 ) } , \cdot \cdot \cdot . \boldsymbol { \omega } ^ { ( H ) } \}$ be the largest set satisfying that for any $j , k \in [ H ]$ and $j \neq k$ , $\begin{array} { r } { \frac { m ^ { d } } { 4 } \leq \rho ( \omega ^ { ( j ) } , \omega ^ { ( k ) } ) \leq \frac { 3 m ^ { d } } { 4 } } \end{array}$ . Let $\bar { \omega } = 1 - \omega$ , it holds that

$$
\left\{ 0 , 1 \right\} ^ { m ^ { d } } \subset \left\{ \bigcup _ { i = 1 } ^ { H } B _ { \mathrm { H } } \left( w ^ { ( i ) } , \frac { m ^ { d } } { 4 } \right) \right\} \cup \left\{ \bigcup _ { i = 1 } ^ { H } B _ { \mathrm { H } } \left( \bar { w } ^ { ( i ) } , \frac { m ^ { d } } { 4 } \right) \right\} ,
$$

where $B _ { \mathrm { H } } ( \omega , r )$ denote the ball centered at $\omega$ with radius $r$ with respect to the Hamming

distance. Therefore, we can obtain that

$$
\begin{array} { r l } & { 2 ^ { n ^ { \alpha } } \leq \displaystyle \sum _ { i = 1 } ^ { H } \left| B _ { 1 1 } \left( w ^ { ( i ) } , \frac { \operatorname* { m } ^ { i } } { 4 } \right) \right| + \displaystyle \sum _ { i = 1 } ^ { H } \left| B _ { 1 1 } \left( w ^ { ( i ) } , \frac { \operatorname* { m } ^ { i } } { 4 } \right) \right| } \\ & { \qquad = 2 H \displaystyle \sum _ { i = 0 } ^ { \frac { \alpha ^ { i } } { 4 } } \left( \operatorname* { m } _ { i } ^ { m ^ { i } } \right) } \\ & { \qquad = 2 H \times 2 ^ { n ^ { \alpha } } \times \mathbb { P } \left( \mathrm { B i n o n i a l } ( m ^ { i } , \frac { 1 } { 2 } ) \leq \frac { 1 } { 4 } m ^ { i } \right) } \\ & { \qquad = 2 H \times 2 ^ { n ^ { \alpha } } \times \mathbb { P } \left( \mathrm { B i n o n i a l } ( m ^ { i } , \frac { 1 } { 2 } ) \geq \frac { 3 } { 4 } m ^ { i } \right) } \\ & { \qquad = 2 H \times 2 ^ { n ^ { \alpha } } \times \mathbb { P } \left( \mathrm { B i n o n i a l } ( m ^ { i } , \frac { 1 } { 2 } ) - \frac { 1 } { 2 } m ^ { i } \geq \frac { 1 } { 4 } m ^ { i } \right) } \\ & { \qquad = 2 H \times 2 ^ { n ^ { \alpha } } \times \mathbb { P } \left( \mathrm { B i n o n i a l } ( m ^ { i } , \frac { 1 } { 2 } ) - \frac { 1 } { 2 } m ^ { i } \geq \frac { 1 } { 4 } m ^ { i } \right) } \end{array}
$$

Hoeffding’s inequality [Hoeffding, 1963] then yields,

$$
2 ^ { m ^ { d } } \leq 2 \times 2 ^ { m ^ { d } } \times H \times \exp ( - \frac { m ^ { d } } { 8 } ) ,
$$

implying $\begin{array} { r } { \log H \geq \frac { m ^ { d } } { 8 } - \log 2 } \end{array}$ .

# E.5 Proof of Lemma 9

We first prove the first part on the KL divergence upper bound. Consider the following partition of ambient space $\mathbb { R } ^ { D }$ :

$$
\begin{array} { r l } & { A _ { 1 } = \left\{ x \in \mathbb { R } ^ { d } \bigg | x _ { 1 : d } \in \left[ - \sqrt { \frac { 1 } { 2 d } } + \frac { 1 } { m } \sqrt { \frac { 2 } { d } } , \sqrt { \frac { 1 } { 2 d } } + \frac { 1 } { m } \sqrt { \frac { 2 } { d } } \right] ^ { d } \right. , } \\ & { \qquad \left. x _ { d + 1 } = G _ { u } ( s _ { 1 : d } ) ( x _ { 1 : d + 2 : D } = 0 _ { D - d - 1 } ) \right\} , } \\ & { A _ { 2 } = \left\{ x \in \mathbb { R } ^ { d } \bigg | x _ { 1 : d } \in \mathbb { B } _ { 1 } ^ { d } \backslash \left[ - \sqrt { \frac { 1 } { 2 d } } + \frac { 1 } { m } \sqrt { \frac { 2 } { d } } , \sqrt { \frac { 1 } { 2 d } } + \frac { 1 } { m } \sqrt { \frac { 2 } { d } } \right] ^ { d } \right\} } \\ & { \qquad x _ { d + 1 } = G _ { 0 } ( x _ { 1 : d } ) ; x _ { d + 2 : D } = 0 _ { D - d - 1 } \Bigg \} , } \\ & { A _ { 3 } = M _ { 0 } \backslash \widetilde { M } _ { 0 } , \quad \mathrm { a n d } \quad A _ { 4 } = \mathbb { R } ^ { D } \backslash \left( A _ { 1 } \cup A _ { 2 } \cup A _ { 3 } \right) . } \end{array}
$$

Under this partition, we claim that for any fixed $i \in [ H ]$ ,

1. if $x \in A _ { 1 }$ , then $\begin{array} { r } { \frac { d \mu _ { i } } { d \bar { \mu } } ( x ) = 2 } \end{array}$ ;   
2. if $x \in A _ { 2 } \cup A _ { 3 }$ , then $\begin{array} { r } { \frac { d \mu _ { i } } { d \bar { \mu } } ( x ) = 1 } \end{array}$ ;   
3. for $A _ { 4 }$ , then $\mu _ { i } ( A _ { 4 } ) = \bar { \mu } ( A _ { 4 } ) = 0$ ,

where recall that $\frac { \mathrm { d } P } { \mathrm { d } Q }$ denotes the Radon–Nikodym derivative of $P$ with respect to $Q$ .

In fact, by construction, all $\mu _ { i }$ ’s are the same outside $A _ { 1 }$ , which leads to 2 and 3. To see $^ { 1 }$ , note that by construction, for each index $\xi \in \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ , there are equal numbers of $0$ ’s and $1$ ’s in $\{ \omega _ { \xi } ^ { ( 0 ) } , \cdot \cdot \cdot , \omega _ { \xi } ^ { ( H ) } \}$ . So for each $x \in A _ { 1 }$ , half $\mu _ { i } ( \mathrm { d } x )$ ’s (density with respect to the volume measure of $\mathcal { M } _ { i }$ ) are equal and the rest half of $\mu _ { i } ( \mathrm { d } x )$ ’s are zero, implying that $\begin{array} { r } { \frac { d \mu _ { i } } { d \bar { \mu } } ( x ) = 2 } \end{array}$ . Now let us bound $D _ { \mathrm { K L } } ( \mu _ { i } \mid \mid \bar { \mu } )$ . Using above properties, we obtain $\begin{array} { r } { D _ { \mathrm { K L } } ( \mu _ { i } \| \bar { \mu } ) = \int _ { A _ { 1 } \cup A _ { 2 } \cup A _ { 3 } } \log \frac { d \mu _ { i } } { d \bar { \mu } } \mathrm { d } \mu _ { i } = \log 2 \int _ { A _ { 1 } } \mathrm { d } \mu _ { i } \le \log 2 } \end{array}$ .

Next, we upper bound $\operatorname* { i n f } _ { j , k \in [ H ] } d _ { \gamma } ( \mu _ { j } , \mu _ { k } )$ by constructing discriminator $f$ for discriminating $\mu _ { j }$ and $\mu _ { k }$ so that $\textstyle { \int f ( x ) \mathrm { d } \mu _ { j } - \int f ( x ) \mathrm { d } \mu _ { k } }$ is large, for each distinct index pair $j$ and $k$ . Fix any pair of $j , k \in [ H ]$ with $j \neq k$ , by construction we have $\rho ( \omega ^ { ( j ) } , \omega ^ { ( k ) } ) \geq \frac { m ^ { d } } { 4 }$ 4 . Define

$$
\widetilde { f } ( z ) = \sum _ { \xi \in [ m ] ^ { d } } \left( \frac { 1 } { m } \right) ^ { \gamma } v _ { \xi } \psi _ { \xi } ( z ) ,
$$

where

$$
v _ { \xi } = \left\{ \begin{array} { l } { 1 , \quad \omega _ { \xi } ^ { ( j ) } = 1 \mathrm { ~ a n d ~ } \omega _ { \xi } ^ { ( k ) } = 0 ; \mathrm { ~ o r ~ } \omega _ { \xi } ^ { ( j ) } = \omega _ { \xi } ^ { ( k ) } ; } \\ { - 1 , \quad \omega _ { \xi } ^ { ( j ) } = 0 \mathrm { ~ a n d ~ } \omega _ { \xi } ^ { ( k ) } = 1 . } \end{array} \right.
$$

By the definition of $g _ { \omega } ( z )$ , there exists a constant $c$ such that for any $j \in [ H ]$ , it holds that supp(µ $\begin{array} { r } { \iota _ { \boldsymbol \omega ^ { ( j ) } } ) \subset \mathbb { R } ^ { d } \times \{ x _ { d + 1 } : | x _ { d + 1 } - \sqrt { 2 - \| x _ { 1 : d } \| ^ { 2 } } | \leq \frac { c } { m ^ { \beta } } \} \times \{ ( x _ { d + 2 } , \cdot \cdot , x _ { D } ) ^ { T } = \mathbf { 0 } _ { D - d - 1 } \} } \end{array}$ . Define function $h : \mathbb { R }  \mathbb { R }$ by $\begin{array} { r } { h ( x ) = \operatorname* { m a x } ( - \frac { c } { m ^ { \beta } } } \end{array}$ , $\begin{array} { r } { \operatorname* { m i n } \bigl ( \frac { c } { m ^ { \beta } } , x \bigr ) \bigr ) } \end{array}$ , then $h$ is a 1-Lipschitz function over $\mathbb { R }$ . Recall that $\chi : \mathbb { R } \to \mathbb { R }$ is defined by $\chi ( t ) = e ^ { - 1 / t }$ for $t > 0$ and $\chi ( t ) = 0$ for t ≤ 0. For z ∈ Rd, we define q(z) = p2 − kzk2 · χ(3/2−kzk2)χ(3/2−kzk2)+χ(kzk2−1) . Note that when $z \in \mathbb { B } _ { 1 } ^ { d }$ , $q ( z ) = \sqrt { 2 - \| z \| ^ { 2 } }$ and we multiply $\sqrt { 2 - \| z \| ^ { 2 } }$ by $\frac { \chi ( 3 / 2 - \| z \| _ { 2 } ) } { \chi ( 3 / 2 - \| z \| _ { 2 } ) + \chi ( \| z \| _ { 2 } - 1 ) }$ to smoothly extend $\sqrt { 2 - \| z \| ^ { 2 } }$ from $\mathbb { B } _ { 1 } ^ { d }$ to the entire space. Now define

$$
f ( x ) = \widetilde { f } ( x _ { 1 : d } ) h \big ( x _ { d + 1 } - q ( x _ { 1 : d } ) \big ) m ^ { \gamma - \gamma \beta + \beta } .
$$

We then prove that $f$ is $\gamma$ -smooth with bounded Hölder norm. Since for any $x , x ^ { \prime } \in \mathbb { R } ^ { D }$ , it holds that $\begin{array} { r } { | h \big ( x _ { d + 1 } - q ( x _ { 1 : d } ) \big ) | \leq \frac { c } { m ^ { \beta } } } \end{array}$ and $\begin{array} { r } { | h ( x _ { d + 1 } ^ { \prime } - q ( x _ { 1 : d } ^ { \prime } ) ) | \leq \frac { c } { m ^ { \beta } } } \end{array}$ . Therefore, we have

$$
h \big ( x _ { d + 1 } - q ( x _ { 1 : d } ) \big ) - h \big ( x _ { d + 1 } - q ( x _ { 1 : d } ^ { \prime } ) \big ) | \leq ( 2 c ) ^ { 1 - \gamma } \frac { 1 } { m ^ { \beta ( 1 - \gamma ) } } | h \big ( x _ { d + 1 } - q ( x _ { 1 : d } ) \big ) - h \big ( x _ { d + 1 } ^ { \prime } - q ( x _ { 1 : d } ^ { \prime } ) \big ) | \mathrm { d } x _ { 1 : d } .
$$

Moreover, for any $z , z ^ { \prime } \in \mathbb { R } ^ { d }$ , there exists a constant $c _ { 1 }$ such that

$$
| \widetilde { f } ( z ) - \widetilde { f } ( z ^ { \prime } ) | \leq c _ { 1 } \frac { 1 } { m ^ { \gamma - 1 } } \| z - z ^ { \prime } \| _ { 2 } .
$$

Therefore, in the case $\begin{array} { r } { \| z - z ^ { \prime } \| _ { 2 } \leq \frac { 1 } { m } } \end{array}$ , then we have $\begin{array} { r } { \| z - z ^ { \prime } \| _ { 2 } \leq \frac { 1 } { m ^ { 1 - \gamma } } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma } } \end{array}$ , and thus $| \widetilde { f } ( z ) - \widetilde { f } ( z ^ { \prime } ) | \leq c _ { 1 } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma }$ ; in the case $\| z - z ^ { \prime } \| _ { 2 } > \frac { 1 } { m }$ , since there exists a constant $c _ { 2 }$ such that $\begin{array} { r } { \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d } } | \widetilde { f } ( z ) | \leq \frac { c _ { 2 } } { m ^ { \gamma } } } \end{array}$ , it holds that $| f ( z ) - f ( z ^ { \prime } ) | \leq 2 c _ { 2 } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma }$ . Putting pieces

together, we have that for any $x , x ^ { \prime } \in \mathbb { R } ^ { D }$ , there exists a constant $c _ { 3 }$ such that

$$
\begin{array} { r l } & { | f ( x ) - f ( x ^ { \prime } ) | \leq m ^ { \gamma - \gamma \beta + \beta } \biggl ( \biggl | \widetilde { f } ( x _ { 1 : d } ) \cdot \Bigl ( h \bigl ( x _ { d + 1 } - q ( x _ { 1 : d } ) \bigr ) - h \bigl ( x _ { d + 1 } ^ { \prime } - q ( x _ { 1 : d } ^ { \prime } ) \bigr ) \Bigr ) \biggr | } \\ & { \qquad + \left| h \bigl ( x _ { d + 1 } ^ { \prime } - q ( x _ { 1 : d } ^ { \prime } ) \bigr ) \cdot ( \widetilde { f } ( x _ { 1 : d } ) - \widetilde { f } ( x _ { 1 : d } ^ { \prime } ) \bigr ) \right| \biggr ) } \\ & { \qquad \leq ( 2 c ) ^ { 1 - \gamma } c _ { 2 } \| x _ { 1 : d + 1 } - x _ { 1 : d + 1 } ^ { \prime } \| ^ { \gamma } + c \left( 2 c _ { 2 } \vee c _ { 1 } \right) m ^ { \gamma - \gamma \beta } \| x _ { 1 : d } - x _ { 1 : d } ^ { \prime } \| ^ { \gamma } } \\ & { \leq c _ { 3 } \| x - x ^ { \prime } \| ^ { \gamma } , } \end{array}
$$

where the last inequality is due to $\beta > 1$ . Consequently, there exists a constant $c _ { 4 }$ such that $\textstyle { \frac { 1 } { c _ { 4 } } } f ( x ) \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ (recall that we only consider $\gamma < 1$ ). Furthermore, since for any $\omega \in \{ 0 , 1 \} ^ { [ m ] ^ { d } }$ , the support of $g _ { \omega } ( z )$ is contained in $B _ { 3 / 4 } ^ { d }$ , we can get

$$
\begin{array} { r l } & { d _ { \tau } ( \mu _ { j } , \mu _ { k } ) \geq \displaystyle \frac { 1 } { c _ { 4 } } \cdot \left( \int f ( x ) \mathrm { d } \mu _ { j } - \int f ( x ) \mathrm { d } \mu _ { k } \right) } \\ & { \quad = \displaystyle \frac { \widetilde { C } } { c _ { 4 } \cdot C } m ^ { \gamma - \gamma \beta _ { 1 } \beta } \Big ( \int \tilde { f } ( x ) \mathrm { d } [ \mu _ { j } | _ { M _ { i } ( \beta ) } ] - \int \tilde { f } ( x ) \mathrm { d } [ \mu _ { k } | _ { M _ { i } ( \tau ) } ] \Big ) } \\ & { \quad = \displaystyle \frac { \widetilde { C } } { c _ { 4 } \cdot C } m ^ { \gamma - \gamma \beta + \beta } \int \tilde { f } ( z ) \cdot \left( g _ { \omega ^ { ( 1 ) } } ( z ) - g _ { \omega ^ { ( 1 ) } } ( z ) \right) \nu _ { 0 } ( z ) \mathrm { d } z } \\ & { \quad = \displaystyle \frac { \widetilde { C } } { c _ { 4 } \cdot C } \int m ^ { - \gamma \beta } \sum _ { \xi \in [ m ] _ { i } ^ { \theta } } \varepsilon _ { \xi } \psi _ { \xi } ( z ) \sum _ { \xi _ { 1 } \in [ m ] _ { i } ^ { \theta } } ( \omega _ { \xi } ^ { ( \beta ) } - \omega _ { \xi _ { 1 } } ^ { ( \beta ) } ) \psi _ { \xi _ { 1 } } ( z ) \nu _ { 0 } ( z ) \mathrm { d } z } \\ & { \quad \geq \displaystyle \frac { \widetilde { C } } { c _ { 4 } \cdot C } m ^ { - \gamma \beta } \operatorname* { i n f } _ { \tilde { x } ^ { ( \beta ) } ( \tilde { x } ) } \sum _ { \xi \in [ m ] _ { i } ^ { \theta } } \int \left. \omega _ { \xi } ^ { ( \beta ) } - \omega _ { \xi } ^ { ( \beta ) } \right. \psi _ { \xi } ^ { \beta } ( z ) \mathrm { d } z \geq c ^ { \prime } n ^ { - \gamma \beta } , } \end{array}
$$

which completes the proof.

# E.6 Proof of Lemma 8

Fix any $\mu \in \mathcal { P } ^ { * }$ , let $\mathcal { M } = \operatorname { s u p p } ( \mu )$ . Then there exist positive constants $\tau , L$ such that

1. $\mathcal { M } \subset \mathbb { B } _ { L } ^ { D }$ ;

2. for any $x _ { 0 } \in \mathcal { M }$ , there exists $\lambda = \lambda ( x _ { 0 } ) \in \Lambda$ such that

(a) $U _ { \lambda } \supset { \mathcal { M } } \cap B _ { \tau } ( x _ { 0 } ) { \mathrm { ~ a n d ~ } } V _ { \lambda } = \phi _ { \lambda } ( U _ { \lambda } ) \supset B _ { \tau } ( \phi _ { \lambda } ( x _ { 0 } ) )$ ;   
(b) $\phi _ { \lambda } ^ { - 1 } \in C _ { L } ^ { \beta } ( V _ { \lambda } )$ and $\mu \circ \phi _ { \lambda } ^ { - 1 } \in C _ { L } ^ { \alpha } ( V _ { \lambda } )$ , where we also use $\mu$ to denote the density of probability measure $\mu$ with respect to the volume measure of $\mathcal { M }$ ;   
(c) $\begin{array} { r } { [ \operatorname* { i n f } _ { z \in V _ { \lambda } } \lambda _ { \operatorname* { m i n } } ( J _ { \phi _ { \lambda } ^ { - 1 } } ( z ) ^ { T } J _ { \phi _ { \lambda } ^ { - 1 } } ( z ) ) ] ^ { - 1 } \leq L . } \end{array}$

We will construct local parametrization $( \mathbb { B } _ { r ^ { \prime } } ( x _ { 0 } ) \cap \mathcal { M } , Q _ { x _ { 0 } } )$ of $\mathcal { M }$ in a neighborhood of $x _ { 0 }$ , where $Q _ { x _ { 0 } } ( x )$ projects $x$ to the tangent space of $\mathcal { M }$ at $x _ { 0 }$ and $Q _ { x _ { 0 } } ^ { - 1 }$ can be $\beta$ -smoothly extended to whole spaces with bounded Hölder norms. More specifically, we have the following lemma.

Lemma 17. There exist positive constants $( \tau _ { 1 } , L _ { 1 } )$ such that for any $x _ { 0 } \in \mathcal { M }$ , define $Q _ { x _ { 0 } } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ as $Q _ { x _ { 0 } } ( x ) = W _ { x _ { 0 } } ^ { T } ( x - x _ { 0 } )$ where $W _ { x _ { 0 } } \in \mathbb { R } ^ { D \times d }$ is an arbitrary orthonormal basis of the tangent space of $\mathcal { M }$ at $x _ { 0 }$ , then there exists a set $\widetilde { U } _ { x _ { 0 } }$ satisfying $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } } \subset$ $\widetilde { U } _ { x _ { 0 } } \subset \mathcal { M }$ and function $G _ { x _ { 0 } } \in C _ { L _ { 1 } } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ so that

1. $G _ { x _ { 0 } } ( \mathbb { B } _ { 1 } ^ { d } ) = \widetilde { U } _ { x _ { 0 } }$ and for any $z \in \mathbb { B } _ { 1 } ^ { d }$ , $Q _ { x _ { 0 } } ( G _ { x _ { 0 } } ( z ) ) = z$ ;   
$\boldsymbol { \mathcal { Z } }$ . $\mu \circ G _ { x _ { 0 } } | _ { \mathbb { B } _ { 1 } ^ { d } } \in C _ { L _ { 1 } } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ and for any $z \in \partial \mathbb { B } _ { 1 } ^ { d }$ , $\| G _ { x _ { 0 } } ( z ) - x _ { 0 } \| \ge \tau _ { 1 }$ .

Then consider any open cover $\mathcal { O } _ { M } = \{ \mathbb { B } _ { r _ { m } } ( a _ { m } ) ^ { \circ } \} _ { m \in [ M ] }$ of $\mathbb { B } _ { L + 1 } ^ { D }$ where $\operatorname* { m i n } \{ r _ { 1 } , r _ { 2 } , \cdot \cdot \cdot , r _ { M } \} \leq$ $\textstyle { \frac { \operatorname { \mathtt { \mathtt { 1 1 } } } } { 4 } }$ . For an arbitrary $m \in \ [ M ]$ such that $\mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } ) \cap \mathcal { M } \neq \emptyset$ , there exists $x _ { 0 } ~ \in$ $\mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } ) \cap \mathcal { M }$ such that $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \supset \mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } )$ . Then by Lemma 17, $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } } \subset \widetilde { U } _ { x _ { 0 } }$ and we can let ${ \widetilde { \cal S } } _ { m }$ be any set containing $\mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } )$ such that $\widetilde { S } _ { m } \cap \mathcal { M } = \widetilde { U } _ { x _ { 0 } }$ . Then we can define $G _ { [ m ] } = G _ { x _ { 0 } }$ . Moreover, by Sobolev extension theorem [Stein, 2016], there exists $\hat { Q } _ { x _ { 0 } } \in C _ { L _ { 1 } } ^ { \beta } ( \mathbb { R } ^ { D } )$ such that $Q _ { x _ { 0 } } | _ { \widetilde { U } _ { x _ { 0 } } } = Q _ { x _ { 0 } } | _ { \widetilde { U } _ { x _ { 0 } } }$ and we can define $Q _ { [ m ] } = Q _ { x _ { 0 } }$ Therefore, by the assumption that the density $\mu$ w.r.t. the volume measure of $\mathcal { M }$ is bounded from above and below, $\mu | _ { \widetilde { S } _ { m } }$ can be written as the push forward measure $[ G _ { [ m ] } ] _ { \# } \nu _ { [ m ] }$ , where

$$
\nu _ { [ m ] } ( z ) = \frac { \mu ( G _ { [ m ] } ( z ) ) \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { [ m ] } } ( z ) ^ { T } \mathbf { J } _ { G _ { [ m ] } } ( z ) ) } } { \int _ { \mathbb { B } _ { 1 } ^ { d } } \mu ( G _ { [ m ] } ( z ) ) \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { [ m ] } } ( z ) ^ { T } \mathbf { J } _ { G _ { [ m ] } } ( z ) ) } \operatorname* { d } z } , \quad z \in \mathbb { B } _ { 1 } ^ { d } .
$$

Then by Lemma 17, $| \log \nu _ { [ m ] } ( z ) |$ is uniformly bounded above over $z \in \mathbb { B } _ { 1 } ^ { d }$ and $\nu _ { [ m ] } \in$ $C _ { L _ { 1 } } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ for a constant $L _ { 1 }$ (recall that $\beta \ge \alpha + 1$ ). Moreover, by the Caffarelli’s global regularity theory [Villani, 2009, Caffarelli, 1996] which states that for $\alpha$ -smooth probability densities $\mu _ { P } , \mu _ { Q }$ supported on $\mathbb { B } _ { 1 } ^ { d }$ and bounded from above and below on their supports, the optimal transport from $\mu _ { P }$ to $\mu _ { Q }$ is $( \alpha + 1 )$ -smooth, we can write $\nu _ { [ m ] }$ as a push forward measure $V _ { [ m ] \# } \nu _ { 0 }$ with $V _ { [ m ] }$ being $\alpha$ -smooth and $\nu _ { 0 }$ being the uniform distribution on $\mathbb { B } _ { 1 } ^ { d }$ . Furthermore, by the third statement of Lemma 17 and Lipschitz-continuity of $G _ { [ m ] }$ , there exists $0 < \epsilon < 1$ so that $G _ { [ m ] } ( \mathbb { B } _ { 1 } ^ { d } \setminus \mathbb { B } _ { 1 - \epsilon } ^ { d } ) \cap \mathbb { B } _ { r _ { m } } ( a _ { m } ) = \emptyset$ . On the other hand, for any $m \in \lfloor M \rfloor$ such that $\mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } ) \cap \mathcal { M } = \emptyset$ , we can choose $\widetilde { S } _ { m } = \mathbb { B } _ { r _ { m } + \frac { \tau _ { 1 } } { 4 } } ( a _ { m } ) \cup \widetilde { S } _ { m ^ { * } }$ , where $m ^ { * }$ can be any $m ^ { * } \in [ M ]$ so that $\mathbb { B } _ { r _ { m ^ { * } } + \frac { \tau _ { 1 } } { 4 } } \big ( a _ { m ^ { * } } \big ) \cap \mathcal { M } \neq \emptyset$ . Proof is completed.

# E.7 Proof of Lemma 17

Fix an $x _ { 0 } \in \mathcal { M }$ , write $z _ { 0 } = \phi _ { \lambda ( x _ { 0 } ) } ( x _ { 0 } )$ , $\psi _ { \lambda ( x _ { 0 } ) } = \phi _ { \lambda ( x _ { 0 } ) } ^ { - 1 }$ and $W _ { x _ { 0 } } \in \mathbb { R } ^ { D \times d }$ be an arbitrary orthonormal basis of the tangent space of $\mathcal { M }$ at $x _ { 0 }$ . For ease of notation, we suppress the subscript $\lambda ( x _ { 0 } )$ and $x _ { 0 }$ in $\phi _ { \lambda ( x _ { 0 } ) } , \psi _ { \lambda ( x _ { 0 } ) } , W _ { x _ { 0 } }$ in the following analysis for a fixed $x _ { 0 } \in \mathcal { M }$ .

Recall $Q _ { x _ { 0 } } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ defined as $Q _ { x _ { 0 } } ( x ) = W ^ { I ^ { \prime } } ( x - x _ { 0 } )$ . Write $Q = Q _ { x _ { 0 } }$ , then given $y = Q ( x )$ for some $x \in \mathcal { M }$ , we may recover $x$ by considering the solution $z$ of the following equation with respect to $z$ :

$$
W ^ { T } ( \psi ( z ) - x _ { 0 } ) = y ,
$$

and $x = \psi ( \bar { z } )$ if a unique solution exists. Now we show that equation (37) has a unique solution in a small neighborhood of $z _ { \mathrm { 0 } }$ when $\| y \|$ is small.

Firstly, by the $\beta$ -smoothness of $\psi$ , there exists a positive constant $L _ { 1 }$ such that for any $\boldsymbol { y } \in \mathbb { B } _ { \tau } ^ { d }$ ,

$$
\| ( W ^ { T } \mathbf { J } _ { \psi } ( z _ { 0 } + y ) ) ^ { - 1 } \| _ { F } \leq L _ { 1 } ,
$$

and for any $y , y ^ { \prime } \in \mathbb { B } _ { \tau } ^ { d }$

$$
\begin{array} { r } { \| W ^ { T } \psi ( z _ { 0 } + y ) - W ^ { T } \psi ( z _ { 0 } + y ^ { \prime } ) - W ^ { T } \mathbf { J } _ { \psi } ( z _ { 0 } + y ^ { \prime } ) ( y - y ^ { \prime } ) \| _ { 2 } \le L _ { 1 } \| y - y ^ { \prime } \| ^ { \beta } , } \end{array}
$$

where recall $\mathbf { J } _ { f } ( x )$ denotes the Jacobian matrix of function $f$ at $x$ . Then for $y \in \mathbb { B } _ { \tau _ { 2 } } ^ { d }$ where $\tau _ { 2 }$ is a small enough positive constant that will be chosen later, we construct a solution $z$ to equation (37) as follows: define $z ^ { 0 } = z _ { 0 }$ and recursively define $z ^ { k } =$ $z ^ { k - 1 } - ( W ^ { T } \mathbf { J } _ { \psi } ( z ^ { k - 1 } ) ) ^ { - 1 } ( W ^ { T } ( \psi ( z ^ { k - 1 } ) - x _ { 0 } ) - y )$ for $k = 1 , 2 , \cdots$ . Then define a sequence $\{ b _ { k } \} _ { k \in \mathbb { N } }$ as $b _ { k } = L _ { 1 } ^ { \frac { 1 + \beta } { 1 - \beta } } ( L _ { 1 } ^ { \frac { 1 + \beta } { \beta - 1 } } \tau _ { 2 } ) ^ { \beta ^ { k } }$ . Then if $\tau _ { 2 }$ satisfies that $\begin{array} { r } { \sum _ { k = 0 } ^ { + \infty } L _ { 1 } b _ { k } \le \frac { \tau } { 2 } \wedge \frac { 1 } { 4 L _ { 1 } ^ { 2 ( \beta - 1 ) } } } \end{array}$ 14L2(β−1) , we can obtain that $\| W ^ { T } ( \psi ( z ^ { k } ) - x _ { 0 } ) - y \| _ { 2 } \leq b _ { k }$ and $\| z ^ { k + 1 } - z ^ { k } \| _ { 2 } \leq L _ { 1 } b _ { k }$ for $k \in \mathbb N$ . Hence $\scriptstyle \operatorname* { l i m } _ { k \to + \infty } z ^ { k } = { \bar { z } }$ exists, $W ^ { T } ( \psi ( \bar { z } ) - x _ { 0 } ) = y$ and $\begin{array} { r } { \| \bar { z } - z _ { 0 } \| _ { 2 } \le \tau ^ { \prime } = \frac { \tau } { 2 } \wedge \frac { 1 } { 4 L _ { 1 } ^ { 2 ( \beta - 1 ) } } } \end{array}$

Now we show that for any $y \in \mathbb { B } _ { \tau _ { 2 } } ^ { d }$ , the equation $W ^ { T } ( \psi ( z ) - x _ { 0 } ) = y$ has a unique solution on $\mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } )$ . Suppose there are two solutions $\bar { z } , \bar { z } ^ { \prime }$ on $\mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } )$ . Then $\| \bar { z } - \bar { z } ^ { \prime } \| _ { 2 } \leq$ ≤ 12L2(β−1) and W T (ψ(¯z) − ψ(¯z0)) = 0. Then by equation (39), we can obtain that

$$
\| \boldsymbol { W } ^ { T } \mathbf { J } _ { \boldsymbol { \psi } } ( \bar { z } ^ { \prime } ) ( \bar { z } - \bar { z } ^ { \prime } ) \| _ { 2 } \leq L _ { 1 } \| \bar { z } - \bar { z } ^ { \prime } \| ^ { \beta } ,
$$

which leads to

$$
\frac { \| \bar { z } - \bar { z } ^ { \prime } \| _ { 2 } } { \| ( W ^ { T } \mathbf { J } _ { \psi } ( \bar { z } ^ { \prime } ) ) ^ { - 1 } \| _ { 2 } } \le L _ { 1 } \| \bar { z } - \bar { z } ^ { \prime } \| ^ { \beta } .
$$

Then combined with equation (38), we can obtain that

$$
\| \bar { z } - \bar { z } ^ { \prime } \| _ { 2 } \geq \frac { 1 } { L _ { 1 } ^ { 2 ( \beta - 1 ) } } ,
$$

which cause contradiction. So we can define a function $q : \mathbb { B } _ { \tau _ { 2 } } ^ { d } \to \mathbb { R } ^ { d }$ so that $q ( y )$ is defined as the unique solution of $W ^ { T } ( \psi ( z ) - x _ { 0 } ) = y$ over $z \in \mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } )$ . Consider $\tilde { V } = \mathbb { B } _ { \tau _ { 2 } } ^ { d }$ and $\widetilde { U } = \psi ( q ( \widetilde { V } ) ) = \{ \psi ( z ) : z \in \mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } )$ , $\| W ^ { T } ( \psi ( z ) - x _ { 0 } ) \| _ { 2 } \leq \tau _ { 2 } \}$ . Next we show that there exists a positive constant $\tau _ { 1 }$ such that $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } } \subset { \mathcal { \widetilde { U } } }$ . First we know that $\mathbb { B } _ { \tau } ( x _ { 0 } ) \cap \mathcal { M } \subset U = U _ { \lambda ( x _ { 0 } ) }$ . Then consider $\tau _ { 1 } \leq \tau$ and any $x \in \mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } }$ , we have $\| x - \psi ( z _ { 0 } ) \| = \| x - x _ { 0 } \| \leq \tau _ { 1 }$ . Define $\widetilde { z } ^ { 0 } = z _ { 0 }$ and recursively define $\widetilde { z } ^ { k } =$ $\widetilde { z } ^ { k - 1 } - \mathbf { J } _ { \psi } ( \widetilde { z } ^ { k - 1 } ) ( \psi ( \widetilde { z } ^ { k - 1 } ) - x )$ for $k \in \mathbb { N } ^ { + }$ , then similar to the above analysis for the function $q ( y )$ , when $\tau _ { 1 }$ is small enough, we can obtain that $\begin{array} { r } { \phi ( x ) = \operatorname* { l i m } _ { k  + \infty } \widetilde { z } ^ { k } } \end{array}$ and $\begin{array} { r } { \| \phi ( x ) - z _ { 0 } \| \leq \tau ^ { \prime } \wedge \frac { \tau _ { 2 } } { \operatorname* { s u p } _ { z \in \mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } ) } \| W ^ { T } \mathbf { J } _ { \psi } ( z ) \| _ { F } } } \end{array}$ . Thus, $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } } \subset { \widetilde { U } }$ for a small enough positive constant $\tau _ { 1 }$ .

Then define $G : \mathbb { B } _ { 1 } ^ { d } \to \widetilde { U }$ as $G ( z ) ~ = ~ \psi ( q ( \tau _ { 2 } z ) )$ and $G ^ { - 1 } \ = \ Q \ : \ { \widetilde { U } } \ \to \ { \mathbb { B } } _ { 1 } ^ { d }$ as $\begin{array} { r } { Q ( x ) = \frac { 1 } { \tau _ { 2 } } W ^ { T } ( x - x _ { 0 } ) } \end{array}$ . Since $\mathbf { J } _ { q } ( z ) = ( W ^ { T } \mathbf { J } _ { \psi } ( q ( z ) ) ) ^ { - 1 }$ , we can obtain that $\mathbf { J } _ { G } ( z ) =$ $\tau _ { 2 } \mathbf { J } _ { \psi } ( q ( \tau _ { 2 } z ) ) ( W ^ { T } \mathbf { J } _ { \psi } ( q ( \tau _ { 2 } z ) ) ) ^ { - 1 }$ . Then by $\psi \in C _ { L } ^ { \beta } ( V )$ and $[ \mathrm { i n f } _ { z \in V } \lambda _ { \mathrm { m i n } } ( \mathbf { J } _ { \psi } ( z ) ^ { I } \mathbf { J } _ { \psi } ( z ) ) ] ^ { - 1 } \leq$ $L$ , we can obtain that $G \in C _ { L ^ { * } } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } )$ and $q \in C _ { L ^ { * } } ^ { \beta } ( \mathbb { B } _ { \tau _ { 2 } } ^ { d } )$ for a constant $L ^ { * }$ , then by Sobolev extension theorem [Stein, 2016], there exists $\bar { G } \in C _ { L ^ { * } } ^ { \beta } ( \mathbb { R } ^ { d } )$ such that $G | _ { \mathbb { B } _ { 1 } ^ { d } } = G$ . Moreover, by the assumption that $\mu \circ \psi \in C _ { L } ^ { \alpha } ( V )$ , we can obtain $\mu \circ G \in C _ { L ^ { * } } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ . Finally, since $G ( \partial \mathbb { B } _ { 1 } ^ { d } ) = \{ \psi ( z ) : z \in \mathbb { B } _ { \tau ^ { \prime } } ( z _ { 0 } )$ , $\| W ^ { T } ( \psi ( z ) - x _ { 0 } ) \| _ { 2 } = \tau _ { 2 } \}$ . We can obtain that for any $x \in G ( \partial \mathbb { B } _ { 1 } ^ { d } )$ , $\lVert x - x _ { 0 } \rVert \geq \tau _ { 2 }$ . Proof is completed.

# E.8 Proof of Lemma 10

Let $\begin{array} { r } { \delta = b _ { 1 } \left( \frac { \log { \widetilde { n } } } { \widetilde { n } } \right) ^ { \frac { 1 } { d + L _ { 0 } } } } \end{array}$ , where $b _ { 1 } \geq 1$ is a sufficiently large positive constant to be specified later. Let $\mathcal { A } _ { z } = \left\{ z \in \mathbb { B } _ { 1 } ^ { d } : \| z \| _ { 2 } \leq 1 - \delta \right.$ , $G _ { [ m ] } ^ { * } ( z ) \in \mathbb { B } _ { r _ { m } + 0 . 2 5 / L } \bigl ( a _ { m } \bigr ) \}$ be a proper subset of $\mathbb { B } _ { 1 } ^ { d }$ . Let $\begin{array} { r } { h _ { \widetilde { n } } ~ = ~ ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { 1 } { d } } } \end{array}$ and $\mathcal { N } _ { h _ { \tilde { n } } } ~ \subset ~ \mathcal { A } _ { z }$ be a minimal $h _ { \widetilde { n } }$ -covering set of $\mathcal { A } _ { z }$ under the $\ell _ { 2 }$ e distance, where its cardinality satisfies $| \mathcal { N } _ { h _ { \widetilde { n } } } | \leq C \frac { \bar { n } } { \log \widetilde { n } }$ . For any $\tilde { z } \in \mathcal N _ { h _ { \widetilde { n } } }$ , define $\begin{array} { r } { \delta _ { \widetilde { z } } = b _ { 2 } \big ( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| \widetilde { z } \| _ { 2 } ) ^ { L _ { 0 } } } \big ) ^ { \frac { 1 } { d } } } \end{array}$ with $\begin{array} { r } { b _ { 2 } = \frac { 1 } { 2 } b _ { 1 } ^ { \frac { L _ { 0 } } { d } + 1 } } \end{array}$

We claim that it suffices to show that for sufficiently large $b _ { 1 }$ , it holds with probability at least $1 - n ^ { - c }$ that for any $\mathcal { \tilde { z } } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ ,

$$
\sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { j | \tilde { \rho } | \leq | \beta | } } \frac { 1 } { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \leq C \left( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| \widetilde { z } \| _ { 2 } ) ^ { L _ { 0 } } } \right) ^ { \frac { \beta } { d } } .
$$

In fact, if this inequality holds, then we can apply a standard argument of approximation by the $h _ { \widetilde { n } }$ -covering set. Concretely, for any $z \in \mathcal A _ { z }$ , there exists $\tilde { z } \in \mathcal N _ { h _ { \widetilde { n } } }$ such that $\begin{array} { r } { \| z - \widetilde { z } \| _ { 2 } \le h _ { \widetilde { n } } = \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { 1 } { d } } } \end{array}$ , we can obtain by applying Taylor expansion to $G _ { [ m ] } ^ { * } ( z ) - { \widehat { f } } _ { [ m ] } ( z )$ that

$$
\begin{array} { r l }   { \| G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } \leq C \sum _ { \overset { 1 } { j \} \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { | j | } { d } } + C ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta } { d } } } \quad } & { } \\ { \leq C ( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| \widetilde { z } \| _ { 2 } ) ^ { L _ { 0 } } } ) ^ { \frac { \beta } { d } } \leq C _ { 1 } ( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| z \| _ { 2 } ) ^ { L _ { 0 } } } ) ^ { \frac { \beta } { d } } , } \end{array}
$$

where the last step follows by choosing $b _ { 1 }$ large enough such that $| \| z \| _ { 2 } - \| \widetilde { z } \| _ { 2 } | \leq \| z - \widetilde { z } \| _ { 2 } \leq$ $\begin{array} { r } { h _ { \widetilde { n } } \le \frac { 1 } { 2 } \delta \le \frac { 1 } { 2 } ( 1 - \| z \| _ { 2 } ) } \end{array}$ , which implies $1 - \| { \widetilde { z } } \| _ { 2 } \geq { \frac { 1 } { 2 } } ( 1 - \| z \| _ { 2 } )$ . Moreover, for any

$z \in \mathcal { A } _ { z } ^ { \prime } = \{ z \in \mathbb { B } _ { 1 } ^ { d } : 1 - \delta \leq \| z \| _ { 2 } \leq 1$ , $G _ { [ m ] } ^ { * } ( z ) \in S _ { m } \}$ , there exists $\tilde { z } \in \mathcal N _ { h _ { \widetilde { n } } }$ such that $\begin{array} { r } { \| z - \widetilde { z } \| _ { 2 } \le C ( \frac { \log { \widetilde { n } } } { \widetilde { n } } ) ^ { \frac { 1 } { d + L _ { 0 } } } } \end{array}$ . Thus for any $z \in \mathcal { A } _ { z } ^ { \prime }$ , there exists $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ such that

$$
\begin{array} { r l } & { G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } \le C \displaystyle \sum _ { j \notin \mathbb { N } _ { 2 } ^ { 6 } } \frac 1 { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } \left( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { | j | } { 4 + L _ { 0 } } } + \left( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { \beta } { d + L _ { 0 } } } } \\ & { \le C \displaystyle \sum _ { j \notin \mathbb { N } _ { 2 } ^ { 6 } } \frac 1 { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } \operatorname* { i n f } _ { \widetilde { z } \in \mathcal { N } _ { h _ { \widetilde { n } } } } ( \delta _ { z } ) ^ { | j | } + \left( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { \beta } { d + L _ { 0 } } } \le C \left( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { \beta } { d + L _ { 0 } } } . } \end{array}
$$

Now let us prove inequality (40). Since $S _ { m } ^ { \dagger } = \mathbb { B } _ { r _ { m } + 0 . 5 / L } ( a _ { m } ) \subset \widetilde { S } _ { m }$ , we have that $( G _ { [ m ] } ^ { * } , Q _ { [ m ] } ^ { * } )$ is a feasible solution to the optimization problem (11) in step one of submanifold estimation and $G _ { [ m ] } ^ { * } \bigl ( Q _ { [ m ] } ^ { * } ( X _ { i } ) \bigr ) \ = \ X _ { i }$ for all $X _ { i } ~ \in ~ S _ { m } ^ { \dagger }$ . Therefore, we obtain by the optimality of the estimator $( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } )$ that

$$
\frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| X _ { i } - \widehat { G } _ { [ m ] } ( \widehat { Q } _ { [ m ] } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \mathbf { 1 } _ { S _ { m } ^ { \dagger } } ( X _ { i } ) = 0 .
$$

In particular, by restricting the sum to those $X _ { i }$ in $\mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } )$ for a fixed $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ , we further obtain (recall that ${ \widehat { f } } _ { [ m ] } = { \widehat { G } } _ { [ m ] } \circ { \widehat { Q } } _ { [ m ] } \circ G ^ { * } )$ )

$$
\frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| { \cal G } _ { [ m ] } ^ { * } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) - \widehat { f } _ { [ m ] } \left( Q _ { [ m ] } ^ { * } ( X _ { i } ) \right) \| _ { 2 } ^ { 2 } \cdot { \bf 1 } _ { \mathcal B _ { \tilde { L } } ( \tilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot { \bf 1 } _ { S _ { m } ^ { \dagger } } ( X _ { i } ) = 0 .
$$

To proceed, we utilize the property that $\mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { S _ { m } ^ { \dagger } } ( X _ { i } ) = \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \ .$ $\mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } )$ where recall $S _ { m } ^ { \dagger } \subset \mathbb { B } _ { r _ { m } + 1 / L } ( a _ { m } ) \subset \widetilde { S } _ { m }$ . To see this, we only need to show that $Q _ { [ m ] } ^ { \ast } ( X _ { i } ) \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } )$ plus $X _ { i } \in \widetilde { S } _ { m }$ imply $X _ { i } \in S _ { m } ^ { \dagger }$ . In fact, by the Lipschitzness of $G _ { [ m ] } ^ { * }$ , we have $\lVert X _ { i } - G ^ { * } ( \widetilde { z } ) \rVert _ { 2 } \leq L \sqrt { D } \delta _ { \widetilde { z } }$ , which combined with $G ^ { * } ( \widetilde { z } ) \in \mathbb { B } _ { r _ { m } + 0 . 2 5 / L } \bigl ( a _ { m } \bigr )$ implies $X _ { i } \in \mathbb { B } _ { r _ { m } + 0 . 5 / L } ( a _ { m } ) = S _ { m } ^ { \dagger }$ when $n \geq ( 4 L ^ { 2 } b _ { 1 } { \sqrt { D } } ) ^ { 4 ( d + L _ { 0 } ) }$ . Based on this replacement of indicator functions, we further obtain

$$
\frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| G _ { [ m ] } ^ { * } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) - \widehat { f } _ { [ m ] } ( Q ^ { * } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } ) = 0 .
$$

By applying the Taylor expansion to $G _ { [ m ] } ^ { * } ( z ) - { \widehat { f } } _ { [ m ] } ( z )$ around $\widetilde { z }$ in the preceding display and using the fact that $G _ { [ m ] } ^ { \ast } - \widehat { f } _ { [ m ] } \in C _ { C _ { 0 } } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; \mathbb { R } ^ { D } )$ with some sufficiently large constant

$C _ { 0 }$ , we can get the following localized basic inequality after some algebra calculation

$$
\begin{array} { l } { { \displaystyle U _ { n } ( \widetilde { z } , \widehat { f } _ { [ m ] } ) : = } } \\ { { \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \Big \| \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } \atop j \in \mathbb { S } _ { \varepsilon } ^ { d } } \frac { 1 } { j ! } \left( G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) \right) ( Q _ { [ m ] } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } ) } } \\ { { \leq } c \Bigg ( ( \delta _ { \widetilde { z } } ) ^ { 2 \beta } + ( \delta _ { \widetilde { z } } ) ^ { \beta } \sum _ { \small j \in \mathbb { N } _ { m } ^ { d } \atop j \in \mathbb { S } _ { \varepsilon } ^ { d } } \frac { 1 } { j ! } \left\| G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) \right\| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \Bigg ) \cdot \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } } }  \end{array}
$$

The second factor on the right hand side of (41) can be bounded by applying a simple union bound argument and Bernstein’s inequality for binomials as follows. First, we can bound the probability

$$
\begin{array} { r l } & { \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } , Q _ { [ m ] } ^ { * } ( X ) \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) \big ) = \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } \big ) \cdot \mathbb { P } _ { \mu ^ { * } } \big ( Q _ { [ m ] } ^ { * } ( X ) \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) \big | X \in \widetilde { S } _ { m } \big ) } \\ & { \overset { ( i ) } { = } \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } \big ) \int _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } \nu _ { [ m ] } ^ { * } ( z ) \mathrm { d } z \leq C \left( 1 - \| \widetilde { z } \| _ { 2 } \right) ^ { L _ { 0 } } \delta _ { \widetilde { z } } ^ { d } \cdot \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } \big ) } \\ & { \leq C _ { 1 } b _ { 2 } ^ { d } \frac { \log \widetilde { n } } { \widetilde { n } } \cdot \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } \big ) \leq C _ { 1 } b _ { 2 } ^ { d } \frac { \log n } { n } , } \end{array}
$$

where step (i) follows by the fact that $Q _ { [ m ] } ^ { * } ( X )$ given $X \in \widetilde { S } _ { m }$ is distributed as $\nu _ { [ m ] } ^ { * }$ , and the last step follows since $\widetilde { n } = n \cdot \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { S } _ { m } )$ . Since the random variable ${ \bf 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q ^ { * } ( X ) ) \mathrm { . }$ $\mathbf { 1 } _ { \widetilde { S } _ { m } } ( X )$ is uniformly bounded by $1$ , and inequality (42) implies its variance to be bounded by $C _ { 1 } b _ { 2 } ^ { d } \frac { \log n } { n }$ , we may apply the Bernstein inequality and a simple union bound argument over all $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ (with $\begin{array} { r } { | \mathcal { N } _ { h _ { \widetilde { n } } } | \leq C \frac { \widetilde { n } } { \log { \widetilde { n } } } ) } \end{array}$ to obtain that with probability at least $1 - n ^ { - c }$ ,

$$
\operatorname* { s u p } _ { \varepsilon N _ { h } } \bigg | \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { s } _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } ) - \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { S } _ { m } , Q _ { [ m ] } ^ { * } ( X ) \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) \big ) \bigg | \leq C _ { 2 } b _ { 2 } ^ { \frac { d } { 2 } } . \frac { \log ^ { 2 } } { \varepsilon N _ { h } } ,
$$

which together with (42) leads to

$$
\operatorname* { s u p } _ { \tilde { z } \in N _ { h _ { \tilde { n } } } } \biggl [ \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \tilde { z } } } ( \tilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } ) \biggr ] \leq C b _ { 2 } ^ { d } \cdot \frac { \log n } { n } .
$$

To analyze the quantity $U _ { n } ( \widetilde { z } , \widehat { f } _ { [ m ] } )$ on the left hand side of the localized basic inequality (41), we will resort to the following lemma. A proof of the lemma is provided in Section E.9, which is quite technical and involved, based on applying the chaining and peeling techniques in empirical process theory to analyze the supreme of the empirical process $U _ { n } ( \widetilde { z } , f )$ indexed by $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ and a $\beta$ -smooth function $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ .

Lemma 18. With probability at least $1 - n ^ { - c }$ , the following inequality holds for any $\beta$ -smooth function $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ and $\mathcal { \widetilde { z } } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ ,

$$
\left( \widetilde { z } , f \right) - \mathbb { E } _ { \mu ^ { * } } [ U _ { n } ( \widetilde { z } , f ) ] \big | \le C b _ { 2 } ^ { \frac { d } { 2 } } \cdot \frac { \log n } { n } \cdot \bigg \{ \bar { \delta } ^ { 2 } + \Big [ \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | \eta | \le | \delta | } } \frac { 1 } { j ! } \| f ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \Big ] ^ { 2 }
$$

where $\begin{array} { r } { \bar { \delta } = \left( \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { \beta } { d } } } \end{array}$ and the expectation is taken with respect to the randomness in $\{ X _ { i } \} _ { i \in I _ { 1 } }$ . Before applying this lemma, notice that for any $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ , we can bound the expectation $\mathbb { E } _ { \mu ^ { * } } [ U _ { n } ( \widetilde { z } , \widehat { f } _ { [ m ] } ) ]$ , where $f$ has been plugged-in with $\widehat { f } _ { [ m ] }$ , by

$$
\begin{array} { r l } & { \mathbb { E } _ { t ^ { * } } \{ U _ { 2 } ( \tilde { z } ) \} = \frac { 1 } { \beta } \int _ { 0 } ^ { t } \int _ { \mathbb { R } ^ { 2 } } \left\{ \left( G _ { m } ^ { * } \right) ^ { 2 } ( \tilde { z } ) - \widehat { f } _ { | m | } ^ { \beta } ( \tilde { z } ) \right\} ( Q _ { m | } ^ { * } ( X ) - \tilde { z } ) ^ { \beta } \Big \| _ { \mathbb { R } ^ { 2 } } ^ { 2 } \cdot \mathbf { 1 } _ { \mathfrak { R } _ { \widehat { z } } ( \tilde { z } ) } ( Q _ { m | } ^ { * } ( X ) ) \cdot \mathbf { 1 } _ { \widehat { S } _ { m } ( X ) } } \\ & { = \mathbb { E } _ { t ^ { * } } \cdot \frac { 1 } { \beta \left( \mathbb { R } ^ { 2 } \right) ^ { 3 } } \frac { 1 } { \beta } \left( \mathbb { E } _ { m } ^ { * } \right) ^ { 2 } \cdot \mathbb { P } ( X \in \widehat { S } _ { m } ) \int _ { \mathbb { R } ^ { 2 } \left( \mathbb { R } ^ { 2 } \right) } \Big \| \sum _ { \widehat { \xi } \in \mathbb { R } _ { \widehat { z } } ^ { 2 } } \frac { 1 } { \beta } \Big ( G _ { m } ^ { * } \big ) ( \tilde { z } ) - \widehat { f } _ { | m | } ^ { \beta } ( \tilde { z } ) \Big ( \tilde { z } ) \Big \} ( \tilde { z } ) \cdot \mathbf { 1 } _ { \widehat { S } _ { m } } ( X ) } \\ &  \overset { ( a ) } { \le } \frac { 1 } { \beta \mathbb { E } _ { \widehat { z } } ^ { 2 } ( \tilde { z } ) } \frac { 1 } { \beta } \Big ( \gamma _ { m } ^ { * } \big ) ( z ) \cdot \mathbb { P } ( X \in \widehat { S } _ { m } ) \int _ { \mathbb { R } ^ { 2 } \left( \mathbb { R } ^ { 2 } \right) } \Big \| \displaystyle \sum _ { \widehat { \xi } \in \mathbb { R } _ { \widehat { z } } ^ { 2 } } \frac  \end{array}
$$

where step (i) uses the fact that $Q _ { [ m ] } ^ { * } ( X )$ given $X \in \widetilde { S } _ { m }$ is distributed as $\nu _ { [ m ] } ^ { * }$ , step (ii) follows by applying the change of variable of $\frac { z - \widetilde { z } } { \delta _ { \widetilde { z } } }  z$ , and the last step uses $\widetilde { n } =$ $n \mathbb { P } ( X \in \widetilde { S } _ { m } )$ and the property that $\nu _ { [ m ] } ^ { \ast } ( z ) \geq c ( 1 - \| \widetilde { z } \| _ { 2 } ) ^ { L _ { 0 } }$ for all $z \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } )$ as long as $b _ { 1 }$ in the definition of $\delta$ is sufficiently large. Now using the fact that for any $d$ -variate polynomial $\begin{array} { r } { S ( y ) = \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } y ^ { j } } \end{array}$ , $\boldsymbol { y } \in \mathbb { R } ^ { d }$ , there exists some positive constant $C ( d , k )$ only depending on $( d , k )$ such that

$$
\int _ { \mathbb { B } _ { 1 } ^ { d } } \mathcal { S } ^ { 2 } ( y ) \mathrm { d } y \geq C ( d , k ) \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } ^ { 2 } ,
$$

we can obtain that

$$
\Big \| \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \delta _ { \tilde { z } } ^ { j } \left( G _ { [ m ] } ^ { * , ( j ) } ( \tilde { z } ) - \widehat { f } _ { [ m ] } ^ { ( j ) } ( \tilde { z } ) \right) z ^ { j } \Big \| _ { 2 } ^ { 2 } \mathrm { d } z \geq c \Bigg ( \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop | j | \leq | \beta | } \frac { 1 } { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \tilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } \left( \delta _ { \tilde { z } } \right) ^ { | j | } \Bigg ) ^ { 2 }
$$

Finally, by combining equations (41), (42), (45), (46) and Lemma 18, we obtain that with

probability at least $1 - n ^ { - c }$ , for any $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ ,

$$
\begin{array} { r l } & { \displaystyle b _ { 2 } ^ { d } \cdot \frac { \log n } { n } \cdot \bigg ( \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) | ^ { j ] } \bigg ) ^ { 2 } } \\ & { \displaystyle \le C b _ { 2 } ^ { d } \cdot \frac { \log n } { n } \cdot \bigg ( \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \bigg ) ^ { 2 } + C b _ { 2 } ^ { \frac { d } { 2 } } \cdot \bigg ( \frac { \log \widetilde { n } } { \widetilde { n } } \bigg ) ^ { \frac { 2 \delta } { d } } \cdot \frac { \log n } { n } } \\ & { \quad \quad \quad + C b _ { 2 } ^ { d } \cdot \frac { \log n } { n } \cdot \bigg ( ( \delta _ { \widetilde { z } } ) ^ { 2 \beta } + ( \delta _ { \widetilde { z } } ) ^ { \beta } \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { [ m ] } ^ { ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \bigg ) . } \end{array}
$$

Consequently, the claimed inequality (40) follows from the above by choosing a sufficiently large $b _ { 1 }$ (recall that $\begin{array} { r } { b _ { 2 } = \frac 1 2 b _ { 1 } ^ { \frac { L _ { 0 } } { d } + 1 } } \end{array}$ ) and the definition that $\begin{array} { r } { \delta _ { \widetilde { z } } = b _ { 2 } \big ( \frac { \log \widetilde { n } } { \widetilde { n } ( 1 - \| \widetilde { z } \| _ { 2 } ) ^ { L _ { 0 } } } \big ) ^ { \frac { 1 } { d } } } \end{array}$ .

# E.9 Proof of Lemma 18

Since $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ , for any $z ~ \in ~ \mathbb { B } _ { 1 } ^ { d }$ and $j ~ \in ~ \mathbb { N } _ { 0 } ^ { d }$ with $| j | \le \lfloor \beta \rfloor$ , it holds that $\| f ^ { ( j ) } ( z ) \| _ { 2 } \leq \sqrt { D } L = C _ { 0 }$ . For any fixed $ { \widetilde { z } } \in  { \mathcal N } _ { h _ { \widetilde { n } } }$ and $\widetilde { \delta } > 0$ , let

$$
\zeta = \left\{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , \ | j | \leq | \beta | } \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \binom { d + | \beta | - 1 } { d } } : \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \left\| T _ { j } - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \right\| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \leq \delta _ { \beta | } \right\} ,
$$

We also define the following supreme of an empirical process indexed by $T \in { \bar { \mathcal { T } } } ( { \widetilde { \delta } } )$ ,

$$
\begin{array} { r l r } {  { Z _ { n } ( \widetilde { \delta } ) = } } \\ & { } &  \underset { Y \in \widetilde { T } ( \widetilde { \delta } ) } { \operatorname* { s u p } } \bigg | \mathbb { E } _ { \mu ^ { * } } \bigg [ \Big \| \begin{array} { l } { \sum _ { j \in \mathbb { N } _ { 2 } ^ { d } } \frac { 1 } { j ! } ( G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } ) ( Q _ { [ m ] } ^ { * } ( X ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { s } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X ) } \bigg ] } \\ & { } & { - \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \bigg [ \Big \| \begin{array} { l l } { \sum _ { j } } & { 1 } \\ { \sum _ { j \in \mathbb { N } _ { 2 } ^ { d } } \frac { 1 } { j ! } ( G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } ) ( Q _ { [ m ] } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { s } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X ) } \end{array} } } \end{array} \end{array}
$$

and $R _ { n } ( { \widetilde \delta } ) = \mathbb { E } _ { \mu ^ { * } } \left[ Z _ { n } ( { \widetilde \delta } ) \right]$ . We will first prove a concentration inequality for a fixed radius $\widetilde { \delta } > 0$ , and then using the peeling technique to allow the radius to be random, which leads to the desired result.

To apply the Talagrand concentration inequality (see, for example, Theorem 3.27 of Wainwright [2019]) for bounding the difference $| Z _ { n } ( \widetilde { \delta } ) - R _ { n } ( \widetilde { \delta } ) |$ for a fixed $\widetilde { \delta } > 0$ , we notice that each additive component in the second empirical sum above has second moment

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \bigg [ \underset { x \in \tilde { \mathcal { T } } ( \tilde { \tilde { \theta } } ) } { \operatorname* { s u p } } \Big ( \Big \lVert \underset { y \in \mathbb { R } ^ { d } } { \sum } \frac { 1 } { j ! } \big ( G _ { \{ m \} } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \big ) ( Q _ { \{ m \} } ^ { * } ( X ) - \tilde { z } ) ^ { j } \big \rVert _ { 2 } ^ { 4 } \cdot \mathbb { 1 } _ { \mathbb { R } _ { \tilde { \theta } _ { \tilde { z } } ( \tilde { z } ) } ( Q _ { \{ m \} } ^ { * } ) ( X ) \cdot \mathbb { 1 } _ { \tilde { \tilde { S } } _ { m } ( \tilde { x } ) } } } \\ & { \leq \underset { x \in \tilde { \mathcal { Z } } ( \tilde { \tilde { \pi } } ) } { \operatorname* { s u p } } \Big ( \Big \lVert \underset { y \in \mathbb { R } _ { \tilde { z } } } { \sum } \frac { 1 } { j ! } \big ( G _ { \{ m \} } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \big ) ( z - \tilde { z } ) ^ { j } \Big \rVert _ { 2 } ^ { 4 } \cdot \mathbb { P } _ { \mu ^ { * } } \big ( X \in \tilde { S } _ { m } , Q _ { \{ m \} } ^ { * } ( X ) \in \mathbb { B } _ { \tilde { \theta } _ { z } ( \tilde { z } ) } \big ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \leq C \underset { \tau \in \tilde { \mathcal { T } } ( \tilde { \tilde { \theta } } ) } { \operatorname* { s u p } } \bigg ( \underset { y \in \mathbb { R } ^ { d } } { \sum } \frac { 1 } { j ! } \lVert T _ { j } - G _ { \{ m \} } ^ { * , ( j ) } ( \tilde { z } ) \rVert _ { 2 } ( \tilde  \end{array}
$$

where we have used inequality (42) to bound $\mathbb { P } _ { \mu ^ { * } } \mathopen { } \mathclose \bgroup ( X \in  { \mathcal { S } } _ { m }$ , $Q _ { [ m ] } ^ { \ast } ( X ) \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) \bigr )$ . Moreover, each additive component can be almost surely bounded by

$$
\begin{array} { r l } & { \quad \underset { z \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } { \operatorname* { s u p } } \Big \Vert \underset { j \in \mathbb { B } _ { 0 } ^ { d } } { \sum } \frac { 1 } { j ! } \left( G _ { [ m ] } ^ { \ast , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { [ m ] } ^ { \ast } ( X ) - \widetilde { z } ) ^ { j } \Big \Vert _ { 2 } ^ { 2 } } \\ & { \le C \left( \underset { j \in \mathbb { B } _ { 0 } ^ { d } } { \sum } \frac { 1 } { j ! } \Vert T _ { j } - G ^ { \ast , ( j ) } ( \widetilde { z } ) \Vert _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \right) ^ { 2 } \le C \widetilde { \delta } ^ { 2 } . } \end{array}
$$

Based on these two bounds, we can apply the Talagrand concentration inequality to obtain that for any $s \geq 0$ ,

$$
\mathbb { P } \big ( Z _ { n } ( { \widetilde { \delta } } ) \geq R _ { n } ( { \widetilde { \delta } } ) + s ^ { 2 } \big ) \leq 2 \exp \left( - \frac { c n s ^ { 4 } } { s ^ { 2 } { \widetilde { \delta } } ^ { 2 } + b _ { 2 } ^ { d } { \widetilde { \delta } } ^ { 4 } \cdot \frac { \log n } { n } } \right) .
$$

It remains to bound the expectation $R _ { n } ( { \widetilde { \delta } } )$ via the symmetrization technique and chaining. By a standard symmetrization, we can get

$$
\begin{array} { r l r } {  { \hat { \boldsymbol { \mathrm {  ~ \xi ~ } } } _ { n } ( \widetilde { \boldsymbol { \delta } } ) \leq \frac { 2 } { \sqrt { | \boldsymbol { I } | _ { 1 } } } \mathbb { E } \bigg [ \operatorname* { s u p } _ { T \in \widetilde { T } ( \widetilde { \boldsymbol { \delta } } ) } } } \\ & { } & { \bigg | \frac { 1 } { \sqrt { | \boldsymbol { I } | _ { 1 } } } \sum _ { i \in I _ { 1 } } \varepsilon _ { i } \bigg [ \Big \| \sum _ { \boldsymbol { j } \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } ( { \boldsymbol { G } } _ { [ m ] } ^ { * , ( j ) } ( \widetilde { \boldsymbol { z } } ) - { \boldsymbol { T } } _ { j } ) ( { \boldsymbol { Q } } _ { [ m ] } ^ { * } ( { \boldsymbol { X } } ) - \widetilde { \boldsymbol { z } } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { \boldsymbol { z } } ) } ( { \boldsymbol { Q } } _ { [ m ] } ^ { * } ( { \boldsymbol { X } } _ { i } ) ) \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } } \end{array}
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from the Rademacher distribution, i.e. $\mathbb { P } ( \varepsilon _ { i } = 1 ) =$ $\mathbb { P } ( \varepsilon _ { i } = - 1 ) = 0 . 5$ . Since given $\{ X _ { i } \} _ { i \in I _ { 1 } }$ , the stochastic process inside the supreme is a

sub-Gaussian process with intrinsic metric

$$
\begin{array} { r l } & { d _ { n } ^ { 2 } ( T , \widetilde { T } ) } \\ & { = \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \subset I _ { 1 } } \bigg ( \Big \| \displaystyle \sum _ { j \in \mathbb { S } ^ { d } } \frac { 1 } { j ! } \big ( G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \big ) \big ( Q _ { [ m ] } ^ { * } ( X _ { i } ) - \widetilde { z } \big ) ^ { j } \Big \| _ { 2 } ^ { 2 } } \\ & { \qquad - \displaystyle \Big \| \displaystyle \sum _ { j \in \mathbb { N } _ { i } ^ { d } } \frac { 1 } { j ! } \big ( G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) - \widetilde { T } _ { j } \big ) \big ( Q _ { [ m ] } ^ { * } ( X _ { i } ) - \widetilde { z } \big ) ^ { j } \Big \| _ { 2 } ^ { 2 } \bigg ) ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) \big ) \cdot \mathbf { 1 } } \\ & { \leq C \widetilde { \delta } ^ { 4 } \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \subset I _ { 1 } } \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X _ { i } ) ) ) \cdot \mathbf { 1 } _ { \widetilde { z } _ { m } } ( X _ { i } ) , } \end{array}
$$

for any $T , \widetilde { T } \in \bar { \mathcal { T } } ( \widetilde { \delta } )$ , where the last step uses the definition of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ . The above combined with inequality (42) implies

$$
\mu ^ { * } \Big [ \operatorname* { s u p } _ { T , \widetilde { T } \in \widetilde { T } ( \delta ) } d _ { n } ^ { 2 } ( T , \widetilde { T } ) \Big ] \leq C b _ { 2 } ^ { d } \widetilde { \delta } ^ { 4 } \cdot \frac { \log n } { n } \quad \mathrm { a n d } \quad d _ { n } ( T , \widetilde { T } ) \leq C \widetilde { \delta } \sum _ { \overset { j \in \widetilde { N } _ { 0 } ^ { d } } { | j | \leq | \delta | } } \frac { 1 } { j ! } \| T _ { j } - \widetilde { T } _ { j } \| _ { 2 } \delta _ { \widetilde { z } } ^ { | j | } .
$$

Lastly, let ${ \displaystyle \mathcal { K } _ { n } ( \delta ) = \operatorname* { s u p } _ { T , \widetilde { T } \in \bar { T } ( \delta ) } d _ { n } ^ { 2 } ( T , \widetilde { T } ) }$ , by applying the standard chaining via Dudley’s inequality, we can get

$$
\begin{array} { r l } & { { \cal R } _ { n } ( \widetilde \delta ) \leq C \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \rho ^ { * } } \Big [ \int _ { 0 } ^ { k _ { \mathrm { o f f } } } \sqrt { \log \frac { \widetilde \delta } { a } } \mathrm { d } u \Big ] } \\ & { \quad = C \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \rho ^ { * } } \Big [ K _ { \epsilon ^ { * } } ( \widetilde \delta ) \cdot \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde \delta } { a \cdot } ( \widetilde \delta ) } \mathrm { d } u \Big ] } \\ & { \quad \quad = C \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \rho ^ { * } } \Big [ K _ { \epsilon ^ { * } } ( \widetilde \delta ) \cdot 1 ( K _ { \omega } ( \widetilde \delta ) \leq b _ { 2 } ^ { * } \widetilde \delta ^ { 2 } \sqrt { \frac { \log n } { n } } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde \delta } { a \cdot K _ { n } ( \widetilde \delta ) } } \mathrm { d } u \Big ] } \\ & { \quad \quad \quad + C \frac { 1 } { \sqrt { n } } \mathbb { E } _ { n ^ { * } } \Big [ K _ { n } ( \widetilde \delta ) \cdot 1 ( K _ { n } ( \widetilde \delta ) > b _ { 2 } ^ { 2 } \widetilde \delta ^ { 2 } \sqrt { \frac { \log n } { n } } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde \delta } { a \cdot K _ { n } ( \widetilde \delta ) } } \mathrm { d } u \Big ] } \\ & { \quad \quad \quad \leq C _ { 1 } b _ { 2 } ^ { * } \cdot \frac { \log ( n / \widetilde \delta ) } { n } \cdot \widetilde \delta ^ { 2 } , } \end{array}
$$

where we have used the fact that the $u$ -covering entropy of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ relative to metric $d _ { n }$ is at most $\begin{array} { r } { C _ { 2 } \log \frac { \tilde { \delta } } { u } } \end{array}$ for $u \in ( 0 , 1 )$ where $C _ { 2 }$ depends on $( d , D )$ (at most polynomial dependence on $D$ ). By combining this with inequality (47), we obtain that for all $t \geq 1$ ,

$$
\mathbb { P } \Big ( Z _ { n } ( \widetilde { \delta } ) \geq C t ^ { 2 } b _ { 2 } ^ { \frac { d } { 2 } } \cdot \frac { \log ( n / \widetilde { \delta } ) } { n } \cdot \widetilde { \delta } ^ { 2 } \Big ) \leq 2 \exp \Big ( - c t ^ { 2 } \log ( n / \widetilde { \delta } ) \Big ) .
$$

Finally, we apply the peeling technique to extend the above high probability bound on

$Z _ { n } ( { \widetilde { \delta } } )$ to the random radius $\begin{array} { r } { \widetilde { \delta } = \sum _ { { \tiny \begin{array} { c } { j \in \mathbb { N } _ { 0 } ^ { d } } \\ { | j | \leq | \beta | } \end{array} } } \frac { 1 } { j ! } \left. \widehat { f } _ { [ m ] } ^ { ( j ) } - G _ { [ m ] } ^ { * , ( j ) } ( \widetilde { z } ) \right. _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } } \end{array}$ . Specifically, we first set the basic level $\bar { \delta } = ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta } { d } }$ |j|≤b, and for $s = 1 , \cdots , S$ with $\begin{array} { r } { S \le C \log \frac { 1 } { \bar { \delta } } } \end{array}$ , define sets

$$
\begin{array} { l } { { \tiny \displaystyle = \left\{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq | \beta \} \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \left( d + \lfloor \beta \rfloor - 1 \right) } : \displaystyle \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop | j | \leq | \beta \| } } \frac { 1 } { j ! } \| T _ { j } - G ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { \tilde { z } } ) ^ { | j | } \leq \bar { \delta } \right\} } } \\  { \tiny \displaystyle = \left\{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq | \beta \} \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \left( d + \lfloor \beta \rfloor - 1 \right) } : \displaystyle 2 ^ { s - 1 } \bar { \delta } \leq \displaystyle \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop | j | \leq | \beta \| } \frac { 1 } { j ! } \| T _ { j } - G ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { \tilde { z } } ) ^ { | j | } \geq 1 } , } } \end{\right\array} \end{array}
$$

By applying inequality (49) to $\widetilde { \delta } = 2 ^ { s } \overline { { \delta } }$ for $s \in [ S ]$ with sufficiently large constant $t > 0$ , as $C _ { 1 } \leq - \log ( 2 ^ { s } \bar { \delta } ) \leq C _ { 2 } \log n$ , we obtain that

$$
\mathbb { P } \left( Z _ { n } ( \bar { \delta } ) \geq C b _ { 2 } ^ { \frac { d } { 2 } } \frac { \log n } { n } \bar { \delta } ^ { 2 } \right) + \sum _ { s = 1 } ^ { S } \mathbb { P } \left( Z _ { n } ( 2 ^ { s } \bar { \delta } ) \geq C b _ { 2 } ^ { \frac { d } { 2 } } \frac { \log n } { n } 4 ^ { s } \bar { \delta } ^ { 2 } \right) \leq n ^ { - ( c + 1 ) } .
$$

$T \in \widetilde { \mathcal { T } } _ { s }$ and any $s \in \{ 0 \} \cup [ S ]$ , the event $Z _ { n } ( 2 ^ { s } { \bar { \delta } } ) \leq C b _ { 2 } ^ { \frac { d } { 2 } } { \frac { \log n } { n } } 4 ^ { s } { \bar { \delta } } ^ { 2 }$ implies

$$
\begin{array} { r l } & { \displaystyle \mathbb { E } _ { \mu ^ { * } } \bigg [ \Big \| \displaystyle \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } } \frac { 1 } { j ! } \big ( G _ { [ m ] } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \big ) ( Q _ { [ m ] } ^ { * } ( X ) - \tilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { B _ { \tilde { z } } ( \tilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X ) ) \cdot \mathbf { 1 } _ { \tilde { s } _ { m } } ( X ) \bigg ] } \\ & { \displaystyle - \frac { 1 } { | I _ { 1 } | } \displaystyle \sum _ { i \in I _ { 1 } } \bigg [ \Big \| \displaystyle \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } } \frac { 1 } { j ! } \big ( G _ { [ m ] } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \big ) ( Q _ { [ m ] } ^ { * } ( X _ { i } ) - \tilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { B _ { \tilde { z } } ( \tilde { z } ) } ( Q _ { [ m ] } ^ { * } ( X ) ) \cdot \mathbf { 1 } _ { \tilde { s } _ { m } } ( X ) } \\ & { \displaystyle \leq c _ { 1 } b _ { 2 } ^ { \frac { \alpha } { 2 } } \frac { \log n } { n } \left\{ \tilde { \delta } ^ { 2 } + \left( \displaystyle \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| T _ { j } - G _ { [ m ] } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \tilde { \delta } _ { \tilde { z } } ) ^ { | j } \right) ^ { 2 } \right\} . } \end{array}
$$

Finally, since for any $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ , $T _ { f } : = \{ T _ { f , j } = f ^ { ( j ) } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq \lfloor \beta \rfloor }$ must belong to some $\widetilde { \mathcal { T } } _ { s }$ , the claimed result is a consequence of the two preceding displays and a simple union bound over $\mathcal { Z } \in \mathcal { N } _ { h _ { \widetilde { n } } }$ where $\begin{array} { r } { | \mathcal { N } _ { h _ { \widetilde { n } } } | \leq C \frac { \widetilde { n } } { \log { \widetilde { n } } } \leq C n } \end{array}$ .

# E.10 Proof of Lemma 11

Let $\bar { \mathcal { A } } _ { z } = \{ z \in \mathbb { B } _ { 1 } ^ { d } : \| z \| _ { 2 } \leq 1 - \epsilon , G _ { [ m ] } ^ { * } ( z ) \in \mathbb { B } _ { r _ { m } + 0 . 2 5 / L } ( a _ { m } ) \}$ for $\epsilon$ being a small positive constant independent of $n$ that will be specified later. From inequality (40), we can get that (recall that ${ \widehat { f } } _ { [ m ] } = { \widehat { G } } _ { [ m ] } \circ { \widehat { l } } _ { [ m ] } ,$ )

$$
\begin{array} { r l } & { \underset { z \in \widetilde { \mathcal { A } } _ { z } } { \operatorname* { s u p } } \Vert G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \Vert _ { 2 } \leq C _ { \epsilon } \Big ( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { \beta } { d } } , \quad \mathrm { a n d } } \\ & { \underset { z \in \widetilde { \mathcal { A } } _ { z } } { \operatorname* { s u p } } \Vert \mathbf { J } _ { G _ { [ m ] } ^ { * } } ( z ) - \mathbf { J } _ { \widehat { f } _ { [ m ] } } ( z ) \Vert _ { F } \leq C _ { \epsilon } \Big ( \displaystyle \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { \beta - 1 } { d } } , \quad \mathrm { ( s i n c e ~ } \beta > 1 \Big ) } \end{array}
$$

where $C _ { \epsilon }$ is a constant depending on $\epsilon$ . Moreover, since $G _ { [ m ] } ^ { * } \in C _ { C _ { 0 } } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and ${ \widehat { f } } _ { [ m ] } \in$ $C _ { C _ { 0 } } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ for some constant $C _ { 0 } > 0$ , we can extend the supreme to $\Omega _ { m }$ as

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { z \in \Omega _ { m } } \| G _ { [ m ] } ^ { * } ( z ) - \widehat { f } _ { [ m ] } ( z ) \| _ { 2 } \leq C _ { \epsilon } \Big ( \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { \beta } { d } } + C _ { 1 } \sqrt { D d } \epsilon ; } \\ & { \displaystyle \operatorname* { s u p } _ { z \in \Omega _ { m } } \| \mathbf { J } _ { G _ { [ m ] } ^ { * } } ( z ) - \mathbf { J } _ { \widehat { f } _ { [ m ] } } ( z ) \| _ { F } \leq C _ { \epsilon } \Big ( \frac { \log \widetilde { n } } { \widetilde { n } } \Big ) ^ { \frac { \beta - 1 } { d } } + C _ { 1 } \sqrt { D } d \epsilon . } \end{array}
$$

By the fact that for $z \in \mathbb { B } _ { 1 } ^ { d }$ , it holds that $z = Q _ { [ m ] } ^ { * } ( G _ { [ m ] } ^ { * } ( z ) )$ , we obtain $I _ { d } = \mathbf { J } _ { Q _ { [ m ] } ^ { * } } ( G _ { [ m ] } ^ { * } ( z ) ) \mathbf { J } _ { G _ { [ m ] } ^ { * } } ( z )$ Since $Q _ { [ m ] } ^ { * }$ is $L$ -Lipschitz, $\mathbf { J } _ { Q _ { [ m ] } ^ { * } } \bigl ( G _ { [ m ] } ^ { * } ( z ) \bigr )$ has bounded operator norm, which implies $\operatorname* { d e t } ( \mathbf { J } _ { G _ { [ m ] } ^ { * } } ^ { \prime } ( z ) \mathbf { J } _ { G _ { [ m ] } ^ { * } } ( z ) ) \geq c$ for some positive constant $c > 0$ . Therefore, the second display in (50) implies $\begin{array} { r } { \operatorname* { d e t } ( \mathbf { J } _ { \widehat { f } _ { [ m ] } } ^ { I ^ { \prime } } ( z ) \mathbf { J } _ { \widehat { f } _ { [ m ] } } ( z ) ) \geq \frac { c } { 2 } } \end{array}$ for all sufficiently small $\epsilon$ and sufficiently large $n$ (recall that $\begin{array} { r } { \widetilde { n } \geq \frac { 1 } { 2 } \sqrt { n \log n } ) } \end{array}$ . Now by using the identity (using $\hat { f } _ { [ m ] } = \hat { G } _ { [ m ] } \circ \hat { l _ { [ m ] } } )$

$$
\begin{array} { r l } & { \mathbf { J } _ { \widehat { f } _ { [ m ] } } ^ { T } ( z ) \mathbf { J } _ { \widehat { f } _ { [ m ] } } ( z ) = \left( \mathbf { J } _ { \widehat { G } _ { [ m ] } } ( \widehat { l } _ { [ m ] } ( z ) ) \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) \right) ^ { T } \left( \mathbf { J } _ { \widehat { G } _ { [ m ] } } ( \widehat { l } _ { [ m ] } ( z ) ) \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) \right) } \\ & { \qquad = \mathbf { J } _ { \widehat { l } _ { [ m ] } } ^ { T } ( z ) \mathbf { J } _ { \widehat { G } _ { [ m ] } } ^ { T } ( \widehat { l } _ { [ m ] } ( z ) ) \mathbf { J } _ { \widehat { G } _ { [ m ] } } ( \widehat { l } _ { [ m ] } ( z ) ) \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) , } \end{array}
$$

by taking determinant we further obtain (note that $\mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z )$ is a square matrix)

$$
\operatorname* { d e t } ^ { 2 } \left( \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) \right) \cdot \operatorname* { d e t } \left( \mathbf { J } _ { \widehat { G } _ { [ m ] } } ^ { T } ( \widehat { l } _ { [ m ] } ( z ) ) \mathbf { J } _ { \widehat { G } _ { [ m ] } } ( \widehat { l } _ { [ m ] } ( z ) ) \right) \geq \frac { c } { 2 } .
$$

Since both $\hat { G } _ { [ m ] }$ and $\widehat { Q } _ { [ m ] }$ are $L$ -Lipschitz, we can further deduce that $c _ { 1 } \leq \mathrm { d e t } ( \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) ) \leq$ $c _ { 2 }$ for all $z \in \Omega _ { m }$ . In addition, since by definition $\hat { l _ { [ m ] } } \in C _ { C _ { 0 } } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { d } )$ for some constant $C _ { 0 }$ and $\beta > 1$ , for sufficiently small $\epsilon > 0$ , we have that

$$
\frac { 1 } { 2 } c _ { 1 } \le \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l } _ { [ m ] } } ( z ) ) \le 2 c _ { 2 }
$$

holds for all $z \in \Omega _ { m , \epsilon } : = \{ z \in \mathbb { B } _ { \epsilon } ( \widetilde { z } ) : \widetilde { z } \in \Omega _ { m } \}$ , the $\epsilon$ -enlargement of set $\Omega _ { m }$ .

We claim that $\widehat { l } _ { [ m ] }$ is globally invertible over $\Omega _ { m , \epsilon }$ when $\epsilon$ is small enough. Otherwise, suppose there exist distinct $z _ { 0 }$ and $z _ { 1 }$ in $\Omega _ { m , \epsilon }$ such that $\widehat { l } _ { [ m ] } ( z _ { 0 } ) = \widehat { l } _ { [ m ] } ( z _ { 1 } )$ . Since (51) implies $\widehat { l } _ { [ m ] }$ to be locally invertible, meaning that there exists some constant $b _ { 0 } > 0$ independent of $\epsilon$ such that $\left\| z _ { 0 } - z _ { 1 } \right\| \ge b _ { 0 }$ . By the definition of $\Omega _ { m , \epsilon }$ and the Lipschitzness of $\widehat { G } _ { [ m ] }$ and $\widehat { l } _ { [ m ] }$ , there exist $z _ { 0 }$ and $z _ { 1 }$ in $\Omega _ { m }$ such that (for sufficiently small $\epsilon$ )

$$
\| \bar { z } _ { 0 } - \bar { z } _ { 1 } \| \geq \frac { 1 } { 2 } b _ { 0 } , \quad \| \widehat { l } _ { [ m ] } ( \bar { z } _ { 0 } ) - \widehat { l } _ { [ m ] } ( \bar { z } _ { 1 } ) \| _ { 2 } \leq C \epsilon \quad \mathrm { a n d } \quad \| \widehat { f } _ { [ m ] } ( \bar { z } _ { 0 } ) - \widehat { f } _ { [ m ] } ( \bar { z } _ { 1 } ) \| \leq C \epsilon .
$$

The third display above combined with the first display in (50) implies $\big | \big | G _ { [ m ] } ^ { * } \big ( \bar { z } _ { 0 } \big ) \ -$ $G _ { [ m ] } ^ { * } ( \bar { z } _ { 1 } ) \| _ { 2 } \leq C _ { 1 } \epsilon$ . On the other hand, from the first display above and the Lipschitzness

of $Q _ { [ m ] } ^ { * }$ , we have

$$
\begin{array} { r } { \overline { { \mathfrak { b } } } _ { 0 } \leq \| \bar { z } _ { 0 } - \bar { z } _ { 1 } \| = \| Q _ { [ m ] } ^ { * } ( G _ { [ m ] } ^ { * } ( \bar { z } _ { 0 } ) - Q _ { [ m ] } ^ { * } ( G _ { [ m ] } ^ { * } ( \bar { z } _ { 1 } ) ) \| _ { 2 } \leq C \| G _ { [ m ] } ^ { * } ( \bar { z } _ { 0 } ) - G _ { [ m ] } ^ { * } ( \bar { z } _ { 1 } ) \| _ { 2 } \leq C } \end{array}
$$

which is a contradiction when $\epsilon$ is chosen small enough.

Let $\widehat { l } _ { [ m ] } ^ { - 1 } : \widehat { l } _ { [ m ] } ( \Omega _ { m , \epsilon / 2 } ) \to \Omega _ { m , \epsilon / 2 }$ be the inverse of $\widehat { l } _ { [ m ] }$ over $\Omega _ { m , \epsilon / 2 }$ . By using (51) and the inverse function theorem for Hölder space (see for example, Appendix A of [Eldering, 2013]), we can conclude $\widehat { l } _ { [ m ] } ^ { - 1 } \in C _ { C _ { 0 } } ^ { \alpha + 1 } ( \widehat { l _ { [ m ] } } ( \Omega _ { m , \epsilon / 2 } ) ; \mathbb { R } ^ { d } )$ for some sufficiently large constant $C _ { 0 }$ . This completes the proof of the first part in the lemma.

The expression of the density function of ν∗[m],Q[m] $\nu _ { _ { [ m ] } , \widehat { Q } _ { [ m ] } } ^ { \ast } = [ \widehat { Q } _ { [ m ] } ] _ { \# } \bigl ( \rho _ { m } \mu ^ { \ast } \bigr )$ is an immediate consequence by applying the change of variable of $z = \widehat { Q } _ { [ m ] } ( x )$ or $x = G _ { [ m ] } ^ { * } \circ \widehat { l _ { [ m ] } ^ { - 1 } } ( z )$ to the right hand side of (28) and using the definition that $[ G _ { [ m ] } ^ { * } ] _ { \# } \nu _ { [ m ] } ^ { * } = \mu ^ { * } | _ { \widetilde { S } _ { m } } = | \mathbb { P } ( X \in$ $\widetilde { S } _ { m } ) \big ] ^ { - 1 } \boldsymbol { \mu } ^ { * }$ on $\widetilde { S } _ { m }$ . Moreover, since $G _ { [ m ] } ^ { * } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ , $\rho _ { m } \in C ^ { \infty } ( \mathbb { B } _ { L } ^ { D } )$ is supported on $S _ { m } = \mathbb { B } _ { r _ { m } } ( a _ { m } )$ and the restriction of $\nu _ { [ m ] } ^ { * }$ on $\mathbb { B } _ { 1 } ^ { d }$ belongs to $C _ { L } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ , we can conclude that $\nu _ { [ m ] } ^ { \ast } \cdot ( \rho _ { m } \circ G _ { [ m ] } ^ { \ast } ) \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ , where we have used the facts that $\beta \ge \alpha + 1$ and either ${ \mathbb B } _ { r _ { m } } ( a _ { m } ) \cap G _ { [ m ] } ^ { * } ( { \mathbb B } _ { 1 } ^ { d } \setminus { \mathbb B } _ { 1 - \epsilon } ^ { d } ) = \emptyset$ or $\nu _ { [ m ] } ^ { * } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ . This together with $\widehat { l _ { [ m ] } ^ { - 1 } } \in$ $C _ { C _ { 0 } } ^ { \alpha + 1 } ( \tilde { l _ { [ m ] } } ( \Omega _ { m , \epsilon / 2 } ) ; \mathbb { R } ^ { d } )$ implies $\nu _ { \widehat { Q } } ^ { \ast } \in C _ { C _ { 1 } } ^ { \alpha } ( \mathbb { R } ^ { d } )$ for some constant $C _ { 1 }$ .

# E.11 Proof of Lemma 12

The bound for $\epsilon \geq 1$ is trivial, so we only consider $\epsilon \in ( 0 , 1 )$ . Choose $\Delta = \epsilon ^ { \frac { 1 } { \tilde { \gamma } } }$ and $m = \lceil \Delta ^ { - 1 } \rceil$ . For each $\xi = ( \xi _ { 1 } , \xi _ { 2 } , \cdot \cdot \cdot , \xi _ { d } ) \in [ m ] ^ { d }$ , define $z _ { \xi } ~ = ~ \Delta \xi$ and $x _ { \xi } = G ( z _ { \xi } )$ . For any integer $s \in  { \mathbb { N } } _ { 0 }$ , denote $\epsilon _ { s } = \frac { \epsilon } { \Delta ^ { s } } = \epsilon ^ { 1 - \frac { s } { \tilde { \gamma } } }$ . For any multi-index $k \in \mathbb { N } _ { 0 } ^ { d }$ , let $\begin{array} { r } { \alpha _ { \xi } ^ { ( k ) } ( f ) = \big \lfloor \frac { f ^ { ( k ) } ( x _ { \xi } ) } { \epsilon _ { | k | } } \big \rfloor } \end{array}$ .

Consider any two functions $f _ { 1 } , f _ { 2 } \in \tilde { C } _ { 1 } ^ { \tilde { \gamma } } ( \mathbb { R } ^ { D } )$ . Suppose for any $\xi \in [ m ] ^ { d }$ and multi-index $k \in \mathbb { N } _ { 0 } ^ { d }$ with $| k | \leq \lfloor \widetilde { \gamma } \rfloor$ , it holds that $\alpha _ { \xi } ^ { ( k ) } ( f _ { 1 } ) = \alpha _ { \xi } ^ { ( k ) } ( f _ { 2 } )$ . Then by the Lipschitzness of $G$ we can get that for any $z \in [ 0 , 1 ] ^ { d }$ ,

$$
\begin{array} { r l } & { \quad \big | f _ { 1 } ( G ( z ) ) - f _ { 2 } ( G ( z ) ) \big | } \\ & { \leq C \displaystyle \sum _ { k \in \mathbb { N } _ { 0 } ^ { d } , | k | \leq | \widetilde { \gamma } | } \frac { \big | f _ { 1 } ^ { ( k ) } ( x _ { \xi } ) - f _ { 2 } ^ { ( k ) } ( x _ { \xi } ) \big | } { k ! } \Delta ^ { | k | } + \Delta ^ { \widetilde { \gamma } } \leq C _ { 1 } \epsilon . } \end{array}
$$

Therefore, $\| f _ { 1 } - f _ { 2 } \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } \le C \epsilon$ .

First consider $\xi ^ { [ 1 ] } = ( 1 , 1 , \cdots , 1 )$ . For any $k \in \mathbb { N } _ { 0 } ^ { d }$ with $| k | \leq \lfloor \widetilde { \gamma } \rfloor$ , since $f \in C _ { 1 } ^ { \tilde { \gamma } } ( \mathbb { R } ^ { D } )$ , we have α(k)ξ[1] |k|be an integer) is upper bounded by $\alpha _ { \xi ^ { [ 1 ] } } ^ { ( k ) } \leq C \frac { 1 } { \epsilon _ { | k | } }$ . Therefore the total number $\frac { C _ { 1 } } { \epsilon _ { | k | } }$ ξ ξ . Therefore, the logarithm of total number of $N _ { \xi ^ { [ 1 ] } } ^ { ( k ) }$ eof possible values of $\alpha _ { \xi ^ { [ 1 ] } } ^ { ( k ) }$ (it must

choices for $\{ \alpha _ { \xi ^ { [ 1 ] } } ^ { ( k ) } : k \in \mathbb { N } _ { 0 } ^ { d }$ , $| k | \leq \lfloor \widetilde { \gamma } \rfloor \}$ is at most

$$
\sum _ { k \in \mathbb { N } _ { 0 } ^ { d } , | k | \le | \widetilde { \gamma } | } \log N _ { \xi ^ { [ 1 ] } } ^ { ( k ) } \le C \sum _ { k \in \mathbb { N } _ { 0 } ^ { d } , | k | \le | \widetilde { \gamma } | } \left( 1 - \frac { | k | } { \widetilde { \gamma } } \right) \log \frac { 1 } { \epsilon } \le C _ { 1 } \log \frac { 1 } { \epsilon } ,
$$

where constant $C _ { 1 }$ only depends on $d$ and $\gamma$ .

Next consider $\xi ^ { [ 2 ] } = ( 2 , 1 , 1 , \cdots , 1 )$ . For any $f \in C _ { 1 } ^ { \widetilde { \gamma } } ( \mathbb { R } ^ { D } )$ and $k \in \mathbb { N } _ { 0 } ^ { d }$ with $| k | \leq \lfloor \widetilde { \gamma } \rfloor$ , note that

$$
\bigg | f ^ { ( k ) } ( x _ { \xi ^ { [ 2 ] } } ) - \sum _ { \eta \in \mathbb { N } _ { 0 } ^ { d } , \vert \eta \vert \le \vert \widetilde { \gamma } \vert - \vert k \vert } \frac { \epsilon _ { \vert k \vert + \vert \eta \vert } \alpha _ { \xi ^ { [ 2 ] } } ^ { ( k + \eta ) } ( f ) } { \eta ! } ( x _ { \xi ^ { [ 2 ] } } - x _ { \xi ^ { [ 1 ] } } ) ^ { \eta } \bigg | \le C \epsilon _ { \vert k \vert } .
$$

Therefore, given $\{ \alpha _ { \xi ^ { [ 1 ] } } ^ { ( k ) } : k \in \mathbb { N } _ { 0 } ^ { d }$ , $| k | \leq \lfloor \widetilde { \gamma } \rfloor \}$ which consists of all $\alpha ^ { ( k ) }$ values at location $\xi ^ { [ 1 ] }$ e, the total number of possible values of $\{ \alpha _ { \xi ^ { [ 2 ] } } ^ { ( k ) } : k \in \mathbb { N } _ { 0 } ^ { d }$ , $| k | \leq \left\lfloor \widetilde { \gamma } \right\rfloor \}$ at location $\xi ^ { [ 2 ] }$ is at most C |k| = C, which is a constant.

Similarly, by considering the rest grid points in $[ m ] ^ { d }$ through the order of $\xi ^ { [ 3 ] } =$ $( 3 , 1 , 1 , \cdots , 1 )$ , · · · , $\xi ^ { [ m ^ { d } ] } = ( m , m , \cdot \cdot \cdot , m )$ such that the Hamming distance between any two adjacent grid points equals one, we can conclude that given the $\alpha ^ { ( k ) }$ values on the previous grid point $\xi ^ { [ j ] }$ , the $\alpha ^ { ( k ) }$ values on $\xi ^ { [ j + 1 ] }$ can take at most constant $C$ many values, for $j \in [ m ^ { d } - 1 ]$ . Therefore, we can conclude that

$$
\log N \big ( C _ { 1 } ^ { \widetilde { \gamma } } ( \mathbb { R } ^ { D } ) , \| \cdot \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } , \epsilon \big ) \leq C _ { 1 } \log \frac { 1 } { \epsilon } + C _ { 2 } m ^ { d } \leq C _ { 3 } \Big ( \frac { 1 } { \epsilon } \Big ) ^ { \frac { d } { \gamma } } \quad \forall \epsilon \in ( 0 , 1 ) .
$$

# F Proof of Extensions of Main Results

# F.1 Proof of Corollary 1

The proof follows the standard analysis for Lepski’s estimator [Lepskii, 1991]. Consider $\mu ^ { * } \in { \mathcal { S } } ^ { * } ( d , D , \alpha ^ { * } , \beta ^ { * } , \mathcal { O } _ { M } , L )$ in Ap and consider, then it $m \in \mathbb { M } \cap \widehat { \mathbb { M } }$ $\widetilde { \beta } = \operatorname* { m a x } \{ \beta \in { \mathcal { B } } _ { 1 } : \beta \leq \beta ^ { * } \}$ $( \widehat { G } _ { [ m ] } ^ { \dagger } , \widehat { Q } _ { [ m ] } ^ { \dagger } ) = ( \widehat { G } _ { [ m ] } ^ { [ \widehat { \beta } _ { [ m ] } ] } , \widehat { Q } _ { [ m ] } ^ { [ \widehat { \beta } _ { [ m ] } ] } )$ $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$

$$
\sum _ { i \in I _ { 1 } } \| X _ { i } - \widehat { G } _ { [ m ] } ^ { \dagger } \circ \widehat { Q } _ { [ m ] } ^ { \dagger } ( X _ { i } ) \| _ { 2 } ^ { 2 } \cdot { \bf 1 } ( X _ { i } \in S _ { m } ^ { \dagger } ) = 0 ,
$$

and $\widehat { G } _ { [ m ] } ^ { \dag } \in C _ { L } ^ { \widetilde { \beta } } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ , $\widehat { Q } _ { [ m ] } ^ { \dag } \in C _ { L } ^ { \widetilde { \beta } } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ . Then by replacing $\beta$ with $\widetilde { \beta }$ in the proof of Lemma 10 in Section E.8 and the proof of Lemma 6 in Section D.2.4, we can obtain it

holds with probability at least $1 - n ^ { - 1 }$ that for any $m \in \mathbb { M } \cap \widehat { \mathbb { M } }$ ,

$$
\begin{array} { r l } { \displaystyle \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal { T } } _ { m , s } ^ { \dagger } ( f ) - \mathcal { T } _ { m , s } ( f ) \big | \leq C \sqrt { \displaystyle \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \tilde { \beta } } { d } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \tilde { \beta } - 1 } { d } } } & { } \\ { \leq C _ { 1 } \sqrt { \displaystyle \frac { \log n } { n } } + C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta ^ { * } } { d } } + C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \beta ^ { * } - 1 } { d } } , } & { } \end{array}
$$

where the last ineuqlity is due to $\textstyle { \beta ^ { * } - { \tilde { \beta } } \leq { \frac { c } { \log n } } }$ . Then it suffice to show that it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n } }$ that for any $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$ ,

$$
\operatorname* { s u p } _ { \in { \mathcal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal T } _ { m , h } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal T } _ { m , l } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) - { \mathcal T } _ { m , h } ( f ) - { \mathcal T } _ { m , l } ( f ) \big | \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha ^ { * } + \gamma } { 2 \alpha ^ { * } + d } } .
$$

Firstly by replacing $\alpha$ with any $\alpha _ { k } \le \alpha ^ { * }$ in proofs of Lemma 4 and Lemma 5 in Section D.2.2 and Section D.2.3, we can get it holds with probability at least $1 - n ^ { - 1 }$ that for any $\alpha _ { k } \in \{ \alpha \in B _ { 2 } : \alpha \le \alpha ^ { * } \}$ and $m \in \mathbb { M } \cap { \widehat { \mathbb { M } } }$ ,

$$
\begin{array} { r } { \displaystyle \operatorname* { s u p } _ { \tau \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k } ] } ( f ) - \mathcal { I } _ { m , h } ( f ) - \mathcal { I } _ { m , l } ( f ) \right| \overset { ( i ) } { \leq } c _ { 1 } \sqrt { \frac { \log n } { n } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha _ { k } \wedge ( \widehat { \beta } - 1 ) + \gamma } { 2 \alpha _ { k } + d } } } \\ { \overset { ( i i ) } { \leq } c _ { 2 } \sqrt { \frac { \log n } { n } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha _ { k } + \gamma } { 2 \alpha _ { k } + d } } , } \end{array}
$$

where $( i )$ uses $\widehat { Q } _ { [ m ] } ^ { \dag } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ and $( i i )$ uses $\alpha _ { k } \leq \alpha ^ { * } \leq \beta ^ { * } - 1 \leq \widetilde { \beta } - 1 + c ( \log n ) ^ { - 1 } .$ Then let $\alpha _ { k ^ { * } } = \operatorname* { m a x } \{ \alpha \in B _ { 2 } : \alpha \leq \alpha ^ { * } \}$ , if $\widehat { \alpha } _ { [ m ] } < \alpha _ { k ^ { * } }$ , then there exists $k < k ^ { * }$ so that

$$
\begin{array} { r l r } {  { c _ { 0 } \sqrt { \frac { \log n } { n } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha _ { k } + \gamma } { 2 \alpha _ { k } + d } } < \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k * } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k * } ] } ( f ) - \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k } ] } ( f ) - \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k } ] } ( f ) \big | } } \\ & { } & { \leq \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k * } ] } ( f ) + \mathcal { I } _ { m , l } ^ { [ \alpha _ { k * } ] } ( f ) - \mathcal { I } _ { m , h } ( f ) - \mathcal { I } _ { m , l } ( f ) \big | } \\ & { } & { + \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k } ] } ( f ) + \mathcal { I } _ { m , l } ^ { [ \alpha _ { k } ] } ( f ) - \mathcal { I } _ { m , h } ( f ) - \mathcal { I } _ { m , l } ( f ) \big | . } \end{array}
$$

Thus when $c _ { 0 } \geq 2 c _ { 2 }$ , we can obtain

$$
\begin{array} { r l } & { \mathbb { P } _ { \mu ^ { * \otimes n } } \big ( \widehat { \alpha } _ { [ m ] } < \alpha _ { k ^ { * } } \big ) } \\ & { \leq \mathbb { P } _ { \mu ^ { * \otimes n } } \bigg ( \operatorname* { s u p } _ { f \in { \mathcal C } _ { 1 } ^ { \gamma } ( \mathbb R ^ { D } ) } \big | \widehat { \mathcal I } _ { m , h } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) + { \mathcal I } _ { m , l } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) - { \mathcal I } _ { m , h } ( f ) - { \mathcal I } _ { m , l } ( f ) \big | \geq c _ { 2 } \sqrt { \frac { \log n } { n } } \vee \big ( \frac { \log n } { n } \big ) } \\ & { + \mathbb { P } _ { \mu ^ { * \otimes n } } \bigg ( \exists k < k ^ { * } , \operatorname* { s u p } _ { f \in { \mathcal C } _ { 1 } ^ { \gamma } ( \mathbb R ^ { D } ) } \big | \widehat { \mathcal I } _ { m , h } ^ { [ \alpha _ { k } ] } ( f ) + { \mathcal I } _ { m , l } ^ { [ \alpha _ { k } ] } ( f ) - { \mathcal I } _ { m , h } ( f ) - { \mathcal I } _ { m , l } ( f ) \big | \geq c _ { 2 } \sqrt { \frac { \log n } { n } } } \\ & { \leq \frac { 1 } { n } . } \end{array}
$$

Then if $\alpha _ { k ^ { * } } \leq \widehat { \alpha } _ { [ m ] }$

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big | \widehat { \mathcal { I } } _ { m , h } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) - \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) - \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) \big | \leq c _ { 0 } \sqrt { \frac { \log n } { n } } + c _ { 0 } \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha _ { k ^ { * } } } { 2 \alpha _ { k ^ { * } } } }
$$

Thus

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | \widehat { \mathcal { T } } _ { m , h } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal { T } } _ { m , l } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) - \mathcal { I } _ { m , h } ( f ) - \mathcal { I } _ { m , l } ( f ) \big | } \\ & { \leq \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | \widehat { \mathcal { T } } _ { m , h } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \widehat { \alpha } _ { [ m ] } ] } ( f ) - \widehat { \mathcal { I } } _ { m , h } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) - \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) \big | } \\ & { + \underset { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \big | \widehat { \mathcal { T } } _ { m , h } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) + \widehat { \mathcal { I } } _ { m , l } ^ { [ \alpha _ { k ^ { * } } ] } ( f ) - \mathcal { I } _ { m , h } ( f ) - \mathcal { I } _ { m , l } ( f ) \big | . } \end{array}
$$

The desired result then follows from α∗ − clog n ≤ $\begin{array} { r } { \alpha ^ { * } - \frac { c } { \log n } \leq \alpha _ { k ^ { * } } \leq \alpha ^ { * } } \end{array}$

# F.2 Proof of Corollary 2

Firstly for any $\mu _ { 1 } = \mu _ { 2 } \in S ^ { * }$ , it holds that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { 1 } ^ { 0 } \mu _ { 2 } ^ { 0 - 1 } } ( \Phi _ { 2 , \nu } ) } \\ & { = \mathbb { P } _ { \mu _ { 1 } ^ { 0 } \mu _ { 2 } ^ { 0 - 1 } } \Big ( \operatorname* { s u p } _ { f \in \mathcal { C } _ { 1 } ^ { \nu } ( [ \mathbb { R } ^ { D } ] ) } \left( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) \right) \geq c \delta _ { n } ^ { * } \Big ) } \\ & { \leq \mathbb { P } _ { \mu _ { 1 } ^ { 0 } \mu _ { 2 } ^ { 0 - 1 } } \Big ( \operatorname* { s u p } _ { f \in \mathcal { C } _ { 1 } ^ { \nu } ( [ \mathbb { R } ^ { D } ] ) } \left( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \int f ( X ) \mathrm { d } \mu _ { 1 } \right) } \\ & { \quad + \quad \operatorname* { s u p } _ { f \in \mathcal { C } _ { 2 } ^ { \nu } ( [ \mathbb { R } ^ { D } ] ) } \left( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \int f ( Y ) \mathrm { d } \mu _ { 2 } \right) \geq c \delta _ { n } ^ { * } \Big ) } \\ & { \quad + \mathbb { P } _ { \mu _ { 1 } ^ { 0 } \mu _ { 2 } ^ { 0 } } \Big ( \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) - \int f ( Y ) \mathrm { d } \mu _ { 2 } \Big ) \geq c \delta _ { n } ^ { * } \Big ) } \\ & { \leq \mathbb { P } _ { \mu _ { 1 } ^ { 0 } } \Bigg ( \operatorname* { s u p } _ { f \in \mathcal { C } _ { 1 } ^ { \nu } ( [ \mathbb { R } ^ { D } ] ) } \left( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \int f ( X ) \mathrm { d } \mu _ { 1 } \right) \geq \frac { c } { 2 } \delta _ { n } ^ { * } \Bigg ) } \\ &  \quad + \mathbb { P }  \end{array}
$$

Then by Theorem 2, for any constant $r$ , there exists a constant $c$ such that

$$
\begin{array} { r l } & { \mathbb { P } _ { \mu _ { 1 } ^ { \otimes n } } \Big ( \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big ( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \displaystyle \int f ( X ) \mathrm { d } \mu _ { 1 } \big ) \geq \frac { c } { 2 } \delta _ { n } ^ { * } \Big ) } \\ & { + \mathbb { P } _ { \mu _ { 2 } ^ { \otimes n } } \Big ( \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big ( \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) - \displaystyle \int f ( Y ) \mathrm { d } \mu _ { 2 } \big ) \geq \frac { c } { 2 } \delta _ { n } ^ { * } \Big ) \leq \frac { n ^ { - r } } { 2 } . } \end{array}
$$

Moreover, for any $\mu _ { 1 } , \mu _ { 2 } \in S ^ { * }$ with $d _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } ) \geq c _ { 1 } \delta _ { n } ^ { * }$ , it holds that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { 1 } ^ { \otimes } , \mu _ { 2 } ^ { \otimes } } ( 1 - \Phi _ { 2 , \sigma } ) } \\ & { = \mathbb { P } _ { \mu _ { 1 } ^ { \otimes } , \mu _ { 2 } ^ { \otimes } } \bigg ( \underset { f \in \mathcal { L } _ { 1 } ^ { ( \pm | \pmb { \mathscr { D } } ^ { \prime } \rangle ) } } { \nabla } \left( \widehat { \mathcal { T } } ( f ; X _ { 1 : n } ) - \widehat { \mathcal { T } } ( f ; Y _ { 1 : n } ) \right) < c \delta _ { \sigma } ^ { \ast } \bigg ) } \\ & { \leq \mathbb { P } _ { \mu _ { 1 } ^ { \otimes } , \mu _ { 2 } ^ { \otimes } } \bigg ( \underset { f \in \mathcal { L } _ { 1 } ^ { ( \pmb { \mathscr { D } } ^ { \prime } \rangle ) } } { \nabla } \left( \widehat { \mathcal { T } } ( f ; X _ { 1 : n } ) - \int f ( X ) \mathrm { d } \mu _ { 1 } \right) } \\ & { + \underset { f \in \mathcal { L } _ { 1 } ^ { ( \pmb { \mathscr { D } } ^ { \prime } \setminus \{ \pmb { \mathscr { D } } ^ { \prime } \} } } { \nabla } \left( \widehat { \mathcal { T } } ( f ; Y _ { 1 : n } ) - \int f ( Y ) \mathrm { d } \mu _ { 2 } \right) \geq [ \mathcal { C } _ { 1 } - c ] \delta _ { n } ^ { \ast } \bigg ) } \\ & { \leq \mathbb { P } _ { \mu _ { 1 } ^ { \otimes } } \bigg ( \underset { f \in \mathcal { L } _ { 1 } ^ { ( \pmb { \mathscr { D } } ^ { \prime } \setminus \{ \pmb { \mathscr { D } } ^ { \prime } \} } } { \nabla } \left( \widehat { \mathcal { T } } ( f ; X _ { 1 : n } ) - \int f ( X ) \mathrm { d } \mu _ { 1 } \right) \geq \frac { c _ { 1 } - c } { 2 } \delta _ { n } ^ { \ast } \bigg ) } \\ &  + \mathbb { P } _ { \mu _ { 2 } ^ { \otimes } } \bigg ( \underset  f \in \mathcal { L } _ { 1 } ^  \end{array}
$$

Then by Theorem 2, for any constant $r$ and $c$ , there exists a constant $c _ { 1 }$ such that

$$
\begin{array} { r l } & { \mathbb { P } _ { \mu _ { 1 } ^ { \otimes n } } \Big ( \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big ( \widehat { \mathcal { I } } ( f ; X _ { 1 : n } ) - \displaystyle \int f ( X ) \mathrm { d } \mu _ { 1 } \big ) \geq \frac { c _ { 1 } - c } { 2 } \delta _ { n } ^ { * } \Big ) } \\ & { + \mathbb { P } _ { \mu _ { 2 } ^ { \otimes n } } \Big ( \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big ( \widehat { \mathcal { I } } ( f ; Y _ { 1 : n } ) - \displaystyle \int f ( Y ) \mathrm { d } \mu _ { 2 } \big ) \geq \frac { c _ { 1 } - c } { 2 } \delta _ { n } ^ { * } \Big ) \leq \frac { n ^ { - r } } { 2 } . } \end{array}
$$

Proof is completed.

# F.3 Proof of Theorem 4

We first describe the estimator. Similar as the analysis in Section 3.1, our proposed minimax-optimal estimator $\widehat { \mu } ^ { \circ }$ is constructed in three steps. Let $[ n ] = I _ { 1 } \cap I _ { 2 }$ be a random splitting of the data indices into two sets with $| I _ { 1 } | = \lceil n / 2 \rceil$ and $\left| I _ { 2 } \right| = n - \left| I _ { 1 } \right|$ .

Step 1: (Submanifold estimation) Recall $K _ { 1 }$ to be the $1 / L$ -enlargement of $K _ { 0 }$ given by $K _ { 1 } = \{ x \in B _ { 1 / L } ( y ) : y \in K _ { 0 } \}$ , we use the first half of data to compute

$$
( \widehat { G } , \widehat { Q } ) = \underset { G \in \mathcal { G } , Q \in \mathcal { Q } } { \arg \operatorname* { m i n } } \bigg ( \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \Big [ \| X _ { i } - G ( Q ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \mathbf { 1 } _ { K _ { 1 } } ( X _ { i } ) \Big ] \bigg ) .
$$

where recall $\mathcal { G } = C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and $\mathcal { Q } = C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ . Let $\begin{array} { r } { \widehat { p } _ { 0 } = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) } \end{array}$ denote the sample frequency of falling into $K _ { 0 }$ .

Step 2: (Surrogate functional construction) Follow the analysis in Section 3.1, we construct a finite sample surrogate to $\int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * }$ as follows. Firstly if ${ \widehat { p _ { 0 } } } < { \sqrt { \frac { \log n } { n } } }$ , then define Jb◦(f ) = 0; otherwise, let J be the largest integer such that 2J ≤ ( nlog n ) , $\Pi _ { J } f$ denote the projection of any $f \in { \mathcal { F } }$ onto the first scale $J$ wavelet coefficients and $\Pi _ { J } ^ { \perp } f = f - \Pi _ { J } f$ . The expectation of low frequency components of $f$ : $\begin{array} { r l } { \int _ { K _ { 0 } } \Pi _ { J } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathrm { d } \mu ^ { * } } \end{array}$ is estimated

with the empirical mean

$$
\widehat { \mathcal { I } } _ { l } ^ { \circ } ( f ) = \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } [ \Pi _ { J } f ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) ] .
$$

For the high frequency part, we construct kernel density estimator (KDE) to estimate the density of $\widehat { Q } _ { \# } ( \mathbf { 1 } _ { K _ { 0 } } \cdot \boldsymbol { \mu } ^ { * } )$ . More specifically, choose a kernel function $k ( x ) \in C _ { c _ { 1 } } ^ { 1 + \alpha } ( \mathbb { R } )$ such that (1) $\operatorname { s u p p } ( k ( x ) ) \subset [ 0 , 1 ]$ ; (2) $\textstyle \int k ( x ) \mathrm { d } x = 1$ ; (3) for any $j \in \mathbb { N } ^ { + }$ with $j \le \lceil \alpha \rceil$ , $\begin{array} { r } { \int x ^ { j } \bar { k } ( x ) \mathrm { d } x = 0 } \end{array}$ . Define the kernel density estimator

$$
\bar { \nu } _ { \widehat { Q } } ( y ) = \frac { 1 } { h ^ { d } | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { j } ( X _ { i } ) - y _ { j } } { h } \Big ) \Big ) \cdot \mathbf { 1 } _ { K _ { 1 / 4 } } ( X _ { i } ) .
$$

with bandwidth $h = \left( { \textstyle { \frac { \log n } { n } } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ . Define

$$
\widehat { U } = \bigcup _ { i \in I _ { 2 } : X _ { i } \in K _ { 1 / 4 } } \mathbb { B } _ { c _ { 0 } ( \frac { 1 } { \widehat { p } _ { 0 } } \cdot \frac { \log n } { n } ) ^ { \frac { 1 } { d } } } ( X _ { i } )
$$

for a large enough constant $c _ { 0 }$ , we use $\{ y = \widehat { Q } ( x ) | x \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( x ) ) \in K _ { 0 } \}$ to estimate the support of $\widehat { Q } _ { \# } ( \mathbf { 1 } _ { K _ { 0 } } \cdot \boldsymbol { \mu } ^ { * } )$ . Therefore, we can define the functional

$$
\widehat { \mathcal { T } } _ { h } ^ { \circ } ( f ) = \int _ { \{ y = \widehat { Q } ( x ) \mid x \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( x ) ) \in K _ { 0 } \} } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \bar { \nu } _ { \widehat { Q } } ( y ) \mathrm { d } y
$$

to estimate $\begin{array} { r } { \int _ { K _ { 0 } } \Pi _ { J } ^ { \perp } f \bigl ( \widehat { G } ( \widehat { Q } ( X ) ) \bigr ) \mathrm { d } \mu ^ { * } } \end{array}$ . Finally we can construct a (sample version of) higher-order smoothness correction $\widehat { \mathcal { I } } _ { s } ^ { \circ } ( f )$ to $\begin{array} { r l } { \int _ { K _ { 0 } } f \bigl ( } & { { } f ( \widehat { G } \circ \widehat { Q } ( X ) ) \mathrm { d } \mu ^ { * } } \end{array}$ for approximating $\int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * }$ , defined as

$$
\widehat { \mathcal { T } } _ { s } ^ { \circ } ( f ) = - \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \sum _ { \underset { 1 \leq | j | \leq | \gamma | } { j \in \mathbb { N } _ { 0 } ^ { D } } } \left[ \frac { 1 } { j ! } f ^ { ( j ) } ( X _ { i } ) ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) - X _ { i } ) ^ { j } \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) \right]
$$

Putting all pieces together, we can construct. a estimator of $\int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * }$ as

$$
\begin{array} { r } { \widehat { \mathcal { T } } ^ { \circ } ( f ) = \widehat { \mathcal { T } } _ { s } ^ { \circ } ( f ) + \widehat { \mathcal { T } } _ { l } ^ { \circ } ( f ) + \widehat { \mathcal { T } } _ { h } ^ { \circ } ( f ) , } \end{array}
$$

for arbitrary $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ .

Step 3: (Generative model estimation) Then we can define the estimator

$$
\widehat { \mu } ^ { \circ } = \operatorname* { i n f } _ { \mu = G _ { \widehat { \mu } ^ { \nu } } ^ { \theta } } \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big ( \frac { 1 } { \widehat { p } _ { 0 } } \cdot \widehat { \mathcal { T } } ^ { \circ } ( f ) - \int f ( X ) \mathrm { d } \mu \Big ) .
$$

We now show that $\widehat { \mu } ^ { \circ }$ achieves the near-optimal rate. Consider a fixed $\mu ^ { \ast } \in \overline { { S } } ^ { \ast }$ , it suffices

to show that

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big | \int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * } - \widehat { \mathcal { T } } ^ { \circ } ( f ) \Big | \leq C \left( \frac { n } { \log n } \right) ^ { - \frac 1 2 } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \left( \frac { n } { \log n } \right) ^ { - \frac { \gamma \beta } { d } } ,
$$

where the regularized surrogate $\widehat { \mathcal { I } } ^ { \circ } ( f ) = \widehat { \mathcal { I } } _ { l } ^ { \circ } ( f ) + \widehat { \mathcal { I } } _ { h } ^ { \circ } ( f ) + \widehat { \mathcal { I } } _ { s } ^ { \circ } ( f )$ . We may similarly decompose the target functional into three terms as $\begin{array} { r } { \int _ { K _ { 0 } } f ( \boldsymbol { X } ) \mathrm { d } \mu ^ { * } = \mathcal { T } _ { l } ^ { \circ } ( f ) + \mathcal { T } _ { h } ^ { \circ } ( f ) + \mathcal { T } _ { s } ^ { \circ } ( f ) } \end{array}$ , where

$$
\begin{array} { r l } & { \mathcal { T } _ { l } ^ { \circ } ( f ) = \displaystyle \int _ { K _ { 0 } } \Pi _ { J } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathrm { d } \mu ^ { * } , } \\ & { \mathcal { T } _ { h } ^ { \circ } ( f ) = \displaystyle \int _ { K _ { 0 } } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathrm { d } \mu ^ { * } , } \\ & { \mathcal { T } _ { s } ^ { \circ } ( f ) = \displaystyle \int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * } - \displaystyle \int _ { K _ { 0 } } f \big ( \widehat { G } ( \widehat { Q } ( X ) ) \big ) \mathrm { d } \mu ^ { * } . } \end{array}
$$

Note that similar as the analysis in Appendix D.2, we only need to consider the case that $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( X \in K _ { 0 } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ and p0 ≥ q ${ \widehat { p _ { 0 } } } \geq { \sqrt { \frac { \log n } { n } } }$ . Recall $\mu ^ { \ast } \in \overline { { \mathcal { S } } } ^ { \ast }$ , then there exists a compact set $\widetilde { K } \supseteq K _ { 1 }$ such that $\mu ^ { * } | _ { \widetilde K }$ can be expressed as a generative model $\mu ^ { * } | _ { \widetilde K } = G _ { \# } ^ { * } \nu ^ { * }$ , where $G ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ . Denote $\Omega ^ { * } = \operatorname { s u p p } ( \nu ^ { * } )$ , then there exists $Q ^ { * } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ such that for any $z \in \Omega ^ { * }$ , $Q ^ { * } ( G ^ { * } ( z ) ) = z$ and $Q ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ .

The following three lemmas show that $\widehat { \mathcal { I } } _ { s } ^ { \circ }$ , $\hat { \mathcal { T } } _ { l } ^ { \circ }$ and $\widehat { \mathcal { I } } _ { h } ^ { \mathrm { o } }$ are good estimators for $\mathcal { I } _ { s } ^ { \circ }$ , $\mathcal { I } _ { l } ^ { \mathrm { o } }$ and $\mathcal { I } _ { h } ^ { \mathrm { o } }$ respectively.

Lemma 19 (Smoothness correction). When $\mu ^ { * } \in \overline { { \mathcal { S } } } ^ { * }$ , it holds with probability at least $1 - n ^ { - c }$ that the functional $\widehat { \mathcal { I } } _ { s } ^ { \circ } : C ^ { \gamma } ( \mathbb { R } ^ { D } ) \to \mathbb { R }$ satisfies

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left. \widehat { \mathcal { T } } _ { s } ^ { \circ } ( f ) - \mathcal { T } _ { s } ^ { \circ } ( f ) \right. \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma \beta } { d } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \beta - 1 } { d } } .
$$

Lemma 20 (Low frequency components). When $\mu ^ { * } \in \overline { { S } } ^ { * }$ , it holds with probability at least $1 - n ^ { - c }$ that the functional $\widehat { \mathcal { I } } _ { l } ^ { \circ } : C ^ { \gamma } ( \mathbb { R } ^ { D } ) \to \mathbb { R }$ satisfies

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left. \widehat { \mathcal { T } } _ { l } ^ { \circ } ( f ) - \mathcal { T } _ { l } ^ { \circ } ( f ) \right. \leq C \sqrt { \frac { \log n } { n } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } .
$$

Lemma 21 (High frequency components). When $\mu ^ { * } \in \overline { { \mathcal { S } } } ^ { * }$ , it holds with probability at least $1 - n ^ { - c }$ that the functional $\widehat { \mathcal { T } } _ { h } ^ { \circ } : C ^ { \gamma } ( \mathbb { R } ^ { D } ) \to \mathbb { R }$ satisfies

$$
\operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \left| \widehat { \mathcal { T } } _ { h } ^ { \circ } ( f ) - \mathcal { T } _ { h } ^ { \circ } ( f ) \right| \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } .
$$

By combining Lemmas 19, 20 and 21, similar as the proof of minimax upper bound in

# F.3.1 Proof of Lemma 19

Recall $K _ { r } = \{ x \in B _ { | r | / L } ( y ) : y \in K _ { 0 } \}$ for $r > 0$ and $K _ { r } = \{ x \in \mathbb { R } ^ { D } : B _ { | r | / L } ( x ) \subset K _ { 0 } \}$ for $r < 0$ . Define $\mathcal { M } ^ { \ast } = G ^ { \ast } ( \Omega ^ { \ast } )$ and $\mathcal { Z } _ { a } = Q ^ { * } ( \mathcal { M } ^ { * } \cap K _ { a } )$ . Then $\mathcal { Z } _ { 1 } \subset [ - L , L ] ^ { d }$ and for any $z _ { 1 } , z _ { 2 } \in \mathcal { Z } _ { 1 }$ ,

$$
\| G ^ { * } ( z _ { 1 } ) - G ^ { * } ( z _ { 2 } ) \| _ { 2 } \leq L \sqrt { D } \| z _ { 1 } - z _ { 2 } \| _ { 2 } .
$$

Let $\begin{array} { r } { \widetilde { n } = \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \cdot n \geq \mathbb { P } _ { \mu ^ { * } } ( X \in K _ { 0 } ) \cdot n \geq \frac { 1 } { 2 } \sqrt { n \log n } } \end{array}$ and $\begin{array} { r } { \epsilon _ { n } = c _ { 0 } \left( \frac { \log \widetilde { n } } { \widetilde { n } } \right) ^ { \frac { 1 } { d } } } \end{array}$ , combined with (53), when $n$ is large enough, for any $z ^ { \ast } \in \mathcal { Z } _ { 1 / 2 }$ , it holds that

$$
\mathbf { 1 } _ { \mathcal { M } ^ { \ast } \cap G ^ { \ast } ( \mathbb { B } _ { \epsilon _ { n } } ( z ^ { \ast } ) ) } ( X ) \leq \mathbf { 1 } _ { \mathcal { M } ^ { \ast } \cap K _ { 1 } } ( X ) .
$$

Therefore, for any $z ^ { \ast } \in \mathcal { Z } _ { 1 / 2 }$ ,

$$
\frac { 1 } { \lceil \frac { n } { 2 } \rceil } \sum _ { i \in I _ { 1 } } \Big [ \| G ^ { * } ( Q ^ { * } ( X _ { i } ) ) - \widehat { G } ( \widehat { Q } ( G ^ { * } ( Q ^ { * } ( X _ { i } ) ) ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathcal { M } ^ { * } \cap \mathcal { G } ^ { * } ( \mathbb { B } _ { \epsilon _ { n } } ( z ^ { * } ) ) } ( X _ { i } ) \Big ] = 0 .
$$

Let $\widehat { l } = \widehat { Q } ( G ^ { * } ( z ) )$ , similar as the proof of Lemma 10 in Section E.8, we can obtain that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\begin{array} { r l } & { \underset { z \in \mathcal { Z } _ { 1 / 2 } } { \operatorname* { s u p } } \| G ^ { * } ( z ) - \widehat { G } ( \widehat { l } ( z ) ) ) \| _ { 2 } \leq C \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { \beta } { d } } ; } \\ & { \underset { x \in \mathcal { M } ^ { * } \cap K _ { 1 / 2 } } { \operatorname* { s u p } } \| x - \widehat { G } ( \widehat { Q } ( x ) ) \| _ { 2 } \leq C \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { \beta } { d } } , } \end{array}
$$

and thus for any $\begin{array} { r } { \eta \in ( 0 , \frac { d } { \beta } ] } \end{array}$

$$
\int _ { K _ { 0 } } \| X - \widehat { G } ( \widehat { Q } ( X ) ) \| ^ { \eta } \mathrm { d } \mu ^ { * } \leq C \mathbb { P } _ { \mu ^ { * } } ( X \in K _ { 0 } ) \cdot \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { \beta } { d } } \leq \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta } { d } } ,
$$

and for any $\begin{array} { r } { \eta > { \frac { d } { \beta } } } \end{array}$

$$
\int _ { K _ { 0 } } \| X - \widehat { G } ( \widehat { Q } ( X ) ) \| ^ { \eta } \mathrm { d } \mu ^ { * } \leq C C _ { 1 } ^ { \eta - \frac { d } { \beta } } \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta } { d } } .
$$

Then similar as the proof of Lemma 6, it holds with probability at least $\textstyle 1 - { \frac { 2 } { n ^ { 2 } } }$ that for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ ,

$$
\begin{array} { r l } & { \displaystyle | \mathcal { T } _ { s } ^ { \circ } ( f ) - \widehat { \mathcal { T } } _ { s } ^ { \circ } ( f ) | } \\ & { \displaystyle = | \int _ { K _ { 0 } } f ( X ) \mathrm { d } \mu ^ { * } - \int _ { K _ { 0 } } f ( \widehat { G } ( \widehat { Q } ( X ) ) \mathrm { d } \mu ^ { * } } \\ & { \displaystyle + \frac { 1 } { | I _ { 2 } | } \sum _ { i \in [ I _ { 2 } ] \atop 1 \leq [ I _ { 1 } ] \leq [ I _ { 1 } ] } \sum _ { j \in [ I ] } [ \frac { 1 } { j ! } f ^ { ( j ) } ( X _ { i } ) ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) - X _ { i } ) ^ { j } \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) ] } \\ & { \displaystyle \leq C _ { 1 } \sqrt { \frac { \log n } { n } } + C _ { 1 } ( \frac { \log n } { n } ) ^ { \frac { \gamma _ { \delta } } { d } } + C _ { 1 } ( \frac { \log n } { n } ) ^ { \frac { \gamma + \delta - 1 } { d } } . } \end{array}
$$

# F.3.2 Proof of Lemma 20

Same as the proof of Lemma 4 in Section D.2.2, for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , it can be written as

$$
f ( \boldsymbol { x } ) = \underbrace { \sum _ { k \in \mathbb { Z } ^ { D } } b _ { k } \phi _ { k } ( \boldsymbol { x } ) + \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 1 } ^ { J } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { J } f } + \underbrace { \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { + \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( \boldsymbol { x } ) } _ { \Pi _ { j } ^ { \perp } f } ,
$$

where $\{ \phi _ { k } , \psi _ { l j k } | l \in [ 2 ^ { D } - 1 ] , j \in \mathbb { N } , k \in \mathbb { Z } ^ { D } \}$ is the orthonormal wavelet basis for Besov space on $\mathbb { R } ^ { D }$ and recall $J$ is the largest integer such that $2 ^ { J } \leq \left( { \frac { n } { \log n } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ . Then define

$$
\begin{array} { r l } & { \widetilde { \mathbb { S } } = \{ k \in \mathbb { Z } ^ { D } | \operatorname { s u p p } ( \phi _ { k } ) \cap \widehat { G } ( [ - L , L ] ^ { d } ) \neq \emptyset \} ; } \\ & { \widetilde { \mathbb { S } } _ { l j } = \{ k \in \mathbb { Z } ^ { D } , | \operatorname { s u p p } ( \psi _ { l j k } ) \cap \widehat { G } ( [ - L , L ] ^ { d } ) \neq \emptyset \} . } \end{array}
$$

By changing $\rho _ { m } ( x )$ in the proof of Lemma 4 in Section D.2.2 to ${ \bf 1 } _ { K _ { 0 } } ( x )$ , we can get it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ ,

$$
\begin{array} { r l } & { \displaystyle \left| \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } [ \Pi _ { J } f ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) ] - \mathbb { E } _ { \mu ^ { * } } [ \Pi _ { J } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) ] \right| } \\ & { \leq C \displaystyle \sum _ { k \in \widehat { \mathbb { S } } } \left| \mathbb { E } _ { \mu ^ { * } } [ \phi _ { k } ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) ] - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } [ \phi _ { k } ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X _ { i } ) ] \right| } \\ & { + \displaystyle \sum _ { i = 1 } ^ { 2 p - 1 } \displaystyle \sum _ { j = 1 } ^ { J } \displaystyle \sum _ { k \in \widehat { \mathbb { S } } _ { k _ { 0 } } } 2 ^ { - \frac { p _ { j } } { 2 } - j \gamma } \left| \mathbb { E } _ { \mu ^ { * } } [ \psi _ { i j k } ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) ] - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } [ \psi _ { i j k } ^ { \prime } ( \widehat { G } ( \widehat { Q } ( X _ { i } ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) ] \right| } \\ & { \leq C _ { 1 } \sqrt { \displaystyle \frac { \log p } { n } } + ( \displaystyle \frac { \log n } { n } ) ^ { \frac { \alpha + \gamma } { 2 + d } } . } \end{array}
$$

# F.3.3 Proof of Lemma 21

Recall $\mathcal { M } ^ { \ast } = G ^ { \ast } ( \Omega ^ { \ast } )$ ; $K _ { r } = \{ x \in B _ { | r | / L } ( y ) : y \in K _ { 0 } \}$ for $r > 0$ and $K _ { r } = \{ x \in \mathbb { R } ^ { D }$ : $B _ { | r | / L } ( x ) \subset K _ { 0 } \}$ for $r < 0$ ; and $\mathcal { Z } _ { a } = Q ^ { * } ( \mathcal { M } ^ { * } \cap K _ { a } )$ . Consider $\widehat { l } = \widehat { Q } \circ G ^ { \ast }$ , then similar as the proof of Lemma 11 in Section E.10, we can obtain that there exist positive constants $( n _ { 0 } , c _ { 2 } , c _ { 3 } )$ such that when $n \geq n _ { 0 }$ , for any $z \in \mathcal { Z } _ { 1 / 2 }$ , it holds that

$$
c _ { 2 } \leq \vert \mathrm { d e t } ( { \bf J } _ { \hat { l } } ( z ) ) \vert \leq c _ { 3 } .
$$

Moreover, by the lipschitzness of $G ^ { * }$ and $\bigcup _ { z \in \Omega ^ { * } , G ^ { * } ( z ) \in K _ { 1 } } B _ { 1 / L } ( z ) \subset \Omega ^ { * }$ , there exists a constant $\epsilon > 0$ such that

$$
\{ z \in \mathbb { B } _ { \epsilon } ( z ^ { * } ) : z ^ { * } \in \mathcal { Z } _ { 1 / 3 } \} \subset \mathcal { Z } _ { 1 / 2 } .
$$

Thus if there exist $z _ { 1 } , z _ { 2 } \in \mathcal { Z } _ { \frac { 1 } { 3 } }$ such that $\| z _ { 1 } - z _ { 2 } \| \leq \epsilon$ and $\widehat { l } ( z _ { 1 } ) = \widehat { l } ( z _ { 2 } )$ , then by $\beta > 1$ and for any $t \in [ 0 , 1 ]$ , $| \mathrm { d e t } ( \mathbf { J } _ { \hat { l } } ( t z _ { 1 } + ( 1 - t ) z _ { 2 } ) | \geq c _ { 2 } > 0$ , we can obtain that there exists a positive constant $c _ { 4 }$ such that $\| z _ { 1 } - z _ { 2 } \| \geq \epsilon \land c _ { 4 }$ . On the opposite side, by equation (54), it holds that

$$
z _ { 1 } - z _ { 2 } \| _ { 2 } = \| Q ^ { * } ( G ^ { * } ( z _ { 1 } ) ) - Q ^ { * } ( G ^ { * } ( z _ { 2 } ) ) \| _ { 2 } \leq \sqrt { d } L \| G ^ { * } ( z _ { 1 } ) - G ^ { * } ( z _ { 2 } ) \| _ { 2 } \leq C \big ( \frac { \log \widetilde { n } } { \widetilde { n } } \big ) ^ { \frac { \beta } { d } } .
$$

Therefore, when $n$ is large enough, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that $\widehat { l }$ is one to one on $\mathcal { Z } _ { \frac { 1 } { 3 } }$ . So we can define $\widehat { l } ^ { - 1 } : \widehat { l } \bigl ( \mathcal { Z } _ { \frac { 1 } { 3 } } \bigr ) \to \mathcal { Z } _ { \frac { 1 } { 3 } }$ as the inverse of $\widehat { l } | _ { \mathcal { Z } _ { \frac { 1 } { 3 } } }$ and by inverse function theorem in holder space (see for example, Appendix A of [Eldering, 2013]), it holds that $\widehat { l } ^ { - 1 } \in C _ { C _ { 1 } } ^ { \beta } ( \widehat { l } ( \mathcal { Z } _ { \frac { 1 } { 3 } } ) ; \mathbb { R } ^ { d } )$ .

Furthermore, recall $\begin{array} { r } { \Pi _ { J } ^ { \perp } ( f ) = \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = J + 1 } ^ { + \infty } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( x ) } \end{array}$ where $\begin{array} { r } { 2 ^ { J } = c \left( \frac { n } { \log n } \right) ^ { \frac { 1 } { 2 \alpha + d } } } \end{array}$ $| f _ { l j k } | \le C 2 ^ { - \frac { D j } { 2 } - j \gamma }$ and $\begin{array} { r } { \| \sum _ { k \in \mathbb { Z } ^ { D } } \psi _ { l j k } \| _ { \infty } \leq C 2 ^ { \frac { D _ { j } } { 2 } } } \end{array}$ . Then by the fact that there exists a constant $C _ { 1 }$ such that for any $j \in [ 2 ^ { D } - 1 ]$ and $j \in \mathbb Z$ , $\begin{array} { r } { \sum _ { k \in \mathbb { Z } ^ { D } } | \psi _ { l j k } ( z ) | \le C _ { 1 } 2 ^ { \frac { D j } { 2 } } } \end{array}$ (recall that the support of $\psi _ { l j k }$ is contained in $\mathbb { B } _ { 2 ^ { - j } C } ( 2 ^ { 1 - j } k ) )$ , we can get for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ ,

$$
| \Pi _ { J } ^ { \perp } f ( x ) | \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \gamma } { 2 \alpha + d } } ,
$$

and

$$
\begin{array} { r l } & { \bigg | \int \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) \mathrm { d } \mu ^ { * } - \int \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { \{ X \in K _ { 1 / 4 } : \widehat { G } ( \widehat { Q } ( X ) ) \in K _ { 0 } \} } ( X ) \mathrm { d } \mu ^ { * } \bigg | } \\ & { \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \gamma } { 2 \alpha + d } } \int \left| \mathbf { 1 } _ { K _ { 0 } } ( X ) - \mathbf { 1 } _ { \{ X \in K _ { 1 / 4 } : \widehat { G } ( \widehat { Q } ( X ) ) \in K _ { 0 } \} } ( X ) \right| \mathrm { d } \mu ^ { * } . } \end{array}
$$

By equation (54), there exists a constant $c$ such that for $\delta _ { n } = c ( \frac { \log \widetilde { n } } { \widetilde { n } } ) ^ { \frac { \beta } { d } }$ with ${ \widetilde { n } } = \mathbb { P } _ { \mu ^ { * } } ( X \in$

$\begin{array} { r } { \widetilde { K } ) \cdot n \ge \mathbb { P } _ { \mu ^ { * } } ( X \in { K _ { 0 } } ) \cdot n \ge \frac { 1 } { 2 } \sqrt { n \log n } } \end{array}$ , it holds that

$$
\begin{array} { r l } & { \displaystyle \int \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { K _ { 0 } } ( X ) \mathrm { d } \mu ^ { * } - \displaystyle \int \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { \{ X \in K _ { 1 / 4 } : \widehat { G } ( \widehat { Q } ( X ) ) \in K _ { 0 } \} } ( X ) \mathrm { d } \mu ^ { * } } \\ & { \displaystyle \overset { ( i ) } { \leq } C \left( \frac { \log n } { n } \right) ^ { \frac { \gamma } { 2 \alpha + d } } \cdot \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \cdot \displaystyle \int \left( \mathbf { 1 } _ { K _ { \delta _ { n } } } ( G ^ { * } ( z ) ) - \mathbf { 1 } _ { K _ { - \delta _ { n } } } ( G ^ { * } ( z ) ) \right) \nu ^ { * } ( z ) \mathrm { d } z } \\ & { \displaystyle \overset { ( i i ) } { \leq } C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \delta } { 2 \alpha + d } } \vee \displaystyle \sqrt { \frac { \log n } { n } } } \\ & { \leq C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \gamma + \alpha } { 2 \alpha + d } } \vee \displaystyle \sqrt { \frac { \log n } { n } } , } \end{array}
$$

where $( i )$ is due to equation (54), $( i i )$ is due to the fact that $\left| \mathbb { P } _ { \nu ^ { * } } \mathopen { } \mathclose \bgroup \left( \lbrace z \in \Omega : G ^ { * } ( z ) \in K _ { 0 } \rbrace \aftergroup \egroup \right) - \right.$ $\mathbb { P } _ { \nu ^ { * } } \bigl ( \{ z \in \Omega : G ^ { * } ( z ) \in K _ { r } \} \bigr ) \bigr | \le L | r |$ holds for any $| r | \leq 1$ and the last step is due to $\alpha \leq$ $\beta - 1$ . It remains to bound the difference between $\begin{array} { r } { \int \Pi _ { J } ^ { \bot } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { \{ X \in K _ { 1 / 4 } : \widehat { G } ( \widehat { Q } ( X ) ) \in K _ { 0 } \} } ( X ) \mathrm { d } \mu ^ { * } } \end{array}$ and

$$
\widehat { \mathcal { T } } _ { h } ^ { \circ } ( f ) = \int _ { \{ y = \widehat { Q } ( x ) : x \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( x ) ) \in K _ { 0 } \} } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \bar { \nu } _ { \widehat { Q } } ( y ) \mathrm { d } y
$$

for arbitrary $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { d } )$ , where recall

$$
\widehat { U } = \bigcup _ { i \in I _ { 2 } : X _ { i } \in K _ { 1 / 4 } } \mathbb { B } _ { c _ { 0 } ( \frac { 1 } { \widehat { p } _ { 0 } } \cdot \frac { \log n } { n } ) ^ { \frac { 1 } { d } } } ( X _ { i } ) .
$$

Next lemma shows that $\mathcal { M } ^ { \ast } \cap K _ { 1 / 4 } \subset \widehat { U }$ with high probability.

Lemma 22. There exists a constant $c _ { 1 }$ such that when $c _ { 0 } \geq c _ { 1 }$ , it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that $\mathcal { M } ^ { * } \cap K _ { 1 / 4 } \subset \widehat { U } = \bigcup _ { i \in I _ { 2 } : X _ { i } \in K _ { 1 / 4 } } \mathbb { B } _ { c _ { 0 } ( \frac { 1 } { \widehat { p _ { 0 } } } \cdot \frac { \log n } { n } ) ^ { \frac { 1 } { d } } } ( X _ { i } ) .$

Let

$$
\widehat { \Omega } = \{ y = \widehat { Q } ( x ) : x \in \mathcal { M } ^ { * } \cap K _ { 1 / 4 } ; \widehat { G } ( \widehat { Q } ( x ) ) \in K _ { 0 } \} .
$$

Since

$$
\begin{array} { r l }   { \int \Pi _ { J } ^ { \perp } f ( \widehat { G } ( \widehat { Q } ( X ) ) ) \mathbf { 1 } _ { \{ X \in K _ { 1 / 4 } , \widehat { G } ( \widehat { Q } ( X ) ) \} \in K _ { 0 } \} \mathrm { d } \mu ^ { * } } } \\ & { = P _ { \mu ^ { * } } ( X \in \widetilde { K } ) \int _ { \widehat { \Omega } } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \nu ^ { * } ( \widehat { l ^ { - 1 } } ( y ) ) | \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l ^ { - 1 } } } ( y ) ) | \mathbf { 1 } _ { \{ y : \widehat { l ^ { - 1 } } ( y ) \in Q ^ { * } ( M ^ { * } \cap K _ { 1 / 4 } ) \} } ( y ) \mathrm { d } y } \\ & { = P _ { \mu ^ { * } } ( X \in \widetilde { K } ) \int _ { \widehat { \Omega } } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \nu ^ { * } ( \widehat { l ^ { - 1 } } ( y ) ) | \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l ^ { - 1 } } } ( y ) ) | \mathrm { d } y . } \end{array}
$$

where recall that $\widehat { l } ^ { - 1 }$ is the inverse of $\widehat { l } | _ { \mathcal { Z } _ { \frac { 1 } { 3 } } }$ with ${ \widehat { l } } ( z ) = { \widehat { Q } } ( G ^ { * } ( z ) )$ . While the definition of $\widehat { \Omega }$ in equation (55) is intractable due to the unknown $\mathcal { M } ^ { * }$ . The next lemma shows that with high probability, $\widehat { \Omega } = \{ y = \widehat { Q } ( x ) : x \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( x ) ) \in K _ { 0 } \}$ .

Lemma 23. There exists a positive constant c such that it holds with probability at least

$\textstyle 1 - { \frac { c } { n ^ { 2 } } }$ that

$$
\begin{array} { r } { y = \widehat { Q } ( { \boldsymbol x } ) : { \boldsymbol x } \in \mathcal { M } ^ { * } \cap K _ { 1 / 4 } ; \widehat { G } ( \widehat { Q } ( { \boldsymbol x } ) ) \in K _ { 0 } \} = \{ y = \widehat { Q } ( { \boldsymbol x } ) : { \boldsymbol x } \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( { \boldsymbol x } ) ) \in K _ { 0 } \} . } \end{array}
$$

Recall

$$
\bar { \nu } _ { \widehat { Q } } ( y ) = \frac { 1 } { h ^ { d } \vert I _ { 2 } \vert } \sum _ { i \in I _ { 2 } } \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { j } ( X _ { i } ) - y _ { j } } { h } \Big ) \Big ) \cdot \mathbf { 1 } _ { X _ { i } \in K _ { 1 / 4 } } .
$$

where $h = \left( { \textstyle { \frac { \log n } { n } } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ . The next lemma shows that with high probability, for any $y \in \widehat { \Omega }$ , $\bar { \nu } _ { \widehat { Q } } ( y )$ is close to $\mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \cdot \nu ^ { * } ( \widehat { l } ^ { - 1 } ( y ) ) \cdot | \mathrm { d e t } ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( y ) ) |$ .

Lemma 24. There exists a positive constant c such that it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 2 } } }$ that for any $y \in \widehat { \Omega }$ ,

$$
\left| \bar { \nu } _ { \widehat { Q } } ( y ) - \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \cdot \nu ^ { * } ( \widehat { l } ^ { - 1 } ( y ) ) \cdot \big | \mathrm { d e t } \big ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( y ) ) \big | \right| \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha } { 2 \alpha + d } } .
$$

Then by Lemma 24, it holds with probability at least $1 - { \frac { c } { n ^ { 2 } } }$

$$
\begin{array} { r l } & { \underset { \stackrel { \leq } { \ell } \subset \mathcal { C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \left| \int _ { \widehat { \Omega } } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \bar { \nu } _ { \widehat { Q } } ( y ) \mathrm { d } y - \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \int _ { \widehat { \Omega } } \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) \nu ^ { * } ( \widehat { l } ^ { - 1 } ( y ) ) | \mathrm { d e t } ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( y ) ) | \right. } \\ & { \left. \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha } { 2 \alpha + d } } \underset { f \in { \cal C } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \int _ { \widehat { \Omega } } | \Pi _ { J } ^ { \perp } f ( \widehat { G } ( y ) ) | \mathrm { d } y \right. } \\ & { \leq C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } . } \end{array}
$$

We can then obtain the desired result by putting all pieces together.

# F.3.4 Proof of Lemma 22

Let $\begin{array} { r } { \widetilde { \epsilon } _ { n } = a \left( \frac { 1 } { \widehat { p } _ { 0 } } \cdot \frac { \log n } { n } \right) ^ { \frac { 1 } { d } } } \end{array}$ . By Bernstein’s inequality, we have it holds with probability at least $1 - n ^ { - 3 }$ b that

$$
\left. \widehat { p } _ { 0 } - \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) \right. \leq C \left( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \sqrt { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } \right) \leq C _ { 1 } \sqrt { \frac { \log n } { n } } \sqrt { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } ,
$$

where the last inequality is due to $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ log n . So we have

$$
\Big | \frac { \widehat { p _ { 0 } } } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } - 1 \Big | \leq C _ { 1 } \frac { \sqrt { \frac { \log n } { n } } } { \sqrt { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } } \leq C _ { 2 } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 4 } } .
$$

So when $n$ is large enough, we have it holds with probability larger than $1 - n ^ { - 3 }$ that $\begin{array} { r } { \widetilde { \epsilon } _ { n } = a \big ( \frac { 1 } { \widehat { p } _ { 0 } } \cdot \frac { \log n } { n } \big ) ^ { \frac { 1 } { d } } \ge \frac { 1 } { 2 } a \big ( \frac { 1 } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } \cdot \frac { \log n } { n } \big ) ^ { \frac { 1 } { d } } = \epsilon _ { n } } \end{array}$ . Let $\bar { N } _ { \epsilon _ { n } } \subset \mathcal { M } ^ { * } \cap K _ { 1 / 4 }$ be the minimal $\epsilon _ { n }$ b-covering set of $\mathcal { M } ^ { \ast } \cap K _ { 1 / 4 }$ , then $| \bar { N } _ { \epsilon _ { n } } | \le C n$ . Moreover, for any $\widetilde { x } \in \bar { N } _ { \epsilon _ { n } }$ , since there

exist positive constants $c , c _ { 1 }$ such that

$$
\begin{array} { r } { \Xi ^ { * } : \| z - Q ^ { * } ( \widetilde { x } ) \| \le c \epsilon _ { n } \} \subset \{ z \in \Omega ^ { * } : \| G ^ { * } ( z ) - \widetilde { x } \| \le \epsilon _ { n } \} \subset \{ z \in \Omega ^ { * } : \| z - Q ^ { * } ( \widetilde { x } ) \| \le \epsilon _ { n } \} . } \end{array}
$$

it holds that

$$
I \frac { \mathbb { P } _ { \mu ^ { * } } ( \widetilde { K } ) } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } \cdot \frac { \log n } { n } \ge \mathbb { P } _ { \mu ^ { * } } ( \widetilde { K } ) \int _ { \{ z \in \Omega ^ { * } : \| G ^ { * } ( z ) - \widetilde { x } \| \le \epsilon _ { n } \} } \nu ^ { * } ( z ) \mathrm { d } z = \mathbb { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon _ { n } } ( \widetilde { x } ) ) \ge C _ { 1 } a ^ { d } \frac { \mathbb { P } _ { \mu ^ { * } } ( \widetilde { K } ) } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } , \epsilon _ { n } ) } \mathrm { d } \Omega ,
$$

Then by Bernstein’s inequality, it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 3 } } }$ that

$$
\bigg | \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \mathbf { 1 } _ { \mathbb { B } _ { \epsilon _ { n } } ( \widetilde { x } ) } ( X _ { i } ) - \mathbb { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon _ { n } } ( \widetilde { x } ) ) \bigg | \leq C \left( 1 + a ^ { \frac { d } { 2 } } \sqrt { \frac { \mathbb { P } _ { \mu ^ { * } } ( \widetilde { K } ) } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) } } \right) \frac { \log n } { n } .
$$

Therefore when $a$ is large enough, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\widetilde x \in N _ { \epsilon _ { n } }$ ,

$$
\frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \mathbf { 1 } _ { \mathbb { B } _ { \epsilon _ { n } } ( \widetilde { x } ) } ( X _ { i } ) \geq \frac { 1 } { n } .
$$

So

$$
\operatorname* { s u p } _ { x \in \mathcal { M } ^ { * } \cap K _ { 1 / 4 } } \operatorname* { m i n } _ { i \in I _ { 2 } } \lVert x - X _ { i } \rVert _ { 2 } \leq \epsilon _ { n } + \ \operatorname* { s u p } _ { x \in \bar { N } _ { \epsilon _ { n } } } \operatorname* { m i n } _ { i \in I _ { 2 } } \lVert x - X _ { i } \rVert _ { 2 } \leq 2 \epsilon _ { n } \leq 2 \widetilde { \epsilon } _ { n } .
$$

Proof is completed.

# F.3.5 Proof of Lemma 23

Firstly by Lemma 22, it holds that

$$
\{ y = \widehat { Q } ( \boldsymbol { x } ) : \boldsymbol { x } \in \mathcal { M } ^ { * } \cap K _ { 1 / 4 } ; \widehat { G } ( \widehat { Q } ( \boldsymbol { x } ) ) \in K _ { 0 } \} \subset \{ y = \widehat { Q } ( \boldsymbol { x } ) : \boldsymbol { x } \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( \boldsymbol { x } ) ) \in K _ { 0 } \}
$$

For the inverse side, Recall (56), it holds with probability at least $1 - n ^ { - 3 }$ that for any $x \in { \widehat { U } }$ such that $\widehat { G } ( \widehat { Q } ( x ) ) \ \in \ K _ { 0 }$ , there exists $i ^ { * } \in I _ { 2 }$ such that $X _ { i ^ { * } } ~ \in ~ K _ { 1 / 4 }$ , $\begin{array} { r } { \| x - X _ { i ^ { * } } \| _ { 2 } \leq C ( \frac { \log n } { n } ) ^ { \frac { 1 } { 2 d } } } \end{array}$ (recall $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( K _ { 0 } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } ) } \end{array}$ and $\begin{array} { r } { \| \widehat { Q } ( x ) - \widehat { Q } ( X _ { i ^ { * } } ) \| _ { 2 } \leq C _ { 1 } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 d } } } \end{array}$ Moreover, since ${ \widehat { G } } ( { \widehat { Q } } ( x ) ) \in K _ { 0 }$ , by equation (54), it holds with probability at least $1 - n ^ { - 2 }$ that ${ \widehat { G } } ( { \widehat { Q } } ( X _ { i ^ { * } } ) ) , X _ { i ^ { * } } \in K _ { c ( { \frac { \log n } { n } } ) ^ { \frac { 1 } { 2 d } } }$ for a constant $c$ .

Then fix $\boldsymbol { y } \in \mathbb { R } ^ { d }$ and $i \in [ n ]$ where $\| y - { \widehat { Q } } ( X _ { i } ) \| _ { 2 } \leq C _ { 1 } ( { \frac { \log n } { n } } ) ^ { \frac { 1 } { 2 d } }$ and $X _ { i } \in K _ { c ( \frac { \log n } { n } ) ^ { \frac { 1 } { 2 d } } } .$ Define $z ^ { ( 0 ) } = Q ^ { * } ( X _ { i } )$ and recursively define $z ^ { ( k ) } = z ^ { ( k - 1 ) } + \mathbf { J } _ { \hat { l } } ( z ^ { ( k - 1 ) } ) ^ { - 1 } \big ( y - \widehat { l } \big ( z ^ { ( k - 1 ) } \big ) \big )$ (recall $\widehat { l } = \widehat { Q } \circ G ^ { \ast }$ ). Since $\beta > 1$ and for any $z \in Q ^ { * } ( \mathcal { M } ^ { * } \cap K _ { 1 / 2 } )$ , it holds that $\vert \mathrm { d e t } ( \mathbf { J } _ { \hat { l } } ( z ) ) \vert \geq c _ { 2 } > 0$ , we can obtain that when $n$ is large enough, there exists $z$ such that $\begin{array} { r } { \operatorname* { l i m } _ { k \to + \infty } z ^ { ( k ) } = \bar { z } } \end{array}$ and $\begin{array} { r } { \| \bar { z } - z ^ { ( 0 ) } \| \le C _ { 2 } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 d } } } \end{array}$ . So $y = \widehat { Q } ( \bar { x } )$ where $\bar { x } = G ^ { * } ( \bar { z } )$ . Moreover, since $G ^ { * } \big ( z ^ { ( 0 ) } \big ) =$ $X _ { i } \in K _ { c ( \frac { \log n } { n } ) ^ { \frac { 1 } { 2 d } } }$ Kc( log n ) 12d , we have x¯ = G∗(z¯) ∈ K 14 ; also since z(0) ∈ Ω∗ with G∗(z(0)) ∈ K1, we have $\bar { z } \in \bigcup _ { z \in \Omega ^ { * } , G ^ { * } ( z ) \in K _ { 1 } } B _ { 1 / L } ( z ) \subset \Omega ^ { * }$ and thus $\bar { x } \in G ^ { * } ( \Omega ^ { * } ) = { \mathcal { M } } ^ { * }$ , which together leads to $\bar { x } \in \mathcal { M } ^ { * } \cap K _ { \frac { 1 } { 4 } }$ . Therefore we can get it holds with probability at least $\textstyle 1 - { \frac { 2 } { n ^ { 2 } } }$ that { $\begin{array} { r } { y = \widehat { Q } ( { \boldsymbol x } ) : { \boldsymbol x } \in \mathcal { M } ^ { * } \cap K _ { 1 / 4 } ; \widehat { G } ( \widehat { Q } ( { \boldsymbol x } ) ) \in K _ { 0 } \} = \{ y = \widehat { Q } ( { \boldsymbol x } ) : { \boldsymbol x } \in \widehat { U } ; \widehat { G } ( \widehat { Q } ( { \boldsymbol x } ) ) \in K _ { 0 } \} . } \end{array}$

# F.3.6 Proof of Lemma 24

Firstly by equation (54), there exists a positive constant $c$ such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\widetilde { y } \in \widehat { \Omega }$ , there exists $\widetilde { z } \in \Omega ^ { * }$ such that $\widetilde { y } = \widehat { Q } ( G ^ { * } ( \widetilde { z } ) ) = \widehat { l } ( \widetilde { z } )$ and G∗(z) ∈ K $G ^ { * } ( \widetilde { z } ) \in K _ { c ( \frac { \log n } { n } ) ^ { \frac { \beta } { 2 d } } }$ (recall $\widetilde { n } \geq \frac { 1 } { 2 } \sqrt { n \log n } \big )$ . Therefore, fix $\widetilde { y } \in \widehat { \Omega }$ and $y \in \mathbb { B } _ { \sqrt { d } h } ( \widetilde { y } )$ , define $z ^ { ( 0 ) } = \widetilde { z }$ and recursively define $z ^ { ( k ) } = z ^ { ( k - 1 ) } + \mathbf { J } _ { \hat { l } } ( z ^ { ( k - 1 ) } ) ^ { - 1 } ( y - \widehat { l } ( z ^ { ( k - 1 ) } ) )$ . Since $\beta > 1$ and for any $z \in Q ^ { * } ( \mathcal { M } ^ { * } \cap K _ { 1 / 2 } )$ , it holds that $| \mathrm { d e t } ( \mathbf { J } _ { \hat { l } } ( z ) ) | \geq c _ { 2 } > 0$ , when $n$ is large enough, we can get there exists $\bar { z }$ such that $\begin{array} { r } { \operatorname* { l i m } _ { k \to + \infty } z ^ { ( k ) } = \bar { z } } \end{array}$ , $\widehat { l } ( \bar { z } ) = y$ and $\begin{array} { r } { \| \bar { z } - z ^ { ( 0 ) } \| \leq C h \leq C _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { 2 \alpha + d } } } \end{array}$ . So when $n$ is large enough, $\bar { z } \in \Omega ^ { * }$ and $G ^ { * } ( \bar { z } ) \in K _ { \frac { 1 } { 4 } }$ , which further leads to $\{ y \in \mathbb { B } _ { \sqrt { d } h } ( \widetilde { y } ) : \widetilde { y } \in \widehat { \Omega } \} \subset \widehat { Q } ( \mathcal { M } ^ { * } \cap K _ { 1 / 4 } )$ . Therefore, it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 2 } } }$ that for any $\widetilde { y } \in \widehat { \Omega }$ ,

$$
\begin{array} { l } { \mathbb { E } _ { \mu ^ { * } } [ \displaystyle \frac { 1 } { h ^ { d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \displaystyle \frac { \widehat { Q } _ { j } ( X ) - \widehat { y } _ { j } } { h } \Big ) \Big ) \cdot \mathbf { 1 } _ { { \cal F } _ { 1 } / 4 } ( X ) ] - \mathbb { E } _ { \mu ^ { * } } \big ( X \in \widetilde { K } \big ) \cdot \nu ^ { * } ( \widehat { l } ^ { - 1 } ( \widetilde { g } ) ) \cdot \big | \operatorname* { d e t } ( \mathbb { J } _ { \tilde { l } ^ { - 1 } } ( \widehat { y } ) ) } \\ { \overset { ( i i ) } { \leq } \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { K } \big ) | \displaystyle \int \frac { 1 } { h ^ { d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \displaystyle \frac { \widehat { l } _ { j } ^ { * } - \widehat { y } _ { j } } { h } \Big ) \Big ) \cdot \nu ^ { * } ( \widehat { l } ^ { - 1 } ( g ) ) \cdot \big | \operatorname* { d e t } ( \mathbf { J } _ { \tilde { l } ^ { - 1 } } ( z ) ) \big | \mathrm { d } z - \nu ^ { * } ( \widehat { l } ^ { - 1 } ( \widetilde { y } ) ) \cdot | \mathrm { d } } \\ { \overset { ( i i ) } { = } \mathbb { P } _ { \mu ^ { * } } \big ( X \in \widetilde { K } \big ) \displaystyle \Big | \int \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ( t _ { j } ) \Big ) \cdot \big ( \nu ^ { * } ( h t + \widetilde { g } ) - v ^ { * } ( \widetilde { y } ) \big ) \mathrm { d } t \Big | } \\  \overset { ( i i ) } { \leq } \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \Big | \displaystyle \int \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ( t _ { j } ) \Big ) \cdot \displaystyle \sum _ { \tau \in \mathbb { N } ^ { * } } \ \end{array}
$$

where $( i )$ uses $\{ y \in \mathbb { B } _ { \sqrt { d } h } ( \widetilde { y } ) \ : \ \widetilde { y } \in \widehat { \Omega } \} \subset \widehat { Q } ( \mathcal { M } ^ { * } \cap K _ { 1 / 4 } )$ and $\mu ^ { * } | _ { \widetilde K } = G _ { \# } ^ { * } \nu ^ { * }$ ; $( i i )$ let $t = ( t _ { 1 } , t _ { 2 } , \cdot \cdot \cdot , t _ { d } )$ with $\begin{array} { r } { t _ { j } = \frac { z _ { j } - \widetilde { y } _ { j } } { h } } \end{array}$ , $\nu ^ { \circ } ( z ) = \nu ^ { \ast } ( \widehat { l } ^ { - 1 } ( z ) ) \cdot | \mathrm { d e t } ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( z ) ) |$ and uses the fact $\textstyle \int k ( t ) \mathrm { d } t = 1$ ; $( i i i )$ uses $\nu ^ { \circ }$ is $\alpha$ -smooth and $\bar { k }$ is compactly supported; $( i i i i )$ uses $\begin{array} { r l } { \int { x ^ { j } k ( x ) = } } \end{array}$ $0$ for $j \in [ [ \alpha ] ]$ .

Moreover, for any $\widetilde { y } \in \widehat { \Omega }$ ,

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { h ^ { 2 d } } \int \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ^ { 2 } \Big ( \frac { \widehat Q _ { j } ( X ) - \widetilde y _ { j } } h \Big ) \Big ) \cdot \mathbf { 1 } _ { K _ { 1 / 4 } } ( X ) \mathrm { d } \mu ^ { * } } \\ & { = \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde K ) \displaystyle \int _ { z \in \mathbb { B } _ { \sqrt { d h } } ( \widetilde y ) } \displaystyle \frac { 1 } { h ^ { 2 d } } \Big ( \displaystyle \prod _ { j = 1 } ^ { d } \bar { k } ^ { 2 } \big ( \frac { z _ { j } - \widetilde y _ { j } } h \big ) \Big ) \cdot \nu ^ { * } ( \widehat l ^ { - 1 } ( z ) ) \cdot | \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( z ) ) | \mathrm { d } z } \\ & { \le C \displaystyle \frac 1 { h ^ { d } } , } \end{array}
$$

and

$$
\frac { 1 } { h ^ { d } } \cdot \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \big ( \frac { \widehat { Q } _ { j } ( X ) - \widetilde { y } _ { j } } { h } \big ) \Big ) \cdot { \mathbf { 1 } } _ { K _ { 1 / 4 } } ( X ) \leq C \frac { 1 } { h ^ { d } } .
$$

Now let $N _ { \frac { 1 } { n ^ { 2 } } } \subset \widehat { \Omega }$ be a $\textstyle { \frac { 1 } { n ^ { 2 } } }$ -covering set $\widehat { \Omega }$ , where $| N _ { \frac { 1 } { n ^ { 2 } } } | \leq C n ^ { 2 d }$ , then by a similar union bound argument plus Bernstein’s inequality as the proof of (43), it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any y ∈ N 1 , it satisfies that

$$
| \mathbb { E } _ { \mu ^ { * } } [ \frac { 1 } { h ^ { d } } \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { j } ( X ) - \widetilde { y } _ { j } } { h } \Big ) ) \cdot \mathbf { 1 } _ { K _ { 1 / 4 } } ( X ) ] - \bar { \nu } _ { \widehat { Q } } ( \widetilde { y } ) | \leq \sqrt { \frac { \log n } { n } } h ^ { - \frac { d } { 2 } } + \frac { \log n } { n } h ^ { - d } .
$$

Then by the uniformly Lipschitzness of $\bar { k } ( x )$ and $h = \left( { \textstyle { \frac { \log n } { n } } } \right) ^ { \frac { 1 } { 2 \alpha + d } }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $y \in \widehat { \Omega }$ ,

$$
\left| \mathbb { E } _ { \mu ^ { * } } \left[ \frac { 1 } { h ^ { d } } \Big ( \prod _ { j = 1 } ^ { d } \bar { k } \Big ( \frac { \widehat { Q } _ { j } ( X ) - y _ { j } } { h } \Big ) \Big ) \cdot \mathbf { 1 } _ { K _ { 1 / 4 } } ( X ) \right] - \bar { \nu } _ { \widehat { Q } } ( y ) \right| \leq C \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha } { 2 \alpha + d } } .
$$

Then by combining all pieces, we have

$$
\operatorname* { s u p } _ { y \in \widehat { \Omega } } \left| \mathbb { P } _ { \mu ^ { * } } ( X \in \widetilde { K } ) \cdot \nu ^ { * } ( \widehat { l } ^ { - 1 } ( y ) ) \cdot | \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l } ^ { - 1 } } ( y ) ) | - \bar { \nu } _ { \widehat { Q } } ( y ) \right| \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \alpha } { 2 \alpha + d } } .
$$

# F.4 Noisy case

Corollary 3. Suppose $\mu ^ { \ast } ~ \in ~ S ^ { \ast }$ , $X _ { 1 : n }$ and $\epsilon _ { 1 : n }$ are n i.i.d. samples from $\mu ^ { * }$ and $\mu _ { \epsilon }$ respectively, where $\mathbb { P } _ { \mu _ { \epsilon } } ( \| \epsilon \| _ { 2 } \le n ^ { - \frac { 1 } { 2 } - \frac { \beta } { d } } ) = 1$ . Let $Y _ { i } = X _ { i } + \epsilon _ { i }$ for any $i \in [ n ]$ . If $D > d$ , $\gamma > 0$ , $\alpha \geq 0$ and $\beta > 1$ , Use $\widehat { \mu } ^ { \circ }$ to denote the estimator $\widehat { \mu }$ defined in Section 3.1 with $X _ { 1 : n }$ being replaced by $Y _ { 1 : n }$ , then there exist positive constants $c _ { 1 }$ and $n _ { 0 }$ such that when $n \geq n _ { 0 }$ it holds that

$$
\mathbb { E } [ d _ { \gamma } ( \widehat { \mu } ^ { \circ } , \mu ^ { * } ) ] \leq C \Big ( \big ( \frac { \log n } { n } \big ) ^ { \frac { \gamma \beta } { d } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { \alpha + \gamma } { 2 \alpha + d } } \vee \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 } } \Big ) .
$$

Proof. Recall $S _ { m } = \mathbb { B } _ { r _ { m } } ( a _ { m } ) \subset \mathbb { B } _ { r _ { m } + 0 . 5 / L } ( a _ { m } ) = S _ { m } ^ { \dagger } \subset \mathbb { B } _ { r _ { m } + 1 / L } ( a _ { m } ) \subset \bar { S } _ { n }$ , then when $n$ is large enough, $\mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ) \leq \mathbb { P } _ { \mu ^ { * } * \mu _ { \epsilon } } ( Y \in S _ { m } ^ { \dagger } ) \leq \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } )$ . Similar as the proof for Theorem 2 in Appendix D.2, we fix an arbitrary $m \in [ M ]$ where $\begin{array} { r } { \mathbb { P } _ { \mu ^ { * } } ( X \in S _ { m } ^ { \dagger } ) \geq \frac { 1 } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ and bound $\begin{array} { r } { \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \big ( \int f ( X ) \rho _ { m } ( X ) \mathrm { d } \mu ^ { * } - \widehat { \mathcal { I } } _ { m } ( f , Y _ { 1 : n } ) \big ) } \end{array}$ in the following proof. Use (Gb[m], Qb[m], νe[m],Qb[m] ) to denote estimators $( \widehat { G } _ { [ m ] } , \widehat { Q } _ { [ m ] } , \widetilde { \nu } _ { [ m ] , \widehat { Q } _ { [ m ] } } )$ with $X _ { 1 : n }$ being replaced by Y1:n, and here we consider ν[m],Q[m] constructed by wavelet expansion with $\gamma \vee \alpha$ -smooth basis. Since there exists a constant $c _ { 2 }$ such that

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| Y _ { i } - \widehat { G } _ { [ m ] } ^ { \circ } ( \widehat { Q } _ { [ m ] } ^ { \circ } ( Y _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { S _ { m } ^ { \dag } } ( Y _ { i } ) \leq \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| Y _ { i } - G _ { [ m ] } ^ { \ast } ( Q _ { [ m ] } ^ { \ast } ( Y _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { S _ { m } ^ { \dag } } ( Y _ { i } ) } & { } \\ { \leq c \left( \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| X _ { i } - G _ { [ m ] } ^ { \ast } ( Q _ { [ m ] } ^ { \ast } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \widetilde { S } _ { m } } ( X _ { i } ) ) \right) } & { } \\ { \leq c _ { 2 } n ^ { - 1 - \frac { 2 \beta } { d } } ; } \end{array}
$$

and when $r$ is small enough, for any $\begin{array} { r } { \widetilde { z } \in \{ z \in \mathbb { B } _ { 1 } ^ { d } : G ^ { * } ( z ) \in \mathbb { B } _ { r _ { m } + 0 . 2 5 / L } ( a _ { m } ) \} _ { \mathrm { : } } } \end{array}$

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| X _ { i } - \widehat { G } _ { [ m ] } ^ { \diamond } ( \widehat { Q } _ { [ m ] } ^ { \diamond } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { r } ( \widetilde { z } ) } ( Q ^ { * } ( X _ { i } ) ) \cdot \mathbf { 1 } _ { S _ { m } ^ { \dagger } } ( X _ { i } ) } \\ & { \leq \displaystyle \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \| X _ { i } - \widehat { G } _ { [ m ] } ^ { \diamond } ( \widehat { Q } _ { [ m ] } ^ { \diamond } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { S _ { m } ^ { \dagger } } ( Y _ { i } ) \leq c _ { 2 } n ^ { - 1 - \frac { 2 \beta } { d } } . } \end{array}
$$

Then same as the proof of Lemma 7 and 11, we can get it holds with probability at least 1 − n−c that the density of ν∗[m],Q belongs to $C _ { c _ { 3 } } ^ { \alpha } ( \mathbb { R } ^ { d } )$ ; and for any $\eta \in [ 4 | \gamma ] ]$ , $\begin{array} { r } { \mathbb { E } _ { \mu ^ { * } } \bigl [ \| X - \widehat { G } _ { [ m ] } ^ { \diamond } ( \widehat { Q } _ { [ m ] } ^ { \diamond } ( X ) ) \| _ { 2 } ^ { \eta } \cdot \rho _ { m } ( X ) \bigr ] \leq c _ { 3 } \bigl ( \bigl ( \frac { \log n } { n } \bigr ) ^ { \frac { \eta \beta } { d } } \vee \frac { \log n } { n } \bigr ) } \end{array}$ ; So same as the proof Lemma 6, it holds with probability at least $1 - n ^ { - c }$ that

$$
\begin{array} { r l } & { \quad \times \underset { \{ t \} } { \mathrm { s u p } } ( \int \Big ( \int \hat { I } ( X ; W _ { m } , X ; \hat { X } ; \hat { t } , \hat { w } ^ { t } ) } \\ & { \quad + \underset { \mathbb { R } ^ { 2 } } { \mathrm { s u p } } ( X , \hat { X } ; \hat { t } , \hat { W } ^ { t } ) \Big ) } \\ & { \quad - \underset { \{ t \} } { \mathrm { s u p } } ( X ; \hat { X } ; \hat { t } , \hat { W } ^ { t } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( \hat { W } ; \hat { t } , \hat { W } ^ { t } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( \hat { W } ; \hat { t } , \hat { W } ^ { t } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { X } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; X ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { X } ) } \\ & { \quad \leq C \underset { \{ t \} } { \mathrm { s u p } } ( X ; \hat { t } , \hat { W } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { t } , \hat { X } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { t } , \hat { W } ^ { t } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { X } ; \hat { W } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { X } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u b } } ( X ; \hat { X } ) } \\ &  \quad - \underset { \{ t \} } { \mathrm { s u p } } ( X ; \hat { t } , \hat { W } ^ { t } ) \underset { \{ \hat { W } ^ { t } \} } { \mathrm { s u p } } ( X ; \hat { t } , \end{array}
$$

Now we bound

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { f \in { \mathcal C } _ { 1 } ^ { \gamma } ( { \mathbb R } ^ { D } ) } \Big ( \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \Pi _ { J } f ( \widehat G _ { [ m ] } ^ { \circ } ( \widehat Q _ { [ m ] } ^ { \circ } ( Y _ { i } ) ) ) \rho _ { m } ( Y _ { i } ) + \int \Pi _ { J } ^ { \perp } f ( \widehat G _ { [ m ] } ^ { \circ } ( z ) ) \widehat \nu _ { \widehat { Q } _ { [ m ] } ^ { \circ } } ^ { \circ } ( z ) \mathrm { d } z } \\ & { \displaystyle - \int f ( \widehat G _ { [ m ] } ^ { \circ } ( \widehat Q _ { [ m ] } ^ { \circ } ( X ) ) ) \rho _ { m } ( X ) \mathrm { d } \mu ^ { * } \Big ) . } \end{array}
$$

By Lemma 5 and 4, we only need to bound

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big ( \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \Pi _ { J } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( \widehat { Q } _ { [ m ] } ^ { \circ } ( Y _ { i } ) ) ) \rho _ { m } ( Y _ { i } ) } \\ & { \displaystyle - \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \Pi _ { J } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( \widehat { Q } _ { [ m ] } ^ { \circ } ( X _ { i } ) ) ) \rho _ { m } ( X _ { i } ) \Big ) } \\ & { \displaystyle + \ \operatorname* { s u p } _ { f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } ) } \Big ( \int \Pi _ { J } ^ { \perp } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( z ) ) \widehat { \nu } _ { \widehat { Q } _ { [ m ] } ^ { \circ } } ^ { \circ } ( z ) \mathrm { d } z - \int \Pi _ { J } ^ { \perp } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( z ) ) \widehat { \nu } _ { \widehat { Q } _ { [ m ] } ^ { \circ } } ( z ) \mathrm { d } z \Big ) . } \end{array}
$$

Recall

$$
\Pi _ { J } f ( x ) = \sum _ { k \in \mathbb { Z } ^ { D } } b _ { k } \phi _ { k } ( x ) + \sum _ { l = 1 } ^ { 2 ^ { D } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { k \in \mathbb { Z } ^ { D } } f _ { l j k } \psi _ { l j k } ( x ) ,
$$

where $2 ^ { d J } = C n ^ { \frac { d } { 2 \alpha + d } }$ . By the fact that the basis $\phi _ { k }$ and $\psi _ { l j k }$ are $\gamma$ -smooth, there exists a constant $c$ such that for any $f \in C _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ , it holds that $\Pi _ { J } f \in C _ { c \log n } ^ { \gamma } ( \mathbb { R } ^ { D } )$ and $\Pi _ { J } ^ { \perp } f \in C _ { c \log n } ^ { \gamma } ( \mathbb R ^ { D } )$ . So it holds that

$$
\begin{array} { r l } & { \underset { f \in C _ { 1 } ^ { \widehat { \Upsilon } } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big ( \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } \Pi _ { J } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( \widehat { Q } _ { [ m ] } ^ { \circ } ( Y _ { i } ) ) ) \rho _ { m } ( Y _ { i } ) } \\ & { - \frac { 1 } { | I _ { 2 } | } \displaystyle \sum _ { i \in I _ { 2 } } \Pi _ { J } f ( \widehat { G } _ { [ m ] } ^ { \circ } ( \widehat { Q } _ { [ m ] } ^ { \circ } ( X _ { i } ) ) ) \rho _ { m } ( X _ { i } ) \Big ) \leq C n ^ { - ( \frac { 1 } { 2 } + \frac { \beta } { d } ) \cdot ( \gamma \wedge 1 ) } \cdot \log n ; } \end{array}
$$

$$
\begin{array} { r l } & { \quad \underset { \leq \ell \in \mathcal { T } ( \mathbb { R } ) } { \operatorname* { s u p } } \underset { n \leq i \leq i \leq n } { \operatorname* { s u p } } \bigg ( \int \prod _ { j \in \mathcal { E } _ { \mathrm { i n } } ( \cdot \xi ) } \widehat { \mathcal { P } } _ { \xi _ { \eta \mathrm { i n } } } ^ { \xi } ( \xi ) d z \bigg ) \leq \int \prod _ { j \in \mathcal { E } _ { \mathrm { i n } } ( \cdot \xi ) } ^ { 1 1 } \widehat { \mathcal { P } } _ { \xi _ { \eta \mathrm { i n } } } ( \xi ) \widehat { \mathcal { P } } _ { \xi _ { \xi \mathrm { i n } } } ( \xi ) \mathrm { d } \xi \bigg ) } \\ & { \leq \mathcal { L } \mathcal { L } \log n - \underset { \phi \in \mathcal { T } ^ { \prime } ( \mathbb { R } ) } { \operatorname* { s u p } } \Bigg ( \int \big ( | \widehat { \mathcal { E } } _ { \xi \mathrm { i n } } ( \xi ) | ^ { 2 } \big _ { \phi _ { \phi \mathrm { i n } } } ( z ) \big | | z - \int \big | \widehat { \mathcal { L } } ( \xi ) \widehat { \mathcal { P } } _ { \phi \mathrm { i n } } ( z ) \big | | z \big ) \Bigg ) } \\ & { \qquad \times \mathcal { L } \mathcal { L } \mathcal { L } _ { \phi \mathrm { i n } } \Bigg ( \underset { \phi \in \mathcal { T } ^ { \prime } ( \cdot \phi ) } { \operatorname* { s u p } } \Bigg ) \underset { \leq \ell \leq i \leq n } { \operatorname* { s u p } } \int \bigg ( \underset { \delta \in \mathcal { E } _ { \phi \mathrm { i n } } ( \cdot \xi ) } { \sum } \bigg ) = \underset { \xi = 1 } { \overset { \alpha , 1 , \dots , \xi } { \sum } } \sum _ { j \in \mathrm { i n } \leq i \leq n } \int _ { \phi \in \mathcal { E } _ { \phi \mathrm { i n } } ( \cdot \xi ) } \Big ( \widehat { \mathcal { P } } _ { \xi \mathrm { i n } } ^ { \xi } ( z ) - \widehat { \mathcal { P } } _ { \xi \mathrm { i n } } ^ { \xi } \Big ) } \\ &  \end{array}
$$

where the last inequality uses the fact that $\phi _ { k } ( \cdot )$ and $\psi _ { l j k } ( \cdot )$ are $\gamma$ -smooth. Then similar as the proof of Theorem 2, we can get the desired conclusion.