# Statistical Inference for Bayesian Risk Minimization via Exponentially Tilted Empirical Likelihood

Rong Tang and Yun Yang

University of Illinois Urbana-Champaign

# Abstract

The celebrated Bernstein von-Mises theorem ensures that credible regions from Bayesian posterior are well-calibrated when the model is correctly-specified, in the frequentist sense that their coverage probabilities tend to the nominal values as data accrue. However, this conventional Bayesian framework is known to lack robustness when the model is misspecified or only partly specified, such as in quantile regression, risk minimization based supervised/unsupervised learning and robust estimation. To overcome this difficulty, we propose a new Bayesian inferential approach that substitutes the (misspecified or partly specified) likelihoods with proper exponentially tilted empirical likelihoods plus a regularization term. Our surrogate empirical likelihood is carefully constructed by using the first order optimality condition of the empirical risk minimization as the moment condition. We show that the Bayesian posterior obtained by combining this surrogate empirical likelihood and the prior is asymptotically close to a normal distribution centering at the empirical risk minimizer with covariance matrix taking an appropriate sandwiched form. Consequently, the resulting Bayesian credible regions are automatically calibrated to deliver valid uncertainty quantification. Computationally, the proposed method can be easily implemented by Markov Chain Monte Carlo sampling algorithms. Our numerical results show that the proposed method tends to be more accurate than existing state-of-the-art competitors.

Keywords— Bayesian inference; Risk minimization; Exponentially tilted empirical likelihood; Gibbs posterior; Misspecified model; Robust estimation

# 1 Introduction

We consider Bayesian approaches for estimation and probabilistic inference on model parameter that is defined by a loss function. Specifically, given a loss function $\ell : \mathcal { X } \times \Theta $ $\mathbb { R }$ of random variable $X \in { \mathcal { X } }$ and parameter $\theta \in \Theta \subset \mathbb { R } ^ { d }$ , we aim to estimate the global minimizer $\theta ^ { * }$ of the population risk function $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ where the expectation is taken with respect to the underlying data generating distribution ${ \mathcal { P } } ^ { * }$ that generates $X$ . Many statistical problems can be formulated as a risk minimization problem. For example, for any $\tau \in ( 0 , 1 )$ , the $\tau$ -th quantile of a random variable $X$ solves the population risk ${ \mathcal { R } } ( \theta )$ with the check loss function $\ell ( x , \theta ) = ( x - \theta ) { \bigl ( } \tau - 1 ( x < \theta ) { \bigr ) }$ where $\mathbf { 1 } ( \cdot )$ stands for the indicator function. More generally, quantile regression [Yu and Moyeed, 2001, Sriram et al., 2013], a widely used data analysis technique in statistics and econometrics, can be fitted via minimizing the empirical check loss on the residuals, where the true parameter (regression coefficients) minimizes the corresponding popular level risk (see Section 5.1.3 for a concrete example). In many high-dimensional problems, the model parameters can also be interpreted as the minimizer of the expectation of a loss function under some low-dimensional structural constraint. For example, sparse high-dimensional regression aims to estimate a regression coefficient vector $\theta ^ { * }$ that is at most $s$ -sparse (an $s$ -sparse vector is a vector with $s$ non-zero components). In this example, $\theta ^ { * }$ can also be defined as the minimizer of the expected squared loss on the residual vector subject to the constraint that it is at most $s$ -sparse (see for example, Yang et al. [2016] and Martin et al. [2017]).

In statistical applications, distribution ${ \mathcal { P } } ^ { * }$ is not directly observable, but instead a set of i.i.d samples $\{ X _ { 1 } , \cdots , X _ { n } \}$ from ${ \mathcal { P } } ^ { * }$ is available. Based on the formulation of the population risk minimization problem, a natural strategy to estimate $\theta ^ { * }$ is the empirical risk minimization (ERM) approach [Vapnik, 1991], which uses any minimizer $\begin{array} { r } { \hat { \theta } \in \arg \operatorname* { m i n } _ { \theta \in \Theta } \mathcal { R } _ { n } ( \theta ) } \end{array}$ of the empirical risk function $\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) } \end{array}$ as the estimator. Beyond point estimation, Bayesian approaches allow natural uncertainty quantification, or more broadly probabilistic inference, on the unknown parameter via the posterior distribution. However, the major challenge for the Bayesian or other likelihoodbased inference is the requirement of assuming a distribution family that contains the underlying data generating distribution, even though the latter is not our primary objective of study. For example, in Bayesian quantile regression [Yu and Moyeed, 2001, Sriram et al., 2013], although estimating and predicting certain quantile of the response in the presence of covariate variables is of the primary interest, a Bayesian procedure still needs to fully specify the error distribution, such as the asymmetric Laplace distribution, to mimic the check loss minimization [Koenker and Bassett Jr, 1978, Koenker, 2005] method in the frequentist paradigm. When the error distribution is misspecified, consistency of point estimation remains valid [Sriram et al., 2013]. However, credible intervals derived from the Bayesian posterior no longer honestly reflect the estimation uncertainty (c.f. our numerical results in Sections 5.1.3 and 5.3.1). More generally, Kleijn and van der Vaart [2012] establishes a Bernstein-von Mises theorem for Bayesian posterior under model misspecification, showing that Bayesian credible sets may not be valid confidence sets. Examples where models are not necessary to be fully specified, or only partly specified, are ubiquitous in various problems, including quantile regression, risk minimization based supervised and unsupervised learning [Vapnik, 1991, Cauwenberghs, 1993, Sun et al., 2019, Barlow, 1989, Buhmann, 1998], and robust estimation [Huber, 1992, Wilcox, 2011, Rousseeuw and Yohai, 1984, Rousseeuw and Leroy, 2005]. Therefore, alternatives to the conventional likelihood based Bayesian approaches that do not require full model specification and are robust to model-misspecification are imperative.

A popular model-free surrogate to the conventional Bayesian posterior is the Gibbs posterior [McAllester, 1999, Bhattacharya and Martin, 2020], whose density function is defined as $\pi _ { \boldsymbol { G } } ( \boldsymbol { \theta } | X _ { 1 : n } ) \propto \exp \{ - n \beta \mathcal { R } _ { n } ( \boldsymbol { \theta } ) \} \pi ( \boldsymbol { \theta } )$ , where $\pi$ denotes the prior density, $X _ { 1 : n } = \{ X _ { i } \} _ { i = 1 } ^ { n }$ is the sample of size $n$ and $\beta > 0$ is a learning rate (sometimes called inverse temperature) parameter for balancing between the empirical risk $\mathcal { R } _ { n }$ and prior $\pi$ . The Gibbs posterior uses the empirical risk to exponentially penalize a “loss” of parameter $\theta$ incurred on the data, thus avoiding full specification of a statistical model. Theoretically, it is shown in Bhattacharya and Martin [2020], Guedj [2019], Syring and Martin [2020] that such a Gibbs posterior has good generalization ability — it concentrates on parameter values with small population risk $\mathcal { R }$ . On the other side, uncertainty quantification remains problematic since the Gibbs posterior is generally incapable of honestly capturing the estimation variability [Kleijn and van der Vaart, 2012, Grünwald and van Ommen, 2017]. In the one-dimensional case where $\theta \in \mathbb { R }$ , the Gibbs posterior can be calibrated via empirically tuning the learning rate $\beta$ (e.g. via bootstrapping as in Syring and Martin [2018], Grünwald and van Ommen [2017]) so that the frequentist coverage probability of its highest posterior region asymptotically agrees with its credible level. In practice, the performance of these calibration methods is highly sensitive to the choice of $\beta$ [Bhattacharya and Martin, 2020]. Furthermore, in the multivariate case where $d > 1$ , a single tuning parameter $\beta$ inflates all entries of the limiting covariance matrix of the Gibbs posterior by the same multiplicative factor. As a consequence, the dependence in the Gibbs posterior among different coordinates in $\theta$ cannot be adjusted. Formally, Bhattacharya and Martin [2020] shows that for general dimensions, the Gibbs posterior can only be calibrated via tuning the learning rate if a generalized information equality [Chernozhukov and Hong, 2003] holds. This generalized information equality almost requires the empirical risk function $\mathcal { R } _ { n }$ to be proportional to the negative log-likelihood function in a local neighborhood of true parameter value $\theta ^ { * }$ .

Another popular approach of statistical inference without full model specification is via the empirical likelihood (EL) [Owen, 1990, Schennach, 2005, Chang and Mukerjee, 2008, Lazar, 2003]. In a nutshell, EL is an attractive nonparametric analogue of the conventional likelihood that only requires partial model specification through moment conditions [Chib et al., 2018]. Specifically, a moment condition takes the form of $\mathbb { E } [ g ( X , \theta ) ] = 0$ [Broniatowski and Keziou, 2012] where $g$ is a known vector-valued function of $X$ and $\theta$ , called the moment function. Statistical models satisfying moment conditions are called moment condition models. In the Bayesian paradigm, the conventional likelihood function can also be replaced by the EL, leading to the Bayesian EL posterior, whose frequentist properties from posterior inference have been shown to be valid in Lazar [2003], Rao and Wu [2010], Zhao et al. [2020] for parameters defined through unbiased estimating functions. As a popular variant of $\mathrm { E L }$ , the exponentially tilted empirical likelihood (ETEL), has been shown in Schennach [2005] that is closely related to $\mathrm { E L }$ but also admits a well-defined probabilistic interpretation arising from a Bayesian nonparametric perspective. Moreover, a Bayesian posterior defined as being proportional to the product of the ETEL and the prior is guaranteed to admit the “correct” covariance structure, under the assumption that the moment function $g$ defining the ETEL is sufficiently smooth [Chib et al., 2018]. Here, the correctness means that the asymptotic posterior covariance matches that of the frequentist sampling distribution of the posterior mean, or the maximum empirical likelihood estimator.

While statistical inference based on Bayesian ETEL for moment condition models enjoys appealing asymptotic properties, it is not clear how it can be applied to problems whose parameter of interest is defined as the minimizer of a population risk function $\mathcal { R }$ , such as quantile regression, risk minimization based statistical learning and robust estimation. One natural idea is to turn the $M$ -estimation problem [Geer and van de Geer, 2000] of empirical risk minimization into the $Z$ -estimation problem (or generalized methods of moments) of solving the moment condition equation $\nabla \mathcal { R } _ { n } ( \theta ) = 0$ arising from its first order optimality condition. Unfortunately, this idea has an obvious limitation: not every first order stationary point that solves this equation is a global minimizer of $\mathcal { R } _ { n }$ , unless restrictive assumptions such as strong convexity of $\mathcal { R } _ { n }$ are imposed. More rigorously, we show in this paper (c.f. Theorem 1) that if equation $\nabla \mathcal { R } _ { n } ( \theta ) = 0$ (or $\nabla R ( \theta ) = 0$ ) admits multiple solutions, then the naive Bayesian ETEL posterior constructed with this equation as the moment condition is close to a Gaussian mixture distribution, where each mixture component corresponds to one solution with a non-vanishing mixture weight. This leads to estimation inconsistency. Computationally, due to the multi-modality any local move based sampling algorithm for simulating from the Bayesian ETEL posterior may suffer from slow-mixing as the algorithm may get stuck in the local modes.

In this article, we propose a new ETEL-based Bayesian approach for risk minimization that enjoys good properties from both: it enjoys the estimation consistency as the Gibbs posterior and captures the estimation variability by exhibiting the “correct” asymptotic covariance as the Bayesian ETEL posterior. We call the resulting posterior distribution as Bayesian penalized exponentially tilted empirical likelihood (PETEL) posterior. Unlike Bayesian inference with Gibbs posteriors, our approach is calibration free and circumvents the need of any restrictive assumption such as the generalized information equality, and is thus more broadly applicable. Unlike the aforementioned naive application of Bayesian ETEL that results in a multi-modal posterior, our proposed posterior concentrates on a shrinking neighborhood of the target $\theta ^ { * }$ , and thus can be used to form consistent point estimators of the parameter. Our proposed methodology also provides an attractive Bayesian alternative to the bootstrapping for uncertainty quantification in empirical risk minimization with several advantages: 1. Bayesian PETEL allows for a direct incorporation of prior information which embraces complicated hierarchical structures and promotes shrinkage estimation; 2. conventional gradient based optimization algorithms for minimizing the empirical risk function tend to get stuck into first order stationary points, while the asymptotic uni-modality of the Bayesian PETEL posterior enhances the sampling efficiency of MCMC algorithms; 3. Bayesian PETEL exhibits superior performance in our numerical studies and tends to be more accurate in terms of coverage probabilities than bootstrapping especially when the risk function is non-convex (c.f. Section 5.1.2). Our proposed Bayesian PETEL method can also be generalized in several ways. First, it applies to non-smooth loss functions by using any sub-gradient of the empirical risk function to substitute the gradient in smooth cases. This improves the results in Chib et al. [2018] where the validity of their Bayesian ETEL method requires moment function $g$ to be at least twice differentiable, excluding many important examples such as quantile regression, soft-margin support vector machines (SVM) for classification and Huber loss based robust estimation. Specifically, we show in Section 4.3 that by replacing the gradient with any subgradient in the Bayesian PETEL posterior, the resulting Bayesian credible region remains well-calibrated [Molanes Lopez et al., 2009]. Second, Bayesian PETEL can be extended to high-dimensional models under sparsity constraints by incorporating sparsity inducing priors. For the high-dimensional extension, we show that under proper conditions: (1) those unimportant parameters shrink to zero in the posterior; (2) the joint posterior distribution of those important non-zero parameters is well-approximated by a normal distribution as if working with the low-dimensional (true) model.

The rest of the paper is organized as follows. In Section 2, we summarize the notation and give a background introduction to the Bayesian exponentially tilted empirical likelihood (ETEL) and Gibbs posterior. Our proposed Bayesian PETEL posterior is introduced in Section 3.1 and its extensions to non-smooth loss functions and high-dimensional problems are introduced in Section 3.2. The non-asymptotic properties on the Bayesian ETEL/PETEL posterior are provided in Section 4 for both smooth and non-smooth loss functions. Numerical comparisons of our proposed method with calibrated Gibbs posteriors [Syring and Martin, 2018] and bootstrapping are provided in Sections 5 and 6. In Appendix A, we discuss in detail computational aspects of our method, which can be easily implemented via MCMC algorithms. As two representative examples, we apply our theory to quantile regression and soft-margin SVM in Appendix B. Proofs of main results and technical results are deferred to the Appendix C and D respectively.

# 2 Background and Problem Formulation

In this section, we begin with the problem setup and summarize some necessary notations. After that, we review two candidate approaches, namely, Gibbs posterior and Bayesian ETEL posterior, for Bayesian inference in risk minimization, and discuss their limitations. As we will see, the Gibbs posterior approach is consistent for parameter estimation, but does not capture the dependence structure and leads to incorrect uncertainty quantification; in contrast, the Bayesian ETEL posterior captures the local covariance, but is susceptible to spurious local minima (a spurious local minimum is a local minimum that is not global) and leads to inconsistent estimation. Both of these will serve as the motivation to our proposed method to be described in the next section.

Recall from the beginning of the introduction section that in the risk minimization problem, we observe i.i.d. copies of a random variable $X$ from an unknown underlying distribution ${ \mathcal { P } } ^ { * }$ , and our goal is to estimate a parameter $\theta ^ { * }$ as the evaluation at ${ \mathcal { P } } ^ { * }$ of a functional $\theta : { \mathcal { P } } ( \mathcal { X } )  \Theta$ , where functional output $\theta ( \mathcal { P } )$ at an input distribution $\mathcal P \in \mathcal P ( \mathcal X )$ is implicitly defined through the following population risk minimization problem

$$
\theta ( \mathcal { P } ) \in \underset { \theta \in \Theta } { \arg \operatorname* { m i n } } \mathcal { R } ( \theta ; \mathcal { P } ) , \quad \mathrm { w i t h } \mathcal { R } ( \theta ; \mathcal { P } ) : = \mathbb { E } _ { \mathcal { P } } \big [ \ell ( X , \theta ) \big ] ,
$$

where $\mathbb { E } _ { \mathcal { P } }$ denotes the expectation with respect to $\mathcal { P }$ , and recall that $\ell : \mathcal { X } \times \Theta  \mathbb { R }$ is the loss function. When no ambiguity arises, we will omit the ${ \mathcal { P } } ^ { * }$ in the expectation $\mathbb { E } _ { \mathcal { P } }$ and the population risk function $\mathcal { R } ( \cdot , \mathcal { P } )$ when $\mathcal { P } = \mathcal { P } ^ { * }$ in the rest of the paper. We use $\mathcal { H } _ { \theta }$ to denote the Hessian of population risk function ${ \mathcal { R } } ( \theta )$ at $\theta$ , and $\Delta _ { \theta } =$ $\mathbb { E } \left( \nabla _ { \theta } \ell ( X , \theta ) \nabla _ { \theta } \ell ( X , \theta ) ^ { T } \right)$ the covariance matrix of the “score” vector $\nabla _ { \theta } \ell ( X , \theta )$ at $\theta$ .

# 2.1 Notation

We use $\| \cdot \| _ { p }$ to denote the vector $\ell _ { p }$ norm and $\mathbf { 1 } _ { A }$ the indicator function of a set $A$ so that $\mathbf { 1 } _ { A } ( x ) = 1$ if $x \in A$ and zero otherwise. For a vector $\theta \in \mathbb { R } ^ { d }$ , we use $S ( \theta )$ to denote the support of vector $\theta$ , the set of all indices from $1$ to $d$ corresponding to non-zero components of $\theta$ . For any set $S = \{ s _ { 1 } , \cdot \cdot \cdot , s _ { p } \} \subseteq \{ 1 , \cdot \cdot \cdot , d \}$ , let $| S |$ denote its cardinality, ${ \boldsymbol { \theta _ { S } } } = ( \theta _ { s _ { 1 } } , \cdot \cdot \cdot , \theta _ { s _ { p } } ) ^ { T } \in \mathbb { R } ^ { | S | }$ , and $\Theta _ { S } = \{ \theta _ { S } | \theta \in \Theta \}$ the $S$ -section of $\Theta$ . When no ambiguity arises, we may also use the density function, for example $\pi$ , to refer an absolutely continuous probability measure $\Pi$ . For a set $\Omega$ , we use $\Omega ^ { \circ }$ to denotes its interior and $\mathscr { P } ( \Omega )$ to denote the space of all probability distributions over $\Omega$ . Let $d _ { \mathrm { T V } } ( \mu , \nu )$ the total variation distance between two probability measures $\mu$ and $\nu$ . For two discrete probability measures $p = ( p _ { 1 } , \cdots , p _ { n } )$ and $p ^ { * } = ( p _ { 1 } ^ { * } , \cdots , p _ { n } ^ { * } )$ , the “forward” Kullback–Leibler (KL) divergence between $p$ and $p ^ { * }$ is defined as $\textstyle \sum _ { i = 1 } ^ { n } p _ { i } ^ { * } \log ( p _ { i } ^ { * } / p _ { i } )$ ; the “backward” Kullback–Leibler (KL) divergence between $p$ and $p ^ { * }$ is defined as $\scriptstyle \sum _ { i = 1 } ^ { n } p _ { i } \log ( p _ { i } / p _ { i } ^ { * } )$ [Kullback, 1997]. For any function $f : \mathcal { X } \times \Theta  \mathbb { R }$ , we use $\nabla _ { { \boldsymbol { \theta } } } f ( { \boldsymbol { x } } , { \boldsymbol { \theta } } )$ to denote the gradient of $f ( x , \theta )$ respect to $\theta$ for $x \in \mathcal { X }$ and $\theta \in \Theta$ . For a sample $X _ { 1 : n } = \{ X _ { 1 } , \ldots , X _ { n } \}$ of size $n$ and any measurable function on $\mathcal { X }$ , we use $\mathcal { P } _ { n }$ to denote its empirical distribution which assigns probability mass $n ^ { - 1 }$ to each observation. We use $[ d ]$ to denote the set $\{ 1 , 2 , \ldots , d \}$ for any $d \in \mathbb { N } _ { + }$ . For two sequences $\{ a _ { n } \}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ to mean $a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n$ . In addition, $a _ { n } \asymp b _ { n }$ means that both $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ hold. For two symmetric matrices $A$ and $B$ , we use $A \succcurlyeq B$ to mean that $A - B$ is a positive semi-definite matrix. Let $N ( \mu , \Sigma )$ denote the multivariate normal distribution with mean $\mu$ and covariance matrix $\Sigma$ .

# 2.2 Gibbs posterior for risk minimization

Originating in statistical mechanics and PAC (Probably Approximately Correct)-Bayes literature [Catoni, 2007, Guedj, 2019], the Gibbs posterior [Alquier, 2008, Bhattacharya and Martin, 2020] arises as the posterior that minimize a certain PAC-Bayesian bound [Guedj, 2019] and is a Bayesian version of empirical risk minimization constructed from a loss function $\ell ( x , \theta )$ ,

$$
\pi _ { \mathbb { G } } ( \theta \mid X _ { 1 : n } ) = \frac { \exp \big ( - n \beta \mathcal { R } _ { n } ( \theta ) \big ) \pi ( \theta ) } { \int _ { \Theta } \exp \big ( - n \beta \mathcal { R } _ { n } ( \theta ) \big ) \pi ( \theta ) d \theta } , \quad \mathrm { w i t h } \mathcal { R } _ { n } ( \theta ) = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } ; \theta ) ,
$$

where $\beta$ is the learning rate (inverse temperature) parameter controlling the spread of the distribution. Since the empirical risk function $\mathcal { R } _ { n }$ provides a good proxy to its population counterpart $\mathcal { R }$ , Bayesian inference via Gibbs posterior aims at minimizing the population risk function $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ without fully specifying a data generating model.

It is proved in several contexts [Bhattacharya and Martin, 2020, Guedj, 2019, Syring and Martin, 2020] that with certain choice of the learning rate $\beta$ and appropriate conditions on the loss function $\ell$ , the Gibbs posterior tends to contract toward the unique minimizer $\theta ^ { * } = \theta ( \mathcal { P } ^ { * } )$ of ${ \mathcal { R } } ( \theta )$ over $\Theta$ . This ensures the consistency of any reasonable estimator constructed from the Gibbs posterior. The rate of contraction depends on the complexity of parameter space $\Theta$ and is the parametric root- $n$ rate (modulo logarithmic factors) for regular parametric models where $\Theta$ is finite-dimensional. For sparse high-dimensional linear regression, Martin and Tang [2020], Martin et al. [2017] show that the Gibbs posterior with suitable $\beta$ achieves the minimax-optimal rate of contraction when a sparsity inducing prior favoring smaller models is employed.

Regarding uncertainty quantification using credible sets, it is observed in Bissiri et al.

[2016], Syring and Martin [2020, 2018] that the learning rate $\beta$ plays a critical role in calibrating the credible intervals from the Gibbs posterior to be asymptotically valid. Here the asymptotic validity means attaining their frequentist nominal (credible) levels in the limit as $n  \infty$ . Syring and Martin [2018] proposes to use a bootstrappingbased algorithm to calibrate the Bayesian credible region of Gibbs posterior by tuning $\beta$ . They apply stochastic approximation [Robbins and Monro, 1951] to update $\beta$ until the empirical coverage probability is close enough to the nominal level. In another related work, Bhattacharya and Martin [2020] shows that the Gibbs posterior is close to a normal distribution centering at the empirical risk minimizer $\hat { \theta }$ with covariance matrix $( n \beta ) ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ , where recall that $\mathcal { H } _ { \theta }$ denotes the Hessian of ${ \mathcal { R } } ( \theta )$ at $\theta$ . Note that this matrix is in general different from $n ^ { - 1 }$ times the asymptotic covariance $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ of $\hat { \theta }$ , unless $\Delta _ { \theta ^ { * } } = c \mathcal { H } _ { \theta ^ { * } }$ for some constant $c > 0$ . Here, recall $\Delta _ { \theta } = \mathbb { E } \big ( \nabla _ { \theta } \ell ( X , \theta ) \nabla _ { \theta } \ell ( X , \theta ) ^ { T } \big )$ . Consequently, unless $\theta$ is one-dimensional, it is impossible to calibrate the covariance structure based on tuning a single parameter $\beta$ . Furthermore, different $\beta$ ’s needed to be tuned in order to calibrate credible intervals corresponding to different components of $\theta$ , making the bootstrapping computationally demanding.

# 2.3 Bayesian exponentially tilted empirical likelihood

Conventional Bayesian inference requires the full specification of the likelihood function. However, for complex problems involving complicated dependence structures, it is inevitable to misspecify part of the data generating model, which may lead to inconsistent estimation due to the use of incorrect distributional assumptions. Empirical likelihood methods overcome this issue by producing inference about parameters using the information supplied by moment conditions. They circumvent the need for full knowledge of the likelihood function and are often more robust against model misspecification. Schennach [2005] shows that the exponentially tilted empirical likelihood (ETEL), a variant of the empirical likelihood, shares many desirable properties as the conventional parametric likelihood. In particular, ETEL naturally arises as the nonparametric limit of a Bayesian procedure for moment condition models with a type of non-informative prior on the space of distributions. For such models, a Bayesian ETEL posterior constructed by combining the ETEL with a prior can be applied to conduct valid statistical inference. In the following, we briefly review the Bayesian ETEL.

As is common in statistics, we only assume the statistical model $\mathcal { P }$ to satisfy the moment condition (general estimating) equation $\mathbb { E } [ g ( X , \theta ) ] = 0$ specified by a vector valued moment function $g : \mathcal { X } \times \Theta  \mathbb { R } ^ { d }$ , where parameter space $\Theta \subset \mathbb { R } ^ { d }$ . In this setup, parameter $\theta$ does not need to fully parametrize the model, and can be certain functional $\theta ( \mathcal { P } )$ of $\mathcal { P } \in \mathcal { P } ( \mathcal { X } )$ such as mean, quantiles and etc. For a sample $X _ { 1 : n } = \{ X _ { i } \} _ { i = 1 } ^ { n }$ of size $n$ , the ETEL function $L : \mathcal { X } _ { 1 : n } \times \Theta \to ( 0 , \infty )$ is defined as $\begin{array} { r } { L ( X _ { 1 : n } ; \theta ) = \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } \end{array}$ , where $( p _ { 1 } ( \theta ) , p _ { 2 } ( \theta ) , \ldots , p _ { n } ( \theta ) )$ solves the following constrained optimization problem

$$
\begin{array} { c } { { \displaystyle \operatorname* { m a x } _ { ( w _ { 1 } , w _ { 2 } , \ldots , w _ { n } ) } \sum _ { i = 1 } ^ { n } \left[ - w _ { i } \log ( n w _ { i } ) \right] } } \\ { { \mathrm { s u b j e c t ~ t o } \displaystyle \sum _ { i = 1 } ^ { n } w _ { i } = 1 , \displaystyle \sum _ { i = 1 } ^ { n } w _ { i } g ( X _ { i } , \theta ) = 0 , } } \\ { { w _ { 1 } , w _ { 2 } , . . . , w _ { n } \ge 0 . } } \end{array}
$$

By introducing Lagrange multipliers to the constraints, these probabilities $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ can be equivalently expressed as

$$
p _ { i } ( \theta ) = \frac { \exp \left( [ \lambda ( \theta ) ] ^ { T } g ( X _ { i } , \theta ) \right) } { \sum _ { i = 1 } ^ { n } \exp \left( [ \lambda ( \theta ) ] ^ { T } g ( X _ { i } , \theta ) \right) } \quad \mathrm { w i t h } \quad \lambda ( \theta ) = \underset { \xi \in \mathbb { R } ^ { d } } { \operatorname { a r g m i n } } \Big \{ \sum _ { i = 1 } ^ { n } \exp \left( \xi ^ { T } g ( X _ { i } , \theta ) \right) \Big \} .
$$

The unconstrained convex minimization problem (3) can be solved by a Newton–Raphson procedure. Here, $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ can be viewed as the probabilities minimizing the KL divergence between the multinomial distribution $( w _ { 1 } , \cdots , w _ { n } )$ , with $w _ { i }$ being assigned to the $i$ th observation $X _ { i }$ , and the empirical distribution $( n ^ { - 1 } , n ^ { - 1 } , \dots , n ^ { - 1 } )$ , subject to the constraint that a weighted sample version of the moment condition equation, $\textstyle \sum _ { i = 1 } ^ { n } w _ { i } g ( X _ { i } , \theta ) = 0$ , is satisfied. It is worth mentioning that Wu and Lu [2016] and Schennach [2007] provide a unifying perspective by interpreting the $\mathrm { E L }$ and the ETEL as minimizing respectively the “forward” and “backward” KL distance between $\left( p _ { 1 } ( \theta ) , p _ { 2 } ( \theta ) , \dots , p _ { n } ( \theta ) \right)$ and $( n ^ { - 1 } , n ^ { - 1 } , \dots , n ^ { - 1 } )$ under each $\theta \in \Theta$ . As a consequence, they show that under some regularity conditions, the probabilities $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ obtained from the $\mathrm { E L }$ and the ETEL are first-order equivalent. Moreover, the point estimators obtained by maximizing the two likelihood functions differ only by a term of order $O _ { p } ( n ^ { - 3 / 2 } )$ .

In the Bayesian framework, ETEL function $L ( X _ { 1 : n } ; \theta )$ plays the role of the conventional likelihood function, leading to the Bayesian ETEL posterior density function

$$
\pi _ { \mathrm { E } } ( \theta | X _ { 1 : n } ) = \frac { L ( X _ { 1 : n } ; \theta ) \pi ( \theta ) } { \int _ { \Theta } L ( X _ { 1 : n } ; \theta ) \pi ( \theta ) d \theta } , \quad \forall \theta \in \Theta ,
$$

where recall that $\pi$ denotes the prior density function. On the theoretical side, Schennach [2007] and Chib et al. [2018] show that even in the presence of model misspecification (i.e., the equation $\mathbb { E } [ g ( X , \theta ) ] = 0$ does not admit a solution on $\Theta$ ), the Bayesian ETEL posterior satisfies the Bernstein–von Mises (BvM) theorem [Schennach, 2007]. Moreover, when the moment condition model is correctly specified in the sense that $\mathbb { E } [ g ( X , \theta ) ] = 0$ admits a unique solution $\theta ^ { * }$ over $\Theta$ , the BETEL posterior distribution concentrates on an $n ^ { - 1 / 2 }$ -ball centered at $\theta ^ { * }$ and is well-approximated by a normal distribution whose data-dependent center is the ETEL maximizer and whose covariance matrix matches the frequentist asymptotic covariance of the center.

# 2.4 Bayesian ETEL for risk minimization

In this part, we discuss a direct application of the Bayesian ETEL framework to the risk minimization problem and its limitation. In the Section 3, we will introduce an improved method that overcomes the limitation.

In the risk minimization problem, if we further assume that loss function $\ell ( x , \theta )$ is differentiable with respect to $\theta$ at any point $x \in \mathcal { X }$ and ${ \mathcal { R } } ( \theta )$ has a unique stationary point, which is its global minimum, then $\theta ( \mathcal P )$ can be equivalently defined as the unique solution of the following first order optimality condition of minimizing $\mathcal { R } ( \cdot , \mathcal { P } )$ ,

$$
\mathbb { E } _ { \mathcal { P } } [ \nabla _ { \theta } \ell ( X , \theta ) ] = 0 .
$$

By supplying the above as the moment condition equation in the Bayesian ETEL with $\nabla _ { \theta } \ell ( X , \theta )$ being the moment function, we obtain the following Bayesian ETEL posterior,

$$
\begin{array} { r l } & { ~ \pi _ { \mathrm { E } } ( \theta \mid X _ { 1 : n } ) = \displaystyle \frac { \pi ( \theta ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } { \int _ { \Theta } \pi ( \theta ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) d \theta } , \quad \theta \in \Theta , } \\ { \mathrm { w i t h } \quad p _ { i } ( \theta ) = \displaystyle \frac { \exp \big ( [ \lambda ( \theta ) ] ^ { T } \nabla _ { \theta } \ell ( X _ { i } , \theta ) \big ) } { \sum _ { i = 1 } ^ { n } \exp \big ( [ \lambda ( \theta ) ] ^ { T } \nabla _ { \theta } \ell ( X _ { i } , \theta ) \big ) } , \quad i = 1 , 2 , \ldots , n } \\ { \mathrm { w h e r e } \quad \lambda ( \theta ) = \displaystyle \operatorname* { a r g m i n } _ { \xi \in \mathbb { R } ^ { d } } \Big \{ \sum _ { i = 1 } ^ { n } \exp \big ( \xi ^ { T } \nabla _ { \theta } \ell ( X _ { i } , \theta ) \big ) \Big \} . } \end{array}
$$

However, this direct application of the Bayesian ETEL suffers from several drawbacks. First, it requires the population level identifiability— the population risk function $_ { \mathcal { R } }$ has a unique stationary point, which can be difficult to verify and only holds under certain restricted assumptions such as $\mathcal { R }$ being strongly convex over $\Theta$ . Second, even though $\mathcal { R }$ admits a unique stationary point, it is not guaranteed that the empirical risk function $\begin{array} { r } { \mathcal { R } _ { n } ( \cdot ) = \mathbb { E } _ { \mathcal { P } _ { n } } [ \ell ( X ; \theta ) ] = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } ; \theta ) } \end{array}$ also admits a unique stationary point (see Figure 1 for an illustration). This may require further restrictive assumptions such as loss function $\ell ( x ; \theta )$ being strongly convex with respect to $\theta$ .

Our theoretical result (Theorem 1) in Section 4.1 shows that if the population moment condition equation $\mathbb { E } [ \nabla _ { \theta } \ell ( X ; \theta ) ] = 0$ admits $K$ isolated solutions $\{ \tilde { \theta } _ { k } \} _ { k = 1 } ^ { K }$ on $\Theta$ , then the with Bayesian ETEL posterior $K$ components whose means and covariance matrices are $\pi _ { \operatorname { E } } ( \theta \mid X _ { 1 : n } )$ tends to be close to a Gaussian mixture distribution $\{ \widehat { \theta } _ { k } \} _ { k = 1 } ^ { K }$ and $\{ n ^ { - 1 } V _ { k } \} _ { k = 1 } ^ { K }$ respectively, with $V _ { k } = \mathcal { H } _ { \tilde { \theta } _ { k } } ^ { - 1 } \Delta _ { \tilde { \theta } _ { k } } \mathcal { H } _ { \tilde { \theta } _ { k } } ^ { - 1 }$ taking a sandwiched form. Each mixture component corresponds to one solution ${ \ddot { \theta } } _ { k }$ , and one of them is centered at the empirical risk minimizer $\hat { \theta }$ . Moreover, the mixing weight of the $k$ th mixture component only depends on $( \pi ( \tilde { \theta } _ { k } ) , V _ { k } )$ for $k = 1 , \ldots , K$ , and does not diminish as sample size $n$ tends to $\infty$ . As a consequence, any reasonable estimator, such as the posterior mean, from the Bayesian BETEL posterior $\pi _ { \mathrm { E } } ( \theta \mid X _ { 1 : n } )$ is not consistent for $\theta ^ { * }$ , let alone statistical inference based on $\pi _ { \mathrm { E } } ( \theta \mid X _ { 1 : n } )$ . On the positive side, the local asymptotic covariance matrix $V _ { k }$ corresponds to $\tilde { \theta } _ { k }$ matches the asymptotic covariance matrix of the normal center $\widehat { \theta } _ { k }$ , meaning that it correctly captures the local random fluctuation. Consequently, if all components other than the one corresponding to the empirical risk minimizer $\hat { \theta }$ are killed, then the remaining component renders correct uncertainty quantification.

![](images/ba42a7808614c8134636f5a3abace33c3321f110275d509103a8d35fd5876607.jpg)  
Figure 1: This figure plots the population risk and its empirical counterpart with loss function $\begin{array} { r } { \ell ( x , \theta ) = - \exp \big \{ - \frac { ( x - \theta ) ^ { 2 } } { 2 \cdot ( 0 . 0 1 ) ^ { 2 } } \big \} } \end{array}$ − (x−θ)22·(0.01)2 	, where random variable X ∼ N (0, 1) and 500 i.i.d. samples of $X$ are used for computing the empirical risk. Although the population risk admits a unique stationary point, the empirical risk has multiple stationary points.

# 3 Bayesian Inference for Risk Minimization

In this section, we propose a new approach of Bayesian inference for solving the risk minimization problem. The proposed method combines merits of the Gibbs posterior and the Bayesian ETEL posterior, leading to consistent estimation and automatically calibrated uncertainty quantification. We also provide its extensions for handling non-smooth loss functions and high-dimensional parameters.

# 3.1 Bayesian penalized exponentially tilted empirical likelihood

From the discussions in Sections 2.2 and 2.4, we see that despite the covariance matrix mismatching, the Gibbs posterior has a good concentration property that it places almost all mass on a shrinking neighborhood of $\theta ^ { * }$ ; in contrast, the Bayesian ETEL posterior is susceptible to spurious local minima and is multi-modal. However, the restriction of the

![](images/7632595c249c458db1313329e3be320370048f01ad6d9f6c48ada84809cb5ebf.jpg)  
Figure 2: The figures illustrate the performance of Bayesian ETEL/PETEL when applied to the regression model $Y = f ( \theta ^ { * } \tilde { X } ) + e$ , where $\theta ^ { * } = 1$ , $f ( x ) = 0 . 1 x ^ { 3 } - 0 . 2 x ^ { 2 } - 0 . 2 x$ , $\tilde { X } \sim N ( 0 , 1 )$ and $e \sim N ( 0 , 1 )$ . Figure (a) plots the population risk and its empirical counterpart with loss function $\ell ( ( \tilde { x } , y ) , \theta ) = ( y - f ( \theta \tilde { x } ) ) ^ { 2 }$ based $n = 5 0 0$ i.i.d. samples $\{ X _ { i } = ( \tilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { 5 0 0 }$ . There are three stationary points for both population risk and empirical risk. Figure (b) plots the respective density functions of Bayesian ETEL and PETEL posteriors with Uniform $( - 2 , 2 )$ prior on $\theta$ . We can see that the Bayesian ETEL posterior has 3 equal weighted local modes corresponding to the 3 stationary points of the empirical risk; while for Bayesian PETEL, the probability mass assigned to the local minimum around $- 0 . 7$ and the local maximum around 0.1 quickly vanishes as $\alpha _ { n }$ increases.

BETEL posterior to a local neighborhood around $\theta ^ { * }$ carries the correct shape that honestly reflects the uncertainty — its local asymptotic covariance matrix $\mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ matches that of its center $\hat { \theta }$ (c.f. Theorem 1). This motivate us to propose the following calibrated Gibbs posterior as a Bayesian penalized exponentially tilted empirical likelihood (PETEL), by adding a penalty term $- \alpha _ { n } \mathcal { R } _ { n } ( \theta )$ to enforce the concentration of the Bayesian ETEL posterior,

$$
\pi _ { \mathrm { P E } } ( \theta \mid X _ { 1 : n } ) = \frac { \pi ( \theta ) \exp \big ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } { \int _ { \Theta } \pi ( \theta ) \exp \big ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) d \theta } , \quad \theta \in \Theta ,
$$

where $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ are defined in equation (4), and $\alpha _ { n } > 0$ is a regularization parameter. Here, we add a subscript $n$ in $\alpha _ { n }$ to indicate that it is allowed to be dependent of $n$ . We intentionally choose $\alpha _ { n }$ to be $o ( n )$ as oppose to $n \beta$ in the Gibbs posterior. As a consequence, the penalty term $\alpha _ { n } \mathcal { R } _ { n } ( \theta )$ has limited impact on the shape of the posterior, since the latter is dominated by the ETEL part $\scriptstyle \left\{ \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) \right\}$ which is of order $e ^ { - O _ { p } ( n | | \theta - \hat { \theta } | | ^ { 2 } ) }$ . More rigorously, our theoretical analysis in Section 4 shows that there is a wide range of $\alpha _ { n }$ as $\log n \lesssim \alpha _ { n } \lesssim \sqrt { n \log n }$ to ensure the concentration of the Bayesian PETEL posterior around $\theta ^ { * }$ . Our numerical results in Section 5.1 also illustrate the robustness of this procedure to the choice of tuning parameter $\alpha _ { n }$ . In contrast, the performance of the Gibbs posterior is quite sensitive to the choice of learning rate $\beta$ . In addition, our theory shows that the Bayesian PETEL posterior is close to a normal distribution with the correct sandwiched covariance matrix; and the coverage probability of the resulting posterior credible region tends to its nominal level in the frequentist sense with the parametric root- $n$ rate (modulo logarithmic factors).

