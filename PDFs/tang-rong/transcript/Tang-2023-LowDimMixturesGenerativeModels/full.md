# Estimating Distributions with Low-dimensional Structures Using Mixtures of Generative Models

Rong Tang and Yun Yang

University of Illinois Urbana Champaign

# Abstract

There has been a growing interest in statistical inference from data satisfying the so-called manifold hypothesis, assuming data points in the high-dimensional ambient space to lie in close vicinity of a submanifold of much lower dimension. In machine learning, encoder-decoder pair based generative modelling approaches have been successful in learning complicated high-dimensional distributions such as those over images and texts by explicitly imposing the low-dimensional manifold structure. In this work, we introduce a new approach for estimating distributions on unknown submanifolds via mixtures of generative models. We show that conventional generative modeling approaches using a single encoder-decoder pair are generally unable to capture data distributions under the manifold hypothesis, unless the underlying manifold admits a global parametrization; however, this issue can be solved by using a collection of encoder-decoder pairs for learning different local patches of the data supporting manifold. A rigorous theoretical analysis is developed to demonstrate that the proposed estimator attains the minimax-optimal rate of convergence for the implicit estimation of data distributions with manifold structures. Our experiments show that, by utilizing parameter sharing, the proposed method can significantly improve the performance of conventional auto-encoder based generative modelling approaches with minimal additional computational efforts.

Keywords: Autoencoder; distribution estimation; generative model; manifold; minimax-rate.

# 1 Introduction

Modelling and estimating complicated high-dimensional distributions with low-dimensional structures remains one of the major challenges in modern statistical learning. Suppose we observe $n$ i.i.d. samples $\{ X _ { 1 } , X _ { 2 } , \ldots , X _ { n } \}$ living in an ambient Euclidean space $\mathbb { R } ^ { D }$ according to some unknown distribution $\mu ^ { * }$ . We wish to estimate $\mu ^ { * }$ based on the samples for conducting statistical inference and generating new samples. One of the most popular nonparametric methods for distribution estimation is kernel density estimation (KDE). It has been shown that when $\mu ^ { * }$ admits a density function relative to the Lebesgue measure of $\mathbb { R } ^ { D }$ , and the density function is $\beta$ -smooth, then KDE can achieve the optimal rate $n ^ { - } ^ { \frac { \beta } { 2 \beta + D } }$ for recovering the density value at any point in $\mathbb { R } ^ { D }$ (Silverman, 2018; Tsybakov, 2009). However, the non-parametric rate $n ^ { - } ^ { \frac { \beta } { 2 \beta + D } }$ suffers from the curse of dimensionality as the ambient dimension $D$ appears in the rate exponent and can be enormous in machine learning applications involving images and texts (Brock et al., 2018; Oord et al., 2016). In order to avoid this exponential blow-up of the dimension, a common practice is to assume some additional structure in the data so that the effective dimension of the data space is relatively low.

One such structure that has attracted much attention recently is the so-called manifold hypothesis, which assumes the date to live on a $d$ -dimensional submanifold $\mathcal { M }$ embedded in the possibly highdimensional ambient space $\mathbb { R } ^ { D }$ . Although submanifolds have more complicated geometry than the conventional Euclidean spaces, the manifold hypothesis is a natural assumption to make in a number of areas of science and technology. For example, in computer vision and medical imaging, data are usually images represented as vectorized pixel intensities. Although images may contain millions of pixels, it is usually determined by a comparatively smaller set of global characteristics such as camera projection, lighting condition, texture, object position and orientation. Other examples of high-dimensional complex data with low-dimensional manifold structures appear in natural language processing (Luo et al., 2020; Ling et al., 2017), protein-protein interaction detection (You et al., 2010; Terradot et al., 2004), and astronomy and shape analysis (Mardia, 1999; Jupp & Mardia, 2009).

Statistical theory and methodology for modeling manifold valued data have been developed in various contexts (Lin et al., 2020, 2017; Zhang et al., 2022; Lan et al., 2021; Divol, 2022; Tang & Yang, 2022; Berenfeld et al., 2022). Specifically, the problem of estimating a probability measure lying on an unknown low-dimensional Riemannian submanifold has been studied in a number of recent works. For example, Divol (2022) consider a kernel density type estimator based on a preliminary step of estimating the volume measure of the submanifold using local polynomial estimation techniques. They prove that the developed estimator can achieve the minimax-optimal error bound under the Wasserstein loss. Tang & Yang (2022) construct a two-step estimator: the first step estimates the data supporting submanifold; and the second step recovers the distribution on the estimated submanifold based on wavelet type estimators. They also show that such an estimation is minimax-optimal with respect to certain adversarial loss functions. Berenfeld et al. (2022) develop a Bayesian procedure based on location-scale mixtures of Gaussians for estimating the density of data living close to an unknown submanifold with theoretical guarantees. However, although these existing methods are theoretically appealing, they usually have poor computational scalability with the ambient dimensionality and the sample size, making them costly to implement for modeling massive and high-dimensional real data, such as images and texts.

Auto-encoder based deep generative modeling approaches in the machine learning literature, such as variational auto-encoder (VAE) (Kingma & Welling, 2013; Rezende et al., 2014; Kingma et al., 2016), Wasserstein auto-encoder (WAE) (Tolstikhin et al., 2019), InfoVAE (Zhao et al., 2019) and inferential Wasserstein generative adversarial networks (iWGAN) (Chen et al., 2022), have achieved great successes in generating synthetic realistic-looking images and texts, and are usually very efficient to implement. However, despite their empirical successes, a general theoretical framework explaining whether and how these generative modelling approaches benefit from the low-dimensional manifold structure is lacking, and it is also not clear whether these existing methods are theoretically optimal in the minimax sense. For example, the key step in the auto-encoder is the extraction of $d$ ( $d \ll D$ ) latent features (via an encoder $Q : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ ) that can be used for accurately reconstructing the original data (via a decoder $G : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ ). In other words, these auto-encoder based methods implicitly assume data $X$ to have a low-dimensional structure so that they can be accurately reconstructed in the sense that $X \approx G ( Q ( X ) )$ . Moreover, it is often the case that real-world data falls on a manifold that does not admit a global parametrization. For example, when the data space is a boundaryless manifold such as a sphere, or disconnected (Khayatkhoei et al., 2018). This lack of global parametrization makes conventional autoencoder methods equipped with a single encoder/decoder pair incapable of recovering the entire data space without incurring distortions. Our empirical results (c.f. Fig. 1) also suggest that conventional auto-encoder based generative modelling approaches tend to generate off real-manifold samples with unrealistic appearances.

In this article, we propose a new generative modelling approach for learning manifold-supported distributions that is theoretically minimax-optimal, computationally efficient, and empirically promising in generating complicated yet realistic-looking data. Unlike most existing generative modelling procedures that rely on the strong assumption of the existence of a global parametrization of the data space, we employ multiple encoder/decoder pairs, where each pair corresponds to the parametrization of a local patch of the data supporting manifold. Moreover, we utilize the partition of unity technique for gluing local probability measures estimated in the patches to form a global estimation of the probability measure on the manifold. In addition, most existing methods simply plug in the data empirical distribution in constructing the objective function for defining a GAN (Goodfellow et al., 2014) type estimator, which may lead to theoretical deficiency due to the failure of taking the smoothness of the target distribution into account. We instead propose to plug in a smoothness-regularized version that provably improves the estimation accuracy. Concretely, we show that when the target distribution is $\alpha$ -smooth and lies in a $\beta$ -smooth $d$ -dimensional submanifold in $\mathbb { R } ^ { D }$ , then the corresponding estimator $\widehat { \mu }$ based on $n$ data points achieves a non-asymptotic error bound of order $\begin{array} { r } { O \big ( \frac { \log n } { \sqrt { n } } \vee n ^ { - \frac { \alpha \wedge ( \beta - 1 ) + 1 } { 2 ( \alpha \wedge ( \beta - 1 ) ) + d } } \big ) } \end{array}$ (here $a \wedge b$ denotes $\operatorname* { m i n } \{ a , b \} )$ under the 1-Wasserstein distance, which corresponds to the minimax rate modulo a logarithmic factor when $\alpha \le \beta - 1$ . The implied rate of convergence does not suffer from the “curse of dimensionality” and only depends on the intrinsic dimensionality $d$ of the data. Our numerical results also show that the proposed method tends to be more accurate than conventional auto-encoder based generative modelling approaches and classic kernel density estimators for learning target distributions with low-intrinsic dimensional structures.

# 1.1 Notation

