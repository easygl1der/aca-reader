Proceedings of Machine Learning Research vol 134:1–58, 2021

34th Annual Conference on Learning Theory

On Empirical Bayes Variational Autoencoder: An Excess Risk Bound
Rong Tang

## RONGT 3@ ILLINOIS . EDU

University of Illinois at Urbana-Champaign

Yun Yang

## YY 84@ ILLINOIS . EDU

University of Illinois at Urbana-Champaign

Editors: Mikhail Belkin and Samory Kpotufe

# Abstract

Abstract
In this paper, we consider variational autoencoders (VAE) via empirical Bayes estimation, referred
to as Empirical Bayes Variational Autoencoders (EBVAE), which is a general framework including
popular VAE methods as special cases. Despite the widespread use of VAE, its theoretical aspects
are less explored in the literature. Motivated by this, we establish a general theoretical framework for
analyzing the excess risk associated with EBVAE under the setting of density estimation, covering
both parametric and nonparametric cases, through the lens of M-estimation. As an application, we
analyze the excess risk of the commonly-used EBVAE with Gaussian models and highlight the
importance of covariance matrices of Gaussian encoders and decoders in obtaining a good statistical
guarantee, shedding light on the empirical observations reported in the literature.

## 1. Introduction
A wide variety of machine learning problems can be framed as directed probabilistic inference in
generative models (Jebara and Meila, 2006), especially when we care about modeling and efficient
sampling from complex distributions such as those over natural images and text (Yang et al., 2017;
Brock et al., 2018; van den Oord et al., 2016). Variational autoencoder (VAE) (Kingma and Welling,
2013; Rezende et al., 2014) replaces conventional instance-specific local inference with a global
inference network and therefore enables efficient training of deep generative models. In plain
language, a latent variable generative model defines a joint density p(x, z) over the data space X and
the latent space Z by specifying a prior π(z) over latent variables and a conditional density p(x|z)
of data given latent variables. Typically we aim at learning pD (x) over data space, based on a finite
number n of samples {xi }ni=1 , assumed to be drawn from it. In most cases, maximizing the average
marginal log-likelihood of the data is difficult, as the marginal likelihood functions are intractable due
to the integral for marginalizing out latent variables (Kingma and Welling, 2013). VAE overcomes
this issue by introducing a family of inference distributions q(z|x) for approximating the posterior of
latent variables given the data and jointly optimizing the so-called evidence lower bound (ELBO,
Ormerod and Wand, 2010) as in the variational Bayes methods. From a coding theory perspective,
the unobserved latent variables can be interpreted as a latent representation or code (Kingma and
Welling, 2013). Therefore, the inference distribution q(z|x) can be interpreted as a probabilistic
encoder, and the conditional distribution p(x|z) of data given latent variables can be interpreted as a
probabilistic decoder.
VAE has received great success in generating complicated data, including images (Gregor et al.,
2015; Kulkarni et al., 2015), molecules (Segler et al., 2017), text (Yang et al., 2017), and predicting
the future from static images (Walker et al., 2016). However, as empirically observed in Tomczak
and Welling (2017), VAE with a standard multivariate Gaussian prior tends to underfit the data. We
c 2021 R. Tang & Y. Yang.

TANG YANG

thus consider a broader class of VAE via empirical Bayes estimation. Specifically, we incorporate
hyperparameters in the prior over latent variables, and jointly optimize the prior with the encoder and
the decoder. We call this framework Empirical Bayes Variational Autoencoders (EBVAE), which
includes popular VAE variants “VampVAE” (Tomczak and Welling, 2017) and “LARSVAE” (Bauer
and Mnih, 2018) as two representative examples. In the statistical literature, density estimation (Silverman, 1986; Sheather, 2004) has been an important topic in both nonparametric statistics and
parametric statistics, and its hardness in terms of minimax optimal rate of convergence has been
understood fairly well for a wide range of density functions under smoothness constraints (Stone,
1982). Despite the celebrated empirical success, little general theory has been developed to investigate
statistical properties of VAE or more broadly, EBVAE (Doersch, 2016). In this paper, we undertake
this task and focus on the theoretical front to answer: how well can EBVAE learn the target density
pD (x) under different choices of prior families, encoder families, and decoder families.
## 1.1. Related Work
In the original formulation of VAE, the prior is chosen to be the standard multivariate Gaussian
and the encoder is optimized over a Gaussian family (Kingma and Welling, 2013), which may lead
to poor performance when applied to complex datasets because of model misspecification. Many
approaches have been developed to increase the model capacity by either using a more flexible
encoder family (Rezende and Mohamed, 2015; Kingma et al., 2016) or choosing a more expressive
family of the priors (Chen et al., 2016; Guillemin and Pollack, 2010). Tomczak and Welling (2017)
have shown that the prior
Pminimizing the objective function of VAE is given by the corresponding
aggregated posterior n1 ni=1 q(z|xi ) with q(z|x) being the encoder. In view of this fact, some
studies (Tomczak and Welling, 2017; Bauer and Mnih, 2018) considered prior families that aim to
approximate the aggregated posterior, which can be seen as special cases of prior parametrization
within the framework of EBVAE.
On the theoretical side, Liang (2018) studied the rates of convergence for learning generative
models using Generative Adversarial Networks (GAN, Goodfellow et al., 2014). They provided a
comprehensive statistical treatment of GAN in which the generator and discriminator are parametrized
by neural networks. Unlike GAN which aims at achieving an equilibrium between the generator and
the discriminator, EBVAE aims at maximizing a variational lower bound to the data log-likelihood
and possess an encoder-decoder type interpretation. In this work, we develop a general theoretical
framework to characterize the excess risk of EBVAE as a generative model learning approach for
density estimation covering both parametric and nonparametric cases. A most relevant work to ours
is Doersch (2016), where they analyzed the approximation error associated with the population level
objective function of VAE for one-dimensional data when Gaussian encoders and decoders are used,
they found that the approximation error will go to zero if the standard deviation (noise level) of the
data given latent variables vanishes, given that the approximation families of mean functions and
covariance functions of the Gaussian models have enough capacity. In our study, we give a excess
risk bound on the estimator arising from EBVAE with Gaussian models, which includes a term
depend on the sample size due to random fluctuations and therefore enables us to study the finite
sample performance of the EBVAE estimator (c.f. Theorem 7).
## 1.2. Summary of Contributions
Below is a summary of our main theoretical contributions in the paper.
2

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

## 1. We provide the first rigorous theoretical analysis to the excess risk of EBVAE.
Despite the empirical success of VAE, to the best of our knowledge, there is no general theory about
the statistical properties of the resulting estimator. A systematic theoretical study on VAE enables
practitioners to be aware of whether their resulting estimators are reliable and provide guidance
on how to set the best hyperparameters and approximation families in concrete situations. In this
study, we address the problem by giving a general statistical framework to analyze the excess risk
for learning densities using EBVAE. The key insight of our work comes from representing the
EBVAE estimator as an M-estimator (see for example, Chapter 5 of Vaart (1998)). Once we make
the connection, we can leverage the rich toolkit of theoretical and methodological results available
for this context. We develop novel oracle inequalities (c.f. Theorem 1) that provide general tools
to verify the statistical accuracy of estimators arising from EBVAE and give insight about which
decoder families, encoder families and prior families yield consistency.
## 2. As an application, we analyze the risk of estimators derived from the commonly-used EBVAE with
Gaussian encoders and decoders in Theorem 7.
The theory we established for EBVAE estimators with Gaussian models highlights the importance
of the covariance matrix of the Gaussian encoder, which is often chosen as a diagonal matrix in
practice. For example, our theory suggests that the approximation error of EBVAE with Gaussian
encoders is strictly related to the model of covariance matrices of encoders, misspecifying the
off-diagonal elements will introduce extra errors. As an implication, the covariate parameters of
Gaussian decoders, which are often chosen to be independent of the data in advance, should be
jointly optimized with other parameters. This explains the reason why Vanilla VAE models tend to
produce unrealistic, blurry samples when applied to complex datasets of natural images (Dosovitskiy
and Brox, 2016). As another implication of our theory, the limited capacity of parametric families
such as Gaussians suggests the necessity of using more complicated encoder/decoder models and
thus we follow the classic nonparametric literature by considering a broad class of nonparametric
families characterized by smoothness levels, and quantify the accompanied approximation error and
estimation error.
## 3. We build a uniform law with a data-dependent complexity specifically tailored to handle the
unbounded loss function associated with EBVAE.
Due to our delicate localization technique in the proof, we obtained a “fast rate” (i.e. n−1 rate in case
of parametric models) without assuming the boundedness of loss function (w.r.t. data x) as opposed
to a “slow rate” (i.e. n−1/2 ). This is achieved by our key localization Lemma 12 and Lemma 13.
Specifically, Lemma 12 provides a “maximal” type inequality for controlling the supreme of an
unbounded empirical process specifically constructed for dealing with the loss function involving the
Killback-Leibler divergence.This inequality captures the local fluctuation behavior of our empirical
loss function via the variance of the increments of an empirical process. Its proof involves non-trivial
applications of many empirical process techniques such as chaining and peeling. Lemma 13 provides
an upper bound to the local Rademacher complexity (Bartlett et al., 2005) associated with unbounded
functions, which enables us to deal with the unbounded loss function associated with EBVAE.
## 4. We take the low-dimensional structure of data space into account and illustrate that EBVAE can
benefit from the underlying submanifold structure.
Specifically, our results for EBVAE with Gaussian encoders/decoders (c.f. Theorem 7) show the
adaptiveness of EBVAE to lower-dimensional submanifold structures so that the bound does not

3

TANG YANG

suffer from the “curse of dimensionality”. This is achieved by our Lemma 17 that provides an error
bound of ReLU neural networks for approximating smooth functions with domain being close to a
dz -dimensional submanifold and Lemma 18 that gives an explicit dependence of the excess risk and
approximation error of EBVAE estimators on the variance of the data given latent variables.
## 1.3. Notations.
We summarize some necessary notations and definitions here. We use X ⊆ Rdx and Z ⊆ Rdz
to denote the data space and the latent space, p(x|z) to denote the decoder, q(z|x) to denote the
encoder and π(z) to denote the prior for the latent variable. To simplify the notation, we may also
use shorthands p, q, π when no ambiguity may arise. In the parametric case, we use θ ∈ Θθ , φ ∈ Θφ
and β ∈ Θβ to denote the parameters associated with the decoder family Fdd , the encoder family
Fed and the prior family Fprior respectively, and use pθ (x|z), qφ (z|x) and πβ (z) with shorthands
pθ , qφ , πβ to denote the decoder, encoder and prior in these families. We use pD (x) to denote the
target data distribution and {xi }ni=1 to denote n i.i.d. copies generated from pD (x).
For a d-dimensional Euclidean vector x, we use kxkp to denote its `p norm. For a function f (x) :
R
i (x)
d
1
R 7→ Rd2 , ∇f (x) is a d2 ×d1 matrix, with (∇f (x))i,j = ∂f∂x
. DTV (p, q) = 12 |p(x)−q(x)|dx
j
R
denotes the total variation distance and DKL (p||q) = log p(x)
q(x) p(x)dx denotes the Kullback-Leibler
(KL) divergence. We use N (µ, Σ) to denote the multivariate Gaussian distribution with mean vector
µ ∈ Rd and covariance matrix Σ ∈ Rd×d . The symbols . and & mean the corresponding inequality
up to an n-independent constant. For multi-indexes γ = (γ1 , · · · , γd ) ∈ Nd0 , a function f is said to
be of class Ck (k ∈ N≥0 ) if all partial derivative of order γ (kγk1 ≤ k) exist and are continuous. We
use C α (Ω) to denote the Hölder space on Ω with Hölder exponent α > 0 (see for example, Evans
(2010)), and we use Brα (Ω) to denote the closed ball in C α (Ω) with Hölder norm k · kC α (Ω) being
bounded by r. We will also use the definition of Orlicz norms (see e.g. Dudley (1999)), recalled
next. For α > 0, define the function ψα : R+ → R+ with the formula ψα (x) = exp (xα ) − 1 . For
a random variable X, we define its Orlicz norm with respect to ψα as



kXkψα = inf λ > 0 : E ψα (|X|/λ) ≤ 1 .
By standard analysis, we have for all t > 0,
P(|X| ≥ t) ≤ 2 exp

n

−



t α o
.
kXkψα

## 1.4. Organization
The rest of the paper is organized as follows. In Section 2, we give a brief description of EBVAE.
In Section 3, we develop an oracle inequality (Theorem 1); and in Section 4, we apply our oracle
inequality to parametric and nonparametric cases. The paper is concluded with a discussion in
Section 5. For the Appendix: a numerical study is included in Appendix A; the proofs of the main
results are included in Appendix B; and the proofs of technical lemmas are included in Appendix C.

## 2. Empirical Bayes Variational Autoencoder
Suppose we have a dataset of x samples from a distribution that can be modelled by a generative
model. Here, a generative model defines a joint distribution over the latent space Z and the data
4

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

space X . Usually we specify a simple prior distribution π(z) over the latent variables, such as
isotropic multivariate Gaussian or uniform, and model the data distribution by complex conditional
distributions (decoders) p(x|z) ∈ Fdd , where Fdd can either be a parametric or nonparametric family.
The goal of VAE is to learn the true underlying marginal likelihood of the data pD (x) in the generative
n
process.
Given
R data {xi }i=1 , we typically aim at maximizing the average marginal log-likelihood
1 Pn
i=1 log p(xi |z)π(z)dz. However, the optimization could be computationally infeasible due to
n
the potentially high dimensional integral in the objective function, so it will be convenient to resort
to VAE. Specifically, VAE overcomes this issue by introducing a family of encoders q(z|x) ∈ Fed
and jointly maximize a lower bound to the log likelihood (Kingma and Welling, 2013),
n

1X
n



Z
log


p(xi |z)π(z)dz − DKL q(·|xi )

i=1

p(xi |·)π(·)
R
p(xi |z)π(z)dz


,

which is equivalent to (up to constants)
n

1X
n

Z
log p(xi |z)q(z|xi )dz − DKL q(·|xi )

π(·)




.

i=1

This objective function is computationally more friendly to optimize since the highest density region
of q(z|x) may be relatively smaller compared with the space of z under the prior.
In the original setting of VAE, the prior is chosen to be simple and data-independent and the
decoder is chosen to be from a Gaussian family for continuous data, i.e, N (Gθ (z), σ 2 I) with Gθ (z)
being implemented with multi-layer perceptron (fully-connected neural networks with one hidden
layer). Even though any d-dimensional distribution can be generated as a push forward measure
through the standard d-dimensional Gaussian (Devroye, 2006), we may need a highly non-regular
map to first map the fixed prior to a complicated distribution of latent variables. This may lead to
underfitting if the decoder families have low capacity. To address this issue, we increase the model
capacity by introducing hyperparameters in the prior and jointly training the prior distribution of
the latent variable over a prior family Fprior with the encoder and decoder (see Appendix A for a
numerical comparison). This lead to the EBVAE as the following optimization problem,

Z
n 
1X
min
− log p(xi |z)π(z)dz + DKL q(·|xi )
p∈Fdd ,q∈Fed ,π∈Fprior n
i=1

R

p(xi |·)π(·)
p(xi |z)π(z)dz


.

R
Pn
−1
The objective function
of
EBVAE
can
also
be
rewritten
as
n
−
log p(xi |z)q(z|xi )dz +
i=1

DKL (q(·|xi ) || π(·)) for facilitating computation. During the learning, we can apply Monte Carlo
method to approximate the above objective function using draws sampled from q(z|x).

## 3. Main Theoretical Results
Despite its popularity, the theoretical aspects of EBVAE are less explored in literature. In this
section, we will study the general statistical properties of the EBVAE estimator through the lens of
M-estimation. As introduced in Section 2, we define the following loss function for a single data x,
m(p, q, π, x) = log R


pD (x)
+ DKL q(·|x)
p(x|z)π(z)dz
5

R

p(x|·)π(·) 
,
p(x|z)π(z)dz

(1)

TANG YANG

where we deliberately added the term log pD (x) which is independent of (p, q, π) to the loss function
for the sake of theoretical analysis. With this notation, the EBVAE estimator can be casted as the
following M-estimator,

(p̂, q̂, π̂) =

arg min

n

p∈Fdd ,q∈Fed ,π∈Fprior

−1

n
X


m(p, q, π, xi ) ,

(2)

i=1

where recall that Fdd denotes the decoder family, Fed denotes the encoder family and Fprior denotes
the prior family. In the population level, we can also define


Ψ∗ =
arg min
EpD (x) m(p, q, π, x)
p∈Fdd ,q∈Fed ,π∈Fprior

as the set of minimizers of the population level loss function.
The goal of this section is to study the finite sample performance of the point estimator obtained
from EBVAE, which is captured by the so-called oracle inequality (Rigollet and Hütter, 2015). We
prove a general oracle inequality for the EBVAE
estimator

 (2) with risk function being chosen
as the population level loss function EpD (x) m(p, q, π, x) in the next theorem. According to the
definition of the loss function in (1), the risk function can be decomposed into two components (c.f.
Theorem 1). The first componentRof the risk function quantifies the difference between the target
density and the marginal density p(x|z)π(z)dz relative to the KL divergence, while the second
p(x|z)π(z)
component quantifies the difference between the encoder and the posterior R p(x|z)π(z)dz
relative to
the KL divergence. Including the second term in the risk function brings several benefits. By writing
the objective function of EBVAE as an empirical counterpart of the risk function as in (2), we can
therefore leverage the existing theory of M-estimation to build an oracle inequality. In addition,
since the second term in the risk function is always nonnegative, the risk function evaluated at
(p̂, q̂, π̂) also acts as an upper bound to the KL divergence between the fitted marginal density and
the target distribution. On the computational side, according to Kingma and WellingR(2013), the loss
function defined in (1) can be regarded as a computationally efficient surrogate to log p(x|z)π(z)dz

in the definition of maximum likelihood estimator (MLE) with error DKL q(·|x) R p(x|·)π(·)dz
,
p(x|z)π(z)dz
which is quantified by the second component of the risk function in the population level. We then
impose the following assumption for controlling the tail for the suprema of an unbounded empirical
process (Adamczak, 2008; Mendelson et al., 2007) appearing in the analysis of EBVAE.
Assumption A For a random variable X with density pD (x), there exist some positive constants
(α, D) such that
(
R

)
p(X|z)π(z)dz
p(X|·)π(·)
sup
log
+ DKL q(·|X) R
≤ D.
pD (X)
p(X|z)π(z)dz
p∈Fdd ,q∈Fed
ψα

π∈Fprior

Roughly speaking, Assumption A is a tail condition on the loss function so that the population level
loss function and its empirical counterpart can be proved to be close to each other uniformly. Similar
assumptions are commonly made in the literature (Grünwald and Mehta, 2020). Our assumption
is comparable to Grünwald and Mehta (2020) on fast rates for unbounded loss where the uniform
boundedness is only in terms of parameters, but not data X. We show in Theorem 7 that Assumption
A is applicable to commonly used encoder/decoder examples. Moreover, for parametric models
6

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

(c.f. Section 4.1) where absolute values of logarithms of density functions pD (x), pθ (x|z), qφ (z|x)
and πβ (z) grow at most polynomially in kxk2 and the parameters (θ, φ, β), if the parameter space
and latent space are bounded and the data X has bounded Orlicz norm with a suitable α > 0 (e.g.
sub-Gaussian and sub-exponential), then Assumption A holds. This requirement holds for any regular
exponential family. Note that Assumption A also holds when the quantity inside the norm is bounded.
For any (p∗ , q ∗ , π ∗ ) ∈ Ψ∗ , consider the shifted function class,

G∗ = g(x) = m(p, q, π, x) − m(p∗ , q ∗ , π ∗ , x) p ∈ Fdd , q ∈ Fed , π ∈ Fprior .
∗

Define the star hull of G∗ as G = {ag | a ∈ (0, 1], g ∈ G∗ }. To bound the estimation error, we
∗
need certain data-dependent estimate of the complexity of G , namely, the local Rademacher
complexity (Bartlett et al., 2005), defined by
"
#
n
1X
∗
sup
Rn (δ, G ) = EpD (x) Eε
εi g(xi ) ,
∗
n
g∈G ,kgk2 ≤δ
i=1

where {εi }ni=1
are n i.i.d. copies from Rademacher distribution, i.e. P (εi = 1) = P (εi = −1) = 12
R
and kgk22 = X g 2 (x)pD (x)dx. We are then ready to state the following theorem that provides oracle
result of EBVAE estimator.
Theorem 1 Consider the EBVAE estimator p̂, q̂ and π̂ defined in (2). Under Assumption A,
1
∗
if there exist δn > 0 and (p∗ , q ∗ , π ∗ ) ∈ Ψ∗ , such that: (1) Rn (δn , G ) ≤ δn2 /(D log α n); (2)
2
(nδn2 /(D2 log α n))min{α,1} ≥ log(log δDn ), then there exist constants (c0 , c1 , c2 ) only dependent of
min{α,1} o
n

2
that,
α, such that it holds with probability at least 1 − c0 exp − c1 2 nδn2
D log α n



EpD (x) m(p̂, q̂, π̂, x) ≤ inf

γ>0




1



1  2 log− α n
(1 + γ)
min
EpD (x) m(p, q, π, x) + c2 1 +
δ
,
p∈Fdd ,q∈Fed ,
γ n D
π∈Fprior




where we can decompose EpD (x) m(p, q, π, x) = DKL pD (·)
h

p(x|·)π(·) i
EpD (x) DKL q(·|x) R
.
p(x|z)π(z)dz

Z


p(·|z)π(z)dz +

Qd1/αe
Remark 2 The constant c2 has a polynomial dependence on d1/αe! = j=1 j when α ≤ 1,
so there is a super-exponential dependence on α. The main tool for proving Theorem 1 is the
tail inequality for the suprema of an unbounded empirical process (Adamczak, 2008). One major
difficulty is that the tail bound applies only to a deterministic radius δ, as opposed to the random
radius kĝk2 = km(p̂, q̂, π̂, ·) − m(p∗ , q ∗ , π ∗ , ·)k2 . This issue can be solved by using the “peeling”
argument (Wainwright, 2019), i.e., considering sets Sm = {2m−1 δn ≤ kĝk2 ≤ 2m δn } with
m = 1, · · · log(D/δn ). See Appendix B.1 for further details.
The result in Theorem 1 can be used to determine a set of sufficient conditions under which the
EBVAE estimator is consistent. An estimator is called consistent if it converges to its estimand
as sample size increases, which gives a guarantee that we could get the right answer of parameters of interest based on the estimator for large sample sizes. The first term of the bound in
7

TANG YANG

Theorem 1 corresponds to the approximation error and tends to be small as the encoder family,
decoder family and prior family become richer. In the next section, we give instances of Fdd ,
Fed and Fprior leading to zero approximation error in concrete examples.
R In particular, in the
usual setting where the target data distribution pD (x) can be expressed as p∗ (x|z)π ∗ (z)dz with
∗
p∗ (x|z) ∈ Fdd and
. The approximation
error can be further upper bounded by
 π (z) ∈ Fprior

minq∈Fed EpD (x) DKL q(·|x) p∗ (x|·)π ∗ (·)/pD (x) , which validates the importance of choosing
a suitable encoder family. In practice, many approaches have been developed to increase the empirical
performance of VAE by using flexible encoder families, e.g. NF (Rezende and Mohamed, 2015),
IAF (Kingma et al., 2016), which outperform the Vanilla VAE. The second term of the bound in
Theorem 1 corresponds to the estimation error which tends to be small as complexities of the encoder
family, decoder family and prior family decrease. In particular, the deterministic radius δn in the
∗
estimation error term is called the critical radius associated with G (Wainwright, 2019), which is
commonly used to specify bounds on the excess risk in M-estimation problems. We will determine
δn in some representative examples under different choices of Fdd , Fed and Fprior in Section 4.
Ideally, we want to make a choice to Fdd , Fed and Fprior such that the approximation error and
estimation error are well-balanced.

## 4. Applications
In this section, we apply Theorem 1 to some representative examples. In each case, we will determine
the approximation error and solve the δn in Theorem 1 via bounding the local Rademacher complexity
from above by Dudley’s integral (see, for example, (8.13) of Vershynin, 2018) to obtain an explicit
excess risk bound in terms of model characteristics.
## 4.1. Parametric Models
In this subsection, we consider the case when Fdd , Fed and Fprior are parametric families. Recall
that to explicitly express the dependence of the encoder and decoder on the parameters, we adopt the
notation in (Kingma and Welling, 2013) to use pθ (x|z), pφ (z|x) and πβ (z) with shorthands pθ , qφ
and πβ to denote the decoder, the encoder and the prior respectively. To begin with, we impose the
∗
following Lipschitz condition for bounding the Rademacher complexity associated with G , which
is a common regularity condition in M-estimation problem (Vaart, 1998).
Condition A For Fdd = {pθ (x|z) | θ ∈ Θθ ⊆ Rdθ }, Fed = {qφ (z|x) | φ ∈ Θφ ⊆ Rdφ } and
Fprior = {πβ (z) | β ∈ Θβ ⊆ Rdβ }, there exist some constants (a0 , a1 ) such that for any θ, θ0 ∈
Θθ , φ, φ0 ∈ Θφ , β, β 0 ∈ Θβ and x ∈ X ,
kθk∞ + kφk∞ + kβk∞ ≤ a0 ,
m(pθ , qφ , πβ , x) − m(pθ0 , qφ0 , πβ 0 , x) ≤ b(x)k(θ, φ, β) − (θ0 , φ0 , β 0 )k2 ,


with EpD (x) b2 (x) ≤ a1 , where m(pθ , qφ , πβ , x) is the loss function for single data point defined in
equation (1).
We are then ready to state the following theorem that provides an oracle inequality for the EBVAE
estimators with parametric models.
Theorem 3 Consider the EBVAE estimator pθ̂ , qφ̂ and πβ̂ defined in (2), and let d∗ = dθ + dφ + dβ .
If Assumption A and Condition A hold, then there exist some constants (c0 , c1 , c2 ) that only depend
8

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND


on (α, a0 , a1 ) so that it holds with probability at least 1 − c0 exp − c1 (d∗ log n)min{α,1} that,
n




EpD (x) m(pθ , qφ , πβ , x)
EpD (x) m(pθ̂ , qφ̂ , πβ̂ , x) ≤ inf (1 + γ)
min
γ>0

θ∈Θθ ,φ∈Θφ ,β∈Θβ


o
1
1  Dd∗
+ c2 1 +
log(nd∗ ) log α n .
γ n
The estimation error (second term) of Theorem 3 scales as O(1/n) up to a logarithmic term, which
matches the minimax optimal rate of parametric density estimation (Rigollet and Hütter, 2015;
Silverman, 1986). The approximation error term of the risk bound in Theorem 3 is zero if the
model is well-specified,
that is, there exist some pθ∗ ∈ Fdd , qφ∗ ∈ Fed and πβ ∗ ∈ Fprior , such that
R
pD (x) = pθ∗ (x|z)πβ ∗ (z)dz and qφ∗ (z|x) is the posterior density with likelihood pθ∗ (x|z) and
prior πβ ∗ (z). Moreover, enriching the prior distribution family Fprior via hyperparameters may
greatly reduce the approximation error term when Fdd and Fed have limited capacities. Conversely,
the estimation error is positively correlated with the number of parameters d∗ . Suitable choices
of Fdd , Fed and Fprior should minimize the risk upper bound, i.e., the approximation error and
estimation error P
are balanced. In fact, Tomczak and Welling (2017) empirically shows that when the
2
“Vamp prior” K1 K
k=1 N (µφ (uk ), diag(σφ (uk )) is used as the parametric family of the prior, a most
suitable choice of K is 500, either decreasing it or increasing it will result in significant deterioration
of the performance (c.f. Appendix A for some numerical results). Theorem 3 provides a theoretically
explanation to this phenomenon. When K is small, the first term (approximation error) in the risk
bound dominates and when K is large, the second term (estimation error) dominates.
It has been
shown that the prior which minimizes (2) is given by the corresponding aggregated
1 Pn
posterior n i=1 qφ̂ (z|xi ) (Tomczak and Welling, 2017). The next corollary offer theoretical guarantees to methods that parameterize the prior for approximating the aggregated posterior (Tomczak
and Welling, 2017; Bauer and Mnih, 2018) via giving an upper bound to the total variation distance
between the target distribution and the distribution generated from a latent space model with prior
being the aggregated posterior and conditional distribution being the fitted decoder.
Corollary 4 Consider the EBVAE estimator pθ̂ , qφ̂ and πβ̂ defined in (2). Let d∗ = dθ + dφ + dβ .
If Assumption A and Condition A hold, and for any z ∈ Z, kzk2 ≤ a2 , x ∈ X , (φ, φ0 ) ∈ Θφ and
(z, z 0 ) ∈ Z, the support of z under qφ (z|x) is contained in Z, and |qφ (z|x) − qφ0 (z 0 |x)| ≤ a3 (kφ −
φ0 k2 + kz − z 0 k2 ), then for some constants (c0 , c1 , c2 , c3 ) only dependent of (dz , α, a0 , a1 , a2 , a3 ),

such that it holds with probability at least 1 − c0 exp − c1 (log n)min{α,1} that
Z  X
n





1
2
DTV pD (·),
qφ̂ (z|xi ) pθ̂ (·|z)dz ≤ c2 min EpD (x) m(pθ , qφ , πβ , x)
θ∈Θθ
Z n
i=1

φ∈Θφ ,β∈Θβ

1
Dd∗
log(nd∗ ) log α n.
n
Remark 5 Here we state the risk bound in terms of total variation distance since the total variation
distance is a metric satisfying the triangle inequality. Corollary 4 is proved by the triangle inequality
and the fact that the aggregated posterior is close to the fitted prior with high probability.

+ c3

## 4.2. Gaussian Encoder and Decoder
In this subsection, we study the theoretical properties of the commonly used Gaussian encoder and
decoder (Kingma and Welling, 2013; Doersch, 2016). Same as Section 4.1, we use pθ (x|z) (pθ )
9

TANG YANG

and qφ (z|x) (qφ ) to denote the decoder and encoder. We consider pθ (x|z) = N (Gθ1 (z), σ 2 Idx )
and qφ (z|x) = N (µφ (x), Σφ (x)), where Gθ1 (z), µφ (x) and Σφ (x) are functions parametrized
by θ1 and φ, and σ is a unknown parameter jointly trained with others. Adopting the Gaussian
encoder family for qφ (z|x) makes the optimization problem (2) in EBVAE computationally simpler.
Unfortunately,
for µφ (x) and Σφ (x), the approximation error from
h
 even if we assume high capacity
i
p (x|·)π (·)

EpD (x) DKL qφ (·|x) R p θ(x|z)π β(z)dz
is nonvanishing, since the posterior is not necessarily
θ
β
Gaussian. However, if we assume the true data X to be generated by some low dimensional latent
variable Z, with a deterministic and invertible generative function GD (z), plus a random Gaussian
error vector with mean 0 and covariance matrix σ ∗ 2 Idx where σ ∗ is small enough, i.e., using T# µ
to denote the image measure (or push-forward) of µ by T and µ ∗ ν to denote the convolution of
µ and ν, so that the model of X can be expressed as (GD# πD ) ∗ N (0, σ ∗ 2 Idx ), then Z becomes
nearly “deterministic” given X and the approximation error vanishes, which is consistent with the
finding in Doersch (2016). We then state the our conditions on the approximation family Fprior and
assumptions on the true model pD . For a vector-valued function f (x), we use kf (x)kp to denote its
vector `p norm at input x.

