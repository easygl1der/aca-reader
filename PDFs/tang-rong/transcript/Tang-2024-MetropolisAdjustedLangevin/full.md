# On the Computational Complexity of Metropolis-Adjusted Langevin Algorithms for Bayesian Posterior Sampling

Rong Tang∗ and Yun Yang†

∗Department of Mathematics, The Hong Kong University of Science and Technology †Department of Statistics, University of Illinois Urbana-Champaign

# Abstract

In this paper, we examine the computational complexity of sampling from a Bayesian posterior (or pseudo-posterior) using the Metropolis-adjusted Langevin algorithm (MALA). MALA first employs a discrete-time Langevin SDE to propose a new state, and then adjusts the proposed state using Metropolis-Hastings rejection. Most existing theoretical analyses of MALA rely on the smoothness and strong log-concavity properties of the target distribution, which are often lacking in practical Bayesian problems. Our analysis hinges on statistical large sample theory, which constrains the deviation of the Bayesian posterior from being smooth and log-concave in a very specific way. In particular, we introduce a new technique for bounding the mixing time of a Markov chain with a continuous state space via the $s$ -conductance profile, offering improvements over existing techniques in several aspects. By employing this new technique, we establish the optimal parameter dimension dependence of $d ^ { 1 / 3 }$ and condition number dependence of $\kappa$ in the non-asymptotic mixing time upper bound for MALA after the burn-in period, under a standard Bayesian setting where the target posterior distribution is close to a $d$ -dimensional Gaussian distribution with a covariance matrix having a condition number $\kappa$ . We also prove a matching mixing time lower bound for sampling from a multivariate Gaussian via MALA to complement the upper bound.

Keywords— Bayesian inference, Gibbs posterior, Large sample theory, Log-isoperimetric inequality, Metropolis-adjusted Langevin algorithms, Mixing time.

# 1 Introduction

Bayesian inference gains significant popularity during the last two decades due to the advance in modern computing power. As a method of statistical analysis based on probabilistic modelling, Bayesian inference allows natural uncertainty quantification on the unknown parameters via a posterior distribution. In the classical Bayesian framework, the data $X ^ { ( n ) } = \{ X _ { 1 } , \ldots , { \bar { X } } _ { n } \}$ is assumed to consist of i.i.d. samples generated from a probability distribution $p ( X \mid \theta )$ depending on an unknown parameter $\theta$ in parameter space $\Theta \subset \mathbb { R } ^ { d }$ . Domain knowledge and prior beliefs can be characterized by a probability distribution $\pi ( \theta )$ over $\Theta$ called prior (distribution), which is then updated into a posterior (distribution) $p ( \theta | X ^ { ( n ) } )$

by multiplying with the likelihood function

$$
\mathcal { L } _ { n } ( \theta ; X ^ { ( n ) } ) : = \prod _ { i = 1 } ^ { n } p ( X _ { i } \mid \theta )
$$

evaluated on the observed data $X ^ { ( n ) }$ using the Bayes theorem. The classical Bayesian framework relies on the likelihood formulation, which hinders its use in problems where the data generating model is hard to fully specify or is not our primary interest. The pseudo-posterior [Alquier et al., 2016, Ghosh et al., 2020] idea provides a more general probabilistic inference framework to alleviate this restriction by replacing the negative log-likelihood function in the Bayesian posterior with a criterion function. For example, when applied to risk minimization problems, the so-called Gibbs posteriors [Bhattacharya and Martin, 2020, Syring and Martin, 2020] use the (scaled) empirical risk function as the criterion function, thus avoiding imposing restrictive assumptions on the statistical model through a fully specified likelihood function.

Despite the conceptual appeal of Bayesian inference, its practical implementation is a notoriously difficult computational problem. For example, the posterior $p ( \theta | X ^ { ( n ) } )$ involves a normalisation constant that can be expressed as a multidimensional integral

$$
\int _ { \Theta } \mathcal { L } _ { n } ( \theta ; X ^ { ( n ) } ) \pi ( \theta ) \mathrm { d } \theta .
$$

This integral is usually analytically intractable and hard to numerically approximate, especially when the parameter dimension $d$ is high. Different from those numerical methods for directly computing the normalisation constant, the Markov chain Monte Carlo (MCMC) algorithm [Hastings, 1970, Geman and Geman, 1984, Robert et al., 2004] constructs a Markov chain, whose simulation only requires evaluations of the likelihood ratio under a pair of parameters, such that its stationary distribution matches the target posterior distribution. Thus, MCMC provides an appealing alternative for Bayesian computation by turning the integration problem into a sampling problem that does not require computing the normalisation constant. Despite its popularity, the theoretical analysis of the computational efficiency of MCMC algorithms is mostly carried out for smooth and log-concave target distributions, and is comparatively rare in the Bayesian literature where a (pseudo-)posterior can be non-smooth and non-log-concave. In addition, precise characterizations of the computational complexity (or mixing time) and its dependence on the parameter dimension $d$ for commonly used MCMC algorithms are important for guiding their practical designs and use.

A widely used MCMC algorithm for sampling from Bayesian posteriors is the Gibbs sampler, which generates samples from a multivariate distribution by iteratively sampling each variable from its conditional distribution, given all other variables. The Gibbs sampler is particularly efficient for Bayesian models with closed-form conditional distributions under conjugate priors. A recent theoretical study by Ascolani and Zanella [2023] provides a dimension-free mixing time bound for the Gibbs sampler when applied to certain high-dimensional Bayesian hierarchical models. However, it is important to note that each iteration of their algorithm involves the sequential sampling of each dimension of the parameter from its corresponding full conditional distribution. This means that the total number of sampling steps required for the Gibbs sampler to converge is at least linear in the parameter dimension, which is larger than our sub-linear $d ^ { 1 / 3 }$ scaling of the needed sampling steps for MALA. On the other hand, the per-step cost of MALA can be linear in $d$ because of gradient computation, while that of Gibbs sampling can be much lower, especially under weak dependence (although in the worst case, computing each conditional distribution may also require $O ( d )$ complexity). On a separate note, we would like to mention that although MALA has a per-iteration cost linear in $d$ to compute the gradient, the computation across different dimensions can be parallelized. In contrast, Gibbs sampling must sequentially scan over all its components and cannot be made parallel in order to maintain the detailed balance property. Additionally, the high efficiency of the Gibbs sampler often relies on the use of conjugate priors that facilitate closed-form conditional distributions. However, for complex Bayesian models, such a conjugate prior may not exist, as is the case in Bayesian quantile regression, discussed in $\mathrm { Y u }$ and Moyeed [2001], or linear regression with heavy-tailed noise (like Student’s t-distributions). Moreover, there are situations where people tend to use specific non-conjugate priors for particular reasons. For example, sparsity-induced priors such as the spike and slab priors (with heavy-tailed slabs) are widely used in regression analysis for facilitating variable selection. In these complicated scenarios, one might have to resort to using MALA or, more broadly, the Metropolis-Hastings (MH) algorithm, to draw samples from the Bayesian posterior.

On the other hand, the Metropolis-Hastings (MH) algorithm provides a more flexible alternative. An MH algorithm produces samples by proposing and then accepting or rejecting these proposals based on a specified acceptance criterion. A key advantage of the MH algorithm is its ability to handle Bayesian (pseudo-)posterior distributions without requiring explicit knowledge of the normalization constant or the full conditional distributions. One of the most popular MH algorithms is the Metropolis random walk (MRW), a zeroth-order method that queries the value of the target density ratio under two points per iteration. Dwivedi et al. [2019] shows that for a log-concave and smooth target density, the $\varepsilon$ -mixing time in total variation distance (the number of iterations required to converge to an $\varepsilon$ -neighborhood of stationary distribution in the total variation distance) for MRW is at most ${ \mathcal { O } } { \left( d \log ( 1 / \varepsilon ) \right) }$ . On the other hand, the $\mathcal O ( d )$ scaling limit of Gelman et al. [1997] suggests that their linear dependence on dimension $d$ is optimal. For a class of Bayesian pseudo-posteriors that can be non-smooth and non-log-concave, it has been shown in Belloni and Chernozhukov [2009] that as the sample size $n$ grows to infinity while the parameter dimension $d$ does not grow too quickly relative to $n$ so that the pseudo-posterior satisfies a Bernstein-von Mises (asymptotic normality) result, then MRW for sampling from the target pseudoposterior constrained on an approximate compact set with a warm start has an asymptotic total variation $\varepsilon$ -mixing time upper bound as $\mathcal { O } _ { p } \big ( d ^ { 2 } \log ( 1 / \varepsilon ) \big )$ .

Another prominent class of MH algorithms is the Metropolis-adjusted Langevin algorithm (MALA), which utilizes additional gradient information about the target density. Although this approach requires computing the gradient and can be costlier than zeroth-order methods that only use function evaluations, the development of automatic differentiation tools [Paszke et al., 2017, Margossian, 2019] has simplified this task for many explicit and smooth densities. These tools make the computational demands for gradient computation comparable to those for evaluating the density itself. Furthermore, it has been demonstrated that MALA tends to have a lower mixing time in comparison to the MRW. For example, Chewi et al. [2021] show that if the negative log-density (will be referred to as potential) of the target distribution is twice continuously differentiable and strongly convex, then the $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence for MALA with a warm start scales as $\Theta \big ( d ^ { 1 / 2 } \big )$ modulo polylogarithmic factors in $\varepsilon$ . Additionally, Roberts and Rosenthal [1998] and Chewi et al. [2021] show that the optimal dimension dependence for MALA is $d ^ { 1 / 3 }$ for some product measures satisfying stringent conditions like the standard Gaussian. However, for Bayesian (pseudo-)posteriors, it is common that the smoothness and strong convexity properties of the log-density assumed in literature are not satisfied. For instance, consider Bayesian quantile regression with a quantile level $\tau$ . Given a dataset $X ^ { ( n ) } = \{ X _ { i } = ( \widetilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ consisting of covariates and response variables, the posterior distribution then takes the form of $\begin{array} { r } { \pi _ { n } ( \widehat { \theta } | X ^ { ( n ) } ) \propto \exp \big ( - \sum _ { i = 1 } ^ { n } ( Y _ { i } - \widetilde { X } _ { i } ^ { T } \theta ) ( \tau - \mathbf { 1 } ( Y _ { i } < \widetilde { X } _ { i } ^ { T } \theta ) ) \big ) \pi ( \theta ) . } \end{array}$ , where $\mathbf { 1 } ( \cdot )$ denotes the indicator function. An important feature of this example is that the resulting Bayesian posterior is neither differentiable owing to the discontinuity introduced by the indicator function, nor strongly log-concave. For such non-differentiable densities, we slightly extend the MALA by using any subgradient to replace the gradient in its algorithm formulation. Theoretically, it is natural to investigate:

What is the optimal dimension (and condition number) dependence when using MALA to sample from a possibly non-smooth and non-log-concave (pseudo-)posterior density, in light of the asymptotic Gaussian nature of the posterior as predicted by statistical large sample theory?

Moreover, it would be insightful to determine to what extent we can diverge from a Gaussian distribution while preserving the dimension dependence as sampling from a Gaussian distribution, and how various factors, such as the dimensionality, sample size and density smoothness, affect the deviance of the

posterior from the Gaussian distribution.

Our contributions. In this work, we show an upper bound on the $\varepsilon$ -mixing time of MALA for sampling from a class of possibly non-smooth and non-log-concave distributions with non-product forms (c.f. Condition A for a precise definition) with an $M _ { 0 }$ -warm start (defined in Section 2.3) as $\mathcal { O } \big ( \operatorname* { m a x } \big \{ d ^ { 1 / 3 } \log ( \varepsilon ^ { - 1 } \log M _ { 0 } ) , \log M _ { 0 } \big \} \big )$ , which matches (up to logarithmic terms in $( M _ { 0 } , \varepsilon ) )$ the lower bound result proved in Chewi et al. [2021] that the mixing time of MALA for the standard Gaussian is at least $\mathcal { O } ( d ^ { \bar { 1 } / 3 } )$ . Specially, our condition requires the target distribution (after proper rescaling by the sample size $n$ ) to be close to a multivariate Gaussian subject to small perturbations. We verify that a wide class of Gibbs posteriors [Bhattacharya and Martin, 2020, Syring and Martin, 2020], including conventional Bayesian posteriors defined through likelihood functions, meets our condition under a minimal set of assumptions. In particular, our theory provides an explicit upper bound condition on the growth of parameter dimension $d$ relative to sample size $n$ , stated in a non-asymptotic manner, that is, d ≤ c nκ1log n , where $\kappa _ { 1 }$ depends on the regularity of the density function (c.f. Theorem 2). Specifically, for less smooth density functions, a smaller dimension $d$ is necessary to maintain the $d ^ { 1 / 3 }$ scaling of the mixing time guarantee, which is also supported by our numerical results in Section 7.

In addition, our result illustrates that the mixing time of MALA exhibits a linear dependence on the condition number $\kappa$ of the covariance matrix (which may have a polynomial dependence on the dimension in some ill-conditioned cases) of the approximating multivariate Gaussian. Our bound matches the mixing time scaling of Gaussian targets with condition number $\kappa$ , and is therefore optimal. For the sake of completeness, we derive a matching lower bound in Appendix A.3. In our lower bound analysis, we extend the proof of Theorem 1 in Chewi et al. [2021], which primarily focuses on a standard Gaussian target distribution. In addition, we also carefully keep track of the dependence on the condition number in our derivation, which allows us to establish a lower bound that explicitly demonstrates a linear dependence on the condition number and also matches with our upper bound.

It is worthwhile mentioning that our Condition A does not require the distance between the target posterior and the multivariate Gaussian distribution to vanish as $n$ tends to infinity; while in the context of Bayesian posteriors, these distances indeed decay to zero under minimal assumptions on the statistical model. Therefore, our mixing time result is more generally applicable to problems beyond Bayesian posterior sampling, for example, to optimization of approximately convex functions via simulated annealing [Belloni et al., 2015], where the target distribution can deviate from being smooth and strongly log-concave by a finite amount. In such settings, the computational complexity of sampling algorithms scales as $\mathcal { O } ( d ^ { 1 / 3 } )$ with the variable dimension $d$ under reasonably good initialization while that of a wide class of gradient-based optimization algorithms may scale exponentially [Ma et al., 2019].

Our result on the $\mathcal { O } ( d ^ { 1 / 3 } )$ dimension dependence for the mixing time of MALA after the burn-in period for the perturbed Gaussian class strengthens our understanding of sampling from non-smooth and non-log-concave distributions. It also partly fills the gap between the optimal $d ^ { 1 / 3 }$ mixing time for a class of sufficiently regular product distributions derived from the scaling limit approach in Roberts and Rosenthal [1998] and the $d ^ { 1 / 2 }$ lower bound on the class of all log-smooth and strongly log-concave distributions obtained in Chewi et al. [2021], by identifying a much larger class of distributions of practical interest that attain the optimal $d ^ { 1 / 3 }$ dimension dependence. Moreover, we introduce a somewhat more general average conductance argument based on the $s$ -conductance profile in Section 3 to improve the warming parameter dependence without deteriorating the dimension dependence. More specifically, our mixing time upper bound improves upon existing results [e.g. Chewi et al., 2021] in the dependence on the warming parameter $M _ { 0 }$ from logarithmic to doubly logarithmic (the $\log \log ( M _ { 0 } )$ term in Theorem 1) when $\log M _ { 0 } \leq d ^ { \frac { 1 } { 3 } }$ , by adapting the $s$ -conductance profile and the log-isoperimetric inequality device [Chen et al., 2020], or more generally, the log-Sobolev inequality device [Lovasz and Kannan ´ , 1999, Kannan et al., 2006], to our target distribution class. Our constraint of $d ^ { \frac { 1 } { 3 } }$ on $\log M _ { 0 }$ can be overly strong for general target distributions in practice. For instance, in the case of distributions possessing product forms, such as a pair of isotropic Gaussians with varying means, $\log M _ { 0 }$ tends to increase linearly with the dimension $d$ . However, for Bayesian posterior with smooth density, we may leverage its asymptotic distribution to construct more effective warm starts (c.f. Lemma 2 and Corollary 1). In addition, we study a variant of MALA where the (sub-)gradient vector in the Langevin SDE is preconditioned by a matrix for capturing the local geometry, for example, the Fisher information matrix in the context of Bayesian posterior sampling, and we illustrate in our Corollaries 1 and 2 that MALA with suitable preconditioning may improve the convergence of the sampling algorithm even though the target density is non-differentiable.

Our analysis is motivated by the statistical large sample theory suggesting the Bayesian posterior to be close to a multivariate Gaussian. We develop mixing time bounds of MALA for sampling from general Gibbs posteriors (possibly with increasing parameter dimension and non-smooth criterion function) by establishing non-asymptotic Bernstein-von Mises results, applying techniques from empirical process theory, including chaining, peeling, and localization. Due to the delicate analysis in our mixing time upper bound proof that utilizes the explicit form of Gaussian distributions for bounding the acceptance probability in each step of MALA, we obtain a better dimension dependence of $d ^ { 1 / 3 }$ than the $d ^ { 1 / 2 }$ dependence derived for general smooth and log-concave densities. In addition, by utilizing our $s$ - conductance profile technique, we can obtain a mixing time upper bound for sampling from the original Bayesian posterior instead of a truncated version considered in Belloni and Chernozhukov [2009].

Organization. The rest of the paper is organized as follows. In Section 2, we describe the background and formally formulate the theoretical problem of analyzing the computational complexity of MALA for Bayesian posterior sampling that is addressed in this work. In Section 3, we briefly review some common concepts and existing techniques for analyzing the computational complexity (in terms of mixing time) of a Markov chain, and introduce our improved technique based on $s$ -conductance profile. In Section 4, we apply the generic technique developed in Section 3 to analyze MALA for Bayesian posterior sampling. In Section 5, we specialize the general mixing bound of MALA to the class of Gibbs posteriors, and apply it to both Gibbs posteriors with smooth and non-smooth loss functions. Section 6 sketches the main ideas in proving the MALA mixing time bound and discuss some main differences with existing proofs. Some numerical studies are provided in Section 7, where we empirically compare the convergence of MALA and MRW. All proofs and technical details are deferred to the appendices in the supplementary material.

Notation. For two real numbers, we use $a \wedge b$ and $a \vee b$ to denote the maximum and minimum between $a$ and $b$ . For two distributions $p$ and $q$ , we use $\begin{array} { r } { \| p - q \| _ { \mathrm { T V } } = \frac { 1 } { 2 } \int | p ( x ) - q ( x ) | \mathrm { d } x } \end{array}$ to denote their the total variation distance and $\chi ^ { 2 } ( p , q )$ to denote their $\chi ^ { 2 }$ divergence. We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and suppress the subscript when $p = 2$ . We use $\mathbf { 0 } _ { d }$ to denote the $d$ -dimensional all zero vector, and $B _ { r } ( x )$ to denote the closed ball centered at $x$ with radius $r$ (under the $\ell _ { 2 }$ distance) in the Euclidean space; in particular, we use $B _ { r } ^ { d }$ to denote $B _ { r } ( \mathbf { 0 } _ { d } )$ when no ambiguity may arise. We use $\mathbb { S } ^ { d } = \left\{ x \in \mathbb { R } ^ { d + 1 } : \left. x \right. = 1 \right\}$ to denote the $d$ -dimensional sphere. We use $N _ { d } ( \mu , \Sigma )$ to denote the $d$ -dimensional multivariate Gaussian distribution with mean vector $\mu \in \mathbb { R } ^ { d }$ and covariance matrix $\Sigma \in \mathbb { R } ^ { d \times d }$ , and d suppress the subscript when $d = 1$ . We use ${ \mathcal { P } } ( K )$ to denote the set of probability measures on a set $K$ . For a function $f : \mathbb { R } ^ { d }  \mathbb { R }$ , we use $\nabla f ( x )$ to denote the $d$ -dimensional gradient vector of $f$ at $x$ and $\operatorname { H e s s } ( f ( x ) )$ to denote the Hessian matrix of $f$ at $x$ . For a matrix $J$ , we use $\| J \| _ { \mathrm { o p } }$ and $\Vert J \Vert _ { \mathrm { F } }$ to denote its operator norm and Frobenius norm respectively, and use $\lambda _ { \operatorname* { m a x } } ( J )$ and $\lambda _ { \operatorname* { m i n } } ( J )$ to denote the maximal and minimal eigenvalues of $J$ . Throughout, $C , c , C _ { 0 } , c _ { 0 } , c _ { 1 } , c _ { 1 } , .$ . . are generically used to denote positive constants independent of $n , d$ whose values might change from one line to another.

# 2 Background and Problem Setup

We first review the Bayesian (pseudo-)posterior framework and the Metropolis-adjusted Langevin algorithm (MALA). After that, we discuss an extension of MALA to handle the case where the target density is non-smooth by using the subgradient to replace the gradient and formulate the theoretical problem to be addressed in this work.

# 2.1 Bayesian pseudo-posterior

A standard Bayesian model consists of a prior distribution (density) $\pi ( \theta )$ over parameter space $\Theta \subset \mathbb { R } ^ { d }$ as the marginal distribution of the parameter $\theta$ and a sampling distribution (density) $p ( X \mid \theta )$ as the conditional distribution of the observation random variable $X$ given $\theta$ . After obtaining a collection of $n$ observations $X ^ { ( n ) } = \{ X _ { 1 } , X _ { 2 } , \cdot \cdot \cdot , X _ { n } \}$ modelled as $n$ independent copies of $X$ given $\theta$ , we update our beliefs about $\theta$ from the prior by calculating the posterior distribution (density)

$$
p ( \theta | X ^ { ( n ) } ) = \frac { \exp \left\{ \log \pi ( \theta ) + \log \mathcal { L } _ { n } ( \theta ; X ^ { ( n ) } ) \right\} } { \int _ { \Theta } \exp \left\{ \log \pi ( \theta ) + \log \mathcal { L } _ { n } ( \theta ; X ^ { ( n ) } ) \right\} \mathrm { d } \theta } , \quad \theta \in \Theta ,
$$

where recall that $\begin{array} { r } { \mathcal { L } _ { n } ( \boldsymbol { \theta } ; X ^ { ( n ) } ) = \prod _ { i = 1 } ^ { n } p ( X _ { i } | \boldsymbol { \theta } ) } \end{array}$ is the likelihood function. Despite the Bayesian formulation, in our theoretical analysis, we will adopt the frequentist perspective by assuming the data $X ^ { ( n ) }$ to be i.i.d. samples from an unknown data generating distribution ${ \mathcal { P } } ^ { * } : = p ( X | \theta ^ { * } )$ , where $\theta ^ { * }$ will be referred to as the true parameter, or simply truth, throughout the rest of the paper.

In many real situations, practitioners may not be interested in learning the entire data generating distribution ${ \mathcal { P } } ^ { * }$ , but want to draw inference on some characteristic as a functional $\theta = \theta ( \mathcal { P } ^ { * } )$ of ${ \mathcal { P } } ^ { * }$ , which alone does not fully specify ${ \mathcal { P } } ^ { * }$ . An illustrative example is the quantile regression where the goal is to learn the conditional quantile of the response given the covariates; however, the conventional Bayesian framework requires a full specification of the condition distribution by imposing extra restrictive assumptions on the model, which may lead to model misspecification and sacrifice estimation robustness. A natural idea to alleviate the limitation of requiring a well-specified likelihood function is to replace the log-likelihood function $\log { \mathcal { L } _ { n } ( \theta ; X ^ { ( n ) } ) }$ in the usual Bayesian posterior (1) by a criterion function ${ \mathcal { C } } _ { n } ( \theta ; X ^ { ( n ) } )$ . The resulting distribution,

$$
\pi _ { n } ( \theta | X ^ { ( n ) } ) = \frac { \exp \left\{ \log \pi ( \theta ) + \mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } ) \right\} } { \int _ { \Theta } \exp \left\{ \log \pi ( \theta ) + \mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } ) \right\} \mathrm { d } \theta } , \quad \theta \in \Theta ,
$$

is called the Bayesian pseudo-posterior with criterion function $\mathcal { C } _ { n } : \Theta \times \mathcal { X } ^ { n } \to \mathbb { R }$ , and we may use the shorthand $\pi _ { n } ( \cdot )$ to denote the pseudo-posterior $\pi _ { n } ( \cdot | X ^ { ( n ) } )$ when no ambiguity may arise. A popular choice of a criterion function is $\mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } ) = - \alpha n \mathcal { R } _ { n } ( \theta )$ , where

$$
{ \mathcal { R } } _ { n } ( \theta ) : = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta )
$$

is the empirical risk function induced from a loss function $\ell : \mathcal { X } \times \Theta  \mathbb { R }$ , and $\alpha \in ( 0 , \infty )$ is the learning rate parameter. The corresponding Bayesian pseudo-posterior is called the Gibbs posterior associated with loss function $\ell$ in the literature [e.g. Bhattacharya and Martin, 2020, Syring and Martin, 2020]. In particular, the usual Bayesian posterior (1) is a special case when the loss function is $\ell ( X , \theta ) = - \log p ( X \mid \theta )$ and $\alpha = 1$ . For Bayesian quantile regression, we may take the check loss function $\ell ( x , q ) = ( q - x ) \cdot ( \tau - 1 ( q < x ) )$ for a given quantile level $\tau \in ( 0 , 1 )$ , since the $\tau$ -th quantile of any one-dimensional random variable $X$ corresponds to the population risk function minimizer $\operatorname { a r g m i n } _ { q \in \mathbb { R } } \mathbb { E } [ \ell ( X , q ) ]$ .

A direct computation of either the posterior $p ( \theta | X ^ { ( n ) } )$ or the pseudo-posterior (2) involves the normalisation constant (the denominator) as a $d$ -dimensional integral, which is often analytically intractable unless the prior distributions form a conjugate family to the likelihood (criterion) function. In practice, Markov chain Monte Carlo (MCMC) algorithm [Hastings, 1970, Geman and Geman, 1984, Robert et al., 2004] is instead employed as an automatic machinery for sampling from the (pseudo-)posterior, whose implementation is free of the unknown normalisation constant. The aim of this paper is to provide a rigorous theoretical analysis on the computational complexity of a popular and widely used class of MCMC algorithms described below. In particular, we are interested in characterizing a sharp dependence of their mixing times on the parameter dimension in the context of Bayesian posterior sampling.

# 2.2 Metropolis-adjusted Langevin algorithm

Consider a generic (possibly unnormalized) density function $f ( \theta ) = \mathrm { e x p } \{ - U ( \theta ) \}$ defined on a set $\Theta \subset$ $\mathbb { R } ^ { d }$ , where $U : \Theta \to \mathbb { R }$ is called the potential (function) associated with $f$ . For example, in the Bayesian setting with target posterior (2), we can take $U ( \theta ) = - \log \pi ( \theta ) - \mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } )$ . Suppose our goal is to sample from the probability distribution µ induced by f , where µ(A) = RA f(θ) dθR f(θ) dθ f or any measurable set $A \subset \Theta$ . Metropolis-adjusted Langevin algorithm (MALA), as an instance of MCMC with a special design of the proposal distribution, aims at producing a sequence of random points $\{ \theta _ { k } \} _ { k \ge 0 }$ in $\Theta$ such that the distribution of $\theta _ { k }$ approaches $\mu$ as $k$ tends to infinity, so that for sufficiently large $k _ { 0 }$ , the $k _ { 0 }$ -th iterate $\theta _ { k _ { 0 } }$ can be viewed as a random variable approximately sampled from the target distribution $\mu$ . In practice, every $k _ { 0 }$ iterates from the chain can be collected (called thinning), which together form approximately independent draws from $\mu$ .

Specifically, given step size $\widetilde { h } > \widetilde { 0 }$ and initial distribution $\mu _ { 0 }$ on $\Theta$ , MALA produces $\{ \theta _ { k } \} _ { k \ge 0 }$ sequentially as follows: for $k = 0 , 1 , 2 , \ldots$ ,

1. (Initialization) If $k = 0$ , sample $\theta _ { 0 }$ from $\mu _ { 0 }$ ;

2. (Proposal) If $k \geq 1$ , given previous state $\theta _ { k - 1 }$ , generate a candidate point $y _ { k }$ from proposal distribution $N _ { d } \big ( \theta _ { k - 1 } - \widetilde { h } \nabla U \big ( \theta _ { k - 1 } \big ) , 2 \widetilde { h } I _ { d } \big )$ whose density function is denoted as $Q ( \theta _ { k - 1 } , \cdot )$ , or equivalently,

$$
y _ { k } = \theta _ { k - 1 } - \widetilde { h } \nabla U ( \theta _ { k - 1 } ) + \sqrt { 2 \widetilde { h } } z _ { k } , \quad \mathrm { w i t h } z _ { k } \sim N _ { d } ( 0 , I _ { d } ) .
$$

3. (Metropolis-Hasting rejection/correction) Set acceptance probability $A ( \theta _ { k - 1 } , y _ { k } ) : = 1 \land \alpha ( \theta _ { k - 1 } , y _ { k } )$ with acceptance ratio statistic

$$
\alpha ( \theta _ { k - 1 } , y _ { k } ) : = \frac { f ( y _ { k } ) \cdot Q ( y _ { k } , \theta _ { k - 1 } ) } { f ( \theta _ { k - 1 } ) \cdot Q ( \theta _ { k - 1 } , y _ { k } ) } .
$$

Flip a coin and accept $y _ { k }$ with probability $A ( \theta _ { k - 1 } , y _ { k } )$ and set $\theta _ { k } = y _ { k }$ ; otherwise, set $\theta _ { k } = \theta _ { k - 1 }$ . It is straightforward to verify that MALA described above produces a Markov chain whose transition kernel is

$$
T ( \theta , \mathrm { d } y ) = \Big ( 1 - \int _ { \Theta } A ( \theta , y ) Q ( \theta , y ) \mathrm { d } y \Big ) \cdot \delta _ { \theta } ( \mathrm { d } y ) + A ( \theta , y ) Q ( \theta , y ) \mathrm { d } y ,
$$

{zrejection probability

where $\delta _ { \theta }$ denotes the point mass measure at $\theta$ . In practice, the target density $f$ can be non-smooth at certain point $\theta \in \Theta$ , and we address this issue by replacing the gradient $\nabla U ( \theta )$ with any of its subgradient $\widetilde { \nabla } U ( \boldsymbol { \theta } )$ in MALA. That means, the proposal distribution $Q$ is being chosen as $N _ { d } ( \theta _ { k - 1 } -$ $\widetilde { h } \widetilde { \nabla } U ( \theta _ { k - 1 } ) , 2 \widetilde { h } )$ and other aspects of the MALA algorithm remain unchanged. Furthermore, MALA can be generalized by introducing a symmetric positive-definite preconditioning matrix $\widetilde { I } \ \in \ \mathbb { R } ^ { d \times d }$ , so that the proposal $Q$ in MALA is modified as $\overset { \cdot } { N } _ { d } ( \theta _ { k - 1 } - \widetilde { h } \widetilde { I } \widetilde { \nabla } \widetilde { U } ( \theta _ { k - 1 } ) , 2 \widetilde { h } \widetilde { I } )$ . It has been shown that [Girolami and Calderhead, 2011, Vacar et al., 2011] for a suitable preconditioning matrix, the resulting preconditioned MALA can help to alleviate the issue caused by the anisotropicity of the target measure. We illustrate both empirically (c.f. Appendix A.1) and theoretically (c.f. Corollary 1) that a suitable preconditioning matrix may improve the convergence of the sampling algorithm for Bayesian posteriors. As a common practice [Chen et al., 2020, Lovasz and Simonovits ´ , 1993] to simplify the analysis of MALA, in this paper, we consider the $\zeta$ -lazy version of MALA, where at each iteration, the chain is forced to remain unchanged with probability $\zeta$ . The corresponding Markov transition kernel of the $\zeta$ -lazy version of MALA is given by

$$
T ^ { \zeta } ( \theta , \mathrm { d } y ) = \big ( 1 - ( 1 - \zeta ) \cdot \int _ { \Theta } A ( \theta , y ) Q ( \theta , y ) \mathrm { d } y \big ) \cdot \delta _ { \theta } ( \mathrm { d } y ) + ( 1 - \zeta ) \cdot A ( \theta , y ) Q ( \theta , y ) \mathrm { d } y .
$$

A closely related algorithm is the unadjusted Langevin algorithm [ULA, Durmus and Moulines, 2017, Cheng et al., 2018, Roberts and Tweedie, 1996, Dalalyan, 2017], which corresponds to discretization of the following Langevin stochastic differential equation (SDE),

$$
\mathrm { d } X _ { t } = - \nabla U ( X _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , \quad t > 0 ,
$$

and does not have the Metropolis-Hasting correction step 3. As a consequence, the stationary distribution√ of ULA is of order $\mathcal { O } ( \sqrt { d h } ) \overline { { } }$ away from $\mu$ under several commonly used metrics [Durmus et al., 2019]. Due to this error, even in the strongly log-concave scenario, unlike MALA which requires at most poly-$\log ( 1 / \varepsilon )$ iterations with a constant step size $h$ to get one sample distributed close from $\mu$ with accuracy $\varepsilon$ , ULA requires poly- $( 1 / \varepsilon )$ iterations and an $\varepsilon$ -dependent choice of $h$ [Durmus et al., 2019].

Another closely related algorithm is the classical Metropolis random walk (MRW), which instead uses $N _ { d } \big ( \theta _ { k - 1 } , 2 \widetilde { h } \ : \dot { I } _ { d } \big )$ without the gradient term in the proposal distribution $Q$ . As we will see, by using the extra gradient information, the dimension dependence of the mixing time can be improved from $\mathcal O ( d )$ [Gelman et al., 1997, Dwivedi et al., 2019] to $\mathcal { O } ( d ^ { 1 / 3 } )$ for sampling from Bayesian posteriors.

# 2.3 Problem setup

The goal of this paper is to characterize the mixing time of MALA for sampling from the Bayesian pseudo-posterior $\pi _ { n }$ defined in (2). Assume we have access to a warm start defined as follows.

Definition 1. We say $\mu _ { 0 }$ is an $M _ { 0 }$ -warm start with respect to the stationary distribution $\mu ,$ , if $\mu _ { 0 } ( E ) \leq$ $M _ { 0 } \mu ( E )$ holds for all Borel set $E \subset \mathbb { R } ^ { d }$ , and we call $M _ { 0 }$ the warming parameter.

We state our problem as characterizing the $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence of the Markov chain produced by (preconditioned) MALA starting from an arbitrary $M _ { 0 }$ -warm start $\mu _ { 0 }$ for obtaining draws from $\pi _ { n } ( \theta )$ , which is mathematically defined as the maximum of the minimal number of steps required for the chain to be within $\varepsilon ^ { 2 } { - } \chi ^ { 2 }$ divergence from its stationary distribution, over $M _ { 0 }$ -warm starts, or $\tau _ { \mathrm { m i x } } ( \varepsilon , M _ { 0 } ) = \operatorname* { m a x } \left\{ \tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) : \mu _ { 0 } \right.$ is an $M _ { 0 }$ -warm start with respect to $\pi _ { n } \}$

$$
\tau _ { \operatorname* { m i x } } ( \varepsilon , \mu _ { 0 } ) = \operatorname* { i n f } \big \{ k \in \mathbb { N } : \sqrt { \chi ^ { 2 } \big ( \mu _ { k } , \pi _ { n } \big ) } \leq \varepsilon \big \} ,
$$

where $\mu _ { k }$ denotes the probability distribution obtained after $k$ steps of the Markov chain. Note that a mixing time upper bound in $\chi ^ { 2 }$ divergence implies that in total variation distance since $\| p - q \| _ { \mathrm { T V } } \leq$ $\sqrt { \chi ^ { 2 } ( p , q ) }$ .

# 3 Mixing Time Bounds via $s$ -Conductance Profile

In this section, we introduce a general technique of using $s$ -conductance profile to bound the mixing time of a Markov chain. We first review some common concepts and previous results in Markov chain convergence analysis, and then provide an improved analysis for obtaining a sharp mixing time upper bound of MALA in this work.

Ergodic Markov chains: Given a Markov transition kernel $T ( \cdot , \cdot )$ with stationary distribution $\mu \in$ ${ \mathcal { P } } ( \mathbb { R } ^ { d } )$ , the ergodic flow of a set $S$ is defined as

$$
\phi ( S ) = \int _ { S } \left\{ \int _ { S ^ { c } } T ( \xi , \mathrm { d } y ) \right\} \mu ( \mathrm { d } \xi ) .
$$

The ergodic flow captures the mass of points leaving $S$ (i.e., $T ( \xi , S ^ { c } ) = \int _ { S ^ { c } } T ( \xi , \mathrm { d } y ) )$ on average under stationary distribution $\mu$ in one step of the Markov chain. A Markov chain is said to be ergodic if $\phi ( S ) > 0$ for all measurable set $S \subset \mathbb { R } ^ { d }$ with $0 < \mu ( S ) < 1$ . Let $\mu _ { k }$ denote the probability distribution

obtained after $k$ steps of a Markov chain. If the Markov chain is ergodic, then $\mu _ { k } \to \mu$ as $k  \infty$ in total variation distance; see, for example, Corollary 1.6 of Lovasz and Simonovits ´ [1993].

Conductance of Markov chain and rapid mixing: The (global) conductance of an ergodic Markov chain characterizes the least relative ratio between $\phi ( S )$ and the measure $\mu ( S )$ of $S$ , and is formally defined as

$$
\Phi = \operatorname* { i n f } { \Bigg \{ } { \frac { \phi ( S ) } { \mu ( S ) } } : 0 < \mu ( S ) \leq { \frac { 1 } { 2 } } { \Bigg \} } .
$$

A Markov chain with low conductance tends to become trapped in a subset of its states, whereas one with high conductance has more freedom to explore and transition across its entire state space. The conductance is related to the spectral $\mathrm { g a p } ^ { 2 }$ of the Markov chain via Cheeger’s inequality [Cheeger, 2015], and thus can be used to characterize the convergence of the Markov chain. For example, Corollary 1.5 in Lovasz and Simonovits ´ [1993] shows that if $\mu _ { 0 }$ is an $M _ { 0 }$ -warm start with respect to the stationary distribution $\mu$ , then

$$
\| \mu _ { k } - \mu \| _ { \mathrm { T V } } \leq \sqrt { M _ { 0 } } \Bigl ( 1 - \frac { \Phi ^ { 2 } } { 2 } \Bigr ) ^ { k } , \quad k \geq 0 .
$$

Furthermore, some people consider the more flexible notion of $s$ -conductance, defined as

$$
\Phi _ { s } : = \operatorname* { i n f } { \biggl \{ } { \frac { \phi ( S ) } { \mu ( S ) - s } } : s < \mu ( S ) \leq { \frac { 1 } { 2 } } { \biggr \} } , \quad { \mathrm { f o r ~ } } s \in ( 0 , 1 / 2 ) ,
$$

which restricts the infimum over all sets with a probability greater than $s$ . This restriction avoids including sets in the conductance bound that have poor conductance but receive negligible probability, which should be less significant to the overall mixing of the Markov chain. Specifically for sampling from Bayesian posteriors, this refined analysis allows us to focus our calculations on these “highest posterior regions” while avoiding some unwieldy tail probability regions (e.g., the region defined in Condition A.3). Using the $s$ -conductance, Corollary 1.6 in Lovasz and Simonovits ´ [1993] proves a similar bound implying the exponential convergence of the algorithm up to accuracy level $s$ as

$$
\Vert \mu _ { k } - \mu \Vert _ { \mathrm { T V } } \leq M _ { 0 } s + M _ { 0 } \Bigl ( 1 - \frac { \Phi _ { s } ^ { 2 } } { 2 } \Bigr ) ^ { k } , \quad k \geq 0 .
$$

Consequently, the $\varepsilon$ -mixing time with respect to the total variation distance of the Markov chain starting from an $M _ { 0 }$ -warm start can be upper bounded by $\frac { 2 } { \Phi _ { s } ^ { 2 } } \log \frac { 2 M _ { 0 } } { \varepsilon }$ 2M0ε if we choose s = ε2M .

Conductance profile of Markov chain: Instead of controlling mixing times via a worst-case conductance bound, some recent works have introduced more refined methods based on the conductance profile. The conductance profile is defined as the following collection of conductance,

$$
\Phi ( v ) : = \operatorname* { i n f } { \biggl \{ } { \frac { \phi ( S ) } { \mu ( S ) } } : 0 < \mu ( S ) \leq v { \biggr \} } , \quad \operatorname { i n d e x e d } \operatorname { b y } v \in \left( 0 , { \frac { 1 } { 2 } } \right] .
$$

Note that the classic conductance constant $\Phi$ is a special case that can be expressed as $\Phi = \Phi ( \mathrm { \frac { 1 } { 2 } } )$ . Based on the conductance profile, Chen et al. [2020] consider the concept of $\Omega$ -restricted conductance profile for a convex set $\Omega$ , given by

$$
\Phi _ { \Omega } ( v ) : = \operatorname* { i n f } { \left\{ \frac { \phi ( S ) } { \mu ( S \cap \Omega ) } : 0 < \mu ( S \cap \Omega ) \leq v \right\} } , \quad v \in \left( 0 , \frac { \mu ( \Omega ) } { 2 } \right] .
$$

It has been shown in Chen et al. [2020] that given an $M _ { 0 }$ -warm start $\mu _ { 0 }$ , if

$$
\mu ( \Omega ) \geq 1 - \frac { \varepsilon ^ { 2 } } { 3 M _ { 0 } ^ { 2 } } \quad \mathrm { a n d } \quad \Phi _ { \Omega } ( v ) \geq \sqrt { B \log \frac { 1 } { v } } \mathrm { ~ f o r ~ a l l ~ } v \in \bigg [ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } \bigg ] ,
$$

then the $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence of the chain is bounded from above by $\begin{array} { r } { \mathcal { O } \bigl ( \frac { 1 } { B } \log \bigl ( \frac { \log M _ { 0 } } { \varepsilon } \bigr ) \bigr ) } \end{array}$ . Therefore, compared with the (global) conductance, employing the technique of conductance profile may improve the warming parameter dependence in the mixing time bound from $\log M _ { 0 }$ to $\log \log M _ { 0 }$ . This improvement from a logarithmic dependence to the double logarithmic dependence may dramatically sharpen the mixing time upper bound, since in a typical Bayesian setting $M _ { 0 }$ may grow exponentially in the dimension $d$ . However, one drawback of the conductance profile technique from Chen et al. [2020] is that the high probability set $\Omega$ should be constrained to be convex (Lemma 4 of Chen et al. [2020]) to bound the $\Omega$ -restricted conductance profile $\Phi _ { \Omega } ( v )$ . This convexity constraint may cause $\Phi _ { \Omega } ( v )$ to have a worse dimension dependence compared with the complexity analysis using the $s$ - conductance $\Phi _ { s }$ .

In order to address the above issues of previous analysis, we introduce the following notion of $s$ conductance profile , which combines ideas from the $s$ -conductance and conductance profile,

$$
\Phi _ { s } ( v ) : = \operatorname* { i n f } \left. \left. \frac { \phi ( S ) } { \mu ( S ) - s } \right| s < \mu ( S ) \leq v \right. \quad \mathrm { i n d e x e d } \mathrm { b y } s \in \left( 0 , \frac { 1 } { 2 } \right) \mathrm { ~ a n d ~ } v \in \left( s , \frac { 1 } { 2 } \right] .
$$

The $s$ -conductance profile evaluated at $\begin{array} { r } { v \ = \ \frac { 1 } { 2 } } \end{array}$ corresponds to the $s$ -conductance that is commonlyused in previous study for analyzing the mixing time of Markov chain [Chewi et al., 2021, Dwivedi et al., 2019]. We show in the following lemmas that a lower bound on the $s$ -conductance profile can be translated into an upper bound on the mixing time in $\chi ^ { 2 }$ -squared divergence. We formulate here an informal result and postpone a more detailed statement to Appendix A.2.

Lemma 1 (Mixing time bound via $s$ -conductance profile (informal)). For any error tolerance $\varepsilon \in$ $( 0 , 1 )$ , the mixing time in $\chi ^ { 2 }$ divergence of the $\zeta$ -lazy version of MALA over $M _ { 0 }$ -warm starts can be bounded as

$$
\tau _ { \mathrm { m i x } } ( \varepsilon , M _ { 0 } ) \lesssim \zeta ^ { - 1 } \cdot \Big ( \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { \mathrm { d } v } { v \Phi _ { s } ^ { 2 } ( v ) } + \frac { 1 } { \Phi _ { s } ^ { 2 } ( \frac { 1 } { 2 } ) } \log ( \frac { 1 } { \varepsilon } ) \Big ) , \quad s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } .
$$

It is worth noting that since $\Phi _ { s } ( v )$ is a decreasing function of $v$ , by replacing $\Phi _ { s } ( v )$ with its lower bound $\Phi _ { s } \ = \ \Phi _ { s } ( \mathrm { \frac { 1 } { 2 } } )$ , one can obtain a mixing time bound via $s$ -conductance. However, instead of simply considering the worst case, the integral $\int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { \mathrm { d } v } { v \Phi _ { s } ^ { 2 } ( v ) }$ averages over $\Phi _ { s } ( v )$ , offering a possible improvement in the dependence on warming parameter $M _ { 0 }$ . To establish a lower bound for the $s$ - conductance profile, we can employ the “overlap argument” frequently used in the literature [Chewi et al., 2021, Chen et al., 2020, Belloni and Chernozhukov, 2009, Wu et al., 2022], that is, 1. prove a log-isoperimetric inequality for $\mu$ ; 2. bound the total variation distance between $T ( x , \cdot )$ and $T ( z , \cdot )$ for any two sufficiently close points $x , z$ in a high probability set (not necessarily convex) of $\mu$ . We leave a detailed description of this argument to Appendix A.2.

Among previous works of mixing time analysis of MALA, Chen et al. [2020] study the problem of sampling from general smooth and strongly log-concave densities, using the technique of $\Omega$ -restricted conductance profile. Their bound has a double logarithmic $\log \log M _ { 0 }$ dependence on the warmth parameter $M _ { 0 }$ under certain regime (of step size $h$ ), and a sub-optimal $\mathcal O ( d )$ -dependence on the dimension. On the other hand, Chewi et al. [2021] study the same problem as Chen et al. [2020] and obtain a mixing time bound with an optimal $O ( d ^ { \frac { 1 } { 2 } } )$ -dependence, based on the $s$ -conductance technique. However, the bound in Chewi et al. [2021] has a quadratic dependence on $\log M _ { 0 }$ . By utilizing our $s$ -conductance profile argument, when $\log M _ { 0 }$ and $h ^ { - 1 }$ are not of constant order, we can improve their bounds from $\hat { h } ^ { - 1 } \log ( \frac { \bar { M } _ { 0 } } { \epsilon } )$ to $\operatorname* { m a x } \{ h ^ { - 1 } \log ( \frac { \log M _ { 0 } } { \epsilon } ) , \log M _ { 0 } \}$ , where $h$ is the step size used in Theorem 3 of Chewi et al. [2021].

# 4 Mixing Time of MALA

In this section, we describe our main result by providing an upper bound to the mixing time of (preconditioned) MALA for sampling from the Bayesian pseudo-posterior $\pi _ { n }$ . We consider the $\zeta$ -lazy version of

MALA and assume that a warm start is accessible, which is a common assumption [e.g. Dwivedi et al., 2019, Mangoubi and Vishnoi, 2019]. For example, Corollary 1 in Section 5.1 provides a construction of $M _ { 0 }$ -warm start for general Gibbs posterior with smooth criterion function, where $M _ { 0 }$ is bounded above by an $( n , d )$ -independent constant.

Note that the Bayesian pseudo-posterior with criterion function ${ \mathcal { C } } _ { n }$ can be rewritten as

$$
{ \begin{array} { r l } & { ~ \pi _ { n } ( \theta \mid X ^ { ( n ) } ) = { \cfrac { \exp { \big \{ } - V _ { n } { \big ( } { \sqrt { n } } ( \theta - { \widehat { \theta } } ) { \big ) } { \big \} } } { \int _ { \Theta } \exp { \big \{ } - V _ { n } { \big ( } { \sqrt { n } } ( \theta - { \widehat { \theta } } ) { \big ) } { \big \} } ~ \forall \theta \in \Theta , } } } \\ & { { \mathrm { w h e r e } } \quad { \widehat { \theta } } = { \underset { \theta \in \Theta } { \operatorname { a r g m a x } } } ~ { \mathcal { C } } _ { n } ( \theta ) \quad { \mathrm { a n d } } } \\ & { V _ { n } ( \xi ) = - { \mathcal { C } } _ { n } { \bigg ( } { \widehat { \theta } } + { \frac { \xi } { \sqrt { n } } } ; X ^ { ( n ) } { \bigg ) } + { \mathcal { C } } _ { n } { \big ( } { \widehat { \theta } } ; X ^ { ( n ) } { \big ) } - \log \pi { \bigg ( } { \widehat { \theta } } + { \frac { \xi } { \sqrt { n } } } { \bigg ) } + \log \pi ( { \widehat { \theta } } ) } \end{array} }
$$

is the corresponding rescaled potential (function). In the expression of $V _ { n }$ , we deliberately added two terms independent of $\xi$ so that $V _ { n } ( 0 ) = 0$ for simplifying the analysis. Motivated by the classical Bernstein-von Mises (BvM) theorem3 [van der Vaart, 2000, Ghosh and Ramamoorthi, 2003] for Bayesian posteriors, we impose following conditions on $V _ { n }$ , stating that $V _ { n } ( \xi )$ is close to a quadratic form and the subgradient of $V _ { n } ( \xi )$ employed in MALA is close to a linear form, uniformly over a high probability set of the rescaled target measure $\pi _ { \mathrm { l o c } } = ( { \sqrt { n } } ( \cdot - { \widehat { \theta } } ) ) _ { \# } \pi _ { n }$ .4 Here $\pi _ { \mathrm { l o c } }$ corresponds to the measure of the localized random variable $\xi = \sqrt { n } ( \theta - \widehat { \theta } )$ for $\theta \sim \pi _ { n } ( \theta | X ^ { ( n ) } )$ , and the transformation ${ \sqrt { n } } ( \cdot - { \widehat { \theta } } )$ makes the limiting distribution of $\xi$ zero-centered and has constant-order variances.

Condition A: There exists a tolerance $\varepsilon \in \mathsf { \Gamma } ( 0 , 1 )$ , preconditioning matrix $\widetilde { I }$ , step size parameter $h$ (rescaled by $n$ ), warming parameter $M _ { 0 }$ , numbers $R , \widetilde { \varepsilon } _ { 0 } , \widetilde { \varepsilon } _ { 1 } \geq 0$ , $\rho _ { 1 } , \rho _ { 2 } > 0$ and a symmetric positive definite matrix $J \in \mathbb { R } ^ { d \times d }$ so that

1. for any

$$
\begin{array} { r l r } {  { \boldsymbol { x } : \| \widetilde { \boldsymbol { I } } ^ { - 1 / 2 } \boldsymbol { x } \| \le R \} ^ { 5 } } } \\ & { } & \\ & { } & { \big | V _ { n } ( \xi ) - \frac { 1 } { 2 } \xi ^ { T } J \xi \big | \le \widetilde { \varepsilon } _ { 0 } \quad a n d \quad \big \| \widetilde { \nabla } V _ { n } ( \xi ) - J \xi \big \| \le \widetilde { \varepsilon } _ { 1 } , } \end{array}
$$

where $\widetilde { \nabla } V _ { n } ( \boldsymbol { \xi } )$ is a subgradient of $V _ { n } ( \xi )$ ;

2. $\rho _ { 1 } I _ { d } \preceq \widetilde { J } = \widetilde { I } ^ { 1 / 2 } J \widetilde { I } ^ { 1 / 2 } \preceq \rho _ { 2 } I _ { d } ,$

$$
\begin{array} { r } { \pi _ { n } \big ( \sqrt { n } \| \widetilde { I } ^ { - 1 / 2 } ( \theta - \widehat { \theta } ) \| \leq R / 2 \big ) \geq 1 - \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { h \rho _ { 1 } \varepsilon ^ { 2 } } { M _ { 0 } ^ { 2 } } a n d R \geq 8 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) } . } \end{array}
$$

The first inequality in Condition A.1 requires that $V _ { n } ( \xi )$ can be uniformly approximated by the quadratic term $\scriptstyle { \frac { 1 } { 2 } } \xi ^ { T } J \xi$ with an approximation error $\widetilde { \varepsilon } _ { 0 }$ . This requirement is implied by the classical BvM result, which is commonly utilized in MCMC mixing time analysis for Bayesian posterior sampling [Belloni and Chernozhukov, 2009, Ascolani and Zanella, 2023]. It is noteworthy that we do not impose any smoothness or convexity constraints on $V _ { n } ( \xi )$ , and the deviation characteristic $\widetilde { \varepsilon } _ { 0 }$ can take any value. We also keep track of the impact of this deviation in the final mixing time bound, as reflected in Theorem 3, where we explicitly show the dependency of the mixing time on this approximation error, $\widetilde { \varepsilon } _ { 0 }$ . The result reveals that the mixing time exhibits an exponential dependence on $\widetilde { \varepsilon } _ { 0 }$ . The second inequality in Condition A.1 assumes that the subgradient of $V _ { n } ( \xi )$ can be approximated by the linear term $J \xi$ with an approximation error $\widetilde { \varepsilon } _ { 1 }$ . Although less standard, this condition is crucial since $\widetilde { \varepsilon } _ { 1 }$ governs the efficacy of the subgradient used in MALA to adjust the proposal distribution and facilitate faster exploration of the parameter space. As we will see in Theorem 3, a small $\widetilde { \varepsilon } _ { 1 }$ enables MALA, leveraging (sub)gradient information, to improve upon MRW in terms of mixing time. Condition A.2 requires the asymptotic covariance matrix $J$ , after rescaling by the preconditioning matrix, to have its maximum eigenvalue upper-bounded by $\rho _ { 2 }$ and its minimum eigenvalue lower-bounded by $\rho _ { 1 }$ . The condition number $\begin{array} { r } { \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } } \end{array}$ serves as an indicator of how well the preconditioning matrix $\widetilde { I }$ is chosen to alleviate issues arising from the anisotropy of the target distribution. As we will see from Theorem 3, a small $\kappa$ will lead to a lower mixing time. The last condition (Condition A.3) assumes that the radius $R$ of the compact set $K$ , considered in Condition A.1, is sufficiently large. This ensures that $K$ is a high probability set under $\pi _ { \mathrm { l o c } }$ . This assumption guarantees that the region where the density $\pi _ { \mathrm { l o c } }$ (or $\pi _ { n }$ ) deviates significantly from a Gaussian form, and is possibly non-smooth and non-log-concave, is negligible, thereby reducing the chances of the Markov chain becoming trapped in such regions.

In summary, Condition A requires the localized (rescaled) posterior $\pi _ { \mathrm { l o c } } = ( { \sqrt { n } } ( \cdot - { \widehat { \theta } } ) ) _ { \# } \pi _ { n }$ to be close to a Gaussian distribution $N _ { d } ( 0 , J ^ { - 1 } )$ , so that we can analyze the mixing time of MALA for sampling $\pi _ { n }$ or $\pi _ { \mathrm { l o c } }$ (note that the complexity for sampling from $\pi _ { n }$ with step size $\widetilde { h } = h / n$ is equivalent to that from $\pi _ { \mathrm { l o c } }$ with rescaled step size $h$ ) by comparing its transition kernel $T$ expressed in (4) with the transition kernel $T ^ { \Delta }$ induced from the MALA for sampling the Gaussian distribution. Interestingly, we find that as long as the deviance of $\pi _ { \mathrm { l o c } }$ to Gaussian is sufficiently small but not necessarily diminishing as $n , d \to \infty$ , some key properties (more precisely, conductance lower bound) of $T ^ { \Delta }$ guarantee that the fast mixing of MALA will be inherited by $T$ , so that the mixing time associated with $T$ can be controlled. Using this argument, we prove a mixing time upper bound without imposing the smoothness and strongly convexity assumptions on $V _ { n } ( \xi )$ that are restrictive and commonly assumed in the literature for analyzing the convergence of MALA [Chewi et al., 2021, Chen et al., 2020]. As a concrete example, under mild assumptions, Condition A holds for a broad class of Gibbs posteriors [Bhattacharya and Martin, 2020] mentioned in Section 2.1 where the criterion function ${ \mathcal { C } } _ { n }$ is proportional to the negative empirical risk function $\mathcal { R } _ { n }$ , as long as $d$ is relatively small compared to $n$ (see Lemma 10 and Lemma 11 in Appendix B.3 for details). Now we are ready to state the following theorem.

Theorem 1 (MALA mixing time upper bound). Let $\pi _ { n }$ defined in (5) be the target distribution and $\zeta \in ( 0 , \frac { 1 } { 2 } ]$ be a lazy parameter. Assume Condition A holds for a tolerance $\varepsilon$ , warming parameter $M _ { 0 }$ , sample size $n$ , preconditioning matrix $\widetilde { I } _ { : }$ , rescaled step size $h _ { i }$ , and some $R > 0$ , $\widetilde { \varepsilon } _ { 1 } \geq 0 ,$ , $\rho _ { 2 } \geq \rho _ { 1 } > 0$ , and that there exists a small enough absolute $( n , d )$ -independent constant $c _ { 0 }$ so that the step size can be expressed as $\widetilde { h } = h / n$ with

$$
\nu = c _ { 0 } \cdot \left[ \rho _ { 2 } \left( d ^ { \frac { 1 } { 3 } } + d ^ { \frac { 1 } { 4 } } \left( \widetilde { \varepsilon } _ { 0 } + \log \frac { M _ { 0 } d \kappa } { \varepsilon } \right) ^ { \frac { 1 } { 4 } } + \left( \widetilde { \varepsilon } _ { 0 } + \log \frac { M _ { 0 } d \kappa } { \varepsilon } \right) ^ { \frac { 1 } { 2 } } + \| \widetilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \widetilde { \varepsilon } _ { 1 } ^ { 2 } \right) \right] ^ { - 1 } , w h e r e \kappa = c _ { 0 } \cdot \varepsilon \cdot D _ { 0 } ^ { \varepsilon } .
$$

then the $\zeta$ -lazy version of MALA with proposal distribution $N _ { d } ( \theta _ { k - 1 } - \widetilde { h } \widetilde { I } \widetilde { \nabla } U ( \theta _ { k - 1 } ) , 2 \widetilde { h } \widetilde { I } )$ and step size $\widetilde { h }$ has a maximal $\varepsilon$ -mixing time in $\chi ^ { 2 }$ divergence over $M _ { 0 }$ -warm starts being bounded as

$$
\tau _ { \operatorname* { m i x } } ( \varepsilon , M _ { 0 } ) \leq \frac { C _ { 1 } \exp ( 4 \widetilde { \varepsilon } _ { 0 } ) } { \zeta } \cdot \biggl \{ \left[ \rho _ { 1 } ^ { - 1 } \exp ( 8 \widetilde { \varepsilon } _ { 0 } ) \cdot h ^ { - 1 } \log \big ( \frac { \log M _ { 0 } } { \varepsilon } \big ) \right] \vee \log M _ { 0 } \biggr \} ,
$$

where $C _ { 1 }$ is an $( n , d )$ -independent constant.

The mixing time bound (7) is proved using the technique of $s$ -conductance profile introduced in Section 3. A similar mixing time bound can be obtained if when consider the sampling of $\pi _ { \mathrm { l o c } }$ constrained on the high probability set $K = \{ x : \| \widetilde { I } ^ { - 1 / 2 } x \| \leq R \}$ , which is adopted by Belloni and Chernozhukov [2009] for analyzing the mixing time of MRW; however, our result does not require such a constraining step. According to Theorem 1, for a fixed tolerance (accuracy level) $\varepsilon$ , the $\varepsilon$ -mixing time is determined by the parameter dimension $d$ , warming parameter $M _ { 0 }$ , preconditioning matrix $\widetilde { I }$ , approximation errors $\widetilde { \varepsilon } _ { 0 } , \widetilde { \varepsilon } _ { 1 }$ of the potential and the gradient, radius $R$ of the high probability set of $\pi _ { \mathrm { l o c } }$ and the precision matrix $J$ of the Gaussian approximation to $\pi _ { \mathrm { l o c } }$ . The derived mixing time bound is exponentially dependent on $\widetilde { \varepsilon } _ { 0 }$ , implying that a bound that is polynomial in $d$ can only be attained if $\widetilde { \varepsilon } _ { 0 }$ is either constant-order or logarithmic in $d$ . The fourth term $\| \widetilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \widetilde { \varepsilon } _ { 1 } ^ { 2 }$ in the expression of $h$ will be dominated by others once $\widetilde { \varepsilon } _ { 1 }$ is sufficiently small. For example, suppose $\widetilde { I } = I _ { d }$ , M0κε = O(d) and πloc has a sub-Gaussian type tail behavior, or

$$
\pi _ { \mathrm { l o c } } \left( \| \xi \| \ge c _ { 1 } ( \sqrt { d } + t ) \right) \le \exp ( - c _ { 2 } t ^ { 2 } ) , \quad t > 0 ,
$$

then we can choose the radius as $R = \mathcal { O } ( \sqrt { d } )$ , and the term $\| \tilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \widetilde { \varepsilon } _ { 1 } ^ { 2 }$ will be dominated by the $O ( d ^ { \frac { 1 } { 3 } } )$ term once $\widetilde { \varepsilon } _ { 1 } = \mathcal { O } ( d ^ { - \frac { 1 } { 3 } } )$ . This suggests that a $d ^ { \frac { 1 } { 3 } }$ -mixing time upper bound is achievable as long as the (sub)gradient used in MALA deviates from a linear form with approximation error at most $d ^ { - \frac { 1 } { 3 } }$ , which is independent of the sample size. Therefore, when $d \ll n$ , it is safe to fix a mini-batch dataset for computing the (sub)gradient in MALA instead of using the full batch. As another remark, our theorem also gives a tight mixing time upper bound $\mathcal O ( d )$ of MRW by taking $\widetilde { \varepsilon } _ { 1 } = O ( 1 )$ , corresponding to the case where the gradient estimate is completely uninformative.

Our mixing time bound has a linear dependence (modulo logarithmic term) on the condition number $\kappa = \rho _ { 2 } / \rho _ { 1 }$ , which matches the best condition number dependence for MALA under strong convexity [Wu et al., 2022] and we show the tightness of the condition number dependence in Theorem 3 of Appendix A.3. Moreover, by introducing preconditioning matrix $\widetilde { I }$ , a small condition number can be obtained once $\widetilde { I }$ acts as a reasonable estimator to $J ^ { - 1 }$ , which will lead to a faster mixing time when $J$ is ill-conditioned. On the other hand, assume $\kappa$ is bounded above by an $( n , d )$ -independent constant and

$$
\left( \| \widetilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \widetilde { \varepsilon } _ { 1 } ^ { 2 } \right) \vee \log \left( \frac { M _ { 0 } } { \varepsilon } \right) \leq d ^ { \frac { 1 } { 3 } } ,
$$

we have $\begin{array} { r } { \tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) \leq C _ { 1 } d ^ { \frac { 1 } { 3 } } \log ( \frac { \log M _ { 0 } } { \varepsilon } ) } \end{array}$ . This upper bound matches the lower bound proved in Chewi et al. [2021] that the mixing time of MALA for sampling from the standard Gaussian target is at least $O ( d ^ { \frac { 1 } { 3 } } )$ , and it improves the warming parameter dependence from $\log M _ { 0 }$ to $\log ( \log M _ { 0 } )$ compared with the upper bound proved in Chewi et al. [2021]. Therefore, in order to attain the best achievable mixing time $O ( d ^ { \frac { 1 } { 3 } } )$ , we need to find a initial distribution $\mu _ { 0 }$ that is close to $\pi _ { n }$ , so that the warming parameter $M _ { 0 }$ can be controlled. For a generic log-concave distribution, it has been shown that a warm start with warming parameter $M _ { 0 }$ polynomial in $d$ can be obtained with $d ^ { \frac { 1 } { 2 } }$ complexity, as demonstrated by Altschuler and Chewi [2023]. However, efficiently obtaining a poly $( d )$ warm start for general nonlog-concave sampling problems is infeasible. Fortunately, in our Bayesian posterior sampling context, although $\pi _ { n }$ may not be log-concave, large sample asymptotic theory (refer to Section 5, for instance) ensures that $\pi _ { n }$ is approximately Gaussian. Therefore, using the Gaussian distribution $N _ { d } ( \widehat { \theta } , n ^ { - 1 } \widetilde { I } )$ , constrained on a compact set, as the initialization $\mu _ { 0 }$ , is a natural choice. To support this initialization scheme, the following lemma provides an upper bound for the corresponding warming parameter $M _ { 0 }$ .

Lemma 2 (Warming parameter control). Suppose Condition $A$ is satisfied. For any compact set $K \subset \mathbb { R } ^ { d }$ , the initial distribution as

$$
\mu _ { 0 } = N _ { d } ( \widehat \theta , n ^ { - 1 } \widetilde I ) \vert _ { \{ \theta : \sqrt { n } ( \theta - \widehat \theta ) \in K \} }
$$

is $M _ { 0 }$ -warm with respect to $\pi _ { n }$ , where

$$
\log M _ { 0 } \leq - \log \pi _ { n } \big ( \{ \theta : \sqrt { n } ( \theta - \widehat \theta ) \in K \} \big ) + \operatorname* { s u p } _ { \xi \in K } \big | \xi ^ { T } ( \widetilde { I } ^ { - 1 } - J ) \xi \big | + 2 \cdot \operatorname* { s u p } _ { \xi \in K } \lvert V _ { n } ( \xi ) - \frac { 1 } { 2 } x ^ { T } J _ { 3 }
$$

In order to construct a feasible warm start using Lemma 2, it is necessary to compute the maximizer $\widehat { \theta }$ of the criterion function $\mathcal { C } _ { n } ( \theta )$ . An inaccurate approximation of $\widehat { \theta }$ may cause the warming parameter $M _ { 0 }$ to grow linearly with the sample size $n$ , a similar observation also noted in studies by Ascolani and Zanella [2023], Belloni and Chernozhukov [2009]. While it is generally challenging to obtain solutions for non-convex optimization problems, there are cases where optimizing a nearly quadratic function can be much easier compared to sampling from a nearly Gaussian distribution. A specific example is Bayesian quantile regression, where the estimation of $\hat { \theta }$ can be efficiently achieved using linear programming techniques. Our theoretical results also suggest that under Condition A, we can control the warming parameter $M _ { 0 }$ in MALA by choosing a reasonable estimator $\widetilde { I }$ for the inverse asymptotic covariance matrix $J ^ { - 1 }$ of $\pi _ { \mathrm { l o c } }$ . For instance, if $\tilde { I }$ is chosen to be the identity matrix and $J$ has a bounded operator norm, then $\log M _ { 0 }$ should be of order $\mathcal O ( d )$ . Furthermore, in Bayesian Gibbs posterior sampling, where the loss function $\ell$ is continuously twice differentiable, a viable option for approximating $J ^ { - 1 }$ could be the plug-in estimator:

$$
\widetilde { I } = \bigg \{ \frac { 1 } { | S | } \sum _ { i \in S } \mathrm { H e s s } _ { \theta } ( \ell ( X _ { i } , \widehat { \theta } ) ) \bigg \} ^ { - 1 } ,
$$

where $S$ is a subset of $1 , 2 , \cdots , n$ , and ${ \mathrm { H e s s } } _ { \theta } ( \ell ( x , \theta ) )$ denotes the Hessian matrix of $\ell ( x , \cdot )$ evaluated at $\theta$ . Notably, since the warming parameter $M _ { 0 }$ can be of order $\mathcal { O } ( d ^ { 1 / 3 } )$ for achieving the best possible mixing time, it is feasible to compute the plug-in estimator using only a mini-batch of data, the size of which depends solely on the dimension, rather than the full dataset. Further details can be found in Corollary 1.

According to Lemma 2 and Theorem 1, a reasonably good approximation $\widetilde { I }$ to matrix $J$ in Condition A will improve both the mixing time of MALA after burn-in period and the initialization affecting the burn-in. For completeness, we also provide an experiment in Appendix A.1 for investigating the impact of the preconditioning matrix and initial distribution on the performance of MALA. However, in some complicated problems, especially when $\log \pi _ { \mathrm { l o c } }$ is not differentiable, a good estimator for the matrix $J$ may not be easy to construct. One possible strategy is to use adaptive MALA [Atchade´, 2006], where the preconditioner $\widetilde { I }$ and step size $h$ are updated in each iteration by using the history draws. It has been empirically shown in Atchade´ [2006] that adaptive MALA outperforms non-adaptive counterparts in many interesting applications. We leave a rigorous theoretical analysis of adaptive MALA as a future direction.

# 5 Sampling from Gibbs Posteriors

Recall from Section 2.1 that a Gibbs posterior is a Bayesian pseudo-posterior defined in (2) with the criterion function $\mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } ) = - \alpha n \mathcal { R } _ { n } ( \theta )$ , where $\alpha$ is an $( n , d )$ -independent positive learning rate and $\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) : = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) } \end{array}$ is the empirical risk function induced from a loss function $\ell : \mathcal { X } \times$ $\Theta \to \mathbb { R }$ . In this section, we first provide generic conditions under which Condition A for Theorem 1 can be verified for the the Gibbs posterior so that the mixing time bound of the corresponding MALA can be applied. After that, we specialize the result to two representative cases: Gibbs posterior with a generic smooth loss function, and Gibbs posterior in Bayesian quantile regression where the check loss function is non-smooth.

Firstly, we make the following conditions on the population level risk function $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ . Recall that $\theta ^ { * } = \arg \operatorname* { m i n } _ { \theta \in \Theta } \mathcal { R } ( \theta )$ denotes the true parameter. The key idea is that although the sample level risk function (i.e. empirical risk function) $\mathcal { R } _ { n }$ is allowed to be non-smooth, but as the sample size $n$ grows, it becomes closer and closer to the population level risk function ${ \mathcal { R } } ( \theta )$ , which can be properly analyzed if smooth.

Condition B.1 (Risk function): For $( n , d )$ -independent constants $( C ^ { \prime } , C , r ) > 0$ and $( \gamma _ { 0 } , \gamma _ { 1 } , \gamma _ { 2 } ) \geq 0$

1. ${ \mathcal { R } } ( \theta )$ is twice differentiable with mixed partial derivatives of order two being uniformly bounded by $C$ on $B _ { r } ( \theta ^ { * } )$ ; for any $\theta \in \Theta$ , $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq C ^ { \prime } d ^ { - \gamma _ { 0 } } \left( d ^ { - \gamma _ { 1 } } \wedge \| \theta - \theta ^ { * } \| ^ { 2 } \right)$ .

2. Let $\mathcal { H } _ { \theta }$ denote the Hessian of $\mathcal { R }$ at $\theta$ . For any $\begin{array} { r } { \theta \in B _ { r } ( \theta ^ { * } ) , \| \mathcal { H } _ { \theta } - \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } \leq C d ^ { \gamma _ { 2 } } \| \theta - \theta ^ { * } \| . } \end{array}$

Condition B.1 imposes two requirements. Firstly, the population level risk function $\mathcal { R } ( \cdot )$ must possess a unique global minimizer $\theta ^ { * }$ . This condition ensures that when the empirical risk $\mathcal { R } _ { n }$ in the Gibbs posterior is substituted with $\mathcal { R }$ , the resulting distribution $\pi ^ { * } ( \theta ) \propto \exp ( - \alpha n \mathcal { R } ( \theta ) ) \pi ( \theta )$ will be unimodal, thereby preventing the Markov chain from getting stuck in any local mode. Note that this condition is equivalent to the identifiability of the parameter in the model, and therefore is natural to assume. Secondly, the risk function should exhibit sufficient smoothness and local strong convexity in the vicinity of $\theta ^ { * }$ . This property enables a reliable Gaussian approximation for the local shape of $\pi ^ { * } ( \theta )$ around $\theta ^ { * }$ , which is again a standard assumption and holds when the Fisher information matrix is not singular. Next, we introduce the following assumption of Lipschitz continuity for the loss function $\ell$ .

Condition B.2 (Loss function): There exist $( n , d )$ -independent constants $C > 0$ and $\gamma \geq 0$ such that for any $x \in \mathcal { X }$ and $( \theta , \theta ^ { \prime } ) \in \Theta ^ { 2 }$ , it holds that $| \ell ( x , \theta ) - \ell ( x , \theta ^ { \prime } ) | \leq C d ^ { \gamma } \| \theta - \theta ^ { \prime } \| .$ .

If the loss function has uniformly bounded derivatives with respect to $\theta$ , that is, $\begin{array} { r } { \big \vert \frac { \partial \ell ( X , \theta ) } { \partial \theta _ { j } } \big \vert \leq C } \end{array}$ holds for any $j \in [ d ]$ , $x \in \mathcal { X }$ , and $\theta \in \Theta$ , where $C$ is a constant independent of $n$ and $d$ , then Condition B.2 holds with $\begin{array} { r } { \gamma = \frac { 1 } { 2 } } \end{array}$ . Next, we introduce a function $g : \mathcal { X } \times \Theta  \mathbb { R } ^ { d }$ that satisfies the following conditions.

Condition B.3 (Subgradient of loss function): There exist some $( n , d )$ -independent constants $( C , r , \beta _ { 1 } ) >$ 0 and $( \gamma _ { 3 } , \gamma _ { 4 } ) \geq 0$ so that:

1. For any $\theta \in B _ { r } ( \theta ^ { * } )$ , it holds $\mathbb { E } [ g ( X , { \boldsymbol { \theta } } ) ] = \nabla \mathcal { R } ( { \boldsymbol { \theta } } )$ and $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { X } } \| g ( x , \theta ) \| \leq C d ^ { \gamma } } \end{array}$ , where $\gamma$ is the same as that defined in Condition B.2.

2. Let $\begin{array} { r } { d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) = \sqrt { n ^ { - 1 } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } } } \end{array}$ be a pseudo-metric in $\Theta$ .6 The logarithm of the $\varepsilon$ -covering number of $B _ { r } ( \theta ^ { * } )$ with respect to $d _ { n } ^ { g }$ is upper bounded by $C d \log ( \frac { n d } { \varepsilon } )$ .

3. For any $v \in \mathbb { S } ^ { d - 1 }$ and $\theta$ , $\theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$ , it holds that $\mathbb { E } \left[ \left( \boldsymbol { v } ^ { T } \boldsymbol { g } ( \boldsymbol { X } , \boldsymbol { \theta } ) - \boldsymbol { v } ^ { T } \boldsymbol { g } ( \boldsymbol { X } , \boldsymbol { \theta } ^ { \prime } ) \right) ^ { 2 } \right] \leq C d ^ { \gamma _ { 3 } } \left. \boldsymbol { \theta } - \mathbf { \theta } \right.$ $\theta ^ { \prime } \Vert ^ { 2 \beta _ { 1 } } a n d \mathbb { E } \big [ \big ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \big ) ^ { 2 } \big ] \leq C d ^ { \gamma _ { 3 } } \| \theta - \theta ^ { \prime } \| ^ { 2 + 2 \beta _ { 1 } }$ .

4. Let $\Delta _ { \theta ^ { * } } = \mathbb { E } [ g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } ]$ be the covariance matrix of the “score vector” $g ( X , \theta ^ { * } )$ . It holds that $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \preceq C d ^ { \gamma _ { 4 } } I _ { d }$ .

Conditions B.3.1 relaxes the pointwise differentiability requirement for the loss function $\ell ( x , \theta )$ with respect to $\theta$ . In fact, in many statistical applications, the expectation in the population-level risk function $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ has the smoothing effect of rendering $\mathcal { R }$ to be twice differentiable. For instance, we can choose $g ( x , \cdot )$ as the gradient (or any subgradient) of $\ell ( x , \cdot )$ for $x \in \mathcal { X }$ when $\ell$ is (or not) differentiable. Moreover, the boundedness assumption on the covering number in Condition B.3.2 allows us to uniformly control the random fluctuation of the empirical mean $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta )$ away from the gradient of ${ \mathcal { R } } ( \theta )$ . Condition B.3.3 can be interpreted as “smooth” assumptions on the loss function at the population level, quantified by $\beta _ { 1 }$ : by taking expectations with respect to the data $X$ , the first term controls the Lipschitz constant of $g ( X , \cdot )$ , while the second term controls the remainder term of the first-order Taylor expansion of $\ell ( X , \cdot )$ , where the gradient is replaced with $g ( X , \cdot )$ . Condition B.3.4 assumes the boundedness of the operator norm of the matrix $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ . This matrix represents the limiting covariance matrix for the sampling distribution of the empirical risk minimizer $\widehat { \theta }$ , scaled by the sample size, i.e., ${ \sqrt { n } } ( { \widehat { \theta } } - \theta )$ converges in distribution to $N _ { d } ( 0 , \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } )$ . This assumption allows us to provide an explicit bound on the deviance of $\widehat { \theta }$ , which represents the asymptotic mean of the Gibbs posterior, from $\theta ^ { * }$ . It is important to highlight that Conditions B.1-B.3 can cover the common scenario where the loss function is continuously twice differentiable (see Corollary 1). Furthermore, these conditions also apply to more general cases with non-smooth loss functions, such as quantile regression (see Corollary 2).

Additionally, we assume the following smoothness condition for the prior distribution and compactness of the parameter space.

Condition B.4 (Prior and parameter space): There exist positive $( n , d )$ -independent constants $( C , r )$ so that the parameter space √ $\Theta$ satisfies $B _ { r } ( \theta ^ { * } ) \subset \Theta \subset [ - C , C ] ^ { d }$ , and for any $\theta \in \Theta$ , $\| \nabla ( \log \pi ) ( \theta ) \| \leq$ $C \sqrt { d }$ .

The posterior density is defined to be zero for values of $\theta$ outside the parameter space $\Theta$ , ensuring that MALA rejects any proposed states that go beyond the boundaries of $\Theta$ . The assumption of compactness for the parameter space is primarily for technical convenience and is commonly made in Bayesian literature [Kleijn and van der Vaart, 2012, Yang and He, 2012]. However, it is possible to relax this requirement by assuming the exponential tail behavior of the prior distribution, which will only incur extra logarithmic terms in the final result. Finally, we made the following conditions to the preconditioning matrix $\widetilde { I }$ .

Condition C (Preconditioning matrix): There exist some $( n , d )$ -independent constants $C$ so that the preconditioning matrix $\widetilde { I }$ satisfies that

$$
\begin{array} { r l } { I . } & { \| \widetilde { I } ^ { - 1 } \| _ { \mathrm { o p } } \| \widetilde { I } \| _ { \mathrm { o p } } \leq C \| \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } \| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } } ; } \\ { 2 . } & { \| \widetilde { I } \| _ { \mathrm { o p } } \| ( \widetilde { I } ^ { \frac { 1 } { 2 } } H _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } ) ^ { - 1 } \| _ { \mathrm { o p } } \leq C \| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } } . } \end{array}
$$

The requirement for the preconditioning matrix $\widetilde { I }$ holds when $\widetilde { I }$ and its inverse has constant-order eigenvalues, such as the identity matrix that is conventionally used in MALA. On the other hand, it can also cover the case when $\widetilde { I }$ acts as a reasonable estimator to $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ (i.e, $\widetilde { I } ^ { 1 / 2 } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { 1 / 2 }$ and its inverse has constant-order eigenvalues).

We now state the following theorem that provides a mixing time bound for sampling from a Gibbs posterior using MALA. Note that the (sub)gradient $g$ is used for constructing the proposal in each step MALA.

Theorem 2 (Complexity of MALA for Bayesian sampling). Consider sampling from the Bayesian Gibbs posteriors where $\mathcal { C } _ { n } ( \theta ; X ^ { ( n ) } ) = - n \alpha \mathcal { R } _ { n } ( \theta )$ . Under Conditions B.1-B.4 and Condition $C _ { i }$ , consider positive numbers $\rho _ { 1 } , \rho _ { 2 }$ , warming parameter $M _ { 0 }$ and tolerance ε satisfying $( I ) \rho _ { 1 } I _ { d } \preceq \widetilde { I } ^ { 1 / 2 } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { 1 / 2 } \preceq$ $\rho _ { 2 } I _ { d }$ ; (2)tant $\begin{array} { r } { \log ( \frac { M _ { 0 } } { \varepsilon } ) \leq C _ { 1 } \left( d ^ { \gamma _ { 5 } } + \log n \right) } \end{array}$ $( n , d )$ dependenso that if $C _ { 1 }$ $\gamma _ { 5 } \geq 1$ . There existsugh constant $a$ $\kappa _ { 1 }$ $( \beta _ { 1 } , \gamma , \gamma _ { 0 } , \gamma _ { 1 } , \cdot \cdot \cdot , \gamma _ { 5 } )$ $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 1 } } } { \log n } } \end{array}$ $c$ then with probability at least $1 - n ^ { - 1 }$ , the mixing time bound (7) in Theorem $I$ holds for

$$
h = c _ { 0 } \cdot \bigg [ \rho _ { 2 } \Big ( d ^ { \frac { 1 } { 3 } } + d ^ { \frac { 1 } { 4 } } \big ( \log \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) ^ { \frac { 1 } { 4 } } + \big ( \log \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) ^ { \frac { 1 } { 2 } } \Big ) \bigg ] ^ { - 1 } , w h e r e \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } ,
$$

where $c _ { 0 }$ is an $( n , d )$ -independent constant.

Remark 1. Theorem 2 is proved by verifying Condition A for Bayesian Gibbs posteriors. The parameter $\kappa _ { 1 }$ sets an upper bound on how the dimensionality of the parameter space $d$ can grow in relation to the sample size $n$ . A smaller $\kappa _ { 1 }$ value implies that a larger dataset is necessary for the target posterior to be well-approximated by a Gaussian distribution. The expression for $\kappa _ { 1 }$ is given by:

$$
\begin{array} { l } { \kappa _ { 1 } = \displaystyle \frac { 1 } { 1 + 2 \gamma + 6 \gamma _ { 0 } + 4 \gamma _ { 2 } + \gamma _ { 4 } } \wedge \displaystyle \frac { \beta _ { 1 } } { 1 + \gamma _ { 3 } + [ ( 2 \gamma _ { 0 } ) \vee ( ( \gamma _ { 5 } + \gamma _ { 0 } ) ( 1 + \beta _ { 1 } ) ) ] } \wedge \displaystyle \frac { 1 } { \gamma _ { 0 } + \gamma _ { 1 } + \gamma _ { 5 } } } \\ { \wedge \displaystyle \frac { 1 } { 2 \gamma + 2 \gamma _ { 0 } + 2 \gamma _ { 1 } + [ 2 \vee ( 1 + \gamma _ { 4 } ) ] } \wedge \displaystyle \frac { 1 } { 3 \gamma _ { 5 } + \gamma _ { 0 } + [ ( 2 \gamma ) \vee ( \gamma _ { 4 } + 2 \gamma _ { 2 } + \gamma _ { 0 } ) \vee ( 2 \gamma _ { 2 } + 2 \gamma _ { 0 } ) ] } . } \end{array}
$$

From the expression, $\kappa _ { 1 }$ tends to be smaller if the loss function exhibits low smoothness, that means, $\beta _ { 1 }$ is small. The classical proof of the Gaussian approximation of Bayesian posteriors with smooth likelihoods is based on the Taylor expansion of the likelihood function around $\widehat { \theta }$ [e.g. see Ghosh and Ramamoorthi, 2003]. For the general non-smooth cases, we instead apply the Taylor expansion to the population level risk function $\mathcal { R }$ and use chaining and localization techniques in the empirical process theory to relate it to the sample version. Moreover, we keep track of the parameter dimension dependence, making Theorem 2 adaptable to more general cases under increasing dimension.

# 5.1 Gibbs posterior with smooth loss function

One representative example of Gibbs posterior satisfying Conditions B.1-B.4 is the one equipped with a smooth loss function. More specifically, we need Condition B.1 for the local convexity of the risk function, Condition B.4 for the smoothness of the prior and the following smoothness condition to the loss function.

Condition B.3’ (Smoothness of loss function):There exist some $( n , d )$ -independent constants $C > 0$ and $( \gamma , \gamma _ { 2 } , \gamma _ { 3 } , \gamma _ { 4 } ) \ge 0$ so that $( l )$ the loss function is twice differentiable so that for any $x \in \mathcal { X }$ and $\theta \in \Theta$ , $\| \nabla _ { \theta } \ell ( x , \theta ) \| \le C d ^ { \gamma }$ ; $\| \mathrm { H e s s } _ { \theta } ( \ell ( x , \bar { \theta } ) ) \| _ { \mathrm { o p } } ^ { 2 } \leq C d ^ { \gamma _ { 3 } } ;$ and for any $\theta , \theta ^ { \prime } \in \Theta$ , $\| \mathrm { H e s s } _ { \theta } ( \ell ( x , \theta ) ) -$ $\mathrm { H e s s } _ { \theta } ( \ell ( x , \theta ^ { \prime } ) ) \| _ { \mathrm { o p } } \leq C d ^ { \gamma _ { 2 } } \| \theta - \theta ^ { \prime } \|$ ; (2) let $\Delta _ { \theta ^ { * } } = \mathbb { E } [ \nabla _ { \theta } \ell ( X , \theta ^ { * } ) \nabla _ { \theta } \ell ( X , \theta ^ { * } ) ^ { T } ] ,$ , then $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \preceq$ $C d ^ { \gamma _ { 4 } } I _ { d }$ .

Corollary 1 (Sampling from smooth posteriors). Consider the Bayesian Gibbs posterior with loss function $\ell .$ . Suppose $( l )$ Conditions B.1, $B . 3 ^ { \prime }$ and B.4 hold; (2) the warming parameter $M _ { 0 }$ and tolerance $\varepsilon$ satisfying $\begin{array} { r } { \log ( \frac { M _ { 0 } } { \varepsilon } ) \leq C _ { 1 } \left( d ^ { \gamma _ { 5 } } + \log n \right) f o r \left( n , d \right) } \end{array}$ -independent constants $C _ { 1 }$ and $\gamma _ { 5 } \geq 1$ ; (3) $\begin{array} { r } { d \le c \frac { n ^ { \kappa _ { 1 } } } { \log n } } \end{array}$ for a small enough constant $c$ , where $\kappa _ { 1 }$ is defined in (8) with $\beta _ { 1 } = 1$ . Then there exists an $( n , \breve { d } )$ - independent constant $c _ { 0 }$ so that it holds with probability at least $1 - n ^ { - 1 }$ that

1. consider the identity preconditioning matrix $\widetilde { I } = I _ { d }$ . the mixing time upper bound (7) holds for any $\rho _ { 1 } \le \rho _ { 2 }$ so that $\rho _ { 1 } I _ { d } \preceq \mathcal { H } _ { \theta ^ { * } } \preceq \rho _ { 2 } I _ { d } , \log ( \frac { \rho _ { 1 } } { \rho _ { 2 } } ) \leq C _ { 1 } d ^ { \gamma _ { 5 } }$ and

$$
h = c _ { 0 } \cdot \bigg [ \rho _ { 2 } \cdot \Big ( d ^ { \frac { 1 } { 3 } } + d ^ { \frac { 1 } { 4 } } \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 4 } } + \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 2 } } \Big ) \bigg ] ^ { - 1 } ;
$$

2. consider the inverse empirical Hessian matrix $\begin{array} { r } { \widetilde { I } = \left( | S | ^ { - 1 } \sum _ { i \in S } \mathrm { H e s s } _ { \theta } \big ( \ell ( X _ { i } , \widehat { \theta } ) \big ) \right) ^ { - 1 } } \end{array}$ , where $S \subset$ $\{ 1 , 2 , \cdots , n \}$ with $| S | \ge C _ { 2 } d ^ { \gamma _ { 3 } + 2 \gamma _ { 0 } + 7 / 3 }$ for a large enough $( n , d )$ -independent constant $C _ { 2 }$ , then the mixing time upper bound (7) holds with $\rho _ { 1 } = { \textstyle { \frac { 1 } { 2 } } }$ and

$$
h = c _ { 0 } \cdot \bigg [ \Big ( d ^ { \frac { 1 } { 3 } } + d ^ { \frac 1 4 } \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 4 } } + \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 2 } } \Big ) \bigg ] ^ { - 1 } ;
$$

moreover, let $\mu _ { 0 } = \left. N _ { d } ( { \widehat { \theta } } , n ^ { - 1 } { \widetilde { I } } ) \right| _ { \{ \theta : { \sqrt { n } } { \widetilde { I } } ^ { - { \frac { 1 } { 2 } } } ( \theta - { \widehat { \theta } } ) \| \leq 3 c _ { 1 } { \sqrt { d } } \} }$ , where $c _ { 1 }$ is a constant so that $c _ { 1 } \geq$ $\displaystyle 3 \vee \operatorname* { s u p } _ { i \in [ d ] , j \in [ d ] } \frac { \partial ^ { 2 } \mathcal { R } ( \theta ^ { * } ) } { \partial \theta _ { i } \partial \theta _ { j } }$ , then $\mu _ { 0 }$ is $M _ { 0 }$ -warm with respect to $\pi _ { n }$ with $\log M _ { 0 } \leq d ^ { \frac { 1 } { 3 } }$ .

When the Hessian matrix $\mathcal { H } _ { \theta ^ { \ast } }$ is ill-conditioned, introducing the preconditioning matrix $\widetilde { I } = \left( \vert S \vert ^ { - 1 } \right.$ $\begin{array} { r l } { \sum _ { i \in S } \operatorname { H e s s } _ { \boldsymbol { \theta } } ( \ell ( X _ { i } , \widehat { \boldsymbol { \theta } } ) ) \big ) ^ { - 1 } } & { { } } \end{array}$ may lead to a faster mixing. Furthermore, if the tolerance satisfying $\begin{array} { r } { \log ( \frac { 1 } { \varepsilon } ) = } \end{array}$ $O ( d ^ { \frac { 1 } { 3 } } )$ , then the second statement of Corollary 1 can lead to an optimal mixing time bound $\mathcal { O } \big ( d ^ { \frac { 1 } { 3 } } \log ( \frac { 1 } { \varepsilon } ) \big )$

# 5.2 Bayesian quantile regression

We consider Bayesian quantile regression as a representative example where the loss function is nonsmooth. Specifically, in quantile regression [Koenker and Bassett, 1978], for a fixed $\tau \in ( 0 , 1 )$ , the $\tau ^ { t h }$ quantile $q _ { \tau } ( Y | \widetilde { X } )$ of the response $Y \in \mathbb { R }$ given the covariates $\widetilde X \in \mathbb R ^ { d }$ is modelled as $q _ { \tau } ( Y | \widetilde { X } ) = \widetilde { X } ^ { T } \theta ^ { * }$ . Here we consider the homogeneous case where the error $e = Y - \widetilde { X } ^ { T } \theta ^ { \ast }$ is independent of the covariates $\widetilde { X }$ . Given a set of $n$ i.i.d. samples $X ^ { ( n ) } = \{ X _ { i } = ( \widetilde { X } _ { i } , Y _ { i } ) \} _ { i \in [ n ] }$ , the quantile regression solves the following convex optimization problem:

$$
\widehat { \theta } = \arg \operatorname* { m i n } _ { \theta \in \Theta } \sum _ { i = 1 } ^ { n } \Big [ ( Y _ { i } - \widetilde { X } _ { i } ^ { T } \theta ) \cdot \big ( \tau - \mathbf { 1 } ( Y _ { i } < \widetilde { X } _ { i } ^ { T } \theta ) \big ) \Big ] ,
$$

where the loss function $\ell _ { q } \big ( ( \widetilde { X } , Y ) , \theta \big ) = ( Y - \widetilde { X } ^ { T } \theta ) \cdot \big ( \tau - \mathbf { 1 } ( Y < \widetilde { X } ^ { T } \theta ) \big )$ is referred to as the check loss. The minimization of the check loss function is equivalent to the maximization of a likelihood function formed by combining independently distributed asymmetric Laplace densities [Yu and Moyeed, 2001]. The posterior for Bayesian quantile regression can thus be formed by assuming a (possibly misspecified) asymmetric Laplace distribution (ALD) for the response, which is

$$
\begin{array} { r } { \pi _ { n } ( \theta ) \propto \exp \big ( - n \mathcal { R } _ { n } ( \theta ) \big ) \pi ( \theta ) , \quad \theta \in \mathbb { R } ^ { d } , } \end{array}
$$

with $\pi ( \theta )$ being a prior on $\Theta$ and $\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell _ { q } ( X _ { i } , \theta ) } \end{array}$ being the empirical risk function. Furthermore, by adding a multiplier $\alpha > 0$ to the likelihood, we can obtain the Gibbs (or tempered) posterior.

Since the loss function $\ell _ { q } ( X , \theta )$ for quantile regression is not differentiable when $Y = \widetilde { X } ^ { T } \theta$ , in order to sampling from the Gibbs posterior associated with Bayesian quantile regression using the (preconditioned) MALA, we need to consider the subgradient of $\ell _ { q }$ with respect to $\theta$ , given by

$$
g ( X , \theta ) = \left( \mathbf { 1 } ( Y < \widetilde { X } ^ { T } \theta ) - \tau \right) \widetilde { X } , \quad X = ( \widetilde { X } , Y ) , \ \theta \in \mathbb { R } ^ { d } .
$$

The following corollary quantifies the computational complexity for sampling from $\pi _ { n }$ using MALA.   
We first state the required conditions.

Condition D.1: There exist $( n , d )$ -independent constants $( C , C ^ { \prime } ) > 0$ and $\left( \alpha _ { 0 } , \alpha _ { 1 } \right) \geq 0$ such that $( l )$ the support $\mathcal { X }$ of the covariates $\ddot { X }$ is included in $[ - C , C ] ^ { d }$ ; (2) for any $v \in \mathbb { S } ^ { d - 1 }$ , $\mathbb { E } | \widetilde { X } ^ { T } v | ^ { 2 } \geq C ^ { \prime } d ^ { - \alpha _ { 0 } }$ and $\mathbb { E } | \widetilde { X } ^ { T } v | ^ { 3 } \le C d ^ { \alpha _ { 1 } }$ .

Condition D.2: Let $f _ { e } ( \cdot )$ denote the probability density function of the homogeneous error $e = Y -$ $\widetilde { X } ^ { T } \theta ^ { \ast }$ , then there exist $( n , d )$ -independent constants $( C , C ^ { \prime } ) > 0$ such that $( l )$ $\begin{array} { r } { \int _ { - \infty } ^ { 0 } f _ { e } ( z ) d z = \tau , } \end{array}$ ; (2) $f _ { e } ( 0 ) > C ^ { \prime }$ and $\operatorname { S u p } _ { e \in \mathbb { R } ^ { d } }$ $f _ { e } ( e ) \leq C$ ; (3) for any $e _ { 1 } , e _ { 2 } \in \mathbb { R } ,$ , $| f _ { e } ( e _ { 1 } ) - f _ { e } ( e _ { 2 } ) | \leq C | e _ { 1 } - e _ { 2 } |$ .

Condition D.1 assumes the compactness of the covariate space and the positive definiteness of the gram matrix $\mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ]$ . Condition D.2 introduces several regularity conditions on the distribution of the error $e \ = \ Y \bar { - } \ \tilde { X } ^ { T } \bar { \theta } ^ { * }$ : (1) The error term $e$ is independent of the covariates. (2) The model is correctly specified, meaning that $\widetilde { X } ^ { T } \theta ^ { \ast }$ corresponds to the $\tau$ -th quantile of the response variable $Y$ given $\widetilde { X }$ . (3) The density function $f _ { e } ( \cdot )$ of the error term is positive at the origin and Lipschitz continuous. Under the assumption of homogeneous errors, the limiting covariance matrix of the posterior distribution of interest is given by $n ^ { - 1 } ( f _ { e } ( \bar { 0 } ) \cdot \mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] ) ^ { - 1 }$ . In this case, a natural choice for the preconditioning matrix is the inverse of the empirical Gram matrix, denoted as $\begin{array} { r } { \widetilde { I } = \big ( | S | ^ { - 1 } \sum _ { i \in S } \widetilde { X } _ { i } \widetilde { X } _ { i } ^ { T } \big ) ^ { - 1 } } \end{array}$ where $S \subset \{ 1 , 2 , \cdots , n \}$ . It is worth noting that similar analyses can be carried out for the case of heterogeneous errors, but the limiting covariance matrix will be more complex.

Corollary 2 (Sampling from non-smooth posteriors). Suppose Conditions $D . l , D . 2 ,$ , and $B . 4$ are satisfied, and the warmingindependent constants rameand $M _ { 0 }$ nd tolera. Assume $\varepsilon$ $\begin{array} { r } { \log ( \frac { M _ { 0 } } { \varepsilon } ) \leq C _ { 1 } \left( d ^ { \alpha _ { 2 } } + \log n \right) f o r \left( n , d \right) . } \end{array}$ $C _ { 1 }$ $\alpha _ { 2 } \geq 1$ $\begin{array} { r } { d \leq c ( \frac { n ^ { \widetilde { \alpha } } } { \log n } ) } \end{array}$ $\begin{array} { r } { \widetilde { \alpha } = \frac { 1 } { 2 + 4 \alpha _ { 1 } + 7 \alpha _ { 0 } } \wedge \frac { 1 } { 2 + 3 \alpha _ { 0 } + 2 \alpha _ { 1 } + 3 \alpha _ { 2 } } } \end{array}$ and a small enough constant c, and let the inverse empirical Gram matrix $\begin{array} { r } { \widetilde { I } = \left( | S | ^ { - 1 } \sum _ { i \in S } \widetilde { X } _ { i } \widetilde { X } _ { i } ^ { T } \right) ^ { - 1 } } \end{array}$ be the preconditioning matrix, where $S \subset \{ 1 , 2 , \cdots , n \}$ with $| S | \geq C _ { 2 } d ^ { \alpha _ { 1 } + 2 \alpha _ { 0 } + 3 / 2 } \log n$ for a large enough $( n , d )$ -independent constant $C _ { 2 }$ , then it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n } }$ that that the mixing time upper bound (7) is true with $\rho _ { 1 } = \frac { 1 } { 2 } f _ { e } ( 0 )$ and

$$
h = c _ { 0 } \cdot \left[ f _ { e } ( 0 ) \cdot \Big ( d ^ { \frac { 1 } { 3 } } + d ^ { \frac { 1 } { 4 } } \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 4 } } + \big ( \log \frac { M _ { 0 } d } { \varepsilon } \big ) ^ { \frac { 1 } { 2 } } \Big ) \right] ^ { - 1 }
$$

with $c _ { 0 }$ being an $( n , d )$ -independent constant.

Corollary 2 illustrates the implications of applying our theory to non-smooth posteriors. A key observation is that in the large-sample regime, although the potential function associated with the Bayesian posterior may be non-smooth, its population-level counterpart is smooth (as per Condition B.3). This allows MALA, using sub-gradients, to effectively sample from non-smooth posteriors. Moreover, while our theory is applicable to non-smooth posteriors, the smoothness of the posterior density function influences its convergence to a Gaussian limit as $n$ grows, as captured by the parameter $\beta _ { 1 }$ in Condition B.3. A posterior with higher smoothness (or larger $\beta _ { 1 . }$ ) will converge more rapidly to a Gaussian distribution, as demonstrated in Lemma 10, which in turn leads to an improved (higher) acceptance rate of MALA. For example, in Bayesian quantile regression, the smoothness parameter $\beta _ { 1 }$ is at most $\frac { 1 } { 2 }$ . In contrast, for posterior densities with smooth loss functions, $\beta _ { 1 }$ can be taken as 1. Interestingly, our theoretical result also leads a practical guideline: when applying MALA to sample from a less smooth Bayesian posterior densities, a relatively larger sample size $n$ is needed to maintain the sampling efficiency. Otherwise, if $n$ is not sufficiently large relative to the dimension, the non-smoothness of the Bayesian posterior can result in a lower acceptance rate and slower mixing times for MALA; see our simulation results in Section 7 for some empirical evidence.

# 6 Proof Sketch of Theorem 1

In this section, we provide a sketched proof about how to utilize the general machinery of $s$ -conductance profile developed in Section 3 to analyze the mixing time of MALA under Condition A. We consider the identity preconditioning matrix (i.e. $\widetilde { I } = I _ { d } )$ in this sketch for simplicity, and the case for general preconditioning matrix can be proved by considering the transformation $\dot { G ( \theta ) } = \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \overline { { \theta } } )$ , see Appendix B.1 for further details.

Let $T _ { x } ^ { \zeta } ( \mathrm { d } y ) = T ^ { \zeta } ( x , \mathrm { d } y )$ denote the Markov transition kernel of the $\zeta$ -lazy version of MALA for sampling from $\pi _ { \mathrm { l o c } }$ as described in Section 4 with rescaled step size $h$ . To apply Lemma 1, we first need to establish a log-isoperimetric inequality, which is a property of $\pi _ { \mathrm { l o c } }$ alone and is not specific to MALA. This step can be done by adapting existing proofs of a log-isoperimetric inequality for Gaussians (e.g. Lemma 16 of Chen et al. [2020]) to $\pi _ { \mathrm { l o c } }$ via a perturbation analysis (see Lemma 6 and its proof in the appendix for details). Second, we need to apply an overlap argument for bounding the total variation distance between $T _ { x } ^ { \zeta } ( \cdot )$ and $T _ { z } ^ { \zeta } ( \cdot )$ for $x$ and $z$ satisfying $\| x - z \| \leq C { \sqrt { h } }$ and belonging to a high probability set $E$ under $\pi _ { \mathrm { l o c } }$ . This step utilizes the structure and properties of MALA algorithm, and we briefly sketch its proof below (details can be found in Lemma 7 in the appendix) and discuss its difference from existing proofs.

We construct a high probability set as $E = \{ \xi \in B _ { R / 2 } ^ { d } : | \xi ^ { T } \widetilde { J } ^ { 3 } \xi - \mathrm { t r } ( \widetilde { J } ^ { 2 } ) | \leq r _ { d } \} \cap \{ \xi \in B _ { R / 2 } ^ { d } :$ $\begin{array} { r } { \left| \xi ^ { T } \widetilde { J } ^ { 2 } \xi - \mathrm { t r } ( \widetilde { J } ) \right| \le r _ { d } / \rho _ { 2 } \} } \end{array}$ , where the value of $r _ { d }$ makes $\pi _ { \mathrm { l o c } } ( E ) \geq 1 - 2 \frac { h \rho _ { 1 } \varepsilon ^ { 2 } } { M _ { 0 } ^ { 2 } }$ based on the last property of Condition A (details can be found in Lemma 13). Recall the acceptance probability $A ( x , y ) = 1 \land$ $\frac { \pi _ { \mathrm { l o c } } ( y ) Q ( y , x ) } { \pi _ { \mathrm { l o c } } ( x ) Q ( x , y ) }$ and denotes $\begin{array} { r } { \overline { { A } } ( x , y ) = 1 \wedge \frac { \overline { \pi } ( y ) Q ( y , x ) } { \overline { \pi } ( x ) Q ( x , y ) } } \end{array}$ with $\overline { { \pi } }$ being the density of the Gaussian $N _ { d } ( 0 , J ^ { - 1 } )$ . By comparing $\pi _ { \mathrm { l o c } }$ and $\overline { { \pi } }$ using Condition A, we can get the following inequality:

$$
\begin{array} { r l } & { \displaystyle | T _ { \mathcal { L } } ^ { \zeta } - T _ { \mathcal { L } } ^ { \zeta } | | _ { T V } \leq 1 - ( 1 - \zeta ) \int _ { B _ { R } ^ { d } } \operatorname* { m i n } \Big ( A ( x , y ) Q ( x , y ) , A ( z , y ) Q ( z , y ) \Big ) \mathrm { d } y } \\ & { \leq 1 - \displaystyle \frac { 1 } { 2 } ( 1 - \zeta ) \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \left( \int _ { B _ { R } ^ { d } } \overline { { A } } ( x , y ) Q ( x , y ) \mathrm { d } y + \int _ { B _ { R } ^ { d } } \overline { { A } } ( z , y ) Q ( z , y ) \mathrm { d } y \right. } \\ & { \qquad \left. - \int _ { B _ { R } ^ { d } } | \overline { { A } } ( x , y ) Q ( x , y ) - \overline { { A } } ( z , y ) Q ( z , y ) | \mathrm { d } y \right) } \\ & { \leq 1 - ( 1 - \zeta ) \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \Big ( 1 - \int _ { B _ { R } ^ { d } } Q ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y - \int _ { B _ { R } ^ { d } } Q ( z , y ) ( 1 - \overline { { A } } ( z , y ) ) \mathrm { d } y } \\ & { \qquad - \| Q _ { x } - Q _ { z } \| _ { \mathbb { T } V } - \frac { 1 } { 2 } \int _ { ( B _ { R } ^ { d } ) ^ { \zeta } } Q ( x , y ) \mathrm { d } y - \frac { 1 } { 2 } \int _ { ( B _ { R } ^ { d } ) ^ { \zeta } } Q ( z , y ) \mathrm { d } y \Big ) . } \end{array}
$$

We will separately bound the terms on the right hand side of (9) as follows. The last term $\begin{array} { r l } { \frac { 1 } { 2 } \int _ { ( B _ { R } ^ { d } ) ^ { c } } Q ( x , y ) \mathrm { d } y + } \end{array}$

$\begin{array} { r l } {  { \frac { 1 } { 2 } \int _ { ( B _ { R } ^ { d } ) ^ { c } } Q ( z , y ) \mathrm { d } } \quad } & { { } } \end{array}$ y can be upper bounded by $\frac { 1 } { 6 }$ using the condition of $R$ in Condition A. For the remaining terms, let $Q _ { x }$ denote the probability measure with density function $Q ( x , \cdot )$ , now we use Condition A by comparing $Q _ { x }$ with the proposal distribution

$$
Q _ { x } ^ { \Delta } : = N _ { d } ( x - h J x , 2 h I _ { d } )
$$

of MALA for sampling from the Gaussian $N _ { d } ( 0 , J ^ { - 1 } )$ , leading to

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { R } ^ { d } } Q ( x , y ) \left( 1 - \overline { { A } } ( x , y ) \right) \mathrm { d } y \leq 2 \| Q _ { x } - Q _ { x } ^ { \Delta } \| _ { \mathrm { T V } } + \int _ { \mathbb { R } ^ { d } } \left| Q ^ { \Delta } ( x , y ) - \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) } \right| \mathrm { d } y } \\ & { \quad \quad \quad \quad \quad + \int _ { B _ { R } ^ { d } } \Big | \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) } - \frac { \overline { { \pi } } ( y ) Q ( y , x ) } { \overline { { \pi } } ( x ) ( x ) } \Big | \mathrm { d } y , } \end{array}
$$

where we use $Q ^ { \Delta } ( x , \cdot )$ to denote the density function of $Q _ { x } ^ { \Delta }$ . It then can be proved using Condition A and Pinsker’s inequality after some careful calculations (see Lemmas 14 and 15 in the appendix) that

$$
\int _ { B _ { R } ^ { d } } Q ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y + \int _ { B _ { R } ^ { d } } Q ( z , y ) ( 1 - \overline { { A } } ( z , y ) ) \mathrm { d } y + \| Q _ { x } - Q _ { z } \| _ { \mathrm { T V } } \leq 1 / 3 .
$$

Our proof of Lemma 14 for bounding $\begin{array} { r } { \int _ { \mathbb { R } ^ { d } } \left| Q ^ { \Delta } ( x , y ) - \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) / \overline { { \pi } } ( x ) \right| \mathrm { d } y } \end{array}$ is technically similar to that of Proposition 38 in Chewi et al. [2021] for bounding the mixing time of MALA with a standard Gaussian target (i.e. $\overline { { \pi } } = N _ { d } ( 0 , I _ { d } ) )$ . The non-trivial part in our analysis lies in keeping track of the dependence on the maximal and minimal eigenvalues of $J$ . Finally, we can obtain

$$
\| T _ { x } ^ { \zeta } - T _ { z } ^ { \zeta } \| _ { T V } \leq 1 - \frac { 1 - \zeta } { 2 } \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) .
$$

With the lower bound on $\pi _ { \mathrm { l o c } } ( E )$ and the upper bound on $\Vert T _ { x } ^ { \zeta } - T _ { z } ^ { \zeta } \Vert _ { T V }$ , we are then able to apply the $s$ -conductance profile argument to control the mixing time.

Remark 2. It is worth mentioning that the analysis in Chen et al. [2020] requires the high probability set, which is set $E$ in our case, to be convex. This requirement will deteriorate the d dependence of the mixing time bound since $\| T _ { x } ^ { \zeta } - T _ { z } ^ { \zeta } \| _ { \mathrm { T V } } f o r x , z \in E$ can no longer be controlled under a large step size h as ours. This motivates us to introduce the more flexible notion of $s$ -conductance profile that extends the commonly used conductance profile [Goel et al., 2006, Chen et al., 2020] and $s$ -conductance [Lovasz ´ and Simonovits, 1993]. Analysis based on the s-conductance profile leads to a better warming parameter dependence than that obtained in Chewi et al. [2021], Belloni and Chernozhukov [2009] without affecting our obtained dimension dependence (based on s-conductance). A complete proof of this theorem is included in Appendix B.1. Similar analysis can also be carried over for analyzing general smooth and strictly log-concave densities to improve the warming parameter dependence [e.g. Chewi et al., 2021, Belloni and Chernozhukov, 2009].

# 7 Numerical Study

In this section, we conduct an empirical study to explore how the performance of MALA varies across different dimensions and sample sizes when targeting different Bayesian posteriors.

# 7.1 Set up

We carry out the experiment using two examples: Bayesian linear regression and Bayesian median regression. For Bayesian linear regression, the corresponding Bayesian posterior is given by:

$$
\pi _ { n } ^ { \mathrm { m e a n } } ( \theta | X ^ { ( n ) } ) \propto \exp \Big ( - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \big \| Y _ { i } - \widetilde { X } _ { i } ^ { T } \theta \big \| ^ { 2 } \Big ) \pi ( \theta ) , \ \theta \in \mathbb { R } ^ { d } .
$$

For Bayesian median regression, the Bayesian posterior is given by

$$
\pi _ { n } ^ { \mathrm { m e d } } ( \theta | X ^ { ( n ) } ) \propto \exp \Big ( - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \big | Y _ { i } - \widetilde { X } _ { i } ^ { T } \theta \big | \Big ) \pi ( \theta ) , \ \theta \in \mathbb { R } ^ { d } .
$$

We choose the parameter dimension $d$ from the set $\{ 1 5 , 2 0 , 3 0 , 4 0 , \cdots , 1 0 0 \}$ and sample size $n$ from $\{ 5 0 0 , 1 0 0 0 , 2 0 0 0 , 5 0 0 0 , 5 0 0 ( d / 1 5 ) , 5 0 0 ( d / 1 5 ) ^ { 3 / 2 } , 5 0 0 ( d / 1 5 ) ^ { 2 } \}$ . The covariates $\widetilde { X }$ are generated from a multivariate Gaussian distribution with zero mean and identity covariance matrix. For Bayesian linear regression, we generate a random error variable $e$ follows a standard normal distribution, and for Bayesian median regression, $e$ follows a Laplace distribution with location parameter $\mu = 0$ and scale parameter $b = 2$ . The response variable $Y$ is given by $Y = \widetilde { X } ^ { T } \theta ^ { \ast } + e$ with $\theta ^ { * } = ( 1 , 1 , \cdots , 1 )$ . We consider the parameter space $\Theta = [ - 1 0 0 , 1 0 0 ] ^ { d }$ and the prior is chosen to be a uniform distribution over $\Theta$ . We then use MALA to sample from the Bayesian posterior $\pi _ { n } ^ { \mathrm { m e a n } }$ and $\pi _ { n } ^ { \mathrm { m e d } }$ .

# 7.2 Results

In general, estimating the mixing time of a Markov chain is a challenging task. Instead, we utilize the effective sample size [Gelman et al., 1995] as a metric to assess the mixing of MALA. The effective sample size of $N$ Markov samples, denoted as $N _ { \mathrm { e f f } }$ , quantifies the amount of information lost due to correlations in the chain, and plays a role similar to the number of independent draws in the standard central limit theorem [Brooks et al., 2011]. The effective sample size of a sequence is formally defined in terms of the autocorrelations within the sequence at different lags, i.e., $\begin{array} { r } { N _ { \mathrm { e f f } } \stackrel { \mathrm { ^ { - } } } { = } \frac { N } { 1 + 2 \sum _ { t = 1 } ^ { \infty } \rho _ { t } } } \end{array}$ , with $\rho _ { t }$ being can be found in Section 11.5 of Gelman et al. [2013]. It is worth noting that, theoretically, the ratio $\frac { N } { N _ { \mathrm { e f f } } }$ can be controlled by the inverse of the spectral gap [Kloeckner, 2019], which governs the convergence of the Markov chain.

Taking into account our theoretical findings regarding the convergence of MALA with an appropriate warm start, we compute the effective sample sizes after a burn-in period of 1000 iterations, totaling 5000 iterations. We choose the step size $\stackrel { \sim } { h } = \stackrel { \sim } { c } _ { 1 } d ^ { - \frac { 1 } { 3 } } n ^ { - 1 }$ , where $c _ { 1 } = 4 . 2 8$ for Bayesian median regression and $c _ { 1 } = 1 . 3 9$ for Bayesian linear regression. These choices of $c _ { 1 }$ ensure that the overall acceptance probability in each example closely approximates 0.574 as suggested by Roberts and Rosenthal [1998]. The preconditioning matrix $\widetilde { I }$ is chosen to be the identity matrix.

Figure 1 present the trends of the average acceptance probability and the logarithm of the effective sample size when sampling from $\pi _ { n } ^ { \mathrm { m e d } }$ and $\pi _ { n } ^ { \mathrm { m e a n } }$ , considering varying sample sizes and dimensions. When $n$ remains unchanged for varying $d$ , we observe a decrease in the acceptance probability as $d$ grows larger in both cases. Additionally, the trends of the logarithmic effective sample size exhibit slopes smaller than $- \frac { 1 } { 3 }$ . The reason for this phenomenon is that, the deviance $\widetilde { \varepsilon } _ { 0 }$ of the target posterior from the Gaussian distribution, stated in Theorem 1, will increase with $d$ when the sample size remains unchanged. Consequently, when $d$ is sufficiently large, the mixing time will deviate significantly from $\mathcal { O } ( d ^ { \frac { 1 } { 3 } } )$ and the acceptance probability will decrease rapidly when employing a step size of order $d ^ { - \frac { 1 } { 3 } } n ^ { - 1 }$ . Another interesting observation is that the decreases in acceptance probability and effective sample size are much slower when sampling from $\pi _ { n } ^ { \mathrm { m e a n } }$ compared to sampling from $\pi _ { n } ^ { \mathrm { m e d } }$ One factor results in this phenomenon can be the smoothness of the loss function used in $\pi _ { n } ^ { \mathrm { m e a n } }$ , which aids the convergence of the Gibbs posterior to the Gaussian distribution. Specifically, Lemma 10 in Appendix B.3 demonstrates that a Gibbs posterior with a smooth loss function will converge to a Gaussian distribution with a rate of $\mathcal { O } ( n ^ { - 1 / 2 } )$ for a fixed $d$ , while the Gibbs posterior used in Bayesian quantile regression approaches a Gaussian distribution at a rate of $\mathcal { O } ( n ^ { - 1 / 4 } )$ . Therefore, under the same $n$ and $d$ , the approximation error $\widetilde { \varepsilon } _ { 0 }$ for $\pi _ { n } ^ { \mathrm { m e a n } }$ is much smaller than $\pi _ { n } ^ { \mathrm { m e d } }$ . Additionally, we can see from Figure 1 that, for achieving a constant acceptance probability and effective sample size at an order of $d ^ { - \frac { 1 } { 3 } }$ when $d$ ranges from 15 to 100, the condition $d = \mathcal { O } ( \sqrt { n } )$ is required for sampling from $\pi _ { n } ^ { \mathrm { m e d } }$ , while the condition $d = \mathcal { O } ( n )$ suffices for sampling from $\pi _ { n } ^ { \mathrm { m e a n } }$ .

![](images/368f68ecb8dfa37e99594a4baaecd26fc1de12f917bb6da90b5477c77976a6d7.jpg)  
Figure 1: Plots (a) and (c) report the average acceptance probabilities of MALA when sampling from the posterior in Bayesian quantile regression (denoted as $\pi _ { n } ^ { \mathrm { m e d } }$ ) and Bayesian linear regression (denoted as $\pi _ { n } ^ { \mathrm { m e a n } } ,$ ) respectively, across various sample sizes $( n )$ and dimensions $( d )$ , with the step size $\widetilde { h } = c d ^ { - \frac { 1 } { 3 } } n ^ { - 1 }$ . Plots (b) and (d) present the relationship between the logarithm of the effective sample size and the logarithm of the dimension for sampling from $\pi _ { n } ^ { \mathrm { m e d } }$ and $\pi _ { n } ^ { \mathrm { m e a n } }$ respectively. As we can see, when the sample size increases with the dimension at a rate of $d ^ { 2 }$ , by choosing steps sizes with scaling $d ^ { - \frac { 1 } { 3 } } n ^ { - 1 }$ , the acceptance probabilities roughly remain constant and the change in the logarithmic effective sample sizes exhibit slopes close to $- { \frac { 1 } { 3 } }$ for both examples of Bayesian linear regression and median regression. On the other hand, when $n$ remains a constant, in both cases, the acceptance probabilities will decrease as $d$ becomes larger, and the changes in the logarithmic effective sample size exhibit slopes smaller than $- { \frac { 1 } { 3 } }$ . However, compared to $\pi _ { n } ^ { \mathrm { m e d } }$ , the decreases in acceptance probability and effective sample size are much slower for sampling from $\pi _ { n } ^ { \mathrm { m e a n } }$ . In particular, when $n$ increases with $d$ at a linear rate, the acceptance probabilities for $\pi _ { n } ^ { \mathrm { m e a n } }$ roughly remain constant, while there is obvious decrease in the acceptance probabilities for $\pi _ { n } ^ { \mathrm { m e d } }$ .

# 8 Conclusion and Discussion

In this paper, we studied the sampling complexity of Bayesian (pseudo-)posteriors using MALA under large sample size, covering cases where the posterior density is non-smooth and/or non-log-concave. A variant of MALA that includes a preconditioning matrix was also considered. While our analysis for the preconditioned MALA suggests an adaptive MALA with a data-driven preconditioning matrix may be preferable, its rigorous theoretical analysis may leave as our future work. When applying our main result to Bayesian inference, we mainly considered the Gibbs posterior, while similar analysis may carry over to other types of Bayesian pseudo-posterior, such as Bayesian empirical likelihood [Lazar, 2003], and we leave this for future research. Another challenge lies in constructing a suitable warm start that satisfies $\log M _ { 0 } \leq d ^ { \frac { 1 } { 3 } }$ . Obtaining a warm start efficiently for general non-log-concave sampling can be challenging. However, the asymptotic Gaussian nature of the Bayesian posterior may aid in the construction of such a warm start, and it is possible to develop specific algorithms tailored to particular problems that leverage the Gaussian asymptotics. For instance, in Bayesian quantile regression, one can determine the point estimator $\hat { \theta }$ using linear programming and utilize the Gaussian asymptotic properties of the posterior to construct initializations. A more detailed exploration of this topic is left for future research.

# References

Pierre Alquier, James Ridgway, and Nicolas Chopin. On the properties of variational approximations of Gibbs posteriors. Journal of Machine Learning Research, 17(236):1–41, 2016. URL http: //jmlr.org/papers/v17/15-290.html. 2   
Jason M Altschuler and Sinho Chewi. Faster high-accuracy log-concave sampling via algorithmic warm starts. arXiv preprint arXiv:2302.10249, 2023. 13   
Filippo Ascolani and Giacomo Zanella. Dimension-free mixing times of Gibbs samplers for Bayesian hierarchical models, 2023. 2, 11, 13   
Yves F Atchade. An adaptive version for the Metropolis Adjusted Langevin Algorithm with a truncated ´ drift. Methodology and Computing in Applied Probability, 8(2):235–254, 2006. URL https: //doi.org/10.1007/s11009-006-8550-0. 14   
Alexandre Belloni and Victor Chernozhukov. On the computational complexity of MCMC-based estimators in large samples. The Annals of Statistics, 37(4):2011–2055, 2009. 3, 5, 10, 11, 12, 13, 20, 37   
Alexandre Belloni, Tengyuan Liang, Hariharan Narayanan, and Alexander Rakhlin. Escaping the local minima via simulated annealing: Optimization of approximately convex functions. In Conference on Learning Theory, pages 240–265. PMLR, 2015. 4   
Indrabati Bhattacharya and Ryan Martin. Gibbs posterior inference on multivariate quantiles. arXiv preprint arXiv:2002.01052, 2020. 2, 4, 6, 12   
Steve Brooks, Andrew Gelman, Galin Jones, and Xiao-Li Meng. Handbook of Markov Chain Monte Carlo. CRC press, 2011. 21   
Jeff Cheeger. A lower bound for the smallest eigenvalue of the Laplacian. In Problems in analysis, pages 195–200. Princeton University Press, 2015. 9   
Yuansi Chen, Raaz Dwivedi, Martin J. Wainwright, and Bin Yu. Fast mixing of Metropolized Hamiltonian Monte Carlo: Benefits of multi-step gradients. Journal of Machine Learning Research, 21(92):

1–72, 2020. URL http://jmlr.org/papers/v21/19-441.html. 4, 7, 9, 10, 12, 19, 20,   
28, 30, 33, 34, 37, 39

Xiang Cheng, Niladri S Chatterji, Yasin Abbasi-Yadkori, Peter L Bartlett, and Michael I Jordan. Sharp convergence rates for Langevin dynamics in the nonconvex setting. arXiv preprint arXiv:1805.01648, 2018. 8

Sinho Chewi, Chen Lu, Kwangjun Ahn, Xiang Cheng, Thibaut Le Gouic, and Philippe Rigollet. Optimal dimension dependence of the Metropolis-adjusted Langevin algorithm. In Mikhail Belkin and Samory Kpotufe, editors, Proceedings of Thirty Fourth Conference on Learning Theory, volume 134 of Proceedings of Machine Learning Research, pages 1260–1300. PMLR, 15–19 Aug 2021. URL https://proceedings.mlr.press/v134/chewi21a.html. 3, 4, 10, 12, 13, 20, 30, 37, 42

Arnak Dalalyan. Further and stronger analogy between sampling and optimization: Langevin Monte Carlo and gradient descent. In Satyen Kale and Ohad Shamir, editors, Proceedings of the 2017 Conference on Learning Theory, volume 65 of Proceedings of Machine Learning Research, pages 678–689. PMLR, 07–10 Jul 2017. URL https://proceedings.mlr.press/v65/dalalyan17a. html. 8

Alain Durmus and Eric Moulines. Nonasymptotic convergence analysis for the unadjusted Langevin algorithm. The Annals of Applied Probability, 27(3):1551–1587, 2017. 8

Alain Durmus, Szymon Majewski, and Błazej Miasojedow. Analysis of Langevin Monte Carlo via ˙ convex optimization. The Journal of Machine Learning Research, 20(1):2666–2711, 2019. 8

Raaz Dwivedi, Yuansi Chen, Martin J. Wainwright, and Bin Yu. Log-concave sampling: Metropolis-Hastings algorithms are fast. Journal of Machine Learning Research, 20(183):1–42, 2019. URL http://jmlr.org/papers/v20/19-306.html. 3, 8, 10, 11, 37

James M Flegal, Murali Haran, and Galin L Jones. Markov chain Monte Carlo: Can we trust the third significant figure? Statistical Science, pages 250–260, 2008. 27

A. Gelman, J.B. Carlin, H.S. Stern, D.B. Dunson, A. Vehtari, and D.B. Rubin. Bayesian Data Analysis, Third Edition. Chapman & Hall/CRC Texts in Statistical Science. Taylor & Francis, 2013. ISBN 9781439840955. URL https://books.google.com.hk/books?id $\underline { { \underline { { \mathbf { \Pi } } } } } =$ ZXL6AQAAQBAJ. 21

Andrew Gelman and Donald B Rubin. Inference from iterative simulation using multiple sequences. Statistical science, 7(4):457–472, 1992. 27

Andrew Gelman, John B Carlin, Hal S Stern, and Donald B Rubin. Bayesian data analysis. Chapman and Hall/CRC, 1995. 21

Andrew Gelman, Walter R Gilks, and Gareth O Roberts. Weak convergence and optimal scaling of random walk Metropolis algorithms. The annals of applied probability, 7(1):110–120, 1997. 3, 8

Stuart Geman and Donald Geman. Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of images. IEEE Transactions on pattern analysis and machine intelligence, pages 721–741, 1984. 2, 6

Abhik Ghosh, Tuhin Majumder, and Ayanendranath Basu. General robust bayes pseudo-posterior: Exponential convergence results with applications, 2020. 2

J. K. Ghosh and R. V. Ramamoorthi. Bayesian Nonparametrics. Springer New York, New York, NY, 2003. URL https://link.springer.com/book/10.1007/b97842. 11, 16

Mark Girolami and Ben Calderhead. Riemann manifold Langevin and Hamiltonian Monte Carlo methods. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 73(2): 123–214, 2011. doi: https://doi.org/10.1111/j.1467-9868.2010.00765.x. URL https://rss. onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9868.2010.00765.x. 7

Sharad Goel, Ravi Montenegro, and Prasad Tetali. Mixing time bounds via the spectral profile. Electronic Journal of Probability, 11(none):1 – 26, 2006. doi: 10.1214/EJP.v11-300. URL https: //doi.org/10.1214/EJP.v11-300. 20

W Keith Hastings. Monte Carlo sampling methods using Markov chains and their applications. 1970. 2, 6

Ravi Kannan, Laszl ´ o Lov ´ asz, and Ravi Montenegro. Blocking conductance and mixing in random ´ walks. Combinatorics, Probability and Computing, 15(4):541–570, 2006. 4

B.J.K. Kleijn and A.W. van der Vaart. The Bernstein-Von-Mises theorem under misspecification. Electronic Journal of Statistics, 6(none):354 – 381, 2012. doi: 10.1214/12-EJS675. URL https: //doi.org/10.1214/12-EJS675. 16

Benoˆıt Kloeckner. Effective berry–esseen and concentration bounds for Markov chains with a spectral gap. The Annals of Applied Probability, 29(3):1778–1807, 2019. 21

Roger Koenker and Gilbert Bassett. Regression quantiles. Econometrica, 46(1):33–50, 1978. ISSN 00129682, 14680262. URL http://www.jstor.org/stable/1913643. 17

M. R Kosorok. Introduction to empirical processes and semiparametric inference. Springer New York, New York, NY, 2008. 65

B. Laurent and P. Massart. Adaptive estimation of a quadratic functional by model selection. The Annals of Statistics, 28(5):1302 – 1338, 2000. doi: 10.1214/aos/1015957395. URL https://doi.org/ 10.1214/aos/1015957395. 53

Nicole A. Lazar. Bayesian empirical likelihood. Biometrika, 90(2):319–326, 06 2003. ISSN 0006-3444. doi: 10.1093/biomet/90.2.319. URL https://doi.org/10.1093/biomet/90.2.319. 23

Laszl ´ o Lov ´ asz and Ravi Kannan. Faster mixing via average conductance. In ´ Proceedings of the thirtyfirst annual ACM symposium on Theory of computing, pages 282–287, 1999. 4

L. Lovasz and M. Simonovits. Random walks in a convex body and an improved volume al- ´ gorithm. Random Structures & Algorithms, 4(4):359–412, 1993. doi: https://doi.org/10.1002/ rsa.3240040402. URL https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa. 3240040402. 7, 9, 20, 28

Yi-An Ma, Yuansi Chen, Chi Jin, Nicolas Flammarion, and Michael I Jordan. Sampling can be faster than optimization. Proceedings of the National Academy of Sciences, 116(42):20881–20885, 2019. 4

Oren Mangoubi and Nisheeth K Vishnoi. Nonconvex sampling with the Metropolis-adjusted Langevin algorithm. In Conference on Learning Theory, pages 2259–2293. PMLR, 2019. 11

Charles C Margossian. A review of automatic differentiation and its efficient implementation. Wiley interdisciplinary reviews: data mining and knowledge discovery, 9(4):e1305, 2019. 3

Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Alban Desmaison, Luca Antiga, and Adam Lerer. Automatic differentiation in pytorch. 2017. 3

Christian P Robert, George Casella, and George Casella. Monte Carlo statistical methods, volume 2. Springer, 2004. 2, 6

Gareth O Roberts and Jeffrey S Rosenthal. Optimal scaling of discrete approximations to Langevin diffusions. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 60(1):255– 268, 1998. 3, 4, 21

Gareth O Roberts and Richard L Tweedie. Exponential convergence of Langevin distributions and their discrete approximations. Bernoulli, pages 341–363, 1996. 8

Vivekananda Roy. Convergence diagnostics for Markov Chain Monte Carlo. Annual Review of Statistics and Its Application, 7:387–412, 2020. 27

Nicholas Syring and Ryan Martin. Gibbs posterior concentration rates under sub-exponential type losses. arXiv preprint arXiv:2012.04505, 2020. 2, 4, 6

Cornelia Vacar, Jean-Franc¸is Giovannelli, and Yannick Berthoumieu. Langevin and hessian with fisher approximation stochastic sampling for parameter estimation of structured covariance. In 2011 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 3964–3967, 2011. doi: 10.1109/ICASSP.2011.5947220. 7

Aad W van der Vaart. Asymptotic statistics, volume 3. Cambridge university press, 2000. 11

Roman Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2018. doi: 10.1017/9781108231596. 44, 65

Martin J. Wainwright. High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2019. doi: 10.1017/ 9781108627771. 55, 56, 58

Keru Wu, Scott Schmidler, and Yuansi Chen. Minimax mixing time of the Metropolis-adjusted Langevin algorithm for log-concave sampling. Journal of Machine Learning Research, 23(270):1–63, 2022. 10, 13, 30, 31

Yunwen Yang and Xuming He. Bayesian empirical likelihood for quantile regression. The Annals of Statistics, 40(2):1102–1131, 2012. ISSN 00905364, 21688966. URL http://www.jstor.org/ stable/41713667. 16

Keming Yu and Rana A. Moyeed. Bayesian quantile regression. Statistics & Probability Letters, 54(4):437–447, 2001. ISSN 0167-7152. doi: https://doi.org/10.1016/ S0167-7152(01)00124-9. URL https://www.sciencedirect.com/science/article/ pii/S0167715201001249. 2, 18

# Appendix

We summarize some necessary notation and definitions in the appendix. We use ${ \bf 1 } _ { A }$ to denote the indicator function of a set $A$ so that $\mathbf { 1 } _ { A } ( x ) = 1$ if $x \in A$ and zero otherwise. For two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ to mean $a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n , d$ . In addition, $a _ { n } \asymp b _ { n }$ means that both $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ hold, and $a _ { n } = \mathcal { O } ( b _ { n } )$ if $a _ { n } \lesssim b _ { n }$ ; $a _ { n } = \Theta ( b _ { n } )$ if $a _ { n } \asymp b _ { n }$ . We use $\mathbf { N } ( { \mathcal { F } } , d _ { n } , \varepsilon )$ to denote the $\varepsilon$ -covering number of $\mathcal { F }$ with respect to pseudo-metric $d _ { n }$ . Throughout, $C , c , C _ { 0 } , c _ { 0 } , c _ { 1 } , c _ { 1 } , .$ . . are generically used to denote positive constants independent of $n , d$ whose values might change from one line to another. We denote ${ \mathcal L } ^ { 2 } ( \pi )$ to be the space of square integrable functions under measure $\pi$ . For a transition kernel $T : \Theta \times B ( \Theta ) \to \mathbb { R }$ of a reversible Markov chain with invariant distribution $\pi$ , where $B ( \Theta )$ is the Borel-sigma algebra on $\Theta$ , the Dirichlet form $\mathcal { E } : \mathcal { L } _ { 2 } ( \pi ) \times \mathcal { L } _ { 2 } ( \pi )  \mathbb { R }$ associated with the transition kernel $T$ is given by $\begin{array} { r } { \mathcal { E } ( g , h ) = \frac { 1 } { 2 } \int _ { x , y \in \Theta ^ { 2 } } ( g ( x ) - h ( y ) ) ^ { 2 } T ( x , \mathrm { d } y ) \pi ( \mathrm { d } x ) . } \end{array}$ .

# A Additional Results

# A.1 Additional Simulation

In this section, we carry out experiment using Bayesian linear regression with the following posterior

$$
\pi _ { n } ^ { \mathrm { m e a n } } ( \theta | X ^ { ( n ) } ) \propto \exp \Big ( - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \| Y _ { i } - \widetilde { X } _ { i } ^ { T } \theta \| ^ { 2 } \Big ) \pi ( \theta ) , \quad \theta \in \mathbb { R } ^ { d } .
$$

for exploring the impact of the preconditioning matrix and initial distribution in MALA. We set the sample size $n = 2 0 0 0$ and choose the parameter dimension $d$ from set $\{ 1 0 , 1 5 , 2 0 , 3 0 , 5 0 \}$ . The covariates $\widetilde { X }$ are generated from a multivariate Gaussian distribution with zero mean and the covariance matrix $\Sigma$ given by a diagonal matrix with elements

$$
\Big ( \underbrace { \sqrt { d } , \sqrt { d } , \cdots , \sqrt { d } } _ { \Big [ \frac { d } { 2 } \Big ] } , \underbrace { \frac { 1 } { \sqrt { d } } , \frac { 1 } { \sqrt { d } } } _ { d - \Big [ \frac { d } { 2 } \Big ] } , \cdots , \frac { 1 } { \sqrt { d } } \Big ) .
$$

We consider two choices for the preconditioning matrix: one is the inverse (mini-batch) empirical gram matrix $\begin{array} { r } { \widehat { \Sigma } _ { m } = ( m ^ { - 1 } \sum _ { j = 1 } ^ { m } \widetilde { X } _ { j } \widetilde { X } _ { j } ^ { T } ) ^ { - 1 } } \end{array}$ , which is an estimator to the covariance matrix $n ^ { - 1 } \Sigma ^ { - 1 }$ of the posterior rescaled by $n$ . Here, we consider values of $m = \{ 2 0 0 , 5 0 0 , 2 0 0 0 \}$ . The other choice is the standard identity matrix. For the initial distribution, we also consider two options: one is $\mathcal { N } ( \widehat { \theta } , n ^ { - 1 } \widehat { \Sigma } _ { m } )$ with $\widehat { \theta }$ being the regression point estimator, as suggested in Corollary 1; and another choice is the standard normal distribution $\mathcal { N } ( 0 , I _ { d } )$ . Figure 2 displays the minimum number of iteration required for achieving a Gelman-Rubin statistic smaller than 1.1, which is a common-used rule for determining the burn-in period [Flegal et al., 2008, Roy, 2020, Gelman and Rubin, 1992]. We observe that choosing the initial distribution as $\mathcal { N } ( \widehat { \theta } , n ^ { - 1 } \widehat { \Sigma } _ { m } )$ allows the chain to converge in a very short period, whereas using $\mathcal { N } ( 0 , I _ { d } )$ requires a much longer time for convergence. Furthermore, we note that the mini-batch size does not significantly affect the required burn-in period, as choosing $m = 2 0 0$ is sufficient for fast convergence.

Figure 3 illustrates the largest step size allowed for achieving an average acceptance probability close to 0.57, as well as the effective sample size, after a total number of 5000 iterations with a burn-in period of 1000. We observe that utilizing the inverse empirical gram matrix enables a larger step size and leads to a larger effective sample size. Additionally, we find that the best performance is achieved when the batch size $m$ is chosen to be equal to the sample size $n$ . This is because a larger batch size provides a better estimator for $\Sigma ^ { - 1 } = ( \mathbb { E } [ \widetilde { X } \widetilde { X } ] ) ^ { - 1 }$ , resulting in a rescaled covariance matrix $\widehat { \Sigma } _ { m } ^ { \frac { 1 } { 2 } } ( \mathbb { E } [ \widetilde { X } \widetilde { X } ] ) ^ { - 1 } \widehat { \Sigma } _ { m } ^ { \frac { 1 } { 2 } }$ with a smaller condition number. However, when $d \leq 2 0$ , choosing $m = 5 0 0$ instead of using the full batch does not result in significant loss in performance.

![](images/7cf099e96ac50d12f87a14e8cf6bdf393b27ab11337f1cceac6afbdadcd70d90.jpg)  
Figure 2: The figure shows the minimal burn-in period required to attain a Gelman-Rubin statistic below 1.1. It compares two scenarios: MALA with an initial distribution of $\mathcal { N } ( 0 , I _ { d } )$ and a preconditioning matrix of $I _ { d }$ , and MALA with an initial distribution of $\mathcal { N } ( \widehat { \theta } , \widehat { \Sigma } _ { m } / n )$ and a preconditioning matrix of $\hat { \Sigma } _ { m }$ . We can see the utilization of $\hat { \Sigma } _ { m }$ for constructing the initial distribution and preconditioning matrix can significantly accelerates the convergence of MALA.

# A.2 Lemmas Related to $s$ -conductance Profile

Lemma 3 (Mixing time bound via $s$ -conductance profile). Consider a reversible,8 irreducible,9 $\zeta$ - $l a z y$ and smooth Markov chain11 with stationary distribution $\mu$ . For any error tolerance $\varepsilon \in ( 0 , 1 )$ , the maximal mixing time in $\chi ^ { 2 }$ divergence of the chain over $M _ { 0 }$ -warm starts can be bounded as

$$
\tau _ { \mathrm { m i x } } ( \varepsilon , M _ { 0 } ) \leq \frac { 1 6 } { \zeta } \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { \mathrm { d } v } { v \Phi _ { s } ^ { 2 } ( v ) } + \frac { 6 4 } { \zeta } \int _ { \frac { 1 } { 2 } } ^ { \frac { 4 \sqrt { 2 } } { \varepsilon } } \frac { \mathrm { d } v } { v \Phi _ { s } ^ { 2 } ( \frac { 1 } { 2 } ) } ,
$$

where $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ .

We can calculate the second term of the upper bound above explicitly as $\frac { 6 4 } { \zeta \Phi _ { s } ^ { 2 } ( \frac 1 2 ) } \log \Big ( \frac { 8 \sqrt { 2 } } { \xi } \Big )$ The next lemma shows that the $s$ -conductance profile can be lower bounded given one can: 1. prove a logisoperimetric inequality for $\mu$ ; 2. bound the total variation distance between $T ( x , \cdot )$ and $T ( z , \cdot )$ for any two sufficiently close points $x , z$ in a high probability set (not necessarily convex) of $\mu$ , which will be referred to as the overlap argument.

Lemma 4 ( $s$ -conductance profile lower bound). Consider a Markov chain with Markov transition kernel $T$ and stationary distribution $\mu$ . Given a tolerance $\varepsilon \in ( 0 , 1 )$ and warming parameter $M _ { 0 } , i f$ there are two sets $K$ , $E$ , and positive numbers $\lambda$ , $\psi$ , $\omega$ so that

![](images/76bdcf1130bf12d607aeb9dc64cf8b84f49c415e43a3de593c9172378fb721e2.jpg)  
Figure 3: Plot (a) illustrates the logarithm of the maximum step size allowed to achieve an average acceptance probability close to 0.57 for various preconditioning matrices and dimensions. Plot (b) illustrates the relationship between the logarithm of the effective sample size and the logarithm of the dimension. The results demonstrate that choosing the preconditioning matrix based on the inverse of the empirical gram matrix enables the use of larger step sizes and leads to a higher effective sample size. Additionally, the disparity between different cases for various values of $m$ becomes more pronounced as the dimension $d$ increases. This is because the approximation error of $\widehat { \Sigma } _ { m }$ increases with higher dimensions, necessitating a larger batch size for accurate estimation.

1. the probability measure of µ constrained on K, denoted as µ|K (·) = µ(· ∩K)µ(K) , satisfies the following log-isoperimetric inequality:

$$
\mu | _ { K } ( S _ { 3 } ) \geq \lambda \cdot t \cdot \operatorname* { m i n } \left\{ \mu | _ { K } ( S _ { 1 } ) , \mu | _ { K } ( S _ { 2 } ) \right\} \cdot \sqrt { \log \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \mu | _ { K } ( S _ { 1 } ) , \mu | _ { K } ( S _ { 2 } ) \right\} } \right) } ,
$$

for any partition12 $K = S _ { 1 } \cup S _ { 2 } \cup S _ { 3 }$ satisfying $\begin{array} { r } { \operatorname* { i n f } _ { x \in S _ { 1 } , z \in S _ { 2 } } \| x - z \| \geq t , } \end{array}$ ;

2. for any $x , z \in E , i f \| x - z \| \leq \psi$ , then $\| T ( x , \cdot ) - T ( z , \cdot ) \| _ { \mathrm { T V } } \leq 1 - \omega ,$ ;

3. it holds that $\begin{array} { r } { \mu ( E ) \geq 1 - \left( \lambda \psi \wedge 1 \right) \frac { \varepsilon ^ { 2 } } { 2 5 6 M _ { 0 } ^ { 2 } } a n d \mu ( K ) \geq 1 - \left( \lambda \psi \wedge 1 \right) \frac { \varepsilon ^ { 2 } } { 2 5 6 M _ { 0 } ^ { 2 } } ; } \end{array}$ then the s-conductance profile $\Phi _ { s } ( v )$ with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ can be bounded from below by

$$
\Phi _ { s } ( v ) \geq { \frac { \omega } { 4 } } \operatorname* { m i n } { \left\{ 1 , { \frac { \lambda \psi } { 9 } } { \sqrt { \log \left( 1 + { \frac { 1 } { v } } \right) } } \right\} } .
$$

By combining this lemma with Lemma 3, we obtain that if the assumptions in Lemma 4 hold, then the mixing time of the chain can be bounded as

$$
\tau _ { \mathrm { m i x } } ( \varepsilon , M _ { 0 } ) \leq \frac { C _ { 1 } } { \zeta \omega ^ { 2 } } \log M _ { 0 } + \frac { C _ { 1 } } { \zeta \omega ^ { 2 } } \lambda ^ { - 2 } \psi ^ { - 2 } \log ( \log M _ { 0 } ) + \frac { C _ { 1 } } { \zeta \omega ^ { 2 } } \lambda ^ { - 2 } \psi ^ { - 2 } \log \frac { 1 } { \varepsilon } ,
$$

for some universal constant $C _ { 1 }$ . Therefore, the problem of bounding the mixing time can be converted to verify the assumptions in Lemma 4.

# A.3 Lower Bound of Mixing Time

Theorem 3 (MALA mixing time lower bound). Consider a positive definite preconditioning matrix $\boldsymbol { \widetilde { I } } \in \mathbb { R } ^ { d \times d }$ , and the target distribution defined as a multivariate normal $\overline { { \pi } } = \mathcal { N } ( 0 , J ^ { - 1 } )$ , where $J \in \mathbb { R } ^ { d \times d }$ is a covariance matrix with $\widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } } = \mathrm { d i a g } ( \rho _ { 2 } , \rho _ { 2 } , \cdots , \rho _ { 2 } , \rho _ { 1 } )$ . Assume $\begin{array} { r } { 1 \leq \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } \leq c _ { 1 } \cdot d ^ { c _ { 2 } } } \end{array}$ for some $c _ { 1 } , c _ { 2 } > 0$ . Then there exists an integer $N$ that depends only on $c _ { 1 } , c _ { 2 }$ and universal constants $c _ { 3 } , c _ { 4 }$ such that for any $d > N$ , $M _ { 0 } \geq 2$ , step size $h > 0$ and tolerance $\varepsilon \in ( 0 , 1 )$ , the $\frac { 1 } { 2 }$ -lazy version of preconditioned MALA for sampling from $\overline { { \pi } }$ has the following mixing time lower bound in $\chi ^ { 2 }$ divergence

$$
\tau _ { \operatorname* { m i x } } ( \varepsilon , M _ { 0 } ) \geq c _ { 3 } \kappa \left( \frac { d } { \log ( d \kappa ) } \right) ^ { \frac { 1 } { 3 } } \log \left( \frac { c _ { 4 } } { \varepsilon } \right) .
$$

A proof of Theorem 3 is provided in Appendix B.3, part of which is adapted from Chewi et al. [2021], Wu et al. [2022]. Note that the worst-case construction used in $\mathrm { W u }$ et al. [2022] does not satisfy our condition A. As a result, our lower bound has a different dimension dependence of $d ^ { 1 / 3 }$ than that in $\mathrm { W u }$ et al. [2022] of $d ^ { 1 / 2 }$ . Additionally, unlike Theorem 1 of Chewi et al. [2021], which considers a standard Gaussian target distribution (i.e., $\kappa = 1$ ), our lower bound has an explicit linear dependence on the condition number. From Theorem 1 and Theorem 3, we can see that when $\begin{array} { r } { \log \left( \frac { M _ { 0 } \kappa } { \varepsilon } \right) = \mathcal { O } ( d ^ { \frac { 1 } { 3 } } ) } \end{array}$ , our mixing time upper bound and lower bound match up to some logarithmic terms of $( d , \kappa )$ and a double logarithmic term of $M _ { 0 }$ .

# B Proof of Main Results

# B.1 Proof of Theorem 1 (MALA mixing time upper bound)

Note that combined with Lemma 3, if the assumptions in Lemma 4 holds, we have

$$
\begin{array} { l } { \tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) \leq \displaystyle \frac { C } { \zeta \omega } \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { 1 } { v } \mathrm { d } v + \displaystyle \frac { C } { \zeta \omega } \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \lambda ^ { - 2 } \psi ^ { - 2 } \frac { 1 } { v \log ( 1 + \frac { 1 } { v } ) } \mathrm { d } v + \displaystyle \frac { C } { \zeta \omega } \int _ { \frac { 1 } { 2 } } ^ { \frac { 4 \sqrt { 2 } } { \varepsilon } } \lambda ^ { - 2 } \psi ^ { - 2 } \frac { 1 } { v } \mathrm { d } v } \\ { \leq \displaystyle \frac { C _ { 1 } } { \zeta \omega } \log M _ { 0 } + \displaystyle \frac { C _ { 1 } } { \zeta \omega } \lambda ^ { - 2 } \psi ^ { - 2 } \log ( \log M _ { 0 } ) + \displaystyle \frac { C _ { 1 } } { \zeta \omega } \lambda ^ { - 2 } \psi ^ { - 2 } \log \frac { 1 } { \varepsilon } , } \end{array}
$$

where the last inequality follows equation (18) of Chen et al. [2020]. Now it remains to verify the assumptions in Lemma 4. Fix a lazy parameter $\zeta \in ( 0 , \frac { 1 } { 2 } ]$ . Consider a linear transformation $G : \mathbb { R } ^ { d } $ $\mathbb { R } ^ { d }$ defined as $G ( \theta ) = \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat { \theta } )$ , and let ${ \widetilde { \mu } } _ { k } = G _ { \# } \mu _ { k }$ denote the push forward measure of $G$ by $\mu _ { k }$ for $k \in \mathbb N$ and $\widetilde { \pi } _ { \mathrm { l o c } }$ edenote the push forward measure of $G$ by $\pi _ { n }$ . Then it holds that

$$
M _ { 0 } = \operatorname* { s u p } _ { A : \pi _ { n } ( A ) > 0 } \frac { \mu _ { 0 } ( A ) } { \pi _ { n } ( A ) } = \operatorname* { s u p } _ { A : \pi _ { \mathrm { l o c } } ( A ) > 0 } \frac { \widetilde { \mu } _ { 0 } ( A ) } { \widetilde { \pi } _ { \mathrm { l o c } } ( A ) } .
$$

Moreover, by the invariability of $\chi ^ { 2 }$ measure to linear transformation, we have $\chi ^ { 2 } ( \mu _ { k } , \pi _ { n } ) = \chi ^ { 2 } ( \widetilde { \mu } _ { k } , \widetilde { \pi } _ { \mathrm { l o c } } )$ Define $\widetilde Q ( \xi , \cdot )$ be the density function of the multivarite normal $N _ { d } ( \xi - h \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) , 2 h I _ { d } )$ , and the corresponding Markov transition kernel

$$
\widetilde { T } ( \xi , \mathrm { d } y ) = \left[ 1 - ( 1 - \zeta ) \cdot \int \widetilde { A } ( \xi , y ) \widetilde { Q } ( \xi , y ) \mathrm { d } y \right] \mathbf { 1 } _ { \xi } ( \mathrm { d } y ) + ( 1 - \zeta ) \cdot \widetilde { Q } ( \xi , y ) \widetilde { A } ( \xi , y ) \mathrm { d } y
$$

with

$$
\widetilde { A } ( \xi , y ) = 1 \wedge \frac { \widetilde { \pi } _ { \mathrm { l o c } } ( y ) \widetilde { Q } ( y , \xi ) } { \widetilde { \pi } _ { \mathrm { l o c } } ( \xi ) \widetilde { Q } ( \xi , y ) } .
$$

We have the following lemma.

Lemma 5. For any $k \in \mathbb N$ , $\widetilde { \mu } _ { k } = G _ { \# } \mu _ { k }$ is the probability distribution obtained after k steps of a Markov chain with transition kernel $\widetilde { T }$ and initial distribution $\widetilde { \mu } _ { 0 }$ .

It remains to calculate the mixing time of $\widetilde { \mu } _ { k }$ converging to $\widetilde { \pi } _ { \mathrm { l o c } }$ , which is equivalent to verify the asesumptions in Lemma 4 for Markov transition kernel $\widetilde { T } ( \xi , \cdot )$ e with stationary distribution $\widetilde { \pi } _ { \mathrm { l o c } }$ . Recall $K = \{ x : \| \widetilde { I } ^ { - \frac { 1 } { 2 } } x \| \leq R \}$ . By Condition A, firstly we have

$$
\begin{array} { r l r } & { \underset { \xi \in B _ { R } ^ { d } } { \operatorname* { s u p } } | V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \xi } ) - \frac { 1 } { 2 } \widetilde { \xi } ^ { T } \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \xi } | = \underset { \xi \in K } { \operatorname* { s u p } } | V _ { n } ( \xi ) - \frac { 1 } { 2 } \xi ^ { T } J \xi | \leq \widetilde { \varepsilon } _ { 0 } ; } & \\ & { \underset { \widetilde { \xi } \in B _ { R } ^ { d } } { \operatorname* { s u p } } | \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) - \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } } \xi | | = \underset { \xi \in K } { \operatorname* { s u p } } | | \widetilde { I } ^ { \frac { 1 } { 2 } } ( \widetilde { \nabla } V _ { n } ( \xi ) - J \xi ) | | \leq \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } , } & \end{array}
$$

and $\begin{array} { r } { \widetilde { \pi } _ { \mathrm { l o c } } ( \widetilde { \xi } \in B _ { R / 2 } ^ { d } ) = \pi _ { n } ( \| \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat { \theta } ) \| \le R / 2 ) \ge 1 - \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { h \rho _ { 1 } \varepsilon ^ { 2 } } { M _ { 0 } ^ { 2 } } . } \end{array}$ We then verify the log-isoperimetric inequality in the following lemma.

Lemma 6. Let ${ \cal \tilde { K } } = B _ { R / 2 } ^ { d } $ , consider any measurable partition form ${ \tilde { K } } = S _ { 1 } \cup S _ { 2 } \cup S _ { 3 }$ such that $\begin{array} { r } { \operatorname* { i n f } _ { x \in S _ { 1 } , z \in S _ { 2 } } \| x - z \| \geq t } \end{array}$ , we have

$$
S _ { 3 } ) \geq \frac { \sqrt { \rho _ { 1 } } } { 2 } t \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) , \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) , \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 2 } ) \} } \Big ) .
$$

We then show that $\| \widetilde { T } ( x , \cdot ) - \widetilde { T } ( y , \cdot ) \| _ { \mathrm { T V } }$ can be bounded with high probability in the following lemma.

Lemma 7. There exists a set $E$ so that $\begin{array} { r } { \widetilde { \pi } _ { \mathrm { l o c } } ( E ) \geq 1 - \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { 2 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } } \end{array}$ and for any $x , z \in E$ with $\begin{array} { r } { \| x - z \| \leq \frac { \sqrt { h } } { 3 } } \end{array}$ , we have $\begin{array} { r } { \| \widetilde { T } ( x , \cdot ) - \widetilde { T } ( z , \cdot ) \| _ { \mathrm { T V } } \leq 1 - \frac { \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) } { 4 } } \end{array}$ .

Thus the first and second assumptions in Lemma 4 holds with $\begin{array} { r } { \lambda = { \frac { \sqrt { \rho _ { 1 } } } { 2 } } \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) } \end{array}$ , $\textstyle \psi = { \frac { \sqrt { h } } { 3 } }$ and ω = exp(−2εe0)4 . Moreover, for the third assumption in Lemma 4, by hρ1 ≤ c0d− 13 , for small enough c0, we have

$$
\exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { 2 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } \leq \frac { \sqrt { 2 h } } { 2 4 } \frac { \sqrt { \rho _ { 1 } } } { 2 } \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \frac { \varepsilon ^ { 2 } } { 2 5 6 M _ { 0 } ^ { 2 } } .
$$

Thus all the assumptions in Lemma 4 are satisfied. The desired result then follows from equation (12).

# B.2 Proof of Theorem 3 (MALA mixing time lower bound)

Without loss of generality, we assume $\widetilde { I } = I _ { d }$ . Otherwise, similar as the proof of Theorem 1, we could transform the measures $\mu _ { k }$ and $\overline { { \pi } }$ by the scale matrix $\widetilde { I } ^ { - \frac { 1 } { 2 } }$ , and study the convergence of the transformed measures. We utilize the following lower bound on the $\chi ^ { 2 }$ -divergence via Dirichlet form.

Lemma 8. (Corollary 7 of Wu et al. [2022]) Le $T$ be the transition kernel of a reversible Markov chain with invariant distribution $\overline { { \pi } }$ . For any $\varepsilon > 0$ and any initial distribution $\mu _ { 0 } \ll \overline { { \pi } }$ satisfying $\chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) <$ $\infty .$ , let $\begin{array} { r } { h _ { 0 } = \frac { \mathrm { d } \mu _ { 0 } } { \mathrm { d } \overline { { \pi } } } } \end{array}$ , if $\mathcal { E } ( h _ { 0 } , h _ { 0 } ) / \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) \leq \frac { 1 } { 4 }$ with $\mathcal { E } ( \cdot , \cdot )$ being the Dirichlet form associated with $T$ , then its mixing time in $\chi ^ { 2 }$ -divergence has a lower bound

$$
\tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) \geq \frac { 1 } { 4 } \left( \frac { \mathcal { E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) } \right) ^ { - 1 } \log \left( \frac { \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) } { \varepsilon ^ { 2 } } \right) .
$$

Then, we state the following lemma for bounding $\mathcal { E } ( h _ { 0 } , h _ { 0 } ) / \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } )$ .

Lemma 9. Consider the target distribution $\overline { { \pi } } = N _ { d } ( 0 , J ^ { - 1 } )$ with $J = \mathrm { d i a g } ( \rho _ { 2 } , \rho _ { 2 } , \cdot \cdot \cdot , \rho _ { 2 } , \rho _ { 1 } )$ and $\begin{array} { r } { 1 \leq \kappa = \frac { \rho _ { 2 } } { \rho _ { 1 } } \leq c _ { 1 } \cdot d ^ { c _ { 2 } } } \end{array}$ , then

1. There exists a 2-warm initial distribution $\mu _ { 0 }$ with $\textstyle \chi ^ { 2 } ( \mu _ { 0 } , { \overline { { \pi } } } ) \geq { \frac { 1 } { 5 } }$ so that for any $h \in ( 0 , \frac { 1 } { \rho _ { 1 } } )$ , denote $\begin{array} { r } { h _ { 0 } = \frac { \mathrm { d } \mu _ { 0 } } { \mathrm { d } \overline { { \pi } } } } \end{array}$ , then for any $\zeta \in [ 0 , 1 ]$ , the term $\mathcal { E } ( h _ { 0 } , h _ { 0 } ) / \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } )$ under the $\zeta$ -lazy version $h$

$$
\frac { { \mathscr E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) } \leq 6 0 \rho _ { 1 } h .
$$

2. When $M _ { 0 } \geq 2 $ , there exists an $M _ { 0 }$ -warm initial distribution $\mu _ { 0 } ^ { \prime }$ with $\chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) = M _ { 0 } - 1$ and a constant $N$ that depends only on $c _ { 1 } , c _ { 2 }$ so that when $d \ge N$ , denote $\begin{array} { r } { h _ { 0 } = \frac { \mathrm { d } \mu _ { 0 } ^ { \prime } } { \mathrm { d } \overline { { \pi } } } } \end{array}$ , for any $h \in$ $( \frac { 8 ( \log ( d \kappa ) ) ^ { \frac { 1 } { 3 } } } { \rho _ { 2 } d ^ { \frac { 1 } { 3 } } } , \infty ) .$ , for any $\zeta \in [ 0 , 1 ]$ , the term $\mathcal { E } ( h _ { 0 } , h _ { 0 } ) / \chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } )$ under the $\zeta$ -lazy version MALA transition kernel with step size h satisfies

$$
\frac { { \mathscr E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) } \leq \frac { 8 } { \kappa d } .
$$

So when $d \geq N \vee 3$ , if $h > \frac { 8 ( \log ( d \kappa ) ) ^ { \frac { 1 } { 3 } } } { \rho _ { 2 } d ^ { \frac { 1 } { 3 } } }$ , we have

$$
\operatorname* { s u p } _ { 2 - \mathrm { w a r m } \mu _ { 0 } } \tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) \geq \frac { \kappa d } { 4 6 } \log ( \frac { 1 } { \varepsilon ^ { 2 } } ) \geq \frac { \kappa d ^ { \frac { 1 } { 3 } } } { 4 6 } \log ( \frac { 1 } { \varepsilon ^ { 2 } } ) ;
$$

$h \leq \frac { 8 ( \log ( d \kappa ) ) ^ { \frac { 1 } { 3 } } } { \rho _ { 2 } d ^ { \frac { 1 } { 3 } } }$ , we have $\rho _ { 1 } h < 1$ and thus,

$$
\operatorname* { s u p } _ { 2 - \mathrm { w a r m } \mu _ { 0 } } \tau _ { \mathrm { m i x } } ( \varepsilon , \mu _ { 0 } ) \geq \frac { 1 } { 2 4 0 } \rho _ { 1 } ^ { - 1 } h ^ { - 1 } \log ( \frac { 1 } { 5 \varepsilon ^ { 2 } } ) \geq \frac { \kappa d ^ { \frac { 1 } { 3 } } } { 1 9 2 0 ( \log ( d \kappa ) ) ^ { \frac { 1 } { 3 } } } \log ( \frac { 1 } { 5 \varepsilon ^ { 2 } } ) .
$$

Proof is completed.

# B.3 Proof of Theorem 2 (Complexity of MALA for Bayesian sampling)

Without loss of generality, we can assume the learning rate $\alpha = 1$ , as otherwise we can take $\ell ( X , \theta ) =$ $\alpha \cdot \ell ( X , \theta )$ . We only need to verify that the Assumptions in Theorem 1 holds for the Bayesian Gibbs posterior. We state the following Lemmas to verify Condition A.

Lemma 10. Let κ2 = β1γ3+β1(1+γ4)+2γ0−γ4 $\begin{array} { r } { \kappa _ { 2 } = \frac { \beta _ { 1 } } { \gamma _ { 3 } + \beta _ { 1 } ( 1 + \gamma _ { 4 } ) + 2 \gamma _ { 0 } - \gamma _ { 4 } } \wedge \frac { 1 } { 1 + 2 \gamma + 2 \gamma _ { 2 } + 4 \gamma _ { 0 } } \wedge \frac { 1 } { 2 + 2 ( \gamma + \gamma _ { 0 } + \gamma _ { 1 } ) } } \end{array}$ . Under Conditions B.1-B.4, $\begin{array} { r } { i f d \leq c ( \frac { n } { \log n } ) ^ { \kappa _ { 2 } } } \end{array}$ for a small enough constant $c ,$ then there exist $( n , d )$ -independent constants √ $c _ { 1 } , C , C _ { 1 }$ so that it holds with probability at least $1 - c _ { 1 } n ^ { - 2 }$ that for any $\xi \in \mathbb { R } ^ { d }$ with $1 \leq \| \xi \| \leq C \sqrt { n }$ ,

$$
\begin{array} { l } { { \displaystyle V _ { n } ( \xi ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } \Big \vert \le C _ { 1 } ( d ^ { 1 + \gamma } \| \xi \| \frac { \log n } { \sqrt { n } } + d ^ { \gamma _ { 2 } } \| \xi \| ^ { 3 } \frac { 1 } { \sqrt { n } } + d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \| \xi \| ^ { 2 } \sqrt { \frac { \log n } { n } }  } } \\ { { \displaystyle  + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \xi \| ^ { 1 + \beta } \frac { \sqrt { \log n } } { n ^ { \beta _ { 1 } / 2 } } ) } ; } \\ { { \displaystyle  \tilde { \nabla } V _ { n } ( \xi ) - \mathcal { H } _ { \theta ^ { * } } \xi   \le C _ { 1 } ( d ^ { 1 + \gamma } \frac { \log n } { \sqrt { n } } + d ^ { \gamma _ { 2 } } \| \xi \| ^ { 2 } \frac { 1 } { \sqrt { n } } + d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \| \xi \| \sqrt { \frac { \log n } { n } }  } \ ~ } \\ { { \displaystyle  + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \xi \| ^ { \beta _ { 1 } } \frac { \sqrt { \log n } } { n ^ { \beta _ { 1 } / 2 } } ) w i t h \tilde { \nabla } V _ { n } ( \xi ) = \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } g \Big ( X _ { i } , \frac { \xi } { \sqrt { n } } + \hat { \theta } \Big ) - \frac { 1 } { \sqrt { n } } \nabla ( \log \pi ) \Big ( \frac { \xi } { \sqrt { n } } + \hat { \theta } \Big ) } . } \end{array}
$$

We provide in the following lemma a tail inequality for the Gibbs posterior $\pi _ { n }$

Lemma 11. Under Condition B.1-B.4. when $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ for a small enough constant c, where

$$
\begin{array} { l } { \displaystyle \ = \frac { \beta _ { 1 } } { 1 + \gamma _ { 3 } + [ ( 2 \gamma _ { 0 } ) \vee ( ( 1 + \gamma _ { 0 } ) ( 1 + \beta _ { 1 } ) ) ] } \wedge \frac { 1 } { 3 + \gamma _ { 0 } + ( ( 2 \gamma ) \vee ( \gamma _ { 4 } + 2 \gamma _ { 2 } + \gamma _ { 0 } ) \vee ( 2 \gamma _ { 2 } + 2 \gamma _ { 0 } ) ) } } \\ { \displaystyle \wedge \frac { 1 } { 1 + 2 \gamma + 6 \gamma _ { 0 } + 4 \gamma _ { 2 } + \gamma _ { 4 } } \wedge \frac { 1 } { 2 \gamma + 2 \gamma _ { 0 } + 2 \gamma _ { 1 } + ( 2 \vee ( 1 + \gamma _ { 4 } ) ) } , } \end{array}
$$

then there exist $( n , d )$ -independent constants $c _ { 1 } , c _ { 2 } , c _ { 3 }$ so that it holds with probability at least $1 - c _ { 1 } n ^ { - 2 }$ that

$$
\begin{array} { r } { \cdot { _ n } \Big ( \sqrt { n } \| \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat { \theta } ) \| \geq \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \vee \frac { 3 ( \sqrt { d } + t ) } { \sqrt { \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) } } \Big ) \leq \exp ( - t ^ { 2 } ) + c _ { 2 } \exp \big ( - c _ { 3 } n d ^ { - \gamma _ { 0 } } ( d ^ { - \gamma _ { 1 } } \wedge d ^ { - 2 \gamma _ { 0 } - 2 \gamma _ { 0 } } ) \big ) . } \end{array}
$$

where $\widetilde { J } = \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } }$ .

By Condition B.1, we have $\| { \mathcal { H } } _ { \theta ^ { * } } \| _ { \mathrm { o p } } \leq C d$ and $\| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } } \leq C d ^ { \gamma _ { 0 } }$ . Moreover, since $\| \widetilde { I } ^ { - 1 } \| _ { \mathrm { o p } } \| \widetilde { I } \| _ { \mathrm { o p } } \leq$ $C \| \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } \| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } }$ and $\| \vert \widetilde { I } \| _ { \mathrm { o p } } \| ( \widetilde { I } ^ { \frac { 1 } { 2 } } H _ { \theta ^ { \ast } } \widetilde { I } ^ { \frac { 1 } { 2 } } ) ^ { - 1 } \| _ { \mathrm { o p } } \leq C \| \dot { \mathcal { H } } _ { \theta ^ { \ast } } ^ { - 1 } \| _ { \mathrm { o p } }$ , we can obtain that there exists constants $C _ { 2 } , C _ { 3 }$ so that for any $R = \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \vee \frac { 3 ( \sqrt { d } + t ) } { \sqrt { \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) } }$ with $t \geq 0$ , and set $K = \{ x : \| \widetilde { I } ^ { - 1 / 2 } x \| \leq R \}$ , (note that we have $K \subseteq \{ x : \| x \| \leq C _ { 2 } d ^ { \frac { 1 + \gamma _ { 0 } } { 2 } } + C _ { 3 } t d ^ { \frac { \gamma _ { 0 } } { 2 } } \}$ $\gamma _ { 5 } \geq 1 \AA$ 2   ), we can find a constant $c$ so that when λmin(Je). Then by Lemma 10, for any $\begin{array} { r } { \dot { d } \le c \frac { n ^ { \kappa _ { 1 } } } { \log n } } \end{array}$ , we have $t = C _ { 1 } \left( d ^ { \frac { \gamma _ { 5 } } { 2 } } + \sqrt { \log n } \right)$

$$
\begin{array} { r } { \| \widetilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \underset { \xi \in \cal K } { \operatorname* { s u p } } \| \widetilde { \nabla } V _ { n } ( \xi ) - \mathcal H _ { \theta ^ { * } } \xi \| ^ { 2 } \leq d ^ { \frac { 1 } { 3 } } . } \end{array}
$$

So in this case the step size parameter $\widetilde { h } = h / n$ in Theorem 1 satisfies

$$
h \leq c _ { 0 } \cdot \bigg [ \rho _ { 2 } \Big ( 2 d ^ { \frac { 1 } { 3 } } + d ^ { \frac { 1 } { 4 } } \big ( \log \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) ^ { \frac { 1 } { 4 } } + \big ( \log \frac { M _ { 0 } d \kappa } { \varepsilon } \big ) ^ { \frac { 1 } { 2 } } \Big ) \bigg ] ^ { - 1 }
$$

Then by the assumption $\begin{array} { r } { \log ( \frac { M _ { 0 } \rho _ { 2 } } { \varepsilon \rho _ { 1 } } ) \leq C _ { 1 } \left( d ^ { \gamma _ { 5 } } + \log n \right) } \end{array}$ , using Lemma 11 and $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 1 } } } { \log { n } } } \end{array}$ , we can obtain that there exists a large enough $C _ { 1 }$ so that for $t = C _ { 1 } \big ( d ^ { \frac { \gamma _ { 5 } } { 2 } } + \sqrt { \log n } \big ) , \pi _ { n } ( K ) = \pi _ { n } \Big ( \sqrt { n } \| \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat \theta ) \| \geq$ $\begin{array} { r } { \| \vert \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \vee \frac { 3 ( \sqrt { d } + t ) } { \sqrt { \lambda _ { \mathrm { m i n } } ( \widetilde { J } ) } } \Big ) \geq 1 - \frac { h \rho _ { 1 } \varepsilon ^ { 2 } } { M _ { 0 } ^ { 2 } } } \end{array}$ . So the Assumptions in Theorem 1 are satisfied.

# C Proof of Lemmas for Theorem 1 and Theorem 3

# C.1 Proof of Lemma 3

Fix an arbitrary $\varepsilon > 0$ . Suppose $\begin{array} { r } { \tau _ { \mathrm { m i x } } ( \sqrt { 2 } \varepsilon , \mu _ { 0 } ) > N = \int _ { \frac { 4 } { M _ { 0 } } } ^ { \frac { 1 } { 2 } } \frac { 1 6 \mathrm { d } v } { \zeta \cdot v \Phi _ { s } ^ { 2 } ( v ) } + \int _ { \frac { 1 } { 2 } } ^ { \frac { 4 } { \varepsilon } } \frac { 6 4 \mathrm { d } v } { \zeta \cdot v \Phi _ { s } ^ { 2 } ( \frac { 1 } { 2 } ) } } \end{array}$ . Then for any $k \le N , \chi ^ { 2 } ( \mu _ { k } , \mu ) > 2 \varepsilon ^ { 2 }$ , where we use $\chi ^ { 2 } ( \cdot , \cdot )$ to denote the $\chi ^ { 2 }$ divergence, $\mu _ { k }$ to denote the distribution in $k$ step of the Markov chain and $\mu \in \mathcal P ( \mathbb { R } ^ { d } )$ to denote the stationary distribution. Then we will prove by contradiction that if $N < \tau _ { \mathrm { m i x } } ( \sqrt { 2 } \varepsilon , \mu _ { 0 } )$ , then when $k = N$ , $\chi ^ { 2 } ( \mu _ { k } , \mu ) \leq 2 \varepsilon ^ { 2 }$ , which oppositely implies $N \ge \tau _ { \operatorname* { m i x } } ( \sqrt { 2 } \varepsilon , \mu _ { 0 } )$ . Our proof is based on the strategy used in Chen et al. [2020]. We first introduce the following related notations. For a measurable set $S \subseteq \mathbb { R } ^ { d }$ and positive numbers $\varepsilon , M _ { 0 }$ , the $( \varepsilon , M _ { 0 } )$ -spectral gap for the set $S$ is defined as

$$
\Lambda _ { \varepsilon , M _ { 0 } } ( S ) : = \operatorname* { i n f } _ { g \in c _ { \varepsilon , M _ { 0 } } ^ { + } ( S ) } \frac { \mathcal { E } ( g , g ) } { \operatorname { V a r } _ { \mu } ( g ) }
$$

where

$$
c _ { \varepsilon , M _ { 0 } } ^ { + } ( S ) : = \left\{ g \in L _ { 2 } \left( \mu \right) \vert \operatorname { s u p p } ( g ) = \left\{ x : g ( x ) > 0 \right\} \subset S , 0 \leq g \leq M _ { 0 } , \operatorname { V a r } _ { \mu } ( g ) \geq \varepsilon ^ { 2 } \right\} ,
$$

and

$$
\mathcal { E } ( g , g ) = \frac { 1 } { 2 } \int ( g ( x ) - g ( y ) ) ^ { 2 } T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) ,
$$

with $T ( x , \mathrm { d } y )$ denoting the Markov transition kernel. Moreover, we can define the $( \varepsilon , M _ { 0 } , s )$ -spectral profile Λε,M0s a s

$$
\overline { { \Lambda } } _ { s } ^ { \varepsilon , M _ { 0 } } ( v ) : = \operatorname* { i n f } _ { \mu ( S ) \in ( s , v ] } \Lambda _ { \varepsilon , M _ { 0 } } ( S ) .
$$

Define the ratio density

$$
h _ { k } ( x ) = \frac { \mu _ { k } ( x ) } { \mu ( x ) } .
$$

Note that

$$
\mathbb { E } _ { \mu } [ h _ { k } ] = 1 \quad \mathrm { a n d } \quad \chi ^ { 2 } ( \mu _ { k } , \mu ) = \mathrm { V a r } _ { \mu } ( h _ { k } ) ,
$$

and $h _ { k } ( x ) \leq M _ { 0 }$ for all $k \geq 0$ (see for example, equation (64) of Chen et al. [2020]). By tracking the proof of Lemma 11 in Chen et al. [2020], it suffices to show that for any $k \leq N$ ,

$$
2 \mathcal { E } ( h _ { k } , h _ { k } ) \geq \mathrm { V a r } _ { \mu } ( h _ { k } ) \overline { { \Lambda } } _ { s } ^ { \varepsilon , M _ { 0 } } \Big ( \frac { 4 } { \mathrm { V a r } _ { \mu } ( h _ { k } ) } \Big ) ,
$$

and

$$
\begin{array} { r } { \overline { { \Lambda } } _ { s } ^ { \varepsilon , M _ { 0 } } ( v ) \geq \left\{ \begin{array} { l l } { \frac { \Phi _ { s } ^ { 2 } ( v ) } { 1 6 } } & { \mathrm { ~ f o r ~ a l l ~ } v \in \left[ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } \right] ; } \\ { \frac { \Phi _ { s } ^ { 2 } \left( \frac { 1 } { 2 } \right) } { 6 4 } } & { \mathrm { ~ f o r ~ a l l ~ } v \in ( \frac { 1 } { 2 } , \infty ) , } \end{array} \right. } \end{array}
$$

with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ . We first prove claim (13). Define γk = V $\begin{array} { r } { \gamma _ { k } = \frac { \operatorname { V a r } _ { \mu } \left( h _ { k } \right) } { 4 \mathbb { E } _ { \mu } \left[ h _ { k } \right] } = \frac { \operatorname { V a r } _ { \mu } \left( h _ { k } \right) } { 4 } } \end{array}$ . Then for any $k \leq N$

$$
\begin{array} { r l } & { \mathrm { V a r } _ { \mu } \left( ( h _ { k } - \gamma _ { k } ) _ { + } \right) = \mathbb { E } _ { \mu } \left[ ( ( h _ { k } - \gamma _ { k } ) _ { + } ) ^ { 2 } \right] - ( \mathbb { E } _ { \mu } \left[ ( h _ { k } - \gamma _ { k } ) _ { + } \right] ) ^ { 2 } } \\ & { \overset { ( i ) } { \geq } \mathbb { E } _ { \mu } [ h _ { k } ^ { 2 } ] - 2 \gamma _ { k } \mathbb { E } _ { \mu } [ h _ { k } ] - ( \mathbb { E } _ { \mu } [ h _ { k } ] ) ^ { 2 } } \\ & { = \mathrm { V a r } _ { \mu } ( h _ { k } ) - 2 \gamma _ { k } \mathbb { E } _ { \mu } [ h _ { k } ] } \\ & { = \frac { 1 } { 2 } \mathrm { V a r } _ { \mu } ( h _ { k } ) \geq \varepsilon ^ { 2 } , } \end{array}
$$

where $( x ) _ { + } = \operatorname* { m a x } \{ 0 , x \}$ , $( i )$ is due to $( ( a - b ) _ { + } ) ^ { 2 } \leq a ^ { 2 } - 2 a b , ( a - b ) _ { + } \leq a$ , and the last inequality is due to the assumption that $N < \tau _ { \mathrm { m i x } } ( \sqrt { 2 } \varepsilon , \mu _ { 0 } )$ ; moreover, since for any $\boldsymbol { x } \in \mathbb { R } ^ { d }$ , $0 \leq h _ { k } ( x ) \leq M _ { 0 }$ we can get $( h _ { k } - \gamma _ { k } ) _ { + } \in c _ { \varepsilon , M _ { 0 } } ^ { + } ( \{ h _ { k } > \gamma _ { k } \} )$ , which leads to

$$
\mathcal { E } ( h _ { k } , h _ { k } ) \overset { ( i i ) } { \geq } \mathcal { E } ( ( h _ { k } - \gamma _ { k } ) _ { + } , ( h _ { k } - \gamma _ { k } ) _ { + } ) \geq \mathrm { V a r } _ { \mu } \left( ( h _ { k } - \gamma _ { k } ) _ { + } \right) \cdot \operatorname* { i n f } _ { f \in \epsilon _ { \varepsilon , M _ { 0 } } ^ { + } ( \{ h _ { k } > \gamma _ { k } \} ) } \frac { \mathcal { E } ( f , f ) } { \mathrm { V a r } _ { \mu } ( f ) } ,
$$

where $( i i )$ follows from the fact that $( a - b ) ^ { 2 } = ( a - c - ( b - c ) ) ^ { 2 } \geq ( ( a - c ) _ { + } - ( b - c ) _ { + } ) ^ { 2 }$ . Furthermore, We have for any $k \leq N$ ,

$$
M _ { 0 } ^ { 2 } \mu ( h _ { k } \geq \gamma _ { k } ) \geq \mathbb { E } _ { \mu } [ ( ( h _ { k } - \gamma _ { k } ) _ { + } ) ^ { 2 } ] \geq \mathrm { V a r } _ { \mu } \left( ( h _ { k } - \gamma _ { k } ) _ { + } \right) \geq \frac { 1 } { 2 } \mathrm { V a r } _ { \mu } ( h _ { k } ) \geq \varepsilon ^ { 2 } .
$$

On the other hand, by applying Markov’s inequality, we also have

$$
\mu ( h _ { k } \geq \gamma _ { k } ) \leq { \frac { \mathbb { E } _ { \mu } [ h _ { k } ] } { \gamma _ { k } } } = { \frac { 4 } { \operatorname { V a r } _ { \mu } ( h _ { k } ) } } .
$$

Thus by equation (15), we can get for $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$

$$
\mathcal { E } ( h _ { k } , h _ { k } ) \geq \frac { 1 } { 2 } \operatorname { V a r } _ { \mu } ( h _ { k } ) \overline { { \Lambda } } _ { s } ^ { \varepsilon , M _ { 0 } } \Big ( \frac { 4 } { \operatorname { V a r } _ { \mu } ( h _ { k } ) } \Big ) .
$$

Then we prove claim (14). For $v \in \left[ \frac { 4 } { M _ { 0 } } , \frac { 1 } { 2 } \right]$ , fix any $A \subset \mathbb { R } ^ { d }$ with $s < \mu ( A ) \leq v$ and $g \in { c _ { \frac { \varepsilon } { 2 } , M _ { 0 } } ^ { + } ( A ) }$ Then by

$$
\begin{array} { l } { \displaystyle \mathbb { E } _ { \boldsymbol \mu } \Big [ \int ( g ^ { 2 } ( x ) - g ^ { 2 } ( y ) ) _ { + } T ( x , \mathrm { d } y ) \Big ] } \\ { = \mathbb { E } _ { \boldsymbol \mu } \Big [ \int ( g ^ { 2 } ( x ) - g ^ { 2 } ( y ) ) \mathbf { 1 } ( g ^ { 2 } ( x ) > g ^ { 2 } ( y ) ) T ( x , \mathrm { d } y ) \Big ] } \\ { = \mathbb { E } _ { \boldsymbol \mu } \Big [ \int \int _ { 0 } ^ { + \infty } \mathbf { 1 } ( g ^ { 2 } ( y ) \le t < g ^ { 2 } ( x ) ) \mathrm { d } t T ( x , \mathrm { d } y ) \Big ] } \\ { = \displaystyle \int _ { 0 } ^ { + \infty } \mathbb { E } _ { \boldsymbol \mu } \Big [ \int \mathbf { 1 } ( g ^ { 2 } ( y ) \le t < g ^ { 2 } ( x ) ) T ( x , \mathrm { d } y ) \Big ] \mathrm { d } t , } \end{array}
$$

let $H _ { t } = \{ x \in \mathbb { R } ^ { d } : g ^ { 2 } ( x ) > t \}$ , we have

$$
\begin{array} { r l } & { \displaystyle \int \int | g ^ { 2 } ( x ) - g ^ { 2 } ( y ) | T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } \\ & { \displaystyle \geq \int \int ( g ^ { 2 } ( x ) - g ^ { 2 } ( y ) ) _ { + } T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } \\ & { \displaystyle = \int _ { 0 } ^ { + \infty } \mathbb { E } _ { \mu } \Big [ \int \mathbf { 1 } ( g ^ { 2 } ( y ) \leq t < g ^ { 2 } ( x ) ) T ( x , \mathrm { d } y ) \Big ] \mathrm { d } t } \\ & { \displaystyle = \int _ { 0 } ^ { + \infty } \int _ { x \in H _ { t } } T ( x , H _ { t } ^ { c } ) \mu ( \mathrm { d } x ) \mathrm { d } t . } \end{array}
$$

Let $t ^ { * } = \operatorname* { s u p } \{ t \geq 0 : \mu ( H _ { t } ) > s \}$ , note that $t ^ { * }$ always exists as otherwise, $\mu ( g ( x ) = 0 ) \geq 1 - s$ and thus $\begin{array} { r } { \mathrm { V a r } _ { \mu } ( g ) \leq M _ { 0 } ^ { 2 } s = \frac { \varepsilon ^ { 2 } } { 1 6 } } \end{array}$ , which is contradictory to the requirement that $\begin{array} { r } { \mathrm { V a r } _ { \mu } ( g ) \geq \frac { \varepsilon ^ { 2 } } { 4 } } \end{array}$ . Then

$$
\begin{array} { r l } & { \displaystyle \int \int | g ^ { 2 } ( x ) - g ^ { 2 } ( y ) | T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } \\ & { \displaystyle \geq \int _ { 0 } ^ { + } \int _ { x \subset H _ { t } } T ( x , H _ { \tau } ^ { c } ) \mu ( \mathrm { d } x ) \mathrm { d } t + \int _ { t ^ { * } } ^ { + \infty } \int _ { x \subset H _ { t } } T ( x , H _ { t } ^ { c } ) \mu ( \mathrm { d } x ) \mathrm { d } t } \\ & { \displaystyle \geq \int _ { 0 } ^ { t } \left( \mu ( H _ { t } ) - s \right) \mathrm { d } t \cdot \Phi _ { s } ( \mu ( A ) ) } \\ & { = \left( \mathbb { R } _ { \mu } | g ^ { 2 } | - \int _ { t _ { * } } ^ { + \infty } \mu ( H _ { t } ) \mathrm { d } t - s \right) \cdot \Phi _ { s } ( \mu ( A ) ) } \\ & { \displaystyle \overset { ( i i ) } { \underset { \leq } { \geq } } \left( \mathbb { E } _ { \mu } | g ^ { 2 } | - \frac { s ^ { 2 } } { 8 } \right) \cdot \Phi _ { s } ( \mu ( A ) ) } \\ & { \displaystyle \overset { ( i i i ) } { \underset { \leq } { \geq } } \frac { 1 } { 2 } \mathbb { E } _ { \mu } [ g ^ { 2 } ] \Phi _ { s } ( \mu ( A ) ) , } \end{array}
$$

where $( i i )$ uses the fact that $t ^ { * } \leq M _ { 0 } ^ { 2 }$ and when $t > t ^ { * }$ , $\begin{array} { r } { \mu ( H _ { t } ) \le s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ and $( i i i )$ uses $\mathbb { E } _ { \mu } [ g ^ { 2 } ] \geq$ $\begin{array} { r } { \mathrm { V a r } _ { \mu } ( g ) \geq \frac { \varepsilon ^ { 2 } } { 4 } } \end{array}$ . Moreover, since

$$
\begin{array} { r l } & { \displaystyle \int \displaystyle \int | g ^ { 2 } ( x ) - g ^ { 2 } ( y ) | T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } \\ & { \le \sqrt { \displaystyle \int \int ( g ( x ) - g ( y ) ) ^ { 2 } T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } \cdot \sqrt { \displaystyle \int \int ( g ( x ) + g ( y ) ) ^ { 2 } T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } } \\ & { \le \sqrt { 2 \mathcal { E } ( g , g ) } \cdot \sqrt { \displaystyle \int \int ( 2 g ^ { 2 } ( x ) + 2 g ^ { 2 } ( y ) ) T ( x , \mathrm { d } y ) \mu ( \mathrm { d } x ) } } \\ & { = \sqrt { 2 \mathcal { E } ( g , g ) } \cdot \sqrt { 4 \mathbb { E } _ { \mu } [ g ^ { 2 } ] } , } \end{array}
$$

we have

$$
\begin{array} { r l } & { \quad \displaystyle \frac { 1 } { 2 } \mathbb { E } _ { \mu } [ g ^ { 2 } ] \cdot \Phi _ { s } ( \mu ( A ) ) \leq \sqrt { 2 \mathcal { E } ( g , g ) } \cdot \sqrt { 4 \mathbb { E } _ { \mu } [ g ^ { 2 } ] } } \\ & { \Rightarrow \displaystyle \frac { \mathcal { E } ( g , g ) } { \mathrm { V a r } _ { \mu } ( g ) } \geq \frac { \Phi _ { s } ^ { 2 } ( \mu ( A ) ) } { 1 6 } . } \end{array}
$$

Taking infimum over $A \subset  { \mathbb { R } } ^ { d }$ with $s < \mu ( A ) \leq v$ and $g \in c _ { \frac { \varepsilon } { 2 } , M _ { 0 } } ^ { + } ( A )$ +ε ,M0 (A), we have

$$
\overline { { \Lambda } } _ { s } ^ { \varepsilon , M _ { 0 } } ( v ) \geq \overline { { \Lambda } } _ { s } ^ { \frac { \varepsilon } { 2 } , M _ { 0 } } ( v ) \geq \operatorname* { i n f } _ { s < \mu ( A ) \leq v } \frac { \Phi _ { s } ^ { 2 } ( \mu ( A ) ) } { 1 6 } \geq \frac { \Phi _ { s } ^ { 2 } ( v ) } { 1 6 } .
$$

For the case $\begin{array} { r } { v > \frac { 1 } { 2 } } \end{array}$ , consider any $A \subset \mathbb { R } ^ { d }$ with $\textstyle \mu ( A ) > { \frac { 1 } { 2 } }$ and $g \in c _ { \varepsilon , M _ { 0 } } ^ { + } ( A )$ . Let $0 \leq \gamma \leq M _ { 0 }$ be the number such that

$$
s < \mu ( \{ g > \gamma \} ) \vee \mu ( \{ g < \gamma \} ) \leq \frac { 1 } { 2 } .
$$

$\gamma$ always exists as otherwise, there exists $0 \leq \widetilde { \gamma } \leq M _ { 0 }$ such that $\mu \{ g = \widetilde { \gamma } \} \ge 1 - 2 s$ , which leads to $\operatorname { V a r } _ { \mu } ( g ) \leq \mathbb { E } _ { \mu } [ ( g - \widetilde { \gamma } ) ^ { 2 } ] \leq 2 M _ { 0 } ^ { 2 } s < \varepsilon ^ { 2 }$ e e, and this causes contradiction. We first consider the case that $\mu ( \{ g > \gamma \} ) \land \mu ( \{ g < \gamma \} ) > s$ . We have

$$
\mathcal { E } ( g , g ) = \mathcal { E } ( ( g - \gamma ) , ( g - \gamma ) ) \geq \mathcal { E } ( ( g - \gamma ) _ { + } , ( g - \gamma ) _ { + } ) + \mathcal { E } ( ( g - \gamma ) _ { - } , ( g - \gamma ) _ { - } ) .
$$

Since for any function $h \geq 0$ with $\begin{array} { r } { \mu ( \operatorname { s u p p } ( h ) ) \leq \frac { 1 } { 2 } } \end{array}$ , using Cauchy-Schwarz inequality, it holds that

$$
\mathbb { E } _ { \mu } [ h ^ { 2 } ] = \int _ { x \in \mathrm { s u p p } ( \mathrm { h } ) } h ^ { 2 } ( x ) \mu ( x ) d x \geq \frac { ( \mathbb { E } _ { \mu } [ h ] ) ^ { 2 } } { \mu ( \operatorname { s u p p } ( h ) ) } \geq 2 ( E _ { \mu } [ h ] ) ^ { 2 } ,
$$

which leads to

$$
\operatorname { V a r } _ { \mu } ( h ) \geq { \frac { 1 } { 2 } } \mathbb { E } _ { \mu } [ h ^ { 2 } ] .
$$

Since $\varepsilon ^ { 2 } \le \mathrm { V a r } _ { \mu } ( g ) \le \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ]$ and $\mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] = \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { + } ^ { 2 } ] + \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { - } ^ { 2 } ] ,$ , w.l.o.g, we can assume Eµ[(g − γ)2+] ≥ Eµ[(g−γ)2]2 . Then taking $h = ( g - \gamma ) _ { + }$ , we can obtain

$$
\begin{array} { r l } & { \mathcal { E } ( g , g ) \geq \mathcal { E } ( ( g - \gamma ) _ { + } , ( g - \gamma ) _ { + } ) } \\ & { \qquad \geq \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { + } ^ { 2 } ] \cdot \frac { \mathcal { E } ( ( g - \gamma ) _ { + } , ( g - \gamma ) _ { + } ) } { 2 \mathrm { V a r } _ { \mu } ( ( g - \gamma ) _ { + } ) } } \\ & { \qquad \overset { ( i ) } { \geq } \frac { 1 } { 4 } \mathrm { V a r } _ { \mu } ( g ) \cdot \underset { \mu ( S ) \in ( s , \frac 1 2 ] { f \in \mathcal { E } _ { \frac { + } { 2 } , M _ { 0 } } ^ { \epsilon } ( S ) } } { \mathrm { i n f } } \frac { \mathcal { E } ( f , f ) } { \mathrm { V a r } _ { \mu } ( f ) } } \\ & { \qquad \overset { ( i i ) } { \geq } \frac { 1 } { 6 4 } \mathrm { V a r } _ { \mu } ( g ) \Phi _ { s } ^ { 2 } ( \frac { 1 } { 2 } ) , } \end{array}
$$

where uses (1 $( i )$ uses  The $\begin{array} { r } { \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { + } ^ { 2 } ] \geq \frac { \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] } { 2 } \geq \frac { \operatorname { V a r } _ { \mu } ( g ) } { 2 } } \end{array}$ $\begin{array} { r } { \mathrm { V a r } _ { \mu } ( ( g - \gamma ) _ { + } ) \geq \frac { 1 } { 2 } \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { + } ^ { 2 } ] \geq \frac { \varepsilon ^ { 2 } } { 4 } } \end{array}$ $( i i )$ $\mu ( \{ g > \gamma \} ) \land \mu ( \{ g < \gamma \} ) \leq s < \mu ( \{ g > \gamma \} ) \lor \mu ( \{ g < \gamma \} )$ W.l.o.g, we can assume $\mu ( \{ g > \gamma \} ) > s$ . Then we can obtain

$$
\begin{array} { r l r } {  { \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { + } ^ { 2 } ] = \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] - \mathbb { E } _ { \mu } [ ( g - \gamma ) _ { - } ^ { 2 } ] } } \\ & { } & { \geq \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] - M _ { 0 } ^ { 2 } s = \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] - \frac { \varepsilon ^ { 2 } } { 8 } \geq \frac { \mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] } { 2 } , } \end{array}
$$

where the last inequality is due to $\mathbb { E } _ { \mu } [ ( g - \gamma ) ^ { 2 } ] \geq \operatorname { V a r } _ { \mu } ( g ) \geq \varepsilon ^ { 2 }$ . We can then obtain the desired result by taking infimum over $A \subset  { \mathbb { R } } ^ { d }$ with $\textstyle \mu ( A ) > { \frac { 1 } { 2 } }$ and $g \in c _ { \varepsilon , M _ { 0 } } ^ { + } ( A )$ in (17).

# C.2 Proof of Lemma 4

The proof follows from the standard conductance argument in Chewi et al. [2021], Belloni and Chernozhukov [2009], Dwivedi et al. [2019], Chen et al. [2020]. Let ε216M2 , and let S be any measurable set of $\mathbb { R } ^ { d }$ with $\begin{array} { r } { s \leq \mu ( S ) \leq v \leq \frac { 1 } { 2 } } \end{array}$ . Define the following subsets:

$$
\begin{array} { l } { S _ { 1 } : = \{ x \in S | T ( x , S ^ { c } ) \leq \frac { \omega } { 2 } \} , } \\ { S _ { 2 } : = \{ x \in S ^ { c } | T ( x , S ) \leq \frac { \omega } { 2 } \} , } \\ { S _ { 3 } : = ( S _ { 1 } \cup S _ { 2 } ) ^ { c } , } \end{array}
$$

Then same as the analysis in Chewi et al. [2021], if $\mu ( S _ { 1 } ) \leq \mu ( S ) / 2$ or $\mu ( S _ { 2 } ) < \mu ( S ^ { c } ) / 2$ , then by the fact that $\mu$ is stationary w.r.t the transition kernel $T$ , we have

$$
\begin{array} { r l } { \displaystyle \int _ { S } T ( x , S ^ { c } ) \mu ( \mathrm { d } x ) = \int T ( x , S ) \mu ( \mathrm { d } x ) - \int _ { S } T ( x , S ) \mu ( \mathrm { d } x ) } \\ { = \displaystyle \int _ { S ^ { c } } T ( x , S ) \mu ( \mathrm { d } x ) \geq \frac { \omega } { 2 } \cdot \operatorname* { m a x } \{ \mu ( S \cap S _ { 1 } ^ { c } ) , \mu ( S ^ { c } \cap S _ { 2 } ^ { c } ) \} } \\ { \geq \frac { \omega \cdot \mu ( S ) } { 4 } . } \end{array}
$$

Then when $\mu ( S _ { 1 } ) \land \mu ( S _ { 2 } ) \geq { \frac { \mu ( S ) } { 2 } }$ , consider $x \in E \cap S _ { 1 }$ and $z \in E \cap S _ { 2 }$ , then $\Vert T _ { x } - T _ { z } \Vert _ { \mathrm { T V } } ~ \geq$ $T ( z , S ^ { c } ) - T ( x , S ^ { c } ) \geq 1 - \omega$ , thus $\| x - z \| \geq \psi$ , which implies that $\begin{array} { r } { \operatorname* { i n f } _ { x \in E \cap S _ { 1 } , z \in E \cap S _ { 2 } } \| x - z \| \geq \psi } \end{array}$ . Then consider sets $E \cap K \cap S _ { 1 }$ and $E \cap K \cap S _ { 2 }$ in the log-isoperimetric inequality of $\mu | _ { K }$ , we can obtain that

$$
\begin{array} { r l } & { \mu | _ { K } ( ( ( E \cap K \cap S _ { 1 } ) \cup ( E \cap K \cap S _ { 2 } ) ) ^ { c } ) \geq \lambda \cdot \psi \cdot \operatorname* { m i n } \{ \mu | _ { K } ( E \cap K \cap S _ { 1 } ) , \mu | _ { K } ( E \cap K \cap S _ { 2 } ) \} } \\ & { \qquad \cdot \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \mu | _ { K } ( E \cap K \cap S _ { 1 } ) , \mu | _ { K } ( E \cap K \cap S _ { 2 } ) \} } } \\ & { \qquad \geq \lambda \cdot \psi \cdot \operatorname* { m i n } \{ \mu ( E \cap K \cap S _ { 1 } ) , \mu ( E \cap K \cap S _ { 2 } ) \} } \\ & { \qquad \cdot \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \mu ( E \cap K \cap S _ { 1 } ) , \mu ( E \cap K \cap S _ { 2 } ) \} } \Big ) , } \end{array}
$$

where the last inequality is due to the fact that the function $x \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { x } )$ is an increasing function. W.l.o.g, we can assume $\mu ( E \cap K \cap S _ { 1 } ) \leq \mu ( E \cap K \cap S _ { 2 } )$ , then by $( ( E \cap { \tilde { K } } \cap S _ { 1 } ) \cup ( E \cap K \cap S _ { 2 } ) ) ^ { c } \subseteq$ $E ^ { c } \cup K ^ { c } \cup S _ { 3 }$ and $\begin{array} { r } { \mu ( E ^ { c } ) \le ( \lambda \psi \wedge 1 ) \frac { \varepsilon ^ { 2 } } { 2 5 6 M _ { 0 } ^ { 2 } } = \frac { ( \lambda \psi \wedge 1 ) s } { 1 6 } } \end{array}$ , $\begin{array} { r } { \mu ( K ^ { c } ) \leq \frac { ( \lambda \psi \wedge 1 ) s } { 1 6 } } \end{array}$ , we can obtain

$$
\begin{array} { r l } & { \mu ( S _ { 3 } ) + \frac { 1 6 \lambda \dot { \gamma } \delta } { 1 2 \Gamma } } \\ & { \geq \mu ( S _ { 3 } ) + \frac { \mu ( K ^ { * } ) } { \mu ( K ) } } \\ & { \geq \frac { \mu ( S _ { 3 } ) } { \mu ( K ) } + \frac { \mu ( K ^ { * } ) } { \mu ( K ) } } \\ & { \geq \mu \frac { \mu ( K ) } { \mu ( K ) } } \\ & { \geq \mu \mathrm { l e } ( ( \overline { { L } } \nabla F \Pi \cdot \nabla _ { 1 } ) \cup ( \bar { L } \cap K \cap S _ { 2 } ) ) ^ { c } ) } \\ & { \geq \lambda \cdot \psi \cdot \mu ( { \cal E } \cap { K \cap S _ { 1 } } \setminus \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \mu ( \overline { { \delta } } \Gamma \setminus \bar { K } \cap S _ { 1 } ) } \right) , } \\ & { \overset { ( ) ) } { \geq } \lambda \cdot \psi \cdot \frac { ( \mu ( \overline { { S } } ) ) } { 4 } + \frac { \delta } { 3 } - \frac { \delta } { 8 } \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \frac { \mu ( \overline { { S } } ) } { 4 } + \frac { \delta } { 4 } - \frac { \delta } { 8 } } \right) } \\ & { \geq \lambda \cdot \psi \cdot \frac { \mu ( \overline { { S } } ) } { 4 } \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 4 } { \mu ( \overline { { S } } ) } \right) , } \end{array}
$$

where (i) uses $\mu ( E \cap K \cap S _ { 1 } ) \ : \geq \ : \mu ( S _ { 1 } ) - \mu ( E ^ { c } ) - \mu ( K ^ { c } ) .$ , $\begin{array} { r } { \mu ( S _ { 1 } ) \geq \frac { \mu ( S ) } { 2 } \geq \frac { s } { 2 } } \end{array}$ and the function $x \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { x } )$ is an increasing function. Then by $\mu ( S ) \geq s$ , we can obtain

$$
\mu ( S _ { 3 } ) \geq \lambda \cdot \psi \cdot \frac { \mu ( S ) } { 9 } \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu ( S ) } \Big ) ,
$$

hence

$$
\begin{array} { r l r } & { } & { \displaystyle \int _ { S } T ( x , S ^ { c } ) \mu ( \mathrm { d } x ) \ge \frac { 1 } { 2 } \left( \int _ { S } T ( x , S ^ { c } ) \mu ( \mathrm { d } x ) + \int _ { S ^ { c } } T ( x , S ) \mu ( \mathrm { d } x ) \right) } \\ & { } & { \displaystyle \ge \frac { \omega } { 4 } \mu ( S _ { 3 } ) \ge \frac { \omega \cdot \lambda \cdot \psi } { 3 6 } \cdot \mu ( S ) \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu ( S ) } \Big ) , } \end{array}
$$

which leads to

$$
\frac { \int _ { S } T ( x , S ^ { c } ) \mu ( \mathrm { d } x ) } { \mu ( S ) } \geq \frac { \omega \cdot \lambda \cdot \psi } { 3 6 } \cdot \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 4 } { \mu ( S ) } \Big ) \geq \frac { \omega \cdot \lambda \cdot \psi } { 3 6 } \cdot \log ^ { \frac { 1 } { 2 } } \Big ( 1 + \frac { 1 } { v } \Big ) .
$$

Then combining with the result for the first case, we can obtain a lower bound of

$$
{ \frac { \omega } { 4 } } \operatorname* { m i n } { \Bigl \{ 1 , { \frac { \lambda \cdot \psi } { 9 } } { \sqrt { \log { \bigl ( } 1 + { \frac { 1 } { v } } { \bigr ) } } } \Bigr \} }
$$

on $s$ -conductance profile $\Phi _ { s } ( v )$ with $\begin{array} { r } { s = \frac { \varepsilon ^ { 2 } } { 1 6 M _ { 0 } ^ { 2 } } } \end{array}$ .

# C.3 Proof of Lemma 5

Recall the transition kernel associated with $\mu _ { k }$ ,

$$
T ( \theta , \mathrm { d } y ) = \left[ 1 - ( 1 - \zeta ) \cdot \int A ( \theta , y ) Q ( \theta , y ) \mathrm { d } y \right] \delta _ { \theta } ( \mathrm { d } y ) + ( 1 - \zeta ) \cdot Q ( \theta , y ) A ( \theta , y ) \mathrm { d } y
$$

with

$$
A ( \theta , y ) = 1 \wedge \frac { \pi _ { n } ( y ) Q ( y , \theta ) } { \pi _ { n } ( \theta ) Q ( \theta , y ) } ; \quad Q ( \theta , \cdot ) = N _ { d } \Big ( \theta - \frac { h } { \sqrt { n } } \widetilde { I } \widetilde { \nabla } V _ { n } \big ( \sqrt { n } ( \theta - \widehat { \theta } ) \big ) , \frac { 2 h } { n } \widetilde { I } \Big ) .
$$

Then given $\xi \in \mathbb { R } ^ { d }$ , the distribution of $G _ { \# } T ( \xi , \cdot )$ is

$$
\begin{array} { r l } & { T ^ { * } ( \theta , \mathrm { d } z ) } \\ & { \ = \left[ 1 - ( 1 - \zeta ) \cdot \displaystyle \int Q ^ { * } ( \theta , z ) A \big ( \theta , { \widehat { \theta } } + { \widetilde { I } } ^ { \frac { 1 } { 2 } } \frac { z } { \sqrt { n } } \big ) \mathrm { d } z \right] \delta _ { \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - { \widehat { \theta } } ) } ( \mathrm { d } z ) } \\ & { + ( 1 - \zeta ) \cdot Q ^ { * } ( \theta , z ) A \big ( \theta , { \widehat { \theta } } + { \widetilde { I } } ^ { \frac { 1 } { 2 } } \frac { z } { \sqrt { n } } \big ) \mathrm { d } z , } \end{array}
$$

where $Q ^ { * } ( \theta , \cdot )$ is the density function of $N _ { d } \big ( \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } \big ( \theta - \widehat { \theta } \big ) - h \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } \big ( \sqrt { n } \big ( \theta - \widehat { \theta } \big ) \big ) , 2 h I _ { d } \big )$ . Then by the fact that

$$
\begin{array} { l } { { { \hat { \bf \Pi } } ^ { \mathrm { i } } + { \displaystyle \widetilde { I } } ^ { \mathrm { 1 } } \frac { z } { 2 } \frac { \partial } { \sqrt { n } } , \displaystyle \widehat { \theta } + { \cal \widetilde { I } } ^ { \mathrm { 1 } } \frac { \xi } { 2 } \frac { \delta } { \sqrt { n } } \Big ) = \exp \left( - \displaystyle \frac { 1 } { 4 h } \left( \| \xi - z + h { \widehat { \cal I } } ^ { \mathrm { 1 } } \widetilde { \nabla } V _ { n } ( { \widetilde { I } } ^ { \mathrm { 1 } } z ) \| ^ { 2 } - \| z - \xi + h { \widehat { \cal I } } ^ { \mathrm { 1 } } \widetilde { \nabla } V _ { n } ( { \widetilde { I } } ^ { \mathrm { 1 } } \xi ) \| ^ { 2 } \right) \right) } } \\ { { { \hat { \bf \Pi } } ^ { \mathrm { i } } + { \displaystyle \widetilde { { \cal T } } } ^ { \mathrm { 1 } } \frac { \xi } { 2 } \frac { \partial } { \sqrt { n } } , \displaystyle \widehat { \theta } + { \widetilde { \cal I } } ^ { \mathrm { 1 } } \frac { 2 } { \nabla h } \frac { \delta } { ( \xi ^ { 2 } \xi ) } \frac { 1 } { \sqrt { n } } \Big ) = \exp \left( - \displaystyle \frac { 1 } { 4 h } \left( \| \xi - z + h { \widehat { \cal I } } ^ { \mathrm { 1 } } \widetilde { \nabla } V _ { n } ( { \widetilde { I } } ^ { \mathrm { 1 } } \overline { { { } } } ^ { \mathrm { 1 } } \xi ) \| ^ { 2 } \right) \right) } } \\ { { { \hat { \bf \Pi } } ^ { \mathrm { i } } } } \\ { { { \hat { \bf \Pi } } ^ { \mathrm { Q } } ( \xi , z ) , } } \end{array}
$$

we have

$$
\widehat { \theta } + \widetilde { I } ^ { \frac { 1 } { 2 } } \frac { \xi } { \sqrt { n } } , \mathrm { d } z \Big ) = \left[ 1 - ( 1 - \zeta ) \cdot \int \widetilde { A } ( \xi , z ) \widetilde { Q } ( \xi , z ) \mathrm { d } z \right] \mathbf { 1 } _ { \xi } ( \mathrm { d } z ) + ( 1 - \zeta ) \cdot \widetilde { Q } ( \xi , z ) \widetilde { A } ( \xi , z ) \mathrm { d } z = \widetilde { T } ( \xi , z ) ,
$$

Thus when ${ \widetilde \mu } _ { k - 1 } = G _ { \# } \mu _ { k - 1 }$ , we have ${ \widetilde { \mu } } _ { k } = G _ { \# } \mu _ { k }$ . Then combine with the fact that ${ \widetilde { \mu } } _ { 0 } = G _ { \# } \mu _ { 0 }$ , we can obtain by induction that $\widetilde { \mu } _ { k } = G _ { \# } \mu _ { k }$ for $k \in \mathbb N$ .

# C.4 Proof of Lemma 6

To begin with, we consider the following lemma stated in Chen et al. [2020].

Lemma 12. (Lemma 16 of Chen et al. [2020]) Let $\gamma$ denote the density of the standard Gaussian distribution $\mathcal { N } \left( 0 , \sigma ^ { 2 } I _ { d } \right)$ , and let $\mu$ be a distribution with density $\mu = q \cdot \gamma _ { : }$ , where $q$ is a log-concave function. Then for any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $\mathbb { R } ^ { d }$ , we have

$$
\mu \left( S _ { 3 } \right) \geq \frac { d \left( S _ { 1 } , S _ { 2 } \right) } { 2 \sigma } \operatorname* { m i n } \left\{ \mu \left( S _ { 1 } \right) , \mu \left( S _ { 2 } \right) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \mu \left( S _ { 1 } \right) , \mu \left( S _ { 2 } \right) \right\} } \right) .
$$

We first consider the case $\widetilde { J } = I _ { d }$ where recall $\widetilde J = \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } }$ . Then define $\overline { { \pi } } = N ( 0 , I _ { d } ) | _ { \widetilde { K } }$ , by the fact that $\widetilde { K } = B _ { R / 2 } ^ { d }$ is a convex set and ${ \mathbf { 1 } } _ { \widetilde K }$ eis a log-concave function, using lemma 12, we can obtain that for any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $\widetilde { K }$ , we have

$$
\pi \left( S _ { 3 } \right) \geq \frac { d \left( S _ { 1 } , S _ { 2 } \right) } { 2 } \operatorname* { m i n } \left\{ \pi \left( S _ { 1 } \right) , \pi \left( S _ { 2 } \right) \right\} \log ^ { \frac { 1 } { 2 } } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \pi \left( S _ { 1 } \right) , \pi \left( S _ { 2 } \right) \right\} } \right) .
$$

Then recall πloc|K (ξ) = 1Ke exp(−Vn(Ie12 ξ)) 1 , using the fact that sup $\begin{array} { r } { \left| V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \xi } ) - \frac { 1 } { 2 } \widetilde { \xi } ^ { T } \widetilde { J } \widetilde { \xi } \right| \leq \widetilde { \varepsilon } _ { 0 } } \end{array}$ , we can ξe∈BdR   
obtain that for any measurable set $S \subseteq { \tilde { K } }$ , we have

$$
\exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \leq \frac { \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S ) } { \overline { { \pi } } ( S ) } = \frac { \int _ { S \cap \widetilde { K } } \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) ) \mathrm { d } \xi \int _ { K } \exp ( - \frac { 1 } { 2 } \xi ^ { T } \xi ) \mathrm { d } \xi } { \int _ { S \cap K } \exp ( - \frac { 1 } { 2 } \xi ^ { T } \xi ) \mathrm { d } \xi \int _ { K } \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) ) \mathrm { d } \xi } \leq \exp ( 2 \widetilde { \varepsilon } _ { 0 } ) .
$$

Thus

$$
\begin{array} { r l } & { \mathrm { ~ \zeta _ { l o c } | } _ { \widetilde { K } } ( S _ { 3 } ) \geq \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \overline { { \pi } } ( S _ { 3 } ) } \\ & { \geq \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \{ \pi ( S _ { 1 } ) , \pi ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \pi ( S _ { 1 } ) , \overline { { \pi } } ( S _ { 2 } ) \} } ) } \\ & { \overset { ( i ) } { \geq } \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) , \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) \} } ) } \\ &  \geq \frac { d ( S _ { 1 } , S _ { 2 } ) } { 2 } \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) , \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 2 } ) \} \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { \operatorname* { m i n } \{ \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 1 } ) , \widetilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde { K } } ( S _ { 2 } ) \} } \end{array}
$$

(18) where $( i )$ uses the fact that $x \log ^ { \frac { 1 } { 2 } } ( 1 + \frac { 1 } { x } )$ is an increasing function. For the general case where $\widetilde J$ is not necessary an identity matrix, we can define $K ^ { \prime } = \widetilde { J } ^ { \frac { 1 } { 2 } } \widetilde { K } = \{ x = \widetilde { J } ^ { \frac { 1 } { 2 } } y : y \in \widetilde { K } \}$ , and $\lambda = \widetilde J ^ { \frac { 1 } { 2 } } \xi$ , where $\xi$ is a random variable with density $\pi _ { \mathrm { l o c } } | _ { \widetilde { K } }$ . Thus $\lambda$ has a density

$$
\pi _ { \lambda } ( \lambda ) = \frac { \mathbf { 1 } _ { K ^ { \prime } } ( \lambda ) \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { J } ^ { - \frac { 1 } { 2 } } \lambda ) ) } { \int _ { K ^ { \prime } } \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } J ^ { - \frac { 1 } { 2 } } \lambda ) ) \mathrm { d } \lambda } ,
$$

Moreover, for any $\lambda \in K ^ { \prime }$ , it holds that

$$
\left| V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { J } ^ { - \frac { 1 } { 2 } } \lambda ) - \frac { 1 } { 2 } \lambda ^ { T } \lambda \right| \leq \widetilde { \varepsilon } _ { 0 } .
$$

Then for any partition $S _ { 1 } , S _ { 2 } , S _ { 3 }$ of $\widetilde { K }$ , let

$$
\begin{array} { r } { \widetilde { S _ { 1 } } = \widetilde { J } ^ { \frac { 1 } { 2 } } S _ { 1 } ; } \\ { \widetilde { S _ { 2 } } = \widetilde { J } ^ { \frac { 1 } { 2 } } S _ { 2 } ; } \\ { \widetilde { S _ { 3 } } = \widetilde { J } ^ { \frac { 1 } { 2 } } S _ { 3 } . } \end{array}
$$

Then by the positive definiteness of $\widetilde J$ , $( \widetilde { S _ { 1 } } , \widetilde { S _ { 2 } } , \widetilde { S _ { 3 } } )$ forms a partition for $K ^ { \prime }$ , and

$$
d ( \widetilde { S _ { 1 } } , \widetilde { S _ { 2 } } ) \geq \sqrt { \rho _ { 1 } } d ( S _ { 1 } , S _ { 2 } ) .
$$

Since $K ^ { \prime }$ is a convex set, by applying $\pi _ { \lambda }$ to statement (18), we can obtain

$$
\begin{array} { l } { { \displaystyle | { \tilde { \kappa } } ( S _ { 3 } ) = \pi _ { \lambda } ( \widetilde S _ { 3 } ) \geq \frac { d ( \widetilde S _ { 1 } , \widetilde S _ { 2 } ) } { 2 } \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \left\{ \pi _ { \lambda } ( \widetilde S _ { 1 } ) , \pi _ { \lambda } ( \widetilde S _ { 2 } ) \right\} \log ^ { \frac 1 2 } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ \pi _ { \lambda } ( \widetilde S _ { 1 } ) , \pi _ { \lambda } ( \widetilde S _ { 2 } ) \right\} } \right) } } \\ { { \displaystyle \frac { \sqrt { \rho _ { 1 } } } { 2 } d ( S _ { 1 } , S _ { 2 } ) \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \operatorname* { m i n } \left\{ \pi _ { \mathrm { l o c } } | _ { \widetilde K } \left( S _ { 1 } \right) , \pi _ { \mathrm { l o c } } | _ { \widetilde K } \left( S _ { 2 } \right) \right\} \log ^ { \frac 1 2 } \left( 1 + \frac { 1 } { \operatorname* { m i n } \left\{ { \tilde { \pi } } _ { \mathrm { l o c } } | _ { \widetilde K } \left( S _ { 1 } \right) , \tilde { \pi } _ { \mathrm { l o c } } | _ { \widetilde K } \left( S _ { 2 } \right) \right\} } \right) } } \end{array}
$$

# C.5 Proof of Lemma 7

We first construct the high probability set $E$ as follows: let

$$
r _ { d } = \left( \sqrt { c ^ { \prime } d \left( \log { \left( \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } \right) } + \widetilde { \varepsilon } _ { 0 } \right) } \rho _ { 2 } ^ { 2 } \right) \vee \left( c ^ { \prime } \left( \log { \left( \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } \right) } + \widetilde { \varepsilon } _ { 0 } \right) \rho _ { 2 } ^ { 2 } \right) ,
$$

and $\widetilde J = \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } }$ . We define ${ \cal E } = \{ \xi \in B _ { R / 2 } ^ { d } : \left| \xi ^ { T } \widetilde { J } ^ { 3 } \xi - \mathrm { t r } ( \widetilde { J } ^ { 2 } ) \right| \le r _ { d } \} \cap \{ \xi \in B _ { R / 2 } ^ { d } : \left| \xi ^ { T } \widetilde { J } ^ { 2 } \xi - \mathrm { t r } ( \widetilde { J } ) \right| \le r _ { d } \}$ $r _ { d } / \rho _ { 2 } \}$ . By the choice of $h$ , when $c _ { 0 }$ is small enough, it holds that

$$
h \leq \sqrt { c _ { 0 } } \cdot \left\{ \left( \rho _ { 2 } ^ { - \frac 1 3 } ( \rho _ { 2 } ^ { 2 } d + r _ { d } ) ^ { - \frac 1 3 } \right) \wedge ( r _ { d } ) ^ { - \frac 1 2 } \right\} .
$$

Now we show that $E$ is indeed a high probability set in the following lemma. Note that all the following lemmas in this subsection are under Assumptions in Theorem 1.

$$
\begin{array} { r l } & { 1 3 . \mathrm { ~ } C o n s i d e r \ E = \{ \xi \in B _ { R / 2 } ^ { d } : \left| \xi ^ { T } \widetilde { J } ^ { 3 } \xi - \mathrm { t r } ( \widetilde { J } ^ { 2 } ) \right| \leq r _ { d } \} \cap \{ \xi \in B _ { R / 2 } ^ { d } : \left| \xi ^ { T } \widetilde { J } ^ { 2 } \xi - \mathrm { t r } ( \widetilde { J } ) \right| \leq r _ { d } \} , } \\ & { I f r _ { d } = \left( \sqrt { c ^ { \prime } d \log \left( \frac { M _ { 0 } ^ { 2 } } { \widetilde { e } ^ { 2 } h \rho _ { 1 } } \right) } \rho _ { 2 } ^ { 2 } \right) \vee \left( c ^ { \prime } \log \left( \frac { M _ { 0 } ^ { 2 } } { \widetilde { e } ^ { 2 } h \rho _ { 1 } } \right) \rho _ { 2 } ^ { 2 } \right) f o r \ a s u f f i c i e n t l y \ l a r g e \ e n o u g h \ c o n s t a n t } \\ & { \widetilde { \tau } _ { \mathrm { l o c } } ( E ) \geq 1 - \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { 2 e ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } . } \end{array}
$$

We now show that for any $x , z \in E$ with $\begin{array} { r } { \| x - z \| \le \frac { \sqrt { h } } { 3 } } \end{array}$ h3 , the total variation distance between $\widetilde { T } _ { x } = \widetilde { T } ( x , \cdot )$ and $\widetilde { T } _ { z } = \widetilde { T } ( z , \cdot )$ can be upper bounded by exp(−2εe0)4 . For any x, z ∈ E, we consider the following decomposition:

$$
\begin{array} { r l } & { \| \widetilde { T } _ { x } - \widetilde { T } _ { z } \| _ { T V } } \\ & { \quad = \frac { 1 } { 2 } \displaystyle \int | \widetilde { T } ( x , y ) - \widetilde { T } ( z , y ) | \mathrm { d } y } \\ & { \quad = \frac { 1 } { 2 } \widetilde { T } _ { x } ( \{ x \} ) + \frac { 1 } { 2 } \widetilde { T } _ { z } ( \{ z \} ) | + \frac { 1 } { 2 } \displaystyle \int _ { 2 \pi \widetilde { \epsilon } ( \xi , y ) } | \widetilde { T } ( x , y ) - \widetilde { T } ( z , y ) | \mathrm { d } y } \\ & { \quad - \frac { 1 } { 2 } - \displaystyle \int _ { 2 \pi } \widetilde { \phi } ( z , y ) \widetilde { \lambda } ( x , y ) \mathrm { d } y + \frac { 1 } { 2 } - \frac { 1 - \zeta } { 2 } \displaystyle \int _ { 2 \pi \widetilde { \epsilon } } \widetilde { \phi } ( z , y ) \widetilde { \lambda } ( z , y ) \mathrm { d } y } \\ & { \quad \quad + \frac { 1 - \zeta } { 2 } \displaystyle \int _ { \mathbb { R } ^ { 1 } } \langle \widetilde { Q } ( x , y ) \widetilde { \lambda } ( z , y ) - \widetilde { Q } ( z , y ) \widetilde { \lambda } ( z , y ) \mathrm { d } y } \\ & { \quad = 1 - ( 1 - \zeta ) \displaystyle \int _ { \mathbb { R } ^ { 1 } } \operatorname* { m i n } \Big ( \widetilde { A } ( x , y ) \widetilde { Q } ( x , y ) \widetilde { \lambda } ( z , y ) \widetilde { Q } ( z , y ) \Big ) \mathrm { d } y } \\ & { \quad \le 1 - ( 1 - \zeta ) \displaystyle \int _ { \mathbb { R } ^ { 2 } } \operatorname* { m i n } \Big ( \widetilde { A } ( x , y ) \widetilde { Q } ( x , y ) , \widetilde { A } ( z , y ) \widetilde { Q } ( z , y ) \Big ) \mathrm { d } y } \end{array}
$$

Recall that

$$
\widetilde { A } ( x , y ) = 1 \wedge \frac { \widetilde { \pi } _ { \mathrm { l o c } } ( y ) \widetilde { Q } ( y , x ) } { \widetilde { \pi } _ { \mathrm { l o c } } ( x ) \widetilde { Q } ( x , y ) } ,
$$

where $\widetilde \pi _ { \mathrm { l o c } } ( x ) \propto \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } x ) )$ and

$$
\operatorname* { s u p } _ { x \in B _ { R } ^ { d } } \big | V _ { n } \big ( \widetilde { I } ^ { \frac { 1 } { 2 } } x \big ) - \frac { 1 } { 2 } x ^ { T } \widetilde { J } x \big | \leq \widetilde { \varepsilon } _ { 0 } .
$$

Define $\overline { { \pi } }$ as the density function of $N _ { d } ( 0 , \widetilde { J } ^ { - 1 } )$ , we have

$$
\frac { \widetilde { \pi } _ { \mathrm { l o c } } ( y ) } { \widetilde { \pi } _ { \mathrm { l o c } } ( x ) } = \frac { \exp ( - V _ { n } \widetilde { ( I ^ { \frac { 1 } { 2 } } y ) ) } } { \exp ( - V _ { n } ( \widetilde { I ^ { \frac { 1 } { 2 } } } y ) ) } \geq \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { \exp ( - \frac { 1 } { 2 } y ^ { T } \widetilde { J } y ) } { \exp ( - \frac { 1 } { 2 } x ^ { T } \widetilde { J } x ) } = \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } .
$$

Therefore, denote

$$
\overline { { { A } } } ( x , y ) = 1 \wedge \frac { \overline { { { \pi } } } ( y ) \widetilde { Q } ( y , x ) } { \overline { { { \pi } } } ( x ) \widetilde { Q } ( x , y ) } ,
$$

we have

$$
\widetilde { A } ( x , y ) \geq 1 \land \frac { \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \overline { { \pi } } ( y ) \widetilde { Q } ( y , x ) } { \overline { { \pi } } ( x ) \widetilde { Q } ( x , y ) } \geq \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \overline { { A } } ( x , y ) .
$$

We can then derive

$$
\begin{array} { r l } & { \| \widetilde { T } _ { x } - \widetilde { T } _ { z } \| _ { T V } } \\ & { \le 1 - ( 1 - \zeta ) \int _ { B _ { R } ^ { d } } \operatorname* { m i n } \Big ( \widetilde { A } ( x , y ) \widetilde { Q } ( x , y ) , \widetilde { A } ( z , y ) \widetilde { Q } ( z , y ) \Big ) \ \mathrm { d } y } \\ & { \le 1 - ( 1 - \zeta ) \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \int _ { B _ { R } ^ { d } } \operatorname* { m i n } \Big ( \overline { { A } } ( x , y ) \widetilde { Q } ( x , y ) , \overline { { A } } ( z , y ) \widetilde { Q } ( z , y ) \Big ) \ \mathrm { d } y } \\ & { = 1 - \displaystyle \frac { 1 } { 2 } ( 1 - \zeta ) \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \left( \int _ { B _ { R } ^ { d } } \overline { { A } } ( x , y ) \widetilde { Q } ( x , y ) \mathrm { d } y + \int _ { B _ { R } ^ { d } } \overline { { A } } ( z , y ) \widetilde { Q } ( z , y ) \mathrm { d } y \right. } \\ & { \qquad \Big . - \displaystyle \int _ { B _ { R } ^ { d } } \big \vert \overline { { A } } ( x , y ) \widetilde { Q } ( x , y ) - \widetilde { A } ( z , y ) \widetilde { Q } ( z , y ) \big \vert \ \mathrm { d } y \Big ) } \end{array}
$$

Then consider the inequality:

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { R } ^ { d } } | \widetilde { Q } ( x , y ) \overline { { A } } ( x , y ) - \widetilde { Q } ( z , y ) \overline { { A } } ( z , y ) | \mathrm { d } y \leq \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y } \\ & { \qquad + \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( z , y ) \big ( 1 - \overline { { A } } ( z , y ) \big ) \mathrm { d } y + 2 \| \widetilde { Q } _ { x } - \widetilde { Q } _ { z } \| _ { \mathrm { T V } } , } \end{array}
$$

where we use $\widetilde { Q } _ { x }$ to denote the probability measure with density function $\widetilde Q ( x , \cdot )$ . Moreover, consider the equation:

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { R } ^ { d } } \overline { { A } } ( x , y ) \widetilde { Q } ( x , y ) \mathrm { d } y = \int _ { B _ { R } ^ { d } } ( \overline { { A } } ( x , y ) - 1 ) \widetilde { Q } ( x , y ) \mathrm { d } y + \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) \mathrm { d } y } \\ & { \qquad = 1 - \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y - \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( x , y ) \mathrm { d } y . } \end{array}
$$

Combined with (20), we can obtain

$$
\begin{array} { r l } & { \| \widetilde { T } _ { x } - \widetilde { T } _ { z } \| _ { T V } } \\ & { \le 1 - ( 1 - \zeta ) \exp ( - 2 \widetilde { \varepsilon } _ { 0 } ) \cdot \bigg ( 1 - \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y - \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( z , y ) ( 1 - \overline { { A } } ( z , y ) ) \mathrm { d } y } \\ & { \qquad - \| \widetilde { Q } _ { x } - \widetilde { Q } _ { z } \| _ { \mathrm { T V } } - \frac { 1 } { 2 } \displaystyle \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( x , y ) \mathrm { d } y - \frac { 1 } { 2 } \displaystyle \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( z , y ) \mathrm { d } y \bigg ) } \end{array}
$$

Consider the proposal distribution of MALA for sampling from the Gaussian $\overline { { \pi } } : = N _ { d } ( 0 , \widetilde J ^ { - 1 } )$

$$
Q _ { x } ^ { \Delta } ( \cdot ) = N _ { d } ( x - h \widetilde { J } x , 2 h I _ { d } ) ,
$$

whose density is denoted as $Q ^ { \Delta } ( x , \cdot )$ . Then $\lVert \widetilde { Q } _ { x } - \widetilde { Q } _ { z } \rVert _ { \mathrm { T V } } \leq \lVert \widetilde { Q } _ { x } - Q _ { x } ^ { \Delta } \rVert _ { \mathrm { T V } } + \lVert Q _ { x } ^ { \Delta } - Q _ { z } ^ { \Delta } \rVert _ { \mathrm { T V } } + \lVert \widetilde { Q } _ { z } -$ $Q _ { z } ^ { \Delta } \| _ { \mathrm { T V } }$ can be upper bounded by Pinsker’s inequality, that is, for any $x \in B _ { R } ^ { d }$ ,

$$
\| \widetilde { Q } _ { x } - Q _ { x } ^ { \Delta } \| _ { \mathrm { T V } } \leq \frac { 1 } { 2 } \sqrt { \frac { h ^ { 2 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } x ) - \widetilde { J } x \| ^ { 2 } } { 2 h } } \leq \frac { \sqrt { h } \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } } { 2 \sqrt { 2 } } ,
$$

and for any $x , z \in B _ { R } ^ { d }$

$$
\| Q _ { x } ^ { \Delta } - Q _ { z } ^ { \Delta } \| _ { \mathrm { T V } } \leq \frac { 1 } { 2 } \sqrt { \frac { \| ( I - h \widetilde { J } ) ( x - z ) \| ^ { 2 } } { 2 h } } \leq \frac { \| x - z \| } { 2 \sqrt { 2 h } } .
$$

Therefore, when $\begin{array} { r } { \| x - z \| \leq \frac { \sqrt { h } } { 3 } } \end{array}$ and $\begin{array} { r } { \sqrt { h } \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \leq \frac { \sqrt { 2 } } { 3 6 } } \end{array}$ , we have

$$
\| \widetilde { Q } _ { x } - \widetilde { Q } _ { z } \| _ { \mathrm { T V } } \leq \frac { \| x - z \| } { 2 \sqrt { 2 h } } + \frac { \sqrt { h } \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } } { \sqrt { 2 } } < \frac { 1 } { 6 } .
$$

For the term of $\begin{array} { r } { \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y } \end{array}$ , we use Condition A by comparing $Q _ { x }$ with $Q _ { x } ^ { \Delta }$ , leading to the following decomposition:

$$
\begin{array} { r l } & { \int _ { B _ { R } ^ { d } } \tilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y } \\ & { \leq \int _ { B _ { R } ^ { d } } \Big | \tilde { Q } ( x , y ) - \frac { \overline { { \pi } } ( y ) \widetilde { Q } ( y , x ) } { \overline { { \pi } } ( x ) } \Big | \mathrm { d } y } \\ & { \leq 2 \| \tilde { Q } _ { x } - Q _ { x } ^ { \Delta } \| _ { \mathrm { T V } } + \underbrace { \displaystyle \prod \left| Q ^ { \Delta } ( x , y ) - \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) } \right| \mathrm { d } y } _ { \mathrm { ( A ) } } + \underbrace { \int _ { B _ { R } ^ { d } } \left| \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) } - \frac { \overline { { \pi } } ( y ) \widetilde { Q } ( y , x ) } { \overline { { \pi } } ( x ) } \right| } _ { \mathrm { ( R ) } } . } \end{array}
$$

We then state the following lemma for bounding the term (A).

Lemma 14. Consider the choice of (rescaled) step size $h$ in Theorem $\cdot$ , then when $c _ { 0 }$ is small enough and $x \in E$ , it holds that

$$
\int \left| Q ^ { \Delta } ( x , y ) - \frac { \overline { { { \pi } } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { { \pi } } } ( x ) } \right| \mathrm { d } y \leq \frac { 1 } { 2 4 } .
$$

Our proof of Lemma 14 is technically similar to that of Proposition 38 in Chewi et al. [2021] for bounding the mixing time of MALA with a standard Gaussian target (i.e. $\overline { { \pi } } = N _ { d } ( 0 , I _ { d } ) )$ . The nontrivial part in our analysis lies in keeping track of the dependence on the maximal and minimal eigenvalues of $J$ . We then bound the term (B) by the following lemma.

Lemma 15. Consider the choice of (rescaled) step size $h$ in Theorem $\cdot$ , then when $c _ { 0 }$ is small enough, for any $x \in E$ , it holds that

$$
\int _ { B _ { R } ^ { d } } \left| Q ^ { \Delta } ( y , x ) - Q ( y , x ) \right| \frac { \overline { { { \pi } } } ( y ) } { \overline { { { \pi } } } ( x ) } \mathrm { d } y \leq \frac { 1 } { 7 2 } .
$$

Thus when $\begin{array} { r } { \| x - z \| \leq \frac { \sqrt { h } } { 3 } } \end{array}$ and $\begin{array} { r } { \sqrt { h } \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \leq \frac { \sqrt { 2 } } { 3 6 } } \end{array}$

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y } \\ & { \le 2 \| \widetilde { Q } _ { x } - Q _ { x } ^ { \Delta } \| _ { \mathrm { T V } } + \frac { 1 } { 2 4 } + \frac { 1 } { 7 2 } } \\ & { \le \sqrt { \displaystyle \frac { h } { 2 } } \widetilde { \varepsilon } _ { 1 } \| \widetilde { I } ^ { \frac 1 2 } \| _ { \mathrm { o p } } + \frac { 1 } { 1 8 } \le \frac { 1 } { 1 2 } . } \end{array}
$$

$x \in E \subset B _ { R / 2 } ^ { d }$

$$
\begin{array} { r l r } & { } & { \displaystyle { \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( x , y ) \mathrm { d } y } \le \int _ { ( B _ { R } ^ { d } ) ^ { c } } Q ^ { \Delta } ( x , y ) \mathrm { d } y + 2 \| \widetilde { Q } _ { x } - Q _ { x } ^ { \Delta } \| _ { \mathrm { T V } } } \\ & { } & { \le \mathbb { E } _ { u \in N _ { d } ( 0 , I _ { d } ) } \Big [ { \mathbf 1 } \big ( \| u \| \ge \frac { R } { 2 \sqrt { 2 h } } \big ) \Big ] + \frac { \sqrt { h } \widetilde { \varepsilon } _ { 1 } \| \Gamma ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } } { \sqrt { 2 } } . } \end{array}
$$

Since $R \geq 8 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( \widetilde J ) }$ , when the constant $c _ { 0 }$ in $h$ is small enough, we can obtain

$$
\int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( x , y ) \mathrm { d } y \leq \frac { 1 } { 6 } .
$$

Then combined with the bound in equation (21) and decomposition (20), we can obtain that when $c _ { 0 }$ is small enough, for any $x , z \in E$ with $\begin{array} { r } { \| x - z \| < \frac { \sqrt { h } } { 3 } } \end{array}$ and $\zeta \in ( 0 , \frac { 1 } { 2 } ]$ , it holds that

$$
\begin{array} { r l } & { \| T _ { x } - \bar { T } _ { z } \| _ { T V } } \\ & { \leq 1 - ( 1 - \zeta ) \exp ( - 2 \tilde { \varepsilon } _ { 0 } ) \cdot \bigg ( 1 - \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( x , y ) ( 1 - \overline { { A } } ( x , y ) ) \mathrm { d } y - \displaystyle \int _ { B _ { R } ^ { d } } \widetilde { Q } ( z , y ) ( 1 - \overline { { A } } ( z , y ) ) \mathrm { d } z } \\ & { \qquad - \| \widetilde { Q } _ { x } - \widetilde { Q } _ { z } \| _ { \mathrm { T V } } - \frac { 1 } { 2 } \displaystyle \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( x , y ) \mathrm { d } y - \frac { 1 } { 2 } \displaystyle \int _ { ( B _ { R } ^ { d } ) ^ { c } } \widetilde { Q } ( z , y ) \mathrm { d } y \bigg ) } \\ & { \leq 1 - \displaystyle \frac { 1 - \zeta } { 2 } \exp ( - 2 \tilde { \varepsilon } _ { 0 } ) } \\ & { \leq 1 - \displaystyle \frac { \exp ( - 2 \tilde { \varepsilon } _ { 0 } ) } { 4 } . } \end{array}
$$

# C.6 Proof of Lemma 13

We can write $\widetilde { \pi } _ { \mathrm { l o c } }$ as

$$
\widetilde { \pi } _ { \mathrm { l o c } } ( \xi ) = \frac { \frac { \sqrt { \operatorname* { d e t } ( \widetilde { J } ) } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) ) } { \int \frac { \sqrt { \operatorname* { d e t } ( \widetilde { J } ) } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \xi ) ) \mathrm { d } \xi } .
$$

Then

$$
\begin{array} { r l } & { 1 - \widetilde { \pi } _ { \mathrm { l o c } } ( E ) \leq \frac { \displaystyle \int _ { \left\{ \xi \in B _ { \scriptscriptstyle { R / 2 } } ^ { d } : | \xi ^ { T } \widetilde { \mathcal { I } } ^ { 3 } \xi - \mathrm { i } \tau ( \widetilde { \mathcal { I } } ^ { 2 } ) | > r _ { d } \right\} } \frac { \sqrt { \operatorname* { d e t } \langle \widetilde { \mathcal { I } } \rangle } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { 1 } \xi ) ) \mathrm { d } \xi } { \displaystyle \int _ { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { 1 } \xi ) ) \mathrm { d } \xi } } \\ & { \qquad + \frac { \displaystyle \int _ { \left\{ \xi \in B _ { \scriptscriptstyle { R / 2 } } ^ { d } : | \xi ^ { T } \widetilde { \mathcal { I } } ^ { 3 } \xi - \mathrm { i } \tau ( \widetilde { \mathcal { I } } ) | > r _ { d } / \rho _ { 2 } \right\} } \frac { \sqrt { \operatorname* { d e t } \langle \widetilde { \mathcal { I } } \rangle } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { 1 } \xi ) ) \mathrm { d } \xi } { \displaystyle \int _ { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - V _ { n } ( \widetilde { I } ^ { 1 } \xi ) ) \mathrm { d } \xi } } \\ & { \qquad + \widetilde { \pi } _ { \mathrm { l o c } } ( \| \xi \| > R / 2 ) . } \end{array}
$$

Then for the denominator, as

$$
\operatorname* { s u p } _ { \widetilde { \xi } \in B _ { R } ^ { d } } \big | V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \xi } ) - \frac { 1 } { 2 } \widetilde { \xi } ^ { T } \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \xi } \big | \leq \widetilde { \varepsilon } _ { 0 } ,
$$

when $R \geq 8 ( \frac { d } { \lambda _ { \operatorname* { m i n } } ( \widetilde J ) } ) ^ { \frac 1 2 }$ , we can obtain that

$$
\begin{array} { r l } & { \int \frac { \sqrt { \operatorname* { d e t } ( \widetilde { \mathcal { I } } ) } } { ( 2 \pi ) ^ { \frac { j } { L } } } \exp ( V _ { n } ( \widetilde { I } ^ { - \frac { 1 } { 2 } } \xi ) ) \mathrm { d } \xi } \\ & { \geq \displaystyle \int _ { B _ { n } ^ { \frac { j } { L } } } \frac { \sqrt { \operatorname* { d e t } ( \widetilde { \mathcal { I } } ) } } { ( 2 \pi ) ^ { \frac { j } { L } } } \exp ( - \frac { \xi ^ { l } / \widetilde { \mathcal { J } } } { 2 } ) \exp ( \frac { \xi ^ { T } / \widetilde { \mathcal { J } } _ { \xi } } { 2 } - V _ { n } ( I ^ { \frac { 1 } { 2 } } \xi ) ) \mathrm { d } \xi } \\ & { \geq \exp ( - \widetilde { \varepsilon } _ { 0 } ) \displaystyle \int _ { B _ { n } ^ { \frac { j } { R } } } \frac { \sqrt { \operatorname* { d e t } ( \widetilde { \mathcal { I } } ) } } { ( 2 \pi ) ^ { \frac { j } { L } } } \exp ( - \frac { \xi ^ { T } / \widetilde { \mathcal { J } } _ { \xi } } { 2 } ) \mathrm { d } \xi } \\ & { \geq \frac { 1 } { 2 } \exp ( - \widetilde { \varepsilon } _ { 0 } ) . } \end{array}
$$

Furthermore, by Bernstein’s inequality (see for example, Theorem 2.8.2 of Vershynin [2018]), for $x \sim$ $N _ { d } ( 0 , \Sigma )$ , it holds that

$$
\mathbb { P } ( \left| \| x \| ^ { 2 } - \operatorname { t r } ( \Sigma ) \right| \geq t ) \leq 2 \exp ( - \frac { 1 } { 8 } ( \frac { t ^ { 2 } } { \| \Sigma \| _ { \mathrm { F } } ^ { 2 } } \land \frac { t } { \| \Sigma \| _ { \mathrm { o p } } } ) )
$$

We can then obtain

$$
\begin{array} { r l } & { \pi _ { \mathrm { l o c } } ( E ) \geq 1 - 2 \exp ( 2 \widetilde { \varepsilon } _ { 0 } ) \displaystyle \int _ { \left\{ | \xi ^ { T } \widetilde { \jmath } ^ { 3 } \xi - \mathrm { t r } ( \widetilde { \jmath } ^ { 2 } ) | > r _ { d } \right\} } \frac { \sqrt { \operatorname* { d e t } ( \widetilde { \jmath } ) } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - \frac { \xi ^ { T } \widetilde { \jmath } \xi } { 2 } ) \mathrm { d } \xi } \\ & { \qquad - 2 \exp ( 2 \widetilde { \varepsilon } _ { 0 } ) \displaystyle \int _ { \left\{ | \xi ^ { T } \widetilde { \jmath } ^ { 2 } \xi - \mathrm { t r } ( \widetilde { \jmath } ) | > r _ { d } / \rho _ { 2 } \right\} } \frac { \sqrt { \operatorname* { d e t } ( \widetilde { \jmath } ) } } { ( 2 \pi ) ^ { \frac { d } { 2 } } } \exp ( - \frac { \xi ^ { T } \widetilde { \jmath } \xi } { 2 } ) \mathrm { d } \xi - \frac { \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } } \\ & { \geq 1 - \exp ( - 4 \widetilde { \varepsilon } _ { 0 } ) \cdot \frac { 2 \varepsilon ^ { 2 } h \rho _ { 1 } } { M _ { 0 } ^ { 2 } } , } \end{array}
$$

where the last inequality is due to the Bernstein’s inequality in (22).

# C.7 Proof of Lemma 14

Recall $\overline { { \pi } } = N _ { d } ( 0 , \widetilde { J } ^ { - 1 } )$ and $Q ^ { \Delta } ( x , \cdot )$ be the density of $N _ { d } ( x - h \widetilde { J } x , 2 h I _ { d } )$ , we have

$$
\begin{array} { r l } & { \displaystyle \int \left| Q ^ { \Delta } ( x , y ) - \frac { \overline { \pi } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { \pi } ( x ) } \right| \mathrm { d } y } \\ & { = \displaystyle \int \frac { 1 } { ( 4 \pi h ) ^ { \frac { d } { 2 } } } \left| \exp \left( - \frac { \| y - x + h \tilde { J } x \| ^ { 2 } } { 4 h } \right) - \exp \left( \frac { x ^ { T } \tilde { J } x - y ^ { T } \tilde { J } y } { 2 } \right) \exp \left( - \frac { \| x - y + h \tilde { J } y \| ^ { 2 } } { 4 h } \right) \right| } \\ & { = \displaystyle \int \frac { 1 } { ( 4 \pi h ) ^ { \frac { d } { 2 } } } \exp \left( - \frac { \| y - x + h \tilde { J } x \| ^ { 2 } } { 4 h } \right) \left| 1 - \exp \left( \frac { h ^ { 2 } \| \tilde { J } x \| ^ { 2 } - h ^ { 2 } \| \tilde { J } y \| ^ { 2 } } { 4 h } \right) \right| \mathrm { d } y , } \end{array}
$$

$\begin{array} { r } { u = \frac { y - x + h \widetilde { J } x } { \sqrt { 2 h } } } \end{array}$ in the above integral, then consider $u \sim N _ { d } ( 0 , I _ { d } )$ and let

$$
A = \{ u \in \mathbb { R } ^ { d } : { \frac { 1 } { 4 } } | 2 h ^ { 2 } \| { \tilde { J } } u \| ^ { 2 } + 2 { \sqrt { 2 } } h ^ { { \frac { 3 } { 2 } } } x ^ { T } { \tilde { J } } ^ { 2 } u - 2 { \sqrt { 2 } } h ^ { { \frac { 5 } { 2 } } } x ^ { T } { \tilde { J } } ^ { 3 } u + h ^ { 3 } x ^ { T } { \tilde { J } } ^ { 4 } x - 2 h ^ { 2 } x ^ { T } { \tilde { J } } ^ { 3 } x | \leq { \frac { 1 } { 4 9 } }
$$

We can then obtain

$$
\begin{array} { r l } & { \bigg | \int \bigg | Q ^ { \Delta } ( x , y ) - \frac { \pi ( y ) Q ^ { \Delta } ( y , x ) } { \pi ( x ) } \bigg | ~ \mathrm { d } y } \\ & { = \mathbb { E } _ { x } [ \bigg | 1 - \exp ( \frac { - h ^ { 2 } \| \sqrt { 2 h } \tilde { J } ^ { \Delta } ( y + \tilde { J } ^ { \Delta } x ) - h \tilde { J } ^ { \Delta } x \| ^ { 2 } + h ^ { 2 } \| \tilde { J } ^ { \Delta } x \| ^ { 2 } } { 4 h } ) \bigg | ] } \\ & { = \mathbb { E } _ { x } [ \bigg | 1 - \exp ( - \frac { 1 } { \lambda } ( 2 h ^ { 2 } \| \tilde { J } _ { M } \| ^ { 2 } + 2 \sqrt { 2 h } \frac { 3 } { 2 x } x ^ { 2 } \tilde { J } ^ { 2 } \tilde { u } - 2 \sqrt { 2 } h \frac { 5 } { 2 x } x ^ { 2 } \tilde { J } ^ { 3 } \tilde { u } + h ^ { 3 } x ^ { T } \tilde { J } ^ { 4 } x - 2 h ^ { 2 } x ^ { T } \tilde { \mathcal { P } } x )  \bigg . \bigg . \bigg . } \\ & { \leq \bigg \{ \mathbb { E } _ { u } \bigg [ \bigg | 1 - \exp \bigg ( - \frac { 1 } { \lambda } ( 2 h ^ { 2 } \| \tilde { J } _ { M } \| ^ { 2 } + 2 \sqrt { 2 h } \frac { 3 } { 2 x } x ^ { 2 } \tilde { J } ^ { 2 } \tilde { u } - 2 \sqrt { 2 } h \frac { 5 } { 2 x } x ^ { 2 } \tilde { J } ^ { 3 } \tilde { u } + h ^ { 3 } x ^ { T } \tilde { \mathcal { P } } \tilde { \mathcal { A } } _ { x } - 2 h ^ { 2 } x ^ { T } \tilde { \mathcal { P } } x _ { x }  \bigg . \bigg . } \\ & {    \mathrm { ~ \ f } _ { M } ( u ) ] \bigg \} + \{ \mathbb { E } _ { u } [ 1 . \kappa ( u ) ] \} + \bigg \{ \exp ( - \frac { 1 } { \lambda } h ^ { 3 } x ^ { \mathcal { P } / \tilde { J } } \frac { 3 } { \kappa } ) \sqrt { \mathbb { E } _ { u } [ 1 . 4 \kappa ( u ) ] } } \\ &  \bigg . \bigg . \bigg \{ \mathbb { E } _ { x } [ \exp ( - 3 h ^ { 2 } ( 2 u ^ { T } \tilde { J } ^ { 2 } u - x ^ { T } \ \end{array}
$$

where the last inequality uses Holder inequality. The first term of the right hand side of equation ( ¨ 23) can be upper bound by $\exp ( 1 / 4 9 ) - 1 \leq 1 / 4 8 .$ . For the second and third term, by $( 1 ) h \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - \frac 1 3 } ( \mathrm { t r } ( \widetilde { J } ^ { 2 } ) + r _ { d } ) ^ { - \frac 1 3 }$ and $h \leq \sqrt { c _ { 0 } } r _ { d } ^ { - \frac 1 2 }$ with $\begin{array} { r } { r _ { d } = \left\{ \left( \sqrt { c ^ { \prime } \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } } \| \widetilde { J } ^ { 2 } \| _ { \mathrm { F } } \right) \vee \left( c ^ { \prime } \log \frac { M _ { 0 } ^ { 2 } } { \varepsilon ^ { 2 } h \rho _ { 1 } } \rho _ { 2 } ^ { 2 } \right) \right\} \wedge ( \rho _ { 2 } ^ { 3 } \| K \| ^ { 2 } ) } \end{array}$ and $\| K \| \geq$ $C ( \textstyle { \frac { d } { \rho _ { 1 } } } ) ^ { \frac { 1 } { 2 } }$ ; (2) $x \in E = \{ x \in K : | x ^ { T } \widetilde { J } ^ { 3 } x - \mathrm { t r } ( \widetilde { J } ^ { 2 } ) | \leq r _ { d } \}$ , it holds that

$$
h ^ { 3 } x ^ { T } \widetilde { J } ^ { 4 } x \le h ^ { 3 } \rho _ { 2 } x ^ { T } \widetilde { J } ^ { 3 } x \le h ^ { 3 } \rho _ { 2 } ( r _ { d } + \mathrm { t r } ( \widetilde { J } ^ { 2 } ) ) \le c _ { 0 } ^ { \frac 3 2 } .
$$

Moreover, since for a Gaussian random variable $\bar { u } \sim N ( 0 , \sigma ^ { 2 } )$ , it holds that

$$
\begin{array} { r l } & { \mathbb { E } \exp ( t \bar { u } ) = \exp ( \frac { \sigma ^ { 2 } t ^ { 2 } } { 2 } ) } \\ & { \mathbb { E } \exp ( - t ^ { 2 } \bar { u } ^ { 2 } ) = \displaystyle \frac { 1 } { \sqrt { 1 + 2 t ^ { 2 } \sigma ^ { 2 } } } \quad | t | < \sqrt { \frac { 1 } { 2 \sigma ^ { 2 } } } . } \end{array}
$$

We can get

$$
\begin{array} { r l } & { \mathbb { E } _ { u } \left[ \exp ( t ^ { 2 } h ^ { 2 } ( x ^ { T } \widetilde { \mathcal { P } } ^ { 3 } x - \| \widetilde { \mathcal { I } } u \| ^ { 2 } ) ) \right] } \\ & { \le \exp ( t ^ { 2 } h ^ { 2 } ( x ^ { T } \widetilde { \mathcal { P } } ^ { 3 } x - \mathrm { t r } ( \widetilde { \mathcal { P } } ^ { 2 } ) ) ) \displaystyle \prod _ { j = 1 } ^ { d } \frac { 1 / \sqrt { 1 + 2 t ^ { 2 } h ^ { 2 } \lambda _ { j } ( \widetilde { \mathcal { P } } ^ { 2 } ) } } { \exp \big ( - t ^ { 2 } h ^ { 2 } \lambda _ { j } ( \widetilde { \mathcal { P } } ^ { 2 } ) \big ) } } \\ & { \le \exp ( t ^ { 2 } h ^ { 2 } r _ { d } ) \cdot \displaystyle \prod _ { j = 1 } ^ { d } \big ( 1 + C t ^ { 4 } h ^ { 4 } ( \lambda _ { j } ( \widetilde { \mathcal { P } } ^ { 2 } ) ) ^ { 2 } \big ) } \\ & { \le \exp ( t ^ { 2 } c _ { 0 } ) \exp ( C t ^ { 4 } h ^ { 4 } \| \widetilde { \mathcal { P } } ^ { 2 } \| _ { \mathrm { t r } } ^ { 2 } ) } \\ & { \le \exp ( t ^ { 2 } c _ { 0 } + t ^ { 4 } C c _ { 0 } ^ { 2 } ) , \quad | t | \le \sqrt { \frac { 1 } { 4 h ^ { 2 } \rho _ { 2 } ( \widetilde { \mathcal { P } } ^ { 2 } ) } } , } \end{array}
$$

where the last inequality uses $h \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - \frac 1 3 } ( \mathrm { t r } ( \widetilde { J } ^ { 2 } ) + r _ { d } ) ^ { - \frac 1 3 } \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - \frac 1 3 } ( \mathrm { t r } ( \widetilde { J } ^ { 2 } ) ) ^ { - \frac 1 3 } \leq \sqrt { c _ { 0 } } \| \widetilde { J } ^ { 2 }$ ∥ − 12F , and

$$
\left[ \exp ( t h ^ { \frac { 3 } { 2 } } x ^ { T } \widetilde { J } ^ { 2 } u ) \right] \le \exp \left( \frac { 1 } { 2 } t ^ { 2 } h ^ { 3 } \| x ^ { T } \widetilde { J } ^ { 2 } \| ^ { 2 } \right) \le \exp \left( \frac { 1 } { 2 } t ^ { 2 } h ^ { 3 } \rho _ { 2 } ( \operatorname { t r } ( \widetilde { J } ^ { 2 } ) + r _ { d } ) \right) \le \exp \left( \frac { 1 } { 2 } c _ { 0 } ^ { \frac { 3 } { 2 } } t ^ { 2 } \right) ;
$$

$\mathbb { E } _ { u } \left[ \exp ( t h ^ { \frac { 5 } { 2 } } x ^ { T } \widetilde { \mathcal { I } } ^ { 3 } u ) \right] \leq \exp \left( \frac { 1 } { 2 } t ^ { 2 } h ^ { 5 } \| x ^ { T } \widetilde { \mathcal { I } } ^ { 3 } \| ^ { 2 } \right) \leq \exp \left( \frac { 1 } { 2 } t ^ { 2 } h ^ { 5 } \rho _ { 2 } ^ { 3 } ( \operatorname { t r } ( \widetilde { \mathcal { I } } ^ { 2 } ) + r _ { d } ) \right) \leq \exp ( \frac { 1 } { 2 } c _ { 0 } ^ { \frac { 5 } { 2 } } t ^ { 2 } \rho _ { 1 } ^ { 3 } ( \operatorname { t r } ( \widetilde { \mathcal { I } } ^ { 3 } ) + r _ { d } ) ) .$ ) , where the last inequality uses $h \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - \frac 1 3 } ( \mathrm { t r } ( \widetilde { J } ^ { 2 } ) + r _ { d } ) ^ { - \frac 1 3 } \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - 1 }$ . Then by Markov inequality, we can obtain that

$$
\begin{array} { r l } & { \mathbb { P } _ { u } \left( | h ^ { \frac { 3 } { 2 } } x ^ { T } \widetilde { J } ^ { 2 } u | \ge \frac { 1 } { 9 6 \sqrt { 2 } } \right) \le 2 \operatorname* { i n f } \exp \left( \frac { 1 } { 2 } c _ { 0 } ^ { \frac { 3 } { 2 } } t ^ { 2 } - \frac { t } { 9 6 \sqrt { 2 } } \right) = 2 \exp \left( - \frac { 1 } { 2 \cdot ( 9 6 \sqrt { 2 } ) ^ { 2 } c _ { 0 } ^ { \frac { 3 } { 2 } } } \right) ; } \\ & { \mathbb { P } _ { u } \left( | h ^ { \frac { 5 } { 2 } } x ^ { T } \widetilde { J } ^ { 3 } u | \ge \frac { 1 } { 9 6 \sqrt { 2 } } \right) \le 2 \operatorname* { i n f } \exp \left( \frac { 1 } { 2 } c _ { 0 } ^ { \frac { 5 } { 2 } } t ^ { 2 } - \frac { t } { 9 6 \sqrt { 2 } } \right) = 2 \exp \left( - \frac { 1 } { 2 \cdot ( 9 6 \sqrt { 2 } ) ^ { 2 } c _ { 0 } ^ { \frac { 5 } { 2 } } } \right) . } \end{array}
$$

Also, by Bernstein’s inequality in (22), we have

$$
\begin{array} { r l } & { \mathbb { P } _ { u } \left( h ^ { 2 } \left| \| \tilde { \mathcal { I } } u \| ^ { 2 } - x ^ { T } \tilde { \mathcal { I } } ^ { 3 } x \right| \geq \frac { 1 } { 9 6 } \right) \leq P _ { u } \left( \left| \| \tilde { \mathcal { I } } u \| ^ { 2 } - \mathrm { t r } ( \tilde { \mathcal { I } } ^ { 2 } ) \right| \geq \frac { 1 } { 9 6 h ^ { 2 } } - r _ { d } \right) } \\ & { \qquad \leq P _ { u } \left( \left| \| \tilde { \mathcal { I } } u \| ^ { 2 } - \mathrm { t r } ( \tilde { \mathcal { I } } ^ { 2 } ) \right| \geq \frac { 1 } { h ^ { 2 } } ( \frac { 1 } { 9 6 } - c _ { 0 } ) \right) } \\ & { \qquad \leq 2 \exp \left( - \frac { 1 } { c ^ { \prime } } \left( \frac { \frac { 1 } { 9 6 } - c _ { 0 } } { h ^ { 2 } \rho _ { 2 } ^ { 2 } } \wedge \frac { \left( \frac { 1 } { 9 6 } - c _ { 0 } \right) ^ { 2 } } { h ^ { 4 } \| \tilde { \mathcal { I } } ^ { 2 } \| _ { F } ^ { 2 } } \right) \right) } \\ & { \qquad \leq 2 \exp \left( - \frac { 1 } { c ^ { \prime } } \left( \frac { \frac { 1 } { 9 6 } - c _ { 0 } } { c _ { 0 } } \wedge \frac { \left( \frac { 1 } { 9 6 } - c _ { 0 } \right) ^ { 2 } } { c _ { 0 } ^ { 2 } } \right) \right) , } \end{array}
$$

where the last inequality uses $h \leq \sqrt { c _ { 0 } } \Vert \widetilde J ^ { 2 } \Vert _ { F } ^ { - \frac { 1 } { 2 } }$ . Therefore, when $c _ { 0 }$ is small enough, we have

Eu [1Ac (u)]

$$
\begin{array} { r l } & { \overset { \mathtt { a d d } } { = } \pi _ { u } [ \overset { s } { = } \pi _ { \mathtt { d } } ^ { \mathtt { d } } \backslash \overset { \mathtt { d } } { = } I ] } \\ & { \le \mathbb { P } _ { u } \Big ( h ^ { 2 } \lVert \widetilde { J } u \rVert ^ { 2 } - x ^ { T } \widetilde { J } ^ { 3 } x \rVert \ge \frac { 1 } { 9 6 } \Big ) + \mathbb { P } _ { u } \Big ( | h ^ { \frac { 3 } { 2 } } x ^ { T } \widetilde { J } ^ { 2 } u | \ge \frac { 1 } { 9 6 \sqrt { 2 } } \Big ) + \mathbb { P } _ { u } \Big ( | h ^ { \frac { 5 } { 2 } } x ^ { T } \widetilde { J } ^ { 3 } u | \ge \frac { 1 } { 9 6 \sqrt { 2 } } \Big ) } \\ & { \le 2 \exp \Big ( - \frac { \frac { 1 } { 9 6 } - c _ { 0 } } { c ^ { \prime } c _ { 0 } } \Big ) + 2 \exp \Big ( - \frac { 1 } { 2 \cdot ( 9 6 \sqrt { 2 } ) ^ { 2 } c _ { 0 } ^ { \frac { 3 } { 2 } } } \Big ) + 2 \exp \Big ( - \frac { 1 } { 2 \cdot ( 9 6 \sqrt { 2 } ) ^ { 2 } c _ { 0 } ^ { \frac { 5 } { 2 } } } \Big ) } \end{array}
$$

and

$$
\begin{array} { r l } & { \mathbb { E } _ { u } \left[ { \mathbf 1 } _ { A ^ { c } } ( u ) \right] + \exp \left( - \frac { 1 } { 4 } h ^ { 3 } x ^ { T } \widetilde { J } ^ { 4 } x \right) \sqrt { \mathbb { E } _ { u } \left[ { \mathbf 1 } _ { A ^ { c } } ( u ) \right] } } \\ & { \cdot \left( \mathbb E _ { u } \left[ \exp ( - 3 h ^ { 2 } ( \| \widetilde { J } u \| ^ { 2 } - x ^ { T } \widetilde { J } ^ { 3 } x ) ) \right] \cdot \mathbb E _ { u } \left[ \exp ( 3 \sqrt { 2 } h ^ { \frac { 3 } { 2 } } x ^ { T } \widetilde { J } ^ { 2 } u ) \right] \cdot \mathbb E _ { u } \left[ \exp ( 3 \sqrt { 2 } h ^ { \frac { 5 } { 2 } } x ^ { T } \widetilde { J } ^ { 3 } u ) \right] \right) } \\ & { \prec \textbf { 1 } } \end{array}
$$

We can then obtain the desired result by combining all pieces.

# C.8 Proof of Lemma 15

We first write

$$
\begin{array} { l l } { \displaystyle \int _ { B _ { R } ^ { d } } \Big | Q ^ { \Delta } ( y , x ) - \widetilde { Q } ( y , x ) \Big | \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } \mathrm { d } y } \\ { \displaystyle = \int _ { B _ { R } ^ { d } } \Big | 1 - \frac { \widetilde { Q } ( y , x ) } { Q ^ { \Delta } ( y , x ) } \Big | \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } Q ^ { \Delta } ( y , x ) \mathrm { d } y } \\ { \displaystyle = \int _ { B _ { R } ^ { d } } \Big | 1 - \exp \left( \frac { - \| x - y + h \widetilde { I } ^ { \perp } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \perp } y ) \| ^ { 2 } + \| x - y + h \widetilde { J } y \| ^ { 2 } } { 4 h } \right) \Bigg | \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } Q ^ { \Delta } ( y , x ) \mathrm { d } y . } \end{array}
$$

Since $h \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - \frac 1 3 } ( \mathrm { t r } ( \widetilde J ^ { 2 } ) + r _ { d } ) ^ { - \frac 1 3 } \leq \sqrt { c _ { 0 } } \rho _ { 2 } ^ { - 1 }$ and $h \rho _ { 2 } \| \widetilde { I } \| _ { \mathrm { o p } } R ^ { 2 } \widetilde { \varepsilon } _ { 1 } ^ { 2 } \leq c _ { 0 }$ , when $c _ { 0 }$ is sufficiently small, we have for any $x \in E$ and $y \in B _ { R } ^ { d }$ ,

$$
\begin{array} { r l } & { \frac { | - \| x - y + h \widetilde { Y } \widetilde { I } ^ { 1 } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { 1 } y ) \| ^ { 2 } + \| x - y + h \widetilde { J } y \| ^ { 2 } | } { 4 h } } \\ & { = \frac { | h ( \widetilde { J } y + \widetilde { I } ^ { 1 } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { 1 } y ) ) ^ { T } ( \widetilde { J } y - \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } y ) ) + 2 ( x - y ) ^ { T } ( \widetilde { J } y - \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { \nabla } V _ { n } ( \widetilde { I } ^ { \frac { 1 } { 2 } } y ) ) | } { 4 } } \\ & { \leq \frac { h ( 2 \rho _ { 2 } R + \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \infty } \widetilde { \varepsilon } \| ) \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \infty } \widetilde { \varepsilon } _ { 1 } + 2 \| x - y \| \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \infty } \widetilde { \varepsilon } _ { 1 } } { 4 } } \\ &  \leq \frac { \sqrt { c _ { 0 } } ( 3 + \frac { 2 \| x - y \| } { R \sqrt { h _ { \rho _ { 2 } } } } ) . } \end{array}
$$

Thus we can bound

$$
\int _ { B _ { R } ^ { d } } \left| \mathcal { Q } ^ { \Delta } ( y , x ) - \widetilde { Q } ( y , x ) \right| \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } \mathrm { d } y \leq \int _ { B _ { R } ^ { d } } \Big ( \exp \Big ( \frac { \sqrt { c _ { 0 } } } { 4 } \big ( 3 + \frac { 2 \| x - y \| } { R \sqrt { h \rho _ { 2 } } } \big ) \Big ) - 1 \Big ) \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } Q ^ { \Delta } ( y , x ) \mathrm { d } y .
$$

Furthermore, by Lemma 14, we can get

$$
\int \frac { \pi ( y ) } { \pi ( x ) } Q ^ { \Delta } ( y , x ) \mathrm { d } y \leq \int Q ^ { \Delta } ( x , y ) \mathrm { d } y + \int \left| Q ^ { \Delta } ( x , y ) - \frac { \pi ( y ) Q ^ { \Delta } ( y , x ) } { \pi ( x ) } \right| \mathrm { d } y \leq \frac { 2 5 } { 2 4 } ,
$$

which leads to

$$
\begin{array} { r l } & { \displaystyle \int _ { B _ { R } ^ { d } } \left. Q ^ { \Delta } ( y , x ) - \widetilde { Q } ( y , x ) \right. \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } \mathrm { d } y } \\ & { \le \frac { 2 5 } { 2 4 } \displaystyle \int _ { B _ { R } ^ { d } } \Big ( \exp \Big ( \frac { \sqrt { c _ { 0 } } } { 4 } ( 3 + \frac { 2 \| x - y \| } { R \sqrt { h \rho _ { 2 } } } ) \Big ) - 1 \Big ) \frac { \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) } \mathrm { d } y } \\ & { = \frac { 2 5 } { 2 4 } \displaystyle \int _ { B _ { R } ^ { d } } \Big ( \exp \Big ( \frac { \sqrt { c _ { 0 } } } { 4 } \big ( 3 + \frac { 2 \| x - y \| } { R \sqrt { h \rho _ { 2 } } } \big ) \Big ) - 1 \Big ) N _ { d } \big ( ( I + h ^ { 2 } \widetilde { J } ) ^ { - 1 } ( x - h \widetilde { J } x ) , 2 h ( I + h ^ { 2 } \widetilde { J } ) ^ { - 1 } \big ) \mathrm { d } y } \end{array}
$$

where the last inequality is due to $\begin{array} { r } { { \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } } Q ^ { \Delta } ( y , x ) \ \propto \ \exp ( - { \frac { y ^ { T } ( I + h ^ { 2 } J ) y - 2 y ^ { T } ( x - h \widetilde { J } x ) } { 4 h } } ) } \end{array}$ . Consider $u \sim$ $N _ { d } ( 0 , I _ { d } )$ , for sufficiently small $c _ { 0 }$ , we have

$$
\begin{array} { r l } & { \displaystyle \int _ { \mathbb { R } _ { + } ^ { n } } \Big ( \exp \Big ( \frac { \sqrt { \epsilon _ { 0 } } } { 4 } \big ( 3 + \frac { 2 \big | \sigma - \beta \big | } { R \sqrt { \eta _ { \rho } } } \Big ) \Big ) - 1 \Big ) N _ { \alpha } \Big ( \big ( I + \delta ^ { 2 } \hat { J } \big ) ^ { - 1 } ( \boldsymbol { x } - h \hat { J } \boldsymbol { x } ) , \Omega \Lambda ( I + \hbar ^ { \beta } \hat { J } ) ^ { - 1 } \Big ) \mathrm { d } \boldsymbol { y } } \\ & { \le \mathbb { E } \mathbb { E } _ { \alpha \sim \mathbb { N } _ { \alpha } ( 0 , I , \boldsymbol { \hat { J } } ) } \Bigg [ \exp \Big ( \frac { \sqrt { \epsilon _ { 0 } } } { 4 } \Big ( 3 + \frac { 2 \big | \big ( I + \delta ^ { 2 } \hat { J } \big ) ^ { - 1 } ( \boldsymbol { x } - h \hat { J } \boldsymbol { x } ) - \boldsymbol { x } - \boldsymbol { \sqrt { 2 \kappa } } ( I + \hbar ^ { 2 } \hat { J } ) ^ { - 1 } \boldsymbol { x } \big | \Big ) } { R \sqrt { \eta _ { \rho } } } \Big ) - 1 } \\ & { \frac { \hat { \Pi } } { \le } \mathbb { E } _ { \alpha \sim N _ { \alpha } ( 0 , I , \boldsymbol { \hat { J } } ) } \Bigg [ \exp \Big ( \frac { \sqrt { \epsilon _ { 0 } } } { 4 } \Big ( 3 - 2 \frac { x _ { 0 } ^ { 1 } } { R \sqrt { \eta _ { \rho } } } \Big ( \frac { 2 \sqrt { 2 } } { 4 } \Big | 8 \boldsymbol { H } \Big | \Big ) \Big ) - 1 \Bigg ] } \\ & { \le \frac { \operatorname* { S u p } _ { 1 } } { 8 } \cdot \mathbb { E } _ { \alpha \sim N _ { \alpha } ( 0 , I , \boldsymbol { \hat { J } } ) } \Bigg [ \exp \Big ( \frac { \sqrt { 2 \epsilon _ { 0 } } } { 2 R \sqrt { \eta _ { \rho } } } \Big | 1 \boldsymbol { q } \Big | \Big ) \Bigg ] - 1 } \\ &  \le \frac { \operatorname* { S u p } _ { 1 } } { 8 } \cdot \Big \sqrt { \mathbb { E } _ { \alpha \sim N _ { \alpha } ( 0 , I , \boldsymbol { \hat { J } } ) } \Big [ \exp \Big ( \frac { \sqrt { 2 \epsilon _ { 0 } } } { 2 R \sqrt { \eta _ { \rho } } } \Big | 1 \boldsymbol { q } \Big | \Big ) \Bigg ] - 1 } \\  \end{array}
$$

where $( i )$ is due to $\begin{array} { r l } & { \lvert \| ( I + h ^ { 2 } \widetilde { J } ) ^ { - 1 } ( x - h \widetilde { J } x ) - x \rvert \rvert \leq h ^ { 2 } \rho _ { 2 } \lvert | x \rvert | + h \rho _ { 2 } \lvert | x \rvert \leq 2 \sqrt { h \rho _ { 2 } } c _ { 0 } ^ { \frac { 1 } { 4 } } \lvert | x \rvert | \leq \sqrt { h \rho _ { 2 } } c _ { 0 } ^ { \frac { 1 } { 4 } } R , } \\ & { R \geq 8 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) } . \mathrm { ~ T h u s ~ w e ~ c a n ~ o b t a i n ~ } \int _ { B _ { R } ^ { d } } \Big | Q ^ { \Delta } ( y , x ) - \widetilde { Q } ( y , x ) \Big | \frac { \overline { { \pi } } ( y ) } { \overline { { \pi } } ( x ) } \mathrm { d } y \leq \frac { 1 } { 7 2 } . } \end{array}$ and $( i i )$ is due to

# C.9 Proof of Lemma 9

# C.9.1 Proof of statement (1) of Lemma 9

Define the following compact supported function $k : \mathbb { R }  \mathbb { R }$ :

$$
k ( t ) = \left\{ \begin{array} { c c } { { 2 ( t - t ^ { 3 } ) } } & { { t \in ( - 1 , 1 ) , } } \\ { { 0 } } & { { \mathrm { o t h e r w i s e } . } } \end{array} \right.
$$

Then consider a initial distribution with density function $\mu _ { 0 } ( x ) = ( 1 + k ( \sqrt { \rho _ { 1 } } x _ { d } ) ) \cdot \overline { { \pi } } ( x )$ . This constriction guarantees that

$$
\begin{array} { r l r } & { } & { \chi ^ { 2 } ( \mu _ { 0 } , \overline { { \pi } } ) = \sqrt { \displaystyle \frac { \rho _ { 1 } } { 2 \pi } } \int _ { - \sqrt { \frac { 1 } { \rho _ { 1 } } } } ^ { \sqrt { \frac { 1 } { \rho _ { 1 } } } } k ^ { 2 } ( \sqrt { \rho _ { 1 } } x _ { d } ) \exp ( - \frac { \rho _ { 1 } } { 2 } x _ { d } ^ { 2 } ) \mathrm { d } x _ { d } } \\ & { } & { \qquad = \sqrt { \displaystyle \frac { 1 } { 2 \pi } } \int _ { - 1 } ^ { 1 } k ^ { 2 } ( t ) \exp ( - \frac { 1 } { 2 } t ^ { 2 } ) \mathrm { d } t \in ( 0 . 2 , 0 . 2 1 ) , } \end{array}
$$

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } \frac { \mu _ { 0 } ( x ) } { \overline { { \pi } } ( x ) } = 1 + \operatorname* { s u p } _ { t \in ( - 1 , 1 ) } k ( t ) < 2 ,
$$

and

$$
\left| h _ { 0 } ( x ) - h _ { 0 } ( y ) \right| = \big | \frac { \mu _ { 0 } ( x ) } { \overline { { \pi } } ( x ) } - \frac { \mu _ { 0 } ( y ) } { \overline { { \pi } } ( y ) } \big | = \left| k ( \sqrt { \rho _ { 1 } } x _ { d } ) - k ( \sqrt { \rho _ { 1 } } y _ { d } ) \right| \leq 2 \sqrt { \rho _ { 1 } } \left| x _ { d } - y _ { d } \right| .
$$

Therefore, the spectral gap of this initialization is controlled by

$$
\begin{array} { r l } & { \frac { \mathcal { E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) } \leq 1 0 \rho _ { 1 } \cdot \mathbb { E } _ { x \in \overline { { \pi } } , y \in T ( x , \cdot ) } \big [ ( x _ { d } - y _ { d } ) ^ { 2 } \big ] } \\ & { \qquad \leq 1 0 \rho _ { 1 } \cdot \mathbb { E } _ { x \in \overline { { \pi } } , y \in N _ { d } ( x - h \rho _ { 1 } x , 2 h I _ { d } ) } \big [ ( x _ { d } - y _ { d } ) ^ { 2 } \big ] } \\ & { \qquad = 1 0 \rho _ { 1 } \cdot \mathbb { E } _ { x _ { d } \in N ( 0 , 1 / \rho _ { 1 } ) , \xi \in N ( 0 , 1 ) } \big [ \big ( h \rho _ { 1 } x _ { d } - \sqrt { 2 h } \xi ) ^ { 2 } \big ] } \\ & { \qquad < 2 0 m ^ { 2 } h ^ { 2 } + 4 0 m h < 6 0 m h . } \end{array}
$$

# C.9.2 Proof of Statement (2) of Lemma 9

Denote sets

$$
\begin{array} { r l } & { K _ { 2 } = \Big \{ x \in \mathbb { R } ^ { d } : \big | x ^ { T } J ^ { 3 } x - \mathrm { t r } ( J ^ { 2 } ) \big | \leq ( 5 \| \| J ^ { 2 } \| _ { \mathrm { F } } ) \vee ( 2 4 \| \| J ^ { 2 } \| _ { \mathrm { o p } } ) \Big \} ; } \\ & { K _ { 3 } = \Big \{ x \in \mathbb { R } ^ { d } : \big | x ^ { T } J ^ { 4 } x - \mathrm { t r } ( J ^ { 3 } ) \big | \leq ( 5 \| \| J ^ { 3 } \| _ { \mathrm { F } } ) \vee ( 2 4 \| \| J ^ { 3 } \| _ { \mathrm { o p } } ) \Big \} ; } \\ & { K _ { 4 } = \Big \{ x \in \mathbb { R } ^ { d } : \big | x ^ { T } J ^ { 6 } x - \mathrm { t r } ( J ^ { 5 } ) \big | \leq ( 5 \| \| J ^ { 5 } \| _ { \mathrm { F } } ) \vee ( 2 4 \| \| J ^ { 5 } \| _ { \mathrm { o p } } ) \Big \} , } \end{array}
$$

To control the probability of the above events, we utilize the following Bernstein’s inequality: for $x \in$ $N _ { d } ( 0 , \Sigma )$ ,

$$
\mathbb { P } ( \left| \left\| x \right\| ^ { 2 } - \operatorname { t r } ( \Sigma ) \right| \geq t ) \leq 2 \exp \Big ( - \frac { 1 } { 8 } \big ( \frac { t ^ { 2 } } { \| \Sigma \| _ { \mathrm { F } } ^ { 2 } } \land \frac { t } { \| \Sigma \| _ { \mathrm { o p } } } \big ) \Big ) ,
$$

which leads to

$$
\mathbb { P } \left( | \| x \| ^ { 2 } - \operatorname { t r } ( \Sigma ) \big | \ge \left( \sqrt { 8 \lambda } \| \Sigma \| _ { F } \right) \vee \left( 8 \lambda \| \Sigma \| _ { \mathrm { o p } } \right) \right) \le 2 \exp ( - \lambda ) .
$$

Therefore, for $x \sim N _ { d } ( 0 , J ^ { - 1 } ) $ , the probability of events $x \in K _ { 2 } \cap K _ { 3 } \cap K _ { 4 }$ is inside the interval of $( 0 . 7 , 1 )$ . Then let $K _ { 1 } \subset \mathbb { R } ^ { d }$ be an arbitrary measurable set so that the probability of events $x \in K =$ $K _ { 1 } \cap K _ { 2 } \cap K _ { 3 } \cap K _ { 4 }$ is equal $\frac { 1 } { M _ { 0 } }$ (notice that $M _ { 0 } \geq 2$ and $\textstyle { \frac { 1 } { M _ { 0 } } } \leq { \frac { 1 } { 2 } } < 0 . 7$ , therefore such a set $K _ { 1 }$ exists). Then consider a initial distribution with density function $\begin{array} { r } { \mu _ { 0 } ^ { \prime } ( x ) = \frac { \overline { { \pi } } ( x ) \mathbf { 1 } _ { K } ( x ) } { \mathbb { E } _ { \overline { { \pi } } } [ \mathbf { 1 } _ { K } ( x ) ] } } \end{array}$ , it holds that

$$
\chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) = \frac { 1 } { \mathbb { E } _ { \overline { { \pi } } } [ \mathbf { 1 } _ { K } ( x ) ] } - 1 = M _ { 0 } - 1 ,
$$

and

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } \frac { \mu _ { 0 } ( x ) } { \overline { { \pi } } ( x ) } = \frac { 1 } { \mathbb { E } _ { \overline { { \pi } } } [ \mathbf { 1 } _ { K } ( x ) ] } = M _ { 0 } .
$$

Then denote for bounding the spectral gap $\frac { \mathcal { E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) }$ with $\begin{array} { r } { h _ { 0 } = \frac { \mathrm { d } \mu _ { 0 } ^ { \prime } } { \mathrm { d } \overline { { \pi } } } } \end{array}$ , we claim it suffices to show the following claim: denote $Q ^ { \Delta } ( x , )$ to be the density function of $N d ( x - h J x , 2 h I _ { d } )$ , then for any $x \in K$ , there exists a set $G _ { x } \subset \mathbb { R } ^ { d }$ so that

$$
\frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , y ) } \leq \exp ( - 1 6 \log ( \kappa d ) ) , \quad \forall y \in G _ { x } ,
$$

and

$$
\int _ { G _ { x } } Q ^ { \Delta } ( x , y ) \mathrm { d } y \geq 1 - \frac { 3 } { \kappa d } .
$$

Indeed, under claim (25) and (26), we have

$$
\begin{array} { r l } { \frac { \mathcal { E } ( h _ { 0 } , h _ { 0 } ) } { \chi ^ { 2 } ( \mu _ { 0 } ^ { \prime } , \overline { { \pi } } ) } = } & { \frac { M _ { 0 } ^ { 2 } \cdot \mathbb { E } _ { x \in \overline { { \pi } } , y \in \mathcal { L } ( x , \cdot ) } \left[ \left( \mathbf { 1 } _ { K } ( x ) - \mathbf { 1 } _ { K } ( y ) \right) ^ { 2 } \right] } { 2 ( M _ { 0 } - 1 ) } } \\ & { \leq \frac { M _ { 0 } ^ { 2 } } { M _ { 0 } - 1 } \int _ { K } \int _ { K ^ { c } } \operatorname* { m i n } \Big \{ 1 , \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , y ) } \Big \} \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , y ) \mathrm { d } y \mathrm { d } x } \\ & { \leq \frac { M _ { 0 } ^ { 2 } } { M _ { 0 } - 1 } \int _ { x \in K } \Big ( \int _ { G _ { z } } \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , y ) } Q ^ { \Delta } ( x , y ) \mathrm { d } y + \int _ { G _ { z } ^ { c } } Q ^ { \Delta } ( x , y ) \mathrm { d } y \Big ) \overline { { \pi } } ( x ) \mathrm { d } x } \\ & { \leq \frac { M _ { 0 } } { M _ { 0 } - 1 } \underset { x \in K } { \operatorname* { s u p } } \Big ( \underset { y \in G _ { z } } { \operatorname* { s u p } } \frac { \overline { { \pi } } ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , y ) } + \int _ { G _ { z } ^ { c } } Q ^ { \Delta } ( x , y ) \Big ) \mathrm { d } y } \\ & { \leq \frac { 8 } { \kappa d } , } \end{array}
$$

where the last inequality uses claim (25) and (26). Now we show the desired claim. First note that

$$
\frac { \pi ( y ) Q ^ { \Delta } ( y , x ) } { \overline { { { \pi } } } ( x ) Q ^ { \Delta } ( x , y ) } = \exp \Big ( \frac { h \cdot ( x ^ { T } J ^ { 2 } x - y ^ { T } J ^ { 2 } y ) } { 4 } \Big ) .
$$

Let sho $\begin{array} { r } { u = \frac { y - x + h J x } { \sqrt { 2 h } } } \end{array}$ $y \in N _ { d } ( x - h J x , 2 h I _ { d } )$ , we ho that $u \in N _ { d } ( 0 , I _ { d } )$ re, it suffice toand $x \in K$ $G _ { x } ^ { \prime } \in \mathbb { R } ^ { d }$ $\begin{array} { r } { \mathbb { E } _ { N _ { d } ( 0 , I _ { d } ) } [ \mathbf { 1 } _ { G _ { x } ^ { \prime } } ( u ) ] \geq 1 - \frac { 3 } { \kappa d } } \end{array}$

$$
\frac { \overline { { \pi } } ( \sqrt { 2 h } u + x - h J x ) Q ^ { \Delta } ( \sqrt { 2 h } u + x - h J x , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , \sqrt { 2 h } u + x - h J x ) } \leq \exp ( - 1 6 \log ( \kappa d ) ) , \quad \forall u \in G _ { x } ^ { \prime } .
$$

Denote the sets

$$
\begin{array} { r l } & { \mathcal { G } _ { x } ^ { 1 } = \{ u \in \mathbb { R } ^ { d } : \| J u \| ^ { 2 } - x ^ { T } J ^ { 3 } x \geq - \big ( \sqrt { 8 \log ( \kappa d ) } + 5 \big ) \rho _ { 2 } ^ { 2 } \sqrt { d } \} ; } \\ & { \mathcal { G } _ { x } ^ { 2 } = \{ u \in \mathbb { R } ^ { d } : x ^ { T } J ^ { 2 } u \geq - \sqrt { \log ( \kappa d ) \cdot \big ( 1 0 \rho _ { 2 } ^ { 3 } \sqrt { d } + 2 \rho _ { 2 } ^ { 3 } d \big ) } \} ; } \\ & { \mathcal { G } _ { x } ^ { 3 } = \{ u \in \mathbb { R } ^ { d } : x ^ { T } J ^ { 3 } u \leq \sqrt { \log ( \kappa d ) \cdot \big ( 1 0 \rho _ { 2 } ^ { 5 } \sqrt { d } + 2 \rho _ { 2 } ^ { 5 } d \big ) } \} . } \end{array}
$$

Then under $G _ { x } ^ { \prime } = \mathcal { G } _ { x } ^ { 1 } \cap \mathcal { G } _ { x } ^ { 2 } \cap \mathcal { G } _ { x } ^ { 3 }$ , we have

$$
\begin{array} { r l } & { \frac { \overline { { \pi } } ( \sqrt { 2 h } u + x - h J x ) Q ^ { \Delta } ( \sqrt { 2 h } u + x - h J x , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , \sqrt { 2 h } u + x - h J x ) } } \\ & { = \exp \bigg ( - \frac { 1 } { 4 } \Big ( 2 h ^ { 2 } \| J u \| ^ { 2 } + 2 \sqrt { 2 } h ^ { \frac { 5 } { 2 } } x ^ { T } J ^ { 2 } u - 2 \sqrt { 2 } h ^ { \frac { 5 } { 2 } } x ^ { T } J ^ { 3 } u + h ^ { 3 } x ^ { T } J ^ { 4 } x - 2 h ^ { 2 } x ^ { T } J ^ { 3 } x \Big ) \bigg ) } \\ & { \leq \exp \bigg ( - \frac { 1 } { 4 } \Big ( h ^ { 3 } x ^ { T } J ^ { 4 } x - 2 h ^ { 2 } \big ( \sqrt { 8 \log ( \kappa d ) } + 5 \big ) \rho _ { 2 } ^ { 2 } \sqrt { d } } \\ & { \qquad - 2 \sqrt { 2 } \sqrt { \log ( \kappa d ) } \big ( h ^ { \frac { 3 } { 2 } } \sqrt { 1 0 \rho _ { 2 } ^ { 3 } \sqrt { d } + 2 \rho _ { 2 } ^ { 3 } d } + h ^ { \frac { 5 } { 2 } } \sqrt { 1 0 \rho _ { 2 } ^ { 5 } \sqrt { d } + 2 \rho _ { 2 } ^ { 5 } d } \big ) \Big ) \bigg ) . } \end{array}
$$

Then there exists a universal constant $N _ { 1 }$ so that when $d \geq N _ { 1 }$ , for any $x \in K$ and $u \in G _ { x } ^ { \prime }$

$$
\begin{array} { r l } & { \frac { \overline { { \pi } } ( \sqrt { 2 h } u + x - h J x ) Q ^ { \Delta } ( \sqrt { 2 h } u + x - h J x , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , \sqrt { 2 h } u + x - h J x ) } } \\ & { \leq \exp \Big ( - \frac { 1 } { 4 } \big ( h ^ { 3 } x ^ { T } J ^ { 4 } x - 6 h ^ { 2 } \sqrt { \log ( \kappa d ) } \rho _ { 2 } ^ { 2 } \sqrt { d } - 5 \sqrt { \log ( \kappa d ) } \big ( h ^ { \frac { 3 } { 2 } } \sqrt { \rho _ { 2 } ^ { 3 } d } + h ^ { \frac { 5 } { 2 } } \sqrt { \rho _ { 2 } ^ { 5 } d } \big ) \big ) \Big ) } \\ & { \leq \exp \Big ( - \frac { 1 } { 4 } \big ( h ^ { 3 } x ^ { T } J ^ { 4 } x - 6 h ^ { 2 } \sqrt { \log ( \kappa d ) } \rho _ { 2 } ^ { 2 } \sqrt { d } - 5 \sqrt { \log ( \kappa d ) } \big ( h ^ { \frac { 3 } { 2 } } \sqrt { \rho _ { 2 } ^ { 3 } d } + h ^ { \frac { 5 } { 2 } } \sqrt { \rho _ { 2 } ^ { 5 } d } \big ) \big ) \Big ) } \\ & { \leq \exp \big ( - 3 2 \log ( \kappa d ) + 9 6 \log ^ { \frac { 7 } { 6 } } ( \kappa d ) d ^ { - \frac { 1 } { 6 } } + 2 2 7 \log ^ { \frac { 4 } { 3 } } ( \kappa d ) d ^ { - \frac { 1 } { 3 } } \big ) . } \end{array}
$$

Therefore, use $\kappa \leq c _ { 1 } \cdot d ^ { c _ { 2 } }$ there exists $N _ { 2 }$ that depends only on $c _ { 1 } , c _ { 2 }$ so that when $d \ge N _ { 2 }$ , for any $x \in K$ and $u \in G _ { x } ^ { \prime }$

$$
\frac { \overline { { \pi } } ( \sqrt { 2 h } u + x - h J x ) Q ^ { \Delta } ( \sqrt { 2 h } u + x - h J x , x ) } { \overline { { \pi } } ( x ) Q ^ { \Delta } ( x , \sqrt { 2 h } u + x - h J x ) } \leq \exp \big ( - 1 6 \log ( \kappa d ) \big ) .
$$

Now we control the probability $u \in G _ { x } ^ { \prime }$ . Firstly by Bernstein’s inequality, for $u \in N _ { d } ( 0 , I _ { d } )$ , we have

$$
\mathbb { P } \left( u ^ { T } J ^ { 2 } u - \mathrm { t r } ( J ^ { 2 } ) \geq - \big ( ( \sqrt { 8 \log ( \kappa d ) } \| J ^ { 2 } \| _ { \mathrm { F } } ) \vee ( 8 \log ( \kappa d ) \| J ^ { 2 } \| _ { \mathrm { o p } } ) \big ) \right) \leq 1 - \frac { 1 } { d \kappa } .
$$

So there exists a universal constant that $N _ { 3 }$ so that when $d \ge N _ { 3 }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { d \kappa } }$

$$
\begin{array} { r l } & { J u \Vert ^ { 2 } - x ^ { T } J ^ { 3 } x \geq \mathrm { t r } ( J ^ { 2 } ) - ( \sqrt { 8 \log ( \kappa d ) } \Vert J ^ { 2 } \Vert _ { \mathrm { F } } ) \vee ( 8 \log ( \kappa d ) \Vert J ^ { 2 } \Vert _ { \mathrm { o p } } ) - \mathrm { t r } ( J ^ { 2 } ) - ( 5 \Vert J ^ { 2 } \Vert _ { \mathrm { F } } ) \vee } \\ & { \qquad \geq - \big ( \sqrt { 8 \log ( \kappa d ) } + 5 \big ) \rho _ { 2 } ^ { 2 } \sqrt { d } . } \end{array}
$$

Moreover, since for any $t \in \mathbb { R }$ and $x \in K$ ,

$$
\begin{array} { r l } & { \mathbb { E } [ \exp ( t x ^ { T } J ^ { 2 } u ) ] = \exp \bigg ( \frac { 1 } { 2 } t ^ { 2 } x ^ { T } J ^ { 4 } x \bigg ) } \\ & { \qquad \leq \exp \Big ( \displaystyle \frac { 1 } { 2 } \Big ( \mathrm { t r } ( J ^ { 3 } ) + \big ( ( 5 \| J ^ { 3 } \| _ { \mathrm { F } } ) \vee ( 2 4 \| J ^ { 3 } \| _ { \mathrm { o p } } ) \big ) \Big ) t ^ { 2 } \Big ) , } \end{array}
$$

and

$$
\begin{array} { r l } & { \mathbb { E } [ \exp ( t x ^ { T } J ^ { 3 } u ) ] = \exp \bigg ( \frac { 1 } { 2 } t ^ { 2 } x ^ { T } J ^ { 6 } x \bigg ) } \\ & { \qquad \leq \exp \Big ( \frac { 1 } { 2 } \Big ( \mathrm { t r } ( J ^ { 5 } ) + \big ( ( 5 \| J ^ { 5 } \| _ { \mathrm { F } } ) \vee ( 2 4 \| J ^ { 5 } \| _ { \mathrm { o p } } ) \big ) \Big ) t ^ { 2 } \Big ) , } \end{array}
$$

by Markov inequality, there exists a universal constant $N _ { 4 }$ so that when $d \ge N _ { 4 }$ , it holds with probability at least $1 - { \textstyle \frac { 2 } { \kappa d } }$ t hat

and

$$
\begin{array} { l } { x ^ { T } J ^ { 2 } u \geq - \sqrt { \log ( \kappa d ) 2 \rho _ { 2 } ^ { 3 } d + 1 0 \rho _ { 2 } ^ { 3 } \sqrt { d } } } \\ { \hfill } \\ { x ^ { T } J ^ { 3 } u \leq \sqrt { \log ( \kappa d ) 2 \rho _ { 2 } ^ { 5 } d + 1 0 \rho _ { 2 } ^ { 5 } \sqrt { d } } . } \end{array}
$$

We can then obtain the desired result by combining all pieces.

# D Proof of Lemmas for Theorem 2

# D.1 Proof of Lemma 10

Without loss of generality, we can assume the learning rate $\alpha = 1$ , as otherwise we can take $\ell ( X , \theta ) = \alpha$ · $\ell ( X , \theta )$ . To begin with, we provide in the following lemma some localized “maximal” type inequalities that control the supreme of empirical processes to deal with the non-smoothness of the loss function. All the following lemmas in this subsection are under Condition B.1-B.4.

Lemma 16. There exist positive constants c and r such that it holds with probability larger than $1 - n ^ { - 2 }$ that ,

$$
\begin{array} { r l } & { F o r \ : a n y \ : \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) , \ : \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \prime } ) - { \mathbb E } [ g ( X , \theta ) ] + { \mathbb E } [ g ( X , \theta ^ { \prime } ) ] \right\| \le } \\ & { C \left( \sqrt \frac { \log n } { n } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } } + \frac { \log n } { n } d ^ { 1 + \gamma } \right) . } \end{array}
$$

$$
\begin{array} { r l } & { F o r \ : a n y \ : \theta , \theta ^ { \prime } \in \Theta , \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { \prime } ) - \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { \prime } ) ] \bigg | \leq } \\ & { C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma } \| \theta - \theta ^ { \prime } \| + \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } \right) . } \end{array}
$$

$$
\begin{array} { r l } & { F o r \ a n y \ \theta , \theta ^ { \prime } \in \ B _ { r } ( \theta ^ { * } ) , \ \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { \prime } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \right. - } \\ & { \left. \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { \prime } ) ] + \mathbb { E } [ g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ] \right| \leq C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } + 1 } + \frac { \log n } { n } d ^ { 1 + \gamma } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } - 1 } \right) } \\ & { \theta ^ { \prime } \| + ( \frac { \log n } { n } ) ^ { 2 } \Bigg ) . } \end{array}
$$

Recall $\begin{array} { r } { V _ { n } ( \xi ) = n \left( \mathcal { R } _ { n } ( \widehat { \theta } + \frac { \xi } { \sqrt { n } } ) - \mathcal { R } _ { n } ( \widehat { \theta } ) \right) + \log \pi ( \widehat { \theta } + \frac { \xi } { \sqrt { n } } ) - \log \pi ( \widehat { \theta } ) } \end{array}$ , in order to bound the difference   
between order ap $V _ { n } ( \xi )$ and ate t $\frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 }$ rst prove that , we have the $\widehat { \theta }$ is close to llowing lem $\theta ^ { * }$ . Define a firsta for bounding $\widehat { \theta }$ $\begin{array} { r } { \widehat { \theta ^ { \diamond } } = \theta ^ { * } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) } \end{array}$   
the difference between $\widehat { \theta } ^ { \circ }$ and $\theta ^ { * }$ .

Lemma 17. It holds with probability larger than $1 - n ^ { - 2 }$ that

$$
\lVert \widehat { { \boldsymbol { \theta } } ^ { \diamond } } - { \boldsymbol { \theta } } ^ { * } \rVert \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } + C d ^ { 1 + \gamma _ { 0 } + \gamma } \frac { \log n } { n } .
$$

And we resort to the following lemma that provides an upper bound on the $\ell _ { 2 }$ distance between $\widehat { \theta }$ and $\widehat { \theta } ^ { \circ }$ .

Lemma 18. There exists a small enough positive constant c such that when d ≤ c ( nlog n ) $\begin{array} { r } { d \le c \bigl ( \bigl ( \frac { n } { \log n } \bigr ) ^ { \frac { 1 } { 2 + 2 ( \gamma + \gamma _ { 0 } + \gamma _ { 1 } ) } } \wedge } \end{array}$ $( \frac { n } { \log n } ) ^ { \frac { 1 } { 1 + 2 \gamma + 2 \gamma _ { 2 } + 4 \gamma _ { 0 } } } )$ , then it holds with probability larger than $1 - c \cdot n ^ { - 2 }$ that

$$
\left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| \leq C d ^ { 1 + \gamma } \frac { \log n } { n } + C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 } + \beta _ { 1 } } ;
$$

$$
\widehat { \theta } - \widehat { \theta ^ { \circ } } \| \leq C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) + \gamma _ { 0 } } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + C d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) + \gamma _ { 0 } } \frac { \log n } { n } + C \Big ( d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \gamma _ { 0 } } \sqrt { \frac { \log n } { n } } \Big ) ^ { \frac { 1 } { 1 } }
$$

By $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { X } } \| g ( X , \theta ^ { * } ) \| \leq C d ^ { \gamma } } \end{array}$ , we have $\begin{array} { r } { \Vert \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \mathbb { E } [ g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } ] \mathcal { H } _ { \theta } ^ { - 1 } \Vert _ { \mathrm { o p } } \leq C _ { 1 } d ^ { 2 \gamma } \Vert | \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } | | _ { \mathrm { o p } } ^ { 2 } \leq } \end{array}$ $C _ { 2 } d ^ { 2 \gamma + 2 \gamma _ { 0 } }$ , which leads to $\gamma _ { 4 } \leq 2 \gamma _ { 0 } + 2 \gamma$ . Then by Lemma 17 and Lemma 18, when

$$
d \leq c \Big ( \big ( \frac { n } { \log n } \big ) ^ { \frac { \beta _ { 1 } } { \gamma _ { 3 } + \beta _ { 1 } ( 1 + \gamma _ { 4 } ) + 2 \gamma _ { 0 } - \gamma _ { 4 } } } \wedge \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { 1 + 2 \gamma + 2 \gamma _ { 2 } + 4 \gamma _ { 0 } } } \wedge \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { 2 + 2 ( \gamma + \gamma _ { 0 } + \gamma _ { 1 } ) } } \Big ) ,
$$

it holds with probability larger than $1 - c _ { 1 } \cdot n ^ { - 2 }$ that

$$
\| { \widehat { \theta } } - \theta ^ { * } \| \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } { \sqrt { \frac { \log n } { n } } } .
$$

We can now derive (high probability) upper bound to the term of $| V _ { n } ( \xi ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } |$ over $1 \leq \| \xi \| \leq C \sqrt { n }$ Consider the following decomposition:

$$
\begin{array} { l } { \displaystyle { V _ { n } ( \xi ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } \bigg | } } \\ { \displaystyle \leq | n ( { \mathcal R } _ { n } ( { \widehat \theta } + \frac { \xi } { \sqrt { n } } ) - { \mathcal R } _ { n } ( { \widehat \theta } ) ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } | + | \log \pi ( { \widehat \theta } + \frac { \xi } { \sqrt { n } } ) - \log \pi ( { \widehat \theta } ) | } \\ { \displaystyle \leq n | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , { \widehat \theta } ) \frac { \xi } { \sqrt { n } } | + n | { \mathcal R } _ { n } ( { \widehat \theta } + \frac { \xi } { \sqrt { n } } ) - { \mathcal R } _ { n } ( { \widehat \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , { \widehat \theta } ) \frac { \xi } { \sqrt { n } } - ( { \mathcal R } ( { \widehat \theta } + \frac { \xi } { \sqrt { n } } ) - { \mathcal R } _ { n } ( { \widehat \theta } ) ) | } \\ { \displaystyle - { \mathbb E } g ( X , { \widehat \theta } ) \frac { \xi } { \sqrt { n } } ) \bigg | + n | { \mathcal R } ( { \widehat \theta } + \frac { \xi } { \sqrt { n } } ) - { \mathcal R } ( { \widehat \theta } ) - { \mathbb E } [ g ( X , { \widehat \theta } ) ] \frac { \xi } { \sqrt { n } } - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } | + C \sqrt { d } \cdot \frac { \| \xi \| } { \sqrt { n } } . } \end{array}
$$

The first term can be bounded by Lemma 18, that is

$$
\left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \frac { \xi } { \sqrt { n } } \right| \leq C \frac { \| \xi \| } { \sqrt { n } } \left[ d ^ { 1 + \gamma } \frac { \log n } { n } + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } ( \frac { \log n } { n } ) ^ { \frac { 1 } { 2 } + \beta _ { 1 } } \right] ;
$$

for the second term, by the third statement of Lemma 16, we can obtain that

$$
\begin{array} { r l } & { \displaystyle \left. \mathcal { R } _ { n } ( \widehat { \theta } + \frac { \xi } { \sqrt { n } } ) - \mathcal { R } _ { n } ( \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \frac \xi { \sqrt { n } } - \left( \mathcal { R } ( \widehat { \theta } + \frac \xi { \sqrt { n } } ) - \mathcal { R } ( \widehat { \theta } ) - \mathbb { E } g ( X , \widehat { \theta } ) \frac \xi { \sqrt { n } } \right) \right. } \\ & { \le C \left[ d ^ { 1 + \gamma } \frac { \log n } { n } \frac { \| \xi \| } { \sqrt { n } } + \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } ( \frac { \| \xi \| } { \sqrt { n } } ) ^ { 1 + \beta _ { 1 } } + ( \frac { \log n } { n } ) ^ { 2 } \right] ; } \end{array}
$$

for the third term, by the twice differentiability of ${ \mathcal { R } } ( \theta )$ and Lipschitzness of $\mathcal { H } _ { \theta }$ , we can obtain that

$$
\begin{array} { r l } & { \mathcal { R } ( \widehat { \theta } + \frac { \xi } { \sqrt { n } } ) - \mathcal { R } ( \widehat { \theta } ) - \mathbb { E } [ g ( X , \widehat { \theta } ) ] \frac { \xi } { \sqrt { n } } - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 n } } \\ & { \leq \frac { \| \xi \| ^ { 2 } } { 2 n } \operatorname* { s u p } _ { \xi \in K } \| \mathcal { H } _ { \widehat { \theta } + \frac { \xi } { \sqrt { n } } } - \mathcal { H } _ { \theta ^ { * } } \| _ { \textup { o p } } } \\ & { \leq C \frac { \| \xi \| ^ { 2 } } { n } d ^ { \gamma _ { 2 } } \left( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } + \frac { \| \xi \| } { \sqrt { n } } \right) } \\ & { = C \frac { \| \xi \| ^ { 3 } } { n ^ { \frac { 3 } { 2 } } } d ^ { \gamma _ { 2 } } + C \frac { \| K \| ^ { 2 } } { n } \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } . } \end{array}
$$

Therefore, by combining all these result, when $1 \leq \| \xi \| \leq c \sqrt { n }$ for a small enough $c$ , we can obtain that

$$
\begin{array} { r l } & { \left| V _ { n } ( \xi ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } \right| \leq C d ^ { 1 + \gamma } \| \xi \| \frac { \log n } { \sqrt { n } } + C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \xi \| ^ { 1 + \beta _ { 1 } } n ^ { - \frac { \beta _ { 1 } } { 2 } } \sqrt { \log n } } \\ & { \qquad + C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \| \xi \| ^ { 2 } \sqrt { \frac { \log n } { n } } + C d ^ { \gamma _ { 2 } } \| \xi \| ^ { 3 } n ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

For the second statement, since when $1 \leq \| \xi \| \leq c \sqrt { n }$ for a small enough $c$ ,

$$
\begin{array} { l } { \displaystyle \widetilde \nabla _ { N } ( \xi ) - \mathcal { H } _ { \theta ^ { * } } \xi \| } \\ { \displaystyle = \left\| \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) - \frac { 1 } { \sqrt { n } } \nabla [ \log \pi ] ( \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) - \mathcal { H } _ { \theta ^ { * } } \xi \right\| } \\ { \displaystyle \leq \left\| \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| + \sqrt { n } \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) - \mathbb { E } [ g ( X , \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) ] + \mathbb { E } [ g ( X , \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) ] \right\| } \\ { + \sqrt { n } \left\| \mathbb { E } [ g ( X , \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) ] - \mathbb { E } [ g ( X , \widehat { \theta } ) ] - \mathcal { H } _ { \theta ^ { * } } \xi \right\| + \left\| \frac { 1 } { \sqrt { n } } \nabla [ \log \pi ] ( \frac { \xi } { \sqrt { n } } + \widehat { \theta } ) \right\| . } \end{array}
$$

Then by the first statement of Lemma 16, Lemma 18, the twice-differentiability of ${ \mathcal { R } } ( \theta )$ and Lipschitz continuity of $\mathcal { H } _ { \theta }$ . Similar to analysis for the first statement, we can obtain that for any $1 \leq \| \xi \| \leq c \sqrt { n }$ ,

$$
\begin{array} { r l } & { \| \widetilde { \nabla } V _ { n } ( \xi ) - H _ { \theta ^ { * } } \xi \| } \\ & { \leq C \sqrt { n } \left[ d ^ { 1 + \gamma } \frac { \log n } { n } + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } ( \frac { \log n } { n } ) ^ { \frac { 1 } { 2 } + \beta _ { 1 } } \right] + C \left( d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \sqrt { \log n } ( \frac { \| \xi \| } { \sqrt { n } } ) ^ { \beta _ { 1 } } + d ^ { 1 + \gamma } \frac { \log n } { \sqrt { n } } \right) } \\ & { + C \left( d ^ { \gamma _ { 2 } } \frac { \xi \| ^ { 2 } } { \sqrt { n } } + d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \sqrt { \log n } \frac { \| \xi \| } { \sqrt { n } } \right) + C \sqrt { \frac { d } { n } } } \\ & { \leq C d ^ { 1 + \gamma } \frac { \log n } { \sqrt { n } } + C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \xi \| ^ { \beta _ { 1 } } n ^ { - \frac { \beta _ { 1 } } { 2 } } \sqrt { \log n } + C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \| \xi \| \sqrt { \frac { \log n } { n } } + C d ^ { \gamma _ { 2 } } \| \xi \| ^ { 2 } n ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

# D.2 Proof of Lemma 11

Without loss of generality, we can assume the learning rate $\alpha = 1$ , as otherwise we can take $\ell ( X , \theta ) =$ $\alpha \cdot \ell ( X , \theta )$ . Denote $\begin{array} { r } { K = \{ \xi : \| \widetilde { I } ^ { - 1 / 2 } \xi \| \le \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \vee \frac { 3 ( \sqrt { d } + t ) } { \sqrt { \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) } } \} } \end{array}$ . Then

$$
\pi _ { n } ( \sqrt { n } ( \theta - \widehat { \theta } ) \in K ^ { c } ) = \frac { \int _ { K ^ { c } } \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \mathcal { H } _ { \theta ^ { * } } ) } { \int \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \mathcal { H } _ { \theta ^ { * } } ) }
$$

Denote $K _ { 1 } = K ^ { c } \cap \{ \xi ~ : ~ \| \xi \| \le c _ { 1 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } \sqrt { n } \}$ and $K _ { 2 } = K ^ { c } \cap \{ \xi ~ : ~ \| \xi \| ~ \ge ~ c _ { 1 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } \sqrt { n } \}$ . When $\xi \in K _ { 1 }$ , we have $\begin{array} { r } { \| \xi \| \ge \frac { \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } } { \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } } = 1 } \end{array}$ = 1. So by Lemma 10 and the fact that

$$
\begin{array} { r } { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi = ( \widetilde { I } ^ { - \frac { 1 } { 2 } } \xi ) ^ { T } \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } \widetilde { I } ^ { - \frac { 1 } { 2 } } \xi \ge \lambda _ { \operatorname* { m i n } } ( \widetilde { J } ) \| \widetilde { I } ^ { - \frac { 1 } { 2 } } \xi \| ^ { 2 } \ge 9 ( \sqrt { d } + t ) ^ { 2 } ; } \end{array}
$$

and

$$
\begin{array} { r } { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi \geq \lambda _ { \operatorname* { m i n } } ( \mathcal { H } _ { \theta ^ { * } } ) \vert \vert \xi \vert \vert ^ { 2 } \geq d ^ { - \gamma _ { 0 } } \vert \vert \xi \vert \vert ^ { 2 } , } \end{array}
$$

we can verify that when d ≤ c nκ3log n f or small enough $c$ and $K _ { 1 } = K ^ { c } \cap \{ \xi : \ \| \xi \| \leq c _ { 1 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } \sqrt { n } \}$ for a small enough $c _ { 1 }$ , it holds that

$$
V _ { n } ( \xi ) \geq \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 4 } , \quad \xi \in K _ { 1 } .
$$

So we have

$$
\begin{array} { r l } & { \displaystyle \int _ { K _ { 1 } } \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \mathcal { H } _ { \theta ^ { * } } ) } \\ & { \displaystyle \le 2 ^ { \frac { d } { 2 } } ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \frac { \mathcal { H } _ { \theta ^ { * } } } { 2 } ) \int _ { K _ { 1 } } \exp \big ( - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 4 } \big ) \mathrm { d } \xi } \\ & { \displaystyle \le 2 ^ { \frac { d } { 2 } } \cdot \mathbb { P } _ { \chi ^ { 2 } ( d ) } ( \| x \| \ge 4 ( \sqrt { d } + t ) ^ { 2 } ) } \\ & { \displaystyle \le \exp ( - t ^ { 2 } - \frac { 1 } { 4 } ) , } \end{array}
$$

where the last inequality uses the tail inequality of $\chi ^ { 2 }$ distribution with $d$ degree of freedom (see for example, Lemma 1 of Laurent and Massart [2000]).

For $\xi \in K _ { 2 }$ and $\theta = { \widehat { \theta } } + { \frac { \xi } { \sqrt { n } } }$ , we have

$$
\lVert \hat { { \boldsymbol { \theta } } } - { \boldsymbol { \theta } } \rVert \geq c _ { 1 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } .
$$

Moreover, by equation (29) which states that $\lVert \widehat { { \boldsymbol { \theta } } } - { \boldsymbol { \theta } } ^ { * } \rVert \lesssim d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } }$ , when $\begin{array} { r } { d \le c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ for small enough $c$ , we have

$$
\lVert \theta - \theta ^ { * } \rVert \geq \frac { c _ { 1 } } { 2 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } .
$$

Therefore, by the second statement of Lemma 16, we can conclude

$$
^ { 1 } ) - \mathcal { R } ( \widehat { \theta } ) = \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) + \mathcal { R } ( \theta ^ { * } ) - \mathcal { R } ( \widehat { \theta } ) \geq C d ^ { - \gamma _ { 0 } } ( d ^ { - \gamma _ { 1 } } \wedge \Vert \theta - \theta ^ { * } \Vert ^ { 2 } ) - C _ { 1 } d ^ { \gamma + \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } }
$$

and

$$
\vert \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \widehat { \theta } ) - \mathcal { R } ( \theta ) + \mathcal { R } ( \widehat { \theta } ) \vert \leq C _ { 2 } \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma } \Vert \theta - \widehat { \theta } \Vert + C _ { 2 } \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } .
$$

Then if (1) $c _ { 1 } d ^ { - \gamma _ { 0 } - \gamma _ { 2 } } \sqrt { n } \leq \lVert \hat { \theta } - \theta \rVert \leq d ^ { - \frac { \gamma _ { 1 } } { 2 } }$ , we have

$$
\begin{array} { r l } & { \displaystyle \mathsf { \Sigma } _ { n } ( \theta ) - { \mathcal R } _ { n } ( \widehat \theta ) \geq { \mathcal R } ( \theta ) - { \mathcal R } ( \widehat \theta ) - | { \mathcal R } _ { n } ( \theta ) - { \mathcal R } _ { n } ( \widehat \theta ) - { \mathcal R } ( \theta ) + { \mathcal R } ( \widehat \theta ) | } \\ & { \qquad \geq C _ { C 1 } d ^ { - 3 \gamma _ { 0 } - 2 \gamma _ { 2 } } - C _ { 1 } d ^ { \gamma + \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } - C _ { 2 } \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma - \frac { \gamma _ { 1 } } { 2 } } - C _ { 2 } \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } } \\ & { \qquad \geq \frac { C _ { C 1 } } { 2 } d ^ { - 3 \gamma _ { 0 } - 2 \gamma _ { 2 } } , } \end{array}
$$

where the last inequality uses $\begin{array} { r } { d \le c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ for small enough $c$ ; when (2) $\lVert \hat { { \boldsymbol { \theta } } } - { \boldsymbol { \theta } } \rVert \geq d ^ { - { \frac { \gamma _ { 1 } } { 2 } } }$ , then by $\Theta \subset [ - C , C ] ^ { d }$ , we can get

$$
\begin{array} { r l } & { { \mathcal { R } } _ { n } ( \theta ) - { \mathcal { R } } _ { n } ( \widehat \theta ) \geq { \mathcal { R } } ( \theta ) - { \mathcal { R } } ( \widehat \theta ) - | { \mathcal { R } } _ { n } ( \theta ) - { \mathcal { R } } _ { n } ( \widehat \theta ) - { \mathcal { R } } ( \theta ) + { \mathcal { R } } ( \widehat \theta ) | } \\ & { \qquad \geq C { _ { c 1 } } d ^ { - \gamma _ { 1 } - \gamma _ { 0 } } - C _ { 1 } d ^ { \gamma + \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } - C _ { 2 } \sqrt { \frac { \log n } { n } } d ^ { 1 + \gamma } - C _ { 2 } \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } } \\ & { \qquad \geq \frac { C c _ { 1 } } { 2 } d ^ { - \gamma _ { 1 } - \gamma _ { 0 } } , } \end{array}
$$

where the last inequality uses $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ for small enough $c$ . So we can obtain that when $\xi \in K _ { 2 }$ ,

$$
\xi ) = n \left( \mathcal { R } _ { n } ( { \widehat { \theta } } + \frac { \xi } { \sqrt { n } } ) - \mathcal { R } _ { n } ( { \widehat { \theta } } ) \right) - \left( \pi ( { \widehat { \theta } } + \frac { \xi } { \sqrt { n } } ) - \pi ( { \widehat { \theta } } ) \right) \geq \frac { C c _ { 1 } } { 4 } \cdot n \cdot d ^ { - \gamma _ { 0 } } \big ( d ^ { - \gamma _ { 1 } } \wedge d ^ { - 2 \gamma _ { 0 } - 2 \gamma _ { 2 } } \big )
$$

Thus using $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ c n 3log n , we have

$$
\begin{array} { r l } & { \displaystyle \int _ { K _ { 2 } } \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \mathcal { H } _ { \theta ^ { * } } ) } \\ & { \le \exp \Big ( - \displaystyle \frac { d } { 2 } \log ( 2 \pi ) + \frac { d } { 2 } \log \big ( \| \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } \big ) \Big ) \cdot \exp \Big ( \frac { C c _ { 1 } } { 4 } \cdot n \cdot d ^ { - \gamma _ { 0 } } \big ( d ^ { - \gamma _ { 1 } } \wedge d ^ { - 2 \gamma _ { 0 } - 2 \gamma _ { 2 } } \big ) \Big ) } \\ & { \le \exp \Big ( \frac { C c _ { 1 } } { 8 } \cdot n \cdot d ^ { - \gamma _ { 0 } } \big ( d ^ { - \gamma _ { 1 } } \wedge d ^ { - 2 \gamma _ { 0 } - 2 \gamma _ { 2 } } \big ) \Big ) . } \end{array}
$$

It remains to bound the denominator $\begin{array} { r } { \int \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( \mathcal { H } _ { \theta ^ { * } } ) } \end{array}$ , we have

$$
\begin{array} { r l } & { \int \exp ( - V _ { n } ( \xi ) ) \mathrm { d } \xi \cdot ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( { \mathcal { H } } _ { \theta ^ { \star } } ) } \\ & { \geq ( 2 \pi ) ^ { - \frac { d } { 2 } } \mathrm { d e t } ( { \mathcal { H } } _ { \theta ^ { \star } } ) \int _ { \| \xi \| \leq 4 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( \mathcal { H } _ { \theta ^ { \star } } ) } } \exp \big ( - \frac { \xi ^ { T } { \mathcal { H } } _ { \theta ^ { \star } } \xi } { 2 } \big ) \mathrm { d } \xi } \\ & { \qquad \times \operatorname* { s u p } _ { \| \xi \| \leq 4 \sqrt { d / \lambda _ { \operatorname* { m i n } } ( \mathcal { H } _ { \theta ^ { \star } } ) } } \exp \big ( \frac { \xi ^ { T } { \mathcal { H } } _ { \theta ^ { \star } } \xi } { 2 } - V _ { n } ( \xi ) \big ) } \\ & { \geq \exp ( - \frac { 1 } { 4 } ) , } \end{array}
$$

where the last inequality uses $\lambda _ { \operatorname* { m i n } } ( \mathcal { H } _ { \theta ^ { * } } ) \geq C d ^ { - \gamma _ { 0 } }$ , $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 3 } } } { \log n } } \end{array}$ and the statements of Lemma 10. We can then obtain the desired results by combining all pieces.

# D.3 Proof of Lemma 16

We first pro men ivalent to show that it holds with probability larger than $1 - { \frac { 1 } { 3 n ^ { 2 } } }$ $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$ $v \in \mathbb { S } ^ { d - 1 }$

$$
\begin{array} { r l } & { \Big | \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ) } - \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) } - \mathbb { E } [ v ^ { T } g ( X , \theta ) ] + \mathbb { E } [ v ^ { T } g ( X , \theta ^ { \prime } ) ] \Big | } \\ & { \le c \Big ( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } } + \frac { \log n } { n } d ^ { 1 + \gamma } \Big ) . } \end{array}
$$

Consider a minimal $\frac { 3 } { n }$ -covering set $\mathcal { A }$ of $\mathbb { S } ^ { d - 1 }$ such that $\mathcal { A } \subset \mathbb { S } ^ { d - 1 }$ , then $\log | { \mathcal { A } } | \leq d \log n$ . For any $v \in { \mathcal { A } }$ , define the function class

$$
\mathcal { G } _ { v } = \{ d ^ { - \gamma } ( v ^ { T } g ( \cdot , \theta ) - v ^ { T } g ( \cdot , \theta ^ { \prime } ) ) : \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) \} .
$$

Let $\overline { { \mathcal { G } } } _ { v } = \{ a f : a \in [ 0 , 1 ] , f \in \mathcal { G } _ { v } \}$ be the star hull of $\mathcal { G } _ { v }$ . Then since $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { X } , \theta \in B _ { r } ( \theta ^ { * } ) } \| g ( x , \theta ) \| \le C d ^ { \gamma } } \end{array}$ , it holds that $\begin{array} { r } { \operatorname* { s u p } _ { f \in \mathcal { \overline { G } } _ { v } , x \in \mathcal { X } } | f ( x ) | \leq 2 C } \end{array}$ . Consider the local Rademacher complexity associated with $\overline { { \mathcal { G } } } _ { v }$ ,

$$
\overline { { R } } _ { n } ( \delta ; \overline { { \mathcal { G } } } _ { v } ) = \mathbb { E } _ { X ^ { ( n ) } } \mathbb { E } _ { \varepsilon } \left[ \operatorname* { s u p } _ { \stackrel { f \in \overline { { \mathcal { G } } } _ { v } } { \mathbb { E } f ^ { 2 } \leq \delta ^ { 2 } } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } f ( X _ { i } ) \right| \right] ,
$$

where $\varepsilon _ { i }$ are i.i.d. samples from Rademacher distribution, i.e., $\mathbb { P } ( \varepsilon _ { i } = 1 ) = \mathbb { P } ( \varepsilon _ { i } = - 1 ) = 0 . 5$ . We will use the following uniform law, which is a special case of Theorem 14.20 of Wainwright [2019], to prove the desired result.

Lemma 19. (Wainwright [2019], Theorem $I 4 . 2 0 $ ) Given a uniformly $\boldsymbol { l }$ -bounded function class $\mathcal { F }$ that is star shaped around 0, let $\textstyle ( \delta ^ { * } ) ^ { 2 } \geq { \frac { c } { n } }$ be any solution to the inequality $\overline { { R } } _ { n } ( \delta ; \mathcal { F } ) \leq \delta ^ { 2 }$ , then we have

$$
\operatorname* { s u p } _ { f \in { \mathcal { F } } } { \frac { \left| { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } f ( X _ { i } ) - \mathbb { E } [ f ( X ) ] \right| } { \sqrt { \mathbb { E } [ f ( X ) ^ { 2 } ] } + \delta ^ { * } } } \leq 1 0 \delta ^ { * }
$$

with probability greater than $1 - c _ { 1 } \exp ( - c _ { 2 } \boldsymbol n \cdot ( \delta ^ { * } ) ^ { 2 } )$ .

Next we will use Dudley’s inequality (see for example, Theorem 5.22 of Wainwright [2019]) to determine the critical radius $\delta ^ { * }$ in Lemma 19. For $f , f ^ { \prime } : \mathcal { X }  \mathbb { R }$ , define the pseudometric

$$
d _ { n } ( f , f ^ { \prime } ) = { \sqrt { { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } ( f ( X _ { i } ) - f ^ { \prime } ( X _ { i } ) ) ^ { 2 } } } .
$$

Then by uniformly boundness of functions in class $\overline { { \mathcal { G } } } _ { v }$ , we can obtain that

$$
\begin{array} { r l } & { \log \mathbf { N } ( \mathcal { G } _ { v } , d _ { n } , \varepsilon ) } \\ & { \leq \log \frac { 4 C } { \varepsilon } + \log \mathbf { N } ( \mathcal { G } _ { v } , d _ { n } , \frac { \varepsilon } { 2 } ) } \\ & { \leq \log \frac { 4 C } { \varepsilon } + \log \mathbf { N } ( { \mathcal { B } _ { r } } ( { \theta ^ { * } } ) , d _ { n } ^ { g } , \frac { d ^ { \gamma } \varepsilon } { 2 } ) } \\ & { \leq C _ { 1 } d \log \frac { n } { \varepsilon } , } \end{array}
$$

where recall that $\mathbf { N } ( { \mathcal { F } } , d _ { n } , \varepsilon )$ denote the $\varepsilon$ -covering number of class $\mathcal { F }$ w.r.t pseudo-metric $d _ { n }$ . Let

$$
\begin{array} { r l } {  { r _ { n } ^ { 2 } = \operatorname* { s u p } _ { f , f ^ { \prime } \in \overline { { \mathscr { G } } } _ { v } \in \overline { { \mathscr { G } } } _ { n } } d _ { n } ^ { 2 } ( f , f ^ { \prime } ) } } \\ & { \le \operatorname* { s u p } _ { \mathbb { E } [ f ^ { 2 } ] , \operatorname* { s u f } [ f ^ { 2 } ] \le \delta ^ { 2 } } } \\ & { \le 4 \operatorname* { s u p } _ { f \in \mathscr { G } _ { v } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ^ { 2 } ( X _ { i } ) } \\ & { \le 8 \operatorname* { s u p } _ { f \in \mathscr { G } _ { v } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( f ( X _ { i } ) - \mathbb { E } f ( X ) ) ^ { 2 } + 8 \delta ^ { 2 } . } \\ & { \overset { \mathrm { E q } \ge 1 } { \le } \delta ^ { 2 } } \end{array}
$$

Then by (3.84) of Wainwright [2019], we can obtain that $\mathbb { E } [ r _ { n } ^ { 2 } ] \le C \delta ^ { 2 } + C \mathcal { R } _ { n } ( \delta )$ . Choose $\delta ^ { * } =$ $c d ^ { \frac { 1 } { 2 } } { \sqrt { \frac { \log n } { n } } }$ , then by Dudley’s inequality,

$$
\begin{array} { r l } & { \overline { { \xi } } _ { n } ( \delta ^ { * } ) \leq C \ \displaystyle \frac { 1 } { \sqrt { n } } \mathbb { E } \int _ { 0 } ^ { \tau _ { n } } d ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { n } { \varepsilon } } d \varepsilon } \\ & { \quad \quad \quad = C \ \displaystyle \frac { 1 } { \sqrt { n } } \mathbb { E } \int _ { 0 } ^ { 1 } r _ { n } d ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { n } { \varepsilon r _ { n } } } d \varepsilon } \\ & { \quad \quad \quad = C \mathbb { E } \left[ \displaystyle \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { 1 } r _ { n } d ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { n } { \varepsilon r _ { n } } } d \varepsilon \cdot 1 ( r _ { n } < n ^ { - \frac { 1 } { 2 } } ) \right] + C \mathbb { E } \left[ \displaystyle \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { 1 } r _ { n } d ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { n } { \varepsilon r _ { n } } } d \varepsilon \cdot 1 \right] } \\ & { \quad \quad \quad \leq C d ^ { \frac { 1 } { 2 } } \displaystyle \frac { \sqrt { \log n } } { n } + C \mathbb { E } \left[ \displaystyle \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { 1 } r _ { n } d ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { n ^ { \frac { 3 } { 2 } } } { \varepsilon } } d \varepsilon \right] } \\ & { \quad \quad \quad \leq C _ { 1 } \sqrt { \displaystyle \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } } \sqrt { \delta ^ { * 2 } + \widetilde { R } _ { n } } ( \delta ^ { * } ) . } \end{array}
$$

Then if $\overline { { { \mathcal { R } } } } _ { n } ( \delta ^ { * } ) > ( \delta ^ { * } ) ^ { 2 }$ , we can obtain that $\begin{array} { r } { \overline { { \mathcal { R } } } _ { n } ( \delta ^ { * } ) \leq 2 C _ { 1 } ^ { 2 } d \frac { \log n } { n } \leq 2 C _ { 1 } ^ { 2 } c ^ { - 2 } \delta ^ { * 2 } } \end{array}$ . thus when $c$ is large enough, $\delta ^ { * }$ solves the inequality $\overline { { { \mathcal { R } } } } _ { n } ( \delta ^ { * } ) \leq ( \delta ^ { * } ) ^ { 2 }$ . Then by Lemma 19 and the assumption that $\begin{array} { r } { \operatorname* { s u p } _ { v \in \mathbb { S } ^ { d - 1 } } \mathbb { E } \big [ ( v ^ { T } g ( X , \theta ) - v ^ { T } g ( X , \theta ^ { \prime } ) ) \big ] ^ { 2 } \leq C d ^ { \gamma _ { 3 } } \| \theta - \theta ^ { \prime } \| ^ { 2 \beta _ { 1 } } } \end{array}$ , there exists a constant $C$ such that it holds with probability larger than $1 - \exp ( - 4 d \log n )$ that for any $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$ ,

$$
\begin{array} { r l } & { \Big | \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ) } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) } - { \mathbb E } v ^ { T } g ( X , \theta ) + { \mathbb E } v ^ { T } g ( X , \theta ^ { \prime } ) \Big | } \\ & { \le C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } } + \frac { \log n } { n } d ^ { 1 + \gamma } \right) . } \end{array}
$$

By the fact that $\log | { \mathcal { A } } | \leq d \log n$ , it holds with probability larger than $1 - \exp ( - 3 d \log n )$ that for any $v \in { \mathcal { A } }$ and $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$ ,

$$
\begin{array} { r l } & { \Big | \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ) } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) } - { \mathbb E } v ^ { T } g ( X , \theta ) + { \mathbb E } v ^ { T } g ( X , \theta ^ { \prime } ) \Big | } \\ & { \le C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } } + \frac { \log n } { n } d ^ { 1 + \gamma } \right) . } \end{array}
$$

Moreover, for any $\widetilde v \in \mathbb { S } ^ { d - 1 }$ , there exists $v \in { \mathcal { A } }$ so that $\begin{array} { r } { \| v - \widetilde v \| \le \frac { 3 } { n } } \end{array}$ , hence for any $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$

$$
\begin{array} { l } { { \displaystyle \operatorname* { s u p } _ { v \in \mathbb S ^ { d - 1 } } \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \widetilde v ^ { T } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \widetilde v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) - \mathbb E \widetilde v ^ { T } g ( X , \theta ) + \mathbb E \widetilde v ^ { T } g ( X , \theta ^ { \prime } ) \Big | } } \\ { { \displaystyle = \operatorname* { s u p } _ { v \in \mathcal A } \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) - \mathbb E v ^ { T } g ( X , \theta ) + \mathbb E v ^ { T } g ( X , \theta ^ { \prime } ) \Big | + { \cal O } ( \frac { d } { \sqrt n } ) } . } \end{array}
$$

Then, it follows that it holds with probability larger than $\begin{array} { r } { 1 - \exp ( 3 d \log n ) \geq 1 - \frac { 1 } { 3 n ^ { 2 } } } \end{array}$ that

$$
\begin{array} { r l } & { \displaystyle \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \prime } ) - \mathbb { E } g ( X , \theta ) + \mathbb { E } g ( X , \theta ^ { \prime } ) \right\| } \\ & { \displaystyle = \operatorname* { s u p } _ { v \in \mathbb S ^ { d - 1 } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } g ( X _ { i } , \theta ^ { \prime } ) - \mathbb { E } v ^ { T } g ( X , \theta ) + \mathbb { E } v ^ { T } g ( X , \theta ^ { \prime } ) \right| } \\ & { \displaystyle \le C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } } + \frac { \log n } { n } d ^ { 1 + \gamma } \right) . } \end{array}
$$

The proof of the first statement is then completed. For the second statement, by the assumption that for any $\theta , \theta ^ { \prime } \in \Theta$ and $x \in \mathcal { X } , | \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) | \leq C d ^ { \gamma } \| \theta - \theta ^ { \prime } \|$ , we can obtain that for any $\theta , \theta ^ { \prime } \in \Theta$

$$
\begin{array} { r } { \mathbb { E } \big [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) ) ^ { 2 } \big ] \leq C ^ { 2 } d ^ { 2 \gamma } \| \theta - \theta ^ { \prime } \| ^ { 2 } , } \end{array}
$$

and

$$
\operatorname* { s u p } _ { x \in \mathcal { X } } \lvert \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) \rvert \leq C d ^ { \gamma } ( \lVert \theta \rVert + \lVert \theta ^ { \prime } \rVert ) \leq C _ { 1 } d ^ { \frac { 1 } { 2 } + \gamma } .
$$

We can therefore prove the second statement using the same strategy as the first statement. For the third statement, define $\begin{array} { r } { \delta _ { n } = ( \frac { \log n } { n } d ^ { - \frac { 3 } { 2 } } ) \wedge ( ( \frac { \log n } { n } ) ^ { \frac { 3 } { 2 } } d ^ { - \frac { 1 + \gamma _ { 3 } } { 2 } } ) ^ { \frac { 1 } { 1 + \beta _ { 1 } } } } \end{array}$ . For $\begin{array} { r } { k = 0 , 1 , \cdots , \lfloor \log _ { 2 } \frac { 2 r } { \delta _ { n } } \rfloor + 1 } \end{array}$ , we define the set

$$
\begin{array} { r l } & { \mathcal A _ { k } = \left\{ \begin{array} { l l } { \{ \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) : \| \theta - \theta ^ { \prime } \| \leq \delta _ { n } \} } & { k = 0 ; } \\ { \{ \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) : 2 ^ { k - 1 } \delta _ { n } < \| \theta - \theta ^ { \prime } \| \leq 2 ^ { k } \delta _ { n } \} } & { k = 1 , 2 , \cdots \lfloor \log _ { 2 } \frac { 2 r } { \delta _ { n } } \rfloor ; } \\ { \{ \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) : 2 ^ { k - 1 } \delta _ { n } < \| \theta - \theta ^ { \prime } \| \leq 2 r \} } & { k = \big \lfloor \log _ { 2 } \frac { 2 r } { \delta _ { n } } \big \rfloor + 1 . } \end{array} \right. } \end{array}
$$

$\begin{array} { r } { \{ \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) \} = \sum _ { k = 1 } ^ { \log _ { 2 } \lfloor \frac { 2 r } { \delta _ { n } } \rfloor + 1 } \mathcal { A } _ { k } } \end{array}$ . Fix an integer $\begin{array} { r } { 0 \leq k \leq \lfloor \log _ { 2 } \frac { 2 r } { \delta _ { n } } \rfloor + 1 } \end{array}$ , we consider the function set

$$
\mathcal { L } _ { k } = \Big \{ \frac { 1 } { 2 ^ { k } \delta _ { n } } d ^ { - \gamma } ( \ell ( \cdot , \theta ) - \ell ( \cdot , \theta ^ { \prime } ) - g ( \cdot , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) : ( \theta , \theta ^ { \prime } ) \in \mathcal { A } _ { k } \Big \} .
$$

k x∈X     c 122kδ2n d−2γ dγ3 (2kδn)2+2β1 ≤ c dγ3−2γ (2kδn)2β1 ≤ 4c dγ3−2γ (2k−1δn)2β1 . Then consider the star hull $\overline { { \mathcal { L } } } _ { k }$ of $\mathcal { L } _ { k }$ , by (1) $d \lesssim n ^ { \kappa _ { 2 } }$ ; (2) the Lipschitzness of $\ell$ ; (3) the bound on the $\varepsilon$ -covering number of $B _ { r } ( \theta ^ { * } ) \mathrm { w . r . t } d _ { n } ^ { g }$ , it holds that

$$
\begin{array} { l } { \log \mathbf { N } ( \overline { { \mathcal { L } } } _ { k } , d _ { n } , \varepsilon ) } \\ { \ \leq \log \displaystyle \frac { 2 c } { \varepsilon } + \log \mathbf { N } ( \mathcal { L } _ { k } , d _ { n } , \varepsilon ) } \\ { \ \leq C d \log \displaystyle \frac { n } { \varepsilon } . } \end{array}
$$

Then similar as the proof of the first statement, we can use Dudley’s inequality and Lemma 19 to obtain that there exists a constant $c$ such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { 3 n ^ { 3 } } }$ that for any $( \theta , \theta ^ { \prime } ) \in \mathcal { A } _ { k }$ ,

$$
\begin{array} { r l } & { \displaystyle \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { \prime } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \right. } \\ & { \displaystyle - \left( \mathbb { E } \ell ( X , \theta ) - \mathbb { E } \ell ( X , \theta ^ { \prime } ) - \mathbb { E } g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) \right) \bigg | } \\ & { \displaystyle \leq c \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \cdot ( 2 ^ { k - 1 } \delta _ { n } ) ^ { \beta _ { 1 } + 1 } + \frac { \log n } { n } d ^ { 1 + \gamma } \cdot ( 2 ^ { k - 1 } \delta _ { n } ) \right) } \\ & { \displaystyle \leq C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \cdot ( \| \theta - \theta ^ { \prime } \| + \delta _ { n } ) ^ { \beta _ { 1 } + 1 } + \frac { \log n } { n } d ^ { 1 + \gamma } \cdot ( \| \theta - \theta ^ { \prime } \| + \delta _ { n } ) \right) } \\ & { \displaystyle \leq 4 C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \theta - \theta ^ { \prime } \| ^ { \beta _ { 1 } + 1 } + \frac { \log n } { n } d ^ { 1 + \gamma } \| \theta - \theta ^ { \prime } \| + ( \frac { \log n } { n } ) ^ { 2 } \right) . } \end{array}
$$

Then by $\log _ { 2 } { \frac { r } { \delta _ { n } } } \lesssim \log n$ , consider the intersection of the above events for $\begin{array} { r } { k = 0 , 1 , \cdots , \lfloor \log _ { 2 } \frac { r } { \delta _ { n } } \rfloor + 1 } \end{array}$ we can obtain the desired result.

# D.4 Proof of Lemma 17

Recall $\begin{array} { r } { \widehat { \theta ^ { \diamond } } = \theta ^ { * } - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) } \end{array}$ , then by $\mathbb { E } [ g ( X , \theta ^ { * } ) = \nabla \mathcal { R } ( \theta ^ { * } ) = 0$ , we have

$$
\begin{array} { r l } & { \| \widehat { \theta } ^ { \diamond } - \theta ^ { * } \| = \| \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) ] \| } \\ & { \qquad = \displaystyle \operatorname* { s u p } _ { v \in \mathbb S ^ { d - 1 } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) ] \right| . } \end{array}
$$

It remains to derive a high probability bound of the supremum of the above empirical process. Consider a minimal $\frac { 3 } { n }$ -covering set $\mathcal { A }$ of $S ^ { d - 1 }$ such that − $A \subset \mathbb { S } ^ { d - 1 }$ , then $\log | \mathcal { A } | \leq d \log n$ . Fix an arbitrary $v \in$ , then by the assumption that (1) $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \mathbb { E } [ g ( X _ { i } , \theta ^ { * } ) ^ { T } g ( X _ { i } , \theta ^ { * } ) ] \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \preceq C d ^ { \gamma _ { 4 } } I _ { d }$ ; (2) for any $\theta \in \Theta$ , $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq C ^ { \prime } d ^ { - \gamma _ { 0 } } ( d ^ { - \gamma _ { 1 } } \wedge \Vert \theta - \theta ^ { * } \Vert ^ { 2 } )$ , which leads to $\mathcal { H } _ { \theta ^ { \ast } } \succeq C ^ { \prime } d ^ { - \gamma _ { 0 } } I _ { d }$ ; (3) $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { X } } \| g ( X , \theta ^ { * } ) \| \leq } \end{array}$ $C d ^ { \gamma }$ , we can obtain

$$
\operatorname* { s u p } _ { X \in \mathcal { X } \atop v \in \mathbb { S } ^ { d - 1 } } | v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) | \leq C C ^ { \prime } d ^ { \gamma + \gamma _ { 0 } } ,
$$

and

$$
\operatorname* { s u p } _ { v \in \mathbb { S } ^ { d - 1 } } \mathbb { E } [ v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) ] ^ { 2 } \leq C d ^ { \gamma _ { 4 } } .
$$

Therefore using Bernstein-type bound (see for example, Proposition 2.10 of Wainwright [2019]), we can get there exists a constant $c$ such that it holds with probability larger than $1 - \exp ( 3 d \log n )$ that,

$$
\left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } \mathcal { H } _ { \theta ^ { + } } ^ { - 1 } g ( X _ { i } , \theta ^ { + } ) - \mathbb { E } v ^ { T } \mathcal { H } _ { \theta ^ { + } } ^ { - 1 } g ( X , \theta ^ { + } ) \right| \leq C ( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } + d ^ { 1 + \gamma + \gamma _ { 0 } } \frac { \log n } { n } ) .
$$

Moreover, for any $\widetilde v \in \mathbb { S } ^ { d - 1 }$ , there exists $v \in { \mathcal { A } }$ so that $\begin{array} { r } { \| v - \widetilde v \| \le \frac { 3 } { n } } \end{array}$ , hence for any $\theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } )$ ,

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \widetilde { v } ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } \widetilde { v } ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) \bigg | \leq \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } v ^ { T } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) \bigg | } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad + \mathcal { O } ( d ^ { \gamma _ { 0 } + \gamma } \frac { \log n } { n } ) . } \end{array}
$$

Thus by a simple union bound, it holds with probability larger than $\begin{array} { r } { 1 - \exp ( 2 d \log n ) > 1 - \frac { 1 } { n ^ { 2 } } } \end{array}$ that

$$
\operatorname* { s u p } _ { v \in \mathbb S ^ { d - 1 } } \left| \frac 1 n \sum _ { i = 1 } ^ { n } v ^ { T } \mathcal H _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) - \mathbb E v ^ { T } \mathcal H _ { \theta ^ { * } } ^ { - 1 } g ( X , \theta ^ { * } ) \right| \le 2 C ( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } + d ^ { 1 + \gamma + \gamma _ { 0 } } \frac { \log n } { n } ) .
$$

We can thus obtain that it holds with probability larger than $1 - n ^ { - 2 }$ that

$$
\lVert \widehat { { \boldsymbol { \theta } } ^ { \diamond } } - { \boldsymbol { \theta } } ^ { * } \rVert \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } \sqrt { \frac { \log n } { n } } + C d ^ { 1 + \gamma + \gamma _ { 0 } } \frac { \log n } { n } .
$$

# D.5 Proof of Lemma 18

Firstly by $\mathcal { R } _ { n } ( \widehat { \theta } ) \leq \mathcal { R } _ { n } ( \theta ^ { * } )$ and $\mathcal { R } ( { \boldsymbol { \theta } } ) - \mathcal { R } ( { \boldsymbol { \theta } } ^ { * } ) \geq C ^ { \prime } d ^ { - \gamma _ { 0 } } ( d ^ { - \gamma _ { 1 } } \wedge \| { \boldsymbol { \theta } } - { \boldsymbol { \theta } } ^ { * } \| ^ { 2 } )$ , we can obtain that

$$
C ^ { \prime } d ^ { - \gamma _ { 0 } } ( d ^ { - \gamma _ { 1 } } \wedge \| \widehat \theta - \theta ^ { * } \| ^ { 2 } ) \leq \mathcal { R } ( \widehat \theta ) - \mathcal { R } ( \theta ^ { * } ) \leq \mathcal { R } ( \widehat \theta ) - \mathcal { R } ( \theta ^ { * } ) - \mathcal { R } _ { n } ( \widehat \theta ) + \mathcal { R } _ { n } ( \theta ^ { * } ) .
$$

It follows from the second statement of Lemma 16 that

$$
d ^ { - \gamma _ { 0 } } \bigl ( d ^ { - \gamma _ { 1 } } \wedge \| \widehat \theta - \theta ^ { * } \| ^ { 2 } \bigr ) \leq C \sqrt { \frac { \log n } { n } } d ^ { \frac 1 2 + \gamma } \| \widehat \theta - \theta ^ { * } \| + C \frac { \log n } { n } d ^ { \frac 3 2 + \gamma } .
$$

If $\lVert \widehat { { \boldsymbol { \theta } } } - { \boldsymbol { \theta } } ^ { * } \rVert \geq d ^ { - \frac { \gamma _ { 1 } } { 2 } }$ , then

$$
d ^ { - \gamma _ { 0 } - \gamma _ { 1 } } \leq C \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma } \lVert \widehat { \theta } - \theta ^ { * } \rVert + C \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } .
$$

On the other hand, as $\widehat { \theta } \in \Theta \subseteq [ - C , C ] ^ { d }$ , we have $\| { \widehat { \theta } } - \theta ^ { * } \| \leq 2 C { \sqrt { d } }$ , we can then obtain that when $\begin{array} { r } { d \leq c \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { 2 + 2 ( \gamma + \gamma _ { 0 } + \gamma _ { 1 } ) } } } \end{array}$ ,

$$
\begin{array} { r } { \sqrt { \frac { \log n } { n } } d ^ { \frac 1 2 + \gamma } \lVert \widehat { \theta } - \theta ^ { * } \rVert + \frac { \log n } { n } d ^ { \frac 3 2 + \gamma } \leq 2 C d ^ { 1 + \gamma } \sqrt { \frac { \log n } { n } } + \frac { \log n } { n } d ^ { \frac 3 2 + \gamma } } \\ { \leq 2 C \sqrt { c } d ^ { - \gamma _ { 0 } - \gamma _ { 1 } } + c d ^ { - \frac 1 2 - \gamma - 2 ( \gamma _ { 0 } + \gamma _ { 1 } ) } , } \end{array}
$$

which will cause contradiction when $c$ is sufficiently small. Hence we have $\lVert \widehat { { \boldsymbol { \theta } } } - { \boldsymbol { \theta } } ^ { * } \rVert < d ^ { - \frac { \gamma _ { 1 } } { 2 } }$ and thus

$$
d ^ { - \gamma _ { 0 } } \lVert \widehat { \boldsymbol { \theta } } - \boldsymbol { \theta } ^ { * } \rVert ^ { 2 } \leq C \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma } \lVert \widehat { \boldsymbol { \theta } } - \boldsymbol { \theta } ^ { * } \rVert + C \frac { \log n } { n } d ^ { \frac { 3 } { 2 } + \gamma } ,
$$

which leads to $\begin{array} { r } { \| \widehat { \theta } - \theta ^ { * } \| \leq C _ { 1 } \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma + \gamma _ { 0 } } } \end{array}$ q log nn d 12 +γ+γ0. We will first show the first statement of Lemma 18 and use the statement to improve the dependence of $d$ in the bound of $\sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma + \gamma _ { 0 } }$ .

By $\mathcal { R } _ { n } ( \widehat { \theta } ) \leq \mathcal { R } _ { n } ( \widetilde { \theta } )$ for any $\widetilde { \theta } \in B _ { r } ( \theta ^ { * } )$ , we can obtain that

$$
\begin{array} { r l } & { \displaystyle - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) } \\ & { \displaystyle \le { \mathcal R } _ { n } ( \widetilde { \theta } ) - { \mathcal R } _ { n } ( \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) } \\ & { \displaystyle \le \left| { \mathcal R } _ { n } ( \widetilde { \theta } ) - { \mathcal R } _ { n } ( \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) - { \mathcal R } ( \widetilde { \theta } ) + { \mathcal R } ( \widehat { \theta } ) + { \mathbb E } [ g ( X , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) ] \right| } \\ & { \displaystyle + \left| { \mathcal R } ( \widetilde { \theta } ) - { \mathcal R } ( \widehat { \theta } ) - { \mathbb E } [ g ( X , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) ] \right| . } \end{array}
$$

The first term can be bounded using the third statement of Lemma 16, that is

$$
\begin{array} { r l } & { \displaystyle \left. \mathcal { R } _ { n } ( \widetilde { \theta } ) - \mathcal { R } _ { n } ( \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) - \mathcal { R } ( \widetilde { \theta } ) + \mathcal { R } ( \widehat { \theta } ) + \mathbb { E } [ g ( X , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) ] \right. } \\ & { \le C \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \lVert \widehat { \theta } - \widetilde { \theta } \rVert ^ { \beta _ { 1 } + 1 } + C \frac { \log n } { n } d ^ { 1 + \gamma } \lVert \widehat { \theta } - \widetilde { \theta } \rVert + C ( \frac { \log n } { n } ) ^ { 2 } . } \end{array}
$$

The second term can be bounded using the twice differentiability of $\mathcal { R }$ around $\theta ^ { * }$ ,

$$
\left. \mathcal { R } ( \widetilde { \theta } ) - \mathcal { R } ( \widehat { \theta } ) - \mathbb { E } [ g ( X , \widehat { \theta } ) ( \widetilde { \theta } - \widehat { \theta } ) ] \right. \leq \frac { 1 } { 2 } \operatorname* { s u p } _ { c \in [ 0 , 1 ] } \| \mathcal { H } _ { c \widetilde { \theta } + ( 1 - c ) \widehat { \theta } } \| _ { \mathrm { o p } } \| \widehat { \theta } - \widetilde { \theta } \| ^ { 2 } \leq C d \| \widehat { \theta } - \widetilde { \theta } \| ^ { 2 } .
$$

where the last inequality is due to the assumption that the mixed partial derivatives of ${ \mathcal { R } } ( \theta )$ up to order two are uniformly bounded by an $( n , d )$ -independent constant on $B _ { r } ( \theta ^ { * } )$ . Then we choose $\stackrel { \sim } { \theta } = \stackrel { \widehat { \theta } } { \theta } -$

$t \frac { \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) } { \Vert \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \Vert }$ for a $t > 0$ that will be chosen later. Thus

$$
\begin{array} { r l r } & { } & { C _ { 1 } t \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| \leq \sqrt { \displaystyle \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } t ^ { \beta _ { 1 } + 1 } + \displaystyle \frac { \log n } { n } d ^ { 1 + \gamma } t + ( \frac { \log n } { n } ) ^ { 2 } + d t ^ { 2 } } \\ & { } & { \Rightarrow C _ { 1 } \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| \leq \sqrt { \displaystyle \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } t ^ { \beta _ { 1 } } + \displaystyle \frac { \log n } { n } d ^ { 1 + \gamma } + ( \frac { \log n } { n } ) ^ { 2 } / t + d t . } \end{array}
$$

Choose $\begin{array} { r } { t = \frac { \log n } { n } } \end{array}$ , we have it holds with probability at least $1 - n ^ { - 2 }$

$$
\left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| \leq C d ^ { 1 + \gamma } \frac { \log n } { n } + C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { 2 } + \beta _ { 1 } } .
$$

For the second statement, recall $\begin{array} { r } { \widehat { \theta ^ { \diamond } } = \theta ^ { * } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ) } \end{array}$ . By Lemma 17 and the assumption that $\begin{array} { r } { d \leq c \lfloor \frac { n } { \log n } ) ^ { \frac { 1 } { 2 + 2 ( \gamma + \gamma _ { 0 } + \gamma _ { 1 } ) } } } \end{array}$ , we can obtain $\| { \widehat { \theta } } ^ { \diamond } - \theta ^ { \ast } \| \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } { \sqrt { \frac { \log n } { n } } }$ . We claim that it suffices to show that

$$
\left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) \right\| \leq C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + C d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) } \frac { \log n } { n }
$$

holds with probability at least $1 - c n ^ { - 2 }$ . Indeed, under the above statement, we have

$$
\begin{array} { r l } & { \displaystyle | \mathbb { E } [ g ( X , \widehat { \theta } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] | } \\ & { \displaystyle \leq \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - \mathbb { E } [ g ( X , \widehat { \theta } ) ] + \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \right\| } \\ & { \displaystyle \ + \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) \right\| + \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) \right\| } \\ & { \displaystyle \leq C \left( \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \widehat { \theta } - \widehat { \theta ^ { \circ } } \| ^ { \beta _ { 1 } } + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) } \frac { \log n } { n } \right) , } \end{array}
$$

where the last inequality follows from the first statement of Lemma 16. On the other hand, by the Lipschitzness of $\mathcal { H } _ { \theta }$ around $\theta ^ { * }$ , we can obtain that,

$$
\begin{array} { r l } & { \lvert \mathbb { E } [ g ( X , \widehat { \theta } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] \rvert } \\ & { \geq \lVert \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \rVert - \lVert \mathbb { E } [ g ( X , \widehat { \theta } ) ] - \mathbb { E } [ g ( X , \widehat { \theta ^ { \circ } } ) ] - H _ { \theta ^ { * } } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \rVert } \\ & { = \lVert \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \rVert - \underset { v \in \mathbb { S } ^ { d - 1 } } { \operatorname* { s u p } } \left. \mathbb { E } [ v ^ { T } g ( X , \widehat { \theta } ) ] - \mathbb { E } [ v ^ { T } g ( X , \widehat { \theta ^ { \circ } } ) ] - v ^ { T } H _ { \theta ^ { * } } ( \widehat { \theta } - \widehat { \theta ^ { \circ } } ) \right. } \\ & { \geq \rho _ { 1 } ( \mathcal { H } _ { \theta ^ { * } } ) \lVert \widehat { \theta } - \widehat { \theta ^ { \circ } } \rVert - \underset { v \in \mathbb { S } ^ { d - 1 } } { \operatorname* { s u p } } \underset { \epsilon \in ( 0 , 1 ) } { \operatorname* { s u p } } \left. v ^ { T } ( \mathcal { H } _ { \widehat { \theta ^ { * } } + ( 1 - t ) \widehat { \theta } } - \mathcal { H } _ { \theta ^ { * } } ) ( \widehat { \theta } - \widehat { \theta ^ { * } } ) \right. } \\ & { \geq \rho _ { 1 } ( \mathcal { H } _ { \theta ^ { * } } ) \lVert \widehat { \theta } - \widehat { \theta ^ { \circ } } \rVert - C \left( d ^ { \frac { 1 } { 2 } + \gamma + \gamma _ { 2 } + \gamma _ { 0 } } \sqrt { \frac { \log n } { n } } \lVert \widehat { \theta } - \widehat { \theta ^ { * } } \rVert \right) , } \end{array}
$$

where the last inequality uses $\begin{array} { r } { \| \widehat { \theta } - \theta ^ { * } \| \leq C _ { 1 } \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 } { 2 } + \gamma + \gamma _ { 0 } } } \end{array}$ and $\| { \widehat { \theta ^ { \circ } } } - \theta ^ { * } \| \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } } { \sqrt { \frac { \log n } { n } } }$ log n with $\gamma _ { 4 } \leq 2 ( \gamma _ { 0 } + \gamma )$ . Hence when $\begin{array} { r } { d \leq c \big ( \frac { n } { \log n } \big ) ^ { \frac { 1 } { 1 + 2 \gamma + 2 \gamma _ { 2 } + 4 \gamma _ { 0 } } } } \end{array}$ for a sufficiently small $c$ , we can obtain that

$$
d ^ { - \gamma _ { 0 } } \| \widehat { \theta } - \widehat { \theta } ^ { \circ } \| \leq \sqrt { \frac { \log n } { n } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } } \| \widehat { \theta } - \widehat { \theta } ^ { \circ } \| ^ { \beta _ { 1 } } + d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) } \frac { \log n } { n } ,
$$

which leads to

$$
\widehat { \theta ^ { \circ } } \| \leq C \left( d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) + \gamma _ { 0 } } ( \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) + \gamma _ { 0 } } \frac { \log n } { n } + \Big ( d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \gamma _ { 0 } } \sqrt { \frac { \log n } { n } } \Big ) ^ { \frac { 1 } { 1 - \beta _ { 1 } } } \right)
$$

Now we show equation (30), using the first statement of Lemma 16, we can obtain that

$$
\begin{array} { r l } & { \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \widehat { \theta ^ { \circ } } ) + \mathbb { E } g ( X , \theta ^ { * } ) \right\| } \\ & { \leq C \left( \displaystyle \frac { \log n } { n } \right) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) } + C \displaystyle \frac { \log n } { n } d ^ { 1 + \gamma } . } \end{array}
$$

Moreover, by the Lipschitz continuity of $\mathcal { H } _ { \theta }$ around $\theta ^ { * }$ , we can obtain that

$$
\| \mathbb { E } g ( X , \widehat { \theta ^ { \circ } } ) - \mathbb { E } g ( X , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } - \theta ^ { * } ) \| \leq d ^ { \gamma _ { 2 } } \| \widehat { \theta ^ { * } } - \theta ^ { * } \| ^ { 2 } \leq C d ^ { 1 + \gamma _ { 4 } + \gamma _ { 2 } } \frac { \log n } { n } .
$$

Therefore, combined with the fact that $\begin{array} { r } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { \diamond } } - \theta ^ { * } ) = 0 } \end{array}$ , we can obtain that it holds with probability at least $1 - c n ^ { - 2 }$ that

$$
\begin{array} { r l } & { \left| \left| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) \right| \right| = \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { \circ } } - \theta ^ { * } ) \right\| } \\ & { \qquad \leq \left\| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta ^ { \circ } } ) - \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \widehat { \theta ^ { \circ } } ) + \mathbb { E } g ( X , \theta ^ { * } ) \right\| } \\ & { \qquad + \left\| \mathbb { E } g ( X , \widehat { \theta ^ { \circ } } ) - \mathbb { E } g ( X , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } ( \widehat { \theta ^ { * } } - \theta ^ { * } ) \right\| } \\ & { \qquad \leq C d ^ { \frac { 1 + \gamma _ { 3 } } { 2 } + \beta _ { 1 } ( \frac { 1 + \gamma _ { 4 } } { 2 } ) } ( \displaystyle \frac { \log n } { n } ) ^ { \frac { 1 + \beta _ { 1 } } { 2 } } + C d ^ { 1 + \gamma \vee ( \gamma _ { 2 } + \gamma _ { 4 } ) } \displaystyle \frac { \log n } { n } . } \end{array}
$$

# E Proof of Remaining Results

# E.1 Proof of Lemma 2

Let $\pi _ { \mathrm { l o c } } = [ { \sqrt { n } } ( \cdot - { \widehat { \theta } } ) ] _ { \# } \pi _ { n }$ and $\mu _ { \mathrm { l o c } } = [ \sqrt { n } ( \cdot - \widehat { \theta } ) ] _ { \# } \mu _ { 0 }$ . We can bound

$$
\begin{array} { r l } & { \quad - \underset { A : \pi _ { \alpha } ( A ) \ > 0 } { \operatorname* { s u p } } \pi _ { n } ( A ) } \\ & { \overset { ( a ) } { = } \underset { A \in K : \pi _ { \alpha } ( A ) \leq 0 } { \operatorname* { s u p } } \frac { \mu _ { \mathrm { l o c } } ( A ) } { \pi _ { \mathrm { l o c } } ( A ) } } \\ & { = \underset { A \in K : \pi _ { \alpha } ( A ) > 0 } { \operatorname* { s u p } } \frac { \mu _ { \mathrm { l o c } } ( A ) } { \pi _ { \mathrm { l o c } } ( K ( A ) ) } \cdot \frac { 1 } { \pi _ { \mathrm { l o c } } ( K ) } } \\ & { \quad \le \underset { A \in K } { \operatorname* { s u p } } \left[ \frac { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } \widetilde { J } ^ { - 1 } x ) } { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \widetilde { J } _ { n } ( x ) ) } \right] \cdot \frac { 1 } { \pi _ { \mathrm { l o c } } ( K ) } } \\ & { \quad \times \underset { x \in K } { \operatorname* { s u p } } \left[ \frac { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } \widetilde { J } ^ { - 1 } x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) } { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } \widetilde { J } ^ { - 1 } x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) } \cdot \underset { x \in K } { \operatorname* { s u p } } \frac { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) } { \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) } \right] } \\ &  \le \underset { x \in K } { \operatorname* { s u p } } \frac { \int _ { K } \exp ( - \frac { 1 } { 2 } x ^ { T } J x ) \mathrm { d } x \exp ( - \frac { 1 } { 2 } x ^ { T } \widetilde { J } ^ { - 1 } x ) }  \int _  K \end{array}
$$

where $( i )$ uses $\mu _ { \mathrm { l o c } } ( K ) = 0$ . Since for any function pair $f _ { 1 } , f _ { 2 }$ , it holds that

$$
\int _ { K } f _ { 1 } ( x ) \mathrm { d } x \cdot \operatorname* { s u p } _ { x \in K } { \frac { f _ { 2 } ( x ) } { f _ { 1 } ( x ) } } \geq \int _ { K } f _ { 1 } ( x ) { \frac { f _ { 2 } ( x ) } { f _ { 1 } ( x ) } } \mathrm { d } x = \int _ { K } f _ { 2 } ( x ) \mathrm { d } x ,
$$

we can obtain that

$$
M _ { 0 } \leq \operatorname* { s u p } _ { x \in K } \exp ( \vert x ^ { T } ( \widetilde { I } ^ { - 1 } - J ) x \vert ) \cdot \operatorname* { s u p } _ { x \in K } \exp \big ( 2 \big \vert V _ { n } ( x ) - \frac { 1 } { 2 } x ^ { T } J x \big \vert \big ) \cdot \frac { 1 } { \pi _ { \mathrm { l o c } } ( K ) } .
$$

# E.2 Proof of Corollary 1

We first verify that under Condition B.3’, Condition B.2 and Condition B.3 holds, where the function $g$ in Condition B.3 is chosen as the gradient $\nabla _ { \boldsymbol { \theta } } \ell$ . Condition B.2 and B.3.1 directly follows from the assumption that $\| \nabla _ { \theta } \ell ( x , \theta ) \| \le C d ^ { \gamma }$ . For Condition B.3.2, since $\left\| \operatorname { H e s s } _ { \boldsymbol { \theta } } ( \ell ( x , \theta ) ) \right\| _ { \mathrm { o p } } ^ { 2 } \leq C d ^ { \gamma _ { 3 } }$ , we have for any $x \in \mathcal { X }$ and $\theta \in \Theta$ ,

$$
\| \nabla _ { \theta } \ell ( x , \theta ) - \nabla _ { \theta } \ell ( x , \theta ^ { \prime } ) \| \leq \sqrt { C d ^ { \gamma _ { 3 } } } \| \theta - \theta ^ { \prime } \|
$$

and thus

$$
d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) \leq \sqrt { C d ^ { \gamma _ { 3 } } } \| \theta - \theta ^ { \prime } \| .
$$

Then the covering number condition for $d _ { n } ^ { g }$ follows from the fact that the $\varepsilon$ -covering number of unit $d$ - ball is bounded by $\displaystyle ( \frac { 3 } { \varepsilon } ) ^ { d }$ . Condition B.3.3 directly follows from the assumption that $\| \bar { \mathrm { H H e s s } } _ { \theta } ( \ell ( x , \theta ) ) \| _ { \mathrm { o p } } ^ { 2 } \leq$ $C d ^ { \gamma _ { 3 } }$ . Condition B.3.4 follows from the assumption that $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \preceq C d ^ { \gamma _ { 4 } } I _ { d }$ with $\Delta _ { \theta ^ { * } } = \mathbb { E } [ \nabla _ { \theta } \ell ( X , \theta ^ { * } )$ $\nabla _ { \theta } \ell ( X , \theta ^ { * } ) ^ { T } ]$ . Then the first statement directly follows from Theorem 2. For the second statement, we first verify that $\begin{array} { r } { \widetilde { I } ^ { - 1 } = | S | ^ { - 1 } \sum _ { i \in S } \mathrm { H e s s } _ { \theta } ( \ell ( \dot { X } _ { i } , \widehat { \theta } ) ) } \end{array}$ is a reasonable estimator to $\mathcal { H } _ { \theta ^ { \ast } }$ in the following lemma.

Lemma 20. Under assumptions in Corollary $I$ , let $m = | S |$ , it holds with probability larger than $1 - n ^ { - 2 }$ that

$$
\bigl \| \widetilde { I } ^ { - 1 } - \mathcal { H } _ { \theta ^ { * } } \bigr \| _ { \mathrm { o p } } \leq C \bigl ( d ^ { \frac { \gamma _ { 3 } + 1 } { 2 } } \sqrt { \frac { \log n } { m } } \bigr ) \vee \bigl ( d ^ { \frac { \gamma _ { 3 } + 2 } { 2 } } \frac { \log n } { m } \bigr ) \vee \bigl ( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \sqrt { \frac { \log n } { n } } \bigr ) .
$$

Then since $\| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| \leq C d ^ { \gamma _ { 0 } } , d \leq c \frac { n ^ { \kappa _ { 1 } } } { \log n }$ and $m \geq C _ { 2 } d ^ { \gamma _ { 3 } + 2 \gamma _ { 0 } + \frac { 7 } { 3 } }$ , we have

$$
\| \widetilde { I } \| _ { \mathrm { o p } } \le 2 C d ^ { \gamma _ { 0 } } ,
$$

and

$$
\begin{array} { r l } & { \ \lVert \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } - I _ { d } \rVert _ { \mathrm { o p } } \leq \lVert \widetilde { I } \rVert _ { \mathrm { o p } } \lVert \widetilde { I } ^ { - 1 } - \mathcal { H } _ { \theta ^ { * } } \rVert _ { \mathrm { o p } } } \\ & { \qquad \leq C d ^ { \gamma _ { 0 } } \big ( d ^ { \frac { \gamma _ { 3 } + 1 } { 2 } } \sqrt { \frac { \log n } { m } } \big ) \vee \big ( d ^ { \frac { \gamma _ { 3 } + 2 } { 2 } } \frac { \log n } { m } \big ) \vee \big ( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \sqrt { \frac { \log n } { n } } \big ) } \\ & { \qquad \leq \frac { 1 } { 2 } , } \end{array}
$$

which leads to

$$
\frac { 1 } { 2 } I _ { d } \preceq \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } \preceq 2 I _ { d } .
$$

Then by

$$
\mathcal { H } _ { { \theta } ^ { \ast } } = \widetilde { I } ^ { - \frac { 1 } { 2 } } \big ( \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { { \theta } ^ { \ast } } \widetilde { I } ^ { \frac { 1 } { 2 } } \big ) \widetilde { I } ^ { - \frac { 1 } { 2 } } ,
$$

we have

$$
\begin{array} { r l } & { \| \widetilde { I } \| _ { \mathrm { o p } } \leq 2 \| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } } ; } \\ & { \| \widetilde { I } ^ { - 1 } \| _ { \mathrm { o p } } \leq 2 \| \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } . } \end{array}
$$

y, we will control theis a constant so that $\widetilde { I }$ Lemma 2. Recall . By $\rho _ { 2 } = 2$ $\rho _ { 1 } =$ $\textstyle { \frac { 1 } { 2 } }$ $\mu _ { 0 } = N _ { d } ( \widehat { \theta } , n ^ { - 1 } \widetilde { I } ) \big | _ { \{ \theta : \sqrt { n } \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat { \theta } ) \| \leq 3 \sqrt { c _ { 1 } d } \} } .$ $c _ { 1 }$ $c _ { 1 } \geq 9 \vee \operatorname* { s u p } _ { i \in [ d ] , j \in [ d ] } \frac { \partial ^ { 2 } \mathcal { R } ( \theta ^ { * } ) } { \partial \theta _ { i } \partial \theta _ { j } }$

$$
\lVert \widetilde { I } ^ { - \frac { 1 } { 2 } } \rVert _ { \mathrm { o p } } \leq \sqrt { 2 } \lVert \mathcal { H } _ { \theta ^ { * } } ^ { \frac { 1 } { 2 } } \rVert _ { \mathrm { o p } } \leq \sqrt { 2 d \operatorname* { s u p } _ { i \in [ d ] , j \in [ d ] } \frac { \partial ^ { 2 } \mathcal { R } ( \theta ^ { * } ) } { \partial \theta _ { i } \partial \theta _ { j } } } \leq \sqrt { 2 c _ { 1 } d } ,
$$

and Lemma 11, we can obtain that

$$
\begin{array} { r } { \pi _ { n } \Big ( \sqrt { n } \| \widetilde { I } ^ { - \frac { 1 } { 2 } } ( \theta - \widehat \theta ) \| \le 2 \sqrt { c _ { 1 } d } \Big ) \ge 1 - \exp ( - 1 ) . } \end{array}
$$

Moreover, consider $K = \{ \xi : \widetilde { I } ^ { - \frac { 1 } { 2 } } \xi \leq 2 \sqrt { c _ { 1 } d } \}$ , then for any $\xi \in K$ , we have

$$
\| \xi \| \leq 2 \| \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \sqrt { c _ { 1 } d } \leq 2 \sqrt { 2 c _ { 1 } d } \| \mathcal { H } _ { \theta ^ { * } } ^ { - \frac { 1 } { 2 } } \| _ { \mathrm { o p } } \leq c _ { 2 } d ^ { \frac { 1 + \gamma _ { 0 } } { 2 } } .
$$

Then by Lemma 1, when $\begin{array} { r } { d \leq c \frac { n ^ { \kappa _ { 1 } } } { \log n } } \end{array}$ for a small enough $c$ , for any $\xi \in K$ , we have

$$
\left| V _ { n } ( \xi ) - \frac { \xi ^ { T } \mathcal { H } _ { \theta ^ { * } } \xi } { 2 } \right| \leq \frac { 1 } { 2 } .
$$

In addition, for any $\xi \in K$ , we have

$$
\begin{array} { r l } & { \underset { \xi \in \mathcal { K } } { \operatorname* { s u p } } \big | \xi ^ { T } ( \widetilde { I } ^ { - 1 } - \mathcal { H } _ { \theta ^ { \star } } ) \xi \big | = \underset { \| \xi \| \leq 2 \sqrt { c _ { 1 } d } } { \operatorname* { s u p } } \big | \xi ^ { T } ( I _ { d } - \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { \star } } \widetilde { I } ^ { \frac { 1 } { 2 } } ) \xi \big | } \\ & { \qquad \leq 2 c _ { 1 } d \| I _ { d } - \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { \star } } \widetilde { I } ^ { \frac { 1 } { 2 } } \| _ { \mathrm { l o p } } } \\ & { \qquad \leq 2 c _ { 1 } C d ^ { \gamma _ { 0 } + 1 } \big ( d ^ { \frac { \gamma _ { 3 } + 1 } { 2 } } \sqrt { \frac { \log n } { m } } \big ) \vee \big ( d ^ { \frac { \gamma _ { 3 } + 2 } { 2 } } \frac { \log n } { m } \big ) \vee \big ( d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \sqrt { \frac { \log n } { n } } \big ) } \\ & { \qquad \leq d ^ { \frac { 1 } { 3 } } , } \end{array}
$$

where the last inequality uses d ≤ c nκ1log n and $m \ge C _ { 2 } d ^ { \gamma _ { 3 } + 2 \gamma _ { 0 } + \frac 7 3 }$ . The desired result then follows from Lemma 2.

# E.3 Proof of Lemma 20

Since $\mathbb { E } [ \widetilde { I } ^ { - 1 } ] = \mathcal { H } _ { \widehat { \theta } } .$ , we have

$$
\begin{array} { r } { \left\| \widetilde { I } ^ { - 1 } - \mathcal { H } _ { \theta ^ { * } } \right\| _ { \mathrm { o p } } \leq \left\| \widetilde { I } ^ { - 1 } - \mathcal { H } _ { \widehat { \theta } } \right\| _ { \mathrm { o p } } + \left\| \mathcal { H } _ { \widehat { \theta } } - \mathcal { H } _ { \theta ^ { * } } \right\| _ { \mathrm { o p } } . } \end{array}
$$

The second term can be bounded using Condition B.1.2 and equation (27) in the proof of Lemma 10, that is

$$
\left\| | \mathcal { H } _ { \widehat { \theta } } - \mathcal { H } _ { \theta ^ { * } } | \right\| _ { \mathrm { o p } } \leq C d ^ { \gamma _ { 2 } } \| \widehat { \theta } - \theta ^ { * } \| \leq C d ^ { \frac { 1 + \gamma _ { 4 } } { 2 } + \gamma _ { 2 } } \sqrt { \frac { \log n } { n } } .
$$

The first term can be bounded using Bernstein’s inequality. Let $m = | S |$ , for $v , v ^ { \prime } \in \mathbb { S } ^ { d - 1 }$ and $\theta , \theta ^ { \prime } \in$ $B _ { r } ( \theta ^ { * } )$ , we have

$$
\begin{array} { r l } & { \sqrt { m ^ { - 1 } \displaystyle \sum _ { i \in S } \left( \boldsymbol { v } ^ { T } \mathrm { H e s s } _ { \boldsymbol { \theta } } ( \boldsymbol { \ell } ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ) ) \boldsymbol { v } - { v ^ { \prime } } ^ { T } \mathrm { H e s s } _ { \boldsymbol { \theta } } ( \boldsymbol { \ell } ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ^ { \prime } ) ) { v ^ { \prime } } \right) ^ { 2 } } } \\ & { \leq C \sqrt { d } \| \boldsymbol { v } - \boldsymbol { v } ^ { \prime } \| + C d ^ { r _ { 1 } } \| \boldsymbol { \theta } - \boldsymbol { \theta } ^ { \prime } \| . } \end{array}
$$

Then consider $\mathcal { N } _ { v }$ and $\mathcal { N } _ { \theta }$ to be the minimal $n ^ { - 1 }$ and $n ^ { - 1 } d ^ { - r _ { 1 } }$ covering set of $\mathbb { S } ^ { d - 1 }$ and $B _ { r } ( \theta ^ { * } )$ , then $\log | \mathcal { N } _ { v } | \leq C d \log n$ and $\log | \mathcal { N } _ { \theta } | \leq C d \log n$ . Using the fact that

$$
\operatorname* { s u p } _ { \theta \in B _ { r } ( \theta ^ { * } ) , X \in \mathcal { X } } \lVert \mathrm { H e s s } _ { \theta } ( \ell ( X , \theta ) ) \rVert _ { \mathrm { o p } } \leq C d ^ { \frac { \gamma _ { 3 } } { 2 } } ;
$$

$$
\operatorname* { s u p } _ { \theta \in B _ { r } ( \theta ^ { * } ) \ v \in \mathbb S ^ { d - 1 } } \mathbb { E } \big [ ( v ^ { T } \mathrm { H e s s } _ { \theta } ( \ell ( X , \theta ) ) ^ { 2 } \big ] \leq \operatorname* { s u p } _ { \theta , \theta ^ { \prime } \in B _ { r } ( \theta ^ { * } ) } \mathbb { E } \Big [ \frac { \big ( v ^ { T } \nabla \ell ( X , \theta ) - v ^ { T } \nabla \ell ( X , \theta ^ { \prime } ) \big ) ^ { 2 } } { \| \theta - \theta ^ { \prime } \| ^ { 2 } } \Big ] \leq C d ^ { \gamma }
$$

we can get by Bernstein’s inequality and a simple union bound argument that it holds with probability at least $1 - n ^ { - c }$ that for any $v \in \mathcal { N } _ { v }$ and $\theta \in { \mathcal { N } } _ { \theta }$ ,

$$
\operatorname* { s u p } _ { \theta \in B _ { r } ( \theta ^ { * } ) \ : v \in \mathbb S ^ { d - 1 } } \left( v ^ { T } ( m ^ { - 1 } \sum _ { i \in S } \mathrm { H e s s } _ { \theta } ( \ell ( X _ { i } , \theta ) ) - \mathcal { H } _ { \theta } ) v ^ { T } \right) \leq C \left( d ^ { \frac { \gamma _ { 3 } + 1 } { 2 } } \sqrt { \frac { \log n } { m } } \right) \vee ( d ^ { \frac { \gamma _ { 3 } + 2 } { 2 } } \frac { \log n } { m } ) .
$$

# E.4 Proof of Corollary 2

We will first check that Conditions B.1-B.3 hold for the quantile regression example under Condition D.1 and D.2. Consider the loss function

$$
\ell ( X , \theta ) = ( Y - \widetilde { X } ^ { T } \theta ) ( \tau - \mathbf { 1 } ( Y < \widetilde { X } ^ { T } \theta ) ) ,
$$

and its subgradient

$$
g ( X , \theta ) = ( \mathbf { 1 } ( Y < \widetilde { X } ^ { T } \theta ) - \tau ) \widetilde { X } .
$$

Then we can write

$$
\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ] = \mathbb { E } \big [ \tau \left( Y - \widetilde { X } ^ { T } \theta \right) \big ] - \mathbb { E } \Big [ \int _ { - \infty } ^ { \widetilde { X } ^ { T } \theta - \widetilde { X } ^ { T } \theta ^ { * } } ( \varepsilon + \widetilde { X } ^ { T } \theta ^ { * } - \widetilde { X } ^ { T } \theta ) f _ { \epsilon } ( \varepsilon ) d \varepsilon \Big ] .
$$

Taking derivative of $\mathcal { R }$ w.r.t $\theta$ , we can obtain

$$
\nabla \mathcal { R } ( \theta ) = - \tau \cdot \mathbb { E } [ \widetilde { X } ] + \mathbb { E } [ \mathbf { 1 } ( Y < \widetilde { X } ^ { T } \theta ) \widetilde { X } ] = \mathbb { E } g ( X , \theta ) .
$$

Thus,

$$
\mathcal { H } _ { \boldsymbol { \theta } } = \mathbb { E } [ f _ { e } ( \widetilde { X } ^ { T } \boldsymbol { \theta } - \widetilde { X } ^ { T } \boldsymbol { \theta } ^ { * } ) \widetilde { X } \widetilde { X } ^ { T } ] .
$$

Then for $\theta \in B _ { c / \sqrt { d } } ( \theta ^ { * } )$ with a small enough $c$ , it holds that

$$
\frac { f _ { e } ( \widetilde { X } ^ { T } \theta - \widetilde { X } ^ { T } \theta ^ { * } ) } { f _ { e } ( 0 ) } \geq \frac { 1 } { 2 } .
$$

Then by the fact that $\nabla \mathcal { R } ( \theta ^ { * } ) = 0$ and $\mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] \succeq C ^ { \prime } d ^ { - \alpha _ { 0 } } I _ { d }$ , we can obtain that for any $\theta \in B _ { \frac { c } { \sqrt { d } } } ( \theta ^ { * } )$ ,

$$
\begin{array} { r } { \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq C _ { 1 } d ^ { - \alpha _ { 0 } } \| \theta - \theta ^ { * } \| ^ { 2 } ; } \end{array}
$$

on the other hand, for any $\theta \in B _ { \frac { c } { \sqrt { d } } } ( \theta ^ { * } ) ^ { c }$ ,

$$
\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq \mathcal { R } \Big ( \theta ^ { * } + \frac { c ( \theta - \theta ^ { * } ) } { \sqrt { d } \| \theta - \theta ^ { * } \| } \Big ) - \mathcal { R } ( \theta ^ { * } ) \geq C _ { 1 } d ^ { - \alpha _ { 0 } - 1 } ,
$$

hence for any $\boldsymbol { \theta } \in \mathbb { R } ^ { d }$ ,

$$
\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq C _ { 1 } d ^ { - \alpha _ { 0 } } ( d ^ { - 1 } \wedge \Vert \theta - \theta ^ { * } \Vert ^ { 2 } ) .
$$

Moreover, for any $\theta \in \Theta$ and $v \in \mathbb { S } ^ { d - 1 }$ ,

$$
\begin{array} { r l } & { | v ^ { T } ( \mathcal { H } _ { \theta } - \mathcal { H } _ { \theta ^ { * } } ) v | \leq v ^ { T } \mathbb { E } \left[ \left| f _ { e } \big ( \widetilde { X } ^ { T } \theta - \widetilde { X } ^ { T } \theta ^ { * } \big ) - f _ { e } ( 0 ) \right| \widetilde { X } \widetilde { X } ^ { T } \right] v } \\ & { \qquad \leq C \mathbb { E } \left[ | \widetilde { X } ^ { T } ( \theta - \theta ^ { * } ) | v ^ { T } \widetilde { X } \widetilde { X } ^ { T } v \right] } \\ & { \qquad \leq C \| \theta - \theta ^ { * } \| \mathbb { E } \left( \left| \widetilde { X } ( \theta - \theta ^ { * } ) / \| \theta - \theta ^ { * } \| \right| ^ { 3 } \right) ^ { \frac { 1 } { 3 } } ( \mathbb { E } | v ^ { T } \widetilde { X } | ^ { 3 } ) ^ { \frac { 2 } { 3 } } } \\ & { \qquad \leq C d ^ { \alpha _ { 1 } } \| \theta - \theta ^ { * } \| , } \end{array}
$$

where the last inequality uses the assumption that $\begin{array} { r } { \operatorname* { s u p } _ { \eta \in \mathbb { S } ^ { d - 1 } } \mathbb { E } [ \eta ^ { T } \widetilde { X } ] \le C d ^ { \alpha _ { 1 } } } \end{array}$ . Thus we have Condition B.1 holds with $\gamma _ { 0 } = \alpha _ { 0 }$ , $\gamma _ { 1 } = 1$ , $\gamma _ { 2 } = \alpha _ { 1 }$ . For Condition B.2, by $\mathcal { X } = \operatorname { s u p p } ( \widetilde { X } ) \subseteq [ - C , C ] ^ { d }$ , we can obtain $\| g ( X , \theta ) \| \leq C { \sqrt { d } }$ , thus for any $\begin{array} { r } { \boldsymbol { \imath } , \theta ^ { \prime } , | \ell ( \boldsymbol { X } , \theta ) - \ell ( \boldsymbol { X } , \theta ^ { \prime } ) | \leq C \sqrt { d } \| \theta - \theta ^ { \prime } \| } \end{array}$ and Condition B.2 and Condition B.3.1 hold with $\begin{array} { r } { \gamma = \frac { 1 } { 2 } } \end{array}$ . For Condition B.3, since for any $\theta , \theta ^ { \prime } \in \Theta$ ,

$$
\begin{array} { r } { \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| ^ { 2 } } = \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| \widetilde X _ { i } \| ^ { 2 } ( { \bf 1 } ( Y < \widetilde X _ { i } ^ { T } \theta ) - { \bf 1 } ( Y < \widetilde X _ { i } ^ { T } \theta ^ { \prime } ) ) ^ { 2 } } } \\ { = \sqrt { d } \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } ( { \bf 1 } ( Y < \widetilde X _ { i } ^ { T } \theta ) - { \bf 1 } ( Y < \widetilde X _ { i } ^ { T } \theta ^ { \prime } ) ) ^ { 2 } } , } \end{array}
$$

by Lemma 9.8 and Lemma 9.12 of Kosorok [2008], the function class $\mathcal { F } = \{ \mathbf { 1 } ( Y \leq \theta ^ { T } \widetilde { X } ) , \theta \in \Theta \}$ is a VC-class with VC-dimension being bouned by $d + 3$ , then using Theorem 8.3.18 of Vershynin [2018] on the covering number’s upper bound via VC dimension, we can verify Condition B.3.2.

For Condition B.3.3, since for any $v \in \mathbb { S } ^ { d - 1 }$ and $\theta , \theta ^ { \prime } \in \Theta$ ,

$$
\begin{array} { r l } & { \mathbb { E } ( v ^ { T } g ( X , \theta ) - v ^ { T } g ( X , \theta ^ { \prime } ) ) ^ { 2 } = \mathbb { E } [ ( \mathbf { 1 } ( Y < \tilde { X } _ { i } ^ { T } \theta ) - \mathbf { 1 } ( Y < \tilde { X } _ { i } ^ { T } \theta ^ { \prime } ) ) ^ { 2 } ( v ^ { T } \tilde { X } ) ^ { 2 } ] } \\ & { \qquad = \mathbb { E } [ ( v ^ { T } \tilde { X } ) ^ { 2 } \int _ { \tilde { X } ^ { T } \theta \wedge \tilde { X } ^ { T } \theta ^ { \prime } } ^ { \tilde { X } ^ { T } \theta \vee \tilde { X } ^ { T } \theta ^ { \prime } } f ( y - \tilde { X } ^ { T } \theta ^ { * } | \tilde { X } ) \mathrm { d } y ] } \\ & { \qquad \leq C \mathbb { E } [ ( v ^ { T } \tilde { X } ) ^ { 2 } | \tilde { X } ^ { T } \theta - \tilde { X } ^ { T } \theta ^ { \prime } ] ] } \\ & { \qquad \leq C \| \theta - \theta ^ { \prime } \| \underset { v \in \mathbb { S } ^ { d - 1 } } { \operatorname* { s u p } } \mathbb { E } | v ^ { T } \tilde { X } | ^ { 3 } \leq C d ^ { \alpha _ { 1 } } \| \theta ^ { \prime } - \theta \| ; } \end{array}
$$

$$
\begin{array} { r l } & { \mathbb { E } \big [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) - g ( X , \theta ^ { \prime } ) ( \theta - \theta ^ { \prime } ) ) ^ { 2 } \big ] } \\ & { = \mathbb { E } \big [ \big ( - ( Y - \widetilde { X } ^ { T } \theta ) \mathbf { 1 } ( Y < \widetilde { X } _ { i } ^ { T } \theta ) + ( Y - \widetilde { X } ^ { T } \theta ^ { \prime } ) \mathbf { 1 } ( Y < \widetilde { X } _ { i } ^ { T } \theta ^ { \prime } ) - \mathbf { 1 } ( Y < \widetilde { X } _ { i } ^ { T } \theta ^ { \prime } ) \widetilde { X } ^ { T } ( \theta - \theta ^ { \prime } ) \big ) ^ { 2 } } \\ & { = \mathbb { E } \left[ \int _ { \widetilde { X } ^ { T } \theta \wedge \widetilde { X } ^ { T } \theta ^ { \prime } } ^ { \widetilde { X } ^ { T } \theta \vee \widetilde { X } ^ { T } \theta ^ { \prime } } ( y - \widetilde { X } ^ { T } \theta ) ^ { 2 } f ( y - \widetilde { X } \theta ^ { * } | \widetilde { X } ) \mathrm { d } y \right] } \\ & { \leq C \mathbb { E } \big | \widetilde { X } ^ { T } \theta - \widetilde { X } ^ { T } \theta ^ { \prime } \big | ^ { 3 } \leq C d ^ { \alpha _ { 1 } } \left\| \theta ^ { \prime } - \theta \right\| ^ { 3 } . } \end{array}
$$

Thus Condition B.3.3 holds with $\gamma _ { 3 } = \alpha _ { 1 }$ and $\beta _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ . For condition B.3.4, since

$$
[ g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } ] = \mathbb { E } \big [ ( \tau ^ { 2 } + \mathbf { 1 } ( Y < \tilde { X } ^ { T } \theta ) - 2 \tau \mathbf { 1 } ( Y < \tilde { X } ^ { T } \theta ) ) \tilde { X } \tilde { X } ^ { T } \big ] = ( \tau - \tau ^ { 2 } ) \mathbb { E } [ \tilde { X } \tilde { X } ^ { T } ] ,
$$

and $J = \mathcal { H } _ { \theta ^ { * } } = f _ { e } ( 0 ) \mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ]$ , we have

$$
( { \mathbb E } [ \widetilde X \widetilde X ^ { T } ] ) ^ { \frac { 1 } { 2 } } J ^ { - 1 } ( { \mathbb E } [ \widetilde X \widetilde X ^ { T } ] ) ^ { \frac { 1 } { 2 } } = f _ { e } ( 0 ) ^ { - 1 } I _ { d } ,
$$

and thus $\gamma _ { 4 } = \gamma _ { 0 }$ .

Now we verify that the requirements of the $\widetilde { I }$ in Theorem 2 are satisfied. Recall $\begin{array} { r } { \widetilde { I } ^ { - 1 } = \frac { 1 } { | S | } \sum _ { i \in S } X _ { i } X _ { i } ^ { T } . } \end{array}$ in order to show that $\lVert \widetilde { I } ^ { - \frac { 1 } { 2 } } J ^ { - 1 } \widetilde { I } ^ { - \frac { 1 } { 2 } } \rVert _ { \mathrm { o p } } \vee \lVert \widetilde { I } ^ { \frac { 1 } { 2 } } J \widetilde { I } ^ { \frac { 1 } { 2 } } \rVert _ { \mathrm { o p } }$ is bounded above by a constant, we will derive upper bound to the term of $\| \widetilde { I } ^ { \frac { 1 } { 2 } } ( \mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] ) \widetilde { I } ^ { \frac { 1 } { 2 } } - I _ { d } \| _ { \mathrm { o p } }$ . Let $m = | S |$ , similar as the proof for Lemma 20, we can obtain it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\begin{array} { r l } & { \left\| \left| \displaystyle n ^ { - 1 } \sum _ { i = 1 } ^ { n } { \widetilde X } _ { i } { \widetilde X } _ { i } ^ { T } - \mathbb { E } [ { \widetilde X } { \widetilde X } ^ { T } ] \right| \right\| _ { \mathrm { o p } } \leq C \operatorname* { s u p } _ { v \in \mathbb S ^ { d - 1 } } \sqrt { \mathbb { E } | v ^ { T } { \widetilde X } | ^ { 4 } } d ^ { \frac { 1 } { 2 } } \sqrt { \frac { \log n } { m } } + d ^ { 2 } \frac { \log n } { m } } \\ & { \leq C d ^ { \frac { 3 } { 4 } + \frac { \alpha _ { 1 } } { 2 } } \sqrt { \displaystyle \frac { \log n } { m } } + d ^ { 2 } \frac { \log n } { m } , } \end{array}
$$

where the last inequality is due to $\operatorname* { s u p } _ { v \in \mathbb { S } ^ { d - 1 } } \sqrt { \mathbb { E } | v ^ { T } \widetilde { X } | ^ { 4 } } \leq C d ^ { \frac { 1 } { 4 } } \operatorname* { s u p } _ { v \in \mathbb { S } ^ { d - 1 } } \sqrt { \mathbb { E } | v ^ { T } \widetilde { X } | ^ { 3 } } \leq C d ^ { \frac { 1 + 2 \alpha _ { 1 } } { 4 } }$ . Then by $\mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] \succeq C ^ { \prime } d ^ { - \alpha _ { 0 } } I _ { d }$ , and $m \geq C _ { 2 } d ^ { \alpha _ { 1 } + 2 \alpha _ { 0 } + 3 / 2 } \log n$ , we can obtain

$$
\| \widetilde { I } \| _ { \mathrm { o p } } \leq \frac { 2 } { C ^ { \prime } } d ^ { \alpha _ { 0 } }
$$

Thus we have

$$
\| \tilde { I } ^ { \frac { 1 } { 2 } } ( \mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] ) \widetilde { I } ^ { \frac { 1 } { 2 } } - I _ { d } \| _ { \mathrm { o p } } \le \| \widetilde { I } \| _ { \mathrm { o p } } \| \widetilde { I } ^ { - 1 } - ( \mathbb { E } [ \widetilde { X } \widetilde { X } ^ { T } ] ) \| _ { \mathrm { o p } } \le C _ { 1 } d ^ { \alpha _ { 0 } + \frac { 3 + 2 \alpha _ { 1 } } { 4 } } \sqrt { \frac { \log n } { m } } ,
$$

which leads to

$$
\frac { 1 } { 2 } I _ { d } \preceq \widetilde { I } ^ { \frac { 1 } { 2 } } ( \mathbb { E } [ X X ^ { T } ] ) \widetilde { I } ^ { \frac { 1 } { 2 } } \preceq 2 I _ { d } ,
$$

Thus

$$
\frac { 1 } { 2 } f _ { e } ( 0 ) I _ { d } \preceq \widetilde { I } ^ { \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } \widetilde { I } ^ { \frac { 1 } { 2 } } \preceq 2 f _ { e } ( 0 ) I _ { d }
$$

Furthermore, by

$$
\mathcal { H } _ { { \theta } ^ { \ast } } = f _ { e } ( 0 ) \cdot \widetilde { I } ^ { - \frac { 1 } { 2 } } \big ( \widetilde { I } ^ { \frac { 1 } { 2 } } ( \mathbb { E } [ X X ^ { T } ] ) \widetilde { I } ^ { \frac { 1 } { 2 } } \big ) \widetilde { I } ^ { - \frac { 1 } { 2 } } ,
$$

we have

$$
\begin{array} { r l } & { \| \widetilde { I } \| _ { \mathrm { o p } } \leq 2 f _ { e } ( 0 ) \| \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \| _ { \mathrm { o p } } ; } \\ & { \| \widetilde { I } ^ { - 1 } \| _ { \mathrm { o p } } \leq \displaystyle \frac { 2 } { f _ { e } ( 0 ) } \| \mathcal { H } _ { \theta ^ { * } } \| _ { \mathrm { o p } } . } \end{array}
$$

We can then obtain that the requirements for the preconditioning matrix $\widetilde { I }$ in Theorem 2 are satisfied with $\rho _ { 2 } = 2 f _ { e } ( 0 )$ and $\rho _ { 1 } = \frac { 1 } { 2 } f _ { e } ( 0 )$ .