We summarize some necessary notations and definitions here. For any positive integer $k$ , we use the shorthand $[ k ] : = \{ 1 , 2 , \cdots , k \}$ . We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and reserve $\| \cdot \|$ for the $\ell _ { 2 }$ norm. We use $\mathbb { S } _ { 1 } ^ { d } = \left\{ x \in \mathbb { R } ^ { d + 1 } : \left\| x \right\| = 1 \right\}$ to denote the $d$ -dimensional unit sphere in $\mathbb { R } ^ { d + 1 }$ . For a probability measure $\mu$ , we use $\operatorname { s u p p } ( \mu )$ to denote its support. For any measure $\nu$ and map $G$ , the push-forward measure $\mu = G _ { \# } \nu$ is defined as the unique measure such that $\mu ( A ) = \nu ( G ^ { - 1 } ( A ) )$ holds for any measurable set $A$ . For two probability measures $\mu , \nu$ , the 1-Wasserstein distance between $\mu$ and $\nu$ is defined as $W _ { 1 } ( \mu , \nu ) = \operatorname * { i n f } \left\{ \int \| x - T ( x ) \| _ { 1 } \mathrm { d } \mu ( x ) : T _ { \# } \mu = \nu \right\} = \operatorname * { s u p } \left\{ \int f ( x ) \mathrm { d } ( \mu - \nu ) : \mathrm { L i p } ( f ) \leq 1 \right\}$ , where $\operatorname { L i p } ( f )$ denotes the minimal Lipschitz constant for $f$ . When no ambiguity arises, for an absolutely continuous probability measure $\nu$ , we may also use $\nu$ to refer to its density function. We use ${ \mathcal { P } } ( \Omega )$ to denote the set of probability measures on $\Omega$ . We use $\mathbb { B } _ { r } ( x )$ to denote the closed ball centered at $x$ with radius $r$ under the $\ell _ { 2 }$ distance. We use $C _ { r } ^ { \alpha } ( \Omega )$ to denote the set of all $\alpha$ -Hölder smooth functions with Hölder norm $\| \cdot \| _ { C ^ { \alpha } ( \Omega ) }$ being bounded by $r$ (see for example, Evans (2010a)). Similarly, we use $C _ { r } ^ { \alpha } ( \Omega ; \mathbb { R } ^ { D } ) = \{ f = ( f _ { 1 } , \ldots , f _ { D } ) \colon \Omega  \mathbb { R } ^ { D } \big \vert \forall j \in [ D ] ,  .$ $f _ { j } \in C _ { r } ^ { \alpha } ( \Omega ) \}$ to denote the vector valued function space counterpart.

# 1.2 Organization

The rest of the paper is organized as follows. In Section 2, we give a brief introduction to the auto-encoder based generative modelling approaches and define smooth distributions on manifolds. Our proposed model is introduced in Section 3, and its implementation and theoretical properties are described in Section 4 and Section 5, respectively. Simulations and a real data application are provided in Section 6 and Section 7.

# 2 Background

# 2.1 Auto-encoder based generative modelling approaches

Assume i.i.d. data $X ^ { ( n ) } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ sampled from an unknown target distribution $\mu ^ { * }$ over data space $\mathcal { X } \subset \mathbb { R } ^ { D }$ are available. In the literature of generative modelling, the target distribution $\mu ^ { * }$ is implicitly specified by its sampling scheme, represented by a generative model. Mathematically, a generative model is defined as a pair $( \nu _ { 0 } , G )$ , where $\nu _ { 0 }$ is a distribution on a low-dimensional latent space $\mathcal { Z } \subset \mathbb { R } ^ { d }$ , called generative distribution, that is easy to sample from; and $G : { \mathcal { Z } } \to { \mathcal { X } }$ is a map from $\mathcal { L }$ to $\mathcal { X }$ , called generative map, so that if $Z \sim \nu _ { 0 }$ , then $G ( Z ) \sim \mu ^ { * }$ . The goal of generative modelling is to fit a generative model that specifies a stochastic process whose simulated data look indistinguishable from real data. In particular, auto-encoder based generative modelling approaches introduce a family of encoders $Q$ that send the data $X$ to the (low-dimensional) latent variables $Z$ , and a family of decoders $G$ that reconstruct the data from the latent variables, so that they jointly minimizes the following objective:

$$
{ \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } c { \big ( } X _ { i } , G ( Q ( X _ { i } ) ) { \big ) } + { \mathrm { P e n a l t y t e r m } } ,
$$

where $c ( \cdot , \cdot )$ is a cost function. The first component $\scriptstyle n ^ { - 1 } \sum _ { i = 1 } ^ { n } c ( X _ { i } , G ( Q ( X _ { i } ) ) )$ of the objective function corresponds to the reconstruction cost: a common choice is the squared loss $c ( x , y ) = \| x - y \| _ { 2 } ^ { 2 }$ . This reconstruction cost enforces the push-forward measure of $( G \circ Q ) _ { \# } \mu ^ { * }$ to be as close to $\mu ^ { * }$ as possible. On the other hand, the second component involves a penalty term for regularizing the encoder/decoder pair. For example, in VAE (Kingma $\&$ Welling, 2013; Rezende et al., 2014; Kingma et al., 2016), the penalty term is chosen to be an averaged Kullback-Leibler (KL) divergence between the latent variable distribution induced by the (probabilistic) encoder and a prior distribution $\nu _ { 0 }$ ; in iWGAN (Chen et al., 2022), the penalty term is chosen to be an approximation to the 1-Wasserstein distance between the reconstructed data distribution $( G \circ Q ) _ { \# } \mu ^ { * }$ and induced distribution from the generative model $G _ { \# } \nu _ { 0 }$ using prior $\nu _ { 0 }$ . Other approaches choose penalty terms for directly matching the encoder-induced latent variable distribution and a given prior in the latent space (for example, WAE, Tolstikhin et al. (2019); infoVAE, Zhao et al. (2019); Sliced WAE, Kolouri et al. (2018)), which leads to the following training objective:

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } c \bigl ( X _ { i } , G ( Q ( X _ { i } ) ) \bigr ) + \lambda \cdot \mathscr { D } ( Q _ { \# } \widehat { \mu } _ { \mathrm { e m } } , \nu _ { 0 } ) ,
$$

where $\begin{array} { r } { \widehat { \mu } _ { \mathrm { e m } } : = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \delta _ { X _ { i } } } \end{array}$ denotes the discrete empirical distribution of the data $X ^ { ( n ) }$ , and $\mathcal { D }$ is a generic discrepancy metrics characterizing closeness between distributions over the latent space. We will call any method whose training objective takes the form as (1) a latent distribution matched auto-encoder (LDMAE) for future reference. Ideally, the learned decoder $\widehat { G }$ from minimizing (1) has the property that $\widehat { \mu } = \widehat { G } _ { \# } \nu _ { 0 } \approx \mu ^ { * }$ . Comparing with approaches directly dealing with distributions on the ambient space (Goodfellow et al., 2014; Arjovsky et al., 2017; Khayatkhoei et al., 2018), the latent distribution matching schemes bring several computational benefits. First, the choice of $\mathcal { D }$ for quantifying the discrepancy between distributions in the latent space $\mathcal { Z }$ is more flexible since these distributions usually admit a density function relative to the Lebesgue measure over $\mathcal { Z }$ ; in contrast, many commonly used discrepancies metrics such as the total variation distance, the Hellinger distance and the KL divergence are known to be unsuitable for characterizing closeness between nearly singular measures over the ambient space (Li et al., 2017; Xu et al., 2018). Second, computing a discrepancy between distributions in the relatively low-dimensional latent space is much more efficient and does not suffer from the curse of dimensionality, make the training process more stable and less time-consuming. In addition, the extra flexibility of $\mathcal { D }$ allows one to employ those metrics that have simple and explicit computational formulas, such as the squared maximum mean discrepancy (MMD) (Tolstikhin et al., 2019; Zhao et al., 2019) and the sliced Wasserstein distance (Kolouri et al., 2018).

At the end of this subsection, we describe two important limitations of LDMAE, which motivate our proposed method to be introduced in Section 3. Concretely, based on the aforementioned decomposition perspective of the training objective (1), the estimation error of $\widehat { \mu }$ from the target distribution $\mu ^ { * }$ depends on two terms: (1) the “distance” between $\mu ^ { * }$ and $( \widehat G \circ \widehat Q ) _ { \# } \mu ^ { * }$ ; (2) the “distance” between $\widehat { Q } _ { \# } \mu ^ { * }$ and $\nu _ { 0 }$ , where $\widehat { Q }$ denotes the learned encoder from minimizing (1). Let $\mathcal { M }$ denote the support of the true data generating distribution $\mu ^ { * }$ as a $d$ -dimensional submanifold embedded in $\mathbb { R } ^ { D }$ . To control the first distance, one needs $\mathcal { M }$ to have a global parametrization, that is, we can find some continuous maps $G ^ { * } : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ and $Q ^ { * } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ so that for any $x \in \mathcal { M }$ , $G ^ { * } ( Q ^ { * } ( x ) ) = x$ . This global-parametrization condition does not hold for many common manifolds, such as disconnected manifolds and boundaryless manifolds like spheres and torus. The second distance depends on how well the empirical data distribution $\widehat { \mu } _ { \mathrm { e m } }$ induced empirical latent distribution $\widehat { Q } _ { \# } \widehat { \mu } _ { \mathrm { e m } }$ can approximate the population level distribution $\widehat { Q } _ { \# } \mu ^ { * }$ . However, even though we assume that manifold $\mathcal { M }$ admits a global parameterization such that $\mu ^ { * } = G _ { \# } ^ { * } \nu _ { 0 }$ and $Q ^ { * } = ( G ^ { * } ) ^ { - 1 }$ for some $G ^ { * }$ , $Q ^ { * }$ in the decoder and encoder families, the discrete empirical distribution $\widehat { \mu } _ { \mathrm { e m } }$ may suffer from statistical deficiency for approximating a smooth measure (Liang, 2020; Tang & Yang, 2022). As a result, simply plugging-in $Q \# \widehat { \mu } _ { \mathrm { e m } }$ in the penalty term may lead to overfitting.

# 2.2 Partition of unity and distributions on manifolds

Intuitively speaking, a manifold is a topological space that locally resembles the Euclidean space. Formally, we have the following mathematical definition of a manifold.

Definition 1. A $d$ -dimensional manifold $\mathcal { M }$ is defined as a topological space satisfying:(1) There exists an atlas on $\mathcal { M }$ consisting of a collection of $d$ -dimensional charts $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ covering $\mathcal { M }$ , that is, $\begin{array} { r } { \mathcal { M } = \bigcup _ { \lambda \in \Lambda } U _ { \lambda } } \end{array}$ . (2) Each chart $^ { 1 } ( U , \varphi )$ in atlas $\mathcal { A }$ consists of a homeomorphism $\varphi : U \to { \widetilde { U } }$ , called coordinate map, from an open set $U \subset { \mathcal { M } }$ to an open set $\widetilde U \subset \mathbb { R } ^ { d }$ .

We call a manifold $\mathcal { M }$ a ( $\beta$ -smooth) submanifold embedded on $\mathbb { R } ^ { D }$ if $\mathcal { M } \subset \mathbb { R } ^ { D }$ , and the coordinate map $\varphi$ and its inverse $\varphi ^ { - 1 }$ in each chart are $\beta$ -smooth maps when identified as functions defined on subsets of Euclidean spaces. Another useful notion related to the manifold is partition of unity.

efinition 2. A partition of unity of a manifold $\mathcal { M }$ is a collection of functions $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ satisfying 1. $0 \leq \rho _ { \lambda } \leq 1$ for all $\lambda \in \Lambda$ , and $\begin{array} { r } { \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( x ) = 1 } \end{array}$ for all $x \in \mathcal { M }$ .

2. Each point $x \in \mathcal { M }$ has a neighborhood which intersects $\operatorname { s u p p } ( \rho _ { \lambda } )$ for only finitely many $\lambda \in \Lambda$

Using the partition of unity, one can glue constructions in the local charts to form a global construction on the manifold. A partition of unity can be constructed from any open cover $\{ U _ { \lambda } \} _ { \lambda \in \Lambda }$ of the manifold in a way where the partition $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ is indexed over the same set and $\operatorname { s u p p } ( \rho _ { \lambda } ) \subset U _ { \lambda }$ for any $\lambda \in \Lambda$ . Such a partition of unity is said to be subordinate to the open cover $\{ U _ { \lambda } \} _ { \lambda \in \Lambda }$ .

For a manifold $\mathcal { M }$ with atlas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ , suppose $\Lambda$ is finite and we write it as $\Lambda = [ K ]$ Given a partition of unity $\{ \rho _ { k } \} _ { k \in [ K ] }$ subordinate to the open cover $\{ U _ { k } \} _ { k \in [ K ] }$ , one can decompose any distribution $\mu ^ { * }$ on $\mathcal { M }$ as

$$
\mu ^ { * } = \sum _ { k \in [ K ] } \rho _ { k } \mu ^ { * } = \sum _ { k \in [ K ] } ( \varphi _ { k } ^ { - 1 } ) _ { \# } \bigl [ ( \varphi _ { k } ) _ { \# } ( \rho _ { k } \mu ^ { * } ) \bigr ] ,
$$

where the first inequality uses $\begin{array} { r } { \sum _ { k \in [ K ] } \rho _ { k } ( x ) = 1 } \end{array}$ for all $x \in \mathcal { M }$ , and the second inequality uses the fact that $\operatorname { s u p p } ( \rho _ { k } ) \subset U _ { k }$ and $\varphi _ { k }$ is a homeomorphism on $U _ { k } \to \varphi _ { k } ( U _ { k } )$ .2 Then if we write $\begin{array} { r } { \nu _ { k } ^ { * } = ( \varphi _ { k } ) _ { \# } \big ( \frac { \rho _ { k } \mu ^ { * } } { \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ] } \big ) } \end{array}$ $\mu ^ { * }$ can be expressed as the following (mixture of) generative models:

$$
\mu ^ { * } = \sum _ { k \in \left[ K \right] } \mathbb { E } _ { \mu ^ { * } } \left[ \rho _ { k } \right] \cdot ( \varphi _ { k } ^ { - 1 } ) _ { \# } \nu _ { k } ^ { * } ,
$$

Decomposition (3) suggests that any distribution $\mu ^ { * }$ lying on a $d$ -dimensional submanifold embedded on $\mathbb { R } ^ { D }$ whose atlas composed of at most $K$ -number of charts belongs to the following mixture of generative models class:

$$
\mathcal { S } ^ { * } = \Big \{ \mu = \sum _ { k \in [ K ] } p _ { k } \cdot ( G _ { k } ) _ { \# } \nu _ { k } \Big | G _ { k } : { \mathbb { R } } ^ { d } \to { \mathbb { R } } ^ { D } , \nu _ { k } \in \mathcal { P } ( { \mathbb { R } } ^ { d } ) , 0 \le p _ { k } \le 1 , \sum _ { k \in [ K ] } p _ { k } = 1 \Big \} .
$$

This space forms our model space representing distributions on manifolds.

# 3 Mixture of latent distribution matched auto-encoder

From discussions in Section 2, we see that conventional auto-encoder based generative modelling approaches may suffer from low representation power when the target distribution to be estimated lies on a general submanifold without global parametrization. However, the property that any manifold-supported distribution can be expressed in the form of a mixture of generative models (c.f. decomposition (3)) motivates us to employ multiple encoder/decoder pairs, and to use the partition of unity to glue them together with proper weights.

Recall that we have a set of $n$ i.i.d observations $X ^ { ( n ) } = \{ X _ { 1 } , . . . , X _ { n } \}$ sampled from the target distribution $\mu ^ { * }$ lying on a $d$ -dimensional submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ with $d \leq D$ . Let $\{ S _ { k } \} _ { k \in [ K ] }$ be a suitably chosen open cover to $\mathcal { M } = \mathrm { s u p p } ( \mu ^ { \ast } ) \subset \mathbb { R } ^ { D }$ , fix a partition of unity $\{ \rho _ { k } \} _ { k \in [ K ] }$ subordinate to $\{ S _ { k } \} _ { k \in [ K ] }$ ,3 which can be chosen without the knowledge of $\mathcal { M }$ (c.f. Section 4). For any generic approximation family $\mathcal { G }$ consists of $( \mathbf { G } , \mathbf { Q } , \mathbf { v } )$ , where $\mathbf { G } = ( G _ { 1 } , G _ { 2 } , \cdot \cdot \cdot , G _ { K } )$ with $G _ { k } : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , $\mathbf { Q } = \left( Q _ { 1 } , Q _ { 2 } , \cdots , Q _ { K } \right)$ with $Q _ { k } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ , and $\mathbf { v } = \left( \nu _ { 1 } , \nu _ { 2 } , \cdots , \nu _ { K } \right)$ with $\nu _ { k } \in \mathcal P ( \mathbb R ^ { d } )$ , we define the following estimator, which we call mixture of latent distribution matched auto-encoder (MLDMAE) estimator:

$$
\begin{array} { r l } & { \qquad \displaystyle \widehat { \mu } = \sum _ { k \in [ K ] } \widehat { p } _ { k } \cdot ( \widehat { G } _ { k } ) _ { \# } \widehat { \nu } _ { k } , \qquad \mathrm { w i t h } \quad \widehat { p } _ { k } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \rho _ { k } ( X _ { i } ) \quad \mathrm { a n d } } \\ & { \qquad \displaystyle ( \widehat { \mathbf { G } } , \widehat { \mathbf { Q } } , \widehat { \mathbf { v } } ) = \operatorname* { a r g m i n } _ { ( { \mathbf { G } } , { \mathbf { Q } } , { \mathbf { v } } ) \in \mathcal { G } } \sum _ { k = 1 } ^ { K } \bigg \{ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } c \big ( X _ { i } , G _ { k } ( Q _ { k } ( X _ { i } ) ) \big ) \cdot \rho _ { k } ( X _ { i } ) + \lambda _ { k } \cdot \mathcal { D } \big ( \widetilde { \nu } _ { k , Q _ { k } } , { \nu } _ { k } \big ) \bigg \} , } \end{array}
$$

where recall that $c ( \cdot , \cdot )$ is the cost function, $\widetilde { \nu } _ { k , Q _ { k } }$ is a (smoothness-regularized) estimator to the density of (Qk)#( µ ·ρkEµ∗ [ρk] ) (the precise definition is available in Appendix C), and $\mathcal { D } ( \cdot , \cdot )$ is a generic discrepancy measure between distributions on the latent space. Different from conventional LDMAE estimators, MLDMAE can also use empirical Bayes method to select data-dependent prior distributions for local latent variables, which adds extra flexibility in the modeling and may potentially reduce the approximation error. We show in Theorem 1 that for some carefully chosen approximation family $\mathcal { G }$ , cost function $c$ , discrepancy metric $\mathcal { D }$ , and smoothness-regularized estimator $\widetilde { \nu } _ { k , Q _ { k } }$ , the resulting estimator $\widehat { \mu }$ attains the eminimax rate of convergence under the 1-Wasserstein distance as $W _ { 1 } ( \widehat { \mu } , \mu ^ { * } ) \leq C n ^ { - \frac { \alpha \wedge ( \beta - 1 ) + 1 } { 2 ( \alpha \wedge ( \beta - 1 ) ) + d } } \vee \frac { \log n } { \sqrt { n } }$ when $\mu ^ { * }$ is an $\alpha$ -smooth distribution on an unknown $\beta$ -smooth $d$ -dimensional submanifold.

$n ^ { - 1 } \textstyle \sum _ { k = 1 } ^ { K } \textstyle \sum _ { i = 1 } ^ { n } c \bigl ( X _ { i } , G _ { k } ( Q _ { k } ( X _ { i } ) ) \bigr ) \cdot \rho _ { k } ( X _ { i } )$ an be decomposand the penalty $\begin{array} { r } { \sum _ { k = 1 } ^ { K } \lambda _ { k } \cdot \mathcal { D } \big ( \widetilde { \nu } _ { k , Q _ { k } } , \nu _ { k } \big ) } \end{array}$ reconstruction cost. We may also allow the latent dimension $d$ to be different across encoder/decoder pairs over $k \in [ K ]$ . The reconstruction cost aims to learn local parametrizations of the supporting manifold of $\mu ^ { * }$ by enforcing the encoder/decoder pair $( \widehat { Q } _ { k } , \widehat { G } _ { k } )$ to represent some coordinate system $( \varphi _ { k } , \varphi _ { k } ^ { - 1 } )$ of local patch $U _ { k } = { \mathcal { M } } \cap S _ { k }$ of $\mathcal { M }$ in decomposition (3). Therefore, it corresponds to the support recovery of $\mu ^ { * }$ . By employing multiple encoder/decoder pairs, the MLDMAE estimator avoids the restrictive global-parametrization assumption that is implicitly assumed in conventional LDMAE estimators. As a result, MLDMAE is suitable for a wider range of problems (see Fig. 1 for an illustration). On the other hand, the penalty term aims to enforce the reweighted local latent distribution (Qbk)#  µ∗·ρkEµ∗ [ρk]  to match some member $\widehat { \nu } _ { k }$ in the pre-specified prior family, so that $\widehat { \nu } _ { k }$ is close to the $\nu _ { k } ^ { * }$ in decomposition (3).

![](images/cd546072ae27d1a1595e06a606c48dda9e2c3ccbd18e88acfc210be48b8712ce.jpg)  
Figure 1: Comparison between LDMAE and MLDMAE when the target distribution is the uniform distribution on a sphere. Figure (a) plots the real data, and Figures (b), (c) plot the randomly generated samples from the MLDMAE and LDMAE estimators respectively, based on 10000 training samples. The partition of unity chosen in MLDMAE is the smooth partition of unity described in Section 4 with $K = 1 0$ and $\gamma = 1 0$ . The discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ is chosen to be the MMD with Gaussian kernel. We can see that LDMAE fails to capture the correct shape of a sphere. The reason is that the sphere (or any boundaryless manifold) requires at least two covering charts in its describing atlas. The LDMAE model uses a single pair of encoder/decoder, and thus it returns a curve that has start/end points. On the contrary, our estimator is able to learn general manifolds that can not be globally parametrized.

In practice, instead of selecting the best data-dependent priors, we can also fix the prior as a simple distribution $\nu _ { 0 }$ such as an isotropic Gaussian. Moreover, $\mathcal { D } ( \cdot , \cdot )$ can be chosen as certain squared maximum mean discrepancy (MMD) loss $^ 4$ that can be efficiently computed in a closed-form formula. The $k$ -th smoothness-regularized distribution $\widetilde { \nu } _ { k , Q _ { k } }$ in (4) can be constructed by applying kernel-smoothing to its (weighted) empirical counterpart $( Q _ { k } ) _ { \# } \widehat { \mu } _ { n } ^ { k }$ with $\begin{array} { r } { \widehat { \mu } _ { n } ^ { k } = ( n \widehat { p } _ { k } ) ^ { - 1 } \sum _ { i = 1 } ^ { n } \rho _ { k } ( X _ { i } ) \delta _ { X _ { i } } } \end{array}$ , leading to $\widetilde { \nu } _ { k , Q _ { k } } ( z ) =$ $\begin{array} { r } { ( n \widehat { p } _ { k } ) ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { k } ( z , Q _ { k } ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) } \end{array}$ for a suitable kernel $\widetilde { k }$ . Note that when kernel $\widetilde { k }$ is the Gaussian bkernel $\begin{array} { r } { \widetilde { k } ( x , y ) = ( 2 \pi h ) ^ { - \frac { d } { 2 } } \exp ( - \frac { \| x - y \| ^ { 2 } } { 2 h } ) } \end{array}$ with bandwidth parameter $h$ , then $\widetilde { \nu } _ { k , Q _ { k } }$ corresponds to the Gaussian-smoothed distribution $( \widetilde { Q } _ { k } ) _ { \# } \widehat { \mu } _ { n } ^ { k }$ , where $\dot { Q } _ { k }$ is the randomly perturbed encoder defined by $\widetilde { Q } _ { k } ( X ) = Q _ { k } ( X ) + \sqrt { h } \cdot \mathcal { N } ( 0 , I _ { d } )$ .5 Employing such a smoothness-regularized distribution can be viewed as applying a randomized data augmentation to increase the variability of the encoded training samples, which mitigates potential overfitting to data and improves the generalization ability of the resulting estimator.

Introducing the encoder-decoder structure as in our estimator brings several benefits. Computationally, the encoders turn the high-dimensional data into low-dimensional latent variables so that we only need to compute a penalty term over low-dimensional distributions. Therefore, the MLDMAE framework brings less computational burden compared with generative modelling approaches (e.g. iWGAN) that directly deal with distributions in the ambient space. Theoretically, when $d \ll D$ , the data distribution $\mu ^ { * }$ becomes a singular measure in $\mathbb { R } ^ { D }$ . As a consequence, with the information about the supporting manifold of $\mu ^ { * }$ , which is explicitly induced by the encoder-decoder pairs, it is possible to utilize classical techniques of nonparametric density estimation, such as wavelet truncation, to construct a minimax-optimal estimator. Specifically, the underlying true latent variable distribution $\begin{array} { r } { ( Q _ { k } ) _ { \# } \big ( \frac { \mu ^ { * } \cdot \rho _ { k } } { \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ] } \big ) } \end{array}$ defined in the mixture of generative models (3) is, with high probability, absolutely continuous with respect to the Lebesgue measure on $\mathbb { R } ^ { d }$ (c.f. Lemma 4 in Appendix C), which enables us to develop smoothness-regularized estimators by borrowing techniques from Liang (2020) and Singh et al. (2018). Indeed, as suggested by Liang (2020) and Tang & Yang (2022), the rate $O \big ( n ^ { - \frac { \alpha + 1 } { 2 \alpha + d } } \vee \frac { \log n } { \sqrt { n } } \big )$ achieved by the MLDMAE estimator when $\alpha \le \beta - 1$ is minimax-optimal up to logarithmic factor relative to the 1-Wasserstein distance.

# 4 Computation

In this section, we discuss some important computational aspects of the proposed method.

Choice of partition of unity: One issue we need to address is how to choose a reasonable partition of unity $\{ \rho _ { k } \} _ { k \in [ K ] }$ . To do this, we can first run a clustering algorithm such as (mini-batch) $K$ -means to the data using a sufficiently large cluster number $K$ . Based on the clustering result, one straightforward choice of $\rho _ { k }$ is the indicator function 1( $x \in k$ -th cluster). We can also choose a smooth partition of unity by the following: firstly we record the centroid of the $k$ -th cluster as $a _ { k }$ and the smallest radius $r _ { k }$ so that data points in the $k$ -th cluster are included in $\mathbb { B } _ { r _ { k } } ( a _ { k } )$ . Then we can construct an open cover $\{ S _ { k } = \mathbb { B } _ { r _ { k } + \varepsilon } ( a _ { k } ) ^ { \circ } \} _ { k \in [ K ] }$ where $\varepsilon$ is a small positive number so that $\{ S _ { k } \} _ { k \in [ K ] }$ can cover the unknown support of $\mu ^ { * }$ with high probability. Given the open cover, for each $k \in [ K ]$ , we define a local partition function as ${ \widetilde { \rho } } _ { k } ( x ) = ( ( r _ { k } + \varepsilon ) ^ { 2 } - \| x - a _ { k } \| ^ { 2 } ) ^ { \gamma } \cdot \mathbf { 1 } ( x \in S _ { k } )$ , where $\gamma > 1$ is a tuning parameter. The resulting $\{ \rho _ { k } \} _ { k \in [ K ] }$ forms a partition of unity for $\mathcal { M }$ with $\rho _ { k } = \widetilde { \rho } _ { k } / \big ( \sum _ { k ^ { \prime } = 1 } ^ { K } \widetilde { \rho } _ { k ^ { \prime } } \big )$ for $k \in [ K ]$ . Note that $\widetilde { \rho } _ { k }$ tends to give less weight to points away from the centroid $a _ { k }$ for large $\gamma$ .

Choice of penalty terms: We choose the smoothness-regularized distribution $\widetilde { \nu } _ { k , Q _ { k } }$ as the Gaussian kernel-smoothed version of $( Q _ { k } ) _ { \# } \widehat { \mu } _ { n } ^ { k }$ as described in Section 3. This $\widetilde { \nu } _ { k , Q _ { k } }$ relates to the commonly-used Gaussian encoder in VAE, and thus we can utilize the reparametrization trick in VAE to optimize the desired objective function. For the priors $\mathbf { v }$ , we can consider a simple distribution $\nu _ { 0 }$ such as standard Gaussian $\mathcal { N } ( 0 , I _ { d } )$ as is usually done in conventional generative modelling approaches. Moreover, to ensure the smoothness of the learned manifold, we can consider data-driven priors described in Remark 1 in Section 5 below, so that $\nu _ { k }$ and $\widetilde { \nu } _ { k , \widehat { Q } _ { k } }$ can be ensured to have matching tails. For the discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ , to prevent instability in the adversarial training, we can: (1) choose $\mathcal { D } ( \cdot , \cdot )$ to be the (squared) MMD characterized by a positive-definite kernel $k$ , such as the inverse multiquadratics (IMQ) kernel $k ( x , y ) = C _ { i m } / ( C _ { i m } + \| x - y \| _ { 2 } ^ { 2 } )$ and the RBF kernel $k ( x , y ) = \exp ( - \| x - y \| ^ { 2 } / C )$ ; (2) when the intrinsic (latent) dimension is of order $O ( 1 )$ , we can choose $\mathcal { D } ( \cdot , \cdot )$ as the 1-Wasserstein distance computed by the “POT” package (Flamary et al., 2021), which returns the optimal transport map between two discrete measures using network simplex algorithm (Bonneel et al., 2011).

Construction of decoders and encoders: The decoders $\mathbf { G }$ and encoders $\mathbf { Q }$ can be realized through neural networks. However, for a large $K$ , we will have a large number of parameters to train if we see each decoder/encoder as an independent neural network. To address this issue, we enable parameter sharing inside the set of decoders $\mathbf { G }$ and the set of encoders $\mathbf { Q }$ . Specifically, for the set of encoders, we set the last (output) layer to be free among the encoders $\{ Q _ { k } \} _ { k \in [ K ] }$ while other layers to be tied. Moreover, since the decoder-encoder structure aims to reconstruct the data, we want the decoder $G _ { k }$ to be close to the inverse of the encoder $Q _ { k }$ . To achieve this, for the set of decoders, we oppositely set the first (input) layer to be free among the decoders $\{ G _ { k } \} _ { k \in [ K ] }$ and tie other layers. The rationale behind our parameter sharing scheme is that in the encoder, the first (convolutional) layer focuses on “low-level” features extraction and other layers extract “high-level” features. Therefore, the described parameter sharing scheme enables the networks to leverage the common “low-level” information among different clusters of the data, hence improves the model training efficiency.

Optimization of objective function: Recall that $\widetilde { \nu } _ { k , Q _ { k } } = \widetilde { Q } _ { k } ( \widehat { \mu } _ { n } ^ { k } )$ , where $\widetilde { Q } _ { k }$ is a randomized perturbed encoder $\widetilde { Q } _ { k } ( X ) = Q _ { k } ( X ) + \sqrt { h } \cdot \mathcal { N } ( 0 , I _ { d } )$ and $\widehat { \mu } _ { n } ^ { k }$ e b is the re-weighted empirical measure $\begin{array} { r } { \widehat { \mu } _ { n } ^ { k } = \frac { \widehat { \mu } _ { n } \cdot \rho _ { k } } { \widehat { p } _ { k } } } \end{array}$ . Given a discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ and cost function $c ( \cdot , \cdot )$ defining the penalty and reconstruction cost, we can

rewrite the objective function as

$$
\sum _ { k = 1 } ^ { K } \Big \{ \widehat { p } _ { k } \int c \big ( x , G _ { k } ( Q _ { k } ( x ) ) \big ) \mathrm { d } \widehat { \mu } _ { n } ^ { k } + \lambda _ { k } \cdot \mathcal { D } \big ( \nu _ { k } , ( \widetilde { Q } _ { k } ) _ { \# } \widehat { \mu } _ { n } ^ { k } \big ) \Big \} .
$$

To approximate the gradient of this objective function, we sample from the measure $\widehat { \mu } _ { n } ^ { k }$ by introducing auxiliary random variables $u \in { \mathrm { U n i f } } ( 0 , 1 )$ . Specifically, we include data $X _ { i }$ into the empirical measure $\widehat { \mu } _ { n } ^ { k }$ if $u < \rho _ { k } ( X _ { i } )$ and otherwise we exclude the data from $\widehat { \mu } _ { n } ^ { k }$ . Moreover, the penalty term can be estimated using finite samples from $\nu _ { k }$ and $( \widetilde { Q } _ { k } ) _ { \# } \widehat { \mu } _ { n } ^ { m }$ .

<table><tr><td>Algorithm 1:Algorithm for implementing MLDMAE</td></tr><tr><td>Input:Regularization coefficient {λk}k∈[K], partition of unity {βk}k∈[K], discrepancy metric D(.,) and cost function c(·,·),priors {Vk}ke[k],latent (intrinsic) dimension d; Data:X(n) = {X1,X2·. ,Xn}; repeat Sample a mini-batch dataset D from X(n); fork←1toKdo Initialize an empty dataset Dk; for X∈のdo Generate random variable u form Unif(0,1); ifu≤pκ(X)then Add X to dataset k; Generate dataset Lk from prior Vk; Generate dataset δk from N(Q,k(X),h Id) for X uniformly picked in Dk: Update  and 0 by one step first-order method (e.g., Adam, Kingma &amp; Ba (2014)) with objective function:</td></tr></table>

until $( \phi , \theta )$ converges;

Based on the above discussion, we can now develop the algorithm as described in Algorithm 1 for implementing the MLDMAE estimation, where we use $\mathbf { G } _ { \theta } = \{ G _ { \theta , 1 } , G _ { \theta , 2 } , \cdot \cdot \cdot , G _ { \theta , M } \}$ and $\mathbf { Q } _ { \phi } =$ $\{ Q _ { \phi , 1 } , Q _ { \phi , 2 } , \cdot \cdot \cdot , Q _ { \phi , M } \}$ to denote the decoders and encoders parametrized by $\theta$ and $\phi$ respectively.

# 5 Theoretical Analysis

In this section, we derive the finite sample error of the MLDMAE estimator. We first state the following assumptions on the target distribution $\mu ^ { * }$ and the approximation family used in defining the estimator (4).

Assumption A (Target distribution): The target distribution $\mu ^ { * }$ on manifold $\mathcal { M }$ satisfies that: (1) ${ \mathcal { M } } \subset \cup _ { k \in [ K ] } S _ { k }$ ; (2) for any $k \in [ K ]$ , there exists $G _ { k } ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and $Q _ { k } ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ so that $x = G _ { k } ^ { * } ( Q _ { k } ^ { * } ( x ) )$ holds for any $x \in \mathcal { M } \cap S _ { k }$ ; (3) for any $m \in [ K ]$ , let $p _ { k } = \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ]$ , then $p _ { k } > 0$ and $\begin{array} { r } { \nu _ { k } ^ { * } = ( Q _ { k } ^ { * } ) _ { \# } ( \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } ) \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } ) } \end{array}$ ; let $\Omega _ { k } = Q _ { k } ^ { * } ( \mathcal { M } \cap S _ { k } )$ , there exists a function $g _ { k } : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ , so that for any $r > 0$ and $z \in \Omega _ { k }$ , there exists $z ^ { \prime } \in \Omega _ { k }$ such that $z \in B _ { r } ( z ^ { \prime } )$ and $\nu _ { k } ^ { * } ( z ^ { \prime } ) \geq g _ { k } ( r )$ .

Assumption $\mathbf { B }$ (Approximation family): The approximation family $\mathcal { G }$ satisfies that (1) $( \mathbf { G } ^ { * } , \mathbf { Q } ^ { * } , \mathbf { v } ^ { * } ) \in$ $\mathcal { G }$ with $\mathbf { G } ^ { * } \ = \ ( G _ { 1 } ^ { * } , G _ { 2 } ^ { * } , \cdot \cdot \cdot , G _ { K } ^ { * } )$ , $\mathbf { Q } ^ { * } \ = \ ( Q _ { 1 } ^ { * } , Q _ { 2 } ^ { * } , \cdot \cdot \cdot , Q _ { K } ^ { * } )$ and $\mathbf { v } ^ { * } ~ = ~ ( \nu _ { 1 } ^ { * } , \nu _ { 2 } ^ { * } , \cdots , \nu _ { K } ^ { * } )$ ; (2) for any $( \mathbf { G } , \mathbf { Q } , \mathbf { v } ) \in \mathcal { G }$ , it holds that $G _ { k } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and $Q _ { k } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ for any $k \in \lfloor K \rfloor$ .

Example (Manifold-supported distributions): For any $\alpha$ -smooth distribution $\mu ^ { * }$ on a $\beta$ -smooth $d$ -dimensional boundaryless compact submanifold embedded in $\mathbb { R } ^ { D }$ and with a positive density, we can find a suitable open cover $\{ S _ { k } \} _ { k \in [ K ] }$ and partition of unity $\{ \rho _ { k } \} _ { k \in [ K ] }$ so that Assumption A holds. Moreover, the (mixture of) generative model class induced by the approximation family ${ \mathcal G } = \{ ( { \bf G } , { \bf Q } , { \bf v } ) :$ ∀k ∈ [K], Gk ∈ CβL(Rd; RD), Qk ∈ CβL(RD; Rd), νk = (Vk#ν0)·ρk(Gk(z))Eν0 [ρk(Gk(Vk(z)))] , Vk ∈ C α+1L (Bd1 ; Bd1 )	 with ν0 being any fixed $\alpha$ -smooth distribution on $\mathbb { B } _ { 1 } ^ { d }$ whose density value bounded away from zero (e.g., uniform distribution), suffices to model the manifold-supported distributions $\mu ^ { * }$ (i.e., Assumption B holds for the approximation family $\mathcal { G }$ ). In particular, when $\alpha + 1 = \beta$ , we can consider the compositions $G _ { k } \circ V _ { k }$ as $\beta$ -smooth encoders for preventing the estimation of priors, that is, we can use the approximation family $\begin{array} { r } { \mathcal { G } = \left\{ ( \mathbf { G } , \mathbf { Q } , \mathbf { v } ) : \forall k \in [ K ] , G _ { k } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } ) , Q _ { k } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) , \nu _ { k } = \frac { \nu _ { 0 } \cdot \rho _ { k } ( G _ { k } ( z ) ) } { \mathbb { E } _ { v _ { 0 } } [ \rho _ { k } ( G _ { k } ( z ) ) ] } \right\} } \end{array}$ . Further details are available in Appendix B.

Remark 1. The choice of the approximation family suggests that, for learning a manifold-supported distribution, instead of taking the priors $\nu _ { k }$ to be some fixed simple distribution $\nu _ { 0 }$ , we may rescale $\nu _ { 0 }$ by the weight $\rho _ { k } ( G _ { k } ( \cdot ) )$ so that the resulting distribution has a matching tail as $Q _ { k \# } ( \rho _ { k } \mu ^ { * } / \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ] )$ after convergence. However, incorporating such a prior family in MLDMAE may lead to an unstable training due to the high irregularity of functions $\rho _ { k }$ . To address this issue, we can consider “data-driven” priors as follows: we first fix $\nu _ { k }$ to be some simple fixed distribution $\nu _ { 0 }$ , such as uniform distribution or truncated normal, then we run the MLDMAE algorithm to obtain estimators of encoder/decoder pairs $\{ ( \widehat { G } _ { k } ^ { [ 1 ] } , \widehat { Q } _ { k } ^ { [ 1 ] } ) \} _ { k \in [ K ] }$ tion Now we fix the priors $\{ ( \widehat { G } _ { k } ^ { [ 1 ] } , \widehat { Q } _ { k } ^ { [ 1 ] } ) \} _ { k \in [ K ] }$ $\nu _ { k }$ to be o obta $\nu _ { 0 }$ rescaled by estimators of encoder/decoder pairs $\rho _ { k } ( G _ { k } ^ { [ 1 ] } ( \cdot ) )$ , and run the MLDMAE algorithm with initializa- $\{ ( \widehat { G } _ { k } ^ { [ 2 ] } , \widehat { Q } _ { k } ^ { [ 2 ] } ) \} _ { k \in [ K ] }$ . The above steps can continue by fixing the priors $\nu _ { k }$ to be $\nu _ { 0 } \cdot \rho _ { k } ( G _ { k } ^ { \lfloor l \rfloor } ( \cdot ) )$ and obtaining estimators $\{ ( \widehat { G } _ { k } ^ { [ l + 1 ] } , \widehat { Q } _ { k } ^ { [ l + 1 ] } ) \} _ { k \in [ K ] }$ , and stop until no improvement in validation error is seen. Using such a data-driven prior can largely improve the performance of MLDMAE at the intersections of the support of different partition functions, see Fig. 2 for an illustration.

![](images/9fb8bafeb5d6be9928e17549d51e098e49b99aac5e7c6c9400f548aff2452a2d.jpg)  
(a) MLDMAE: truncated normal prior (b) MLDMAE: data-driven prior (once (c) MLDMAE: data-driven prior update) (twice updates)

Figure 2: Performance of MLDMAE with different choices of priors when the target measure is the uniform distribution on a sphere. Figure (a) plots the generated samples from MLDMAE estimator when the priors are truncated normal. Figures (b) and (c) plot the generated samples from MLDMAE estimator with data-driven priors described in Remark 1 under once and twice updates respectively, where $\nu _ { 0 }$ is the truncated normal as in Figure (a). We can see with a simple truncated normal prior, the generated plot tends to be non-smooth at the intersection of different partition functions. While once update of priors using the strategy described in Remark 1 can lead to much better performance.

Example (Distributions with clustering structures): Another example is a distribution induced by the mixture of generative models $\begin{array} { r } { \mu ^ { * } = \sum _ { k = 1 } ^ { K } p _ { k } \cdot ( G _ { k } ^ { * } ) _ { \# } \nu _ { k } ^ { * } } \end{array}$ , where supports of generative models are disjoint. In this case, the supporting manifold of $\mu ^ { * }$ is a disconnected manifold, and we can simply choose $\{ S _ { k } \} _ { k \in [ K ] }$ to be any disjoint sets that can cover each support of the generative model (i.e., $\operatorname { s u p p } ( ( G _ { k } ^ { * } ) _ { \# } \nu _ { k } ^ { * } ) \subset S _ { k }$ for $k \in [ K ]$ ), and take $\rho _ { k }$ to be the indicator function $\mathbf { 1 } ( x \in S _ { k } )$ . With such choices, Assumption A holds if for each $k \in [ K ]$ , $\nu _ { k } ^ { * }$ is $\alpha$ -smooth with a compact support, and $G _ { k } ^ { * }$ is $\beta$ -smooth with a $\beta$ -smooth inverse.

Theorem 1. Fix $\alpha \geq 0$ , $\beta \geq 1$ and a partition of unity $\{ \rho _ { k } \} _ { k \in [ K ] }$ subordinate to the open cover $\{ S _ { k } \} _ { k \in [ K ] }$ . Suppose the target distribution $\mu ^ { * }$ satisfies Assumption $A$ and the approximation family $\vec { \mathcal { G } }$ satisfies Assumption $B$ . If we choose the discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ to be the 1-Wasserstein distance $W _ { 1 }$ and cost function $c ( \cdot , \cdot )$ to be the squared $\ell _ { 2 }$ loss, then there exists a choice of regularization coefficients $\{ \lambda _ { k } \} _ { k \in [ K ] }$ so that for large enough $n$ ,

1. if $\alpha = 0$ , then by choosing the re-weighted empirical measure $\begin{array} { r } { \widetilde { \nu } _ { k , Q _ { k } } = \frac { 1 } { \widehat { p } _ { k } n } \sum _ { i = 1 } ^ { n } \delta _ { Q ( X _ { i } ) } \rho _ { k } \bigl ( X _ { i } \bigr ) } \end{array}$ with $\begin{array} { r } { \widehat { p } _ { k } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \rho _ { k } ( X _ { i } ) } \end{array}$ as the plug-in, the resulting estimator $\widehat { \mu }$ b satisfies with probability at least $1 - n ^ { - 1 }$ that

$$
W _ { 1 } ( \widehat { \mu } , \mu ^ { * } ) \leq C n ^ { - \frac { 1 } { d } } \vee \frac { \log n } { \sqrt { n } } .
$$

2. if $\alpha > 0$ , $\beta > 1$ , then there exists a smoothness-regularized empirical measure $\widetilde { \nu } _ { k , Q _ { k } }$ as the plug-in, so that the resulting estimator $\widehat { \mu }$ satisfies with probability at least $1 - n ^ { - 1 }$ that

$$
W _ { 1 } ( \widehat { \mu } , \mu ^ { * } ) \leq C n ^ { - \frac { ( \alpha \wedge ( \beta - 1 ) ) + 1 } { 2 ( \alpha \wedge ( \beta - 1 ) ) + d } } \vee \frac { \log n } { \sqrt { n } } .
$$

The smoothness-regularized empirical measure $\widetilde { \nu } _ { k , Q _ { k } }$ adopted in the proof of Theorem 1 can either be based on wavelet truncation or kernel density estimator of the measure $Q _ { k \# } ( \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } )$ . Based on the minimax lower bound developed in Liang (2020) and Tang & Yang (2022), the convergence rate in Theorem 1 is minimax-optimal relative to the 1-Wasserstein distance when $\alpha \le \beta - 1$ . If Assumption A holds for $K = 1$ , then statement (5) can provide a theoretical guarantee to the LDMAE estimator. The ambient dimension $D$ does not appear in the exponent of the developed rate; thus Theorem 1 shows the adaptiveness of MLDMAE to low-dimensional submanifold structures since the bound does not suffer from the “curse of dimensionality”. Moreover, the MLDMAE estimator can take advantage of the smoothness of the target measure to further enhance the estimation accuracy by regularizing the empirical measure in the penalty.

# 6 Simulation

In this section, we present some visual results of the MLDMAE approach when apply to common manifolds: 2D-spiral and torus. The precise data generating distributions are given in Appendix A. The penalty term $\mathcal { D } ( \cdot , \cdot )$ is chosen to be the 1-Wasserstein distance computed by the “POT” package (Flamary et al., 2021) and the cost function $c ( \cdot , \cdot )$ is the squared $\ell _ { 2 }$ loss. As benchmarks, we also consider (1) the classic kernel density estimator (KDE) with Gaussian kernel that is commonly employed in statistics literature for density estimation; (2) the LDMAE estimator with the same kind of cost function and discrepancy metric as MLDMAE. The generated samples from the generators learned by different approaches are given in Fig. 3. The 1-Wasserstein distance between the estimated distribution and the true distribution are given in Table 1. We can see that employing multiple encoders and decoders can lead to much better performance than employing a single pair of encoder and decoder. In particular, we can see even though we increase the complexity of the encoder/decoder family, LDMAE still can not capture the correct shape of these standard manifolds in statistics. On the other hand, by allowing multiple encoders/decoders in MLDMAE, the manifold structure can be correctly learned with a relatively simple encoder/decoder structure and a smaller number of training parameters. Moreover, MLDMAE can beat the classic KDE in both examples.

![](images/8527ad7ab439a627f40d5c2470909307d5bed5f9ad017b074921dffd0eebaec5.jpg)  
Figure 3: The figure illustrates the performance of MLDMAE, LDMAE and KDE when the target measures lying on a spiral and torus. We observe $n = 1 0 0 0$ and $n =  { \mathrm { 3 0 0 0 } }$ training points for the example of spiral (Top row) and torus (Bottom row) respectively. The first column plots the training samples. The second column plots the generated samples from the classic kernel density estimator, which corresponds to adding Gaussian noises to the original training samples. The third column plots the generated samples from our proposed MLDMAE estimator ( $K = 1 0$ for spiral and $K = 1 5$ for torus), the encoders and decoders are parameterized by one-hidden layer neural networks with hidden layer size being 128, the partition of unity is chosen to be the smooth partition of unity described in Section 4 with $\gamma = 1 0$ , the priors are selected as described in Remark 1 with $\nu _ { 0 }$ being a truncated normal. The fourth and fifth columns plot the generated samples from the LDMAE estimator where the encoder-decoder pair are parameterized by one-hidden layer and two-hidden layer neural networks respectively.

<table><tr><td colspan="2"></td><td>KDE</td><td>MLDMAE</td><td>LDMAE (1-NN)</td><td>LDMAE (2-NN)</td></tr><tr><td rowspan="2">Spiral</td><td>W1 distance</td><td>0.2119</td><td>0.1936</td><td>0.6315</td><td>0.4666</td></tr><tr><td> Number of training parameters</td><td>一</td><td>4492</td><td>1027</td><td>34051</td></tr><tr><td rowspan="2">Torus</td><td>W1 distance</td><td>0.2837</td><td>0.2335</td><td>0.9101</td><td>0.6193</td></tr><tr><td> Number of training parameters</td><td>/</td><td>10529</td><td>1412</td><td>34565</td></tr></table>

Table 1: The table gives the 1-Wasserstein distance between the target measure and the distribution estimators of different approaches for the spiral and torus examples. We also provide numbers of training parameters for different methods.

# 7 Real Data Application

In this section, we empirically evaluate the proposed MLDMAE approach using three real-world datasets: MNIST handwritten digit (LeCun et al., 1995), Fashion-MNIST (Xiao et al., 2017) and CelebA $6 4 \times$ 64 (Krizhevsky et al., 2009). For comparison, we consider LDMAE approach and variational auto-enocoder (VAE) (Kingma & Welling, 2013; Rezende et al., 2014; Kingma et al., 2016), which are commonly used autoencoder based generative modelling approaches. In all reported experiments, we set the reconstruction cost to be the squared $\ell _ { 2 }$ loss, and fix the priors $\nu _ { k }$ to be a standard Gaussian $\mathcal { N } ( 0 , I _ { d } )$ . The partition of unity is chosen to be the indicator functions described in Section 4. The encoders and decoders are modelled by convolutional deep neural networks with parameter sharing as described in Section 4, and further details are available in Appendix A. We consider two kinds of discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ in the penalty terms of LDMAE and MLDMAE, one is the 1-Wasserstein distance computed through “POT” package, and the other one is MMD with the inverse multiquadratics (IMQ) kernel $k ( x , y ) = 2 d / ( 2 d + \| x - y \| _ { 2 } ^ { 2 } )$ . As described in Tolstikhin et al. (2019), the inverse multiquadratics kernel has a much heavier tail than the conventional RBF kernel $k ( x , y ) = \exp ( - \| x - y \| ^ { 2 } / C )$ , so it can provide more meaningful gradients for outliers. The numbers $K$ of clusters for MLDMAE are selected so that the number of free parameters is around $\textstyle { \frac { 1 } { 5 } } \sim { \frac { 1 } { 2 } }$ of the number of sharing parameters, and it turns out $K = 5$ works well for all the examples. Another important factor is the latent dimension, which is not explicit for the real dataset. Selecting a too small latent dimension would lead to large reconstruction errors and thus result in noisy generated samples. On the contrary, selecting a too large latent dimension would lead to the singularity of the encoded distribution and thus result in numerical instabilities. We use $d = 4$ for Fashion-MNIST, $d = 8$ for MNIST handwritten digit and $d = 6 4$ for CelebA, which seems to work reasonably well, and trainings of MLDMAE are stable and robust to initialization.

To quantitatively assess the MLDMAE estimator, for the dataset of MNIST handwritten digit and Fashion-MNIST, we consider two kinds of evaluation metrics: one is the test log-likelihood (Test LL) used in Goodfellow et al. (2014) by fitting a Gaussian Parzen window to the generated samples and reporting the log-likelihood evaluated at the test samples, and the other one is the 1-Wasserstein distance ( $W _ { 1 }$ ) between the test samples and generated samples. The generated samples are shown in Fig. 4 and the Test LL and $W _ { 1 }$ distance are provided in Table 2. We can see for the Fashion-MNIST dataset, MLDMAE with $W _ { 1 }$ or MMD penalty obviously outperforms VAE and LDMAE. For the MNIST handwritten digit dataset, MLDMAE with MMD penalty outperforms the Wasserstein penalty in the $W _ { 1 }$ metric, and it may attribute to the fact that the MNIST digit dataset has a relatively larger latent dimension $d = 8$ , so we need a very large batch size for accurately estimating the Wasserstein penalty, which will reduce the number of gradient updating. In addition, Fig. 5 gives the trends of the Test LL and $W _ { 1 }$ distance as the cluster number $K$ increases for the MNIST digit dataset. We can see the trends of both metrics become smooth when $M \geq 1 0$ , this is consistent with the underlying fact that the MNIST digit dataset contains 10 digits (clusters). Furthermore, we can see an obvious improvement in both metrics when increasing $K$ in the range of [1, 10], while the total number of training parameters only increases by 7% when cluster number $K$ increases by 1.

Table 2: MNIST handwritten digit and Fashion-MNIST dataset: Test LL and $W _ { 1 }$ distance for different approaches, “+MMD” and “ $+ W _ { 1 }$ ” represent the choices of the discrepancy metric $\mathcal { D } ( \cdot , \cdot )$ in the penalty terms.   

<table><tr><td></td><td>Fashion-MNIST</td><td>MNIST</td></tr><tr><td></td><td>Test LL ↑ W1↓</td><td>Test LL ↑ W1↓</td></tr><tr><td>VAE</td><td>533 77.7</td><td>393 63.2</td></tr><tr><td>LDMAE+MMD</td><td>549 75.5</td><td>381 63.0</td></tr><tr><td>LDMAE+W1</td><td>562 74.6</td><td>400 68.1</td></tr><tr><td>MLDMAE+MMD</td><td>557 66.0</td><td>443 56.6</td></tr><tr><td>MLDMAE+W1</td><td>562 65.8</td><td>456 63.1</td></tr></table>

Table 3: CelebA dataset: FID and KID for different approaches. The penalty term in LDMAE and MLD-MAE are chosen to be MMD penalties.   

<table><tr><td></td><td>FID↓</td><td>KID↓</td></tr><tr><td>VAE</td><td>63.0</td><td>0.063</td></tr><tr><td>LDMAE+MMD</td><td>55.5</td><td>0.057</td></tr><tr><td>LDMAE+SW1</td><td>62.8</td><td>0.064</td></tr><tr><td>MLDMAE+MMD</td><td>51.1</td><td>0.051</td></tr><tr><td>MLDMAE+SW1</td><td>52.0</td><td>0.052</td></tr></table>

![](images/5fb7eabf064bb3dfa880d572e3adfb1ad385486dd68c508612d4968176564e9d.jpg)  
Figure 4: The generated samples from different approaches for Fashion-MNIST (Top row) and MNIST handwritten digit dataset (Bottom row). The first column corresponds to the VAE estimator; the second and third columns correspond to the LMDAE estimator with MMD and $W _ { 1 }$ penalty respectively; the fourth and firth columns correspond to the MLMDAE estimator with MMD and $W _ { 1 }$ penalty respectively.

![](images/4679911ffe03eb97b54a59a3da8b57ec08987e636295545766d593284410d390.jpg)  
Figure 5: Negative test log-likelihood (red) and $W _ { 1 }$ distance (black) of MLDMAE with MMD penalty and different cluster numbers $K$ for the MNIST handwritten digit dataset.

For the celebA dataset, since the ambient dimension $D = 6 4 \times 6 4 \times 3$ is extremely large. Instead of using test log-likelihood or $W _ { 1 }$ distance, which are evaluated in the ambient space; we consider two commonly-used metrics for color image data: FID (Heusel et al., 2017) and KID (Bińkowski et al., 2018), in which the original high-dimensional data is fed into an ImageNet-pretrained inception network to obtain 2048-dimensional inception (feature) representations, and the FID and KID are the fréchet distance and the squared MMD between inception representations of generated samples and test samples, respectively. Moreover, as described previously, the $W _ { 1 }$ penalty is unsuitable for large intrinsic dimensions, for avoiding the curse of dimensionality, we consider the so-called sliced Wasserstein distance: $S W _ { 1 } ( \mu , \nu ) : = \mathbb { E } _ { \theta \sim \mathrm { U n i f } ( \mathbb { S } _ { 1 } ^ { d - 1 } ) } \big [ W _ { 1 } ( \mathrm { P r o j } _ { \theta \neq \mu } , \mathrm { P r o j } _ { \theta \neq \nu } ) \big ]$ , where $\operatorname { P r o j } _ { \theta }$ denotes the projection function to the direction $\theta$ and $\mathrm { U n i f } ( \mathbb { S } _ { 1 } ^ { d - 1 } )$ denotes the uniform distribution on $\mathbb { S } _ { 1 } ^ { d - 1 }$ . The expectation over $\mathrm { U n i f } ( \mathbb { S } _ { 1 } ^ { d - 1 } )$ can be estimated by Monte Carlo method. The sliced-Wasserstein distance slices high-dimensional probability densities into sets of one-dimensional marginal distributions and compare these marginal distributions via the Wasserstein distance, it has similar qualitative properties to the Wasserstein distance, but is much easier to compute. The generated samples and FID, KID are given in Fig. 6 and Table 3.

We can see that the MLDMAE estimator can achieve the best performance under all evaluation metrics. The MLDMAE with MMD penalty performs slightly better than the $S W _ { 1 }$ penalty, while it also requires more computation time (the computation time for MLDMAE $^ +$ MMD is 150s per epoch using NVIDIA A100-SXM4-40GB GPU, while that is 120s per epoch for MLDMAE+ $S W _ { 1 }$ ).

![](images/6e75d791a8454f1f4b4f5d9be08d5eb03052209d560104c3ef6b119d6ff024a2.jpg)  
Figure 6: The generated samples from different approaches (first column: VAE; second and third columns: LDMAE with MMD and $S W _ { 1 }$ penalty respectively; fourth and fifth columns: MLDMAE with MMD and $S W _ { 1 }$ penalty respectively) for the CelebA dataset.

# 8 Conclusion

In this work, we proposed a new approach, mixture of latent distribution matched auto-encoder (MLD-MAE), to improve the conventional auto-encoder based generative modelling approaches for learning manifold-supported distributions. We showed theoretically that the proposed estimator can learn manifoldsupported distributions with a minimax-optimal convergence rate. Moreover, we conducted experiments to show that by employing multiple encoder/decoder pairs, the estimators derived from MLDMAE can substantially boost the target distribution estimation accuracy. In our theoretical analysis, we consider the case where the penalty term is chosen to be the Wasserstein distance. We leave the theoretical analysis for some other adversarial losses, such as the MMD distance considered in our experiments, to future work.

References   
Arjovsky, M., Chintala, S. & Bottou, L. (2017). Wasserstein generative adversarial networks. In International conference on machine learning. PMLR.   
Berenfeld, C., Rosa, P. & Rousseau, J. (2022). Estimating a density near an unknown manifold: a bayesian nonparametric approach. arXiv preprint arXiv:2205.15717 .   
Bińkowski, M., Sutherland, D. J., Arbel, M. & Gretton, A. (2018). Demystifying mmd gans. arXiv preprint arXiv:1801.01401 .   
Bonneel, N., Van De Panne, M., Paris, S. & Heidrich, W. (2011). Displacement interpolation using lagrangian mass transport. In Proceedings of the 2011 SIGGRAPH Asia conference.   
Bouzebda, S. & Didi, S. (2017). Multivariate wavelet density and regression estimators for stationary and ergodic discrete time processes: Asymptotic results. Communications in Statistics - Theory and Methods 46, 1367–1406.   
Brock, A., Donahue, J. & Simonyan, K. (2018). Large scale gan training for high fidelity natural image synthesis.   
Caffarelli, L. A. (1996). Boundary regularity of maps with convex potentials–ii. Annals of Mathematics 144, 453–496.   
Chen, Y., Gao, Q. & Wang, X. (2022). Inferential wasserstein generative adversarial networks. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 84, 83–113.   
Divol, V. (2022). Measure estimation on manifolds: an optimal transport approach. Probability Theory and Related Fields .   
Eldering, J. (2013). Normally Hyperbolic Invariant Manifolds: The Noncompact Case. Paris: Atlantis Press.   
Evans, L. C. (2010a). Partial differential equations, vol. 19. American Mathematical Soc.   
Evans, L. C. (2010b). Partial differential equations. Providence, R.I.: American Mathematical Society.   
Flamary, R., Courty, N., Gramfort, A., Alaya, M. Z., Boisbunon, A., Chambon, S., Chapel, L., Corenflos, A., Fatras, K., Fournier, N. et al. (2021). Pot: Python optimal transport. J. Mach. Learn. Res. 22, 1–8.   
Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A. & Bengio, Y. (2014). Generative adversarial networks.   
Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B. & Hochreiter, S. (2017). Gans trained by a two time-scale update rule converge to a local nash equilibrium .   
Jupp, P. E. & Mardia, K. V. (2009). Directional statistics. John Wiley & Sons.   
Khayatkhoei, M., Singh, M. K. & Elgammal, A. (2018). Disconnected manifold learning for generative adversarial networks. In Advances in Neural Information Processing Systems, S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi & R. Garnett, eds., vol. 31. Curran Associates, Inc.   
Kingma, D. P. & Ba, J. (2014). Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 .   
Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I. & Welling, M. (2016). Improved variational inference with inverse autoregressive flow. In Advances in Neural Information Processing Systems, D. Lee, M. Sugiyama, U. Luxburg, I. Guyon & R. Garnett, eds., vol. 29. Curran Associates, Inc.   
Kingma, D. P. & Welling, M. (2013). Auto-encoding variational bayes.   
Kolouri, S., Pope, P. E., Martin, C. E. & Rohde, G. K. (2018). Sliced-wasserstein autoencoder: An embarrassingly simple generative model. arXiv preprint arXiv:1804.01947 .   
Krizhevsky, A., Hinton, G. et al. (2009). Learning multiple layers of features from tiny images .   
Lan, Z., Reich, B. J. & Bandyopadhyay, D. (2021). A spatial bayesian semiparametric mixture model for positive definite matrices with applications in diffusion tensor imaging. Canadian Journal of Statistics 49, 129–149.   
LeCun, Y., Jackel, L. D., Bottou, L., Cortes, C., Denker, J. S., Drucker, H., Guyon, I., Muller, U. A., Sackinger, E., Simard, P. et al. (1995). Learning algorithms for classification: A comparison on handwritten digit recognition. Neural networks: the statistical mechanics perspective 261, 2.   
Li, C.-L., Chang, W.-C., Cheng, Y., Yang, Y. & Póczos, B. (2017). Mmd gan: Towards deeper understanding of moment matching network. Advances in neural information processing systems 30.   
Liang, T. (2020). How well generative adversarial networks learn distributions.   
Lin, L., Lazar, D., Sarpabayeva, B. & Dunson, D. B. (2020). Robust optimization and inference on manifolds. arXiv preprint arXiv:2006.06843 .   
Lin, L., Rao, V. & Dunson, D. (2017). Bayesian nonparametric inference on the stiefel manifold. Statistica Sinica , 535–553.   
Ling, Y., An, Y., Liu, M., Hasan, S. A., Fan, Y. & Hu, X. (2017). Integrating extra knowledge into word embedding models for biomedical nlp tasks. In 2017 International Joint Conference on Neural Networks (IJCNN). IEEE.   
Luo, L., Yang, Z., Cao, M., Wang, L., Zhang, Y. & Lin, H. (2020). A neural network-based joint learning approach for biomedical entity and relation extraction from biomedical literature. Journal of biomedical informatics 103, 103384.   
Mardia, K. (1999). Directional statistics and shape analysis. Journal of applied Statistics 26, 949–957.   
Oord, A. v. d., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior, A. & Kavukcuoglu, K. (2016). Wavenet: A generative model for raw audio.   
Rezende, D. J., Mohamed, S. & Wierstra, D. (2014). Stochastic backpropagation and approximate inference in deep generative models.   
Silverman, B. W. (2018). Density estimation for statistics and data analysis. Routledge.   
Singh, S., Uppal, A., Li, B., Li, C.-L., Zaheer, M. & Poczos, B. (2018). Nonparametric density estimation under adversarial losses. In Advances in Neural Information Processing Systems, S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi & R. Garnett, eds., vol. 31. Curran Associates, Inc.   
Tang, R. & Yang, Y. (2022). Minimax rate of distribution estimation on unknown submanifold under adversarial losses. arXiv preprint arXiv:2202.09030 .   
Terradot, L., Durnell, N., Li, M., Li, M., Ory, J., Labigne, A., Legrain, P., Colland, F. & Waksman, G. (2004). Biochemical characterization of protein complexes from the helicobacter pylori protein interaction map: strategies for complex formation and evidence for novel interactions within type iv secretion systems. Molecular & Cellular Proteomics 3, 809–819.   
Tolstikhin, I., Bousquet, O., Gelly, S. & Schoelkopf, B. (2019). Wasserstein auto-encoders.   
Tsybakov, A. B. (2009). Introduction to Nonparametric Estimation. New York, NY: Springer New York.   
Villani, C. (2009). Optimal Transport: Old and New. Berlin, Heidelberg: Springer Berlin Heidelberg.   
Wainwright, M. J. (2019). High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press.   
Xiao, H., Rasul, K. & Vollgraf, R. (2017). Fashion-mnist: a novel image dataset for benchmarking machine learning algorithms. arXiv preprint arXiv:1708.07747 .   
Xu, Q., Huang, G., Yuan, Y., Guo, C., Sun, Y., Wu, F. & Weinberger, K. (2018). An empirical study on evaluation metrics of generative adversarial networks. arXiv preprint arXiv:1806.07755 .   
You, Z.-H., Lei, Y.-K., Gui, J., Huang, D.-S. & Zhou, X. (2010). Using manifold embedding for assessing and predicting protein interactions from high-throughput experimental data. Bioinformatics 26, 2744–2751.   
Zhang, R., Ogden, R. T., Picard, M. & Srivastava, A. (2022). Nonparametric k-sample test on shape spaces with applications to mitochondrial shape analysis. Journal of the Royal Statistical Society: Series $C$ (Applied Statistics) 71, 51–69.   
Zhao, S., Song, J. & Ermon, S. (2019). Infovae: Balancing learning and inference in variational autoencoders. Proceedings of the AAAI Conference on Artificial Intelligence 33, 5885–5892.

# Appendix

Notations: We adopt the notations in the manuscript, and further introduce the following additional notations for technical proofs. We use $\mathbf { N } ( \mathcal { F } , \widetilde { d } , \epsilon )$ to denote the $\epsilon$ -covering number of function space $\mathcal { F }$ with respect to pseudo-metric $\dot { d }$ . We use $\mathbb { B } _ { r } ( x )$ to denote the closed ball centered at $x$ with radius $r$ under the $\ell _ { 2 }$ distance; in particular, we use $\mathbb { B } _ { r } ^ { d }$ denote $\mathbb { B } _ { r } ( \mathbf { 0 } _ { d } )$ when no ambiguity may arise. We denote $\mathbb { S } _ { 1 } ^ { d - 1 } = \left\{ x \in \mathbb { R } ^ { d } \ : \ \| x \| = 1 \right\}$ . For a function $f : \Omega \to \mathbb { R } ^ { d }$ , we use $\mathbf { J } _ { f } ( x )$ to denote the $d \times m$ Jacobian matrix of $f$ at $x \in \Omega$ . For a function $f :  { \mathbb { R } ^ { d } } \to  { \mathbb { R } }$ , we use $f ^ { ( a ) }$ to denote its mixed partial derivative $\partial ^ { | a | } f / \partial x _ { 1 } ^ { a _ { 1 } } \cdot \cdot \cdot \partial x _ { d } ^ { a _ { d } }$ . We define the $\alpha$ -smooth Hölder (function) class (see e.g., Evans (2010b)) with radius $r > 0$ over $\Omega$ as $\begin{array} { r } { C _ { r } ^ { \alpha } ( \Omega ) : = \left\{ f : \Omega \to \mathbb { R } \big | \| f \| _ { C ^ { \alpha } ( \Omega ) } = \sum _ { | a | \leq | \alpha \rfloor } \operatorname* { m a x } _ { x \in \Omega } | f ^ { ( a ) } ( x ) | + \right. } \end{array}$ $\begin{array} { r } { \sum _ { | a | = \lfloor \alpha \rfloor } \operatorname* { m a x } _ { x , y \in \Omega , x \neq y } \left| f ^ { ( a ) } ( x ) - f ^ { ( a ) } ( y ) \right| / \| x - y \| ^ { \tilde { \alpha } - \lfloor \alpha \rfloor } \leq r \} } \end{array}$ . Similarly, we use $C _ { r } ^ { \alpha } ( \Omega ; \mathbb { R } ^ { D } ) = \{ f =$ $( f _ { 1 } , \dots , f _ { D } ) : \Omega \to \mathbb { R } ^ { D } | \forall j \in [ D ] , f _ { j } \in C _ { r } ^ { \alpha } ( \Omega )  \}$ to denote the vector valued function space counterpart. For an $f \in C _ { r } ^ { \alpha } ( \Omega ; \mathbb { R } ^ { D } )$ and a multi-index $a \in  { \mathbb { N } } _ { 0 } ^ { d }$ , we denote $f ^ { ( a ) }$ as the $D$ dimensional vector whose $j$ -th component is the mixed partial derivative $[ f _ { j } ] ^ { ( a ) }$ of $f _ { j }$ for $j \in [ D ]$ . Throughout, $C$ , $c$ , $C _ { 0 }$ , $c _ { 0 }$ , $C _ { 1 }$ , $c _ { 1 }$ , $C _ { 2 }$ , $c _ { 2 } , . \ .$ are generically used to denote positive constants whose values might change from one line to another, but are independent from everything else.

# A Remaining implementation details

# A.1 Simulation

The training points $\mathcal { D }$ in spiral are generated via the following steps: (1) generate $\phi _ { 0 } \sim \mathcal { N } ( 0 , 1 )$ ; (2) set $\phi = 3 \pi \phi _ { 0 }$ ; (3) generate data point $X$ though $\begin{array} { r } { X = [ \frac { \cos ( \phi + 2 ) \cdot \phi } { \pi } , \frac { 2 \sin ( \phi + 2 ) \cdot \phi } { \pi } ] } \end{array}$ . The training points $\mathcal { D }$ in torus are generated via the following steps: (1) generate $\phi _ { 0 } , \phi _ { 1 } \sim { \mathcal { N } } ( 0 , 1 )$ ; (2) set $\phi = 2 \pi \phi _ { 0 }$ and $\theta = 2 \pi \phi _ { 1 }$ ; (3) generate data point $X$ through X $\ell = [ ( 3 + \cos ( \theta ) ) \cos ( \phi ) , ( 3 + \cos ( \theta ) ) \sin ( \phi ) , \sin ( \theta ) ]$ . The cluster number $M$ in MLDMAE is $M = 1 0$ for the dataset of spiral and $M = 1 5$ for the dataset of torus. The partition of unity is given by $\rho _ { k } = \widetilde { \rho } _ { k } / \big ( \sum _ { k ^ { \prime } = 1 } ^ { K } \widetilde { \rho } _ { k ^ { \prime } } \big )$ with ${ \widetilde { \rho } } _ { k } = ( r _ { k } ^ { 2 } - \| x - a _ { k } \| ^ { 2 } ) ^ { 1 0 } \cdot \mathbf { 1 } ( x \in S _ { k } )$ , where $\{ a _ { k } \} _ { k \in [ K ] }$ are the centers returned by the K-means algorithm, $r _ { k } = \operatorname* { s u p } \{ \| x - a _ { k } \| : x \in \mathcal { D }$ ; $\forall k _ { 1 } \in [ K ]$ , $\| x - a _ { k } \| \leq \| x - a _ { k _ { 1 } } \| \}$ , and $S _ { k } = \mathbb { B } _ { r _ { k } } ( a _ { k } )$ .

# A.2 Real data application

The specification of our models trained on MNIST handwritten digit, Fashion-MNIST and CelebA are described in Table 4, 5, and 6. “Shared” is short for parameter sharing among encoders or among decoders. All models are optimized using Adam optimization with learning rate 0.001, $\beta _ { 1 } = 0 . 9$ , and $\beta _ { 2 } = 0 . 9 9 9$ . The partition of unity for all datasets is chosen as the indicator function $\rho _ { k } ( x ) = 1 ( x \in \mathrm { c l u s t e r } \ m )$ for $k \in [ K ]$ . The codes for reproducing the experiments are available in https://github.com/rtang1997/MLDMAE.

Table 4: Encoder/decoder Network architecture and hyperparameters for the MNIST handwritten digit dataset.   

<table><tr><td>Operation</td><td>Kernel</td><td></td><td>StridesFeature maps</td><td>Activation</td><td>Shared?</td></tr><tr><td>Decoder Gκ(z) : k ∈[K],z ∈ N(0,Id)</td><td></td><td></td><td>8</td><td></td><td></td></tr><tr><td>Fully connected</td><td></td><td></td><td>3×3×128</td><td>ReLU</td><td>No</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>7×7×64</td><td>ReLU</td><td>Yes</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>14 × 14 × 32</td><td>ReLU</td><td>Yes</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>28×28×1</td><td>ReLU</td><td>Yes</td></tr><tr><td>Encoder Qκ(x) : k ∈ [K]</td><td></td><td></td><td>28×28×1</td><td></td><td></td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>26×26×3</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>12 × 12 × 32</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>5×5×64</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>2×2×128</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Fully connected</td><td></td><td></td><td>8</td><td></td><td>No</td></tr><tr><td>Cluster number K for MLDMAE</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>Batch size</td><td></td><td></td><td>256 for MLDMAE,and128 forWAE and VAE</td><td></td><td></td></tr><tr><td>Number of epochs</td><td>50</td><td></td><td></td><td></td><td></td></tr><tr><td>Leaky ReLU slope</td><td>0.1</td><td></td><td></td><td></td><td></td></tr><tr><td>Regularization coefficients (入k)</td><td></td><td></td><td>100 for MMD penalty and 10 for W1 penalty</td><td></td><td></td></tr><tr><td>Bandwidth (h) for MLDMAE</td><td>0.01</td><td></td><td></td><td></td><td></td></tr><tr><td>Number of training samples</td><td>60k</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>Operation</td><td>Kernel</td><td>Strides</td><td>Feature maps</td><td>Activation</td><td>Shared?</td></tr><tr><td>Decoder Gκ(z) : k ∈[K],z ∈N(0,Id)</td><td></td><td></td><td>4</td><td></td><td></td></tr><tr><td>Fully connected</td><td></td><td></td><td>3×3×128</td><td>ReLU</td><td>No</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>7×7×64</td><td>ReLU</td><td>Yes</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>14 × 14 × 32</td><td>ReLU</td><td>Yes</td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>2×2</td><td>28× 28×1</td><td>ReLU</td><td>Yes</td></tr><tr><td>Encoder Qk(x) : k ∈ [K]</td><td></td><td></td><td>28×28×1</td><td></td><td></td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>26×26×3</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>12 × 12 × 32</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>5×5×64</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Convolution</td><td>3×3</td><td>2×2</td><td>2×2×128</td><td>LeakyReLU</td><td>Yes</td></tr><tr><td>Fully connected</td><td></td><td></td><td>4</td><td></td><td>No</td></tr><tr><td>Cluster number K for MLDMAE</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>Batch size</td><td></td><td></td><td>256 for MLDMAE,and 128 for WAE and VAE</td><td></td><td></td></tr><tr><td>Number of epochs</td><td>50</td><td></td><td></td><td></td><td></td></tr><tr><td>Leaky ReLU slope</td><td>0.1</td><td></td><td></td><td></td><td></td></tr><tr><td>Regularization coefficients (入k)</td><td></td><td></td><td>100 for MMD penalty and 10 for W1 penalty</td><td></td><td></td></tr><tr><td>Bandwidth (h) for MLDMAE</td><td>0.01</td><td></td><td></td><td></td><td></td></tr><tr><td>Number of training samples</td><td>60k</td><td></td><td></td><td></td><td></td></tr></table>

Table 5: Encoder/decoder architecture and hyperparameters for the Fashion-MNIST dataset.

Table 6: Encoder/decoder architecture and hyperparameters for the CelebA dataset.   

<table><tr><td>Operation</td><td></td><td></td><td>KernelStridesFeature maps</td><td>ActivationShared?</td><td></td></tr><tr><td>Decoder Gk(z) : k ∈[K],z ∈ N(0,Id)</td><td></td><td></td><td>64</td><td></td><td></td></tr><tr><td>Fully connected</td><td></td><td></td><td>8×8×1024</td><td>ReLU</td><td>No</td></tr><tr><td>Transposed convolution</td><td>5×5</td><td>2×2</td><td>16 ×16 ×512 </td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td>5×5</td><td></td><td></td><td>ReLU</td><td></td></tr><tr><td>Transposed convolution Batch normalization</td><td></td><td></td><td>2×232×32×256</td><td></td><td>Yes</td></tr><tr><td>Transposed convolution</td><td>5×5</td><td>2×2</td><td>64×64×128</td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Transposed convolution</td><td>3×3</td><td>1×1</td><td>64 × 64×3</td><td>Tanh</td><td>Yes</td></tr><tr><td>Encoder Qk(x) : k ∈[K]</td><td></td><td></td><td>64×64×3</td><td></td><td></td></tr><tr><td>Convolution</td><td>5×5</td><td>2×2</td><td>32 × 32× 128</td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convolution</td><td>5×5</td><td>2×2</td><td>16 ×16×256</td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convolution</td><td>5×5</td><td>2×2</td><td>8×8×512</td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Convolution</td><td>5×5</td><td>2×2</td><td>4×4×1023</td><td>ReLU</td><td>Yes</td></tr><tr><td>Batch normalization</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fully connected</td><td></td><td></td><td>64</td><td></td><td>No</td></tr><tr><td>Cluster number K for MLDMAE</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>Batch size</td><td></td><td></td><td>256 for MLDMAE,and 128 for WAE and VAE</td><td></td><td></td></tr><tr><td>Number of epochs</td><td>50</td><td></td><td></td><td></td><td></td></tr><tr><td>Regularization coefficients (入)</td><td>100</td><td></td><td></td><td></td><td></td></tr><tr><td>Bandwidth (h) for SWAE and MLDMAE</td><td>0.01</td><td></td><td></td><td></td><td></td></tr><tr><td>Number of training samples</td><td>180k</td><td></td><td></td><td></td><td></td></tr></table>

# B Generative modelling of Distributions on submanifolds

A submanifold in the ambient space $\mathbb { R } ^ { D }$ can be viewed as a nonlinear “subspace”. Borrow the definition in Tang & Yang (2022), we define the family of smooth distributions on $d$ -dimensional smooth compact submanifolds without boundaries on $\mathbb { R } ^ { D }$ as the set $\mathcal { P } ^ { * } = \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ with $d \leq D$ , $\beta > 1$ and $\alpha \in ( 0 , \beta - 1 ]$ composed of all probability measures $\mu \in \mathcal P ( \mathbb { R } ^ { D } )$ satisfying:

1. $\mu$ is an $\alpha$ -smooth distribution on a $\beta$ -smooth $d$ -dimensional compact submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ .   
2. The density $\mu$ relative to the volume measure of $\mathcal { M }$ is uniformly bounded from below by $1 / L ^ { * }$ on $\mathcal { M }$ .   
3. $\mathcal { M }$ is covered by an atlas $\mathcal { A } = \{ ( U _ { \lambda } , \phi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ on $\mathcal { M }$ such that: a) each chart $( U , \phi )$ in atlas $\mathcal { A }$ satisfies $\| \phi ^ { - 1 } \| _ { C ^ { \beta } ( \phi ( U ) ) } \leq L ^ { * }$ and $\| \mu \circ \phi ^ { - 1 } \| _ { C ^ { \alpha } ( \phi ( U ) ) } \leq L ^ { * }$ ; b) for any $z \in \phi ( U )$ , the Jacobian of $\phi ^ { - 1 } ( z )$ is full rank and all its singular values are lower bounded by $1 / L ^ { * }$ in absolute values. Moreover, for any $x \in \mathcal { M }$ , there exists a $\lambda \in \Lambda$ such that $U _ { \lambda }$ and $\phi _ { \lambda } ( U _ { \lambda } )$ covers $\mathbb { B } _ { 1 / L ^ { * } } ( x ) \cap \mathcal { M }$ and $\mathbb { B } _ { 1 / L ^ { * } } ( \phi _ { \lambda } ( x ) )$ respectively.

We have the following lemma describing the mixture of generative model classes that can model the submanifold-supported distributions.

Lemma 1. Consider OK = {Sk = B◦rk (ak)}Km=1, for k ∈ [K], choosing ρk(x) = P ρek(x)k∈[K] ρk(x) with $\widetilde { \rho } _ { k } ( \boldsymbol { x } ) = ( r _ { k } ^ { 2 } - \| \boldsymbol { x } - \boldsymbol { a } _ { k } \| ^ { 2 } ) ^ { \gamma } \cdot \mathbf { 1 } ( \boldsymbol { x } \in S _ { k } )$ for $\gamma \geq \alpha + 1$ . There exists a constant $r ^ { * }$ that only depends on $( L ^ { * } , \beta , \alpha , d , D )$ so that for any $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ , if ( $\mathbf { \chi } ^ { \prime } \mathbf { \mathcal { I } } ) \ \operatorname { s u p p } ( { \boldsymbol { \mu } } ^ { * } ) \ \subset \ \cup _ { k \in [ K ] } S _ { k }$ ; (2) for any $k \in [ K ]$ , $r _ { k } \leq r ^ { * }$ and $a _ { k } \in \mathcal { M }$ ; (3) there exists some positive constants $L _ { 1 } ^ { * }$ so that $\begin{array} { r } { \operatorname* { m i n } _ { k \in [ K ] } r _ { k } \ge L _ { 1 } ^ { * } } \end{array}$ and $\begin{array} { r } { \operatorname* { i n f } _ { x \in \mathcal { M } } \sum _ { k \in [ K ] } \widetilde { \rho } _ { k } ( x ) \geq L _ { 1 } ^ { * } } \end{array}$ . Then:

1. there exist some universal constants $( L , c )$ that only depend on $( L ^ { * } , L _ { 1 } ^ { * } , \beta , \alpha , d , D , \gamma )$ so that Assumption $A$ holds for $\mu ^ { * }$ with upper bound $L$ and function $g _ { k } ( r ) = c ( r ^ { \gamma } \wedge 1 )$ for any $k \in [ K ]$ ;

2. consider $\nu _ { 0 } \in \mathcal { P } ( \mathbb { B } _ { 1 } ^ { d } )$ whose density being $\alpha$ -smooth and bounded below from zero, and approximation families

$$
\begin{array} { r l } { ( a ) } & { { \mathcal G } _ { 1 } = \big \{ ( G , Q , v ) : \forall k \in [ K ] , G _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { d } ; { \mathbb R } ^ { D } ) , Q _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { D } ; { \mathbb R } ^ { d } ) , \nu _ { k } \in \mathcal { P } ( { \mathbb R } _ { 1 } ^ { d } ) \mathrm { w i t h } } \\ { \mathrm { v a r } _ { \mathrm { { L } } } ( { \mathbb B } _ { 1 } ^ { d } ) \big \} ; } \\ { ( b ) \cdot } & { { \mathcal G } _ { 2 } = \big \{ ( G , Q , v ) : \forall k \in [ K ] , G _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { d } ; { \mathbb R } ^ { D } ) , Q _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { D } ; { \mathbb R } ^ { d } ) , v _ { k } = \frac { ( V _ { m \mu } v _ { 0 } ) \cdot \rho _ { k } ( G _ { k } ( z ) ) } { \mathbb E _ { v _ { 0 } } [ \rho _ { k } ( G _ { k } ( V _ { k } ( z ) ) ) ] } , } \\ { \mathrm { v a r } _ { \mathrm { { L } } } ^ { \gamma \alpha + 1 } ( { \mathbb B } _ { 1 } ^ { d } ; { \mathbb B } _ { 1 } ^ { d } ) \big \} ; } \\ { ( c ) . \quad { \mathcal G } _ { 3 } = \big \{ ( G , Q , v ) : \forall k \in [ K ] , G _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { d } ; { \mathbb R } ^ { D } ) , Q _ { k } \in C _ { L } ^ { \beta } ( { \mathbb R } ^ { D } ; { \mathbb R } ^ { d } ) , v _ { k } = \frac { v _ { 0 } \cdot \rho _ { k } ( G _ { k } ( z ) ) } { \mathbb E _ { v _ { 0 } } [ \rho _ { k } ( G _ { k } ( z ) ) ] } \big \} . } \end{array}
$$

then for sufficiently large $L$ , we have Assumption $B$ holds for $\mathcal { G } _ { 1 }$ or $\mathcal { G } _ { 2 }$ , that is, the approximation families $\vec { \mathcal { G } } _ { 1 }$ and $\mathcal { G } _ { 2 }$ are both sufficient to model distributions inside $\mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ . Moreover, if $\alpha = \beta - 1$ , then Assumption $B$ holds for $\mathcal { G } _ { 3 }$ .

The next lemma shows that ${ \mathcal { O } } _ { K }$ satisfying conditions of Lemma 1 can be found based on a small portion of data.

Lemma 2. Consider any $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ with support $\mathcal { M }$ , fix $r ^ { * }$ being an arbitrary positive constant and let $n _ { 1 } \leq n$ be a positive integer. Then for any positive constant $c$ , there exist constants $C , c _ { 1 }$ that only depend on $( d , D , \beta , L ^ { * } , r ^ { * } , c )$ so that when $C \leq n _ { 1 } \leq n$ , let $I _ { 1 }$ be any subset of $[ n ]$ with $| I _ { 1 } | = n _ { 1 }$ , it holds with probability larger than $1 - n _ { 1 } ^ { - c }$ that

$\begin{array} { r } { \imath ) . \ M \subset \bigcup _ { i \in I _ { 1 } } \mathbb { B } _ { c _ { 1 } ( \frac { \log n _ { 1 } } { n _ { 1 } } ) ^ { \frac { 1 } { d } } } ( x _ { i } ) ; } \end{array}$ (2). there exists a constant $K$ that only depends on $( d , D , \beta , L ^ { * } , r ^ { * } )$ and a subset $\{ a _ { k } \} _ { k = 1 } ^ { K } \subset \{ X _ { i } \} _ { i \in I _ { 1 } }$ so that

$$
\begin{array} { r l } & { ( a ) . \bigcup _ { i \in I _ { 1 } } \mathbb { B } _ { c _ { 1 } ( \frac { \log n _ { 1 } } { n _ { 1 } } ) ^ { \frac { 1 } { d } } } ( x _ { i } ) \subset \bigcup _ { k = 1 } ^ { K } \mathbb { B } _ { r ^ { * } } ( a _ { k } ) . } \\ & { ( b ) . \operatorname* { i n f } _ { x \in M } \sum _ { k \in [ K ] } \widetilde { \rho } _ { k } ( x ) > ( \frac { r ^ { * } } { \sqrt { 2 } } ) ^ { 2 \gamma } , \ w h e r e \widetilde { \rho } _ { k } ( x ) = ( ( r ^ { * } ) ^ { 2 } - \| x - a _ { k } \| ^ { 2 } ) ^ { \gamma } \cdot \mathbf { 1 } ( x \in \mathbb { B } _ { r ^ { * } } ( a _ { k } ) ) . } \end{array}
$$

# C Proof of Theorem 5.1

We first consider the case $\alpha > 0$ and $\beta > 1$ . To simplify the notation, we write $\tilde { \alpha } = \alpha \wedge ( \beta - 1 )$ . We consider two kinds of smoothness-regularized empirical measure $\widetilde { \nu } _ { k , Q _ { k } }$ , one is based on kernel density estimator and one is based on wavelet estimator.

# Kernel density estimator: Define

$$
\widetilde { \nu } _ { k , Q _ { k } } ( y ) = \frac { 1 } { n \widehat { p _ { k } } h ^ { d } } \sum _ { i = 1 } ^ { n } \widetilde { k } ( \frac { y - Q _ { k } ( X _ { i } ) } { h } ) \rho _ { k } ( X _ { i } ) , \quad \widehat { p } _ { k } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \rho _ { k } ( X _ { i } ) ,
$$

with $h = n ^ { - 1 / ( 2 \widetilde { \alpha } + d ) }$ and $\widetilde { k } : \mathbb { R } ^ { d } \to \mathbb { R }$ satisfies that

$1 . { \overset { \sim } { k } } ( \cdot )$ is $\lceil \tilde { \alpha } \rceil \vee \lceil \frac { d } { 2 } \rceil$ smooth in $\mathbb { R } ^ { d }$ and has support contained in $[ - 1 , 1 ] ^ { d }$ ;

2. $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \widetilde { k } ( z ) \mathrm { d } z = 1 } \end{array}$ and for any $j \in  { \mathbb { N } } _ { 0 } ^ { d }$ with $1 \leq | j | \leq \lfloor \alpha \rfloor + 1$ , $\begin{array} { r } { \int \stackrel { \sim } { k } ( z ) \cdot z ^ { j } \mathrm { d } z = 0 } \end{array}$ ;

3. for any $z \in \mathbb { R } ^ { d }$ , $ { \widetilde { k } } ( z ) =  { \widetilde { k } } ( - z )$ .

Wavelet estimator: Define $\widetilde { \nu } _ { k , Q _ { k } } ( y )$ as

with

$$
\widetilde { \nu } _ { k , Q _ { k } } ( y ) = \frac { 1 } { \widehat { p } _ { k } } \Big ( \sum _ { m \in \mathbb { S } } \widetilde { a } _ { m } ^ { Q _ { k } } \phi _ { m } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } \widetilde { \theta } _ { l j m } ^ { Q _ { k } } \psi _ { l j m } ( y ) \Big ) ,
$$

$$
\begin{array} { r l r } {  { \widehat { p } _ { k } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \rho _ { k } ( X _ { i } ) ; } } \\ & { \mathbb { S } = \{ m \in \mathbb { Z } ^ { d } | \operatorname { s u p p } ( \phi _ { m } ) \cap [ - L , L ] ^ { d } \neq \emptyset \} ; } \\ & { \mathbb { S } _ { l j } = \{ m \in \mathbb { Z } ^ { d } | \operatorname { s u p p } ( \psi _ { l j m } ) \cap [ - L , L ] ^ { d } \neq \emptyset \} ; } \end{array}
$$

$$
\begin{array} { r } { \widetilde { a } _ { m } ^ { Q _ { k } } = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \phi _ { m } ( Q _ { k } ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) ; } \\ { \widetilde { \theta } _ { l j m } ^ { Q _ { k } } = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \psi _ { l j m } ( Q _ { k } ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) , } \end{array}
$$

where $2 ^ { d J } \asymp n ^ { \frac { d } { 2 \alpha + d } }$ and $\{ \phi _ { m } , \psi _ { l j m } : l = 1 , \cdots , 2 ^ { d } - 1 , j \in \mathbb { N } , m \in \mathbb { Z } ^ { d } \}$ } is the orthonormal wavelet basis for Besov space on $\mathbb { R } ^ { d }$ defined as $\phi _ { m } ( y ) = \phi ( y - m )$ and $\psi _ { l j m } ( y ) = 2 ^ { \frac { j d } 2 } \psi _ { l } ( 2 ^ { j } y - m )$ , and it holds that $\phi ( \cdot )$ and $\psi _ { l } ( \cdot )$ are compactly supported and have bounded $\lceil \alpha \vee \left( { \frac { d } { 2 } } - \alpha \right) \rceil$ order derivatives for any $1 \leq l \leq 2 ^ { d } - 1$ (Bouzebda $\&$ Didi, 2017).

We will show both choices of $\widetilde { \nu } _ { k , Q _ { k } }$ can lead to the desired result. By Assumption A of $\mu ^ { * }$ , for any $k \in \lfloor K \rfloor$ , there exist $G _ { k } ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ and $Q _ { k } ^ { \ast } \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ so that and for any $x \in \mathcal { M } \cap S _ { k }$ , $G _ { k } ^ { * } ( Q _ { k } ^ { * } ( x ) ) = x$ . By the optimality of $\widehat { \mathbf { G } }$ , $\widehat { \mathbf { Q } }$ and $\widehat { \mathbf { v } }$ for the training objective, we can get that

$$
\begin{array} { r l } & { \displaystyle \sum _ { k = 1 } ^ { K } \left\{ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| ^ { 2 } \rho _ { k } ( X _ { i } ) + \lambda _ { k } \cdot \operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \widehat { \nu } _ { k } ( z ) { \mathrm { d } } z - \int f ( z ) \widetilde { \nu } _ { k , \widehat { Q } _ { k } } ( z ) { \mathrm { d } } z \Big ) \right\} } \\ & { \leq \displaystyle \sum _ { k = 1 } ^ { K } \lambda _ { k } \cdot \operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \nu _ { k } ^ { * } ( z ) { \mathrm { d } } z - \int f ( z ) \widetilde { \nu } _ { k , Q _ { k } ^ { * } } ( z ) { \mathrm { d } } z \Big ) , } \end{array}
$$

$\begin{array} { r } { \nu _ { k } ^ { * } = ( Q _ { k } ^ { * } ) _ { \# } ( \frac { \mu ^ { * } \rho _ { k } } { p _ { k } } ) } \end{array}$

Lemma 3. For any fixed $c _ { 1 }$ and $c _ { 2 }$ , define

Then there exists a constant $c _ { 3 }$ such that it holds with probability larger than $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $k \in [ K ]$ ,

$$
\operatorname* { s u p } _ { Q \in \widetilde { \mathcal { Q } } _ { k } f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \nu _ { k , Q } ^ { * } ( z ) \mathrm { d } z - \int f ( z ) \widetilde { \nu } _ { k , Q } ( z ) \mathrm { d } z \Big ) \leq c _ { 4 } \Big ( n ^ { - \frac { \bar { \alpha } + 1 } { 2 \bar { \alpha } + d } } + \frac { \log n } { \sqrt { n } } \Big ) ,
$$

where $\widetilde { \nu } _ { k , Q }$ can either be the kernel density estimator in (7) or wavelet estimator in (8).

So we choose $\begin{array} { r } { \lambda _ { k } = \lambda = \left( n ^ { - \frac { { \bar { \alpha } } + 1 } { 2 { \bar { \alpha } } + d } } + \frac { \log { n } } { \sqrt { n } } \right) ^ { - 1 } \cdot n ^ { - \frac { 2 \beta } { d } - 1 } } \end{array}$ − 2βd −1 for any k ∈ [K], then by the second statement of

Lemma 3 and $Q _ { k } ^ { * } \in \widetilde { \mathcal { Q } } _ { k }$ , it holds with probability larger than $1 - M n ^ { - 2 }$ that,

$$
\begin{array} { r l } & { \displaystyle \sum _ { k = 1 } ^ { K } \left\{ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| ^ { 2 } \rho _ { k } ( X _ { i } ) + \lambda \cdot \operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \big ( \displaystyle \int f ( z ) \widehat { \nu } _ { k } ( z ) { \mathrm { d } } z - \int f ( z ) \widetilde { \nu } _ { k , \widehat { Q } _ { k } } ( z ) { \mathrm { d } } z \big ) \right\} } \\ & { \leq C \lambda \cdot \big ( n ^ { - \frac { \bar { \alpha } + 1 } { 2 \hat { \alpha } + d } } + \frac { \log n } { \sqrt { n } } \big ) . } \end{array}
$$

So it holds with probability larger than $1 - M n ^ { - 2 }$ that for any $k \in \lfloor K \rfloor$ ,

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| ^ { 2 } \rho _ { k } ( X _ { i } ) \leq C n ^ { - \frac { 2 \beta } { d } - 1 } ,
$$

and

$$
\operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \widehat { \nu } _ { k } ( z ) \mathrm { d } z - \int f ( z ) \widetilde { \nu } _ { k , \widehat { Q } _ { k } } ( z ) \mathrm { d } z \Big ) \leq C \Big ( n ^ { - \frac { \bar { \alpha } + 1 } { 2 \tilde { \alpha } + d } } + \frac { \log n } { \sqrt { n } } \Big ) .
$$

Then we use the following lemma for bounding the population level reconstruction error.

Lemma 4. For the estimator $\widehat { \mathbf { G } }$ and $\widehat { \mathbf { Q } }$ , there exist positive constants $N$ , $c _ { 1 }$ , $c _ { 2 }$ and $c _ { 3 }$ such that when $n \geq N$ , for any $k \in \lfloor K \rfloor$ ,

(2). if (1). it holds with probability larger than $\tilde { \alpha } > 0$ , then it holds with probability larger than $1 - c _ { 1 } n ^ { - 3 }$ that $\begin{array} { r } { \mathbb { E } [ \| X - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X ) ) \| _ { 2 } { \cdot } \rho _ { k } ( X ) ] \le c _ { 2 } n ^ { - \frac { \beta } { d } } \vee \frac { \log n } { \sqrt { n } } . } \end{array}$ $1 - c _ { 1 } n ^ { - 3 }$ that the density $\nu _ { k , \widehat { Q } _ { k } } ^ { * }$ nof ; $\begin{array} { r } { ( \widehat { Q } _ { k } ) _ { \# } \left( \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } \right) } \end{array}$ exists and belongs to $C _ { c _ { 3 } } ^ { \tilde { \alpha } } ( \mathbb { R } ^ { d } )$ .

Then by Lemma 3 and second statement of Lemma 4, there exist constants $c , c _ { 1 }$ such that it holds with probability larger than $1 - c n ^ { - 2 }$ that

$$
\operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \nu _ { k , \widehat { Q } _ { k } } ^ { * } ( z ) \mathrm { d } z - \int f ( z ) \widetilde { \nu } _ { k , \widehat { Q } _ { k } } ( z ) \mathrm { d } z \Big ) \leq c _ { 1 } \Big ( n ^ { - \frac { \alpha + 1 } { 2 \widehat { \alpha } + d } } + \frac { \log n } { \sqrt { n } } \Big ) .
$$

So combined with equation (10), (11) and (12), it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n } }$ that

$$
\begin{array} { r l } { \varepsilon ^ { \prime \prime } \in \mathcal { S } _ { \varepsilon } ^ { \varepsilon } } & { = \varepsilon ^ { \prime \prime } , \rho _ { \varepsilon } ^ { \prime \prime } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } } \\ & { \quad + \varepsilon ^ { \prime } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } \mathrm { S } _ { \varepsilon } ^ { \varepsilon } } \\  \varepsilon ^ { \prime } \mathrm { S } _  \ \end{array}
$$

where $( i )$ uses Bernstein’s inequality to obtain that $\left| { \widehat { p } } _ { k } - p _ { k } \right| \leq C \sqrt { \frac { \log n } { n } }$ log nn holds with probability at least $1 - n ^ { - 3 }$ , and $( i i )$ uses the fact that $\beta \geq 1$ .

Then we consider the case $\alpha = 0$ . Define $\begin{array} { r } { \widetilde { \nu } _ { k , Q } = \frac { 1 } { \widehat { p } _ { k } n } \sum _ { i = 1 } ^ { n } \delta _ { Q ( X _ { i } ) } \rho _ { k } \bigl ( X _ { i } \bigr ) } \end{array}$ . For any $f \in \operatorname { L i p } _ { 1 } ( \mathbb { R } ^ { d } )$ , we have

$$
\int f ( z ) \mathrm { d } \widetilde { \nu } _ { k , Q } = \frac { 1 } { \widehat { p } _ { k } n } \sum _ { i = 1 } ^ { n } f ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) .
$$

Then we have the following lemma.

Lemma 5. There exists a constant c so that it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\operatorname* { s u p } _ { Q \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) } \operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \frac { 1 } { p _ { k } } \int f ( Q ( x ) ) \rho _ { k } ( x ) \mathrm { d } \mu ^ { * } - \int f ( z ) \tilde { \nu } _ { k , Q } ( z ) \mathrm { d } z \Big ) \leq c \Big ( \frac { \log n } { \sqrt { n } } + n ^ { - \frac { 1 } { d } } \Big ) .
$$

Then by Lemma 5 and equation (9), choose $\begin{array} { r } { \lambda _ { k } = \lambda = \left( n ^ { - \frac { 1 } { d } } + \frac { \log n } { \sqrt { n } } \right) ^ { - 1 } \cdot n ^ { - \frac { 2 \beta } { d } - 1 } } \end{array}$ , we have that statement (10) holds and

$$
\operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( z ) \widehat { \nu } _ { k } ( z ) \mathrm { d } z - \int f ( z ) \widetilde { \nu } _ { k , \widehat { Q } _ { k } } ( z ) \mathrm { d } z \Big ) \leq C \Big ( n ^ { - \frac { 1 } { d } } + \frac { \log n } { \sqrt { n } } \Big ) .
$$

Then by Lemma 4, we have

$$
\mathbb { E } [ \| X - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X ) ) \| _ { 2 } \rho _ { k } ( X ) ] \le c _ { 2 } n ^ { - \frac { \beta } { d } } \vee \frac { \log n } { \sqrt { n } } .
$$

So combined with Lemma 5, following equation (13), we have

$$
\begin{array} { r l } & { W _ { 1 } ( \widehat { \mu } , \mu ^ { * } ) \leq C \sqrt { \displaystyle \frac { \log n } { n } } + 2 \sum _ { k = 1 } ^ { K } \mathbb { E } _ { \mu ^ { * } } \Big [ \| X - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X ) ) \| \cdot \rho _ { k } ( X ) \Big ] } \\ &  \qquad + \displaystyle \sum _ { k = 1 } ^ { K } \operatorname* { s u p } _ { f \in \mathrm { L i p } _ { 1 } \{ [ \mathcal { D } _ { k } ( \mathcal { Q } _ { k } ( 2 ) ) \nu _ { k , \widehat { Q } _ { k } } ^ { * } ( \mathcal { Q } _ { k } ( \mathcal { Q } ) ] - \int f ( \widehat { G } _ { k } ( \mathcal { Q } ) ) \widehat { \nu } _ { k } ( \mathcal { Q } ) \mathrm { d } z )  } \\ & { \qquad \leq C _ { 1 } n ^ { - \frac { \rho } { \alpha } } \vee \displaystyle \frac { \log n } { \sqrt { n } } + C _ { 2 } \sum _ { k = 1 } ^ { K } \Big [ _ { f \in \mathrm { L i p } _ { 1 } \{ \mathcal { R } ^ { * } ( \mathcal { Q } ) \} } \Big ( \int f ( \mathcal { Q } ) \nu _ { k , \widehat { G } _ { k } } ^ { * } ( \mathcal { Q } ) \mathrm { d } z - \int f ( \mathcal { Z } ) \overline { { \nu } } _ { k , \widehat { G } _ { k } } ( \mathcal { z } ) \mathrm { d } z \Big ) } \\ & { \qquad +  \operatorname* { s u p } _ { f \in \mathrm { L i p } \{ ( \mathcal { D } _ { k } ^ { * } ) ( \mathcal { T } f ) \overline { { \nu } } _ { k , \widehat { G } _ { k } } ( \mathcal { Z } ) \mathrm { d } z - \int f ( \mathcal { Z } ) \widehat { \nu } _ { k } ( \mathcal { Z } ) \mathrm { d } z ) \Big ] } } \\ &  \qquad \leq C _ { 2 } n ^ { - \frac { 1 } { \alpha } } \vee \displaystyle \frac { \log n }  \ \end{array}
$$

# C.1 Proof of Lemma 3: kernel density estimator

Fix an arbitrary $k \in [ K ]$ . Since $\widetilde { \mathcal { Q } } _ { k } \subseteq C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ , it holds that for any $Q \in \widetilde { \mathcal { Q } } _ { k }$ , $\nu _ { k , Q } ^ { * } \in C _ { L } ^ { \tilde { \alpha } } ( \mathbb { R } ^ { d } )$ and $\mathrm { s u p p } ( \nu _ { k , Q } ^ { * } ) \in [ - L , L ] ^ { d }$ , where $\nu _ { k , Q } ^ { * }$ is the density of the push-forward measure of $\frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } }$ by map $Q$ . Recall that

$$
\widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) = \frac { 1 } { n h ^ { d } } \sum _ { i = 1 } ^ { n } \widetilde { k } ( \frac { y - Q ( X _ { i } ) } { h } ) \rho _ { k } ( X _ { i } ) .
$$

Since $\nu _ { k , Q } ^ { * }$ and $\widetilde { \nu } _ { k , Q }$ are both compactly supported, there exists a constant $C$ so that for any $Q \in \widetilde { \mathcal { Q } } _ { k }$

$$
\operatorname* { s u p } _ { \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big ) \leq C \operatorname* { s u p } _ { f \in \mathbb { C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big )
$$

where $\begin{array} { r } { \mathbf { C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) = \{ f : \mathbb { R } ^ { d }  \mathbb { R } \vert \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d } } \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , \vert j \vert \leq 1 } \vert f ^ { ( j ) } ( z ) \vert \leq 1 \} } \end{array}$ . Then we consider $f \in { \bf C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } )$ , we can get