Condition B The family of prior Fprior = πβ (z) | β ∈ Θβ ⊆ Rdβ has a compact parameter
space Θβ . In addition, there exist some constants (b2 , b3 ) such that for any β, β 0 ∈ Θβ and z ∈ Rdz ,
kβk2 ≤ b2 , | log πβ (0)| ≤ b2 , k∇z log πβ (z)k2 ≤ b2 (kzk2 + 1) and | log πβ (z) − log πβ 0 (z)| ≤
b(z) kβ − β 0 k2 with kb(z)k2 ≤ b2 (kzkb23 + 1).
Assumption B Assume the followings:
1
), where πD (z) is a
B.1: The data distribution pD = (GD# πD ) ∗ N (0, σ ∗ 2 Idx ) (σ1 ≤ σ ∗ ≤ 2e
d
z
probability density function (w.r.t. the Lebesgue measure on R ) that belongs to Fprior . For a
Pz
random variable Z with probability density πD , it holds that k di=1
(Zi )2 kψ1 ≤ b5 with some
d
constant b5 > 0. Moreover, ∀ z ∈ R z , ∇πD (z) exists and k∇πD (z)k2 ≤ b5 .
B.2: There exists an integer k ≥ 2, so that GD (z) : Rdz 7→ Rdx (dz ≤ dx ) is a Ck map, and there
exists a Ck map QD (x) : Rdx 7→ Rdz such that ∀ z ∈ Rdz , QD ◦ GD (z) = z. Also, there exist some
constants (α, b6 ) where 0 < α ≤ 2, such that for any 1 ≤ i ≤ dx , 1 ≤ j ≤ dz , z ∈ Rdz and x ∈ Rdx ,
2
2
P
P
it holds that |γ|≤k |Dγ GD,i (z)| ≤ b6 (kzk2α +1) and |γ|≤k |Dγ QD,j (x)| ≤ b6 (kxk2α +1), where
GD,i (z) and QD,j (x) are the elements of the ith and the jth dimension of GD (z) and QD (x), γ is a
multi-index γ = (γ1 , γ2 , . . . , γd ) ∈ Nd0 and Dγ denotes the mixed partial derivative operator.

Remark 6 Condition B requires the priors in Fprior to behave like (mixture of) Gaussian distributions. Assumption B requires the latent variable to have a density function that is sub-Gaussian and
sufficiently smooth, and demands some regularity conditions on the map GD . It states that GD (z)
is a Ck map with a Ck inverse QD (x) and the mixed partial derivatives of GD (z) and QD (x) are
upper bounded by polynomial functions of z and x with order up to α2 respectively. The invertibility
of GD (z) is also assumed in Doersch (2016). The assumptions on the mixed partial derivatives of
GD and QD ensure that GD and QD can be well approximated by ReLU neural networks.

1
Theorem 7 Choose σ1 ∈(0, 2e
], and consider Fdd = pθ (x|z) = N (Gθ1 (z), σ 2 Idx ) | Gθ1 (z) ∈
FG , σ ∈ [σ1 , 1] , Fed = qφ (z|x) = N (µφ (x), Σφ (x)) | (µφ (x), Σφ (x)) ∈ Fµ,Σ and Fprior =
{πβ (z) | β ∈ Θβ ⊆ Rdβ }. If Condition B holds for Fprior , then there exists a choice of FG and
Fµ,Σ so that for any target distribution pD = (GD# πD ) ∗ N (0, σ ∗ 2 Idx ) satisfying Assumption B,
the EBVAE estimator pθ̂ , qφ̂ and πβ̂ defined in (2) satisfies that there exist some constants (c, c1 , c2 )
10

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

that only depend on (dz , dx ) and (α, k, b2 , b3 , b5 , b6 ) in Assumption B and Condition B, such that it
holds with probability at least 1 − n−c that,
2dz



2
1 d β + σ1 − k
1
EpD (x) m(pθ̂ , qφ̂ , πβ̂ , x) ≤ c1 logα̃1 ∗ σ ∗ 2 + c2 log α n logα̃2
,
σ
σ1
nσ12

(3)

2

dz
where α̃1 = 28+10α+3α
and α̃2 = α2 + α(k−1)
+ d2z + 6. Recall that σ ∗ is the standard deviation of
α2
1
each component of the data X given the latent variable Z with σ ∗ ∈ [σ1 , 2e
].

Remark 8 In the decoder, we use a Gaussian distribution to approximate the posterior, so that
D (z)
pD (z|x) = pD (x|z)π
can be well approximated by a Gaussian either. When σ ∗ is small, the
pD (x)
invertibility assumption on GD guarantees that the highest density region of pD (z|x) is concentrated
around QD (x). By applying the first order Taylor expansion of GD,j (z) at z = QD (x), we have that
Px
pD (z|x) ∝ πD (z) exp(− dj=1
(xj − GD,j (z))2 /2σ ∗ 2 ) is approximately a Gaussian distribution
with mean QD (x) + ΣD (x)∇GD (z)T |z=QD (x) (x − GD (QD (x))) and covariance matrix σ ∗ 2 ΣD (x)
with ΣD (x) = (∇GD (z)T |z=QD (x) ∇GD (z)|z=QD (x) )−1 . FG and Fµ,Σ are realized through feedforward ReLU neural networks with sizes depend on σ1 in the proof of Theorem 7 to achieve the rate
in equation (3). Since the data X lie approximately on a dz -dimensional manifold, the result does
not suffer from the “the curse of dimensionality”, i.e., the dimension of X (dx ) does not occur in the
exponent of the approximation error of a ReLU neural network with given size for approximating
functions of X with certain smoothness constraints, see Appendix B.3.1 for further details.
The constants (c1 , c2 ) has an exponential dependence on dz and a polynomial dependence on dx ,
scale as (c3 )dz and (dx )c4 for positive constants c3 , c4 independent of (n, dx , dz ). The occurrence
of σ ∗ 2 in the above theorem is from the fact that pD (z|x) is not necessarily a Gaussian distribution,
which theoretically explains the reason why VAE models tend to produce unrealistic, blurry samples
when applied to complex datasets of natural images (Dosovitskiy and Brox, 2016). In particular,
when σ1  σ ∗ , regardless of the logarithmic term, the risk bound in above thorem scales as
2dz
σ ∗ 2 + nσ1∗2 (dβ + σ ∗ − k ), where the first term corresponds to an upper bound for the approximation
error and the second term correspond to an excess risk bound. In particular, if the noise level
k
σ ∗ decreases with the sample size at the rate σ ∗  n−k1 , where 0 < k1 < 2(k+d
, the EBVAE
z)
estimator will be consistent relative to the KL risk function, which give theoretical guarantee to
EBVAE estimators and theoretically explains the phenomenon that Vanilla VAE still achieves good
performance for some simple dataset (e.g. MNIST dataset) even if the encoder model is misspecified
as a simple gaussian model. Here, we emphasize that we need k1 to be upper bounded since dz
can be smaller than dx and the KL divergence may diverge to infinity if the supports of the two
distributions are not the same. In addition, for fixed σ ∗ and n, the above bound depends on the
number of parameters in the prior family and the smoothness of GD . When a pre-specified data
independent prior is used, we may need a highly complicated GD to first map the chosen prior to a
highly irregular distribution of latent variables, which increases the capacity demand for GD .
In practice, the covariance matrix of the encoder model Σφ (x) is often chosen to be diagonal
and characterized by a variance vector (Kingma and Welling, 2013; Tomczak and Welling, 2017).
However, Remark 8, when σ ∗ converges to 0, the posterior of the latent variable converges to a
Gaussian distribution with covariance matrix σ ∗ 2 (∇GD (z)T |z=QD (x) ∇GD (z)|z=QD (x) )−1 , which
may not be diagonal. Misspecifying the off-diagonal elements of the covariance matrix introduces
11

TANG YANG

extra approximation errors and thus deteriorates the performance of the EBAVE estimator. In order
to achieve the smallest risk, we should model the full dz × dz covariance matrix instead of through
a variance vector. A natural practical choice of Σφ (x) is Σ̃φ (x)T Σ̃φ (x) + ε2 Idz , where Σ̃φ (x) is
a dz × dz matrix modelled by a neural network and ε is small number to guarantee the positive
definiteness of the covariance matrix. The theory we established for EBVAE estimators with Gaussian
encoders and decoders also validates the importance of the variance parameter σ in the decoder
family, which is often chosen as a predefined weighting factor depending on the target accuracy level
for reconstructing. However, our theory suggests that misspecifying the conditional variance of the
data will lead to a large approximation error. Consequently, the variance parameter of the decoder
family should be jointly optimized instead of being prespecified. Moreover, if the decoder family is
correctly specified, i.e. the conditional distribution of data is N (Gθ∗ (z), σ ∗ 2 Idx ), then the parameter
σ should be constrained by a lower bound that is close to σ ∗ up to a multiplicative constant.
## 4.3. Nonparametric Models
The risk bound in the previous subsection demands us to consider more complicated encoder and
decoder families to reduce the approximation error. Motivated by this, we consider nonparametric
families in this subsection. We assume the data space X and the latent space Z are [0, 1]dx and [0, 1]dz
respectively. To begin with, we consider the following densities on X characterized by an undirected
graphical model (Markov network) (Koller
sizes being
bounded

 and Friedman, 2009) withPclique
k1
l
(x
by p as our decoder family: F̄dd = pdd (x|z) : p(x|z) ∝ exp
l
(x
,
z)
j
j
j
j , z) ∈
j=1
α
|+d
|x
z
j
Br1 ([0, 1]
), |xj | ≤ p , where xj is a subvector of x = (x1 , · · · , xdx ) with |xj | being its
dimension. Similarly, we consider the following encoder family on Z: F̄ed = q(z|x) : q(z|x) ∝

Pk2
fj (z, xj ) ∈ Brα2 ([0, 1]|xj |+dz ), |xj | ≤ p . We then state our condition on
exp
j=1 fj (z, xj )
the approximation families and assumption on the true model pD for deriving the Lipschitzness of
the loss function in (1).

Condition C Fdd ⊆ F̄dd and Fed ⊆ F̄ed . For the family of prior Fprior = πβ (z) | β ∈
Θβ , Θβ is a compact set so that for any β, β 0 ∈ Θβ and z ∈ Z, | log πβ (z) − log πβ 0 (z)| ≤
c1 kβ − β 0 k2 with a constant c1 and the support of πβ is contained in Z. Moreover, we have
supπβ ∈Fprior supz∈Z | log πβ (z)| ≤ c2 with some positive constant c2 .
Assumption C There exists a positive constant c such that supx∈X |log pD (x)| ≤ c.
For ease of notation, we define δn as: if dz + p < 2α, then δn = n
α
1√
−
δn = n− 4 log n; if dz + p > 2α, then δn = n 2(dz +p) .

α
− 2α+d
+p
z

; if dz + p = 2α, then

Theorem 9 Consider the EBVAE estimator p̂, q̂ and πβ̂ defined in (2). If Condition C and Assumption C hold, then forsome constants (c0 , c1 , c2 ) independent of n, it holds with probability at least
1 − c0 exp −c1 nδn2 that







1 2
EpD (x) m(p̂, q̂, πβ̂ , x) ≤ inf (1 + γ) min EpD (x) m(p, q, πβ , x) + c2 1 +
δ .
p∈Fdd ,q∈Fed
γ>0
γ n
πβ ∈Fprior

R
Remark 10 If the target distribution pD (x) can be expressed as Z pD (x|z)πD (z)dz with some
pD (x|z) and πD (z), where pD (x|z) ∈ F̄dd , log πD (z) ∈ Crα1 ([0, 1]dz ) and πD (z) ∈ Fprior , then
by choosing (k2 , r2 ) in F̄ed to be (k1 , cr1 ) with some constants c and (Fdd , Fed ) = (F̄dd , F̄ed ), the
12

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

approximation error term in the above risk bound is zero. Moreover, when p  dx (e.g. given the
latent variable, the component of each dimension of the data is independent of each other), the
additive structure in the encoder family and decoder family prevents the risk bound from suffering
from “the curse of dimensionality”.

## 5. Discussion
In this paper, we consider variational autoencoders via empirical Bayes estimation, referred to as
Empirical Bayes Variational Autoencoders (EBVAE), which is a general framework including popular
VAE methods as special cases. Theoretically, we give a general statistical framework to analyze
the convergence rate for learning densities using EBVAE. We develop novel oracle inequalities
which quantitively capture impacts of prior families, encoder families, and decoder families on
excess risks of the estimators arising from the EBVAE. The key idea in our proof comes from
representing the EBVAE estimator as an M-estimator. Once making this connection, we can leverage
the general theoretical machinery of M-estimation for obtaining a risk bound. Our theory gives
sufficient conditions under which the EBVAE estimators are consistent in both parametric cases
and nonparametric cases. In particular, we carefully analyze the estimator derived from EBVAE
with Gaussian encoders and decoders, we show that it is consistent if the conditional variance of
data given latent variables decreases with sample size under suitable rates. Our result highlights the
importance of covariance matrices of encoders and decoders in obtaining a good statistical guarantee.
The risk bound we derived for the EBVAE estimators under Gaussian models does not apply to
the case that the data is deterministic given latent variables, for the reason that the dimension of latent
variables can be smaller than the dimension of data and the KL divergence may diverge to infinity
if the supports of the two distributions are not the same. We suspect that this issue can be resolved
by stating the risk bound in terms of some adversarial losses that is insensitive to small fluctuations
compared with KL divergence (e.g. Wasserstein distance, Santambrogio, 2015); we leave this for
future work. Moreover, the proposal of encoder and decoder families that yield consistency in more
general cases without adding significant computational burden is another important topic of future
research.

13

TANG YANG

References
Radoslaw Adamczak. A tail inequality for suprema of unbounded empirical processes with applications to markov chains. Electron. J. Probab., 13:1000–1034, 2008. doi: 10.1214/EJP.v13-521.
URL https://doi.org/10.1214/EJP.v13-521.
Martin Anthony and Peter L. Bartlett. Neural Network Learning: Theoretical Foundations. Cambridge University Press, 1999. doi: 10.1017/CBO9780511624216.
Peter L. Bartlett, Olivier Bousquet, and Shahar Mendelson. Local rademacher complexities. Ann.
Statist., 33(4):1497–1537, 08 2005. doi: 10.1214/009053605000000282. URL https://doi.
org/10.1214/009053605000000282.
Peter L. Bartlett, Nick Harvey, Christopher Liaw, and Abbas Mehrabian. Nearly-tight vc-dimension
and pseudodimension bounds for piecewise linear neural networks. Journal of Machine Learning
Research, 20(63):1–17, 2019. URL http://jmlr.org/papers/v20/17-612.html.
Matthias Bauer and Andriy Mnih. Resampled priors for variational autoencoders, 2018.
Andrew Brock, Jeff Donahue, and Karen Simonyan. Large scale gan training for high fidelity natural
image synthesis, 2018.
Yuri Burda, Roger Grosse, and Ruslan Salakhutdinov. Importance weighted autoencoders. arXiv
preprint arXiv:1509.00519, 2015.
Xi Chen, Diederik P. Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya
Sutskever, and Pieter Abbeel. Variational lossy autoencoder, 2016.
Chandler Davis and William Morton Kahan. The rotation of eigenvectors by a perturbation. iii. SIAM
Journal on Numerical Analysis, 7(1):1–46, 1970.
Luc Devroye. Nonuniform random variate generation. Handbooks in operations research and
management science, 13:83–121, 2006.
Carl Doersch. Tutorial on variational autoencoders, 2016.
Alexey Dosovitskiy and Thomas Brox. Generating images with perceptual similarity metrics based
on deep networks, 2016.
R. M. Dudley. Uniform Central Limit Theorems. Cambridge Studies in Advanced Mathematics.
Cambridge University Press, 1999. doi: 10.1017/CBO9780511665622.
Lawrence C. Evans. Partial differential equations. American Mathematical Society, Providence, R.I.,
## 2010.
Clark R. Givens and Rae Michael Shortt. A class of wasserstein metrics for probability distributions.
Michigan Math. J., 31(2):231–240, 1984. doi: 10.1307/mmj/1029003026. URL https://doi.
org/10.1307/mmj/1029003026.
Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair,
Aaron Courville, and Yoshua Bengio. Generative adversarial networks, 2014.
14

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Karol Gregor, Ivo Danihelka, Alex Graves, Danilo Jimenez Rezende, and Daan Wierstra. Draw: A
recurrent neural network for image generation, 2015.
Peter D. Grünwald and Nishant A. Mehta. Fast rates for general unbounded loss functions: From
erm to generalized bayes. Journal of Machine Learning Research, 21(56):1–80, 2020. URL
http://jmlr.org/papers/v21/18-488.html.
Victor Guillemin and Alan Pollack. Differential topology, volume 370. American Mathematical
Soc., 2010.
Tony Jebara and Marina Meila. Machine learning: Discriminative and generative. The Mathematical
Intelligencer, 28(1):67–69, 2006.
Diederik P Kingma and Max Welling. Auto-encoding variational bayes, 2013.
Durk P Kingma, Tim Salimans, Rafal Jozefowicz, Xi Chen, Ilya Sutskever, and Max Welling.
Improved variational inference with inverse autoregressive flow. In Advances in neural information
processing systems, pages 4743–4751, 2016.
Daphne Koller and Nir Friedman. Probabilistic graphical models: principles and techniques. MIT
press, 2009.
Tejas D. Kulkarni, Will Whitney, Pushmeet Kohli, and Joshua B. Tenenbaum. Deep convolutional
inverse graphics network, 2015.
Michel Ledoux and Michel Talagrand. Probability in Banach Spaces: Isoperimetry and Processes.
Springer Berlin Heidelberg, Berlin, Heidelberg, 1991. ISBN 978-3-642-20212-4. doi: 10.1007/
978-3-642-20212-4_8. URL https://doi.org/10.1007/978-3-642-20212-4_8.
Tengyuan Liang. How well generative adversarial networks learn distributions, 2018.
Pascal Massart. Concentration inequalities and model selection. 2007.
Shahar Mendelson, Alain Pajor, and Nicole Tomczak-Jaegermann. Reconstruction and subgaussian
operators in asymptotic geometric analysis. Geometric and Functional Analysis, 17(4):1248–1282,
## 2007.
John T Ormerod and Matt P Wand. Explaining variational approximations. The American Statistician,
64(2):140–153, 2010.
Danilo Jimenez Rezende and Shakir Mohamed. Variational inference with normalizing flows. arXiv
preprint arXiv:1505.05770, 2015.
Danilo Jimenez Rezende, Shakir Mohamed, and Daan Wierstra. Stochastic backpropagation and
approximate inference in deep generative models, 2014.
Phillippe Rigollet and Jan-Christian Hütter. High dimensional statistics. Lecture notes for course
## 18S997, 2015.
Filippo Santambrogio. Optimal transport for applied mathematicians. Birkäuser, NY, 55(58-63):94,
## 2015.
15

TANG YANG

Marwin H. S. Segler, Thierry Kogej, Christian Tyrchan, and Mark P. Waller. Generating focussed
molecule libraries for drug discovery with recurrent neural networks, 2017.
Simon J. Sheather. Density estimation. Statist. Sci., 19(4):588–597, 11 2004. doi: 10.1214/
088342304000000297. URL https://doi.org/10.1214/088342304000000297.
Bernard W Silverman. Density estimation for statistics and data analysis, volume 26. CRC press,
## 1986.
Charles J. Stone. Optimal global rates of convergence for nonparametric regression. Ann. Statist.,
10(4):1040–1053, 12 1982. doi: 10.1214/aos/1176345969. URL https://doi.org/10.
1214/aos/1176345969.
Jakub M. Tomczak and Max Welling. Vae with a vampprior, 2017.
A. W. van der Vaart. Asymptotic Statistics. Cambridge Series in Statistical and Probabilistic
Mathematics. Cambridge University Press, 1998. doi: 10.1017/CBO9780511802256.
Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves,
Nal Kalchbrenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet: A generative model for
raw audio, 2016.
R. Vershynin. High-Dimensional Probability: An Introduction with Applications in Data Science. Cambridge Series in Statistical and Probabilistic Mathematics. Cambridge University
Press, 2018. ISBN 9781108415194. URL https://books.google.com/books?id=
NDdqDwAAQBAJ.
Martin J. Wainwright. High-Dimensional Statistics: A Non-Asymptotic Viewpoint. Cambridge
Series in Statistical and Probabilistic Mathematics. Cambridge University Press, 2019. doi:
## 10.1017/9781108627771.
Jacob Walker, Carl Doersch, Abhinav Gupta, and Martial Hebert. An uncertain future: Forecasting
from static images using variational autoencoders, 2016.
Zichao Yang, Zhiting Hu, Ruslan Salakhutdinov, and Taylor Berg-Kirkpatrick. Improved variational
autoencoders for text modeling using dilated convolutions, 2017.
Dmitry Yarotsky. Error bounds for approximations with deep relu networks. Neural Networks, 94:
103–114, 2017.

16

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Appendix
Notations: We adopt the notations in the manuscript, and further introduce the following additional
notations for technical proof. We write a  b if a . b and a & b. a = O(b) if a  b. For a matrix
A ∈ Rm×n , we use kAkF and kAkop to denote its Frobenius norm and operator norm respectively.
When m = n, we use λmin (A) and λmax (A) to denote its minimal and maximal eigenvalues. Unless
otherwise specified, for a matrix A ∈ Rn×n , |A| denotes the determinant. N(G, d, ε) denotes the
ε-covering number of G under metric d. O(n, d) denotes the set of n × d matrices U such that
U T U = Id , O(d) denotes the set of d × d orthogonal matrices.

Appendix A. Numerical study
A.1. Set up
In the experiments we aim at: (1) verifying empirically whether the EBVAE outperform VAE, (2)
investigate the influence of the choice of the prior family on the performance of data generation
and (3) showing the validity of our theory. We carry out experiment using two models: “Vanilla
VAE” (Kingma and Welling, 2013) and “VampPrior” (VP) (Tomczak and Welling, 2017). The
“Vanilla VAE” model use a predefined isotropic gaussian prior. The “VampPrior” model consider
prior and amortized inference distribution
K

1 X
N (µφ (uk ), diag(σφ2 (uk ))
πφ,u (z) =
K
k=1

qφ (z|x) = N (µφ (x), diag(σφ2 (x)),
where K is the number of pseudo-inputs, and uk is a D-dimensional vector we refer to as a pseudoinput. We then apply the two model to the dynamic MNIST dataset. In the experiments we modeled all
distributions using MLPs with two hidden layers of 300 hidden units. The dimension of the latent variable is choose to be 40, and for “VampPrior” model, we choose K = (1, 10, 100, 300, 400, 500, 600).
A.2. Results
We quantitatively evaluate the three method using the test marginal log-likelihood (LL) estimated
using the Importance Sampling (Burda et al., 2015). The LL values and the digits generated by the
two models is given in Figure 1 and Figure 2.
We can see that the supremacy of EBVAE is visible not only in LL values but in image generations as well. According to our results on the parametric rate, the estimation error includes two
terms: Approximation error and the dimension of parameters. The “Vanilla VAE” model use a
predefined prior, so dβ = 0, but the approximation error is larger than VP model, which result in
a poor performance. Also, for the VP model, when the number of pseudo-inputs is large enough,
increasing the number of pseudo-inputs will actually result in drop of the performance, which is
d +d +d
consistent with our bound, since when the parameter space of prior is too large, the θ nφ β term
will dominate.
17

TANG YANG

Figure 1: Test LL between different models

(a) Vanilla VAE

(b) VP-K=300

(c) VP-K=500

Figure 2: Digits generated by different models

Appendix B. Proof of Main Results
B.1. Main Theoretical Results
Define

n

Mn (p, q, π) =

1X
m(p, q, π, xi );
n
i=1

∗

M (p, q, π) = EpD (x) m(p, q, π, x),
where m(p, q, π, x) is defined in equation (1). We also use the notation p(x) to denote the marginal
R
p(x|z)π(z)
p(x|z)π(z)dz and p(z|x) to denote the posterior R p(x|z)π(z)dz
when no ambiguity may arise. We
18

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

begin the proof of Theorem 1 with the following two lemmas for controlling the supreme of an
unbounded empirical process.
Lemma 11 Suppose Assumption A holds, then there exist some constants (c1 , c2 ) only depend on α,
such that for any p(x|z), p0 (x|z) ∈ Fdd , q(z|x), q 0 (z|x) ∈ Fed and π(z), π 0 (z) ∈ Fprior ,
!
2
D2 log α n
≤ c1 (D log n)DKL (pD (·)||p(·)) +
;
EpD (x)
n


EpD (x) (DKL (q(·|x)||p(·|x)) − DKL (q 0 (·|x)||p0 (·|x)))2 ≤
!

2  D2 log α2 n
p
p
1
c2 (D log α n)EpD (x)
DKL (q(·|x)||p(·|x)) − DKL (q 0 (·|x)||p0 (·|x))
+
.
n
"

pD (x)
log
p(x)

2 #

1
α

Lemma 12 Under Assumption A, if there exist (p∗ , q ∗ , π ∗ ) ∈ Ψ∗ and δn satisfying conditions
defined in Theorem 1, then there exist some constants (c0 , c1 , c2 ) that only!depend on α , such that it

min{α,1}
2
nδn
holds with probability larger than 1 − c0 exp −c1
that,
2
2
D log α n

∀p(x|z) ∈ Fdd , q(z|x) ∈ Fed , π(z) ∈ Fprior ,
|Mn (p, q, π) − Mn (p∗ , q ∗ , π ∗ ) − M ∗ (p, q, π) + M ∗ (p∗ , q ∗ , π ∗ )|
δn + km(p, q, π, ·) − m(p∗ , q ∗ , π, ·)k2
1

≤ c2 δn /(D log α n).
## B.1.1. P ROOF OF T HEOREM 1
km(p̂, q̂, π̂, ·) − m(p∗ , q ∗ , π ∗ , ·)k22
"
2 #
p̂(x)
p∗ (x)
= EpD (x)
+ DKL (q̂(·|x)||p̂(·|x)) + log
− DKL (q ∗ (·|x)||p∗ (·|x))
− log
pD (x)
pD (x)
"
"
 #
 #
p̂(x) 2
p∗ (x) 2
≤ 4EpD (x)
log
+ 4EpD (x)
log
pD (x)
pD (x)
h
i
+ 2EpD (x) (DKL (q̂(·|x)||p̂(·|x)) − DKL (q ∗ (·|x)||p∗ (·|x)))2 .
Therefore by Lemma 11 and
such that,

√

a+b ≤

√
√
a + b (a, b ≥ 0), there exists a constant C0 = C0 (α)

km(p̂, q̂, π̂, ·) − m(p∗ , q ∗ , π ∗ , ·)k2
≤ C0

log

1
2α

!

√

r
p
n D
M ∗ (p̂, q̂, π̂) +

min

p∈Fdd ,q∈Fed ,π∈Fprior

19

M ∗ (p, q, π)

1

D log α n
√
+
n

!
.

TANG YANG

Therefore by Lemma 12 and the fact that Mn (p̂, q̂, π̂) ≤ Mn (p∗ , q ∗ , π ∗ ), under the high probability
set of Lemma 12, there exists a constant C = C(α) such that,
M ∗ (p̂, q̂, π̂) −

min

p∈Fdd ,q∈Fed ,π∈Fprior

M ∗ (p, q, π)

= M ∗ (p̂, q̂, π̂) − M ∗ (p∗ , q ∗ , π ∗ )
≤ |Mn (p̂, q̂, π̂) − Mn (p∗ , q ∗ , π ∗ ) − M ∗ (p̂, q̂, π̂) + M ∗ (p∗ , q ∗ , π ∗ )|
!
!
1
1
r
−α
log− 2α n p ∗
n
1
log
√
≤ Cδn
.
M (p̂, q̂, π̂) +
min
M ∗ (p, q, π) + √ + δn
p∈Fdd ,q∈Fed ,π∈Fprior
D
n
D

By the fact that

min{α,1}

2
nδn

2
D2 log α n

√
& log(log δDn ) and the inequalities that 2 ab ≤ γa +

1
depend on α such that it holds
γ b (a, b, γ > 0), there exist some constant (c0 , c1 , c2 ) that only !

min{α,1}
2
nδn
with probability larger than 1 − c0 exp −c1
that,
2
2
D log α n

DKL (pD (·)||p̂(·)) + EpD (x) [DKL (q̂(·|x)||p̂(·|x))] = M ∗ (p̂, q̂, π̂)


DKL (pD (·)||p(·)) + EpD (x) [DKL (q(·|x)||p(·|x))]
min
≤ min (1 + γ)
γ>0

p∈Fdd ,q∈Fed ,π∈Fprior
1

1  log− α n 
+ c2 1 + δn2
.
γ
D
## B.1.2. P ROOF OF L EMMA 12
For G∗ = {g(x) = m(p, q, π, x) − m(p∗ , q ∗ , π ∗ , x) | p ∈ Fdd , q ∈ Fed , π ∈ Fprior }, it holds that

sup |g(x)| ≤ 2
g∈G∗

Therefore

sup

log

p∈Fdd ,q∈Fed ,π∈Fprior

sup |g(x)|
g∈G∗

< +∞ and
ψα


p(x)
+ DKL (q(·|x)||p(·|x)) .
pD (x)

sup g(x) − EpD (x) g(x)

g∈G∗

< +∞. Define
ψα

n

Zn (δ, G∗ ) = sup

g∈G∗
kgk2 ≤δ

Since n1 sup

g∈G∗
kgk2 ≤δ

1X
g(xi ) − EpD (x) g(x) .
n
i=1

Pn

2
i=1 var(g(xi )) ≤ δ , by the tail inequality for suprema of unbounded empirical

processes (see for example, Theorem 4 and Lemma 1 of Adamczak (2008)), it holds that
P (Zn (δ, G∗ ) ≥ (1 + η)EpD (x) (Zn (δ, G∗ )) + s2 )
(
)!
ns4 nα s2α
ns2
≤ c0 (η, α) exp −c1 (η, α) min
,
,
.
δ 2 Dα log n D log α1 n
20

(4)

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Using the standard symmetrization (see, for example, Proposition 4.11 of Wainwright (2019)), we
can get


n
X
2
EpD (x) [Zn (δ, G∗ )] ≤ EpD (x) Eε  sup
εi g(xi ) 
∗
n
g∈G
i=1

kgk2 ≤δ

∗

= 2Rn (δ, G∗ ) ≤ 2Rn (δ, G ),
∗

∗

1

where recall that G = {ag|a ∈ (0, 1], g ∈ G∗ }. Therefore by Rn (δn , G ) ≤ δn2 /(D log α n), it
holds that
∀r ≥ δn ,

∗

EpD (x) [Zn (r, G∗ )] ≤ 2Rn (r, G )


= 2EpD (x) Eε 



sup
g∈G

∗

k δrn gk2 ≤δn

r 1
δn n

n
X

εi

i=1


δn
g(xi ) 

r

r
∗
Rn (δn , G )
δn
rδn
≤2
.
1
D log α n
≤2

Define the events
1

A0 = {Zn (δn , G∗ ) ≥ c2 δn2 /(D log α n)};
n

A1 = {∃g ∈ G∗ , such that

1
1X
g(xi ) − EpD (x) g(x)] ≥ c2 δn kgk2 /(D log α n)
n

i=1

and kgk2 ≥ δn }.
Using equation (4), there exist some constants (c00 , c01 , c2 ) that only depend on α such that

!min{α,1} 
2
nδ
n
.
P (A0 ) ≤ c00 exp −c01
2
2
D log α n

2
Define Sm = 2m−1 δn ≤ kgk2 ≤ 2m δn with m = 1, · · · M , since kgk
D is upper bounded by some
D
constant less than infinity, we have M . log( δn ).
1
Under A1 ∩Sm , it holds that Zn (2m δn ) ≥ c2 2m−1 δn2 /(D log α n). Therefore by



2
nδn

log(log δDn ), we know, for some constants (c3 , c4 ) that only depend on α,

!min{α,1} 
M
2
X
nδn
.
P (A1 ) =
P (A1 ∩ Sm ) ≤ c3 exp −c4
2
2
α n
D
log
m=1
Moreover, under Ac0 ∩ Ac1 , we have
1 Pn
1
i=1 g(xi ) − EpD (x) g(x)
n
sup
≤ c2 δn /(D log α n).
δn + kgk2
g∈G∗
We can then get the desired conclusion.
21

2

D2 log α n

min{α,1}
&

TANG YANG

B.2. Parametric Models
R
We use pθ,β (x) to denote the marginal pθ (x|z)πβ (z)dz and pθ,β (z|x) to denote the posterior
R pθ (x|z)πβ (z) . We begin the proof of Theorem 3 with the following lemma for dealing with the
pθ (x|z)πβ (z)dz
unboundedness of the objective function. The Proof of Lemma 13 is based on the proof of Proposition
## 6.7 of Ledoux and Talagrand (1991).
∗

Lemma 13 Consider G∗ and G defined in Section 3. If

sup |g(x)|
g∈G∗

≤ 2D, then there exists
ψα

1

ρ ≤ c0 D log α n and a constant c, where (c, c0 ) only depend on α, such that ∀δ > 0,


EpD (x)  sup

∗
g∈G
kgk2 ≤δ

n
X

1
n



g(xi ) − EpD (x) g(x) 

i=1


1
n


≤ EpD (x)  sup

∗
g∈G
kgk2 ≤δ

n
X
i=1

(
where A denotes the event



1

D log α n

g(xi )1A (xi ) − EpD (x) [g(x)1A (x)]  + c
.
n

)
sup |g(x)| ≤ ρ , and 1A (x) denotes the indicator function of event A.

g∈G∗

## B.2.1. P ROOF OF T HEOREM 3
(
1
α

Choose ρ ≤ c0 D log n in Lemma 13 and define A =

)
sup |g(x)| ≤ ρ . Define

g∈G∗

n
o
∗
∗
GA = gA (x) = g(x)1A (x), g(x) ∈ G ;

(5)

G∗A = {gA (x) = g(x)1A (x), g(x) ∈ G∗ } ,
∗

with G and G∗ being defined in Section 3. Using standard symmetrization, we can get


EpD (x)  sup

∗
g∈G
kgk2 ≤r

n
1X

n





g(xi )1A (xi ) − EpD (x) [g(x)1A (x)]  ≤ EpD (x) Eε  sup

∗
gA ∈GA
kgA k2 ≤r

i=1

0 )=
Define dn (gA , gA



q P
n
1
n

0
2
i=1 (gA (xi ) − gA (xi )) , then

rn =

max

∗
gA ,g 0 ∈G
A
0
kgA k2 ,kg k2 ≤r
A

0
dn (gA , gA
) ≤ 2ρ.

22

2
n

n
X
i=1



εi gA (xi )  .

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

By equation (3.84) of Wainwright (2019), there exists a constant c such that,


n
2X 2


EpD (x) rn2 ≤ EpD (x)  sup
gA (xi )
∗ n
gA ∈GA
i=1

kgA k2 ≤r


4

≤ EpD (x)  sup
∗ n
gA ∈GA
kgA k2 ≤r

n
X


2 
gA (xi ) − EpD (x) gA (x)  + 4r2

i=1

∗

≤ c(r2 + ρRn (r, GA )).
∗

Since G∗A is uniformly bounded by ρ, it holds that Rn (r, GA ) ≤ ρ and we only need to consider r ≤ ρ.
∗
Therefore we can get c(r2 + ρRn (r, GA )) ≤ c0 ρ2 . Moreover, for any gA ∈ G∗A and a ∈ (0, 1], there
ε
ε
ε
ε
< a ≤ (k + 1) 2ρ
gA , agA ) ≤ 2ρ
ρ = 2ε . Therefore
exists a k ∈ N, such that k 2ρ
and dn ((k + 1) 2ρ
∗

∗

it follows that the ε- covering number of GA satisfies that, N(GA , dn , ε) ≤ N(G∗A , dn , 2ε ) 2ρ
ε and
∗
2ρ
ε
∗
∗
log N(GA , dn , ε) ≤ log N(GA , dn , 2 ) + log ε . Recall the definition of GA in equation (5), it
follows that
v
u n
u1 X
0
∗
0
∀gA , gA ∈ GA , dn (gA , gA ) = t
(m(pθ , qφ , πβ , xi ) − m(pθ0 , qφ0 , πβ 0 , xi ))2 1A (xi )
n
i=1
v
u n
u1 X
≤t
b2 (xi )k(θ, φ, β) − (θ0 , φ0 , β 0 )k22
n
i=1
v
u n
u1 X
=t
b2 (xi )k(θ, φ, β) − (θ0 , φ0 , β 0 )k2
n
i=1

= dn ((θ, φ, β), (θ0 , φ0 , β 0 )).
W.l.o.g, we can assume kθk∞ + kφk∞ + kβk∞ ≤ 1. By the fact that the ε-covering number of unit
ball in Rd is smaller than ( 3ε )d , let d∗ = dθ + dφ + dβ , we have
 √ q P

n
1
∗
2 (x )
3
b
d
i
i=1
ε
ε
n
.
log N(G∗A , dn , ) ≤ log N(Θ, dn , ) ≤ d∗ log 
2
2
ε
We next analyze the Dudley entropy integral in the following lemma.
Lemma 14 Given Condition A, there exists a constant c1 that only depend on a1 in Condition A
such that,
v


 q ∗P

u
n
Z rn u
d
2 (x )
3
b
i
u ∗
i=1
n

 + log 2ρ dε
td log 
EpD (x) 

ε
ε
0
≤ c1

√
ρ d∗

s
−EpD (x)



!

h p
i
rn 2
rn 2
rn 2
∗
∗
( ) log EpD (x) ( ) + EpD (x) ( ) + EpD (x) rn d log d
.
2ρ
2ρ
2ρ
23

TANG YANG

√
Since rn ≤ 2ρ and −xlogx + x is an increasing function when x < 1, by EpD (x) rn2 ≤ c(r2 +
∗
ρRn (r, GA )) ≤ c0 ρ2 and Dudley inequality (see, for example, (8.13) of Vershynin (2018)), we have
r
√
1
1 2
ρ
∗
∗
Rn (r, GA ) . √ (r + ρRn (r, GA )) 2 log + log d∗ d∗ .
r
n
q
1
1
∗
d∗ ∗
Choose δn = c2 log n+log
d D log α n, if Rn (δn , GA ) > δn2 /(D log α n), then
n
1 1
∗
∗ 1p
Rn (δn , GA ) . √ ρ 2 Rn (δn , GA ) 2 d∗ (log n + log d∗ ),
n
which means
∗

Rn (δn , GA ) .

ρd∗
log(nd∗ ).
n
∗

1
Therefore for a large enough c2 , we have Rn (δn , G ) ≤ δn2 /(D log α n) and



2
nδn

min{α,1}

2

D2 log α n

≥

log(log δDn ), the desired conclusion then follows from Theorem 1.
## B.2.2. P ROOF OF C OROLLARY 4
!
Z
n
1X
DTV
pθ̂ (·|z)
qφ̂ (z|xi )dz, pD (·)
n
Z
i=1
Z Z
n
1
1X
=
pθ̂ (x|z)
qφ̂ (z|xi )dz − pD (x) dx
2 X Z
n
i=1
Z Z
Z
n
1
1X
≤
pθ̂ (x|z)
qφ̂ (z|xi )dz −
pθ̂ (x|z)EpD (x) qφ̂ (z|x)dz dx
2 X Z
n
Z
i=1
Z Z
Z
1
p (x|z)EpD (x) qφ̂ (z|x)dz −
pθ̂ (x|z)πβ̂ (z)dz dx
+
2 X Z θ̂
Z
+ DTV (pθ̂,β̂ (·), pD (·))
Z

n
1X
qφ (z|xi ) − EpD (x) qφ (z|x) + DTV
qφ̂ (·|x)pD (x)dx, πβ̂ (·)
≤ sup
φ,z n
X
i=1

+ DTV (pθ̂,β̂ (·), pD (·)).
R
By the fact that X pθ̂,β̂ (z|x)pθ̂,β̂ (x)dx = πβ̂ (z), it holds that
Z

DTV
qφ̂ (·|x)pD (x)dx, πβ̂ (·)
Z XZ
1
q (z|x)pD (x)dx − πβ̂ (z) dz
=
2 Z X φ̂
Z Z
Z
1
≤
qφ̂ (z|x)pD (x)dx −
pθ̂,β̂ (z|x)pD (x)dx dz
2 Z X
X
Z Z
Z
1
+
p (z|x)pD (x)dx −
pθ̂,β̂ (z|x)pθ̂,β̂ (x)dx dz.
2 Z X θ̂,β̂
X
24

(6)

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

For the first term in equation (6), we can further upper bound,
Z
Z Z
1
pθ̂,β̂ (z|x)pD (x)dx dz
q (z|x)pD (x)dx −
2 Z X φ̂
X
Z Z
1
qφ̂ (z|x) − pθ̂,β̂ (z|x) dzpD (x)dx
≤
2
Z X Z
DTV (qφ̂ (·|x), pθ̂,β̂ (·|x))pD (x)dx,
=
X

and for the second term,
Z
Z Z
1
p (z|x)pD (x)dx −
pθ̂,β̂ (z|x)pθ̂ (x)dx dz
2 Z X θ̂,β̂
X
Z Z
1
≤
pD (x) − pθ̂,β̂ (x) pθ̂,β̂ (z|x)dzdx
2 X Z
= DTV (pD (·), pθ̂,β̂ (·)).
Now we define Zn = sup n1

Pn

0
i=1 qφ (z|xi ) − EpD (x) qφ (z|x) , then by kqφ (z|x) − qφ0 (z |x)k ≤

φ,z

c(kφ − φ0 k2 + kz − z 0 k2 ) and the compactness of parameter space and latent space, using Dudley
inequality (see, for example, (8.13) of Vershynin (2018)) and Talagrand concentration inequality
(see, for example, 3.27 of Wainwright
(2019)), we can get that it holds with probability larger than
q
d log(d n)

φ
φ
1 − exp(c log n) that Zn .
. Then, the desired conclusion follows from Theorem 3 and
n
Pinsker inequality (see, for example, Theorem 2.16 of Massart (2007)).

B.3. Gaussian Encoders and Decoders
We use pθ,β (x) to denote the marginal
R pθ (x|z)πβ (z) .
p (x|z)π (z)dz
θ

R

pθ (x|z)πβ (z)dz and pθ,β (z|x) to denote the posterior

β

## B.3.1. P ROOF OF T HEOREM 7
To begin with, we make the following definition.
Definition 15 FdD (L, W, U, b, V ) is defined as the set of following feedfoward ReLU neural networks (feedfoward neural network with ReLU activation σ(x) = max(x, 0)): 1. The information
of each layer can only come from the previous one layer. 2. U is a (L − 2)-dimensional vector,
U = (u1 , · · · , uL−2 ). The network has d input units, D output units, L layers, ul−1 computation
units in layer l (2 ≤ l ≤ L − 1) and W weights (parameters). 2. There exists a constant V ≥ 2
such that in each layer, the absolute value of each weight unit is upper bounded by V . 3. The output
unit has the Hard Tanh hb (x) = max(−b, min(b, x)) as its activation function. In particular, we use
FdD (L, W, U, b) to denote FdD (L, W, U, b, V ) with V = +∞.
1

Then we consider the following ReLU neural networks: Qφ1 (x) ∈ Fddxz (L1 , U1 , W1 , b8 (log σ11 ) 2 ),
1

1

Gdφ2 (z) ∈ Fddzx dz (L2 , U2 , W2 , b9 (log σ11 ) α ) and Gθ1 (z), Gφ3 (z) ∈ Fddzx (L, U, W, b(log σ11 ) α , V ),
where Gdφ2 (z) is rescaled to be a dx ×dz matrix. Since there is no boundary towards the support of the
25

TANG YANG

1

1

data x and the latent variable z, we define compact sets of z and : Bz = [−η log 2 σ1∗ , η log 2 σ1∗ ]dz
1
1
and B = [−γ log 2 σ1∗ , γ log 2 σ1∗ ]dx . And let Bx = {x = GD (z)+σ ∗  | z ∈ Bz ,  ∈ B }. Then we
1
1
define B z = [−η log 2 σ1∗ , η log 2 σ1∗ ]dz so that QD (Bx ) ⊆ B z . Next We define following numbers
to characterize the expressivity of families of Qφ1 , Gφ3 and Gdφ2 ,
0 := min max kQφ1 (x) − QD (x)k2 ;
Qφ1 x∈Bx

1 := min max kGφ3 (z) − GD (z)k2 ;
Gφ3 z∈B z

(7)

2 := min max kGdφ2 (z) − ∇GD (z)kF .
Gdφ z∈B z
2

Here we omit families of (Qφ1 , Gφ3 , Gdφ2 ) and the dependency of (0 , 1 , 2 ) on (η, γ, η, GD (z), QD (x))
and families of (Qφ1 , Gφ3 , Gdφ2 ) for ease of notation.
Remark 16 The decoder is using a gaussian to approximate the posterior, so we want pD (z|x) =
pD (x|z)πD (z)
to be well approximated by a gaussian either. When σ ∗ is small, the above assumptions
pD (x)
on GD (z) can guarantee that the space
are likely under pD(z|x) is z being close to QD (x).
 of z that
1 Pdx
Also, we have pD (z|x) ∝ πD (z) exp − 2σ∗2 j=1 (xj − GjD (z))2 , consider the first order Taylor
expansion of GjD (z) at z = QD (x), pD (z|x) can be well approximated by a gaussian distribution
with mean QD (x) + ΣD (x)∇GD (QD (x))T (x − GD (QD (x))) and covariance matrix σ ∗ 2 ΣD (x)
with ΣD (x) = (∇GD (QD (x))T ∇GD (QD (x)))−1 , where ∇GD (QD (x)) = ∇GD (z)|z=QD (x) .
So we can make specific choices of Σφ (x) and µφ (x),

−1
Σφ (x) = σ̄ 2 Gdφ2 (Qφ1 (x))T Gdφ2 (Qφ1 (x)) + σ̄ 2 Idz
;
1
Σφ (x)i,j ));
σ̄ 2
µφ (x) = Qφ1 (x) + Σ̃φ (x)Gdφ2 (Qφ1 (x))T (x − Gφ3 (Qφ1 (x))),
Σ̃φ (x)i,j = max(−b̄7 , min(b̄7 ,

(8)


 42
where Σφ (x)i,j is the (i, j) element of Σφ (x), b̄7 = b7 log σ11 α with a large enough constant b7
and σ̄ ∈ [σ1 , 1] is a parameter. Here we add σ̄ 2 Idz to Σφ (x) to guarantee the positive definiteness.
For ease of notation, we use Θθ1 to denote the parameter spaces of Gθ1 , and use Θφ̃ to denote the
cartesian product of parameter spaces of Qφ1 , Gdφ2 and Gφ3 , we can then define:

Fdd = pθ (x|z) = N (Gθ1 (z), σ 2 Idx ) | θ1 ∈ Θθ1 , σ ∈ [σ1 , 1] ;

4
1 α2
Fed = qφ (z|x) = N (µφ (x), Σφ (x)) | φ = (φ1 , φ2 , φ3 , σ̄), (φ1 , φ2 , φ3 ) ∈ Θφ̃ , σ̄ ∈ [σ1 , 1], b̄7 = b7 log
.
σ1
(9)
We then state the following Lemma 17 to bound the error of ReLU neural networks for approximating
QD (x) satisfying Assumption B, whose domain is close to a dz -dimensional submanifold, the proof
of Lemma 17 is based on the proof of Theorem 1 of Yarotsky (2017).


26

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Lemma 17 Consider Bx , B z , (Qφ1 , Gφ3 , Gdφ2 ) and (0 , 1 , 2 ) defined above, there exist some
constants (c0 , c, c1 , c2 , c3 ) that only depend on (η, γ, η, dz , dx ) and (α, k, b6 ) in Assumption B, such
that if we choose
1
b = b8 = b9 = c0 , L = L1 = L2 = c log , V = σ1−c3 , N =
σ1

!− 1

k

σ1


log σ11

 2dz2+2 + dz +k + k
α

α

;

2

dz


 dz dz
 dz
dz
1 αk + 2 +2
1 α(k−1) + 2 +2
1 2
2 − dkz
dz
W = c1 log
(σ1 )
, W1 = c1 N (log ) , W2 = c1 log
(σ1 )− k−1 ;
σ1
σ1
σ1

 dz + dz +1
 dz + dz +1

dz
dz
1 α(k−1) 2
1 αk 2
1
(σ1 2 )− k , u1 = c2 N dz (log ), u2 = c2 log
(σ1 )− k−1 ;
u = c2 log
σ1
σ1
σ1
U = (u, · · · , u), U1 = (u1 , · · · , u1 ), U2 = (u2 , · · · , u2 ),
| {z }
| {z }
| {z }

L1 −2

L−2

L2 −2

1
then for any GD (z) and QD (x) satisfying Assumption B and σ ∗ ≥ σ1 , it holds that σ0∗ + σ∗2
+ σ2∗ ≤ 1.

We can then state the following lemma to bound the approximation error and the excess risk of the
EBVAE estimator with Gaussian encoder/decoder.
Lemma 18 Consider Fdd , Fed defined in (9), Fprior satisfying Condition B and the EBVAE estimator pθ̂ , qφ̂ and πβ̂ defined in (2), suppose Assumption B is satisfied, then there exist some constants
(η, γ, η, b7 , c1 , c2 , c3 ) that only depend on (dz , dx ) and (α, k, b2 , b3 , b5 , b6 ) in Assumption B and
1
Condition B, such that when σ0∗ + σ∗2
+ σ2∗ ≤ 1, it holds with probability at least 1 − n1c that,
h
i
DKL (pD (·)||pθ̂,β̂ (·)) + EpD (x) DKL (qφ̂ (·|x)||pθ̂,β̂ (·|x))
2
 28+10α+3α
2







2



2 


α
1
≤ c1 σ
log n + L log(V kU k1 ) + log
σ1


× dβ + (W1 + W2 )(L1 + L2 ) log(kU1 k1 + kU2 k1 ) + (W1 + W )(L1 + L) log(kU1 k1 + kU k1 ) .
∗2

1
log ∗
σ

α

log α n
+ c2
nσ12

1
log
σ1

So, by lemma 17 and lemma 18 and the fact that k ≥ 2 and σ1 ≤ σ ∗ , one has
h
i
DKL (pD (·)||pθ̂,β̂ (·)) + EpD (x) DKL (qφ̂ (·|x)||pθ̂,β̂ (·|x))




2
1 α̃1
log α n
1 α̃2
−2
−(2+ 2dkz )
∗2
+ c2
(dβ σ1 + σ1
) log
,
≤ c1 σ
log ∗
σ
n
σ1
2

dz
where α̃1 = 28+10α+3α
and α̃2 = α2 + α(k−1)
+ d2z + 6.
α2

B.4. Nonparametric Models
R
We use the notation p(x) to denote the marginal p(x|z)πβ (z)dz and p(z|x) to denote the posterior
R p(x|z)πβ (z) . We begin the proof of Theorem 9 with the following two lemmas.
p(x|z)π (z)dz
β

27

TANG YANG

Lemma 19 When Condition C and Assumption C hold, consider m(p, q, πβ , x) defined in (1), there
exists a constant c such that ∀p(x|z), p0 (x|z) ∈ Fdd , ∀q(z|x), q 0 (z|x) ∈ Fed and ∀πβ (z), πβ 0 (z) ∈
Fprior , it holds that
v
u n
u1 X
t
m(p, q, πβ , xi ) − m(p0 , q 0 , πβ 0 , xi ))2
n
i=1




≤ c  sup | log q(z|x) − log q 0 (z|x)| + sup | log p(x|z) − log p0 (x|z)| + sup log πβ (z) − log πβ 0 (z)  .
x∈X
z∈Z

z∈Z

x∈X
z∈Z

P

P

k1
k1
0 (x|z) ∝ exp
0 (x , z) and q(z|x) ∝
l
(x
,
z)
,
p
l
Lemma 20 If p(x|z) ∝ exp
j
j
j
j=1
j=1 j

P

P
k2
k2
0
0
exp
j=1 fj (z, xj ) . Then,
j=1 fj (z, xj ) , q (z|x) ∝ exp
sup | log q(z|x) − log q 0 (z|x)| +
x∈X ,z∈Z

sup | log p(x|z) − log p0 (x|z)|
x∈X ,z∈Z


≤ 2  sup

k2
X

fj (z, xj ) −

x∈X ,z∈Z j=1

k2
X

fj0 (z, xj ) +

j=1

sup

k1
X

lj (xj , z) −

x∈X ,z∈Z j=1

k1
X


lj0 (xj , z)  .

j=1

## B.4.1. P ROOF OF T HEOREM 9
∗

W.l.o.g, we can assume k1 = k2 = k and r1 = r2 = 1. Consider G and G∗ defined in Section 3.
By Condition C, we have
|g(x)| = |m(p, q, πβ , x) − m(p∗ , q ∗ , πβ ∗ , x)|
= log

p(x)
+ DKL (q(·|x)||p(·|x)) − DKL (q ∗ (·|x)||p∗dd,β ∗ (·|x))
∗
pdd,β ∗ (x)

≤ 2(

sup

sup (| log p(x)| + | log q(z|x)| + | log p(z|x)|))

p∈Fdd ,q∈Fed x∈[0,1]dx
πβ ∈Fprior z∈[0,1]dz

≤ 2C.
∗

Therefore G is uniformly bounded by 2C.
∗

First we consider R̂n (δ, G ) = Eε [ sup | n1
∗
g∈G
kgkn ≤δ

Pn

i=1 εi g(xi )|] and

v
u n
u1 X
0
dn (g, g ) = t
(g(xi ) − g 0 (xi ))2 .
n
i=1

∗

2

δ̂n
By Corollary 14.3 of Wainwright (2019), R̂n (δ̂n , G ) ≤ 2C
is satisfied if

64
√
n

Z δ̂n q
δ̂n2
∗
log
N(G
,
d
,
ε)dε
≤
.
n
2
δ̂n
2C
4C

28

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Furthermore, by the same argument of the proof of Theorem 3, one has
∗

log N(G , dn , ε) ≤ log N(G∗ , dn , ε) + log

4C
.
ε

Define set Q and G as
Q :=

G :=


k
X

j=1

k
X


j=1

lj (xj , z) | lj (xj , z) ∈ C1α ([0, 1]|xj |+dz ), |xj | ≤ p




;



α
|xj |+dz
), |xj | ≤ p .
fj (z, xj ) | fj (z, xj ) ∈ C1 ([0, 1]


Then by Lemma 19 and Lemma 20, we have for some constant c,
ε
ε
ε
N(G∗ , dn , ε) ≤ cN(G, k.k∞ , ) · N(Q, k.k∞ , ) · N(Θβ , k.k2 , ).
3
3
3
Since every Gj (xj , z) with |xj | ≤ p can be seen as a function of x0j ⊇ xj with |x0j | = p, we can
p+dz

assume |xj | = p. Since log N(B1α ([0, 1]p+dz ), k.k∞ , ε) . ( 1ε ) α (see equation (5.17) of (Wain
wright, 2019)) and dpx ≤ ( edpx )p , we can get
ε
log N(G, k.k∞ , )
2
 

dx
ε k
α
p+dz
≤ log
## N(B1 ([0, 1]
), k.k∞ , )
p
k
dz +p 1 p+dz
edx
. k 1+ α ( ) α + kp log
.
ε
p
dz +p