![](images/3d472558facc229805ca115e68142896138dd7eb39a983c98c0edf152d649580.jpg)  
Figure 3: We plot contours of Bayesian PETEL and Calibrated Gibbs (CG) posteriors when applied to the South African heart disease dataset, described in Section 4.4.2 of Hastie et al. [2009]. The binary response variable $Y$ is the presence or absence of myocardial infarction (MI) at the time of the survey. Following Hastie et al. [2009], we focus here on predictors tobacco, ldl, famhist and age. Our parameter $\theta \in \mathbb { R } ^ { 4 }$ of interest is the minimizer of population risk from the smoothed hinge loss in the SVM classification [Hajewski et al.,√ 2018], i.e., $\begin{array} { r } { \frac 1 2 \lambda \| \theta \| _ { 2 } ^ { 2 } + \mathbb { E } \frac 1 2 ( \sqrt { U ^ { 2 } + \varepsilon ^ { 2 } } + U ) } \end{array}$ where $U = 1 - Y \theta ^ { I ^ { \prime } } X$ , $\lambda = 0 . 5$ and $\varepsilon = 0 . 8$ . The blue and red curves are the contours of the joint distribution of $( \theta _ { 1 } , \theta _ { 3 } )$ (associated with tobacco and famhist) from the Bayesian PETEL and CG posteriors, respectively. The black curve is the benchmark contour based on bootstrapping samples. As we can see, the CG posterior fails to capture the heterogeneous variance of different $\theta$ components. For example, it overestimates the variance of $\theta _ { 3 }$ .

The Bayesian ETEL posterior described in Section 2.4 is a special case of Bayesian PETEL with $\alpha _ { n } = 0$ . Here, adding a penalty term $\alpha _ { n } \mathcal { R } _ { n } ( \theta )$ with appropriate nonzero $\alpha _ { n }$ forces the Bayesian PETEL posterior to empty out mixture components associated with stationary points (local optima and saddle points) of $\mathcal { R } _ { n }$ that are not the global minimum $\hat { \theta }$ (see Figure 2 for an illustration). The inclusion of this extra penalty term also comes with computational benefits. For example, suppose we apply Markov Chain Monte Carlo (MCMC) algorithm with local moves to sample from the posteriors. For the Bayesian

ETEL, due to the multi-modality, the Markov chain based on local moves may easily get stuck in one mode for a long time. However, for the Bayesian PETEL, the extra penalty term $\alpha _ { n } \mathcal { R } _ { n } ( \theta )$ favors points closer to the global minimum $\hat { \theta }$ of $\mathcal { R } _ { n }$ , and will encourage the Markov chain to move quickly towards $\hat { \theta }$ in a reasonable amount of steps.

Although the Bayesian PETEL shares a similar component $\exp \big ( - \alpha _ { n } \mathcal { R } _ { n } ( \theta ) \big )$ as the Gibbs posterior, this component only plays the role of forcing the posterior concentration, and does not contribute to forming its shape. Therefore, the Bayesian PETEL avoids any restrictive assumption, such as the generalized information equality $\Delta _ { \theta ^ { * } } = c \mathcal { H } _ { \theta ^ { * } }$ that is required by the Gibbs posterior to exhibit the correct shape for uncertainty quantification, and is suitable for a wider range of problems (see Figure 3 for a comparison). Furthermore, even if the generalized information equality holds, the Gibbs posterior approach involves the daunting task of selecting the learning rate $\beta$ for calibrating the scale of the covariance. In particular, the performance of Gibbs posterior inference is highly sensitive to the choice of $\beta$ [Bhattacharya and Martin, 2020]. In comparison, our method provably works under a much wider range of $\alpha _ { n }$ values.

# 3.2 Extensions

In this subsection, we discuss two extensions of our Bayesian PETEL approach.

Extension to non-smooth loss functions: When the loss function $\ell ( X ; \theta )$ is not differentiable with respect to $\theta$ at certain pair $( X , \theta )$ , we can replace the gradient with any of its subgradient (a subgradient of a function $f : \mathbb { R } ^ { d }  \mathbb { R }$ at point $x \in \mathbb { R } ^ { d }$ is a vector $\boldsymbol { g } \in \mathbb { R } ^ { d }$ such that $f ( y ) \geq f ( x ) + \langle g , y - x \rangle + o ( \| y - x \| _ { 2 } )$ as $y  x$ ). If $\ell ( X ; \theta )$ is everywhere differentiable with respect to $\theta$ , then the gradient $\nabla _ { \theta } \ell ( X ; \theta )$ is the unique subgradient and the method reduces to the Bayesian PETEL with a smooth loss function. Our theory in Section 4 will cover this case.

Extension to high-dimensional problems: In this extension, our interest is in the high-dimensional setting where dimension $d$ of parameter $\theta$ can be similar or much larger than the sample size $n$ . We follow the convention by considering the case where the population risk minimizer $\theta ^ { * }$ is $s ^ { * }$ -sparse with $s ^ { * } \ll n$ , i.e., the number of non-zero elements in $\theta ^ { * }$ is at most $s ^ { * }$ . Let $s _ { 0 }$ be a pre-specified upper bound on the sparsity level. For convenience, we consider the following class of sparse priors for achieving consistent estimation, and the method can be straightforwardly carried over to other sparsity inducing priors such as spike and slab priors [Ishwaran and Rao, 2005] and global-local shrinkage priors [Carvalho et al., 2010].

Definition (Sparse Prior). Prior on $\theta \in \mathbb { R } ^ { d }$ is induced by: (1) Draw s from a distribution $Q$ on the set $[ s _ { 0 } ]$ with probability mass function $q ( s ) \propto \exp ( - \beta _ { n , d } s )$ , for some constant $\beta _ { n , d } > 0$ ; (2) Pick uniformly a subset $S$ of cardinality $s$ of $[ d ]$ ; (3) Sample $\theta _ { S } = \{ \theta _ { j } : j \in S \}$

Such sparse priors are employed in many existing works [Martin and Tang, 2020, Martin et al., 2017, Castillo et al., 2015, Dellaportas et al., 2002] in the Bayesian literature. A correct specification of prior mass $q ( s )$ is crucial for controlling the sparsity level of $\theta$ , which should decay exponentially fast in $s$ [Castillo et al., 2015]. In the regression setting, the prior $\pi _ { S }$ , for example, can be chosen as Zellner’s $g$ -prior [Zellner, 1986].

Let $\{ p _ { i } ( \theta _ { S } ; S ) \} _ { i = 1 } ^ { n }$ denote the low-dimensional counterpart of the empirical probability functions $\{ p _ { i } ( \theta ) \} _ { i = 1 } ^ { n }$ defined in equation (5) when $\theta$ is restricted to $\Theta _ { S } \times \{ 0 \} ^ { d - | S | }$ , or

$$
\{ p _ { i } ( \theta _ { S } ; S ) \} _ { i = 1 } ^ { n } = \underset { { \Sigma _ { u = 1 } ^ { n } } } { \arg \operatorname* { m a x } } ~ \Big \{ \sum _ { i = 1 } ^ { n } [ - w _ { i } \log ( n w _ { i } ) ] \Big \} , \quad \mathrm { f o r } ~ \theta = ( \theta _ { S } , 0 ) \in { \mathbb R } ^ { d } .
$$

Now we define the “model-averaged” Bayesian PETEL posterior for high-dimensional parameter $\theta$ , or equivalently for $( \theta _ { S } , S )$ with $| \boldsymbol { S } | \le s _ { 0 }$ and $\theta _ { S } \in \Theta _ { S }$ , as

$$
\begin{array} { r l } & { \pi _ { \mathrm { P E } } ( \theta _ { S } , S \vert X _ { 1 : n } ) = } \\ & { \enspace \enspace \frac { \binom { d } { | S | } ^ { - 1 } q ( | S | ) \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } \mathcal { R } _ { n } ( \theta _ { S } , 0 ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; S ) } { S \in [ d ] , | S | \le s _ { 0 } ^ { \left( \alpha \right) } } q ( | S | ) \int _ { \Theta _ { S } } \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } \mathcal { R } _ { n } ( \theta _ { S } , 0 ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; S ) d \theta _ { S } } .  \end{array}
$$

Note that $\theta$ has a one-to-one correspondence with the pair $( \theta _ { S } , S )$ as: 1. Given $\theta \in \mathbb { R } ^ { d }$ we have $S = S ( \theta )$ and $\theta _ { S } = \theta _ { S ( \theta ) }$ ; 2. Given $( \theta _ { S } , S )$ , we have $\theta = ( \theta _ { S } , 0 ) \in \mathbb { R } ^ { d }$ .

Our theoretical result (Theorem 4) shows that as long as $\log d = o ( n )$ , there exist ranges of $\alpha _ { n , d }$ and $\beta _ { n , d }$ to guarantee the concentration of the posterior to the population risk minimizer $\theta ^ { * }$ . In addition, if all nonzero signals in $\theta ^ { * }$ are suitably large and $\log = o ( { \sqrt { n } } )$ , then the choice of $\log ( d \lor n ) \lesssim \alpha _ { n , d } \lesssim \sqrt { n \log n }$ and $\log ( d \lor n ) \lesssim \beta _ { n , d } \lesssim \alpha _ { n , d }$ leads to the so-called oracle property: 1. variable selection consistency, or $\pi _ { \mathrm { P E } } ( S = S ^ { * } \mid X _ { 1 : n } ) \approx 1$ , where $S ^ { * } = S ( \theta ^ { * } )$ denote the support of $\theta ^ { * }$ ; 2. the condition posterior $\pi _ { \mathrm { P E } } ( \theta _ { S ^ { * } } \mid S ^ { * } , X _ { 1 : n } )$ tends to be close to the normal distribution centering at the constrained minimizer $\hat { \theta } _ { S ^ { * } }$ of empirical risk $\mathcal { R } _ { n }$ over $\Theta _ { S ^ { * } }$ with the correct covariance matrix for uncertainty quantification. Consequently, we recommend a default choice of $\alpha _ { n , d } = C \sqrt { n }$ and $\beta _ { n , d } = C ^ { \prime } \log ( d \vee n )$ for some suitable constant $C$ and $C ^ { \prime }$ .

# 3.3 Computation

Since equation (5) provides an explicit expression for the Bayesian PETEL posterior up to a normalization constant, we utilize the Metroplis-Hasting algorithm to draw samples. The major non-trivial part in the algorithm is solving for $\lambda ( \theta )$ in the calculation of the ETEL function [c.f. equation (4)], which is a convex problem and can be calculated by a modified Newton-Raphson algorithm [Chen et al., 2002]. Algorithm 2 summarizes the pseudocode for the Metroplis-Hasting steps to sample from Bayesian PETEL posterior, where $\nabla _ { \theta } \ell ( X , \theta )$ can be replaced by its subgradient if not differentiable. Further details on the computation are provided in Appendix A.

<table><tr><td>osterior Input: Number of iteration L, tolerance ε, proposal distribution Pprop(*l·), initial state 0o and X(00); Data:X1, X2 ... , Xn;</td></tr><tr><td>for t←OtoL-1do Sample θ from Pprop(*10t);</td></tr><tr><td>Generate a uniform random number u ∈ (0,1); Define f(λ) ←1∑²=1exp(TVθl(xi,0θ));</td></tr><tr><td>入°←入(0t）;</td></tr><tr><td>k←0；</td></tr><tr><td>repeat k←k+1;</td></tr><tr><td>γ=1; H←∑exp（(x,）-1）(x,)(x,);</td></tr><tr><td>G←∑- exp((xi,0）Tx-1)）l(x,）;； repeat</td></tr><tr><td>xκ←λk-1-γH-1G; γ=γ；</td></tr><tr><td>until f(x²) ≤f(Xk-1); until ||H-1Gll2 ≤ε;</td></tr><tr><td>入(）←²; π)exp( (∑n=1og exp(λ(θ)Tge(Xi,0) -anRn()) 1exp(（）Tl(x0）) pprop(0t1θ) if u≤ then exp(x(0t)Tθl(Xi,0t))</td></tr><tr><td>π(0t)exp( (∑=1 log -anRn(t))pprop(@θt) ∑=1exp(x（0t）Te(xi,0t） θt+1←θ； 入(θt+1) ←入(0); else θt+1←0t;</td></tr></table>

# 4 Theoretical Results and their Consequences

In this section, we begin with theoretical analysis of the Bayesian ETEL posterior and discuss the consequent limitation. After that, we analyze the proposed Bayesian PETEL posterior with smooth loss, non-smooth loss, and sparse high-dimensional parameters. In

Appendix B, we apply these theoretical results to two representative examples, quantile regression and classification using soft-margin SVM.

# 4.1 Analysis of Bayesian ETEL posterior

In this subsection, we study the large sample behavior of the Bayesian ETEL posterior distribution. We first state the following regularity conditions to the loss function, risk function and prior distribution.

Assumption A.1: The loss function $\ell ( X , \theta ) : \mathcal { X } \times \Theta  \mathbb { R }$ is thrice differentiable with respect to $\theta$ with bounded mixed partial derivatives up to order three. In addition, the parameter space $\Theta \subset \mathbb { R } ^ { d }$ is compact.

Assumption A.2: (1) The equation $\nabla _ { \theta } \mathcal { R } ( \theta ) = 0$ has $K \geq 1$ isolated solutions $ { \tilde { \theta } } _ { 1 } , \cdots  { \tilde { \theta } } _ { K }$ on $\Theta$ , where for any $1 \leq k \leq K$ , $ { \tilde { \theta } } _ { k } \in \Theta ^ { \circ }$ ; (2) There exist positive constants $( a , b )$ such that for any $k \in [ K ]$ , it holds that $\Delta _ { \tilde { \theta } _ { k } } \succcurlyeq a I _ { d }$ and $\mathcal { H } _ { \widetilde { \theta } _ { k } } ^ { T } \mathcal { H } _ { \widetilde { \theta } _ { k } } \succcurlyeq b I _ { d }$ , where recall that $\mathcal { H } _ { \theta }$ denotes the Hessian matrix of ${ \mathcal { R } } ( \theta )$ and $\Delta _ { \theta } = \mathbb { E } \left( \nabla _ { \theta } \ell ( X , \theta ) \nabla _ { \theta } \ell ( X , \theta ) ^ { T } \right)$ .

Assumption A.3: (1) The prior admits a density function $\pi ( \theta )$ with respect to the Lebesgue measure; (2) There exist positive constants $( c , r , L )$ such that for any $k \in [ K ]$ , it holds that $\pi (  { \tilde { \theta } } _ { k } ) \geq c$ and $\pi ( \theta )$ is locally $L$ -Lipschitz around $\tilde { \theta } _ { k }$ , or $| \pi ( \theta ) - \pi ( \tilde { \theta } _ { k } ) | \leq L \lVert \theta - \tilde { \theta } _ { k } \rVert _ { 2 }$ for all $\theta$ satisfying $\lVert { \boldsymbol { \theta } } - { \tilde { { \boldsymbol { \theta } } } } _ { k } \rVert \leq r$ .

The assumptions on the smoothness of the loss function with respect to $\theta$ and the Lipschitz continuity of the prior are common for proving the asymptotic normality of the posterior in parametric models [Ghosh and Ramamoorthi, 2003]. Assumption A.2 on the risk function requires the positive definiteness of the sandwich covariance matrix $\mathcal { H } _ { \theta } ^ { - 1 } \Delta _ { \theta } \mathcal { H } _ { \theta } ^ { - 1 }$ [Syring and Martin, 2018] evaluated at $\{ \tilde { \theta } _ { k } \} _ { k = 1 } ^ { K }$ , so that posterior distributions constrained on neighborhoods of $\tilde { \theta } _ { k } \left( 1 \leq k \leq K \right)$ are asymptotically normal. The lower bounds on absolute values of eigenvalues of the Hessian matrix $\mathcal { H } _ { \widetilde { \theta } _ { k } }$ (not necessarily positive semi-definite) requires all saddle points and local optima to be strict, which is a common assumption for analyzing the algorithmic convergence of first-order optimization methods and is satisfied in most applications.

Our first theorem shows that, under these assumptions, the Bayesian ETEL posterior distribution tends to be close to a normal mixture distribution. The center of each mixture component falls into an $n ^ { - 1 / 2 }$ -neighborhood centered at one solution of $\nabla _ { \theta } \mathcal { R } ( \theta ) = 0$ , either a saddle point or a local optimum. For any $r > 0$ , we use $B _ { r } ( \theta )$ to denote the $\ell _ { 2 }$ -ball with radius $r$ centering at $\theta$ . Recall that $V _ { \theta }$ denotes the matrix $\mathcal { H } _ { \theta } ^ { - 1 } \Delta _ { \theta } \mathcal { H } _ { \theta } ^ { - 1 }$ for any $\theta \in \Theta$ .

Theorem 1. Under Assumption A.1, A.2 and A.3, there exists some positive constants $( r , C )$ independent of n such that it holds with probability at least $1 - n ^ { - 1 }$ that,

1. For any $1 \leq k \leq K$ , the equation $\nabla _ { \boldsymbol { \theta } } \mathcal { R } _ { n } ( \boldsymbol { \theta } ) = 0$ associated with empirical risk $\mathcal { R } _ { n }$ has a unique solution $\widehat { \theta } _ { k }$ in $B _ { r } ( { \tilde { \theta } } _ { k } )$ , where $\sqrt { n } (  { \hat { \theta } } _ { k } -  { \tilde { \theta } } _ { k } )  N ( 0 , V _ {  { \tilde { \theta } } _ { k } } )$ in distribution

as $n \to \infty$ ;

2. $\begin{array} { r l } & { d _ { \mathrm { T V } } \Big ( \pi _ { \mathrm { E } } \big ( \cdot \vert X _ { 1 : n } \big ) , \ \sum _ { k = 1 } ^ { K } \frac { \pi ( \theta _ { k } ) \vert V _ { \tilde { \theta } _ { k } } \vert ^ { 1 / 2 } } { \sum _ { l = 1 } ^ { K } \pi ( \tilde { \theta } _ { l } ) \vert V _ { \tilde { \theta } _ { l } } \vert ^ { 1 / 2 } } N \big ( \hat { \theta } _ { k } , n ^ { - 1 } V _ { \tilde { \theta } _ { k } } \big ) \Big ) \leq C \sqrt { \frac { \log n } { n } } } \end{array}$ , where $\pi _ { \mathrm { E } } ( \cdot | X _ { 1 : n } )$ is the Bayesian ETEL posterior defined in (4).

According to Theorem 1, each stationary point (saddle point, local minimum or local maximum) of population risk $\mathcal { R }$ contributes to one component in the normal mixture approximation to the posterior with non-vanishing mixing weight. Moreover, one of these mixture components corresponds to the global minimizer $\theta ^ { * }$ of $\mathcal { R }$ , which is our estimation target. As a consequence, the Bayesian ETEL posterior does not concentrate around $\theta ^ { * }$ unless $\mathcal { R }$ has a unique stationary point, for example, when $_ { \mathcal { R } }$ is strictly convex over $\Theta$ . A nice property in the theorem is that for each $k \in \lfloor K \rfloor$ , the (rescaled) local covariance matrix $V _ { \tilde { \theta } _ { k } }$ matches the asymptotic covariance matrix of the local center $\widehat { \theta } _ { k }$ . Therefore, the local shape of the posterior honestly captures the random fluctuation around local center $\hat { \theta } _ { k }$ .

# 4.2 Analysis of Bayesian PETEL posterior with smooth loss

In this subsection, we establish a Bernstein–von Mises type theorem (asymptotic normality of the posterior) for the Bayesian PETEL posterior when the loss function $\ell ( x , \theta )$ is smooth with respect to $\theta$ . We need Assumptions A.1, A.3 and the following.

Assumption A.2’: (1) The risk function ${ \mathcal { R } } ( \theta )$ has a unique global minimizer $\theta ^ { * }$ on $\Theta$ and $\theta ^ { * } \in \Theta ^ { \circ }$ . (2) There exists a positive constant $a$ such that $\Delta _ { \theta ^ { * } } \succcurlyeq a I _ { d }$ and $\mathcal { H } _ { \theta ^ { * } } \succcurlyeq a I _ { d }$ .

Assumption A.2’ is a counterpart of Assumption A.2 in the previous subsection. However, here we only need matrices $\Delta _ { \theta ^ { * } }$ and $\mathcal { H } _ { \theta ^ { \ast } }$ at a single point $\theta ^ { * }$ to be positive definite, which is much weaker.

Theorem 2. Under Assumption A.1, A.2’ and A.3, there exist some constants $( C , C _ { 1 } , C _ { 2 } )$ independent of $n$ , such that if $C _ { 1 } \log n \leq \alpha _ { n } \leq C _ { 2 } { \sqrt { n \log n } }$ , then it holds with probability at least $1 - n ^ { - 1 }$ that,

$$
d _ { \mathrm { T V } } \left( \pi _ { \mathrm { P E } } ( \cdot \mid X _ { 1 : n } ) , \ : N \left( \hat { \theta } , n ^ { - 1 } V _ { \theta ^ { * } } \right) \right) \leq C \sqrt { \frac { \log n } { n } } ,
$$

where recall that $\pi _ { \mathrm { P E } } ( \cdot | X _ { 1 : n } )$ is the Bayesian PETEL posterior distribution defined in equation (5) and $\hat { \theta }$ is the empirical risk minimizer on $\Theta$ . In addition, we have ${ \sqrt { n } } \left( { \hat { \theta } } - \theta ^ { * } \right) \to$ $N ( 0 , V _ { \theta ^ { * } } )$ in distribution as $n \to \infty$ .

Theorem 2 shows that the Bayesian PETEL posterior distribution of ${ \sqrt { n } } ( \theta - { \hat { \theta } } )$ is close to the multivariate normal distribution with center 0 and covariance matrix $V _ { \theta ^ { * } }$ in the total variation metric with rate $O ( { \sqrt { \frac { \log n } { n } } } )$ . The lower bound requirement of $\alpha _ { n } \geq C _ { 1 } \log n$ ensures that the extra penalty from $\mathcal { R } _ { n }$ is stronger enough to force the concentration of the posterior towards to global minimum $\theta ^ { * }$ by emptying out other mixture components indicated in Theorem 1. In contrast, the upper bound requirement of $\alpha _ { n } \leq C _ { 2 } \sqrt { n \log n }$ guarantees that this extra penalty term will not dominate the ETEL so that it preserves the local shape of the Bayesian ETEL posterior around $\theta ^ { * }$ .

Since the covariance matrix $V _ { \theta ^ { * } }$ in the normal approximation of $\pi _ { \mathrm { { P E } } } ( \cdot | X _ { 1 : n } )$ matches the asymptotic covariance matrix of $\hat { \theta }$ , inferential conclusions derived from the Bayesian PETEL distributions are valid in a frequentist sense. The following corollary formalize this statement through characterizing frequentist coverage probabilities of credible regions. Given a credible level $\alpha \in ( 0 , 1 )$ , let $q _ { \alpha }$ be the $\alpha$ -th upper quantile of a $\chi ^ { 2 }$ distribution with $d$ degrees of freedom. Let ${ \hat { \theta } } _ { B }$ and $\hat { \Sigma } _ { B }$ be the mean and covariance matrix of $\theta$ under the Bayesian PETEL posterior distribution. According to Theorem 2, the highest density region of Bayesian PETEL posterior is close to the credible ellipse ${ \mathcal { E } } _ { n } =$ $\left\{ ( \theta - { \hat { \theta } } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta - { \hat { \theta } } _ { B } ) \leq q _ { \alpha } \right\}$ , and the next corollary shows that its frequentist coverage is at most $O ( ( \log n ) ^ { 3 / 2 } / \sqrt { n } )$ away from $( 1 - \alpha )$ .

Corollary 1. Let ${ \hat { \theta } } _ { B }$ and $\hat { \Sigma } _ { B }$ be the posterior mean and covariance matrix of the Bayesian PETEL posterior distribution (5). Under the assumptions of Theorem 2, there exists $a$ constant $C _ { 3 }$ such that

$$
\left| \mathcal { P } ^ { * } \big ( \theta ^ { * } \in \mathcal { E } _ { n } \big ) - ( 1 - \alpha ) \right| \leq C _ { 3 } \frac { ( \log n ) ^ { 3 / 2 } } { \sqrt { n } } .
$$

The Bayesian credible region ${ \mathcal { E } } _ { n }$ in Corollary 1 provides a simultaneous inference on the entire parameter vector $\theta$ . Similar error bound also applies to the individual credible interval for each coordinate $\theta _ { j }$ in $\theta$ for $j \in [ d ]$ , which is approximately $\begin{array} { r l } {  { \big [ \hat { \theta } _ { B , j } - z _ { \alpha / 2 } \sqrt { \big [ \hat { \Sigma } _ { B } \big ] _ { j j } } , \hat { \theta } _ { B , j } + } \quad } & { { } } \end{array}$ $z _ { \alpha / 2 } \sqrt { [ \hat { \Sigma } _ { B } ] _ { j j } } ]$ , with $z _ { \alpha / 2 }$ denoting the $\alpha / 2$ -upper quantile of the standard normal distribution.

# 4.3 Analysis of Bayesian PETEL posterior with non-smooth loss

In practice, non-smooth loss functions are common, for example, in quantile regression and classification via soft-margin SVM [Duda et al., 2012]. In this subsection, we address the non-smooth case. In this case, it is common that due to the smoothing effect of taking expectation with respect to $X$ , the population loss function $\mathcal { R } ( \theta ) = \mathbb { E } [ \ell ( X , \theta ) ]$ remains smooth, which is true in all our considered examples. Under such cases, we assume that the moment function $g : \mathcal { X } \times \Theta  \mathbb { R } ^ { d }$ employed in the ETEL (2) for forming our Bayesian PETEL (5) is any function such that $\mathbb { E } [ g ( X , { \boldsymbol { \theta } } ) ] = \nabla \mathcal { R } ( { \boldsymbol { \theta } } )$ , for all $\theta \in \Theta$ . For example, this condition can be achieved by choosing $g$ as any subgradient of $\ell ( X , \theta )$ with respect to $\theta$ given that subgradients exist everywhere. Let $\Delta _ { \theta } = \mathbb { E } \big \lfloor g ( X , \theta ) g ( X , \theta ) ^ { T } \big \rfloor$ . We make following assumptions on $g$ and $\mathcal { R }$ . Let $\| \cdot \| _ { \mathrm { F } }$ denote the matrix Frobenius norm.

Assumption B.1: The parameter space $\Theta$ is compact. The risk function ${ \mathcal { R } } ( \theta )$ is bounded and has bounded derivatives up to order three with respect to $\theta$ on $\Theta$ . Both $g$ and $\ell$ are bounded over $\Theta$ and $\mathcal { X }$ . There exist positive constants $( r , c )$ such that $\Vert \Delta _ { \theta } - \Delta _ { \theta ^ { * } } \Vert _ { \mathrm { F } } \leq c \Vert \theta - \theta ^ { * } \Vert _ { 2 }$ for all $\theta \in B _ { r } ( \theta ^ { * } )$ .

Assumption B.2: Define pseudo-metrics $d _ { n } ^ { g }$ and $d _ { n } ^ { \ell }$ as $d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) = ( n ^ { - 1 } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) -$ $g ( X _ { i } , \theta ^ { \prime } ) \vert \vert _ { 2 } ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ and $\begin{array} { r l } { d _ { n } ^ { \ell } ( \theta , \theta ^ { \prime } ) = ( n ^ { - 1 } \sum _ { i = 1 } ^ { n } ( \ell ( X _ { i } , \theta ) - \ell ( X _ { i } , \theta ^ { \prime } ) ) ^ { 2 } ) ^ { \frac { 1 } { 2 } } } \end{array}$ respectively. There exists some positive constants $( c _ { 0 } , c _ { 1 } , \beta )$ such that

(a) The $\varepsilon$ -covering numbers of $\Theta$ with respect to $d _ { n } ^ { g }$ and $d _ { n } ^ { \ell }$ are upper bounded by $( n / \varepsilon ) ^ { c _ { 0 } }$ ;   
(b) For any $\theta \in \Theta$ , it holds that $\begin{array} { r } { \mathbb { E } \big [ \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| _ { 2 } ^ { 2 } \big ] + \mathbb { E } \big [ ( \ell ( X , \theta ) - \ell ( X , \theta ^ { * } ) ) ^ { 2 } \big ] \leq } \end{array}$ $c _ { 1 } \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 \beta }$ , where $\beta \leq 1$ .

Assumptions B.1 and B.2 are similar to the assumptions made in Molanes Lopez et al. [2009]. In Assumption B.1, we impose smoothness directly on the risk function ${ \mathcal { R } } ( \theta )$ instead of on the loss function $\ell ( x , \theta )$ . Therefore, we are able to handle non-smooth loss functions like those involving indicator functions as in quantile regression. Moreover, we only require the Lipschitz continuity of $\Delta _ { \theta } = \mathbb { E } ( g ( X , \theta ) g ( X , \theta ) ^ { T } )$ instead of $g ( x , \theta )$ . The statement in Assumption B.1 and B.2 is a sufficient condition to Assumptions (C4)-(C6) in Molanes Lopez et al. [2009] and is easier to verify .

Theorem 3. Under Assumptions A.2’, A.3, B.1 and B.2, there exist constants $( C , C _ { 1 } , C _ { 2 } )$ independent of $n$ , such that if $C _ { 1 } \log n \leq \alpha _ { n } \leq C _ { 2 } { \sqrt { n \log n } }$ , then it holds with probability at least $1 - n ^ { - 1 }$ that,

$$
d _ { \mathrm { T V } } \Big ( \pi _ { \mathrm { P E } } ( \cdot \mid X _ { 1 : n } ) , N \big ( \hat { \theta } ^ { \circ } , n ^ { - 1 } V _ { \theta ^ { * } } \big ) \Big ) \leq C \frac { ( \log n ) ^ { 1 + \beta / 2 } } { n ^ { \beta / 2 } } ,
$$

where $\begin{array} { r } { \hat { \theta } ^ { \diamond } = \theta ^ { \ast } - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \mathcal { H } _ { \theta ^ { \ast } } ^ { - 1 } g ( X _ { i } , \theta ^ { \ast } ) } \end{array}$ , $\pi _ { \mathrm { P E } } ( \cdot | X _ { 1 : n } )$ is the Bayesian PETEL posterior distribution with $\nabla _ { \boldsymbol { \theta } } \ell$ replaced by $g$ and $V _ { \theta ^ { * } } = H _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } H _ { \theta ^ { * } } ^ { - 1 }$ . In addition, we have ${ \sqrt { n } } ( { \hat { \theta } } ^ { \circ } -$ $\theta ^ { * } ) \to N ( 0 , V _ { \theta ^ { * } } )$ in distribution as $n \to \infty$ .

If the loss function $\ell$ is differentiable with respect to $\theta$ everywhere and $g ( x , \theta )$ is chosen to be $\nabla _ { \theta } \ell ( X , \theta )$ , by a standard analysis of empirical risk minimizer [Newey and McFadden, 1986], $\| \hat { \theta } ^ { \circ } - \hat { \theta } \| _ { 2 } = O _ { p } ( n ^ { - 1 } )$ , and $\hat { \theta } ^ { \circ }$ in Theorem 3 can be replaced with $\hat { \theta }$ . Therefore, Theorem 2 can be viewed as a special case of Theorem 3.

# 4.4 Analysis of Bayesian PETEL posterior for high-dimensional problem

We consider the high-dimensional setting as discussed in Section 3.2. We assume our estimation target $\theta ^ { * }$ , the global minimizer of risk function $\mathcal { R }$ over $\Theta$ , is $s ^ { * }$ -sparse for some $s ^ { * } \ll n$ . The following Theorem 4 gives a non-asymptotic analysis to the “model-averaged” Bayesian PETEL posterior distribution defined in equation 6. To begin with, we state the following regularity conditions.

Assumption C.1: There exists an $( n , d )$ independent constant $c$ such that $\Theta$ is contained in $[ - c , c ] ^ { d }$ . Moreover, there exist some constants $\left( c _ { 0 } , c _ { 1 } \right)$ independent of $( n , d )$ such that for any $S \subseteq [ d ]$ with $| S | \le s _ { 0 }$ , it holds that $\ell ( x , \theta _ { S } , 0 )$ is uniformly bounded by $c _ { 0 }$ and uniformly $c _ { 1 }$ Lipschitz with respect to $\theta _ { S }$ over $\theta _ { S } \in \Theta _ { S }$ and $x \in \mathcal { X }$ .

Assumption C.2: There exists a positive constant $c _ { 2 }$ independent of $( n , d )$ such that $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq c _ { 2 } \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { 2 }$ holds for any $\theta \in \Theta$ that is at most $s _ { 0 }$ sparse.

Assumption C.2’: There exists a positive constant $c _ { 3 }$ independent of $( n , d )$ such that $\operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } \ge c _ { 3 } \sqrt { \log ( d \vee n ) / n }$ . Moreover, there exists a positive constant $c _ { 4 }$ independent of $( n , d )$ such that $\mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq c _ { 4 } \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { 2 }$ holds for any $\theta \in \Theta$ that is at most $s ^ { * }$ sparse.

Assumption C.3: There exist some positive constants $( c _ { 5 } , r , L )$ such that $\pi _ { S ^ { * } } ( \theta _ { S ^ { * } } ^ { * } ) \ge c _ { 5 }$ and $| \pi _ { S ^ { \ast } } ( \theta _ { S ^ { \ast } } ) - \pi _ { S ^ { \ast } } ( \theta _ { S ^ { \ast } } ^ { \ast } ) | \leq L \| \theta _ { S ^ { \ast } } - \theta _ { S ^ { \ast } } ^ { \ast } \| _ { 2 }$ holds for any $\theta _ { S ^ { * } } \in B _ { r } ( \theta _ { S ^ { * } } ^ { * } )$ , where $S ^ { * } = S ( \theta ^ { * } )$ denotes the support of $\theta ^ { * }$ .

Assumption C.2 guarantees the concentration of the “model-averaged” Bayesian PETEL posterior to the population risk minimizer $\theta ^ { * }$ . If all nonzero signals in $\theta ^ { * }$ are suitably large as in Assumption C.2’, then Assumption C.2 can be relaxed to the second statement of Assumption C.2’.

Theorem 4. Suppose the risk function $\mathcal { R } ( \theta ) : \mathbb { R } ^ { d }  \mathbb { R }$ has a unique global minimizer $\theta ^ { * }$ on $\Theta$ that is $s ^ { * }$ sparse, where $\theta _ { S ^ { \ast } } ^ { \ast } \in \Theta _ { S ^ { \ast } } ^ { \circ }$ , $s ^ { * } \leq s _ { 0 }$ , $d \leq \exp ( C n )$ with an $( n , d )$ independent constant $C$ and Assumption C.1, C.3 holds. Suppose Assumptions A.1 and A.2’ hold for the loss function $\ell ( x , \theta _ { S ^ { * } } , 0 )$ and risk function $\mathcal { R } ( \theta _ { S ^ { * } } , 0 )$ with the parameter space being $\Theta _ { S ^ { * } }$ , then there exist constants $( C _ { 0 } , C _ { 1 } , C _ { 2 } )$ independent of n and d such that if $C _ { 0 } \log n \leq \alpha _ { n , d } \leq C _ { 1 } n$ , then with probability at least $1 - n ^ { - 1 }$ the “model-averaged” Bayesian PETEL posterior in (6) satisfies

$$
d _ { \mathrm { T V } } \bigg ( \pi _ { \mathrm { P E } } ( \cdot \vert S ^ { \ast } , X _ { 1 : n } ) , N \Big ( \hat { \theta } _ { S ^ { \ast } } , \frac { 1 } { n } \big ( V _ { \theta _ { S ^ { \ast } } ^ { S ^ { \ast } } } ^ { S ^ { \ast } } + \frac { \alpha _ { n , d } } { n } \mathcal { H } _ { \theta _ { S ^ { \ast } } ^ { S ^ { \ast } } } ^ { S ^ { \ast } } \big ) ^ { - 1 } \Big ) \bigg ) \leq C _ { 2 } \sqrt { \frac { \log n } { n } } ,
$$

where $\mathcal { H } _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } }$ is the Hessian of $\mathcal { R } ( \theta _ { S ^ { * } } , 0 )$ at $\theta _ { S ^ { * } } ^ { * }$ , $\Delta _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } } = \mathbb { E } ( \nabla _ { \theta _ { S ^ { * } } } \ell ( X , \theta _ { S ^ { * } } ^ { * } , 0 ) \nabla _ { \theta _ { S ^ { * } } } \ell ( X , \theta _ { S ^ { * } } ^ { * } , 0 ) ^ { T } )$ and $V _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } } = \mathcal { H } _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } \ - 1 } \Delta _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } } \mathcal { H } _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } \ - 1 }$ . In addition:

1. If Assumption C.2 holds, then there exist some positive constants $\left( C _ { 0 } ^ { \prime } , C _ { 1 } ^ { \prime } , C _ { 2 } ^ { \prime } , C _ { 3 } ^ { \prime } , C _ { 4 } ^ { \prime } \right)$ independent of $n$ and $d$ such that $C _ { 1 } ^ { \prime } \leq C _ { 3 } ^ { \prime }$ and if $\beta _ { n , d } = C _ { 0 } ^ { \prime } \log ( d \vee n )$ and $\left( C _ { 1 } ^ { \prime } n \right) \wedge$ $( C _ { 2 } ^ { \prime } \log ( d \vee n ) / \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } ) \leq \alpha _ { n , d } \leq C _ { 3 } ^ { \prime } n$ , then it holds with probability at least $1 - n ^ { - 1 }$ that