$$
\begin{array} { r l } & { \displaystyle \int f ( y ) v _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \widetilde v _ { k , Q } ( y ) \mathrm { d } y } \\ & { \displaystyle = \frac { 1 } { \widehat { p _ { k } } } \Big ( \int p _ { k } \cdot f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int \widehat { p _ { k } } \cdot f ( y ) \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big ) + \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y \cdot \big ( 1 - \frac { p _ { k } } { \widehat { p _ { k } } } \big ) } \\ & { \displaystyle \leq \frac { 1 } { \widehat { p _ { k } } } \Big | \int f ( y ) \cdot p _ { k } \cdot \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \cdot \mathbb { E } _ { X ^ { ( n ) } } \big [ \widehat { p _ { k } } \cdot \widetilde { \nu } _ { k , Q } ( y ) \big ] \mathrm { d } y \Big | } \\ & { \quad + \frac { 1 } { \widehat { p _ { k } } } \Big | \int f ( y ) \cdot \mathbb { E } _ { X ^ { ( n ) } } \big [ \widehat { p _ { k } } \cdot \widetilde { \nu } _ { k , Q } ( y ) \big ] \mathrm { d } y - \int f ( y ) \cdot \widehat { p _ { k } } \cdot \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big | + \underbrace { \big | 1 - \frac { p _ { k } } { \widehat { p _ { k } } } \big | } _ { ( \mathcal { C } ) } . } \end{array}
$$