p+dz

Similarly, we also have log N(Q, k.k∞ , 2ε ) . k 1+ α ( 1ε ) α + kp log edpx . Then, combined with
∗

dz +p

p+dz

the fact that log N(Θβ , k.k2 , ε) ≤ dβ log( 3 ), we can get log N(G , dn , ε) . k 1+ α ( 1ε ) α
2
∗
δ̂n
kp log edpx . Therefore, R̂n (δ̂n , G ) ≤ 2C
is satisfied if,

## 1. when p + dz < 2α
1
√
n
−α

Z δ̂n s
dz +p 1 p+dz
edx
k 1+ α ( ) α + kp log
dε . δ̂n2 .
ε
p
0
α+dz +p

Choose δ̂n  n 2α+dz +p k 2α+dz +p +

q

kp
edx
n log p .

## 2. when p + dz > 2α
1
√
n
−α

s
Z ∞r
dz +p 1 p+dz
edx
1
k 1+ α ( ) α dε + √ δ̂n kp log
. δ̂n2 .
2
δ̂n
ε
p
n
4C

α+dz +p

Choose δ̂n  n 2(dz +p) k 2(dz +p) +

q

kp
edx
n log p .

29

+

TANG YANG

## 3. when p + dz = 2α

1
√
n
1

1