$$
\Pi _ { \mathrm { P E } } \Big ( \| \theta - \theta ^ { * } \| _ { 2 } \leq C _ { 4 } ^ { \prime } \sqrt { \frac { \log d \vee \log n } { n } } \Big | X _ { 1 : n } \Big ) \geq 1 - \frac { 1 } { d \vee n } .
$$

2. If Assumption C.2’ holds with a large enough $c _ { 2 }$ , then there exist some positive constants $( \bar { C } _ { 0 } , \bar { C } _ { 1 } , \bar { C } _ { 2 } , \bar { C } _ { 3 } , \bar { C } _ { 4 } )$ independent of $n$ and $d$ such that if $\bar { C } _ { 0 }$   $\left( \log ( d \lor n ) ) \lor \right.$ $( \alpha _ { n , d } { \sqrt { \log ( d \vee n ) / n } } ) )$ $\leq \beta _ { n , d } \leq \bar { C } _ { 1 } \alpha _ { n , d } \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 }$ and $\bar { C } _ { 2 } \log ( d \vee n ) / \underset { i \in S ^ { * } } { \operatorname* { m i n } } \theta _ { i } ^ { * 2 } \leq \alpha _ { n , d } \leq \bar { C } _ { 3 } n$ , then it holds with probability at least $1 - n ^ { - 1 }$ that

$$
\Pi _ { \mathrm { P E } } \big ( S ^ { * } \mid X _ { 1 : n } \big ) \ge 1 - \exp ( - \bar { C } _ { 4 } \beta _ { n , d } ) ,
$$

Theorem 4 shows that when $\log d \leq C { \sqrt { n } }$ and $\operatorname* { m i n } _ { i \in S ^ { * } } \left| \theta _ { i } ^ { * } \right|$ is lower bounded by a positive $( n , d )$ -independent constant, if we choose $( \log d \lor \log n ) \lesssim \alpha _ { n , d } \lesssim \sqrt { n \log n }$ and $( \log d \lor$ $\log n ) \lesssim \beta _ { n , d } \lesssim \alpha _ { n , d }$ , then the Bayesian PETEL posterior of $\theta \in \mathbb { R } ^ { d }$ converges to a degenerate $s ^ { * }$ -dimensional normal distribution with mean $\hat { \theta } _ { S ^ { * } }$ and covariance matrix $V _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } }$ with rate $O ( { \sqrt { \frac { \log n } { n } } } )$ . Since $\sqrt { n } ( \hat { \theta } _ { S ^ { * } } - \theta _ { S ^ { * } } ^ { * } )  N ( 0 , V _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } } )$ in distribution as $n  \infty$ , it follows that the highest posterior region derived from the Bayesian PETEL posterior distribution has valid frequentist coverage probability.

# 5 Numerical Studies

In this section, we will investigate the performance of the Bayesian PETEL from the frequentist perspective in classification and regression problems, using both synthetic and real datasets. In addition to Bayesian PETEL, we include three other methods in our comparison.

• CG (calibrated Gibbs posterior): A Bayesian method proposed in Syring and Martin [2018], where they estimate the coverage probability by checking if the highest posterior density credible region $\{ \theta : \pi _ { G } ( \theta | X _ { 1 : n } ) \geq c _ { \alpha } \}$ , with $c _ { \alpha }$ being chosen such that its posterior coverage is $1 - \alpha$ based on the bootstrapping data, covers the empirical risk minimizer, and apply stochastic approximation to update the learning rate of Gibbs posterior until the estimated coverage probability is equal to the nominal level.   
• Bootstrap: A frequentist method by bootstrapping the given data and constructing confidence intervals using bootstrapping empirical risk minimizers.   
• (Misspecfied) ALD: A Bayesian method used in quantile regression, where the response distribution is misspecified to be an asymmetric Laplace distribution (ALD) [Sriram et al., 2013].

Unless otherwise specified, in the following simulation and real data examples, for Bayesian method, we use Metropolis-Hasting algorithm to generate 3000 posterior samples, and use their $\frac { \alpha } { 2 }$ and $1 - { \frac { \alpha } { 2 } }$ quantiles to construct $1 - \alpha$ Bayes credible intervals independently for each dimension of $\theta$ . For Bootstrap, we resample the data 3000 times, and construct $1 - \alpha$ confidence intervals using the $\frac { \alpha } { 2 }$ and $1 - { \frac { \alpha } { 2 } }$ quantiles of bootstrapping empirical risk minimizers solved by gradient descent. The coverage probabilities (coverage) and average interval lengths (length) are computed based on 1000 replicates. We use average error to denote the average of the $\ell _ { 2 }$ norm of the difference between the resulting point estimates (posterior mean or bootstrapping empirical risk minimizer average) and the population minimizer of the risk function.

# 5.1 Simulation examples

In our simulation study, we will use synthetic data to investigate the performance of the Bayesian PETEL in classification, robust regression and quantile regression problem.

# 5.1.1 Classification via support vector machine

