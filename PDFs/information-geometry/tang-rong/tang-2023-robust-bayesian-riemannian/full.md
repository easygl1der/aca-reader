# Robust Bayesian Inference on Riemannian Submanifold

Rong Tang $^ *$ , Anirban Bhattacharya $\ S$ , Debdeep Pati $\ S$ , and Yun Yang†

$^ *$ Department of Mathematics, The Hong Kong University of Science and Technology $\ S$ Department of Statistics, Texas A&M University †Department of Statistics, University of Illinois Urbana-Champaign

# Abstract

Manifold-valued parameters routinely arise in modern statistical applications such as in medical imaging, robotics, and computer vision, to name a few. While traditional Bayesian approaches are applicable to such settings by considering an ambient Euclidean space as the parameter space, we demonstrate the benefits of integrating manifold structure into the Bayesian framework, both theoretically and computationally. Moreover, existing Bayesian approaches which are designed specifically for manifold-valued parameters are primarily model-based, which are typically subject to inaccurate uncertainty quantification under model misspecification. In this article, we propose a robust model-free Bayesian inference for parameters defined on a Riemannian submanifold, which is shown to provide valid uncertainty quantification from a frequentist perspective. Computationally, we propose a Markov chain Monte Carlo to sample from the posterior on the Riemannian submanifold, where the mixing time, in the large sample regime, is shown to depend only on the intrinsic dimension of the parameter space instead of the potentially much larger ambient dimension. Our numerical results demonstrate the effectiveness of our approach on a variety of problems, such as multiple quantile regression, reduced-rank regression, and Fréchet mean estimation.

# Contents

1 Introduction 2   
1.1 Notation . 5   
1.2 Preliminary 5

# 2 Bayesian Inference with Manifold-supported Priors 6

3 Robust Bayesian Inference on Manifold 1 3

# 4 Posterior Sampling on Riemannian Submanifold 17

4.1 Riemannian random-walk Metropolis (RRWM) algorithm 18   
4.2 Mixing time analysis of RRWM algorithm for Bayesian RPETEL sampling . . . . 20

# 5 Numerical Illustration 2 2

5.1 Multiple quantile modeling with common slopes 22   
5.2 Spectral projectors of covariance matrices 23   
5.3 Mean parameter inference for diffusion tensors . 25

# 6 Conclusion and Discussion 27

A Notions in Riemannian Submanifold 33   
B Mixing time analysis 3 6

# C Detailed Algorithms 37

C.1 Algorithm to compute the inverse of the projection map 37   
C.2 Algorithm for sampling from Bayesian RPETEL 39   
C.3 Riemannian MALA algorithm 41

# D Auxiliary and Supporting Lemmas 42

D.1 Proof of Lemma 2 43   
D.2 Proof of Lemma 3 44

# E Proof for Bayesian RPETEL Posterior 54

E.1 Proof of Theorem 2 . 54   
E.2 Proof of Corollary 2 65   
E.3 Proof of Corollary 3 67

# F Proof for Gibbs Posterior 67

F.1 Proof of Theorem 1 . 68   
F.2 Proof of Corollary 1 71

# G Proof for Examples 73

G.1 Example 1: Reduced-Rank Multi-Response Regression . 73   
G.2 Example 2: Mean Direction of the Von Mises-Fisher Distribution 76

# H Proof for Mixing time Bound 77

H.1 Proof of Theorem 3 . 77   
H.2 Proof of Lemma 8 82   
H.3 Proof of Corollary 4 86

# I Proof of Technical Results 88

I.1 Proof of Lemma 1 88   
I.2 Proof of Lemma 5 90   
I.3 Proof of Lemma 6 93   
I.4 Proof of Lemma 7 97   
I.5 Proof of Lemma 11 97   
I.6 Proof of Lemma 12 99   
I.7 Proof of Lemma 13 100

# J Proof Related to Conductance Profile 101

.1 Proof of Lemma 10 . .

J.2 Proof of Lemma 14 . 102

# 1 Introduction

There has been a growing interest in statistical inference from complex data that are non-Euclidean, such as covariance matrices (diffusion tensor) in diffusion tensor imaging [48, 47], column orthogonal matrices (the Stiefel manifold) in orbit data analysis [21, 53] , shape objects in medical vision [33, 44], and Grassmannian-supported data in computer vision [20]. Typically, the target parameters of interest are population summary measures such as the Fréchet mean [30] or the extrinsic mean [11], both of which reside on the same manifold as the data. Non-Euclidean parameter spaces also arise when the target parameters are subject to certain constraints (e.g., low-rank, fixed sum, etc.). In such cases, one can cast the constrained parameter space as a manifold without the constraint. For instance, Grassmannian and Stiefel manifolds are widely explored in various dimensionality reduction problems [37, 79, 65]. Other constraints may be related to the rank of the optimal solutions [56, 82], which arise in various areas such as signal and image processing [42], computational finance [80] and multivariate reduced-rank regression [40, 62].

With the rapid growth in data acquisition devices, algorithms for performing statistical inference on non-Euclidean spaces encounter challenges associated with increasing sample size, complexity of the manifold, and the intrinsic dimension of the manifold. To that end, techniques for optimization on a Riemannian manifold have gained significant attention over the past decade [38, 29, 81, 15]. While Euclidean-based optimization typically uses Euclidean (stochastic) gradient descent, the Riemannian gradient, also known as the natural gradient [57], exploits the underlying data geometry to form a steepest descent direction of the cost function relative to the induced (Riemannian) metric. This leads to stability and substantial speed-up in comparison with the Euclidean stochastic gradient descent. Despite the rich development in Riemannian optimization, extending the techniques to obtain uncertainty quantification in the form of credible or confidence sets along with point estimates remains a comparatively less explored direction.

In a likelihood-based paradigm, a Bayesian approach offers a natural way to quantify uncertainty through a posterior distribution. Numerous studies have investigated Bayesian inference on specific manifolds using both parametric and more flexible semi-parametric approaches. For instance, [59, 53] focus on Bayesian inference on the Stiefel manifold. Meanwhile, [37, 55, 70] utilize Bayesian inference on the Grassmannian manifolds to perform dimensionality reduction. Moreover, Bayesian approaches have been proven useful in dealing with circular and directional statistics [13, 58, 61]. Bayesian techniques have also been effectively utilized in manifold regression [75, 52] and density estimation on manifold [7, 4]. Despite the existing literature, most of the current methods and associated sampling algorithms are tailored to specific manifolds. On the theoretical side, posterior consistency results are available [19, 7] when the observations sit on a compact manifold. However, the impact of crucial geometric properties, such as the intrinsic dimension and the curvature, on the limiting posterior distribution remains largely unexplored. Therefore, despite the significant benefits of Bayesian methods in providing a unified framework for point estimation and uncertainty quantification, the theoretical and computational advantages of incorporating manifold structures into a Bayesian posterior remains unclear.

To address this gap, we first consider a Bayesian approach that incorporates manifold information through the prior distribution, and study the asymptotic properties of the resulting Bayesian posterior supported on a Riemannian submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ . A central question in Bayesian asymptotics is the limiting shape of a posterior distribution. In a regular finitedimensional model, the classical Bernstein von-Mises (BvM; [32, Chapter 1]) theorem establishes that the posterior distribution for a $D$ -dimensional parameter $\theta$ approximately assumes a normal shape as the sample size increases to infinity. However, the same result does not apply when the posterior distribution is defined on a low-dimensional submanifold, which is singular with respect to the Lebesgue measure on $\mathbb { R } ^ { D }$ . To address the challenges, we introduce a general theoretical framework analogous to the BvM theorem, called the manifold Bernstein von-Mises theorem, to characterize the asymptotic shape of such manifold-supported posteriors. Rather than working directly with the singular posterior, we analyze the projection of the posterior onto the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ at the target parameter $\theta ^ { * }$ , in which $T _ { \theta ^ { * } } { \mathcal { M } }$ serves as a first-order approximation of $\mathcal { M }$ locally around $\theta ^ { * }$ . Moreover, we allow for non-differentiable likelihoods that relax classical smoothness assumptions, and develop our theory using gradient-like estimating functions defined on the manifold, thereby substantially broadening the scope of applicability of our theorems. Our results (c.f. Theorem 1) encompass two important regimes. In well-specified models, where the parameter $\theta$ indexes a true likelihood $p ( x | \theta ^ { * } )$ with $\theta ^ { * } \in \mathcal { M }$ , the posterior arising from a manifold-supported prior, after projection onto $T _ { \theta ^ { * } } { \mathcal { M } }$ , is asymptotically normal under mild assumptions. In particular, it possesses a “correct” covariance, in the sense that it matches the limiting frequentist covariance of the posterior’s center. Consequently, credible sets derived from the posterior asymptotically attain valid frequentist coverage, akin to the regular Euclidean case.

Moreover, we show that these credible sets can be shorter than those from the classical ambientspace posterior that ignores the manifold structure (c.f., Corollary 1), providing quantitative statistical justification for exploiting the manifold constraint. However, in misspecified models, where either the manifold assumption $\theta ^ { * } \in \mathcal { M }$ is violated or the likelihood function $p ( x | \theta ^ { * } )$ is incorrect, the posterior generally fails to deliver correct uncertainty quantification, once again generalizing similar conclusions from the Euclidean framework [23, 45].

To address the challenge of accurately specifying a distribution family that captures the true data generating distribution, [51] propose the use of the “median-of-mean” approach for robust and scalable inference on manifolds for problems that can be formalized as optimization problems over non-Euclidean spaces; [10] derive a central limit theorem for the empirical Fréchet mean of manifold-valued data, which serves as the foundation for nonparametric inference based on the Fréchet mean. Another possible direction for robust inference on manifolds is to enhance the flexibility of the model by considering mixtures of parametric models [7]. However, this approach often leads to over-parameterization and requires the usage of a multitude of nuisance parameters, leading to potential loss of statistical and computational efficiency when the focus is on simple population summary measures. Additionally, when dealing with manifold-valued parameters, Bayesian inference requires specific constructions and prior elicitation tailored to the manifold structure, making it more challenging to develop flexible nonparametric Bayesian models. Furthermore, even with more flexible models, problems associated with misspecification may still persist. One promising approach in the literature involves the use of pseudo-posterior distributions [23, 43, 25], where the parameter is treated as the solution of an estimating equation and one generates a likelihood targeting that. Specifically, we represent the parameter of interest $\theta ( { \mathcal { P } } ^ { * } )$ , viewed as a functional $\theta ( \cdot )$ evaluated at ${ \mathcal { P } } ^ { * }$ , through a population risk minimizer on a Riemannian submanifold $\mathcal { M }$ :

$$
\theta ( \mathcal { P } ^ { * } ) \in \underset { \theta \in \mathcal { M } } { \arg \operatorname* { m i n } } \mathcal { R } ( \theta ; \mathcal { P } ^ { * } ) , \quad \mathrm { w i t h ~ } \mathcal { R } ( \theta ; \mathcal { P } ^ { * } ) : = \mathbb { E } _ { \mathcal { P } ^ { * } } [ \ell ( X , \theta ) ] .
$$

Here, $\ell : \mathcal { X } \times \mathcal { M }  \mathbb { R }$ is a loss function that evaluates the compatibility of $\theta$ (the parameter of interest) with the data point $X$ , and $\mathbb { E } _ { \mathcal { P } ^ { * } }$ represents the expectation under ${ \mathcal { P } } ^ { * }$ . Observe that the maximum likelihood estimator (MLE) over a restricted parameter space can also be seen as a risk minimizer on a manifold with the loss function being the negative log-density function.

Many statistical problems can be cast as risk minimization on a manifold. For example, the Bures-Wasserstein barycenter estimation of a set of multivariate normal distributions $N ( u , \Sigma )$ ( $\boldsymbol { \mu } \in \mathbb { R } ^ { p }$ and $\Sigma \in \mathbb { S } _ { + } ^ { p \mathrm { ~ 1 ~ } }$ ) can be framed as a risk minimization over $\mathbb { R } ^ { p } \times \mathbb { S } _ { + } ^ { p }$ using a Wasserstein loss function [46]. In the context of multiple quantile modeling [50] where quantile slope coefficients are enforced to share information across quantile levels, the target parameter (matrix with rows corresponding to quantile slope coefficients at various quantile levels) can be seen as the risk minimizer with respect to a check loss function on the space of low-rank matrices. Expressing the parameter as a risk minimizer allows us to partially define a model through the loss function without fully specifying the data-generating distribution. Drawing inspiration from the first-order optimality condition for identifying a local minimizer on Riemannian submanifold, we propose a Riemannian exponentially tilted empirical likelihood (RETEL) function, which replaces the standard parametric likelihood. Moreover, a penalty term associated with the empirical risk function is added to ensure the concentration of the posterior around the global minimizer. We refer to the resulting posterior as the Bayesian Riemannian penalized exponentially tilted empirical likelihood (RPETEL) posterior, which extends the Euclidean PETEL [67]. As we will demonstrate, the Bayesian RPETEL posterior provides three forms of robustness: (1) It satisfies a Manifold Bernstein-von Mises theorem (c.f., Theorem 2), yielding automatically calibrated uncertainty quantification without requiring a correctly specified likelihood. Establishing this result necessitates new analytical tools to handle posterior singularity, to represent the posterior in local coordinates, and to control curvature-induced distortions absent in the Euclidean setting. (2) Even when the global risk minimizer over the ambient space $\mathbb { R } ^ { D }$ lies off the manifold or does not exist, the mean of the posterior remains meaningful – it closely matches the risk minimizer over the manifold, and the covariance matrix of the posterior matches that of the frequentist sampling distribution of this mean; (3) In a well-specified setting where both the likelihood and the manifold assumption are correct, the posterior is asymptotically equivalent to the standard Bayesian posterior with the same manifold-supported prior. Hence, the proposed Bayesian RPETEL posterior is robust to model misspecification, while incurring no efficiency loss under correct specification.

Beyond the appealing asymptotic properties of the proposed posterior, we also demonstrate computational advantages from the incorporation of low-dimensional manifold structure. Specifically, we develop a Riemannian Random-walk Metropolis (RRWM) algorithm for sampling from posterior distributions defined on submanifolds, which adapts the classical Random-walk Metropolis (RWM) algorithm to the manifold setting. We show that, in the large-sample regime, the RRWM algorithm can be applied for sampling from the derived posterior with a mixing time that is almost linear in the intrinsic dimension $d$ (c.f. Corollary 4). This is different from the conventional RWM algorithm for sampling from the standard Bayesian posterior in the ambient space $\mathbb { R } ^ { D }$ , where the mixing time is at least linear in the ambient dimension $D$ [31].

The rest of the paper is organized as follows. Section 1.1 provides a summary of the notation used throughout the paper, while Section 1.2 offers a brief background on Riemannian submanifolds. In Section 2.1, we discuss the non-asymptotic properties of the Bayesian posterior on submanifolds, highlighting its advantage over the Euclidean counterpart that does not incorporate the manifold structure, as well as its limitation. Section 3 presents our proposed Bayesian RPETEL posterior for statistical inference on Riemannian submanifolds without fully specifying the model. Section 4 presents a Riemannian Random-Walk Metropolis algorithm for posterior sampling and analyzes its computational complexity. Section 5 reports numerical studies, and Section 6 concludes with a discussion. Proofs and other technical details are deferred to a Supplementary Material.

# 1.1 Notation

We use $0 _ { d }$ to denote the $d$ -dimensional all zero vector, and may omit the subscript when no ambiguity may arise. We use $B _ { r } ( x )$ to denote the closed ball centered at $x$ with radius $r$ (under the $\ell _ { 2 }$ distance) in the Euclidean space. We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and reserve $\| \cdot \|$ for the $\ell _ { 2 }$ norm (that is, suppress the subscript when $p = 2$ ). For a topological space $\mathcal { X }$ , we use ${ \mathcal { X } } ^ { n } = \{ ( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { n } ) : \forall i$ , $x _ { i } \in \mathcal { X } \}$ to denote the $n$ -fold Cartesian product of $\mathcal { X }$ . We use $P ( \Omega )$ to denote the set of probability measures on space $\Omega$ . For a measure $\mu \in P ( \Omega )$ and a map $G : \Omega \to \Omega ^ { \prime }$ , we use $\nu = G _ { \# } \mu \in P ( \Omega ^ { \prime } )$ to denote the push-forward measure of $\mu$ by $G$ so that $\nu ( \mathcal { A } ) = \mu ( G ^ { - 1 } ( \mathcal { A } ) )$ holds for any measurable set $\mathcal { A }$ on $\Omega ^ { \prime }$ . A $k$ -dimensional real random vector $X$ is said to follow a multivariate normal distribution, denoted $\textstyle { \mathcal { N } } ( { \boldsymbol { \mu } } , { \boldsymbol { \Sigma } } )$ , if there exists a full-rank matrix $A \in \mathbb { R } ^ { k \times l }$ (with $l \leq k$ ) so that $\Sigma = A A ^ { T }$ and $X = A Z + \mu$ , where $Z$ is an $l$ -dimensional standard normal random vector – when $l < k$ , the distribution is said to be singular. For a matrix $A \in \mathbb { R } ^ { D \times D }$ , we use $A ^ { \dag } \in \mathbb { R } ^ { D \times D }$ to denote its pseudo-inverse (Moore-Penrose inverse), and the pseudo-determinant of $A$ is defined as $\begin{array} { r } { | A | _ { + } = \operatorname* { l i m } _ { \alpha \to 0 } { \frac { \operatorname* { d e t } ( A + \alpha I _ { D } ) } { \alpha ^ { D - \operatorname { r a n k } ( A ) } } } } \end{array}$ , where $\operatorname* { d e t } ( A )$ denotes the usual determinant, $I _ { D }$ denotes the $D \times D$ identity matrix, and $\operatorname { r a n k } ( A )$ denotes the rank of $A$ For a metric space $( \mathcal { F } , \rho )$ , let $\mathbf { N } ( \mathcal { F } , \rho , \varepsilon )$ denote the $\varepsilon$ -covering number of $\mathcal { F }$ with respect to $\rho$ and define the metric entropy as $\log \mathbf { N } ( \mathcal { F } , \rho , \varepsilon )$ .

# 1.2 Preliminary

Suppose we observe i.i.d. copies $X ^ { ( n ) } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ of a random variable $X \in { \mathcal { X } }$ from an unknown distribution ${ \mathcal { P } } ^ { * }$ . Henceforth, we use $\mathbb { E }$ and $\mathbb { P }$ to denote expectation and probability under ${ \mathcal { P } } ^ { * }$ . Our target is to estimate a parameter $\theta ^ { * } = \theta ( \mathcal { P } ^ { * } )$ associated with the unknown population ${ \mathcal { P } } ^ { * }$ based on the finite observations $X ^ { ( n ) }$ , and quantify the estimation uncertainty. In many cases, the functional $\theta ( { \mathcal { P } } ^ { * } )$ can take values in a Riemannian submanifold, such as in Bures-Wasserstein barycenter estimation, Fréchet mean estimation, reduced-rank multiple quantile regression, among others. In order to discuss the properties of the parameter space, it is necessary to revisit some essential definitions from manifold theory; see [15] for book-level details.

Let $\mathcal { M }$ be a $d$ -dimensional Riemannian submanifold embedded in $\mathbb { R } ^ { D }$ . Intuitively speaking, a manifold is a topological space that locally resembles a Euclidean space. Formally, the definition is as follows:

Definition 1 (Submanifold). A subset $\mathcal { M }$ of $\mathbb { R } ^ { D }$ is a $d$ -dimensional Riemannian submanifold if for every point $\theta$ in $\mathcal { M }$ , there exists a neighbourhood $U _ { \theta }$ of $\theta$ on $\mathcal { M }$ and an open set $V _ { \theta } \subseteq \mathbb { R } ^ { d }$ , such that there exists a homeomorphism $\xi _ { \theta }$ that maps $V _ { \theta }$ to $U _ { \theta }$ , that is, $\xi _ { \theta } : V _ { \theta } \to U _ { \theta }$ is bijective and both $\xi _ { \theta }$ and $\xi _ { \theta } ^ { - 1 }$ are continuous maps. Moreover, the differential $\mathcal { D } \xi _ { \theta } ( z ) [ \cdot ]$ of $\xi _ { \theta } ( \cdot )$ at $z$ exists and is injective for every $z \in V _ { \theta }$ . The pair $( U _ { \theta } , \xi _ { \theta } ^ { - 1 } )$ is called a local coordinate chart near $\theta$ , with $\xi _ { \theta } ^ { - 1 }$ the coordinate map and $\xi _ { \theta }$ a local parameterization. We refer to $D$ as the ambient dimension and $d$ as the intrinsic dimension of $\mathcal { M }$ .

The tangent space of $\mathcal { M }$ at a point $\theta \in \mathcal { M }$ , denoted as $T _ { \theta } \mathcal { M }$ , is a linearization of $\mathcal { M }$ locally around $\theta$ , which contains possible directions (tangent vector) in which one can tangentially pass through $\theta$ . This linearization forms a foundation for extending many notions and techniques in Euclidean space to the Riemannian submanifold. For example, for a smooth function $f$ acting on $\mathcal { M }$ , by considering smooth extension $\overline { { f } }$ of $f$ to a neighborhood of $\mathcal { M }$ in $\mathbb { R } ^ { D }$ , the so-called Riemannian gradient grad $f ( \theta )$ of $f$ at $\theta \in \mathcal { M }$ can be thought of as the orthogonal projection of the (Euclidean) gradient of $\overline { { f } }$ at $\theta$ onto $T _ { \theta } \mathcal { M }$ . Therefore, the Riemannian gradient gives the steepest ascent tangent direction for $f$ along the manifold, and we have the so-called first-order necessary optimality condition that any local minimizer $\theta$ of a smooth function $f : \mathcal { M }  \mathbb { R }$ satisfies grad $f ( \theta ) = 0$ . This first-order necessary optimality condition serves as a main motivation for our developed method in Section 3.

The detailed definitions of all the notions mentioned above are available in Appendix A. Throughout, we assume the manifold is $C ^ { 3 }$ -smooth locally around the risk minimizer $\theta ^ { * }$ , as specified below. This smoothness guarantees that, near $\theta ^ { * }$ , the manifold is well-approximated by its tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ . Such assumptions are standard in manifold-based inference [1, 26] where $\mathcal { M }$ is typically assumed to be at least $C ^ { 2 }$ -smooth. Our stronger $C ^ { 3 }$ smoothness assumption enables us to establish the desired BvM result with a root- $_ n$ convergence rate.

Definition 2 (Local $C ^ { 3 }$ -Smoothness). Let $\mathcal { M }$ is a $d$ -dimensional submanifold embedded in $\mathbb { R } ^ { D }$ and let $\theta \in \mathcal { M }$ . We call $\mathcal { M }$ is locally $C _ { r , L } ^ { 3 }$ -smooth at $\theta$ if there exist constants $L > 0$ and neighborhoods $U _ { \theta } \subset \mathcal { M }$ , $V _ { \theta } \subset T _ { \theta } { \mathcal { M } }$ such that

1. $B _ { r } ( \theta ) \cap { \mathcal { M } } \subset U _ { \theta }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta } { \mathcal { M } } \subset V _ { \theta }$ ;

2. the map $\psi _ { \theta } : U _ { \theta } \to V _ { \theta }$ defined by $\psi _ { \boldsymbol { \theta } } ( x ) = \mathrm { P r o j } _ { T _ { \boldsymbol { \theta } } \mathcal { M } } ( x - \theta )$ is a bijection onto $V _ { \theta }$ ;

3. the inverse $\phi _ { \theta } : V _ { \theta } \to U _ { \theta }$ of $\psi _ { \theta }$ is thrice Fréchet differentiable, and its Fréchet derivatives up to order three have operator norms uniformly bounded by $L$ .

# 2 Bayesian Inference with Manifold-supported Priors

In the classical Bayesian framework, we model the unknown data distribution ${ \mathcal { P } } ^ { * }$ by a parametric family $\{ p ( x | \theta ) : \theta \in \mathbb { R } ^ { D } \}$ . Prior knowledge about $\theta$ is incorporated through a prior distribution, which is updated to a posterior using Bayes’ theorem. If the model is correctly specified, i.e., if ${ \mathcal P ^ { * } = p ( x | \theta ^ { * } ) }$ for some $\theta ^ { * } \in \mathbb { R } ^ { D }$ , then the celebrated Bernstein-von Mises (BvM) theorem ensures under mild regularity conditions that credible regions derived from the posterior will asymptotically be confidence sets of the same level. In many application, however, the parameter of interest is subject to certain constraint – for example, it may have unit norm, sum to one, or be low-rank. Such constraints can be represented by viewing the parameter as living on a $d$ -dimensional Riemannian submanifold $\mathcal { M }$ embedded in the ambient space $\mathbb { R } ^ { D }$ . We can then place a prior directly on $\mathcal { M }$ and perform Bayesian inference. For instance, in many models for multivariate and relational data, the posterior takes the form of a matrix Bingham-von Mises-Fisher distribution under a uniform prior on the Stiefel manifold [36]. In Bayesian estimation of a covariance matrix, a natural conjugate prior for the normal sampling model is the inverse Wishart distribution [2], which is defined on the space of real-valued positive-definite matrices. The inverse Wishart prior also provides conjugacy for diffusion tensor data sets modeled by the Wishart distribution. A key difference from the unconstrained Euclidean setting is that the posterior, which is supported on a lower-dimensional Riemannian submanifold, is singular with respect to the Lebesgue measure on $\mathbb { R } ^ { D }$ . As a result, the usual Bernstein-von Mises theorem does not apply in its standard form. On the frequentist side, several studies have investigated the asymptotic behavior of the empirical risk minimizer over the Riemannian manifold $\mathcal { M }$ , under local coordinates in $\mathbb { R } ^ { d }$ specified by a chart around the target parameter $\theta ^ { * }$ . For example, [12, 9] show that the local coordinate representation of the empirical Fréchet mean is asymptotically normal around that of the population Fréchet mean. However, only limited general theory has been developed to study the theoretical properties of Bayesian inference in the manifold setting.

To bridge this gap, we analyze the shape of the posterior, denoted by $\Pi ( \cdot | X ^ { ( n ) } )$ , in two complementary ways. First, we study $\Pi ( \cdot | X ^ { ( n ) } )$ after projecting it onto the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ of $\mathcal { M }$ at $\theta ^ { * }$ . The tangent space provides a first-order Euclidean approximation to the manifold $\mathcal { M }$ near $\theta ^ { * }$ , which enables the use of conventional analytical tools in Euclidean space while preserving the local geometric structure of the manifold. Moreover, in the vicinity of $\theta ^ { * }$ , points within $\mathcal { M }$ have a one-to-one correspondence with tangent vectors via the projection map onto $T _ { \theta ^ { * } } { \mathcal { M } }$ . Consequently, this projection can be viewed as a local chart around $\theta ^ { * }$ by identifying tangent vectors as $d$ -dimensional coordinates using an orthonormal basis of the tangent space. This leads to a clean normal approximation for the projected posterior with an asymptotic covariance matrix that is independent of the choice of local chart. Second, we investigate one-dimensional summaries $f ( \theta )$ with $f : \mathcal { M }  \mathbb { R }$ smooth, and $\theta \sim \Pi ( \cdot | X ^ { ( n ) } )$ , and study their asymptotic normality. This allows us to directly compare the variance of the push-forward posterior $f _ { \# } \Pi ( \cdot | X ^ { ( n ) } )$ with that of the frequentist sampling distribution of its mean, thereby assessing whether credible intervals for $f ( \theta )$ remain valid in large samples.

To make our theoretical results broadly applicable, we adopt a general loss-function-based framework. In the classical Bayesian setting, the loss function $\ell ( X , \theta )$ corresponds to the negative log-likelihood, $- \log p ( X | \theta )$ , and the posterior is likelihood-based. However, for complex data, specifying a flexible and accurate probabilistic model with parameters constrained to a manifold can be challenging. For example, in diffusion tensor imaging, inference on the Fréchet or extrinsic mean requires a well-specified distribution on the space of positive semidefinite matrices, which is often difficult to formulate. To mitigate strong modeling assumptions, we define the target parameter as a risk minimizer – that is, a minimizer of an expected loss – and adopt a Gibbs posterior [8, 66, 43, 23] constructed from the corresponding empirical loss. This approach preserves the Bayesian updating mechanism while decoupling inference from full likelihood specification, and it naturally accommodates manifold-valued parameters. Our theoretical results are developed within this general risk-minimization and Gibbs posterior framework, with the classical Bayesian case recovered by taking the loss function to be the negative log-likelihood.

Let $\mathcal { M }$ be a $d$ -dimensional Riemannian submanifold, and let $S _ { \Pi } \subseteq { \mathcal { M } }$ denote the support of the prior $\Pi$ . Let $\ell : \mathcal { X } \times \mathcal { M } \to \mathbb { R }$ be the loss function, and define the population risk $\mathcal { R } ( \theta ) = \mathbb { E } _ { \mathcal { P } ^ { * } } [ \ell ( X , \theta ) ]$ . The (Gibbs) posterior is defined as

$$
\Pi ( \mathrm { d } \theta | X ^ { ( n ) } ) = { \frac { \exp ( - \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) ) \Pi ( \mathrm { d } \theta ) } { \int _ { \cal M } \exp ( - \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) ) \Pi ( \mathrm { d } \theta ) } } = { \frac { \exp ( - \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) ) \Pi ( \mathrm { d } \theta ) } { \int _ { S _ { \Pi } } \exp ( - \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) ) \Pi ( \mathrm { d } \theta ) } } .
$$

Assume the risk minimizer $\theta ^ { * } = \arg \operatorname* { m i n } _ { \theta \in \mathcal { M } } \mathcal { R } ( \theta )$ exists and is unique. Fix positive constants $L , r , \beta _ { 1 } \in ( 0 , \infty )$ , $\beta _ { 2 } \in ( 0 , 1 ]$ , and positive integers $d , D$ with $d \leq D$ . We impose the following four assumptions.

Assumption 1 (Parameter space regularity). $\mathcal { M }$ is a $d$ -dimensional Riemannian submanifold of $\mathbb { R } ^ { D }$ and is locally $C _ { r , L } ^ { 3 }$ -smooth at $\theta ^ { * }$ .

This assumption requires the manifold $\mathcal { M }$ to be locally $C ^ { 3 }$ -smooth around $\theta ^ { * }$ so that the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ provides a valid local approximation of $\mathcal { M }$ near $\theta ^ { * }$ .

Assumption 2 (Prior regularity). The support $S _ { \Pi }$ of $\Pi$ satisfies that $B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subset S _ { \Pi } \subset$ $\mathbb { B } _ { L } ( 0 _ { D } ) \cap \mathcal { M }$ . Moreover, $\Pi$ admits a density $\pi$ with respect to the volume measure of $\mathcal { M }$ , such that $\pi ( \theta ^ { * } ) > 1 / L$ and, for all $\theta \in B _ { 1 / L } ( \theta ^ { * } ) \cap S _ { \Pi }$ , $\left| \pi ( \theta ) - \pi ( \theta ^ { * } ) \right| \leq L \left\| \theta - \theta ^ { * } \right\|$ .

This assumption requires the prior to assign positive mass to a fixed-radius neighborhood of $\theta ^ { * }$ on $\mathcal { M }$ and have a Lipschitz continuous density with respect to the volume measure on $\mathcal { M }$ in a neighborhood of $\theta ^ { * }$ .

Assumption 3 (Risk regularity). For all $\theta \in S _ { \Pi }$ , $\begin{array} { r } { | \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) | \geq \frac { 1 } { L } \| \theta - \theta ^ { * } \| ^ { 2 } } \end{array}$ . There exists $\overline { { \mathcal { R } } } : B _ { r } ( \theta ^ { * } )  \mathbb { R }$ that coincides with $\mathcal { R }$ on $B _ { r } ( { \theta ^ { * } } ) \cap S _ { \Pi }$ , where $\textstyle { \overline { { \mathcal { R } } } }$ has uniformly $L$ -bounded partial derivatives up to order three.

This assumption requires the risk function $\mathcal { R }$ to increase locally in a quadratic fashion away from its minimizer $\theta ^ { * }$ and admit a smooth extension to a neighborhood of $\theta ^ { * }$ in the ambient space.

Assumption 4 (Regularity of the loss and gradient-like proxy). There exists a function $b : \mathcal { X } \to \mathbb { R } _ { \geq 0 }$ with . M $\mathbb { E } [ \exp { \big ( } { \big ( } { \frac { b ( X ) } { L } } { \big ) } ^ { \beta _ { 1 } } { \big ) } ] \leq 1$ such tha a map $x \in \mathcal { X }$ $\theta , \theta ^ { \prime } \in S _ { \Pi }$ $| \ell ( x , \theta ) - \ell ( x , \theta ^ { \prime } ) | \leq$ $b ( x ) \| \theta - \theta ^ { \prime } \|$ $g : \mathcal { X } \times S _ { \Pi } \to \mathbb { R } ^ { D }$ $g ( x , \theta ) \ \in \ T _ { \theta } { \mathcal { M } }$ $\| g ( x , \theta ) \| \leq b ( x )$ for all $( x , \theta ) \in \mathcal { X } \times S _ { \Pi }$ , such that:

1. (Gradient-like behavior and population-level smoothness). For any $\theta \in \mathbb { B } _ { r } ( \theta ^ { * } ) \cap S _ { \Pi }$ , $\mathbb { E } [ g ( X , \theta ) ] = \operatorname { P r o j } _ { T _ { \theta } \mathcal { M } } ( \nabla \overline { { \mathcal { R } } } ( \theta ) )$ , and $\begin{array} { r } { \mathbb { E } [ \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| ^ { 2 } ] \le L \| \theta - \theta ^ { * } \| ^ { 2 \beta _ { 2 } } } \end{array}$ . Moreover, for any $\theta , \theta ^ { \prime } \in \mathbb { B } _ { r } ( \theta ^ { * } ) \cap S _ { \Pi }$ , $\begin{array} { r } { \mathbb { E } [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) ^ { 2 } ] \leq L \| \theta - \theta ^ { \prime } \| ^ { 2 + 2 \beta _ { 2 } } } \end{array}$ . For any $\eta \in T _ { \theta ^ { \ast } } \mathcal { M }$ with unit norm, $\begin{array} { r } { \mathbb { E } [ ( \eta ^ { T } g ( X , \theta ^ { * } ) ) ^ { 2 } ] \ge \frac { 1 } { L } } \end{array}$ .

2. (Metric entropy bounds for $g ( x , \cdot ) )$ . For any $n \in \mathbb { N } ^ { + }$ and sample $\{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \} \in { \mathcal { X } } ^ { n }$ , define the pseudo-metric $\begin{array} { r } { d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } } } \end{array}$ . Then for any $\varepsilon > 0$ , $\begin{array} { r } { \log \mathbf { N } ( B _ { r } ( \theta ^ { * } ) \cap S _ { \Pi } , d _ { n } ^ { g } , \varepsilon ) \leq \operatorname* { m a x } ( 0 , L \log n + L \log ( \frac { \sqrt { n ^ { - 1 } \sum _ { i = 1 } ^ { n } b ( X _ { i } ) ^ { 2 } } } { \varepsilon } ) ) } \end{array}$ .

Similar assumptions also appear in [69, 67]. Notably, we do not require the loss function $\ell$ to be differentiable. Instead, we introduce a gradient-like proxy $g ( \cdot , \cdot )$ whose expectation $\mathbb { E } [ g ( X , \cdot ) ]$ coincides with the Riemannian gradient of the population risk $\mathcal { R } ( \cdot )$ . In particular, for each fixed $X \in { \mathcal { X } }$ , if $\ell ( X , \cdot )$ is differentiable on $\mathcal { M }$ , we may take $g ( X , \cdot )$ to be its Riemannian gradient. When $\ell ( X , \cdot )$ is not differentiable but admits a Lipschitz extension ${ \overline { { \ell } } } ( X , \cdot )$ to the ambient space, we define $g ( X , \theta )$ as the projection onto $T _ { \theta } \mathcal { M }$ of any subgradient of $\theta \mapsto \overline { { \ell } } ( X , \theta )$ . The parameter $\beta _ { 2 }$ characterizes the average smoothness of $g ( X , \cdot )$ . Specifically, $\mathbb { E } [ \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| ^ { 2 } ]$ controls the Lipschitz behavior of $g ( X , \cdot )$ , while $\mathbb { E } [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) ^ { 2 } ]$ bounds the mean squared error of the first-order approximation to $\ell ( X , \cdot )$ with $g$ in place of the gradient. When $\theta \mapsto \ell ( X , \theta )$ is twice differentiable on $\mathcal { M }$ for every $X$ , we have $\beta _ { 2 } = 1$ . If $\theta \mapsto \ell ( X , \theta )$ is not everywhere differentiable, $\beta _ { 2 }$ can be smaller than one. For example, [69] shows that in Bayesian quantile regression, where $\ell$ is the non-smooth check loss, the assumptions hold with $\beta _ { 2 } = \textstyle { \frac { 1 } { 2 } }$ . As shown in Theorem 1, a larger value of $\beta _ { 2 }$ implies a faster convergence rate of the posterior $\Pi ( \cdot | X ^ { ( n ) } )$ to its limiting distribution. Finally, the metric-entropy condition ensures uniform control of the random fluctuations of $\textstyle n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta )$ around the Riemannian gradient of the population risk ${ \mathcal { R } } ( \theta )$ .

We now state the main result. Let $P _ { \theta ^ { \ast } } \in \mathbb { R } ^ { D \times D }$ be the projection matrix onto $T _ { \theta ^ { * } } { \mathcal { M } }$ , and let $\widetilde { \mathcal { H } } _ { \theta ^ { * } }$ denote the Jacobian matrix of the map $\theta \mapsto \operatorname { P r o j } _ { { T _ { \theta } } \mathcal { M } } ( \nabla \overline { { \mathcal { R } } } ( \theta ) )$ evaluated at $\theta = \theta ^ { * }$ , where $\overline { { \mathcal { R } } } ( \cdot )$ is the ambient-space extension of $\mathcal { R } ( \cdot )$ . Then we define $\mathcal { H } _ { \theta ^ { \ast } } = P _ { \theta ^ { \ast } } \widetilde { \mathcal { H } } _ { \theta ^ { \ast } } P _ { \theta ^ { \ast } }$ as the Riemannian Hessian matrix of $\mathcal { R } ( \cdot )$ at $\theta ^ { * }$ . Also, set $\Delta _ { \theta ^ { * } } = \mathbb { E } [ g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } ]$ . We use $\phi _ { \theta ^ { * } } : V _ { \theta ^ { * } } \to U _ { \theta ^ { * } }$ for the local inverse of $\operatorname { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \cdot - \theta ^ { * } )$ , as defined in Definition 2.

Theorem 1 (Manifold BvM Theorem for Gibbs Posterior). Suppose Assumptions 1-4 hold. Let ${ \widehat { \theta } } : { \mathcal { X } } ^ { n }  S _ { \Pi }$ denote the empirical risk minimizer, that is, $\begin{array} { r } { \hat { \theta ( X ^ { ( n ) } ) } \in \arg \operatorname* { m i n } _ { \theta \in S _ { \Pi } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) } \end{array}$ Then, there exists a set $A \subset \mathcal { X } ^ { n }$ with $\mathbb { P } ( X ^ { ( n ) } \in \mathcal { A } ) \geq 1 - n ^ { - 1 }$ such that

1. There exists a constant $C > 0$ such that, for every dataset $X ^ { ( n ) } \in { \mathcal { A } }$ ,

$$
\mathrm { T V } \Big ( \Pi ( \cdot | X ^ { ( n ) } ) , [ \phi _ { \theta ^ { * } } ] _ { \# } \big [ \mathrm { \it { N } } \big ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \widehat { \theta } ( X ^ { ( n ) } ) - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) \big | _ { V _ { \theta ^ { * } } } \big ] \Big ) \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

where recall that $\mathcal { H } _ { \theta ^ { \ast } } ^ { \dagger }$ denotes the Moore-Penrose inverse of $\mathcal { H } _ { \theta ^ { \ast } }$ . Moreover, when $n$ is suffiiciently large, the extrinsic posterior mean $\begin{array} { r } { \widehat { \theta } _ { p } ( X ^ { ( n ) } ) : = \arg \operatorname* { m i n } _ { y \in \mathcal { M } } \big \| y - \int _ { \mathcal { M } } \theta \operatorname { \Pi } \mathrm { H } ( \mathrm { d } \theta | X ^ { ( n ) } ) \big \| ^ { 2 } } \end{array}$ is uniquely defined and satisfies ∥θbp(X(n)) − θb(X(n))∥ ≤ C (log n) β1 +1β2+1 .

2. For any fixed positive constants $L _ { 1 }$ and $r _ { 1 }$ , there exists a constant $C > 0$ such that, for every function $f : \mathbb { R } ^ { D }  \mathbb { R }$ satisfying that (1) all partial derivatives of $f$ up to second order are bounded in absolute value by $L _ { 1 }$ on $\mathbb { B } _ { r _ { 1 } } ( \theta ^ { * } )$ , and (2) $\begin{array} { r } { \| \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \nabla f ( \theta ^ { * } ) ) \| \ge \frac { 1 } { L _ { 1 } } } \end{array}$ , the following holds:

(a) for every dataset $X ^ { ( n ) } \in { \mathcal { A } }$ ,

$$
\operatorname { T V } \Big ( f _ { \# } \Pi ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \big ( f ( \widehat { \theta } ( X ^ { ( n ) } ) ) , n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \nabla f ( \theta ^ { * } ) \big ) \Big ) \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

$\begin{array} { r l } & { ( b ) \ \sqrt { n } \cdot \big ( f \big ( \widehat { \theta } ( X ^ { ( n ) } ) \big ) - f ( \theta ^ { * } ) \big ) \ \to \ \mathcal { N } \big ( 0 , \nabla f ( \theta ^ { * } ) ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \nabla f ( \theta ^ { * } ) \big ) } \\ & { \quad n \to \infty . } \end{array}$ in distribution as

The proof of Theorem 1 is provided in Appendix F. In the proof, we introduce a one-toone change of variables $y = W _ { \theta ^ { * } } ^ { T } \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \theta - \theta ^ { * } ) \in \mathbb { R } ^ { d }$ locally around $\theta ^ { * }$ , where $W _ { \theta ^ { * } }$ is an orthonormal basis of the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ . This transformation allows us to convert the analysis to the Euclidean space $\mathbb { R } ^ { d }$ . By exploiting the regularity properties of both the manifold and the loss function, we derive a Bernstein–von Mises type result for the posterior distribution after this variable transformation.

To interpret the first result, note that the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ locally approximates the manifold $\mathcal { M }$ as a flat space. The map $\theta \mapsto \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \theta - \theta ^ { * } )$ projects points from the manifold onto this tangent space, and $V _ { \theta ^ { \ast } }$ denotes a neighborhood on the tangent space where this projection is one-to-one, so that each tangent vector in $V _ { \theta ^ { \ast } }$ corresponds to a unique point on the manifold. The map $\phi _ { \theta ^ { * } }$ is the inverse of this projection, mapping points back from the tangent space to the manifold. The first statement in Theorem 1 then establishes that, after projecting the posterior distribution onto the tangent space, the distribution of the resulting tangent vectors is well-approximated by a normal distribution centered at the projected empirical risk minimizer. Because the projection is invertible on $V _ { \theta ^ { * } }$ , we can also map these normal vectors back to the manifold through $\phi _ { \theta ^ { * } }$ , thereby obtaining a direct approximation of the posterior distribution on $\mathcal { M }$ . Furthermore, the posterior mean projected onto $\mathcal { M }$ , denoted by ${ \widehat { \theta } } _ { p } ( X ^ { ( n ) } )$ , serves as a point estimator that closely aligns with the empirical risk minimizer.

The second statement in Theorem 1 concerns one-dimensional functionals of the parameter, given by mappings $f ( \theta )$ . Specifically, it states that for any smooth function $f$ with bounded derivatives and a nonzero Riemannian gradient at $\theta ^ { * }$ , the posterior distribution of $f ( \theta )$ given data $X ^ { ( n ) }$ is well-approximated by a normal distribution centered at $f ( \widehat { \theta } ( X ^ { ( n ) } ) )$ . An important subtlety is that the variance in the posterior normal approximation of $f ( \theta )$ , given by $n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \nabla f ( \theta ^ { * } )$ , generally differs from the asymptotic variance of the sampling distribution of $f ( \widehat { \theta } ( X ^ { ( n ) } ) )$ , which is $n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { \dag } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dag } \nabla f ( \theta ^ { * } )$ . Consequently, the posterior typically fails to provide correct uncertainty quantification for $f ( \theta )$ ; that is, posterior credible intervals may not achieve valid frequentist coverage. However, when $\mathcal { H } _ { \theta ^ { \ast } } = \Delta _ { \theta ^ { \ast } }$ , the two variances coincide, and the posterior delivers asymptotically correct uncertainty quantification. This equivalence (see [23, 45] for Euclidean analogues) holds, for instance, under correct model specification—when the loss function corresponds to the negative log-likelihood, $\ell ( x , \theta ) = - \log p ( x \mid \theta )$ , and the data are i.i.d. from $p ( x \mid \theta ^ { * } )$ .

For regular models, both $\mathcal { H } _ { \theta ^ { \ast } }$ and $\Delta _ { \theta ^ { \ast } }$ coincide with the Fisher information matrix $I _ { \theta ^ { * } }$ projected onto the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ . To formalize this relationship, we introduce the following assumption on correct model specification and model regularity.

Assumption 5 (Correct model specification and model regularity). The true data distribution ${ \mathcal { P } } ^ { * }$ admits a density $p ( x \mid \theta ^ { * } )$ . Moreover, there exists a function $b : \mathcal { X } \to \mathbb { R } _ { \geq 0 }$ such that cond $\mathbb { E } \big [ \exp \big ( \big ( \frac { b ( X ) } { L } \big ) ^ { \beta _ { 1 } } \big ) \big ] \leq 1$ nd the density, the function $\{ p ( x \mid \theta ) : \theta \in \mathbb { R } ^ { D } \}$ satisfies the followingderivatives up to third $x \in \mathcal { X }$ $\log p ( x \mid \theta )$   
order are uniformly bounded in absolute value by $b ( x )$ for all $\theta \in \mathbb { B } _ { r } ( \theta ^ { * } ) \cap S _ { \Pi }$ ; (2) for any $\theta \in S _ { \Pi }$ , the Kullback–Leibler divergence satisfies $\begin{array} { r } { \mathrm { { K L } } ( p ( x \mid \theta ^ { * } ) \parallel p ( x \mid \theta ) ) \ge \frac { 1 } { L } \lVert \theta - \theta ^ { * } \rVert ^ { 2 } } \end{array}$ ; (3) the Fisher information matrix $I _ { \theta ^ { * } } = \mathbb { E } \big \lfloor ( \nabla _ { \theta } \log p ( X \mid \theta ^ { * } ) ) ( \nabla _ { \theta } \log p ( X \mid \theta ^ { * } ) ) ^ { T } \big \rfloor$ equals the negative Hessian of $\theta \mapsto \mathbb { E } [ \log p ( X \mid \theta ) ]$ at $\theta ^ { * }$ , and satisfies $\begin{array} { r } { I _ { \theta ^ { * } } \succcurlyeq \frac { 1 } { L } I _ { D } } \end{array}$ .

Corollary 1 (BvM Result under Correct Model Specification). Suppose Assumptions 1,2, and $\it 5$ hold. Consider the posterior distribution $\begin{array} { r } { \Pi ( \mathrm { d } \theta | X ^ { ( n ) } ) \propto \prod _ { i = 1 } ^ { n } p ( X _ { i } | \theta ) \Pi ( \mathrm { d } \theta ) } \end{array}$ . Let ${ \widehat { \theta } } ( X ^ { ( n ) } ) =$ $\begin{array} { r } { \arg \operatorname* { m i n } _ { \theta \in S _ { \Pi } } \left\{ n ^ { - 1 } \sum _ { i = 1 } ^ { n } - \log p ( X _ { i } | \theta ) \right\} } \end{array}$ denote the MLE over the prior support and $P _ { \theta ^ { * } }$ be the projection matrix onto $T _ { \theta ^ { * } } { \mathcal { M } }$ . Then there exists a set ${ \mathcal { A } } \subset { \mathcal { X } } ^ { n }$ with $\mathbb { P } ( X ^ { ( n ) } \in \mathcal { A } ) \geq 1 - n ^ { - 1 } \ s o$ that for any function $f : \mathbb { R } ^ { D } \to f$ satisfies the condition stated in Theorem $\mathit { 1 }$ , and any $X ^ { ( n ) } \in { \mathcal { A } }$ ,

$$
\mathrm { T V } \Big ( \int _ { \# } \Pi ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \big ( f ( \widehat { \theta } ( X ^ { ( n ) } ) ) , n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } \big ( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } \big ) ^ { \sharp } \nabla f ( \theta ^ { * } ) \big ) \Big ) \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { \sqrt { n } } ,
$$

where the matrix $( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger }$ always satisfies $( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger } \preccurlyeq I _ { \theta ^ { * } } ^ { - 1 }$ . Moreover, for any $\alpha \in ( 0 , 1 )$ , let $q _ { \alpha } ^ { f } ( X ^ { ( n ) } )$ denote the $\alpha$ -quantile of $f _ { \# } \Pi ( \cdot | X ^ { ( n ) } )$ . Then

$$
\left| \mathbb { P } \big ( q _ { \alpha / 2 } ^ { f } ( X ^ { ( n ) } ) \leq \theta ^ { * } \leq q _ { 1 - \alpha / 2 } ^ { f } ( X ^ { ( n ) } ) \big ) - ( 1 - \alpha ) \right| \leq \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { \sqrt { n } } .
$$

Corollary 1 shows that, under correct model specification, the Bayesian posterior with a manifold-supported prior can provide credible intervals for $f ( \theta )$ that are also valid from a frequentist perspective. Another key implication of this result is that using a prior supported on a lower-dimensional submanifold can lead to more efficient inference. Specifically, the asymptotic variance of the posterior for $f ( \theta )$ , given by $n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } ( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dag } \nabla f ( \theta ^ { * } )$ , is always less than or equal to the variance $n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } \nabla f ( \theta ^ { * } )$ obtained when using a conventional prior supported on the full Euclidean space. This implies that, in large samples and under correct model specification, credible intervals based on a posterior with a manifold-supported prior are at least as short as, and possibly shorter than, those from a standard Bayesian posterior, while still maintaining correct coverage.

An interesting special case arises when the Fisher information matrix $I _ { \theta ^ { * } }$ is the identity matrix. In this setting, the two variances are equal if and only if the gradient $\nabla f ( \theta ^ { * } )$ lies entirely within the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ . This indicates that, for functions $f$ that are naturally compatible with the manifold structure, the standard Bayesian posterior may achieve the same efficiency as the manifold-aware approach. However, if $\nabla f ( \theta ^ { * } )$ is not contained in $T _ { \theta ^ { * } } { \mathcal { M } }$ , then explicitly accounting for the manifold structure can lead to strictly shorter credible intervals for $f ( \theta )$ . In contrast, ignoring the manifold structure may result in overestimated uncertainty along directions orthogonal to the manifold, which do not correspond to meaningful variations of the parameter under the model.

It is important to note that Corollary 1 relies on two key assumptions: (1) the model family $\{ p ( X \mid \theta ) : \theta \in \mathbb { R } ^ { D } \}$ contains the true data-generating distribution, and (2) the true parameter $\theta ^ { * }$ lies on the manifold $\mathcal { M }$ . If either condition is violated, the posterior may yield incorrect uncertainty quantification. In the following, we present specific examples to illustrate these points. Proofs of the statements in these examples are provided in Appendix G.

Example 1: Reduced-rank multi-response regression. We consider a linear regression model with multi-dimensional response: $Y = \theta ^ { I ^ { \prime } } X + \varepsilon$ , where $Y ~ \in ~ \mathbb { R } ^ { p }$ is a $p$ -dimensional response vector, $X \in \mathbb { R } ^ { d }$ is a covariate, and $\theta = ( \beta _ { 1 } , \beta _ { 2 } , \cdot \cdot \cdot , \beta _ { p } ) \in \mathbb { R } ^ { d \times p }$ is the parameter matrix of interest. To share information across different responses, the reduced-rank multi-response regression [40] imposes a low-rank constraint $\operatorname { R a n k } ( \theta ) = r$ with $r < \operatorname* { m i n } ( d , p )$ . For clarity, we focus on the case $d = p = 2$ and $r = 1$ . Suppose the true parameter is given by $\theta ^ { * } = ( \beta _ { 1 } ^ { * } , \beta _ { 2 } ^ { * } )$ with $\beta _ { 1 } ^ { * } = ( 1 , 1 ) ^ { T }$ and $\beta _ { 2 } ^ { * } = ( 2 , 2 ) ^ { T }$ , so indeed $\theta ^ { * }$ has rank one. We generate covariates from $\mathcal { N } ( 0 _ { 2 } , I _ { 2 } )$ and the noise from $\varepsilon \sim \mathcal { N } ( 0 _ { 2 } , \Sigma )$ , where $\Sigma$ is either the identity or a non-identity full covariance matrix (specified below). Given $n$ i.i.d. samples $\{ ( X _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ , we collect the design matrix $\widetilde { X } = ( \widetilde { X } _ { 1 } , \widetilde { X } _ { 2 } , \cdot \cdot \cdot , \widetilde { X } _ { n } ) ^ { T } \in \mathbb { R } ^ { n \times 2 }$ and the response matrix $\widetilde { Y } = ( \widetilde { Y } _ { 1 } , \widetilde { Y } _ { 2 } , \cdot \cdot \cdot , \widetilde { Y } _ { n } ) ^ { T } \in \mathbb { R } ^ { n \times 2 }$ . To compare the effect of imposing the low-rank structure, we introduce two priors on the parameter space: $\Pi _ { \mathrm { M } } = \{ \theta \in \mathbb { R } ^ { 2 \times 2 } : \operatorname { R a n k } ( \theta ) = 1 , \| \theta \| _ { F } \leq 1 0 0 \}$ and $\Pi _ { \mathrm { E } } = \{ \theta \in \mathbb { R } ^ { \geq \times 2 } : \| \theta \| _ { F } \leq 1 0 0 \}$ Specifying the noise distribution as Gaussian with identity covariance (which is misspecified when $\Sigma \neq I _ { p }$ ), the posteriors take the form $\begin{array} { r } { \Pi _ { \mathrm { M } } ( \mathrm { d } \theta \ | \ ( \widetilde { X } , \widetilde { Y } ) ) \propto \Pi _ { \mathrm { M } } ( \mathrm { d } \theta ) \exp ( - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \| \widetilde { Y } _ { i } - \theta ^ { T } \widetilde { X } _ { i } \| ^ { 2 } ) } \end{array}$ and similarly for $\Pi _ { \mathrm { E } } ( \mathrm { d } \theta \mid ( \widetilde { X } , \widetilde { Y } ) )$ with prior $\Pi _ { \mathrm { E } }$ . Let $\widetilde { Y } _ { , j }$ $( j = 1 , 2 )$ denote the $j$ -th column of $\widetilde { Y }$ (corresponding to the $j$ -th response). Then the ordinary least squares (OLS) estimator is $\widehat { \theta } = ( \widehat { \beta } _ { 1 } , \widehat { \beta } _ { 2 } )$ , where $\widehat { \beta } _ { j } = ( \widetilde { X } ^ { T } \widetilde { X } ) ^ { - 1 } \widetilde { X } ^ { T } \widetilde { Y } _ { , j }$ for $j = 1 , 2$ . For illustration, we focus inference on $f ( \theta ) = \theta _ { 1 1 } - \theta _ { 2 1 }$ , where $\theta _ { i j }$ denotes the $( i , j )$ entry of $\theta$ . We consider two cases:

1. Correctly specified likelihood ( $\Sigma = I _ { 2 }$ ): the Euclidean posterior $f _ { \# } \Pi _ { \mathrm { E } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) )$ approaches $\textstyle { \mathcal { N } } ( f ( { \widehat { \theta } } ) , { \frac { 2 } { n } } )$ , and ${ \sqrt { n } } ( f ( { \widehat { \theta } } ) - f ( \theta ^ { * } ) ) \ { \xrightarrow { d } } \ N ( 0 , 2 )$ . On the other hand, the manifold posterior $f _ { \# } \Pi _ { \mathrm { M } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) )$ approaches $\begin{array} { r } { \mathcal { N } ( \widehat { s } ( \widehat { \theta } _ { 1 1 } + \widehat { \theta } _ { 2 1 } ) , \frac { 1 . 1 } { n } ) } \end{array}$ , where $\widehat { s }$ is a data-dependent scaling factor, and $\sqrt { n } ( \widehat { s } ( \widehat { \theta } _ { 1 1 } + \widehat { \theta } _ { 2 1 } ) - f ( \theta ^ { * } ) ) \stackrel { d } { \to } \mathcal { N } ( 0 , 1 . 1 )$ . Thus, both posteriors deliver valid uncertainty quantification, with the manifold posterior achieving smaller asymptotic variance.

2. Misspecified likelihood ( $\Sigma = \left( { \bf \Phi } _ { 0 . 3 } ^ { 1 } { \bf \Phi } _ { 1 } ^ { 0 . 3 } \right) )$ : the Euclidean and manifold posteriors have the same asymptotic Gaussian forms as in the correctly specified case. However, the sampling distributions of the posterior centers differ: $\sqrt { n } ( f ( \widehat { \theta } ) - f ( \theta ^ { * } ) ) \stackrel { d } { \to } \mathcal { N } ( 0 , 1 . 4 )$ and ${ \sqrt { n } } ( { \widehat { s } } ( { \widehat { \theta } } _ { 1 1 } +$ $\widehat { \theta } _ { 2 1 } ) - f ( \theta ^ { * } ) ) \stackrel { d } {  } \mathcal { N } ( 0 , 0 . 8 2 4 )$ . Hence, although the rank-one manifold assumption is satisfied, the misspecified likelihood prevents both posteriors from providing valid uncertainty quantification.

Figure 1 numerically illustrates these findings. In both the correctly specified and misspecified settings, the posterior density of $f ( \theta ) = \theta _ { 1 1 } - \theta _ { 2 1 }$ under the Euclidean Bayesian posterior $\Pi _ { \mathrm { E } } ( \cdot \mid ( \widetilde { X } , \widetilde { Y } ) )$ (red curves) exhibits heavier tails than under the manifold Bayesian posterior $\Pi _ { \mathrm { M } } ( \cdot \mid ( \bar { X } , \bar { Y } ) )$ (green curves). Moreover, the posterior mean based on $\Pi _ { \mathrm { M } }$ shows a smaller estimation error compared to that based on $\Pi _ { \mathrm { E } }$ . However, under likelihood misspecification, the (c) Coverage, interval length, point estimation error and effective sample size (ESS)

![](images/dcd3dca80934b6ef7ef0a0bbdf464527f0ae72b72ad620479937f5c88e0026fe.jpg)  
(a) Density plot: Correctly specified likelihood

![](images/6ad9f427993a960c9eec1eb8dab874a4cc67b82794d0018e5eff44b648df5b90.jpg)

(b) Density plot: Misspecified likelihood   

<table><tr><td rowspan="2"></td><td colspan="3">Correctly specifed likelihood</td><td colspan="3">1Misspecified likelihood</td></tr><tr><td>IIE</td><td>IIM</td><td>IIRP</td><td>IIE</td><td>IIM</td><td>IIRP</td></tr><tr><td>Coverage (%, target 90%)</td><td>90.3</td><td>90.1</td><td>89.4</td><td>94.3</td><td>95.6</td><td>90.6</td></tr><tr><td>Interval length (×10-1)</td><td>1.47</td><td>1.15</td><td>1.14</td><td>1.47</td><td>1.15</td><td>0.98</td></tr><tr><td>MSE (×10-3)</td><td>1.87</td><td>1.15</td><td>1.15</td><td>1.47</td><td>0.83</td><td>0.83</td></tr><tr><td>Effective sample size</td><td>683</td><td>944</td><td>948</td><td>680</td><td>942</td><td>1100</td></tr></table>

Figure 1: Results for Example 1. Figure (a) and (b) show posterior densities of $\theta _ { 1 1 } - \theta _ { 2 1 }$ from a single experiment with $n = 1 0 0 0$ , under $\Pi _ { \mathrm { E } }$ (Bayesian posterior with Euclidean prior: red), $\Pi _ { \mathrm { M } }$ (Bayesian posterior with manifold-supported prior: green) and ΠRP (Bayesian RPETEL posterior described in Section 3: blue). Posteriors are estimated from 5000 samples drawn using the (Riemannian) random-walk Metropolis algorithm described in Section 4. Figure (a) corresponds to the correctly specified likelihood and $( b )$ to the misspecified likelihood. Table (c) reports a quantitative summary based over 1000 replicated experiments for inference on $\theta _ { 1 1 } - \theta _ { 2 1 }$ , including: coverage probability for the nominal 90% credible interval, the average length of that $9 0 \%$ interval, the MSE defined as the average squared Euclidean distance between the posterior mean and the true value, and the effective sample size of the Markov chain for total of 5000 samples.

empirical coverage of credible intervals for $f ( \theta )$ under both $\Pi _ { \mathrm { M } }$ and $\mathrm { { I I } _ { E } }$ substantially exceeds the nominal level.

Example 2: Mean direction of the von Mises-Fisher distribution. The von Mises-Fisher distribution models random unit vectors on the $( d - 1 )$ -dimensional unit sphere $\mathbb { S } _ { 1 } ^ { d - 1 }$ . Its density takes the form $f ( x \mid \theta ) = C _ { d } ( \| \theta \| ) \exp ( \theta ^ { T } x )$ , for $x \in \mathbb { S } _ { 1 } ^ { d - 1 }$ and $\theta \in \mathbb { R } ^ { d }$ , where the magnitude $\| \theta \|$ controls concentration, the direction of $\theta$ determines the mean direction of the distribution, and $C _ { d } ( | | \theta | | )$ is the normalization constant depending only on $\| \theta \|$ and $d$ . Consider the case $d = 3$ with true parameter √ √ √ $\theta ^ { * } = \kappa ^ { * } ( 1 / \sqrt { 3 } , 1 / \sqrt { 3 } , 1 / \sqrt { 3 } ) ^ { T }$ , so that the true mean direction is $\mu ^ { * } = ( 1 / \sqrt { 3 } , 1 / \sqrt { 3 } , 1 / \sqrt { 3 } ) ^ { T }$ . Suppose we observe $n$ i.i.d. samples $X ^ { ( n ) } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ from $f ( x \mid \theta ^ { * } )$ . To infer the mean direction, we take the parameter space $\mathcal { M }$ to be the unit sphere $\mathbb { S } _ { 1 } ^ { d - 1 }$ and place a uniform prior $\Pi$ on $\mathcal { M }$ . This yields the posterior distribution $\begin{array} { r } { \Pi ( \mathrm { d } \theta \ \vert \ X ^ { ( n ) } ) \propto \Pi ( \mathrm { d } \theta ) \exp \left( \sum _ { i = 1 } ^ { n } \theta ^ { T } X _ { i } + n \log C _ { d } ( \Vert \theta \Vert ) \right) \propto \Pi ( \mathrm { d } \theta ) \exp ( \sum _ { i = 1 } ^ { n } \theta ^ { T } X _ { i } ) } \end{array}$ . The likelihood function is correctly specified, but the manifold assumption $\theta ^ { * } \in \mathcal { M }$ holds only if $\kappa ^ { * } = 1$ . For illustration, consider inference on the first coordinate $f ( \theta ) = \theta _ { 1 }$ . The posterior distribution $f _ { \# } \Pi ( \cdot \ | \ X ^ { ( n ) } )$ converges to $\begin{array} { r } { \mathcal { N } ( f ( \overline { { X } } / \| \overline { { X } } \| ) , n ^ { - 1 } \frac { 2 } { 3 A ( \kappa ^ { * } ) } ) } \end{array}$ where $A ( \kappa ^ { * } ) = \coth ( \kappa ^ { * } ) - 1 / \kappa ^ { * }$ and $\begin{array} { r } { X = n ^ { - 1 } \sum _ { i = 1 } ^ { n } X _ { i } } \end{array}$ . On the other hand, the sampling distribution of the posterior center satisfies $\sqrt { n } ( f ( \overline { { X } } / \| \overline { { X } } \| ) - f ( \mu ^ { * } ) ) \overset { d } { \to } \mathcal N ( 0 , \frac { 2 } { 3 \kappa ^ { * } A ( \kappa ^ { * } ) } )$ . Thus, unless $\kappa ^ { * } = 1$ so that $\theta ^ { * }$ lies exactly on the manifold $\mathcal { M }$ , the posterior variance fails to match the true sampling variability, and the posterior cannot provide valid uncertainty quantification.

# 3 Robust Bayesian Inference on Manifold

We begin with a likelihood-based formulation in Euclidean space, defining the target parameter as $\begin{array} { r } { \theta _ { \mathrm { E } } ^ { * } = \arg \operatorname* { m i n } _ { \theta \in \mathbb { R } ^ { d } } \mathbb { E } [ - \log p ( X \mid \theta ) ] } \end{array}$ . In practice, however, we often possess additional structural information about the parameter $\theta _ { \mathrm { E } } ^ { * }$ —for example, low-rank structure, unit norm, or symmetry—suggesting that $\theta ^ { * }$ lies (approximately) on a low-dimensional Riemannian submanifold $\mathcal { M } \subset \mathbb { R } ^ { d }$ . Such information can be encoded through a prior $\Pi$ supported on $\mathcal { M }$ . As discussed in Section 2, however, the resulting posterior’s ability to deliver correct uncertainty quantification depends on two strong conditions: the likelihood family must be correctly specified to include the true data-generating distribution, and the Euclidean minimizer $\theta _ { \mathrm { E } } ^ { \ast }$ must lie exactly on $\mathcal { M }$ . Both requirements are often unrealistic. In complex models, specifying a correct likelihood is difficult—for instance, in regression problems, we may primarily care about the regression coefficients, while the noise distribution is difficult to fully characterize and not of primary interest. Moreover, even when $\theta _ { \mathrm { E } } ^ { * }$ does not lie exactly on $\mathcal { M }$ , casting the problem as a manifold-constrained optimization can yield substantial computational benefits. In Section 4, we show that a manifold-adapted random walk Metropolis algorithm can be used to sample from a manifold-constrained posterior with mixing time nearly linear in the intrinsic dimension $d$ of $\mathcal { M }$ , rather than in the ambient dimension $D$ . This motivates a deliberate trade-off between small statistical bias and significant computational efficiency gains. For example, in reduced-rank multi-response regression, the true coefficient matrix may not be exactly rank $r$ but can be well approximated by a rank- $r$ matrix, with residual components attributable to weak signals. In such settings, classical Bayesian approaches that rely on fully specified likelihoods and exact manifold adherence may fail to provide valid uncertainty quantification. This motivates the development of robust, manifold-aware pseudo-Bayesian methods that avoid full likelihood specification while retaining valid uncertainty quantification.

As in Section 2, to avoid full likelihood specification, we adopt a loss-function-based framework by introducing a loss function $\ell ( X , \theta )$ that quantifies how well a parameter explains the data. Rather than assuming that the Euclidean minimizer $\theta _ { \mathrm { E } } ^ { * }$ lies exactly on $\mathcal { M }$ , we define the target parameter directly as the constrained population risk minimizer on $\mathcal { M }$ :

$$
\begin{array} { r } { \theta ^ { * } = \arg \operatorname* { m i n } _ { \theta \in \mathcal { M } } \mathcal { R } ( \theta ) , \quad \mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ] . } \end{array}
$$

However, as shown in Section 2, treating the scaled empirical risk $\textstyle \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta )$ as a surrogate log-likelihood can yield consistent point estimates but generally fails to provide valid uncertainty quantification. To address this limitation, we leverage the first-order optimality condition of $\theta ^ { * }$ on $\mathcal { M }$ (see Appendix A for details):

grad $\mathcal { R } ( \theta ^ { \ast } ) = 0 _ { D }$ , where grad $\mathcal { R } ( \theta ^ { \ast } )$ denotes the Riemannian gradient of $\mathcal { R } ( \cdot )$ at $\theta ^ { * }$ on $\mathcal { M }$ which provides identifying information about $\theta ^ { * }$ without requiring a full likelihood specification. In particular, if for any $X$ and $\theta$ the Riemannian gradient $\operatorname { g r a d } _ { \theta } \ell ( X , \theta )$ of the loss function $\theta \mapsto \ell ( X , \theta )$ exists, then the target parameter can be equivalently characterized by the moment condition $\mathbb { E } [ \mathrm { g r a d } _ { \theta } \ell ( X , \theta ^ { * } ) ] = \mathrm { g r a d } \mathcal { R } ( \theta ^ { * } ) = 0 _ { D }$ . We then incorporate the information from these moment conditions to construct a Bayesian pseudo-posterior.

One choice is to use the exponentially tilted empirical likelihood (ETEL) approach [63, 25, 67]. To do this, we define the Riemannian exponentially tilted empirical likelihood (RETEL) function $\begin{array} { r } { L ( X ^ { ( n ) } ; \theta ) = \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } \end{array}$ , where $( p _ { 1 } ( \theta ) , p _ { 2 } ( \theta ) , \cdot \cdot \cdot , p _ { n } ( \theta ) )$ is the solution of

$$
\begin{array} { c } { { \displaystyle \operatorname* { m a x } _ { ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ) } \sum _ { i = 1 } ^ { n } \big [ - w _ { i } \log ( n w _ { i } ) \big ] } } \\ { { \mathrm { s u b j e c t ~ t o } \quad \displaystyle \sum _ { i = 1 } ^ { n } w _ { i } = 1 , \quad \sum _ { i = 1 } ^ { n } w _ { i } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) = 0 _ { D } , \quad w _ { 1 } , w _ { 2 } , \ldots , w _ { n } \geq 0 . } } \end{array}
$$

We can view $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ as the probabilities minimizing the “backward” KL divergence between the empirical distribution $( n ^ { - 1 } , n ^ { - 1 } , \cdots , n ^ { - 1 } )$ and the multinomial distribution $( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } )$ , subject to the constraint that a weighted-sample version of the first-order optimality condition on the Riemannian submanifold is satisfied. It is worth noting that the ETEL function is not the only possible choice for the pseudo-likelihood; for instance, we can consider the Riemannian empirical likelihood (REL) function, which minimizes the “forward” KL divergence between the empirical distribution and the multinomial distribution $( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } )$ assigned to data points $X ^ { ( n ) }$ , subject to the same constraint as the RETEL function. Another option is to utilize the generalized method of moments (GMM) [23, 34, 77], where the pseudo-likelihood is given by the objective function optimized in GMM using the moment condition (1), i.e., −  √12n $\begin{array} { r l } & { - \big ( \frac { 1 } { \sqrt { 2 n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \big ) ^ { T } \big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \big ) ^ { - 1 } \big ( \frac { 1 } { \sqrt { 2 n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \big ) } \end{array}$ with $g ( X , \theta ) = \operatorname { g r a d } _ { \theta } \ell ( X , \theta )$ . However, all these pseudo-likelihoods derived from the moment condition (1) share a common issue: the first-order optimality condition grad $\mathcal { R } ( \theta ) = 0 _ { D }$ may have multiple solutions, and directly incorporating them as pseudo-likelihoods in a posterior distribution may result in inconsistent estimation.

To address this issue of inconsistent estimation and enforce the concentration of the posterior around the global risk minimizer $\theta ^ { * }$ , we adopt the approach proposed in [67] to exponentially penalize the posterior using the empirical risk function $\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) } \end{array}$ . Given a prior distribution $\Pi$ defined on $\mathcal { M }$ , we define the following Bayesian penalized Riemannian exponentially tilted empirical likelihood (RPETEL) posterior

$$
\Pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } ) = \frac { \exp ( \sum _ { i = 1 } ^ { n } \log p _ { i } ( \theta ) - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \Pi ( \mathrm { d } \theta ) } { \int _ { \mathcal { M } } \exp ( \sum _ { i = 1 } ^ { n } \log p _ { i } ( \theta ) - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \Pi ( \mathrm { d } \theta ) } ,
$$

where $\alpha _ { n } \geq 0$ is an $n$ -dependent regularization parameter and $( p _ { 1 } ( \theta ) , p _ { 2 } ( \theta ) , \cdot \cdot \cdot , p _ { n } ( \theta ) )$ is the solution to (2). Notice that the RETEL function in (3) may be replaced with other moment condition-based pseudo-likelihoods, such as the REL function or the GMM objective discussed earlier.

An important design choice in our construction is the use of the Riemannian gradient rather than the full Euclidean gradient. Indeed, if $\theta ^ { \ast } = \theta _ { \mathrm { E } } ^ { \ast }$ , one could instead work with the moment condition $\nabla \mathcal { R } ( \theta ) = \mathbb { E } [ \nabla _ { \theta } \ell ( X , \theta ) ] = 0 _ { D }$ , in which case our method reduces to the Bayesian PETEL posterior of [67] when combined with a manifold-supported prior. However, this approach has several drawbacks. First, it critically relies on the assumption that the global Euclidean minimizer lies exactly on the manifold $\mathcal { M }$ . If this is not the case, the moment condition becomes misspecified. As shown in [25], such misspecification can lead to invalid uncertainty quantification, and the resulting posterior may even fail to concentrate around the risk minimizer $\theta ^ { * }$ on the manifold $\mathcal { M }$ , even when the Euclidean minimizer $\theta _ { \mathrm { E } } ^ { * }$ is very close to the manifold (see Figure 2 for an illustration). Second, in settings where the parameter is intrinsically defined on a manifold, such as Fréchet mean estimation on the sphere, the Euclidean gradient is not a meaningful object, and only the Riemannian gradient correctly encodes the first-order optimality condition.

The Bayesian RPETEL approach also applies when the loss function $\ell ( x , \theta )$ is not everywhere differentiable in $\theta$ . In such cases, the Riemannian gradient grad ${ } _ { \theta } \ell ( X , \theta )$ can be replaced by any function $g ( X , \theta )$ that satisfies Assumption 4. The moment condition underlying $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ is then specified as $\mathbb { E } [ g ( X , \theta ) ] = 0 _ { D }$ . Under this generalized formulation, we establish a Bernstein–von Mises type theorem for the Bayesian RPETEL posterior. Throughout, we follow the notation of Theorem 1, including the Riemannian Hessian matrix $\mathcal { H } _ { \theta ^ { \ast } }$ , the Gram matrix $\Delta _ { \theta ^ { * } }$ , the empirical risk minimizer ${ \widehat { \theta } } ( X ^ { ( n ) } )$ , and the inverse of the projection map $\phi _ { \theta ^ { * } } : V _ { \theta ^ { * } } \to U _ { \theta ^ { * } }$ . We also use ${ \widehat { \theta } } _ { p } ( X ^ { ( n ) } )$ to denote the posterior mean of $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ projected onto $\mathcal { M }$ .

Theorem 2 (Manifold BvM theorem for Bayesian RPETEL). Suppose Assumptions 1-4 hold. Then there exists a set $A \subset \mathcal { X } ^ { n }$ with $\mathbb { P } ( X ^ { ( n ) } \in \mathcal { A } ) \geq 1 - n ^ { - 1 }$ , and positive constants $c _ { 1 } , c _ { 2 }$ such that when $c _ { 1 } \log n \leq \alpha _ { n } \leq c _ { 2 } { \sqrt { n } }$ , the followings hold

1. There exists a constant $C > 0$ such that, for every dataset $X ^ { ( n ) } \in { \mathcal { A } }$ , we have

$$
\begin{array} { r l } & { \mathrm { T V } \Big ( \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) , \phi _ { \theta ^ { * } \# } \big [ \mathcal { N } \big ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \widehat { \theta } ( X ^ { ( n ) } ) - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) | _ { V _ { \theta ^ { * } } } \big ] \Big ) } \\ & { \quad \quad \leq C \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } , } \end{array}
$$

and when $n$ is sufficiently large, $\widehat { \theta } _ { p } ( X ^ { ( n ) } )$ is uniquely defined and satisfies $\| \widehat { \theta } _ { p } ( X ^ { ( n ) } ) -$ $\begin{array} { r } { \widehat { \theta } ( X ^ { ( n ) } ) \| \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } + 1 } { 2 } } } . } \end{array}$

2. There exists a constant $C > 0$ such that for any function $f$ satisfies the conditions specified in Theorem $\mathit { 1 }$ and for every dataset $X ^ { ( n ) } \in { \mathcal { A } }$ , we have

$$
\operatorname { T V } \Big ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \big ( f ( \widehat { \theta } ( X ^ { ( n ) } ) ) , n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \nabla f ( \theta ^ { * } ) \big ) \Big ) \leq C \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

A key observation is that the variance in the normal approximation of the posterior of $f ( \theta )$ coincides with the asymptotic variance of the sampling distribution of $f ( \widehat { \theta } ( X ^ { ( n ) } ) )$ established in Theorem 1. Consequently, credible intervals for $f ( \theta )$ obtained from the quantiles of posterior samples from $f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ achieve correct frequentist coverage without requiring the correct model specification assumption (i.e., Assumption 5). Moreover, when we project the posterior onto the tangent space, it is approximately normal with a “sandwich” covariance matrix. This makes it natural to construct credible regions for parameters constrained to the manifold: we form a Wald-type region in the tangent space and then map it back to the manifold. Since the θ estimator θbp = θbp(X(n)). Specifically, define the local projection ψθbp(θ) = ProjTθbpM are unknown, we instead work around the point When $\widehat { \theta _ { p } }$ is sufficiently close to $\theta ^ { * }$ , $\psi _ { \widehat { \theta } _ { p } }$ is injective on $\mathbb { B } _ { r _ { 1 } } ( \widehat { \theta } _ { p } ) \cap \mathcal { M }$ for some small enough radius $r _ { 1 } ~ > ~ 0$ and admits an inverse map $\phi _ { \widehat { \theta } _ { p } }$ (c.f., Lemma 2 in Appendix D). Let $\Sigma _ { p } =$ $\operatorname { C o v } _ { \theta \sim \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) } \big ( \psi _ { \widehat { \theta } _ { p } } ( \theta ) \big )$ . For a chosen level of significance $\alpha$ , let $q _ { \alpha }$ be the $\alpha$ -upper quantile of $\psi _ { \widehat { \theta } _ { p } } ( \theta ) ^ { T } \Sigma _ { p } ^ { \dagger } \psi _ { \widehat { \theta } _ { p } } ( \theta ) = ( \theta - \widehat { \theta } _ { p } ) ^ { T } \Sigma _ { p } ^ { \dagger } ( \theta - \widehat { \theta } _ { p } )$ under $\theta \sim \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ . The Wald-type credible region with level $\alpha$ is then

$$
\mathcal { E } _ { n } = \{ \theta \in \mathcal { M } \cap B _ { r _ { 1 } } ( \widehat { \theta } _ { p } ) : ( \theta - \widehat { \theta } _ { p } ) ^ { T } \Sigma _ { p } ^ { \dagger } ( \theta - \widehat { \theta } _ { p } ) \leq q _ { 1 - \alpha } \} .
$$

The next corollary shows that $\mathcal { E } _ { n }$ attains valid frequentist coverage.

Corollary 2 (Validity of Wald-type Credible Region). Under the conditions in Theorem $\mathcal { Z }$ , there exists a small enough positive constant $r _ { 1 }$ so that for any level $\alpha \in ( 0 , 1 )$ , there exists a constant $C$ satisfying

$$
\left| \mathbb { P } ( \theta ^ { * } \in \mathcal { E } _ { n } ) - ( 1 - \alpha ) \right| \le C \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

Next, we return to the likelihood-based setting. A key implication of Theorem 2 is that, under correct model specification, the Bayesian RPETEL posterior shares the same asymptotic distribution as the classical Bayesian posterior supported on the manifold. This result is formalized below.

![](images/4cfe731b6a367401d7237660503ad9c2a2a09413531014285945add23a65d1e4.jpg)

Figure 2: The figures compare Bayesian RPETEL and Bayesian PETEL on a toy example with loss function $\begin{array} { r } { \ell ( x , \theta ) = \sum _ { j = 1 } ^ { 2 } \exp ( - ( \theta _ { j } - 0 . 5 ) ^ { 2 } ) \cdot x _ { j } - \exp ( - \theta _ { j } ^ { 2 } ) } \end{array}$ for $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } ) ^ { \prime }$ and $\theta = ( \theta _ { 1 } , \theta _ { 2 } ) ^ { T }$ . The parameter is constrained to the line-shaped manifold $\mathcal { M } = \{ ( \theta _ { 1 } , \theta _ { 2 } ) \in \mathbb { R } ^ { 2 } : \theta _ { 2 } = 0 . 9 \theta _ { 1 } + 0 . 1 \}$ . We draw $n = 1 0 0 0$ i.i.d. samples from $\mathcal { N } ( 0 _ { 2 } , I _ { 2 } )$ and use a uniform prior on $\mathcal { M } \cap [ - 2 , 2 ] ^ { 2 }$ . The Bayesian RPETEL posterior (BRPETEL) builds the ETEL function from the Riemannian gradient on $\mathcal { M }$ , while the Bayesian PETEL posterior (BPETEL) uses the Euclidean gradient in $\mathbb { R } ^ { 2 }$ to construct the ETEL. Figure (a) shows the population risk $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ for $\theta \in [ - 2 , 2 ] ^ { 2 }$ . The blue dot marks the Euclidean risk minimizer on $[ - 2 , 2 ] ^ { 2 }$ , which lies very close to but not exactly on $\mathcal { M }$ . The green and orange dots indicate the posterior modes of BRPETEL and BPETEL, respectively, when $\alpha _ { n } = \log n$ ; the BRPETEL mode sits close to the true risk minimizer, whereas the BPETEL mode is noticeably farther away. Figure (b) plots the marginal densities of $\theta _ { 1 }$ for both posteriors under $\alpha _ { n } = \log n$ and $\alpha _ { n } = 0$ . The gray line marks $\theta _ { 1 } ^ { * }$ , the $\theta _ { 1 }$ -coordinate of the risk minimizer on $\mathcal { M }$ . When $\alpha _ { n } = 0$ , both posteriors are multimodal because the risk function is nonconvex. In particular, $\operatorname { g r a d } _ { \theta } { \mathcal { R } } ( \theta ) = 0$ has two solutions on $\mathcal { M }$ : one near $( - 0 . 5 4 5 , 0 . 3 9 1 )$ corresponding to the risk minimizer on $\mathcal { M }$ , and another near (0.975, 0.977) corresponding to a local risk maximizer. With $\alpha _ { n } = 0$ , the BRPETEL exhibits two comparable modes around these points, while the BPETEL with $\alpha _ { n } = 0$ shows a poorly interpretable shape and allocates little mass near $\theta _ { 1 } ^ { * }$ . When $\alpha _ { n } = \log n$ , the BRPETEL concentrates around $\theta _ { 1 } ^ { * }$ , whereas the BPETEL still fails to place meaningful mass there.

Corollary 3 (Bayesian RPETEL under Correct Model Specification). Suppose Assumptions 1,2, and $\it 5$ hold, let $\ell ( X , \theta ) = \log p ( X | \theta )$ , and take $g ( X , \theta ) = \operatorname { g r a d } _ { \theta } \ell ( X , \theta )$ . Then there exists a set $A \subset \mathcal { X } ^ { n }$ with $\mathbb { P } ( X ^ { ( n ) } \in \mathcal { A } ) \geq 1 - n ^ { - 1 }$ , and positive constants $c _ { 1 } , c _ { 2 }$ such that if $c _ { 1 } \log n \leq \alpha _ { n } \leq$ $c _ { 2 } \sqrt { n }$ , then for any function $f : \mathbb { R } ^ { D }  f$ satisfies the condition stated in Theorem $\mathit { 1 }$ , and any $X ^ { ( n ) } \in { \mathcal { A } }$ , we have

$$
\mathrm { T V } \Big ( \int _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \big ( f ( \widehat { \theta } ( X ^ { ( n ) } ) ) , n ^ { - 1 } \nabla f ( \theta ^ { * } ) ^ { T } ( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger } \nabla f ( \theta ^ { * } ) \big ) \Big ) \leq C \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { \sqrt { n } } .
$$

Under the correct model specification in Corollary 3, where $\theta ^ { \ast } = \theta _ { \mathrm { E } } ^ { \ast }$ also satisfies $\mathbb { E } [ \nabla \mathcal { R } ( \theta ^ { * } ) ] =$ $0 _ { D }$ , the moment condition based on the Riemannian gradient extracts the most “relevant” information contained in the full Euclidean gradient. This extraction does not reduce efficiency; rather, it transforms an overidentified problem—where the ambient gradient yields $D$ moment conditions with $D > d$ —into an identified one, where the intrinsic dimension $d$ of the manifold matches the effective number of moment conditions. Indeed, with an orthonormal basis $W _ { \theta } \in \mathbb { R } ^ { D \times d }$ of the tangent space $T _ { \theta } \mathcal { M }$ , the condition $\mathbb { E } [ \mathrm { g r a d } _ { \theta } \ell ( X , \theta ) ] = 0 _ { D }$ is equivalent to $\mathbb { E } [ W _ { \theta } ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X , \theta ) ] = 0 _ { d }$ . This identifiability provides additional benefits under model misspecification, where $\theta _ { \mathrm { E } } ^ { * } \notin { \mathcal { M } }$ , preventing spurious overidentification and ensuring that the posterior remains concentrated near $\theta ^ { * }$ . Overall, these results highlight a threefold robustness of our method: (1) the posterior is automatically calibrated to deliver valid uncertainty quantification without requiring a correctly specified likelihood; (2) even if the unconstrained (Euclidean) risk minimizer lies off the manifold or does not exist, the posterior center remains meaningful—it closely matches the risk minimizer over the manifold, and the posterior covariance aligns with the frequentist sampling covariance of this center; and (3) when both the likelihood model is correctly specified and the manifold assumption holds, the posterior is asymptotically equivalent to the standard Bayesian posterior with the same prior. Hence, there is no loss of efficiency in well-specified models. To conclude this section, we revisit Examples 1 and 2 from Section 2 to illustrate our method.

Example 1 (revisited): Reduced-rank multi-response regression. Take the prior $\Pi = \Pi _ { \mathrm { M } }$ and recall $f ( \theta ) = \theta _ { 1 1 } - \theta _ { 1 2 }$ . When the likelihood is correctly specified $\Sigma = I _ { 2 }$ ), $f _ { \# } \Pi _ { \mathrm { R P } } \big ( \cdot | ( \widetilde { X } , \widetilde { Y } ) \big )$ approaches to $\begin{array} { r } { \mathcal { N } ( \widehat { s } ( \widehat { \theta } _ { 1 1 } + \widehat { \theta } _ { 2 1 } ) , \frac { 1 . 1 } { n } ) } \end{array}$ , which matches the Gaussian limit of the standard Bayesian posterior $\Pi _ { \mathrm { M } } ( \cdot | X ^ { ( n ) } )$ with prior $\Pi _ { \mathrm { M } }$ . When the likelihood is misspecified $\Sigma ~ = ~ \left( \begin{array} { c } { { 1 } } \\ { { 0 . 3 } } \end{array} 0 . 3 \right) )$ $f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) )$ approaches to $\begin{array} { r } { \mathcal { N } ( \widehat { s } ( \widehat { \theta } _ { 1 1 } + \widehat { \theta } _ { 2 1 } ) , \frac { 0 . 8 2 4 } { n } ) } \end{array}$ , and recall that ${ \sqrt { n } } ( { \widehat { s } } ( { \widehat { \theta } } _ { 1 1 } + { \widehat { \theta } } _ { 2 1 } ) - f ( \theta ^ { * } ) ) \ { \xrightarrow { d } }$ $\mathcal { N } ( 0 , 0 . 8 2 4 )$ b b. Thus, even with likelihood misspecification, the Bayesian RPETEL posterior still provides valid uncertainty quantification.

Example 2 (revisited): Mean direction of the von Mises-Fisher distribution. Place a uniform prior $\Pi$ on $\mathcal { M } = \mathbb { S } _ { 1 } ^ { 2 }$ and consider $f ( \theta ) = \theta _ { 1 }$ . The (pushforward) posterior $f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ converges to $\begin{array} { r l } {  { \mathcal { N } ( f ( \overline { { X } } / \| \overline { { X } } \| ) , n ^ { - 1 } \frac { 2 } { 3 \kappa ^ { * } A ( \kappa ^ { * } ) } ) } \qquad } & { { } } \end{array}$ , and recall that $\begin{array} { r } { \sqrt { n } ( f ( \overline { { X } } / \| \overline { { X } } \| ) - f ( \mu ^ { * } ) ) \overset { d } { \to } \mathcal N ( 0 , \frac { 2 } { 3 \kappa ^ { * } A ( \kappa ^ { * } ) } ) } \end{array}$ Hence, for any $\kappa ^ { * }$ , the posterior provides valid uncertainty quantification. Moreover, when $\kappa ^ { * } = 1$ so that $\theta ^ { * } \in \mathcal { M }$ , the Gaussian limits of $f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ and $f _ { \# } \Pi ( \cdot | X ^ { ( n ) } )$ coincide, where $\Pi ( \cdot | X ^ { ( n ) } )$ denotes the classical Bayesian posterior with prior $\Pi$ .

# 4 Posterior Sampling on Riemannian Submanifold

Given that the (pseudo-)posterior has an explicit form up to a normalization constant, we can employ a Markov chain Monte Carlo (MCMC) algorithm for sampling. MCMC transforms the integration problem of computing the normalization constant into a sampling task, thereby circumventing the need to evaluate a high-dimensional integral directly. The main difficulty in implementing MCMC algorithms arises from the fact that the posterior is defined on the manifold $\mathcal { M }$ rather than in a Euclidean space. While several MCMC methods have been developed for sampling from distributions on specific manifolds, such as the sphere [14, 73] and the Stiefel manifold [41, 36], these techniques are highly specialized to the particular manifold structures they target. In addition, Hamiltonian Monte Carlo (HMC) algorithms have been adapted for more general manifold sampling. For instance, [17] introduced a constrained version of HMC for sampling from solution manifolds $\mathcal { M } _ { \mathbf { q } } = \{ \theta \in \mathbb { R } ^ { D } : \mathbf { q } ( \theta ) = 0 \}$ . However, their method is closely tied to the constraint functions $\mathbf { q } ( \theta ) = 0$ and does not easily extend beyond such manifolds. Similarly, [18] explored HMC on general Riemannian submanifolds, but this approach requires the computationally intensive task of evaluating geodesic flows on the submanifold. [5] derived error bounds for sampling and estimation using an intrinsically defined Langevin diffusion on a compact Riemannian submanifolds. However, both Langevin and HMC-based methods require computing the Riemannian gradient of the log-density, which becomes difficult when the density is not smooth. Beyond HMC and Langevin methods, [78] proposed a simpler algorithm for sampling on solution manifolds, where a random vector in the tangent space of the current state is proposed and then projected back onto the manifold using the constraint functions $\mathbf { q } ( \cdot )$ before applying an acceptance–rejection step. Inspired by this idea, we develop a Riemannian Random-Walk Metropolis (RRWM) algorithm that generalizes [78] for sampling from posteriors supported on general Riemannian submanifolds. In this section, we first introduce the RRWM algorithm and then provide a mixing time analysis for sampling from the Bayesian RPETEL posterior.

# 4.1 Riemannian random-walk Metropolis (RRWM) algorithm

The key idea of the RRWM algorithm is that, starting from the current state $\theta \in \mathcal { M }$ , we generate a proposal increment $v$ by first drawing an ambient vector from $\mathcal { N } ( 0 _ { D } , \Sigma )$ and then projecting it onto the tangent space $T _ { \theta } \mathcal { M }$ . We then map $\boldsymbol { v }$ back to the manifold using a map $\widetilde { \phi } _ { \theta } : T _ { \theta } \mathcal { M }  \mathcal { M }$ , setting the candidate $y = \widetilde { \phi } _ { \theta } ( v )$ . The candidate is then accepted or rejected using the standard Metropolis–Hastings acceptance probability. A key design issue is that both the covariance matrix $\Sigma$ and the mapping $\widetilde { \phi } _ { \theta }$ influence how far the proposal $y$ tends to move from the current state $\theta$ . If $\widetilde { \phi } _ { \theta }$ rescales small tangent steps differently across locations, $\Sigma$ no longer controls the proposal step size consistently. For example, suppose $T _ { \theta _ { 1 } } { \mathcal { M } } = T _ { \theta _ { 2 } } { \mathcal { M } }$ , while $\widetilde { \phi } _ { \theta _ { 1 } } ( v ) \approx v + \theta _ { 1 }$ and $\widetilde { \phi } _ { \theta _ { 2 } } ( v ) \approx 2 v + \theta _ { 2 }$ for $\lVert \boldsymbol { v } \rVert \approx 0$ . Then, the same tangent increment $\boldsymbol { v }$ produces a move of size $\lVert v \rVert$ near $\theta _ { 1 }$ but $2 \Vert v \Vert$ near $\theta _ { 2 }$ , leading to location-dependent proposal magnitudes. To eliminate this confounding effect, we require $\bar { \phi } _ { \theta }$ to be a retraction (see Appendix A for a detailed definition), which guarantees first-order equivalence between $\tilde { \phi } _ { \theta } ( v )$ and $\theta + v$ when $\lVert v \rVert$ is small. This ensures that acceptance-rate tuning via $\Sigma$ is both stable and interpretable. A retraction can be constructed from any local parameterization $\xi _ { \theta } ( \cdot )$ as

$$
\widetilde { \phi } _ { \boldsymbol { \theta } } ( \boldsymbol { v } ) = \xi _ { \boldsymbol { \theta } } \Big ( \big ( W _ { \boldsymbol { \theta } } ^ { T } J _ { \xi _ { \boldsymbol { \theta } } } ( \xi _ { \boldsymbol { \theta } } ^ { - 1 } ( \boldsymbol { \theta } ) ) \big ) ^ { - 1 } W _ { \boldsymbol { \theta } } ^ { T } \boldsymbol { v } + \xi _ { \boldsymbol { \theta } } ^ { - 1 } ( \boldsymbol { \theta } ) \Big ) ,
$$

where $W _ { \theta }$ is a $D \times d$ matrix whose columns form an orthonormal basis for $T _ { \theta } \mathcal { M }$ , and $\xi _ { \theta } ^ { - 1 }$ is the inverse of $\xi _ { \theta }$ .

To describe the RRWM algorithm more precisely, we assume that for any $\theta \in \mathcal { M }$ , there exists a retraction $\widetilde { \phi } _ { \theta }$ that is injective on an open neighborhood $\widetilde { V _ { \theta } }$ of $0 _ { D }$ in $T _ { \theta } \mathcal { M }$ . Let $\widetilde { U } _ { \theta } = \widetilde { \phi } _ { \theta } ( \widetilde { V } _ { \theta } )$ and define the local inverse $\tilde { \psi } _ { \theta } : \widetilde { U } _ { \theta } \to \widetilde { V } _ { \theta }$ . The set $\widetilde { V _ { \theta } }$ serves as a “safety” region: proposals $y = \widetilde { \phi } _ { \theta } ( v )$ with $v \not \in \widetilde { V } _ { \theta }$ are rejected to prevent the algorithm from stepping outside the domain where $( \widetilde { \psi } _ { \boldsymbol { \theta } } , \widetilde { \phi } _ { \boldsymbol { \theta } } )$ are mutual inverses. The retraction map $\widetilde { \phi } _ { \theta }$ is used to define proposal states in RRWM, while its inverse $\widetilde { \psi } _ { \boldsymbol { \theta } }$ plays a crucial role in computing the acceptance probability of those proposals. Given a target density $\mu ^ { * } ( \theta )$ with respect to the volume measure $\mu _ { \mathcal { M } }$ on the submanifold $\mathcal { M }$ , the RRWM algorithm also involves a step size $\widetilde h > 0$ , a symmetric positive definite preconditioning (proposal) covariance matrix $\boldsymbol { \widetilde { I } } \in \mathbb { R } ^ { D \times D }$ e, and an initial distribution $\mu _ { 0 }$ on $\mathcal { M }$ . The RRWM algorithm then generates the sequence $\{ \theta ^ { k } \} _ { k \geq 0 }$ iteratively as follows: for k = 0, 1, 2, . . .,

1. (Initialization) If $k = 0$ , sample $\theta ^ { 0 }$ from initial distribution $\mu _ { 0 }$

2. (Proposal) If $k \geq 1$ ,

(a) (Generate random vector in tangent space) sample $\widetilde { v }$ from $\mathcal { N } ( 0 , 2 \widetilde { h } \widetilde { I } )$ and let $v =$ $\mathrm { P r o j } _ { T _ { \theta ^ { k - 1 } } \mathcal { M } } ( \widetilde { v } )$ ;   
(b) (Reject proposal if $v$ escape from $\widetilde { V } _ { \theta ^ { k - 1 } }$ ) if $v \not \in \widetilde { V } _ { \theta ^ { k - 1 } }$ , then set $\theta ^ { k } = \theta ^ { k - 1 }$ and terminate the current iteration;   
(c) (Map back to manifold) set $y = \widetilde { \phi } _ { \theta ^ { k - 1 } } ( v )$ ;

# 3. (Metropolis-Hasting rejection/correction)

(a) (Reject proposal if $\theta ^ { k - 1 }$ escapes from $\widetilde { U } _ { y }$ ) if $\theta ^ { k - 1 } \notin \widetilde { U } _ { y }$ , then set $\theta ^ { k } = \theta ^ { k - 1 }$ and terminate the current iteration; (b) (Set acceptance probability) let $v ^ { \prime } = \widetilde { \psi } _ { y } ( \theta ^ { k - 1 } )$ , set acceptance probability $A ( \theta ^ { k - 1 } , y ) =$

$1 \wedge \alpha ( \theta ^ { k - 1 } , y )$ with acceptance ratio statistic:

$$
\begin{array} { r } { \alpha ( \theta ^ { k - 1 } , y ) = \frac { \mu ^ { * } ( y ) \cdot \exp \big ( - v ^ { \prime T } ( P _ { y } \widetilde { I } P _ { y } ) ^ { \dagger } v ^ { \prime } / ( 4 \widetilde { h } ) \big ) } { \mu ^ { * } ( \theta ^ { k - 1 } ) \cdot \exp \big ( - v ^ { T } ( P _ { \theta ^ { k - 1 } } \widetilde { I } P _ { \theta ^ { k - 1 } } ) ^ { \dagger } v / ( 4 \widetilde { h } ) ) \big ) } } \\ { \cdot \frac { \big ( \big | ( \mathcal { D } \widetilde { \phi } _ { y } ( v ^ { \prime } ) [ P _ { y } ] ) ^ { T } \mathcal { D } \widetilde { \phi } _ { y } ( v ^ { \prime } ) [ P _ { y } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } { \big ( \big | ( \mathcal { D } \widetilde { \phi } _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] ) ^ { T } \mathcal { D } \widetilde { \phi } _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } , } \end{array}
$$

where recall that $| \cdot | _ { + }$ denotes the pseudo-determinant, $\mathcal { D } \tilde { \phi } _ { \theta } ( v ) [ \cdot ]$ is the differential of $\widetilde { \phi } _ { \theta }$ at $\boldsymbol { v }$ , and we denote $\mathcal { D } \widetilde { \phi } _ { y } ( \boldsymbol { v } ^ { \prime } ) [ \mathcal { V } ] = \left[ \mathcal { D } \widetilde { \phi } _ { y } ( \boldsymbol { v } ^ { \prime } ) [ \widetilde { \boldsymbol { v } } _ { 1 } ] , \mathcal { D } \widetilde { \phi } _ { y } ( \boldsymbol { v } ^ { \prime } ) [ \widetilde { \boldsymbol { v } } _ { 2 } ] , \cdots , \mathcal { D } \widetilde { \phi } _ { y } ( \boldsymbol { v } ^ { \prime } ) [ \widetilde { \boldsymbol { v } } _ { D } ] \right]$ for $\mathcal { V } = [ \widetilde { v } _ { 1 } , \widetilde { v } _ { 2 } , \cdots , \widetilde { v } _ { D } ]$ .

(c) (Accept/reject the proposal) flip a coin and accept $y$ with probability $A ( \theta ^ { k - 1 } , y )$ and set $\theta ^ { k } = y$ ; otherwise, set $\theta ^ { k } = \theta ^ { k - 1 }$ .

Remark 1. The Metropolis-adjusted Langevin algorithm (MALA) is another well-known class of MCMC algorithms that utilizes additional gradient information about the target density to improve its mixing time compared with the Random-Walk Metropolis algorithm [24]. Let $\mu ^ { * } ( \theta ) \propto$ $\exp ( - f ( \theta ) )$ denote the target density with respect to the volume measure $\mu _ { \mathcal { M } }$ , where $f ( \cdot )$ is the potential function. Similar to the RRWM algorithm, we can develop a Riemannian Metropolisadjusted Langevin algorithm (RMALA) that leverages Riemannian gradient information for smooth potential functions. In the proposal step of the RMALA algorithm, a random vector $\widetilde { v }$ is drawn from $\mathcal { N } ( - \widetilde { h } \widetilde { I } \cdot$ · grad $f ( \theta ^ { k - 1 } ) , 2 \widetilde { h } \widetilde { I } )$ and then projected onto the tangent space $T _ { \theta ^ { k - 1 } } { \mathcal { M } }$ e. The acceptance ratio statistic is given by the following expression:

$$
\begin{array} { r l } & { \alpha ( \theta ^ { k - 1 } , y ) = \frac { \mu ^ { * } ( y ) \cdot \big ( \big | ( \mathcal { D } \widetilde { \phi } _ { y } ( v ^ { \prime } ) [ P _ { y } ] ) ^ { T } \mathcal { D } \widetilde { \phi } _ { y } ( v ^ { \prime } ) [ P _ { y } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } { \mu ^ { * } ( \theta ^ { k - 1 } ) \cdot \big ( \big | ( \mathcal { D } \widetilde { \phi } _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] ) ^ { T } \mathcal { D } \widetilde { \phi } _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } } \\ & { \quad \cdot \frac { \exp \big ( - ( v ^ { \prime } + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( y ) ) ^ { T } ( P _ { y } \widetilde { I } P _ { y } ) ^ { \dagger } ( v ^ { \prime } + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( y ) ) / ( 4 \widetilde { h } ) \big ) } { \exp \big ( - ( v + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( \theta ^ { k - 1 } ) ) ^ { T } \big ( P _ { \theta ^ { k - 1 } } \widetilde { I } P _ { \theta ^ { k - 1 } } \big ) ^ { \dagger } \big ( v + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( \theta ^ { k - 1 } ) \big ) / ( 4 \widetilde { h } ) \big ) } . } \end{array}
$$

Further details about the RMALA algorithm are provided in Appendix C.3. In particular, RRWM is a zero-th order sampling algorithm (relying only on log-density evaluations), while RMALA is a first-order algorithm that additionally incorporates gradient information of the log-density.

A crucial component of the RRWM algorithm is the choice of the retraction $\tilde { \phi } _ { \theta } ( \cdot )$ for the Riemannian submanifold $\mathcal { M }$ . However, in many problems, $\mathcal { M }$ is not equipped with a ready-made retraction or explicit local parameterization. Instead, it is often defined implicitly through constraints, such as a solution set $\mathcal { M } _ { \mathbf { q } } = \{ \theta \in \mathbb { R } ^ { D } : \mathbf { q } ( \theta ) = 0 \}$ , or through a structural property, such as the fixed-rank matrix manifold $\mathcal { M } _ { r } = \{ B \in \mathbb { R } ^ { p \times k } : \mathrm { r a n k } ( B ) = r \}$ . Therefore, it is necessary to identify a suitable retraction for the specific manifold of interest to ensure that randomly generated samples from the tangent space can be correctly mapped back onto the manifold. One particularly convenient choice is the retraction considered in [78], which coincides with the inverse $\phi _ { \theta } : V _ { \theta } \to U _ { \theta }$ of the projection map $\psi _ { \theta } : U _ { \theta } \to V _ { \theta }$ , where $\psi _ { \boldsymbol { \theta } } ( y ) = \mathrm { P r o j } _ { T _ { \boldsymbol { \theta } } \mathcal { M } } ( y - \boldsymbol { \theta } )$ as defined in Section 2. This retraction $\phi _ { \theta }$ has the advantage of eliminating the Jacobian factor in the acceptance ratio:

$$
\left| ( \mathcal { D } \phi _ { y } ( v ^ { \prime } ) [ P _ { y } ] ) ^ { T } \mathcal { D } \phi _ { y } ( v ^ { \prime } ) [ P _ { y } ] \right| _ { + } = \left| ( \mathcal { D } \phi _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] ) ^ { T } \mathcal { D } \phi _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] \right| _ { + } ,
$$

where $v ^ { \prime } = \psi _ { y } ( \theta ^ { k - 1 } )$ , $v = \psi _ { \theta ^ { k - 1 } } ( y )$ . As a result, the acceptance ratio in the RRWM algorithm can be simplified to

$$
\mathcal { A } ( \theta ^ { k - 1 } , y ) = 1 \wedge \frac { \mu ^ { * } ( y ) \cdot \exp \big ( - v ^ { \prime T } ( P _ { y } \widetilde { I } P _ { y } ) ^ { \dagger } v ^ { \prime } / ( 4 \widetilde { h } ) \big ) } { \mu ^ { * } ( \theta ^ { k - 1 } ) \cdot \exp \big ( - v ^ { T } ( P _ { \theta ^ { k - 1 } } \widetilde { I } P _ { \theta ^ { k - 1 } } ) ^ { \dagger } v / ( 4 \widetilde { h } ) ) \big ) } .
$$

According to [78], if the manifold is a solution manifold $\mathcal { M } _ { \mathbf { q } }$ for some smooth function $\mathbf { q }$ , then $y = \phi _ { \theta } ( v )$ can be obtained by numerically solving the equation

$$
y = \theta + v + Q _ { \theta } ^ { T } { a } \quad \mathrm { w h e r e ~ } Q _ { \theta } = { \bf J _ { q } } ( \theta ) \mathrm { a n d } { \bf q } ( \theta + v + Q _ { \theta } ^ { T } { a } ) = 0 _ { k } ,
$$

for example using the Newton–Raphson algorithm, where ${ \bf J } _ { \bf q } ( \theta )$ denotes the $k \times D$ Jacobian matrix of q at θ, i.e., -Jq(θ)ij = $\begin{array} { r } { \left[ \mathbf { J } _ { \mathbf { q } } ( \theta ) \right] _ { i j } = \frac { \partial q _ { i } ( \theta ) } { \partial \theta _ { j } } } \end{array}$ for $i \in \left\lfloor k \right\rfloor$ and $j \in \left[ D \right]$ . However, this numerical scheme for computing $\phi _ { \theta } ( v )$ does not apply to more general manifolds where the function $\mathbf { q } ( \cdot )$ does not exist or is difficult to obtain. To address this, we propose a more general numerical scheme for computing $\phi _ { \theta } ( v )$ by solving the following optimization problem: given a tangent vector $v \in T _ { \theta } { \mathcal { M } }$ with sufficiently small norm $\lVert v \rVert$ , there exists $r > 0$ such that $y = \phi _ { \theta } ( v )$ can be identified as the unique solution to

$$
\underset { y \in \mathcal { M } \cap B _ { r } ( \theta ) } { \arg \operatorname* { m i n } } \left. \mathrm { P r o j } _ { T _ { \theta } \mathcal { M } } ( y - \theta ) - v \right. ^ { 2 } .
$$

The optimization problem (10) can be solved using the Riemannian gradient descent method or Riemannian Newton’s method, initialized at $\theta$ . Furthermore, the step “reject the proposal if $v \not \in V _ { \theta ^ { k - 1 } }$ or $\theta ^ { k - 1 } \notin U _ { y } "$ in the RRWM algorithm—used to prevent tangent vectors from escaping the domain of $\phi _ { \theta ^ { t } }$ or $\phi _ { y }$ —can be implemented by rejecting proposals when the algorithms for computing $\phi _ { \theta ^ { k - 1 } } ( v )$ or $\phi _ { y } ( v ^ { \prime } )$ with $v ^ { \prime } = \mathrm { P r o j } _ { T _ { y } \mathcal { M } } ( \theta ^ { k - 1 } - y )$ fail to converge. Detailed algorithms are provided in Appendix C.

# 4.2 Mixing time analysis of RRWM algorithm for Bayesian RPETEL sampling

It is straightforward to verify that the Markov chain associated with RRWM is time-reversible and has $\mu ^ { * }$ as the stationary distribution. Nevertheless, obtaining a quantitative bound on the convergence rate of the algorithm is crucial for guiding its practical design and implementation. Following a common practice in the literature [22, 54], we analyze a $\zeta$ -lazy version of the RRWM algorithm, where at each iteration a coin is flipped: with probability $1 - \zeta$ , the algorithm proceeds with the proposal and Metropolis–Hastings acceptance step, and with probability $\zeta$ , the chain remains unchanged. We characterize the $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence for the Markov chain generated by this $\zeta$ -lazy version, assuming an $M _ { 0 }$ -warm start $\mu _ { 0 }$ .2 The $\varepsilon$ -mixing time is defined as the minimal number of steps required for the chain to reach $\varepsilon ^ { 2 }$ - $\chi ^ { 2 }$ divergence from the stationary distribution:

$$
\tau _ { \operatorname* { m i x } } ( \varepsilon , \mu _ { 0 } ) : = \operatorname* { i n f } \{ k \in \mathbb { N } : \sqrt { \chi ^ { 2 } ( \mu _ { k } , \mu ^ { * } ) } \leq \varepsilon \} .
$$

where $\mu _ { k }$ denotes the probability distribution of the Markov chain after $k$ steps.

Most existing analyses of MCMC mixing time are conducted in Euclidean settings and rely on restrictive assumptions such as smoothness or strong log-concavity of the target distribution [22, 74]. However, these assumptions are often violated by Bayesian posterior densities. [3] shows that, in large-sample regimes where the Bayesian posterior satisfies an asymptotic normality property, the Random-walk Metropolis (RWM) algorithm for sampling from the posterior restricted to a compact subset of $\mathbb { R } ^ { D }$ has an asymptotic $\varepsilon$ -mixing time upper bound of $O ( D ^ { 2 } \log ( \frac { 1 } { \varepsilon } ) )$ . This motivates the question of whether the Riemannian Random-walk Metropolis (RRWM) algorithm can achieve faster mixing when the parameter space is a lower-dimensional submanifold.

In the next theorem, we show that for the Bayesian RPETEL posterior $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ , in the large-sample regime, the $\varepsilon$ -mixing time of the RRWM algorithm scales as $O \big ( ( d + \log ( \frac { 1 } { \varepsilon } ) ) \cdot \log \frac { 1 } { \varepsilon } \big )$ , given a warm start, an appropriate covariance matrix $\tilde { I }$ , and a step size $\bar { h } \asymp n ^ { - 1 } ( d + \log ( \frac { 1 } { \varepsilon } ) ) ^ { - 1 } .$ . This behavior differs from that of the conventional RWM algorithm in the ambient space $\mathbb { R } ^ { D }$ , where the mixing time grows at least linearly with the ambient dimension $D$ [31]. The mixing time for sampling from $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ using RRWM depends only on the intrinsic dimension $d$ , demonstrating that incorporating manifold structure into Bayesian inference yields computational advantages in addition to statistical ones.

The main challenge in bounding the mixing time of the RRWM algorithm arises from the irregularity of the density of $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ with respect to the volume measure on $\mathcal { M }$ : the density may be non-log-concave or even discontinuous. Nevertheless, as shown in Theorem 2, the Bayesian RPETEL posterior $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ converges to a multivariate normal distribution after projection onto the tangent space $T _ { \theta ^ { * } } { \mathcal { M } }$ . Leveraging this result, we obtain the following corollary, which bounds the mixing time of the RRWM algorithm by showing that its convergence behavior is comparable to that of sampling from the corresponding multivariate normal limit. For simplicity, we take the retraction $\widetilde { \phi } _ { \theta }$ to be $\phi _ { \theta }$ , the local inverse of the projection map $\psi _ { \boldsymbol { \theta } } ( y ) = \mathrm { P r o j } _ { T _ { \boldsymbol { \theta } } \mathcal { M } } ( y - \boldsymbol { \theta } )$ defined in Section 2.

Corollary 4. Assume the conditions of Theorem $\boldsymbol { \mathcal { Z } }$ hold, and suppose there exist $n$ -independent constants $\rho _ { 2 } \geq \rho _ { 1 } > 0$ such that $\rho _ { 1 } \leq \eta ^ { T } \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \Delta _ { \theta ^ { * } } ^ { \dagger } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } \eta \leq \rho _ { 2 }$ for every unit vector $\eta \in T _ { \theta ^ { * } } { \mathcal { M } }$ . Then, for sufficiently large $n$ , there exists a set $A \subset \mathcal { X } ^ { n }$ satisfying $\mathbb { P } ( X ^ { ( n ) } \in \mathcal { A } ) \geq 1 - n ^ { - 1 }$ such that the following holds for every dataset $X ^ { ( n ) } \in { \mathcal { A } }$ : let $\mu _ { 0 }$ be an $M _ { 0 }$ -warm start with respect to $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ . For any positive constant c and accuracy level $\begin{array} { r } { \varepsilon \geq \frac { M _ { 0 } } { n ^ { c } } } \end{array}$ nc , there exist $( n , d , D )$ - independent absolute constants $( c _ { 0 } , C _ { 1 } )$ such that the $\zeta$ -lazy version $\left. \zeta \in \left( 0 , \textstyle { \frac { 1 } { 2 } } \right] \right.$ of the RRWM algorithm targeting $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ , using the retraction $\phi _ { \theta } ( \cdot )$ and step-size parameter $\widetilde { h } = h / n$ with $\begin{array} { r } { h = c _ { 0 } \rho _ { 2 } ^ { - 1 } \big ( d + \log ( \frac { M _ { 0 } d \rho _ { 2 } } { \varepsilon \rho _ { 1 } } ) \big ) ^ { - 1 } } \end{array}$ , has an $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence bounded by

$$
\operatorname { i m i x } ( \varepsilon , \mu _ { 0 } ) \leq \frac { C _ { 1 } } { \zeta } \bigg \{ \bigg [ \kappa \cdot \Big ( d + \log \Big ( \frac { M _ { 0 } d \kappa } { \varepsilon } \Big ) \Big ) \cdot \log \Big ( \frac { \log M _ { 0 } } { \varepsilon } \Big ) \bigg ] \vee \log ( M _ { 0 } ) \bigg \} , \quad w h e r e \quad \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } .
$$

Remark 2. Corollary 4 shows that the mixing time of the RRWM algorithm for sampling from the Bayesian RPETEL posterior is linear in the intrinsic dimension d and independent of the ambient dimension $D$ , given a suitable pre-conditioning matrix $\widetilde { I }$ and initial distribution. This result also implies that RRWM achieves faster convergence when $\kappa \approx 1$ , that is, when the pre-conditioning covariance matrix $\boldsymbol { \widetilde { I } } \in \mathbb { R } ^ { D \times D }$ for the proposal state is chosen such that $P _ { \theta ^ { * } } \widetilde { I } P _ { \theta ^ { * } } \approx \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger }$ where $P _ { \theta ^ { * } }$ denotes the projection matrix onto $T _ { \theta ^ { * } } { \mathcal { M } }$ . We suggest two approaches for selecting an appropriate $\widetilde { I }$ :

1. Direct estimation of $\mathcal { H } _ { \theta ^ { \ast } }$ and $\Delta _ { \theta ^ { * } }$ : obtain a consistent estimator $\widehat { \theta }$ of $\theta ^ { * }$ (for example, via empirical risk minimization), and estimate $\mathcal { H } _ { \theta ^ { \ast } }$ and $\Delta _ { \theta ^ { * } }$ by replacing $\theta ^ { * }$ with $\widehat { \theta }$ and using empirical averages in place of population expectations based on $X ^ { ( n ) }$ . Then choose $\widetilde { I }$ as any symmetric positive definite $D \times D$ matrix satisfying $P _ { \widehat { \theta } } \widetilde { I } P _ { \widehat { \theta } } = \widehat { \mathcal { H } } ^ { \dagger } \widehat { \Delta } \widehat { \mathcal { H } } ^ { \dagger }$ , where $\widehat { \mathcal { H } }$ and $\widehat { \Delta }$ denote the corresponding estimators of $\mathcal { H } _ { \theta ^ { \ast } }$ and $\Delta _ { \theta ^ { \ast } }$ .

2. Estimation of $\mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger }$ from posterior samples: when direct evaluation of the Riemannian Hessian of $\mathcal { R } ( \cdot )$ is infeasible, we can estimate $\mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger }$ using the covariance of $\psi _ { \widehat { \theta _ { p } } \# } \Pi _ { \mathrm { R P } } ^ { ( n ) }$ Initialize $\widetilde { I } = I _ { D }$ and run the RRWM algorithm for a moderate number of iterations $K$ . Let $\widehat { \theta } _ { p }$ ebe the mean of the resulting samples $\{ \theta ^ { k } \} _ { k = 1 } ^ { K }$ , and denote the covariance matrix of $\{ \psi _ { \widehat { \theta } _ { p } } ( \theta ^ { k } ) \} _ { k = 1 } ^ { K }$ by $\widehat { \Sigma } _ { p }$ . Then set $\tilde { I }$ such that $P _ { \widehat { \theta } _ { p } } ^ { T } \widetilde { I } P _ { \widehat { \theta } _ { p } } = n \cdot \widehat { \Sigma } _ { p }$ .

More generally, a similar mixing time bound can be established for any target posterior $\mu ^ { * }$ that satisfies a manifold Bernstein–von Mises theorem, as stated in Theorem 3 of Appendix B, with the proof given in Appendix H. Our analysis builds upon and extends the mathematical techniques, particularly the conductance profile method, developed in [22, 69]. We generalize the mixing time analysis from the Euclidean to the non-Euclidean setting by showing that, under suitable regularity conditions, the conductance profile associated with $\mu ^ { * }$ can be lower bounded by that of $\mu ^ { * }$ restricted to a high-probability region $K _ { \theta }$ around $\theta ^ { * }$ , denoted $\mu ^ { * } | _ { K _ { \theta } }$ , up to higher-order terms. The analysis then reduces to the Euclidean space $\mathbb { R } ^ { d }$ by establishing a one-to-one correspondence between local coordinates in $\mathbb { R } ^ { d }$ and points on $K _ { \theta }$ . Using the manifold Bernstein–von Mises theorem, we further perform a perturbation analysis that connects the Markov transition kernel of the local-coordinate representation of $\theta \sim \mu ^ { * } | _ { K _ { \theta } }$ with that of its Gaussian approximation. Figure 1 presents the effective sample size (ESS) for a fixed number of iterations obtained by the RRWM algorithm when sampling from the manifold-supported Bayesian posterior $\Pi _ { \mathrm { M } }$ and the Bayesian RPETEL posterior ΠRP in Example 1 (with $d = 3 < D = 4$ ), as well as by the conventional RWM algorithm when sampling from the Euclidean posterior $\Pi _ { \mathrm { E } }$ . The RRWM ESS values range approximately from 940 to 1100, whereas the RWM ESS is about 680, yielding a ratio close to $D / d$ and demonstrating the computational advantage of the manifold-supported posterior.

# 5 Numerical Illustration

In this section, we evaluate the frequentist operating characteristics of the Bayesian RPETEL method in three problems: (1) multiple-quantile modeling with common slopes; (2) spectral projector estimation; and (3) mean parameter inference for diffusion tensors. Unless otherwise specified, for all scenarios considered below, we generate posterior samples $\{ \theta ^ { k } \} _ { k = 1 } ^ { K }$ from the Bayesian RPETEL posterior and competitor posteriors using the RRWM algorithm (see Algorithm 5 in Appendix C), with $K$ specified in each example. The regularization parameter $\alpha _ { n }$ is set to dible interval for $2 \log n$ throughout. For a function $f ( \theta )$ using the $\frac { \alpha } { 2 }$ and $1 - { \frac { \alpha } { 2 } }$ quantiles of the posterior samples $f : \mathcal { M }  \mathbb { R }$ , we construct a $( 1 - \alpha )$ $\{ f ( \theta ^ { k } ) \} _ { k = 1 } ^ { K }$ Bayesian We also construct a $( 1 - \alpha )$ credible region for $\theta$ using equation (4), where the quantile $q _ { \alpha }$ is approximated from the corresponding $\alpha$ -quantile of the posterior samples. Coverage probabilities for the resulting credible intervals or credible regions are estimated based on 1000 simulation replicates. Since closed-form expressions for the population-level global risk minimizers are not available, we approximate them using empirical risk minimizers computed from a large sample of size $5 \times 1 0 ^ { 5 }$ in all experiments. We consider example-specific competitor methods, with details provided in the corresponding sections. These competitors include Gibbs posterior, parametric Bayesian, and Bayesian ETEL approaches, thereby offering a comprehensive set of benchmarks for comparison.

# 5.1 Multiple quantile modeling with common slopes

The multiple linear quantile regression problem aims to estimate several quantile regression coefficients simultaneously. At the population level, it solves

$$
\underset { u , \beta } { \arg \operatorname* { m i n } } \ \sum _ { j = 1 } ^ { J } \mathbb { E } \big [ \rho _ { \tau _ { j } } ( Y - u _ { j } - \widetilde { X } ^ { T } \beta _ { j } ) \big ] ,
$$

where $u = ( u _ { 1 } , \dotsc , u _ { J } )$ are intercepts, $\beta = ( \beta _ { 1 } , \dotsc , \beta _ { J } )$ are slope vectors, $( \tau _ { 1 } , \dots , \tau _ { J } )$ are the quantile levels, and $\rho _ { \tau } ( t ) = t \{ \tau - { \bf 1 } ( t \leq 0 ) \}$ is the check loss. Estimating each quantile coefficient separately can be inefficient, so to borrow information across quantile levels, one may impose a common-slope constraint while allowing intercepts to vary [76], restricting $( u , \beta )$ to the hyperplane $\mathcal { M } = \{ ( u , \beta ) : \beta _ { 1 } = \cdot \cdot \cdot = \beta _ { J } \}$ .

In this experiment, we consider quantile levels $( \tau _ { 1 } , \tau _ { 2 } , \tau _ { 3 } ) = ( 0 . 2 , 0 . 4 , 0 . 7 )$ and simulate data as follows. We generate $n$ i.i.d. samples $\widetilde { X } _ { i } \sim { \mathcal { N } } ( 0 , 1 )$ and errors $\varepsilon _ { i } \sim \mathrm { L a p l a c e } ( 0 , 1 )$ independently, and set $Y _ { i } = \widetilde { X } _ { i } + \varepsilon _ { i } ( 1 + \epsilon \widetilde { X } _ { i } )$ for $i = 1 , \ldots , n$ . Let $q _ { \tau }$ denote the $\tau$ -th quantile of $\mathrm { L a p l a c e } ( 0 , 1 )$ . Then the population solution to (6) is $\boldsymbol { u } ^ { * } = ( q _ { 0 . 2 } , q _ { 0 . 4 } , q _ { 0 . 7 } )$ and $\beta ^ { * } = 1 + \epsilon u ^ { * }$ . We consider two cases: $\epsilon = 0$ , where the common-slope model is correctly specified (so $( u ^ { \ast } , \beta ^ { \ast } ) \in \mathcal { M }$ ), and $\epsilon = 0 . 1$ , where the model is misspecified. We compare three posteriors: (1) BRPETEL: the Bayesian RPETEL posterior with prior $\Pi _ { \mathrm { M } }$ uniform on $\{ ( u , \beta ) \in \mathcal { M } : | u _ { j } | < 1 0 0$ , $| \beta _ { j } | < 1 0 0 \}$ ;

Table 1: MSE (reported as $\times 1 0 ^ { - 2 }$ ) and effective sample size (ESS) for multiple quantile modeling with common slopes. Here MSE is defined as the average of $\| ( \widehat { \boldsymbol { u } } _ { p } , \widehat { \boldsymbol { \beta } } _ { p } ) - ( \boldsymbol { u } ^ { * } , \boldsymbol { \beta } ^ { * } ) \| ^ { 2 }$ over 1000 replications, and ESS is computed per parameter dimension of $\theta = \left( u , \beta \right)$ , averaged across dimensions and then across the 1000 replications. Results are shown for correctly specified ( $\varepsilon = 0$ ) and misspecified ( $\varepsilon = 0 . 1$ ) settings, and for sample sizes $n \in \{ 5 0 0 , 1 0 0 0 \}$ .   

<table><tr><td rowspan="2" colspan="3"></td><td colspan="3">Correctly specified (ε=0)</td><td colspan="3">Misspecified (ε = 0.1)</td></tr><tr><td>BRPETEL</td><td>BPETELM</td><td>BPETELE</td><td>BRPETEL</td><td>BPETELm</td><td>BPETELE</td></tr><tr><td rowspan="2">n = 500</td><td>MSE</td><td>1.144</td><td>1.140</td><td>1.418</td><td>1.657</td><td>1.780</td><td></td><td>1.437</td></tr><tr><td>ESS</td><td>695</td><td></td><td>673</td><td>294</td><td>671</td><td>629</td><td>282</td></tr><tr><td rowspan="2">n = 1000</td><td>MSE</td><td>0.581</td><td></td><td>0.576</td><td>0.724</td><td>1.084</td><td>1.191</td><td>0.730</td></tr><tr><td>ESS</td><td>722</td><td>709</td><td></td><td>310</td><td>702</td><td>645</td><td>302</td></tr></table>

(2) BPETELM: the Bayesian PETEL posterior (full-gradient ETEL) with the same manifold prior $\Pi _ { \mathrm { M } }$ ; (3) BPETELE: the Bayesian PETEL posterior (full-gradient ETEL) with Euclidean prior $\Pi _ { \mathrm { E } }$ uniform on $\{ ( u , \beta ) \in \mathbb { R } ^ { 6 } : | u _ { j } | < 1 0 0$ , $| \beta _ { j } | < 1 0 0 \}$ . Posterior summaries are computed using $K = 1 5 , 0 0 0$ Metropolis–Hastings draws, with the posterior mean $( \hat { u } _ { p } , \hat { \beta } _ { p } )$ used as the point estimator. For posteriors with prior $\Pi _ { \mathrm { M } }$ , we use the RRWM algorithm with step size $\widetilde { h } = 1 / n$ and ${ \widetilde { I } = I _ { 6 } }$ . For the Euclidean prior $\Pi _ { \mathrm { E } }$ , we use the RWM algorithm with proposal covariance $( 1 / n ) I _ { 6 }$ .

We report the mean squared error $\mathrm { M S E } = \| ( \hat { u } _ { p } , \hat { \beta } _ { p } ) - ( u ^ { * } , \beta ^ { * } ) \| ^ { 2 }$ and sampling efficiency via the effective sample size (ESS), averaged across dimensions. We consider $n = 5 0 0$ and $n = 1 0 0 0$ , with each configuration replicated 1000 times. Results are summarized in Table 1. Under correct specification ( $\epsilon = 0$ ), the manifold-supported posteriors (BRPETEL, BPETELM) achieve lower MSE than the Euclidean BPETEL $\mathrm { E }$ , with BRPETEL and BPETEL $\mathrm { M }$ having nearly identical MSE. Under misspecification ( $\epsilon = 0 . 1$ ), BRPETEL and BPETELM have larger MSE than BPETEL $\mathrm { E }$ due to the bias induced by the common-slope restriction; however, BRPETEL outperforms BPETELM, showing improved robustness. In terms of computation, the manifoldsupported posteriors yield substantially higher ESS than BPETEL $\mathbf { E }$ , and BRPETEL additionally shows a slight ESS advantage over BPETELM.

Table 2 reports the sampling coverages of the $9 5 \%$ credible intervals and their average lengths for $u _ { 1 }$ , $u _ { 2 }$ , $u _ { 3 }$ , and $\beta _ { 1 }$ under the two manifold-supported posteriors (BRPETEL and BPETELM), targeting the components of the risk minimizer on $\mathcal { M }$ (not $( u ^ { * } , \beta ^ { * } )$ ), based on 1000 replications. Under correct specification ( $\epsilon = 0$ ), both methods achieve coverage close to $9 5 \%$ with nearly identical interval lengths, with BRPETEL’s coverages slightly closer to the nominal level. Increasing $n$ improves coverage for both methods. Under misspecification ( $\epsilon = 0 . 1$ ), BRPETEL maintains coverages near 93–95% for all coordinates, whereas BPETELM shows notable undercoverage for $\beta _ { 1 }$ (e.g., 87.7% when $n = 1 0 0 0$ ). Increasing $n$ improves the coverage of BRPETEL but has little effect on BPETEL $^ { | \mathrm { M } }$ . Interval lengths are nearly identical across methods (especially for $n = 1 0 0 0$ ), indicating that BRPETEL’s superior coverage is due to better calibration rather than wider intervals.

# 5.2 Spectral projectors of covariance matrices

Let $X \in \mathbb { R } ^ { p }$ be a zero-mean random vector with covariance matrix $\Sigma ^ { * }$ . Consider a direct sum of the eigenspaces associated with the first $\mathcal { P } _ { k } ( \Sigma ^ { * } )$ , defined as $\begin{array} { r } { \mathcal { P } _ { k } \mathopen { } \mathclose \bgroup \left( \Sigma ^ { * } \aftergroup \egroup \right) = \sum _ { i = 1 } ^ { k } u _ { i } ^ { * } u _ { i } ^ { * ^ { T } } } \end{array}$ $k$ largest eigenvalues of , where $( u _ { 1 } ^ { * } , u _ { 2 } ^ { * } , \cdots , u _ { k } ^ { * } )$ $\Sigma ^ { * }$ and the corresponding projectors are the eigenvectors associated with the first largest eigenvalues of $\Sigma ^ { * }$ . Our goal is to quantify the uncertainty in recovering the true spectral projector $P _ { k } ^ { * } = \mathcal { P } _ { k } ( \Sigma ^ { * } )$ [64]. We view $P _ { k } ^ { * }$ as the minimizer of the risk function $\mathbb { E } [ - \mathrm { t r } ( P X X ^ { T } ) ]$ on the Grassmannian manifold $\mathcal { M } = \{ P \in \mathbb { R } ^ { p \times p } | P ^ { 2 } = P$ , $P ^ { T } = P$ , $\operatorname { t r } ( P ) = k  \}$ . It is noteworthy that $\mathcal { M }$ can be regarded as a solution manifold in $\mathbb { R } ^ { p ^ { 2 } }$ by flattening matrices in the Grassmannian manifold into $p ^ { 2 }$ -dimensional vectors.

Table 2: Coverage probabilities and average lengths of 95% credible intervals for multiplequantile modeling with common slopes, computed over 1000 replications. Columns labeled $u _ { i }$ and $\beta _ { 1 }$ report, respectively, the sampling coverage (in $\%$ ) and average interval length for the $_ i$ th component of $u$ and for $\beta _ { 1 }$ . Coverage targets the corresponding components of the risk minimizer on the manifold $\mathcal { M }$ (not $( u ^ { * } , \beta ^ { * } )$ ).   

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Correctly specified (ε = 0)</td><td colspan="4">Misspecifed (ε = 0.1)</td></tr><tr><td>u1</td><td>u2</td><td>u3</td><td>β1</td><td>u1</td><td>u2</td><td>u3</td><td>β1</td></tr><tr><td rowspan="4">BRPETEL</td><td>Coverage (n = 500)</td><td>94.5</td><td>94.1</td><td>93.8</td><td>93.0</td><td>93.1</td><td>94.0</td><td>94.2</td><td>92.9</td></tr><tr><td>Length (n = 500)</td><td>0.255</td><td>0.155</td><td>0.193</td><td>0.153</td><td>0.254</td><td>0.157</td><td>0.194</td><td>0.153</td></tr><tr><td>Coverage (n = 1000)</td><td>94.6</td><td>94.4</td><td>94.8</td><td>93.6</td><td>94.2</td><td>94.2</td><td>94.3</td><td>93.9</td></tr><tr><td>Length (n = 1000)</td><td>0.177</td><td>0.109</td><td>0.136</td><td>0.107</td><td>0.177</td><td>0.109</td><td>0.136</td><td>0.107</td></tr><tr><td rowspan="4">BPETELM</td><td>Coverage (n = 500)</td><td>94.0</td><td>93.6</td><td>93.2</td><td>92.3</td><td>91.2</td><td>92.8</td><td>93.5</td><td>88.0</td></tr><tr><td>Length (n = 500)</td><td>0.253</td><td>0.154</td><td>0.192</td><td>0.146</td><td>0.252</td><td>0.154</td><td>0.190</td><td>0.144</td></tr><tr><td>Coverage (n = 1000)</td><td>94.1</td><td>93.9</td><td>94.1</td><td>93.1</td><td>91.9</td><td>92.5</td><td>93.3</td><td>87.7</td></tr><tr><td>Length (n = 1000)</td><td>0.177</td><td>0.109</td><td>0.136</td><td>0.103</td><td>0.176</td><td>0.109</td><td>0.135</td><td>0.102</td></tr></table>

We generate $n$ i.i.d. samples $\begin{array} { r } { X _ { i } \sim \frac { 1 } { 2 } \mathcal { N } ( 0 , \Sigma _ { 0 } ) + \frac { 1 } { 2 } \mathrm { U n i f o r m } ( [ - 1 , 1 ] ^ { 3 } ) } \end{array}$ where

$$
\Sigma _ { 0 } = \left[ \begin{array} { c c c } { { 1 } } & { { 0 . 1 } } & { { 0 . 1 } } \\ { { 0 . 1 } } & { { 1 . 2 } } & { { 0 . 1 } } \\ { { 0 . 1 } } & { { 0 . 1 } } & { { 0 . 3 } } \end{array} \right] .
$$

Letting $\Sigma ^ { * }$ denote the population covariance matrix for the generated data—computed analytically under this model—we focus on inferring the projector $\mathcal { P } _ { 2 } ( \Sigma ^ { * } )$ . The prior $\Pi$ has density proportional to 1 $( \Vert P \Vert _ { \mathrm { F } } ^ { 2 } < 1 0 0 )$ with respect to the volume measure on $\mathcal { M }$ , where $\Vert \cdot \Vert _ { \mathrm { F } }$ denotes the Frobenius norm. In addition to our Bayesian RPETEL posterior, we consider two competitors. (i) A Gibbs posterior with learning rate $\beta$ :

$$
\Pi _ { G } ( \mathrm { d } P \mid X ^ { ( n ) } ) \propto \exp \Big ( - \beta \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , P ) \Big ) \Pi ( \mathrm { d } P ) , \qquad \ell ( X , P ) = \mathrm { t r } ( P X X ^ { \top } ) ,
$$

where $\beta$ is calibrated via the stochastic approximation method of [66] to match nominal coverage based on bootstrap estimation.3 The selected value is approximately 0.95, and we fix $\beta = 0 . 9 5$ across replications. (ii) A misspecified parametric Bayesian method assuming the data follow $\mathcal { N } ( 0 , \Sigma )$ , with an inverse-Wishart prior $I W ( p + 1 , I _ { p } )$ on $\Sigma$ . Under this model, the posterior is $\begin{array} { r } { I W ( n + d + 1 , I + \sum _ { i = 1 } ^ { n } X _ { i } X _ { i } ^ { \prime } ) } \end{array}$ . We construct credible intervals by taking spectral projectors of posterior draws of $\Sigma$ ; we refer to this method as MVN-IW.

The coverage probabilities of credible intervals for the diagonal elements of $\mathcal { P } _ { 2 } ( \Sigma ^ { * } )$ and coverage of credible regions for different sample sizes are presented in Table 3. When $n = 5 0 0$ , Bayesian RPETEL exhibits slightly better performance than both the Gibbs posterior and MVN-IW. For example, for the target 95% coverage, the Gibbs posterior deviates by 2.7% for $\theta _ { 5 }$ , MVN-IW by $2 . 0 \%$ , whereas Bayesian RPETEL deviates by at most 1.8%. However, all three methods tend to underestimate the precision of $\theta _ { 5 }$ when $n = 5 0 0$ . With $n = 1 0 0 0$ , both Bayesian RPETEL and MVN-IW show substantial improvement, while the Gibbs posterior does not improve and continues to underestimate the precision of $\theta _ { 5 }$ . Overall, Bayesian RPETEL outperforms MVN-IW even at larger sample sizes.

Table 3: Coverage probabilities for inference on the spectral projectors of the covariance matrix: “ $\theta _ { k }$ ” represents the credible interval for the kth dimension of the parameter θ obtained by flattening the matrix $P \in \mathbb { R } ^ { d \times d }$ into a vector (by column), and “Credible region” refers to the credible region given in (4).   

<table><tr><td colspan="2">Target coverage</td><td colspan="2">(%) 01</td><td colspan="2">05 09</td><td>Credible region</td></tr><tr><td rowspan="6">Bayesian RPETEL n = 500 Gibbs posterior</td><td>95</td><td>94.8</td><td>96.8</td><td>94.0</td><td>94.1</td></tr><tr><td>90</td><td>89.2</td><td>91.5</td><td>88.4</td><td>88.8</td></tr><tr><td>95</td><td>95.0</td><td>97.7</td><td>95.4</td><td>94.1</td></tr><tr><td>90</td><td>88.7</td><td>93.9</td><td>90.9</td><td>89.1</td></tr><tr><td>95</td><td>97.7</td><td>97.0</td><td>96.1</td><td>96.1</td></tr><tr><td>90</td><td>92.4</td><td>93.7</td><td>91.9</td><td>90.9</td></tr><tr><td rowspan="5">Bayesian RPETEL n = 1000 Gibbs posterior</td><td>95</td><td>95.0</td><td>95.9</td><td>95.0</td><td>94.1</td></tr><tr><td>90</td><td>90.1</td><td>90.9</td><td>89.1</td><td>88.9</td></tr><tr><td>95</td><td>96.5</td><td>97.9</td><td>95.6</td><td>95.7</td></tr><tr><td>90</td><td>90.4</td><td>94.3</td><td>91.0</td><td>90.6</td></tr><tr><td>95 90</td><td>95.9 91.8</td><td>95.6 90.7</td><td>96.3 91.1</td><td>96.4 91.7</td></tr></table>

# 5.3 Mean parameter inference for diffusion tensors

The superiority of the Bayesian RPETEL posterior over the competitors in the simulation examples supports our theoretical conclusion that the Bayesian RPETEL posterior can provide valid uncertainty quantification under certain regularity conditions. To examine how well these conditions hold in practice, we analyze an areal diffusion tensor imaging (DTI) dataset and compare Bayesian RPETEL with a parametric competitor. We employ a “subsampling” strategy to empirically assess inferential validity: we repeatedly sample $n = 1 0 0 0$ observations with replacement from the original dataset, perform this procedure 1000 times, and compute the coverage probabilities of the $9 5 \%$ Bayesian credible intervals produced by the Bayesian RPETEL posterior and the competitor posterior for covering the empirical risk minimizer $\hat { \theta }$ computed from the full dataset.

Diffusion tensor data [48, 47] consist of symmetric, positive definite $3 \times 3$ covariance matrices at each voxel, representing the anisotropic diffusion of water molecules. Such data arise not only in diffusion imaging but also in other contexts, including brain connectivity [39] and portfolio covariance estimation [28]. Our goal is to infer the mean parameter $\theta$ of a random covariance matrix $X \sim \mu _ { \theta }$ supported on $\mathbb { S } _ { + } ^ { 3 } = \{ \Sigma \in \mathbb { R } ^ { 3 \times 3 } : \Sigma$ is positive semidefinite}. Two common notions of the “mean” of a distribution $\mu$ on ${ \mathbb S } _ { + } ^ { 3 }$ are: (1) the extrinsic mean, defined as the minimizer over $\theta \in \mathbb { S } _ { + } ^ { 3 }$ of $\begin{array} { r } { \int \| \theta - X \| _ { 2 } ^ { 2 } \mu ( \mathrm { d } X ) } \end{array}$ , and (2) the Bures–Wasserstein (BW) barycenter [46], which is also the Fréchet mean:

$$
\theta ^ { * } \in \arg \operatorname* { m i n } _ { \theta \in \mathbb { S } _ { + } ^ { 3 } } \int _ { \mathbb { S } _ { + } ^ { 3 } } d _ { \mathrm { B W } } ^ { 2 } ( \theta , X ) \mu ( \mathrm { d } X ) ,
$$

where for $Q , S \in \mathbb { S } _ { + } ^ { 3 }$ the BW distance [6] is

$$
d _ { \mathrm { B W } } ^ { 2 } ( Q , S ) = \operatorname { t r } ( Q ) + \operatorname { t r } ( S ) - 2 \operatorname { t r } { \left( Q ^ { 1 / 2 } S Q ^ { 1 / 2 } \right) } ^ { 1 / 2 } ,
$$

which coincides with the 2-Wasserstein distance between $\mathcal { N } ( 0 , Q )$ and $\mathcal N ( 0 , S )$ .

We conduct a real data analysis using the diffusion tensor dataset from a $1 4 8 \times 1 9 0 \times 1 6 0$ scan of Gordon Kindlmann’s brain.4 Our focus is a spatial patch $\mathcal { D }$ of neighboring voxels around voxel (75, 95, 80) with neighborhood size 20: specifically, we extract the voxels $\{ ( x , y , z ) : x \in$ [55, 95], $y \in [ 7 5 , 1 1 5 ]$ , $z \in [ 6 0 , 1 0 0 ] \}$ and study the extrinsic/Fréchet mean of the diffusion tensors within this region. This large neighborhood provides a sufficiently large effective population to assess inferential validity under subsampling. We investigate three scientifically meaningful functionals of the mean diffusion tensor: fractional anisotropy (FA),5 trace, and maximum eigenvalue. Alongside Bayesian RPETEL, we consider a parametric Bayesian approach that assumes each $3 \times 3$ diffusion tensor follows a Wishart distribution $\mathrm { W I _ { 3 } } ( \theta , v )$ with (extrinsic) mean $\theta \in \mathbb { S } _ { + } ^ { 3 }$ and degrees of freedom $v > 4$ . The extrinsic mean $\theta$ is given an inverse-Wishart prior with mean $I _ { 3 }$ and degrees of freedom 5, and $v$ is assigned a uniform prior over [5, 50]. Posterior samples of the BW barycenter $\theta ^ { \prime }$ are obtained as a functional of posterior draws of $( \theta , v )$ , where $\theta ^ { \prime }$ solves

![](images/44297bd14c3e80456762e0a535695f51d3412d5b641dae69ddfe5e03769bb110.jpg)  
Figure 3: Density plots of the fractional anisotropy (FA) computed from the posterior samples obtained using Bayesian RPETEL and Wishart Modeling in the extrinsic mean example. The plot includes overlays from ten runs of experiments. The red vertical line indicates the FA of the empirical risk minimizer $\widehat { \theta }$ computed from the original dataset.

Table 4: Coverage probabilities ( $\%$ ) for inference of the fractional anisotropy (FA), trace and maximum eigenvalues of the extrinsic mean and Fréchet mean of the diffusion tensors (the target coverage is given by $9 5 \%$ ).   

<table><tr><td></td><td></td><td>FA</td><td>Trace</td><td>Maximum eigenvalue</td></tr><tr><td rowspan="2">Extrinsic Mean</td><td>Bayesian RPETEL</td><td>93.7</td><td>94.9</td><td>94.5</td></tr><tr><td>Wishart Modeling</td><td>99.4</td><td>59.2</td><td>81.6</td></tr><tr><td rowspan="2">Fréchet Mean</td><td>Bayesian RPETEL</td><td>94.1</td><td>93.8</td><td>93.6</td></tr><tr><td>Wishart Modeling</td><td>&gt;99.9</td><td>73.1</td><td>87.2</td></tr></table>

$$
\theta ^ { \prime } = \arg \operatorname* { m i n } _ { \theta ^ { \prime } \in \mathbb { S } _ { + } ^ { 3 } } \mathbb { E } _ { \mathrm { W I } _ { 3 } ( \theta , v ) } \big [ d _ { \mathrm { B W } } ^ { 2 } ( \theta ^ { \prime } , X ) \big ] ,
$$

assuming uniqueness. We refer to this approach as Wishart Modeling.

The coverage probabilities computed by subsampling are given in Table 4. We can observe that the Bayesian RPETEL posterior performs significantly better than the Wishart Modeling, especially for the inference of FA and Trace. For instance, Figure 3 displays the density plot of the FA for the posterior samples obtained from Bayesian RPETEL and Wishart Modeling in the extrinsic mean example. Notably, the posterior distribution from Wishart Modeling exhibits a much heavier tail compared to Bayesian RPETEL. As a result, the Wishart Modeling approach noticeably underestimates the precision of the inference for FA.

# 6 Conclusion and Discussion

In this paper, we have developed a general Bayesian inference framework for parameters constrained to a Riemannian submanifold, highlighting the benefits of incorporating manifold structure into Bayesian analysis. To further address potential model misspecification, we proposed a novel Bayesian method—Bayesian Riemannian Penalized Exponentially Tilted Empirical Likelihood (RPETEL)—for robust statistical inference with manifold-valued parameters. This approach avoids the need for a correctly specified likelihood and provides accurate uncertainty quantification with provable asymptotic guarantees. Numerical studies demonstrate that our method outperforms state-of-the-art alternatives in terms of inferential precision.

Our theoretical analysis in this work focuses on the mixing time of the Riemannian randomwalk Metropolis algorithm. Future work may extend this analysis to the Riemannian Metropolisadjusted Langevin and Hamiltonian Monte Carlo algorithms, which leverage higher-order information from the likelihood or loss function. Another promising direction is to extend the current methodology to incorporate additional inequality constraints on the parameters. Finally, although our development centers on parameter spaces with trivial or explicit embeddings in an ambient Euclidean space, it would be of substantial interest to explore more general Riemannian manifolds without explicit Euclidean embeddings, as well as settings where the underlying manifold structure is itself unknown, such as in text, network, and graph data.

# References

[1] Eddie Aamari and Clément Levrard. Nonasymptotic rates for manifold, tangent space and curvature estimation. The Annals of Statistics, 47(1):177 – 204, 2019.   
[2] Ignacio Alvarez, Jarad Niemi, and Matt Simpson. Bayesian inference for a covariance matrix. arXiv preprint arXiv:1408.4050, 2014.   
[3] Alexandre Belloni and Victor Chernozhukov. On the computational complexity of mcmcbased estimators in large samples. The Annals of Statistics, 37(4):2011–2055, 2009.   
[4] Clément Berenfeld, Paul Rosa, and Judith Rousseau. Estimating a density near an unknown manifold: a bayesian nonparametric approach. arXiv preprint arXiv:2205.15717, 2022.   
[5] Karthik Bharath, Alexander Lewis, Akash Sharma, and Michael V. Tretyakov. Sampling and estimation on manifolds using the langevin diffusion. Journal of Machine Learning Research, 26(71):1–50, 2025.   
[6] Rajendra Bhatia, Tanvi Jain, and Yongdo Lim. On the bures–wasserstein distance between positive definite matrices. Expositiones Mathematicae, 37(2):165–191, 2019.   
[7] Abhishek Bhattacharya and David B Dunson. Nonparametric bayesian density estimation on manifolds with applications to planar shapes. Biometrika, 97(4):851–865, 2010.   
[8] Indrabati Bhattacharya and Ryan Martin. Gibbs posterior inference on multivariate quantiles. arXiv preprint arXiv:2002.01052, 2020.   
[9] Rabi Bhattacharya and Lizhen Lin. Omnibus clts for fréchet means and nonparametric inference on non-euclidean spaces, 2013.   
[10] Rabi Bhattacharya and Lizhen Lin. Omnibus clts for fréchet means and nonparametric inference on non-euclidean spaces. Proceedings of the American Mathematical Society, 145(1):413–428, 2017.   
[11] Rabi Bhattacharya and Vic Patrangenaru. Large sample theory of intrinsic and extrinsic sample means on manifolds. The Annals of Statistics, 31(1):1–29, 2003.   
[12] Rabi Bhattacharya and Vic Patrangenaru. Large sample theory of intrinsic and extrinsic sample means on manifolds—II. The Annals of Statistics, 33(3):1225 – 1259, 2005.   
[13] Olivier Binette and Simon Guillotte. Bayesian nonparametrics for directional statistics. Journal of Statistical Planning and Inference, 216:118–134, 2022.   
[14] Christopher Bingham. An antipodally symmetric distribution on the sphere. The Annals of Statistics, 2(6):1201 – 1225, 1974.   
[15] Nicolas Boumal. An introduction to optimization on smooth manifolds. Cambridge University Press, 2023.   
[16] Nicolas Boumal. An introduction to optimization on smooth manifolds. Cambridge University Press, 2023.   
[17] Marcus Brubaker, Mathieu Salzmann, and Raquel Urtasun. A family of mcmc methods on implicitly defined manifolds. In Proceedings of the Fifteenth International Conference on Artificial Intelligence and Statistics, volume 22, pages 161–172. PMLR, 21–23 Apr 2012.   
[18] Simon Byrne and Mark Girolami. Geodesic monte carlo on embedded manifolds. Scandinavian Journal of Statistics, 40(4):825–845, sep 2013.   
[19] Ismaël Castillo, Gérard Kerkyacharian, and Dominique Picard. Thomas bayes’ walk on manifolds. Probability Theory and Related Fields, 158(3-4):665–710, 2014.   
[20] Rudrasis Chakraborty and Baba C Vemuri. Recursive frechet mean computation on the grassmannian and its applications to computer vision. In Proceedings of the IEEE International Conference on Computer Vision, pages 4229–4237, 2015.   
[21] Rudrasis Chakraborty and Baba C. Vemuri. Statistics on the Stiefel manifold: Theory and applications. The Annals of Statistics, 47(1):415 – 438, 2019.   
[22] Yuansi Chen, Raaz Dwivedi, Martin J. Wainwright, and Bin Yu. Fast mixing of metropolized hamiltonian monte carlo: Benefits of multi-step gradients. Journal of Machine Learning Research, 21(92):1–72, 2020.   
[23] Victor Chernozhukov and Han Hong. An MCMC approach to classical estimation. Journal of Econometrics, 115(2):293 – 346, 2003.   
[24] Sinho Chewi, Chen Lu, Kwangjun Ahn, Xiang Cheng, Thibaut Le Gouic, and Philippe Rigollet. Optimal dimension dependence of the metropolis-adjusted langevin algorithm. In Proceedings of Thirty Fourth Conference on Learning Theory, volume 134, pages 1260–1300. PMLR, 15–19 Aug 2021.   
[25] Siddhartha Chib, Minchul Shin, and Anna Simoni. Bayesian estimation and comparison of moment condition models. Journal of the American Statistical Association, 113(524):1656– 1668, 2018.   
[26] Vincent Divol. Measure estimation on manifolds: an optimal transport approach. Probability Theory and Related Fields, 183(1-2):581–647, 2022.   
[27] Jaap Eldering. Normally Hyperbolic Invariant Manifolds: The Noncompact Case. Atlantis Press, Paris, 2013.   
[28] Jianqing Fan, Yuan Liao, and Han Liu. An overview of the estimation of large covariance and precision matrices. The Econometrics Journal, 19(1):C1–C32, 2016.   
[29] O. P. Ferreira, M. S. Louzeiro, and L. F. Prudente. Gradient method for optimization on riemannian manifolds with lower bounded curvature. SIAM Journal on Optimization, 29(4):2517–2541, 2019.   
[30] Maurice Fréchet. Les éléments aléatoires de nature quelconque dans un espace distancié. In Annales de l’institut Henri Poincaré, volume 10, pages 215–310, 1948.   
[31] A. Gelman, W. R. Gilks, and G. O. Roberts. Weak convergence and optimal scaling of random walk Metropolis algorithms. The Annals of Applied Probability, 7(1):110 – 120, 1997.   
[32] Jayanta K Ghosh and RV Ramamoorthi. Bayesian nonparametrics. Springer, 2003.   
[33] Xiaoyang Guo, Aditi Basu Bal, Tom Needham, and Anuj Srivastava. Statistical shape analysis of brain arterial networks (ban). The Annals of Applied Statistics, 16(2):1130–1150, 2022.   
[34] Alastair R Hall. Generalized method of moments. OUP Oxford, 2004.   
[35] Thomas Hillen, Kevin J Painter, Amanda C Swan, and Albert D Murtha. Moments of von mises and fisher distributions and applications. Mathematical biosciences and engineering, 14(3):673–694, 2017.   
[36] Peter D Hoff. Simulation of the matrix bingham–von mises–fisher distribution, with applications to multivariate and relational data. Journal of Computational and Graphical Statistics, 18(2):438–456, 2009.   
[37] Andrew Holbrook, Alexander Vandenberg-Rodes, and Babak Shahbaba. Bayesian inference on matrix manifolds for linear dimensionality reduction. arXiv preprint arXiv:1606.04478, 2016.   
[38] Reshad Hosseini and Suvrit Sra. Matrix manifold optimization for gaussian mixtures. Advances in Neural Information Processing Systems, 28, 2015.   
[39] Madhura Ingalhalikar, Alex Smith, Drew Parker, Theodore D Satterthwaite, Mark A Elliott, Kosha Ruparel, Hakon Hakonarson, Raquel E Gur, Ruben C Gur, and Ragini Verma. Sex differences in the structural connectome of the human brain. Proceedings of the National Academy of Sciences, 111(2):823–828, 2014.   
[40] Alan Julian Izenman. Reduced-rank regression for the multivariate linear model. Journal of multivariate analysis, 5(2):248–264, 1975.   
[41] Michael Jauch, Peter D Hoff, and David B Dunson. Monte carlo simulation on the stiefel manifold via polar expansion. Journal of Computational and Graphical Statistics, 30(3):622– 631, 2021.   
[42] Hui Ji, Sibin Huang, Zuowei Shen, and Yuhong Xu. Robust video restoration by joint sparse and low rank matrix approximation. SIAM Journal on Imaging Sciences, 4(4):1122–1142, 2011.   
[43] Wenxin Jiang and Martin A Tanner. Gibbs posterior for variable selection in high-dimensional classification and data mining. The Annals of Statistics, 36(5):2207–2231, 2008.   
[44] David G Kendall. Shape manifolds, procrustean metrics, and complex projective spaces. Bulletin of the London mathematical society, 16(2):81–121, 1984.   
[45] BJK Kleijn and AW van der Vaart. The bernstein-von-mises theorem under misspecification. Electronic Journal of Statistics, 6:354–381, 2012.   
[46] Alexey Kroshnin, Vladimir Spokoiny, and Alexandra Suvorikova. Statistical inference for Bures–Wasserstein barycenters. The Annals of Applied Probability, 31(3):1264 – 1298, 2021.   
[47] Zhou Lan, Brian J. Reich, and Dipankar Bandyopadhyay. A spatial bayesian semiparametric mixture model for positive definite matrices with applications in diffusion tensor imaging. Canadian Journal of Statistics, 49(1):129–149, 2021.   
[48] Han Na Lee and Armin Schwartzman. Inference for eigenvalues and eigenvectors in exponential families of random symmetric matrices. Journal of Multivariate Analysis, 162:152–171, 2017.   
[49] John M Lee. Introduction to smooth manifolds. Springer, 2013.   
[50] Heng Lian, Weihua Zhao, and Yanyuan Ma. Multiple quantile modeling via reduced-rank regression. Statistica Sinica, 29(3):1439–1464, 2019.   
[51] Lizhen Lin, Drew Lazar, Bayan Sarpabayeva, and David B Dunson. Robust optimization and inference on manifolds. arXiv preprint arXiv:2006.06843, 2020.   
[52] Lizhen Lin, Niu Mu, Pokman Cheung, and David Dunson. Extrinsic Gaussian Processes for Regression and Classification on Manifolds. Bayesian Analysis, 14(3):887 – 906, 2019.   
[53] Lizhen Lin, Vinayak Rao, and David Dunson. Bayesian nonparametric inference on the stiefel manifold. Statistica Sinica, pages 535–553, 2017.   
[54] L. Lovász and M. Simonovits. Random walks in a convex body and an improved volume algorithm. Random Structures & Algorithms, 4(4):359–412, 1993.   
[55] Kai Mao, Feng Liang, and Sayan Mukherjee. Supervised dimension reduction using bayesian mixture modeling. In Proceedings of the thirteenth international conference on artificial intelligence and statistics, pages 501–508. JMLR Workshop and Conference Proceedings, 2010.   
[56] Ivan Markovsky. Low rank approximation: algorithms, implementation, applications, volume 906. Springer, 2012.   
[57] James Martens. New insights and perspectives on the natural gradient method. The Journal of Machine Learning Research, 21(1):5776–5851, 2020.   
[58] Ross McVinish and Kerrie Mengersen. Semiparametric bayesian circular statistics. Computational statistics & data analysis, 52(10):4722–4730, 2008.   
[59] Arya A Pourzanjani, Richard M Jiang, Brian Mitchell, Paul J Atzberger, and Linda R Petzold. Bayesian inference over the stiefel manifold via the givens representation, 2017.   
[60] Martin Raič. A multivariate Berry–Esseen theorem with explicit constants. Bernoulli, 25(4A):2824–2853, Nov 2019.   
[61] Palanikumar Ravindran and Sujit K Ghosh. Bayesian analysis of circular data using wrapped distributions. Journal of Statistical Theory and Practice, 5(4):547–561, 2011.   
[62] Gregory C Reinsel, Raja P Velu, and Kun Chen. Multivariate Reduced-Rank Regression: Theory, Methods and Applications, volume 225. Springer Nature, 2023.   
[63] Susanne M Schennach. Bayesian exponentially tilted empirical likelihood. Biometrika, 92(1):31–46, 2005.   
[64] Igor Silin and Vladimir Spokoiny. Bayesian inference for spectral projectors of the covariance matrix. Electronic Journal of Statistics, 12(1):1948 – 1987, 2018.   
[65] Taiji Suzuki and Masashi Sugiyama. Sufficient dimension reduction via squared-loss mutual information estimation. In Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics, volume 9, pages 804–811, Chia Laguna Resort, Sardinia, Italy, 13–15 May 2010. PMLR.   
[66] Nicholas Syring and Ryan Martin. Calibrating general posterior credible regions. Biometrika, 106(2):479–486, Dec 2018.   
[67] Rong Tang and Yun Yang. Bayesian inference for risk minimization via exponentially tilted empirical likelihood. Journal of the Royal Statistical Society. Series B: Statistical Methodology, 2022.   
[68] Rong Tang and Yun Yang. Supplement to “minimax rate of distribution estimation on unknown submanifolds under adversarial losses”. 2023.   
[69] Rong Tang and Yun Yang. On the computational complexity of metropolis-adjusted langevin algorithms for bayesian posterior sampling. Journal of Machine Learning Research, 25(157):1–79, 2024.   
[70] Brian St Thomas, Kisung You, Lizhen Lin, Lek-Heng Lim, and Sayan Mukherjee. Learning subspaces of different dimensions. Journal of Computational and Graphical Statistics, 31(2):337–350, 2022.   
[71] Roman Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2018.   
[72] Martin J. Wainwright. High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2019.   
[73] Andrew T.A Wood. Simulation of the von mises fisher distribution. Communications in Statistics - Simulation and Computation, 23(1):157–164, 1994.   
[74] Keru Wu, Scott Schmidler, and Yuansi Chen. Minimax mixing time of the metropolisadjusted langevin algorithm for log-concave sampling, 2021.   
[75] Yun Yang and David B. Dunson. Bayesian manifold regression. The Annals of Statistics, 44(2):876 – 905, 2016.   
[76] Yunwen Yang and Xuming He. Bayesian empirical likelihood for quantile regression. The Annals of Statistics, 2012.   
[77] Guosheng Yin. Bayesian generalized method of moments. Bayesian Analysis, 2009.   
[78] Emilio Zappa, Miranda Holmes-Cerfon, and Jonathan Goodman. Monte carlo on manifolds: Sampling densities and integrating functions. Communications on Pure and Applied Mathematics, 71(12):2609–2647, 2018.   
[79] Jiayao Zhang, Guangxu Zhu, Robert W Heath Jr, and Kaibin Huang. Grassmannian learning: Embedding geometry awareness in shallow and deep learning. arXiv preprint arXiv:1808.02229, 2018.   
[80] Zhenyue Zhang and Lixin Wu. Optimal low-rank approximation to a correlation matrix. Linear algebra and its applications, 364:161–187, 2003.   
[81] Bingxin Zhou, Junbin Gao, Minh-Ngoc Tran, and Richard Gerlach. Manifold optimizationassisted gaussian variational approximation. Journal of Computational and Graphical Statistics, 30(4):946–957, 2021.   
[82] Guifang Zhou. Rank-constrained optimization: A Riemannian manifold approach. PhD thesis, The Florida State University, 2015.

# Appendix

Notations: We adopt the notations in the manuscript, and further introduce the following additional notations for technical proofs. For any function $f : \mathcal { X } \times \mathbb { R } ^ { d } \to \mathbb { R }$ , we use $\nabla _ { y } f ( x , y )$ to denote the gradient vector of $f ( x , y )$ with respect to $y$ for $x \in \mathcal { X }$ and $\boldsymbol { y } \in \mathbb { R } ^ { d }$ . For any function $f : \mathbb { R } ^ { d }  \mathbb { R } ^ { k }$ , we use $\mathbf { J } _ { f } ( y )$ to denote the $k \times d$ Jacobian matrix of $f$ at $y$ , i.e., $\begin{array} { r } { \mathbf { J } _ { f } ( y ) _ { i j } = \frac { \partial f _ { i } ( y ) } { \partial y _ { j } } } \end{array}$ with $f ( \cdot ) = ( f _ { 1 } ( \cdot ) , f _ { 2 } ( \cdot ) , \cdot \cdot \cdot , f _ { k } ( \cdot ) )$ . We use $\mathbf { 1 } _ { A } ( x )$ to denote the indicator function of a set $A$ so that $\mathbf { 1 } _ { A } ( x ) = 1$ if $x \in A$ and zero otherwise. We use $\chi _ { \alpha } ^ { 2 } ( d )$ to denote the $\alpha$ -th quantile of $\chi ^ { 2 }$ distribution with $d$ degrees of freedom. For a probability measure $\mu$ and measurable set $A$ , the (unnormalized) restriction of to $A$ is defined by $\mu | _ { A } ( B ) = \mu ( B \cap A )$ for any measurable set $B$ , and the normalized restriction of $\mu$ to $A$ is defined by $\begin{array} { r } { \mu | _ { A } ( B ) = \frac { \mu ( B \cap A ) } { \mu ( A ) } } \end{array}$ . When no ambiguity may arise, we will use the same symbol $\mu ^ { * } ( \cdot )$ to denote the density function of the probability measure $\mu ^ { * }$ . If $X$ is an random variable with law $\mu$ , we write $P ( X \in A ) = \mu ( A )$ to denote the probability of $A$ under $\mu$ . For any two positive integers $D , d$ with $D \geq d$ , we use $\mathbb { O } ( D , d )$ to denote the set of all orthogonal $d$ -frames in $\mathbb { R } ^ { D }$ , i.e., $\mathbb { O } ( D , d ) = \{ U \in \mathbb { R } ^ { D \times d } : U ^ { T } U = I _ { d } \}$ , and when $D = d$ , we write $\mathbb { O } ( d ) = \mathbb { O } ( d , d )$ . We use the notation $\Vert \cdot \Vert _ { \mathrm { F } }$ and $\| \cdot \| _ { \mathrm { o p } }$ to denote the matrix Frobenius norm and operator norm respectively. We use $\mathbb { S } _ { 1 } ^ { d }$ to denote the $d$ -dimensional $1 -$ sphere, i.e., $\mathbb { S } _ { 1 } ^ { d } = \{ \lambda \in \mathbb { R } ^ { d + 1 } : \| \lambda \| = 1 \}$ . For two numbers $a , b$ , we denote $a \vee b = \operatorname* { m a x } ( a , b )$ . The symbols $\lesssim$ and $\gtrsim$ mean the corresponding inequality up to an $n$ -independent constant. We write $A = B + O ( a _ { n } )$ if $| A - B | \lesssim a _ { n }$ . Throughout, $C$ , $c$ , $C _ { 0 }$ , $c _ { 0 }$ , $C _ { 1 }$ , $c _ { 1 }$ , $C _ { 2 }$ , $c _ { 2 } , . \ .$ are generically used to denote positive constants whose values might change from one line to another, but are independent from everything else.

# A Notions in Riemannian Submanifold

This subsection provides an introduction to Riemannian submanifolds and their relevance in optimization problems for determining the parameter of interest $\theta ^ { * }$ . We draw upon the works of [16, 49] for this purpose. Understanding optimization tools for Riemannian submanifolds is crucial for constructing appropriate posterior distributions for Bayesian inference and for efficient sampling. We begin with a review of first-order embedded geometry and present a popular first-order optimization algorithm for Riemannian submanifolds. Subsequently, we delve into second-order embedded geometry and discuss second-order optimization algorithms.

1. Definition of manifold. We first recall the definition of manifold.

Definition 3 (Submanifold). A subset $\mathcal { M }$ of $\mathbb { R } ^ { D }$ is a $d$ -dimensional Riemannian submanifold if for every point $\theta$ in $\mathcal { M }$ , there exists a neighbourhood $U _ { \theta }$ of $\theta$ on $\mathcal { M }$ and an open set $V _ { \theta } \subseteq \mathbb { R } ^ { d }$ , such that that there exists a homeomorphism $\xi _ { \theta }$ that maps $V _ { \theta }$ to $U _ { \theta }$ , that is, $\xi _ { \theta } : V _ { \theta } \to U _ { \theta }$ is bijective and both $\xi _ { \theta }$ and $\xi _ { \theta } ^ { - 1 }$ are continuous maps. Moreover, the differential $\mathcal { D } \xi _ { \theta } ( z ) [ \cdot ]$ of $\xi _ { \theta } ( \cdot )$ at $z$ exists and is injective for every $z \in V _ { \theta }$ . The pair $( U _ { \theta } , \xi _ { \theta } ^ { - 1 } )$ is called a local coordinate chart near $\theta$ , with $\xi _ { \theta } ^ { - 1 }$ the coordinate map and $\xi _ { \theta }$ a local parameterization. We refer to $D$ as the ambient dimension and $d$ as the intrinsic dimension of $\mathcal { M }$ .

Next, we define the atlas.

Definition 4 (Atlas). A collection of $d$ -dimensional charts $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ is called an atlas on $\mathcal { M }$ if 1. $\begin{array} { r } { \mathcal { M } = \bigcup _ { \lambda \in \Lambda } U _ { \lambda } } \end{array}$ . 2. Each chart $( U _ { \lambda } , \varphi _ { \lambda } )$ in atlas $\mathcal { A }$ consists of a homeomorphism $\varphi _ { \lambda } : U _ { \lambda } \to \widetilde { U } _ { \lambda }$ , from an open set $U _ { \lambda } \subset \mathcal { M }$ to an open set $\widetilde { U } _ { \lambda } \subset \mathbb { R } ^ { d }$ . 3. Any two charts $( U , \varphi )$ and $( V , \psi )$ in atlas $\mathcal { A }$ are compatible, meaning that the transition map $\varphi \circ \psi ^ { - 1 } : \psi ( U \cap V ) \to \varphi ( U \cap V )$ is a diffeomorphism.

A function $f : M \to \mathbb { R }$ is called $C ^ { k }$ -smooth if there exists an open neighborhood $U \subset \mathbb { R } ^ { D }$ of $M$ and a function ${ \overline { { f } } } : U \to \mathbb { R }$ such that $f = { \overline { { f } } } | _ { M }$ and $\overline { { f } }$ has continuous partial derivatives up to order $k$ on $U$ .

2. First-order embedded geometry. We start by introducing the following concepts of the tangent bundle and the differential of a smooth map, which enable us to define gradients on submanifolds.

Definition 5. (Tangent bundle) For a submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ , we denote the tangent space of $\mathcal { M }$ at $\theta$ as $T _ { \theta } { \mathcal { M } } = \{ c ^ { \prime } ( 0 ) | c : I \to { \mathcal { M } }$ is differentiable and $c ( 0 ) = \theta \}$ , where $I$ is any open interval containing $t = 0$ ; we use $T \mathcal M = \{ ( \theta , v ) : \theta \in \mathcal M , v \in T _ { \theta } \mathcal M \}$ to denote the tangent bundle of $\mathcal { M }$ .

Definition 6. (Differential of a smooth map) The differential $f : { \mathcal { M } } \to { \mathcal { M } } ^ { \prime }$ at $\theta$ is a linear operator ${ \mathcal { D } } f ( \theta ) : T _ { \theta } { \mathcal { M } } \to T _ { f ( \theta ) } { \mathcal { M } } ^ { \prime }$ defined by

$$
{ \mathcal { D } } f ( \theta ) [ v ] = { \frac { \mathrm { d } } { \mathrm { d } t } } f ( c ( t ) ) { \big | } _ { t = 0 } ,
$$

where c is a differentiable curve on $\mathcal { M }$ passing through $\theta$ at $t = 0$ with velocity $c ^ { \prime } ( 0 ) = v$

Now, we are prepared to define the Riemannian gradient of a smooth function on a submanifold.

Definition 7. (Riemannian gradient/natural gradient) Let $f : \mathcal { M }  \mathbb { R }$ be a $C ^ { 1 }$ -smooth function on a Riemannian submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ . The Riemannian gradient grad $f$ of $f$ is the vector field on $\mathcal { M }$ (i.e., an assignment of a tangent vector to each point in $\mathcal { M }$ ) uniquely defined by the following identities:

$$
\forall ( \theta , v ) \in T { \mathcal { M } } : \quad { \mathcal { D } } f ( \theta ) [ v ] = \langle v , \operatorname { g r a d } f ( \theta ) \rangle _ { \theta } ,
$$

where $\langle \cdot , \cdot \rangle _ { \theta } : T _ { \theta } { \mathcal { M } } \times T _ { \theta } { \mathcal { M } } \to { \mathbb { R } }$ is the Riemannian metric defined by the restriction of the $D$ -dimensional Euclidean inner product on $T _ { \theta } { \mathcal { M } } \times T _ { \theta } { \mathcal { M } }$ .

If we consider any $C ^ { 1 }$ -smooth extension $\overline { { f } }$ of $f$ to a neighborhood of $\mathcal { M }$ in $\mathbb { R } ^ { D }$ , the Riemannian gradient of $f$ is given by

$$
\operatorname { g r a d } f ( \theta ) = \operatorname { P r o j } _ { T _ { \theta } \mathcal { M } } ( \nabla \overline { { f } } ( \theta ) ) ,
$$

where ProjT M(v) = arg min∥v′ − v∥ denote the projection of $v$ onto $T _ { \theta } \mathcal { M }$

3. First-order algorithm for optimization on a Riemannian submanifold. Consider a generic optimization problem

$$
\operatorname* { m i n } _ { \theta \in \mathcal { M } } f ( \theta ) ,
$$

where $\mathcal { M }$ is a Riemannian submanifold embedded in $\mathbb { R } ^ { D }$ , and $f$ is a smooth function called the objective function. Optimizaing $f$ over $\mathcal { M }$ can be viewed as a “constrained” optimization problem, where $\theta$ is not allowed to move freely in the ambient space $\mathbb { R } ^ { D }$ , but instead must remain on $\mathcal { M }$ . To generalize unconstrained optimization algorithms such as gradient descent, one can utilize the following first-order necessary optimality condition for identifying a local minimizer of $f$ on $\mathcal { M }$ :

Proposition 1. (Propositions 4.5 and 4. $\it 6$ of [15] ) Any local minimizer $\theta$ of a smooth function $f : \mathcal { M }  \mathbb { R }$ satisfies grad $f ( \theta ) = 0$ .

The first-order optimality condition outlined in Proposition 1 enables us to convert the problem of identifying a (local) optimizer for $f$ into the task of solving a system of (first-order) equations. Therefore, one can apply the Riemannian gradient descent method (RGD) to solve problem (8). The Riemannian gradient determines the direction of movement in each iteration, and a retraction is used to ensure that the point stays on the manifold. The retraction allows us to move away from a point $\theta \in \mathcal { M }$ along the direction $v \in T _ { \theta } { \mathcal { M } }$ while remaining on the manifold, which is the basic operation of essentially all optimization algorithms on manifolds. The retraction is formally defined as follows.

Definition 8. (Retraction) $A$ retraction on a manifold $\mathcal { M }$ is a map:

$$
\mathrm { R } : T \mathcal { M } \to \mathcal { M } : ( \theta , v ) \longmapsto \mathrm { R } _ { \theta } ( v )
$$

such that each curve $c ( t ) = \operatorname { R } _ { \theta } ( t v )$ satisfies $c ( 0 ) = \theta$ and $c ^ { \prime } ( 0 ) = v$ ; and if in addition $c ^ { \prime \prime } ( 0 ) = 0$ for each curve $c$ , then $\mathrm { R }$ is called a second-order retraction on $\mathcal { M }$ .

Given a retraction $\mathrm { R } _ { \theta } ( v )$ , the RGD algorithm is as follows: select an initial point $\theta _ { 0 } \in \mathcal { M }$ , choose step sizes $\alpha _ { k } > 0$ , and iterate

$$
\theta _ { k + 1 } = \mathrm { R } _ { \theta _ { k } } \bigl ( - \alpha _ { k } \mathrm { g r a d } f ( \theta _ { k } ) \bigr ) \quad k = 0 , 1 , 2 , \cdot \cdot \cdot
$$

4. Second-order embedded geometry. Based on the notion of Riemannian gradient for smooth functions on submanifolds, we can consider the following concept of Riemannian Hessian.

Definition 9. Let $\mathcal { M }$ be a Riemannian submanifold embedded in $\mathbb { R } ^ { D }$ . The Riemannian Hessian of a function $f : \mathcal { M }  \mathbb { R }$ at point $\theta \in \mathcal { M }$ is the linear map $\operatorname { H e s s } f ( \theta ) : T _ { \theta } { \mathcal { M } } \to T _ { \theta } { \mathcal { M } }$ defined as follows [15]:

$$
\mathrm { H e s s } f ( \theta ) [ u ] = \mathrm { P r o j } _ { { \cal T } _ { \theta } \mathcal { M } } \Big ( \operatorname* { l i m } _ { t  0 } \frac { \mathrm { g r a d } f ( c ( t ) ) - \mathrm { g r a d } f ( c ( 0 ) ) } { t } \Big ) ,
$$

where c is a differentiable curve on $\mathcal { M }$ so that $c ( 0 ) = \theta$ and $c ^ { \prime } ( 0 ) = u$ .

Let $\overline { G }$ be a $C ^ { 1 }$ -smooth extension of grad $f$ defined on a neighborhood of $\mathcal { M }$ in $\mathbb { R } ^ { D }$ , then we have

$$
{ \mathrm { H e s s } } f ( \theta ) [ u ] = { \mathrm { P r o j } } _ { T _ { \theta } { \mathcal { M } } } ( { \mathcal { D } } { \overline { { G } } } ( \theta ) [ u ] ) .
$$

The following proposition states the second-order necessary optimality condition for identifying local minimizer of $f$ on $\mathcal { M }$ .

Proposition 2. (Propositions 6.2 and 6.3 of [15] ) Any local minimizer $\theta$ of a smooth function $f : \mathcal { M }  \mathbb { R }$ satisfies grad $f ( \theta ) = 0$ and ${ \mathrm { H e s s } } f ( \theta ) \succcurlyeq 0$ . 6

We can consider second-order optimization algorithms based on the second-order necessary optimality condition described in Proposition 2. The most popular one is the Riemannian Newton’s method where the Riemannian Hessian and Riemannian gradient are used to decide the moving direction. Given a second-order retraction $\mathrm { R }$ on manifold, the Riemannian Newton’s algorithm is given by: select initial point $\theta _ { 0 } \in \mathcal { M }$ , for $k = 0 , 1 , 2 , \cdots$ , iterate

$$
\begin{array} { r l r } { \mathrm { s o l v e } } & { { \mathrm { H e s s } } f ( \theta _ { k } ) [ s _ { k } ] = - \mathrm { g r a d } f ( \theta _ { k } ) } & { \mathrm { f o r } \quad s _ { k } \in T _ { \theta _ { k } } { \mathcal { M } } ; } \\ & { \theta _ { k + 1 } = { \mathrm { R } } _ { \theta _ { k } } ( s _ { k } ) . } \end{array}
$$

5. Riemannian volume measure. The Riemannian volume measure is a commonly-used base measure for defining density function on a Riemannian submanifold. Consider a $d$ -dimensional Riemannian submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ , and with atlas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ . We first consider the following mathematical technique of partition of unity, so that one can glue constructions in the local charts to form a global construction on the manifold.

Definition 10. (partition of unity) $A$ partition of unity subordinate to altas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ is a collection of functions $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ on $\mathcal { M }$ so that

1. $0 \le \rho _ { \lambda } \le 1$ for all $\lambda \in \Lambda$ , and $\begin{array} { r } { \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( x ) = 1 } \end{array}$ for all $x \in \mathcal { M }$ .

2. $\operatorname { s u p p } ( \rho _ { \lambda } ) \subset U _ { \lambda }$ for any $\lambda \in \Lambda$ .

3. Each point $x \in \mathcal { M }$ has a neighborhood which intersects $\operatorname { s u p p } ( \rho _ { \lambda } )$ for only finitely many $\lambda \in \Lambda$ .

Then given a partition of unity $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ subordinate to altas $\mathcal { A }$ , the Riemannian volume measure $\mu _ { \mathcal { M } }$ is defined as

$$
\mathrm { d } \mu _ { \mathcal { M } } = \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \sqrt { \operatorname* { d e t } ( J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ^ { T } J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ) } \mathrm { d } z .
$$

A measure $\mu$ on $\mathcal { M }$ is said to have a density $f$ (with respect to the volume measure $\mu _ { \mathcal { M } }$ ) if for any measurable subset $A \subset { \mathcal { M } }$ ,

$$
\mu ( A ) = \int _ { A } f \mathrm { d } \mu _ { \mathcal { M } } = \sum _ { \lambda \in \Lambda } \int _ { \varphi _ { \lambda } ( U _ { \lambda } \cap A ) } \rho _ { \lambda } ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \cdot f ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \sqrt { \operatorname* { d e t } ( J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ^ { T } J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ) } \mathrm { d } z .
$$

# B Mixing time analysis

The goal of this section is to characterize the computational complexity of the RRWM algorithm for sampling from a Bayesian posterior $\mu ^ { * }$ defined on a submanifold $\mathcal { M }$ . We impose a condition on the target distribution $\mu ^ { * }$ that requires the existence of a point $\widetilde { \theta } \in { \mathcal { M } }$ so that $\psi _ { \widetilde { \theta } \# } \mu ^ { * }$ is uniformly close to a zero-centered multivariate normal distribution in a high probability set of $\mu ^ { * }$ . This is formalized as the following Assumptions.

Assumption B.1 (Conditions for the retraction at $\theta$ ): There exist positive constants $r$ , $L$ so that the retraction $\widetilde { \phi } _ { \theta } : \widetilde { V } _ { \theta } \to \widetilde { U } _ { \theta }$ , and its inverse $\widetilde { \psi } _ { \theta } : \widetilde { U } _ { \theta } \to \widetilde { V } _ { \theta }$ satisfies that:

1. $B _ { r } ( \theta ) \cap \mathcal { M } \subset \widetilde { U } _ { \theta }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta } { \mathcal { M } } \subset { \widetilde { V } } _ { \theta }$ ;   
2 $\cdot \operatorname* { s u p } _ { \theta ^ { \prime } \in B _ { r } ( \theta ) \cap M } \frac { \| \widetilde { \psi } _ { \theta } ( \theta ^ { \prime } ) - ( \theta ^ { \prime } - \theta ) \| _ { 2 } } { \| \theta ^ { \prime } - \theta \| _ { 2 } ^ { 2 } } \leq L \mathrm { ~ a n d ~ } \operatorname* { s u p } _ { v \in B _ { r } ( 0 _ { D } ) \cap T _ { \theta } \mathcal { M } } \frac { \| \widetilde { \phi } _ { \theta } ( v ) - ( v + \theta ) \| _ { 2 } } { \| v \| _ { 2 } ^ { 2 } } \leq L ;$

3. for any $v , v ^ { \prime } \in B _ { r } ( \mathbf { 0 } _ { D } ) \cap T _ { \theta } \mathcal { M }$ and any unit vector $\eta \in T _ { \theta } \mathcal { M }$ , $\| \widetilde { \cal D } \widetilde { \phi } _ { \theta } ( v ) [ \eta ] - \widetilde { \cal D } \widetilde { \phi } _ { \theta } ( v ^ { \prime } ) [ \eta ] \| _ { 2 } \leq$ $L \| v - v ^ { \prime } \| _ { 2 }$ .

Assumption B.1 requires that the retraction employed in RRWM algorithm is at least $C ^ { 2 }$ - smooth. For a submanifold that is locally $C ^ { 3 }$ -smooth around $\theta$ , there are multiple viable choices for the retraction that meets Assumption B.1. For instance, a special choice of $\tilde { \psi } _ { \boldsymbol { \theta } } ( \cdot )$ is the projection map $\psi _ { \boldsymbol \theta } ( \cdot ) = \mathrm { P r o j } _ { T _ { \boldsymbol \theta } \mathcal { M } } ( \cdot - \boldsymbol \theta )$ , which has been applied in [78] for sampling from a solution manifold. Additionally, the exponential map and logarithmic map pair serves as another example, which is utilized in [18] to develop Hamiltonian Monte Carlo algorithm on a general Riemannian submanifold.

Assumption B.2 (Conditions for the target distribution $\mu ^ { * }$ and hyperparameters in the RRWM algorithm): There exist a reference point $\widetilde { \theta } \in { \mathcal { M } }$ , a matrix $W _ { \widetilde { \theta } } \in \ R ^ { D \times d }$ whose columns form an orthonormal basis for $T _ { \widetilde { \theta } } { \mathcal { M } }$ , positive numbers $\varepsilon , \varepsilon _ { 1 } , M _ { 0 } , n , \rho _ { 1 } , \rho _ { 2 } , R , h$ and covariance matrices $\boldsymbol { \widetilde { I } } \in \mathbb { R } ^ { D \times D }$ and $J \in \mathbb { R } ^ { d \times d }$ e, so that

$$
\begin{array} { r l } & { K _ { \theta } = \{ x = \widetilde { \phi } _ { \widetilde { \theta } } ( W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } ) : z \in K \} \mathrm { w i t h } K = \{ z \in \mathbb { R } ^ { d } : \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R \} } \\ & { \mathrm { w e l l - d e f i n e d , t h a t i s , } \{ v = W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } : z \in K \} \subset { \widetilde { V } } _ { \widetilde { \theta } } ; } \end{array}
$$

2. Let $\mu ^ { * } | _ { K _ { \theta } }$ be the normalized restriction of $\mu ^ { * }$ to $K _ { \theta }$ , and define the push-forward measure $\mu _ { \mathrm { l o c } } ^ { * } = \big [ \sqrt { n } \cdot W _ { \widetilde { \theta } } ^ { T } \widetilde { \psi } _ { \widetilde { \theta } } ( \cdot ) \big ] _ { \# } ( \mu ^ { * } | _ { K _ { \theta } } )$ , then $\mu _ { \mathrm { l o c } } ^ { \ast }$ is absolute continuous with respect to the Lebesgue measure on $\mathbb { R } ^ { d }$ . Denote its density by the same symbol $\mu _ { \mathrm { l o c } } ^ { * } ( \cdot )$ , then for any $\xi \in K$ ,

$$
\Big | \log \big ( \mu _ { \mathrm { l o c } } ^ { * } ( \boldsymbol { \xi } ) \big ) - \log \Big ( \big ( 2 \pi \mathrm { d e t } ( J ^ { - 1 } ) \big ) ^ { - \frac { d } 2 } \exp ( - \frac 1 2 \boldsymbol { \xi } ^ { T } J \boldsymbol { \xi } ) \Big ) \Big | \le \varepsilon _ { 1 } ;
$$

3. $J ^ { \Delta } = ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { \frac { 1 } { 2 } } J ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { \frac { 1 } { 2 } }$ satisfies $\rho _ { 1 } I _ { d } \precsim J ^ { \Delta } \preccurlyeq \rho _ { 2 } I _ { d }$

$$
\begin{array} { r } { \mu ^ { * } \big ( \{ x = \widetilde { \phi } _ { \widetilde { \theta } } \big ( W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } \big ) : \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R / 2 \} \big ) \geq 1 - \exp ( - 5 \varepsilon _ { 1 } ) \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } . } \end{array}
$$

Assumption B.2 is motivated by the manifold BvM theorem. The first two conditions in Assumption B.2 requires that the target distribution $\mu ^ { * }$ , when constrained on a neighborhood $K _ { \theta }$ around $ { \hat { \theta } }$ , can be approximated by a Gaussian distribution in the local coordinate system characterized by $\stackrel { \sim } { \psi } _ { \widetilde { \theta } }$ . It is noteworthy that we do not impose any smoothness or convexity constraints on the density of $\mu ^ { * }$ with respect to the volume measure of $\mathcal { M }$ , and the deviation characteristic $\varepsilon _ { 1 }$ can take any value. The third condition requires the asymptotic covariance matrix $J$ , after rescaling by the preconditioning matrix $\ddot { I }$ , to have its maximum eigenvalue upper-bounded by $\rho _ { 2 }$ and its minimum eigenvalue lower-bounded by $\rho _ { 1 }$ . The condition number $\begin{array} { r } { \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } } \end{array}$ serves as an indicator of how well the preconditioning matrix $\hat { I }$ is chosen to alleviate issues arising from the anisotropy of the target distribution. The last condition requires that $\mu ^ { * }$ should be concentrated around $ { \widetilde { \theta } }$ , which ensures that the Markov chain has a low probability of getting stuck in regions far away from $\widetilde { \theta }$ and shape constraints on $\mu ^ { * } | _ { K _ { \theta } }$ are sufficient to guarantee fast mixing of the chain.

Theorem 3. (Mixing time for sampling from Bayesian posteriors satisfying Bernstein-von Mises results in local coordinates) Let $\mu ^ { * }$ be the target distribution on a submanifold $\mathcal { M }$ . Suppose there exists a reference point $\widetilde { \theta } \in { \mathcal { M } }$ and a positive radius $r$ , so that Assumption B.1 holds uniformly for $\theta \in B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } }$ . Then there exist a small enough absolute $( n , d , D )$ -independent constant $c _ { 0 }$ and an $n$ -independent constant $C _ { 1 }$ so that if Assumption B.2 holds for reference point $\widetilde { \theta }$ , $a$ tolerance $\varepsilon \in ( 0 , 1 )$ , warming parameter $M _ { 0 }$ , sample size $n$ , preconditioning matrix $\tilde { I }$ , covariance matrix $J$ , eigenvalue constraints $\rho _ { 2 } \geq \rho _ { 1 } > 0$ , a rescaled step size $h$ that can be expressed as

$$
h = c _ { 0 } \rho _ { 2 } ^ { - 1 } \Big ( d + \log \big ( { \frac { M _ { 0 } d \kappa } { \varepsilon } } \big ) + \varepsilon _ { 1 } \Big ) ^ { - 1 } , \quad w h e r e \quad \kappa = { \frac { \rho _ { 2 } } { \rho _ { 1 } } } ,
$$

and radius $R$ satisfying $6 \sqrt { d / \rho _ { 1 } } \le R \le C _ { 1 } ( h \sqrt { n } ) ^ { \frac { 1 } { 3 } }$ . Then the $\zeta$ -lazy version of the RRWM Algorithm with an $M _ { 0 }$ -warm start $\mu _ { 0 }$ and step size $\begin{array} { r } { \widetilde { h } = \frac { h } { n } } \end{array}$ has an $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence bounded as

$$
\begin{array} { r l } & { \operatorname* { \bar { \rho } } _ { \operatorname* { m i n } } ( \varepsilon , \mu _ { 0 } ) } \\ & { \leq \frac { C _ { 2 } \exp \left( - 2 \varepsilon _ { 1 } \right) } { \zeta } \left\{ \left[ \exp ( - 3 \varepsilon _ { 1 } ) \cdot \kappa \cdot \left( d + \log \big ( \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) + \varepsilon _ { 1 } \right) \cdot \log \left( \frac { \log M _ { 0 } } { \varepsilon } \right) \right] \vee \log \left( M _ { 0 } \right) \right\} , } \end{array}
$$

where $C _ { 2 }$ is an $( n , d , D )$ -independent constant.

# C Detailed Algorithms

# C.1 Algorithm to compute the inverse of the projection map

In this subsection, we introduce algorithms to compute the local inverse $\phi _ { \theta } ( v )$ of the projection map $\phi _ { \theta } ( \theta ^ { \prime } ) = \mathrm { P r o j } _ { T _ { \theta } \mathcal { M } } ( \theta ^ { \prime } - \theta )$ . Notice that this specific choice of the retraction has the advantage of eliminating the Jacobian factor in the acceptance ratio. As a result, the acceptance ratio in the RRWM algorithm can be simplified to

$$
\mathcal { A } ( \theta ^ { k - 1 } , y ) = 1 \wedge \frac { \mu ^ { * } ( y ) \cdot \exp \big ( - v ^ { \prime T } ( P _ { y } \widetilde { I } P _ { y } ) ^ { \dagger } v ^ { \prime } / ( 4 \widetilde { h } ) \big ) } { \mu ^ { * } ( \theta ^ { k - 1 } ) \cdot \exp \big ( - v ^ { T } ( P _ { \theta ^ { k - 1 } } \widetilde { I } P _ { \theta ^ { k - 1 } } ) ^ { \dagger } v / ( 4 \widetilde { h } ) ) \big ) } .
$$

According to [78], if the manifold is a solution manifold $\mathcal { M } _ { \mathbf { q } } = \{ \theta \in \mathbb { R } ^ { D } : \mathbf { q } ( \theta ) = 0 \}$ for some smooth function $\mathbf { q }$ , then $y = \phi _ { \theta } ( v )$ can be found by numerically solving the equation

$$
y = \theta + v + Q _ { \theta } ^ { T } { a } \quad \mathrm { w h e r e } Q _ { \theta } = { \bf J _ { q } } ( \theta ) \mathrm { a n d } { \bf q } ( \theta + v + Q _ { \theta } ^ { T } { a } ) = 0 _ { k } ,
$$

by using the Newton-Raphson algorithm, where ${ \bf J _ { q } } ( \theta )$ to denote the $k \times D$ Jacobian matrix of $f$ at θ, i.e., -Jq(θ)ij $\begin{array} { r } { \left[ \mathbf { J _ { q } } ( \theta ) \right] _ { i j } = \frac { \partial q _ { i } ( \theta ) } { \partial \theta _ { j } } } \end{array}$ for $i \in [ k ]$ and $j \in [ D ]$ . The detailed algorithm is given as follows.

Algorithm 1: Finding $\phi _ { \theta } ( v )$ : Solution manifold   

<table><tr><td>MnBr(θ)={x ∈Br(0)|q(𝑥)=0}; Qθ ←Jq(0); repeat</td></tr><tr><td>Solve (Jq(θ+v+ Qea)TV-)△a = -q(θ+v+Qea) for △a;</td></tr><tr><td>a←a+△a; i←i+1;</td></tr><tr><td>until |q(θ+v+Qea)ll2≤εo or i&gt;nmax; ifi&gt;nmax or θ+v+Qea ≠M then</td></tr></table>

Here flag indicates whether the computation of $\phi _ { \theta } ( v )$ succeeds ( $\mathrm { H a g } = 1$ ) or fails $\mathrm { { f l a g } = 0 }$ ). However, this numerical scheme of computing $\phi _ { \theta } ( v )$ does not apply to a more general manifold where the function $\mathbf { q } ( \cdot )$ does not exist or is difficult to obtain. Instead, we propose a more general numerical scheme of computing $\phi _ { \theta } ( v )$ by solving the following optimization problem: given a tangent vector $v \in T _ { \theta } { \mathcal { M } }$ with a small enough norm $\lVert v \rVert$ , there exists $r > 0$ so that $y = \phi _ { \theta } ( v )$ can be identified as the unique solution of

$$
\underset { y \in \mathcal { M } \cap B _ { r } ( \theta ) } { \arg \operatorname* { m i n } } \left. \mathrm { P r o j } _ { T _ { \theta } \mathcal { M } } ( y - \theta ) - v \right. ^ { 2 } .
$$

The above optimization problem can be solved using the Riemannian gradient descent method or Riemannian Newton’s method, with the initial point set to $\theta$ . Implementing these methods requires retraction, which can also be used in the RRWM algorithm. However, unlike an arbitrary retraction, the inverse projection map eliminates Jacobian terms in the acceptance ratio, which is advantageous when second-order information for the retraction is hard to compute. The algorithms are detailed below.

Algorithm 2: Finding $\phi _ { \theta } ( v )$ : Given a retraction (first-order algorithm)   

<table><tr><td>Function project(M, 0, v): Initialization: y = 0, k = 0, flag = 1, step size {αk}keN, a retraction R on M; repeat G ← ProjTyM(ProjTθM(y -0) - U);</td></tr><tr><td>y ← Ry(-αk : G); k←k+1; until ||Gll2 ≤εo or k &gt; nmax; if k &gt; nmax or y M then</td></tr><tr><td>Function project(M, 0, v): Initialization: y = θ, k = O, fag = 1,a second order retraction R on M; repeat G ← ProjTyM(ProjTeM(y -0) - U);</td></tr><tr><td>Solve Hessf(y)[△y] = -G for △y ∈ TyM, where f : M →R is defined as f(y)= 1||ProjtoM(y-0)- vl|2; y ←Ry(△y); k←k+1; until |△yll2 ≤εo or k &gt;nmax; if k &gt;nmax or y Mthen flag←O; end return [y,flag];</td></tr></table>

# C.2 Algorithm for sampling from Bayesian RPETEL

We now detail the RRWM algorithm for sampling from the Bayesian RPETEL posterio $\Pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } )$ , defined as

$$
\pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } ) = \frac { \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) \Pi ( \mathrm { d } \theta ) } { \int _ { \mathcal { M } } \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) \Pi ( \mathrm { d } \theta ) } ,
$$

where $( p _ { 1 } ( \theta ) , p _ { 2 } ( \theta ) , \cdot \cdot \cdot , p _ { n } ( \theta ) )$ is the solution of

$$
\begin{array} { r l } & { \displaystyle \operatorname* { m a x } _ { ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ) } \sum _ { i = 1 } ^ { n } \big [ - w _ { i } \log ( n w _ { i } ) \big ] } \\ & { \mathrm { s u b j e c t ~ t o } \quad \displaystyle \sum _ { i = 1 } ^ { n } w _ { i } = 1 , \sum _ { i = 1 } ^ { n } w _ { i } \mathrm { g r a d } _ { \theta } , \ell ( X _ { i } , \theta ) = 0 _ { D } , \quad w _ { 1 } , w _ { 2 } , \ldots , w _ { n } \geq 0 . } \end{array}
$$

Since $\operatorname { g r a d } _ { \theta } \ell ( X , \theta ) \in T _ { \theta } \mathcal { M }$ , we can reformulate the constraints $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } \cdot \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) = 0 _ { D } } \end{array}$ by using a matrix $W _ { \theta } \in \mathbb { R } ^ { D \times d }$ , whose columns form a basis for $T _ { \theta } \mathcal { M }$ . This results in $\sum _ { i = 1 } ^ { n } w _ { i } \cdot$ $W _ { \theta } ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) = 0 _ { d }$ . By introducing Lagrange multipliers, we can rewrite the RETEL function $\scriptstyle \prod _ { i = 1 } ^ { n } p _ { i } ( \theta )$ as

$$
L ( X ^ { ( n ) } ; \theta ) = \prod _ { i = 1 } ^ { n } \frac { \exp \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) \right) } { \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) \right) } ,
$$

where λ(θ) = arg min Pni=1 exp  ξT W Tθ gradθ ℓ(Xi, θ). Note that the expression (11) is invariant ξ∈Rd   
to the choice of the basis $W _ { \theta }$ and is equivalent to

$$
L ( X ^ { ( n ) } ; \theta ) = \prod _ { i = 1 } ^ { n } \frac { \exp { \left( \overline { { \lambda } } ( \theta ) ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) \right) } } { \sum _ { i = 1 } ^ { n } \exp { \left( \overline { { \lambda } } ( \theta ) ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) \right) } } ,
$$

with $\begin{array} { r } { \overline { { \lambda } } ( \theta ) = \underset { \xi \in { T _ { \theta } } \mathcal { M } } { \arg \operatorname* { m i n } } \sum _ { i = 1 } ^ { n } \exp ( \xi ^ { T } \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) ) } \end{array}$ . Therefore, the computation of ETEL function can be simplified by solving an optimization problem on the manifold $T _ { \theta } \mathcal { M }$ , which can be performed using an adjusted Riemannian Newton’s algorithm outlined below.

Now we can state the RRWM algorithm for sampling from $\Pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } )$ .

$$
\begin{array} { r l } & { H \gets \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathrm { e x p } \left( \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) ^ { T } \overline { { \lambda } } ^ { k - 1 } \right) \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) ^ { T } ; } \\ & { G \gets \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathrm { e x p } \left( \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) ^ { T } \overline { { \lambda } } ^ { k - 1 } \right) \mathrm { g r a d } _ { \theta } \ell ( X _ { i } , \theta ) ; } \end{array}
$$

Algorithm 5: RRWM algorithm for sampling from Bayesian RPETEL posterior $\Pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } )$

<table><tr><td>Input: Number of iteration L, step size parameter h, covariance matrix I, initial distribution μ0; Data: X1, X2 ..,Xn;</td></tr><tr><td>Sampling 0° from μo; x0 = x(00,M,e); fort←0toL-1do Sample  from N(0,2hI) and let v = ProjTatM(u); [y,flag] ← project(M,0t,v);</td></tr><tr><td>if flag== O then 0t+1←0t；</td></tr><tr><td>else</td></tr><tr><td>U&#x27; ← ProjtyM(0t - y);</td></tr><tr><td>Generate a uniform random number u E (0,1); λ=λ(y,M,e)；</td></tr><tr><td>if</td></tr><tr><td>exp(xTgradg e(Xi,y)) π(y)exp anRn(y)) Eexp(xTgradge(x）） exp(-UT(PTIPy)tu&#x27;/(4h）） u&gt; π(0t)exp ∑110g exp((xO)Tgradg e(Xi,0t)) -anRn(0t)) exp(-uT(PiPot)t1/（4h)) ∑1exp(0）Tgrade(xi0t））</td></tr><tr><td></td></tr><tr><td>then θt+1←0t；</td></tr><tr><td>else [a,fag] ← project(M,y,u&#x27;); if flag == O then</td></tr><tr><td>θt+1←θt； else</td></tr><tr><td>θt+1←y; x←入； end end</td></tr></table>

In the context of the Bayesian RPETEL posterior with a non-smooth loss function, the term ${ \mathrm { y r a d } } _ { \theta } \ell ( X , \theta )$ can be replaced with $g ( X , \theta ) \in T _ { \theta } { \mathcal { M } }$ that satisfies Assumption 4.

# C.3 Riemannian MALA algorithm

Let $\mu { \mathcal { M } }$ denote the volume measure of $\mathcal { M }$ . Consider a target distribution that has a density $\begin{array} { r } { \mu ^ { * } ( \theta ) = \frac { \exp ( - f ( \theta ) ) } { \int _ { \mathcal { M } } \exp ( - f ( \theta ) ) \mu _ { \mathcal { M } } ( \mathrm { d } \theta ) } } \end{array}$ with respect to $\mu _ { \mathcal { M } }$ , where $f ( \theta )$ is the potential of $\mu ^ { * }$ . The Riemannian Metropolis-adjusted Langevin algorithm (MALA) produces $\{ \theta ^ { k } \} _ { k \geq 0 }$ sequentially as follows: for $k = 0 , 1 , 2 , \cdots$ ,

1. (Initialization) If $k = 0$ , sample $\theta ^ { 0 }$ from $\mu _ { 0 }$ ;

2. (Proposal) If $k \geq 1$ ,

(a) (generate random vector in tangent space) sample $\widetilde { v }$ from $\mathcal { N } ( - \widetilde { h } \widetilde { I } \cdot \mathrm { g r a d } f ( \theta ^ { k - 1 } ) , 2 \widetilde { h } \widetilde { I } )$ and let $v = \mathrm { P r o j } _ { T _ { \theta k - 1 } \mathcal { M } } ( \widetilde { v } )$ ;   
(b) (reject proposal if $v$ escape from $\widetilde { V } _ { \theta ^ { k - 1 } }$ ) if $v \not \in \widetilde { V } _ { \theta ^ { k - 1 } }$ , then $\theta ^ { k } = \theta ^ { k - 1 }$ ;   
(c) (“project” back to manifold) set $y = \phi _ { \theta ^ { k - 1 } } ( v )$ ;

# 3. (Metropolis-Hasting rejection/correction)

(a) (reject proposal if $\theta ^ { k - 1 }$ escape from $\widetilde { U } _ { y }$ ) if $\theta ^ { k - 1 } \notin \widetilde { U } _ { y }$ , then $\theta ^ { k } = \theta ^ { k - 1 }$ ; (b) (set acceptance probability) let $v ^ { \prime } = \psi _ { y } ( \theta ^ { k - 1 } )$ , set acceptance probability $A ( \theta ^ { k - 1 } , y ) =$ $1 \wedge \alpha ( \theta ^ { k - 1 } , y )$ with acceptance ratio statistic

$$
\begin{array} { r l } & { \alpha ( \theta ^ { k - 1 } , y ) = \frac { \mu ^ { * } ( y ) \cdot \big ( \big | ( \mathcal { D } \phi _ { y } ( v ^ { \prime } ) [ P _ { y } ] ) ^ { T } \mathcal { D } \phi _ { y } ( v ^ { \prime } ) [ P _ { y } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } { \mu ^ { * } ( \theta ^ { k - 1 } ) \cdot \big ( \big | ( \mathcal { D } \phi _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] ) ^ { T } \mathcal { D } \phi _ { \theta ^ { k - 1 } } ( v ) [ P _ { \theta ^ { k - 1 } } ] \big | _ { + } \big ) ^ { - \frac { 1 } { 2 } } } } \\ & { \quad \cdot \frac { \exp \big ( - \big ( v ^ { \prime } + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( y ) \big ) ^ { T } ( P _ { y } \widetilde { I } P _ { y } ) ^ { \dagger } ( v ^ { \prime } + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( y ) ) / ( 4 \widetilde { h } ) \big ) } { \exp \big ( - \big ( v + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( \theta ^ { k - 1 } ) \big ) ^ { T } \big ( P _ { \theta ^ { k - 1 } } \widetilde { I } \widetilde { P } _ { \theta ^ { k - 1 } } \big ) ^ { \dagger } \big ( v + \widetilde { h } \widetilde { I } \mathrm { g r a d } f ( \theta ^ { k - 1 } ) \big ) / ( 4 \widetilde { h } ) \big ) \big ) } . } \end{array}
$$

(c) (accept/reject the proposal) flip a coin and accept $y$ with probability $A ( \theta ^ { k - 1 } , y )$ and set $\theta ^ { k } = y$ ; otherwise, set $\theta ^ { k } = \theta ^ { k - 1 }$ .

Then consider the Bayesian RPETEL posterior $\Pi _ { \mathrm { R P } } ( \mathrm { d } \theta | X ^ { ( n ) } )$ whose density with respect to the volume measure $\mu _ { \mathcal { M } }$ is given by

$$
\pi _ { \mathrm { R P } } ( \theta | X ^ { ( n ) } ) = \frac { \pi ( \theta ) \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } { \int \pi ( \theta ) \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) \mathrm { d } \mu \mathcal { M } } .
$$

The potential $f$ of $\Pi _ { \mathrm { R P } } ^ { ( n ) }$ is then given by

$$
f ( \theta ) = \alpha _ { n } \mathcal { R } _ { n } ( \theta ) - \sum _ { i = 1 } ^ { n } \log p _ { i } ( \theta ) - \log \pi ( \theta ) .
$$

We then have the following lemma about the Riemannian gradient of $f$ .

Lemma 1. Denote $g ( X , \theta ) = ( g _ { 1 } ( X , \theta ) , g _ { 2 } ( X , \theta ) , \cdots , g _ { D } ( X , \theta ) ) = \operatorname { g r a d } _ { \theta } \ell ( X , \theta )$ and gradθ $g ( X , \theta ) =$ [gradθ $g _ { 1 } ( X , \theta ) , \mathrm { g r a d } _ { \theta } g _ { 2 } ( X , \theta ) , \cdot \cdot \cdot , \mathrm { g r a d } _ { \theta } g _ { D } ( X , \theta ) ]$ for $\theta \in { \mathcal { M } }$ . The Riemannian gardient of $f$ given in (12) on $\mathcal { M }$ is

$$
\begin{array} { l } { \displaystyle \mathrm { r a d } f ( \theta ) = \frac { \alpha _ { n } } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \sum _ { i = 1 } ^ { n } g _ { \overline { { \lambda } } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) } \\ { \displaystyle \qquad - \sum _ { i = 1 } ^ { n } [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) + n \cdot \frac { \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) } { \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) } , } \end{array}
$$

where $\begin{array} { r } { \overline { { \lambda } } ( \theta ) = \arg \operatorname* { m i n } _ { \xi \in T _ { \theta } \mathcal { M } } \sum _ { i = 1 } ^ { n } \exp ( \xi ^ { T } g ( X _ { i } , \theta ) ) } \end{array}$ and

$$
\begin{array} { r l r } {  { g _ { \overline { { \lambda } } } ( \theta ) = - ( \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } ) ^ { + } } } \\ & { } & { \cdot ( \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ( I _ { D } + g ( X _ { i } , \theta ) \overline { { \lambda } } ( \theta ) ^ { T } ) [ \mathrm { g r a d } _ { \theta } g ( X , \theta ) ] ^ { T } ) , } \end{array}
$$

with $A ^ { + }$ being the Moore–Penrose inverse of $A$ .

# D Auxiliary and Supporting Lemmas

This appendix contains supporting lemmas used in the main proofs. We first show that local smoothness at $\theta ^ { * }$ implies local smoothness at any $\theta _ { 0 }$ sufficiently close to $\theta ^ { * }$ .

Lemma 2. Let $\mathcal { M }$ be a $d$ -dimensional Riemannian submanifold embedded in $\mathbb { R } ^ { D }$ . If $\mathcal { M }$ is locally $C _ { r , L } ^ { 3 }$ -smooth at $\theta ^ { * } \in { \mathcal { M } }$ , then there exist positive constants $r _ { 1 } , L _ { 1 }$ such that, for any $\theta _ { 0 } \in B _ { r / 2 } ( \theta ^ { * } ) \cap { \mathcal { M } }$ , the manifold $\mathcal { M }$ is locally $C _ { r _ { 1 } , L _ { 1 } } ^ { 3 }$ -smooth at $\theta _ { 0 }$ .

Next, we state a lemma used to prove the manifold Bernstein-von Mises results for all posteriors considered in the main text. Consider a prior measure $\Pi _ { \mathcal { M } }$ defined on $\mathcal { M }$ and a point $\theta ^ { * } \in \mathcal { M }$ so that the manifold $\mathcal { M }$ and the prior $\Pi _ { \mathcal { M } }$ satisfy Assumption 1 and 2 in the main text. Then since $\mathcal { M }$ is $C _ { r , L } ^ { 3 }$ -smooth at $\theta ^ { * }$ , there exists $U _ { \theta ^ { * } } , V _ { \theta ^ { * } }$ with $B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subseteq U _ { \theta ^ { * } } \subseteq \mathcal { M }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta ^ { * } } { \mathcal { M } } \subseteq V _ { \theta ^ { * } } \subset T _ { \theta ^ { * } } { \mathcal { M } }$ , so that $\psi _ { \theta ^ { * } } : U _ { \theta ^ { * } } \to V _ { \theta ^ { * } }$ defined by $\psi _ { \theta ^ { * } } ( x ) = \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( x - \theta ^ { * } )$ is a bijective, where the inverse, denoted by $\phi _ { \theta ^ { * } }$ is thrice Fréchet differentiable, and its Fréchet derivatives up to order three have operator norms uniformly bounded by $L$ . With this notation in place, we can derive the following lemma. We first state the required assumption on lowdimensional summaries of the parameter.

Assumption D (Conditions for function $f$ ): There exist some positive constants $( r , C , L , a , b )$ so that the function $f = ( f _ { 1 } , f _ { 2 } \cdot \cdot \cdot , f _ { p } ) : \mathcal { M } \to \mathbb { R } ^ { p }$ satisfies that (1) $) 1 \leq p \leq d$ ; (2) $\operatorname { s u p } _ { \theta \in { \mathcal { M } } } \lVert f ( \theta ) \rVert \leq$ $C$ ; (3) for any $j \in [ p ]$ , $f _ { j } ( \cdot )$ has $L$ -Lipschitz continuous Riemannian gradient on $B _ { r } ( \theta ^ { * } ) \cap { \mathcal { M } }$ ; (4) denote $J _ { f } = [ \mathrm { g r a d } f _ { 1 } ( \theta ^ { * } ) , \cdot \cdot \cdot , \mathrm { g r a d } f _ { p } ( \theta ^ { * } ) ] ^ { I }$ , it holds that $a ^ { 2 } I _ { p } \preccurlyeq J _ { f } J _ { f } ^ { T } \preccurlyeq b ^ { 2 } I _ { p }$ .

Lemma 3. Let $\mathcal { M }$ be a submanifold satisfies Assumption 1. Consider a prior $\Pi = \Pi _ { \mathcal { M } }$ satisfies Assumption 2, and a map $\mathcal { L } : \mathcal { X } ^ { n } \times \mathcal { M }  \mathbb { R }$ . For any $X ^ { ( n ) } = ( X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } ) \in \chi ^ { n }$ , define the measure

$$
\Pi ^ { ( n ) } ( \mathrm { d } \theta ) = \frac { \exp ( \mathcal { L } ( X ^ { ( n ) } , \theta ) ) \Pi _ { \mathcal { M } } ( \mathrm { d } \theta ) } { \int _ { \mathcal { M } } \exp ( \mathcal { L } ( X ^ { ( n ) } , \theta ) ) \Pi _ { \mathcal { M } } ( \mathrm { d } \theta ) } .
$$

Suppose there exist a set ${ \mathcal { A } } \in { \mathcal { X } } ^ { ( n ) }$ , a $D \times d$ matrix $W _ { \theta ^ { \ast } }$ whose columns form an orthonormalbasis of $T _ { \theta ^ { * } } { \mathcal { M } }$ , a map $\widehat { \theta } ^ { \circ } : { \mathcal { A } }  { \mathcal { M } }$ , a positive definite $d \times d$ matrix $\Sigma$ , and absolute constants $\delta , \delta _ { 1 } , c , \gamma _ { 2 } > 0$ , $\gamma _ { 1 } \in ( 0 , \frac { 1 } { 2 } ]$ , $\gamma _ { 0 } \geq 1$ and $c _ { 1 } \geq 2$ , such that, for any $X ^ { ( n ) } \in { \mathcal { A } }$ , writing ${ \widehat { \theta } } ^ { \diamond } = { \widehat { \theta } } ^ { \diamond } ( X ^ { ( n ) } )$ , the following hold:

$$
\begin{array} { r } { \| \widehat { \theta ^ { \diamond } } - \theta ^ { * } \| \leq c \sqrt { \frac { \log n } { n } } , \ \Pi ^ { ( n ) } ( \| \theta - \widehat { \theta ^ { \diamond } } \| \geq \delta ) \leq n ^ { - c _ { 1 } } \ a n d \ B _ { \delta } ( \widehat { \theta ^ { \diamond } } ) \cap \mathcal M \subseteq U _ { \theta ^ { * } } . } \end{array}
$$

2. For any $h \in B _ { \delta _ { 1 } ( \log n ) ^ { 3 / 2 } } ( 0 _ { d } )$ ,

$$
\begin{array} { r l } & { \bigg | \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h \bigg | } \\ & { \qquad \leq C \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } ( \| h \| ^ { \gamma _ { 2 } } + 1 ) . } \end{array}
$$

$\textit { h } \in \mathbb { R } ^ { d }$ $\| h \| \ge \delta _ { 1 } ( \log n ) ^ { 3 / 2 }$ $\frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) \in V _ { \theta ^ { * } }$ , it holds that $\begin{array} { r } { \log \mathcal { L } \big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta } ^ { \diamond } ) \big ) \big ) \leq - 2 c _ { 1 } d \log n } \end{array}$

Then there exist positive constants $C _ { 0 } , C _ { 1 } , C _ { 2 }$ so that for any $X ^ { ( n ) } \in { \mathcal { A } }$ ,

$$
\begin{array} { r } { \boldsymbol { \mathit { 1 } } . ~ \Pi ^ { ( n ) } ( \lVert \boldsymbol { \theta } - \widehat { \boldsymbol { \theta ^ { \circ } } } \rVert \geq C _ { 0 } \sqrt { \frac { \log n } { n } } ) \leq C _ { 1 } n ^ { - c _ { 1 } } , } \end{array}
$$

2. Consider the projection of the posterior mean to the manifold: $\widehat { \theta } _ { p } = \mathrm { a r g } \operatorname* { m i n } _ { y \in \mathcal { M } } \lVert y -$ $\mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \rVert ^ { 2 }$ , when $n$ is sufficiently large, $\widehat { \theta } _ { p }$ is uniquely defined and it holds that $\| \widehat { \theta } _ { p } - \widehat { \theta } ^ { \circ } \| \leq$ $C _ { 1 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } }$

3. for any $f : \mathcal { M } \to \mathbb { R } ^ { p }$ satisfying Assumption $D$ , it holds that

$$
\mathrm { T V } \Big ( f _ {  { \# } } \Pi ^ { ( n ) } ,  { \mathcal { N } } \big ( f (  { \widehat { \theta ^ { \circ } } } ) , n ^ { - 1 } J _ { f } W _ { \theta ^ { * } } \Sigma W _ { \theta ^ { * } } ^ { T } J _ { f } ^ { T } \big ) \Big ) \leq C _ { 2 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } .
$$

# D.1 Proof of Lemma 2

We will use the following lemma to show the desired result; its proof follows directly from the proof of the first statement of Lemma F.4 in [68].

Lemma 4. Let $\mathcal { M }$ be a $d$ -dimensional Riemannian submanifold embedded in $\mathbb { R } ^ { D }$ and let $\theta _ { 0 } \in \mathcal { M }$ . Suppose there exist positive constants $( r , L )$ , sets $U \subseteq { \mathcal { M } }$ and $\Upsilon \subseteq \mathbb { R } ^ { d }$ , and a map $\xi : U \to \Upsilon$ such that (1) $\mathcal { M } \cap B _ { r } ( \theta _ { 0 } ) \subseteq U$ and $B _ { r } ( \xi ( \theta _ { 0 } ) ) \subset \Upsilon$ ; (2) $\xi$ is a bijective, and its inverse $\xi ^ { - 1 }$ is three times differentiable, with all mixed partial derivatives up to order three are bounded in absolute values by $L$ ; (3) $\begin{array} { r } { \operatorname* { i n f } _ { z \in \Upsilon } \lambda _ { \operatorname* { m i n } } ( J _ { \xi _ { - 1 } } ( z ) ^ { T } J _ { \xi _ { - 1 } } ( z ) ) \geq 1 / L } \end{array}$ , where $\lambda _ { \mathrm { m i n } } ( \cdot )$ denotes the minimal such that eigenvalue and $\mathcal { M }$ is $J _ { \xi ^ { - 1 } }$ $\dot { C } _ { r _ { 1 } , L _ { 1 } } ^ { 3 }$ is the Jacobian matrix of -smooth around $\theta _ { 0 }$ . $\xi ^ { - 1 }$ . Then there exist positive constants $( r _ { 1 } , L _ { 1 } )$

So we only need to verify the three conditions in Lemma 4. Notice that since $\mathcal { M }$ is locally $C _ { \tau , r , L } ^ { 3 }$ -smooth around $\theta ^ { * } \in \mathcal { M }$ , there exists $U , V$ with $B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subseteq U \subseteq \mathcal { M }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta ^ { * } } { \mathcal { M } } \subseteq$ $V \subseteq T _ { \theta ^ { * } } { \mathcal { M } }$ , so that $\psi _ { \theta ^ { * } } : U \to V$ defined by $\psi _ { \theta ^ { * } } ( x ) = \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( x - \theta )$ is a bijective, where the inverse, denoted by $\phi _ { \theta ^ { * } }$ is thrice Fréchet differentiable, and its Fréchet derivatives up to order three have operator norms uniformly bounded by $L$ .

Then let $W _ { \theta ^ { * } } \in \mathbb { R } ^ { D \times d }$ be an arbitrary orthonormal basis of $T _ { \theta ^ { * } } { \mathcal { M } }$ . Define $\Upsilon = B _ { r } ( 0 _ { d } )$ and $U _ { 1 } = \{ x = \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) \ : \ z \in \Upsilon \}$ . Then notice that for any $x \in B _ { r } ( \theta ^ { * } ) \cap { \mathcal { M } }$ , it holds that $\| W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( x ) \| < r$ . We have $B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subseteq U _ { 1 }$ . Define

$$
\xi : U _ { 1 } \to \Upsilon , \xi ( \theta ) = W _ { \theta ^ { * } } ^ { T } ( \theta - \theta ^ { * } ) .
$$

Then $\xi$ is a bijective with inverse given by $\xi ^ { - 1 } ( z ) = \phi _ { \theta ^ { \ast } } ( W _ { \theta ^ { \ast } } z )$ . Moreover, $\xi ^ { - 1 }$ is three-times differentiable, and there exists a constant $L _ { 1 }$ so that all mixed partial derivatives up to order three are bounded in absolute values by $L _ { 1 }$ , this verifies the second condition in Lemma 4. Now using the fact that, for any $z \in \Upsilon = B _ { r } ( 0 _ { d } )$ , it holds that

$$
J _ { \xi ( \xi ^ { - 1 } ( \cdot ) ) } ( z ) = I _ { d } \Rightarrow W _ { \theta ^ { * } } ^ { T } J _ { \xi ^ { - 1 } } ( z ) = I _ { d } .
$$

Therefore,

$$
\operatorname* { i n f } _ { z \in \Upsilon } \lambda _ { \operatorname* { m i n } } ( J _ { \xi ^ { - 1 } } ( z ) ^ { T } J _ { \xi ^ { - 1 } } ( z ) ) \geq 1 ,
$$

this verifies the third condition in Lemma 4. Moreover, for any $\theta _ { 0 } \in B _ { r / 2 } ( \theta ^ { * } ) \cap { \mathcal { M } }$ , it holds that $\lVert \xi ( \theta _ { 0 } ) \rVert < r / 2$ and $B _ { r / 2 } ( \xi ( \theta _ { 0 } ) ) \subseteq B _ { r } ( 0 _ { d } ) = \Upsilon$ . Moreover, $B _ { r / 2 } ( \theta _ { 0 } ) \cap \mathcal { M } \subseteq B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subseteq U _ { 1 }$ . So the first condition in Lemma 4 is also verified, and this completes the proof.

# D.2 Proof of Lemma 3

By the thrice differentiablity of $\phi _ { \theta ^ { * } }$ , there exists a constant $C$ so that

$$
\operatorname* { s u p } _ { v \in V _ { \theta ^ { * } } } \frac { \lVert \phi _ { \theta ^ { * } } ( v ) - ( v + \theta ^ { * } ) \rVert } { \lVert v \rVert ^ { 2 } } \leq C ,
$$

and

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { \theta ^ { \prime } \in U _ { \theta ^ { * } } } \frac { \| \psi _ { \theta ^ { * } } ( \theta ^ { \prime } ) - ( \theta ^ { \prime } - \theta ^ { * } ) \| } { \| \theta ^ { * } - \theta ^ { \prime } \| ^ { 2 } } = \displaystyle \operatorname* { s u p } _ { \theta ^ { \prime } \in U _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } \left( \psi _ { \theta ^ { * } } \left( \theta ^ { \prime } \right) \right) - \left( \theta ^ { * } + \psi _ { \theta ^ { * } } \left( \theta ^ { \prime } \right) \right) \| } { \| \theta ^ { * } - \theta ^ { \prime } \| } } \\ & { \quad \quad \le \displaystyle \operatorname* { s u p } _ { v \in V _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } \left( v \right) - ( v + \theta ^ { * } ) \| } { \| v \| ^ { 2 } } \le C . } \end{array}
$$

Then let’s fix an $X ^ { ( n ) } \in { \mathcal { A } }$ and write ${ \widehat { \theta } } ^ { \diamond } = { \widehat { \theta } } ^ { \diamond } ( X ^ { ( n ) } )$ . Define $V _ { \theta ^ { * } } ^ { \diamond } = \{ W _ { \theta ^ { * } } ^ { T } ( y - \psi _ { \theta ^ { * } } ( \widehat { \theta } ^ { \diamond } ) ) : y \in V _ { \theta ^ { * } } \}$ , and the function $\psi ^ { \diamond } : \mathbb { R } ^ { D } \to \mathbb { R } ^ { d }$ by $\psi ^ { \diamond } ( \theta ) = W _ { \theta ^ { * } } ^ { T } ( \theta - \widehat { \theta ^ { \diamond } } )$ . Its restriction $\psi ^ { \diamond } | _ { U _ { \theta ^ { \ast } } } : U _ { \theta ^ { \ast } } \to V _ { \theta ^ { \ast } } ^ { \diamond }$ satisfies, for any $\theta \in U _ { \theta ^ { * } }$ , $\psi ^ { \diamondsuit } | _ { U _ { \theta ^ { \ast } } } ( \theta ) = \psi ^ { \diamondsuit } ( \theta ) = W _ { \theta ^ { \ast } } ^ { T } ( \psi _ { \theta ^ { \ast } } ( \theta ) - \psi _ { \theta ^ { \ast } } ( \theta ^ { \diamond } ) )$ . Then we define the function $\phi ^ { \circ } : V _ { \theta ^ { * } } ^ { \circ } \to U _ { \theta ^ { * } }$ by $\phi ^ { \circ } ( z ) = \phi _ { \theta ^ { \ast } } \bigl ( W _ { \theta ^ { \ast } } z + \psi _ { \theta ^ { \ast } } ( \widehat { \theta } ^ { \circ } ) \bigr )$ . It is straightforward to verify that $\phi ^ { \circ }$ is the inverse of $\psi ^ { \diamond } | _ { U _ { \theta ^ { * } } }$ , and $\phi ^ { \diamond }$ is thrice differentiable with $\mathbf { J } _ { \phi ^ { \circ } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) ) = W _ { \theta ^ { * } }$ .

Step 1. We will first show that

$$
\mathrm { T V } ( \psi _ { \# } ^ { \diamond } \Pi ^ { ( n ) } , \mathcal { N } ( 0 , n ^ { - 1 } \Sigma ) ) \lesssim \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } .
$$

Using the assumption that $\begin{array} { r } { \| \widehat { \theta ^ { \circ } } - \theta ^ { * } \| \leq c \sqrt { \frac { \log n } { n } } } \end{array}$ and $B _ { \delta } ( \widehat { \theta ^ { \circ } } ) \cap M \subseteq U _ { \theta ^ { * } }$ , there exist positive constants $C _ { 1 } , C _ { 2 }$ so that for any $\theta \in B _ { \delta } ( \widehat { \theta ^ { \circ } } ) \cap { \mathcal { M } }$ and $y = \psi ^ { \diamond } ( \theta )$ ,

$$
\begin{array} { r l } & { \Big | \Big | \Big | \mathbf { J } _ { \phi ^ { \diamond } } ( y ) - W _ { \theta ^ { \ast } } \Big | \Big | \Big | _ { \mathrm { o p } } = \Big | \Big | \Big | \mathbf { J } _ { \phi ^ { \diamond } } ( y ) - \mathbf { J } _ { \phi ^ { \diamond } } ( - W _ { \theta ^ { \ast } } ^ { T } \psi _ { \theta ^ { \diamond } } ( \widehat { \theta ^ { \diamond } } ) ) \Big | \Big | \Big | _ { \mathrm { o p } } \leq C _ { 1 } \| y + W _ { \theta ^ { \ast } } ^ { T } \psi _ { \theta ^ { \star } } ( \widehat { \theta ^ { \diamond } } ) \| , } \\ & { \mathcal { I } ^ { \diamond } ( y ) = \sqrt { \Big | \mathbf { J } _ { \phi ^ { \diamond } } ( y ) ^ { T } \mathbf { J } _ { \phi ^ { \diamond } } ( y ) \Big | } \leq C _ { 2 } . } \end{array}
$$

Moreover, when $n$ is large enough, there exist positive constants $r _ { 1 }$ so that for any $\theta \in B _ { r _ { 1 } } ( \theta ^ { * } ) \cap M$ and $y = \psi ^ { \diamond } ( \theta )$ ,

$$
\mathcal { T } ^ { \circ } ( y ) \geq 1 / 2 .
$$

Let $h = { \sqrt { n } } \cdot \psi ^ { \diamond } ( \theta )$ be the local coordinate, and define $B _ { \delta } = \{ y = \psi ^ { \diamond } ( \theta ) : \theta \in \mathcal { M }$ , $\| \theta - \widehat { \theta } ^ { \circ } \| \leq \delta \}$ . Let $\pi ( \cdot )$ be the density function of $\Pi _ { \mathcal { M } }$ with respect to the volume measure of $\mathcal { M }$ . We will start by showing the following result.

Step 1.1. Show

$$
\begin{array} { r l } & { \displaystyle \int \bigg | \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { T } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) } \\ & { \quad \quad - \pi ( \theta ^ { \ast } ) \exp \big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h \big ) \bigg | \mathrm { d } h \leq C \frac { \big ( \log n \big ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } . } \end{array}
$$

To show the desired result, we define the following set of $h \in \mathbb { R } ^ { d }$ ,

$$
\begin{array} { r l } & { A _ { 1 } = \left\{ \| h \| _ { 2 } \leq \delta _ { 2 } \sqrt { \log n } \right\} , } \\ & { A _ { 2 } = \left\{ \delta _ { 2 } \sqrt { \log n } \leq \| h \| _ { 2 } \leq \delta _ { 1 } ( \log n ) ^ { 1 . 5 } \right\} , } \\ & { A _ { 3 } = \left\{ \| h \| _ { 2 } \geq \delta _ { 1 } ( \log n ) ^ { 1 . 5 } \right\} , } \end{array}
$$

where $\delta _ { 2 }$ is a large enough constant that will be chosen later, $\delta _ { 1 }$ is the one specified in the assumption. Then notice that when $\textstyle { \frac { h } { \sqrt { n } } } = \psi ^ { \diamond } ( \theta ) \in B _ { \delta }$ , it holds that $\begin{array} { r } { \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat \theta ^ { \diamond } ) = W _ { \theta ^ { * } } W _ { \theta ^ { * } } { } ^ { T } ( \theta - \theta ^ { * } ) = } \end{array}$

θ holds for any , where $h \in A _ { 3 }$ $\theta \in B _ { \delta } ( \widehat { \theta ^ { \circ } } ) \cap \mathcal { M } \subseteq U _ { \theta ^ { * } }$ δ b  with $\textstyle { \frac { h } { \sqrt { n } } } \in B _ { \delta }$ θ , that . Therefore, by the third condition in the assumptions, it

$$
\log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \leq - 2 c _ { 1 } d \log n .
$$

We can derive that, when $n$ is large enough,

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 3 } } \left. \pi \Big ( \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \right) \mathbf 1 \Big ( \frac { h } { \sqrt { n } } \in B _ { \delta } \Big ) \mathcal { T } ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) } \\ & { \qquad - \pi ( \theta ^ { * } ) \exp \big ( - \frac 1 2 h ^ { T } \Sigma ^ { - 1 } h \big ) \Big \vert \mathrm { d } h } \\ & { \displaystyle \leq \int _ { A _ { 3 } } \pi \Big ( \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf 1 \Big ( \frac { h } { \sqrt { n } } \in B _ { \delta } \Big ) \mathcal { T } ^ { \circ } \Big ( \frac { h } { \sqrt { n } } \Big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } \\ & { \qquad + \int _ { A _ { 3 } } \pi ( \theta ^ { * } ) \exp \big ( - \frac 1 2 h ^ { T } \Sigma ^ { - 1 } h \big ) \mathrm { d } h } \\ & { \displaystyle \leq \exp ( - 2 c _ { 1 } d \log n ) \cdot n ^ { \frac { d } { 2 } } \int _ { B _ { \delta } } \pi ( \phi ^ { \circ } ( y ) ) \mathcal { T } ^ { \circ } ( y ) \mathrm { d } y + \int _ { A _ { 3 } } \pi ( \theta ^ { * } ) \exp \big ( - \frac 1 2 h ^ { T } \Sigma ^ { - 1 } h \big ) \mathrm { d } h } \\ & { \qquad \quad \leq \pi ^ { - c _ { 1 } } , } \end{array}
$$

where the last inequality follows from the positive definiteness of $\Sigma$ and the sub-exponential tail bound (see for example, [72]) to control $\begin{array} { r } { \int _ { A _ { 3 } } \pi ( \theta ^ { * } ) \exp \big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h \big ) \mathrm { d } h } \end{array}$ . Next we consider $h \in A _ { 2 }$ , by the second condition in the assumptions, there exist positive constants $C _ { 3 } , C _ { 4 } , C _ { 5 }$ so that when $\delta _ { 2 } \geq C _ { 3 }$ ,

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 2 } } \pi \Big ( \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } \\ & { \le \displaystyle \int _ { A _ { 2 } } \pi \Big ( \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h + C _ { 4 } \frac { ( \log n ) ^ { \gamma _ { 0 } + 1 . 5 \gamma _ { 2 } } } { n ^ { \gamma _ { 1 } } } \Big ) \mathrm { d } h } \\ & { \le C _ { 5 } \displaystyle \int _ { A _ { 2 } } \exp ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h ) \mathrm { d } h \le n ^ { - c _ { 1 } } , } \end{array}
$$

and

$$
\int _ { A _ { 2 } } \boldsymbol { \pi } \big ( \theta ^ { * } \big ) \exp \big ( { - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h } \big ) \mathrm { d } h \leq n ^ { - c _ { 1 } } .
$$

Then we consider $h \in A _ { 1 }$ ,

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 1 } } \Big \lvert \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) - \pi ( \theta ^ { \ast } ) \exp \big ( - \frac { 1 } { 2 } h ^ { T } \log ( \pi ) \big ) } \\ & { \displaystyle \leq \underbrace { \int _ { A _ { 1 } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \Big | \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) - \exp \big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } \Big ) } _ { ( I _ { A } ) } } \\ & { \displaystyle + \underbrace { \int _ { A _ { 1 } } \exp ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h ) \Big | \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) - \pi ( \theta ^ { \ast } ) \Big | \mathrm { d } h } _ { ( I _ { B } ) } . } \end{array}
$$

For the term ( $I _ { A }$ ), by the second condition in the assumption, we have, for some positive constants $C , C _ { 1 }$ that,

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 1 } } \pi \Big ( \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf 1 \Big ( \frac { h } { \sqrt { n } } \in \mathcal B _ { \delta } \Big ) \mathcal { T } ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \Big | \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \circ } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) - \exp ( - \frac 1 2 h ^ { T } \Sigma ^ { - 1 } h ) \Big | } \\ & { \leq C \displaystyle \int _ { A _ { 1 } } \exp ( - \frac 1 2 h ^ { T } \Sigma ^ { - 1 } h ) \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } ( \| h \| ^ { \gamma _ { 2 } } + 1 ) \mathrm { d } h } \\ & { \leq C _ { 1 } \frac { \left( \log n \right) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } . } \end{array}
$$

For the term ( $I _ { B }$ ), by using the Lipschitz continuity of the prior and the local $C ^ { 3 }$ smoothness of the manifold around $\theta ^ { * }$ (Assumption 1) , it holds for any $h \in A _ { 1 }$ that,

$$
\begin{array} { l } { \displaystyle \Big \vert \pi \big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) - \pi \big ( \theta ^ { \ast } \big ) \Big \vert \leq L \left. \right. \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) - \theta ^ { \ast } \right. \left. = L \left. \right. \phi _ { \theta ^ { \ast } } \big ( W _ { \theta ^ { \ast } } \frac { h } { \sqrt { n } } + \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \circ } } ) \big ) - \phi _ { \theta ^ { \ast } } ( 0 ) \big \vert \Big \vert } \\ { \displaystyle \leq L \left. \left. W _ { \theta ^ { \ast } } \frac { h } { \sqrt { n } } + \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \circ } } ) \right. \right. + C \left. \right. W _ { \theta ^ { \ast } } \frac { h } { \sqrt { n } } + \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \circ } } ) \right. \Big \vert ^ { 2 } \leq C _ { 1 } \frac { \left. \left. \left. h \right. \right. _ { 2 } + \sqrt { \log n } } { \sqrt { n } } . } \end{array}
$$

$$
\mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in B _ { \delta } \Big ) = 1 ,
$$

and

$$
\big | \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) - 1 \big | = \bigg | \sqrt { \bigg | \mathbf { J } _ { \phi ^ { \diamond } } \big ( \frac { h } { \sqrt { n } } \big ) ^ { T } \mathbf { J } _ { \phi ^ { \diamond } } \big ( \frac { h } { \sqrt { n } } \big ) \bigg | } - \sqrt { \bigg | W _ { \theta ^ { \ast } } ^ { T } W _ { \theta ^ { \ast } } \bigg | } \bigg | \leq C _ { 1 } \frac { \| h \| _ { 2 } + \sqrt { \log n } } { \sqrt { n } } .
$$

where the last inequality uses equation (14). Therefore, we can get $\left( I _ { B } \right) \lesssim { \sqrt { \frac { \log n } { n } } }$ , and for some positive constant $C$ ,

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 1 } } \bigg | \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt { n } } \in \mathcal { B } _ { \delta } \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) } \\ & { \quad \quad \quad - \pi \big ( \theta ^ { \ast } \big ) \exp \big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h \big ) \bigg | \mathrm { d } h \leq C \frac { \big ( \log n \big ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } . } \end{array}
$$

Putting together the bounds over $A _ { 1 }$ , $A _ { 2 }$ , and $A _ { 3 }$ gives the desired result in (15).

Step 1.2. Show that there exist positive constants $C _ { 0 } , C _ { 1 }$ such that

$$
\Pi ^ { ( n ) } \Big ( \lVert \theta - \widehat { \theta } ^ { \diamond } \rVert \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big ) \leq C _ { 1 } n ^ { - c _ { 1 } } .
$$

This is precisely the first claim in Lemma 3.

Note that since $\Pi ^ { ( n ) } ( \lVert \theta - { \widehat { \theta } } ^ { \circ } \rVert \geq \delta ) \leq n ^ { - c _ { 1 } }$ , we have

$$
\begin{array} { r l } & { \Pi ^ { ( n ) } \Big ( \| \theta - \widehat { \theta ^ { \circ } } \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big ) \leq \Pi ^ { ( n ) } \Big ( C _ { 0 } \sqrt { \frac { \log n } { n } } \leq \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \Big ) + n ^ { - c _ { 1 } } } \\ & { \qquad \leq \Pi ^ { ( n ) } \Big ( | \| \theta - \widehat { \theta ^ { \circ } } \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big | \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \Big ) + n ^ { - c _ { 1 } } . } \end{array}
$$

Moreover, recall that for any $v \in V _ { \theta ^ { * } }$ , $\| \phi _ { \theta ^ { * } } ( v ) - v - \theta ^ { * } \| \leq C \| v \| ^ { 2 }$ and for any $\theta \in \ U _ { \theta ^ { * } }$ $\lVert \psi _ { \theta ^ { * } } ( \theta ) - ( \theta - \theta ^ { * } ) \rVert \leq C \lVert \theta - \theta ^ { * } \rVert ^ { 2 }$ . Consider any $z ~ \in ~ \mathbb { R } ^ { d }$ with $\begin{array} { r } { \| z \| \leq \frac { C _ { 0 } } { 2 } \sqrt { \frac { \log n } { n } } } \end{array}$ , then for $\theta = \phi ^ { \diamondsuit } ( z ) = \phi _ { \theta ^ { \ast } } ( W _ { \theta ^ { \ast } } z + \psi _ { \theta ^ { \ast } } ( \widehat { \theta } ^ { \diamond } ) )$ , we have for sufficiently large $n$ ,

$$
\begin{array} { r l r } {  { \| \theta - \widehat { \theta ^ { \circ } } \| = \| \theta - ( \theta ^ { * } + W _ { \theta ^ { * } } z + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) ) \| + \| \theta ^ { * } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) - \widehat { \theta ^ { \circ } } \| + \| W _ { \theta ^ { * } } z \| } } \\ & { } & { \leq C \| W _ { \theta ^ { * } } z + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) \| ^ { 2 } + C \| \widehat { \theta ^ { \circ } } - \theta ^ { * } \| ^ { 2 } + \frac { C _ { 0 } } { 2 } \sqrt { \frac { \log n } { n } } \leq C _ { 0 } \sqrt { \frac { \log n } { n } } . } \end{array}
$$

Therefore, we can derive

$$
\begin{array} { r l } & { \Pi ^ { ( n ) } \Big ( \| \theta - \widehat { \theta ^ { \circ } } \| \geq C _ { 0 } \sqrt { \displaystyle \frac { \log n } { n } } \Big ) } \\ & { \leq \Pi ^ { ( n ) } \Big ( | \| \theta - \widehat { \theta ^ { \circ } } \| \geq C _ { 0 } \sqrt { \displaystyle \frac { \log n } { n } } \Big | \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \Big ) + n ^ { - c _ { 1 } } } \\ & { \leq \Pi ^ { ( n ) } \Big ( \| \psi ^ { \diamond } ( \theta ) \| \geq C _ { 0 } \sqrt { \displaystyle \frac { \log n } { n } } \Big | \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \Big ) + n ^ { - c _ { 1 } } . } \end{array}
$$

Moreover, using (17) and (18), when $C _ { 0 } \geq \delta _ { 2 }$ ,

$$
\begin{array} { r l } & { \displaystyle \Pi ^ { ( n ) } \Big ( \| \psi ^ { \diamond } ( \theta ) \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big | \| \theta - \widehat { \theta ^ { \diamond } } \| \leq \delta \Big ) } \\ & { \displaystyle = \frac { \int _ { \frac { h } { \sqrt { n } } \in B _ { \delta } , \| h \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } { \int _ { \frac { h } { \sqrt { n } } \in B _ { \delta } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } } \\ & { \displaystyle \lesssim \bigg ( \int _ { \frac { h } { \sqrt { n } } \in B _ { \delta } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h \bigg ) ^ { - 1 } \cdot n ^ { - c _ { 1 } } . } \end{array}
$$

Moreover, using (15), we have

$$
\begin{array} { r l } & { \bigg | \int _ { \frac { h } { \sqrt n } \in B _ { \delta } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \big ) \Big ) \mathrm { d } h - \pi \big ( \theta ^ { \ast } \big ) ( 2 \pi ) ^ { \frac { d } { 2 } } | \Sigma | ^ { \frac { 1 } { 2 } } \bigg | } \\ & { \leq \int \bigg | \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \Big ) \mathbf { 1 } \Big ( \frac { h } { \sqrt n } \in B _ { \delta } \Big ) \mathcal { I } ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt n } \big ) \big ) \Big ) } \\ & { \qquad - \pi \big ( \theta ^ { \ast } \big ) \exp \big ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } h \big ) \bigg | \mathrm { d } h \leq C \frac { \big ( \log n \big ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } . } \end{array}
$$

Moreover, using the fact that $\pi ( \theta ^ { * } )$ is lower bounded away from zero and $\Sigma$ is positive definite, we have, for sufficiently large $n$ ,

$$
\Pi ^ { ( n ) } \Big ( \| \psi ^ { \circ } ( \theta ) \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big ) \leq \Pi ^ { ( n ) } \Big ( \| \psi ^ { \circ } ( \theta ) \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } \Big | \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \Big ) + n ^ { - c _ { 1 } } \leq C _ { 1 } n ^ { - c _ { 1 } }
$$

# Step 1.3. Show the desired result of (13).

Given that $\Pi ^ { ( n ) } ( \lVert \theta - { \widehat { \theta } } ^ { \circ } \rVert \geq \delta ) \leq n ^ { - c _ { 1 } }$ , it holds for any measurable set $B \subseteq \mathbb { R } ^ { d }$ that,

$$
\left| \Pi ^ { ( n ) } \big ( \psi ^ { \diamond } ( \theta ) \in B \big ) - \Pi ^ { ( n ) } \big ( \psi ^ { \diamond } ( \theta ) \in B \big | \ \| \theta - \widehat \theta ^ { \diamond } \| _ { 2 } \leq \delta \big ) \right| \leq 2 n ^ { - c _ { 1 } } \leq 2 n ^ { - 2 } .
$$

Then we have

$$
\begin{array} { r l } & { \Pi ^ { ( n ) } \Big ( \psi ^ { \diamond } ( \theta ) \in B \Big | \| \theta - \widehat { \theta ^ { \diamond } } \| \leq \delta \Big ) } \\ & { = \frac { \int _ { \frac { h } { \sqrt { n } } \in B _ { \delta } \cap B } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { T } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } { \int _ { \frac { h } { \sqrt { n } } \in B _ { \delta } } \pi \Big ( \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { T } ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { \diamond } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } . } \end{array}
$$

Let $Z$ be a random variable with distribution $\mathcal { N } ( 0 , n ^ { - 1 } \Sigma )$ , then

$$
\begin{array} { r l } & { \quad \mathbb { T } ^ { - \nu } \cdot \langle \mathcal { D } _ { t } ^ { \nu } ( \cdot , \mathcal { S } _ { t } ^ { \nu } ) , ~ F _ { i } ^ { \nu } | \mathcal { L } _ { t } ^ { \nu } \mathcal { L } _ { t } ^ { \nu } \rangle } \\ & { \quad = | | \nabla _ { t } ^ { \nu } \cdot \langle \mathbf { y } _ { t } ^ { \nu } ; \mathbf { y } _ { t } ^ { \nu } \rangle | | \cdot \sum _ { j = 1 } ^ { N } | \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | \cdot \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | } \\ & { \quad = | | \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | \cdot | - \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | | \cdot \sum _ { j = 1 } ^ { N } | \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | \cdot \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | \cdot | \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \mathbf { \hat { y } } _ { t } ^ { \nu } \rangle | } \\ &  \quad \times \langle \mathbf { \hat { y } } _ { t } ^ { \nu } | \cdot \sum _ { j = 1 } ^ { N } | | | \int _  \hat { \mathcal { M } } _  \end{array}
$$

Now using (15) and (19), we have, for any measurable set $B \subseteq \mathbb { R } ^ { d }$ ,

$$
\left| \Pi ^ { ( n ) } ( \psi ^ { \diamond } ( \theta ) \in B ) - P ( z \in B ) \right| \lesssim \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } ,
$$

which completes the proof of Statement (13).

Step 2. Then we will show $\begin{array} { r } { \| \widehat { \theta } _ { p } - \widehat { \theta } ^ { \circ } \| \leq C _ { 1 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } } \end{array}$

This is precisely the second claim in Lemma 3. Note that

$$
\begin{array} { r l } & { \Big \| \mathbb { E } _ { \Pi ^ { ( s ) } } \big [ \psi ^ { \delta } ( \theta ) \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { s } } \| \leq \delta ) \big ] \Big \| } \\ & { = \frac { \Pi ^ { ( s ) } \big ( \| \theta - \widehat { \theta ^ { s } } \| \leq \delta \big ) } { \int _ { \frac { \widehat { h ^ { s } } } { \sqrt { n } } \in B _ { s } } \pi \Big ( \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \mathcal { T } ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } } \\ & { \qquad \cdot \Big \| \int _ { \frac { \widehat { h } } { \sqrt { n } } \in B _ { s } } \frac { h } { \sqrt { n } } \pi \Big ( \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { T } ^ { s } \Big ( \frac { h } { \sqrt { n } } \Big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h \Big \| } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \cdot \Big \| \int _ { \frac { \widehat { h } } { \sqrt { n } } \in B _ { s } } h \cdot \pi \Big ( \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \Big ) \mathcal { T } ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \cdot \exp \Big ( \log \mathcal { L } \big ( X ^ { ( n ) } , \phi ^ { s } \big ( \frac { h } { \sqrt { n } } \big ) \big ) \Big ) \mathrm { d } h } \\ & { \qquad - \int h \cdot \pi ( \theta ^ { s } ) \cdot \exp ( - \frac { 1 } { 2 } h ^ { T } \Sigma ^ { - 1 } { h } ) \mathrm { d } h \Big \| . } \end{array}
$$

Then, by an analysis analogous to Step 1.1 (used to prove (15)), we obtain

$$
\Big \vert \Big \vert \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ \psi ^ { \diamond } ( \theta ) \mathbf { 1 } ( \| \theta - \widehat { \theta } ^ { \diamond } \| \leq \delta ) \big ] \Big \vert \Big \vert \leq C \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } .
$$

Similarly,

$$
\begin{array} { r l } & { \Big \| \mathbb { E } _ { 1 \operatorname* { m i n } } \big [ \mathcal { W } ^ { \phi } ( \theta ) \Psi ^ { \theta } ( \theta ^ { \phi } ) ^ { \lambda } \mathbb { 1 } \big [ ( \theta - \widehat { \theta } ^ { \phi } ) \big ] - \delta \mathbb { 1 } \Big ] - 1 \leq 1 \Big ] \Big \| _ { \Gamma } } \\ & { = \Big \| \int _ { \widehat { \mathcal { T } } _ { \phi } \in \mathcal { E } _ { \phi } } \pi \Big ( \frac { \mu } { \phi ^ { \phi } } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \mathcal { T } ^ { ( \theta ) } \Big ( \theta - \widehat { \theta } ^ { \phi } \Big \| \leq \widehat { \mathcal { W } } \Big ) \Big \| \leq \widehat { \mathcal { W } } \Big ) } \\ & { \quad \quad \cdot \int _ { \widehat { \mathcal { T } } _ { \phi } \in \mathcal { E } _ { \phi } } \frac { \mu \mu ^ { \gamma } } { \pi } \Big ( \theta ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \mathcal { T } ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \cdot \exp \Big ( \log \mathcal { L } \Big ( \mathcal { X } ^ { \sharp \sharp } , \phi ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \Big ) \Big ) \mathrm { d } \widehat { \theta } } \\ & { \quad \quad \cdot \int _ { \frac { 1 } { \pi } \in \mathcal { E } _ { \phi } } \frac { \mu \mu ^ { \gamma } } { \pi } \Big ( \theta ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \Big ) \mathcal { T } ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \cdot \exp \Big ( \log \mathcal { L } \Big ( \mathcal { X } ^ { \sharp } , \phi ^ { \phi } \Big ( \frac { \lambda } { \sqrt { \pi } } \Big ) \Big ) \Big ) \mathrm { d } \widehat { h } - \frac { \Sigma } { \pi } \Big \| \Big \| _ { \mathcal { F } } } \\ &  \lesssim  \end{array}
$$

Then, by an analysis analogous to Step 1.1, we can obtain

$$
\|  n \cdot \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ \psi ^ { \diamond } ( \theta ) \psi ^ { \diamond } ( \theta ) ^ { T } \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { \diamond } } \| \leq \delta ) \big ] - \Sigma \| _ { \mathrm { F } } \leq C \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } .
$$

Notice that $W _ { \theta ^ { * } } \psi ^ { \diamondsuit } ( \theta ) = W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } ( \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) = \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } )$ and

$$
\begin{array} { r l } & { \| \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) - ( \theta - \widehat { \theta ^ { * } } ) \| } \\ & { \leq \| \psi _ { \theta ^ { * } } ( \theta ) - ( \theta - \theta ^ { * } ) \| + \| \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) - ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \| } \\ & { \leq C \| \theta - \theta ^ { * } \| ^ { 2 } + C \| \widehat { \theta ^ { * } } - \theta ^ { * } \| ^ { 2 } } \\ & { \leq C \| \theta - \widehat { \theta ^ { * } } \| ^ { 2 } + C _ { 1 } \frac { \log n } { n } . } \end{array}
$$

Then let $r _ { 1 } = \operatorname* { m i n } ( \delta , { \frac { 1 } { 2 C } } )$ , for any $\theta \in { \mathcal { M } } \cap B _ { r _ { 1 } } ( { \widehat { \theta ^ { \circ } } } )$ , we have

$$
\frac { 1 } { 2 } \| \theta - \widehat { \theta ^ { \circ } } \| \leq \| \theta - \widehat { \theta ^ { \circ } } \| - C \| \theta - \widehat { \theta ^ { \circ } } \| ^ { 2 } \leq \| \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) \| + C _ { 1 } \frac { \log n } { n } .
$$

Therefore,

$$
\begin{array} { r l } & { \left| \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \left[ W _ { \theta } \cdot \hat { \psi } ^ { \diamond } ( \theta ) \mathbf { 1 } ( \| \theta - \hat { \theta } ^ { \diamond } \| \leq \delta ) \right] - \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \left[ ( \theta - \hat { \theta } ^ { \diamond } ) \mathbf { 1 } ( \| \theta - \hat { \theta } ^ { \diamond } \| \leq \delta ) \right] \right| } \\ & { \leq C \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \left[ \| \theta - \hat { \theta } ^ { \diamond } \| ^ { 2 } \mathbf { 1 } ( \| \theta - \hat { \theta } ^ { \diamond } \| \leq \delta ) \right] + C \mathrm { l } \frac { \log n } { n } } \\ & { \leq C \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \left[ \| \theta - \hat { \theta } ^ { \diamond } \| ^ { 2 } \mathbf { 1 } ( \| \theta - \hat { \theta } ^ { \diamond } \| \leq r _ { 1 } ) \right] + C \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \left[ \| \theta - \hat { \theta } ^ { \diamond } \| ^ { 2 } \mathbf { 1 } ( r _ { 1 } \leq \| \theta - \hat { \theta } ^ { \diamond } \| \leq \delta ) \right] + C _ { 1 } ^ { \log } } \\ & { \leq 4 C \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \Bigg [ \Big ( \| \psi _ { \theta ^ { \star } } ( \theta ) - \psi _ { \theta ^ { \star } } ( \hat { \theta } ^ { \diamond } ) \| + C _ { 1 } \frac { \log n } { n } \Big ) ^ { 2 } \mathbf { 1 } ( \| \theta - \hat { \theta } ^ { \diamond } \| \leq r _ { 1 } ) \Bigg ] + C \delta ^ { 2 } \mathbf { I } ^ { ( n ) } ( \| \theta - \hat { \theta } ^ { \diamond } \| \geq \gamma ) } \\ &  \leq 4 C \mathbb { E } _ { \mathbf { I } ^ { ( n ) } } \Big [ \psi ^ { \diamond } ( \theta ) ^ { T } \psi ^ { \diamond } (  \end{array}
$$

and

$$
\begin{array} { r l } & { \left\| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ ( \theta - \widehat { \theta ^ { \circ } } ) \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta ) \big ] - \big ( \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \widehat { \theta ^ { \circ } } \big ) \right\| } \\ & { \leq \left\| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ \theta \cdot \mathbf { 1 } \big ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \big ) \big ] - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \right\| + \left\| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ \widehat { \theta ^ { \circ } } \cdot \mathbf { 1 } \big ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta \big ) \big ] - \widehat { \theta ^ { \circ } } \right\| } \\ & { \leq C _ { 4 } \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Combined with statements (21), we can get

$$
\begin{array} { r l } & { \| \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \widehat { \theta ^ { \circ } } \| } \\ & { \leq \Big \| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ ( \theta - \widehat { \theta ^ { \circ } } ) \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta ) \big ] \Big \| + \frac { C _ { 4 } } { n ^ { 2 } } } \\ & { \leq \Big \| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ W _ { \theta ^ { * } } \psi ^ { \circ } ( \theta ) \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta ) \big ] \Big \| + C _ { 3 } \frac { \log n } { n } + \frac { C _ { 4 } } { n ^ { 2 } } } \\ & { = \Big \| \mathbb { E } _ { \Pi ^ { ( n ) } } \big [ \psi ^ { \circ } ( \theta ) \mathbf { 1 } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq \delta ) \big ] \Big \| + C _ { 3 } \frac { \log n } { n } + \frac { C _ { 4 } } { n ^ { 2 } } } \\ & { \leq C _ { 5 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } . } \end{array}
$$

Based on the fact, we can now show the existence of arg $\mathrm { m i n } _ { y \in \mathcal { M } } \| y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| ^ { 2 }$ . Using $\lVert \widehat { { \boldsymbol { \theta } } ^ { \circ } } - { \boldsymbol { \theta } } ^ { * } \rVert \leq$ $c { \sqrt { \frac { \log n } { n } } }$ , it holds that $\begin{array} { r } { \left\| \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \theta ^ { * } \right\| \leq c \sqrt { \frac { \log n } { n } } + C _ { 5 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } \leq 2 c \sqrt { \frac { \log n } { n } } } \end{array}$ So for any $y \in \mathcal { M }$ with $\left\| y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \right\| \leq \left\| \theta ^ { * } - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \right\|$ , it holds that

$$
\Vert y - \theta ^ { * } \Vert \leq \Vert y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \Vert + \Vert \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \theta ^ { * } \Vert \leq 4 c \sqrt { \frac { \log n } { n } } .
$$

Moreover, for any $\begin{array} { r } { y \in B ( \theta ^ { * } , 4 c \sqrt { \frac { \log n } { n } } ) \cap \mathcal { M } \subset U _ { \theta ^ { * } } } \end{array}$ , it holds that $\lVert \psi ^ { \diamond } ( y ) \rVert = \lVert W _ { \theta ^ { \ast } } ^ { T } ( y - \widehat { \theta ^ { \diamond } } ) \rVert \leq$ $\left\| y - { \widehat { \theta } } ^ { \circ } \right\| \leq 5 c { \sqrt { \frac { \log n } { n } } }$ . So we have $y \in \{ \phi ^ { \circ } ( z ) : \| z \| \leq 5 c { \sqrt { \frac { \log n } { n } } } \}$ , and

$$
\begin{array} { r } { \arg \operatorname* { m i n } _ { y \in \mathcal { M } } \| y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| ^ { 2 } = \arg \operatorname* { m i n } _ { z \in \mathbb { R } ^ { d } , \| z \| \leq 5 c \sqrt { \frac { \log n } { n } } } \| \phi ^ { \diamond } ( z ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| ^ { 2 } . } \end{array}
$$

Using the compactness of $\{ z \in \mathbb { R } ^ { d } : \| z \| \leq 5 c { \sqrt { \frac { \log n } { n } } } \}$ , the set of arg $\operatorname* { m i n } _ { z \in \mathbb { R } ^ { d } , \| z \| \leq 5 c \sqrt { \frac { \log n } { n } } } \| \phi ^ { \diamond } ( z ) -$ $\mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \rVert ^ { 2 }$ is well defined and non-empty. Then we will show that the set only contains a single point . Suppose there exist $z _ { 1 } , z _ { 2 } \in \{ z \in \mathbb { R } ^ { d } : \| z \| \leq 5 c \sqrt { \frac { \log n } { n } } \}$ log nn } with z1 ̸= z2 so that $\| \phi ^ { \diamondsuit } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| = \| \phi ^ { \diamondsuit } ( z _ { 2 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| = \mathrm { m }$ $\begin{array} { r } { \| \phi ^ { \diamondsuit } ( z _ { 2 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| = \operatorname* { m i n } _ { y \in \mathcal { M } } \| y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| } \end{array}$ . Then note that $\phi ^ { \circ } ( 0 _ { d } ) = \widehat { \theta ^ { \circ } }$ , it holds that

$$
\begin{array} { r l } & { \| \phi ^ { \diamond } ( z _ { 1 } ) - \phi ^ { \diamond } ( 0 _ { d } ) \| \leq \| \phi ^ { \diamond } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| + \| \widehat { \theta ^ { \diamond } } - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| } \\ & { \leq 2 \| \widehat { \theta ^ { \diamond } } - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| \leq 2 C _ { 5 } \frac { \left( \log n \right) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } . } \end{array}
$$

So $\begin{array} { r } { \| z _ { 1 } \| \leq \| \phi ^ { \diamond } ( z _ { 1 } ) - \phi ^ { \diamond } ( 0 _ { d } ) \| \leq 2 C _ { 5 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } } \end{array}$ Similarly, we have $\begin{array} { r } { \| z _ { 2 } \| \le 2 C _ { 5 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } } \end{array}$ So both $z _ { 1 }$ and $z _ { 2 }$ are interior points of $\{ z \in \mathbb { R } ^ { d } : \| z \| \leq 5 c { \sqrt { \frac { \log n } { n } } } \}$ q log nn }, and we have

$$
\mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 1 } ) ^ { T } ( \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \phi ^ { \diamond } ( z _ { 1 } ) ) = \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } ( \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] - \phi ^ { \diamond } ( z _ { 2 } ) ) = 0 _ { d } .
$$

Then we can further write

$$
\mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } ( \phi ^ { \diamond } ( z _ { 1 } ) - \phi ^ { \diamond } ( z _ { 2 } ) ) = \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } ( \phi ^ { \diamond } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] ) .
$$

For the left hand side, when $n$ is sufficiently large, there exist some constants $C _ { 1 } , C _ { 2 }$ so that

$$
\begin{array} { r l } & { \displaystyle \| \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } ( \phi ^ { \diamond } ( z _ { 1 } ) - \phi ^ { \diamond } ( z _ { 2 } ) ) \| } \\ & { \geq \| \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ( z _ { 1 } - z _ { 2 } ) \| - C _ { 1 } \| z _ { 1 } - z _ { 2 } \| ^ { 2 } } \\ & { \geq C _ { 2 } \| z _ { 1 } - z _ { 2 } \| - C _ { 1 } \| z _ { 1 } - z _ { 2 } \| ^ { 2 } } \\ & { \geq \displaystyle \frac { C _ { 2 } } { 2 } \| z _ { 1 } - z _ { 2 } \| . } \end{array}
$$

For the right hand side, there exists a constant $C _ { 3 }$ so that

$$
\begin{array} { r l } & { \left\| \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } ( \phi ^ { \diamond } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] ) \right\| } \\ & { \leq \Big \| \big ( \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } - \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 1 } ) ^ { T } \big ) ( \phi ^ { \diamond } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] ) \Big \| } \\ & { \leq \big \| \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 2 } ) ^ { T } - \mathbf { J } _ { \phi ^ { \diamond } } ( z _ { 1 } ) ^ { T } \big \| _ { \mathrm { F } } \| \phi ^ { \diamond } ( z _ { 1 } ) - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| } \\ & { \leq C _ { 3 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } \| z _ { 1 } - z _ { 2 } \| . } \end{array}
$$

So combined with these inequalities, we have

$$
C _ { 3 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } \| z _ { 1 } - z _ { 2 } \| \geq \frac { C _ { 2 } } { 2 } \| z _ { 1 } - z _ { 2 } \| .
$$

So when $n$ is large enough so that $C _ { 3 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } < \frac { C _ { 2 } } { 2 }$ < C22 , we must have z1 = z2. This shows that $\begin{array} { r } { \widehat { \theta } _ { p } = \arg \operatorname* { m i n } _ { y \in \mathcal { M } } \| y - \mathbb { E } _ { \Pi ^ { ( n ) } } [ \theta ] \| ^ { 2 } } \end{array}$ is well and uniquely defined, and

$$
\| \widehat { \theta } _ { p } - \widehat { \theta } ^ { \diamond } \| = \| \phi ^ { \diamond } ( z _ { 1 } ) - \phi ^ { \diamond } ( 0 _ { d } ) \| \leq 2 C _ { 5 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } + \frac { 1 } { 2 } } } .
$$

Step 3. Show that for any $f : \mathcal { M } \to \mathbb { R } ^ { p }$ satisfying Assumption D, it holds that $\begin{array} { r } { \mathrm { T V } \Big ( f _ { \# } \Pi ^ { ( n ) } , \mathcal { N } \big ( f ( \widehat { \theta ^ { \diamond } } ) , n ^ { - 1 } J _ { f } \Sigma J _ { f } ^ { T } \big ) \Big ) \leq C _ { 2 } \frac { ( \log n ) ^ { \frac { 1 + \beta } { 2 } } } { n ^ { \frac { \beta } { 2 } } } . } \end{array}$

This is precisely the third claim in Lemma 3. Note that it suffices to consider the case where $p = d$ . Indeed, when $p < d$ , uses that each column of $J _ { f } ^ { I }$ lies in $T _ { \theta ^ { * } } { \mathcal { M } }$ and that $J _ { f }$ is full rank. There exists a matrix $J ^ { \perp } = [ v _ { 1 } , v _ { 2 } , \cdots , v _ { d - p } ] \in \mathbb { R } ^ { D \times ( d - p ) }$ whose columns lie in $T _ { \theta ^ { * } } { \mathcal { M } }$ , satisfy $( J ^ { \perp } ) ^ { T } J ^ { \perp } = I _ { d - p }$ , and orthogonal to the columns of $J _ { f } ^ { I }$ . Define $f _ { p + j } ( \theta ) = v _ { j } ^ { T } \theta$ for $j = \{ 1 , 2 , \cdot \cdot \cdot , d - p \}$ , and set ${ \overline { { f } } } = \left( f _ { 1 } , f _ { 2 } , \cdots , f _ { d } \right)$ . Then Assumption B holds for $f$ with $p = d$ . Consequently, the desired conclusion for $f _ { \# } \Pi ^ { ( n ) }$ follows from the result for $\overline { { f } } _ { \# } \Pi ^ { ( n ) }$ by the data processing inequality. Now let’s suppose $d = p$ . Since $\mathbf { J } _ { \phi ^ { \circ } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) ) = W _ { \theta ^ { * } }$ , we have

$$
\mathbf { J } _ { f \circ \phi ^ { \circ } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) ) = J _ { f } W _ { \theta ^ { * } } ,
$$

and

$$
a ^ { 2 } I _ { p } \preccurlyeq { \mathbf { J } } _ { f \circ \phi ^ { \diamond } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) \mathbf { J } _ { f \circ \phi ^ { \diamond } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) ^ { T } = J _ { f } J _ { f } ^ { T } \preccurlyeq b ^ { 2 } I _ { p } .
$$

Moreover, it holds for any measurable set $A \subset \mathbb { R } ^ { d }$ that,

$$
\begin{array} { r l } & { \Pi ^ { ( n ) } ( f ( \theta ) \in A ) - \Pi ^ { ( n ) } \Big ( \psi ^ { \circ } ( \theta ) \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \circ } ( \psi ^ { \circ } ( \theta ) ) \in A \Big ) \Big | } \\ & { \leq \Big | \Pi ^ { ( n ) } \big ( \theta \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( \widehat { \theta ^ { \circ } } ) , f ( \theta ) \in A \big ) - \Pi ^ { ( n ) } \Big ( \psi ^ { \circ } ( \theta ) \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \circ } ( \psi ^ { \circ } ( \theta ) ) \in A \Big ) \Big | + } \\ & { = \Big | \Pi ^ { ( n ) } \big ( \theta \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( \widehat { \theta ^ { \circ } } ) , f \circ \phi ^ { \circ } ( \psi ^ { \circ } ( \theta ) ) \in A \big ) } \\ & { \qquad - \Pi ^ { ( n ) } \Big ( \psi ^ { \circ } ( \theta ) \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \circ } ( \psi ^ { \circ } ( \theta ) ) \in A \Big ) \Big | + \frac { 1 } { n ^ { 2 } } } \\ & { \leq \Pi ^ { ( n ) } \big ( \theta \not \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( \widehat { \theta ^ { \circ } } ) \big ) + \frac { 1 } { n ^ { 2 } } \leq \frac { 2 } { n ^ { 2 } } . } \end{array}
$$

Let $Z$ be a random vector with distribution $\begin{array} { r l } {  { \mathcal { N } ( 0 , n ^ { - 1 } \Sigma _ { 0 } ) } } \end{array}$ . Then by statement (13), we have

$$
\begin{array} { r l } & { \left| \Pi ^ { ( n ) } \Big ( \psi ^ { \diamond } ( \theta ) \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \diamond } ( \psi ^ { \diamond } ( \theta ) ) \in A \Big ) - P \Big ( Z \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \diamond } ( Z ) \in A \Big ) \right. } \\ & { \left. \le C \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } , \right. } \end{array}
$$

which leads to

$$
\left| \Pi ^ { ( n ) } ( f ( \theta ) \in A ) - P \Big ( Z \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \diamond } ( Z ) \in A \Big ) \right| \leq C _ { 1 } \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } .
$$

Furthermore, using the Lipschitz continuous of the Riemannian gradient of $f$ , and the thrice differentiability of $\phi ^ { \circ }$ , there exists a positive constant $r$ so that for any $z \in B _ { r } ( 0 _ { d } )$ ,

$$
\big | \big | \big | \mathbf { J } _ { f \circ \phi ^ { \circ } } ( z ) - \mathbf { J } _ { f \circ \phi ^ { \circ } } ( - W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) ) \big | \big | _ { \mathrm { F } } \leq C \| z + W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) \| \leq C \| z \| + C \| \theta ^ { \circ } - \theta ^ { * } \| .
$$

Therefore, using $a ^ { 2 } I _ { d } \ \preccurlyeq \ \mathbf { J } _ { f \circ \phi ^ { \diamond } } ( - W _ { \theta ^ { \ast } } ^ { T } \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \diamond } } ) ) \mathbf { J } _ { f \circ \phi ^ { \diamond } } ( - W _ { \theta ^ { \ast } } ^ { T } \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \diamond } } ) ) ^ { T } \ \preccurlyeq \ b ^ { 2 } I _ { d }$ , when $r$ is small enough, we have for any $z \in B _ { r } ( 0 _ { d } )$ , $\begin{array} { r } { \frac { a ^ { 2 } } { 2 } I _ { d } \preccurlyeq \mathbf { J } _ { f \circ \phi ^ { \diamond } } ( z ) \mathbf { J } _ { f \circ \phi ^ { \diamond } } ( z ) ^ { T } \preccurlyeq \frac { b ^ { 2 } } { 2 } I _ { d } } \end{array}$ . Moreover, by inverse function theorem for Hölder space (see for example, Appendix A of [27]), there exist positive constants $r _ { 1 } , r _ { 2 }$ and open sets $\mathcal { U } \supset B _ { r _ { 1 } } ( 0 _ { d } )$ and $\mathcal { V } \supset B _ { r _ { 2 } } ( f ( \widehat { \theta ^ { \circ } } ) )$ , so that $f \circ \phi ^ { \circ } | \mathcal { U } : \mathcal { U } \to \mathcal { V }$ is a diffeomorphism. Moreover, there exist positive constants $C , C _ { 1 }$ so that for any $y , y ^ { \prime } \in B _ { r _ { 2 } } ( f ( \widehat { \theta ^ { \circ } } ) )$ ,

$$
\lvert ( f \circ \phi ^ { \diamond } | u ) ^ { - 1 } ( y ) - ( f \circ \phi ^ { \diamond } | u ) ^ { - 1 } ( y ^ { \prime } ) \rvert \leq C \lVert y - y ^ { \prime } \rVert .
$$

and

$$
\begin{array} { r l } & { \| ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } ( y ) - ( J _ { f } W _ { \theta ^ { \bullet } } ) ^ { - 1 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) \| } \\ & { = \| ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } ( y ) - ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } ( f ( \widehat { \theta ^ { \circ } } ) ) - \mathbf { J } _ { ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } } ( f ( \widehat { \theta ^ { \circ } } ) ) ( y - f ( \widehat { \theta ^ { \circ } } ) ) \| } \\ & { \quad + \| \mathbf { J } _ { ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } } ( f ( \widehat { \theta ^ { \circ } } ) ) ( y - f ( \widehat { \theta ^ { \circ } } ) ) - ( \mathbf { J } _ { f } W _ { \theta ^ { \ast } } ) ^ { - 1 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) \| } \\ & { \leq C \| y - f ( \widehat { \theta ^ { \circ } } ) \| ^ { 2 } + C \| y - f ( \widehat { \theta ^ { \circ } } ) \| \cdot \big \| \big | J _ { f \circ \phi ^ { \circ } } ( 0 _ { d } ) - \mathbf { J } _ { f \circ \phi ^ { \circ } } ( - W _ { \theta ^ { \ast } } ^ { T } \psi _ { \theta ^ { \ast } } ( \widehat { \theta ^ { \circ } } ) ) \big | \big \| _ { \mathrm { F } } } \\ & { \leq C _ { 1 } \| y - f ( \widehat { \theta ^ { \circ } } ) \| ^ { 2 } + C _ { 1 } \frac { \log n } { n } . } \end{array}
$$

Therefore, let $Y$ be a random vector with distribution $\mathcal { N } ( f ( \widehat { \theta ^ { \circ } } ) , n ^ { - 1 } J _ { f } W _ { \theta ^ { * } } \Sigma W _ { \theta ^ { * } } ^ { T } J _ { f } ^ { T } )$ , when $C _ { 0 }$ is large enough, we have

$$
\begin{array} { r l } & { 0 \leq P ( Y \in A ) - P \big ( Y \in A \cap \{ y = f \circ \phi ^ { \circ } ( z ) : z \in B _ { C _ { 0 } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) \} \big ) } \\ & { \leq 1 - P \Big ( Y \in B _ { \frac { C _ { 0 } } { C } \sqrt { \frac { \log n } { n } } } ( f ( \widehat { \theta ^ { \circ } } ) ) \Big ) \leq \frac { 1 } { n } . } \end{array}
$$

Consider

$$
\begin{array} { r l } & { \begin{array} { l } { \displaystyle p \Big ( Z \in B _ { _ { C _ { 0 } } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) , f \circ \phi ^ { \circ } ( Z ) \in A \Big ) } \\ { \displaystyle p = \int _ { y \in A \cap \{ y = f \circ \phi ^ { \circ } ( z ) : z \in B _ { _ { C _ { 0 } } \sqrt { \frac { \log n } { n } } } ( 0 _ { d } ) \} } \frac { \operatorname* { d e t } \big ( J _ { ( f \circ \phi ^ { \circ } | u ) } - 1 ( y ) \big ) } { ( 2 \pi ) ^ { \frac { d } { 2 } } \operatorname* { d e t } ( n ^ { - 1 } \Sigma ) ^ { \frac { 1 } { 2 } } } \exp \Big ( - \frac { n } { 2 } ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } ( y ) ^ { T } \Sigma ^ { - 1 } ( f \circ \phi ^ { \circ } ( z ) | u ) \Big ) } \end{array} } \end{array}
$$

We have

$$
\begin{array} { r l } & { P \Big ( Z \in B _ { C _ { \hat { \sigma } } \sqrt { \frac { \log n } { n } } } ( \mathbb { I } _ { \hat { \sigma } } ) , f \circ \hat { \sigma } ^ { \hat { \sigma } } ( Z ) \in A \Big ) - P ( Y \in A ) \Big | } \\ & { \leq \int _ { y \in A \cap \{ y = \hat { \sigma } ^ { \hat { \sigma } } ( z ) : z \in B _ { \hat { \sigma } } \sqrt { \frac { \log n } { n } } ( \mathbb { I } _ { \hat { \sigma } } ) \} } \Big | \frac { \big | \mathrm { d } \mathrm { c } \big ( \mathbf { J } _ { 1 } ( f _ { \sigma } \phi \circ \hat { \sigma } ) , ( y ) \big ) } { \big ( 2 \pi ) ^ { \frac { d } { d } } \mathrm { d } \mathrm { e t } \big ( n ^ { - 1 } \Sigma \big ) ^ { \frac { 1 } { 2 } } } \mathrm { e x p } \Big ( - \frac { n } { 2 } ( f \circ \phi ^ { \varepsilon } | _ { \mathcal { U } } ) ^ { - 1 } ( y ) ^ { T } \Sigma ^ { - 1 } ( f \circ \cdot } \\ & { \qquad - \frac { \mathrm { d } \mathrm { c } \mathrm { t } ( ( \mathcal { J } _ { f } W _ { \hat { \sigma } } \star ) ^ { - 1 } ) } { ( 2 \pi ) ^ { \frac { d } { d } } \mathrm { d } \mathrm { e t } ( n ^ { - 1 } \Sigma ) ^ { \frac { 1 } { 2 } } } ) \mathrm { e x p } \Big ( - \frac { n } { 2 } ( y - f ( \hat { \theta } ^ { \varepsilon } ) ) ^ { T } ( ( \mathcal { J } _ { f } W _ { \hat { \sigma } } \star ) ^ { - 1 } ) ^ { T } \Sigma ^ { - 1 } ( \mathcal { J } _ { f } W _ { \hat { \sigma } } \star ) ^ { - 1 } ( y - f ( \hat { \theta } ^ { \varepsilon } ) ) \Big ) \Big | \leq } \\ &  \leq \int _  y \subseteq A \cap \{ y \leq \hat { \sigma } ^ { \hat { \sigma } } ( z ) : z \in B _ { \hat { \sigma } } \sqrt { \frac { \log n } { n } } ( \hat  \sigma  \end{array}
$$

Furthermore, for term $( I _ { C } )$ , using (26), we have for some constants $C , C _ { 1 }$ ,

$$
\begin{array} { r l } & { ( I _ { C } ) \le C \displaystyle \int _ { y \in A \cap \{ y = f \otimes \phi ^ { \circ } ( z ) : z \in B _ { C _ { 0 } } \sqrt { \frac { \log n } { n } } ( 0 , d ) \} } \frac { \operatorname* { d e t } \big ( \mathbf { J } _ { ( f \circ \phi ^ { \circ } | u ) } - 1 ( y ) \big ) } { ( 2 \pi ) ^ { \frac d 2 } \operatorname* { d e t } ( n ^ { - 1 } \Sigma ) ^ { \frac 1 2 } } } \\ & { \qquad \cdot \exp \Big ( - \frac { n } { 2 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) ^ { T } ( ( J _ { f } W _ { \theta ^ { \ast } } ) ^ { - 1 } ) ^ { T } \Sigma ^ { - 1 } ( J _ { f } W _ { \theta ^ { \ast } } ) ^ { - 1 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) \Big ) } \\ & { \qquad \cdot n \cdot ( \| y - f ( \widehat { \theta ^ { \circ } } ) \| ^ { 2 } + \frac { \log n } { n } ) \cdot \| y - f ( \widehat { \theta ^ { \circ } } ) \| \mathrm { d } y } \\ & { \le C _ { 1 } \frac { \log n } { \sqrt { n } } . } \end{array}
$$

For term $\left( I _ { D } \right)$ , using $\mathbf { J } _ { ( f \circ \phi ^ { \circ } | u ) ^ { - 1 } } ( y ) = ( \mathbf { J } _ { f \circ \phi ^ { \circ } } ( z ) ) ^ { - 1 }$ with $z = ( f \circ \phi ^ { \circ } | \boldsymbol { u } ) ^ { - 1 } ( y )$ , and

$$
\begin{array} { r l } { \| ( f \circ \phi ^ { \circ } | _ { \mathcal { U } } ) ^ { - 1 } ( y ) \| = } & { \| ( f \circ \phi ^ { \circ } | _ { \mathcal { U } } ) ^ { - 1 } ( y ) - ( f \circ \phi ^ { \circ } | _ { \mathcal { U } } ) ^ { - 1 } ( f ( \widehat { \theta ^ { \circ } } ) ) \| \leq C \| y - f ( \widehat { \theta ^ { \circ } } ) \| , } \end{array}
$$

as well as inequality (25), we can get for some constants $C , C _ { 1 }$ ,

$$
\begin{array} { r l } & { ( I _ { D } ) \le C n ^ { \frac { d } { 2 } } \displaystyle \int _ { y \in A \cap \{ y = f \circ \phi ^ { \circ } ( z ) : z \in B _ { C _ { 0 } } \sqrt { \frac { \log n } { n } } ( 0 _ { d } ) \} } \left( \| y - f ( \widehat { \theta ^ { \circ } } ) \| + \sqrt { \frac { \log n } { n } } \right) } \\ & { \qquad \cdot \exp \Big ( - \displaystyle \frac { n } { 2 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) ^ { T } ( ( \mathbf { J } _ { f } W _ { \theta ^ { * } } ) ^ { - 1 } ) ^ { T } \Sigma ^ { - 1 } ( \mathbf { J } _ { f } W _ { \theta ^ { * } } ) ^ { - 1 } ( y - f ( \widehat { \theta ^ { \circ } } ) ) \Big ) \mathrm { d } y } \\ & { \le C _ { 1 } \sqrt { \displaystyle \frac { \log n } { n } } . } \end{array}
$$

Then combined with (24), it holds for $\boldsymbol { Y } \sim \mathcal { N } ( \boldsymbol { f } ( \widehat { \boldsymbol { \theta } ^ { \circ } } ) , n ^ { - 1 } J _ { f } W _ { \boldsymbol { \theta } ^ { \ast } } \Sigma W _ { \boldsymbol { \theta } ^ { \ast } } ^ { T } J _ { f } ^ { T } )$ and any measurable set $A \subset \mathbb { R } ^ { d }$ that,

$$
\left| P ( Y \in A ) - \Pi ^ { ( n ) } ( f ( \theta ) \in A ) \right| \leq C { \frac { ( \log n ) ^ { \gamma _ { 0 } } } { n ^ { \gamma _ { 1 } } } } ,
$$

which leads to the desired result.

# E Proof for Bayesian RPETEL Posterior

We will prove Theorem 2, Corollary 2 and Corollary 3 in this section.

# E.1 Proof of Theorem 2

We will use Lemma 3 to show the desired result. We will start with verifying the conditions of Lemma 3.

Step 1: Define the set $\mathcal { A }$ . Consider sufficiently large constants $C$ and $C _ { 1 }$ , and define

$$
\begin{array} { r } { \mathcal A _ { 1 } = \big \{ X ^ { ( n ) } \in \mathcal X ^ { n } : \forall i \in [ n ] , b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big \} ; } \end{array}
$$

$$
{ \mathcal { A } } _ { 2 } = \Big \{ X ^ { ( n ) } \in \mathcal { X } ^ { n } : \Big \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \Big \| \leq C _ { 1 } \sqrt { \frac { \log n } { n } } \Big \} ;
$$

$$
\mathcal A _ { 3 } = \Big \{ X ^ { ( n ) } \in \mathcal X ^ { n } : n ^ { - 1 } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ^ { \ast } ) \| ^ { 3 } \cdot \mathbf { 1 } \big ( b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \leq C _ { 1 } \Big \} ;
$$

$$
\begin{array} { c l } { \displaystyle \mathcal { A } _ { 4 } = \bigg \{ X ^ { ( n ) } \in \mathcal { X } ^ { n } : \forall \theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } , \bigg \| \Big \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } } \\ { \displaystyle - \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \big ] \bigg \| _ { \mathrm { F } } \leq C _ { 1 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + \frac { 1 } { 2 } } } { \sqrt { n } } \bigg \} ; } \end{array}
$$

$$
\mathcal A _ { 5 } = \Bigg \{ X ^ { ( n ) } \in \mathcal X ^ { n } : \forall \theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal M , \Big \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 } \Big \| n ^ { - 1 }
$$

$$
- \mathbb { E } [ g ( X , \theta ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] { \Big \| } _ { 2 } \leq C _ { 1 } ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( { \sqrt { \frac { \log n } { n } } } \| \theta - \theta ^ { * } \| ^ { \beta _ { 2 } } + { \frac { \log n } { n } } \Big ) \Bigg \} ;
$$

$$
{ \mathcal { A } } _ { 6 } = \left\{ X ^ { ( n ) } \in { \mathcal { X } } ^ { n } : \forall \theta , \theta ^ { \prime } \in S _ { \Pi } , \left| n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { \prime } ) \right. \right.
$$

$$
- \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { \prime } ) ] { \Big | } { \le { C _ { 1 } } } ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } + \frac { \log n } { n } \Big ) \bigg \} ;
$$

$$
\begin{array} { r l } & { \mathcal { A } _ { 7 } = \bigg \{ X ^ { ( n ) } \in \mathcal { X } ^ { n } : \forall \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } , \bigg | n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { \prime } ) } \\ & { \qquad - \displaystyle \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \prime } ) ^ { T } ( \theta - \theta ^ { \prime } ) - \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { \prime } ) ] + \mathbb { E } \big [ g ( X , \theta ^ { \prime } ) ^ { T } ( \theta - \theta ^ { \prime } ) \big ] \bigg | } \\ & { \qquad \leq C _ { 1 } \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \bigg ( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 2 } + 1 } + \displaystyle \frac { \log n } { n } \| \theta - \theta ^ { \prime } \| + ( \frac { \log n } { n } ) ^ { 2 } \bigg ) \bigg \} . } \end{array}
$$

Let $\mathcal { A } = \mathcal { A } _ { 1 } \cap \mathcal { A } _ { 2 } \cap \cdot \cdot \cdot \cap \mathcal { A } _ { 7 }$ . Then we have the following lemma concerning the probability of $\mathcal { A }$ .

Lemma 5. Under Assumptions 1-4, there exist constants $C$ and $C _ { 1 }$ such that $P ( X ^ { ( n ) } \in { \mathcal { A } } ) \geq$ $1 - n ^ { - 2 }$ .

Now let’s fix an $X ^ { ( n ) } \in { \mathcal { A } }$ and let $W _ { \theta ^ { * } } \in \mathbb { R } ^ { D \times d }$ be an arbitrary matrix whose columns form an orthonormal basis of $T _ { \theta ^ { * } } { \mathcal { M } }$ .

Step 2: Show $\begin{array} { r } { \| \theta ^ { * } - \widehat { \theta } ^ { \diamond } ( X ^ { ( n ) } ) \| \lesssim \sqrt { \frac { \log n } { n } } } \end{array}$ .

Since $\mathcal { M }$ is locally $C _ { r , L } ^ { 3 }$ around $\theta ^ { * }$ , there exists $U _ { \theta ^ { * } } , V _ { \theta * }$ with $B _ { r } ( \theta ) \cap \mathcal { M } \subseteq U _ { \theta ^ { * } } \subseteq \mathcal { M }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta ^ { * } } { \mathcal { M } } \subseteq V _ { \theta ^ { * } } \subset T _ { \theta ^ { * } } { \mathcal { M } }$ , so that $\psi _ { \theta ^ { * } } : U _ { \theta ^ { * } } \to V _ { \theta ^ { * } }$ defined by $\psi _ { \theta ^ { * } } ( x ) = \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( x - \theta ^ { * } )$

is a bijective, where the inverse, denoted by $\phi _ { \theta ^ { * } }$ is thrice Fréchet differentiable, and its Fréchet derivatives up to order three have operator norms uniformly bounded by $L$ . By the thrice differentiablity of $\phi _ { \theta ^ { * } }$ , there exists a constant $C _ { 2 }$ so that

$$
\operatorname* { s u p } _ { v \in V _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } ( v ) - ( v + \theta ^ { * } ) \| } { \| v \| ^ { 2 } } \leq C _ { 2 } ,
$$

and

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { \theta ^ { \prime } \in U _ { \theta ^ { * } } } \frac { \| \psi _ { \theta ^ { * } } ( \theta ^ { \prime } ) - ( \theta ^ { \prime } - \theta ^ { * } ) \| } { \| \theta ^ { * } - \theta ^ { \prime } \| ^ { 2 } } = \displaystyle \operatorname* { s u p } _ { \theta ^ { \prime } \in U _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } \left( \psi _ { \theta ^ { * } } \left( \theta ^ { \prime } \right) \right) - \left( \theta ^ { * } + \psi _ { \theta ^ { * } } \left( \theta ^ { \prime } \right) \right) \| } { \| \theta ^ { * } - \theta ^ { \prime } \| } } \\ & { \quad \quad \quad \quad \leq \displaystyle \operatorname* { s u p } _ { v \in V _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } \left( v \right) - ( v + \theta ^ { * } ) \| } { \| v \| ^ { 2 } } \leq C _ { 2 } . } \end{array}
$$

Note that $\begin{array} { r } { \mathcal { R } ( \theta ) { - } \mathcal { R } ( \theta ^ { * } ) \geq \frac { 1 } { L } \vert \vert \theta { - } \theta ^ { * } \vert \vert ^ { 2 } } \end{array}$ holds for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap { \mathcal { M } }$ . Moreover, using second-order Taylor expansion on curves of manifold (see for example (5.26) of [16]), it holds that for any $v \in \mathbb { R } ^ { d }$ with $\lVert \boldsymbol { v } \rVert = 1$ , and $0 < t \leq r$ ,

$$
\mathcal { R } ( \phi _ { \theta ^ { * } } ( t W _ { \theta ^ { * } } v ) ) - \mathcal { R } ( \theta ^ { * } ) \leq \frac { t ^ { 2 } } { 2 } v ^ { T } W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } v + C t ^ { 3 } .
$$

Moreover when $t$ is small enough so that $\phi _ { \theta ^ { \ast } } ( t W _ { \theta ^ { \ast } } v ) \in S _ { \Pi }$ , it holds that

$$
\mathcal { R } ( \phi _ { \theta ^ { * } } ( t W _ { \theta ^ { * } } v ) ) - \mathcal { R } ( \theta ^ { * } ) \geq \frac { 1 } { L } \| \phi _ { \theta ^ { * } } ( t W _ { \theta ^ { * } } v ) - \theta ^ { * } \| ^ { 2 } \geq \frac { t ^ { 2 } } { L } \| v \| ^ { 2 } .
$$

So let $t \to 0$ , we have $v ^ { T } W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } v \geq \frac { 2 } { L } \| v \| ^ { 2 }$ holds for any $v \in \mathbb { R } ^ { d }$ with $\lVert \boldsymbol { v } \rVert = 1$ , and therefore, $\begin{array} { r } { W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } \succcurlyeq \frac { 2 } { L } I _ { d } } \end{array}$ . Then since $X ^ { ( n ) } \in { \mathcal { A } }$ , we have

$$
\begin{array} { r l } & { \Big \| \displaystyle { W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| } } \\ & { \displaystyle = \Big \| { W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X _ { i } ) \le C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) } \Big \| } \\ & { \displaystyle \lesssim \sqrt { \frac { \log n } { n } } . } \end{array}
$$

When $n$ is sufficiently large, we have $\begin{array} { r } { - W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T ^ { \prime } } g ( X _ { i } , \theta ^ { * } ) \in V _ { \theta ^ { * } } } \end{array}$ . Define

$$
\widehat { \theta ^ { \circ } } ( X ^ { ( n ) } ) = \phi _ { \theta ^ { * } } \big ( - W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \big ) .
$$

For brevity, write ${ \widehat { \theta } } ^ { \diamond } = { \widehat { \theta } } ^ { \diamond } ( X ^ { ( n ) } )$ . Then there exists a constant $C _ { 3 }$ so that

$$
\begin{array} { r l } & { \displaystyle \| \theta ^ { * } - \widehat { \theta ^ { * } } \| = \Big \| \theta ^ { * } - \phi _ { \theta ^ { * } } \big ( - W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \big ) \Big \| } \\ & { \leq \Big \| W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| + C _ { 2 } \Big \| W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) } \\ & { \leq C _ { 3 } \sqrt { \frac { \log n } { n } } . } \end{array}
$$

Step 3: Let $\begin{array} { r } { \mathcal { L } ( X ^ { ( n ) } , \theta ) = \frac { L ( X ^ { ( n ) } , \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \exp \big ( - \alpha _ { n } \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) \big ) } \end{array}$ . Show that for any $h \in B _ { \delta _ { 1 } ( \log n ) ^ { 3 / 2 } } ( 0 _ { d } )$ ,

$$
\left| \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat \theta ^ { * } ) \Big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \right| \leq C \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \cdot ( \| h \| ^ { 3 } + 1 ) .
$$

For any $\theta \in U _ { \theta ^ { * } }$ , set $W _ { \theta } = \mathbf { J } _ { \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } y ) } ( y = W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) )$ . Since $g ( X _ { i } , \theta ) \in T _ { \theta } \mathcal { M }$ , we can rewrite the constraint $\begin{array} { r } { \sum _ { i = 1 } ^ { n } w _ { i } \cdot g ( X _ { i } , \theta ) = 0 _ { D } } \end{array}$ as

$$
\sum _ { i = 1 } ^ { n } w _ { i } \cdot W _ { \theta } ^ { T } g ( X _ { i } , \theta ) = 0 _ { d }
$$

and introducing Lagrange multipliers, the RETEL function can be rewritten as

$$
L ( X ^ { ( n ) } ; \theta ) = \prod _ { i = 1 } ^ { n } \frac { \exp \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) } { \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) } ,
$$

with λ(θ) = arg min Pni=1 exp(ξT W Tθ g(Xi, θ)). Denote $\mathcal { H } _ { 0 } = W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } }$ and $\Delta _ { 0 } = W _ { \theta ^ { * } } ^ { T } \Delta _ { \theta ^ { * } } W _ { \theta ^ { * } }$ We present the following lemma that provides an approximate form to $\lambda ( \theta )$ .

Lemma 6. For any $X ^ { ( n ) } \in { \mathcal { A } }$ , define

$$
\begin{array} { r l } & { \lambda ( \theta ) = \underset { \xi \in \mathbb { R } ^ { d } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \xi ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) ) ; } \\ & { \widetilde { \lambda } ( \theta ) = - \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \big ( \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta } ^ { * } ( X ^ { ( n ) } ) ) \big ) . } \end{array}
$$

Then for any positive constant $\delta$ , there exists a constant $C$ so that for any $\theta \in \mathcal { M }$ with $\lVert \theta - \theta ^ { * } \rVert \leq$   
δ (log n)3/2√ , ，

$$
\| \lambda ( \theta ) - \widetilde \lambda ( \theta ) \| _ { 2 } \leq C \Big ( ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } \Big ( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \Big ) + \| \theta - \theta ^ { * } \| ^ { 2 } \Big ) .
$$

Fix an arbitrary $h \in B _ { \delta _ { 1 } ( \log n ) ^ { 3 / 2 } } ( 0 _ { d } )$ and let $\begin{array} { r } { \theta = \phi _ { \theta ^ { * } } \left( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) \right) } \end{array}$ . It holds that

$$
\Vert \theta - \theta ^ { * } \Vert \leq \Vert \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Vert + C \Vert \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Vert ^ { 2 } \lesssim \frac { \Vert h \Vert } { \sqrt { n } } + \sqrt { \frac { \log n } { n } } \lesssim \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } .
$$

Then we can write

$$
\log \frac { L ( X ^ { ( n ) } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } = \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) - n \cdot \log \Bigg ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) \Bigg ) .
$$

By Lemma 6, we have

$$
\begin{array} { r l } & { \| \lambda ( \theta ) + \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } \frac { h } { \sqrt { n } } \| = \| \lambda ( \theta ) + \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } ( \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) ) \| } \\ & { \qquad \lesssim ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } \Big ( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \Big ) + \| \theta - \theta ^ { * } \| ^ { 2 } } \\ & { \qquad \lesssim ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } \sqrt { \frac { \log n } { n } } \Big ( \frac { \| h \| + \sqrt { \log n } } { \sqrt { n } } \Big ) ^ { \beta _ { 2 } } . } \end{array}
$$

Therefore, using $\| \theta ^ { * } - \widehat { \theta ^ { \circ } } \| \lesssim \sqrt { \frac { \log n } { n } }$ log nn , we can get

$$
\| \lambda ( \theta ) \| \leq \| \lambda ( \theta ) + \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } \frac { h } { \sqrt { n } } \| + \frac { 1 } { \sqrt { n } } \| \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \| \lesssim \Big ( \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 2 } { \beta _ { 1 } } } } { \sqrt { n } } \Big ) ^ { 1 + \beta _ { 2 } } + \frac { \| h \| _ { 2 } } { \sqrt { n } } .
$$

Then we can obtain

$$
\begin{array} { r l } & { \displaystyle \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \big ( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \big ) - 1 - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) - \frac { 1 } { 2 n } \sum _ { i = 1 } ^ { n } \big ( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \big ) ^ { 2 } } \\ & { \displaystyle \leq \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \big ( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \big ) ^ { 3 } \lesssim \| \lambda ( \theta ) \| ^ { 3 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) \| ^ { 3 } \lesssim \| h \| ^ { 2 } n ^ { - \frac { 3 } { 2 } } + \Big ( \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 2 } { \beta _ { 1 } } } } { \sqrt { n } } \Big ) ^ { 3 + 3 } } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle \log \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) \right) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) } } \\ { { \displaystyle ~ - \frac { 1 } { 2 n } \sum _ { i = 1 } ^ { n } \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } + \frac { 1 } { 2 } \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) ^ { 2 } \Bigg | \lesssim \| h \| ^ { 2 } n ^ { - \frac { 3 } { 2 } } + \left( \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta } } } { \sqrt { n } } - \lambda ( \theta ) \right) ^ { \frac { 1 } { 2 } } } } \end{array}
$$

Therefore, it holds for a constant $C$ that,

$$
\begin{array} { r l } & { \left| \log \frac { L ( X ^ { ( n ) } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } + \frac { 1 } { 2 } \displaystyle \sum _ { i = 1 } ^ { n } \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } - \frac { n } { 2 } \Big ( \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) ^ { 2 } \right| } \\ & { \leq C \left\| h \right\| _ { 2 } ^ { 3 } \cdot n ^ { - \frac { 1 } { 2 } } + C n ^ { - \frac { 1 + 3 \beta _ { 2 } } { 2 } } \cdot ( \log n ) ^ { \frac { ( 4 + \beta _ { 1 } ) ( 3 + 3 \beta _ { 2 } ) } { 2 \beta _ { 1 } } } . } \end{array}
$$

For the term of $\begin{array} { r } { \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \left( \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } } \end{array}$ , note that $X ^ { ( n ) } \in \mathcal { A } _ { 4 }$ , so

$$
\begin{array} { r l } & { \bigg | \displaystyle \sum _ { i = 1 } ^ { n } \big ( \lambda \langle \theta \rangle ^ { T } W _ { \theta } ^ { \mathcal { T } } g ( X _ { i } , \theta ) \big ) ^ { 2 } - n \lambda \langle \theta \rangle ^ { T } \Delta _ { 0 } \lambda \langle \theta \rangle \bigg | } \\ & { \le \bigg | \lambda \langle \theta \rangle ^ { T } W _ { \theta } ^ { \mathcal { T } } \displaystyle \sum _ { \le = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { \mathcal { T } } W _ { \theta } \lambda ( \theta ) - n \cdot \lambda \langle \theta \rangle ^ { T } W _ { \theta } ^ { \mathcal { T } } \mathbb { R } [ \sigma ( X , \theta ) g ( X , \theta ) ^ { \mathcal { T } } ] W _ { \theta } \lambda ( \theta ) \bigg | } \\ & { \qquad + \bigg | n \cdot \lambda \langle \theta \rangle ^ { T } W _ { \theta } ^ { \mathcal { T } } \mathbb { E } [ g ( X , \theta ) g ( X , \theta ) ^ { \mathcal { T } } ] W _ { \theta } \lambda ( \theta ) - n \cdot \lambda \langle \theta \rangle ^ { T } W _ { \theta } ^ { \mathcal { T } } \mathbb { E } [ g ( X , \theta ) ^ { \mathcal { T } } ] [ W _ { \theta } \lambda \theta ^ { \mathcal { T } } ] ^ { T } ] [ W _ { \theta } \cdot \lambda \langle \theta } \\ & { \le n \cdot \| \lambda \langle \theta \rangle \| ^ { 2 } \cdot \bigg \| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { \mathcal { T } } - \mathbb { E } [ g ( X , \theta ) g ( X , \theta ) ^ { T } ] \bigg \| _ { \mathbb { F } } } \\ & { \qquad + n \cdot \| \lambda \langle \theta \rangle \| ^ { 2 } \cdot \bigg \| [ W _ { \theta } ^ { \mathcal { T } } \Delta _ { \theta } W _ { \theta } - W _ { \theta } ^ { \mathcal { T } } \Delta _ { \theta } \cdot W _ { \theta } \ast \| _ { \mathbb { F } } } \\ &  \lesssim \bigg ( \displaystyle \frac  \| \partial \mathbf { g } \| _ \end{array}
$$

For the term of $\begin{array} { r } { \frac { n } { 2 } \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) ^ { : 2 } } \end{array}$ . Since $X ^ { ( n ) } \in \mathcal { A } _ { 1 } \cap \mathcal { A } _ { 3 } \cap \mathcal { A } _ { 5 }$ , we have

$$
\begin{array} { r l } & { \displaystyle \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \right\| \leq \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \theta ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \right\| } \\ & { \displaystyle \qquad + \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \right\| + \left\| \mathbb { E } [ g ( X , \theta ) ] - \mathbb { E } [ g ( X , \theta ^ { * } ) ] \right\| \lesssim \sqrt { \frac { \log n } { n } } + \frac { \| h \| } { \sqrt { n } } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \displaystyle \frac { n } { 2 } \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) ^ { 2 } } \\ & { \le \displaystyle \frac { n } { 2 } \cdot \| \lambda ( \theta ) \| ^ { 2 } \cdot \Big \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \Big \| ^ { 2 } \ \lesssim \Big ( \Big ( \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 2 } { \beta _ { 1 } } } } { \sqrt { n } } \Big ) ^ { 1 + \beta _ { 2 } } + \frac { \| h \| _ { 2 } } { \sqrt { n } } \Big ) ^ { 2 } \cdot \big ( \sqrt { \log n } + \| h \| \big ) . } \end{array}
$$

Putting the pieces together, we obtain

$$
\Big | \log \frac { L ( X ^ { ( n ) } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } + n \cdot \lambda ( \theta ) ^ { T } \Delta _ { 0 } \lambda ( \theta ) \Big | \lesssim \Big ( \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + \frac { 1 } { 2 } } } { \sqrt { n } } + \frac { \| h \| } { \sqrt { n } } \Big ) \cdot \Big ( \| h \| ^ { 2 } + \frac { ( \log n ) ^ { \frac { ( 1 + \beta _ { 2 } ) ( 4 + \beta _ { 1 } ) } { 2 \beta _ { 1 } } } } { n ^ { \beta _ { 2 } } } \Big ) .
$$

Together with (28), we obtain

$$
\begin{array} { r l } & { \log \frac { L ( X ^ { ( n ) } ; \hat { \phi } _ { \phi } , \cdot \big ( \frac { W _ { \phi } - h } { \sqrt { n } } + \hat { \psi } _ { \phi } ; \hat { \theta } ^ { * } \big ( \hat { \theta } ^ { * } \big ) \big ) ) } { \langle \frac { N } { n } \rangle ^ { n } } + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \Bigg | } \\ & { \leq | \log \frac { L ( X ^ { ( n ) } ; \hat { \theta } ) } { \langle \frac { N } { n } \rangle ^ { n } } + n \cdot \lambda ( \theta ) ^ { T } \Delta _ { 0 } \lambda ( \theta ) | + | \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h - \frac { n } { 2 } \lambda ( \theta ) ^ { T } \Delta _ { 0 } \lambda ( \theta ) | } \\ & { \lesssim \Big ( \frac { ( \log \eta ) ^ { \frac { n } { \beta } , 1 } } { \sqrt { n } } + \frac { \| h \| } { \sqrt { n } } \Big ) \cdot \Big ( \| h \| ^ { 2 } + \frac { ( \log \eta ) ^ { \frac { ( 1 + \hat { \theta } _ { 2 } ) ^ { 2 } + ( 4 \hat { \theta } ) } { \sqrt { n } } } } { \pi ^ { \beta } } \Big ) } \\ & { \quad + ( ( \log \pi ) ^ { \frac { n } { \beta } } \sqrt { \frac { \log n } { n } } \Big ( \frac { \| h \| + \sqrt { \log n } } { \sqrt { n } } \Big ) ^ { \beta } \Big ) \cdot \Big ( \Big ( \frac { ( \log \eta ) ^ { \frac { 1 } { \beta } , 1 } \hat { \sigma } _ { 1 } } { \sqrt { n } } \Big ) ^ { 1 / \hat { \beta } _ { 2 } } + \frac { \| h \| _ { 2 } } { \sqrt { n } } \Big ) } \\ &  \lesssim \frac  ( \log n ) ^  \frac { n } \end{array}
$$

Furthermore, consider the transformed risk function $\widetilde { \mathcal { R } } : B _ { r } ( 0 _ { d } ) \to \mathbb { R }$ defined by $\begin{array} { r } { \mathcal { \widetilde { R } } ( z ) = } \end{array}$ $\mathcal { R } ( \underline { { \phi } } _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) = \mathbb { E } [ \ell ( X , \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) ]$ . By Assumption 1 and 3, $\widetilde { \mathcal { R } }$ is thrice differentiable and $\nabla \mathcal { R } ( 0 _ { d } ) = 0$ . Therefore,

$$
\Big | \widetilde { \mathcal { R } } \big ( \frac { h } { \sqrt { n } } + W _ { \theta ^ { * } } ^ { T } ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \big ) - \widetilde { \mathcal { R } } ( 0 _ { d } ) \Big | \lesssim \Big \| \frac { h } { \sqrt { n } } + W _ { \theta ^ { * } } ^ { T } ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \Big \| ^ { 2 } \lesssim \frac { \log n } { n } + \frac { \| h \| ^ { 2 } } { n } .
$$

Then using $X ^ { ( n ) } \in \mathcal { A } _ { 6 }$ , we can get

$$
\begin{array} { r l } & { \Big | \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \Big | \leq \Big | n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { * } ) ] \Big | } \\ & { \quad \quad \quad + \big | \mathcal { \widetilde { R } } \big ( \displaystyle \frac { h } { \sqrt { n } } + W _ { \theta ^ { * } } ^ { T } ( \widehat { \theta ^ { \circ } } - \theta ^ { * } ) \big ) - \widetilde { \mathcal { R } } ( 0 _ { d } ) \big | \lesssim \displaystyle \frac { \log n } { n } + \displaystyle \frac { \| h \| ^ { 2 } } { n } . } \end{array}
$$

Collecting the above results and using $\alpha _ { n } \lesssim \sqrt { n }$ , we can finally obtain

$$
\begin{array} { r l } & { \Big | \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \Big | } \\ & { \leq \Big | \log \frac { L \big ( X ^ { ( n ) } ; \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \big ) \big ) } { ( \frac { 1 } { n } ) ^ { n } } + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \Big | + \alpha _ { n } \Big | \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \Big | } \\ & { \lesssim \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \cdot ( \| h \| ^ { 3 } + 1 ) . } \end{array}
$$

Step 4: Show that when $c _ { 2 } \log n \leq \alpha _ { n } \leq c _ { 3 } { \sqrt { n } }$ with sufficiently large $c _ { 2 }$ , for any constant $\delta > 0$ and constant $c _ { 1 } \geq 2$ , it holds for sufficiently large $n$ that $\Pi _ { \mathrm { R P } } \big ( \lVert \theta - \widehat { \theta ^ { \circ } } \rVert \geq \delta | X ^ { ( n ) } \big ) \leq$ $n ^ { - c _ { 1 } }$ .

Since $\| { \widehat { \theta ^ { \circ } } } - \theta ^ { * } \| \leq C { \sqrt { \frac { \log n } { n } } }$ , for any positive constant $\delta$ , there exists $N$ so that when $n \geq N$

$$
\begin{array} { r l } { \mathrm { \mathrm { a p } } ( \| \theta - \widehat { \theta ^ { \circ } } \| _ { 2 } \geq \delta | X ^ { ( n ) } ) \leq \Pi _ { \mathrm { R P } } ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \delta / 2 | X ^ { ( n ) } ) } & { } \\ & { \quad \quad \quad = \frac { \int _ { B _ { \delta / 2 } ( \theta ^ { * } ) ^ { c } \cap S _ { \Pi } } \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) L \left( X ^ { ( n ) } ; \theta \right) \Pi ( \mathrm { d } \theta ) } { \int \exp ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) ) L \left( X ^ { ( n ) } ; \theta \right) \Pi ( \mathrm { d } \theta ) } } \\ & { \quad \quad \quad \quad \quad \quad \quad \int _ { B _ { 1 / n } ( \widehat { \theta ^ { * } } ) ^ { c } \cap S _ { \Pi } } \exp ( - \alpha _ { n } ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) ) L \left( X ^ { ( n ) } ; \theta \right) / ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } \Pi ( \mathrm { d } \theta ) } \\ &  \quad \quad \quad \quad \leq \frac { \int _ { B _ { \widehat { \star } } ( \theta ^ { * } ) ^ { c } \cap S _ { \Pi } } \exp ( - \alpha _ { n } ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) ) L \left( X ^ { ( n ) } ; \theta \right) / ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } \Pi ( \mathrm { d } \theta ) }  \int _ { B _ { 1 / n } ( \widehat { \theta ^ { * } } ) \cap S _ { \Pi } } \exp ( - \alpha _ { n } ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) ) L \left( X ^ { ( n ) } ; \theta \right) / ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } \Pi ( \mathrm \end{array}
$$

For the denominator, by equation (30), there exists positive constant $c , c ^ { \prime }$ such that

$$
\begin{array} { r l } & { \displaystyle \int _ { \theta \in \mathbb { B } _ { 1 / n } ( \widehat { \theta } ^ { \diamond } ) \cap S _ { \Pi } } \exp ( - \alpha _ { n } ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) ) L ( X ^ { ( n ) } ; \theta ) / ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } \Pi ( \mathrm { d } \theta ) } \\ & { \ge c \displaystyle \int _ { \theta \in B _ { 1 / n } ( \widehat { \theta } ^ { \diamond } ) \cap S _ { \Pi } } \Pi ( \mathrm { d } \theta ) } \\ & { \ge \exp ( - c ^ { \prime } \log n ) . } \end{array}
$$

For the numerator, by the assumption that $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq L \left. \theta - \theta ^ { * } \right.$ and $X ^ { ( n ) } \in \mathcal { A } _ { 6 }$ , when $n$ is large enough, it holds for any $\theta \in B _ { \frac { \delta } { 2 } } ( \theta ^ { * } ) ^ { c } \cap S _ { \Pi }$ that ,

$$
\mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \geq \frac { L \delta } { 2 } - C \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta _ { 1 } } } } { \sqrt { n } } \geq \frac { L \delta } { 4 } .
$$

Therefore when $c _ { 2 } \log n \leq \alpha _ { n } \leq c _ { 3 } { \sqrt { n } }$ with sufficiently large $c _ { 2 }$ , it holds that

$$
\mathrm { I } _ { \mathrm { R P } } ( \| \theta - \widehat { \theta ^ { \circ } } \| _ { 2 } \geq \delta | X ^ { ( n ) } ) \leq \mathrm { I } _ { \mathrm { R P } } ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \frac \delta 2 | X ^ { ( n ) } ) \leq \exp ( c ^ { \prime } \log n ) \exp ( - c _ { 2 } L \delta \log n / 4 ) \leq \pi \exp ( \frac \delta 2 | X ^ { ( n ) } ) .
$$

Step 5: Show that for any positive constant $c _ { 1 } \geq 2$ , with for sufficiently large $\delta _ { 1 }$ , for any $h \in \mathbb { R } ^ { d }$ satisfying $\| h \| \ge \delta _ { 1 } ( \log n ) ^ { 3 / 2 }$ and Wθ∗ h√n + ψθ∗ (θb⋄) ∈ Vθ∗ , it holds that $\begin{array} { r } { \log \mathcal { L } \big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta } ^ { \circ } ) \big ) \big ) \leq - 2 c _ { 1 } d \log n . } \end{array}$

Consider the transformed risk function $\widetilde { \mathcal { R } } : B _ { r } ( 0 _ { d } )  \mathbb { R }$ defined by $\begin{array} { r } { \widetilde { \mathcal { R } } ( z ) = \mathcal { R } ( \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) = } \end{array}$ $\mathbb { E } [ \ell ( X , \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) ]$ . Then it can be verified that W Tϕ ∗ (W ∗ z)E[g(X, ϕθ∗ (Wθ∗ z))] and the Hessian matrix of $\widetilde { \mathcal { R } }$ at $0 _ { d }$ is given by $\mathcal { H } _ { 0 }$ . Now take an arbitrary $h \in \mathbb { R } ^ { d }$ with $\| h \| \geq \delta _ { 1 } ( \log n ) ^ { 3 / 2 }$ an e d Wθ∗ h√n + ψθ∗ (θb⋄) ∈ Vθ∗ . Denote θ = ϕθ∗ ( Wθ∗ h√n $\begin{array} { r } { \theta = \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) } \end{array}$ . Then when $\| \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) \| \leq r$ , there exist constant $C , C _ { 1 }$ so that

$$
\begin{array} { r l } & { \big \| W _ { \theta } ^ { T } \mathbb { E } [ g ( X , \theta ) ] - W _ { \theta ^ { * } } ^ { T } \mathbb { E } [ g ( X , \theta ^ { * } ) ] - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \big \| } \\ & { = \big \| \nabla \widetilde { \mathcal { R } } ( W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) ) - \nabla \widetilde { \mathcal { R } } ( 0 _ { d } ) - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \big \| } \\ & { \leq C \| W _ { \theta ^ { * } } ^ { T } ( \theta - \theta ^ { * } ) \| ^ { 2 } \leq C _ { 1 } ( \frac { \| h \| ^ { 2 } } { n } + \frac { \log n } { n } ) . } \end{array}
$$

Moreover, since $\mathcal { H } _ { 0 }$ is positive definite, there exist positive constants $\delta _ { 1 }$ , $\delta _ { 2 }$ and $C _ { 2 }$ such that when $\delta _ { 1 } ( \log n ) ^ { 1 . 5 } \leq \| h \| \leq \delta _ { 2 } \sqrt { n }$ and $\begin{array} { r } { \theta = \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) } \end{array}$ ,

$$
\begin{array} { r l } & { \displaystyle \bigl \| W _ { \theta } ^ { T } \mathbb { E } [ g ( X , \theta ) ] \bigr \| } \\ & { \ge \bigl \| \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \bigr \| - \bigl \| W _ { \theta } ^ { T } \mathbb { E } [ g ( X , \theta ) ] - W _ { \theta ^ { * } } ^ { T } \mathbb { E } [ g ( X , \theta ^ { * } ) ] - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \bigr \| } \\ & { \ge \| \mathcal { H } _ { 0 } ( \frac { h } { \sqrt { n } } + W _ { \theta ^ { * } } ^ { T } ( \widehat \theta ^ { \diamond } - \theta ^ { * } ) ) \| - C _ { 1 } ( \frac { \| h \| ^ { 2 } } { n } + \frac { \log n } { n } ) \ge C _ { 2 } \frac { \| h \| } { \sqrt { n } } . } \end{array}
$$

Then using $X ^ { ( n ) } \in \mathcal { A } _ { 1 } \cap \mathcal { A } _ { 2 } \cap \mathcal { A } _ { 5 }$ , we have, for sufficiently large $n$ that,

$$
\begin{array} { r l } & { \Big \| \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big \| \geq \Big \| W _ { \theta } ^ { T } \mathbb { E } [ g ( X , \theta ) ] \Big \| - \Big \| \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| } \\ & { \qquad - \left\| W _ { \theta } ^ { T } \Big ( \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \theta ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big ) \right\| } \\ & { \qquad \geq \displaystyle \frac { C _ { 2 } } { 2 } \displaystyle \frac { \| h \| } { \sqrt { n } } \geq \frac { C _ { 2 } \delta _ { 1 } } { 2 } \displaystyle \frac { ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } . } \end{array}
$$

Then by

$$
\begin{array} { l } { \displaystyle \log \frac { L ( X ^ { ( n ) } ; \theta ) } { ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } } = \sum _ { i = 1 } ^ { n } p _ { i } ( \theta ) - n \log \frac { 1 } { n } ; } \\ { \displaystyle \sum _ { i = 1 } ^ { n } p _ { i } ( \theta ) W _ { \theta } ^ { T } g ( X _ { i } , \theta ) = 0 _ { d } . } \end{array}
$$

It holds that when $\delta _ { 1 } ( \log n ) ^ { 1 . 5 } \leq \| h \| _ { 2 } \leq \delta _ { 2 } { \sqrt { n } }$ ,

$$
\Big \| \sum _ { i = 1 } ^ { n } \Big ( p _ { i } ( \theta ) - \frac { 1 } { n } \Big ) W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big \| \geq \frac { C _ { 2 } \delta _ { 1 } } { 2 } \frac { ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } .
$$

Then using $X ^ { ( n ) } \in \mathcal { A } _ { 4 }$ , there exists a positive constant $C _ { 3 }$ such that

$$
\sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ) - \frac { 1 } { n } \right) ^ { 2 } \geq \frac { C _ { 2 } \delta _ { 1 } ^ { 2 } } { 4 } \frac { ( \log n ) ^ { 3 } } { n } \cdot \frac { 1 } { \sum _ { i = 1 } ^ { n } \| W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \| ^ { 2 } } \geq C _ { 3 } \delta _ { 1 } ^ { 2 } \frac { ( \log n ) ^ { 3 } } { n ^ { 2 } } .
$$

Define $\begin{array} { r } { q ( p _ { 1 } , \cdots , p _ { n - 1 } ) = \sum _ { i = 1 } ^ { n - 1 } \log p _ { i } + \log ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) } \end{array}$ . The Hessian matrix of function $q$ at point $\left( p _ { 1 } , \cdots , p _ { n - 1 } \right)$ is

$$
\mathcal { H } _ { q } | _ { ( p _ { 1 } , \cdots , p _ { n - 1 } ) } = \mathrm { D i a g } ( - \frac { 1 } { p _ { 1 } ^ { 2 } } , \cdots , - \frac { 1 } { p _ { n - 1 } ^ { 2 } } ) - \frac { 1 } { ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) ^ { 2 } } \mathbf { 1 } _ { ( n - 1 ) \times ( n - 1 ) } ,
$$

where $\mathbf { 1 } _ { ( n - 1 ) \times ( n - 1 ) }$ denotes the $( n - 1 ) \times ( n - 1 )$ matrix with all entries being 1. Let $p = ( p _ { 1 } , \cdots , p _ { n } )$ and $p _ { - n } = \left( p _ { 1 } , \cdots , p _ { n - 1 } \right)$ . If $\| p \| _ { \infty } \geq 3 c _ { 1 } d { \frac { \log n } { n } }$ , then

$$
\sum _ { i = 1 } ^ { n } \log p _ { i } \leq \log { \frac { 3 c _ { 1 } d \log n } { n } } + ( n - 1 ) \log { \frac { 1 - 3 c _ { 1 } d { \frac { \log n } { n } } } { n - 1 } } .
$$

So,

$$
\begin{array} { r l } & { - n \log n - \displaystyle \sum _ { i = 1 } ^ { n } \log p _ { i } \geq - \log \bigl ( 3 c _ { 1 } d \log n \bigr ) - ( n - 1 ) \log \left( \bigl ( 1 - 3 c _ { 1 } d \frac { \log n } { n } \bigr ) \frac { n } { n - 1 } \right) } \\ & { \qquad \geq \frac { 5 } { 2 } c _ { 1 } d \log n . } \end{array}
$$

If $\| p \| _ { \infty } \leq 3 c _ { 1 } d { \frac { \log n } { n } }$ , then when $\delta _ { 1 }$ is large enough, we have $\begin{array} { r } { \sum _ { i = 1 } ^ { n - 1 } ( p _ { i } - \frac { 1 } { n } ) ^ { 2 } \geq \frac { 4 5 c _ { 1 } ^ { 3 } d ^ { 3 } ( \log n ) ^ { 3 } } { n ^ { 2 } } } \end{array}$ , so by mean value theorem,

$$
\begin{array} { r l } & { q ( \frac { 1 } { n } , \cdots , \frac { 1 } { n } ) - q ( p _ { - n } ) } \\ & { \ = - \displaystyle \frac { 1 } { 2 } ( p _ { - n } - \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) ^ { T } \mathcal { H } _ { q } \vert _ { ( c p _ { - n } + ( 1 - c ) \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) } ( p _ { - n } - \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) } \\ & { \ \geq \displaystyle \frac { 5 } { 2 } c _ { 1 } d \log n . } \end{array}
$$

Therefore, it holds that when $\delta _ { 1 } ( \log n ) ^ { 1 . 5 } \leq \| h \| \leq \delta _ { 2 } \sqrt { n }$ ,

$$
\log \frac { L \Big ( X ^ { ( n ) } ; \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( { \widehat { \theta ^ { * } } } ) \big ) \Big ) } { ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } } \leq - \frac { 5 } { 2 } c _ { 1 } d \log n .
$$

Moreover, by $X ^ { ( n ) } \in \mathcal { A } _ { 6 }$ , it holds that

$$
\begin{array} { r l } & { \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) - \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) } \\ & { \geq - C \displaystyle \frac { \log n } { n } - C \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \sqrt { \frac { \log n } { n } } \cdot \| \theta - \theta ^ { * } \| ^ { \beta _ { 2 } } , } \end{array}
$$

then there exists a positive constant $c _ { 3 }$ such that when $\alpha _ { n } \leq c _ { 3 } { \sqrt { n } }$ and $\delta _ { 1 } ( \log n ) ^ { 1 . 5 } \leq \| h \| \leq \delta _ { 2 } \sqrt { n }$

$$
\begin{array} { r l } & { \exp \Bigg ( \log \frac { L \Big ( X ^ { ( n ) } ; \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat \theta ^ { * } ) ) \Big ) } { ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } } - \alpha _ { n } \bigg ( \mathcal { R } _ { n } \Big ( \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat \theta ^ { * } ) \big ) \Big ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \bigg ) \Bigg ) } \\ & { \leq \exp \Bigg ( \log \frac { L \big ( X ^ { ( n ) } ; \theta \big ) } { \big ( \frac { 1 } { n } \big ) ^ { \frac { 1 } { n } } } - \alpha _ { n } \bigg ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) - \mathcal { R } ( \theta ) + \mathcal { R } ( \theta ^ { * } ) \bigg ) \Bigg ) \leq \exp ( - 2 c _ { 1 } d \log n ) . } \end{array}
$$

Then consider the case of $\| h \| > \delta _ { 2 } { \sqrt { n } }$ . Using equation (33) and $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq L \vert \vert \theta - \theta ^ { * } \vert \vert ^ { 2 }$ , there exists a constant $c _ { 2 }$ such that when $\alpha _ { n } \geq c _ { 2 } \log n$ , it holds that

$$
\begin{array} { r l } & { \operatorname* { s p } \bigg ( \log \frac { L \Big ( X ^ { ( n ) } ; \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) ) \Big ) } { ( \frac { 1 } { n } ) ^ { \frac { 1 } { n } } } - \alpha _ { n } \bigg ( \mathcal { R } _ { n } \Big ( \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Big ) \Big ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \bigg ) \bigg ) } \\ & { \leq \exp \Big ( - \alpha _ { n } \big ( \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \big ) + \alpha _ { n } \Big | \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) - \mathcal { R } ( \theta ) + \mathcal { R } ( \theta ^ { * } ) \big | \Big ) \leq \exp ( - 2 c _ { 1 } d \log n ) . } \end{array}
$$

Step 6: Show $\begin{array} { r } { \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| \lesssim \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } + \frac { 1 } { 2 } } } } \end{array}$

Denote ${ \widehat { \theta } } = { \widehat { \theta } } ( X ^ { ( n ) } )$ , using $X ^ { ( n ) } \in \mathcal { A } _ { 6 }$ , we have

$$
n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \widehat { \theta } ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ \ell ( X , \widehat { \theta } ) ] + \mathbb { E } [ \ell ( X , \theta ^ { * } ) ] \Big \vert \leq C _ { 1 } ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \sqrt { \frac { \log n } { n } } \| \widehat { \theta } - \theta ^ { * } \| _ { \mathcal { X } _ { \widehat { X } _ { i } } } \Big )
$$

Moreover, since $\begin{array} { r } { n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \widehat { \theta } ) < n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { * } ) } \end{array}$ , we can get

$$
\frac { 1 } { L } \| \widehat { \theta } - \theta ^ { * } \| ^ { 2 } \leq \mathbb { E } [ \ell ( X , \widehat { \theta } ) ] - \mathbb { E } [ \ell ( X , \theta ^ { * } ) ] \leq C _ { 1 } \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \bigg ( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } + \frac { \log n } { n } \bigg ) ,
$$

and therefore

$$
\| \widehat { \theta } - \theta ^ { * } \| \lesssim \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta _ { 1 } } } } { \sqrt { n } } ,
$$

which implies $\begin{array} { r } { \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| \leq \| \widehat { \theta } - \theta ^ { * } \| + \| \widehat { \theta ^ { \circ } } - \theta ^ { * } \| \lesssim \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta _ { 1 } } } } { \sqrt { n } } } \end{array}$ . Then using Lemma 2, there exist sets $V _ { \widehat { \theta ^ { \circ } } }$ , $U _ { \widehat { \theta ^ { \circ } } }$ so that $T _ { \widehat { \theta ^ { \circ } } } \mathcal { M } \cap B _ { r _ { 1 } } ( 0 _ { D } ) \subseteq V _ { \widehat { \theta ^ { \circ } } } \subseteq T _ { \widehat { \theta ^ { \circ } } } \mathcal { M }$ and $\mathcal { M } \cap B _ { r _ { 1 } } ( \widehat { \theta ^ { \circ } } ) \subset U _ { \widehat { \theta ^ { \circ } } } \subset \mathcal { M }$ . The map $\psi _ { \widehat { \theta ^ { \circ } } } : U _ { \widehat { \theta ^ { \circ } } } \to V _ { \widehat { \theta ^ { \circ } } }$ defined as $\psi _ { \widehat { \theta } ^ { \diamond } } ( \theta ) = \operatorname { P r o j } _ { T _ { \widehat { \theta } ^ { \diamond } } \mathcal { M } } ( \theta - \mathrm { \widehat { \theta } } ^ { \diamondsuit } )$ , admits a inverse, denoted as $\phi _ { \widehat { \theta ^ { \circ } } }$ , which b b b b bis thrice differentiable. Now consider the curve

$$
c ( t ) = \phi _ { \widehat { \theta } ^ { \diamond } } \Big ( t \frac { \psi _ { \widehat { \theta } ^ { \diamond } } ( \widehat { \theta } ) } { \| \psi _ { \widehat { \theta } ^ { \diamond } } ( \widehat { \theta } ) \| } \Big ) .
$$

It holds that $c ( 0 ) = { \widehat { \theta } } ^ { \circ }$ and $c ( \| \psi _ { \widehat { \theta } ^ { \diamond } } ( \widehat { \theta } ) \| ) = \widehat { \theta }$ . Let $\mathcal { \widetilde { H } } _ { \widehat { \theta } ^ { \diamond } }$ be the Jacobian matrix of the map $\theta \mapsto \operatorname { P r o j } _ { T _ { \theta } \mathcal { M } } ( \nabla \overline { { \mathcal { R } } } ( \theta ) )$ at $\theta = { \widehat { \theta } } ^ { \circ }$ , where $\overline { { \mathcal { R } } } ( \cdot )$ is the ambient space extension of $\mathcal { R } ( \cdot )$ . Then denote $P _ { \widehat { \theta } ^ { \circ } }$ as the projection matrix onto $T _ { \widehat { \theta ^ { \circ } } } { \mathcal { M } }$ and $\mathcal { H } _ { \widehat { \theta ^ { \circ } } } = P _ { \widehat { \theta ^ { \circ } } } \widetilde { \mathcal { H } } _ { \widehat { \theta ^ { \circ } } } P _ { \widehat { \theta ^ { \circ } } }$ . Using Assumption 1 and 3, it holds that

$$
\left\| \right\| \mathcal { H } _ { \widehat { \theta } ^ { \circ } } - \mathcal { H } _ { \theta ^ { * } } \left\| \right\| _ { \mathrm { F } } \lesssim \sqrt { \frac { \log n } { n } } .
$$

Moreover, it has been shown in Step 2 that there exists a positive constant $C$ so that $W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } \succcurlyeq$ $C I _ { d }$ . For $W _ { \widehat { \theta ^ { \circ } } } = \mathbf { J } _ { \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } y ) } ( y = W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) )$ , when $n$ is sufficiently large, it holds that $\frac { 1 } { 2 } I _ { d } \preccurlyeq$ $W _ { \widehat { \theta ^ { \circ } } } ^ { T } W _ { \widehat { \theta ^ { \circ } } } \preccurlyeq 2 I _ { d }$ and

$$
W _ { \widehat { \theta ^ { \circ } } } ^ { T } \mathcal { H } _ { \widehat { \theta ^ { \circ } } } W _ { \widehat { \theta ^ { \circ } } } \succcurlyeq \frac { C } { 2 } I _ { d } .
$$

Using second-order Taylor expansion on curves of manifold (see for example (5.26) of [16]), it holds that

$$
\begin{array} { r l } & { \bigg | \mathcal { R } \Big ( c \big ( \| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| \big ) \Big ) - \mathcal { R } ( \widehat { \theta } ^ { \circ } ) - \| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| \cdot \mathbb { E } [ g ( X , \widehat { \theta } ^ { \circ } ) ] ^ { T } c ^ { \prime } ( 0 ) - \frac { \| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| ^ { 2 } } { 2 } \mathbb { E } [ g ( X , \widehat { \theta } ^ { \circ } ) ] ^ { T } c ^ { \prime \prime } ( 0 ) } \\ & { \qquad - \frac { \| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| ^ { 2 } } { 2 } c ^ { \prime } ( 0 ) ^ { T } \mathcal { H } _ { \widehat { \theta } ^ { \circ } } c ^ { \prime } ( 0 ) \bigg ) \leq C \| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| ^ { 3 } , } \end{array}
$$

Moreover, notice that $\| \psi _ { \widehat { \theta } ^ { \circ } } ( \widehat { \theta } ) \| \lesssim \| \widehat { \theta } - \widehat { \theta } ^ { \circ } \|$ and $\begin{array} { r } { \| \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \| \lesssim \| \widehat { \theta ^ { \circ } } - \theta ^ { * } \| \lesssim \sqrt { \frac { \log n } { n } } } \end{array}$ . Using $\begin{array} { r } { c ^ { \prime } ( 0 ) = \frac { \psi _ { \widehat { \theta } ^ { \diamond } } ( \widehat { \theta } ) } { \| \psi _ { \widehat { \theta } ^ { \diamond } } ( \widehat { \theta } ) \| } } \end{array}$ , it holds for a constant $C _ { 1 }$ that

$$
\begin{array} { r l } & { \displaystyle \left. \mathcal { R } ( \widehat { \theta } ) - \mathcal { R } ( \widehat { \theta ^ { \circ } } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ^ { T } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) ] - \frac { 1 } { 2 } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) ^ { T } \mathcal { H } _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \right. } \\ & { \leq C _ { 1 } ( \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 3 } + \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 2 } \sqrt { \frac { \log n } { n } } ) , } \end{array}
$$

Then using $X ^ { ( n ) } \in \mathcal { A } _ { 7 }$ , we have

$$
\begin{array} { r l } & { \displaystyle \left. n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \widehat { \theta } ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \widehat { \theta ^ { \circ } } ) \right. } \\ & { \displaystyle \left. \qquad - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) ^ { T } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) - \mathcal { R } ( \widehat { \theta } ) + \mathcal { R } ( \widehat { \theta ^ { \circ } } ) + \mathbb { E } \big [ g ( X , \widehat { \theta ^ { \circ } } ) ^ { T } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \big ] \right. } \\ & { \displaystyle \leq C _ { 1 } ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \sqrt { \frac { \log n } { n } } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { \beta _ { 2 } + 1 } + \frac { \log n } { n } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| + ( \frac { \log n } { n } ) ^ { 2 } \Big ) . } \end{array}
$$

Furthermore, using $\begin{array} { r } { { \frac { 1 } { 2 } } I _ { d } \prec { W } _ { \widehat { \theta } \circ } ^ { T } { W } _ { \widehat { \theta } \circ } \prec 2 I _ { d } } \end{array}$ and $\begin{array} { r } { W _ { \widehat { \theta } ^ { \circ } } ^ { T } \mathcal { H } _ { \widehat { \theta } ^ { \circ } } W _ { \widehat { \theta } ^ { \circ } } \succcurlyeq \frac { C } { 2 } I _ { d } } \end{array}$ , there exists constants $C _ { 1 } , C _ { 2 }$ such that

$$
\begin{array} { r l } & { ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) ^ { T } \mathcal { H } _ { \widehat { \theta ^ { \circ } } } ( \theta - \widehat { \theta ^ { \circ } } ) } \\ & { \geq \psi _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } ) ^ { T } \mathcal { H } _ { \widehat { \theta ^ { \circ } } } \psi _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } ) - C _ { 1 } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 3 } } \\ & { = \psi _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } ) ^ { T } W _ { \widehat { \theta ^ { \circ } } } ( W _ { \widehat { \theta ^ { \circ } } } ^ { T } W _ { \widehat { \theta ^ { \circ } } } ) ^ { - 1 } W _ { \widehat { \theta ^ { \circ } } } ^ { T } \mathcal { H } _ { \widehat { \theta ^ { \circ } } } W _ { \widehat { \theta ^ { \circ } } } ( W _ { \widehat { \theta ^ { \circ } } } ^ { T } W _ { \widehat { \theta ^ { \circ } } } ) ^ { - 1 } W _ { \widehat { \theta ^ { \circ } } } ^ { T } \psi _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } ) - C _ { 1 } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 3 } } \\ & { \geq \frac { C } { 4 } \| \psi _ { \widehat { \theta ^ { \circ } } } ( \widehat { \theta } ) \| ^ { 2 } - C _ { 1 } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 3 } \geq C _ { 2 } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { 2 } . } \end{array}
$$

We can get

$$
\begin{array} { r l } & { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \delta ( X _ { i } , \tilde { \theta } ^ { \prime \prime } ) ( \tilde { \theta } - \tilde { \theta } ^ { \prime } ) | \geq - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \delta ( X _ { i } , \tilde { \theta } ^ { \prime \prime } ) ^ { \top } ( \tilde { \theta } - \tilde { \theta } ^ { \prime } )  } \\ & {  \sum _ { j } \tilde { \theta } ^ { \top } \tilde { \theta } ^ { \top } \tilde { \theta } ^ { \top } \tilde { \theta } \tilde { \theta } \tilde { \theta } ^ { \top } \tilde { \theta } \tilde { \theta } ^ { \top } - \frac { 1 } { n } | \frac { \tilde { \theta } ^ { \top } } { n } \tilde { \theta } ^ { \top } \tilde { \theta } ^ { \top } \tilde { \theta } \tilde { \theta } \tilde { \theta } ^ { \top } \tilde { \theta } - \tilde { \theta } ^ { \top } \tilde { \theta } \tilde { \theta } ^ { \top }  } \\ & { -  | \Re ( \tilde { \theta } - \mathcal { U } _ { i } ^ { \mathcal { G } } ) - \mathcal { L } | | \Omega ( X _ { i } , \tilde { \theta } ^ { \mathcal { G } } ) ^ { \top } ( \tilde { \theta } - \tilde { \theta } ^ { \prime } ) ^ { \top }  } \\ & { \qquad -  \tilde { \theta } ^ { \top } \tilde { \theta } ^ { \top } ( X _ { i } , \tilde { \theta } ^ { \mathcal { G } } ) + \pi ^ { - 1 } \sum _ { i = 1 } ^ { n } \delta ( X _ { i } , \tilde { \theta } ^ { \mathcal { G } } ) + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \delta ( X _ { i } , \tilde { \theta } ^ { \mathcal { G } } ) ^ { \top } ( \tilde { \theta } - \tilde { \theta } ^ { \prime } ) | } \\ &  \qquad - \alpha ^ { - 1 } \sum _ { i = 1 } ^ { n } \delta ( X _ { i } , \tilde { \theta } ^  \mathcal  \end{array}
$$

Moreover, using $X ^ { ( n ) } \in \mathcal { A } _ { 5 }$ , we have

$$
\Big \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big \| _ { 2 } \leq C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } + 1 } { 2 } } } .
$$

Furthermore,

$$
\begin{array} { r l } & { \displaystyle n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathbb { E } [ g ( X , \widehat { \theta ^ { * } } ) ] - \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big \| } \\ & { \leq \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \Big \| + C \displaystyle \frac { \log n } { n } } \\ & { \leq \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \displaystyle \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| + C _ { 1 } \displaystyle \frac { \log n } { n } } \\ & { = \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) - W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { \mathcal { H } } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \displaystyle \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| + C _ { 1 } \displaystyle \frac { \mathrm { k } } { - \mathrm { c } } } \\ & { - { C _ { 1 } } \displaystyle \frac { \log n } { n } . } \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } & { 2 C _ { 1 } \displaystyle \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } + 1 } { 2 } } } \| \widehat \theta - \widehat \theta ^ { \circ } \| } \\ & { \geq \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat \theta ^ { \circ } ) ^ { T } ( \widehat \theta - \widehat \theta ^ { \circ } ) \right\| } \\ & { \geq \displaystyle \frac { C _ { 2 } } { 2 } \| \widehat \theta - \widehat \theta ^ { \circ } \| ^ { 2 } - C _ { 3 } \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \sqrt { \frac { \log n } { n } } \| \widehat \theta - \widehat \theta ^ { \circ } \| ^ { \beta _ { 2 } + 1 } + \displaystyle \frac { \log n } { n } \| \widehat \theta - \widehat \theta ^ { \circ } \| + ( \frac { \log n } { n } ) ^ { 2 } \Big ) . } \end{array}
$$

So $\begin{array} { r } { \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| \lesssim \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } + 1 } { 2 } } } . } \end{array}$

# Step 7: Summarizing the results.

We have verified in Steps 1-6 the conditions of Lemma 3 with $\begin{array} { r } { \gamma _ { 0 } = \frac { 2 } { \beta _ { 1 } } + 1 } \end{array}$ , $\begin{array} { r } { \gamma _ { 1 } = \frac { \beta _ { 2 } } { 2 } } \end{array}$ , $\gamma _ { 2 } = 3$ and $\Sigma = \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 }$ . Therefore, for any $X ^ { ( n ) } \in { \mathcal { A } }$ , and any positive constants $c _ { 1 }$ , there exists constants $C _ { 0 } , C _ { 1 } , C _ { 2 }$ so that

1. $\begin{array} { r } { \Pi _ { \mathrm { R P } } ( \| \theta - \widehat { \theta ^ { \circ } } \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } | X ^ { ( n ) } ) \leq C _ { 1 } n ^ { - c _ { 1 } } , } \end{array}$

3. for any $f : \mathcal { M } \to \mathbb { R } ^ { p }$ satisfying Assumption B, it holds that

$$
\mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot \mid X ^ { ( n ) } ) , \mathcal { N } \big ( f ( \widehat { \theta ^ { * } } ) , n ^ { - 1 } J _ { f } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } J _ { f } ^ { T } \big ) \Big ) \leq C _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { \beta } } } .
$$

Hence, $\lVert \sqrt { n } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) - \sqrt { n } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta } ) \rVert$ converge to in probability. Since $\sqrt { n } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) =$ $\begin{array} { r } { \mathcal { H } _ { 0 } ^ { - 1 } \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) } \end{array}$ θ  b θ  b, by Slutsky’s Theorem and the central Limit theorem, we can obtain that $\sqrt { n } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta } )$ converges to $\mathcal { N } ( 0 , \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \overline { { \Delta } } _ { \theta ^ { * } } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } )$ in distribution. Using

$$
\mathcal { H } _ { { \boldsymbol { \theta } } ^ { * } } = W _ { { \boldsymbol { \theta } } ^ { * } } W _ { { \boldsymbol { \theta } } ^ { * } } ^ { T } \mathcal { H } _ { { \boldsymbol { \theta } } ^ { * } } W _ { { \boldsymbol { \theta } } ^ { * } } W _ { { \boldsymbol { \theta } } ^ { * } } ^ { T } = W _ { { \boldsymbol { \theta } } ^ { * } } \mathcal { H } _ { 0 } W _ { { \boldsymbol { \theta } } ^ { * } } ^ { T } ,
$$

we conclude that $\sqrt { n } \psi _ { \theta ^ { * } } ( \widehat { \theta } ) = \sqrt { n } W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta } )$ converges to $\mathcal { N } ( 0 , \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } )$ in distribution. Moreover, choosing $f ( \theta ) = W _ { \theta ^ { * } } ^ { T } ( \theta - \theta ^ { * } )$ , we obtain

$$
\begin{array} { r } { \mathbb { V } \bigg ( \big ( W _ { \theta ^ { * } } ^ { T } ( \cdot - \theta ^ { * } ) \big ) _ { \# } [ \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) ] , \mathcal { N } \big ( W _ { \theta ^ { * } } ^ { T } ( \widehat \theta ^ { \circ } - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } \big ) \bigg ) \leq C _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Using $\begin{array} { r } { \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| \leq C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } + \frac { 1 } { 2 } } } } \end{array}$ , we further have

$$
\mathrm { T V } \bigg ( \big ( W _ { \theta ^ { * } } ^ { T } ( \cdot - \theta ^ { * } ) \big ) _ { \# } \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) \vert , \mathcal { N } \big ( W _ { \theta ^ { * } } ^ { T } ( \widehat \theta - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } \big ) \bigg ) \leq C _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

It follows that

$$
\begin{array} { r } { \bigg ( \bigl ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \cdot - \theta ^ { * } ) _ { \# } [ \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) ] , \mathcal { N } \bigl ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \widehat \theta - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \bigr ) \bigg ) \leq C _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } } \end{array}
$$

Furthermore, using $\begin{array} { r } { \Pi _ { \mathrm { R P } } \big ( \lVert \theta - \widehat { \theta ^ { \diamond } } \rVert \geq C _ { 0 } \sqrt { \frac { \log n } { n } } | X ^ { ( n ) } \big ) \leq n ^ { - 1 } } \end{array}$ and $B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } \subseteq U _ { \theta ^ { * } }$ , $B _ { r } ( 0 _ { d } ) \cap \mathcal { M } \subseteq$ $V _ { \theta ^ { * } }$ , we have

$$
\begin{array} { r l } & { \mathrm { T V } \bigg ( \psi _ { \theta ^ { * } \# } [ \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) \vert _ { U _ { \theta ^ { * } } } ] , \mathcal { N } \big ( \psi _ { \theta ^ { * } } ( \widehat \theta ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) \vert _ { V _ { \theta ^ { * } } } \bigg ) } \\ & { \le \mathrm { T V } \bigg ( \big ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \cdot - \theta ^ { * } ) _ { \# } [ \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) ] , \mathcal { N } \big ( \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( \widehat \theta - \theta ^ { * } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) \bigg ) + \frac { 2 } { n } } \\ & { \lesssim \frac { ( \log n ) ^ { \frac { \omega } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

By the invertibility of $\psi _ { \theta ^ { * } } : U _ { \theta ^ { * } } \to V _ { \theta ^ { * } }$ , we have

$$
\mathrm { T V } \bigg ( \Pi _ { \mathrm { R P } } ( \cdot \mid X ^ { ( n ) } ) \big | _ { U _ { \theta ^ { * } } } , \phi _ { \theta ^ { * } \mathcal { H } } \Big [ \mathcal { N } \big ( \psi _ { \theta ^ { * } } ( \widehat { \theta } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) \big | _ { V _ { \theta ^ { * } } } \Big ] \bigg ) \lesssim \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

Finally, using again $\begin{array} { r } { \Pi _ { \mathrm { R P } } ( \| \theta - \widehat \theta ^ { \circ } \| \geq C _ { 0 } \sqrt { \frac { \log n } { n } } | X ^ { ( n ) } ) \leq n ^ { - 1 } } \end{array}$ , we conclude

$$
\mathrm { T V } \bigg ( \Pi _ { \mathrm { R P } } ( \cdot \mid X ^ { ( n ) } ) , \phi _ { \theta ^ { * } \mathcal { H } } \Big [ \mathcal { N } \big ( \psi _ { \theta ^ { * } } ( \widehat { \theta } ) , n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \big ) \big | _ { V _ { \theta ^ { * } } } \Big ] \bigg ) \lesssim \frac { ( \log n ) ^ { \frac { w } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

# E.2 Proof of Corollary 2

Consider events $\mathcal { A }$ defined in the proof of Theorem 2. Then we have $P ( X ^ { ( n ) } \in \mathcal A ) \ge 1 - n ^ { - 2 }$ , and when $X ^ { ( n ) } \in { \mathcal { A } }$ , we have $\begin{array} { r } { \| \widehat { \theta ^ { \diamond } } - \theta ^ { * } \| _ { 2 } \leq C _ { 1 } \sqrt { \frac { \log n } { n } } } \end{array}$ n and ∥θp − θ⋄∥2 ≤ C1 (log n) 1β1 +1β 1 . Moreover, there exists a constant $C _ { 0 }$ so that $\begin{array} { r } { \Pi _ { \mathrm { R P } } \big ( \lVert \theta - \widehat { \theta ^ { \circ } } \rVert \leq C _ { 0 } \sqrt { \frac { \log n } { n } } \big ) \geq 1 - n ^ { - 2 } } \end{array}$ , and using analysis analogous to (22), we can get

$$
\cdot \mathbb { E } _ { \Pi _ { \mathrm { R P } } } \big [ W _ { \theta ^ { * } } ^ { T } ( \theta - \widehat \theta ^ { \circ } ) ( \theta - \widehat \theta ^ { \circ } ) ^ { T } W _ { \theta ^ { * } } \mathbf { 1 } \big ( \| \theta - \widehat \theta ^ { \circ } \| \leq C _ { 0 } \sqrt { \frac { \log n } { n } } \big ) \big ] - \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } \big [ \big \| _ { \mathrm { F } } \lesssim \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } ,
$$

and

$$
\begin{array} { r l } & { \Big \| \pi \cdot \mathbb { E } _ { \mathrm { I n t e r } } \big [ W _ { \hat { \theta } _ { p } ^ { \star } } ^ { \mathcal { P } } ( \theta - \hat { \theta } _ { p } ) ( \theta - \hat { \theta } _ { p } ) ^ { T } W _ { \hat { \theta } _ { p } ^ { \star } } \big ] - \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } \Big \| _ { \Gamma } } \\ & { \leq \Big \| \Big \| \cdot \mathbb { E } _ { \mathrm { I n t e r } } \big [ W _ { \hat { \theta } _ { p } ^ { \star } } ^ { \mathcal { P } } ( \theta - \hat { \theta } _ { p } ) ( \theta - \hat { \theta } _ { p } ) ^ { T } W _ { \hat { \theta } _ { p } ^ { \star } } \big ] \big \| \theta - \hat { \theta } ^ { \star } \big \| \| \boldsymbol { \mathcal { E } } _ { \hat { \theta } _ { p } } \Big \| \frac { \big [ \log n } { n } \big ) \Big ] - \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } \Big \| \Big \| _ { \Gamma } + \frac { C } { n } } \\ & { \leq \Big \| \Big \| \cdot \mathbb { E } _ { \mathrm { I n t e r } } \big [ W _ { \hat { \theta } _ { p } ^ { \star } } ^ { T } ( \theta - \hat { \theta } ^ { \star } ) ( \theta - \hat { \theta } ^ { \star } ) ^ { T } W _ { \hat { \theta } ^ { \star } } \big ] \big \| \theta - \hat { \theta } ^ { \star } \big \| \| \boldsymbol { \mathcal { E } } _ { \hat { \theta } ^ { \star } } \big \| \big \| \theta - \hat { \theta } ^ { \star } \big \| \| \boldsymbol { \mathcal { E } } _ { n } \big ] \Big \| - \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } \Big \| \Big \| _ { \Gamma } + \frac { ( \log n ) } { n } } \\ &  \lesssim \Big \| \Big \| \cdot  \end{array}
$$

where we use the shorthand $\mathbb { E } _ { \Pi _ { \mathrm { R P } } } [ f ( \theta ) ]$ to denote the expectation of $f ( \theta )$ with respect to $\theta \sim \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ . Then using $W _ { \theta ^ { * } } W _ { \theta ^ { * } } { } ^ { T } ( \theta - \widehat { \theta ^ { \diamond } } ) = \psi _ { \theta ^ { * } } ( \theta ) - \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } )$ and $\lVert \psi _ { \theta ^ { * } } ( \theta ) - ( \theta - \theta ^ { * } ) \rVert \leq$ $C \| \theta - \theta ^ { * } \| ^ { 2 }$ , we have

$$
\begin{array} { r l } & { n \cdot \mathbb { E } _ { \Pi _ { \mathrm { R P } } } \big [ \big \| \theta - \widehat { \theta ^ { \circ } } \big \| ^ { 2 } \cdot { \bf 1 } \big ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq C _ { 0 } \sqrt \frac { \log n } { n } \big ) \big ] } \\ & { \leq n \cdot \mathbb { E } _ { \Pi _ { \mathrm { R P } } } \big [ \big \| W _ { \theta ^ { \star } } \big ( \theta - \widehat { \theta ^ { \circ } } \big ) \big \| ^ { 2 } \cdot { \bf 1 } \big ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq C _ { 0 } \sqrt \frac { \log n } { n } \big ) + C \big ( \frac { \log n } { n } \big ) ^ { \frac { 3 } { 2 } } } \\ & { \leq C _ { 1 } . } \end{array}
$$

Therefore, we have

$$
\left. \left. \boldsymbol { n } \cdot \mathbb { E } _ { \Pi _ { \mathrm { R P } } } \big [ W _ { \widehat { \theta } _ { p } } ^ { T } ( \theta - \widehat { \theta } _ { p } ) ( \theta - \widehat { \theta } _ { p } ) ^ { T } W _ { \widehat { \theta } _ { p } } \big ] - \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } \right. \right. _ { \mathrm { F } } \lesssim \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

Furthermore, using (35) and choosing $f ( \theta ) = W _ { \widehat { \theta } _ { p } } ^ { T } ( \theta - \widehat { \theta } _ { p } )$ , we have

$$
\begin{array} { r l } & { \mathrm { T V } ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) , \mathcal { N } ( 0 , n ^ { - 1 } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } ) ) } \\ & { \leq \mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot \vert X ^ { ( n ) } ) , \mathcal { N } \big ( W _ { \hat { \theta } _ { p } } ^ { T } ( \widehat { \theta ^ { * } } - \widehat { \theta } _ { p } ) , n ^ { - 1 } W _ { \hat { \theta } _ { p } } ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } W _ { \hat { \theta } _ { p } } \big ) \Big ) } \\ & { \qquad + \mathrm { T V } \Big ( \mathcal { N } \big ( W _ { \hat { \theta } _ { p } } ^ { T } ( \widehat { \theta ^ { * } } - \widehat { \theta } _ { p } ) , n ^ { - 1 } W _ { \hat { \theta } _ { p } } ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } W _ { \hat { \theta } _ { p } } \big ) , N \big ( 0 , n ^ { - 1 } \mathcal { H } _ { 0 } ^ { - 1 } \Delta _ { 0 } \mathcal { H } _ { 0 } ^ { - 1 } \big ) \Big ) } \\ & { \lesssim \frac { \big ( \log n \big ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Therefore, let $\chi _ { 1 - \alpha } ^ { 2 }$ denote the $1 - \alpha$ quantile of $\chi ^ { 2 } ( d )$ , there exists a constant $C _ { 3 }$ so that

$$
\begin{array} { r l } & { \operatorname { I } _ { \mathrm { R P } } ( \psi _ { \hat { \theta } _ { p } } ( \theta ) ^ { T } \Sigma _ { p } ^ { \dagger } \psi _ { \hat { \theta } _ { p } } ( \theta ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) - C _ { 3 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \Big | X ^ { ( n ) } ) } \\ & { = \Pi _ { \mathrm { R P } } ( \psi _ { \hat { \theta } _ { p } } ( \theta ) ^ { T } W _ { \hat { \theta } _ { p } } \Big ( \mathbb { E } _ { \Pi _ { \mathrm { R P } } } \big [ W _ { \hat { \theta } _ { p } } ^ { T } ( \theta - \hat { \theta } _ { p } ) ( \theta - \hat { \theta } _ { p } ) ^ { T } W _ { \hat { \theta } _ { p } } \big ] \Big ) ^ { - 1 } W _ { \hat { \theta } _ { p } } ^ { T } \psi _ { \hat { \theta } _ { p } } ( \theta ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) - C _ { 3 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \Big | X ^ { ( n ) } \Big ) } \\ &  \leq \Pi _ { \mathrm { R P } } ( n \cdot \psi _ { \hat { \theta } _ { p } } ( \theta ) ^ { T } W _ { \hat { \theta } _ { p } } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \hat { \theta } _ { p } } ^ { T } \psi _ { \hat { \theta } _ { p } } ( \theta ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) - \frac { C _ { 3 } } { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \Big | X ^ { ( n ) } ) \leq \ \end{array}
$$

and similarly,

$$
\Pi _ { \mathrm { R P } } \left( \psi _ { \widehat { \theta } _ { p } } ( \theta ) ^ { T } \Sigma _ { p } ^ { \dagger } \psi _ { \widehat { \theta } _ { p } } ( \theta ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) + C _ { 3 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \left| X ^ { ( n ) } \right. \right) \geq \alpha ,
$$

Which implies $\begin{array} { r } { | q _ { 1 - \alpha } - \chi _ { 1 - \alpha } ^ { 2 } ( d ) | \lesssim \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } } \end{array}$ . Then let ${ \mathcal { P } } ^ { * \otimes n }$ denote the true distribution of the data $X ^ { ( n ) }$ , it holds that

$$
\begin{array} { r l } & { \mathcal { P } ^ { * \otimes n } \left( \left\{ \psi _ { \widehat { \theta } _ { p } } ( \theta ^ { * } ) ^ { T } \Sigma _ { p } ^ { \dag } \psi _ { \widehat { \theta } _ { p } } ( \theta ^ { * } ) \leq q _ { 1 - \alpha } \right\} \cap \mathcal { A } \right) } \\ & { \leq \mathcal { P } ^ { * \otimes n } \big ( \theta ^ { * } \in \{ \theta \in B _ { r } ( \widehat { \theta } _ { p } ) \cap \mathcal { M } : ( \theta - \widehat { \theta } _ { p } ) ^ { T } \Sigma _ { p } ^ { \dag } ( \theta - \widehat { \theta } _ { p } ) \leq q _ { 1 - \alpha } \} \big ) } \\ & { \leq \mathcal { P } ^ { * \otimes n } \left( \left\{ \psi _ { \widehat { \theta } _ { p } } ( \theta ^ { * } ) ^ { T } \Sigma _ { p } ^ { \dag } \psi _ { \widehat { \theta } _ { p } } ( \theta ^ { * } ) \leq q _ { 1 - \alpha } \right\} \cap \mathcal { A } \right) + \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Furthermore, we can obtain that there exist positive constants $c _ { 1 } , c _ { 2 }$ such that

$$
\begin{array} { r l } & { P ^ { * \otimes n } ( \{ n \cdot \psi _ { \theta } \langle \hat { \theta } ^ { * } \rangle ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \hat { \theta } ^ { * } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) - c _ { 2 } \frac { ( \log n ) ^ { \frac { \beta _ { 1 } ^ { 2 } } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \} \cap \mathcal { A } ) } \\ & { \leq P ^ { * \otimes n } ( \{ n \cdot \psi _ { \hat { \theta } ^ { * } } ( \theta ^ { * } ) ^ { T } W _ { \hat { \theta } ^ { * } } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \hat { \theta } ^ { * } } ^ { T } \psi _ { \hat { \theta } ^ { * } } ( \theta ^ { * } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) - c _ { 1 } \frac { ( \log n ) ^ { \frac { \beta _ { 1 } } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \} \cap \mathcal { A } ) } \\ & { \leq P ^ { * \otimes n } ( \{ \tilde { w } _ { \hat { \theta } ^ { * } } ( \theta ^ { * } ) ^ { T } \Sigma _ { P } ^ { \dagger } \tilde { \psi } _ { \hat { \theta } ^ { * } } ( \theta ^ { * } ) \leq q _ { 1 - \alpha } \} \cap \mathcal { A } ) } \\ &  \leq P ^ { * \otimes n } ( \{ n \cdot \psi _ { \hat { \theta } ^ { * } } ( \theta ^ { * } ) ^ { T } W _ { \hat { \theta } ^ { * } } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _  \hat { \theta } \end{array}
$$

Then by $\begin{array} { r } { \widehat { \theta ^ { \diamond } } = - \phi _ { \theta ^ { \ast } } \bigl ( W _ { \theta ^ { \ast } } \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { \ast } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \ast } ) \bigr ) } \end{array}$ , we can obtain that

$$
\begin{array} { r l } & { \displaystyle p ^ { * \otimes n } ( \{ n \cdot \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) + c _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \} \cap \mathcal { A } ) } \\ & { \displaystyle = \mathcal { P } ^ { * \otimes n } ( \{ ( W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) ) ^ { T } \Delta _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) + c _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \} \cap \mathcal { B } ) } \\ &  \leq \mathcal { P } ^ { * \otimes n } ( ( W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) ) ^ { T } \Delta _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) + c _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } }  n ^  \frac { \beta _ { 2 } }  2 \end{array}
$$

Since $\mathbb { E } _ { \mathcal { P } ^ { * } } [ g ( X , \theta ) ] = 0$ and $\mathrm { C o v } _ { \mathcal { P } ^ { * } } ( W _ { \theta ^ { * } } g ( X , \theta ^ { * } ) ) = \Delta _ { 0 }$ , using Berry-Esseen theorem [60], we can obtain that

$$
\begin{array} { r l } & { P ^ { * \otimes n } \big ( \theta ^ { * } \in \{ \theta \in B _ { r } ( \widehat { \theta } _ { p } ) \cap \mathcal { M } : \psi _ { \widehat { \theta } _ { p } } ( \theta ) ^ { T } \Sigma _ { p } ^ { \sharp } \psi _ { \widehat { \theta } _ { p } } ( \theta ) \leq q _ { 1 - \alpha } \} \big ) } \\ & { \leq \mathcal { P } ^ { * \otimes n } \left( \left( W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \right) ^ { T } \Delta _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \leq \chi _ { 1 - \alpha } ^ { 2 } ( d ) + c _ { 2 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \right) } \\ & { \leq 1 - \alpha + c _ { 3 } \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Similarly, we can obtain that

$$
\begin{array} { r l } & { \mathcal { P } ^ { * \otimes n } \big ( \theta ^ { * } \in \{ \theta \in B _ { r } ( \widehat \theta _ { p } ) \cap \mathcal { M } : \psi _ { \widehat \theta _ { p } } ( \theta ) ^ { T } \Sigma _ { p } ^ { \dagger } \psi _ { \widehat \theta _ { p } } ( \theta ) \leq q _ { 1 - \alpha } \} \big ) } \\ & { \quad \geq 1 - \alpha - c _ { 3 } \frac { \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Proof is completed.

# E.3 Proof of Corollary 3

Denote

$$
\begin{array} { r l } & { \ell ( x , \theta ) = - \log p ( x | \theta ) } \\ & { \overline { { \mathcal { R } } } ( \theta ) = \mathbb { E } [ \ell ( x , \theta ) ] , \theta \in \mathbb { R } ^ { D } } \\ & { \mathcal { R } = \overline { { \mathcal { R } } } | _ { \mathcal { M } } } \\ & { g ( x , \theta ) = \mathrm { g r a d } _ { \theta } \ell ( x , \theta ) = P _ { \theta ^ { * } } \nabla _ { \theta } \ell ( x , \theta ) . } \end{array}
$$

Since

$$
\nabla \overline { { \mathcal { R } } } ( \theta ^ { * } ) = \int - \nabla _ { \theta } p ( x | \theta ^ { * } ) \mathrm { d } x = 0 _ { D } ,
$$

using Corollary 5.47 of [15], the Riemannian Hessian matrix $\mathcal { H } _ { \theta ^ { \ast } }$ of $\mathcal { R }$ at $\theta ^ { * }$ satisfies

$$
\mathcal { H } _ { \theta ^ { * } } = P _ { \theta ^ { * } } \mathrm { H e s s i a n } ( \overline { { \mathcal { R } } } ( \theta ^ { * } ) ) P _ { \theta ^ { * } } = P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ,
$$

where Hessian $\mathcal { R } ( \theta ^ { \ast } ) )$ denotes the Euclidean Hessian matrix of $\mathcal { R } ( \cdot )$ at $\theta ^ { * }$ , and $I _ { \theta ^ { * } }$ is the Fisher Information matrix. Then by Assumption 5, it is straightforward to verify that Assumption 3-4 holds with $\beta _ { 2 } = 1$ . Moreover,

$$
\Delta _ { \theta ^ { * } } = \mathbb { E } [ g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } ] = P _ { \theta ^ { * } } \mathbb { E } \left[ \nabla _ { \theta } \ell ( x , \theta ^ { * } ) \nabla _ { \theta } \ell ( x , \theta ^ { * } ) ^ { T } \right] P _ { \theta ^ { * } } = P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ,
$$

$$
\begin{array} { r } { \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } = ( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger } . } \end{array}
$$

The desired result then directly follows from Theorem 2.

# F Proof for Gibbs Posterior

In this section, we prove Theorem 1 and Corollary 1.

# F.1 Proof of Theorem 1

Similar as the proof of Theorem 2, we will use Lemma 3 to show the desired result. We will start with verifying the conditions of Lemma 3. Consider the set $\mathcal { A }$ defined in the proof of Theorem 2, then $P ( X ^ { ( n ) } \in \mathcal A ) \ge 1 - n ^ { - 2 }$ . Moreover, since $\mathcal { M }$ is locally $C _ { r , L } ^ { 3 }$ around $\theta ^ { * }$ , there exists $U _ { \theta ^ { * } } , V _ { \theta * }$ with $B _ { r } ( \theta ) \cap \mathcal { M } \subseteq U _ { \theta ^ { * } } \subseteq \mathcal { M }$ and $B _ { r } ( 0 _ { D } ) \cap T _ { \theta ^ { * } } { \mathcal { M } } \subseteq V _ { \theta ^ { * } } \subset T _ { \theta ^ { * } } { \mathcal { M } }$ , so that $\psi _ { \theta ^ { * } } : U _ { \theta ^ { * } } \to V _ { \theta ^ { * } }$ defined by $\psi _ { \theta ^ { * } } ( x ) = \mathrm { P r o j } _ { T _ { \theta ^ { * } } \mathcal { M } } ( x - \theta ^ { * } )$ is a bijective, where the inverse, denoted by $\phi _ { \theta ^ { * } }$ is thrice Fréchet differentiable. Then it has been show in the proof of Theorem 2 that, there exists a constant $C _ { 2 }$ so that

$$
\operatorname* { s u p } _ { v \in V _ { \theta ^ { * } } } \frac { \| \phi _ { \theta ^ { * } } ( v ) - ( v + \theta ^ { * } ) \| } { \| v \| ^ { 2 } } \leq C _ { 2 } ,
$$

and

$$
\operatorname* { s u p } _ { \theta ^ { \prime } \in U _ { \theta ^ { * } } } \frac { \| \psi _ { \theta ^ { * } } ( \theta ^ { \prime } ) - ( \theta ^ { \prime } - \theta ^ { * } ) \| } { \| \theta ^ { * } - \theta ^ { \prime } \| ^ { 2 } } \leq C _ { 2 } .
$$

Fix an arbitrary $X ^ { ( n ) } \in { \mathcal { A } }$ , and define

$$
\widehat { \theta ^ { \circ } } ( X ^ { ( n ) } ) = \phi _ { \theta ^ { * } } \big ( - W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \big ) .
$$

It has been shown in the proof of Theorem 2 that $\| { \widehat { \theta ^ { \circ } } } - \theta ^ { * } \| \lesssim { \sqrt { \frac { \log n } { n } } }$ log nn . Then it suffices to prove

1. Let $\mathcal { L } ( X ^ { ( n ) } , \theta ) = \exp \big ( - n \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) ) \big )$ . Show that for any $h \in B _ { \delta _ { 1 } ( \log n ) ^ { 3 / 2 } } ( 0 _ { d } )$ ,

$$
\bigg | \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat \theta ^ { \circ } ) \Big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } h \bigg | \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \cdot ( \| h \| ^ { 3 } + 1 ) .
$$

2. For any constant $\delta > 0$ and constant $c _ { 1 } \geq 2$ , it holds for sufficiently large $n$ that $\Pi ( \lVert { \boldsymbol { \theta } } - { \widehat { \boldsymbol { \theta } } } ^ { \circ } \rVert \geq$ $\delta \mid X ^ { ( n ) } ) \leq n ^ { - c _ { 1 } }$ .

3. For any positive constant $c _ { 1 } \geq 2$ , with for sufficiently large $\delta _ { 1 }$ , for any $h \in \mathbb { R } ^ { d }$ satisfying $\| h \| \ge \delta _ { 1 } ( \log n ) ^ { 3 / 2 }$ and $\frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) \in V _ { \theta ^ { * } }$ , it holds that $\begin{array} { r l } { \log \mathcal { L } ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + } & { { } } \end{array}$ $\psi _ { \theta ^ { * } } ( { \widehat { \theta ^ { \diamond } } } ) ) \big ) \leq - 2 c _ { 1 } d \log n$ .

The we can get the desired result by following the Step 7 of the proof of Theorem 2. Now we prove the above three claims. Then fix an arbitrary $h \in B _ { \delta _ { 1 } ( \log n ) ^ { 3 / 2 } } ( 0 _ { d } )$ , denote $\begin{array} { r } { \theta = \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) \big ) } \end{array}$ it holds that

$$
\begin{array} { r l } & { \left\| \theta - \widehat { \theta } ^ { \diamond } - \frac { W _ { \theta ^ { \ast } } h } { \sqrt { n } } \right\| } \\ & { \leq \left\| \frac { W _ { \theta ^ { \ast } } h } { \sqrt { n } } + \psi _ { \theta ^ { \ast } } ( \widehat { \theta } ^ { \diamond } ) + \theta ^ { * } - \theta ) \right\| + \left\| \widehat { \theta } ^ { \diamond } - \theta ^ { * } - \psi _ { \theta ^ { \ast } } ( \widehat { \theta } ^ { \diamond } ) \right\| } \\ & { \lesssim \frac { \log n } { n } + \frac { \| h \| ^ { 2 } } { n } . } \end{array}
$$

Since $X ^ { ( n ) } \in \mathcal { A } _ { 7 }$ ,

$$
\begin{array} { r l } & { \displaystyle - \frac { 1 } { n } \mathcal { L } \big ( X ^ { ( n ) } , \theta \big ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g \big ( X _ { i } , \widehat { \theta ^ { \circ } } \big ) ^ { T } \big ( \theta - \widehat { \theta ^ { \circ } } \big ) - \big ( \mathbb { E } [ \ell ( X , \theta ) ] - \mathbb { E } [ \ell ( X , \widehat { \theta ^ { \circ } } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ^ { T } ( \theta - \widehat { \theta ^ { \circ } } ) ] \big ) } \\ & { \leq C _ { 1 } \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \bigg ( \sqrt { \frac { \log n } { n } } \left\| \theta - \widehat { \theta ^ { \circ } } \right\| ^ { \beta _ { 2 } + 1 } + \frac { \log n } { n } \left\| \theta - \widehat { \theta ^ { \circ } } \right\| + ( \frac { \log n } { n } ) ^ { 2 } \bigg ) \bigg \} } \\ & { \lesssim \frac { \left( \log n \right) ^ { 1 + \frac { 1 } { \beta _ { 1 } } } } { n ^ { 1 + \frac { \beta _ { 2 } } { 2 } } } ( \| h \| ^ { \beta _ { 2 } + 1 } + 1 ) . } \end{array}
$$

Then notice that,

$$
\begin{array} { r l } & { \left| \mathbb { E } [ \ell ( X , \theta ) ] - \mathbb { E } [ \ell ( X , \widehat { \theta ^ { \circ } } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ^ { T } ( \theta - \widehat { \theta ^ { \circ } } ) ] - \frac { 1 } { 2 n } h ^ { T } W _ { \theta ^ { \ast } } ^ { T } \mathcal { H } _ { \theta ^ { \ast } } W _ { \theta ^ { \ast } } h \right| } \\ & { \leq \left| \mathbb { E } [ \ell ( X , \theta ) ] - \mathbb { E } [ \ell ( X , \widehat { \theta ^ { \circ } } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ^ { T } ( \theta - \widehat { \theta ^ { \circ } } ) ] - \frac { 1 } { 2 } ( \theta - \widehat { \theta ^ { \circ } } ) ^ { T } \mathcal { H } _ { \theta ^ { \ast } } ( \theta - \widehat { \theta ^ { \circ } } ) \right| } \\ & { + \left| \frac { 1 } { 2 n } h ^ { T } W _ { \theta ^ { \ast } } ^ { T } \mathcal { H } _ { \theta ^ { \ast } } W _ { \theta ^ { \ast } } h - \frac { 1 } { 2 } ( \theta - \widehat { \theta ^ { \circ } } ) ^ { T } \mathcal { H } _ { \theta ^ { \ast } } ( \theta - \widehat { \theta ^ { \circ } } ) \right| \lesssim \frac { \log n } { n ^ { \frac { 3 } { 2 } } } ( \| h \| ^ { 3 } + 1 ) . } \end{array}
$$

Moreover, since $X ^ { ( n ) } \in \mathcal { A } _ { 5 }$

$$
\begin{array} { r l } & { \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \Big \| } \\ & { = \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big \| } \\ & { \leq C _ { 2 } ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ( \displaystyle \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 2 } } { 2 } } . } \end{array}
$$

Furthermore,

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { n - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathbb { E } [ g ( X , \widehat { \theta ^ { * } } ) ] \Big \| = \Big \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathbb { E } [ g ( X , \widehat { \theta ^ { * } } ) ] - \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big \| } \\ & { \leq \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \Big \| + C \frac { \log n } { n } } \\ & { \leq \Big \| n ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) - W _ { \theta ^ { * } } W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \Big \| + C _ { 1 } ^ { \mathrm { \scriptsize ~ k ~ } } } \\ & { = C _ { 1 } \displaystyle \frac { \log n } { n } . } \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } & { \displaystyle n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) ( \theta - \widehat { \theta ^ { \circ } } ) \| \leq \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) \| \cdot \| \theta - \widehat { \theta ^ { \circ } } \| } \\ & { \displaystyle \lesssim \frac { \| h \| + 1 } { \sqrt { n } } \cdot \Big ( \left\| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \right\| + \left\| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \right\| \Big ) } \\ & { \displaystyle \lesssim ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 2 } } { 2 } } \frac { \| h \| + 1 } { \sqrt { n } } . } \end{array}
$$

Therefore, combining all pieces, we can get

$$
\begin{array} { r l } & { \bigg | \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \Big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \Big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } h \bigg | } \\ & { = \bigg | \log \mathcal { L } \big ( X ^ { ( n ) } , \theta \big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } h \bigg | \lesssim \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \cdot ( \| h \| ^ { 3 } + 1 ) . } \end{array}
$$

For the second claim, Since $\| { \widehat { \theta ^ { \circ } } } - \theta ^ { * } \| \leq C { \sqrt { \frac { \log n } { n } } }$ , for any positive constant $\delta$ , there exists $N$ so that when $n \geq N$ ,

$$
\begin{array} { r l } { \Pi ( \| \theta - \widehat { \theta ^ { \circ } } \| _ { 2 } \geq \delta | X ^ { ( n ) } ) \leq \Pi ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \delta / 2 | X ^ { ( n ) } ) } & { } \\ { = \frac { \int _ { B _ { \hat { \delta } } } ( \theta ^ { * } ) ^ { c } \cap M } { \int \exp \big ( - n \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) ) \big ) \Pi ( \mathrm { d } \theta ) } } & { } \\ { \int \exp \big ( - n \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) ) \big ) \Pi ( \mathrm { d } \theta ) } & { } \\ { \leq \frac { \int _ { B _ { \hat { \delta } } } ( \theta ^ { * } ) ^ { c } \cap M } { \int _ { B _ { 1 / n } ( \widehat { \theta ^ { \circ } } ) \cap M } \exp \big ( - n \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) ) \big ) \Pi ( \mathrm { d } \theta ) } } & { } \end{array}
$$

For the denominator, by equation (38), there exists positive constant $c , c ^ { \prime }$ such that

$$
\begin{array} { r l } & { \displaystyle \int _ { \theta \in \mathbb { B } _ { 1 / n } ( \widehat { \theta ^ { \circ } } ) \cap \mathcal { M } } \exp \big ( - n \cdot ( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) ) \big ) \Pi ( \mathrm { d } \theta ) } \\ & { \geq c \displaystyle \int _ { \theta \in B _ { 1 / n } ( \widehat { \theta ^ { \circ } } ) \cap \mathcal { M } } \Pi ( \mathrm { d } \theta ) } \\ & { \geq \exp ( - c ^ { \prime } \log n ) . } \end{array}
$$

For the numerator, by the assumption that $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq L \| \theta - \theta ^ { * } \| ^ { 2 }$ and $\| \theta ^ { * } - { \widehat { \theta ^ { \circ } } } \| \lesssim { \sqrt { \frac { \log n } { n } } }$ , when $n$ is sufficiently large, there exists a positive constant $c _ { 3 }$ so that for any $\theta \in B _ { \frac { \delta } { 2 } } ( \theta ^ { * } ) ^ { c } \cap { \mathcal { M } }$ , $\mathcal { R } ( \theta ) - \mathcal { R } ( \widehat { \theta ^ { \circ } } ) \geq c _ { 3 }$ . Moreover, since $X ^ { ( n ) } \in \mathcal { A } _ { 6 }$ , for any θ ∈ B δ (θ∗)c ∩ M,

$$
\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta ^ { \circ } } ) \geq c _ { 3 } / 2 . } \end{array}
$$

Therefore, when $n$ is sufficiently large,

$$
\Pi ( \| \theta - \widehat { \theta ^ { \circ } } \| _ { 2 } \geq \delta | X ^ { ( n ) } ) \leq \Pi ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \frac { \delta } { 2 } | X ^ { ( n ) } ) \leq \exp ( c ^ { \prime } \log n ) \exp ( - c _ { 3 } n / 2 ) \leq n ^ { - c _ { 1 } } .
$$

For the last claim, consider any $h \in \mathbb { R } ^ { d }$ with $\| h \| \geq \delta _ { 1 } ( \log n ) ^ { 3 / 2 }$ and $\frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) \in V _ { \theta ^ { * } }$ denote $\begin{array} { r } { \theta = \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) ) } \end{array}$ . If $\theta \not \in B _ { r } ( \theta ^ { * } ) \cap { \mathcal { M } }$ , then using (39), it is straightforward to show that

$$
\log \mathcal { L } \big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \big ) \big ) \leq - 2 c _ { 1 } d \log n .
$$

If $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ , using $X ^ { ( n ) } \in \mathcal { A } _ { 1 } \cap \mathcal { A } _ { 2 } \cap \mathcal { A } _ { 5 } \cap \mathcal { A } _ { 7 }$ , we have

$$
\begin{array} { r l } & { \log \mathcal { L } \big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \big ) \big ) - \big ( \mathbb { E } [ \ell ( X , \theta ) ] } \\ & { \le { \mathcal R } ( \widehat { \theta ^ { * } } ) - { \mathcal R } ( \theta ) + \Big | { \mathcal R } ( \theta ) - { \mathcal R } ( \widehat { \theta ^ { * } } ) - \mathbb { E } [ g ( X , \widehat { \theta ^ { * } } ) ] ( \theta - \widehat { \theta ^ { * } } ) - { \mathcal R } _ { n } ( \theta ) + { \mathcal R } _ { n } ( \widehat { \theta ^ { * } } ) + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { * } } ) } \\ & { + \left\| \theta - \widehat { \theta ^ { * } } \right\| \cdot \left\| \mathbb { E } [ g ( X , \widehat { \theta ^ { * } } ) ] - \mathbb { E } [ g ( X , \theta ^ { * } ) ] - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { * } } ) + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \right\| + \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \right\| ^ { 2 } } \\ & { \le { \mathcal R } ( \widehat { \theta ^ { * } } ) - { \mathcal R } ( \theta ) + C _ { 1 } \frac { \left( \log n \right) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta _ { 1 } } } } { \sqrt { n } } ( \frac { \left\| h \right\| } { \sqrt { n } } ) ^ { \beta _ { 2 } + 1 } . } \end{array}
$$

Moreover,

$$
\begin{array} { r l } & { \mathcal { R } ( \theta ) - \mathcal { R } ( \widehat { \theta ^ { \circ } } ) } \\ & { \geq \mathcal { R } ( \theta ) - \mathcal { R } ( \widehat { \theta ^ { * } } ) + \mathcal { R } ( \widehat { \theta ^ { * } } ) - \mathcal { R } ( \widehat { \theta ^ { * } } ) } \\ & { \geq L \frac { \| h \| ^ { 2 } } { n } - C _ { 1 } \frac { \log n } { n } . } \end{array}
$$

Therefore, when $\delta _ { 1 }$ is large enough, we have

$$
\begin{array} { r l } & { \log \mathcal { L } \big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \big ) \big ) } \\ & { \leq n \cdot \Big ( - L \frac { \| h \| ^ { 2 } } { n } + C _ { 1 } \frac { \log n } { n } + + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 1 } { \beta _ { 1 } } } } { \sqrt { n } } ( \frac { \| h \| } { \sqrt { n } } ) ^ { \beta _ { 2 } + 1 } \Big ) } \\ & { \leq - 2 c _ { 1 } d \log n . } \end{array}
$$

Proof is completed.

# F.2 Proof of Corollary 1

Denote

$$
\begin{array} { r l } & { \ell ( x , \theta ) = - \log p ( x | \theta ) } \\ & { \overline { { \mathcal { R } } } ( \theta ) = \mathbb { E } [ \ell ( x , \theta ) ] , \theta \in \mathbb { R } ^ { D } } \\ & { \mathcal { R } = \overline { { \mathcal { R } } } | _ { \mathcal { M } } } \\ & { g ( x , \theta ) = \mathrm { g r a d } _ { \theta } \ell ( x , \theta ) = P _ { \theta ^ { * } } \nabla _ { \theta } \ell ( x , \theta ) . } \end{array}
$$

Then given Assumption 5, it is straightforward to verify that Assumption 3 and 4 hold with $\beta _ { 2 } = 1$ . Moreover, using (37), we have $\mathcal { H } _ { \theta ^ { \ast } } = P _ { \theta ^ { \ast } } I _ { \theta ^ { \ast } } P _ { \theta ^ { \ast } }$ and $\mathcal { H } _ { 0 } = W _ { \theta ^ { * } } ^ { I ^ { \prime } } I _ { \theta ^ { * } } P _ { \theta ^ { * } }$ . Consider events $\mathcal { A }$ defined in the proof of Theorem 2. Then we have $P ( X ^ { ( n ) } \in \mathcal A ) \ge 1 - n ^ { - 2 }$ . Fix an $X ^ { ( n ) } \in { \mathcal { A } }$ and define

$$
\widehat { \theta } ^ { \diamond } = \widehat { \theta } ^ { \diamond } ( X ^ { ( n ) } ) = \phi _ { \theta ^ { \ast } } \big ( - W _ { \theta ^ { \ast } } ( W _ { \theta ^ { \ast } } ^ { T } \mathcal { H } _ { \theta ^ { \ast } } W _ { \theta ^ { \ast } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { \ast } } ^ { T } g ( X _ { i } , \theta ^ { \ast } ) \big ) .
$$

Then it has been shown in the step 6 of the proof of Theorem 2 that $\begin{array} { r } { \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| \lesssim \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n } } \end{array}$ , where we have taken $\beta _ { 2 } = 1$ . Then using Theorem 1, we have

$$
\Gamma \vee ( f _ { \# } \Pi ( \cdot \vert X ^ { ( n ) } ) , N ( f ( \widehat \theta ) , n ^ { - 1 } \sigma _ { f } ^ { 2 } ) ) \leq C \ \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } , \quad \sigma _ { f } ^ { 2 } = \ \nabla f ( \theta ^ { * } ) ^ { T } ( P _ { \theta ^ { * } } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger } \nabla f ( \theta ^ { * } ) ,
$$

and

$$
\mathrm { T V } ( f _ { \# } \Pi ( \cdot | X ^ { ( n ) } ) , N ( f ( \widehat \theta ^ { \diamond } ) , n ^ { - 1 } \sigma _ { f } ^ { 2 } ) ) \leq C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } .
$$

Now denote

$$
P = I _ { \theta ^ { * } } ( P _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dag } = I _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } .
$$

Then we have for any $\eta \in \mathbb { R } ^ { D }$ ,

$$
\begin{array} { r l } & { \imath = \left( P \eta + \left( I _ { D } - P \right) \eta \right) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } ( P \eta + ( I _ { D } - P ) \eta ) } \\ & { \quad = \eta ^ { T } P ^ { T } I _ { \theta ^ { * } } ^ { - 1 } P \eta + \eta ^ { T } ( I _ { D } - P ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } P \eta + \eta ^ { T } P ^ { T } I _ { \theta ^ { * } } ^ { - 1 } ( I _ { D } - P ) \eta + \eta ^ { T } ( I _ { D } - P ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } ( I _ { D } - P ) \eta } \\ & { \qquad P ^ { T } I _ { \theta ^ { * } } ^ { - 1 } P = W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } I _ { \theta ^ { * } } I _ { \theta ^ { * } } ^ { - 1 } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } } \\ & { \qquad = W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } . } \end{array}
$$

$$
\begin{array} { r l } & { ( I _ { D } - P ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } P = ( I _ { D } - I _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } } \\ & { \qquad = W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } - W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } } \\ & { \qquad = 0 . } \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { \eta ^ { T } I _ { \theta ^ { * } } ^ { - 1 } \eta = \eta ^ { T } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \eta + \eta ^ { T } ( I _ { D } - P ) ^ { T } I _ { \theta ^ { * } } ^ { - 1 } ( I _ { D } - P ) \eta } \\ & { \qquad \geq \eta ^ { T } W _ { \theta ^ { * } } ( W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } } ) ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \eta = \eta ^ { T } ( P _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) ^ { \dagger } \eta . } \end{array}
$$

Hence we have $( P _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } P _ { \theta ^ { * } } ) \preccurlyeq I _ { \theta ^ { * } } ^ { - 1 }$

We now prove the last statement. Let $z _ { \frac { \alpha } { 2 } }$ to be the $\frac { \alpha } { 2 }$ quantile of $\mathcal { N } ( 0 , 1 )$ and let $Z \sim { \mathcal { N } } ( 0 , 1 )$ , there exists a constant $C _ { 1 }$ so that

$$
\begin{array} { r l } & { \Pi \left( f ( \theta ) \geq f ( \widehat { \theta ^ { \circ } } ) + \frac { \sigma _ { f } } { \sqrt { n } } z _ { \frac { \alpha } { 2 } } + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { 1 + \beta _ { 2 } } { 2 } } } | X ^ { ( n ) } \right) } \\ & { \leq P \Big ( Z \geq z _ { \frac { \alpha } { 2 } } + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \Big ) + C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \leq \frac { \alpha } { 2 } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \Pi \left( f ( \theta ) \geq f ( \widehat { \theta ^ { \circ } } ) + \frac { \sigma _ { f } } { \sqrt { n } } z _ { \frac { \alpha } { 2 } } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { 1 + \beta _ { 2 } } { 2 } } } | X ^ { ( n ) } \right) } \\ & { \geq P \Big ( Z \geq z _ { \frac { \alpha } { 2 } } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \Big ) - C \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \geq \frac { \alpha } { 2 } . } \end{array}
$$

So

$$
\left| q _ { \frac { \alpha } { 2 } } ^ { f } - f ( \widehat { \theta ^ { \diamond } } ) - \frac { \sigma _ { f } } { \sqrt { n } } z _ { \frac { \alpha } { 2 } } \right| \leq C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { 1 + \beta _ { 2 } } { 2 } } } .
$$

Similarly, we can show that

$$
\left| q _ { 1 - { \frac { \alpha } { 2 } } } ^ { f } - f ( { \widehat { \theta ^ { \circ } } } ) - { \frac { \sigma _ { f } } { \sqrt { n } } } z _ { 1 - { \frac { \alpha } { 2 } } } \right| \leq C _ { 1 } { \frac { ( \log n ) ^ { { \frac { 1 } { \beta _ { 1 } } } + 1 } } { n ^ { \frac { 1 + \beta _ { 2 } } { 2 } } } } .
$$

Furthermore, let ${ \mathcal { P } } ^ { * \otimes n }$ be the distribution of the data $X ^ { ( n ) }$ , then

$$
\begin{array} { r l } & { \mathcal { P } ^ { * \otimes n } \left( \left\{ q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { * } ) \leq q _ { 1 - \frac { \alpha } { 2 } } ^ { f } \right\} \cap \mathcal { A } \right) } \\ & { \leq \mathcal { P } ^ { * \otimes n } \left( q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { * } ) \leq q _ { z _ { 1 - \frac { \alpha } { 7 } 2 } } ^ { f } \right) } \\ & { \leq \mathcal { P } ^ { * \otimes n } \left( \left\{ q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { * } ) \leq q _ { z _ { 1 - \frac { \alpha } { 7 } 2 } } ^ { f } \right\} \cap \mathcal { A } \right) + \frac { 2 } { n ^ { 2 } } . } \end{array}
$$

For the term $\mathcal { P } ^ { \ast \otimes n } \left( \left\{ q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { \ast } ) \leq q _ { z _ { 1 - \frac { \alpha } { \gamma } 2 } } ^ { f } \right\} \cap \mathcal { A } \right)$ , using qfα − f (θb⋄) − √σfn z α2  ≤ C1 (log n) 1β1 +11+β2 and qf1− α − f (θb⋄) − √σfn z1− α2  ≤ C1 (log n) 1β1 +11+β2 , we can get

$$
\begin{array} { r l } & { { \mathcal { P } } ^ { * \otimes n } \left( \left\{ z _ { \alpha / 2 } + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { \sqrt { n } } { \sigma _ { f } } ( f ( \theta ^ { * } ) - f ( \widehat { \theta ^ { * } } ) \leq z _ { 1 - \frac { \alpha } { 2 } } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \right\} \cap \mathcal { A } \right) } \\ & { \leq { \mathcal { P } } ^ { * \otimes n } \left( \left\{ q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { * } ) \leq q _ { 1 - \alpha / 2 } ^ { f } \right\} \cap \mathcal { A } \right) } \\ & { \leq { \mathcal { P } } ^ { * \otimes n } \left( \left\{ z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { \sqrt { n } } { \sigma _ { f } } ( f ( \theta ^ { * } ) - f ( \widehat { \theta ^ { * } } ) \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \right\} \cap \mathcal { A } \right) . } \end{array}
$$

Moreover, using

$$
\sqrt { n } \cdot W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \hat { \theta } ^ { \diamond } ) = - \mathcal { H } _ { 0 } ^ { - 1 } \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) ,
$$

we have

$$
\begin{array} { r l } & { \Big \| f ( \theta ^ { * } ) - f ( \widehat { \theta ^ { * } } ) - \nabla f ( \theta ^ { * } ) ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } W _ { \theta ^ { * } } ^ { T } \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \Big \| } \\ & { \leq \Big \| f ( \theta ^ { * } ) - f ( \widehat { \theta ^ { * } } ) - \nabla f ( \theta ^ { * } ) ^ { T } ( \theta ^ { * } - \widehat { \theta ^ { * } } ) \Big \| + C \| \theta ^ { * } - \widehat { \theta ^ { * } } \| ^ { 2 } } \\ & { \lesssim \frac { \log n } { n } . } \end{array}
$$

Therefore, denote $\begin{array} { r } { \mathcal { I } = \frac { 1 } { \sigma _ { f } } \nabla f ( \theta ^ { * } ) ^ { T } W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } } \end{array}$ , there exists a constant $C _ { 2 }$ such that

$$
\begin{array} { r l } & { \mathcal { P } ^ { * \otimes n } ( \{ z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { \sqrt { n } } { \sigma _ { f } } ( f ( \theta ^ { * } ) - f ( \widehat { \theta ^ { * } } ) \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \} \cap \mathcal { A } ) } \\ & { \leq \mathcal { P } ^ { * \otimes n } ( \{ z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \mathcal { T } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 2 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \} \cap \mathcal { A } ) } \\ &  \leq \mathcal { P } ^ { * \otimes n } ( z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } \mathcal { T } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 2 } \frac  ( \log n ) ^  \frac { 1 } { \beta _ { 1 } } \end{array}
$$

Since $\mathbb { E } [ W _ { \theta ^ { * } } ^ { T } g ( X , \theta ^ { * } ) ] = 0 _ { d }$ , $\mathrm { C o v } _ { \mathcal { P } ^ { * } } ( W _ { \theta ^ { * } } ^ { T } g ( X , \theta ^ { * } ) ) = W _ { \theta ^ { * } } ^ { T } I _ { \theta ^ { * } } W _ { \theta ^ { * } }$ , we have

$$
\begin{array} { r l } & { \mathbb { E } [ \mathcal { I } W _ { \theta ^ { * } } ^ { T } g ( X , \theta ^ { * } ) ] = 0 } \\ & { \mathrm { C o v } _ { \mathcal { P } ^ { * } } ( \mathcal { I } W _ { \theta ^ { * } } ^ { T } g ( X , \theta ^ { * } ) ) = \mathcal { I } \Delta _ { 0 } \mathcal { I } ^ { T } = 1 . } \end{array}
$$

Then by Berry-Esseen theorem [60], there exist constants $C _ { 3 } , C _ { 4 }$ such that

$$
\begin{array} { r l } & { P ^ { * } \left( \boldsymbol { q } _ { \alpha / 2 } ^ { f } \leq \boldsymbol { f } ( \boldsymbol { \theta } ^ { * } ) \leq \boldsymbol { q } _ { 1 - \frac { \alpha } { 2 } } ^ { f } \right) } \\ & { \leq \mathcal { P } ^ { * } \left( z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } \mathcal { T } W _ { \boldsymbol { \theta } ^ { * } } ^ { \mathcal { T } } g ( X _ { i } , \boldsymbol { \theta } ^ { * } ) \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 2 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \right) + \frac { 2 } { n ^ { 2 } } } \\ & { \leq \mathcal { P } ^ { * } \left( z _ { \alpha / 2 } - C _ { 1 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \leq Z \leq z _ { 1 - \frac { \alpha } { 2 } } + C _ { 2 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } \sigma _ { f } } \right) + C _ { 3 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } } \\ & { = 1 - \alpha + C _ { 4 } \frac { ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Similarly, we can show that there exists a constant $C _ { 5 }$ such that

$$
\begin{array} { r l } & { \mathcal { P } ^ { * } \left( q _ { \alpha / 2 } ^ { f } \leq f ( \theta ^ { * } ) \leq q _ { 1 - \alpha / 2 } ^ { f } \right) } \\ & { } \\ & { \geq 1 - \alpha - C _ { 5 } \frac { \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } + 1 } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

We then get the desired conclusion.

# G Proof for Examples

# G.1 Example 1: Reduced-Rank Multi-Response Regression

We write the parameter matrix as

$$
\theta = { \binom { \theta _ { 1 1 } } { \theta _ { 2 1 } } } \ \theta _ { 2 2 } { \Big ) } , { \mathrm { ~ e q u i v a l e n t l y ~ } } \theta = ( \theta _ { 1 1 } , \theta _ { 2 1 } , \theta _ { 1 2 } , \theta _ { 2 2 } )
$$

The squared error loss for one observation $( X , Y )$ is

$$
\ell ( ( X , Y ) , \theta ) = \frac { 1 } { 2 } ( Y _ { 1 } - \theta _ { 1 1 } X _ { 1 } - \theta _ { 2 1 } X _ { 2 } ) ^ { 2 } + \frac { 1 } { 2 } ( Y _ { 2 } - \theta _ { 1 2 } X _ { 1 } - \theta _ { 2 2 } X _ { 2 } ) ^ { 2 } ,
$$

where $Y = ( Y _ { 1 } , Y _ { 2 } ) ^ { T }$ and $X = ( X _ { 1 } , X _ { 2 } ) ^ { \prime }$ . A direct calculation shows that the population risk $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( ( X , Y ) , \theta ) ]$ satisfies

$$
\begin{array} { r l } & { \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) } \\ & { \ = \displaystyle \frac { 1 } { 2 } \mathbb { E } \big [ ( \theta _ { 1 1 } X _ { 1 } - \theta _ { 2 1 } X _ { 2 } - \theta _ { 1 1 } ^ { * } X _ { 1 } - \theta _ { 2 1 } ^ { * } X _ { 2 } ) ^ { 2 } \big ] + \frac { 1 } { 2 } \mathbb { E } \big [ ( \theta _ { 1 2 } X _ { 1 } - \theta _ { 2 2 } X _ { 2 } - \theta _ { 1 2 } ^ { * } X _ { 1 } - \theta _ { 2 2 } ^ { * } X _ { 2 } ) ^ { 2 } \big ] } \\ & { \ \ge \displaystyle \frac { 1 } { 2 } \| \theta - \theta ^ { * } \| ^ { 2 } . } \end{array}
$$

which guarantees identifiability of the parameter. The gradient takes the form

$$
\nabla _ { \theta } \ell ( ( X , Y ) , \theta ) = \left( \begin{array} { l } { ( \theta _ { 1 1 } X _ { 1 } + \theta _ { 2 1 } X _ { 2 } - Y _ { 1 } ) X _ { 1 } } \\ { ( \theta _ { 1 1 } X _ { 1 } + \theta _ { 2 1 } X _ { 2 } - Y _ { 1 } ) X _ { 2 } } \\ { ( \theta _ { 1 2 } X _ { 1 } + \theta _ { 2 2 } X _ { 2 } - Y _ { 2 } ) X _ { 1 } } \\ { ( \theta _ { 1 2 } X _ { 1 } + \theta _ { 2 2 } X _ { 2 } - Y _ { 2 } ) X _ { 2 } . } \end{array} \right)
$$

Taking expectations, the gram matrix of the score at $\theta ^ { * }$ is give by:

$$
\begin{array} { r } { \mathbb { E } [ \nabla _ { \theta } \ell ( ( X , Y ) , \theta ^ { * } ) \nabla _ { \theta } \ell ( ( X , Y ) , \theta ) ^ { T } ] = \left( \begin{array} { c c c c } { \sum _ { 1 1 } } & { 0 } & { \Sigma _ { 1 2 } } & { 0 } \\ { 0 } & { \Sigma _ { 1 1 } } & { 0 } & { \Sigma _ { 1 2 } } \\ { \Sigma _ { 2 1 } } & { 0 } & { \Sigma _ { 2 2 } } & { 0 } \\ { 0 } & { \Sigma _ { 2 1 } } & { 0 } & { \Sigma _ { 2 2 } . } \end{array} \right) . } \end{array}
$$

The Hessian of the loss at $\theta ^ { * }$ is given by

$$
\mathrm { H e s s } _ { \theta } \ell ( ( X , Y ) , \theta ^ { * } ) = \left( \begin{array} { c c c c } { { X _ { 1 } ^ { 2 } } } & { { X _ { 1 } X _ { 2 } } } & { { 0 } } & { { 0 } } \\ { { X _ { 1 } X _ { 2 } } } & { { X _ { 2 } ^ { 2 } } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { X _ { 1 } ^ { 2 } } } & { { X _ { 1 } X _ { 2 } } } \\ { { 0 } } & { { 0 } } & { { X _ { 1 } X _ { 2 } } } & { { X _ { 2 } ^ { 2 } } } \end{array} \right) .
$$

So $\mathbb { E } [ \mathrm { H e s s } _ { \theta } \ell ( ( X , Y ) , \theta ) ] = I _ { 4 }$ . Since loss function is smooth in $\theta$ , when the parameter space is the Euclidean set of $\mathbb { R } ^ { 4 }$ , Assumption 1-4 are satisfied with $\beta _ { 1 } = \beta _ { 2 } = 1$ . Moreover, the empirical risk minimizer corresponds to ordinary least squares:

$$
( \widehat { \beta } _ { 1 } ^ { T } , \widehat { \beta } _ { 2 } ^ { T } ) ^ { T } = \arg \operatorname* { m i n } _ { \theta \in \mathbb { R } ^ { 4 } } n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( ( \widetilde { X } _ { i } , \widetilde { Y } _ { i } ) , \theta ) , \quad \widehat { \beta } _ { j } = ( \widetilde { X } ^ { T } \widetilde { X } ) \widetilde { X } ^ { T } \widetilde { Y } _ { , j } .
$$

Because $\theta ^ { * }$ belongs to $S _ { \Pi _ { \mathrm { E } } } = \{ \theta \in \mathbb { R } ^ { 4 } : \| \theta \| \le 1 0 0 \}$ , the support of the Euclidean prior $\Pi _ { \mathrm { E } }$ after flattening matrices into vectors. For sufficiently large $n$ , it holds with probability at least $1 - n ^ { - 1 }$ that the OLS estimator $( \widehat { \beta } _ { 1 } ^ { T } , \widehat { \beta } _ { 2 } ^ { T } ) ^ { T }$ also lies in $S _ { \Pi _ { \mathrm { E } } }$ . Hence the empirical risk minimizer over $S _ { \Pi _ { \mathrm { E } } }$ coincides with the OLS solution. Applying Theorem 1, with high probability, for $f ( \theta ) = \theta _ { 1 } - \theta _ { 3 }$ , the posterior satisfies

$$
\mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { E } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) ) , \mathcal { N } \Big ( \widehat { \beta } _ { 1 1 } - \widehat { \beta } _ { 2 1 } , \frac { 2 } { n } \Big ) \Big ) \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } .
$$

In addition, the sampling distribution of the OLS estimator satisfies

$$
\sqrt { n } ( \widehat { \beta } _ { 1 1 } - \widehat { \beta } _ { 2 1 } - ( \beta _ { 1 1 } ^ { * } - \beta _ { 2 1 } ^ { * } ) ) \stackrel { d } {  } \mathcal { N } ( 0 , \Sigma _ { 1 1 } + \Sigma _ { 2 2 } - 2 \Sigma _ { 1 2 } ) .
$$

We now turn to the manifold posterior. Note that the manifold $\overline { { \mathcal { M } } } = \{ \theta \in \mathbb { R } ^ { 2 \times 2 } : \operatorname { R a n k } ( \theta ) = 1 \}$ admits a global parametrization and can be written as

$$
{ \overline { { \mathcal { M } } } } = { \big \{ } \theta = { \binom { \theta _ { 1 1 } \ a \theta _ { 1 1 } } { \theta _ { 1 2 } \ a \theta _ { 1 2 } } } \ : \ ( \theta _ { 1 1 } , \theta _ { 1 2 } ) \neq ( 0 , 0 ) , a \in \mathbb { R } { \big \} } .
$$

Flattening matrices into $\mathbb { R } ^ { 4 }$ , this corresponds to

$$
\mathcal { M } = \left. \theta = ( \theta _ { 1 1 } , \theta _ { 2 1 } , \theta _ { 1 2 } , \theta _ { 2 2 } ) ^ { T } : \left( ^ { \theta _ { 1 1 } \theta _ { 1 2 } } _ { \theta _ { 2 2 } } \right) \in \overline { { \mathcal { M } } } \right. .
$$

At a point $\theta = ( \theta _ { 1 1 } , \theta _ { 2 1 } , a \theta _ { 1 1 } , a \theta _ { 2 1 } ) ^ { T } \in \mathcal { M }$ , the projection matrix $P _ { \theta }$ onto the tangent space $T _ { \theta } \mathcal { M }$ is given by

$$
P _ { \theta } = W _ { \theta } ( W _ { \theta } ^ { T } W _ { \theta } ) ^ { - 1 } W _ { \theta } \mathrm { ~ w i t h ~ } W _ { \theta } = \left( \begin{array} { c c c } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { a } } & { { 0 } } & { { \theta _ { 1 } } } \\ { { 0 } } & { { a } } & { { \theta _ { 2 } } } \end{array} \right) .
$$

At the true parameter $\theta ^ { * } = ( 1 , 1 , 2 , 2 ) ^ { \scriptscriptstyle 2 ^ { \prime } }$ , this gives

$$
P _ { \theta ^ { * } } = \left( { \begin{array} { c c c c } { 0 . 6 } & { 0 . 4 } & { 0 . 2 } & { 0 . 2 } \\ { 0 . 4 } & { 0 . 6 } & { - 0 . 2 } & { 0 . 2 } \\ { 0 . 2 } & { - 0 . 2 } & { 0 . 9 } & { 0 . 1 } \\ { - 0 . 2 } & { 0 . 2 } & { 0 . 1 } & { 0 . 9 } \end{array} } \right) .
$$

By Lemma 4, the manifold $\mathcal { M }$ is locally $C _ { r , L } ^ { 3 }$ -smooth around $\theta ^ { * }$ for constants $r , L > 0$ . Consider the Riemannian gradient

$$
g ( ( X , Y ) , \theta ) = P _ { \theta } \nabla _ { \theta } \ell ( ( X , Y ) , \theta ) .
$$

The corresponding covariance matrix at the truth is

$$
\Delta _ { \theta ^ { * } } = \mathbb { E } [ g ( ( X , Y ) , \theta ^ { * } ) g ( ( X , Y ) , \theta ^ { * } ) ^ { T } ] = P _ { \theta ^ { * } } \left( \begin{array} { c c c c } { \Sigma _ { 1 1 } } & { 0 } & { \Sigma _ { 1 2 } } & { 0 } \\ { 0 } & { \Sigma _ { 1 1 } } & { 0 } & { \Sigma _ { 1 2 } } \\ { \Sigma _ { 2 1 } } & { 0 } & { \Sigma _ { 2 2 } } & { 0 } \\ { 0 } & { \Sigma _ { 2 1 } } & { 0 } & { \Sigma _ { 2 2 } } \end{array} \right) P _ { \theta ^ { * } } .
$$

Since $\mathbb { E } [ \nabla _ { \theta } \ell ( ( X , Y ) , \theta ^ { * } ) ] = 0 _ { 2 }$ , the Riemannian Hessian matrix reduces to

$$
\mathcal { H } _ { \theta ^ { * } } = P _ { \theta ^ { * } } \mathbb { E } [ \mathrm { H e s s } _ { \theta } \ell ( ( X , Y ) , \theta ) ] P _ { \theta ^ { * } } = P _ { \theta ^ { * } } .
$$

So $\mathcal { H } _ { \theta ^ { \ast } } ^ { \dagger } = P _ { \theta ^ { \ast } }$ and $\mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } = \Delta _ { \theta ^ { * } }$ . Thus Assumption 1-4 can be verified for the manifold setting as well with $\beta _ { 1 } = \beta _ { 2 } = 1$ . Now we solve the empirical risk minimizer under the manifold:

$$
\arg \operatorname* { m i n } _ { \theta \in \mathcal { M } } n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( ( \widetilde X _ { i } , \widetilde Y _ { i } ) , \theta ) .
$$

This is equivalent to solving for $( \widehat { \theta } _ { 1 1 } , \widehat { \theta } _ { 2 1 } , \widehat { a } )$ satisfying

$$
\begin{array} { r l } & { \widetilde { X } ^ { T } ( \widetilde { Y } _ { , 1 } + \widetilde { Y } _ { , 2 } - \widetilde { X } ( \widehat { \theta } _ { 1 1 } , \widehat { \theta } _ { 2 1 } ) ^ { T } ( 1 + \widehat { a } ) ) = 0 _ { 2 } } \\ & { ( \widehat { \theta } _ { 1 1 } , \widehat { \theta } _ { 2 1 } ) \widetilde { X } ^ { T } ( \widetilde { Y } _ { , 2 } - \widetilde { X } ( \widehat { \theta } _ { 1 1 } , \widehat { \theta } _ { 2 1 } ) ^ { T } \widehat { a } ) = 0 , } \end{array}
$$

which is

$$
\begin{array} { r l } & { \widehat { a } = \displaystyle \frac { ( \widetilde { Y } _ { 1 } + \widetilde { Y } _ { 2 } ) ^ { T } \widetilde { X } \widehat { \beta } _ { 2 } } { ( \widetilde { Y } _ { 1 } + \widetilde { Y } _ { 2 } ) ^ { T } \widetilde { X } \widehat { \beta } _ { 1 } } } \\ & { \widehat { \theta } _ { 1 1 } = \displaystyle \frac { \widehat { \beta } _ { 1 1 } + \widehat { \beta } _ { 2 1 } } { 1 + \widehat { \alpha } } } \\ & { \widehat { \theta } _ { 2 1 } = \displaystyle \frac { \widehat { \beta } _ { 1 2 } + \widehat { \beta } _ { 2 2 } } { 1 + \widehat { \alpha } } . } \end{array}
$$

Letting $\textstyle { \widehat { s } } = { \frac { 1 - { \widehat { a } } } { 1 + { \widehat { a } } } }$ . Similarly as the Euclidean case, applying Theorem 1 yields that, with high probability, for $f ( \theta ) = \theta _ { 1 } - \theta _ { 3 }$ ,

$$
\mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { M } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) ) , \mathcal { N } \Big ( \widehat { s } ( \widehat { \beta } _ { 1 1 } + \widehat { \beta } _ { 2 1 } ) , \frac { 1 . 1 } { n } \Big ) \Big ) \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } ,
$$

and

$$
\sqrt { n } ( \widehat { s } ( \widehat { \beta } _ { 1 1 } + \widehat { \beta } _ { 2 1 } ) - ( \beta _ { 1 1 } ^ { * } - \beta _ { 2 1 } ^ { * } ) ) \overset { d } {  } \mathcal { N } ( 0 , 0 . 5 2 \Sigma _ { 1 1 } + 0 . 5 8 \Sigma _ { 2 2 } - 0 . 9 2 \Sigma _ { 1 2 } ) .
$$

Applying Theorem 2 then yields,

$$
\mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | ( \widetilde { X } , \widetilde { Y } ) ) , \mathcal { N } \Big ( \widehat { s } ( \widehat { \beta } _ { 1 1 } + \widehat { \beta } _ { 2 1 } ) , \frac { 0 . 5 2 \Sigma _ { 1 1 } + 0 . 5 8 \Sigma _ { 2 2 } - 0 . 9 2 \Sigma _ { 1 2 } } { n } \Big ) \Big ) \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } ,
$$

# G.2 Example 2: Mean Direction of the Von Mises-Fisher Distribution

Let $A ( \kappa ^ { * } ) = \coth \kappa ^ { * } - 1 / \kappa ^ { * }$ , for $X \sim V M F 3 ( \mu ^ { * } , \kappa ^ { * } )$ , the standard moment formula (see for example [35]) are

$$
\mathbb { E } [ X ] = A ( \kappa ^ { * } ) \mu ^ { * } ,
$$

and

$$
\mathbb { E } [ X X ^ { T } ] = \frac { A ( \kappa ^ { * } ) } { \kappa ^ { * } } I _ { 3 } + ( 1 - \frac { 3 \coth \kappa ^ { * } } { \kappa ^ { * } } + \frac { 3 } { ( \kappa ^ { * } ) ^ { 2 } } ) \mu ^ { * } \mu ^ { * T } .
$$

Consider the loss function for one observation $\ell ( X , \theta ) = - \theta ^ { T } X$ . the risk function $\mathcal { R } ( \theta ) =$ $\mathbb { E } [ \ell ( X , \theta ) ] = - A ( \kappa ^ { * } ) \theta ^ { T } \mu ^ { * }$ satisfies for any $\theta \in \mathcal { M } = \mathbb { S } _ { 1 } ^ { 2 }$ that

$$
\mathcal { R } ( \theta ) - \mathcal { R } ( \mu ^ { * } ) = A ( \kappa ^ { * } ) ( ( \mu ^ { * } - \theta ) ^ { T } \mu ^ { * } ) = \frac { A ( \kappa ^ { * } ) } { 2 } \| \mu ^ { * } - \theta \| ^ { 2 } .
$$

Hence the population risk $\mathcal { R }$ is uniquely minimized on $\mathcal { M }$ at $\theta = \mu ^ { * }$ . Moreover, at a point $\theta \in \mathcal { M }$ , the projection matrix $P _ { \theta }$ onto the tangent space $T _ { \theta } \mathcal { M }$ is given by $P _ { \theta } = I _ { 3 } - \theta \theta ^ { T }$ . At $\textstyle \mu ^ { * } = ( { \frac { 1 } { \sqrt { 3 } } } , { \frac { 1 } { \sqrt { 3 } } } , { \frac { 1 } { \sqrt { 3 } } } )$ , this gives

$$
P _ { \mu ^ { * } } = \left( { - 1 / 3 } \quad { - 1 / 3 } \quad { - 1 / 3 } \right) .
$$

Consider the Riemannian gradient

$$
g ( X , \theta ) = P _ { \theta } \nabla _ { \theta } \ell ( X , \theta ) = - P _ { \theta } X = - ( I _ { 3 } - \theta \theta ^ { T } ) X ,
$$

the Gram matrix at $\boldsymbol \theta = \boldsymbol \mu ^ { * }$ is given by

$$
\Delta _ { \mu ^ { * } } = P _ { \mu ^ { * } } \mathbb { E } [ X X ^ { T } ] P _ { \mu ^ { * } } = \frac { A ( \kappa ^ { * } ) } { \kappa ^ { * } } P _ { \mu ^ { * } } .
$$

Moreover, the Riemannian Hessian matrix of the population risk at $\mu ^ { * }$ is

$$
\mathcal { H } _ { \mu ^ { * } } = \mathbb { E } \big [ P _ { \mu ^ { * } } ( \mu ^ { * } X ^ { T } + ( X ^ { T } \mu ^ { * } ) I _ { 3 } ) P _ { \mu ^ { * } } \big ] = A ( \kappa ^ { * } ) P _ { \mu ^ { * } } .
$$

So $\begin{array} { r } { \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } = \frac { 1 } { A ( \kappa ^ { * } ) } P _ { \mu ^ { * } } } \end{array}$ and $\begin{array} { r } { \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } \Delta _ { \theta } \mathcal { H } _ { \theta ^ { * } } ^ { \dagger } = \frac { 1 } { \kappa ^ { * } \underline { { A } } ( \kappa ^ { * } ) } P _ { \mu ^ { * } } } \end{array}$ . Thus Assumption 1-4 d with $\beta _ { 2 } = 1$ , and any $\beta _ { 1 } > 0$ , and here we choose $\beta _ { 1 } = 1$ . The empirical risk minimizer on $\mathcal { M }$ is given by

$$
\arg \operatorname* { m i n } _ { \theta \in \mathcal { M } } - \theta ^ { T } \sum _ { i = 1 } ^ { n } X _ { i } = \frac { \sum _ { i = 1 } ^ { n } X _ { i } } { \Vert \sum _ { i = 1 } ^ { n } X _ { i } \Vert } = \frac { \overline { { X } } } { \Vert \overline { { X } } \Vert } .
$$

Applying Theorem 1 with $f ( \theta ) = \theta _ { 1 }$ yields, with high probability,

$$
\mathrm { T V } \Big ( f _ { \# } \Pi ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \Big ( f \big ( \overline { { X } } / \| \overline { { X } } \| \big ) , n ^ { - 1 } \frac { 2 } { 3 A ( \kappa ^ { * } ) } \Big ) \Big ) \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } ,
$$

and

$$
\sqrt { n } ( f ( \overline { { X } } / \| \overline { { X } } \| ) - f ( \mu ^ { * } ) ) \overset { d } { \to } \mathcal { N } ( 0 , \frac { 2 } { 3 \kappa ^ { * } A ( \kappa ^ { * } ) } ) .
$$

Applying Theorem 2 yields,

$$
\mathrm { T V } \Big ( f _ { \# } \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) , \mathcal { N } \Big ( f \big ( \overline { { X } } / \| \overline { { X } } \| \big ) , n ^ { - 1 } \frac { 2 } { 3 \kappa ^ { * } A ( \kappa ^ { * } ) } \Big ) \Big ) \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } .
$$

# H Proof for Mixing time Bound

In this section, we prove Theorem 3 and Corollary 4 for the mixing time bound of sampling from $\Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } )$ .

# H.1 Proof of Theorem 3

We first consider the mixing time for sampling from a truncated distribution $\mu ^ { * } | _ { K _ { \theta } }$ , where recall $K _ { \theta } = \{ x = \phi _ { \widetilde { \theta } } \big ( W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } \big ) ~ : ~ \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \le R \}$ . Using Assumption B.1, there exists a set of matrices $\widetilde { W } _ { \theta } \in \mathbb { R } ^ { D \times d }$ indexed by $\theta \in \mathcal { M }$ so that (1) the columns of $\widetilde { W _ { \theta } }$ form an orthonormal basis to $T _ { \theta } \mathcal { M }$ ; (2) $\widetilde { W } _ { \widetilde { \theta } } = W _ { \widetilde { \theta } }$ and $\| \widetilde { W } _ { \theta } - \widetilde { W } _ { \widetilde { \theta } } \| _ { \mathrm { F } } \leq L _ { 1 } \| \theta - \widetilde { \theta } \|$ for $\theta \in K _ { \theta }$ and an $n$ -independent constant $L _ { 1 }$ . Then we consider the following equivalent version of the $\zeta$ -lazy RRWM algorithm described in Section 4, which transforms the operations performed in each iteration into the $\mathbb { R } ^ { d }$ space for convenience of analysis.

<table><tr><td>Algorithm 6: Equivalent version of the (-lazy RRWM algorithm to sample from a density μ*(0) on manifold</td></tr><tr><td>Input: Number of iterations L, step size h, initial distribution μo,Wθ ∈ RDxd where for any θ ∈ M, W forms an orthonormal basis for the tangent space of TeM, covariance matrix I∈ RD×D; Sampling 0° from μo; for t←O toL-1 do Generate a uniform random number uo ∈ (0,1); if uo≤ζ then ot+1←0t; else Sample v from N(0,2hWTIWet) and denote its density by Pet (u); if WθtU  Vet then θt+1←θt； else Let y = et (Wθtv); if 0t Uy then θt+1←θt； else Let u&#x27;=WTy（0t); Generate a uniform random number u ∈ (0,1); ）(（et if u&gt; then （ θt+1←θt； else</td></tr></table>

Note that the probability distribution obtained after $k$ steps of the Markov chain defined in Algorithm 6 is same as the probability distribution obtained after $k$ steps of the Markov chain generated by the $\zeta$ -lazy version of RRWM Algorithm defined in Section 4. Then let $\widetilde { \mu } _ { k }$ denotes the probability distribution obtained after $k$ steps of the Markov chain defined in normalized restriction of Algorithm 6 for sampling from $\mu ^ { * }$ to $\mu ^ { * } | _ { K _ { \theta } }$ $K _ { \theta }$ θ , i.e., with initial distribution $\begin{array} { r } { \mu ^ { * } \vert _ { K _ { \theta } } ( A ) = \frac { \mu ^ { * } ( A \cap K _ { \theta } ) } { \mu ^ { * } ( K _ { \theta } } } \end{array}$ $\widetilde { \mu } _ { 0 } = \mu _ { 0 } | _ { K _ { \theta } }$ θ. Define $\mathcal { Q } = \{ z = \sqrt { n } W _ { \widetilde { \theta } } ^ { T } \widetilde { \psi } _ { \widetilde { \theta } } ( \theta )$ . Here, $\mu ^ { * } | _ { K _ { \theta } }$ denotes the : $\theta \in B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } } \}$ , and

$$
Q : B _ { r } ( \widetilde { \theta } ) \cap \mathcal { M }  \mathcal { Q } \mathrm { ~ a s ~ } Q ( \theta ) = \sqrt { n } \cdot W _ { \widetilde { \theta } } ^ { T } \widetilde { \psi } _ { \widetilde { \theta } } ( \theta ) .
$$

We can also define the inverse of $Q$ as

$$
G : \mathcal { Q } \to B _ { r } ( \widetilde { \theta } ) \cap \mathcal { M } \mathrm { a s } G ( z ) = Q ^ { - 1 } ( z ) = \widetilde { \phi } _ { \widetilde { \theta } } \big ( W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } \big ) .
$$

Then when $R \leq C \sqrt { n }$ with small enough $C$ , it holds that $K _ { \theta } \subset B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } }$ . Define $\mu _ { \mathrm { l o c } } ^ { \ast }$ as the push-forward measure $Q _ { \# } ( \mu ^ { * } | _ { K _ { \theta } } )$ , which has a density (with respect to the Lebesgue measure of $\mathbb { R } ^ { d }$ ),

$$
\begin{array} { r } { \iota _ { \mathrm { l o c } } ^ { * } ( z ) = \mu ^ { * } | _ { K _ { \theta } } ( G ( z ) ) \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) \bigr ) } , \quad z \in K = \{ z \in \mathbb { R } ^ { d } : \| ( W _ { \tilde { \theta } } ^ { T } \widetilde { I } W _ { \tilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R \} . } \end{array}
$$

Similarly, denote $\nu _ { k } = Q _ { \# } \widetilde { \mu } _ { k }$ , it has a density (with respect to the Lebesgue measure on $\mathbb { R } ^ { d }$ ):

$$
\nu _ { k } ( z ) = \widetilde { \mu } _ { k } ( G ( z ) ) \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) \bigr ) } , \quad z \in K ,
$$

where we abuse the notation to use $\widetilde { \mu } _ { k }$ to denote its density function with respect to the volume measure of $\mathcal { M }$ . For $x \in \mathcal { M }$ , define $\Omega _ { x } = \{ v \in \mathbb { R } ^ { d } : \widetilde { W } _ { x } v \in \widetilde { V } _ { x } \}$ and

$$
\widetilde { \eta } _ { x } = P ( Z \in \Omega _ { x } ) , \quad Z \sim { \mathcal { N } } ( 0 , \frac { 2 h } { n } \widetilde { W } _ { x } ^ { T } \widetilde { I W } _ { x } ) .
$$

Let $\widetilde { p } _ { x }$ denote the density function of $\begin{array} { r } { \mathcal { N } ( 0 , \frac { 2 h } { n } \widetilde { W } _ { x } ^ { T } \widetilde { I W } _ { x } ) } \end{array}$ . Define $\widetilde { \phi } _ { x } ^ { * } ( \cdot ) = \widetilde { \phi } _ { x } ( \widetilde { W } _ { x } \cdot )$ and $\widetilde { \psi } _ { x } ^ { * } ( \cdot ) =$ $\widetilde { W } _ { x } ^ { T } \widetilde { \psi } _ { x } ( \cdot )$ . We write $p ( x , \cdot )$ as the density of $\begin{array} { r } { ( \widetilde { \phi } _ { x } ^ { * } ) _ { \# } ( \widetilde { p } _ { x } | _ { \Omega _ { x } } ) = ( \widetilde { \phi } _ { x } ^ { * } ) _ { \# } ( \mathcal { N } ( 0 , \frac { 2 h } { n } \widetilde { W } _ { x } ^ { T } \widetilde { I W } _ { x } ) | _ { \Omega _ { x } } ) } \end{array}$ with respect to the volume measure $\mu _ { \mathcal { M } }$ of $\mathcal { M }$ , then we have

$$
p ( x , y ) = \frac { 1 } { \widetilde { \eta } _ { x } } \cdot \widetilde { p } _ { x } ( \widetilde { \psi } _ { x } ^ { * } ( y ) ) \cdot \big ( \operatorname* { d e t } \bigl ( J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } ( y ) ) ^ { T } J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } ( y ) ) \big ) \big ) ^ { - \frac { 1 } { 2 } } \cdot \mathbf { 1 } \big ( y \in \widetilde { \phi } _ { x } ^ { * } ( \Omega _ { x } ) \big ) .
$$

So we can write the transition probability function $\tau$ associated with $\widetilde { \mu } _ { k } \to \widetilde { \mu } _ { k + 1 }$ as

$$
\mathcal { r } ( x , \mathrm { d } y ) = ( 1 - \zeta ) \widetilde { \eta } _ { x } \cdot A ( x , y ) p ( x , y ) \mu _ { M } ( \mathrm { d } y ) + \left( 1 - \int ( 1 - \zeta ) \widetilde { \eta } _ { x } \cdot A ( x , y ) p ( x , y ) \mu _ { M } ( \mathrm { d } y ) \right) \cdot \delta _ { x } ( x , y ) p ( x , y ) \mu _ { M } ( \mathrm { d } y ) ,
$$

where $\delta _ { x } ( \cdot )$ denotes the Dirac measure at $x$ , $\zeta$ is the lazy parameter and $A ( x , y )$ is the acceptance ratio given by

$$
A ( x , y ) = 1 \wedge \frac { \widetilde { \eta } _ { y } \cdot \mu ^ { * } | _ { K _ { \theta } } ( y ) p ( y , x ) } { \widetilde { \eta } _ { x } \cdot \mu ^ { * } | _ { K _ { \theta } } ( x ) p ( x , y ) } ,
$$

and note that when $x \notin \widetilde { U } _ { y }$ , the acceptance ratio $\boldsymbol { \mathcal { A } } ( \boldsymbol { x } , \boldsymbol { y } ) = \boldsymbol { 0 }$ , which is consistent with the algorithm that we will reject the update if $x \notin \widetilde { U } _ { y }$ . Next we will solve the transition probability function $\tau ^ { * }$ for $\nu _ { k } \to \nu _ { k + 1 }$ . Denote $p ^ { * } ( z _ { 1 } , \cdot )$ as the density of $\big ( Q \circ \widetilde { \phi } _ { G ( z _ { 1 } ) } ^ { * } \big ) _ { \# } \big ( \widetilde { p } _ { G ( z _ { 1 } ) } | \Omega _ { G ( z _ { 1 } ) } \big )$ with respect to Lebesgue measure of $\mathbb { R } ^ { d }$ , that is

$$
p ^ { * } ( z _ { 1 } , z _ { 2 } ) = \frac { 1 } { \widetilde { \eta } _ { G ( z _ { 1 } ) } } \cdot \widetilde { p } _ { G ( z _ { 1 } ) } ( \widetilde { \psi } _ { G ( z _ { 1 } ) } ^ { * } \circ G ( z _ { 2 } ) ) \cdot \left| \operatorname* { d e t } \bigl ( \mathbf { J } _ { \widetilde { \psi } _ { G ( z _ { 1 } ) } ^ { * } \circ G } ( z _ { 2 } ) \bigr ) \right| \cdot \mathbf { 1 } \big ( z _ { 2 } \in [ Q \circ \widetilde { \phi } _ { G ( z _ { 1 } ) } ^ { * } ] \big ( \Omega _ { G ( z _ { 1 } ) } \circ G ( z _ { 2 } ) \bigr ) \cdot \mathbf { 1 } \big )
$$

Then define

$$
\alpha ^ { * } ( z _ { 1 } , z _ { 2 } ) = \frac { \widetilde { \eta } _ { G ( z _ { 2 } ) } \cdot p ^ { * } ( z _ { 2 } , z _ { 1 } ) \mu _ { \mathrm { l o c } } ^ { * } ( z _ { 2 } ) } { \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot p ^ { * } ( z _ { 1 } , z _ { 2 } ) \mu _ { \mathrm { l o c } } ^ { * } ( z _ { 1 } ) } ,
$$

The next lemma shows that the acceptance ratio $\mathcal { A } ( G ( z _ { 1 } ) , G ( z _ { 2 } ) )$ is equal to $\mathcal { A } ^ { \ast } ( z _ { 1 } , z _ { 2 } ) =$ $1 \wedge \alpha ^ { * } ( z _ { 1 } , z _ { 2 } )$ .

Lemma 7. For any $z _ { 1 } \in K$ and $z _ { 2 } \in [ Q \circ \widetilde { \phi } _ { G ( z _ { 1 } ) } ^ { * } ] \bigl ( \Omega _ { G ( z _ { 1 } ) } \bigr )$ , we have

$$
\mathbf { \Psi } ^ { * } ( z _ { 1 } , z _ { 2 } ) = 1 \wedge \alpha ^ { * } ( z _ { 1 } , z _ { 2 } ) = 1 \wedge \frac { \widetilde { \eta } _ { G ( z _ { 2 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 2 } ) ) \cdot p ( G ( z _ { 2 } ) , G ( z _ { 1 } ) ) } { \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 1 } ) ) \cdot p ( G ( z _ { 1 } ) , G ( z _ { 2 } ) ) } = \mathcal { A } ( G ( z _ { 1 } ) , G ( z _ { 2 } ) ) .
$$

Therefore, the transition probability function $\tau ^ { * }$ for $\nu _ { k } \to \nu _ { k + 1 }$ is defined as

$$
\begin{array} { r l } & { \mathcal { T } ^ { * } ( z _ { 1 } , \mathrm { d } z _ { 2 } ) = ( 1 - \zeta ) \cdot \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot \mathcal { A } ^ { * } ( z _ { 1 } , z _ { 2 } ) p ^ { * } ( z _ { 1 } , z _ { 2 } ) \mathrm { d } z _ { 2 } } \\ & { \qquad + \left( 1 - \displaystyle \int ( 1 - \zeta ) \cdot \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot \mathcal { A } ^ { * } ( z _ { 1 } , z _ { 2 } ) p ^ { * } ( z _ { 1 } , z _ { 2 } ) \mathrm { d } z _ { 2 } \right) \cdot \delta _ { z _ { 1 } } ( \mathrm { d } z _ { 2 } ) . } \end{array}
$$

Now we show that given the choice of the step size stated in Theorem 3, the $s$ -conductance profile associated $\tau ^ { * }$ or $\tau$ can be lower bounded.

Lemma 8. It holds that the $s$ -conductance profile with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 3 2 M _ { 0 } ^ { 2 } } } \end{array}$ satisfies

$$
\begin{array} { r l } & { \Phi _ { s } ( v ) : = \operatorname* { i n f } \bigg \{ \frac { \int _ { S } { \mathcal { T } } ( x , M \backslash S ) \mu ^ { * } | K _ { \theta } ( \mathrm { d } x ) } { \mu ^ { * } | K _ { \theta } ( S ) - s } | S \subseteq \mathcal { M } , s < \mu ^ { * } | K _ { \theta } ( S ) \leq v \bigg \} } \\ & { \qquad \geq \operatorname* { i n f } \bigg \{ \frac { \int _ { S } { \mathcal { T } } ( x , M \backslash S ) \mu ^ { * } | K _ { \theta } ( \mathrm { d } x ) } { \mu ^ { * } | K _ { \theta } ( S ) } | S \subseteq \mathcal { M } , s < \mu ^ { * } | K _ { \theta } ( S ) \leq v \bigg \} } \\ & { \qquad = \operatorname* { i n f } \bigg \{ \frac { \int _ { S } { \mathcal { T } } ^ { * } ( z , \mathbb { R } ^ { d } \backslash S ) \mu _ { \mathrm { l o c } } ^ { * } ( z ) \mathrm { d } z } { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } | S \subseteq \mathbb { R } ^ { d } , s < \mu _ { \mathrm { l o c } } ^ { * } ( S ) \leq v \bigg \} } \\ & { \qquad \geq C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \bigg \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \bigg \} , } \end{array}
$$

for $v \in [ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } ]$ and an $( n , D , d )$ -independent constant $C$

We can then bound the mixing time using the following lemma, whose directly follows the proof of Lemma 1 in [69] by changing the Lebesgue measure to $\mu _ { \mathcal { M } }$ .

Lemma 9 (Lemma 1 of [69]). Suppose we have a target distribution $\pi ^ { * }$ that is absolutely continuous with respect to $\mu _ { \mathcal { M } }$ . Let $\varepsilon$ be an error tolerance, and let $\pi _ { 0 }$ be a $M _ { 0 }$ -warm distribution of $\pi ^ { * }$ . Consider the Markov chain obtained from the $\zeta$ -lazy version of the RRWM algorithm for sampling from $\pi ^ { * }$ , then its mixing time in $\chi ^ { 2 }$ divergence is bounded as

$$
\tau _ { \mathrm { m i x } } ( \varepsilon , \pi _ { 0 } ) \leq \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { 1 6 \mathrm { d } v } { \zeta \cdot v \Phi _ { s } ^ { 2 } ( v ) } + \int _ { \frac { 1 } { 2 } } ^ { \frac { 4 \sqrt { 2 } } { \varepsilon } } \frac { 6 4 \mathrm { d } v } { \zeta \cdot v \Phi _ { s } ^ { 2 } ( \frac { 1 } { 2 } ) } ,
$$

where $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ , $\begin{array} { r } { \Phi _ { s } ( v ) = \operatorname* { i n f } \left\{ \frac { \int _ { S } { \mathcal { T } } ( x , { \mathcal { M } } \backslash S ) \pi ^ { * } ( \mathrm { d } x ) } { \pi ^ { * } ( S ) - s } \vert S \subseteq { \mathcal { M } } , s < \pi ^ { * } ( S ) \leq v \right\} } \end{array}$ , and $\tau ( \cdot , \cdot )$ represents the transition probability function associated with the considered Markov chain.

Then combining Lemmas 8 and 9, follows equation (18) of [22], we can get a mixing time bound

$$
\operatorname* { m i x } ( \varepsilon , \mu _ { 0 } | \kappa _ { \theta } ) \lesssim \frac { \exp ( 2 \varepsilon _ { 1 } ) } { \zeta } \left\{ \left[ \kappa \cdot \exp ( 3 \varepsilon _ { 1 } ) \cdot \left( d + \log \big ( \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) + \varepsilon _ { 1 } \right) \cdot \log \left( \frac { \log M _ { 0 } } { \varepsilon } \right) \right] \vee \log \big ( M _ { 0 } d \kappa _ { \theta } / \varepsilon \big ) \right\} .
$$

for sampling from $\mu ^ { * } | _ { K _ { \theta } }$ using the $\zeta$ -lazy version of the RRWM algorithm.

Now we investigate the mixing time for sampling from the original distribution $\mu ^ { * }$ . Let $\mu _ { k }$ denote the probability distribution obtained after $k$ steps of the Markov chain obtained Algorithm (6) for sampling from $\mu ^ { * }$ , with initial distribution $\mu _ { 0 }$ . Then transition probability function from $\mu _ { k }$ to $\mu _ { k + 1 }$ can be written as

$$
\overline { { \mathsf { r } } } ( x , \mathrm { d } y ) = ( 1 - \zeta ) \widetilde { \eta } _ { x } \cdot \overline { { A } } ( x , y ) p ( x , y ) \mu _ { M } ( \mathrm { d } y ) + \left( 1 - \int ( 1 - \zeta ) \widetilde { \eta } _ { x } \cdot \overline { { A } } ( x , y ) p ( x , y ) \mu _ { M } ( \mathrm { d } y ) \right) \cdot \delta _ { x } ( x , y ) \mu _ { M } ( \mathrm { d } y ) ,
$$

where $\zeta$ is the lazy parameter and $\overline { { \boldsymbol { A } } } ( \boldsymbol { x } , \boldsymbol { y } )$ is the acceptance ratio given by

$$
\overline { { { \mathcal { A } } } } ( x , y ) = 1 \wedge \frac { \widetilde { \eta } _ { y } \cdot \mu ^ { * } ( y ) p ( y , x ) } { \widetilde { \eta } _ { x } \cdot \mu ^ { * } ( x ) p ( x , y ) } .
$$

Denote $K _ { \theta } ^ { \prime } = \{ \theta = \widetilde { \phi } _ { \widetilde { \theta } } ( \widetilde { W } _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } ) ~ : ~ \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \le R / 2 \}$ . Then for any $x \in K _ { \theta } ^ { \prime }$ , let $Z$ be a

random variable follows $\mathcal { N } ( 0 , I _ { d } )$ , the acceptance probability satisfies that

$$
\begin{array} { r l } & { \bigg | \int ( 1 - \zeta ) \tilde { \eta } _ { x } \cdot \tilde { \mathcal { A } } _ { ( z , x ) } \tilde { y } ( x , y ) \beta ( x , y ) \beta ( x , \eta ) \delta ( \mathrm { d } \bar { y } ) - \int \left\{ 1 - \zeta \right\} \tilde { \eta } _ { x } \cdot \mathcal { A } ( x , y ) \tilde { \eta } ( z , y ) \beta ( x , \eta ) \delta ( \mathrm { d } \bar { y } ) \bigg | } \\ & { = \int _ { X _ { \epsilon } } ( 1 - \zeta ) \tilde { \eta } _ { x } \cdot \tilde { \mathcal { A } } ( x , y ) \gamma ( x , y ) \beta ( x , y ) \tilde { \eta } _ { x } \mathrm { d } \bar { y } ) } \\ & { \le \int _ { X _ { \epsilon } } \tilde { \gamma } _ { x } \cdot \tilde { \eta } _ { x } \cdot \gamma _ { y } | \beta x , \mathrm { d } \bar { y } ) } \\ & { \stackrel { \mathrm { G } } { \le } \int _ { ( x , \bar { x } ^ { * } ) \times 1 } | \psi _ { x } ^ { * } \rangle \tilde { \eta } _ { x } \delta ( \bar { y } ) | \bar { x } | \bar { y } | \bar { x } | \bar { y } \rangle } \\ & { \le \int _ { ( x , \bar { x } ^ { * } ) \times 1 } | \psi _ { x } ^ { * } \rangle \tilde { \eta } _ { x } \delta ( \bar { y } ) | \bar { x } | \bar { y } \rangle - \frac { \eta } { 2 } \delta _ { - } \gamma ( x , y ) | \delta x ( \mathrm { d } \bar { y } ) } \\ & { \le P \bigg ( \| \bar { z } \| ^ { 2 } \le \frac { \eta } { 8 } \| ( \bar { \mathcal { U } } _ { \delta } ^ { 2 } \bar { \mathcal { U } } _ { \delta } ) ^ { 2 } + \bar { ( \bar { \mathcal { U } } _ { \delta } ^ { 2 } \bar { \mathcal { U } } _ { \delta } ^ { 2 } ) } \bar { \eta } _ { x } \rangle \big | \bar { y } \rangle \bigg | } \\ &  \stackrel { \mathrm { G } } { \le } P ( \| \ \end{array}
$$

where $( i )$ is due to that, if $x \in K _ { \theta } ^ { \prime }$ , $y \in \widetilde { U } _ { x }$ and $\| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } \cdot \widetilde { \psi } _ { x } ^ { * } ( y ) \| \le \frac { 1 } { 4 } R / \sqrt { n }$ , then there exist $n$ -independent constants $C _ { 0 } , C _ { 1 } , C _ { 2 }$ so that $\| y - x \| \leq C _ { 0 } R / { \sqrt { n } }$ , $\| x - { \widetilde { \theta } } \| \leq C _ { 0 } R / { \sqrt { n } }$ and

$$
\begin{array} { r l } {  { \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } \widetilde { \psi } _ { \widetilde { \theta } } ^ { * } ( y ) \| \leq \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } ( \widetilde { \psi } _ { \widetilde { \theta } } ^ { * } ( y ) - \widetilde { \psi } _ { \widetilde { \theta } } ^ { * } ( x ) ) \| + \frac { R } { 2 \sqrt { n } } } } \\ & { \leq \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } ( y - x ) \| + C _ { 1 } ( \| y - \widetilde { \theta } \| ^ { 2 } + \| x - \widetilde { \theta } \| ^ { 2 } ) + \frac { R } { 2 \sqrt { n } } } \\ & { \leq \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } \widetilde { \psi } _ { x } ^ { * } ( y ) \| + C _ { 2 } \| y - x \| ^ { 2 } + C _ { 1 } ( \| y - \widetilde { \theta } \| ^ { 2 } + \| x - \widetilde { \theta } \| ^ { 2 } ) + \frac { 1 } { 2 } . } \\ & { \leq R / \sqrt { n } } \end{array}
$$

holds when $\begin{array} { r } { R \leq \frac { \sqrt { n } } { 4 ( 3 C _ { 1 } C _ { 0 } ^ { 2 } + C _ { 2 } C _ { 0 } ^ { 2 } ) } } \end{array}$ ; $( i i )$ uses the Lipschitzness of $\widetilde { W } _ { x }$ with respect to $x$ around $\widetilde { \theta }$ and the last inequality uses $\begin{array} { r } { R ^ { 2 } / h \geq \frac { 3 6 d } { \rho _ { 1 } h } \geq 2 4 \big ( \sqrt { d } + \sqrt { \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } + 5 \varepsilon _ { 1 } } \big ) ^ { 2 } } \end{array}$ given $h \leq c _ { 0 } \rho _ { 2 } ^ { - 1 } ( d +$ $\log ( \frac { M _ { 0 } d \rho _ { 2 } } { \varepsilon \rho _ { 1 } } ) + \varepsilon _ { 1 } \big ) ^ { - 1 }$ for small enough $c _ { 0 }$ . So for any $x \in K _ { \theta } ^ { \prime }$ , and $S \subset K _ { \theta }$ , we have

$$
| \overline { { { \cal T } } } ( x , S ) - { \cal T } ( x , S ) | \leq \exp ( - 5 \varepsilon _ { 1 } ) \cdot \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } .
$$

Then let $\begin{array} { r } { s ~ = ~ \frac { { \varepsilon } ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ . Fix any $S \subset { \mathcal { M } }$ so that $s < \mu ^ { * } ( S ) \le v$ for $v ~ \in ~ [ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } ]$ . Then by $\begin{array} { r } { \mu ^ { * } ( K _ { \theta } ^ { \prime } ) \geq 1 - \exp ( - 5 \varepsilon _ { 1 } ) \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } } \end{array}$ , we have

s 2 $\begin{array} { r } { \mathrm { ~ \ T ~ } _ { 1 } ^ { \prime } \leq s - \mu ^ { * } ( K _ { \theta } ^ { c } ) < \mu ^ { * } ( S \cap K _ { \theta } ) \leq \mu ^ { * } | _ { K _ { \theta } } ( S ) = \mu ^ { * } ( S \cap K _ { \theta } ) / \mu ^ { * } ( K _ { \theta } ) \leq \mu ^ { * } ( S ) / \mu ^ { * } ( K _ { \theta } ) \leq v + s < \mu ^ { * } ( S \cap K _ { \theta } ) , } \end{array}$ < 2v. If $\begin{array} { r } { \frac 1 2 \leq \mu ^ { * } | _ { K _ { \theta ^ { * } } } ( S ) \leq v + s \leq \frac 1 2 + s } \end{array}$ , then since ε216M2 ≤ 116 , we have s < 12 − s ≤ µ∗|Kθ∗ (Kθ\S) ≤ $\frac { 1 } { 2 } < 2 v$ . Then by Lemma 8,

$$
\begin{array} { r l } & { \displaystyle \int _ { K _ { \theta } \cap S } \mathcal { T } ( x , K _ { \theta } \setminus S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } x ) = \int _ { K _ { \theta } \setminus S } \mathcal { T } ( x , K _ { \theta } \cap S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } x ) } \\ & { \ge C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { 2 v } \big ) \Big \} \mu ^ { * } | _ { K _ { \theta } } ( K _ { \theta } \setminus S ) } \\ & { \overset { ( i ) } { \ge } \frac { 1 } { 2 } C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { 2 v } \big ) \Big \} \mu ^ { * } | _ { K _ { \theta } } ( S ) } \\ & { \ge \frac { 1 } { 4 } C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \Big \} \mu ^ { * } | _ { K _ { \theta } } ( S ) , } \end{array}
$$

where $( i )$ uses that $\begin{array} { r } { \mu ^ { * } | _ { K _ { \theta } } ( K _ { \theta } \backslash S ) \geq \frac { 1 } { 2 } - s \geq \frac { 7 } { 1 6 } > \frac { 1 } { 2 } ( \frac { 1 } { 2 } + s ) \geq \frac { 1 } { 2 } \mu ^ { * } | _ { K _ { \theta } } ( S ) } \end{array}$ . If $\mu ^ { * } | _ { K _ { \theta } } ( K _ { \theta } \backslash S ) < \frac { 1 } { 2 }$ then combined with $\mu ^ { * } | _ { K _ { \theta } } ( K _ { \theta } \backslash S ) \le 2 v$ , using Lemma 8, we have

$$
\begin{array} { l } { \displaystyle \int _ { K _ { \theta } \cap S } \mathcal { T } ( \boldsymbol { x } , K _ { \theta } \backslash S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } \boldsymbol { x } ) \geq C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { 2 v } \big ) \Big \} \mu ^ { * } | _ { K _ { \theta } } ( \boldsymbol { x } ) | _ { K _ { \theta } } } \\ { \geq \frac { 1 } { 4 } C \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \Big \} \mu ^ { * } | _ { K _ { \theta } } ( \boldsymbol { x } ) | _ { K _ { \theta } } } \end{array}
$$

For the right hand side, we further have

$$
\mu ^ { * } | _ { K _ { \theta } } ( S ) \geq \mu ^ { * } ( S ) - \frac { s } { 2 } \geq \frac { 1 } { 2 } \mu ^ { * } ( S ) .
$$

For the left hand side, we further have

$$
\begin{array} { r l } & { \displaystyle \int _ { S } \overline { { \tau } } ( x , \mathcal { M } \backslash S ) \mu ^ { * } ( \mathrm { d } x ) - \int _ { K _ { \theta } \cap S } \mathcal { T } ( x , K _ { \theta } \backslash S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } x ) } \\ & { \displaystyle \geq \int _ { S \cap K _ { \theta } ^ { * } } \overline { { \tau } } ( x , K _ { \theta } \backslash S ) \mu ^ { * } ( \mathrm { d } x ) - \int _ { K _ { \theta } \cap S } \mathcal { T } ( x , K _ { \theta } \backslash S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } x ) } \\ & { \displaystyle \geq \int _ { S \cap K _ { \theta } ^ { * } } \overline { { \tau } } ( x , K _ { \theta } \backslash S ) \mu ^ { * } ( \mathrm { d } x ) - \int _ { S \cap K _ { \theta } ^ { * } } \mathcal { T } ( x , K _ { \theta } \backslash S ) \mu ^ { * } | _ { K _ { \theta } } ( \mathrm { d } x ) - \mu ^ { * } | _ { K _ { \theta } } ( K _ { \theta } \backslash K _ { \theta } ^ { \prime } ) } \\ & { \displaystyle \geq - \exp ( - 5 \varepsilon _ { 1 } ) \cdot \frac { 3 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } , } \end{array}
$$

where the last inequality uses equation (41) and $\begin{array} { r } { \mu ^ { * } ( K _ { \theta } ^ { \prime } ) \geq 1 - \exp ( - 5 \varepsilon _ { 1 } ) \cdot \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } } \end{array}$ Then by equation (43), we have

$$
\int _ { S } \overline { { { \mathcal { T } } } } ( x , \mathcal { M } \backslash S ) \mu ^ { * } ( \mathrm { d } x ) + \exp ( - 5 \varepsilon _ { 1 } ) \cdot \frac { 3 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } \geq \frac { C \exp ( - 2 \varepsilon _ { 1 } ) } { 8 } \operatorname* { m i n } \left\{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \left( 1 + \exp ( - 3 \varepsilon _ { 1 } ) \right) \right\} .
$$

Using $\begin{array} { r } { \mu ^ { * } ( S ) \geq s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ ε 16M 2 , we have

$$
\int _ { S } \overline { { { T } } } ( x , \mathcal { M } \backslash S ) \mathrm { d } \mu ^ { * } ( x ) \geq \frac { C \exp ( - 2 \varepsilon _ { 1 } ) } { 1 6 } \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \Big \} \mu ^ { * } ( S ) .
$$

Taking infimum over $S$ , we can obtain that

$$
\begin{array} { r l } & { \operatorname* { i n f } \bigg \{ \frac { \int _ { S } \overline { { \mathcal { T } } } ( x , \mathcal { M } \backslash S ) \mathrm { d } \mu ^ { * } ( x ) } { \mu ^ { * } ( S ) - s } | S \subseteq \mathcal { M } , s < \mu ^ { * } ( S ) \leq v \bigg \} } \\ & { \geq C _ { 2 } \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \Big \{ 1 , \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { h \rho _ { 1 } } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \Big \} , } \end{array}
$$

for $v \in [ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } ]$ and $( n , d , D )$ -independent constant $C _ { 2 }$ . The desired result then follows from Lemma 9.

# H.2 Proof of Lemma 8

Denote $I ^ { \Delta } = \mathrm { \tilde { \it W } } _ { \widetilde { \theta } } ^ { T } \mathrm { \tilde { \it I } } \mathrm { \tilde { \it W } } _ { \widetilde { \theta } }$ and $J ^ { \Delta } = ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } }$ . We first present the following lemma for bounding the $s$ -conductance profile for sampling from $\mu _ { \mathrm { l o c } } ^ { * } = \sqrt { n } \cdot W _ { \widetilde { \theta } } ^ { T } \mathcal { \widetilde { V } } _ { \widetilde { \theta } } ( \cdot ) _ { \# } ( \mu ^ { * } | _ { K _ { \theta } } )$ with $K _ { \theta } = \{ x = \widetilde { \phi } _ { \widetilde { \theta } } ( W _ { \widetilde { \theta } } \frac { z } { \sqrt { n } } \Big ) : z \in K \}$ and $K = \{ z \in \mathbb { R } ^ { d } : \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I } W _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R \}$ .

Lemma 10. Suppose (1) sup log  µ∗loc(ξ) − log  (2πdet(J−1))− d2 exp(− 12 ξT Jξ) ≤ ε1; (2) ξ∈K there exists a set $E$ satisfying $\begin{array} { r } { \mu _ { \mathrm { l o c } } ^ { * } ( E ) \geq 1 - \exp ( - 3 \varepsilon _ { 1 } ) \frac { 4 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } } \end{array}$ , so that for any $x , z \in E$ with $\begin{array} { r } { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - z ) \| \le \frac { 1 } { 8 } \sqrt { 2 h } } \end{array}$ , $\mathrm { T V } ( \mathcal { T } ^ { * } ( x , \cdot ) , \mathcal { T } ^ { * } ( z , \cdot ) ) < 1 - \omega$ . Then it holds that the $s$ -conductance profile of the Markov chain under transition probability $\tau ^ { * }$ with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 3 2 M _ { 0 } ^ { 2 } } } \end{array}$ satisfies

$$
\begin{array} { r l } & { \operatorname* { i n f } \bigg \{ \frac { \int _ { S } \mathcal { T } ^ { * } ( x , \mathbb { R } ^ { d } \backslash S ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x } { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } | S \subseteq \mathbb { R } ^ { d } , s < \mu _ { \mathrm { l o c } } ^ { * } ( S ) \leq v \bigg \} } \\ & { \geq \frac { \omega } { 4 } \operatorname* { m i n } \Big \{ 1 , \frac { \exp ( - 3 \varepsilon _ { 0 } ) } { 6 4 } \sqrt { \rho _ { 1 } h } \log ^ { \frac { 1 } { 2 } } \big ( 1 + \frac { 1 } { v } \big ) \Big \} , } \end{array}
$$

for $v \in [ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } ]$

By Assumption B.2 and lemma 10, it only remains to show that when $\| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - z ) \| \leq$ $\scriptstyle { \frac { 1 } { 8 } } { \sqrt { 2 h } }$ , $\operatorname { T V } ( { T } ^ { * } ( x , \cdot ) , { T } ^ { * } ( z , \cdot ) )$ can be controlled with high probability. Define $E = \{ \xi \in K \ :$ $\left| \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J \xi \| ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } ) \right| \le r _ { d } \}$ , where recall $K = \{ z \in \mathbb { R } ^ { d } : \| ( W _ { \widetilde { \theta } } ^ { T } \widetilde { I W } _ { \widetilde { \theta } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R \}$ . Note that by Assumption B.2,

$$
\operatorname* { s u p } _ { \xi \in K } \Big | \log \big ( \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \big ) - \log \Big ( ( 2 \pi \mathrm { d e t } ( J ^ { - 1 } ) ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } \xi ^ { T } J \xi ) \Big ) \Big | \le \varepsilon _ { 1 } .
$$

Moreover,

$$
\begin{array} { r l } & { - \mu _ { \mathrm { l o c } } ^ { \ast } ( E ) = \mu _ { \mathrm { l o c } } ^ { \ast } \big ( \big | \big | \big ( I ^ { \Delta } \big ) ^ { \frac { 1 } { 2 } } J \xi \big | ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } ) \big | > r _ { d } \big ) } \\ &  = \displaystyle \int _ { \left\{ \xi \in K : \big \} \big \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J \xi \big | ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } ) \big | > r _ { d } \right\} \mu _ { \mathrm { l o c } } ^ { \ast } ( \xi ) \mathrm { d } \xi } \\ &  \leq \displaystyle \int _ { \left\{ \xi \in K : \big \} \big \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J \xi \big | ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } ) \big | > r _ { d } \right\} \frac { \sqrt { \operatorname* { d e t } ( J ) } } { \big ( 2 \pi \big ) ^ { \frac { d } { 2 } } } \exp ( - \frac { \xi ^ { T } J \xi } { 2 } ) \mathrm { d } \xi \cdot \frac { \mathrm { i n f } } { \xi \in K } \frac { \mu _ { \mathrm { l o c } } ^ { \ast } ( \xi ) } { \big ( 2 \pi \operatorname* { d e t } \big ( \big ( J ^ { \Delta } \big ) ^ { - 1 } \big ) \big ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } \xi } } \\ &  \leq \exp ( \varepsilon _ { 1 } ) \cdot \displaystyle \int _ { \left\{ \xi \in \mathbb { R } ^ { d } \cdot \big \} \big \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J \xi \big | ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } \big ) \big | > r _ { d } \right\} \frac { \sqrt { \operatorname* { d e t } ( J ) } } { \big ( 2 \pi \big ) ^ { \frac { d } { 2 } } } \exp ( - \frac { \xi ^ { T } J \xi } { 2 } ) \mathrm { d } \xi } \\ &  = \exp ( \end{array}
$$

Furthermore, by Bernstein’s inequality (see for example, Theorem 2.8.2 of [71]), for $Z \sim { \mathcal { N } } ( 0 , \Sigma )$ , it holds that

$$
\mathbb { P } ( \left| \| Z \| ^ { 2 } - \operatorname { t r } ( \Sigma ) \right| \geq t ) \leq 2 \exp ( { - \frac { 1 } { c ^ { \prime } } ( \frac { t ^ { 2 } } { \| \Sigma \| _ { \mathrm { F } } ^ { 2 } } \land \frac { t } { \| \Sigma \| _ { \mathrm { o p } } } ) } )
$$

for a positive $( n , d , D )$ -independent constant $c ^ { \prime }$ . When $\begin{array} { r } { r _ { d } = \left( \sqrt { c ^ { \prime } \big ( \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } + 4 \varepsilon _ { 1 } \big ) } \| J ^ { \Delta } \| _ { \mathrm { F } } \right) \vee } \end{array}$ $\begin{array} { r } { \left( c ^ { \prime } \big ( \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } + 4 \varepsilon _ { 1 } \big ) \rho _ { 2 } \right) } \end{array}$ , we can obtain

$$
\begin{array} { r l } & { \mu _ { \mathrm { l o c } } ^ { * } ( E ) \geq 1 - \exp ( \varepsilon _ { 1 } ) \cdot \displaystyle \int _ { \left\{ | \xi ^ { T } ( J ^ { \Delta } ) ^ { 2 } \xi - \mathrm { t r } ( J ^ { \Delta } ) | > r _ { d } \right\} } \frac { \sqrt { \operatorname* { d e t } ( J ^ { \Delta } ) } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - \frac { \xi ^ { T } J ^ { \Delta } \xi } { 2 } ) \mathrm { d } \xi } \\ & { \qquad \geq 1 - 2 \cdot \exp ( \varepsilon _ { 1 } ) \cdot P _ { Z \sim \mathcal { N } ( 0 , J ^ { \Delta } ) } \Big ( \big | \| Z \| ^ { 2 } - \mathrm { t r } ( J ^ { \Delta } ) \big | \geq r _ { d } \Big ) } \\ & { \qquad \geq 1 - 4 \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } \exp ( - 3 \varepsilon _ { 1 } ) . } \end{array}
$$

Recall

$$
\mathcal { r } ^ { * } ( x , \mathrm { d } y ) = ( 1 - \zeta ) \cdot \widetilde { \eta } _ { G ( x ) } \cdot \mathcal { A } ^ { * } ( x , y ) p ^ { * } ( x , y ) \mathrm { d } y + \left( 1 - \int ( 1 - \zeta ) \cdot \widetilde { \eta } _ { G ( x ) } \cdot \mathcal { A } ^ { * } ( x , y ) p ^ { * } ( x , y ) \mathrm { d } y \right) \cdot \delta _ { x } ( x , y ) ,
$$

For any $x , z \in E$ , we consider the following decomposition:

$$
\begin{array} { r l } & { \begin{array} { r l } & { \Gamma \backslash ( \mathcal { T } ^ { * } ( x , \cdot ) , \mathcal { T } ^ { * } ( z , \cdot ) ) } \\ & { = \displaystyle \frac { 1 } { 2 } \int | \mathcal { T } ^ { * } ( x , y ) - \mathcal { T } ^ { * } ( z , y ) | \mathrm { d } y } \\ & { = \displaystyle \frac { 1 } { 2 } \mathcal { T } _ { x } ^ { * } ( \{ x \} ) + \frac { 1 } { 2 } \mathcal { T } _ { z } ^ { * } ( \{ z \} ) + \frac { 1 } { 2 } \int _ { \mathbb R ^ { d } \backslash \{ x , y \} } | \mathcal { T } ^ { * } ( x , y ) - \mathcal { T } ^ { * } ( z , y ) | \mathrm { d } y } \\ & { = \displaystyle \frac { 1 } { 2 } - \frac { 1 - \zeta } { 2 } \cdot \tilde { \mathcal { T } } _ { G ( x ) } \cdot \int _ { R } p ^ { * } ( x , y ) A ^ { * } ( x , y ) \mathrm { d } y + \frac { 1 } { 2 } - \frac { 1 - \zeta } { 2 } \cdot \tilde { \mathcal { T } } _ { G ( z ) } \cdot \int _ { R } p ^ { * } ( z , y ) A ^ { * } ( z , y ) \mathrm { d } y } \\ & { \qquad - \frac { 1 - \zeta } { 2 } \int _ { R } \left| \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) A ^ { * } ( x , y ) - \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( z , y ) A ^ { * } ( z , y ) \right| \mathrm { d } y } \\ & { = 1 - ( 1 - \zeta ) \int _ { R } \operatorname* { m i n } \left( \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) A ^ { * } ( x , y ) , \tilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) A ^ { * } ( z , y ) \right) \mathrm { d } y } \end{array} } \end{array}
$$

where we use $\mathcal { T } _ { x } ^ { * }$ to denote $\tau ^ { * } ( x , \cdot )$ . Recall that

$$
\mathcal { A } ^ { * } ( x , y ) = 1 \wedge \frac { \widetilde { \eta } _ { G ( y ) } \cdot p ^ { * } ( y , x ) \mu _ { \mathrm { l o c } } ^ { * } ( y ) } { \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) } .
$$

Define $\overline { { \mu } } : = \mathcal { N } ( 0 , J ^ { - 1 } )$ , we have

$$
\operatorname* { s u p } _ { \xi \in K } \left. \log ( \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) ) - \log ( \overline { { \mu } } ( \xi ) \vert \leq \varepsilon _ { 1 } , \right.
$$

and thus

$$
\frac { \mu _ { \mathrm { l o c } } ^ { * } ( y ) } { \mu _ { \mathrm { l o c } } ^ { * } ( x ) } \geq \exp ( - 2 \varepsilon _ { 1 } ) \frac { \overline { { \mu } } ( y ) } { \overline { { \mu } } ( x ) } .
$$

Therefore, denote

$$
\overline { { { \mathcal { A } } } } ^ { * } ( x , y ) = 1 \wedge \frac { \widetilde { \eta } _ { G ( y ) } \cdot p ^ { * } ( y , x ) \overline { { \mu } } ( y ) } { \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \overline { { \mu } } ( x ) } .
$$

We have

$$
\begin{array} { r l } & { \mathrm { T V } ( \mathcal { T } ^ { * } ( x , \cdot ) , \mathcal { T } ^ { * } ( z , \cdot ) ) } \\ & { \leq 1 - ( 1 - \zeta ) \exp ( - 2 \varepsilon _ { 1 } ) \displaystyle \int _ { K } \operatorname* { m i n } \Big ( \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) , \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) \overline { { \mathcal { A } } } ^ { * } ( z , y ) \Big ) \mathrm { d } y } \\ & { = 1 - \displaystyle \frac { 1 - \zeta } { 2 } \exp ( - 2 \varepsilon _ { 1 } ) \cdot \Big ( \widetilde { \eta } _ { G ( x ) } \cdot \displaystyle \int _ { K } p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) \mathrm { d } y + \widetilde { \eta } _ { G ( z ) } \cdot \displaystyle \int _ { K } p ^ { * } ( z , y ) \overline { { \mathcal { A } } } ^ { * } ( z , y ) \mathrm { d } y } \\ & { \qquad - \displaystyle \int _ { K } \left| \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) \overline { { \mathcal { A } } } ^ { * } ( z , y ) \right| \mathrm { d } y \Big ) . } \end{array}
$$

Then consider the inequality,

$$
\begin{array} { r l } & { \displaystyle \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) \overline { { \mathcal { A } } } ^ { * } ( z , y ) | \mathrm { d } y \le \displaystyle \int _ { K } \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) ( 1 - \overline { { \mathcal { A } } } ^ { * } ( x , y ) ) } \\ & { \quad \quad + \displaystyle \int _ { K } \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) ( 1 - \overline { { \mathcal { A } } } ^ { * } ( z , y ) ) \mathrm { d } y + \displaystyle \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) | \mathrm { d } y . } \end{array}
$$

Moreover, consider the proposal distribution of RWM,

$$
p _ { x } ^ { \Delta } ( \cdot ) = p ^ { \Delta } ( x , \cdot ) = \mathcal { N } ( x , 2 h I ^ { \Delta } ) ,
$$

we have the equation,

$$
\begin{array} { r l } & { \widetilde { \eta } _ { G ( x ) } \cdot \displaystyle \int _ { K } p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) \mathrm { d } y } \\ & { = 1 - \Big ( \displaystyle \int p ^ { \Delta } ( x , y ) \mathrm { d } y - \displaystyle \int _ { K } \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \overline { { \mathcal { A } } } ^ { * } ( x , y ) \mathrm { d } y \Big ) } \\ & { = 1 - \Big ( \displaystyle \int _ { K } \big ( p ^ { \Delta } ( x , y ) - \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \big ) \mathrm { d } y } \\ & { \qquad + \displaystyle \int _ { K } \widetilde { \eta } _ { G ( x ) } \cdot ( 1 - \overline { { \mathcal { A } } } ^ { * } ( x , y ) ) p ^ { * } ( x , y ) \mathrm { d } y + \displaystyle \int _ { K ^ { c } } p ^ { \Delta } ( x , y ) \mathrm { d } y \Big ) } \end{array}
$$

Combined with (47), we can then obtain

$$
\begin{array} { l } { \displaystyle \mathbb { V } ( \mathcal { T } ^ { * } ( x , \cdot ) , \mathcal { T } ^ { * } ( z , \cdot ) ) } \\ { \displaystyle \le 1 - ( 1 - \zeta ) \exp ( - 2 \varepsilon _ { 1 } ) \Bigg ( 1 - \int _ { K } \widetilde { \eta } _ { G ( x ) } \cdot ( 1 - \overline { { A } } ^ { * } ( x , y ) ) p ^ { * } ( x , y ) \mathrm { d } y - \int _ { K } \widetilde { \eta } _ { G ( z ) } \cdot ( 1 - \overline { { A } } ^ { * } ( z , y ) ) } \\ { \displaystyle \quad - \frac 1 2 \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) | \mathrm { d } y - \frac 1 2 \int _ { K ^ { c } } p ^ { \Delta } ( x , y ) \mathrm { d } y - \frac 1 2 \int _ { K ^ { c } } p ^ { \Delta } ( z , y ) \mathrm { d } y } \\ { \displaystyle \qquad - \frac 1 2 \int _ { K } \big ( p ^ { \Delta } ( x , y ) - \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) \big ) \mathrm { d } y - \frac 1 2 \int _ { K } \big ( p ^ { \Delta } ( z , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) \big ) \mathrm { d } y \Bigg ) . } \end{array}
$$

Notice that

$$
\begin{array} { l } { \displaystyle \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) | \mathrm { d } y } \\ { \displaystyle \le \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - p ^ { \Delta } ( x , y ) | \mathrm { d } y + 2 \mathrm { T V } ( p ^ { \Delta } ( x , \cdot ) , p ^ { \Delta } ( z , \cdot ) ) + \int _ { K } | \widetilde { \eta } _ { G ( z ) } \cdot p ^ { * } ( z , y ) - p ^ { \Delta } ( z , y ) | \mathrm { d } y } \end{array}
$$

The term $\mathrm { T V } ( p ^ { \Delta } ( x , \cdot ) , p ^ { \Delta } ( z , \cdot ) )$ can be upper bounded by Pinsker’s inequality, that is, for any $x , z \in K$ ,

$$
\mathrm { T V } ( p ^ { \Delta } ( x , \cdot ) , p ^ { \Delta } ( z , \cdot ) ) \leq \frac { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - z ) \| } { 2 \sqrt { 2 h } } .
$$

For the term $\begin{array} { r } { \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - p ^ { \Delta } ( x , y ) | \mathrm { d } y } \end{array}$ , recall

$$
p ^ { * } ( x , y ) = \frac { 1 } { \widetilde { \eta } _ { G ( x ) } } \cdot \widetilde { p } _ { G ( x ) } ( \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G ( y ) ) \cdot \left| \operatorname* { d e t } \bigl ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G } ( y ) \bigr ) \right| \cdot \mathbf { 1 } \bigl ( y \in ( Q \circ \widetilde { \phi } _ { G ( x ) } ^ { * } ) ( \Omega _ { G ( x ) } ) \bigr ) .
$$

We have the following lemma.

Lemma 11. There exists a constant $C$ independent of n so that for any $x , y \in K$

$$
\Big | 1 - \frac { \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) } { p ^ { \Delta } ( x , y ) } \Big | \leq C \frac { R ^ { 3 } } { h \sqrt { n } } .
$$

So by Lemma 11, fo any $x \in K$ , $\begin{array} { r } { \int _ { K } | \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - p ^ { \Delta } ( x , y ) | \mathrm { d } y \le C \frac { R ^ { 3 } } { h \sqrt { n } } } \end{array}$ holds for an $n$ $C$ . For the term of $\begin{array} { r } { \int _ { K } \widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) ( 1 - \overline { { \mathcal { A } } } ^ { * } ( x , y ) ) \mathrm { d } y } \end{array}$ , we use Assumption

B.2 by comparing $\mu _ { \mathrm { l o c } } ^ { * }$ with $\overline { { \mu } }$ , leading to the following decomposition:

$$
\begin{array} { r l } & { \int _ { K } \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) ( 1 - \overline { { A } } ^ { * } ( x , y ) ) \mathrm { d } y } \\ & { \le \int _ { K } \Big | \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - \frac { \tilde { \eta } _ { G ( y ) } \cdot \tilde { \eta } ( y ) p ^ { * } ( y , x ) } { \tilde { \mu } ( x ) } \Big | \mathrm { d } y } \\ & { \le \int _ { K } | \tilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) - p ^ { \Delta } ( x , y ) | \mathrm { d } y + \underbrace { \int \left| p ^ { \Delta } ( x , y ) - \frac { \overline { { \mu } } ( y ) p ^ { \Delta } ( y , x ) } { \overline { { \mu } } ( x ) } \right| \mathrm { d } y } _ { ( \Lambda ) } } \\ & { \quad + \underbrace { \int _ { K } \Big | \frac { \overline { { \mu } } ( y ) p ^ { \Delta } ( y , x ) } { \tilde { \mu } ( x ) } - \frac { \tilde { \eta } _ { G ( y ) } \cdot \tilde { \mu } ( y ) p ^ { * } ( y , x ) } { \tilde { \mu } ( x ) } \Big | \mathrm { d } y } _ { ( \Lambda ) } . } \end{array}
$$

We then state the following lemma for bounding the term $( A )$

Lemma 12. There exists a small enough $( n , d , D )$ -independent positive constant $c _ { 0 }$ so that when $\begin{array} { r } { h \leq c _ { 0 } \rho _ { 2 } ^ { - 1 } \Big ( d + \log \big ( \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) \Big ) ^ { - 1 } } \end{array}$ , for any $x \in E$ , it holds that

$$
\int \left| p ^ { \Delta } ( x , y ) - \frac { \overline { { \mu } } ( y ) p ^ { \Delta } ( y , x ) } { \overline { { \mu } } ( x ) } \right| \mathrm { d } y \leq \frac { 1 } { 2 4 } .
$$

For the term $( B )$ , by Lemma 11 and 12, we have

$$
\begin{array} { l } { \displaystyle \int _ { K } \left. p ^ { \Delta } ( y , x ) - \widetilde \eta _ { G ( y ) } \cdot p ^ { * } ( y , x ) \right. \frac { \overline { { \mu } } ( y ) } { \overline { { \mu } } ( x ) } \mathrm { d } y } \\ { \displaystyle = \int _ { K } \left. 1 - \frac { \widetilde \eta _ { G ( y ) } \cdot p ^ { * } ( y , x ) } { p ^ { \Delta } ( y , x ) } \right. \frac { \overline { { \mu } } ( y ) p ^ { \Delta } ( y , x ) } { \overline { { \mu } } ( x ) } \mathrm { d } y } \\ { \displaystyle \leq \frac { 2 5 } { 2 4 } \cdot \frac { C R ^ { 3 } } { h \sqrt { n } } . } \end{array}
$$

Then it remains to bound $\textstyle \int _ { K ^ { c } } p ^ { \Delta } ( x , y ) \mathrm { d } y$ , which is captured by the following lemma.

Lemma 13. When $R \geq 6 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) }$ , there exists $a$ $( n , d , D )$ -independent constant $c _ { 0 }$ so that when $h \leq c _ { 0 } \rho _ { 2 } ^ { - 1 } d ^ { - 1 }$ , for any $x \in K$ , it holds that

$$
\int _ { K ^ { c } } \mathcal { N } ( x , 2 h I ^ { \Delta } ) \mathrm { d } y \leq \frac { 1 3 } { 2 4 } .
$$

Then by combining all the pieces, we can obtain that

$$
\mathrm { T V } ( { \cal T } ^ { * } ( x , \cdot ) , { \cal T } ^ { * } ( z , \cdot ) ) \leq 1 - ( 1 - \zeta ) \exp ( - 2 \varepsilon _ { 1 } ) \biggr ( \frac { 3 } { 8 } - \frac { 7 3 } { 1 2 } \frac { C R ^ { 3 } } { h \sqrt { n } } - \frac { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - z ) \| } { 2 \sqrt { 2 } h } \biggr ) .
$$

So when $R \leq C _ { 1 } ( h \sqrt { n } ) ^ { \frac { 1 } { 3 } }$ for a small enough $n$ -independent constant $C _ { 1 }$ , for any $x , z \in E$ with $\| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - z ) \| \le \frac { 1 } { 8 } \sqrt { 2 h }$ and $\zeta \in \ ( 0 , \frac { 1 } { 2 } ]$ , it holds that $\mathrm { T V } ( \mathcal { T } ^ { * } ( x , \cdot ) , \mathcal { T } ^ { * } ( z , \cdot ) ) \leq 1 -$ $\begin{array} { r } { \frac { 1 - \zeta } { 4 } \exp ( - 2 \varepsilon _ { 1 } ) \leq 1 - \frac { \exp ( - 2 \varepsilon _ { 1 } ) } { 8 } } \end{array}$ exp(−2ε1)8 . The desired result then directly follows from Lemma 10.

# H.3 Proof of Corollary 4

Fix an $X ^ { ( n ) } \in { \mathcal { A } }$ where $\mathcal { A }$ is defined in the proof of Theorem 2. Let $R = C { \sqrt { \log n } }$ , where $C$ is a large enough constant that will be chosen later. Define

$$
\widehat { \theta } ^ { \diamond } = \phi _ { \theta ^ { \ast } } \big ( - W _ { \theta ^ { \ast } } ( W _ { \theta ^ { \ast } } ^ { T } \mathcal { H } _ { \theta ^ { \ast } } W _ { \theta ^ { \ast } } ) ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { \ast } } ^ { T } g ( X _ { i } , \theta ^ { \ast } ) \big ) ,
$$

as in the proof of Theorem 2. Then we have shown $\| \theta ^ { * } - \widehat { \theta ^ { \circ } } \| \lesssim \sqrt { \frac { \log n } { n } }$ . Let $W _ { \theta ^ { * } } \in \mathbb { R } ^ { D \times d }$ be an orthonormal basis of $T _ { \theta ^ { * } } { \mathcal { M } }$ , and define $\widetilde { W } _ { \widehat { \theta ^ { \diamond } } } = \mathcal { U } _ { \widehat { \theta ^ { \diamond } } } \mathcal { W } _ { \widehat { \theta ^ { \diamond } } } ^ { T }$ with $\mathcal { U } _ { \widehat { \theta } \circ } S _ { \widehat { \theta } \circ } \mathcal { W } _ { \widehat { \theta } \circ } ^ { T }$ being the singular value decomposition of $\mathbf { J } _ { \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } y ) } ( y = W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } ) )$ . We will show the desired result using Theorem 3. We start by verifying the four conditions in Theorem 3.

1. Using Lemma 2, and $\| \theta ^ { * } - { \widehat { \theta ^ { \circ } } } \| \lesssim { \sqrt { \frac { \log n } { n } } }$ , there exists a positive constant $r$ so that $B _ { r } ( 0 _ { D } ) \cap$ $T _ { \widehat { \theta ^ { \circ } } } { \mathcal { M } } \subseteq V _ { \widehat { \theta ^ { \circ } } }$ . Moreover, since $R \lesssim { \sqrt { \log n } }$ , for $z \in K = \{ z \in \mathbb { R } ^ { d } : \| ( \widetilde W _ { \widehat { \theta } ^ { \circ } } \widetilde { I } \widetilde { W } _ { \widehat { \theta } ^ { \circ } } ) ^ { - \frac { 1 } { 2 } } z \| \leq R \}$ , bwe have $\| z \| \leq R \cdot \left\| \widetilde W _ { \widehat { \theta } ^ { \diamond } } \widetilde { I W } _ { \widehat { \theta } ^ { \diamond } } \right\| _ { \mathrm { o p } } \lesssim \sqrt { \log n }$ . Thus $\begin{array} { r } { \{ v = \widetilde W _ { \widehat { \theta } ^ { \circ } } \frac { z } { \sqrt { n } } : z \in K \} \subseteq B _ { r } ( 0 _ { D } ) \cap } \end{array}$ $T _ { \widehat { \theta ^ { \circ } } } { \mathcal { M } } \subseteq V _ { \widehat { \theta ^ { \circ } } }$ .

2. Define $K _ { \theta } = \{ x = \phi _ { \widehat { \theta } ^ { \circ } } ( \widetilde { W } _ { \widehat { \theta } ^ { \circ } } \frac { z } { \sqrt { n } } ) : z \in K \}$ and let $\begin{array} { r } { \mathcal { L } ( X ^ { ( n ) } , \theta ) = \frac { L ( X ^ { ( n ) } , \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \exp \big ( - \alpha _ { n } \cdot } \end{array}$ $( { \mathcal { R } } _ { n } ( \theta ) - { \mathcal { R } } _ { n } ( \theta ^ { * } ) ) )$ . Denote $G ( z ) = \sqrt { n } \cdot \phi _ { \widehat { \theta } ^ { \diamond } } \bigl ( \tilde { W } _ { \widehat { \theta } ^ { \diamond } } { \textstyle \frac { z } { \sqrt { n } } } \bigr )$ . The density function $\mu _ { \mathrm { l o c } } ^ { * } ( \cdot )$ of $[ \left( \sqrt { n } \cdot \widetilde { W } _ { \widehat { \theta ^ { \circ } } } ^ { T } \psi _ { \widehat { \theta ^ { \circ } } } \right) _ { \# } ( \Pi _ { \mathrm { R P } } ( \cdot | X ^ { ( n ) } ) | _ { K _ { \theta } } ) ]$ is given by

$$
\mu _ { \mathrm { l o c } } ^ { * } ( z ) = \frac { \pi ( G ( z ) ) \mathcal { L } \left( X ^ { ( n ) } , G ( z ) \right) \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } } { \int _ { K } \pi ( G ( z ) ) \mathcal { L } \left( X ^ { ( n ) } , G ( z ) \right) \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } \mathrm { d } z } , \quad z \in K .
$$

Since $\| { \widehat { \theta ^ { \circ } } } - \theta ^ { * } \| \leq C _ { 1 } { \sqrt { \frac { \log n } { n } } }$ , we have $\left\| \widetilde { W } _ { \widehat { \theta ^ { \circ } } } - W _ { \theta ^ { * } } \right\| _ { \mathrm { F } } \leq C _ { 2 } \sqrt { \frac { \log n } { n } }$ . Define $h = { \sqrt { n } }$ · $\begin{array} { r } { W _ { \theta ^ { * } } ^ { T } \Big ( \phi _ { \widehat { \theta } ^ { \diamond } } \big ( \frac { \widehat { W } _ { \widehat { \theta } ^ { \diamond } } z } { \sqrt { n } } \big ) - \widehat { \theta } ^ { \diamond } \Big ) } \end{array}$ , we can get

$$
\begin{array} { r l } & { \Big \| \displaystyle \frac { h } { \sqrt { n } } - \frac { z } { \sqrt { n } } \Big \| = \Big \| \boldsymbol { W } _ { \boldsymbol { \theta ^ { * } } } ^ { T } \Big ( \phi _ { \boldsymbol { \widehat { \theta ^ { * } } } } \Big ( \frac { \widetilde { W } _ { \widehat { \boldsymbol { \theta ^ { * } } } } z } { \sqrt { n } } \Big ) - \widehat { \boldsymbol { \theta ^ { * } } } \Big ) - \frac { z } { \sqrt { n } } \Big \| } \\ & { \qquad \leq \Big \| \boldsymbol { W } _ { \boldsymbol { \theta ^ { * } } } ^ { T } \frac { \widetilde { W } _ { \widehat { \boldsymbol { \theta ^ { * } } } } z } { \sqrt { n } } - \frac { z } { \sqrt { n } } \Big \| + C _ { 3 } \frac { \| \boldsymbol { z } \| ^ { 2 } } { n } } \\ & { \qquad \leq \displaystyle \frac { \| \boldsymbol { z } \| } { \sqrt { n } } \| \big \| \boldsymbol { W } _ { \boldsymbol { \theta ^ { * } } } ^ { T } \widetilde { \boldsymbol { W } } _ { \widehat { \boldsymbol { \theta ^ { * } } } } - \boldsymbol { W } _ { \boldsymbol { \theta ^ { * } } } ^ { T } \boldsymbol { W } _ { \boldsymbol { \theta ^ { * } } } \big \| _ { \mathrm { o p } } + C _ { 3 } \frac { \| \boldsymbol { z } \| ^ { 2 } } { n } \lesssim \frac { R ^ { 2 } } { n } } \end{array}
$$

and by Step 3 of the proof of Theorem 2,

$$
\begin{array} { r l } & { \log \mathcal { L } ( X ^ { ( n ) } , G ( z ) ) + \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } z \Big | } \\ & { \le \Big | \log \mathcal { L } \Big ( X ^ { ( n ) } , \phi _ { \theta ^ { * } } \big ( \frac { W _ { \theta ^ { * } } h } { \sqrt { n } } + \psi _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } ) \big ) \Big ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h \Big | + \Big | \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } h - \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - } } \\ & { \lesssim \frac { R ^ { 3 } ( \log n ) ^ { 1 + \frac { 2 } { \beta _ { 1 } } } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Moreover, by Assumption 1 and Lemma 2, we can verify

$$
\sqrt { n } \cdot \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } - 1 \big | = \big | \sqrt { n } \cdot \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } - \sqrt { n } \cdot \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G } ( 0 _ { d } ) ^ { T } \mathbf { J } _ { G } ( 0 _ { d } ) ) } \big | \leq C \ .
$$

So there exists a constant $C _ { 1 }$ so that for any $z \in K$ ,

$$
\begin{array} { r l } & { \log \left( \pi ( G ( z ) ) \mathcal { L } ( X ^ { ( n ) } , G ( z ) ) \sqrt { n \cdot \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } \right) - \log \left( \pi ( \theta ^ { * } ) \exp ( - \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } z ) \right) | } \\ & { \leq C _ { 1 } \frac { R ^ { 3 } \left( \log n \right) ^ { 1 + \frac { 1 } { \beta _ { 1 } } } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

Furthermore, when $R = C \sqrt { \log n }$ with large enough $C$ , there exists a constant $C _ { 2 }$ so that

$$
\begin{array} { r l } & { \displaystyle \int _ { K } \pi ( G ( z ) ) \mathcal { L } ( X ^ { ( n ) } , G ( z ) ) \sqrt { n \cdot \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } \mathrm { d } z - \displaystyle \int \pi ( \theta ^ { * } ) \exp ( - \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } z ) \mathrm { d } z \Big | } \\ & { \le \Big | \displaystyle \int _ { K } \pi ( G ( z ) ) \mathcal { L } ( X ^ { ( n ) } , G ( z ) ) \sqrt { n \cdot \operatorname* { d e t } ( \mathbf { J } _ { G } ( z ) ^ { T } \mathbf { J } _ { G } ( z ) ) } \mathrm { d } z } \\ & { \quad - \displaystyle \int _ { K } \pi ( \theta ^ { * } ) \exp ( - \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } z ) \mathrm { d } z \Big | + \displaystyle \int _ { K ^ { c } } \pi ( \theta ^ { * } ) \exp ( - \frac { 1 } { 2 } z ^ { T } \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } z ) \mathrm { d } z } \\ & { \le C _ { 2 } \frac { R ^ { 3 } ( \log n ) ^ { 1 + \frac { 1 } { 2 } } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

We can then obtain by combining all pieces that there exists a constant $C _ { 3 }$ so that

$$
\operatorname* { s u p } _ { z \in K } \Big | \log \big ( \mu _ { \mathrm { l o c } } ^ { * } ( z ) \big ) - \log \Big ( ( 2 \pi \mathrm { d e t } ( J ^ { - 1 } ) ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } z ^ { T } J z ) \Big ) \Big | \leq C _ { 3 } \frac { R ^ { 3 } ( \log n ) ^ { 1 + \frac { 1 } { \beta _ { 1 } } } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } ,
$$

with $J = \mathcal { H } _ { 0 } \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 }$ .

3. Using $\rho _ { 1 } I _ { d } \preccurlyeq ( W _ { \theta ^ { * } } ^ { T } \widetilde { I } W _ { \theta ^ { * } } ) ^ { \frac { 1 } { 2 } } J ( W _ { \theta ^ { * } } ^ { T } \widetilde { I } W _ { \theta ^ { * } } ) ^ { \frac { 1 } { 2 } } \preccurlyeq \rho _ { 2 } I _ { d }$ , and $\left. \mathbf { W } _ { \theta ^ { * } } - \widetilde { W } _ { \widehat { \theta } ^ { \circ } } \right. _ { \mathrm { F } } \lesssim \sqrt { \frac { \log n } { n } }$ , when $n$ is large enough, we have

$$
\frac { \rho _ { 1 } } { 2 } I _ { d } \prec ( \widetilde { W } _ { \widehat { \theta } \diamond } ^ { T } \widetilde { I } \widetilde { W } _ { \widehat { \theta } \diamond } ) ^ { \frac { 1 } { 2 } } J ( \widetilde { W } _ { \widehat { \theta } \diamond } ^ { T } \widetilde { I } \widetilde { W } _ { \widehat { \theta } \diamond } ) ^ { \frac { 1 } { 2 } } \prec 2 \rho _ { 2 } I _ { d } .
$$

4. Notice that for sufficiently large $n$ , we have

$$
\begin{array} { r l } & { \varepsilon _ { 1 } = \underset { z \in K } { \operatorname* { s u p } } \Big | \log \left( \mu _ { \mathrm { l o c } } ^ { * } ( z ) \right) - \log \left( ( 2 \pi \mathrm { d e t } ( J ^ { - 1 } ) ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } z ^ { T } J z ) \right) \Big | } \\ & { \quad \leq C _ { 3 } \frac { R ^ { 3 } ( \log n ) ^ { 1 + \frac { 1 } { \beta _ { 1 } } } } { n ^ { \frac { \beta _ { 2 } } { 2 } } } \leq 1 } \end{array}
$$

Then using $\frac { \varepsilon } { M _ { 0 } } \geq n ^ { - c }$ , we have for sufficiently large $n$ that $\exp \bigl ( - 5 \varepsilon _ { 1 } \bigr ) \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { 2 M _ { 0 } ^ { 2 } } \ \geq \ n ^ { - 2 c - 1 }$ Furthermore, using the results from Step 6 of the proof of Theorem 2, there exists a constant $C _ { 0 }$ so that $\begin{array} { r } { \Pi _ { \mathrm { R P } } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq C _ { 0 } \sqrt { \frac { \log n } { n } } | X ^ { ( n ) } ) \geq 1 - n ^ { - 2 c - 1 } } \end{array}$ . Therefore, when $R = C \sqrt { \log n }$ with large enough $C$ , when have

$$
\begin{array} { r l } & { \Pi _ { \mathrm { R P } } \Big ( \theta \in \Big \{ \theta = \phi _ { \widehat { \theta ^ { \circ } } } ( \widetilde { W } _ { \widehat { \theta ^ { \circ } } } \frac { z } { \sqrt { n } } ) : \| ( \widetilde { W } _ { \widehat { \theta ^ { \circ } } } \widetilde { I W } _ { \widehat { \theta ^ { \circ } } } ) ^ { - \frac 1 2 } z \| \leq R / 2 \} | X ^ { ( n ) } \Big ) } \\ & { \geq \Pi _ { \mathrm { R P } } ( \| \theta - \widehat { \theta ^ { \circ } } \| \leq C _ { 0 } \sqrt { \displaystyle \frac { \log n } { n } } | X ^ { ( n ) } ) \geq 1 - n ^ { - 2 c - 1 } . } \end{array}
$$

The desired result then follows from Theorem 3.

# I Proof of Technical Results

# I.1 Proof of Lemma 1

Recall that

$$
\prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) = \prod _ { i = 1 } ^ { n } \frac { \exp \left( \overline { { { \lambda } } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) } { \sum _ { i = 1 } ^ { n } \exp \left( \overline { { { \lambda } } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) } ,
$$

with $\overline { { \lambda } } ( \theta ) = \underset { \xi \in T _ { \theta } \mathcal { M } } { \arg \operatorname* { m i n } } \sum _ { i = 1 } ^ { n } \exp ( \xi ^ { T } g ( X _ { i } , \theta ) )$ . Therefore, we can write

$$
f ( \theta ) = \frac { \alpha _ { n } } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - \sum _ { i = 1 } ^ { n } \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) - n \cdot \log \Big ( \sum _ { i = 1 } ^ { n } \exp \big ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \big ) \Big ) .
$$

So the Riemannian gradient of $f$ is given by

$$
\begin{array} { l } { \displaystyle \mathrm { ~ s r a d ~ } \int ( \theta ) = \frac { \alpha _ { n } } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \displaystyle \sum _ { i = 1 } ^ { n } [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) - \displaystyle \sum _ { i = 1 } ^ { n } [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] \cdot g ( X _ { i } , \theta ) } \\ { \displaystyle ~ - n \cdot \frac { \sum _ { i = 1 } ^ { n } \exp \big ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \big ) \cdot \big ( [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) + [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] \cdot g ( X _ { i } , \theta ) \big ) } { \sum _ { i = 1 } ^ { n } \exp \big ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \big ) } } \\ { \displaystyle ~ = \frac { \alpha _ { n } } { n } \sum _ { i = 1 } ^ { n } g \big ( X _ { i } , \theta \big ) - \displaystyle \sum _ { i = 1 } ^ { n } [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) - \displaystyle \sum _ { i = 1 } ^ { n } [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] \cdot g ( X _ { i } , \theta ) } \\ { \displaystyle ~ - n \cdot \frac { \sum _ { i = 1 } ^ { n } \exp \big ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \big ) \cdot [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \cdot \overline { { \lambda } } ( \theta ) } { \sum _ { i = 1 } ^ { n } \exp \big ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \big ) } , } \end{array}
$$

where grad $\bar { \lambda } ( \cdot )$ denotes the Riemannian gradient of $\bar { \lambda } ( \cdot )$ on $\mathcal { M }$ and the last equality is due to the fact that

$$
\sum _ { i = 1 } ^ { n } \frac { \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) } { \sum _ { i = 1 } ^ { n } \exp \left( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) } \cdot g ( X _ { i } , \theta ) = \sum _ { i = 1 } ^ { n } p _ { i } ( \theta ) g ( X _ { i } , \theta ) = 0 _ { D } .
$$

So it remains to show that $g _ { \overline { { \lambda } } } ( \theta ) = [ \mathrm { g r a d } \ : \overline { { { \lambda } } } ( \theta ) ] ^ { T }$ . Recall for any $k \in \left[ D \right]$ and $\theta \in \mathcal { M }$ ,

$$
\sum _ { i = 1 } ^ { n } \exp ( \overline { { { \lambda } } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g _ { k } ( X _ { i } , \theta ) = 0 .
$$

Therefore, we have for any $k \in \left[ D \right]$ , the Riemannian gradient of $\begin{array} { r l } { \sum _ { i = 1 } ^ { n } \exp ( \bar { \lambda } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g _ { k } ( X _ { i } , \theta ) } & { { } } \end{array}$ with respect to $\theta$ on $\mathcal { M }$ satisfies that

$$
\mathrm { g r a d } _ { \theta } \Big ( \sum _ { i = 1 } ^ { n } \mathrm { e x p } ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g _ { k } ( X _ { i } , \theta ) \Big ) = 0 _ { D } .
$$

We can then obtain that for any $k \in \left[ D \right]$ ,

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) \cdot \Big ( \mathrm { g r a d } _ { \theta } g _ { k } ( X _ { i } , \theta ) + g _ { k } ( X _ { i } , \theta ) [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] g ( X _ { i } , \theta ) + g _ { k } ( X _ { i } , \theta ) [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] \Big ) } \\ & { = 0 _ { D } , } \end{array}
$$

which further lead to

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) g ^ { T } ( X _ { i } , \theta ) [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] ^ { T } } \\ & { = - \displaystyle \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) \cdot \Big ( [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] ^ { T } + g ( X _ { i } , \theta ) \overline { { \lambda } } ( \theta ) ^ { T } [ \mathrm { g r a d } _ { \theta } g ( X _ { i } , \theta ) ] ^ { T } \Big ) . } \end{array}
$$

Therefore, we have

$$
\begin{array} { r l r } {  { [ \mathrm { g r a d } \overline { { \lambda } } ( \theta ) ] ^ { T } = - ( \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } ) ^ { + } } } \\ & { } & { \cdot ( \sum _ { i = 1 } ^ { n } \exp ( \overline { { \lambda } } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ( I _ { D } + g ( X _ { i } , \theta ) \overline { { \lambda } } ( \theta ) ^ { T } ) [ \mathrm { g r a d } _ { \theta } g ( X , \theta ) ] ^ { T } ) = g _ { \overline { { \lambda } } } ( \theta ) . } \end{array}
$$

# I.2 Proof of Lemma 5

Using $\mathbb { E } [ \exp { \Big ( } { \big ( } { \frac { b ( X ) } { L } } { \big ) } ^ { \beta _ { 1 } } { \Big ) } { \Big ] } \leq 1$ and Markov’s inequality, we obtain, for $C \geq L 4 ^ { \frac { 1 } { \beta _ { 1 } } }$ , that

$$
\begin{array} { r } { P ( X ^ { ( n ) } \notin \mathcal { A } _ { 1 } ) \le n \cdot P ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) } \\ { \le n \frac { 1 } { \exp ( ( \frac { C } { L } ) ^ { \beta _ { 1 } } \log n ) } \le \frac { 1 } { n ^ { 3 } } . } \end{array}
$$

Furthermore, for any $X \in { \mathcal { X } }$ ,

$$
\left\| g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \right\| \leq b ( X ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } .
$$

Moreover, there exists a constant $C _ { 2 }$ so that

$$
\begin{array} { r l } & { \mathbb { E } \Big [ \| g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \| ^ { 2 } \Big ] } \\ & { \leq \mathbb { E } \big [ \| g ( X , \theta ^ { * } ) \| ^ { 2 } \big ] \leq \mathbb { E } \big [ ( b ( X ) ) ^ { 2 } \big ] \leq C _ { 2 } . } \end{array}
$$

In addition, using $\mathbb { E } [ g ( X , \theta ^ { * } ) ] = \mathrm { g r a d } _ { \theta } \mathcal { R } ( \theta ^ { * } ) = 0 _ { D }$ , we have

$$
\begin{array} { r l } & { \left\| \mathbb { E } \Big [ g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \Big ] \right\| } \\ & { = \Big \| \mathbb { E } \Big [ g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \Big ] \Big \| } \\ & { \leq \sqrt { d } \sqrt { \mathbb { E } \Big [ \Big \| g ( X , \theta ^ { * } ) \Big \| ^ { 2 } \Big ] } \cdot \sqrt { P \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) } } \\ & { \leq \frac { C _ { 3 } } { n ^ { 2 } } . } \end{array}
$$

We can then obtain via Bernstein’s inequality that, when $C _ { 1 }$ is sufficiently large,

$$
\begin{array} { r l r } {  { P ( X ^ { ( n ) } \not \in \mathcal { A } _ { 2 } ) \leq P \Big ( \Big \| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) } } \\ & { } & { \qquad - \mathbb { E } \Big [ g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \Big ] \Big \| \geq C _ { 1 } \sqrt { \frac { \log n } { n } } - \frac { C _ { 3 } } { n ^ { \frac { 3 } { 2 } } } \Big ) } \\ & { } & { \leq P \Big ( \Big \| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) } \\ & { } & { \qquad - \mathbb { E } \Big [ g ( X , \theta ^ { * } ) \cdot \mathbf { 1 } \big ( b ( X ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \Big ] \Big \| \geq \frac { C _ { 1 } } { 2 } \sqrt { \frac { \log n } { n } } \Big ) \leq \frac { 1 } { n ^ { 3 } } . } \end{array}
$$

Similarly, since $\mathbb { E } [ \| g ( X , \theta ^ { * } ) \| ^ { 6 } ] \le \mathbb { E } [ b ( X ) ^ { 6 } ] < \infty$ , we can apply Bernstein inequality to obtain $\textstyle P ( X ^ { ( n ) } \not \in { \mathcal { A } } _ { 3 } ) \leq { \frac { 1 } { n ^ { 3 } } }$ . Define

$$
\widetilde { g } ( x , \theta ) = \frac { 1 } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \cdot g ( x , \theta ) \cdot \mathbf { 1 } \big ( b ( x ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big )
$$

and

$$
\widetilde \ell ( x , \theta ) = \frac { 1 } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \cdot \ell ( x , \theta ) \cdot { \mathbf 1 } ( b ( x ) \le C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) .
$$

Then, for any $x \in \mathcal { X }$ and $\theta \in S _ { \Pi }$ , $\begin{array} { r } { \| \widetilde { g } ( x , \theta ) \| \le \frac { b ( x ) } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \cdot { \mathbf 1 } ( b ( x ) \le C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) \le 1 } \end{array}$ and for any $x \in { \mathcal { X } } , \theta , \theta ^ { \prime } \in S _ { \Pi }$ ,

$$
| \widetilde { \ell } ( x , \theta ) - \widetilde { \ell } ( x , \theta ^ { \prime } ) | \leq \frac { 1 } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } b ( x ) \cdot \mathbf { 1 } ( b ( x ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) \cdot \| \theta - \theta ^ { \prime } \| \leq \| \theta - \theta ^ { \prime } \| .
$$

Now define the pseudo-metric $d _ { n } ^ { \widetilde { g } } : S _ { \Pi } \times S _ { \Pi } \to \mathbb { R }$ as

$$
d _ { n } ^ { \widetilde { g } } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| \widetilde { g } ( X _ { i } , \theta ) - \widetilde { g } ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } } .
$$

Then for any $\theta , \theta ^ { \prime } \in S _ { \Pi }$ ,

$$
\begin{array} { r l } & { d _ { n } ^ { \widetilde { g } } ( \theta , \theta ^ { \prime } ) = \displaystyle \frac { 1 } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } \cdot \mathbf { 1 } ( b ( X _ { i } ) \le C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) } } \\ & { = \displaystyle \frac { 1 } { C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \sqrt { \frac { 1 } { n } \sum _ { i \in [ n ] , b ( X _ { i } ) \le C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } } . } \end{array}
$$

Therefore

$$
\begin{array} { r } { \log \mathbf { N } ( B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } , d _ { n } ^ { \widetilde { g } } , \varepsilon ) = \log \mathbf { N } ( B _ { r } ( \theta ^ { * } ) \cap S _ { \Pi } , d _ { n } ^ { \widetilde { g } } , C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \varepsilon ) \leq L _ { 2 } \log n + L _ { 3 } \log ( \frac { 1 } { \varepsilon } ) . } \end{array}
$$

Furthermore, for any $\theta , \theta ^ { \prime } \in S _ { \Pi }$ , it holds that

$$
\sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \big \| \big | \widetilde { g } ( X _ { i } , \theta ) \widetilde { g } ( X _ { i } , \theta ) ^ { T } - \widetilde { g } ( X _ { i } , \theta ^ { \prime } ) \widetilde { g } ( X _ { i } , \theta ^ { \prime } ) ^ { T } \big \| \big \| _ { \mathrm { F } } ^ { 2 } } \le 2 d _ { n } ^ { \widetilde { g } } ( \theta , \theta ^ { \prime } ) .
$$

Using the uniform low via Rademacher complexity (see for example Theorem 4.10 of [72]) and Dudley’s entropy integral bound (see for example Theorem 5.22 of [72]), there exist constants $C _ { 2 } , C _ { 3 }$ so that it holds with probability at least $1 - n ^ { - 3 }$ that for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
\begin{array} { r l } & { \displaystyle \left\| \left| n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ) \widetilde { g } ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ \widetilde { g } ( X , \theta ) \widetilde { g } ( X , \theta ) ^ { T } \big ] \right| \right\| _ { \mathrm { F } } } \\ & { \leq C _ { 2 } \sqrt { \displaystyle \frac { \log n } { n } } + \frac { C _ { 2 } } { \sqrt { n } } \mathbb { E } \Big [ \int _ { 0 } ^ { 2 } \sqrt { \log \mathbf { N } ( B _ { r } ( \theta ^ { * } ) \cap \mathcal { M } , d _ { n } ^ { \widetilde { g } } , \varepsilon ) } \mathrm { d } \varepsilon \Big ] } \\ & { \leq C _ { 3 } \sqrt { \displaystyle \frac { \log n } { n } } . } \end{array}
$$

In addition, for any $\theta \in \mathcal { M }$ ,

$$
[ \| \widetilde { g } ( X , \theta ) - \widetilde { g } ( X , \theta ^ { * } ) \| ^ { 2 } ] \leq \frac { 1 } { C ^ { 2 } ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } } \mathbb { E } [ \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| ^ { 2 } ] \leq \frac { L } { C ^ { 2 } ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } } \| \theta - \theta ^ { * } \| ^ { 2 \beta _ { 2 } } .
$$

Moreover, for any $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
\begin{array} { r l } & { \overset \sim { / } ( X , \theta ) - \widetilde \ell ( X , \theta ^ { \prime } ) - \widetilde g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) ^ { 2 } \big ] \leq \frac { 1 } { C ^ { 2 } ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } } \mathbb { E } \big [ \big ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \big ) \big ] } \\ & { \qquad \leq \frac { L } { C ^ { 2 } ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } } } \| \theta - \theta ^ { * } \| ^ { 2 + 2 \beta _ { 2 } } . } \end{array}
$$

Following the proof of Lemma 24 in [69], we can obtain that there exists a constant $C _ { 4 }$ so that it holds with probability at least $1 - n ^ { - 3 }$ that

1. For any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ \widetilde { g } ( X , \theta ) ] + \mathbb { E } [ \widetilde { g } ( X , \theta ^ { * } ) ] \Big \Vert _ { 2 } \le C _ { 4 } \left( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| ^ { \beta _ { 2 } } + C _ { 4 } \right) ,
$$

2. For any $\theta , \theta ^ { \prime } \in S _ { \Pi }$ ,

$$
\eta ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { \ell } \big ( X _ { i } , \theta \big ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { \ell } \big ( X _ { i } , \theta ^ { \prime } \big ) - \mathbb { E } \big [ \widetilde { \ell } \big ( X , \theta \big ) \big ] + \mathbb { E } \big [ \widetilde { \ell } \big ( X , \theta ^ { \prime } \big ) \big ] \bigg | \leq C _ { 4 } \Big ( \sqrt { \frac { \log n } { n } } \ \| \theta - \theta ^ { \prime } \| + \frac { \log n } { n } \Big )
$$

3. For any $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
\begin{array} { r l r } & { } & { \displaystyle \left. n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde \ell ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde \ell ( X _ { i } , \theta ^ { \prime } ) - \frac 1 n \sum _ { i = 1 } ^ { n } \widetilde g ( X _ { i } , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) - \mathbb { E } [ \widetilde \ell ( X , \theta ) ] + \mathbb { E } [ \widetilde \ell ( X , \theta ^ { \prime } ) ] \right. } \\ & { } & { \left. + \mathbb { E } \left[ \widetilde g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \right] \right. \le C _ { 4 } \left( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 2 } + 1 } + \frac { \log n } { n } \| \theta - \theta ^ { \prime } \| + ( \frac { \log n } { n } ) ^ { 2 } \right) . } \end{array}
$$

Furthermore, by Hölder’s inequality, there exist constants $C _ { 5 } , C _ { 6 }$ so that for any $\theta \in S _ { \Pi }$ ,

$$
\begin{array} { r l } & { \left\| \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \cdot { \mathbf 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \big ] \right\| _ { \mathrm { F } } } \\ & { \leq C _ { 5 } \sqrt { \mathbb { E } \big [ b ( X ) ^ { 4 } \big ] } \sqrt { P ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } ) } } \\ & { \leq C _ { 6 } \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Similarly, for any $\theta , \theta ^ { \prime } \in S _ { \Pi }$ ,

$$
\begin{array} { r l } & { \left| \mathbb { E } \big [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) ) \cdot \mathbf { 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \big ] \right| } \\ & { ~ \leq \mathbb { E } \big [ b ( X ) \cdot \mathbf { 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \big ] \cdot \| \theta - \theta ^ { \prime } \| } \\ & { ~ \leq C _ { 6 } \frac { 1 } { n ^ { 2 } } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \left| \mathbb { E } \big [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) \cdot \mathbf { 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \big ] \right| } \\ & { \leq 2 \cdot \mathbb { E } \big [ b ( X ) \cdot \mathbf { 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } } \big ) \big ] \cdot \| \theta - \theta ^ { \prime } \| } \\ & { \leq C _ { 6 } \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Furthermore, notice that given $X ^ { ( n ) } \in \mathcal { A } _ { 1 }$ and $\begin{array} { r } {   n ^ { - 1 } \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ) \widetilde { g } ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ \widetilde { g } ( X , \theta ) \widetilde { g } ( X , \theta ) ^ { T } \big ]  _ { \mathrm { F } } \le } \end{array}$ $C _ { 3 } { \sqrt { \frac { \log n } { n } } }$ log n , it holds that

$$
\begin{array} { r l } & { \left\| { n } ^ { - 1 } \displaystyle { \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \big ] } \right\| _ { \mathrm { F } } } \\ & { = \left\| { C ^ { 2 } ( \log n ) } ^ { \frac { 2 } { n _ { 1 } } } \cdot n ^ { - 1 } \displaystyle { \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ) \widetilde { g } ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \big ] } \right\| _ { \mathrm { F } } } \\ & { \leq C ^ { 2 } ( \log n ) ^ { \frac { 2 } { n _ { 1 } } } \cdot \left\| { n } ^ { - 1 } \displaystyle { \sum _ { i = 1 } ^ { n } \widetilde { g } ( X _ { i } , \theta ) \widetilde { g } ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ \widetilde { g } ( X , \theta ) \widetilde { g } ( X , \theta ) ^ { T } \big ] } \right\| _ { \mathrm { F } } ^ { n } } \\ & { \qquad + \left\| { \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \cdot { \bf 1 } \big ( b ( X ) > C ( \log n ) ^ { \frac { 1 } { n _ { 1 } } } \big ) \big ] } \right\| _ { \mathrm { F } } } \\ & { \leq C _ { 1 } \displaystyle { \frac { ( \log n ) ^ { \frac { 2 } { n _ { 1 } } + \frac { 1 } { 2 } } } { \sqrt { n } } } . } \end{array}
$$

Therefore, $P ( X ^ { ( n ) } \in \mathcal { A } _ { 4 } ) \geq P ( X ^ { ( n ) } \in \mathcal { A } _ { 1 } \cap \mathcal { A } _ { 4 } ) \geq 1 - 2 n ^ { - 3 }$ . Proceeding analogously, we obtain the same type of bounds for $\mathbf { \mathcal { A } } _ { 5 } , \mathbf { \mathcal { A } } _ { 6 } , \mathbf { \mathcal { A } } _ { 7 }$ , and hence conclude the desired result.

# I.3 Proof of Lemma 6

Write $\begin{array} { r } { \widehat { \theta ^ { * } } = \widehat { \theta ^ { * } } ( X ^ { ( n ) } ) = \phi _ { \theta ^ { * } } \left( - W _ { \theta ^ { * } } \mathcal { H } _ { 0 } ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) \right) } \end{array}$ . Recall $\widetilde { \lambda } ( \theta ) = - \Delta _ { 0 } ^ { - 1 } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } ( \psi _ { \theta ^ { * } } ( \theta ) -$ $\psi _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } ) )$ , we have

$$
\begin{array} { l } { \displaystyle \big \| \Delta _ { 0 } ^ { - 1 } W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) + \widetilde { \lambda } ( \theta ) \big \| } \\ { = \displaystyle \left\| \Delta _ { 0 } ^ { - 1 } \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \right) \right\| . } \end{array}
$$

Since $X ^ { ( n ) } \in { \mathcal { A } }$ and $\mathbb { E } [ g ( X , \theta ^ { * } ) ] = 0 _ { D }$ , there exists a constant $C$ so that it holds for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ that,

$$
\begin{array} { r l } & { \Big | \Big | \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g \big ( X _ { i } , \theta \big ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g \big ( X _ { i } , \theta ^ { * } \big ) - \mathbb { E } [ W _ { \theta } ^ { T } g \big ( X , \theta \big ) ] + \mathbb { E } [ W _ { \theta ^ { * } } ^ { T } g ( X , \theta ^ { * } ) ] \Big | \Big | } \\ & { \le \Big \| W _ { \theta } ^ { T } \cdot \Big ( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g \big ( X _ { i } , \theta \big ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g \big ( X _ { i } , \theta ^ { * } \big ) - \mathbb { E } [ g \big ( X , \theta \big ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \Big ) \Big \| } \\ & { + \left\| ( W _ { \theta } - W _ { \theta ^ { * } } ) \cdot \big ( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g \big ( X _ { i } , \theta ^ { * } \big ) - \mathbb { E } [ g \big ( X , \theta ^ { * } \big ) ] \big ) \right\| } \\ & { \le C \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \sqrt { \displaystyle \frac { \log n } { n } } \| \theta - \theta ^ { * } \| ^ { \beta _ { 2 } } + \displaystyle \frac { \log n } { n } \Big ) . } \end{array}
$$

Consider the transformed risk function $\widetilde { \mathcal { R } } : B _ { r } ( 0 _ { d } ) \to \mathbb { R }$ defined by $\begin{array} { r } { \widetilde { \mathcal { R } } ( z ) = \mathcal { R } ( \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) = } \end{array}$ $\mathbb { E } [ \ell ( X , \phi _ { \theta ^ { * } } ( W _ { \theta ^ { * } } z ) ) ]$ . By Assumption 1 and 3, $\bar { \mathcal { R } }$ is thrice differentiable. Moreover, by proposition 5.44 of [15], we have $\mathcal { H } _ { 0 } = W _ { \theta ^ { * } } ^ { T } \mathcal { H } _ { \theta ^ { * } } W _ { \theta ^ { * } } = \mathrm { H e s s i a n } ( \widetilde { R } ( z ) | _ { z = 0 _ { d } } )$ . Let $\mathcal { H } _ { z }$ denote the Hessian matrix of $\mathcal { \widetilde { R } } ( \cdot )$ at $z$ , then $\mathcal { H } _ { z }$ is uniformly Lipshitz-continuous over $B _ { r } ( 0 _ { d } )$ . Hence, there exists a constant $C$ so that for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
\begin{array} { r l } & { \Big | \mathbb { E } [ W _ { \theta } ^ { T } g ( X , \theta ) ] - W _ { \theta ^ { * } } ^ { T } \mathbb { E } [ g ( X , \theta ^ { * } ) ] - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \Big | \Big | } \\ & { \leq \underset { \eta \in \mathbb { S } _ { 1 } ^ { d - 1 } } { \operatorname* { s u p } } \Big | \eta ^ { T } \nabla \widetilde { \mathcal { R } } ( W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) ) - \eta ^ { T } \nabla \widetilde { \mathcal { R } } ( 0 _ { d } ) - \eta ^ { T } \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \Big | } \\ & { \leq \underset { \eta \in \mathbb { S } _ { 1 } ^ { d - 1 } t \in ( 0 , 1 ) } { \operatorname* { s u p } } \Big | \eta ^ { T } ( \mathcal { H } _ { t W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) } - \mathcal { H } _ { 0 } ) W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \Big | } \\ & { \leq C \lVert \theta - \theta ^ { * } \rVert _ { 2 } ^ { 2 } . } \end{array}
$$

Therefore, for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ , it holds that

$$
\begin{array} { r l } & { \displaystyle \big \| \Delta _ { 0 } ^ { - 1 } W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) + \widetilde { \lambda } ( \theta ) \big \| } \\ & { \leq C \left( \log n \right) ^ { \frac { 1 } { \beta _ { 1 } } } \Big ( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \Big ) + C \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } . } \end{array}
$$

Moreover, notice that

$$
\begin{array} { l } { \displaystyle | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g \big ( X _ { i } , \theta \big ) | | \leq \Big \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g \big ( X _ { i } , \theta \big ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g \big ( X _ { i } , \theta ^ { * } \big ) - \mathbb { E } [ W _ { \theta } ^ { T } g \big ( X , \theta \big ) ] + \mathbb { E } [ W _ { \theta } ^ { T } g \big ( X , \theta \big ) ] } \\ { \displaystyle + \Big \| \mathbb { E } [ W _ { \theta } ^ { T } g ( X , \theta ) ] - W _ { \theta ^ { * } } ^ { T } \mathbb { E } [ g ( X , \theta ^ { * } ) ] - \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } \psi _ { \theta ^ { * } } ( \theta ) \Big \| + \| \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } ( \theta - \theta ^ { * } ) \| + \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta ^ { * } } ^ { T } g } \\ { \leq C \left( \log n \right) ^ { \frac { 1 } { n } } \Big ( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| ^ { \beta _ { 2 } } + \frac { \log n } { n } \Big ) + C \left\| \theta - \theta ^ { * } \right\| _ { 2 } ^ { 2 } + \| \mathcal { H } _ { 0 } W _ { \theta ^ { * } } ^ { T } ( \theta - \theta ^ { * } ) \| + C _ { 1 } \sqrt { \frac { \log k } { \eta } } } \\ { \lesssim \| \theta - \theta ^ { * } \| + \sqrt { \frac { \log n } { n } } . } \end{array}
$$

(52) Consequently, there exist constant C1, C2, C3 so that for any θ ∈ M with ∥θ − θ∗∥ ≤ δ (log n) 32 √n , we have

$$
\begin{array} { r l } & { \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \tilde { A } \{ \theta \} ^ { \top \top } W _ { i } ^ { \theta } S _ { i } ^ { \theta } ( X _ { i } , \theta ) \right\| W _ { i } ^ { \theta } S _ { i } ^ { \theta } ( X , \theta ) \right) } \\ & { = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( - ( \Delta _ { i } \cdot ( W _ { i } ) ^ { \top } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \tilde { N } _ { i } \zeta ) ^ { \top } W _ { i } ^ { \theta } S _ { i } ( X _ { i } , \theta ) \right) W _ { i } ^ { \theta } S _ { i } ( X , \theta ) \Big \| } \\ & { = - \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( - ( \Delta _ { i } \cdot ( W _ { i } ) ^ { \top } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \tilde { N } _ { i } \zeta ) ^ { \top } W _ { i } ^ { \theta } S _ { i } ( X _ { i } , \theta ) \right) ^ { \top } C _ { i } ( X _ { i } , \theta ) \right\| } \\ & { = - \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \tilde { A } \{ \theta \} ^ { \top \top } W _ { i } ^ { \theta } \tilde { \theta } ^ { \top } ( X _ { i } , \theta ) \right\| W _ { i } ^ { \theta } S _ { i } ( X _ { i } , \theta ) \right) \cdot \nabla _ { i } \zeta \left\| \tilde { \theta } ^ { \top } ( X _ { i } ) \zeta _ { i } ( X _ { i } , \theta ) \right\| ^ { \top } S _ { i } ( X _ { i } , \theta ) \right\| } \\ &  \qquad - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( - ( \Delta _ { i } \cdot W _ { i } ^ { \theta } ) ^ { \top } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \tilde { \theta } ^ { \top }  \end{array}
$$

Furthermore, using $| \exp ( x ) - ( 1 + x ) | \leq x ^ { 2 }$ for $x \in [ - 1 , 1 ]$ , and the Lipschitz continuity of $\overline { { \Delta } } _ { \theta }$ around θ∗, there exist constant C1, C2, C3 so that for any θ ∈ M with ∥θ − θ∗∥ ≤ δ (log n) 32 √n ,

$$
\begin{array} { r l } & { \displaystyle \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( - \big ( \Delta _ { 0 } ^ { - 1 } W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g \big ( X _ { j } , \theta \big ) \big ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right. } \\ & { \displaystyle - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) + \frac { 1 } { n } \sum _ { j = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { j } , \theta ) g ( X _ { j } , \theta ) ^ { T } W _ { \theta } \cdot \Delta _ { 0 } ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Bigg \| } \\ & { \displaystyle \leq C _ { 1 } \big \| \Delta _ { 0 } ^ { - 1 } W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \big \| ^ { 2 } \cdot \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) \| ^ { 3 } \cdot \mathbf { 1 } ( b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \mathcal { R } _ { 1 } } } ) } \\ & { \displaystyle \leq C _ { 2 } \Big ( \big \| \theta - \theta ^ { * } \big \| + \sqrt { \frac { \log n } { n } } \Big ) ^ { 2 } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \left\| I _ { d } - n ^ { - 1 } \displaystyle \sum _ { j = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { j } , \theta ) g ( X _ { j } , \theta ) ^ { T } W _ { \theta } \Delta _ { 0 } ^ { - 1 } \right\| } \\ & { = \left\| W _ { \theta ^ { * } } ^ { T } \Delta _ { \theta ^ { * } } W _ { \theta ^ { * } } \Delta _ { 0 } ^ { - 1 } - n ^ { - 1 } \displaystyle \sum _ { j = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { j } , \theta ) g ( X _ { j } , \theta ) ^ { T } W _ { \theta } \Delta _ { 0 } ^ { - 1 } \right\| } \\ & { \leq C _ { 1 } \Big ( \left\| \Delta _ { \theta ^ { * } } - \Delta _ { \theta } \right\| _ { \mathrm { F } } + \left\| W _ { \theta ^ { * } } - W _ { \theta } \right\| _ { \mathrm { F } } + \left\| | n ^ { - 1 } \displaystyle \sum _ { j = 1 } ^ { n } g ( X _ { j } , \theta ) g ( X _ { j } , \theta ) ^ { T } - \Delta _ { \theta } \right\| _ { \mathrm { F } } \Big ) } \\ & { \leq C _ { 2 } \left\| \theta - \theta ^ { * } \right\| + C _ { 2 } \frac { \left( \log n \right) ^ { \frac { 2 } { \beta _ { 1 } } + \frac { 1 } { 2 } } } { \sqrt { n } } , } \end{array}
$$

which leads to

$$
\begin{array} { r l } & { \Big \| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( - \big ( \Delta _ { 0 } ^ { - 1 } W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( X _ { j } , \theta ) \big ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big \| } \\ & { \leq \Big \| \Big ( I _ { d } - n ^ { - 1 } \displaystyle \sum _ { j = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { j } , \theta ) g ( X _ { j } , \theta ) ^ { T } W _ { \theta } \Delta _ { 0 } ^ { - 1 } \Big ) \frac { 1 } { n } \sum _ { i = 1 } ^ { n } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big \| } \\ & { \quad + C _ { 2 } \Big ( \| \theta - \theta ^ { * } \| + \sqrt { \displaystyle \frac { \log n } { n } } \Big ) ^ { 2 } , } \\ & { \leq C _ { 3 } \Big ( \| \theta - \theta ^ { * } \| + \sqrt { \displaystyle \frac { \log n } { n } } \Big ) \cdot \Big ( \| \theta - \theta ^ { * } \| + \frac { ( \log n ) ^ { \frac { 2 } { \beta _ { 1 } } + \frac { 1 } { 2 } } } { \sqrt { n } } \Big ) . } \end{array}
$$

Together with (53), we can obtain that there exists a constant $C$ such that, for any $\theta \in \mathcal { M }$ with ∥θ − θ∗∥ ≤ δ (log n) 32 √ ,

$$
\begin{array} { r l } & { \Big \| \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \exp \left( \widetilde { \lambda } ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big \| } \\ & { \leq C \left( \log n \right) ^ { \frac { 2 } { \beta _ { 1 } } } \Big ( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \Big ) + C \| \theta - \theta ^ { * } \| ^ { 2 } . } \end{array}
$$

Fix any θ ∈ M with ∥θ − θ∗∥ ≤ δ (log n) 32 √n . Set $\begin{array} { r } { v = \frac { \widetilde \lambda ( \theta ) - \lambda ( \theta ) } { \| \widetilde \lambda ( \theta ) - \lambda ( \theta ) \| } } \end{array}$ and $a = \lVert \widetilde { \lambda } ( \theta ) - \lambda ( \theta ) \rVert$ . Define the function $f : \mathbb { R } _ { \geq 0 } \to \mathbb { R }$ by

$$
f ( t ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \big ( \lambda ( \theta ) + t \cdot v \big ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) ,
$$

then $f$ has a first-order derivative

$$
\boldsymbol { f } ^ { \prime } ( t ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \big ( \lambda ( \theta ) + t \cdot v \big ) ^ { T } \boldsymbol { W } _ { \theta } ^ { T } \boldsymbol { g } ( X _ { i } , \theta ) \Big ) \cdot \boldsymbol { v } ^ { T } \boldsymbol { W } _ { \theta } ^ { T } \boldsymbol { g } ( X _ { i } , \theta ) ,
$$

and a second-order derivative

$$
\boldsymbol { f } ^ { \prime \prime } ( t ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \big ( \boldsymbol { \lambda } ( \theta ) + t \cdot \boldsymbol { v } \big ) ^ { T } \boldsymbol { W } _ { \theta } ^ { T } \boldsymbol { g } ( X _ { i } , \theta ) \Big ) \cdot \boldsymbol { v } ^ { T } \boldsymbol { W } _ { \theta } ^ { T } \boldsymbol { g } ( X _ { i } , \theta ) \boldsymbol { g } ( X _ { i } , \theta ) ^ { T } \boldsymbol { W } _ { \theta } \boldsymbol { v } .
$$

Then it holds that $f ^ { ' } ( 0 ) = 0$ , and $f ^ { \prime \prime } ( t ) > 0$ for $t > 0$ , so $f ^ { ' } ( \cdot )$ is non-decreasing on $[ 0 , \infty )$ Moreover, it holds that

$$
\begin{array} { r l } & { f ^ { \prime } ( a ) = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \widetilde { \lambda } ( \theta ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \right) \displaystyle \frac { \left( \widetilde { \lambda } ( \theta ) - \lambda ( \theta ) \right) ^ { T } } { \| \widetilde { \lambda } ( \theta ) - \lambda ( \theta ) \| } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) } \\ & { \le C \left( \log n \right) ^ { \frac { 2 } { \beta _ { 1 } } } \left( \displaystyle \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \right) + C \left\| \theta - \theta ^ { * } \right\| ^ { 2 } } \\ & { \lesssim \displaystyle \frac { ( \log n ) ^ { 3 } } { n } + \frac { ( \log n ) ^ { \frac { 1 } { 2 } + \frac { 2 } { \beta _ { 1 } } + \frac { 3 \beta _ { 2 } } { 2 } } } { n ^ { \frac { 1 } { 2 } + \frac { \beta _ { 2 } } { 2 } } } . } \end{array}
$$

We will first show $a = \lVert \widetilde { \lambda } ( \theta ) - \lambda ( \theta ) \rVert \lesssim \left( \log n \right) ^ { - \frac { 1 } { \beta _ { 1 } } }$ . Let’s suppose $a > C ( \log n ) ^ { - { \frac { 1 } { \beta _ { 1 } } } }$ with a positive constant $C$ . Then

$$
f ^ { ' } ( a ) \geq f ^ { ' } \Big ( a - \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } \Big ) .
$$

On the other hand, we have $\begin{array} { r } { \| \widetilde \lambda ( \theta ) \| \lesssim \frac { ( \log n ) ^ { 3 / 2 } } { \sqrt { n } } } \end{array}$ , and $\| g ( X _ { i } , \theta ) \| \leq b ( X _ { i } ) \leq C ( \log n ) ^ { \frac { 1 } { \beta _ { 1 } } }$ holds for any $i \in [ n ]$ . Thus, there exists a positive constant $C _ { 1 }$ so that for any $\begin{array} { r } { t \in [ a - \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } , a ] } \end{array}$ and any $i \in [ n ]$

$$
\begin{array} { r } { \exp \Big ( \big ( \lambda ( \theta ) + t \cdot v \big ) ^ { T } W _ { \theta } ^ { T } g ( X _ { i } , \theta ) \Big ) \geq C _ { 1 } . } \end{array}
$$

Furthermore, note that for $W _ { \theta } = \mathbf { J } _ { \phi _ { \theta ^ { \ast } } ( W _ { \theta ^ { \ast } } y ) } ( y = W _ { \theta ^ { \ast } } ^ { I ^ { \prime } } \psi _ { \theta ^ { \ast } } ( \theta ) )$ , there exists a positive constant $C _ { 2 }$ so that for any $\theta \in B _ { r } ( \theta ^ { * } ) \cap \mathcal { M }$ ,

$$
\left\| W _ { \theta } - W _ { \theta ^ { * } } \right\| _ { \mathrm { F } } \leq C _ { 2 } \left\| \theta - \theta ^ { * } \right\| .
$$

Combined with $\lVert \Delta _ { \theta } - \Delta _ { \theta ^ { * } } \rVert \leq L \lVert \theta - \theta ^ { * } \rVert$ and $W _ { \theta ^ { * } } ^ { T } \Delta _ { \theta ^ { * } } W _ { \theta ^ { * } } \succcurlyeq L _ { 1 } I _ { d }$ for $L _ { 1 } > 0$ , there exists a small enough positive constant $r _ { 1 }$ so that for any $\theta \in B _ { r _ { 1 } } ( \theta ^ { * } ) \cap { \mathcal { M } }$ ,

$$
W _ { \theta } ^ { T } \Delta _ { \theta } W _ { \theta } \asymp \frac { L _ { 1 } } { 2 } I _ { d } ,
$$

and

$$
W _ { \theta } ^ { T } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } W _ { \theta } \succcurlyeq \frac { L _ { 1 } } { 4 } I _ { d } .
$$

Therefore, for any $\begin{array} { r } { t \in [ a - \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } , a ] } \end{array}$ , it holds that $\begin{array} { r } { f ^ { \prime \prime } ( t ) \geq \frac { L _ { 1 } } { 4 } C _ { 1 } : = C _ { 2 } > 0 } \end{array}$ . Thus, when $n$ is sufficiently large,

$$
f ( a - \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } ) - f ( a ) \geq - f ^ { ' } ( a ) \cdot \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } + \frac { C _ { 2 } } { 2 } ( \frac { C } { 2 } ( \log n ) ^ { - \frac { 1 } { \beta _ { 1 } } } ) ^ { 2 } > 0 ,
$$

which cause contradiction. Therefore, we have $a \leq C ( \log n ) ^ { - { \frac { 1 } { \beta _ { 1 } } } }$ , and there exists a positive constant $C _ { 3 }$ so that for any $t \in [ 0 , a ]$ , it holds that

$$
f ^ { \prime \prime } ( t ) \geq C _ { 3 }
$$

So we can get

$$
f ^ { ' } ( a ) = f ^ { ' } ( a ) - f ^ { ' } ( 0 ) \geq C _ { 3 } a \Rightarrow a \leq \frac { f ^ { ' } ( a ) } { C _ { 3 } } .
$$

Thus there exists a constant C so that for any θ ∈ M with ∥θ − θ∗∥ ≤ δ (log n) 32 √n ,

$$
\| \widetilde \lambda ( \theta ) - \lambda ( \theta ) \| \leq C \left( \log n \right) ^ { \frac { 2 } { \beta _ { 1 } } } \left( \frac { \log n } { n } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta _ { 2 } } \right) + C \| \theta - \theta ^ { * } \| ^ { 2 } .
$$

# I.4 Proof of Lemma 7

Firstly if $z _ { 2 } \not \in K$ , then we have $G ( z _ { 2 } ) \notin K _ { \theta }$ , and thus $\mathcal { A } ^ { * } ( z _ { 1 } , z _ { 2 } ) = \mathcal { A } ( G ( z _ { 1 } ) , G ( z _ { 2 } ) ) = 0$ . So it remains to show that for any $z _ { 1 } \in K$ and $z _ { 2 } \in [ Q \circ \widetilde { \phi } _ { G ( z _ { 1 } ) } ^ { * } ] \bigl ( \Omega _ { G ( z _ { 1 } ) } \bigr ) \cap K$ ,

$$
\alpha ^ { * } ( z _ { 1 } , z _ { 2 } ) = \frac { \widetilde { \eta } _ { G ( z _ { 2 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 2 } ) ) \cdot p ( G ( z _ { 2 } ) , G ( z _ { 1 } ) ) } { \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 1 } ) ) \cdot p ( G ( z _ { 1 } ) , G ( z _ { 2 } ) ) } .
$$

We claim that it suffices to show that for any $z \in Q ( B _ { r } ( \widetilde { \theta } ) \cap \mathcal { M } )$ and $x \in B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } }$ ,

$$
\operatorname* { d e t } \bigl ( J _ { G } ( z ) ^ { T } J _ { G } ( z ) \bigr ) = \Bigl ( \operatorname* { d e t } \bigl ( J _ { \widetilde { \psi } _ { x } ^ { * } \circ G } ( z ) \bigr ) \Bigr ) ^ { 2 } \cdot \operatorname* { d e t } \bigl ( J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) ^ { T } J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) \bigr ) .
$$

Indeed, under (55), when $z _ { 1 } \in ( Q \circ \tilde { \phi } _ { G ( z _ { 2 } ) } ^ { * } ) ( \Omega _ { G ( z _ { 2 } ) } )$ and $z _ { 2 } \in K$ , we have

$$
\begin{array} { r l } { \Dot { \varepsilon } ^ { * } ( z _ { 1 } , z _ { 2 } ) = } & { \frac { \widetilde { \eta } _ { G ( z _ { 3 } ) } \cdot p ^ { * } ( z _ { 2 } , z _ { 1 } ) \mu _ { G ( z _ { 2 } ) } ^ { * } ( z _ { 2 } ) } { \widetilde { \eta } ( G ( z _ { 1 } ) \cdot p ^ { * } ( z _ { 1 } , z _ { 2 } ) ) \mu _ { t o t } ^ { * } ( z _ { 1 } ) } } \\ & { = } &  \frac { \widetilde { \eta } ( \widetilde { \nu } _ { G ( z _ { 2 } ) } ^ { * } ) ^ { \alpha } ( G ( z _ { 1 } ) ) \cdot \big | \operatorname* { d e t } \big ( \mathbf { J } _ { \widetilde { \nu } _ { G ( z _ { 2 } ) ^ { * G G } } ( z _ { 1 } ) } \big ) \big | \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 2 } ) ) \cdot \sqrt { \operatorname* { d e t } \big ( \mathbf { J } _ { G ( z ( 2 ) ^ { * T } ] _ { G } ( z _ { 2 } ) } \big ) } } { \widetilde { \eta } ( \widetilde { \nu } _ { G ( z _ { 4 } ) } ^ { * } ) ^ { \alpha } ( G ( z _ { 2 } ) ) \cdot \big | \operatorname* { d e t } \big ( \mathbf { J } _ { \widetilde { \nu } _ { G ( z _ { 3 } ) } ^ { * } ) ^ { \alpha } ( G ( z _ { 2 } ) ) } \big | \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 1 } ) ) \cdot \sqrt { \operatorname* { d e t } \big ( \mathbf { J } _ { G ( z ( 2 ) ^ { * T } ] ^ { \widetilde { \nu } _ { \mathbf { J } _ { G } ( z _ { 1 } ) } } } } } \\ &  = \frac  \widetilde { \eta } ( \widetilde { \nu } _ { G ( z _ { 4 } ) } ^ { * } ) ^ { \alpha } ( G ( z _ { 2 } ) ) \cdot \big | \operatorname* { d e t } \big ( \mathbf { J } _  \widetilde { \nu } _ { G ( z _ { 3 } ) } ^ { * } ) ^  \alpha  \end{array}
$$

where $( i )$ uses equation (55) and $K _ { \theta } \subseteq B _ { r } ( { \widetilde { \theta } } ) \cap { \mathcal { M } }$ ; the last inequality uses the definition of $p ( \cdot , \cdot )$ in (40). On the other hand, when $z _ { 1 } \not \in ( Q \circ \phi _ { G ( z _ { 2 } ) } ^ { * } ) ( \Omega _ { G ( z _ { 2 } ) } )$ , we have $G ( z _ { 1 } ) \not \in \widetilde { \phi } _ { G ( z _ { 2 } ) } ^ { * } ( \Omega _ { G ( z _ { 2 } ) } )$ , and thus

$$
\alpha ^ { * } ( z _ { 1 } , z _ { 2 } ) = 0 = \frac { \widetilde { \eta } _ { G ( z _ { 2 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 2 } ) ) \cdot p ( G ( z _ { 2 } ) , G ( z _ { 1 } ) ) } { \widetilde { \eta } _ { G ( z _ { 1 } ) } \cdot \mu ^ { * } | _ { K _ { \theta } } ( G ( z _ { 1 } ) ) \cdot p ( G ( z _ { 1 } ) , G ( z _ { 2 } ) ) } .
$$

Now we show claim (55). For any $z \in Q ( B _ { r } ( \widetilde { \theta } ) \cap \mathcal { M } )$ and $x \in B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } }$ , we have

$$
\widetilde { \phi } _ { x } ^ { * } \circ \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) = G ( z ) ,
$$

thus

$$
J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) \cdot J _ { \widetilde { \psi } _ { x } ^ { * } \circ G } ( z ) = J _ { G } ( z ) .
$$

Therefore,

$$
\begin{array} { r l } & { J _ { G } ( z ) ^ { T } J _ { G } ( z ) = J _ { \widetilde { \psi } _ { x } ^ { * } \circ G } ( z ) ^ { T } J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) ^ { T } J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) \cdot J _ { \widetilde { \psi } _ { x } ^ { * } \circ G } ( z ) } \\ & { \qquad \quad \Longleftrightarrow \operatorname* { d e t } \bigl ( J _ { G } ( z ) ^ { T } J _ { G } ( z ) \bigr ) = \Bigl ( \operatorname* { d e t } \bigl ( J _ { \widetilde { \psi } _ { x } ^ { * } \circ G } ( z ) \bigr ) \Bigr ) ^ { 2 } \cdot \operatorname* { d e t } \bigl ( J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) ^ { T } J _ { \widetilde { \phi } _ { x } ^ { * } } ( \widetilde { \psi } _ { x } ^ { * } \circ G ( z ) ) \bigr ) , } \end{array}
$$

which proves claim (55).

# I.5 Proof of Lemma 11

Since $B _ { r } ( 0 _ { D } ) \cap T _ { \theta } { \mathcal { M } } \subset V _ { \theta }$ holds for $\theta \in B _ { r } ( \widetilde { \theta } ) \cap { \mathcal { M } }$ , when $R \leq c { \sqrt { n } }$ for a small enough $n$ - independent constant $c$ and $x \in K$ , we have $K \subseteq ( Q \circ \widetilde { \phi } _ { G ( x ) } ) ( \Omega _ { G ( x ) } )$ , where recall $\Omega _ { \theta } = \{ v \in$ $\mathbb { R } ^ { d } : \widetilde { W } _ { \theta } v \in V _ { \theta } \}$ . Therefore, when $x , y \in K$ ,

$$
\widetilde { \eta } _ { G ( x ) } \cdot p ^ { * } ( x , y ) = \widetilde { p } _ { G ( x ) } ( \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G ( y ) ) \cdot \left| \operatorname* { d e t } \bigl ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G } ( y ) \bigr ) \right| .
$$

Moreover, for any $x , y \in K$ , we have

$$
\begin{array} { r l } { \tilde { \psi } _ { G ( x ) } ^ { * } \circ G ( y ) = \widetilde { W } _ { G ( x ) } ^ { T } \tilde { \psi } _ { G ( x ) } \big ( \tilde { \phi } _ { \tilde { \theta } } \big ( W _ { \tilde { \theta } } \frac { y } { \sqrt { n } } \big ) \big ) } & { } \\ & { = \widetilde { W } _ { G ( x ) } ^ { T } \Big ( \tilde { \phi } _ { \tilde { \theta } } \big ( W _ { \tilde { \theta } } \frac { y } { \sqrt { n } } \big ) - G ( x ) \Big ) + O \Big ( \big \| \tilde { \phi } _ { \tilde { \theta } } \big ( W _ { \tilde { \theta } } \frac { y } { \sqrt { n } } \big ) - G ( x ) \big \| ^ { 2 } \Big ) } \\ & { = \widetilde { W } _ { G ( x ) } ^ { T } \big ( \tilde { \theta } + W _ { \tilde { \theta } } \frac { y } { \sqrt { n } } - G ( x ) \big ) + O \Big ( \big \| \tilde { \theta } + W _ { \tilde { \theta } } \frac { y } { \sqrt { n } } - G ( x ) \big \| ^ { 2 } \Big ) + O \Big ( \frac { \big \| y \big \| ^ { 2 } } { n } \Big ) } \\ & { = \widetilde { W } _ { G ( x ) } ^ { T } \big ( W _ { \tilde { \theta } \sqrt { n } } - W _ { \tilde { \theta } } \frac { x } { \sqrt { n } } \big ) + O \Big ( \big \| W _ { \tilde { \theta } \sqrt { n } } - W _ { \tilde { \theta } } \frac { x } { \sqrt { n } } \big \| ^ { 2 } \Big ) + O \Big ( \frac { \big \| y \big \| ^ { 2 } + \big \| x \big \| ^ { 2 } } { n } \Big ) } \\ & { = \widetilde { W } _ { G ( x ) } ^ { T } W _ { \tilde { \theta } } \frac { y - x } { \sqrt { n } } + O \Big ( \frac { \big \| \widetilde { \eta } \big \| _ { \infty } R ^ { 2 } } { n } \Big ) . } \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { n \cdot ( \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G ( y ) ) ^ { T } ( \widetilde { W } _ { G ( x ) } ^ { T } \widetilde { I W } _ { G ( x ) } ) ^ { - 1 } ( \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G ( y ) ) } \\ & { = ( y - x ) ^ { T } W _ { \overline { { \theta } } } ^ { T } \widetilde { W } _ { G ( x ) } ( \widetilde { W } _ { G ( x ) } ^ { T } \widetilde { I W } _ { G ( x ) } ) ^ { - 1 } \widetilde { W } _ { G ( x ) } ^ { T } W _ { \overline { { \theta } } } ( y - x ) + O \Big ( \frac { R ^ { 3 } } { \sqrt { n } } \| \widetilde { I } \| _ { \infty } ^ { \frac { 3 } { 2 } } \| \widetilde { I } ^ { - 1 } \| _ { \infty } \Big ) } \\ & { = ( y - x ) ^ { T } ( W _ { \overline { { \theta } } } ^ { T } \widetilde { I W } _ { \overline { { \theta } } } ) ^ { - 1 } ( y - x ) + O \Big ( \frac { R ^ { 3 } } { \sqrt { n } } \| \widetilde { I } \| _ { \infty } ^ { \frac { 3 } { 2 } } \| \widetilde { I } ^ { - 1 } \| _ { \infty } + \frac { R } { \sqrt { n } } \| \widetilde { I } \| _ { \infty } \| \widetilde { I } ^ { - 1 } \| _ { \infty } + \frac { R } { \sqrt { n } } \| \widetilde { I } ^ { - 1 } \| _ { \infty } } \end{array}
$$

Furthermore, since for any $z \in B _ { r } ( 0 _ { d } )$ ,

$$
\begin{array} { r } { \widetilde { \psi } _ { G ( x ) } ^ { * } \circ \widetilde { \phi } _ { G ( x ) } ^ { * } ( z ) = z , } \end{array}
$$

we have

$$
\mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( \widetilde { \phi } _ { G ( x ) } ^ { * } ( z ) \big ) \mathbf { J } _ { \widetilde { \phi } _ { G ( x ) } ^ { * } } ( z ) = I _ { d } .
$$

For $x , y \in K$ , choose $z = { \tilde { \psi } } _ { G ( x ) } ^ { * } ( G ( y ) )$ , we have

$$
\mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \bigl ( G ( y ) \bigr ) \mathbf { J } _ { \widetilde { \phi } _ { G ( x ) } ^ { * } } \bigl ( \widetilde { \psi } _ { G ( x ) } ^ { * } ( G ( y ) ) \bigr ) = I _ { d } .
$$

Then by Assumption B.1, there exist some $n$ -independent constants $C _ { 1 } , C _ { 2 } , C _ { 3 } , C _ { 4 }$ so that,

$$
\| \mathbf { J } _ { \widetilde { \phi } _ { G ( x ) } ^ { * } } \big ( \widetilde { \psi } _ { G ( x ) } ^ { * } ( G ( y ) ) \big ) - \widetilde { W } _ { G ( x ) } \| _ { \mathbf { \phi } _ { \mathrm { o p } } } \leq C _ { 1 } \| \widetilde { \psi } _ { G ( x ) } ( G ( y ) ) \| \leq C _ { 2 } \frac { L } { \sqrt { n } } \| y - x \| + C _ { 2 } \frac { R ^ { 2 } } { n } \leq C _ { 3 } \frac { R } { \sqrt { n } } ,
$$

and

$$
\| \| \sqrt { n } \cdot \mathbf { J } _ { G } ( y ) - W _ { \widetilde { \theta } } \| _ { \mathrm { o p } } = \| \mathbf { J } _ { \widetilde { \phi } _ { \widetilde { \theta } } ^ { * } } ( y / \sqrt { n } ) - W _ { \widetilde { \theta } } \| _ { \mathrm { o p } } \leq C _ { 4 } \frac { R } { \sqrt { n } } .
$$

We can obtain that for any $x , y \in K$ ,

$$
\begin{array} { r l } & { \mathrm { d e t } \Big ( \sqrt { n } \cdot \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G } ( y ) \Big ) - 1 \Big | \leq \Big | \mathrm { d e t } \Big ( \sqrt { n } \cdot \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } \circ G } ( y ) \Big ) - \mathrm { d e t } \Big ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( G ( y ) \big ) \cdot W _ { \widetilde { \theta } } \Big ) \Big | } \\ & { \qquad + | \mathrm { d e t } \Big ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( G ( y ) \big ) \cdot W _ { \widetilde { \theta } } \Big ) - \mathrm { d e t } \Big ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( G ( y ) \big ) \cdot \widetilde { W } _ { G ( x ) } \Big ) | } \\ & { \qquad + | \mathrm { d e t } \Big ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( G ( y ) \big ) \cdot \widetilde { W } _ { G ( x ) } \Big ) - \mathrm { d e t } \Big ( \mathbf { J } _ { \widetilde { \psi } _ { G ( x ) } ^ { * } } \big ( G ( y ) \big ) \mathbf { J } _ { \widetilde { \phi } _ { G ( x ) } ^ { * } } \big ( \widetilde { \psi } _ { G ( x ) } ^ { * } \big ) } \\ & { \qquad \lesssim \frac { R } { \sqrt { n } } , } \end{array}
$$

where the last step uses equation (57), (56) and the fact that $\lVert \widetilde { \theta } - G ( x ) \rVert \lesssim R / \sqrt { n }$ for $x \in K$ We can then obtain the desired result by combining all pieces.

# I.6 Proof of Lemma 12

Recall $\overline { { u } } = \mathcal { N } ( 0 , J ^ { - 1 } )$ and $p ^ { \Delta } ( x , \cdot ) = \mathcal { N } ( x , 2 h I ^ { \Delta } )$ , we have

$$
\begin{array} { l } { \displaystyle \int \left| p ^ { \Delta } ( x , y ) - \frac { \overline { \mu } ( y ) p ^ { \Delta } ( y , x ) } { \overline { \mu } ( x ) } \right| \mathrm { d } y } \\ { = \displaystyle \int \frac { 1 } { ( 4 \pi h ) ^ { \frac { d } { 2 } } } \left| \exp \left( - \frac { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( y - x ) \| ^ { 2 } } { 4 h } \right) - \exp \left( \frac { x ^ { T } J x - y ^ { T } J y } { 2 } \right) \exp \left( - \frac { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } \cdot ( x - y ) \| ^ { 2 } } { 4 h } \right) \right| } \\ { = \displaystyle \int \frac { 1 } { ( 4 \pi h ) ^ { \frac { d } { 2 } } } \exp \left( - \frac { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } \cdot ( y - x ) \| ^ { 2 } } { 4 h } \right) \left| 1 - \exp \left( \frac { x ^ { T } J x - y ^ { T } J y } { 2 } \right) \right| \mathrm { d } y . } \end{array}
$$

Let $\begin{array} { r } { u = \frac { ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( y - x ) } { \sqrt { 2 h } } } \end{array}$ in the above integral, then consider $u \sim \mathcal { N } ( 0 , I _ { d } )$ , we have

$$
\begin{array} { r l } & { \displaystyle \int \left| p ^ { \Delta } ( x , y ) - \frac { \overline { { \mu } } ( y ) p ^ { \Delta } ( y , x ) } { \overline { { \mu } } ( x ) } \right| \mathrm { d } y } \\ & { = \mathbb { E } _ { u \sim { \mathcal { N } } ( 0 , I _ { d } ) } \left[ \left| 1 - \exp \left( \frac { x ^ { T } J x - ( x + \sqrt { 2 h } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } u ) ^ { T } J ( x + \sqrt { 2 h } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } u ) } { 2 } \right) \right| \right] } \\ & { = \mathbb { E } _ { u \sim { \mathcal { N } } ( 0 , I _ { d } ) } \left[ \left| 1 - \exp \left( - h \cdot u ^ { T } J ^ { \Delta } u - \sqrt { 2 h } \cdot u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x \right) \right| \right] . } \end{array}
$$

Let

$$
\mathcal { B } = \left\{ u \in \mathbb { R } ^ { d } : \left| h \cdot u ^ { T } J ^ { \Delta } u + \sqrt { 2 h } \cdot u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x \right| \leq \frac { 1 } { 4 9 } \right\} ,
$$

then by Hölder inequality, we have

$$
\begin{array} { r l } & { \displaystyle \int \left| p ^ { \Delta } ( x , y ) - \frac { \overline { \mu } ( y ) p ^ { \Delta } ( y , x ) } { \overline { \mu } ( x ) } \right| \mathrm { d } y } \\ & { \leq \exp ( 1 / 4 9 ) - 1 + \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] } \\ & { \quad + \sqrt { \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] } \cdot \left( \mathbb { E } _ { u } \left[ \exp ( - 4 h \cdot u ^ { T } J ^ { \Delta } u ) \right] \cdot \mathbb { E } _ { u } \left[ \exp ( - 4 \sqrt { 2 h } u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x ) \right] \right) ^ { \frac { 1 } { 4 } } } \\ & { \leq 1 / 4 8 + \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] + \sqrt { \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] } \cdot \left( \mathbb { E } _ { u } \left[ \exp ( - 4 h \cdot u ^ { T } J ^ { \Delta } u ) \right] \cdot \mathbb { E } _ { u } \left[ \exp ( - 4 \sqrt { 2 h } u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J ^ { \Delta } u ) \right] \right) \cdot \mathbb { E } _ { u } \left[ \exp ( - 4 \sqrt { 2 h } u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J ^ { \Delta } u ) \right] } \end{array}
$$

where we use the shorthand $\mathbb { E } _ { u }$ to denote $\mathbb { E } _ { u \sim \mathcal { N } ( 0 , I _ { d } ) }$ . Then by (1) $h \leq \sqrt { c _ { 0 } } ( { \mathrm { t r } } ( J ^ { \Delta } ) + r _ { d } ) ^ { - 1 }$ with $\begin{array} { r } { r _ { d } = \left\{ \left( \sqrt { c ^ { \prime } \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } } \| J ^ { \Delta } \| _ { \mathrm { F } } \right) \vee \left( c ^ { \prime } \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } \rho _ { 2 } ^ { 2 } \right) \right\} \wedge ( \rho _ { 2 } ^ { 2 } R ^ { 2 } ) } \end{array}$ and $\begin{array} { r } { R \geq C ( \frac { d } { \rho _ { 1 } } ) ^ { \frac { 1 } { 2 } } } \end{array}$ ; (2) $x \in E = \{ x \in$ K : ∥(I∆) 12 J x∥2 − tr(J ∆) ≤ rd}, it holds that for 0 ≤ t ≤ 14hλmax(J∆) ,

$$
\begin{array} { r l r } {  { \mathbb { E } _ { u } [ \exp ( t h \cdot u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } u ) ] = \prod _ { j = 1 } ^ { d } \frac { 1 } { \sqrt { 1 - 2 t h \cdot \lambda _ { j } ( J ^ { \Delta } ) } } } } \\ & { } & { \leq \exp ( 2 t h \cdot \mathrm { t r } ( J ^ { \Delta } ) ) \leq \exp ( 2 t \sqrt { c _ { 0 } } ) , } \end{array}
$$

where $\{ \lambda _ { j } ( J ^ { \Delta } ) \} _ { j = 1 } ^ { d }$ denotes the eigenvalues of $J ^ { \Delta }$ , and $\lambda _ { \operatorname* { m a x } } ( J ^ { \Delta } )$ denotes the maximum eigenvalues of $J ^ { \Delta }$ . Moreover, for $t \in \mathbb R$ ,

$$
\mathbb { E } _ { u } \left[ \exp ( t \sqrt { h } u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J { x } ) \right] = \exp ( \frac { 1 } { 2 } t ^ { 2 } h \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J { x } \| ^ { 2 } ) \le \exp ( \frac { 1 } { 2 } t ^ { 2 } h ( r _ { d } + \mathrm { t r } ( J ^ { \Delta } ) ) ) \le \exp ( \frac { 1 } { 2 } t ^ { 2 } \sqrt { h } ( r _ { d } + \mathrm { t r } ( J ^ { \Delta } ) ) ) .
$$

Thus we have

$$
\begin{array} { r l } & { \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] \leq P \left( h \cdot u ^ { T } J ^ { \Delta } u \geq \frac { 1 } { 9 6 } \right) + P \left( \sqrt { h } \cdot | u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x | \geq \frac { 1 } { 9 6 \sqrt { 2 } } \right) } \\ & { \qquad \leq \underset { 0 \leq t \leq \frac { \operatorname* { i n f } _ { 1 } } { 4 h \lambda _ { \operatorname* { m a x } } ( J ^ { \Delta } ) } } { \operatorname* { i n f } } \exp \left( 2 t \sqrt { c _ { 0 } } - \frac { t } { 9 6 } \right) + 2 \underset { t > 0 } { \operatorname* { i n f } } \exp \left( \frac { 1 } { 2 } t ^ { 2 } \sqrt { c _ { 0 } } - \frac { t } { 9 6 \sqrt { 2 } } \right) } \\ & { \qquad \leq \exp \left( \frac { 1 } { 2 } - \frac { 1 } { 3 8 4 \sqrt { c _ { 0 } } } \right) + 2 \exp \left( - \frac { 1 } { 2 \cdot \left( 9 6 \sqrt { 2 } \right) ^ { 2 } \sqrt { c _ { 0 } } } \right) , } \end{array}
$$

and

$$
\begin{array} { r } { \left( \mathbb { E } _ { u } \left[ \exp ( - 4 h \cdot u ^ { T } J ^ { \Delta } u ) \right] \cdot \mathbb { E } _ { u } \left[ \exp ( - 4 \sqrt { 2 h } u ^ { T } ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x ) \right] \right) ^ { \frac { 1 } { 4 } } \leq \exp ( 4 \sqrt { c _ { 0 } } ) . } \end{array}
$$

So when $c _ { 0 }$ is small enough, we have

$\begin{array} { r } { \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] + \sqrt { \mathbb { E } _ { u } \left[ \mathbf { 1 } _ { B ^ { c } } ( u ) \right] } \cdot \left( \mathbb { E } _ { u } \left[ \exp ( - 4 h \cdot u ^ { T } J ^ { \Delta } u ) \right] \cdot \mathbb { E } _ { u } \left[ \exp ( - 4 \sqrt { 2 h } u ^ { T } ( \widetilde { I } ^ { \Delta } ) ^ { \frac { 1 } { 2 } } J x ) \right] \right) ^ { \frac { 1 } { 4 } } \le } \end{array}$ 148 , which leads to the desired result.

# I.7 Proof of Lemma 13

Since

$$
\begin{array} { r l } & { \left. \int _ { K ^ { \varepsilon } \times \mathcal { N } ( 0 , f ) h } ( x , 2 h t ^ { \varepsilon } ) \mathrm { d } y \right. } \\ & { = \mathbb { E } _ { w \sim \mathcal { N } ( 0 , f ) } \Big [ \big ( \| ( Z ^ { \delta } ) ^ { - \frac { 2 } { 2 } } x + \sqrt { 2 \tilde { f } _ { \varepsilon } } u \| \ge R \big ) \Big ] } \\ & { = \mathbb { E } _ { w \sim \mathcal { N } ( 0 , f ) } \Big [ \big ( 1 \big ( \nabla \sqrt { 2 \tilde { h } \omega ^ { \varepsilon } } ( I ^ { \delta } ) ^ { \frac { 1 } { 2 } } \big ) ^ { \frac { 1 } { 2 } } u \ge \frac { 2 \tilde { f } _ { \varepsilon } } { 2 } \big ) \big \| \omega \big ] ^ { 2 } + R ^ { 2 } - \| ( I ^ { \delta } ) ^ { - \frac { 1 } { 2 } } x \| ^ { 2 } \Big ] } \\ & { = \mathbb { E } _ { w \sim \mathcal { N } ( 0 , f ) } \Big [ 1 \Big ( \frac { X ^ { \varepsilon } \big ( T ^ { \delta } \big ) ^ { \frac { 2 } { 2 } } } { \| ( I ^ { \delta } ) ^ { - \frac { 1 } { 2 } } x \| } \Big ) ^ { \frac { 1 } { 2 } } w \ge - \frac { \sqrt { 2 \tilde { h } } } { 2 } \frac { \| u \| ^ { 2 } } { \| ( I ^ { \delta } ) ^ { - \frac { 1 } { 2 } } x \| } + \frac { R ^ { 2 } - \| ( I ^ { \delta } ) ^ { \frac { 2 } { 2 } } x \| ^ { 2 } } { 2 \sqrt { 2 \tilde { h } } \| ( I ^ { \delta } ) ^ { - \frac { 1 } { 2 } } x \| } \Big ) \Big ] } \\ & { \le \exp ( - 4 ) } \\ &  \quad \quad + \mathbb { E } _ { w \sim \mathcal { N } ( 0 , f ) } \Bigg [ 1 \Big ( \frac { X ^ { \varepsilon } \big ( T ^ { \delta } \big ) ^ { \frac { 2 } { 2 } } }  \| ( I ^ { \delta } ) ^ { - \frac { 1 } { 2 } } \end{array}
$$

Then when $h \leq c _ { 0 } \rho _ { 2 } ^ { - 1 } d ^ { - 1 }$ for a small enough $c _ { 0 }$ , by $R \geq 6 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) }$ , we can obtain

$$
\begin{array} { l } { \displaystyle \int _ { K ^ { c } } { \mathcal N } ( x , 2 h I _ { d } ) \mathrm { d } y \leq \exp ( - 4 ) + \mathbb { E } _ { u \sim \mathcal { N } ( 0 , 1 ) } \bigg [ \mathbf { 1 } \Big ( u \geq - \frac { \sqrt { 2 h } } { 2 } \frac { d + 4 \sqrt { d } + 8 } { \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } x \| } + \frac { R ^ { 2 } - \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } x \| ^ { 2 } } { 2 \sqrt { 2 h } \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } x \| } } \\ { \leq \exp ( - 4 ) + \mathbb { E } _ { u \sim \mathcal { N } ( 0 , 1 ) } \bigg [ \mathbf { 1 } \Big ( u \geq - \frac { \sqrt { 2 h \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) } } { 1 2 } \frac { d + 4 \sqrt { d } + 8 } { \sqrt { d } } \Big ) \bigg ] } \\ { \leq \frac { 1 3 } { 2 4 } . } \end{array}
$$

# J Proof Related to Conductance Profile

# J.1 Proof of Lemma 10

Recall s = ε232M2 , and let S be any measurable set of Rd with s ≤ µ∗loc(S) ≤ v ≤ 12 . Define the following subsets:

$$
\begin{array} { r l } & { S _ { 1 } : = \{ x \in S | \mathcal { T } ^ { * } ( x , S ^ { c } ) \leq \frac { \omega } { 2 } \} , } \\ & { S _ { 2 } : = \{ x \in S ^ { c } | \mathcal { T } ^ { * } ( x , S ) \leq \frac { \omega } { 2 } \} , } \\ & { S _ { 3 } : = ( S _ { 1 } \cup S _ { 2 } ) ^ { c } , } \end{array}
$$

Then if $\mu _ { \mathrm { l o c } } ^ { * } ( S _ { 1 } ) \leq \mu _ { \mathrm { l o c } } ^ { * } ( S ) / 2$ or $\mu _ { \mathrm { l o c } } ^ { * } ( S _ { 2 } ) < \mu _ { \mathrm { l o c } } ^ { * } ( S ^ { c } ) / 2$ , by the fact that $\mu _ { \mathrm { l o c } } ^ { \ast }$ is stationary w.r.t the transition kernel $\tau ^ { * }$ , we have

$$
\begin{array} { r l } {  { \int _ { S } \mathcal { T } ^ { * } ( x , S ^ { c } ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x = \int \mathcal { T } ^ { * } ( x , S ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x - \int _ { S } \mathcal { T } ^ { * } ( x , S ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x } } \\ & { = \displaystyle \int _ { S ^ { c } } \mathcal { T } ^ { * } ( x , S ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x \geq \frac { \omega } { 2 } \cdot \operatorname* { m a x } \{ \mu _ { \mathrm { l o c } } ^ { * } ( S \cap S _ { 1 } ^ { c } ) , \mu _ { \mathrm { l o c } } ^ { * } ( S ^ { c } \cap S _ { 2 } ^ { c } ) \} } \\ & { \geq \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) \omega } { 4 } . } \end{array}
$$

Moreover, when µ∗loc(S1) ∧ µ∗loc(S2) ≥ µ∗loc(S)2 , consider $x \in E \cap S _ { 1 }$ and $z \in E \cap S _ { 2 }$ , then $\Vert \mathcal { T } ^ { * } ( x , \cdot ) - \mathcal { T } ^ { * } ( z , \cdot ) \Vert _ { \mathrm { T V } } \geq \mathcal { T } ^ { * } ( z , S ^ { c } ) - \mathcal { T } ^ { * } ( x , S ^ { c } ) \geq 1 - \omega$ , thus $\begin{array} { r } { \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } ( x - z ) \| \ge \frac { \sqrt { 2 h } } { 8 } } \end{array}$ , which implies that $\begin{array} { r } { \operatorname* { i n f } _ { x \in E \cap S _ { 1 } , z \in E \cap S _ { 2 } } \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } ( x - z ) \| \ge \frac { \sqrt { 2 h } } { 8 } } \end{array}$ . We then state the following log-isoperimetric inequality to lower bound $\mu _ { \mathrm { l o c } } ^ { * } ( S _ { 3 } )$ .

$\mathbf { L e m m a 1 4 . } \ S u p p o s e \operatorname* { s u p { e } } _ { \xi \in K } \left| \log \left( \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \right) - \log \left( ( 2 \pi \mathrm { d e t } ( J ^ { - 1 } ) ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } \xi ^ { T } J \xi ) \right) \right| \leq \varepsilon _ { 1 } .$ Consider any measurable partition form $K = S _ { 1 } \cup S _ { 2 } \cup S _ { 3 }$ such that $\begin{array} { r } { \operatorname* { i n f } _ { x \in S _ { 1 } , z \in S _ { 2 } } \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } ( x - z ) \| \ge t } \end{array}$ , we have

$$
\mathrm { \Sigma } _ { ( } S _ { 3 } ) \geq \frac { \sqrt { \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) } } { 2 } t \exp ( - 3 \varepsilon _ { 1 } ) \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 2 } ) \} } \right) .
$$

where $\lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } )$ denotes the minimum eigenvalue of $J ^ { \Delta }$ .

Then take $S _ { 1 }$ as $E \cap S _ { 1 }$ , $S _ { 2 }$ as $E \cap S _ { 2 }$ , and $\begin{array} { r } { t = \frac { \sqrt { 2 h } } { 8 } } \end{array}$ in Lemma 14, we can obtain that

$$
\begin{array} { r l } & { \mu _ { \mathrm { l o c } } ^ { * } ( ( ( E \cap S _ { 1 } ) \cup ( E \cap S _ { 2 } ) ) ^ { c } ) \geq \exp ( - 3 \varepsilon _ { 1 } ) \frac { \sqrt { 2 h \rho _ { 1 } } } { 1 6 } \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 2 } ) \} } \\ & { \qquad \cdot \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 2 } ) \} } \right) . } \end{array}
$$

Without loss of generality, we can assume $\mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) \leq \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 2 } )$ , then by $( ( E \cap S _ { 1 } ) \cup ( E \cap$ $S _ { 2 } ) ) ^ { c } \subseteq E ^ { c } \cup S _ { 3 }$ and $\begin{array} { r } { \mu _ { \mathrm { l o c } } ^ { * } ( E ^ { c } ) \leq \exp ( - 3 \varepsilon _ { 1 } ) \frac { 4 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } = 1 2 8 s h \rho _ { 1 } \exp ( - 3 \varepsilon _ { 1 } ) } \end{array}$ , when $c _ { 0 }$ is small enough, we can obtain

$$
\begin{array} { r l } & { \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 3 } ) + 1 2 8 s h \rho _ { 1 } \exp ( - 3 \varepsilon _ { 1 } ) } \\ & { \geq \exp ( - 3 \varepsilon _ { 1 } ) \frac { \sqrt { 2 h \rho _ { 1 } } } { 1 6 } \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { \mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) } \Big ) } \\ & { \overset { \mathrm { ( i ) } } { \geq } \exp ( - 3 \varepsilon _ { 1 } ) \frac { \sqrt { 2 h \rho _ { 1 } } } { 1 6 } ( \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { 4 } + \frac { s } { 4 } - 1 2 8 s h \rho _ { 1 } ) \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { 4 } + \frac { s } { 4 } - 1 2 8 s h \rho _ { 1 } } \Big ) } \\ & { \geq \exp ( - 3 \varepsilon _ { 1 } ) \frac { \sqrt { 2 h \rho _ { 1 } } } { 1 6 } \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { 4 } \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } \Big ) , } \end{array}
$$

where (i) uses $\mu _ { \mathrm { l o c } } ^ { * } ( E \cap S _ { 1 } ) \geq \pi _ { \mathrm { l o c } } ( S _ { 1 } ) - \mu _ { \mathrm { l o c } } ^ { * } ( E ^ { c } )$ , $\pi _ { \mathrm { l o c } } ( S _ { 1 } ) \geq { \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { 2 } } \geq { \frac { s } { 2 } }$ and the function $x \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { x } )$ is an increasing function. Then when $h \leq c _ { 0 } \rho _ { 1 } ^ { - 1 }$ with small enough $c _ { 0 }$ , we have

$$
\mu _ { \mathrm { l o c } } ^ { * } ( S _ { 3 } ) \geq \exp ( - 3 \varepsilon _ { 1 } ) \frac { \sqrt { h \rho _ { 1 } } \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { 6 4 } \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } \Big ) .
$$

hence

$$
\begin{array} { r l } { \displaystyle \int _ { S } \mathcal { T } ^ { * } ( x , S ^ { c } ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x \geq \frac { 1 } { 2 } \left( \displaystyle \int _ { S } \mathcal { T } ^ { * } ( x , S ^ { c } ) \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x + \displaystyle \int _ { S ^ { c } } \mathcal { T } ^ { * } \mu _ { \mathrm { l o c } } ^ { * } ( x ) \mathrm { d } x \right) } & { } \\ { \displaystyle \geq \frac { \omega } { 4 } \mu _ { \mathrm { l o c } } ^ { * } ( S _ { 3 } ) \geq \frac { \omega } { 2 5 6 } \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { \rho _ { 1 } h } \mu _ { \mathrm { l o c } } ^ { * } ( S ) \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } \Big ) , } & { } \end{array}
$$

which leads to

$$
\frac { r ^ { \ast } ( x , S ^ { c } ) \mu _ { \mathrm { l o c } } ^ { \ast } ( x ) } { \mu _ { \mathrm { l o c } } ^ { \ast } ( S ) } \mathrm { d } x \geq \frac { \omega } { 2 5 6 } \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { \rho _ { 1 } h } \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 4 } { \mu _ { \mathrm { l o c } } ^ { \ast } ( S ) } \right) \geq \frac { \omega } { 4 } \exp ( - 3 \varepsilon _ { 1 } ) \sqrt { \rho _ { 1 } h } \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 4 } { \mu _ { \mathrm { l o c } } ^ { \ast } ( S ) } \right) .
$$

Then combining with the result for the first case, we can obtain a lower bound of

$$
\frac { \omega } { 4 } \operatorname* { m i n } \big \{ 1 , \frac { \exp ( - 3 \varepsilon _ { 1 } ) } { 6 4 } \sqrt { \rho _ { 1 } h \log \big ( 1 + \frac { 1 } { v } \big ) } \big \}
$$

on $s$ -conductance profile $\Phi _ { s } ( v )$ with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 3 2 M _ { 0 } ^ { 2 } } } \end{array}$ .

# J.2 Proof of Lemma 14

To begin with, we consider the following lemma stated in [22].

Lemma 15. (Lemma 16 of [22]) Let $\gamma$ denote the density of the standard Gaussian distribution $\mathcal { N } \left( 0 , \sigma ^ { 2 } I _ { d } \right)$ , and let $\mu ^ { * }$ be a distribution with density $\mu ^ { * } = q \cdot \gamma$ , where $q$ is a log-concave function. Then for any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $\mathbb { R } ^ { d }$ , we have

$$
\mu ^ { \ast } \left( S _ { 3 } \right) \geq \frac { d \left( S _ { 1 } , S _ { 2 } \right) } { 2 \sigma } \operatorname* { m i n } \left\{ \mu ^ { \ast } \left( S _ { 1 } \right) , \mu ^ { \ast } \left( S _ { 2 } \right) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \mu ^ { \ast } \left( S _ { 1 } \right) , \mu ^ { \ast } \left( S _ { 2 } \right) \right\} } \right) .
$$

We first consider the case $J = I _ { d }$ . Define $\overline { { \mu } } = N ( 0 , I _ { d } )$ and $\overline { { \mu } } | _ { K } = N ( 0 , I _ { d } ) | _ { K }$ , by the fact that $K$ is a convex set and $\mathbf { 1 } _ { K }$ is a log-concave function, using lemma 15, we can obtain that for any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $K$ , we have

$$
\overline { { \mu } } | _ { K } \left( S _ { 3 } \right) \geq \frac { d \left( S _ { 1 } , S _ { 2 } \right) } { 2 } \operatorname* { m i n } \left\{ \overline { { \mu } } | _ { K } \left( S _ { 1 } \right) , \overline { { \mu } } | _ { K } \left( S _ { 2 } \right) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \overline { { \mu } } | _ { K } \left( S _ { 1 } \right) , \overline { { \mu } } | _ { K } \left( S _ { 2 } \right) \right\} } \right) .
$$

$$
\begin{array} { l l } { \displaystyle \operatorname* { s u p } _ { \xi \in K } \big \vert \log \big ( \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \big ) - \log \big ( ( 2 \pi \operatorname* { d e t } ( J ^ { - 1 } ) ) ^ { - \frac { d } { 2 } } \exp ( - \frac { 1 } { 2 } \xi ^ { T } J \xi ) \big ) \big \vert = \varepsilon _ { 1 } , \mathrm { ~ w e ~ h a v e ~ } } \\ { \displaystyle 1 \geq \int _ { K } \overline { { \mu } } ( \xi ) \mathrm { d } \xi = \int _ { K } \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \mathrm { d } \xi \cdot \frac { \int _ { K } \overline { { \mu } } ( \xi ) \mathrm { d } \xi } { \int _ { K } \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \mathrm { d } \xi } \stackrel { ( i ) } { \geq } \operatorname* { m i n } _ { \xi \in K } \frac { \overline { { \mu } } ( \xi ) } { \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) } \geq \exp ( - \varepsilon _ { 1 } ) , } \end{array}
$$

where $( i )$ uses $\begin{array} { r } { \int _ { K } \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \mathrm { d } \xi = 1 } \end{array}$ . Furthermore, we can obtain that for any measurable set $S \subseteq K$ ,

$$
\exp ( - 2 \varepsilon _ { 1 } ) \le \frac { \mu _ { \mathrm { l o c } } ^ { * } ( S ) } { \overline { { \mu } } | _ { K } ( S ) } = \frac { \int _ { S } \mu _ { \mathrm { l o c } } ^ { * } ( \xi ) \mathrm { d } \xi \int _ { K } \overline { { \mu } } ( \xi ) \mathrm { d } \xi } { \int _ { S } \overline { { \mu } } ( \xi ) \mathrm { d } \xi } \le \exp ( \varepsilon _ { 1 } ) .
$$

Thus

$$
\begin{array} { r l } & { \mathsf { \Pi } _ { \mathsf { l o c } } ^ { \ast } ( S _ { 3 } ) \geq \exp ( - 2 \varepsilon _ { 1 } ) \overline { { \mu } } | _ { K } ( S _ { 3 } ) } \\ & { \geq \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 2 \varepsilon _ { 1 } ) \operatorname* { m i n } \{ \overline { { \mu } } | _ { K } ( S _ { 1 } ) , \overline { { \mu } } | _ { K } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \overline { { \mu } } | _ { K } ( S _ { 1 } ) , \overline { { \mu } } | _ { K } ( S _ { 2 } ) \} } ) } \\ & { \overset { ( i ) } { \geq } \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 3 \varepsilon _ { 1 } ) \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { \exp ( - \varepsilon _ { 1 } ) \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 2 } ) \} } ) } \\ &  \geq \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 3 \varepsilon _ { 1 } ) \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 1 } ) , \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 }  \operatorname* { m i n } \{ \mu _ { \mathrm { l o c } } ^ { \ast } ( S _ { 1 } ) , \mu _  \mathrm { l o c } \end{array}
$$

where $( i )$ uses the fact that $x \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { x } )$ is an increasing function. For the general case where $J$ is not necessary an identity matrix, we can define $K ^ { \prime } = J ^ { \frac { 1 } { 2 } } K = \{ x = J ^ { \frac { 1 } { 2 } } y \ : \ y \in K \}$ , and $\lambda = J ^ { \frac { 1 } { 2 } } \xi$ , where $\xi$ is a random variable with density $\mu _ { \mathrm { l o c } } ^ { * }$ . Thus $\lambda$ has a density

$$
\widetilde { \mu } ^ { * } ( \lambda ) = \mu _ { \mathrm { l o c } } ^ { * } ( J ^ { - \frac { 1 } { 2 } } \lambda ) ( \operatorname* { d e t } ( J ) ) ^ { \frac { d } { 2 } } .
$$

Then for any $\lambda \in K ^ { \prime }$ , it holds that

$$
\Big | \log ( \widetilde { \mu } ^ { * } ( \lambda ) ) - \log \big ( ( 2 \pi ) ^ { - \frac { d } { 2 } } \exp ( - \frac 1 2 \lambda ^ { T } \lambda ) \big ) \Big | \leq \varepsilon _ { 1 } .
$$

Consider any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $K$ , let

$$
\begin{array} { c } { { \widetilde { S _ { 1 } } = J ^ { \frac { 1 } { 2 } } S _ { 1 } ; } } \\ { { \widetilde { S _ { 2 } } = J ^ { \frac { 1 } { 2 } } S _ { 2 } ; } } \\ { { \widetilde { S _ { 3 } } = J ^ { \frac { 1 } { 2 } } S _ { 3 } . } } \end{array}
$$

Then for any point $x \in S _ { 1 }$ and $y \in S _ { 2 }$ , we have

$$
\begin{array} { r l } & { \| J ^ { \frac { 1 } { 2 } } x - J ^ { \frac { 1 } { 2 } } y \| ^ { 2 } = ( x - y ) ^ { T } ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } J ^ { \Delta } ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - y ) } \\ & { \qquad \geq \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) \| ( I ^ { \Delta } ) ^ { - \frac { 1 } { 2 } } ( x - y ) \| ^ { 2 } } \end{array}
$$

So by applying $\widetilde { \mu } ^ { * }$ to statement (58), we can obtain

$$
\begin{array} { l l } { \displaystyle _ { \mathrm { l o c } } ^ { * } ( S _ { 3 } ) = \widetilde { \mu } ^ { * } ( \widetilde { S } _ { 3 } ) \geq \frac { d ( \widetilde { S } _ { 1 } , \widetilde { S } _ { 2 } ) } { 2 } \exp ( - 3 \varepsilon _ { 1 } ) \operatorname* { m i n } \left\{ \widetilde { \mu } ^ { * } ( \widetilde { S } _ { 1 } ) , \widetilde { \mu } ^ { * } ( \widetilde { S } _ { 2 } ) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \widetilde { \mu } ^ { * } ( \widetilde { S } _ { 1 } ) , \widetilde { \mu } ^ { * } ( \widetilde { S } _ { 2 } ) \right\} } \right) } \\ { \geq \frac { \sqrt { \lambda _ { \operatorname* { m i n } } ( J ^ { \Delta } ) } } { 2 } t \exp ( - 3 \varepsilon _ { 1 } ) \operatorname* { m i n } \left\{ \mu _ { \mathrm { l o c } } ^ { * } \left( S _ { 1 } \right) , \mu _ { \mathrm { l o c } } ^ { * } \left( S _ { 2 } \right) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \mu _ { \mathrm { l o c } } ^ { * } \left( S _ { 1 } \right) , \mu _ { \mathrm { l o c } } ^ { * } \left( S _ { 2 } \right) \right\} } \right) , } \end{array}
$$

where the last inequality uses $\begin{array} { r } { \operatorname* { i n f } _ { x \in S _ { 1 } , z \in S _ { 2 } } \| ( I ^ { \Delta } ) ^ { \frac { 1 } { 2 } } ( x - z ) \| \ge t } \end{array}$ . Proof is completed.