First for term ( $C$ ),by Bernstein’s inequality, it holds with probability at least $1 - n ^ { - 3 }$ that $| p _ { k } - \widehat { p } _ { k } | \leq$ $C \sqrt { \frac { \log n } { n } }$ , then by $p _ { k } > 0$ , for large enough $n$ , we have $\begin{array} { r } { \left| 1 - \frac { p _ { k } } { \widehat { p } _ { k } } \right| \le C \sqrt { \frac { \log n } { n } } } \end{array}$ b. For bounding the term $( A )$ , we use a similar strategy as in the proof of Lemma 4.3 of Divol (2022). Recall $\begin{array} { r } { \nu _ { k , Q } ^ { * } = Q _ { \# } [ \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } ] } \end{array}$ , we can

write

$$
\begin{array} { r } { \displaystyle \int f ( y ) \cdot \mathbb { E } _ { X ^ { ( n ) } } \big [ \widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) \big ] \mathrm { d } y = \displaystyle \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \mathbb { E } _ { \mu ^ { * } } \big [ \widetilde { k } ( \frac { y - Q ( X ) } { h } ) \cdot \rho _ { k } ( X ) \big ] \mathrm { d } y } \\ { \displaystyle = \int \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } ( \frac { y - z } { h } ) \cdot p _ { k } \cdot \nu _ { k , Q } ^ { * } ( z ) \mathrm { d } z \mathrm { d } y } \end{array}
$$

Denote $v ( \cdot ) = p _ { k } \cdot \nu _ { k , Q } ^ { * } ( \cdot )$ , we can obtain

$$
\begin{array} { r l } & { \bigg | \displaystyle \int f ( y ) \cdot p _ { k } \cdot \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \cdot \mathbb { E } _ { X ^ { ( n ) } } \big [ \widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) \big ] \mathrm { d } y \bigg | } \\ & { = \Big | \displaystyle \int f ( y ) \cdot v ( y ) \mathrm { d } y - \int \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } ( \frac { y - z } { h } ) \cdot v ( z ) \mathrm { d } z \mathrm { d } y \bigg | } \\ & { = \Big | \displaystyle \int \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } ( \frac { y - z } { h } ) \cdot ( v ( z ) - v ( y ) ) \mathrm { d } z \mathrm { d } y \Big | . } \end{array}
$$

When $\lfloor \tilde { \alpha } \rfloor$ is even, denote $s = \lfloor \tilde { \alpha } \rfloor$ ; when $\lfloor \tilde { \alpha } \rfloor$ is odd, denote $s = \lfloor \tilde { \alpha } \rfloor - 1$ . Then using Taylor’s theorem, we can decompose

$$
v ( z ) - v ( y ) = \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { 1 \leq | j | < s } } \frac { v ^ { ( j ) } ( y ) } { j ! } \cdot ( z - y ) ^ { j } + \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { j \leq s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } v ^ { ( j ) } ( y + t ( z - y ) ) \mathrm { d } t \cdot ( z - y ) ^ { j } .
$$

Using the fact that for any $j \in  { \mathbb { N } } _ { 0 } ^ { d }$ with $1 \leq | j | \leq \lfloor \tilde { \alpha } \rfloor$ , $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \widetilde { k } ( z ) \cdot z ^ { j } \mathrm { d } z = 0 } \end{array}$ and $ { \widetilde { k } } ( \cdot ) =  { \widetilde { k } } ( - \cdot )$ , we can obtain

$$
\begin{array} { l } { \displaystyle \int \int f ( y ) \cdot \frac 1 { h ^ { d } } \cdot \widetilde k ( \frac { y - z } h ) \cdot \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | j | < s } } \frac { v ^ { ( j ) } ( y ) } { j ! } \cdot ( z - y ) ^ { j } \mathrm { d } z \mathrm { d } y } \\ { = \displaystyle \int \int f ( y ) \cdot \widetilde k ( z ) \cdot \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { j \in \mathbb { N } _ { 0 } ^ { d } } } \frac { v ^ { ( j ) } ( y ) } { j ! } \cdot z ^ { j } \cdot h ^ { | j | } \mathrm { d } z \mathrm { d } y = 0 , } \end{array}
$$

and