The soft-margin SVM [Duda et al., 2012] minimizes $\begin{array} { r } { \frac { 1 } { 2 } \lambda \| \theta \| _ { 2 } ^ { 2 } + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname* { m a x } ( 0 , 1 - Y _ { i } \theta ^ { T } \dot { X } _ { i } ) } \end{array}$ over $\theta \in \mathbb { R } ^ { d }$ with given data $\{ ( \tilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ and $Y _ { i } = \pm 1$ . The value of $\lambda > 0$ controls the $\ell _ { 2 }$ norm of $\theta$ and the function $\operatorname* { m a x } ( 0 , 1 - Y \theta ^ { T } \tilde { X } )$ is called the hinge-loss function. Following Hajewski et al. [2018], we also consider the smoothed hinge loss $\textstyle { \frac { 1 } { 2 } } ( { \sqrt { u ^ { 2 } + \varepsilon ^ { 2 } } } + u )$ with $u = 1 - Y { \theta } ^ { T } \tilde { X }$ and $\varepsilon$ being a small number, so the SVM with smoothed hinge loss minimizes $\textstyle { \frac { 1 } { 2 } } \lambda \| \theta \| _ { 2 } ^ { 2 } + { \frac { 1 } { 2 n } } \sum _ { i = 1 } ^ { n } ( { \sqrt { u _ { i } ^ { 2 } + \varepsilon ^ { 2 } } } + u _ { i } )$ where $u _ { i } = 1 - Y _ { i } \theta ^ { T } \tilde { X } _ { i }$ . We generate a synthetic data by creating two centroids $c _ { 1 } = ( 0 . 6 4 , 0 . 4 5 )$ and $c _ { - 1 } = ( - 1 . 1 8 , - 0 . 2 4 )$ , then uniformly sampling $Y$ from $\{ - 1 , 1 \}$ and given $Y = i$ , sampling $\tilde { X } \sim N ( c _ { i } , I _ { 2 } )$ with $c _ { i }$ being the respective centroid. We use the synthetic data to study the performance of Bayesian PETEL posterior for estimation and inference on the global minimizer of the population level loss function associated with SVM with hinge loss (SVMH) problem and smoothed hinge loss (SVMSH) problem with different $n$ and $\alpha _ { n }$ , where $\lambda = 0 . 1$ and $\varepsilon = 0 . 5$ . We also include in the comparison two other methods, one is the classical bootstrapping method (Bootstrap) and the other one is the Calibrated Gibbs posterior (CG). The Coverage probabilities and average interval lengths with target coverage being 95% are shown in Table 1 and Table 2.

We can see from the tables that, first, our method is robust to choices of the penalty parameter $\alpha _ { n }$ in both SVMH and SVMSH, as the coverage is at most 0.018 away from the target 0.95 and the change of the interval length is at most 0.021 when $\alpha _ { n }$ is from $0 . 5 n ^ { \frac { 1 } { 4 } }$ to $2 n ^ { \frac { 1 } { 2 } }$ . Second, the Calibrated Gibbs posterior (CG) tends to underestimate the precision of the inference of $\theta _ { 1 }$ and overestimate the precision of the inference of $\theta _ { 2 }$ , for the reason that we cannot find a learning rate that simultaneously corrects all entries in the covariance matrix. Table 3 gives coverage probabilities of our method with $\alpha _ { n } = 0 . 5 n ^ { \frac { 1 } { 4 } }$ , CG and Bootstrap for different target coverages, we can see when the sample size $n$ is 500 and target coverage is $7 0 \%$ , the coverage of $\theta _ { 1 }$ from CG is $1 1 . 7 \%$ away from 70% in SVMH and $1 2 \%$ away from $7 0 \%$ in SVMSH, while our method is at most $2 . 1 \%$ away from the target. Moreover, coverage probabilities of CG do not improve when $n$ increases from 500 to 1000, while we can see an obvious improvement in our method. Indeed, in the example of SVMSH, the variance vector in the Gaussian limiting distribution of Gibbs posterior with learning rate $\gamma$ and sample size $n$ is approximately $n ^ { - 1 } ( 1 . 1 4 8 / \gamma , 1 . 1 9 0 / \gamma )$ , while the variance vector in the Gaussian limiting distribution of the empirical risk minimizer is approximately $n ^ { - 1 } ( 0 . 9 5 3 , 1 . 9 7 5 )$ , so no matter how large is the sample size, there does not exist a learning rate that calibrate the credible intervals of $\theta _ { 1 }$ and $\theta _ { 2 }$ simultaneously. Moreover, from Table 3, our method performs slightly better than classical bootstrapping method in terms of coverage probabilities, as the deviances of coverage probabilities from the target coverages for our method are in general smaller than that of bootstrapping. It appears that in Table 3, most coverage probabilities of Bayesian PETEL in the SVMSH column are closer to their nominal values than those in the SVMH column. This phenomenon may attribute to our theoretical results that the Bayesian PETEL with smoothed hinge loss converges to its Gaussian limiting distribution at a faster rate of $O _ { p } ( n ^ { - \frac { 1 } { 2 } } )$ (c.f. Theorem 2) than the Bayesian PETEL with hinge loss whose rate is $O _ { p } ( n ^ { - \frac { 1 } { 4 } } )$ (c.f. Corollary 2 in Appendix B.2). In addition, a larger sample size may be required for improving the performance of all methods for uncertainty quantification when estimating $\theta _ { 2 }$ (it suffers from noticeable precision overestimation/underestimation across all methods). To study the performance of the resulting point estimators derived from Bayesian PETEL, CG and Bootstrap for correctly classifying the data, we provide in Table 4 the average testing accuracies of the resulting point estimators based on 500 training samples and 500 testing samples, where the average testing accuracy means the average of probabilities that the testing sample is correctly classified using the corresponding point estimator. We can see the average testing accuracies are quite similar among the three methods.

Table 1: Coverage probabilities ( $\%$ ) and average interval lengths under SVMH   

<table><tr><td></td><td></td><td colspan="2">Bayesian PETEL an=0.5n4</td><td colspan="2">Bayesian PETEL an =2n</td><td colspan="2">Bayesian PETEL an =0.5n3</td><td colspan="2">Bayesian PETEL an=2n3</td></tr><tr><td></td><td></td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td></tr><tr><td rowspan="2">n = 500</td><td>01</td><td>96.1</td><td>0.171</td><td>96.0</td><td>0.170</td><td>96.6</td><td>0.170</td><td>95.7</td><td>0.169</td></tr><tr><td>.</td><td>95.5</td><td>0.241</td><td>95.1</td><td>0.237</td><td>95.6</td><td>0.239</td><td>94.8</td><td>0.234</td></tr><tr><td>n = 1000</td><td>0 0</td><td>95.9 94.1</td><td>0.121</td><td>95.5</td><td>0.121</td><td>96.0</td><td>0.122</td><td>95.3</td><td>0.120</td></tr><tr><td></td><td></td><td>Bayesian PETEL</td><td>0.170</td><td>93.9</td><td>0.169 Bayesian PETEL</td><td>93.9</td><td>0.170</td><td>93.9</td><td>0.169</td></tr><tr><td></td><td></td><td>an =0.5n</td><td></td><td>an=</td><td>2n</td><td>CG</td><td></td><td>Bootstrap</td><td></td></tr><tr><td></td><td></td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td></tr><tr><td rowspan="2">n = 500</td><td>01</td><td>96.0</td><td>0.169</td><td>95.5</td><td>0.163</td><td>98.7</td><td>0.210</td><td>94.2</td><td>0.132</td></tr><tr><td>.</td><td>94.7</td><td>0.236</td><td>93.5</td><td>0.222</td><td>92.7</td><td>0.215</td><td>92.5</td><td>0.184</td></tr><tr><td rowspan="2">n = 1000</td><td>0</td><td>95.6</td><td>0.120</td><td>95.4</td><td>0.117</td><td>98.8</td><td>0.156</td><td>94.5</td><td>0.095</td></tr><tr><td>0</td><td>93.7</td><td>0.168</td><td>93.2</td><td>0.161</td><td>93.2</td><td>0.159</td><td>91.6</td><td>0.131</td></tr></table>

Table 2: Coverage probabilities $( \% )$ and average interval lengths under SVMSH   

<table><tr><td></td><td></td><td colspan="2">Bayesian PETEL an = 0.5n</td><td colspan="2">Bayesian PETEL 2n an=</td><td colspan="2">Bayesian PETEL an =0.5n3</td><td colspan="2">Bayesian PETEL 2n an=</td></tr><tr><td></td><td></td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td></tr><tr><td rowspan="2">n = 500</td><td>01</td><td>94.6</td><td>0.169</td><td>94.8</td><td>0.168</td><td>94.6</td><td>0.169</td><td>94.2</td><td>0.167</td></tr><tr><td>0</td><td>95.6</td><td>0.243</td><td>95.2</td><td>0.239</td><td>95.3</td><td>0.241</td><td>94.9</td><td>0.237</td></tr><tr><td>n = 1000</td><td>01</td><td>94.9</td><td>0.120</td><td>95.1</td><td>0.120</td><td>95.2</td><td>0.120</td><td>95.0</td><td>0.120</td></tr><tr><td></td><td>0</td><td>94.5 Bayesian PETEL</td><td>0.173</td><td>94.8</td><td>0.171 Bayesian PETEL</td><td>94.7</td><td>0.172</td><td>94.2</td><td>0.170</td></tr><tr><td></td><td></td><td>an=0.5n</td><td></td><td>an=</td><td>2n</td><td>CG</td><td></td><td>Bootstrap</td><td></td></tr><tr><td></td><td></td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td><td>coverage</td><td>length</td></tr><tr><td rowspan="2">n = 500</td><td>01</td><td>94.5</td><td>0.168</td><td>93.3</td><td>0.162</td><td>98.5</td><td>0.225</td><td>95.2</td><td>0.171</td></tr><tr><td>0</td><td>95.1</td><td>0.239</td><td>94.3</td><td>0.222</td><td>94.1</td><td>0.230</td><td>95.4</td><td>0.246</td></tr><tr><td rowspan="2">n = 1000</td><td>0</td><td>95.1</td><td>0.120</td><td>94.3</td><td>0.117</td><td>99.0</td><td>0.163</td><td>94.8</td><td>0.121</td></tr><tr><td>0</td><td>94.5</td><td>0.171</td><td>93.5</td><td>0.164</td><td>94.0</td><td>0.167</td><td>93.8</td><td>0.174</td></tr></table>

Table 3: Coverage probabilities ( $\%$ ) for different target coverages $9 0 \%$ , $8 0 \%$ , $7 0 \%$ ) under SVMH and SVMSH   

<table><tr><td rowspan="2"></td><td rowspan="2">Bayesian</td><td colspan="3">SVMH</td><td colspan="3">SVMSH</td></tr><tr><td>PETEL</td><td>CG</td><td>Bootstrap</td><td>Bayesian PETEL</td><td>CG</td><td>Bootstrap</td></tr><tr><td rowspan="6">n = 500</td><td>90%</td><td>01</td><td>91.7</td><td>96.4</td><td>88.4</td><td>89.0</td><td>95.2</td><td>88.7</td></tr><tr><td></td><td>.</td><td>91.0</td><td>86.9</td><td>87.1</td><td>89.7</td><td>87.4</td><td>88.8</td></tr><tr><td>80%</td><td>01</td><td>81.6</td><td>89.6</td><td>79.2</td><td>80.6</td><td>88.7</td><td>78.9</td></tr><tr><td></td><td>0</td><td>82.1</td><td>76.2</td><td>76.7</td><td>79.2</td><td>76.2</td><td>78.6</td></tr><tr><td>70%</td><td>01</td><td>71.8</td><td>81.7</td><td>70.5</td><td>68.3</td><td>82.0</td><td>70.1</td></tr><tr><td></td><td>0</td><td>71.8</td><td>66.7</td><td>66.0</td><td>69.4</td><td>67.3</td><td>68.0</td></tr><tr><td rowspan="6">n = 1000</td><td>90%</td><td>01</td><td>91.3</td><td>95.5</td><td>88.9</td><td>89.4</td><td>98.2</td><td>90.2</td></tr><tr><td></td><td>0</td><td>89.8</td><td>88.7</td><td>87.3</td><td>90.2</td><td>89.6</td><td>89.0</td></tr><tr><td>80%</td><td>01</td><td>81.3</td><td>89.8</td><td>77.5</td><td>80.0</td><td>92.4</td><td>80.9</td></tr><tr><td></td><td>0</td><td>79.0</td><td>76.7</td><td>73.7</td><td>80.8</td><td>79.4</td><td>78.9</td></tr><tr><td>70%</td><td>01</td><td>70.5</td><td>81.8</td><td>68.1</td><td>69.7</td><td>84.5</td><td>71.7</td></tr><tr><td></td><td>0</td><td>70.2</td><td>66.6</td><td>64.8</td><td>71.6</td><td>67.8</td><td>68.4</td></tr></table>

Table 4: Average testing accuracies under SVMH and SVMSH   

<table><tr><td colspan="3">SVMH</td><td colspan="3">SVMSH</td></tr><tr><td>Bayesian PETEL</td><td>CG</td><td>Bootstrap</td><td>Bayesian PETEL</td><td>CG</td><td>Bootstrap</td></tr><tr><td>0.830</td><td>0.830</td><td>0.832</td><td>0.831</td><td>0.831</td><td>0.832</td></tr></table>

Table 5: Coverage probabilities ( $\%$ ) and average interval lengths under Robust regression   

<table><tr><td rowspan="2"></td><td colspan="2">Bootstrap</td><td rowspan="2">Coverage</td><td rowspan="2">Bayesian ETEL Length</td><td rowspan="2">Coverage</td><td rowspan="2">Bayesian PETEL Length</td></tr><tr><td>Coverage</td><td>Length</td></tr><tr><td rowspan="3">Target=95%</td><td>01</td><td>98.0</td><td>3.67</td><td>72.0</td><td>1.24</td><td>93.4</td><td>0.68</td></tr><tr><td>0</td><td>99.5</td><td>4.06</td><td>77.3</td><td>1.13</td><td>93.9</td><td>1.00</td></tr><tr><td>03</td><td>96.7</td><td>0.70</td><td>71.9</td><td>0.44</td><td>92.7</td><td>0.39</td></tr><tr><td rowspan="3">Target=90%</td><td>01</td><td>95.8</td><td>2.85</td><td>67.8</td><td>1.04</td><td>87.4</td><td>0.57</td></tr><tr><td>02</td><td>97.6</td><td>3.40</td><td>72.5</td><td>0.94</td><td>88.6</td><td>0.84</td></tr><tr><td>03</td><td>93.7</td><td>0.58</td><td>66.6</td><td>0.37</td><td>87.3</td><td>0.33</td></tr></table>

# 5.1.2 Robust regression for learning sigmoid unit

Consider the simple example of learning a sigmoid unit. Let $\begin{array} { r } { S ( z ) = \frac { \exp ( z ) } { 1 + \exp ( z ) } } \end{array}$ for $z \in \mathbb { R }$ . We assume the predictor $\tilde { X } \in \mathbb { R } ^ { 2 }$ follows $N ( 0 , I _ { 2 } )$ and the response $Y$ is generated by the model $Y = \theta _ { 3 } ^ { * } \cdot S ( \theta _ { 1 } ^ { * } \tilde { X } _ { 1 } + \theta _ { 2 } ^ { * } \tilde { X } _ { 2 } ) + e$ , where $\theta ^ { * } = ( \theta _ { 1 } ^ { * } , \theta _ { 2 } ^ { * } , \theta _ { 3 } ^ { * } ) = ( 1 , 2 , 3 )$ and the heterogeneous error $e$ follows a Cauchy distribution with location being 0 and scale being kX√˜ k2 . We consider the Huber loss

$$
\ell ( X , \theta ) = \left\{ \begin{array} { l l } { \frac { 1 } { 2 } ( Y - \theta _ { 3 } \cdot S ( \theta _ { 1 } \tilde { X } _ { 1 } + \theta _ { 2 } \tilde { X } _ { 2 } ) ) ^ { 2 } } & { \mathrm { f o r ~ } | Y - \theta _ { 3 } \cdot S ( \theta _ { 1 } \tilde { X } _ { 1 } + \theta _ { 2 } \tilde { X } _ { 2 } ) | \leq \delta } \\ { \delta | Y - \theta _ { 3 } \cdot S ( \theta _ { 1 } \tilde { X } _ { 1 } + \theta _ { 2 } \tilde { X } _ { 2 } ) | - \frac { 1 } { 2 } \delta ^ { 2 } } & { \mathrm { o t h e r w i s e } } \end{array} \right.
$$

where $X = ( \tilde { X } , Y )$ and $\delta$ is fixed to be 2 here. We sample $n = 5 0 0$ number of i.i.d samples $\{ ( \tilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ and use the synthetic data to study the performance of Bayesian PETEL/ETEL and bootstrapping. For Bayesian PETEL, to achieve fast convergence, we first generate 500 number of samples from Bayesian PETEL posterior with $\alpha _ { n } = n$ using symmetric random-walk Metropolis algorithm (RMW), where the initial point is randomly selected from $N ( 2 , 4 I _ { 3 } )$ , then we use the mean of 400 to 500 posterior samples to be the new initial point, and generate 3000 number of samples from Bayesian PETEL posterior with $\alpha _ { n }$ equal to $2 \sqrt { n }$ . For Bootstrap, we use gradient descent to solve the empirical risk minimizer and for Bayesian ETEL, we use RMW to generate posterior samples, where initial points in gradient descent algorithm and RMW algorithm are randomly selected from $N ( 2 , 4 I _ { 3 } )$ respectively.

The coverage probabilities and average interval lengths are given in Table 5. We can see from Table 5 that firstly, Bayesian PETEL performs notably better than Bootstrap and Bayesian ETEL in terms of coverage probability. Specifically, the Bootstrap tends to underestimate the precision of inferences of $\theta _ { 1 }$ , $\theta _ { 2 }$ and $\theta _ { 3 }$ and the average interval lengths are much larger than those of Bayesian PETEL/ETEL. Moreover, the Bayesian ETEL tends to overestimate the precision of inferences of $\theta _ { 1 }$ , $\theta _ { 2 }$ and $\theta _ { 3 }$ . In addition, the average errors of the resulting point estimators are 1.084 for Bootstrap, 1.825 for Bayesian ETEL and 0.3124 for Bayesian PETEL, we can see that the posterior mean of Bayesian PETEL leads to a much better point estimator of $\theta ^ { * }$ than Bayesian ETEL and Bootstrap. These phenomenons are due to the fact that the risk function is not convex. Indeed, for the Bootstrap method, the marginal density plots for the first and second dimensions of the bootstrapping empirical risk minimizers solved by gradient descent algorithm are right heavy-tailed, which leads to wider confidence intervals. Specifically, the gradient vector field of the risk function in region $A = \left. 2 . 5 , 4 \right. \times \left. 4 , 7 . 5 \right. \times \left. 2 . 5 , 2 . 8 \right.$ is fairly flat (i.e., the $\ell _ { 2 }$ norms of the gradients of the risk function evaluated at points in set $A$ are all smaller than 0.1). For each bootstrapping replicate, if the initial point of the gradient descent algorithm lies in $A$ and the step size is too small for the next iterate to jump over this flat area, the algorithm will converge to some points inside $A$ instead of the true bootstrapping empirical risk minimizer. For the Bayesian ETEL method, depends on the initial state of the Markov chain, the random walk Metropolis-Hasting algorithm may get stuck in a local mode of the Bayesian ETEL posterior that is far away from $\theta ^ { * }$ , which leads to a large point estimation error for estimating $\theta ^ { * }$ ; while for the Bayesian PETEL method, the extra penalty term $- \alpha _ { n } \mathcal { R } _ { n } ( \theta )$ favors points closer to the empirical risk minimizer. Unlike the gradient descent which may converge to a local minimum or saddle point, the Markov chain has the ability of escaping from any local mode and the generated samples from the Bayesian PETEL after the burn-in period becomes all around $\theta ^ { * }$ with marginal densities for each dimension of $\theta$ being Gaussian-like. Further details are available in Appendix A.5.

# 5.1.3 High Dimensional Quantile Regression

Table 6: Coverage probabilities ( $\%$ ) and average interval lengths under High Dimensional Quantile Regression   

<table><tr><td rowspan="2"></td><td rowspan="2">Coverage</td><td rowspan="2">Bayesian PETEL Length</td><td colspan="2">BIC CG</td><td colspan="2">BIC Bootstrapping</td><td colspan="2">BIC ALD</td></tr><tr><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td></tr><tr><td>01</td><td>95.3</td><td>0.180</td><td>95.3</td><td>0.179</td><td>96.3</td><td>0.182</td><td>99.7</td><td>0.250</td></tr><tr><td>0</td><td>94.9</td><td>0.138</td><td>94.7</td><td>0.131</td><td>96.0</td><td>0.139</td><td>98.9</td><td>0.184</td></tr></table>

In quantile regression, for fixed $\tau \in ( 0 , 1 )$ , the $\tau ^ { t h }$ quantile of the response $Y \in \mathbb { R }$ given the covariates $\tilde { X } \in \mathbb { R } ^ { d }$ is modelled as

$$
Q _ { \tau } ( Y | \tilde { X } ) = \tilde { X } ^ { T } \theta ^ { * } .
$$

Here we consider loss function $\ell ( X , \theta ) = ( Y - \tilde { X } ^ { T } \theta ) ( \tau - \mathbf { 1 } ( Y < \tilde { X } ^ { T } \theta ) )$ [Syring and Martin, 2018] with $\tau = 0 . 5$ . To investigate the performance of our proposed “model-averaged” Bayesian PETEL posterior, we choose $d = 1 0 0 0$ and simulate datasets of $n = 5 0 0$ i.i.d observations where each $( \tilde { X } _ { i 1 } , \tilde { X } _ { i 2 } )$ is from multivariate Gaussian $N ( 0 , \mathrm { d i a g } ( 1 , 2 ) )$ and $( \tilde { X } _ { i 3 } , \cdots , \tilde { X } _ { i d } )$ is from $N ( 0 , I _ { d - 2 } )$ . To sample $Y _ { i } = \tilde { X } _ { i } ^ { T } \theta ^ { * } + e _ { i }$ , we use $\theta ^ { * } = ( 2 , 3 , \mathbf { 0 } _ { d - 2 } ^ { T } ) ^ { T }$ and the heterogeneous error $e _ { i }$ sampled from $N ( 0 , 0 . 5 \sqrt { ( X _ { i 1 } ^ { 2 } + X _ { i 2 } ^ { 2 } ) / 2 } )$ . To alleviate the curse of dimensionality, we first use stepwise search to find the model $\bar { S }$ that maximizes $\mathrm { e x p } ( - \alpha _ { n , d } \mathcal { R } _ { n } ( \hat { \theta } _ { S } , 0 ) - \beta _ { n , d } \vert S \vert - \mathrm { l o g } \left( { ^ d _ { | S | } } \right) )$ with $\alpha _ { n , d } = 2 \sqrt { n }$ and $\beta _ { n , d } = 1 . 2 \log d$ , where ${ \hat { \theta } } _ { S }$ is the constrained empirical risk minimizer on model $S$ . We limit the model space to models that have 1-bounded Hamming distances with $\tilde { S }$ and choose the prior to be $\pi ( S ) \propto \exp ( { - \beta _ { n , d } \lvert S \rvert } ) { \binom { d } { \lvert S \rvert } } ^ { - 1 }$ and $\pi ( \theta _ { S } | S ) = N ( \mathbf { 0 } _ { | S | } , I _ { | S | } )$ . We run the Bayesian PETEL algorithm a thousand times and get that the average Bayesian PETEL posterior probability of the true model is $2 \times 1 0 ^ { - 3 }$ away from 1. Furthermore, Table 6 gives coverage probabilities and average interval lengths of $9 5 \%$ Bayesian PETEL posterior credible intervals of $\theta _ { 1 }$ and $\theta _ { 2 }$ . To make comparison, we also consider Calibrated Gibbs posterior, bootstrapping estimators and misspecified ALD [Sriram et al., 2013] with the model selected by High dimensional BIC [Rigollet and Hütter, 2015] where the penalty parameter on the number of degrees of freedom is $1 0 \log d$ . We can see from Table 6 that for the quantile regression problem, our method achieves notably better performance than misspecified ALD, due to the misspecification of error distribution in the misspecified ALD. Moreover, our method performs similarly with BIC CG and slightly better than BIC Bootstrap, as coverage probabilities of BIC Bootstrap are at least $1 \%$ away from 95%, while those of Bayesian PETEL are at most 0.3% away of 95%. In addition, the average errors of the resulting point estimators are 0.1892 for Bayesian PETEL, 0.1997 for BIC CG, 0.1950 for BIC Bootstrap and 0.1898 for BIC ALD, thus our method achieves the smallest average error among methods considered in this section.

# 5.2 Markov chain Monte Carlo convergence and efficiency

In this section, we use Gelman–Rubin convergence diagnostic tool [Gelman and Rubin, 1992] to check the convergence of the chains, and use their effective sample sizes and computation times to report the efficiency of the proposed MCMC algorithm. We study the convergence and efficiency of the proposed MCMC algorithm for implementing the proposed Bayesian PETEL posterior for (1) smooth loss function; (2) non-smooth loss function; (3) high-dimensional problems, using examples in Section 5.1.1 and Section 5.1.3. The proposed algorithms are implemented using the R program with a 2.3GHz computer processor.

# 5.2.1 Soft-margin SVMs with hinge loss and smoothed hinge loss

In this section, we consider the example of soft-margin SVMs with hinge loss (SVMH) and smoothed hinge loss (SVMSH) in Section 5.1.1. We use the Random walk Metropolis-Hasting algorithm with proposal $N ( \theta _ { \mathrm { o l d } } , \sigma ^ { 2 } I _ { d } )$ where $\theta _ { \mathrm { o l d } }$ is the previous one state in the Markov chain and $\sigma$ is a parameter that is tuned such that the acceptance rate of the Markov chain is close to 0.234. For both SVMH and SVMSH, the computation time of a single run with $n = 5 0 0$ , $\alpha _ { n } = 2 \sqrt { n }$ and 3000 iterations is 1.24 min on average.

The Gelman–Rubin plots available in Appendix A.5 shows that the MCMC procedure converges after 1000 iterations in both SVMSH and SVMH problems. The effective sample sizes of the Markov chain for each dimension of samples with a total of 3000 iterations are on average (402, 305) for SVMSH and (380, 294) for SVMH. We can see the effective sample sizes of the Markov chain for SVMSH are slightly larger than those of SVMH.

# 5.2.2 High dimensional sparse quantile Regression

In this section, we consider the example of high dimensional quantile regression in Section 5.1.3. We use the independence sampling algorithm with proposal $p _ { p r o p } ( S , \theta _ { S } ) =$ $p _ { p r o p } ( S ) p _ { p r o p } ( \theta _ { S } | S )$ being chosen as that described in Appendix A.4. The computation time of a single run with $n = 5 0 0$ , $d = 1 0 0 0$ , $\alpha _ { n , d } = 2 \sqrt { n }$ , $\beta _ { n , d } = 1 . 2 \log d$ and 3000 iterations is 1.87 min on average. The algorithm generates a sequence of samples $\{ ( S _ { i } , \theta _ { S , i } \} _ { i = 1 } ^ { 3 0 0 0 }$ , with $S _ { i }$ being the model and $\theta _ { S , i }$ being the parameter corresponds to $S _ { i }$ . We can consider the sequence of $\theta _ { S , i }$ that corresponds to the true model $S ^ { * } = ( 1 , 2 )$ , i.e. $\{ \theta _ { S , i _ { j } } \} _ { j = 1 } ^ { n ^ { \prime } }$ where $\begin{array} { r } { n ^ { \prime } = \sum _ { k = 1 } ^ { 3 0 0 0 } \mathbf { 1 } ( S _ { k } = S ^ { * } ) } \end{array}$ and $i _ { j } = \{ i \mid S _ { i } = S ^ { * }$ ; $\begin{array} { r } { \sum _ { k = 1 } ^ { i - 1 } \mathbf { 1 } ( S _ { k } = S ^ { * } ) = j - 1 \} } \end{array}$ . The number of $n ^ { \prime }$ are on average 2997 and we can learn from the Gelman–Rubin plots for multiple chains of $\{ \theta _ { S , i _ { j } } \} _ { j = 1 } ^ { n ^ { \prime } }$ in Appendix A.5 that the MCMC procedure converges after 1000 iterations. The effective sample sizes for each dimension of $\{ \theta _ { S , i _ { j } } \} _ { j = 1 } ^ { n ^ { \prime } }$ are on average (830, 785) respectively. The choice of the proposal distribution of the model $S$ is significant for efficiently sampling from Bayesian PETEL with high dimensional structures. Indeed, if we choose $p _ { p r o p } ( S )$ to be a uniform distribution among $S \subseteq [ d ]$ , the Markov chain may never generate samples correspond to the true model in any reasonable number of iterations, as the number of candidate models is extremely large. Therefore, we need to adjust the weight of the model in $\{ S \subseteq [ d ] \}$ to form a reasonable proposal, such that $p _ { p r o p } ( S )$ will only give mass to models that correspond to small constrained minimal empirical risks (i.e., $\mathcal { R } _ { n } ( \widehat { \theta } _ { S } , 0 )$ where ${ \hat { \theta } } _ { S }$ is the constrained empirical risk minimizer on model $S$ ) while in the meantime do not have large complexities. Possible choices of the $p _ { p r o p } ( S )$ are described in Appendix A.4.

Table 7: Coverage probabilities ( $\%$ ) and average interval lengths in the Parking Birmingham Dataset   

<table><tr><td rowspan="2"></td><td colspan="2">Bayesian PETEL</td><td colspan="2">CG</td><td colspan="2">ALD</td><td colspan="2">Bootstrap</td></tr><tr><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td></tr><tr><td>0</td><td>95.1</td><td>0.078</td><td>92.1</td><td>0.070</td><td>89.3</td><td>0.065</td><td>95.6</td><td>0.080</td></tr><tr><td>01</td><td>95.2</td><td>0.092</td><td>97.6</td><td>0.100</td><td>92.5</td><td>0.081</td><td>95.2</td><td>0.093</td></tr><tr><td>0</td><td>95.6</td><td>0.061</td><td>97.1</td><td>0.065</td><td>92.7</td><td>0.053</td><td>96.1</td><td>0.062</td></tr><tr><td>03</td><td>95.4</td><td>0.087</td><td>97.7</td><td>0.097</td><td>92.0</td><td>0.077</td><td>95.2</td><td>0.088</td></tr></table>

Table 8: Coverage probabilities ( $\%$ ) and average interval lengths in the Occupancy Detection Dataset   

<table><tr><td></td><td colspan="2">Bayesian PETEL</td><td colspan="2">CG</td><td colspan="2">Bootstrap</td></tr><tr><td></td><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td><td>Coverage</td><td>Length</td></tr><tr><td>01(Light)</td><td>93.7</td><td>0.0571</td><td>93.6</td><td>0.0567</td><td>95.6</td><td>0.0576</td></tr><tr><td>0(C02)</td><td>95.2</td><td>0.0541</td><td>97.2</td><td>0.0555</td><td>96.0</td><td>0.0545</td></tr><tr><td>03 (Humidity Ratio)</td><td>94.7</td><td>0.0640</td><td>94.2</td><td>0.0622</td><td>93.5</td><td>0.0644</td></tr></table>

# 5.3 Real data analysis

The good performance of Bayesian PETEL posterior in the simulation examples validates the correctness of our theoretical results in Section 4, that is, the Bayesian PETEL has valid frequentist properties when some regularity conditions are satisfied. However, it is also a crucial problem of whether our regularity conditions are met in real data applications. To check this, we conduct a real data analysis and study the performance of Bayesian PETEL and its competitors. In the real data analysis, we consider quantile regression with the Parking Birmingham Dataset and classification with the Occupancy Detection Dataset. In each example, to show the “correctness” of the inference from our method, we sample $n ^ { \prime } = 2 0 0 0$ samples with replacement from the original dataset 1000 times, and in each time, we construct 95% Bayesian credible intervals from Bayesian PETEL posterior with $\alpha _ { n ^ { \prime } } = 2 \sqrt { n ^ { \prime } }$ for each dimension of $\theta$ using the resampling dataset and check whether those credible intervals covers each dimension of the empirical risk minimizer $\hat { \theta }$ from the original dataset. Similarly for CG, Bootstrap and ALD. Moreover, we use average error to denote the average of the $\ell _ { 2 }$ norm of the difference between resulting point estimates (posterior mean or bootstrapping empirical risk minimizer average) and $\hat { \theta }$ .

# 5.3.1 Parking Birmingham Dataset

We study a dataset comprising Car park occupancy rate from 2016/10/04 to 2016/12/19. The predictors include time and car park capacity. The dataset is archived from UCI machine learning repository. We model the median of the response $Y$ (occupancy rate) given the covariate $T$ (time) and $\tilde { X }$ (car park capacity) by the following quantile regression model,

$$
Q _ { 0 . 5 } ( Y | T , \tilde { X } ) = \theta _ { 0 } \tilde { X } + \sum _ { k = 1 } ^ { K } \theta _ { k } B _ { k } ( T ) ,
$$

where $B _ { k } ( T )$ denote the $k$ th degree of B-spline in $T$ . $K$ is fixed to be 3 here and the columns of the data matrix are scaled to be with center 0 and variance 1. The coverage probabilities and average interval lengths computed by subsampling are given in Table 7. To make comparison, we also check coverage probabilities and average interval lengths of CG, ALD and Bootstrap with target coverage being $9 5 \%$ . We can see from Table 7 that our method performs better than CG and ALD in terms of coverage probabilities, and performs similarly with Bootstrap in terms of coverage probabilities and average interval lengths. Moreover, the average errors of the resulting point estimators from Bayesian PETEL, CG, ALD and Bootstrap are 0.1368, 0.1460, 0.1420 and 0.1493 respectively, we can see that Bayesian PETEL has the smallest average error.

# 5.3.2 Occupancy Detection Dataset

In this section, we consider the occupancy detection dataset, archived in UCI machine learning repository. The binary response variable $Y$ is the occupied status of a room which was obtained from time stamped pictures that were taken every minute. We focus here on predictors $\ddot { X }$ including Light, CO2 and Humidity ratio. The goal of this section is to conduct inference to the parameter $\theta$ under the problem of SVM using smoothed hinge loss, where the loss function is $\begin{array} { r } { \frac { 1 } { 2 } \lambda \| \theta \| _ { 2 } ^ { 2 } + \frac { 1 } { 2 } ( \sqrt { U ^ { 2 } + \varepsilon ^ { 2 } } + U ) } \end{array}$ with $U = 1 - Y \theta ^ { T } \tilde { X }$ . The tuning parameters $\lambda$ and $\varepsilon$ are chosen to be 0.5 and 0.1. The coverage probabilities and average interval lengths computed by subsampling are given in Table 8. We also include CG and Bootstrap in comparison. We can see that our method performs similarly with Bootstrap in terms of coverage probabilities and the average interval lengths of each dimension of $\theta$ in our method are all strictly smaller than those of Bootstrap. Moreover, our method achieves slightly better performance than CG, as the coverage probability of $\theta _ { 2 }$ using CG is $2 . 2 \%$ away from the target while the coverage probability in our method is at most 1.3% away from the target. In addition, the averaged errors of the resulting point estimators derived from Bayesian PETEL, CG and Bootstrap are 0.1092, 0.1059 and 0.1074 respectively, thus the average error of Bayesian PETEL is quite similar to that of CG and Bootstrap.

# 6 Discussion

In this paper, we propose the Bayesian penalized exponentially tilted empirical likelihood (Bayesian PETEL) posterior, which takes the exponentially tilted empirical likelihood (ETEL) into a Bayesian framework and uses the empirical risk to exponentially penalize certain “loss” of parameter $\theta$ on the training data. Our model is free from the underlying distribution and is theoretically justified in the sense that it can be approximated by a normal distribution centered at the empirical risk minimizer, and its covariance matrix matches the frequentist asymptotic covariance matrix of its mean vector. As a consequence, the posterior credible regions derived from Bayesian PETEL posteriors have approximately correct frequentist coverage. The theory we provided can adapt to the case that the loss function is non-smooth, which includes quantile regression and soft-margin SVM as two representative examples. Our method naturally extends to the sparse high dimensional model: we show that the proposed “model-averaged” Bayesian PETEL posterior converges to a normal distribution under the true model, and the accompanied Bayesian credible region has valid frequentist coverage. Compared with methods based on Gibbs posterior, our method does not require the generalized information equality and is thus insusceptible to the model misspecification biases. Furthermore, we show in the simulation study that the corresponding posterior inference from our method is notably more accurate than the calibrated Gibbs posterior and performs comparably to the bootstrapping. Although the current paper focused on the exponentially tilted empirical likelihood, using the empirical likelihood or some other variants may work as well, which will be left as a future direction.

# References

P. Alquier. PAC-Bayesian bounds for randomized empirical risk minimizers. Mathematical Methods of Statistics, 17(4):279–304, Dec 2008. ISSN 1934-8045. doi: 10.3103/ s1066530708040017. URL http://dx.doi.org/10.3103/S1066530708040017.   
H. B. Barlow. Unsupervised learning. Neural computation, 1(3):295–311, 1989.   
I. Bhattacharya and R. Martin. Gibbs posterior inference on multivariate quantiles. arXiv preprint arXiv:2002.01052, 2020.   
P. G. Bissiri, C. C. Holmes, and S. G. Walker. A general framework for updating belief distributions. Journal of the Royal Statistical Society. Series B, Statistical methodology, 78(5):1103, 2016.   
L. Bottolo and S. Richardson. Evolutionary stochastic search for bayesian model exploration. Bayesian Anal., 5(3):583–618, 09 2010. doi: 10.1214/10-BA523. URL https://doi.org/10.1214/10-BA523.   
M. Broniatowski and A. Keziou. Divergences and duality for estimation and test under moment condition models. Journal of Statistical Planning and Inference, 142(9):2554– 2573, 2012.   
J. Buhmann. Empirical risk approximation: An induction principle for unsupervised learning. Citeseer, 1998.   
C. M. Carvalho, N. G. Polson, and J. G. Scott. The horseshoe estimator for sparse signals. Biometrika, 97(2):465–480, 2010.   
I. Castillo, J. Schmidt-Hieber, and A. van der Vaart. Bayesian linear regression with sparse priors. Ann. Statist., 43(5):1986–2018, 10 2015. doi: 10.1214/15-AOS1334. URL https://doi.org/10.1214/15-AOS1334.

O. Catoni. PAC-Bayesian supervised classification: the thermodynamics of statistical learning. IMS Lecture Notes Monograph Series, page 1–163, 2007. ISSN 0749-2170. doi: 10. 1214/074921707000000391. URL http://dx.doi.org/10.1214/074921707000000391.

G. Cauwenberghs. A fast stochastic error-descent algorithm for supervised learning and optimization. In S. Hanson, J. Cowan, and C. Giles, editors, Advances in Neural Information Processing Systems, volume 5. Morgan-Kaufmann, 1993. URL https://proceedings.neurips.cc/paper/1992/file/ c06d06da9666a219db15cf575aff2824-Paper.pdf.

I. H. Chang and R. Mukerjee. Bayesian and frequentist confidence intervals arising from empirical-type likelihoods. Biometrika, 95(1):139–147, 2008. ISSN 00063444. URL http://www.jstor.org/stable/20441448.

J. Chen, R. R. Sitter, and C. Wu. Using empirical likelihood methods to obtain range restricted weights in regression estimators for surveys. Biometrika, 89(1):230–237, 03 2002. ISSN 0006-3444. doi: 10.1093/biomet/89.1.230. URL https://doi.org/10. 1093/biomet/89.1.230.

V. Chernozhukov and H. Hong. An MCMC approach to classical estimation. Journal of Econometrics, 115(2):293 – 346, 2003. ISSN 0304-4076. doi: https://doi.org/10.1016/ S0304-4076(03)00100-3. URL http://www.sciencedirect.com/science/article/ pii/S0304407603001003.

S. Chib, M. Shin, and A. Simoni. Bayesian estimation and comparison of moment condition models. Journal of the American Statistical Association, 113(524):1656– 1668, 2018. doi: 10.1080/01621459.2017.1358172. URL https://doi.org/10.1080/ 01621459.2017.1358172.

P. Dellaportas, J. J. Forster, and I. Ntzoufras. On Bayesian model and variable selection using MCMC. Statistics and Computing, 2002. doi: 10.1023/A:1013164120801.

R. Duda, P. Hart, and D. Stork. Pattern Classification. Wiley, 2012. ISBN 9781118586006. URL https://books.google.com/books?id=Br33IRC3PkQC.

S. A. Geer and S. van de Geer. Empirical processes in M-estimation, volume 6. Cambridge university press, 2000.

A. Gelman and D. B. Rubin. Inference from iterative simulation using multiple sequences. Statistical Science, 7(4):457 – 472, 1992. doi: 10.1214/ss/1177011136. URL https: //doi.org/10.1214/ss/1177011136.

A. Gelman, W. R. Gilks, and G. O. Roberts. Weak convergence and optimal scaling of random walk Metropolis algorithms. The Annals of Applied Probability, 7(1):110 – 120, 1997. doi: 10.1214/aoap/1034625254. URL https://doi.org/10.1214/aoap/ 1034625254.   
J. Ghosh and R. Ramamoorthi. Bayesian Nonparametric. Springer New York, New York, NY, 2003.   
P. Grünwald and T. van Ommen. Inconsistency of Bayesian inference for misspecified linear Models, and a proposal for repairing It. Bayesian Anal., 12(4):1069–1103, 12 2017. doi: 10.1214/17-BA1085. URL https://doi.org/10.1214/17-BA1085.   
B. Guedj. A primer on PAC-Bayesian learning. arXiv preprint arXiv:1901.05353, 2019.   
J. Hajewski, S. Oliveira, and D. Stewart. Smoothed hinge loss and $\ell _ { 1 }$ support vector machines. In 2018 IEEE International Conference on Data Mining Workshops (ICDMW), pages 1217–1223, 2018. doi: 10.1109/ICDMW.2018.00174.   
T. Hastie, R. Tibshirani, and J. Friedman. Linear methods for classification, pages 101–137. Springer New York, New York, NY, 2009. ISBN 978-0-387-84858-7. doi: 10.1007/ 978-0-387-84858-7_4. URL https://doi.org/10.1007/978-0-387-84858-7_4.   
P. J. Huber. Robust estimation of a location parameter. In Breakthroughs in statistics, pages 492–518. Springer, 1992.   
H. Ishwaran and J. S. Rao. Spike and slab variable selection: Frequentist and Bayesian strategies. The Annals of Statistics, 33(2):730 – 773, 2005.   
B. Kleijn and A. van der Vaart. The Bernstein-von-Mises theorem under misspecification. Electron. J. Statist., 6:354–381, 2012. doi: 10.1214/12-EJS675. URL https://doi. org/10.1214/12-EJS675.   
R. Koenker. Quantile Regression. Econometric Society Monographs. Cambridge University Press, 2005.   
R. Koenker and G. Bassett Jr. Regression quantiles. Econometrica: journal of the Econometric Society, pages 33–50, 1978.   
M. R. Kosorok. Introduction to empirical processes and semiparametric inference. Springer New York, New York, NY, 2008.   
S. Kullback. Information theory and statistics. Courier Corporation, 1997.   
N. A. Lazar. Bayesian empirical likelihood. Biometrika, 90(2):319–326, 2003. ISSN 00063444. URL http://www.jstor.org/stable/30042042.   
R. Martin and Y. Tang. Empirical priors for prediction in sparse high-dimensional linear regression. Journal of Machine Learning Research, 21(144):1–30, 2020. URL http://jmlr.org/papers/v21/19-152.html.   
R. Martin, R. Mess, and S. G. Walker. Empirical bayes posterior concentration in sparse high-dimensional linear models. Bernoulli, 23(3):1822–1847, Aug 2017. ISSN 1350-7265. doi: 10.3150/15-bej797. URL http://dx.doi.org/10.3150/15-BEJ797.   
D. A. McAllester. PAC-Bayesian model averaging. In Proceedings of the Twelfth Annual Conference on Computational Learning Theory, COLT ’99, page 164–170, New York, NY, USA, 1999. Association for Computing Machinery. ISBN 1581131674. doi: 10. 1145/307400.307435. URL https://doi.org/10.1145/307400.307435.   
E. M. Molanes Lopez, I. V. Keilegom, and N. Veraverbeke. Empirical likelihood for non-smooth criterion functions. Scandinavian Journal of Statistics, 36(3):413–432, 2009.   
W. K. Newey and D. McFadden. Large sample estimation and hypothesis testing. In R. F. Engle and D. McFadden, editors, Handbook of Econometrics, volume 4 of Handbook of Econometrics, chapter 36, pages 2111–2245. Elsevier, 1986. URL https://ideas. repec.org/h/eee/ecochp/4-36.html.   
A. Owen. Empirical likelihood ratio confidence regions. Ann. Statist., 18(1):90–120, 03 1990. doi: 10.1214/aos/1176347494. URL https://doi.org/10.1214/aos/1176347494.   
N. G. Polson and S. L. Scott. Data augmentation for support vector machines. Bayesian Analysis, 6(1):1 – 23, 2011. doi: 10.1214/11-BA601. URL https://doi.org/10.1214/ 11-BA601.   
M. Raič. A multivariate Berry–Esseen theorem with explicit constants. Bernoulli, 25 (4A):2824–2853, Nov 2019. ISSN 1350-7265. doi: 10.3150/18-bej1072. URL http: //dx.doi.org/10.3150/18-BEJ1072.   
J. N. K. Rao and C. Wu. Bayesian pseudo-empirical-likelihood intervals for complex surveys. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 72 (4):533–544, 2010. doi: https://doi.org/10.1111/j.1467-9868.2010.00747.x. URL https: //rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9868.2010.00747.x.   
P. Rigollet and J.-C. Hütter. High dimensional statistics. Lecture notes for course 18S997, 2015.   
H. Robbins and S. Monro. A stochastic approximation method. Ann. Math. Statist., 22(3):400–407, 09 1951. doi: 10.1214/aoms/1177729586. URL https://doi.org/10. 1214/aoms/1177729586.

P. Rousseeuw and V. Yohai. Robust regression by means of S-estimators. In Robust and nonlinear time series analysis, pages 256–272. Springer, 1984.

P. J. Rousseeuw and A. M. Leroy. Robust regression and outlier detection, volume 589. John wiley & sons, 2005.

S. M. Schennach. Bayesian exponentially tilted empirical likelihood. Biometrika, 92(1): 31–46, 2005. ISSN 00063444. URL http://www.jstor.org/stable/20441164.

S. M. Schennach. Point estimation with exponentially tilted empirical likelihood. The Annals of Statistics, 35(2):634 – 672, 2007. doi: 10.1214/009053606000001208. URL https://doi.org/10.1214/009053606000001208.

K. Sriram, R. Ramamoorthi, and P. Ghosh. Posterior consistency of Bayesian quantile regression based on the Misspecified Asymmetric Laplace Density. Bayesian Analysis, 8(2):479 – 504, 2013. doi: 10.1214/13-BA817. URL https://doi.org/10.1214/ 13-BA817.

C. Sun, D. Liu, and C. Yang. Model-free unsupervised learning for optimization problems with constraints. In 2019 25th Asia-Pacific Conference on Communications (APCC), pages 392–397. IEEE, 2019.

N. Syring and R. Martin. Calibrating general posterior credible regions. Biometrika, 106(2):479–486, Dec 2018. ISSN 1464-3510. doi: 10.1093/biomet/asy054. URL http: //dx.doi.org/10.1093/biomet/asy054.

N. Syring and R. Martin. Gibbs posterior concentration rates under sub-exponential type losses. arXiv preprint arXiv:2012.04505, 2020.

L. Tierney. Markov chains for exploring posterior distributions. Ann. Statist., 22(4): 1701–1728, 12 1994. doi: 10.1214/aos/1176325750. URL https://doi.org/10.1214/ aos/1176325750.

V. Vapnik. Principles of risk minimization for learning theory. In Proceedings of the 4th International Conference on Neural Information Processing Systems, NIPS’91, page 831–838, San Francisco, CA, USA, 1991. Morgan Kaufmann Publishers Inc. ISBN 1558602224.

R. Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2018. doi: 10.1017/9781108231596.

M. J. Wainwright. High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2019. doi: 10.1017/9781108627771.

R. R. Wilcox. Introduction to robust estimation and hypothesis testing. Academic press, 2011.   
C. Wu and W. W. Lu. Calibration weighting methods for complex surveys. International Statistical Review, 84(1):79–98, 2016. doi: https://doi.org/10.1111/insr.12097. URL https://onlinelibrary.wiley.com/doi/abs/10.1111/insr.12097.   
Z. Yang, Z. Wang, H. Liu, Y. Eldar, and T. Zhang. Sparse nonlinear regression: Parameter estimation under nonconvexity. In M. F. Balcan and K. Q. Weinberger, editors, Proceedings of The 33rd International Conference on Machine Learning, volume 48 of Proceedings of Machine Learning Research, pages 2472–2481, New York, New York, USA, 20–22 Jun 2016. PMLR. URL https://proceedings.mlr.press/v48/yangc16.html.   
K. Yu and R. A. Moyeed. Bayesian quantile regression. Statistics and Probability Letters, 54(4):437–447, 2001. ISSN 0167-7152. doi: https://doi.org/10.1016/ S0167-7152(01)00124-9. URL https://www.sciencedirect.com/science/article/ pii/S0167715201001249.   
A. Zellner. On assessing prior distributions and Bayesian regression analysis with g prior distributions. Bayesian Inference and Decision Techniques: Essays in Honor of Bruno de Finetti. Studies in Bayesian Econometrics and Statistics, 6:233–243, 1986.   
P. Zhao, M. Ghosh, J. N. K. Rao, and C. Wu. Bayesian empirical likelihood inference with complex survey data. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 82(1):155–174, 2020. doi: https://doi.org/10.1111/rssb.12342. URL https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/rssb.12342.

# Appendix

# A Computational Details

In this section, we will discuss computational aspects of sampling from the Bayesian PETEL posterior distribution.

# A.1 Algorithm Overview

Since the Bayesian PETEL provides an explicit expression for the posterior up to a normalisation constant, we can utilize the Metroplis-Hasting algorithm to draw posterior samples. In each step, we propose a new parameter $\tilde { \theta }$ from the proposal $p _ { p r o p } ( \theta | \theta _ { o l d } )$ , where $\theta _ { o l d }$ is the parameter value from the previous step. A uniform random number $u \in ( 0 , 1 )$ is drawn, if

$$
u < \frac { \pi ( \tilde { \theta } ) \exp ( \log L ( X ^ { n } ; \tilde { \theta } ) - \alpha _ { n } \mathcal { R } _ { n } ( \tilde { \theta } ) ) p _ { p r o p } ( \theta _ { o l d } | \tilde { \theta } ) } { \pi ( \theta _ { o l d } ) \exp \left( \log L ( X ^ { n } ; \theta _ { o l d } ) - \alpha _ { n } \mathcal { R } _ { n } ( \theta _ { o l d } ) \right) p _ { p r o p } ( \tilde { \theta } | \theta _ { o l d } ) } ,
$$

then we accept the proposed $\tilde { \theta }$ , otherwise, we retain $\theta _ { o l d }$ in the chain.

One major difficulty in the sampling from Bayesian PETEL posterior distribution is the computation of the log ETEL, as it involves solving the Lagrange multiplier $\begin{array} { r } { \lambda ( \theta ) = \arg \operatorname* { m i n } _ { \lambda } n ^ { - 1 } \sum _ { i = 1 } ^ { n } \exp ( \lambda ^ { T } \nabla _ { \theta } L ( x _ { i } , \theta ) ) } \end{array}$ . Since solving $\lambda ( \theta )$ is a convex problem, it can be calculated by modified Newton-Raphson algorithm [Chen et al., 2002]. Algorithm 1 summarizes the pseudocode for the Metroplis-Hasting steps to sample from Bayesian PETEL posterior and $\nabla _ { \theta } \ell ( X , \theta )$ is replaced by its subgradient when the loss function is not differentiable at $\theta$ .

# A.2 Choice of $\alpha _ { n }$

According to Theorem 2, the penalty parameter $\alpha _ { n }$ should be in the range $\log n \lesssim \alpha _ { n } \lesssim$ $\sqrt { n \log n }$ . In practice, we could choose $\alpha _ { n } = C n ^ { - c }$ with $0 < c \le 0 . 5$ and $C$ being a positive constant (e.g., $\alpha _ { n } = 0 . 5 \sqrt { n }$ ). We show in the simulation study in Section 5 that the performance of Bayesian PETEL is robust to the choice of $C$ and $c$ . In the case of small dataset, by the result in Theorem 1, the BETEL posterior distribution, which is equivalent to the Bayesian PETEL posterior with $\alpha _ { n } = 0$ , is asymptotically mixture of Gaussian, with centers being solutions of $\nabla _ { \boldsymbol { \theta } } \mathcal { R } _ { n } ( \boldsymbol { \theta } ) = 0$ , so the posterior mean of BETEL will mismatch that of the empirical risk minimizer when $\nabla _ { \theta } \mathcal { R } _ { n } ( \theta ) = 0$ has multiple solutions on $\Theta$ . So intuitively, with a small value of $\alpha _ { n }$ , the Bayesian PETEL posterior of $\theta$ may have several modes, while a large value of $\alpha _ { n }$ may lead to the invalidity of inference due to the mismatching of covariance matrix. According to this fact, we could tune the penalty parameter by starting with a small number (e.g. $\log n$ ) and increase it with step size $s _ { n }$ until the posterior mean matches that of the empirical risk minimizer, in which the empirical risk minimizer can be solved by subgradient/gradient descent or estimated by the posterior mean of the Gibbs posterior given by $\pi _ { \mathrm { { G } } } ( \theta | X ^ { n } ) \propto \pi ( \theta ) \exp ( - n \mathcal { R } _ { n } ( \theta ) )$ . Since the target range $\log n \lesssim \alpha _ { n } \lesssim \sqrt { n \log n }$ is wide, it’s safe to choose a large step size (e.g., $0 . 5 \sqrt { n }$ ), and a reasonable $\alpha _ { n }$ could be found in few steps.

<table><tr><td>osterior Input: Number of iteration L, tolerance ε, proposal distribution Pprop(·l·), initial state 0° and λ(00); Data:X1, X2 ... ,Xn;</td></tr><tr><td>fort←O toL-1do Sample θ from Pprop(-|0t); Generate a uniform random number u ∈ (0,1);</td></tr><tr><td>Define f(λ) ←¹∑²=1 exp(λT∀θl(xi,0)); 入°←入（0t）； k←0；</td></tr><tr><td>repeat k←k+1; γ =1;</td></tr><tr><td>H←∑i-1 xp(Vol(Xi,0)TX~-1）∀o(Xi,θ)el(Xi,）T;</td></tr><tr><td>G←∑- exp(v(xi,0θ)Tx-1)）l(xi,);； repeat λκ←λκ-1-γH-1G; γ=γ;</td></tr><tr><td></td></tr><tr><td>入(0t+1) ← 入(θ);</td></tr><tr><td>until f(λ²) ≤f(λ𝑘-1); until ||H-1G|l2 ≤ ε; 入（θ）←λ²； π()exp( exp(X(θ)Tge(Xi,0)) -anRn(0)) )pprop(0t1θ) ifu≤ then π(0t)exp( (∑=11 exp(入(0t)Te(Xi,0t)) log -anRn(θt)) Pprop(@θt) ∑=1exp(x（ot）Te(xi,0t）） 0t+1←θ；</td></tr></table>

# A.3 Choice of the proposal distribution

It has long been recognized that the choice of the proposal distribution is crucial to the rapid convergence of the Metropolis-Hastings algorithm. The most common case involves a symmetric random-walk Metropolis algorithm (RMW) in which the proposal is given by $\theta = \theta _ { o l d } + e$ , where the increment $e$ is follow some fixed symmetric distribution (e.g. $N ( 0 , \sigma ^ { 2 } \Sigma )$ with $\Sigma$ being a positive definite $d \times d$ matrix). In this case, the crucial issue is to how to properly scale the proposal (e.g., how to choose $\sigma$ ) for avoiding extreme cases that the chain moves too slowly or the proposal is usually be rejected. A simple way to avoid the extremes is to monitor the acceptance rate of the algorithm. In our case, by Theorem 2, the Bayesian PETEL posterior distribution can be well approximated by $N ( \hat { \theta } , \frac { 1 } { n } \mathcal { H } _ { \theta ^ { * } } \Delta _ { \theta ^ { * } } ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } )$ , so a reasonable choice of $\sigma$ would be $\sigma \asymp n ^ { - \frac { 1 } { 2 } }$ and we could start with $\sigma = c n ^ { - \frac { 1 } { 2 } }$ with positive constant $c$ and adjust $c$ until the acceptance rate is close to 0.234 [Gelman et al., 1997]. Apart from guaranteeing the quick convergence of Metropolis-Hastings algorithm, choosing $\sigma \asymp n ^ { - \frac { 1 } { 2 } }$ can guarantee the rapid convergence of the Newton-Raphson algorithm for computing $\lambda ( \tilde { \theta } )$ if we choose the initial value of $\lambda$ in the Newton-Raphson algorithm at time $t$ to be the $\lambda$ value computed in the last step (i.e., $\lambda ( \theta ^ { t - 1 } ) ,$ ), and only one step update will give a estimate that at most $n ^ { - 1 }$ away from $\lambda ( { \dot { \theta } } )$ .

# A.4 Sampling from “model-averaged” Bayesian PETEL with sparse prior

A Metropolis–Hastings procedure can be used to sample from the “model-averaged” posterior under model uncertainty [Dellaportas et al., 2002]. Given the current value of a proposal $( S , \theta _ { S } )$ , a proposal $( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } )$ is generated from some proposal distribution $p _ { p r o p } ( \cdot | ( S , \theta _ { S } ) )$ , the proposal is accepted as the next observation of the chain with the conventional Metropolis–Hastings acceptance probability

$$
= \frac { q ( | S ^ { \prime } | ) \big ( | _ { S ^ { \prime } } ^ { d } | \big ) ^ { - 1 } \pi _ { S ^ { \prime } } ( \theta _ { S ^ { \prime } } ^ { \prime } ) \exp ( - \alpha _ { n , d } \mathcal { R } _ { n } ( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S ^ { \prime } } ^ { \prime } ; S ^ { \prime } ) p _ { p r o p } ( ( S , \theta _ { S } ) | ( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } ) ) } { q ( | S | ) \big ( | _ { S } ^ { d } | \big ) ^ { - 1 } \pi _ { S } ( \theta _ { S } ) \exp ( - \alpha _ { n , d } \mathcal { R } _ { n } ( S , \theta _ { S } ) ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; S ) p _ { p r o p } ( ( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } ) | ( S , \theta _ { S } ) ) } .
$$

In practice, the proposal is constructed as a proposal for model $S$ , followed by a proposal for model parameters $\theta _ { S }$ , i.e., $p _ { p r o p } ( ( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } ) | ( S , \theta _ { S } ) ) = p _ { p r o p } ( S ^ { \prime } | ( S , \theta _ { S } ) ) p _ { p r o p } ( \theta _ { S ^ { \prime } } ^ { \prime } | S ^ { \prime } , S , \theta _ { S } )$ [Dellaportas et al., 2002]. The independence sampler [Tierney, 1994] is a special case of this approach and is straightforward to implement. By independence sampler, we mean the Markov chains with proposal that is not allowed to depend on the previous states, i.e., $p _ { p r o p } ( ( S ^ { \prime } , \theta _ { S ^ { \prime } } ^ { \prime } ) | ( S , \theta _ { S } ) ) = p _ { p r o p } ( S ^ { \prime } ) p _ { p r o p } ( \theta _ { S ^ { \prime } } ^ { \prime } | S ^ { \prime } )$ . The independence sampler is closely related to the corresponding important sampling process and works best if the proposal $p _ { p r o p }$ is a reasonable approximation to the target posterior distribution [Dellaportas et al., 2002]. Therefore, we should choose $p _ { p r o p } ( S )$ such it will only give mass to models that correspond to small constrained minimal empirical risks (i.e., $\mathcal { R } _ { n } ( \widehat { \theta } _ { S } , 0 )$ where ${ \hat { \theta } } _ { S }$ is the constrained empirical risk minimizer on model $S$ ) while in the meantime do not have large complexities. One possible choice for the proposal of model $S$ could be $p _ { p r o p } ( S ^ { \prime } | ( S , \theta _ { S } ) ) = p _ { p r o p } ( S ^ { \prime } ) \propto$ $\mathrm { e x p } ( - \alpha _ { n , d } \mathcal { R } _ { n } ( \hat { \theta } _ { S ^ { \prime } } , 0 ) - \beta _ { n , d } | S ^ { \prime } | - \log \binom { d } { | S ^ { \prime } | } )$ . To alleviate the curse of dimensionality, one can first use (stochastic) local search algorithms [Bottolo and Richardson, 2010] to find the model $\tilde { S }$ that maximizes $\mathrm { e x p } ( - \alpha _ { n , d } \mathcal { R } _ { n } ( \boldsymbol { \hat { \theta } } _ { S } , 0 ) - \beta _ { n , d } \vert S \vert - \log \binom { d } { \vert S \vert } )$ and limit the model space to models that have bounded Hamming distances with $\tilde { S }$ . Moreover, Based on Theorem 4, the target posterior distribution could be approximated by a Gaussian distribution on the true model with mean $\hat { \theta } _ { S ^ { * } }$ and covariance matrix $\begin{array} { r } { \frac { 1 } { n } ( \mathcal { H } _ { \theta _ { S ^ { \ast } } ^ { \ast } } ^ { S ^ { \ast } } ) ^ { - 1 } \Delta _ { \theta _ { S ^ { \ast } } ^ { \ast } } ^ { S ^ { \ast } } ( \mathcal { H } _ { \theta _ { S ^ { \ast } } ^ { \ast } } ^ { S ^ { \ast } } ) ^ { - 1 } } \end{array}$ , so when the loss function is twice-differentiable w.r.t to $\theta$ , we could use the empirical counterpart $( \hat { H } _ { \theta _ { S ^ { * } } } ^ { S ^ { * } } , \hat { \Delta } _ { \theta _ { S ^ { * } } } ^ { S ^ { * } } )$ of $( \mathcal { H } _ { \theta _ { S ^ { * } } } ^ { S ^ { * } } , \Delta _ { \theta _ { S ^ { * } } } ^ { S ^ { * } } )$ evaluated at $\hat { \theta } _ { S ^ { * } }$ in place of $\mathcal { H } _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } }$ and $\Delta _ { \theta _ { S ^ { * } } ^ { * } } ^ { S ^ { * } }$ . Thus the proposal distribution of $\theta _ { S }$ given $S$ could be chosen as $N ( \hat { \theta } _ { S } , n ^ { - 1 } ( \hat { H } _ { \hat { \theta } _ { S } } ^ { S } ) ^ { - 1 } \tilde { \hat { \Delta } } _ { \hat { \theta } _ { S } } ^ { S } ( \hat { H } _ { \hat { \theta } _ { S } } ^ { S } ) ^ { - 1 } )$ . For the non-smooth loss function, the strategy for estimating the covariance matrix of the Gaussian limiting distribution of Bayesian PETEL posterior with smooth loss function may not apply, as the empirical risk function in general dos not admit a Hessian matrix. While if we can find a twice differentiable function $\ell _ { \epsilon }$ such that $\begin{array} { r } { \operatorname* { l i m } _ { \epsilon \to 0 } \operatorname* { l i m } _ { n \to \infty } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname { H e s s } _ { \theta } \ell _ { \epsilon } ( X _ { i } , \theta ) = } \end{array}$ $\operatorname { H e s s } _ { \theta } \mathbb { E } \ell ( \theta )$ , then we can estimate the Hessian of the risk function by the Hessian of $\textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \ell _ { \epsilon } ( X _ { i } , \theta )$ where $\epsilon$ can decrease with $n$ at suitable rate. For example, for the hinge loss $\ell ( ( \tilde { X } , Y ) , \theta ) = \operatorname* { m a x } ( 0 , 1 - Y \theta ^ { T } \tilde { X } )$ , by equation (1.7) of Hajewski et al. [2018], we can choose $\ell _ { \epsilon } ( ( \tilde { X } , Y ) , \theta ) = \frac { 1 } { 2 } ( u + \sqrt { \epsilon ^ { 2 } + u ^ { 2 } } )$ where $u = 1 - Y \theta ^ { T } \tilde { X }$ . Similarly for the loss function in quantile regression $\ell ( ( \tilde { X } , Y ) , \theta ) = \tau ( Y - \tilde { X } ^ { T } \theta ) + \operatorname* { m a x } ( 0 , \tilde { X } ^ { T } \theta - Y )$ , we can choose $\ell _ { \epsilon } ( ( \tilde { X } , Y ) , \theta ) = - \tau u + { \textstyle \frac { 1 } { 2 } } ( u + \sqrt { \epsilon ^ { 2 } + u ^ { 2 } } )$ where $u = \tilde { X } ^ { T } \theta - Y$ .

# A.5 Additional Plots

Diagnostic Plots on MCMC Convergence We provide the Gelman–Rubin plots mentioned in Section 5.2. The Gelman–Rubin diagnostic evaluates MCMC convergence by analyzing the difference between multiple Markov chains. The convergence is assessed by checking whether the 50% and $9 7 . 5 \%$ quantiles of the sampling distribution of the Markov chain for the shrink factor (the estimated potential scale reduction) is close to 1. Plots showing the evolution of Gelman and Rubin’s shrink factor as the number of iterations increases for the SVMH, SVMSH and high dimensional quantile regression described in Section 5.2 are presented in Figure 4.

![](images/1991dd84c8836bc8369c8c7863ac1ccdf76728e661596b56cbd73c8191663299.jpg)  
  
Figure 4: Gelman-Rubin diagnostic plots for each dimension of parameters (left: the first dimension; right: the second dimension) after 5000 iterations

![](images/204139d02e5398b74b9522265982b34b0c0add21cfb67bb45202c119fe9fbe7c.jpg)

(a) Marginal density plots of bootstrapping empirical risk minimizers solved by gradient descent algorithm.

![](images/99fbbdd12b04717973d69117aa5436eefb7485d25c1a9e11e52d508b9592cb80.jpg)

(b) Marginal density plots of posterior samples from Bayesian ETEL using RMW algorithm.

![](images/992fd2b8273a13b15feba2f13619de53d1d8072596e4ef7d61c6056ef1aa6fc2.jpg)  
(c) Marginal density plots of posterior samples from Bayesian PETEL using RMW algorithm with $\alpha _ { n } = 2 \sqrt { n }$ .   
Figure 5: Marginal density plots for each dimension of parameters (Bootstrap, Bayesian ETEL and Bayesian PETEL).

Plots of Robust regression for learning sigmoid unit We provide in Figure 5 the marginal density plots of each dimension of bootstrapping empirical risk minimizers and posterior samples from Bayesian ETEL and Bayesian PETEL for a single run. We can see that for the Bootstrap, the marginal density plots for the first and second dimensions of the bootstrapping empirical risk minimizers solved by gradient descent algorithm are right heavy-tailed; for the Bayesian ETEL, when the initial state is near $( - 3 , 4 , 2 )$ , then the samples generated in the Markov chain may all included in a small neighborhood of $( - 3 , 4 , 2 )$ ; while for the Bayesian PETEL, when we choose $\alpha _ { n } = n$ and the initial state to be $( - 3 , 4 , 2 )$ , the Markov chain converges to a neighborhood of $\theta ^ { * } = ( 1 , 2 , 3 )$ in less than 200 number of iterations. Then when we use the posterior mean of the previous Markov chain to be the new initial state and change $\alpha _ { n }$ to $2 \sqrt { n }$ , the samples generated in the new Markov chain are all around $\theta ^ { * }$ and the marginal density plots are all Gaussian-like.

# B Applications of our Theoretical Results

In this section, we will apply our theoretical results to two representative examples: quantile regression and soft-margin support vector machine.

# B.1 Example: Quantile Regression

In quantile regression, for fixed $\tau \in ( 0 , 1 )$ , the $\tau ^ { t h }$ quantile of the response $Y \in \mathbb { R }$ given the covariates $\dot { X } \in \mathbb { R } ^ { d }$ is modelled as

$$
Q _ { \tau } ( Y | \tilde { X } ) = \tilde { X } ^ { T } \theta ^ { * } .
$$

The main difficulty in putting the Bayesian framework to work for quantile regression is that no parametric likelihood is given in the model on $Q _ { \tau } ( Y | \tilde { X } )$ , which is essential to the validity of Bayesian inference. Several authors have attempted to use a misspecified asymmetric Laplace likelihood as a working likelihood in the Bayesian quantile regression framework [Yu and Moyeed, 2001, Sriram et al., 2013], which corresponds to a Gibbs posterior using the empirical risk function $\begin{array} { r l } & { \mathcal { R } _ { n } ( \theta ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( Y _ { i } - \tilde { X } _ { i } ^ { T } \theta ) ( \tau - \mathbf { 1 } ( Y _ { i } < \tilde { X } _ { i } ^ { T } \theta ) ) } \end{array}$ given data $\{ X _ { i } = ( \tilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ [Syring and Martin, 2018]. However, the inference derived from Gibbs posterior may be invalid as the generalized information equality [Chernozhukov and Hong, 2003] may not hold. Our method overcomes this issue by taking log ETEL into the Gibbs posterior framework, so the validity of inference is not affected by whether the generalized information equality holds or not. We consider $g ( X , \theta ) = ( \mathbf { 1 } ( Y < \tilde { X } ^ { T } \theta ) - \tau ) \tilde { X }$ with moment conditions $\mathbb { E } g ( X , \theta ) = 0$ and the loss function $\ell ( X , \theta ) = ( Y - \tilde { X } ^ { T } \theta ) ( \tau - \mathbf { 1 } ( Y < \tilde { X } ^ { T } \theta ) )$ in the Bayesian PETEL posterior distribution, where $X = ( \tilde { X } , Y )$ . In this case, Assumption B.1 and B.2 could be simplified to the following Assumption B.q.

Assumption B.q: (1) The support of data $\dot { X }$ and $Y$ , denoted by $\ddot { \mathcal { X } }$ and $\mathcal { V }$ respectively, are bounded. (2) The conditional density of $Y$ given $\tilde { X }$ : $p ( t | \tilde { X } )$ is bounded and has bounded derivatives with respect to $t$ over $t \in \mathbb R$ and $\tilde { X } \in \tilde { \mathcal { X } }$ .

Corollary 2. Consider loss function $\ell ( X , \theta )$ and $g ( X , \theta )$ defined in the above Quantile regression example, under Assumption B.q, Assumption $A . 2$ and Assumption A.3, there exists some constants $\left( c , c _ { 1 } , c _ { 2 } \right)$ independent of $n$ , such that when $c _ { 1 } \log n \leq \alpha _ { n } \leq c _ { 2 } { \sqrt { n \log n } }$ , it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n } } }$ that,

$$
T V \big ( \pi _ { \mathrm { P E } } ( \cdot \mid X ^ { n } ) , N ( \theta ^ { * } - n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) , n ^ { - 1 } V _ { \theta ^ { * } } ) \big ) \leq c \frac { ( \log n ) ^ { \frac { 5 } { 4 } } } { n ^ { \frac { 1 } { 4 } } } ,
$$

where $\pi _ { \mathrm { P E } } ( \cdot | X ^ { n } )$ is the Bayesian PETEL posterior distribution and $V _ { \theta ^ { * } } = \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$ .

The convergence rate in Corollary 2 is slower than the case of smooth loss functions, for the reason that $g ( X , \theta )$ involves indicators and Assumption B.2 holds with $\beta = \textstyle { \frac { 1 } { 2 } }$ . Asymptotically, Corollary 2 justifies the validity of the inference derived from the Bayesian PETEL approach in a frequentist sense, which is a property that is not shared by all working likelihoods. Indeed, when the $\tau$ th quantile of $Y$ given $\tilde { X }$ is equal to $\tilde { X } ^ { T } \theta ^ { \ast }$ , by simple computation, we can get $\mathcal { H } _ { \boldsymbol { \theta } ^ { * } } = \mathbb { E } ( p ( \tilde { X } ^ { T } \theta ^ { * } | \tilde { X } ) \tilde { X } \tilde { X } ^ { T } )$ and $\Delta _ { \theta ^ { * } } = \mathbb { E } ( ( \tau - 1 ( Y <$ $\begin{array} { r } { \tilde { X } ^ { T } \theta ^ { * } ) ) ^ { 2 } \tilde { X } \tilde { X } ^ { T } ) = ( \tau - \tau ^ { 2 } ) \mathbb { E } \tilde { X } \tilde { X } ^ { T } } \end{array}$ . So the generalized information equality holds when $p ( \tilde { X } ^ { T } \theta ^ { * } | \tilde { X } )$ is constant for all $\tilde { X } \in \tilde { \mathcal { X } }$ (e.g., homoscedastic error models), while there is no guarantee of the validity of the inference derived from misspecified asymmetric Laplace likelihood or calibrated Gibbs posterior when the homoscedasticity assumption is invalid. Conversely, our method is insusceptible to model misspecification biases.

# B.2 Example: Soft-Margin Support Vector Machine

The soft-margin SVM [Duda et al., 2012] minimizes $\begin{array} { r } { \mathcal { R } _ { n } ( \theta ) = \frac { 1 } { 2 } \lambda \| \theta \| _ { 2 } ^ { 2 } + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname* { m a x } ( 0 , 1 - } \end{array}$ $Y _ { i } \theta ^ { T } \tilde { X } _ { i } )$ over $\theta \in \mathbb { R } ^ { d }$ given data $\{ X _ { i } = ( \tilde { X } _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ and $Y _ { i } = \pm 1$ . The value of $\lambda > 0$ controls the $\ell _ { 2 }$ norm of $\theta$ and the function $\operatorname* { m a x } ( 0 , 1 - y \theta ^ { I ^ { \prime } } \tilde { x } )$ is called the hinge-loss function. Polson and Scott [2011], Syring and Martin [2018] proposed to taking a pseudo-likelihood $\exp ( - \alpha n \mathcal { R } _ { n } ( \theta ) )$ with a learning rate $\alpha$ into a Bayesian framework, while there is no reason that posterior credible regions derived from it will be calibrated even though the learning rate is tuned to be the optimal, as the generalized information equality is generally not guaranteed. In our method, we consider $g ( X , \theta ) = \lambda \theta - Y \mathbf { 1 } ( Y \theta ^ { T } \tilde { X } \le 1 ) \tilde { X }$ with moment conditions $\mathbb { E } g ( X , \theta ) = 0$ and the loss function $\begin{array} { r } { \ell ( X , \theta ) = \frac { 1 } { 2 } \lambda \| \theta \| _ { 2 } ^ { 2 } + \operatorname* { m a x } ( 0 , 1 - Y \theta ^ { T } \tilde { X } ) } \end{array}$ in the Bayesian PETEL posterior distribution, where $X = ( \tilde { X } , Y )$ . In this case, Assumption B.1 and B.2 could be simplified to the following Assumption B.s.

Assumption B.s: (1) The support of covariant $\tilde { X }$ , denoted by $\tilde { \mathcal X }$ , is bounded. (2) There exist some positive constants $( c _ { 1 } , c _ { 2 } )$ such that the parameter space $\Theta \subseteq \{ \theta \in \mathbb { R } ^ { d } , c _ { 1 } \leq$ $\left| \theta _ { i } \right| \leq c _ { 2 } \left( 1 \leq i \leq d \right) \}$ . (3) Let $p _ { 1 } ^ { j } ( \tilde { X } _ { j } )$ and $p _ { - 1 } ^ { j } ( \dot { X } _ { j } )$ denotes the conditional density of $\dot { X _ { j } }$ given ${ \tilde { X } } _ { - j }$ and $Y = \pm 1$ respectively, where ${ \tilde { X } } _ { j }$ denotes the $j$ th dimension of $\tilde { X }$ and ${ \tilde { X } } _ { - j }$ denotes the element of $\tilde { X }$ except for $\tilde { X _ { j } }$ . Let $\tilde { \mathcal { X } } _ { - j }$ denote the support of ${ \tilde { X } } _ { - j }$ , $\{ p _ { 1 } ^ { j } ( \tilde { X } _ { j } ) \} _ { j = 1 } ^ { d }$ and $\{ p _ { - 1 } ^ { j } ( \tilde { X } _ { j } ) \} _ { j = 1 } ^ { d }$ are bounded and have bounded first order derivatives with respect to ${ \tilde { X } } _ { j }$ over $\tilde { X } _ { j } \in \mathbb { R }$ and $\tilde { X } _ { - j } \in \tilde { \mathcal { X } } _ { - j }$ .

Corollary 3. Under Assumption B.s, Assumption A.2’ and Assumption A.3, there exists some constants $( c , c _ { 1 } , c _ { 2 } )$ independent of $n$ , such that when $c _ { 1 } \log n \leq \alpha _ { n } \leq c _ { 2 } { \sqrt { n \log n } }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that,

$$
T V \big ( \pi _ { \mathrm { P E } } ( \cdot \mid X ^ { n } ) , \ : N ( \theta ^ { * } - n ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) , n ^ { - 1 } V _ { \theta ^ { * } } ) \big ) \leq c \frac { ( \log n ) ^ { \frac { 5 } { 4 } } } { n ^ { \frac { 1 } { 4 } } } ,
$$

where $\pi _ { \mathrm { P E } } ( \cdot | X ^ { n } )$ is the Bayesian PETEL posterior distribution and $V _ { \theta ^ { * } } = \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \Delta _ { \theta ^ { * } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 }$

Corollary 3 gives theoretical guarantee to the inference from our method for soft-margin SVM and in general, the calibrated Gibbs posterior would not work for this example. Indeed, it can be shown that $\Delta _ { \theta ^ { * } } = \mathbb { E } ( ( \lambda \theta ^ { * } - Y \mathbf { 1 } _ { Y { \theta ^ { * } } ^ { T } X \le 1 } \bar { X } ) ( \lambda \theta ^ { * } - Y \mathbf { 1 } _ { Y { \theta ^ { * } } ^ { T } X \le 1 } \bar { X } ) ^ { T } )$ ), while the diagonal elements of $\mathcal { H } _ { \theta ^ { \ast } }$ are $\begin{array} { r l } { \lambda + \mathbb { E } ( ( 1 - Y \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) ^ { 2 } p _ { Y } ^ { i } ( ( Y - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) / \theta _ { i } ) / | \theta _ { i } | ^ { 3 } ) } & { { } } \end{array}$ with $1 \leq i \leq d$ respectively. So generally, adjusting the learning rate of Gibbs posterior couldn’t exactly correct for the covariance matrix mismatching.

# C Proof of Main results

# C.1 Proof of Theorem 1

Let $\nabla _ { \theta } \ell ( X , \theta ) = g ( x , \theta )$ and $\begin{array} { r } { L ( X ^ { n } ; \theta ) = \prod _ { i = 1 } ^ { n } p _ { i } ( \theta ) } \end{array}$ . We begin the proof of Theorem 1 with the following lemmas.

Lemma 1. Under Assumption A.1 and A.2 , for any $\tilde { \theta } \in \Theta$ such that $\nabla _ { \theta } R ( { \tilde { \theta } } ) = 0$ , if the prior $\pi ( \theta )$ has support $B _ { r } ( { \tilde { \theta } } )$ and there exist some positive constants $( c , L )$ such that $\pi ( { \tilde { \theta } } ) \geq c$ and for any $\theta \in B _ { r } ( \tilde { \theta } )$ , it holds that $| \pi ( \theta ) - \pi ( { \tilde { \theta } } ) | \leq L \| \theta - { \tilde { \theta } } \| _ { 2 }$ , $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \theta } \succcurlyeq c I _ { d }$ and $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \tilde { \theta } } ^ { - 1 } \succcurlyeq c I _ { d }$ . Then there exist some constants $\left( { { c _ { 1 } } , { c _ { 2 } } , { c _ { 3 } } } \right)$ independent of $n$ , so that it holds with probability at least $\textstyle 1 - { \frac { c _ { 3 } } { n ^ { 2 } } }$ that,