s
Z δ̂n r
1
kp
edx
k 3 ( )2 dε +
log
. δ̂n2 .
2
δ̂n
ε
n
p
4C

3

Choose δ̂n  n− 4 (log n) 2 k 4 +

q

kp
edx
n log p .

Moreover, for the above choices of δ̂n , nδ̂n2 & log(log 1 ) is satisfied. Let δ n be the smallest positive

δ̂n
2
∗
2
∗
δn
solutions to the inequalities Rn (δ n , G ) ≤ 2C . Then if nδ n . log(log δ1 ), we have δ n . δ̂n . If
n
2
nδ n & log(log δ1 ), we have with probability larger than 0, δ n is smaller than the smallest positive
n
2
∗
δ̂n
solution to R̂n (δ̂n , G ) ≤ 2C
up to some constant (see for example, Proposition 14.25 of Wainwright
(2019)). Since the choice of δ̂n is independent of {xi }ni=1 , we have δ n . δ̂n . Then combined with

Assumption C and Theorem 1, we can get the desired conclusion.

Appendix C. Remaining Proofs
C.1. Main Theoretical Results
## C.1.1. P ROOF OF L EMMA 11
Firstly we state the following lemma for proving the first statement.
| ≤ C, it holds that
Lemma 21 When | log pp(x)
D (x)