$$
\begin{array} { l l } { \displaystyle \int \int f ( y ) \cdot \frac 1 { h ^ { d } } \cdot \widetilde k ( \frac { y - z } h ) \cdot \sum _ { \scriptstyle j \in \mathbb { N } _ { 0 } ^ { d } \atop { \scriptstyle | j | = s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } v ^ { ( j ) } ( y ) \cdot ( z - y ) ^ { j } \mathrm { d } t \mathrm { d } z \mathrm { d } y } \\ { \displaystyle } \\ { \displaystyle } \\ { \displaystyle } \\ { \displaystyle } \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } & { \displaystyle \int \displaystyle \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \tilde { k } ( \frac { y - z } { h } ) \cdot ( v ( z ) - v ( y ) ) \mathrm { d } z \mathrm { d } y } \\ & { = \displaystyle \int \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \tilde { k } ( \frac { y - z } { h } ) \cdot \sum _ { \underbrace { j \in \mathbb { N } _ { 0 } ^ { d } } _ { \vert j \vert = s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } \big ( v ^ { ( j ) } ( y + t ( z - y ) ) - v ^ { ( j ) } ( y ) \big ) \cdot ( z - y ) ^ { j } \mathrm { d } t \mathrm { d } z \mathrm { d } y } \\ & { \overset { ( i ) } { = } \displaystyle \int \int f ( y ) \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \tilde { k } ( \frac { x - y } { t h } ) \cdot \sum _ { \underbrace { j \in \mathbb { N } _ { 0 } ^ { d } } _ { \vert j \vert = s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } \big ( v ^ { ( j ) } ( x ) - v ^ { ( j ) } ( y ) \big ) \cdot ( \frac { x - y } { t } \big ) ^ { j } \mathrm { d } t \mathrm { d } x \mathrm { d } y , } \end{array}
$$

where $( i )$ uses the change of variable $x = y + t ( z - y )$ and $ { \widetilde { k } } ( \cdot ) =  { \widetilde { k } } ( - \cdot )$ . Then by switching the variable $x$ and $y$ , using the facts that $s$ is a even number and $k$ is an even function, we have

$$
\begin{array} { r l } & { \displaystyle \int \int f ( y ) \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \tilde { k } ( \frac { x - y } { t h } ) \cdot \sum _ { i \neq j \atop j \in \mathbb { R } _ { s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } \big ( v ^ { ( j ) } ( x ) - v ^ { ( j ) } ( y ) \big ) \cdot \big ( \frac { x - y } { t } \big ) ^ { j } \mathrm { d } t \mathrm { d } x \mathrm { d } y } \\ & { \displaystyle = \int \int f ( x ) \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \tilde { k } ( \frac { y - x } { t h } ) \cdot \sum _ { j \in \mathbb { R } _ { s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } \big ( 1 - t ) ^ { s - 1 } \big ( v ^ { ( j ) } ( y ) - v ^ { ( j ) } ( x ) \big ) \cdot \big ( \frac { y - x } { t } \big ) ^ { j } \mathrm { d } t \mathrm { d } x \mathrm { d } y } \\ & { \displaystyle = - \int \int f ( x ) \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \tilde { k } ( \frac { x - y } { t h } ) \cdot \sum _ { j \in \mathbb { N } _ { s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } \big ( 1 - t ) ^ { s - 1 } \big ( v ^ { ( j ) } ( x ) - v ^ { ( j ) } ( y ) \big ) \cdot \big ( \frac { x - y } { t } \big ) ^ { j } \mathrm { d } t \mathrm { d } x \mathrm { d } y . } \end{array}
$$

Therefore, when $\lfloor \tilde { \alpha } \rfloor$ is even, we can obtain

$$
\begin{array} { r l } & { \displaystyle | \displaystyle \int \int f ( y ) \cdot \frac { 1 } { h ^ { 4 } } \cdot \widetilde { k } \frac { y ^ { y - \frac { z } { h } } } { h ^ { \frac { k } { 2 } } } \cdot ( w ( z ) - v ( y ) ) \pm z \mathrm { d } y | } \\ & { = \displaystyle | \frac { 1 } { 2 } \int \int ( f ( y ) - f ( x ) ) \cdot \frac { 1 } { l ^ { \frac { k } { 2 } } h ^ { \frac { k } { 2 } } } \cdot \widetilde { k } \frac { x ^ { \frac { x } { h } - y } } { l h } ) \cdot \displaystyle \sum _ { \frac { l , \phi \widetilde { x } } { l h ^ { \frac { k } { 2 } } } } \frac { \frac { \tilde { x } } { h } \int } { 1 } \int _ { 0 } ^ { \frac { 1 } { \tilde { x } } ( 1 - l ) ^ { s - 1 } \big ( v ^ { ( j ) } ( x ) - v ^ { ( j ) } ( y ) \big ) \cdot \big ( \frac { x - y } { l } \big ) ^ { j } \ : \mathrm { d } l \ : \mathrm { d } w }  } \\ & { \displaystyle = | \frac { 1 } { 2 } \int \int ( f ( y ) - f ( y + w h ) ) \cdot \widetilde { k } ( w ) \cdot \displaystyle \sum _ { \frac { l , \phi \widetilde { x } } { l ( w ) } } \frac { \tilde { x } } { j l } \int _ { 0 } ^ { \frac { 1 } { \tilde { x } } - 1 } \big ( v ^ { ( j ) } ( y + w h ) - v ^ { ( j ) } ( y ) \big ) \cdot ( w h ) ^ { j } \ : \mathrm { d } t \mathrm { d } w  } \\ &   \displaystyle \frac { ( \tilde { w } ) } { \widetilde { \mathcal { L } } } h ^ { 1 + \tilde { \alpha } } \cdot \displaystyle \sum _ { \frac { l , \phi \widetilde { x } } { l ( w ) } } \frac { \tilde { x } } { j l } \int _ { 1 - L - h , L + h \mathrm { d } } \int _ { \Gamma ( - 1 , 1 ) ^ { 1 / 2 } } | u | ^ { 1 + \tilde { \alpha } } \cdot \widetilde { k } ( w ) \cdot \int _ { 0 } ^ { 1 } ( 1 - t ) \end{array}
$$

where $( i i )$ uses $v ( \cdot ) = p _ { k } \cdot \nu _ { k , Q } ^ { * } ( \cdot )$ has support contained in $[ - L , L ] ^ { d }$ and $\widetilde { k } ( \cdot )$ has support contained in $[ - 1 , 1 ] ^ { d }$ . On the other hand, when $\lfloor \tilde { \alpha } \rfloor$ is odd, recall $s = \lfloor \tilde { \alpha } \rfloor - 1$ is even, we have

$$
\begin{array} { r l } & { \left| \int \int \hat { \rho } ( \omega ) \frac { 1 } { \omega ^ { 4 } } \hat { u } ^ { 2 } e ^ { - z \frac { \nu } { 2 } \hat { \rho } ( \omega ) } \langle \hat { \rho } ( z ) - \hat { \rho } ( z ) - \hat { \rho } ( y ) \rangle d z \right| } \\ & { = \frac { 1 } { 2 } \int \int ( \hat { \rho } ( \omega ) - \hat { \rho } ( y ) ) \cdot \frac { 1 } { \omega ^ { 4 } } e ^ { - z \frac { \nu } { 4 } \hat { \rho } ( \omega ) } \cdot \sum _ { n = 1 } ^ { \infty } \frac { \hat { \rho } } { \omega ^ { 4 } } \int _ { 0 } ^ { \frac { 1 } { \omega } } ( 1 - \hat { \rho } ^ { n - 1 } \hat { \rho } ( \hat { \rho } ( \hat { \rho } ( z ) - \hat { \rho } ^ { n } ( y ) ) \cdot ( \frac { z ^ { n - 1 } } { L } ) ) ^ { 2 } - \frac { \hat { \rho } } { 4 } ) ^ { n } \cdot \hat { \rho } ( \hat { \rho } ^ { n } ) \cdot \hat { \rho } ( \hat { \rho } ^ { n } ) } \\ & { \leq \frac { 1 } { 2 } \int \int ( \hat { \rho } ( \omega ) - \hat { \rho } ( y ) ) \cdot \frac { 1 } { \hat { \rho } ( z ) } e ^ { - z \frac { \nu } { 4 } \hat { \rho } ( \frac { \rho } { \omega } ) } \cdot \frac { \hat { \rho } ^ { \alpha } } { \hat { \rho } ( \hat { \rho } ^ { n } ) } } \\ &  \qquad \cdot \sum _ { n = 1 } ^ { \infty } \frac { \hat { \rho } } { \hat { \rho } ^ { n } } \int _ { 0 } ^ { \frac { 1 } { \omega } } ( 1 - \hat { \rho } ^ { n } ( \hat { \rho } ^ { n } ( z ) - \hat { \rho } ^ { n } ( y ) ) ) \cdot \frac { \hat { \rho } ^ { \alpha } } { \hat { \rho } ^ { n + 2 } } \cdot \hat { \rho } ( \hat { \rho } ( \hat { \rho } ^  n \end{array}
$$

Then for the term ( $D$ ), using Taylor’s theorem and $f \in { \bf C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } )$ , we can write

$$
f ( x ) - f ( y ) = \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | j | = 1 } } \int _ { 0 } ^ { 1 } f ^ { ( j ) } ( y + t ( x - y ) ) \mathrm { d } t \cdot ( x - y ) ^ { j } .
$$

So using the fact that for any $j \in \mathbb { N } _ { 0 } ^ { d }$ with $1 \leq | j | \leq \lfloor \tilde { \alpha } \rfloor + 1$ , $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \widetilde { k } ( z ) \cdot z ^ { j } \mathrm { d } z = 0 } \end{array}$ , we can obtain

$$
\begin{array} { r l } { { \displaystyle \int \int \displaystyle \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x d } } { | \varepsilon | = 1 } } } f ^ { ( l ) } ( y ) \cdot ( x - y ) ^ { l } \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \widetilde { k } ( \frac { x - y } { t h } ) \cdot \displaystyle \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x d } } { | \varepsilon | = s } } \frac { s } { j ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x d } } { | \varepsilon | = 1 } } \upsilon ^ { ( j + q ) } ( y ) \cdot ( x - y ) ^ { q } \cdot \big ( \frac { x - y } { t } \big ) ^ { \varepsilon } }  & { { \scriptstyle | \varepsilon \mathrm { e x d } | } } \\ { { \displaystyle = } } & { { \displaystyle \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x d } } { | \varepsilon | = 1 } } \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x d } } { | \varepsilon | = 1 } } \ \sum _ { \stackrel { \scriptstyle | \varepsilon \mathrm { e x } } { | \varepsilon | = 0 } } \int _ { 0 } ^ { 1 } \frac { 1 } { t ^ { d } h ^ { d } } \cdot \frac { s } { j ! } \cdot \displaystyle \int \int \int f ^ { ( l ) } ( y ) \cdot ( x - y ) ^ { l } \cdot \widetilde { k } ( \frac { x - y } { t h } ) ( 1 - t ) ^ { s - 1 } \upsilon ^ { ( j + q ) } ( y ) \cdot ( x - y ) ^ { q } \cdot \big ( \frac { x - y } { t } \big ) ^ { \varepsilon } } } & { { \scriptstyle | \varepsilon \mathrm { e x d } | } } \\ { { \displaystyle | t | = 1 | \ , \ | j | = s | \ } } & { { \scriptstyle | \varepsilon \mathrm { e x d } | } } & { { \scriptstyle | \varepsilon \mathrm { e x d } | } } \end{array}
$$

Therefore,

$$
\begin{array} { l } { ( D ) = \displaystyle | \frac { 1 } { 2 } \int \int \displaystyle \sum _ { \frac { t \neq \mathrm { e f f } } { t \neq h } } \int _ { 0 } ^ { 1 } ( f ^ { ( t ) } ( y + \omega ( x - y ) ) - f ^ { ( t ) } ( y ) ) \mathrm { d } \omega \cdot ( x - y ) ^ { t }  } \\ { \cdot \frac { 1 } { ( t ) + 1 } . } \\ { \cdot \frac { 1 } { t ^ { d } h ^ { d } } \cdot \overbrace { k ( \frac { x - y } { t h } ) } ^ { - 1 } \cdot \underbrace { \sum _ { \frac { s } { t \neq \mathrm { e f f } } } \frac { \delta } { y } } _ { s \mathrm { t i f } h } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { s - 1 } \displaystyle \sum _ { \frac { t \neq \mathrm { e f f } } { t \neq h } } v ^ { ( j + \dagger ) } ( y ) \cdot ( x - y ) ^ { \sigma } \cdot ( \frac { \overline { { x - y } } } { t } ) ^ { i } \mathrm { d } t \mathrm { d } x \mathrm { d } y | } \\ { \displaystyle  \overset { ( i i i ) } { = } | \frac { 1 } { 2 } \int \int \displaystyle \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \sum _ { \frac { t \neq \mathrm { e f f } } { t \neq h } } ( f ^ { ( t ) } ( \theta ) - f ^ { ( t ) } ( y ) ) \cdot ( \frac { \theta - y } { \omega } ) ^ { t }  } \\  \cdot \frac { 1 } {  \omega ^ { d } d t  } \cdot \widetilde { k } _ { t } ^ { ( \frac { \theta - y } { \omega + h } ) } \cdot \displaystyle \sum _ { \frac { s } { s \mathrm { e f f } } } \frac { \delta } { t } ( 1 - t ) ^ { s - 1 } \displaystyle \sum _ { \frac { t \neq \mathrm { e f f } } { t \neq h } } v ^ { ( j + \dagger ) } ( y ) \cdot ( \frac { \theta - y } { \omega } ) ^ { \sigma } \cdot ( \frac { \theta - y } { \omega } ) ^ { i } \cdot ( \frac  \theta  \end{array}
$$

where $( i i i )$ uses the change of variable $y + \omega ( x - y ) = \theta$ . By switching the variable $\theta$ and $y$ , we have

$$
\begin{array} { r l } & { \displaystyle \int \int \int _ { 0 } ^ { 1 } \int _ { \infty } ^ { 1 } \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \sum _ { n = 0 } ^ { \infty } | \partial ^ { 2 } u | ^ { 3 } \cdot \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \big | ^ { 2 } } \\ & { \quad - \frac { 1 } { \omega ^ { 4 } \partial u ^ { 3 } } \cdot \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \cdot \frac { \partial ^ { 3 } u } { \partial u ^ { 3 } } \big | ^ { 2 } } \\ & { \quad - \displaystyle \int \int \int _ { 0 } ^ { 1 } \int _ { \infty } ^ { 1 } \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \cdot \frac { \partial ^ { 3 } u } { \partial u ^ { 3 } } ( 1 - u ^ { 3 } ) ^ { n - 1 } \sum _ { n = 0 } ^ { \infty } u ^ { 3 + \omega } \partial u \cdot ( \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } ) ^ { n } \cdot \frac { ( \partial ^ { 2 } u - \partial ^ { 3 } u ) ^ { n } ( \partial u + \partial u ) \cdot \big ( \partial ^ { 2 } u \big ) } { \partial u ^ { 3 } } } \\ & { \quad - \displaystyle \int \int \int _ { 0 } ^ { 1 } \int _ { \infty } ^ { 1 } \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \cdot \frac { \partial ^ { 3 } u } { \partial u ^ { 3 } } ( 1 - u ^ { 3 } ) ^ { n } \cdot \frac { ( \partial ^ { 2 } u - \partial ^ { 3 } u ) ^ { n } } { \partial u ^ { 3 } } } \\ & { \quad - \frac { 1 } { \omega ^ { 4 } \partial u ^ { 3 } } \cdot \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \cdot \frac { \partial ^ { 3 } u } { \partial u ^ { 3 } } \big | ^ { 2 } \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } - \frac { \partial ^ { 2 } u } { \partial u ^ { 3 } } \big | ^ { 2 } } \\ &  \quad - \displaystyle \int \end{array}
$$

which leads to

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { 2 } \int \int \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \sum _ { \omega \in \mathbb { R } _ { + } ^ { d } } \big ( f ^ { ( l l ) } ( \theta ) - f ^ { ( l ) } ( y ) \big ) \cdot \big ( \frac { \theta - y } { \omega } \big ) ^ { l } } \\ & { \quad \cdot \frac { 1 } { | \omega | ^ { d + 1 } h ^ { d } } \cdot \tilde { k } \big ( \frac { \theta - y } { \omega | h | } \big ) \cdot \sum _ { \frac { \theta \in \mathbb { R } ^ { d + 1 } } { | \omega | ^ { d + 1 } } } \sum _ { \frac { \theta \in \Theta } { | \omega | } } \big ( y + \theta ^ { ( l + d ) } ( y ) \cdot \big ( \frac { \theta - y } { \omega } \big ) ^ { a } \cdot \big ( \frac { \theta - y } { \omega l } \big ) ^ { j } \mathrm { d } \omega \mathrm { d } t \mathrm { d } \theta \mathrm { d } \theta \big ] , } \\ & { = \displaystyle | \frac { 1 } { 4 } \int \int \int _ { 0 } ^ { 1 } \int _ { 0 } ^ { 1 } \sum _ { \frac { l \in \mathbb { R } _ { + } ^ { d } } { | \omega | ^ { d + 1 } } } \big ( f ^ { ( l l ) } ( \theta ) - f ^ { ( l l ) } ( y ) \big ) \cdot \big ( \frac { \theta - y } { \omega } \big ) ^ { l } } \\ &  \quad \cdot \frac { 1 } { \omega ^ { d + d + h ^ { d } } h ^ { d } } \cdot \tilde { k } \big ( \frac { \theta - y } { \omega | h | } \big ) \cdot \sum _ { \frac { l \in \mathbb { R } ^ { d + 1 } } { | \omega | ^ { d + 1 } } } \sum _ { \frac { \theta \in \Theta } { | \omega | } } \big ( \sigma ^ { ( l + d ) } ( y ) - v ^ { ( l + d ) } ( \theta ) \big ) \cdot \big ( \frac { \theta - y } { \omega } \big ) ^ { a } \cdot \big ( \frac { \theta - y } { \omega l } \big ) ^ { j } \mathrm { d } \omega \mathrm \end{array}
$$

. h 1+ ˜α ,

where the last inequality uses the fact that $s = \lfloor \tilde { \alpha } \rfloor - 1$ and $\upsilon$ is $\ddot { \alpha }$ is smooth. We can then obtain that

$$
( A ) \lesssim n ^ { - \frac { \tilde { \alpha } + 1 } { 2 \tilde { \alpha } + d } } .
$$

It remains to bound term ( $B$ ), which is

$$
\begin{array} { l } { ( B ) = \displaystyle \bigg | \displaystyle \int f ( y ) \cdot \mathbb { E } _ { X ^ { ( \ast ) } } \big [ \widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) \big ] \mathrm { d } y - \displaystyle \int f ( y ) \cdot \widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \bigg | } \\ { \displaystyle \quad = \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } \big ( \frac { y - Q ( X _ { i } ) } { h } \big ) \cdot \rho _ { k } ( X _ { i } ) \mathrm { d } y - \mathbb { E } _ { \mu ^ { \ast } } \bigg [ \displaystyle \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } \big ( \frac { y - Q ( X ) } { h } \big ) \cdot \rho _ { k } ( X ) \mathrm { d } y } \end{array}
$$

By standard symmetrization, we can get

$$
\begin{array} { r l }   { \mathbb { z } \Bigg [ \operatorname* { s u p } _ { \stackrel { f \in \mathcal { S } _ { k } } { Q \in \mathcal { Q } _ { k } } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \tilde { k } \big ( \frac { y - Q ( X _ { i } ) } { h } \big ) \cdot \rho _ { k } ( X _ { i } ) \mathrm { d } y - \mathbb { E } \bigg [ \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot k \big ( \frac { y - Q ( X ) } { h } \big ) \cdot \rho _ { k } ( X ) \mathrm { d } y } \\ & { \leq 2 \mathbb { E } \bigg [ \operatorname* { s u p } _ { \stackrel { f \in \mathcal { S } _ { 1 } ( \tilde { \tilde { \alpha } } ^ { d } ) } { Q \in \mathcal { Q } _ { k } } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \tilde { k } \big ( \frac { y - Q ( X _ { i } ) } { h } \big ) \cdot \rho _ { k } ( X _ { i } ) \mathrm { d } y \bigg | \bigg ] , } \end{array}
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from Rademacher distribution, i.e. $P ( \varepsilon _ { i } = 1 ) = P ( \varepsilon _ { i } = - 1 ) = 0 . 5$ Define function set

$$
\mathcal F = \left\{ f : \mathcal M \to \mathbb R \mid f ( x ) = \int g ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde k ( \frac { y - Q ( x ) } { h } ) \cdot \rho _ { k } ( x ) \mathrm { d } y ; g \in \mathbf C _ { 1 } ^ { 1 } ( \mathbb R ^ { d } ) ; Q \in \widetilde { \mathcal Q } _ { k } \right\} .
$$

Since there exists a constant $L$ so that $\operatorname { s u p p } ( Q ) = [ - L , L ] ^ { d }$ , we can first consider the function set

$$
\mathcal { F } _ { 1 } = \left\{ f : [ - L , L ] ^ { d } \to \mathbb { R } \mid f ( z ) = \int g ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } \big ( \frac { y - z } { h } \big ) { \mathrm { d } } y ; g \in \mathbf { C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) \right\} .
$$

For any $f \in \mathcal { F } _ { 1 }$ and $j \in  { \mathbb { N } } _ { 0 } ^ { d }$ with $1 \leq | j | \leq \lfloor { \frac { d } { 2 } } \rfloor$ , we have

$$
\begin{array} { l } { { f ^ { ( j ) } ( z ) = \displaystyle \int g ( y ) \frac { 1 } { h ^ { d + \vert j \vert } } \widetilde { k } ^ { ( j ) } ( \frac { z - y } { h } ) \mathrm { d } y } } \\ { { \displaystyle \quad = \frac { 1 } { h ^ { \vert j \vert } } \int g ( z - h t ) \widetilde { k } ^ { ( j ) } ( t ) \mathrm { d } t } . } \end{array}
$$

Since $| j | \geq 1$ , there exists $j _ { 1 } \in \mathbb { N } _ { 0 } ^ { d }$ with $| j _ { 1 } | = 1$ so that every element in $j - j _ { 1 }$ is non-negative. Then we have

$$
| f ^ { ( j ) } ( z ) | = \left| \frac { 1 } { h ^ { | j | - 1 } } \int g ^ { ( j _ { 1 } ) } ( z - h t ) \widetilde { k } ^ { ( j - j _ { 1 } ) } ( t ) \mathrm { d } t \right| \lesssim \frac { 1 } { h ^ { | j | - 1 } } ,
$$

where the last inequality uses $g \in { \bf C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } )$ . Moreover, when $d \geq 2$ , for any $j \in \mathbb { N } _ { 0 } ^ { d }$ with $\left| j \right| = \left\lfloor { \frac { d } { 2 } } \right\rfloor$ and $z _ { 1 } , z _ { 2 } \in \mathbb { R } ^ { d }$ it holds that

$$
\begin{array} { l } { { \displaystyle { \cal F } ^ { ( j ) } ( z _ { 1 } ) - f ^ { ( j ) } ( z _ { 2 } ) \big \vert = \Big \vert \displaystyle { \frac { 1 } { h ^ { \lfloor \frac { q } { 2 } \rfloor - 1 } } \int _ { 0 } ^ { q ( j _ { 1 } ) } ( z _ { 1 } - h t ) \widetilde { k } ^ { ( j - j _ { 1 } ) } ( t ) \mathrm { d } t } - \displaystyle { \frac { 1 } { h ^ { \lfloor \frac { q } { 2 } \rfloor - 1 } } \int _ { 0 } ^ { g ( j _ { 1 } ) } ( z _ { 2 } - h t ) \widetilde { k } ^ { ( j - j _ { 1 } ) } ( t ) \mathrm { d } t } \Big \vert } } \\  { \displaystyle ~ = \Big \vert \displaystyle { \frac { 1 } { h ^ { \lfloor \frac { q } { 2 } \rfloor - 1 } } \int _ { \mathbb { \displaystyle { \hat { h } } } ^ { 1 } d } g ^ { ( j _ { 1 } ) } ( y ) \big ( \widetilde { k } ^ { ( j - j _ { 1 } ) } \big ( \displaystyle { \frac { z _ { 1 } - y } { h } \big ) - \widetilde { k } ^ { ( j - j _ { 1 } ) } ( \displaystyle { \frac { z _ { 2 } - y } { h } \big ) } \big ) \mathrm { d } y } \Big \vert } } \end{array}
$$

If $\| z _ { 1 } - z _ { 2 } \| \leq h$ , then

$$
\begin{array} { r l } & { | f ^ { ( j ) } ( z _ { 1 } ) - f ^ { ( j ) } ( z _ { 2 } ) | = \Big | \displaystyle \frac { 1 } { h ^ { \lfloor \frac { d } { 2 } \rfloor - 1 } } \int \frac { 1 } { h ^ { d } } g ^ { ( j _ { 1 } ) } ( y ) \big ( \widetilde { k } ^ { ( j - j _ { 1 } ) } ( \frac { z _ { 1 } - y } { h } ) - \widetilde { k } ^ { ( j - j _ { 1 } ) } ( \frac { z _ { 2 } - y } { h } ) \big ) \mathrm { d } y \Big | } \\ & { \qquad \le C \displaystyle \frac { 1 } { h ^ { \lfloor \frac { d } { 2 } \rfloor } } \| z _ { 1 } - z _ { 2 } \| \le C \displaystyle \frac { 1 } { h ^ { \frac { d } { 2 } - 1 } } \| z _ { 1 } - z _ { 2 } \| ^ { \frac { d } { 2 } - \lfloor \frac { d } { 2 } \rfloor } ; } \end{array}
$$

If $\| z _ { 1 } - z _ { 2 } \| \geq h$ , then

$$
| f ^ { ( j ) } ( z _ { 1 } ) - f ^ { ( j ) } ( z _ { 2 } ) | \leq | f ^ { ( j ) } ( z _ { 1 } ) | + | f ^ { ( j ) } ( z _ { 2 } ) | \leq C { \frac { 1 } { h ^ { \lfloor { \frac { d } { 2 } } \rfloor - 1 } } } \leq C { \frac { 1 } { h ^ { { \frac { d } { 2 } } - 1 } } } \| z _ { 1 } - z _ { 2 } \| ^ { { \frac { d } { 2 } } - \lfloor { \frac { d } { 2 } } \rfloor } .
$$

So we can get when $d \geq 2$ , there exists a constant $C$ such that for any $f \in \mathcal { F } _ { 1 }$ , it holds that

$$
C h ^ { \frac { d } { 2 } - 1 } f \in C _ { 1 } ^ { \frac { d } { 2 } } ( [ - L , L ] ^ { d } ) .
$$

Similarly, when $d = 1$ , we have for any $z _ { 1 } , z _ { 2 } \in \mathbb { R } ^ { d }$ it holds that

$$
| f ( z _ { 1 } ) - f ( z _ { 2 } ) | = { \big | } \int ( g ( z _ { 1 } - h t ) - g ( z _ { 2 } - h t ) ) \cdot { \widetilde { k } } ( t ) \mathrm { d } y { \big | } \lesssim \| z _ { 1 } - z _ { 2 } \| .
$$

Therefore, we can conclude that

$$
\mathcal { F } _ { 1 } \in C _ { L _ { 1 } h ^ { - ( \frac { d } { 2 } - 1 ) } + } ^ { \frac { d } { 2 } } ( [ - L , L ] ^ { d } ) ,
$$

for a constant $L _ { 1 }$ , where $( a ) _ { + } = \operatorname* { m a x } ( a , 0 )$ . So for any $\epsilon > 0$ , we can find a set $N _ { \epsilon } ^ { f } \subseteq \mathcal { F } _ { 1 }$ such that q log |N f | . h−( d2 −1)+ and for any $f \in \mathcal { F } _ { 1 }$ , there exists $\widetilde { f } \in N _ { \epsilon } ^ { f }$ such that

$$
\operatorname* { s u p } _ { y \in [ - L , L ] ^ { d } } | f ( y ) - { \widetilde { f } } ( y ) | \leq \epsilon .
$$

Then, to derive an $\epsilon$ -covering number for $\mathcal { F }$ , we introduce the following lemma.

Lemma 6. (Lemma 12 of Tang $\mathcal { E A }$ Yang (2022)) Let $\mathcal { X } _ { G } = \left\{ \boldsymbol { x } \in \mathbb { R } ^ { D } : \boldsymbol { x } = G ( \boldsymbol { z } ) , \boldsymbol { z } \in \mathbb { B } _ { 1 } ^ { d } \right\}$ be a $d$ - dimensional submanifold induced by a Lipschitz continuous map $G : \mathbb { R } ^ { d }  \mathbb { R } ^ { D }$ , then it holds for any $\widetilde { \gamma } > 0$ that

$$
\log \mathbf { N } \big ( C _ { 1 } ^ { \widetilde { \gamma } } ( \mathbb { R } ^ { D } ) , \| \cdot \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } , \epsilon \big ) \leq C \epsilon ^ { - \frac { d } { \widetilde { \gamma } } } , \quad \forall \epsilon > 0 ,
$$

where $\mathbf { N } ( \mathcal { F } , \widetilde { d } , \epsilon )$ denotes the $\epsilon$ -covering number of function space $\mathcal { F }$ with respect to pseudo-metric $\hat { d }$ , and $\| f \| _ { L ^ { \infty } ( \mathcal { X } _ { G } ) } = \operatorname* { s u p } _ { x \in \mathcal { X } _ { G } } \left| f ( x ) \right|$ denotes the functional supreme norm constrained on set $\chi _ { G }$ .

Then since $\Omega _ { k } = Q _ { k } ^ { * } ( \mathcal { M } \cap S _ { k } )$ is compactly supported and $\mathcal { M } \cap S _ { k } = G _ { k } ^ { \ast } ( \Omega _ { k } )$ , for any $\epsilon > 0$ , we can

find a function set $N _ { \epsilon } ^ { Q }$ such that $\sqrt { \log | N _ { \epsilon } ^ { Q } | } \lesssim ( \frac { 1 } { \epsilon } ) ^ { \frac { d } { 2 \beta } }$ and for any $Q \in \widetilde { \mathcal { Q } } _ { k }$ , there exists $\widetilde Q \in N _ { \epsilon } ^ { Q }$ such that

$$
\operatorname* { s u p } _ { x \in \mathcal { M } \cap { S _ { k } } } \| \widetilde { Q } ( x ) - Q ( x ) \| \le \epsilon .
$$

Then for any $Q \in \bar { \mathcal { Q } } _ { k }$ and $f \in { \mathcal { F } } _ { 1 }$ , there exists $\widetilde Q \in N _ { \epsilon } ^ { Q }$ , $\widetilde { f } \in N _ { \epsilon } ^ { f }$ and a constant $c$ such that

$$
\begin{array} { r l } & { \Big | f ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( \widetilde { Q } ( x ) ) \rho _ { k } ( x ) \Big | } \\ & { \le \Big | f ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( Q ( x ) ) \rho _ { k } ( x ) \Big | + \Big | \widetilde { f } ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( \widetilde { Q } ( x ) ) \rho _ { k } ( x ) \Big | } \\ & { \le c \epsilon . } \end{array}
$$

So we can get

$$
\log \mathbf { N } ( \mathcal { F } , \epsilon , \Vert \cdot \Vert _ { \infty } ) \lesssim \left( \frac { 1 } { \epsilon } \right) ^ { \frac { d } { \beta } } + \left( \frac { h ^ { - ( \frac { d } { 2 } - 1 ) _ { + } } } { \epsilon } \right) ^ { 2 } .
$$

Choose $\begin{array} { r } { \delta = \left( \frac { 1 } { n } \right) ^ { \frac { \tilde { \alpha } + 1 } { 2 \tilde { \alpha } + d } } \vee \left( \frac { 1 } { n } \right) ^ { \frac { \beta } { d } } } \end{array}$ , we can get

$$
\begin{array} { l } { \displaystyle \frac { 1 } { \sqrt { n } } \int _ { \delta } ^ { 1 } \left[ \left( \frac { 1 } { \epsilon } \right) ^ { \frac { d } { 2 \beta } } + \frac { h ^ { 1 - \frac { d } { 2 } } \vee 1 } { \epsilon } \right] \mathrm { d } \epsilon } \\ { \displaystyle \lesssim \frac { \log n } { \sqrt { n } } + ( \frac { 1 } { n } ) ^ { \frac { \tilde { \alpha } + 1 } { 2 \tilde { \alpha } + d } } + ( \frac { 1 } { n } ) ^ { \frac { \beta } { d } } . } \end{array}
$$

By Dudley’s entropy integral bound (see for example, Theorem 5.22 of Wainwright (2019)), it holds that

$$
\begin{array} { r l } & { \mathbb { E } \bigg [ \underset { f \in \mathbf { C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \int f ( y ) \cdot \frac { 1 } { h ^ { d } } \cdot \widetilde { k } \big ( \frac { y - Q ( X _ { i } ) } { h } \big ) \cdot \rho _ { k } ( X _ { i } ) \mathrm { d } y \bigg | \bigg ] } \\ & { \lesssim \frac { \log n } { \sqrt { n } } + \big ( \frac { 1 } { n } \big ) ^ { \frac { \widetilde { \alpha } + 1 } { 2 \widetilde { \alpha } + d } } + \big ( \frac { 1 } { n } \big ) ^ { \frac { \beta } { d } } . } \end{array}
$$

The statement is then followed by Talagrand concentration inequality (see for example, Theorem 3.27 of Wainwright (2019)) and the fact that $\tilde { \alpha } + 1 \le \beta$ .

# C.2 Proof of Lemma 3: Wavelet estimator

Fix an arbitrary $k \in \lfloor K \rfloor$ . Since $\widetilde { \mathcal { Q } } _ { k } \subseteq C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } )$ , it holds that for any $Q \in \widetilde { \mathcal { Q } } _ { k }$ , $\mathrm { s u p p } ( \nu _ { k , Q } ^ { * } ) \subseteq [ - L , L ] ^ { d }$ , where $\nu _ { k , Q } ^ { * }$ is the density of the push-forward measure of $\frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } }$ by map $Q$ . Moreover, by $\nu _ { k , Q } ^ { * } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ with support contained in $[ - L , L ] ^ { d }$ and $0 < p _ { k } = \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ] \le 1$ , we can write $p _ { k } \cdot \nu _ { k , Q } ^ { * } ( y )$ as

$$
p _ { k } \cdot \nu _ { k , Q } ^ { * } ( y ) = \sum _ { m \in \mathbb { S } } a _ { m } ^ { Q } \phi _ { m } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { + \infty } \sum _ { m \in \mathbb { S } _ { l j } } \theta _ { l j m } ^ { Q } \psi _ { l j m } ( y ) ,
$$

where $\{ \phi _ { m } , \psi _ { l j m } : l = 1 , \cdot \cdot \cdot , 2 ^ { d } - 1 , j \in \mathbb { N } , m \in \mathbb { Z } ^ { d } \}$ is the orthonormal wavelet basis for Besov space on $\mathbb { R } ^ { d }$ defined as $\phi _ { m } ( y ) = \phi ( y - m )$ and $\psi _ { l j m } ( y ) = 2 ^ { \frac { j d } { 2 } } \psi _ { l } ( 2 ^ { j } y - m )$ , and it holds that $\phi ( \cdot )$ and $\psi _ { l } ( \cdot )$ for any $1 \leq l \leq 2 ^ { d } - 1$ are compactly supported and have bounded $\beta$ order derivatives (Bouzebda $\&$ Didi, 2017). Then there exists a constant $C$ such that $| \theta _ { l j m } ^ { Q } | \leq C ( 2 ^ { - d j } ) ^ { \frac { \alpha } { d } + \frac { 1 } { 2 } }$ and $a _ { m } ^ { Q } \leq C$ . Recall that

$$
\widehat { p } _ { k } \cdot \widetilde { \nu } _ { k , Q } ( y ) = \sum _ { m \in \mathbb { S } } \widetilde { a } _ { m } ^ { Q } \phi _ { m } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } \widetilde { \theta } _ { l j m } ^ { Q } \psi _ { l j m } ( y ) ,
$$

with

$$
\begin{array} { r l r } & { } & { \displaystyle \widetilde { a } _ { m } ^ { Q } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \phi _ { m } ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) ; } \\ & { } & { \displaystyle \widetilde { \theta } _ { l j m } ^ { Q } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \psi _ { l j m } ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) . } \end{array}
$$

We have