1. $\nabla \mathcal { R } _ { n } ( \theta ) = 0$ has unique solution $\hat { \theta }$ on $B _ { r } ( { \tilde { \theta } } )$ and $\begin{array} { r } { \| \hat { \theta } - \tilde { \theta } \| \leq c _ { 1 } \sqrt { \frac { \log n } { n } } } \end{array}$

$$
\begin{array} { r } { ? \cdot \displaystyle \int \Biggl | \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } \right) - \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \Biggr | d h \leq c _ { 2 } \sqrt { \frac { \log n } { n } } . } \end{array}
$$

Lemma 2. Under Assumption A.1, A.2 and A.3, let $A = \Sigma _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } )$ , if there exists $a$ positive constant c such that for any $\theta \in A ^ { c }$ , $\Vert \nabla _ { \theta } \mathcal { R } ( \theta ) \Vert _ { 2 } \geq c$ , then there exist constants $( c _ { 1 } , c _ { 2 } )$ so that it holds with probability at least $\textstyle 1 - { \frac { c _ { 2 } } { n ^ { 2 } } }$ that $\Pi _ { \mathrm { E } } ( \theta \in A ^ { c } \vert X ^ { n } ) \leq \exp ( - c _ { 1 } n ^ { \frac { 1 } { 3 } } )$

By Assumption A.1 and A.2, there exists a small enough positive constant $r$ such that for any $1 \leq k \leq K$ and $\theta \in B _ { r } ( \tilde { \theta } _ { k } )$ , it holds that $\begin{array} { r } { \mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \theta } \succcurlyeq \frac { b } { 2 } I _ { d } } \end{array}$ and $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \tilde { \theta } _ { k } } ^ { - 1 } \succcurlyeq \frac { 1 } { 2 } I _ { d }$ . Also, for any $1 \le k , k ^ { \prime } \le K$ and $k \neq k ^ { \prime }$ , $B _ { r } ( { \tilde { \theta } } _ { k } ) \cap B _ { r } ( { \tilde { \theta } } _ { k ^ { \prime } } ) = \varnothing$ . Moreover, by the assumption that the equation $\nabla \mathcal { R } ( \theta ) = 0$ has exact $K$ number of isolated solutions, there exists a positive constant $c$ such that for any $\theta \in \{ \Sigma _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } ) \} ^ { c }$ , $\Vert \nabla _ { \theta } \mathcal { R } ( \theta ) \Vert _ { 2 } \geq c$ . Denote the posterior distribution of $\theta$ constrained on $B _ { r } ( \tilde { \theta } _ { k } )$ by $\pi _ { k } ( \theta | X ^ { n } )$ , then

$$
\pi _ { k } ( \theta | X ^ { n } ) = \frac { \pi _ { k } ( \theta ) L ( X ^ { n } ; \theta ) } { \int _ { B _ { r } ( \tilde { \theta } _ { k } ) } \pi ( \theta ) L ( X ^ { n } ; \theta ) d \theta } ,
$$

where $\pi _ { k } ( \theta ) = \pi ( \theta ) \mathbf { 1 } _ { B _ { r } ( \tilde { \theta } _ { k } ) }$ . Let $\widehat { \theta } _ { k }$ be the solution of $\nabla _ { \boldsymbol { \theta } } \mathcal { R } _ { n } ( \boldsymbol { \theta } ) = 0$ on $B _ { r } ( { \tilde { \theta } } )$ , then by Lemma $1$ , it holds with probability at least $\textstyle { 1 - { \frac { c _ { 3 } K } { n ^ { 2 } } } }$ that for any $1 \leq k \leq K$ ,

$$
\left( \pi _ { k } ( \hat { \theta } _ { k } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } _ { k } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } _ { k } ) } \right) - \pi ( \hat { \theta } _ { k } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } _ { k } } ^ { - 1 } h } { 2 } \right) \right) d h \Bigg | \lesssim \sqrt { \frac { \log ( \sqrt { n } ) } { \sqrt { n } } } .
$$

So combined with Lemma 1 and the shift and scale invariance of the total variation distance, we have

$$
d _ { \mathrm { T V } } ( \pi _ { k } ( \theta | X ^ { n } ) , N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \tilde { \theta } _ { k } } ) ) \leq c _ { 2 } \sqrt { \frac { \log n } { n } } .
$$

We then compute $\Pi _ { \mathrm { E } } ( \theta \in B _ { r } ( \tilde { \theta } _ { k } ) | X ^ { n } )$ .

$$
\Pi _ { \mathrm { E } } ( \theta \in B _ { r } ( \tilde { \theta } _ { k } ) | X ^ { n } ) = \frac { n ^ { \frac { d } { 2 } } \int _ { \theta \in B _ { r } ( \tilde { \theta } _ { k } ) } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { \left( \frac { 1 } { n } \right) ^ { n } } \right) d \theta } { n ^ { \frac { d } { 2 } } \int _ { \Sigma _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } ) } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { \left( \frac { 1 } { n } \right) ^ { n } } \right) d \theta } \cdot \Pi _ { \mathrm { E } } ( \theta \in \Sigma _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } ) | X ^ { n } ) .
$$

Then by Lemma $^ { 1 }$ , it holds with probability at least $\textstyle { 1 - { \frac { c _ { 3 } K } { n ^ { 2 } } } }$ that for any $1 \leq k \leq K$ , $\begin{array} { r } { \| \tilde { \theta } _ { k } - \hat { \theta } _ { k } \| _ { 2 } \leq c _ { 1 } \sqrt { \frac { \log n } { n } } } \end{array}$ . Then there exist some constant $( c _ { 4 } , c _ { 5 } )$ such that

$$
\begin{array} { r l } & { \displaystyle \int _ { \| h \| _ { 2 } \leq c \mathsf { a } \sqrt n } \pi _ { k } ( \widehat { \theta } _ { k } + \frac { h } { \sqrt n } ) \exp \left( \log \frac { L ( X ^ { n } ; \widehat { \theta } _ { k } + h / \sqrt n ) } { L ( X ^ { n } ; \widehat { \theta } _ { k } ) } \right) d h } \\ & { \displaystyle \leq ( \sqrt n ) ^ { d } \int _ { \theta \in B _ { r } ( \widehat { \theta } _ { k } ) } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { \left( \frac n { n } \right) ^ { n } } \right) d \theta } \\ & { \displaystyle \leq \int _ { \| h \| _ { 2 } \leq c _ { 5 } \sqrt n } \pi _ { k } ( \widehat { \theta } _ { k } + \frac { h } { \sqrt n } ) \exp \left( \log \frac { L ( X ^ { n } ; \widehat { \theta } _ { k } + h / \sqrt n ) } { L ( X ^ { n } ; \widehat { \theta } _ { k } ) } \right) d h . } \end{array}
$$

Then, by Lemma 1 and Lemma 2, it holds with probability at least $\textstyle 1 - { \frac { c _ { 3 } K } { n ^ { 2 } } }$ that for any

1 ≤ k ≤ K ,

$$
\begin{array} { r l } & { \displaystyle \left| ( \sqrt { n } ) ^ { d } \int _ { \theta \in B _ { r } ( \tilde { \theta } _ { k } ) } \pi ( \theta ) \exp \left( \log \frac { L \left( X ^ { n } ; \theta \right) } { \left( \frac { 1 } { n } \right) ^ { n } } \right) d \theta - \pi ( \tilde { \theta } _ { k } ) ( 2 \pi ) ^ { \frac { d } { 2 } } | V _ { \tilde { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } \right| \lesssim \sqrt { \frac { \log n } { n } } , } \\ & { \displaystyle \left| ( \sqrt { n } ) ^ { d } \int _ { \theta \in \sum _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } ) } \pi ( \theta ) \exp \left( \log \frac { L \left( X ^ { n } ; \theta \right) } { \left( \frac { 1 } { n } \right) ^ { n } } \right) d \theta - \sum _ { k = 1 } ^ { K } \pi ( \tilde { \theta } _ { k } ) ( 2 \pi ) ^ { \frac { d } { 2 } } | V _ { \tilde { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } \right| \lesssim \sqrt { \frac { \log n } { n } } } \\ & { \displaystyle \left| \Pi _ { \mathbb { E } } ( \theta \in B _ { r } ( \tilde { \theta } _ { k } ) | X ^ { n } ) - \frac { \pi ( \tilde { \theta } _ { k } ) | V _ { \tilde { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } } { \sum _ { k = 1 } ^ { K } \pi ( \tilde { \theta } _ { k } ) | V _ { \tilde { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } } \right| \lesssim \sqrt { \frac { \log n } { n } } . } \end{array}
$$

Let $\begin{array} { r } { A = \sum _ { k = 1 } ^ { K } B _ { r } ( \tilde { \theta } _ { k } ) } \end{array}$ , for any measurable set $A ^ { \prime } \subseteq \mathbb { R } ^ { d }$ , $A ^ { \prime }$ can written as

$$
A ^ { \prime } = A ^ { \prime } \cap A + A ^ { \prime } \cap A ^ { c } .
$$

So,

$$
\Pi _ { \mathrm { E } } ( \theta \in A ^ { \prime } | X ^ { n } ) = \Pi _ { \mathrm { E } } ( \theta \in A ^ { \prime } \cap A ^ { c } | X ^ { n } ) + \sum _ { k = 1 } ^ { K } \Pi _ { \mathrm { E } } ( \theta \in A ^ { \prime } \cap B _ { r } ( { \tilde { \theta } } _ { k } ) | X ^ { n } )
$$

$$
0 \leq \Pi _ { \operatorname { E } } ( \theta \in A ^ { \prime } \cap A ^ { c } | X ^ { n } ) \leq \Pi _ { \operatorname { E } } ( \theta \in A ^ { c } | X ^ { n } ) \leq \exp ( - c _ { 1 } n ^ { \frac 1 3 } ) .
$$

Then by equation (7) and equation (8), there exist positive constants $( c _ { 0 } , c _ { 1 } , c _ { 2 } )$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that for any $1 \leq k \leq K$ and $A ^ { \prime } \subseteq \mathbb { R } ^ { d }$ ,

$$
\begin{array} { r l } & { \left| \Pi _ { \mathrm { E } } ( \theta \in A ^ { \prime } \cap B _ { r } ( \widetilde { \theta } _ { k } ) | X ^ { n } ) - \widetilde { \pi } _ { k } \Pi _ { N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \bar { \theta } _ { k } } ) } ( \theta \in A ^ { \prime } \cap B _ { r } ( \widetilde { \theta } _ { k } ) ) \right| \lesssim \sqrt { \frac { \log n } { n } } } \\ & { \left| \widetilde { \pi } _ { k } \Pi _ { N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \bar { \theta } _ { k } } ) } ( \theta \in A ^ { \prime } \cap B _ { r } ( \widetilde { \theta } _ { k } ) ) - \Pi _ { \sum _ { k = 1 } ^ { K } \widetilde { \pi } _ { k } N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \bar { \theta } _ { k } } ) } ( \theta \in A ^ { \prime } \cap B _ { r } ( \widetilde { \theta } _ { k } ) ) \right| \lesssim \exp ( - c _ { 1 } n \eta ( \theta ) ) } \\ & { \Pi _ { \sum _ { k = 1 } ^ { K } \widetilde { \pi } _ { k } N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \bar { \theta } _ { k } } ) } ( \theta \in A ^ { c } ) \leq \exp ( - c _ { 2 } n ) } \\ & { \widetilde { \pi } _ { k } = \frac { \pi ( \widetilde { \theta } _ { k } ) | V _ { \bar { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } } { \sum _ { k = 1 } ^ { K } \pi ( \widetilde { \theta } _ { k } ) | V _ { \bar { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } } } \end{array}
$$

Take supreme over $A ^ { \prime }$ , we can get with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ ,

$$
T V \left( \pi _ { \mathrm { E } } ( \theta | X ^ { n } ) , \sum _ { k = 1 } ^ { K } \frac { \pi ( \tilde { \theta } _ { k } ) | V _ { \tilde { \theta } _ { k } } | ^ { \frac { 1 } { 2 } } } { \sum _ { i = 1 } ^ { K } \pi ( \tilde { \theta } _ { i } ) | V _ { \tilde { \theta } _ { i } } | ^ { \frac { 1 } { 2 } } } N ( \hat { \theta } _ { k } , \frac { 1 } { n } V _ { \tilde { \theta } _ { k } } ) \right) \lesssim \sqrt { \frac { \log n } { n } } .
$$

Moreover, by Lemma $1$ and $0 = \nabla \mathcal { R } _ { n } ( \tilde { \theta } _ { k } ) + \mathcal { H } _ { \tilde { \theta } _ { k } } ^ { n } ( \hat { \theta } _ { k } - \tilde { \theta } _ { k } ) + O ( \| \tilde { \theta } _ { k } - \hat { \theta } _ { k } \| _ { 2 } ^ { 3 } )$ , we can get that $\begin{array} { r } { \lVert \sqrt { n } ( \hat { { \boldsymbol \theta } } _ { k } - \tilde { { \boldsymbol \theta } } _ { k } ) + \mathcal { H } _ { \tilde { { \boldsymbol \theta } } _ { k } } ^ { - 1 } \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \tilde { { \boldsymbol \theta } } _ { k } ) \rVert _ { 2 } = o _ { p } ( 1 ) } \end{array}$ , then the statement that $\sqrt { n } (  { \hat { \theta } } _ { k } -  { \tilde { \theta } } _ { k } )$ converges to $N ( 0 , V _ { \tilde { \theta } _ { k } } )$ in distribution is followed from standard Central limit theorem and Slutsky’s theorem.

# C.1.1 Proof of Lemma 1

Let $\mathcal { H } _ { \theta } ^ { n }$ be the Hessian matrix of $\mathcal { R } _ { n } ( \theta )$ . By Assumption A.1, we can get for any $\theta , \theta ^ { \prime } \in \Theta$ and $1 \leq j , k \leq d$ ,

$$
\begin{array} { r l r } {  { \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \frac { \partial \ell ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ) } { \partial \theta _ { j } } - \frac { \partial \ell ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ^ { \prime } ) } { \partial \theta _ { j } ^ { \prime } } ) ^ { 2 } } \lesssim \| \boldsymbol { \theta } - \boldsymbol { \theta } ^ { \prime } \| _ { 2 } } } \\ & { } & { \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \frac { \partial ^ { 2 } \ell ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ) } { \partial \theta _ { j } \partial \theta _ { k } } - \frac { \partial ^ { 2 } \ell ( \boldsymbol { X } _ { i } , \boldsymbol { \theta } ^ { \prime } ) } { \partial \theta _ { j } ^ { \prime } \partial \theta _ { k } ^ { \prime } } ) ^ { 2 } } \lesssim \| \boldsymbol { \theta } - \boldsymbol { \theta } ^ { \prime } \| _ { 2 } . } \end{array}
$$

Since $\Theta$ is compact, w.l.o.g, we can assume $\Theta = B _ { 1 } ( \mathbf { 0 } _ { d } )$ . Then by standard symmetrization (see for example, 8.3.24 of [Vershynin, 2018]) and Dudley’s inequality (see for example, 8.1.3 of [Vershynin, 2018]), we can get for any $1 \leq j , k \leq d$ ,

$$
\begin{array} { r l } & { \mathbb { E } \underset { \theta \in \Theta } { \operatorname* { s u p } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \frac { \partial \ell ( X _ { i } , \theta ) } { \partial \theta _ { j } } - \mathbb { E } \frac { \partial \ell ( X , \theta ) } { \partial \theta _ { j } } \right| + \mathbb { E } \underset { \theta \in \Theta } { \operatorname* { s u p } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \frac { \partial ^ { 2 } \ell ( X _ { i } , \theta ) } { \partial \theta _ { j } \partial \theta _ { k } } - \mathbb { E } \frac { \partial ^ { 2 } \ell ( X , \theta ) } { \partial \theta _ { j } \partial \theta _ { k } } \right| } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \int \sqrt { \log \mathcal { N } ( \Theta , \| \cdot \| _ { 2 } , \varepsilon ) } d \varepsilon , } \end{array}
$$

where $\mathcal { N } ( \Theta , \| \cdot \| _ { 2 } , \varepsilon )$ denotes the $\varepsilon$ -covering number of $\Theta$ with respect to $\ell _ { 2 }$ norm, which is upper bounded by $\left( \frac { 3 } { \varepsilon } \right) ^ { d }$ [Vershynin, 2018]. Then using Bernstein inequality [Wainwright, 2019], there exists a constant $c _ { 1 }$ , such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\operatorname* { s u p } _ { \theta \in \Theta } ( \| \nabla _ { \theta } \mathcal { R } ( \theta ) - \nabla _ { \theta } \mathcal { R } _ { n } ( \theta ) \| _ { 2 } + \| \mathcal { H } _ { \theta } - \mathcal { H } _ { \theta } ^ { n } \| _ { \mathrm { F } } ) \leq c _ { 1 } \sqrt { \frac { \log n } { n } }
$$

Then we have for any $\theta \in B _ { r } ( \tilde { \theta } )$ , $\begin{array} { r } { \mathcal { H } _ { \theta } ^ { n } \mathcal { H } _ { \theta } ^ { n } \succcurlyeq \frac { b } { 4 } I _ { d } \left( b > 0 \right) } \end{array}$ and $\begin{array} { r } { \| \nabla \mathcal { R } _ { n } ( \tilde { \theta } ) \| \leq c _ { 1 } \sqrt { \frac { \log n } { n } } } \end{array}$ log n . Let $\theta ^ { 0 } = \widetilde { \theta }$ , and for $k = 1 , 2 , \cdots$ , we recurring define $\theta ^ { k } = \theta ^ { k - 1 } - ( \mathcal { H } _ { \theta ^ { k - 1 } } ^ { n } ) ^ { - 1 } \nabla _ { \theta } \mathcal { R } _ { n } ( \theta ^ { k - 1 } ) .$ . Then with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ , for any $k \geq 1$ , it holds that $\begin{array} { r } { \| \theta ^ { k } - \theta ^ { k - 1 } \| _ { 2 } \lesssim ( \frac { \log n } { n } ) ^ { 2 ^ { k - 2 } } } \end{array}$ and k∇θRn(θk)k2 . ( log nn )2k−1 , so we can define ${ \hat { \theta } } = \operatorname* { l i m } _ { k \to + \infty } \theta ^ { k }$ and we have $\nabla \mathcal { R } _ { n } ( { \hat { \theta } } ) = 0$ and ${ \hat { \theta } } \in B _ { r } ( { \tilde { \theta } } )$ . We now prove the uniqueness of the solution of $\nabla \mathcal { R } _ { n } ( \theta ) = 0$ on $B _ { r } ( { \tilde { \theta } } )$ in the following lemma.

Lemma 3. Under Assumption A.1 and A.2 , for any $\tilde { \theta } \in \Theta$ such that $\nabla _ { \theta } R ( \tilde { \theta } ) = 0$ , if there exist some positive constants $( r , c )$ such that for any $\theta \in B _ { r } ( \tilde { \theta } )$ , it holds that $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \theta } \succcurlyeq c I _ { d }$ and $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \tilde { \theta } } ^ { - 1 } \succcurlyeq c I _ { d }$ . There exists a positive constant $c _ { 0 }$ , such that

1. For any $\begin{array} { r } { \mathrm { ~  ~ \gamma ~ } \in { B _ { r } ( \tilde { \theta } ) } , \| \nabla _ { \theta } \mathcal { R } ( \theta ) \| _ { 2 } \geq c _ { 0 } \| \theta - \tilde { \theta } \| _ { 2 } . } \end{array}$

2. It holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $\theta \in B _ { r } ( \tilde { \theta } )$ , $\Vert \nabla _ { \theta } \mathcal { R } _ { n } ( \theta ) \Vert _ { 2 } \ \geq$ $c _ { 0 } \lVert \theta - { \hat { \theta } } \rVert _ { 2 }$ .

So, by Lemma 3, we could get the conclusion of the first statement.

For the second statement, since

$$
\pi _ { \mathrm { E } } ( \sqrt { n } ( \theta - \hat { \theta } ) | X ^ { n } ) = \frac { \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } ) } { \int \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } ) d h } ,
$$

we then bound $\begin{array} { r } { \int \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } ) - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } ) \right| d h . } \end{array}$

Define the following set of $h$ ,

$$
\begin{array} { r l } & { A _ { 1 } = \left\{ \| h \| _ { 2 } \leq \delta _ { 1 } \sqrt { \log n } \right\} , } \\ & { A _ { 2 } = \left\{ \delta _ { 1 } \sqrt { \log n } \leq \| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} , } \\ & { A _ { 3 } = \left\{ \| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} . } \end{array}
$$

Step 1: Consider $A _ { 3 }$ . let $\theta ^ { \prime } = { \hat { \theta } } + { \frac { h } { \sqrt { n } } }$ , where $\theta ^ { \prime } \in B _ { r } ( \tilde { \theta } )$ , then by Lemma 3, with probability at least 1 − 1n2 , kθ0 − ˜θk ≥ δ22 (log n)1.5√n .

$$
\begin{array} { l } { \log \displaystyle \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } = \displaystyle \sum _ { i = 1 } ^ { n } \log p _ { i } ( \theta ^ { \prime } ) - n ( \log \frac { 1 } { n } ) } \\ { \displaystyle \sum _ { i = 1 } ^ { n } p _ { i } ( \theta ^ { \prime } ) g ( X _ { i } , \theta ^ { \prime } ) = 0 . } \end{array}
$$

So,

$$
\sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ^ { \prime } ) - \frac { 1 } { n } \right) g ( X _ { i } , \theta ^ { \prime } ) = \nabla \mathcal { R } _ { n } ( \theta ^ { \prime } ) .
$$

By Lemma 3, there exists a positive constant $c$ such that it holds with probability at least 1 − 1n2 that, k∇θR(θ0)k2 ≥ cδ22 (log n)1.5√n and k∇θRn(θ0)k2 ≥ cδ2 (log n)1.5√ . So,

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ^ { \prime } ) - \frac 1 n \right) ^ { 2 } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) \| _ { 2 } ^ { 2 } \geq \frac { c ^ { 2 } \delta _ { 2 } ^ { 2 } } { 1 6 } \frac { ( \log n ) ^ { 3 } } n } \\ { \displaystyle \sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ^ { \prime } ) - \frac 1 n \right) ^ { 2 } \geq c _ { 2 } \delta _ { 2 } ^ { 2 } \frac { ( \log n ) ^ { 3 } } { n ^ { 2 } } . } \end{array}
$$

Define $\begin{array} { r } { q ( p _ { 1 } , \cdots , p _ { n - 1 } ) = \sum _ { i = 1 } ^ { n - 1 } \log p _ { i } + \log ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) } \end{array}$ . The Hessian matrix of function $q$ at point $( p _ { 1 } , \cdots , p _ { n - 1 } )$ is

$$
\mathcal { H } _ { q } | _ { ( p _ { 1 } , \cdots , p _ { n - 1 } ) } = \mathrm { D i a g } ( - \frac { 1 } { p _ { 1 } ^ { 2 } } , \cdots , - \frac { 1 } { p _ { n - 1 } ^ { 2 } } ) - \frac { 1 } { ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) ^ { 2 } } \mathbf { 1 } _ { ( n - 1 ) \times ( n - 1 ) } ,
$$

where ${ \bf 1 } _ { ( n - 1 ) \times ( n - 1 ) }$ denotes the $( n - 1 ) \times ( n - 1 )$ matrix with all entries being 1. Let $p = ( p _ { 1 } , \cdots , p _ { n } )$ and $p _ { - n } = ( p _ { 1 } , \cdot \cdot \cdot , p _ { n - 1 } )$ . If $\| p \| _ { \infty } \geq 2 d { \frac { \log n } { n } }$ , then

$$
\sum _ { i = 1 } ^ { n } \log p _ { i } \leq \log { \frac { 2 d \log n } { n } } + ( n - 1 ) \log { \frac { 1 - 2 d { \frac { \log n } { n } } } { n - 1 } } .
$$

So,

$$
\begin{array} { c l l } { - n \log n - \displaystyle \sum _ { i = 1 } ^ { n } \log p _ { i } \geq - \log ( 2 d \log n ) - ( n - 1 ) \log \left( ( 1 - 2 d \frac { \log n } { n } ) \frac { n } { n - 1 } \right) } \\ { \geq d \log n . } \end{array}
$$

If $\| p \| _ { \infty } \leq 2 d { \frac { \log n } { n } }$ , then when $\delta _ { 2 }$ is large enough, we have $\begin{array} { r } { \sum _ { i = 1 } ^ { n - 1 } ( p _ { i } - \frac { 1 } { n } ) ^ { 2 } \geq \frac { 8 d ^ { 3 } ( \log n ) ^ { 3 } } { n ^ { 2 } } } \end{array}$ , so by mean value theorem,

$$
\begin{array} { r l } & { q ( \displaystyle \frac 1 n , \cdots , \frac 1 n ) - q ( p _ { - n } ) } \\ & { \ = - \displaystyle \frac 1 2 ( p _ { - n } - \frac 1 n \mathbf { 1 } _ { ( n - 1 ) } ) ^ { T } \mathcal { H } _ { q } \big \rvert _ { ( c p _ { - n } + ( 1 - c ) \frac 1 n \mathbf { 1 } _ { ( n - 1 ) } ) } \big ( p _ { - n } - \frac 1 n \mathbf { 1 } _ { ( n - 1 ) } \big ) } \\ & { \ \geq d \log n . } \end{array}
$$

So,

$$
\begin{array} { r l } & { \int _ { A _ { 3 } } \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } ) - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } ) \right| d h } \\ & { \leq \exp ( - d \log n ) ( \sqrt { n } ) ^ { d } + \int _ { A _ { 3 } } \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } ) d h } \\ & { \leq \frac { 1 } { \sqrt { n } } . } \end{array}
$$

Step 2: Consider $A _ { 1 }$ and $A _ { 2 }$ . let $\begin{array} { r } { \theta = \hat { \theta } + \frac { h } { \sqrt { n } } } \end{array}$ , we have with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ kθ − ˜θk2 ≤ 2δ2(log n)1.5√ .

Lemma 4. If (1) $\| g ( x , \theta ) \| _ { 2 }$ is uniformly bounded over $x \in \mathcal { X }$ and $\theta \in \Theta$ ; (2) each element of $\Delta _ { \theta }$ and $\mathbb { E } g ( X , \theta )$ are uniformly Lipschitz over a neighborhood of $\tilde { \theta }$ and $\Delta _ { \tilde { \theta } } \succcurlyeq a I _ { d }$ with $a$ positive constant $a$ ; (4) $\mathbb { E } g ( X , \tilde { \theta } ) = 0$ . Then there exist some positive constants $\left( \delta _ { 0 } , c _ { 2 } , c _ { 3 } \right)$ , such that

1. For any $\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \tilde { \theta } )$ , $\mathcal { P } ^ { * } ( \lambda ^ { T } g ( X , \theta ) \geq c _ { 2 } ) \geq c _ { 3 }$ , where recall that ${ \mathcal { P } } ^ { * }$ denotes the underlying data distribution.

2. If in addition each element of $g ( X , \theta )$ is uniformly Lipschitz with respect to $\theta$ over a neighborhood of $\tilde { \theta }$ and $X \in { \mathcal { X } }$ , then it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \tilde { \theta } )$ , it satisfies that $\begin{array} { r } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \pmb { I } _ { \lambda ^ { T } g ( X _ { i } , \theta ) \geq \frac { c _ { 2 } } { 2 } } \geq \frac { c _ { 3 } } { 2 } } \end{array}$ .

Since $\begin{array} { r } { \lambda ( \theta ) = \underset { \lambda \in \mathbb { R } ^ { d } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ^ { T } g ( X _ { i } , \theta ) ) } \end{array}$ . By Lemma 4, $\lambda ( \theta )$ exists and

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) = 0 \mathbf { 1 } _ { d } .
$$

Let $\begin{array} { r } { \tilde { \lambda } ( \theta ) = \frac { \lambda ( \theta ) } { \| \lambda ( \theta ) \| _ { 2 } } } \end{array}$

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( \| \lambda ( \theta ) \| _ { 2 } \tilde { \lambda } ( \theta ) ^ { T } g ( X _ { i } , \theta ) \Big ) \tilde { \lambda } ( \theta ) ^ { T } g ( X _ { i } , \theta ) = 0 .
$$

So, by Lemma 4, it holds with probability larger than $1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\begin{array} { r } { \theta \in \Bigl \{ \theta \ : \big | \ : \| \theta - \tilde { \theta } \| _ { 2 } \le \frac { 2 \delta _ { 2 } ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } \Bigr \} \frac { } { \sin \theta } , } \end{array}$

$$
\begin{array} { r l } & { \frac { 1 } { \alpha } \displaystyle \sum _ { \lambda \in \mathbb { P } _ { x } ^ { \varepsilon } \times \mathbb { R } _ { n } ^ { s } } \exp \left( \| \lambda ( \beta ) \| _ { 2 } \lambda ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) \right) \lambda ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) } \\ & { \le \frac { 1 } { \alpha } \displaystyle \sum _ { \lambda \in \mathbb { P } _ { x } ^ { \varepsilon } \times \mathbb { R } _ { n } ^ { s } \times \mathbb { P } _ { x } ^ { \varepsilon } } \exp \left( \| \lambda ( \dot { \theta } ) \| _ { 2 } \bar { \lambda } ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) \right) \bar { \lambda } ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) } \\ & { \quad - \frac { 1 } { \alpha } \displaystyle \sum _ { \lambda \in \mathbb { P } _ { x } ^ { \varepsilon } \times \mathbb { R } _ { n } ^ { s } \times \mathbb { P } _ { x } ^ { \varepsilon } } \exp \left( \| \lambda ( \dot { \theta } ) \| _ { 2 } \bar { \lambda } ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) \right) \bar { \lambda } ( \dot { \theta } ) ^ { T } g ( X _ { \ast } \theta ) } \\ & { \le \sqrt { \frac { 1 } { \alpha } \displaystyle \sum _ { \lambda \in \mathbb { P } _ { x } ^ { \varepsilon } \times \mathbb { P } _ { x } ^ { \varepsilon } } \| g ( X _ { \ast } \theta ) \| _ { 2 } ^ { 2 } } } \\ & { \le 2 \sqrt { \nu ( \Delta _ { \dot { \theta } } ) } . } \end{array}
$$

So we can get

$$
\begin{array} { r l } & { \sqrt [ 2 ] { t r ( \Delta _ { \tilde { \theta } } ) } \geq \frac { c _ { 2 } c _ { 3 } } { 4 } \exp ( \frac { c _ { 2 } } { 2 } \| \lambda ( \theta ) \| _ { 2 } ) } \\ & { \| { \lambda ( \theta ) } \| _ { 2 } \leq \frac { 2 \log \frac { 8 \sqrt { t r ( \Delta _ { \tilde { \theta } } ) } } { c _ { 2 } c _ { 3 } } } { c _ { 2 } } = \lambda _ { 0 } } \end{array}
$$

Lemma 5. Under Assumption $A . 1$ and A.2, for any $\tilde { \theta } \in \Theta$ such that $\nabla _ { \theta } R ( \tilde { \theta } ) = 0$ , there exist constants $\left( c _ { 5 } , c _ { 6 } \right)$ , such that it holds with probability larger than $\textstyle 1 - { \frac { c _ { 6 } } { n ^ { 2 } } }$ that for any θ ∈ nθ  kθ − ˜θk2 ≤ 2δ2(log n)1.5√n o , it holds that $\operatorname* { m a x } _ { 1 \leq i \leq d } \lVert \frac { \partial \lambda ( \theta ) } { \partial \theta _ { i } } \rVert _ { 2 } \leq c _ { 5 }$ and $\operatorname* { m a x } _ { 1 \leq i \leq d } \| \frac { \partial ^ { 2 } \lambda ( \theta ) } { \partial \theta _ { i } \partial \theta _ { j } } \| _ { 2 } \leq c _ { 5 }$ .