Since

pD (x)
p(x)



sup

log pp(x)
D (x)

p∈Fdd ,π∈Fprior

pD (x)
log
p(x)

2


≤ (2 + C)


pD (x)
pD (x) pD (x)
log
−
+1 .
p(x)
p(x)
p(x)
1

≤ D, if we choose ρ = D(log n) α and define
ψα

(
A1 =

)
p(x)
sup
| log
|>ρ ,
pD (x)
p∈Fdd ,π∈Fprior

then by Chebyshev’s inequality, we have P (A1 ) ≤ n2 . Using 1A1 (x) to denote the indicator of A1 ,
and Ac1 to denote the complementary set of A1 , we can get
"
EpD (x)

p(x)
log
pD (x)

2 #

"
= EpD (x)

p(x)
log
pD (x)

2

#
1Ac1 (x) + EpD (x)

"

p(x)
log
pD (x)

2

#
1A1 (x) .
(10)

30

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

By Lemma 21, we can upper bound the first term of equation (10),
"

#

p(x) 2
EpD (x)
log
1Ac1 (x)
pD (x)
#
"


pD (x) 2
pD (x)
log
1Ac1 (x)
= Ep(x)
p(x)
p(x)



pD (x)
pD (x) pD (x)
≤ (2 + ρ)Ep(x)
log
−
+ 1 1Ac1 (x)
p(x)
p(x)
p(x)
≤ (2 + ρ)DKL (pD (·)||p(·)),
and for the second term,
"

p(x)
log
pD (x)
"

EpD (x)

1A1 (x)

p(x)
sup
log2
pD (x)
p∈Fdd ,π∈Fprior

≤ EpD (x)
Z +∞
=

#

2

!

#
1A1 (x)

p(x)
log2
sup
pD (x)
p∈Fdd ,π∈Fprior

P
0

!

!
1A1 (x)

!
> t dt

Z D2 (log n) α2

!
!
!
p(x)
log2
≤
P
sup
1A1 (x) > 0 dt
pD (x)
p∈Fdd ,π∈Fprior
0
!
Z +∞
p(x)
+
P
sup
log2
> t dt
2
pD (x)
p∈Fdd ,π∈Fprior
D2 (log n) α
!
2
Z +∞
√
α n
log
p(x)
sup
≤ 2D2
+
P
log
> t dt
2
n
pD (x)
p∈Fdd ,π∈Fprior
D2 (log n) α
!α !
2
1
Z +∞
α
t2
2 log n
≤ 2D
+
2 exp −
dt
2
n
D
D2 (log n) α
2
Z ∞
2
log α n
4
= 2D2
+ D2
exp(−x)x α −1 dx
n
α
log n
.D

Therefore EpD (x)

2 log



2
α

n

n

.

D (x)
log pp(x)

2 


≤ c1 (D log
(

1
α

2

2
α n
n)DKL (pD (·)||p(·)) + D log
n


.
)

For the second statement, define A2 =

sup
p∈Fdd ,q∈Fed ,π∈Fprior

31

DKL (q(·|x)||p(·|x)) ≥ ρ . By the

TANG YANG

fact that


EpD (x) (DKL (q(·|x)||p(·|x)) − DKL (q 0 (·|x)||p0 (·|x)))2


2
p
p
0
0
≤ 4ρEpD (x)
DKL (q(·|x)||p(·|x)) − DKL (q (·|x)||p (·|x)) 1Ac2 (x)
"
!
#
+ 4EpD (x)

sup
p∈Fdd ,q∈Fed ,π∈Fprior

2
DKL
(q(·|x)||p(·|x)) 1A2 (x) .

We can get the desired conclusion using the same argument as the first statement.
C.2. Parametric Models
## C.2.1. P ROOF OF L EMMA 13
Since sup |g(x)| = sup |g(x)|, we have
g∈G

∗

g∈G∗

sup |g(x)|
g∈G

≤ 2D.

∗

ψα

Choose
ρ = 8EpD (x) max sup |g(xi )|
∗
1≤i≤n
g∈G

≤ Kα

Since

max sup |g(xi )|

1≤i≤n

g∈G

max sup |g(xi )|

∗
1≤i≤n
g∈G

1

≤ Kα sup |g(x)|

∗

log α n (see for example, equation (13) of

∗

g∈G

ψα

.
ψα

ψα

(
1
α

Adamczak (2008)), it holds that ρ . D log n. Define A =

)
sup |g(x)| ≤ ρ , we have

g∈G



EpD (x)  sup

∗
g∈G
kgk2 ≤δ

1
n

n
X

∗

g∈G
kgk2 ≤δ

"
+ EpD (x)



g(xi ) − EpD (x) g(x) 

i=1



≤ EpD (x)  sup

∗

1
n

n
X



g(xi )1A (xi ) − EpD (x) (g(x)1A (x)) 

i=1

n

1X
sup
g(xi )1Ac (xi ) − EpD (x) (g(x)1Ac (x))
∗ n
g∈G

#
,

i=1

where we can further upper bounded the second term,
"
EpD (x)

n

1X
sup
g(xi )1Ac (xi ) − EpD (x) (g(x)1Ac (x))
∗ n
g∈G
i=1

32

#

"
≤ 2EpD (x)

n

1X
sup
g(xi )1Ac (xi )
∗ n
g∈G
i=1

#
.

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Let τ = inf{j ≤ n : sup |

Pj

∗

i=1 g(xi )1Ac (xi )| > t}. Under τ = j,

g∈G

max sup |
k≤n

g∈G

∗

k
X

g(xi )1Ac (xi )|

i=1
k
X

≤ t + max sup |g(xi )1Ac (xi )| + max sup |
∗
1≤i≤n
g∈G

∗
j<k≤n
g∈G i=j+1

g(xi )1Ac (xi )|

Since {τ = j} only depend on x1 , · · · , xj , we have
P (τ = j, max sup |
k≤n

g∈G

∗

k
X

g(xi )1Ac (xi )| > 3t + s)

i=1
k
X

≤ P (τ = j, max sup |g(xi )1Ac (xi )| > s) + P (τ = j)P ( max sup |
∗
1≤i≤n
g∈G

∗
j<k≤n
g∈G i=j+1

≤ P (τ = j, max sup |g(xi )1Ac (xi )| > s) + P (τ = j)P (max sup |
∗
1≤i≤n
g∈G

k≤n

∗

g∈G

k
X

g∈G
k≤n

g∈G

∗

g(xi )1Ac (xi )| > t)

i=1

Where the last inequality is due to the fact that for any 1 ≤ j < n, sup |
2max sup |

g(xi )1Ac (xi )| > 2t)

∗

Pk

i=j+1 g(xi )1Ac (xi )| ≤

Pk

i=1 g(xi )1Ac (xi )|. A summation over j = 1, · · · , n yields

P (max sup |
k≤n

g∈G

∗

k
X

g(xi )1Ac (xi )| > 3t + s) ≤ P ( max sup |g(xi )1Ac (xi )| > s)
∗
1≤i≤n
g∈G

i=1

+ P 2 (max sup |
k≤n

g∈G

∗

k
X

g(xi )1Ac (xi )| > t)

i=1

So,
n

1X
g(xi )1Ac (xi )
∗ n
g∈G

EpD (x) sup

i=1

k
X
1
EpD (x) max sup
g(xi )1Ac (xi )
∗
k≤n
n
g∈G i=1
Z
k
X
4 +∞
=
P (max sup
g(xi )1Ac (xi ) > 4t)dt
∗
k≤n
n 0
g∈G i=1
Z
Z
k
X
4 +∞ 2
4 +∞
≤
P (max sup
g(xi )1Ac (xi ) > t)dt +
P ( max sup |g(xi )1Ac (xi )| > t)dt
∗
∗
1≤i≤n
k≤n
n 0
n 0
g∈G i=1
g∈G
!
k
k
X
X
4
≤ P max sup
g(xi )1Ac (xi ) > 0 EpD (x) max sup
g(xi )1Ac (xi )
∗
∗
k≤n
k≤n
n
g∈G
g∈G

≤

i=1

i=1

4
+ EpD (x) max sup |g(xi )|
∗
1≤i≤n
n
g∈G
33

TANG YANG

By Markov inequality,
P

max sup
k≤n

∗

g∈G

k
X

!
g(xi )1Ac (xi ) > 0

i=1

≤ P ( max sup |g(xi )| > ρ) ≤
∗
1≤i≤n
g∈G

1
8
1

EpD (x) max sup |g(xi )| . D log α n
1≤i≤n
g∈G

So, we have EpD (x) sup
g∈G

∗

∗

1 Pn
i=1 g(xi )1Ac (xi )
n

1
α

. D logn n .

## C.2.2. P ROOF OF L EMMA 14
q P
∗
Since rn ≤ 2ρ and rn ≤ 2 dn ni=1 b2 (xi ),
v

 q ∗P
u
Z rn u
3 dn ni=1 b2 (xi )
u ∗
 + log 2ρ dε
td log 
ε
ε
0
v
 r
 q ∗P
u
n
Z rn u
d
2 (x )
b
3
i
u ∗
i=1
n
 + log 2ρ dε
td log 
≤
ε
ε
0
v
 q ∗P

u
r
Z 1u
3 dn ni=1 b2 (xi )
u ∗
 + log 2ρ dε
td log 
= rn
rn ε
rn ε
0
v
 q ∗P

u
r
n
d
u
2 (x )
√
Z 1r
3
b
i
u ∗
2ρ
1
i=1
n
∗


t
≤ rn d log
+ rn log
+ rn
d +1
log dε.
rn
rn
ε
0
By log x ≤ 1e x

 v
q P
u
∗
u
3 dn ni=1 b2 (xi ) 
 t


EpD (x) rn log

rn
 v

q P
u
√
n
1
u
2
3 n i=1 b (xi ) 
 t
2ρ d∗

= EpD (x) 
r
log
+
log
n


rn
2ρ



v q
u
√
1 Pn
u
2
t 1 3 n i=1 b (xi ) 
2ρ d∗
.
log
+ rn

rn
e
2ρ

s

≤ EpD (x) 
rn

34

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Since b(x) ∈ L2 (pD (x)), by Cauchy-Schwarz inequality, we have

 v q
u
s
P
n
1
u
2
 t 1 3 n i=1 b2 (xi ) 
 . Ep (x) rn ,
EpD (x) 
D

rn e
2ρ
ρ
 r

 r

2ρ
rn
2ρ 1
EpD (x) rn log
≤ 2ρEpD (x)
log
+
.
rn
2ρ
rn
2
q
 2
Let r2ρn
= y(y ≤ 1), since − 12 y log y + 12 y is concave and non-decreasing when y ≤ 1, by
Jensen inequality, we have

EpD (x)

rn
2ρ

r

v
" 
u
 2
 2 #
2
u 1
2ρ 1
r
rn
rn
1
n
t
log
+
≤ − EpD (x)
log EpD (x)
+ EpD (x)
.
rn
2
2
2ρ
2ρ
2
2ρ

Combine with the fact



R1q
log 1ε dε is less than infinity, we can get the desired conclusion.
0

C.3. Gaussian Encoders and Decoders
## C.3.1. P ROOF OF L EMMA 17
We first state the following lemmas about error bounds for approximations with deep ReLU networks
stated in Yarotsky (2017).
Lemma 22 (Theorem 1 of Yarotsky (2017)) There is a deep feedforward ReLU network architecture with depth at most c(log(1/) + 1), the absolute value of each weight unit at most −c1 and
d
weights and computation units at most c2 − α log(1/) + 1 that is capable of expressing any function
belong to C1α ([0, 1]d ) with error .
Lemma 23 (Proposition 3 of Yarotsky (2017)) Given M > 0 and  ∈ (0, 1), there is a feedforward ReLU network η with two input units that implements a function x
e : R2 → R so that
## 1. For any inputs x, y, if |x| ≤ M and |y| ≤ M, then |e
x(x, y) − xy| ≤ ;
## 2. if x = 0 or y = 0, then x̃(x, y) = 0;
## 3. The depth and the number of weights and computation units in η is not greater than c1 ln(1/)+
c2 with an absolute constant c1 and a constant c2 = c2 (M ).
W.l.o.g, we can assume η = η = 1 and γ q
= 1. Then we consider m = (m1 , · · · , md ) ∈
log 1∗ mi