$$
\mathbb { E } [ \widetilde { a } _ { m } ^ { Q } ] = p _ { k } \cdot \int \phi _ { m } ( y ) \nu _ { k , Q } ^ { * } ( y ) d y = a _ { m } ^ { Q } , \quad \mathbb { E } [ \widetilde { \theta } _ { l j m } ^ { Q } ] = p _ { k } \cdot \int \psi _ { l j m } ( y ) \nu _ { k , Q } ^ { * } ( y ) d y = \theta _ { l j m } ^ { Q } .
$$

Moreover, by the fact that $\phi ( \cdot )$ and $\psi _ { l } ( \cdot )$ are compactly supported, we can get that there exists a constant $C$ such that for any $1 \leq l \leq 2 ^ { d } - 1$ and $j \in \mathbb N$ , it holds that $| \mathbb { S } _ { l j } | \le C 2 ^ { d j }$ and $| \mathbb { S } | \leq C$ . Since $\nu _ { k , Q } ^ { * }$ and $\widetilde { \nu } _ { k , Q }$ are both compactly supported. There exists a constant $C$ so that for any $Q \in \bar { \mathcal { Q } } _ { k }$ ,

$$
\operatorname* { s p } _ { \substack { 2 \leq r _ { 1 } ^ { 4 } ( \mathbb { R } ^ { d } ) } } \Big ( \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big ) \leq C \operatorname* { s u p } _ { f \in C _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) } \Big ( \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) \mathrm { d } y - \int f ( y ) \widetilde { \nu } _ { k , Q } ( y ) \mathrm { d } y \Big )
$$

Then we consider $f \in C _ { 1 } ^ { 1 } (  { \mathbb { R } } ^ { d } )$ , similarly, we can rewrite

$$
f ( y ) = \sum _ { m \in \mathbb { Z } ^ { d } } b _ { m } \phi _ { m } ( y ) + \sum _ { l = 1 } ^ { 2 ^ { d } - 1 + \infty } \sum _ { j = 0 } ^ { + \infty } \sum _ { m \in \mathbb { Z } ^ { d } } f _ { l j m } \psi _ { l j m } ( y )
$$

where $| f _ { l j m } | \le C _ { 1 } ( 2 ^ { - d j } ) ^ { \frac { 1 } { d } + \frac { 1 } { 2 } }$ and $| b _ { m } | \leq C _ { 1 }$ . So we can get

$$
\begin{array} { l l } { \displaystyle \int f ( y ) \nu _ { k , Q } ^ { * } ( y ) d y - \int f ( y ) \tilde { \nu } _ { k , Q } ( y ) d y } \\ { \displaystyle = \frac { 1 } { \tilde { \mathcal { P } } _ { k } } ( \int \int ( y ) p _ { k } \cdot \nu _ { k , Q } ^ { * } ( y ) d y - \int \hat { p } _ { k } \cdot J ( y ) \tilde { \nu } _ { k , Q } ( y ) d y ) + \int \int \hat { J } ( y ) \nu _ { k , Q } ^ { * } ( y ) d y \cdot \big ( 1 - \frac { p _ { k } } { \tilde { \mathcal { P } } _ { k } } \big ) } \\ { \displaystyle = \frac { 1 } { \tilde { \mathcal { P } } _ { k } } \int f ( y ) ( \sum _ { m \in \binom { 1 } { m } } \frac { \chi _ { Q } ^ { 2 } } { ( \tilde { \nu } _ { m } ^ { 2 } - \tilde { \nu } _ { m } ^ { 2 } ) \xi _ { m } ( y ) } + \sum _ { l = 1 } ^ { 2 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \binom { 1 } { m } } \hat { \nu } _ { l , Q m } ^ { Q } - \mathbb { E } \hat { \beta } _ { l , Q m } ^ { Q } ) \hat { \nu } _ { l j m } ( y ) \Bigg ) d y } \\ { \displaystyle + \frac { 1 } { \tilde { \mathcal { P } } _ { k } } \int f ( y ) ( \sum _ { l = 1 } ^ { 2 - 1 } \sum _ { j = 1 } ^ { \infty } \sum _ { m \in \binom { 1 } { m } } \theta _ { l , m } ^ { Q } ( y ) d y ) d y + \int \hat { J } ( y ) \nu _ { k , Q } ^ { * } ( y ) d y \cdot \big ( 1 - \frac { p _ { k } } { \tilde { \mathcal { P } } _ { k } } \big ) } \\  \displaystyle \leq \frac { 1 } { \tilde { \mathcal { P } } _ { k } } | \frac { 1 } { n } \sum _ { i = 1 } ^ { n ^ { 2 - 1 } } \sum _ { j = 0 } ^ { J } \sum _ { m \in \binom { 1 } { m } } \hat { \nu } _  l j \end{array}
$$

$$
+ \frac { 1 } { \hat { p } _ { k } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { m \in \mathbb { S } } b _ { m } \phi _ { m } ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) - \mathbb { E } \Big [ \sum _ { m \in \mathbb { S } } b _ { m } \phi _ { m } ( Q ( X ) ) \rho _ { k } ( X ) \Big ] \right| + \frac { 1 } { \hat { p } _ { k } } \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 2 } ^ { \infty } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \theta _ { l j m } ^ { Q } + \int _ { \frac { 1 } { 2 } } ^ { 1 } \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 2 } ^ { \infty } \operatorname { d } f _ { l j m } \theta _ { l j m } ^ { Q } .
$$

First for term ( $D$ ),by Bernstein’s inequality, it holds with probability at least $1 - n ^ { - 3 }$ that $| p _ { k } - \widehat { p _ { k } } | \leq$ $C \sqrt { \frac { \log n } { n } }$ , then by $p _ { k } > 0$ , for large enough $n$ , we have $\begin{array} { r } { \left| 1 - \frac { p _ { k } } { \widehat { p } _ { k } } \right| \leq C \sqrt { \frac { \log n } { n } } } \end{array}$ . Moreover, for term $( C )$ , since $| f _ { l j m } | \lesssim ( 2 ^ { - d j } ) ^ { \frac { 1 } { d } + \frac { 1 } { 2 } }$ , $| \theta _ { l j m } ^ { Q } | \lesssim ( 2 ^ { - d j } ) ^ { \frac { \alpha } { d } + \frac 1 2 }$ and $2 ^ { d J } \asymp n ^ { \frac { d } { 2 \alpha + d } }$ , we can get

$$
\sum _ { j = J + 1 } ^ { + \infty } \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \theta _ { l j m } ^ { Q } \lesssim n ^ { - \frac { \alpha + 1 } { 2 \alpha + d } } .
$$

Then for term ( $A$ ), by standard symmetrization, we can get

$$
\begin{array} { r l } & { \mathbb { E } [ \underset { f \in \mathcal { C } _ { k } ^ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { l = 1 } ^ { d - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) - \mathbb { E } \bigg [ \displaystyle \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( Q ( X ) ) \rho _ { k } ( X ) } \\ & { \leq 2 \mathbb { E } \bigg [ \underset { f \in \mathcal { C } _ { k } ^ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \bigg | \frac { 1 } { n } \displaystyle \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) \bigg | \bigg ] , } \end{array}
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from Rademacher distribution, i.e. $P ( \varepsilon _ { i } = 1 ) = P ( \varepsilon _ { i } = - 1 ) = 0 . 5$ Define function set

$$
\mathcal { F } = \left\{ f : \mathcal { M } \to \mathbb { R } : f ( z ) = \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( Q ( x ) ) ; | f _ { l j m } | \leq ( 2 ^ { - d j } ) ^ { \frac { 1 } { d } + \frac { 1 } { 2 } } ; Q \in \widetilde { \mathcal { Q } } _ { k } \right\} .
$$

First we consider the function set

$$
\mathcal { F } _ { 1 } = \{ f : [ - L _ { 3 } , L _ { 3 } ] ^ { d }  \mathbb { R } , f ( y ) = \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathfrak { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( y ) , | f _ { l j m } | \leq ( 2 ^ { - d j } ) ^ { \frac { 1 } { d } + \frac { 1 } { 2 } } \} .
$$

If $\textstyle { \frac { 1 } { d } } \leq { \frac { 1 } { 2 } }$ , then there exists a constant $c$ such that for any $f \in { \mathcal { F } } _ { 1 }$ , it holds that

$$
c ( 2 ^ { d J } ) ^ { \frac { 1 } { d } - \frac { 1 } { 2 } } f \in C _ { 1 } ^ { \frac { d } { 2 } } ( [ - L , L ] ^ { d } ) .
$$

So for any  > 0, we can find a set N f ⊆ F1 such that qlog |N f | . (2dJ )( 12 − 1d )+ and for any $f \in { \mathcal { F } } _ { 1 }$ , there exists $\widetilde { f } \in N _ { \epsilon } ^ { f }$ such that

$$
\operatorname* { s u p } _ { y \in [ - L , L ] ^ { d } } | f ( y ) - { \widetilde { f } } ( y ) | \leq \epsilon .
$$

Then since $\Omega _ { k } = Q _ { k } ^ { * } ( \mathcal { M } \cap S _ { k } )$ is compactly supported and $\mathcal { M } \cap S _ { k } = G _ { k } ^ { * } ( \Omega _ { k } )$ , by lemma 6, for any $\epsilon > 0$ , we can find a function set $N _ { \epsilon } ^ { Q }$ such that $\sqrt { \log | N _ { \epsilon } ^ { Q } | } \lesssim ( \frac { 1 } { \epsilon } ) ^ { \frac { d } { 2 \beta } }$ and for any $Q \in \widetilde { \mathcal { Q } } _ { k }$ , there exists $\widetilde Q \in N _ { \epsilon } ^ { Q }$ such that

$$
\operatorname* { s u p } _ { x \in \mathcal { M } \cap { S _ { k } } } \| \widetilde { Q } ( x ) - Q ( x ) \| \le \epsilon .
$$

Then for any $Q \in \widetilde { \mathcal { Q } } _ { k }$ and $f \in { \mathcal { F } } _ { 1 }$ , there exists $\widetilde Q \in N _ { \epsilon } ^ { Q }$ , $\widetilde { f } \in N _ { \epsilon } ^ { f }$ and a constant $c$ such that

$$
\begin{array} { r l } & { \Big | f ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( \widetilde { Q } ( x ) ) \rho _ { k } ( x ) \Big | } \\ & { \le \Big | f ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( Q ( x ) ) \rho _ { k } ( x ) \Big | + \Big | \widetilde { f } ( Q ( x ) ) \rho _ { k } ( x ) - \widetilde { f } ( \widetilde { Q } ( x ) ) \rho _ { k } ( x ) \Big | } \\ & { \le c \epsilon . } \end{array}
$$

So we can get

$$
\log \mathbf { N } ( \mathcal { F } , \epsilon , \| \cdot \| _ { \infty } ) \lesssim \left( \frac { 1 } { \epsilon } \right) ^ { \frac { d } { \beta } } + \left( \frac { 2 ^ { d J ( \frac { 1 } { 2 } - \frac { 1 } { d } ) _ { + } } } { \epsilon } \right) ^ { 2 } .
$$

Choose $\begin{array} { r } { \delta = \left( \frac { 1 } { n } \right) ^ { \frac { \alpha + 1 } { 2 \alpha + d } } \lor \left( \frac { 1 } { n } \right) ^ { \frac { \beta } { d } } } \end{array}$ , we can get

$$
{ \begin{array} { r l } & { { \frac { 1 } { \sqrt { n } } } \int _ { \delta } ^ { 1 } \left[ \left( { \frac { \log n } { \epsilon } } \right) ^ { \frac { d } { 2 \beta } } + { \frac { ( 2 ^ { d J ( { \frac { 1 } { 2 } } - { \frac { 1 } { d } } ) } \log n ) \vee 1 } { \epsilon } } \right] \mathrm { d } \epsilon } \\ & { \lesssim { \frac { \log n } { \sqrt { n } } } + ( { \frac { 1 } { n } } ) ^ { \frac { \alpha + 1 } { 2 \alpha + d } } + ( { \frac { 1 } { n } } ) ^ { \frac { \beta } { d } } . } \end{array} }
$$

By Dudley’s entropy integral bound, it holds that

$$
\begin{array} { r l } & { \mathbb { E } \underset { f \in \mathcal { C } _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } | \frac { 1 } { n } \sum _ { l = 1 } ^ { 2 ^ { d } - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \sum _ { j = 0 } ^ { J } \sum _ { m \in \mathbb { S } _ { l j } } f _ { l j m } \psi _ { l j m } ( Q ( X _ { i } ) ) ) \rho _ { k } ( X _ { i } ) | } \\ & { \lesssim \frac { \log n } { \sqrt { n } } + ( \frac { 1 } { n } ) ^ { \frac { \alpha + 1 } { 2 \alpha + d } } + ( \frac { 1 } { n } ) ^ { \frac { \beta } { d } } . } \end{array}
$$

Similarly we can get

$$
\begin{array} { r l } & { \mathbb { E } \underset { f \in C _ { 1 } ^ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \left| \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \sum _ { m \in \mathbb { S } } b _ { m } \phi _ { m } \left( Q ( X _ { i } ) \right) \rho _ { k } ( X _ { i } ) \right| } \\ & { \quad \lesssim n ^ { - \frac { \beta } { d } } + \frac { \log n } { \sqrt { n } } . } \end{array}
$$

The statement is then followed by Talagrand concentration inequality (see for example, Theorem 3.27 of Wainwright (2019)) and the fact that $\alpha + 1 \le \beta$ .

# C.3 Proof of Lemma 4

We fix an arbitrary $k \in \lfloor K \rfloor$ in the following analysis. Since

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \rho _ { k } ( X _ { i } ) \leq n ^ { - \frac { 2 \beta } { d } - 1 } ,
$$

we can get

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| _ { 2 } \rho _ { k } ( X _ { i } ) \leq \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| _ { 2 } \sqrt { \rho _ { k } ( X _ { i } ) } } & { } \\ { \leq \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| _ { 2 } ^ { 2 } \cdot \rho _ { k } ( X _ { i } ) } } & { } \\ { \leq n ^ { - \frac { \beta } { d } - \frac { 1 } { 2 } } . } \end{array}
$$

Define

$$
\mathcal { F } _ { 2 } = \{ f = G \circ Q : G \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } ) , Q \in C _ { L } ^ { \beta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) \} .
$$

Then we have $\widehat { G } \circ \widehat { Q } \in \mathcal { F } _ { 2 }$ . Moreover, when $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { M } \cap { S } _ { k } } \| f _ { 1 } ( x ) - f _ { 2 } ( x ) \| _ { 2 } \leq \epsilon } \end{array}$ , it holds that

$$
\begin{array} { r l } & { \underset { x \in \mathcal { M } } { \operatorname* { s u p } } \Vert { \Vert x - f _ { 1 } ( x ) \Vert _ { 2 } \rho _ { k } ( x ) - \Vert x - f _ { 2 } ( x ) \Vert _ { 2 } \rho _ { k } ( x ) } \vert } \\ & { \le \underset { x \in \mathcal { M } \cap S _ { k } } { \operatorname* { s u p } } \Vert f _ { 2 } ( x ) - f _ { 1 } ( x ) \Vert _ { 2 } } \\ & { \le \epsilon . } \end{array}
$$

So consider the function class $\widetilde { \mathcal { F } } _ { 2 } = \{ | \| x - f ( x ) \| _ { 2 } \rho _ { k } ( x ) , f \in \mathcal { F } _ { 2 } \}$ , by Lemma 6, it holds that $\log N ( \widetilde { \mathcal { F } } _ { 2 } , \Vert \cdot$ $\begin{array} { r } { \| _ { \mathcal { M } } , \epsilon ) \le \log N ( \mathcal { F } _ { 2 } , \| \cdot \| _ { \mathcal { M } } , \epsilon ) \lesssim ( \frac { 1 } { \epsilon } ) ^ { \frac { d } { \beta } } } \end{array}$ . By Dudley’s entropy integral bound (see for example, Wainwright (2019)), we can get that

$$
\mathbb { E } \bigg [ \operatorname* { s u p } _ { f \in \mathcal { F } _ { 2 } } \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - f ( X _ { i } ) \| _ { 2 \rho _ { k } } ( X _ { i } ) - \mathbb { E } _ { \mu ^ { * } } \big [ \| X - f ( X ) \| _ { 2 \rho _ { k } } ( X ) \big ] \Big | \bigg ] \leq C n ^ { - \frac { \beta } { d } } \vee \frac { \log n } { \sqrt { n } } .
$$

Then by Talagrand concentration inequality (see for example, Wainwright (2019)), we can get that there exists a constant $c _ { 2 }$ , such that it holds with probability $1 - n ^ { - 3 }$ that

$$
\mathbb { E } _ { \mu ^ { * } } \left[ \| X - \widehat { G } _ { k } \circ \widehat { Q } _ { k } ( X ) \| _ { 2 } \cdot \rho _ { k } ( X ) \right] \leq c _ { 2 } \left( n ^ { - \frac { \beta } { d } } \vee \frac { \log n } { \sqrt { n } } \right) .
$$

For the second statement, we first fix a small enough positive constant $r > 0$ that will be chosen later. Then for any $z \in \Omega _ { k } = Q ^ { * } ( \mathcal { M } \cap S _ { k } )$ , there exists $\sigma ( z ) \in \Omega _ { k }$ so that $z \in \mathbb { B } _ { r } ( \sigma ( z ) )$ and $\nu _ { k } ^ { * } ( \sigma ( z ) ) \geq g ( r ) > 0$ . Let $\mathcal { A } _ { z } = \{ \sigma ( z ) : z \in \Omega _ { k } \}$ and $\widehat { f } _ { k } = \widehat { G } _ { k } \circ \widehat { Q } _ { k } \circ G _ { k } ^ { * }$ , we resort to the following lemma that provides an upper bound on $\| G _ { k } ^ { * } ( z ) - \widehat { f } _ { k } ( z ) \| _ { 2 }$ for all $z \in \mathcal { A } _ { z }$ .

Lemma 7. It holds with probability at least $1 - c n ^ { - 3 }$ that for all $z \in A _ { z }$ ,

$$
\begin{array} { r l } & { \displaystyle \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop j | \leq | \beta | } \frac { 1 } { j ! } | | \widehat { f } _ { k } ^ { ( j ) } ( \tilde { z } ) - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) | | _ { 2 } ( \delta _ { n } ) ^ { | j | } \leq C \cdot \big ( g ( r ) \big ) ^ { - \frac { 2 \beta } { d } - 1 } \cdot \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta } { d } } , } \end{array}
$$

where $\delta _ { n } = b _ { 1 } \cdot ( g ( r ) ) ^ { - { \frac { 2 } { d } } } \cdot \left( { \frac { \log n } { n } } \right) ^ { \frac { 1 } { d } }$ for a constant $b _ { 1 }$ independent of $n$ and $r$ .

So by Lemma 7, we can get

$$
\begin{array} { l } { \displaystyle \operatorname* { s u p } _ { z \in A _ { z } } \| G _ { k } ^ { * } ( z ) - \widehat { f } _ { k } ( z ) \| _ { 2 } \leq C \cdot \big ( g ( r ) \big ) ^ { - \frac { 2 \beta } { d } - 1 } \cdot \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta } { d } } } \\ { \displaystyle \operatorname* { s u p } _ { z \in A _ { z } } \| \mathbf { J } _ { G _ { k } ^ { * } } ( z ) - \mathbf { J } _ { \widehat { f } _ { k } } ( z ) \| _ { F } \leq C _ { 1 } \cdot \big ( g ( r ) \big ) ^ { - \frac { 2 \beta - 2 } { d } - 1 } \cdot \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta - 1 } { d } } . } \end{array}
$$

Also by the fact that $G _ { k } ^ { * }$ and $\widehat { f } = \widehat { G } _ { k } \circ \widehat { Q } _ { k } \circ G _ { k } ^ { * }$ are $\beta$ -Hölder smooth with $\beta \ge 1 + \tilde { \alpha } > 1$ , we have

$$
\begin{array} { r l } & { \underset { z \in \Omega _ { k } } { \operatorname* { s u p } } \| G _ { k } ^ { * } ( z ) - \widehat { f } _ { k } ( z ) \| _ { 2 } \leq C \cdot \big ( g ( r ) \big ) ^ { - \frac { 2 \beta } d - 1 } \cdot \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta } d } + C _ { 2 } r } \\ & { \underset { z \in \Omega _ { k } } { \operatorname* { s u p } } \| \mathbf { J } _ { G _ { k } ^ { * } } ( z ) - \mathbf { J } _ { \widehat { f } _ { k } } ( z ) \| _ { F } \leq C _ { 1 } \cdot \big ( g ( r ) \big ) ^ { - \frac { 2 \beta - 2 } { d } - 1 } \cdot \big ( \frac { \log n } { n } \big ) ^ { \frac { \beta - 1 } d } + C _ { 3 } r . } \end{array}
$$

By the fact that for any $z \in \Omega _ { k }$ , it holds that $z = Q _ { k } ^ { * } ( G _ { k } ^ { * } ( z ) )$ , we obtain $I _ { d } = \mathbf { J } _ { Q _ { k } ^ { * } } ( G _ { k } ^ { * } ( z ) ) \mathbf { J } _ { G _ { k } ^ { * } } ( z )$ . Since $Q _ { k } ^ { * }$ is $L$ -Lipschitz, $\mathbf { J } _ { Q _ { k } ^ { * } } ( G _ { k } ^ { * } ( z ) )$ has bounded operator norm, which implies $\operatorname* { d e t } ( \mathbf { J } _ { G _ { k } ^ { * } } ^ { T } ( z ) \mathbf { J } _ { G _ { k } ^ { * } } ( z ) ) \ge c$ for some positive constant $c > 0$ and $z \in \Omega _ { k }$ . Moroever, by the fact that $G _ { k } ^ { * }$ is $\beta$ -Hölder smooth with $\beta > 1$ , there exists a positive constant $\epsilon$ so that for the $\scriptstyle \epsilon$ - enlargement of $\Omega _ { k }$ : $\Omega _ { k , \epsilon } = \{ y \in \mathbb { B } _ { \epsilon } ( z ) : z \in \Omega _ { k } \}$ , it holds that for any $z \in \Omega _ { k , \epsilon }$ , $\begin{array} { r } { \operatorname* { d e t } ( \mathbf { J } _ { G _ { k } ^ { * } } ^ { T } ( z ) \mathbf { J } _ { G _ { k } ^ { * } } ( z ) ) \geq \frac { c } { 2 } } \end{array}$ . Therefore, the second display in (18) and $\beta$ -Hölder smooth of $\widehat { f _ { k } }$ implies that $\begin{array} { r } { \operatorname* { i n f } _ { z \in \Omega _ { k , \epsilon } } \operatorname* { d e t } ( \mathbf { J } _ { \widehat { f } _ { k } } ^ { T } ( z ) \mathbf { J } _ { \widehat { f } _ { k } } ( z ) ) \geq \frac { c } { 4 } } \end{array}$ for all sufficiently small $\epsilon$ , $r$ and sufficiently large $n$ . Now let $\widehat { l } _ { k } = \widehat { Q } _ { k } \circ G _ { k } ^ { * }$ and by using the identity $\widehat { f } _ { k } = \widehat { G } _ { k } \circ \widehat { l } _ { k }$ ,

$$
\begin{array} { r l } & { \mathbf { J } _ { \widehat { f } _ { k } } ^ { T } ( z ) \mathbf { J } _ { \widehat { f } _ { k } } ( z ) = \left( \mathbf { J } _ { \widehat { G } _ { k } } ( \widehat { l } _ { k } ( z ) ) \mathbf { J } _ { \widehat { l } _ { k } } ( z ) \right) ^ { T } \left( \mathbf { J } _ { \widehat { G } _ { k } } ( \widehat { l } _ { k } ( z ) ) \mathbf { J } _ { \widehat { l } _ { k } } ( z ) \right) } \\ & { \qquad = \mathbf { J } _ { \widehat { l } _ { k } } ^ { T } ( z ) \mathbf { J } _ { \widehat { G } _ { k } } ^ { T } ( \widehat { l } _ { k } ( z ) ) \mathbf { J } _ { \widehat { G } _ { k } } ( \widehat { l } _ { k } ( z ) ) \mathbf { J } _ { \widehat { l } _ { k } } ( z ) , } \end{array}
$$

by taking determinant we further obtain (note that $\mathbf { J } _ { \widehat { l } _ { k } } ( z )$ is a square matrix)

$$
\operatorname* { d e t } ^ { 2 } \left( \mathbf { J } _ { \widehat { l _ { k } } } ( z ) \right) \cdot \operatorname* { d e t } \left( \mathbf { J } _ { \widehat { G } _ { k } } ^ { T } ( \widehat { l _ { k } } ( z ) ) \mathbf { J } _ { \widehat { G } _ { k } } ( \widehat { l _ { k } } ( z ) ) \right) \geq \frac { c } { 4 } .
$$

Since both $\widehat { G } _ { k }$ and $\widehat { Q } _ { k }$ are $L$ -Lipschitz, we can further deduce that $0 < c _ { 1 } \le \operatorname* { d e t } ( \mathbf { J } _ { \widehat { l _ { k } } } ( z ) ) \le c _ { 2 }$ for all $z \in \Omega _ { k , \epsilon }$ .

We claim that $\widehat { l _ { k } }$ is globally invertible over $\Omega _ { k , \epsilon }$ when $\epsilon$ , $r$ are small enough and $n$ is large enough. Otherwise, suppose there exist distinct $z _ { 0 }$ and $z _ { 1 }$ in $\Omega _ { k , \epsilon }$ such that $\widehat { l _ { k } } ( z _ { 0 } ) = \widehat { l _ { k } } ( z _ { 1 } )$ . Since $0 < c _ { 1 } \leq$

$\operatorname* { d e t } ( \mathbf { J } _ { \widehat { l } _ { k } } ( z ) ) \leq c _ { 2 }$ implies $\widehat { l _ { k } }$ to be locally invertible, meaning that there exists some constant $b _ { 0 } > 0$ independent of $\epsilon$ such that $\left\| z _ { 0 } - z _ { 1 } \right\| \ge b _ { 0 }$ . By the definition of $\Omega _ { k , \epsilon }$ and the Lipschitzness of $\widehat { G } _ { k }$ and $\widehat { l _ { k } }$ , there exist $z _ { 0 }$ and $z _ { 1 }$ in $\Omega _ { k }$ such that (for sufficiently small $\epsilon$ )

$$
\| \bar { z } _ { 0 } - \bar { z } _ { 1 } \| \geq \frac { 1 } { 2 } b _ { 0 } , \quad \| \widehat { l } _ { k } ( \bar { z } _ { 0 } ) - \widehat { l } _ { k } ( \bar { z } _ { 1 } ) \| _ { 2 } \leq C \epsilon \quad \mathrm { a n d } \quad \| \widehat { f } _ { k } ( \bar { z } _ { 0 } ) - \widehat { f } _ { k } ( \bar { z } _ { 1 } ) \| \leq C \epsilon .
$$

The third display above combined with the first display in (18) implies $\| G _ { k } ^ { * } ( \bar { z } _ { 0 } ) - G _ { k } ^ { * } ( \bar { z } _ { 1 } ) \| _ { 2 } \leq C _ { 1 } ( \epsilon + r )$ . On the other hand, from the first display above and the Lipschitzness of $Q _ { k } ^ { * }$ , we have

$$
\begin{array} { r } { \frac 1 2 b _ { 0 } \le \| \bar { z } _ { 0 } - \bar { z } _ { 1 } \| = \| Q _ { k } ^ { * } ( G _ { k } ^ { * } ( \bar { z } _ { 0 } ) - Q _ { k } ^ { * } ( G _ { k } ^ { * } ( \bar { z } _ { 1 } ) ) \| _ { 2 } \le C \| G _ { k } ^ { * } ( \bar { z } _ { 0 } ) - G _ { k } ^ { * } ( \bar { z } _ { 1 } ) \| _ { 2 } \le C C _ { 1 } ( \epsilon + r ) , } \end{array}
$$

which is a contradiction when $\epsilon$ , $r$ are chosen small enough.

Let $\widehat { l } _ { k } ^ { - 1 } : \widehat { l } _ { k } ( \Omega _ { k , \epsilon / 2 } ) \to \Omega _ { k , \epsilon / 2 }$ be the inverse of $\widehat { l _ { k } }$ over $\Omega _ { k , \epsilon / 2 }$ . By using the inverse function theorem for Hölder space (see for example, Appendix A of (Eldering, 2013)), we can conclude $\widehat { l _ { k } ^ { - 1 } } \in C _ { C _ { 0 } } ^ { \beta } ( \widehat { l _ { k } } ( \Omega _ { k , \epsilon / 2 } ) ; \mathbb { R } ^ { d } )$ for some sufficiently large constant $C _ { 0 }$ . Therefore, we can write the expression of the density function of $\begin{array} { r } { \nu _ { k , \widehat { Q } _ { k } } ^ { * } = [ \widehat { Q } _ { k } ] _ { \# } \big ( \frac { \rho _ { k } \mu ^ { * } } { p _ { k } } \big ) } \end{array}$ as

$$
\nu _ { k , \widehat Q _ { k } } ^ { * } ( y ) = \nu _ { k } ^ { * } ( \widehat l _ { k } ^ { - 1 } ( y ) ) \cdot \left( \operatorname* { d e t } \big ( \mathbf { J } _ { \widehat { l _ { k } ^ { - 1 } } } ^ { T } ( x ) \mathbf { J } _ { \widehat { l _ { k } ^ { - 1 } } } ( x ) \big ) \right) ^ { \frac 1 2 } \cdot \mathbf { 1 } \big ( y \in \widehat { l _ { k } } ( \Omega _ { k } ) \big )
$$

by applying the change of variable of $y = \widehat { l _ { k } } ( z )$ with $z \sim \nu _ { k } ^ { * }$ . Moreover, since $\nu _ { k } ^ { * } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ , this together with $\widehat { l _ { k } ^ { - 1 } } \in C _ { C _ { 0 } } ^ { \beta } ( \widehat { l _ { k } } ( \Omega _ { k , \epsilon / 2 } ) ; \mathbb { R } ^ { d } )$ implies $\nu _ { \widehat { Q } } ^ { \ast } \in C _ { C _ { 1 } } ^ { \widehat { \alpha } } ( \mathbb { R } ^ { d } )$ for some constant $C _ { 1 }$ (recall $\tilde { \alpha } = \alpha \wedge ( \beta - 1 ) )$ ).

# C.4 Proof of Lemma 7

The proof follows the analysis in Tang $h _ { n }$ -covering set of $\mathcal { A } _ { z }$ under the $\ell _ { 2 }$ n distance, where its cardinality satisfies $\&$ Yang (2022). Let $\begin{array} { r } { h _ { n } = \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { d } } } \end{array}$ and $| \mathcal { N } _ { h _ { n } } | \leq C \frac { n } { \log n }$ $\mathcal { N } _ { h _ { n } } \subset \mathcal { A } _ { z }$ be a minimal . For any $\widetilde { z } \in \mathcal N _ { h _ { n } }$ , define $\delta _ { n } = b \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { d } }$ .

We claim that it suffices to show that for sufficiently large $b$ , it holds with probability at least $1 - n ^ { - 3 }$ that for any $\tilde { z } \in \mathcal N _ { h _ { n } }$ ,

$$
\sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop j | \leq | \beta | } \frac { 1 } { j ! } \| \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \leq C \left( \frac { \log n } { n } \right) ^ { \frac { \beta } { d } } .
$$