Since $\begin{array} { r } { \log L ( X ^ { n } ; \theta ) = - n \log n + \sum _ { i = 1 } ^ { n } \log \frac { \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) } } \end{array}$ . Let l(X, θ) = log exp(λ(θ) g(X,θ))1n Pni=1 exp(λ(θ)T g(Xi,θ)) , then

$$
\log \left( \frac { L ( X ^ { n } ; \hat { \theta } + \frac { h } { { \sqrt { n } } } ) } { L ( X ^ { n } ; \hat { \theta } ) } \right) = \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } + \frac { h } { { \sqrt { n } } } ) - \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } ) .
$$

$$
\| h \| \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } .
$$

Since $\begin{array} { r } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \widehat { \theta } ) = 0 } \end{array}$ and $\lambda ( { \hat { \theta } } ) = 0$ , let $l ^ { ( 1 ) } ( x , \theta )$ and ${ l ^ { ( 2 ) } ( x , \theta ) }$ denote the gradient and Hessian matrix of $l ( X , \theta )$ with respect to $\theta$ , we have $\textstyle \sum _ { i = 1 } ^ { n } l ^ { ( 1 ) } ( X _ { i } , { \hat { \theta } } ) = 0$ . Let $\begin{array} { r } { \theta _ { t } = \hat { \theta } + \frac { t h } { \sqrt { n } } } \end{array}$ with some $t \in [ 0 , 1 ]$ . Let $\tau _ { i } ( \theta ) = \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) )$ and $\begin{array} { r } { \tau _ { n } ( \theta ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \tau _ { i } ( \theta ) } \end{array}$ . Then, we have

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { \alpha } \sum _ { i = 1 } ^ { N } l ^ { ( 2 ) } ( X _ { i } , \theta _ { i } ) } \\ & { = \displaystyle \frac { 1 } { \alpha } \sum _ { i = 1 } ^ { N } \Big ( 1 - \frac { \tau _ { i } ( \theta _ { i } ) } { \tau _ { i } ( \theta _ { i } ) } \Big ) \Big ( \sum _ { j = 1 } ^ { N } \lambda _ { j } ( \theta _ { i } ) g _ { j } ^ { ( 2 ) } ( X _ { i } , \theta _ { j } ) + \lambda ^ { ( 1 ) } ( \theta _ { i } ) ^ { T } g _ { j } ^ { ( 3 ) } ( X _ { i } , \theta _ { j } ) } \\ & { \displaystyle + g ^ { ( 1 ) } ( X _ { i } , \theta _ { i } ) ^ { T } \lambda ^ { ( 1 ) } ( \theta _ { i } ) + \sum _ { j = 1 } ^ { N } g _ { j } ( X _ { i } , \theta _ { j } ) \lambda _ { j } ^ { ( 3 ) } ( \theta _ { i } ) \Big ) } \\ & { = \displaystyle \frac { 1 } { \alpha } \sum _ { i = 1 } ^ { N } \frac { \tau _ { i } ( \theta _ { i } ) } { \tau _ { i } ( \theta _ { i } ) } \Big ( \lambda ( \theta _ { i } ) ^ { T } g _ { i } ^ { ( 3 ) } ( X _ { i } , \theta _ { j } ) + g ( X _ { i } , \theta _ { j } ) ^ { T } \lambda ^ { ( 1 ) } ( \theta _ { i } ) \Big ) ^ { T } ( \lambda ( \theta _ { i } ) ^ { T } g _ { j } ^ { ( 3 ) } ( X _ { i } , \theta _ { j } ) + g ( X _ { i } , \theta _ { i } ) ^ { T } ) } \\ &  \displaystyle + \frac { 1 } { \alpha } \sum _ { i = 1 } ^ { N } \frac { \tau _ { i } ( \theta _ { i } ) } { ( \tau _ { i } ( \theta _ { i } ) ) ^ { T } } ( \frac { 1 } { \alpha } \sum _ { j = 1 } ^ { N } g _ { j } \Big ( g _ { i } \Big ) \Big ( \lambda ( \theta _ { i } ) ^ \end{array}
$$

By Lemma 5 and the facts that $\lambda ( \hat { \theta } ) = 0$ and ${ \begin{array} { r } { { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , { \hat { \theta } } ) = 0 } \end{array} }$ , we have for any $1 \leq i \leq n$ ,

$$
\begin{array} { l } { \displaystyle | | \lambda ( \theta _ { t } ) | | _ { 2 } \lesssim \frac { \| h \| _ { 2 } } { \sqrt { n } } } \\ { \displaystyle \tau _ { i } ( \theta _ { t } ) - 1 | \lesssim \frac { \| h \| _ { 2 } } { \sqrt { n } } } \\ { \displaystyle \tau _ { n } ( \theta _ { t } ) - 1 | \lesssim \frac { \| h \| _ { 2 } } { \sqrt { n } } } \\ { \displaystyle | \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( x _ { j } , \theta _ { t } ) - 0 | | _ { 2 } \lesssim \frac { \| h \| _ { 2 } } { \sqrt { n } } . } \end{array}
$$

So, we can get

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } l ^ { ( 2 ) } ( X _ { i } , \theta _ { t } ) = O ( \frac { \| h \| _ { 2 } } { \sqrt { n } } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \frac { \tau _ { i } ( \theta _ { t } ) } { \tau _ { n } ( \theta _ { t } ) } \left( \lambda ^ { ( 1 ) } ( \theta _ { t } ) ^ { T } g ( X _ { i } , \theta _ { t } ) g ( X _ { i } , \theta _ { t } ) ^ { T } \lambda ^ { ( 1 ) } ( \theta _ { t } ) \right)
$$

Since $\begin{array} { r } { \lambda ^ { ( 1 ) } ( \hat { \theta } ) = - \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \hat { \theta } ) g ( X _ { i } , \hat { \theta } ) ^ { T } \right) ^ { - 1 } \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ^ { ( 1 ) } ( X _ { i } , \hat { \theta } ) \right) } \end{array}$ , then by Bernstein inequality [Wainwright, 2019] and the first statement of Lemma $1$ , there exists a constant $c _ { 0 }$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that,

$$
\lVert \lambda ^ { ( 1 ) } ( \hat { { \boldsymbol { \theta } } } ) - ( - \Delta _ { \widetilde { { \boldsymbol { \theta } } } } ^ { - 1 } \mathcal { H } _ { \widetilde { { \boldsymbol { \theta } } } } ) \rVert _ { \mathrm { F } } \lesssim \sqrt { \frac { \log n } { n } } .
$$

Then by Lemma 5 and the mean value theorem, there exists a constant $c _ { 0 }$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that for any $t \in [ 0 , 1 ]$ and $\| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 }$ ,

$$
| \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } + \frac { h } { \sqrt { n } } ) - \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } ) + \frac { 1 } { 2 } h ^ { T } \mathcal { H } _ { \hat { \theta } } \Delta _ { \hat { \theta } } ^ { - 1 } \mathcal { H } _ { \hat { \theta } } h | \lesssim \frac { \| h \| _ { 2 } ^ { 3 } + \| h \| _ { 2 } ^ { 2 } \sqrt { \log n } } { \sqrt { n } } .
$$

So for set $A _ { 2 }$ ,

$$
\begin{array} { l l } { \displaystyle \int _ { A _ { 2 } } \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } \right) - \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \right| d h } \\ { \displaystyle \leq \int _ { A _ { 2 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } + \frac { h } { \sqrt { n } } ) - \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } ) \right) d h + \int _ { A _ { 2 } } \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \exp \left( \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \hat { \theta } } \end{array}
$$

When $\delta _ { 1 }$ is large enough, we have with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that,

$$
\begin{array} { l } { \displaystyle \int _ { A _ { 2 } } \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) d h \leq \frac { 1 } { n } , } \\ { \displaystyle \int _ { A _ { 2 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } + \frac { h } { \sqrt { n } } ) - \sum _ { i = 1 } ^ { n } l ( X _ { i } , \hat { \theta } ) \right) d h } \\ { \displaystyle \leq \int _ { A _ { 2 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } + c \frac { ( \log n ) ^ { 4 . 5 } } { \sqrt { n } } \right) d h } \\ { \displaystyle \leq \frac { 1 } { n } } \end{array}
$$

For set $A _ { 1 }$ , we have with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that,

$$
\begin{array} { r l } & { \displaystyle \int _ { \lambda _ { 1 } } \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } , \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } \right) - \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { \prime } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \right| d h } \\ & { \le \displaystyle \int _ { \lambda _ { 1 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \left| \exp \left( \frac { \sum _ { i } ^ { n } \left| ( X ^ { n } , \hat { \theta } + \frac { h } { \sqrt { n } } ) - \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \hat { \theta } ) \right| } { \sum _ { i = 1 } ^ { n } \left| ( X ^ { n } , \hat { \theta } ) - \sum _ { i } ^ { n } \right| } \right) - \exp \left( - \frac { h ^ { \prime } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \right| d h } \\ & { + \displaystyle \int _ { \lambda _ { 1 } } \left| \pi ( \hat { \theta } ) - \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \right| \exp \left( - \frac { h ^ { \prime } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) d h } \\ & { \le \displaystyle \int _ { \lambda _ { 1 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( - \frac { h ^ { \prime } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \frac { \| h \| _ { 2 } ^ { 3 } + \| h \| _ { 2 } ^ { 2 } \sqrt { \log n } } { \sqrt { n } } d h + \sqrt { \frac { \log n } { n } } } \\ & { \le \sqrt { \frac { \log n } { n } } , } \end{array}
$$

So, it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that

$$
\int \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } \right) - \pi ( \hat { \theta } ) \exp \left( - \frac { h ^ { T } V _ { \hat { \theta } } ^ { - 1 } h } { 2 } \right) \right| d h \lesssim \sqrt { \frac { \log n } { n } }
$$

# C.2 Proof of Theorem 2

We use the notation $L ( X ^ { n } ; \theta )$ to denote $\Pi _ { i = 1 } ^ { n } p _ { i } ( \theta )$ . The statement that $\sqrt { n } (  { \hat { \theta } } -  { \theta } ^ { * } )$ converge to $N ( 0 , V _ { \theta ^ { * } } )$ in distribution is followed from Theorem 7.1 of Newey and McFadden [1986]. Moreover, we have the following lemma.

Lemma 6. Under Assumption A.1, A.2’ and A.3, there exists a constant $C _ { 1 }$ such that for any constant $C _ { 2 }$ , there exists a constant $C$ such that if $C _ { 1 } \log n \le \alpha _ { n } \le C _ { 2 } n$ , then it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n } }$ that,

$$
d _ { \mathrm { T V } } \bigg ( \pi _ { \mathrm { P E } } \big ( \sqrt { n } ( \theta - \hat { \theta } ) | X ^ { n } \big ) , N \bigg ( 0 , \big ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal { H } _ { \theta ^ { * } } \big ) ^ { - 1 } \bigg ) \bigg ) \leq C \sqrt { \frac { \log n } { n } } .
$$

So, when $C _ { 1 } \log n \leq \alpha _ { n } \leq C _ { 2 } { \sqrt { n \log n } }$ , it holds that $d _ { \mathrm { T V } } ( \pi _ { \mathrm { P E } } ( \sqrt { n } ( \theta - \hat { \theta } ) | X ^ { n } ) , N ( 0 , V _ { \theta ^ { * } } ) ) \lesssim$ $\sqrt { \frac { \log n } { n } }$ . The desired conclusion is then followed from the shift and scale invariance of the total variation distance.

# C.2.1 Proof of Lemma 6

$$
\begin{array}{c} \left( \sqrt { n } ( \theta - \hat { \theta } ) \right. X ^ { n } \right) = \frac { \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) } { \int \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) \right)}   \end{array}
$$

we then bound

$$
\begin{array} { l } { \displaystyle \int \Bigl | \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) \right) } \\ { - \pi ( \hat { \theta } ) \exp \big ( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal H _ { \theta ^ { * } } ) h } { 2 } ) \Bigl | d h . } \end{array}
$$

Define the following set of $h$ ,

$$
\begin{array} { r l } & { A _ { 1 } = \left\{ \| h \| _ { 2 } \leq \delta _ { 1 } \sqrt { \log n } \right\} , } \\ & { A _ { 2 } = \left\{ \delta _ { 1 } \sqrt { \log n } \leq \| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} , } \\ & { A _ { 3 } = \left\{ \| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} . } \end{array}
$$

First for $A _ { 3 }$ , when $\delta _ { 2 } ( \log n ) ^ { 1 . 5 } \leq \| h \| _ { 2 } \leq \delta _ { 3 } \sqrt { n }$ , let $\begin{array} { r } { \theta = \hat { \theta } + \frac { h } { \sqrt { n } } } \end{array}$ , then $\lVert { \boldsymbol { \theta } } - { \boldsymbol { \hat { \theta } } } \rVert _ { 2 } \leq \delta _ { 3 }$ . Also, by the positive definiteness of $\mathcal { H } _ { \theta ^ { \ast } }$ and Lemma $1$ , it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$

that,

$$
\lVert { \boldsymbol { \theta } } ^ { * } - { \hat { \boldsymbol { \theta } } } \rVert _ { 2 } \lesssim { \sqrt { \frac { \log n } { n } } } .
$$

So we can choose ${ \delta } _ { 3 }$ to be small enough such that there exists a positive constant $c$ so that for any $\theta \in B _ { 2 \delta _ { 3 } } ( \theta ^ { * } )$ ,

$$
\mathcal { H } _ { \boldsymbol { \theta } } \succcurlyeq c I _ { d } .
$$

Also, by the fact that $\| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 }$ and equation (10), (11), we can get that when $\delta _ { 2 }$ is large enough, there exists a constant $c _ { 0 }$ such that it holds with probability larger than $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that for any $\| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 }$ , it satisfies that

$$
\log { \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } } \geq 2 d \log n .
$$

When $\| h \| _ { 2 } \geq \delta _ { 3 } { \sqrt { n } }$ , by the assumption that $\theta ^ { * }$ is the unique minimizer of ${ \mathcal { R } } ( \theta )$ , there exists a positive constant $c$ such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\| h \| _ { 2 } \geq \delta _ { 3 } { \sqrt { n } }$ , it satisfies that

$$
R \left( { \hat { \theta } } + { \frac { h } { \sqrt { n } } } \right) - { \mathcal { R } } ( \theta ^ { * } ) \geq c .
$$

Similar as equation (9), by Dudley’s inequality and Bernstein inequality, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that,

$$
\operatorname* { s u p } _ { \theta \in \Theta } \vert \mathcal { R } ( \theta ) - \mathcal { R } _ { n } ( \theta ) \vert \lesssim \sqrt { \frac { \log n } { n } } .
$$

Then combined with equation (14), it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\theta \in \Theta$ such that $\lVert { \boldsymbol { \theta } } - { \boldsymbol { \hat { \theta } } } \rVert _ { 2 } \geq \delta _ { 3 }$ ,

$$
\begin{array} { r l } & { \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) \right) } \\ & { \leq \exp \left( - \alpha _ { n } \left( \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) \right) } \\ & { \leq \exp ( - \alpha _ { n } \frac { c } { 2 } ) . } \end{array}
$$

So if we choose $\alpha _ { n } \geq { \frac { 3 } { c } } d \log n$ , there exists a constant $c _ { 0 }$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that,

$$
\begin{array} { l } { \displaystyle \int _ { A _ { 3 } } \bigg | \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \Big ( \log \frac { L \big ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } \big ) } { L \big ( X ^ { n } ; \hat { \theta } \big ) } - \alpha _ { n } \big ( \mathcal R _ { n } \big ( \hat { \theta } + h / \sqrt { n } \big ) - \mathcal R _ { n } ( \hat { \theta } ) \big ) \Big ) } \\ { - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } V _ { \theta ^ { * } } ^ { - 1 } h } { 2 } ) \bigg | d h \lesssim \displaystyle \frac { 1 } { n } } \end{array}
$$

For set $A _ { 1 }$ and $A _ { 2 }$ , use the same strategy of the proof of Lemma 1, there exists a constant $c _ { 0 }$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that for any $\| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 }$ ,

$$
\left| \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \frac { h ^ { T } V _ { \theta ^ { * } } ^ { - 1 } h } { 2 } \right| \lesssim \frac { \| h \| _ { 2 } ^ { 2 } ( \| h \| _ { 2 } + \sqrt { \log n } ) } { \sqrt { n } } .
$$

Also, since $\nabla _ { \boldsymbol { \theta } } \mathcal { R } _ { n } ( \hat { \boldsymbol { \theta } } ) = 0$ and $\alpha _ { n } \leq C _ { 2 } n$ ,

$$
\mathcal { R } _ { n } ( \boldsymbol { \hat { \theta } } + \frac { \boldsymbol { h } } { \sqrt { n } } ) - \mathcal { R } _ { n } ( \boldsymbol { \hat { \theta } } ) = \frac { 1 } { 2 n ^ { 2 } } h ^ { T } \sum _ { i = 1 } ^ { n } \ell ^ { ( 2 ) } ( X _ { i } , \boldsymbol { \hat { \theta } } + \frac { c h } { \sqrt { n } } ) \boldsymbol { h } ,
$$

it holds with probability larger than $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that

$$
\left| \alpha _ { n } ( \mathcal { R } _ { n } ( { \widehat { \theta } } + \frac { h } { { \sqrt { n } } } ) - \mathcal { R } _ { n } ( { \widehat { \theta } } ) ) - \frac { \alpha _ { n } } { n } \frac { h ^ { T } \mathcal { H } _ { \theta ^ { * } } h } { 2 } \right| \lesssim \frac { \| h \| _ { 2 } ^ { 2 } ( \| h \| _ { 2 } + \sqrt { \log n } ) } { \sqrt { n } } .
$$

Then if $\alpha _ { n } \leq C _ { 2 } n$ and $\delta _ { 1 }$ is large enough, we have

$$
\begin{array} { r l } & { \displaystyle \int _ { \Omega } \Big | z ( \bar { \theta } + \frac { h } { \sqrt { n } } ) \exp \Big ( \log \frac { L ( X ^ { n } ; \bar { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \bar { \theta } ) } - \alpha _ { n } \big ( \mathbb { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \big ) \Big ) } \\ & { \displaystyle - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { n } ( Y _ { n } ^ { n - 1 } + \frac { \alpha _ { n } } { 2 } \mathcal { H } _ { n } ; h ) } { 2 } ) \Big | \Delta h } \\ & { \displaystyle < \int _ { \Omega } \pi ( \hat { \theta } \mid \frac { h } { \sqrt { n } } ) \Big | \log \Big ( \log \frac { L ( X ^ { n } ; \bar { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \bar { \theta } ) } ~ \alpha _ { n } \big ( \mathbb { R } _ { n } ( \hat { \theta } \mid h / \sqrt { n } ) ~ \mathcal { R } _ { n } ( \hat { \theta } ) \big ) \Big ) } \\ & { \displaystyle - \exp ( - \frac { h ^ { n } ( Y _ { n } ^ { n - 1 } ; \cos \mathcal { R } _ { n } ; h ) } { 2 } ) \Big | \Delta h + \int _ { \Delta _ { 1 } } \Big | \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) - \pi ( \hat { \theta } ) \Big | \exp ( - \frac { h ^ { n } ( Y _ { n } ^ { n - 1 } ; \cos \mathcal { R } _ { n } ; h ) } { 2 } } \\ &  \displaystyle \lesssim \int _ { \Omega } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( - \frac { h ^ { n } ( Y _ { n } ^ { n - 1 } + \frac { \alpha _ { n } } { 2 } \mathcal { H } _ { n } ; h ) } { 2 } ) \frac { \| h \| \| \tilde { \theta } \| ( \hat { \theta } \| \| \sqrt { n } ) \| \sqrt { \log n } }  \sqrt  n \end{array}
$$

$$
\begin{array} { r l } & { \displaystyle \int _ { A _ { 2 } } \left| \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \big ( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \big ) \right) \right. } \\ & { \displaystyle - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal { H } _ { \theta ^ { * } } ) h } { 2 } ) \Bigg | d h } \\ & { \displaystyle \leq \int _ { A _ { 2 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \big ( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \big ) \right) d h } \\ & { \displaystyle + \int _ { A _ { 2 } } \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal { H } _ { \theta ^ { * } } ) h } { 2 } ) d h } \\ & { \displaystyle \leq \int _ { A _ { 2 } } \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal { H } _ { \theta ^ { * } } ) h } { 2 } + c \frac { \left( \log n \right) ^ { 4 . 5 } } { \sqrt { n } } \right) d h + \frac { 1 } { n } \lesssim \frac { 1 } { n } } \end{array}
$$

So, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that,

$$
\begin{array} { l } { \displaystyle \int | \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp ( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } ( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) ) )  } \\ { \displaystyle - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal { H } _ { \theta ^ { * } } ) h } { 2 } ) | d h \lesssim \sqrt { \frac { \log n } { n } } , } \end{array}
$$

$$
\begin{array} { r l } & { ~ \displaystyle \left. \int \pi ( \hat { \theta } + \frac { h } { \sqrt { n } } ) \exp \left( \log \frac { L ( X ^ { n } ; \hat { \theta } + h / \sqrt { n } ) } { L ( X ^ { n } ; \hat { \theta } ) } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \hat { \theta } ) \right) \right) } \\ & { - \pi ( \hat { \theta } ) \exp ( - \frac { h ^ { T } ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal H _ { \theta ^ { * } } ) h } { 2 } ) d h \right. \lesssim \sqrt { \frac { \log n } { n } } , } \\ & { ~ \displaystyle \qquad d _ { \mathrm { T V } } \left( \pi _ { \mathrm { P E } } ( \sqrt { n } ( \theta - \hat { \theta } ) | X ^ { n } ) , N \Big ( 0 , \big ( V _ { \theta ^ { * } } ^ { - 1 } + \frac { \alpha _ { n } } { n } \mathcal H _ { \theta ^ { * } } \big ) ^ { - 1 } \Big ) \right) \lesssim \sqrt { \frac { \log n } { n } } . } \end{array}
$$

# C.3 Proof of Corollary 1

Define sets

$$
A _ { 1 } = \left\{ X ^ { n } { \Big | } \| { \hat { \theta } } - \theta ^ { * } \| _ { 2 } \leq c _ { 1 } { \sqrt { \frac { \log n } { n } } } \right\} ,
$$

$$
A _ { 2 } = \left\{ X ^ { n } \Big \vert d _ { \mathrm { T V } } \big ( \pi _ { \mathrm { P E } } ( \cdot \vert X ^ { n } ) , N ( \widehat { \theta } , \frac { 1 } { n } V _ { \theta ^ { * } } ) \big ) \leq c _ { 2 } \sqrt { \frac { \log n } { n } } \right\} ,
$$

$$
A _ { 3 } = \left\{ X ^ { n } \Big | \left\| \hat { \theta } _ { B } - \hat { \theta } \right\| \leq c _ { 3 } \frac { \sqrt { \log n } } { n } , \left\| n \hat { \Sigma } _ { B } - V _ { \theta ^ { * } } \right\| _ { \mathrm { F } } \leq c _ { 3 } \sqrt { \frac { \log n } { n } } \right\}
$$

$$
A _ { 4 } = \left\{ X ^ { n } \right\} \left\| \left. \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ^ { ( 2 ) } ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } \right\| _ { \mathrm { F } } \leq c _ { 4 } \sqrt { \frac { \log n } { n } } \right\} .
$$

Let $A = A _ { 1 } \cap A _ { 2 } \cap A _ { 3 } \cap A _ { 4 }$ . Then by equation (15), (16), (17), (18) and Bernstein inequality, when $C _ { 1 } \log n \leq \alpha _ { n } \leq C _ { 2 } { \sqrt { n \log n } }$ and $( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$ is large enough, we have $\begin{array} { r } { \mathcal { P } ^ { * } ( A ) \geq 1 - \frac { 1 } { n } } \end{array}$ . Then

$$
\begin{array} { r l } & { P \left( \left\{ ( \theta ^ { * } - \hat { \theta } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } _ { B } ) \leq q _ { \alpha } \right\} \cap A \right) } \\ & { \leq P \left( ( \theta ^ { * } - \hat { \theta } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } _ { B } ) \leq q _ { \alpha } \right) } \\ & { \leq P \left( \left\{ ( \theta ^ { * } - \hat { \theta } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } _ { B } ) \leq q _ { \alpha } \right\} \cap A \right) + \frac { 1 } { n } } \end{array}
$$

So there exists a positive constant $c$ such that

$$
\begin{array} { r l } & { P \left( \left\{ ( \theta ^ { * } - \hat { \theta } ) ^ { T } n V _ { \theta ^ { * } } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } ) \leq q _ { \alpha } - c \frac { \left( \log n \right) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } \right\} \cap A \right) } \\ & { \leq P \left( \left\{ ( \theta ^ { * } - \hat { \theta } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } _ { B } ) \leq q _ { \alpha } \right\} \cap A \right) } \\ & { \leq P \left( \left\{ ( \theta ^ { * } - \hat { \theta } ) ^ { T } n V _ { \theta ^ { * } } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } ) \leq q _ { \alpha } + c \frac { \left( \log n \right) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } \right\} \cap A \right) } \end{array}
$$

Since under set $A$ , $\begin{array} { r } { \| \hat { \theta } - \theta ^ { * } \| _ { 2 } \lesssim \sqrt { \frac { \log n } { n } } } \end{array}$ , $\hat { \theta }$ is an interior point of $\Theta$ and $\nabla \mathcal { R } _ { n } ( { \widehat { \theta } } ) = 0$ . So we have

$$
\begin{array} { c } { { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \hat { \theta } ) = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ^ { ( 1 ) } ( X _ { i } , \theta ^ { * } ) ( \hat { \theta } - \theta ^ { * } ) + \displaystyle \frac { 1 } { 2 n } \sum _ { i = 1 } ^ { n } g ^ { ( 2 ) } ( X _ { i } , \theta ^ { \prime } ) ( \hat { \theta } - \theta ^ { * } ) } } \\ { { \displaystyle \ell ^ { * } - \hat { \theta } ) = \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ^ { ( 1 ) } ( X _ { i } , \theta ^ { * } ) \right) ^ { - 1 } \left( \displaystyle \frac { 1 } { \sqrt { n } } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + \displaystyle \frac { 1 } { 2 \sqrt { n } } \sum _ { i = 1 } ^ { n } g ^ { ( 2 ) } ( X _ { i } , \theta ^ { \prime } ) ( \hat { \theta } - \theta ^ { * } ) ^ { \otimes } \right) , } } \end{array}
$$

where $g ( x , \theta ) = \nabla \ell ( X , \theta )$ . Since under set $A$ , $\begin{array} { r } { \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ^ { ( 1 ) } ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } \right\| _ { \mathrm { F } } \leq c _ { 4 } \sqrt { \frac { \log n } { n } } , } \end{array}$ there exists a constant $c _ { 5 }$ such that

$$
\begin{array} { r l } & { \textup { p } ( \{ ( \theta ^ { * } - \hat { \theta } ) ^ { T } n V _ { \theta ^ { * } } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } ) \leq q _ { \alpha } + c \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } \} \cap A ) } \\ & { \leq P ( \{ ( \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) ^ { T } ( \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) \leq q _ { \alpha } + c _ { 5 } \frac { ( \log n ) } { \sqrt { n } }  } \\ & { \leq P ( ( \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) ^ { T } ( \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) \leq q _ { \alpha } + c _ { 5 } \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } }  } \end{array}
$$

Since $\mathbb { E } g ( X , \theta ^ { * } ) = \nabla \mathcal { R } ( \theta ^ { * } ) = 0$ , $\mathrm { C o v } ( g ( X , \theta ^ { * } ) ) = \Delta _ { \theta ^ { * } }$ and $V _ { \theta ^ { * } } ^ { - 1 } = \mathcal { H } _ { \theta ^ { * } } \Delta _ { \theta ^ { * } } ^ { - 1 } \mathcal { H } _ { \theta ^ { * } }$ , we have

$$
\begin{array} { r l } & { E ( V _ { { \theta } ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { { \theta } ^ { * } } ^ { - 1 } g ( X _ { i } , { \theta } ^ { * } ) ) = 0 } \\ & { \mathrm { C o v } ( V _ { { \theta } ^ { * } } ^ { - \frac { 1 } { 2 } } \mathcal { H } _ { { \theta } ^ { * } } ^ { - 1 } g ( X _ { i } , { \theta } ^ { * } ) ) = I _ { d } . } \end{array}
$$

Then by Berry-Esseen theorem [Raič, 2019], there exists a constant $c _ { 5 }$ such that

$$
\begin{array} { r l } & { \mathsf { P } ( ( \theta ^ { * } - \hat { \theta } _ { B } ) ^ { T } \hat { \Sigma } _ { B } ^ { - 1 } ( \theta ^ { * } - \hat { \theta } _ { B } ) \le q _ { \alpha } ) } \\ & { \le P ( ( \displaystyle \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac 1 2 } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) ^ { T } ( \displaystyle \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i = 1 } ^ { n } V _ { \theta ^ { * } } ^ { - \frac 1 2 } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } g ( X _ { i } , \theta ^ { * } ) ) \le q _ { \alpha } + c _ { 4 } \displaystyle \frac { ( \log n ) ^ { \frac 3 2 } } { \sqrt { n } } } \\ & { \le P ( \chi _ { d } ^ { 2 } \le q _ { \alpha } ) + c _ { 5 } \displaystyle \frac { ( \log n ) ^ { \frac 3 2 } } { \sqrt { n } } } \\ & { = 1 - \alpha + c _ { 5 } \displaystyle \frac { ( \log n ) ^ { \frac 3 2 } } { \sqrt { n } } } \end{array}
$$

Similarly, there exists a constant $c _ { 6 }$ such that

$$
\begin{array} { l } { P \left( ( { \theta ^ { * } } - { \hat { \theta } _ { B } } ) ^ { T } { \hat { \Sigma } _ { B } } ^ { - 1 } ( { \theta ^ { * } } - { \hat { \theta } _ { B } } ) \leq q _ { \alpha } \right) } \\ { \quad \geq 1 - \alpha - c _ { 6 } \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } . } \end{array}
$$

We then get the desired conclusion.

# C.4 Proof of Theorem 3

We first state an assumption that is similar to the Assumptions (C4)-(C6) in Molanes Lopez et al. [2009].

Assumption B.2’: There exist constant $c$ and $0 ~ < ~ \beta ~ \leq ~ 1$ such that it holds with probability at least $1 - n ^ { - 2 }$ that

(a) $\begin{array} { r } { \underset { \theta \in \Theta } { \operatorname* { s u p } } \left. n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } - \mathbb { E } \big [ g ( X , \theta ) g ( X , \theta ) ^ { T } \big ] \right. _ { \mathrm { F } } \leq c \sqrt { \frac { \log n } { n } } ; } \end{array}$ (b) $\begin{array} { l } { \underset { \leq \ell \leq } { \operatorname* { m p } } \ | n \cdot \sum _ { i = 1 } g ( \Lambda _ { i } , \ell ) g ( \Lambda _ { i } , \ell ) ^ { \circ } - \mathbb { E } [ g ( \Lambda , \ell ) g ( \Lambda , \ell ) ^ { \circ } ] \| _ { \mathrm { F } } \geq c _ { \gamma } \frac { \ldots } { n } ; } \\ { \underset { \leq \ell \leq } { \operatorname* { m p } } \ \| n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ g ( X , \theta ) ] + \mathbb { E } [ g ( X , \theta ^ { * } ) ] \| _ { 2 } \leq c \left( \sqrt { \frac { \log n } { n } } \ \| \theta - \sum _ { i = 1 } ^ { n } g ( \Lambda _ { i } , \theta ^ { * } ) \right) } \\ { \underset { \leq \ell \leq } { \operatorname* { m p } } \Big | \int _ { 2 } ^ { \theta } + \frac { \log n } { n } \Big ) ; } \\ { \underset { \leq \ell \leq } { \operatorname* { m p } } \Big | n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , \theta ^ { * } ) - \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { * } ) ] \Big | \leq c \left( \sqrt { \frac { \log n } { n } } \ \| \theta - \sum _ { i = 1 } ^ { n } g ( \Lambda _ { i } , \theta ^ { * } ) \right) . } \end{array}$ (c) s θ $\begin{array} { r l } & { \underset { \mathop { : } \mathop { \operatorname { u p } } } { \operatorname* { s u p } } \Big | n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell \big ( X _ { i } , \theta \big ) - n ^ { - 1 } \sum _ { i = 1 } ^ { n } \ell \big ( X _ { i } , \theta ^ { * } \big ) - \mathbb { E } [ \ell ( X , \theta ) ] + \mathbb { E } [ \ell ( X , \theta ^ { * } ) ] \Big | \leq c \left( \sqrt { \frac { \log n } { n } } \ \| \theta - \theta ^ { * } \| ^ { 2 } \right) } \\ & { \mathop { : } \mathop { \operatorname { u p } } _ { \texttt { + } } ^ { \beta } + \frac { \log n } { n } \bigg ) . } \end{array}$

We then state a lemma to prove that the statement in Assumption B.2 and Assumption B.1 is a sufficient condition to the statement in Assumption B.2’.

Lemma 7. Define

$$
\begin{array} { r l } & { d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| _ { 2 } ^ { 2 } } , } \\ & { d _ { n } ^ { \ell } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } ( \ell ( X _ { i } , \theta ) - \ell ( X _ { i } , \theta ^ { \prime } ) ) ^ { 2 } } . } \end{array}
$$

If (1) $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { X } , \theta \in \Theta } ( \| g ( x , \theta ) \| _ { 2 } + | \ell ( X , \theta ) | ) \leq C } \end{array}$ . (2) The $\varepsilon$ -covering numbers with respect to distance $d _ { n } ^ { g }$ and $d _ { n } ^ { \ell }$ of $\Theta$ , denoted by $\mathcal { N } ( \Theta , d _ { n } ^ { g } , \varepsilon )$ and $\mathcal { N } ( \Theta , d _ { n } ^ { \ell } , \varepsilon )$ respectively, are bounded by $\textstyle { \left( { \frac { n } { \varepsilon } } \right) } ^ { c }$ with a constant $c$ . (3) $\begin{array} { r } { \sqrt { \mathbb { E } \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| _ { 2 } ^ { 2 } } + \sqrt { \mathbb { E } ( \ell ( X , \theta ) - \ell ( X , \theta ^ { * } ) ) ^ { 2 } } \leq } \end{array}$ $c _ { 1 } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta }$ , then Assumption B.2’ holds.

Let $\begin{array} { r } { \hat { \theta } ^ { \circ } = \theta ^ { * } - \frac { 1 } { n } \mathcal { H } _ { \theta ^ { * } } ^ { - 1 } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) } \end{array}$ . We then bound

$$
\tau ( \hat { \theta } ^ { \diamond } + \frac { h } { \sqrt { n } } ) \exp \Big ( \log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) } { ( \frac { 1 } { n } ) ^ { n } } - \alpha _ { n } \big ( \mathcal { R } _ { n } ( \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \theta ^ { \ast } ) \big ) \Big ) - \pi ( \hat { \theta } ^ { \diamond } ) \exp ( - \frac { h } { \sqrt { n } } ) ,
$$

Define the following set of $h$ ,

$$
\begin{array} { r l } & { A _ { 1 } = \left\{ \| h \| _ { 2 } \leq \delta _ { 1 } \sqrt { \log n } \right\} , } \\ & { A _ { 2 } = \left\{ \delta _ { 1 } \sqrt { \log n } \leq \| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} , } \\ & { A _ { 3 } = \left\{ \| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \right\} . } \end{array}
$$

To begin with, we state the following lemmas.

Lemma 8. Suppose Assumption B.1, B.2 and $A . { \mathcal { Q } } ^ { \prime }$ holds, then there exist some positive constants $r$ and $C$ , such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that,

$$
\operatorname* { s u p } _ { \theta \in B _ { r } ( \theta ^ { * } ) } \lVert \lambda ( \theta ) \rVert _ { 2 } \leq C .
$$

Lemma 9. Suppose Assumption B.1, B.2 and A.2’ holds. Define $\begin{array} { r } { \tilde { \lambda } ( \theta ) = - \Delta _ { \theta ^ { * } } ^ { - 1 } \big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) + } \end{array}$ $\mathcal { H } _ { \theta ^ { * } } ( \theta - \theta ^ { * } ) \big ) = - \Delta _ { \theta ^ { * } } ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ( \theta - \hat { \theta } ^ { \circ } )$ . There exist positive constants $r _ { 0 }$ , $c _ { 0 }$ and c such that it holds with probability at least $\textstyle { 1 - { \frac { c _ { 0 } } { n ^ { 2 } } } }$ that,

$$
\operatorname* { s u p } _ { \theta \in B _ { r _ { 0 } } ( \theta ^ { * } ) } \| \lambda ( \theta ) - \tilde { \lambda } ( \theta ) \| _ { 2 } \leq c ( \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta } + \frac { \log n } { n } ) .
$$

Let $\mathcal { A } _ { 1 }$ be the event $\begin{array} { r } { \{ \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \theta ^ { * } ) \| _ { 2 } \leq c \sqrt { \frac { \log n } { n } } \} \cap \{ | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } L ( X _ { i } , \theta ^ { * } ) - \theta ( X _ { i } , \theta ^ { * } ) | \} = 0 } \end{array}$ $\mathbb { E } L ( X , \theta ^ { * } ) | \leq c \sqrt { \frac { \log n } { n } } \}$ , then by Assumption B.1, there exists a large enough $c$ such that $\begin{array} { r } { \mathcal { P } ^ { * } ( \mathcal { A } _ { 1 } ) \ge 1 - \frac { 1 } { n ^ { 2 } } } \end{array}$ . Let $\boldsymbol { \mathcal { A } } _ { 2 }$ be the event that statements in (a), (b), (c) of Assumption B.2’ hold, then by Lemma 7, $\begin{array} { r } { \mathcal { P } ^ { * } ( \mathcal { A } _ { 2 } ) \ge 1 - \frac { 1 } { n ^ { 2 } } } \end{array}$ . Unless otherwise specified, the following analysis is under event $\mathcal { A } _ { 1 } \cap \mathcal { A } _ { 2 }$ .