σ
i =
1 , · · · , z dz ). By the Lip{−N, −(N − 1) · · · , 0, 1, · · · , N }dz , zm
and zm = (zm
m
N
schitzness of GD (z) and QD (x), there exists a constant c1 such that for any (z, z 0 ) ∈ Bz =
q
h q
idz
− log σ1∗ , log σ1∗ , it holds that

35

TANG YANG

0



0

kGD (z) − GD (z )k2 ≤ c1 kz − z k2
0



0

kz − z k2 ≤ c1 kGD (z) − GD (z )k2

1
log ∗
σ

1

1
log ∗
σ

 22

α

;
α

.

Then for m ∈ {−N, −(N − 1) · · · , 0, 1, · · · , N }dz , we define


dx
Y
1

φm (x) =
ψ q
 1 1 (xi − GD,i (zm )) ,
√
1
1 α+2
1
∗
σ dx log σ∗ + c1 dz 2N log σ∗
i=1

|x| < 1
 1,
0,
2 < |x|
where ψ(x) =
and xi , GD,i (zm ) denote the i-th dimension of x and

2 − |x|, 1 ≤ |x| ≤ 2
GD (zm ). For any z ∈ Bz , there exist a m ∈ {−N, −(N − 1) · · · , 0, 1, · · · , N }dz , such that
q

1 1
log σ1∗ dz
p
1
1 α+2
kz − zm k2 ≤
.
kGD (z) − GD (zm )k2 ≤ c1 dz
log ∗
2N
2N
σ
Therefore for any x ∈ Bx = {x = GD (z) + σ ∗ q
| z ∈ Bz ,  ∈ B }, there exists zm , such that
1 1
√ 1
1 α+2
∗
kx − GD (zm )k2 ≤ c1 dz 2N log σ∗
+ σ dx log σ1∗ . It follows that for any x ∈ Bx ,
Σ φm (x) ≥ 1. Moreover, by the fact that the support of φm (x) is
m

(

r

x : |xi − GD,i (zm )| ≤ 2(σ
We have Σ φm (x) . log σ1∗

p
1
1
dx log ∗ + c1 dz
σ
2N

∗

 2d2z + dz
α

α

m

Pm,j (x) =

+ (σ ∗ N )dz log σ1∗

 2d2z
α

X Dγ QD,j
γ!

γ:|γ|<k

)

1 1
1 α+2
log ∗
), ∀ 1 ≤ i ≤ dx .
σ
. Let

(x − GD (zm ))γ ,
x=GD (zm )

Qd x

Qx
with the usual conventions γ! = i=1 γ i , (x − GD (zm ))γ = di=1
(xi − GD,i (zm ))γk and QD,j (1 ≤
j ≤ dz ) being the jth dimension of QD . Now define an approximation to QD (x) by
Σ φm (x)Pm,j (x)
Q̃j (x) = m
;
Σ φm (x)
m

Q̃(x) = (Q̃1 (x), · · · , Q̃dz (x)).
We have for any x ∈ Bx and 1 ≤ j ≤ dz ,
|Q̃j (x) − QD,j (x)| ≤ |Σ φm (x)Pm,j (x) − Σ φm (x)QD,j (x)|
m

m

 2dz2+2 + dz +k + k

α
2
α
1
1
(1 + (σ ∗ N )dz )(σ ∗ + )k .
. log ∗
σ
N
36

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Furthermore, by the fact that x = max(x, 0) − max(−x, 0), one has for any feedforward ReLU
neural work with d input units, depth L, kU k1 computation units and W weights, it can be expressed
as a feedforward ReLU neural work in which information can only come from the previous one layer
with depth L, computation units at most 2L(kU k1 + d) and weights at most 4W + 2L(kU k1 + d).
Choose
!− 1
k
σ1
N 
.
 2dz2+2 + dz +k + k
α
2
α
1
log σ1
By the fact that
|x| = max(x, 0) + max(−x, 0),
max(0, min(1, x)) = max(− max(−x + 1, 0) + 1, 0),
and when x ≥ 1, f (x) = x1 is C ∞ , combined with lemma 22, lemma 23 and when x ∈ Bx ,
Σ φm (x) ≥ 1, we can conclude that there exist ReLU neural networks with depth O(log σ11 )

m

and weights and computation units at most O(N dz (log σ11 )) that approximate Q1 (x) with er 2dz + dz +k + k
α
2
ror at most log σ1∗ α2
(1 + (σ ∗ N )dz )(σ ∗ + N1 )k in domain Bx . Since k ≥ 2, we
can choose W1 , kU1 k1  N dz (log σ11 )2 , L1  log σ11 and a large enough constant b8 , such
that 0 ≤ 13 σ ∗ . Checking the proof of Lemma 22 and Lemma 23 (Theorem 1 and Proposition

 dz + dz +2
dz
αk
2
3 of Yarotsky (2017)), we can choose kU k1 , W  log σ11
(σ1 2 )− k ; kU2 k1 , W2 

 dz + dz +2
 c
dz
α(k−1)
2
log σ11
(σ1 )− k−1 ; L, L2  log σ11 ; V = σ11 with a large enough c and (b, b9 ) to
be large enough constants, such that 1 ≤ 31 σ ∗ 2 and 2 ≤ 13 σ ∗ .
## C.3.2. P ROOF OF L EMMA 18
To begin with, we state the following lemma in Anthony and Bartlett (1999) for bounding the
covering number of ReLU Neural networks.
Lemma 24 (Theorem 12.2 of Anthony and Bartlett (1999)) Assume for all f ∈ F, kf k∞ ≤ M .
Denote the pseudo-dimension of F as Pdim(F), then for n ≥ Pdim(F), we have for any  and any
X1 , . . . , Xn

  2eM · n Pdim(F )
.
N , F|X1 ,...,Xn , ∞ ≤
 · Pdim(F)
By the choice of µφ (x) and Σφ (x), we have µφ (x) ≤ logc0 σ11 (c1 kxk2 +c2 ) and 0 < c3 log−c0 σ11 σ12 ≤
λmin (Σφ (x)) ≤ λmax (Σφ (x)) ≤ 1 with some constants (c0 , c1 , c2 , c3 ). Also,
dx
1
log(
);
2
2πσ ∗ 2


Z
dx
(x − GD (z))T (x − GD (z))
πD (z)dz
− log pD (x) =
log(2πσ ∗ 2 ) − log exp −
2
2σ ∗ 2
Z
dx
kxk22
1
∗2
≤
log(2πσ ) + ∗ 2 + ∗ 2 kGD (z)k22 πD (z)dz.
2
σ
σ
log pD (x) ≤

We then state the following Lemma 25 for bounding the Orlicz norm in Assumption A.
37

(11)

TANG YANG

Lemma 25 Consider Fdd and Fed defined in equation (9), given Assumption B and Condition
B, there exists a constant C0 that only depend on (α, k, b2 , b3 , b5 , b6 , dz , dx ) in Assumption B and
Condition B, such that


1 2
C0
2
α
.
sup
(|log pθ,β (x)| + DKL (qφ (·|x)||pθ,β (·|x))) ≤ 2 kxk2 + (log )
σ1
σ1
pθ ∈Fdd ,qφ ∈Fed
πβ ∈Fprior

1

For any Gθ1 (z) ∈ Fddzx (L, U, W, b(log σ11 ) α , V ) with U = (u1 , · · · , uL−2 ), it can be expressed
as a fully-connected ReLU neural network with depth L, computation units kU k1 , andPFrobenius
norm of weights in each layer at most V kU k1 . We use θ1F to denote the (dz + 1)u1 + L−3
l=1 (ul +
1)ul+1 + dx (uL−2 + 1) dimensional weights vector of Gθ1 (z) after expressed as a fully-connected
ReLU neural network, then it can only has at most W -number of nonzero elements. Consider
1
1
Bx = [−c1 log α n, c1 log α n]dx such that pD (x ∈
/ Bx ) ≤ n12 . Next we state a lemma about the
lipschitzness of m(pθ , πβ , qφ , x) on Bx .
Lemma 26 Consider Fdd and Fed defined in (9), given Assumption B and condition B, there
exist some constants (c0 , c1 ) that only depend on (α, k, b2 , b3 , b5 , b6 , dz , dx ) in Assumption B and
Condition B, such that for any x ∈ Bx , (pθ , pθ0 ) ∈ Fdd , (qφ , qφ0 ) ∈ Fed and (πβ , πβ 0 ) ∈ Fprior ,
m(pθ , πβ , qφ , x) − m(pθ0 , πβ 0 , qφ0 , x)
1
1 √
1
0
≤ c2 logc3 n c4
L(kU k1 V )L−2 kθ1F − θ1F k2 + kβ − β 0 k2 + 2 − 02
σ1
σ
σ

+ (kU k1 V )L−1 (kµφ (x) − µφ0 (x)k2 + kΣφ (x) − Σφ0 (x)kF ) .
Therefore by
Σφ (x) − Σφ0 (x)

−1
d
T d
2
2
= σ̄ Gφ2 (Qφ1 (x)) Gφ2 (Qφ1 (x)) + σ̄ Idz
−1

2
− σ̄ 2 Gdφ0 (Qφ01 (x))T Gdφ0 (Qφ01 (x)) + σ̄ 0 Idz
2
2
−1

2
+ σ̄ 2 Gdφ0 (Qφ01 (x))T Gdφ0 (Qφ01 (x)) + σ̄ 0 Idz
2
2

−1
2
2
− σ̄ 0 Gdφ0 (Qφ01 (x))T Gdφ0 (Qφ01 (x)) + σ̄ 0 Idz
.
2

2

And by the fact that
kA−1 − A0

−1

kF = kA0

−1

## A0 A−1 − A0

−1

= kA0

−1

(A0 − A)A−1 kF

≤ kA0

−1

kF kA0 − AkF kA−1 kF .

AA−1 kF

We can get that there exists a constant c0 such that,
kΣφ (x) − Σφ0 (x)kF .

logc0 σ11 
σ12


kGdφ2 (Qφ1 (x)) − Gdφ0 (Qφ01 (x))kF + |σ̄ 2 − (σ̄ 0 )2 | .
2

38

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Moreover,
kµφ (x) − µ0φ (x)k2
1
(kΣφ (x) − Σφ0 (x)kF + kGdφ2 (Qφ1 (x)) − Gdφ0 (Qφ01 (x))kF )
2
σ1

1

≤ kQφ1 (x) − Qφ01 (x)k2 + log α n logc0
+ kGφ3 (Qφ1 (x)) − Gφ03 (Qφ01 (x))k2 .

So we can obtain that under Bx , there exist some constant (c5 , c6 , c7 ) such that
m(pθ , πβ , qφ , x) − m(pθ0 , πβ 0 , qφ0 , x)
√
1 
0
≤ c5 logc6 n c7 kβ − β 0 k2 + L(kU k1 V )L−1 kθ1F − θ1F k2 + (kU k1 V )L kQφ1 (x) − Qφ01 (x)k2
σ1

1 
1
+ kGφ3 (Qφ1 (x)) − Gφ03 (Qφ01 (x))k2 + kGdφ2 (Qφ1 (x)) − Gdφ0 (Qφ01 (x))kF + |σ̄ 2 − (σ̄ 0 )2 | + 2 − 02 .
2
σ
σ
Denote ΘFθ1 as the parameter space of θ1F , it holds that
n
o
PL−3
1
ΘFθ1 ⊆ θ1F ∈ R(dz +1)u + l=1 (ul +1)ul+1 +dx (uL−2 +1) | kθ1F k0 ≤ W, kθ1F k∞ ≤ V .
1

1

k1
So one has log N(ΘFθ1 , `2 , ) . W log V LkU
. Recall Bx = [−c1 log α n, c1 log α n]dx , we have



P


[

{xi ∈ Bxc } ≤

1≤i≤n

1
1
n= .
2
n
n

Moreover, by Lemma 25, for any x ∈ Bx , it holds that
2

sup
pθ ∈Fdd ,qφ ∈Fed
πβ ∈Fprior

|m(pθ , qφ , πβ , x) − log pD (x)| .

(log σn1 ) α
σ12

;

2

sup |g(x)| .
g∈G

∗

(log σn1 ) α
σ12

.

Then, by changing the set A to Bx in the proof of Lemma 13, we can get


EpD (x)  sup

∗
g∈G
kgk2 ≤δ

n
1X

n

∗
g∈G
kgk2 ≤δ


g(xi ) − EpD (x) g(x) 

i=1



≤ EpD (x)  sup



1
n



n
X

n

2

(log σ1 ) α

g(xi )1Bx (xi ) − EpD (x) (g(x)1Bx (x))  + C
.
nσ12
i=1
39

TANG YANG

Therefore by lemma 25, lemma 26 and lemma 24, like the proof of Theorem 3, we should choose
r

δn 

W + dβ + Pdim(Gdφ2 (Qφ1 (x))) + Pdim(Qφ1 (x)) + Pdim(Gφ3 (Qφ1 (x)))

r
n 2
1 1 (log σ1 ) α
.
(log n + L log(kU k1 V ) + log )
σ1 n
σ12
Furthermore, for the Hard Tanh function h(x) = max(−b, min(b, x)), it can be express as h(x) =
σ(−σ(−x + b) + 2b) − b with σ(x) = max(x, 0). Then, by Theorem 6 of Bartlett et al. (2019), we
have
Pdim(Gdφ2 (Qφ1 (x))) = O((W1 + W2 )(L1 + L2 ) log(kU1 k1 + kU2 k1 ));
Pdim(Qφ1 (x)) = O(W1 L1 log kU1 k1 );
Pdim(Gφ3 (Qφ1 (x))) = O((W + W1 )(L + L1 ) log(U + kU1 k1 )).
We then bound the approximation error in the following lemma.
Lemma 27 Consider Fdd , Fed defined in (9) and Fprior satisfying Condition B, given Assumption
B, there exist some constants (η, γ, η, b7 , c) that only depend on (dz , dx ) and (α, k, b2 , b3 , b5 , b6 ) in
1
Assumption B and Condition B, such that when σ0∗ + σ∗2
+ σ2∗ ≤ 1,
min

pθ ∈Fdd ,qφ ∈Fed
πβ ∈Fprior

DKL (pD (·)||pθ,β (·)) + EpD (x) [DKL (qφ (·|x)||pθ,β (·|x))]

2
 28+10α+3α

α2
1
∗2
,
≤ cσ
log ∗
σ





with (0 , 1 , 2 ) being defined in equation (7).
We can then get the desired conclusion using Theorem 1.
C.4. Nonparametric Models
## C.4.1. P ROOF OF L EMMA 19 AND L EMMA 20
v
u n
u1 X
t
m(p, q, πβ , xi ) − m(p0 , q 0 , πβ 0 , xi ))2
n
i=1

p(x)
≤ sup log 0
+ sup DKL (q(·|x)||p(·|x)) − DKL (q 0 (·|x)||p0 (·|x)) .
p (x)
x
x
For the first term of equation (12), one has
p(x|z)πβ (z)
p0 (x)sup 0
z p (x|z)πβ 0 (z)
Z
p(x|z)πβ (z)
=
p0 (x|z)sup 0
πβ 0 (z)dz
z p (x|z)πβ 0 (z)
Z
Z
p(x|z)πβ (z)
≥
p0 (x|z) 0
πβ 0 (z)dz
p
(x|z)πβ 0 (z)
Z
= p(x).
40

(12)

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

p0 (x|z)π 0 (z)

0

(x)
Similarly, it holds that pp(x)
≤ sup p(x|z)πββ (z) . Therefore when pp(x)
0 (x) ≥ 1,
z

log

p(x|z)πβ (z)
p(x)
p(x)
= log 0
≤ log sup 0
0
p (x)
p (x)
z p (x|z)πβ 0 (z)
≤ sup log p(x|z) − log p0 (x|z) + sup log πβ (z) − log πβ 0 (z) .
z

z

Similarly, when pp(x)
0 (x) ≤ 1,
log

p0 (x|z)πβ 0 (z)
p(x)
≤
log
sup
p0 (x)
z p(x|z)πβ (z)
≤ sup log p(x|z) − log p0 (x|z) + sup log πβ (z) − log πβ 0 (z) .
z

z

For the second term of equation (12),
sup DKL (q(·|x)||p(·|x)) − DKL (q 0 (·|x)||p0 (·|x))
x
Z
Z
q(z|x)
q(z|x)
log
≤ sup
q(z|x)dz −
log 0
q(z|x)dz
p(z|x)
p (z|x)
x
Z
Z
Z
Z
q(z|x)
q 0 (z|x) 0
+ sup
log 0
q(z|x)dz −
log 0
q (z|x)dz .
p (z|x)
p (z|x)
x
Z
Z

(13)

Then for the first part of equation (13),
p0 (z|x)
q(z|x)dz
p(z|x)
x
Z
p0 (x|z)p0 (x)
≤ sup log
+ sup log πβ (z) − log πβ 0 (z)
p(x|z)p(x)
x,z
z
Z

sup

log

≤ 2sup log p(x|z) − log p0 (x|z) + 2sup log πβ (z) − log πβ 0 (z) .
x,z

z

For the second part of equation (13),
Z
q(z|x) q(z|x) 0
q 0 (z|x) q 0 (z|x) 0
log 0
p
(z|x)dz
−
log 0
p (z|x)dz
0
p (z|x) p (z|x)
p (z|x) p0 (z|x)
x
Z
Z
Z
q(z|x) q(z|x)
q 0 (z|x) q 0 (z|x) 0
log 0
≤ sup
p (z|x)dz
−
log
p (z|x) p0 (z|x)
p0 (z|x) p0 (z|x)
x
Z
Z
q(z|x)
q 0 (z|x) 0
≤
sup sup(1 + | log p(z|x)| + | log q(z|x)|) · sup
−
p (z|x)dz
0
p0 (z|x)
p∈Fdd ,q∈Fed x,z
x
Z p (z|x)
πβ ∈Fprior
Z
≤ (C + 1)sup
q(z|x) − q 0 (z|x) dz.
Z

sup

x

Z

41

TANG YANG

Then by x log x ≥ x − 1
Z

q(z|x) − q 0 (z|x) dz

Z 
q(z|x)
=
− 1 1(q(z|x) ≥ q 0 (z|x))q 0 (z|x)dz
0 (z|x)
q

ZZ  0
q (z|x)
− 1 1(q 0 (z|x) ≥ q(z|x))q(z|x)dz
+
q(z|x)
Z
Z
Z
q 0 (z|x)
q(z|x)
q(z|x) 0
q 0 (z|x)
q
(z|x)dz
+
q(z|x)dz
≤
log
log
0
0
q (z|x)
q(z|x)
Z q(z|x)
Z q (z|x)
≤ 2sup log q(z|x) − log q 0 (z|x) .
Z

z

We then get the desired conclusion in Lemma 19.
P

P 1
k1
For Lemma 20, since p(x|z) ∝ exp
l
(x
,
z)
, then we can write log p(x|z) as kj=1
lj (xj , z)−
j
j
j=1
R
Pk1
C(x), with C(x) = log Z exp( j=1 lj (xj , z))dz. By the same argument of the proof of Lemma 19,
we have
R
P 1
Pk1
lj (xj , z))
exp( kj=1
Z exp( j=1 lj (xj , z))dz
≤ sup
R
Pk1 0
Pk1 0
z exp( j=1 lj (xj , z))
Z exp( j=1 lj (xj , z))dz
R
Pk1
k1
k1
X
X
Z exp( j=1 lj (xj , z))dz
log R
≤ sup
lj (xj , z) −
lj0 (xj , z) .
Pk1 0
z
l
exp(
(x
,
z))dz
j=1 j j
j=1
j=1
Z
So we have sup| log p(x|z) − log p0 (x|z)| ≤ 2sup
x,z

Pk1

x,z

j=1 lj (xj , z) −

Pk1

0
j=1 lj (xj , z) . Similarly for

the case of q(z|x).
C.5. Proof of additional lemmas
## C.5.1. P ROOF OF L EMMA 21
D (x)
, then y ∈ [e−C , eC ].
Let y = pp(x)

f (y) = (2 + C)(y log y − y + 1) − y(log y)2 .
f 0 (y) = (C − log y) log y.
When 1 ≤ y ≤ eC , f 0 (y) > 0. When e−C ≤ y < 1, f 0 (y) < 0. Since f (1) = 0, when
y ∈ [e−C , eC ]), it holds that f (y) ≥ 0.
## C.5.2. P ROOF OF L EMMA 25
R
For pθ,β (x) = pθ (x|z)πβ (z)dz, define
Aθ,β = {x : pθ,β (x) > 1}.
42

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

Then for any x ∈ Aθ,β ,
Z
| log pθ,β (x)| = log pθ,β (x) = log
Z 
= log
Z 
≤ log
≤−

pθ (x|z)πβ (z)dz

1
2πσ 2

 dx

1
2πσ 2

 dx

Pdx

2

exp −

2
j=1 (xj − Gθ,j (z))
2σ 2

!
πβ (z)dz

2

πβ (z)dz

dx
log(2πσ12 ),
2
Z

DKL (qφ (·|x)||pθ,β (·|x)) =

log

qφ (z|x)pθ,β (x)
qφ (z|x)dz
pθ (x|z)πβ (z)

Z
=

log qφ (z|x)qφ (z|x)dz + log pθ,β (x)
Z
Z
− log pθ (x|z)qφ (z|x)dz − log πβ (z)qφ (z|x)dz.
For any x ∈ Acθ,β ,
| log pθ,β (x)| + DKL (qφ (·|x)||pθ,β (·|x))
Z
= − log pθ (x|z)qφ (z|x)dz + DKL (qφ (·|x)||πβ (·))
Z
Z
Z
= log qφ (z|x)qφ (z|x)dz − log pθ (x|z)qφ (z|x)dz − log πβ (z)qφ (z|x)dz,
Z

Z
−

dz
1
log qφ (z|x)qφ (z|x)dz = − log |Σφ (x)| − (1 + log(2π)),
2
2

dx
log pθ (x|z)qφ (z|x)dz =
log(2πσ 2 ) +
2
≤

Z Pdx

2
j=1 (xj − Gθ,j (z))
qφ (z|x)dz
2σ 2


Z
dx 
dx
1 X
x2j + G2θ,j (z)qφ (z|x)dz .
log(2π) + 2
2
σ1
j=1

By the definition of Fdd and Fed in (9) and Condition B, there exists a constant c such that
Z
1 2
kGθ (z)k22 qφ (z|x)dz ≤ c(log ) α ;
σ1
Z
1
log πβ (z)qφ (z|x)dz ≤ c log .
σ1
Then by the fact that when σ1 ≤ 1, log σ12 ≤ σ12 , we can get the desired conclusion.
1

1

43

TANG YANG

## C.5.3. P ROOF OF L EMMA 26
We begin the proof with the following lemma about the Lipschitzness of ReLU neural networks (w.r.t
the parameter).
Lemma 28 If Gθ1 (z) is ReLU neural network in which the information of each layer can only come
from the previous one layer. Also, it has L layers, use Hard Tanh as the activation function for the
output and there exists a constant V ≥ 2 such that in each layer, the units ω has kωk2 ≤ V , then,
for any Gθ1 (z) and Gθ10 (z),
√
kGθ1 (z) − Gθ10 (z)k2 ≤ V L−2 (2 + kzk2 ) 2Lkθ1 − θ10 k2 .
We then return to our proof of Lemma 26. For any x ∈ Bx ,
|m(pθ , qφ , πβ , x) − m(pθ0 , qφ0 , πβ 0 , x)|
Z
Z
pθ (x|z)
≤
log
qφ (z|x)dz +
log pθ0 (x|z)(qφ (z|x) − qφ0 (z|x))dz
pθ0 (x|z)
Z
Z
+
log qφ (z|x)qφ (z|x)dz − log qφ0 (z|x)qφ0 (z|x)dz
Z
Z
+
log πβ (z)qφ (z|x)dz − log πβ 0 (z)qφ0 (z|x)dz .

(14)

For the first term of equation (14), since in each layer of Gθ1 (z), the weights w has kwkF ≤ V kU k1 .
Then by Lemma 28 and the boundedness of µφ (x) and Σφ (x), we have
Z
pθ (x|z)
log
qφ (z|x)dz
pθ0 (x|z)
Z
dx G2 (z) − G2 (z)
1 X
θ1 ,j
θ10 ,j
≤
+ xj (Gθ10 ,j (z) − Gθ1 ,j (z)) qφ (z|x)dz
σ2
2
j=1
Z Pdx
2
1
1
1
dx
1
j=1 (xj − Gθ10 ,j (z))
qφ (z|x)dz
log 2 − log 02 + 2 − 02
+
2
σ
σ
σ
σ
2



Z
1
1
n 2 1
1
≤ 2
kGθ1 ,j (z) − Gθ10 ,j (z)k2
kGθ1 ,j (z) + Gθ10 ,j (z)k2 + kxk2
qφ (z|x)dz + c(log ) α 2 − 02
2
σ1
σ
σ
σ1
√
2
L(log σn1 ) α
n 2 1
1
(kU k1 V )L−2 kθ1 − θ10 k2 + (log ) α 2 − 02 .
.
2
σ1
σ
σ
σ1
For the second term of equation (14),
Z
log pθ0 (x|z)(qφ (z|x) − qφ0 (z|x))dz
1
= 02
σ

Z

1
≤ 02
σ

Z

Pdx
−

2
j=1 (xj − Gθ10 ,j (z))

2

(qφ (z|x) − qφ0 (z|x))dz

Pdx
−

2
j=1 Gθ10 ,j (z) − 2xj Gθ10 ,j (z)

2
44

(qφ (z|x) − qφ0 (z|x))dz .

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

By the fact that kGθ1 (z) − Gθ1 (z 0 )k2 ≤ (kU k1 V )L−1 kz − z 0 k2 , it holds that
Z
kGθ10 (z)k22 (qφ (z|x) − qφ0 (z|x))dz
Z
≤
inf
kGθ10 (z)k22 − kGθ10 (z0 )k22 dγx
γx ∈Π(qφ (·|x),qφ0 (·|x)) Rdz ×Rdz
Z
≤
inf
kGθ10 (z) − Gθ10 (z0 )k2 kGθ10 (z) + Gθ10 (z0 )k2 dγx
γx ∈Π(qφ (·|x),qφ0 (·|x)) Rdz ×Rdz
1 1
≤ c(kU k1 V )L−1 (log ) α W2 (qφ (·|x), qφ0 (·|x)),
σ1
where W2 (µ0 , µ1 ) denotes the Wasserstein-2 distance defined as (Santambrogio, 2015):
Z


2
2
W2 (µ0 , µ1 ) :=
inf
ky0 − y1 k22 dγ (y0 , y1 ) .
E kY0 − Y1 k =
inf
Y0 ∼µ0 ;Y1 ∼µ1

γ∈Π(µ0 ,µ1 ) Rdz ×Rdz

Similarly, we can get
Z X
dx

xj Gθ10 (z)(qφ (z|x) − qφ0 (z|x))dz

j=1
1

≤ c log α n(kU k1 V )L−1 W2 (qφ (·|x), qφ0 (·|x)).
Therefore,
Z
log pθ0 (x|z)(qφ (z|x) − qφ0 (z|x))dz
.

n 1
(kU k1 V )L−1
(log ) α W2 (qφ (·|x), qφ0 (·|x)).
σ1
σ12

Furthermore, by Givens and Shortt (1984), we have
W2 (qφ (·|x), qφ0 (·|x)) = µφ (x) − µφ0 (x)

1 !
 1
1
2
Σφ (x) + Σφ0 (x) − 2 Σφ2 (x)Σφ0 (x)Σφ2 (x)

2
+ Tr
2
1

2

1

= µφ (x) − µφ0 (x) 2 + kΣφ2 (x) − Σφ20 (x)U (x, φ, φ0 )k2F ,
1

1

−
−
where U (x, φ, φ0 ) = Σφ0 2 (x)Σφ 2 (x)

 1
1
1
2
2
2
Σφ (x)Σφ0 (x)Σφ (x) . Then let Σφ (x) = U S 2 U T and

Σφ0 (x) = V S12 V T be the eigenvalue decomposition of Σφ (x) and Σφ0 (x), we have
U (x, φ, φ0 ) = U S −1 U T V S1−1 V T U SU T V S12 V T U SU T

 21

.

By Davis-Kahan theorem (Davis and Kahan, 1970) and the boundedness of the eigenvalues of Σφ (x),
it holds with a constant c4 that
kI − U T V kF . σ1−c4 kΣφ (x) − Σφ0 (x)kF ;
kI − V T U kF . σ1−c4 kΣφ (x) − Σφ0 (x)kF .
45

TANG YANG

Then combine all these facts, we have
Z
log pθ0 (x|z)(qφ (z|x) − qφ0 (z|x))dz
. (kU k1 V )L−1

logc3 n
(kµφ (x) − µφ0 (x)k2 + kΣφ (x) − Σφ0 (x)kF ).
σ1c4

For the third term of equation (14),
Z
Z
log qφ (z|x)qφ (z|x)dz − log qφ0 (z|x)qφ0 (z|x)dz
=

1
1
log |Σφ (x)| − log Σφ0 (x)
2
2

. σ1−c4 kΣφ (x) − Σφ0 (x)kF .
For the last term of equation (14), by Condition B, we can get
| log πβ (z) − log πβ (z0 )| = ∇z log πβ (cz + (1 − c)z0 )(z − z0 )
≤ (c1 (kzk2 + kz0 k2 ) + c2 )kz − z0 k2 .
Therefore,
Z
| log πβ (z)qφ (z|x)dz − log πβ (z)qφ0 (z|x)dz| ≤
≤

inf
γx ∈Π(qφ (z|x),qφ0 (z|x)) Rd ×Rd

(c1 (kzk2 + kz0 k2 ) + c2 )kz − z0 k2 dγx



Z
Z
2c22 + 4c21 ( kzk22 qφ (z|x)dz + kzk22 qφ0 (z|x)dz
Z

×

inf
γx ∈Π(qφ (z|x),qφ0 (z|x)) Rd ×Rd

!1

2

|z − z0 |22 dγx

.

Then use the same strategy for bounding the second term of equation (14) and the fact that
| log πβ (z) − log πβ 0 (z)| ≤ (c3 kzkc25 + c4 )kβ − β 0 k2 , we have
Z
Z
log πβ (z)qφ (z|x)dz − log πβ 0 (z)qφ0 (z|x)dz
.

logc3 n
(kβ − β 0 k2 + kµφ (x) − µφ0 (x)k2 + kΣφ (x) − Σφ0 (x)kF ).
σ1c4

We can then get the desired conclusion.
## C.5.4. P ROOF OF L EMMA 27
Assume Q1 (x), G1 (z) and Gd1 (z) achieve the rate 0 , 1 and 2 , that is
max kQ1 (x) − QD (x)k2 = 0 ;

x∈Bx

max kG1 (z) − GD (z)k2 = 1 ;
z∈B z

max kGd1 (z) − ∇GD (z)kF = 2 .

z∈B z

46

(15)

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

2

By Assumption B, we have supkzk2 ≤r k∇GD (z)kF ≤ c5 r α +c6 and supkzk2 ≤r k∇QD (x)|x=GD (z) kF ≤
4

c5 r α2 + c6 . Moreover, by the fact that z = QD (GD (z)), we have Idz = ∇QD (x)|x=GD (z) ∇GD (z).
Then, for a fixed z ∈ B z , let ∇QD (x)T |x=GD (z) = U1 S1 V1T and ∇GD (z) = U2 S2 V2T be the
singular value decomposition of ∇QD (x)T |x=GD (z) and ∇GD (z), where U1 , U2 ∈ O(dx , dz ),
V1 , V2 ∈ O(dz ). Then it holds that S2−1 = V2T V1 S1 U1T U2 . We can thus obtain that when kzk2 ≤ r,
λmin (∇GD (z)T ∇GD (z)) ≥  1 8  for some constant a > 0. Given this fact, we define
a 1+r α2

Σ1 (x) = (Gd1 (Q1 (x))T Gd1 (Q1 (x)) + σ ∗ 2 Idz )−1 ;
Σ̃1 (x)i,j = max(−b̄7 , min(b̄7 , Σ1 (x)i,j ))

(1 ≤ i, j ≤ dx , b̄7 = b7 (log

1 42
) α );
σ∗

µ1 (x) = Q1 (x) + Σ̃1 (x)Gd1 (Q1 (x))T (x − G1 (Q1 (x)));

(16)

02 = max kµ1 (x) − (Q1 (x) + Σ(x)∇GD (Q1 (x))T (x − GD (Q1 (x))))k2 ;
x∈Bx
0
3 = max kΣ1 (x)−1 − Σ(x)−1 kF ,
x∈Bx
in which Σ(x) is defined as (∇GD (Q1 (x))T ∇GD (Q1 (x)))−1 with ∇GD (Q1 (x)) = ∇GD (z)|z=Q1 (x) .
Define


∗2

Z



p(x|z) ∼ N G1 (z), σ I , p(x) =


q(z|x) ∼ N µ1 (x), σ ∗ 2 Σ1 (x) ;
p(z|x) =

p(x|z)πD (z)dz;
(17)

p(x|z)πD (z)
.
p(x)

Consider z = Q1 (x) + (z 0 − Q1 (x))σ ∗ , define


µ1 (x) − Q1 (x)
q 0 (z 0 |x) ∼ N Q1 (x) +
,
Σ
(x)
;
1
σ∗

p0 (z 0 |x) = σ ∗ dz p z = Q1 (x) + (z 0 − Q1 (x))σ ∗ |x .
Since DKL is invariant to affine transformations, we have
DKL (q 0 (·|x)||p0 (·|x)) = DKL (q(·|x)||p(·|x)).
1

1

1

1

Recall that Bz = [−η log 2 σ1∗ , η log 2 σ1∗ ]dz and B = [−γ log 2 σ1∗ , γ log 2 σ1∗ ]dx , then by Lemma 25
2

and the assumption that kGD (z)k2 ≤ c3 kzk2α + c4 , we have for sufficient large η and γ, it holds that
Z
q 0 (z 0 |x)
EpD (x) log 0 0 q 0 (z 0 |x)dz 0
p (z |x)
Z Z Z
q 0 (z 0 |GD (z) + σ ∗ ) 0 0
=
log 0 0
q (z |GD (z) + σ ∗ )dz 0 πD (z)p()dzd
p (z |GD (z) + σ ∗ )
Z Z Z
q 0 (z 0 |GD (z) + σ ∗ ) 0 0
q (z |GD (z) + σ ∗ )dz 0 πD (z)p()dzd + σ ∗ 2 .
≤
log 0 0
p (z |GD (z) + σ ∗ )
B Bz
47

TANG YANG

Define x = GD (z) + σ ∗ , x = GD (z) and r = Q1 (x) + (z 0 − Q1 (x))σ ∗ . Then,
p0 (z 0 |x) = p(r|x)σ ∗ dz =

p(x|r)πD (r)σ ∗ dz
;
p(x)

πD (r) = πD (Q1 (x)) + σ ∗ ∇πD (az 0 )T (z 0 − Q1 (x)),
az 0 = Q1 (x) + cσ ∗ (z 0 − Q1 (x))
and

(c ∈ [0, 1]);

 dx



(x − G1 (r))T (x − G1 (r))
exp −
2σ ∗ 2


 dx

2
(x − GD (r))T (x − GD (r))
1
exp −
=
2πσ ∗ 2
2σ ∗ 2




(GD (r) − G1 (r))T (x − GD (r))
kGD (r) − G1 (r)k22
exp −
.
exp −
2σ ∗ 2
σ∗2


p(x|r) =

Let D = −

1
2πσ ∗ 2

2

T (x−G (r))
kGD (r)−G1 (r)k22
D
and E = − (GD (r)−G1 (r))
.
2σ ∗2
σ ∗2

GD (r) = GD (Q1 (x)) + ∇GD (Q1 (x))(z 0 − Q1 (x))σ ∗ + Rn (x, z 0 ).
Since for any z ∈ Bz and  ∈ B , it holds that x = GD (z) and x = x + σ ∗  belong to Bx . Then,
kx − GD (Q1 (x))k2 = kx − x + x − GD (QD (x)) + GD (QD (x)) − GD (Q1 (x))k2

1
2 1 1

1 α2 + α + 2
1 α
∗
+ σ log ∗
. 0 log ∗
σ
σ
 22 + 1 + 1

1 α α 2
.
. σ ∗ log ∗
σ
−1
Define Σ(x) = ∇GD (Q1 (x))T ∇GD (Q1 (x)) , we have

1
Σ(x)
2
p(x|r) = (2π)dz |Σ(x)| N (z0 , Q1 (x) + ∗ ∇GD (Q1 (x))T (x − GD (Q1 (x))), Σ(x))
σ

 dx


2
1
(x − GD (Q1 (x)))T (x − GD (Q1 (x)))
×
exp −
2πσ ∗ 2
2σ ∗ 2


(x − GD (Q1 (x)))T ∇GD (Q1 (x))Σ(x)∇GD (Q1 (x))T (x − GD (Q1 (x)))
× exp
2σ ∗ 2


(x − GD (Q1 (x)) − σ ∗ ∇GD (Q1 (x))(z 0 − Q1 (x))T
0
× exp
Rn (x, z )
σ∗2


Rn (x, z 0 )T Rn (x, z 0 )
× exp −
exp(D + E),
2σ ∗ 2
T
where N (z0 , Q1 (x) + Σ(x)
σ ∗ ∇GD (Q1 (x)) (x − GD (Q1 (x))), Σ(x)) is the corresponding normal

48

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

T
density with variable z0 , mean vector Q1 (x) + Σ(x)
σ ∗ ∇GD (Q1 (x)) (x − GD (Q1 (x))) and covariance
matrix Σ(x). Set

B=

C=

(x − GD (Q1 (x)))T ∇GD (Q1 (x))Σ(x)∇GD (Q1 (x))T (x − GD (Q1 (x)))
;
2σ ∗ 2
(x − GD (Q1 (x)))T (x − GD (Q1 (x)))
−
.
2σ ∗ 2

(x − GD (Q1 (x)) − σ ∗ ∇GD (Q1 (x))(z 0 − Q1 (x))T
Rn (x, z 0 )T Rn (x, z 0 )
0
R
(x,
z
)
−
n
σ∗2
2σ ∗ 2

Then,

1
Σ(x)
2
p(x|r) = (2π)dz |Σ(x)| N (z0 , Q1 (x) + ∗ ∇GD (Q1 (x))T (x − GD (Q1 (x))), Σ(x))
σ

 dx
2
1
exp(B) exp(C + D + E).
2πσ ∗ 2
R
We then bound p(x) = p(x|r)πD (r)dr with the following lemma.
Lemma 29 Given above notations in Section C.5.4 and α1 = α42 + α1 + 12 , there exist some constants
(c0 , c1 , c2 , c3 , c4 ), such that for any x ∈ Bx , it holds that
!!
!

2
2

1
1


1 α +3α1
1 α +α1
1 α +2α1
1
1 2 +α1
∗
∗
exp −c1 σ log ∗
+ 0 log ∗
exp −c2 ∗ log ∗
− c0 σ log ∗
σ
σ
σ
σ
σ
p(x)

≤

≤
1
((2π)dz |Σ(x)|) 2 πD (Q1 (x))exp(B)

 2 +3α1
 2 +2α1 !!

 1 +α1 !
1


α
α
α
1
1
1

1 2 +α1
1
∗
∗
σ log ∗
+ 0 log ∗
exp c2 ∗ log ∗
+ c0 σ log ∗
.
σ
σ
σ
σ
σ

1
2πσ ∗2

σ ∗ dz
exp c1

 dx
2

α
α
And there exists Az 0 = [−c3 log σ1∗ 1 , c3 log σ1∗ 1 ]dz , such that for any x ∈ Bx , it holds that
Z
p0 (z 0 |x)dz 0 ≤ σ ∗ 2 ;
Ac 0

Z z

q 0 (z 0 |x)dz 0 ≤ σ ∗ 2 ;

Ac 0
z

Z
log
Ac 0

q 0 (z 0 |x) 0 0
q (z |x)dz 0 ≤ σ ∗ 2 .
p0 (z 0 |x)

z

Given Lemma 29, we have
 0 0
2
q (z |x)
DKL (q (·|x)||p (·|x)) ≤
− 1 p0 (z 0 |x)dz 0 + 2σ ∗ 2
0 (z 0 |x)
p
Az 0



2
Z
q 0 (z 0 |x)
=
exp log 0 0
− 1 p0 (z 0 |x)dz 0 + 2σ ∗ 2 .
p (z |x)
Az 0
0

0

Z

49

TANG YANG

Since
log

q 0 (z 0 |x)
p0 (z 0 |x)
N

≤ log

+ log





1 (x)
z0 , Q1 (x) + µ1 (x)−Q
, Σ1 (x)
σ∗




T (x − G (Q (x))), Σ(x)
N z0 , Q1 (x) + Σ(x)
∇G
(Q
(x))
1
1
D
D
σ∗


T (x − G (Q (x))), Σ(x)
N z0 , Q1 (x) + Σ(x)
∇G
(Q
(x))
∗
1
1
D
D
σ
p0 (z 0 |x)

(18)

.

q

log σ1∗ , it holds
2
4
that λmin (∇GD (z)T ∇GD (z)) & (log σ1∗ )− α2 and λmax (∇GD (z)T ∇GD (z)) . log σ1∗ α , we can
obtain
4

1 α2
sup |log |Σ1 (x)| − log |Σ(x)|| . 3 log ∗
.
σ
x∈Bx

Then under Bx , for the first term of equation (18), by the fact that when kzk2 ≤

Recall the definition of 02 and 03 in equation (16). Combined with the fact that
sup
x∈Bx

02
1
T
(µ
(x)
−
Q
(x)
−
Σ(x)∇G
(Q
(x))
(x
−
G
(Q
(x))))
.
,
1
1
1
1
D
D
σ∗
σ∗
2

we can get

sup

log

x∈Bx
z0 ∈A 0
z

. 03





1 (x)
N z0 , Q1 (x) + µ1 (x)−Q
,
Σ
(x)
1
σ∗


T (x − G (Q (x))), Σ(x)
N z0 , Q1 (x) + Σ(x)
∇G
(Q
(x))
∗
1
1
D
D
σ

1
log ∗
σ

2α1

0
+ 2∗
σ



1
log ∗
σ

α1 + 2

α

.

For the second term of (18), since when x ∈ Bx , Q1 (x) ∈ B z , then for z 0 ∈ Az 0 and x ∈ Bx , we
have r = Q1 (x) + σ ∗ (z0 − Q1 (x)) ∈ B z given large enough η. And for x ∈ Bx and r ∈ B z , we
have
(x − GD (Q1 (x)) − σ ∗ ∇GD (Q1 (x))(z 0 − Q1 (x))T
Rn (x, z 0 )T Rn (x, z 0 )
0
R
(x,
z
)
−
n
σ∗2
2σ ∗ 2

2

2
1 α +3α1
1 α +2α1
∗
. σ log ∗
+ 0 log ∗
;
σ
σ
kGD (r) − G1 (r)k22
2
|D| =
≤ 1∗ 2 ;
2
∗
2σ
2σ

1
T
(GD (r) − G1 (r)) (x − GD (r))
1
1 α +α1
|E| =
. ∗ log ∗
.
σ
σ
2σ ∗ 2
|C| =

By the assumption that k∇ log πD (z)k2 ≤ c1 kzk2 + c2 , we have for any x ∈ Bx , z 0 ∈ Az 0 and
50

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

az 0 = Q1 (x) + cσ ∗ (z 0 − Q1 (x)) (c ∈ [0, 1]), it holds that
k∇πD (az 0 )k2
.
πD (Q1 (x))

r
log

1
.
σ∗

Then combined with Lemma 29, and the fact that x exp(x) ≤ ex when x ≤ 1. We can get that for
any z 0 ∈ Az 0 and x ∈ Bx ,


T (x − G (Q (x))), Σ(x)
∇G
(Q
(x))
N z0 , Q1 (x) + Σ(x)
∗
1
1
D
D
σ
log
p0 (z 0 |x)


2
2

1
1 α +3α1
1 α +2α1
1
1 α +α1
. σ log ∗
+ 0 log ∗
+ ∗ log ∗
.
σ
σ
σ
σ
∗

So finally, we have

4
2
4


1 α +6α1
1 α +2α1
1 α +2α1
21
0 22
DKL (q (·|x)||p (·|x)) . σ
log ∗
+ ∗ 2 log ∗
+ ∗ 2 log ∗
σ
σ
σ
σ
σ
 4 +4α1

4α1

1
1 α
2
.
+ 0 3 log ∗
+ 20 log ∗
σ
σ
0

0

∗2

Also, by Assumption C, we can choose a large enough b7 such that
b̄7 = b7 (log

1 42
) α ≥ max sup |Σ(x)i,j | ,
1≤i,j≤dz x∈Bx
σ1

−1
with Σ(x) = ∇GD (Q1 (x)) ∇GD (Q1 (x))
. So by the definition of µ1 (x) and Σ1 (x) in
eqaution (16), we have,


T

2

 10 3 1

1 α2 + α + 2
1 α2
∗
+ σ 2 log ∗
log ∗
;
σ
σ

1
1 α
0
3 . 2 log ∗
+ σ∗2.
σ

02 . 1

We then bound DKL (pD (·)||p(·)) with the following lemma.
Lemma 30 Given Assumption B and Condition B, there exists a constant c, such that

DKL (pD (·)||p(·)) ≤ c


1 42 +1+ α2
21
2
∗
(log ∗ ) α
+σ
,
σ
σ∗2

where p(x) is defined in equation (17).
We can then get the desired conclusion.
51

TANG YANG

## C.5.5. P ROOF FOR L EMMA 28
We first consider the case that the activation function of the output is an identity function. when
L = 2,
G2θ (z) = w1 z + b1 .
Then we have
kG2θ1 (z)k2 ≤ kb1 k2 + kw1 k2 kzk2 ≤ V (1 + kzk2 );
kG2θ1 (z) − G2θ0 (z)k2 ≤ kb1 − b01 k2 + kw1 z − w10 zk2
1

≤ (2 + kzk2 )(kw1 − w10 k2 + kb1 − b01 k2 )).
If it’s hold for k-depth ReLU neural network that,
kGkθ1 (z)k2 ≤ V k−1 (1 + kzk2 ) +

k−2
X

V j;

j=1

kGkθ1 (z) − Gkθ0 (z)k2 ≤ V k−2 (2 + kzk2 )

k−1
X

1

(kwj − wj0 k2 + kbj − b0j k2 ).

j=1

Then,
k
kGk+1
θ1 (z)k2 ≤ kwk+1 σ(Gθ1 (z))k2 + kbk+1 k2


≤ kbk+1 k2 + kwk+1 kF V k−1 (1 + kzk2 ) +

k−2
X


V j

j=1

≤ V k (1 + kzk2 ) +

k−1
X

Vj

j=1
k

≤ V (2 + kzk2 );
k+1
kGk+1
θ1 (z) − Gθ0 (z)k2
1

0
σ(Gkθ0 (z))k2 + kbk+1 − b0k+1 k2
≤ kwk+1 σ(Gkθ1 (z)) − wk+1
1
0
≤ kwk+1 − wk+1
kF kGkθ1 (z)k2 + kbk+1 − b0k+1 k2


k−1
X
0
+ kwk+1
kF V k−2 (2 + kzk2 )
(kwj − wj0 k2 + kbj − b0j k2 )
j=1

≤ V k−1 (2 + kzk2 )

k
X

(kwj − wj0 k2 + kbj − b0j k2 )

j=1

≤V

k−1

√
(2 + kzk2 ) 2kkθ − θ0 k2 .

Furthermore, by the fact that for h(x) = max(−b1 , min(b1 , x)), it holds that
|h(x)| ≤ |x|;
|h(x) − h(x0 )| ≤ |x − x0 |,
the desired conclusion also holds for the case that the activation function of the output is h(x).
52

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

## C.5.6. P ROOF OF L EMMA 29
Set r = Q1 (x) + σ ∗ (z 0 − Q1 (x)) then
Z
p(x) = p(x|z = r)πD (z = r)dr
Z
= σ ∗ dz p(x|r)(πD (Q1 (x)) + σ ∗ ∇πD (az 0 )T (z 0 − Q1 (x)))dz 0 .
By the assumptions on πD (z) and the fact that kx − GD (Q1 (x))k2 . σ ∗ log σ1∗
exist some constants (c0 , c1 ) such that for any x ∈ Bx ,

 22 + 1 + 1
α

α

1
1
≤ exp(c0 log ∗ );
πD (Q1 (x))
σ
2!

4
1
1 α2 +1+ α
,
≤ exp c1 log ∗
exp(B)
σ
where recall that
B=

(x − GD (Q1 (x)))T ∇GD (Q1 (x))Σ(x)∇GD (Q1 (x))T (x − GD (Q1 (x)))
2σ ∗ 2
(x − GD (Q1 (x)))T (x − GD (Q1 (x)))
.
−
2σ ∗ 2

Let

 22 + 1 + 1
 22 + 1 + 1 #dz


α
2
α
2
α
α
1
1
;
Bz1 = −c2 log ∗
, c2 log ∗
σ
σ

 d



1 α1
1 α1 z
1
Az 0 = −c3 log ∗
, c3 log ∗
;
σ
σ

A2z 0 = z 0 | r = Q1 (x) + σ ∗ (z 0 − Q1 (x)) ∈ Bz1 .
"

For sufficiently large c2 , we have ∀x ∈ Bx ,
Z
p(x|z = r)πD (z = r)dr
(Bz1 )c


≤
≤σ
Under z0 ∈ A1,c
z0

T

1
2πσ ∗ 2


∗2

 dx
2

1
2πσ ∗ 2

σ

∗ dz

 dx
2

πD (z ∈ (Bz1 )c ) exp



1
dz log ∗
σ

σ ∗ dz πD (Q1 (X)) exp(B).

A2z 0 , for any x ∈ Bx , we have
GD (r) = GD (Q1 (x)) + ∇GD (bz 0 )(z 0 − Q1 (x))σ ∗ ,
bz 0 = Q1 (x) + cσ ∗ (z 0 − Q1 (x)) c ∈ [0, 1].
53

2

, there

TANG YANG

So there exists a constant a, such that


1
(z − Q1 (x)) ∇GD (bz 0 ) ∇GD (bz 0 )(z − Q1 (x)) ≥ a log ∗
σ
0

T

T

0

− 42
α

kz 0 − Q1 (x)k22 .

Then, by the fact that
(x − G1 (r))T (x − G1 (r))
=(x − GD (Q1 (x)) − ∇GD (bz 0 )(z 0 − Q1 (x))σ ∗ + (GD (r) − G1 (r)))T
(x − GD (Q1 (x)) − ∇GD (bz 0 )(z 0 − Q1 (x))σ ∗ + (GD (r) − G1 (r)).
We have for large enough A1z0 , there exists a constant c4 such that for any x ∈ Bx ,
σ

∗ dz

Z
T 2
A1,c
A 0
z0
z

≤

p(x|r)π(r)dz 0

p(x|r = Q1 (x) + σ ∗ (z 0 − Q1 (x)))

sup
T 2
A1,c
A 0
z0
z

∗ 2 ∗ dz

≤ c4 σ σ



1
2πσ ∗ 2

 dx
2

πD (Q1 (x)) exp(B).

Then, we only need to bound
Z
p(x|r)(π(Q1 (x)) + σ ∗ ∇π(az 0 )T (z 0 − Q1 (x)))dz 0 .
σ ∗ dz
A1 0
z

We first bound
σ

∗ dz

Z
A1 0

p(x|r)σ ∗ ∇π(az 0 )T (z 0 − Q1 (x))dz 0 .

z

By the assumption that k∇ log πD (z)k2 ≤ c1 kzk2 + c2 , we have for any x ∈ Bx , z 0 ∈ A1z 0 and
az 0 = Q1 (x) + cσ ∗ (z 0 − Q1 (x)) (c ∈ [0, 1]),
k∇πD (az 0 )k2
= k∇ log πD (az 0 )k2 exp(log πD (az 0 ) − log πD (Q1 (x)))
πD (Q1 (x))
r
1
. log ∗ .
σ
And using the fact that

1
Σ(x)
2
p(x|z = r) = (2π)dz |Σ(x)| N (z0 , Q1 (x) + ∗ ∇GD (Q1 (x))T (x − GD (Q1 (x))), Σ(x))
σ

 dx
2
1
exp(B) exp(C + D + E),
2
∗
2πσ
54

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

with
(x − GD (Q1 (x)) − σ ∗ ∇GD (Q1 (x))(z 0 − Q1 (x))T
Rn (x, z 0 )T Rn (x, z 0 )
0
R
(x,
z
)
−
;
n
σ∗2
2σ ∗ 2
kGD (r) − G1 (r)k22
;
D=−
2σ ∗ 2
(GD (r) − G1 (r))T (x − GD (r))
E=−
.
σ∗2

C=

We could then obtain,
Z
p(x|r) z 0 − Q1 (x) 2 dz 0
A1 0
z

 dx
2
1
. (2π) |Σ(x)|
exp(B) exp c1
2
2πσ ∗
!

1

1
1 α +α1
1 α1
× exp c2 ∗ log ∗
log ∗
.
σ
σ
σ


1 
2

dz

!!

2

2
1 α +3α1
1 α +2α1
σ log ∗
+ 0 log ∗
σ
σ
∗

Then we have,
−σ

∗



1
log ∗
σ

σ ∗ dz

 1 +α1
2

T 0
0
∗
A10 p(x|r)σ ∇πD (az 0 ) (z − Q1 (x))dz

R

z

.

1

1
2πσ ∗2

((2π)dz |Σ(x)|) 2

Next we bound
σ

∗ dz

Z
A1 0


1
1 2 +α1
.
. σ log ∗
 dx
σ
d
∗
2
z
exp(B)σ π (Q (x))
D

∗

1

p(x|r)πD (Q1 (x))dz 0 .

z

Since for sufficient large A1z 0 , we have
Z
A1 0

N (Q1 (x) +

Σ(x)
∇GD (Q1 (x))T (x − GD (Q1 (x))), Σ(x)) ≥ 1 − σ ∗ 2 .
σ∗

z

We could then obtain

 2 +3α1
 2 +2α1 !!

 1 +α1 !
α
α
α
1
1

1
1
exp −c1 σ ∗ log ∗
+ 0 log ∗
exp −c2 ∗ log ∗
(1 − σ ∗ 2 )
σ
σ
σ
σ
R
σ ∗ dz A1 p(x|r)πD (Q1 (x))dz 0
z0
.
 dx
1
((2π)dz |Σ(x)|) 2 2πσ1 ∗2 2 exp(B)σ ∗ dz πD (Q1 (x))
!!
!
2

2

1

1 α +3α1
1 α +2α1
1
1 α +α1
∗
. exp c1 σ log ∗
+ 0 log ∗
exp c2 ∗ log ∗
.
σ
σ
σ
σ


55

TANG YANG

Then by the fact that
σ

Z

∗ dz

A1 0
z

p(x|r)(πD (Q1 (x)) + σ ∗ ∇πD (az 0 )T (z 0 − Q1 (x)))dz 0

≤ p(x) ≤ σ ∗ dz

Z
A1 0
z

p(x|r)(πD (Q1 (x)) + σ ∗ ∇πD (az 0 )T (z 0 − Q1 (x)))dz 0

Z
+

c
Bz

p(x|z = r)πD (z = r)dr + σ

∗ dz

Z
T 2
A 0
A1,c
z0
z

p(x|r)πD (r)dz 0 .

We could then get the conclusion of the first part of the lemma. For the second part of the lemma,
since
R
0
Z
Ac 0 p(x|z = r)πD (z = r)dz
0 0
0
z
p (z |x)dz = R
,
p(x|z = r)πD (z = r)dz 0
Ac 0
z

we can get the desired conclusion using the same strategy of the proof of the first part of the lemma.

## C.5.7. P ROOF OF L EMMA 30
Since
dx
1
log(
);
2
2πσ ∗ 2


Z
dx
(x − G1 (z))T (x − G1 (z))
∗2
− log p(x) =
log(2πσ ) − log exp −
πD (z)dz
2
2σ ∗ 2
Z
kxk2
dx
1
log(2πσ ∗ 2 ) + ∗ 22 + ∗ 2 kG1 (z)k22 πD (z)dz,
≤
2
σ
σ
log pD (x) ≤

1

(19)

1

where the last inequality is due to Jensen inequality. So for Bz = [−η(log σ1∗ ) 2 , η(log σ1∗ ) 2 ]dz ,
1
1
B = [−γ(log σ1∗ ) 2 , γ(log σ1∗ ) 2 ]dx and Bx = {GD (z) + σ ∗ , z ∈ Bz ,  ∈ B }, if η and γ are large
enough, by the assumption that 1 ≤ σ ∗ 2 , we have
Z
log
Bxc

pD (x)
pD (x) − pD (x) + p(x)dx ≤ σ ∗ 2 .
p(x)

Also, there exists a constant c such that when x ∈ Bx , it holds that


1
pD (x) & exp −c log ∗ ;
σ


1
p(x) & exp −c log ∗ .
σ
56

## O N E MPIRICAL BAYES VARIATIONAL AUTOENCODER : A N E XCESS R ISK B OUND

1

1

We then consider a compact set of  and z: B̃ = [−c̄1 (log σ1∗ ) 2 , c̄1 (log σ1∗ ) 2 ]dx and B̃z =
1
1
[−c̄2 (log 12 ) α , c̄2 (log σ1∗ ) 2 ]dz with B̃z ⊂ B z . we can obtain
DKL (pD (·)||p(·))

Z 
pD (x) pD (x) pD (x)
−
+ 1 p(x)dx
=
log
p(x) p(x)
p(x)

2
Z
pD (G1 (z) + σ ∗ )
≤
− 1 πD (z)p()dzd
T
T
p(G1 (z) + σ ∗ )
B̃z B̃ Bx


Z
pD (G1 (z) + σ ∗ ) pD (G1 (z) + σ ∗ ) pD (G1 (z) + σ ∗ )
log
−
+ 1 πD (z)p()dzd
+
T
T
p(G1 (z) + σ ∗ ) p(G1 (z) + σ ∗ )
p(G1 (z) + σ ∗ )
B̃z B̃c Bx


Z
pD (G1 (z) + σ ∗ ) pD (G1 (z) + σ ∗ ) pD (G1 (z) + σ ∗ )
log
+
−
+ 1 πD (z)p()dzd
T
p(G1 (z) + σ ∗ ) p(G1 (z) + σ ∗ )
p(G1 (z) + σ ∗ )
B̃zc Bx
+ σ∗2.
(20)
Where we also reserve the notation Bx to be the set {(z, ) | x = G1 (z) + σ1  ∈ Bx }.
For the second and third part of equation (20), by (1)  is gaussian noise with mean 0 and identity covariance; (2) for Z ∼ πD (z), max kZ j kψ2 is bounded; (3) when x ∈ Bx , pD (x) &
1≤j≤dz


exp −c log σ1∗ and p(x) & exp −c log σ1∗ . we can get that when (c̄1 , c̄2 ) are large enough, the
second and third part of equation (20) can be upper bounded by σ ∗ 2 .
For the first part of equation (20), since
pD (G1 (z) + σ ∗ )
p(G1 (z) + σ ∗ )


R
∗
0 T (G (z)+σ ∗ −G (z 0 ))
1
D
πD (z 0 )dz 0
exp − (G1 (z)+σ −GD (z ))
∗2
2σ


.
=R
∗
0 T (G (z)+σ ∗ −G (z 0 ))
1
1
0 )dz 0
π
(z
exp − (G1 (z)+σ −G1 (z ))
D
2σ ∗2
We first consider the numerator, define
"
Bσ∗ (z, c̄3 ) = z − c̄3 σ

∗



1
log ∗
σ

 22 + 1
α

2

#
2 1

1 α2 + 2
1dz , z + c̄3 σ log ∗

1dz .

σ
∗

Therefore by the fact that under B z , kGD (z) − GD (z 0 )k22 ≥ a log σ1∗
GD (z)k2 ≤ 1 and (a − b)2 ≥ 12 a2 − b2 , we can get

 42
α

kz − z 0 k22 , kG1 (z) −



(G1 (z) + σ ∗  − GD (z 0 ))T (G1 (z) + σ ∗  − GD (z 0 ))
exp −
πD (z 0 )dz 0
T
2σ ∗ 2
Bσ∗ (z,c̄3 )c B z
 2



1
dz 2
1
2
≤ exp
−
c̄ a − dx c̄1 log ∗ .
4 3
σ
σ∗2

Z

57

TANG YANG

Also,



(G1 (z) + σ ∗  − GD (z 0 ))T (G1 (z) + σ ∗  − GD (z 0 ))
πD (z 0 )dz 0
exp −
c
2σ ∗ 2
Bz

Z

c

≤ πD (B z ).

Then, by the fact that when x ∈ Bx , p(x) & exp −c log σ1∗ , we can choose a large enough c̄3 and
η, such that


(G1 (z) + σ ∗  − GD (z 0 ))T (G1 (z) + σ ∗  − GD (z 0 ))
πD (z 0 )dz 0
exp −
T
∗2
c
2σ
Bσ∗ (z,c̄3 )
Bz
!




Z
(G1 (z) + σ ∗  − GD (z 0 ))T (G1 (z) + σ ∗  − GD (z 0 ))
1
0
+ c exp −
πD (z )dz exp c log ∗ ≤ σ ∗ .
∗2
σ
2σ
Bz
Z

So we have
pD (G1 (z) + σ ∗ )
p(G1 (z) + σ ∗ )


R
(G1 (z)+σ ∗ −GD (z 0 ))T (G1 (z)+σ ∗ −GD (z 0 ))
exp
−
πD (z 0 )dz 0
Bσ∗ (z,c3 )
2σ ∗2


≤
+ σ∗
R
(G1 (z)+σ ∗ −G1 (z 0 ))T (G1 (z)+σ ∗ −G1 (z 0 ))
0
0
exp −
πD (z )dz
2σ ∗2


∗
0 T (G (z)+σ ∗ −G (z 0 ))
1
D
exp − (G1 (z)+σ −GD (z ))
∗2
2σ

 + σ∗
≤
sup
∗ −G (z 0 ))T (G (z)+σ ∗ −G (z 0 ))
(G
(z)+σ
1
1
1
1
z 0 ∈Bσ∗ (z,c3 ) exp −
2σ ∗2
 p
 2

p
1
1
1 1
1 22 + 12 + α1
c̄1 dx (log ∗ ) 2 + c̄3 dz (log ∗ ) α
+ 1
≤ exp
+
+ σ∗.
σ
σ
2σ ∗ 2 σ ∗
Therefore we can get
log

1
1 2 1 1
pD (G1 (z) + σ ∗ )
. σ ∗ + ∗ (log ∗ ) α2 + 2 + α .
∗
p(G1 (z) + σ )
σ
σ

Similarly,

p(G1 (z) + σ ∗ )
1
1 2 1 1
. σ ∗ + ∗ (log ∗ ) α2 + 2 + α .
∗
pD (G1 (z) + σ )
σ
σ
 2

4
2

So we can bound the first part of equation (20) by O σ12 (log σ1∗ ) α2 + α +1 + σ ∗ 2 . We can then get
the desired conclusion by combining all those facts.
log

58