In fact, if this inequality holds, then we can apply a standard argument of approximation by the $h _ { n }$ - covering set. Concretely, for any $z \in \mathcal { A } _ { z }$ , there exists $\tilde { z } \in \mathcal N _ { h _ { n } }$ such that $\begin{array} { r } { \| z - \widetilde { z } \| _ { 2 } \leq h _ { n } = \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { d } } } \end{array}$ , we can obtain by applying Taylor expansion to $G _ { k } ^ { * } ( z ) - { \widehat { f } } _ { k } ( z )$ that

$$
\begin{array} { r l } & { \| G _ { k } ^ { * } ( z ) - \widehat f _ { k } ( z ) \| _ { 2 } \leq C \displaystyle \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \| \widehat f _ { k } ^ { ( j ) } ( \widetilde z ) - G _ { k } ^ { * , ( j ) } ( \widetilde z ) \| _ { 2 } \left( \frac { \log n } { n } \right) ^ { \frac { | j | } { d } } + C \left( \frac { \log n } { n } \right) ^ { \frac { \beta } { d } } } \\ & { \qquad \leq C \left( \displaystyle \frac { \log n } { n } \right) ^ { \frac { \beta } { d } } . } \end{array}
$$

Now let us prove inequality (20). Recall that

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| X _ { i } - \widehat { G } _ { k } ( \widehat { Q } _ { k } ( X _ { i } ) ) \| ^ { 2 } \rho _ { k } ( X _ { i } ) \leq C n ^ { - \frac { 2 \beta } { d } - 1 } .
$$

In particular, by restricting the sum to those $Q ^ { * } ( X _ { i } )$ in $\mathbb { B } _ { \delta _ { n } } ( { \widetilde { z } } )$ for a fixed $\tilde { z } \in \mathcal N _ { h _ { n } }$ , we further obtain (recall that $\widehat { f } _ { k } = \widehat { G } _ { k } \circ \widehat { Q } _ { k } \circ G _ { k } ^ { * } .$ )

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| G _ { k } ^ { * } ( Q _ { k } ^ { * } ( X _ { i } ) ) - \widehat { f } _ { k } ( Q _ { k } ^ { * } ( X _ { i } ) ) \| ^ { 2 } \cdot \rho _ { k } ( X _ { i } ) \cdot \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \vec { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \leq C n ^ { - \frac { 2 \beta } { d } - 1 } .
$$

By applying the Taylor expansion to $G _ { k } ^ { * } ( z ) - { \widehat { f } } _ { k } ( z )$ around $\widetilde { z }$ in the preceding display and using the fact that $G _ { k } ^ { \ast } - \widehat { f } _ { k } \in C _ { C _ { 0 } } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; \mathbb { R } ^ { D } )$ with some sufficiently large constant $C _ { 0 }$ , we can get the following localized basic inequality after some algebra calculation

$$
\begin{array} { l } { { \displaystyle U _ { n } ( \widetilde { z } , \widehat { f } _ { k } ) : = } } \\ { { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Big \| \sum _ { \substack { j \in \mathbb { N } _ { k } ^ { 0 } } \atop | j | \leq | \delta | } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) \right) ( Q _ { k } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \cdot \rho _ { k } ( X _ { i } ) } } \\ { { \displaystyle \leq c \Big ( ( \delta _ { n } ) ^ { 2 \beta } + ( \delta _ { n } ) ^ { \beta } \sum _ { \substack { j \in \mathbb { N } _ { k } ^ { 0 } } \atop j | \leq | \delta | } \frac { 1 } { j ! } \left\| G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) \right\| _ { 2 } ( \delta _ { n } ) ^ { | j | } \Big ) \cdot \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \cdot \rho _ { k } ( X _ { i } ) } . }  \end{array}
$$

The second factor on the right hand side of (21) can be bounded by applying a simple union bound argument and Bernstein’s inequality for bounded function as follows. First, we can bound the expectation

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \bigl [ \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \bigr ] } \\ & { \stackrel { ( i ) } { = } p _ { k } \int _ { \mathbb { B } _ { \delta _ { n } } ( \tilde { z } ) } \nu _ { k } ^ { * } ( z ) { \mathrm { d } } z \leq C p _ { k } \delta _ { n } ^ { d } } \\ & { \leq C b ^ { d } \frac { \log n } { n } , } \end{array}
$$

where step (i) follows by the fact that $\begin{array} { r } { \nu _ { k } ^ { * } = ( Q _ { k } ^ { * } ) _ { \# } ( \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } ) } \end{array}$ . Since the random variable $\mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( z ) } ( Q _ { k } ^ { * } ( X ) ) { \cdot \rho _ { k } ( X ) }$ is uniformly bounded by 1, and inequality (22) and $\rho _ { k } \le 1$ implies its variance to be bounded by $C _ { 1 } b ^ { d } \frac { \log n } { n }$ , we may apply the Bernstein inequality and a simple union bound argument over all $\widetilde { z } \in \mathcal N _ { h _ { n } }$ (with $| \mathcal { N } _ { h _ { n } } | \leq C \frac { n } { \log n } )$ to obtain that with probability at least $1 - n ^ { - c }$ ,

$$
\operatorname* { s u p } _ { \tilde { z } \in \mathcal { N } _ { h _ { n } } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \cdot \rho _ { k } ( X _ { i } ) - \mathbb { E } _ { \mu ^ { * } } \left[ \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \right] \bigg | \le C _ { 2 } b ^ { \frac { d } { 2 } } \cdot \frac { \log n } { n } ,
$$

which together with (22) leads to

$$
\operatorname* { s u p } _ { \tilde { z } \in \mathcal { N } _ { h _ { n } } } \left[ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { n } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \right] \leq C b ^ { d } \cdot \frac { \log n } { n } .
$$

To analyze the quantity $U _ { n } ( \widetilde { z } , \widehat { f _ { k } } )$ on the left hand side of the localized basic inequality (21), we will resort to the following lemma.

Lemma 8. With probability at least $1 - n ^ { - 3 }$ , the following inequality holds for any $\beta$ -smooth function $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ and $\tilde { z } \in \mathcal N _ { h _ { \tilde { n } } }$ ,

$$
\left| U _ { n } ( \widetilde { z } , f ) - \mathbb { E } _ { \mu ^ { * } } [ U _ { n } ( \widetilde { z } , f ) ] \right| \leq C b ^ { \frac { d } { 2 } } \cdot \frac { \log n } { n } \cdot \bigg \{ \big ( \frac { \log n } { n } \big ) ^ { \frac { 2 \beta } { d } } + \Big [ \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop | j | \leq | \beta | } \frac { 1 } { j ! } \| f ^ { ( j ) } ( \widetilde { z } ) - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \Big ] ^ { 2 }
$$

where the expectation is taken with respect to the randomness in $\{ X _ { i } \} _ { i = 1 } ^ { n }$

Before applying this lemma, notice that for any $\tilde { z } \in \mathcal N _ { h _ { n } }$ , we can bound the expectation $\mathbb { E } _ { \mu ^ { * } } [ U _ { n } ( \widetilde { z } , \widehat { f } _ { k } ) ]$ , where $f$ has been plugged-in with $\widehat { f _ { k } }$ , by

$$
\begin{array} { r l } & { \mathbb { E } _ { n ^ { * } } \{ U _ { n } ( \tilde { \varepsilon } ) , \tilde { f } _ { k } \} \Big | } \\ & { = \mathbb { E } _ { n ^ { * } } \Big [ \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \frac { 1 } { j ! } \Big ( G _ { k } ^ { s , ( i ) } ( \tilde { \varepsilon } ) - \widetilde f _ { k } ^ { ( i ) } ( \tilde { \varepsilon } ) \big ) ( Q _ { k } ^ { s } ( X ) - \tilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { E } _ { n } ( \tilde { \varepsilon } ) } ( Q _ { k } ^ { s } ( X ) ) \cdot \rho _ { k } ( X ) \Big ] } \\ & { \qquad \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big [ \displaystyle \sum _ { s \in \mathbb { R } _ { n } ( \tilde { \varepsilon } ) } \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } ( \tilde { \varepsilon } ) } \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big [ G _ { k } ^ { s , ( i ) } ( \tilde { \varepsilon } ) - \widetilde f _ { k } ^ { ( i ) } ( \tilde { \varepsilon } ) \big ) ( z - \tilde { z } ) ^ { j } \Big ] \Big \| _ { 2 } ^ { 2 }  { \mathrm { d } } z } \\ &  \leq \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } ( \frac { 1 } { j ! } \cdot \Big [ \| Q _ { k } ^ { s , ( i ) } ( z ) \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } ( \tilde { \varepsilon } ) } \Big \| \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big [ \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big [ \displaystyle \sum _ { s \in \mathbb { R } _ { n } } \Big ( \delta _ { s } ^ { ( i ) } ( \tilde { \varepsilon } ) - \widetilde f _ { k } ^ { ( i ) } ( \tilde { \varepsilon } ) \Big ) \cdot z \Big \| _  2 \end{array}
$$

where step (i) uses the fact that $Q _ { k } ^ { * } ( X )$ given $\begin{array} { r } { X \sim \frac { \mu ^ { * } \cdot \rho _ { k } } { p _ { k } } } \end{array}$ is distributed as $\nu _ { k } ^ { * }$ , step (ii) follows by applying the change of variable of $\frac { z - \bar { z } } { \delta _ { n } }  z$ , and the last step follows by the fact that $\nu _ { k } ^ { * } ( \widetilde { z } ) \geq g ( r )$ for $\widetilde { z } \in A _ { z }$ and the smoothness of $\nu _ { k } ^ { * }$ . Now using the fact that for any $d$ -variate polynomial $\begin{array} { r } { S ( y ) = \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } y ^ { j } } \end{array}$ , $\boldsymbol { y } \in \mathbb { R } ^ { d }$ , there exists some positive constant $C ( d , k )$ only depending on $( d , k )$ such that

$$
\int _ { \mathbb { B } _ { 1 } ^ { d } } \mathcal { S } ^ { 2 } ( y ) \mathrm { d } y \geq C ( d , k ) \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } ^ { 2 } ,
$$

we can obtain that

$$
\int _ { \mathbb { B } _ { 1 } ^ { d } } \Big \lVert \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | j | \leq | \beta | } } \frac { 1 } { j ! } \delta _ { n } ^ { j } \left( G _ { k } ^ { * , ( j ) } ( \tilde { z } ) - \widehat f _ { k } ^ { ( j ) } ( \tilde { z } ) \right) z ^ { j } \Big \rVert _ { 2 } ^ { 2 } \mathrm { d } z \geq c \bigg ( \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | j | \leq | \beta | } } \frac { 1 } { j ! } \| \widehat { f } _ { k } ^ { ( j ) } ( \tilde { z } ) - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \bigg ) ^ { 2 } .
$$

Finally, by combining equations (21), (22), (25), (26) and Lemma 8, we obtain that with probability at least $1 - c n ^ { - 3 }$ , for any $\widetilde { z } \in \mathcal N _ { h _ { n } }$ ,

$$
\begin{array} { r l } & { \displaystyle b ^ { d } \cdot \frac { \log n } { n } \cdot g ( r ) \cdot \bigg ( \sum _ { j \in \mathbb { N } _ { n } ^ { d } } \frac { 1 } { j ! } \| \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \bigg ) ^ { 2 } } \\ & { \le C b ^ { \frac { d } { 2 } } \cdot \displaystyle \frac { \log n } { n } \cdot \bigg ( \sum _ { j \in \mathbb { N } _ { n } ^ { d } } \frac { 1 } { j ! } \| \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \bigg ) ^ { 2 } + C b ^ { \frac { d } { 2 } } \cdot \Big ( \displaystyle \frac { \log n } { n } \Big ) ^ { \frac { 2 \beta } { d } } \cdot \displaystyle \frac { \log n } { n } } \\ & { \qquad \quad + C b ^ { d } \cdot \displaystyle \frac { \log n } { n } \cdot \bigg ( ( \delta _ { n } ) ^ { 2 \beta } + ( \delta _ { n } ) ^ { \beta } \sum _ { j \in \mathbb { N } _ { n } ^ { d } } \frac { 1 } { j ! } \| G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - \widehat { f } _ { k } ^ { ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { n } ) ^ { | j | } \bigg ) . } \end{array}
$$

Consequently, the claimed inequality (20) follows from the above by choosing $b = b _ { 1 } ( g ( r ) ) ^ { - \frac { 2 } { d } }$ with sufficiently large $b _ { 1 }$ and the definition that $\delta _ { n } = b \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { d } }$ .

# C.5 Proof of Lemma 8

The proof follows from the proof of Lemma 18 in Tang $\&$ Yang (2022), we include it here for completeness.   
Since $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ , for any $z \in \mathbb { B } _ { 1 } ^ { d }$ and $j \in  { \mathbb { N } } _ { 0 } ^ { d }$ with $| j | \le \lfloor \beta \rfloor$ , it holds that $\| f ^ { ( j ) } ( z ) \| _ { 2 } \leq \sqrt { D } L = C _ { 0 }$ .

For any fixed $\tilde { z } \in \mathcal N _ { h _ { \tilde { n } } }$ and $\tilde { \delta } > 0$ , let

$$
\bar { T } ( \widetilde { \delta } ) = \Big \{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , \lfloor j \rfloor \leq \lfloor \beta \rfloor } \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \left( \boldsymbol { d } + \lfloor \beta \rfloor - 1 \right) } : \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } \atop | \boldsymbol { j } | \leq \lfloor \beta \rfloor } \frac { 1 } { j ! } \left\| T _ { j } - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \right\| _ { 2 } ( \delta _ { \overline { { z } } } ) ^ { \lfloor j \rfloor } \leq \widetilde { \delta } \Big \} .
$$

We also define the following supreme of an empirical process indexed by $T \in { \bar { \mathcal { T } } } ( { \widetilde { \delta } } )$ ,

$$
\begin{array} { r l r } & { } & { Z _ { n } ( \widetilde { \boldsymbol { \theta } } ) = } \\ & { } & { \underset { T \in \widetilde { T } ( \widetilde { \boldsymbol { \theta } } ) } { \operatorname* { s u p } } \Bigg | \mathbb { E } _ { \mu ^ { * } } \Bigg [ \Big \| \underset { | j | \leq 0 } { \sum } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \Bigg ] } \\ & { } & { \quad - \frac { 1 } { n } \underset { i = 1 } { \sum } \Bigg [ \Big \| \underset { | j | \leq 0 } { \sum } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \Bigg ] \Bigg | , } \end{array}
$$

and $R _ { n } ( \widetilde { \delta } ) = \mathbb { E } _ { \mu ^ { * } } \left[ Z _ { n } ( \widetilde { \delta } ) \right]$ . We will first prove a concentration inequality for a fixed radius $\widetilde { \delta } > 0$ , and then using the peeling technique to allow the radius to be random, which leads to the desired result.

To apply the Talagrand concentration inequality (see, for example, Theorem 3.27 of Wainwright (2019)) for bounding the difference $| Z _ { n } ( { \widetilde { \delta } } ) - R _ { n } ( { \widetilde { \delta } } ) |$ for a fixed $\tilde { \delta } > 0$ , we notice that each additive component in the second empirical sum above has second moment uniformly bounded by

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \Bigg [ \underset { T \in \mathcal { T } ( \tilde { \mathcal { O } } ) } { \operatorname* { s u p } } \Big ( \Big \lVert \underset { j \in \mathcal { K } ^ { 0 } } { \sum } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X ) - \tilde { z } ) ^ { j } \Big \rVert _ { 2 } ^ { 4 } \cdot \mathfrak { I } _ { \mathcal { B } _ { \mathcal { B } _ { \mathcal { Z } } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \Big ) \Bigg ] } \\ & { \leq \underset { \tau \in \tilde { \mathcal { S } } _ { \tilde { \mathcal { B } } _ { \tilde { \mathcal { Z } } } } ( \tilde { z } ) } { \operatorname* { s u p } } \Big \lVert \underset { j \in \mathcal { K } _ { \tilde { \mathcal { A } } } } { \sum } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \right) ( z - \tilde { z } ) ^ { j } \Big \rVert _ { 2 } ^ { 4 } \cdot \mathbb { E } _ { \mu ^ { * } } \cdot \big [ \mathfrak { I } _ { \mathcal { B } _ { \mathcal { Z } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \big ] } \\ & { \quad \tau \in \mathcal { T } ( \tilde { \mathcal { S } } ) \quad | \tilde { z } | ^ { \mathrm { L } } } \\ & { \leq C \underset { T \in T ( \tilde { \mathcal { B } } ) } { \operatorname* { s u p } } \Bigg ( \underset { j \in \mathcal { K } _ { \tilde { \mathcal { A } } } ^ { 0 } } { \sum } \frac { 1 } { j ! } \left| T _ { j } - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) \right| \| _ { 2 } ( \delta _ { \tilde { z } } ) | i \Bigg ) ^ { 4 } \cdot b _ { 2 } ^ { i } \cdot \frac { \log n } { n } } \\  \end{array}
$$

where we have used inequality (22) to bound $\mathbb { E } _ { \mu ^ { * } } \left\lfloor \mathbf { 1 } _ { \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \mathcal { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) \right\rfloor$ . Moreover, each additive component can be almost surely bounded by

$$
\begin{array} { r l } & { \quad \underset { z \in \mathbb { B } _ { \delta _ { \widetilde { z } } } ( \widetilde { z } ) } { \operatorname* { s u p } } \Big \Vert \underset { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { \jmath \in \mathbb { N } _ { 0 } ^ { d } } } { \sum } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X ) - \widetilde { z } ) ^ { j } \Big \Vert _ { 2 } ^ { 2 } } \\ & { \le C \left( \underset { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { \jmath \in \mathbb { N } _ { 0 } ^ { d } } } { \sum } \frac { 1 } { j ! } \| T _ { j } - G ^ { * , ( j ) } ( \widetilde { z } ) \| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } \right) ^ { 2 } \le C \widetilde { \delta } ^ { 2 } . } \end{array}
$$

Based on these two bounds, we can apply the Talagrand concentration inequality to obtain that for any $s \geq 0$ ,

$$
\mathbb { P } \big ( Z _ { n } ( \widetilde { \delta } ) \geq R _ { n } ( \widetilde { \delta } ) + s ^ { 2 } \big ) \leq 2 \exp \left( - \frac { c n s ^ { 4 } } { s ^ { 2 } \widetilde { \delta } ^ { 2 } + b _ { 2 } ^ { d } \widetilde { \delta } ^ { 4 } \cdot \frac { \log n } { n } } \right) .
$$

It remains to bound the expectation $R _ { n } ( { \widetilde { \delta } } )$ via the symmetrization technique and chaining. By a standard

$$
\begin{array} { r l } & { \displaystyle R _ { n } ( \widetilde \delta ) \leq \frac { 2 } { \sqrt { n } } { \mathbb E } \Bigg [ \operatorname* { s u p } _ { \substack { T \in \widetilde { T } ( \widetilde \delta ) } } } \\ & { \quad \bigg | \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } \Big [ \Big \| \displaystyle \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X ) - \widetilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde \delta } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) \cdot \rho _ { k } ( X _ { i } ) \Big ] \Bigg | \Bigg ] , } \end{array}
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from the Rademacher distribution, i.e. $\mathbb { P } ( \varepsilon _ { i } = 1 ) = \mathbb { P } ( \varepsilon _ { i } = - 1 ) = 0 . 5$ Since given $\{ X _ { i } \} _ { i = 1 } ^ { n }$ , the stochastic process inside the supreme is a sub-Gaussian process with intrinsic metric

$$
\begin{array} { r l } & { \displaystyle { d _ { n } ^ { 2 } ( T , \widetilde { T } ) } } \\ & { \displaystyle { = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \bigg ( \Big \lVert \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \Big \rVert _ { 2 } ^ { 2 } } } \\ & { \displaystyle { \phantom { \displaystyle { \sum _ { i \in \mathbb { N } _ { 0 } ^ { d } } \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } } } } \left. \prod _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) - \widetilde { T } _ { j } \right) ( Q _ { k } ^ { * } ( X _ { i } ) - \widetilde { z } ) ^ { j } \right. _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \widetilde { z } } ( \widetilde { z } ) } ( Q _ { k } ^ { * } ( X _ { i } ) ) ) \cdot \rho _ { k } ( X _ { i } ) } \\ & { \displaystyle { \phantom { \displaystyle { \sum _ { i \in \mathbb { N } _ { 0 } ^ { d } } \sum _ { j \in \widetilde { \mathbb { N } _ { 0 } ^ { d } } } \frac { 1 } { j ! } } } } \left. \prod _ { j \in \widetilde { \mathcal { S } } } \mathbf { 1 } _ { \mathcal { S } _ { i } ( \widetilde { z } ) } \right. \cdot \rho _ { k } ( X _ { i } ) ) \cdot \rho _ { k } ( X _ { i } ) , } \end{array}
$$

for any $T , \tilde { T } \in \bar { \mathcal { T } } ( \tilde { \delta } )$ , where the last step uses the definition of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ . The above combined with inequality (22) implies

$$
\mathbb { E } _ { \mu ^ { * } } \Big [ \operatorname* { s u p } _ { T , \tilde { T } \in \tilde { \mathcal { T } } ( \delta ) } d _ { n } ^ { 2 } ( T , \tilde { T } ) \Big ] \leq C b _ { 2 } ^ { d } \widetilde { \delta } ^ { 4 } \cdot \frac { \log n } { n } \quad \mathrm { a n d } \quad d _ { n } ( T , \tilde { T } ) \leq C \widetilde { \delta } \sum _ { \stackrel { j \in \mathbb { N } _ { 0 } ^ { d } } { | j | \leq | \delta | } } \frac { 1 } { j ! } \| T _ { j } - \widetilde { T } _ { j } \| _ { 2 } \delta _ { \tilde { \varepsilon } } ^ { | j | } .
$$

Lastly, let ${ \mathrm { ~ \mathcal { K } } } _ { n } ( \delta ) = \operatorname* { s u p } _ { T , \widetilde { T } \in \bar { \mathcal { T } } ( \delta ) } d _ { n } ^ { 2 } ( T , \widetilde { T } )$ , by applying the standard chaining via Dudley’s inequality, we can get

$$
\begin{array} { r l } & { \mathcal { R } _ { n } \big ( \widetilde { \delta } \big ) \leq \mathcal { C } \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \mu ^ { * } } \bigg [ \int _ { 0 } ^ { \mathcal { K } _ { n } ( \widetilde { \delta } ) } \sqrt { \log \frac { \widetilde { \delta } } { n } } \mathrm { d } u \bigg ] } \\ & { \quad \quad = \mathcal { C } \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \mu ^ { * } } \bigg [ \mathcal { K } _ { n } \big ( \widetilde { \delta } \big ) \cdot \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde { \delta } } { n \cdot K _ { n } ( \widetilde { \delta } ) } } \mathrm { d } u \bigg ] } \\ & { \quad \quad = \mathcal { C } \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \mu ^ { * } } \bigg [ \mathcal { K } _ { n } \big ( \widetilde { \delta } \big ) \cdot 1 ( \mathcal { K } _ { n } ( \widetilde { \delta } ) \leq b _ { 2 } ^ { * } \widetilde { \delta } ^ { 2 } \sqrt { \frac { \log n } { n } } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde { \delta } } { u \cdot \mathcal { K } _ { n } ( \widetilde { \delta } ) } } \mathrm { d } u \bigg ] } \\ & { \quad \quad \quad + \mathcal { C } \frac { 1 } { \sqrt { n } } \mathbb { E } _ { \mu ^ { * } } \bigg [ \mathcal { K } _ { n } \big ( \widetilde { \delta } \big ) \cdot 1 ( \mathcal { K } _ { n } ( \widetilde { \delta } ) > b _ { 2 } ^ { * } \widetilde { \delta } ^ { 2 } \sqrt { \frac { \log n } { n } } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { \widetilde { \delta } } { u \cdot \mathcal { K } _ { n } ( \widetilde { \delta } ) } } \mathrm { d } u \bigg ] } \\ & { \quad \quad \quad \leq \mathcal { C } _ { 1 } b _ { 2 } ^ { * } \frac { \log ( n / \widetilde { \delta } ) } { n } . } \end{array}
$$

where we have used the fact that the $u$ -covering entropy of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ relative to metric $d _ { n }$ is at most $\begin{array} { r } { C _ { 2 } \log \frac { \tilde { \delta } } { u } } \end{array}$ for $u \in ( 0 , 1 )$ where $C _ { 2 }$ depends on $( d , D )$ (at most polynomial dependence on $D$ ). By combining this with inequality (27), we obtain that for all $t \geq 1$ ,

$$
\mathbb { P } \Big ( Z _ { n } ( \widetilde { \delta } ) \geq C t ^ { 2 } b _ { 2 } ^ { \frac { d } { 2 } } \cdot \frac { \log ( n / \widetilde { \delta } ) } { n } \cdot \widetilde { \delta } ^ { 2 } \Big ) \leq 2 \exp \Big ( - c t ^ { 2 } \log ( n / \widetilde { \delta } ) \Big ) .
$$

Finally, we apply the peeling technique to extend the above high probability bound on $Z _ { n } ( { \widetilde { \delta } } )$ to the random radius $\begin{array} { r } { \widetilde { \delta } = \sum _ { { \tiny \begin{array} { c } { j \in \mathbb { N } _ { 0 } ^ { d } } \end{array} } } { \frac { 1 } { j ! } } \left\| \widehat { f } _ { k } ^ { ( j ) } - G _ { k } ^ { * , ( j ) } ( \widetilde { z } ) \right\| _ { 2 } ( \delta _ { \widetilde { z } } ) ^ { | j | } } \end{array}$ . Specifically, we first set the basic level $\begin{array} { r } { \bar { \delta } = \left( \frac { \log n } { n } \right) ^ { \frac { \beta } { d } } } \end{array}$ , and for $s = 1 , \cdots , S$ with $\begin{array} { r } { S \le C \log \frac { 1 } { \delta } } \end{array}$ , define sets

$$
\begin{array} { l }   \displaystyle { \breve { Y } _ { 0 } = \Big \{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq | \beta \} \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \left( \stackrel { d + \lfloor \beta \rfloor - 1 } { d } - 1 \right) } : \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac 1 { j ! } \| T _ { j } - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { \overline { { z } } } ) ^ { | j | } \leq \bar { \delta } \Big \} ; } } \\  { \displaystyle { \breve { Y } _ { s } = \Big \{ T = \{ T _ { j } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq | \beta \} \in [ - C _ { 0 } , C _ { 0 } ] ^ { D \times \left( \stackrel { d + \lfloor \beta \rfloor - 1 } { d } - 1 \right) } : 2 ^ { s - 1 } \bar { \delta } \leq \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } } \frac 1 { j ! } \| T _ { j } - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { \overline { { z } } } ) ^ { | j | } \leq 2 ^ { s } } } } \\ { { \displaystyle { \qquad \quad | \jmath | \leq \lfloor \beta \rfloor } } } \end{array}
$$

By applying inequality (29) to $\widetilde { \delta } = 2 ^ { s } \overline { { \delta } }$ for $s \in [ S ]$ with sufficiently large constant $t > 0$ , as $C _ { 1 } \ \leq$ $- \log ( 2 ^ { s } { \bar { \delta } } ) \leq C _ { 2 } \log n$ , we obtain that

$$
\mathbb { P } \left( Z _ { n } ( \bar { \delta } ) \geq C b _ { 2 } ^ { \frac { d } { 2 } } \frac { \log n } { n } \bar { \delta } ^ { 2 } \right) + \sum _ { s = 1 } ^ { S } \mathbb { P } \left( Z _ { n } ( 2 ^ { s } \bar { \delta } ) \geq C b _ { 2 } ^ { \frac { d } { 2 } } \frac { \log n } { n } 4 ^ { s } \bar { \delta } ^ { 2 } \right) \leq n ^ { - ( c + 1 ) } .
$$

Note that for any $T \in \widetilde { \mathcal { T } } _ { s }$ and any $s \in \{ 0 \} \cup [ S ]$ , the event $Z _ { n } ( 2 ^ { s } { \bar { \delta } } ) \leq C b _ { 2 } ^ { \frac { d } { 2 } } { \frac { \log n } { n } } 4 ^ { s } { \bar { \delta } } ^ { 2 }$ implies

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \Bigg [ \Big \| \displaystyle \sum _ { j \in \mathbb { S } _ { \alpha } ^ { \alpha } } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X ) - \tilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \tilde { z } _ { \tilde { z } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) } \Bigg ] } \\ & { \qquad \mathrm { i } j \leq 1 \| \displaystyle \sum _ { j \in \mathbb { S } _ { \alpha } ^ { \alpha } } \frac { 1 } { j ! } \left( G _ { k } ^ { * , ( j ) } ( \tilde { z } ) - T _ { j } \right) ( Q _ { k } ^ { * } ( X _ { i } ) - \tilde { z } ) ^ { j } \Big \| _ { 2 } ^ { 2 } \cdot \mathbf { 1 } _ { \mathbb { B } _ { \tilde { z } _ { \tilde { z } } ( \tilde { z } ) } ( Q _ { k } ^ { * } ( X ) ) \cdot \rho _ { k } ( X ) } \Bigg ] } \\ & { \qquad \leq c _ { 1 } b _ { 2 } ^ { \frac { d } { 2 } } \frac { \log { \displaystyle n } } { n } \Bigg \{ \tilde { \delta } ^ { 2 } + \bigg ( \displaystyle \sum _ { j \in \mathbb { S } _ { \alpha } ^ { \alpha } } \frac { 1 } { j ! } \| T _ { j } - G _ { k } ^ { * , ( j ) } ( \tilde { z } ) \| _ { 2 } ( \delta _ { \tilde { z } } ) ^ { | j | } \bigg ) ^ { 2 } \Bigg \} . } \end{array}
$$

Finally, since for any $f \in C _ { L } ^ { \beta } ( \mathbb { B } _ { 1 } ^ { d } ; R ^ { D } )$ , $T _ { f } : = \{ T _ { f , j } = f ^ { ( j ) } \} _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq \lfloor \beta \rfloor }$ must belong to some $\widetilde { \tau _ { s } }$ , the claimed result is a consequence of the two preceding displays and a simple union bound over $\tilde { z } \in \mathcal N _ { h _ { n } }$ where $\begin{array} { r } { | \mathcal { N } _ { h _ { n } } | \leq C \frac { n } { \log n } \leq C n } \end{array}$ .

# C.6 Proof of Lemma 5

Firstly by Bernstein’s inequality, it holds with probability at least $1 - n ^ { - 3 }$ that $\left| p _ { k } - { \widehat { p } } _ { k } \right| \leq C \sqrt { \frac { \log n } { n } }$ then by $p _ { k } > 0$ , for large enough $n$ , we have $\begin{array} { r } { \left| 1 - \frac { p _ { k } } { \widehat { p } _ { k } } \right| \le C \sqrt { \frac { \log n } { n } } } \end{array}$ . Thus