Step 1: Consider set $A _ { 3 } ~ = ~ \{ \| h \| _ { 2 } \geq \delta _ { 2 } ( \log n ) ^ { 1 . 5 } \}$ . We first consider the case that $\delta _ { 2 } ( \log n ) ^ { 1 . 5 } ~ \leq ~ \| h \| _ { 2 } ~ \leq ~ \delta _ { 3 } { \sqrt { n } }$ and let $\theta \ = \ \hat { \theta } ^ { \circ } + \ \frac { h } { \sqrt { n } }$ , then by Assumption B.2’ and $\mathbb { E } g ( X , \theta ^ { * } ) = 0$ , we can get $\begin{array} { r } { \| \hat { \theta } ^ { \circ } - \theta ^ { * } \| \lesssim \sqrt { \frac { \log n } { n } } } \end{array}$ and $\operatorname* { i n f } _ { \theta \in \Theta } \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \gtrsim - \sqrt { \frac { \log n } { n } }$ . Then by the thirce differentiability of ${ \mathcal { R } } ( \theta )$ and $\mathcal { H } _ { \theta ^ { \ast } } \succcurlyeq a I _ { d }$ with a positive constant $a$ , when $\delta _ { 3 }$ is small enough, it holds that $\mathcal { H } _ { \theta } \succcurlyeq \frac { a } { 2 } I _ { d }$ . So, by $\alpha _ { n } \lesssim \sqrt { n \log n }$ and (b) of Assumption B.2’, same as Step 1 of the proof of Lemma 1, we can get when $\delta _ { 2 }$ is large enough, for any $h \in \mathbb { R } ^ { d }$ such that $\delta _ { 2 } ( \log n ) ^ { 1 . 5 } \leq \| h \| _ { 2 } \leq \delta _ { 3 } \sqrt { n }$ , it holds that

$$
\begin{array} { r } { \mathrm { x p } \left( \log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \circ } + h / \sqrt { n } ) } { ( \frac { 1 } { n } ) ^ { n } } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } ^ { \circ } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \theta ^ { \ast } ) \right) \right) \leq \mathrm { e x p } ( - 2 d \log n ) . } \end{array}
$$

For the case that $\| h \| _ { 2 } \geq \delta _ { 3 } { \sqrt { n } }$ , by Assumption A.2’, B.1 and B.2’ we can get that there exists a positive constant $c$ such that

$$
\operatorname* { s u p } _ { \theta \in \Theta } \vert \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { \ast } ) - \mathcal { R } ( \theta ) + R ( \theta ^ { \ast } ) \vert \lesssim \sqrt { \frac { \log n } { n } } ,
$$

$$
\operatorname* { i n f } _ { \theta \in \Theta } \mathcal { R } ( \theta ) - \mathcal { R } ( \theta ^ { * } ) \geq c > 0 .
$$

So, when $\begin{array} { r } { \alpha _ { n } \geq \frac { 4 d } { c } \log n } \end{array}$ , for any $h$ such that $\| h \| _ { 2 } \geq \delta _ { 3 } { \sqrt { n } }$ , it holds that

$$
\begin{array} { r } { \mathrm { x p } \left( \log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \circ } + h / \sqrt { n } ) } { ( \frac { 1 } { n } ) ^ { n } } - \alpha _ { n } \left( \mathcal { R } _ { n } ( \hat { \theta } ^ { \circ } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \theta ^ { \ast } ) \right) \right) \leq \mathrm { e x p } ( - 2 d \log n ) . } \end{array}
$$

So we can get

$$
\begin{array} { l } { { \displaystyle \int _ { A _ { 3 } } \bigg | \pi ( \hat { \theta } ^ { \diamond } + \frac { h } { \sqrt { n } } ) \exp \Big ( \log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) } { ( \frac { 1 } { n } ) ^ { n } } - \alpha _ { n } \big ( \mathcal R _ { n } ( \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) - \mathcal R _ { n } ( \theta ^ { \ast } ) \big ) \Big ) } \ ~ } \\ { { \displaystyle - \pi ( \hat { \theta } ^ { \diamond } ) \exp ( - \frac { h ^ { T } V _ { \theta ^ { \star } } h } { 2 } ) \bigg | d h \leq \frac { 1 } { \sqrt { n } } . } } \end{array}
$$

Step 2: Consider set $A _ { 1 }$ and $A _ { 2 }$ , when $\| h \| _ { 2 } \leq \delta _ { 2 } ( \log n ) ^ { 1 . 5 }$ , let $\begin{array} { r } { \theta = \hat { \theta } ^ { \circ } + \frac { h } { \sqrt { n } } } \end{array}$ , then we have $\begin{array} { r } { \| \theta - \theta ^ { * } \| _ { 2 } \leq \frac { \| h \| _ { 2 } } { \sqrt { n } } + c \sqrt { \frac { \log n } { n } } } \end{array}$ . By Lemma 9, we can get $\begin{array} { r } { \| \lambda ( \theta ) \| \lesssim \sqrt { \frac { \log n } { n } } + \frac { \| h \| _ { 2 } } { \sqrt { n } } } \end{array}$ . Moreover,

$$
\log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } = \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) - n \log \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) \right) .
$$

Since

$$
( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) = 1 + \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) + \frac { 1 } { 2 } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ^ { 2 } + O \left( \| h \| _ { 2 } ^ { 3 } n ^ { - \frac { 3 } { 2 } } + ( \frac { \log n } { n } ) ^ { \frac { 3 } { 2 } } \right)
$$

We have

$$
\begin{array} { c l } { \displaystyle \log \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) \right) = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) + \displaystyle \frac { 1 } { 2 n } \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ^ { 2 } } \\ { \displaystyle - \frac { 1 } { 2 } \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } + O \left( \| h \| _ { 2 } ^ { 3 } n ^ { - \frac { 3 } { 2 } } + ( \frac { \log n } { n } ) ^ { \frac { 3 } { 2 } } \right) , } \end{array}
$$

So

$$
{ \frac { L ( X ^ { n } ; \theta ) } { ( { \frac { 1 } { n } } ) ^ { n } } } = - { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ^ { 2 } + { \frac { n } { 2 } } \left( { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } + O \left( \| h \| _ { 2 } ^ { 3 } n ^ { - { \frac { 1 } { 2 } } } + { \frac { ( 1 - \lambda ) ^ { n } } { 2 } } \right)
$$

For the first term, by Assumption B.1 and B.2’, we have

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ^ { * } ) ) ^ { 2 } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ^ { 2 } - \mathbb { E } ( \lambda ( \theta ) ^ { T } g ( X , \theta ^ { * } ) ) ^ { 2 } + \mathbb { E } ( \lambda ( \theta ) ^ { T } g ( X , \theta ^ { * } ) ) ^ { 2 } } \\ & { = \Big | \lambda ( \theta ) ^ { T } \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) g ( X _ { i } , \theta ^ { * } ) ^ { T } - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } - \mathbb { E } g ( X , \theta ^ { * } ) g ( X , \theta ^ { * } ) ^ { T } } \\ & { + \mathbb { E } g ( X , \theta ) g ( X , \theta ) ^ { T } \Big ) \lambda ( \theta ) \Big | \lesssim \sqrt { \frac { \log n } { n } } \frac { \| h \| _ { 2 } ^ { 2 } } { n } + ( \frac { \log n } { n } ) ^ { \frac { 3 } { 2 } } . } \end{array}
$$

Also,

$$
\begin{array} { r l } & { | \mathbb { E } ( \lambda ( \theta ) ^ { T } g ( X , \theta ^ { * } ) ) ^ { 2 } - \mathbb { E } ( \lambda ( \theta ) ^ { T } g ( X , \theta ) ) ^ { 2 } | } \\ & { = | \lambda ( \theta ) ^ { T } ( \Delta _ { \theta } - \Delta _ { \theta ^ { * } } ) \lambda ( \theta ) | } \\ & { \lesssim \| h \| _ { 2 } ^ { 3 } n ^ { - \frac { 3 } { 2 } } + ( \frac { \log n } { n } ) ^ { \frac { 3 } { 2 } } . } \end{array}
$$

$$
\begin{array} { l } { \displaystyle \frac 1 n \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ^ { * } ) ) ^ { 2 } } \\ { = \lambda ( \theta ) ^ { T } \frac 1 n \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) g ( X _ { i } , \theta ^ { * } ) ^ { T } \lambda ( \theta ) } \\ { = \lambda ( \theta ) ^ { T } \Delta _ { \theta ^ { * } } \lambda ( \theta ) + O \left( \sqrt { \frac { \log n } { n } } \frac { \| h \| _ { 2 } ^ { 2 } } { n } + ( \frac { \log n } { n } ) ^ { \frac 3 2 } \right) } \end{array}
$$

So we can get

$$
- \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) ^ { 2 } = - \frac { n } { 2 } \lambda ( \theta ) ^ { T } \Delta _ { \theta ^ { * } } \lambda ( \theta ) + O \left( \frac { \| h \| _ { 2 } ^ { 3 } } { \sqrt { n } } + \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } \right)
$$

For the second term, Since

$$
\begin{array} { r l } & { \| \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \mathbb { E } g ( X , \theta ) \| _ { 2 } \lesssim \sqrt { \frac { \log n } { n } } } \\ & { \| \mathbb { E } g ( X , \theta ) \| _ { 2 } \lesssim \displaystyle \frac { \| h \| _ { 2 } } { \sqrt { n } } + \sqrt { \frac { \log n } { n } } , } \end{array}
$$

we have

$$
{ \frac { n } { 2 } } \left( { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) ^ { 2 } \lesssim { \frac { \| h \| _ { 2 } ^ { 4 } } { n } } + { \frac { ( \log n ) ^ { 2 } } { n } }
$$

So we can get

$$
\log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } = - \frac { n } { 2 } \lambda ( \theta ) ^ { T } \Delta _ { \theta ^ { * } } \lambda ( \theta ) + O \left( \| h \| _ { 2 } ^ { 3 } n ^ { - \frac { 1 } { 2 } } + \frac { ( \log n ) ^ { \frac { 3 } { 2 } } } { \sqrt { n } } \right) .
$$

Also by Lemma 9, we have

$$
\lVert \lambda ( \theta ) - ( - \Delta _ { \theta ^ { * } } ^ { - 1 } \mathcal { H } _ { \theta ^ { * } } ( \theta - \hat { \theta } ^ { \circ } ) ) \rVert _ { 2 } \lesssim \lVert \theta - \theta ^ { * } \rVert _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \lVert \theta - \theta ^ { * } \rVert _ { 2 } ^ { \beta } + \frac { \log n } { n } .
$$

So we can get

$$
\log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \circ } + h / \sqrt { n } ) } { ( \frac { 1 } { n } ) ^ { n } } = - \frac { 1 } { 2 } h ^ { T } V _ { \theta ^ { * } } ^ { - 1 } h + O \left( \frac { \| h \| _ { 2 } ^ { 2 + \beta } + \log n ^ { 1 + \frac { \beta } { 2 } } } { n ^ { \frac { \beta } { 2 } } } \right) .
$$

Moreover, by Assumption B.1 and B.2’,

$$
\begin{array} { r l } & { \mathcal { R } _ { n } ( \hat { \theta } ^ { \circ } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \theta ^ { * } ) - \mathcal { R } ( \hat { \theta } ^ { \circ } + h / \sqrt { n } ) + \mathcal { R } ( \theta ^ { * } ) | \lesssim \bigg ( \displaystyle \frac { \log n } { n } \bigg ) ^ { \frac { 1 + \beta } { 2 } } + \sqrt { \frac { \log n } { n } } \bigg ( \displaystyle \frac { \| h \| _ { 2 } } { \sqrt { n } } + \frac { \| h \| _ { 2 } } { \| h \| _ { 2 } ^ { 3 } } \bigg ) } \\ & { \mathcal { R } ( \hat { \theta } ^ { \circ } + h / \sqrt { n } ) - \mathcal { R } ( \theta ^ { * } ) | \lesssim \displaystyle \frac { \log n } { n } + \frac { \| h \| _ { 2 } ^ { 2 } } { n } . } \end{array}
$$

So we have

$$
\mathcal { R } _ { n } ( \widehat { \theta } ^ { \circ } + h / \sqrt { n } ) - \mathcal { R } _ { n } ( \theta ^ { * } ) \gtrsim - \left( \left( \frac { \log n } { n } \right) ^ { \frac { 1 + \beta } { 2 } } + \sqrt { \frac { \log n } { n } } \left( \frac { \| h \| _ { 2 } } { \sqrt { n } } \right) ^ { \beta } + \frac { \| h \| _ { 2 } ^ { 2 } } { n } \right) .
$$

Then by $\alpha _ { n } \lesssim \sqrt { n \log n }$ , similar as the proof of Theorem 2, we can get

$$
\begin{array} { l } { { \displaystyle \int _ { A _ { 1 } \cup A _ { 2 } } \left| \pi ( \hat { \theta } ^ { \diamond } + \frac { h } { \sqrt { n } } ) \exp \Big ( \log \frac { L ( X ^ { n } ; \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) } { \binom { 1 } { n } ^ { n } } - \alpha _ { n } \big ( \mathcal R _ { n } ( \hat { \theta } ^ { \diamond } + h / \sqrt { n } ) - \mathcal R _ { n } ( \theta ^ { \ast } ) \big ) \Big ) \right. } } \\ { { \displaystyle - \left. \pi ( \hat { \theta } ^ { \diamond } ) \exp ( - \frac { h ^ { T } V _ { \theta ^ { \star } } h } { 2 } ) \right| d h \lesssim \frac { ( \log n ) ^ { 1 + \frac { \beta } { 2 } } } { n ^ { \frac { \beta } { 2 } } } . } } \end{array}
$$

So by Assumption A.2’ and B.1, we could get the first statement. The second statement that $\sqrt { n } ( \hat { \theta } ^ { \circ } - \theta ^ { * } )$ converges to $N ( 0 , V _ { \theta ^ { * } } )$ in distribution is followed from standard central limit theorem.

# C.5 Proof of Theorem 4

The first statement of Theorem 4 is a direct result from Lemma 6. W.l.o.g, we can assume $d > n$ , otherwise we could replace $\log d$ with $\log n$ in the following analysis. By the definition of the “model-averaged” Bayesian PETEL in Section 3.2, we have

$$
\begin{array} { r l } & { \mathrm { I } _ { \mathrm { P E } } ( S \left. \boldsymbol { X } ^ { n } \right) = } \\ & { \qquad \frac { \bigl ( \boldsymbol { \mathcal { A } } \bigr ) ^ { - 1 } q ( | \boldsymbol { S } | ) \int _ { \Theta _ { S } } \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } ( R _ { n } ( \theta _ { S } , 0 ) - R _ { n } ( \theta ^ { * } ) ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; \boldsymbol { S } ) / ( \frac { 1 } { n } ) ^ { n } d \theta } { \sum _ { \ell \in [ d ] , | \boldsymbol { S } | \leq s _ { 0 } } \bigl ( | \boldsymbol { S } | \bigr ) ^ { - 1 } q ( | \boldsymbol { S } | ) \int _ { \Theta _ { S } } \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } ( R _ { n } ( \theta _ { S } , 0 ) - R _ { n } ( \theta ^ { * } ) ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; \boldsymbol { S } ) / ( \frac { 1 } { n } ) ^ { n } } } \end{array}
$$

$$
\begin{array} { l } { \mathrm { I } _ { \mathrm { P E } } ( \| \theta - \theta ^ { * } \| _ { 2 } \ge \delta | X ^ { n } ) = } \\ { \quad \displaystyle \sum _ { \le \underline { { \epsilon } } [ d ] , | S | \le s _ { 0 } } \binom { d } { | S | } ^ { - 1 } q ( | S | ) \int _ { \| ( \theta _ { S } , 0 ) - \theta ^ { * } \| _ { 2 } \ge \delta } \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } ( R _ { n } ( \theta _ { S } , 0 ) - R _ { n } ( \theta ^ { * } ) ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } , S _ { i } ) , } \\ { \quad \quad \displaystyle \sum _ { S \in [ d ] , | S | \le s _ { 0 } } \binom { d } { | S | } ^ { - 1 } q ( | S | ) \int _ { \Theta _ { S } } \pi _ { S } ( \theta _ { S } ) \exp \big ( - \alpha _ { n , d } ( R _ { n } ( \theta _ { S } , 0 ) - R _ { n } ( \theta ^ { * } ) ) \big ) \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; S _ { i } ) , } \end{array}
$$

Let $\begin{array} { r } { L ( X ^ { n } ; \theta _ { S } , S ) = \prod _ { i = 1 } ^ { n } p _ { i } ( \theta _ { S } ; S ) } \end{array}$

Step 1: Lower bound the denominator.

By $\alpha _ { n , d } \leq C _ { 3 } n$ , similar as the analysis of Lemma 1 and Theorem 2, it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that,

$$
\begin{array} { r l } & { \displaystyle \sum _ { | S | \leq \alpha } q ( | S | ) \bigg ( \displaystyle \frac { d } { | S | } \bigg ) ^ { - 1 } \int \pi _ { S } ( \theta _ { S } ) \exp ( \log \frac { L ( X ^ { n } ; \theta _ { S } , S ) } { \big ( \frac 1 n \big ) ^ { n } } - \alpha _ { n , d } ( \mathcal { R } _ { n } ( \theta _ { S } , 0 ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) ) d } \\ & { \displaystyle \geq q ( s ^ { * } ) \bigg ( \displaystyle \frac { d } { s ^ { * } } \bigg ) ^ { - 1 } \int _ { \| \theta _ { S ^ { * } } - \hat { \theta } _ { S ^ { * } } \| _ { 2 } \leq \frac 1 n } \pi _ { S ^ { * } } ( \theta _ { S ^ { * } } ) \exp ( \log \frac { L ( X ^ { n } ; \theta _ { S ^ { * } } , S ^ { * } ) } { \big ( \frac 1 n \big ) ^ { n } } - \alpha _ { n , d } ( \mathcal { R } _ { n } ( S ^ { * } , \theta _ { S ^ { * } } ) - \mathcal { T } } \\ & { \displaystyle \geq c _ { 0 } q ( | S ^ { * } | ) \Big ) \bigg ( \displaystyle \frac { d } { | S ^ { * } | } \bigg ) ^ { - 1 } \int _ { | \theta _ { S ^ { * } } - \hat { \theta } _ { S ^ { * } } | | \geq \frac 1 n } \pi _ { S ^ { * } } ( \theta _ { S ^ { * } } ) d \theta _ { S ^ { * } } } \\ & { \displaystyle \geq \exp ( - c _ { 1 } s ^ { * } \log d ) \exp ( - \beta _ { n , d } s ^ { * } ) . } \end{array}
$$

Step 2: Upper bound $\Pi _ { \mathrm { P E } } ( | S | \geq s ^ { * } + 1 | X ^ { n } )$ .

By Theorem 14.20 of Wainwright [2019], there exist some constant $( c , c _ { 1 } , c _ { 2 } )$ such that it holds with probability at least $1 - \exp ( - c \log d )$ that

$$
\operatorname* { s u p } _ { \theta \in \Theta } \ | \mathcal { R } _ { n } ( \theta ) - \mathcal { R } _ { n } ( \theta ^ { * } ) - \mathcal { R } ( \theta ) + \mathcal { R } ( \theta ^ { * } ) | \leq c _ { 1 } ( \frac { \log d } { n } + \| \theta - \theta ^ { * } \| _ { 2 } \sqrt { \frac { \log d } { n } } )
$$

Also by Definition of the sparse prior in Section 3.2, there exists a constant $c _ { 4 }$ such that for any $s \geq s ^ { * } + 1$ , it holds that $q ( s ) \leq c _ { 4 } \exp { ( - \beta _ { n , d } ( s ^ { * } + 1 ) ) }$ .

1. Under Assumption C.2, by equation (22), we can further obtain that sup $\mathcal { R } _ { n } ( \theta ) -$ $\theta \in \Theta$ . Then by and , when i $\| \theta \| _ { 0 } \le s _ { 0 }$ e enough, $\mathcal { R } _ { n } ( \theta ^ { * } ) \geq - c _ { 2 } \frac { \log d } { n }$ $\beta _ { n , d } = C _ { 0 } \log d$ $\alpha _ { n , d } \leq C _ { 3 } n$ $C _ { 0 }$ we can get that $\begin{array} { r } { \Pi _ { \mathrm { P E } } ( | S | \geq s ^ { * } + 1 | X ^ { n } ) \leq \frac { 1 } { d } } \end{array}$ .

2. Under Assumption C.2’, by equation (22), we can further obtain that sup $\mathcal { R } _ { n } ( \theta ) -$ $\theta \in \Theta$ $\| \theta \| _ { 0 } \le s _ { 0 }$ $\mathcal { R } _ { n } ( \theta ^ { * } ) \geq - c _ { 2 } \sqrt { \frac { \log d } { n } }$ log dn , then by βn,d ≥ C0(log d ∨ αn,dq log dn ), when C0 is large enough, we can get that $\Pi _ { \mathrm { P E } } ( | S | \geq s ^ { * } + 1 | X ^ { n } ) \leq \exp ( - \frac { 1 } { 2 } \beta _ { n , d } )$ .

Step 3: Upper bound $\Pi _ { \mathrm { P E } } ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \delta | X ^ { n } )$ with $\delta \geq c { \frac { \log d } { n } }$ under Assumption C.2.

1. When $\alpha _ { n , d } ~ \geq ~ C _ { 1 } n$ . Since by Assumption C.2, there exists a positive constant $c _ { 1 }$ , such that $R ( \theta ) - R ( \theta ^ { * } ) \geq c _ { 1 } \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { 2 }$ , by equation (22), when $c$ is larger enough, then there exists a positive constant $c _ { 2 }$ such that it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $S \subset [ d ]$ with $| S | \le s ^ { * }$ and $\theta _ { S } \in \Theta _ { S }$ such that $\| ( \theta _ { S } , 0 ) - \theta ^ { * } \| _ { 2 } \geq \delta$ , it satisfies that $\exp \left( - \alpha _ { n , d } ( R _ { n } ( \theta _ { S } , 0 ) - R _ { n } ( \theta ^ { * } ) ) \right) \leq \exp ( - C _ { 1 } c _ { 2 } n \delta ^ { 2 } )$ . Then combined with equation (21) and the conclusion in Step 2, we can get that whenthat $\delta \geq c { \frac { \log d } { n } }$ $c$ probability larger than . $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ $\Pi _ { \mathrm { P E } } ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \delta | X ^ { n } ) \leq \exp ( - \frac { C _ { 1 } c _ { 1 } } { 2 } n \delta ^ { 2 } ) \leq \frac { 1 } { d }$

2. When αn,d ≥ C2 log dmini∈S∗ θ∗2 and $\begin{array} { r } { C _ { 2 } \frac { \log d } { \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } } \le C _ { 1 } n } \end{array}$ , then we have $\mathrm { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } \ge$ $\frac { C _ { 2 } \log d } { C _ { 1 } n }$ i. Moreover, we can get when $| S | \le s ^ { * }$ and $S \ne S ^ { * }$ , there exists a positive constant $c _ { 0 }$ such that for any $\theta _ { S } \in \Theta _ { S }$ , it holds that $\begin{array} { r } { R ( \theta _ { S } , 0 ) - R ( \theta ^ { * } ) \geq c _ { 0 } \operatorname* { m i n } _ { i \in S ^ { * } } { \theta _ { i } ^ { * } } ^ { 2 } } \end{array}$ , then by equation (22) when $C _ { 2 }$ is large enough, we can get that it holds with probability larger than $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that $\Pi _ { \mathrm { P E } } ( | S | \leq s ^ { * } , S \neq S ^ { * } | X ^ { n } ) \leq \frac { 1 } { 2 d }$ . Then by Lemma 6 and the conclusion in Step 2, we can get that when $c$ is large enough, $\Pi _ { \mathrm { P E } } ( \| \theta - \theta ^ { * } \| _ { 2 } \geq \delta | X ^ { n } ) \leq \frac { 1 } { d }$ .

Step 4: Upper bound $\Pi _ { \mathrm { P E } } ( | S | \le s ^ { * }$ , $S \neq S ^ { * } | X ^ { n } )$ under Assumption C.2’.

By Assumption C.2’, there exists a positive constant $c _ { 2 }$ such that for any $S \subseteq [ d ]$ with $| S | \le s ^ { * }$ and $S \neq S ^ { * }$ , it holds that inf R(θS, 0) − R(θ∗) ≥ c2mini∈S∗ θ∗i 2. Moreover, by equation (22), it holds with probability at least $1 - \exp ( - c \log d )$ that,

$$
\operatorname* { s u p } _ { \theta \in \Theta \atop | | \theta | | _ { 0 } \leq s ^ { * } } | \mathcal { R } ( \theta ) - \mathcal { R } _ { n } ( \theta ) | \lesssim \sqrt { \frac { \log d } { n } } .
$$

Then by $\begin{array} { r } { \binom { d } { 1 } + \cdot \cdot \cdot + \binom { d } { s ^ { * } } \leq p ( \frac { e d } { s ^ { * } } ) ^ { s ^ { * } } } \end{array}$ , $\log n \leq \log d \leq C n$ and $\begin{array} { r } { \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } \geq c _ { 1 } \sqrt { \frac { \log d } { n } } } \end{array}$ log d , when $c _ { 1 }$ is large enough, it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $S \subseteq [ d ]$ with

$| S | \le s ^ { * }$ and $S \neq S ^ { * }$ , it satisfies that

$$
\operatorname* { s u p } _ { \theta _ { S } \in \Theta _ { S } } \exp \left( \log \frac { L ( X ^ { n } ; \theta _ { S } , S ) } { ( \frac { 1 } { n } ) ^ { n } } - \alpha _ { n , d } ( \mathcal { R } _ { n } ( \theta _ { S } , 0 ) - \mathcal { R } _ { n } ( \theta ^ { * } ) ) \right) \leq \exp \left( - \alpha _ { n , d } \frac { \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } } { 2 } \right)
$$

Then combined with equation (21), there exist some constant $( C _ { 1 } , C _ { 2 } )$ such that when αn,d ≥ C2 log dmini∈S∗ θ∗i 2 and $\begin{array} { r } { \beta _ { n , d } \leq C _ { 1 } \alpha _ { n , d } \operatorname* { m i n } _ { i \in S ^ { * } } \theta _ { i } ^ { * 2 } } \end{array}$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$

$$
\Pi _ { \mathrm { P E } } ( | S | \leq s ^ { * } , S \neq S ^ { * } | X ^ { n } ) \leq \exp \left( - \frac { 1 } { 2 } \beta _ { n , d } \right) .
$$

Combined with the conclusion in Step 2, we could then get that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that $\Pi _ { \mathrm { P E } } ( S = S ^ { * } | X ^ { n } ) \geq 1 - 2 \exp ( - \frac { 1 } { 2 } \beta _ { n , d } )$ .

# D Proof of Technical details

# D.1 Proof of lemma 2

$$
\Pi _ { \mathrm { E } } ( \theta \in A ^ { c } \vert X ^ { n } ) = \frac { \int _ { A ^ { c } } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \right) d \theta } { \int \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \right) d \theta } .
$$

Step 1: Lower bound the denominator.

$$
\int \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \right) d \theta \geq \int _ { B _ { \frac { 1 } { \sqrt { n } } } ( \hat { \theta } _ { 1 } ) } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { L ( X ^ { n } ; \hat { \theta } _ { 1 } ) } \right) d \theta
$$

By equation (13), there exist constants $( c _ { 0 } , c )$ such that it holds with probability at least $\textstyle 1 - { \frac { c _ { 0 } } { n ^ { 2 } } }$ that when $\begin{array} { r } { \| \theta - \hat { \theta } _ { 1 } \| _ { 2 } \leq \frac { 1 } { \sqrt { n } } } \end{array}$ ,

$$
\left| \log { \frac { L ( X ^ { n } ; \theta ) } { L ( X ^ { n } ; { \hat { \theta } } _ { 1 } ) } } \right| \leq c .
$$

So, we can get that

$$
\int \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \right) d \theta \geq c _ { 1 } ( \frac { 1 } { \sqrt { n } } ) ^ { d } ,
$$

with a positive constant $c _ { 1 }$ .

Step 2: Upper bound the numerator.

$$
\begin{array} { l } { \displaystyle \int _ { A ^ { c } } \pi ( \theta ) \exp \left( \log \frac { L ( X ^ { n } ; \theta ) } { ( \frac { 1 } { n } ) ^ { n } } \right) d \theta } \\ { = \displaystyle \int _ { A ^ { c } } \pi ( \theta ) \exp \left( \sum _ { i = 1 } ^ { n } \log p _ { i } ( \theta ) - n \log \frac { 1 } { n } \right) d \theta . } \end{array}
$$

When $\theta \in \Theta \cap A ^ { c }$ , $\| \nabla _ { \theta } \mathcal { R } ( \theta ) \| \ge c$ .

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { n } p _ { i } ( \theta ) g ( X _ { i } , \theta ) = 0 } \\ { \displaystyle \sum _ { i = 1 } ^ { n } \left( \frac { 1 } { n } - p _ { i } ( \theta ) \right) g ( X _ { i } , \theta ) = \nabla _ { \theta } \mathcal { R } _ { n } ( \theta ) . } \end{array}
$$

By equation (9), it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ ,

$$
\operatorname* { s u p } _ { \theta \in \Theta } \lVert \nabla _ { \theta } \mathcal { R } _ { n } ( \theta ) - \nabla _ { \theta } \mathcal { R } ( \theta ) \rVert _ { 2 } \lesssim \sqrt { \frac { \log n } { n } } .
$$

So,

$$
\begin{array} { l } { { \displaystyle \sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ^ { \prime } ) - \frac { 1 } { n } \right) ^ { 2 } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) \| _ { 2 } ^ { 2 } \geq \frac { c ^ { 2 } } { 2 } } } \\ { { \displaystyle \sum _ { i = 1 } ^ { n } \left( p _ { i } ( \theta ^ { \prime } ) - \frac { 1 } { n } \right) ^ { 2 } \gtrsim \frac { 1 } { n } } . } \end{array}
$$

Define $\begin{array} { r } { q ( p _ { 1 } , \cdots , p _ { n - 1 } ) = \sum _ { i = 1 } ^ { n - 1 } \log p _ { i } + \log ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) } \end{array}$ . The Hessian matrix of function $q$ at point $( p _ { 1 } , \cdots , p _ { n - 1 } )$ is

$$
\mathcal { H } _ { q } | _ { ( p _ { 1 } , \cdots , p _ { n - 1 } ) } = D i a g ( - \frac { 1 } { p _ { 1 } ^ { 2 } } , \cdots , - \frac { 1 } { p _ { n - 1 } ^ { 2 } } ) - \frac { 1 } { ( 1 - \sum _ { i = 1 } ^ { n - 1 } p _ { i } ) ^ { 2 } } \mathbf { 1 } _ { ( n - 1 ) \times ( n - 1 ) }
$$

Let $p = ( p _ { 1 } , \cdots , p _ { n } )$ and $p _ { - n } = ( p _ { 1 } , \cdot \cdot \cdot , p _ { n - 1 } )$ . If $\| p \| _ { \infty } \geq n ^ { - \frac { 2 } { 3 } }$ , then

$$
\sum _ { i = 1 } ^ { n } \log p _ { i } \leq ( n - 1 ) \log { \frac { 1 - n ^ { - { \frac { 2 } { 3 } } } } { n - 1 } } .
$$

So,

$$
- n \log n - \sum _ { i = 1 } ^ { n } \log p _ { i } \geq - \log n - ( n - 1 ) \log \left( ( 1 - n ^ { - { \frac { 2 } { 3 } } } ) { \frac { n } { n - 1 } } \right)
$$

If $\| p \| _ { \infty } \leq n ^ { - \frac { 2 } { 3 } }$ , then we have $\begin{array} { r } { \sum _ { i = 1 } ^ { n - 1 } ( p _ { i } - \frac { 1 } { n } ) ^ { 2 } \gtrsim \frac { 1 } { n } } \end{array}$ , so by mean value theorem,

$$
\begin{array} { r l } & { q ( \displaystyle \frac { 1 } { n } , \cdots , \frac { 1 } { n } ) - q ( p _ { - n } ) } \\ & { \ = - \displaystyle \frac { 1 } { 2 } ( p _ { - n } - \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) ^ { T } \mathcal { H } _ { q } \vert _ { ( c p _ { - n } + ( 1 - c ) \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) } ( p _ { - n } - \frac { 1 } { n } \mathbf { 1 } _ { ( n - 1 ) } ) } \\ & { \ \gtrsim n ^ { \frac { 1 } { 3 } } . } \end{array}
$$

So there exists a positive constant $c$ , such that it holds with probability at least $\textstyle 1 - { \frac { 2 } { n ^ { 2 } } }$ that,

$$
\int _ { A ^ { c } } \pi ( \theta ) \exp \left( \log { \frac { L ( X ^ { n } ; \theta ) } { ( { \frac { 1 } { n } } ) ^ { n } } } \right) d \theta \leq \exp ( - c n ^ { \frac { 1 } { 3 } } ) .
$$

Then, combined with the lower bound on the denominator, we can get the desired conclusion.

# D.1.1 Proof of lemma 3

Fix a vector $\nu \in \mathbb { S } ^ { d - 1 }$ , then for any $\theta \in B _ { r } ( \tilde { \theta } )$ , there exists a constant $c \in \left[ 0 , 1 \right]$ depend on $\nu$ and $\theta$ , such that

$$
\nabla _ { \boldsymbol { \theta } } \mathcal { R } ( \boldsymbol { \theta } ) ^ { T } \boldsymbol { \nu } = \nabla _ { \boldsymbol { \theta } } R ( \tilde { \boldsymbol { \theta } } ) ^ { T } \boldsymbol { \nu } + ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) ^ { T } \mathcal { H } _ { ( c \boldsymbol { \theta } + ( 1 - c ) \tilde { \boldsymbol { \theta } } ) } \boldsymbol { \nu } .
$$

So, we have

$$
\| \nabla _ { \boldsymbol { \theta } } \mathcal { R } ( \boldsymbol { \theta } ) \| _ { 2 } \geq \operatorname* { i n f } _ { \boldsymbol { \theta ^ { \prime } } \in B _ { r } ( \tilde { \boldsymbol { \theta } } ) } \left| ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) ^ { T } \mathcal { H } _ { \boldsymbol { \theta ^ { \prime } } } \nu \right| .
$$

Take the supreme over $\nu \in \mathbb { S } ^ { d - 1 }$ , we can get

$$
\begin{array} { r l } & { \| \nabla _ { \boldsymbol { \theta } } \mathcal { R } ( \boldsymbol { \theta } ) \| _ { 2 } \geq \underset { \nu \in \mathbb { S } ^ { d - 1 } \boldsymbol { \theta } ^ { \prime } \in B _ { r } ( \tilde { \boldsymbol { \theta } } ) } { \operatorname* { s u p } } \operatorname* { i n f } _ { \mathbb { I } ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) } \left| ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) ^ { T } \mathcal { H } _ { \boldsymbol { \theta } ^ { \prime } } \nu \right| } \\ & { \geq \underset { \boldsymbol { \theta } ^ { \prime } \in B _ { r } ( \tilde { \boldsymbol { \theta } } ) } { \operatorname* { i n f } } \left| \frac { ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) ^ { T } \mathcal { H } _ { \boldsymbol { \theta } ^ { \prime } } \mathcal { H } _ { \tilde { \boldsymbol { \theta } } } ^ { - 1 } ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) } { \| \mathcal { H } _ { \tilde { \boldsymbol { \theta } } } ^ { - 1 } ( \boldsymbol { \theta } - \tilde { \boldsymbol { \theta } } ) \| } \right| } \end{array}
$$

Since for any $\theta \in B _ { r } ( \tilde { \theta } )$ , $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \theta } \succcurlyeq c I _ { d }$ and $\mathcal { H } _ { \theta } ^ { T } \mathcal { H } _ { \tilde { \theta } } ^ { - 1 } \succcurlyeq c I _ { d }$ , there exists a constant $c _ { 0 }$ such that

$$
\lVert \nabla _ { \theta } \mathcal { R } ( \theta ) \rVert _ { 2 } \geq c _ { 0 } \lVert \theta - \tilde { \theta } \rVert _ { 2 } .
$$

Since it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that $\operatorname* { s u p } _ { \theta \in \Theta } \lVert \mathcal { H } _ { \theta } - \mathcal { H } _ { \theta } ^ { n } \rVert _ { \mathrm { F } } \leq c _ { 1 } \sqrt { \frac { \log n } { n } }$ , we can get for any $\theta \in B _ { r } ( \tilde { \theta } )$ , $\mathcal { H } _ { \theta } ^ { n } \mathcal { H } _ { \theta } ^ { n } \succcurlyeq \frac { c } { 2 } I _ { d }$ and $\mathcal { H } _ { \theta } ^ { n } ( \mathcal { H } _ { \widetilde { \theta } } ^ { n } ) ^ { - 1 } \succcurlyeq \frac { c } { 2 } I _ { d }$ . Then by $\| \nabla \mathcal { R } _ { n } ( { \widehat { \theta } } ) \| _ { 2 } = 0$ , use the same strategy, we can get the conclusion of the second statement.

# D.2 Proof of lemma 4

Let b1 = supx∈X kg(x, θ)k2, choose $\begin{array} { r } { c _ { 2 } = \operatorname* { m i n } \left( \sqrt { \frac { a } { 8 } } , \frac { a } { 8 b _ { 1 } } \right) } \end{array}$ . Since $\Delta _ { \tilde { \theta } } \succcurlyeq a I _ { d }$ and $E g ( x , { \tilde { \theta } } ) = 0$ , we can find a small enough $\delta _ { 0 }$ , such that for any $\theta \in B _ { \delta _ { 0 } } ( \tilde { \theta } )$ , $\begin{array} { r } { \Delta _ { \theta } \succcurlyeq \frac { a } { 2 } I _ { d } } \end{array}$ and $\| \mathbb { E } g ( x , \theta ) \| _ { 2 } \le$ $\frac { a } { 8 b _ { 1 } }$ a

Then if there exist $\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \tilde { \theta } )$ such that $\mathcal { P } ^ { * } ( \lambda ^ { T } g ( X , \theta ) \geq c _ { 2 } ) < c _ { 3 }$ , by $\begin{array} { r } { \Delta _ { \theta } \succcurlyeq \frac { a } { 2 } I _ { d } } \end{array}$ , we can get

$$
\begin{array} { r l r } & { \frac { a } { 2 } \le \mathbb { E } ( \lambda ^ { T } g ( x , \theta ) ) ^ { 2 } } & \\ & { \quad < c _ { 2 } ^ { 2 } + b _ { 1 } ^ { 2 } c _ { 3 } + \displaystyle \int _ { \lambda ^ { T } g ( x , \theta ) \le 0 } ( \lambda ^ { T } g ( x , \theta ) ) ^ { 2 } d \mathcal { P } ^ { * } . } & \end{array}
$$

So,

$$
b _ { 1 } \int _ { \lambda ^ { T } g ( x , \theta ) \leq 0 } - \lambda ^ { T } g ( x , \theta ) d \mathcal { P } ^ { * } \geq \int _ { \lambda ^ { T } g ( x , \theta ) \leq 0 } ( \lambda ^ { T } g ( x , \theta ) ) ^ { 2 } d \mathcal { P } ^ { * } > \frac { a } { 2 } - ( c _ { 2 } ^ { 2 } + b _ { 1 } ^ { 2 } c _ { 3 } ) .
$$

