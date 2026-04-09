# Minimax Optimal Rates for Regression on Manifolds and Distributions

Rong Tang∗ and Yun Yang†

∗Department of Mathematics, Hong Kong University of Science and Technology †Department of Mathematics, University of Maryland, College Park

# Abstract

Distribution regression seeks to estimate the conditional distribution of a multivariate response given a continuous covariate. This approach offers a more complete characterization of dependence than traditional regression methods. Classical nonparametric techniques often assume that the conditional distribution has a well-defined density, an assumption that fails in many real-world settings. These include cases where data contain discrete elements or lie on complex low-dimensional structures within high-dimensional spaces. In this work, we establish minimax convergence rates for distribution regression under nonparametric assumptions, focusing on scenarios where both covariates and responses lie on low-dimensional manifolds. We derive lower bounds that capture the inherent difficulty of the problem and propose a new hybrid estimator that combines adversarial learning with simultaneous least squares to attain matching upper bounds. Our results reveal how the smoothness of the conditional distribution and the geometry of the underlying manifolds together determine the estimation accuracy.

Keywords: Conditional distribution estimation; Manifold learning; Distribution regression; Minimax rate; Conditional generative models; Adversarial learning.

# Contents

1 Introduction 3   
1.1 Related Work 4   
1.2 Main Contribution 5

# Background and preliminary results 7

2.1 Notation 7   
2.2 Functions with separate smoothness 7   
2.3 Smooth manifolds and covariate-dependent manifolds . 9

# Minimax Rate for Distribution Regression with Covariate-independent Response Space 10

3.1 Density regression in Euclidean spaces 11   
3.2 Distribution regression with low-dimensional manifold structures 13

# Minimax Rate for Distribution Regression with Covariate-dependent Response Space 15

4.1 Manifold regression 15   
4.2 Distribution regression with covariate-dependent manifolds 17

# Minimax Optimal Estimators for Distribution Regression 20

5.1 Minimax optimal estimator for Euclidean response space 20   
5.2 Minimax optimal estimator for manifold response space . 22   
5.2.1 Estimator for coarse-scale component $\cdot$ 23   
5.2.2 Estimator for fine-scale component $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ 24   
5.2.3 Convergence rate of the estimator for $\cdot$ 25

# 6 Discussion 27

# A Omitted Definitions and Results in Main Text 34

A.1 Smooth Submanifold 34   
A.2 Smooth submanifold family and smooth conditional distributions 36   
A.3 Wavelet 37   
A.4 Matching error for Joint Mean Regression 39

# Details of Miniax Optimal Estimators

# 40

B.1 Minimax Optimal Estimator for Regime 1 40   
B.2 Minimax Optimal Estimator for Regime 2 40   
B.2.1 Density regression in the ambient space 40   
B.2.2 Density regression in the latent space 42   
B.2.3 Simultaneous minimax optimal estimator for $\cdot$ 43   
B.3 Minimax Optimal Estimator for Regime 3b 44

# C Proof for Distribution Regression with Euclidean Response 46

C.1 Proof of Theorem 5 (minimax upper bound for Regime 1) . 46   
C.2 Proof of Theorem 1 (minimax lower bound for Regime 1) 47   
C.2.1 Proof for the lower bound of $ { n } ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } }$ 47   
αX   
C.2.2 Proof for the lower bound of $\cdot$ 49   
C.3 Proof of Lemma 9 . 51   
C.4 Proof of Lemma 11 52

# D Proof for Distribution Regression with Manifold Responses 55

D.1 Proof of Theorem 9 55   
D.2 Proof of Theorem 10 56   
D.3 Proof of Theorem 6 (minimax upper bound for Regime 2 and 3b) 60   
D.3.1 Proof for Regime 2 60   
D.3.2 Proof for Regime 3b 65   
D.4 Proof of Theorem 2 (minimax lower bound for Regime 2) 70   
D.5 Proof of Theorem 4 (minimax lower bound for Regime 3b) 71   
D.6 Proof of Corollary 1 and Corollary 2 75   
D.7 Proof of Lemma 12 76   
D.8 Proof of Lemma 13 80   
D.9 Proof of Lemma 14 83   
D.10 Proof of Lemma 15 90   
D.11 Proof of Lemma 16 93   
D.12 Proof of Lemma 17 95   
D.13 Proof of Lemma 18 99   
D.14 Proof of Lemma 19 101   
D.15 Proof of Lemma 20 112   
D.16 Proof of Lemma 21 113

# E Proof of Technical Details 115

E.1 Proof of Lemma 7 115   
E.2 Proof of Lemma 1 117   
E.3 Proof of Lemma 8 118   
E.4 Proof of Lemma 2 . 119   
E.5 Proof of Lemma 3 123   
E.5.1 $( 3 ) \Rightarrow ( 2 )$ 123   
E.5.2 $\cdot$ (1) 127   
E.5.3 $\cdot$ (3) 128   
E.6 Proof of Lemma 4 129   
E.7 Proof of Lemma 5 . 130   
E.8 Proof of Lemma 6 . 135   
E.9 Proof of Lemma 10 136   
E.10 Proof of Theorem 8 137   
E.11 Proof of Theorem 3 140   
E.11.1 Proof of Lemma 22 144   
E.11.2 Proof of Lemma 23 148

# 1 Introduction

Distribution regression (or more precisely, distribution-on-vector regression), where the goal is to estimate the conditional distribution $\mu _ { Y | X } ^ { * }$ of a random response vector $Y \in \mathbb { R } ^ { D _ { Y } }$ given a continuous covariate $X \in \mathbb { R } ^ { D _ { X } }$ , is a fundamental problem in statistics and machine learning. Unlike traditional regression [Christensen et al., 2002, Hardle ¨ , 1990, Koenker, 2005] or classification [Bishop, 2006], which typically involves a univariate response (i.e., $D _ { Y } ~ = ~ 1 $ ) and predicts scalar or categorical outcomes, distribution regression aims to recover the full conditional distribution of a potentially multivariate response, providing a more comprehensive characterization of the dependence between $X$ and $Y$ [DiNardo and Tobias, 2001], which may represent complex objects encoded or embedded as numerical vectors, including images, texts, or other structured data. In particular, distribution regression allows for capturing how $\mu _ { Y \mid X = x }$ evolves as the covariate $x$ varies, enabling a richer understanding of conditional variability, skewness, uncertainty and multiple-modality [Rodr´ıguez-Alvarez et al. ´ , 2025]. This framework is especially important in applications where characterizing the entire distribution, rather than just its mean or quantiles, is crucial, such as in biomedical sciences [Krishnaswamy et al., 2014], climate modeling [Guinness and Hammerling, 2018] and econometrics [Li and Racine, 2007].

There is a vast literature on nonparametric density regression (conditional density estimation), where the conditional distribution $\mu _ { Y \mid X } ^ { * }$ is assumed to have a density function with respect to the Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ . However, many existing methods, particularly classical nonparametric estimators based on kernel smoothing [Bashtannyk and Hyndman, 2001, Izbicki and Lee, 2016, Li et al., 2022b], have several notable limitations. A primary drawback of these approaches is their reliance on the existence of a conditional density function, an assumption that often fails when the response variable $Y$ contains discrete components or is embedded in a high-dimensional ambient space with low-dimensional singular structures, as is common in structured data environments [Wang et al., 2020, Bellet et al., 2013]. As a consequence, these methods are primarily effective in low-dimensional settings but struggle as dimensionality increases, ultimately suffering from the curse of dimensionality [Pope et al., 2021, Latorre et al., 2021]. Furthermore, classical density regression methods generally lack adaptability to the intrinsic geometric structure of data, such as underlying manifold structures that are common in modern high-dimensional datasets [Gong et al., 2019, Aghajanyan et al., 2020]. This inability to exploit lowdimensional representations limits their effectiveness in capturing complex dependencies and accurately modeling conditional distributions in modern data environments, which often involve high-dimensional, complex data such as images in computer vision [Parker, 2010], medical imaging [Suetens, 2017], and signal processing [Franc¸a et al., 2021], as well as text in data mining [Zhai and Massung, 2016], natural language processing [Kao and Poteet, 2007], and public health [Yang et al., 2022].

These limitations of classical density regression motivate us to study the statistical properties of distribution regression, which can accommodate general data types and singular distributions. In particular, the recent surge in conditional generative models—such as conditional generative adversarial networks [Mirza and Osindero, 2014], conditional diffusion models [Song et al., 2021, Zhang et al., 2023], and conditional normalizing flows [Abdelhamed et al., 2019, Winkler et al., 2019]—demonstrates their effectiveness and efficiency in generating new data given a covariate (or control variable) in complex environments. These models approximate complex conditional distributions by learning the underlying data-generating processes, making them powerful tools for tasks such as image-to-image translation [Isola et al., 2017], medical image synthesis [Dar et al., 2019], and super-resolution imaging [Zhao et al., 2019]. Consequently, conditional generative models can be regarded as implicit distribution regression methods, as they do not explicitly estimate the conditional density or cumulative distribution function but instead generate samples that follow the underlying conditional distribution. However, despite their empirical success, the theoretical understanding of their statistical properties remains limited. In particular, it is unclear how well these models approximate the true conditional distribution and under what conditions they achieve optimal performance. This gap highlights the need to establish rigorous theoretical guarantees for distribution regression, particularly in terms of minimax rates, to provide a deeper understanding of the fundamental limits of learning conditional distributions.

In this work, we investigate the minimax convergence rates for distribution regression under nonparametric settings, where both the response variable $Y$ and the covariate $X$ may be high-dimensional but possess an underlying low-dimensional manifold structure. This setting is particularly relevant for modern conditional generative models using deep neural networks [Sohn et al., 2015, Salakhutdinov, 2015], as many complex data types—such as images, text, and other structured objects—reside on lowdimensional manifolds despite being represented in high-dimensional ambient spaces. Moreover, deep neural networks are naturally suitable for learning low-dimensional nonlinear features, making them inherently adaptive to such data structures [Schmidt-Hieber, 2019, Kohler and Langer, 2021, Schmidt-Hieber, 2020]. Unlike the unconditional distribution estimation setting (e.g., Tang and Yang [2023a]), where the data is supported on a single manifold, the conditional distribution setting is more intricate. Both the covariate $X$ and the response $Y$ can reside on distinct manifolds, and more importantly, the manifold supporting $Y$ may depend on $X$ . This dependence transforms the problem of recovering the support of $Y$ into a manifold regression problem, which is highly nontrivial and remains largely unexplored in the existing literature.

Concretely, we consider a random design distribution regression setting where the covariate $X$ follows a marginal distribution $\mu _ { X } ^ { * }$ supported on a $d _ { X }$ -dimensional submanifold $\mathcal { M } _ { X }$ within the ambient covariate space $\mathbb { R } ^ { D _ { X } }$ . Furthermore, our target of interest, the conditional distribution $\mu _ { Y \mid X = x } ^ { * }$ of $Y$ given $X = x$ , is supported on a $d _ { Y }$ -dimensional, $\beta _ { Y }$ -smooth submanifold $\mathcal { M } _ { Y \mid x }$ (c.f. Definition 3) within the ambient response space $\mathbb { R } ^ { D _ { Y } }$ , which may or may not vary with $x$ . In cases where $\mathcal { M } _ { Y \mid x }$ depends on $x$ , we assume that its dependence on $x$ is $\beta _ { X }$ -smooth (c.f. Definition 4). We also assume that $\mu _ { Y \mid X = x } ^ { * }$ admits a density function with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ that is $\alpha _ { Y }$ -smooth in $y$ and $\alpha _ { X ^ { - } }$ smooth in $x$ (c.f. Definition 1). The data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ consists of $n$ i.i.d. copies of $( X , Y )$ sampled from the joint distribution $\mu _ { X Y } ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ .To quantify the estimation error, we follow Tang and Yang [2023b] and use the integral probability metric (IPM) [Muller ¨ , 1997], also known as the adversarial loss in the machine learning literature (e.g., Singh et al. [2018]), to measure the closeness between two probability measures, which may be mutually singular in our setting. In particular, we consider the $\gamma$ -Holder ¨ IPM, denoted as $d _ { \gamma }$ , which is indexed by a smoothness parameter $\gamma \geq 0$ that regulates the strength of the metric and balances the trade-off between distribution support mismatch and relative density differences over the support (c.f. equation(1) and the subsequent discussion). Notably, the $d _ { \gamma }$ metric includes classical total variation distance $\langle \gamma = 0 \rangle$ ) and 1-Wasserstein distance $W _ { 1 }$ $( \gamma = 1 )$ ) as special cases.

# 1.1 Related Work

There is a vast literature on nonparametric density regression in both the statistics and machine learning communities, where proposed estimators range from classical nonparametric methods based on kernel smoothing [Rosenblatt, 1969, Fan and Yim, 2004, Holmes et al., 2007, Bashtannyk and Hyndman, 2001,

Izbicki and Lee, 2016, Li et al., 2022b] to Bayesian nonparametric approaches [Norets and Pati, 2017] and more recent methods leveraging deep neural networks [Rothfuss et al., 2019]. These works mostly consider the classical setting where the dimension $D _ { X }$ of the covariate $X$ is low and the conditional distribution $\mu _ { Y | X = } ^ { * }$ · admits a density function, corresponding to our setting with $d _ { X } = D _ { X }$ , $d _ { Y } = D _ { Y }$ , $\mathcal { M } _ { X } = \mathbb { R } ^ { D _ { X } }$ , $\dot { \mathcal { M } } _ { Y | x } = \mathbb { R } ^ { D _ { Y } }$ for each $x \in \mathbb { R } ^ { D _ { X } }$ , and $\beta _ { X } = \beta _ { Y } = \infty$ . In this classical setting, Li et al. [2022b] establish the minimax rate of conditional density estimation as $n ^ { - 1 / ( 2 + D _ { X } / \alpha _ { X } + D _ { Y } / \alpha _ { Y } ) }$ under the total variation metric (corresponding to the $d _ { 0 }$ IPM) when $\alpha _ { X } \in [ 0 , 1 ]$ . Bilodeau et al. [2023] studies the minimax rate for conditional density estimation under the Kullback-Leibler (KL) risk, providing both upper and lower bounds expressed in terms of empirical Hellinger entropy.

Recent work has also addressed statistical inference problems involving manifolds. Several studies [Tang and Yang, 2023b, Ozakin and Gray, 2009, Berenfeld et al., 2024, Berenfeld and Hoffmann, 2021, Cholaquidis et al., 2022, Divol, 2022] focus on the problem of (unconditional) distribution estimation on an unknown manifold. Notably, Tang and Yang [2023b] derives the minimax rate $n ^ { - 1 / 2 } +$ $n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } ) } + n ^ { - \gamma \beta _ { Y } / d _ { Y } }$ for estimating an $\alpha _ { Y }$ -smooth distribution supported on a $d _ { Y }$ -dimensional, $\beta _ { Y }$ -smooth $( \beta _ { Y } \ge \alpha _ { Y } + 1 )$ manifold $\mathcal { M } _ { Y } \subset \mathbb { R } ^ { D _ { Y } }$ with respect to the $d _ { \gamma }$ metric for all $\gamma \geq 0$ . Under a similar setting, Divol [2022] shows that the minimax rate under the $p$ -Wasserstein distance is $n ^ { - 1 / 2 } + n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } ) }$ for any $p > 0$ . Some other studies [Genovese et al., 2012b,c, Divol, 2021, Aamari and Levrard, 2019] consider the problem of manifold estimation, which corresponds to support recovery for singular distributions. For instance, Aamari and Levrard [2019] establishes that the minimax rate for estimating a boundaryless, $\beta _ { Y }$ -smooth $\beta _ { Y } \geq 2  ,$ ), $d _ { Y }$ -dimensional submanifold under the Hausdorff distance is $\dot { n } ^ { - \beta _ { Y } / d _ { Y } }$ .

There has been a recent line of work leveraging generative models, such as generative adversarial networks (GAN) and diffusion models, for implicit (conditional) distribution estimation via sampling, such as Oko et al. [2023], Chen et al. [2023a], Wang et al. [2024], Li and Yan [2024], De Bortoli et al. [2021], Lee et al. [2022], Chen et al. [2022], Lee et al. [2023], Chen et al. [2023b], Tang and Yang [2024], Li et al. [2024b], Zhou et al. [2022], Liu et al. [2021], Chen et al. [2024], Fu et al. [2024], Li et al. [2024a], Azangulov et al. [2024], Tang et al. [2025]. To name a few most relevant to our problem, in the unconditional distribution estimation case of estimating the distribution $\mu _ { Y } ^ { * }$ without covariate $X$ , Oko et al. [2023] show that diffusion models can achieve the respective minimax rate $n ^ { - 1 / ( 2 + D _ { Y } / \alpha _ { Y } ) }$ under the total variation metric and $n ^ { - ( 1 + 1 / \alpha _ { Y } ) / ( 2 + D _ { Y } / \alpha _ { Y } ) }$ under the $W _ { 1 }$ distance. Furthermore, Tang and Yang [2024] extend the results of Oko et al. [2023] to the manifold setting and derive a convergence rate $n ^ { - 1 / 2 } + n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } ) } + n ^ { - \gamma \beta _ { Y } / ( 2 \alpha _ { Y } + d _ { Y } ) }$ under the $d _ { \gamma }$ distance, showing that diffusion models are minimax-optimal at least when $\gamma \in \ [ 0 , 1 ]$ , covering the total variation distance and the $W _ { 1 }$ distance. In the conditional generative model setting, Zhou et al. [2022] propose a conditional GANbased approach [Mirza and Osindero, 2014] and establish the consistency of the resulting conditional density estimator, though no convergence rates or error bounds are provided. Meanwhile, Liu et al. [2021] adopt a Wasserstein generative approach for conditional distribution estimation and derive a convergence rate of $n ^ { - 1 / ( 1 + D _ { X } + D _ { Y } ) }$ under the $W _ { 1 }$ distance (corresponding to the $d _ { 1 }$ IPM). For conditional diffusion models, Chen et al. [2024] provides a recent survey of related theoretical investigations on conditional score estimation and the resulting sample complexity. Among the most relevant works to ours, Fu et al. [2024] explore the theoretical properties of conditional diffusion models under the classical setting without a manifold structure and derive a convergence rate of $n ^ { - \alpha _ { Y } / ( 2 \alpha _ { Y } + D _ { X } + D _ { Y } ) }$ relative to the total variation distance, under the special case where the conditional distribution has the same smoothness level in $X$ and $Y$ , i.e., $\alpha _ { X } = \alpha _ { Y }$ . More recently, Tang et al. [2025] consider the manifold setting and derive a convergence rate of $n ^ { - \alpha _ { X } / ( 2 \alpha _ { X } + d _ { X } ) } + n ^ { - ( \alpha _ { Y } + \hat { 1 } ) / ( 2 \alpha _ { Y } + d _ { Y } + d _ { X } \alpha _ { Y } / \alpha _ { X } ) }$ relative to the $W _ { 1 }$ distance for conditional diffusion models when all manifolds are sufficiently smooth.

# 1.2 Main Contribution

In this work, we investigate the minimax convergence rates for distribution regression under nonparametric settings. We derive lower bounds that characterize the fundamental difficulty of the problem and provide matching upper bounds achieved by a new hybrid estimator combining adversarial learning and simultaneous least squares estimation. Our results reveal how the smoothness of the conditional distribution and the geometric properties of the underlying manifolds influence estimation accuracy. Moreover, we extend our analysis to the case where both the response variable and the covariate are high-dimensional but admit an underlying low-dimensional manifold structure. This setting is highly relevant, as many complex data types—such as images, text, and other structured objects—lie on lowdimensional manifolds despite being represented in high-dimensional ambient spaces. Since conditional generative models are particularly effective in modeling such complex data distributions, understanding the minimax rates in this setting provides valuable insights into the theoretical foundations of generative modeling.

By developing a rigorous theoretical framework, our results precisely characterize the statistical complexity of the problem and establish benchmarks for evaluating the performance of modern conditional generative models. This is particularly relevant in high-dimensional settings, where leveraging low-dimensional structures enhances statistical efficiency. Specifically, our main results on the minimax rate across different regimes are summarized below. For all regimes considered, we assume that the covariant space $\mathcal { M } _ { X }$ exhibits a low-dimensional structure with an intrinsic/effective dimension of $d _ { X }$ (c.f. Definition 5). The minimax rates are presented excluding logarithmic factors.

Regime 1. Classic density regression. In this setting, the conditional distribution $\mu _ { Y \mid X } ^ { * }$ is assumed to admit a density with respect to the Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ . The minimax convergence rate takes the form n−αX/(2αX+dX) + n−(αY +γ)/(2αY +DY + αYαX dX). The first term corresponds to the classical minimax rate for estimating an $\alpha _ { X }$ -smooth regression function under the $L ^ { 2 }$ loss, as established by Stone [1982]. The second term captures the inherent difficulty of nonparametric conditional density estimation. Notably, when $\alpha _ { X } \in [ 0 , 1 ]$ and $\gamma = 0$ , the rate coincides with the minimax rate for conditional density estimation under the total variation metric derived in Li et al. [2022b].

Regime 2. Distribution regression with covariate-independent response space. In this regime, the support $\mathcal { M } _ { Y \mid X }$ of the conditional distribution $\mu _ { Y | X } ^ { * }$ is assumed to be independent of $X$ , with a common support $\mathcal { M } _ { Y | X } = \mathcal { M } _ { Y }$ that is an unknown $\beta _ { Y }$ -smooth submanifold of intrinsic dimension $d _ { Y }$ . The minimax rate for this setting is $n ^ { - \alpha _ { X } / ( 2 \alpha _ { X } + d _ { X } ) } + n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } ) } +$ $n ^ { - \gamma \beta _ { Y } / d _ { Y } }$ . The first two terms are analogous to those in Regime 1, with the ambient dimension $D _ { Y }$ replaced by the intrinsic dimension $d _ { Y }$ , reflecting the lower complexity of the support. The third term accounts for the intrinsic difficulty of estimating the unknown submanifold $\mathcal { M } _ { Y }$ . When $\gamma = 1$ , this term matches the minimax rate for estimating a $\beta _ { Y }$ -smooth submanifold under the Hausdorff distance, as established in Aamari and Levrard [2019]. Additionally, when $d _ { X } = 0$ , the minimax rate reduces to that of unconditional distribution estimation on unknown submanifolds, as shown in Tang and Yang [2023a].

Regime 3. Distribution regression with covariate-dependent response space. In this regime, the support $\mathcal { M } _ { Y \mid x }$ of the conditional distribution $\mu _ { Y \mid x } ^ { * }$ varies with the covariate $x$ , where the collection of conditional response supports $\{ \mathcal { M } _ { Y | x } : \ \dot { x } \in \mathcal { M } _ { X } \}$ forms an unknown family of submanifolds that is $( \beta _ { Y } , \beta _ { X } )$ -smooth (see Definition 4 for details). The minimax rate for this setting is $\begin{array} { r } { n ^ { - \alpha _ { X } / ( 2 \alpha _ { X } + d _ { X } ) } + n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } ) } + n ^ { - \gamma / ( \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } ) } } \end{array}$ . The first two terms are analogous to those in Regime 2, with the key difference arising in the third term, which accounts for the complexity of estimating the submanifold family $\{ \mathcal { M } _ { Y | x } : , x \in \mathcal { M } _ { X } \}$ . As established in Theorem 3, this term corresponds to the minimax optimal rate for manifold regression over a $( \beta _ { Y } , \beta _ { X } )$ -smooth family.

The remainder of the paper is organized as follows. Section 2 reviews and formalizes key concepts, including multivariate functions with separate smoothness, smooth manifolds, and covariate-dependent manifolds. Sections 3 and 4 present our main theoretical results on the minimax rates for distribution regression under covariate-independent and covariate-dependent response supports, respectively. In Section 5, we introduce conditional distribution estimators that attain the minimax upper bounds across the different regimes. Finally, some concluding discussion are offered in Section 6.

# 2 Background and preliminary results

In this section, we begin by introducing notation. We then present a formal definition of functions with separate smoothness, which will be used to characterize the conditional distribution functions $\mu _ { Y \mid X = x } ^ { * }$ of $Y$ given $X = x$ and their supporting manifolds $\mathcal { M } _ { Y \mid x }$ . Finally, we provide a brief review of submanifolds, with more detailed background material included in Appendix A.1 of the supplementary material. We also formally define the covariate-dependent manifold $\mathcal { M } _ { Y \mid x }$ and characterize its joint smoothness in $Y$ and $x$ .

# 2.1 Notation

Recall from the introduction section that $X \in \mathbb { R } ^ { D _ { X } }$ denotes the covariate, distributed as $\mu _ { X } ^ { * }$ , and $Y \in$ $\mathbb { R } ^ { D _ { Y } }$ denotes the response variable, distributed as $\mu _ { Y } ^ { * }$ , with the superscript $^ *$ indicating the ground truth. The conditional distribution of $Y$ given $X = x$ is denoted by $\mu _ { Y \mid X = x } ^ { * }$ , leading to the joint distribution of $( X , Y )$ as $\mu _ { X Y } ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , where $\mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ represents the generation process of first generating $X ~ \sim ~ \mu _ { X } ^ { * }$ and then $[ Y | X = x ] \sim \mu _ { Y | X = x } ^ { * }$ . When no ambiguity arises, we also use the shorthand $\mu ^ { * }$ to denote $\mu _ { X Y } ^ { * }$ . We use $\mu ^ { * , \otimes n }$ to denote the $n$ -fold product of $\mu ^ { * }$ , and $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ to denote a sample of size $n$ drawn from $\mu ^ { * }$ . The support of $\mu _ { X } ^ { * }$ is denoted by $\mathcal { M } _ { X }$ , and the support of $\mu _ { Y | x } ^ { * }$ is denoted by $\mathcal { M } _ { Y \mid x }$ . We write $\mathcal { M } = \{ ( x , y ) : x \in \mathcal { M } _ { X } , y \in \mathcal { M } _ { Y | x } \}$ as the joint space of $( X , Y )$ and $\begin{array} { r } { \mathcal { M } _ { Y } = \bigcup _ { x \in \mathcal { M } _ { X } } \mathcal { M } _ { Y \mid x } } \end{array}$ as the marginal space of $Y$ .

We use $\lVert x \rVert$ to denote the Euclidean norm of a vector $\boldsymbol { x } \in \mathbb { R } ^ { d }$ , and $\mathbf { 0 } _ { d }$ to represent the $d$ -dimensional zero vector. For a set $U \subseteq \mathbb { R } ^ { d }$ , we denote by $\mathbb { B } _ { U } ( x , r ) = \{ y \in U : \| y - x \| < r \}$ the ball of radius $r$ centered at $x$ and contained in $U$ . For a measure $\mu$ on $\mathbb { R } ^ { d }$ , we write $\mu | _ { U }$ as the restriction of $\mu$ to $U$ , i.e., $\mu | _ { U } ( A ) = \mu ( A \cap U )$ for any measurable set $A \subseteq \mathbb { R } ^ { d }$ . The floor and ceiling functions for $\alpha \in \mathbb { R }$ are denoted by $\lfloor \alpha \rfloor$ and $\lceil \alpha \rceil$ , respectively, which round $\alpha$ to the nearest smaller and larger integers. For two real numbers $a , b$ , we write $a \lor b$ and $a \wedge b$ as the maximal and minimal value between $a$ and $b$ respectively. For any sequence $\{ a _ { n } : n \geq 1 \}$ , we use the notation $\mathcal { O } ( a _ { n } )$ to mean of order $a _ { n }$ up to multiplicative constant, and use $\mathcal { O } ( a _ { n } )$ to mean of order $a _ { n }$ up to multiplicative constant and logarithmic terms of $n$ .

For a positive integer $m$ , we use the shorthand $[ m ] : = \{ 1 , \cdots , m \}$ . We denote by $\mathbb { N }$ the set of non-negative integers, $\mathbb { N } _ { + }$ the set of positive integers, and write $\mathbb { N } _ { 0 } ^ { d } = \{ ( j _ { 1 } , \cdot \cdot \cdot , j _ { d } ) | j _ { i } \in \mathbb { N } , \forall i \in [ d ] \}$ as the set of all multi-indices with $d$ components. For a multi-index $j = ( j _ { 1 } , \cdot \cdot \cdot , j _ { d } ) \in \mathbb { N } _ { 0 } ^ { d }$ , we use $\begin{array} { r } { | \boldsymbol j | = \sum _ { i = 1 } ^ { d } j _ { i } } \end{array}$ to mean its size and $\begin{array} { r } { j ! \stackrel { \cdot } { = } \prod _ { i = 1 } ^ { d } j _ { i } ! } \end{array}$ as the multi-index factorial. For a multivariate function $f : \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }  \mathbb { R }$ and two multi-indices $j \in \mathbb { N } _ { 0 } ^ { d _ { 1 } }$ and $j ^ { \prime } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } }$ , we denote by $f ^ { ( j , j ^ { \prime } ) } ( x , y )$ the mixed partial derivative $\frac { \partial ^ { | j | + | j ^ { \prime } | } f ( x , y ) } { \partial x ^ { j _ { 1 } } \cdots \partial x ^ { j _ { d _ { 1 } } } \partial y ^ { j _ { 1 } ^ { \prime } } \cdots \partial y ^ { j _ { d _ { 2 } } ^ { \prime } } }$ evaluated at $( x , y )$ . Moreover, for a vector-valued function $( x , y ) \mapsto f ( x , y ) = ( f _ { 1 } ( x , y ) , f _ { 2 } ( x , y ) , \cdot \cdot \cdot , f _ { d } ( x , y ) ) \in \mathbb { R } ^ { d }$ , the notation $f ^ { ( j , j ^ { \prime } ) } ( x , y )$ represents the vector of mixed partial derivatives $( f _ { 1 } ^ { ( j , j ^ { \prime } ) } ( x , y ) , f _ { 2 } ^ { ( j , j ^ { \prime } ) } ( x , y ) , \cdot \cdot \cdot , f _ { d } ^ { ( j , j ^ { \prime } ) } ( x , y ) )$ evaluated at $( x , y )$ . For a vector , we use $x _ { i }$ to denote its $i$ -th element. For $x , y \in \mathbb { R } ^ { d }$ and $j \in  { \mathbb { N } } _ { 0 } ^ { d }$ , we use the shorthand $( x - y ) ^ { j }$ to represent $\textstyle \prod _ { i = 1 } ^ { d } ( x _ { i } - y _ { i } ) ^ { j _ { i } }$ .

# 2.2 Functions with separate smoothness

In order to allow conditional distributions $\mu _ { Y \mid X = x } ^ { * }$ and their supporting manifolds $\mathcal { M } _ { Y \mid x }$ to have different smoothness levels in $x$ and $y$ , we consider two classes of functions with separate smoothness: a weaker class that requires differentiability along each coordinate separately and a stronger class that requires joint differentiability.

Before that, recall the classical definition of the $\alpha$ -smooth Holder function class ¨ $\mathcal { H } _ { r } ^ { \alpha } ( \mathbb { R } ^ { d } )$ with radius $r > 0$ over $\mathbb { R } ^ { d }$ , which assumes a uniform smoothness level across all its components, that is,

$$
\mathcal { H } _ { r } ^ { \alpha } ( \mathbb { R } ^ { d } ) : = \Big \{ f : \mathbb { R } ^ { d } \to \mathbb { R } : \| f \| _ { \mathcal H ^ { \alpha } ( \mathbb { R } ^ { d } ) } = \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } , \vert j \vert < \alpha } \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } \vert f ^ { ( j ) } ( x ) \vert  \\  + \sum _ { j \in \mathbb { R } _ { 0 } ^ { d } , \alpha - 1 \leq \vert j \vert < \alpha } \operatorname* { s u p } _ { x , y \in \mathbb { R } ^ { d } , x \neq y } \vert f ^ { ( j ) } ( x ) - f ^ { ( j ) } ( y ) \vert / \| x - y \| ^ { \alpha - \vert \alpha \vert } \leq r \Big \} ;
$$

when $\alpha > 0$ and $\begin{array} { r } { \mathcal { H } _ { r } ^ { \alpha } ( \mathbb { R } ^ { d } ) = \{ f : \mathbb { R } ^ { d }  \mathbb { R } : \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } | f ( x ) | \leq r \} } \end{array}$ when $\alpha = 0$ . Additionally, for any subset $U \in \mathbb { R } ^ { d }$ and a function $f : U \to \mathbb { R }$ , we say $f \in { \mathcal { H } } _ { r } ^ { \alpha } ( U )$ if there exists an extension $\overline { { f } } \in \mathcal { H } _ { r } ^ { \alpha } ( \mathbb { R } ^ { d } )$ of $f$ from $U$ to $\mathbb { R } ^ { d }$ , that is, ${ \overline { { f } } } | _ { U } = f$ . For any integer $D > 1$ , we use $\mathcal { H } _ { r , D } ^ { \alpha } ( U ) = \{ f = ( f _ { 1 } , f _ { 2 } , \cdot \cdot \cdot , f _ { D } ) :$ $U \to \mathbb { R } ^ { D } : \forall i \in [ D ] , f _ { i } \in \mathcal { H } _ { r } ^ { \alpha } ( U ) \}$ to denote the corresponding vector-valued function space.

There are multiple ways to define a multivariate function with separate smoothness levels across its components. We first introduce a class of smooth multivariate functions, denoted as $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ , which includes functions that exhibit different marginal smoothness across components. This definition corresponds to the so-called anisotropic function class in the literature [Barron et al., 1999, Nicolas, 2005, Bhattacharya et al., 2014], which we use to characterize our conditional distribution function class, as the marginal smoothness constraint is sufficient for controlling the complexity of the function class through the covering entropy.

Definition 1. A function $f : \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }  \mathbb { R }$ belongs to the family $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ if for any $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ $f ( \cdot , y ) \in \mathcal { H } _ { r } ^ { \alpha _ { 1 } } ( \mathbb { R } ^ { d _ { 1 } } )$ and for any $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ , $f ( x , \cdot ) \in { \mathcal { H } } _ { r } ^ { \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 2 } } )$ .

Next, we introduce a second, stronger definition of multivariate functions with separate smoothness, denoted as $\mathcal { H } ^ { \alpha _ { 1 } , \alpha _ { 2 } }$ , which not only requires marginal smoothness but also imposes constraints on the boundedness of certain mixed partial derivatives for both components. This definition will be used to characterize the covariate-dependent supporting manifold $\mathcal { M } _ { Y \mid x }$ , as it is necessary to ensure that the smoothness definition of the manifold is intrinsic—that is, compatible across different parameterizations; see Remark 1 for further details.

Definition 2. The class $\mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ consists of all functions $f : \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }  \mathbb { R }$ so that

$$
\sum _ { j _ { 1 } , j _ { 2 } \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , \ d _ { 2 } } } \operatorname* { s u p } _ { ( x , y ) \in \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } } } \vert f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x , y ) \vert + \sum _ { \stackrel { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } } } { \{ 1 , j _ { 1 } \} + 1 } } \operatorname* { s u p } _ { x \neq x _ { 0 } \in \mathbb { R } ^ { d _ { 1 } } , y \in \mathbb { R } ^ { d _ { 2 } } } \frac { \vert f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x , y ) - f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x _ { 0 } ) \vert } {  \vert x - x _ { 0 }  ^ {  \alpha _ { 1 } -  j _ { 1 }  - \frac { \alpha _ { 1 } } { \alpha _ { 2 } }  j _ { 2 }  } } \vert  {  \vert x - x _ { 0 }  ^ {  \alpha _ { 1 } -  j _ { 1 }  - \frac { \alpha _ { 1 } } { \alpha _ { 2 } }  j _ { 2 }  } }
$$

where $\begin{array} { r } { \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } } = \{ j _ { 1 } \in { \mathbb N } _ { 0 } ^ { d _ { 1 } } , j _ { 2 } \in { \mathbb N } _ { 0 } ^ { d _ { 2 } } : \frac { | j _ { 1 } | } { \alpha _ { 1 } } + \frac { | j _ { 2 } | } { \alpha _ { 2 } } < 1 \} . } \end{array}$

Specifically, when $\alpha _ { 1 } ~ = ~ \alpha _ { 2 } ~ = ~ \alpha$ , the class $\mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ reduces to the classical $\alpha$ -smooth Holder function class ¨ $\mathcal { H } _ { r } ^ { \alpha } ( \mathbb { R } ^ { d } )$ on the joint space $\mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ . For this reason, we call functions in $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ marginally smooth functions, while functions in $\mathcal { H } ^ { \alpha _ { 1 } , \alpha _ { 2 } }$ will be referred to as jointly smooth functions.

The stronger smoothness criterion in Definition 2 requires the existence of mixed derivatives of $f ( x , y )$ up to a certain order and enables a local polynomial approximation of $f$ up to certain degree, which is crucial for controlling approximation error when building local polynomial approximations of smooth manifold charts during our estimator construction. Specifically, the following lemma shows that in the vicinity of any point $( x _ { 0 } , y _ { 0 } )$ , the function $f ( x , y )$ can be approximated by a polynomial function with an error of $\mathcal { O } ( \| x - x _ { 0 } \| ^ { \alpha _ { 1 } } + \| y - y _ { 0 } \| ^ { \alpha _ { 2 } } )$ .

Lemma 1 (Local polynomial approximation for $\mathcal { H } ^ { \alpha _ { 1 } , \alpha _ { 2 } }$ -smooth functions). Suppose $f \in \mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } ) .$ , then there exists a constant $r _ { 1 }$ so that for any $( x _ { 0 } , y _ { 0 } ) \in \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ , it holds for any $( x , y ) \in \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ that,

$$
f ( x , y ) - \sum _ { \substack { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } } } } \frac { f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x _ { 0 } , y _ { 0 } ) } { j _ { 1 } ! j _ { 2 } ! } ( x - x _ { 0 } ) ^ { j _ { 1 } } ( y - y _ { 0 } ) ^ { j _ { 1 } } \Big | \leq r _ { 1 } ( \| x - x _ { 0 } \| ^ { \alpha _ { 1 } } + \| y - y _ { 0 } \| ^ { \alpha _ { 2 } } ) .
$$

The function class $\mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ is closely related to the class $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ defined in Definition 1. On one hand, we have $\mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } \big ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } \big ) \subset \overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } \big ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } \big )$ , and this inclusion is strict since marginal differentiability does not imply joint differentiability. On the other hand, the following lemma shows that over a fixed compact set, each function in $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ can be approximated by a funcon in . $\mathcal { H } _ { c r ( \log \varepsilon ) ^ { 2 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ r for any given error tolerance $\varepsilon > 0$ , where $c$ is a constant independent of $\varepsilon$

Lemma 2 (Relationship between $\mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } }$ and $\overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } .$ ). Consider an arbitrary function $\bar { f } \in \overline { { \mathcal { H } } } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } ) .$ and two compact sets $0 < \varepsilon \leq e ^ { - 1 }$ , there exists a function $U _ { 1 } ~ \subset ~ \mathbb { R } ^ { d _ { 1 } }$ and $f \in \mathcal { H } _ { c r ( \log \varepsilon ) ^ { 2 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ $U _ { 2 } ~ \subset ~ \mathbb { R } ^ { d _ { 2 } }$ , then there exists a constant so that $c$ so that for any

$$
\operatorname* { s u p } _ { x \in U _ { 1 } , y \in U _ { 2 } } | f ( x , y ) - \bar { f } ( x , y ) | \leq \varepsilon \quad a n d \quad \operatorname* { s u p } _ { \stackrel { x \in U _ { 1 } , y \in U _ { 2 } } { ( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } } } | f ^ { ( l _ { 1 } , l _ { 2 } ) } ( x , y ) | \leq c r .
$$

The approximation property of this lemma allows, in many cases, the two smoothness criteria to be used interchangeably up to a logarithmic term. However, the stronger smoothness condition in Definition 2 is necessary to rigorously define the smoothness of the covariate-dependent supporting manifold $\mathcal { M } _ { Y \mid x }$ through its local charts; see Remarks 1 in the following subsection for further details.

# 2.3 Smooth manifolds and covariate-dependent manifolds

We focus on distribution regression in settings where both the covariate and the response may exhibit low-dimensional structure. A natural way to describe such structure mathematically is through the manifold hypothesis. In its simplest form, this hypothesis asserts that high-dimensional data of interest (including both $X$ and $Y$ in our context) often lie on an unknown $d$ -dimensional submanifold $\mathcal { M }$ of $\mathbb { R } ^ { D }$ , where $d < D$ . To formally study distribution regression under the manifold hypothesis, we introduce several key concepts and definitions related to submanifolds in this subsection, which will be used throughout the paper. In particular, we define a class of covariate-dependent manifolds to characterize the support $\mathcal { M } _ { Y \mid x }$ of the response variable $Y$ , which may vary with the covariate value $X = x$ .

We follow Tang and Yang [2023a], Aamari and Levrard [2019], Divol [2022] in defining the class of regular manifolds. A key quantity that determines the regularity of a manifold, first introduced in Federer [1959], is the reach $r _ { \mathcal { M } }$ , defined as

$$
\begin{array} { r l } & { r _ { M } : = \operatorname* { s u p } \Big \{ \varepsilon \Big | \forall x \in \mathcal { M } ^ { \varepsilon } , \mathrm { ~ t h e r e ~ e x i s t s ~ u n i q u e ~ } y \in \mathcal { M } , \mathrm { ~ s o ~ t h a t ~ } \mathrm { d i s t } ( x , \mathcal { M } ) = \| x - y \| \Big \} , } \\ & { \qquad \mathrm { w h e r e } \quad \mathrm { d i s t } ( x , M ) = \displaystyle \operatorname* { i n f } _ { y \in \mathcal { M } } \| x - y \| , \mathrm { ~ a n d ~ } \mathcal { M } ^ { \varepsilon } = \big \{ x \in \mathbb { R } ^ { D } : \mathrm { d i s t } ( x , \mathcal { M } ) < \varepsilon \big \} . } \end{array}
$$

The reach $r _ { \mathcal { M } }$ quantifies the largest radius of a neighborhood around $\mathcal { M }$ within which every point has a unique projection onto the manifold. A lower bound on the reach (i.e., $r _ { \mathcal { M } } \ge \tau > 0 _ {  }$ ) is crucial, as it prevents the manifold from becoming nearly self-intersecting and ensures a uniform upper bound on its curvature, given by $r _ { \mathcal { M } } ^ { - 1 } \leq \tau ^ { - 1 }$ . For a more detailed discussion on the importance of this assumption, we refer the reader to Aamari and Levrard [2019].

Following standard differential geometry texts such as Do Carmo [2016], the smoothness of a submanifold $\mathcal { M }$ of $\mathbb { R } ^ { D }$ —a manifold embedded in $\mathbb { R } ^ { D }$ —is defined by the smoothness of its local charts. Specifically, for every point $y _ { 0 } \in \mathcal { M }$ , the manifold $\mathcal { M }$ can locally be represented as the graph of an $\mathcal { H } ^ { \beta }$ - smooth, one-to-one function $\phi _ { y _ { 0 } } : V _ { y _ { 0 } } \to \mathbb { R } ^ { D }$ , where $V _ { y _ { 0 } }$ is an open subset of $\mathbb { R } ^ { d }$ containing the origin $\mathbf { 0 } _ { d }$ , and $\phi _ { y _ { 0 } } ( \mathbf { 0 } _ { d } ) = y _ { 0 }$ [Tang and Yang, 2023a]. The pair $( \phi _ { y _ { 0 } } ( V _ { y _ { 0 } } ) , \phi _ { y _ { 0 } } ^ { - 1 } )$ is referred to as a $\mathcal { H } ^ { \beta }$ -smooth local chart on $\mathcal { M }$ . In Divol [2022], the function $\phi _ { y _ { 0 } }$ is alternatively defined as the inverse of the orthogonal projection $\mathrm { P r o j } _ { T y _ { 0 } \mathcal { M } }$ of a local neighborhood of $y _ { 0 }$ in $\mathcal { M }$ onto the tangent space $T _ { y _ { 0 } } \mathcal { M }$ . Here, the tangent space $T _ { y _ { 0 } } \mathcal { M }$ is identified with a $d$ -dimensional subspace of $\mathbb { R } ^ { D }$ that pass through the origin, and consists of all vectors tangential to $\mathcal { M }$ at $y _ { 0 }$ . For precise definitions and additional background on submanifolds and tangent spaces, please refer to Appendix A.1. These two definitions for smooth submanifolds are shown to be equivalent in Lemma 3 in Appendix A.2. For clarity and consistency, we adopt the latter definition of the class of $\beta$ -smooth submanifolds as described in Divol [2022] throughout this paper, which is stated as follows.

Definition 3 $\beta$ -Smooth submanifold). A $d$ -dimensional submanifold $\mathcal { M }$ in $\mathbb { R } ^ { D }$ is said to belong to the manifold class $\mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta } ( d , D )$ if: $1 . \mathcal { M }$ is closed; 2. it has reach larger than $\tau$ ; and 3. for all $y _ { 0 } \in \mathcal { M }$ , there exists a neighborhood $U _ { y _ { 0 } }$ of y0 on $\mathcal { M }$ so that the projection $\widetilde { \pi } _ { y _ { 0 } } : \mathcal { M }  T _ { y _ { 0 } } \mathcal { M }$ defined by $\widetilde { \pi } _ { y _ { 0 } } ( y ) = \mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } } ( y - y _ { 0 } )$ , when restricted to $U _ { y _ { 0 } }$ , is a diffeomorphism, with inverse function $\phi _ { y _ { 0 } }$ defined on $\mathbb { B } _ { T _ { y _ { 0 } } , M } ( 0 , \tau _ { 1 } )$ , and $\phi _ { y _ { 0 } } ~ \in \ \mathcal { H } _ { L , D } ^ { \beta } ( \mathbb { B } _ { T _ { y _ { 0 } } \mathcal { M } } ( 0 , \tau _ { 1 } ) )$ (recall that $\mathcal { H } _ { L , D } ^ { \beta }$ denotes the $\beta$ -smooth Holder class of ¨ $\mathbb { R } ^ { D }$ -valued functions with Holder norm bounded by ¨ $L$ ).

Next, we formally define a family of manifolds $\left\{ \mathcal { M } _ { Y | x } : \ x \in \mathcal { M } _ { X } \right\}$ that is indexed by $x$ on its own support $\mathcal { M } _ { X }$ in the covariate space $\mathbb { R } ^ { D _ { X } }$ and varies smoothly with respect to $x \in \mathcal { M } _ { X }$ . The notion of (joint) smoothness in $( x , y )$ for the family $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \}$ is based on characterizing the joint smoothness of the local charts (which now also depends on $x$ ) introduced in Definition 3. Specifically, for each $( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , we consider the orthogonal projection $\mathrm { P r o j } _ { T y _ { 0 } \mathcal { M } _ { Y \mid x _ { 0 } } } ( \cdot - y _ { 0 } )$ . When restricted to a local neighborhood of $y _ { 0 }$ on $\mathcal { M } _ { Y \mid x }$ , this projection should be invertible for each $x$ near $x _ { 0 }$ , provided that the tangent spaces of $\mathcal { M } _ { Y \mid x }$ at points near $y _ { 0 }$ remain sufficiently aligned with $T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ . The (joint) smoothness of the manifold family is then defined through the (joint) smoothness of the inverse of this projection in a neighborhood of $( x _ { 0 } , y _ { 0 } )$ . The precise definition is given below.

Definition 4 $( \beta _ { Y } , \beta _ { X } )$ -Smooth submanifold family). A submanifold family $\left\{ \mathcal { M } _ { Y | x } : \ x \in \mathcal { M } _ { X } \right\}$ is said to belong to $\mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d , D , \mathcal { M } _ { X } )$ , if for any $x \in \mathcal { M } _ { X }$ : 1. the manifold $\mathcal { M } _ { Y \mid x }$ is a closed $d .$ dimensional submanifold in $\mathbb { R } ^ { D }$ ; 2. it has reach larger that $\tau$ ; and 3. if, for any $w _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in$ $\mathcal { M }$ , there exists a neighborhood $U _ { \omega _ { 0 } }$ of $y _ { 0 }$ on $\mathcal { M } _ { Y }$ , so that for any $x \in \mathbb { B } _ { M _ { X } } ( x _ { 0 } , \tau )$ , the function $\widetilde \pi _ { w _ { 0 } } : \mathcal { M } _ { Y } \to T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ defined by $\widetilde { \pi } _ { w _ { 0 } } ( y ) \ = \ \mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } } } \left( y - y _ { 0 } \right)$ , when restricted to $U _ { \omega _ { 0 } } \cap$ $\mathcal { M } _ { Y \mid x }$ , is a diffeomorphism with inverse function $\phi _ { \omega _ { 0 } , x } ( \cdot )$ defined on $\mathbb { B } _ { T _ { y _ { 0 } } , \mathcal { M } _ { Y \mid x _ { 0 } } } ( 0 , \tau _ { 1 } )$ . Moreover, the function $\Phi _ { \omega _ { 0 } } : \mathbb { B } _ { T _ { y _ { 0 } } , { \cal M } _ { Y | x _ { 0 } } } ( 0 , \tau _ { 1 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )  \mathbb { R } ^ { D _ { Y } }$ defined as $\Phi _ { \omega _ { 0 } } ( z , x ) = \phi _ { \omega _ { 0 } , x } ( z )$ belongs to $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { T _ { y _ { 0 } } , \mathcal { M } _ { Y \mid x _ { 0 } } } ( 0 , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$ .

Remark 1. When $\beta _ { Y } \geq 2$ , and $\beta _ { Y } ~ \ge ~ \beta _ { X }$ , assuming the manifold family $\left\{ \mathcal { M } _ { Y | x } : \ x \in \mathcal { M } _ { X } \right\}$ to be $( \beta _ { Y } , \beta _ { X } )$ -smooth is equivalent to assuming the existence of $x$ -dependent and $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth local charts to characterize the manifold family. Specifically, this means that for any point $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ and any $x$ near $x _ { 0 }$ , the manifold $\mathcal { M } _ { Y \mid x }$ can be locally represented as the graph of a injective function $\widetilde { g } _ { \omega _ { 0 } , x } : \mathbb { B } _ { \mathbb { R } ^ { d } } ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } )  \mathbb { R } ^ { D }$ indexed by $x$ , for some positive constant $\widetilde { \tau } _ { 1 }$ ; in addition, this function changes smoothly in both $x$ and $y$ , i.e., the multivariate function $\widetilde { G } _ { \omega _ { 0 } }$ defined by $\widetilde { G } _ { \omega _ { 0 } } ( z , x ) = \widetilde { g } _ { \omega _ { 0 } , x } ( z )$ is $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ - smooth. It’s also equivalent to the assumption that locally, the manifold family can be described as set of solution manifolds indexed by $x$ , with the function $F ( y , x )$ that define the equation system being $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth. See Lemma 3 in Appendix A.2 for details.

# 3 Minimax Rate for Distribution Regression with Covariate-independent Response Space

In this section, we establish the minimax rate of convergence for distribution regression with $n$ i.i.d. samples $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ drawn from $\mu _ { X Y } ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , under a relatively simpler setting where the support $\mathcal { M } _ { Y \mid x }$ of $\mu _ { Y | x } ^ { * }$ is independent of $x$ . Specifically, we assume $\mathcal { M } _ { Y \mid x } = \mathcal { M } _ { Y }$ for all $x \in \mathcal { M } _ { X }$ . This setting includes the classical case of density regression when $Y$ is supported on the ambient space $\mathbb { R } ^ { D _ { Y } }$ . We will study the more general, covariate-dependent case in the next section.

We analyze the minimax rate relative to the integral probability metric [IPM, Muller ¨ , 1997], which is also called the adversarial loss in the machine learning literature [Singh et al., 2018, Tang and Yang, 2023a, Liang, 2021]. Specifically, we consider the following IPM, induced by a Holder test function ¨ class indexed by a smoothness parameter $\gamma \geq 0$ , referred to as the $( \gamma - )$ Holder IPM, ¨

$$
d _ { \gamma } ( \mu , \nu ) = \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } \bigg | \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \mathrm { d } \mu - \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \mathrm { d } \nu \bigg | ,
$$

for any two distributions $\mu$ and $\nu$ over $\mathbb { R } ^ { D _ { Y } }$ . This metric quantifies the maximum discrepancy in expected test function values between the two distributions $\mu$ and $\nu$ , evaluated over test functions from the Holder space ¨ $\mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ . The smoothness parameter $\gamma$ controls the strength of the metric. Larger values of $\gamma$ correspond to smoother test functions, which average out local distortions. This makes $d _ { \gamma }$ less sensitive to fine details, such as differences in the supports of the distributions, and more responsive to significant global differences in the allocation of probability mass. In contrast, smaller values of $\gamma$ make $d _ { \gamma }$ more sensitive to structural changes in the distributions, allowing it to detect subtle variations in shape, such as support misalignment and small bumps in density. Many common probability metrics are special cases of the Holder IPM. For example, the 1-Wasserstein distance ¨ $W _ { 1 }$ corresponds to the choice $\gamma = 1$ , while the total variation distance $d _ { \mathrm { T V } }$ corresponds to choosing $\gamma = 0$ .

To further compare two conditional distributions, such as when evaluating the quality of a conditional distribution estimator ${ \widehat { \mu } } _ { Y \mid X }$ for approximating $\mu _ { Y | X } ^ { * }$ , we adopt the expected Holder IPM, i.e., ¨ $\mathbb { E } _ { \mu _ { X } ^ { * } } \left[ d _ { \gamma } \big ( \widehat { \mu } _ { Y | X } , \mu _ { Y | X } ^ { * } \big ) \right]$ , which takes the expectation with respect to the marginal distribution $\mu _ { X } ^ { * }$ over the covariate $X$ . More concretely, we consider two regimes for analyzing the minimax rate of conditional distribution estimation under the expected $d _ { \gamma }$ metric. The first regime, referred to as Regime 1, assumes that $\mathcal { M } _ { Y } = \mathbb { R } ^ { D _ { Y } }$ and that $\mu _ { Y \mid x } ^ { * }$ is absolutely continuous with respect to the Lebesgue measure on the ambient space. In this case, the response variable $Y$ does not exhibit any low-dimensional manifold structure. The second regime, referred to as Regime 2, assumes that $\mathcal { M } _ { Y }$ is an unknown, $\beta _ { Y }$ - smooth, $d _ { Y }$ -dimensional submanifold with $d _ { Y } < D _ { Y }$ , and that $\mu _ { Y | x } ^ { * }$ admits a density with respect to the volume measure on $\mathcal { M } _ { Y }$ (see Appendix A.1 for the precise definition). In both regimes, we allow $\mathcal { M } _ { X }$ to exhibit low-dimensional structure by imposing conditions on its Minkowski dimension, defined below. Recall that for any $\varepsilon > 0$ , a set $P \subseteq S$ is called an $\varepsilon$ -packing of $S$ if $\| x - x ^ { \prime } \| > \varepsilon$ for every pair of distinct points $x , x ^ { \prime } \in P$ .

Definition 5. (Covariate space Minkowski dimension) We say that a topological space $\mathcal { M } _ { X } \subset \mathbb { R } ^ { D _ { X } }$ has Minkowski dimension at most $d _ { X }$ , or write $\mathcal { M } _ { X } \in \mathcal { M } _ { X } ( D _ { X } , d _ { X } , L )$ for some $L > 0$ , if $\mathcal { M } _ { X } ~ \in$ $\mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L )$ , and for any $0 < \varepsilon \le 1$ , the maximal cardinality of an $\varepsilon$ -packing of $\mathcal { M } _ { X }$ is at most $L \varepsilon ^ { - d _ { X } }$ .

This assumption is less restrictive than the manifold assumption in Definition 3, as it does not impose any conditions on the smoothness or reach of the manifold. In particular, any compact $d _ { X }$ -dimensional submanifold of $\mathbb { R } ^ { D _ { X } }$ has Minkowski dimension (at most) $d _ { X }$ .

# 3.1 Density regression in Euclidean spaces

In this subsection, we analyze Regime 1, which corresponds to classical density regression, where the conditional distribution $\mu _ { Y \mid x } ^ { * }$ is characterized by a conditional density function $u ^ { * } ( y \mid x )$ with respect to the Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ . We further assume that $u ^ { * } ( y \mid x )$ is $\alpha _ { Y }$ -smooth in $y$ (marginally) and $\alpha _ { X }$ -smooth in $x$ , which defines the class of conditional density functions considered below.

Regime 1 (Euclidean response space). For dimensions $D _ { Y } , D _ { X } \in \mathbb { N } _ { + }$ , $d _ { X } \in \mathbb { N } \cap [ 0 , D _ { X } ] .$ , smoothness parameters $\alpha _ { Y } , \alpha _ { X } \in ~ ( 0 , \infty )$ , and a constant $L > 0$ , we define the distribution family $\mathcal { P } _ { 1 } ^ { * } =$ $\mathcal { P } _ { 1 } ^ { * } ( D _ { Y } , D _ { X } , d _ { X } , \alpha _ { Y } , \alpha _ { X } , L )$ that consists of all joint distributions $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } = \mu _ { Y } ^ { * } \mu _ { X | Y } ^ { * }$ so that

1. The support $\mathcal { M } _ { X }$ of $\mu _ { X } ^ { * }$ belongs to the family $\mathcal { M } _ { X } ( D _ { X } , d _ { X } , L )$ and the support $\mathcal { M } _ { Y }$ of $\mu _ { Y } ^ { * }$ is $a$ subset of $\mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L )$ .

2. For any $x \in \mathcal { M } _ { X } , \mu _ { Y | x } ^ { * }$ has a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ , and $u ^ { * } ( y \vert x ) \in \dot { \mathcal { H } } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathcal { M } _ { X } )$ .

We also allow $d _ { X } = 0$ in the above definition, which corresponds either to unconditional distribution estimation or to settings where the covariate $X$ is discrete and takes finitely many values. The assumption that $\mu _ { Y } ^ { * }$ is compactly supported is made primarily for technical convenience. However, the analysis can be extended to cases with non-compact support, provided that $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ exhibits sufficiently light tails (e.g., exponential decay) for every $x \in \mathcal { M } _ { X }$ . In such cases, it is sufficient to restrict the analysis to a compact region with radius on the order of ${ \mathcal { O } } ( \log n )$ . Additionally, we assume that the density $\mu ^ { * } ( y \mid x )$ decays $\alpha _ { Y }$ -smoothly to zero near the boundary of $\operatorname { s u p p } ( \mu _ { Y | x } ^ { * } )$ , although the exact boundary need not be known and is allowed to vary with $x$ . The following theorem summarizes our result on the minimax rate for estimating the family of conditional distributions $\{ \mu _ { Y | X = x } ^ { * } : x \in \mathcal { M } _ { X } \}$ under this regime. A proof of the theorem is provided in Appendix C.

Theorem 1 (Minimax rate under Regime 1). For each $\gamma \geq 0$ , there exist a constant $L _ { 0 }$ so that when $L , n \ge L _ { 0 }$ , it holds that

$$
\begin{array} { r l } & { C \left( n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + n ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \right) \leq \operatorname* { i n f } _ { \widehat { \mu } _ { Y | X } \mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 1 } ^ { * } } \mathbb { E } _ { \mu ^ { * } \ast \mathcal { O } n } \left[ \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ d _ { \gamma } ( \mu _ { Y | X } ^ { * } , \widehat { \mu } _ { Y | X } ) \right] \right] } \\ & { \qquad \leq C _ { 1 } \left( \sqrt { \log n } \cdot \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \right) , } \end{array}
$$

where $( C , C _ { 1 } )$ are constants independent of $n$ , and the infimum is taken over all conditional distribution estimators ${ \widehat { \mu } } _ { Y \mid X }$ based on data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ sampled from $\mu ^ { * , \otimes n }$ . The shorthand $\mathcal { P } _ { 1 } ^ { * }$ stands for $\mathcal { P } _ { 1 } ^ { * } ( D _ { Y } , D _ { X } , d _ { X } , \dot { \alpha } _ { Y } , \alpha _ { X } , L )$ .

Here the assumption $L \geq L _ { 0 }$ is used for deriving the minimax lower bound. The proof involves constructing distributions that are difficult to distinguish and applying reduction techniques to transform the estimation problem into a multiple testing problem. The constant $L _ { 0 }$ serves as a threshold ensuring that the constructed distributions satisfy the assumptions of Regime 1. We observe a phase transition in the minimax convergence rate as the parameter γ varies. When γ ≥ dY αX2αX+dX , the dominant term in the rate is $\widetilde { \mathcal { O } } \left( n ^ { - \alpha _ { X } / \left( 2 \alpha _ { X } + d _ { X } \right) } \right)$ , which matches the classical minimax rate for estimating an $\alpha { X }$ -smooth regression function under $L _ { 2 }$ loss [Stone, 1982]. This is because smoother test functions average out local fluctuations in the conditional density, making the metric $d _ { \gamma }$ primarily responsive to the overall dependence trend, such as the conditional mean of $Y$ given $X$ . In this regime, the complexity is governed solely by the smoothness $\alpha _ { X }$ and intrinsic dimension $d _ { X }$ of the covariate $X$ . In contrast, when dY αX2αX+dX , the metric dγ becomes more sensitive to local features of the density, and the dominant term in the minimax rate becomes $\widetilde { \mathcal { O } } \big ( n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } ) } \big )$ . This rate reflects the intrinsic difficulty of nonparametric conditional density estimation, and improves as either the smoothness of the conditional density increases or the intrinsic dimensions $d _ { X }$ and $D _ { Y }$ decrease. The rate also improves with larger values of $\gamma$ , as the metric gradually shifts its sensitivity from local irregularities toward global structural differences.

A related work by Bilodeau et al. [2023] studies the minimax rate for conditional density estimation under the Kullback-Leibler (KL) risk, providing both upper and lower bounds expressed in terms of empirical Hellinger entropy. Under the assumption that $\mathcal { M } _ { X }$ and $\mathcal { M } _ { Y }$ are unit cubes in $\mathbb { R } ^ { D _ { X } }$ and $\mathbb { R } ^ { \bar { D } _ { Y } }$ , respectively, and that the partial derivatives $( u ^ { * } ) ^ { ( j _ { 1 } , j _ { 2 } ) } ( y \mid x )$ exist and are bounded for all multi-indices $j _ { 1 } \in \mathring { \mathbb { N } } _ { 0 } ^ { D _ { Y } }$ and α $j _ { 2 } \in \mathsf { N } _ { 0 } ^ { D _ { X } }$ with $| j _ { 1 } | \le \alpha _ { Y }$ and $| j _ { 2 } | \le \alpha _ { X }$ , they derive an upper bound of $\widetilde { \mathcal { O } } ( n ^ { - \alpha _ { Y } / ( \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } D _ { X } ) } )$ YX DX ) for the KL risk when αX , αY ∈ N+. This result further

implies an upper bound of $\widetilde { \mathcal { O } } \left( n ^ { - \alpha _ { Y } / ( 2 \alpha _ { Y } + 2 D _ { Y } + 2 \frac { \alpha _ { Y } } { \alpha _ { X } } D _ { X } ) } \right)$ for the expected total variation distance, via Piof st, by setting  for the expec $\gamma = 0$ in Theorem 1, we obtain a sharper upper boundl variation distance, along with a matching lower $\widetilde { \mathcal { O } } \big ( n ^ { - \alpha _ { Y } / ( 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } ) } \big )$   
bound. Our result further accommodates low-dimensional structure in the covariate space $\mathcal { M } _ { X }$ and relies on a weaker smoothness assumption that does not require the existence of mixed partial derivatives of order up to $( \alpha _ { \scriptstyle X } + \alpha _ { Y } )$ .

In another line of work, Li et al. [2022a] show that for $\alpha _ { X } ~ \in ~ [ 0 , 1 ]$ , a properly designed kernel estimator achieves the minimax rate under the expected total variation distance. Our result extends beyond this setting, allowing for general $\alpha _ { X } > 0$ and covering a broader class of metrics $\{ d _ { \gamma } : \gamma \ge 0 \}$ . Finally, Tang et al. [2024] study the convergence rate of conditional diffusion models [Song et al., 2020, Batzolis et al., 2021, Tashiro et al., 2021] under the expected 1-Wasserstein distance, which corresponds to $d _ { \gamma }$ with $\gamma = 1$ . Their derived upper bound, up to logarithmic factors, matches ours in Theorem 1 for $\gamma = 1$ , although they do not provide a matching lower bound. When combined with our minimax lower bound, their result implies that conditional diffusion models are minimax optimal under the expected 1-Wasserstein metric.

# 3.2 Distribution regression with low-dimensional manifold structures

In this subsection, we consider the regime where the response space $\mathcal { M } _ { Y }$ is an unknown $\beta _ { Y }$ -smooth submanifold of intrinsic dimension $d _ { Y }$ , embedded in the ambient space $\mathbb { R } ^ { D _ { Y } }$ . The conditional distribution $\mu _ { Y \mid x } ^ { * }$ is characterized by a density function $u ^ { * } ( y \mid x )$ defined with respect to the volume measure on $\mathcal { M } _ { Y }$ . We assume that $u ^ { * }$ exhibits marginal smoothness of order $\alpha _ { Y }$ in the $y$ -component and $\alpha _ { X }$ in the $x$ -component (c.f. Definition 1). We refer to this setting as “distribution regression” rather than “density regression”, since $\mu _ { Y | x } ^ { * }$ is not absolutely continuous with respect to the Lebesgue measure on the ambient space $\mathbb { R } ^ { D _ { Y } }$ , nor with respect to any known base measure, due to the supporting manifold $\mathcal { M } _ { Y }$ being unknown. A formal definition of this regime is given below.

Regime 2 (Covariate-independent manifold response space). For dimensions $D _ { Y } , d _ { Y } , D _ { X } \in \mathbb { N } _ { + }$ , $d _ { X } \in \mathbb { N } _ { 0 }$ , smoothness parameters $\beta _ { Y } , \alpha _ { Y } , \alpha _ { X } > 0 $ , a function $g : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ , and absolute constants $\tau , \tau _ { 1 } , L > 0$ , we define the following distribution family

$$
\mathcal { P } _ { 2 } ^ { * } = \mathcal { P } _ { 2 } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \alpha _ { Y } , \alpha _ { X } , \tau , \tau _ { 1 } , g , L ) ,
$$

which consists of all $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ so that

1. The support $\mathcal { M } _ { X }$ of $\mu _ { X } ^ { * }$ belongs to $\mathcal { M } _ { X } ( D _ { X } , d _ { X } , L )$ .

2. For any $x \in \mathcal { M } _ { X }$ , the conditional distribution $\mu _ { Y \mid x } ^ { * }$ is supported on a submanifold $\mathcal { M } _ { Y }$ independent of $x$ , and has a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to the volume measure of $\mathcal { M } _ { Y }$ , where $\mathcal { M } _ { Y } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } } ( d _ { Y } , D _ { Y } )$ and $u ^ { * } \in \overline { { \mathcal { H } } } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathcal { M } _ { Y } , \mathcal { M } _ { X } )$ .

3. For any $x _ { 0 } \in \mathcal { M } _ { X }$ , $y _ { 0 } \in \mathcal { M } _ { Y | x _ { 0 } }$ and $0 \textless r \leq 1$ , the measure $\mu _ { X } ^ { * }$ on the ball $\mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , r )$ is bounded below by $g ( r ) r ^ { d _ { X } } / { L }$ , and the measure $\mu _ { Y \mid x _ { 0 } } ^ { * }$ of $Y$ given $X ~ = ~ x _ { 0 }$ , on the ball $\mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { 0 } , r )$ , is bounded below by $g ( r ) r ^ { d _ { Y } } / L$ .

The function $g ( \cdot )$ in Item 3 of Regime 2 is introduced for technical purposes, serving to control over the constant term that captures the decay behavior of $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ when taking the supremum over all measures in ${ \mathcal { P } } _ { 2 } ^ { * }$ . Setting $g ( r ) \equiv 1$ corresponds to the case where $u ^ { * } ( y \mid x )$ is uniformly bounded away from zero for any $y \in \mathcal { M } _ { Y | x }$ and $x \in \mathcal { M } _ { X }$ . However, our framework accommodates greater generality by requiring only that $\dot { \boldsymbol g } ( \boldsymbol r ) > 0$ for all $r > 0$ . As an illustrative example, consider the distribution $\mu ^ { * } ( y \mid x ) = \mu ^ { * } ( y ) = G _ { \# } \nu$ supported on the unit sphere $\mathbb { S } _ { 1 }$ , where $G ( \theta ) = ( \sin ( \pi \theta ) , \cos ( \pi \theta ) )$ , and $\nu$ is a probability measure with density $v ( \theta ) \propto \theta ^ { 2 } ( 1 - \theta ) ^ { 2 } { \bf 1 } ( 0 < \theta < 1 ) + \theta ^ { 2 } ( \theta + 1 ) ^ { 2 } { \bf 1 } ( - 1 < \theta < 0 ) .$ . It can be shown that the density of $\mu ^ { * }$ with respect to the volume measure on $\mathbb { S } _ { 1 }$ is given by $u ^ { \ast } ( y _ { 1 } , y _ { 2 } ) \propto$ $\operatorname { a r c c o s } ( y _ { 1 } ) ^ { 2 } ( \pi - \operatorname { a r c c o s } ( y _ { 1 } ) ) ^ { 2 }$ , which is uniformly Lipschitz continuous but not bounded away from zero. Nonetheless, by choosing $g ( r ) = r ^ { 2 }$ , the inequality $\begin{array} { r } { \mu ^ { * } ( \mathbb { B } _ { \mathbb { S } _ { 1 } } ( y , r ) ) > \frac { 0 . 1 5 } { \pi ^ { 3 } } r g ( r ) } \end{array}$ holds for every $y \in \mathbb { S } _ { 1 }$ and $0 < r \leq 1$ . A similar argument applies to $\mu _ { X } ^ { * }$ , where we likewise do not require the measure to admit a density uniformly bounded away from zero. We are now prepared to present our result on the minimax rate of convergence under Regime 2.

Theorem 2 (Minimax rate under Regime 2). For each $\gamma > 0 ,$ , $f \beta _ { Y } \geq 2 \vee ( \alpha _ { Y } + 1 )$ , then there exists $a$ constant $L _ { 0 }$ so that when $L , \tau , \tau _ { 1 } , n \geq L _ { 0 } $ , it holds that

$$
\begin{array} { r l } & { \mathcal { D } \left( n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + n ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \ + \ n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } \right) } \\ & { \qquad \leq \operatorname* { i n f } _ { \substack { \hat { \mu } _ { Y } | X \mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y } ^ { * } | X } } \underset { \leq \mathcal { P } _ { 2 } ^ { * } } { \operatorname* { s u p } } \underset { + \mathcal { P } _ { 2 } ^ { * } } { \operatorname* { l e } } \left[ \mathbb { E } _ { \mu ^ { * } } \left[ d _ { Y } ( \mu _ { Y | X } ^ { * } , \hat { \mu } _ { Y | X } ) \right] \right] } \\ & { \qquad \leq C _ { 1 } \bigg ( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \ + \ \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \ + \ n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } \bigg ) , } \end{array}
$$

where $( C , C _ { 1 } )$ are constants independent of $n$ , and the infimum is taken over all conditional distribution estimators ${ \widehat { \mu } } _ { Y \mid X }$ based on data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ sampled from $\mu ^ { * , \otimes n }$ . The shorthand ${ \mathcal { P } } _ { 2 } ^ { * }$ stands for $\mathcal { P } _ { 2 } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \alpha _ { Y } , \alpha _ { X } , \tau , \tau _ { 1 } , g , L )$ .

Given that $\mathcal { M } _ { Y }$ is unknown and we only observe $n$ i.i.d. samples, the estimator ${ \widehat { \mu } } _ { Y \mid x }$ and the true conditional distribution $\mu _ { Y | x } ^ { * }$ are almost surely mutually singular, as they are supported on different submanifolds. Consequently, the total variation distance between them is identically 1 and fails to meaningfully reflect distributional closeness. To address this issue, we restrict attention to metrics $d _ { \gamma }$ with $\gamma > 0$ in this regime. The condition $\beta _ { Y } \ \geq \ 2$ ensures that the submanifold $\mathcal { M } _ { Y }$ has bounded curvature, while the assumption $\beta _ { Y } \ge \alpha _ { Y } + 1$ guarantees that the smoothness parameter $\alpha _ { Y }$ is compatible and invariant to the choice of the local charts of the manifold $\mathcal { M } _ { Y }$ . For further discussion, see Tang and Yang [2023a]. Compared to Theorem 1, the minimax rate in Theorem 2 contains an additional term $n ^ { - \gamma \beta _ { Y } / { \bar { d _ { Y } } } }$ , which reflects the intrinsic difficulty of estimating the unknown submanifold $\mathcal { M } _ { Y }$ from i.i.d. samples $\{ Y _ { i } \} _ { i = 1 } ^ { n }$ drawn on the manifold. Moreover, in settings where $\mu _ { X } ^ { * }$ is discrete (i.e., $d \boldsymbol { X } = 0$ ) or where $Y$ is independent of $X$ (corresponding to the limiting case of $\alpha _ { X }  \infty$ ), the minimax rate simplifies to $n ^ { - 1 / 2 } + \bar { n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } ) } } + \bar { n ^ { - \gamma \beta _ { Y } / d _ { Y } } }$ , which recovers the rate for unconditional distribution estimation on unknown submanifolds obtained in Tang and Yang [2023a].

Figure 1 illustrates the three regimes of problem characteristics identified in Theorem 2, based on varying values of $\alpha _ { X } , \alpha _ { Y }$ , and $\gamma$ . Each regime is determined by which of the three terms in the minimax rate dominates. The diagram reveals two critical transition points for γ: γ = dY αY2αY βY +dY (βY −1)+dXβY αY /αX and $\begin{array} { r } { \gamma = \frac { d _ { y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ . The first transition occurs between two dominant error regimes. For smaller values $\gamma$ , the error is governed by support estimation with rates to that of nonparametric conditional density estimati $n ^ { - \gamma \beta _ { Y } / d _ { Y } }$ . As ror r $\gamma$ . $n ^ { - ( \alpha _ { Y } + \gamma ) / ( 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } ) }$ This transition reflects a key sensitivity of the $d _ { \gamma }$ metric: for small $\gamma$ , it is more responsive to support misalignment than to discrepancies in mass allocation across the support. Consequently, support estimation dominates when $\gamma$ is small. Moreover, this transition point increases with larger $\alpha { X }$ and $\alpha _ { Y }$ , indicating that higher smoothness in the covariate or response reduces the complexity of density recovery. As a result, a larger $\gamma$ is needed to render support estimation errors negligible in comparison to those in density estimation. The second transition point marks the shift from conditional density estimation for smaller $\gamma$ values to global dependence recovery, characterized by the rate $n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } }$ . This threshold depends on $\alpha _ { X }$ but not on $\alpha _ { Y }$ , and it increases with larger $\alpha _ { X }$ . A higher $\alpha _ { X }$ reduces the difficulty of capturing the dependence between $X$ and $Y$ , thereby requiring a smoother test function (i.e., larger $\gamma$ ) to adequately smooth out local variations in the conditional distribution.

(a) Dominant term in the minimax rate for varying $\alpha _ { Y }$ and $\gamma$ , where $\begin{array} { r } { C _ { 1 } = \frac { 2 \alpha _ { X } + d _ { X } } { d _ { Y } \alpha _ { X } } } \end{array}$ .

![](images/462ff3af6e7c6201f0947b93954c2335ece6c2affc6f50959f6db88cb13f1ab8.jpg)  
Figure 1: Diagram for the minimax rate under Regime 2 for fixed $d _ { X } \in \mathbb { N }$ , $d _ { Y } \in \mathbb { N } ^ { + }$ and $\beta _ { Y } \ge 2$

![](images/facd086234c4b2ea77932f320a31c16ba6452b27e4a55de03e72b3366f911462.jpg)

(b) Dominant term in the minimax rate for varying $\alpha _ { X }$ and $\gamma$ , where $\begin{array} { r } { C _ { 2 } = \frac { \beta _ { Y } - 1 } { \beta _ { Y } \alpha _ { Y } } } \end{array}$ .

# 4 Minimax Rate for Distribution Regression with Covariate-dependent Response Space

In this section, we investigate a more complex setting where the support $\mathcal { M } _ { Y \mid x }$ of the conditional distribution $\mu _ { Y | x } ^ { * }$ depends on the covariate $x$ . This additional flexibility requires estimating not a single submanifold $\mathcal { M } _ { Y }$ , but a family of submanifolds $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \}$ indexed by $x$ . We refer to this task as manifold regression, where the goal is to use the data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ i.i.d. drawn from $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , to estimate or predict the submanifold $\mathcal { M } _ { Y \mid x }$ , which serves as the support of $\mu _ { Y \mid X = x } ^ { * }$ , for any given $x$ . We begin by introducing the formal setup and deriving the minimax rate for manifold regression. We then extend the analysis to obtain the minimax rate for distribution regression in this more general setting with covariate-dependent supporting manifold.

# 4.1 Manifold regression

Recall that we observe i.i.d. data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ drawn from a joint distribution $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , where the conditional distribution $\mu _ { Y | x } ^ { * }$ has support $\mathcal { M } _ { Y \mid x }$ . In this subsection, our goal is to analyze the minimax rate for estimating the family of submanifolds $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \}$ based on the observed data, under the assumption that this family is $( \beta _ { Y } , \beta _ { X } )$ -smooth (c.f. Definition 4). This problem is highly relevant to various real-world applications. For example, consider the face image data $Y$ conditioned on specific attributes $X$ such as age and gender Antipov et al. [2017], Lu et al. [2018], Ding et al. [2021]. For a given value of $X$ , it is reasonable to assume that the image dataset lies in (or close to) a submanifold [Wang et al., 2008], while different $X$ values may correspond to distinct manifolds. For instance, the face image dataset for age 18 might be quite different from that for age 80, making it reasonable to model these as two distinct submanifolds. It is worth noting that when $\mathcal { M } _ { Y | x } = \mathcal { M } _ { Y }$ for any $x \in \mathcal { M } _ { X }$ , the problem reduces to (single) manifold estimation, a topic previously explored in various literature [Aamari and Levrard, 2019, Genovese et al., 2012c, Puchkin and Spokoiny, 2022]. Therefore, our framework can be viewed as an extension of these prior works to the conditional setting under a noiseless model. We measure the estimation error using the maximal Hausdorff distance evaluated over the covariate space $\mathcal { M } _ { X }$ , defined as ${ \mathrm { s u p } } _ { x \in { \mathcal { M } } _ { X } } \mathbb { H } ( { \mathcal { M } } _ { Y | x } , { \widehat { { \mathcal { M } } } } _ { Y | x } )$ , where the Hausdorff distance $\mathbb { H } ( \mathcal { M } _ { 1 } , \mathcal { M } _ { 2 } )$ between two sets $\mathcal { M } _ { 1 }$ and $\mathcal { M } _ { 2 }$ is defined as $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { M } _ { 1 } } \operatorname* { i n f } _ { y \in \mathcal { M } _ { 2 } } \| x - y \| + \operatorname* { s u p } _ { x \in \mathcal { M } _ { 2 } } \operatorname* { i n f } _ { y \in \mathcal { M } _ { 1 } } \| x - y \| } \end{array}$ . The Hausdorff distance $\mathbb { H }$ is commonly used to evaluate errors in manifold estimation [Aamari and Levrard, 2019,

Genovese et al., 2012c]. Our analysis will be carried out over a class ${ \mathcal { P } } ^ { * }$ of distributions $\mu ^ { * }$ defined as follows.

Regime 3a (Manifold regression). For dimensions $d _ { X } , D _ { X } , d _ { Y } , D _ { Y } \in \mathbb { N } _ { + }$ , smoothness parameters $\beta _ { Y }$ , $\beta _ { X } > 0$ , and absolute constants $\tau , \tau _ { 1 } , L > 0$ , we define the following distribution family ${ \mathcal { P } } ^ { * } =$ $\mathcal { P } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \beta _ { X } , \tau , \tau _ { 1 } , L )$ , which consists of all $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ so that

1. µ∗X has a support MX ∈ MβX∨2τ,τ1,L(dX , DX ) and has a density uX function with respect to the volume measure on such that $1 / L \leq u _ { X } ^ { * } ( x ) \leq L$ for any .

2. For any $x \in \mathcal { M } _ { X }$ , the conditional distribution $\mu _ { Y \mid x } ^ { * }$ is supported on a manifold $\mathcal { M } _ { Y \mid x }$ , and admits a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to the volume measure on $\mathcal { M } _ { Y \mid x }$ so that $1 / L \leq u ^ { * } ( y | x ) \leq$ $L$ for any $y \in \mathcal { M } _ { Y | x }$ , and $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \} \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } ) .$ .

Different from Regimes 1 and 2, here we no longer impose any smoothness conditions on the conditional density function $u ^ { * } ( y \mid x )$ , since the goal is to recover the support of $\mu _ { Y \mid X } ^ { * }$ . However, we require the covariate space $\mathcal { M } _ { X }$ to be a smooth submanifold, as the regularity of $\mathcal { M } _ { X }$ facilitates the control of the “worst-case” sense error in terms of Hausdorff distance through a localized mean squared error, simplifying the problem to controlling an “average” sense error. Note that in the subsequent subsection, where we focus on estimating the conditional distribution and the error metric is directly defined in an “average” sense (rather than a worst-case one), this stronger assumption on $\mathcal { M } _ { X }$ can be relaxed to requiring only that $\mathcal { M } _ { X }$ has bounded upper Minkowski dimension, as specified in Definition 5. Moreover, here we requires the density function $u _ { X } ^ { * }$ to be bounded away from zero to ensure that there are sufficiently many samples around each $x \in \mathcal { M } _ { X }$ , which is crucial for controlling the maximal Hausdorff distance. We conjecture that this condition could be relaxed by considering an average Hausdorff distance, for example, $\mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \mathbb { H } ( \mathcal { M } _ { Y | x } , \widehat { \mathcal { M } } _ { Y | x } ) \right]$ . With these assumptions in place, we are now ready to present our main result on the minimax rate of convergence for manifold regression. The proof is provided in Appendix E.11.

Theorem 3 (Minimax rate for manifold regression). Suppose $\beta _ { Y } \ge 2$ and $\beta _ { Y } \geq \beta _ { X }$ , then there exists $a$ constant $L _ { 0 }$ so that when $L , \tau , \tau _ { 1 } , n \geq L _ { 0 }$ , it holds that

$$
C n \overbrace { \frac { \beta _ { Y } + \frac { d _ { X } } { \beta _ { X } } } { \beta _ { Y } } } ^ { - \frac { 1 } { { \frac { d _ { Y } } { \beta _ { Y } } } + \frac { d _ { X } } { \beta _ { X } } } } \ \le _ { \widehat M _ { Y | z } , x \in \mathcal { M } _ { X } } \operatorname* { s u p } _ { \mu ^ { * } \in \mathcal { P } ^ { * } } \mathbb { E } _ { \mu ^ { * } , \otimes n } \Big [ \operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \mathbb { H } \big ( \mathcal { M } _ { Y | x } , \widehat { \mathcal { M } } _ { Y | x } \big ) \big ] \Big ] \le C _ { 1 } \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } ,
$$

where $( C , C _ { 1 } )$ are constants independent of $n _ { \mathrm { : } }$ , and the infimum is taken over all estimators $\{ \widehat { \mathcal { M } } _ { Y | x } :$ $x \ \in \ { \mathcal { M } } _ { X } \}$ based on data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ sampled from $\mu ^ { * , \otimes n }$ . Here, the shorthand ${ \mathcal { P } } ^ { * }$ stands for $\mathcal { P } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \beta _ { X } , \tau , \tau _ { 1 } , L )$ .

Compared to the minimax rate for estimating a $\beta _ { Y }$ -smooth, $d _ { Y }$ -dimensional submanifold [Aamari and Levrard, 2019], which is $n ^ { - 1 / ( d _ { Y } / \beta _ { Y } ) }$ , our rate includes an additional term $d _ { X } / \beta _ { X }$ in the denominator of the exponent. This reflects the increased statistical complexity of estimating an entire family of submanifolds $\left\{ { \mathcal { M } } _ { Y | x } : x \in { \mathcal { M } } _ { X } \right\}$ , rather than a single submanifold $\mathcal { M } _ { Y \mid x }$ . Our results indicate that higher smoothness $\beta _ { X }$ with respect to the covariate $X$ makes the manifold regression problem easier, as it facilitates information sharing across different covariate values, which in turn leads to faster convergence of the minimax rate. Our estimator generalizes the local polynomial estimator from [Aamari and Levrard, 2019] by incorporating the covariate $X$ . Specifically, for each data point $w _ { k } \ = \ ( X _ { k } , Y _ { k } )$ , we select nearby data samples $( X , Y )$ such that $\| Y - Y _ { k } \| ~ \le ~ h _ { 1 }$ and $\| X - X _ { k } \| ~ \le ~ h _ { 2 }$ , where $h _ { 1 } \asymp ( \log n / n ) ^ { \frac { \beta _ { X } } { d _ { Y } \beta _ { X } + d _ { X } \beta _ { Y } } }$ and $h _ { 2 } \asymp ( \log n / n ) ^ { \frac { \beta _ { Y } } { d _ { Y } \beta _ { X } + d _ { X } \beta _ { Y } } }$ . We then learn a local polynomial estimator by minimizing the average reconstruction loss between $Y$ and $G ( Q ( Y ) , X )$ , where $Q ( \cdot ) = V ^ { T } ( \cdot - Y _ { k } )$ with $V$ being $D _ { y } \times d _ { Y }$ orthonormal matrices targeting one of the orthonormal basis $V _ { k } ^ { * }$ of the tangent space $T _ { Y _ { k } } . M _ { Y | X _ { k } }$ . The function $G ( \cdot , X )$ consists of polynomial functions designed to approximate $\Phi _ { w _ { k } } ( V _ { k } ^ { * } z , x )$ , where $\Phi _ { w _ { k } } ( \cdot , X )$ is the inverse of $\mathrm { P r o j } _ { T _ { Y _ { k } } , M _ { Y | X _ { k } } } ( \cdot - Y _ { k } )$ when restricted to the neighborhood of $w _ { k }$ on $\mathcal { M } _ { Y | X }$ , as defined in Definition 4. The assumption $\beta _ { Y } \geq \beta _ { X }$ ensures that $h _ { 2 } \leq h _ { 1 }$ , allowing us to establish the equivalence between the distance $\| Y - Y _ { k } \|$ and the distance of the projections $\| V _ { k } ^ { * } ( Y - Y _ { k } ) \|$ , up to multiplicative constants. This equivalence enables the analysis to be carried out in the low-dimensional coordinates $V _ { k } ^ { \ast T } ( Y - Y _ { k } )$ by employing polynomial approximations of the $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ smooth functions $\Phi _ { w _ { k } } ( z , x )$ within the regions $\left\| z \right\| \leq h _ { 1 }$ and $\| x \| \leq h _ { 2 }$ . Similar to [Aamari and Levrard, 2019], the final estimator is then constructed by assembling a union of polynomial patches. Further details of the estimator are provided in Appendix E.11.

# 4.2 Distribution regression with covariate-dependent manifolds

In this subsection, we study the problem of distribution regression under the setting where the conditional response supports $\left\{ \mathcal { M } _ { Y | x } : \ x \in \mathcal { M } _ { X } \right\}$ form an unknown family of submanifolds that is $( \beta _ { Y } , \beta _ { X } )$ - smooth (c.f. Definition 4). We still use $u ^ { * } ( y \mid x )$ to denote conditional density function of the conditional distribution $\mu _ { Y | x } ^ { * }$ with respect to the volume measure on its (covariate-dependent) supporting manifold $\mathcal { M } _ { Y \mid x }$ . Due to the variability in the response space and its associated volume measure across different values of $x$ , we employ the stronger smoothness criteria ${ \mathcal { H } } ^ { \alpha _ { Y } , \alpha _ { X } }$ defined in Definition 2 to quantify the smoothness of $u ^ { * }$ , and we will discuss its implications later in Remark 2. A formal definition of this regime is presented below.

Regime $^ { 3 b }$ (Covariate-dependent manifold response space). For dimensions $D _ { Y } , d _ { Y } , D _ { X } , d _ { X } \in \mathbb { N } _ { + }$ , smoothness parameters $\beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } ~ > ~ 0 ,$ , a function $g : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ , and absolute constants $\tau , \tau _ { 1 } , L > 0$ , we define the following distribution family

$$
\mathcal { P } _ { 3 } ^ { * } = \mathcal { P } _ { 3 } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } , \tau , \tau _ { 1 } , g , L ) ,
$$

which consists of all $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ so that

1. The supporting manifold $\mathcal { M } _ { X }$ of $\mu _ { X } ^ { * }$ belongs to $\mathcal { M } _ { X } ( D _ { X } , d _ { X } , L )$ .

2. For any $x \in \mathcal { M } _ { X }$ , the conditional distribution $\mu _ { Y | x } ^ { * }$ supported on a submanifold $\mathcal { M } _ { Y \mid x }$ and has a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ so that $\{ \mathcal { M } _ { Y | x } : x \in$ $\mathcal { M } _ { X } \} \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ here exists a function . $\overline { { u } } ^ { * } \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ so that $u ^ { * } ( y | x ) = \overline { { u } } ^ { * } ( \dot { y } , x )$ $( x , y ) \in { \mathcal { M } }$

3. For any $x _ { 0 } ~ \in ~ \mathcal { M } _ { X }$ , $y _ { 0 } \in \mathcal { M } _ { Y | x _ { 0 } }$ and any $0 ~ < ~ r ~ \leq ~ 1$ , it holds that $\mu _ { X } ^ { * } ( \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , r ) ) \ \geq$ $g ( r ) r ^ { d _ { X } } / L$ and $\mu _ { Y | x _ { 0 } } ^ { * } ( \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , r ) ) \geq g ( r ) r ^ { d _ { Y } } / L$ .

Compared to Regime 2, Regime 3b introduces an additional parameter $\beta _ { X }$ that characterizes the smoothness of the manifold family $\left\{ { \mathcal { M } } _ { Y | x } : x \in { \mathcal { M } } _ { X } \right\}$ with respect to the index variable $x$ . Unlike Regime 3a, Regime 3b imposes weaker conditions on the covariate distribution, whose support is not necessarily a smooth submanifold and does not require a density that is bounded away from zero. On the other hand, since Regime 3b focuses on distribution estimation, it requires a smoothness condition on the conditional density function $u ^ { * }$ . Here, the conditional density function $u ^ { * } ( y \mid x )$ operates on the joint space $\mathcal { M } _ { Y X } = \{ ( y , x ) : x \in \mathcal { M } _ { X } , y \in \mathcal { M } _ { Y | x } \}$ , which cannot be decomposed into a product form $U _ { 1 } \times U _ { 2 }$ for the spaces of $y$ and $x$ , due to the dependency of $\mathcal { M } _ { Y \mid x }$ on $x$ . To quantify the smoothness of $u ^ { * }$ with respect to $y$ and $x$ , we assume that $u ^ { * }$ can be expressed as the restriction of a function that is ${ \mathcal { H } } ^ { \alpha _ { Y } , \alpha _ { X } }$ -smooth over the entire space $\mathbb { R } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } }$ . We are now ready to present our result on the minimax rate of convergence for distribution regression under Regime 3b.

Theorem 4. (Minimax rate for distribution regression under Regime $_ { 3 b }$ ) For each $\gamma > 0 ,$ , if $\beta _ { Y } \ \geq$ $\begin{array} { r } { 2 \vee ( \alpha _ { Y } + 1 ) \vee \beta _ { X } , \beta _ { X } \geq \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ and $\alpha _ { Y } ~ \ge ~ \alpha _ { X }$ , then there exits a constant $L _ { 0 }$ so that when

$L , \tau , \tau _ { 1 } , n \geq L _ { 0 }$ , it holds that

$$
\begin{array} { r l } & { \mathcal { C } \left( n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \ + \ n ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { X } } { \alpha _ { X } } + \alpha _ { \mathrm { ~ { ~ X ~ } } } } } \ + \ n ^ { - \frac { \alpha _ { Y } } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } \ \right) } \\ & { \qquad \leq \operatorname* { i n f } _ { \substack { \hat { \mu } _ { Y | X } \mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 3 } ^ { * } } } \mathbb { E } _ { \mu ^ { * } , \otimes n } \Big [ \mathbb { E } _ { \mu _ { X } ^ { * } } \big [ d _ { \gamma } \big ( \mu _ { Y | X } ^ { * } , \hat { \mu } _ { Y | X } \big ) \big ] \Big ] } \\ & { \qquad \leq C _ { 1 } \bigg ( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \ + \ ( \log n ) \cdot \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } + \alpha _ { X } } } \ + \ ( \log n ) \cdot n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } } \end{array}
$$

where $( C , C _ { 1 } )$ are constants independent of $n$ , and the infimum is taken over all conditional distribution estimators ${ \widehat { \mu } } _ { Y \mid X }$ based on data $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ sampled from $\mu ^ { * , \otimes n }$ . Here, the shorthand ${ \mathcal { P } } _ { 3 } ^ { * }$ stands for $\mathcal { P } _ { 3 } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } , \tau , \bar { \tau _ { 1 } } , \bar { g } , L )$

Remark 2. This theorem assumes that $\begin{array} { r } { \beta _ { Y } \geq 2 \vee ( \alpha _ { Y } + 1 ) \vee \beta _ { X } , \beta _ { X } \geq \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } , } \end{array}$ $\alpha _ { Y } \geq \alpha _ { X }$ , and requires the stronger smoothness criteria ${ \mathcal { H } } ^ { \alpha _ { Y } , \alpha _ { X } }$ on the conditional density function. These conditions enable a suitable decomposition of the distribution regression problem into two main tasks: manifold regression and density regression. Specifically, for each fixed point $\boldsymbol { w } _ { 0 } = \left( x _ { 0 } , y _ { 0 } \right)$ in $\mathcal { M }$ and for any $x$ near $x _ { 0 }$ , we can perform localized analysis by restricting the measure $\mu _ { Y | x } ^ { * }$ to $U _ { w _ { 0 } } \cap { \mathcal { M } } _ { Y | x }$ , where $U _ { w _ { 0 } }$ is a defined neighborhood of y0 on $\mathcal { M } _ { Y }$ (see Definition 4). We then map the high-dimensional data points into a lower-dimensional latent space by projecting them onto a fixed tangent space $T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ , that is, $\widetilde { \pi } _ { w _ { 0 } } ( y ) = \mathrm { P r o j } _ { T _ { y _ { 0 } } , M _ { Y | x _ { 0 } } } ( y - y _ { 0 } )$ , and noting that each tangent vector can be uniquely represented by a $d _ { y }$ -dimensional coordinate. The resulting push forward measure $[ \widetilde { \pi } _ { w _ { 0 } } ] _ { \# } [ \mu _ { Y | x } ^ { * } | _ { U _ { w _ { 0 } } } ]$ admits a density function $v _ { w _ { 0 } } ( z | x )$ with respect the volume measure on $T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ , given by

$$
v _ { w _ { 0 } } ( z | x ) = u ^ { * } ( \Phi _ { w _ { 0 } } ( z , x ) | x ) \cdot \sqrt { | J _ { \Phi _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } J _ { \Phi _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) | _ { + } } , \quad z \in \mathbb { B } _ { T _ { y _ { 0 } } , M _ { Y | x _ { 0 } } } ( 0 , \tau _ { 1 } ) .
$$

The ${ \mathcal { H } } ^ { \alpha _ { Y } , \alpha _ { X } }$ -smoothness of $u ^ { * } ( \cdot , \cdot )$ and the $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smoothness of $\Phi _ { w _ { 0 } } ( \cdot , \cdot )$ , together with the conditions $\beta _ { Y } \ge \alpha _ { Y } + 1$ , $\textstyle { \beta _ { X } \geq \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } }$ and $\alpha _ { Y } \geq \alpha _ { X }$ , then ensure that $v _ { w _ { 0 } } ( \cdot , \cdot )$ is $\overline { { \mathcal { H } } } ^ { \alpha _ { Y } , \alpha _ { X } }$ -smooth. Therefore, if the tangent space at $w _ { 0 }$ can be exactly recovered, learning the local conditional distribution near $w _ { 0 }$ can be divided into: $( l )$ learning the $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth map $\Phi _ { w _ { 0 } } ( \cdot , \cdot )$ (manifold regression); and (2) learning the $\overline { { \mathcal { H } } } ^ { \alpha _ { Y } , \alpha _ { X } }$ -smooth conditional density function $v _ { w _ { 0 } }$ 0(density regression). However, it is generally impossible to exactly recover the tangent space with only a finite number of samples around $w _ { 0 }$ . Nevertheless, it is possible to approximate a hyperplane $\widehat { T }$ close to $T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ . By adding the condition $\beta _ { Y } \ge 2 \lor \beta _ { X }$ , it is ensured that for $x \approx x _ { 0 }$ , the function $\mathrm { P r o j } _ { \widehat { T } } ( y - y _ { 0 } )$ , which operates on $y \in \mathcal { M } _ { Y | x } \cap U _ { w _ { 0 } }$ , is invertible. Moreover, the inverse function is $\mathcal { H } ^ { \beta _ { Y } , \tilde { \beta } _ { X } }$ -smooth when treating $x$ as an input (c.f. Lemma $\cdot$ of Appendix A.2). Furthermore, the push forward measure $[ \mathrm { P r o j } _ { \widehat { T } } ( \cdot - y _ { 0 } ) ] _ { \# } [ \mu _ { Y | x } ^ { * } | _ { U _ { w _ { 0 } } } ]$ also admits an $\overline { { \mathcal { H } } } ^ { \alpha _ { Y } , \bar { \alpha } _ { X } }$ -smooth conditional density function $( c . f .$ , Lemma $\cdot$ bof Appendix A.2). This allows for a similar decomposition of the problem, even if the tangent space cannot be precisely recovered.

When comparing the minimax rate in Theorem 4 with that from Theorem 2, the key difference lies in the last term related to supporting manifold estimation. Specifically, by setting $\gamma = 1$ , the term $n ^ { - \gamma / ( \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } ) }$ in Theorem 4, up to logarithmic terms, matches the minimax optimal rate for manifold regression on the $( \beta _ { Y } , \beta _ { X } )$ -smooth manifold family, as obtained in Theorem 3. To simplify notation, we use $v _ { 1 } = d _ { Y } / \beta _ { Y }$ and $v _ { 2 } = d _ { X } / \beta _ { X }$ to denote the complexity indices characterizing the supporting manifolds associated with the response variable $Y$ and the covariate variable $X$ , respectively—defined as the intrinsic dimensions scaled by manifold smoothness; and $v _ { 3 } = d _ { Y } / \alpha _ { Y }$ , $v _ { 4 } = d _ { X } / \alpha _ { X }$ to denote the complexity indices characterizing the conditional distribution class with respect to inputs $y$ and $x$ , defined as the input intrinsic dimensions scaled by the corresponding density marginal smoothness. The minimax rates in Theorem 4 can then be expressed as $\widetilde { \mathcal { O } } \big ( n ^ { - \frac { 1 } { 2 + v _ { 4 } } } + n ^ { - \frac { 1 + \gamma / \alpha _ { Y } } { 2 + v _ { 3 } + v _ { 4 } } } + n ^ { - \frac { \gamma } { v _ { 1 } + v _ { 2 } } } \big )$ , which depends on the magnitude of the intrinsic dimensions relative to the smoothness levels, the value of $\gamma$ , and its proportion relative to $\alpha _ { Y }$ . Similar to Regime 1 and 2, the dominant term in the overall rate varies with different values of $\gamma$ . When $\gamma$ is sufficiently small, specifically, $\begin{array} { r } { \gamma \le \frac { v _ { 1 } + v _ { 2 } } { 2 + v _ { 3 } + v _ { 4 } - \frac { 1 } { \alpha _ { Y } } \cdot \left( ( v _ { 1 } + v _ { 2 } ) \wedge ( v _ { 3 } \alpha _ { Y } ) \right) } , } \end{array}$ the manifold regression hardness becomes the bottleneck, and the dominant term in the minimax rate is − υ1+υ2 . When $\begin{array} { r } { \frac { v _ { 1 } + v _ { 2 } } { 2 + v _ { 3 } + v _ { 4 } - \frac { 1 } { \alpha _ { Y } } \cdot \left( \left( v _ { 1 } + v _ { 2 } \right) \wedge \left( v _ { 3 } \alpha _ { Y } \right) \right) } \leq \gamma \leq \frac { ( v _ { 1 } + v _ { 2 } ) \vee \left( v _ { 3 } \alpha _ { Y } \right) } { 2 + v _ { 4 } } } \end{array}$ (υ1+υ2)∨(υ3αY ) , the term n− 2 $n ^ { - \frac { 1 + \gamma / \alpha _ { Y } } { 2 + v _ { 3 } + v _ { 4 } } }$ related to nonparametric conditional density estimation becomes dominant. If $\gamma$ increases beyond $\frac { ( v _ { 1 } + v _ { 2 } ) \vee ( v _ { 3 } \alpha _ { Y } ) } { 2 + v _ { 4 } }$ , the dominant term becomes the nonparametric mean regression risk $n ^ { - \frac { 1 } { 2 + \upsilon _ { 4 } } }$ , reflecting the overall dependence trend of $Y$ on $X$ (see the discussion after Theorem 1).

![](images/05688ab97020ff798d3ed9d6eaf0957f2e9ee9d3286bd1f5a4e9467738ed2e39.jpg)  
ying and $\gamma$ $\beta _ { X }$ where . $\begin{array} { r } { C _ { 1 } = \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ , $\begin{array} { r } { C _ { 2 } = ( 2 + \frac { d _ { X } } { \alpha _ { X } } ) \frac { \beta _ { Y } } { d _ { Y } } } \end{array}$ $\begin{array} { r } { C _ { 3 } = \frac { d _ { X } \beta _ { Y } } { d _ { Y } } } \end{array}$ dXβYd , C4 = (2 + $\begin{array} { r } { C _ { 4 } = ( 2 + \frac { d _ { X } } { \alpha _ { X } } + \frac { d _ { Y } } { \alpha _ { Y } } ) \frac { \beta _ { Y } } { d _ { Y } } - \frac { 1 } { \alpha _ { Y } } } \end{array}$ C5 = dXβYdY αY

Figure 2 illustrates these three regimes with varying $\beta _ { X }$ and $\gamma$ . When $\beta _ { X }$ falls within the interval $\begin{array} { r } { ( \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } , \frac { d _ { X } \beta _ { Y } } { d _ { Y } ( \beta _ { Y } - 1 ) } ) } \end{array}$ —assuming this interval is non-empty—there are only two regimes, where the rate for nonparametric conditional density estimation is either dominated by that for manifold regression or by that for nonparametric mean regression. The transition point in terms of $\gamma$ decreases with increasing $\beta _ { X }$ , as a larger $\beta _ { X }$ reduces the challenges for manifold regression, allowing for less smooth test functions to be effective in averaging out minor irregularities in the support, thereby focusing more on the global dependence of $Y$ on $X$ . When $\begin{array} { r } { \beta _ { X } \notin ( \hat { \alpha _ { X } } + \alpha _ { X } / \alpha _ { Y } , \frac { d _ { X } \hat { \beta } _ { Y } } { d _ { Y } ( \beta _ { Y } - 1 ) } ) } \end{array}$ , all three regimes become possible. For the first transitions (from manifold regression to nonparametric conditional density regression), the transition point in terms of $\gamma$ decreases with increasing $\beta _ { X }$ , as large $\beta _ { X }$ ease the manifold regression, prompting an earlier shift in challenges of nonparametric conditional density estimation. While the second transitions point (from nonparametric conditional density regression to mean regression) remains constant relative to $\beta _ { X }$ , as the rates for these tasks are independent of $\beta _ { X }$ .

A natural extension beyond our current setting is the noisy case, corresponding to a singular measure deconvolution problem in which the observed data are contaminated by additive noise. Specifically, we observe $n$ i.i.d. samples $\left\{ ( X _ { i } , Z _ { i } ) \right\} _ { i = 1 } ^ { n }$ generated according to the model $X _ { i } \sim \mu _ { X } ^ { * }$ , $Y _ { i } \sim \mu _ { Y | X _ { i } } ^ { * }$ , and $Z _ { i } = Y _ { i } + \varepsilon _ { i }$ , where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are i.i.d. zero-mean errors independent of $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ . The goal is to recover $\mu _ { Y \mid x } ^ { * }$ and the underlying manifolds $\mathcal { M } _ { Y \mid x }$ for each “noiseless” covariate value $x$ , based on noisy measurements. However, even the support recovery problem of estimating a single manifold from noisy observations is intrinsically difficult: for instance, Genovese et al. [2012a] show that when the noise is Gaussian, the minimax rate of manifold estimation under the Hausdorff distance is lower bounded by $C ( \log n ) ^ { - 1 }$ . One way to mitigate this slow convergence is to assume that the noise variance $\sigma ^ { 2 }$ decreases with the sample size. For clarity and simplicity, this paper focuses on the noiseless scenario and defers the detailed exploration of the deconvolution problem, including the analysis of the minimax rate in terms of both $n$ and $\sigma ^ { 2 }$ , to future work.

# 5 Minimax Optimal Estimators for Distribution Regression

In this section, we introduce our conditional distribution estimators designed to achieve minimax upper bounds across different regimes. We will start with the simpler estimator for Regime 1, where the response space is Euclidean. Following this, we will proceed to describe the more complex estimators for Regimes 2 and 3, where the response variable lies in a low-dimensional manifold.

A key component of our approach is the use of multi-scale function decomposition via wavelet, which provides a robust framework for analyzing functions by separating them into components at different levels of detail. This methodology is particularly effective for characterizing Holder regularity, as ¨ it captures both local and global smoothness properties through a hierarchical analysis of the structure of the function. The core of this decomposition is the concept of a wavelet, defined as a rapidly decaying and localized oscillating function. Commonly used constructions include the Haar basis [Triebel, 2010], Meyer basis [Tri, 2006, Meyer, 1992], and Daubechies basis [Daubechies, 1988], among others. A fundamental aspect of wavelet analysis is the concept of scaling, which involves stretching or shrinking the wavelet to adapt to different features of the target function. By stretching the analyzing function, one can capture slowly varying and global trends, whereas shrinking it allows the detection of abrupt changes and fine details.

To put things more formally, consider the space $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ of square-integrable functions on $\mathbb { R } ^ { d }$ . Within this space, one can construct a complete orthonormal basis $\textstyle \bigcup _ { j \geq 0 } { \overline { { \Psi } } } _ { j } ^ { d }$ formed by localized oscillatory functions. The level-zero basis $\overline { { \Psi } } _ { 0 } ^ { d }$ is generated by shifting a compactly supported scaling function, while the higher-level bases $\overline { { \Psi } } _ { j } ^ { d }$ are formed by shifting and scaling a compactly supported oscillatory function by a factor of $2 ^ { - ( j - 1 ) }$ . As a result, any function $p \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ admits a unique expansion of the form

$$
p ( x ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d } } p _ { \psi } \psi ( x ) \quad \mathrm { w i t h } \quad p _ { \psi } = \int _ { \mathbb { R } ^ { d } } \psi ( x ) p ( x ) \mathrm { d } x .
$$

The coefficients $p _ { \psi }$ reveal different aspects of the function $p ( x )$ : at lower levels (i.e., $\psi \in \Psi _ { j } ^ { d }$ with small $j )$ , they capture broad, slowly varying trends, whereas at higher levels, they are sensitive to fine details and abrupt variations. Consequently, for a smooth function $p ( \cdot )$ without significant local oscillations, the wavelet coefficients $p _ { \psi }$ tend to be small in absolute value for higher levels. In particular, if $p ( \cdot )$ belongs to the Holder space ¨ ${ \mathcal { H } } ^ { \alpha }$ with bounded norm, then for any $j \in \mathbb N$ and $\boldsymbol { \psi } \in \Psi _ { j } ^ { d }$ , the coefficients satisfy the bound $| p _ { \psi } | \leq C 2 ^ { - \frac { d j } 2 - j \alpha }$ for some constant $C$ independent of $j$ . Further details on wavelet theory are provided in Appendix A.3.

Throughout the following, for any dimension $d$ , we use $\textstyle \bigcup _ { j \geq 0 } { \overline { { \Psi } } } _ { j } ^ { d }$ to denote an orthonormal wavelet basis satisfying appropriate smoothness conditions, as specified in Lemma 7 of Appendix A.3 (for example, the Daubechies basis [Daubechies, 1988]). The precise smoothness requirements for different regimes are detailed in Appendix B.

# 5.1 Minimax optimal estimator for Euclidean response space

In this subsection, we focus on Regime 1, where the conditional distribution $\mu _ { Y \mid X } ^ { * }$ is characterized by a $\overline { { \mathcal { H } } } ^ { \alpha _ { Y } , \alpha _ { X } }$ -smooth conditional density function $\boldsymbol { u } ^ { * } ( \cdot | \cdot )$ . Our goal is to construct an estimator for this conditional density. For any $x \in \mathcal { M } _ { X }$ , given that $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ is assumed to be compactly supported within $\mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L )$ , we define for any $j \in \mathbb N$ ,

$$
\Psi _ { j } ^ { D _ { Y } } = \big \{ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L ) \neq \emptyset \big \} .
$$

Then the function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ has a wavelet expansion as

$$
u ^ { * } ( y | x ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \Psi _ { j } ^ { D } \gamma } u _ { \psi } ^ { * } ( x ) \psi ( y ) \quad \mathrm { w i t h } \quad u _ { \psi } ^ { * } ( x ) = \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( y ) ] = \int _ { \mathbb { R } ^ { D _ { Y } } } \psi ( y ) u ^ { * } ( y | x ) \mathrm { d } y .
$$

Since $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ belongs to $\mathcal { H } _ { L } ^ { \alpha _ { Y } } ( \mathbb { R } ^ { D _ { Y } } )$ , we truncate its wavelet expansion at a finite level $J$ to eliminate high-frequency fluctuations. The value of $J$ will be carefully chosen later to balance the bias-variance trade-off. Consequently, the problem of jointly estimating $u ^ { * } ( y \mid x )$ over $x \in \mathcal { M } _ { X }$ reduces to the joint estimation of the wavelet coefficients $u _ { \psi } ^ { * } ( x )$ for $j \in \mathbb N$ , $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , and $x \in \mathcal { M } _ { X }$ . Observing that each coefficient $u _ { \psi } ^ { * } ( x )$ can be expressed as the conditional mean $\mathbb { E } \dot { \mu } _ { Y \mid x } ^ { * } [ \psi ( y ) ]$ , the estimation of $u _ { \psi } ^ { * } ( x )$ for different $\psi$ can be formulated as a collection of regression problems, where the response variables are $\left\{ \psi ( Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ with covariates $\{ X _ { i } \} _ { i = 1 } ^ { n }$ .

For each level $j \in 0 \cup [ J ]$ , we consider an approximation family $\mathcal { S } _ { j }$ consisting of functions mapping $\mathbb { R } ^ { D _ { X } }$ to $\mathbb { R }$ . For each $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , we minimize the mean squared error to obtain

$$
\widehat { u } _ { \psi } ( \cdot ) = \mathop { \mathrm { a r g } \operatorname* { m i n } } _ { u \in \mathcal { S } _ { j } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \big ( \psi ( Y _ { i } ) - u ( X _ { i } ) \big ) ^ { 2 } .
$$

Note that this estimation procedure uses the same approximation family ${ \mathcal { S } } _ { j }$ for coefficients of $\psi$ at each specific level $j$ , while $\mathcal { S } _ { j }$ varies across different levels $j$ .

To construct the approximation family $\mathcal { S } _ { j }$ , we leverage the fact that, for each $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , the conditional mean $\begin{array} { r } { \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( Y ) ] = \int _ { \mathbb { R } ^ { D _ { Y } } } \psi ( y ) u ^ { * } ( y \mid x ) \mathrm { d } y } \end{array}$ is a ${ \mathcal { H } } ^ { \alpha _ { X } }$ -smooth function of $x$ , with its Holder ¨ norm bounded by $\mathcal { O } \big ( 2 ^ { - \frac { D _ { Y } j } { 2 } } \big )$ . This property motivate us to define the following approximating family by utilizing local polynomial approximations for Holder-smooth functions, ¨

$$
\begin{array} { r } { \mathcal { S } _ { j } = \Bigg \{ u ( x ) = \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } X , | k | < \alpha _ { X } } a _ { i k } \left( x - b _ { i } \right) ^ { k } \rho \left( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } \right) } { \sum _ { i = 1 } ^ { W _ { j } } \rho \left( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } \right) + \frac { 1 } { n } } : b _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( \mathbf { 0 } , L \right) \mathrm { , ~ } } \\ { a _ { i k } \in \bigg [ - \frac { C } { 2 ^ { D _ { Y } j / 2 } } , \frac { C } { 2 ^ { D _ { Y } j / 2 } } \bigg ] \mathrm { , ~ f o r ~ a n y ~ } i \in [ W _ { j } ] \mathrm { ~ a n d ~ m u l t i - i n d e x ~ } k \Bigg \} \mathrm { , ~ } } \end{array}
$$

where $\begin{array} { r } { \varepsilon _ { j } ^ { x } = 2 ^ { j D _ { Y } / \left( 2 \alpha _ { X } + d _ { X } \right) } \left( \frac { n } { \log { n } } \right) ^ { - 1 / \left( 2 \alpha _ { X } + d _ { X } \right) } } \end{array}$ −1/(2αX+dX), Wj = C1 (εxj )−dX , and (C, C1) are some sufficiently large constants. Here, $\rho$ is a smooth transition function satisfying $\rho ( t ) = 1$ for $t \in [ 0 , 1 ]$ and $\rho ( t ) =$ 0 for $t \geq 2$ . The function $\rho \big ( \| x - b _ { i } \| / \varepsilon _ { j } ^ { x } \big )$ effectively partitions the covariate space $\mathcal { M } _ { X }$ into local neighborhoods, where the radius (bandwidth) and number of neighborhoods scale with the effective dimension $d _ { X }$ of $\mathcal { M } _ { X }$ . Within each neighborhood, the conditional mean $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( Y ) ]$ can be well approximated by a low-degree polynomial in $x$ .

By substituting the estimator $\widehat { u } _ { \psi } ( x )$ into the truncated wavelet expansion of $u ^ { * } ( y \mid x )$ , we can derive a conditional density estimator as

$$
\widehat { u } ( y | x ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \widehat { u } _ { \psi } ( x ) \psi ( y ) , \quad x \in \mathcal { M } _ { X } .
$$

The following theorem shows that the conditional distribution estimator ${ \widehat { \mu } } _ { Y \mid X }$ , whose density function is ${ \widehat { u } } ( y \mid x )$ b, can achieve the minimax upper bound stated in Theorem 1 simultaneously for all $\gamma \geq 0$ .

Theorem 5 (Convergence rate for density regression estimator in Regime 1). Let $\mathcal { P } _ { 1 } ^ { * }$ be the target distribution class defined in Theorem $\cdot$ . Suppose $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ are $n$ i.i.d. samples from $\mu ^ { * }$ , and set

$\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + D _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . For any $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 1 } ^ { * }$ , the following holds with probability at least $1 - n ^ { - 1 }$ : for any $\gamma \geq 0$ , the conditional density estimator $\widehat { u }$ defined in (4) satisfies

$$
\mathbb { E } _ { \mu _ { X } ^ { \star } } \left[ d _ { \gamma } \big ( \mu _ { Y | X } ^ { * } , \widehat { \mu } _ { Y | X } \big ) \right] \leq C _ { \gamma } \bigg ( \sqrt { \log n } \cdot \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \Big ( \frac { n } { \log n } \Big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \bigg ) ,
$$

where $C _ { \gamma }$ is a constant independent $n$

A complete proof of Theorem 5 is provided in Appendix C.1, and further details on the estimator construction are summarized in Appendix B.1. A key observation is that the bandwidth $\varepsilon _ { j } ^ { x }$ increases with the level $j$ , in contrast to the bandwidth $2 ^ { - j }$ in $Y$ , which decreases as $j$ increases. This asymmetric scaling is crucial for balancing the overall complexity of jointly estimating $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( Y ) ]$ across different levels $j$ . Intuitively, as $j$ increases, the resolution in $Y$ becomes finer because the bandwidth decreases, allowing the model to capture more detailed variations in $Y$ . At the same time, the resolution in $X$ becomes coarser because the bandwidth increases, meaning that the model mainly captures broad, global patterns in $X$ while finer structures in $Y$ are being learned.

The multiresolution analysis underlying wavelet decompositions shares a close connection with score-based forward backward diffusion models [Song et al., 2020] for implicit distribution estimation. For example, in the backward diffusion model, the data generation process gradually builds structure by transforming white noise into realistic data, following a progression from coarse to fine details. This process parallels how multiresolution analysis decomposes a function, first capturing global trends and then progressively refining finer structures. In particular, when comparing the conditional diffusion model with the wavelet-based conditional distribution estimator, both approaches can be viewed as solving multiple mean regression problems across different resolution levels. More specifically, the index $j \in \mathbb N$ in the preceding wavelet estimator and the time variable $t \in \mathbb { R } ^ { + }$ in the backward diffusion model and both represent levels of resolution, controlling the scale of analysis from coarse to fine details.

# 5.2 Minimax optimal estimator for manifold response space

In this subsection, we focus on Regimes 2 and 3, where, given $X = x$ for $x \in \mathcal { M } _ { X }$ , the conditional distribution $\mu _ { Y | x } ^ { * }$ is supported on a $d _ { Y }$ -dimensional submanifold $\mathcal { M } _ { Y \mid x }$ . Since the conditional density with respect to the Lebesgue measure does not exist in these regimes, we reformulate the conditional distribution estimation problem as one that involves simultaneously estimating the conditional expectations $\mathcal { T } ^ { * } ( f , x ) : = \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$ for a class of test functions $f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ and covariate values $x \in \mathcal { M } _ { X }$ , where $\gamma \geq 0$ corresponds to the same smoothness index used in defining the Holder IPM ¨ $d _ { \gamma }$ . In other words, we construct an explicit estimator for the conditional expectation functional, denoted by $\widehat { \mathcal { I } } : \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) \times \mathbb { R } ^ { D _ { X } }  \mathbb { R }$ , and evaluate its performance using the simultaneous estimation risk

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \Bigg [ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } \bigg | \widehat { \mathcal { I } } ( f , x ) - \mathcal { I } ^ { * } ( f , x ) \bigg | \Bigg ] .
$$

There exists a one-to-one correspondence between the conditional distribution $\mu _ { Y | x } ^ { * }$ and the conditional expectation functional $\mathcal { T } ^ { * } ( \cdot , x )$ evaluated over any rich enough class of test functions that is dense in $\mathcal { L } _ { 2 } ( \mathbb { R } ^ { D _ { Y } } )$ , such as ${ \mathcal { H } } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ . As a result, estimating the conditional distribution is equivalent to estimating its associated conditional expectation functional. Specifically, as discussed in [Tang and Yang, 2023b], for any fixed $\gamma > 0$ and $x$ , one can employ adversarial training with $\gamma$ -smooth test functions to obtain a conditional distribution estimator

$$
\widehat { \mu } _ { Y | x } ^ { \gamma } = \underset { \mu \in \mathcal { P } _ { Y } ^ { * } } { \arg \operatorname* { m i n } } \ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } | \mathbb { E } _ { \mu } [ f ( y ) ] - \widehat { \mathcal { I } } ( f , x ) |
$$

where for a suitable $\mathcal { P } _ { Y } ^ { * }$ , the estimation error of ${ \widehat \mu } _ { Y | x } ^ { \gamma }$ under the $d _ { \gamma }$ metric can be bounded from above by twice the maximal deviation between $\widehat { \mathcal { I } } ( f , x )$ and $\mathcal { T } ^ { * } ( f , x )$ over $f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } )$ . Furthermore, given

a suitable set $\Gamma$ of $\gamma$ values, consider the estimator:

$$
\widehat { \mu } _ { Y | x } = \underset { \mu \in \mathcal { P } _ { Y } ^ { * } } { \arg \operatorname* { m i n } } \sum _ { \gamma \in \Gamma } \frac { 1 } { \delta _ { n , \gamma } } \cdot \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \left[ \mathbb { E } _ { \mu } [ f ( y ) ] - \widehat { \mathcal { I } } ( f , x ) \right] ,
$$

with appropriate choices for $\mathcal { P } _ { Y } ^ { * }$ and $\delta _ { n , \gamma }$ . This estimator is simultaneously minimax optimal up to logarithmic factors for all $\gamma > 0$ (cf. Corollary 1 and Corollary 2 in Appendix B). This optimality is attained by incorporating a jointly optimal $\hat { \mathcal { I } } ( \cdot , \cdot )$ , the construction of which will be detailed below.

To construct an estimator $\hat { \mathcal { I } } ( f , \hat { x } )$ for $\mathcal { T } ^ { * } ( f , x )$ , we first observe that, since $\mu _ { Y | x } ^ { * }$ is compactly supported for any $x \in \mathcal { M } _ { X }$ , it suffices to restrict our analysis to test functions $f \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { D _ { Y } } ) \cap \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ . Each such function admits a wavelet expansion

$$
f ( y ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) \quad \mathrm { w i t h } f _ { \psi } = \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) \mathrm { d } y .
$$

We fix a finite truncation level $J$ (to be specified later) and consider the wavelet thresholding approximation $f _ { J }$ of $f$ :

$$
f ( y ) \ = \ \underbrace { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) } _ { f _ { J } ( y ) } + \underbrace { \sum _ { j = J + 1 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) } _ { f _ { J } ^ { \perp } ( y ) } ,
$$

with $f _ { J } ^ { \perp }$ denoting the corresponding remainder term. The thresholding approximation $f _ { J } ( \cdot )$ primarily captures the slowly varying and global structure of the function $f$ , while the remainder term $f _ { J } ^ { \bot } ( \cdot )$ accounts for the more abrupt, localized variations and oscillations. By decomposing the conditional expectation as $\mathcal { J } ^ { * } ( f , x ) \ = \ \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( Y ) ] + \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ , we then estimate the two components $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( Y ) ]$ and $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ using different strategies.

# 5.2.1 Estimator for coarse-scale component $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( Y ) ]$

Given the inherent smoothing effect of the truncation operation in $f _ { J }$ , minor irregularities in the conditional distribution $\mu _ { Y | x } ^ { * }$ have limited impact and are effectively averaged out. Based on this observation, we construct a estimator for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( Y ) ]$ by treating $\mu _ { Y | x } ^ { * }$ as if it admits a density with respect to the Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ . Specifically, we estimate the coarse-scale component $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( y ) ]$ in $\mathcal { T } ^ { * } ( f , x )$ by $\begin{array} { r } { \int _ { \mathbb { R } ^ { D _ { Y } } } f _ { J } ( y ) \widehat { u } ( y | x ) \mathrm { d } y } \end{array}$ , where the “conditional density” estimator ${ \widehat { u } } ( y \mid x )$ is constructed solely to define this integral. The construction follows a strategy similar to that introduced in Section 5.1 for Regime 1, as detailed below.

To construct the conditional density estimator $\widehat { u }$ , we begin by simultaneously estimating the conditional means $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } \big [ 2 ^ { j ( d _ { Y } - D _ { Y } ) / 2 } \psi ( y ) \big ]$ for all $j ~ \in ~ \{ 0 \} ~ \bigcup ~ [ J ] , ~ \psi ~ \in ~ \Psi _ { j } ^ { D _ { Y } }$ and $x \ \in \ \mathcal { M } _ { X }$ . The scaling factor $2 ^ { j ( d _ { Y } - D _ { Y } ) / 2 }$ is introduced to account for the intrinsic dimension $d _ { Y }$ of the support of $\mu _ { Y \mid x } ^ { * }$ , ensuring that the second moment $\mathbb { E } _ { \mu _ { Y | x } ^ { * } } \big [ ( 2 ^ { j ( d _ { Y } - D _ { Y } ) / 2 } \psi ( y ) ) ^ { 2 } \big ]$ remains bounded, i.e., of order $\mathcal { O } ( 1 )$ . In contrast to the method used in Section 5.1, where each conditional expectation was estimated independently through separate mean regression problems, we adopt a joint estimation strategy that better reflects the low-dimensional structure of the support $\mathcal { M } _ { Y \mid x }$ . Estimating each $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ]$ separately may ignore geometric dependencies and lead to inefficient use of data. Instead, we treat the wavelet function $\psi$ as an additional input, alongside $x$ , and formulate a joint mean regression problem over the product space $\Psi _ { j } ^ { D _ { Y } } \times \bar { \mathbb { R } ^ { D _ { X } } }$ . This leads us to define an estimator $\widehat { S } _ { j } ^ { \dagger }$ satisfying $\widehat { S } _ { j } ^ { \dagger } ( \psi , x ) \approx \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } \big [ 2 ^ { j ( d _ { Y } - D _ { Y } ) / 2 } \psi ( y ) \big ]$ . To this end, for each $j \in 0 \cup [ J ]$ , we introduce a function class $\boldsymbol { S } _ { j } ^ { \dagger }$ consisting of mappings $S : \Psi _ { j } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R }$ , and formulate the following joint mean regression problem by minimizing the aggregated squared loss over all $\psi \in \Psi _ { j } ^ { D _ { Y } }$ :

$$
\widehat { S } _ { j } ^ { \dagger } = \arg \operatorname* { m i n } _ { S \in { \mathcal { S } _ { j } ^ { \dagger } } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \Big ( 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) - S ( \psi , X _ { i } ) \Big ) ^ { 2 } .
$$

Note that the separate mean regressions described in Section 5.1 can be viewed as a special case of the joint mean regression framework introduced above. In that setting, the approximation family for $S$ is separable in $\psi$ and takes the form $\begin{array} { r } { \begin{array} { r } { \mathcal { S } _ { j } = \big \{ S ( \psi , x ) = \sum _ { \psi ^ { \prime } \in \Psi _ { j } ^ { D _ { Y } } } s _ { \psi ^ { \prime } } ( x ) \cdot \mathbf { 1 } ( \psi ^ { \prime } = \psi ) . } \end{array} } \end{array}$ , such that $s _ { \psi ^ { \prime } } \in$ ${ \mathcal { S } } _ { j }$ for each $\psi ^ { \prime } \in \Psi _ { j } ^ { D _ { Y } } \big \}$ . However, this separable approximation family does not allow the sharing of information across different $\psi$ . Specifically, due to the manifold structure of the response space, only a subset of the functions $\psi ( \cdot )$ have non-zero conditional means. This inherent sparsity is not fully utilized in separate mean regression. In contrast, by choosing $S _ { j }$ in a non-separable form, one can more effectively exploit this structure. Further details on these constructions are provided in Appendix B.2 (for Regime 2) and Appendix B.3 (for Regime 3b). The conditional density estimator ${ \widehat { u } } ( y \mid x )$ is then defined as

$$
\widehat { u } ( y | x ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dag } ( \psi , x ) \psi ( y ) ,
$$

and the associated estimator for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ( Y ) ]$ is given by

$$
\int _ { \mathbb { R } ^ { D _ { Y } } } f _ { J } ( y ) \widehat { u } ( y | x ) \mathrm { d } y = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } f _ { \psi } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) .
$$

# 5.2.2 Estimator for fine-scale component $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$

This term is more sensitive to fine-scale structure and to potential misalignment in the support of the distributions resulting from manifold estimation. To address this, we incorporate an explicit manifold estimation step by learning $x$ -dependent local charts of the submanifold $\mathcal { M } _ { Y \mid x }$ . Specifically, for each local patch of the joint space $\mathcal { M }$ , we learn an encoder $Q : \mathbb { R } ^ { D _ { Y } }  \mathbb { R } ^ { d _ { Y } }$ and a conditional decoder $G : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R } ^ { D _ { Y } }$ such that the reconstruction relation $y \approx G ( Q ( y ) , x )$ holds for each $( x , y )$ in the patch.

These estimated charts allow us to map the data into a low-dimensional latent space $\mathbb { R } ^ { d _ { Y } }$ , where subsequent analysis becomes more tractable. In the second step, we will perform density regression in the latent space using the transformed samples $\{ \left( X _ { i } , Q ( Y _ { i } ) \right) \} _ { i = 1 } ^ { n }$ to estimate conditional density functions associated with the latent distributions. This encoder–decoder framework, which shifts the analysis from the ambient to a lower-dimensional latent space, is widely used in practice, including in methods such as latent diffusion models Rombach et al. [2022], variational autoencoders Kingma [2013], and Wasserstein autoencoders Tolstikhin et al. [2017], among others.

The final estimator is formulated as a mixture of conditional generative models, given by

$$
\sum _ { k \in \widehat { \mathcal { K } } } \big [ \widehat { G } _ { [ k ] } ( \cdot , x ) \big ] _ { \# } \widehat { \nu } _ { [ k ] } ( \cdot | x ) ,
$$

where $\widehat { \kappa }$ is a data-dependent index set, $\widehat { G } _ { [ k ] } : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R } ^ { D _ { Y } }$ is a learned decoding map from the latent space $\mathbb { R } ^ { d _ { Y } }$ to the data ambient space $\mathbb { R } ^ { D _ { Y } }$ , and $\widehat { \nu } _ { [ k ] } ( \cdot | x )$ is an estimated conditional distribution of the latent variable on $\mathbb { R } ^ { d _ { Y } }$ . This pushforward measure serves as a surrogate for $\mu _ { Y | x } ^ { * }$ in the estimation of the fine-scale component $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ .

For technical simplicity, we adopt a data-splitting strategy to divide the dataset into two disjoint subsets: $I _ { 1 } = [ \lfloor n / 2 \rfloor ]$ and $I _ { 2 } = [ n ] \setminus I _ { 1 }$ . The two-step estimation procedure described above can be summarized in the following concrete algorithm.

Manifold estimation: Let $\{ \omega _ { k } = ( x _ { k } , y _ { k } ) \} _ { k = 1 } ^ { K }$ be a $\tau _ { 2 }$ -covering set of $\mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L )$ where $\tau _ { 2 }$ is a sufficiently small absolute constant. Define

$$
{ \widehat { K } } = \big \{ k \in [ K ] : \exists i \in I _ { 1 } , \| ( X _ { i } , Y _ { i } ) - \omega _ { k } \| \leq \sqrt { 2 } \tau _ { 2 } \big \} .
$$

Let $\mathcal { G }$ be a family of functions $G : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R } ^ { D _ { Y } }$ . For each $k \in { \widehat { \mathcal { K } } }$ , we define the estimator

$$
\begin{array} { r l } & { ( G _ { [ k ] } , V _ { [ k ] } ) } \\ { \ } & { = \ \underset { V \in 0 ( D _ { Y } , d _ { Y } ) } { \operatorname { a r g m i n } } \ \frac { 1 } { \left| I _ { 1 } \right| } \displaystyle \sum _ { i \in I _ { 1 } } \left\| Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { k } ) , X _ { i } ) \right\| ^ { 2 } \cdot \mathbf { 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { k } , 2 \tau _ { 2 } ) \big ) \cdot \mathbf { 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x , 2 \tau _ { 2 } ) \big ) } \end{array}
$$

where $\mathbb { O } ( D _ { Y } , d _ { Y } ) = \{ A \in \mathbb { R } ^ { D _ { Y } \times d _ { Y } } : A ^ { T } A = I _ { d _ { Y } } \} .$ .

Density regression on the latent space: Denote $\widehat { Q } _ { [ k ] } ( y ) = \widehat { V } _ { [ k ] } ^ { T } ( y - y _ { k } )$ . For any $j \in \mathbb N$ , we define $\Psi _ { j } ^ { d _ { Y } } = \big \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau _ { 2 } ) \neq \emptyset \big \}$ . Let ${ \mathcal { S } } _ { j }$ denote a class of functions $v : \mathbb { R } ^ { D _ { X } }  \mathbb { R }$ For each $k \in { \widehat { \mathcal { K } } }$ , $j \in \{ 0 \} \cup [ J ]$ and $\psi \in \Psi _ { j } ^ { d _ { Y } }$ , we define the estimator

$$
\widehat v _ { k \psi } ( \cdot ) = \arg \operatorname* { m i n } _ { \boldsymbol v \in \mathcal { S } _ { j } } \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \Big [ \psi ( \widehat Q _ { [ k ] } ( Y _ { i } ) ) \cdot \rho _ { [ k ] } ( X _ { i } , Y _ { i } ) - \boldsymbol v ( X _ { i } ) \Big ] ^ { 2 } ,
$$

where $\begin{array} { r } { \rho _ { [ k ] } ( x , y ) = \frac { \rho ( \| ( x , y ) - ( x _ { k } , y _ { k } ) \| ^ { 2 } / \tau _ { 2 } ^ { 2 } ) } { \sum _ { k = 1 } ^ { K } \rho ( \| ( x , y ) - ( x _ { k } , y _ { k } ) \| ^ { 2 } / \tau _ { 2 } ^ { 2 } ) } } \end{array}$ with $\rho$ being a smooth transition function taking value 1 on [0, 1] and zero on $[ 2 , \infty )$ . Here, the functions $\{ \rho _ { [ k ] } \} _ { k = 1 } ^ { K }$ serve as a partition of unity, allowing the local constructions around each $\omega _ { k }$ to be smoothly combined into a global estimator.

Final estimator for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ : Denote $\widehat { \nu } _ { [ k ] } ( \cdot | x )$ as the measure that has a density function

$$
\sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( \cdot ) \widehat { v } _ { k \psi } ( x )
$$

with respect to the Lebesgue measure on $\mathbb { R } ^ { d _ { Y } }$ . By using $\begin{array} { r } { \sum _ { k \in \widehat { \mathcal { K } } } \big [ \widehat { G } _ { [ k ] } ( \cdot , x ) \big ] _ { \# } \widehat { \nu } _ { [ k ] } ( \cdot | x ) } \end{array}$ as an estimator for $\mu _ { Y | x } ^ { * }$ , we define the plug-in estimator for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f _ { J } ^ { \perp } ( Y ) ]$ as

$$
\sum _ { k \in \widehat { \mathcal { K } } } \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { J } ^ { \perp } \big ( \widehat { G } _ { [ k ] } ( z , x ) \big ) \bigg \{ \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \bigg \} \mathrm { d } z .
$$

# 5.2.3 Convergence rate of the estimator for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$

For any $\mathcal { L } ^ { 2 }$ integrable function $f : \mathbb { R } ^ { D _ { Y } }  \mathbb { R }$ and any $x \in \mathbb { R } ^ { D _ { X } }$ , our estimator $\widehat { \mathcal { I } } ( f , x )$ for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$ is constructed by combining the estimators for the coarse-scale and fine-scale components,

$$
\widehat { \mathcal { I } } ( f , x ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } f _ { \psi } \widehat { S } _ { j } ( \psi , x )
$$

$$
+ \sum _ { k \in \widehat { \mathcal { K } } } \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { J } ^ { \perp } \big ( \widehat { G } _ { [ k ] } ( z , x ) \big ) \bigg \{ \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \bigg \} \mathrm { d } z ,
$$

$$
f _ { \psi } = \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) \mathrm { d } y \quad \mathrm { a n d } \quad f _ { J } ^ { \perp } ( y ) = f ( y ) - \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) .
$$

Suppose $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ are $n$ i.i.d. samples from $\mu ^ { * }$ , and let $\mathcal { P } _ { 2 } ^ { * }$ and $\mathcal { P } _ { 3 } ^ { * }$ denote the target distribution classes defined in Theorem 2 and Theorem 4, respectively. The following theorem shows that, by setting $\begin{array} { r } { J = \Big \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \alpha _ { Y } / \alpha _ { X } } \cdot \log _ { 2 } \bigl ( \frac { n } { \log n } \bigr ) \Big \rceil } \end{array}$ , there exist suitable choices of $\mathcal { G } , \mathcal { S } _ { j } ^ { \dag }$ , and $\mathcal { S } _ { j }$ for Regime 2 $( \mu ^ { \ast } \in \mathcal { P } _ { 2 } ^ { \ast } )$ and Regime 3b $( \mu ^ { \ast } \in \mathcal { P } _ { 3 } ^ { \ast } )$ such that the estimator $\widehat { \mathcal { I } }$ simultaneously achieves the minimax upper bound for all $\gamma > 0$ .

Theorem 6 (Convergence rates for distribution regression estimators in Regimes 2 and 3b). For Regimes 2 and $_ { 3 b }$ , there exist distinct families $\mathcal { G }$ and $\{ { \bar { \mathcal { S } } _ { j } ^ { \dag } } \} _ { j = 0 } ^ { J }$ tailored for each regime, alongside families $\{ \mathcal { S } _ { j } \} _ { j = 0 } ^ { J }$ that are applicable to both regimes, so that for any $\mu ^ { * } \ = \ \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \ \mathcal { P } _ { i } ^ { * }$ (where $i \ = \ 2$ for Regime 2, and $i = 3$ for Regime $_ { 3 b }$ ), the following holds with probability at least $1 - n ^ { - 1 }$ : for any $\gamma > 0$ , the conditional expectation functional estimator $\widehat { \mathcal { I } }$ defined in (9) satisfies

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { \frac { s } { \lambda } } } \bigg [ \underset { f \in \mathcal { H } _ { 1 } ^ { \lambda } ( \mathbb { R } ^ { D } Y ) } { \operatorname* { s u p } } \bigg | \widehat { \mathcal { I } } ( f , x ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { s } } f ( y ) \bigg | \bigg ] } \\ & { \leq C _ { \gamma } \left\{ \begin{array} { l l } { \displaystyle \left( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } } } + n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } \right) , } & { f o r i s \frac { \alpha _ { X } + \gamma } { 2 \alpha _ { X } + d _ { X } } \sum _ { i = 1 } ^ { \infty } \frac { n ^ { - \frac { \gamma } { 2 } } } { \beta _ { Y } + \frac { \gamma } { \beta _ { X } } } } \\ { \displaystyle \left( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \log n \cdot \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } } } + \log n \cdot n ^ { - \frac { \gamma } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } \right) , } & { f o r i s \frac { \alpha _ { X } + \gamma } { 2 \alpha _ { X } + d _ { X } } \sum _ { i = 1 } ^ { \infty } \frac { n ^ { - \frac { \gamma } { 2 } } } { \beta _ { Y } } } \end{array} \right. , } \end{array}
$$

for some constant $C _ { \gamma }$ independent of $n$ .

The proof of Theorem 6 is provided in Appendix D.3.1 (for Regime 2) and Appendix D.3.2 (for Regime 3b). The estimator $\hat { \mathcal { I } } ( f , x )$ leverages the strengths of density regression performed in both the ambient space and the latent space. By considering the wavelet expansion of $\textstyle { \mathcal { L } } ^ { 2 }$ -integrable functions, the task of estimating $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$ for $f \in \mathcal { L } ^ { 2 } ( \mathbb { R } ^ { D _ { Y } } )$ becomes equivalent to jointly estimating the coefficients $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ]$ over $\psi \in \bigcup _ { j \geq 0 } \overline { { \Psi } } _ { j } ^ { D _ { Y } }$ . Moreover, when $f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ , the collection of wavelet coefficients $\left\{ \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ] : \ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } \right\}$ contribute to $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$ with different levels of importance, depending on the resolution level $j$ and the smoothness parameter $\gamma$ . Notably, the difficulty of jointly estimating the coefficients over $\Psi _ { j } ^ { D _ { Y } }$ decreases as $j$ becomes smaller, due to the lower complexity of the basis functions at coarse scales. This property can be exploited in density regression over the ambient space by using a joint mean regression strategy, with a function class $\boldsymbol { S } _ { j } ^ { \dagger }$ of reduced complexity selected for lower levels $j$ . Accordingly, the conditional density estimator ${ \widehat { u } } ( y | x )$ defined in (6) is particularly effective for estimating $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ]$ when $f$ is smooth (i.e., for large $\gamma$ ). Specifically, by choosing $\begin{array} { r } { J = \left\lceil \frac { 1 } { d _ { Y } } \log _ { 2 } \left( \frac { n } { \log n } \right) \right\rceil } \end{array}$ , there exists an appropriate choice of the function families $\{ \boldsymbol { S } _ { j } ^ { \dagger } \} _ { j \in \mathrm { 0 } \cup [ J ] }$ such that the estimator u(y | x) achieves the minimax upper bound for all γ ≥ dY αX2α+dX under Regime 2. This result is detailed in Theorem 9 in Appendix B.2.1.

However, without explicitly estimating the manifold, this approach integrates manifold estimation and conditional density estimation into a single process of joint mean regression. While efficient, it may overlook finer local details of the supporting manifolds, and can fail to achieve minimax optimality for small $\gamma$ , where the loss $d _ { \gamma }$ becomes more sensitive to such fine-scale structures and misalignments arising from manifold estimation. In contrast, density regression in the latent space—augmented by an explicit manifold estimation step—can achieve the minimax rate when $\gamma$ is small. Specifically, by setting $\begin{array} { r } { J = \big \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \alpha _ { Y } / \alpha _ { X } } \cdot \log _ { 2 } \bigl ( \frac { n } { \log n } \bigr ) \big \rceil } \end{array}$ , the mixture of generative models given by (7) serving as an estimator for the conditional distribution $\mu _ { Y \mid x } ^ { * }$ , can simultaneously achieve minimax optimality for all $\gamma \leq 1$ under Regime 2, up to logarithmic factors, as detailed in Theorem 10 of Appendix B.2.2.

On the other hand, for large values of $\gamma$ , this encoder–decoder–based manifold estimation approach fails to fully exploit the higher-order smoothness of the test functions. In such cases, better convergence rates are achievable through alternative strategies. The estimator defined in (9) addresses this tradeoff by combining the strengths of both approaches: it uses density regression in the ambient space to estimate the coarse-scale component, while employing density regression in the latent space to recover finer-scale details.

# 6 Discussion

In this paper, we explored the minimax rate of distribution regression under a non-parametric setting, where both the response variable and the covariate may exhibit low-dimensional structures. Our analysis extended to settings in which the conditional response space varies with the covariate, thereby generalizing the classical manifold estimation and support recovery problems into a manifold regression framework. The minimax rates derived for manifold regression rely on regularity assumptions in the covariate space, including the condition that the covariate density is bounded away from zero. An important direction for future work is to explore the possibility of relaxing or eliminating these assumptions, either through more refined analytical techniques or by adopting weaker evaluation metrics. Additionally, the rate-optimal procedure for distribution regression developed in this work is primarily theoretical, designed to establish the minimax upper bound. Developing a computationally efficient algorithm that achieves similar statistical guarantees remains an open challenge. For example, our procedure employs density regression in the ambient space to capture global structure and in the latent space to resolve fine-scale details. Given the conceptual similarities between our multiscale approach and techniques used in forward-backward diffusion models Song et al. [2020], Ho et al. [2020], it would be worthwhile to investigate whether ideas from our estimator could enhance score-based generative models Chen et al. [2022], Oko et al. [2023], Tang et al. [2024]. Specifically, one could envision a new class of diffusion-based models that estimate global structure in the conditional distribution using diffusion processes in the ambient space Song et al. [2020], while capturing fine-scale features via latent diffusion methods Rombach et al. [2022].

# References

Theory of Function Spaces III. Birkhauser Basel, Basel, 2006. URL ¨ https://link.springer. com/book/10.1007/3-7643-7582-5. 20, 38, 115   
Eddie Aamari and Clement Levrard. Nonasymptotic rates for manifold, tangent space and curvature ´ estimation. The Annals of Statistics, 47(1):177 – 204, 2019. URL https://doi.org/10.1214/ 18-AOS1685. 5, 6, 9, 15, 16, 17, 128, 135, 141, 148, 149   
Abdelrahman Abdelhamed, Marcus A Brubaker, and Michael S Brown. Noise flow: Noise modeling with conditional normalizing flows. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 3165–3173, 2019. 4   
Armen Aghajanyan, Luke Zettlemoyer, and Sonal Gupta. Intrinsic dimensionality explains the effectiveness of language model fine-tuning. arXiv preprint arXiv:2012.13255, 2020. 3   
Grigory Antipov, Moez Baccouche, and Jean-Luc Dugelay. Face aging with conditional generative adversarial networks. In 2017 IEEE international conference on image processing (ICIP), pages 2089–2093. IEEE, 2017. 15   
Iskander Azangulov, George Deligiannidis, and Judith Rousseau. Convergence of diffusion models under the manifold hypothesis in high-dimensions. arXiv preprint arXiv:2409.18804, 2024. 5   
Andrew Barron, Lucien Birge, and Pascal Massart. Risk bounds for model selection via penalization. ´ Probability theory and related fields, 113:301–413, 1999. 8   
David M Bashtannyk and Rob J Hyndman. Bandwidth selection for kernel conditional density estimation. Computational Statistics & Data Analysis, 36(3):279–298, 2001. 3, 4   
Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Schonlieb, and Christian Etmann. Conditional image ¨ generation with score-based diffusion models, 2021. 13

Aurelien Bellet, Amaury Habrard, and Marc Sebban. A survey on metric learning for feature vectors ´ and structured data. arXiv preprint arXiv:1306.6709, 2013. 3

Clement Berenfeld and Marc Hoffmann. Density estimation on an unknown submanifold. 2021. ´ 5

Clement Berenfeld, Paul Rosa, and Judith Rousseau. Estimating a density near an unknown manifold:´ a bayesian nonparametric approach. The Annals of Statistics, 52(5):2081–2111, 2024. 5

Anirban Bhattacharya, Debdeep Pati, and David Dunson. Anisotropic function estimation using multibandwidth gaussian processes. Annals of statistics, 42(1):352, 2014. 8

Peter J Bickel and Bo Li. Local polynomial regression on unknown manifolds. In Complex datasets and inverse problems, pages 177–186. Institute of Mathematical Statistics, 2007. 35

Blair Bilodeau, Dylan J. Foster, and Daniel M. Roy. Minimax rates for conditional density estimation via empirical entropy. The Annals of Statistics, 51(2):762 – 790, 2023. URL https://doi.org/ 10.1214/23-AOS2270. 5, 12

C.M. Bishop. Pattern Recognition and Machine Learning. Information Science and Statistics. Springer, 2006. ISBN 9780387310732. URL https://books.google.com/books?id $\underline { { \underline { { \mathbf { \Pi } } } } } =$ kTNoQgAACAAJ. 3

Minshuo Chen, Kaixuan Huang, Tuo Zhao, and Mengdi Wang. Score approximation, estimation and distribution recovery of diffusion models on low-dimensional data. arXiv preprint arXiv:2302.07194, 2023a. 5

Minshuo Chen, Song Mei, Jianqing Fan, and Mengdi Wang. An overview of diffusion models: Applications, guided generation, statistical rates and optimization. arXiv preprint arXiv:2404.07771, 2024. 5

Sitan Chen, Sinho Chewi, Jerry Li, Yuanzhi Li, Adil Salim, and Anru R Zhang. Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions. arXiv preprint arXiv:2209.11215, 2022. 5, 27

Sitan Chen, Giannis Daras, and Alex Dimakis. Restoration-degradation beyond linear diffusions: A non-asymptotic analysis for ddim-type samplers. In International Conference on Machine Learning, pages 4462–4484. PMLR, 2023b. 5

Alejandro Cholaquidis, Ricardo Fraiman, and Leonardo Moreno. Level set and density estimation on manifolds. Journal of Multivariate Analysis, 189:104925, 2022. 5

Ronald Christensen et al. Plane answers to complex questions, volume 35. Springer, 2002. 3

Salman UH Dar, Mahmut Yurt, Levent Karacan, Aykut Erdem, Erkut Erdem, and Tolga Cukur. Image synthesis in multi-contrast mri with conditional generative adversarial networks. IEEE transactions on medical imaging, 38(10):2375–2388, 2019. 4

Ingrid Daubechies. Orthonormal bases of compactly supported wavelets. Communications on pure and applied mathematics, 41(7):909–996, 1988. 20

Ingrid Daubechies. Ten lectures on wavelets. SIAM, 1992. 37, 115

Valentin De Bortoli, James Thornton, Jeremy Heng, and Arnaud Doucet. Diffusion schrodinger bridge ¨ with applications to score-based generative modeling. Advances in Neural Information Processing Systems, 34:17695–17709, 2021. 5

John DiNardo and Justin L Tobias. Nonparametric density and regression estimation. Journal of Economic Perspectives, 15(4):11–28, 2001. 3

Xin Ding, Yongwei Wang, Zuheng Xu, William J Welch, and Z Jane Wang. Ccgan: Continuous conditional generative adversarial networks for image generation. In International conference on learning representations, 2021. 15

Vincent Divol. Minimax adaptive estimation in manifold inference. Electronic Journal of Statistics, 15 (2):5888–5932, 2021. 5

Vincent Divol. Measure estimation on manifolds: an optimal transport approach. Probability Theory and Related Fields, 183(1):581–647, 2022. 5, 9, 10, 35

Manfredo P Do Carmo. Differential geometry of curves and surfaces: revised and updated second edition. Courier Dover Publications, 2016. 9

Jaap Eldering. Normally Hyperbolic Invariant Manifolds: The Noncompact Case. Atlantis Press, Paris, 2013. 124

Jianqing Fan and Tsz Ho Yim. A crossvalidation method for estimating conditional densities. Biometrika, 91(4):819–834, 2004. 4

Herbert Federer. Curvature measures. Transactions of the American Mathematical Society, 93(3):418– 491, 1959. 9

Reinaldo Padilha Franc¸a, Ana Carolina Borges Monteiro, Rangel Arthur, and Yuzo Iano. An overview of deep learning in big data, image, and signal processing in the modern digital age. Trends in deep learning methodologies, pages 63–87, 2021. 3

Hengyu Fu, Zhuoran Yang, Mengdi Wang, and Minshuo Chen. Unveil conditional diffusion models with classifier-free guidance: A sharp statistical theory. arXiv preprint arXiv:2403.11968, 2024. 5

Christopher R. Genovese, Marco Perone-Pacifico, Isabella Verdinelli, and Larry Wasserman. Manifold estimation and singular deconvolution under Hausdorff loss. The Annals of Statistics, 40(2):941 – 963, 2012a. URL https://doi.org/10.1214/12-AOS994. 19

Christopher R Genovese, Marco Perone-Pacifico, Isabella Verdinelli, and Larry Wasserman. Manifold estimation and singular deconvolution under hausdorff loss. 2012b. 5

Christopher R Genovese, Marco Perone-Pacifico, Isabella Verdinelli, and Larry Wasserman. Minimax manifold estimation. The Journal of Machine Learning Research, 13(1):1263–1291, 2012c. 5, 15, 16

Evarist Gine and Richard Nickl. ´ Mathematical Foundations of Infinite-Dimensional Statistical Models. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2015. 38

Sixue Gong, Vishnu Naresh Boddeti, and Anil K Jain. On the intrinsic dimensionality of image representations. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 3987–3996, 2019. 3

Joseph Guinness and Dorit Hammerling. Compression and conditional emulation of climate model output. Journal of the American Statistical Association, 113(521):56–67, 2018. 3

Wolfgang Hardle. ¨ Applied nonparametric regression. Number 19. Cambridge university press, 1990. 3

Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in neural information processing systems, 33:6840–6851, 2020. 27

Michael P. Holmes, Alexander G. Gray, and Charles Lee Isbell. Fast nonparametric conditional density estimation. In Proceedings of the Twenty-Third Conference on Uncertainty in Artificial Intelligence, UAI’07, page 175–182, Arlington, Virginia, USA, 2007. AUAI Press. ISBN 0974903930. 4

Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A Efros. Image-to-image translation with conditional adversarial networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 1125–1134, 2017. 4

Rafael Izbicki and Ann B Lee. Nonparametric conditional density estimation in a high-dimensional regression setting. Journal of Computational and Graphical Statistics, 25(4):1297–1316, 2016. 3, 5

Anne Kao and Steve R Poteet. Natural language processing and text mining. Springer Science & Business Media, 2007. 3

Diederik P Kingma. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114, 2013. 24

Roger Koenker. Quantile regression, volume 38. Cambridge university press, 2005. 3

Michael Kohler and Sophie Langer. On the rate of convergence of fully connected deep neural network regression estimates. The Annals of Statistics, 49(4):2231–2249, 2021. 4

Smita Krishnaswamy, Matthew H Spitzer, Michael Mingueneau, Sean C Bendall, Oren Litvin, Erica Stone, Dana Pe’er, and Garry P Nolan. Conditional density-based analysis of t cell signaling in single-cell data. Science, 346(6213):1250689, 2014. 3

Fabian Latorre, Leello Tadesse Dadi, Paul Rolland, and Volkan Cevher. The effect of the intrinsic dimension on the generalization of quadratic classifiers. Advances in Neural Information Processing Systems, 34:21138–21149, 2021. 3

Holden Lee, Jianfeng Lu, and Yixin Tan. Convergence for score-based generative modeling with polynomial complexity. Advances in Neural Information Processing Systems, 35:22870–22882, 2022. 5

Holden Lee, Jianfeng Lu, and Yixin Tan. Convergence of score-based generative modeling for general data distributions. In International Conference on Algorithmic Learning Theory, pages 946–985. PMLR, 2023. 5

Gen Li and Yuling Yan. Adapting to unknown low-dimensional structures in score-based diffusion models. arXiv preprint arXiv:2405.14861, 2024. 5

Gen Li, Yuting Wei, Yuxin Chen, and Yuejie Chi. Towards non-asymptotic convergence for diffusionbased generative models. In The Twelfth International Conference on Learning Representations, 2024a. 5

Gen Li, Yuting Wei, Yuejie Chi, and Yuxin Chen. A sharp convergence theory for the probability flow odes of diffusion models. arXiv preprint arXiv:2408.02320, 2024b. 5

Michael Li, Matey Neykov, and Sivaraman Balakrishnan. Minimax optimal conditional density estimation under total variation smoothness. Electronic Journal of Statistics, 16(2):3937 – 3972, 2022a. URL https://doi.org/10.1214/22-EJS2037. 13

Michael Li, Matey Neykov, and Sivaraman Balakrishnan. Minimax optimal conditional density estimation under total variation smoothness. Electronic Journal of Statistics, 16(2):3937–3972, 2022b. 3, 5, 6

Q. Li and J.S. Racine. Nonparametric Econometrics: Theory and Practice. 2007. ISBN 9780691121611. URL https://books.google.com/books?id $\equiv$ BI_PiWazY0YC. 3

Tengyuan Liang. How well generative adversarial networks learn distributions. Journal of Machine Learning Research, 22(228):1–41, 2021. URL http://jmlr.org/papers/v22/20-911. html. 11, 47

Shiao Liu, Xingyu Zhou, Yuling Jiao, and Jian Huang. Wasserstein generative learning of conditional distribution. arXiv preprint arXiv:2112.10039, 2021. 5

Clive Loader. Local regression and likelihood. Springer Science & Business Media, 2006. 35

Yongyi Lu, Yu-Wing Tai, and Chi-Keung Tang. Attribute-guided face generation using conditional cyclegan. In Proceedings of the European conference on computer vision (ECCV), pages 282–297, 2018. 15

Yves Meyer. Wavelets and operators: volume 1. Number 37. Cambridge university press, 1992. 20, 37, 115

Mehdi Mirza and Simon Osindero. Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784, 2014. 4, 5

Alfred Muller. Integral probability metrics and their generating classes of functions. ¨ Advances in applied probability, 29(2):429–443, 1997. 4, 11

Klutchnikoff Nicolas. On the adaptive estimation of anisotropic functions. HAL, 2005, 2005. 8

Andriy Norets and Debdeep Pati. Adaptive bayesian estimation of conditional densities. Econometric Theory, 33(4):980–1012, 2017. 5

Kazusato Oko, Shunta Akiyama, and Taiji Suzuki. Diffusion models are minimax optimal distribution estimators. arXiv preprint arXiv:2303.01861, 2023. 5, 27

Arkadas Ozakin and Alexander Gray. Submanifold density estimation. Advances in neural information processing systems, 22, 2009. 5

Jim R Parker. Algorithms for image processing and computer vision. John Wiley & Sons, 2010. 3

Phillip Pope, Chen Zhu, Ahmed Abdelkader, Micah Goldblum, and Tom Goldstein. The intrinsic dimension of images and its impact on learning. arXiv preprint arXiv:2104.08894, 2021. 3

Nikita Puchkin and Vladimir Spokoiny. Structure-adaptive manifold estimation. Journal of Machine Learning Research, 23(40):1–62, 2022. URL http://jmlr.org/papers/v23/21-0338. html. 15

Mar´ıa Xose Rodr ´ ´ıguez-Alvarez, Vanda In ´ acio, and Nadja Klein. Density regression via dirichlet process ´ mixtures of normal structured additive regression models. Statistics and Computing, 35(2):47, 2025. 3

Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bjorn Ommer. High- ¨ resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 10684–10695, June 2022. 24, 27

M. Rosenblatt. Conditional probability density and regression estimators. In Paruchuri R. Krishnaiah, editor, Multivariate analysis, II, pages 25–31. Academic Press, New York, 1969. (Dayton, OH, 17–22 June 1968). MR:254987. 4

Jonas Rothfuss, Fabio Ferreira, Simon Walther, and Maxim Ulrich. Conditional density estimation with neural networks: Best practices and benchmarks, 2019. 5

Ruslan Salakhutdinov. Learning deep generative models. Annual Review of Statistics and Its Application, 2(1):361–385, 2015. 4

Johannes Schmidt-Hieber. Deep relu network approximation of functions on a manifold. arXiv preprint arXiv:1908.00695, 2019. 4

Johannes Schmidt-Hieber. Nonparametric regression using deep neural networks with ReLU activation function. The Annals of Statistics, 48(4):1875 – 1897, 2020. 4

Shashank Singh, Ananya Uppal, Boyue Li, Chun-Liang Li, Manzil Zaheer, and Barnabas P ´ oczos. Non- ´ parametric density estimation under adversarial losses. Advances in Neural Information Processing Systems, 31, 2018. 4, 11

Kihyuk Sohn, Honglak Lee, and Xinchen Yan. Learning structured output representation using deep conditional generative models. Advances in neural information processing systems, 28, 2015. 4

Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. arXiv preprint arXiv:2011.13456, 2020. 13, 22, 27

Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. In International Conference on Learning Representations, 2021. 4

Charles J Stone. Optimal global rates of convergence for nonparametric regression. The annals of statistics, pages 1040–1053, 1982. 6, 12

Paul Suetens. Fundamentals of medical imaging. Cambridge university press, 2017. 3

Rong Tang and Yun Yang. Minimax rate of distribution estimation on unknown submanifolds under adversarial losses. The Annals of Statistics, 51(3):1282 – 1308, 2023a. 4, 6, 9, 10, 11, 14, 70, 73, 141, 144

Rong Tang and Yun Yang. Minimax rate of distribution estimation on unknown submanifolds under adversarial losses. The Annals of Statistics, 51(3):1282–1308, 2023b. 4, 5, 22

Rong Tang and Yun Yang. Adaptivity of diffusion models to manifold structures. 27th International Conference on Artificial Intelligence and Statistics, 2024. 5

Rong Tang, Lizhen Lin, and Yun Yang. Conditional diffusion models are minimax-optimal and manifold-adaptive for conditional distribution estimation, 2024. URL https://arxiv.org/ abs/2409.20124. 13, 27

Rong Tang, Lizhen Lin, and Yun Yang. Conditional diffusion models are minimax-optimal and manifold-adaptive for conditional distribution estimation. The Thirteenth International Conference on Learning Representations, 2025. 5

Yusuke Tashiro, Jiaming Song, Yang Song, and Stefano Ermon. Csdi: Conditional scorebased diffusion models for probabilistic time series imputation. In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan, editors, Advances in Neural Information Processing Systems, volume 34, pages 24804–24816. Curran Associates, Inc., 2021. URL https://proceedings.neurips.cc/paper_files/paper/2021/file/ cfe8504bda37b575c70ee1a8276f3486-Paper.pdf. 13

Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, and Bernhard Schoelkopf. Wasserstein auto-encoders. arXiv preprint arXiv:1711.01558, 2017. 24

Hans Triebel. Bases in function spaces, sampling, discrepancy, numerical integration, volume 11. European Mathematical Society, 2010. 20

Alexandre B. Tsybakov. Introduction to Nonparametric Estimation. Springer New York, New York, NY, 2009. 48, 50, 73

Roman Vershynin. High-dimensional probability: An introduction with applications in data science, volume 47. Cambridge university press, 2018. 139

Martin J Wainwright. High-dimensional statistics: A non-asymptotic viewpoint, volume 48. Cambridge university press, 2019. 49, 96, 138, 139, 145

Peng Wang, Huijie Zhang, Zekai Zhang, Siyi Chen, Yi Ma, and Qing Qu. Diffusion models learn low-dimensional distributions via subspace clustering. arXiv preprint arXiv:2409.02426, 2024. 5

Ruiping Wang, Shiguang Shan, Xilin Chen, and Wen Gao. Manifold-manifold distance with application to face recognition based on image set. In 2008 IEEE Conference on Computer Vision and Pattern Recognition, pages 1–8. IEEE, 2008. 15

Wenjuan Wang, Martin Kiik, Niels Peek, Vasa Curcin, Iain J Marshall, Anthony G Rudd, Yanzhong Wang, Abdel Douiri, Charles D Wolfe, and Benjamin Bray. A systematic review of machine learning models for predicting outcomes of stroke with structured data. PloS one, 15(6):e0234722, 2020. 3

Christina Winkler, Daniel Worrall, Emiel Hoogeboom, and Max Welling. Learning likelihoods with conditional normalizing flows. arXiv preprint arXiv:1912.00042, 2019. 4

Xi Yang, Aokun Chen, Nima PourNejatian, Hoo Chang Shin, Kaleb E Smith, Christopher Parisien, Colin Compas, Cheryl Martin, Anthony B Costa, Mona G Flores, et al. A large language model for electronic health records. NPJ digital medicine, 5(1):194, 2022. 3

ChengXiang Zhai and Sean Massung. Text data management and analysis: a practical introduction to information retrieval and text mining. Morgan & Claypool, 2016. 3

Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF international conference on computer vision, pages 3836– 3847, 2023. 4

Lijun Zhao, Huihui Bai, Jie Liang, Bing Zeng, Anhong Wang, and Yao Zhao. Simultaneous color-depth super-resolution with conditional generative adversarial networks. Pattern Recognition, 88:356–369, 2019. 4

Xingyu Zhou, Yuling Jiao, Jin Liu, and Jian Huang. A deep generative approach to conditional sampling. Journal of the American Statistical Association, pages 1–12, 2022. 5

# Supplementary Materials to “Minimax Optimal Rates for Regression on Manifolds and Distributions”

Notation: We adopt the notations in the manuscript, and further introduce the following additional notations for the technical proofs. For a set $U \subset \mathbb { R } ^ { d }$ , we write $\mathbf { 1 } _ { U } ( x )$ the indicator function of $x \in U$ . For two vectors $a , b \in \mathbb { R } ^ { d }$ , we use $\begin{array} { r } { \| a - b \| = \sqrt { \textstyle \sum _ { j = 1 } ^ { d } ( a _ { i } - b _ { i } ) ^ { 2 } } } \end{array}$ to denote the Euclidean distance between them. For two sequences $\left\{ a _ { n } \right\}$ and $\left\{ b _ { n } \right\}$ , the notations $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ imply $a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n$ . Additionally, $a _ { n } \asymp b _ { n }$ indicates that both $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ are hold. For sequences $\{ a _ { n } \} , \{ b _ { n } \} , \{ c _ { n } \}$ We write $a _ { n } = b _ { n } + \mathcal { O } ( c _ { n } )$ if $\| a _ { n } - b _ { n } \| \lesssim c _ { n }$ . For a function $f : \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } }$ , we use $\mathbf { J } _ { f } ( x )$ to denote the Jacobian matrix of $f$ evaluate at $x$ , so that the $( i , j )$ element of $\mathbf { J } _ { f } ( x )$ is $\frac { \partial f _ { i } ( x ) } { \partial x _ { j } }$ . We denote the $d$ -dimensional zero vector as $\mathbf { 0 } _ { d }$ and may omit the subscript $d$ when it does not lead to ambiguity. For a function $f : U \to \mathbb { R }$ , we use $\operatorname { s u p p } ( f ) = \{ x \in U : f ( x ) \neq 0 \}$ to denote the support of $f$ .

# A Omitted Definitions and Results in Main Text

# A.1 Smooth Submanifold

This subsection provides an introduction to Riemannian submanifolds, Intuitively speaking, a manifold is a topological space that locally resembles the Euclidean space. A submanifold in the ambient space $\mathbb { R } ^ { D }$ can be viewed as a nonlinear “subspace” and is formally defined as follows.

Definition 6 (Submanifold). A subset $\mathcal { M }$ of $\mathbb { R } ^ { D }$ is a $d$ -dimensional Riemannian submanifold if for every point $x$ in $\mathcal { M }$ , there exists a neighbourhood $V$ of $x$ on $\mathcal { M }$ and an open set $U \subseteq \mathbb { R } ^ { d }$ , such that that there exists a homeomorphism $\xi$ that maps $U$ to $V$ , that is, $\xi : U \to V$ is bijective and both $\xi$ and $\xi ^ { - 1 }$ are continuous maps. Moreover, the differential $D _ { y } \xi$ of $\xi ( \cdot )$ at $y$ exists and be injective for every $y \in U$ .† We call $( V , \xi )$ a local coordinate chart of $\mathcal { M }$ near $x$ , and $\xi$ a coordinate map around $x$ . We refer to $D$ as the ambient dimension and $d$ as the intrinsic dimension of $\mathcal { M }$ .

Definition 7 (Atlas). A collection of $d$ -dimensional charts $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ is called an atlas on $\mathcal { M }$ if 1. $\begin{array} { r } { \mathcal { M } = \bigcup _ { \lambda \in \Lambda } U _ { \lambda } } \end{array}$ . 2. Each chart $( U _ { \lambda } , \varphi _ { \lambda } )$ in atlas $\mathcal { A }$ consists of a homeomorphism $\varphi _ { \lambda } : U _ { \lambda } \to \widetilde { U } _ { \lambda }$ , from an open set $U _ { \lambda } \subset \mathcal { M }$ to an open set $\widetilde { U } _ { \lambda } \subset \mathbb { R } ^ { d }$ . 3. Any two charts $( U , \varphi )$ and $( V , \psi )$ in atlas $\mathcal { A }$ are compatible, meaning that the transition map $\varphi \circ \psi ^ { - 1 } : \psi ( U \cap V ) \to \varphi ( U \cap V )$ is a diffeomorphism.

The tangent space $T _ { \theta } \mathcal { M }$ is the linearization of $\mathcal { M }$ at $\theta$ . When $\mathcal { M }$ is an embedded submanifold of a Euclidean space $\mathbb { R } ^ { D }$ , the tangent spaces of $\mathcal { M }$ are linear subspaces of $\mathbb { R } ^ { D }$ that pass through the origin and have dimensions that equal the intrinsic dimension $d$ of $\mathcal { M }$ . The formal definition is as follows.

Definition 8 (Tangent space). For a submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ , we denote the tangent space of $\mathcal { M }$ at $\theta$ as $T _ { \theta } { \mathcal { M } } = \{ c ^ { \prime } ( 0 ) | c : I \to { \mathcal { M } }$ is $C ^ { 1 }$ -smooth around 0 and $c ( 0 ) = \theta \}$ , where $I$ is any open interval containing $t = 0$ . That is, $v$ is in $T _ { \theta } \mathcal { M }$ if and only if there exists a smooth curve on $\mathcal { M }$ passing through $x$ with velocity $v$ . Vectors in $T _ { \theta } \mathcal { M }$ are called tangent vectors to $\mathcal { M }$ at $\theta$ . The collection $T \mathcal M = \{ ( \theta , v ) : \theta \in \mathcal M , v \in T _ { \theta } \mathcal M \}$ is called the tangent bundle of $\mathcal { M }$ .

To manage multiple local coordinate charts in the underlying data manifold representation, we will use the mathematical technique of partition of unity as defined below.

Definition 9 (partition of unity). A partition of unity subordinate to altas $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ is $a$ collection of smooth functions $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ on $\mathcal { M }$ so that

1. $0 \le \rho _ { \lambda } \le 1$ for all $\lambda \in \Lambda ,$ , and $\begin{array} { r } { \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( x ) = 1 } \end{array}$ for all $x \in \mathcal { M }$ .

2. $\operatorname { s u p p } ( \rho _ { \lambda } ) \subset U _ { \lambda }$ for any $\lambda \in \Lambda .$ .

3. Each point $x \in \mathcal { M }$ has a neighborhood which intersects $\operatorname { s u p p } ( \rho _ { \lambda } )$ for only finitely many $\lambda \in \Lambda$ .

Using the partition of unity, one can glue constructions in the local charts to form a global construction on the manifold. Such a global construction usually does not rely on the choice of the partition of unity. Conversely, the partition of unity enables the decomposition of a global estimation problem into local ones, which resembles the data localization in local (polynomial) regression [Loader, 2006, Bickel and Li, 2007].

Definition 10 (Riemannian volume measure of submanifold). Suppose $\mathcal { A } = \{ ( U _ { \lambda } , \varphi _ { \lambda } ) \} _ { \lambda \in \Lambda }$ is an atlas on a submanifold $\mathcal { M }$ and $\{ \rho _ { \lambda } \} _ { \lambda \in \Lambda }$ is a partition of unity subordinate to altas $\mathcal { A }$ . Then the Riemannian volume measure $\mu _ { \mathcal { M } }$ can be written as

$$
\mathrm { d } \mu _ { \mathcal { M } } = \sum _ { \lambda \in \Lambda } \rho _ { \lambda } ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \sqrt { \operatorname* { d e t } ( J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ^ { T } J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ) } \mathrm { d } z ,
$$

where $\mathrm { d } z$ is the Lebesgue measure on $\mathbb { R } ^ { d }$ . A measure $\mu$ on $\mathcal { M }$ is said to have a density $f$ (with respect to the volume measure $\mu _ { \mathcal { M } } )$ if for any measurable subset $A \subset { \mathcal { M } }$ ,

$$
\mu ( A ) = \int _ { A } f \mathrm { d } \mu _ { \mathcal { M } } = \sum _ { \lambda \in \Lambda } \int _ { \varphi _ { \lambda } ( U _ { \lambda } \cap A ) } \rho _ { \lambda } ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \cdot f ( \varphi _ { \lambda } ^ { - 1 } ( z ) ) \sqrt { \operatorname* { d e t } ( J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ^ { T } J _ { \varphi _ { \lambda } ^ { - 1 } } ( z ) ) } \mathrm { d } z .
$$

Note that the Riemannian volume measure and the density function with respect to it are independent of the choice of atlas and partition of unity.

Definition 11 (Reach). The reach of a closed subset $\mathcal { M } \subset \mathbb { R } ^ { D }$ is defined as

$$
r _ { M } = \operatorname* { s u p } \Big \{ \varepsilon \Big | \forall x \in \mathcal { M } ^ { \varepsilon } , t h e r e \arcsin i s t s \operatorname* { m i d } u e \ y \in \mathcal { M } , s o t h a t \ \mathrm { d i s t } ( x , \mathcal { M } ) = \| x - y \| \Big \} .
$$

where $\begin{array} { r } { \mathrm { d i s t } ( z , \mathcal { M } ) = \operatorname* { i n f } _ { p \in \mathcal { M } } \| p - z \| } \end{array}$ denotes the distance function to $\mathcal { M }$ , and $\mathcal { M } ^ { \varepsilon } = \left\{ x \in \mathbb { R } ^ { D } : \mathrm { d i s t } ( x , \mathcal { M } ) < \varepsilon \right\}$ is the $\varepsilon$ -offset of $\mathcal { M }$ .

A lower bound on the reach prevents the manifold from becoming nearly self-intersecting and ensures a uniform upper bound on its curvature. We also restate the definition of a $\beta$ -smooth submanifold as described in Definition 3 of the main text for completeness.

Definition ( $\beta$ -Smooth submanifold). A $d$ -dimensional submanifold $\mathcal { M }$ in $\mathbb { R } ^ { D }$ is said to belong to the manifold class $\mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta } ( d , D )$ if: 1. $\mathcal { M }$ is closed; 2. it has reach larger than $\tau$ ; and 3. for all $y _ { 0 } \in \mathcal { M }$ , there exists a neighborhood $U _ { y _ { 0 } }$ of $y _ { 0 }$ on $\mathcal { M }$ so that the projection $\widetilde { \pi } _ { y _ { 0 } } : \mathcal { M }  T _ { y _ { 0 } } \mathcal { M }$ defined by $\widetilde { \pi } _ { y _ { 0 } } ( y ) = \mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } } ( y - y _ { 0 } )$ , when restricted to $U _ { y _ { 0 } }$ , is a diffeomorphism, with inverse function $\phi _ { y _ { 0 } }$ defined on $\mathbb { B } _ { T _ { y _ { 0 } } , M } ( 0 , \tau _ { 1 } )$ , and $\phi _ { y _ { 0 } } \in \mathcal { H } _ { L , D } ^ { \beta } ( \mathbb { B } _ { T _ { y _ { 0 } } \mathcal { M } } ( 0 , \tau _ { 1 } ) )$ .

Geometric Properties of $\beta$ -smooth submanifolds with positive reach: (see for example, Lemma 20 of Divol [2022])Suppose $\mathcal { M } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta } ( d , D )$ with $\beta \geq 2$ . Then

1. If $\begin{array} { r } { h \leq \frac { \tau } { 4 } } \end{array}$ , then there exist some constants $( c , C )$ so that for any $x \in \mathcal { M }$ ,

$$
c h ^ { d } \leq \mathrm { v o l } _ { \mathcal { M } } ( \mathbb { B } _ { \mathcal { M } } ( x , h ) ) \leq C h ^ { d } ,
$$

where $\mathrm { v o l } _ { \mathcal { M } }$ denotes the volume measure of $\mathcal { M }$ .

$$
h \leq r _ { 0 } = \tau _ { 1 } \wedge ( ( \tau \wedge L ) / 4 ) \mathrm { a n d } x \in \mathcal { M } , \mathbb { B } _ { \mathcal { M } } ( x , h ) \subset \phi _ { x } \big ( \mathbb { B } _ { T _ { x } \mathcal { M } } ( \mathbf { 0 } , h ) \big ) \subset \mathbb { B } _ { \mathcal { M } } ( x , 8 h / 7 ) .
$$

3. If $\mathrm { P r o j } _ { \mathcal { M } } ( z ) = x$ for some $z$ satisfying $\mathrm { d i s t } ( z , \mathcal { M } ) < \tau$ , then $z - x \in T _ { x } \mathcal { M } ^ { \perp }$ .

# A.2 Smooth submanifold family and smooth conditional distributions

Firstly we recall the definition of $( \beta _ { Y } , \beta _ { X } )$ -smooth manifold family defined in Definition 4 of the main text.

Definition $( ( \beta _ { Y } , \beta _ { X } )$ -smooth submanifold family). A submanifold family $\left\{ \mathcal { M } _ { Y | x } : \ x \ \in \ \mathcal { M } _ { X } \right\}$ is said to belong to $\mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d , D , \mathcal { M } _ { X } ) .$ , if for any $x \in \mathcal { M } _ { X }$ : 1. the manifold $\mathcal { M } _ { Y \mid x }$ is a closed $d .$ - dimensional submanifold in $\mathbb { R } ^ { D }$ ; 2. it has reach larger that $\tau$ ; and 3. if, for any $w _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in$ $\mathcal { M }$ , there exists a neighborhood $U _ { \omega _ { 0 } }$ of $y _ { 0 }$ on $\mathcal { M } _ { Y }$ , so that for any $x \in \mathbb { B } _ { M _ { X } } ( x _ { 0 } , \tau )$ , the function $\widetilde \pi _ { w _ { 0 } } : \mathcal { M } _ { Y } \to T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ defined by $\widetilde { \pi } _ { w _ { 0 } } ( y ) \ = \ \mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } } } \left( y - y _ { 0 } \right)$ , when restricted to $U _ { \omega _ { 0 } } \cap$ $\mathcal { M } _ { Y \mid x }$ , is a diffeomorphism with inverse function $\phi _ { \omega _ { 0 } , x } ( \cdot )$ defined on $\mathbb { B } _ { T _ { y _ { 0 } } , \mathcal { M } _ { Y \mid x _ { 0 } } } ( 0 , \tau _ { 1 } )$ . Moreover, the function $\Phi _ { \omega _ { 0 } } : \mathbb { B } _ { T _ { y _ { 0 } } , { \cal M } _ { Y | x _ { 0 } } } ( 0 , \tau _ { 1 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )  \mathbb { R } ^ { D _ { Y } }$ defined as $\Phi _ { \omega _ { 0 } } ( z , x ) = \phi _ { \omega _ { 0 } , x } ( z )$ belongs to $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { T _ { y _ { 0 } } , \mathcal { M } _ { Y \mid x _ { 0 } } } ( 0 , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$

We have the following lemma which provides an equivalent definition of $( \beta _ { Y } , \beta _ { X } )$ -smooth manifold family, whose proof is given in Appendix E.5.

Lemma 3. (Properties of Smooth submanifold family) Suppose $\beta _ { Y } \geq 2$ and $\beta _ { Y } \geq \beta _ { X }$ . Consider a submanifold faimly $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \}$ , the following statements are equivalent:

1. There exist constants $( \tau , \tau _ { 1 } , L )$ so that $\{ \mathcal { M } _ { Y | x } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } ) .$

2. (Existence of $x$ -dependent $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth local charts) There exist constants $( \widetilde { \tau } , \widetilde { \tau } _ { 1 } , \widetilde { L } )$ so that for any $w _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , there exists a neighborhood $\widetilde { U } _ { y _ { 0 } }$ of $y _ { 0 }$ on $\mathcal { M } _ { Y }$ such that for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \widetilde { \tau } )$ , it holds that $\mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \widetilde { \tau } ) \subset \widetilde { U } _ { y _ { 0 } } \cap \mathcal { M } _ { Y | x } \subset \mathbb { R } ^ { D _ { Y } }$ and there exists a uniformly $\widetilde { L }$ -Lipschitz diffeomorphism $\widetilde { Q } _ { \omega _ { 0 } } ( \cdot , x )$ that maps $\widetilde { U } _ { y _ { 0 } } \cap { \mathcal { M } } _ { Y | x } t o { \mathbb { B } } _ { { \mathbb { R } } ^ { d _ { Y } } } ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } )$ with inverse denoted as de $\widetilde { g } _ { \omega _ { 0 } , x } ( \cdot )$ $\widetilde { Q } _ { \omega _ { 0 } } ( y _ { 0 } , x _ { 0 } ) = \mathbf { 0 }$ and the fsfies that $\widetilde { G } _ { \omega _ { 0 } } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \widetilde { \tau } )  \mathbb { R } ^ { D _ { Y } }$ $\widetilde { G } _ { \omega _ { 0 } } ( z , x ) = \widetilde { g } _ { \omega _ { 0 } , x } ( z )$ $\widetilde { G } _ { \omega _ { 0 } } \in \mathcal { H } _ { \widetilde { L } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } \bigl ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } \bigr ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \widetilde { \tau } ) \bigr )$

3. (Solution manifold with $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth defining functions) There exist constants $( \overline { { \tau } } , \overline { { \tau } } _ { 1 } , \overline { { L } } )$ so that $\mathcal { H } _ { \overline { { L } } , D _ { Y } - d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) ) s _ { c }$ $\mathcal { M } _ { Y } ~ \subset ~ \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , \overline { { L } } )$ and for any $\omega _ { 0 } ~ = ~ ( x _ { 0 } , y _ { 0 } ) ~ \in \mathcal { M }$ o that for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } )$ , there exists a function , it holds that $\mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { 0 } , \overline { { \tau } } ) =$ $F _ { \omega _ { 0 } } \in$ $\{ y \in \bar { \mathbb { B } } _ { \mathbb { R } ^ { D } Y } \left( y _ { 0 } , \overline { { \tau } } \right) : \ F _ { \omega _ { 0 } } ( y , x ) = \mathbf { 0 } \}$ , and for any $( x , y ) \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } )$ , it holds that $J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) ^ { T } \succeq \overline { { { \tau } } } _ { 1 } I _ { D _ { Y } - d _ { Y } } .$ .

As a crucial intermediate result for proving Lemma 3, the following lemma states that if $x$ -dependent $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth local charts exist, then for an appropriate choice of $V$ , the function $V ^ { T } ( \cdot - y _ { 0 } )$ , when restricted to $\mathcal { M } _ { Y \mid x }$ , will be locally invertible around $y _ { 0 }$ .

Lemma 4. Suppose the family of submanifolds $\{ \mathcal { M } _ { Y | x } : x \in \mathcal { M } _ { X } \}$ meets the conditions specified in Point 2 of Lemma 3, with $\beta _ { Y } \geq \operatorname* { m a x } ( 2 , \beta _ { X } )$ . For any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , consider $P _ { \omega _ { 0 } }$ as the projection matrix onto $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } \mathcal { Y } 0 }$ and let $V _ { \omega _ { 0 } } ~ \in ~ \mathbb { R } ^ { D _ { Y } \times d _ { Y } }$ be an arbitrary orthonormal matrix such that $V _ { \omega _ { 0 } } ^ { T } P _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ~ \succeq ~ \tau _ { 0 } I _ { d _ { Y } }$ for some positive constant $\tau _ { 0 }$ . Then, there exist constants $( \tau , \tau _ { 1 } , L )$ such that for any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , there is a subset $U _ { \omega _ { 0 } }$ of $\mathcal { M } _ { Y }$ satisfying the following conditions: 1. For any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) , \ \mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { 0 } , \tau ) \subset U _ { \omega _ { 0 } } \cap \mathcal { M } _ { Y \mid x }$ . 2. The function $V _ { \omega _ { 0 } } ^ { T } ( \cdot - y _ { 0 } )$ , when restricted to domain $U _ { \omega _ { 0 } } \cap \mathcal { M } _ { Y | x }$ , is a diffeomorphism onto its image, with the inverse function denoted by by $g _ { \omega _ { 0 } , x }$ $G _ { \omega _ { 0 } } ( z , x ) = g _ { \omega _ { 0 } , x } ( z )$ , defined on $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ Y,belongs to . 3. The function $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$ $G _ { \omega _ { 0 } } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )  \mathbb { R } ^ { D _ { Y } }$ . , defined

The proof of Lemma 4 is given in Appendix E.6.

For ease of notation, we make the following definition to the smooth conditional distributions on submanifolds.

to bfold Definition 12. (Smooth conditional distributions) The conditional distribution e a $\mathcal { C } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ or any with r $x \ \in \ \mathcal { M } _ { X } , \ \mu _ { Y | x } ^ { * }$ is supported ome measure of $\{ \mu _ { Y | x } ^ { * } \} _ { x \in \mathcal { M } _ { X } }$ is said ubmani-so that $\mathcal { M } _ { Y \mid x }$ $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ $\mathcal { M } _ { Y \mid x }$ $\{ \mathcal { M } _ { Y | x } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ and there exists a function . $\overline { { u } } ^ { * } \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } ) \mathrm { ~ } s o$ $u ^ { * } ( y | x ) = \overline { { u } } ^ { * } ( y , x )$ $( x , y ) \in { \mathcal { M } }$

The following lemma, whose proof is given in Appendix E.7, shows that the smoothness of the density function of $\mu _ { Y \mid x } ^ { * }$ w.r.t. the volume measure of $\mathcal { M } _ { Y \mid x }$ is equivalent to the smoothness of the latent distributions defined through the $x$ -dependent local charts of the submanifolds.

LemConswith quivondiand een smbution , then $\{ \mu _ { Y | x } ^ { * } \} _ { x \in \mathcal { M } _ { X } }$ nctioned on satis $\{ \mathcal { M } _ { Y | x } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ $\beta _ { Y } ~ \geq ~ 2$ $\beta _ { Y } ~ \ge ~ \beta _ { X }$ $\alpha _ { Y } , \alpha _ { X } \ > \ 0$ $\alpha _ { Y } ~ \ge ~ \alpha _ { X }$ $\beta _ { Y } \ge \alpha _ { Y } + 1$ $\begin{array} { r } { \beta _ { X } \ge \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ , we have

1. If for any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , the push-forward measure $[ \mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } } } \left( \cdot - y _ { 0 } \right) ] _ { \# } ( \mu _ { Y | x } ^ { * } | _ { U _ { \omega _ { 0 } } \cap \mathcal { M } _ { Y | x } } )$ exists with a density function with respect to the volume measure of $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } } y _ { 0 }$ , denoted as $\nu _ { \omega _ { 0 } } ( \cdot | x )$ , and it satisfies that $\nu _ { \omega _ { 0 } } ( z , | , x ) \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { B } _ { T _ { \smash { \mathcal { M } _ { Y | x _ { 0 } } } y _ { 0 } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) ) }$ . Then there exists $L ^ { \prime }$ so that $\{ \mu _ { Y | x } ^ { * } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { C } _ { \tau , \tau _ { 1 } , L ^ { \prime } } ^ { \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ .

2. If $\{ \mu _ { Y | x } ^ { * } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { C } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ . Then there exists a constant $L ^ { \prime }$ so that for any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ and any $\widetilde { Q } _ { \omega _ { 0 } }$ that satisfies the conditions specified in Point 2 of Lemma 3, the density of the push forward measure $[ \widetilde { Q } _ { \omega _ { 0 } } ( \cdot , x ) ] _ { \# } ( \mu _ { Y | x } ^ { * } | _ { \widetilde { U } _ { Y | x } ^ { \omega _ { 0 } } } )$ with respect to the Lebesgue measure on $\mathbb { R } ^ { d _ { Y } }$ , denoted as $\widetilde { \nu } _ { \omega _ { 0 } } ( \cdot | x )$ , exists and satisfies $\begin{array} { r } { \widetilde { \nu } _ { \omega _ { 0 } } ( z , | , x ) \in \mathcal { H } _ { L ^ { \prime } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) ) . } \end{array}$

The following result shows that smooth conditional distributions on submanifold can be expressed as mixture of conditional generative models.

Lemma 6. (Expressing $\mathcal { C } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ $\mu _ { Y \mid X } ^ { * }$ as mixture of conditional generative models) Suppose . For anyn for any $\tau _ { 2 }$ $0 < \tau _ { 2 } \leq ( \tau \wedge \tau _ { 1 } ) / 4$ $\{ ( x _ { k } ^ { * } , y _ { k } ^ { * } ) \} _ { k = 1 } ^ { K ^ { * } } \subset \mathcal { M }$ $\{ \mu _ { Y | x } ^ { * } \} _ { x \in \mathcal { M } _ { X } } \in$ $\tau _ { 2 }$ $\mathcal { M }$ $k \in [ K ^ { * } ]$ $G _ { [ k ] } ^ { * } \in \mathcal { H } _ { L _ { 1 } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } ) .$ $v _ { [ k ] } ^ { \ast } ( z , x ) \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ with some constant $L _ { 1 }$ , such that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ and $x \in$ $\mathcal { M } _ { X } , v _ { [ k ] } ^ { \ast } ( z , x ) = 0 $ if either $\| x - x _ { k } ^ { * } \| \ge \sqrt { 2 } \tau _ { 2 }$ or $\| G _ { [ k ] } ^ { * } ( z , x ) - y _ { k } ^ { * } \| \ge \sqrt { 2 } \tau _ { 2 }$ . Moreover, for any $x \in \mathcal { M } _ { X }$ and any continuous function $g : \mathcal { M } _ { Y | x }  \mathbb { R } ,$ , it holds that

$$
\mathbb { E } _ { \boldsymbol { y } \sim \boldsymbol { \mu } _ { Y \mid x } ^ { * } } [ \boldsymbol { g } ( \boldsymbol { y } ) ] = \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } _ { Y } } ( \mathbf { 0 } , \tau _ { 1 } ) } \boldsymbol { g } ( G _ { [ k ] } ^ { * } ( \boldsymbol { z } , \boldsymbol { x } ) ) \boldsymbol { v } _ { [ k ] } ^ { * } ( \boldsymbol { z } | \boldsymbol { x } ) \mathrm { d } \boldsymbol { z } .
$$

The proof of Lemma 6 is given in Appendix E.8.

# A.3 Wavelet

In this section, we give a brief introduction to the wavelet. Let $\phi { \mathfrak { M } }$ and $\phi _ { \mathfrak { F } }$ be a compactly supported wavelet and scaling function, respectively, for example Daubechies wavelets [Daubechies, 1992, Meyer, 1992]. This implies that

$$
\left\{ \begin{array} { l l } { \phi _ { \mathfrak { F } } ( x - k ) } & { j = 0 , k \in \mathbb { Z } , } \\ { 2 ^ { ( j - 1 ) / 2 } \phi _ { \mathfrak { M } } ( 2 ^ { j - 1 } x - k ) , } & { j \in \mathbb { N } ^ { + } , k \in \mathbb { Z } , } \end{array} \right.
$$

is an orthonormal basis of ${ \mathcal { L } } ^ { 2 } ( \mathbb { R } )$ , where we use $\textstyle { \mathcal { L } } ^ { 2 }$ to denote the set of square integrable functions. To obtain a basis of $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ for an integer $d > 1$ , set

$$
{ \mathfrak { G } } = \{ { \mathfrak { F } } , { \mathfrak { M } } \} ^ { d } \backslash \{ ( { \mathfrak { F } } , \dots , { \mathfrak { F } } ) \} .
$$

Then for any multi-index $k \in  { \mathbb { Z } ^ { d } }$ , the level zero basis $\phi _ { k } ^ { [ d ] }$ is obtained by translating the $d$ -fold tensor product $\phi _ { \mathfrak { F } } ^ { \otimes d }$ by $k$ as $\begin{array} { r } { \phi _ { k } ^ { [ d ] } ( x ) = \prod _ { i = 1 } ^ { d } \phi _ { \mathfrak { F } } ( x _ { i } - k _ { i } ) } \end{array}$ for $x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { R } ^ { d }$ , and for any $j \geq 1$ , the level $j$ basis $\{ \psi _ { l j k } ^ { [ d ] } : l \in [ 2 ^ { d } - 1 ] \}$ with translation $k$ is any ordering of the following $2 ^ { d } - 1$ functions,

$$
\psi _ { g j k } ^ { [ d ] } ( x ) = 2 ^ { \frac { d ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { d } \phi _ { g _ { i } } ^ { [ d ] } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) , \quad \forall g \in \mathfrak { G } .
$$

This gives the orthornormal basis

$$
\left\{ \begin{array} { l l } { \phi _ { k } ^ { [ d ] } ( x ) , } & { j = 0 , l = 0 , k \in \mathbb { Z } ^ { d } , } \\ { \psi _ { l j k } ^ { [ d ] } ( x ) , } & { j \in \mathbb { N } ^ { + } , l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } . } \end{array} \right.
$$

Denote $\overline { { \Psi } } _ { 0 } ^ { d } = \{ \phi _ { k } ^ { [ d ] } ( \cdot ) : k \in \mathbb { Z } ^ { d } \}$ as the set of level zero basis and $\overline { { \Psi } } _ { j } ^ { d } = \{ \psi _ { l j k } ^ { [ d ] } ( \cdot ) : l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } \}$ as the set of level $j$ basis for $j \in \mathbb { N } ^ { + }$ . We can define the Besov space $B _ { p , q } ^ { s } ( \mathbb { R } ^ { d } )$ consists of functions $f$ that admits the wavelet expansion

$$
f ( x ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d } } f _ { \psi } \psi ( x ) ,
$$

where $\begin{array} { r } { f _ { \psi } : = \int f ( x ) \psi ( x ) \mathrm { d } x } \end{array}$ , and is equipped with the norm

$$
\begin{array} { r } { \| f \| _ { B _ { p , q } ^ { s } } : = \left\| 2 ^ { j s } 2 ^ { d j ( \frac { 1 } { 2 } - \frac { 1 } { p } ) } \| f _ { j } \| _ { p } \right\| _ { q } , } \end{array}
$$

with $f _ { j } = \left\{ f _ { \psi } \right\} _ { \psi \in \overline { { \Psi } } _ { j } ^ { d } }$ . The following Theorem collects the relationship between the Besov space and Holder space. ¨

Theorem 7. (Theorem 1.122 of Tri [2006] and Proposition 4.3.30 of Gine and Nickl ´ [2015]) Let $\alpha > 0$ if $\alpha$ is not integer, then

$$
\begin{array} { r } { \mathcal { H } ^ { \alpha } ( \mathbb { R } ^ { d } ) = B _ { \infty , \infty } ^ { \alpha } ( \mathbb { R } ^ { d } ) ; } \end{array}
$$

if α is integer, then

$$
B _ { 1 , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset \mathcal { H } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) \subset B _ { \infty , \infty } ^ { \alpha } (  { \mathbb { R } } ^ { d } ) .
$$

Focusing on the Holder space, we can find a wavelet basis that satisfies the following property. ¨

Lemma 7. For any positive integer $\alpha$ , there exists an orthonormal basis $\textstyle \bigcup _ { j \geq 0 } { \overline { { \Psi } } } _ { j } ^ { d }$ for $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ , so that there exist constants $C _ { R } , C _ { L } , C _ { L } ^ { \prime } , C _ { L } ^ { \dagger } , C _ { L } ^ { \dagger } , C _ { W } , C _ { I }$ such that for any integer $j \geq 0$ ,

1. (Regularity) $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } | \psi ^ { ( l ) } ( x ) | \leq C _ { R } 2 ^ { j | l | + \frac { d j } { 2 } } } \end{array}$ holds for any $l \in \mathbb { N } _ { 0 } ^ { d } w i t h \ | l | \leq \alpha$ and $\psi \in \overline { { \Psi } } _ { j } ^ { d }$

2. (Locality) for any $\psi \in \overline { { \Psi } } _ { j } ^ { d }$ , there exists a rectangle $I _ { \psi }$ such that

(a) for any $l \in  { \mathbb { N } } _ { 0 } ^ { d } w i t h | l | \leq \alpha , \mathrm { s u p p } ( \psi ^ { ( l ) } ) \subset I _ { \psi }$ and the diameter of $I _ { \psi }$ is smaller than $C _ { L } 2 ^ { - j }$   
(b) $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d } } \mathbf { 1 } ( x \in I _ { \psi } ) \leq C _ { L } ^ { \prime } } \end{array}$   
(c) for any $R \geq 1$ , $\left| \{ \psi \in \overline { { \Psi } } _ { j } ^ { d } : I _ { \psi } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( 0 , R ) \neq \emptyset \} \right| \leq C _ { L } ^ { \dagger } R 2 ^ { j d } .$

$$
a n d x \in \mathbb { R } ^ { d } , \left| \{ \psi \in \overline { { \Psi } } _ { j } ^ { d } : I _ { \psi } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( x , 2 ^ { - ( j - 1 ) } ) \neq \emptyset \} \right| \leq C _ { L } ^ { \pm } .
$$

3. (Wavelet coefficients of smooth function) for any $\alpha _ { 1 } \leq \alpha _ { : }$ , $r > 0$ and $f \in \mathcal { H } _ { r } ^ { \alpha _ { 1 } } ( \mathbb { R } ^ { d } )$ , it holds for any $\psi \in \overline { { \Psi } } _ { j } ^ { d }$ that the wavelet coefficient $\begin{array} { r } { f _ { \psi } = \int _ { \mathbb R ^ { d } } f ( x ) \psi ( x ) \mathrm d x } \end{array}$ is bounded by $C _ { W } r 2 ^ { - { \frac { d j } { 2 } } - j \alpha _ { 1 } } \ i n$ absolute value.

4. (Index of Wavelet basis) for any $R ^ { \prime } > 0$ , let $\Psi _ { j } ^ { d } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( \mathbf { 0 } , R ^ { \prime } ) \neq \emptyset \} _ { \mathrm { : } }$ , then $\Psi _ { j } ^ { d }$ can be written as an index set

$$
\begin{array} { r } { \Psi _ { j } ^ { d } = \{ \psi _ { j \iota } ( \cdot ) : \iota \in \mathcal { I } _ { j } \subset [ 0 , 1 ] ^ { d + 1 } \} , } \end{array}
$$

where ${ \mathcal { I } } _ { j }$ is $C _ { I } 2 ^ { - j } / ( R ^ { \prime } + C _ { L } )$ -separated.

The proof of Lemma 7 is provided in Appendix E.1. The following lemma presents the wavelet truncation approximation for marginal smooth functions, the proof of which is given in Appendix E.3.

Lemma 8. Suppose $f \in \overline { { \mathcal { H } } } _ { L } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( { \mathbb R } ^ { d _ { 1 } } , { \mathbb R } ^ { d _ { 2 } } )$ . Consider two wavelet basis $\{ \overline { { \Psi } } _ { j } ^ { d _ { 1 } } \} _ { j \ge 0 }$ and $\{ \overline { { \Psi } } _ { j } ^ { d _ { 2 } } \} _ { j \ge 0 }$ that both satisfy the properties in Lemma 7 with smoothness $\alpha = \lceil \alpha _ { 1 } \lor \alpha _ { 2 } \rceil$ and constants $C _ { R } , C _ { L } , C _ { L } ^ { \prime } , C _ { L } ^ { \dagger } , C _ { L } ^ { \dagger } , C _ { W } , C _ { I } .$ It holds for any $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ and $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ that

$$
f ( \boldsymbol { x } , \boldsymbol { y } ) - \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \boldsymbol { \psi } \in \overline { { \mathbb { V } } } _ { j _ { 1 } } ^ { d _ { 1 } } } \sum _ { \boldsymbol { \psi } \in \overline { { \mathbb { V } } } _ { j _ { 2 } } ^ { d _ { 2 } } } f _ { \boldsymbol { \psi } , \boldsymbol { \psi } } \psi ( \boldsymbol { x } ) \phi ( \boldsymbol { y } ) \Big | \leq C _ { R } C _ { L } ^ { \prime } C _ { W } L \boldsymbol { 2 } ^ { - J _ { 1 } \alpha _ { 1 } } + \boldsymbol { 2 } ^ { d _ { 1 } } C _ { R } ^ { 3 } C _ { L } ^ { \prime } ^ { 2 } C _ { W } C _ { L } ^ { d _ { 1 } } L J _ { 1 } 2
$$

where $\begin{array} { r } { f _ { \psi , \phi } = \int _ { \mathbb { R } ^ { d _ { 2 } } } \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) \psi ( x ) \phi ( y ) \mathrm { d } x \mathrm { d } y . } \end{array}$ .

# A.4 Matching error for Joint Mean Regression

In this subsection, we present a general result for bounding the matching error in joint mean regression. This result will be frequently applied in the proofs of the main results that follow. Let $\Lambda$ be a countable set and consider a function class $\{ \psi _ { \lambda } ( \cdot ) \} _ { \lambda \in \Lambda }$ on $\mathbb { R } ^ { D _ { Y } }$ , the joint mean regression aim to find a ${ \widehat { S } } ( \lambda , x )$ that solves

$$
\underset { S \in \mathcal { S } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \lambda \in \Lambda } ( S ( \lambda , X _ { i } ) - \psi _ { \lambda } ( Y _ { i } ) ) ^ { 2 } ,
$$

where $s$ is a suitable approximation family for $S$ . This can be think of using the function ${ \widehat { S } } ( \lambda , X )$ that depend both on the index $\lambda$ and the covariate $X$ to form a global estimator to the conditional expectation of $\mathbb { E } [ \psi _ { \lambda } ( Y ) | X ]$ over $\lambda \in \Lambda , x \in \mathcal { M } _ { X }$ . We derive the following theorem to study the matching error of the joint mean regression, the proof of which is given in Appendix E.10.

Theorem 8. Suppose $\{ ( X _ { i } , Y _ { i } ) \} _ { i = 1 } ^ { n }$ are n i.i.d samples from $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ supported on $\mathcal { M }$ . Consider the estimator $\widehat { S } ( \cdot , \cdot )$ defined in (10). Assume that there exist positive constants $C , C _ { 1 }$ so that the following assumptions are satisfied:

1. It holds for any $\in \mathcal { S } \ t h a t \operatorname* { s u p } _ { ( x , y ) \in \mathcal { M } } \sum _ { \lambda \in \Lambda } S ( \lambda , x ) ^ { 2 } + | \psi _ { \lambda } ( y ) S ( \lambda , x ) | \leq C .$

2. Denote $\begin{array} { r } { \ell ( x , y , S ) = \sum _ { \lambda \in \Lambda } \| S ( \lambda , x ) \| ^ { 2 } - 2 \psi _ { \lambda } ( y ) ^ { T } S ( \lambda , x ) , } \end{array}$ , then for any $S , S ^ { \prime } \in { \mathcal { S } }$ , it holds that

$$
\mathbb { E } _ { \mu ^ { * } } \Big [ \big ( \ell ( X , Y , S ) - \ell ( X , Y , S ^ { \prime } ) \big ) ^ { 2 } \Big ] \leq C \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \lambda \in \Lambda } \big ( S ( \lambda , X ) - S ^ { \prime } ( \lambda , X ) \big ) ^ { 2 } \Big ] .
$$

3. Define the distance $d _ { n }$ as $\begin{array} { r } { d _ { n } ( S , S ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \ell ( X _ { i } , Y _ { i } , S ) - \ell ( X _ { i } , Y _ { i } , S ^ { \prime } ) ) ^ { 2 } } } \end{array}$ and $\mathbf { N } ( S , d _ { n } , \varepsilon )$ be the $\varepsilon$ -covering number of $s$ with respect to $d _ { n }$ , Then, for some terms $W _ { n } , T _ { n } > 1$ that may depend on $n$ , it holds for any $0 < \varepsilon \le \operatorname* { s u p } _ { S , S ^ { \prime } \in S } d _ { n } ( S , S ^ { \prime } )$ that

$$
\mathbf { N } ( S , d _ { n } , \varepsilon ) \leq ( \frac { T _ { n } } { \varepsilon } ) ^ { W _ { n } } .
$$

Then for any constant $c > 0$ , there exists a constant $C _ { 1 }$ so that it holds with probability at least $1 - n ^ { - c }$ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \widehat { S } ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( y ) ] \right) ^ { 2 } \right] } \\ & { \leq C _ { 1 } \displaystyle \frac { W _ { n } \left( \log n + \log T _ { n } \right) } { n } + C _ { 1 } \displaystyle \operatorname* { m i n } _ { S \in \mathcal { S } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( y ) ] \right) ^ { 2 } \right] . } \end{array}
$$

# B Details of Miniax Optimal Estimators

# B.1 Minimax Optimal Estimator for Regime 1

Consider a wavelet basis $\cup _ { j \geq 0 } \overline { { \Psi } } _ { j } ^ { D _ { Y } }$ that satisfies the properties stated in Lemma 7, where the parameter $\alpha$ is greater than $\lceil \alpha _ { Y } \rceil \vee \lceil \alpha _ { X } \rceil$ . For any $j \in \{ 0 \} \cup [ J ]$ with $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + D _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ , define $\Psi _ { j } ^ { D _ { Y } }$ as the subset of the wavelet basis $\cup _ { j \geq 0 } \overline { { \Psi } } _ { j } ^ { D _ { Y } }$ for which

$$
\Psi _ { j } ^ { D _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L ) \neq \emptyset \} .
$$

Consider a smooth transition function $\rho : \mathbb { R }  [ 0 , 1 ]$ defined by

$$
\rho ( t ) = \left\{ \begin{array} { c c } { 0 } & { | t | \geq 2 } \\ { 1 } & { | t | \leq 1 } \\ { \frac { 1 } { 1 + \exp ( \frac { 3 - 2 t } { ( t - 1 ) ( t - 2 ) } ) } } & { 1 < t < 2 } \\ { \frac { 1 } { 1 + \exp ( \frac { 2 t + 3 } { ( t + 1 ) ( 2 + t ) } ) } } & { - 2 < t < - 1 . } \end{array} \right.
$$

This function ensures $\rho ( t ) = 1$ for $t \in [ 0 , 1 ]$ and $\rho ( t ) = 0$ for $t \in [ 2 , \infty )$ . For any $j \in [ J ]$ , define a class of functions ${ \mathcal { S } } _ { j }$ on $\mathbb { R } ^ { D _ { X } }$ as

$$
\begin{array} { r l } & { { \mathscr C } _ { j } = \Bigg \{ S ( x ) = \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } a _ { i k } \left( x - b _ { i } \right) ^ { k } \rho \left( \frac { \| x - b _ { i } \| } { { \varepsilon } _ { j } ^ { \varepsilon } } \right) } { \sum _ { i = 1 } ^ { W _ { j } } \rho \left( \frac { \| x - b _ { i } \| } { { \varepsilon } _ { j } ^ { \varepsilon } } \right) + \frac { 1 } { n } } ; b _ { i } \in \mathbb B _ { \mathbb { R } ^ { D _ { X } } } \left( \mathbf { 0 } , L \right) , a _ { i k } \in [ - \frac { C } { 2 ^ { D _ { Y } / d } } ] , } \\ & { \quad { \mathrm { ~ f o r ~ a n y ~ } } i \in [ W _ { j } ] { \mathrm { ~ a n d ~ } } k \in \mathbb N _ { 0 } ^ { D _ { X } } \mathrm { ~ w i t h ~ } | k | < \alpha _ { X } \Bigg \} , } \end{array}
$$

where $\varepsilon _ { j } ^ { x } = 2 ^ { \frac { j D _ { Y } } { 2 \alpha _ { X } + d _ { X } } } { \big ( } { \frac { n } { \log n } } { \big ) } ^ { - { \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } }$ , $W _ { j } = C _ { 1 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ and $C , C _ { 1 }$ are large enough constants. Consider the estimator

$$
\widehat { u } _ { \psi } ( \cdot ) = \underset { S \in \mathcal { S } _ { j } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \psi ( Y _ { i } ) - S ( X _ { i } ) ) ^ { 2 } , \quad j \in \{ 0 \} \cup [ J ] , \psi \in \Psi _ { j } ^ { D _ { Y } } .
$$

Finally, define a conditional density estimator for $\mu _ { Y | x } ^ { * }$ as

$$
\widehat { u } \big ( \cdot | x \big ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \psi ( \cdot ) \widehat { u } _ { \psi } ( x ) .
$$

# B.2 Minimax Optimal Estimator for Regime 2

# B.2.1 Density regression in the ambient space

For any $j \in \mathbb N$ , define

$$
\Psi _ { j } ^ { D _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L ) \neq \emptyset \} ,
$$

where $\cup _ { j \geq 0 } \overline { { \Psi } } _ { j } ^ { D _ { Y } }$ 0 ΨDYj is a wavelet basis that satisfies the properties stated in Lemma 7 with the parameter $\alpha$ being greater than $\begin{array} { r } { \left\lceil \alpha _ { Y } \right\rceil \vee \left\lceil \alpha _ { X } \right\rceil \vee \left\lceil \frac { d _ { Y } \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } \right\rceil \vee \left\lceil \beta _ { Y } \right\rceil } \end{array}$ . For any $j \in \mathbb N$ , consider the estimator

$$
\widehat { S } _ { j } ^ { \dagger } ( \cdot , \cdot ) = \arg \operatorname* { m i n } _ { S \in S _ { j } ^ { \dagger } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y _ { i } ) - S ( \psi , X _ { i } ) ) ^ { 2 } .
$$

To construct the families $\boldsymbol { S } _ { j } ^ { \dagger }$ , we leverage the fact that, for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , the term

$$
\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } \left[ 2 ^ { j d _ { Y } - \frac { j D _ { Y } } { 2 } } \psi ( y ) \right] = \int _ { \mathcal { M } _ { Y } } 2 ^ { j d _ { Y } - \frac { j D _ { Y } } { 2 } } \psi ( y ) u ^ { * } ( y | x ) \mathrm { v o l } _ { \mathcal { M } _ { Y } } ( \mathrm { d } y ) ,
$$

where $\mathrm { v o l } _ { \mathcal { M } _ { Y } } ( \mathrm { d } y )$ denotes the volume measure on the manifold $\mathcal { M } _ { Y }$ , is ${ \mathcal { H } } ^ { \alpha _ { X } }$ -smooth as a function of $x$ and has a bounded Holder norm. As a result, each conditional expectation ¨ $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ]$ can be effectively approximated using local polynomial approximation techniques. Furthermore, since the response space $\mathcal { M } _ { Y }$ lies on a low-dimensional submanifold, only $O ( 2 ^ { d _ { Y } j } )$ of the functions $\psi ( \cdot )$ will have non-zero conditional means. This observation allows us to construct parametric families $\boldsymbol { S } _ { j } ^ { \dagger }$ whose complexity depends only on the level $j$ , the intrinsic dimensions $d _ { x } , d _ { Y }$ and the smoothness level $\alpha _ { X }$ . According to Lemma 7, for any $j \in \mathbb N$ , we can express $\Psi _ { j } ^ { D _ { Y } }$ using an index set as follows:

$$
\Psi _ { j } ^ { D _ { Y } } = \big \{ \psi _ { j \iota } ( \cdot ) : \iota \in \mathcal { I } _ { j } \subset [ 0 , 1 ] ^ { D _ { Y } + 1 } \big \} ,
$$

where ${ \mathcal { I } } _ { j }$ is a $c 2 ^ { - j }$ -separated set for some constant $c > 0$ . We denote the index of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ by ${ \mathcal { T } } _ { j } ( \psi )$ ; that is, for $\psi = \psi _ { j \iota }$ , we write ${ \mathcal { T } } _ { j } ( \psi ) = \iota$ . Then we define $\boldsymbol { S } _ { j } ^ { \dagger }$ as

$$
\begin{array} { r } { \mathcal { S } _ { j } ^ { \dagger } = \Bigg \{ S ( \psi , x ) = \frac { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k \in \mathbb { R } _ { 0 } ^ { D } x , | k | < \alpha x } a _ { i _ { 1 } i _ { 2 } k } ( x - b _ { i _ { 2 } } ) ^ { k } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) \rho \left( \frac { \| Z _ { j } ( \psi ) - e _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) } { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) \rho \left( \frac { \| Z _ { j } ( \psi ) - e _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) + \frac { 1 } { n } } : } \end{array}
$$

$$
b _ { i _ { 2 } } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L ) , a _ { i _ { 1 } i _ { 2 } k } \in [ - \frac { C } { 2 ^ { d _ { Y } j / 2 } } , \frac { C } { 2 ^ { d _ { Y } j / 2 } } ] , e _ { i _ { 1 } } \in [ 0 , 1 ] ^ { D _ { Y } + 1 } \mathrm { ~ f o r ~ a n y ~ } i _ { 1 } , i _ { 2 } , k \Bigg \} ,
$$

where $\rho$ is a smooth transition function defined in (11); $\begin{array} { r } { \varepsilon _ { j } ^ { y } = \frac { 2 ^ { - j } } { C _ { 1 } } } \end{array}$ and $\begin{array} { r } { \varepsilon _ { j } ^ { x } = 2 ^ { j d _ { Y } / \left( 2 \alpha _ { X } + d _ { X } \right) } \left( \frac { n } { \log { n } } \right) ^ { - 1 / \left( 2 \alpha _ { X } + d _ { X } \right) } } \end{array}$ are the bandwidth parameters in the $y$ and $x$ directions, respectively. The quantities $W _ { j } = \bar { C } _ { 3 } ( \varepsilon _ { j } ^ { y } ) ^ { - d _ { Y } }$ and $W _ { j } ^ { \prime } = C _ { 2 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ represent the number of local neighborhoods in $y$ and $x$ , respectively, over which the partition of unity is defined. The numbers $C , C _ { 1 } , C _ { 2 }$ , and $C _ { 3 }$ are sufficiently large constants. Now we define

$$
\widehat { u } ( y | x ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) \psi ( y ) .
$$

The measure ${ \widehat { u } } ( y \mid x ) \mathrm { d } y$ , when utilized directly as an estimator for the conditional distribution $\mu _ { Y \mid x } ^ { * }$ , can achieve minimax optimality under the condition when $\begin{array} { r } { \gamma > \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ . This is formally established in the theorem presented below.

Theorem 9. Let $\begin{array} { r } { J = \lceil \frac { 1 } { d _ { Y } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . With the choice of $\boldsymbol { \mathcal { S } } _ { j } ^ { \dagger }$ defined in (14), consider any distribution $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 2 }$ Y , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that, for any $\begin{array} { r } { \gamma > \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } Y ) } \big | \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } f ( y ) - \int _ { \mathbb { R } ^ { D } Y } f ( y ) \widehat { u } ( y \mid x ) \mathrm { d } y \big | \Big ] \lesssim ( \log n ) \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

The proof of Theorem 9 is given in Appendix D.1.

# B.2.2 Density regression in the latent space

We split the data into two subsets by considering $I _ { 1 } = [ \lfloor n / 2 \rfloor ]$ and $I _ { 2 } = [ n ] \backslash I _ { 1 }$ . Let $\{ \omega _ { k } = ( x _ { k } , y _ { k } ) \} _ { k = 1 } ^ { K }$ be a $\tau _ { 2 }$ -covering set of $\mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L )$ , where $\tau _ { 2 }$ is a sufficiently small absolute constant. Define

$$
{ \widehat { K } } = \{ k \in [ K ] : \exists i \in I _ { 1 } , \| ( x _ { i } , y _ { i } ) - \omega _ { k } \| \leq \sqrt { 2 } \tau _ { 2 } \} .
$$

Consider a wavelet basis $\textstyle \bigcup _ { j \geq 0 } { \overline { { \Psi } } } _ { j } ^ { d _ { Y } }$ that satisfies the properties of Lemma 7, where the parameter $\alpha$ is greater than $\lceil \alpha _ { Y } \rceil \vee \lceil \alpha _ { X } \rceil \vee \rceil \beta _ { Y } \rceil \vee \lceil \beta _ { X } \rceil$ . Then for any $j \in \mathbb N$ , we denote

$$
\Psi _ { j } ^ { d _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau _ { 2 } ) \neq \emptyset \} .
$$

For any $k \in { \widehat { \mathcal { K } } }$ , we consider the estimator

$$
\widehat { G } _ { [ k ] } , \widehat { V } _ { [ k ] } ) = \underset { \substack { G \in G ( D _ { \mathbb { Y } } , d _ { \mathbb { Y } } ) } } { \mathrm { a r g } \mathrm { m i n } } \ \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \Vert Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { k } ) , X _ { i } ) \Vert ^ { 2 } \mathbf { 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) \big ) \mathbf { 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { \mathbb { Y } } } } \big ) \mathbf { 1 } \big ( X _ { i } \in \mathbb { R } ^ { 1 } , \widehat { \mathbf { t } } _ { i \in I _ { 1 } } \big )
$$

where ${ \mathbb O } ( D _ { Y } , d _ { Y } ) = \{ A \in { \mathbb R } ^ { D _ { Y } \times d _ { Y } } : A ^ { T } A = I _ { d _ { Y } } \}$ . To clarify the selection of $\mathcal { G }$ , we note that the choice depends on whether the submanifold $\mathcal { M } _ { Y \mid x }$ varies with $x$ . Here in Regime 2, since $\mathcal { M } _ { Y \mid x }$ remains invariant across $x$ , we define $\mathcal { G }$ as a function class that operates solely on the latent space $\mathbb { R } ^ { d _ { Y } }$ and does not depend on the covariate. Given that the global manifold $\mathcal { M } _ { Y }$ is $\beta$ -smooth, we construct each function $\bar { G } : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R } ^ { D _ { Y } }$ in $\mathcal { G }$ by truncating the wavelet expansion of $\mathcal { H } ^ { \beta }$ -smooth functions at a finite resolution level. Specifically, the function class $\mathcal { G }$ is defined as

$$
\mathcal { G } = \bigg \{ G ( z , x ) = G ( z ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } }  g _ { \psi _ { 1 } } \psi _ { 1 } ( z ) : g _ { \psi _ { 1 } } \in [ - L _ { 1 } \delta _ { j _ { 1 } } , L _ { 1 } \delta _ { j _ { 1 } } ] ^ { D _ { Y } } \mathrm { f o r } \mathrm { e a c h } \psi _ { 1 } \bigg \} ,
$$

where $J _ { 1 } = \lceil \log _ { 2 } ( n ^ { - 1 / d _ { Y } } ) \rceil$ , $\delta _ { j _ { 1 } } = 2 ^ { - d _ { Y } j _ { 1 } / 2 - \left( j _ { 1 } \beta _ { Y } \right) }$ and $L _ { 1 }$ is a sufficiently large constant. Then we denote $\widehat { Q } _ { [ k ] } ( \cdot ) = \widehat { V } _ { [ k ] } ^ { T } ( \cdot - y _ { k } )$ . For any $k \in { \widehat { \mathcal { K } } }$ , $j \in \{ 0 \} \cup [ J ]$ and $\psi \in \Psi _ { j } ^ { d _ { Y } }$ , we consider the estimator

$$
\widehat { v } _ { k \psi } ( \cdot ) = \arg \operatorname* { m i n } _ { S \in \mathcal { S } _ { j } } \frac { 1 } { | I _ { 2 } | } \sum _ { i \in I _ { 2 } } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } ( \psi ( \widehat { Q } _ { [ k ] } ( Y _ { i } ) ) \rho _ { [ k ] } ( X _ { i } , Y _ { i } ) - S ( X _ { i } ) ) ^ { 2 } ,
$$

where $\begin{array} { r } { \rho _ { [ k ] } ( x , y ) = \frac { \rho ( \| ( x , y ) - ( x _ { k } , y _ { k } ) \| ^ { 2 } / \tau _ { 2 } ^ { 2 } ) } { \sum _ { k = 1 } ^ { K } \rho ( \| ( x , y ) - ( x _ { k } , y _ { k } ) \| ^ { 2 } / \tau _ { 2 } ^ { 2 } ) } } \end{array}$ with $\rho$ being defined in (11). Note that the construction of ${ \mathcal { S } } _ { j }$ in both Regime 2 and the later Regime 3b is based on the construction in Equation (12), originally developed for density regression in Euclidean space (Regime 1). The key modification is the substitution of the ambient dimension $D _ { Y }$ with the intrinsic dimension $d _ { Y }$ . Specifically, for any $j \in \{ 0 \} \cup [ J ]$ with $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ , define

$$
\begin{array} { r l } & { \mathcal { S } _ { j } = \Bigg \{ S ( x ) = \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D \chi } , | k | < \alpha _ { X } } a _ { i k } ( x - b _ { i } ) ^ { k } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } : } \\ & { \qquad b _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D \chi } } ( \mathbf { 0 } , L ) , a _ { i k } \in [ - \frac { C } { 2 ^ { d _ { Y } j / 2 } } , \frac { C } { 2 ^ { d _ { Y } j / 2 } } ] , \mathrm { f o r } \arg i , k \Bigg \} , } \end{array}
$$

where $W _ { j } = C _ { 1 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ , $\varepsilon _ { j } ^ { x } = 2 ^ { \frac { j d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \big ( \frac { n } { \log n } \big ) ^ { - \frac { 1 } { 2 \alpha _ { X } + d _ { X } } }$ , $C _ { 1 } , C$ are large enough constants and $\rho$ is a smooth transition function defined in (11). Then denote $\widehat { \nu } _ { [ k ] } ( \cdot | x )$ as the measure that has a density function $\begin{array} { r } { \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( \cdot ) \widehat { v } _ { k \psi } ( x ) } \end{array}$ with respect to the Lebesgue measure on $\mathbb { R } ^ { d _ { Y } }$ . We can define a mixture of conditional generative models $\begin{array} { r } { \sum _ { k \in \widehat { \mathcal { K } } } \widehat { G } _ { [ k ] } ( \cdot , x ) _ { \# } \widehat { \nu } _ { [ k ] } ( \cdot | x ) } \end{array}$ , which, as an estimator of the bconditional distribution, can achieve minimax optimality when $\gamma \leq 1$ , as detailed in the following theorem.

Theorem 10. Let $\begin{array} { r } { J = \big \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } \bigl ( \frac { n } { \log n } \bigr ) \big \rceil } \end{array}$ . With the choices of $\mathcal { G }$ and ${ \mathcal { S } } _ { j }$ defined in (17) and (19) respectively. Consider any distribution $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 2 } ^ { * }$ , it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n } } }$ that for any $\gamma \leq 1$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ f ( Y ) ] - \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \int _ { \mathbb { R } ^ { d _ { Y } } } f ( \widehat { G } _ { [ k ] } ( z , x ) ) \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) { \mathrm { d } } z | \Big ] } \\ & { \lesssim ( \log n ) ^ { 2 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } . } \end{array}
$$

The proof of Theorem 10 is given in Appendix D.2.

# B.2.3 Simultaneous minimax optimal estimator for $\gamma > 0$

Choose $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ hen we define an operator $\mathcal { I } ( f , x )$ such that for any con-$f : \mathbb { R } ^ { D _ { Y } } \xrightarrow { \sim } \mathbb { R }$ $\boldsymbol { x } \in \mathbb { R } ^ { D _ { X } }$

$$
\begin{array} { r l } & { \widehat { \mathcal { I } } ( f , x ) = \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D } } f _ { \psi } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) + \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { { \mathbb { Z } } } ^ { \bot } ( \widehat G _ { [ k ] } ( z ) ) \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) { \mathrm { d } } x , } \\ & { f _ { \psi } = \displaystyle \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) { \mathrm { d } } y , \quad f _ { J } ^ { \bot } ( y ) = f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) , } \end{array}
$$

where all notations are adopted from subsections B.2.1 and B.2.2. The estimator ${ \widehat { \mathcal { I } } } ( f , x )$ can achieve the upper bound specified in Theorem 6 (Regime 2). By utilizing $\widehat { \mathcal { I } } ( f , x )$ , we can also derive a valid conditional distribution estimator that is simultaneous optimal for all $\gamma > 0$ using the steps described below.

Consider the set $\Gamma = \{ \textstyle { \frac { 1 } { \log n } } , \frac { 2 } { \log n } , \cdot \cdot \cdot , \frac { s } { \log n } \}$ with $\begin{array} { r } { s = \lceil \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } \log n \rceil } \end{array}$ , and define

$$
\delta _ { n , \gamma } = C _ { \gamma } \Big ( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } \Big ) .
$$

For any $x \in \mathcal { M } _ { X }$ , consider the estimator

$$
\widehat { \mu } _ { Y | x } = \underset { \mu \in \mathcal { P } _ { Y } ^ { * } } { \arg \operatorname* { m i n } } \sum _ { \gamma \in \Gamma } \frac { 1 } { \delta _ { n , \gamma } } \cdot \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \Big [ \mathbb { E } _ { \mu } [ f ( y ) ] - \widehat { \mathcal { I } } ( f , x ) \Big ] ,
$$

where $\mathcal { P } _ { Y } ^ { * }$ includes all probability measures of $\mu$ that are supported on a submanifold $\mathcal { M } _ { Y }$ and have a density function $u ( \cdot )$ with respect to the volume measure of $\mathcal { M } _ { Y }$ such that $\mathcal { M } _ { Y } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } } ( d _ { Y } , D _ { Y } )$ $\mu \in \mathcal { H } _ { L } ^ { \alpha _ { Y } } ( \mathcal { M } _ { Y } )$ .

Corollary 1. With the choices of $\mathcal { S } _ { j } ^ { \dagger } , \mathcal { S } _ { j } , \mathcal { G }$ defined in (14), (19) and (17) respectively, alongside $J =$ $\Big \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } \big ( \frac { n } { \log n } \big ) \Big \rceil$ . For any $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 2 } ^ { * }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that for any $\gamma > 0$ ,

$$
\mu _ { X } ^ { * } \left[ d _ { \gamma } ( \mu _ { Y | X } ^ { * } , \widehat { \mu } _ { Y | X } ) \right] \lesssim ( \log n ) ^ { 4 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \log n \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + \log n \cdot n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } .
$$

The proof of Corollary 1 is given in Appendix D.6.

# B.3 Minimax Optimal Estimator for Regime 3b

The estimator is formulated similarly to that for Regime 2. Choose $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ we define an operator $\widehat { \mathcal { I } } ( f , x )$ so that for any continuous function $f : \mathbb { R } ^ { D _ { Y } }  \mathbb { R }$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( \mathbf { 0 } , L )$ ,

$$
\begin{array} { r l } & { \widehat { \mathcal { I } } ( f , x ) = \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \mathbb { V } _ { j } ^ { D _ { Y } } } f _ { \psi } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) + \displaystyle \sum _ { k \in \widehat { \mathbb { K } } } \displaystyle \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z , x ) ) \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \mathrm { d } } \\ & { \quad \quad \Psi _ { j } ^ { D _ { Y } } = \displaystyle \{ \psi \in \widehat { \mathbb { V } } _ { j } ^ { D _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L ) \neq \emptyset \} , } \\ & { f _ { \psi } = \displaystyle \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) \mathrm { d } y , \quad f _ { J } ^ { \perp } ( y ) = f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) , } \end{array}
$$

where

$$
\widehat { G } _ { [ k ] } , \widehat { V } _ { [ k ] } ) = \underset { \substack { G \in G ( D _ { \mathbb { Y } } , d _ { \mathbb { Y } } ) } } { \mathrm { a r g } \mathrm { m i n } } \ \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \Vert Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { k } ) , X _ { i } ) \Vert ^ { 2 } \mathbf { 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) \big ) \mathbf { 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { \mathbb { Y } } } } \big ) \mathbf { 1 } \big ( X _ { i } \in \mathbb { R } ^ { 1 } , \widehat { \mathbf { t } } _ { i \in I _ { 1 } } \big )
$$

and $\widehat { S } _ { j } ^ { \dagger } ( \cdot , \cdot ) , \widehat { v } _ { k \psi } ( \cdot )$ are the estimators defined in (13) and (18) respectively. For the approximation families, ${ \mathcal { S } } _ { j }$ bis defined as in (19). For the family $\mathcal { G }$ , unlike Regime 2, Regime 3b involves scenarios where the submanifold $\mathcal { M } _ { Y \mid x }$ varies with $x$ . In this context, we construct $G$ using the tensor-product expansion of $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth functions. Specifically, we use the basis functions $\{ \psi _ { 1 } ( z ) \cdot \psi _ { 2 } ( x ) : \psi _ { 1 } \in$ $\mathsf { U } _ { j = 0 } ^ { \infty } \Psi _ { j } ^ { d _ { Y } }$ , $\psi _ { 2 } \in \bigcup _ { j = 0 } ^ { \infty } \overline { { \Psi } } _ { j } ^ { D _ { X } } \big \}$ and truncate the expansion at finite resolution levels. Accordingly, the function class $\mathcal { G }$ is defined as:

$$
\mathcal { G } = \{ G ( z , x ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \overline { { \Psi } } _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) :
$$

$$
\begin{array} { r } { g _ { \psi _ { 1 } \psi _ { 2 } } \in [ - L _ { 1 } \delta _ { j _ { 1 } j _ { 2 } } , L _ { 1 } \delta _ { j _ { 1 } j _ { 2 } } ] ^ { D _ { Y } } , \mathrm { f o r e a c h } \psi _ { 1 } , \psi _ { 2 } \} , } \end{array}
$$

$$
\begin{array} { r l } & { \mathfrak { r } \ : J _ { 1 } = \big \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } } } ) \big \rceil , \ : J _ { 2 } = \big \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { X } + d _ { Y } \frac { \beta _ { X } } { \beta _ { Y } } } } ) \big \rceil , \ : \delta _ { j _ { 1 } j _ { 2 } } = 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } - ( ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) ) } } \\ & { \Psi _ { j } ^ { d _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( { \bf 0 } , 2 \tau _ { 2 } ) \neq \emptyset \} . } \end{array}
$$

Now, let’s define the class $\boldsymbol { S } _ { j } ^ { \dagger }$ . Compared with Regime 2, the construction of $\boldsymbol { S } _ { j } ^ { \dagger }$ becomes more challenging in Regime 3b , where the conditional response space $\mathcal { M } _ { Y \mid x }$ varies with $x$ . In this setting, the conditional distribution $\mu _ { Y | x } ^ { * }$ can be expressed as a mixture of conditional generative models, $\begin{array} { r } { \mu _ { Y | x } ^ { * } = \sum _ { k = 1 } ^ { K ^ { * } } G _ { [ k ] } ^ { * } ( \cdot , x ) _ { \# } \nu _ { [ k ] } ^ { * } ( \cdot | x ) } \end{array}$ , where the generators $G _ { k } ^ { * }$ are $x$ -dependent and $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth (see Lemma 6 in Appendix A.2). The conditional mean

$$
\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } \left[ 2 ^ { j d _ { Y } - \frac { j D _ { Y } } { 2 } } \psi ( y ) \right] = \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { R } ^ { d _ { Y } } } 2 ^ { j d _ { Y } - \frac { j D _ { Y } } { 2 } } \psi \left( G _ { [ k ] } ^ { * } ( z , x ) \right) \nu _ { [ k ] } ^ { * } ( z | x ) \mathrm { d } z ,
$$

may not be uniformly ${ \mathcal { H } } ^ { \alpha _ { X } }$ -smooth in $x$ because the gradients of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ grow rapidly with $j$ . To address this challenge, we propose a hybrid strategy for constructing approximation families for $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ]$ , applied over all $\hat { \psi } \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathcal { M } _ { X }$ . The first component involves building parametric approximation families for the generators $G _ { [ k ] } ^ { * }$ and the latent distributions $\nu _ { [ k ] } ^ { * }$ , enabling direct approximation of the integral in (21). While effective for high-resolution levels (large $j$ ), this approach strategy similar to that used in Regime 2: for each does not fully exploit the smoothness properties of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ $\psi$ when $j$ is small. The second component adopts a , we treat $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( y ) ]$ as an ${ \mathcal { H } } ^ { \alpha _ { X } }$ -smooth function of $x$ , and use local polynomial approximations. However, as noted earlier, this strategy becomes less effective at large $j$ due to the growing instability of the wavelet basis functions.

To combine these two strategies in a resolution-adaptive manner, we first define parametric function classes for approximating $G _ { [ k ] } ^ { * }$ and $\nu _ { [ k ] } ^ { * }$ , where the number of parameters increases with $j$ , allowing the approximation accuracy to improve as resolution increases. We then use local polynomial approximations to model the residual, capturing smooth variation in $x$ . Specifically, letting ${ \mathcal T } _ { a } ( x ) =$ max ${ \bigl ( } - a , \operatorname* { m i n } ( a , x ) { \bigr ) }$ be a truncation operator and $\begin{array} { r } { \widetilde { \beta } _ { X } = \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ , and recall that for any $j \in \mathbb { N } , \Psi _ { j } ^ { D _ { Y } }$ can be written as an index set

$$
\Psi _ { j } ^ { D _ { Y } } = \{ \psi _ { j \iota } ( \cdot ) : \iota \in \mathcal { I } _ { j } \subset [ 0 , 1 ] ^ { D _ { Y } + 1 } \} ,
$$

where ${ \mathcal { I } } _ { j }$ is $c 2 ^ { - j }$ -separated and we use $\mathcal { T } _ { j } ( \boldsymbol { \psi } )$ to denote the index of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ (i.e., ${ \mathcal { T } } _ { j } ( \psi _ { j \iota } ) = \iota )$ . We define $\boldsymbol { S } _ { j } ^ { \dagger }$ for Regime 3b as the class of mappings $S : \Psi _ { j } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R }$ structured as follows:

$$
\begin{array} { l } { { \displaystyle \left. | \nabla _ { x } | \cdot | \bar { x } _ { 2 } | - \mathcal { T } _ { \mathrm { c r o s s } } \right. \left( \begin{array} { l } { { \nabla _ { y } \cdot | \bar { x } _ { 2 } | } } \\ { { \frac { 1 } { \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } } } \end{array} \right) \left( \begin{array} { l } { { \nabla _ { y } \cdot | \bar { x } _ { 2 } | } } \\ { { \frac { 1 } { \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } } } \end{array} \right) \sigma \Bigg ( \frac { | \bar { x } _ { 2 } | ( \cdot | \nabla _ { x } | ) - \bar { x } _ { 2 } | \cdot | } { \sigma } \Bigg ) \sigma \Bigg ( \frac { | \bar { x } _ { 2 } | ( \cdot | \nabla _ { x } | ) - \bar { x } _ { 2 } | \cdot | } { \sigma } \Bigg ) } } \\ { { \displaystyle \qquad + \left\{ \sum _ { h = 1 } ^ { \infty } \int _ { \bar { x } _ { 2 } \in \{ \bar { x } _ { 2 } \} } \left( \begin{array} { l } { { \frac { 2 \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } { 2 \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } } } \\ { { \frac { 1 } { \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } } } \end{array} \right) \left( \bar { x } _ { 2 } + \bar { x } _ { 2 } \right) \right\} \sigma _ { \kappa _ { h } \omega _ { 1 } , \bar { x } _ { 2 } | < \bar { x } _ { 2 } } \Bigg \} \bar { \sigma } _ { \kappa _ { h } \omega _ { 1 } } + \frac { \sum _ { h = 1 } ^ { \infty } \omega _ { \mathrm { i n } , \bar { x } _ { 2 } | } \sigma _ { \kappa } - \bar { x } _ { h } _ { 2 } | } { \mathrm { t a k } \sqrt { x - 1 } - \omega _ { \mathrm { i n } } ^ { 2 } } } } \\  \end{array}
$$

Here, $\rho$ is a smooth transition function defined in (11); $\widetilde { \Psi } _ { j } ^ { d _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) \neq \emptyset \}$ ; $K ^ { * }$ and $C _ { 1 }$ are sufficiently large constants. $\begin{array} { r } { \varepsilon _ { j } ^ { y } = \frac { 2 ^ { - j } } { C _ { 1 } } } \end{array}$ and $\begin{array} { r } { \varepsilon _ { j } ^ { x } = 2 ^ { j d _ { Y } / \left( 2 \alpha _ { X } + d _ { X } \right) } \left( \frac { n } { \log { n } } \right) ^ { - 1 / \left( 2 \alpha _ { X } + d _ { X } \right) } } \end{array}$ are the bandwidth parameters in the $y$ and $x$ directions, respectively. The quantities $\tilde { W _ { j } } = C _ { 3 } ( \varepsilon _ { j } ^ { y } ) ^ { - d _ { Y } }$ and $W _ { j } ^ { \prime } = C _ { 2 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ for large enough constants $C _ { 2 }$ and $C _ { 3 }$ . The parameters are constrained as follows: $g _ { k , i _ { 2 } , s , \psi , l } \in [ - C _ { 1 } , C _ { 1 } ] ^ { D _ { Y } }$ , $v _ { k , i _ { 2 } , s , \psi , l } \in \left[ - C _ { 1 } , C _ { 1 } \right]$ , and $a _ { i _ { 1 } i _ { 2 } l } \in \left[ - C _ { 1 } n , C _ { 1 } n \right]$ . The indices $e _ { i _ { 1 } i _ { 2 } }$ lie in $[ 0 , 2 ] ^ { D _ { Y } + 1 }$ . The centers $\{ b _ { 1 } , b _ { 2 } , \ldots , b _ { W _ { j } ^ { \prime } } \}$ are $\varepsilon _ { j } ^ { x }$ -separated, meaning that $\| b _ { i } - b _ { k } \| \geq \varepsilon _ { j } ^ { x }$ for any $i \neq k$ in $[ W _ { j } ^ { \prime } ]$ , and all lie within the ball $\mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L _ { 1 } )$ for a large enough constant $L _ { 1 }$ .

Similar to Regime 2, by utilizing $\widehat { \mathcal { I } } ( f , x )$ , we can also develop a conditional distribution estimator by considering the set $\Gamma = \{ \textstyle { \frac { 1 } { \log n } } , \frac { 2 } { \log n } , \cdot \cdot \cdot , \frac { s } { \log n } \}$ with $\begin{array} { r } { s = \lceil ( d _ { Y } \overset { - } { \vee } ( \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } ) ) \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } \log n \rceil } \end{array}$ + dXβX )) αX2αX+dX log n⌉, and define

$$
\mathfrak { H } _ { n , \gamma } = C _ { \gamma } \cdot \Big ( ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \log n ) \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + ( \log n ) \cdot n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } \Big ) .
$$

For any $x \in \mathcal { M } _ { X }$ , consider the estimator

$$
\widehat { \mu } _ { Y | x } = \underset { \mu \in \mathcal { P } _ { Y } ^ { * } } { \arg \operatorname* { m i n } } \sum _ { \gamma \in \Gamma } \frac { 1 } { \delta _ { n , \gamma } } \cdot \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \Big [ \mathbb { E } _ { \mu } [ f ( y ) ] - \widehat { \mathcal { I } } ( f , x ) \Big ] ,
$$

where $\mathcal { P } _ { Y } ^ { * }$ is defined as in Appendix B.2.2.

Corollary 2. With the choice of $\mathcal { S } _ { j } ^ { \dagger } , \mathcal { S } _ { j } , \mathcal { G }$ defined in (22), (19) and (20) respectively, alongside $J =$ $\Big \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } \big ( \frac { n } { \log n } \big ) \Big \rceil$ . For any $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * } \in \mathcal { P } _ { 3 } ^ { * }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that for any $\gamma > 0$ ,

$$
\Sigma _ { \mu _ { X } ^ { * } } [ d _ { \gamma } ( \mu _ { Y | X } ^ { * } , \widehat { \mu } _ { Y | X } ) ] \lesssim ( \log n ) ^ { 4 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \log n ) ^ { 2 } \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + ( \log n ) ^ { 2 } \cdot n ^ { - \frac { \gamma } { \beta _ { Y } } + \frac { \gamma } { 2 \alpha _ { Y } + d _ { X } } } .
$$

# C Proof for Distribution Regression with Euclidean Response

# C.1 Proof of Theorem 5 (minimax upper bound for Regime 1)

For any j ∈ {0} ∪ [J] with J = ⌈ 12αY +DY +dX αYα $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + D _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ , we define a class of mappings $S _ { j }$ on $\Psi _ { j } ^ { D _ { Y } } \times \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L )$ as

$$
\hat { \gamma } _ { j } = \left\{ S ( \psi , x ) = \sum _ { \widetilde { \psi } \in \Psi _ { J } ^ { D _ { Y } } } \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } a _ { i k } ^ { \widetilde { \psi } } ( x - b _ { i } ) ^ { k } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } \cdot \mathbf { 1 } ( \widetilde { \psi } = \psi ) : b _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbb { T } _ { 1 } ^ { 2 } / \mathbf { E } ) \right\} ,
$$

where $\varepsilon _ { j } ^ { x } = 2 ^ { \frac { j D _ { Y } } { 2 \alpha _ { X } + d _ { X } } } { \big ( } { \frac { n } { \log n } } { \big ) } ^ { - { \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } }$ , $W _ { j } = C _ { 1 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ and $C , C _ { 1 }$ are large enough constants. Then consider the estimator

$$
\widehat { S } _ { j } = \arg \operatorname* { m i n } _ { \substack { S \in { \mathcal { S } _ { j } } } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( \psi ( Y _ { i } ) - S ( \psi , X _ { i } ) ) ^ { 2 } .
$$

It is straightforward to verify that $\widehat { S } _ { j } ( \psi , x ) = \widehat { u } _ { \psi } ( x )$ for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathcal { M } _ { X }$ , and we can express

$$
\widehat { u } ( \cdot | x ) = \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \psi ( \cdot ) \widehat { S } _ { j } ( \psi , x ) .
$$

We then present the following lemma to bound the mean squared error between $\widehat { S } _ { j } ( \psi , x )$ and $u _ { \psi } ^ { * } ( x ) =$ $\begin{array} { r } { \int _ { \mathbb { R } ^ { D _ { Y } } } \boldsymbol { u } ^ { * } ( \boldsymbol { y } \vert \boldsymbol { x } ) \boldsymbol { \psi } ( \boldsymbol { y } ) \mathrm { d } \boldsymbol { y } } \end{array}$ , where $u ^ { * } ( y \mid x )$ is the density function of $\mu _ { Y \mid x } ^ { * }$ with respect to the Lebesgue measure on $\mathbb { R } ^ { D _ { Y } }$ .

Lemma 9. Suppose $\mu ^ { * } \in \mathcal { P } _ { 1 } ^ { * }$ and with the choices of $S _ { j }$ defined in (23), there exists a constant $C$ so that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that for any $j \in [ J ]$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \bigg [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \bigl ( \widehat { S } _ { j } ( \psi , X ) - u _ { \psi } ^ { * } ( X ) \bigr ) ^ { 2 } \bigg ] \leq C 2 ^ { \frac { 2 j \alpha _ { X } D _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \big ( \frac { n } { \log n } \big ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

The proof of Lemma 9 is given in Appendix C.3. For ease of notation, we define ${ \widehat { S } } _ { j } ( \psi , x ) = 0$ for any $j > J$ . Then, the estimator ${ \widehat { u } } ( y \mid x )$ can be rewritten as

$$
\widehat { u } ( y | x ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \psi ( y ) \widehat { S } _ { j } ( \psi , x ) .
$$

For any $\gamma \geq 0$ , we can obtain the following bound:

$$
\begin{array} { r l } & { \mathbb { E } _ { u \leq \frac { 1 } { 2 } } \left[ \displaystyle \sum _ { f \in R _ { 1 } ^ { \epsilon } \geq \mathcal { E } ^ { r } } \displaystyle \prod _ { 2 ^ { f } \geq r _ { 1 } } f ( y ) u ^ { \star } ( y | \mathcal { X } ) \operatorname { d } y - \displaystyle \int _ { \mathbb { R } ^ { n \epsilon } \geq \mathcal { F } } f ( y ) \hat { w } ( y | \mathcal { X } ) \operatorname { d } y \right] } \\ & { - \mathbb { E } _ { u \leq \frac { 1 } { 2 } } \left[ \displaystyle \sum _ { f \in R _ { 1 } ^ { \epsilon } \geq \mathcal { E } ^ { r } } \displaystyle \sum _ { j = 0 } ^ { \infty } \sum _ { i = 0 } ^ { r } \displaystyle \sum _ { s \in \mathcal { S } _ { 0 } ^ { r _ { 1 } } } f _ { s \in \mathcal { S } _ { 1 } } ( \displaystyle \hat { s } _ { \Psi } ( \mathcal { X } ) - \hat { S } ( \hat { s } , X ) ) \right] } \\ & { \leq \mathbb { E } _ { u \leq \frac { 1 } { 2 } } \left[ \displaystyle \sum _ { f \in R _ { 1 } ^ { \epsilon } \geq \mathcal { E } ^ { r } } \displaystyle \sum _ { j = 0 } ^ { s } \sum _ { i \in \mathcal { S } _ { 0 } ^ { r _ { 1 } } } f _ { s \in \mathcal { S } _ { 1 } ^ { s } } ( x _ { 0 } ^ { \star } ( X ) - \hat { S } ( \hat { s } _ { 0 } ^ { \star } , X ) ) \right] + \mathbb { E } _ { u \leq \frac { 1 } { 2 } } \left[ \displaystyle \sum _ { f \in R _ { 1 } ^ { \epsilon } \geq \mathcal { E } ^ { r } } \displaystyle \sum _ { j = r _ { 1 } } ^ { \infty } \sum _ { s \in \mathcal { S } _ { 0 } ^ { r _ { 1 } } } f _ { s \in \mathcal { S } _ { 1 } ^ { s } } \right. } \\ &  \overset { ( a ) } { \leq } C \displaystyle \sum _ { j = 0 } ^ { \frac { 1 } { 2 } } \sum _ { s \in \mathcal { S } _ { 0 } ^ { r _ { 1 } } } 2 ^  - 2 s \ \end{array}
$$

where $\psi \in \Psi _ { j } ^ { D _ { Y } }$ $( i )$ , uses $| u _ { \psi } ^ { * } ( x ) | \lesssim 2 ^ { - \frac { D _ { Y } j } { 2 } - j \alpha _ { Y } }$ $| f _ { \psi } | \lesssim 2 ^ { - j \gamma - j D _ { Y } / 2 }$ j L, alongside the Jensen’s inequality; the last inequality is derived using for $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , and $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } ) \in \mathcal { H } _ { L } ^ { \alpha _ { Y } } ( \mathbb { R } ^ { D _ { Y } } )$ , implying that for Cauchy-Schwarz inequality and $| \Psi _ { j } ^ { D _ { Y } } | \lesssim 2 ^ { D _ { Y } j }$ . Finally, using Lemma 9, we can get it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that for any $\gamma \geq 0$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) u ^ { * } ( y \vert X ) \mathrm { d } y - \displaystyle \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \widehat { u } ( y \vert X ) \mathrm { d } y \right] } \\ & { \leq C \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - j \gamma } 2 ^ { \frac { j \alpha _ { X } D _ { Y } } { 2 \alpha _ { X } + d _ { X } } } ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + C 2 ^ { - J ( \gamma + \alpha _ { Y } ) } } \\ & { \leq C _ { 1 } \left( \log n \right) \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + C _ { 1 } \left( \frac { n } { \log n } \right) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } . } \end{array}
$$

This completes the proof.

# C.2 Proof of Theorem 1 (minimax lower bound for Regime 1)

The upper bound can be directly derived from Theorem 5, so here we focus solely on establishing the lower bound. Notice that the lower bound for $d _ { X } = 0$ follows directly follows from the minimax rate for the unconditional case (see for example, Theorem 4 of Liang [2021]). Therefore, we will assume $d _ { X } \in \mathbb { N } _ { + }$ in the following.

# αY +γ C.2.1 Proof for the lower bound of $\begin{array} { l l } { { n } } & { { { 2 \alpha } { Y } { + } D { Y } { + } { \frac { { \alpha } { Y } } { { \alpha } { X } } } { d } { X } } } \end{array}$

Define the covariate space $\mathcal { M } _ { X } = [ 0 , 1 ] ^ { d _ { X } } \times \mathbf { 0 } _ { D _ { X } - d _ { X } }$ and let $\mu _ { X } ^ { * }$ be the uniform distribution over $\mathcal { M } _ { X }$ . Then let ${ \widetilde { m } } _ { 1 } = { \lceil } b n ^ { \frac { \star } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } { \rceil }$ and $\widetilde { m } _ { 2 } = \lceil b n ^ { \frac { 1 } { 2 \alpha _ { X } + d _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } D _ { Y } } } \rceil$ where $b$ is a large enough positive e econstant. Consider the following bump function

$$
\widetilde { k } ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \alpha _ { Y } \vee \alpha _ { X } \vee \gamma + 1 } t ^ { \alpha _ { Y } \vee \alpha _ { X } \vee \gamma + 1 } ( t - \frac { 1 } { 2 } ) , \quad t \in ( 0 , 1 ) } \\ { 0 , \quad \mathbf { o . w . } } \end{array} \right.
$$

so that $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \widetilde { k } ( t ) \mathrm { d } t = 0 } \end{array}$ , and the corresponding localized bump function over $\mathbb { R } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } }$

$$
\widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) = \prod _ { i = 1 } ^ { D \gamma } \widetilde { k } \Big ( \widetilde { m } _ { 1 } \sqrt { \frac { D \gamma } { 2 } } y _ { i } + \frac { \widetilde { m } _ { 1 } } { 2 } - \xi _ { 1 i } \Big ) \prod _ { i = 1 } ^ { d _ { X } } \widetilde { k } \Big ( \widetilde { m } _ { 2 } \sqrt { 2 d _ { X } } x _ { i } - \xi _ { 2 i } \Big ) , \quad \forall y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , 1 ) ,
$$

indexed by the $D _ { Y }$ -dimensional grid point $\xi _ { 1 } = ( \xi _ { 1 1 } , \ldots , \xi _ { 1 D _ { Y } } ) \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } }$ and the $d _ { X }$ -dimensional grid $\xi _ { 2 } = ( \xi _ { 2 1 } , \dots , \xi _ { 2 d _ { X } } ) \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } }$ , where we have used the notation $[ m ] ^ { d } = \{ ( i _ { 1 } , i _ { 2 } , \cdots , i _ { d } ) : i _ { k } \in$ $\{ 1 , 2 , \cdots , m \}$ , $\forall k \in \{ 1 , 2 , \cdot \cdot \cdot , d \} \}$ . Define the baseline density function

$$
\begin{array} { r } { \nu _ { 0 } ( y ) = \left\{ \begin{array} { c c } { \frac { \prod _ { i = 1 } ^ { D _ { Y } } ( 1 - y _ { i } ) ^ { \alpha _ { Y } \vee \gamma + 1 } ( y _ { i } + 1 ) ^ { \alpha _ { Y } \vee \gamma + 1 } } { ( \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { \alpha _ { Y } \vee \gamma + 1 } ( t + 1 ) ^ { \alpha _ { Y } \vee \gamma + 1 } \mathrm { d } t ) ^ { D _ { Y } } } } & { y \in [ - 1 , 1 ] ^ { D _ { Y } } } \\ { 0 } & { o . w . } \end{array} \right. } \end{array}
$$

and two function sets

$$
\begin{array} { l } { { \Psi _ { \alpha _ { Y } , \alpha _ { X } } = \Big \{ \nu _ { \omega } ( y , x ) = \nu _ { 0 } ( y ) + \Big ( \frac { 1 } { \widetilde { m } _ { 1 } } \Big ) ^ { \alpha _ { Y } } \displaystyle \sum _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } \displaystyle \sum _ { \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) } } \\ { { \mathrm { : ~ } \omega = \{ \omega _ { \xi _ { 1 } , \xi _ { 2 } } \} _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } , \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \in \{ 0 , 1 \} ^ { \widetilde { m } _ { 1 } ^ { D _ { Y } } \times \widetilde { m } _ { 2 } ^ { d _ { X } } } \Big \} , } } \\ { { \Lambda _ { \gamma } = \Big \{ f _ { v } ( y , x ) = \Big ( \frac { 1 } { \widetilde { m } _ { 1 } } \Big ) ^ { \gamma } \displaystyle \sum _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } \displaystyle \sum _ { \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \nu _ { \xi _ { 1 } , \xi _ { 2 } } \widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) } } \\   \mathrm { : ~ } v = \{ v _ { \xi _ { 1 } , \xi _ { 2 } } \} _  \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } , \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } \in \{ - 1 , 1 \} ^  \widetilde { m } _ { 1 } ^ { D _ { Y } } \times \widetilde { m } _ { 2 } ^  d _  X  \end{array}
$$

Here, $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ consists of all perturbed conditional densities around $\nu _ { 0 } ( \cdot )$ and $\Lambda _ { \gamma }$ serves as set of discriminators for discriminating the conditional densities in $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ . Moreover, $\widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } }$ ’s with distinct indices $( \xi _ { 1 } , \xi _ { 2 } )$ ’s have disjoint supports and when $b$ is sufficiently large, we have for each $\nu \in \Psi _ { \alpha _ { Y } , \alpha _ { X } }$ : $\nu ( y , x ) = \nu _ { 0 } ( y , x )$ for all $( y , x ) \notin \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , 3 / 4 ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( \mathbf { 0 } , 3 / 4 )$ ; and $\begin{array} { r } { \nu ( y , x ) \geq \operatorname* { i n f } _ { y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , 3 / 4 ) } \nu _ { 0 } ( y ) - } \end{array}$ $b ^ { - \alpha _ { Y } } \operatorname* { s u p } _ { t \in ( 0 , 1 ) } | \widetilde { k } ( t ) | ^ { D _ { Y } + d _ { X } } > 0$ for all $y \in \mathbb { R } ^ { D _ { Y } } ( \mathbf { 0 } , 3 / 4 )$ and $x \in \mathcal { M } _ { X }$ , which makes $\nu$ non-negative. In addition, since $\begin{array} { r } { \int _ { - \infty } ^ { \infty } \widetilde { k } ( t ) \mathrm { d } t = 0 } \end{array}$ , we have $\begin{array} { r } { \int _ { \mathbb { R } ^ { D _ { Y } } } \nu ( y , x ) \mathrm { d } y = \int _ { \mathbb { R } ^ { D _ { Y } } } \nu _ { 0 } ( y ) \mathrm { d } y = 1 } \end{array}$ . Therefore, all functions in $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ are valid conditional probability density functions. Furthermore, we state the following lemma that verifies the smoothness of functions in $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ and $\Lambda _ { \gamma }$ , the proof of which is given in Appendix E.9.

Lemma 10. Let $\phi _ { 1 } \in \mathcal { H } _ { L } ^ { [ \alpha _ { 1 } ] } ( \mathbb { R } ^ { d _ { 1 } } )$ , $\phi _ { 2 } \in \mathcal { H } _ { L } ^ { [ \alpha _ { 2 } ] } ( \mathbb { R } ^ { d _ { 2 } } )$ be two compactly supported functions. Consider the function

$$
f ( x , y ) = ( \frac { 1 } { m _ { 1 } } ) ^ { \alpha _ { 1 } } \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ( m _ { 1 } x - \xi _ { 1 } ) \phi _ { 2 } ( m _ { 2 } y - \xi _ { 2 } ) .
$$

For any positive constants $C , C _ { 1 } , C _ { 2 }$ , there exists a constant $L _ { 1 }$ so that for any $m _ { 1 } , m _ { 2 } \in \mathbb { N } _ { + }$ with $C _ { 1 } m _ { 2 } ^ { \alpha _ { 2 } } \leq m _ { 1 } ^ { \alpha _ { 1 } } \leq C _ { 2 } m _ { 2 } ^ { \alpha _ { 2 } }$ , and any $\omega _ { \xi _ { 1 } , \xi _ { 2 } } \in [ - C , C ]$ , it holds that $f \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ .

Therefore, there exist constants $( L _ { 1 } , L _ { 2 } )$ such that $\Psi _ { \alpha _ { Y } , \alpha _ { X } } \subset \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } \bigl ( \mathbb { R } ^ { D _ { Y } } , \mathcal { M } _ { X } \bigr ) \subset \overline { { \mathcal { H } } } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } \bigl ( \mathbb { R } ^ { D _ { Y } } , \mathcal { M } _ { X } \bigr )$ and for any $f \in \Lambda _ { \gamma }$ and $x \in \mathcal { M } _ { X }$ , it holds that $f ( \cdot , x ) \in \mathcal { H } _ { L _ { 2 } } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ . Then for each $\omega \in \{ 0 , 1 \} ^ { \widetilde { m } _ { 1 } ^ { D _ { Y } } \times \widetilde { m } _ { 2 } ^ { d _ { X } } }$ , we define the conditional distribution $\mu _ { Y \mid X } ^ { \omega }$ of $Y | X$ as $\mu _ { Y | X } ^ { \omega } = \nu _ { \omega } ( y , X ) \mathrm { d } y$ and the joint distribution of $( X , Y )$ as $\mu ^ { \omega } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { \omega }$ . Then there exists a constant $L$ so that $\mu ^ { \omega } \in \mathcal { P } _ { 1 } ^ { * } ( D _ { Y } , D _ { X } , d _ { X } , \alpha _ { Y } , \alpha _ { X } , L )$ . Next, by the Varshamov-Gilbert lemma [Tsybakov, 2009], there exists a set $\{ \omega ^ { ( 0 ) } , \cdot \cdot \cdot , \omega ^ { ( H ) } \} \subset \{ 0 , 1 \} ^ { \widetilde m _ { 1 } ^ { D _ { Y } } \times \widetilde m _ { 2 } ^ { d _ { X } } }$ such that $\begin{array} { r } { \log H \geq \frac { \widetilde { m } _ { 1 } ^ { D _ { Y } } \widetilde { m } _ { 2 } ^ { d _ { X } } } { 8 } \log 2 } \end{array}$ and the Hamming distance $\begin{array} { r } { \Vert \omega ^ { ( j ) } - \omega ^ { ( k ) } \Vert _ { \mathrm { H } } \ge \frac { \widetilde { m } _ { 1 } ^ { D _ { Y } } \widetilde { m } _ { 2 } ^ { d _ { X } } } { 8 } } \end{array}$ for any dis-

tinct pair $j , k \in [ H ]$ . Therefore, for any distinct $j , k \in [ H ]$ , we have by our construction of $\mu ^ { \omega }$ ’s that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { x } ^ { n } } \mathbb { E } \Bigg [ d _ { \gamma } ( \mu _ { y } ^ { \alpha ( t ) } ) ^ { \alpha } \mu _ { x } ^ { \alpha ( t ) } ] = \mathbb { E } _ { \mu _ { x } ^ { n } } \Bigg [ \underset { f ( \mathbf { x } _ { t } ^ { n } ) \in \mathcal { R } ^ { n } ( \mathbb { R } ^ { n } ) } { \operatorname* { s u p } } \int _ { \mathbb { R } ^ { n } \mathcal { N } } \int _ { \mathbb { R } ^ { n } \mathcal { N } } \big ( \nu _ { z , 0 } ( \mathbf { x } , X ) - \nu _ { z , \alpha ( t ) } ( \mathbf { x } , X ) \big ) \mathrm { d } y \Bigg ] } \\ & { \geq \frac { 1 } { L } \mathbb { E } _ { \mu _ { x } ^ { n } } \Bigg [ \underset { f ( \mathbf { x } _ { t } ^ { n } ) \sim \mathcal { R } } { \operatorname* { s u p } } \int _ { \mathbb { R } ^ { n } \mathcal { N } } \int ( y , X ) \cdot ( \nu _ { z } \phi ( y , X ) - \nu _ { z , \alpha ( t ) } ( \mathbf { x } , X ) ) \mathrm { d } y \Bigg ] } \\ & { \geq \frac { 1 } { L } \underset { f ( \mathbf { x } _ { t } ^ { n } ) \in \mathcal { R } } { \operatorname* { s u p } } \mathbb { E } \Bigg [ \int _ { \mathbb { R } ^ { n } \mathcal { L } } \int _ { \mathbb { R } ^ { n } \mathcal { L } } \int ( y , X ) \cdot ( \nu _ { z , \alpha ( t ) } ( y , X ) - \nu _ { z , \alpha ( t ) } ( y , X ) ) \mathrm { d } y \Bigg ] } \\ &  = \overline { { 1 } } _ { \widehat { L } _ { f } } \underset { \forall x \in \{ - 1 , 1 \} } { \operatorname* { s u p } } \frac { ( \frac { 1 } { \omega } ) ^ { \alpha } \succ \gamma _ { x } ( \frac { 1 } { \omega } ) ^ { \alpha } } { \operatorname* { s u p } } \int _ { \{ 0 , 1 \} ^ { 1 / \lambda } } \underset  f ( \mathbf { x } _ { t } ^ { n } ) \end{array}
$$

Moreover, we have

$$
\begin{array} { r l } & { \mathcal { D } _ { \mathrm { K L } } ( \mu ^ { \omega ^ { ( i ) } } , \mu ^ { \omega ^ { ( k ) } } ) } \\ & { = \mathbb { E } _ { \mu _ { X } ^ { * } } \bigg [ \int _ { \mathbb { R } ^ { D _ { Y } } } - \log \bigg ( \frac { \nu _ { 0 } ( y ) + \left( \frac { 1 } { \widetilde { m _ { 1 } } } \right) ^ { \alpha _ { Y } } } { \nu _ { 0 } ( y ) + \left( \frac { 1 } { \widetilde { m _ { 1 } } } \right) ^ { \alpha _ { Y } } } \sum _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } \sum _ { \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } ^ { ( k ) } \widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) } \\ & { \qquad \quad \times _ { 0 } ^ { ( \ell ) } \bigg ( \frac { 1 } { \nu _ { 0 } ( y ) + \left( \frac { 1 } { \widetilde { m _ { 1 } } } \right) ^ { \alpha _ { Y } } } \sum _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } \sum _ { \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } ^ { ( j ) } \widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) \bigg ) \nu _ { \omega ^ { ( j ) } } ( y , x ) } \end{array}
$$

For sufficiently large $b$ , we have $| u ( y , x ) | \leq 1 / 4$ so that $- \log ( 1 + u ( y , x ) ) \leq u ^ { 2 } ( y , x ) - u ( y , x )$ . This leads to

$$
\begin{array} { r l } & { \mathrm { \partial ~ } _ { \operatorname { N L } } ( \mu _ { \omega ^ { ( j ) } } , \mu _ { \omega ^ { ( k ) } } ) \leq C \Big ( \frac { 1 } { \widetilde { m } _ { 1 } } \Big ) ^ { 2 \alpha \gamma } } \\ & { + \left( \frac { 1 } { \widetilde { m } _ { 1 } } \right) ^ { \alpha \gamma } \displaystyle \int _ { [ 0 , 1 ] ^ { d } X } \int _ { \mathbb { R } ^ { D _ { Y } } } \Bigg \{ \underset { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } { \sum } \sum _ { \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d } X } ( \omega _ { \xi } ^ { ( j ) } - \omega _ { \xi } ^ { ( k ) } ) \cdot \psi _ { \xi _ { 1 } , \xi _ { 2 } } ( y , ( x , \mathbf { 0 } _ { D _ { X } - d _ { X } } ) ) \Bigg \} \mathrm { d } y \mathrm { d } x = } \end{array}
$$

where we used the fact that $\begin{array} { r } { \int _ { \mathbb { R } ^ { D _ { Y } } } \psi _ { \xi _ { 1 } , \xi _ { 2 } } \big ( y , ( x , \mathbf { 0 } _ { D _ { X } - d _ { X } } ) \big ) \mathrm { d } y = 0 } \end{array}$ . Then we can apply Fano’s lemma (proposition 15.12 of Wainwright [2019]) to obtain

$$
\begin{array} { r l } & { \underset { \hat { \mu } _ { Y } \mid x _ { \mu } \in \mathcal { P } _ { \vec { \mathtt { X } } } ^ { \mathtt { s } } } { \mathrm { i n f ~ s u p ~ } } \mathbb { E } _ { \mu \lesssim n } \mathbb { E } _ { \mu _ { X } } \big [ d _ { \gamma } ( \widehat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ) \big ] \geq \underset { \hat { \mu } _ { Y } \mid x _ { j } \in [ H ] } { \mathrm { i n f ~ s u p ~ } } \mathbb { E } _ { \mu ^ { \omega , j } \otimes n } \mathbb { E } _ { \mu _ { X } ^ { * } } \big [ d _ { \gamma } ( \widehat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ^ { \omega ( j ) } ) \big ] } \\ & { \geq \frac { 1 } { 2 } \underset { \hat { \mu } _ { Y \mid X } \in \{ \mu _ { Y \mid X } ^ { \omega ( j ) } : \xi \in [ H ] \} } { \mathrm { i n f ~ } } \underset { \mu \in [ H ] } { \mathrm { s u p ~ } } \mathbb { E } _ { \mu ^ { \omega , j } \otimes n } \mathbb { E } _ { \mu _ { X } ^ { * } } \big [ d _ { \gamma } ( \widehat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ^ { \omega ( j ) } ) \big ] } \\ & { \geq \frac { 1 } { 2 } \underset { \underbrace { \mathrm { i n f ~ } } _ { \hat { \mu } _ { X } ^ { \mathtt { s } } \in [ H ] } } { \mathrm { i n f ~ } } \mathbb { E } _ { \mu _ { X } ^ { * } } \big [ d _ { \gamma } ( \mu _ { Y \mid X } ^ { \omega ( j ) } , \mu _ { Y \mid X } ^ { \omega ( k ) } ) \big ] \cdot \bigg ( 1 - \frac { \log 2 + \frac { n } { H ^ { 2 } } \sum _ { j , k = 1 } ^ { H } D _ { \mathrm { K L } } ( \mu ^ { \omega ( j ) } , \mu ^ { \omega ( k ) } ) } { \log H } \bigg ) } \\ &  \gtrsim n ^  - \frac { \alpha _ { Y } + \gamma }  2 \omega _ { Y } + D  \end{array}
$$

# C.2.2 Proof for the lower bound of $n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } }$

Consider the same covariate space $\mathcal { M } _ { X } = [ 0 , 1 ] ^ { d _ { X } } \times \mathbf { 0 } _ { D _ { X } - d _ { X } }$ and uniform distribution $\mu _ { X } ^ { * }$ over $\mathcal { M } _ { X }$ . Define $\widetilde { m } = \lceil b n ^ { \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } \rceil$ , where $b$ is a large enough positive constant. Consider $\widetilde { k } ( \cdot )$ as defined in (25) eand the localized bump function over $\mathbb { R } ^ { D _ { X } }$ ,

$$
\widetilde { \psi } _ { \xi } ( x ) = \prod _ { i = 1 } ^ { d _ { X } } \widetilde { k } \Big ( \widetilde { m } \sqrt { 2 d _ { X } } x _ { i } - \xi _ { i } \Big )
$$

indexed by the $d _ { X }$ -dimensional grid $\xi = ( \xi _ { 1 } , \dots , \xi _ { d _ { X } } ) \in [ \widetilde { m } ] ^ { d _ { X } }$ . Then define two function sets

$$
\begin{array} { l } { { \Psi _ { \alpha _ { X } } = \Bigl \{ \nu _ { \omega } ( y , x ) = \nu _ { 0 } ( y ) + \Bigl ( \frac { 1 } { \widetilde { m } } \Bigr ) ^ { \alpha _ { X } } \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \omega _ { \xi } \widetilde { \psi } _ { \xi } ( x ) \prod _ { i = 1 } ^ { D _ { Y } } \widetilde { k } ( y _ { i } ) : \omega = \{ \omega _ { \xi } \} _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \in \{ 0 , 1 \} ^ { \widetilde { m } ^ { d _ { X } } } } } \\ { { \Lambda _ { \gamma } = \Bigl \{ f _ { v } ( y , x ) = \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } v _ { \xi } \widetilde { \psi } _ { \xi } ( x ) \prod _ { i = 1 } ^ { D _ { Y } } \widetilde { k } ( y _ { i } ) : v = \{ v _ { \xi } \} _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \in \{ - 1 , 1 \} ^ { \widetilde { m } ^ { d _ { X } } } \Bigr \} , } } \end{array}
$$

that where $\Psi _ { \alpha _ { X } } \subset \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathcal { M } _ { X } )$ $\nu _ { 0 }$ is defined in (27). Then it is straightforward to verify that there exist constants and for any $f \in \Lambda _ { \gamma }$ and $x \in \mathcal { M } _ { X } , f ( \cdot , x ) \in \mathcal { H } _ { L _ { 2 } } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } )$ $( L _ { 1 } , L _ { 2 } )$ . Moreover, such $\nu _ { \omega }$ ’s in $\Psi _ { \alpha _ { X } }$ are valid probability density functions. Then for each $\omega \in \{ 0 , 1 \} ^ { \widetilde { m } ^ { d } X }$ , we define the conditional distribution $\mu _ { Y \mid X } ^ { \omega }$ of $Y | X$ as $\mu _ { Y | X } ^ { \omega } = \nu _ { \omega } ( y , X ) \mathrm { d } y$ and the joint distribution of $( X , Y )$ as $\mu ^ { \omega } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { \omega }$ . Then there exists a constant $L$ so that $\mu ^ { \omega } \in \mathcal { P } _ { 1 } ^ { * } ( D _ { Y } , D _ { X } , d _ { X } , \alpha _ { Y } , \alpha _ { X } , L )$ . Next, by the Varshamov-Gilbert lemma [Tsybakov, 2009], there exists a set $\{ \omega ^ { ( 0 ) } , \cdot \cdot \cdot , \omega ^ { ( H ^ { \prime } ) } \} \subset \{ 0 , 1 \} ^ { \tilde { m } ^ { d _ { X } } }$ such that $\begin{array} { r } { \log H ^ { \prime } \geq \frac { \widetilde { m } ^ { d _ { X } } } { 8 } \log 2 } \end{array}$ and the Hamming distance $\begin{array} { r } { \| \omega ^ { ( j ) } - \omega ^ { ( k ) } ) \| _ { \mathrm { H } } \ge \frac { \widetilde { m } ^ { d _ { X } } } { 8 } } \end{array}$ for any distinct pair $j , k \in [ H ^ { \prime } ]$ . Therefore, for any distinct $j , k \in [ H ^ { \prime } ]$ , we have by our construction of $\mu ^ { \omega }$ ’s that

$$
\begin{array} { r l } & { \mathbb { E } _ { \rho _ { X } ^ { n } } [ \alpha _ { i } ( \rho _ { Y } ^ { \theta ( \theta ) } ( \rho _ { Y } ^ { \theta ( \theta ) } , \mu _ { Y } ^ { \theta ( \theta ) } ) ] = \mathbb { E } _ { \rho _ { X } ^ { n } } ^ { \theta } \bigg [ \underset { f \in \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } \bigg [ \underset { \mathbb { R } ^ { n } \in \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } \bigg ] \underset { \mathbb { R } ^ { n } \in \mathcal { R } _ { 1 } ^ { n } } f ( y ) \cdot \big ( \nu _ { \alpha ( \theta ) } ( y , X ) - \nu _ { \alpha ( \theta ) } ( y , X ) \big ) \mathrm { d } y \bigg ] } \\ & { \geq \frac { 1 } { L _ { 2 } } \mathbb { E } _ { \rho _ { X } ^ { n } } \bigg [ \underset { f \in \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } \bigg [ \underset { \mathbb { R } ^ { n } \cap \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } f ( y , X ) \cdot \big ( \nu _ { \alpha ( \theta ) } ( y , X ) - \nu _ { \alpha ( \theta ) } ( y , X ) \big ) \mathrm { d } y \bigg ] } \\ & { = \frac { 1 } { L _ { 2 } } \underset { f \in \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } \mathbb { E } _ { \rho _ { X } ^ { n } } \bigg [ \int _ { \mathbb { R } ^ { n } \mathcal { P } _ { 1 } ^ { n } } f ( y , X ) \cdot \big ( \nu _ { \alpha ( \theta ) } ( y , X ) - \nu _ { \alpha ( \theta ^ { \theta } ) } ( y , X ) \big ) \mathrm { d } y \bigg ] } \\ &  = \frac { 1 } { L _ { 2 } } \underset { \mathbb { R } ^ { n } \in \mathcal { R } _ { 1 } ^ { n } } { \operatorname* { s u p } } \underset { \mathbb { R } ^ { n } \in \mathcal { R } _ { n } ^ { n } }  \operatorname* { s u p }  \end{array}
$$

Moreover, similar to (29), we can derive

$$
\begin{array} { r l } & { \mathrm { \partial _ { K L } } ( \mu ^ { \omega ^ { ( j ) } } , \mu ^ { \omega ^ { ( k ) } } ) } \\ & { = \mathbb { E } _ { \mu _ { X } ^ { * } } \int _ { \left[ 0 , 1 \right] ^ { D _ { Y } } } - \log \bigg ( \frac { \nu _ { 0 } ( y ) + \left( \frac { 1 } { \overline { { m } } } \right) ^ { \alpha _ { X } } \sum _ { \xi \in [ \overline { { m } } ] ^ { d _ { X } } } \omega _ { \xi } ^ { ( j ) } \widetilde { \psi } _ { \xi } ( x ) \prod _ { i = 1 } ^ { D _ { Y } } \widetilde { k } ( y _ { i } ) } { \nu _ { 0 } ( y ) + \left( \frac { 1 } { \overline { { m } } } \right) ^ { \alpha _ { X } } \sum _ { \xi \in [ \overline { { m } } ] ^ { d _ { X } } } \omega _ { \xi } ^ { ( k ) } \widetilde { \psi } _ { \xi } ( x ) \prod _ { i = 1 } ^ { D _ { Y } } \widetilde { k } ( y _ { i } ) } \bigg ) \nu _ { \omega ^ { ( j ) } } ( y , x ) \mathrm { d } y \lesssim ( \frac { 1 } { \widetilde { m } } ) } \end{array}
$$

where we used the fact that $\begin{array} { r } { \int _ { \mathbb { R } ^ { D _ { Y } } } \prod _ { i = 1 } ^ { D _ { Y } } \widetilde { k } ( y _ { i } ) \mathrm { d } y = 0 } \end{array}$ . Then we can apply Fano’s lemma to obtain

$$
\begin{array} { r l } & { \underset { \hat { \mu } _ { Y } \mid X \mu \in \mathcal { P } _ { \mathrm { k } } ^ { \kappa } } { \mathrm { i n f ~ s u p ~ } } \mathbb { E } _ { \mu \otimes n } \mathbb { E } _ { \mu _ { X } } \left[ d _ { \gamma } ( \hat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ) \right] \geq \underset { \hat { \mu } _ { Y \mid X } j \in [ H ] } { \mathrm { i n f ~ s u p ~ } } \mathbb { E } _ { \mu ^ { \infty / \otimes n } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ d _ { \gamma } ( \hat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ^ { \infty ( \theta ) } ) \right] } \\ & { \geq \frac { 1 } { 2 } \underset { \hat { \mu } _ { Y \mid X } \in \{ \mu _ { Y \mid X } ^ { \infty ( j ) } : j \in [ H ] \} } { \mathrm { i n f ~ } } \underset { j \in [ H ] } { \mathrm { s u p ~ } } \mathbb { E } _ { \mu ^ { \infty / \otimes n } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ d _ { \gamma } ( \hat { \mu } _ { Y \mid X } , \mu _ { Y \mid X } ^ { \infty ( j ) } ) \right] } \\ & { \geq \frac { 1 } { 2 } \underset { \hat { \mu } _ { X } ^ { \varepsilon } \in [ H ^ { \varepsilon } ] } { \mathrm { i n f ~ } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ d _ { \gamma } ( \mu _ { Y \mid X } ^ { \infty ( h ) } , \mu _ { Y \mid X } ^ { \infty ( \varepsilon ) } ) \right] \cdot \left( 1 - \frac { \log 2 + \frac { n } { H ^ { \prime 2 } } \sum _ { h , \ell = 1 } ^ { H ^ { \prime } } D _ { \mathrm { K L } } ( \mu ^ { \infty ( h ) } , \mu ^ { \infty ( \ell ) } ) } { \log H ^ { \prime } } \right) } \\ & { \gtrsim n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } } } . } \end{array}
$$

# C.3 Proof of Lemma 9

We first derive an oracle inequality in the following lemma,

Lemma 11. Suppose $\mu ^ { * } \in \mathcal { P } _ { 1 } ^ { * }$ and with the choices of $S _ { j }$ defined in (23), it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n } }$ that for any $j \in [ J ]$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { \star } } \bigg [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( \widehat S _ { j } ( \psi , x ) - u _ { \psi } ^ { * } ( x ) ) ^ { 2 } \bigg ] \lesssim \frac { 2 ^ { D _ { Y } j } W _ { j } \log n } { n } + \operatorname* { m i n } _ { S \in { \mathcal S } _ { j } } \mathbb { E } _ { \mu _ { X } ^ { \star } } \bigg [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( S ( \psi , x ) - u _ { \psi } ^ { * } ( x ) ) ^ { 2 } \bigg ]
$$

The proof of Lemma 11 is provided in Appendix C.4. Then we provide an upper bound for the approximation error given by $\begin{array} { r l } & { \underset { S \in S _ { j } } { \operatorname* { m i n } } \mathbb { E } _ { \mu _ { X } ^ { * } } \big [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( S ( \psi , x ) - u _ { \psi } ^ { * } ( x ) ) ^ { 2 } \big ] } \end{array}$ . Fix an arbitrary $j \in [ J ]$ and considering $u ^ { * } \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathcal { M } _ { X } )$ , there exists $\overline { { u } } ^ { * } \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ so that $\overline { { u } } ^ { * } | _ { \mathbb { R } ^ { D _ { Y } } \times \mathcal { M } _ { X } } = u ^ { * }$ Consequently, there exists a constant $L _ { 1 }$ so that for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ ,

$$
2 ^ { \frac { D _ { Y } j } { 2 } } u _ { \psi } ^ { * } ( x ) = 2 ^ { \frac { D _ { Y } j } { 2 } } \int _ { \mathbb { R } ^ { D _ { Y } } } \psi ( y ) \overline { { u } } _ { \psi } ^ { * } ( y | x ) \mathrm { d } y \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { X } } ( \mathbb { R } ^ { D _ { X } } ) ,
$$

where we have used the fact that the support of $\psi ( y )$ has a volume of $\mathcal { O } ( 2 ^ { - j D _ { Y } } )$ and $| \psi ( y ) | = \mathcal { O } ( 2 ^ { \frac { D _ { Y } j } { 2 } } )$ . $\mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ e largest . Then w $\varepsilon _ { j } ^ { x }$ -packing sdefine a set $\mathcal { M } _ { X }$ r large, where $C _ { 1 }$ $| \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | \le$ $W _ { j } = \ ' C _ { 1 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ e . For any $\overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } ^ { x } = \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } \cup \mathcal { X }$ $\mathcal { X }$ is an arbitrary subset of $\mathcal { M } _ { X } \backslash \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ $| \mathcal { X } | = W _ { j } - | \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } |$ $\psi \in \Psi _ { j } ^ { D _ { Y } }$

$$
\widetilde { u } _ { \psi } ( x ) = \frac { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } } } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } \rho ( \frac { | | x - \widetilde { x } | | } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } } } } \rho ( \frac { | | x - \widetilde { x } | | } { \varepsilon _ { j } ^ { x } } ) }
$$

and for any $x \in \mathcal { M } _ { X }$ ,

$$
S _ { j } ^ { * } ( \psi , x ) = \frac { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } _ { \varepsilon _ { j } ^ { x } } } } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( ^ { k } ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } _ { \varepsilon _ { j } ^ { x } } } } } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } .
$$

It holds that $S _ { j } ^ { * } ( \psi , x ) \in { \cal S } _ { j }$ and for any $x \in \mathcal { M } _ { X } , \psi \in \Psi _ { j } ^ { D _ { Y } }$ ,

$$
\begin{array} { r l } &  \displaystyle \widetilde { u } _ { \psi } ( x ) - S _ { j } ^ { * } ( \psi , x ) | - \frac { | \sum _ { \widetilde { x } \in \widetilde { \mathbb { N } } _ { \epsilon _ { j } ^ { x } } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } \times \lfloor \epsilon _ { k } ^ { x } \rfloor \in \mathcal { R } _ { k } } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } \rho ( \frac { | \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { - } \widetilde { x } | } { \varepsilon _ { j } ^ { x } } ) | } { n \cdot ( \sum _ { \widetilde { x } \in \widetilde { \mathbb { N } } _ { \epsilon _ { j } ^ { x } } ^ { x } } \rho ( \frac { | \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } ) + \frac { 1 } { \delta } ) ( \sum _ { \widetilde { x } \in \widetilde { \mathcal { N } } _ { \epsilon _ { j } ^ { x } } ^ { x } } \rho ( \frac { | \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { - } \widetilde { x } | } { \varepsilon _ { j } ^ { x } } ) | ) } } \\ &  \qquad \le \frac { 1 } { n } \frac { \sum _ { \widetilde { x } \in \widetilde { \mathbb { N } } _ { \epsilon _ { j } ^ { x } } ^ { x } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } \times \lfloor \epsilon _ { k } ^ { x } \rfloor \in \mathcal { R } _ { k } } | u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } | \rho ( \frac { | \mathbb { L } \mathbb { - } \widetilde { x } | } { \varepsilon _ { j } ^ { x } } ) | }  \sum _  \widetilde { x } \in \widetilde { \mathbb { N } } _ { \epsilon _ { j } ^ { x } } ^ { x } \rho ( \frac  | \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb { L } \mathbb  L \end{array}
$$

$$
\begin{array} { r l } & { | \widetilde { u } _ { \psi } ( x ) - u _ { \psi } ^ { * } ( x ) | = \frac { \big | \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } } \big ( \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } - u _ { \psi } ^ { * } ( x ) \big ) \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) \big | } { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) } } \\ & { \qquad \le \underset { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } , x \in \mathbb { B } _ { M _ { X } } ( \widetilde { x } , 2 \varepsilon _ { j } ^ { x } ) } } { \operatorname* { s u p } } \big | _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( k ) ( x - \widetilde { x } ) ^ { k } - u _ { \psi } ^ { * } ( x ) \big | } \\ & { \qquad \lesssim 2 ^ { - \frac { D _ { Y } j } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } . } \end{array}
$$

We can then get

$$
\begin{array} { r l } & { \underset { S \in \mathcal { S } _ { j } } { \operatorname* { m i n } } \mathbb { E } _ { \mu _ { x } ^ { * } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { V } _ { j } ^ { D } } \big ( S ( \psi , x ) - u _ { \psi } ^ { * } ( x ) \big ) ^ { 2 } \bigg ] } \\ & { \leq \mathbb { E } _ { \mu _ { x } ^ { * } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { V } _ { j } ^ { D } } \big ( S _ { j } ^ { * } ( \psi , x ) - u _ { \psi } ^ { * } ( x ) \big ) ^ { 2 } \bigg ] } \\ & { \lesssim \displaystyle \sum _ { \psi \in \mathbb { V } _ { j } ^ { D } } 2 ^ { - D \gamma \mathcal { I } } \big ( ( \varepsilon _ { j } ^ { x } ) ^ { - \alpha _ { X } } + \frac { 1 } { n } \big ) ^ { 2 } } \\ & { \lesssim ( \varepsilon _ { j } ^ { x } ) ^ { 2 \alpha _ { X } } + \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Finally, by substituting $\varepsilon _ { j } ^ { x } = 2 ^ { \frac { j D _ { Y } } { 2 \alpha _ { X } + d _ { X } } } { \big ( } { \frac { n } { \log n } } { \big ) } ^ { - { \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } }$ and $W _ { j } \asymp ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ , the desired result follows directly from lemma 11.

# C.4 Proof of Lemma 11

To show the desired result, we will apply Theorem 8 with $\{ \psi _ { \lambda } ( \cdot ) \} _ { \lambda \in \Lambda } = \Psi _ { j } ^ { D _ { Y } }$ . We will then proceed by verifying the three assumptions in Theorem 8. For the first assumption, note that for any $S ( \psi , x ) =$

$$
\begin{array} { r l } & { \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } X } a _ { i k } ^ { \psi } ( x - b _ { i } ) ^ { k } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } \in \mathcal { S } _ { j } , } \end{array}
$$

$$
\begin{array} { r l } & { \underset { x \in \mathcal { M } _ { X } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D } Y } { \operatorname* { s u p } } \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } X , | k | < \alpha _ { X } } a _ { i k } ^ { \psi } ( x - b _ { i } ) ^ { k } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } } \\ & { \leq \underset { i \in [ W _ { j } ] } { \operatorname* { s u p } } \underset { x \in \mathcal { M } _ { X } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \operatorname* { s u p } } \underset { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } { \sum } a _ { i k } ^ { \psi } ( x - b _ { i } ) ^ { k } } \\ & { \lesssim 2 ^ { - \frac { D _ { Y } j } { 2 } } . } \end{array}
$$

Moreover, for any $y$ , there exists only a constant-order number of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ so that $\boldsymbol { \psi } ( y ) \neq \boldsymbol { 0 }$ . Therefore, it holds that

$$
\begin{array} { r l } & { \quad \underset { ( x , y ) \in \mathcal { M } } { \operatorname* { s u p } } \underset { S \in \mathcal { S } _ { j } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } S ^ { 2 } ( \psi , x ) + \vert \psi ( y ) S ( \psi , x ) \vert } \\ & { \lesssim \underset { ( x , y ) \in \mathcal { M } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } 2 ^ { - D _ { Y } j } + \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } \vert \psi ( y ) \vert \cdot 2 ^ { - \frac { D _ { Y } j } { 2 } } } \\ & { = \mathcal { O } ( 1 ) , } \end{array}
$$

which verifies the first assumption. For the second assumption, let

$$
\ell ( x , y , S ) = \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } S ^ { 2 } ( \psi , x ) - 2 \psi ( y ) S ( \psi , x ) .
$$

It holds that

$$
\begin{array} { r l } & { \quad = \widehat { S } _ { \varepsilon ^ { \prime } \star } \big [ \big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } \big ) - \varepsilon ( X , Y , S ^ { \star } ) \big ) ^ { 2 } \big ] } \\ & { \quad = \widehat { S } _ { \varepsilon ^ { \prime } \star } \bigg [ \Big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } \big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } S ^ { 2 } ( \psi , X ) - S ^ { 2 } ( \psi , X ) \big ) - 2 \widehat { \psi } ( Y ) \big ) \big ( S ( \psi , X ) - S ^ { 2 } ( \psi , X ) \big ) \Big ) ^ { 2 } \bigg ] } \\ & { \quad = \widehat { S } _ { \varepsilon ^ { \prime } \star } \bigg [ \Big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } \big ( S ( \psi , X ) + S ^ { 2 } ( \psi , X ) - 2 \widehat { \psi } ( Y ) \big ) - \big ( S ( \psi , X ) - S ^ { 2 } ( \psi , X ) \big ) \Big ) ^ { 2 } \bigg ] } \\ & { \quad \leq \mathfrak { R } _ { \varepsilon ^ { \prime } \star } \bigg [ \Big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } \big ( \underset { \psi \in \mathbb { F } _ { \varepsilon ^ { \prime } } ^ { \star } } { \sum } S ( \psi ) , X ) - S ^ { 2 } ( \psi , X ) \big ) \Big ) ^ { 2 } \bigg ] } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times ( \psi , X ) - S ^ \end{array}
$$

Then notice that

$$
\begin{array} { r l } & { \mathbb { E } _ { \varphi } \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) \xi \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg \} ^ { \lambda } } \\ & { = \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg \} ^ { \lambda } } \\ & { = \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) - \xi \psi ( x ) , X _ { j } \Vert \xi \psi ( x , \lambda ) - \xi \psi ( x , X _ { j } ) , X _ { j } \Bigg ) \Bigg ] } \\ & { \Bigg ] } \\ & { = \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg \} } \\ & { \quad - \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ] } \\ & { = \mathbb { E } _ { \varphi } \Bigg [ \Bigg ( \sum _ { j \in \mathcal { S } } \psi ( \xi ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) - \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg ( \xi \psi ( x , \lambda ) \Bigg ) ^ { \lambda } \Bigg \} } \\ &  \quad - \mathbb { E } _ { \varphi } \Bigg [  \end{array}
$$

where the last inequality uses the fact that for any $\psi _ { 1 } ~ \in ~ \Psi _ { j } ^ { D _ { Y } }$ , there are only constant number of $\psi _ { 2 } \in \Psi _ { j } ^ { D _ { Y } }$ so that $\operatorname { s u p p } ( \psi _ { 1 } ) \cap \operatorname { s u p p } ( \psi _ { 2 } ) \neq \emptyset$ . Moreover,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Psi _ { \mathcal { I } } ^ { D _ { Y } } } 2 ^ { - \frac { D _ { Y } j } { 2 } } \cdot \big | S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big | \Big ) ^ { 2 } \Big ] } \\ & { \leq \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { \mathcal { I } } ^ { D _ { Y } } } 2 ^ { - D _ { Y } j } \cdot \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) ^ { 2 } \Big ] } \\ & { \lesssim \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { \mathcal { I } } ^ { D _ { Y } } } \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) ^ { 2 } \Big ] . } \end{array}
$$

Therefore, it holds for some constant $C$ that

$$
{  { \mathbb E } } _ { \mu ^ { * } } \Big [ \big ( \ell ( X , Y , S ) - \ell ( X , Y , S ^ { \prime } ) \big ) ^ { 2 } \Big ] \leq C {  { \mathbb E } } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) \big ) ^ { 2 } \Big ] ,
$$

which verifies the second assumption. Now we verify the last assumption. Note that for any $S , S ^ { \prime } \in S _ { j }$ it holds that

$$
\begin{array} { r l } & { \displaystyle \mathcal { L } _ { n } ( S , S ^ { \xi } ) } \\ & { = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Big ( \sum _ { \ell = 1 } ^ { n } \big ( S ^ { 2 } ( \psi , X _ { i } ) - S ^ { 2 } ( \psi , X _ { i } ) \big ) - 2 \psi ( X _ { i } ) \big ) \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) \Big ) ^ { 2 } } } \\ & { = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \Big ( \displaystyle \sum _ { \ell = 1 } ^ { n } \Big ( S \Big ( \psi , X _ { i } ) + S ^ { \prime } ( \psi , X _ { i } ) - 2 \psi ( Y _ { i } ) \Big ) \cdot \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) \Big ) ^ { 2 } } } \\ & { \leq \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { \psi \leq q _ { i } ^ { \prime \prime \prime } } S \Big ( S ( \psi , X _ { i } ) + S ^ { \prime } ( \psi , X _ { i } ) - 2 \psi ( Y _ { i } ) \Big ) \cdot \sum _ { \ell = 1 } ^ { n } \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) ^ { 2 } } } \\ & { \leq \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { \psi \leq q _ { i } ^ { \prime \prime } } \big ( S ( \psi , X _ { i } ) + S ^ { \prime } ( \psi , X _ { i } ) - 2 \psi ( Y _ { i } ) \big ) ^ { 2 } \cdot \sum _ { \ell = 1 } ^ { n } \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) ^ { 2 } } } \\ &  \lesssim \mathrm { c } \xi ^ { 2 \nu } \displaystyle \sum _ { \ell = 1 } ^ { n } \bigg ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n }  \end{array}
$$

where the last inequality uses that for any $( x , y ) \in { \mathcal { M } }$ and $S , S ^ { \prime } \in S _ { j }$ ,

$$
\sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( S ( \psi , x ) + S ^ { \prime } ( \psi , x ) - 2 \psi ( y ) \big ) ^ { 2 } \lesssim | \Psi _ { j } ^ { D _ { Y } } | \cdot 2 ^ { - D _ { Y } j } + \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \psi ( y ) ^ { 2 } \lesssim 2 ^ { D _ { Y } j } .
$$

$$
\begin{array} { r l } & { \mathrm { ~ s u r t h e r m o r e , ~ f o r ~ a n y ~ } \psi \in \Psi _ { j } ^ { D _ { Y } } , x \in \mathcal { M } _ { X } , S ( \psi , x ) = \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } a _ { i k } ^ { \psi } ( x - b _ { i } ) ^ { k } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } > ^ { \prime } ( \psi , x ) = \frac { \sum _ { i = 1 } ^ { W _ { j } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } a _ { i k } ^ { \psi _ { i } ^ { \prime } ( x - b _ { i } ^ { \prime } ) k } \rho ( \frac { \| x - b _ { i } ^ { \prime } \| } { \varepsilon _ { j } ^ { x } } ) } { \sum _ { i = 1 } ^ { W _ { j } } \rho ( \frac { \| x - b _ { i } ^ { \prime } \| } { \varepsilon _ { j } ^ { x } } ) + \frac { 1 } { n } } , \mathrm { ~ i t ~ h o l d s ~ t h a t ~ } } \end{array}
$$

$$
\begin{array} { r l } & { | S ( \psi , x ) - S ^ { \prime } ( \psi , x ) | } \\ & { \leq \Big | \frac { \sum _ { k = 1 } ^ { W _ { j } } \sum _ { k \in \mathcal { N } _ { 1 } } \alpha _ { k } ^ { W } ( x - b _ { k j } ) ( x - b _ { k j } ) ( b _ { k } ( \frac { \psi } { \zeta } ) \frac { | \psi - b _ { k j } | } { \zeta } ) } { \sum _ { k = 1 } ^ { W _ { j } } \rho \left( \frac { | \mathbf { D } \psi | } { \zeta } \right) \Big | + \frac { 1 } { \eta } } - \frac { \sum _ { k = 1 } ^ { W _ { j } } \sum _ { k \in \mathcal { N } _ { 1 } } \alpha _ { k } ^ { W } ( x - b _ { k j } ) ( x - b _ { k j } ) ( \psi \frac { | \mathbf { D } \psi | - b _ { k j } | } { \zeta } ) } { \sum _ { k = 1 } ^ { W _ { j } } \rho \left( \frac { | \mathbf { D } \psi | } { \zeta } \right) } + \frac { 1 } { \eta } } \\ & { + \Big | \frac { \sum _ { k = 1 } ^ { W _ { j } } \sum _ { k \in \mathcal { N } _ { 1 } } \alpha _ { k } ^ { W } ( x - b _ { k i } ^ { W } ) ( x - b _ { k i } ^ { W } ) ( x - b _ { k i } ^ { W } ) } { \sum _ { k = 1 } ^ { W _ { j } } \rho \left( \frac { | \mathbf { D } \psi | } { \zeta } \right) \Big | + \frac { 1 } { \eta } } - \frac { \sum _ { k = 1 } ^ { W _ { j } } \sum _ { k \in \mathcal { N } _ { 1 } } \alpha _ { k } ^ { W } ( x - b _ { k i } ^ { W } ) ( x - b _ { k i } ^ { W } ) \rho ( \frac { | \mathbf { D } \psi | - b _ { k i } ^ { W } } { \zeta } ) } { \sum _ { k = 1 } ^ { W _ { j } } \rho \left( \frac { | \mathbf { D } \psi | } { \zeta } \right) \Big | + \frac { 1 } { \eta } } } \\ &  + \Big | \frac \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } & { \sqrt { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) ^ { 2 } } } \\ & { \lesssim \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \left[ \operatorname* { m a x } _ { i \in [ W _ { j } ] } \big ( \sum _ { k \in \mathbb { R } _ { 0 } ^ { D _ { X , | k | < \alpha _ { X } } } } \vert a _ { i k } ^ { \psi } - a _ { i k } ^ { \psi , \prime } \vert \big ) ^ { 2 } + 2 ^ { - D _ { Y } j } \frac { n ^ { 2 } } { ( \xi _ { j } ^ { x } ) ^ { 2 } } \big ( \sum _ { i = 1 } ^ { W _ { i } } \vert b _ { i } - b _ { i } ^ { \prime } \vert \big ) ^ { 2 } \right] } } \\ & { \lesssim \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \sum _ { i \in [ W _ { j } ] } \sum _ { k \in \mathbb { R } _ { 0 } ^ { D _ { X , | k | < \alpha _ { X } } } } \big ( a _ { i k } ^ { \psi } - a _ { i k } ^ { \psi , \prime } ) ^ { 2 } + \frac { n ^ { 2 } W _ { j } } { ( \xi _ { j } ^ { x } ) ^ { 2 } } \sum _ { i = 1 } ^ { W _ { j } } \Vert b _ { i } - b _ { i } ^ { \prime } \Vert ^ { 2 } } . } \end{array}
$$

Using the fact that the $\varepsilon$ -covering number of a $d$ -dimensional ball with radius $R$ is bounded by $\big ( \frac { 3 R } { \varepsilon } \big ) ^ { d }$ , there exists a constant $C$ so that for any $0 < \varepsilon \leq \operatorname* { s u p } _ { S , S ^ { \prime } \in { \mathcal { S } } _ { j } } d _ { n } ( S , S ^ { \prime } ) .$ ,

$$
\log \mathbf { N } ( S , d _ { n } , \varepsilon ) \leq C W _ { j } 2 ^ { j D _ { Y } } \log { \frac { n } { \varepsilon } } .
$$

which verifies the third assumption. The desired result is obtained by setting $W _ { n } = C W _ { j } 2 ^ { j D _ { Y } }$ and $T _ { n } = n$ in Theorem 8, and applying a union bound over $j \in [ J ]$ .

# D Proof for Distribution Regression with Manifold Responses

In the forthcoming analysis, let $\mathcal { M } _ { X }$ denote the support of $\mu _ { X } ^ { * }$ , and let $\mathcal { M } _ { Y \mid x }$ denote the support of $\mu _ { Y \mid X } ^ { * }$ . We define $\mathcal { M } = \{ ( x , y ) : x \in \mathcal { M } _ { X } , y \in \mathcal { M } _ { Y | x } \}$ as the support of the joint distribution $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ . Let $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ represent the density function of $\mu _ { Y | x } ^ { * }$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ . Moreover, $\textstyle { \mathcal { M } } _ { Y } = \bigcup _ { x \in { \mathcal { M } } _ { X } } { \mathcal { M } } _ { Y \mid x }$ is the support of the marginal distribution of $Y$ .

We will also refer to the notations from the definition of the $( \beta _ { Y } , \beta _ { X } )$ -smooth submanifold family as outlined in Definition 4 in the main text, and provide a recapitulation here: for any $w _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in$ $\mathcal { M }$ , there exists a neighborhood $U _ { \omega _ { 0 } }$ of $y _ { 0 }$ on $\mathcal { M } _ { Y }$ , so that for any $x \in \mathbb { B } _ { M _ { X } } ( x _ { 0 } , \tau )$ , the function $\mathrm { P r o j } _ { T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } } } ( y - y _ { 0 } ) : \mathcal { M } _ { Y }  T _ { y _ { 0 } } \mathcal { M } _ { Y | x _ { 0 } }$ , when restricted to $U _ { \omega _ { 0 } } \cap \mathcal { M } _ { Y | x }$ , is a diffeomorphism with inverse function $\phi _ { \omega _ { 0 } , x } ( \cdot )$ defined on $\mathbb { B } _ { T _ { M _ { Y | x _ { 0 } } } y _ { 0 } } ( 0 , \tau _ { 1 } )$ . Moreover, the function $\Phi _ { \omega _ { 0 } } : \mathbb { B } _ { T _ { \mathcal { M } _ { Y | x _ { 0 } } } y _ { 0 } } ( 0 , \tau _ { 1 } ) \times$ $\mathbb { B } _ { M _ { X } } ( x _ { 0 } , \tau )  \mathbb { R } ^ { D _ { Y } }$ define as $\Phi _ { \omega _ { 0 } } ( z , x ) = \phi _ { \omega _ { 0 } , x } ( z )$ belongs to $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { T _ { \mathcal { M } _ { Y | x _ { 0 } } } y _ { 0 } } ( 0 , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$

For any point $w _ { 0 } \in \mathcal { M }$ , the terms $U _ { w _ { 0 } }$ , $\Phi _ { w _ { 0 } }$ will be used to denote the neighborhood and function described above respectively. In the scenario where the response space remains invariant across different covariates (referred to as Regime 2), we have $\mathcal { M } _ { Y | x } = \mathcal { M } _ { Y }$ for all $x \in \mathcal { M } _ { X }$ . Consequently, $\Phi _ { \omega _ { 0 } } ( z , x )$ is independent of $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } } ( \mathbb { B } _ { T _ { \boldsymbol { M } _ { Y | x _ { 0 } } } y _ { 0 } } ( 0 , \tau _ { 1 } ) )$ $x$ , allowing us to simplify the notation to . $\Phi _ { \omega _ { 0 } } ( z ) = \Phi _ { \omega _ { 0 } } ( z , x )$ , and we have $\Phi _ { \omega _ { 0 } } ( z ) \in$

# D.1 Proof of Theorem 9

We consider the estimator defined in Appendix B.2.1. For any $j \in \{ 0 \} \cup [ J ]$ with $\begin{array} { r } { J = \lceil \frac { 1 } { d _ { Y } } \cdot \log _ { 2 } \bigl ( \frac { n } { \log n } \bigr ) \rceil } \end{array}$ , the following lemma provides a bound for the mean squared error between $\widehat { S } _ { j } ^ { \dag } ( \psi , x )$ and $u _ { \psi } ^ { * } ( x ) =$ $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) ] .$ .

Lemma 12. Suppose $\mu ^ { * } \in \mathcal { P } _ { 2 }$ and with the choices of $\boldsymbol { S } _ { j } ^ { \dagger }$ defined in (14), it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \bigg [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) - u _ { \psi } ^ { * } ( x ) ) ^ { 2 } \bigg ] \lesssim 2 ^ { \frac { 2 j \alpha _ { X } d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \big ( \frac { n } { \log n } \big ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

The proof of Lemma 12 is given in Appendix D.7. Then let η = dY αX2αX+dX . Utilizing the property that for any function $f \in \mathbb { H } _ { 1 } ^ { \eta } ( \mathbb { R } ^ { D _ { Y } } )$ and $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , it holds that $\begin{array} { r } { | f _ { \psi } | = | \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) { \mathrm { d } } y | \lesssim 2 ^ { - j \eta - j D _ { y } } } \end{array}$ , we can deduce that with probability at least $\textstyle { \mathrm { ~ I ~ - ~ } } { \frac { 1 } { n ^ { 2 } } }$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { k } ^ { n } } \bigg [ \underset { f \in \mathbb { R } ^ { n } } { \operatorname* { s u p } } \bigg | \underset { 0 \leq t \leq r } { \operatorname* { s u p } } \Big | \underset { f \in \mathcal { G } _ { 1 } ^ { n } \times \{ 1 \} } \big | \mathcal { G } _ { \varepsilon _ { k } ^ { n } \times \mathcal { G } _ { 1 } ^ { n } } \big | \mathcal { G } _ { \varepsilon _ { k } ^ { n } } \Big ) - \underset { 0 \leq t \leq r } { \sum } \sum _ { \substack { \xi _ { \xi } = 0 } } \sum _ { \xi _ { \xi } \in \mathcal { G } _ { 2 } ^ { 2 ( \xi ) \times \mathcal { G } _ { 2 } } } \mathcal { F } _ { \xi } \big ( \xi _ { k } , X \big ) \big | \Big ] } \\ & { \leq \mathbb { E } _ { \mu _ { k } ^ { n } } \bigg [ \underset { f \in \mathcal { G } _ { 1 } ^ { n } \times \mathcal { G } _ { 1 } ^ { n } } { \operatorname* { s u p } } \bigg | \underset { 0 \leq t \leq r } { \sum } \sum _ { \substack \xi _ { \xi } \in \mathcal { G } _ { \phi ^ { \pm } \times \mathcal { G } _ { 2 } ^ { n } } } \int _ { \xi _ { \xi } \in \mathcal { G } _ { \xi } ^ { 2 } } { \operatorname* { s u p } } _ { \xi _ { 1 } ^ { n } \times \mathbb { E } } \big | \mathcal { G } ( \xi ) \big | - \underset { j = r + 1 } { \overset { j } { \sum } } \sum _ { \substack { \xi = 1 } } \int _ { \xi \in \phi \phi ^ { \xi _ { 2 } } } \mathcal { F } _ { \xi } \big ( \xi , X \big ) \Big | \Big ] } \\ &  + \underset { f \in \mathcal { G } _ { 2 } ^ { n } \times \mathcal { G } _ { 2 } ^ { n } \times \mathcal { G } _ { 1 } ^ { n } } { \operatorname* { s u p } } \bigg | \underset { j = r + 1 } { \overset { j } { \sum } } \sum _ { \substack { \xi = 1 } } \int _ { \xi \in \phi } \end{array}
$$

So for any γ ≥ η = dY αX2α +d , it holds that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { \star } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu _ { Y | X } ^ { * } } f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } f _ { \psi 2 } \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) | \Big ] } \\ & { \leq \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { ( \mathbb { R } ^ { D _ { Y } } ) } } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu _ { Y | X } ^ { * } } f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } f _ { \psi 2 } \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \Big | \Big ] } \\ & { \lesssim ( \log n ) \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } . } \end{array}
$$

# D.2 Proof of Theorem 10

We first derive the following results concerning the population-level reconstruction error for the first step of manifold recovery, the proof of which is given in Appendix D.8.

Lemma 13. Suppose $\mu ^ { * } \in \mathcal { P } _ { 2 } ^ { * }$ and with the choices of $\mathcal { G }$ defined in (17), there exist positive constants $C , C _ { 1 }$ so that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

1. For any $k \in { \widehat { \mathcal { K } } }$ and $\gamma _ { 1 } \in ( 0 , 1 ] ,$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { \lesssim \left\{ \begin{array} { l l } { \qquad C \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \frac { d _ { Y } ^ { * } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } , } \\ { C ( \log n \wedge \frac { 1 } { d _ { Y } - 2 \gamma _ { 1 } \beta _ { Y } } ) ^ { 1 + \gamma _ { 1 } } \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { Y } } } } & { \frac { d _ { Y } ^ { * } } { \beta _ { Y } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

2. For any $k \in { \widehat { K } } ,$ , there exists $( x _ { k } ^ { * } , y _ { k } ^ { * } ) \in \mathbb { B } _ { \mathcal { M } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } )$ such that

$$
\widehat V _ { [ k ] } ^ { T } { \cal P } _ { [ k ] } ^ { * } \widehat V _ { [ k ] } \gtrsim C _ { 1 } I _ { d _ { Y } } ,
$$

where $\mathcal { P } _ { [ k ] } ^ { * }$ is the projection matrix of $T _ { \mathcal { M } _ { Y } } y _ { k } ^ { * }$

Given the assumption that $\mathcal { M } _ { Y | x } = \mathcal { M } _ { Y }$ for any $x \in \mathcal { M } _ { x }$ , and note that if a function $f ( y , x )$ is $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth for some $\beta _ { X } ~ > ~ 0$ , and if $f ( y , x )$ is independent of $x$ , then $f ( y ) = f ( y , x )$ must inherently be $\mathcal { H } ^ { \beta _ { Y } }$ -smooth. Conversely, if $f ( y )$ is $\mathcal { H } ^ { \beta _ { Y } }$ -smooth, defining $f ( y , x ) = f ( y )$ will result in a function being $\mathcal { H } ^ { \beta _ { Y } , \beta _ { X } }$ -smooth for any $\beta _ { X } > 0$ . Consequently, we can use Lemma 4 from Appendix A.2 to obtain the invertibility of $\widehat { V } _ { [ k ] } ^ { T } ( \cdot - \upsilon _ { k } )$ . Specifically, when $\tau _ { 2 }$ is small enough, given the second statement in Lemma 13, for any $k \in { \widehat { \mathcal { K } } }$ , there exists a subset $\widehat { U } _ { Y } ^ { [ k ] }$ so that $\mathbb { B } _ { \mathcal { M } _ { Y } } ( y _ { k } ^ { * } , 3 \tau _ { 2 } ) \subset \widehat { U } _ { Y } ^ { [ k ] } \subset \mathcal { M } _ { Y }$ , and the function $\widehat { Q } _ { [ k ] } ( \cdot ) = \widehat { V } _ { [ k ] } ^ { T } ( \cdot - y _ { k } )$ , when restricted to domain ${ \widehat { U } } _ { Y } ^ { [ k ] }$ , is a diffeomorphism that maps ${ \widehat { U } } _ { Y } ^ { [ k ] }$ to $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } )$ with inverse denoted as $[ \widehat { Q } _ { [ k ] } ( \cdot ) ] ^ { - 1 }$ . The function $\widehat { G } _ { [ k ] } ^ { \dagger } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } -$ $y _ { k } ) , 3 \tau _ { 2 } ) \to \mathbb { R } ^ { D _ { Y } }$ defined as $\widehat { G } _ { [ k ] } ^ { \dagger } ( z ) = [ \widehat { Q } _ { [ k ] } ( \cdot ) ] ^ { - 1 } ( z )$ belongs to $\mathcal { H } _ { L _ { 1 } , D _ { Y } } ^ { \beta _ { Y } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) )$ for some constant $L _ { 1 }$ . Based on this fact, the push forward measure $\widehat { Q } _ { [ k ] \# } ( \mu _ { Y | x } ^ { * } | _ { \widehat { U } _ { Y } ^ { [ k ] } } )$ , has a density ${ \widehat { \nu } } _ { [ k ] } ( z | x ) = u ^ { * } ( { \widehat { G } } _ { [ k ] } ^ { \dagger } ( z ) | x ) \cdot \sqrt { \operatorname * { d e t } ( J _ { { \widehat { G } } _ { [ k ] } ^ { \dagger } } ( z ) ^ { T } J _ { { \widehat { G } } _ { [ k ] } ^ { \dagger } } ( z ) ) }$ for $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } )$ , where $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ is the density of $\mu _ { Y | x } ^ { * }$ with respect to the volume measure of $\mathcal { M } _ { Y }$ . Since $\beta _ { Y } \geq \alpha _ { Y } + 1$ , there exists a constant $L _ { 2 }$ so that $\begin{array} { r } { \hat { \mathcal { V } } _ { [ k ] } ( z , | , x ) \in \mathcal { \overline { H } } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) , \mathcal { M } _ { X } ) } \end{array}$ . Furthermore, for any $j \in \mathbb N$ and $\psi \in \Psi _ { j } ^ { d _ { Y } }$ , we have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] } \\ & { \ = \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) \mathbf { 1 } ( Y \in \widehat { U } _ { Y } ^ { [ k ] } ) \mathbf { 1 } ( x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { k } ^ { * } , 2 \tau _ { 2 } ) ) ] } \\ & { \ = \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , \widehat { G } _ { [ k ] } ^ { \dagger } ( \widehat { Q } _ { [ k ] } ( Y ) ) ) \mathbf { 1 } ( Y \in \widehat { U } _ { Y } ^ { [ k ] } ) ] } \\ & { \ = \displaystyle \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } Y } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) } \psi ( z ) \rho _ { [ k ] } ( x , \widehat { G } _ { [ k ] } ^ { \dagger } ( z ) ) \widehat { v } _ { [ k ] } ( z | x ) \mathrm { d } z . } \end{array}
$$

Let $\overline { { \nu } } _ { [ k ] } ( z , | , x ) \in \overline { { \mathcal { H } } } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $\widehat { \nu } _ { [ k ] } ( z , | , x )$ to $\mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } }$ . Define

$$
\widetilde v _ { [ k ] } ( z , x ) = \left\{ \begin{array} { l l } { \rho _ { [ k ] } ( x , \widehat G _ { [ k ] } ^ { \dagger } ( z ) ) \overline { { \nu } } _ { [ k ] } ( z | x ) , } & { \mathrm { ~ i f ~ } z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat V _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) , x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } ) } \\ { 0 } & { \mathrm { ~ o t h e r w i s e } . } \end{array} \right.
$$

We can verify that $\widetilde { v } _ { [ k ] } ( z , x ) \in \mathcal { \overline { H } } _ { L _ { 3 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ with a constant $L _ { 3 }$ . Therefore, for any $j \in \mathbb N$ $\psi \in \Psi _ { j } ^ { d _ { Y } }$ and $x \in \mathcal { M } _ { X }$ , it holds that

$$
2 ^ { \frac { d _ { Y } j } { 2 } } \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] = 2 ^ { \frac { d _ { Y } j } { 2 } } \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | x ) \mathrm { d } z ,
$$

and $\begin{array} { r } { 2 ^ { \frac { d _ { Y } j } { 2 } } \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | \cdot ) \mathrm { d } z \in \mathcal { H } _ { L _ { 4 } } ^ { \alpha _ { X } } ( \mathbb { R } ^ { D _ { X } } ) } \end{array}$ for some constant $L _ { 4 }$ . Moreover, for any $x \in \mathcal { M } _ { X }$ , given that $\widetilde { v } _ { [ k ] } ( \cdot | x ) \in \mathcal { H } _ { L _ { 3 } } ^ { \alpha _ { Y } } ( \mathbb { R } ^ { d _ { Y } } )$ , it follows that for any $x \in \mathcal { M } _ { X }$ ,

$$
\left| \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] \right| = \Big | \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | x ) \mathrm { d } z \Big | \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } - j \alpha _ { Y } } .
$$

Let $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . For $j \in \{ 0 \} \cup [ J ]$ , denote

$$
\mathbf { \Psi } _ { j } ^ { \sharp } = \{ S : \Psi _ { j } ^ { d _ { Y } } \times \mathbb { R } ^ { D \chi } \to \mathbb { R } : S ( \psi , x ) = \sum _ { \psi _ { 1 } \in \Psi _ { j } ^ { d _ { Y } } } s _ { \psi _ { 1 } } ( x ) , \mathrm { ~ w h e r e ~ } s _ { \psi _ { 1 } } \in \mathcal { S } _ { j } \mathrm { ~ f o r ~ e a c h ~ } \psi _ { 1 } \in \Psi _ { j } ^ { d _ { Y } } \} ,
$$

where ${ \mathcal { S } } _ { j }$ is defined in (19). Using the independence of $\{ X _ { i } \} _ { i \in I _ { 1 } }$ and $\{ X _ { i } \} _ { i \in I _ { 2 } }$ , and mirroring the analysis from the proof of Lemma 9—where we replace $D _ { Y }$ with $d _ { Y }$ , and modify $\psi ( Y )$ to $\psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y )$ To apply Theorem 8, we set $\{ \psi _ { \lambda } ( ( X , Y ) ) \} _ { \lambda \in \Lambda } = \{ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) : \ \psi \in \Psi _ { j } ^ { d _ { Y } } \}$ , where the response variable $Y$ is redefined as the joint vector of $( X , Y )$ , alongside $\boldsymbol { S } = \boldsymbol { S } _ { j } ^ { \ddag }$ — we can show that, by applying a union argument over $j \in [ J ]$ and $k \in { \widehat { \mathcal { K } } }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ and $k \in { \widehat { \mathcal { K } } }$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } ( \widehat { v } _ { k \psi } ( X ) - \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) ] ) ^ { 2 } \Big ] \lesssim 2 ^ { \frac { 2 j \alpha _ { X } d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } ( \frac { n } { \log n } ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

Furthermore, recall that

$$
\widehat { K } = \{ k \in [ K ] : \exists i \in I _ { 1 } , \| ( X _ { i } , Y _ { i } ) - ( x _ { k } , y _ { k } ) \| \leq \sqrt { 2 } \tau _ { 2 } \} .
$$

So for any $k \in [ K ] \setminus { \widehat { \mathcal { K } } }$ , it holds that

$$
\frac { 1 } { n } \sum _ { i \in I _ { 1 } } \rho _ { [ k ] } ( X _ { i } , Y _ { i } ) \leq \frac { 1 } { n } \sum _ { i \in I _ { 1 } } \mathbf { 1 } ( \| ( X _ { i } , Y _ { i } ) - ( x _ { k } , y _ { k } ) \| \leq \sqrt { 2 } \tau _ { 2 } ) = 0 ,
$$

and by Bernstein’s inequality, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $k \in [ K ] \setminus { \widehat { \mathcal { K } } }$

$$
\mathbb { E } _ { \mu ^ { * } } [ \rho _ { [ k ] } ( X , Y ) ] \lesssim \sqrt { \frac { \log n } { n } } .
$$

Denote $\begin{array} { r } { \widehat { \mu } _ { Y | x } = \sum _ { k \in \widehat { \mathcal { K } } } \widehat { G } _ { [ k ] } ( \cdot , x ) _ { \# } \widehat { \nu } _ { [ k ] } ( \cdot | x ) } \end{array}$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

$$
\begin{array} { r l } & { \begin{array} { r l } & { \sum _ { i = 1 } \biggl \{ \underset { j \in \mathcal { N } _ { i } \backslash i \in \mathcal { N } _ { i } } { \mathrm { A u p } } } \biggr \} \biggl \{ \int \mathrm { f o r } \mathrm { d } \mathrm { b } \mathrm { b } \mathrm { t } _ { i } ^ { * } \mathrm { * } \mathrm { * } - \int \mathrm { f o r } \mathrm { d } \mathrm { b } \mathrm { d } \mathrm { b } \mathrm { t } _ { i } \mathrm { * } \mathrm { * } \mathrm { * } \biggr | } \\ & { - \mathbb { E } _ { \mathrm { s } \backslash i \backslash i \mathrm { ~ f o r } } \biggr \} \biggl \{ \int \mathrm { c } \mathrm { i } \mathrm { b } \mathrm { d } \mathrm { b } \mathrm { t } _ { i } ^ { * } \mathrm { * } \mathrm { * } - \int \mathrm { f o r } \mathrm { d } \mathrm { b } \mathrm { d } \mathrm { b } \mathrm { t } _ { i } \mathrm { * } \mathrm { * } \biggr | } \\ & { - \mathbb { E } _ { \mathrm { s } \backslash i \backslash i \mathrm { ~ f o r } } \biggr \} \biggl \{ \int _ { - 1 } ^ { \infty } \mathrm { b } \mathrm { d } \mathrm { b } \mathrm { d } \mathrm { s } \mathrm { * } \mathrm { * } \mathrm { * } \biggr | } \\ & { \leq \mathbb { E } _ { \mathrm { s } \backslash i \backslash i \mathrm { ~ f o r } } \mathrm { * } \mathrm { * } \mathrm { * } \mathrm { * } \mathrm { * } \mathrm { ' } \int \sum _ { i = 1 } ^ { \infty } \mathrm { b } \mathrm { d } \mathrm { | } \mathrm { d } \mathrm { \Omega } \mathrm { b } \mathrm { * } \mathrm { * } \mathrm { ' } \mathrm { * } \mathrm { * } \biggr / \mathrm { d } \mathrm { b } \mathrm { * } \mathrm { * } \mathrm { ' } \mathrm { * } \biggr \} \biggr \} \end{array} } \\ &  \leq \mathbb { E } _ { \mathrm { s } \backslash i } \sum _ { i \in \mathcal { N } _ { i } \backslash i \in \mathcal { N } _ { i } \backslash i } \int _ { - 1 } ^ { \infty } \int _ { - 1 } ^ { \infty } \int _ { - 1 } ^ { \infty } \end{array}
$$

To simplify the notation, for any $j > J , k \in \widehat { \mathcal { K } }$ and $\psi \in \Psi _ { j } ^ { d _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau _ { 2 } ) \neq$ $\emptyset \}$ , we set $\widehat { v } _ { k \psi } ( \cdot ) \equiv 0$ . Then denote $\begin{array} { r } { f _ { \psi } = \int f ( y ) \psi ( y ) \mathrm { d } y } \end{array}$ , it holds with probability at least $\textstyle 1 - { \frac { 3 } { n ^ { 2 } } }$ that for any $\gamma \in ( 0 , 1 ]$ ,

$$
\begin{array} { r l } & { \mathbb { E } [  \sum _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } \mathrm { d } \hat { \Phi } ( \mathbf { x } , \ell \mathbf { x } ) \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } - \int _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \Big | \sum _ { \ell \in \mathcal { R } _ { N } } \Big | \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \Big | } \\ & { \quad \le \mathbb { E } [  \sum _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } \mathrm { d } \hat { \Phi } ( \mathbf { x } , \ell \hat { \Phi } ( \hat { \Phi } ( \mathbf { x } ) ) ) \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } | ] } \\ &  \quad \quad = \mathbb { E } [  \sum _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \sum _ { \ell \in \mathbb { R } _ { N } } \int _ { 0 } ^ { \infty } \int _ { 0 } ^ { \infty } \mathrm { d } \hat { \Phi } ( \mathbf { x } , \ell \mathbf { x } ) \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } \mathrm { d } \hat { \mathbf { x } } _ { \ell } - \sum _ { \ell } ^ { \prime } \int _ { 0 } ^ { \infty } \mathrm { d } \hat { \Phi } ( \mathbf { x } , \ell \mathbf { x } ) \sum _  \ell \in \mathbb  R  \end{array}
$$

$$
\begin{array} { r l } & { \Gamma _ { \mathrm { R C } } ^ { \mathrm { R C } } = \frac { \Gamma _ { 1 } ^ { \mathrm { R C } } } { \Gamma _ { 1 } ^ { \mathrm { R C } } } , \quad \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , } \\ & { \quad + \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 2 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 2 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 2 } ^ { \mathrm { R C } } = \mathrm { R C } , } \\ & { = \sum _ { \boldsymbol { \mathcal { \mathcal { \bar { \mathcal { \Lambda } } } } _ { c } \in [ [ \boldsymbol { \mathcal { T } } ] ] } } \sum _ { \boldsymbol { \mathcal { \bar { \mathcal { \Lambda } } } _ { c } \in [ \boldsymbol { \mathcal { R } } ] } } \Gamma _ { \mathrm { R C } } ^ { \mathrm { R C } } \mathrm { R C } , \quad \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 2 } ^ { \mathrm { R C } } = \mathrm { R C } , } \\ & { \quad - \sum _ { \boldsymbol { \mathcal { \bar { \mathcal { \Lambda } } } _ { c } \in [ \boldsymbol { \mathcal { T } } ] } } \Gamma _ { \mathrm { R C } } ^ { \mathrm { R C } } \mathrm { R C } , \quad \Gamma _ { 2 } ^ { \mathrm { R C } } = \mathrm { R C } , \quad \Gamma _ { 1 } ^ { \mathrm { R C } } = \mathrm { R C } , } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array}
$$

$$
( E _ { A } ) \lesssim ( \log n \wedge \frac { \mathbf { 1 } ( d _ { Y } / \beta _ { Y } > 2 \gamma ) } { \beta _ { Y } d _ { Y } - 2 \gamma \beta _ { Y } ) } ) ^ { 2 } \cdot n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } + \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } .
$$

Moreover, since $| f _ { \psi } | \lesssim 2 ^ { - j \gamma - j d _ { Y } / 2 }$ for $\psi \in \Psi _ { j } ^ { d _ { Y } }$ , we have

$$
\begin{array} { r l } & { \displaystyle \big ( E _ { B } \big ) \lesssim \sum _ { k \in \widehat { \mathcal { K } } } \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } 2 ^ { - j \gamma - \frac { j d _ { Y } } { 2 } } \sqrt { \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \Big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) ] - \widehat { \nu } _ { k \psi } ( X ) \Big ) ^ { 2 } \right] } } \\ & { \quad \lesssim \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \displaystyle \sum _ { j = 0 } ^ { J } \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } 2 ^ { - 2 j \gamma } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \Big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) ] - \widehat { \nu } _ { k \psi } ( X ) \Big ) ^ { 2 } \right] } } \\ & { \quad \lesssim ( \log n ) \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + C _ { 1 } \big ( \frac { n } { \log n } \big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } , } \end{array}
$$

and

$$
\begin{array} { c } { { ( E _ { C } ) \lesssim \displaystyle \sum _ { k \in \widehat { K } } \displaystyle \sum _ { j = J + 1 } ^ { \infty } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } 2 ^ { - j ( \gamma + \alpha _ { Y } ) - j d _ { Y } } } } \\ { { \lesssim ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } } } \end{array}
$$

Finally, we have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { \star } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \Upsilon } ( \mathbb { R } ^ { D } Y ) } { \operatorname* { s u p } } \Big | \int f ( y ) \mathrm { d } \mu _ { Y \mid X } ^ { \star } - \int f ( y ) \mathrm { d } \widehat { \mu } _ { Y \mid X } \Big | \Big ] } \\ & { \lesssim \sqrt { \frac { \log n } { n } } + ( E _ { A } ) + ( E _ { B } ) + ( E _ { C } ) } \\ & { \lesssim ( \log n ) ^ { 2 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \big ( \frac { n } { \log n } \big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } + n ^ { - \frac { \gamma } { \frac { \beta _ { Y } } { \beta _ { Y } } } } . } \end{array}
$$

# D.3 Proof of Theorem 6 (minimax upper bound for Regime 2 and 3b)

# D.3.1 Proof for Regime 2

We consider the estimator detailed in Appendix B.2.3. For

$$
\begin{array} { r l } & { \widehat { \mathcal { I } } ( f , x ) = \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } f _ { \psi } 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) + \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { { \overline { { J } } } } ^ { \bot } ( \widehat { G } _ { [ k ] } ( z ) ) \displaystyle \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \mathrm { d } x } \\ & { f _ { \psi } = \displaystyle \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) \mathrm { d } y , \quad f _ { { \overline { { J } } } } ^ { \bot } ( y ) = f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) , } \end{array}
$$

where $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . We can get

$$
\begin{array} { r l } & { \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { p _ { Y } } ) } { \operatorname* { s u p } } \left| \mathbb { E } _ { \mu _ { Y | X } ^ { * } \left[ f \left( Y \right) \right] - \widehat { \mathcal { T } } ( f , X ) } \right| \Big ] } \\ & { \overset { \xi } { \underset { i \in \mathcal { H } _ { 1 } ^ { \prime } \left[ \mathbb { R } ^ { p _ { Y } } \right] } { \operatorname* { s u p } } } \underset { j = 0 } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { p _ { Y } } } { \sum } \underset { ( E _ { i } ^ { * } \backslash \mathcal { K } ) } { f _ { i } \psi ( \mathbb { R } _ { i _ { Y } ^ { * } \backslash I } ^ { * } \left[ \psi ( Y ) \right] - 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) ) } \big | \Big ] } \\ & { \overset { ( E _ { i } ) } { \underset { i \in \mathcal { H } _ { 1 } ^ { * } } { \operatorname* { s u p } } } \underset { \xi \in \mathcal { H } _ { 1 } ^ { * } \left[ \mathbb { R } ^ { p _ { Y } } \right] } { \operatorname* { s u p } } \Big | \mathbb { E } _ { \mu _ { Y | X } ^ { * } \left[ \begin{array} { c } { ( E _ { 1 } ^ { * } ( X , Y ) f _ { j } ^ { \bot } ( Y ) + \sum _ { k \in \widehat { K } } \rho _ { [ k ] } ( X , Y ) \left( f _ { j } ^ { \bot } ( Y ) - f _ { j } ^ { \bot } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \right) } \\ { k \in [ K ] \backslash \widehat { K } } \end{array} \right] } } \end{array}
$$

$$
+ \mathbb { E } _ { \mu _ { X } ^ { s } } \Big [ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \mathcal { I } } ( \mathbb { R } ^ { D } Y ) } \Big | \sum _ { k \in \widehat { \mathcal { K } } } \mathbb { E } _ { \mu _ { Y | X } ^ { s } } \big [ f _ { \mathcal { I } } ^ { \bot } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) ) \rho _ { [ k ] } ( X , Y ) \big ] - \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { \mathcal { I } } ^ { \bot } ( \widehat { G } _ { [ k ] } ( z ) ) \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ j ] } ) ) ) ) ) \rho _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ k ] } ( \widehat { G } _ { [ j ] } ) ) ) \big ] \Big | _ { \widehat { X } } d \widehat { G } _ { [ k ] }
$$

We first bound term $\left( E _ { A } \right)$ , notice that

$$
\begin{array} { r l } & { \left( E _ { A } \right) \ \le \ C \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { - j \gamma - \frac { j D _ { Y } } { 2 } } \sqrt { \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } \left[ 2 ^ { \frac { j \left( d _ { Y } - D _ { Y } \right) } { 2 } } \psi ( Y ) \right] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \right) ^ { 2 } \right] } } \\ & { \qquad \le C \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } 2 ^ { - j D _ { Y } } \cdot 2 ^ { - j \gamma } \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } \left[ 2 ^ { \frac { j \left( d _ { Y } - D _ { Y } \right) } { 2 } } \psi ( Y ) \right] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \right) \right. } } \\ & { \qquad \le \ C _ { 1 } \displaystyle \sum _ { j = 0 } ^ { J } 2 ^ { - j \gamma } \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } \left[ 2 ^ { \frac { j \left( d _ { Y } - D _ { Y } \right) } { 2 } } \psi ( Y ) \right] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \right) ^ { 2 } \right] } , } \end{array}
$$

where the first inequalities uses f ∈ Hγ1 (RDY ), which implies |fψ| ≲ 2−jγ− j , alongside Jensen’s inequality; the second inequality is derived using the Cauchy-Schwarz inequality, while the final inequality uses the fact that $| \Psi _ { j } ^ { D _ { Y } } | = \mathcal { O } ( 2 ^ { D _ { Y } j } )$ . We then bound the mean squared error $\begin{array} { r l } { } & { \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \right. \right. } \end{array}$ $\widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) ^ { 2 } \Big ]$ for each $j$ by applying Lemma 12, which yields

$$
\sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \right) ^ { 2 } \right] \lesssim 2 ^ { \frac { 2 j \alpha _ { X } d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \big ( \frac { n } { \log n } \big ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

This further implies

$$
E _ { A } ) \lesssim \sum _ { j = 0 } ^ { J } 2 ^ { - j \gamma } \big ( 2 ^ { \frac { j \alpha _ { X } d \gamma } { 2 \alpha _ { X } + d _ { X } } } \big ( \frac { n } { \log { n } } \big ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \big ) \lesssim ( \log { n } ) \cdot \big ( \frac { n } { \log { n } } \big ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + \big ( \frac { n } { \log { n } } \big ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } + d _ { X } } } } \big ( \frac { n } { \log { n } } \big ) ^ { \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { X } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } + d _ { X } } } } .
$$

Note that when γ > $\begin{array} { r } { \gamma > \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ the dominant term in the summation is at $j = 0$ , indicating that the bottleneck lies in learning the overall dependence of $Y$ on $X$ , reflected by the conditional mean of the wavelets at smaller levels, leading to a term of n−αX/(2αX+dX). Conversely, when γ < dY αX2αX+dX , the dominant term is at $j = J$ , suggesting that the bottleneck is in learning finer irregularities of the conditional distribution, captured by the conditional mean of the wavelets at higher levels, resulting in a term of $n ^ { - ( \alpha _ { Y } + \gamma ) / \left( 2 \alpha _ { Y } + D _ { Y } ^ { - } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } \right) }$ + αYαX dX. Then for the term (EB) and (EC ), notice that

$$
f _ { J } ^ { \perp } ( y ) = f ( y ) - \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) = \sum _ { j = J + 1 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) \lesssim 2 ^ { - J \gamma } ,
$$

and there exists a constant $C$ so that for any $y , y ^ { \prime } \in \mathbb { R } ^ { D _ { Y } }$ , $j \in \mathbb N$ and $\psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } }$ ,

$$
| \psi ( y ) - \psi ( y ^ { \prime } ) | \leq C 2 ^ { j + \frac { j D _ { y } } { 2 } } \| y - y ^ { \prime } \| ,
$$

and

$$
| \psi ( y ) - \psi ( y ^ { \prime } ) | \leq | \psi ( y ) | + | \psi ( y ^ { \prime } ) | \leq C 2 ^ { \frac { j D _ { y } } { 2 } } .
$$

So let $J ^ { \prime } = - \log _ { 2 } ( n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } + n ^ { - \frac { \alpha _ { X } } { ( 2 \alpha _ { X } + d _ { X } ) \gamma } } )$ , when $\begin{array} { r } { 1 \le \gamma \le \frac { d _ { Y } \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ ,

$$
\begin{array} { r l } & { \bigl | f _ { J } ^ { \perp } ( y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) \bigr | } \\ & { \leq \big | \displaystyle \sum _ { j = J + 1 } ^ { J ^ { \prime } } \displaystyle \sum _ { \psi \in \overline { { \mathbb { V } } } _ { j } ^ { D } } f _ { \psi } \psi ( y ) - \displaystyle \sum _ { j = J + 1 } ^ { J ^ { \prime } } \displaystyle \sum _ { \psi \in \overline { { \mathbb { V } } } _ { j } ^ { D } } f _ { \psi } \psi ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) \big | + n ^ { - \frac { \gamma } { \frac { \beta \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } } \\ & { \lesssim \displaystyle \sum _ { j = J + 1 } ^ { J ^ { \prime } } 2 ^ { - j ( \gamma - 1 ) } ( 2 ^ { - j } \wedge \| y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) \| ) + n ^ { - \frac { \gamma } { \frac { \beta \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } ; } \end{array}
$$

when $\gamma \leq 1$ , let $\begin{array} { r } { \gamma _ { 1 } = ( \frac { 2 \alpha _ { X } + d _ { X } } { 2 \alpha _ { X } } \gamma ) \wedge 1 } \end{array}$ , then

$$
\begin{array} { l } { \displaystyle | f _ { J } ^ { \perp } ( y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) | } \\ { \displaystyle \leq | \sum _ { j = J + 1 } ^ { J ^ { \prime } } \sum _ { y \in \overline { { \Psi } } _ { j } ^ { D } \gamma } f _ { \psi } \psi ( y ) - \sum _ { j = J + 1 } ^ { J ^ { \prime } } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D } \gamma } f _ { \psi } \psi ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) | + n ^ { - \frac { \gamma } { \frac { 4 \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha \chi } { 2 \alpha _ { X } + d \chi } } } \\ { \displaystyle \lesssim \sum _ { j = J + 1 } ^ { J ^ { \prime } } 2 ^ { - j ( \gamma - 1 ) } ( 2 ^ { - j } \wedge \| y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) \| ) + n ^ { - \frac { \gamma } { \frac { 4 \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha \chi } { 2 \alpha _ { X } + d \chi } } } \\ { \displaystyle \lesssim \sum _ { j = J + 1 } ^ { J ^ { \prime } } 2 ^ { j ( \gamma _ { 1 } - \gamma ) } \| y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) \| ^ { \gamma _ { 1 } } + n ^ { - \frac { \gamma } { \frac { 4 \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha \chi } { 2 \alpha _ { X } + d \chi } } . } \end{array}
$$

Moreover, as demonstrated in the proof of Theorem 10 in Appendix D.2, it holds with probability at least $\textstyle 1 - { \frac { 3 } { n ^ { 2 } } }$ that

1. for any $\gamma _ { 1 } \in ( 0 , 1 ]$ and $k \in { \widehat { \mathcal { K } } }$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { \lesssim \left\{ \begin{array} { l l } { \hfill ~ C \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \hfill ~ \frac { d _ { Y } ^ { * } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } , } \\ { \hfill ~ C ( \log n \wedge \frac { 1 } { d _ { Y } - 2 \gamma _ { 1 } \beta _ { Y } } ) ^ { 1 + \gamma _ { 1 } } \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { Y } } } } & { \hfill ~ \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } ; } \end{array} \right. } \end{array}
$$

2. for any $j \in \{ 0 \} \cup [ J ]$ with $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } ( \widehat { v } _ { k \psi } ( X ) - \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) ] ) ^ { 2 } \Big ] \lesssim 2 ^ { \frac { 2 j \alpha _ { X } d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } ( \frac { n } { \log n } ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } ;
$$

3. for any $j \in \mathbb { N } , \psi \in \Psi _ { j } ^ { d _ { Y } }$ and $x \in \mathcal { M } _ { X }$ ,

4. for any

$$
\begin{array} { r l } & { ~ \Bigl | \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] \Bigr | \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } - j \alpha _ { Y } } ; } \\ & { } \\ & { , \mathbb { E } _ { \mu ^ { * } } [ \rho _ { [ k ] } ( X , Y ) ] \lesssim \sqrt { \frac { \log n } { n } } . } \end{array}
$$

So for any 1 < γ ≤ dY αY2αX+dX ,

$$
\begin{array} { r l } & { ( E _ { \mathcal { R } } ) \lesssim \underline { { \mathbb { E } } } _ { \mu ^ { \star } } [ \displaystyle \sum _ { k \in [ K ] \backslash \widehat { K } } \rho _ { [ k ] } ( X , Y ) ] + \mathbb { E } _ { \mu ^ { \star } } \Big [ \displaystyle \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \star } ( \mathbb { R } ^ { D } Y ) } \Big | \displaystyle \sum _ { k \in \widehat { \mathcal { R } } } \rho _ { [ k ] } ( X , Y ) \big ( f _ { J } ^ { \bot } ( Y ) - f _ { J } ^ { \bot } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y } \\ & { \lesssim - \textstyle \sqrt { \frac { \log n } { n } } ) + ( \log n ) \cdot 2 ^ { - J ( \gamma - 1 ) } \displaystyle \sum _ { k \in \widehat { \mathcal { R } } } \mathbb { E } _ { \mu ^ { \star } } \big [ \rho _ { [ k ] } ( X , Y ) \big ] \big | Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \big \| \big ] + n ^ { - \frac { \alpha _ { k } } { \frac { \beta _ { Y } } { \beta _ { Y } } } } + n ^ { - \frac { \alpha _ { k } } { 2 \alpha _ { X } } } } \\ & { \lesssim \frac { ( \log n ) ^ { 3 } } { \sqrt { n } } + ( \log n ) \cdot ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \gamma - 1 } { 2 \alpha _ { Y } + d \gamma + d _ { Y } \frac { \alpha _ { Y } } { \Delta _ { Y } } } - \frac { 1 } { \frac { \alpha _ { Y } } { \frac { \alpha _ { Y } } { \delta _ { Y } } } } } + n ^ { - \frac { \gamma } { \frac { 2 } { \beta _ { Y } } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } } \\ &  \lesssim ( \displaystyle \frac { n } { \log n } ) ^  - \frac { \alpha _ { Y } + \gamma }  2 \alpha _ { Y } + d _ { Y } + \frac   \end{array}
$$

where the last inequality uses the fact that $\beta _ { Y } \geq \alpha _ { Y } + 1$ . Similarly, we can get when $\gamma \leq 1$

$$
\begin{array} { r l } & { E _ { B } ) \lesssim \underline { { \mathsf { E } } } _ { \mu ^ { * } } [ \displaystyle \sum _ { k \in [ K ] \backslash \widehat { \mathcal { K } } } \rho _ { [ k ] } ( X , Y ) ] + \mathbb { E } _ { \mu ^ { * } } \Big [ \displaystyle \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { ( 1 ) } ( \mathbb { R } ^ { D } Y ) } \Big | \sum _ { k \in \widehat { \mathcal { K } } } \rho _ { [ k ] } ( X , Y ) \big ( f _ { f } ^ { \perp } ( Y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) ) } \\ & { \lesssim \displaystyle \sqrt { \frac { \log n } { n } } + n ^ { - \frac { \gamma } { \frac { \gamma } { \beta \gamma } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \log n ) \cdot \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \mathbb { E } _ { \mu ^ { * } } \big [ \rho _ { [ k ] } ( X , Y ) \big \Vert Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \big \Vert \big ] } \\ & { + \left( n ^ { \frac { \beta _ { Y } ( \tau _ { 1 } - \gamma ) } { d _ { Y } } } \wedge n ^ { \frac { \alpha _ { X } ( \tau _ { 1 } / \gamma - 1 ) } { 2 \alpha _ { X } + d _ { X } } } \right) \displaystyle \sum _ { k \in \widehat { \mathbb { K } } } \mathbb { E } _ { \mu ^ { * } } \big [ \rho _ { [ k ] } ( X , Y ) \big \Vert Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \big \Vert ^ { n } \big ] } \\ &  \lesssim n ^ { - \frac { \gamma } { \beta \gamma } } + ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \frac { n } { \log n } ) ^  - \frac  \alpha _ { Y } +  \end{array}
$$

where the last inequality uses that for $\begin{array} { r } { \gamma _ { 1 } = ( \frac { 2 \alpha _ { X } + d _ { X } } { 2 \alpha _ { X } } \gamma ) \wedge 1 } \end{array}$ , it holds that

$$
\begin{array} { r l } & { ( n ^ { \frac { \beta _ { \gamma } ( \gamma _ { 1 } - \gamma ) } { d _ { \gamma } } } \wedge n ^ { \frac { \alpha _ { X } ( \gamma _ { 1 } / \gamma - 1 ) } { 2 \alpha _ { X } + d _ { X } } } ) \displaystyle \sum _ { k \in \widehat { \mathbb { K } } } \mathbb { E } _ { \mu ^ { \ast } } \big [ \rho _ { | k | } ( X , Y ) \| Y - \widehat { G } _ { | k | } ( \widehat { Q } _ { | k | } ( Y ) ) \| ^ { \gamma _ { 1 } } \big ] } \\ & { \lesssim ( n ^ { \frac { \beta _ { \gamma } ( \gamma _ { 1 } - \gamma ) } { d _ { Y } } } \wedge n ^ { \frac { \alpha _ { X } ( \gamma _ { 1 } / \gamma - 1 ) } { 2 \alpha _ { X } + d _ { X } } } ) \cdot ( n ^ { - \frac { \gamma _ { 1 } } { \frac { \beta _ { Y } } { \beta _ { Y } } } } + \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } ) } \\ & { \lesssim n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } + \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } n ^ { \frac { \alpha _ { X } ( \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } } - 1 ) } { 2 \alpha _ { X } + d _ { X } } } } \\ & { \lesssim n ^ { - \frac { \gamma } { \frac { d _ { Y } } { \beta _ { Y } } } } + ( \log n ) ^ { 2 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } . } \end{array}
$$

When $\begin{array} { r } { \gamma \ge \eta = \frac { d _ { Y } \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ , we have

$$
\begin{array} { r l } & { ( E _ { B } ) \lesssim \sqrt { \frac { \log n } { n } } + \mathbb { E } _ { \mu ^ { * } } \biggl [ \underset { f \in \mathcal { H } _ { 1 } ^ { \eta } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \biggr | \sum _ { k \in \widehat { \mathcal { K } } } \rho _ { [ k ] } ( X , Y ) \bigl ( f _ { J } ^ { \perp } ( Y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) ) \bigr ) \bigr ] \biggr | } \\ & { \qquad \lesssim ( \log n ) ^ { 3 } n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } . } \end{array}
$$

Finally, for term $\left( E _ { C } \right)$ , it holds that

$$
\begin{array} { r l } &  \begin{array} { r l } &  \sum _ { k = 1 } ^ { n } \lambda _ { 1 } \sum _ { k = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots \sum _ { \ell = 1 } ^ { n } \cdots  \end{array} \end{array}
$$

where to derive $( i )$ , we utilize the property that there exists a positive constant $c$ so that for any $k \in { \widehat { \mathcal { K } } }$ , x ∈ MX and y ∈ RDY :

$$
f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) \rho _ { [ k ] } ( x , y ) = f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) ) ) \rho _ { [ k ] } ( x , y ) \cdot \rho ( \| \widehat { Q } _ { [ k ] } ( y ) \| ^ { 2 } / c ^ { 2 } ) ,
$$

and for any $z \in \mathbb { R } ^ { d _ { Y } }$ ,

$$
f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { \gamma } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) = f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \sum _ { j = 0 } ^ { J } \sum _ { \psi \in \Psi _ { j } ^ { d _ { \gamma } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \cdot \rho ( \| z \| ^ { 2 } / c ^ { 2 } ) ,
$$

where $\rho$ is the smooth transition function defined in (11). Furthermore, there exists a constant $C$ so that for any $f \in \mathcal { H } _ { 1 } ^ { \gamma } ( { \mathbb R } ^ { D _ { Y } } )$ , the function $2 ^ { J \gamma } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \cdot \rho ( \| z \| ^ { 2 } / c ^ { 2 } )$ satisfies

$$
\begin{array} { r l } & { \displaystyle \int _ { \mathbb { R } ^ { d _ { Y } } } \left( 2 ^ { J \gamma } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \cdot \rho ( \| z \| ^ { 2 } / c ^ { 2 } ) \right) ^ { 2 } \mathrm { d } z } \\ { \displaystyle } & { \leq \int _ { \mathbb { R } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \sqrt { 2 } c ) } \left( 2 ^ { J \gamma } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \right) ^ { 2 } \mathrm { d } z } \\ { \displaystyle } & { \leq \int _ { \mathbb { R } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \sqrt { 2 } c ) } \mathrm { d } z \cdot \underset { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \sqrt { 2 } c ) } { \operatorname* { s u p } } \left( 2 ^ { J \gamma } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z ) ) \right) ^ { 2 } } \\ { \displaystyle } & { < C . } \end{array}
$$

Therefore, it holds for any $x \in \mathcal { M } _ { X }$ that

$$
\begin{array} { r l } & { \quad \times \underset { \{ \mathcal { X } _ { i } ^ { n } \} } { \times \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \times \mathcal { X } _ { i } ^ { n } } } \Bigg \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \sum \sum \sum } \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } \{ \mathcal { \bar { Z } } _ { i } \mathcal { \bar { H } } _ { i } \mathcal { \bar { H } } _ { i } ( \mathcal { \bar { Z } } _ { i } ) \mathcal { \bar { H } } _ { i } ( \mathcal { X } _ { i } ^ { n } ) \} = \underset { \{ \mathcal { X } _ { i } ^ { n } \} } { \int } - \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \mathcal { \bar { Z } } _ { i } ^ { n } } \{ \mathcal { \bar { H } } _ { i } \mathcal { \bar { H } } _ { i } ( \mathcal { Z } ) \} \underset { \mathcal { X } _ { i } ^ { n } } { \sum \sum } \quad } \\ &  = \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \times \sum } \Bigg \{ \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \sum } \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \sum } \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } \{ \mathcal { \bar { Z } } _ { i } \mathcal { \bar \bar { H } } _ { i } ( \mathcal { \bar { H } } _ { i } ( \mathcal { \bar { X } } _ { i } ^ { n } ) ) \rho _ { \mathrm { H } } \{ \bar { X } _ { i } ^ { n } \} \} - \underset { \mathcal { X } \in \mathcal { X } } { \sum } \underset { \mathcal { X } _ { i } ^ { n } \mathcal { X } _ { i } ^ { n } } { \sum } \underset  \mathcal { X } _  \end{array}
$$

which further substantiates inequality $( i )$ . Finally, by combining the bounds for term $( E _ { A } ) , ( E _ { B } ) , ( E _ { C } ) .$ we can then get the desired results.

# D.3.2 Proof for Regime 3b

The overall structure of the proof mirrors that for Regime 2, as detailed in Appendix D.3.1. We consider the estimator $\widehat { \mathcal { I } } ( f , x )$ defined in Appendix B.3:

$$
\begin{array} { r l } & { \widehat { \mathcal { I } } ( f , x ) = \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } f _ { \psi } 2 ^ { j ( D _ { Y } - d _ { Y } ) } \widehat { S } _ { j } ^ { \dagger } ( \psi , x ) + \displaystyle \sum _ { k \in \widehat { \mathcal { K } } } \displaystyle \int _ { \mathbb { R } ^ { d _ { Y } } } f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( z , x ) ) \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \psi ( z ) \widehat { v } _ { k \psi } ( x ) \mathfrak { e } _ { j } } \\ & { \quad f _ { \psi } = \displaystyle \int _ { \mathbb { R } ^ { D _ { Y } } } f ( y ) \psi ( y ) { \mathrm { d } } y , \quad f _ { J } ^ { \perp } ( y ) = f ( y ) - \displaystyle \sum _ { j = 0 } ^ { J } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } } f _ { \psi } \psi ( y ) , } \end{array}
$$

where $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . We can get

$$
\begin{array} { r l } & { \mathbb { E } \| \mathbf { x } _ { \theta } \bigg [ \underbrace { \mathcal { A } \mathbf { z } _ { \theta } \mathbf { z } _ { \theta } \nabla \mathbf { z } _ { \theta } } _ { \mathcal { C } \times \mathcal { R } _ { \theta } ^ { \epsilon } \mathcal { R } _ { \epsilon } ^ { \epsilon } \mathcal { R } _ { \epsilon } ^ { \epsilon } } \Big [ \mathcal { A } ( \mathbf { Y } ) - \mathcal { \bar { A } } ( \mathcal { I } ) - \mathcal { \bar { A } } ( \mathcal { I } ) \Big ] \bigg ] } \\ & { \leq \mathbb { E } \underbrace { \mathcal { L } \mathbf { z } _ { \theta } \mathbf { x } _ { \theta } ^ { \epsilon } \Big [ \underbrace { \partial \mathbf { z } _ { \theta } \mathbf { x } _ { \theta } ^ { \epsilon } \nabla \mathbf { z } _ { \theta } } _ { \mathcal { C } \times \mathcal { R } _ { \epsilon } ^ { \epsilon } } \Big ] } _ { \mathcal { C } \times \mathcal { L } _ { \epsilon } } \sum _ { i = 1 } ^ { N } \mathbb { E } _ { \phi } \Big [ \mathbb { E } _ { \phi _ { \epsilon } \mathbf { x } _ { \theta } } \Big [ \Psi ( \mathbf { Y } ) \Big ] - 2 ^ { i ( \Omega _ { \epsilon } - i \Omega _ { \epsilon } - i \Omega _ { \epsilon } ) } \mathbb { \hat { S } } _ { \phi } ^ { \epsilon } ( \mathcal { R } , \mathcal { X } ) \Big ] \Big ] \bigg ] } \\ &  \leq \underbrace  \mathcal { L } \mathbf { z } _ { \theta } \mathbf { x } _ { \theta } ^ { \epsilon } \Big [ \underbrace { \mathcal { A } \mathbf { z } _ { \theta } \mathbf { z } _ { \theta } \nabla \mathbf { z } _ { \theta } } _ { \mathcal { C } \times \mathcal { L } _ { \epsilon } ^ { \epsilon } } \Big [ \underbrace { \mathcal { C } \mathbf { z } _ { \theta } \mathbf { z } _ { \theta } \nabla \mathbf { z } _ { \theta } } _ { \mathcal { C } \times \mathcal { L } _ { \epsilon } ^ { \epsilon } } \Big [ \mathcal { C } \mathbf { z } _ { \theta } \mathbf { z } \Big [ \mathbf { X } , \mathcal { Y } ] \mathbf  f  \end{array}
$$

To bound term $\left( E _ { A } \right)$ , notice that similarly to Regime 2, we have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } | \underset { j = 0 } { \overset { \mathcal { I } } { \sum } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } f _ { \psi } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( Y ) ] - 2 ^ { \frac { j ( D _ { Y } - d _ { Y } ) } { 2 } } \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) \big | \Big ] } \\ & { \lesssim \underset { j = 0 } { \overset { \mathcal { J } } { \sum } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } 2 ^ { - j \gamma - \frac { j D _ { Y } } { 2 } } \sqrt { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) ^ { 2 } \Big ] } } \\ & { \lesssim \underset { j = 0 } { \overset { \mathcal { J } } { \sum } } \sqrt { \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } 2 ^ { - 2 j \gamma } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) ^ { 2 } \Big ] } . } \end{array}
$$

Then we bound $\begin{array} { r } { \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \left( \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \right) ^ { 2 } \right] , } \end{array}$ , where recall that

$$
\widehat { S } _ { j } ^ { \dagger } = \arg \operatorname* { m i n } _ { S \in S _ { j } ^ { \dagger } } \frac { 1 } { | I _ { 1 } | } \sum _ { i \in I _ { 1 } } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y _ { i } ) - S ( \psi , X _ { i } ) ) ^ { 2 } .
$$

Lemma 14. Suppose $\mu ^ { * } \in \mathcal { P } _ { 3 } ^ { * }$ and with the choices of $\boldsymbol { S } _ { j } ^ { \dagger }$ defined in (22), it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { \star } } \Big [ \sum _ { \psi \in \Psi _ { \lambda } ^ { D } \gamma } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { \star } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) ^ { 2 } \Big ] \lesssim \frac { \log n } { n } 2 ^ { j d _ { Y } } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } } + ( \log n ) ^ { 2 } \cdot ( \varepsilon _ { j } ^ { x } ) ^ { 2 \alpha _ { X } }
$$

The proof of Lemma 14 is provided in Appendix D.9. So it holds with probability at least $\textstyle { 1 - { \frac { 1 } { n ^ { 2 } } } }$ that for any $\gamma \in ( 0 , 1 ]$ ,

$$
\begin{array} { l } { \displaystyle ( E _ { A } ) \lesssim \sum _ { j = 0 } ^ { J } 2 ^ { - j \gamma } \Big ( \sqrt { \frac { \log n } { n } } 2 ^ { j d _ { Y } / 2 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } / 2 } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } \Big ) } \\ { \lesssim ( \log n ) ^ { 2 } \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \log n ) \cdot ( \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + D _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } . } \end{array}
$$

Now we bound term $\left( E _ { B } \right)$ . Follow the same procedure as in the proof for Regime 2, let $J ^ { \prime } = - \log _ { 2 } ( n \stackrel { - \frac { 1 } { d _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } { ^ { \beta _ { Y } } } +$ $n ^ { - \frac { \alpha _ { X } } { ( 2 \alpha _ { X } + d _ { X } ) \gamma } } ,$ ), we can get, when $\begin{array} { r } { 1 \leq \gamma \leq \frac { \bar { \left( { d _ { Y } } \vee \bigl ( \frac { { d _ { Y } } } { \beta _ { Y } } + \frac { { d _ { X } } } { \beta _ { X } } \bigr ) \right) } \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ ，

$$
\begin{array} { r } { - \left. f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) ) \right| \lesssim \displaystyle \sum _ { j = J + 1 } ^ { J ^ { \prime } } 2 ^ { - j ( \gamma - 1 ) } ( 2 ^ { - j } \wedge \| y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) \| ) + n ^ { - \frac { \gamma } { \beta _ { Y } ^ { \prime } + \frac { \beta _ { X } } { \beta _ { X } } } } + n ^ { - \frac { \gamma } { 2 \alpha _ { X } } } } \end{array}
$$

and when $\gamma \leq 1$ , let $\begin{array} { r } { \gamma _ { 1 } = ( \frac { 2 \alpha _ { X } + d _ { X } } { 2 \alpha _ { X } } \gamma ) \wedge 1 } \end{array}$ , it holds that

$$
f _ { J } ^ { \perp } ( y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) ) \vert \lesssim \sum _ { j = J + 1 } ^ { J ^ { \prime } } 2 ^ { j ( \gamma _ { 1 } - \gamma ) } \Vert y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) \Vert ^ { \gamma _ { 1 } } + n ^ { - \frac { \gamma } { \frac { \gamma _ { Y } } { \beta _ { Y } } + \frac { \beta _ { X } } { \beta _ { X } } } } + n ^ { - \frac { \alpha } { 2 \alpha _ { X } } }
$$

Then we establish a bound on the population-level reconstruction error in the following lemma, the proof of which is given in Appendix D.10.

Lemma 15. Suppose $\mu ^ { * } \in \mathcal { P } _ { 3 }$ and with the choices of $\mathcal { G }$ defined in (20), for any $0 < \gamma _ { 1 } \leq 1$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that

1. For any $k \in { \widehat { \mathcal { K } } }$ and $\gamma _ { 1 } \in ( 0 , 1 ] ,$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { \star } } \mathbb { E } _ { \mu _ { Y | X } ^ { \star } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { \lesssim \left\{ \begin{array} { l l } { \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } , } \\ { \Big ( ( \log n \wedge \frac { 1 } { \beta _ { Y } ( d _ { Y } / \beta _ { Y } + d _ { X } / \beta _ { X } - 2 \gamma _ { 1 } ) } ) ^ { 1 + \gamma _ { 1 } } + ( \log n ) ^ { \gamma _ { 1 } } \Big ) \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

2. For any $k \in { \widehat { \mathcal { K } } }$ , there exists $( x _ { k } ^ { * } , y _ { k } ^ { * } ) \in \mathbb { B } _ { \mathcal { M } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } )$ such that

$$
\widehat V _ { [ k ] } ^ { T } { \cal P } _ { [ k ] } ^ { * } \widehat V _ { [ k ] } \gtrsim C _ { 1 } I _ { d _ { Y } } ,
$$

where $\mathcal { P } _ { [ k ] } ^ { * }$ k] is the projection matrix of TMY |x∗k y .

Moreover, since for any $k \in [ K ] \setminus { \widehat { \mathcal { K } } }$ , it holds that

$$
\frac { 1 } { n } \sum _ { i \in I _ { 1 } } \rho _ { [ k ] } ( X _ { i } , Y _ { i } ) \leq \frac { 1 } { n } \sum _ { i \in I _ { 1 } } \mathbf { 1 } ( \| ( X _ { i } , Y _ { i } ) - ( x _ { k } , y _ { k } ) \| \leq \sqrt { 2 } \tau _ { 2 } ) = 0 .
$$

By Bernstein’s inequality, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $k \in [ K ] \setminus \widehat { \mathcal { K } }$ ,

$$
\mathbb { E } _ { \mu ^ { * } } [ \rho _ { [ k ] } ( X , Y ) ] \lesssim \sqrt { \frac { \log n } { n } } .
$$

Therefore it holds with probability at least $\textstyle 1 - { \frac { 2 } { n ^ { 2 } } }$ that for any $\begin{array} { r } { 1 \leq \gamma \leq \frac { \left( d _ { Y } \vee ( \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } ) \right) \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$

$$
\begin{array} { r l } & { E _ { B } ) \lesssim \sqrt { \displaystyle \frac { \log n } { n } } + \mathbb { E } _ { \mu ^ { * } } \Big [ \displaystyle \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \times } ( \mathbb { R } ^ { N } ) } \Big | \sum _ { k \in \tilde { \mathcal { K } } } \rho _ { [ k ] } ( X , Y ) \big ( f _ { f } ^ { \perp } ( Y ) - f _ { \mathcal { I } } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) ) \big ) \big ] \Big | \Big ] } \\ & { \lesssim \sqrt { \displaystyle \frac { \log n } { n } } + ( \log n ) \cdot 2 ^ { - J ( \gamma - 1 ) } \sum _ { k \in \tilde { \mathcal { K } } } \mathbb { E } _ { \mu ^ { * } } \big [ \rho _ { [ k ] } ( X , Y ) \big \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \big \| \big ] + n ^ { - \frac { 7 } { \frac { \sqrt { \gamma } } { \beta _ { Y } } + \frac { d \chi } { \beta _ { X } } } } + n ^ { - \frac { 7 } { \sqrt { \gamma } } } } \\ & { \lesssim ( \log n ) ^ { 2 } \cdot ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \gamma - 1 } { 2 \alpha _ { Y } + d _ { X } + d _ { X } } \frac { \sqrt { \gamma } } { \alpha _ { X } } - \frac { 1 } { \frac { d _ { Y } } { \sqrt { \gamma } } + \frac { d \chi } { \beta _ { X } } } } + \displaystyle \frac { ( \log n ) ^ { 3 } } { \sqrt { n } } + n ^ { - \frac { 7 } { \frac { d _ { Y } } { \sqrt { \gamma } } + \frac { d \chi } { \beta _ { X } } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } } \\ &  \lesssim ( \log n ) ^ { 3 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + ( \log n \end{array}
$$

where the last inequality uses $\beta _ { Y } \geq \alpha _ { Y } + 1$ and $\begin{array} { r } { \beta _ { X } \ge \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ . Similarly, we can get when $\gamma \leq 1$ ,

$$
\begin{array} { r l } & { \big ( E _ { B } \big ) \lesssim \sqrt { \displaystyle \frac { \log n } { n } } + \mathbb { E } _ { \mu _ { x } ^ { * } } \Big [ \int _ { f \in \mathcal { H } _ { 1 } ^ { \star } ( \mathbb { R } ^ { D } \gamma ) } \Big | \sum _ { k \in \widehat { \mathbb { R } } } \rho _ { [ k ] } ( x , y ) \big ( f _ { J } ^ { 1 } ( y ) - f _ { J } ^ { 1 } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) ) \big ) \big ] \Big | } \\ & { \lesssim n ^ { - \frac { \gamma } { \mu _ { Y } ^ { * } + \frac { \widehat { d } \lambda } { \gamma } } } + n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d \chi } } + ( \log n ) \cdot \sum _ { k \in \widehat { \mathbb { R } } } \mathbb { E } _ { \mu ^ { * } } \big [ \rho _ { [ k ] } ( X , Y ) \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| \big ] } \\ & { \quad + \left. ( n ^ { \frac { ( \gamma _ { 1 } - \gamma ) } { \mu _ { Y } ^ { * } + \frac { d } { \mu _ { X } } } } \wedge { \frac { \alpha _ { X } ( \gamma _ { 1 } / \gamma - 1 ) } { n ^ { \frac { \gamma } { 2 } \alpha _ { X } + d \chi } } } \right) \sum _ { k \in \widehat { \mathbb { R } } } \big [ \rho _ { [ k ] } ( X , Y ) \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { n } \big ] } \\ & { \lesssim ( \log n ) \cdot n ^ { - \frac { \gamma } { \mu _ { Y } ^ { * } } + \frac { d } { \gamma \alpha _ { X } } } + ( \log n ) ^ { 2 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d \chi } } + \frac { ( \log n ) ^ { 3 } } { \sqrt { n } } , } \end{array}
$$

where the last inequality uses that for any $\begin{array} { r } { \gamma _ { 1 } = ( \frac { 2 \alpha _ { X } + d _ { X } } { 2 \alpha _ { X } } \gamma ) \wedge 1 } \end{array}$

$$
\begin{array} { r l } & { \quad \frac { \frac { \left( \eta _ { 1 } - \gamma \right) } { \sqrt { \gamma } } } { \mu } _ { Y } + \frac { \lambda } { \beta _ { X } } \wedge n ^ { \frac { \alpha _ { X } ( \gamma _ { 1 } / \gamma - 1 ) } { 2 \alpha _ { X } + d _ { X } } } ) \sum _ { k \in \mathbb { R } } \mathbb { E } _ { \mu ^ { * } } \left[ \rho _ { [ k ] } ( X , Y ) \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \right] } \\ & { \quad \times ( n ^ { \frac { \gamma _ { 1 } - \gamma } { \beta _ { Y } + \frac { d _ { X } ^ { \gamma } } { \beta _ { X } } } } \wedge n ^ { \frac { \alpha _ { X } ( \gamma _ { 1 } / \gamma - 1 ) } { 2 \alpha _ { X } + d _ { X } } } ) \cdot ( n ^ { - \frac { \gamma _ { 1 } } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } + \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } ) } \\ & { \quad \lesssim n ^ { \frac { \gamma _ { 1 } - \frac { \gamma } { \beta _ { Y } } } { \beta _ { Y } + \frac { d _ { X } } { \beta _ { X } } } } + \frac { \left( \log n \right) ^ { 2 } } { \sqrt { n } } n ^ { \frac { \alpha _ { X } ( \frac { 2 \alpha _ { X } + d _ { X - 1 } } { 2 \alpha _ { X } + d _ { X } } ) } { 2 \alpha _ { X } + d _ { X } } } } \\ &  \quad \lesssim n ^ { - \frac { \gamma _ { 1 } - \frac { \gamma } { \beta _ { Y } } } { \beta _ { Y } + \frac { d _ { X } } { \beta _ { X } } } } + \frac { \left( \log n \right) ^ { 2 } } { \sqrt { n } } n ^  \frac { \alpha _ { X } ( \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } - 1 ) }  2 \end{array}
$$

When $\begin{array} { r } { \gamma \geq \eta = \frac { \left( d _ { Y } \vee ( \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } ) \right) \alpha _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ , we have

$$
\begin{array} { r l } & { ( E _ { B } ) \lesssim \sqrt { \frac { \log n } { n } } + \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \eta } ( \mathbb { R } ^ { D } Y ) } { \operatorname* { s u p } } \Big | \sum _ { k \in \widehat { \mathcal { K } } } \rho _ { [ k ] } ( x , y ) \big ( f _ { J } ^ { \perp } ( y ) - f _ { J } ^ { \perp } ( \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( y ) , x ) ) \big ) \big ] \Big | \Big ] } \\ & { \quad \lesssim ( \log n ) ^ { 3 } n ^ { - \frac { \alpha X } { 2 \alpha _ { X } + d _ { X } } } . } \end{array}
$$

Finally, we bound term $\left( E _ { C } \right)$ . Given the second statement in Lemma 15, we can use Lemma 4 in dix Aand ertibility of , there exist $\widehat { V } _ { [ k ] } ^ { T } ( \cdot - y _ { k } )$ ecificalso that $\tau _ { 2 }$ $k \in { \widehat { K } }$ $x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } )$ $\widehat { U } _ { Y | x } ^ { [ k ] }$ $\mathbb { B } _ { \mathcal { M } _ { Y \vert x } } ( y _ { k } ^ { * } , 3 \tau _ { 2 } ) \subset \widehat { U } _ { Y \vert x } ^ { [ k ] } \subset \mathcal { M } _ { Y \vert x } .$ and the function $\widehat { Q } _ { [ k ] } ( \cdot ) = \widehat { V } _ { [ k ] } ^ { T } ( \cdot - y _ { k } )$ , when restricted to domain ${ \widehat { U } } _ { Y \mid x } ^ { [ k ] }$ , is a diffeomorphism that maps ${ \widehat { U } } _ { Y \mid x } ^ { [ k ] }$ to $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } )$ with inverse denoted as $[ \widehat { Q } _ { [ k ] } ( \cdot , x ) ] ^ { - 1 }$ . The function $\widehat { G } _ { [ k ] } ^ { \dag }$ : $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } )  \mathbb { R } ^ { D _ { Y } }$ defined as $\widehat { G } _ { [ k ] } ^ { \dagger } ( z , x ) = [ \widehat { Q } _ { [ k ] } ( \cdot , x ) ] ^ { - 1 } ( z )$ belongs to $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } )$ b[k] b ). Then by Lemma 5, the push forward measure $\widehat { Q } _ { [ k ] \# } ( \mu _ { Y | x } ^ { * } | _ { \widehat { U } _ { Y | x } ^ { [ k ] } } )$ has a density $\widehat { \nu } _ { [ k ] } ( z , | , x ) \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } \bigl ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } \bigr ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } ) \bigr )$ for some constant $L _ { 1 }$ . Furthermore, for any $j \in \mathbb N$ and $\psi \in \Psi _ { j } ^ { d _ { Y } }$ , we have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] } \\ & { \ = \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) \mathbf { 1 } ( Y \in \widehat { U } _ { Y | x } ^ { [ k ] } ) \mathbf { 1 } ( x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { k } ^ { * } , 2 \tau _ { 2 } ) ) ] } \\ & { \ = \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , \widehat { G } _ { [ k ] } ^ { \dagger } ( \widehat { Q } _ { [ k ] } ( Y ) , x ) ) \mathbf { 1 } ( Y \in \widehat { U } _ { Y | x } ^ { [ k ] } ) ] } \\ & { \ = \displaystyle \int _ { \mathbb { B } _ { \mathbb { Z } } d _ { Y } ( \widehat { V } _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) } \psi ( z ) \rho _ { [ k ] } ( x , \widehat { G } _ { [ k ] } ^ { \dagger } ( z , x ) ) \widehat { v } _ { [ k ] } ( z | x ) \mathrm { d } z . } \end{array}
$$

Let $\overline { { \nu } } _ { [ k ] } ( z , | , x ) \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $\widehat { \nu } _ { [ k ] } ( z , | , x )$ to $\mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } }$ . Then we define a function $\widetilde { v } _ { [ k ] } : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R }$ :

$$
\widetilde v _ { [ k ] } ( z , x ) = \left\{ \begin{array} { c c } { \rho _ { [ k ] } ( x , \widehat G _ { [ k ] } ^ { \dagger } ( z , x ) ) \overline { { \nu } } _ { [ k ] } ( z | x ) , } & { \mathrm { i f } z \in \mathbb { B } _ { \mathbb { R } ^ { d } Y } ( \widehat V _ { [ k ] } ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , 3 \tau _ { 2 } ) , x \in \mathbb { B } _ { \mathbb { R } ^ { p _ { X } } } ( x _ { k } ^ { * } , 3 \tau _ { 2 } ) } \\ { 0 } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

We can verify that $\widetilde { v } _ { [ k ] } ( z , x ) \in \mathcal { \overline { { H } } } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ for some constant $L _ { 2 }$ . So for any $j \in \mathbb N$ , $\psi \in \Psi _ { j } ^ { d _ { Y } }$ and $x \in \mathcal { M } _ { X }$ ,

$$
2 ^ { \frac { d _ { Y } j } { 2 } } \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] = 2 ^ { \frac { d _ { Y } j } { 2 } } \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | x ) \mathrm { d } z ,
$$

and $\begin{array} { r } { 2 ^ { \frac { d _ { Y } j } { 2 } } \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | \cdot ) \mathrm { d } z \in \mathcal { H } _ { L _ { 3 } } ^ { \alpha _ { X } } ( \mathbb { R } ^ { D _ { X } } ) } \end{array}$ for some constant $L _ { 3 }$ . Moreover, for any $x \in \mathcal { M } _ { X }$ , since $\widetilde { v } _ { [ k ] } ( \cdot | x ) \in \mathcal { H } _ { L _ { 4 } } ^ { \alpha _ { Y } } ( \mathbb { R } ^ { d _ { Y } } )$ , it holds that

$$
\left| \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( x , Y ) ] \right| = \Big | \int _ { \mathbb { R } ^ { d _ { Y } } } \psi ( z ) \widetilde { v } _ { [ k ] } ( z | x ) \mathrm { d } z \Big | \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } - j \alpha _ { Y } } .
$$

Let $\begin{array} { r } { J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) \rceil } \end{array}$ . For $j \in \{ 0 \} \cup [ J ]$ , denote

$$
\mathbf { \Psi } _ { j } ^ { \sharp } = \{ S : \Psi _ { j } ^ { d _ { Y } } \times \mathbb { R } ^ { D x } \to \mathbb { R } : S ( \psi , x ) = \sum _ { \psi _ { 1 } \in \Psi _ { j } ^ { d _ { Y } } } s _ { \psi _ { 1 } } ( x ) , \mathrm { ~ w h e r e ~ } s _ { \psi _ { 1 } } \in \mathcal { S } _ { j } \mathrm { ~ f o r ~ e a c h ~ } \psi _ { 1 } \in \Psi _ { j } ^ { d _ { Y } } \} ,
$$

where ${ \mathcal { S } } _ { j }$ is defined in (19). Using the independence of $\{ X _ { i } \} _ { i \in I _ { 1 } }$ and $\{ X _ { i } \} _ { i \in I _ { 2 } }$ , and mirroring the analysis from the proof of Lemma 9—where we replace $D _ { Y }$ with $d _ { Y }$ , and modify $\psi ( Y )$ to $\psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y )$ To apply Theorem 8, we set $\{ \psi _ { \lambda } ( ( X , Y ) ) \} _ { \lambda \in \Lambda } = \{ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) : \ \psi \in \Psi _ { j } ^ { d _ { Y } } \}$ , where the response variable $Y$ is redefined as the joint vector of $( X , Y )$ , alongside $\boldsymbol { S } = \boldsymbol { S } _ { j } ^ { \ddag }$ — we can show that, by applying a union argument over $j \in [ J ]$ and $k \in { \widehat { \mathcal { K } } }$ , it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ and $k \in { \widehat { \mathcal { K } } }$ ,

$$
\mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } ( \widehat { v } _ { k \psi } ( X ) - \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \psi ( \widehat { Q } _ { [ k ] } ( Y ) ) \rho _ { [ k ] } ( X , Y ) ] ) ^ { 2 } \Big ] \lesssim 2 ^ { \frac { 2 j \alpha _ { X } d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } ( \frac { n } { \log n } ) ^ { - \frac { 2 \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } .
$$

Thus, employing a similar strategy to that used in Regime 2, we can demonstrate that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $\gamma > 0$ ,

$$
\begin{array} { r l } &  \qquad - \underbrace  \sum _ { k = 1 } ^ { n } \frac { 1 } { 2 } \delta \alpha \delta _ { k + 1 , k } \sum _ { p = 1 } ^ { n } \sum _ { \ell = 1 } ^ { n } \frac { 1 } { \ 2 } \sum _ { \ell = 1 } ^ { n } \frac { 1 }  \gamma \delta _ { k } \alpha \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _ { p } \delta _  p \end{array}
$$

By combining the bounds for term $( E _ { A } ) , ( E _ { B } ) , ( E _ { C } )$ , we can then get the desired results.

# D.4 Proof of Theorem 2 (minimax lower bound for Regime 2)

The upper bound is established by Theorem 6 and Corollary 1; hence, our focus here is on establishing the lower bound. The term $n ^ { - \frac { \beta _ { Y } \dot { \gamma } } { d _ { Y } } }$ in the lower bound is directly derived from the minimax lower bound for the unconditional case as specified in Theorem 3.1 of Tang and Yang [2023a]. Moreover, the lower bound for $d _ { X } = 0$ also follows directly from the minimax rate in the unconditional case. Consequently, our analysis will concentrate on the terms $n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } }$ and − 2αY +dY + αYαX dX for dX ∈ N+. Define the covariate space $\mathcal { M } _ { X } = [ - 1 , 1 ] ^ { d _ { X } } \times \mathbf { 0 } _ { D _ { X } - d _ { X } }$ , with $\mu _ { X } ^ { * }$ representing the uniform distribution over $\mathcal { M } _ { X }$ . Let $\mathcal { M } _ { 0 } = \mathbb { S } _ { 2 } ^ { d _ { Y } } \times \mathbf { 0 } _ { D _ { Y } - d _ { Y } - 1 } = \{ y \in \mathbb { R } ^ { D _ { Y } } : \| y _ { 1 : d _ { Y } + 1 } \| ^ { 2 } = 2 .$ $y _ { d _ { Y } + 2 : D _ { Y } } = { \bf 0 } _ { D _ { Y } - d _ { Y } - 1 } \}$ denote the $d _ { Y }$ -dimensional sphere embedded in $\mathbb { R } ^ { D _ { Y } }$ and let $\tilde { \mathcal { M } } _ { 0 } = \{ y \in \mathbb { R } ^ { D _ { Y } } : y _ { 1 : d _ { Y } } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ , $y _ { d + 1 } =$ $\sqrt { 2 - \| y _ { 1 : d _ { Y } } \| ^ { 2 } }$ , $y _ { d _ { Y } + 2 : D _ { Y } } = \mathbf { 0 } _ { D _ { Y } - d _ { Y } - 1 } \}$ denote the middle area of $\mathcal { M } _ { 0 }$ . Then $\widetilde { \mathcal { M } } _ { 0 }$ admits a global parametrization $G _ { 0 } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )  \widetilde { \mathcal { M } } _ { 0 }$ defined as $G _ { 0 } ( z ) = ( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , { \bf 0 } _ { D _ { Y } - d _ { Y } - 1 }$ for $z \in$ $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ . So we can define $\nu _ { 0 }$ as the density function on $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ so that $[ G _ { 0 } ] _ { \# } \nu _ { 0 }$ is the normalized restriction of $\mu _ { 0 }$ on $\widetilde { \mathcal { M } _ { 0 } }$ , or

$$
\nu _ { 0 } ( z ) = \frac { 1 } { \widetilde { C } } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } , \quad \forall z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) ,
$$

where $\mathbf { J } _ { G _ { 0 } }$ denotes the Jacobian matrix of $G _ { 0 }$ and $\begin{array} { r } { \widetilde { C } = \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } \mathrm { d } z } \end{array}$ is the normalizing constant. Let $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ be a conditional density function class of $z | x$ indexed by a parameter $\omega$ , so that for any $\nu _ { \omega } ( z , x ) \in \Psi _ { \alpha _ { Y } , \alpha _ { X } }$ and $x \in \mathcal { M } _ { X }$ , $\nu _ { \omega } ( z , x ) = \nu _ { 0 } ( z )$ if $z \not \in { \mathbb { B } } _ { { \mathbb { R } } ^ { d _ { Y } } } ( { \mathbf { 0 } } , 3 / 4 )$ . Then for any $\nu _ { \omega } ( z , x ) \in \Psi _ { \alpha _ { Y } , \alpha _ { X } }$ and $x \in \mathcal { M } _ { X }$ , we define the following distribution over $\mathcal { M } _ { 0 }$ as

$$
\mu _ { Y | x } ^ { \omega } = \Big ( 1 - \frac { \widetilde { C } } { C } \Big ) \cdot \mu _ { 1 } + \frac { \widetilde { C } } { C } \cdot [ G _ { 0 } ] _ { \# } [ \nu _ { \omega } ( z , x ) \mathrm { d } z ] ,
$$

where $\mu _ { 1 }$ represents the uniform distribution over $\widetilde { \mathcal { M } } _ { 1 } = \mathcal { M } _ { 0 } \setminus \widetilde { \mathcal { M } } _ { 0 }$ . and $C$ is the surface area of $\mathbb { S } _ { 2 } ^ { d _ { Y } }$ Then $\mu _ { Y \mid x } ^ { \omega }$ has the following conditional density function with respect to the volume measure of $\mathcal { M } _ { 0 }$ ,

$$
\begin{array} { l } { { \displaystyle \omega ^ { \omega } ( y | x ) = \frac { 1 } { C } { \bf 1 } ( y \in \widetilde { \mathcal { M } } _ { 1 } ) + \frac { \widetilde { C } } { C } \cdot \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } } , x ) } { \sqrt { \operatorname* { d e t } ( { \bf J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { T } { \bf J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ) } } \cdot { \bf 1 } ( y \in \widetilde { \mathcal { M } } _ { 0 } ) , \forall y \in \mathcal { M } _ { 0 } } } \\ { { \displaystyle \ = \{ \begin{array} { l c } { { \displaystyle \widetilde { C } \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } , x } ) } { \sqrt { \operatorname* { d e t } ( { \bf J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { T } { \bf J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ) } } , ~ y \in \widetilde { \mathcal { M } } _ { 0 } = \{ y = ( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , { \bf 0 } _ { D _ { Y } - d _ { Y } - 1 } ) ~ : } } } \\ { { \displaystyle \qquad \frac { 1 } { C } , ~ } } \\ { { \displaystyle \sqrt { \operatorname* { d e t } ( { \bf J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { \tau , x } ) } } , ~ y \in \{ y = ( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , { \bf 0 } _ { D _ { Y } - d _ { Y } - 1 } ) ~ : } } \end{array}    \\   \displaystyle \ = \{ \begin{array} { l c } { { \displaystyle \widetilde { C } \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } , x } ) } { C } , ~ } } \\   \displaystyle \widetilde { C } \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } , x } ) }  \sqrt  \operatorname* { d e t } ( { \bf J } _  G _ { 0 }  \end{array} \end{array}
$$

Moreover, we have

$$
\begin{array} { r l } & { d _ { \gamma } ( \mu _ { Y | x } ^ { \omega } , \mu _ { Y | x } ^ { \omega ^ { \prime } } ) = \overset { \widetilde { C } } { \underset { C } { \longrightarrow } } \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } f ( G _ { 0 } ( z ) ) ( \nu _ { \omega } ( z , x ) - \nu _ { \omega ^ { \prime } } ( z , x ) ) \mathrm { d } z } \\ & { \geq \overset { \widetilde { C } } { \underset { C } { \longrightarrow } } \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { d _ { Y } } ) } { \operatorname* { s u p } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } f ( z ) ( \nu _ { \omega } ( z , x ) - \nu _ { \omega ^ { \prime } } ( z , x ) ) \mathrm { d } z , } \end{array}
$$

and

$$
D _ { \mathrm { K L } } ( \mu _ { Y | x } ^ { \omega } , \mu _ { Y | x } ^ { \omega ^ { \prime } } ) = \frac { \widetilde { C } } { C } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } - \log \frac { \nu _ { \omega ^ { \prime } } ( z , x ) } { \nu _ { \omega } ( z , x ) } \nu _ { \omega } ( z , x ) \mathrm { d } z .
$$

Therefore, selecting

$$
\begin{array} { l } { { \Psi _ { \alpha _ { Y } , \alpha _ { X } } = \Bigl \{ \nu _ { \omega } ( z , x ) = \nu _ { 0 } ( z ) + \biggl ( \frac { 1 } { \widetilde { m _ { 1 } } } \biggr ) ^ { \alpha _ { Y } } \displaystyle \sum _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { D _ { Y } } } \displaystyle \sum _ { \xi _ { 2 } \in [ \widetilde { m } ] ^ { d _ { Y } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( z , x ) } } \\ { { : \quad \omega = \{ \omega _ { \xi _ { 1 } , \xi _ { 2 } } \} _ { \xi _ { 1 } \in [ \widetilde { m } _ { 1 } ] ^ { d _ { Y } } , \xi _ { 2 } \in [ \widetilde { m } _ { 2 } ] ^ { d _ { X } } } \in \{ 0 , 1 \} ^ { \widetilde { m } _ { 1 } ^ { d _ { Y } } \times \widetilde { m } _ { 2 } ^ { d _ { X } } } \Bigr \} , } } \\ { { \widetilde { m } _ { 1 } = \big \lceil b n ^ { \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } } \big \rceil , \quad \widetilde { m } _ { 2 } = \big \lceil b n ^ { \frac { 1 } { 2 \alpha _ { X } + d _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } d _ { Y } } } \big \rceil , } } \end{array}
$$

where

$$
\widetilde { \psi } _ { \xi _ { 1 } , \xi _ { 2 } } ( y , x ) = \prod _ { i = 1 } ^ { d _ { Y } } \widetilde { k } \Big ( \widetilde { m } _ { 1 } \sqrt { \frac { d _ { Y } } { 2 } } y _ { i } + \frac { \widetilde { m } _ { 1 } } { 2 } - \xi _ { 1 i } \Big ) \prod _ { i = 1 } ^ { d _ { X } } \widetilde { k } \Big ( \widetilde { m } _ { 2 } \sqrt { 2 d _ { X } } x _ { i } - \xi _ { 2 i } \Big ) , \quad \forall y \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) ,
$$

and

$$
\widetilde { k } ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \alpha _ { Y } \vee \alpha _ { X } \vee \gamma + 1 } t ^ { \alpha _ { Y } \vee \alpha _ { X } \vee \gamma + 1 } ( t - \frac { 1 } { 2 } ) , \quad t \in ( 0 , 1 ) } \\ { 0 , \quad \mathbf { o . w . } } \end{array} \right.
$$

We can verify that there exists a constant $L$ so that for any $\nu _ { \omega } \in \Psi _ { \alpha _ { Y } , \alpha _ { X } }$ , the function $\overline { { \mu } } ^ { \omega } : \mathbb { R } ^ { D _ { Y } } \times \mathbb { \Lambda }$ $\mathbb { R } ^ { D _ { X } }  \mathbb { R }$ defined by

$$
\begin{array} { r l } & { \overline { { \mu } } ^ { \omega } ( y , x ) = \left\{ \begin{array} { c c } { \frac { \widetilde { C } } { C } \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } } , x ) } { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ) } } , } & { \quad \| y _ { 1 : d _ { Y } } \| \leq 1 } \\ { \frac { 1 } { C } , } & { \quad \| y _ { 1 : d _ { Y } } \| > 1 } \end{array} \right. } \\ & { \quad \quad = \left\{ \begin{array} { c c } { \frac { \widetilde { C } } { C } \frac { \nu _ { \omega } ( y _ { 1 : d _ { Y } } , x ) } { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ) } } , } & { \quad \| y _ { 1 : d _ { Y } } \| \leq 3 / 4 } \\ { \frac { 1 } { C } , } & { \quad \| y _ { 1 : d _ { Y } } \| > 3 / 4 . } \end{array} \right. } \end{array}
$$

satisfies that $\overline { { \mu } } ^ { \omega } \in \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ , and $\overline { { \mu } } ^ { \omega } ( y , x ) = \mu ^ { \omega } ( y | x )$ holds for any $y \in \mathcal { M } _ { 0 }$ and $x \in \mathcal { M } _ { X }$ Therefore, let $g ( \cdot ) \equiv 1$ , for any $\beta _ { Y } > 0$ , there exist constants $\tau , \tau _ { 1 } , L$ so that

$$
\begin{array} { r l } & { \left. \mu = \mu _ { X } ^ { \ast } \mu _ { Y | x } : \mu _ { Y | x } = \left( 1 - \frac { \widetilde { C } } { C } \right) \cdot \mu _ { 1 } + \frac { \widetilde { C } } { C } \cdot [ G _ { 0 } ] _ { \# } [ \nu ( z , x ) \mathrm { d } z ] , \quad \nu \in \Psi _ { \alpha _ { Y } , \alpha _ { X } } \right. } \\ & { \subset \mathcal { P } _ { 2 } ^ { \ast } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { Y } , \alpha _ { Y } , \alpha _ { X } , \tau , \tau _ { 1 } , g , L ) . } \end{array}
$$

Following the same procedure as in the proof of Theorem 1 (see Appendix C.2), we can then get the desired lower bound of − 2αY +dY + αYαX dX . Similarly, to attain the desired lower bound of n− αX2αX +dX , we can follow the same step as in the proof of Theorem 1, but this time opting for $\Psi _ { \alpha _ { Y } , \alpha _ { X } }$ as

$$
\begin{array} { r l r } { \boldsymbol { \mathfrak { f } } _ { \alpha \gamma , \alpha _ { X } } = \Psi _ { \alpha _ { X } } = \Big \{ \nu _ { \omega } ( y , x ) = \nu _ { 0 } ( y ) + \Big ( \frac { 1 } { \widetilde { m } } \Big ) ^ { \alpha _ { X } } \displaystyle \sum _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \omega _ { \xi } \widetilde { \psi } _ { \xi } ( x ) \prod _ { i = 1 } ^ { d _ { Y } } \widetilde { k } ( y _ { i } ) : \omega = \{ \omega _ { \xi } \} _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \displaystyle \sum _ { i = 1 } ^ { d _ { Y } } \widetilde { k } ( y _ { i } ) : \omega = \{ \omega _ { \xi } \} _ { \xi \in [ \widetilde { m } ] ^ { d _ { X } } } \Big \} } & \\ { \widetilde { m } = \big \lceil b n ^ { \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } \big \rceil , \quad \widetilde { \psi } _ { \xi } ( x ) = \displaystyle \prod _ { i = 1 } ^ { d _ { X } } \widetilde { k } \Big ( \widetilde { m } \sqrt { 2 d _ { X } } x _ { i } - \xi _ { i } \Big ) . } & \end{array}
$$

# D.5 Proof of Theorem 4 (minimax lower bound for Regime 3b)

The upper bound is established by Theorem 6 and Corollary 2, so our focus here is solely on the lower bound. The lower bound of $n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + n ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } }$ 2αY +dY + αYαX dX can be directly derived from the proof of the lower bound in Theorem 2 (see Appendix D.4). So the remaining task is to show the lower bound of

$\overset { } { \underset { n } { - } } \frac { \overset { \gamma } { d _ { Y } } } { \overset { d _ { X } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } }$ . Notice that when $\gamma > 1$ , we can observe that

$$
\begin{array} { r l } & { \frac { \gamma } { \frac { d \gamma } { \beta \gamma } + \frac { d _ { X } } { \beta _ { X } } } = \frac { \gamma \left( \alpha _ { Y } + 1 \right) } { \frac { d \gamma \left( \alpha _ { Y } + 1 \right) } { \beta \gamma } + \frac { d _ { X } \left( \alpha _ { Y } + 1 \right) } { \beta _ { X } } } } \\ & { > \frac { \alpha _ { Y } + \gamma } { \frac { d _ { Y } \left( \alpha _ { Y } + 1 \right) } { \beta \gamma } + \frac { d _ { X } \left( \alpha _ { Y } + 1 \right) } { \beta _ { X } } } \qquad ( \gamma > 1 ) } \\ & { \geq \frac { \alpha _ { Y } + \gamma } { d _ { Y } + \frac { d _ { X } \alpha _ { Y } } { \alpha _ { X } } } \quad \quad \left( \beta _ { Y } \geq \alpha _ { Y } + 1 \quad \beta _ { X } \geq \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } \right) } \\ & { > \frac { \alpha _ { Y } } { 2 \alpha _ { Y } + d _ { Y } + \frac { d _ { X } \alpha _ { Y } } { \alpha _ { X } } } . } \end{array}
$$

Hence, the term $\overset { } { \underset { n } { - } } \frac { \overset { \gamma } { d _ { Y } } } { \overset { d _ { X } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } }$ will be dominated by $n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } + n ^ { - \frac { \alpha _ { Y } + \gamma } { 2 \alpha _ { Y } + d _ { Y } + \frac { \alpha _ { Y } } { \alpha _ { X } } d _ { X } } }$ . So here we only focus on the scenario where $\gamma \leq 1$ . Define the covariate space $\mathcal { M } _ { X } = [ - 1 , 1 ] ^ { d _ { X } } \times 0 _ { D _ { X } - d _ { X } }$ and let $\mu _ { X } ^ { * }$ be the uniform distribution over $\mathcal { M } _ { X }$ . Then any $x \in \mathcal { M } _ { X }$ can be expressed as a $d _ { X }$ -dimensional vector by removing the last $D _ { X } - d _ { X }$ element. So in the following, we write $x = \left( x _ { 1 } , x _ { 2 } , \cdots , x _ { d } \right)$ when no ambiguity may arise. Let $\mathcal { M } _ { 0 } = \mathbb { S } _ { 2 } ^ { d _ { Y } } \times { \mathbf { 0 } } _ { D _ { Y } - d _ { Y } - 1 } = \{ y \in \mathbb { R } ^ { D _ { Y } } : \lVert y _ { 1 : d _ { Y } + 1 } \rVert ^ { 2 } = 2$ , $y _ { d _ { Y } + 2 : D _ { Y } } = 0 _ { D _ { Y } - d _ { Y } - 1 } \}$ denote the $d _ { Y }$ -dimensional sphere embedded in $\mathbb { R } ^ { D _ { Y } }$ , with $\mu _ { 0 }$ representing the uniform distribution over $\mathcal { M } _ { 0 }$ . Let $\widetilde { \mathcal { M } } _ { 0 } = \{ y \in \mathbb { R } ^ { D _ { Y } } : y _ { 1 : d _ { Y } } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ , $y _ { d + 1 } = \sqrt { 2 - \| y _ { 1 : d _ { Y } } \| ^ { 2 } }$ , $y _ { d _ { Y } + 2 : D _ { Y } } = 0 _ { D _ { Y } - d _ { Y } - 1 } \}$ denote the middle area of $\mathcal { M } _ { 0 }$ . Then $\widetilde { \mathcal { M } } _ { 0 }$ admits a global parametrization $G _ { 0 } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )  \widetilde { \mathcal { M } } _ { 0 }$ defined as $G _ { 0 } ( z ) = ( z , \sqrt { 2 - \| z \| _ { 2 } ^ { 2 } } , \mathbf { 0 } _ { D _ { Y } - d _ { Y } - 1 } )$ for $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ . So we can define $\nu _ { 0 }$ as the density function on $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ so that $[ G _ { 0 } ] _ { \# } \nu _ { 0 }$ is the normalized restriction of $\mu _ { 0 }$ on $\widetilde { \mathcal { M } } _ { 0 }$ , or

$$
\nu _ { 0 } ( z ) = \frac { 1 } { \widetilde { C } } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } , \quad \forall z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) ,
$$

where $\mathbf { J } _ { G _ { 0 } }$ denotes the Jacobian matrix of $G _ { 0 }$ and $\begin{array} { r } { \widetilde { C } = \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) ) } \mathrm { d } z } \end{array}$ is the normalizing constant. Moreover, there exist positive constants $c _ { 1 } , c _ { 2 }$ so that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ , $c _ { 1 } I _ { d } \prec \mathbf { J } _ { G _ { 0 } } ( z ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( z ) \prec c _ { 2 } I _ { d }$ . Next we will add small bumps to function $G _ { 0 }$ to construct perturbations of $\widetilde { \mathcal { M } } _ { 0 }$ , whose unions with the spherical cap $\widetilde { \mathcal { M } } _ { 1 } : = \mathcal { M } _ { 0 } \backslash \widetilde { \mathcal { M } } _ { 0 }$ form our constructed perturbed $x$ - dependent manifolds.

Let $m _ { 1 } = { \lceil { b n } ^ { \frac { 1 } { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } } } \rceil }$ 1 and $m _ { 2 } = { \lceil { b n } ^ { \frac { 1 } { d _ { X } + d _ { Y } \frac { \beta _ { X } } { \beta _ { Y } } } } \rceil }$ , where $b$ is a large enough constant. Then consider a bump function

$$
\begin{array} { r } { k ( t ) = \left\{ \begin{array} { l l } { ( 1 - t ) ^ { \beta _ { Y } + 1 } t ^ { \beta _ { Y } + 1 } , \quad t \in ( 0 , 1 ) , } \\ { 0 , \quad \mathrm { ~ o . w . } } \end{array} \right. } \end{array}
$$

$$
\xi _ { 1 } = ( \xi _ { 1 1 } , \xi _ { 1 2 } , \cdot \cdot \cdot , \xi _ { 1 d _ { Y } } ) \in [ \widetilde m _ { 1 } ] ^ { d _ { Y } } , \xi _ { 2 } = ( \xi _ { 2 1 } , \xi _ { 2 2 } , \cdot \cdot \cdot , \xi _ { 2 d _ { X } } ) \in [ \widetilde m _ { 2 } ] ^ { d _ { X } } ,
$$

$$
\psi _ { \xi _ { 1 } , \xi _ { 2 } } ( z , x ) = \prod _ { i = 1 } ^ { d _ { Y } } k \Big ( m _ { 1 } \sqrt { \frac { d _ { Y } } { 2 } } z _ { i } + \frac { m _ { 1 } } { 2 } - \xi _ { 1 i } \Big ) \prod _ { i = 1 } ^ { d _ { X } } k \Big ( m _ { 2 } \sqrt { \frac { d _ { X } } { 2 } } x _ { i } + \frac { m _ { 2 } } { 2 } - \xi _ { 2 i } \Big ) .
$$

For any $\omega = ( \omega _ { \xi _ { 1 } , \xi _ { 2 } } ) _ { \{ \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { Y } } , \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { X } } \} } \in \{ 0 , 1 \} ^ { m _ { 1 } ^ { d _ { Y } } \times m _ { 2 } ^ { d _ { X } } }$ , we define the multi-bump function

$$
g _ { \omega } ( z , x ) = \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { Y } } , \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { X } } } \frac { 1 } { m _ { 1 } ^ { \beta _ { Y } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \psi _ { \xi _ { 1 } , \xi _ { 2 } } ( z , x ) ,
$$

whose bumps correspond to the non-zero components of $\omega$ . Finally, we define $G _ { \omega } ( z , x ) = G _ { 0 } ( z ) +$ $( { \bf 0 } _ { d _ { Y } } , g _ { \omega } ( z , x ) , { \bf 0 } _ { D _ { Y } - d _ { Y } - 1 } )$ as the perturbed $x$ -dependent generative map parametrized by the binary

teto $\omega$ straightforward to verify that there exists a constant . Furthermore, by Lemma F.3 in Tang and Yang [20 $L$ 3 $G _ { \omega }$   
$\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbf { \bar { \mathbb { B } } } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) , \mathcal { M } _ { X } )$ $\{ \omega ^ { ( 1 ) } , \cdot \cdot \cdot , \omega ^ { ( H _ { 0 } ) } \} \subset$   
$\{ 0 , 1 \} ^ { m _ { 1 } ^ { d _ { Y } } \times m _ { 2 } ^ { d _ { X } } }$ such that:   
$\begin{array} { r } { 1 . \ \log H _ { 0 } \geq \frac { m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 8 } - \log 2 ; } \end{array}$   
2. for any $j , k \in [ H _ { 0 } ]$ with $j \neq k$ , the Hamming distance $\| \boldsymbol { \omega } ^ { ( j ) } - \boldsymbol { \omega } ^ { ( k ) } \| _ { \mathrm { H } }$ between $\boldsymbol { \omega } ^ { ( j ) }$ and $\boldsymbol { \omega } ^ { ( k ) }$ satisfies $\begin{array} { r } { \frac { m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 4 } \leq \| \omega ^ { ( j ) } - \omega ^ { ( k ) } \| _ { \mathrm { H } } \leq \frac { 3 m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 4 } . } \end{array}$

For each $\omega \in \{ 0 , 1 \} ^ { m _ { 1 } ^ { d _ { Y } } \times m _ { 2 } ^ { d _ { X } } }$ , define $\bar { \omega } = 1 - \omega$ in the element-wise manner. We may expand the above $H _ { 0 }$ tensors into $H = 2 H _ { 0 }$ ones, ordered as

$$
\{ \omega ^ { ( 1 ) } , \cdots , \omega ^ { ( H ) } \} = \{ \omega ^ { ( 1 ) } , \cdots , \omega ^ { ( H _ { 0 } ) } , \bar { \omega } ^ { ( 1 ) } , \cdots , \bar { \omega } ^ { ( H _ { 0 } ) } \} .
$$

Then $\begin{array} { r } { \log H \geq \frac { m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 8 } } \end{array}$ and for any $i , j \in [ H ]$ with $i \neq j$ , it holds that $\begin{array} { r } { \| \omega ^ { ( i ) } - \omega ^ { ( j ) } \| _ { \mathrm { H } } \ge \frac { m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 4 } } \end{array}$

Next, for each $i \in [ H ]$ and $x \in \mathcal { M } _ { X }$ , let $\mathcal { M } _ { Y | x } ^ { \omega ^ { ( i ) } } = G _ { \omega ^ { ( i ) } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) , x ) = \{ G _ { \omega ^ { ( i ) } } ( z , x ) : z \in \in$ $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) \}$ denote the perturbed manifher the uniform distribution fromover $G _ { \omega ^ { ( i ) } } ( \cdot , x )$ on to over $\mu _ { 0 }$ moothlyas $\mu _ { 1 }$ $\widetilde { \mathcal { M } } _ { 1 }$ $\mu _ { Y | x } ^ { \omega ^ { ( i ) } } : = [ G _ { \omega ^ { ( i ) } } ( \cdot , x ) ] _ { \# } \nu _ { 0 }$ $\mathcal { M } _ { Y \mid x } ^ { \omega ^ { ( i ) } }$

$$
\mu _ { Y | x } ^ { i } = \Big ( 1 - \frac { \widetilde { C } } { C } \Big ) \cdot \mu _ { 1 } + \frac { \widetilde { C } } { C } \cdot \mu _ { Y | x } ^ { \omega ^ { ( i ) } } ,
$$

re a $C$ olume o. Then $\mathcal { M } _ { 0 }$ so that is suppo $C ^ { - 1 }$ is the density funover the manifold ribution over. Given that $\mathcal { M } _ { 0 }$ $C > \widetilde { C }$ $\mu _ { Y \mid x } ^ { i }$ $\mathcal { M } _ { Y | x } ^ { i } : = \widetilde { \mathcal { M } } _ { 1 } \cup \mathcal { M } _ { Y | x } ^ { \omega ^ { ( i ) } }$ $G _ { \omega ^ { ( i ) } } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) , \mathcal { M } _ { X } \bigr )$ and, bya 3 that $G _ { \omega ^ { ( i ) } } ( z , x ) = G _ { 0 } ( z )$ $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) \backslash$ $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , { \frac { 3 } { 4 } } )$ $\{ \mathcal { M } _ { Y | x } ^ { \omega ^ { ( i ) } } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } , \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ enough $\tau , \tau _ { 1 }$ and large enough $L$ . Furthermore, the density function of distribution $\mu _ { Y \mid x } ^ { i }$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x } ^ { i }$ is given by

$$
u _ { i } ( y | x ) = \frac { 1 } { C } \mathbf { 1 } ( y \in \widetilde { \mathcal { M } _ { 1 } } ) + \frac { 1 } { C } \frac { \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G _ { 0 } } \bigl ( y _ { 1 : d _ { Y } } \bigr ) ^ { T } \mathbf { J } _ { G _ { 0 } } \bigl ( y _ { 1 : d _ { Y } } \bigr ) \bigr ) } } { \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G _ { \omega ^ { ( i ) } } ( \cdot , x ) } \bigl ( y _ { 1 : d _ { Y } } \bigr ) ^ { T } \mathbf { J } _ { G _ { \omega ^ { ( i ) } } ( \cdot , x ) } \bigl ( y _ { 1 : d _ { Y } } \bigr ) \bigr ) } } \mathbf { 1 } ( y \in \mathcal { M } _ { Y | x } ^ { \omega ^ { ( i ) } } ) .
$$

Then consider the smooth transition function

$$
\rho _ { a } ( t ) = \left\{ \begin{array} { c c } { 0 } & { | t | \geq a } \\ { 1 } & { | t | \leq 1 } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) - 2 t } { ( t - 1 ) ( t - a ) } ) } } & { 1 < t < a } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) + 2 t } { ( t + 1 ) ( a + t ) } ) } } & { - a < t < - 1 , } \end{array} \right.
$$

and define

$$
\overline { { u } } _ { i } ( y , x ) = \frac { 1 } { C } + \frac { 1 } { C } \Big ( \frac { \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G _ { 0 } } \bigl ( y _ { 1 : d _ { Y } } \bigr ) ^ { T } \mathbf { J } _ { G _ { 0 } } \bigl ( y _ { 1 : d _ { Y } } \bigr ) \bigr ) } } { \sqrt { \operatorname* { d e t } \bigl ( \mathbf { J } _ { G _ { \omega ^ { ( i ) } } ( \cdot , x ) } \bigl ( y _ { 1 : d _ { Y } } \bigr ) ^ { T } \mathbf { J } _ { G _ { \omega ^ { ( i ) } } ( \cdot , x ) } \bigl ( y _ { 1 : d _ { Y } } \bigr ) \bigr ) } } - 1 \Big ) \rho _ { \frac { 1 6 } { 9 } } \big ( \frac { \| y _ { 1 : d _ { Y } } \| ^ { 2 } } { \frac { 9 } { 1 6 } } \big ) ,
$$

Note that function $\begin{array} { r } { \frac { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ^ { T } \mathbf { J } _ { G _ { 0 } } ( y _ { 1 : d _ { Y } } ) ) } } { \sqrt { \operatorname* { d e t } ( \mathbf { J } _ { G _ { \omega } ( i ) } ( \cdot , x ) \left( y _ { 1 : d _ { Y } } \right) ^ { T } \mathbf { J } _ { G _ { \omega } ( i ) } ( \cdot , x ) \left( y _ { 1 : d _ { Y } } \right) ) } } = 1 } \end{array}$ for $\begin{array} { r } { y _ { 1 : d _ { Y } } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) \setminus \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { 3 } { 4 } ) . } \end{array}$ Consequently, for any $x \in \mathcal { M } _ { X }$ and $y \in \mathcal { M } _ { Y | x } ^ { i }$ , it holds that $\overline { { \mu } } _ { i } ( y , x ) = \mu _ { i } ( y | x )$ , and there exists a constant $L$ such that $\overline { { { \mu } } } _ { i } ( y , x ) \in \mathcal { H } _ { L } ^ { \beta _ { Y } - 1 , \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } ) \subset \mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ . Therefore,

for any $i \in [ H ]$ , it holds that $\mu _ { X } ^ { * } \mu _ { Y | X } ^ { i } \ \in \ \mathcal { P } _ { 3 } ^ { * } ( D _ { Y } , D _ { X } , d _ { Y } , d _ { X } , \beta _ { X } , \beta _ { Y } , \alpha _ { Y } , \alpha _ { X } , \tau , \tau _ { 1 } , g , L )$ , where $g ( \cdot ) \equiv 1$ . Then let $\begin{array} { r } { \bar { \mu } = \frac { 1 } { H } \sum _ { i = 1 } ^ { H } \mu _ { X } ^ { * } \mu _ { Y | X } ^ { i } } \end{array}$ be the averaged distribution. Since for any fixed index $\xi \in [ m _ { 1 } ] ^ { d _ { Y } } \otimes [ m _ { 2 } ] ^ { d _ { X } }$ , there are equal numbers of 0’s and 1’s in the sequence $( \omega _ { \xi } ^ { ( 1 ) } , \cdots , \omega _ { \xi } ^ { ( H ) } )$ , we have

$$
D _ { \mathrm { K L } } ( \mu _ { X } ^ { * } \mu _ { Y | X } ^ { i } , \bar { \mu } ) = \mathbb { E } _ { \mu _ { X } ^ { * } } [ D _ { \mathrm { K L } } ( \mu _ { Y | x } ^ { i } , \bar { \mu } _ { Y | x } ) ] \leq \log 2 .
$$

Moreover, for any pair of $j , k \in [ H ]$ with $j \neq k$ , by construction we have $\begin{array} { r } { \| \omega ^ { ( j ) } - \omega ^ { ( k ) } \| _ { \mathrm { H } } \ge \frac { m _ { 1 } ^ { d _ { Y } } m _ { 2 } ^ { d _ { X } } } { 4 } } \end{array}$ . Define

$$
\widetilde { f } ( z , x ) = \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { Y } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { X } } } \left( \frac { 1 } { m _ { 1 } } \right) ^ { \gamma } v _ { \xi _ { 1 } , \xi _ { 2 } } \psi _ { \xi _ { 1 } \xi _ { 2 } } ( z , x ) ,
$$

where

holds that By the definition of $\begin{array} { r } { \operatorname* { s u p p } ( \mu _ { Y | x } ^ { \omega ( j ) } ) \subset \mathbb { R } ^ { d _ { Y } } \times \{ y _ { d + 1 } : | y _ { d + 1 } - \sqrt { 2 - \| y _ { 1 : d } \| ^ { 2 } } | \leq \frac { c } { m _ { 1 } ^ { \beta } Y } \} \times \{ ( y _ { d _ { Y } + 2 } , \cdot \cdot \cdot , x _ { D _ { Y } } ) ^ { T } = \frac { c } { m _ { 1 } ^ { \beta } Y } \} , } \end{array}$ $g _ { \omega } ( z , x )$ , there exists a constant $c$ such that for any $j \in [ H ]$ and $x \in \mathcal { M } _ { X }$ , it ${ \bf 0 } _ { D _ { Y } - d _ { Y } - 1 } \}$ . Define function $h : \mathbb { R }  \mathbb { R }$ by $\begin{array} { r } { h ( x ) \ = \ \operatorname* { m a x } ( - \frac { c } { m _ { 1 } ^ { \beta _ { Y } } } , \operatorname* { m i n } ( \frac { c } { m _ { 1 } ^ { \beta _ { Y } } } , x ) ) } \end{array}$ cβY , x)), then h is a 1- Lipschitz function over $\mathbb { R }$ . Consider function $\chi : \mathbb { R }  \mathbb { R }$ defined by $\chi ( t ) = e ^ { - 1 / t }$ for $t > 0$ and $\chi ( t ) = 0$ for $t \leq 0$ . For $z \in \mathbb { R } ^ { d _ { Y } }$ , we define

$$
q ( z ) = \left\{ \begin{array} { c c } { \sqrt { 2 - \| z \| ^ { 2 } } \cdot \frac { \chi ( 5 / 4 - \| z \| _ { 2 } ) } { \chi ( 5 / 4 - \| z \| _ { 2 } ) + \chi ( \| z \| _ { 2 } - 1 ) } } & { \| z \| \leq \frac { 5 } { 4 } } \\ { 0 } & { \| z \| > \frac { 5 } { 4 } . } \end{array} \right.
$$

Note that when z ∈ BRdY (0, 1), q(z) = p2 − ∥z∥2 and we multiply p2 − ∥z∥2 by χ(5/4−∥z∥2)χ(5/4−∥z∥2)+χ(∥z∥2−1) to smoothly extend $\sqrt { 2 - \| z \| ^ { 2 } }$ from $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 )$ to the entire space. Now define

$$
f ( y , x ) = \widetilde { f } ( y _ { 1 : d } , x ) h \big ( y _ { d + 1 } - q ( y _ { 1 : d } ) \big ) m _ { 1 } ^ { \gamma - \gamma \beta _ { Y } + \beta _ { Y } } .
$$

We then prove that $f ( \cdot , x )$ is $\gamma$ -smooth with bounded Holder norm. Since for any ¨ $y , y ^ { \prime } \in \mathbb { R } ^ { D _ { Y } }$ , it holds that $\begin{array} { r } { | h \big ( y _ { d _ { Y } + 1 } - q ( y _ { 1 : d _ { Y } } ) \big ) | \leq \frac { c } { m _ { 1 } ^ { \beta _ { Y } } } } \end{array}$ and $\textstyle | h \bigl ( y _ { d _ { Y } + 1 } ^ { \prime } - q ( y _ { 1 : d _ { Y } } ^ { \prime } ) \bigr ) | \leq \frac { c } { m _ { 1 } ^ { \beta _ { Y } } }$ ≤ mβY1 . Therefore, we have

$$
\begin{array} { r l } { h \big ( y _ { d _ { Y } + 1 } - q ( y _ { 1 : d _ { Y } } ) \big ) - h \big ( y _ { d _ { Y } + 1 } ^ { \prime } - q ( y _ { 1 : d _ { Y } } ^ { \prime } ) \big ) \big | \leq \displaystyle \frac { ( 2 c ) ^ { 1 - \gamma } } { m \beta \gamma ( 1 - \gamma ) } \big | h \big ( y _ { d _ { Y } + 1 } - q ( y _ { 1 : d _ { Y } } ) \big ) - h \big ( y _ { d _ { Y } + 1 } ^ { \prime } - q ( y _ { 1 : d _ { Y } + 1 } ) \big ) } & { { } \mathrm { ~ f ~ o ~ r ~ } \quad x \in [ 0 , 1 ] , } \\ { \lesssim \displaystyle \frac { 1 } { m ^ { \beta _ { Y } ( 1 - \gamma ) } } \| y - y ^ { \prime } \| ^ { \gamma } . } & { { } } \end{array}
$$

Moreover, for any $z , z ^ { \prime } \in \mathbb { R } ^ { d _ { Y } }$ , there exists a constant $c _ { 1 }$ such that

$$
| \widetilde { f } ( z , x ) - \widetilde { f } ( z ^ { \prime } , x ) | \leq c _ { 1 } \frac { 1 } { m _ { 1 } ^ { \gamma - 1 } } \| z - z ^ { \prime } \| .
$$

Therefore, in the case $\begin{array} { r } { \| z - z ^ { \prime } \| \leq \frac { 1 } { m _ { 1 } } } \end{array}$ , we have $\begin{array} { r } { \| z - z ^ { \prime } \| \leq \frac { 1 } { m _ { 1 } ^ { 1 - \gamma } } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma } } \end{array}$ , and thus $| \widetilde f ( z , x ) - \widetilde f ( z , x ) | \leq$ $c _ { 1 } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma }$ ; in the case $\begin{array} { r } { \| z - z ^ { \prime } \| _ { 2 } > \frac { 1 } { m _ { 1 } } } \end{array}$ , since there exists a constant $c _ { 2 }$ such that $\begin{array} { r } { \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d } } | \widetilde { f } ( z , x ) | \leq } \end{array}$ $\frac { c _ { 2 } } { m _ { 1 } ^ { \gamma } }$ , it holds that $| \widetilde { f } ( z , x ) - \widetilde { f } ( z , x ) | \leq 2 c _ { 2 } \| z - z ^ { \prime } \| _ { 2 } ^ { \gamma }$ . Putting pieces together, we have that for any $y , \bar { y } ^ { \prime } \in \mathbb { R } ^ { D _ { Y } }$ and $\boldsymbol { x } \in \mathbb { R } ^ { D _ { X } }$ , there exist constants $c _ { 3 } , c _ { 4 }$ such that

$$
\begin{array} { r l } & { | f ( y , x ) - f ( y ^ { \prime } , x ) | \leq m _ { 1 } ^ { \gamma - \gamma \beta _ { Y } + \beta _ { Y } } \biggl ( \biggl | \widetilde { f } ( y _ { 1 : d _ { Y } } , x ) \cdot \Bigl ( h \bigl ( y _ { d _ { Y } + 1 } - q ( y _ { 1 : d _ { Y } } ) \bigr ) - h \bigl ( y _ { d _ { Y } + 1 } ^ { \prime } - q ( y _ { 1 : d _ { Y } } ^ { \prime } ) \bigr ) } \\ & { \qquad + \Bigl | h \bigl ( y _ { d _ { Y } + 1 } ^ { \prime } - q ( y _ { 1 : d _ { Y } } ^ { \prime } ) \bigr ) \cdot ( \widetilde { f } ( y _ { 1 : d _ { Y } } , x ) - \widetilde { f } ( y _ { 1 : d _ { Y } } ^ { \prime } , x ) ) \Bigr | \biggr ) } \\ & { \qquad \leq c _ { 3 } \bigl ( \| y - y ^ { \prime } \| ^ { \gamma } + m _ { 1 } ^ { \gamma ( 1 - \beta _ { Y } ) } \| y - y ^ { \prime } \| ^ { \gamma } \bigr ) } \\ & { \qquad \leq c _ { 4 } \| y - y ^ { \prime } \| ^ { \gamma } , } \end{array}
$$

where the last inequality is due to $\beta _ { Y } ~ > ~ 1$ . Consequently, we have for any $x \in \mathcal { M } _ { X } , \frac { 1 } { c _ { 4 } } f ( \cdot , x ) \in$ $\mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } _ { Y } ^ { D } )$ (recall that we only consider $\gamma < 1$ ). Then

$$
\begin{array} { r l } & { \mathbb { E } _ { t \neq \frac { 1 } { C } } \Big [ \int _ { \Omega _ { t } } \langle \beta _ { t } ^ { x } | _ { t ^ { \prime } } \rangle _ { t ^ { \prime } } | \beta \rangle \Big ] } \\ & { = \frac { 1 } { C _ { 1 } } \cdot \frac { 1 } { C _ { 2 } } \cdot \frac { 1 } { B _ { 1 } } \Big [ \int f ( y , x ) \mathrm { d } y _ { 1 ^ { \prime } \setminus \Omega _ { t } } ^ { y } - \int f ( y , x ) \mathrm { d } \mu _ { 1 ^ { \prime } \setminus \Omega _ { t } } ^ { B } } \\ & { = \frac { \tilde { C } } { C _ { 1 } \cdot C ^ { 2 } } m _ { 1 ^ { \prime } \setminus \Omega ^ { \prime } } ^ { - \gamma _ { 2 } \beta \gamma _ { 1 } \beta \gamma _ { 2 } } \Big [ \int _ { \mathbb { R } ^ { 2 \setminus \Omega _ { t } } } \tilde { f } ( z , x ) \cdot \big ( g _ { \omega ^ { \prime } } ( z , x ) - g _ { \omega ^ { \prime } \beta \gamma _ { 1 } \beta } ( z , x ) \big ) \nu _ { 0 } ( z ) \mathrm { d } z \Big ] } \\ & { = \frac { \tilde { C } } { C _ { 1 } \cdot C } \int _ { \left[ 0 , 1 \right] \times \pi } \frac { m \cdot \gamma _ { 1 } \beta \gamma _ { 1 } } { \int _ { \mathbb { R } ^ { 2 \setminus \Omega _ { t } } } \gamma _ { 0 } ! \gamma _ { 1 } \beta \gamma _ { 1 } \langle z \rangle _ { 1 } \cdot \big ( \sum _ { \ell \in [ m , 1 ] ^ { \prime } \setminus \xi _ { 2 } \in [ m , 2 ] ^ { \prime } } \nu _ { 1 } \xi _ { 1 } , z \mathrm { d } \ell _ { 1 ^ { \prime } \setminus \xi _ { 2 } \ell } ( z , x ) \big ) } } \\ &  \qquad \cdot \frac { 1 }  \xi _ { 1 } \cdot C \left[ m + 1 \right] ^ { \delta } \cdot \xi _ { 2 } \zeta [ m ] ^ { 4 \setminus \xi _ { 2 } \cdot \delta } - \frac  \omega _ { 0 } ^  \prime  \end{array}
$$

Then similarly to the proof of Theorem 1, we can apply Fano’s lemma to obtain

$$
\begin{array} { r l } & { \underset { \hat { \mu } _ { Y | X } \mu \in \mathcal P _ { 2 } ^ { * } } { \operatorname* { i n f } } \ \mathbb { E } _ { \mu \otimes \boldsymbol { n } } \mathbb { E } _ { \mu _ { X } } \left[ d _ { \gamma } ( \widehat { \mu } _ { Y | X } , \mu _ { Y | X } ) \right] } \\ & { \geq \underset { \underset { \scriptstyle j \neq Y } { \textsc { i n f } } } { \overset { 1 } { \sum } } \mathbb { i n f } _ { \mu _ { X } ^ { * } } [ d _ { \gamma } ( \mu _ { Y | X } ^ { j } , \mu _ { Y | X } ^ { k } ) ] \cdot \left( 1 - \frac { \log 2 + \frac { n } { H ^ { 2 } } \sum _ { j = 1 } ^ { H } D _ { \mathrm { K L } } ( \mu _ { X } ^ { * } \mu _ { Y | X } ^ { j } , \bar { \mu } ) } { \log H } \right) } \\ & { \gtrsim n ^ { - \frac { \gamma } { d _ { Y } / \beta _ { Y } + d _ { X } / \beta _ { X } } } . } \end{array}
$$

# D.6 Proof of Corollary 1 and Corollary 2

We will show Corollary 1 here. The proof of Corollary 2 follows the same approach. Note that for any $x \in \mathcal { M } _ { X }$ , since $\mu _ { Y | x } ^ { * } \in \mathcal { P } _ { Y } ^ { * }$ , it holds that

$$
\sum _ { \gamma \in \Gamma } \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } Y ) } \frac { 1 } { \delta _ { n , \gamma } } \Big [ \mathbb { E } _ { \widehat { \mu } _ { Y | x } } [ f ( Y ) ] - \widehat { \mathcal { I } } ( f , x ) \Big ] \leq \sum _ { \gamma \in \Gamma } \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } Y ) } \frac { 1 } { \delta _ { n , \gamma } } \Big [ \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ f ( Y ) ] - \widehat { \mathcal { I } } ( f , x ) \Big ] .
$$

Therefore, we have

$$
\begin{array} { r l } & { \underset { \gamma \in \mathbb { T } } { \operatorname* { s u p } } \mathbb { E } _ { \mu _ { \hat { X } } ^ { \star } } \bigg [ \underset { f \in \mathcal { H } _ { 1 } ^ { ( \mathbb { R } ^ { N } ) } \cap \mathcal { H } _ { N , \gamma } } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \hat { n } _ { \gamma } \times \lfloor f } ( Y ) \vert - \widehat { \mathcal { T } } ( f , X ) \Big ) \bigg ] } \\ & { \leq \mathbb { E } _ { \mu _ { \hat { X } } ^ { \star } } \bigg [ \underset { \gamma \in \mathbb { T } } { \sum } \underset { \forall n _ { x } ^ { \prime } } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \hat { n } _ { \gamma } \times \lfloor f } ( Y ) \vert - \widehat { \mathcal { T } } ( f , X ) \Big ) \bigg ] } \\ & { \leq \mathbb { E } _ { \mu _ { x } ^ { \star } } \bigg [ \underset { \gamma \in \mathbb { T } } { \sum } \underset { f \in \mathcal { H } _ { 1 } ^ { ( \mathbb { R } ^ { N } ) } \cap \mathcal { H } _ { n , \gamma } } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \mu _ { \hat { X } } ^ { \star } \lfloor \mathcal { T } } \{ f ( Y ) \vert - \widehat { \mathcal { T } } ( f , X ) \Big ) } \bigg ]  \\ & { = \underset { \gamma \in \mathbb { T } } { \sum } \mathbb { E } _ { \mu _ { \hat { X } } ^ { \star } } \bigg [ \underset { f \in \mathcal { H } _ { 1 } ^ { ( \mathbb { R } ^ { N } ) } \cap \mathcal { H } _ { n , \gamma } } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \mu _ { \hat { X } } ^ { \star } \lfloor \mathcal { T } } \{ f ( Y ) \vert - \widehat { \mathcal { T } } ( f , X ) \Big ) } \bigg ]  \\  \end{array}
$$

Furthermore, by Theorem 6, it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that

$$
\operatorname* { s u p } _ { \gamma \in \Gamma } \frac { 1 } { \delta _ { n , \gamma } } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } \left( \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ] - \widehat { \mathcal { I } } ( f , x ) \right) \right] \leq 1 .
$$

Therefore,

$$
\begin{array} { r l } & { \underset { \gamma \in \Gamma } { \operatorname* { s u p } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \hat { \mu } _ { Y \mid X } } [ f ( Y ) ] - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ f ( Y ) ] \Big ) \Big ] } \\ & { \leq \underset { \gamma \in \Gamma } { \operatorname* { s u p } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \hat { \mu } _ { Y \mid X } } [ f ( y ) ] - \widehat { \mathcal { I } } ( f , X ) \Big ) \Big ] } \\ & { \quad \quad + \underset { \gamma \in \Gamma } { \operatorname* { s u p } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \frac { 1 } { \delta _ { n , \gamma } } \Big ( \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ f ( Y ) ] - \widehat { \mathcal { I } } ( f , X ) \Big ) \Big ] \lesssim \log n . } \end{array}
$$

Then for any $\gamma > 0$ , if $\gamma < { \frac { 1 } { \log n } }$ < 1log n , then

$$
\mu _ { X } ^ { * } \left[ \operatorname* { s u p } _ { f \in \mathcal { H } _ { 1 } ^ { \gamma } ( \mathbb { R } ^ { D } Y ) } \left( \mathbb { E } _ { \widehat { \mu } _ { Y \mid x } } [ f ( Y ) ] - \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ] \right) \right] \leq 2 = 2 \exp ( \frac { \beta _ { Y } } { d _ { Y } } ) n ^ { - \frac { \mathrm { I m } \alpha } { \beta _ { Y } } } \leq 2 \exp ( \frac { \beta _ { Y } } { d _ { Y } } ) n ^ { - \frac { \gamma } { \beta _ { Y } } } .
$$

If $\begin{array} { r } { \frac { 1 } { \log n } \leq \gamma \leq \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ , then there exists $k \in [ s ]$ , so that $\textstyle { \frac { k } { \log n } } \leq \gamma \leq { \frac { k + 1 } { \log n } }$ , thus

$$
\begin{array} { r l } { \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \left( \mathbb { E } _ { \widehat { \mu } _ { Y \mid x } } [ f ( y ) ] - \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ] \right) \Big ] \leq \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \underset { \mathrm { R e r } } { \operatorname* { s u p } } } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \left( \mathbb { E } _ { \widehat { \mu } _ { Y \mid x } } [ f ( y ) ] - \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ f ( Y ) ] \right) } \\ { \lesssim \log n \cdot \delta _ { n , \frac { k } { \log n } } \lesssim \log n \cdot \delta _ { n , \gamma } . } \end{array}
$$

If $\begin{array} { r } { \gamma > \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \end{array}$ , then

$$
\begin{array} { r l } { \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \prime } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \left( \mathbb { E } _ { \widehat { \mu } _ { Y | x } } [ f ( y ) ] - \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ f ( Y ) ] \right) \Big ] \leq \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \underset { f \in \mathcal { H } _ { 1 } ^ { \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } ( \mathbb { R } ^ { D _ { Y } } ) } { \operatorname* { s u p } } \left( \mathbb { E } _ { \widehat { \mu } _ { Y | x } } [ f ( y ) ] - \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ f ( Y ) ] \right) \Big ] } & { } \\ { \lesssim \log n \cdot \delta _ { n , \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } \asymp ( \log n ) ^ { 4 } \cdot n ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } . } & { } \end{array}
$$

Proof is completed.

# D.7 Proof of Lemma 12

We will first show an oracle inequality for the estimator

$$
\tilde { \mathrm { f } } _ { j } ^ { \dagger } = \arg \operatorname* { m i n } _ { S \in S _ { j } ^ { \dagger } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( 2 ^ { \frac { j ( d \chi - D _ { Y } ) } { 2 } } \psi ( Y _ { i } ) - S ( \psi , X _ { i } ) ) ^ { 2 } , \quad j \in \{ 0 \} \cup [ J ] \mathrm { ~ w i t h ~ } J = \lceil \frac { 1 } { d _ { Y } } \cdot \log ( \frac { 1 } { d _ { Y _ { i } } } ) \rceil ,
$$

with a general choice of $\boldsymbol { S } _ { j } ^ { \dagger }$ . For $S , S ^ { \prime } \in \mathcal { S } _ { j } ^ { \dagger }$ , we denote

$$
d _ { S } ( S , S ^ { \prime } ) = \operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \sqrt { \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) ) ^ { 2 } } ,
$$

and let $\mathbf { N } ( \boldsymbol { S } _ { j } ^ { \dagger } , d _ { S } , \varepsilon )$ denote the $\varepsilon$ -covering number of $\boldsymbol { S } _ { j } ^ { \dagger }$ under the pseudo-distance $d _ { S }$ .

Lemma 16. Suppose $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ are $n$ i.i.d data from $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , and the following assumptions are satisfied: $( l )$ for any $x \in \mathcal { M } _ { X } = \mathrm { s u p p } ( \mu _ { X } ^ { * } ) , \mu _ { Y | x } ^ { * }$ supported on a submanifold, denoted as $\mathcal { M } _ { Y \mid x }$ , and has a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ , and there exist constants $\beta _ { Y } ~ \ge ~ 2 , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } ~ > ~ 0$ and $a$ function $\overline { { u } } ^ { * } \in \overline { { \mathcal { H } } } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ so that $\{ \mathcal { M } _ { Y | x } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ and $\overline { { u } } ^ { * } ( y , x ) = u ( y | x )$ for any $( x , y ) \in { \mathcal { M } }$ ; (2) there exists a constant $C$ so that for any $x \in \mathcal { M } _ { X }$ , $j \in \{ 0 \} \cup [ J ]$ and $S \in \mathcal { S } _ { j } ^ { \dagger }$ ,

$$
\operatorname* { s u p } _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \lvert S ( \psi , x ) \rvert \leq C 2 ^ { - \frac { d _ { Y } j } { 2 } } a n d \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbf { 1 } ( S ( \psi , x ) \neq 0 ) \leq C 2 ^ { d _ { Y } j } ,
$$

and $\begin{array} { r } { \log \mathbf { N } (  { \mathcal { S } } _ { j } ^ { \dagger } , d _ { S } , \varepsilon ) \leq \mathcal { W } _ { j } \log ( \frac { n } { \varepsilon } ) } \end{array}$ for any $\varepsilon < \operatorname* { s u p } _ { S , S ^ { \prime } \in { \mathcal { S } } _ { j } ^ { \dagger } } d _ { S } ( S , S ^ { \prime } )$ . Then it holds with probability at least $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dagger } ( \psi , X ) \big ) ^ { 2 } \Big ] \lesssim \frac { \log n } { n } \mathcal { W } _ { j } } \\ & { \qquad + \displaystyle \operatorname* { m i n } _ { S \in \mathcal { S } _ { j } ^ { \dagger } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - S ( \psi , X ) \big ) ^ { 2 } \Big ] . } \end{array}
$$

The proof of Lemma 16 is provided in Appendix D.11. Then for the family $\boldsymbol { S } _ { j } ^ { \dagger }$ defined as

$$
\begin{array} { r } { S _ { j } ^ { \dagger } = \Bigg \{ S ( \psi , x ) = \frac { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } X , | k | < \alpha _ { X } } a _ { i _ { 1 } i _ { 2 } k } ( x - b _ { i _ { 2 } } ) ^ { k } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { x } } \right) \rho \left( \frac { \| Z _ { j } ( \psi ) - e _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { y } } \right) } { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { x } } \right) \rho \left( \frac { \| Z _ { j } ( \psi ) - e _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { y } } \right) + \frac { 1 } { n } } : } \end{array}
$$

for any $i _ { 1 } \in [ W _ { j } ] , i _ { 2 } \in [ W _ { j } ^ { \prime } ]$ , and $k \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ with $| k | < \alpha _ { X }$

$$
b _ { i _ { 2 } } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L ) , a _ { i _ { 1 } i _ { 2 } k } \in [ - \frac { C } { 2 ^ { d _ { Y } j / 2 } } , \frac { C } { 2 ^ { d _ { Y } j / 2 } } ] , e _ { i _ { 1 } } \in [ 0 , 1 ] ^ { D _ { Y } + 1 } \Bigg \} ,
$$

where $\begin{array} { r } { \frac { x } { j } = 2 ^ { \frac { j d \gamma } { 2 \alpha _ { X } + d _ { X } } } \bigl ( \frac { n } { \log n } \bigr ) ^ { - \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } , \varepsilon _ { j } ^ { y } = \frac { 2 ^ { - j } } { C _ { 1 } } , W _ { j } ^ { \prime } = C _ { 2 } \bigl ( \varepsilon _ { j } ^ { x } \bigr ) ^ { - d _ { X } } , W _ { j } = C _ { 3 } \bigl ( \varepsilon _ { j } ^ { y } \bigr ) ^ { - d _ { Y } } . } \end{array}$ . It holds for any $S \in S _ { j } ^ { \dagger }$ that

$$
\operatorname* { s u p } _ { \psi \in \Psi _ { j } ^ { D _ { Y } x \in \mathcal { M } _ { X } } } \operatorname* { s u p } _ { x } | S ( \psi , x ) | \leq \operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \sum _ { \substack { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } } | a _ { i _ { 1 } i _ { 2 } k } | \cdot \| x - b _ { i _ { 2 } } \| ^ { k } \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } } .
$$

Moreover, since for any $\psi , \psi ^ { \prime } \in \Psi _ { j } ^ { D _ { Y } }$ with $\psi \neq \psi ^ { \prime }$ , it holds that $\lVert \mathbb { Z } _ { j } ( \psi ) - \mathbb { Z } _ { j } ( \psi ^ { \prime } ) \rVert ~ > ~ c 2 ^ { - j }$ . If $\varepsilon _ { j } ^ { y } \leq \frac { c } { 4 } 2 ^ { - j }$ , then for any $e \in [ 0 , 1 ] ^ { D _ { Y } + 1 }$ , there are at least one $\psi \in \Psi _ { j } ^ { D _ { Y } }$ so that $\rho \big ( \frac { \lVert \boldsymbol { \mathcal { Z } } _ { j } ( \psi ) - \boldsymbol { e } \rVert } { \varepsilon _ { j } ^ { y } } \big ) \neq 0$ . Therefore, there are at least $W _ { j } = { \mathcal { O } } ( 2 ^ { j d _ { Y } } )$ number of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ so that $S ( \psi , x ) \neq 0$ . So

$$
\sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbf { 1 } ( S ( \psi , x ) \neq 0 ) \leq C 2 ^ { d _ { Y } j } .
$$

Furthermore, consider

$$
S ( \psi , x ) = \frac { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } \boldsymbol { x } _ { , | k | < \alpha _ { X } } } a _ { i _ { 1 } i _ { 2 } k } ( x - b _ { i _ { 2 } } ) ^ { k } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) \rho \left( \frac { \| \boldsymbol { Z } _ { j } ( \psi ) - \boldsymbol { e } _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { \psi } } \right) } { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho \left( \frac { \| x - b _ { i _ { 2 } } \| } { \varepsilon _ { j } ^ { \varepsilon } } \right) \rho \left( \frac { \| \boldsymbol { Z } _ { j } ( \psi ) - \boldsymbol { e } _ { i _ { 1 } } \| } { \varepsilon _ { j } ^ { \psi } } \right) + \frac { 1 } { n } } \in S _ { j } ^ { \dagger }
$$

and

$$
S ^ { \prime } ( \psi , x ) = \frac { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k \in \mathbb { R } _ { 0 } ^ { D } x } { _ { , | k | < \alpha _ { X } } } a _ { i _ { 1 i 2 k } } ^ { \prime } ( x - b _ { i _ { 2 } } ^ { \prime } ) ^ { k } \rho \big ( \frac { \| x - b _ { i _ { 2 } } ^ { \prime } \| } { \varepsilon _ { j } ^ { \varepsilon } } \big ) \rho \big ( \frac { \| \mathcal { D } _ { j } ( \psi ) - e _ { i _ { 1 } } ^ { \prime } \| } { \varepsilon _ { j } ^ { \varepsilon } } \big ) } { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho \big ( \frac { \| x - b _ { i _ { 2 } } ^ { \prime } \| } { \varepsilon _ { j } ^ { \varepsilon } } \big ) \rho \big ( \frac { \| \mathcal { D } _ { j } ( \psi ) - e _ { i _ { 1 } } ^ { \prime } \| } { \varepsilon _ { j } ^ { \varepsilon } } \big ) + \frac { 1 } { n } } \in S _ { j } ^ { \dagger } .
$$

It holds that for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathcal { M } _ { X }$ ,

$$
\begin{array} { r l } & { | S ( \psi , x ) - S ^ { \prime } ( \psi , x ) | } \\ & { \lesssim \underset { i _ { 1 } \in [ W _ { j } ] } { \operatorname* { s u p } } \underset { i _ { 2 } \in [ W _ { j } ] } { \operatorname* { s u p } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } , | k | < \alpha _ { X } } | a _ { i _ { 1 } i _ { 2 } k } - a _ { i _ { 1 } i _ { 2 } k } ^ { \prime } | + \frac { W _ { j } n } { \varepsilon _ { j } ^ { x } } \underset { i _ { 2 } = 1 } { \overset { W _ { j } ^ { \prime } } { \sum } } \Vert b _ { i _ { 2 } } - b _ { i _ { 2 } } ^ { \prime } \Vert + \frac { W _ { j } ^ { \prime } n } { \varepsilon _ { j } ^ { y } } \underset { i _ { 1 } = 1 } { \overset { W _ { j } } { \sum } } \Vert e _ { i _ { 1 } } - e _ { i _ { 1 } } ^ { \prime } \Vert } \end{array}
$$

So

$$
\begin{array}{c} \begin{array} { r l } & { \displaystyle { \mathrm {  ~ \xi ~ } _ { S } ( S , S ^ { \prime } ) = \operatorname* { s u p } _ { x \in \mathcal { M } _ { x } } \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) ) ^ { 2 } } } } \\ & { \displaystyle \leq \operatorname* { s u p } _ { x \in \mathcal { M } _ { x } } \sqrt { \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) ) ^ { 2 } ( { \bf 1 } ( S ( \psi , x ) \neq 0 ) + { \bf 1 } ( S ^ { \prime } ( \psi , x ) \neq 0 ) ) } } \\ & { \displaystyle \lesssim 2 ^ { \frac { j d _ { Y } } { 2 } } \cdot \left( \operatorname* { s u p } _ { i _ { 1 } \in [ W _ { j } ] _ { i _ { 2 } \in [ W _ { j } ^ { D _ { Y } } ] _ { k \in \mathbb { N } _ { x } } } } \displaystyle \sum _ { | a _ { i _ { 1 } i _ { 2 k } k } - a _ { i _ { 1 } i _ { 2 k } } ^ { \prime } | + \frac { W _ { j } n } { \varepsilon _ { j } ^ { x } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } | | b _ { i _ { 2 } } - b _ { i _ { 2 } ^ { \prime } } ^ { \prime } | | + \frac { W _ { j } ^ { \prime } n } { \varepsilon _ { j } ^ { y } } ; } \end{array} \right. } \end{array}
$$

Then, using the fact that the $\varepsilon$ -covering number of a $d$ -dimensional ball with radius $R$ is being bounded by $\big ( \frac { 3 R } { \varepsilon } \big ) ^ { d }$ , we have

$$
\log \mathbf { N } ( \mathcal { S } _ { j } ^ { \dagger } , d _ { S } , \varepsilon ) \lesssim W _ { j } W _ { j } ^ { \prime } \log \frac { n } { \varepsilon } \lesssim 2 ^ { j d _ { Y } } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } } \log \frac { n } { \varepsilon } .
$$

Now we bound the approximation error. Let $\mathrm { v o l } _ { \mathcal { M } }$ denote the volume measure of $\mathcal { M }$ and let $\overline { { u } } ^ { * } \in$ $\mathcal { H } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $u ^ { * }$ . We have

$$
u _ { \psi } ^ { * } ( x ) = \int 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) \overline { { u } } ^ { * } ( y | x ) \mathrm { d v o l } _ { \mathcal { M } _ { Y } } \in \mathcal { H } _ { L _ { 1 2 } - d _ { Y } j / 2 } ^ { \alpha _ { X } } ( \mathbb { R } ^ { D _ { X } } ) ,
$$

where we have used the fact that

$$
\int 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } | \psi ( y ) | \mathrm { d v o l } _ { M _ { Y } } \lesssim 2 ^ { \frac { j d _ { Y } } { 2 } } \int \mathbf { 1 } ( \psi ( y ) \neq 0 ) \mathrm { d v o l } _ { M _ { Y } } \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } } .
$$

Let $\mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ denote the largest $\varepsilon _ { j } ^ { x }$ -packing set of $\mathcal { M } _ { X }$ , then its cardinality satisfies $| \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | \leq C _ { 2 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } } =$ $W _ { j } ^ { \prime }$ when $C _ { 2 }$ is large enough. Then we define a set $\overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } ^ { x } = \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } \cup \mathcal { X }$ , where $\mathcal { X }$ is an arbitrary subset of $\mathcal { M } _ { X } \backslash \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ with $| \mathcal { X } | = W _ { j } ^ { \prime } - | \mathcal { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } |$ . Denote

$$
\Psi _ { j } ^ { * } : = \{ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathcal { M } _ { Y } \neq \emptyset \} ,
$$

it holds that $\Psi _ { j } ^ { * } \subset \Psi _ { j } ^ { D _ { Y } }$ and $| \Psi _ { j } ^ { * } | \le C _ { 3 } ( \varepsilon _ { j } ^ { y } ) ^ { - d _ { Y } } = W _ { j }$ when $C _ { 3 }$ is large enough. Moreover, define $\overline { { \Psi } } _ { j } ^ { * } = \Psi _ { j } ^ { * } \cup \Phi _ { j }$ , where $\Phi _ { j }$ is an arbitrary subset of $\Psi _ { j } ^ { D _ { Y } } \backslash \Psi _ { j } ^ { * }$ with $| \Phi _ { j } | = W _ { j } - | \Psi _ { j } ^ { * } |$ . For any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ , we define

$$
\widetilde { u } _ { \psi } ( x ) = \left\{ \begin{array} { l l } { \frac { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } X , | k | < \alpha _ { X } } { u _ { \psi } ^ { * } ^ { ( k ) } ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) } } { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) } , } & { \psi \in \Psi _ { j } ^ { * } } \\ { 0 } & { o . w . } \end{array} \right.
$$

and

$$
\begin{array} { r l } & { S _ { j } ^ { \alpha } ( \psi , x ) = \frac { \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } N _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } w _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } ( \vec { x } ) ( \vec { x } ) ( x - \widetilde { x } ) ^ { k } \rho \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) } { \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \rho \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) } } \\ & { \quad = \frac { \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \left( \| x \right) \left( \vec { x } \right) ( ( \vec { x } - \widetilde { x } ) ^ { k } \rho _ { j } \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \mathbb { 1 } \left( \psi = \widetilde { y } _ { 1 } \right) } { \sum _ { \vec { x } \in \mathbb { N } _ { j } ^ { \prime } } \rho \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \left( \frac { \| x - \widetilde { x } \| } { \zeta _ { j } ^ { k } } \right) \mathbb { 1 } \left( \psi = \widetilde { y } _ { 1 } \right) } } \\ &  \quad = \frac  \sum _  \vec { x } \in \mathbb { N } _ { j } ^   \end{array}
$$

It holds that $S _ { j } ^ { * } ( \psi , x ) \in \mathcal { S } _ { j } ^ { \dagger }$ , Moreover, for any $\psi \in \Psi _ { j } ^ { D _ { Y } } \setminus \Psi _ { j } ^ { * }$ , it holds that $u _ { \psi } ^ { * } ( \cdot ) \equiv 0$ , and therefore $S _ { j } ^ { * } ( \psi , \cdot ) = \mu _ { \psi } ^ { * } ( \cdot ) \equiv 0$ . Moreover, for any $x \in \mathcal { M } _ { X }$ and $\psi \in \Psi _ { j } ^ { * }$ , we have

$$
\begin{array} { c } { \displaystyle | \widetilde { u } _ { \psi } ( x ) - S _ { j } ^ { * } ( \psi , x ) | = \frac { | \sum _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } ( x _ { 0 } ^ { 1 } , | k | < x x ) } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } \rho ( \frac { | \widetilde { x } - \widetilde { x } | } { \xi _ { j } ^ { 2 } } ) | } { n \cdot ( \sum _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } \rho ( \frac { | \widetilde { x } - \widetilde { x } | } { \xi _ { j } ^ { 2 } } ) + \frac { 1 } { n } ) ( \sum _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } \rho ( \frac { | \widetilde { x } - \widetilde { x } | } { \xi _ { j } ^ { 2 } } ) ) } | } \\ { \leq \frac { 1 } { n } \frac { \sum _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } \sum _ { k \in \mathbb { N } _ { 0 } ^ { D } ( x _ { 0 } ^ { 1 } , | k | < x ) } | u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } | \rho ( \frac { | \widetilde { x } - \widetilde { x } | } { \xi _ { j } ^ { 2 } } ) | } { \sum _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } \rho ( \frac { | \widetilde { x } - \widetilde { x } | } { \xi _ { j } ^ { 2 } } ) } } \\  \leq \frac { 1 } { n } \cdot \frac { \operatorname* { s u p } _ { \widetilde { x } \in \widetilde { N } _ { \varphi _ { \widetilde { x } ^ { 2 } } } ^ { x } } }  \pi \in \widetilde { N } _  \end{array}
$$

$$
\begin{array} { r l } & { | \widetilde { u } _ { \psi } ( x ) - u _ { \psi } ^ { * } ( x ) | = \frac { \big | \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } } \big ( \sum _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } - u _ { \psi } ^ { * } ( x ) \big ) \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) \big | } { \sum _ { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } } } \rho ( \frac { \| x - \widetilde { x } \| } { \varepsilon _ { j } ^ { x } } ) } } \\ & { \qquad \le \underset { \widetilde { x } \in \overline { { \mathcal { N } } } _ { \varepsilon _ { j } ^ { x } , x \in \mathbb { B } _ { M _ { X } } ( \widetilde { x } , 2 \varepsilon _ { j } ^ { x } ) } } { \operatorname* { s u p } } \big | _ { k \in \mathbb { N } _ { 0 } ^ { D _ { X } } , | k | < \alpha _ { X } } u _ { \psi } ^ { * } ( k ) ( \widetilde { x } ) ( x - \widetilde { x } ) ^ { k } - u _ { \psi } ^ { * } ( x ) \big | } \\ & { \qquad \lesssim 2 ^ { - \frac { d _ { Y } j } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } . } \end{array}
$$

We can get

$$
\begin{array} { r l } & { \displaystyle \operatorname* { m i n } _ { \hat { \mathbf { S } } \in \mathcal { S } _ { j } } \mathbb { E } _ { \boldsymbol { u } ^ { \star } } \bigg [ \sum _ { \ell \in \mathcal { V } _ { j } ^ { D } } \big ( S ( \boldsymbol { \psi } , X ) - u _ { \boldsymbol { \psi } } ^ { * } ( X ) \big ) ^ { 2 } \bigg ] } \\ & { \lesssim \mathbb { E } _ { \boldsymbol { \theta } _ { \boldsymbol { \hat { X } } } ^ { \star } } \bigg [ \sum _ { \ell \in \mathcal { V } _ { j } ^ { D } } ( S _ { j } ^ { \star } ( \boldsymbol { \psi } , X ) - u _ { \boldsymbol { \psi } } ^ { * } ( X ) ) ^ { 2 } \bigg ] } \\ & { \quad \quad - \mathbb { E } _ { \boldsymbol { \theta } _ { \boldsymbol { \hat { X } } } ^ { \star } } \bigg [ \displaystyle \sum _ { \ell \in \mathcal { V } _ { j } ^ { D } } ( S _ { j } ^ { \star } ( \boldsymbol { \psi } , X ) - u _ { \boldsymbol { \psi } } ^ { * } ( X ) ) ^ { 2 } \bigg ] } \\ & { \lesssim \displaystyle \sum _ { \ell \in \mathcal { V } _ { j } ^ { D } } 2 ^ { - d \nu _ { j } } \big ( ( E _ { j } ^ { \star } ) ^ { - \alpha _ { X } } + \frac { 1 } { n } \big ) ^ { 2 } } \\ & { \quad \lesssim ( \epsilon _ { j } ^ { x } ) ^ { 2 n _ { X } } + \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

The desired result then follows by substituting $\varepsilon _ { j } ^ { x } = 2 ^ { \frac { j d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } \Big ( \frac { n } { \log { n } } \Big ) ^ { - \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } .$ .

# D.8 Proof of Lemma 13

We begin by establishing a general lemma to bound the population-level reconstruction error. Consider arbitrary points $x _ { 0 } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L )$ and $y _ { 0 } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \mathbf { 0 } , L )$ , and consider the estimator

$$
\widehat { G } , \widehat { V } ) = \underset { V \in \Theta ( D _ { Y } , d _ { Y } ) } { \mathrm { a r g } \mathrm { m i n } } ~ \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { 0 } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ,
$$

where $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ are i.i.d. samples from $\mu ^ { * }$ and $\mathcal { G }$ represents an arbitrary class of functions $G$ : $\mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R } ^ { \mathbf { \bar { D } } _ { Y } }$

Lemma 17. Suppose $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ are $n$ i.i.d data from $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ , and the following assumptions are satisfied: $( l )$ for any $x \in \mathcal { M } _ { X } = \mathrm { s u p p } ( \mu _ { X } ^ { * } )$ , the conditional distribution of $Y$ given $X \ = \ x$ , denoted as $\mu _ { Y | x } ^ { * }$ , is supported on a submanifold $\mathcal { M } _ { Y \mid x }$ , and has a density function $\boldsymbol { u } ^ { * } ( \cdot | \boldsymbol { x } )$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ . There exist constants $\beta _ { Y } \ge 2 , \beta _ { X } , \alpha _ { Y } , \alpha _ { X } , L > 0$ and a function $\overline { { u } } ^ { * } \in \overline { { \mathcal { H } } } _ { L } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ such that $\{ \mathcal { M } _ { Y | x } \} _ { x \in \mathcal { M } _ { X } } \in \mathcal { M } _ { \tau , \tau _ { 1 } , L } ^ { \beta _ { Y } \beta _ { X } } ( d _ { Y } , D _ { Y } , \mathcal { M } _ { X } )$ and $\overline { { u } } ^ { * } | _ { \mathcal { M } } = u$ ; (2) there exists a function $g : \mathbb { R } ^ { + }  \mathbb { R } ^ { + }$ such that for any $x _ { 0 } \in \mathcal { M } _ { X } , y _ { 0 } \in \mathcal { M } _ { Y | x _ { 0 } }$ and for all $0 < r \leq 1$ , it holds that $\mu _ { X } ^ { * } ( \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , r ) ) \ge g ( r )$ and $\mu _ { Y | x _ { 0 } } ^ { * } ( \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , r ) ) \ge g ( r ) _ { \Sigma }$ ; (3) there exist constants $L > 0$ and $\beta > 1$ such that that for any $G ( z , x ) \in \mathcal { G }$ , it holds for any $x \in \mathcal { M } _ { X }$ that $G ( \cdot , x ) \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta } ( \mathbb { R } ^ { d _ { Y } } )$ . Then

1. If there exists $G \in { \mathcal { G } }$ and $V \in \mathbb { O } ( D _ { Y } , d _ { Y } )$ such that for any $( x , y ) \in \mathcal { M } = \{ ( x , y ) : x \in$ $\mathcal { M } _ { X } , y \in \mathcal { M } _ { Y | x } \}$ with $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } )$ and $y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } )$ , it holds that $\parallel y - G ( V ^ { T } ( y -$ $y _ { 0 } ) , x ) \| \leq \varepsilon ^ { * }$ . Consider any $\gamma _ { 1 } \in ( 0 , 1 ]$ and denote $\mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon )$ as the $\varepsilon$ -covering number of $\mathcal { G }$ with respect to the $d _ { \infty } ^ { \gamma _ { 1 } }$ distance, where $\begin{array} { r l r l } { d _ { \infty } ^ { \gamma _ { 1 } } ( G _ { 1 } , G _ { 2 } ) = } & { { } } & { \operatorname* { s u p } \quad } & { { } \| G _ { 1 } ( z , x ) - G _ { 2 } ( z , x ) \| ^ { \gamma _ { 1 } } } \end{array}$ . $z \in \mathbb { R } ^ { d _ { Y } } , x \in \mathbb { R } ^ { D _ { X } }$ There exists a constant C so that, with probability at least 1 − 1n3 ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } ( \widehat { V } ^ { T } ( Y - y _ { 0 } ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq C \Big ( \displaystyle \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon / 2 ) } \mathrm { d } \varepsilon + \sqrt { \displaystyle \frac { \log n } { n } } + ( \varepsilon ^ { * } ) ^ { \gamma _ { 1 } } \Big ) . } \end{array}
$$

2. If there exists $( x ^ { * } , y ^ { * } ) \in \mathbb { B } _ { \boldsymbol { \mathcal { M } } } ( ( x _ { 0 } , y _ { 0 } ) , \sqrt { 2 } \tau _ { 2 } )$ , and $\tau _ { 2 } < \frac { \tau _ { 1 } \wedge \tau } { 2 }$ . Then let $P ^ { * }$ be the projection matrix of $T _ { \mathcal { M } _ { Y \mid x ^ { * } } } y ^ { * }$ , there exist positive constants $c , c _ { 1 }$ so that if $\cdot \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } ( \widehat { V } ^ { T } ( Y - y _ { 0 } ) , X ) \|$ · $\mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \leq c ,$ then $\widehat { V } ^ { T } P ^ { * } \widehat { V } ^ { T } \geq c _ { 1 } I _ { d _ { Y } }$ .

The proof of Lemma 17 can be found in Appendix D.12. Given Lemma 17, it suffices to demonstrate the first statement of Lemma 13. The second statement of Lemma 13 naturally follows from the second statement of Lemma 17. Consider the family

$$
\mathcal { G } = \{ G ( z ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } g _ { \psi _ { 1 } } \psi _ { 1 } ( z ) : g _ { \psi _ { 1 } } \in [ - L _ { 1 } \delta _ { j _ { 1 } } , L _ { 1 } \delta _ { j _ { 1 } } ] ^ { D _ { Y } } , \mathrm { ~ f o r ~ } \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } \} ,
$$

where there $J _ { 1 } = \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { Y } } } ) \rceil$ $L$ $\delta _ { j _ { 1 } } = 2 ^ { - \frac { d _ { Y } j _ { 1 } } { 2 } - \left( j _ { 1 } \beta _ { Y } \right) }$ $\mathcal { G } \subset \mathcal { H } _ { L , D _ { Y } } ^ { \beta } ( \mathbb { R } ^ { d _ { Y } } )$ − dY j12 −(j1βY ). It is straightforward to verify that for any β < βY , Moreover, we can derive the following le $\mathcal { G }$

Lemma 18. With the choice of $\mathcal { G }$ in (37), there exists a constant $C _ { 1 }$ so that for any $\gamma _ { 1 } \in ( 0 , 1 ] ,$ the $\varepsilon$ -covering number $\mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma 1 } , \varepsilon )$ of $\mathcal { G }$ with respect to the $d _ { \infty } ^ { \gamma _ { 1 } }$ distance, satisfies that

$$
\begin{array} { r l } & { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) } \\ & { \leq \left\{ \begin{array} { l l } { \quad C _ { 1 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { d _ { Y } j _ { 1 } } \log \left( \frac { C _ { 1 } J _ { 1 } 2 ^ { - \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } \vee 1 } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } \vee 1 \right) } & { \frac { d _ { Y } } { \beta _ { 1 } } \leq 2 \gamma _ { 1 } , } \\ { C _ { 1 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { d _ { Y } j _ { 1 } } \log \left( \frac { C _ { 1 } \left( J _ { 1 } \wedge c ( \beta _ { Y } , d _ { Y } , d _ { X } , \gamma _ { 1 } ) \right) 2 ^ { - j _ { 1 } \beta _ { Y } } } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } } } \vee 1 \right) } & { \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } , } \end{array} \right. } \end{array}
$$

where $\begin{array} { r } { c ( \beta _ { Y } , d _ { Y } , d _ { X } , \gamma _ { 1 } ) = \frac { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) } { 4 \gamma _ { 1 } } } } { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) } { 4 \gamma _ { 1 } } } - 1 } a n d s _ { j _ { 1 } } = \sqrt { \frac { 2 ^ { \frac { d _ { Y } j _ { 1 } } { 2 \gamma _ { 1 } } - j _ { 1 } \beta _ { Y } } } { 2 ^ { \frac { d _ { Y } J _ { 1 } } { 2 \gamma _ { 1 } } - J _ { 1 } \beta _ { Y } } } } . } \end{array}$

Notice that $| I _ { 1 } | = \lfloor n / 2 \rfloor \asymp n$ , we will then bound the integral $\begin{array} { r } { \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) } \mathrm { d } \varepsilon } \end{array}$ . When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } \le 2 \gamma _ { 1 } } \end{array}$ , we have

$$
\begin{array} { r l } & { \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( G , d \vec { x } , \frac { s } { \sigma _ { 1 } } ) d z } } \\ & { \lesssim \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } \sqrt { \frac { 3 } { \sqrt { \pi } - 1 } \log \left( \frac { C _ { 1 , 1 } / 2 ^ { - \frac { 3 \sigma _ { 1 } } { \sigma _ { 1 } } - \frac { \lambda ^ { 4 \sigma _ { 1 } } } { \sigma _ { 1 } } } - \sigma ^ { 1 } } { s ^ { \sigma _ { 1 } } } \right) } \Bigg ) ^ { 2 / 4 \nu + 3 } } \\ & { \lesssim \frac { 1 } { \sqrt { \pi } } \frac { 1 } { \sqrt { \pi } } \int _ { 0 } ^ { \infty } \sqrt { \log \left( \frac { C _ { 1 , 1 } / 2 ^ { - \frac { 3 \sigma _ { 1 } } { \sigma _ { 1 } } - \frac { \lambda ^ { 4 \sigma _ { 1 } } } { \sigma _ { 1 } } } - \sigma ^ { 1 } } { s ^ { \sigma _ { 1 } } } \right) } \Bigg ) ^ { 2 / 4 \nu + 3 } } \\ & { \lesssim \frac { 1 } { \sqrt { \pi } } \frac { 1 } { \sqrt { \pi } \infty } \int _ { 0 } ^ { \infty } \sqrt { \log \left( \frac { C _ { 1 , 1 } / 2 ^ { - \frac { 3 \sigma _ { 1 } } { \sigma _ { 1 } } - \frac { \lambda ^ { 4 \sigma _ { 1 } } } { \sigma _ { 1 } } } - \sigma ^ { 1 } } { s ^ { \sigma _ { 1 } } } \right) ^ { 2 } } \sqrt { \log \left( \frac { C _ { 1 , 1 } / 2 ^ { - \frac { 3 \sigma _ { 1 } } { \sigma _ { 1 } } - \frac { \lambda ^ { 4 \sigma _ { 1 } } } { \sigma _ { 1 } } } - \sigma ^ { 2 } } { s ^ { \sigma _ { 1 } } } \right) } \frac { 2 ^ { 4 \sigma _ { 1 } } \sqrt { \pi } } { s ^ { \sigma _ { 1 } } } } \\ &  \lesssim \frac \end{array}
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } } \end{array}$ , we have

$$
\begin{array} { r l } & { \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \log ( G , d _ { 1 } ^ { n / 2 } , s ) \mathrm { d } s } } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \frac { 1 } { \sqrt { n } - 0 } \log \Big ( \frac { C _ { 1 } ( J _ { 1 } , \chi _ { \varepsilon } ( J _ { 1 } , \ d _ { 1 } , \chi _ { 1 } , \chi _ { 1 } ) ) \big ) ^ { 2 - j / \beta } } { \varepsilon ^ { 1 / \beta } } \times 1 } \Big ) 2 ^ { \mathrm { d } s / n } \times 1 \Bigg ) } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \int _ { 0 } ^ { \infty } \sqrt { \log \Big ( \frac { C _ { 1 } ( J _ { 1 } , \chi _ { \varepsilon } ( \chi _ { 1 } , \chi _ { 1 } , \chi _ { 1 } ) ) \big ) ^ { 2 - j / \beta } } { \varepsilon ^ { 1 / \beta } } \times 1 } \Big ) } } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \frac { \lambda } { \sqrt { n } } \frac { 1 } { \log { \log } } \int _ { 0 } ^ { \infty } \sqrt { | \log \Big ( \frac { C _ { 1 } ( J _ { 1 } , \chi _ { \varepsilon } ( \chi _ { 1 } , \chi _ { 1 } , \chi _ { 1 } ) ) \big ) \big ) \cdot \frac { 1 } { \varepsilon ^ { 1 / \beta } } } \times 1 \rangle } } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \frac { 1 } { \sqrt { n } } \frac { 1 } { \log { \log } _ { 2 } ^ { \infty } ( \beta _ { 1 } \wedge \varepsilon ( \delta ) , q , \wedge \pi , 1 ) ) ^ { 2 - j / \beta } \cdot \sigma ^ { 1 / \beta } \Sigma _ { 2 } \frac { \delta ( \nu , \pi ) } { \varepsilon ^ { 1 / \beta } } } } \\ &  \lesssim ( J _ { 1 } \wedge \varepsilon ( \nu _ { 1 } , \delta _ { 1 } , \chi _ { 1 } ) \end{array}
$$

Then it remains to bound the term $\varepsilon ^ { * }$ . Fix an arbitrary $k \in [ K ]$ . If √ $\mathbb { B } _ { \mathbb { R } ^ { D } X + D _ { Y } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } ) \cap$ $\mathcal { M } = \emptyset$ , then $k \not \in { \widehat { \mathcal { K } } }$ . Otherwise, there exists $( x _ { k } ^ { * } , y _ { k } ^ { * } ) \in \mathbb { B } _ { \mathcal { M } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } )$ . Let $V _ { [ k ] } ^ { * }$ be an arbitrary orthonormal basis of $T _ { \mathcal { M } _ { Y } } y _ { k } ^ { * }$ , and denote $Q _ { [ k ] } ^ { * } ( y ) = ( V _ { [ k ] } ^ { * } ) ^ { T } ( y - y _ { k } )$ and $G _ { [ k ] } ^ { * } ( z ) = \Phi _ { y _ { k } ^ { * } } ( V _ { [ k ] } ^ { * } ( z +$ $( V _ { [ k ] } ^ { * } ) ^ { T } ( y _ { k } { - } y _ { k } ^ { * } ) ) )$ . Then $G _ { [ k ] } ^ { * } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } } \left( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( V _ { [ k ] } ^ { * ~ T } ( y _ { k } ^ { * } - y _ { k } ) , \tau _ { 1 } ) \right)$ and for any $y \in \mathcal { M } _ { Y }$ with $\| y - y _ { k } ^ { * } \| <$ $\tau _ { 1 }$ , we have $y = G _ { [ k ] } ^ { * } ( Q _ { [ k ] } ^ { * } ( y ) )$ . Moreover, by leveraging the decay of wavelet coefficients for $\mathcal { H } ^ { \beta _ { Y } }$ - smooth functions as stated in Lemma 7, when $J _ { 1 } = \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { Y } } } ) \rceil$ and $\tau _ { 2 } < \frac { \tau _ { 1 } \wedge \tau } { 4 }$ , it holds that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau _ { 2 } ) \subset \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( V _ { [ k ] } ^ { * ^ { T } } ( y _ { k } ^ { * } - y _ { k } ) , \tau _ { 1 } )$ that,

$$
\left\| G _ { [ k ] } ^ { * } ( z ) - \sum _ { j = 1 } ^ { J _ { 1 } } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \int _ { \mathbb { R } ^ { d _ { Y } } } G _ { [ k ] } ^ { * } ( z ) \psi ( z ) \mathrm { d } z \cdot \psi ( z ) \right\| \leq C n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } .
$$

Moreover, we have $\begin{array} { r } { G _ { [ k ] } ^ { \dag } ( z ) = \sum _ { j = 1 } ^ { J _ { 1 } } \sum _ { \psi \in \Psi _ { j } ^ { d _ { Y } } } \int _ { \mathbb { R } ^ { d _ { Y } } } G _ { [ k ] } ^ { * } ( z ) \psi ( z ) \mathrm { d } z \cdot \psi ( z ) \in \mathcal { G } } \end{array}$ , and for any $y \in \mathcal { M } _ { Y }$ with $\| y - y _ { k } \| \le 2 \tau _ { 2 }$ ,

$$
\| y - G _ { [ k ] } ^ { \dag } ( ( V _ { [ k ] } ^ { * } ) ^ { T } ( y - y _ { 0 } ) ) \| \le \| y - G _ { [ k ] } ^ { * } ( Q _ { [ k ] } ^ { * } ( y ) ) \| + C n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } = C n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } .
$$

Therefore, let $\widehat { Q } _ { [ k ] } ( \cdot ) = \widehat { V } _ { [ k ] } ^ { T } ( \cdot - y _ { k } )$ , using Lemma 18, we can conclude that for any $\gamma _ { 1 } \in ( 0 , 1 ]$ , there exists a constant $C _ { \gamma _ { 1 } }$ so that it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ that for any $k \in { \widehat { \mathcal { K } } }$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \left\{ \begin{array} { l l } { \qquad C _ { \gamma _ { 1 } } \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \frac { d _ { Y } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } , } \\ { C _ { \gamma _ { 1 } } ( \log n \wedge \frac { 1 } { d _ { Y } - 2 \gamma _ { 1 } \beta _ { Y } } ) ^ { 1 + \gamma _ { 1 } } \cdot n ^ { - \frac { \gamma _ { 1 } } { \frac { d _ { Y } } { \beta _ { Y } } } } } & { \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

Then if $\begin{array} { r } { \frac { d _ { Y } } { 2 \beta _ { Y } } > 1 } \end{array}$ , set $\gamma _ { 1 } = 1$ , it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ that for any $k \in { \widehat { \mathcal { K } } }$

$$
\mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| \cdot { \mathbf { 1 } } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) { \mathbf { 1 } } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \lesssim n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } .
$$

Therefore, with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ , it holds for any $k \in { \widehat { \mathcal { K } } }$ and any $\gamma _ { 1 } \in ( 0 , 1 ]$ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { s } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \Big ( \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \Big ) ^ { \gamma _ { 1 } } \lesssim n ^ { - \frac { \gamma _ { 1 } } { \frac { d _ { Y } } { \beta _ { Y } } } } . } \end{array}
$$

If $\begin{array} { r } { \frac { d _ { Y } } { 2 \beta _ { Y } } \le 1 } \end{array}$ , let $\delta _ { n } = \frac { 1 - \frac { d _ { Y } } { 4 \beta _ { Y } } } { \lceil \log n \rceil }$ and consider the set $\begin{array} { r } { \Gamma = \{ \frac { d _ { Y } } { 4 \beta _ { Y } } , \frac { d _ { Y } } { 4 \beta _ { Y } } + \delta _ { n } , \cdot \cdot \cdot , \frac { d _ { Y } } { 4 \beta _ { Y } } + \delta _ { n } \cdot \lceil \log n \rceil \} } \end{array}$ . Then by a union argument, it holds that with probability at least c log nn3 that for any k ∈ Kb and any γ1 ∈ Γ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \left\{ \begin{array} { l l } { \quad ~ { \cal C } \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } ~ } & { \frac { d _ { Y } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } , } \\ { \quad ~ } & { \quad - \frac { \gamma _ { 1 } } { \beta _ { Y } } ~ } \\ { { \cal C } ( \log n \wedge \frac { 1 } { d _ { Y } - 2 \gamma _ { 1 } \beta _ { Y } } ) ^ { 1 + \gamma _ { 1 } } \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { Y } } } } & { \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

Under the above event, for any $\gamma _ { 2 } \in ( 0 , \frac { d _ { Y } } { 4 \beta _ { Y } } )$ , by setting $\begin{array} { r } { \gamma _ { 1 } = \frac { d _ { Y } } { 4 \beta _ { Y } } } \end{array}$ , it holds that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 2 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \ \leq \left( \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \right) ^ { \gamma _ { 2 } / \gamma _ { 1 } } } \\ & { \ \lesssim n ^ { - \frac { \gamma _ { 2 } } { 4 \gamma _ { 1 } } } = n ^ { - \frac { \gamma _ { 2 } } { d _ { Y } / \beta _ { Y } } } . } \end{array}
$$

Moreover, for any $\gamma _ { 2 } \in [ \frac { d _ { Y } } { 4 \beta _ { Y } } , 1 ]$ , there exists $\gamma _ { 1 } \in \Gamma$ so that $\gamma _ { 1 } \leq \gamma _ { 2 } \leq \gamma _ { 1 } + \delta _ { n }$ , so

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 2 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq 2 L \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \left\{ \begin{array} { r l } & { C _ { 1 } \frac { \mathrm { d o g n } } { \sqrt { n } } } \\ & { C _ { 1 } ( \log n \wedge \frac { 1 } { d Y } ) ^ { 1 + \gamma _ { 1 } } } \\ & { C _ { 1 } ( \log n \wedge \frac { 1 } { d Y } ) ^ { 1 + \gamma _ { 1 } } \cdot n ^ { - \frac { \gamma _ { 1 } } { \frac { d Y } { \beta Y } } } } \end{array} \right. \overset { d _ { Y } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } } \\ &  \leq \left\{ \begin{array} { r l } & { C _ { 2 } \frac { \mathrm { d o g n } \lambda ^ { 1 + \gamma _ { 2 } } } { \sqrt { n } } } & { \frac { d _ { Y } } { \beta _ { Y } } \leq 2 \gamma _ { 2 } , } \\ & { C _ { 2 } ( \log n \wedge \frac { 1 } { d Y - 2 \gamma _ { 1 } \beta _ { Y } } ) ^ { 1 + \gamma _ { 2 } } \cdot n ^ { - \frac { \gamma _ { 2 } } { \frac { d Y } { \beta Y } } } \end{array} \right. } \endarray \end{array}
$$

This completes the proof of Lemma 13.

# D.9 Proof of Lemma 14

We will show the desired result using Lemma 16. For the family $S _ { j } ^ { \dagger }$ that consists of

$$
\begin{array} { r l } & { S ( \psi , x ) = { \mathcal { T } _ { C _ { 1 } 2 ^ { - } \frac { d _ { \gamma } j } { 2 } } } \Big ( } \\ &  \underbrace { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { \tilde { B } } _ { \mathbb { R } ^ { d } \gamma } } ( \mathbf { 0 } , \tau _ { 1 } ) ^ { 2 } } _ { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho \left( \frac { \| x - b _ { i , 2 } \| } { \varepsilon _ { j } ^ { * } } \right) \rho \left( \frac { \| \mathcal { D } _ { k , i _ { 2 } } ( z , x )  \nu _ { k , i _ { 2 } } ( z , x ) } { \varepsilon _ { j } ^ { * } } \mathrm { d } z \rho ( \frac { \| x - b _ { i , 2 } \| } { \varepsilon _ { j } ^ { * } } ) \rho ( \frac { \| \mathcal { D } _ { j } ( \psi ) - e _ { i _ { 1 } i _ { 2 } } \| } { \varepsilon _ { j } ^ { * } } } \\ & \right) + \underbrace { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { \tau _ { k } \in \mathbb { N } } ^ { \prime } \mu _ { x } a _ { i _ { 1 } i _ { 2 } l } ( x - b _ { i , 2 } ) \rho ( \frac { \| \mathcal { D } _ { j } ( \psi ) - e _ { i _ { 1 } i _ { 2 } } \| } { \varepsilon _ { j } ^ { * } } ) \rho \left( \frac { \| \mathcal { D } _ { j } ( \psi ) - e _ { i _ { 1 } i _ { 2 } } \| } { \varepsilon _ { j } ^ { * } } \right) } _  \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^  \end{array}
$$

where ${ \widetilde { \beta } } _ { X } = \alpha _ { X } + { \frac { \alpha _ { X } } { \alpha _ { Y } } }$ ,

$$
G _ { k , i _ { 2 } } ( z , x ) = \sum _ { s = 0 } ^ { j } \sum _ { \psi \in \widetilde { \Psi } _ { s } ^ { d _ { Y } } } \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D _ { X } } } { | l | < \beta _ { X } } } g _ { k , i _ { 2 } , s , \psi , l } ( x - b _ { i _ { 2 } } ) ^ { l } \cdot \psi ( z )
$$

where the parameters satisfy that $g _ { k , i _ { 2 } , s , \psi , l } \in [ - C _ { 1 } , C _ { 1 } ] ^ { D _ { Y } } , v _ { k , i _ { 2 } , s , \psi , l } \in [ - C _ { 1 } , C _ { 1 } ] , a _ { i _ { 1 } i _ { 2 } l } \in [ - C _ { 1 } , C _ { 1 } ] .$ $a _ { i _ { 1 } i _ { 2 } l } \in [ - C _ { 1 } n , C _ { 1 } n ] ,$ , $e _ { i _ { 1 } i _ { 2 } } \in [ 0 , 2 ] ^ { D _ { Y } + 1 }$ , and $\{ b _ { 1 } , b _ { 2 } , \cdot \cdot \cdot , b _ { W _ { j } ^ { \prime } } \} \subset \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( { \bf 0 } , L _ { 1 } )$ are $\varepsilon _ { j } ^ { x } -$ separated. It holds for any $S \in S _ { j } ^ { \dagger }$ that

$$
\operatorname* { s u p } _ { \psi \in \Psi _ { j } ^ { D _ { Y } x \in \mathcal { M } _ { X } } } | S ( \psi , x ) | \leq C _ { 1 } 2 ^ { - \frac { d _ { Y } j } { 2 } } .
$$

Moreover, for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in { \mathcal { M } } _ { X } , S ( \psi , x )$ will be non-zero only if there exist $i _ { 1 } \in [ W _ { j } ]$ and $i _ { 2 } \in [ W _ { j } ^ { \prime } ]$ so that $\| x - \bar { b _ { i _ { 2 } } } \| < 2 \varepsilon _ { j } ^ { x }$ and $| \mathcal { T } _ { j } ( \psi ) - e _ { i _ { 1 } i _ { 2 } } | < 2 \varepsilon _ { j } ^ { y }$ . Given that the set $\{ b _ { 1 } , b _ { 2 } , \cdots , b _ { W _ { j } ^ { \prime } } \}$ are $\varepsilon _ { j } ^ { x }$ -separated, for any $x \in \mathcal { M } _ { X }$ , there are $\mathcal { O } ( 1 )$ number of $i _ { 2 } \in [ W _ { j } ^ { \prime } ]$ so that $\lVert x - b _ { i _ { 2 } } \rVert < 2 \dot { \varepsilon } _ { j } ^ { x }$ . Moreover, for any $i _ { 2 } \in [ W _ { j } ^ { \prime } ]$ and $i _ { 1 } \in [ W _ { j } ]$ , there are at most constant number of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ so that $| \mathcal { T } _ { j } ( \psi ) - e _ { i _ { 1 } i _ { 2 } } | < 2 \varepsilon _ { j } ^ { y }$ . Therefore, for any $x \in \mathcal { M } _ { X }$ , there are $\mathcal { O } ( W _ { j } ) = \mathcal { O } ( 2 ^ { d _ { Y } j } )$ number of $\psi \in \Psi _ { j } ^ { D _ { Y } }$ so that $S ( \psi , x ) \neq 0$ , and thus

$$
\sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbf { 1 } ( S ( \psi , x ) \neq 0 ) \leq C 2 ^ { d _ { Y } j } .
$$

Furthermore, consider $S , S ^ { \prime } \in \mathcal { S } _ { j } ^ { \dagger }$ with

$$
\begin{array} { r l } & { \mathrm { S i g s } _ { 2 } \lesssim - T _ { G _ { 2 } \leq \frac { 2 d } { 2 } } \Big ( } \\ &  \begin{array} { r l } &  \sum _ { u = 1 } ^ { \boldsymbol { N } _ { 1 } } \sum _ { u = 1 } ^ { \boldsymbol { N } _ { 2 } } \sum _ { u = 1 } ^ { \boldsymbol { N } _ { 1 } } \sum _ { u = 1 } ^ { \boldsymbol { N } _ { 2 } } ( \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . . } { \sum } } \big ( \underset { \mathrm { R } ^ { u } = 1 } { \overset { . . . } { \sum } } \big ) \underset  \mathrm  \end{array} \end{array}
$$

and

$$
\begin{array} { r l } & { \quad \sqrt { ( \dot { \tau } _ { \mathrm { C , A } } ) } = \displaystyle - \sum _ { \vec { \tau } _ { \mathrm { C , B } } = 1 } ^ { N _ { B } } \sum _ { \vec { \tau } _ { \mathrm { C , B } } \neq \vec { \tau } _ { \mathrm { A } } } \Big ( \int _ { 0 } ^ { \tau _ { \mathrm { C , B } } } \gamma _ { \tau } ^ { \mathrm { a d d } } \gamma _ { \tau } ^ { \mathrm { a d } } \frac { \dot { \sigma } _ { \mathrm { C , B } } ^ { \mathrm { a d } } } { \tau _ { \mathrm { C , B } } ^ { \mathrm { a d } } } \psi ( \dot { \tau } _ { \mathrm { C , B } } ^ { \mathrm { a d } } / \sigma _ { \mathrm { C , B } } ^ { \mathrm { a d } } ) \big ) \xi _ { \boldsymbol { \xi } _ { \boldsymbol { \xi } _ { \boldsymbol { \xi } _ { \boldsymbol { \xi } _ { \boldsymbol { \xi } } } } } } \Delta \rho _ { \boldsymbol { \xi } } \big [ \frac { 1 - K _ { B } ^ { 2 } } { \hbar \sigma _ { \mathrm { C , B } } ^ { \mathrm { a d } } } \big ] \mu _ { \boldsymbol { \xi } } ^ { \frac { \gamma _ { \mathrm { A } } ( \tau _ { \mathrm { C , B } } ^ { \mathrm { a d } } ) } { \tau _ { \mathrm { C , B } } ^ { \mathrm { a d } } } - \frac { \lambda _ { \tau } } { 2 } } \big ] } \\ &  \quad \sum _ { \vec { \tau } _ { \mathrm { A } } = 1 } ^ { N _ { B } } \sum _ { \vec { \tau } _ { \mathrm { B } } = 1 } ^ { N _ { B } } \sum _ { \vec { \tau } _ { \mathrm { B } } = 1 } ^ { N _ { B } } \sum _ { \vec { \tau } _ { \mathrm { B } } = 1 } ^ { N _ { B } } \sum _ { \vec { \tau } _ { \mathrm { B } } = 1 } ^ { N _ { B } } \frac  \big ( \mathrm { d } _ { \vec { \tau } _ { \mathrm { B } } } ^ { \tau _ { \mathrm { A } } } / \sigma _  \mathrm  C \end{array}
$$

It holds for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathcal { M } _ { X }$ that,

$$
\begin{array} { r l } & { S ( \psi , x ) - S ^ { \prime } ( \psi , x ) | } \\ & { \lesssim \ j 2 ^ { \frac { j \hat { a } \psi _ { \gamma } } { 2 } + j } \ast \operatorname* { s u p } _ { i \in \{ W _ { j } ^ { 1 } \} k \in \{ k ^ { 1 } \} s \in \{ s , d \} ^ { \nu } } \ \displaystyle \sum _ { \mathrm { \normalfont { ~ t e } } \in \{ s , d \} ^ { \nu } } \ \| g _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } ^ { \prime } - g _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } | \| } \\ & { \qquad + j 2 ^ { \frac { j \hat { a } \psi _ { \gamma } } { 2 } + j } \ \operatorname* { s u p } _ { i \not \in \{ W _ { j } ^ { 1 } \} k \in \{ k ^ { 1 } \} s \in \{ s , d \} ^ { \nu } } \ \displaystyle \sum _ { \mathrm { \normalfont { ~ t e } } \in \{ s , d \} ^ { \nu } } \ \| s \gamma _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } - v _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } | | } \\ & { \qquad + j 2 ^ { \frac { j \hat { a } \psi _ { \gamma } } { 2 } + j } \ \underset { i \not \in \{ W _ { j } ^ { 1 } \} k \in \{ k ^ { 1 } \} } { \operatorname* { s u p } } \ \underset { \forall i \in \{ s , d \} ^ { \nu } } { \operatorname* { s u p } } \ \underset { \mathrm { \normalfont { ~ t e } } \in \{ s , d \} ^ { \nu } } { \operatorname* { s u p } } \ \underset { \mathrm { \normalfont { ~ t e } } \in \{ s , d \} ^ { \nu } } { \operatorname* { s u p } } \ \| \gamma _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } ^ { \prime } - v _ { k , i _ { 2 } , s , \tilde { \psi } _ { \downarrow } } | | } \\ &  \qquad + \displaystyle \operatorname* { m a x } _  i _ { 1 } \in \{ W _ { j } ^ { 1 } \} , i _  \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } { \mathcal { A } ( S , S ^ { * } ) - } & { \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \Bigg [ \displaystyle \sum _ { \sigma \in S ^ { \prime } } \big ( S ( S ( S , \sigma ) - S ^ { * } ( \sigma ) , z ) \big ) ^ { 2 } } \\ & { \leq \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \Bigg [ \displaystyle \sum _ { \sigma \in S ^ { \prime } } \big ( S ( S ( S , \sigma ) - S ^ { * } ( \sigma ) , z ) \big ) ^ { 2 } ( \| S ( \sigma , z ) \| ^ { 2 } + \| S ^ { * } ( \sigma , z ) \| ^ { 2 } + \| ) } \\ & { \leq \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \Bigg [ \displaystyle \sum _ { \sigma \in S ^ { \prime } } \big ( S ( S , \sigma ) - S ^ { * } ( \sigma ) , z \big ) ^ { 2 } ( \| S ( \sigma , z ) \| ^ { 2 } \big ) } \\ & { \leq 2 \sigma ^ { 2 } \Bigg ( \displaystyle \int _ { ( ( 0 , 0 ) ) ^ { 2 } } ^ { \mathcal { \sigma \sigma \in S } } \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \displaystyle \sum _ { \sigma \in S ^ { \prime } } \big | U _ { \mathcal { N } ( \sigma , z ) , z \in \mathcal { N } _ { \sigma } ( \mathcal { N } ) } ^ { \prime } - U _ { \mathcal { N } ( \sigma , z ) , z \in \mathcal { N } _ { \sigma } ( \mathcal { N } ) } \big | \Big ] } \\ &  + \displaystyle \frac { \partial ^ { 2 } \sigma ^ { 2 } } { \partial x ^ { 2 } } \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \operatorname* { s u p } _ { x \in \mathcal { N } ( \mathcal { N } ) } \sum _ { \sigma \in S ^ { \prime } } \big | \big | U _ { \mathcal { N } ( \mathcal { N } ) } ^ { \prime } - U _  \mathcal { N } ( \sigma , z ) , z \in \mathcal { N } _ { \sigma } \end{array}
$$

Then, using the fact that the $\varepsilon$ -covering number of a $d$ -dimensional ball with radius $R$ is being bounded by $\big ( \frac { 3 R } { \varepsilon } \big ) ^ { d }$ , we have for any $\begin{array} { r } { 0 < \varepsilon \le \operatorname* { s u p } _ { S , S ^ { \prime } \in S _ { j } ^ { \dagger } } d _ { S } ( S , S ^ { \prime } ) , } \end{array}$ ,

$$
\log \mathbf { N } ( S _ { j } ^ { \dagger } , d _ { S } , \varepsilon ) \lesssim 2 ^ { j d _ { Y } } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } } \log \frac { n } { \varepsilon } .
$$

Then by Lemma 16, it holds with probability larger than $\textstyle 1 - { \frac { 1 } { n ^ { 2 } } }$ that for any $j \in [ J ]$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - \widehat { S } _ { j } ^ { \dag } ( \psi , X ) \big ) ^ { 2 } \Big ] \lesssim \frac { \log n } { n } 2 ^ { j d _ { Y } } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } } } \\ & { \qquad + \displaystyle \operatorname* { m i n } _ { S \in \mathcal { S } _ { j } ^ { \dag } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - S ( \psi , X ) \big ) ^ { 2 } \Big ] . } \end{array}
$$

Next, we bound the approximation error $\begin{array} { r } { \operatorname* { m i n } _ { S \in S _ { j } ^ { \dag } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } ( \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( Y ) ] - S ( \psi , X ) ) ^ { 2 } \Big ] . } \end{array}$ Consider a $\tau _ { 2 }$ -covering set $\{ ( x _ { k } ^ { \ast } , y _ { k } ^ { \ast } ) \} _ { k = 1 } ^ { K ^ { \ast } } \subset \mathcal { M }$ of $\mathcal { M }$ , by Lemma 6, we can write

$$
\Sigma _ { \mu _ { Y | x } ^ { * } } \big [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) \big ] = \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathfrak { g } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z , x \in \mathcal { M } _ { X } , \psi \in \Psi _ { j } ^ { D _ { Y } } .
$$

where $G _ { [ k ] } ^ { \ast } \in \mathcal { H } _ { L _ { 1 } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ , $v _ { [ k ] } ^ { \ast } \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } \big ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } \big )$ . Moreover, for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ and $x \in \mathcal { M } _ { X } , v _ { [ k ] } ^ { * } ( z , x )$ is zero if $\lVert x - x _ { k } ^ { * } \rVert \geq 2 \tau _ { 2 }$ or $\| G _ { [ k ] } ^ { * } ( z , x ) - y _ { k } ^ { * } \| \ge 2 \tau _ { 2 }$ . Fix a $j \in \{ 0 \} \cup [ J ]$ and let $\mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ be the largest $\varepsilon _ { j } ^ { x }$ -packing set of $\mathcal { M } _ { X }$ . Then for any $k \in [ K ^ { * } ]$ and $\boldsymbol { x } ^ { * } \in \mathbb { R } ^ { D _ { \boldsymbol { X } } }$ , we define $G _ { [ k ] , x ^ { * } } ^ { \dagger } ( \cdot , \cdot )$ and $v _ { [ k ] , x ^ { * } } ^ { \dag } ( \cdot , \cdot )$ as follows.

1. If $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { i } ^ { x } } ^ { x }$ , and $\| x ^ { * } - x _ { k } ^ { * } \| \leq \tau _ { 2 } + 2 \varepsilon _ { j } ^ { x }$ , then considering the following local approximation to $G _ { [ k ] } ^ { * }$ and $v _ { [ k ] } ^ { \ast }$ :

$$
G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) = \sum _ { s = 0 } ^ { j } \sum _ { \psi \in \widetilde { \mathbb { V } } _ { s } ^ { d _ { Y } } } \sum _ { \begin{array} { l } { \vert \in \mathbb { N } _ { 0 } ^ { D _ { X } } } \\ { \vert \vert < \beta _ { X } } \end{array} } \int _ { \mathbb { R } ^ { d _ { Y } } } \frac { 1 } { l ! } G _ { [ k ] } ^ { * ( \mathbf { 0 } , l ) } ( t , x ^ { * } ) ( x - x ^ { * } ) ^ { l } \psi ( t ) \mathrm { d } t \cdot \psi ( z )
$$

and

$$
v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) = \sum _ { s = 0 } ^ { j } \sum _ { \psi \in \widetilde { \mathbb { W } } _ { s } ^ { d _ { Y } } } \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D } X } { | l | < \alpha _ { X } } } \int _ { \mathbb { R } ^ { d _ { Y } } } \frac { 1 } { l ! } v _ { [ k ] } ^ { * ( \mathbf { 0 } , l ) } ( t , x ^ { * } ) ( x - x ^ { * } ) ^ { l } \psi ( t ) \mathrm { d } t \cdot \psi ( z ) ,
$$

where recall $\widetilde { \Psi } _ { s } ^ { d _ { Y } } = \{ \psi \in \overline { { \Psi } } _ { s } ^ { d _ { Y } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) \neq \emptyset \}$ , and we use $G ^ { ( \mathbf { 0 } , l ) } ( { \boldsymbol { z } } , { \boldsymbol { x } } )$ to denote the partial derivative of $G ( z , \cdot )$ of order $l$ evaluated at $x$ . It holds that

$$
\begin{array} { r l } & { \underset { \leq t \leq \frac { 2 } { \epsilon } \leq k _ { 1 } , \mathcal { K } ^ { ( \epsilon , 1 ) } } { \operatorname* { s u p } } \| \mathcal { C } _ { | \mathbb { H } , \epsilon } ^ { 1 } ( z , x ) - \mathcal { C } _ { | \mathbb { H } | } ^ { s } ( z , x ) \| } \\ & { = \epsilon ^ { s } \mathrm { s u } _ { \mathcal { K } } \{ \alpha ^ { * , 2 } \epsilon _ { 5 } ^ { 2 } \} } \\ & { \leq \underset { s \in \mathbb { Z } _ { s } } { \operatorname* { s u p } } \underset { ( s ^ { \epsilon , 1 } \leq t ) _ { 2 } ^ { s } } { \operatorname* { s u p } } \| \underset { s = 0 } { \overset { j } { \sum } } \displaystyle \sum _ { \mathfrak { v } \in \tilde { \mathcal { V } } _ { \mathfrak { K } ^ { \epsilon } } ^ { \epsilon } } \int _ { \mathbb { R } ^ { 4 \nu } } \mathcal { C } _ { | \mathbb { H } | } ^ { s } ( t , x ) \psi ( t ) \mathrm { d } t \cdot \psi ( z ) - \mathcal { C } _ { | \mathbb { H } | } ^ { s } ( z , x ) \| } \\ & { \overset { x \geq 2 } s _ { \mathcal { K } _ { 1 } , \mathcal { K } ^ { ( \epsilon , 2 ) } \leq \frac { 1 } { 2 ^ { \alpha } \beta } } \eta } \\ & { + \underset { s \in \mathbb { R } _ { \mathcal { K } ^ { \epsilon } } \{ 0 , 1 , \epsilon ^ { * } \} } { \operatorname* { s u p } } \| \mathcal { C } _ { | \mathbb { H } , \epsilon } ^ { 1 } ( z , x ) - \displaystyle \sum _ { s = 0 } ^ { j } \sum _ { \mathfrak { v } \in \tilde { \mathcal { V } } _ { \mathfrak { K } ^ { \epsilon } } ^ { \epsilon } } \int _ { \mathbb { R } ^ { 4 \nu } } \mathcal { C } _ { | \mathbb { H } | } ^ { s } ( t , x ) \psi ( t ) \mathrm { d } t \cdot \psi ( z ) \| } \\ & { \quad \lesssim \epsilon \Phi _ { M , X } \{ s ^ { \epsilon , 1 } \alpha ^ { * , 2 } \} } \\ &  \lesssim 2 ^ \end{array}
$$

and similarly,

$$
\operatorname* { s u p } _ { \substack { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } } \| v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) - v _ { [ k ] } ^ { * } ( z , x ) \| \lesssim 2 ^ { - j \alpha _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } .
$$

2. If $x ^ { * } \notin \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , or $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , but $\| x ^ { * } - x _ { k } ^ { * } \| > \tau _ { 2 } + 2 \varepsilon _ { j } ^ { x }$ , we define $G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \equiv \mathbf { 0 } _ { D _ { Y } }$ and $v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \overset { \cdot } { \equiv } 0 .$

Let $\mathbb { N } _ { c 2 ^ { - j } } ^ { z }$ be a $c 2 ^ { - j }$ -covering set of $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ , contained within $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ , where $c$ is a small enough positive constant. For any ${ \boldsymbol { x } } ^ { * } \in { \mathcal { M } } _ { X }$ , denote

$$
\begin{array} { r l } & { \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) = \{ \psi \in \Psi _ { j } ^ { D _ { Y } } : \exists { z ^ { * } } \in \mathbb { N } _ { c 2 ^ { - j } } ^ { z } , k \in [ K ^ { * } ] , l \in \mathbb { N } _ { 0 } ^ { D _ { Y } } \mathrm { ~ w i t h ~ } | l | \leq \lfloor \widetilde { \beta } _ { X } \rfloor } \\ & { \qquad \mathrm { s o ~ t h a t ~ s u p p } ( \psi ^ { ( l ) } ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) , C 2 ^ { - j } ) \neq \emptyset \} , } \end{array}
$$

where into su $C$ is a large enough constant. Thenmation of a term that depend on following lemma that decompose and a polynomial term. $\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) ]$ $G _ { [ k ] , x ^ { * } } ^ { \dagger } , v _ { [ k ] , x ^ { * } } ^ { \dagger }$

Lemma 19. There exist constants $C _ { 1 } , C _ { 2 }$ such that for any $x ^ { \ast } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , $\psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } }$ , there exists coefficients $a _ { \psi ^ { \ast } , x ^ { \ast } , s } ^ { \ast } \in ( - C _ { 1 } n , C _ { 1 } n )$ indexed by $s \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ with $s \leq \lfloor \widetilde { \beta } _ { X } \rfloor ^ { 2 } + \lfloor \alpha _ { X } \rfloor$ , satisfying the following conditions:

1. It holds for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$ that

$$
\begin{array} { r l } & { \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \geq d \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { \gamma } - D _ { \gamma } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z } \\ & { \displaystyle - \left( \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) ) v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \mathrm { d } z + \sum _ { \stackrel { \delta \in \mathbb { N } _ { 0 } ^ { D } X } { 0 \leq s \leq [ \tilde { \beta } _ { X } ] ^ { 2 } + | \alpha _ { X } | } } a _ { \psi ^ { * } , x ^ { * } , s } ^ { * } ( x - x _ { 0 } , \tau _ { 1 } ) \mathrm { d } z \right) } \\ & { \leq C _ { 2 } \left( \log n \right) \cdot 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } . } \end{array}
$$

2. If $\psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } \setminus \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } )$ , then it holds for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , \varepsilon _ { j } ^ { x } )$ and $x ^ { \prime } \in \mathbb { B } _ { \mathbb { N } _ { \varepsilon _ { j } ^ { x } } } ( x , 2 \varepsilon _ { j } ^ { x } )$ that,

$$
\sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z = 0
$$

and

$$
\sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { \gamma } - D _ { \gamma } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ) ) v _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ) \mathrm { d } z + \sum _ { \substack { s \in \mathbb { N } _ { 0 } ^ { D } X } \atop \mathbf { 0 } \leq s \leq \lfloor \widetilde { \beta } _ { X } \rfloor ^ { 2 } + \lfloor \alpha _ { X } \rfloor } a _ { \psi ^ { * } , x ^ { \prime } , s } ^ { * } ( x - x ^ { \prime } ) ^ { s } = 0
$$

The proof of Lemma 19 is provided in Appendix D.14. Then since ${ \mathcal { I } } _ { j }$ is $c 2 ^ { - j }$ separated, let $c ^ { \prime } = c / 2$ , for any $\iota , \iota ^ { \prime } \in \mathcal { S } _ { j }$ , $\rho \big ( \frac { | \iota - \iota ^ { \prime } | } { c ^ { \prime } 2 ^ { - j } } \big ) \ \ne 0$ if and only if $\iota = \iota ^ { \prime }$ . Applying Lemma 19, for any $\psi \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathcal { M } _ { X }$ , if $\begin{array} { r } { \sum _ { x ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) \rho ( \frac { | \mathbb { Z } _ { j } ( \psi ) - \mathbb { Z } _ { j } ( \psi ^ { * } ) | } { c ^ { \prime } 2 ^ { - j } } ) \geq 1 } \end{array}$ ( |Ij (ψ)−Ij (ψ∗)|′ −j ) ≥ 1, then

$$
\begin{array} { r l } & { \mathbb { E } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \rho \sim \rho } \sum _ { \ell = 1 } ^ { \infty } \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } ( \ell ^ { \star } , \ell ^ { \star } ) \Big ] = \xi _ { \nu \rho } \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big ] \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big ] \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big ] \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big ] } \\ & { = \mathbb { E } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big [ \mathcal { F } _ { \rho \sim \rho } ^ { \lambda } \xi _ { \nu \rho } \Big ] \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } ^ { \lambda } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } \xi _ { \nu \rho } } \\ &  \quad \times \frac  \sum _ { \ell = 1 } ^ { \infty } \eta _ { \ell } \sum _ { \ell = 1 } ^ { \infty } \end{array}
$$

On the other hand, if $\begin{array} { r } { \sum _ { x ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) \rho ( \frac { | \mathcal { D } _ { j } ( \psi ) - \mathcal { D } _ { j } ( \psi ^ { * } ) | } { c ^ { \prime } 2 ^ { - j } } ) < 1 } \end{array}$ . Since $\mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ is the largest $\varepsilon _ { j } ^ { x }$ -packing of $\mathcal { M } _ { X }$ , there exists $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ so that $\| x - x ^ { * } \| \leq \varepsilon _ { j } ^ { x }$ and $\begin{array} { r } { \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) = 1 } \end{array}$ . Moreover, since

$$
\sum _ { * \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) \rho ( \frac { | \mathcal { D } _ { j } ( \psi ) - \mathcal { D } _ { j } ( \psi ^ { * } ) | } { c ^ { \prime } 2 ^ { - j } } ) \leq \sum _ { x ^ { * } \in \mathbb { R } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) \rho ( \frac { | \mathcal { D } _ { j } ( \psi ) - \mathcal { D } _ { j } ( \psi ^ { * } ) | } { c ^ { \prime } 2 ^ { - j } } )
$$

it holds that $\psi \in \Psi _ { j } ^ { D _ { Y } } \setminus \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } )$ . Therefore,

$$
\sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z = 0 ,
$$

and for any $x ^ { \prime } \in \mathbb { B } _ { \mathbb { N } _ { \varepsilon _ { j } ^ { x } } } ( x , 2 \varepsilon _ { j } ^ { x } )$

$$
\sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { \gamma } - D _ { \gamma } ) } { 2 } \psi ( G _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ) ) v _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ) \mathrm { d } z + } \sum _ { \substack { s \in \mathbb { N } _ { 0 } ^ { D } X } \atop \mathbf { 0 } \leq s \leq [ \tilde { \mathcal { B } } _ { X } ] ^ { 2 } + [ \alpha _ { X } ] } a _ { \psi , x ^ { \prime } , s } ^ { * } ( x - x ^ { \prime } ) ^ { s } = 0
$$

Hence,

$$
\begin{array} { r l } & { \displaystyle \sum _ { i = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( 0 , \tau _ { i } ) } 2 ^ { \frac { j ( d \gamma - D _ { \gamma } ) } { 2 } \psi } \big ( G _ { [ k ] } ^ { * } ( z , x ) \big ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z = 0 } \\ & { = \frac { \sum _ { x ^ { * } \in \mathbb { R } _ { \xi _ { j } } ^ { n _ { c } } } \sum _ { \psi ^ { * } \in \mathbb { V } _ { j } ^ { D _ { \gamma } } ( x ^ { * } ) } \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( 0 , \tau _ { i } ) } 2 ^ { \frac { j ( d \gamma - D _ { \gamma } ) } { 2 } \psi } \big ( G _ { [ k ] , x ^ { * } } ^ { ( i ) } ( z , x ) \big ) v _ { [ k ] , x ^ { * } } ^ { \uparrow } ( z , x ) \mathrm { d } z \rho \big ( \frac { | \mathcal { X } - x ^ { * } | } { \xi _ { j } ^ { s } } \big ) \big ) _ { \mathscr { R } } } { \sum _ { x ^ { * } \in \mathbb { R } _ { \xi _ { j } } ^ { n _ { c } } } \sum _ { \psi ^ { * } \in \mathbb { V } _ { j } ^ { D _ { \gamma } } ( x ^ { * } ) } \rho \big ( \frac { | \mathcal { X } - x ^ { * } | } { \xi _ { j } ^ { s } } \big ) \rho \big ( \frac { | \mathcal { X } _ { j } ( \psi ) - \mathcal { X } _ { j } ( \psi ^ { * } ) | } { \xi _ { j } ^ { 2 } - \rho } \big ) \mathrm { d } \frac { 1 } { n ^ { 2 } } } } \\ &  + \frac  \sum _ { x ^ { * } \in \mathbb { R } _ { \xi _ { j } } ^ { n _ { c } } } \sum _  \psi ^ { * } \in \Psi _ { j } ^ { D _ { \gamma } } ( x ^ { * } \end{array}
$$

Let $W _ { j } ( x ^ { * } ) = | \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) |$ , we have $\begin{array} { r } { \operatorname* { m a x } _ { x ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } } W _ { j } ( x ^ { * } ) \leq W _ { j } = C _ { 3 } ( \varepsilon _ { j } ^ { y } ) ^ { - d _ { Y } } } \end{array}$ and $| \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | \le W _ { j } ^ { \prime } =$ $C _ { 2 } ( \varepsilon _ { j } ^ { x } ) ^ { - d _ { X } }$ when $C _ { 2 } , C _ { 3 }$ are sufficiently large. Let $\chi _ { j }$ be an arbitrary subset of $\mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \mathbf { 0 } , L _ { 1 } ) \backslash \cup _ { x \in \mathcal { M } _ { X } } \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x , 2 \varepsilon _ { j } ^ { x } )$ so that the points in $\chi _ { j }$ are $\varepsilon _ { j } ^ { x }$ -separated and $| \mathcal { X } _ { j } | ~ = ~ W _ { j } ^ { \prime } - | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } |$ (note that such a set $\chi _ { j }$ exist if $L _ { 1 }$ is sufficiently large). Arrange the points in $\mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ and $\chi _ { j }$ as $\mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } \ = \ ( x _ { j 1 } , x _ { j 2 } , \cdot \cdot \cdot , x _ { j | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | } )$ and $\mathcal { X } _ { j } = ( z _ { j 1 } , z _ { j 2 } , \cdot \cdot \cdot , z _ { j | \mathcal { X } _ { j } | } )$ , we denote

$$
\begin{array} { r } { x _ { j l } ^ { * } = \left\{ \begin{array} { l l } { x _ { j l } , } & { \mathrm { ~ f o r ~ } l \in \{ 1 , 2 , \cdots , | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | \} } \\ { z _ { j l _ { 1 } } \mathrm { ~ w i t h ~ } l _ { 1 } = l - | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | , } & { \mathrm { ~ f o r ~ } l \in \{ | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | + 1 , | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | + 2 , \cdots , W _ { j } ^ { \prime } \} . } \end{array} \right. } \end{array}
$$

Furthermore, denote $\Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) = ( \psi _ { j 1 } ^ { x ^ { * } } , \psi _ { j 2 } ^ { x ^ { * } } , \cdot \cdot \cdot , \psi _ { j W _ { j } ( x ^ { * } ) } ^ { x ^ { * } } )$ . We define

$$
e _ { j i _ { 1 } i _ { 2 } } ^ { * } = \left\{ \begin{array} { l l } { { \bar { \mathcal { L } } } _ { j } ( \psi _ { j i _ { 1 } } ^ { x _ { j i _ { 2 } } ^ { * } } ) , } & { \mathrm { i f ~ } i _ { 1 } \leq W _ { j } ( x _ { j i _ { 2 } } ^ { * } ) \mathrm { ~ a n d ~ } i _ { 2 } \leq | { \mathbb N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | } \\ { ( 2 , 2 , \cdots , 2 ) , } & { \mathrm { i f ~ } W _ { j } ( x _ { j i _ { 2 } } ^ { * } ) < i _ { 1 } \leq W _ { j } \mathrm { ~ o r ~ } i _ { 2 } > | { \mathbb N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | , } \end{array} \right.
$$

$$
c _ { j i _ { 1 } i _ { 2 } l } ^ { * } = \left\{ \begin{array} { l l } { a _ { \quad \nu _ { j i _ { 1 } } ^ { * } , x _ { j i _ { 2 } } ^ { * } , l } ^ { * } , } & { \mathrm { ~ i f ~ } i _ { 1 } \leq W _ { j } ( x _ { j i _ { 2 } } ^ { * } ) \mathrm { ~ a n d ~ } i _ { 2 } \leq | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | } \\ { \nu _ { j i _ { 1 } } ^ { * } , x _ { j i _ { 2 } } ^ { * } , l } & { \mathrm { ~ i f ~ } W _ { j } ( x _ { j i _ { 2 } } ^ { * } ) < i _ { 1 } \leq W _ { j } \mathrm { ~ o r ~ } i _ { 2 } > | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | , } \\ { 0 , } & { \mathrm { ~ i f ~ } W _ { j } ( x _ { j i _ { 2 } } ^ { * } ) < i _ { 1 } \leq W _ { j } \mathrm { ~ o r ~ } i _ { 2 } > | \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x } | , } \end{array} \right.
$$

and

$$
\begin{array} { r l } & { \tilde { v } _ { j } ^ { * } ( \psi , x ) = T _ { C _ { 1 2 } - \frac { d _ { \gamma _ { j } } } { 2 } } \Big ( } \\ &  + \frac { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } \setminus \{ 0 , T _ { 1 } \} } } 2 ^ { \frac { j ( d _ { \gamma } - D _ { \gamma } ) } { 2 } } \psi ( G _ { [ k ] , x _ { j _ { 2 } } ^ { * } } ^ { \dagger } ( z , x ) ) v _ { [ k ] , x _ { j _ { 2 } } ^ { * } } ^ { \dagger } ( z , x ) \mathrm { d } z \rho ( \frac { \| x - x _ { j _ { 1 } } ^ { * } \| } { \varepsilon _ { j } ^ { * } } ) \rho ( \frac { | Z _ { j } ( \psi ) - \varepsilon } { \varepsilon _ { j } ^ { * } } } \\ &  \xrightarrow { \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } } \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \rho ( \frac { \| x - x _ { j _ { 1 } } ^ { * } \| _ { \partial _ { \sigma } } } { \varepsilon _ { j } ^ { * } } ) \rho ( \frac { | Z _ { j } ( \psi ) - \varepsilon _ { j _ { 1 } } ^ { * } \| _ { \partial _ { \sigma } } } { \varepsilon _ { j } ^ { * } } ) + \frac { 1 } { n ^ { 2 } } } \\ &  + \frac  \sum _ { i _ { 1 } = 1 } ^ { W _ { j } } \sum _ { i _ { 2 } = 1 } ^ { W _ { j } ^ { \prime } } \sum _  \begin{array} { l }  \varepsilon _ { j _ { 1 } i _ { 2 } i } ^ { * } ( x - x _ { j _ { 1 } } ^ { * } ) \end{array} \end{array}
$$

Then for any $x \in \mathcal { M } _ { X }$ , denote

$$
\widetilde { \Psi } _ { j } ^ { D Y } ( x ) = \{ \psi \in \Psi _ { j } ^ { D _ { Y } } : \sum _ { x ^ { * } \in \mathbb { R } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { x } } ) \rho ( \frac { | \mathcal { T } _ { j } ( \psi ) - \mathcal { T } _ { j } ( \psi ^ { * } ) | } { c ^ { \prime 2 - j } } \ge 1 \} .
$$

We have $\mathrm { s u p } _ { x \in \mathcal { M } _ { X } } | \widetilde { \Psi } _ { j } ^ { D _ { Y } } ( x ) | = \mathcal { O } ( 2 ^ { j d _ { Y } } )$ and by (41), (42), it holds for any $\psi \in \Psi _ { j } ^ { D _ { Y } } \backslash \widetilde { \Psi } _ { j } ^ { D _ { Y } } ( x )$ that,

$$
\mathsf { E } _ { \mu _ { Y | x } ^ { \star } } [ 2 ^ { \frac { j ( d \chi - D _ { Y } ) } { 2 } } \psi ( y ) ] = \sum _ { k = 1 } ^ { K ^ { \star } } \int _ { \mathbb { B } _ { \mathsf { R } ^ { d _ { Y } } } ( \mathsf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( G _ { [ k ] } ^ { \star } ( z , x ) ) v _ { [ k ] } ^ { \star } ( z , x ) \mathrm { d } z = S _ { j } ^ { \star } ( \psi , x ) = 0 .
$$

Furthermore, since supx∈MX supψ∈ΨD $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \operatorname* { s u p } _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) ] \leq C _ { 1 } 2 ^ { - \frac { d _ { Y } j } { 2 } } } \end{array}$ , we can get for any $x \in$ $\mathcal { M } _ { X }$ and $\psi \in \Psi _ { j } ^ { D _ { Y } }$ ,

$$
\begin{array} { r l } & { \mathsf { f } _ { j } ^ { \mathsf { e } } ( \psi , x ) = } \\ & { = \frac { \sum _ { x ^ { * } \in \mathbb { R } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D } Y ( x ^ { * } ) } \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \varepsilon ^ { d } Y } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) ) v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \mathrm { d } z \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { * } } ) } { \sum _ { x ^ { * } \in \mathbb { R } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \rho ( \frac { \| x - x ^ { * } \| } { \varepsilon _ { j } ^ { * } } ) \rho ( \frac { \| \mathcal { E } _ { j } ( \psi ) - \mathcal { T } _ { j } ( \psi ^ { * } ) \| } { \varepsilon _ { j } ^ { * } - \varepsilon ^ { * } } ) \rho ( \frac { \| \mathcal { E } _ { j } ( \psi ) - \mathcal { T } _ { j } ( \psi ^ { * } ) \| } { \varepsilon _ { j } ^ { * } - \varepsilon ^ { * } } ) } + \frac { 1 } { n ^ { 2 } } }  \\ &  + \frac  \sum _ { x ^ { * } \in \mathbb { R } _ { \varepsilon _ { j } ^ { x } } ^ { x } } \sum _ { \psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } ) } \sum _ { \tau \in \mathbb { R } _ { 0 } ^ { D _ { X } } ( \tau ) } a _ { \psi ^ { * } , x ^ { * } , l } ^ { * } ( x - x ^ { * } ) ^ { l } \rho ( \frac  \ \end{array}
$$

Therefore, using bound (40), we have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { x } ^ { \nu } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { W } _ { j } ^ { N } } \big ( \mathbb { E } _ { \mu _ { x } ^ { \nu } | x } \big [ \frac { \mathcal { S } ^ { \alpha } ( \psi - D \gamma ) } { 2 } \psi ( y ) \big ] - S _ { j } ^ { \alpha } ( \psi , x ) \big ) ^ { 2 } \bigg ] } \\ & { = \mathbb { E } _ { \mu _ { x } ^ { \nu } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { W } _ { j } ^ { N } } \Big ( \displaystyle \sum _ { k = 1 } ^ { K ^ { \nu } } \int _ { \mathbb { E } _ { \mathbb { Z } ^ { d } \setminus \{ 0 , \tau \} } } 2 \frac { \mathcal { I } ( \mathcal { A } \gamma - D \gamma ) } { 2 } \psi ( G _ { | k | } ^ { \nu } ( z , x ) ) v _ { | k | } ^ { \ast } ( z , x ) \mathrm { d } z - S _ { j } ^ { \ast } ( \psi , x ) \Big ) ^ { 2 } \bigg ] } \\ & { = \mathbb { E } _ { \mu _ { x } ^ { \ast } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { W } _ { j } ^ { N } \times \{ x \} } \Big ( \displaystyle \sum _ { k = 1 } ^ { K ^ { \nu } } \int _ { \mathbb { B } _ { \mathbb { Z } ^ { d } \setminus \{ 0 , \tau \} } } 2 \frac { \mathcal { I } ( \mathcal { A } \gamma - D \gamma ) } { 2 } \psi ( G _ { | k | } ^ { \ast } ( z , x ) ) v _ { | k | } ^ { \ast } ( z , x ) \mathrm { d } z - S _ { j } ^ { \ast } ( \psi , x ) \Big ) ^ { 2 } \bigg ] } \\ &  \lesssim ( \log n ) ^ { 2 } \cdot ( \frac { c ^ { x } } { \xi } ) ^ { 2 \alpha x } 2 ^ { - j d y } \quad \underset { x \in A \times \mathbb { X } } { \times } | \tilde { \mathbb { V } } _ { j } ^ { D \gamma } ( x ) | \lesssim ( \log n ) ^ { 2 } \cdot ( \frac { c ^ { x } } { \xi ^ { 2 } } \end{array}
$$

which completes the proof.

# D.10 Proof of Lemma 15

We will use Lemma 17 to show the desired results. Denote

$$
\Psi _ { j } ^ { D _ { X } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { D _ { X } } : \operatorname { s u p p } ( \psi ) \cap \mathcal { M } _ { x } \neq \emptyset \} ,
$$

and consider the family

$$
\begin{array} { r l } & { \widetilde { \mathcal { G } } = \{ G ( z , x ) = \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) : } \\ & { | g _ { \psi _ { 1 } \psi _ { 2 } } | \le L _ { 1 } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } - ( ( j _ { 1 } \beta _ { Y } ) \vee ( j _ { 2 } \beta _ { X } ) ) } \mathrm { ~ f o r ~ } \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } , \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } \} , } \end{array}
$$

where $J _ { 1 } = \lceil \log _ { 2 } ( n ^ { - \frac { \cdot } { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } } } ) \rceil$ 1 , $J _ { 2 } = \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { X } + d _ { Y } \frac { \beta _ { X } } { \beta _ { Y } } } } ) \rceil$ . Since for any $z \in \mathbb { R } ^ { d _ { Y } }$ and $x \in \mathcal { M } _ { X }$ , it holds that

$$
\begin{array} { r l } & { \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \overline { { \Psi } } _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) } \\ & { \displaystyle = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) , } \end{array}
$$

we can obtain

$$
\begin{array} { r l } { | | \widehat { V } _ { [ k ] } ) = } & { \underset { V \in \mathbb { Q } ( D _ { Y } , d _ { Y } ) } { \mathrm { a r g } \mathrm { m i n } } \frac { 1 } { | I _ { 1 } | } \displaystyle \sum _ { i \in I _ { 1 } } \| Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { k } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } } \\ { = } & { \underset { V \in \mathbb { Q } ( D _ { Y } , d _ { Y } ) } { \mathrm { a r g } \mathrm { m i n } } \frac { 1 } { | I _ { 1 } | } \displaystyle \sum _ { i \in I _ { 1 } } \| Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { k } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } } \end{array}
$$

Furthermore, since $\beta _ { Y } \ge 2$ , we have the following smoothness property for functions in $\widetilde { \mathcal G }$ , the proof of which is given in Appendix D.15.

Lemma 20. With the choice of $\widetilde { \mathcal G }$ in (43), there exists a constant $L _ { 1 }$ so that for any $G \in \widetilde { \mathcal { G } } , x \in \mathbb { R } ^ { D _ { X } }$ and $z \in \mathbb { R } ^ { d _ { Y } }$ ,

$$
\| J _ { G ( \cdot , x ) } ( z ) \| _ { F } \leq L _ { 1 } .
$$

Moreover, for any $1 ~ < ~ \beta ~ < ~ 2$ , there exists a constant $L _ { \beta }$ so that for any $G \in \widetilde { \mathcal { G } } , x \in \mathbb { R } ^ { D _ { X } }$ and $z , z ^ { \prime } \in \mathbb { R } ^ { d _ { Y } }$

$$
\| J _ { G ( \cdot , x ) } ( z ) - J _ { G ( \cdot , x ) } ( z ^ { \prime } ) \| _ { F } \leq L _ { \beta } \| z - z ^ { \prime } \| ^ { \beta - 1 } .
$$

Moreover, we can derive the following lemma that control the covering number of $\widetilde { \mathcal G }$ .

Lemma 21. With the choice of $\widetilde { \mathcal G }$ in (43), there exists a constant $C _ { 1 }$ so that for any $0 ~ < ~ \gamma _ { 1 } ~ \leq ~ 1$ ,   
the $\varepsilon$ -covering number $\mathbf { N } ( \widetilde { \mathcal { G } } , \dot { d } _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon )$ of $\widetilde { \mathcal G }$ with respect to the $d _ { \infty } ^ { \gamma _ { 1 } }$ distance, defined as $d _ { \infty } ^ { \gamma _ { 1 } } ( G _ { 1 } , G _ { 2 } ) =$ sup $\lVert G _ { 1 } ( z , x ) - G _ { 2 } ( z , x ) \rVert ^ { \gamma _ { 1 } }$ , satisfies   
$z \in \mathbb { R } ^ { d _ { Y } } , x \in \mathbb { R } ^ { D _ { X } }$

$$
\begin{array} { r l } & { \mathrm { o g } \mathbf { N } ( \widetilde { \mathcal { G } } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) } \\ & { \leq \left\{ \begin{array} { r l } { \quad C _ { 1 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } \log \left( \frac { C _ { 1 } ( J _ { 1 } + J _ { 2 } ) 2 ^ { - \frac { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } { \varepsilon ^ { \frac { 1 } { 7 } } } - \frac { ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) } { 2 } } } { \varepsilon ^ { \frac { 1 } { 7 } } \mathbf { 1 } } \lor 1 \right) } & { \mathrm { ~ \frac { d _ { Y } } { \beta _ { 1 } } ~ } } \\ { \quad C _ { 1 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } \log \left( \frac { C _ { 1 } ( ( J _ { 1 } + J _ { 2 } ) \land c ( \beta _ { Y } , \beta _ { X } , d _ { Y } , d _ { X } , \gamma _ { 1 } ) ) 2 ^ { - ( ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) ) } } { \varepsilon ^ { \frac { 1 } { 7 1 } } s _ { j _ { 1 } j _ { 2 } } } \lor 1 \right) } & { \mathrm { ~ \frac { d _ { Y } } { \beta _ { 1 } } ~ } } \end{array} \right. } \end{array}
$$

$$
\begin{array} { r } { ( \beta _ { Y } , \beta _ { X } , d _ { Y } , d _ { X } , \gamma _ { 1 } ) = \frac { 2 ^ { \frac { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } - 2 \beta _ { Y } \gamma _ { 1 } } { 4 \gamma _ { 1 } } } } { 2 ^ { \frac { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } - 2 \beta _ { Y } \gamma _ { 1 } } { 4 \gamma _ { 1 } } } - 1 } + \frac { 2 ^ { \frac { d _ { X } + d _ { Y } \beta _ { X } / \beta _ { Y } - 2 \beta _ { X } \gamma _ { 1 } } { 4 \gamma _ { 1 } } } } { 2 ^ { \frac { d _ { X } + d _ { Y } \beta _ { X } } { 4 \gamma _ { 1 } } - 2 \beta _ { X } \gamma _ { 1 } } } a n d s _ { j _ { 1 } j _ { 2 } } = \sqrt { \frac { 2 ^ { \frac { d _ { Y } + 1 + d _ { X } j _ { 2 } } { 2 \gamma _ { 1 } } - ( j _ { 1 } + d _ { X } ) / 2 } - ( j _ { 1 } + d _ { Y } ) } { 2 ^ { \frac { d _ { Y } - 1 + d _ { X } j _ { 2 } } { 2 \gamma _ { 1 } } - ( j _ { 1 } + d _ { Y } ) / 2 } - 1 } } . } \end{array}
$$

The proof of Lemma 21 is provided in Appendix D.16. Then we can bound the integral $\begin{array} { r } { \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( \widetilde { \mathcal { G } } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) } \mathrm { d } \varepsilon . } \end{array}$ When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } } \end{array}$ , we have

$$
\begin{array} { r l } &  \frac { 1 } { \sqrt { N } } \displaystyle \int _ { 0 } ^ { \infty } \sqrt { \log \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } } \frac { \sqrt { \log ( \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } - \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } ) } } { \sqrt { N } } \displaystyle \sum _ { \lambda = \frac { 1 } { \sqrt { N } } , \lambda = \frac { \lambda } { \sqrt { N } } , \lambda = \frac { \lambda } { \sqrt { N } } } \\ & { \le \frac { 1 } { \sqrt { N } } \displaystyle \int _ { 0 } ^ { \infty } \sqrt { \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) - \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } } \log ( \frac { \delta f _ { 4 , \xi } ( \lambda + \frac { \lambda f _ { 4 , \xi } } { \log ( \lambda ) } - \frac { \delta f _ { 4 , \xi } ( \lambda ) + \log ( \lambda ) + \log ( \lambda ) } { \le ( \lambda ) } ) } { \sqrt { N } } } ) \displaystyle \sum _ { \lambda = \frac { 1 } { \sqrt { N } } } \operatorname { d i v i d e } \delta ( \lambda ) d \lambda } \\ & { \le \frac { 1 } { \sqrt { N } } \displaystyle \frac { \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } } { \log ( \lambda ) - \log ( \lambda ) } \displaystyle ( \log ( \frac { \delta f _ { 4 , \xi } ( \lambda ) + \frac { \lambda f _ { 4 , \xi } } { \log ( \lambda ) } - \frac { \delta f _ { 4 , \xi } ( \lambda ) + \log ( \lambda ) } { \sqrt { N } } } { \varepsilon } ) ) \displaystyle 2 \operatorname { d i v i d e } \delta ( \lambda ) d \lambda ^ { \prime } } \\ &  \le \frac { 1 } { \sqrt { N } } \displaystyle \frac { \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) - \frac { \delta f _ { 4 , \xi } } { \log ( \lambda ) } } }  \rho - \frac { \lambda f _ { 4 , \xi } } { \sqrt { N } } \end{array}
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } } \end{array}$ , we have

$$
\begin{array} { r l } & { \frac { 1 } { \sqrt { n } } \displaystyle \int _ { 0 } ^ { \infty } \sqrt { \log \log ( \tilde { \phi } , d \hat { x } _ { \perp } ^ { \perp } , e ) } \mathrm { d } \boldsymbol { \xi } } \\ &  \le \frac { 1 } { \sqrt { n } } \displaystyle \int _ { 0 } ^ { \infty } \sqrt  \frac { 1 } { \lambda - 1 } \sum _ { j = 0 } ^ { n } \log ( \frac { C _ { 1 } ( ( J , 1 + J _ { j } ) , \boldsymbol { \hat { x } } _ { \perp } , \hat { x } _ { j } , \hat { x } _ { j } , d , x , \hat { x } _ { 1 } , \hat { y } _ { 1 } ) ) ^ { 2 - \frac { 1 } { 2 } ( j , j ) ( g , g , g ) ^ { \lambda } ( g , g , g ) ^ { \lambda } } { \nabla _ { 1 } ^ { 1 / 2 - \lambda } \sum _ { j = 0 } ^ { n } \log ( \frac { C _ { 1 } ( ( J , 1 + J _ { j } ) , \boldsymbol { \hat { x } } _ { \perp } , \hat { x } _ { j } , d , x , \hat { y } _ { 1 } ) ) ^ { 2 } } - \frac { 1 } { 2 } ( j , j ) ( g , g , g ) ^ { \lambda } ( g , g , g ) ^ { \lambda } ) } } { \delta ^ { \frac { 1 / 2 - \lambda } { \lambda } } \sum _ { j = 0 } ^ { n } \log ( \frac { C _ { 1 } ( ( J , 1 - J _ { j } ) , \boldsymbol { \hat { x } } _ { \perp } , \hat { x } _ { j } , d , y , \hat { x } _ { 1 } , d , x , \hat { y } _ { 1 } ) ) ^ { 2 - \frac { 1 } { 2 } ( j , j ) ( g , g , g ) ^ { \lambda } ( g , g , g ) ^ { \lambda } } { \nabla _ { 1 } ^ { 1 / 2 - \lambda } \sum _ { j = 0 } ^ { n } \log ( \frac { N _ { 1 } } { \lambda } ) } ) ^ { 2 n / g } } } \\ &  \le \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { \lambda = 0 } ^ { \frac { J } { \lambda } } \ \end{array}
$$

Then it remains to bound the term $\varepsilon ^ { * }$ in Lemma 17. Fix an arbitrary $k \in [ K ]$ . If $\mathbb { B } _ { \mathbb { R } ^ { D } X ^ { + D _ { Y } } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } ) \cap$ $\mathcal { M } = \emptyset$ , then $k \not \in { \widehat { \mathcal { K } } }$ . Otherwise, there exists $( x _ { k } ^ { * } , y _ { k } ^ { * } ) \in \mathbb { B } _ { \mathcal { M } } ( ( x _ { k } , y _ { k } ) , \sqrt { 2 } \tau _ { 2 } )$ . Let $V _ { [ k ] } ^ { * }$ be an arbitrary orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x _ { k } ^ { * } } } y _ { k } ^ { * }$ . Denote $Q _ { [ k ] } ^ { * } ( y ) = ( V _ { [ k ] } ^ { * } ) ^ { T } ( y - y _ { k } )$ and $G _ { [ k ] } ^ { * } ( z , x ) = \Phi _ { ( x _ { k } ^ { * } , y _ { k } ^ { * } ) } ( V _ { [ k ] } ^ { * } ( z +$ $( V _ { [ k ] } ^ { * } ) ^ { T } ( y _ { k } - y _ { k } ^ { * } ) ) , x )$ . Then there exists $\overline { { G } } _ { [ k ] } ^ { \ast } \in \mathcal { \overline { { H } } } _ { L } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ so that $\overline { { G } } _ { [ k ] } ^ { * } ( z , x )$ and $G _ { [ k ] } ^ { * } ( z , x )$ coincide within $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( ( V _ { [ k ] } ^ { * } ) ^ { T } ( y _ { k } ^ { * } - y _ { k } ) , \tau _ { 1 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { k } ^ { * } , \tau )$ . Moreover, for any $( x , y ) \in { \mathcal { M } }$ with $\| x - x _ { k } ^ { * } \| < \tau$ and $\lVert y - y _ { k } ^ { * } \rVert < \tau _ { 1 }$ , it holds that $y = \overline { { G } } _ { [ k ] } ^ { * } ( Q _ { [ k ] } ^ { * } ( y ) , x )$ . Then Let

$$
\vec { \mathfrak { x } } _ { [ k ] } ^ { \mathfrak { i } } ( z , x ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { \mathtt { b } } _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D } } g _ { [ k ] , \psi _ { 1 } , \psi _ { 2 } } ^ { * } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) , \quad g _ { [ k ] , \psi _ { 1 } , \psi _ { 2 } } ^ { * } = \int _ { \mathbb { R } ^ { D _ { X } } } \int _ { \mathbb { R } ^ { d _ { Y } } } \overline { { G } } _ { [ k ] } ^ { * } ( z , x ) \psi _ { 2 } ( x ) d \psi _ { 2 } ( x ) .
$$

It holds that G†[k] ∈ Ge. Moreover, by leveraging the wavelet approximation for HβY ,βX - smooth functions as described in Lemma 8, and setting $J _ { 1 } \ = \ \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { Y } + d _ { X } \frac { \beta _ { Y } } { \beta _ { X } } } } ) \rceil$ , $J _ { 2 } ~ = ~ \lceil \log _ { 2 } ( n ^ { - \frac { 1 } { d _ { X } + d _ { Y } \frac { \beta _ { X } } { \beta _ { Y } } } } ) \rceil$ and $\tau _ { 2 } < \frac { \tau _ { 1 } \wedge \tau } { 4 }$ , there exists a constant $C$ such that for any $x \in \mathbb { B } _ { M _ { X } } ( x _ { k } , 2 \tau _ { 2 } )$ and $z \in \mathbb { B } _ { R ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau _ { 2 } )$ ,

$$
\| G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { \dag } ( z , x ) \| \leq C \left( \log n \right) \cdot n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } .
$$

Therefore, for any $y \in \mathcal { M } _ { Y }$ with $\| y - y _ { k } \| \le 2 \tau _ { 2 }$ and $x \in \mathbb { B } _ { M _ { X } } ( x _ { k } , 2 \tau _ { 2 } )$ ,

$$
\begin{array} { r } { - G _ { [ k ] } ^ { \dagger } ( ( V _ { [ k ] } ^ { * } ) ^ { T } ( y - y _ { 0 } ) , x ) \Vert \leq \Vert y - G _ { [ k ] } ^ { * } ( Q _ { [ k ] } ^ { * } ( y ) , x ) \Vert + C \left( \log n \right) \cdot n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } = C \left( \log n \right) \cdot n ^ { - \frac { d _ { Y } } { \frac { d _ { Y } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } } } \end{array}
$$

Therefore, by Lemma 17, we can conclude that for any $\gamma _ { 1 } \in ( 0 , 1 ]$ , there exists a constant $C _ { \gamma _ { 1 } }$ so that it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ that for any $k \in { \widehat { \mathcal { K } } }$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot { \bf 1 } ( X \in \mathbb { B } _ { \mathbb { B } _ { X } } ( x _ { k } , 2 \tau _ { 2 } ) ) { \bf 1 } ( Y \in \mathbb { B } _ { \mathbb { B } _ { Y } } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq C _ { \gamma _ { 1 } } \left\{ \begin{array} { l l } { \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } , } \\ { \left( ( \log n \wedge \frac { 1 } { \beta _ { Y } ( d _ { Y } / \beta _ { Y } + d _ { X } / \beta _ { X } - 2 \gamma _ { 1 } ) } ) ^ { 1 + \gamma _ { 1 } } + ( \log n ) ^ { \gamma _ { 1 } } \right) \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

Then if $\begin{array} { r } { \frac { d _ { Y } } { 2 \beta _ { Y } } + \frac { d _ { X } } { 2 \beta _ { X } } > 1 } \end{array}$ , set $\gamma _ { 1 } = 1$ , it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ that for any $k \in { \widehat { \mathcal { K } } }$ ,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \lesssim ( \log n ) \cdot n ^ { - \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } } } } \end{array}
$$

Therefore, it holds with probability at least $\textstyle 1 - { \frac { c } { n ^ { 3 } } }$ that for any $k \in { \widehat { \mathcal { K } } }$ and any $\gamma _ { 1 } \in ( 0 , 1 ]$ that

$$
\begin{array} { r l } & { [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \quad \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \Big ) ^ { \gamma _ { 1 } } \lesssim ( \log n ) ^ { \gamma _ { 1 } } \ . } \end{array}
$$

If dY $\begin{array} { r } { \frac { d _ { X } } { 4 \beta _ { X } } + \delta _ { n } \cdot \lceil \log n \rceil \} } \end{array}$ $\frac { d _ { Y } } { 2 \beta _ { Y } } + \frac { d _ { X } } { 2 \beta _ { X } } < 1$ , let n  ⌈log n⌉  4βY  4βX  4βY  4β. Then by a union argument, it holds that with probability at least $\begin{array} { r } { \delta _ { n } = \frac { 1 - \frac { d _ { Y } } { 4 \beta _ { Y } } - \frac { d _ { X } } { 4 \beta _ { X } } } { \lceil \log n \rceil } } \end{array}$ and consider the set dX $\frac { d _ { Y } } { 4 \beta _ { Y } } + \frac { d _ { X } } { 4 \beta _ { X } } + \delta _ { n } , \cdot \cdot \cdot , \frac { d _ { Y } } { 4 \beta _ { Y } } +$ $1 - { \frac { c \log n } { n ^ { 3 } } }$ 4βY that for any $k \in { \widehat { \mathcal { K } } }$ and any $\gamma _ { 1 } \in \Gamma$ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { \lesssim \left\{ \begin{array} { l l } { \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } , } \\ { \Big ( ( \log n \wedge \frac { 1 } { \beta _ { Y } ( d _ { Y } / \beta _ { Y } + d _ { X } / \beta _ { X } - 2 \gamma _ { 1 } ) } ) ^ { 1 + \gamma _ { 1 } } + ( \log n ) ^ { \gamma _ { 1 } } \Big ) \cdot n ^ { - \frac { \gamma _ { 1 } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } . } \end{array} \right. } \end{array}
$$

Then under the above event, for any γ2 ∈ (0, 1] with γ2 < dY4βY , by setting $\begin{array} { r } { \gamma _ { 1 } = \frac { d _ { Y } } { 4 \beta _ { Y } } + \frac { d _ { X } } { 4 \beta _ { X } } } \end{array}$ , it holds that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 2 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \Big ( \mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \Big ) ^ { \gamma _ { 2 } / \gamma _ { 1 } } } \\ & { \lesssim ( \log n ) ^ { \gamma _ { 2 } } \cdot n ^ { - \frac { \gamma _ { 2 } } { 4 \gamma _ { 1 } } } = ( \log n ) ^ { \gamma _ { 2 } } \cdot n ^ { - \frac { \gamma _ { 2 } } { \frac { \gamma _ { 1 } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } . } \end{array}
$$

Moreover, for any $\begin{array} { r } { \gamma _ { 2 } \in [ \frac { d _ { Y } } { 4 \beta _ { Y } } + \frac { d _ { X } } { 4 \beta _ { X } } , } \end{array}$ 1], there exists $\gamma _ { 1 } \in \Gamma$ so that $\gamma _ { 1 } \leq \gamma _ { 2 } \leq \gamma _ { 1 } + \delta _ { n }$ , and therefore,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { \star } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 2 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq 2 L \mathbb { E } _ { \mu ^ { \star } } [ \| Y - \widehat { G } _ { [ k ] } ( \widehat { Q } _ { [ k ] } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D } Y } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \{ \begin{array} { l l } { ~ C _ { 1 } \frac { ( \log n ) ^ { 1 + \gamma _ { 1 } } } { \sqrt { n } } ~ } & { \frac { d _ { Y } } { \sqrt { n } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } , } \\ { C _ { 1 } \big ( ( \log n \wedge \frac { 1 } { \beta _ { Y } ( d _ { Y } / \beta _ { Y } + d _ { X } / \beta _ { X } - 2 \gamma _ { 1 } ) } \big ) ^ { 1 + \gamma _ { 1 } } + ( \log n ) ^ { \gamma _ { 1 } } \big ) \cdot n ^ { - \frac { \gamma _ { 1 } } { \frac { \beta _ { X } } { \beta _ { X } } + \frac { d _ { Y } ^ { \gamma } } { \beta _ { Y } } } } } & { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } . } \end{array}  } \\ &  \leq \{ \begin{array} { l l }  ~ C _ { 2 } \frac  ( \log n ) ^  1 \end{array} \end{array}
$$

This completes the proof for the first statement of Lemma 15 by combining all pieces. The second statement of Lemma 15 then directly follows from the second statement of Lemma 17.

# D.11 Proof of Lemma 16

The proof follows the pipeline of the proof of Lemma 11 and is included here for completeness. To show the result for a fixed $j \in [ J ]$ , we will use Theorem 8 with $\{ \psi _ { \lambda } ( \cdot ) \} _ { \lambda \in \Lambda } = \Psi _ { j } ^ { D _ { Y } }$ . Then we will verify the three assumptions in Theorem 8. For the first assumption, it holds for a constant $C _ { 1 }$ that

$$
\begin{array} { r l } & { \underset { ( x , y ) \in { \mathcal M } _ { S } \in { \mathcal S } _ { j } ^ { \dag } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } S ^ { 2 } ( \psi , x ) + | 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) S ( \psi , x ) | } \\ & { \le \underset { ( x , y ) \in { \mathcal M } _ { S } \in { \mathcal S } _ { j } ^ { \dag } } { \operatorname* { s u p } } \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } S ^ { 2 } ( \psi , x ) + C \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } | 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \psi ( y ) | \cdot 2 ^ { - \frac { d _ { Y } j } { 2 } } } \\ & { \le \underset { x \in { \mathcal M } _ { X } } { \operatorname* { s u p } } \left\{ \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \operatorname* { s u p } } | S ( \psi , x ) | ^ { 2 } \cdot \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } { \mathbf 1 } \big ( S ( \psi , x ) \neq 0 \big ) \right\} + C \underset { \psi \in \Psi _ { j } ^ { D _ { Y } } } { \sum } | 2 ^ { \frac { - D _ { Y } j } { 2 } } \psi ( y ) | \le C _ { 1 } . } \end{array}
$$

Then for the second assumption, we denote

$$
\ell ( x , y , S ) = \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } S ^ { 2 } ( \psi , x ) - 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } + 1 } \psi ( y ) S ( \psi , x ) .
$$

It holds for any $S , S ^ { \prime } \in S _ { j } ^ { \dagger }$ that

$$
\begin{array} { r l } & { \frac { 1 } { \Psi ^ { k } } \Big [ \big ( \{ ( X , Y , S ) - \ell ( X , Y , S ^ { \prime } ) \} ^ { 2 } \big ) \Big ] } \\ & { = \mathrm { R } _ { \mu ^ { k } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Theta _ { r } ^ { \mathcal { P } } } \big ( S ( \psi , X ) + S ^ { \prime } ( \psi , X ) - 2 ^ { j ( i \psi _ { r } - D \chi ) } + 1 _ { \psi ( Y ) } \big ) \cdot \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) \Big ) ^ { 2 } \Big ] } \\ & { \qquad \quad \forall \psi \in \Theta _ { r } ^ { \mathcal { P } } } \\ & { \leq 8 \mathrm { E } _ { \mu ^ { k } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Theta _ { r } ^ { \mathcal { P } } } 2 ^ { \frac { j ( i \psi - D \chi ) } { 2 } } \cdot 1 \cdot \psi ( Y ) \cdot \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) \Big ) ^ { 2 } \Big ] } \\ & { \qquad \quad + 2 \mathrm { R } _ { \mu ^ { k } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Theta _ { r } ^ { \mathcal { P } } } \big ( S ( \psi , X ) + S ^ { \prime } ( \psi , X ) \big ) \cdot \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) \Big ) ^ { 2 } \Big ] } \\ &  \leq 8 \mathrm { E } _ { \mu ^ { k } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Theta _ { r } ^ { \mathcal { P } } } 2 ^ { \frac { j ( i \psi - D \chi ) } { 2 } } \cdot \big | \psi ( Y ) \cdot \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) \Big ) ^ { 2 } \Big ] + 8 C ^ { 2 } \mathrm { R } _ { \mu ^ { k } } \Big [ \Big ( \displaystyle \sum _ { \psi \in \Theta _ { r } ^ { \mathcal { P } } } 2 ^ { - \frac { d \psi _ { r } ^ { \mathcal { P } } } { 2 } } \cdot \big  \end{array}
$$

Then notice that

$$
\begin{array} { r l } & { \mathbb { E } _ { \varphi ^ { * } } \bigg [ \bigg ( \displaystyle \sum _ { s \in \Psi _ { s } } 2 ^ { s ( k + \frac { \nu \beta \nu } { 2 } ) } \cdot \varphi ( Y ) \cdot \big ( S ( \psi _ { 1 } , X ) - S ^ { * } ( \psi _ { * } , X ) \big ) \bigg ) ^ { 2 } \bigg ] } \\ & { \quad = \mathbb { E } _ { \theta _ { 1 } ^ { * } } \bigg [ \displaystyle \sum _ { s \in \Psi _ { s } ^ { * } } \sum _ { \alpha \in \Psi _ { s } ^ { * } } 2 ^ { s ( k + \frac { \nu \beta \nu } { 2 } ) } \mathbb { E } _ { \theta _ { 1 } ^ { * } \cap \mathbb { R } _ { 1 } ^ { * } \cap \mathbb { R } _ { 1 } ^ { * } \cap \mathbb { P } _ { 2 } ( Y ) \backslash \mathbb { P } _ { 1 } ^ { * } } \big ( S ( \psi _ { 1 } , X ) - S ^ { * } ( \psi _ { 1 } , X ) \big ) \big ( S ( \psi _ { 2 } , \lambda ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \end{array}
$$

where we have used the fact that for any $x \in \mathcal { M } _ { X }$ ,

$$
\mathbb { E } _ { \mu _ { Y \mid x } ^ { * } } [ \psi _ { 1 } ( Y ) \psi _ { 2 } ( Y ) ] \lesssim \int _ { \mathcal { M } _ { Y \mid x } } \mathbf { 1 } ( y \in \mathrm { s u p p } ( \psi _ { 1 } ) \cap \mathrm { s u p p } ( \psi _ { 2 } ) ) 2 ^ { D _ { Y } j } u ^ { * } ( y \mid x ) \mathrm { d v o l } _ { \mathcal { M } _ { Y \mid x } } \lesssim 2 ^ { ( D _ { Y } - d _ { Y } ) }
$$

Moreover,

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { x } ^ { * } } \bigg [ \bigg ( \displaystyle \sum _ { \vartheta \in \mathbb { R } _ { j } ^ { D } } \sum ^ { - \frac { d _ { \gamma \lambda } } { 2 } } \big \cdot \big | S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big | \bigg ) ^ { 2 } \bigg ] } \\ & { = \mathbb { E } _ { \mu _ { x } ^ { * } } \bigg [ \Big ( \displaystyle \sum _ { \vartheta \in \mathbb { R } _ { j } ^ { D } } 2 ^ { - \frac { d _ { \gamma \lambda } } { 2 } } \cdot \big | S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big | \cdot \mathbf { 1 } \big ( S ( \psi , X ) \neq 0 \mathrm { o r } S ^ { \prime } ( \psi , X ) \neq 0 \big ) \Big ) ^ { 2 } \bigg ] } \\ & { \leq \mathbb { E } _ { \mu _ { x } ^ { * } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { R } _ { j } ^ { D } } 2 ^ { - d _ { \gamma } } \mathbf { 1 } \big ( S ( \psi , X ) \neq 0 \mathrm { o r } S ^ { \prime } ( \psi , X ) \neq 0 \big ) \cdot \displaystyle \sum _ { \psi \in \widehat { \mathbb { R } } _ { j } ^ { D } } \big ( S ( \psi , X ) - S ^ { \prime } ( \psi , X ) \big ) ^ { 2 } \bigg ] } \\ & { \leq 2 C \mathbb { E } _ { \mu _ { x } ^ { * } } ^ { \mathbb { E } } \bigg [ \displaystyle \sum _ { \psi \in \mathbb { R } _ { j } ^ { D } } \big ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) \big ) ^ { 2 } \Big ] . } \end{array}
$$

Therefore, it holds for some constant $C _ { 2 }$ that

$$
\big \| \ell ( x , y , S ) - \ell ( x , y , S ^ { \prime } ) \big \| _ { 2 } ^ { 2 } \leq C _ { 2 } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \psi \in \Psi _ { j } ^ { D _ { Y } } } \big ( S ( \psi , x ) - S ^ { \prime } ( \psi , x ) \big ) ^ { 2 } \Big ] ,
$$

which verifies the second assumption. For the last assumption, note that for any $S , S ^ { \prime } \in \mathcal { S } _ { j } ^ { \dagger }$ ,

$$
\begin{array} { r l } & { \displaystyle \tilde { I } _ { n } ( S , S ^ { \prime } ) } \\ & { = \sqrt { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \sum _ { s \in \Psi _ { s } ^ { \prime } } ( S ^ { 2 } ( \psi , X _ { i } ) - S ^ { \prime 2 } ( \psi , X _ { i } ) ) - 2 ^ { 2 ( d \psi - \frac { n } { 2 } ) } \mathbb { I } _ { 1 } \mathbb { I } _ { \psi } ( Y _ { i } ) \big ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) \big ) ) ^ { 2 } } } \\ &  \leq \sqrt { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { s \in \Psi _ { s } ^ { \prime \prime } } ( S ( \psi , X _ { i } ) + S ^ { \prime } ( \psi , X _ { i } ) - 2 ^ { \lambda ( d \psi - \frac { n } { 2 } ) + 1 } \psi ( Y _ { i } ) ) ^ { 2 } \cdot \sum _ { s \in \Psi _ { s } ^ { \prime \prime } } ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X } \\ & { \leq C _ { 3 } 2 ^ { \frac { d \psi - \frac { n } { 2 } } { 2 } } \lceil \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \sum _ { s \in \Psi _ { s } ^ { \prime \prime } } ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) ) ^ { 2 }  } \\ & { \leq  C _ { 3 } 2 ^ { \frac { d \psi - \frac { n } { 2 } } { 2 } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( S ( \psi , X _ { i } ) - S ^ { \prime } ( \psi , X _ { i } ) ) ^ { 2 }  } \\ & { \leq  C _ { 3 } 2 ^ { \frac { d \psi - \frac { n } { 2 } } { 2 } } d _ { 3 } ( S , S ^ { \prime } ) . } \end{array}
$$

Then, using the fact that $\begin{array} { r } { \log \mathbf { N } ( \mathcal { S } _ { j } ^ { \dagger } , d ^ { S } , \varepsilon ) \leq \mathcal { W } _ { j } \log ( \frac { n } { \varepsilon } ) } \end{array}$ , there exists a constant we have for any $0 < \varepsilon \le$ $\mathrm { s u p } _ { S , S ^ { \prime } \in S _ { j } ^ { \dagger } } d _ { n } ( S , S ^ { \prime } ) .$ ,

$$
\begin{array} { r } { \log \mathbf { N } ( \mathcal { S } _ { j } ^ { \dagger } , d _ { n } , \varepsilon ) \leq \mathcal { W } _ { j } \log \frac { C _ { 3 } n \cdot 2 ^ { d _ { Y } J / 2 } } { \varepsilon } \leq 2 \mathcal { W } _ { j } \log \frac { n } { \varepsilon } . } \end{array}
$$

The desired result is obtained by setting $W _ { n } = 2 \mathcal { W } _ { j }$ and $T _ { n } = n$ in Theorem 8, and applying a union bound over $j \in [ J ]$ .

# D.12 Proof of Lemma 17

Denote $\widehat { Q } ( y ) = \widehat { V } ^ { T } ( y - y _ { 0 } )$ , it holds that

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| Y _ { i } - \widehat { G } ( \widehat { Q } ( Y _ { i } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) } \\ & { = \displaystyle \operatorname* { m i n } _ { V \in \mathbb { Q } ( D _ { Y } , d _ { Y } ) } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| Y _ { i } - G ( V ^ { T } ( Y _ { i } - y _ { 0 } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) } \\ & { < ( \mathbf { \sigma } ^ { * } \mathbf { 1 } ^ { 2 } } \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| Y _ { i } - \widehat { G } ( \widehat { Q } ( Y _ { i } ) , X _ { i } ) \| ^ { \gamma _ { 1 } } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) } \\ & { \displaystyle \leq \Big ( \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \| Y _ { i } - \widehat { G } ( \widehat { Q } ( Y _ { i } ) , X _ { i } ) \| ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) \Big ) ^ { \frac { \gamma _ { 1 } } { 2 } } \leq ( \varepsilon ^ { * } ) ^ { \gamma _ { 1 } } } \end{array}
$$

Define the class

$$
{ \mathcal { F } } = \{ f ( x , y ) = \| y - G ( V ^ { T } ( y - y _ { 0 } ) , x ) \| ^ { \gamma _ { 1 } } : G \in { \mathcal { G } } , V \in \mathbb { O } ( D _ { Y } , d _ { Y } ) \} .
$$

Then we have $\| y - { \widehat { G } } ( { \widehat { Q } } ( y ) , x ) \| ^ { \gamma _ { 1 } } \in { \mathcal { F } }$ . Moreover, It is straightforward to verify that for any $\beta \in$ $( 1 , \beta _ { Y } )$ , there exists a constant $L$ so that for any $G \in \mathcal G$ , and $x \ \in \ \mathcal { M } _ { X }$ , it holds that $G ( \cdot , x ) \in$ $\mathcal { H } _ { L , D _ { Y } } ^ { \beta } ( \mathbb { R } ^ { d _ { Y } } )$ . Then for any $G _ { 1 } , G _ { 2 } \in \mathcal { G } , V _ { 1 } , V _ { 2 } \in \mathbb { O } ( D _ { Y } , d _ { Y } )$ , and $( x , y ) \in { \mathcal { M } }$ where $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { k } , 2 \tau _ { 2 } )$ and $\boldsymbol { y } ^ { \bullet } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( \boldsymbol { y } _ { k } , 2 \tau _ { 2 } )$ , it holds that

$$
\begin{array} { r l } & { \Big | \| y - G _ { 1 } \big ( V _ { 1 } ^ { T } ( y - y _ { k } ) , x \big ) \| ^ { \gamma _ { 1 } } - \| y - G _ { 2 } \big ( V _ { 2 } ^ { T } ( y - y _ { k } ) , x \big ) \| ^ { \gamma _ { 1 } } \Big | } \\ & { \leq \| G _ { 1 } \big ( V _ { 1 } ^ { T } ( y - y _ { k } ) , x \big ) - G _ { 2 } \big ( V _ { 2 } ^ { T } ( y - y _ { k } ) , x \big ) \| ^ { \gamma _ { 1 } } } \\ & { \leq \underset { z \in \mathbb { R } ^ { d _ { Y } } , x \in \mathcal { M } _ { X } } { \operatorname* { s u p } } \| G _ { 1 } ( z , x ) - G _ { 2 } ( z , x ) \| ^ { \gamma _ { 1 } } + ( 2 L \tau _ { 2 } ) ^ { \gamma _ { 1 } } \| V _ { 1 } - V _ { 2 } \| _ { \mathrm { o p } } ^ { \gamma _ { 1 } } } \end{array}
$$

Consider the distance

$$
I _ { n } ( f , f ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( f ( X _ { i } , Y _ { i } ) - f ^ { \prime } ( X _ { i } , Y _ { i } ) ) ^ { 2 } \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) } .
$$

Using (44), we can bound the $\varepsilon$ -covering number $\mathbf { N } ( { \mathcal { F } } , d _ { n } , \varepsilon )$ of $\mathcal { F }$ with respect to $d _ { n }$ by

$$
\begin{array} { r l } & { { \bf N } ( { \mathcal F } , d _ { n } , \varepsilon ) \leq { \bf N } ( { \mathcal G } , d _ { \infty } ^ { \gamma _ { 1 } } , \frac { \varepsilon } { 2 } ) \cdot { \bf N } \Big ( { \mathbb O } ( D _ { Y } , d _ { Y } ) , \| \cdot \| _ { \mathrm { o p } } , \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } { 2 ^ { \frac { 1 } { \gamma _ { 1 } } + 1 } L \tau _ { 2 } } \Big ) } \\ & { \quad \quad \quad \leq { \bf N } ( { \mathcal G } , d _ { \infty } ^ { \gamma _ { 1 } } , \frac { \varepsilon } { 2 } ) \cdot ( \frac { C } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } ) ^ { D _ { Y } d _ { Y } } . } \end{array}
$$

Then by standard symmetrization and Dudley’s entropy integral bound (see for example, Wainwright [2019]), we can get that

$$
\begin{array} { r l } & { \mathbb { E } \left[ \underset { f \in \mathcal { F } } { \operatorname* { s u p } } \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } , Y _ { i } ) { \bf 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } \big ( x _ { 0 } , 2 \tau _ { 2 } \big ) \big ) { \bf 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } \big ( y _ { 0 } , 2 \tau _ { 2 } \big ) \big ) \right. } \\ & { \left. - \mathbb { E } _ { \mu ^ { * } } \big [ f ( X , Y ) { \bf 1 } \big ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } \big ( x _ { 0 } , 2 \tau _ { 2 } \big ) \big ) { \bf 1 } \big ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } \big ( y _ { 0 } , 2 \tau _ { 2 } \big ) \big ) \big ] \right| } \\ & { \leq \frac { C _ { 1 } } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \frac { \varepsilon } { 2 } ) } \mathrm { d } \varepsilon + \frac { C _ { 1 } } { \gamma _ { 1 } \sqrt { n } } . } \end{array}
$$

Then by Talagrand concentration inequality (see for example, Theorem 3.27 of Wainwright [2019]), there exists a constant $C _ { 2 }$ , such that it holds with probability at least $1 - n ^ { - 3 }$ that

$$
\begin{array} { r l } {  { \operatorname* { s u p } _ { f \in \mathcal { F } } \bigg | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } , Y _ { i } ) { \bf 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) \big ) { \bf 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) \big ) } \bigg | } \\ & { \quad - \mathbb { E } _ { \mu ^ { * } } [ f ( X , Y ) { \bf 1 } \big ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) \big ) { \bf 1 } \big ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) \big ) ] } \\ & { \quad \le C _ { 2 } \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty } \sqrt { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \frac { \varepsilon } { 2 } ) } \mathrm { d } \varepsilon + C _ { 2 } \sqrt { \frac { \log n } { n } } + \frac { C _ { 2 } } { \gamma _ { 1 } \sqrt { n } } . } \end{array}
$$

So by combining all pieces, it holds with probability at least $1 - n ^ { - 3 }$ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { s } } [ \| Y - \widehat { G } ( \widehat { V } ( Y - y _ { 0 } ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { = \mathbb { E } _ { \mu ^ { s } } [ \| Y - \widehat { G } ( \widehat { Q } ( Y ) , X ) \| ^ { \gamma _ { 1 } } \cdot \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq \underset { f \in \mathcal { F } } { \operatorname* { s u p } } \Big | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } f ( X _ { i } , Y _ { i } ) \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) } \\ & { - \mathbb { E } _ { \mu ^ { * } } \Big [ f ( X , Y ) \mathbf { 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) \Big ] \Big | + ( \varepsilon ^ { * } ) ^ { \gamma _ { 1 } } } \\ &  \lesssim \frac { 1 } { \sqrt { n } } \displaystyle \int _ { 0 } ^ { \infty } \sqrt  \log \mathbf { N } ( \mathcal { G }  \end{array}
$$

The proof of the first statement is complete. Then we show the second statement. Let $V ^ { * }$ be a $D _ { Y } \times d _ { Y }$ matrix whose column form an orthonormal basis of $T _ { \mathcal { M } _ { Y | x ^ { * } } } y ^ { * }$ . Denote $Q ^ { * } ( y ) = ( V ^ { * } ) ^ { T } ( y - y ^ { * } )$ and $G ^ { * } ( z , x ) = \Phi _ { ( x ^ { * } , y ^ { * } ) } ( V ^ { * } z , x )$ . Then $G ^ { \ast } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { \ast } , \tau ) )$ , and for any $( x , y ) \in { \mathcal { M } }$ with $\| x - x ^ { * } \| < \tau$ and $\| y - y ^ { * } \| < \tau _ { 1 }$ , we have $y = G ^ { * } ( Q ^ { * } ( y ) , x )$ . Moreover, define

$$
v ^ { * } ( z , x ) = u ^ { * } ( G ^ { * } ( z , x ) | x ) \cdot \sqrt { \operatorname * { d e t } ( J _ { G ^ { * } ( \cdot , x ) } ( z ) ^ { T } J _ { G ^ { * } ( \cdot , x ) } ( z ) ) } .
$$

Let $\alpha _ { 1 } = 1 \Lambda \alpha _ { Y }$ and $\alpha _ { 2 } = 1 \wedge \alpha _ { X } \wedge \alpha _ { Y } \wedge ( \alpha _ { Y } \beta _ { X } ) \wedge ( \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } )$ . It holds that $v ^ { \ast } \in \overline { { \mathcal { H } } } _ { L } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { \ast } , \tau ) )$ with a constant $L$ . Therefore, there exists a constant $L _ { 1 }$ so that for any $x ^ { \prime } , x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , \tau )$ and $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ ,

$$
\| v ^ { * } ( z , x ) - v ^ { * } ( z ^ { \prime } , x ^ { \prime } ) \| \leq L _ { 1 } ( \| z - z ^ { \prime } \| ^ { \alpha _ { 1 } } + \| x - x ^ { \prime } \| ^ { \alpha _ { 2 } } ) .
$$

Moreover, there exists a constant $\tau _ { 3 } < \tau _ { 2 }$ so that when $\lVert x - x ^ { * } \rVert \leq \tau _ { 3 }$ and $\| z \| \leq \tau _ { 3 }$ ,

$$
\begin{array} { r } { \| G ^ { * } ( z , x ) - y _ { 0 } \| \leq \| G ^ { * } ( z , x ) - G ^ { * } ( \mathbf { 0 } , x ^ { * } ) \| + \| y ^ { * } - y _ { 0 } \| < 2 \tau _ { 2 } . } \end{array}
$$

Furthermore, since $\mu _ { Y | x ^ { * } } ^ { * } ( \mathbb { B } _ { \mathcal { M } _ { Y | x ^ { * } } } ( y ^ { * } , \tau _ { 3 } / 2 ) ) \ge g ( \tau _ { 3 } / 2 ) / L$ , it holds that

$$
\begin{array} { r l } & { g ( \tau _ { 3 } / 2 ) / L \le \mu _ { Y | x ^ { * } } ^ { * } ( \mathbb { B } _ { M _ { Y | x ^ { * } } } ( y ^ { * } , \tau _ { 3 } / 2 ) ) } \\ & { = \displaystyle \int _ { \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| G ^ { * } ( z , x ^ { * } ) - y ^ { * } \| < \tau _ { 3 } / 2 \} } v ^ { * } ( z , x ^ { * } ) \mathrm { d } z } \\ & { \le \displaystyle \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 3 } / 2 ) } v ^ { * } ( z , x ^ { * } ) \mathrm { d } z } \\ & { \le \displaystyle \operatorname* { m a x } _ { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 3 } / 2 ) } v ^ { * } ( z , x ^ { * } ) \frac { \pi ^ { d _ { Y } / 2 } } { ( d _ { Y } / 2 ) ! } ( \tau _ { 3 } / 2 ) ^ { d _ { Y } } . } \end{array}
$$

Therefore, there exists $\widetilde { z } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 3 } / 2 )$ so that $\begin{array} { r } { v ^ { * } ( \widetilde { z } , x ^ { * } ) \ge \frac { g ( \tau _ { 3 } / 2 ) ( d _ { Y } / 2 ) ! } { \pi ^ { d _ { Y } / 2 } ( \tau _ { 3 } / 2 ) ^ { d _ { Y } } L } = \tau _ { 4 } > 0 . } \end{array}$ . Then consider a small enough positive constant $\tau _ { 5 }$ that will be chosen later. When $\begin{array} { r } { \tau _ { 5 } < \frac { \tau _ { 3 } } { 2 } \wedge \big ( \frac { \tau _ { 4 } } { 4 L _ { 1 } } \big ) ^ { \frac { 1 } { \alpha _ { 1 } \wedge \alpha _ { 2 } } } } \end{array}$ , for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \widetilde { z } , \tau _ { 5 } )$ and $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , \tau _ { 5 } )$ , it holds that

$$
v ^ { * } ( z , x ) \leq L _ { 1 } \| z - \widetilde { z } \| ^ { \alpha _ { 1 } } + L _ { 1 } \| x - x ^ { * } \| ^ { \alpha _ { 2 } } + v ^ { * } ( \widetilde { z } , x ^ { * } ) \leq \frac { \tau _ { 4 } } { 2 } + v ^ { * } ( \widetilde { z } , x ^ { * } ) \leq \frac { 3 } { 2 } v ^ { * } ( \widetilde { z } , x ^ { * } )
$$

and

$$
v ^ { * } ( z , x ) \geq v ^ { * } ( \widetilde { z } , x ^ { * } ) - \frac { \tau _ { 4 } } { 2 } \geq \frac { v ^ { * } ( \widetilde { z } , x ^ { * } ) } { 2 } .
$$

Moreover, since $\mathbb { E } _ { \mu ^ { * } } [ \| Y - \widehat { G } ( \widehat { Q } ( Y ) , X ) \| \cdot { \mathbf { 1 } } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) { \mathbf { 1 } } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] \leq c$ , there exists a constant $C _ { 1 }$ so that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } ( \tilde { z } , \tilde { \tau } _ { 5 } ) } } \| G ^ { * } ( z , X ) - \widehat { G } ( \widehat { Q } ( G ^ { * } ( z , X ) ) , X ) \| ^ { 2 } \cdot { \bf 1 } ( X \in \mathbb { B } _ { M _ { X } } ( x ^ { * } , \tau _ { 5 } ) ) v ^ { * } ( z , X ) \mathrm { d } z \right] } \\ & { \leq \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } ( \widehat { Q } ( Y ) , X ) \| ^ { 2 } \cdot { \bf 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) { \bf 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \\ & { \leq C _ { 1 } \mathbb { E } _ { \mu _ { X } ^ { * } } \mathbb { E } _ { \mu _ { Y | X } ^ { * } } [ \| Y - \widehat { G } ( \widehat { Q } ( Y ) , X ) \| \cdot { \bf 1 } ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau _ { 2 } ) ) { \bf 1 } ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , 2 \tau _ { 2 } ) ) ] } \end{array}
$$

Define $\widehat { l } ( z , x ) = \widehat { G } ( \widehat { Q } ( G ^ { * } ( z , x ) ) , x )$ . Given that for any $x \in \mathcal { M } _ { X }$ , $\widehat { G } ( \cdot , x ) \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta } ( \mathbb { R } ^ { d _ { Y } } )$ with $\beta > 1$ and a constant $L$ , there exists a constant $L _ { 2 }$ such that for any $x \in B _ { \mathcal { M } _ { X } } ( x , \tau )$ and $z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ ,

$$
\begin{array} { r l } & { \| ( G ^ { * } ( z , x ) - \widehat { l } ( z , x ) ) - ( G ^ { * } ( \widetilde { z } , x ) - \widehat { l } ( \widetilde { z } , x ) + \big ( J _ { G ^ { * } ( \cdot , x ) } ( \widetilde { z } ) - J _ { \widehat { l } ( \cdot , x ) } ( \widetilde { z } ) \big ) ( z - \widetilde { z } ) ) \| } \\ & { \qquad \leq L _ { 2 } \| z - \widetilde { z } \| ^ { \beta \wedge 2 } . } \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { \quad \iota _ { \theta : \tilde { x } } ^ { * } \Big [ \int _ { \mathbb R _ { 0 } \tilde { x } ( \tilde { x } ^ { * } ; \mathbb R ^ { n } ) } \| G ^ { * } ( z , X ) - \hat { G } ( \hat { Q } ( G ^ { * } ( z , X ) ) , X ) \| ^ { 2 } \cdot v ^ { * } ( z , X ) \mathrm { d } z \cdot \boldsymbol 1 ( X \in \mathbb B _ { M _ { X } } ( x ^ { * } , \tau _ { \tilde { x } } ) ) \Big ] } \\ & { = \mathbb { E } _ { \mu _ { \tilde { x } } ^ { * } \times \mathbb R _ { 0 } } \cdot \operatorname* { s u p } _ { x \in \mathcal { S } ^ { * } , \mathbb { P } } \Big [ \int _ { \mathbb R _ { 0 } ^ { n } \mathcal { S } ^ { * } ( \tilde { x } ^ { * } ; \mathbb R ^ { n } ) } \| G ^ { * } ( z , X ) - \hat { T } ( z , X ) \| ^ { 2 } \cdot v ^ { * } ( z , X ) \mathrm { d } z \Big ] } \\ & { \leq \frac { 1 } { 4 } \mathbb { E } _ { \rho _ { \tilde { x } } ^ { * } \times \mathbb I _ { \mathcal H _ { M _ { X } } ( \tilde { x } ^ { * } ; \mathbb R ^ { n } ) } } \Big [ \int _ { \mathbb R _ { 0 } ^ { n } \mathcal { S } ( \tilde { \mathcal H _ { Q } } ) } \| G ^ { * } ( \tilde { z } , X ) - \hat { T } ( \tilde { z } , X ) + \big ( \int _ { \mathcal G ^ { * } ( \tilde { x } , X ) } ( \tilde { z } ) - \int _ { \tilde { T } _ { \tilde { \tau } } , \mathbb N } ( \tilde { z } ) \big ) ( z - \tilde { z } ) \| ^ { 2 } \mathrm { d } z \cdot } \\ &  \qquad - \frac { 3 \pi ^ { \tilde { d } ^ { 2 } \tilde { t } ^ { 2 } } } { 2 ( \tilde { d } ( \tilde { \mathcal { Y } } ^ { 2 } ) ) ^ { L } } L _ { 2 } \tau _ { 0 } ^ { 2 ( \tilde { y } \times \tilde { \mathcal { Z } } ) } v ^ { * } ( \ \end{array}
$$

where the last inequality uses the fact that for any $d$ -variate polynomial $\begin{array} { r } { \mathbf { S } ( y ) \ = \ \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } y ^ { j } } \end{array}$ , $\boldsymbol { y } \in \mathbb { R } ^ { d }$ , there exists some positive constant $C ( d , k )$ only depending on $( d , k )$ such that

$$
\int _ { \mathbb { B } _ { 1 } ^ { d } } \mathbf { S } ^ { 2 } ( y ) \mathrm { d } y \geq C ( d , k ) \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } ^ { 2 } .
$$

So combined with $\begin{array} { r } { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \tilde { z } , \tau _ { 5 } ) } \| G ^ { * } ( z , X ) - \widehat { G } ( \widehat { Q } ( G ^ { * } ( z , X ) ) , X ) \| ^ { 2 } \cdot { \mathbf 1 } ( X \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , \tau _ { 5 } ) ) v ^ { * } ( z , X ) \mathrm { d } z \Big ] \leq \mathbb { E } _ { \mu _ { X } } ( \tau _ { 5 } ) , } \end{array}$ $C _ { 1 } c$ , we can obtain

$$
\begin{array} { r l r } {  { \mathbb { E } _ { \mu _ { X } ^ { * } \mid _ { B _ { M _ { X } } } ( x ^ { * } , \tau _ { 5 } ) } \Big [ \| J _ { G ^ { * } ( \cdot , X ) } ( \widetilde { z } ) - J _ { \widehat { l } ( \cdot , X ) } ( \widetilde { z } ) \| _ { \mathrm { F } } ^ { 2 } \Big ] \leq \frac { C _ { 1 } c } { \tau _ { 5 } ^ { d _ { Y } + 2 } \tau _ { 4 } L _ { 3 } } } } \\ & { } & { \quad + \frac { 3 \pi ^ { d _ { Y } / 2 } L _ { 2 } } { 2 ( d _ { Y } / 2 ) ! L _ { 3 } } \tau _ { 5 } ^ { 2 ( \beta \wedge 2 ) - 2 } \mu _ { X } ^ { * } ( B _ { { \mathcal M } _ { X } } ( x ^ { * } , \tau _ { 5 } ) ) . } \end{array}
$$

Therefore there exists $\widetilde { \boldsymbol { x } } \in B _ { \mathcal { M } _ { \boldsymbol { X } } } ( \boldsymbol { x } ^ { * } , \tau _ { 5 } )$ , so that

$$
\Vert J _ { G ^ { * } ( \cdot , \widetilde { x } ) } ( \widetilde { z } ) - J _ { \widehat { l } ( \cdot , \widetilde { x } ) } ( \widetilde { z } ) \Vert _ { \mathrm { F } } ^ { 2 } \le \frac { C _ { 1 } c } { \tau _ { 5 } ^ { d _ { Y } + 2 } \tau _ { 4 } L _ { 3 } \mu _ { \mathrm { X } } ^ { * } ( B _ { \mathcal { M } _ { X } } ( x ^ { * } , \tau _ { 5 } ) ) } + \frac { 3 \pi ^ { d _ { Y } / 2 } L _ { 2 } } { 2 ( d _ { Y } / 2 ) ! L _ { 3 } } \tau _ { 5 } ^ { 2 ( \beta \wedge 2 ) - 2 } .
$$

Then notice that

$$
J _ { \widehat { l } ( \cdot , \widetilde { x } ) } ( \widetilde { z } ) = J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { \ast } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } J _ { G ^ { \ast } ( \cdot , \widetilde { x } ) } ( \widetilde { z } ) ,
$$

$$
\| J _ { G ^ { * } ( \cdot , \tilde { x } ) } ( \tilde { z } ) - V ^ { * } \| = \| J _ { G ^ { * } ( \cdot , \tilde { x } ) } ( \tilde { z } ) - J _ { G ^ { * } ( \cdot , x ^ { * } ) } ( \mathbf { 0 } ) \| \leq L ( \| \tilde { z } \| + \| \tilde { x } - x ^ { * } \| ^ { ( \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } ) \wedge 1 } ) ,
$$

and there exists a constant $L _ { 4 }$ so that for any $z \in \mathbb { R } ^ { d _ { Y } }$ and $x \in \mathbb { R } ^ { D _ { X } }$ ,

$$
J _ { \widehat { G } ( \cdot , x ) } ( z ) ^ { T } J _ { \widehat { G } ( \cdot , x ) } ( z ) \preceq L _ { 4 } I _ { d _ { Y } } .
$$

When $\tau _ { 3 } , \tau _ { 5 }$ and $c$ are small enough, it holds that

$$
\begin{array} { r l } & { \| V ^ { * } - J _ { \widehat { G } ( \cdot , \widehat { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widehat { x } ) ) ) \widehat { V } ^ { T } V ^ { * } \| _ { \mathrm { F } } } \\ & { \leq \| V ^ { * } - J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) \| _ { \mathrm { F } } + \| J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) - J _ { \widehat { U } ( \cdot , \widehat { x } ) } ( \widetilde { z } ) \| _ { \mathrm { F } } } \\ & { \qquad + \| J _ { \widehat { G } ( \cdot , \widehat { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widehat { x } ) ) ) \widehat { V } ^ { T } J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) - J _ { \widehat { G } ( \cdot , \widehat { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widehat { x } ) ) ) \widehat { V } ^ { T } V ^ { * } \| _ { \mathrm { F } } } \\ & { \leq \| V ^ { * } - J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) \| _ { \mathrm { F } } + \| J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) - J _ { \widehat { t } ( \cdot , \widehat { x } ) } ( \widehat { z } ) \| _ { \mathrm { F } } } \\ & { \qquad + \| J _ { \widehat { G } ( \cdot , \widehat { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widehat { x } ) ) ) \widehat { V } ^ { T } \| _ { \mathrm { o p } } \| J _ { G ^ { * } ( \cdot , \widehat { x } ) } ( \widehat { z } ) - V ^ { * } \| _ { \mathrm { F } } } \\ &  \leq ( 1 + \sqrt { L _ { 4 } } ) L _ { \left( \eta _ { 3 } / 2 \right) } + \tau _ { 5 } ^  ( \beta _ { X } - \frac { \delta _ { X } }  \beta _  Y \end{array}
$$

Therefore,

$$
\begin{array} { r l } & { \| I _ { d _ { Y } } - ( V ^ { * } ) ^ { T } \widehat { V } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) ^ { T } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } V ^ { * } \| _ { \mathrm { F } } } \\ & { = \| ( V ^ { * } ) ^ { T } V ^ { * } - ( V ^ { * } ) ^ { T } \widehat { V } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) ^ { T } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } V ^ { * } \| _ { \mathrm { F } } } \\ & { \leq \| ( V ^ { * } ) ^ { T } ( V ^ { * } - J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } V ^ { * } ) \| _ { \mathrm { F } } } \\ & { \qquad + \| ( V ^ { * } - J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } V ^ { * } ) ^ { T } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \widehat { V } ^ { T } V ^ { * } \| _ { \mathrm { F } } } \\ & { \leq \frac { 1 } { 2 } , } \end{array}
$$

which, combined with $J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) ^ { T } J _ { \widehat { G } ( \cdot , \widetilde { x } ) } ( \widehat { Q } ( G ^ { * } ( \widetilde { z } , \widetilde { x } ) ) ) \preceq L _ { 4 } I _ { d _ { Y } }$ can imply that

$$
( V ^ { * } ) ^ { T } \widehat { V } \widehat { V } ^ { T } V ^ { * } \succeq \frac { 1 } { 2 L _ { 4 } } I _ { d } ,
$$

and thus

$$
\widehat { V } ^ { T } P ^ { * } \widehat { V } = \widehat { V } ^ { T } V ^ { * } ( V ^ { * } ) ^ { T } \widehat { V } \succeq \frac { 1 } { 2 L _ { 4 } } I _ { d } .
$$

# D.13 Proof of Lemma 18

Consider

$$
G ( z ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } g _ { \psi _ { 1 } } \psi _ { 1 } ( z )
$$

and

$$
G ^ { \prime } ( z ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } g _ { \psi _ { 1 } } ^ { \prime } \psi _ { 1 } ( z ) .
$$

Then there exists a constant $C$ so that

$$
\begin{array} { r l } & { \displaystyle \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d _ { \mathcal { Y } } } } \| G ( z ) - G ^ { \prime } ( z ) \| } \\ & { \displaystyle = \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d _ { \mathcal { Y } } } } \Big \| \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { 2 \mathcal { Y } _ { 1 } } ^ { d _ { \mathcal { Y } } } } \left( g _ { \psi _ { 1 } } - g _ { \psi _ { 1 } } ^ { \prime } \right) \psi _ { 1 } ( z ) \Big \| } \\ & { \displaystyle \leq \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \operatorname* { m a x } _ { \psi _ { 1 } \in \Psi _ { 2 \mathcal { Y } _ { 1 } } ^ { d _ { \mathcal { Y } } } } \Big \| g _ { \psi _ { 1 } } - g _ { \psi _ { 1 } } ^ { \prime } \Big \| \cdot \displaystyle \operatorname* { s u p } _ { z \in \mathbb { R } ^ { d _ { \mathcal { Y } } } } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { 2 \mathcal { Y } _ { 1 } } ^ { d _ { \mathcal { Y } } } } | \psi _ { 1 } ( z ) \Big \| } \\ & { \displaystyle \leq C \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \operatorname* { m a x } _ { \psi _ { 1 } \in \Psi _ { 2 \mathcal { Y } _ { 1 } } ^ { d _ { \mathcal { Y } } } } \Big \| g _ { \psi _ { 1 } } - g _ { \psi _ { 1 } ^ { \prime } } \Big \| \cdot 2 ^ { \psi _ { 2 } } . } \end{array}
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } \leq 2 \gamma _ { 1 } } \end{array}$ , we have

$$
\sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } \leq ( J _ { 1 } + 1 ) \leq 2 J _ { 1 } .
$$

So if for any $j _ { 1 } \in [ J _ { 1 } ]$ and $\psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } }$ ,

$$
\left\| g _ { \psi _ { 1 } } - g _ { \psi _ { 1 } } ^ { \prime } \right\| \le \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } { 2 C J _ { 1 } } 2 ^ { \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } - \frac { d _ { Y } j _ { 1 } } { 2 } } ,
$$

then

$$
\operatorname* { s u p } _ { z \in \mathbb { R } ^ { d _ { Y } } } \| G ( z ) - G ^ { \prime } ( z ) \| ^ { \gamma _ { 1 } } \leq \Big ( C \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } { 2 C J _ { 1 } } 2 ^ { \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } \Big ) ^ { \gamma _ { 1 } } \leq \varepsilon .
$$

Therefore, we can get

$$
\begin{array} { l } { \displaystyle \nabla ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) \leq \prod _ { j = 0 } ^ { J _ { 1 } } \prod _ { \substack { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { \mathcal { I } _ { 1 } } } } \mathbf { N } ( [ - L _ { 1 } 2 ^ { - \frac { d _ { \gamma _ { j _ { 1 } } } } { 2 } - j _ { 1 } \beta _ { \gamma } } , L _ { 1 } 2 ^ { - \frac { d _ { \gamma _ { j _ { 1 } } } } { 2 } - j _ { 1 } \beta _ { \gamma } } ] ^ { D _ { \gamma } } , \frac { \varepsilon ^ { \frac { \gamma _ { 1 } } { \gamma _ { 1 } } } } { 2 C J _ { 1 } } ) ^ { \frac { d _ { \gamma _ { j _ { 1 } } } } { 2 } + j _ { \gamma _ { 1 } } - \frac { d _ { \gamma _ { 1 } } } { 2 } - \frac { d _ { \gamma _ { j _ { 1 } } } } { 2 } } , } \\ { \leq \displaystyle \prod _ { j = 0 } ^ { J _ { 1 } } \prod _ { \substack { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { \mathcal { I } _ { 1 } } } } \big [ \big ( \frac { 1 2 \sqrt { D _ { \gamma } } L _ { 1 } C J _ { 1 } 2 ^ { - \frac { d _ { \gamma _ { j _ { 1 } } } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { \gamma } } { 2 } } } { \varepsilon ^ { \frac { \gamma _ { 1 } } { \gamma _ { 1 } } } } \big ) ^ { D _ { \gamma } } \big ] \vee 1 } \\  \leq \displaystyle \prod _ { j = 0 } ^ { J _ { 1 } } \prod _ { \substack { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { \mathcal { I } _ { 1 } } } } \Big ( \frac  2 4 \sqrt { D _ { \gamma } } L _ { 1 } C J _ { 1 } 2 ^  - \frac { d _ { \gamma _ { j _ { 1 } } } } { 4 \gamma _ { 1 } } - \frac  j _ { 1 } \beta _  \end{array}
$$

Hence there exist constants $C _ { 1 } , C _ { 2 }$ so that for any $\begin{array} { r } { \gamma _ { 1 } \ge \frac { d _ { Y } } { 2 \beta _ { Y } } } \end{array}$ ,

$$
\log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) \leq C _ { 1 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { d _ { Y } j _ { 1 } } \log \left( \frac { C _ { 2 } J _ { 1 } 2 ^ { - \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } \vee 1 \right) .
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } > 2 \gamma _ { 1 } } \end{array}$ , denote

$$
s _ { j _ { 1 } } = \sqrt { \frac { 2 ^ { \frac { d _ { Y } j _ { 1 } } { 2 \gamma _ { 1 } } - j _ { 1 } \beta _ { Y } } } { 2 ^ { \frac { d _ { Y } J _ { 1 } } { 2 \gamma _ { 1 } } - J _ { 1 } \beta _ { Y } } } } .
$$

It holds that

$$
\begin{array} { l } { S = \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } s _ { j _ { 1 } } = \sqrt { \frac { 1 } { 2 ^ { \frac { d _ { Y } J _ { 1 } } { 2 \gamma _ { 1 } } } - J _ { 1 } \beta _ { Y } } } \cdot \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } } \\ { = \sqrt { \frac { 1 } { 2 ^ { \frac { d _ { Y } J _ { 1 } } { 2 ^ { \frac { d _ { Y } J _ { 1 } } { 2 \gamma _ { 1 } } } - J _ { 1 } \beta _ { Y } } } } } \cdot \frac { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) ( J _ { 1 } + 1 ) } { 4 \gamma _ { 1 } } } - 1 } { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) } { 4 \gamma _ { 1 } } } - 1 } } \\ { \leq J _ { 1 } \wedge \displaystyle \frac { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) } { 4 \gamma _ { 1 } } } } { 2 ^ { \frac { ( d _ { Y } - 2 \beta _ { Y } \gamma _ { 1 } ) } { 4 \gamma _ { 1 } } } - 1 } . } \end{array}
$$

So if for any $j _ { 1 } \in [ J _ { 1 } ]$ and $\psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } }$ ,

$$
\left\| g _ { \psi _ { 1 } } - g _ { \psi _ { 1 } } ^ { \prime } \right\| \leq \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } } } { C S } 2 ^ { - \frac { d _ { Y } j _ { 1 } } { 2 } } ,
$$

then

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { D _ { X } } } \| G ( z , x ) - G ^ { \prime } ( z , x ) \| ^ { \gamma _ { 1 } } \leq \Big ( C \sum _ { j _ { 1 } = 0 } ^ { J } \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } } } { C S } \Big ) ^ { \gamma _ { 1 } } = \varepsilon .
$$

Therefore, there exist constants $C _ { 1 } , C _ { 2 }$ so that for any $\begin{array} { r } { \gamma _ { 1 } \ge \frac { d _ { Y } } { 2 \beta _ { Y } } } \end{array}$

$$
\begin{array} { l } { \log \mathbb { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) \leq \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \log \mathbb { N } ( [ - L _ { 1 } 2 ^ { - \frac { d _ { Y _ { 2 } ^ { j _ { 1 } } } } { 2 } - j _ { 1 } \beta _ { Y } } , L _ { 1 } 2 ^ { - \frac { d _ { Y _ { 2 } ^ { j _ { 1 } } } } { 2 } - j _ { 1 } \beta _ { Y } } ] ^ { D _ { Y } } , \frac { \varepsilon ^ { \frac { 1 } { 7 1 } } s _ { j _ { 1 } } } { C S } 2 ^ { - \frac { d _ { Y _ { 2 } ^ { j _ { 1 } } } } { 2 } } , \| } \\ { \quad \quad \leq C _ { 1 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { d _ { Y } j _ { 1 } } \log \Big ( \frac { C _ { 2 } S 2 ^ { - j _ { 1 } \beta _ { Y } } } { \varepsilon ^ { \frac { 1 } { 7 1 } } s _ { j _ { 1 } } } \vee 1 \Big ) , } \end{array}
$$

which completes the proof.

# D.14 Proof of Lemma 19

Fix an $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , then for any $\psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$ , it holds that

$$
\begin{array} { r l } &  \begin{array} { r l } &  \displaystyle \sum _ { k = 1 } ^ { K ^ { n } } \int _ { \mathbb { R } _ { x ^ { n } } ( \Psi ( z , \tau ) ) } \frac { 2 ^ { n ( k - \tau ) } \log ^ { 2 } ( \tau ( \hat { C } _ { 1 } ^ { n } ( | z , \tau ) ) ) _ { k } ^ { n } ( \hat { x } _ { 1 } ^ { n } ( z , \tau ) ) + 2 - \frac { K ^ { n } } { \sum _ { k = 1 } ^ { K } } \int _ { \mathbb { R } _ { x ^ { n } } ( \tau ) \leq 0 } \eta ^ { 2 } \frac { 2 ^ { n ( k - \tau ) } \log ^ { 2 } ( \tau ( \hat { C } _ { 1 } ^ { n } ( | z , \tau ) ) ) _ { k } ^ { n } ( \hat { x } _ { 1 } ^ { n } ( z , \tau ) ) } { 1 - \sqrt { \pi } \log ^ { 2 } ( \tau ( \hat { C } _ { 1 } ^ { n } ( | z , \tau ) ) ) _ { k } ^ { n } ( \hat { x } _ { 1 } ^ { n } ( z , \tau ) ) + 2 } } \\ &  = \displaystyle \sum _ { k = 1 } ^ { K - \sum _ { k = 1 } ^ { K } } \int _ { \mathbb { R } _ { x ^ { k } } ( \tau ) \leq 0 } \int _ { 0 } ^ { \tau ( \hat { C } _ { 1 } ^ { n } ( | z , \tau ) ) _ { k } ^ { n } ( \hat { C } _ { 1 } ^ { n } ( \hat { C } _ { 1 } ^ { n } ( \hat { C } _ { 1 } ^ { n } ( z , \tau ) ) ) _ { k } ^ { n } ( \hat { C } _ { 1 } ^ { n } ( z , \tau ) ) + 2 \lambda ) \log ^ { 2 } ( \tau ( \hat { C } _ { 1 } ^ { n } ( | z , \tau ) ) ) _ { k } ^ { n } ( \hat { C } _ { 1 } ^ { n } ( z , \tau ) ) + 2 \lambda ) } \\ &  = \displaystyle \sum _ { k = 1 } ^ { K - \sum _ { k = 1 } ^ { K } } \int _ { 0 } ^ { \tau } \int _  \mathbb { R } _ { x ^ { k } } ( \end{array} \end{array}
$$

Let $I _ { \psi }$ be a rectangle on which $\psi$ is supported and $y _ { \psi }$ denote the center of $I _ { \psi }$ . Then for any $\psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } }$ , $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$ , and $k \in [ K ^ { * } ]$ with $\| x ^ { * } - x _ { k } ^ { * } \| \leq \tau _ { 2 } + 2 \varepsilon _ { j } ^ { x }$ , we have

$$
\begin{array} { r l } & { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) - \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) \neq 0 \} } \\ & { \leq \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) \neq 0 \} \cup \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) \neq 0 \} } \\ & { \leq \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| y _ { \psi ^ { * } } - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) \| < C 2 ^ { - j } \} \cup \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| y _ { \psi ^ { * } } - G _ { [ k ] } ^ { * } ( z , x ) \| } \\ & { \leq \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| y _ { \psi ^ { * } } - G _ { [ k ] } ^ { * } ( z , x ) \| < C _ { 1 } 2 ^ { - j } \} , } \end{array}
$$

where we have used the fact that

$$
\begin{array} { r l } { \| G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| \lesssim 2 ^ { - j \beta _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } } & { } \\ & { \lesssim 2 ^ { - 2 j } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } } \\ & { \lesssim 2 ^ { - 2 j } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } \left( 2 ^ { \frac { J d _ { Y } } { 2 \alpha _ { X } + d _ { X } } } ( \frac { n } { \log n } ) ^ { - \frac { 1 } { 2 \alpha _ { X } + d _ { X } } } \right) ^ { \frac { \alpha _ { X } } { \alpha _ { Y } } } } \\ & { \lesssim 2 ^ { - 2 j } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } 2 ^ { - J } } \\ & { \lesssim 2 ^ { - j } . } \end{array}
$$

Hence,

$$
\begin{array} { r l } & { \frac { \ d } { \ d t } \frac { \ d ^ { ( D _ { Y } - d _ { Y } ) } } { \ d t ^ { 2 } } \cdot ( E _ { A } ) = \underset { \lVert x ^ { * } - x _ { k } ^ { * } \rVert \le z _ { 2 } + 2 \varepsilon _ { j } ^ { * } } { \sum _ { \mathbb { I } \in \mathbb { R } ^ { + } \mathbb { I } } } \int _ { \mathbb { R } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } \left( \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) - \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) \right) \ b \nu _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) \mathrm { d } \tau } \\ & { = \underset { \lVert x ^ { * } - x _ { k } ^ { * } \rVert \le z _ { 2 } + 2 \varepsilon _ { j } ^ { * } } { \sum } \int _ { \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \lVert G _ { [ k ] } ^ { * } ( z , x ^ { * } ) - y _ { y } \ast \rVert \le C _ { 1 } \ge - j \} } \left( \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) - \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) \right) \ b \nu _ { [ k ] , } ^ { \dag } } \\ & { \lVert x ^ { * } - x _ { k } ^ { * } \rVert \le \tau _ { j } ^ { * } \le \varepsilon _ { j } ^ { * } } \end{array}
$$

Based on

$$
\operatorname* { s u p } _ { \substack { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } } \| G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| \lesssim 2 ^ { - j \beta _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ,
$$

and

$$
\operatorname* { s u p } _ { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( 0 , \tau _ { 1 } ) } \| v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) - v _ { [ k ] } ^ { * } ( z , x ) \| \lesssim 2 ^ { - j \alpha _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } ,
$$

we can verify that

$$
\begin{array} { r l } & { ( E _ { A } ) | } \\ & { \leq 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } \displaystyle \sum _ { \| x ^ { * } - x _ { x } ^ { * } \| \leq r _ { j } ^ { 1 } } \int _ { \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| G _ { [ k ] } ^ { * } ( z , x ^ { * } ) - y _ { \psi ^ { * } } \| \leq C _ { 1 } 2 ^ { - j } \} } | \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) - \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dagger } ( \mathbf { \Delta } } \\ & { \lesssim 2 ^ { \frac { d _ { Y } j } { 2 } + j } \displaystyle \sum _ { \| x ^ { * } \| \leq r _ { j } ^ { * } \| \leq r _ { j } ^ { * } } \int _ { \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) : \| G _ { [ k ] } ^ { * } ( z , x ^ { * } ) - y _ { \psi ^ { * } } \| \leq C _ { 1 } 2 ^ { - j } \} } \| G _ { [ k ] } ^ { * } ( z , x ) ) - G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \| \mathrm { d } z } \\ & { \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } } \cdot ( 2 ^ { - j ( \beta _ { Y } - 1 ) } + 2 ^ { j } \cdot \log n \cdot ( \epsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) . } \end{array}
$$

Let $\begin{array} { r } { \widetilde { \beta } _ { X } = \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ , using the Taylor’s theorem for $\psi ^ { * }$ , we have

$$
\begin{array} { l } { { \displaystyle \jmath ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) = \sum _ { \scriptstyle \imath \in \mathbb { N } _ { 0 } ^ { D } \gamma } \quad \frac { \psi ^ { * ( l ) } ( G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) } { l ! } ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } } } \\ { { \displaystyle \qquad \partial _ { 0 \leq \lfloor l \leq \lfloor \bar { \beta } _ { X } \rfloor } } } \\ { { \displaystyle + \sum _ { \scriptstyle \imath \in \mathbb { N } _ { 0 } ^ { D } \gamma } \quad \frac { | l | } { l ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { | \bar { \beta } _ { X } \rfloor } \psi ^ { * ( l ) } ( G _ { [ k ] } ^ { * } ( z , x ^ { * } ) + t ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ) \mathrm { d } t \cdot ( G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) } } \\ { { \displaystyle \qquad \operatorname * { \jmath } _ { \scriptstyle \imath \in [ \bar { \beta } _ { X } ] + 1 } } } \end{array}
$$

and

$$
\begin{array} { r l } & { \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) = \displaystyle \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D } Y } { \imath \in \mathbb { N } _ { 0 } ^ { D } Y } } \frac { \psi ^ { * ( l ) } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) ) } { l ! } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) ) ^ { l } } \\ & { \qquad + \displaystyle \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D } Y } { \imath \imath = [ k ] } } \frac { | l | } { l ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { | \tilde { \beta } _ { X } | } \psi ^ { * ( l ) } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) + t ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) ) ) \mathrm d \boldsymbol { t } } \\ & { \quad \overset { | \imath | } { \imath | = [ \tilde { \beta } _ { X } ] + 1 } } \\ & { \qquad \cdot ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) ) ^ { l } . } \end{array}
$$

Then we can obtain

$$
\begin{array} { r l } { \{ \mathbf { E } _ { 2 , 1 } : = } &  \displaystyle \sum _ { t = 0 } ^ { \infty } \int _ { \mathbb { R } _ { + } \mathbb { R } _ { + } \mathbb { R } _ { + } } ^ { \infty } \int _ { ( \mathbb { R } _ { + } \mathbb { R } _ { + } \mathbb { R } _ { + } ) \times ( \mathbb { R } _ { + } \mathbb { R } _ { + } ) ^ { 2 } \times ( 1 - \mathbb { R } _ { + } ) ^ { 2 } \times ( 1 - \mathbb { R } _ { + } ) ^ { 2 } \times \mathbb { R } _ { + } ^ { 2 } } \\ { \ : = } &  \ : - \frac { \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ) ) ) ^ { 2 } \mathrm { d } x _ { t } ^ { \infty } \mathrm { d } x _ { t } ^ { \infty } } \\ { \ : = } &  \ : - \frac { \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ) ) ) ^ { 2 } \mathrm { d } x _ { t } ^ { \infty } } \\ { \ : = } &  \ : - \frac  \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { t } ^ { t } ( \sum _ { t = 0 } ^ { \infty } \mathbb { E }  \end{array}
$$

We first bound the term $\left( E _ { C } \right)$ . Notice that

$$
\begin{array} { r l } & { \psi ^ { * ( l ) } ( G _ { [ k ] } ^ { * } ( z , x ^ { * } ) + t ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ) - \psi ^ { * ( l ) } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) + t ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ) } \\ & { \leq 2 ^ { \frac { D _ { Y } j } { 2 } } 2 ^ { j ( | l | + 1 ) } \cdot ( \| G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| + \| G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) \| ) } \\ & { \leq 2 ^ { \frac { D _ { Y } j } { 2 } } 2 ^ { j ( | \tilde { \beta } _ { X } | + 2 ) } ( 2 ^ { - j \beta _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) } \end{array}
$$

and

$$
\begin{array} { r } { | ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } | \lesssim \left\{ \begin{array} { c c } { ( \varepsilon _ { j } ^ { x } ) ^ { | l | } } & { \beta _ { X } \geq 1 } \\ { ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } | l | } } & { \beta _ { X } < 1 . } \end{array} \right. } \end{array}
$$

Using the conditions: $\beta _ { X } ~ \ge ~ \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } , \beta _ { Y } ~ \ge ~ \alpha _ { Y } + 1 , \alpha _ { Y } ~ \ge ~ \alpha _ { X }$ , and considering that for any j ∈ {0} ∪ [J] with J = ⌈ 12αY +dY +dX α $J = \lceil \frac { 1 } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } \cdot \log _ { 2 } ( \frac { n } { \log n } ) } \rceil$ , it holds that

$$
\begin{array} { l } { { 2 ^ { - j \alpha _ { Y } } \geq 2 ^ { - J \alpha _ { Y } } = ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \alpha _ { Y } } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } } } } \\ { { \ ~ = ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } ( \displaystyle \frac { n } { \log n } ) ^ { \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } - \frac { \alpha _ { Y } } { 2 \alpha _ { Y } + d _ { Y } + d _ { X } \frac { \alpha _ { Y } } { \alpha _ { X } } } } } } \\ { { \ ~ = ( \displaystyle \frac { n } { \log n } ) ^ { - \frac { \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } 2 ^ { { \frac { d _ { Y } \alpha _ { X } } { 2 \alpha _ { X } + d _ { X } } } } } } \\ { { \ ~ = ( \varepsilon _ { J } ^ { x } ) ^ { \alpha _ { X } } \geq ( \varepsilon _ { J } ^ { x } ) ^ { \alpha _ { X } } . } } \end{array}
$$

We can conclude, when $\beta _ { X } \geq 1$ ,

$$
\begin{array} { l } { \displaystyle E _ { C } \Big ( x \Big ) = \sum _ { i = 1 } \sum _ { \{ s ^ { \prime } , s \} \neq s ^ { \prime } = 2 \atop s ^ { \prime } = 2 } \int _ { \{ s ^ { \prime } , s ^ { \prime } , s \} \neq s ^ { \prime } = 1 } \| E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - x _ { 0 } - s ^ { \prime } \| _ { \mathcal { C } _ { 1 } ^ { 2 } } ^ { 2 ( s ) - 1 } \sum _ { \alpha = 1 } ^ { \infty } \frac { \| E _ { 1 } ^ { * } \| ^ { 2 } } { 2 } ( 1 - x ) ^ { \lambda } } \\ { \displaystyle \qquad \cdot \| x ^ { 1 - s ^ { \prime } - s \frac { \alpha + \beta + \gamma } { s } } - \xi ^ { \prime } \frac { \alpha } { s ^ { \prime } } x _ { 0 } x ( s , s ) - \| E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - x _ { 0 } - s ^ { \prime } \| _ { \mathcal { C } _ { 1 } ^ { 2 } } ^ { 2 ( s ) - 1 } \frac { \| E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - x _ { 0 } \| ^ { \lambda } } { 2 } } & { x _ { 0 } \lesssim s ^ { \prime } \| _ { \mathcal { C } _ { 1 } ^ { 2 } } ^ { 2 ( s ) - 1 } } \\ { \displaystyle \Big | e ^ { - s ^ { \prime } \alpha } ( E _ { 1 } ^ { * } ( x , s ^ { \prime } ) + i \langle E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - \mathcal { C } _ { 1 } ^ { * } ( x , s ^ { \prime } ) \rangle - \langle E _ { 1 } ^ { * } ( x , s ^ { \prime } ) \rangle - \langle E _ { 1 } ^ { * } ( x , s ^ { \prime } ) ( x , s ^ { \prime } ) + i \langle E _ { 1 } ^ { * } ( x , s ^ { \prime } ) - \mathcal { C } _ { 1 } ^ { \dagger } \| _ { \mathcal { C } _ { 1 } } ^ { 2 } } \\  \ \end{array}
$$

When $\beta _ { X } < 1$ , we have $\begin{array} { r } { \lfloor \widetilde { \beta } _ { X } \rfloor = \lfloor \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } \rfloor \le \lfloor \beta _ { X } \rfloor = 0 } \end{array}$ , and

$$
\begin{array} { r l } & { ( E _ { C } ) \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } } 2 ^ { 2 j } ( 2 ^ { - j \beta _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } } \\ & { \quad \quad \quad = 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } \cdot 2 ^ { 2 j } ( 2 ^ { - j \beta _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } - \alpha _ { X } } } \\ & { \quad \quad \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } \cdot \Big ( 2 ^ { 2 j } 2 ^ { - j \beta _ { Y } } ( 2 ^ { - j \frac { \alpha _ { Y } } { \alpha _ { X } } } ) ^ { \beta _ { X } - \alpha _ { X } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \frac { 2 \alpha _ { X } } { \alpha _ { Y } } } 2 ^ { 2 j } \Big ) } \\ & { \quad \quad \quad = 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } \cdot \Big ( 2 ^ { 2 j } 2 ^ { - j \beta _ { Y } } ( 2 ^ { - j \frac { \alpha _ { Y } } { \alpha _ { X } } } ) ^ { \beta _ { X } - \alpha _ { X } } + \log n \cdot ( 2 ^ { - j \frac { \alpha _ { Y } } { \alpha _ { X } } } ) ^ { \frac { 2 \alpha _ { X } } { \alpha _ { Y } } } 2 ^ { 2 j } \Big ) } \\ & { \quad \quad \lesssim ( \log n ) \cdot 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } . } \end{array}
$$

Furthermore, for bounding the term $\left( E _ { D } \right)$ , notice that for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$ and $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$

$$
\| G _ { [ k ] } ( z , x ) - G _ { [ k ] } ( z , x ^ { * } ) \| \lesssim \| x - x ^ { * } \| ^ { 1 \wedge \beta _ { X } } \lesssim ( \varepsilon _ { j } ^ { x } ) ^ { 1 \wedge \beta _ { X } } ,
$$

and when $\beta _ { X } \leq 1$ , it holds that $\| G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) \| = 0$ ; when $\beta _ { X } > 1$

$$
\begin{array} { r l } & { \| G _ { [ k ] , x ^ { * } } ^ { ( * ) } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { ( * ) } ( z , x ^ { * } ) \| } \\ & { = \Big \| \displaystyle \sum _ { s = 0 } ^ { j } \displaystyle \sum _ { y \in \bar { \Psi } _ { \alpha } ^ { \bar { \theta } ^ { * } } } \sum _ { \underline { { t \in \mathbb { S } } } ^ { s } } \int _ { \underline { { t \in \mathbb { S } } } ^ { s } } \frac { 1 } { l ! } G _ { [ k ] } ^ { + ( 0 , l ) } ( t , x ^ { * } ) \big ( x - x ^ { * } \big ) ^ { l } \psi ( t ) \mathrm { d } t \cdot \psi ( z ) \Big \| } \\ & { = \Big \| \displaystyle \sum _ { s = 0 } ^ { j } \displaystyle \sum _ { y \in \bar { \Psi } _ { \alpha } ^ { \bar { \theta } ^ { * } } } \sum _ { \underline { { t \in \mathbb { S } } } ^ { s } } \sum _ { \underline { { t \in \bar { \Psi } } } ^ { s } } \frac { 1 } { l ! } G _ { [ k ] } ^ { + ( 0 , l ) } ( t , x ^ { * } ) \big ( x - x ^ { * } \big ) ^ { l } \psi ( t ) \mathrm { d } t \cdot \psi ( z ) \Big \| + o ( \varepsilon _ { j } ^ { x } ) } \\ & { \overset { ( i ) } { \lesssim } \varepsilon _ { j } ^ { j } \displaystyle \sum _ { s = 0 } ^ { j } 2 ^ { - s ( \beta _ { x } - \frac { \delta _ { y } } { \beta _ { x } } ) } \lesssim \varepsilon _ { j } ^ { x } \cdot ( j \wedge \frac { 1 } { \beta _ { x } - 1 } ) , } \end{array}
$$

where $( i )$ uses that for any $l \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ with $| l | = 1$ $= 1 , G _ { [ k ] } ^ { \ast ( \mathbf { 0 } , l ) } ( \cdot , x ^ { \ast } ) \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } - \beta _ { Y } / \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } )$ . Together with $\| G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| \lesssim 2 ^ { - j \beta _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } }$ , we can derive that, for any $l \in \mathbb { N } _ { 0 } ^ { D _ { Y } }$ with $| l | = \lfloor \widetilde { \beta } _ { X } \rfloor + 1$ , and any $i \in [ D _ { Y } ]$ with $l _ { i } \geq 1$ ,

$$
\begin{array} { r l r } {  { ( G _ { [ k ] i } ^ { * } ( z , x ) - G _ { [ k ] i } ^ { * } ( z , x ^ { * } ) ) ^ { l _ { i } } - ( G _ { [ k ] i } ^ { * } ( z , x ) - G _ { [ k ] i } ^ { * } ( z , x ^ { * } ) ) ^ { l _ { i } } \vert } } \\ & { } & { = \vert ( G _ { [ k ] i } ^ { * } ( z , x ) - G _ { [ k ] i } ^ { * } ( z , x ^ { * } ) - G _ { [ k ] i } ^ { * } ( z , x ) + G _ { [ k ] i } ^ { \dagger } ( z , x ^ { * } ) ) } \\ & { } & { \cdot \sum _ { i = 1 } ^ { k } ( G _ { [ k ] i } ^ { * } ( z , x ) - G _ { [ k ] i } ^ { * } ( z , x ^ { * } ) ) ^ { l _ { i } - i } ( G _ { [ k ] i } ^ { * } ( z , x ) - G _ { [ k ] i } ^ { \dagger } ( z , x ^ { * } ) ) ^ { i _ { 1 } - 1 } \vert } \\ & { } & { \lesssim \{ \begin{array} { l l } { ( \log n ) \cdot ( ( 2 \cdot ^ { - j _ { 3 } j _ { Y } } + ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) \wedge \varepsilon _ { j } ^ { x } ) \big ( ( j \wedge \frac { 1 } { \beta _ { X } - 1 } ) \cdot \varepsilon _ { j } ^ { x } \big ) ^ { l _ { i } - 1 } } & { \beta _ { X } \geq 1 } \\ { \big ( \varepsilon _ { j } ^ { x } \big ) ^ { j _ { X } } } & { \beta _ { X } \leq 1 } \end{array}  } \\ & { } &  \lesssim \{ \begin{array} { l l }  ( \log n ) \cdot ( j \wedge \frac { 1 } { \beta _ { X } - 1 } ) ^ { l _ { i } - 1 } \cdot ( 2 \cdot ^ { - j _ { \beta _ { Y } } } + ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) ^ { \frac { \alpha _ { X } } { \alpha _ { Y } } } ( \varepsilon _ { j } ^ { x } ) ^  \end{array} \end{array}
$$

$G _ { [ k ] i } ^ { * } ( z , x )$ denote the $i$ -th component of the $D _ { Y }$ -dimensional vector $G _ { [ k ] } ^ { * } ( z , x )$ . Therefore, when $\beta _ { X } > 1$

$$
\begin{array} { r l } & { \big | ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } - ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) ) ^ { l } \big | } \\ & { \lesssim ( \log n ) \cdot ( j \wedge \frac { 1 } { \beta _ { X } - 1 } ) ^ { \lfloor \widetilde { \beta } _ { X } \rfloor } ( 2 ^ { - j \beta _ { Y } } + ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } ) ^ { \frac { \alpha _ { X } } { \alpha _ { Y } } } ( \varepsilon _ { j } ^ { x } ) ^ { \lfloor \widetilde { \beta } _ { X } \rfloor + 1 - \frac { \alpha _ { X } } { \alpha _ { Y } } } , } \end{array}
$$

and

$$
\begin{array} { c c l } { { } } & { { } } & { { } } \\ { { } } & { { } } & { { \displaystyle \sum _ { k = 1 } ^ { n \theta } \sum _ { i = 1 } ^ { n } \int _ { \mathbb { R } ^ { k } } \| \Gamma _ { \mu ^ { k } \mu _ { k } ^ { k } } ( \theta _ { 0 } ) \| ^ { 2 } \mathcal { L } _ { \mu _ { k } ^ { k } } ( \theta _ { 0 } - \theta _ { 1 } ) \| _ { \mathcal L ^ { k } } \| _ { \mu ^ { k } } ^ { 2 } \leq \int _ { 0 } ^ { \theta _ { 0 } } \int _ { \mathbb { R } ^ { k } } \| \int _ { 0 } ^ { \theta _ { 0 } } \| \tilde { \mu } ^ { k } | - \mu _ { 0 } ^ { \prime } \| _ { \mathcal L ^ { k } } \| _ { \mu ^ { k } } ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } \\ & { { } { } } & { { \displaystyle \| \theta _ { 0 } ^ { \mu \mu \mu } \| _ { \mathbb { R } ^ { 2 } \mu _ { k } ^ { k } } ( \theta _ { 0 } ^ { \star \prime } ) + \mu ( \theta _ { 0 } ^ { \prime } ) _ { \mathcal L ^ { k } } ( \theta _ { 0 } ^ { \star \prime } ) - \mathbb { E } _ { \mu ^ { k } \mu _ { k } ^ { k } } ( \theta _ { 0 } ^ { \star \prime } ) \| _ { \mathcal L ^ { k } } \| _ { \mu ^ { k } } ^ { 2 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { } } &   \displaystyle - \| \theta _ { 0 } ^ { \mu \mu \mu } \| _ { \mathbb { R } ^ { 2 } \mu _ { k } ^ { k } } ( \theta _ { 0 } ^ { \star \prime } ) - \mathbb { E } _ { \mu ^ { k } \mu _ { k } ^ { k } } ( \theta _ { 0 } ^ { \star \prime } ) \| _ { \mathbb L ^ { k } } ^ { 2 } \| u _ { 0 } ^ { \prime } - u _ { 0 } ^  \end{array}
$$

where the last inequality uses that

$$
\begin{array} { r l r } {  { ( \frac { \alpha _ { Y } } { \alpha _ { X } } - 1 ) ( \big | \widetilde { \beta } _ { X } \big | + 1 ) + \beta _ { Y } \frac { \alpha _ { X } } { \alpha _ { Y } } - 1 - \alpha _ { Y } \ge ( \frac { \alpha _ { Y } } { \alpha _ { X } } - 1 ) \widetilde { \beta } _ { X } + \beta _ { Y } \frac { \alpha _ { X } } { \alpha _ { Y } } - 1 - \alpha _ { Y } } } \\ & { } & { \ge ( \frac { \alpha _ { Y } } { \alpha _ { X } } - 1 ) ( \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } ) + ( \alpha _ { Y } + 1 ) \frac { \alpha _ { X } } { \alpha _ { Y } } - 1 - \alpha _ { Y } = 1 . } \end{array}
$$

and

$$
\begin{array} { r } { ( \lfloor \widetilde { \beta } _ { X } \rfloor + 1 ) ( 1 - \frac { \alpha _ { X } } { \alpha _ { Y } } ) + \beta _ { X } \frac { \alpha _ { X } } { \alpha _ { Y } } - \frac { \alpha _ { X } } { \alpha _ { Y } } - \alpha _ { X } \ge \widetilde { \beta } _ { X } ( 1 - \frac { \alpha _ { X } } { \alpha _ { Y } } ) + \beta _ { X } \frac { \alpha _ { X } } { \alpha _ { Y } } - \frac { \alpha _ { X } } { \alpha _ { Y } } - \alpha _ { X } } \\ { \ge \widetilde { \beta } _ { X } - \frac { \alpha _ { X } } { \alpha _ { Y } } - \alpha _ { X } = 0 , ~ } \end{array}
$$

alongside the fact that $\lfloor \widetilde { \beta } _ { X } \rfloor + 1 = \widetilde { \beta } _ { X }$ only if ${ \widetilde { \beta } } _ { X }$ is an integer. Similarly, when $\beta _ { X } \leq 1$ ,

$$
( E _ { D } ) \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } + 1 } ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } 2 ^ { j } ( \varepsilon _ { j } ^ { x } ) ^ { \frac { \alpha _ { X } } { \alpha _ { Y } } } \lesssim 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } .
$$

By combining the bounds for terms $\left( E _ { C } \right)$ and $\left( E _ { D } \right)$ , and using Equation (45), we can obtain that

$$
\begin{array} { r l } & { E _ { A } ) = \displaystyle \sum _ { \| x ^ { * } - x _ { x } ^ { * } \| \leq z _ { 2 } ^ { x } } \int _ { \{ z \in \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( 0 , \tau _ { 1 } ) : \| G _ { [ k ] } ^ { * } ( z , x ^ { * } ) - y _ { \psi ^ { * } } \| \leq C 2 ^ { - j } \} } 2 ^ { \frac { j ( d _ { Y } - D _ { Y } ) } { 2 } } } \\ & { \displaystyle \sum _ { l \in \mathbb { R } _ { 0 } ^ { D } } \frac { \psi ^ { * ( l ) } \left( G _ { [ k ] } ^ { * } \left( z , x ^ { * } \right) \right) } { l ! } ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } - \frac { \psi ^ { * ( l ) } \left( G _ { [ k ] , x ^ { * } } ^ { \dagger } \left( z , x ^ { * } \right) \right) } { l ! } ( G _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } } \\ & { \displaystyle 0 \leq | l | \leq 1 \delta _ { 1 } } \\ & { \quad \quad \cdot v _ { [ k ] , x ^ { * } } ^ { \dagger } ( z , x ) \mathrm { d } z + \mathcal { O } ( \log n \cdot 2 ^ { - \frac { j d _ { Y } } { 2 } } ( \hat { \varepsilon } _ { j } ^ { x } ) ^ { \alpha _ { X } } ) . } \end{array}
$$

Given that for any $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$ ,

$$
G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) = \sum _ { \tiny \begin{array} { c } { s \in \mathbb { N } _ { 0 } ^ { D } { \cal X } } \\ { 1 \leq | s | \leq | \tilde { \beta } _ { \cal X } | } \end{array} } \frac { G _ { [ k ] } ^ { * } ( { \bf 0 } , s ) ( z , x ^ { * } ) } { s ! } ( x - x ^ { * } ) ^ { s } + { \mathcal O } ( ( \varepsilon _ { j } ^ { x } ) ^ { \widetilde { \beta } _ { \cal X } } )
$$

and considering that G†[k],x∗ (z, x) is polynomial in x,

$$
G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) - G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ^ { * } ) = \sum _ { \tiny \begin{array} { c } { { s \in \mathbb { N } _ { 0 } ^ { D } x } } \\ { { 1 \leq | s | \leq | \tilde { \beta } _ { X } | } } \end{array} } \frac { G _ { [ k ] , x ^ { * } } ^ { \dag } ( { \bf 0 } , s ) ( z , x ^ { * } ) } { s ! } ( x - x ^ { * } ) ^ { s } ,
$$

where recall $G ^ { ( 0 , s ) } ( z , x )$ denotes the partial derivative of $G ( z , \cdot )$ of order $s$ evaluated at $x$ . If $\widetilde { \beta } _ { X } > 1$ , it holds for any $l \in  { \mathbb { N } } _ { 0 } ^ { D _ { Y } }$ with $1 \leq | l | \leq \lfloor \widetilde { \beta } _ { X } \rfloor$ that,

$$
\Big | ( G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ^ { * } ) ) ^ { l } - \big ( \sum _ { \scriptstyle s \in \mathbb { N } _ { 0 } ^ { D } \atop { \scriptstyle 1 \leq | s | \leq | \tilde { g } _ { X } | } } \frac { G _ { [ k ] } ^ { * } ( 0 , s ) ( z , x ^ { * } ) } { s ! } ( x - x ^ { * } ) ^ { s } \big ) ^ { l } \Big | \lesssim ( \varepsilon _ { j } ^ { x } ) ^ { \tilde { \beta } _ { X } + | l | - 1 } .
$$

Therefore,

$$
\begin{array} { r l } &  \underset { \{ \mathbf { x } ^ { \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \quad \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset { \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \} } { \sum } \underset  \{ \mathbf { x } ^ { \prime \prime } , \mathbf { x } ^ { \prime \prime } \leq \mathbf { x } ^ { \prime \prime } \leq \mathbf { x } ^ { \prime \prime } \leq \mathbf { x } ^ { \prime \prime } \leq \mathbf { x } ^ { \prime \prime } \ \end{array}
$$

where we have used the fact that

$$
\begin{array} { r l } { 2 ^ { j | l | } \big ( \varepsilon _ { j } ^ { x } \big ) ^ { \widetilde { \beta } _ { X } + | l | - 1 } \lesssim } & { \displaystyle \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D _ { Y } } } { 1 \leq | l | \leq | \widetilde { \beta } _ { X } | } } \big ( \varepsilon _ { j } ^ { x } \big ) ^ { - \frac { \alpha _ { X } } { \alpha _ { Y } } | l | + \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } + | l | - 1 } = \displaystyle \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { D _ { Y } } } { 1 \leq | l | \leq | \widetilde { \beta } _ { X } | } } \big ( \varepsilon _ { j } ^ { x } \big ) ^ { \alpha _ { X } } \big ( \varepsilon _ { j } ^ { x } \big ) ^ { ( 1 - \frac { \alpha _ { X } } { \alpha _ { Y } } ) ( | l | - 1 ) } \lesssim } \\ { \times \displaystyle \coprod _ { \textnormal { N } ^ { 1 } } \big \langle 1 \big | 1 \leq | \beta _ { X } | \big \rangle _ { X } } \end{array}
$$

Together with the fact that $v _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x )$ is polynomial in $x$

$$
{ v _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) = \sum _ { \stackrel { s \in \mathbb { N } _ { 0 } ^ { D _ { X } } } { 0 \leq | s | \leq \lfloor \alpha _ { X } \rfloor } } \frac { { v _ { [ k ] } ^ { \dag } ( \mathbf { 0 } , s ) } ( z , x ^ { * } ) } { s ! } ( x - x ^ { * } ) ^ { s } , }
$$

we can then obtain

$$
\begin{array} { l }  { E _ { 4 } \Big ) = \displaystyle \sum _ { \stackrel { k \in [ K _ { 1 } ] } { l _ { 1 } ^ { \mathrm { t e s } } - \kappa _ { k } ^ { \mathrm { g r i } } [ 1 ] } } \displaystyle \int _ { \{ z : \nabla _ { \mathbf { R } _ { k } ^ { \mathrm { d e f } } } ( 0 , \pi ) : | | G _ { | k | } ^ { \mathrm { c } } ( z , \pi ^ { * } ) - y _ { \mathrm { g r } } | \leq ( z - 2 ) \} } \frac { 2 i ^ { ( d _ { 1 } - D - D ) } } { 2 } \left( \psi ^ { * } ( G _ { | k | } ^ { \mathrm { s } } ( z , x ^ { * } ) ) - \psi ^ { * } ( G _ { | k | } ^ { \mathrm { s } } ( z , x ^ { * } ) ) \right) } \\ { { + \displaystyle \sum _ { \stackrel { k \in [ K _ { 1 } ] } { l _ { 1 } ^ { \mathrm { g r } } \kappa _ { l } ^ { \mathrm { g r } } } } \frac { \psi ^ { * ( \delta ) } \left( G _ { | k | } ^ { \mathrm { d e } } \left( z , x ^ { * } \right) \right) } { l ! } \Big ( \displaystyle \sum _ { \stackrel { k \in [ N _ { 1 } ] } { l _ { 1 } ^ { \mathrm { g r } } \kappa _ { l } ^ { \mathrm { g r } } } } \frac { G _ { | k | } ^ { \mathrm { s } } \left( 0 , \mathrm { s } \right) \left( z , x ^ { * } \right) } { s ! } ( x - x ^ { * } ) s \Big ) ^ { l } } } \\   + \displaystyle \frac { \psi ^ { * ( l ) } \left( G _ { | k | } ^ { \mathrm { s } } ( z , x ^ { * } ) \right) } { l ! } \left( \displaystyle \sum _ { \stackrel { k \in [ N _ { 1 } ] } { l _ { 1 } ^ { \mathrm { g r } } \kappa _ { l } ^ { \mathrm { g r } } } } ( \frac { 0 . \mathrm { e } ^ { \mathrm { f } } } { s ! } ( z , x ^ { * } ) \left( z , x ^ { * } \right) \right) \displaystyle \sum _  \stackrel { k \in [ N _ { 1 } ] }  l _  1  \end{array}
$$

Also notice that we can rewrite

$$
\begin{array} { r l } & { \underset { \underset { x \in \mathbb { R } _ { n } ^ { d } \times \mathbb { R } _ { n } ^ { d } } { \sum \leq \nu \leq k } } { \sum \sum _ { i \in \mathbb { R } _ { n } ^ { d } \times \mathbb { R } _ { n } ^ { d } } } \int _ { \left\{ \xi \in \mathbb { R } _ { n } ^ { d } \times \{ 0 , x \} \leq \| G _ { i } \| _ { \mathcal { X } } ^ { \varepsilon } ( z , z ^ { \varepsilon } ) - g _ { \varepsilon ^ { \varepsilon - 1 } } \geq \mathcal { X } _ { \varepsilon ^ { \varepsilon } } \right\} } \frac { 2 ^ { \lambda ( d , \varepsilon - D , x ) } } { \lambda ^ { 2 } } \left( \psi ^ { * } ( G _ { | \mathcal { X } | } ^ { \varepsilon } ( z , x ^ { \varepsilon } ) ) - \psi ^ { * } ( G _ { | \mathcal { X } | } ^ { \varepsilon } ) \right) - \frac { 2 ^ { \lambda } } { \lambda ^ { 2 } } \psi ^ { * } ( G _ { | \mathcal { X } | } ^ { \varepsilon } ) \mathrm { , ~ } } \\ & { \overset { = } - \underset { \underset { x \in \mathbb { R } _ { n } ^ { d } \times \mathbb { R } _ { n } ^ { d } } { \sum \leq \nu \leq k } } { \sum \sum _ { i \in \mathbb { R } _ { n } ^ { d } \times \mathbb { R } _ { n } ^ { d } } } \frac { \psi ^ { * ( \lambda ) } ( G _ { | \mathcal { X } | } ^ { \varepsilon } ( z , x ^ { \varepsilon } ) ) } { \| \lambda ^ { 2 } } \Big ( \underset { \underset { x \in \mathbb { R } ^ { d } \times \mathbb { R } ^ { d } } { \sum \leq \nu } } { \sum \sum _ { i \in \mathbb { R } _ { n } ^ { d } \times \mathbb { R } _ { n } ^ { d } } } \frac { G _ { | \mathcal { X } | } ^ { \varepsilon } ( 0 , \varepsilon ) } { \lambda ^ { 2 } } ( x - x ^ { \varepsilon } ) \big ) ^ { \lambda } } \\ &  \underset { \leq t \leq \nu } { \sum \varepsilon \eta } ( \tilde { G } _ { | \mathcal { X } | } ^ { \varepsilon }  \end{array}
$$

where $\begin{array} { r } { | a _ { \psi ^ { * } , x ^ { * } , s } | \leq C 2 ^ { j \lfloor \widetilde { \beta } _ { X } \rfloor } ( \log n ) ^ { 1 + \lfloor \widetilde { \beta } _ { X } \rfloor } \lesssim n . } \end{array}$

Then for term $\left( E _ { B } \right)$ , using the Taylor’s theorem for $\psi ^ { * } ( \cdot ) , G _ { [ k ] } ^ { * } ( z , \cdot )$ , and $v _ { [ k ] } ^ { \ast } ( z , \cdot )$ , we have

$$
\begin{array} { r l } { \psi ^ { * } ( G _ { | k | } ^ { * } ( z , x ) ) = } & { \displaystyle \sum _ { \alpha \in [ 0 , T ] } \frac { \psi ^ { * } ( \theta ) ( G _ { | k | } ^ { * } ( z , x ^ { * } ) ) } { | z | } ( G _ { | k | } ^ { * } ( z , x ^ { * } ) ) ( G _ { | k | } ^ { * } ( z , x ) - G _ { | k | } ^ { * } ( z , x ^ { * } ) ) ^ { l } + O ( 2 ^ { \frac { 2 \nu _ { \chi } } { 2 } } ( ( \varepsilon _ { > } ^ { * } ) ^ { \beta } ) } \\ & { \displaystyle \qquad \otimes \xi | z | \big \langle z | z | x \big \rangle } \\ { = \psi ^ { * } ( G _ { | k | } ^ { * } ( z , x ^ { * } ) ) + \displaystyle \sum _ { \alpha \in [ 0 , T ] } \frac { \psi ^ { * } ( \theta ) ( G _ { | k | } ^ { * } ( z , x ^ { * } ) ) } { | \xi | } \big ( \displaystyle \sum _ { \alpha \in [ 0 , T ] } \frac { G _ { | k | } ^ { * } ( 0 , \varepsilon ^ { * } ) } { | \xi | } ( s , x ^ { * } ) \big ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \times | s | \operatorname* { d e t } | s \frac { \psi ^ { * } ( \theta ) } { | \xi | } \big ( s , x ^ { * } \big ) } \\ { + O ( 2 ^ { \frac { 2 \nu _ { \chi } } { 2 } } \big ( ( \varepsilon _ { > } ^ { * } ) ^ { \gamma _ { \chi } \kappa _ { 1 } \gamma _ { 2 } } \big ) | \hat { j } _ { k } \big | ^ { 1 } ) + O \big ( 2 ^ { \frac { 2 \nu _ { \chi } } { 2 } } \big ( \varepsilon _ { > } ^ { * } \big ) ^ { \hat { \pi } _ { 2 } \gamma _ { \chi } } 2 \big ) \Big \{  } \\ &  \quad \quad \quad  \end{array}
$$

and recall

$$
v _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) = \sum _ { \tiny \begin{array} { c } { { s \in \mathbb { N } _ { 0 } ^ { D _ { X } } } } \\ { { 0 \leq | s | \leq \lfloor \alpha _ { X } \rfloor } } \end{array} } \frac { v _ { [ k ] } ^ { \dag } ( { \bf 0 } , s ) ( z , x ^ { * } ) } { s ! } ( x - x ^ { * } ) ^ { s } .
$$

Combined with the fact that $| v _ { [ k ] } ^ { * } ( z , x ) - v _ { [ k ] } ^ { \dag } ( z , x ) | \lesssim 2 ^ { - j \alpha _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } }$ , and

$$
\begin{array} { r l } & { ( 2 ^ { - j \alpha _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } ) ( ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } \wedge 1 } 2 ^ { j } ) ^ { \lfloor \widetilde { \beta } _ { X } \rfloor + 1 } } \\ & { \lesssim \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } + 2 ^ { - j \alpha _ { Y } } ( \varepsilon _ { j } ^ { x } 2 ^ { j } ) ^ { \alpha _ { X } } + 2 ^ { - j \alpha _ { Y } } ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } 2 ^ { j } } \\ & { \lesssim \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } , } \end{array}
$$

$$
\begin{array} { r l } & { ( 2 ^ { - j \alpha _ { Y } } + \log n \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } ) ( \varepsilon _ { j } ^ { x } ) ^ { \widetilde { \beta } _ { X } } 2 ^ { j } } \\ & { \lesssim ( \varepsilon _ { j } ^ { x } ) ^ { \widetilde { \beta } _ { X } } ( \varepsilon _ { j } ^ { x } ) ^ { - \frac { \alpha _ { X } } { \alpha _ { Y } } } } \\ & { = ( \varepsilon _ { j } ^ { x } ) ^ { \alpha _ { X } } . } \end{array}
$$

We can get

$$
\begin{array} { r l } & { \quad _ { 1 } < \frac { \sqrt { 3 } } { 2 } \displaystyle { \operatorname* { I m } _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \left( \frac { 1 } { \alpha } \right) } = \int _ { 0 } ^ { \infty } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \lesssim } \\ &  = \int _ { \mathbb { Z } _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } } \displaystyle { \operatorname* { I m } _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \lesssim } \\ &  \quad _ { 1 } < \frac { \sqrt { 3 } } { 2 } \displaystyle  \operatorname* { I m } _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } } \log _ { \alpha \in \mathbb { Z } _ { \alpha } ^ { \star } }  \end{array}
$$

Notice that we can write

$$
\begin{array} { r l } { \underset { 1 \leq t \leq \frac { \hat { \sigma } _ { \hat { \sigma } _ { \hat { \sigma } } _ { \hat { \sigma } } ^ { \star } } } { 2 } } \sum _ { \substack { ( z \in \mathcal { E } _ { \hat { \sigma } _ { \hat { \sigma } } \hat { \sigma } _ { \hat { \sigma } } } ( \boldsymbol { 1 } , z ) ) \leq ( \mathcal { C } _ { 1 } \backslash ( ( \frac { z } { \hat { \sigma } _ { \hat { \sigma } } } , z ) - \hat { \sigma } _ { \hat { \sigma } } + 1 \leq ( \frac { z \sigma - \hat { \sigma } } { 2 } ) ) ^ { \epsilon } } } ( \psi ^ { s } ( \mathcal { E } _ { ( \hat { \sigma } ) \hat { \sigma } } ( z , x ^ { * } ) )   } \\ {   +  \sum _ { \textbf { \sigma \in \hat { \sigma } _ { \hat { \sigma } } ^ { \hat { \sigma } } } \times \mathcal { F } _ { \hat { \sigma } } } \psi ^ { s } ( \boldsymbol { 1 } ) ( \mathcal { E } _ { \hat { \hat { \sigma } } } ( z , x ^ { * } ) ) ) ( \quad \sum _ { \textbf { \sigma \in \hat { \sigma } _ { \hat { \sigma } } ^ { \hat { \sigma } } } \times \mathcal { F } _ { \hat { \sigma } } } ( \frac { \mathcal { E } _ { \hat { \sigma } } ^ { \mathrm { K } } ( \boldsymbol { 1 } , \boldsymbol { \hat { \sigma } } ) ( z , x ^ { * } ) } { s ! } ( ( z - x ^ { * } ) ) ) )   } \\ {    \underset { 1 \leq t \leq \frac { \hat { \sigma } _ { \hat { \sigma } } ^ { \hat { \sigma } } } { 2 } } \psi ( \mathcal { E } _ { \hat { \sigma } } )    } \\      ( \sum _ { \textbf { \sigma \in \hat { \sigma } _ { \hat { \sigma } } ^ { \hat { \sigma } } } } \frac  \mathcal { E } _ { \hat { \sigma } } ^  \mathrm { K }  \end{array}
$$

where $| a _ { \psi ^ { * } , x ^ { * } , s } ^ { \prime } | \lesssim n$ . So by combining all pieces, we have for any $\psi ^ { * } \in \Psi _ { j } ^ { D _ { Y } }$ and $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , 2 \varepsilon _ { j } ^ { x } )$

$$
\begin{array} { l } { { \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d } { \cal Y } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { \cal Y } - D _ { \cal Y } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z } } \\ { { \displaystyle = \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { \cal Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d _ { \cal Y } - D _ { \cal Y } ) } { 2 } } \psi ^ { * } ( G _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) ) v _ { [ k ] , x ^ { * } } ^ { \dag } ( z , x ) \mathrm { d } z + \sum _ { s \in \mathbb { N } _ { 0 } ^ { D _ { \cal X } } } a _ { \psi ^ { * } , x ^ { * } , s } ^ { * } ( x - x ^ { * } ) \mathrm { d } z } } \\ { { \displaystyle \qquad \quad } } \end{array}
$$

where $a _ { \psi ^ { * } , x ^ { * } , s } ^ { * } = a _ { \psi ^ { * } , x ^ { * } , s } + a _ { \psi ^ { * } , x ^ { * } , s } ^ { \prime }$ . This completes the proof of the first statement.

For the second statement, fix arbitrary $\boldsymbol { x } ^ { * } \in \mathbb { N } _ { \varepsilon _ { j } ^ { x } } ^ { x }$ , $\psi \in \Psi _ { j } ^ { D _ { Y } } \setminus \Psi _ { j } ^ { D _ { Y } } ( x ^ { * } )$ , $x \in \mathbb { B } _ { M _ { X } } ( x ^ { * } , \varepsilon _ { j } ^ { x } )$ , $x ^ { \prime } \in$ $\mathbb { B } _ { \mathbb { N } _ { \varepsilon _ { j } ^ { x } } } ( x , 2 \varepsilon _ { j } ^ { x } ) , k \in [ K ^ { * } ]$ , and $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ . There exists $z ^ { * } \in \mathbb { N } _ { c 2 ^ { - j } } ^ { z }$ so that $\| z - z ^ { * } \| \leq c 2 ^ { - j }$ and when $c$ is small enough, it holds that

$$
\| G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) \| < L c 2 ^ { - j } + L ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } \wedge 1 } \leq \frac { C } { 2 } 2 ^ { - j } .
$$

Since for any $l \in  { \mathbb { N } } _ { 0 } ^ { D _ { Y } }$ with $| l | \leq \lfloor \widetilde { \beta } _ { X } \rfloor$

$$
\mathrm { s u p p } ( \psi ^ { * ( l ) } ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) , C 2 ^ { - j } ) = \emptyset ,
$$

we have $\psi ^ { * ( l ) } ( G _ { [ k ] } ^ { * } ( z , x ) ) = 0$ . Moreover, since $\| x - x ^ { \prime } \| \leq 2 \varepsilon _ { j } ^ { x }$ , when $\| x ^ { \prime } - x _ { k } ^ { * } \| \leq \tau _ { 2 } + 2 \varepsilon _ { j } ^ { x }$ and $C$ is sufficiently large, we have

$$
\| G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| \leq C _ { 1 } \left( 2 ^ { - j \beta _ { Y } } + ( \log n ) \cdot ( \varepsilon _ { j } ^ { x } ) ^ { \beta _ { X } } \right) < \frac { C } { 2 } 2 ^ { - j }
$$

and

$\| G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) - G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) \| \leq \| G _ { [ k ] } ^ { * } ( z , x ) - G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) \| + \| G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) - G _ { [ k ] } ^ { * } ( z , x ) \| < C \geq 0 .$ − j , and thus $\psi ^ { * ( l ) } ( G _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ) ) = 0$ . Furthermore, since $\| x ^ { \prime } - x ^ { * } \| \leq 3 \varepsilon _ { j } ^ { x }$ , we have, when $C$ is sufficiently large,

$$
G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ^ { \prime } ) - G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) \| \leq \| G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ^ { \prime } ) - G _ { [ k ] } ^ { * } ( z , x ^ { \prime } ) \| + \| G _ { [ k ] } ^ { * } ( z , x ^ { \prime } ) - G _ { [ k ] } ^ { * } ( z ^ { * } , x ^ { * } ) \| < C .
$$

and hence $\psi ^ { * ( l ) } ( G _ { [ k ] , x ^ { \prime } } ^ { \dagger } ( z , x ^ { \prime } ) ) = 0$ and $\psi ^ { * ( l ) } ( G _ { [ k ] } ^ { * } ( z , x ^ { \prime } ) ) = 0$ . So we can get

$$
\begin{array} { r l } & { \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \geq d \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d \gamma - D \gamma ) } { 2 } } \psi ^ { * } ( G _ { [ k ] } ^ { * } ( z , x ) ) v _ { [ k ] } ^ { * } ( z , x ) \mathrm { d } z = 0 , } \\ & { \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \geq d \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d \gamma - D \gamma ) } { 2 } } \psi ^ { * } ( G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) ) v _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) \mathrm { d } z } \\ & { = \sum _ { k \in [ K ^ { * } ] \leq \tau _ { 1 } } \displaystyle \sum _ { \mathbb { B } _ { \geq d \gamma } ( \mathbf { 0 } , \tau _ { 1 } ) } 2 ^ { \frac { j ( d \gamma - D \gamma ) } { 2 } } \psi ^ { * } ( G _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) ) v _ { [ k ] , x ^ { \prime } } ^ { \dag } ( z , x ) \mathrm { d } z = 0 , } \end{array}
$$

and

$$
\begin{array} { r l } &  \qquad \sum _ { j \in \mathcal { N } _ { 1 } } \frac  \phi _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _ { j } _  j \end{array}
$$

The proof is now complete.

# D.15 Proof of Lemma 20

Consider any G = PJ1j1=0 PJ2j2=0 Pψ1∈ΨdY $\begin{array} { r } { G = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) \in \widetilde { \mathcal { G } } } \end{array}$ , then since $\beta _ { Y } \geq 2$ , we have

$$
\begin{array} { r l } { \| J _ { G ( \cdot , x ) } ( z ) \| _ { F } = \displaystyle \left\| \sum _ { j _ { 1 } = 0 } \displaystyle \sum _ { j _ { 2 } = 0 } \displaystyle \sum _ { \psi _ { 1 } \in \mathfrak g _ { j _ { 1 } } ^ { \mathcal { N } } } \displaystyle \sum _ { \psi _ { 2 } \in \psi _ { j _ { 2 } } ^ { D _ { { \boldsymbol { \chi } } } } } g _ { \psi _ { 1 } \psi _ { 2 } } J _ { \psi _ { 1 } } ( z ) \psi _ { j _ { 2 } } ( x ) \right\| _ { F } } & \\ { \lesssim \displaystyle \sum _ { j _ { 1 } = 0 } \displaystyle \sum _ { j _ { 2 } = 0 } \displaystyle \sum _ { 0 } z ^ { - ( \bar { j } _ { 1 } / \beta _ { F } ) \vee ( j _ { 2 } \beta _ { K } ) } ) 2 \bar { j } ^ { \bar { j } _ { 1 } } } & \\ { \leq \displaystyle \sum _ { j _ { 1 } = 0 } \displaystyle \sum _ { j _ { 2 } = 0 } \sum _ { 2 } - \bar { j } _ { 1 } ( \beta _ { F } - 1 ) + \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 1 } ^ { J _ { 2 } } \sum _ { \vartheta _ { 1 } \in \mathcal { J } } 2 ^ { - \bar { j } _ { 2 } ( \beta _ { K } - \frac { \partial _ { X } } { \beta _ { Y } } ) } } \\ { \leq \displaystyle \sum _ { j _ { 1 } = 0 } \displaystyle \sum _ { j _ { 2 } = 0 } \sum _ { 0 } z ^ { - \bar { j } _ { 1 } ( \beta _ { Y } - 1 ) } + \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 1 } ^ { J _ { 1 } } \sum _ { \vartheta _ { 1 } \in \mathcal { J } } 2 ^ { - \bar { j } _ { 2 } ( \beta _ { X } - \frac { \partial _ { X } } { \beta _ { Y } } ) } } & \\ { = \mathcal { O } ( 1 ) . } \end{array}
$$

For the second statement, define set $\mathcal { A } _ { J _ { 1 } + 1 } = ( 0 , 2 ^ { - J _ { 1 } } )$ . Then $\cup _ { j = 0 } ^ { J _ { 1 } + 1 } { A } _ { j } = ( 0 , \stackrel { \cdot } { \infty } )$ $\mathcal { A } _ { 0 } = [ 1 , \infty )$ . If , and for any $\| z - z ^ { \prime } \| \in \mathcal { A } _ { 0 }$ $j \in [ J _ { 1 } ]$ , we have , define $\mathcal { A } _ { j } = [ 2 ^ { - j } , 2 ^ { - ( j - 1 ) } )$ , and

$$
\| J _ { G ( \cdot , x ) } ( z ) - J _ { G ( \cdot , x ) } ( z ^ { \prime } ) \| _ { F } \leq \| J _ { G ( \cdot , x ) } ( z ) \| _ { F } + \| J _ { G ( \cdot , x ) } ( z ^ { \prime } ) \| _ { F } \leq L _ { 2 } \leq L _ { 2 } \Vert z - z ^ { \prime } \Vert ^ { \beta - 1 } .
$$

If $\| z - z ^ { \prime } \| \in \mathcal { A } _ { j }$ with $j \in [ J _ { 1 } ]$ , we have

$$
\begin{array} { r l } { \displaystyle ( z ) - J _ { G ( \cdot , \cdot , \tau ) } ( z ^ { * } ) \| _ { F = } = \Big \| \displaystyle \sum _ { i = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j = 0 } ^ { J _ { 2 } } \sum _ { 0 \le i \in \mathbb { N } _ { \epsilon } ^ { 0 , \nu } \backslash i \ge 2 \le 0 } J _ { 0 \Psi _ { 1 } ( z ) } ( J _ { \Psi _ { 1 } } ( z ) - J _ { \Psi _ { 1 } ( z ^ { * } ) } ( z ^ { * } ) ) \psi _ { 2 } ( x ) \Big \| _ { F } } & { } \\ { \displaystyle \lesssim \sum _ { i = 0 } ^ { J } \sum _ { j = 0 } ^ { J _ { 2 } } \sum _ { 0 \le i \in \mathbb { N } _ { \epsilon } ^ { 0 , \nu } \backslash i \ge 2 \le N } ^ { 2 } \displaystyle \sum _ { j = 1 } ^ { J _ { 3 } } \| z - z ^ { * } \| + \displaystyle \sum _ { j _ { 1 } = j + 1 } ^ { J } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \frac { J _ { 2 } } { 2 } } & { } \\ { \displaystyle \lesssim \sum _ { j _ { 1 } = 0 } ^ { J } \sum _ { j _ { 2 } = 0 } ^ { J _ { 1 } } \Big ( 2 ^ { - ( ( J _ { 1 } , \delta _ { 1 } ) \psi _ { 1 } ) ( j _ { 2 } , \delta _ { 2 } \chi _ { 1 } ) } \Big ) 2 ^ { 2 } \hbar 2 - \delta ( 2 - \delta ) \| z - z ^ { * } \| ^ { \beta _ { 1 } } \Big ) + 2 ^ { - ( J _ { 2 } , \nu - 1 ) } \cdot j } & { } \\ { \displaystyle \lesssim \| z - z ^ { * } \| ^ { \beta _ { 1 } - 1 } \cdot 2 ^ { - ( J _ { 2 } - \beta ) } \cdot \sum _ { j _ { 1 } = 0 } ^ { J } ( 1 + j _ { 1 } ) 2 ^ { - ( J _ { 2 } - 2 ) \delta _ { 1 } } + 2 ^ { - J ( \beta - 1 ) } \cdot 2 ^ { - J ( \beta - \beta ) } \cdot 2 } & { } \\   \end{array}
$$

where the last inequality uses $\beta < 2 \le \beta _ { Y }$ . Similarly, if $\| z - z ^ { \prime } \| \in \mathcal { A } _ { J _ { 1 } + 1 }$ , then

$$
\begin{array} { r l } { \| J _ { G ( \cdot , x ) } ( z ) - J _ { G ( \cdot , x ) } ( z ^ { \prime } ) \| _ { F } = \Big \| \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { \chi } } } \displaystyle \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { \chi } } } { g _ { \psi _ { 1 } \psi _ { 2 } } } \big ( J _ { \psi _ { 1 } } ( z ) - J _ { \psi _ { 1 } } ( z ^ { \prime } ) \big ) \psi _ { 2 } ( x ) \Big \| _ { F } } & \\ { \lesssim \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \frac { 2 ^ { - ( ( j _ { 1 } \vartheta _ { \chi } ) \vee ( j _ { 2 } \vartheta _ { \chi } ) ) } 2 ^ { j _ { 1 } } } { 2 ^ { j _ { 1 } } } \| z - z ^ { \prime } \| } & \\ { \lesssim \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { - ( ( j _ { 1 } \vartheta _ { \chi } ) \vee ( j _ { 2 } \vartheta _ { \chi } ) ) } 2 ^ { 2 j _ { 1 } } 2 ^ { - J _ { 1 } ( 2 - \beta ) } \| z - z ^ { \prime } \| ^ { \beta - 1 } } & \\ { \lesssim \displaystyle \frac { z ^ { \prime } } { j _ { 1 } - 0 } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 1 } } 0 ^ { - 1 } . } & \end{array}
$$

The proof is complete.

# D.16 Proof of Lemma 21

Consider

$$
G ( z , x ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } \psi _ { 1 } ( z ) \psi _ { 2 } ( x )
$$

and

$$
G ^ { \prime } ( z , x ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } g _ { \psi _ { 1 } \psi _ { 2 } } ^ { \prime } \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) .
$$

Then

$$
\begin{array} { r l } & { \quad \underset { x \in \mathbb { R } ^ { d } } { \operatorname* { s u p } } \ \lVert G ( z , x ) - G ^ { \prime } ( z , x ) \rVert } \\ & { = \epsilon \overset { g ^ { ( R , X ) } } { \epsilon } } \\ & { = \ \underset { x \in \mathbb { R } ^ { d } } { \operatorname* { s u p } } \ \underset { y _ { 1 } = 0 } { \overset { J ^ { 1 } } { \sum } } \ \underset { \phi _ { 1 } \in \mathcal { V } _ { 1 } ^ { d } } { \sum } \underset { \psi \geq \epsilon } { \sum } \underset { \psi \geq \epsilon } { \sum } \ \underset { \psi _ { 1 } \not = \mathcal { V } _ { 2 } } { \sum \sum } \ \ \underset { \psi \geq \epsilon } { \sum } \ \big ( g _ { \psi _ { 1 } \psi _ { 2 } } - g _ { \psi _ { 1 } \psi _ { 2 } } ^ { \prime } \big ) \psi _ { 1 } ( z ) \psi _ { 2 } ( x ) \Big \lVert } \\ & { \ \underset { x \in \mathbb { R } ^ { d } } { \operatorname* { s u p } } \ \underset { y _ { 1 } = 0 } { \overset { J ^ { 1 } } { \sum } } \ \underset { \psi \geq \epsilon } { \sum } \underset { \psi \geq \epsilon } { \sum } \underset { \psi \geq \epsilon } { \sum } { \operatorname* { s u p } } \ \underset { x \not = \mathcal { V } _ { 2 } } { \sum \operatorname* { s u p } } \ \underset { \psi \geq \epsilon } { \sum } \underset { \psi \geq \epsilon } { \sum } { \operatorname* { s u p } } \ \underset { x \in \mathbb { R } ^ { d } } { \sum } \ \underset { \psi \geq \epsilon } { \sum } \underset { \psi _ { 1 } \in \mathcal { V } _ { 1 } ^ { d } } { \sum } \ \underset { \psi \geq \epsilon } { \sum } \underset { \gamma _ { 2 } } { \sum } \ } \\ &  \leq \ C \underset { j _ { 1 } = 0 } { \overset { J ^ { 1 } } { \sum } } \underset { 0 \geq 0 } { \overset { J ^ { 1 } } { \sum } } \ \underset { \psi \geq \epsilon } { \operatorname* { s u p } } \underset { \psi \geq \epsilon }   \end{array}
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } \leq 2 } \end{array}$ , there exists a constant $C _ { 1 }$ so that

$$
\begin{array} { r l } & { \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { \frac { d _ { \gamma { j _ { 1 } } + d _ { X } { j _ { 2 } } } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { \gamma } \vee j _ { 2 } \beta _ { X } } { 2 } } } \\ & { \leq \frac { 2 ^ { d _ { X } / 4 } } { 2 ^ { d _ { X } / 4 } - 1 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { \frac { d _ { X } j _ { 1 } \beta _ { Y } } { 4 \beta _ { X } \gamma _ { 1 } } + \frac { d _ { Y } j _ { 1 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } } { 2 } } + \frac { 2 ^ { d _ { Y } / 4 } } { 2 ^ { d _ { Y } / 4 } - 1 } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { \frac { d _ { Y } j _ { 2 } \beta _ { X } } { 4 \beta _ { Y } \gamma _ { 1 } } + \frac { d _ { X } j _ { 2 } } { 4 \gamma _ { 1 } } - \frac { j _ { 2 } \beta _ { X } } { 2 } } } \\ & { \leq C _ { 1 } ( J _ { 1 } + J _ { 2 } ) . } \end{array}
$$

So if for any $j _ { 1 } \in [ J _ { 1 } ] , j _ { 2 } \in [ J _ { 2 } ] , \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } }$ , and $\psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } }$ ,

$$
\left. g _ { \psi _ { 1 } \psi _ { 2 } } - g _ { \psi _ { 1 } \psi _ { 2 } } ^ { \prime } \right. \leq \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } { C C _ { 1 } ( J _ { 1 } + J _ { 2 } ) } 2 ^ { \frac { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } { 4 \gamma _ { 1 } } - \frac { j _ { 1 } \beta _ { Y } \vee j _ { 2 } \beta _ { X } } { 2 } } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } } ,
$$

then

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { D _ { X } } } \| G ( z , x ) - G ^ { \prime } ( z , x ) \| ^ { \gamma _ { 1 } } \leq \varepsilon .
$$

Therefore, we can get

$$
\begin{array} { r l } & { \bigl [ \underset { \displaystyle \hat { \mathcal { I } } = 0 , \infty } { \overset { \mathcal { I } } { \sum } } \varepsilon \Bigr ] \leq \displaystyle \prod _ { j = 1 } ^ { J _ { 1 } } \displaystyle \prod _ { \eta = \Theta } \prod _ { \eta \leq \frac { \hat { \mathcal { I } } _ { 1 } ^ { \Phi } } { 2 } } \prod _ { \eta \leq \frac { \hat { \mathcal { I } } _ { 1 } ^ { \Phi } } { 2 } } \prod _ { \eta = \Theta } W \bigl ( [ - L _ { 1 } ] - \frac { d \gamma _ { 1 } + \frac { \hat { \mathcal { I } } _ { 2 } \gamma _ { 1 } + \hat { \mathcal { I } } _ { 2 } \gamma _ { 1 } } { 2 } - ( ( j _ { 1 } \hat { \mathcal { I } } _ { 1 } \gamma ) \sqrt { ( j _ { 2 } \hat { \mathcal { I } } _ { 2 } \hat { \mathcal { I } } _ { 1 } ) } ) } { 2 } , L _ { 1 } ] ^ { - \frac { d \gamma _ { 1 } + \hat { \mathcal { I } } _ { 1 } \gamma _ { 1 } + \hat { \mathcal { I } } _ { 2 } } { 2 } - ( ( j _ { 1 } \hat { \mathcal { I } } _ { 1 } \gamma ) \sqrt { ( j _ { 2 } \hat { \mathcal { I } } _ { 2 } \hat { \mathcal { I } } _ { 2 } ) } ) } } \\ & { \qquad \times \displaystyle \prod _ { \zeta = \frac { \hat { \mathcal { I } } _ { 1 } ^ { \Phi } } { 2 } } \sum _ { \eta \leq \frac { \hat { \mathcal { I } } _ { 1 } ^ { \Phi } } { 2 } } \frac { d \gamma _ { 2 } \gamma _ { 1 } + d \gamma _ { 2 } } { 2 } \frac { d \gamma _ { 2 } - \frac { d \gamma _ { 1 } + \hat { \mathcal { I } } _ { 2 } \gamma _ { 2 } + \hat { \mathcal { I } } _ { 2 } \gamma _ { 1 } } { 2 } } { 2 } 2 ^ { - d \gamma _ { 1 } + \frac { d \gamma _ { 2 } \hat { \mathcal { I } } _ { 2 } } { 2 } } , \| \cdot \| \vert \rangle } \\ &  \leq \end{array}
$$

Moreover, for any $j \in [ J _ { 2 } ]$ , let $\mathcal { N } _ { 2 ^ { - j } } ^ { x }$ be the largest $2 ^ { - j }$ -packing set of $\mathcal { M } _ { x }$ , then $| \mathcal { N } _ { 2 ^ { - j } } ^ { x } | \lesssim 2 ^ { j d _ { X } }$ , and

$$
| \Psi _ { j } ^ { D x } | \leq \sum _ { x \in \mathcal { N } _ { 2 ^ { - j } } ^ { x } } \left| \left\{ \psi \in \overline { { \Psi } } _ { j } ^ { D x } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x , 2 ^ { - j } ) \neq \emptyset \right\} \right| \lesssim 2 ^ { j d _ { X } } .
$$

Hence there exists a constant $C _ { 2 }$ so that for any $\gamma _ { 1 }$ satisfying $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } \leq 2 \gamma _ { 1 } \leq 2 } \end{array}$ , it holds that

$$
\begin{array} { r } { \log \mathbf { N } ( \mathcal { G } , d _ { \infty } ^ { \gamma _ { 1 } } , \varepsilon ) \leq C _ { 2 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } \log \left( \frac { C _ { 2 } ( J _ { 1 } + J _ { 2 } ) 2 ^ { - \frac { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } { 4 \gamma _ { 1 } } - \frac { ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) } { 2 } } } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } } \vee 1 \right) . } \end{array}
$$

When $\begin{array} { r } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } > 2 \gamma _ { 1 } } \end{array}$ , denote

$$
s _ { j _ { 1 } j _ { 2 } } = \sqrt { \frac { 2 ^ { \frac { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } { 2 \gamma _ { 1 } } - \left( j _ { 1 } \beta _ { Y } \vee j _ { 2 } \beta _ { X } \right) } } { 2 ^ { \frac { d _ { Y } J _ { 1 } + d _ { X } J _ { 2 } } { 2 \gamma _ { 1 } } - \left( J _ { 1 } \beta _ { Y } \vee J _ { 2 } \beta _ { X } \right) } } } .
$$

There exists constants $C _ { 2 } , C _ { 3 }$ so that for any $\begin{array} { r } { \gamma _ { 1 } \in ( 0 , \frac { d _ { Y } } { 2 \beta _ { Y } } + \frac { d _ { X } } { 2 \beta _ { X } } ) } \end{array}$

$$
\begin{array} { r l } & { \varepsilon : = \displaystyle \sum _ { j = 1 } ^ { J _ { 1 } } \sum _ { j = 1 } ^ { J _ { 1 } } g _ { j } = \sqrt { \frac { 2 \delta x _ { j } x _ { j } } { 2 ^ { ( 1 ) \epsilon } x _ { j } + 2 \delta x _ { j } - 2 ( J _ { 1 } + J _ { 2 } ) \delta x _ { j } + 2 \delta x _ { 1 } } } \cdot \sum _ { j = 1 } ^ { J _ { 1 } } \frac { \delta \alpha _ { j } x _ { j } x _ { j } } { 2 ^ { ( 1 ) \epsilon } x _ { j } } \cdot \frac { 2 \delta x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } } { 2 } } \\ &  \leq \sqrt \frac { \displaystyle \sum _ { j = 1 } ^ { J _ { 1 } } \frac { \delta x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } } \cdot \left( \frac { 2 \delta x _ { j } x _ { j } x _ { j } } { 2 ^ { ( 1 ) \epsilon } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } } - \frac { 2 \delta x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } } { 2 ^ { ( 1 ) \epsilon } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } } + \frac { \delta x _ { j } x _ { j } x _ { j } } { 2 ^ { ( 1 ) \epsilon } x _ { j } x _ { j } } - \frac { \delta x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j }  } { 2 ^ { ( 1 ) \epsilon } x _ { j } + 1 } \cdot } \\ & \right. \leq \mathcal { C } _ { 2 } \sqrt \frac { 1 }  \displaystyle \frac  \delta x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _ { j } x _  \end{array}
$$

So if for any $j _ { 1 } \in [ J _ { 1 } ] , j _ { 2 } \in [ J _ { 2 } ] , \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } }$ , and $\psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } }$ ,

$$
\left\| g _ { \psi _ { 1 } \psi _ { 2 } } - g _ { \psi _ { 1 } \psi _ { 2 } } ^ { \prime } \right\| \le \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } j _ { 2 } } } { C S } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } } ,
$$

then

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { D _ { X } } } \| G ( z , x ) - G ^ { \prime } ( z , x ) \| ^ { \gamma _ { 1 } } \leq \varepsilon .
$$

Therefore, there exists a constant $C _ { 4 }$ so that for any $\begin{array} { r } { \gamma _ { 1 } \in ( 0 , \frac { d _ { Y } } { 2 \beta _ { Y } } + \frac { d _ { X } } { 2 \beta _ { X } } ) } \end{array}$

$$
\begin{array} { r l } & { \varepsilon ) \le \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \displaystyle \sum _ { \psi _ { 1 } \in \Psi _ { j _ { 1 } } ^ { d _ { Y } } } \displaystyle \sum _ { \psi _ { 2 } \in \Psi _ { j _ { 2 } } ^ { D _ { X } } } \log \mathbf { N } \big ( } \\ & { [ - L _ { 1 } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } - ( ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) ) } , L _ { 1 } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } - ( ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) ) } \big ] ^ { D _ { Y } } , \frac { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } j _ { 2 } } } { C S } 2 ^ { - \frac { d _ { Y } j _ { 1 } + D _ { X } j _ { 2 } } { 2 } } , } \\ & { \quad \le C _ { 4 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { d _ { Y } j _ { 1 } + d _ { X } j _ { 2 } } \log \Big ( \frac { C _ { 4 } S 2 ^ { - ( ( j _ { 1 } \beta _ { Y } ) \lor ( j _ { 2 } \beta _ { X } ) ) } } { \varepsilon ^ { \frac { 1 } { \gamma _ { 1 } } } s _ { j _ { 1 } j _ { 2 } } } \lor 1 \Big ) , } \end{array}
$$

which completes the proof.

# E Proof of Technical Details

# E.1 Proof of Lemma 7

Let $\zeta ~ = ~ ( \lceil { \alpha } \rceil ~ \vee ~ \lceil { \frac { d } { 2 } } ~ - ~ \alpha \rceil ) + 1$ and let $\phi { \mathfrak { M } }$ and $\phi _ { \mathfrak { F } }$ be the Daubechies wavelet and scaling function [Daubechies, 1992, Meyer, 1992] that are supported in a compact set $[ - C , C ]$ , have derivatives up to order $\zeta$ and

$$
\int _ { \mathbb { R } } x ^ { l } \psi _ { \mathfrak { M } } ( x ) \mathrm { d } x = 0 \quad f o r \quad l = 0 , \ldots , \zeta .
$$

Then by Proposition 1.51 of Tri [2006],

$$
\left\{ \begin{array} { l l } { \psi _ { \mathfrak { F } } ( x - k ) } & { j = 0 , k \in \mathbb { Z } , } \\ { 2 ^ { ( j - 1 ) / 2 } \psi _ { \mathfrak { M } } ( 2 ^ { j - 1 } x - k ) , } & { j \in \mathbb { N } _ { + } , k \in \mathbb { Z } , } \end{array} \right.
$$

is an orthonormal basis of ${ \mathcal { L } } ^ { 2 } ( \mathbb { R } )$ . Furthermore, by Proposition 1.53 of $\operatorname { T r i } \ [ 2 0 0 6 ]$ , to obtain a basis of $\mathcal { L } ^ { 2 } ( \mathbb { R } ^ { d } )$ for an integer $d > 1$ , set

$$
{ \mathfrak { G } } = \{ { \mathfrak { F } } , { \mathfrak { M } } \} ^ { d } \backslash \{ ( { \mathfrak { F } } , \dots , { \mathfrak { F } } ) \} .
$$

Then for any multi-index $k \in  { \mathbb { Z } ^ { d } }$ , the level zero basis $\phi _ { k } ^ { [ d ] }$ is obtained by translating the $d$ -fold tensor product $\phi _ { \mathfrak { F } } ^ { \otimes d }$ by $k$ as $\begin{array} { r } { \phi _ { k } ^ { [ d ] } ( x ) = \prod _ { i = 1 } ^ { d } \phi _ { \mathfrak { F } } ( x _ { i } - k _ { i } ) } \end{array}$ for $x = ( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { R } ^ { d }$ , and for any $j \geq 1$ , the level $j$ basis $\{ \psi _ { l j k } ^ { [ d ] } : l \in [ 2 ^ { d } - 1 ] \}$ with translation $k$ is any ordering of the following $2 ^ { d } - 1$ functions,

$$
\phi _ { g j k } ^ { [ d ] } ( x ) = 2 ^ { \frac { d ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { d } \phi _ { g _ { i } } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) , \quad \forall g \in \mathfrak { G } .
$$

This gives the orthornormal basis

$$
\left\{ \begin{array} { l l } { \phi _ { k } ^ { [ d ] } ( x ) , } & { j = 0 , l = 0 , k \in \mathbb { Z } ^ { d } , } \\ { \psi _ { l j k } ^ { [ d ] } ( x ) , } & { j \in \mathbb { N } _ { + } , l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } . } \end{array} \right.
$$

Denote $\overline { { \Psi } } _ { 0 } ^ { d } = \{ \phi _ { k } ^ { [ d ] } ( \cdot ) : k \in \mathbb { Z } ^ { d } \}$ as the set of level zero basis and $\overline { { \Psi } } _ { j } ^ { d } = \{ \psi _ { l j k } ^ { [ d ] } ( \cdot ) : l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } ^ { d } \}$ as the set of level $j$ basis for $j \in \mathbb { N } _ { + }$ . Then use the fact that for any $s \in \mathbb { N } _ { 0 } ^ { d }$ with $| s | \leq \alpha$ ,

$$
\phi _ { g j k } ^ { [ d ] } { } ^ { ( s ) } ( x ) = 2 ^ { \frac { d ( j - 1 ) } { 2 } } \prod _ { i = 1 } ^ { d } 2 ^ { ( j - 1 ) s _ { i } } \phi _ { g _ { i } } ^ { ( s _ { i } ) } \big ( 2 ^ { j - 1 } x _ { i } - k _ { i } \big ) \le C _ { R } 2 ^ { \frac { d j } { 2 } + j | s | } ,
$$

we can get the regularity condition. Moreover, by the compactness of the supports and smoothness of $\phi _ { \mathfrak { M } }$ and $\phi _ { \mathfrak { F } }$ , we have

$$
\mathrm { s u p p } ( \psi _ { l j k } ^ { [ d ] } ( s ) ) \subset \prod _ { i = 1 } ^ { d } [ \frac { - C + k _ { i } } { 2 ^ { j - 1 } } , \frac { C + k _ { i } } { 2 ^ { j - 1 } } ] = I _ { \psi _ { l j k } ^ { [ d ] } } .
$$

$$
\operatorname { s u p p } ( \phi _ { k } ^ { [ d ] ( s ) } ) \subset \prod _ { i = 1 } ^ { d } [ - C + k _ { i } , C + k _ { i } ] = I _ { \phi _ { k } ^ { [ d ] } } .
$$

So for any $x \in \mathbb { R } ^ { d } , j \in \mathbb { N }$ , and $l \in [ 2 ^ { d } - 1 ]$ , there are only constant number of $k$ so that $\psi _ { l j k } ^ { [ d ] } ( x ) \neq 0 ( j >$ 0) or $\phi _ { k } ^ { [ d ] } ( x ) \neq 0 ( j = 0 )$ . Hence $\begin{array} { r } { \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d } } \mathbf { 1 } ( x \in I _ { \psi } ) \leq C _ { L } ^ { \prime } } \end{array}$ . Moreover, if $I _ { \phi _ { k } ^ { [ d ] } } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( 0 , R ) \neq \emptyset$ , then $k \in [ - C - R , C + R ] ^ { d }$ ; if $I _ { \psi _ { l j k } ^ { [ d ] } } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( 0 , R ) \neq \emptyset$ , then $k \in [ 2 ^ { j - 1 } ( - C - R ) , 2 ^ { j - 1 } ( C + R ) ] ^ { d }$ , so | $\{ \psi \in \overline { { \Psi } } _ { j } ^ { d } : I _ { \psi } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( 0 , R ) \neq \emptyset \} \big | \le ( 2 ^ { d } - 1 ) ( 2 ^ { j } ( C + R ) + 1 ) ^ { d } \le ( 2 ^ { d } - 1 ) ( C + 2 ) ^ { d } R ^ { d } 2 ^ { j }$ d; if ${ \cal I } _ { \psi _ { l j k } ^ { [ d ] } } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( x , 2 ^ { - ( j - 1 ) } ) \neq \emptyset$ , then for any $i \ \in \ [ d ] , k _ { i } \ \in \ [ 2 ^ { j - 1 } x _ { i } - C , 2 ^ { j - 1 } x _ { i } + C ]$ , which means $\left| \{ \psi \in \overline { { \Psi } } _ { j } ^ { d } \ : \ I _ { \psi } \cap \mathbb { B } _ { \mathbb { R } ^ { d } } ( x , 2 ^ { - ( j - 1 ) } ) \ \neq \ \varnothing \} \right| \ \leq \ ( 2 ^ { d } - 1 ) ( 2 C + 1 ) ^ { d }$ . For the third statement, since $f \in \mathcal { H } _ { r } ^ { \alpha _ { 1 } } ( \mathbb { R } ^ { d } )$ , it holds for any $x , x _ { 0 } \in \mathbb { R } ^ { d }$ that

$$
\Big | f ( x ) - \sum _ { \stackrel { s \in \mathbb { N } _ { 0 } ^ { d } } { | s | < \alpha _ { 1 } } } \frac { f ^ { ( s ) } ( x _ { 0 } ) } { s ! } ( x - x _ { 0 } ) ^ { s } \Big | \leq r \| x - x _ { 0 } \| ^ { \alpha _ { 1 } } .
$$

Then for any $j \in \mathbb N$ and $\psi \in \overline { { \Psi } } _ { j } ^ { d }$ , we have

1. If $j = 0$ ,

$$
\int _ {  { { \mathbb R } } ^ { d } } f ( x ) \psi ( x ) \mathrm { d } x = \int _ { I _ { \psi } } f ( x ) \psi ( x ) \mathrm { d } x \leq \sqrt { \int _ { I _ { \psi } } \psi ^ { 2 } ( x ) \mathrm { d } x \int _ { I _ { \psi } } f ^ { 2 } ( x ) \mathrm { d } x } \leq ( 2 C ) ^ { \frac { d } { 2 } } r .
$$

2. If $j > 0$ , then we have for any $l \in  { \mathbb { N } } _ { 0 } ^ { d }$ with $| l | < \alpha _ { 1 }$

$$
\int _ { \mathbb R ^ { d } } x ^ { l } \psi ( x ) \mathrm d x = 0
$$

and thus for any $x _ { 0 } \in I _ { \psi }$ , we have

$$
\begin{array} { r l } & { \Bigl | \int _ { \infty } f ( z ) \phi ( x ) \mathrm { d } z \Bigr | = \Bigl | \int _ { \infty } \int _ { 0 } ^ { z } ( f ( x ) - f ( x _ { 0 } ) ) \mathrm { e } ( z ) \mathrm { d } z \Bigr | = \Bigl | \int _ { U } \zeta ( z ) - f ( x _ { 0 } ) \mathrm { e } ( z ) \mathrm { d } z \Bigr | } \\ & { - \Bigl | \int _ { U } \displaystyle \sum _ { u \in \mathbb { N } _ { 0 } } \frac { f ( x ) ( x _ { 0 } , x _ { 0 } ) } { z } \bigl ( \sigma - x _ { 0 } ) ^ { \phi } ( x ) \mathrm { d } z \Bigr | \le \int _ { U } f ( x ) - \displaystyle \sum _ { u \in \mathbb { N } _ { 0 } } \frac { f ( x , x _ { 0 } ) } { z } \bigl ( \sigma - x _ { 0 } ) ^ { \phi } ( x ) \mathrm { d } z \Bigr | } \\ & { \le \displaystyle \int _ { \infty } \int _ { \infty } ^ { z } \int _ { 0 } ^ { z } \zeta ( z ) - \displaystyle \sum _ { u \in \mathbb { N } _ { 0 } } \frac { f ( x ) ( x _ { 0 } , x _ { 0 } ) } { z } \zeta ( z - x _ { 0 } ) ^ { \phi } \Bigl | \cdot \mathrm { e } ( z ) \Bigr | \le \int _ { \infty } ^ { z } \int _ { 0 } ^ { z } \zeta ( z ) - f ( x ) \mathrm { d } z \Bigr | } \\ &  \le \displaystyle \int _ { \infty } ^ { z } \int _ { 0 } ^ { z } \zeta ( z ) \frac { \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi ( z ) \xi \xi ( z ) \xi ( z ) \xi \xi ( z ) \xi \xi ( z ) \xi \xi ( z ) \xi \xi ( z ) \xi \xi } \\ &  \le \displaystyle \int _ { \mathbb { R } _ { 0 } } ^ { z } | z - z _ { 0 } | ^ { \alpha } \left| \xi ( z ) \right| ^ { \alpha } \ \end{array}
$$

For the last statement. When $j = 0$ , we have

$$
\Psi _ { 0 } ^ { d } \subset \{ \phi _ { k } ^ { [ d ] } ( x ) : k \in \mathbb { Z } \mathrm { ~ a n d ~ } k \in [ - C _ { L } - R ^ { \prime } , C _ { L } + R ^ { \prime } ] ^ { d } \}
$$

Then we set

$$
\overline { { \mathcal { S } } } _ { 0 } = \{ ( \iota _ { 1 } , 0 ) : \iota _ { 1 } \in [ 0 , 1 ] ^ { d } \mathrm { ~ a n d ~ } ( 2 \iota _ { 1 } - 1 ) \cdot ( C _ { L } + R ^ { \prime } ) \in \mathbb { Z } ^ { d } \}
$$

and for any $\iota = ( \iota _ { 1 } , 0 ) \in \overline { { \mathcal { S } } } _ { 0 }$ , we set

$$
\phi _ { 0 \iota } ( \cdot ) = \phi _ { ( 2 \iota _ { 1 } - 1 ) \cdot ( C _ { L } + R ^ { \prime } ) } ^ { [ d ] } ) ( \cdot ) .
$$

Let

$$
\mathcal { I } _ { 0 } = \{ \iota \in \overline { { \mathcal { I } } } _ { 0 } : \phi _ { 0 \iota } ( \cdot ) \in \Psi _ { 0 } ^ { d } \} ,
$$

we have

$$
\Psi _ { 0 } ^ { d } = \{ \phi _ { 0 \iota } ( \cdot ) : \iota \in \mathcal { I } _ { 0 } \subset [ 0 , 1 ] ^ { d + 1 } \} ,
$$

and for any $\iota , \iota ^ { \prime } \in \mathcal { I } _ { 0 }$ with $\iota \neq \iota ^ { \prime }$ , it holds that $\begin{array} { r } { \| \iota - \iota ^ { \prime } \| \geq \frac { 1 } { 2 ( C _ { L } + R ^ { \prime } ) } } \end{array}$ . When $j > 0$ , we have

$$
\Psi _ { j } ^ { d } \subset \{ \psi _ { l j k } ^ { [ d ] } ( x ) : l \in [ 2 ^ { d } - 1 ] , k \in \mathbb { Z } \mathrm { ~ a n d ~ } k \in [ - 2 ^ { j - 1 } C _ { L } - R ^ { \prime } , 2 ^ { j - 1 } C _ { L } + R ^ { \prime } ] ^ { d } \} .
$$

Then we set

$\overline { { \mathcal { I } } } _ { j } = \{ \left( \iota _ { 1 } , \iota _ { 2 } \right) : \iota _ { 1 } \in [ 0 , 1 ] ^ { d } \mathrm { ~ a n d ~ } ( 2 \iota _ { 1 } - 1 ) \cdot ( 2 ^ { j - 1 } C _ { L } + R ^ { \prime } ) \in \mathbb { Z } ^ { d } , \iota _ { 2 } \in [ 0 , 1 ] \colon \ O ( \mathrm { Z } ^ { d } ) \} .$ and $\iota _ { 2 } ( 2 ^ { d - 1 } - 1 ) + 1 \in \mathbb { Z } \}$ , and for any $\iota = \left( \iota _ { 1 } , \iota _ { 2 } \right) \in \overline { { \mathcal { S } } } _ { j }$ , we set

$$
\phi _ { j \iota } = \psi _ { \iota _ { 2 } ( 2 ^ { d - 1 } - 1 ) + 1 , j , ( 2 \iota _ { 1 } - 1 ) \cdot ( C _ { L } + R ^ { \prime } ) } ^ { [ d ] } ( x ) .
$$

Let

$$
\mathcal { S } _ { j } = \{ \iota \in \overline { { \mathcal { I } } } _ { j } \ \phi _ { j \iota } \in \Psi _ { j } ^ { d } \} ,
$$

we have

$$
\begin{array} { r } { \Psi _ { j } ^ { d } = \{ \psi _ { j \iota } ( \cdot ) : \iota \in \mathcal { I } _ { j } \subset [ 0 , 1 ] ^ { d + 1 } \} , } \end{array}
$$

and for any $\iota , \iota ^ { \prime } \in \mathcal { I } _ { j }$ with $\iota \neq \iota ^ { \prime }$ , it holds that

$$
\| \iota - \iota ^ { \prime } \| \geq \frac { 1 } { 2 ^ { j } C _ { L } + 2 R ^ { \prime } } \wedge \frac { 1 } { 2 ^ { d - 1 } - 1 } .
$$

We can then get the desired result by combining all pieces.

# E.2 Proof of Lemma 1

Without loss of generality, we may assume $\alpha _ { 1 } \geq \alpha _ { 2 }$ . Given any $x \in \mathbb { R } ^ { d _ { 1 } }$ , and considering $f ( x , \cdot ) \in$ $\mathcal { H } _ { r } ^ { \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 2 } } )$ , it follows that for any $y _ { 0 } , y \in \mathbb { R } ^ { d _ { 2 } }$ ,

$$
\begin{array} { r l } & { f ( x , y ) - \displaystyle \sum _ { j _ { 2 } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } } } \frac { f ^ { ( 0 , j _ { 2 } ) } ( x , y _ { 0 } ) } { j _ { 2 } ! } ( y - y _ { 0 } ) ^ { j _ { 2 } } \Big | } \\ & { = \left\{ \begin{array} { l l } { \displaystyle \sum _ { j _ { 2 } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } } } \frac { \big [ 2 0 , j _ { 2 } \big ] } { j _ { 2 } ! } \int _ { 0 } ^ { 1 } ( 1 - t ) ^ { \lfloor \alpha _ { 2 } \rfloor - 1 } \big ( f ^ { ( 0 , j _ { 2 } ) } ( x , y _ { 0 } + t ( y - y _ { 0 } ) ) - f ^ { ( 0 , j _ { 2 } ) } ( x , y _ { 0 } ) \big ) \mathrm { d } t \cdot ( y - y _ { 0 } ) ^ { j _ { 2 } } } \\ { \displaystyle | f ( x , y ) - f ( x , y _ { 0 } ) | , } \\ { = \displaystyle O ( \| y - y _ { 0 } \| ^ { \alpha _ { 2 } } ) . } \end{array} \right. } \end{array}
$$

Moreover, using $f \in \mathcal { H } _ { r } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ , we have for any $x , x _ { 0 } \in \mathbb { R } ^ { d _ { 1 } }$ ,

$$
\begin{array} { r l } & { \quad \displaystyle \sum _ { b \geq \varepsilon } \frac { f ( \mathbf { J } ^ { ( b ) , j } ( x , \mathbf { J } ) ) } { \tilde { \mathbf { J } } ^ { ( b ) , j } } ( \psi - y _ { b } ) ^ { i _ { 1 } } - \sum _ { b \geq \varepsilon } \quad \sum _ { j \leq i _ { 1 } } \frac { f ^ { ( b ) , j } ( x , \mathbf { J } ) \cdot ( x _ { i } , \mathbf { A } ) ! } { \tilde { \mathbf { J } } ^ { ( b ) , j } } ( \psi - x _ { i } ) ^ { j _ { 1 } } ( y - y _ { b } ) ^ { j _ { 2 } } \Big | } \\ & { \mathrm { s i n c e : s o l } } \\ &  = \Big | \displaystyle \sum _ { b \geq \varepsilon } \quad \sum _ { j \leq i _ { 1 } } \frac { [ a _ { 1 } - c _ { 2 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 1 } ] } { \tilde { \mathbf { J } } ^ { ( b ) , j } } \int _ { 0 } ^ { 1 } ( 1 - I ) ^ { i _ { 2 } - 1 } \frac { x _ { i } [ a _ { 2 } ] \cdot [ a _ { 1 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 1 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 1 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 2 } ] \cdot [ a _ { 1 } ] \cdot [ ( \varepsilon - x _ { i } ) , \theta ] } \\ & { \quad \quad \times \mathrm { s i n c e : s i } } \\ & { \quad \quad \mathrm { b i n c e : s i } \frac { f ^ { ( b ) , j } } { \tilde { \mathbf { J } } ^ { ( b ) , j } } \frac { \partial \cdot \varepsilon } { \partial t } \mathrm { d } _ { i _ { 1 } } \mathrm { s i n c e : s i } \frac { \partial \cdot \varepsilon } { \partial t } | } \\ & { \quad \quad \times \left( \mathbf { J } - x _ { i } \right) ^ { j _ { 1 } } ( y - y _ { b } ) ^ { j _ { 2 } } \Big | } \\ &  \quad + \Big | \quad \sum _ { b \geq \varepsilon } \frac { 1 }  \tilde \end{array}
$$

where the last inequality uses the Young’s inequality for products. Therefore, we can get

$$
\begin{array} { l } { f ( x , y ) - \displaystyle \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } } } \frac { f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x _ { 0 } , y _ { 0 } ) } { j _ { 1 } ! j _ { 2 } ! } ( x - x _ { 0 } ) ^ { j _ { 1 } } ( y - y _ { 0 } ) ^ { j _ { 1 } } \Big | } \\ { = \Big | f ( x , y ) - \displaystyle \sum _ { j _ { 2 } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } } } \displaystyle \sum _ { j _ { 1 } \in \mathbb { N } _ { 0 } ^ { d _ { 1 } } } \frac { f ^ { ( j _ { 1 } , j _ { 2 } ) } ( x _ { 0 } , y _ { 0 } ) } { j _ { 2 } ! } ( x - x _ { 0 } ) ^ { j _ { 1 } } ( y - y _ { 0 } ) ^ { j _ { 2 } } \Big | = \mathcal { O } ( \| x - x _ { 0 } \| ^ { \alpha _ { 1 } } + \| y - y _ { 0 } \| ^ { \alpha _ { 1 } } ) } \\ { \displaystyle | j _ { 2 } | < \alpha _ { 2 } } \end{array}
$$

# E.3 Proof of Lemma 8

For any $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ , the function $f ( \cdot , y )$ has the following wavelet expansion

$$
f ( \cdot , y ) = \sum _ { j = 0 } ^ { \infty } \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d _ { 1 } } } \psi ( \cdot ) f _ { \psi } ( y ) , \quad f _ { \psi } ( y ) = \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) \psi ( x ) \mathrm { d } x ,
$$

with $| f _ { \psi } ( y ) | \le C _ { W } L 2 ^ { - \frac { d _ { 1 } j } 2 - j \alpha _ { 1 } }$ when $\psi \in \overline { { \Psi } } _ { j } ^ { d _ { 1 } }$ . Then we have

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { d _ { 1 } } } \Big | \sum _ { j = J _ { 1 } + 1 } ^ { \infty } \sum _ { \psi \in \Psi _ { j } } \psi ( x ) f _ { \psi } ( y ) \Big | \le C _ { R } C _ { L } ^ { \prime } C _ { W } L \sum _ { j = J _ { 1 } + 1 } ^ { \infty } 2 ^ { - j \alpha _ { 1 } } \le C _ { R } C _ { L } ^ { \prime } C _ { W } L 2 ^ { - J _ { 1 } \alpha _ { 1 } } .
$$

Moreover, for any $j _ { 1 } \in [ J _ { 1 } ]$ and $\psi \in \overline { { \Psi } } _ { j _ { 1 } } ^ { d _ { 1 } }$ , it holds that

$$
2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } \int _ { \mathbb { R } ^ { d _ { 1 } } } | \psi ( x ) | \mathrm { d } x \leq 2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } \int _ { I _ { \psi } } \mathrm { d } x \cdot \operatorname* { s u p } _ { x \in I _ { \psi } } | \psi ( x ) | \leq ( 2 C _ { L } ) ^ { d _ { 1 } } C _ { R } .
$$

Furthermore, for any multi-index $\ell \in \mathbb { N } _ { 0 } ^ { d _ { 2 } }$ with $| \ell | < \alpha$ , it holds that

$$
\begin{array} { r } { 2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } f _ { \psi } ^ { ( \ell ) } ( y ) = 2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } \left[ \displaystyle \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , \cdot ) \psi ( x ) { \mathrm { d } } x \right] ^ { ( \ell ) } ( y ) } \\ { = 2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } \displaystyle \int _ { \mathbb { R } ^ { d _ { 1 } } } f ^ { ( \mathbf { 0 } _ { d _ { 1 } } , \ell ) } ( x , y ) \psi ( x ) { \mathrm { d } } x . } \end{array}
$$

Therefore, there exists a constant $L _ { 1 } = ( 2 C _ { L } ) ^ { d _ { 1 } } C _ { R } L$ so that

$$
2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } f _ { \psi } ( y ) = 2 ^ { \frac { d _ { 1 } j _ { 1 } } { 2 } } \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) \psi ( x ) \mathrm { d } x \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 2 } } ) .
$$

For any $j _ { 1 } \in \mathbb { N }$ and $\psi \in \overline { { \Psi } } _ { j _ { 1 } } ^ { d _ { 1 } } , f _ { \psi } ( \cdot )$ has the following wavelet expansion

$$
f _ { \psi } ( y ) = \sum _ { j _ { 2 } = 0 } ^ { \infty } \sum _ { \phi \in \overline { { \Psi } } _ { j _ { 2 } } ^ { d _ { 2 } } } \phi ( y ) f _ { \psi , \phi } , \quad f _ { \psi , \phi } = \int _ { \mathbb { R } ^ { d _ { 2 } } } f _ { \psi } ( y ) \phi ( y ) \mathrm { d } y = \int _ { \mathbb { R } ^ { d _ { 2 } } } \int _ { \mathbb { R } ^ { d _ { 1 } } } f ( x , y ) \psi ( x ) \phi ( y ) \mathrm { d } x \mathrm { d } y
$$

with $| \widetilde { f } _ { \psi , \phi } | \le C _ { W } L _ { 1 } 2 ^ { - \frac { d _ { 1 } j _ { 1 } + d _ { 2 } j _ { 2 } } { 2 } } 2 ^ { - j _ { 2 } \alpha _ { 2 } }$ for any $\boldsymbol { \psi } \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } }$ and $\phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } }$ . Then let

$$
f ^ { \prime } ( x , y ) = \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi \in \overline { { \Psi } } _ { j _ { 1 } } ^ { d _ { 1 } } } \sum _ { \psi \in \overline { { \Psi } } _ { j _ { 2 } } ^ { d _ { 2 } } } f _ { \psi , \phi } \psi ( x ) \phi ( y ) ,
$$

we have

$$
\begin{array} { r l } & { | f ^ { \prime } ( x , y ) - f ( x , y ) | \leq \Big | \displaystyle \sum _ { j = J _ { 1 } + 1 } ^ { \infty } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j } ^ { d _ { 1 } } } \psi ( x ) f _ { \psi } ( y ) \Big | + \Big | \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { j _ { 2 } = J _ { 2 } + 1 } ^ { \infty } \displaystyle \sum _ { \phi \in \overline { { \Psi } } _ { j _ { 2 } } ^ { d _ { 2 } } } f _ { \psi , \phi } \psi ( x ) \phi ( y ) \Big | } \\ & { \leq C _ { R } C _ { L } ^ { \prime } C _ { W } L 2 ^ { - J _ { 1 } \alpha _ { 1 } } + C _ { R } C _ { L } ^ { \prime } C _ { W } L _ { 1 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } 2 ^ { - \frac { d _ { 1 } j _ { 1 } } { 2 } } 2 ^ { - J _ { 2 } \alpha _ { 2 } } | \psi ( x ) | } \\ & { \leq C _ { R } C _ { L } ^ { \prime } C _ { W } L 2 ^ { - J _ { 1 } \alpha _ { 1 } } + 2 ^ { d _ { 1 } } C _ { R } ^ { 3 } C _ { L } ^ { \prime } ^ { 2 } C _ { W } C _ { L } ^ { d _ { 1 } } L ^ { 2 - J _ { 2 } \alpha _ { 2 } } . } \end{array}
$$

# E.4 Proof of Lemma 2

Without loss of generality, we assume $U _ { 1 } \subseteq \mathbb { B } _ { \mathbb { R } ^ { d _ { 1 } } } ( \mathbf { 0 } , 1 )$ and $U _ { 2 } \subseteq \mathbb { B } _ { \mathbb { R } ^ { d _ { 2 } } } ( \mathbf { 0 } , 1 )$ . Then consider a smooth transition function

$$
\rho ( t ) = \left\{ \begin{array} { c c } { 0 } & { | t | \geq 2 } \\ { 1 } & { | t | \leq 1 } \\ { \frac { 1 } { 1 + \exp ( \frac { 3 - 2 t } { ( t - 1 ) ( t - 2 ) } ) } } & { 1 < t < 2 } \\ { \frac { 1 } { 1 + \exp ( \frac { 2 t + 3 } { ( t + 1 ) ( 2 + t ) } ) } } & { - 2 < t < - 1 . } \end{array} \right.
$$

Set $\widetilde { f } ( x , y ) = \overline { { f } } ( x , y ) \rho ( \| x \| ^ { 2 } ) \rho ( \| y \| ^ { 2 } )$ . We have $\widetilde { f } ( x , y ) \in \overline { { \mathcal { H } } } _ { L ^ { \prime } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ , $\widetilde { f } | _ { U _ { 1 } \times U _ { 2 } } = \overline { { f } } | _ { U _ { 1 } \times U _ { 2 } }$ and the support of $\widetilde { f }$ is contained in $\mathbb { B } _ { \mathbb { R } ^ { d _ { 1 } } } ( \mathbf { 0 } , \sqrt { 2 } ) \times \mathbb { B } _ { \mathbb { R } ^ { d _ { 2 } } } ( \mathbf { 0 } , \sqrt { 2 } )$ . Consider two wavelet basis $\{ \overline { { \Psi } } _ { j } ^ { d _ { 1 } } \} _ { j \ge 0 }$ and $\{ \overline { { \Psi } } _ { j } ^ { d _ { 2 } } \} _ { j \ge 0 }$ that both satisfy the properties in Lemma 7 with smoothness $\alpha = \lceil \alpha _ { 1 } \lor \alpha _ { 2 } \rceil$ and constants $C _ { R } , \bar { C } _ { L } , C _ { L } ^ { \prime } , C _ { L } ^ { \dagger } , C _ { L } ^ { \dagger } , C _ { W } , C _ { I }$ . For any $j \in \mathbb N$ , define

$$
\Psi _ { j } ^ { d _ { 1 } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { 1 } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { 1 } } } ( \mathbf { 0 } , \sqrt { 2 } ) \neq \emptyset \} ,
$$

and

$$
\Psi _ { j } ^ { d _ { 2 } } = \{ \psi \in \overline { { \Psi } } _ { j } ^ { d _ { 2 } } : \operatorname { s u p p } ( \psi ) \cap \mathbb { B } _ { \mathbb { R } ^ { d _ { 2 } } } ( \mathbf { 0 } , \sqrt { 2 } ) \neq \emptyset \} .
$$

we have $| \Psi _ { j } ^ { d _ { 1 } } | \leq \sqrt { 2 } C _ { L } ^ { \dagger } 2 ^ { d _ { 1 } j }$ and $| \Psi _ { j } ^ { d _ { 2 } } | \leq \sqrt { 2 } C _ { L } ^ { \dagger } 2 ^ { d _ { 2 } j }$ . Set

$$
J _ { 1 } = \lceil \frac { \log ( 2 C _ { R } C _ { L } ^ { \prime } C _ { W } L ^ { \prime } ) + \log \frac { 1 } { \varepsilon } } { \alpha _ { 1 } \log 2 } \rceil
$$

and

$$
J _ { 2 } = \lceil { \frac { \log ( 2 ^ { d _ { 1 } + 1 } C _ { R } ^ { 3 } C _ { L } ^ { \prime } { } ^ { 2 } C _ { W } C _ { L } ^ { d _ { 1 } } L ^ { \prime } J _ { 1 } ) + \log { \frac { 1 } { \varepsilon } } } { \alpha _ { 2 } \log 2 } } \rceil .
$$

Define

$$
\begin{array} { r l r } { \widetilde { f } ^ { \prime } ( x , y ) = \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \psi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde { f } _ { \psi , \phi } \psi ( x ) \phi ( y ) } & \\ { = \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \displaystyle \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \psi \in \overline { { \Psi } } _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde { f } _ { \psi , \phi } \psi ( x ) \phi ( y ) , } & { \widetilde { f } _ { \psi , \phi } = \displaystyle \int _ { \mathbb { R } ^ { d _ { 2 } } } \displaystyle \int _ { \mathbb { R } ^ { d _ { 1 } } } \widetilde { f } ( x , y ) \psi ( x ) \phi ( y ) { \mathrm { d } } x { \mathrm { d } } y } & \end{array}
$$

It holds that

$$
\vert \widetilde { f } ^ { \prime } ( x , y ) - \widetilde { f } ( x , y ) \vert \le C _ { R } C _ { L } ^ { \prime } C _ { W } L ^ { \prime } 2 ^ { - J _ { 1 } \alpha _ { 1 } } + 2 ^ { d _ { 1 } } C _ { R } ^ { 3 } C _ { L } ^ { \prime } { } ^ { 2 } C _ { W } C _ { L } ^ { d _ { 1 } } L ^ { \prime } J _ { 1 } 2 ^ { - J _ { 2 } \alpha _ { 2 } } \le \varepsilon .
$$

Now we show that $\widetilde { f } ^ { \prime } ( x , y ) \in \mathcal { H } _ { L _ { 0 } J _ { 1 } J _ { 2 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ for a constant $L _ { 0 }$ . Notice that for any $\psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } }$ and $\phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } }$ , we have

$$
\begin{array} { r l } & { | \widetilde f _ { \psi , \phi } | = \big | \displaystyle \int _ { \mathbb R ^ { d _ { 2 } } } \int _ { \mathbb R ^ { d _ { 1 } } } \widetilde f ( x , y ) \psi ( x ) \phi ( y ) { \mathrm { d } } x { \mathrm { d } } y \big | \le \displaystyle \int _ { \mathbb R ^ { d _ { 2 } } } | \widetilde f _ { \psi } ( y ) | \cdot | \phi ( y ) | { \mathrm { d } } y } \\ & { \le C _ { W } L 2 ^ { - \frac { d _ { 1 } j _ { 1 } } 2 - j _ { 1 } \alpha _ { 1 } } \displaystyle \int _ { \mathbb R ^ { d _ { 2 } } } | \phi ( y ) | { \mathrm { d } } y } \\ & { \le C _ { W } L ( 2 C _ { L } ) ^ { d _ { 1 } } C _ { R } 2 ^ { - \frac { d _ { 1 } j _ { 1 } + d _ { 2 } j _ { 2 } } 2 - j _ { 1 } \alpha _ { 1 } } . } \end{array}
$$

Combined with $| \widetilde { f } _ { \psi , \phi } | \le C _ { W } L _ { 1 } 2 ^ { - \frac { d _ { 1 } j _ { 1 } + d _ { 2 } j _ { 2 } } { 2 } } 2 ^ { - j _ { 2 } \alpha _ { 2 } }$ − d1j1+d2j22 2−j2α2 , we can estbalish that, for some constant L2,

$$
| \widetilde { f } _ { \psi , \phi } | \leq L _ { 2 } 2 ^ { - \frac { d _ { 1 } j _ { 1 } + d _ { 2 } j _ { 2 } } { 2 } } 2 ^ { - \left( \left( j _ { 1 } \alpha _ { 1 } \right) \vee \left( j _ { 2 } \alpha _ { 2 } \right) \right) } .
$$

Then, for any $\begin{array} { r } { ( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } } = \{ l _ { 1 } \in \mathbb { N } _ { 0 } ^ { d _ { 1 } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } } : \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } < 1 \} } \end{array}$ , we have

$$
\begin{array} { r l } & { \displaystyle \left| \widetilde { f } ^ { ( \ell _ { 1 } , \ell _ { 2 } ) } ( x , y ) | = \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi \in \mathcal { S } _ { j _ { 1 } } ^ { \ell _ { 1 } } } \sum _ { \psi \in \mathcal { S } _ { j _ { 2 } } ^ { \ell _ { 1 } } } \widetilde { f } _ { \psi , \psi } ( \ell ^ { \ell _ { 1 } } ) ( x ) \phi ^ { ( \ell _ { 2 } ) } ( y ) \right| } \\ & { \leq L _ { 2 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi \in \mathcal { S } _ { j _ { 1 } } ^ { \ell _ { 1 } } } \sum _ { \phi \in \mathcal { S } _ { j _ { 2 } } ^ { \ell _ { 2 } } } 2 ^ { - ( \ell ( j _ { 1 } \alpha ) ) \psi ( j _ { 2 } \alpha ) } 2 ^ { - \frac { \ell _ { 1 } j _ { 1 } + \ell _ { 2 } j _ { 2 } } { 2 } } | \psi ^ { ( I _ { 1 } ) } ( x ) \phi ^ { ( \ell _ { 2 } ) } ( y ) | } \\ &  \leq L _ { 2 } \displaystyle \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } \sum _ { \psi \in \mathcal { S } _ { j _ { 1 } } ^ { \ell _ { 1 } } } \sum _ { \psi = \mathcal { S } _ { j _ { 2 } } ^ { \ell _ { 1 } } } 2 ^ { - ( \ell ( j _ { 1 } \alpha ) ) \psi ( j _ { 2 } \alpha _ { 2 } ) ) } 2 ^ { - \frac { \ell _ { 1 } j _ { 1 } + \ell _ { 2 } j _ { 2 } } { 2 } } C _ { R } ^ { 2 } 2 ^ { j _ { 1 } | \ell _ { 1 } | + \frac { \ell _ { 2 } j _ { 1 } } { 2 } } 2 ^ \end{array}
$$

Notice that when $\begin{array} { r } { j _ { 1 } \le \frac { j _ { 2 } \alpha _ { 2 } } { \alpha _ { 1 } } } \end{array}$ , we have

$$
- j _ { 2 } \alpha _ { 2 } + | l _ { 1 } | j _ { 1 } + | l _ { 2 } | j _ { 2 } \le - j _ { 2 } \alpha _ { 2 } + | l _ { 1 } | \frac { j _ { 2 } \alpha _ { 2 } } { \alpha _ { 1 } } + | l _ { 2 } | j _ { 2 } = j _ { 2 } ( | l _ { 1 } | \frac { \alpha _ { 2 } } { \alpha _ { 1 } } + | l _ { 2 } | - \alpha _ { 2 } ) < 0 ,
$$

and when $\begin{array} { r } { j _ { 1 } \geq \frac { j _ { 2 } \alpha _ { 2 } } { \alpha _ { 1 } } } \end{array}$ j2α2 , we have

$$
- j _ { 1 } \alpha _ { 1 } + | l _ { 1 } | j _ { 1 } + | l _ { 2 } | j _ { 2 } \le - j _ { 1 } \alpha _ { 1 } + | l _ { 1 } | j _ { 1 } + | l _ { 2 } | \frac { j _ { 1 } \alpha _ { 1 } } { \alpha _ { 2 } } = j _ { 1 } ( | l _ { 2 } | \frac { \alpha _ { 1 } } { \alpha _ { 2 } } + | l _ { 1 } | - \alpha _ { 1 } ) < 0
$$

Therefore,

$$
| \widetilde { f } ^ { \prime } ( l _ { 1 } , l _ { 2 } ) ( x , y ) | \leq L _ { 3 } \sum _ { j _ { 1 } = 0 } ^ { J _ { 1 } } 2 ^ { j _ { 1 } ( | l _ { 2 } | \frac { \alpha _ { 1 } } { \alpha _ { 2 } } + | l _ { 1 } | - \alpha _ { 1 } ) } + L _ { 3 } \sum _ { j _ { 2 } = 0 } ^ { J _ { 2 } } 2 ^ { j _ { 2 } ( | l _ { 1 } | \frac { \alpha _ { 2 } } { \alpha _ { 1 } } + | l _ { 2 } | - \alpha _ { 2 } ) } \leq L _ { 4 } .
$$

Then consider $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } \wedge \alpha _ { 2 } } \geq 1 } \end{array}$ , we claim that

Claim 1. There exists a constant $L _ { 4 }$ so that for any $x , x ^ { \prime } \in \mathbb { R } ^ { d _ { 1 } }$ , $y , y ^ { \prime } \in \mathbb { R } ^ { d _ { 2 } }$ , $j _ { 1 } \in [ J _ { 1 } ]$ and $j _ { 2 } \in [ J _ { 2 } ]$ ,

1. for any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } } \ge 1 } \end{array}$ ,

$$
\begin{array} { r l } & { \big | \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) - \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) \phi ^ { ( l _ { 2 } ) } ( y ) \big | } \\ & { \leq L _ { 4 } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } . } \end{array}
$$

2. for any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \ge 1 , } \end{array}$

$$
\begin{array} { r l } & { \displaystyle | \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) - \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ^ { \prime } ) | } \\ & { \le L _ { 4 } \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - | l _ { 2 } | - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | } . } \end{array}
$$

Then given Claim 1, we can derive that for any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } } \ge 1 } \end{array}$

$$
\begin{array} { r } { | \widetilde { f } ^ { \prime } ( l _ { 1 } , l _ { 2 } ) ( x , y ) - \widetilde { f } ^ { \prime } ( l _ { 1 } , l _ { 2 } ) ( x ^ { \prime } , y ) | \leq J _ { 1 } J _ { 2 } L _ { 4 } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } , } \end{array}
$$

and for any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \ge 1 } \end{array}$ ,

$$
\begin{array} { r } { | \widetilde { f } ^ { \prime ( l _ { 1 } , l _ { 2 } ) } ( x , y ) - \widetilde { f } ^ { \prime ( l _ { 1 } , l _ { 2 } ) } ( x , y ^ { \prime } ) | \leq J _ { 1 } J _ { 2 } L _ { 4 } \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - | l _ { 2 } | - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | } . } \end{array}
$$

Together with (48), these results confirm that $\widetilde { f } ^ { \prime } \in \mathcal { H } _ { L _ { 0 } J _ { 1 } J _ { 2 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$ with some constant $L _ { 0 }$ . Finally, by choosing $f = \widetilde { f } ^ { \prime }$ , we can get the the desired result.

We now present the proof of Claim 1. Consider an arbitrary pair $j _ { 1 } \in [ J _ { 1 } ]$ and $j _ { 2 } \in [ J _ { 2 } ]$ . Without loss of generality, we assume that $j _ { 1 } \le j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } }$ . The proof for the case where $j _ { 1 } \geq j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } }$ follows a similar argument. For the first statement, consider an arbitrary (l1, l2) ∈ J d1,d2α1,α2 with |l1|α1 + |lα $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } } \ge 1 } \end{array}$ 1α ≥ 1, then when $\| x - x ^ { \prime } \| \geq 2 ^ { - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } }$ , there exists a constant $L _ { 4 }$ so that the following inequality holds:

$$
\begin{array} { r l } & { \quad \displaystyle \sum _ { \psi \in \Psi _ { j 1 } ^ { d } } \displaystyle \sum _ { \psi \in \Psi _ { j 2 } ^ { d } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) - \sum _ { \psi \in \Psi _ { j 1 } ^ { d } } \sum _ { \psi \in \Psi _ { j 2 } ^ { d } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) \phi ^ { ( l _ { 2 } ) } ( y ) \Big | } \\ & { \le \Big | \displaystyle \sum _ { \psi \in \Psi _ { j 1 } ^ { d } } \sum _ { \psi \in \Psi _ { j 2 } ^ { d } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) \Big | + \Big | \displaystyle \sum _ { \psi \in \Psi _ { j 1 } ^ { d } } \sum _ { \psi \in \Psi _ { j 2 } ^ { d } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) \phi ^ { ( l _ { 2 } ) } ( y ) \Big | } \\ & { \le L _ { 4 } 2 ^ { - j _ { 2 } \alpha _ { 2 } + j _ { 1 } | l _ { 1 } | + j _ { 2 } | l _ { 2 } | } } \\ & { = L _ { 4 } 2 ^ { - j _ { 2 } ( - \alpha _ { 2 } + \frac { 3 } { \frac { 1 } { \alpha _ { 2 } } } | l _ { 1 } | + | l _ { 2 } | ) } } \\ & { \le L _ { 4 } 2 ^ { - \frac { 2 } { \alpha _ { 2 } ( \alpha _ { 2 } - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | - | l _ { 2 } | ) } } } \\ & { \le L _ { 4 } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } . } \end{array}
$$

When $\| x - x ^ { \prime } \| \leq 2 ^ { - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } }$ , we have

$$
\begin{array} { r l } & { \Big | \displaystyle \sum _ { y \in \Psi _ { 1 } ^ { d } } \displaystyle \sum _ { \phi \in \Psi _ { 2 } ^ { d } } \widetilde f _ { y , \phi } \psi ^ { ( 1 ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) - \displaystyle \sum _ { \psi \in \Psi _ { 1 } ^ { d } } \displaystyle \sum _ { \phi \in \Psi _ { 2 } ^ { d } } \widetilde f _ { \phi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) \phi ^ { ( l _ { 2 } ) } ( y ) \Big | } \\ & { \le \displaystyle \sum _ { y \in \Psi _ { 1 } ^ { d } } \displaystyle \sum _ { \phi \in \Psi _ { 2 } ^ { d } } | \psi ^ { ( l _ { 1 } ) } ( x ) - \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) | \cdot | \widetilde f _ { \phi , \phi } \psi ^ { ( l _ { 2 } ) } ( y ) | } \\ & { \le C _ { n } C _ { l } ^ { \prime } L _ { 2 ^ { 2 } } \frac { 1 + n \alpha _ { n } - 2 \frac { 1 + 1 } { 2 } } { 2 } \operatorname* { i } j _ { 2 } | l _ { 2 } | \displaystyle \sum _ { y \in \Psi _ { 1 } ^ { d } } | l _ { 1 } ^ { ( 1 ) } ( x ) - \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) | } \\ & { \le C _ { n } C _ { L } ^ { \prime } L _ { 2 ^ { 2 } } - j _ { 2 } \alpha _ { n } - \frac { 1 + 1 } { 2 } \operatorname* { i } j _ { 2 } | l _ { 2 } | \displaystyle \sum _ { y \in \Psi _ { 1 } ^ { d } } | l _ { 1 } ^ { ( 1 ) } ( x ) - \psi ^ { ( l _ { 1 } ) } ( x ^ { \prime } ) | \cdot \big ( 1 ( x \in I _ { \psi } ) + 1 ( x ^ { \prime } \in I _ { \psi } ) \big ) } \\ &  \le C _ { n } C _ { L } ^ { \prime } L _ { 2 ^ { 2 } } \frac { 1 } { 2 } \frac  1 + n \alpha _ { n } + 2 \operatorname* { i }  \eta  \end{array}
$$

where the last inequality uses $\| \nabla \psi ^ { ( l _ { 1 } ) } ( x ) \| \lesssim 2 ^ { \frac { j _ { 1 } d _ { 1 } } { 2 } + | l _ { 1 } | j _ { 1 } + j _ { 1 } }$ . Given that $\| x - x ^ { \prime } \| \leq 2 ^ { - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } }$ , ${ \frac { | l _ { 1 } | } { \alpha _ { 1 } } } +$ $\begin{array} { r } { \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } } \ge 1 } \end{array}$ and $j _ { 1 } \leq j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } }$ , we deduce that

$$
\begin{array} { r l } & { - j _ { 2 } \alpha _ { 2 } + j _ { 1 } ( | l _ { 1 } | + 1 ) + j _ { 2 } | l _ { 2 } | \| x - x ^ { \prime } \| = 2 ^ { - j _ { 2 } \alpha _ { 2 } + j _ { 1 } ( | l _ { 1 } | + 1 ) + j _ { 2 } | l _ { 2 } | } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } \| x - x ^ { \prime } \| ^ { 1 - \alpha _ { 1 } + | l _ { 1 } | + } } \\ & { \leq 2 ^ { - j _ { 2 } \alpha _ { 2 } + j _ { 1 } ( | l _ { 1 } | + 1 ) + j _ { 2 } | l _ { 2 } | - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } ( 1 - \alpha _ { 1 } + | l _ { 1 } | + \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | ) } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } } \\ & { = 2 ^ { j _ { 1 } ( | l _ { 1 } | + 1 ) - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } ( 1 + | l _ { 1 } | ) } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } } \\ & { \leq \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } . } \end{array}
$$

This completes the proof of the first statement in Claim 1. Next, we prove the second statement. Consider an arbitrary $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \ge 1 } \end{array}$ . When $\| y - y ^ { \prime } \| \geq 2 ^ { - j _ { 2 } }$ , we have

$$
\begin{array} { r l } & { \Big | \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) - \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ^ { \prime } ) \Big | } \\ & { \le \Big | \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ) \Big | + \Big | \displaystyle \sum _ { \psi \in \Psi _ { j _ { 1 } } ^ { d _ { 1 } } } \displaystyle \sum _ { \phi \in \Psi _ { j _ { 2 } } ^ { d _ { 2 } } } \widetilde f _ { \psi , \phi } \psi ^ { ( l _ { 1 } ) } ( x ) \phi ^ { ( l _ { 2 } ) } ( y ^ { \prime } ) \Big | } \\ & { \le L _ { 4 } 2 ^ { - j _ { 2 } ( \alpha _ { 2 } - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | - | l _ { 2 } | ) } } \\ & { \le L _ { 4 } \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | - | l _ { 2 } | } . } \end{array}
$$

When $\| y - y ^ { \prime } \| \leq 2 ^ { - j _ { 2 } }$ , we have

$$
\begin{array} { r l } & { \quad \displaystyle \sum _ { y \in S _ { j _ { 1 } } ^ { { \theta } } } \displaystyle \sum _ { i \in S _ { j _ { 2 } } ^ { { \theta } } } \displaystyle \sum _ { j _ { 1 } \in S _ { j _ { 2 } } ^ { { \theta } } }  j _ { 1 } ^ { ( k ) } ( x ) \phi ^ { ( k ) } ( y ) - \displaystyle \sum _ { y \in S _ { j _ { 1 } } ^ { k } \geq S _ { j _ { 2 } } ^ { k } } \displaystyle \sum _ { i \in S _ { j _ { 2 } } ^ { k } \geq \theta } \hat { j } _ { i \in S _ { j _ { 2 } } ^ { k } } \| \phi ^ { ( k ) } ( y ) \phi ^ { ( k ) } \| } \\ & { \leq \displaystyle \sum _ { y \in S _ { j _ { 1 } } ^ { k } \geq S _ { j _ { 1 } } ^ { k } } \displaystyle \sum _ { i \in S _ { j _ { 2 } } ^ { k } \geq \theta } | \hat { j } _ { i \in S _ { j } } ^ { k } ( x ) | \cdot | \phi ^ { ( k ) } ( y ) - \phi ^ { ( k ) } ( y ) \phi ^ { ( k ) } | } \\ & { \quad \displaystyle \leq C _ { n } C _ { j _ { 1 } } ^ { k } L _ { 2 ^ { 2 } } - \frac { 2 i \theta L _ { 2 } } { 2 } \cdot \| \hat { j } _ { 1 } | _ { 1 } | \displaystyle \sum _ { \phi \in S _ { j _ { 2 } } ^ { k } \geq \theta } \| \phi ^ { ( k ) } ( y ) - \phi ^ { ( k ) } ( y ) \| } \\ & { \leq C _ { n } C _ { L } ^ { \theta } L _ { 2 ^ { 2 } } - j _ { 2 } \alpha _ { 2 } - \frac { 2 i \theta L _ { 2 } } { 2 } + j _ { 1 } | _ { 1 } | \displaystyle \sum _ { \phi \in V _ { j _ { 2 } } ^ { k } \geq \theta } \| \phi ^ { ( k ) } ( y ) - \phi ^ { ( k ) } ( y ) \| \cdot \big ( 1 ( y \in I _ { \phi } ) + 1 ( y ^ { \prime } \in I _ { \phi } ) \big ) } \\ &  \leq C _  n \end{array}
$$

where the last inequality uses $\begin{array} { r } { \| \nabla \phi ^ { ( l _ { 2 } ) } ( y ) \| \lesssim 2 ^ { \frac { j _ { 2 } d _ { 2 } } { 2 } + | l _ { 2 } | j _ { 2 } + j _ { 2 } } } \end{array}$ . Then given that $\begin{array} { r } { \| y - y ^ { \prime } \| \leq 2 ^ { - j _ { 2 } } , \frac { | l _ { 1 } | } { \alpha _ { 1 } } + } \end{array}$ $\begin{array} { r } { \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \ge 1 } \end{array}$ and $j _ { 1 } \leq j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } }$ , we obtain

$$
\begin{array} { r l } & { - j _ { 2 } \alpha _ { 2 } + j _ { 1 } | l _ { 1 } | + j _ { 2 } ( | l _ { 2 } | + 1 ) } \\ & { \leq 2 ^ { j _ { 1 } | l _ { 1 } | - j _ { 2 } \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | } \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | - | l _ { 2 } | } } \\ & { \leq \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | - | l _ { 2 } | } . } \end{array}
$$

This completes the proof.

# E.5 Proof of Lemma 3

# E.5.1 $( 3 ) \Rightarrow ( 2 )$

Consider a small enough positive constant $\begin{array} { r } { \overline { { \tau } } _ { 2 } \leq \frac { \overline { { \tau } } } { 2 } } \end{array}$ that will be specified later, and take an arbitrary point $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M } = \{ ( x , y ) : x \in \mathcal { M } _ { X } , y \in \bar { \mathcal { M } } _ { Y | x } \} \mathrm { . }$ . Let $V ^ { \bar { * } } \in \mathbb { R } ^ { D _ { Y } \times d _ { Y } }$ be a matrix whose column forms an orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } } y _ { 0 }$ and let $V ^ { * \perp } \in \mathbb { R } ^ { D _ { Y } \times ( D _ { Y } - d _ { Y } ) }$ be the orthogonal complement of $V ^ { * }$ . Consider $\overline { { F } } _ { \omega _ { 0 } } \in \mathcal { \overline { H } } _ { \overline { { L } } , D _ { Y } - d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ so that $\overline { { F } } _ { \omega _ { 0 } } | _ { \mathbb { B } _ { \mathbb { R } ^ { D } \Gamma } ( y _ { 0 } , \overline { { \tau } } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) } = F _ { \omega _ { 0 } }$ . Define $\mathfrak { F } _ { \omega _ { 0 } } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } } { 2 } ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } ) \to \mathbb { R } ^ { D _ { Y } - d _ { Y } }$ as

$$
\mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) = \overline { { F } } _ { \omega _ { 0 } } ( V ^ { * } z + V ^ { * \perp } s + y _ { 0 } , x ) .
$$

Step 1. We will first show that the equation system, $\mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) = \mathbf { 0 }$ admits a solution for $s$ for any given $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$ .

at there exists a con $\overline { { L } } _ { 1 }$ $\mathfrak { F } _ { \omega _ { 0 } } \in \mathcal { H } _ { \overline { { L } } _ { 1 } , D _ { Y } - d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) \ \times$ $\mathbb { B } _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } } { 2 } ) , \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( \underline { { x } } _ { 0 } , \overline { { \tau } } _ { 2 } ) )$ $( x , y ) \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } )$ $J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) ^ { T } \succeq \overline { { \tau } } _ { 1 } I _ { D _ { Y } - d _ { Y } }$ and thus

$$
J _ { \overline { { F } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) V ^ { * \perp } ( V ^ { * \perp } ) ^ { T } J _ { \overline { { F } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) ^ { T } = J _ { \overline { { F } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) J _ { \overline { { F } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) ^ { T } \succeq \overline { { \tau } } _ { 1 } I _ { D _ { Y } - d _ { Y } } .
$$

When $\overline { { \tau } } , \overline { { \tau } } _ { 2 }$ are small enough, there exists a constant $L _ { 2 }$ so that for any $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) , s , s ^ { \prime } \in$ $\mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } } { 2 } )$ , and $x , x ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \overline { { \tau } } _ { 2 } \right)$ , the following conditions are satisfied:

$$
\begin{array} { l } { \displaystyle _ { z _ { 0 } ( \cdot , x ) } ( V ^ { * } z + V ^ { * \perp } s + y _ { 0 } ) J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( V ^ { * } z + V ^ { * \perp } s + y _ { 0 } ) ^ { T } \succeq \frac { \overline { \tau } _ { 1 } } { 2 } I _ { D _ { Y } - d _ { Y } } , } \\ { \| \mathfrak F _ { \omega _ { 0 } } ( z , 0 , x ) - \mathfrak F _ { \omega _ { 0 } } ( z ^ { \prime } , 0 , x ^ { \prime } ) \| \leq L _ { 2 } ( \| z - z ^ { \prime } \| + \| x - x ^ { \prime } \| ^ { \beta x \wedge 1 } ) , } \\ { \displaystyle _ { ( z , \cdot , x ) } ( s ) ^ { T } = J _ { \overline { F } _ { \omega _ { 0 } ( \cdot , x ) } } ( V ^ { * } z + V ^ { * \perp } s + y _ { 0 } ) V ^ { * \perp } ( V ^ { * \perp } ) ^ { T } J _ { \overline { F } _ { \omega _ { 0 } } ( \cdot , x ) } ( V ^ { * } z + V ^ { * \perp } s + y _ { 0 } ) ^ { T } \succeq \frac { \overline { \tau } _ { 1 } } { 2 } I _ { D _ { Y } - d _ { Y } } , } \end{array}
$$

$$
\| \mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) - \mathfrak { F } _ { \omega _ { 0 } } ( z , s ^ { \prime } , x ) - J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ^ { \prime } ) ( s - s ^ { \prime } ) \| \le L _ { 2 } \| s - s ^ { \prime } \| ^ { 2 } .
$$

For any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$ , we construct a solution $s ( z , x )$ to the equation system, $\mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) = \mathbf { 0 }$ in $s$ as follows: define $s _ { 0 } ( z , x ) = \mathbf { 0 }$ and for $k = 1 , 2 , \cdots$ , we recursively define

$$
s _ { k } ( z , x ) = s _ { k - 1 } ( z , x ) - ( J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s _ { k - 1 } ( z , x ) ) ) ^ { - 1 } \mathfrak { F } _ { \omega _ { 0 } } ( z , s _ { k - 1 } ( z , x ) , x ) .
$$

Then define a sequence √ $\begin{array} { r } { b _ { k } = \frac { \sqrt { \overline { { \tau } } _ { 1 } } } { \sqrt { 2 } L _ { 2 } } ( \frac { 4 L _ { 2 } ^ { 2 } } { \overline { { \tau } } _ { 1 } } \overline { { \tau } } _ { 2 } ) ^ { 2 ^ { k } } } \end{array}$ . We can set $\overline { { \tau } } _ { 2 }$ to be small enough so that $\textstyle \sum _ { k = 0 } ^ { \infty } b _ { k } <$ $\frac { \overline { { \tau } } } { 2 } \wedge \frac { \sqrt { \overline { { \tau } } _ { 1 } } } { 2 \sqrt { 2 } L _ { 2 } }$ , and we can verify that for any $k \in \mathbb N$ ,

$$
\begin{array} { r l } & { \| s _ { k + 1 } ( z , x ) - s _ { k } ( z , x ) \| \leq b _ { k } , } \\ & { \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s _ { k } ( z , x ) , x ) \| \leq \sqrt { \frac { \overline { { \tau } } _ { 1 } } { 2 } } b _ { k } . } \end{array}
$$

Hence $\begin{array} { r } { s ( z , x ) = \operatorname* { l i m } _ { k \to \infty } s _ { k } ( z , x ) } \end{array}$ exists, $\mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ) , x ) = \mathbf { 0 }$ and $\begin{array} { r } { \| s ( z , x ) \| < \overline { { \tau } } _ { 3 } = \frac { \overline { { \tau } } } { 2 } \wedge \frac { \sqrt { \overline { { \tau } } _ { 1 } } } { 2 \sqrt { 2 } L _ { 2 } } } \end{array}$ .

Step 2. Now we demonstrate that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \ \in \ \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$ , the equation $\mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) = 0$ has a unique solution over $s \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 3 } )$ .

Suppose there are two solution $s , s ^ { \prime }$ on $\mathbb { B } _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 3 } )$ , then

$$
\sqrt { \frac { \overline { { \tau _ { 1 } } } } { 2 } } \| s - s ^ { \prime } \| \leq \frac { \| s - s ^ { \prime } \| } { \| ( J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ^ { \prime } ) ) ^ { - 1 } \| _ { \mathrm { o p } } } \leq \| J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ^ { \prime } ) ( s - s ^ { \prime } ) \| \leq L _ { 2 } \| s - s ^ { \prime } \| ^ { 2 } .
$$

So we have

$$
\| s - s ^ { \prime } \| \geq \frac { \sqrt { \overline { { \tau } } _ { 1 } } } { \sqrt { 2 } L _ { 2 } } ,
$$

which causes contradiction. Then we define a function $\widetilde { G } _ { \omega _ { 0 } } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) \times \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) \to \mathbb { R } ^ { D _ { Y } }$ as $\widetilde { G } _ { \omega _ { 0 } } ( z , x ) = V ^ { * } z + V ^ { * \bot } s ( z , x ) + y _ { 0 }$ , where $s ( z , x )$ is defined as the unique solution of $\mathfrak { F } _ { \omega _ { 0 } } ( z , s , x ) = 0$ over $s \in B _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 3 } )$ , and define $\widetilde Q _ { \omega _ { 0 } } ( y , x ) = V ^ { * T } ( y - y _ { 0 } )$ .

Step 3. We will show that the pair $( \widetilde { G } _ { \omega _ { 0 } } , \widetilde { Q } _ { \omega _ { 0 } } )$ satisfies the conditions in Statement (2) of Lemma 3.

Notice that for any $\begin{array} { r } { x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) } \end{array}$ and $\boldsymbol { y } \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( \boldsymbol { y } _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } \wedge \overline { { \tau } } _ { 3 } )$ , we have $\begin{array} { r } { \| V ^ { * T } ( y - y _ { 0 } ) \| < \frac { \overline { { \tau } } _ { 2 } } { 2 } } \end{array}$ and $F _ { \omega _ { 0 } } ( y , x ) = \mathfrak { F } _ { \omega _ { 0 } } ( V ^ { * T } ( y - y _ { 0 } ) , ( V ^ { * \perp } ) ^ { T } ( y - y _ { 0 } ) , x ) = \mathbf { 0 }$ . Therefore, for any $\begin{array} { r } { x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) } \end{array}$ , it holds that

$$
\mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } \wedge \overline { { \tau } } _ { 3 } ) \subset \widetilde { G } _ { \omega _ { 0 } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) , x ) .
$$

Furthermore, for any $\begin{array} { r } { x \in \mathbb { B } _ { \mathcal { M } _ { x } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) } \end{array}$ and $\begin{array} { r } { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) } \end{array}$ , it holds that

and

$$
\widetilde Q _ { \omega _ { 0 } } ( \widetilde G _ { \omega _ { 0 } } ( z , x ) , x ) = V ^ { * T } V ^ { * } z = z .
$$

Now it only remains to show the smoothness of $\widetilde { G } _ { \omega _ { 0 } }$ . For $a > 1$ , consider the smooth transition function

$$
\rho _ { a } ( t ) = \left\{ \begin{array} { c c } { 0 } & { | t | \geq a } \\ { 1 } & { | t | \leq 1 } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) - 2 t } { ( t - 1 ) ( t - a ) } ) } } & { 1 < t < a } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) + 2 t } { ( t + 1 ) ( a + t ) } ) } } & { - a < t < - 1 . } \end{array} \right.
$$

We define $\overline { { G } } _ { \omega _ { 0 } } : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } }  \mathbb { R } ^ { D _ { Y } }$ as

$$
\overset { \triangledown } { \widetilde { \tau } _ { \omega _ { 0 } } } ( z , x ) = \left\{ \begin{array} { l l } { ( V ^ { * } z + V ^ { * \bot } s ( z , x ) + y _ { 0 } ) \rho _ { \frac { 9 } { 4 } } ( \frac { 4 \| z \| ^ { 2 } } { \overline { { \tau } } _ { 2 } ^ { 2 } } ) \rho _ { \frac { 9 } { 4 } } ( \frac { 4 \| x \| ^ { 2 } } { \overline { { \tau } } _ { 2 } ^ { 2 } } ) , } & { z \in B _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { 3 \overline { { \tau } } _ { 2 } } { 4 } ) , x \in \mathbb { R } _ { \mathbb { R } ^ { D _ { X } } } ( x , x ) } \\ { \mathbf { 0 } , } & { o . w , } \end{array} \right.
$$

Then it holds that $\widetilde { G } _ { \omega _ { 0 } } = \overline { { G } } _ { \omega _ { 0 } } | _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) }$ , and we will show that $\overline { { G } } _ { \omega _ { 0 } } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \left( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } \right)$ When $\beta _ { X } > 1$ , by implicit function theorem (see for example, Theorem A.3 of Eldering [2013]), for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$

$$
\begin{array} { r } { J _ { s ( \cdot , x ) } ( z ) = - ( J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ( z , x ) ) ) ^ { - 1 } J _ { \mathfrak { F } _ { \omega _ { 0 } } ( \cdot , s ( z , x ) , x ) } ( z ) , } \end{array}
$$

and

$$
J _ { s ( z , \cdot ) } ( x ) = - ( J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ( z , x ) ) ) ^ { - 1 } J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ) , \cdot ) } ( x ) .
$$

Given that $\begin{array} { r } { J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ( z , x ) ) J _ { \mathfrak { F } _ { \omega _ { 0 } } ( z , \cdot , x ) } ( s ( z , x ) ) ^ { T } \succeq \frac { \overline { \tau } _ { 1 } } { 2 } I _ { D _ { Y } - d _ { Y } } } \end{array}$ , we can verify the following: for any multi-indices $j _ { 1 } \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ and $j _ { 2 } \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ , if for all $l _ { 1 } \in \mathbb { N } _ { 0 } ^ { D _ { Y } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ satisfying $| l _ { 1 } | + | l _ { 2 } | \le | j _ { 1 } | + | j _ { 2 } |$ and $| l _ { 2 } | \ \leq \ | j _ { 2 } |$ ,the partial derivatives $\mathfrak { F } _ { \omega _ { 0 } } { } ^ { ( l _ { 1 } , l _ { 2 } ) } ( ( z , s ) , x )$ exist and are uniformly bounded in absolute value across $( z , s ) \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) \times B _ { \mathbb { R } ^ { D _ { Y } - d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 3 } )$ and $x \ \in \ \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$ , then the partial derivatives $s ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x )$ exist and are uniformly bounded in absolute value for $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$ .

, note thFor any $\mathfrak { F } _ { \omega _ { 0 } } \in \overline { { \mathcal { H } _ { L _ { 1 } , D _ { Y } - d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } } } \left( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) \times \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \frac { \tau } { 2 } } } ) , \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } ) \right)$ $\beta _ { Y } \geq \beta _ { X }$ $\beta _ { Y } \geq 2$ $( j _ { 1 } , j _ { 2 } ) \in \mathcal { T } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , D _ { X } }$ and $l _ { 1 } \in \mathbb { N } _ { 0 } ^ { D _ { Y } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ satisfying $| l _ { 1 } | + | l _ { 2 } | \le | j _ { 1 } | + | j _ { 2 } |$ $| l _ { 2 } | \le | j _ { 2 } |$

$$
\frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } = \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { Y } } + | l _ { 2 } | ( \frac { 1 } { \beta _ { X } } - \frac { 1 } { \beta _ { Y } } ) \leq \frac { | j _ { 1 } | + | j _ { 2 } | } { \beta _ { Y } } + | j _ { 2 } | ( \frac { 1 } { \beta _ { X } } - \frac { 1 } { \beta _ { Y } } ) = \frac { | j _ { 1 } | } { \beta _ { Y } } + \frac { | j _ { 2 } | } { \beta _ { X } } < 1 ,
$$

and thus fore, the $( l _ { 1 } , l _ { 2 } ) \in \mathcal { T } _ { \beta _ { Y } , \beta _ { X } } ^ { D _ { Y } , D _ { X } }$ at $\mathfrak { F } _ { \omega _ { 0 } } { } ^ { ( l _ { 1 } , l _ { 2 } ) } ( ( z , s ) , x )$ ound, the in absolute val-th component re-of $L _ { 3 }$ $k \in [ D _ { Y } - d _ { Y } ]$ $k$ $s _ { k } ( z , x )$ $s ( z , x ) = ( s _ { 1 } ( z , x ) , s _ { 2 } ( z , x ) , \cdot \cdot \cdot , s _ { D _ { Y } - d _ { Y } } ( z , x ) )$ satisfies

$$
\sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , D _ { X } } } \operatorname* { s u p } _ { ( z , x ) \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) \times \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } ) } | s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x ) | \leq L _ { 3 } .
$$

Moreover, for any (j1, j2) ∈ J dY ,DXβY ,βX with $\begin{array} { r } { \frac { | j _ { 1 } | } { \beta _ { Y } } + \frac { | j _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } \ge 1 } \end{array}$ and $l _ { 1 } \in \mathbb { N } _ { 0 } ^ { D _ { Y } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ satisfying $| l _ { 1 } | + | l _ { 2 } | \le | j _ { 1 } | + | j _ { 2 } |$ and $| l _ { 2 } | \le | j _ { 2 } |$ ,

1. If $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } \ge 1 } \end{array}$ , then for any $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \bigr ( ( z , s ( z , x ) ) , x \bigr ) - \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \bigr ( ( z ^ { \prime } , s ( z ^ { \prime } , x ) ) , x \bigr ) \| } \\ & { \lesssim \| z - z ^ { \prime } \| ^ { \beta _ { Y } - | l _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | l _ { 2 } | } + \| s ( z , x ) - s ( z ^ { \prime } , x ) \| ^ { \beta _ { Y } - | l _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | l _ { 2 } | } } \\ & { \lesssim \| z - z ^ { \prime } \| ^ { \beta _ { Y } - | l _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | l _ { 2 } | } } \\ & { \lesssim \| z - z ^ { \prime } \| ^ { \beta _ { Y } - | j _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | j _ { 2 } | } . } \end{array}
$$

2. If $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } < 1 } \end{array}$ , then for any $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z , s ( z , x ) ) , x \big ) - \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z ^ { \prime } , s ( z ^ { \prime } , x ) ) , x \big ) \| } \\ & { \lesssim \| z - z ^ { \prime } \| + \| s ( z , x ) - s ( z ^ { \prime } , x ) \| } \\ & { \lesssim \| z - z ^ { \prime } \| \lesssim \| z - z ^ { \prime } \| ^ { \beta _ { Y } - | j _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | j _ { 2 } | } . } \end{array}
$$

Therefore, there exists a constant $L _ { 3 }$ so that for any $k \in [ D _ { Y } - d _ { Y } ]$ , the $k$ -th component $s _ { k } ( z , x )$ of $s ( z , x )$ satisfies

$$
\sum _ { \{ j _ { 1 } , j _ { 2 } \} \in \mathcal { T } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , D _ { X } } } \operatorname* { s u p } _ { z , z _ { 0 } \in \mathbb { R } _ { \mathbb { R } } d _ { Y } } \operatorname* { s u p } _ { x \in \mathbb { R } _ { \mathbb { R } } D _ { X } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } ) \frac { \vert s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x ) - s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) \vert } { \Vert z - z _ { 0 } \Vert ^ { \beta _ { Y } - \vert j _ { 1 } \vert - \frac { \beta _ { Y } } { \beta _ { X } } \vert j _ { 2 } \vert } } \le L _ { 3 } .
$$

Furthermore, for any (j1, j2) ∈ J dY ,DXβY ,βX with $\begin{array} { r } { \frac { \left| j _ { 1 } \right| } { \beta _ { Y } } + \frac { \left| j _ { 2 } \right| } { \beta _ { X } } + \frac { 1 } { \beta _ { X } } \ge 1 } \end{array}$ and $l _ { 1 } \in \mathbb { N } _ { 0 } ^ { D _ { Y } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { D _ { X } }$ satisfying $| l _ { 1 } | + | l _ { 2 } | \le | j _ { 1 } | + | j _ { 2 } |$ and $| l _ { 2 } | \le | j _ { 2 } |$ ,

1. If $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } \ge 1 } \end{array}$ , then for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x , x ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \overline { { \tau } } _ { 2 } \right)$

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z , s ( z , x ) ) , x \big ) - \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z , s ( z , x ^ { \prime } ) ) , x ^ { \prime } \big ) \| } \\ & { \lesssim \| s ( z , x ) - s ( z , x ^ { \prime } ) \| ^ { \beta _ { Y } - | l _ { 1 } | - \frac { \beta _ { Y } } { \beta _ { X } } | l _ { 2 } | } + \| x - x ^ { \prime } \| ^ { \beta _ { X } - | l _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | l _ { 1 } | } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - | l _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | l _ { 1 } | } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - | j _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | j _ { 1 } | } . } \end{array}
$$

2. If $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } < 1 } \end{array}$ and $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { X } } \ge 1 } \end{array}$ , then for any $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in$ B

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z , s ( z , x ) ) , x \big ) - \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) \big ( ( z , s ( z , x ^ { \prime } ) ) , x ^ { \prime } \big ) \| } \\ & { \lesssim \| s ( z , x ) - s ( z , x ^ { \prime } ) \| + \| x - x ^ { \prime } \| ^ { \beta _ { X } - | l _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | l _ { 1 } | } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - | l _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | l _ { 1 } | } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - | j _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | j _ { 1 } | } . } \end{array}
$$

3. If $\begin{array} { r } { \frac { | l _ { 1 } | } { \beta _ { Y } } + \frac { | l _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { X } } < 1 } \end{array}$ , then for any $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } )$

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) ( ( z , s ( z , x ) ) , x ) - \mathfrak { F } _ { \omega _ { 0 } } ( l _ { 1 } , l _ { 2 } ) ( ( z , s ( z , x ^ { \prime } ) ) , x ^ { \prime } ) \| } \\ & { \lesssim \| s ( z , x ) - s ( z , x ^ { \prime } ) \| + \| x - x ^ { \prime } \| } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - | j _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | j _ { 1 } | } . } \end{array}
$$

Therefore, there exists a constant $L _ { 3 }$ so that for any $k \in [ D _ { Y } - d _ { Y } ]$ , the $k$ -th component $s _ { k } ( z , x )$ of $s ( z , x )$ satisfies

$$
\sum _ { \{ j _ { 1 } , j _ { 2 } \} \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , D _ { X } } } \operatorname* { s u p } _ { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } ) , x , x _ { 0 } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \overline { { \tau } } _ { 2 } ) } \frac { \big | s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x ) - s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x _ { 0 } ) \big | } { \| x - x _ { 0 } \| ^ { \beta _ { X } - | j _ { 2 } | - \frac { \beta _ { X } } { \beta _ { Y } } | j _ { 1 } | } } \leq L _ { 3 } .
$$

So by combining all pieces, we establish that for any $k \in [ D _ { Y } - d _ { Y } ]$

$$
\begin{array} { r l } & { \displaystyle \sum _ { \lbrace j _ { 1 } , j _ { 2 } \rbrace < j _ { 2 } ^ { \mathcal { A } _ { Y } , \mathcal { D } _ { X } } } ( z , x ) \in { \mathbb { B } _ { \mathbb { R } ^ { d } } } \gamma ( 0 , z ) \times { \mathbb { R } _ { \mathbb { R } ^ { D } X } } ( x _ { 0 } , { \tau } _ { 2 } ) | s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z , x ) | } \\ & { \displaystyle + \sum _ { \lbrace j _ { 1 } , j _ { 2 } \rbrace \in J _ { \mathbb { R } ^ { d } Y } , \mathcal { D } _ { X } } z \cdot z _ { 0 } \mathrm { e } ^ { \lambda _ { \mathbb { R } ^ { d } Y } } ( 0 , z ) \times { \mathbb { R } _ { \mathbb { R } ^ { D } X } } ( x _ { 0 } , { \tau } _ { 2 } ) | { \frac { S ( j _ { 1 } , j _ { 2 } ) } { \mu _ { 1 } } } ( z , x ) - s _ { k } ^ { ( j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | } \\ & { \displaystyle { ( \partial _ { 1 } , j _ { 2 } ) \in J _ { \mathbb { R } ^ { d } Y } } _ { s ^ { \mathcal { A } } } \gamma _ { 0 } x _ { 0 } \mathrm { e } ^ { \lambda _ { \mathbb { R } ^ { d } Y } } ( 0 , z ) \times { \mathbb { A } _ { \mathbb { R } ^ { D } X } } _ { \mathbb { X } } \gamma _ { 0 } x _ { 0 } \gamma _ { 2 } ) } \\ & { \displaystyle { \frac { | j _ { 1 } | + | j _ { 2 } | _ { \mathbb { R } ^ { d } Y } - \lambda _ { \mathbb { R } ^ { d } Y } } { \beta _ { Y } } } ( z , x ) } \\ &  +  \sum _ { \lbrace j _ { 1 } , j _ { 2 } \rbrace \in J _ { \mathbb { R } ^ { d } Y } , \mathcal { D } _ { X } }  \times { \mathbb { E } } \mathbb { I } _ { \mathbb { R } ^ { d } Y } ^ { \lambda } ( 0 , z ) \times  \end{array}
$$

Utilizing the fact that when $z \in B _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ $\mathrm { a n d } x \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \overline { \tau } _ { 2 } \right) , \overline { G } _ { \omega _ { 0 } } ( z , x ) = ( V ^ { * } z + V ^ { * \perp } s ( z , x ) +$ $y _ { 0 } ) \rho _ { \frac { 9 } { 4 } } ( \frac { 4 \| z \| ^ { 2 } } { \overline { { \tau } } ^ { 2 } } ) \rho _ { \frac { 9 } { 4 } } ( \frac { 4 \| x \| ^ { 2 } } { \overline { { \tau } } ^ { 2 } } )$ $\begin{array} { r } { ( z , x ) \notin B _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { 3 \overline { \tau } _ { 2 } } { 4 } ) \times B _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \frac { 3 \overline { \tau } _ { 2 } } { 4 } ) } \end{array}$ $\overline { { G } } _ { w _ { 0 } } ( z , x ) = 0$ , we can $\overline { { G } } _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 5 } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ $\begin{array} { r } { \widetilde { G } _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 5 } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \frac { \overline { { \tau } } _ { 2 } } { 2 } ) ) . } \end{array}$

Then we consider the case when $\beta _ { X } \ \leq \ 1$ , similar to the case for $\beta _ { X } ~ > ~ 1$ , using implicit function theorem, it is straightforward to show that for any $x \in \mathbb { R } ^ { D _ { X } }$ ${ { \cal D } _ { X } } , \overline { { { G } } } _ { \omega _ { 0 } } ( \cdot , x ) \in \mathcal { H } _ { L _ { 5 } , { \cal D } _ { Y } } ^ { \beta _ { Y } } ( \mathbb { R } ^ { \bar { d } _ { Y } } )$ . Next, we shall demonstrate that for any $l \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ with $| l | < \beta _ { Y }$ , and for any $z \in \mathbb { R } ^ { d _ { Y } }$ , $x , x ^ { \prime } \in \mathbb { R } ^ { D _ { X } }$ , it holds that

$$
\begin{array} { r } { \left\| \overline { G } ^ { ( l , \mathbf { 0 } ) } ( z , x ) - \overline { G } ^ { ( l , \mathbf { 0 } ) } ( z , x ^ { \prime } ) \right\| \leq L _ { 5 } \left\| x - x ^ { \prime } \right\| ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } . } \end{array}
$$

To verify this result, it suffices to prove that for any $l \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ with $| l | < \beta _ { Y }$ , and any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \overline { { \tau } } _ { 2 } )$ and $x , x ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \overline { { \tau } } _ { 2 } \right)$ ,

$$
\begin{array} { r } { \| s ^ { ( l , \mathbf { 0 } ) } ( z , x ) - s ^ { ( l , \mathbf { 0 } ) } ( z , x ^ { \prime } ) \| \leq C _ { 1 } \| x - x ^ { \prime } \| ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } . } \end{array}
$$

To establish this, note that

$$
\begin{array} { r l } & { \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ) - \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ) , x ) \| } \\ & { = \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ) \| } \\ & { \leq \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ^ { \prime } ) \| + \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ^ { \prime } ) - \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ) \| } \\ & { = \| \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ^ { \prime } ) - \mathfrak { F } _ { \omega _ { 0 } } ( z , s ( z , x ^ { \prime } ) , x ) \| } \\ & { \leq C \| x - x ^ { \prime } \| ^ { \beta _ { X } } , } \end{array}
$$

we can get $\| s ( z , x ) - s ( z , x ^ { \prime } ) \| \leq C _ { 1 } \| x - x ^ { \prime } \| ^ { \beta _ { X } }$ . So for any $l \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ with $| l | < \beta _ { Y } - 1$ , it holds that

$$
\begin{array} { r l } & { \left. s ^ { ( l , 0 ) } ( z , x ) - s ^ { ( l , 0 ) } ( z , x ^ { \prime } ) \right. } \\ & { \leq \left. x - x ^ { \prime } \right. ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } + \left. s ( z , x ) - s ( z , x ^ { \prime } ) \right. } \\ & { \lesssim \left. x - x ^ { \prime } \right. ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } . } \end{array}
$$

For any $l \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ with $| l | = \lfloor \beta _ { Y } \rfloor$ , it holds that

$$
\begin{array} { r l } & { \| s ^ { ( l , \mathbf { 0 } ) } ( z , x ) - s ^ { ( l , \mathbf { 0 } ) } ( z , x ^ { \prime } ) \| } \\ & { \leq \| x - x ^ { \prime } \| ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } + \| s ( z , x ) - s ( z , x ^ { \prime } ) \| ^ { \beta _ { Y } - | l | } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } + \| x - x ^ { \prime } \| ^ { \beta _ { Y } ( \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | ) } } \\ & { \lesssim \| x - x ^ { \prime } \| ^ { \beta _ { X } - \frac { \beta _ { X } } { \beta _ { Y } } | l | } . } \end{array}
$$

We can then get the desired result by combining all pieces.

# E.5.2 $( 2 ) \Rightarrow ( 1 )$

We first show that the conditions in (2) can imply that $\mathcal { M } _ { Y \mid x }$ has a reach that is uniformly lower bounded away from zero. Suppose that there exists $x \in \mathcal { M } _ { X }$ , so that the reach of $\mathcal { M } _ { Y \mid x }$ is smaller than $\tau$ . Then by definition, there exists $y \in \mathbb { R } ^ { D _ { Y } }$ and $y _ { 1 } , y _ { 2 } \in \mathcal { M } _ { Y | x }$ , so that $y _ { 1 } \neq y _ { 2 }$ , $\left\| y - y _ { 1 } \right\| = \left\| y - y _ { 2 } \right\| < \tau$ , $y - y _ { 1 } \perp T _ { y _ { 1 } } \mathcal { M } _ { Y | x }$ , and $y - y _ { 2 } \perp T _ { y _ { 2 } } \mathcal { M } _ { Y | x }$ . Let $\omega = ( x , y _ { 1 } )$ and consider the local parametrization $( \widetilde { Q } _ { \omega } , \widetilde { G } _ { \omega } )$ . It holds that $\widetilde { G } _ { \omega } ( \mathbf { 0 } , x ) = y _ { 1 }$ . Moreover, since $\left\| y _ { 2 } - y _ { 1 } \right\| \leq \left\| y - y _ { 1 } \right\| + \left\| y - y _ { 2 } \right\| < 2 \tau$ , when $\begin{array} { r } { \tau \leq \frac { \widetilde \tau } { 2 } } \end{array}$ , it holds for $z _ { 2 } = \widetilde { Q } _ { \omega } ( y _ { 2 } , x )$ that

$$
0 < \| z _ { 2 } \| = \| \widetilde Q _ { \omega } ( y _ { 2 } , x ) - \widetilde Q _ { \omega } ( y _ { 1 } , x ) \| \le \widetilde L \| y _ { 2 } - y _ { 1 } \| < 2 \widetilde L \tau ,
$$

and $\widetilde { G } _ { \omega } ( z _ { 2 } , x ) = y _ { 2 }$ . Furthermore, since $y - y _ { 1 } \perp T _ { y _ { 1 } } \mathcal { M } _ { Y | x }$ , let $V _ { \omega } ^ { \perp }$ be a $D _ { Y }$ by $( D _ { Y } - d _ { Y } )$ matrix whose columns form an orthornormal basis for the normal space of $T _ { y _ { 1 } } { \mathcal { M } } _ { Y | x }$ , there exists a vector $s \in \mathbb { R } ^ { D _ { Y } - d _ { Y } }$ so that $y = y _ { 1 } + V _ { \omega } ^ { \perp } s$ and $\| s \| < \tau$ . Then by $y - y _ { 2 } \perp T _ { y _ { 2 } } M _ { Y | x }$ , it holds that

$$
J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } ( y _ { 1 } + V _ { \omega } ^ { \perp } s - y _ { 2 } ) = J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } ( y - y _ { 2 } ) = \mathbf { 0 } ,
$$

which implies that

$$
\| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } ( y _ { 1 } - y _ { 2 } ) \| = \| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } V _ { \omega } ^ { \perp } s \| .
$$

Then since $\widetilde { G } _ { \omega } ( \cdot , x )$ is $\beta _ { Y }$ -Holder-smooth with ¨ $\beta _ { Y } \ge 2$ , we have

$$
\begin{array} { r l } & { \| y _ { 1 } - y _ { 2 } + J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) z _ { 2 } \| } \\ & { = \| \widetilde { G } _ { \omega } ( \mathbf { 0 } , x ) - \widetilde { G } _ { \omega } ( z _ { 2 } , x ) - J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( \mathbf { 0 } - z _ { 2 } ) \| } \\ & { \leq \widetilde { L } \sqrt { D _ { Y } d _ { Y } } \| z _ { 2 } \| ^ { 2 } } \\ & { < 2 \widetilde { L } ^ { 2 } \sqrt { D _ { Y } d _ { Y } } \tau \| z _ { 2 } \| , } \end{array}
$$

and therefore,

$$
\begin{array} { r l } & { \| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } ( y _ { 1 } - y _ { 2 } ) \| } \\ & { > \| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) z _ { 2 } \| - 2 \widetilde { L } ^ { 3 } D _ { Y } d _ { Y } \tau \| z _ { 2 } \| } \\ & { > \sqrt { \lambda _ { \operatorname* { m i n } } ( J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ) } \| z _ { 2 } \| - 2 \widetilde { L } ^ { 3 } D _ { Y } d _ { Y } \tau \| z _ { 2 } \| } \\ & { \geq \left( \frac { 1 } { \widetilde { L } } - 2 \widetilde { L } ^ { 3 } D _ { Y } d _ { Y } \tau \right) \| z _ { 2 } \| , } \end{array}
$$

where the last inequality uses the $\widetilde { L }$ -Lipschitzness of $\widetilde { Q } _ { \omega }$ . Moreover, since $\| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( \mathbf { 0 } ) ^ { T } V _ { \omega } ^ { \perp } s \| = 0$ , we can obtain

$$
\begin{array} { r l } & { \| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) ^ { T } V _ { \omega } ^ { \perp } s \| = \| ( J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) - J _ { G _ { \omega } ( \cdot , x ) } ( \mathbf { 0 } ) ) ^ { T } V _ { \omega } ^ { \perp } s \| } \\ & { \leq \| J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( z _ { 2 } ) - J _ { \widetilde { G } _ { \omega } ( \cdot , x ) } ( \mathbf { 0 } ) \| _ { \mathrm { F } } \| s \| } \\ & { \leq \widetilde { L } d _ { Y } \sqrt { D _ { Y } } \| z _ { 2 } \| \| s \| } \\ & { < \widetilde { L } d _ { Y } \sqrt { D _ { Y } } \tau \| z _ { 2 } \| . } \end{array}
$$

Therefore, we have

$$
\begin{array} { l } { { \widetilde { L } d _ { Y } \sqrt { D _ { Y } } \tau \| z _ { 2 } \| > \left( \displaystyle \frac { 1 } { \widetilde { L } } - 2 \widetilde { L } ^ { 3 } D _ { Y } d _ { Y } \tau \right) \| z _ { 2 } \| } } \\ { { \Rightarrow \tau > \Big ( \widetilde { L } ^ { 2 } d _ { Y } \sqrt { D _ { Y } } ( 1 + 2 \widetilde { L } ^ { 2 } \sqrt { D _ { Y } } ) \Big ) ^ { - 1 } . } } \end{array}
$$

So by selecting $\begin{array} { r } { \tau = { \frac { \widetilde \tau } { 2 } } \wedge \big ( \widetilde { L } ^ { 2 } d _ { Y } \sqrt { D _ { Y } } ( 1 + 2 \widetilde { L } ^ { 2 } \sqrt { D _ { Y } } ) \big ) ^ { - 1 } } \end{array}$ , it holds for any $x \in \mathcal { M } _ { X }$ that the reach of $\mathcal { M } _ { Y \mid x }$ is lower bounded by $\tau$ .

To complete our proof, it remains to show the smoothness of the inverse of the projection map onto the tangent space of the manifold. Notice that any tangent vector in $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } y _ { 0 } }$ can be uniquely represented by a $d _ { Y }$ -dimensional vector using an orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } y _ { 0 } }$ . Therefore, by selecting $V _ { \omega _ { 0 } }$ as an orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x _ { 0 } } y _ { 0 } }$ in Lemma 4, we can obtain the desired result.

# E.5.3 $( 1 ) \Rightarrow ( 3 )$

Take an arbitrary $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ . Let $V _ { \omega _ { 0 } } ~ \in ~ \mathbb { R } ^ { D _ { Y } \times d _ { Y } }$ be a matrix whose column forms an orthonormal basis of $T _ { M _ { Y \mid x _ { 0 } } } y _ { 0 }$ and $V _ { \omega _ { 0 } } ^ { \perp } \in \mathbb { R } ^ { D _ { Y } \times ( \bar { D } _ { Y } - \bar { d } _ { Y } ) }$ be the orthogonal complement of $V _ { \omega _ { 0 } }$ . Given that the submanifold $\mathcal { M } _ { Y \mid x _ { 0 } }$ has reach that is lower bounded by $\tau$ , by Lemma 2 of Aamari and Levrard [2019], it holds with some constants τ2, τ3 > 0 so that BMY |x(y0, τ2) ⊂ Φω0(BTMY |x y $\mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { 0 } , \tau _ { 3 } )$ , where $\Phi _ { \omega _ { 0 } }$ is defined as per Definition 4 in the main text. Now define

$$
F _ { \omega _ { 0 } } ( y , x ) = ( V _ { \omega _ { 0 } } ^ { \perp } ) ^ { T } ( y - \Phi _ { \omega _ { 0 } } ( V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 0 } ) , x ) ) .
$$

Then $J _ { F _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) J _ { F _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( y _ { 0 } ) ^ { T } = ( V _ { \omega _ { 0 } } ^ { \perp } ) ^ { T } ( I _ { D _ { Y } } - V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ) ( I _ { D _ { Y } } - V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ) V _ { \omega _ { 0 } } ^ { \perp } = I _ { D _ { Y } - d _ { Y } } .$ So there ω0 0 exist constants $0 < \overline { { \tau } } < \tau _ { 1 } \land \tau _ { 2 }$ and $L _ { 1 }$ Y so that $F _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 1 } , D _ { Y } - d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) )$ and for any $\begin{array} { r } { ( y , x ) \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \overline { { \tau } } ) , J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) J _ { F _ { \omega _ { 0 } } ( \cdot , x ) } ( y ) ^ { T } \succeq \frac { 1 } { 2 } I _ { D _ { Y } - d _ { Y } } . } \end{array}$ hen we show that for any $x \in \mathbb { B } _ { M _ { X } } ( x _ { 0 } , \overline { { \tau } } )$ $x _ { 0 } , \overline { { \tau } } ) , \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \overline { { \tau } } ) = \{ y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } ) : F _ { \omega _ { 0 } } ( y , x ) = 0 \}$ . Firstly, if $y \in \mathbb { B } _ { M _ { Y | x } } ( y _ { 0 } , \overline { { \tau } } )$ , then $F _ { \omega _ { 0 } } ( y , x ) \ \stackrel { \cdot } { = } \ 0$ , which implies that $\mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \overline { { \tau } } ) \subset \{ y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } ) \ :$ $F _ { \omega _ { 0 } } ( y , x ) = 0 \}$ . Furthermore, if $y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } )$ and $F _ { \omega _ { 0 } } ( y , x ) = \mathbf { 0 }$ . Then define $y _ { 1 } = \Phi _ { \omega _ { 0 } } ( V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ( y -$ $y _ { 0 } ) , x ) \subset \mathcal { M } _ { Y | x }$ . It holds that

$$
\begin{array} { r } { \| V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 0 } ) \| \le \| y - y _ { 0 } \| \le \overline { { \tau } } < \tau _ { 1 } , } \end{array}
$$

$$
\begin{array} { r } { \mathbf { \Phi } _ { \omega _ { 0 } } ^ { \prime } V _ { \omega _ { 0 } } ^ { T } ( y _ { 1 } - y _ { 0 } ) = \operatorname* { P r o j } _ { T _ { y _ { 0 } } , M _ { Y | x _ { 0 } } } ( y _ { 1 } - y _ { 0 } ) = V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 0 } ) \Rightarrow V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 1 } ) = \mathbf { 0 } _ { D _ { Y } } \Rightarrow V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 0 } ) = 0 } \end{array}
$$

Then combined with the fact that $F _ { \omega _ { 0 } } ( y , x ) = ( V _ { \omega _ { 0 } } ^ { \perp } ) ^ { T } ( y - y _ { 1 } ) = \mathbf { 0 } _ { D _ { Y } - d _ { Y } }$ , we have $y = y _ { 1 } \in \mathcal { M } _ { Y | x }$ Therefore,

$$
\mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \overline { { \tau } } _ { 2 } ) = \{ y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( y _ { 0 } , \overline { { \tau } } _ { 2 } ) : F _ { \omega _ { 0 } } ( y , x ) = \mathbf { 0 } \} ,
$$

this completes the proof.

# E.6 Proof of Lemma 4

$\tau _ { 2 } \in ( 0 , \frac { \pi } { 2 } )$ y small positive c be a smooth ext ke an arbi. For any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ $\overline { { G } } _ { \omega _ { 0 } } ~ \in ~ \overline { { \mathcal { H } } } _ { \widetilde { L } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { d _ { X } } )$ $\widetilde { G } _ { \omega _ { 0 } }$ $s \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 2 } )$ $x \in$ $\mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \tau _ { 2 } \right)$ , consider the following equation for $z \in \mathbb { R } ^ { d _ { Y } }$ :

$$
V _ { \omega _ { 0 } } ^ { T } ( \overline { { G } } _ { \omega _ { 0 } } ( z , x ) - y _ { 0 } ) = s .
$$

Since $\widetilde { Q } _ { \omega _ { 0 } } ( \cdot , x )$ is $\widetilde { L }$ -Lipschitz, we have

$$
J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( \mathbf { 0 } ) ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( \mathbf { 0 } ) \succeq \frac { 1 } { \widetilde { L } ^ { 2 } } I _ { d _ { Y } } .
$$

Then let $\widetilde { V } _ { \omega _ { 0 } } \in \mathbb { R } ^ { D _ { Y } \times d _ { Y } }$ be an orthonormal matrix with $\widetilde { V } _ { \omega _ { 0 } } \widetilde { V } _ { \omega _ { 0 } } ^ { T } = P _ { \omega _ { 0 } }$ , since

$$
\begin{array} { r } { V _ { \omega _ { 0 } } ^ { T } P _ { \omega _ { 0 } } V _ { \omega _ { 0 } } = ( V _ { \omega _ { 0 } } ^ { T } \widetilde { V } _ { \omega _ { 0 } } ) ( V _ { \omega _ { 0 } } ^ { T } \widetilde { V } _ { \omega _ { 0 } } ) ^ { T } \succeq \tau _ { 0 } I _ { d _ { Y } } , } \end{array}
$$

we have

and

$$
\begin{array} { r l } & { \widetilde { V } _ { \omega _ { 0 } } ^ { T } V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } \widetilde { V } _ { \omega _ { 0 } } = ( V _ { \omega _ { 0 } } ^ { T } \widetilde { V } _ { \omega _ { 0 } } ) ^ { T } ( V _ { \omega _ { 0 } } ^ { T } \widetilde { V } _ { \omega _ { 0 } } ) \succeq \tau _ { 0 } I _ { d _ { Y } } , } \\ & { } \\ & { J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( \mathbf { 0 } ) ^ { T } V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x _ { 0 } ) } ( \mathbf { 0 } ) \succeq \frac { \tau _ { 0 } } { \widetilde { L } ^ { 2 } } I _ { d _ { Y } } . } \end{array}
$$

Then using the fact that $\overline { { G } } _ { \omega _ { 0 } } \in \mathcal { \overline { { H } } } _ { \widetilde { L } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { d _ { X } } )$ with $\beta _ { Y } \geq 2$ eand $\beta _ { X } > 0$ , when $\widetilde { \tau } _ { 1 } , \tau _ { 2 }$ are small $x \in \mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \tau _ { 2 } \right)$ and $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } )$ ,

$$
J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } V _ { \omega _ { 0 } } V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) \succeq \frac { \tau _ { 0 } } { 4 \widetilde { L } ^ { 2 } } I _ { d _ { Y } } .
$$

So there exists a constant $L _ { 1 }$ so that for any $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \tau _ { 2 } )$ and $z , z ^ { \prime } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \widetilde { \tau } _ { 1 } )$ ,

$$
\| ( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } ( \cdot , x ) } } ( z ) ) ^ { - 1 } \| _ { \mathrm { o p } } \leq L _ { 1 } ,
$$

and

$$
\| V _ { \omega _ { 0 } } ^ { T } \overline { { G } } _ { \omega _ { 0 } } ( z , x ) - V _ { \omega _ { 0 } } ^ { T } \overline { { G } } _ { \omega _ { 0 } } ( z ^ { \prime } , x ) - V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ^ { \prime } ) ( z - z ^ { \prime } ) \| \leq L _ { 1 } \| z - z ^ { \prime } \| ^ { 2 } .
$$

Then, by following a similar analysis to that outlined in the proof for $( 3 ) \ \Rightarrow \ ( 1 )$ of Lemma 3 in Section E.5.1, we can show that for sufficiently small $\tau _ { 2 }$ , there exists a function $\zeta : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 2 } ) \times$ $\begin{array} { r } { \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \tau _ { 2 } ) \to \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \tau _ { 1 } } { 2 } \wedge \frac { 1 } { 2 L _ { 1 } ^ { 2 } } ) } \end{array}$ , so that $\zeta ( s , x )$ is the unique solution of $V _ { \omega _ { 0 } } ^ { T } ( \overline { { G } } _ { \omega _ { 0 } } ( z , x ) - y _ { 0 } ) = s$ over $\begin{array} { r } { z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \widetilde { \tau } _ { 1 } } { 2 } \wedge \frac { 1 } { 2 L _ { 1 } ^ { 2 } } ) } \end{array}$ . Then we can define $G _ { \omega _ { 0 } } : \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 2 } ) \times \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau _ { 2 } ) \to \mathbb { R } ^ { D _ { Y } }$ as $G _ { \omega _ { 0 } } ( z , x ) = \overline { { G } } _ { \omega _ { 0 } } ( \zeta ( z , x ) , x )$ . Denote $Q _ { \omega _ { 0 } } ( y ) = V _ { \omega _ { 0 } } ^ { T } ( y - y _ { 0 } )$ , for any $\begin{array} { r } { x \in B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \frac { \tau _ { 2 } } { 2 } \land \frac { \widetilde \tau _ { 1 } } { 4 \widetilde L } \land \frac { 1 } { 4 \widetilde L L _ { 1 } ^ { 2 } } ) } \end{array}$ $\begin{array} { r } { y \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \frac { \tau _ { 2 } } { 2 } \land \frac { \widetilde { \tau } _ { 1 } } { 4 \widetilde { L } } \land \frac { 1 } { 4 \widetilde { L } L _ { 1 } ^ { 2 } } ) } \end{array}$ ∧ 14LL 2 ) and z ∈ BRdY (0, τ22 ), we have

$$
\begin{array} { l } { \displaystyle | | \widetilde { Q } _ { \omega _ { 0 } } ( y , x ) | | = | | \widetilde { Q } _ { \omega _ { 0 } } ( y , x ) - \widetilde { Q } _ { \omega _ { 0 } } ( \widetilde { G } _ { \omega _ { 0 } } ( \mathbf { 0 } , x ) , x ) | | } \\ { \displaystyle \le L \| y - \widetilde { G } _ { \omega _ { 0 } } ( \mathbf { 0 } , x ) \| } \\ { \displaystyle \le L \| y - y _ { 0 } \| + L \| \widetilde { G } _ { \omega _ { 0 } } ( \mathbf { 0 } , x _ { 0 } ) - \widetilde { G } _ { \omega _ { 0 } } ( \mathbf { 0 } , x ) \| } \\ { \displaystyle < \frac { \widetilde { T } _ { 1 } } { 2 } \wedge \frac { 1 } { 2 L _ { 1 } ^ { 2 } } , } \end{array}
$$

$$
G _ { \omega _ { 0 } } ( Q _ { \omega _ { 0 } } ( y ) , x ) = G _ { \omega _ { 0 } } ( Q _ { \omega _ { 0 } } ( \widetilde { G } _ { \omega _ { 0 } } ( \widetilde { Q } _ { \omega _ { 0 } } ( y , x ) , x ) ) , x ) = G _ { \omega _ { 0 } } ( \widetilde { Q } _ { \omega _ { 0 } } ( y , x ) , x ) = y .
$$

and

$$
Q _ { \omega _ { 0 } } ( G _ { \omega _ { 0 } } ( z , x ) ) = z .
$$

Therefore, for any $\begin{array} { r } { x \in B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \frac { \tau _ { 2 } } { 2 } \land \frac { \widetilde \tau _ { 1 } } { 4 \widetilde L } \land \frac { 1 } { 4 \widetilde { L } L _ { 1 } ^ { 2 } } ) } \end{array}$ ∧ 14LLe 21 ), let UY |x = Gω0 (BRdY (0, τ22 ), x), it holds that (1) $Q _ { \omega _ { 0 } }$ is a diffeomorphism that maps $U _ { Y \mid x }$ to $\begin{array} { r } { \dot { \mathbb { B } } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \tau _ { 2 } } { 2 } ) } \end{array}$ with inverse $G _ { \omega _ { 0 } } ( \cdot , x ) | _ { \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \frac { \tau _ { 2 } } { 2 } ) } .$ . (2) $\begin{array} { r } { \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { 0 } , \frac { \tau _ { 2 } } 2 \wedge \frac { \widetilde \tau _ { 1 } } { 4 L } \wedge \frac 1 { 4 L L _ { 1 } ^ { 2 } } ) \subset U _ { Y | x } \subset \mathcal { M } _ { Y | x } . } \end{array}$

So it only remains to show the smoothness of $G _ { \omega _ { 0 } }$ . By implicit function theorem, for any $z \in B _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 2 } ) , x \in$ $\mathbb { B } _ { \mathbb { R } ^ { D } X } \left( x _ { 0 } , \tau _ { 2 } \right)$ ,

$$
\begin{array} { r } { J _ { \zeta ( \cdot , x ) } ( z ) = \left( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( \zeta ( z , x ) ) \right) ^ { - 1 } . } \\ { J _ { G _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) = J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( \zeta ( z , x ) ) \left( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( \zeta ( z , x ) ) \right) ^ { - 1 } . } \end{array}
$$

And when $\beta _ { X } > 1$ ,

$$
J _ { \zeta ( z , \cdot ) } ( x ) = - \left( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } ( \cdot , x ) } } ( \zeta ( z , x ) ) \right) ^ { - 1 } ( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \zeta ( z , x ) , \cdot ) } ( x ) ) ,
$$

and

$$
J _ { G _ { \omega _ { 0 } } ( z , \cdot ) } ( x ) = J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( \zeta ( z , x ) ) J _ { \zeta ( z , \cdot ) } ( x ) + J _ { \overline { { G } } _ { \omega _ { 0 } } ( \zeta ( z , x ) , \cdot ) } ( x ) .
$$

analy with d in the proof for , and $( 3 ) \Rightarrow ( 1 )$ of Lemma 3, using the fact that $\overline { { G } } _ { \omega _ { 0 } } \in$ $\mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { d _ { X } } )$ $\beta _ { Y } \geq \beta _ { X }$

$$
\| ( V _ { \omega _ { 0 } } ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( \zeta ( z , x ) ) ) ^ { - 1 } \| _ { \mathrm { o p } } \leq L _ { 1 } ,
$$

we can conclude that there exists a constant $L _ { 2 }$ so that $G _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 2 } , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } \bigl ( \mathbf { 0 } , \tau _ { 2 } \bigr ) , \mathbb { B } _ { \mathcal { M } _ { X } } \bigl ( x _ { 0 } , \tau _ { 2 } \bigr ) \bigr ) .$

# E.7 Proof of Lemma 5

We will begin by proving the first statement. For $a > 1$ , consider the smooth transition function $\rho _ { a } ( \cdot )$ defined as

$$
\rho _ { a } ( t ) = \left\{ \begin{array} { c c } { 0 } & { | t | \geq a } \\ { 1 } & { | t | \leq 1 } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) - 2 t } { ( t - 1 ) ( t - a ) } ) } } & { 1 < t < a } \\ { \frac { 1 } { 1 + \exp ( \frac { ( a + 1 ) + 2 t } { ( t + 1 ) ( a + t ) } ) } } & { - a < t < - 1 . } \end{array} \right.
$$

Let $\{ \omega _ { k } = ( x _ { k } ^ { * } , y _ { k } ^ { * } ) \} _ { k = 1 } ^ { K ^ { * } } \subset \mathcal { M }$ be a $\scriptstyle { \frac { \tau } { \sqrt { 2 } } }$ -covering set of $\mathcal { M }$ . For any $k \in [ K ^ { * } ]$ , let $V _ { k }$ be a matrix whose column forms an orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x _ { k } ^ { * } } } y _ { k } ^ { * }$ , and denote $G _ { [ k ] } ( z , x ) = \Phi _ { \omega _ { k } } ( V _ { k } z , x ) , Q _ { [ k ] } ( y ) =$ $V _ { k } ^ { T } ( y - y _ { k } ^ { \ast } )$ , $\nu _ { k } ( z | x ) = \nu _ { \omega _ { k } } ( V _ { k } z | x )$ and $U _ { Y | x } ^ { \omega _ { k } } = U _ { \omega _ { k } } \cap \mathcal { M } _ { Y | x }$ . Then define the function

$$
( y , x ) = \sum _ { k = 1 } ^ { K ^ { * } } \frac { \nu _ { k } ( Q _ { [ k ] } ( y ) | x ) \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) \left( \operatorname* { d e t } \Bigl ( J _ { G _ { [ k ] } ( \cdot , x ) } \bigl ( Q _ { [ k ] } ( y ) \bigr ) ^ { T } J _ { G _ { [ k ] } ( \cdot , x ) } \bigl ( Q _ { [ k ] } ( y ) \bigr ) \Bigr ) \right) ^ { - \frac { 1 } { 2 } } } { \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } \bigl ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } \bigr ) } .
$$

We will show that $u ( \cdot , x )$ is the density function of $\mu _ { Y \mid x } ^ { * }$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ In support of this objective, we present the following claim that will be proved later.

Claim 2. For any $( x , y ) \in { \mathcal { M } }$ and $k \in [ K ^ { * } ] , i f \left| \omega _ { k } - ( x , y ) \right| < \tau$ , then

$$
\begin{array} { r } { u ( y , x ) = \nu _ { k } ( Q _ { [ k ] } ( y ) | x ) \left( \mathrm { d e t } \Big ( J _ { G _ { [ k ] } ( \cdot , x ) } \big ( Q _ { [ k ] } ( y ) \big ) ^ { T } J _ { G _ { [ k ] } ( \cdot , x ) } \big ( Q _ { [ k ] } ( y ) \big ) \Big ) \right) ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

Given the claim above, it follows that for any $x \in \mathcal { M } _ { x }$ and measurable function $f _ { 1 } : \mathcal { M } _ { Y | x }  \mathbb { R }$ ,

$$
\begin{array} { r l } &  \mathbb { E } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { S } } _ { \hat { S } } _ { \mathcal { \hat { S } } _ { \hat { S } } _ { \hat { S } } } } } } } } } } } } } } } } } } } } } } } \\ &  = \frac { K ^ { \hat { \mathcal { \mathcal { { S } } } } } } { \sum _ { k = 1 } } ^ { K } \mathbb { E } _  \hat { \mathcal { S } } _  \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \hat { \mathcal { S } } _ { \hat { S } } _ { \hat { S } } } } } } } } } } } [ \frac  f _ { k } ( \mathcal \end{array}
$$

where $( i )$ uses the fact that $\mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y _ { k } ^ { * } , \tau ) \subset U _ { Y \mid x } ^ { \omega _ { k } }$ . Therefore, $u ( \cdot , x )$ is the density function of $\mu _ { Y | x } ^ { * }$ with respect to the volume measure of $\mathcal { M } _ { Y \mid x }$ .

Now we will show the smoothness of $u$ . Let $\overline { { G } } _ { [ k ] } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \left( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } \right)$ be a smooth extension of $G _ { [ k ] }$ and and $\mathcal { V } _ { k } \in \mathcal { H } _ { L , D _ { Y } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $\nu _ { k }$ . Then notice that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )$

$$
J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( z ) ^ { T } J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( z ) \succeq \frac { 1 } { L ^ { 2 } } I _ { d _ { Y } } .
$$

When $\tau$ is small enough, it holds that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 2 \tau )$ , and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , 2 \tau )$ ,

$$
J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( z ) ^ { T } J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( z ) \succeq \frac { 1 } { 2 L ^ { 2 } } I _ { d _ { Y } } .
$$

Then we define a function $s _ { k } : \mathbb { R } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } } \to \mathbb { R }$ as

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \bar { \nu } _ { k } ( Q _ { [ k ] } ( y ) | x ) \left( \operatorname* { d e t } \left( J _ { \overline { G } _ { [ k ] } ( \cdot , x ) } \left( Q _ { [ k ] } ( y ) \right) ^ { T } J _ { \overline { G } _ { [ k ] } ( \cdot , x ) } \left( Q _ { [ k ] } ( y ) \right) \right) \right) ^ { - \frac { 1 } { 2 } } \rho _ { \frac { 9 } { 4 } } ( \frac { \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { { \tau ^ { 2 } } } ) , } & { \quad ( x , y ) \in [ k , \frac { 1 } { 2 } ] } \\ { 0 , } & { \quad \mathrm { o t h e r w i s e } } \end{array} \right. } \end{array}
$$

and define $\overline { { u } } : \mathbb { R } ^ { D _ { Y } } \times \mathbb { R } ^ { D _ { X } }  \mathbb { R }$ as

$$
\overline { { u } } ( y , x ) = \sum _ { k = 1 } ^ { K ^ { * } } \frac { \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) s _ { k } ( y , x ) } { \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) + \rho _ { 2 } ( 2 \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) ) } .
$$

Then when $y \in \mathcal { M } _ { Y | x }$ and $x \in \mathcal { M } _ { X }$ , since $\{ \omega _ { k } = ( x _ { k } ^ { * } , y _ { k } ^ { * } ) \} _ { k = 1 } ^ { K ^ { * } } \subset \mathcal { M }$ is a $\scriptstyle { \frac { \tau } { \sqrt { 2 } } }$ -covering set of $\mathcal { M }$ , it holds that

$$
\sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) \ge 1 ,
$$

and thus

$$
\begin{array} { r l } & { \overline { { u } } ( y , x ) = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \frac { \rho _ { 2 } ( 2 \| \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) s _ { k } ( y , x ) } { \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } \big ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } \big ) ^ { \frac { 1 } { 2 } } } } \\ & { = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \frac { \rho _ { 2 } \big ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } \big ) \overline { { \nu } } _ { k } ( Q _ { [ k ] } ( y ) \big ) x \big ( \operatorname* { d e t } \big ( \mathcal { J } _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( Q _ { [ k ] } ( y ) \big ) ^ { T } \mathcal { J } _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( Q _ { [ k ] } ( y ) ) \big ) \big ) ^ { - \frac { 1 } { 2 } } } { \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } \big ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } \big ) } } \\ &  = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \frac { \rho _ { 2 } \big ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } \big ) \nu _ { k } ( Q _ { [ k ] } ( y ) \big ) \big ( x \big ) \Big ( \operatorname* { d e t } \big ( \mathcal { J } _ { G [ k ] } ( \cdot , x ) \big ( Q _ { [ k ] } ( y ) \big ) ^ { T } \mathcal { J } _ { G _ { [ k ] } ( \cdot , x ) } ( Q _ { [ k ] } ( y ) ) \big ) \Big ) ^ { - \frac { 1 } { 2 } } }  \sum _  k = 1 \end{array}
$$

Moreover, given that

$$
\sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) + \rho _ { 2 } ( 2 \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { 2 } ( \frac { 2 \| \omega _ { k } - ( x , y ) \| ^ { 2 } } { \tau ^ { 2 } } ) ) > \frac { 1 } { 2 } ,
$$

in order to show that $\overline { { u } } \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ for some constant $L _ { 1 }$ , it suffices to show that each component of $J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( z )$ 1, as a function with input $( z , x )$ , belongs to $\mathcal { H } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ for a certain constant $L _ { 2 }$ . Then notice that $\overline { { G } } _ { [ k ] } \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } \left( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } \right)$ with $\beta _ { Y } \geq \alpha _ { Y } + 1$ and $\begin{array} { r } { \beta _ { X } \ge \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ . For any $( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { Y } , \alpha _ { X } } ^ { d _ { Y } , D _ { X } }$ , it holds that

$$
\begin{array} { r l } & { \frac { | j _ { 1 } | + 1 } { \beta \gamma } + \frac { | j _ { 2 } | } { \beta \chi } } \\ & { \leq \frac { | j _ { 1 } | + 1 } { \alpha \gamma + 1 } + \frac { | j _ { 2 } | } { \alpha \chi } } \\ & { = \frac { | j _ { 1 } | + 1 + | j _ { 2 } | \frac { \alpha \gamma } { \alpha \chi } } { \alpha \gamma + 1 } } \\ & { = \frac { \alpha \gamma ( \frac { | j _ { 1 } | } { \alpha \chi } + \frac { | j _ { 2 } | } { \alpha \chi } ) + 1 } { \alpha + 1 } < 1 . } \end{array}
$$

Hence, let $e _ { j } \in \mathbb { N } _ { 0 } ^ { d _ { Y } }$ denote the multi-index with the $j$ -th component being 1 and all other components being 0. It holds for any $k \in [ K ^ { * } ]$ and $j \in [ d _ { Y } ]$ that

$$
\sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { Y } , \alpha _ { X } } ^ { d _ { Y } , D _ { X } } } \operatorname* { s u p } _ { ( x , y ) \in \mathbb { R } ^ { d _ { 1 } } \times \mathbb { R } ^ { d _ { 2 } } } | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) | \leq L .
$$

Furthermore, for any $( j _ { 1 } , j _ { 2 } ) \in \mathcal { T } _ { \alpha _ { Y } , \alpha _ { X } } ^ { d _ { Y } , D _ { X } }$ with $\begin{array} { r } { \frac { | j _ { 1 } | } { \alpha _ { Y } } + \frac { | j _ { 2 } | } { \alpha _ { X } } + \frac { 1 } { \alpha _ { Y } } \geq 1 , } \end{array}$

1. if $\begin{array} { r } { \frac { | j _ { 1 } | + 1 } { \beta _ { Y } } + \frac { | j _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } < 1 } \end{array}$ | + 1β < 1, then for any j ∈ [dY ], z, z0 ∈ Rdz with z ̸= z0 and x ∈ RDX , • if $\| z - z _ { 0 } \| \ge 1$ , then

$$
\begin{array} { r } { | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | \le 2 L \le 2 L \| z - z _ { 0 } \| ^ { \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | } . } \end{array}
$$

• if $\| z - z _ { 0 } \| < 1$ , then

$$
\begin{array} { r } { | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | \le \sqrt { d _ { Y } } L \| z - z _ { 0 } \| \le \sqrt { d _ { Y } } L \| z - z _ { 0 } \| ^ { \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | } . } \end{array}
$$

2. if |j1|+1 $\begin{array} { r } { \frac { | j _ { 1 } | + 1 } { \beta _ { Y } } + \frac { | j _ { 2 } | } { \beta _ { X } } + \frac { 1 } { \beta _ { Y } } \ge 1 } \end{array}$ , then since

$$
\begin{array} { r l } & { \beta _ { Y } - ( | j _ { 1 } | + 1 ) - \frac { \beta _ { Y } } { \beta _ { X } } | j _ { 2 } | } \\ & { = \beta _ { Y } ( 1 - \frac { | j _ { 1 } | + 1 } { \beta _ { Y } } - \frac { | j _ { 2 } | } { \beta _ { X } } ) } \\ & { \ge ( \alpha _ { Y } + 1 ) ( 1 - \frac { | j _ { 1 } | + 1 } { \beta _ { Y } } - \frac { | j _ { 2 } | } { \beta _ { X } } ) } \\ & { \ge ( \alpha _ { Y } + 1 ) ( 1 - \frac { | j _ { 1 } | + 1 } { \alpha _ { Y } + 1 } - \frac { | j _ { 2 } | } { \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } ) } \\ & { = \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | , } \end{array}
$$

we have for any $j \in [ d _ { Y } ] , z , z _ { 0 } \in \mathbb { R } ^ { d _ { z } }$ with $z \neq z _ { 0 }$ and $\boldsymbol { x } \in \mathbb { R } ^ { D _ { X } }$ ,

• if $\| z - z _ { 0 } \| \ge 1$ , then

$$
\begin{array} { r } { | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | \le 2 L \le 2 L \| z - z _ { 0 } \| ^ { \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | } . } \end{array}
$$

• if $\| z - z _ { 0 } \| < 1$ , then

$$
| G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | \leq L \| z - z _ { 0 } \| ^ { \beta _ { Y } - | j _ { 1 } | - 1 - \frac { \beta _ { Y } } { \beta _ { X } } | j _ { 2 } | } \leq L \| z - z _ { 0 } \| ^ { \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | } .
$$

Therefore, there exists a constant $L ^ { \prime }$ so that for any $j \in [ d _ { Y } ]$ ,

$$
\sum _ { \{ j _ { 1 } , j _ { 2 } \} \in \mathcal { I } _ { \alpha _ { Y } , D _ { X } } ^ { d _ { Y } , D _ { X } } } \operatorname* { s u p } _ { z , z _ { 0 } \in \mathbb { R } ^ { d _ { Y } , x \in \mathbb { R } ^ { D _ { X } } } } \frac { | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z _ { 0 } , x ) | } { \| z - z _ { 0 } \| ^ { \alpha _ { Y } - | j _ { 1 } | - \frac { \alpha _ { Y } } { \alpha _ { X } } | j _ { 2 } | } } \leq L ^ { \prime } .
$$

Similarly, using the fact that for any $j _ { 1 } , j _ { 2 } \in \mathcal { T } _ { \alpha _ { Y } , \alpha _ { X } } ^ { d _ { Y } , D _ { X } }$ with $\begin{array} { r } { { \frac { | j _ { 1 } | } { \alpha _ { Y } } } + { \frac { | j _ { 2 } | + 1 } { \alpha _ { X } } } \ge 1 } \end{array}$

$$
\begin{array} { r l } {  { \beta _ { X } - \vert j _ { 2 } \vert - \frac { \beta _ { X } } { \beta _ { Y } } ( \vert j _ { 1 } \vert + 1 ) = \beta _ { X } ( 1 - \frac { \vert j _ { 2 } \vert } { \beta _ { X } } - \frac { \vert j _ { 1 } \vert + 1 } { \beta _ { Y } } ) } \quad } & { } \\ & { \geq ( \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } ) \cdot ( 1 - \frac { \vert j _ { 2 } \vert } { \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } - \frac { \vert j _ { 1 } \vert + 1 } { \alpha _ { Y } + 1 } ) } \\ & { = \alpha _ { X } - \vert j _ { 2 } \vert - \frac { \alpha _ { X } } { \alpha _ { Y } } \vert j _ { 1 } \vert . } \end{array}
$$

We can also show that for any $j \in [ d _ { Y } ]$ ,

$$
\sum _ { \substack { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \alpha _ { Y } , \alpha _ { X } } ^ { d _ { Y } , D _ { X } } } } \operatorname* { s u p } _ { x \in \mathbb { R } ^ { d _ { Y } } , x , x _ { 0 } \in \mathbb { R } ^ { D _ { X } } } \frac { | G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x ) - G _ { [ k ] } ^ { ( e _ { j } + j _ { 1 } , j _ { 2 } ) } ( z , x _ { 0 } ) | } { \| x - x _ { 0 } \| ^ { \alpha _ { X } - | j _ { 2 } | - \frac { \alpha _ { X } } { \alpha _ { Y } } | j _ { 1 } | } } \leq L ^ { \prime } .
$$

By combining all pieces, we can obtain that there exists a constant $L _ { 1 }$ so that

$$
J _ { \overline { { G } } _ { [ k ] } ( \cdot , x ) } ( \cdot ) \in \mathcal { H } _ { L _ { 1 } , D _ { Y } d _ { Y } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } ) ,
$$

which implies that there exists a constant $L _ { 2 }$ so that $\overline { { u } } \in \mathcal { H } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$

Now it remains to show Claim 2. For any $( x , y ) \in { \mathcal { M } }$ , if there exists $k _ { 1 } \neq k _ { 2 }$ so that $\| \omega _ { k _ { 1 } } - ( x , y ) \| < \tau$ and $\| \omega _ { k _ { 2 } } - ( x , y ) \| < \tau$ , then by change of variable formula, we have

$$
{ } _ { 1 } ( Q _ { [ k _ { 1 } ] } ( y ) | x ) = \nu _ { k _ { 2 } } ( Q _ { [ k _ { 2 } ] } ( y ) | x ) \sqrt { \left( \operatorname * { d e t } ( J _ { Q _ { [ k _ { 2 } ] } ( G _ { [ k _ { 1 } ] } ( \cdot , x ) ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } ( G _ { [ k _ { 1 } ] } ( \cdot , x ) ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ) \right) } ,
$$

and

$$
\begin{array} { r l } & { \nu _ { k _ { 1 } } ( Q _ { [ k _ { 1 } ] } ( y ) | x ) ( \operatorname* { d e t } ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ) ) ^ { - \frac { 1 } { 2 } } } \\ & { = \nu _ { k _ { 2 } } ( Q _ { [ k _ { 2 } ] } ( y ) | x ) } \\ & { \cdot \sqrt { \frac { \operatorname* { d e t } ( J _ { Q _ { [ k _ { 2 } ] } ( G _ { [ k _ { 1 } ] } ( \cdot , x ) ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } ( G _ { [ k _ { 1 } ] } ( \cdot , \cdot , x ) ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ) } { \operatorname* { d e t } ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ) ^ { T } J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) } } } \\ & { = \nu _ { k _ { 2 } } ( Q _ { [ k _ { 2 } ] } ( y ) | x ) } \\ &  \cdot \sqrt  \frac { \operatorname* { d e t } ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } ( y ) } \mathcal { N } _ { J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } } ( Q _ { [ k _ { 1 } ] } ( y ) ) ) }  \operatorname* { d e t } ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _  [ k _ { 1 } ] \end{array}
$$

Then using the fact that for any $y ^ { \prime } \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { k _ { 1 } } ^ { * } , \tau ) \cap \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y _ { k _ { 2 } } ^ { * } , \tau )$

$$
G _ { [ k _ { 1 } ] } ( Q _ { [ k _ { 1 } ] } ( y ^ { \prime } ) , x ) = G _ { [ k _ { 2 } ] } ( Q _ { [ k _ { 2 } ] } ( G _ { [ k _ { 1 } ] } ( Q _ { [ k _ { 1 } ] } ( y ^ { \prime } ) , x ) ) , x ) ,
$$

we can get

$$
J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) = J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 2 } ] } ( y ) ) J _ { Q _ { [ k _ { 2 } ] } } ( y ) J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) .
$$

So we can write

$$
\begin{array} { r l } & { \mathrm { e t } \Big ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 1 } ] } ( y ) \big ) ^ { T } J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 1 } ] } ( y ) \big ) \Big ) } \\ & { = \mathrm { d e t } \Big ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } } ( y ) ^ { T } J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 2 } ] } ( y ) ) ^ { T } J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 2 } ] } ( y ) ) J _ { Q _ { [ k _ { 2 } ] } } ( y ) J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } } \\ & { = \mathrm { d e t } \Big ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } } ( y ) ^ { T } \Big ) \mathrm { d e t } \Big ( J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 2 } ] } ( y ) ) ^ { T } J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 2 } ] } ( y ) ) \Big ) } \\ & { \qquad \cdot \mathrm { d e t } \Big ( J _ { Q _ { [ k _ { 2 } ] } } ( y ) J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) \Big ) } \\ &  = \mathrm { d e t } \Big ( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } ( Q _ { [ k _ { 1 } ] } ( y ) ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } } ( y ) ^ { T } J _ { Q _ { [ k _ { 2 } ] } } ( y ) J _  G _  [ k _  1  \end{array}
$$

Therefore, we have

$$
\begin{array} { r l } & { \nu _ { k _ { 1 } } ( Q _ { [ k _ { 1 } ] } ( y ) | x ) \left( \operatorname* { d e t } \left( J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 1 } ] } ( y ) \big ) ^ { T } J _ { G _ { [ k _ { 1 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 1 } ] } ( y ) \big ) \right) \right) ^ { - \frac { 1 } { 2 } } } \\ & { = \nu _ { k _ { 2 } } ( Q _ { [ k _ { 2 } ] } ( y ) | x ) \left( \operatorname* { d e t } \left( J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 2 } ] } ( y ) \big ) ^ { T } J _ { G _ { [ k _ { 2 } ] } ( \cdot , x ) } \big ( Q _ { [ k _ { 2 } ] } ( y ) \big ) \right) \right) ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

That implies that for any $( x , y ) \in { \mathcal { M } }$ and $k \in [ K ^ { * } ]$ , if $\| \omega _ { k } - ( x , y ) \| < \tau$ , then

$$
\begin{array} { r } { u ( y , x ) = \nu _ { k } ( Q _ { [ k ] } ( y ) | x ) \left( \mathrm { d e t } \Big ( J _ { G _ { [ k ] } ( \cdot , x ) } \big ( Q _ { [ k ] } ( y ) \big ) ^ { T } J _ { G _ { [ k ] } ( \cdot , x ) } \big ( Q _ { [ k ] } ( y ) \big ) \Big ) \right) ^ { - \frac { 1 } { 2 } } , } \end{array}
$$

which concludes the proof of Claim 2. The proof of the first statement in Lemma 5 is now concluded.

Then we show the second statement in Lemma 5. For any $\omega _ { 0 } = ( x _ { 0 } , y _ { 0 } ) \in \mathcal { M }$ , we can express $\widetilde { v } _ { \omega _ { 0 } }$ as

$$
\widetilde { v } _ { \omega _ { 0 } } ( z , x ) = u ( \widetilde { G } _ { \omega _ { 0 } } ( z , x ) | x ) \cdot \sqrt { \operatorname* { d e t } ( J _ { \widetilde { G } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } J _ { \widetilde { G } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ) } .
$$

Let $\overline { { G } } _ { \omega _ { 0 } } ~ \in ~ \overline { { \mathcal { H } } } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $\widetilde { G } _ { \omega _ { 0 } }$ and $\overline { { u } } \in \mathcal { H } _ { L , D _ { Y } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { D _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ be a smooth extension of $u$ , using $\begin{array} { r } { \beta _ { Y } \ge 2 \lor ( \alpha _ { Y } + 1 ) , \beta _ { X } \ge \alpha _ { X } + \frac { \alpha _ { X } } { \alpha _ { Y } } } \end{array}$ , $\alpha _ { Y } \geq \alpha _ { X }$ , we have $\overline { { u } } ( \overline { { G } } _ { \omega _ { 0 } } ( z , x ) | x ) \in$ $\mathcal { H } _ { L _ { 1 } , D _ { Y } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ for a constant $L _ { 1 }$ Y. Then notice that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ , and $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )$

$$
J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) \succeq \frac { 1 } { L ^ { 2 } } I _ { d _ { Y } } .
$$

So there exist a constant $\tau _ { 2 }$ so that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } + \tau _ { 2 } )$ , and $x \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( x _ { 0 } , \tau + \tau _ { 2 } )$ ,

$$
J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) \succeq \frac { 1 } { 2 L ^ { 2 } } I _ { d _ { Y } } .
$$

Therefore, consider the smooth transition function $\rho _ { a } ( \cdot )$ , we define $\overline { { v } } _ { \omega _ { 0 } } : \mathbb { R } ^ { d _ { Y } } \times \mathbb { R } ^ { D _ { X } }  \mathbb { R }$ as

$$
( z , x ) = \overline { { u } } ( \overline { { G } } _ { \omega _ { 0 } } ( z , x ) | x ) \sqrt { \operatorname* { d e t } ( J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ^ { T } J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) ) } \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert z \Vert ^ { 2 } } { \tau _ { 1 } ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau } ) ^ { 2 } } ( \frac { \Vert x - x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x - x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x - x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x - x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac { \Vert x _ { 0 } \Vert ^ { 2 } } { \tau ^ { 2 } } ) \rho _ { ( 1 + \frac { \tau _ { 2 } } { 2 \tau _ { 1 } } ) ^ { 2 } } ( \frac  \Vert x _ { 0 }
$$

By applying the same argument as in the proof of statement 1, we can establish that $J _ { \overline { { G } } _ { \omega _ { 0 } } ( \cdot , x ) } ( z ) \in$ $\mathcal { H } _ { L _ { 1 } , D _ { Y } d _ { Y } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ and therefore $\overline { { v } } _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ , for some constants $L _ { 1 } , L _ { 2 }$ . Additionally, $\widetilde { v } _ { \omega _ { 0 } } \in \mathcal { H } _ { L _ { 2 } } ^ { \alpha _ { Y } , \alpha _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) \bigr )$ $\dot { \overline { { \nu } } } _ { \omega _ { 0 } } ( z , x ) = \widetilde { \nu } _ { \omega _ { 0 } } ( z , x )$ holds for any . $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ and $x \in B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )$ . Consequently,

# E.8 Proof of Lemma 6

For any $\omega ^ { \ast } = ( x ^ { \ast } , y ^ { \ast } )$ , let $V _ { \omega ^ { * } }$ be an arbitrary orthonormal basis of $T _ { \mathcal { M } _ { Y \mid x ^ { * } } } y ^ { * }$ , and denote $G _ { \omega ^ { * } } ( z , x ) =$ $\Phi _ { \omega ^ { * } } ( V _ { \omega ^ { * } } z , x )$ , $Q _ { \omega ^ { * } } ( y ) = V _ { \omega ^ { * } } ^ { T } ( y - y ^ { * } )$ and $U _ { Y | x } ^ { \omega ^ { * } } = U _ { \omega ^ { * } } \cap \mathcal { M } _ { Y | x }$ . Then since $\mathcal { M } _ { Y \mid x }$ has a reach no smaller than $\tau$ , by by Lemma 2 of Aamari and Levrard [2019], it holds that $\begin{array} { r l } { } & { { } \mathbb { B } _ { \mathcal { M } _ { Y \mid x } } ( y ^ { * } , \frac { 7 \tau _ { 1 } } { 8 } \wedge \frac { 7 \tau } { 1 6 } ) \ \subset } \end{array}$ $U _ { Y | x } ^ { \omega ^ { * } }$ . Moreover, according to Lemma 5, the density of the push forward measure $[ Q _ { \omega ^ { * } } ( \cdot ) ] _ { \# } ( \mu _ { Y | x } ^ { * } | _ { U _ { Y | x } ^ { \omega ^ { * } } } )$ , denoted as $v _ { \omega ^ { * } } ( z | x )$ , satisfies that $v _ { \omega ^ { * } } ( z , | , x ) \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } \bigl ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) \bigr )$ . Based on the

Claim 3. For any $( x ^ { \ast } , y ^ { \ast } ) \in \mathcal { M }$ and $x \in \mathbb { B } _ { \mathcal { M } _ { X } } ( x ^ { * } , \tau )$ , it holds for any $\begin{array} { r } { r \leq \frac { 7 \tau _ { 1 } } { 8 } \land \frac { 7 \tau } { 1 6 } } \end{array}$ and any measurable function $g : \mathcal { M } _ { Y | x }  \mathbb { R }$ that

$$
\mathtt { l } _ { \mu _ { Y | z } ^ { * } } [ g ( Y ) \cdot \mathbf { 1 } ( Y \in \mathbb { B } _ { \mathcal { M } _ { Y | z } } ( y ^ { * } , r ) ) ] = \int _ { \mathbb { B } _ { \mathtt { N } ^ { d } Y } ( \mathbf { 0 } , \tau _ { 1 } ) } g ( G _ { \omega ^ { * } } ( z , x ) ) \mathbf { 1 } ( G _ { \omega ^ { * } } ( z , x ) \in \mathbb { B } _ { \mathcal { M } _ { Y | z } } ( y ^ { * } , r ) ) ) v _ { \omega ^ { * } } ( x , x ) \mathrm { d } \mu _ { Y | z } | _ { z } \mathtt { m } ( \mathtt { N } ^ { \mathtt { e } } ) ,
$$

Indeed, denote $\mathrm { v o l } _ { \mathcal { M } _ { Y \mid x } }$ as the volume measure of $\mathcal { M } _ { Y \mid x }$ , and let $u ( y \mid x )$ be the density of $\mu _ { Y | x } ^ { * }$ with respect to $\mathrm { v o l } _ { \mathcal { M } _ { Y \mid x } }$ . We can obtain that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { Y | x } ^ { * } } [ g ( Y ) \cdot \mathbf { 1 } ( Y \in \mathbb { B } _ { M _ { Y | x } } ( y ^ { * } , r ) ) ] = \displaystyle \int g ( y ) \cdot \mathbf { 1 } ( y \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y ^ { * } , r ) ) u ( y | x ) \mathrm { d v o l } _ { \mathcal { M } _ { Y | x } } ( y ) } \\ & { = \displaystyle \int _ { U _ { Y | x } ^ { * * } } g ( y ) \cdot \mathbf { 1 } ( y \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y ^ { * } , r ) ) u ( y | x ) \mathrm { d v o l } _ { \mathcal { M } _ { Y | x } } ( y ) } \\ & { = \displaystyle \int _ { \mathbb { B } _ { \mathbf { 2 } ^ { d } Y } ( \mathbf { 0 } , \tau ) } g ( G _ { \omega ^ { * } } ( z , x ) ) \mathbf { 1 } ( G _ { \omega ^ { * } } ( z , x ) \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y ^ { * } , r ) ) u ( G _ { \omega ^ { * } } ( z , x ) | x ) \sqrt { \operatorname* { d e t } ( J _ { G _ { \omega ^ { * } } ( \cdot , x ) } ( z ) ^ { T } , \mathcal { M } ) ( \mathcal { M } _ { Y | x } ( y ^ { * } , r ) ) } } \\ & { = \displaystyle \int _ { \mathbb { B } _ { \mathbf { 2 } ^ { d } Y } ( \mathbf { 0 } , \tau _ { 1 } ) } g ( G _ { \omega ^ { * } } ( z , x ) ) \mathbf { 1 } ( G _ { \omega ^ { * } } ( z , x ) \in \mathbb { B } _ { \mathcal { M } _ { Y | x } } ( y ^ { * } , r ) ) ) v _ { \omega ^ { * } } ( z | x ) \mathrm { d } z , } \end{array}
$$

which proves Claim 3. Then let $\{ \omega _ { k } ^ { * } = ( x _ { k } ^ { * } , y _ { k } ^ { * } ) \} _ { k = 1 } ^ { K ^ { * } } \subset \mathcal { M }$ be a $\tau _ { 2 }$ -covering set of $\mathcal { M }$ , and consider a smooth transition function $\rho : \mathbb { R }  [ 0 , 1 ]$ that satisfies $\rho ( t ) = 1$ when $t \in [ 0 , 1 ]$ and $\rho ( t ) = 0$ when $t \in [ 2 , \infty )$ (for example, the function defined in (47)). For $k \in [ K ^ { * } ]$ , define

$$
\widetilde { \rho } _ { [ k ] } ( x , y ) = \rho ( \frac { \| x - x _ { k } ^ { * } \| ^ { 2 } } { \tau _ { 2 } ^ { 2 } } ) \rho ( \frac { \| y - y _ { k } ^ { * } \| ^ { 2 } } { \tau _ { 2 } ^ { 2 } } ) .
$$

and

$$
\rho _ { [ k ] } ( x , y ) = \frac { \widetilde { \rho } _ { [ k ] } ( x , y ) } { \kappa \Big ( \sum _ { k ^ { \prime } = 1 } ^ { K ^ { * } } \widetilde { \rho } _ { [ k ^ { \prime } ] } ( x , y ) \Big ) } ,
$$

with

$$
\kappa ( t ) = t ( 1 - \rho ( 2 t ) ) + \frac { \rho ( 2 t ) } { 2 } .
$$

We can verify that $\kappa ( t ) \geq 1 / 2$ holds for any $t > 0$ and $\kappa ( t ) = t$ if $t \geq 1$ . Consequently, $\rho _ { [ k ] }$ is a smooth function defined over the entire space of $\mathbb { R } ^ { D _ { X } } \times \mathbb { R } ^ { D _ { Y } }$ . Additionally, for any $( x , y ) \in { \mathcal { M } }$ , there exists $k ^ { \prime } \in [ K ^ { * } ]$ so that $\| ( x _ { k ^ { \prime } } ^ { * } , y _ { k ^ { \prime } } ^ { * } ) - ( x , y ) \| \leq \tau _ { 2 }$ . Consequently, $\begin{array} { r } { \sum _ { k = 1 } ^ { K ^ { * } } \tilde { \rho } _ { [ k ] } ( x , y ) \geq \widetilde { \rho } _ { [ k ^ { \prime } ] } ( x , y ) \geq 1 } \end{array}$ . Therefore, when $( x , y ) \in { \mathcal { M } }$ , it holds that $\begin{array} { r } { \rho _ { [ k ] } ( x , y ) = \widetilde { \rho } _ { [ k ] } ( x , y ) / \sum _ { k ^ { \prime } = 1 } ^ { K ^ { * } } \widetilde { \rho } _ { [ k ^ { \prime } ] } ( x , y ) } \end{array}$ e and $\begin{array} { r } { \sum _ { k = 1 } ^ { K ^ { * } } \rho _ { [ k ] } ( x , y ) = } \end{array}$ 1. Furthermore, given that for any $k \in [ K ^ { * } ]$ , $G _ { \omega _ { k } ^ { * } } ( z , x ) \in \mathcal { H } _ { L } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$ and $v _ { \omega _ { k } ^ { * } } ( z , | , x ) \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau ) )$ , there exist $G _ { [ k ] } ^ { \ast } \in \mathcal { H } _ { L } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ and $\tilde { \nu } _ { [ k ] } ^ { * } \in$ $\mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { Y } , \alpha _ { X } } ( \mathbb { R } ^ { d _ { Y } } , \mathbb { R } ^ { D _ { X } } )$ such that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } )$ and $x \in B _ { \mathcal { M } _ { X } } ( x _ { 0 } , \tau )$ , $G _ { [ k ] } ^ { * } ( z , x ) = G _ { \omega _ { k } ^ { * } } ( z , x )$ and $\widetilde { \nu } _ { [ k ] } ^ { \ast } ( z | x ) = \nu _ { \omega _ { k } ^ { \ast } } ( z | x )$ . Then based on $\begin{array} { r } { \sqrt { 2 } \tau _ { 2 } \le \frac { \sqrt { 2 } } { 4 } \bigl ( \tau \wedge \tau _ { 1 } \bigr ) < \frac { 7 \tau _ { 1 } } { 8 } \wedge \frac { 7 \tau } { 1 6 } } \end{array}$ and Claim 3, we have

$$
\begin{array} { r l } { \mathbb { E } _ { \mu _ { Y | \tau } ^ { \star } } [ g ( Y ) ] = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \mathbb { E } _ { \mu _ { Y | \tau | } ^ { \star } } [ g ( Y ) \rho _ { [ k ] } ( x , Y ) ] } & { } \\ & { = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \mathbb { E } _ { \mu _ { Y | \tau | } ^ { \star } } [ g ( Y ) \rho _ { [ k ] } ( x , Y ) \cdot \mathbf { 1 } ( Y \in \mathbb { B } _ { M _ { Y | \tau | } } ( y _ { k } , 2 \tau _ { 2 } ) ) ] } \\ & { = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { R } _ { \mathbf { e } ^ { d _ { Y | \tau | } } } } g ( G _ { [ k ] } ^ { * } ( z , x ) ) \rho _ { [ k ] } ( x , G _ { [ k ] } ^ { * } ( z , x ) ) \mathbf { 1 } ( G _ { [ k ] } ^ { * } ( z , x ) \in \mathbb { B } _ { M _ { Y | \tau | } } ( y _ { k } , \sqrt { 2 } \tau _ { 2 } ) } \\ & { = \displaystyle \sum _ { k = 1 } ^ { K ^ { * } } \int _ { \mathbb { B } _ { \mathbf { e } ^ { d _ { Y | \tau | } } } ( 0 , \tau _ { 1 } ) } g ( G _ { [ k ] } ^ { * } ( z , x ) ) \rho _ { [ k ] } ( x , G _ { [ k ] } ^ { * } ( z , x ) ) \widetilde { \sigma } _ { [ k ] } ^ { * } ( z | x ) \mathrm { d } z . } \end{array}
$$

Then let $v _ { [ k ] } ^ { \ast } ( z , x ) = \rho _ { [ k ] } ( x , G _ { [ k ] } ^ { \ast } ( z , x ) ) \widetilde { v } _ { [ k ] } ^ { \ast } ( z | x )$ , we can get the desired result.

# E.9 Proof of Lemma 10

The proof uses a similar argument as in the proof of Lemma 2 (see Appendix E.4). For any $( l _ { 1 } , l _ { 2 } ) \in$ $\mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , \bar { d } _ { 2 } } = \{ l _ { 1 } \in \mathbb { N } _ { 0 } ^ { d _ { 1 } } , l _ { 2 } \in \mathbb { N } _ { 0 } ^ { d _ { 2 } } : \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } < 1 \}$ , since $\phi _ { 1 } , \phi _ { 2 }$ are smooth compactly supported, we have

$$
\begin{array} { r l } & { | f ^ { ( l _ { 1 } , l _ { 2 } ) } ( x , y ) | = \displaystyle \left| \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ^ { ( l _ { 1 } ) } ( m _ { 1 } x - \xi _ { 1 } ) \phi _ { 2 } ^ { ( l _ { 2 } ) } ( m _ { 2 } y - \xi _ { 2 } ) \right| } \\ & { \leq L \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \leq L _ { 1 } \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 1 } ^ { \alpha _ { 1 } | l _ { 2 } | / \alpha _ { 2 } } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \leq L _ { 1 } . } \end{array}
$$

Furthermore, by employing a similar approach to that used in the proof of Claim 1, and considering the relationship $| \omega _ { \xi _ { 1 } , \xi _ { 2 } } | \lesssim m _ { 1 } ^ { - \alpha _ { 1 } } \asymp m _ { 2 } ^ { - \alpha _ { 2 } }$ , we can demonstrate that for any $x , x ^ { \prime } \in \mathbb { R } ^ { d _ { 1 } }$ , $\boldsymbol { y } \in \mathbb { R } ^ { d _ { 2 } }$ , and any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 1 } } \ge 1 } \end{array}$ , it holds that

$$
\begin{array} { r l } & { \Bigl | \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \displaystyle \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ^ { ( l _ { 1 } ) } ( m _ { 1 } x - \xi _ { 1 } ) \phi _ { 2 } ^ { ( l _ { 2 } ) } ( m _ { 2 } y - \xi _ { 2 } ) } \\ & { \quad - \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \displaystyle \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ^ { ( l _ { 1 } ) } ( m _ { 1 } x ^ { \prime } - \xi _ { 1 } ) \phi _ { 2 } ^ { ( l _ { 2 } ) } ( m _ { 2 } y - \xi _ { 2 } ) \Bigr | } \\ & { \le L _ { 1 } \| x - x ^ { \prime } \| ^ { \alpha _ { 1 } - | l _ { 1 } | - \frac { \alpha _ { 1 } } { \alpha _ { 2 } } | l _ { 2 } | } . } \end{array}
$$

Moreover, for any $( l _ { 1 } , l _ { 2 } ) \in \mathcal { I } _ { \alpha _ { 1 } , \alpha _ { 2 } } ^ { d _ { 1 } , d _ { 2 } }$ with $\begin{array} { r } { \frac { | l _ { 1 } | } { \alpha _ { 1 } } + \frac { | l _ { 2 } | } { \alpha _ { 2 } } + \frac { 1 } { \alpha _ { 2 } } \ge 1 } \end{array}$ , and for any $\boldsymbol { x } \in \mathbb { R } ^ { d _ { 1 } }$ , $y , y ^ { \prime } \in \mathbb { R } ^ { d _ { 2 } }$ ,

$$
\begin{array} { r l } & { \displaystyle | \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ^ { ( l _ { 1 } ) } ( m _ { 1 } x - \xi _ { 1 } ) \phi _ { 2 } ^ { ( l _ { 2 } ) } ( m _ { 2 } y - \xi _ { 2 } ) } \\ & { \quad - \frac { m _ { 1 } ^ { | l _ { 1 } | } m _ { 2 } ^ { | l _ { 2 } | } } { ( m _ { 1 } ) ^ { \alpha _ { 1 } } } \sum _ { \xi _ { 1 } \in [ m _ { 1 } ] ^ { d _ { 1 } } } \sum _ { \xi _ { 2 } \in [ m _ { 2 } ] ^ { d _ { 2 } } } \omega _ { \xi _ { 1 } , \xi _ { 2 } } \phi _ { 1 } ^ { ( l _ { 1 } ) } ( m _ { 1 } x - \xi _ { 1 } ) \phi _ { 2 } ^ { ( l _ { 2 } ) } ( m _ { 2 } y ^ { \prime } - \xi _ { 2 } ) \Big | } \\ & { \leq L _ { 1 } \| y - y ^ { \prime } \| ^ { \alpha _ { 2 } - | l _ { 2 } | - \frac { \alpha _ { 2 } } { \alpha _ { 1 } } | l _ { 1 } | } . } \end{array}
$$

We can then conclude that there exists a constant $L _ { 1 }$ so that $f \in \mathcal { H } _ { L _ { 1 } } ^ { \alpha _ { 1 } , \alpha _ { 2 } } ( \mathbb { R } ^ { d _ { 1 } } , \mathbb { R } ^ { d _ { 2 } } )$

# E.10 Proof of Theorem 8

Denote the loss function

$$
\ell ( x , y , S ) = \sum _ { \lambda \in \Lambda } S ( \lambda , x ) ^ { 2 } - 2 \psi _ { \lambda } ( y ) S ( \lambda , x ) .
$$

Then we have

$$
\begin{array} { r l } & { \widehat { S } = \underset { S \in \mathcal { S } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \overset { n } { \underset { i = 1 } { \sum } } \underset { \lambda \in \Lambda } { \sum } ( S ( \lambda , X _ { i } ) - \psi _ { \lambda } ( Y _ { i } ) ) ^ { 2 } } \\ & { \quad = \underset { S \in \mathcal { S } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \overset { n } { \underset { i = 1 } { \sum } } \underset { \lambda \in \Lambda } { \sum } S ( \lambda , X _ { i } ) ^ { 2 } - 2 \psi _ { \lambda } ( Y _ { i } ) S ( \lambda , X _ { i } ) } \\ & { \quad = \underset { S \in \mathcal { S } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \overset { n } { \underset { i = 1 } { \sum } } \ell ( X _ { i } , Y _ { i } , S ) . } \end{array}
$$

Denote $\mu ^ { * } = \mu _ { X } ^ { * } \mu _ { Y | X } ^ { * }$ as the joint distribution of $( X , Y )$ . We have

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } [ \ell ( X , Y , S ) ] } \\ & { = \mathbb { E } _ { \mu ^ { * } } [ \displaystyle \sum _ { \lambda \in \Lambda } \left( S ( \lambda , X ) ^ { 2 } - 2 \psi _ { \lambda } ( Y ) S ( \lambda , X ) \right) ] } \\ & { = \mathbb { E } _ { \mu _ { X } ^ { \star } } [ \displaystyle \sum _ { \lambda \in \Lambda } S ( \lambda , X ) ^ { 2 } ] - 2 \cdot \mathbb { E } _ { \mu _ { X } ^ { \star } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \mathbb { E } _ { \mu _ { Y \mid X } ^ { \star } } [ \psi _ { \lambda } ( Y ) ] S ( \lambda , X ) \right] } \\ & { \quad + \mathbb { E } _ { \mu _ { X } ^ { \star } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( Y ) ] \right) ^ { 2 } \right] - \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( Y ) ] \right) ^ { 2 } \right] } \\ & { = \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( Y ) ] \right) ^ { 2 } \right] - \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } [ \psi _ { \lambda } ( Y ) ] \right) ^ { 2 } \right] . } \end{array}
$$

Furthermore, for $\rho = \mathrm { m a x } \{ \mathrm { s u p } _ { ( x , y ) \in \mathcal { M } } \mathrm { s u p } _ { S \in \mathcal { S } } | \ell ( x , y , S ) | , 1 \}$ , it holds that

$$
\rho \leq \operatorname* { m a x } \{ \operatorname* { s u p } _ { ( x , y ) \in { \mathcal { M } } } \operatorname* { s u p } _ { S \in { \mathcal { S } } } \sum _ { \lambda \in \Lambda } \left( S ( \lambda , x ) ^ { 2 } + 2 | \psi _ { \lambda } ( y ) S ( \psi , x ) | \right) , 1 \} \leq \operatorname* { m a x } \{ 2 C , 1 \} .
$$

Then let

$$
S ^ { * } \in \arg \operatorname* { m i n } _ { S \in { \mathcal { S } } } \mathbb { E } _ { \mu ^ { * } } [ \ell ( X , Y , S ) ] = \arg \operatorname* { m i n } _ { S \in { \mathcal { S } } } \mathbb { E } _ { \mu _ { X } ^ { * } } \bigg [ \sum _ { \lambda \in \Lambda } \Big ( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \Big ) ^ { 2 } \bigg ] .
$$

Consider the function class

$$
\mathcal { G } ^ { * } = \{ g ( x , y ) = \ell ( x , y , S ) - \ell ( x , y , S ^ { * } ) : S \in \mathcal { S } \}
$$

and the star hull

$$
{ \overline { { \mathcal { G } } } } ^ { * } = \{ g ( x , y ) = a ( \ell ( x , y , S ) - \ell ( x , y , S ^ { * } ) ) : a \in [ 0 , 1 ] , S \in S \} .
$$

Define the local Rademacher complexity

$$
\mathcal { R } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , r ) = \mathbb { E } _ { \mu ^ { * } } , \otimes n \left[ \operatorname* { s u p } _ { \begin{array} { c } { g \in \overline { { \mathcal { G } } } ^ { * } } \\ { \mathbb { E } _ { \mu ^ { * } } [ g ^ { 2 } ] \leq r ^ { 2 } } \end{array} } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , Y _ { i } ) - \mathbb { E } _ { \mu ^ { * } } \left[ g ( x , y ) \right] \right| \right] ,
$$

where we uses the notation $\mathbb { E } _ { \mu ^ { * } } [ g ^ { 2 } ] = \mathbb { E } _ { \mu ^ { * } } [ g ( X , Y ) ^ { 2 } ]$ for simplicity. We claim that the critical radius associated with $\overline { { \mathcal { G } } } ^ { * }$ is $\begin{array} { r } { \delta _ { n } = c _ { 1 } \sqrt { \frac { W _ { n } ( \log n + \log T _ { n } ) } { n } } } \end{array}$ Wn(log n+log Tn) for a large enough c1. This implies that

$$
\overline { { { R } } } _ { n } ( \overline { { { \mathcal { G } } } } ^ { * } , \delta _ { n } ) \leq \delta _ { n } ^ { 2 } .
$$

The Claim (54) will be proved later. Then define

$$
M _ { n } ( S ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \ell ( X _ { i } , Y _ { i } , S ) \mathrm { ~ a n d ~ } M ^ { * } ( S ) = \mathbb { E } _ { \mu ^ { * } } [ \ell ( X , Y , S ) ] .
$$

Utilizing the uniform law (see for example, Theorem 14.20 of Wainwright [2019]) in conjunction with the aforementioned Claim (54), we can get that, there exists a constant $C _ { 1 }$ so that it holds with probability larger than $1 - n ^ { - c }$ that

$$
\forall S \in { \mathcal { S } } , \quad \frac { | M _ { n } ( S ) - M _ { n } ( S ^ { * } ) - M ^ { * } ( S ) + M ^ { * } ( S ^ { * } ) | } { \delta _ { n } + \sqrt { \mathbb { E } _ { \mu ^ { * } } [ ( \ell ( x , y , S ) - \ell ( x , y , S ^ { * } ) ) ^ { 2 } ] } } \leq C _ { 1 } \delta _ { n } .
$$

By the assumption that for any $S , S ^ { \prime } \in { \mathcal { S } }$

$$
{  { \mathbb E } } _ { \mu ^ { * } } \Big [ \big ( \ell ( X , Y , S ) - \ell ( X , Y , S ^ { \prime } ) \big ) \Big ] \leq C {  { \mathbb E } } _ { \mu _ { X } ^ { * } } \Big [ \sum _ { \lambda \in \Lambda } \big ( S ( \lambda , X ) - S ^ { \prime } ( \lambda , X ) \big ) ^ { 2 } \Big ] ,
$$

we can get

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu ^ { * } } \big [ ( \ell ( X , Y , S ) - \ell ( X , Y , S ^ { * } ) ) ^ { 2 } \big ] \leq C \mathbb { E } _ { \mu _ { X } ^ { * } } \bigg [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( \widehat { S } ( \lambda , X ) - S ^ { * } ( \lambda , X ) \big ) ^ { 2 } \bigg ] } \\ & { \leq 2 C \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( \widehat { S } ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \big ) ^ { 2 } \Big ] + 2 C \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( S ^ { * } ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \big ) ^ { 2 } } \end{array}
$$

Then, combined with (52), (53), (55), we can get

$$
\begin{array} { r l } & { \displaystyle \mathbb { L } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \widehat S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \left[ \psi _ { \lambda } ( Y ) \right] \right) ^ { 2 } \right] - \displaystyle \operatorname* { m i n } _ { S \in S } \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \left[ \psi _ { \lambda } ( Y ) \right] \right) ^ { 2 } \right] } \\ & { = \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \widehat S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \left[ \psi _ { \lambda } ( Y ) \right] \right) ^ { 2 } \right] - \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( S ^ { * } ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \left[ \psi _ { \lambda } ( Y ) \right] \right) ^ { 2 } \right] } \\ & { = { \cal M } ^ { * } ( \widehat S ) - { \cal M } ^ { * } ( S ^ { * } ) \leq { \cal M } ^ { * } ( \widehat S ) - { \cal M } ^ { * } ( { \cal S } ^ { * } ) + { \cal M } ( { \cal S } ^ { * } ) - { \cal M } _ { n } ( { \cal S } ^ { * } ) - { \cal M } _ { n } ( { \cal S } ) } \\ &  \leq C _ { 1 } \delta _ { n } ^ { 2 } + C _ { 1 } \sqrt { 2 C } \delta _ { n } \cdot \sqrt  \mathbb { E } _ { \mu _ { X } ^ { * } } \left[ \displaystyle \sum _ { \lambda \in \Lambda } \left( \widehat S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \left[ \psi _ { \lambda } ( Y ) \right] \right) ^ { 2 } \right] + \displaystyle \operatorname* { m i n } _  \end{array}
$$

So by combining all pieces, we can get that it holds with probability at least $1 - n ^ { - c }$ that

$$
\begin{array} { r l } & { \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( \widehat S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \big ) ^ { 2 } \Big ] } \\ & { \le C _ { 2 } \Big ( \delta _ { n } ^ { 2 } + \displaystyle \operatorname* { m i n } _ { S \in \mathcal { S } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \big ) ^ { 2 } \Big ] \Big ) \Big ) } \\ & { \le C _ { 2 } \Big ( \displaystyle \frac { W _ { n } ( \log n + \log T _ { n } ) } { n } + \displaystyle \operatorname* { m i n } _ { S \in \mathcal { S } } \mathbb { E } _ { \mu _ { X } ^ { * } } \Big [ \displaystyle \sum _ { \lambda \in \Lambda } \big ( S ( \lambda , X ) - \mathbb { E } _ { \mu _ { Y \mid X } ^ { * } } \big [ \psi _ { \lambda } ( Y ) \big ] \big ) ^ { 2 } \Big ] \Big ) \Big ) . } \end{array}
$$

Now it only remains to show Claim (54). Using standard symmetrization, we can get for any $r > 0$ ,

$$
, r ) = \mathbb { E } _ { \mu ^ { * } , \otimes n } \left[ \operatorname* { s u p } _ { \mathbb { E } _ { \mu ^ { * } } \in \mathcal { G } ^ { * } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } g ( X _ { i } , Y _ { i } ) - \mathbb { E } _ { \mu ^ { * } } \left[ g ( x , y ) \right] \right| \right] \leq \mathbb { E } _ { \mu ^ { * } , \otimes n } \mathbb { E } _ { \epsilon } \left[ \operatorname* { s u p } _ { \mathbb { E } _ { \mu ^ { * } } \in \mathcal { G } ^ { * } \times \mathcal { T } ^ { 2 } } \left| \frac { 2 } { n } \sum _ { i = 1 } ^ { n } \epsilon _ { i } g ( X _ { i } , Y _ { i } ) - \mathbb { E } _ { \mu ^ { * } } \left[ g ( x , y ) \right] \right| \right]
$$

where $\{ \epsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from Rademacher distribution, i.e. $\begin{array} { r } { \mathbb { P } \left( \epsilon _ { i } = 1 \right) = \mathbb { P } \left( \epsilon _ { i } = - 1 \right) = \frac { 1 } { 2 } } \end{array}$

Define $\begin{array} { r } { d _ { n } ^ { g } ( g , g ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( g ( X _ { i } , Y _ { i } ) - g ^ { \prime } ( X _ { i } , Y _ { i } ) ) ^ { 2 } } } \end{array}$ , then

$$
r _ { n } : = \operatorname* { m a x } _ { \substack { g , g ^ { \prime } \in \overline { { \mathcal { G } } } ^ { * } } } d _ { n } ( g , g ^ { \prime } ) \leq 2 \rho ,
$$

and by equation (3.84) of Wainwright [2019], there exists a constant $C _ { 3 }$ such that,

$$
\begin{array} { r l } { \mathbb { E } _ { \mu ^ { * } \cdot \otimes n } [ r _ { n } ^ { 2 } ] \le \mathbb { E } _ { \mu ^ { * } \cdot \otimes n } \left[ \begin{array} { c c } { \displaystyle \operatorname* { s u p } _ { \tilde { \pi } _ { \rho } \in \overline { { \mathcal { G } } } ^ { * } } } & { \displaystyle \frac { 4 } { n } \sum _ { i = 1 } ^ { n } g ^ { 2 } ( X _ { i } , Y _ { i } ) \Bigg ] } \\ { \displaystyle \operatorname* { s u p } _ { \tilde { \pi } _ { \rho } \ast [ g ^ { 2 } ] \leq r ^ { 2 } } } & { } \end{array} \right] } & { } \\ { \le \mathbb { E } _ { \mu ^ { * } \cdot \otimes n } \left[ \begin{array} { c c } { \displaystyle \operatorname* { s u p } _ { \rho \in \overline { { \mathcal { G } } } ^ { * } } } & { \displaystyle \frac { 8 } { n } \sum _ { i = 1 } ^ { n } ( g ( X _ { i } , Y _ { i } ) - \mathbb { E } _ { \mu ^ { * } } [ g ( x , y ) ] ) ^ { 2 } \Bigg ] + 8 r ^ { 2 } } \\ { \displaystyle \operatorname* { s u p } _ { \rho \ast [ g ^ { 2 } ] \leq r ^ { 2 } } } & { } \end{array} \right] } & { } \\ { \le C _ { 3 } ( r ^ { 2 } + \rho \mathcal { R } _ { n } ( \overline { { g } } ^ { * } , r ) ) . } \end{array}
$$

Moreover, for any $g \in \mathcal { G } ^ { * }$ and $a \in ( 0 , 1 ]$ , there exists an integer $\kappa \in \mathbb { N }$ , such that $\begin{array} { r } { \kappa \frac { \varepsilon } { 2 \rho } < a \leq ( \kappa + 1 ) \frac { \varepsilon } { 2 \rho } } \end{array}$ and $\begin{array} { r } { d _ { n } ^ { g } ( ( \kappa + 1 ) \frac { \varepsilon } { 2 \rho } g , a g ) \le \frac { \varepsilon } { 2 \rho } \rho = \frac { \varepsilon } { 2 } } \end{array}$ . Therefore it follows that the $\varepsilon$ -covering number of $\overline { { \mathcal { G } } } ^ { * }$ with respect to $d _ { n } ^ { g }$ satisfies that, $\begin{array} { r } { \mathbf { N } ( \overline { { \mathcal { G } } } ^ { * } , d _ { n } ^ { g } , \varepsilon ) \leq \mathbf { N } ( \mathcal { G } ^ { * } , d _ { n } ^ { g } , \frac { \varepsilon } { 2 } ) \cdot \frac { 2 \rho } { \varepsilon } } \end{array}$ . Therefore, we can obtain for any $0 < \varepsilon \le r _ { n }$

$$
\begin{array} { l } { \log \mathbf { N } ( \overline { { \mathcal { G } } } ^ { * } , d _ { n } ^ { g } , \varepsilon ) \leq \log \mathbf { N } ( \mathcal { G } ^ { * } , d _ { n } ^ { g } , \frac { \varepsilon } { 2 } ) + \log \displaystyle \frac { 2 \rho } { \varepsilon } = \log \mathbf { N } ( S , d _ { n } , \frac { \varepsilon } { 2 } ) + \log \displaystyle \frac { 2 \rho } { \varepsilon } } \\ { \leq W _ { n } \log \displaystyle \frac { 2 T _ { n } } { \varepsilon } + \log \displaystyle \frac { 2 \rho } { \varepsilon } \leq W _ { n } \log \displaystyle \frac { 4 T _ { n } \rho } { \varepsilon ^ { 2 } } . } \end{array}
$$

Then, by Dudley entropy integral bound Wainwright [2019], Vershynin [2018], we have

$$
\begin{array} { r l } & { \overline { { R } } _ { n } ( \overline { { g } } ^ { * } , r ) \leq \frac { C _ { 4 } } { \sqrt { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ \int _ { 0 } ^ { r _ { n } } \sqrt { W _ { n } } \log \frac { 4 \overline { { \Gamma } } _ { n ^ { \rho } } } { \xi ^ { 2 } } \mathrm { d } \xi \right] } \\ & { = \frac { C _ { 4 } } { \sqrt { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ r _ { n } \int _ { 0 } ^ { 1 } \sqrt { W _ { n } \log \frac { 4 \overline { { T } } _ { n ^ { \rho } } } { \xi ^ { 2 } r _ { n } ^ { 2 } } } \mathrm { d } \xi \right] } \\ & { \leq \frac { C _ { 4 } } { \sqrt { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ r _ { n } \int _ { 0 } ^ { 1 } \sqrt { W _ { n } \log \frac { \overline { { T } } _ { n } } { \xi ^ { 2 } \rho } } \mathrm { d } \xi \right] + \frac { \sqrt { 2 } C _ { 4 } } { \sqrt { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ r _ { n } \int _ { 0 } ^ { 1 } \sqrt { W _ { n } \log \frac { 2 \rho } { r _ { n } } } \mathrm { d } \xi \right] } \\ & { \leq C _ { 4 } \left( \log ( T _ { n } ) + \int _ { 0 } ^ { 1 } \sqrt { 2 \log \frac { 1 } { \xi } } \mathrm { d } \xi \right) \sqrt { \frac { W _ { n } } { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ r _ { n } \right] + 2 C 4 \rho \sqrt { \frac { W _ { n } } { n } } \mathbb { E } _ { n ^ { * } } \omega _ { n } \left[ \sqrt { \left( \frac { T _ { n } } { 2 \rho } \right) ^ { 2 } - \left( \frac { r _ { n } } { 2 \rho } \right) ^ { 2 } } \right. } \\ &  \leq C _ { 3 }  \end{array}
$$

where the last inequality uses that $\sqrt { - y \log y + y }$ is concave and non-decreasing when $\begin{array} { r } { y = ( \frac { r _ { n } } { 2 \rho } ) ^ { 2 } \leq 1 } \end{array}$ . Then by $\mathbb { E } _ { \mu ^ { * , \otimes n } } [ r _ { n } ^ { 2 } ] \leq C _ { 3 } ( r ^ { 2 } + \rho \overline { { R } } _ { n } ( r , \overline { { \mathcal { G } } } ^ { * } ) )$ , there exists some constant $C _ { 6 }$ so that

$$
\overline { { R } } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , r ) \leq C _ { 6 } \sqrt { \frac { W _ { n } } { n } } ( r ^ { 2 } + \rho \overline { { R } } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , r ) ) ^ { \frac { 1 } { 2 } } \sqrt { \log \frac { 1 } { r } + \log T _ { n } } .
$$

Choose $\begin{array} { r } { \delta _ { n } = c _ { 1 } \sqrt { \frac { W _ { n } ( \log n + \log T _ { n } ) } { n } } } \end{array}$ with $c _ { 1 } > 1$ . If $\overline { { R } } _ { n } ( \delta _ { n } , \overline { { \mathcal { G } } } ^ { * } ) > \delta _ { n } ^ { 2 }$ , then

$$
\overline { { R } } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , \delta _ { n } ) \leq C _ { 6 } \sqrt { \frac { W _ { n } } { n } } \sqrt { 2 ( 1 + C ) } \overline { { R } } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , \delta _ { n } ) ^ { \frac { 1 } { 2 } } \sqrt { \log n + \log T _ { n } }
$$

which means

$$
\overline { { R } } _ { n } ( \overline { { \mathcal { G } } } ^ { * } , \delta _ { n } ) \leq 2 ( 1 + C ) C _ { 6 } ^ { 2 } \frac { W _ { n } } { n } ( \log n + \log T _ { n } ) \leq \frac { 2 ( 1 + C ) C _ { 6 } ^ { 2 } } { c _ { 1 } ^ { 2 } } \delta _ { n } ^ { 2 } .
$$

So $\overline { { R } } _ { n } ( \delta _ { n } , \overline { { \mathcal { G } } } ^ { * } ) \leq \delta _ { n } ^ { 2 }$ holds if $c _ { 1 } > \sqrt { 2 ( 1 + C ) C _ { 6 } ^ { 2 } } \vee 1$ . This completes the proof.

# E.11 Proof of Theorem 3

The proof of the lower bound is derived directly from the proof of the lower bound in Theorem 4 as detailed in Appendix D.5. Specifically, consider the construction of the submanifolds described in Appendix D.5. For any $j , k \in [ H ]$ with $j \neq k$ , it is established that:

$$
\begin{array} { r l } & { \quad \underset { x \in \mathcal { M } _ { X } } { \operatorname* { s u p } } \mathbb { H } [ \mathbb { H } ( \mathcal { M } _ { Y | x } ^ { ( j ) } , \mathcal { M } _ { Y | x } ^ { ( k ) } ) = \underset { x \in \mathcal { M } _ { X } } { \operatorname* { s u p } } \mathbb { H } [ \mathcal { M } _ { Y | x } ^ { \omega ( j ) } , \mathcal { M } _ { Y | x } ^ { \omega ( k ) } ) } \\ & { \quad \ge \underset { x \in \mathcal { M } _ { X } \ : z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , 1 ) } { \operatorname* { s u p } } \Vert g _ { \omega ^ { ( j ) } } ( z , x ) - g _ { \omega ^ { ( k ) } } ( z , x ) \Vert } \\ & { \quad \gtrsim \frac { 1 } { m _ { 1 } ^ { \beta _ { Y } } } \asymp n ^ { \frac { 1 } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } . } \end{array}
$$

The desired result then follows in a manner similar to that outlined in Appendix D.5, utilizing Fano’s th $\left\{ ( X _ { i } , Y _ { i } ) \right\} _ { i = 1 } ^ { n }$ , for each $k \in [ n ]$ , we define the local polynomial estimator $( \widehat { V } _ { k } , ( \widehat { a } _ { j _ { 1 } j _ { 2 } k } ) _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , D _ { X } } } )$ $( X _ { k } , Y _ { k } )$ to be any element of

$$
\begin{array} { c } { \displaystyle \underset { { V \in \mathbb { O } ( D _ { Y } , d _ { Y } ) } } { \arg \operatorname* { m i n } } \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { \| Y _ { i } - \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \mathbb { B } _ { X } } ^ { d _ { Y } , \mathbb { B } _ { X } } } \frac { a _ { j _ { 1 } j _ { 2 } } } { j _ { 1 } ! j _ { 2 } ! } ( V ^ { T } ( Y _ { i } - Y _ { k } ) ) ^ { j _ { 1 } } ( X _ { i } - X _ { k } ) ^ { j _ { 2 } } \| ^ { 2 } } } \\ { \displaystyle \underset { { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \mathbb { B } _ { X } } ^ { d _ { Y } , \mathbb { B } _ { X } } } } { \arg \operatorname* { m i n } } } \\ { \cdot \mathbf { 1 } ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( Y _ { k } , h _ { 1 } ) ) \mathbf { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( X _ { k } , h _ { 2 } ) ) , } \end{array}
$$

$h _ { 1 } = b _ { 1 } \left( { \frac { \log n } { n } } \right) ^ { \frac { 1 } { d _ { Y } + { \frac { d _ { X } \beta _ { Y } } { \beta _ { X } } } } }$ , $h _ { 2 } = b _ { 2 } \left( { \frac { \log n } { n } } \right) ^ { \frac { 1 } { d _ { X } + { \frac { d _ { Y } \beta _ { X } } { \beta _ { Y } } } } }$ and $b _ { 1 } , b _ { 2 }$ are large enough constants. Then for any $x \in \mathcal { M } _ { X }$ , consider the estimator $\widehat { \mathcal { M } } _ { Y | x }$ of $\mathcal { M } _ { Y \mid x }$ defined as

$$
\widehat { \mathcal { M } } _ { Y | x } = \bigcup _ { \| X _ { i } ^ { i } = x \| \leq h _ { 2 } } \Big \{ y = \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , d _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \widehat { a } _ { j _ { 1 } j _ { 2 } k } z ^ { j _ { 1 } } ( x - X _ { i } ) ^ { j _ { 2 } } : z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) \Big \} .
$$

We will show $\widehat { \mathcal { M } } _ { Y | x }$ can achieve the upper bound in Theorem 3. Let $V _ { k } \in \mathbb { R } ^ { D _ { Y } \times d _ { Y } }$ be a matrix whose column forms an orthonormal basis of $T _ { \mathcal { M } _ { Y | X _ { k } } } Y _ { k }$ . Consider the function $G _ { [ k ] } ^ { * } ( z , x ) = \Phi _ { ( X _ { k } , Y _ { k } ) } ( V _ { k } ^ { * } z , x )$ , where $\Phi _ { ( X _ { k } , Y _ { k } ) }$ is the one defined in Definition 4 of the main text. It holds with a constant $L$ that $G _ { [ k ] } ^ { \ast } ( z , x ) \in \mathcal { H } _ { L , D _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } ( \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , \tau _ { 1 } ) , \mathbb { B } _ { \mathcal { M } _ { X } } ( X _ { k } , \tau ) )$ . Moreover, notice that $\mathcal { M } _ { X }$ is a $\beta _ { X }$ -smooth manifold, let $W _ { k } ^ { * }$ be a matrix whose column forms an orthornormal basis of $T _ { \mathcal { M } _ { X } } X _ { k }$ and define $g _ { [ k ] } ( s ) =$ $\phi _ { X _ { k } } ( W _ { k } ^ { * } s )$ , where $\phi _ { X _ { k } }$ is the one defined in Definition 3. Denote $\widetilde { G } _ { [ k ] } ( z , s ) = G _ { [ k ] } ^ { * } ( z , g _ { [ k ] } ( s ) )$ , it holds that

$$
\| G _ { [ k ] } ^ { * } ( z , g _ { [ k ] } ( s ) ) - \sum _ { \scriptstyle ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , d _ { X } } ^ { { \beta _ { Y } , \beta _ { X } } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \widetilde { G } _ { [ k ] } { } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) z ^ { j _ { 1 } } s ^ { j _ { 2 } } \| \lesssim \| z \| ^ { \beta _ { Y } } + \| s \| ^ { \beta _ { X } } .
$$

Denote

$$
\widehat { f } _ { [ k ] } ( z , x ) = \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , d _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \widehat { a } _ { j _ { 1 } j _ { 2 } k } ( \widehat { V } _ { k } ^ { T } ( G _ { [ k ] } ^ { * } ( z , x ) - Y _ { k } ) ) ^ { j _ { 1 } } ( x - X _ { k } ) ^ { j _ { 2 } } ,
$$

and $\widetilde { f } _ { [ k ] } ( z , s ) = \widehat { f } _ { [ k ] } ( z , g _ { [ k ] } ( s ) )$ . Then

$$
\| \widehat { f } _ { [ k ] } ( z , g _ { [ k ] } ( s ) ) - \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , d _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) z ^ { j _ { 1 } } s ^ { j _ { 2 } } \| \lesssim \| z \| ^ { \beta _ { Y } } + \| s \| ^ { \beta _ { X } } .
$$

Therefore, denote $Z _ { i k } = V _ { k } ^ { \ast T } ( Y _ { i } - Y _ { k } )$ and $S _ { i k } = W _ { k } ^ { * T } ( X _ { i } - X _ { k } )$ , we have

$$
\begin{array} { r l } & { \quad + \| \hat { x } _ { \perp } \| _ { L ^ { \infty } } \psi _ { 0 } ( x , y ) \| \hat { x } _ { 1 } \psi _ { 1 } , } \\ & { \leq \frac { \eta _ { 1 } ^ { 2 } } { \kappa _ { 1 } } \frac { 1 } { \kappa _ { 1 } } ( \hat { x } _ { 0 } ^ { 2 } \psi _ { 1 } \psi _ { 1 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 }  } \\ & { \qquad - \frac { \eta _ { 1 } ^ { 2 } } { \kappa _ { 1 } } ( \hat { x } _ { 0 } ^ { 2 } \psi _ { 1 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 } \psi _ { 1 } ^ { 2 }   } \\ &  \qquad  + \frac { \eta _ { 1 } ^ { 2 } } { \kappa _ { 1 } } ( \hat { x } _ { 0 } ^ { 2 } \psi _ { 1 } ^  \end{array}
$$

Building on the analysis presented in Tang and Yang [2023a], Aamari and Levrard [2019], we can derive the following lemma, whose proof is given in Section E.11.1.

Lemma 22. For any positive constant c, there exists a constant $C$ so that it holds with probability at

least $1 - n ^ { - c }$ that for any $k \in [ n ]$ ,

$$
\begin{array} { r l } &  \mathbb { E } _ { \mu ^ { k } } \Bigg [ \Bigg \| \underset { ( \hat { \mu } _ { k } \to \hat { \mu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( 1 } ) ) } \times \hat { \mu } _ { k } ^ { \hat { \nu } _ { k } ^ { ( 1 ) } ) } } ) } { \sum _ { i \neq j \leq k } \sum _ { \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( 1 ) } ) } \times \hat { \mu } _ { k } ^ { \hat { \nu } _ { k } ^ { ( 1 ) } ) } } } \frac { 1 } { j ! \hat { \rho } ! } \big | \hat { \mathbf { z } } _ { | k | ^ { \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( 1 ) } \cdot \hat { \mu } _ { j } ) } } ( \mathbf { { \theta } } _ { d \nu } , \mathbf { 0 } _ { d \nu } ) ( V _ { k } ^ { - \mu } ( \{ \boldsymbol { Y } } - \boldsymbol { Y } _ { k } ) ) ) ^ { \hat { \mu } _ { i } } ( W _ { k } ^ { - \mu } ( \boldsymbol { X } - \boldsymbol { X } _ { k } ) ) ^ { \hat { j } } \big | ^ { 2 } } { \displaystyle \Bigg | } } \\ &  - \underset  ( \hat { \mu } _ { k } \to \hat { \mu } _ { k } ^  ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ) } \cdot \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { \hat { \nu } _ { k } ^ { ( 1 ) } ) } } ) } } \times \hat { \mu } _ { k } ^ { \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( \hat { \nu } _ { k } ^ { ( 1 ) } ) } ) } } ( \mathbf { \theta } _ { d \nu } , \mathbf { 0 } _ { d \nu } ) ( V _  \end{array}
$$

On the other hand, notice that there exists a small enough constant $c$ so that for any $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , c h _ { 1 } )$ and $s \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , c h _ { 2 } )$ , it holds that

$$
\| g _ { [ k ] } ( s ) - X _ { k } \| = \| g _ { [ k ] } ( s ) - g _ { [ k ] } ( \mathbf { 0 } ) \| \leq h _ { 2 } ,
$$

$$
\| G _ { [ k ] } ^ { * } ( z , g _ { [ k ] } ( s ) ) - Y _ { k } \| = \| G _ { [ k ] } ^ { * } ( z , g _ { [ k ] } ( s ) ) - G _ { [ k ] } ^ { * } ( \mathbf { 0 } , g _ { [ k ] } ( \mathbf { 0 } ) ) \| \leq \frac { h _ { 1 } + h _ { 2 } ^ { \beta _ { X } \wedge 1 } } { 2 } \leq h _ { 1 } .
$$

Therefore, we can obtain the following lower bound

$$
\begin{array} { r l } & { \nabla _ { \varphi } \Big [ \underset { \left\{ \vphantom { \frac { 1 } { \{ \sqrt { \varphi } } } \right\} } } { \sum _ { \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi \} } \Big ] } \\ & { = - \underset { \{ \vphantom { \frac { 1 } { \sqrt { \varphi } } \leq \frac { \sqrt { \varphi } } { \sqrt { \varphi } } , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi \} } } { \sum _ { \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi } } \Big ] ^ { \varphi } } \\ &  \qquad - \underset { \{ \vphantom { \frac { 1 } { \sqrt { \varphi } } \leq \frac { \sqrt { \varphi } } { \sqrt { \varphi } } , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi \} } }  \sum _  \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi \varphi , \varphi  \end{array}
$$

The term $\left( E _ { A } \right)$ can be further lower bounded by

$$
\begin{array} { r l } & { E _ { A } \Big ) = \displaystyle \int _ { z \in \mathbb { F } _ { \mathbf { g } _ { \mathbf { g } ^ { d } \mathcal { Y } } } ( 0 , \epsilon , h _ { 1 } ) } \int _ { s \in \mathbb { F } _ { \mathbf { g } _ { \mathbf { g } ^ { d } \mathcal { X } } } ( 0 , \epsilon , h _ { 2 } ) } \Big | \displaystyle \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { L } _ { \mathcal { X } _ { \mathbf { g } ^ { d } \mathcal { X } } } ^ { \mathcal { N } _ { \mathcal { X } } } , \alpha h _ { 1 } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \Big ( \widetilde { G } _ { [ k ] } ( j _ { 1 } , j _ { 2 } ) ( \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Phi } } } } } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf ) - \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { \mathbf { \mathbf { \mathbf { \Phi } } } } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf ( } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf )  \\ &  \mu _ { X } ^ { * } \left( g _ { [ k ] } ( s ) \right) \boldsymbol { \mu } _ { Y [ y _ { [ j _ { 1 } ] } ( s ) } ^ { * } ( \widetilde { G } _ { [ k ] } ( z , s ) ) \sqrt { \operatorname* { d e t } \left( \mathcal { I } _ { ( \mathcal { X } _ { [ j ] } , s ] } ( z ) ^ { T } \mathcal { I } _ { \widetilde { G } _ { [ k ] } ( \cdot , s ) } ( z ) \right) } \sqrt  \end{array}
$$

where the last inequality uses the fact that for any $d$ -variate polynomial $\begin{array} { r } { S ( y ) \ = \ \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } y ^ { j } } \end{array}$ $\boldsymbol { y } \in \mathbb { R } ^ { d }$ , there exists some positive constant $C ( d , k )$ only depending on $( d , k )$ such that

$$
\int _ { \mathbb { B } _ { 1 } ^ { d } } \mathcal { S } ^ { 2 } ( y ) \mathrm { d } y \geq C ( d , k ) \sum _ { j \in \mathbb { N } _ { 0 } ^ { d } , | j | \leq k } a _ { j } ^ { 2 } .
$$

Therefore, combined with Lemma 22, when $\begin{array} { r } { h _ { 1 } = b _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { d _ { Y } + \frac { d _ { X } \beta _ { Y } } { \beta _ { X } } } } } \end{array}$ , $\begin{array} { r } { h _ { 2 } = b _ { 2 } \big ( \frac { \log n } { n } \big ) ^ { \frac { 1 } { d _ { X } + \frac { d _ { Y } \beta _ { X } } { \beta _ { Y } } } } } \end{array}$ with sufficiently large $b _ { 1 } , b _ { 2 }$ , we can obtain that

$$
\sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , d _ { X } } ^ { \vartheta _ { Y } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \Big \| \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) \Big \| h _ { 1 } ^ { j _ { 1 } } h _ { 2 } ^ { j _ { 2 } } \lesssim ( \frac { \log n } { n } ) ^ { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } .
$$

In order to show $\widehat { \mathcal { M } } _ { Y | x }$ satisfies the desired result, we will also use the following lemma, whose proof is provided in Appendix E.11.2.

Lemma 23. It holds with probability at least $1 - n ^ { - 1 }$ that for any $( x , y ) \in { \mathcal { M } }$ , there exists $i \in [ n ]$ so that $\| y - Y _ { i } \| < h _ { 1 }$ and $\| x - X _ { i } \| < h _ { 2 }$ .

Using Lemma 23 and inequality (56), for any $x \in \mathcal { M } _ { X }$ and $y \in \mathcal { M } _ { Y | x }$ , there exists $k \in [ n ]$ so that $\| y - Y _ { k } \| \leq h _ { 1 }$ , $\| x - X _ { k } \| \leq h _ { 2 }$ , and

$$
\begin{array} { r l } & { y = \Phi _ { ( X _ { k } , Y _ { k } ) } ( V _ { k } ^ { * } V _ { k } ^ { * T } ( y - Y _ { k } ) , x ) = G _ { [ k ] } ^ { * } ( V _ { k } ^ { * T } ( y - Y _ { k } ) , x ) = \bar { G } _ { [ k ] } ( V _ { k } ^ { * T } ( y - Y _ { k } ) , W _ { k } ^ { * T } ( x - X _ { k } ) } \\ & { = \underset { ( \bar { I } _ { k } , \bar { J } _ { 2 } ) \subset \mathcal { L } _ { \bar { N } _ { k } , \bar { N } _ { k } } ^ { \bar { J } _ { 1 } , \bar { J } _ { 1 } } } { \sum } \frac { 1 } { j ! j _ { 2 } ! } \bar { G } _ { [ k ] } ( j _ { 1 } , j _ { 2 } ) ( \mathbf { 0 } _ { d _ { X } } , \mathbf { 0 } _ { d _ { X } } ) ( V _ { k } ^ { * T } ( y - Y _ { k } ) ) ^ { j _ { 1 } } ( W _ { k } ^ { * T } ( x - X _ { k } ) ) ^ { j _ { 2 } } + \mathcal { O } ( h _ { 1 } ^ { \beta _ { X } } + h _ { 2 } ^ { \prime } } \\ & { = \underset { ( \bar { I } _ { k } , \bar { J } _ { 2 } ) \subset \mathcal { L } _ { \bar { N } _ { k } , \bar { N } _ { k } } ^ { \bar { J } _ { 1 } , \bar { J } _ { 1 } } } { \sum } \frac { 1 } { j ! j _ { 2 } ! } \tilde { G } _ { [ k ] } ^ { j _ { 1 } , j _ { 2 } } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) ( V _ { k } ^ { * T } ( y - Y _ { k } ) ) ^ { j _ { 1 } } ( W _ { k } ^ { * T } ( x - X _ { k } ) ) ^ { j _ { 2 } } + \mathcal { O } ( h _ { 1 } ^ { \beta _ { X } } + h _ { 2 } ^ { \beta _ { X } } } \\ &  \quad - \hat { f } _   \end{array}
$$

Moreover, we have $\begin{array} { r } { \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { Y } , \beta _ { X } } ^ { d _ { Y } , d _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \widehat { a } _ { j _ { 1 } j _ { 2 } k } ( \widehat { V } _ { k } ^ { T } ( y - Y _ { k } ) ) ^ { j _ { 1 } } ( x - X _ { k } ) ^ { j _ { 2 } } \in \widehat { \mathcal { M } } _ { Y | x } . } \end{array}$

$$
\operatorname* { s u p } _ { y \in \mathcal { M } _ { Y | x } y ^ { \prime } \in \widehat { \mathcal { M } } _ { Y | x } } \| y - y ^ { \prime } \| \lesssim ( \frac { \log n } { n } ) ^ { \frac { 1 } { \frac { d _ { Y } } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } } .
$$

On the other side, for a fixed $x \in \mathcal { M } _ { X }$ , consider any $k \in [ n ]$ with $\| X _ { k } - x \| \leq h _ { 2 }$ and $z \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } )$ . Then

$$
\begin{array} { r l } & { \underset { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { 1 } , \gamma , \mathscr { A } } ^ { \sigma } } { \sum } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \hat { a } _ { j _ { 1 } j _ { 2 } ! k ^ { \sigma } } j ^ { - 1 } ( x - X _ { k } ) ^ { j _ { 2 } } = \hat { f } _ { [ k ] } ( z , g _ { [ k ] } ( W _ { k } ^ { * T } ( x - X _ { k } ) ) ) } \\ & { = \underset { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { 1 } , \gamma , \mathscr { A } } ^ { \sigma } } { \sum } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \hat { F } _ { [ k ] } ( j _ { 1 } , j _ { 2 } ) ( \mathbf { 0 } _ { d _ { 1 } \gamma } , \mathbf { 0 } _ { d _ { \chi } } ) z ^ { j _ { 1 } } ( W _ { k } ^ { * T } ( x - X _ { k } ) ) ^ { j _ { 2 } } + \mathcal { O } \big ( h _ { 1 } ^ { \beta _ { X } } + h _ { 2 } ^ { \beta _ { Y } } \big ) } \\ & { \overset { ( ) } { = } \underset { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { 1 } , \gamma , \mathscr { A } } ^ { \sigma } } { \sum } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \hat { G } _ { [ k ] } ( j _ { 1 } , j _ { 2 } ) ( \mathbf { 0 } _ { d _ { 1 } \gamma } , \mathbf { 0 } _ { d _ { \chi } } ) z ^ { j _ { 1 } } ( W _ { k } ^ { * T } ( x - X _ { k } ) ) ^ { j _ { 2 } } + \mathcal { O } \big ( h _ { 1 } ^ { \beta _ { X } } + h _ { 2 } ^ { \beta _ { Y } } \big ) } \\ &  = \underset  ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \beta _ { 1 } , \gamma , \mathscr { A } } ^  \end{array}
$$

Then since $G _ { [ k ] } ^ { * } ( z , x ) \in \mathcal { M } _ { Y | x }$ , we have

$$
\operatorname* { s u p } _ { y ^ { \prime } \in \widehat { \mathcal { M } } _ { Y } | x } \operatorname* { i n f } _ { y \in \mathcal { M } _ { Y } | x } \| y - y ^ { \prime } \| \lesssim ( \frac { \log n } { n } ) ^ { \frac { 1 } { \beta _ { Y } } + \frac { d _ { X } } { \beta _ { X } } } .
$$

Therefore, it holds with probability at least $1 - 2 n ^ { - 1 }$ that

$$
\operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \mathbb { H } ( \widehat { \mathcal { M } } _ { Y | x } , \mathcal { M } _ { Y | x } ) \lesssim ( \frac { \log n } { n } ) ^ { \frac { 1 } { \frac { d _ { X } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } } ,
$$

which can lead to

$$
\mathbb { E } _ { \mu ^ { * } } , \otimes n \big [ \operatorname* { s u p } _ { x \in \mathcal { M } _ { X } } \mathbb { H } ( \widehat { \mathcal { M } } _ { Y | x } , \mathcal { M } _ { Y | x } ) \big ] \lesssim ( \frac { \log n } { n } ) ^ { \frac { d _ { X } } { \beta _ { X } } + \frac { d _ { Y } } { \beta _ { Y } } } .
$$

# E.11.1 Proof of Lemma 22

The proof directly follows Tang and Yang [2023a], we include it here for completeness. Since there exists a constant $C _ { 0 }$ so that $\| \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) \| _ { 2 } \le C _ { 0 }$ holds for any possible $k , j _ { 1 } , j _ { 2 }$ . For any fixed $k \in [ n ]$ and $\widetilde { \delta } > 0$ , let

$$
\begin{array} { r l } & { \bar { \mathcal { T } } ( \widetilde \delta ) = \Big \{ T = \{ { T _ { j _ { 1 } , j _ { 2 } } } \} _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } \in \left[ - C _ { 0 } , C _ { 0 } \right] ^ { D \times | \mathcal { I } _ { d _ { Y } , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } | } : } \\ & { \qquad \displaystyle \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , \beta _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big \| { T _ { j _ { 1 } , j _ { 2 } } } - \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) \big \| _ { 2 } h _ { 1 } ^ { | j _ { 1 } | } h _ { 2 } ^ { | j _ { 2 } | } \leq \widetilde \delta \Big \} . } \end{array}
$$

We also define the following supreme of an empirical process indexed by $T \in { \bar { \mathcal { T } } } ( { \widetilde { \delta } } )$ ,

$$
\begin{array} { l } { { \displaystyle Z _ { n } ( \hat { \delta } ) = } } \\ { { \displaystyle \sum _ { c \mathcal { T } ( \hat { \delta } ) \atop c \mathcal { T } ( \hat { \delta } ) \atop c \mathcal { T } ( \hat { \delta } ) } \bigg [ \Big | \sum _ { \{ \hat { \sigma } _ { 1 } , \hat { \sigma } \} \subset \mathcal { X } _ { \hat { \sigma } _ { 1 } ^ { \mathcal { N } , \hat { \nu } _ { X } } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \tilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d \chi _ { \tau } } , \mathbf { 0 } _ { d \chi _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \big ) \big ( V _ { k } ^ { \star T } ( Y - Y _ { k } ) \big ) ^ { j _ { 1 } } \big ( W _ { k } ^ { \star T } ( X - X _ { k } ) } } \\ { { \mathrm { 1 } \big ) } } \\ { { \mathrm { 1 } \big ( Y \in \mathbb { B } _ { \mathbb { B } ^ { \mathcal { N } } \mathcal { X } } ( Y _ { k } , h _ { 1 } ) \big ) { \mathrm { 1 } \big ( X \in \mathbb { B } _ { \mathcal { R } ^ { \mathcal { N } , \chi } } ( X _ { k } , h _ { 2 } ) \big ) } \bigg ] } } \\   \displaystyle - n ^ { - 1 } \sum _ { \tau _ { k } \mid \tau _ { k } } \Big [ \Big | \Big | \sum _ { \{ j _ { 1 } , j _ { 2 } \} \in \mathcal { X } _ { \hat { \sigma } _ { 1 } ^ { \mathcal { N } , \hat { \nu } _ { X } } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \tilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d \gamma } , \mathbf { 0 } _ { d \chi } ) - T _ { j _ { 1 } , j _ { 2 } } \big ) \big ( V _ { k } ^ { \star T } ( Y _ { i } - Y _ { k } ) \big \end{array}
$$

and $R _ { n } ( { \widetilde \delta } ) = \mathbb { E } _ { \mu ^ { * } \otimes n } \left[ Z _ { n } ( { \widetilde \delta } ) \right]$ . We will first prove a concentration inequality for a fixed radius $\widetilde { \delta } > 0$ , and then using the peeling technique to allow the radius to be random, which leads to the desired result.

To apply the Talagrand concentration inequality (see, for example, Theorem 3.27 of Wainwright [2019]) for bounding the difference $| Z _ { n } ( \tilde { \delta } ) - \mathop { \mathbf { \hat { R } } _ { n } } ( \tilde { \delta } ) |$ for a fixed $\widetilde { \delta } \dot { } > 0$ , we notice that each additive component in the second empirical sum above has second moment uniformly bounded by

$$
\begin{array} { r l } & { \displaystyle \sum _ { i \neq j \neq i } [ \displaystyle \operatorname* { s u p } _ { \{ i , j \} \neq j \neq i } ( | \sum _ { \{ i , j \} \neq j \neq i } \sum _ { j \neq j \neq i } \frac { 1 } { j ! j \neq j } ( \widetilde { G } _ { \{ i \} } ^ { ( j , j , j ) , 2 } ( \mathbf { 0 } _ { d _ { x } } , \mathbf { 0 } _ { d _ { x } } ) - T _ { j \neq j } ) ( V _ { k } ^ { - T } ( Y - Y _ { k } ) ) ^ { j \ast } ( W _ { k } ^ { + T } ( X - X } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad \quad \quad \quad  \quad \quad \quad \quad \quad \quad  \quad \quad \quad \quad \quad  \\ & { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad \quad  \quad \quad \quad \quad \quad \quad  \\ & { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \quad \quad \quad \quad \quad \quad \quad \quad  \\ & { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ &  \displaystyle \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \ \end{array}
$$

Moreover, each additive component can be almost surely bounded by

$$
\begin{array} { r l } & { \underset { z \in \mathbb { B } _ { \mathbb { R } ^ { d } \gamma } ( \mathbf { 0 } , h _ { 1 } ) , s \in \mathbb { B } _ { \mathbb { R } ^ { d } X } ( \mathbf { 0 } , h _ { 2 } ) } { \operatorname* { s u p } } \Big \| \underset { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { T } _ { d \gamma , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } { \sum } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \big ) z ^ { j _ { 1 } } s ^ { j _ { 2 } } \Big \| _ { 2 } ^ { 2 } } \\ & { \leq C \underset { { T \in \mathcal { T } ( \widetilde { \delta } ) } } { \operatorname* { s u p } } \Bigg ( \underset { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { T } _ { d \gamma , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } { \sum } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \| \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \| h _ { 1 } ^ { | j _ { 1 } | } h _ { 2 } ^ { | j _ { 2 } | } \Bigg ) ^ { 2 } \leq C \widetilde { \delta } ^ { 2 } . } \end{array}
$$

Based on these two bounds, we can apply the Talagrand concentration inequality to obtain that for any $s \geq 0$ ,

$$
\mathbb { P } \big ( Z _ { n } ( \widetilde { \delta } ) \geq R _ { n } ( \widetilde { \delta } ) + s ^ { 2 } \big ) \leq 2 \exp \left( - \frac { c n s ^ { 4 } } { s ^ { 2 } \widetilde { \delta } ^ { 2 } + \widetilde { \delta } ^ { 4 } h _ { 1 } ^ { d _ { Y } } h _ { 2 } ^ { d _ { X } } } \right) .
$$

It remains to bound the expectation $R _ { n } ( { \widetilde { \delta } } )$ via the symmetrization technique and chaining. By a standard symmetrization, we can get

$$
\begin{array} { r l } & { \mathfrak { L } _ { n } ( \widetilde { \delta } ) \le \displaystyle \frac { 2 } { \sqrt { n } } \mathbb { E } \Bigg [ \displaystyle \operatorname* { s u p } _ { T \in \mathcal { T } ( \widetilde { \delta } ) } } \\ & { \frac { 1 } { \sqrt { n } } \displaystyle \sum _ { i \in [ n ] } \varepsilon _ { i } \Big [ \Big \| \displaystyle \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , \mathscr { B } _ { X } } ^ { \beta _ { Y } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \big ) \big ( V _ { k } ^ { * T } ( Y _ { i } - Y _ { k } ) \big ) ^ { j _ { 1 } } \big ( W _ { k } ^ { * T } ( X _ { i } - X _ { k } ) \big ) \Big ] } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { 1 } \big ( Y _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } \big ( Y _ { k } , h _ { 1 } ) \big ) \mathbf { 1 } \big ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } \big ( X _ { k } , h _ { 2 } ) \big ) \bigg ] \Bigg | \Bigg ] , } \end{array}
$$

where $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ are $n$ i.i.d. copies from the Rademacher distribution, i.e. $\mathbb { P } ( \varepsilon _ { i } = 1 ) = \mathbb { P } ( \varepsilon _ { i } = - 1 ) = 0 . 5$ . Since given $\{ X _ { i } , Y _ { i } \} _ { i \in [ n ] , i \neq k }$ , the stochastic process inside the supreme is a sub-Gaussian process with

intrinsic metric

$$
\begin{array} { r l } & { \displaystyle \boldsymbol { d } _ { n } ^ { 2 } ( T , \widetilde { T } ) } \\ & { = \frac { 1 } { n } \sum _ { i \in [ n ] } \bigg ( \prod _ { \scriptstyle ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \boldsymbol { q } _ { \gamma } , \mathscr { D } _ { X } } ^ { \delta _ { \gamma } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { \boldsymbol { d } _ { \gamma } } , \mathbf { 0 } _ { \boldsymbol { d } _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \big ) ( V _ { k } ^ { * T } ( Y _ { i } - Y _ { k } ) \big ) ^ { j _ { 1 } } ( V _ { k } ^ { * T } ( X _ { i } - X _ { i } ) } \\ & { \quad \quad \quad - \Big | \prod _ { \scriptstyle ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \boldsymbol { q } _ { \gamma } , \mathscr { D } _ { X } } ^ { \delta _ { \gamma } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { \boldsymbol { d } _ { Y } } , \mathbf { 0 } _ { \boldsymbol { d } _ { X } } ) - \widetilde { T } _ { j _ { 1 } , j _ { 2 } } \big ) ( V _ { k } ^ { * T } ( Y _ { i } - Y _ { k } ) \big ) ^ { j _ { 1 } } ( V _ { k } ^ { * T } ( X _ { i } - X _ { i } ) } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad } \\ & &  \leq C \widetilde { \delta } ^ { 4 } \frac { 1 } { n } \sum _ { i \in [ n ] } \mathbf { 1 } _  ( Y _ { i } \in \mathbb { B } _ { \mathbb { B } ^ { D } \gamma } ( Y _  \end{array}
$$

for any $T , \widetilde { T } \in \bar { \mathcal { T } } ( \widetilde { \delta } )$ , where the last step uses the definition of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ . So we have

$$
\left[ \operatorname* { s u p } _ { T , \tilde { T } \in \mathcal { T } ( \delta ) } d _ { n } ^ { 2 } ( T , \widetilde { T } ) \right] \leq C \widetilde { \delta } ^ { 4 } \cdot h _ { 1 } ^ { d _ { Y } } h _ { 2 } ^ { d _ { X } } \quad \mathrm { a n d } \quad d _ { n } ( T , \widetilde { T } ) \leq C \widetilde { \delta } \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \| T _ { ( j _ { 1 } , j _ { 2 } ) } - \widetilde { T } _ { ( j _ { 1 } , j _ { 2 } ) } .
$$

Lastly, let ${ \displaystyle \mathcal { K } _ { n } ( \delta ) = \operatorname* { s u p } _ { T , \widetilde { T } \in \bar { T } ( \delta ) } d _ { n } ( T , \widetilde { T } ) }$ , by applying the standard chaining via Dudley’s inequality, we can get

$$
\begin{array} { r l } & { { \cal R } _ { n } ( { \tilde { \delta } } ) \leq C \frac { 1 } { \sqrt n } \mathbb { E } _ { \mu ^ { * } } \Big [ \int _ { 0 } ^ { { \boldsymbol { K } } _ { n } ( { \tilde { \delta } } ) } \sqrt { \log \frac { C _ { 1 } \tilde { \delta } } { u } } \mathrm { d } u \Big ] } \\ & { \qquad = C \frac { 1 } { \sqrt n } \mathbb { E } _ { \mu ^ { * } } \Big [ K _ { n } ( { \tilde { \delta } } ) \cdot \int _ { 0 } ^ { 1 } \sqrt { \log \frac { C _ { 1 } \tilde { \delta } } { u _ { n } \cdot K _ { n } ( { \tilde { \delta } } ) } } \mathrm { d } u \Big ] } \\ & { \qquad = C \frac { 1 } { \sqrt n } \mathbb { E } _ { \mu ^ { * } } \Big [ K _ { n } ( { \tilde { \delta } } ) \cdot 1 ( \mathcal { K } _ { n } ( { \tilde { \delta } } ) \leq { \tilde { \delta } } ^ { 2 } ) _ { 1 } ^ { k ( \tilde { \delta } ^ { * } ) / 2 } h _ { 2 } ^ { d _ { 2 } / 2 } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { C _ { 1 } \tilde { \delta } } { u \cdot K _ { n } ( { \tilde { \delta } } ) } } \mathrm { d } u \Big ] } \\ & { \qquad + C \frac { 1 } { \sqrt n } \mathbb { E } _ { \mu ^ { * } } \Big [ K _ { n } ( { \tilde { \delta } } ) \cdot 1 ( K _ { n } ( { \tilde { \delta } } ) > { \tilde { \delta } } ^ { 2 } { h _ { 1 } ^ { d _ { 1 } / 2 } } ) h _ { 2 } ^ { d _ { 2 } / 2 } ) \int _ { 0 } ^ { 1 } \sqrt { \log \frac { C _ { 1 } \tilde { \delta } } { u \cdot K _ { n } ( { \tilde { \delta } } ) } } \mathrm { d } u \Big ] } \\ &  \qquad \leq C _ { 1 } \ h _ { 1 } ^ { \mathcal { S } } \ h _ { 2 } ^ { \mathcal { S } } \cdot \sqrt  \frac  - \log ( \tilde { \delta } / h _ \end{array}
$$

where we have used the fact that the $u$ -covering entropy of $\bar { \mathcal { T } } ( \widetilde { \delta } )$ relative to metric $d _ { n }$ is at most $\begin{array} { r } { C _ { 2 } \log \frac { C _ { 1 } \widetilde \delta } { u } } \end{array}$ for $u \in ( 0 , C _ { 1 } \widetilde { \delta } )$ . By combining this with inequality (57), we obtain that for all $t \geq 1$ ,

$$
\mathbb { P } \Big ( Z _ { n } ( \widetilde { \delta } ) \geq C t ^ { 2 } h _ { 1 } ^ { \frac { d _ { Y } } { 2 } } h _ { 2 } ^ { \frac { d _ { X } } { 2 } } \cdot \sqrt { \frac { - \log ( \widetilde { \delta } h _ { 1 } h _ { 2 } ) } { n } } \widetilde { \delta } ^ { 2 } \Big ) \leq 2 \exp \Big ( - c t ^ { 2 } \log ( n / \widetilde { \delta } ) \Big ) .
$$

Finally, we apply the peeling technique to extend the above high probability bound on $Z _ { n } ( { \widetilde { \delta } } )$ to the random radius δe = P(j1,j2)∈J βY ,βXdY ,DX j $\begin{array} { r } { \widetilde { \delta } = \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , D _ { X } } ^ { \beta _ { Y } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \| \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - T _ { j _ { 1 } , j _ { 2 } } \| h _ { 1 } ^ { | j _ { 1 } | } \dot { h } _ { 2 } ^ { | j _ { 2 } | } } \end{array}$ . Specifically, we first

set the basic level $\bar { \delta } = h _ { 1 } ^ { \beta _ { Y } } + h _ { 2 } ^ { \beta _ { X } }$ , and for $s = 1 , \cdots , S$ with $\begin{array} { r } { S \le \log \frac { C } { \bar { \delta } } } \end{array}$ , define sets

$$
\begin{array} { r l } & { \widetilde { T } _ { 0 } = \Big \{ T = \{ T ( { _ { j 1 } , j _ { 2 } } ) \} _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { \partial _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } } \in [ - C _ { 0 } ( \log n ) ^ { 2 } , ~ C _ { 0 } ( \log n ) ^ { 2 } ] ^ { D \times | \mathcal { I } _ { d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } | } \ ; } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \frac { 1 } { j _ { 1 } ! } | { _ { 2 j _ { 1 } } } | | T _ { j _ { 1 } , j _ { 2 } } - \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) | | _ { 2 } h _ { 1 } ^ { | j _ { 1 } | _ { 1 } } h _ { 2 } ^ { | j _ { 2 } | } \leq \bar { \delta } \Big \} ; } \\ & { \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \widetilde { T } _ { s } = \Big \{ T - \{ T ( { _ { j 1 } , j _ { 2 } } ) \} _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } } \in [ - C _ { 0 } ( \log n ) ^ { 2 } , ~ C _ { 0 } ( \log n ) ^ { 2 } ] ^ { D \times | \mathcal { I } _ { d _ { Y } } ^ { \beta _ { Y } , \beta _ { X } } | } \ ; } \\ &  \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad 2 ^ { s - 1 } \bar { \delta } \leq \underset  ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { d _ { Y } , D _ { X } } ^  \beta _ { Y } , \beta _ { X } \end{array}
$$

By applying inequality (59) to $\widetilde { \delta } = 2 ^ { s } \overline { { \delta } }$ for $s \in [ S ]$ with sufficiently large constant $t > 0$ , we obtain that

$$
\mathbb { P } \left( Z _ { n } ( \bar { \delta } ) \geq C h _ { 1 } ^ { \frac { d _ { Y } } { 2 } } h _ { 1 } ^ { \frac { d _ { X } } { 2 } } \sqrt { \frac { \log n } { n } } \bar { \delta } ^ { 2 } \right) + \sum _ { s = 1 } ^ { S } \mathbb { P } \left( Z _ { n } ( 2 ^ { s } \bar { \delta } ) \geq C h _ { 1 } ^ { \frac { d _ { Y } } { 2 } } h _ { 1 } ^ { \frac { d _ { X } } { 2 } } \sqrt { \frac { \log n } { n } } 4 ^ { s } \bar { \delta } ^ { 2 } \right) \leq n ^ { - ( c + 1 ) } \exp \left( \frac { 2 \pi \kappa } { \varepsilon } \frac { 1 } { n } \right)
$$

$T \in \widetilde { \mathcal { T } } _ { s }$ $s \in \{ 0 \} \cup [ S ]$ $Z _ { n } ( 2 ^ { s } { \bar { \delta } } ) \leq C b _ { 2 } ^ { \frac { d } { 2 } } { \frac { \log n } { n } } 4 ^ { s } { \bar { \delta } } ^ { 2 }$ implies

$$
\begin{array} { r l } & { \underset { \{ \bar { \theta } ^ { * } \} } { \operatorname* { l i m } } [ \| \underset { \bar { \theta } \leq t } { \sum }  \underset { \bar { \theta } \leq t \leq t } { \sum } \underset { j \in \mathcal { K } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } } _ { \bar { \theta } _ { \bar { \theta } } _ { \bar { \theta } _ { \bar { \theta } } _ { \bar { \theta } } _ { \bar { \theta } } } } } } } } } \frac { 1 } { j ! j ! } ( \bar { G } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } } } } } ^ { j ( 1 , j ) ; j } ( \mathbf { 0 } _ { 4 \nu _ { \bar { \theta } } } , \mathbf { 0 } _ { 4 \kappa } ) - T _ { j _ { \bar { \theta } _ { \bar { \theta } } } , \bar { \theta } } ) ( V _ { k } ^ { T } ( Y - Y _ { k } ) ) ^ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } } } } ( W _ { k } ^ { T } ( X - X _ { k } ) )    } \\ & {    \mathrm { ~ \operatorname { l i f } ~ } \bar { \theta } \leq \frac { \kappa } { 2 } \kappa \underset { j \leq t \leq j } { \sum } \mathrm { ~ \operatorname { l i m } }  \mathrm { ~ V a r } \underset { \{ \bar { \theta } \leq t \leq j _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } } } } } } } { \sum } \frac { 1 } { j ! j ! } ( \bar { G } _ { \bar { \theta } \leq t } ^ { j _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } _ { \bar { \theta } } } } } } ( X _ { k } , b _ { 2 } ) )     \\ &  - \underset    \frac { \kappa ^ { 2 } } { 2 } \kappa \underset  j \leq t  \end{array}
$$

Furthermore,

$$
\begin{array} { r l } &  \mathrm { ~ \displaystyle \sum _ { i \ne [ n ] } ^ { - 1 } \sum _ { \ d ( j _ { \bar { i } } \nearrow n ) \atop i \ne j _ { k } } \left[ \left\| \sum _ { \ d ( j _ { 1 } , j _ { 2 } ) \in \mathcal { I } _ { q _ { \gamma } , D _ { X } } ^ { \rho } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \left( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - \widetilde f _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) \right) ( V _ { k } ^ { * T } ( Y _ { i } - Y _ { k } ) ) ^ { j _ { 1 } } ( W _ { k } ^ { * } \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) \right) \right] } \\ &  \mathrm { ~ \displaystyle \sum _ { i \ne j _ { k } } ^ { - 1 } \widetilde { \mathbb { E } } _ { \mathbb { R } ^ { D } Y } ( Y _ { k } , h _ { 1 } ) \mathbb { 1 } ( X _ { i } \in \mathbb { B } _ { \mathbb { R } ^ { D } X } ( X _ { k } , h _ { 2 } ) ) } \\ & { \le ( h _ { 1 } ^ { 2 \beta _ { Y } } + h _ { 2 } ^ { 2 \beta _ { X } } ) \cdot \frac { 1 } { n } \sum _ { \ d ( i \ne [ n ] } ^ { \infty } \mathbf { 1 } ( Z _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) . } \\ &  \mathrm  ~ \displaystyle \sum _ { i \ne j _ { k } } \widetilde { \mathbb { E } } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { \widetilde { \Phi } } \end{array}
$$

Then since

E $\begin{array} { r } { \vert \vert ( \boldsymbol { \mathcal { Z } } _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) ) ^ { 2 } \vert = \mathbb { P } _ { \mu ^ { * } } \big ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( Y _ { k } , h _ { 1 } ) , X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( X _ { k } , h _ { 1 } ) \big ) \vert \sqrt { \mu } , } \end{array}$ h2) ≤ C hdY1 hdX2 .

By Bernstein’s inequality, it holds with probability at least $1 - n ^ { - c - 1 }$ that

$$
\begin{array} { r l } & { \displaystyle \frac { 1 } { n } \sum _ { i \in [ n ] } \mathbf { 1 } ( Z _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) } \\ & { \displaystyle \overset { ( ) } { \le \frac { 1 } { n - 1 } } \sum _ { i \in [ n ] } \mathbf { 1 } ( Z _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) } \\ &  \displaystyle \qquad \overset { ( ) } { \le \left| \frac { 1 } { n - 1 } \sum _ { i = 1 } ^ { n } \mathbf { 1 } ( Z _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) - \mathbb { P } _ { \mu ^ { * } } \bigl ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( Y _ { k } , h _ { 1 } ) , X \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 2 } ) \bigr ) \right. } \\ & { \displaystyle \qquad + \mathbb { P } _ { \mu ^ { * } } \bigl ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( Y _ { k } , h _ { 1 } ) , X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( X _ { k } , h _ { 2 } ) \bigr ) . } \end{array}
$$

Then using the fact that $\mathcal { M } _ { X }$ and $\mathcal { M } _ { Y | X }$ are smooth submaifolds with reach bounded away from zero, and $f _ { X } , f _ { Y \mid X }$ are uniformly lower bounded by a constant, using Lemma B.7 of Aamari and Levrard [2019], we can get

$$
\frac { 1 } { n } \sum _ { i \in [ n ] \atop i \neq k } \mathbf { 1 } ( Z _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { Y } } } ( \mathbf { 0 } , h _ { 1 } ) ) \mathbf { 1 } ( S _ { i k } \in \mathbb { B } _ { \mathbb { R } ^ { d _ { X } } } ( \mathbf { 0 } , h _ { 2 } ) ) \lesssim \frac { \log n } { n } + h _ { 1 } ^ { d _ { Y } } h _ { 2 } ^ { d _ { X } } .
$$

So by combining all pieces, we can get that it holds with probability at least $1 - n ^ { - c - 1 }$ that

$$
\begin{array} { r l } & { \displaystyle \mu ^ { * } \bigg [ \bigg \| \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { J } _ { d _ { \mathcal { Y } } , D _ { X } } ^ { \beta _ { \mathcal { Y } } , \beta _ { X } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big ( \widetilde { G } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { \mathcal { Y } } } , \mathbf { 0 } _ { d _ { X } } ) - \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { \mathcal { Y } } } , \mathbf { 0 } _ { d _ { X } } ) \big ) \big ( V _ { k } ^ { * T } ( Y - Y _ { k } ) \big ) ^ { j _ { 1 } } \big ( W _ { k } ^ { * T } ( X - Y _ { k } ) \big ) ^ { j _ { 1 } } \big ( W _ { k } ^ { * T } ( X - Y _ { k } ) \big ) } \\ & { \displaystyle \mathbf { 1 } \big ( Y \in \mathbb { B } _ { \mathbb { R } ^ { D _ { Y } } } ( Y _ { k } , h _ { 1 } ) \big ) \mathbf { 1 } \big ( X \in \mathbb { B } _ { \mathbb { R } ^ { D _ { X } } } ( X _ { k } , h _ { 2 } ) \big ) \bigg ] } \\ &  \displaystyle \vdots \mathbb { h } _ { 1 } ^ { \frac { d _ { \mathcal { Y } } } { 2 } } h _ { 1 } ^ { \frac { d _ { X } } { 2 } } \sqrt { \frac { \log n } { n } } \bigg ( \sum _ { ( j _ { 1 } , j _ { 2 } ) \in \mathcal { J } _ { d _ { Y } } ^ { { \beta _ { Y } , \beta _ { X } } } } \frac { 1 } { j _ { 1 } ! j _ { 2 } ! } \big | \big | \widetilde { f } _ { [ k ] } ^ { ( j _ { 1 } , j _ { 2 } ) } ( \mathbf { 0 } _ { d _ { Y } } , \mathbf { 0 } _ { d _ { X } } ) - \widetilde { G } _ { [ k ] } ^  ( j _ { 1 } , \end{array}
$$

Then the claimed result is a consequence of a simple union bound over $k \in [ n ]$ .

# E.11.2 Proof of Lemma 23

$\begin{array} { r } { h _ { 1 } = b _ { 1 } \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { d _ { Y } + \frac { d _ { X } \beta _ { Y } } { \beta _ { X } } } } } \end{array}$ $\begin{array} { r } { h _ { 2 } = b _ { 2 } \left( \frac { \log n } { n } \right) ^ { \frac { 1 } { d _ { X } + \frac { d _ { Y } \beta _ { X } } { \beta _ { Y } } } } } \end{array}$ , since $\beta _ { Y } \geq \beta _ { X }$ and $\beta _ { Y } \geq 2$ , we have $\begin{array} { r } { h _ { 2 } ^ { 1 \wedge \beta _ { X } } \leq \frac { b _ { 2 } } { b _ { 1 } } h _ { 1 } } \end{array}$ . Then when $\frac { b _ { 2 } } { b _ { 1 } }$ is small enough, it holds for some positive constants $C , C _ { 1 }$ that,

$$
\begin{array} { r l } { \forall ( x ^ { * } , y ^ { * } ) \in \mathcal { M } , \quad } & { \mathbb { P } _ { \mu ^ { * } } ( \| y - y ^ { * } \| < h _ { 1 } / 2 , \| x - x ^ { * } \| < h _ { 2 } / 2 ) } \\ & { \ge \mathbb { P } _ { \mu _ { x } ^ { * } } ( \| x - x ^ { * } \| < h _ { 2 } / 2 ) \cdot \underset { x \in \mathbb { B } _ { M _ { X } } ( x ^ { * } , h _ { 2 } / 2 ) } { \operatorname* { i n f } } \mathbb { P } _ { \mu _ { Y | x } ^ { * } } ( \| y - y ^ { * } \| < h _ { 1 } / 2 ) } \\ & { \overset { ( i ) } { \ge } C h _ { 2 } ^ { d _ { X } } \cdot \underset { x \in \mathbb { B } _ { M _ { X } } ( x ^ { * } , h _ { 2 } / 4 ) } { \operatorname* { i n f } } \mathbb { P } _ { \mu _ { Y | x } ^ { * } } ( \| y - \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ) \| < \frac { h _ { 1 } } { 4 } ) } \\ & { \ge C _ { 1 } h _ { 2 } ^ { d _ { X } } h _ { 1 } ^ { d _ { Y } } , } \end{array}
$$

where $( i )$ uses the fact that $\mathbb { P } _ { \mu _ { X } ^ { * } } ( \| x - x ^ { * } \| < h _ { 2 } / 2 ) \gtrsim h _ { 2 } ^ { d _ { X } }$ and $\| y ^ { * } - \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ) \| = \| \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ^ { * } ) -$ $\begin{array} { r } { \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ) \rVert \le L \left. x ^ { * } - x \right. ^ { \beta _ { X } \wedge 1 } < \frac { h _ { 1 } } { 4 } } \end{array}$ when t for an $\frac { b _ { 2 } } { b _ { 1 } }$ fficiently small. Furthermore, b, it holds with probability at least $C _ { 2 }$ $t > 0$ $1 - \exp ( - t )$

that

$$
\begin{array} { l } { \displaystyle \frac 1 n \sum _ { i = 1 } ^ { n } \mathbf { 1 } ( \| Y _ { i } - y _ { 0 } \| < h _ { 1 } / 2 , \| X _ { i } - x _ { 0 } \| < h _ { 2 } / 2 ) - { \mathbb P } _ { \mu ^ { * } } ( \| y - y _ { 0 } \| < h _ { 1 } / 2 , \| x - x _ { 0 } \| < h _ { 2 } / 2 ) } \\ { \displaystyle \geq - \sqrt \frac \frac t n \sqrt { { \mathbb P } _ { \mu ^ { * } } \Big ( \| Y - y _ { 0 } \| < h _ { 1 } / 2 , \| X - x _ { 0 } \| < h _ { 2 } / 2 \Big ) } - \frac t { 3 n } } \\ { \displaystyle \geq - \frac t { 3 n } - C _ { 2 } \sqrt \frac { t } { n } h _ { 2 } ^ { d _ { X } / 2 } h _ { 1 } ^ { d _ { Y } / 2 } . } \end{array}
$$

Consider ε1 = c1h1 and ε2 = c1h2 with c1 = ( b12b1+2Lb2 ) . Let $N _ { \varepsilon _ { 2 } } ^ { x }$ be the largest $\varepsilon _ { 2 }$ -packing of $\mathcal { M } _ { X }$ , then by Lemma B.7 of Aamari and Levrard [2019], it holds that $| N _ { \varepsilon _ { 2 } } ^ { x } | \lesssim \varepsilon _ { 2 } ^ { - d _ { X } }$ . Moreover, for each $x \in N _ { \varepsilon _ { 2 } } ^ { x }$ , let $N _ { \varepsilon _ { 1 } } ^ { y } ( x )$ be the largest $\varepsilon _ { 1 }$ -packing of $\mathcal { M } _ { Y \mid x }$ , then $| N _ { \varepsilon _ { 1 } } ^ { y } ( x ) | \lesssim \varepsilon _ { 1 } ^ { - d _ { Y } }$ . So for any $( x ^ { * } , y ^ { * } ) \in \mathcal { M } _ { X }$ , there exists $x _ { 0 } \in N _ { \varepsilon _ { 2 } } ^ { x }$ so that $\lVert x ^ { * } - x _ { 0 } \rVert \leq \varepsilon _ { 2 }$ . Moreover, there exists $y _ { 0 } \in N _ { \varepsilon _ { 1 } } ^ { y } ( x _ { 0 } )$ so that $\lVert y _ { 0 } - \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ) \rVert \leq \varepsilon _ { 1 }$ and thus $\begin{array} { r } { \| y _ { 0 } - y ^ { * } \| \leq \varepsilon _ { 1 } + \| \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ) - \Phi _ { ( x ^ { * } , y ^ { * } ) } ( \mathbf { 0 } , x ^ { * } ) \| \leq } \end{array}$ $\varepsilon _ { 1 } + L \varepsilon _ { 2 } ^ { \beta _ { X } \wedge 1 }$ . By a union argumentith probability at least $\{ ( x , y ) : x \in N _ { \varepsilon _ { 2 } } ^ { x } , y \in N _ { \varepsilon _ { 1 } } ^ { y } ( x ) \}$ s a constant , $C _ { 3 }$ so $1 - n ^ { - 1 }$ $x _ { 0 } \in N _ { \varepsilon _ { 2 } } ^ { x }$ $y _ { 0 } \in N _ { \varepsilon _ { 1 } } ^ { y } ( x _ { 0 } )$

$$
\begin{array} { r l } & { \displaystyle \frac 1 n \sum _ { i = 1 } ^ { n } \mathbf { 1 } ( \| Y _ { i } - y _ { 0 } \| < h _ { 1 } / 2 , \| X _ { i } - x _ { 0 } \| < h _ { 2 } / 2 ) } \\ & { = \mathbb { P } _ { p ^ { * } } \big ( \| y - y _ { 0 } \| < h _ { 1 } / 4 , \| x - x _ { 0 } \| < h _ { 2 } / 4 \big ) } \\ & { \displaystyle + \frac 1 n \sum _ { i = 1 } ^ { n } \mathbf { 1 } ( \| Y _ { i } - y _ { 0 } \| < h _ { 1 } / 2 , \| X _ { i } - x _ { 0 } \| < h _ { 2 } / 2 ) - \mathbb { P } _ { \mu ^ { * } } \big ( \| y - y _ { 0 } \| < h _ { 1 } / 2 , \| x - x _ { 0 } \| < h _ { 2 } / 2 \big ) } \\ & { \ge C _ { 1 } h _ { 2 } ^ { d x } h _ { 1 } ^ { d y } - C _ { 3 } \frac { \log n } { 3 n } - C _ { 2 } \sqrt { \frac { C _ { 3 } \log n } { n } } h _ { 2 } ^ { d x / 2 } h _ { 1 } ^ { d y / 2 } . } \end{array}
$$

When $b _ { 1 } , b _ { 2 }$ are sufficiently large, we have $\begin{array} { r } { C _ { 1 } h _ { 2 } ^ { d _ { X } } h _ { 1 } ^ { d _ { Y } } - C _ { 3 } \frac { \log n } { 3 n } - C _ { 2 } \sqrt { \frac { C _ { 3 } \log n } { n } } h _ { 2 } ^ { d _ { X } / 2 } h _ { 1 } ^ { d _ { Y } / 2 } > 0 } \end{array}$ means for any $x _ { 0 } ~ \in ~ N _ { \varepsilon _ { 2 } } ^ { x }$ and $y _ { 0 } \ \in \ N _ { \varepsilon _ { 1 } } ^ { y } ( x _ { 0 } )$ , there exists $i \in [ n ]$ so that $\| Y _ { i } - y _ { 0 } \| < h _ { 1 } / 2$ and $y _ { 0 } \in N _ { \varepsilon _ { 1 } } ^ { y } ( x _ { 0 } )$ $\| X _ { i } - x _ { 0 } \| < h _ { 2 } / 2$ so that . Then, combined with the fact that for any $\begin{array} { r } { \| \boldsymbol { x } ^ { * } - \boldsymbol { x } _ { 0 } \| \le \varepsilon _ { 2 } < \frac { h _ { 2 } } { 2 } } \end{array}$ and $\begin{array} { r } { \| y ^ { * } - y _ { 0 } \| \le \varepsilon _ { 1 } + L \varepsilon _ { 2 } ^ { \beta _ { X } \wedge 1 } \le \frac { h _ { 1 } } { 2 } } \end{array}$ $( x ^ { \ast } , y ^ { \ast } ) \in \mathcal { M }$ h12 , we can get the desired , there exists $x _ { 0 } \in N _ { \varepsilon _ { 2 } } ^ { x }$ and result.