$$
\begin{array} { r l } & { \underset { Q \in C _ { L } ^ {  ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) f \in \mathrm { L i p } _ { 1 } \mathbb { R } ^ { d } } } { \operatorname* { s u p } } \Big ( \frac { 1 } { p _ { k } } \bigg ) \int f ( Q ( x ) ) \rho _ { k } ( x ) \mathrm { d } \mu ^ { * } - \displaystyle \int f ( z ) \tilde { \nu } _ { k , Q } ( z ) \mathrm { d } z \Big ) } \\ & { = \underset { Q \in C _ { L } ^ {  ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } } { \operatorname* { s u p } } \Big ( \frac { 1 } { p _ { k } } \bigg ) \Big ( \frac { 1 } { p _ { k } } \int f ( Q ( x ) ) \rho _ { k } ( x ) \mathrm { d } \mu ^ { * } - \frac { 1 } { \widehat { p } _ { k } n } \underset { i = 1 } { \overset { n } { \sum } } f ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) \Big ) } \\ & { \leq C \sqrt { \frac { \log n } { n } } + \frac { 1 } { p _ { k } } \underset { Q \in C _ { L } ^ { \delta } ( \mathbb { R } ^ { D } ; \mathbb { R } ^ { d } ) \ f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { d } ) } { \operatorname* { s u p } } \underset { 1 \leq n } { \operatorname* { s u p } } \Big ( \displaystyle \int f ( Q ( x ) ) \rho _ { k } ( x ) \mathrm { d } \mu ^ { * } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( Q ( X _ { i } ) ) \rho _ { k } ( X _ { i } ) \Big ) } \\ &  \leq C \sqrt { \frac { \log n } { n } } + C \underset { f \in \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { D } ) } { \operatorname* { s u p } } \Big ( \displaystyle \int f ( x ) \rho _ { k } ( x ) \mathrm { d } \mu ^ { * } - \frac { 1 } { n } \sum _  i \end{array}
$$

where the last inequality is due to the assumption that $\beta \geq 1$ . Then consider the pseudo-metric for $f , f ^ { \prime } \in \operatorname { L i p } _ { 1 } ( \mathbb { R } ^ { D } )$

$$
{ _ n } ( f , f ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left( f ( X _ { i } ) \rho _ { k } ( X _ { i } ) - f ^ { \prime } ( X _ { i } ) \rho _ { k } ( X _ { i } ) \right) ^ { 2 } } \leq \operatorname* { s u p } _ { x \in S _ { k } \cap M } | f ( x ) - f ^ { \prime } ( x ) | = \operatorname* { s u p } _ { x \in G ^ { \ast } ( Q ^ { \ast } ( S _ { k } \cap M ) ) } | f ( x ) - f ^ { \prime } ( x ) | = 1 + \operatorname* { s u p } _ { x \in G ^ { \ast } ( Q ^ { \ast } ( S _ { k } \cap M ) ) } | f ( x ) - f ^ { \prime } ( x ) | .
$$

Then by Lemma 6, we have $\log \mathbf { N } ( \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { D } ) , \| \cdot \| _ { L ^ { \infty } ( S _ { k } \cap \mathcal { M } ) } , \epsilon ) \le C \epsilon ^ { - d }$ . Choose $\delta = \left( { \textstyle { \frac { 1 } { n } } } \right) ^ { \frac { 1 } { d } }$ , we can get

$$
\frac { 1 } { \sqrt { n } } \int _ { \delta } ^ { 1 } \sqrt { \log \mathbf { N } ( \mathrm { L i p } _ { 1 } ( \mathbb { R } ^ { D } ) , \| \cdot \| _ { L ^ { \infty } ( S _ { k } \cap \mathcal { M } ) } , \epsilon ) } \mathrm { d } \epsilon \leq C n ^ { - \frac { 1 } { d } } \vee \frac { \log n } { \sqrt { n } } .
$$

Thus similar as the analysis in the proof of Lemma 3, using Dudley’s entropy integral bound and Talagrand concentration inequality, we can obtain the desired result.

# D Proof of Technical Details

# D.1 Proof of Lemma 1

Consider an aritrary $\mu ^ { * } \in \mathcal { P } ^ { * } ( d , D , \alpha , \beta , L ^ { * } )$ . Denote $\mathcal { M } = \operatorname { s u p p } ( \mu ^ { * } )$ , to begin with, we consider the following lemma.

Lemma 9 (Lemma 17 of Tang $\&$ Yang (2022)). There exist positive constants $( \tau _ { 1 } , L _ { 1 } )$ such that for any $x _ { 0 } \in \mathcal { M }$ , define $Q _ { x _ { 0 } } : \mathbb { R } ^ { D }  \mathbb { R } ^ { d }$ as $Q _ { x _ { 0 } } ( x ) = W _ { x _ { 0 } } ^ { T } ( x - x _ { 0 } )$ where $W _ { x _ { 0 } } \in \mathbb { R } ^ { D \times d }$ is an arbitrary orthonormal basis of the tangent space of $\mathcal { M }$ at $x _ { 0 }$ , then there exists a set $\widetilde { U } _ { x _ { 0 } }$ satisfying $\mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap { \mathcal { M } } \subset { \widetilde { U } } _ { x _ { 0 } } \subset { \mathcal { M } }$ and function $G _ { x _ { 0 } } \in C _ { L _ { 1 } } ^ { \beta } ( \mathbb { R } ^ { d } ; \mathbb { R } ^ { D } )$ so that

(1). $G _ { x _ { 0 } } ( \mathbb { B } _ { 1 } ^ { d } ) = \widetilde { U } _ { x _ { 0 } }$ and for any $z \in \mathbb { B } _ { 1 } ^ { d }$ , $Q _ { x _ { 0 } } ( G _ { x _ { 0 } } ( z ) ) = z$ ;   
(2). $\mu ^ { * } \circ G _ { x _ { 0 } } | _ { \mathbb { B } _ { 1 } ^ { d } } \in C _ { L _ { 1 } } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ and for any $z \in \partial \mathbb { B } _ { 1 } ^ { d }$ , $\| G _ { x _ { 0 } } ( z ) - x _ { 0 } \| \ge \tau _ { 1 }$ .

By Sobolev extension theorem, there exists a constant $L _ { 2 }$ so that for any $x _ { 0 } \in \mathcal { M }$ , there exists $Q _ { x _ { 0 } } \in$ $C _ { L _ { 2 } } ^ { \beta } ( \mathbb { R } ^ { D } )$ so that $\overline { { Q } } _ { x _ { 0 } } | _ { \widetilde { U } _ { x _ { 0 } } } = Q _ { x _ { 0 } } | _ { \widetilde { U } _ { x _ { 0 } } }$ . Since $J _ { G _ { x _ { 0 } } } ( z ) ^ { T } J _ { G _ { x _ { 0 } } } ( z )$ has uniformly lower bounded eigenvalues on $z \in \mathbb { B } _ { 1 } ^ { d }$ and $G _ { x _ { 0 } }$ is $\beta$ -smooth with $\beta > 1$ and uniformly bounded Hölder norm, there exists a small enough positive constant $r _ { 0 }$ so that for any $x _ { 0 } \in \mathcal { M }$ ,

$$
\begin{array} { r } { \displaystyle \operatorname* { s u p } _ { \boldsymbol { v } \in \mathbb { S } _ { 1 } ^ { d - 1 } = \{ \boldsymbol { v } \in \mathbb { R } ^ { d } : \| \boldsymbol { v } \| = 1 \} } \frac { \displaystyle \operatorname* { s u p } _ { \boldsymbol { z } , \boldsymbol { z } ^ { \prime } \in \mathbb { B } _ { r _ { 0 } } ^ { d } } \| ( J _ { G _ { x _ { 0 } } } ( \boldsymbol { z } ) - J _ { G _ { x _ { 0 } } } ( \boldsymbol { z } ^ { \prime } ) ) \boldsymbol { v } \| } { \| J _ { G _ { x _ { 0 } } } ( 0 ) \boldsymbol { v } \| } \leq \frac { 1 } { 3 } . } \end{array}
$$

We then choose $r ^ { * } \leq \tau _ { 1 } / 2$ to be a small enough positive constant so that for any $x _ { 0 } \in \mathcal { M }$ , $Q _ { x _ { 0 } } ( \mathbb { B } _ { r ^ { * } } ( x _ { 0 } ) \cap$ $\mathcal { M } ) \subset \mathbb { B } _ { r _ { 0 } } ^ { d }$ . For an arbitrary $k \in [ K ]$ , consider $x _ { 0 } = a _ { k } \in \mathcal { M }$ . Define $G _ { k } = G _ { x _ { 0 } }$ and $Q _ { k } = \overline { { Q } } _ { x _ { 0 } }$ . Then we have $S _ { k } \cap \mathcal { M } \subset \mathbb { B } _ { \tau _ { 1 } } ( x _ { 0 } ) \cap \mathcal { M } \subset \tilde { U } _ { x _ { 0 } }$ , and for any $x \in \mathcal { M } \cap S _ { k }$ , $x = G _ { k } ( Q _ { k } ( x ) )$ . Moreover, let $p _ { k } = \mathbb { E } _ { \mu ^ { * } } [ \rho _ { k } ( X ) ]$ , since the density of $\mu ^ { * }$ is uniformly bounded from below and $r _ { k } \geq L ^ { * }$ , we have $p _ { k }$ is also uniformly bounded from below. Furthermore, we can write $\begin{array} { r } { \nu _ { k } = ( Q _ { k } ) _ { \# } ( \frac { \mu ^ { * } \rho _ { k } } { p _ { k } } ) } \end{array}$ as

$$
\nu _ { k } ( z ) = \left\{ \begin{array} { l l } { \frac { \mu ^ { * } \left( G _ { k } ( z ) \right) \cdot \rho _ { k } \left( G _ { k } ( z ) \right) \sqrt { \operatorname* { d e t } \left( J _ { G _ { k } } ( z ) ^ { T } J _ { G _ { k } } ( z ) \right) } } { \int _ { Q _ { k } ( M \cap S _ { k } ) } \mu ^ { * } \left( G _ { k } ( z ) \right) \cdot \rho _ { k } \left( G _ { k } ( z ) \right) \sqrt { \operatorname* { d e t } \left( J _ { G _ { k } } ( z ) ^ { T } J _ { G _ { k } } ( z ) \right) } \mathrm { d } z } } & { z \in \mathbb { B } _ { 1 } ^ { d } ; } \\ { 0 } & { o . w . } \end{array} \right.
$$

Then by the $\alpha$ -smoothness of $\widetilde { \rho } _ { k } ( \cdot )$ and the uniformly lower boundness of $\textstyle \sum _ { k \in [ K ] } { \widetilde { \rho } } _ { k } ( \cdot )$ , we have $\nu _ { k } ( z ) | _ { \mathbb { B } _ { 1 } ^ { d } } \in$ $C _ { L } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ for some constant $L$ . On the other hand, by the second statement of Lemma 9 and the Lipschitzness of $G _ { m }$ , there exists a positive constant $\epsilon$ so that $Q _ { k } ( \mathcal { M } \cap S _ { k } ) \subset \mathbb { B } _ { 1 - \epsilon } ^ { d }$ . Combined with

the fact that $\nu _ { k } ( z ) = 0$ when $z \not \in Q _ { k } ( \mathcal { M } \cap S _ { k } )$ , we can obtain $\nu _ { k } ( z ) \in C _ { L ^ { * } } ^ { \alpha } ( \mathbb R ^ { d } )$ . In addition, for any $z \in \Omega _ { k } = Q _ { k } ( \mathcal { M } \cap S _ { k } )$ and any $r > 0$ , we will show that there exists $z ^ { \prime } \in \mathbb { B } _ { r } ( z )$ so that $\nu _ { k } ( z ^ { \prime } ) \ge c ( r ^ { \gamma } \wedge 1 )$ Firstly if $\| G _ { k } ( z ) - x _ { 0 } \| \leq r ^ { \ast } / 2$ , then we have

$$
\nu _ { k } ( z ) \geq c _ { 1 } \rho _ { k } ( G _ { k } ( z ) ) \geq c _ { 1 } \frac { ( \frac { 3 r _ { k } ^ { 2 } } { 4 } ) ^ { \gamma } } { M ( r ^ { \ast } ) ^ { 2 \gamma } } .
$$

On the other hand, if $\| G _ { k } ( z ) - G _ { k } ( 0 ) \| = \| G _ { k } ( z ) - x _ { 0 } \| \geq r ^ { \ast } / 2$ , denote $z = a v$ with $v = z / \| z \|$ and $a = \| z \|$ . Then we have $a \leq r _ { 0 }$ and

$$
r ^ { * } / 2 \leq \| G _ { k } ( z ) - G _ { k } ( 0 ) \| \leq c _ { 2 } \| z \| = c _ { 2 } | a | .
$$

If $r \geq a$ , then $z = a v \in \mathbb { B } _ { r } ( 0 )$ and $\nu _ { k } ( 0 ) \geq c$ for some positive constant $c$ . If $r < a$ , choose $z ^ { \prime } = ( a - r ) v$ then $z ^ { \prime } \in \mathbb { B } _ { r } ( z )$ and

$$
\begin{array} { r l } { \| G _ { k } ( z ^ { * } ) - G _ { k } ( 0 ) \| = } & { \underset { \ell \in \mathbb { R } ^ { 2 } } { \operatorname* { s u p } } \bigg ( \lambda ^ { 2 } G _ { k } ( z ^ { * } ) - \ell ^ { 2 } G _ { k } ( 0 ) \bigg ) } \\ & { = \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ( \lambda ^ { 2 } G _ { k } ( z ) - \lambda ^ { 2 } G _ { k } ( 0 ) + \lambda ^ { 2 } G _ { k } ( z ) - \lambda ^ { 2 } G _ { k } ( z ) \bigg ) } \\ & { = \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ( \lambda ^ { 2 } \mathscr { G } _ { k } ( z ) - \lambda ^ { 2 } G _ { k } ( 0 ) \bigg ) } \\ & { \overset { ( a ) } { = } \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ( \lambda ^ { 2 } G _ { k } ( z ) \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } - \lambda ^ { 2 } G _ { k } ( z ) \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ) } \\ & { = \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ( \lambda ^ { 2 } F _ { L _ { k } } ( z ) ( \alpha - r ) \nu + \lambda ^ { 2 } ( F _ { L _ { k } } ( z ) - \lambda _ { \ell _ { k } } ( z ) ) \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ) } \\ & { \overset { ( a ) } { \leq } \underset { \ell \in \mathbb { R } ^ { 3 } } { \operatorname* { s u p } } \bigg ( \ell ^ { 2 } F _ { L _ { k } } ( z ) ( \alpha - r ) \nu + \frac { r } { 2 \alpha } \big \vert G _ { k } ( z ) - G _ { k } ( 0 ) \big \vert } \\ &  = \frac { \alpha - r } { \alpha } \bigg ( \frac { \lambda } { \alpha } \bigg ( z \big ( z \big ) - G \end{array}
$$

where $( i )$ uses mean-value theorem and $( i i )$ uses equation (30) and Taylor’s theorem to obtain

$$
\begin{array} { r l } & { \displaystyle \frac { r } { 2 a } \| G _ { k } ( z ) - G _ { k } ( 0 ) \| = \frac { r } { 2 } \Big \| \int _ { 0 } ^ { 1 } J _ { G _ { k } } ( t z ) \mathrm { d } t \cdot v \Big \| } \\ & { \qquad \ge \displaystyle \frac { r } { 2 } \| J _ { G _ { k } } ( 0 ) \cdot v \| - \frac { r } { 2 } \Big \| \int _ { 0 } ^ { 1 } J _ { G _ { k } } ( 0 ) - J _ { G _ { k } } ( t z ) \mathrm { d } t \cdot v \Big \| } \\ & { \qquad \ge \displaystyle \frac { 3 r } { 2 } \operatorname* { s u p } _ { z , v ^ { \prime } \in \mathcal { B } _ { v } ^ { I } } \| ( J _ { G _ { n _ { 0 } } } ( z ) - J _ { G _ { \sigma _ { 0 } } } ( z ^ { \prime } ) ) v \| - \frac { r } { 2 } \int _ { 0 } ^ { 1 } \| ( J _ { G _ { k } } ( 0 ) - J _ { G _ { k } } ( t z ) ) v \| \mathrm { d } t } \\ & { \qquad \ge r \operatorname* { s u p } _ { z , v ^ { \prime } \in \mathcal { B } _ { v } ^ { I } } \| ( J _ { G _ { n _ { 0 } } } ( z ) - J _ { G _ { \sigma _ { 0 } } } ( z ^ { \prime } ) ) v \| } \\ & { \qquad \ge \operatorname* { s u p } _ { t \le \sigma ^ { \prime } \in \mathcal { B } _ { v } ^ { I } } \| \big ( J _ { G _ { k } } ( z ) - J _ { G _ { k } } ( z ^ { \prime } ) \big ) v \| } \\ & { \qquad \ge \operatorname* { s u p } _ { t \le s ^ { \prime } } l ^ { T } ( J _ { G _ { k } } ( z _ { l } ) - J _ { G _ { k } } ( z _ { l } ^ { \prime } ) ) r v . } \end{array}
$$

So we have

$$
\widetilde { \rho } _ { k } ( G _ { k } ( z ^ { \prime } ) ) = ( r _ { k } ^ { 2 } - \| G _ { k } ( z ^ { \prime } ) - x _ { 0 } \| ^ { 2 } ) ^ { \gamma } . \ge ( \frac { r r _ { k } ^ { 2 } } { 2 r _ { 0 } } ) ^ { \gamma } \ge ( \frac { r _ { k } ^ { 2 } } { 2 r _ { 0 } } ) ^ { \gamma } r ^ { \gamma } \ge ( \frac { ( L _ { 1 } ^ { * } ) ^ { 2 } } { 2 r _ { 0 } } ) ^ { \gamma } r ^ { \gamma } .
$$

Thus there exists constant $c$ so that

$$
\nu _ { k } ( z ^ { \prime } ) \geq c r ^ { \gamma } .
$$

Therefore, we have Assumption A holds for $\mu ^ { * }$ with $G _ { k } ^ { * } = G _ { k }$ , $Q _ { k } ^ { * } = Q _ { k }$ and $\nu _ { k } ^ { * } = \nu _ { k }$ with $k \in [ K ]$ . For

the second statement, note that by the $\beta$ -smoothness of $G _ { k } ^ { * } = G _ { k }$ , $Q _ { k } ^ { * } = Q _ { k }$ and the $\alpha$ -smoothness of $\nu _ { k } ^ { * } = \nu _ { k }$ , Assumption $\mathrm { B }$ trivially holds for approximation family $\mathcal { G } = \mathcal { G } _ { 1 }$ . Moreover, consider

$$
\overline { { \nu } } _ { k } ( z ) = \frac { \mu ^ { * } ( G _ { k } ( z ) ) \cdot \sqrt { \operatorname* { d e t } ( J _ { G _ { k } } ( z ) ^ { T } J _ { G _ { k } } ( z ) ) } } { \int _ { \mathbb { B } _ { 1 } ^ { d } } \mu ^ { * } ( G _ { k } ( z ) ) \cdot \sqrt { \operatorname* { d e t } ( J _ { G _ { k } } ( z ) ^ { T } J _ { G _ { k } } ( z ) ) } \mathrm { d } z } , \quad z \in \mathbb { B } _ { 1 } ^ { d } .
$$

Then we have νk(z) = νk(z)·ρk(Gk(z))E [ρ (G (z))] , $\overline { { \nu } } _ { k } ( z ) \in C _ { L } ^ { \alpha } ( \mathbb { B } _ { 1 } ^ { d } )$ and $\begin{array} { r } { \operatorname* { i n f } _ { z \in \mathbb { B } _ { 1 } ^ { d } } \overline { { \nu } } _ { k } ( z ) \geq L _ { 3 } > 0 } \end{array}$ . So there exists an $( \alpha + 1 )$ -smooth invertible function $V _ { k } : \mathbb { B } _ { 1 } ^ { d } \to \mathbb { B } _ { 1 } ^ { d }$ (see for example, (Caffarelli, 1996; Villani, 2009)) so that $\nu _ { 0 } = V _ { m \# } \overline { { \nu } } _ { k }$ and $\overline { { \nu } } _ { k } = V _ { m } ^ { - 1 } \# ^ { \nu _ { 0 } }$ . Therefore, $\zeta _ { 2 }$ suffices to model $\mu ^ { * }$ .

For the family G3, let V k be an (α + 1)-smooth extension of Vk|Bd to $\mathbb { R } ^ { d }$ . Note that $V _ { k }$ has $( \alpha + 1 )$ - smooth inverse and $V _ { k } ( \mathbb { B } _ { 1 - \epsilon / 2 } ^ { d } ) \subset \mathbb { B } _ { 1 - \epsilon _ { 1 } } ^ { d }$ for some positive constant $\epsilon _ { 1 }$ . We can consider $V _ { k } ^ { - 1 }$ as an $\alpha$ -smooth extension of $V _ { k } ^ { - 1 } | _ { V _ { k } ( \mathbb { B } _ { 1 - \epsilon / 2 } ^ { d } ) }$ to $\mathbb { R } ^ { d }$ . Then we can define $G _ { k } ^ { \prime } = G _ { k } \circ \overline { { V _ { k } ^ { - 1 } } }$ and $Q _ { k } ^ { \prime } = \overline { { V } } _ { k } \circ Q _ { k }$ , by the fact that $Q _ { k } ( \mathcal { M } \cap S _ { k } ) \subset \mathbb { B } _ { 1 - \epsilon } ^ { d }$ , we have for any $x \in \mathcal { M } \cap S _ { k }$ , $G _ { k } ^ { \prime } ( Q _ { k } ^ { \prime } ( x ) ) = x$ . Moreover, let

$$
\nu _ { k } ^ { \prime } ( z ) = ( Q _ { k } ^ { \prime } ) _ { \# } \frac { \mu ^ { * } \rho _ { k } } { p _ { k } } = \left\{ \begin{array} { c c } { \frac { \nu _ { 0 } ( z ) \cdot \rho _ { k } ( G _ { k } \circ V _ { k } ^ { - 1 } ( z ) ) } { \int _ { \mathbb { B } _ { 1 } ^ { d } } \nu _ { 0 } ( z ) \cdot \rho _ { k } ( G _ { k } \circ V _ { k } ^ { - 1 } ( z ) ) \mathrm { d } z } , } & { z \in V _ { k } ( \mathbb { B } _ { 1 - \epsilon / 2 } ^ { d } ) , } \\ { 0 , } & { o . w . } \end{array} \right.
$$

Using the fact that $V _ { k } ^ { - 1 } \big | _ { V _ { k } ( \mathbb { B } _ { 1 - \epsilon / 2 } ^ { d } ) }$ is $( \alpha + 1 )$ -smooth with bounded Hölder norm and $\nu _ { k } ^ { \prime } ( z ) = 0$ when $z \not \in V _ { k } ( \mathbb { B } _ { 1 - \epsilon } ^ { d } )$ , we have $\nu _ { k } ^ { \prime } \in C _ { L } ^ { \alpha } ( \mathbb { R } ^ { d } )$ for some constant $L$ . In addition, recall that for any $z _ { 0 } \in Q _ { k } ( \mathcal { M } \cap S _ { k } )$ and $r > 0$ , there exists $z _ { 0 } ^ { \prime } \in Q _ { k } ( \mathcal { M } \cap S _ { k } )$ so that $z _ { 0 } \in \mathbb { B } _ { r } ( z _ { 0 } ^ { \prime } )$ and $\widetilde { \rho } _ { k } ( G _ { k } ( z _ { 0 } ^ { \prime } ) ) \geq c _ { 1 } ( r ^ { \gamma } \wedge 1 )$ . Note that by the Lipschitzness of $V _ { k }$ , there exists a constant $L _ { 4 } \geq 1$ so that

$$
\| V _ { k } ( z _ { 0 } ) - V _ { k } ( z _ { 0 } ^ { \prime } ) \| \le L _ { 4 } \| z _ { 0 } - z _ { 0 } ^ { \prime } \| .
$$

Therefore, for any $z \in V _ { k } ( Q _ { k } ( \mathcal { M } \cap S _ { k } ) )$ and $r > 0$ , there exists $z ^ { \prime } \in V _ { k } ( Q _ { k } ( \mathcal { M } \cap S _ { k } ) ) \cap \mathbb { B } _ { r } ( z )$ , so that $\begin{array} { r } { \widetilde { \rho } _ { k } ( G _ { k } \circ V _ { k } ^ { - 1 } ( z ^ { \prime } ) ) \geq \frac { c _ { 1 } } { L _ { 4 } ^ { \gamma } } ( r ^ { \gamma } \wedge 1 ) } \end{array}$ and $\nu _ { k } ^ { \prime } ( z ) \geq c \left( r ^ { \gamma } \wedge 1 \right)$ . Therefore, when $\alpha = \beta - 1$ . Assumption A holds with $G _ { k } ^ { * } = G _ { k } ^ { \prime }$ , $Q _ { k } ^ { * } = Q _ { k } ^ { \prime }$ and $\nu _ { k } ^ { * } = \nu _ { k } ^ { \prime }$ , and Assumption B holds with $\mathcal { G } = \mathcal { G } _ { 3 }$ .

# D.2 Proof of Lemma 2

Let $\mathcal { N } _ { \epsilon }$ be the minimal $\epsilon$ -covering set of $\mathcal { M }$ , where $\epsilon$ is a number that will be chosen later, then by Lemma 9 and the compactness of $\mathcal { M }$ , we have $\vert \mathcal { N } _ { \epsilon } \vert \leq C _ { 1 } ( \frac { 1 } { \epsilon } ) ^ { d }$ where $C _ { 1 }$ is a positive constant that only depends on $( d , D , \beta , L ^ { * } )$ . Then if $\epsilon \leq \tau _ { 1 }$ , by Lemma 9, we have for any $x _ { 0 } \in \mathcal { M }$

$$
\mathcal { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon } ( x _ { 0 } ) ) = \int _ { Q _ { x _ { 0 } } ( \mathbb { B } _ { \epsilon } ( x _ { 0 } ) ) } \mu ^ { * } ( G _ { x _ { 0 } } ( z ) ) \sqrt { \operatorname* { d e t } ( J _ { G _ { x _ { 0 } } } ( z ) ^ { T } J _ { G _ { x _ { 0 } } } ( z ) ) } \mathrm { d } z \geq C _ { 2 } \epsilon ^ { d } .
$$

Then, by Bernstein’s inequality and a simple union bound argument, it holds with probability at least $1 - n _ { 1 } ^ { - c }$ that for any $x _ { 0 } \in \mathcal { N } _ { \epsilon }$ ,

$$
\Big | \frac { 1 } { n _ { 1 } } \sum _ { i \in I _ { 1 } } { \mathbf { 1 } } ( \| X _ { i } - x _ { 0 } \| \le \epsilon ) - \mathcal { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon } ( x _ { 0 } ) ) \Big | \le \frac { 1 } { 3 n _ { 1 } } \log ( \delta ) + \sqrt { \frac { 2 C _ { 2 } \epsilon ^ { d } \log ( \delta ) } { n _ { 1 } } } , \quad \delta = 2 C _ { 1 } n _ { 1 } ^ { c } ( \frac { 1 } { \epsilon } ) ^ { d } .
$$

Therefore, there exists a constant $C _ { 3 } , C$ so that when $n _ { 1 } \geq C$ , by choosing $\begin{array} { r } { \epsilon = C _ { 3 } \left( \frac { \log n _ { 1 } } { n _ { 1 } } \right) ^ { \frac { 1 } { d } } } \end{array}$ , we have it holds with probability at least $1 - n _ { 1 } ^ { - c }$ that for any $x _ { 0 } \in \mathcal { N } _ { \epsilon }$ ,

$$
\Big | \frac { 1 } { n _ { 1 } } \sum _ { i \in I _ { 1 } } \mathbf { 1 } ( \| X _ { i } - x _ { 0 } \| \le \epsilon ) - \mathcal { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon } ( x _ { 0 } ) ) \Big | \le \frac { C _ { 2 } } { 2 } \epsilon ^ { d } \le \frac { 1 } { 2 } \mathcal { P } _ { \mu ^ { * } } ( \mathbb { B } _ { \epsilon } ( x _ { 0 } ) ) .
$$

Therefore, for any $x _ { 0 } \in \mathcal { N } _ { \epsilon }$ , there exists $i \in { I } _ { 1 }$ so that $\lVert X _ { i } - x _ { 0 } \rVert \leq \epsilon$ . We can then obtain that for any $x \in \mathcal { M }$ , there exists $i \in { I } _ { 1 }$ so that $\lVert X _ { i } - x _ { 0 } \rVert \leq 2 \epsilon$ . Proof of the first statement is then completed. For the second statement, when $n _ { 1 }$ is large enough, we have $\begin{array} { r } { \epsilon = C _ { 3 } \left( \frac { \log n _ { 1 } } { n _ { 1 } } \right) ^ { \frac { 1 } { d } } \le \frac { r ^ { * } } { 1 6 } } \end{array}$ . Let $\widetilde { \mathcal { N } } _ { r ^ { * } / 4 }$ denote the minimal $r ^ { * } / 4$ -covering set of $\textstyle \bigcup _ { i \in I _ { 1 } } { \mathbb { B } } _ { 2 \epsilon } ( X _ { i } )$ . Then $| \widetilde { \mathcal { N } } _ { r ^ { * } / 4 } |$ is controlled by the minimal $r ^ { * } / 8$ -covering number of $\mathcal { M }$ . For any $x _ { 0 } \in | \widetilde { \mathcal { N } } _ { r ^ { * } / 4 } |$ , there exists an index $i \in { I } _ { 1 }$ so that $\mathbb { B } _ { 2 \epsilon } ( X _ { i } ) \cap \mathbb { B } _ { r ^ { * } / 4 } ( x _ { 0 } ) \neq \emptyset$ . Let $I _ { 2 }$ be the set of such index $_ i$ for $x _ { 0 } \in | \widetilde { \mathcal { N } } _ { r ^ { * } / 4 } |$ . Then for any $\begin{array} { r } { x \in \bigcup _ { i \in I _ { 1 } } \mathbb { B } _ { 2 \epsilon } ( X _ { i } ) } \end{array}$ , there exists $i \in { I } _ { 2 }$ so that

$$
\| x - X _ { i } \| \leq r ^ { * } / 4 + r ^ { * } / 4 + 2 \epsilon \leq \frac { 5 r ^ { * } } { 8 } .
$$

Therefore, set $M = | I _ { 2 } |$ and $\{ a _ { k } \} _ { k = 1 } ^ { K } = \{ X _ { i } \} _ { i \in I _ { 2 } }$ , we have

$$
\bigcup _ { i \in I _ { 1 } } \mathbb { B } _ { 2 \epsilon } ( X _ { i } ) \subset \bigcup _ { k \in [ K ] } \mathbb { B } _ { r ^ { * } } ( a _ { k } ) ,
$$

and

$$
\operatorname* { i n f } _ { x \in \mathcal { M } } \sum _ { k \in [ K ] } \widetilde { \rho } _ { k } ( x ) \ge ( ( r ^ { * } ) ^ { 2 } - ( \frac { 5 r ^ { * } } { 8 } ) ^ { 2 } ) ^ { \gamma } > ( \frac { ( r ^ { * } ) ^ { 2 } } { 2 } ) ^ { \gamma } .
$$

Proof is completed.