Also,

$$
\int _ { \lambda ^ { T } g ( x , \theta ) \leq 0 } - \lambda ^ { T } g ( x , \theta ) d \mathcal { P } ^ { * } = \int _ { \lambda ^ { T } g ( x , \theta ) \geq 0 } \lambda ^ { T } g ( x , \theta ) d \mathcal { P } ^ { * } - \mathbb { E } ( \lambda ^ { T } g ( x , \theta ) ) .
$$

Then, by $\begin{array} { r } { \| E g ( x , \theta ) \| _ { 2 } \le \frac { a } { 8 b _ { 1 } } } \end{array}$ , we can get

$$
b _ { 1 } \int _ { \lambda ^ { T } g ( x , \theta ) \geq 0 } \lambda ^ { T } g ( x , \theta ) d \mathcal { P } ^ { * } + \frac { a } { 8 } > \frac { a } { 2 } - ( c _ { 2 } ^ { 2 } + b _ { 1 } ^ { 2 } c _ { 3 } ) .
$$

Then, by

$$
\int _ { \lambda ^ { T } g ( x , \theta ) \geq 0 } \lambda ^ { T } g ( x , \theta ) d \mathcal { P } ^ { * } < c _ { 2 } + b _ { 1 } c _ { 3 } ,
$$

we can get

$$
c _ { 3 } > \frac { \frac { 3 } { 8 } a - c _ { 2 } ^ { 2 } - b _ { 1 } c _ { 2 } } { 2 b _ { 1 } ^ { 2 } } \geq \frac { a } { 1 6 b _ { 1 } ^ { 2 } } .
$$

So, if we choose $\begin{array} { r } { c _ { 3 } = \frac { a } { 1 6 b _ { 1 } ^ { 2 } } } \end{array}$ , we can get the conclusion of the first statement.

For the second statement, let $\begin{array} { r } { \varepsilon = \frac { c _ { 2 } } { 4 b _ { 1 } } } \end{array}$ and $N _ { \varepsilon }$ be the minimal $\varepsilon$ -covering set of $\mathbb { S } ^ { d - 1 }$ with respect to $\ell _ { 2 }$ distance, then $| N _ { \varepsilon } | \leq ( \frac { 3 } { \varepsilon } ) ^ { d }$ .

Then by Bernstein inequality, there exists a constant $c _ { 4 }$ such that it hold with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\operatorname* { s u p } _ { \lambda \in N _ { \varepsilon } } \left. \mathcal { P } ^ { \ast } ( \lambda ^ { T } g ( X , \tilde { \theta } ) \geq c _ { 2 } ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \lambda ^ { T } g ( X _ { i } , \tilde { \theta } ) \geq c _ { 2 } } \right. \leq c _ { 4 } \sqrt { \frac { \log n } { n } } .
$$

So, for any $\lambda \ \in \ N _ { \varepsilon }$ , there are at least $\left( c _ { 3 } - c _ { 4 } { \sqrt { \frac { \log n } { n } } } \right) n$ number of data such that $\lambda ^ { T } g ( x , \tilde { \theta } ) \geq c _ { 2 }$ . Also, for any $\lambda \in \mathbb { S } ^ { d - 1 }$ , there exists $\tilde { \lambda } \in N _ { \varepsilon }$ such that $\| \lambda - \widetilde { \lambda } \| _ { 2 } \leq \varepsilon$ , so we can choose a small enough $\delta _ { 0 }$ , such that for any $\theta \in B _ { \delta _ { 0 } } ( \tilde { \theta } )$ ,

$$
| \lambda ^ { T } g ( x , \theta ) - \tilde { \lambda } ^ { T } g ( x , \tilde { \theta } ) | \leq b _ { 1 } \varepsilon + \| g ( x , \theta ) - g ( x , \tilde { \theta } ) \| _ { 2 } \leq \frac { c _ { 2 } } { 2 } .
$$

So for any $1 \leq i \leq n$ such that $\tilde { \lambda } ^ { T } g ( X _ { i } , \tilde { \theta } ) \geq c _ { 2 }$ , it holds that $\begin{array} { r } { \lambda ^ { \prime } g ( X _ { i } , \theta ) \ge \frac { c _ { 2 } } { 2 } } \end{array}$ , we can then get the desired conclusion.

# D.3 Proof of lemma 5

Consider $\begin{array} { r } { \theta \in \Bigl \{ \theta \ : \big | \ : \| \theta - \tilde { \theta } \| _ { 2 } \le \frac { 2 \delta _ { 2 } ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } \Bigr \} } \end{array}$ , by equation (12), it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\begin{array} { r } { \theta \in \left\{ \theta \vert \Vert \theta - \tilde { \theta } \Vert _ { 2 } \leq \frac { 2 \delta _ { 2 } ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } \right\} } \end{array}$ , it satisfies that $\lVert \lambda ( \theta ) \rVert _ { 2 } \leq \lambda _ { 0 }$ . Since $\lambda ( \theta )$ is the solution of

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) g ( X _ { i } , \theta ) = 0
$$

we have

$$
\begin{array} { r l } & { \lambda ^ { ( 1 ) } ( \theta ) = - \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \right) ^ { - 1 } } \\ & { \quad \quad \cdot \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) \left( g ^ { ( 1 ) } ( X _ { i } , \theta ) + g ( X _ { i } , \theta ) \lambda ( \theta ) ^ { T } g ^ { ( 1 ) } ( X _ { i } , \theta ) \right) \right) . } \end{array}
$$

For any $\nu \in \mathbb { S } ^ { d - 1 }$ , let $b _ { 1 } =$ sup kg(x, θ)k2, x∈X θ∈{θ | kθ−θ˜k2≤ 2δ1(log n)1.5√ } n

$$
\begin{array} { r l } & { \nu ^ { T } \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \right) \nu } \\ & { \geq \exp ( - \lambda _ { 0 } b _ { 1 } ) \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \nu ^ { T } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \nu } \\ & { = \exp ( - \lambda _ { 0 } b _ { 1 } ) \left( \nu ^ { T } \Delta _ { \theta } \nu + \nu ^ { T } \left( \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } - \Delta _ { \theta } \right) \nu \right) } \end{array}
$$

Similar as equation (9), by Dudley’s inequality and Bernstein inequality, with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ ,

$$
\operatorname* { s u p } _ { \theta \in \left\{ \| \theta - \tilde { \theta } \| _ { 2 } \leq \frac { 2 \delta _ { 2 } ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } \right\} } \left\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } - \Delta _ { \theta } \right\| _ { \mathrm { F } } \lesssim \sqrt { \frac { \log n } { n } } .
$$

Also, by $\Delta _ { \tilde { \theta } } \succcurlyeq a I _ { d }$ , we have for any $\begin{array} { r } { \theta \in \Big \{ \| \theta - \tilde { \theta } \| _ { 2 } \leq \frac { 2 \delta _ { 2 } ( \log n ) ^ { 1 . 5 } } { \sqrt { n } } \Big \} } \end{array}$ , $\begin{array} { r } { \Delta _ { \theta } \succcurlyeq \frac { a } { 2 } I _ { d } } \end{array}$ . Then we can get for any ν ∈ Sd−1,

$$
\nu ^ { T } \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) \right) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \right) \nu \geq \exp ( - \lambda _ { 0 } b _ { 1 } ) \frac { a } { 4 }
$$

So,

$$
\left\| \left( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } \right) ^ { - 1 } \right\| _ { o p } \leq \exp ( \lambda _ { 0 } b _ { 1 } ) \frac { 4 } { a } .
$$

Then, by

$$
\operatorname* { s u p } _ { \stackrel { x \in \mathcal { X } } { \theta \in \Theta } } \left( \operatorname* { m a x } _ { 1 \leq i \leq d } \left| \frac { \partial \ell ( X , \theta ) } { \partial \theta _ { i } } \right| + \operatorname* { m a x } _ { 1 \leq i \leq d } \left| \frac { \partial ^ { 2 } \ell ( X , \theta ) } { \partial \theta _ { i } \partial \theta _ { j } } \right| + \operatorname* { m a x } _ { 1 \leq i \leq d \atop 1 \leq j \leq d } \left| \frac { \partial ^ { 3 } \ell ( X , \theta ) } { \partial \theta _ { i } \partial \theta _ { j } \partial \theta _ { k } } \right| \right) \leq C ,
$$

and

$$
g ( x , \theta ) = \nabla \ell ( X , \theta ) ,
$$

we can get the desired conclusion.

# D.4 Proof of Lemma 7

For (b) of Assumption B.2’, let $g _ { j } ( X _ { i } , \theta )$ denote the $j$ th dimension of $g ( X _ { i } , \theta )$ , for any $1 \leq j \leq d$ , define the function class $\mathcal { G } _ { j } = \{ g _ { j } ( \cdot , \theta ) - g _ { j } ( \cdot , \theta ^ { * } ) , \theta \in \Theta \}$ and its star hull $\mathcal { G } _ { j } = \{ a g , g \in \mathcal { G } _ { j } \}$ . Define

$$
\mathcal { R } _ { n } ( \delta ) = \mathbb { E } _ { X } \mathbb { E } _ { \varepsilon } \left[ \operatorname* { s u p } _ { \stackrel { f \in \bar { \mathcal { G } } _ { j } } { \mathbb { E } f ^ { 2 } \leq \delta ^ { 2 } } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \varepsilon _ { i } f ( X _ { i } ) \right| \right] ,
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are n i.i.d. copies from Rademacher distribution, i.e. $P ( \varepsilon _ { i } = 1 ) = P ( \varepsilon _ { i } =$ $- 1 ) = 0 . 5$ . Define the distance between $f , f ^ { \prime } \in \bar { \mathcal { G } } _ { j }$ ,

$$
d _ { n } ( f , f ^ { \prime } ) = { \sqrt { \sum _ { i = 1 } ^ { n } ( f ( X _ { i } ) - f ^ { \prime } ( X _ { i } ) ) ^ { 2 } } } .
$$

Then by the uniformly boundness of $\mathcal { G } _ { j }$ , it follows that

$$
\begin{array} { r l } & { \log \mathcal { N } ( \bar { \mathcal { G } } _ { j } , d _ { n } , \varepsilon ) } \\ & { \leq \log ( \frac { c } { \varepsilon } ) + \log \mathcal { N } ( \mathcal { G } _ { j } , d _ { n } , \varepsilon ) } \\ & { \leq \log ( \frac { c } { \varepsilon } ) + \log \mathcal { N } ( \Theta , d _ { n } ^ { g } , \varepsilon ) } \\ & { \lesssim \log n + \log ( \frac { 1 } { \varepsilon } ) } \end{array}
$$

Then by Dudley inequality [Vershynin, 2018] and equation (3.84) of Wainwright [2019], it holds that

$$
\mathcal { R } _ { n } \left( \sqrt { \frac { \log n } { n } } \right) \lesssim \frac { \log n } { n } .
$$

Then by Theorem 14.20 of Wainwright [2019] and $\sqrt { \mathbb { E } \| g ( X , \theta ) - g ( X , \theta ^ { * } ) \| _ { 2 } ^ { 2 } } \ \lesssim \ \| \theta \ - $ $\theta ^ { * } \| _ { 2 } ^ { \beta }$ , there exists a constant $c$ such that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that s θ∈Θ $\begin{array} { r l } & { \underset { \leq \Theta } { \operatorname { u p } } \Vert \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \theta ) + \mathbb { E } g ( X , \theta ^ { * } ) \Vert _ { 2 } \leq c ( \sqrt { \frac { \log n } { n } } \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { \beta } + \frac { \log n } { \log n } ) ^ { \frac { 1 } { \beta } } . } \end{array}$ g nn ) ; We can use the same strategy to prove the statement in (c) of Assumption B.2’. For (a) of the Assumption B.2’, there exists a constant $c$ such that for any $1 \leq j , k \leq d$ and $\theta , \theta ^ { \prime } \in \Theta$ ,

$$
\sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( g ^ { h } ( X _ { i } , \theta ) g ^ { k } ( X _ { i } , \theta ) - g ^ { h } ( X _ { i } , \theta ^ { \prime } ) g ^ { k } ( X _ { i } , \theta ^ { \prime } ) ) ^ { 2 } } \leq c \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| }
$$

So the statement in (a) of Assumption B.2’ is followed by Dudley inequality and Talagrand concentration inequality [Wainwright, 2019].

# D.5 Proof of Lemma 8 and Lemma 9

Let $\mathcal { A } _ { 1 }$ be the event $\begin{array} { r } { \{ \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \theta ^ { * } ) \| _ { 2 } \leq c \sqrt { \frac { \log n } { n } } \} \cap \{ | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } L ( X _ { i } , \theta ^ { * } ) - \theta ( X _ { i } , \theta ^ { * } ) | \} = 0 } \end{array}$ $\mathbb { E } L ( X , \theta ^ { * } ) | \leq c \sqrt { \frac { \log n } { n } } \}$ , then by Assumption B.1, there exists a large enough $c$ such that $\textstyle { \mathcal { P } } ^ { * } ( { \mathcal { A } } _ { 1 } ) \geq 1 - { \frac { 1 } { n ^ { 2 } } }$ . Let $\boldsymbol { A } _ { 2 }$ be the event that statements (a), (b), (c) in Assumption B.2’ hold, then by Lemma 7, it holds that $\begin{array} { r } { \mathcal { P } ^ { * } ( \mathcal { A } _ { 2 } ) \ge 1 - \frac { 1 } { n ^ { 2 } } } \end{array}$ . Unless otherwise specified, the following analysis is under event $\mathcal { A } _ { 1 } \cap \mathcal { A } _ { 2 }$ . For the statement of Lemma 8, by Assumption B.1 and $\mathrm { A . 2 ^ { \prime } }$ and Lemma 4, we can get that there exist some positive constants $\left( \delta _ { 0 } , c _ { 2 } , c _ { 3 } \right)$ such that for any $\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \theta ^ { * } )$ , it holds that $\mathcal { P } ^ { * } ( \lambda ^ { I ^ { \prime } } g ( X , \theta ) \ge c _ { 2 } ) \ge c _ { 3 }$ . So $\mathbb { E } \operatorname* { m a x } \left( \lambda ^ { T } g ( X , \theta ) - \frac { c _ { 2 } } { 2 } , 0 \right) \geq \frac { c _ { 2 } c _ { 3 } } { 2 }$ . Moreover, by Assumption B.2 that the $\varepsilon$ -covering number of $\Theta$ with respect to $d _ { n } ^ { g }$ is upper bounded by $\scriptstyle { \left( { \frac { n } { \varepsilon } } \right) } ^ { c }$ , using Dudley inequality and Talagrand concentration inequality, we can get that there exists a constant $c _ { 4 }$ such that it

hold with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$

$$
\operatorname* { s u p } _ { x \in \Theta } \left| \mathbb { E } \operatorname* { m a x } \left( \lambda ^ { T } g ( X , \theta ) - \frac { c _ { 2 } } { 2 } , 0 \right) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname* { m a x } \left( \lambda ^ { T } g ( X _ { i } , \theta ) - \frac { c _ { 2 } } { 2 } , 0 \right) \right| \leq c _ { 4 } \sqrt { \frac { \log n } { n } } .
$$

Let $b = \qquad \operatorname* { s u p } \qquad \| g ( x , \theta ) \| _ { 2 }$ , it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $x { \in } \mathcal { X } , \theta { \in } B _ { \delta _ { 0 } } ( \theta ^ { * } )$   
$\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \theta ^ { * } )$ , it satisfies that

$$
\frac { c _ { 2 } c _ { 3 } } { 4 } \leq \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname* { m a x } ( \lambda ^ { T } g ( X _ { i } , \theta ) - \frac { c _ { 2 } } { 2 } , 0 ) \leq ( b - \frac { c _ { 2 } } { 2 } ) \frac { \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \lambda ^ { T } g ( X _ { i } , \theta ) \geq \frac { c _ { 2 } } { 2 } } } { n }
$$

So we can get that there exist some positive constants $\left( \delta , c _ { 2 } , c _ { 3 } \right)$ such that for any $\lambda \in \mathbb { S } ^ { d - 1 }$ and $\theta \in B _ { \delta _ { 0 } } ( \theta ^ { * } )$ , it holds that $\begin{array} { r } { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbf { 1 } _ { \lambda ^ { T } g ( x , \theta ) \geq c _ { 2 } / 2 } \geq \frac { c _ { 2 } c _ { 3 } } { 4 ( b - \frac { c _ { 2 } } { 2 } ) } > 0 } \end{array}$ . So lemma 8 can be proved using equation (12). For the proof of Lemma 9, according to Assumption B.2’, it holds that

$$
\underset { \in \Theta } { \operatorname { u p } } \Vert \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathbb { E } g ( X , \theta ) + \mathbb { E } g ( X , \theta ^ { * } ) \Vert _ { 2 } \leq c ( \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta } + \frac { \log n } { n } )
$$

Also, by Assumption B.1, we have

$$
\begin{array} { r } { \mathbb { E } g ( X , \theta ) - \mathbb { E } g ( X , \theta ^ { * } ) = \mathcal { H } _ { \theta ^ { * } } ( \theta - \theta ^ { * } ) + O ( \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } ) , } \end{array}
$$

so we can get

$$
\underset { \in \Theta } { \operatorname { u p } } \Vert \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ^ { * } ) - \mathcal { H } _ { \theta ^ { * } } ( \theta - \theta ^ { * } ) \Vert _ { 2 } \lesssim \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \Vert \theta - \theta ^ { * } \Vert _ { 2 } ^ { \beta } + \frac { \log n } { \log n } \Vert \theta ^ { * } \Vert _ { 2 } ^ { 2 } ,
$$

So we have

$$
\begin{array} { l } { \displaystyle \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \widetilde { \lambda } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \Big ( - \big ( \Delta _ { \theta ^ { * } } ^ { - 1 } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( x _ { j } , \theta ) \big ) ^ { T } g ( X _ { i } , \theta ) \Big ) g ( X _ { i } , \theta ) \Big | _ { \displaystyle \theta \in \mathbb { Z } } \Big | _ { \theta \in \mathbb { Z } } \Big | _ { \theta \in \mathbb { Z } } \Big | _ { \theta \in \mathbb { Z } } } \\ { \displaystyle \lesssim \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta } + \frac { \log n } { n } . } \end{array}
$$

By $\mathbb { E } g ( X , \theta ^ { * } ) = 0$ , we can get $\begin{array} { r } { \| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) \| \lesssim \| \theta - \theta ^ { * } \| _ { 2 } + \sqrt { \frac { \log n } { n } } . } \end{array}$ , so

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { n } \exp \Big ( - \big ( \Delta _ { \theta ^ { * } } ^ { - 1 } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( x _ { j } , \theta ) \big ) ^ { T } g ( X _ { i } , \theta ) \Big ) g ( X _ { i } , \theta ) } \\ { \displaystyle = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) - \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( x _ { j } , \theta ) g ( x _ { j } , \theta ) ^ { T } \Delta _ { \theta ^ { * } } ^ { - 1 } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , \theta ) + O ( \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } + \frac { \log n } { n } ) . } \end{array}
$$

Then by

$$
\| \frac { 1 } { n } \sum _ { j = 1 } ^ { n } g ( x _ { j } , \theta ) g ( x _ { j } , \theta ) ^ { T } \Delta _ { \theta ^ { * } } ^ { - 1 } - I _ { d } \| _ { 2 } \lesssim \| \theta - \theta ^ { * } \| _ { 2 } + \sqrt { \frac { \log n } { n } } ,
$$

we can get

$$
\| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \widetilde { \lambda } ( \theta ) ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) \| _ { 2 } \lesssim \| \theta - \theta ^ { * } \| _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \| \theta - \theta ^ { * } \| _ { 2 } ^ { \beta } + \frac { \log n } { n } .
$$

By Lemma 8, there exist positive constants $C$ and $r$ such that sup $\operatorname* { m a x } \{ \| \lambda ( \theta ) \| _ { 2 } , \| \tilde { \lambda } ( \theta ) \| _ { 2 } \} \le$ $\theta \in B _ { r } ( \theta ^ { * } )$   
$C$ . By Assumption A.2’ and B.1, we can find a small enough $r _ { 0 } \le r$ such that for any   
$\theta \in B _ { r _ { 0 } } ( \theta ^ { * } )$ , it holds that $\mathcal { H } _ { \theta } \succcurlyeq \frac { a } { 2 } I _ { d }$ and $\Delta _ { \theta } \succcurlyeq \frac { b } { 2 } I _ { d }$ , where $a , b > 0$ . Fix a $\theta \in B _ { r _ { 0 } } ( \theta ^ { * } )$ ,   
define $\begin{array} { r } { f ( \lambda ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ^ { T } g ( X _ { i } , \theta ) ) } \end{array}$ , then we have

$$
\begin{array} { l } { { \displaystyle f ^ { ( 1 ) } ( \lambda ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) } } \\ { { \displaystyle f ^ { ( 2 ) } ( \lambda ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( \lambda ^ { T } g ( X _ { i } , \theta ) ) g ( X _ { i } , \theta ) g ( X _ { i } , \theta ) ^ { T } . } } \end{array}
$$

By Assumption A.2’, B.1 and B.2’, there exists a positive constant $a _ { 1 }$ such that for any $\| \lambda \| _ { 2 } \leq C$ , it holds that

$$
f ^ { ( 2 ) } ( \lambda ) \succcurlyeq a _ { 1 } I _ { d } .
$$

Moreover, for any $\| \lambda \| _ { 2 } \leq C$ and $l \in \mathbb { S } ^ { d - 1 }$ there exists a $\lambda ^ { \prime }$ depend on $\lambda$ and $l$ such that $\| \lambda ^ { \prime } \| _ { 2 } \leq C$ and

$$
f ^ { ( 1 ) } ( \lambda ) ^ { T } l = f ^ { ( 1 ) } ( \lambda ( \theta ) ) ^ { T } l + ( \lambda - \lambda ( \theta ) ) ^ { T } f ^ { ( 2 ) } ( \lambda ^ { \prime } ) l .
$$

So we can get

$$
\begin{array} { r l } & { \| f ^ { ( 1 ) } ( \widetilde { \lambda } ( \boldsymbol { \theta } ) ) \| _ { 2 } \ge \underset { l \in \mathbb S ^ { d - 1 } } { \operatorname* { s u p } } \underset { \mathbb { 1 } \sqcup \mathbb { 2 } } { \operatorname* { i n f } } \vert ( \widetilde { \lambda } ( \boldsymbol { \theta } ) - \lambda ( \boldsymbol { \theta } ) ) ^ { T } f ^ { ( 2 ) } ( \lambda ) l \vert } \\ & { \qquad \ge \underset { \underset { \Vert \boldsymbol { \lambda } \in \mathbb R ^ { d } } { \operatorname* { i n f } } } { \operatorname* { i n f } } \left| \frac { ( \widetilde { \lambda } ( \boldsymbol { \theta } ) - \lambda ( \boldsymbol { \theta } ) ) ^ { T } f ^ { ( 2 ) } ( \lambda ) ( \widetilde { \lambda } ( \boldsymbol { \theta } ) - \lambda ( \boldsymbol { \theta } ) ) } { \Vert \widetilde { \lambda } ( \boldsymbol { \theta } ) - \lambda ( \boldsymbol { \theta } ) \Vert _ { 2 } } \right| } \\ & { \qquad \ge a _ { 1 } \Vert \widetilde { \lambda } ( \boldsymbol { \theta } ) - \lambda ( \boldsymbol { \theta } ) \Vert _ { 2 } . } \end{array}
$$

We can then get for any $\theta \in B _ { r _ { 0 } } ( \theta ^ { * } )$ ,

$$
\lVert \tilde { \lambda } ( \theta ) - \lambda ( \theta ) \rVert _ { 2 } \lesssim \lVert \theta - \theta ^ { * } \rVert _ { 2 } ^ { 2 } + \sqrt { \frac { \log n } { n } } \lVert \theta - \theta ^ { * } \rVert _ { 2 } ^ { \beta } + \frac { \log n } { n } .
$$

# D.6 Proof of Corollary 2

Recall $\ell ( X , \theta ) = ( Y - \tilde { X } ^ { T } \theta ) ( \tau - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } )$ and $g ( X , \theta ) = ( \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \tau ) \tilde { X }$ . We first prove that the statement in Assumption B.1 is satisfied. Since

$$
\mathcal { R } ( \theta ) = \mathbb { E } \tau ( Y - \tilde { X } ^ { T } \theta ) - \mathbb { E } _ { \tilde { X } } \int _ { - \infty } ^ { \tilde { X } ^ { T } \theta } ( Y - \tilde { X } ^ { T } \theta ) p ( Y | \tilde { X } ) d Y .
$$

We can get

$$
\nabla \mathcal { R } ( \theta ) = - \tau \mathbb { E } \tilde { X } + \mathbb { E } _ { \tilde { X } } \int _ { - \infty } ^ { \tilde { X } ^ { T } \theta } p ( Y | \tilde { X } ) \tilde { X } d Y = \mathbb { E } g ( X , \theta ) .
$$

So we have

$$
\mathcal { H } _ { \theta } = \mathbb { E } _ { \tilde { X } } p ( \tilde { X } ^ { T } \theta | \tilde { X } ) \tilde { X } \tilde { X } ^ { T }
$$

Then by the assumption that $p ( t | \tilde { X } )$ is bounded and has bounded derivative w.r.t. $t$ over $t \in \mathbb R$ and $\tilde { X } \in \tilde { { \mathcal { X } } }$ and the assumption that the support of $\tilde { X }$ is compact, we can get that ${ \mathcal { R } } ( \theta )$ is bounded and has bounded derivatives w.r.t. $\theta$ up to order three. Moreover, the boundness of $\ell ( X , \theta )$ and $g ( X , \theta )$ is guaranteed by the compactness of supports of $\ddot { X }$ and $Y$ . In addition, there exists a constant $c$ such that for any $\tilde { X } \in \tilde { \mathcal { X } }$ and $\theta , \theta ^ { \prime } \in \Theta$ it holds that,

$$
\begin{array} { r l } & { \mathbb { E } _ { Y | \tilde { X } } ( \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta ^ { \prime } } ) ^ { 2 } } \\ & { = \mathbb { E } _ { Y | \tilde { X } } ( \mathbf { 1 } _ { \tilde { X } ^ { T } \theta ^ { \prime } \leq Y < \tilde { X } ^ { T } \theta } + \mathbf { 1 } _ { \tilde { X } ^ { T } \theta \leq Y < \tilde { X } ^ { T } \theta ^ { \prime } } ) } \\ & { \leq c \| \theta - \theta ^ { \prime } \| _ { 2 } . } \end{array}
$$

So there exists a constant $c _ { 1 }$ such that

$$
\begin{array} { r l } & { \| \boldsymbol { \Delta } _ { \theta } - \boldsymbol { \Delta } _ { \theta ^ { * } } \| _ { \mathrm { F } } } \\ & { \leq \| \mathbb { E } \tilde { X } \tilde { X } ^ { T } ( \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta ^ { * } } ) \| _ { \mathrm { F } } } \\ & { \ \leq \| \mathbb { E } _ { \tilde { X } } \tilde { X } \tilde { X } ^ { T } \mathbb { E } _ { Y | \tilde { X } } | \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta ^ { * } } | \| _ { \mathrm { F } } } \\ & { \leq c _ { 1 } \| \theta - \theta ^ { * } \| _ { 2 } . } \end{array}
$$

For the Assumption B.2, Define

$$
\begin{array} { r l } & { d _ { n } ^ { g } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } \| g ( X _ { i } , \theta ) - g ( X _ { i } , \theta ^ { \prime } ) \| _ { 2 } ^ { 2 } } , } \\ & { d _ { n } ^ { \ell } ( \theta , \theta ^ { \prime } ) = \sqrt { \frac { 1 } { n } \displaystyle \sum _ { i = 1 } ^ { n } ( \ell ( X _ { i } , \theta ) - \ell ( X _ { i } , \theta ^ { \prime } ) ) ^ { 2 } } . } \end{array}
$$

By Lemma 9.12 and Lemma 9.8 of Kosorok [2008], we know the function class ${ \mathcal F } =$ $\left\{ \mathbf { 1 } _ { Y \leq \theta ^ { T } \tilde { X } } , \theta \in \Theta \right\}$ is a VC-class, so by Theorem 8.3.18 of Vershynin [2018] and the fact

that the $\varepsilon$ -covering number of $B _ { 1 } ( 0 )$ with respect to $\ell _ { 2 }$ norm is upper bounded by $\left( \frac { 3 } { \varepsilon } \right) ^ { d }$ , we can get that

$$
\begin{array} { l } { \log \mathcal { N } ( \Theta , d _ { n } ^ { g } , \varepsilon ) \lesssim \log \frac { 1 } { \varepsilon } } \\ { \log \mathcal { N } ( \Theta , d _ { n } ^ { \ell } , \varepsilon ) \lesssim \log \frac { 1 } { \varepsilon } . } \end{array}
$$

Moreover, by equation (26), there exist some constants $\left( c , c _ { 1 } \right)$ such that for any $\theta , \theta ^ { \prime } \in \Theta$ it holds that,

$$
\begin{array} { r l } & { \sqrt { \mathbb { E } ( g ( X , \theta ) - g ( X , \theta ^ { \prime } ) ) ^ { T } ( g ( X , \theta ) - g ( X , \theta ^ { \prime } ) ) } } \\ & { = \sqrt { \mathbb { E } \tilde { X } ^ { T } \tilde { X } ( \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta ^ { \prime } } ) ^ { 2 } } } \\ & { \leq c \| \theta - \theta ^ { \prime } \| _ { 2 } ^ { \frac { 1 } { 2 } } } \end{array}
$$

$$
\begin{array} { r l } & { \sqrt { \mathbb { E } ( \ell ( X , \theta ) - \ell ( X , \theta ^ { \prime } ) ) ^ { 2 } } } \\ & { \leq c _ { 1 } \left( \| \theta - \theta ^ { \prime } \| _ { 2 } + \sqrt { \mathbb { E } ( \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta } - \mathbf { 1 } _ { Y < \tilde { X } ^ { T } \theta ^ { \prime } } ) ^ { 2 } } \right) } \\ & { \leq c \| \theta - \theta ^ { \prime } \| _ { 2 } ^ { \frac { 1 } { 2 } } } \end{array}
$$

Then, we can get the statement of Assumption B.2 with $\beta = \textstyle { \frac { 1 } { 2 } }$ . The desired conclusion is then followed by Theorem 3.

# D.7 Proof of Corollary 3

Recall that $\begin{array} { r } { \ell ( X , \theta ) = \frac { 1 } { 2 } \lambda \theta ^ { T } \theta + \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } ( 1 - Y \theta ^ { T } \tilde { X } ) } \end{array}$ and $g ( X , \theta ) = \lambda \theta - Y \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } \tilde { X }$ . Since

$$
\mathfrak { L } ( \theta ) = \mathbb { P } ( Y = 1 ) \mathbb { E } _ { \tilde { X } | Y = 1 } ( ( 1 - \theta ^ { T } \tilde { X } ) \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \geq 1 } ) + \mathbb { P } ( Y = - 1 ) \mathbb { E } _ { \tilde { X } | Y = - 1 } ( ( 1 + \theta ^ { T } \tilde { X } ) \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \geq - 1 } ) + \mathbb { P } ( Y = - 1 ) \mathbb { E } _ { \tilde { X } | Y = 0 } ( \mathfrak { L } ( \tilde { X } ) \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \geq - 1 } ) .
$$

We now prove the thirce differentiability of ${ \mathcal { R } } ( \theta )$ , choose any $\theta = ( \theta _ { 1 } , \cdot \cdot \cdot , \theta _ { d } ) \in \Theta$ , w.l.o.g, we can assume $\theta _ { 1 } , \cdots , \theta _ { d } > 0$ . Since for any $1 \leq j \leq d$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \tilde { X } | Y = 1 } ( ( 1 - \theta ^ { T } \tilde { X } ) { \bf 1 } _ { \theta ^ { T } \tilde { X } \le 1 } ) } \\ & { = \mathbb { E } _ { \tilde { X } _ { - j } | Y = 1 } \int _ { \tilde { X } _ { j } \le \frac { 1 - \sum _ { k \neq j } \theta _ { k } \tilde { X } _ { k } } { \theta _ { j } } } ( 1 - \displaystyle \sum _ { k \neq j } \theta _ { k } \tilde { X } _ { k } - \theta _ { j } \tilde { X } _ { j } ) P _ { 1 } ^ { j } ( \tilde { X } _ { j } ) d \tilde { X } _ { j } } \end{array}
$$

We can get

$$
\begin{array} { r l } & { \nabla \mathcal { R } ( \theta ) = \lambda \theta - \mathbb { P } ( Y = 1 ) \mathbb { E } _ { \tilde { X } | Y = 1 } \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \leq 1 } \tilde { X } + \mathbb { P } ( Y = - 1 ) \mathbb { E } _ { \tilde { X } | Y = - 1 } \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \geq - 1 } \tilde { X } } \\ & { \ = - \mathbb { E } Y \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } \tilde { X } + \lambda \theta } \\ & { = \mathbb { E } g ( X , \theta ) . } \end{array}
$$

Moreover, for any $1 \leq i \leq d$

$$
\begin{array} { r l } & { \displaystyle \frac { \partial ^ { 2 } \mathcal { R } ( \theta ) } { \partial \theta _ { i } ^ { 2 } } = \lambda + \mathbb { P } ( Y = 1 ) \mathbb { E } _ { \tilde { X } _ { - i } | Y = 1 } \left( \frac { ( 1 - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) ^ { 2 } } { \theta _ { i } ^ { 3 } } p _ { 1 } ^ { i } \big ( ( 1 - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) / \theta _ { i } \big ) \right) } \\ & { \displaystyle + \mathbb { P } ( Y = - 1 ) \mathbb { E } _ { \tilde { X } _ { - i } | Y = - 1 } \left( \frac { ( 1 + \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) ^ { 2 } } { \theta _ { i } ^ { 3 } } p _ { - 1 } ^ { i } \big ( ( - 1 - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } ) / \theta _ { i } \big ) \right) . } \end{array}
$$

when $1 \leq i \neq j \leq d$ ,

$$
\begin{array} { r l } & { \frac { \partial ^ { 2 } \mathcal { R } ( \theta ) } { \partial \theta _ { i } \theta _ { j } } = \mathbb { P } ( Y = 1 ) \mathbb { E } _ { \tilde { X } _ { - i } | Y = 1 } \left( \frac { \tilde { X } _ { j } \bigl ( 1 - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } \bigr ) } { \theta _ { i } ^ { 2 } } p _ { 1 } ^ { i } \bigl ( \bigl ( 1 - \underset { k \neq i } { \overset { d } { \sum } } \theta _ { k } \tilde { X } _ { k } \bigr ) / \theta _ { i } \bigr ) \right) } \\ & { + \mathbb { P } ( Y = - 1 ) \mathbb { E } _ { \tilde { X } _ { - i } | Y = - 1 } \left( \frac { \tilde { X } _ { j } \bigl ( - 1 - \sum _ { k \neq i } ^ { d } \theta _ { k } \tilde { X } _ { k } \bigr ) } { \theta _ { i } ^ { 2 } } p _ { - 1 } ^ { i } \bigl ( \bigl ( - 1 - \underset { k \neq i } { \overset { d } { \sum } } \theta _ { k } \tilde { X } _ { k } \bigr ) / \theta _ { i } \bigr ) \right) . } \end{array}
$$

Then by Assumption B.s, it holds that ${ \mathcal { R } } ( \theta )$ is bounded and has bounded derivatives w.r.t. $\theta$ up to order three. Moreover, the boundness of $\ell ( X , \theta )$ and $g ( X , \theta )$ is guaranteed by the compactness of $\Theta$ and $\ddot { \mathcal X }$ . In addition, there exist some constants $( c , c _ { 0 } , c _ { 1 } , c _ { 2 } )$ such that

$$
\begin{array} { r l } & { \| \Delta _ { \theta } - \Delta _ { \theta ^ { \prime } } \| _ { \mathrm { F } } } \\ & { \leq \| \mathbb { E } ( \tilde { X } \tilde { X } ^ { T } | \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } - \mathbf { 1 } _ { Y \theta ^ { \prime } \tilde { X } \leq 1 } | ) \| _ { F } + c _ { 0 } \| \mathbb { E } ( \tilde { X } | \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } - \mathbf { 1 } _ { Y \theta ^ { \prime \prime } \tilde { X } \leq 1 } | ) \| _ { 2 } + c \| \theta - \theta ^ { \prime } \| } \\ & { \leq c _ { 1 } ( \mathbb { E } _ { \tilde { X } | Y = 1 } | \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \leq 1 } - \mathbf { 1 } _ { \theta ^ { \prime \prime } \tilde { X } \leq 1 } | + \mathbb { E } _ { \tilde { X } | Y = - 1 } | \mathbf { 1 } _ { \theta ^ { T } \tilde { X } \geq - 1 } - \mathbf { 1 } _ { \theta ^ { \prime \prime } \tilde { X } \geq - 1 } | ) + c \| \theta - \theta ^ { \prime } \| _ { 2 } } \\ & { \leq c _ { 2 } \| \theta - \theta ^ { \prime } \| _ { 2 } . } \end{array}
$$

So the statement in Assumption B.1 holds. For the Assumption B.2, there exists a constant $c$ such that for any $\theta , \theta ^ { \prime } \in \Theta$ ,

$$
\begin{array} { r l } & { \sqrt { \mathbb { E } ( g ( X , \theta ) - g ( X , \theta ^ { \prime } ) ) ^ { T } ( g ( X , \theta ) - g ( X , \theta ^ { \prime } ) ) } } \\ & { = \sqrt { \mathbb { E } ( | \mathbf { 1 } _ { Y \theta ^ { T } \bar { X } \leq 1 } - \mathbf { 1 } _ { Y \theta ^ { T } \bar { X } \leq 1 } | \tilde { X } ^ { T } \tilde { X } ) + \lambda ^ { 2 } \| \theta - \theta ^ { \prime } \| _ { 2 } ^ { 2 } - 2 \mathbb { E } ( \lambda Y ( \mathbf { 1 } _ { Y \theta ^ { T } \bar { X } \leq 1 } - \mathbf { 1 } _ { Y \theta ^ { T } \bar { X } \leq 1 } ) ( \theta - \theta ^ { \prime } ) ) } } \\ & { \leq c \| \theta - \theta ^ { \prime } \| _ { 2 } ^ { \frac { 1 } { 2 } } . } \end{array}
$$

Then combined with the fact that $\mathcal { F } = \{ \mathbf { 1 } _ { Y \theta ^ { T } \tilde { X } \leq 1 } , \theta \in \Theta \}$ is a VC-class and $\ell ( X , \theta )$ is uniformly Lipschitz continuous w.r.t $\theta$ , similar as the proof of Corollary 2, we can get that Assumption B.2 is satisfied with $\beta = \textstyle { \frac { 1 } { 2 } }$ . The desired conclusion is then followed by Theorem 3.