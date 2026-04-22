# Adaptivity of Diffusion Models to Manifold Structures

Rong Tang Hong Kong University of Science and Technology

Yun Yang University of Illinois Urbana-Champaign

# Abstract

Empirical studies have demonstrated the effectiveness of (score-based) diffusion models in generating high-dimensional data, such as texts and images, which typically exhibit a low-dimensional manifold nature. These empirical successes raise the theoretical question of whether score-based diffusion models can optimally adapt to low-dimensional manifold structures. While recent work has validated the minimax optimality of diffusion models when the target distribution admits a smooth density with respect to the Lebesgue measure of the ambient data space, these findings do not fully account for the ability of diffusion models in avoiding the the curse of dimensionality when estimating high-dimensional distributions. This work considers two common classes of diffusion models: Langevin diffusion and forward-backward diffusion. We show that both models can adapt to the intrinsic manifold structure by showing that the convergence rate of the inducing distribution estimator depends only on the intrinsic dimension of the data. Moreover, our considered estimator does not require knowing or explicitly estimating the manifold. We also demonstrate that the forward-backward diffusion can achieve the minimax optimal rate under the Wasserstein metric when the target distribution possesses a smooth density with respect to the volume measure of the low-dimensional manifold.

# 1 Introduction

Generative models have emerged as powerful and routinely utilized tools for generating complex data, finding numerous applications across various domains, including computer vision Park et al. (2021); Wang et al. (2021); Turhan and Bilge (2018), natural language processing Salakhutdinov (2015); Nadkarni et al. (2011), and bioinformatics Cheng et al. (2021); Lan et al. (2020). Contrasted with classical explicit distribution estimation approaches, generative modeling implicitly estimates the data distribution by characterizing the data-generating process, and can adeptly capture highly nonlinear structures that may lead to singularities, such as jumps and point masses, in the distribution. Additionally, generating samples from the underlying data distribution can be more useful and important than estimating it in many applications, such as synthetic image creation, automated text generation, and biological structure simulation.

Various architectures and training methodologies, such as Generative Adversarial Networks (GAN) Goodfellow et al. (2014), Variational Autoencoders (VAE) Kingma and Welling (2013), and flow-based generative model Papamakarios et al. (2021), have been developed to enhance the efficacy and application range of generative models, each presenting unique strengths and challenges. Recently, a new class of generative models, known as (score-based) diffusion models Ho et al. (2020); Song et al. (2020); Nichol and Dhariwal (2021); Song and Ermon (2019), has showcased stateof-the-art performance in various domains, including high-quality image generation Song et al. (2020); Nichol and Dhariwal (2021), photorealistic text-toimage translation Saharia et al. (2022), and highfidelity audio production Kong et al. (2020). In particular, two classes of diffusion models are prevalently employed for sampling and data generation. One is Langevin diffusion models, which leverage Langevin dynamics to gradually transition a simple initial distribution to the target data distribution, making use of the gradient of the logarithmic data density (i.e. score), typically estimated through score matching. The other is forward-backward diffusion models, which employ two diffusions to construct the generative model. The first diffusion, called the forward process, utilizes an analytically tractable stochastic differential equation, such as the Ornstein-Uhlenbeck (OU) process, to transform the data distribution to a simple noise distribution. The second diffusion, called the backward process, utilizes the time-reversal of the forward process to generate data from noise based on the score estimated from the forward process.

Despite the high-dimensional form of data in various applications, the empirical success of state-of-the-art generative modeling approaches is often attributed to the identification and utilization of low-dimensional manifold structures within the data. These structures enable a means to circumvent the curse of dimensionality, allowing generative models to adeptly adapt to manifold structures. For instance, earlier generative modeling approaches, including GAN and VAE, typically involve the extraction of latent features or representations (encoding) that are used for accurately reconstructing the original data (decoding). In other words, a low-dimensional manifold structure is implicitly assumed and utilized in distribution modeling and estimation. In contrast, diffusion models do not explicitly estimate or utilize the manifold structure, beyond merely injecting Gaussian noise to smooth out the (possibly) singular data distribution, yet they achieve remarkably accurate data generation. Motivated by these considerations, the present study aims to address the following theoretical question: Is diffusion modeling able to optimally adapt to the manifold structure in the data? In other words, does the convergence rate of the induced distribution estimator from diffusion models depend only on the intrinsic dimension of the data, and is the rate optimal?

Related works. Recently, convergence rates of generative models for implicit distribution estimation have been investigated by a number of works. Tang and Yang (2021) examines the excess risk associated with VAE through the lens of $M$ -estimation. When specialized to Gaussian encoders and decoders with mean functions approximated by ReLU neural networks, their result demonstrates that VAE can adapt to lowdimensional manifold structures. However, the derived rate of convergence is worse than the minimax-optimal rate, as the KullbackLeibler (KL) divergence objective in VAE appears unsuitable for comparing mutually singular distributions. Several recent studies establish quantitative convergence rates for GAN in distribution estimation under various discrepancy metrics, such as the Jensen-Shannon divergence Belomestny et al. (2021), Wasserstein distances Liang (2021); Chae (2022); Tang and Yang (2023), and adversarial losses (also termed integral probability metrics) Liang (2021); Tang and Yang (2023); Uppal et al. (2019). Among these, Liang (2021) demonstrates that, by replacing the empirical distribution with a regularized version that incorporates the smoothness of the target density function, GAN can attain the minimax rate of convergence for smooth density estimation under the 1-Wasserstein metric. Furthermore, Tang and Yang (2023) establishes the minimax rate under adversarial losses for estimating smooth distributions supported on manifolds, and shows that a regularized GAN explicitly incorporating the manifold structure can attain this rate.

For Langevin diffusion models, some previous works such as Huggins and Zou (2017); Dalalyan and Karagulyan (2019); Yang and Wibisono (2022) have studied its convergence and asymptotic bias due to the use of an inaccurate score (e.g., based on stochastic gradient or score matching). However, their assumptions on the score approximation either requires a nearly $L _ { \infty }$ -accurate score estimator Dalalyan and Karagulyan (2019), or a controlled moment generating function for the approximation error Yang and Wibisono (2022), both implying a controlled error under all finite moments. In comparison, our proof only requires a fourthmoment error bound (expectation under the stationary distribution of the diffusion) on the score estimation.

For forward-backward diffusion models, Chen et al. (2022); Lee et al. (2023) demonstrate that an $L _ { 2 }$ - accurate score estimator leads to a controlled distribution estimation error bound in the total variation distance. Oko et al. (2023) analyzes the $L _ { 2 }$ -error in score estimation utilizing score matching over a neural network class, and demonstrates that, under certain smoothness conditions on the true density function, the estimated data distribution achieves the minimax optimal rate both in the total variation distance and in the 1-Wasserstein distance. For data distributions supported on manifolds, Pidstrigach (2022) identifies conditions that enable forward-backward diffusion to generate samples from the data manifold and highlights the drift explosion in the backward diffusion process as time progresses; De Bortoli (2022) examines convergence in the 1-Wasserstein distance under an $L _ { 2 }$ error assumption on the score estimator; and Oko et al. (2023); Chen et al. (2023) establish explicit convergence rates using specific score estimation methods when the data-supporting manifold is a lowdimensional hyperplane in the ambient space, with the rate by Oko et al. (2023) attaining the minimax optimality in the 1-Wasserstein distance.

Our contributions. In this paper, we illustrate that both diffusion models can adapt to the intrinsic manifold structure by demonstrating that the convergence rates of the inducing distribution estimators are $n ^ { - O ( d ^ { - 1 } ) }$ up to logarithmic terms, with $d$ denoting the data intrinsic dimension. Interestingly, unlike other generative modelling approaches such as GAN and VAE, our considered estimator does not need knowing or explicitly estimating the manifold. Furthermore, our result shows that the forward-backward diffusion can achieve the minimax optimal rate of max  √1n , $\left\{ { \frac { 1 } { \sqrt { n } } } , n ^ { - { \frac { \alpha + 1 } { 2 \alpha + d } } } \right\}$ under the 1-Wasserstein metric when the target distribution admits an $\alpha$ -smooth density with respect to the volume measure of a (potentially non-linear) $d$ -dimensional manifold in the ambient space $\mathbb { R } ^ { D }$ . For Langevin diffusion models, in order to appropriately define the drift based on a singular data distribution, we consider a Gaussian-smoothed score and a corresponding score estimation method; technically, we demonstrate that a fourth-moment error bound on the score estimator suffices to imply a distribution estimation error bound, which refines existing theory that assumes either an $L _ { \infty }$ error bound or a moment-generating function bound on the error distribution of the score estimator. For forward-backward diffusion models, we show that the minimax optimal estimation error can be attained without explicitly estimating the manifold by employing a new class of score approximating neural network class whose complexity gradually changes with time $t$ , and derive an explicit score approximation error bound.

# 2 Diffusion Models and Score Estimation

In this section, we review two representative scorebased diffusion models for distribution estimation. We also discuss their adaptations for handling singular distributions with manifold structure.

# 2.1 Langevin diffusion models

In generative modeling, the goal is to implicitly learn the underlying data distribution $p _ { \mathrm { d a t a } }$ on data space $\mathcal { X } \subset \mathbb { R } ^ { D }$ by specifying a data generative model that produces samples looking similar to a given set of i.i.d. samples $\{ x _ { i } \} _ { i = 1 } ^ { n }$ from $p _ { \mathrm { d a t a } }$ . Earlier attempts (e.g., Song and Ermon (2019)) to address this problem using diffusion models directly used a (timediscretized) Langevin model to generate new data when $p _ { \mathrm { d a t a } }$ admits a density with respect to the Lebesgue measure on $\mathbb { R } ^ { D }$ ,

$$
\begin{array} { r } { \mathrm { d } X _ { t } = - \nabla \log p _ { \mathrm { d a t a } } ( X _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , X _ { 0 } \sim p _ { 0 } , } \end{array}
$$

where $\{ B _ { t } : t \geq 0 \}$ denotes the standard Brownian motion in $\mathbb { R } ^ { D }$ , $p _ { 0 }$ is an initial distribution that is easy to sample from, and $\nabla \log p _ { \mathrm { d a t a } } : \mathbb { R } ^ { D } \to \mathbb { R } ^ { D }$ is called the score function defining the drift term of the diffusion model. As a well-known result, the stationary (or limiting) distribution of the Langevin model (1) coincides with the target distribution $p _ { \mathrm { d a t a } }$ . In other words, the distribution $p _ { t }$ of $X _ { t }$ converges to $p _ { \mathrm { d a t a } }$ as $t \to \infty$ under various metrics over $\mathcal { P } ( \mathcal { X } )$ , the space of all distribution on the data space $\mathcal { X } \subset \mathbb { R } ^ { D }$ . In practice, the score function needs to be estimated; we defer details about score estimation using the finite sample set $\{ x _ { i } \} _ { i = 1 } ^ { n }$ to Section 2.3. In this paper, we aim to keep the presentation simple by ignoring the technical issues that arise from the time-discretization error in simulating or generating samples from diffusion models, which have been addressed in many existing works, e.g., Zhang et al. (2023); Dalalyan (2017); Li et al. (2019). Unfortunately, this conceptually simple score-based diffusion modeling approach has a notable drawback: the convergence of $p _ { t }$ to its limit $p _ { \mathrm { d a t a } }$ can be exponentially slow due to the non-log-concavity or multi-modality of $p _ { \mathrm { d a t a } }$ .

When dealing with high-dimensional data residing on low-dimensional manifolds, a common scenario in image and text generation, $p _ { \mathrm { d a t a } }$ becomes a singular distribution on the data ambient space $\mathbb { R } ^ { D }$ . In such cases, Song and Ermon (2019) proposes an annealing approach, where they use scores associated with the Gaussian-smoothed data distribution $p _ { \mathrm { d a t a } , \sigma } ( \cdot ) =$ $\int _ { \mathbb { R } ^ { D } } p _ { \mathrm { d a t a } } ( y ) \phi _ { \sigma } ( \cdot - y ) \mathrm { d } y$ with different levels of noise $\sigma$ to construct a sequence of annealed Langevin models. Here, $\phi _ { \sigma }$ denotes the density function of ${ \mathcal { N } } ( 0 , \sigma ^ { 2 } I _ { D } )$ . In the sampling stage, noise levels are gradually decreased as the sampling process approaches the data manifold. In this work, we instead consider the following Gaussian-smoothed Langevin diffusion

$$
\mathrm { d } X _ { t } = - \nabla \log p _ { \mathrm { d a t a } , \sigma } ( X _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , \ X _ { 0 } \sim p _ { 0 }
$$

using a single noise parameter $\sigma$ to optimally trade-off the bias and variance in order to attain a best estimation error. Intuitively, this parameter $\sigma$ plays a similar role as an inverse bandwidth parameter as in the kernel density estimator (e.g., Kim et al. (2019); Divol (2022) for KDE on manifolds). The first contribution of this paper is to show that, with a properly chosen $\sigma$ that depends only on the sample size $n$ and the intrinsic dimensionality $d$ of the data, this Gaussian-smoothed Langevin diffusion can adapt to the intrinsic manifold structure by showing that the convergence rate of the inducing distribution estimator for estimating $p _ { \mathrm { d a t a } }$ depends only on $d$ . Here, the estimation of the noiseperturbed score function $\nabla \log p _ { \mathrm { d a t a } , \sigma }$ is discussed in Section 2.3.

# 2.2 Forward and backward diffusion models

To address the issue of potentially exponentially slow convergence inherent to the Langevin diffusion model, several recent papers (e.g., Ho et al. (2020); Song et al. (2020)) have introduced forward and backward diffusion models. These strategies employ two diffusion processes collaboratively: one for constructing more complex, time-dependent score functions, and the other for generating samples through a time-inhomogeneous process, based on the estimated score functions. Consequently, this method can circumvent the slow convergence typically associated with using a single diffusion model.

Specifically, the first diffusion process, referred to as the forward diffusion, employs a simple diffusion starting from $p _ { \mathrm { d a t a } }$ that admits a closed-form solution and converges exponentially quickly to its limiting distribution, such as the OrnsteinUhlenbeck (OU) process:

$$
\mathrm { d } \overrightarrow { X } _ { t } = - \beta _ { t } \overrightarrow { X } _ { t } \mathrm { d } t + \delta _ { t } \mathrm { d } B _ { t } , \ \overrightarrow { X } _ { 0 } \sim p _ { \mathrm { d a t a } } ,
$$

for some (possibly time-dependent) drift coefficient $\beta _ { t } : , t \geq 0$ and scalar diffusion coefficient $\delta _ { t } : , t \geq 0$ Without loss of generality, we will focus on the OU process with $\delta _ { t } ~ = ~ \sqrt { 2 \beta _ { t } }$ as the forward diffusion in this paper,1 which admits the closed form solution $\begin{array} { r } { X _ { t } = m _ { t } X _ { 0 } + \int _ { 0 } ^ { t } \frac { m _ { t } } { m _ { s } } \sqrt { 2 \beta _ { s } } \mathrm { d } B _ { s } } \end{array}$ and has the conditional distribution of $p _ { t } ( { } \cdot { } | X _ { 0 } ) = \mathcal { N } ( m _ { t } X _ { 0 } , \sigma _ { t } ^ { 2 } I _ { D } )$ given $X _ { 0 }$ , where $\begin{array} { r } { m _ { t } = \exp \big ( - \int _ { 0 } ^ { t } \beta _ { s } \mathrm { d } s \big ) } \end{array}$ and $\sigma _ { t } ^ { 2 } = 1 - m _ { t } ^ { 2 }$ . Fo r example, for constant drift $\beta _ { t } \equiv \beta$ and diffusion $\delta _ { t } \equiv$ $\sqrt { 2 \beta }$ , we have $m _ { t } = \exp ( - \beta t )$ , $\sigma _ { t } ^ { 2 } = 1 - \exp ( - 2 \beta t )$ , and $p _ { t }$ converges exponentially quickly to its limiting distribution $p _ { \infty } = \mathcal { N } ( 0 , \sigma _ { \infty } ^ { 2 } I _ { D } )$ with $\sigma _ { \infty } ^ { 2 } = 1$ under the total variation metric $d _ { \mathrm { T V } }$ , or

$$
\begin{array} { r } { d _ { \mathrm { T V } } ( p _ { t } , p _ { \infty } ) \leq C \exp ( - \beta t ) , t \geq 0 , } \end{array}
$$

for some constant $C$ only depending on $p _ { 0 } ~ = ~ p _ { \mathrm { d a t a } }$ Using sample trajectories generated from the forward diffusion (3), one can estimate the (time-dependent) score function $\nabla \log p _ { t } : , \mathbb { R } ^ { D } \to \mathbb { R } ^ { D }$ by score matching (c.f. Section 2.3), where $p _ { t }$ denotes the (unconditional) distribution of $X _ { t }$ , for $t$ from zero to a sufficiently large time $T \asymp \log ( \varepsilon ^ { - 1 } )$ such that $d _ { \mathrm { T V } } ( p _ { T } , p _ { \infty } ) \leq \varepsilon$ for some error tolerance level $\varepsilon \in ( 0 , 1 )$ .

The second diffusion process, usually called the backward diffusion, reverses the forward diffusion:

$$
\begin{array} { r l } & { \mathrm { d } \overleftarrow { X } _ { t } = \left[ \beta _ { T - t } \overleftarrow { X } _ { t } + 2 \beta _ { T - t } \nabla \log p _ { T - t } ( \overleftarrow { X } _ { t } ) \right] \mathrm { d } t } \\ & { \qquad + \ \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } , \quad \overleftarrow { X } _ { 0 } \sim p _ { T } . } \end{array}
$$

Under mild conditions on $p _ { \mathrm { d a t a } }$ Song et al. (2020); Haussmann and Pardoux (1986) (valid for our setting), the distribution of $\smash { \overleftarrow { X } } _ { t }$ is $p _ { T - t }$ , so that $\overleftarrow { X } _ { T } \sim p _ { 0 } =$ $p _ { \mathrm { d a t a } }$ . Since $p _ { T }$ is close to $p _ { \infty } = \mathcal { N } ( 0 , I _ { D } )$ , one can instead initialize the backward diffusion using the easyto-sample distribution $p _ { \infty }$ , i.e. set $\overleftarrow { X } _ { 0 } \sim \mathcal { N } ( 0 , I _ { D } )$

The drift term of the backward diffusion depends on the score function estimated using the forward diffusion; therefore, the forward and the backward diffusions together yield a generative model for sampling from pdata.

When $p _ { \mathrm { d a t a } }$ is a singular distribution on $\mathbb { R } ^ { D }$ , the distribution $p _ { t }$ of $\vec { X } _ { t }$ for any $t > 0$ from the forward diffusion is the convolution of a rescaled $p _ { \mathrm { d a t a } }$ and Gaussian noise $N ( 0 , \sigma _ { t } ^ { 2 } I _ { D } )$ , making it absolutely continuous with respect to the Lebesgue measure on $\mathbb { R } ^ { D }$ . Therefore, unlike the Langevin diffusion (1) that requires deliberately injecting Gaussian noise to smooth out $p _ { \mathrm { d a t a } }$ , the forward and backward diffusion model does not require this extra step. The second contribution of this paper is to show that the forward and backward diffusion model can also achieve the minimax-optimal convergence rate for estimating $p _ { \mathrm { d a t a } }$ . Moreover, compared to the Langevin diffusion model, the forward and backward diffusion model does not impose any log-concavity condition or any logarithmic Sobolev inequalities on $p _ { \mathrm { d a t a } }$ . This is consistent with the key observations made in earlier studies (e.g., Chen et al. (2022); Lee et al. (2023)) that do not involve manifold structures.

# 2.3 Score estimation

Langevin diffusion model: The score function in the Langevin diffusion model can be estimated by score matching Song and Ermon (2019); Vincent (2011). At the population level, score matching solves the following optimization problem

$$
\operatorname* { m i n } _ { \theta } \mathbb { E } _ { x \sim p _ { \mathrm { d a t a } } } \big [ \| S _ { \theta } ( x ) - \nabla \log p _ { \mathrm { d a t a } } ( x ) \| ^ { 2 } \big ] ,
$$

where $S _ { \theta } : \mathbb { R } ^ { D }  \mathbb { R } ^ { D }$ denotes a score approximating map parameterized by parameter $\theta$ , e.g., (deep) neural networks with controlled depth and number of non-zero parameters. Recall that the primary focus of this paper is on estimating a singular distribution with manifold structure. Therefore, we consider using $\widehat { S } \ = \ S _ { \widehat { \theta } }$ to approximate the noise-injected score $\nabla \log p _ { \mathrm { d a t a } , \sigma }$ , where $\widehat { \theta }$ minimizes the following samplelevel score matching loss:

$$
\frac { 1 } { n } \sum _ { i = 1 } ^ { n } \mathbb { E } _ { \boldsymbol { x } \sim p _ { \sigma } ( \cdot \mid \boldsymbol { x } _ { i } ) } \big [ \| S _ { \boldsymbol { \theta } } ( \boldsymbol { x } ) - \nabla \log p _ { \sigma } ( \boldsymbol { x } \mid \boldsymbol { x } _ { i } ) \| ^ { 2 } \big ] .
$$

Here, $p _ { \sigma } ( x \vert x _ { i } ) = \mathcal { N } ( x _ { i } , \sigma ^ { 2 } I _ { D } )$ denotes the conditional distribution of the Gaussian error-injected random variable $x$ given $i$ -th data $x _ { i }$ , so that the (unconditional) distribution of $x$ is $p _ { \mathrm { d a t a } , \sigma }$ . Finally, the distribution estimator of $p _ { \mathrm { d a t a } }$ based the estimated Langevin diffusion model is ${ \widehat { p } } = { \widehat { p } } _ { T }$ , where $\widehat { p } _ { t }$ is the distribution

of $Y _ { t }$ for $t \in [ 0 , T ]$ , and

$$
\mathrm { d } Y _ { t } = - \widehat { S } \left( Y _ { t } \right) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , Y _ { 0 } \sim \mu _ { 0 } .
$$

Forward-backward diffusion model: To estimate the time-dependent score function $\nabla \log p _ { t }$ in the forward diffusion (3), one can use a score function $S _ { \theta } ( x , t )$ over space and time, indexed by a parameter $\theta$ , and minimize the following sample score matching loss:

$$
\begin{array} { r l } { \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \int _ { 0 } ^ { T } \mathbb { E } _ { x _ { t } \sim p _ { t } ( \cdot \mid x _ { i } ) } } & { } \\ { \displaystyle \left[ \| S _ { \theta } ( x _ { t } , t ) - \nabla \log p _ { t } ( x _ { t } \mid x _ { i } ) \| ^ { 2 } \right] \lambda ( t ) \mathrm { d } t , } \end{array}
$$

where $\lambda ( t )$ is a weighting function. Here, given $x _ { i }$ $x _ { t } \sim p _ { t } ( { \cdot } | x _ { i } ) = \mathcal { N } ( m _ { t } x _ { i } , \sigma _ { t } ^ { 2 } I _ { D } )$ follows the forward diffusion (3) with initialization $X _ { 0 } = x _ { i }$ . Without loss of generality, we may assume $\lambda ( t )$ to be a normalized probability density function over $[ 0 , T ]$ . Finally, let $\widehat { S } ( x , t ) = S _ { \widehat { \theta } } ( x , t )$ denote the corresponding score estimator. The distribution estimator of $p _ { \mathrm { d a t a } }$ based the forward-backward diffusion model is ${ \widehat { p } } = { \widehat { p } } _ { T }$ , where $\widehat { p } _ { t }$ is the distribution of $\smash { \overleftarrow { Y } } _ { t }$ for $t \in [ 0 , T ]$ b b, and

$$
\begin{array} { r } { \mathrm { d } \overleftarrow { Y } _ { t } = \left[ \beta _ { T - t } \overleftarrow { Y } _ { t } \ + \ 2 \beta _ { T - t } \widehat { S } ( \overleftarrow { Y } _ { t } , T - t ) \right] \mathrm { d } t } \\ { + \ \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } , \overleftarrow { Y } _ { 0 } \sim \mathcal { N } ( 0 , I _ { D } ) . } \end{array}
$$

In both cases, we consider using neural networks to define the function class for approximating the score.

Definition (Neural network class): A class of neural networks $\Phi ( L , W , S , B , V )$ with height $L$ , width vector $W = ( W _ { 1 } , W _ { 2 } , \dots , W _ { L + 1 } ) $ ), sparsity $R$ , norm constraint $B$ , and function norm constraint $V$ is defined as $\Phi ( L , W , R , B , V ) = \left\{ f ( \cdot ) = \left( A ^ { ( L ) } \mathrm { R e L U ( \cdot ) } + \right. + \right.$ $b ^ { ( L ) } \big ) \circ \cdot \cdot \cdot \circ \big ( A ^ { ( 2 ) } \mathrm { R e L U } ( \cdot ) + b ^ { ( 2 ) } \big ) \circ \big ( A ^ { ( 1 ) } x + b ^ { ( 1 ) } \big ) \big | A ^ { ( i ) } \in$ $\mathbb { R } ^ { W _ { i } \times W _ { i + 1 } }$ ; $b ^ { ( i ) } ~ \in ~ \mathbb { R } ^ { W _ { i + 1 } }$ ; $\begin{array} { r } { \sum _ { i = 1 } ^ { l } ( \| A ^ { ( i ) } \| _ { 0 } + \| b ^ { ( i ) } \| _ { 0 } ) \leq } \end{array}$ $R$ ; $\begin{array} { r } { \operatorname* { m a x } _ { i } \| A ^ { ( i ) } \| _ { \infty } \vee \| b ^ { ( i ) } \| _ { \infty } \le B ; \| f \| _ { \infty } \le V \Big \} } \end{array}$ , where $\mathrm { R e L U } ( x ) = \operatorname* { m a x } \{ 0 , x \}$ denotes the rectified linear unit activation function.

# 3 Main Results

In this section, we present our main results showing that both diffusion models can adapt to the data manifold structure without requiring knowledge or explicit estimation of the manifold. For any sequence $\{ a _ { n } : n \geq 1 \}$ , we use the notation $\Theta ( a _ { n } )$ to mean of order of $a _ { n }$ up to a multiplicative constant as $n \to \infty$ and $\widetilde { \Theta } ( a _ { n } )$ to mean of order of $a _ { n }$ up to a multiplicative constant and logarithmic terms of $n$ . Similarly, we use $\mathcal { O } ( a _ { n } )$ and $\widetilde { \mathcal { O } } ( a _ { n } )$ to mean of at most order of $a _ { n }$ .

# 3.1 Assumptions

Assumption A (Regularity of data manifold): The target distribution $p _ { \mathrm { d a t a } }$ lies in a $d$ -dimensional submanifold $\mathcal { M }$ embedded in $\mathbb { R } ^ { D }$ . The manifold $\mathcal { M }$ is compact and boundaryless. Additionally, it is $\beta$ - smooth for $\beta \geq 2$ and has a reach that is lower bounded away from zero.2

Intuitively, imposing a lower bound on the reach of the manifold ensures that the projection map to the manifold is locally well-defined; that is, it guarantees a unique projection from any point close to the manifold. In the analysis of the generalization bound (see Appendix C), the existence of such local projection maps will be leveraged to construct neural networks capable of approximating true score functions. Furthermore, appropriate neural networks will be designed to locally approximate these projection maps (see Lemma C.8), with their complexity being dependent on the smoothness level $\beta$ of the manifold.

Assumption B (Regularity of data distribution): The density $f ^ { * }$ of $p _ { \mathrm { d a t a } }$ relative to the volume measure of $\mathcal { M }$ is $\alpha$ -smooth with $\alpha \in [ 0 , \beta - 1 ]$ and uniformly bounded away from zero on $\mathcal { M }$ .

Here, we restrict $\alpha ~ \in ~ [ 0 , \beta - 1 ]$ to make the density smoothness compatible with the manifold smoothness (see Appendix A for details). In the special case when $\mathcal { M } = \mathbb { R } ^ { D }$ , the density function $f ^ { * }$ becomes the usual probability density function with respect to the Lebesgue measure on $\mathbb { R } ^ { D }$ , and the $\alpha$ -smoothness condition reduces to the usual Hölder smoothness. The lower bound requirement of $p _ { \mathrm { d a t a } }$ on $\mathcal { M }$ is commonly imposed for distribution estimation in statistics; otherwise, we can redefine the manifold $\mathcal { M }$ as the support of $p _ { \mathrm { d a t a } }$ , or the region where $p _ { \mathrm { d a t a } }$ is lower bounded by any sufficiently small positive constant.

Assumption $\mathbf { C }$ (Poincaré constant): $p _ { \mathrm { d a t a } }$ satisfies a Poincaré inequality with a (Poincaré) constant $\zeta _ { \mathrm { P I } } >$ $0$ , that is, for all smooth functions $f : \mathbb { R } ^ { D }  \mathbb { R }$ ,

$$
\begin{array} { r } { \mathrm { V a r } _ { p _ { \mathrm { d a t a } } } ( f ) = \mathbb { E } _ { p _ { \mathrm { d a t a } } } \big [ ( f - \mathbb { E } _ { \mu ^ { * } } f ) ^ { 2 } \big ] \leq C _ { \mathrm { P I } } . \mathbb { E } _ { p _ { \mathrm { d a t a } } } \big [ \| \nabla f \| ^ { 2 } \big ] , } \end{array}
$$

Assumption C will be utilized only in the analysis of Langevin diffusion. Note that in a standard analysis of Langevin diffusion, a positive Poincaré constant $C _ { \mathrm { P I } }$ , as assumed in Assumption C, is a common condition to guarantee exponential ergodicity with respect to the chi-squared divergence $\chi ^ { 2 }$ : if $\mathcal { M } = \mathbb { R } ^ { D }$ and $p _ { \mathrm { d a t a } }$ satisfies Assumption C, then the time $t$ distribution $p _ { t }$ of the Langevin diffusion (1) converges to $p _ { \mathrm { d a t a } }$ as

$$
\chi ^ { 2 } ( p _ { t } \parallel p _ { \mathrm { d a t a } } ) \leq \exp \big ( - 2 t / C _ { \mathrm { P I } } \big ) \chi ^ { 2 } ( \mu _ { 0 } \parallel p _ { \mathrm { d a t a } } ) , t \geq 0 .
$$

Langevin diffusion is a useful approach for sampling only when $p _ { t }$ rapidly approaches its stationary distribution as $t$ increases; therefore, making Assumption C when analyzing the Langevin diffusion approach is reasonable. See, for example Besson et al. (2018); Mertin (2022), for related results about Poincaré inequalities on manifolds. In particular, the corresponding Poincaré constant also depends on certain geometric characterizations of the manifold, such as the Ricci curvature. As an intermediate result in our proof (proof of Lemma B.4 in Appendix D.6), we show that Assumption C implies the Gaussian-smoothed distribution $p _ { \mathrm { d a t a } , \sigma }$ also satisfies a Poincaré inequality with constant $C _ { \mathrm { P I } } + \sigma ^ { 2 }$ , leading to the exponential convergence of the Gaussian-smoothed Langevin diffusion (2).

# 3.2 Langevin diffusion model

Let $\widehat { S }$ denote the score estimator defined as the minimizer of score matching loss (7) over the neural network class $\Phi ( L , W , R , B , V )$ . Recall that $\{ Y _ { t } : t \geq 0 \}$ follows the diffusion (8) with estimated score $\widehat { S }$ , which approximates the “population-level” Langevin diffusion (2) . Since the Langevin diffusion (2) converges exponentially fast to $p _ { \mathrm { d a t a } , \sigma }$ as $t \to \infty$ and the manifold is compact, we define a (truncated) estimator $\widehat { p }$ for $p _ { \mathrm { d a t a } }$ as the distribution of $Y _ { T } \cdot \mathbf { 1 } ( \| Y _ { T } \| _ { \infty } \leq L )$ , for some large constants $( T , L )$ so that $p _ { T } \approx p _ { \mathrm { d a t a } }$ and $\mathcal { M } \subset \mathbb { B } _ { L / 2 } ( 0 _ { D } )$ . Here, we truncate the support of the distribution $p _ { T }$ of $Y _ { T }$ to guarantee a bounded support for the distribution estimator, which is merely for technical reasons. Let $\begin{array} { r } { W _ { 1 } ( \mu , \nu ) ~ = ~ \operatorname* { s u p } _ { f \mathrm { i s } 1 - \mathrm { L i p } } \mid \int f \mathrm { d } \mu - } \end{array}$ $\int f \mathrm { d } \nu |$ denote the 1-Wasserstein distance.

Theorem 1 (Langevin diffusion). Suppose Assumptions $A$ , $B$ , and $C$ are satisfied, and the initial distribution $p _ { 0 }$ in the Langevin diffusion satisfies $\chi ^ { 2 } ( p _ { 0 } \| p _ { \mathrm { d a t a } , \sigma } ) = \mathcal { O } ( 1 )$ . If we set $T = \Theta \big ( \log n \big )$ an d

$$
\sigma = \left\{ \begin{array} { c c } { n ^ { - \frac { 1 } { 8 + d } } } & { \alpha \leq 4 ~ o r ~ \beta \leq 5 } \\ { n ^ { - \frac { \alpha } { 8 \alpha + 4 d } } } & { 4 < \alpha \leq \frac { 4 } { 5 } \beta } \\ { n ^ { - \frac { \beta } { 1 0 \alpha + 5 d } } } & { o t h e r w i s e , } \end{array} \right.
$$

then there exist neural network size $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = { \widetilde { \Theta } } { \big ( } ( \sigma \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } { \big ) }$ , $R = \widetilde { \Theta } \big ( ( \sigma \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } \big )$ , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ and $\begin{array} { r } { V = \Theta \big ( \frac { \sqrt { \log n } } { \sigma } \big ) } \end{array}$ , so that

$$
\mathbb { E } [ W _ { 1 } ( \widehat { p } , p _ { \mathrm { d a t a } } ) ] = \widetilde { \mathcal { O } } ( \sigma ) .
$$

Theorem 1 shows that the convergence rate of the distribution estimator $\hat { p }$ only depends on the intrinsic dimension $d$ as opposed to the ambient dimension $D$ . However, as we will see, the current error upper bound is worse than error attained by the forward-backward diffusion model (see Theorem 2). By inspecting our current proof, we find this larger error bound is mainly due to several reasons.

At the technical level, an $L _ { 2 }$ error (or second-moment) bound on the estimated score $\widehat S$ is not sufficient to control the $W _ { 1 }$ error (or any other common error metrics) of the distribution estimator $\widehat { p }$ based on the Langevin diffusion, an observation also made in Huggins and Zou (2017); Yang and Wibisono (2022). Our new proof technique (c.f. Section 4) demonstrates that a fourthmoment error bound on the score estimation suffices to control the $W _ { 1 }$ error, thereby relaxing the moment generating function error assumption from Yang and Wibisono (2022) that implies an error bound on the score estimation for all finite moments. However, since the score estimation method based on score matching is intrinsically tied up with the second-moment bound, and directly relating the fourth-moment to the secondmoment by the $L _ { \infty }$ norm on the score will introduce an extra factor of order $\widetilde { \mathcal { O } } ( \sigma ^ { - 1 } )$ since the Gaussiansmoothed score $\nabla \log p _ { \mathrm { d a t a } , \sigma }$ has $L _ { \infty }$ norm of order $\widetilde { \mathcal { O } } ( \sigma ^ { - 1 } )$ near the manifold.

At the method design level, given that Gaussian noise $N ( 0 , \sigma ^ { 2 } I _ { D } )$ in the full space $\mathbb { R } ^ { D }$ is injected into the true data distribution $p _ { \mathrm { d a t a } }$ in the construction of the Langevin diffusion, it is plausible that such isotropic noise might dilute the manifold structure and lead to an inflated approximation error. For instance, this isotropic noise renders the approximation error $W _ { 1 } ( p _ { \mathrm { d a t a } , \sigma } , p _ { \mathrm { d a t a } } ) = \mathcal { O } ( \sigma )$ , which is larger than a typical approximation error of order $\sigma ^ { \alpha + 1 }$ that can lead to the minimax rate in the analysis. Note that $\sigma$ cannot be chosen too small, as otherwise the Gaussiansmoothed score $\nabla \log p _ { \mathrm { d a t a } , \sigma }$ becomes nearly singular, causing its estimation error to explode. It is therefore an interesting direction to explore whether it is possible to improve the score estimation procedure in Langevin diffusion either by using a different loss, or by avoiding the injection of isotropic Gaussian noise and incorporating information about the manifold beyond merely its intrinsic dimension $d$ .

One natural choice of initialization $p _ { 0 }$ is the kernel density estimator (KDE) with bandwidth $\sigma$ in $\mathbb { R } ^ { D }$ , i.e., $\begin{array} { r } { p _ { 0 } ( y ) = n ^ { - 1 } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| X _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \cdot ( 2 \pi \sigma ^ { 2 } ) ^ { - \frac { D } { 2 } } } \end{array}$ . Interestingly, the following lemma shows that the chisquared error rate only depends on the intrinsic dimension $d$ , and $\chi ^ { 2 } ( p _ { 0 } \| p _ { \mathrm { d a t a } , \sigma } ) = \mathcal { O } ( 1 )$ is satisfied if $\sigma ^ { - 1 } = \widetilde { \mathcal { O } } ( n ^ { \frac { 1 } { d } } )$ .

Lemma 1. Let $( \delta _ { 1 } , \delta _ { 2 } )$ be any fixed positive constants. Consider the initial distribution with density $p _ { 0 } ( y ) =$ $\begin{array} { r } { n ^ { - 1 } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \Vert X _ { i } - y \Vert ^ { 2 } } { 2 \sigma ^ { 2 } } ) \cdot ( 2 \pi \sigma ^ { 2 } ) ^ { - \frac { D } { 2 } } } \end{array}$ $c _ { 1 } n ^ { - \delta _ { 1 } } \leq \sigma \leq$ $c _ { 2 } n ^ { - \delta _ { 2 } }$ $1 - c _ { 3 } n ^ { - 1 }$

$$
\chi ^ { 2 } ( p _ { 0 } \parallel p _ { \mathrm { d a t a } , \sigma } ) = \widetilde { \mathcal { O } } \bigl ( n ^ { - 1 } \sigma ^ { - d } + n ^ { - 2 } \sigma ^ { - 2 d } \bigr ) .
$$

# 3.3 Forward-backward diffusion model

Recall that in the forward diffusion process (3), the distribution $p _ { t }$ of $X _ { t }$ as $t \to \infty$ rapidly approaches a limiting normal distribution $\mathcal { N } ( 0 , I _ { D } )$ , which admits an infinitely differentiable density function, allowing the corresponding score function to be approximated by relatively small neural networks. Consequently, it is anticipated that the required sizes of neural networks for approximating $\nabla \log p _ { t }$ would gradually decrease as $t$ increases. This motivates us to consider score neural networks whose size decreases in $t$ . For technical convenience, we discretize the time and consider the following piece-wise constant complexity neural network class, although it is possible to design a more sophisticated network architecture that allows for a smoother change of network complexity over time $t$ and facilitate the sharing of parameters (potentially long-range) between different times,

$$
\begin{array} { r l r } {  { \mathcal { S } _ { N N } = \big \{ S ( x , t ) = \sum _ { k = 0 } ^ { K - 1 } S _ { k } ( x , t ) \cdot \mathbf { 1 } \big ( t _ { k } \leq t < t _ { k + 1 } \big ) } } \\ & { } & { \big | S _ { k } \in \Phi ( L _ { k } , W _ { k } , R _ { k } , B _ { k } , V _ { k } ) , \ k \in [ K ] \big \} , } \end{array}
$$

where $\tau = t _ { 0 } < t _ { 1 } < \cdots < t _ { K } = T$ , tk+1 = 2 for any $0 \leq k \leq K - 1$ , and ${ \tau } = 2 ^ { - K } T$ . Let $\widehat { S } ( x , t )$ be the score estimator defined as the minimizer of score matching loss (9) over score class $\mathit { S } _ { \mathit { N N } }$ with weight function $\lambda ( t ) = t$ (other weights like $\lambda ( t ) \equiv 1$ also work). Based on the backward diffusion process (10) with the estimated score $\widehat { S }$ , we define a similar truncated estimator $\widehat { p }$ for $p _ { \mathrm { d a t a } }$ as the distribution of $\{ \overleftarrow { Y } _ { T - \tau } . \mathbf { 1 } ( \Vert \overleftarrow { Y } _ { T - \tau } \Vert _ { \infty } \leq$ $L$ ). Here, we consider time $T - \tau$ instead of $T$ to mitigate the issue of the score function explosion, which arises due to the singularity of the target distribution, or $p _ { t } \to \infty$ on $\mathcal { M }$ as $t  0 _ { + }$ . For any $\gamma \in ( 0 , 1 ]$ , let $\begin{array} { r } { d _ { \gamma } ( \mu , \nu ) \ = \ \operatorname* { s u p } _ { f : \| f ( x ) - f ( y ) \| \leq \| x - y \| ^ { \gamma } } \big | \int f \mathrm { d } \mu - \int f \mathrm { d } \nu \big | } \end{array}$ denote a general $\gamma$ adversarial loss, which reduces to $W _ { 1 }$ at $\gamma = 1$ and to $d _ { \mathrm { T V } }$ as $\gamma  0 _ { + }$ . Roughly speaking, a smaller (larger) $\gamma$ causes $d _ { \gamma }$ to place more weight on the manifold (density) estimation; see Appendix B.1 for further details.

Theorem 2 (Forward-backward diffusion). Suppose Assumptions $A$ and $B$ are satisfied, and the drift coefficient $\beta _ { t }$ is infinitely differentiable and uniformly bounded from above and below in $t$ . Then there exist $\tau = \widetilde { \Theta } ( n ^ { - \frac { 2 \beta } { 2 \alpha + d } } )$ , $T = \Theta ( \log n )$ , and neural network sizes satisfying $L _ { k } = \Theta ( \log ^ { 4 } n )$ , $\| \boldsymbol { W } _ { k } \| _ { \infty } = \widetilde { \Theta } \big ( t _ { k } ^ { - \frac { d } { 2 } } \vee$ $n ^ { \frac { d } { 2 \alpha + d } } )$ , $R _ { k } \ = \ \widetilde \Theta \big ( t _ { k } ^ { - \frac { d } { 2 } } \vee n ^ { \frac { d } { 2 \alpha + d } } \big )$ , $\log B _ { k } \ = \ \Theta ( \log ^ { 4 } n )$ and $\begin{array} { r } { V _ { k } = \Theta \big ( \sqrt { \frac { \log n } { t _ { k } \wedge 1 } } \big ) } \end{array}$ for $k \in \{ 0 , 1 , \cdots , K - 1 \}$ , so that

$$
\begin{array} { r } { \mathbb { E } [ d _ { \gamma } ( \widehat { p } , p _ { \mathrm { d a t a } } ) ] = \widetilde { \mathcal { O } } \big ( n ^ { - \frac { 1 } { 2 } } \vee n ^ { - \frac { \beta \gamma } { 2 \alpha + d } } \vee n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \big ) . } \end{array}
$$

Theorem 2 shows that the forward-backward diffusion model can also adapt to the (possibly unknown) manifold structure. Moreover, when taking $\gamma = 1$ , the obtained convergence rate ${ \frac { 1 } { \sqrt { n } } } \lor n ^ { - { \frac { \alpha + 1 } { 2 \alpha + d } } }$ matches the minimax-optimal rate under $W _ { 1 }$ metric of estimating an $\alpha$ -smooth distribution supported on a $d$ - dimensional manifold in $\mathbb { R } ^ { D }$ Tang and Yang (2023) up to $\log n$ terms. As expected, to attain the minimax rate by optimally balancing the approximation and estimation error of the score estimator, the neural network size (e.g., $\| W _ { k } \| _ { \infty }$ , $R _ { k }$ and $V _ { k }$ ) demanded in the theorem for approximating the score function $\nabla \log p _ { t }$ decreases as $t$ increases.

Compared to the Langevin diffusion model, forwardbackward diffusion does not require imposing any condition, such as isoperimetry (Assumption C) or log-Sobolev inequality on $p _ { \mathrm { d a t a } }$ , to ensure a controlled error bound that does not explode as $t$ increases. This observation is consistent with numerous existing theoretical works (e.g., De Bortoli et al. (2021); Oko et al. (2023); Lee et al. (2023); Chen et al. (2022)) primarily focusing on characterizing error bounds on sampling from distributions in $\mathbb { R } ^ { D }$ that admit (at least) Lipschitz continuous density functions (with respect to the ambient space Lebesgue measure). In addition, according to Theorem 1, Langevin diffusion requires a reasonably good initialization $p _ { 0 }$ so that $\chi ^ { 2 } ( p _ { 0 } \| p _ { \mathrm { d a t a } , \sigma } ) = \mathcal { O } ( 1 )$ , while the backward diffusion for sampling simply initializes at a normal distribution. It is worth noticing that an essential property leading to minimax-optimality is that forward-backward diffusion only requires an $L _ { 2 }$ -accurate score estimate in order to produce a good distribution estimator $\widehat { p }$ Lee et al. (2023); Chen et al. (2022); the present work rigorously demonstrates that this property remains valid when estimating singular target distributions, utilizing the same technique of Girsanov’s theorem.

The convergence rate implied by Theorem 2 is minimax-optimal in $d _ { \gamma }$ for a sufficiently smooth manifold, i.e., $\beta \ge \gamma ^ { - 1 } \alpha + 1$ , or relatively large $\gamma$ , i.e., $\gamma \ge \alpha / ( \beta - 1 )$ . However, the term arising from (implicitly) estimating the unknown $\beta$ -smooth manifold structure is $\scriptstyle n ^ { - \frac { \beta \gamma } { 2 \alpha + d } }$ (cf. Theorem B.1 in the appendix), which is suboptimal compared to the minimax rate $n ^ { - \frac { \beta \gamma } { d } }$ Aamari and Levrard (2019); Tang and Yang (2023) in $d _ { \gamma }$ . We suspect that this sub-optimality may not arise from our analysis but rather from adding isotropic Gaussian noises in the forward process (3), which may mask finer details of the manifold structure and lead to an inflated error akin to the Langevin diffusion model with Gaussian-smoothing. In contrast to the Langevin diffusion, employing Gaussian-smoothed score functions at all noise levels during the sampling step in the backward process helps mitigate its impact on directions tangential to the manifold, resulting in a considerably improved error bound ${ \frac { 1 } { \sqrt { n } } } \vee n ^ { - { \frac { \alpha + \gamma } { 2 \alpha + d } } }$ compared to that based on the Langevin diffusion. However, errors accumulated along directions perpendicular to the manifold are less impacted and contribute to the sub-optimal error term $\scriptstyle n ^ { - \frac { \beta \gamma } { 2 \alpha + d } }$ . We leave a formal investigation of this to future research.

# 4 Technical Highlights

In this section, we highlight some technical contributions in the proof.

Langevin diffusion with inaccurate score. Consider a generic diffusion model with negative drift $\widetilde { S }$ (which is the score $\nabla \log p _ { \mathrm { d a t a } , \sigma }$ in our case) and stationary distribution $\widetilde { p }$ (i.e., $p _ { \mathrm { d a t a } , \sigma }$ ),

$$
\mathrm { d } X _ { t } = - \widetilde { S } ( X _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , \quad X _ { 0 } \sim p _ { 0 } ;
$$

and an approximating diffusion model with an estimated negative drift $\widehat S$ ,

$$
\mathrm { d } Y _ { t } = - \widehat { S } \left( Y _ { t } \right) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } , \quad Y _ { 0 } \sim p _ { 0 } .
$$

Let $p _ { t }$ and $\widehat { p } _ { t }$ denote the respective distributions of $X _ { t }$ and $Y _ { t }$ . Note that the score matching loss (7) is averaged over independent and identically distributed (i.i.d.) samples $\{ x _ { i } \} _ { i = 1 } ^ { n } \sim p _ { \mathrm { d a t a } }$ . Consequently, the induced generalization error bound is only averaged over the stationary distribution $\widetilde { p }$ (see Lemma B.5 in Appendix B.2) rather than over both $p _ { t }$ and $t$ . This is in contrast with the forward-backward diffusion, where the score $S ( x , t )$ is dependent on $t$ , and the score matching loss (9) is averaged over time $t \in [ 0 , T ]$ ; so that its generalization error has an $L _ { 2 }$ bound averaged over both $p _ { t }$ and $t$ (see Lemma B.3 in Appendix B.1), facilitating the neat application of Girsanov’s theorem to control the distribution estimation error (see the proof of Lemma B.2 in Appendix D.1, or Song and Ermon (2019); Chen et al. (2022); Oko et al. (2023)). However, the complication in analyzing the Langevin diffusion with inexact drift calls for the more stringent $L _ { \infty }$ or the moment generating function bound (e.g., Dalalyan and Karagulyan (2019); Yang and Wibisono (2022)) than a simple second moment bound in order to analyze the distribution estimation error. In comparison, our analysis demonstrates that a bound on the fourth moment of the score estimation error is sufficient. More specifically, we can invoke Pinsker’s inequality and Girsanov’s Theorem to obtain

$$
\begin{array} { r l } & { d _ { \mathrm { T V } } ^ { 2 } ( p _ { T } , \widehat { p } _ { T } ) \leq \displaystyle \int _ { 0 } ^ { T } \int _ { \mathbb { R } ^ { D } } \left\| \widehat { S } ( x ) - \widetilde { S } ( x ) \right\| ^ { 2 } \frac { p _ { t } ( x ) } { \widetilde { p } ( x ) } \widetilde { p } ( x ) \mathrm { d } x \mathrm { d } t } \\ & { \leq \sqrt { \displaystyle \int _ { \mathbb { R } ^ { D } } \left\| \widehat { S } ( x ) - \widetilde { S } ( x ) \right\| ^ { 4 } \widetilde { p } ( x ) \mathrm { d } x } \cdot \displaystyle \int _ { 0 } ^ { T } \sqrt { \chi ^ { 2 } ( p _ { t } \| \widetilde { p } ) + 1 } \mathrm { d } t , } \end{array}
$$

where the second inequality is due to the Cauchy-Schwarz inequality (over $x$ ). If $\widetilde { p }$ satisfies Poincaré inequality with Poincaré constant $C _ { \mathrm { P I } } ^ { \prime }$ (in our case, we can take $C _ { \mathrm { P I } } ^ { \prime } = C _ { \mathrm { P I } } + \sigma ^ { 2 }$ , see Appendix D.6), then $\chi ^ { 2 } ( p _ { t } \parallel \tilde { p } ) \leq \exp ( - 2 t C _ { \mathrm { P I } } ^ { \prime - 1 } ) \cdot \chi ^ { 2 } ( p _ { 0 } \parallel \tilde { p } )$ . Therefore, by choosing $T = \mathcal { O } \big ( C _ { \mathrm { P I } } ^ { \prime } \big \lfloor \log n \vee \log \big ( \chi ^ { 2 } ( p _ { 0 } \| \widetilde { p } ) \big ) \big \rfloor \big )$ , we can obtain the following using basic algebra,

$$
\begin{array} { r l r } & { } & { d _ { \mathrm { T V } } ( \widehat { p } _ { T } , \widetilde { p } ) \leq n ^ { - 1 } + \sqrt { C _ { \mathrm { P I } } ^ { \prime } } \cdot \Big ( \big ( \chi ^ { 2 } ( p _ { 0 } \| \widetilde { p } ) \big ) ^ { \frac { 1 } { 4 } } + \sqrt { \log n } \Big ) } \\ & { } & { \cdot \left( \displaystyle \int _ { \mathbb { R } ^ { D } } \| \widehat { S } ( x ) - \widetilde { S } ( x ) \| ^ { 4 } \widetilde { p } ( x ) { \mathrm { d } } x \right) ^ { 1 / 4 } . } \end{array}
$$

This inequality relates the distribution estimation error to the fourth-moment of the score estimation error.

Forward-backward diffusion score estimation. Our strategy for bounding the distribution estimation error mainly follows the pipeline of Oko et al. (2023). First, we construct a concrete neural network in $\cal { S } _ { N N }$ to approximate the true score function $\nabla \log p _ { t } ( x )$ . Subsequently, we use the complexity of $\mathit { S } _ { \mathit { N N } }$ to control the generalization bound for the score estimator $\widehat { S }$ , which minimizes the sample score matching loss (9). Finally, we apply Girsanov’s theorem to relate the distribution estimation error with the $L _ { 2 }$ score estimation error Song and Ermon (2019); Chen et al. (2022); Oko et al. (2023). Our main technical novelty occurs in the first step of constructing score approximating neural networks with controlled sizes under manifold structure, as summarized in the following lemma.

Lemma 2. Under the same neural network sizes $\{ ( L _ { k } , W _ { k } , R _ { k } , B _ { k } , V _ { k } ) \} _ { k = 1 } ^ { K }$ and time $T$ as in Theorem $\mathcal { Z }$ , for any $k \in \{ 0 , 1 , \cdots , K { - } 1 \}$ , there exists neural network $\phi _ { k } ( x , t ) \in \Phi ( L _ { k } , W _ { k } , R _ { k } , B _ { k } , V _ { k } )$ so that

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { k } } ^ { t _ { k + 1 } } \int _ { \mathbb { R } ^ { D } } \left\| \phi _ { k } ( x , t ) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t } \\ & { \displaystyle = \left\{ \widetilde { \mathcal { O } } \Big ( t _ { k } ^ { - 1 } n ^ { - \frac { 2 \beta } { 2 \alpha + d } } + n ^ { - \frac { 2 \alpha } { 2 \alpha + d } } \Big ) , \quad i f \tau \leq t _ { k } \leq n ^ { - \frac { 2 } { 2 \alpha + d } } ; \right. } \\ & { \left. i f n ^ { - \frac { 2 } { 2 \alpha + d } } \leq t _ { k } \leq T . \right. } \end{array}
$$

The proof of this lemma (Appendix C) is substantially more involved under a general (nonlinear) manifold as considered in this paper than under a hyperplane as considered in earlier studies Oko et al. (2023); Chen et al. (2023). The term $n ^ { - \frac { 2 \beta } { 2 \alpha + d } }$ originates from the nonlinearity of the $\beta$ -smooth manifold, where we discretize the manifold with a suitable cover (resolution level varying over $t _ { k }$ ) and approximate its local charts via polynomials of order $\lfloor \beta \rfloor$ (largest integer less than $\beta$ ); see equation (16) in Appendix C. These local polynomials can additionally be efficiently approximated by neural networks with controlled sizes. The term 2α $n ^ { - \frac { 2 \alpha } { 2 \alpha + d } }$ arises from local polynomial approximations to the $\alpha$ -smooth density function within local chart parametrization over compact sets in $\mathbb { R } ^ { d }$ ; refer to equation (27) in Appendix C. The actual proof contains other technical components, such as using neural networks to approximate the local projection map $\mathrm { P r o j } _ { \mathcal { M } }$ onto the manifold and local inner products over the manifold; see Lemma C.8. Some of these bounds are also utilized in the analysis of the score estimation error under the Langevin diffusion model (e.g., Lemma B.5).

# 5 Discussion

In this study, we explored theoretical properties of two prevalent diffusion models for sampling from complex data distributions, demonstrating that both models can accommodate general manifold structures of the data by showing that the convergence rates of their induced distribution estimators only depend on the manifold intrinsic dimension. Our results strengthen the findings of some existing studies, which either focus on distributions supported on (potentially known) hyperplanes or provide non-quantitative bounds. Additionally, we showed that the forward-backward diffusion achieves the corresponding minimax optimal rate under the 1-Wasserstein metric. Some possible future directions include improving the analysis of the Langevin diffusion model and its score estimation method, analyzing the discretization error arising from simulating the continuous-time diffusion, as well as proposing data-driven methods that can accommodate unknown intrinsic dimension $d$ and smoothness levels $( \alpha , \beta )$ for both diffusion-based generative models.

# References

Aamari, E. and Levrard, C. (2019) Nonasymptotic rates for manifold, tangent space and curvature estimation. The Annals of Statistics, 47, 177 – 204.   
Belomestny, D., Moulines, E., Naumov, A., Puchkin, N. and Samsonov, S. (2021) Rates of convergence for density estimation with generative adversarial networks. arXiv e-prints, arXiv–2102.   
Besson, G., Courtois, G. and Hersonsky, S. (2018) Poincar\’e inequality on complete riemannian manifolds with ricci curvature bounded below. arXiv preprint arXiv:1801.04216.   
Chae, M. (2022) Rates of convergence for nonparametric estimation of singular distributions using generative adversarial networks. arXiv preprint arXiv:2202.02890.   
Chen, M., Huang, K., Zhao, T. and Wang, M. (2023) Score approximation, estimation and distribution recovery of diffusion models on low-dimensional data. arXiv preprint arXiv:2302.07194.   
Chen, S., Chewi, S., Li, J., Li, Y., Salim, A. and Zhang, A. R. (2022) Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions. arXiv preprint arXiv:2209.11215.   
Cheng, Y., Gong, Y., Liu, Y., Song, B. and Zou, Q. (2021) Molecular design in drug discovery: a comprehensive review of deep generative models. Briefings in bioinformatics, 22, bbab344.   
Dalalyan, A. S. (2017) Theoretical guarantees for approximate sampling from smooth and log-concave densities. Journal of the Royal Statistical Society Series B: Statistical Methodology, 79, 651–676.   
Dalalyan, A. S. and Karagulyan, A. (2019) Userfriendly guarantees for the langevin monte carlo with inaccurate gradient. Stochastic Processes and their Applications, 129, 5278–5311.   
De Bortoli, V. (2022) Convergence of denoising diffusion models under the manifold hypothesis. arXiv preprint arXiv:2208.05314.   
De Bortoli, V., Thornton, J., Heng, J. and Doucet, A. (2021) Diffusion schrödinger bridge with applications to score-based generative modeling. Advances in Neural Information Processing Systems, 34, 17695–17709.   
Divol, V. (2022) Measure estimation on manifolds: an optimal transport approach. Probability Theory and Related Fields, 183, 581–647.   
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A. and Bengio, Y. (2014) Generative adversarial nets. Advances in neural information processing systems, 27.   
Haussmann, U. G. and Pardoux, E. (1986) Time reversal of diffusions. The Annals of Probability, 1188– 1205.   
Ho, J., Jain, A. and Abbeel, P. (2020) Denoising diffusion probabilistic models. Advances in neural information processing systems, 33, 6840–6851.   
Huggins, J. and Zou, J. (2017) Quantifying the accuracy of approximate diffusions and markov chains. In Artificial Intelligence and Statistics, 382–391. PMLR.   
Kim, J., Shin, J., Rinaldo, A. and Wasserman, L. (2019) Uniform convergence rate of the kernel density estimator adaptive to intrinsic volume dimension. In International Conference on Machine Learning, 3398–3407. PMLR.   
Kingma, D. P. and Welling, M. (2013) Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114.   
Kong, Z., Ping, W., Huang, J., Zhao, K. and Catanzaro, B. (2020) Diffwave: A versatile diffusion model for audio synthesis. arXiv preprint arXiv:2009.09761.

Lan, L., You, L., Zhang, Z., Fan, Z., Zhao, W., Zeng, N., Chen, Y. and Zhou, X. (2020) Generative adversarial networks and its applications in biomedical informatics. Frontiers in public health, 8, 164.

Lee, H., Lu, J. and Tan, Y. (2023) Convergence of score-based generative modeling for general data distributions. In International Conference on Algorithmic Learning Theory, 946–985. PMLR.

Li, X., Wu, Y., Mackey, L. and Erdogdu, M. A. (2019) Stochastic runge-kutta accelerates langevin monte carlo and beyond. Advances in neural information processing systems, 32.

Liang, T. (2021) How well generative adversarial networks learn distributions. The Journal of Machine Learning Research, 22, 10366–10406.

Mertin, M. (2022) Long-time behaviour of Langevintype dynamics on Riemannian manifolds and scaling limits. Ph.D. thesis, Technische Universität Kaiserslautern.

Nadkarni, P. M., Ohno-Machado, L. and Chapman, W. W. (2011) Natural language processing: an introduction. Journal of the American Medical Informatics Association, 18, 544–551.

Nichol, A. Q. and Dhariwal, P. (2021) Improved denoising diffusion probabilistic models. In International Conference on Machine Learning, 8162–8171.

Oko, K., Akiyama, S. and Suzuki, T. (2023) Diffusion models are minimax optimal distribution estimators. arXiv preprint arXiv:2303.01861.

Papamakarios, G., Nalisnick, E., Rezende, D. J., Mohamed, S. and Lakshminarayanan, B. (2021) Normalizing flows for probabilistic modeling and inference. The Journal of Machine Learning Research, 22, 2617–2680.

Park, S.-W., Ko, J.-S., Huh, J.-H. and Kim, J.-C. (2021) Review on generative adversarial networks: focusing on computer vision and its applications. Electronics, 10, 1216.

Pidstrigach, J. (2022) Score-based generative models detect manifolds. Advances in Neural Information Processing Systems, 35, 35852–35865.

Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E. L., Ghasemipour, K., Gontijo Lopes, R., Karagol Ayan, B., Salimans, T. et al. (2022) Photorealistic text-to-image diffusion models with deep language understanding. Advances in Neural Information Processing Systems, 35, 36479–36494.

Salakhutdinov, R. (2015) Learning deep generative models. Annual Review of Statistics and Its Application, 2, 361–385.

Song, Y. and Ermon, S. (2019) Generative modeling by estimating gradients of the data distribution. Advances in neural information processing systems, 32.

Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S. and Poole, B. (2020) Score-based generative modeling through stochastic differential equations. arXiv preprint arXiv:2011.13456.

Tang, R. and Yang, Y. (2021) On empirical bayes variational autoencoder: An excess risk bound. In Conference on Learning Theory, 4068–4125.

(2023) Minimax rate of distribution estimation on unknown submanifolds under adversarial losses. The Annals of Statistics, 51, 1282–1308.

Turhan, C. G. and Bilge, H. S. (2018) Recent trends in deep generative models: a review. In 2018 3rd International Conference on Computer Science and Engineering (UBMK), 574–579. IEEE.

Uppal, A., Singh, S. and Póczos, B. (2019) Nonparametric density estimation & convergence rates for gans under besov ipm losses. Advances in neural information processing systems, 32.

Vincent, P. (2011) A connection between score matching and denoising autoencoders. Neural computation, 23, 1661–1674.

Wang, Z., She, Q. and Ward, T. E. (2021) Generative adversarial networks in computer vision: A survey and taxonomy. ACM Computing Surveys (CSUR), 54, 1–38.

Yang, K. Y. and Wibisono, A. (2022) Convergence in kl and rényi divergence of the unadjusted langevin algorithm using estimated score. In NeurIPS 2022 Workshop on Score-Based Methods.

Zhang, S., Chewi, S., Li, M., Balasubramanian, K. and Erdogdu, M. A. (2023) Improved discretization analysis for underdamped langevin monte carlo. In The Thirty Sixth Annual Conference on Learning Theory, 36–71. PMLR.

# Checklist

1. For all models and algorithms presented, check if you include:

(a) A clear description of the mathematical setting, assumptions, algorithm, and/or model. [Yes]   
(b) An analysis of the properties and complexity (time, space, sample size) of any algorithm. [Not Applicable]   
(c) (Optional) Anonymized source code, with specification of all dependencies, including external libraries. [Not Applicable]

2. For any theoretical claim, check if you include:

(a) Statements of the full set of assumptions of all theoretical results. [Yes]   
(b) Complete proofs of all theoretical results. [Yes]   
(c) Clear explanations of any assumptions. [Yes]

3. For all figures and tables that present empirical results, check if you include:

(a) The code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL). [Not Applicable]   
(b) All the training details (e.g., data splits, hyperparameters, how they were chosen). [Not Applicable]   
(c) A clear definition of the specific measure or statistics and error bars (e.g., with respect to the random seed after running experiments multiple times). [Not Applicable]   
(d) A description of the computing infrastructure used. (e.g., type of GPUs, internal cluster, or cloud provider). [Not Applicable]

4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets, check if you include:

(a) Citations of the creator If your work uses existing assets. [Not Applicable]   
(b) The license information of the assets, if applicable. [Not Applicable]   
(c) New assets either in the supplemental material or as a URL, if applicable. [Not Applicable]   
(d) Information about consent from data providers/curators. [Not Applicable]   
(e) Discussion of sensible content if applicable, e.g., personally identifiable information or offensive content. [Not Applicable]

5. If you used crowdsourcing or conducted research with human subjects, check if you include:

(a) The full text of instructions given to participants and screenshots. [Not Applicable]   
(b) Descriptions of potential participant risks, with links to Institutional Review Board (IRB) approvals if applicable. [Not Applicable]   
(c) The estimated hourly wage paid to participants and the total amount spent on participant compensation. [Not Applicable]

# Supplementary Materials for “Adaptivity of Diffusion Models to Manifold Structures”

Notation: We adopt the notations in the main text, and further introduce the following additional notations for technical proofs. We use $\mathbf { 1 } ( \cdot )$ to denote the indicator function so that $\mathbf { 1 } ( x \in A ) = 1$ if $x \in A$ and zero otherwise. For a finite set $A$ , we use $| A |$ to denote its cardinality. We use $\operatorname* { d e t } ( \cdot )$ to denote the determinant of sqaure matrices. For any positive integer $m$ , we use the shorthand $[ m ] : = \{ 1 , 2 , \cdots , m \}$ . We use $ { \mathbb { N } } _ { 0 }$ to denote the set of nonnegative integers and $\mathbb { N } _ { 0 } ^ { d } = \{ ( i _ { 1 } , i _ { 2 } , \cdot \cdot \cdot , i _ { d } ) : i _ { k } \in \mathbb { N } _ { 0 }$ , $\forall k \in [ d ] \}$ to denote the set of $d$ -dimensional multi-index. For a multi-index $i \in \mathbb { N } _ { 0 } ^ { d }$ , we denote $| i | = i _ { 1 } + i _ { 2 } + \cdot \cdot \cdot + i _ { d }$ . We use $\textstyle { \mathcal { N } } ( { \boldsymbol { \mu } } , { \boldsymbol { \Sigma } } )$ to denote the (multivariate) Gaussian distribution with mean $\mu$ and covariance matrix $\Sigma$ . For $\alpha \in \mathbb { R }$ , the floor and ceiling functions are denoted by $\lfloor \alpha \rfloor$ and $\lceil \alpha \rceil$ , indicating rounding $\alpha$ to the next smaller and larger integer. For two sequences $\{ a _ { n } \}$ and $\left\{ b _ { n } \right\}$ , we use the notation $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ to mean $a _ { n } \leq C b _ { n }$ and $a _ { n } \geq C b _ { n }$ , respectively, for some constant $C > 0$ independent of $n$ . In addition, $a _ { n } \asymp b _ { n }$ means that both $a _ { n } \lesssim b _ { n }$ and $a _ { n } \gtrsim b _ { n }$ hold. For any measure $\nu$ on $\mathcal { Z }$ and map $G : { \mathcal { Z } }  { \mathcal { X } }$ , we denote $G _ { \# } \nu$ as the push forward measure, which is defined as the unique measure on $\mathcal { X }$ such that $G _ { \# } \nu ( A ) = \nu \bigl ( G ^ { - 1 } ( A ) \bigr )$ holds for any measurable set $A$ on $\mathcal { X }$ . For a probability measure $\mu$ $\nu$ and a measurable set where $\mu$ is absolutely continuous with respect to $\Omega$ , we use $\mu | _ { \Omega }$ to denote the restriction of $\nu$ , we use $\frac { \mathrm { d } \mu } { \mathrm { d } \nu }$ t $\mu$ on denote the Radon-Nikodym derivativ $\Omega$ . For two probability measures $\mu$ and of $\mu$ with respect to $\nu$ . The KL divergence between and $\nu$ is denoted by $\operatorname { K L } ( \mu \parallel \nu )$ and is defined as $\textstyle \int \log ( { \frac { \mathrm { d } \mu } { \mathrm { d } \nu } } ) \mathrm { d } \mu$ The $\chi ^ { 2 }$ divergence between $\mu$ and $\nu$ is denoted by $\chi ^ { 2 } ( \mu \parallel \nu )$ and is defined as $\textstyle \int ( { \frac { \mathrm { d } \mu } { \mathrm { d } \nu } } - 1 ) ^ { 2 } \mathrm { d } \nu$ . The total variation distance between $\mu$ and $\nu$ is denoted by $d _ { \mathrm { T V } } ( \mu , \nu )$ and is defined as $\textstyle \int { \frac { 1 } { 2 } } { \big | } { \frac { \mathrm { d } \mu } { \mathrm { d } \nu } } - 1 { \big | } \mathrm { d } \nu$ . When no ambiguity arises, for an absolutely continuous probability measure $\mu$ , we may also use $\mu$ to refer its density function. We use $\| \cdot \| _ { p }$ to denote the usual vector $\ell _ { p }$ norm, and reserve $\| \cdot \|$ for the $\ell _ { 2 }$ norm (that is, suppress the subscript when $p = 2$ ). We use $0 _ { d }$ to denote the $d$ -dimensional all zero vector, and $\mathbb { B } _ { r } ( x )$ the closed ball centered at $x$ with radius $r$ (under the $\ell _ { 2 }$ distance) in the Euclidean space. For the neural network class $\Phi ( L , W , R , B , V )$ defined in the main text, when there is no constraint on $V$ , we write $\Phi ( L , W , R , B ) = \Phi ( L , W , R , B , \infty )$ .

# Contents

A Regularity of Submanifold 2   
B Proofs of Main Result 3   
B.1 Forward backward diffusion model 3   
B.2 Langevin diffusion model 5   
C Proof of Lemma B.3 6   
C.1 Case 1: $n ^ { - 2 \delta } ( \log n ) ^ { - 3 } \leq \underline { { t } } \leq T$ 7   
C.2 Case 2: $n ^ { - \frac { 2 } { 2 \alpha + d } } \leq \underline { { t } } \leq n ^ { - 2 \delta } ( \log n ) ^ { - 3 }$ 11   
C.3 Case 3: $\tau \leq \underline { { t } } \leq n ^ { - \frac { 2 } { 2 \alpha + d } }$ 16   
D Proof of Technical Lemmas 21   
D.1 Proof of Lemma B.2 21   
D.2 Proof for Lemma C.1 . 23   
D.3 Proof of Lemma C.2 24   
D.4 Proof of Lemma C.3 25   
D.5 Proof of Lemma C.8 26   
D.6 Proof of Lemma B.4 29   
D.7 Proof of Lemma B.5 30   
D.8 Analysis of KDE as initial distribution in Langevin diffusion . 31

# A Regularity of Submanifold

Definition (Submanifold): A subset $\mathcal { M }$ of $\mathbb { R } ^ { D }$ is a $d$ -dimensional submanifold if for every point $x$ in $\mathcal { M }$ , there exists a neighbourhood $V$ of $x$ on $\mathcal { M }$ and an open set $U \subseteq \mathbb { R } ^ { d }$ , such that that there exists a homeomorphism $\xi$ that maps $V$ to $U$ , that is, $\xi : V \to U$ is bijective and both $\xi$ and $\xi ^ { - 1 }$ are continuous maps. We call $( V , \xi )$ a local coordinate chart of $\mathcal { M }$ near $x$ , and $\xi$ a coordinate map around $x$ .

Definition (Reach): The reach of a closed subset $A \subset \mathbb { R } ^ { D }$ is defined as

$$
\tau _ { A } = \operatorname* { i n f } _ { p \in A } \mathrm { d i s t } ( p , \mathrm { M e d } ( A ) ) = \operatorname* { i n f } _ { z \in \mathrm { M e d } ( A ) } \mathrm { d i s t } ( z , A )
$$

where $\begin{array} { r } { \mathrm { d i s t } ( z , A ) \ : = \ : \operatorname* { i n f } _ { p \in A } \| p - z \| } \end{array}$ denotes the distance function to $A$ , and $\operatorname { M e d } ( A )$ is the medial axis of $A$ consisting of the points that have at least two nearest neighbors on $A$ , or

$$
\operatorname { M e d } ( A ) = \left\{ z \in \mathbb { R } ^ { D } \mid \exists p \neq q \in A , \| p - z \| = \| q - z \| = \operatorname { d i s t } ( z , A ) \right\} .
$$

The reach is the largest distance $\rho \geq 0$ such that the projection to $A$ is well defined on the $\rho$ -offset $\left\{ x \in \mathbb { R } ^ { D } \mid \operatorname { d i s t } ( x , A ) < \rho \right\}$ .

Definition (Smooth Manifold): We say that a submanifold $\mathcal { M }$ is $\beta$ -smooth if there exist positive constants $( r _ { 0 } , L )$ such that for any $x ^ { \ast } \in \mathcal { M }$ , the function $\operatorname { P r o j } _ { T _ { x ^ { * } } \mathcal { M } } ( x - x ^ { * } ) : \mathcal { M } \to T _ { x ^ { * } } \mathcal { M }$ , defined as the projection function of $x - x ^ { * }$ onto the tangent space $T _ { x ^ { * } } { \mathcal { M } }$ of $\mathcal { M }$ at $x ^ { * }$ , is a local diffeomorphism at $x ^ { * }$ with inverse function $\Psi _ { x ^ { * } }$ defined on $\mathbb { B } _ { r _ { 0 } } ( 0 _ { D } ) \cap T _ { x ^ { * } } { \mathcal { M } }$ , and $\Psi _ { x ^ { * } }$ is $\beta$ -Hölder smooth with Hölder norm bounded by $L$ .

Remark A.1. Let $V _ { x ^ { * } } \in \mathbb { R } ^ { D \times d }$ be an arbitrary orthonormal basis of $T _ { x ^ { * } } { \mathcal { M } }$ . Then, $\xi ( x ) = V _ { x ^ { * } } ^ { T } \cdot \operatorname { P r o j } _ { T _ { x ^ { * } } \mathcal { M } } ( x - x ^ { * } )$ serves as a special coordinate map around $x ^ { * }$ with a $\beta$ -smooth inverse $\xi ^ { - 1 } ( z ) = \Psi _ { x ^ { * } } ( V _ { x ^ { * } } z )$ . It is worth noting that, for a manifold $\mathcal { M }$ with positive reach, the $\beta$ -smoothness of $\mathcal { M }$ is equivalent to the existence of $\beta$ -smooth coordinate maps that possess a $\beta$ -smooth inverse (see for example, Lemma $F$ .4 of Tang and Yang (2023)). Consequently, the smoothness of $\mathcal { M }$ is an intrinsic property that does not rely on the the choice of the coordinate map.

Definition (Smooth distribution on a smooth manifold) We say a distribution $\mu ^ { * }$ on a $\beta$ -smooth submanifold $\mathcal { M }$ being $\alpha$ -smooth if, for every $x ^ { * } \in \mathcal { M }$ and $\beta$ -smooth coordinate map $\xi ( \cdot ) : V \to U$ around $x ^ { * }$ that admits a $\beta$ -smooth inverse, the distribution of the local coordinate $\xi ( x )$ for $x \sim \mu ^ { * } | _ { V }$ admits an $\alpha$ -smooth density on $U$ with respect to the Lebesgue measure of $\mathbb { R } ^ { d }$ .

Remark A.2. To ensure compatibility between the smoothness of the density and the smoothness of the manifold, the distribution smoothness parameter $\alpha$ should be smaller than $\beta - 1$ . This is because when considering two coordinate maps $\xi _ { 1 } : V _ { 1 } \to U _ { 1 }$ and $\xi _ { 2 } : V _ { 2 } \to U _ { 2 }$ around a point $x ^ { * }$ , the change of measure formula yields:

$$
\begin{array} { r } { \xi _ { 1 } ) _ { \# } \left( \mu | _ { V _ { 1 } \cap V _ { 2 } } \right) \Big ] \left( \xi _ { 1 } ( x ) \right) = \left[ \left( \xi _ { 2 } \right) _ { \# } \left( \mu | _ { V _ { 1 } \cap V _ { 2 } } \right) \right] \left( \xi _ { 2 } ( x ) \right) \cdot \left| \operatorname* { d e t } \left( \mathrm { d } \left[ \xi _ { 2 } \circ \xi _ { 1 } ^ { - 1 } \right] _ { \xi _ { 1 } ( x ) } \right) \right| , \quad x \in V _ { 1 } \cap V _ { 2 } . } \end{array}
$$

where the differential $\mathrm { d } [ \xi _ { 2 } \circ \xi _ { 1 } ^ { - 1 } ]$ of the transition map $\xi _ { 2 } \circ \xi _ { 1 } ^ { - 1 }$ is $( \beta - 1 )$ -smooth. If the smoothness level $\alpha$ is larger than $\beta - 1$ , it may lead to incompatible definitions of smoothness over the intersection of two coordinate charts. Furthermore, when $\alpha \le \beta - 1$ , an $\alpha$ -smooth distribution on $\mathcal { M }$ can be equivalently defined as a distribution whose density function with respect to the volume measure of $\mathcal { M }$ exists and is $\alpha$ -smooth, as defined in the following.

Definition (Smooth density function): We say a density function $f : \mathcal { M }  \mathbb { R }$ with respect to the volume measure of $\mathcal { M }$ is $\alpha$ -smooth, if for any $x \in \mathcal { M }$ , $f \circ \Psi _ { x } : \mathbb { B } _ { r _ { 0 } } ( 0 _ { D } ) \cap T _ { x } { \mathcal { M } } \to \mathbb { R }$ is $\alpha$ -Hölder smooth with bounded Hölder norm.

Geometric Properties of $\beta$ -smooth manifolds with positive reach: (see for example, Lemma 20 of Divol (2022)) Suppose $\mathcal { M }$ is a $\beta$ -smooth $d$ -dimensional submanifold with $\beta \geq 2$ and reach $\tau _ { \mathcal { M } }$ . Then

1. If $h \leq \frac { \pi _ { M } } { 4 }$ , then there exist some constants $( c , C )$ so that for any $x \in \mathcal { M }$ ,

$$
c h ^ { d } \leq \mathrm { v o l } _ { \mathcal { M } } ( \mathbb { B } _ { h } ( x ) \cap \mathcal { M } ) \leq C h ^ { d } ,
$$

where $\mathrm { v o l } _ { \mathcal { M } }$ denotes the volume measure of $\mathcal { M }$ .

2. For any $h \leq r _ { 0 }$ and $x \in \mathcal { M }$ , $\mathbb { B } _ { h } ( x ) \cap \mathcal { M } \subset \Psi _ { x } \big ( \mathbb { B } _ { h } ( 0 _ { D } ) \cap T _ { x } \mathcal { M } \big ) \subset \mathbb { B } _ { 8 h / 7 } ( x ) \cap \mathcal { M } .$

3. For any $x \in \mathcal { M }$ , denotes $T _ { x } { \mathcal { M } } ^ { \perp }$ as the normal space of $\mathcal { M }$ at $x$ , then there exists a map $N _ { x } : \mathbb { B } _ { r _ { 0 } } ( 0 _ { D } ) \cap$ $T _ { x } { \mathcal { M } } \to T _ { x } { \mathcal { M } } ^ { \perp }$ satisfying $d N _ { x } ( 0 ) = 0$ , and for $u \in B _ { r _ { 0 } } ( 0 _ { D } ) \cap T _ { x } { \mathcal { M } }$ , we have $\Psi _ { x } ( u ) = x + u + N _ { x } ( u )$ with $| N _ { x } ( u ) | \leq L | u | ^ { 2 }$ .

4. If $\mathrm { P r o j } _ { \mathcal { M } } ( z ) = x$ for some $z$ satisfying $\mathrm { d i s t } ( z , \mathcal { M } ) < \tau _ { \mathcal { M } }$ , then $z - x \in T _ { x } \mathcal { M } ^ { \perp }$ .

# B Proofs of Main Result

# B.1 Forward backward diffusion model

We consider metric $d _ { \gamma }$ $0 < \gamma \leq 1$ ) defined as

$$
d _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } ) \leq \operatorname* { s u p } _ { f : \| f ( x ) - f ( y ) \| \leq \| x - y \| ^ { \gamma } } \int f ( x ) \mathrm { d } \mu _ { 1 } - \int f ( x ) \mathrm { d } \mu _ { 2 } .
$$

When $\gamma = 1$ , $d _ { \gamma }$ is equivalent to the 1-Wasserstein distance.

Remark B.1. The smoothness parameter $\gamma$ in $d _ { \gamma }$ characterizes a trade-off between supporting manifold recovery and density estimation on the manifold. A smaller $\gamma$ makes $d _ { \gamma } ( \mu , \nu )$ more sensitive to the misalignment between the supports of $\mu$ and $\nu$ . To see this, define $\begin{array} { r } { \mathrm { d i s t } ( x , A ) = \operatorname* { i n f } _ { y \in A } \| x - y \| } \end{array}$ as the distance from a point $x \in \mathbb { R } ^ { d }$ to a set $A \subset \mathbb { R } ^ { D }$ . Note that $\mathrm { d i s t } ( \cdot , A ) ^ { \gamma }$ is $\gamma$ -smooth for any $\gamma > 0$ . For two distributions $\mu$ and $\nu$ with bounded supports, we may take ${ } ^ { \prime } ( x ) = c \mathrm { d i s t } ( x , \operatorname { s u p p } ( \nu ) ) ^ { \gamma } - c \mathrm { d i s t } ( x , \operatorname { s u p p } ( \mu ) ) ^ { \gamma }$ for some sufficiently small constants $c$ , leading to

$$
\begin{array} { r } { d _ { \gamma } ^ { \mathrm { S } } ( \mu , \nu ) : = \mathbb { E } _ { \mu } \bigl [ \mathrm { d i s t } ( X , \operatorname { s u p p } ( \nu ) ) ^ { \gamma } \bigr ] + \mathbb { E } _ { \nu } \bigl [ \mathrm { d i s t } ( X , \operatorname { s u p p } ( \mu ) ) ^ { \gamma } \bigr ] \leq c ^ { - 1 } d _ { \gamma } ( \mu , \nu ) . } \end{array}
$$

Consequently, an upper bound of $d _ { \gamma }$ implies an error bound on the supporting manifold recovery through discrepancy measure $d _ { \gamma } ^ { \mathrm { s } }$ . As $\gamma$ tends to zero, $d _ { \gamma } ^ { \mathrm { s } } ( \mu , \nu )$ approaches $\mathbb { P } _ { \mu } \bigl ( X \not \in \operatorname { s u p p } ( \nu ) \bigr ) + \mathbb { P } _ { \nu } \bigl ( X \not \in \operatorname { s u p p } ( \mu ) \bigr )$ , which vanishes only if $\mu$ and $\nu$ have perfectly aligned supports.

Theorem B.1. Suppose Assumptions $A$ and $B$ are satisfied, and the drift coefficient $\beta _ { t }$ is infinitely differentiable with respect to $t$ and $\underline { { \beta } } \le \beta _ { t } \le \overline { { \beta } }$ holds uniformly over $t$ for some positive constants $( { \underline { { \beta } } } , { \overline { { \beta } } } )$ . We choose $\tau =$ $c \left( n ^ { - { \frac { 2 \beta } { 2 \alpha + d } } } ( \log n ) ^ { \beta + 1 } \right)$ and e exis $T = C \log n$ constants so that $( c , C )$ . Then for any $\frac { 3 \log \log n } { \log n } \leq \delta \leq$ $\begin{array} { r } { \frac { 2 } { 2 \alpha + d } - \frac { \log \log n } { \log n } } \end{array}$ $\{ L _ { k } , W _ { k } , R _ { k } , B _ { k } , V _ { k } \} _ { k = 0 } ^ { K - 1 }$

$$
\begin{array} { r l } & { \mathbb { E } [ d _ { \gamma } ( \widehat { p } , p _ { \mathrm { d a t a } } ) ] \lesssim n ^ { - \frac { \beta \gamma } { 2 \alpha + d } } ( \log n ) ^ { ( \frac { \beta } { 2 } + \frac { \gamma } { 2 } + 1 ) \gamma } + n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } } \cdot ( \log n ) ^ { \{ ( 9 + \frac { \gamma } { 2 } - \frac { d } { 4 } ) \vee ( \frac { 1 5 } { 2 } + \frac { \gamma } { 2 } + \frac { d } { 4 } ) \vee ( \frac { \alpha + 1 } { 2 } ) \} } } \\ & { \quad + \frac { n ^ { - \frac { 1 } { 2 } + \delta d } \cdot ( \log n ) ^ { d + \frac { \gamma } { 2 } } } { \delta ^ { 4 } } \cdot ( \log ^ { \frac { 3 } { 2 } } n \vee \sqrt { ( \frac { 2 } { \delta } ) + D } ) ) . } \end{array}
$$

Remark B.2. The detailed choices of $\{ L _ { k } , W _ { k } , R _ { k } , B _ { k } , V _ { k } \} _ { k = 0 } ^ { K - 1 }$ are provided in Lemma B.3. If we select 2 $\delta =$ $\frac { 3 \log \log n } { \log n }$ ， , we can recover the result stated in Theorem $\boldsymbol { \mathcal { Z } }$ . However, it is worth noting that the term $\binom { \lceil \frac { 2 } { \delta } \rceil + D } { D }$ introduces $( \log n ) ^ { D }$ in the bound, which might pose challenges for large $D$ . Fortunately, this issue can be resolved by choosing a sufficiently small constant value for $\delta$ . Specifically, when $d \geq 3$ , as the dominant term in the bound is $n ^ { - \frac { \beta \gamma } { 2 \alpha + d } } + n ^ { - \frac { \alpha + \gamma } { 2 \alpha + d } }$ for any $\gamma \leq 1$ , we can set $\begin{array} { r } { \delta = \frac { 1 } { 2 } - ( \frac { \beta \gamma } { 2 \alpha + d } \wedge \frac { \alpha + \gamma } { 2 \alpha + d } ) } \end{array}$ . Consequently, the term $\binom { \lceil \frac { 2 } { \delta } \rceil + D } { D }$ only introduces a constant that is polynomial in $D$ .

Proof. For the sake of simplicity and without loss of generality, in the following analysis, we assume $\mathcal { M } \subset \mathbb { B } _ { 1 } ( 0 _ { D } )$ . Recall that $\begin{array} { r } { \sigma _ { t } = \sqrt { 1 - \exp ( - 2 \int _ { 0 } ^ { t } \beta _ { s } \mathrm { d } s ) } \asymp \sqrt { t \wedge 1 } } \end{array}$ . We first state the following lemma to relate the generalization error of the score function $\nabla \log p _ { t } ( X _ { t } )$ to the generalization error of the distribution $p _ { \mathrm { d a t a } }$ under the $d _ { \gamma }$ metric.

Lemma B.2. Suppose $\begin{array} { r } { \widehat { S } ( x , t ) \lesssim \frac { \sqrt { \log n } } { \sigma _ { t } } } \end{array}$ , then when $\gamma \leq 1$

$$
\gamma \left( { \widehat { p } } , p _ { \mathrm { d a t a } } \right) \lesssim \frac { 1 } { n } + \tau ^ { \frac { \gamma } { 2 } } + \sum _ { i = 0 } ^ { K - 1 } \sqrt { \left( ( t _ { i } ^ { \gamma } \log ^ { \gamma } n ) \wedge 1 \right) \int _ { t _ { i } } ^ { t _ { i + 1 } } \int _ { \mathbb R ^ { D } } \left\| { \widehat { S } } ( x , t ) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) } \mathrm { d } x \mathrm { d } t
$$

The following lemma provides upper bounds to the score approximation error.

Lemma B.3. For $t \in [ \underline { { t } } , \bar { t } ]$ with $1 < \frac { \bar { t } } { \underline { { t } } } \le 2$ :

1. If $\tau \leq \underline { { t } } \leq n ^ { - \frac { 2 } { 2 \alpha + d } }$ , there exists a neural network $\phi _ { s c o r e } \left( x , t \right) \in \Phi ( L , W , R , B , V )$ satisfying

$$
\int _ { t } ^ { t } \int _ { \mathbb { R } ^ { D } } \left\| \phi _ { s c o r e } \left( x , t \right) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t \lesssim \frac { n ^ { - \frac { 2 \beta } { 2 \alpha + d } } \cdot ( \log n ) ^ { \beta + 2 } } { \frac { t } { L } } + n ^ { - \frac { 2 \alpha } { 2 \alpha + d } } \cdot ( \log n ) ^ { \alpha + 1 } .
$$

Here $L$ , $W$ , $R$ , $B$ and $V$ are evaluated as $L = \Theta \left( \log ^ { 4 } n \right)$ , $\| W \| _ { \infty } = \Theta \bigl ( n ^ { \frac { d } { 2 \alpha + d } } ( \log n ) ^ { - \frac { d } { 2 } } \cdot ( \log ^ { 6 } n \vee ( \log n ) ^ { d + 3 } ) \bigr ) _ { ! }$ $R = \Theta \big ( n ^ { \frac { d } { 2 \alpha + d } } ( \log n ) ^ { - \frac { d } { 2 } } \cdot ( \log ^ { 8 } n \vee ( \log n ) ^ { d + 5 } ) \big )$ , $B = \exp \left( \Theta ( \log ^ { 4 } n ) \right)$ and $V = \Theta ( \sqrt { \frac { \log n } { \underline { { t } } } } )$ .

2. For any $\begin{array} { r } { \frac { 3 \log \log { n } } { \log { n } } \leq \delta \leq \frac { 2 } { 2 \alpha + d } - \frac { \log \log { n } } { \log { n } } } \end{array}$ :

(a) If $n ^ { - \frac { 2 } { 2 \alpha + d } } \leq \underline { { t } } \leq n ^ { - 2 \delta } ( \log n ) ^ { - 3 }$ , there exists a neural network ϕscore $( x , t ) \in \Phi ( L , W , R , B , V )$ satisfying

$$
\int _ { \frac { t } { \tau } } ^ { \bar { t } } \int _ { \mathbb { R } ^ { D } } \left\| \phi _ { s c o r e } \left( x , t \right) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t \lesssim \frac { \log ^ { 4 } n } { n } .
$$

Here $L$ , $W$ , $R$ , $B$ and $V$ are evaluated as $L \ = \ \Theta \left( \log ^ { 4 } n \right)$ , $\| W \| _ { \infty } ~ = ~ \Theta \big ( \big ( \underline { { { t } } } \log n \big ) ^ { - \frac { d } { 2 } }$ · $\left[ \log ^ { 6 } n + \right.$ $\mathcal { L } _ { 2 } ( \log n ) ^ { d + 3 } \binom { \mathcal { L } _ { 2 } + D } { D } \Big ] \Big )$ , $R = \Theta \big ( \big ( \underline { { t } } \log n \big ) ^ { - \frac { d } { 2 } } \cdot \big [ \log ^ { 8 } n \vee \mathcal { L } _ { 2 } ( \log n ) ^ { d + 5 } \binom { \mathcal { L } _ { 2 } + D } { D } \big ] \big )$ , $B = \exp \left( \Theta ( \log ^ { 4 } n ) \right)$ and $V = \Theta ( \sqrt { \frac { \log n } { \underline { { t } } } } )$ , where $\begin{array} { r } { \mathcal { L } _ { 2 } = \lceil \frac { \log ( n ^ { - \frac { 1 } { 2 } } ) } { \log ( \sigma _ { \pm } \log ^ { \frac { 3 } { 2 } } n ) } \rceil } \end{array}$ .

(b) If $n ^ { - 2 \delta } ( \log n ) ^ { - 3 } \leq \underline { { t } } \leq T = \Theta ( \log n )$ , there exists a neural network $\phi _ { s c o r e } \left( x , t \right) \in \Phi ( L , W , R , B , V )$ satisfying

$$
\int _ { \frac { t } { 2 } } ^ { \bar { t } } \int _ { \mathbb { R } ^ { D } } \left\| \phi _ { s c o r e } \left( x , t \right) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t \lesssim \frac { \log ^ { 5 } n } { n } .
$$

Here $L$ , $W$ , $R$ , $B$ and $V$ are evaluated as $\begin{array} { r } { L = \Theta \big ( \frac { \log ^ { 2 } n } { \delta ^ { 2 } } \big ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \big ( \frac { n ^ { 2 \delta d } ( \log n ) ^ { 2 d } } { \delta ^ { 3 } } \cdot \big [ \log ^ { 3 } n \vee \binom { \lceil \frac { 1 } { 2 \delta } \rceil + D } { D } \big ] \big ) } \end{array}$ $\begin{array} { r } { R = \Theta \big ( \frac { n ^ { 2 \delta d } ( \log n ) ^ { 2 d + 1 } } { \delta ^ { 4 } } \cdot \big [ \log ^ { 3 } n \vee \big ( \frac { \lceil \frac { 1 } { 2 \delta } \rceil + D } { D } \big ) \big ] \big ) , } \end{array}$ $\begin{array} { r } { B = \exp \left( \Theta \big ( \frac { \log ^ { 2 } n } { \delta ^ { 2 } } \big ) \right) } \end{array}$ and $V = \Theta ( \sqrt { \frac { \log n } { \underline { { { t } } } \wedge 1 } } )$ .

Define $\begin{array} { r } { \ell _ { S } ^ { [ k ] } ( x ) ~ = ~ \int _ { t _ { k } } ^ { t _ { k + 1 } } \int _ { \mathbb { R } ^ { D } } ~ \| S ( x _ { t } , t ) ~ - \nabla \log p _ { t } ( x _ { t } | x ) \| ^ { 2 } p _ { t } ( x _ { t } | x ) \mathrm { d } x _ { t } \mathrm { d } t } \end{array}$ , where $p ( x _ { t } | x )$ is the density function of $\mathcal { N } ( m _ { t } x , \sigma _ { t } ^ { 2 } )$ . Then when $\begin{array} { r } { S ( x _ { t } , t ) \lesssim \sqrt { \frac { \log n } { t \wedge 1 } } } \end{array}$ log nt∧1 , we have

$$
\ell _ { S } ^ { [ k ] } ( x ) \leq \int _ { t _ { k } } ^ { t _ { k + 1 } } \int 2 \cdot \| S ( x _ { t } , t ) \| ^ { 2 } p _ { t } ( x _ { t } | x ) \mathrm { d } x _ { t } \mathrm { d } t + \int _ { t _ { k } } ^ { t _ { k + 1 } } \int 2 \cdot \| \nabla \log p _ { t } ( x _ { t } | x ) \| ^ { 2 } p _ { t } ( x _ { t } | x ) \mathrm { d } x _ { t } \mathrm { d } t ;
$$

Then by Theorem 4.3 of Oko et al. (2023) and Lemma B.3, for any $k \in \{ 0 , 1 , \cdots , K - 1 \}$ ,

$$
\begin{array} { r l } & { \displaystyle \int _ { t _ { k } } ^ { t _ { k + 1 } } \int _ { \mathbb R ^ { D } } \left\| \widehat S ( x , t ) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t \biggr ] } \\ & { \displaystyle \left( \frac { n ^ { - \frac { 2 \beta } { 2 \alpha + d } } ( \log n ) ^ { \beta + 2 } } { t _ { k } } + n ^ { - \frac { 2 \alpha } { 2 \alpha + d } ( \log n ) ^ { \alpha + 1 } } \right) 1 \left( t _ { k } \leq n ^ { - \frac { 2 } { 2 \alpha + d } } \right) + \frac { \log ^ { 5 } n } { n } + \frac { ( \log n ) ^ { 2 } } { n } R _ { k } L _ { k } \log \left( n L _ { k } \log \left( \frac { 1 } { n } \right) \right) } \end{array}
$$

Therefore, combined with Lemma B.2, we can obtain

$$
\begin{array} { r l } { \mathbb { E } \{ d _ { \tau } ( \widehat { \mu } , p , \widehat { p } _ { \hat { \sigma } \Delta \omega } ) \} \lesssim \tau ^ { \frac { - 1 } { 2 } } + \displaystyle \sum _ { i = 1 } ^ { K - 1 } \sqrt { ( ( \xi ^ { * } ) ^ { 2 } \operatorname* { m a x } ^ { 2 } \pi ) \wedge 1 } \cdot \mathbb { E } [ \int _ { t _ { i } } ^ { t _ { i + 1 } \setminus \tau } \int _ { \partial \tau }  \widehat { S } ( x , t ) - \nabla \log p _ { \mathbb { P } } ( \hat { x } )  ^ { 2 } p _ { \hat { \sigma } } ( x ) \mathrm { d } \Omega  } \\ { \lesssim \tau ^ { \frac { 3 } { 2 } } + \displaystyle \sum _ { i \in \{ 0 , \cdots , K - 1 \} \atop \tau \leq t _ { i } , \Delta \neq 0 } \log ^ { \frac { 3 } { 2 } } n \cdot ( \frac { n \mathrm { g } ^ { \frac { - 5 \sigma ^ { 2 } } { 4 \sigma ^ { 2 } } } \cdot ( 1 6 \mathrm { g } \sigma ) u ^ { \frac { 3 / 2 + 1 } { \sigma ^ { 2 } } } + 1 } { \widehat { \mu } _ { i } ^ { \frac { 5 \sigma ^ { 2 } } { 4 \sigma ^ { 2 } } } } + n ^ { \frac { - 5 \sigma ^ { 2 } } { 4 \sigma ^ { 2 } } } \cdot ( \log \tau ) ^ { \frac { 1 \sigma ^ { 3 } } { \sigma ^ { 2 } } } \cdot \tau _ { i } ^ { \frac { - 5 } { 2 } } ) } & { } \\ {  + \displaystyle \sum _ { i = 0 } ^ { K - 1 } \frac { ( \frac { 1 } { \mu } \log \tau ) ^ { 2 } } { \sqrt { n } } \wedge 1 \cdot \log n \cdot \sqrt { R } _ { i } \int _ { t _ { i } } \log ( n L _ { i }  W _ { i }  _ { \infty } B _ { i } ) } & { } \\  \lesssim n ^ { - \frac { \sigma ^ { 2 } } { 2 \sigma ^ { 2 } } } ( \log n ) ^ { \frac { \sigma ^ { 2 } } { 4 } } \end{array}
$$

# B.2 Langevin diffusion model

Consider the Langevin diffusion model

$$
\begin{array} { c } { { \mathrm { d } X _ { t } = - \widetilde { S } ( X _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } } } \\ { { X _ { 0 } \sim p _ { 0 } , } } \end{array}
$$

where $\widetilde { S }$ is the score function of the Gaussian-smoothed data distribution with noise level $\sigma$ , i.e.,

$$
\widetilde { S } ( x ) = \frac { \mathbb { E } _ { p _ { \mathrm { d a t a } } } ( X - x ) \exp ( - \frac { \| X - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) } { \sigma ^ { 2 } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \exp ( - \frac { \| X - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) } .
$$

And the estimated Langevin diffusion model

$$
\begin{array} { c } { \mathrm { d } Y _ { t } = - \widehat { S } ( Y _ { t } ) \mathrm { d } t + \sqrt { 2 } \mathrm { d } B _ { t } } \\ { Y _ { 0 } \sim p _ { 0 } . } \end{array}
$$

Let $\widehat { p } _ { T }$ denote the distribution of $Y _ { T }$ and $\widetilde { p } = p _ { \mathrm { d a t a } , \sigma } = p _ { \mathrm { d a t a } } * \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } )$ . We have the following lemma.

Lemma B.4. Suppose Assumption $C$ is satisfied. Then set $T = \Theta \big ( ( C _ { \mathrm { P I } } + \sigma ^ { 2 } ) \cdot [ \log n \vee \log \chi ^ { 2 } ( p _ { 0 } \left. \widetilde { p } \right. ] \big )$ , we have

$$
d _ { \mathrm { T V } } ( \widehat { p } _ { T } , \widetilde { p } ) \lesssim \sqrt { C _ { \mathrm { P I } } + \sigma ^ { 2 } } \cdot \Big ( ( \chi ^ { 2 } ( p _ { 0 } \| \widetilde { p } ) ) ^ { \frac { 1 } { 4 } } + \sqrt { \log n } \Big ) \cdot \Big ( \mathbb { E } _ { \widetilde { p } } \Big [ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 4 } \Big ] \Big ) ^ { \frac { 1 } { 4 } } + \frac { 1 } { n } .
$$

Then we state the following lemma for bounding $\left( \mathbb { E } _ { \widetilde { p } } \left[ \lVert \widetilde { S } ( x ) - \widehat { S } ( x ) \rVert ^ { 4 } \right] \right) ^ { \frac { 1 } { 4 } }$

Lemma B.5. Suppose Assumptions $A$ and $B$ are satisfied. If we choose

$$
\widehat { S } = \operatorname* { a r g m i n } _ { S \in \Phi ( L , W , R , B , V ) } n ^ { - 1 } \sum _ { i = 1 } ^ { n } \mathbb { E } _ { z \sim \mathcal { N } ( x _ { i } , \sigma ^ { 2 } I _ { D } ) } \left\| s ( z ) - \frac { x _ { i } - z } { \sigma ^ { 2 } } \right\| ^ { 2 }
$$

with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \bigl ( ( h \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } ( \log ^ { 6 - \frac { d } { 2 } } n \vee \log ^ { \frac { d } { 2 } + 3 } n ) \bigr )$  , $R = \Theta \bigl ( ( h \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } ( \log ^ { 8 - \frac { d } { 2 } } n \vee$ $\log ^ { \frac { d } { 2 } + 5 } n ) \big$  , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ , and $\begin{array} { r } { V = \Theta ( \frac { \sqrt { \log n } } { \sigma } ) } \end{array}$ . Then for any positive constants $\delta _ { 1 } , \delta _ { 2 }$ and $\sigma$ satisfying $n ^ { - \delta _ { 1 } } \lesssim \sigma \lesssim n ^ { - \delta _ { 2 } }$ , we have

1. If $\sigma > n ^ { - \frac { 1 } { 2 \alpha + d } }$ , then

$$
\begin{array} { r } { \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \left( \mathbb { E } _ { \widetilde { p } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 4 } \right] \right) ^ { \frac { 1 } { 4 } } \right] \lesssim n ^ { - \frac { 1 } { 4 } } \sigma ^ { - \frac { d } { 4 } - 1 } \left( \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \vee \log ^ { \frac { d } { 8 } + \frac { 1 5 } { 4 } } n \right) . } \end{array}
$$

2. If $\sigma \leq n ^ { - \frac { 1 } { 2 \alpha + d } }$ , then

$$
\begin{array} { r } { _ { \mathfrak { a } ^ { \otimes n } } \left[ \left( \mathbb { E } _ { \widetilde { \mathcal { P } } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 4 } \right] \right) ^ { \frac { 1 } { 4 } } \right] \lesssim \frac { n ^ { - \frac { \beta } { 4 \alpha + 2 d } } } { \sigma ^ { \frac { 3 } { 2 } } } \log ^ { \frac { \beta + 3 } { 4 } } n + \frac { n ^ { - \frac { \alpha } { 4 \alpha + 2 d } } } { \sigma } \left( \log ^ { \frac { \alpha + 2 } { 4 } } n \vee \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \vee \log ^ { \frac { 1 5 } { 4 } + \frac { \alpha } { 4 } } \right) } \end{array}
$$

Then denote $\widehat { p }$ as the distribution of $Y _ { T } \cdot \mathbf { 1 } ( \| Y _ { T } \| _ { \infty } \leq L )$ and $\widetilde { p } ^ { \prime }$ as the distribution of $X \cdot \mathbf { 1 } ( \| X \| _ { \infty } \leq L )$ with $X \sim p$ b. Based on $\mathcal { M } \subset B _ { L / 2 } ( 0 _ { D } )$ , we can get

$$
\begin{array} { r l } & { W _ { 1 } ( \widetilde { p } ^ { \prime } , p _ { \mathrm { d a t a } } ) \leq \underset { z \sim \mathcal { N } ( 0 , t _ { D } ) } { \underline { { \mathbb { E } } } } \| x - ( x + \sigma z ) \mathbf { 1 } ( \| x + \sigma z \| _ { \infty } \leq L ) \| } \\ & { \qquad \leq \underset { z \sim \mathcal { N } ( 0 , t _ { D } ) } { \underline { { \mathbb { E } } } } \| x - ( x + \sigma z ) \| } \\ & { \qquad \lesssim \sigma . } \end{array}
$$

Furthermore, combined with Lemma B.4 and B.5, we can obtain

1. When $\sigma > n ^ { - \frac { 1 } { 2 \alpha + d } }$ ,

$$
\begin{array} { r l } & { \cdot _ { p _ { \mathrm { d a t a } } \otimes n } [ W _ { 1 } ( \widehat { p } , \widetilde { p } ^ { \prime } ) ] \lesssim \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } [ d _ { \mathrm { T V } } ( \widehat { p } , \widetilde { p } ^ { \prime } ) ] } \\ & { \qquad \leq \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } [ d _ { \mathrm { T V } } ( \widehat { p } _ { T } , \widetilde { p } ) ] } \\ & { \qquad \lesssim \sqrt { C _ { \mathrm { P I } } + \sigma ^ { 2 } } \cdot \Big ( ( \chi ^ { 2 } ( p _ { 0 } \left. \widetilde { p } \right. ) ^ { \frac { 1 } { \delta } } + \sqrt { \log n } \Big ) \cdot n ^ { - \frac { 1 } { 4 } } \sigma ^ { - \frac { d } { 4 } - 1 } \left( \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \vee \log ^ { \frac { d } { 8 } + \frac { 1 5 } { 4 } } + \sqrt { \log n } \right) \Big ) ^ { \frac { 1 } { \delta } } } \end{array}
$$

2. When $\sigma \leq n ^ { - \frac { 1 } { 2 \alpha + d } }$ ,

$$
\begin{array} { r l } & { \cdots \bigl [ W _ { 1 } ( \widehat { p } , \widetilde { p } ^ { \prime } ) \bigr ] \lesssim \mathop { \mathbb { E } } _ { p _ { \mathrm { d a t a } } \otimes n } \bigl [ d _ { \mathrm { T V } } ( \widehat { p } , \widetilde { p } ^ { \prime } ) \bigr ] \leq \mathop { \mathbb { E } } _ { p _ { \mathrm { d a t a } } \otimes n } \bigl [ d _ { \mathrm { T V } } ( \widehat { p } _ { T } , \widetilde { p } ) \bigr ] } \\ & { \qquad \times _ { \mathrm { I } } + \sigma ^ { 2 } \cdot \Bigl ( ( \chi ^ { 2 } ( p _ { 0 } \| \widehat { p } ) ) ^ { \frac { 1 } { 4 } } + \sqrt { \log n } \Bigr ) \cdot \biggl ( \frac { n ^ { - \frac { \beta } { 4 \sigma + 2 d } } } { \sigma ^ { \frac { 3 } { 2 } } } \log ^ { \frac { \beta + 3 } { 4 } } n + \frac { n ^ { - \frac { \alpha } { 4 \sigma + 2 d } } } { \sigma } \Bigl ( \log ^ { \frac { \alpha + 2 } { 4 } } n \vee \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \vee \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \vee \log ^ { \frac { 9 } { 2 } - \frac { d } { 8 } } n \Bigr ) . } \end{array}
$$

We can obtain the desired result in Theorem 1 by combining (1), (2), and (3).

# C Proof of Lemma B.3

To begin with, we introduce the following lemma, which states that it is sufficeint to approximate the score function $\nabla \log p _ { t } ( x )$ only for values of $x$ that are in close proximity to the manifold.

Lemma C.1. If sup sup $[ \| S ( x , t ) \| _ { \infty } \sigma _ { t } ] \le c \sqrt { \log n }$ . Then, there exist constants $( c _ { 0 } , c _ { 1 } , c _ { 2 } , c _ { 3 } )$ so that for any $i \in \{ 0 , 1 , \cdots , K - 1 \}$ $x \in \mathbb { R } ^ { D } t \in [ \tau , T ]$ and $t \in [ t _ { i } , t _ { i + 1 } ]$ with $\begin{array} { r } { 1 < \frac { t _ { i + 1 } } { t _ { i } } \le 2 } \end{array}$ ,

1. Denote $\mathrm { d i s t } ( x , { \mathcal { M } } )$ as the distance of point $\boldsymbol { x } \in \mathbb { R } ^ { D }$ to manifold $\mathcal { M }$ . Then

$$
\begin{array} { l } { \displaystyle \int \| \nabla \log p _ { t } ( x ) - S ( x , t ) \| ^ { 2 } p _ { t } ( x ) \mathrm { d } x } \\ { \displaystyle \leq \int \| \nabla \log p _ { t } ( x ) - S ( x , t ) \| ^ { 2 } p _ { t } ( x ) \cdot 1 \left( \mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } \right) \mathrm { d } x + ( 1 + c ^ { 2 } ) \cdot c _ { 1 } \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

2. For any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ satisfying $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n }$ , we have

(a) (b) $\begin{array} { r l } & { \| \nabla \log p _ { t } ( x ) \| _ { \infty } \leq c _ { 2 } \frac { \sqrt { \log n } } { \sigma _ { t _ { i } } } } \\ & { \rangle ~ ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } p _ { t } ( x ) \geq n ^ { - c _ { 3 } } . } \end{array}$

Then we use the following lemma to bound the covering number of $\mathcal { M }$ .

Lemma C.2. For any $\epsilon > 0$ there exists an $\epsilon$ -cover $N _ { \epsilon }$ of $\mathcal { M }$ so that $N _ { \epsilon } \subset \mathcal { M }$ and $| N _ { \epsilon } | \lesssim ( \epsilon \wedge 1 ) ^ { - d }$ , moreover, for any $x _ { 0 } \in \mathcal { M }$ and $r \geq \epsilon$ , we have

$$
\left| \{ x \in N _ { \epsilon } : \| x - x _ { 0 } \| \leq r \} \right| \lesssim \bigl ( \frac { r \wedge 1 } { \epsilon \wedge 1 } \bigr ) ^ { d } .
$$

Let us fix a time interval $t \in [ \underline { { t } } , t ]$ where $1 < \frac { \bar { t } } { \underline { { t } } } \le 2$ . According to Lemma C.1, it suffices to focus on approximating√ the score function for $t \in [ \underline { { t } } , \overline { { t } } ]$ and $\boldsymbol { x } \in \mathbb { R } ^ { D }$ with $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ . Our first objective is to demonstrate that if there are neural networks capable of accurately approximating $\nabla \log p _ { t } ( x )$ within local neighborhoods in $\mathcal { M }$ , then there exists a neural network capable of providing a reliable approximation of $\nabla \log p _ { t } ( x )$ for all $x$ satisfying $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ , this is summarized in the following Lemma.

Lemma C.3. Suppose $\tau \leq \underline { { t } } \leq T$ and $\epsilon ^ { * } \geq \sigma _ { \underline { { t } } } \sqrt { \log n }$ . Let $N _ { \epsilon ^ { * } } = \{ Y _ { 1 } ^ { * } , Y _ { 2 } ^ { * } , \cdot \cdot \cdot , Y _ { J ^ { * } } ^ { * } \}$ be an $\epsilon ^ { * }$ -cover of $\mathcal { M }$ satisfying the statements in Lemma C.2. Then if for each $j \in \ [ J ^ { * } ]$ , there exists a neural network $\phi _ { j } ^ { \ast } ( x , t ) \in$ $\Phi \big ( L , W , R , B , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \pm } } ) \big )$ so that for any $t \in [ \underline { { t } } , \bar { t } ]$ and $\boldsymbol { x } \in \mathbb { R } ^ { D }$ satisfying $\| x - Y _ { j } ^ { * } \| \leq \sqrt { 2 } ( \epsilon ^ { * } + c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } )$ and $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ ,

$$
\| \phi _ { j } ^ { * } ( x , t ) - \nabla \log p _ { t } ( x ) \| _ { \infty } \leq \varepsilon .
$$

Then there exists a neural network $\begin{array} { r } { \phi _ { \mathrm { s c o r e } } ( x , t ) \in \big ( L _ { 1 } , W _ { 1 } , R _ { 1 } , B _ { 1 } , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \frac { t } { L } } } ) \big ) } \end{array}$ with $L _ { 1 } = \Theta ( L + \log ^ { 2 } n )$ , $\| W _ { 1 } \| _ { \infty } =$ $\Theta ( J ^ { * } ( \| W \| _ { \infty } + \log n ) + \log ^ { 3 } n )$ , $R _ { 1 } = \Theta ( J ^ { * } ( R + \log n ) + \log ^ { 4 } n )$ and $B _ { 1 } = \exp ( \Theta ( \log ^ { 2 } n ) )$ , so that for any $t \in [ \underline { { t } } , \overline { { t } } ]$ and $\boldsymbol { x } \in \mathbb { R } ^ { D }$ satisfying $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \mathit { t } } \sqrt { \log n }$ ,

$$
\| \phi _ { \mathrm { s c o r e } } ( x , t ) - \nabla \log p _ { t } ( x ) \| _ { \infty } \lesssim \varepsilon + \frac { 1 } { n } .
$$

Recall

$$
\nabla \log p _ { t } ( x ) = \frac { \nabla p _ { t } ( x ) } { p _ { t } ( x ) } ,
$$

where

$$
\nabla p _ { t } ( x ) = ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { - \frac { D } { 2 } } \int \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } ^ { 2 } } \right) f ( y ) \mathrm { d } { \mathrm { v o l } _ { M } ( y ) } ,
$$

and

$$
p _ { t } ( \boldsymbol { x } ) = ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { - \frac { D } { 2 } } \int \exp \left( - \frac { \| \boldsymbol { x } - m _ { t } \boldsymbol { y } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) f ( \boldsymbol { y } ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( \boldsymbol { y } ) ,
$$

with $\begin{array} { r } { m _ { t } = \exp \big ( - \int _ { 0 } ^ { t } \beta _ { s } \mathrm { d } s \big ) } \end{array}$ and $\sigma _ { t } ^ { 2 } = 1 - m _ { t } ^ { 2 }$ satisfying $1 - m _ { t } \asymp t \wedge 1$ and $\sigma _ { t } \asymp \sqrt { t \wedge 1 }$ . By statement 2 of Lemma C.1, there exists a large enough constant √ $c _ { 2 }$ , so that for any $t \in [ \underline { { t } } , t ]$ , $x \in \mathbb { R } ^ { D }$ with $\mathrm { d i s t } ( x , \mathcal { M } ) \leq$ $c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ , and any partition $\{ \mathcal { A } , \mathcal { M } \backslash \mathcal { A } \}$ of $\mathcal { M }$ satisfying $\{ y \in { \mathcal { M } } : \| y - x \| \leq c _ { 2 } \sigma _ { \underline { { t } } } { \sqrt { \log n } } \} \subset { \mathcal { A } }$ , it holds that

$$
\left. \nabla \log p _ { t } ( x ) - \frac { 1 } { \sigma _ { t } } \cdot \frac { \int _ { A } \exp \left( - \frac { \Vert x - m _ { t } y \Vert ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } { \int _ { A } \exp \left( - \frac { \Vert x - m _ { t } y \Vert ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } \right. _ { \infty } \leq \frac { 1 } { n } .
$$

We will approximate $\nabla \log p _ { t } ( x )$ by constructing suitable sets $\boldsymbol { A }$ and considering the approximation of $\int _ { \mathcal { A } } \exp \big ( \mathrm { - }$ $\begin{array} { r } { \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \big ( - \frac { x - m _ { t } y } { \sigma _ { t } } \big ) f ( y ) \operatorname { d } { \operatorname { v o l } _ { \mathcal { M } } ( y ) } } \end{array}$ and $\begin{array} { r } { \int _ { \mathcal { A } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) } \end{array}$ separately.

# C.1 Case 1: $n ^ { - 2 \delta } ( \log n ) ^ { - 3 } \leq \underline { { t } } \leq T$

Let $N _ { \epsilon ^ { * } }$ be an $\epsilon ^ { * }$ -cover of $\mathcal { M }$ with $\epsilon ^ { * } = \sigma _ { \underline { { t } } } \sqrt { \log n }$ so that statements in Lemma C.2 are satisfied. Then the carnidality of $N _ { \epsilon ^ { * } }$ , denoted by $| N _ { \epsilon ^ { * } } |$ , satisfies $| N _ { \epsilon ^ { * } } | = \Theta \bigl ( 1 \vee ( \epsilon ^ { * } ) ^ { - d } \bigr )$ . As per Lemma C.3, our focus lies in constructing approximations of $\nabla \log p _ { t } ( x )$ within local neighborhoods of points inside $N _ { \epsilon ^ { * } }$ . Fix an arbitrary $y ^ { \ast } \in N _ { \epsilon ^ { * } }$ and consider

$$
\begin{array} { r } { x \in \mathcal { S } _ { y ^ { * } } = \{ x \in \mathbb { R } ^ { D } : \| x - y ^ { * } \| \leq \sqrt { 2 } ( \epsilon ^ { * } + c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } ) , \mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} , } \end{array}
$$

we have

$$
y \in { \mathcal { M } } : \| y - x \| \leq c _ { 2 } \sigma _ { t } { \sqrt { \log n } } \} \subset \{ y \in { \mathcal { M } } : \| y - y ^ { * } \| \leq ( c _ { 2 } + { \sqrt { 2 } } + { \sqrt { 2 } } c _ { 0 } ) \sigma _ { t } { \sqrt { \log n } } \} = { \mathcal { A } } .
$$

Then by Lemma C.2, let $\epsilon = n ^ { - 2 \partial } ( \log n ) ^ { - 2 }$ , there exists an $\epsilon$ -cover $\smash { \widetilde { N } _ { \epsilon } }$ of $\mathcal { A }$ so that $\smash { \widetilde { N } _ { \epsilon } \subset \mathcal { A } }$ and

$$
| \widetilde { N } _ { \epsilon } | \lesssim \bigl ( \frac { \sigma _ { \frac { t } { 2 } } \sqrt { \log n } \wedge 1 } { n ^ { - 2 \delta } ( \log n ) ^ { - 2 } } \bigr ) ^ { d } ,
$$

and for any $y \in \mathcal { M }$ ,

$$
\left| \{ y ^ { \prime } \in \widetilde { N } _ { \epsilon } : \| y ^ { \prime } - y \| \le \sqrt { 2 } \epsilon \} \right| = \mathcal { O } ( 1 ) .
$$

Denote $\widetilde { N } _ { \epsilon } = \{ Y _ { 1 } , Y _ { 2 } , \cdot \cdot \cdot , Y _ { J } \}$ and define the following partition functions

$$
\widetilde { \rho } ( x ) = \left\{ \begin{array} { c c } { 1 } & { | x | < 1 } \\ { 0 } & { | x | > 2 } \\ { 2 - | x | } & { 1 < | x | \le 2 } \end{array} \right.
$$

$$
\widetilde { \rho } _ { j } ( \boldsymbol { x } ) = \widetilde { \rho } \left( \frac { \| \boldsymbol { x } - \boldsymbol { Y } _ { j } \| ^ { 2 } } { \epsilon ^ { 2 } } \right) , \quad \rho _ { j } ( \boldsymbol { x } ) = \frac { \widetilde { \rho } _ { j } ( \boldsymbol { x } ) } { \sum _ { j = 1 } ^ { J } \widetilde { \rho } _ { j } ( \boldsymbol { x } ) } \mathrm { ~ f o r ~ } j \in [ J ] .
$$

Since for any $y \in { \cal A }$ : (1) there exists $Y _ { j } \in  { N _ { \epsilon } }$ so that $\| y - Y _ { j } \| \leq \epsilon$ ; (2) there are constant-order number of $Y _ { j } \in  { N _ { \epsilon } }$ so that $\| y - Y _ { j } \| \leq \sqrt { 2 } \epsilon$ , we can obtain $\begin{array} { r } { 1 \leq \sum _ { j = 1 } ^ { J } \widetilde { \rho } _ { j } ( y ) \leq C } \end{array}$ . Then,

$$
\begin{array} { r l } & { \displaystyle \int _ { A } \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } \\ &  = \displaystyle \int _ { A \sum _ { j = 1 } ^ { J } \rho _ { j } ( y ) \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } \\ & { = \displaystyle \sum _ { j = 1 } ^ { J } \int _ { \{ y \in A : \| y - Y _ { j } \| \leq \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) , } \end{array}
$$

where the last inequality uses the fact that $\rho _ { j } ( y ) = 0$ when $\| y - Y _ { j } \| \ge \sqrt { 2 } \epsilon$ . Then based on the decomposition

$$
\lVert x - m _ { t } y \rVert ^ { 2 } = \lVert x - m _ { t } Y _ { j } \rVert ^ { 2 } + 2 \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle + \lVert m _ { t } Y _ { j } - m _ { t } y \rVert ^ { 2 } ,
$$

we can obtain

$$
\begin{array} { r l } & { \displaystyle \int _ { A } \exp ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \cdot ( - \frac { x - m _ { t } y } { \sigma _ { t } } ) f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } \\ & { = \displaystyle \sum _ { j = 1 } ^ { J } [ \int _ { \{ y \in A \colon \| y - Y _ { j } \| \le \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp ( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \cdot \exp ( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } ) \cdot \mathrm { d } \epsilon ] } \\ & { \mathrm { \ ~ \ } \cdot ( - \frac { x - m _ { t } y } { \sigma _ { t } } ) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) \cdot \exp ( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) ] . } \end{array}
$$

Similarly, we have

$$
\begin{array} { l l } { \displaystyle \int _ { A } \exp ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) } \\ { \displaystyle = \sum _ { j = 1 } ^ { J } [ \int _ { \{ y \in A : \| y - Y _ { j } \| \le \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp ( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \cdot \exp ( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } } ) \cdot \mathrm { d } \frac { m _ { t } Y _ { j } } { \sigma _ { t } } ] } \\ { \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) \cdot \exp ( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) ] . } \end{array}
$$

Notice that for any $Y _ { j } \in  { N _ { \epsilon } }$ , $x \in \mathcal { S } _ { y ^ { * } }$ and $t \in [ \underline { { t } } , \overline { { t } } ]$ , we have

$$
\frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \leq C _ { 1 } \log n ,
$$

and for any $\| y - Y _ { j } \| \leq \sqrt { 2 } \epsilon$ ,

$$
\frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \lesssim n ^ { - 2 \delta } ,
$$

and

$$
\left| \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right| \lesssim n ^ { - \delta } .
$$

We can then obtain

$$
\begin{array} { r l r } & { } & { \left| \int _ { \{ y \in A : \Vert y - Y _ { j } \Vert \leq \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \Vert m _ { t } Y _ { j } - m _ { t } y \Vert ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right) \cdot f ( y ) \mathrm { d } y \right| } \\ & { } & { \left| \left| \frac { \int _ { \{ y \in A : \Vert y - Y _ { j } \Vert \leq \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \Vert m _ { t } Y _ { j } - m _ { t } y \Vert ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f ( y ) \mathrm { d } y  } { \int _ { \{ y \in A : \Vert y - Y _ { j } \Vert \leq \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \Vert m _ { t } Y _ { j } - m _ { t } y \Vert ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right) \cdot f ( y ) \mathrm { d } w } \right| } \end{\right|array} \end{array}
$$

and

$$
\left| \exp \left( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \right| \lesssim n ^ { - C _ { 1 } } .
$$

Therefore, if there exist neural networks $\phi _ { j } ^ { [ 1 ] } ( x , t )$ , $\phi _ { j } ^ { [ 2 ] } ( x , t )$ and $\phi _ { j } ^ { [ 3 ] } ( x , t )$ so that for any $j \in [ J ]$ , $x \in \mathcal { S } _ { y ^ { * } }$ and $t \in [ \underline { { t } } , t ]$ ,

$$
\begin{array} { r } { \bigg \| \displaystyle \int _ { \{ y \in A : \| y - Y _ { j } \| \leq \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \left. x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \right. } { \sigma _ { t } ^ { 2 } } \right) } \\ { \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f ( y ) \operatorname { d v o l } _ { M } ( y ) - \phi _ { j } ^ { [ 1 ] } ( x , t ) \bigg \| _ { \infty } \lesssim \epsilon ^ { - d } n ^ { - \delta - \frac { 1 } { 2 } } \sqrt { \log n } , } \end{array}
$$

$$
\bigg | \int _ { \{ y \in A : \| y - Y _ { j } \| \le \sqrt { 2 } \epsilon \} } \rho _ { j } ( y ) \exp \left( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \left. x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \right. } { \sigma _ { t } ^ { 2 } } \right)
$$

and

$$
\left| \exp \left( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) - \phi _ { j } ^ { [ 3 ] } ( x , t ) \right| \leq n ^ { - C _ { 1 } - \frac { 1 } { 2 } - \delta } .
$$

We have

$$
\left\| \nabla \log p _ { t } ( x ) - \frac { 1 } { \sigma _ { t } } \cdot \frac { \sum _ { j = 1 } ^ { J } \phi _ { j } ^ { [ 1 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) } { \sum _ { j = 1 } ^ { J } \phi _ { j } ^ { [ 2 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) } \right\| _ { \infty } \lesssim \frac { \log ^ { 2 } n } { \sqrt { n } } .
$$

To construct $\phi _ { j } ^ { [ 1 ] } ( x , t )$ , $\phi _ { j } ^ { [ 2 ] } ( x , t )$ and $\phi _ { j } ^ { [ 3 ] } ( x , t )$ , we consider the following lemmas in Oko et al. (2023) for the approximation of $m _ { t }$ , $\sigma _ { t }$ , exponential function, monomial and reciprocal function.

Lemma C.4. (Lemma 3.3 in Oko et al. (2023)) There exist neural networks $\phi _ { m } ( t ) , \phi _ { \sigma } ( t ) \in \Phi ( L , W , B , R )$ that approximates $m _ { t }$ and $\sigma _ { t }$ up to $\varepsilon$ for al l $t \geq 0$ , where $L = \mathcal { O } \left( \log ^ { 2 } \left( \varepsilon ^ { - 1 } \right) \right) , \| W \| _ { \infty } = \mathcal { O } \left( \log ^ { 3 } \left( \varepsilon ^ { - 1 } \right) \right) , R =$ ${ \mathcal { O } } \left( \log ^ { 4 } \left( \varepsilon ^ { - 1 } \right) \right)$ , and $B = \exp { \left( \mathcal { O } \left( \log ^ { 2 } { \left( \varepsilon ^ { - 1 } \right) } \right) \right) }$ .

Lemma C.5. (Lemma $F . 1 2$ in Oko et al. (2023)) Take $\varepsilon > 0$ arbitrarily. There exists a neural network $\phi _ { \mathrm { e x p } } \in \Phi ( L , W , R , B )$ such that

$$
\operatorname* { s u p } _ { x , x ^ { \prime } \geq 0 } \left. e ^ { - x ^ { \prime } } - \phi _ { \mathrm { e x p } } ( x ) \right. \leq \varepsilon + \vert x - x ^ { \prime } \vert
$$

holds, where $L = \mathcal { O } \left( \log ^ { 2 } \varepsilon ^ { - 1 } \right) , \| W \| _ { \infty } = \mathcal { O } \left( \log \varepsilon ^ { - 1 } \right) , R = \mathcal { O } \left( \log ^ { 2 } \varepsilon ^ { - 1 } \right) , B = \exp \left( \mathcal { O } \left( \log ^ { 2 } \varepsilon ^ { - 1 } \right) \right) .$ Moreover, $| \phi _ { \mathrm { e x p } } ( x ) | \le \varepsilon$ for al l $x \geq \log 3 \varepsilon ^ { - 1 }$ .

Lemma C.6. (Lemma F.6 in Oko et al. (2023)) Let $d \ge 2 , C \ge 1 , 0 < \varepsilon _ { e r r o r } \ \le 1$ . For any $\varepsilon > 0$ , there exists a neural network $\phi _ { m u l t } \left( x _ { 1 } , x _ { 2 } , \cdot \cdot \cdot , x _ { d } \right) \in \Phi ( L , W , R , B )$ with $L = \mathcal { O } \left( \log d \left( \log \varepsilon ^ { - 1 } + d \log C \right) \right) , \| W \| _ { \infty } = 4 8 d$ , $R = \mathcal { O } \left( d \log \varepsilon ^ { - 1 } + d \log C \right) , B = C ^ { d }$ such that

$$
\left| \phi _ { m u l t } \left( x _ { 1 } ^ { \prime } , x _ { 2 } ^ { \prime } , \cdots , x _ { d } ^ { \prime } \right) - \prod _ { d ^ { \prime } = 1 } ^ { d } x _ { d ^ { \prime } } \right| \leq \varepsilon + d C ^ { d - 1 } \varepsilon _ { e r r o r } , \ f o r \ a l l \ x \in [ - C , C ] ^ { d } \ a n d \ x ^ { \prime } \in \mathbb { R } \ w i t h
$$

and $| \phi _ { m u l t } ( x ) | \leq C ^ { d }$ for al l $x \in [ - C , C ]$ . Note that some of $x _ { i } , x _ { j } ( i \neq j )$ can be shared. For $\textstyle \prod _ { i = 1 } ^ { I } x _ { i } ^ { \omega _ { i } }$ with $\omega _ { i } \in \mathbb { Z } _ { + } ( i = 1 , 2 , \cdot \cdot \cdot , I )$ and $\textstyle \sum _ { i = 1 } ^ { I } \omega _ { i } = d$ , there exists a neural network satisfying the same bounds as above, and the network is denoted by $\phi _ { m u l t } ( x ; \omega )$ .

Lemma C.7. (Lemma $F . 7$ in Oko et al. (2023)) For any $0 < \varepsilon < 1$ , there exists $\phi _ { r e c } \in \Phi ( L , W , R , B )$ with $L \leq \mathcal { O } \left( \log ^ { 2 } \varepsilon ^ { - 1 } \right) , \| W \| _ { \infty } = \mathcal { O } \left( \log ^ { 3 } \varepsilon ^ { - 1 } \right) , R = \mathcal { O } \left( \log ^ { 4 } \varepsilon ^ { - 1 } \right)$ , and $B = \mathcal { O } \left( \varepsilon ^ { - 2 } \right)$ such that

$$
\left| \phi _ { r e c } \left( x ^ { \prime } \right) - \frac { 1 } { x } \right| \leq \varepsilon + \frac { | x ^ { \prime } - x | } { \varepsilon ^ { 2 } } , ~ f o r ~ a l l ~ x \in \left[ \varepsilon , \varepsilon ^ { - 1 } \right] ~ a n d ~ x ^ { \prime } \in \mathbb { R } .
$$

Since for any $- 1 < z < 1$ , we have $\begin{array} { r } { | \exp ( z ) - \sum _ { l = 0 } ^ { \mathcal { L } } \frac { z ^ { l } } { l ! } | \leq e \frac { | z | ^ { \mathcal { L } + 1 } } { ( \mathcal { L } + 1 ) ! } \leq e \bigl ( \frac { | z | e } { \mathcal { L } + 1 } \bigr ) ^ { \mathcal { L } + 1 } } \end{array}$   |z|e+1 L +1. Set L = ⌈ 12δ ⌉, using inequality (7), we have

$$
\left| \exp \left( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right) - \sum _ { l = 0 } ^ { \mathcal { L } } ( - 1 ) ^ { l } \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle ^ { l } } { l ! ( \sigma _ { t } ) ^ { 2 l } } \right| \lesssim n ^ { - \frac { 1 } { 2 } - \delta } .
$$

Therefore,

$$
\begin{array}{c} \begin{array} { l } { \varepsilon . 4 \cdot \| y - Y _ { j } \| \leq \sqrt { 2 } \varepsilon ) \left( y \right) \exp \left( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) } \\ { \varepsilon . 4 \cdot \| y - Y _ { j } \| \leq \sqrt { 2 } \varepsilon ) } \\ { \varepsilon . 4 \cdot \| y - Y _ { j } \| \leq \sqrt { 2 } \varepsilon ) } \end{array} \rho _ { j } ( y ) \exp \left( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } ( - 1 ) ^ { l } \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle } { l ! ( \sigma _ { t } ) ^ { 2 l } } \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f _ { l } ^ { 2 }  \\ { n ^ { - \delta - \frac { 1 } { 2 } } \epsilon ^ { - d } \sqrt { \log n } . } \end{array}
$$

Notice that we can write

$$
\begin{array} { l }  \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } ( \frac { 1 } { \sigma _ { t } } ) ^ { 2 l + 1 } \sum _ { 0 \leq k \leq 2 l + 1 } ^ { \rho _ { j } ( y ) \exp \big ( - \frac { \| m _ { t } Y _ { j } - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } ( - 1 ) ^ { l } \frac { \langle x - m _ { t } Y _ { j } , m _ { t } Y _ { j } - m _ { t } y \rangle ^ { l } } { l ! ( \sigma _ { t } ) ^ { 2 l } } \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) \cdot f } \\ { \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } ( \frac { 1 } { \sigma _ { t } } ) ^ { 2 l + 1 } \sum _ { 0 \leq k \leq 2 l + 1 } m _ { t } ^ { k } \sum _ { i \in \mathbb { N } _ { 0 } ^ { D } , \ | i | \leq l + 1 } a _ { l k i } \cdot x ^ { ( i ) } , } \end{array}
$$

where $\begin{array} { r } { x ^ { ( i ) } = \prod _ { s = 1 } ^ { D } x _ { s } ^ { i _ { s } } } \end{array}$ and $a _ { l k i } \in \mathbb { R } ^ { D }$ . Therefore, using Lemmas C.4, C.5, C.6 and C.7, we

1. Approximate $m _ { t }$ by ${ \phi } _ { m } ( t ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \bigl ( \frac { 1 } { \delta ^ { 3 } } \log ^ { 3 } n \bigr ) } \end{array}$ , R = Θ( 1δ4 log4 n) and $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ .

2. Approximate $\sigma _ { t }$ by $\phi _ { \sigma } ( t ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \bigl ( \frac { 1 } { \delta ^ { 3 } } \log ^ { 3 } n \bigr ) } \end{array}$ , R = Θ( 1δ4 log4 n) and $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ .

3. Approximate $\textstyle { \frac { 1 } { x } }$ by $\phi _ { r e c } ( x ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \bigl ( \frac { 1 } { \delta ^ { 3 } } \log ^ { 3 } n \bigr ) } \end{array}$ , $\begin{array} { r } { R = \Theta \big ( \frac { 1 } { \delta ^ { 4 } } \log ^ { 4 } n \big ) } \end{array}$ and $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ .

4. For vector $\boldsymbol { x } \in \mathbb { R } ^ { D }$ , approximate $\boldsymbol { x } ^ { ( i ) }$ by $\phi _ { v p o w e r } ^ { [ D ] } ( x ; i ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta \big ( \frac { 1 } { \delta } \log n \log \big ( \frac { 1 } { \delta } \big ) \big ) } \end{array}$ , $\| W \| _ { \infty } =$ $\Theta \big ( \textstyle { \frac { 1 } { \delta } } \big )$ , $\begin{array} { r } { R = \Theta \big ( \frac { 1 } { \delta ^ { 2 } } \log n \big ) } \end{array}$ and $B = \exp ( \Theta ( \frac 1 \delta \log \log n ) )$ ).

5. For $x \in \mathbb { R }$ , approximate $x ^ { a }$ by $\phi _ { p o w e r } ( x ; a ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta ( \frac { 1 } { \delta } \log n \log ( \frac { 1 } { \delta } ) ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta ( \frac { 1 } { \delta } ) } \end{array}$ , $\begin{array} { r } { R = \Theta \big ( \frac { 1 } { \delta ^ { 2 } } \log n \big ) } \end{array}$ and $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta } \log n ) ) } \end{array}$ .

6. For $x , y \in \mathbb { R }$ , approximate $x \cdot y$ by $\phi _ { m u l t } ( x , y ) \in \Phi ( L , W , R , B )$ with ${ \cal L } = \Theta ( { \textstyle \frac { 1 } { \delta } } \log n )$ , $\| W \| _ { \infty } = \Theta ( 1 )$ , $\begin{array} { r } { R = \Theta \big ( \frac { 1 } { \delta } \log n \big ) } \end{array}$ and $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta } \log n ) ) } \end{array}$ .

We have for any $x \in \mathcal { S } _ { y ^ { \ast } }$ and $t \in [ \underline { { t } } , t ]$ ,

$$
\begin{array} { l } { { \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } ( \frac { 1 } { \sigma _ { t } } ) ^ { 2 l + 1 } \sum _ { 0 \le k \le 2 l + 1 } m _ { t } ^ { k } \sum _ { i \in N _ { 0 } ^ { D } , | i | \le l + 1 } a _ { l k i } x ^ { ( i ) } } \ ~ } \\ { { - \displaystyle \sum _ { l = 0 } ^ { \mathcal { L } } \sum _ { 0 \le k \le 2 l + 1 } \sum _ { i \in N _ { 0 } ^ { D } , | i | \le l + 1 } a _ { l k i } \cdot \phi _ { m u l t } \left( \phi _ { m u l t } \Big ( \phi _ { p o w e r } \big ( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) ; 2 l + 1 \big ) , \phi _ { p o w e r } \big ( \phi _ { m } ( t ) ; k \big ) \Big ) , \phi _ { i l } \right) } \ ~ } \\ { { \le n ^ { - \delta - \frac { 1 } { 2 } } \epsilon ^ { - d } . } } \end{array}
$$

Therefore, based on Lemmas F.1-F.3 in Oko et al. (2023) for the concatenation and parallelization of neural networks, there exists networks $\phi _ { j } ^ { [ 1 ] } ( x , t ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \big ( \frac { 1 } { \delta ^ { 3 } } ( \log ^ { 3 } { n \vee \big ( \begin{array} { c } { \mathcal { L } + D } \\ { D } \end{array} \big ) } ) \big ) } \end{array}$ , $\begin{array} { r } { R = \Theta \big ( \frac { \log n } { \delta ^ { 4 } } \big ( \log ^ { 3 } n \vee \binom { \mathcal { L } + D } { D } \big ) \big ) } \end{array}$ $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ so that (8) holds. Si holds. For the term sts a neural network, using Lemma C.5, $\phi _ { j } ^ { [ 2 ] } ( x , t )$ $\phi _ { j } ^ { [ 1 ] } ( x , t )$ $\mathrm { e x p } ( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } )$ we construct neural network $\phi _ { \mathrm { e x p } } \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( \log n )$ , $R = \Theta ( \log ^ { 2 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ , so that

$$
- \frac { 1 } { 2 } \phi _ { m u l t } ( \phi _ { p o w e r } ( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) ; 2 ) , \sum _ { i = 1 } ^ { D } \phi _ { p o w e r } ( x _ { i } - m _ { t } Y _ { j , i } ; 2 ) ) ) - \exp ( - \frac { \| x - m _ { t } Y _ { j } \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \Bigg | \lesssim r \| _ { \phi ^ { \prime } } \| _ { L ^ { 2 } ( D ) }
$$

Therefore, there exists $\phi _ { j } ^ { [ 3 ] } ( x , t ) \in \Phi ( L , W , R , B )$ with $\begin{array} { r } { L = \Theta \big ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n \big ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \big ( \frac { 1 } { \delta ^ { 3 } } \log ^ { 3 } n \big ) } \end{array}$ , $\begin{array} { r } { R = \Theta \big ( \frac { 1 } { \delta ^ { 4 } } \log ^ { 4 } n \big ) } \end{array}$ , $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ so that (10) holds. Then using (11) and Lemmas C.1, C.6, C.7, we can obtain

$$
\begin{array} { l l } { \displaystyle \frac { - c _ { 2 } \sqrt { \log n } } { \sigma _ { \perp } } , \operatorname* { m i n } \{ \frac { c _ { 2 } \sqrt { \log n } } { \sigma _ { \perp } } , \phi _ { m u l t } \bigg ( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) , \phi _ { m u l t } \bigg ( \displaystyle \sum _ { j = 1 } ^ { J } \phi _ { j } ^ { [ 1 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) , \phi _ { r e c } \big ( \displaystyle \sum _ { j = 1 } ^ { J } \phi _ { j } ^ { [ 2 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) \phi _ { j } ^ { [ 3 ] } ( x , t ) } \\ { \displaystyle - \nabla \log p _ { t } ( x ) \bigg \| _ { \infty } \lesssim \frac { \log ^ { 2 } n } { \sqrt { n } } . } \end{array}
$$

bt, $\phi ^ { \ast } ( x , t ) \in \Phi \big ( L , W , R , B , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \pm } } ) \big )$ with  so tha $\begin{array} { r } { L = \Theta \big ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n \big ) } \end{array}$ , $\begin{array} { r } { \| W \| _ { \infty } = \Theta \big ( \frac { J } { \delta ^ { 3 } } ( \log ^ { 3 } { n \vee \big ( \begin{array} { c } { \mathcal { L } + D } \\ { D } \end{array} \big ) } ) \big ) } \end{array}$ $\begin{array} { r } { R = \Theta \big ( \frac { J \log n } { \delta ^ { 4 } } \big ( \log ^ { 3 } n \vee \big ( \begin{array} { c } { \mathcal { L } + D } \\ { D } \end{array} \big ) \big ) \big ) } \end{array}$ $\begin{array} { r } { B = \exp ( \Theta ( \frac { 1 } { \delta ^ { 2 } } \log ^ { 2 } n ) ) } \end{array}$ $x \in \mathcal { S } _ { y ^ { * } }$ and $t \in [ \underline { { t } } , t ]$ ,

$$
\| \phi ^ { * } ( x , t ) - \nabla \log p _ { t } ( x ) \| _ { \infty } \lesssim \frac { \log ^ { 2 } n } { \sqrt { n } } .
$$

The desired result then follows from Lemmas C.1, C.3 and the fact that $| N _ { \epsilon ^ { * } } | \cdot | \tilde { N } _ { \epsilon } | = \mathcal { O } \big ( n ^ { 2 \delta d } ( \log n ) ^ { 2 d } \big )$

C.2 Case 2: $n ^ { - \frac { \cdot 2 } { 2 \alpha + d } } \leq \underline { { t } } \leq n ^ { - 2 \delta } ( \log n ) ^ { - 3 }$

Let $N _ { \epsilon ^ { * } }$ be an $\epsilon ^ { * }$ -cover of $\mathcal { M }$ with $\epsilon ^ { * } = \sigma _ { \underline { { t } } } \sqrt { \log n }$ so that statements in Lemma C.2 are satisfied. Then $| N _ { \epsilon ^ { * } } | =$ $\mathcal { O } \big ( ( \epsilon ^ { * } ) ^ { - d } \big )$ . Fix an arbitrary $y ^ { * } \in N _ { \epsilon ^ { * } }$ and consider

$$
\begin{array} { r } { x \in \mathcal S _ { y ^ { * } } ^ { \dagger } = \{ x \in \mathbb R ^ { D } : \| x - y ^ { * } \| \leq \sqrt { 2 } ( \epsilon ^ { * } + c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } ) , \ \mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} . } \end{array}
$$

Let $c _ { 1 } = \sqrt { 2 } ( 1 + c _ { 0 } )$ and $c _ { 1 } ^ { \prime } = c _ { 0 } + c _ { 1 }$ , we have

$$
\| y ^ { * } - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| \leq \| y ^ { * } - x \| + \| x - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| \leq ( c _ { 0 } + c _ { 1 } ) \sigma _ { t } \sqrt { \log n } = c _ { 1 } ^ { \prime } \sigma _ { t } \sqrt { \log n } ,
$$

where $\mathrm { P r o j } _ { \mathcal { M } } ( x )$ denotes the projection of $x$ to $\mathcal { M }$ , and it is uniquely defined because $\mathcal { M }$ has a positive reach and $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } \lesssim n ^ { - \delta } ( \log n ) ^ { - 2 } = o ( 1 )$ .

Then since $\mathcal { M }$ is $\beta$ -smooth, ther exists a positive constant $r$ so that

1. The projection function $\mathrm { P r o j } _ { T _ { y ^ { * } } \mathcal { M } } ( x - y ^ { * } )$ is a local diffeomorphism in $y ^ { * }$ , with the inverse $\Psi _ { y ^ { * } }$ defined on $\mathbb { B } _ { r } ( \mathbf { 0 } _ { D } ) \cap T _ { y ^ { * } } { \mathcal { M } }$ and is $\beta$ -smooth.

Let $V ^ { * }$ be an arbitrary orthornormal basis for the tangent space $T _ { y ^ { * } } { \mathcal { M } }$ at $y ^ { * }$ . Define a function $G ^ { * }$ with domain $\mathbb { B } _ { r } ( 0 _ { d } )$ so that

$$
G ^ { * } ( z ) = \Psi _ { y ^ { * } } ( V ^ { * } z )
$$

Then we can define the inverse function

$$
Q ^ { * } ( y ) = { G ^ { * } } ^ { - 1 } ( y ) = { V ^ { * } } ^ { T } \mathrm { P r o j } _ { T _ { y ^ { * } } \mathcal { M } } ( y - y ^ { * } ) = { V ^ { * } } ^ { T } ( y - y ^ { * } ) .
$$

Recall that $\| y ^ { * } - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| \leq c _ { 1 } ^ { \prime } \sigma _ { \underline { { t } } } \sqrt { \log n }$ and $\| x - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ , we have

$$
\begin{array} { r l } & { \left\{ y \in { \mathcal { M } } : \| y - x \| \leq c _ { 2 } \sigma _ { \underline { { t } } } \sqrt { \log { n } } \right\} \subset \left\{ y \in { \mathcal { M } } : \| y - \mathrm { P r o j } _ { { \mathcal { M } } } ( x ) \| \leq ( c _ { 2 } + c _ { 0 } ) \sigma _ { \underline { { t } } } \sqrt { \log { n } } \right\} } \\ & { \qquad \subset \left\{ y \in { \mathcal { M } } : \| y - y ^ { * } \| \leq ( c _ { 2 } + c _ { 0 } + c _ { 1 } ^ { \prime } ) \sigma _ { \underline { { t } } } \sqrt { \log { n } } \right\} } \\ & { \qquad \subset \left\{ y = G ^ { * } ( z ) : \| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log { n } } \right\} } \end{array}
$$

where the last statement uses $G ^ { * } ( 0 _ { d } ) = y ^ { * }$ and the Lipschitz continuity of $Q ^ { * }$ . Therefore, using equation (4), we only need to approximate

$$
\begin{array} { r l } & { \frac { 1 } { \sigma _ { t } } \cdot \frac { \int _ { \{ y = G ^ { * } ( z ) : \| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} } \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } y } { \sigma _ { t } } \right) f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathscr { M } } ( y ) } { \int _ { \{ y = G ^ { * } ( z ) : \| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} } \exp \left( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathscr { M } } ( y ) } } \\ & { = \frac { 1 } { \sigma _ { t } } \cdot \frac { \int _ { \| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } } \exp \left( - \frac { \| x - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \right) v ^ { * } ( z ) \mathrm { d } z } { \int _ { \| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } } \exp \left( - \frac { \| x - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) v ^ { * } ( z ) \mathrm { d } z } , } \end{array}
$$

where $v ^ { * } ( z ) = f ( G ^ { * } ( z ) ) \sqrt { \operatorname* { d e t } \left( \nabla G ^ { * } ( z ) ^ { T } \nabla G ^ { * } ( z ) \right) }$ . Then consider the Taylor expansion of $G ^ { * }$ at $0 _ { d }$ ,

$$
G ^ { * } ( z ) = y ^ { * } + \sum _ { i = 1 } ^ { \lfloor \beta \rfloor } T _ { i } ^ { * } ( z ^ { \otimes i } ) + O ( \| z \| ^ { \beta } ) ,
$$

we denote

$$
G ( z ) = y ^ { \ast } + \sum _ { i = 1 } ^ { \lfloor \beta \rfloor } T _ { i } ^ { \ast } ( z ^ { \otimes i } )
$$

as the polynomial approximation to $G ^ { * }$ . We have

$$
\begin{array} { r l } & { \underset { \| \boldsymbol { z } \| \leq c _ { 3 } \sigma _ { \frac { t } { 2 } } \sqrt { \log n } } { \operatorname* { s u p } } \| G ^ { * } ( \boldsymbol { z } ) - G ( \boldsymbol { z } ) \| \lesssim ( \underline { { t } } \log n ) ^ { \frac { \beta } { 2 } } } \\ & { \underset { \| \boldsymbol { z } \| \leq c _ { 3 } \sigma _ { \frac { t } { 2 } } \sqrt { \log n } } { \operatorname* { s u p } } \| \nabla G ^ { * } ( \boldsymbol { z } ) - \nabla G ( \boldsymbol { z } ) \| \lesssim ( \underline { { t } } \log n ) ^ { \frac { \beta - 1 } { 2 } } , } \end{array}
$$

where $\nabla G ( z ) = ( \nabla G _ { 1 } ( z ) , \nabla G _ { 2 } ( z ) , \cdot \cdot \cdot , \nabla G _ { D } ( z ) ) ^ { T }$ is the Jacobian matrix of $G$ . Next, we present the following lemma, which provides an approximation to the projection function $\mathrm { P r o j } _ { \mathcal { M } } ( x )$ .

Lemma C.8. If $\tau \leq t \leq n ^ { - 2 \delta } ( \log n ) ^ { - 3 }$ , there exists a neural network $\phi _ { p } ( x ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } ~ = ~ \Theta ( \log ^ { 3 } n )$ , $R \ : = \ : \Theta ( \log ^ { 4 } n )$ and $B \ = \ \exp ( \Theta ( \log n ) )$ so that for any $x$ with $\| x - y ^ { * } \| ~ \leq ~ c _ { 1 } ( \sigma _ { \frac { t } { \cdot } } \lor$ $n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ and $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ ,

$$
\left\| \left. \nabla G ( \phi _ { p } ( x ) ) , x - G ( \phi _ { p } ( x ) ) \right. \right\| \lesssim \left( ( \sigma _ { \frac { t } { 2 } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \right) ^ { 2 \beta } .
$$

2. $\left\| \phi _ { p } ( x ) - Q ^ { * } ( { \mathrm { P r o j } } _ { \mathcal { M } } ( x ) ) \right\| \lesssim \left( ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) { \sqrt { \log n } } \right) ^ { \beta } .$

Lemma C.8 suggests that that $G ( \phi _ { p } ( x ) )$ is a good approximation for $\mathrm { P r o j } _ { \mathcal { M } } ( x )$ . Based on this, we consider the following decomposition

$$
| x - m _ { t } G ^ { * } ( z ) | | ^ { 2 } = \| x - G ( \phi _ { p } ( x ) ) \| ^ { 2 } + 2 \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle + \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| _ { 1 } .
$$

We can then substitute this expression into (15) to obtain

$$
\begin{array} { r l } { \underset { t } { = } - \frac { \int _ { \| z \| \leq c _ { 3 } \sigma _ { \xi } \sqrt { \log { n _ { \xi } } } } \exp \Big ( - \frac { \| x - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \Big ) \cdot \Big ( - \frac { x - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \Big ) v ^ { * } ( z ) \mathrm { d } z } { \int _ { \| z \| \leq c _ { 3 } \sigma _ { \xi } \sqrt { \log { n _ { \xi } } } } \exp \Big ( - \frac { \| z - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \Big ) \| ^ { 2 } } } \\  \underset { + } { = } \frac { \int _ { \| z \| \leq c _ { 3 } \sigma _ { \xi } \sqrt { \log { n _ { \xi } } } } \exp \Big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \Big ) \cdot \exp \Big ( - \frac { \{ \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \Big ) \cdot \Big ( - \frac { x - m _ { t } } { \sigma } } \\ { \sigma _ { t } \int _ { \| z \| \leq c _ { 3 } \sigma _ { \xi } \sqrt { \log { n _ { \xi } } } } \exp \Big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \Big ) \cdot \exp \Big ( - \frac { \{ x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \} { \sigma _ { t } ^ { 2 } } \Big ) } { \sigma _ { t } ^ { 2 } } } \\  \underset { + } { = } \frac  \int _  \| \end{array}
$$

For the term ( $B$ ), since $G$ is a polynomial function, using Lemma C.6, C.7 and C.4, we can obtain that there exists a neural network $\phi _ { B } ( x , t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| = \Theta ( \log ^ { 3 } n )$ , $R = \varTheta ( \log ^ { 4 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ so that

$$
\operatorname* { s u p } _ { x \in \mathcal { S } _ { y ^ { * } } ^ { \dagger } } \left\| \frac { x - G ( \phi _ { p } ( x ) ) } { \sigma _ { t } ^ { 2 } } - \phi _ { B } ( x , t ) \right\| _ { \infty } \leq \frac { 1 } { n } .
$$

Then for the term ( $A$ ), notice that for any $x \in \mathcal { S } _ { y ^ { \ast } } ^ { \dagger } = \{ x \in \mathbb { R } ^ { D } : \| x - y ^ { \ast } \| \leq \sqrt { 2 } ( \epsilon ^ { \ast } + c _ { 0 } \sigma _ { \pm } \sqrt { \log n } ) ,$ $\mathrm { l i s t } ( x , \mathcal { M } ) \leq$ $c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } \}$ and $\| z \| \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ ,

$$
\begin{array} { r l } & { \| \phi _ { p } ( x ) \| \leq \| \phi _ { p } ( x ) - Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \| + \| Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) - Q ^ { * } ( y ^ { * } ) \| \lesssim \sigma _ { \underline { { t } } } \sqrt { \log n } , } \\ & { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| } \\ & { \quad \leq \| G ( \phi _ { p } ( x ) ) - G ( z ) \| + \| G ( z ) - G ^ { * } ( z ) \| + \| ( 1 - m _ { t } ) G ^ { * } ( z ) \| } \\ & { \quad \lesssim \| \phi _ { p } ( x ) \| + \| z \| + ( \sigma _ { \underline { { t } } } \sqrt { \log n } ) ^ { \beta } + \underline { { t } } } \\ & { \quad \lesssim \sigma _ { \underline { { t } } } \sqrt { \log n } , } \\ & { \| x - G ( \phi _ { p } ( x ) ) \| \leq \| x - y ^ { * } \| + \| G ( 0 _ { d } ) - G ( \phi _ { p } ( x ) \| \lesssim \sigma _ { t } \sqrt { \log n } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \left| \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle \right| } \\ & { \leq \left| \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ( z ) \rangle \right| + \left| \langle x - G ( \phi _ { p } ( x ) ) , G ( z ) - G ^ { * } ( z ) \rangle \right| + \left| \langle x - G ( \phi _ { p } ( x ) ) , G ^ { * } ( z ) \rangle \right| } \\ & { \leq \left| \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ( z ) \rangle \right| + \mathcal { O } \left( ( \sigma _ { L } \sqrt { \log n } ) ^ { \beta + 1 } \right) + \mathcal { O } \left( ( \sigma _ { L } \sqrt { \log n } ) ^ { 3 } \right) } \\ & { \leq \left| \langle x - G ( \phi _ { p } ( x ) ) , \nabla G ( \phi _ { p } ( x ) ) ( \phi _ { p } ( x ) - z ) \rangle \right| + \mathcal { O } \left( ( \sigma _ { L } \sqrt { \log n } ) ^ { 3 } \right) } \\ & { < ( \sigma _ { * } , \sqrt { \log n } ) ^ { 3 } } \end{array}
$$

Therefore, denote

$$
\begin{array} { r l } & { \bar { \boldsymbol { \mathscr { \tau } } } _ { t } ( x ) = \displaystyle \int _ { \| \boldsymbol z \| \leq s \sigma _ { t } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \left. x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - n \right. } { \sigma _ { t } ^ { 2 } } \right) } \\ & { \quad \quad \cdot \left( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \right) v ^ { * } ( z ) \mathrm { d } z , } \end{array}
$$

and

$$
\int _ { \| z \| \leq c _ { 3 } \sigma _ { t } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \right)
$$

we can derive

$$
\left\| \frac { \overline { { d p } } _ { t } ( x ) } { \overline { { p } } _ { t } ( x ) } \right\| \lesssim \sqrt { \log n } ,
$$

and

$$
\begin{array} { r l } & { \geq \displaystyle \int _ { \| z - \phi _ { p } ( x ) \| \leq \sigma _ { \varepsilon } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { \sigma _ { t } ^ { 2 } } \right) } \\ & { \gtrsim \displaystyle \int _ { \| z - \phi _ { p } ( x ) \| \leq \sigma _ { \varepsilon } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - G ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) v ^ { * } ( z ) \mathrm { d } z } \\ & { \gtrsim ( \sigma _ { t } ) ^ { d } . } \end{array}
$$

Therefore, if there exist neural networks $\phi ^ { [ 1 ] } ( x , t )$ and $\phi ^ { [ 2 ] } ( x , t )$ so that for any $t \in [ \underline { { t } } , \overline { { t } } ]$ and $x \in \mathcal { S } _ { y ^ { \ast } } ^ { \dagger }$

$$
\| \overline { { d p } } _ { t } ( x ) - \phi ^ { [ 1 ] } ( x , t ) \| _ { \infty } \lesssim ( \sigma _ { \underline { { t } } } ) ^ { d + 1 } n ^ { - \frac { 1 } { 2 } } \log ^ { 2 } n ,
$$

$$
\| \overline { { p } } _ { t } ( x ) - \phi ^ { [ 2 ] } ( x , t ) \| _ { \infty } \lesssim ( \sigma _ { \underline { { t } } } ) ^ { d + 1 } n ^ { - \frac 1 2 } \log ^ { \frac 3 2 } n .
$$

Then we have

$$
\left. \frac { 1 } { \sigma _ { t } } \cdot \frac { \overline { { d p } } _ { t } ( x ) } { \overline { { p } } _ { t } ( x ) } - \frac { 1 } { \sigma _ { t } } \cdot \frac { \phi ^ { [ 1 ] } ( x , t ) } { \phi ^ { [ 2 ] } ( x , t ) } \right. _ { \infty } \lesssim \frac { ( \log n ) ^ { 2 } } { \sqrt { n } } .
$$

To construct $\phi ^ { [ 1 ] } ( x , t )$ , we approximate $\overline { { d p } } _ { t } ( x )$ by polynomials. Use (18) and (19), by choosing $\mathcal { L } _ { 1 } = \Theta ( \log n )$ and $\begin{array} { r } { \mathcal { L } _ { 2 } = \lceil \frac { \log ( n ^ { - \frac { 1 } { 2 } } ) } { \log ( \sigma _ { \pm } \log ^ { \frac { 3 } { 2 } } n ) } \rceil } \end{array}$ , we have

$$
\left| \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) - \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \right| \lesssim n ^ { - 2 } ,
$$

and

$$
\begin{array} { l l } { \displaystyle  \exp ( - \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z )  } { \sigma _ { t } ^ { 2 } } ) - \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } ( - 1 ) ^ { l _ { 2 } } \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( \phi _ { p } ( x ) )  } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } } \\ { \lesssim \sigma _ { t } \log ^ { \frac { 3 } { 2 } } n \cdot n ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

Therefore, we have

$$
\begin{array} { r l }   { \boldsymbol { x } \cdot \boldsymbol { x } ) - \int _ { \| z \| \leq c _ { 3 } \sigma _ { \mathsf { L } } \sqrt { \log n } } \sum _ { l = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \cdot \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } ( - 1 ) ^ { l _ { 2 } } \frac { \langle \boldsymbol { x } - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) \rangle } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } } \\ & { \quad \cdot ( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } ) \boldsymbol { v } ^ { * } ( z ) \operatorname { d } z \Big \| } \\ & { \mathrm { g } ^ { 2 } \boldsymbol { n } \cdot \sigma _ { \mathsf { L } } \cdot \boldsymbol { n } ^ { - \frac { 1 } { 2 } } \cdot \int _ { \| z \| \leq c _ { 3 } \sigma _ { \mathsf { L } } \sqrt { \log n } } \exp ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \nu ^ { * } ( z ) \operatorname { d } z + ( \sigma _ { \mathsf { L } } \sqrt { \log n } ) ^ { d } \sqrt { \log 2 } } \end{array}
$$

Then since

$$
\begin{array} { c } { { \displaystyle \tilde { \tau } ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } \geq \frac { 1 } { 2 } \| G ^ { * } ( \phi _ { p } ( x ) ) - G ^ { * } ( z ) \| ^ { 2 } - 2 \| G ( \phi _ { p } ( x ) ) - G ^ { * } ( \phi _ { p } ( x ) ) + G ^ { * } ( z ) - m _ { t } G ^ { * } } } \\ { { \displaystyle \geq \frac { 1 } { 2 } \| \phi _ { p } ( x ) - z \| ^ { 2 } - C ( t ^ { 2 } + ( \sigma _ { t } \sqrt { \log n } ) ^ { 2 \beta } ) , } } \end{array}
$$

notice that $\sigma _ { t } \asymp \sqrt { t \wedge 1 } \asymp \sqrt { \underline { { t } } \wedge 1 } \leq n ^ { - \delta } ( \log n ) ^ { - \frac { 3 } { 2 } }$ and $\beta \geq 2$ , we have

$$
\frac { t ^ { 2 } + ( \sigma _ { t } \sqrt { \log { n } } ) ^ { 2 \beta } } { \sigma _ { t } ^ { 2 } } = o ( 1 ) ,
$$

and

$$
\int _ { \| z \| \leq c _ { 3 } \sigma _ { t } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \nu ^ { * } ( z ) \mathrm { d } z \lesssim \int \exp \left( - \frac { \| z - \phi _ { p } ( x ) \| ^ { 2 } } { 4 \sigma _ { t } ^ { 2 } } \right) \mathrm { d } z \lesssim \alpha
$$

So based on (23), we can obtain

$$
\begin{array} { l } { \displaystyle { \boldsymbol { \cdot } \boldsymbol { x } ) - \int _ { \| z \| \leq c _ { 3 } \sigma _ { \mathrm { \pm } } \sqrt { \log n } } \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { \ast } ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \cdot \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } ( - 1 ) ^ { l _ { 2 } } \frac { \langle \boldsymbol { x } - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) \rangle } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } } } \\ { \displaystyle \quad \cdot ( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { \ast } ( z ) } { \sigma _ { t } } ) \boldsymbol { v } ^ { \ast } ( z ) \operatorname { d } z \| } \\  \displaystyle \mathrm { \mathrm { \mathrm { \} } } \mathrm { \mathrm { \Sigma } } ^ { 2 } n \cdot ( \sigma _ { \mathrm { \pm } } ) ^ { d + 1 } \cdot n ^ { - \frac { 1 } { 2 } } . } \end{array}
$$

Furthermore,

$$
\begin{array} { r l } &  \begin{array} { r l } & { \frac { \Delta x } { \xi _ { 1 } + 1 } - \sum _ { k \geq 0 } ^ { \infty } \frac { \Delta x } { \xi _ { 2 } + 1 } - \eta ^ { k } \frac { ( \frac { 1 } { 2 } \xi _ { 3 } ( x _ { 1 } + x _ { 2 } ) - \eta \xi _ { 3 } ) \xi _ { 1 } } { \mu ^ { k } } - \frac { \Delta x } { \xi _ { 2 } + 1 } - \frac { \Delta x } { \xi _ { 3 } + 1 } - \frac { \Delta x ^ { 2 } } { \xi _ { 2 } + 1 } \frac { \Delta x ^ { 2 } } { \mu ^ { k } } \frac { \Delta x ^ { 2 } + \eta ^ { k } } { \mu ^ { k } } \frac { \Delta x ^ { 3 } + \eta ^ { k } } { \mu ^ { k } } } \\ & { \qquad \cdot ( \frac { \Delta x ^ { 2 } + \eta ^ { 2 } - \Delta x } { \mu ^ { k } } - \alpha ^ { 2 } \frac { \Delta x ^ { 2 } } { \mu ^ { k } } ) ^ { k } - \frac { \Delta x ^ { 2 } } { \mu ^ { k } } \frac { \Delta x ^ { 3 } + \eta ^ { k } } { \mu ^ { k } } } \\ & { - \int _ { \mathrm { T r a n s s o } } \frac { \Delta x } { \eta ^ { k } } { \mu ^ { k } } - \frac { \Delta x ^ { 2 } } { \mu ^ { k } } \frac { ( \frac { 1 } { 2 } \xi _ { 3 } ( x _ { 1 } + x _ { 2 } ) - \eta \xi _ { 3 } ) \xi _ { 1 } } { \mu ^ { k } } \frac { \Delta x ^ { 2 } + \eta ^ { k } } { \mu ^ { k } } } \\ &  - \int _ { \mathrm { T r a n s o } } \frac { \Delta x } { \eta ^ { k } } \frac { ( \frac { 1 } { 2 } \xi _ { 3 } ( x _ { 1 } + x _ { 2 } ) - \eta ^ { k } ) \xi _ { 1 } } { \mu ^ { k } } \frac  ( \frac { 1 } { 2 } \xi _ { 3 } ( x _ { 1 } + x _ { 2 } ) - \eta \ \end{array} \end{array}
$$

where $a _ { l _ { 1 } , l _ { 2 } , k , i , s } \in \mathbb { R } ^ { D }$ are some constant coefficients and the last equation use the fact that $G = ( G _ { 1 } , G _ { 2 } , \cdot \cdot \cdot , G _ { D } )$ are polynomials up to order $\lfloor \beta \rfloor$ . Then notice that $\begin{array} { r } { \big ( \frac { 1 } { \sigma _ { t } } \big ) ^ { 2 l _ { 1 } + 2 l _ { 2 } + 1 } a _ { l _ { 1 } , l _ { 2 } , k , i , s } \lesssim \exp ( \mathcal { O } ( \log ^ { 2 } n ) ) } \end{array}$ , we

1. Approximate $m _ { t }$ by ${ \phi } _ { m } ( t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \mathrm { s } } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .   
2. Approximate $\sigma _ { t }$ by $\phi _ { \sigma } ( t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \mathrm { s } } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .   
3. Approximate $\textstyle { \frac { 1 } { x } }$ by $\phi _ { r e c } ( x ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \mathrm { s } } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .   
4. For vector $\boldsymbol { x } \in \mathbb { R } ^ { D }$ , approximate $\boldsymbol { x } ^ { ( i ) }$ by $\phi _ { v p o w e r } ^ { [ D ] } ( x ; i ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n \cdot \log \mathcal { L } _ { 2 } )$ , $\| W \| _ { \infty } =$ $\Theta ( \mathcal { L } _ { 2 } )$ , $R = \Theta ( \mathcal { L } _ { 2 } \log ^ { 2 } n )$ and $B = \exp ( \Theta ( \mathcal { L } _ { 2 } \cdot \log \log n ) )$ ).

5. For vector $z \in \mathbb { R } ^ { d }$ , approximate $z ^ { ( i ) }$ by $\phi _ { v p o w e r } ^ { [ d ] } ( z ; i ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n \cdot \log \log n )$ , $\| W \| _ { \infty } =$ $\Theta ( \log n )$ , $R = \Theta ( \log ^ { 3 } n )$ and $B = \exp ( \Theta ( \log n \cdot \log \log n )$ .

6. For $x \in \mathbb R$ , Approximate $x ^ { a }$ by $\phi _ { p o w e r } ( x ; a ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n \cdot \log \log n )$ , $\| W \| _ { \infty } = \Theta ( \log n )$ , $R = \Theta ( \log ^ { 3 } n )$ and $B = \exp ( \Theta ( \log n \cdot \log \log n )$ ).

7. For $x , y \in \mathbb { R }$ , Approximate $x \cdot y$ by $\phi _ { m u l t } ( x , y ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( 1 )$ , $R = \Theta ( \log ^ { 2 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ .

We have

$$
\begin{array} { r l } & { \displaystyle \sum _ { t _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } \displaystyle \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } \big ( \frac { 1 } { \sigma _ { t } } \big ) ^ { 2 l _ { 1 } + 2 l _ { 2 } + 1 } \sum _ { 0 \leq k \leq 2 l _ { 1 } + l _ { 2 } + 1 } { m _ { t } ^ { k } } \sum _ { \substack { s \in [ \mathbb { R } _ { 0 } ^ { d } , | s | \leq ( 2 l _ { 1 } + 2 l _ { 2 } + 1 ) ] ( \beta ] } } ^ { \sum } ( \phi _ { p } ( x ) ) ^ { ( s ) } \sum _ { i \in \mathbb { R } _ { 0 } ^ { D } , | i | \leq l _ { 2 } } a _ { l _ { 1 } , l _ { 2 } , k , s , i } \cdot x ^ { ( i } } \\ & { \cdot \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } \displaystyle \sum _ { \ r { l _ { 2 } = 0 } } ^ { \mathcal { L } } \sum _ { 0 \leq k \leq 2 l _ { 1 } + l _ { 2 } + 1 } \sum _ { \substack { s \in \mathbb { R } _ { 0 } ^ { d } , | s | \leq ( 2 l _ { 1 } + 2 l _ { 2 } + 1 ) [ \beta ] } } \sum _ { \substack { a l _ { 1 } , l _ { 2 } , k , i _ { 2 } , i _ { 1 } \leq l _ { 2 } } } } \\ & { \dot { \rho } _ { m u l t } \left( \phi _ { m u l t } \left( \phi _ { p o w e r } \left( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) \right) ; 2 l _ { 1 } + 2 l _ { 2 } + 1 \right) , \phi _ { p o w e r } ( \phi _ { m } ( t ) ; k ) \right) , \phi _ { m u l t } \left( \phi _ { v p o w e r } ^ { [ D ] } ( x ; i ) , \phi _ { v p o u } ^ { [ d ] } \right) } \\ & { \lesssim ( \sigma _ { t } ) ^ { d + 1 } n ^ { - \frac { 1 } { 2 } } \log ^ { 2 } n . } \end{array}
$$

Therefore, by concatenation and parallelization of neural networks, we can obtain that there exists a network $\phi ^ { [ 1 ] } ( x , t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \big ( \log ^ { 6 } n + \mathcal { L } _ { 2 } \log ^ { d + 3 } n { \binom { \mathcal { L } _ { 2 } + D } { D } } \big )$ , $R = \Theta \bigl ( \log ^ { 8 } n +$ $\mathcal { L } _ { 2 } \log ^ { d + 5 } n \big ( \begin{array} { c } { \mathcal { L } _ { 2 } + D } \\ { D } \end{array} \big ) \big )$ , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ so that (20) holds. Similarly, there exists a neural network $\phi _ { j } ^ { [ 2 ] } ( x , t )$ with the same size as $\phi _ { j } ^ { [ 1 ] } ( x , t )$ so that (21) holds. Then using (22), (17) and Lemmas C.1, C.6, C.7, we can obtain

$$
\begin{array} { r l } & { \kappa \{ \displaystyle \frac { - c _ { 2 } \sqrt { \log n } } { \sigma _ { \underline { { t } } } } , \operatorname* { m i n } \{ \displaystyle \frac { c _ { 2 } \sqrt { \log n } } { \sigma _ { \underline { { t } } } } , \phi _ { m u l t } ( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) , \phi _ { m u l t } ( \phi ^ { [ 1 ] } ( x , t ) , \phi _ { r e c } ( \phi ^ { [ 2 ] } ( x , t ) ) ) ) - \phi _ { B } ( t ) \} ( \phi _ { r e c } ( \phi _ { \sigma } ( t ) ) , \phi _ { m u l t } ( \phi ^ { [ 3 ] } ( x , t ) , \phi _ { r e c } ( \phi ^ { [ 2 ] } ( x , t ) ) ) ) } \\ & { \qquad - \nabla \log p _ { t } ( x ) \bigg \| _ { \infty } \lesssim \displaystyle \frac { \log ^ { 2 } n } { \sqrt { n } } . } \end{array}
$$

t, $\phi ^ { \ast } ( x , t ) \in \Phi \big ( L , W , R , B , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \pm } } ) \big )$ $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \big ( \log ^ { 6 } n + \mathcal { L } _ { 2 } \log ^ { d + 3 } n { \binom { \mathcal { L } _ { 2 } + D } { D } } \big )$ $R = \Theta \big ( \log ^ { \mathrm { s } } n + \mathcal { L } _ { 2 } \log ^ { d + 5 } n \big ( \ O _ { D } ^ { \mathcal { L } _ { 2 } + D } \big ) \big )$ $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ $\begin{array} { r } { \mathcal { L } _ { 2 } = \lceil \frac { \log ( n ^ { - \frac { 1 } { 2 } } ) } { \log ( \sigma _ { \pm } \log ^ { \frac { 3 } { 2 } } n ) } \rceil } \end{array}$ , so that for any $x \in \mathbb { R } ^ { D }$ with $\| x - y ^ { * } \| \leq c _ { 1 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ and $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } { \sqrt { \log n } }$ , and $t \in [ \underline { { t } } , t ]$ ,

$$
\| \phi ^ { * } ( x , t ) - \nabla \log p _ { t } ( x ) \| _ { \infty } \lesssim \frac { \log ^ { 2 } n } { \sqrt { n } } .
$$

The desired result then follows from Lemmas C.1, C.3 and the fact that $| N _ { \epsilon ^ { * } } | = \mathcal { O } \bigl ( \sigma _ { \underline { { t } } } ^ { - d } ( \log n ) ^ { - \frac { d } { 2 } } \bigr )$ .

# C.3 Case 3: $\tau \leq \underline { { t } } \leq n ^ { - \frac { 2 } { 2 \alpha + d } }$

Let $N _ { \epsilon ^ { * } }$ be an $\epsilon ^ { * }$ -cover of $\mathcal { M }$ with $\epsilon ^ { * } = n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n }$ so that statements in Lemma C.2 are satisfied. Then $| N _ { \epsilon ^ { * } } | = \mathcal { O } \bigl ( n ^ { \frac { d } { 2 \alpha + d } } ( \log n ) ^ { - \frac { d } { 2 } } \bigr )$ . Fix an arbitrary $y ^ { * } \in N _ { \epsilon ^ { * } }$ and consider $( G ^ { * } , Q ^ { * } )$ defined in (13) and (14). For any

$$
\begin{array} { r } { x \in \mathcal { S } _ { y ^ { * } } ^ { \sharp } = \big \{ x \in \mathbb { R } ^ { D } : \| x - y ^ { * } \| \leq \sqrt { 2 } \big ( \epsilon ^ { * } + c _ { 0 } \sigma _ { \sharp } \sqrt { \log n } \big ) , \ : \mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \sharp } \sqrt { \log n } \big \} , } \end{array}
$$

we have

$$
\begin{array} { r l } { \{ y \in { \mathcal { M } } : \| y - x \| \leq c _ { 2 } \sigma _ { \underline { { t } } } \sqrt { \log { n } } \} \subset \{ y \in { \mathcal { M } } : \| y - \mathrm { P r o j } _ { { \mathcal { M } } } ( x ) \| \leq ( c _ { 2 } + c _ { 0 } ) \sigma _ { \underline { { t } } } \sqrt { \log { n } } \} } \\ { \subset \{ y = G ^ { * } ( z ) : \| z - Q ^ { * } ( \mathrm { P r o j } _ { { \mathcal { M } } } ( x ) ) \| \leq ( c _ { 2 } + c _ { 0 } ) \sigma _ { \underline { { t } } } \sqrt { \log { n } } \} } \end{array}
$$

Using Lemma C.8 and $c n ^ { - { \frac { 2 \beta } { 2 \alpha + d } } } ( \log n ) ^ { \beta + 1 } = \tau \leq t \leq n ^ { - { \frac { 2 } { 2 \alpha + d } } }$ , we have

$$
\begin{array} { r l } & { \| z - \phi _ { p } ( x ) \| \leq \| z - Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \| + \| \phi _ { p } ( x ) - Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \| } \\ & { \qquad \leq \| z - Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \| + \mathcal { O } \left( n ^ { - \frac { \beta } { 2 \alpha + d } } ( \log n ) ^ { \frac { \beta } { 2 } } \right) , } \end{array}
$$

and thus

$$
\begin{array} { r l } & { \{ y = G ^ { * } ( z ) : \| z - Q ^ { * } ( \mathrm { P r o j } _ { { \cal M } } ( x ) ) \| \le ( c _ { 2 } + c _ { 0 } ) \sigma _ { \underline { { t } } } \sqrt { \log n } \} } \\ & { \subset \{ y = G ^ { * } ( z ) : \| z - \phi _ { p } ( x ) \| \le c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} } \\ & { \subset \{ y = G ^ { * } ( z ) : \| z - \phi _ { p } ( x ) \| _ { \infty } \le c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } \} . } \end{array}
$$

So based on equation (4), we only need to approximate

$$
\begin{array} { r l } &  t ^ { - } \frac { \int _ { \{ y = G ^ { * } ( z ) \} \backslash \left\{ | z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \mathrm { f } } \sqrt { \log n _ { \mathrm { p } } } \right\} \exp \left( - \frac { \| x - m _ { t } g \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } g } { \sigma _ { t } } \right) f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) } { \int _ { \{ y = G ^ { * } ( z ) \} \backslash \left\{ | z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \mathrm { f } } \sqrt { \log n _ { \mathrm { p } } } \right\} \exp \left( - \frac { \| x - m _ { t } g \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { \| x - m _ { t } g \| ^ { 2 } } { \sigma _ { t } ^ { 2 } } \right) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) } } } \\ & { = \frac { 1 } { \sigma _ { t } } \cdot \frac { \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \mathrm { f } } \sqrt { \log n } } \exp \left( - \frac { \| x - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \left( - \frac { x - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \right) v ^ { * } ( z ) \mathrm { d } z } { \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \mathrm { f } } \sqrt { \log n } } \exp \left( - \frac { \| x - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot v ^ { * } ( z ) \mathrm { d } z } } \\ &  \geq \frac  \int _  \| z  \end{array}
$$

where $v ^ { * } ( z ) = f ( G ^ { * } ( z ) ) \sqrt { \operatorname * { d e t } \left( \nabla G ^ { * } ( z ) ^ { T } \nabla G ^ { * } ( z ) \right) }$ . In a similar manner to Case 2, the term $( B )$ can be approximated by neural network $\phi _ { B } ( x , t ) \in \Phi ( L , W , R , B )$ with an error $\frac { 1 } { n }$ if $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 3 } n )$ , $R = \Theta ( \log ^ { 4 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ .

Notice that $v ^ { * }$ is $\alpha$ -smooth, we can write

$$
\begin{array} { l } { { \displaystyle v ^ { * } ( z ) = v ( z ) + \mathcal { O } ( \| z \| ^ { \alpha } ) } } \\ { { \displaystyle v ( z ) = v ^ { * } ( 0 _ { d } ) + \sum _ { \stackrel { l \in \mathbb { N } _ { 0 } ^ { d } } { 1 \leq | l | \leq | \alpha | } } v ^ { * ( l ) } ( 0 _ { d } ) \cdot z ^ { ( l ) } } , } \end{array}
$$

where $\begin{array} { r } { v ^ { * ( l ) } ( 0 _ { d } ) = \frac { \partial ^ { | l | } v ^ { * } } { \partial z _ { 1 } ^ { l _ { 1 } } \partial z _ { 2 } ^ { l _ { 2 } } \cdots \partial z _ { d } ^ { l _ { d } } } \Big | _ { z = 0 _ { d } } } \end{array}$ . We wil first build an appro imation to term ( $C$ ) by replacing $G ^ { * }$ and $v ^ { * }$ $G$ $\boldsymbol { v }$   
error, we will consider and bound the following terms using Lemma C.8 for any $x \in \mathcal { S } _ { y ^ { \ast } } ^ { \ddagger } = \{ x \in \mathbb { R } ^ { D } : \| x -$   
$y ^ { * } \| \leq \sqrt { 2 } ( \epsilon ^ { * } + c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } )$ , $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } { \sqrt { \log n } } \} \subset \{ x \in \mathbb { R } ^ { D } : \| x - y ^ { * } \| \leq c _ { 1 } n ^ { - { \frac { 1 } { 2 \alpha + d } } } { \sqrt { \log n } } $ , $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq$   
$c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n } \}$ , and any $z \in \mathbb { R } ^ { d }$ satisfying $\| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ :

$$
\begin{array} { r } { \| \phi _ { p } ( x ) \| \leq \| \phi _ { p } ( x ) - Q ^ { * } ( \mathrm { P r o j } _ { M } ( x ) ) \| + \| Q ^ { * } ( \mathrm { P r o j } _ { M } ( x ) ) - Q ^ { * } ( y ^ { * } ) \| \lesssim n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } ; } \end{array}
$$

$$
\| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| \leq \| G ( \phi _ { p } ( x ) ) - G ( z ) \| + ( 1 - m _ { t } ) \| G ( z ) \| \lesssim \sigma _ { \bot } \sqrt { \log n } ;
$$

$$
\begin{array} { r } { ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } - \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 } \Big | \lesssim \frac { \sigma _ { t } \sqrt { \log n } \big ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } \big ) ^ { \beta } } { \sigma _ { t } ^ { 2 } } \asymp \frac { \sqrt { \log n } \big ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } \big ) ^ { \beta } } { \sigma _ { t } } } \end{array}
$$

$$
\phi _ { p } ( x ) ) \| \leq \| x - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| + \| G ^ { * } ( Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) ) - G ^ { * } ( \phi _ { p } ( x ) ) \| + \| G ^ { * } ( \phi _ { p } ( x ) ) - G ( \phi _ { p } ( x ) ) \| \lesssim \| \phi _ { p } ( x ) \| _ { L ^ { 2 } ( \mathcal { M } ) } ^ { 2 } ,
$$

$$
\begin{array} { r l } & { \frac { 1 } { \sigma _ { t } ^ { 2 } } \cdot \big | \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle - \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \rangle \big | } \\ & { \lesssim \frac { \sigma _ { t } \sqrt { \log n } \big ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } \big ) ^ { \beta } } { \sigma _ { t } ^ { 2 } } \asymp \frac { \sqrt { \log n } \big ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } \big ) ^ { \beta } } { \sigma _ { t } } ; } \end{array}
$$

$$
\begin{array} { r l } & { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \rangle | } \\ & { \leq \Big | \langle x - G ( \phi _ { p } ( x ) ) , \nabla G ( \phi _ { p } ( x ) ) ( \phi _ { p } ( x ) - z ) \rangle \Big | + \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ( z ) - \nabla G ( \phi _ { p } ( x ) ) ( \phi _ { p } ( x ) ) \rangle } \\ & { \qquad + \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ( z ) - m _ { t } G ( z ) \rangle \Big | } \\ & { \lesssim ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } ) ^ { 2 \beta } \sigma _ { \pm } \sqrt { \log n } + \sigma _ { \pm } ^ { 3 } ( \log n ) ^ { \frac { 3 } { 2 } } + \sigma _ { \pm } ^ { 3 } \sqrt { \log n } } \\ & { \lesssim \sigma _ { \pm } ^ { 3 } ( \log n ) ^ { \frac { 3 } { 2 } } ; } \\ & { \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \Big \| \lesssim \bigg \| \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) } { \sigma _ { t } } \bigg \| + \bigg \| \frac { G ( \phi _ { p } ( x ) ) - G ( z ) } { \sigma _ { t } } } \\ & { \qquad \quad \lesssim \sqrt { \log n } . } \end{array}
$$

Combining all the pieces, we can obtain

$$
\begin{array} { r l r } & { } & { \displaystyle  \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \varepsilon } \sqrt { \log n } } \exp ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \cdot \exp ( - \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - \log ( \phi _ { p } ( x ) )  } { \sigma _ { t } ^ { 2 } } ) \cdot  } \\ & { } & {  \cdot ( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } ) v ^ { * } ( z ) \mathrm { d } z - \displaystyle \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \varepsilon } \sqrt { \log n } } \exp ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( \lambda - z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } )  } \\ & { } & {  \cdot \exp ( - \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( z )  } { \sigma _ { t } ^ { 2 } } ) \cdot ( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) } { \sigma _ { t } } ) v ( z ) \mathrm { d } z ) } \\ & { } &  \lesssim \displaystyle \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \varepsilon } \sqrt { \log n } } \exp ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \mathrm { d } z \cdot ( \frac  n ^  - \frac { \beta } { 2 \sigma _ { \varepsilon } } ( \log n ) ^  \frac { \beta } { 2 }  \end{array}
$$

Similarly, we have

$$
\begin{array} { r l r } { } & { } & { \displaystyle \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( \phi _ { p } ( x ) ) - m _ { t } G ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } \right) } \\ { } & { } & { \displaystyle \mathrm { e } _ { p } ( x ) \| _ { \infty } \le c _ { s } \sigma _ { \xi } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } \right)  \\ { } & { } & { \displaystyle \mathrm { e } _ { t } ^ { - \phi _ { p } ( x ) \| _ { \infty } \le c _ { s } \sigma _ { \xi } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \lambda ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta + 1 } { 2 } } } } { \sigma _ { t } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) \right) } \\ { } & { } &  \displaystyle \lesssim \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \le c _ { s } \sigma _ { \xi } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right)  \end{array}
$$

Denote

$$
\begin{array} { r l } & { = \displaystyle \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \le c _ { 3 } \sigma _ { \mathsf { t } } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \left. x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - \phi _ { p } ( x ) \right. } { \sigma _ { t } ^ { 2 } } \right) } \\ & { \quad \quad \quad \quad \cdot \left( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) } { \sigma _ { t } } \right) v ( z ) \mathrm { d } z , } \end{array}
$$

and

$$
\begin{array} { l } { \displaystyle \widetilde { d p } _ { t } ( x ) } \\ { = \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \le c _ { 3 } \sigma _ { t } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } \right) } \end{array}
$$

We will show that if there exist neural networks $\phi ^ { [ 1 ] } ( x , t )$ and $\phi ^ { [ 2 ] } ( x , t )$ so that for any $t \in [ \underline { { t } } , \overline { { t } } ]$ and $x \in \mathcal { S } _ { y ^ { \ast } } ^ { \ddag }$

$$
\begin{array} { r } { \| \widetilde { d p } _ { t } ( x ) - \phi ^ { [ 1 ] } ( x , t ) \| _ { \infty } \lesssim ( \sigma _ { \frac { t } { 2 } } ) ^ { d } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta } { 2 } + 1 } } } { \sigma _ { \frac { t } { 2 } } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha + 1 } { 2 } } \Big ) , } \end{array}
$$

$$
\| \widetilde { p } _ { t } ( x ) - \phi ^ { [ 2 ] } ( x , t ) \| _ { \infty } \lesssim ( \sigma _ { \underline { { t } } } ) ^ { d } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta + 1 } { 2 } } } } { \sigma _ { \underline { { t } } } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha } { 2 } } \Big ) .
$$

Then we have

$$
\begin{array} { r l } & { \frac { _ { \varepsilon \to \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \varepsilon } \sqrt { \log n } } \exp \big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \exp \Big ( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \Big ) \left( \frac { m _ { t } G ^ { * } ( z ) - G ( \phi _ { t } ) } { \sigma _ { t } } \right) } { \sigma _ { t } } } \\ & { \phantom { \frac { _ { ( - \phi _ { p } ( x ) ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \varepsilon } \sqrt { \log n } } \exp \big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \exp \big ( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \big ) \cdot } } } \\ & { - \frac { 1 } { \sigma _ { t } } \cdot \frac { \phi ^ { [ 1 ] } ( x , t ) } { \phi ^ { [ 2 ] } ( x , t ) \Big \| _ { \infty } } \lesssim \frac { \eta - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta } { 2 } + 1 } } { \sigma _ { t } ^ { 2 } } + \frac { \eta ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha + 1 } { 2 } } } { \sigma _ { L } } . } \end{array}
$$

To show (34), we first bound $\begin{array} { r } { \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \underline { { t } } } \sqrt { \log n } } \exp \Big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \Big ) \mathrm { d } z } \end{array}$ . Notice that

$$
\begin{array} { r l } & { | \phi _ { p } ( x ) - z | \leq \| G ^ { * } ( \phi _ { p } ( x ) ) - G ^ { * } ( z ) \| \leq \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| + ( 1 - m _ { t } ) \| G ^ { * } ( z ) \| + { \cal O } ( n ^ { - \frac { \beta } { 2 \alpha _ { + } } } \alpha ^ { \frac { \gamma } { 2 } } ) } \\ & { \qquad \leq \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| + o ( \sigma _ { t } ) , } \end{array}
$$

we have

$$
\int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { t } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \mathrm { d } z \lesssim \int \exp \left( - \frac { \| \phi _ { p } ( x ) - z \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \mathrm { d } z
$$

Therefore, combined with (30) and (31), we can get

$$
\begin{array} { r l r } & { } & { \displaystyle { \bigg \| \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \le c _ { 3 } \sigma _ { \mathsf { L } } \sqrt { \log n } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } \right) } } \\ & { } & { \displaystyle { \quad \cdot \left( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) } { \sigma _ { t } } \right) v ^ { * } ( z ) \mathrm { d } z - \phi ^ { [ 1 ] } ( x , t ) \bigg \| _ { \infty } \lesssim ( \sigma _ { \mathsf { L } } ) ^ { d } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta } { 2 } + 1 } } } { \sigma _ { t } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } } } \end{array}
$$

and

$$
\begin{array} { r l } & { \displaystyle \int _ { | | z - \phi _ { p } ( x ) | | _ { \infty } \leq c _ { 3 } \sigma _ { \tt f } \sqrt { \log n } } \exp ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } ) \cdot \exp ( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - n G ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } ) } \\ & { \quad \quad \quad \quad - \phi ^ { [ 2 ] } ( x , t ) \| _ { \infty } \lesssim ( \sigma _ { \tt f } ) ^ { d } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta + 1 } { 2 } } } } { \sigma _ { t } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha } { 2 } } \Big ) . } \end{array}
$$

Now use the fact that

∥ $\begin{array} { r } { \Im ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| \le \| G ^ { * } ( \phi _ { p } ( x ) ) - G ^ { * } ( z ) \| + ( 1 - m _ { t } ) \| G ^ { * } ( z ) \| + \| G ( \phi _ { p } ( x ) ) - G ^ { * } ( \phi _ { p } ( x ) ) \| \lesssim \| \phi _ { p } ( z ) \| . } \end{array}$ ϕp(x)−z∥+o(σt), we have

$$
\begin{array} { r l } & { \frac { \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \frac { \epsilon } { 4 } } \sqrt { \log { n } } } \exp \Big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { \epsilon } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { \epsilon } ^ { 2 } } \Big ) \exp \Big ( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { \epsilon } G ^ { * } ( z ) \rangle } { \sigma _ { \epsilon } ^ { 2 } } \Big ) \Bigg ( \frac { m _ { \epsilon } G ^ { * } ( z ) - G ^ { * } ( z ) } { \sigma _ { \epsilon } } \Big ) } { \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \frac { \epsilon } { 4 } } \sqrt { \log { n } } } \exp \Big ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { \epsilon } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { \epsilon } ^ { 2 } } \Big ) \cdot \exp \Big ( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { \epsilon } G ^ { * } ( z ) \rangle } { \sigma _ { \epsilon } ^ { 2 } } \Big ) } \Bigg ) \ , } \\ & { \quad \lesssim \sqrt { \log { n } } , } \end{array}
$$

and

$$
\begin{array} { r l } & { \stackrel { \textsf { e } } { \underbrace { \mid z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \tt L } \sqrt { \log n } } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } ( \phi _ { p } ( x ) ) \rangle } { \sigma _ { t } ^ { 2 } } \right) } \\ & { \cdot \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq \sigma _ { t } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) \| _ { \infty } ^ { 2 } } { \sigma _ { t } ^ { 2 } } \right) } \\ & { : \int _ { \| z - \phi _ { p } ( x ) \| _ { \infty } \leq \sigma _ { t } } \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \right) \mathrm { d } z . } \end{array}
$$

Moreover, when $\| z - \phi _ { p } ( x ) \| _ { \infty } \leq \sigma _ { \underline { { t } } }$ ,

$$
\begin{array} { r l } & { \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle \Big | } \\ & { \leq \Big | \langle x - G ( \phi _ { p } ( x ) ) , \nabla G ( \phi _ { p } ( x ) ) ( \phi _ { p } ( x ) - z ) \rangle \Big | + \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ^ { * } ( z ) - \nabla G ( \phi _ { p } ( x ) ) \Big | } \\ & { \qquad + \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ( z ) - G ^ { * } ( z ) \rangle \Big | + \Big | \langle x - G ( \phi _ { p } ( x ) ) , G ^ { * } ( z ) - m _ { t } G ^ { * } ( z ) \rangle \Big | } \\ & { \lesssim ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } ) ^ { 2 \beta } \sigma _ { \frac { t } { L } } + \sigma _ { \frac { L } { 2 } } ^ { 3 } \sqrt { \log n } + \sigma _ { \frac { t } { 2 } } \sqrt { \log n } ( n ^ { - \frac { 1 } { 2 \alpha + d } } \sqrt { \log n } ) ^ { \beta } + \sigma _ { \frac { 3 } { 2 } } ^ { 3 } \sqrt { \log n } } \\ & { < \ \alpha ^ { 2 } } \end{array}
$$

where we have used Lemma C.8 and $\underline { { t } } \geq \tau \geq c n ^ { - \frac { 2 \beta } { 2 \alpha + d } } ( \log n ) ^ { \beta + 1 }$ with a large enough constant $c$ . Therefore, we have

$$
\operatorname { e x p } _ { \substack { _ { 0 } \le c _ { 3 } \sigma _ { t } \sqrt { \log n } } } \exp \left( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \cdot \exp \left( - \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ^ { * } ( z ) \rangle } { \sigma _ { t } ^ { 2 } } \right)
$$

We can then show (34) by combining all pieces.

Then we construct $\phi ^ { [ 1 ] } ( x , t )$ by approximating $\tilde { d p } _ { t } ( x )$ with polynomials. Based on statements (28) and (29), by choosing $\mathcal { L } _ { 1 } = \Theta ( \log n )$ and $\mathcal { L } _ { 2 } = \Theta ( 1 )$ , we have

$$
\begin{array} { r l } & { \Big | \exp \bigg ( - \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \bigg ) - \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \Big | } \\ & { \quad \lesssim ( \log n ) ^ { - \frac { d } { 2 } } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta + 1 } { 2 } } } } { \sigma _ { \frac { t } { L } } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha } { 2 } } \Big ) , } \end{array}
$$

and

$$
\begin{array} { r l } {  { \exp ( - \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( z )  } { \sigma _ { t } ^ { 2 } } ) - \sum _ { l _ { 2 } = 0 } ^ { \infty } ( - 1 ) ^ { l _ { 2 } } \frac {  x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( z )  } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } } \quad } & { { } } \\ {  { \lesssim ( \log n ) ^ { - \frac { a } { 2 } } \Big ( \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta + 1 } { 2 } } } } { \sigma _ { t } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha } { 2 } } \Big ) . } } \end{array}
$$

Therefore,

$$
\begin{array} { r l r } { \displaystyle } & { \displaystyle \sum _ { l = \le c _ { 3 } \sigma _ { \mathsf { E } } \sqrt { \log n } } \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \cdot \displaystyle \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } ( - 1 ) ^ { l _ { 2 } } \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - m _ { t } G ( \phi _ { p } ( x ) ) \rangle } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } \cdot \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 2 } } } & \\ { \displaystyle } & { \cdot \left( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) } { \sigma _ { t } } \right) v ( z ) \mathrm { d } z - \widetilde { d p } _ { t } ( x ) \Big \| _ { \infty } \lesssim ( \sigma _ { \mathsf { E } } ) ^ { d } \cdot \Big ( \frac { n ^ { - \frac { 3 } { 2 \sigma _ { \mathsf { d } } } } ( \log n ) ^ { \frac { \beta } { 2 } + 1 } } { \sigma _ { t } } + n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha + 1 } { 2 } } } & \end{array}
$$

Moreover, since $G ( z ) = ( G _ { 1 } ( z ) , G _ { 2 } ( z ) , \cdot \cdot \cdot , G _ { D } ( z ) )$ and $v ( z )$ are polynomials with degree at most $\lfloor \beta \rfloor$ and $\lfloor \alpha \rfloor$ respectively, we can write

$$
\begin{array} { l } { { \displaystyle z - \phi _ { p } ( x ) \| _ { \infty } \leq c _ { 3 } \sigma _ { \pm } \sqrt { \log \Lambda } \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 1 } } \frac { \| G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) \| ^ { 2 l _ { 1 } } } { 2 ^ { l _ { 1 } } l _ { 1 } ! \sigma _ { t } ^ { 2 l _ { 1 } } } \cdot \displaystyle \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } ( - 1 ) ^ { l _ { 2 } } \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ( \phi _ { p } ( x ) ) \rangle } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } \cdot \displaystyle \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 1 } } ( - 1 ) ^ { l _ { 2 } } \frac { \langle x - G ( \phi _ { p } ( x ) ) , G ( \phi _ { p } ( x ) ) - G ( \phi _ { p } ( x ) ) \rangle } { l _ { 2 } ! \sigma _ { t } ^ { 2 l _ { 2 } } } } , }  \\ { { \displaystyle \quad \cdot \left( - \frac { G ( \phi _ { p } ( x ) ) - m _ { t } G ( z ) } { \sigma _ { t } } \right) v ( z ) \operatorname { d } z } } \\   \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } \sum _ { l _ { 2 } = 0 } ^ { \mathcal { L } _ { 2 } } \left( \frac { 1 } { \sigma _ { t } } \right) ^ { 2 l _ { 1 } + 2 l _ { 2 } + 1 } \sum _ { 0 \leq k \leq 2 l _ { 1 } + l _ { 2 } + 1 } ^ { \mathcal { L } _ { 1 } } m _ { t } ^ { k } \sum _ { s \in \mathbb { R } _ { 0 } ^ { d } , | s | \leq ( 4 l _ { 1 } + 3 l _ { 2 } + 2 ) [ \beta ] + d + [ \alpha ] } ( \phi _ { p } ( x ) ) ^ { ( s ) } \sum \end{array}
$$

where $a _ { l _ { 1 } , l _ { 2 } , k , i , s } \in \mathbb { R } ^ { D }$ are some constant coefficients. Then notice that $\begin{array} { r } { ( \frac { 1 } { \sigma } ) ^ { 2 l _ { 1 } + 2 l _ { 2 } + 1 } a _ { l _ { 1 } , l _ { 2 } , k , i , s } \lesssim \exp ( \mathcal { O } ( \log ^ { 2 } n ) ) } \end{array}$ , we

1. Approximate $m _ { t }$ by ${ \phi } _ { m } ( t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \mathrm { s } } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .

2. Approximate $\sigma _ { t }$ by $\phi _ { \sigma } ( t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \mathrm { s } } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .

3. Approximate $\textstyle { \frac { 1 } { x } }$ by $\phi _ { r e c } ( x ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 6 } n )$ , $R = \varTheta ( \log ^ { \ 8 } n )$ and $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ .

4. For vector $\boldsymbol { x } \in \mathbb { R } ^ { D }$ , approximate $\boldsymbol { x } ^ { ( i ) }$ by $\phi _ { v p o w e r } ^ { [ D ] } ( x ; i ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( 1 )$ $R = \Theta ( \log ^ { 2 } n )$ and $B = \exp ( \Theta ( \log \log n ) )$ .

5. For vector $z \in \mathbb { R } ^ { d }$ , approximate $z ^ { ( i ) }$ by $\phi _ { v p o w e r } ^ { [ d ] } ( z ; i ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n \cdot \log \log n )$ , $\| W \| _ { \infty } =$ $\Theta ( \log n )$ , $R = \Theta ( \log ^ { 3 } n )$ and $B = \exp ( \Theta ( \log n \cdot \log \log n )$ ).

6. For $x \in \mathbb R$ , Approximate $x ^ { a }$ by $\phi _ { p o w e r } ( x ; a ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n \log \log n )$ , $\| W \| _ { \infty } = \Theta ( \log n )$ , $R = \Theta ( \log ^ { 3 } n )$ and $B = \exp ( \Theta ( \log n \log \log n )$ .

7. For $x , y \in \mathbb { R }$ , Approximate $x \cdot y$ by $\phi _ { m u l t } ( x , y ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( 1 )$ , $R = \Theta ( \log ^ { 2 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ .

We have

$$
\begin{array} { r l } & { \displaystyle \sum _ { 1 } ^ { \mathcal { L } _ { 1 } } \displaystyle \sum _ { 1 = 0 } ^ { \mathcal { L } _ { 2 } } ( \frac { 1 } { \sigma _ { t } } ) ^ { 2 l _ { 1 } + 2 l _ { 2 } + 1 } \sum _ { 0 \leq k \leq 2 l _ { 1 } + l _ { 2 } + 1 } \sum _ { \substack { s \in \mathbb { N } _ { 0 } ^ { k } , | s | \leq ( 4 l _ { 1 } + 3 l _ { 2 } + 2 ) | \delta | + d + | \alpha | } } ( \phi _ { p } ( x ) ) ^ { ( s ) } \sum _ { \substack { i \in \mathbb { N } _ { 0 } ^ { n } , | s | \leq l _ { 2 } , k | } } a _ { i _ { 1 } , l _ { 2 } , k } } \\ & { \displaystyle \sum _ { l _ { 1 } = 0 } ^ { \mathcal { L } _ { 1 } } \sum _ { 2 = 0 } ^ { \mathcal { L } _ { 2 } } \sum _ { 0 \leq k \leq 2 l _ { 1 } + l _ { 2 } + 1 } \sum _ { s \in \mathbb { N } _ { 0 } ^ { k } , | s | \leq ( 4 l _ { 1 } + 3 l _ { 2 } + 2 ) | \delta | + d + | \alpha | } \sum _ { \substack { s \in \mathbb { N } _ { 0 } ^ { k } , | s | \leq l _ { 2 } , k | } } a _ { l _ { 1 } , l _ { 2 } , k , i _ { s } , s } } \\ & { \phi _ { m u l t } ( \phi _ { m u l t } ( \phi _ { p o w e r } ( \phi _ { r e } ( \phi _ { \sigma } ( \cdot ) ) ) ; 2 l _ { 1 } + 2 l _ { 2 } + 1 ) , \phi _ { p o w e r } ( \phi _ { m } ( t ) ; k ) ) , \phi _ { m u l t } ( \phi _ { v p o w e r } ^ { [ D ] } ( x ; i ) , \phi _ { v p o n } ^ { [ d ] } ) } \\ &  \lesssim ( \sigma _ { t } ) ^ { d } \cdot ( \frac { n ^ { - \frac { s } { 2 \alpha + d } ( \log n ) ^ { \frac { s } { 2 } } | 1 } + 1 }  \sigma  \end{array}
$$

Therefore, there exists network $\phi ^ { [ 1 ] } ( x , t ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \bigl ( \log ^ { 6 } n + \log ^ { d + 3 } n \bigr )$ , $R = \Theta \big ( \log ^ { 8 } n + \log ^ { d + 5 } n \big )$ , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ so that (32) holds. By employing same techniques, we can also obtain that there exists a neural network $\phi _ { j } ^ { [ 2 ] } ( x , t )$ with the same size as $\phi _ { j } ^ { [ 1 ] } ( x , t )$ so that (33) holds. Then use (34), similar as the analysis for Case 2, we can obtain that there exists $\phi ^ { \ast } ( x , t ) \in \Phi \big ( L , W , R , B , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \pm } } ) \big )$ with $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \big ( \log ^ { 6 } n + \log ^ { d + 3 } n \big )$ , $R = \Theta \big ( \log ^ { 8 } n + \log ^ { d + 5 } n \big )$ , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ , so that for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ with $\| x - y ^ { * } \| \leq c _ { 1 } n ^ { - { \frac { 1 } { 2 \alpha + d } } } { \sqrt { \log n } }$ and $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ , and $t \in [ \underline { { t } } , \overline { { t } } ]$ ,

$$
\| \phi ^ { * } ( x , t ) - \nabla \log p _ { t } ( x ) \| _ { \infty } \lesssim \frac { n ^ { - \frac { \beta } { 2 \alpha + d } ( \log n ) ^ { \frac { \beta } { 2 } + 1 } } } { \sigma _ { \frac { t } { L } } ^ { 2 } } + \frac { n ^ { - \frac { \alpha } { 2 \alpha + d } } ( \log n ) ^ { \frac { \alpha + 1 } { 2 } } } { \sigma _ { \frac { t } { L } } } .
$$

The desired result then follows from Lemmas C.1, C.3 and the fact that $| N _ { \epsilon ^ { * } } | = \mathcal { O } \bigl ( n ^ { \frac { d } { 2 \alpha + d } } ( \log n ) ^ { - \frac { d } { 2 } } \bigr )$ .

# D Proof of Technical Lemmas

# D.1 Proof of Lemma B.2

Consider processes

$$
\begin{array} { l l } { { Y _ { 0 } \sim p _ { T } } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \\ { { } } \end{array} \nonumber
$$

$$
\begin{array} { r l } & { Y _ { 0 } \sim p _ { T } } \\ & { \mathrm { d } \overline { { Y } } _ { t } = \beta _ { T - t } ( \overline { { Y } } _ { t } + 2 \widehat { S } ( \overline { { Y } } _ { t } , T - t ) ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( 0 \leq t \leq T - \tau ) } \\ & { \overline { { Y } } _ { T - \tau } = \overline { { Y } } _ { T - \tau } \cdot \mathbf { 1 } \left( \| \overline { { Y } } _ { T - \tau } \| _ { \infty } \leq L \right) . } \end{array}
$$

$$
\begin{array} { r l } & { \widehat { Y } _ { 0 } \sim \mathcal { N } ( 0 , I _ { D } ) } \\ & { { \mathrm { d } } \widehat { Y } _ { t } = \beta _ { T - t } ( \widehat { Y } _ { t } + 2 \widehat { S } ( \widehat { Y } _ { t } , T - t ) ) { \mathrm { d } } t + \sqrt { 2 \beta _ { T - t } } { \mathrm { d } } B _ { t } \quad ( 0 \leq t \leq T - \tau ) } \\ & { \widehat { Y } _ { T - \tau } = \widehat { Y } _ { T - \tau } \cdot \mathbf { 1 } \left( \| \widehat { Y } _ { T - \tau } \| _ { \infty } \leq L \right) . } \end{array}
$$

Denote $p _ { t }$ , $\overline { { p } } _ { t }$ and $\widehat { p } _ { t }$ ( $\tau \leq t \leq T$ ) as the probability distribution of $Y _ { T - t }$ , $\overline { { Y } } _ { T - t }$ and $\hat { Y } _ { T - t }$ respectively. Then we have

$$
\mathbb { E } [ d _ { \gamma } ( p _ { \mathrm { d a t a } } , \widehat { p } ) ] \leq \mathbb { E } [ d _ { \gamma } ( p _ { \mathrm { d a t a } } , p _ { \tau } ) ] + \mathbb { E } [ d _ { \gamma } ( p _ { \tau } , \overline { { p } } _ { \tau } ) ] + \mathbb { E } [ d _ { \gamma } ( \overline { { p } } _ { \tau } , \widehat { p } ) ] .
$$

Since $c ( x , y ) = \| x - y \| ^ { \gamma }$ is a distance cost function for $\gamma \leq 1$ , we have

$$
d _ { \gamma } ( \mu _ { 1 } , \mu _ { 2 } ) \asymp \operatorname* { m i n } _ { \pi \in \Pi ( \mu _ { 1 } , \mu _ { 2 } ) } \int \| x - y \| ^ { \gamma } \mathrm { d } \pi ,
$$

where $\Pi ( \mu _ { 1 } , \mu _ { 2 } )$ is the set of all couplings of $\mu _ { 1 }$ and $\mu _ { 2 }$ . Notice that $p _ { \mathrm { d a t a } }$ is supported on $\mathcal { M } \subset \mathbb { B } _ { L / 2 } ^ { D }$ , we can bound

$$
\begin{array} { r l } & { \mathbb { E } [ d _ { \gamma } ( p _ { \mathrm { d a t a } , } p _ { \tau } ) ] \lesssim \mathbb { E } _ { x \in p _ { \mathrm { d a t a } } , z \in \mathcal { N } ( 0 , I _ { D } ) } [ \| x - ( m _ { \tau } x + \sigma _ { \tau } z ) \cdot \mathbf { 1 } ( \| m _ { \tau } x + \sigma _ { \tau } z \| _ { \infty } \leq L ) \| ^ { \gamma } ] } \\ & { \qquad \leq \mathbb { E } _ { x \in p _ { \mathrm { d a t a } } , z \in \mathcal { N } ( 0 , I _ { D } ) } [ \| x - ( m _ { \tau } x + \sigma _ { \tau } z ) \| ^ { \gamma } ] } \\ & { \qquad \leq ( ( 1 - m _ { \tau } ) ^ { \gamma } + \sigma _ { \tau } ^ { \gamma } ) \cdot \mathbb { E } _ { x \in p _ { \mathrm { d a t a } } } [ \| x \| ^ { \gamma } ] } \\ & { \qquad \lesssim \tau ^ { \frac { \gamma } { 2 } } . } \end{array}
$$

Furthermore,

$$
\begin{array} { r l } & { d _ { \gamma } ( \overline { { p } } _ { \tau } , \widehat { p } ) \lesssim d _ { \mathrm { T V } } ( \overline { { p } } _ { \tau } , \widehat { p } ) \leq d _ { \mathrm { T V } } ( p _ { T } , \mathcal { N } ( 0 , I _ { D } ) ) } \\ & { \qquad \leq \sqrt { 2 \mathrm { K L } ( p _ { T } \| \mathcal { N } ( 0 , I _ { D } ) ) } } \\ & { \qquad \leq 2 \exp ( ( T - 1 ) \underline { { \beta } } ) \sqrt { \mathrm { K L } ( p _ { 1 } \| \mathcal { N } ( 0 , I _ { D } ) } , } \end{array}
$$

where the last inequality is due to the exponential convergence of the Ornstein-Ulhenbeck process (Bakry et al., 2014). Moreover,

$$
\mathrm { p g } \left( \frac { p _ { 1 } } { ( 2 \pi ) ^ { - \frac { D } { 2 } } \exp ( - \| x \| ^ { 2 } / 2 ) } \right) = \log \left( \frac { 1 } { \sigma _ { 1 } ^ { D } } \cdot \int \exp ( - \frac { \| x - m _ { 1 } y \| ^ { 2 } - \| x \| ^ { 2 } } { 2 \sigma _ { 1 } ^ { 2 } } ) f ( y ) \mathrm { d } \mathrm { v o l } _ { \cal M } ( y ) \right) \lesssim \| x \| ^ { 2 } ,
$$

and

$$
\mathbb { E } _ { p _ { 1 } } [ \| x \| ] = \mathcal { O } ( 1 ) ,
$$

we have

$$
d _ { \gamma } ( \overline { { p } } _ { \tau } , \widehat { p } ) \lesssim 2 \exp ( ( T - 1 ) \underline { { \beta } } ) \sqrt { \mathrm { K L } ( p _ { 1 } \| \mathcal { N } ( 0 , I _ { D } ) } \lesssim \exp ( ( T - 1 ) \underline { { \beta } } ) \lesssim \frac { 1 } { n } .
$$

The analysis for the term $\mathbb { E } [ d _ { \gamma } ( p _ { \tau } , \overline { { p } } _ { \tau } ) ]$ follows from Lemma D.7 of Oko et al. (2023), the only difference is that we need to take $\gamma$ into consideration. We include the proof below for completeness.

For $0 \leq i \leq K$ , denote

$$
\begin{array} { r l } & { \overline { { Y } } _ { 0 } ^ { ( i ) } \sim p _ { T } } \\ & { \mathrm { d } \overline { { Y } } _ { t } ^ { ( i ) } = \beta _ { T - t } ( \overline { { Y } } _ { t } ^ { ( i ) } + 2 \log p _ { T - t } ( \overline { { Y } } _ { t } ^ { ( i ) } ) ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( 0 \leq t \leq T - t _ { i } ) } \\ & { \mathrm { d } \overline { { Y } } _ { t } ^ { ( i ) } = \beta _ { T - t } ( \overline { { Y } } _ { t } ^ { ( i ) } + 2 \widehat { S } ( \overline { { Y } } _ { t } ^ { ( i ) } , T - t ) ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( T - t _ { i } \leq t \leq T - \tau ) } \\ & { \overline { { Y } } _ { T - \tau } ^ { ( i ) } = \overline { { Y } } _ { T - \tau } ^ { ( i ) } \cdot \mathbf { 1 } \left( \| \overline { { Y } } _ { T - \tau } ^ { ( i ) } \| _ { \infty } \leq L \right) . } \end{array}
$$

Denote $\overline { { p } } _ { t } ^ { ( i ) }$ ( $\tau \leq t \leq T )$ as the probability distribution of $\overline { { Y } } _ { T - t } ^ { ( i ) }$ . We have

$$
\mathbb { E } [ d _ { \gamma } ( p _ { \tau } , \overline { { p } } _ { \tau } ) ] \leq \sum _ { i = 0 } ^ { K - 1 } \mathbb { E } [ d _ { \gamma } ( \overline { { p } } _ { \tau } ^ { ( i ) } , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } ) ] .
$$

Denote $\begin{array} { r } { \mathcal { A } = \{ ( x , t ) \in \mathbb { R } ^ { d } \times \mathbb { R } : \| x \| _ { \infty } \leq m _ { t } + C \sigma _ { t } \sqrt { \log n } , \tau \leq t \leq T \} } \end{array}$ . By Lemma A.1 of Oko et al. (2023), there exists a large enough constant $C$ so that it holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that for all $0 \leq t \leq T - \tau$ , $( Y _ { t } , T - t ) \in \mathcal { A }$ . Then consider

$$
\begin{array} { r l } & { \overline { { Y } } _ { 0 } ^ { ' ( i ) } \sim p _ { T } } \\ & { \mathrm { d } \overline { { Y } } _ { t } ^ { ' ( i ) } = \beta _ { T - t } ( \overline { { Y } } _ { t } ^ { ' ( i ) } + 2 \log p _ { T - t } ( \overline { { Y } } _ { t } ^ { ' ( i ) } ) ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( 0 \leq t \leq T - t _ { i + 1 } ) } \\ & { \mathrm { d } \overline { { Y } } _ { t } ^ { ' ( i ) } = \beta _ { T - t } \Big ( \overline { { Y } } _ { t } ^ { ' ( i ) } + 2 \log p _ { T - t } ( \overline { { Y } } _ { t } ^ { ' ( i ) } ) \mathbf { 1 } \big ( ( Y _ { t } ^ { ' ( i ) } , T - t ) \in \mathcal { A } , \mathrm { ~ f o r ~ a l l ~ } s \leq t \big ) } \\ & { \qquad + 2 \widehat { S } ( \overline { { Y } } _ { t } ^ { ' ( i ) } , T - t ) \mathbf { 1 } \big ( ( Y _ { t } ^ { ' ( i ) } , T - t ) \notin \mathcal { A } , \mathrm { ~ f o r ~ s o m e ~ } s \leq t \big ) \Big ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( T - t ) \mathrm { d } B _ { t } \quad ( T - t ) \mathrm { d } B _ { t } \quad ( T - t ) \mathrm { d } B _ { t } \quad ( T - t ) \mathrm { d } B _ { t } \quad ( T - t ) } \\ & { \mathrm { d } \overline { { Y } } _ { t } ^ { ' ( i ) } = \beta _ { T - t } ( \overline { { Y } } _ { t } ^ { ' ( i ) } + 2 \widehat { S } ( \overline { { Y } } _ { t } ^ { ' ( i ) } , T - t ) ) \mathrm { d } t + \sqrt { 2 \beta _ { T - t } } \mathrm { d } B _ { t } \quad ( T - t _ { i } \leq t \leq T - \tau ) } \\ &  \overline { { Y } } _ { T - \tau } ^ { ' ( i ) } = \overline { { Y } }  \end{array}
$$

Denote $\overline { { p } } _ { t } ^ { \prime ( i ) }$ $\tau \leq t \leq T )$ as the probability distribution of $\overline { { Y } } _ { \ : T - t } ^ { \prime \left( i \right) }$ , we have $\begin{array} { r } { d _ { \gamma } ( \overline { { p } } _ { \tau } ^ { \prime } ^ { ( i ) } , \overline { { p } } _ { \tau } ^ { ( i ) } ) \lesssim \frac { 1 } { n } } \end{array}$ . Furthermore, when $t _ { i } \gtrsim ( \log n ) ^ { - 1 }$ , we have $d _ { \gamma } ( \overline { { p } } _ { \tau } ^ { \prime } ( i ) , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } ) \lesssim d _ { \mathrm { T V } } ( \overline { { p } } _ { \tau } ^ { \prime } ( i ) , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } )$ . When $t _ { i } \lesssim ( \log n ) ^ { - 1 }$ , Oko et al. (2023) construct a transportation map between $\overline { { p } } _ { \tau } ^ { \prime } \left( i \right)$ and $\overline { { p } } _ { \tau } ^ { ( i + 1 ) }$ so that

1. As much as $\scriptstyle { \frac { 1 } { 2 } } d _ { \mathrm { T V } } ( { \overline { { p } } } _ { \tau } ^ { \prime } ^ { ( i ) } , { \overline { { p } } } _ { \tau } ^ { ( i + 1 ) } )$ of the mass is transported from $\overline { { p } } _ { \tau } ^ { \prime } \left( i \right)$ to $\overline { { p } } _ { \tau } ^ { ( i + 1 ) }$ .

2. With probability $\textstyle 1 - { \frac { 1 } { n } }$ , the transportation map moves at most $\mathcal { O } ( \sqrt { t _ { i } \log n } )$ .

Based on the above fact, we can then conclude

$$
d _ { \gamma } \left( \overline { { p } } _ { \tau } ^ { \ ( i ) } , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } \right) \lesssim \frac { 1 } { n } + \left( \sqrt { t _ { i } \log n } \wedge 1 \right) ^ { \gamma } \cdot d _ { \mathrm { T V } } ( \overline { { p } } _ { \tau } ^ { \prime \ ( i ) } , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } ) .
$$

Finally, follow the analysis in Chen et al. (2022), we can use invoke Girsanovs Theorem to shows that

$$
\begin{array} { r } { l _ { \mathrm { T V } } ( \overline { { p } } _ { \tau } ^ { \prime } ( ^ { i ) } , \overline { { p } } _ { \tau } ^ { ( i + 1 ) } ) \leq \sqrt { 2 \mathrm { K L } ( \overline { { p } } _ { \tau } ^ { \prime } ( ^ { i } ) \| \overline { { p } } _ { \tau } ^ { ( i + 1 ) } ) } \leq \sqrt { \displaystyle \int _ { t _ { i } } ^ { t _ { i + 1 } } \int _ { \mathbb R ^ { D } } \left\| \widehat { S } ( x , t ) - \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) } \mathrm { d } x \mathrm { d } t . } \end{array}
$$

The desired result is then follows from (35).

# D.2 Proof for Lemma C.1

Since $\mathcal { M } \subset \mathbb { B } _ { 1 } ( 0 _ { D } )$ , for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$

$$
\begin{array} { r l } & { \| \nabla \log p _ { t } ( x ) \| = \left\| \frac { \nabla p _ { t } ( x ) } { p _ { t } ( x ) } \right\| } \\ & { \qquad = \left\| \frac { \int \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \big ( - \frac { x - m _ { t } y } { \sigma _ { t } ^ { 2 } } \big ) \cdot f ( y ) \mathrm { d v o l } _ { M } ( y ) } { \int \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot f ( y ) \mathrm { d v o l } _ { M } ( y ) } \right\| } \\ & { \qquad \leq \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } . } \end{array}
$$

Therefore, for any constant $c _ { 1 } > 0$ ,

$$
\begin{array} { l l } & { ^ { \mathsf { \tiny \mathsf { \top } } } \| \nabla \log p _ { t } ( x ) \| ^ { 2 } p _ { t } ( x ) \cdot 1 \left( \mathrm { d i s t } ( x , M ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } \right) \mathrm { d } x } \\ & { : \displaystyle \int \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } \int \frac { f ( y ) } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) \cdot 1 \left( \mathrm { d i s t } ( x , M ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } , \| x \| \right) } \\ & { \cdot \displaystyle \int \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } \int \frac { f ( y ) } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( y ) \cdot 1 \left( \mathrm { d i s t } ( x , M ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } , \| x \| \right) } \end{array}
$$

Note that for large enough $c _ { 1 }$ ,

$$
\begin{array} { r l } & { \int \displaystyle \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } \int \frac { f ( y ) } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \operatorname { d v o l } _ { M } ( y ) \cdot 1 \Big ( \operatorname { d i s t } ( x , M ) \ge c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } , \| x \| \ge \frac { \| x - m _ { t } y \| ^ { 2 } } { \sigma _ { t } ^ { 2 } } \Big ) } \\ & { \le \displaystyle \int \left[ \int \displaystyle \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } \frac { 1 } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot 1 \Big ( \| x \| \ge c _ { 1 } \sqrt { \log n } \Big ) \mathrm { d } x \right] \cdot f ( y ) \mathrm { d v o l } _ { M } ( y ) } \\ & { \le \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Moreover, for large enough $c _ { 0 }$ , we have

$$
\begin{array} { r l } & { \displaystyle \int \frac { \| x \| + \sqrt { D } } { \sigma _ { t } ^ { 2 } } \int \frac { f ( y ) } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \mathrm { d v o l } _ { M } ( y ) \cdot 1 \Big ( \mathrm { d i s t } ( x , M ) \ge c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } , \| x \| \le \frac { \| x - m _ { t } y \| ^ { 2 } } { \sigma _ { t } ^ { 2 } } \Big ) } \\ & { \lesssim \frac { c _ { 1 } \sqrt { \log n } + D } { \sigma _ { t } ^ { 2 } } \frac { 1 } { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } } \cdot \exp \big ( - \frac { c _ { 0 } ^ { 2 } \sigma _ { t _ { i } } ^ { 2 } } { 4 \sigma _ { t } ^ { 2 } } \log n \big ) \displaystyle \int \int f ( y ) \cdot 1 \Big ( \| x \| \le c _ { 1 } \sqrt { \log n } \Big ) \mathrm { d v o l } _ { M } ( y ) \mathrm { d } x } \\ & { \le \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

Therefore, we have

$$
\int \left\| \nabla \log p _ { t } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \cdot 1 \left( { \mathrm { d i s t } } ( x , \mathcal { M } ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } \right) \mathrm { d } x \leq c _ { 1 } \frac { 1 } { n ^ { 2 } } .
$$

Similarly, we can show

$$
\begin{array} { r l } & { \displaystyle \int \| S ( x , t ) \| ^ { 2 } p _ { t } ( x ) \cdot 1 \left( \mathrm { d i s t } ( x , \mathcal { M } ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } \right) \mathrm { d } x } \\ & { \leq \displaystyle \int c ^ { 2 } \frac { \log n } { \sigma _ { t } ^ { 2 } } p _ { t } ( x ) \cdot 1 \left( \mathrm { d i s t } ( x , \mathcal { M } ) \geq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } \right) \mathrm { d } x \leq c ^ { 2 } c _ { 1 } \frac { 1 } { n ^ { 2 } } . } \end{array}
$$

The first statement is then proved. For the second statement. Denote $\mathrm { P r o j } _ { \mathcal { M } } ( x )$ as any point inside $\mathrm { a r g } \operatorname* { m i n } _ { y \in \mathcal { M } } \| x - y \|$ . Then for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ with $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n }$ ,

$$
\begin{array} { r l } & { ( 2 \pi \sigma _ { t } ^ { 2 } ) ^ { \frac { D } { 2 } } p _ { t } ( x ) \geq \displaystyle \int _ { y \in \mathbb { B } _ { \sigma _ { t } } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \cap \mathcal { M } } \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot f ( y ) \mathrm { d v o l } _ { \mathcal { M } } ( y ) } \\ & { \qquad \gtrsim \exp ( - \frac { \big ( C _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n } + \sigma _ { t } + ( 1 - m _ { t } ) \big ) ^ { 2 } } { 2 \sigma _ { t } } ) \sigma _ { t } ^ { d } } \\ & { \qquad \geq n ^ { - c _ { 2 } } . } \end{array}
$$

Therefore, there exists a constant $c _ { 0 } ^ { \prime }$ so that for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ with $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma _ { t _ { i } } \sqrt { \log n }$ ,

$$
\begin{array} { r l } & { \log p _ { t } ( x ) \| \leq \left\| \frac { \int \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \big ( - \frac { x - m _ { t } y } { \sigma _ { t } ^ { 2 } } \big ) \cdot \mathbf { 1 } \big ( \| x - m _ { t } y \| \leq c _ { 3 } \sigma _ { t } \sqrt { \log n } \big ) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } { \int \exp \big ( - \frac { \| x - m _ { t } y \| ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \big ) \cdot \mathbf { 1 } \big ( \| x - m _ { t } y \| \leq c _ { 3 } \sigma _ { t } \sqrt { \log n } \big ) \cdot f ( y ) \mathrm { d } \mathrm { v o l } _ { M } ( y ) } \right. } \\ & { \qquad \lesssim \frac { \sqrt { \log n } } { \sigma _ { t } } \asymp \frac { \sqrt { \log n } } { \sigma _ { t _ { i } } } . } \end{array}
$$

We can then get the desired statement by combining all pieces.

# D.3 Proof of Lemma C.2

The case for $\epsilon > 1$ is trivial. So we only consider the case of $\epsilon \leq 1$ . Since $\mathcal { M }$ is $\beta$ -smooth and has a reach that is bounded away from zero, there exists a constant $r$ so that for any $x \in \mathcal { M }$ , there exists a local homeomorphism $\psi _ { x }$ defined on $\mathbb { B } _ { r } ( 0 _ { d } )$ so that $\mathbb { B } _ { r } ( x ) \cap \mathcal { M } \subset \psi _ { x } ( \mathbb { B } _ { r } ( 0 _ { d } ) ) \subset \mathbb { B } _ { 8 r / 7 } ( x ) \cap \mathcal { M }$ and both $\psi _ { x }$ and $\psi _ { x } ^ { - 1 }$ are $\beta$ -smooth

maps. Therefore, we can write $\mathcal { M }$ as $\cup _ { i = 1 } ^ { M } \psi _ { i } ( \mathbb { B } _ { r } ( 0 _ { d } ) )$ , where $M$ is a positive constant and $\psi _ { i }$ is $\beta$ -smooth map with $\beta$ -smooth inverse. Without loss of generality, we assume $\psi _ { i } ^ { - 1 }$ to be 1-Lipschitz. Denote

$$
A = \{ z = \frac { ( j _ { 1 } , j _ { 2 } , \cdot \cdot \cdot , j _ { d } ) } { \lceil \frac { 1 } { \epsilon } \rceil } : j _ { i } \mathrm { ~ i s ~ i n t e g e r , } z \in \mathbb { B } _ { r } ( 0 _ { d } ) \} .
$$

Then

$$
\begin{array} { r } { \left| \cup _ { i = 1 } ^ { M } \psi _ { i } ( A ) \right| \lesssim \epsilon ^ { - d } . } \end{array}
$$

For any $y \in \mathcal M$ , there exists $i \in [ M ]$ and $z \in \mathbb { B } _ { r } ( 0 _ { d } )$ so that $y = \psi _ { i } ( z )$ . Moreover, there exists $z ^ { * } \in A$ so that $\| z - z ^ { * } \| \leq \epsilon$ . So,

$$
\| y - \psi _ { i } ( z ^ { * } ) \| \leq \| z - z ^ { * } \| \leq \epsilon ,
$$

which indicates that $\cup _ { i = 1 } ^ { M } \psi _ { i } ( A )$ is an $\epsilon$ -cover of $\mathcal { M }$ . Furthermore, for any $x _ { 0 } \in \mathcal { M }$ and $i \in [ M ]$ , if $\| x - x _ { 0 } \| \leq r$ and $\| y - x _ { 0 } \| \leq r$ , then

$$
\| \psi ^ { - 1 } ( x ) - \psi ^ { - 1 } ( y ) \| \leq \| x - y \| \leq 2 r .
$$

Therefore,

$$
| \{ x \in \psi _ { i } ( A ) : \| x - x _ { 0 } \| \leq 2 r \} | \lesssim ( r / \epsilon ) ^ { d } ,
$$

and thus

$$
| \{ x \in \mathcal { M } : \| x - x _ { 0 } \| \leq 2 r \} | \lesssim ( r / \epsilon ) ^ { d } ,
$$

# D.4 Proof of Lemma C.3

Consider $\boldsymbol { x } \in \mathbb { R } ^ { D }$ so that $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ . Then there exists $y \in N _ { \epsilon ^ { * } }$ so that

$$
\| x - y \| \leq \mathrm { d i s t } ( x , { \mathcal { M } } ) + \epsilon ^ { * } \leq c _ { 0 } \sigma _ { \underline { { t } } } { \sqrt { \log n } } + \epsilon ^ { * } .
$$

Write $N _ { \epsilon ^ { * } } = \{ Y _ { 1 } ^ { * } , Y _ { 2 } , \cdot \cdot \cdot , Y _ { J ^ { * } } ^ { * } \}$ and define

$$
\widetilde { \rho } ( x ) = \left\{ \begin{array} { c c } { 1 } & { | x | < 1 } \\ { 0 } & { | x | > 2 } \\ { 2 - | x | } & { 1 < | x | \le 2 } \end{array} \right.
$$

$$
\widetilde { \rho } _ { j } ( x ) = \widetilde { \rho } \left( \frac { \| x - Y _ { j } ^ { * } \| ^ { 2 } } { ( c _ { 0 } \sigma _ { \bot } \sqrt { \log n } + \epsilon ^ { * } ) ^ { 2 } } \right) , \quad \rho _ { j } ( x ) = \frac { \widetilde { \rho } _ { j } ( x ) } { \sum _ { j = 1 } ^ { J ^ { * } } \widetilde { \rho } _ { j } ( x ) } \mathrm { ~ f o r ~ } j \in [ J ^ { * } ] .
$$

Then we have

$$
\nabla \log p _ { t } ( x ) = \sum _ { j = 1 } ^ { J ^ { * } } \nabla \log p _ { t } ( x ) \cdot \rho _ { j } ( x ) .
$$

By Lemma C.6 and C.7, we construct the following neural networks:

1. For $j ~ \in ~ [ J ^ { * } ]$ , we approximate $\widetilde { \rho } _ { j } ( x )$ by $\phi _ { \widetilde { \rho } _ { j } } ( x ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log n )$ , $\| W \| _ { \infty } = \Theta ( \log n )$ , $R = \Theta ( \log n )$ and $B = \exp ( \Theta ( \log n ) )$ .

2. We approximate $\textstyle { \frac { 1 } { x } }$ by $\phi _ { r e c } ( x ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 3 } n )$ , $R = \Theta ( \log ^ { 4 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ .

3. We approximate $x \cdot y$ by $\phi _ { m u l t } ( x , y ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log n )$ , $\| W \| _ { \infty } = \Theta ( \log n )$ , $R = \Theta ( \log n )$ and $B = \exp ( \Theta ( \log n ) )$ .

We have for any $\boldsymbol { x } \in \mathbb { R } ^ { D }$ with $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ ,

$$
\begin{array} { r l } &  \begin{array} { r l } & { | \displaystyle \sum _ { j = 1 } ^ { N } \nabla \phi ( x ( x ) ^ { j } ) \cdot \boldsymbol { \phi } ( x ^ { j } ) - \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x ) ^ { j } \leq t , x , t , \phi ( x ) ) | _ { \infty } } \\ & { \leq \epsilon | \displaystyle \sum _ { j = 1 } ^ { N } \nabla \phi ( x , t , x ) \cdot \boldsymbol { \phi } ( x ) | _ { \infty } ^ { 2 } - \sum _ { j = 1 } ^ { N } \phi ( x , t , x , t , x ) \cdot \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x , t , x ) \cdot \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x , t , x ) ^ { j } ) ) | _ { \infty } } \\ & { + | \displaystyle \sum _ { j = 1 } ^ { N } \delta ( x , t , x ) \cdot \delta ( x ) \cdot \boldsymbol { \phi } ( x ) | _ { \infty } ^ { 2 } - \sum _ { j = 1 } ^ { N } \phi ( x , t , x , t , x ) \cdot \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x , t , x ) ^ { j } ) | _ { \infty } } \\ & { = \epsilon | \displaystyle \sum _ { j = 1 } ^ { N } \delta ( x , t , x ) \cdot \delta ( x ) \cdot \boldsymbol { \phi } ( x ) | _ { \infty } ^ { 2 } - \sum _ { j = 1 } ^ { N } \delta ( x , t , x , t , x ) \cdot \delta ( x ) \cdot \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x , t , x ) ^ { j } ) | _ { \infty } } \\ &  + | \displaystyle \sum _ { j = 1 } ^ { N } \delta ( x , t , x ) \cdot \delta _ { j } ( x , t , x ) \cdot \delta _ { \mathrm { t r a n ~ 1 } } ( \displaystyle \sum _ { j = 1 } ^ { N } \phi ( x , t  \end{array} \end{array}
$$

where the last inequality uses the fact that there are only constant-order number of $j \in \ [ J ]$ so that $\rho _ { j } ( x ) ~ \neq ~ 0$ . Finally, by concatenation and parallelization of neural networks, there exists $\phi _ { s c o r e } ( x ) \ \in$ $\begin{array} { r l } { \Phi ( L _ { 1 } , W _ { 1 } , S _ { 1 } , B _ { 1 } , \Theta ( \frac { \sqrt { \log n } } { \sigma _ { \frac { t } { } } } ) ) } & { { } } \end{array}$ with ${ \cal L } _ { 1 } \ = \ \Theta ( L + \log ^ { 2 } n )$ , $\| W _ { 1 } \| _ { \infty } ~ = ~ \Theta ( J ^ { * } ( \| W \| _ { \infty } + \log n ) + \log ^ { 3 } n )$ , $\begin{array} { r l } { S _ { 1 } } & { { } = } \end{array}$ $\Theta ( J ^ { * } ( S + \log n ) + \log ^ { 4 } n )$ and $B _ { 1 } = \exp ( \Theta ( \log ^ { 2 } n ) )$ so that

$$
\operatorname* { m a x } ( - c _ { 2 } \frac { \sqrt { \log n } } { \sigma _ { \underline { { t } } } } , \operatorname* { m i n } ( c _ { 2 } \frac { \sqrt { \log n } } { \sigma _ { \underline { { t } } } } , \phi _ { m u t i } ( \sum _ { j = 1 } ^ { J ^ { * } } \phi _ { m u t i } ( \phi _ { j } ^ { * } ( x , t ) , \phi _ { \widetilde { \rho } _ { j } } ( x ) ) , \phi _ { r e c } ( \sum _ { j = 1 } ^ { J ^ { * } } \phi _ { \widetilde { \rho } _ { j } } ( x ) ) ) )
$$

The result is then follows from the fact that $\begin{array} { r } { \| \nabla \log p _ { t } ( x ) \| _ { \infty } \leq c _ { 2 } \frac { \sqrt { \log n } } { \sigma _ { \frac { t } { \epsilon } } } } \end{array}$ when $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ .

# D.5 Proof of Lemma C.8

Let $h ( x , z ) = ( \nabla G ( z ) ) ^ { T } ( x - G ( z ) )$ . Then we can write the Jacobian of $h$ with respect to $z$ as

$$
\nabla _ { z } h ( x , z ) = - \nabla G ( z ) ^ { T } \nabla G ( z ) + \sum _ { k = 1 } ^ { D } ( x _ { k } - G _ { k } ( z ) ) \mathcal { H } _ { k } ( z ) ,
$$

where $G ( z ) = ( G _ { 1 } ( z ) , G _ { 2 } ( z ) , \cdot \cdot \cdot , G _ { D } ( z ) )$ and $\mathcal { H } _ { k } ( z )$ denotes the Hessian matrix of $G _ { k } ( z )$ . Then denote

$$
g ( x , z ) = z - ( \nabla _ { z } h ( x , z ) ) ^ { - 1 } h ( x , z ) .
$$

Note that for any $x$ with $\| x - G ( 0 _ { d } ) \| = \| x - y ^ { * } \| \leq c _ { 1 } ( \sigma _ { \underline { { t } } } \vee n ^ { - { \frac { 1 } { 2 \alpha + d } } } ) \sqrt { \log n } ,$ we have

$$
\begin{array} { r } { \| h ( x , 0 _ { d } ) \| = \| ( \nabla G ( 0 _ { d } ) ) ^ { T } ( x - G ( 0 _ { d } ) ) \| \le c _ { 1 } ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } . } \end{array}
$$

Then since $G ( z )$ is $C ^ { \infty }$ -smooth and $\nabla G ( 0 _ { d } ) ^ { T } \nabla G ( 0 _ { d } ) = I _ { d }$ , we have

$$
\| g ( x , 0 _ { d } ) \| = \mathcal { O } ( \| h ( x , 0 _ { d } ) \| ) = \mathcal { O } \left( ( \sigma _ { \frac { t } { 2 } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \right) ,
$$

and

$$
\begin{array} { r l } & { \| h ( x , g ( x , 0 _ { d } ) ) \| = \left\| h \left( x , 0 _ { d } - ( \nabla _ { z } h ( x , 0 _ { d } ) ) ^ { - 1 } h ( x , 0 _ { d } ) \right) \right\| } \\ & { \qquad = \left\| h ( x , 0 _ { d } ) - \nabla _ { z } h ( x , 0 _ { d } ) ( \nabla _ { z } h ( x , 0 _ { d } ) ) ^ { - 1 } h ( x , 0 _ { d } ) \right\| + { \cal O } ( \| h ( x , 0 _ { d } ) \| ^ { 2 } ) } \\ & { \qquad = { \cal O } \left( \left( ( \sigma _ { \perp } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \right) ^ { 2 } \right) . } \end{array}
$$

Similarly, define

$$
\overline { { g } } ( x ) = \underbrace { g \circ g \circ \cdots \circ g ( x , g ( x , 0 _ { d } ) ) } _ { \lceil \log _ { 2 } ( 2 \beta ) \rceil } ,
$$

we can obtain

$$
\| \overline { { { g } } } ( x ) \| = \mathcal { O } \left( ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \right) ,
$$

and

$$
\| h ( x , \overline { { g } } ( x ) ) \| = \mathcal { O } \left( \left( \left( \sigma _ { \frac { t } { - } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } \right) \sqrt { \log n } \right) ^ { 2 \beta } \right) ,
$$

Then we approximate $\overline { { g } } ( x )$ by the neural network. Notice that by Cayley-Hamilton theorem, for $A \in \mathbb { R } ^ { d \times d }$ , denote $S _ { k }$ as the trace of $A ^ { k }$ and $B _ { k }$ as the $k$ th complete exponential Bell polynomial.1 We can write

$$
\begin{array} { l } { \displaystyle \operatorname* { d e t } ( A ) = \frac { 1 } { d ! } B _ { d } ( S _ { 1 } , - 1 ! S _ { 2 } , \cdots , ( - 1 ) ^ { d - 1 } ( n - 1 ) ! S _ { d } ) } \\ { \displaystyle A ^ { - 1 } = \frac { 1 } { \operatorname* { d e t } ( A ) } \sum _ { k = 0 } ^ { d - 1 } ( - 1 ) ^ { d + k - 1 } \frac { A ^ { d - k - 1 } } { k ! } B _ { k } ( S _ { 1 } , - 1 ! S _ { 2 } , \cdots , ( - 1 ) ^ { k - 1 } ( k - 1 ) ! S _ { k } ) . } \end{array}
$$

Note that there exists a small enough constant $r$ so that for any $x$ with $\| x - G ( 0 _ { d } ) \| \leq c _ { 1 } ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ when $\| z \| \leq r$ ,

$$
- 2 I _ { d } \prec \nabla _ { z } h ( x , z ) \prec - \frac { 1 } { 2 } I _ { d } .
$$

By Lemmas C.6 and C.7, there exists $\phi _ { g } ( x , z ) \in \Phi ( L , W , R , B )$ with $L = \Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 3 } n )$ , $R = \Theta ( \log ^ { 4 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ so that for any $x$ with $\| x - G ( 0 _ { d } ) \| \leq c _ { 1 } ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ and $\| z \| \leq r$ ,

$$
\| \phi _ { g } ( x , z ) - g ( x , z ) \| \lesssim n ^ { - \frac { 2 \beta } { 2 \alpha + d } } .
$$

Furthermore,

$$
\begin{array} { r l } & { \left| \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - \infty , - \infty , \phi ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } - \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } \right| } \\ & { \leq \left| \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } - \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } \right| } \\ & { + \left| \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } - \frac { g _ { \phi } g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } \right| } \\ & { + \left| \frac { g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } - \frac { g _ { \phi } g _ { \phi } g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } \right| } \\ & { + \cdots } \\ & { + \left| \frac { g _ { \phi } g _ { \phi } g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } - \frac { g _ { \phi } g _ { \phi } g _ { \phi } \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } \right| } \\ & { \leq \epsilon \frac { \gamma \phi ^ { ( 0 , - 1 ) } ( x , g ) ( x , 0 ) ) } { | \log ( 2 \phi ) | } } \end{array}
$$

$$
\begin{array} { r l } & { \quad ^ { 1 } B _ { k } \left( x _ { 1 } , \ldots , x _ { k } \right) = \sum _ { w = 1 } ^ { k } B _ { k , w } \left( x _ { 1 } , x _ { 2 } , \ldots , x _ { k - w + 1 } \right) \mathrm { ~ w i t h ~ } B _ { k , w } \left( x _ { 1 } , x _ { 2 } , \ldots x _ { k - w + 1 } \right) } \\ & { = \sum _ { \scriptstyle j _ { 1 } + \ldots + j _ { k - w + 1 } = w \atop j _ { 1 } + 2 j _ { 2 } + \ldots + { ( k - w + 1 ) } j _ { k - w + 1 } = k } \frac { k ! } { j _ { 1 } ! j _ { 2 } ! \ldots j _ { k - w + 1 } ! } \left( \frac { x _ { 1 } } { 1 ! } \right) ^ { j _ { 1 } } \left( \frac { x _ { 2 } } { 2 ! } \right) ^ { j _ { 2 } } \cdots \left( \frac { x _ { k - w + 1 } } { k - w + 1 ! } \right) ^ { j _ { k - w + 1 } } } \end{array}
$$

So by concatenation and parallelization of neural networks, there exists $\phi _ { p } ( x ) \ \in \ \Phi ( L , W , R , B )$ with $L \ =$ $\Theta ( \log ^ { 2 } n )$ , $\| W \| _ { \infty } = \Theta ( \log ^ { 3 } n )$ , $R = \varTheta ( \log ^ { 4 } n )$ and $B = \exp ( \Theta ( \log ^ { 2 } n ) )$ so that for any $x$ with $\| x - y ^ { * } \| \leq$ $c _ { 1 } ( \sigma _ { \frac { t } { } } \lor n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ ,

$$
\| \phi _ { p } ( x ) - \overline { { { g } } } ( x ) \| \lesssim n ^ { - \frac { 2 \beta } { 2 \alpha + d } } .
$$

So we have $\| ( \nabla G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) \| = \| h ( x , \phi _ { p } ( x ) ) \| \lesssim \left( ( \sigma _ { \frac { t } { L } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \right) ^ { 2 \beta }$ . The proof of the first statement is completed. Then for the second statement, note that for any $x$ with $\| x - G ( 0 _ { d } ) \| = \| x - y ^ { * } \| \leq$ $c _ { 1 } ( \sigma _ { \frac { t } { } } \lor n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ , we have $\| \phi _ { p } ( x ) \| \lesssim ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ . Therefore,

$$
\begin{array} { r l } & { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ^ { * } ( \phi _ { p } ( x ) ) \| \le \| ( \nabla G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) \| } \\ &  \phantom { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) } \\ &  \phantom { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) - ( \nabla G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) } \\ & { \phantom { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { \beta } ) } } \\ &  \phantom { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) } \\ & { \phantom { ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { T } ( x - G ( \phi _ { p } ( x ) ) ^ { \beta } ) } . } \end{array}
$$

Then define $\ell ( x , z ) = \| x - G ^ { * } ( z ) \| ^ { 2 }$ , we have the Jacobian matrix of $\ell$ with respect to $z$ is

$$
\nabla \ell _ { z } ( x , z ) = - 2 \nabla G ^ { * } ( z ) ^ { T } ( x - G ^ { * } ( z ) ) ,
$$

and the Hessian matrix of $\ell$ with respect to $z$ is

$$
\mathcal { H } _ { z } ( \boldsymbol { x } , z ) = \nabla G ^ { * } ( z ) ^ { T } \nabla G ^ { * } ( z ) - 2 \sum _ { k = 1 } ^ { D } ( x _ { k } - G _ { k } ^ { * } ( z ) ) \mathcal { H } _ { k } ^ { * } ( z ) ,
$$

where $G ^ { * } ( z ) = ( G _ { 1 } ^ { * } ( z ) , G _ { 2 } ^ { * } ( z ) , \cdot \cdot \cdot , G _ { D } ^ { * } ( z ) )$ and $\mathcal { H } _ { k } ^ { * } ( z )$ denotes the Hessian matrix of $G _ { k } ^ { * } ( z )$ . For any $x$ with $\| x - G ^ { * } ( 0 _ { d } ) \| = \| x - y ^ { * } \| \leq c _ { 1 } ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ and $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ , denote

$$
\overline { { { z } } } = Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) .
$$

We have

$$
\| \overline { { z } } \| \leq \| y ^ { * } - \mathrm { P r o j } _ { \mathcal { M } } ( x ) \| \leq \| x - y ^ { * } \| + \mathrm { d i s t } ( x , \mathcal { M } ) \lesssim ( \sigma _ { \frac { L } { 2 } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } .
$$

Since $G ^ { * }$ is $\beta$ -smooth with $\beta \geq 2$ and $\nabla G ^ { * } ( 0 _ { d } ) ^ { T } \nabla G ^ { * } ( 0 _ { d } ) = I _ { d }$ , we have

$$
\begin{array} { r } { \| \mathcal { H } _ { z } ( x , z ) - \mathcal { H } _ { z } ( x , 0 _ { d } ) \| _ { \mathrm { F } } \lesssim \| z \| + ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } , } \end{array}
$$

and

$$
\| \mathcal { H } _ { z } ( x , 0 _ { d } ) - I _ { d } \| _ { \mathrm { F } } \lesssim ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } .
$$

Therefore, there exist positive constants $r _ { 1 } , a$ so that when $z \in \mathbb { B } _ { r _ { 1 } } ( \overline { { z } } )$ ,

$$
\begin{array} { r } { \mathcal { H } _ { z } ( x , z ) \succcurlyeq a I _ { d } . } \end{array}
$$

Then use Taylor’s theorem, for any $v \in \mathbb { R } ^ { d }$ with $\lVert \boldsymbol { v } \rVert = 1$ , $z \in \mathbb { B } _ { r _ { 1 } } ( \overline { { z } } )$ and $x$ with $\left\| x - G ^ { * } ( 0 _ { d } ) \right\| = \left\| x - y ^ { * } \right\| \leq$ $c _ { 1 } ( \sigma _ { \frac { t } { } } \lor n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n }$ and $\mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma _ { \underline { { t } } } \sqrt { \log n }$ ,

$$
\begin{array} { r } { \tau \ell _ { z } ( x , z ) ^ { T } v = \nabla \ell _ { z } ( x , \overline { { z } } ) ^ { T } v + ( z - \overline { { z } } ) ^ { T } \mathcal { H } _ { z } ^ { * } ( x , t z + ( 1 - t ) \overline { { z } } ) v = ( z - \overline { { z } } ) ^ { T } \mathcal { H } _ { z } ^ { * } ( x , t z + ( 1 - t ) \overline { { z } } ) v , } \end{array}
$$

where $t \in ( 0 , 1 )$ and depends on $v , x , z$ . Therefore,

$$
\| \nabla \ell _ { z } ( x , z ) \| \geq \operatorname* { s u p } _ { \stackrel { v \in \mathbb { R } ^ { d } } { \| v \| = 1 } } \operatorname* { i n f } _ { z \in \mathbb { B } _ { r _ { 1 } } ( \overline { { z } } ) } \big | ( z - \overline { { z } } ) ^ { T } \mathcal { H } _ { z } ^ { * } ( z ) v \big | \geq a \| z - \overline { { z } } \| .
$$

Then since $\| \nabla \ell _ { z } ( x , \phi _ { p } ( x ) ) \| = \left\| ( \nabla G ^ { * } ( \phi _ { p } ( x ) ) ^ { T } ( x - G ^ { * } ( \phi _ { p } ( x ) ) \| \lesssim \left( ( \sigma _ { \frac { L } { 2 } } \lor n ^ { - { \frac { 1 } { 2 \alpha + d } } } ) { \sqrt { \log n } } \right) ^ { \beta } \right\|$ , we can obtain

$$
\begin{array} { r } { \| \phi _ { p } ( x ) - Q ^ { * } ( \mathrm { P r o j } _ { \mathcal { M } } ( x ) ) \| = \| \phi _ { p } ( x ) - \overline { { z } } \| \lesssim \Big ( ( \sigma _ { \underline { { t } } } \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) \sqrt { \log n } \Big ) ^ { \beta } . } \end{array}
$$

Proof is completed.

# D.6 Proof of Lemma B.4

We first show that $\hat { p }$ satisfies Poincaré inequality with Poincaré constant $C _ { \mathrm { P I } } + \sigma ^ { 2 }$ . Indeed, consider $x \sim p _ { \mathrm { d a t a } }$ and $z \sim \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } )$ e, for any smooth function $f : \mathbb { R } ^ { D }  \mathbb { R }$ , we have

$$
\begin{array} { r l } & { f ( y ) - \mathbb { E } _ { \widehat { p } } [ f ( y ) ] ) ^ { 2 } \bigg ] } \\ & { \mathrm { ~ } } \\ & { \mathrm { ~ } _ { \mathrm { \scriptsize { J a t a l } } } \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \left( f ( x + z ) - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } [ f ( x + z ) ] \right) ^ { 2 } \right] } \\ & { \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } _ { \mathrm { \scriptsize { V } } ( 0 , \sigma ^ { 2 } I _ { D } ) } \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \left( f ( x + z ) - \mathbb { E } _ { p _ { \mathrm { d a t a } } } [ f ( x + z ) ] \right) ^ { 2 } \right] + \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \left( \mathbb { E } _ { p _ { \mathrm { d a t a } } } [ f ( x + z ) ] - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } [ f ( x + z ) ] \right) ^ { 2 } \right] } \\ & { \mathrm { ~ } _ { \mathrm { \scriptsize { V } } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ C _ { \mathrm { \small { P I } } } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \left\| \nabla f ( x + z ) \right\| ^ { 2 } \right] \right] + \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \left( \mathbb { E } _ { p _ { \mathrm { d a s t } } } [ f ( x + z ) ] - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \mathbb { E } _ { N ( 0 , \sigma ^ { 2 } I _ { D } ) } [ f ( x + z ) ] \right) ^ { 2 } \right] } \end{array}
$$

where the last inequality uses the fact that $p _ { \mathrm { d a t a } }$ satisfying Poincaré inequality with Poincaré constant $C _ { \mathrm { P I } }$ . Furthermore, by Gaussian Poincaré inequality, for any smooth function $g : \mathbb { R } ^ { D }  \mathbb { R }$ ,

$$
\begin{array} { r } { \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \left( g ( z ) - \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } [ g ( z ) ] \right) ^ { 2 } \right] \leq \sigma ^ { 2 } \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \| \nabla g ( z ) \| ^ { 2 } \right] . } \end{array}
$$

Choose $g ( z ) = \mathbb { E } _ { p _ { \mathrm { d a t a } } } [ f ( x + z ) ]$ in the above inequality, we can obtain

$$
\begin{array} { r l } & { \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \left( \mathbb { E } _ { p _ { \mathrm { d a t a } } } [ f ( x + z ) ] - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } [ f ( x + z ) ] \right) ^ { 2 } \right] } \\ & { \ \leq \sigma ^ { 2 } \cdot \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \| \mathbb { E } _ { p _ { \mathrm { d a t a } } } [ \nabla f ( x + z ) ] \| ^ { 2 } \right] } \\ & { \ \leq \sigma ^ { 2 } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \mathbb { E } _ { \mathcal { N } ( 0 , \sigma ^ { 2 } I _ { D } ) } \left[ \| \nabla f ( x + z ) \| ^ { 2 } \right] . } \end{array}
$$

So finally, we can obtain that

$$
\begin{array} { r } { \mathbb { E } _ { \widetilde { p } } \left[ \left( f ( y ) - \mathbb { E } _ { \widetilde { p } } [ f ( y ) ] \right) ^ { 2 } \right] \leq \left( C _ { \mathrm { P I } } + \sigma ^ { 2 } \right) \cdot \mathbb { E } _ { \widetilde { p } } \left[ \Vert \nabla f ( y ) \Vert ^ { 2 } \right] , } \end{array}
$$

Therefore, $\widetilde { p }$ satisfies Poincaré inequality with Poincaré constant $C _ { \mathrm { P I } } ^ { \prime } = C _ { \mathrm { P I } } + \sigma ^ { 2 }$ , which can imply the following econvergence result (see for example, Chewi et al. (2021))

$$
\chi ^ { 2 } ( p _ { t } \parallel \widetilde { p } ) \le \exp ( - \frac { 2 t } { C _ { \mathrm { P I } } ^ { \prime } } ) \cdot \chi ^ { 2 } ( p _ { 0 } \parallel \widetilde { p } ) ,
$$

where $p _ { t }$ denotes the distribution of $X _ { t }$ in the Langevin diffusion model. Therefore, by choosing $T = \Theta \big ( C _ { \mathrm { P I } } ^ { \prime } [ \log n \vee$ $\log ( \chi ^ { 2 } ( p _ { 0 } \| \widetilde { p }  ) ] )$ , we have $\chi ^ { 2 } ( p _ { T } \parallel \widetilde { p } ) = \mathcal { O } ( \textstyle \frac { 1 } { n } )$ . Moreover, follow the analysis in Chen et al. (2022), we can invoke eGirsanovs Theorem to shows that

$$
\begin{array} { l } { \displaystyle { d _ { \mathrm { T V } } ( p _ { T } , \widehat { p } _ { T } ) \leq \sqrt { 2 \mathrm { K L } ( p _ { T } \| \widehat { p } _ { T } ) } \leq \sqrt { \int _ { 0 } ^ { T } \int _ { \mathbb R ^ { D } } \left\| \widehat { S } ( x ) - \widetilde { S } ( x ) \right\| ^ { 2 } p _ { t } ( x ) \mathrm { d } x \mathrm { d } t } } } \\ { \displaystyle { = \sqrt { \int _ { 0 } ^ { T } \int _ { \mathbb R ^ { D } } \left\| \widehat { S } ( x ) - \widetilde { S } ( x ) \right\| ^ { 2 } \frac { p _ { t } ( x ) } { \widetilde { p } ( x ) } \widetilde { p } ( x ) \mathrm { d } x \mathrm { d } t } } } \\ { \displaystyle { \leq \left( \int _ { \mathbb R ^ { D } } \left\| \widehat { S } ( x ) - \widetilde { S } ( x ) \right\| ^ { 4 } \widetilde { p } ( x ) \mathrm { d } x \right) ^ { \frac { 1 } { 4 } } \cdot \sqrt { \int _ { 0 } ^ { T } ( \chi ^ { 2 } ( p _ { t } \| \widetilde { p } ) + 1 ) ^ { \frac { 1 } { 2 } } \mathrm { d } t } . } } \end{array}
$$

Combined with (36), we have

$$
\begin{array} { l } { \displaystyle { ^ \prime _ { \mathrm { T V } } ( \widehat { p } _ { T } , \widehat { p } ) \leq d _ { \mathrm { T V } } ( \widehat { p } _ { T } , p _ { T } ) + d _ { \mathrm { T V } } ( p _ { T } , \widehat { p } ) } } \\ { \displaystyle \leq \bigg ( \int _ { \mathbb R ^ { D } } \left\| \widehat S ( x ) - \widetilde S ( x ) \right\| ^ { 4 } \widetilde { p } ( x ) \mathrm { d } x \bigg ) ^ { \frac 1 4 } \cdot \bigg ( \sqrt { T } + \sqrt { C _ { \mathrm { P I } } ^ { \prime } \bigg ( 1 - \exp ( - \frac { T } { C _ { \mathrm { P I } } ^ { \prime } } ) \bigg ) } ( { x ^ { 2 } ( p _ { 0 } \| \widehat { p } ) } ) ^ { \frac 1 4 } }  \\ { \displaystyle \lesssim \sqrt { C _ { \mathrm { P I } } ^ { \prime } } \cdot \Big ( ( { \chi ^ { 2 } ( p _ { 0 } \| \widehat { p } ) } ) ^ { \frac 1 4 } + \sqrt { \log n } \Big ) \cdot \bigg ( \int _ { \mathbb R ^ { D } } \left\| \widehat S ( x ) - \widetilde S ( x ) \right\| ^ { 4 } \widetilde { p } ( x ) \mathrm { d } x \bigg ) ^ { \frac 1 4 } + \frac 1 n . } \end{array}
$$

# D.7 Proof of Lemma B.5

Notice that

$$
\widetilde { S } ( x ) = \frac { \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ ( y - x ) \exp ( - \frac { \| y - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] } { \sigma ^ { 2 } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp ( - \frac { \| y - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] } .
$$

Compared with the score function used in forward backward diffusion

$$
\nabla \log p _ { t } ( x ) = \frac { \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \left( m _ { t } y - x \right) \exp \left( - \frac { \left. x - m _ { t } y \right. ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \right] } { \sigma _ { t } ^ { 2 } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \frac { \left. x - m _ { t } y \right. ^ { 2 } } { 2 \sigma _ { t } ^ { 2 } } \right) \right] } ,
$$

we can see $\widetilde { S } ( \boldsymbol { x } )$ can be recovered by choosing $m _ { t } = 1$ and $o _ { t } = o$ in $\nabla \log p _ { t } ( x )$ . Therefore, follow the analysis in the proof of Lemma B.3, by choosing $L = \Theta ( \log ^ { 4 } n )$ , $\| W \| _ { \infty } = \Theta \bigl ( ( \sigma \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } ( \log ^ { 6 - \frac { d } { 2 } } n \vee \log ^ { \frac { d } { 2 } + 3 } n ) \bigr )$  , $R = \Theta \big ( ( \sigma \vee n ^ { - \frac { 1 } { 2 \alpha + d } } ) ^ { - d } ( \log ^ { 8 - \frac { d } { 2 } } n \vee \log ^ { \frac { d } { 2 } + 5 } n ) \big )$  , $B = \exp ( \Theta ( \log ^ { 4 } n ) )$ , and $\begin{array} { r } { V = \Theta \big ( \frac { \sqrt { \log n } } { \sigma } \big ) } \end{array}$ , we have

$$
\operatorname* { i n f } _ { S \in \Phi ( L , W , R , B , V ) } \mathbb { E } _ { \widetilde { \rho } } \left[ \| S ( x ) - \widetilde { S } ( x ) \| ^ { 2 } \right] \lesssim \left\{ \begin{array} { l l } { \frac { \log ^ { 4 } n } { n - 2 \alpha + d } } & { \sigma > n ^ { - \frac { 1 } { 2 \alpha + d } } } \\ { \frac { n ^ { - \frac { 2 \alpha } { 2 \alpha + d } } ( \log n ) ^ { \beta + 2 } } { \sigma ^ { 4 } } + \frac { n ^ { - \frac { 2 \alpha } { 2 \alpha + d } } ( \log n ) ^ { \alpha + 1 } } { \sigma ^ { 2 } } } & { \sigma \leq n ^ { - \frac { 1 } { 2 \alpha + d } } . } \end{array} \right.
$$

Then notice that by the equivalence of the explicit score matching and denoising score matching (see for example, Vincent (2011)), for any $S \in \Phi ( L , W , R , B , V )$ ,

$$
\mathbb { E } _ { \widetilde { p } } \left[ \| S ( x ) - \widetilde { S } ( x ) \| ^ { 2 } \right] = \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \mathbb { E } _ { z \sim \mathcal { N } ( X , \sigma ^ { 2 } I _ { D } ) } \left[ \left\| S ( z ) - \frac { X - z } { \sigma ^ { 2 } } \right\| ^ { 2 } \right] \right] + C ,
$$

where $C = \mathbb { E } _ { \widetilde { p } } [ \| \widetilde { S } ( \boldsymbol { x } ) \| ^ { 2 } ] - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \mathbb { E } _ { z \sim \mathcal { N } ( \boldsymbol { X } , \sigma ^ { 2 } I _ { D } ) } \left[ \left\| \frac { \boldsymbol { X } - \boldsymbol { z } } { \sigma ^ { 2 } } \right\| ^ { 2 } \right] \right]$ is independent of $s$ . Furthermore,

$$
{ _ { z \sim \mathcal N ( X , \sigma ^ { 2 } I _ { D } ) } } \left[ \left\| S ( z ) - \frac { X - z } { \sigma ^ { 2 } } \right\| ^ { 2 } \right] \lesssim \mathbb { E } _ { z \sim \mathcal N ( X , \sigma ^ { 2 } I _ { D } ) } \left[ \left\| S ( z ) \right\| ^ { 2 } \right] + \mathbb { E } _ { z \sim \mathcal N ( X , \sigma ^ { 2 } I _ { D } ) } \left[ \left\| \frac { X - z } { \sigma ^ { 2 } } \right\| ^ { 2 } \right] \lesssim \frac { 1 } { \sigma }
$$

Then follow the proof of Theorem 4.3 of Oko et al. (2023), we can obtain

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \mathbb { E } _ { \widetilde { p } } \left[ \| \widehat { S } ( x ) - \widetilde { S } ( x ) \| ^ { 2 } \right] \right] } \\ & { \stackrel { { \lesssim } } { \sim } _ { S \in \Phi ( L , W , R , B , V ) } \mathbb { E } _ { \widetilde { p } } \left[ \| S ( x ) - \widetilde { S } ( x ) \| ^ { 2 } \right] + \frac { \log n } { \sigma ^ { 2 } } \frac { L R \log \left( n L \| W \| _ { \infty } B \right) } { n } } \\ & { \lesssim \left\{ \begin{array} { l l } { n ^ { - 1 } \sigma ^ { - d - 2 } \left( \log ^ { 1 7 - \frac { d } { 2 } } n \vee \log ^ { \frac { d } { 2 } + 1 4 } n \right) } & { \sigma > n ^ { - \frac { 1 } { 2 \alpha + d } } } \\ { \frac { n ^ { - \frac { 2 \beta } { 2 4 } } } { \sigma ^ { 4 } } \log ^ { \beta + 2 } n + \frac { n ^ { - \frac { 2 \alpha } { 2 \alpha } + d } } { \sigma ^ { 2 } } \left( \log ^ { \alpha + 1 } n \vee \log ^ { 1 7 - \frac { d } { 2 } } n \vee \log ^ { 1 4 + \frac { d } { 2 } } n \right) } & { \sigma \leq n ^ { - \frac { 1 } { 2 \alpha + d } } . } \end{array} \right. } \end{array}
$$

Then notice that

$$
\| \widetilde { S } ( x ) \| = \left\| \frac { \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \left( y - x \right) \exp \left( - \frac { \| y - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] } { \sigma ^ { 2 } \cdot \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \frac { \| y - x \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] } \right\| \le \frac { \| x \| + D } { \sigma ^ { 2 } } .
$$

Similar as Lemma C.1, we can obtain that for any $S \in \Phi ( L , W , R , B , V )$ ,

$$
\begin{array} { r l } & { \quad \mathbb { E } _ { \widetilde { p } } \left[ \left. \widetilde { S } ( x ) - S ( x ) \right. ^ { 4 } \right] } \\ & { \leq \mathbb { E } _ { \widetilde { p } } \left[ \left. \widetilde { S } ( x ) - S ( x ) \right. ^ { 4 } \cdot 1 \left( \mathrm { d i s t } ( x , \mathcal { M } ) \leq c _ { 0 } \sigma \sqrt { \log n } \right) \right] \mathrm { d } x + \mathcal { O } ( \frac { 1 } { n ^ { 2 } } ) . } \end{array}
$$

$x \in \mathbb { R } ^ { D }$ satiwith $\mathrm { d i s t } ( x , { \mathcal { M } } ) \leq c _ { 0 } \sigma { \sqrt { \log n } }$ , we have $\| \widetilde { S } ( x ) \| _ { \infty } \leq c _ { 2 } \frac { \sqrt { \log n } } { \sigma }$ . Then combined with $\widehat { S } \in \Phi ( L , W , R , B , V )$ $\begin{array} { r } { V = \Theta \big ( \frac { \sqrt { \log n } } { \sigma } \big ) } \end{array}$

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \left( \mathbb { E } _ { \widetilde { p } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 4 } \right] \right) ^ { \frac { 1 } { 4 } } \right] } \\ & { \lesssim \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \left( \mathbb { E } _ { \widetilde { p } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 2 } \right] \right) ^ { \frac { 1 } { 4 } } \right] \frac { \log ^ { \frac { 1 } { 4 } } n } { \sqrt { \sigma } } + { \mathcal O } ( \frac { 1 } { \sqrt { n } } ) } \\ & { \lesssim \left( \mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \mathbb { E } _ { \widetilde { p } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 2 } \right] \right] \right) ^ { \frac { 1 } { 4 } } \frac { \log ^ { \frac { 1 } { 4 } } n } { \sqrt { \sigma } } + { \mathcal O } ( \frac { 1 } { \sqrt { n } } ) . } \end{array}
$$

The desired result then follows by plugging in the bound for $\mathbb { E } _ { p _ { \mathrm { d a t a } } \otimes n } \left[ \mathbb { E } _ { \widetilde { p } } \left[ \| \widetilde { S } ( x ) - \widehat { S } ( x ) \| ^ { 2 } \right] \right]$ given in (37).

# D.8 Analysis of KDE as initial distribution in Langevin diffusion

Lemma D.1. Consider $o$ satisfying $n ^ { - \delta _ { 1 } } \lesssim \sigma \lesssim n ^ { - \delta _ { 2 } }$ for any positive constants $( \delta _ { 1 } , \delta _ { 2 } )$ . Let the initial distribution be the kernel density estimator $\begin{array} { r } { p _ { 0 } ( y ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \cdot ( 2 \pi \sigma ^ { 2 } ) ^ { - \frac { D } { 2 } } } \end{array}$ . It holds with probability at least $\textstyle 1 - { \frac { 1 } { n } }$ that

$$
\chi ^ { 2 } ( p _ { 0 } \parallel p _ { \mathrm { d a t a } , \sigma } ) \lesssim \frac { 1 } { n } ( \log n ) ^ { \frac { 3 d } { 2 } + 1 } \sigma ^ { - d } + \frac { 1 } { n ^ { 2 } } ( \log n ) ^ { d + 2 } \sigma ^ { - 2 d } .
$$

Proof. For any $r _ { n } \geq 0$ , we can write

$$
\begin{array} { r l } & { \chi ^ { 2 } ( p _ { 0 } \| p _ { \mathrm { d a t a } , \sigma } ) = \mathbb { E } _ { p _ { \mathrm { d a t a } , \sigma } } \left[ \left( \frac { p _ { 0 } } { p _ { \mathrm { d a t a } , \sigma } } - 1 \right) ^ { 2 } \right] } \\ & { = \displaystyle \int _ { \mathbb { R } ^ { D } } \left( \frac { p _ { 0 } ( y ) } { p _ { \mathrm { d a t a } , \sigma } ( y ) } - 1 \right) ^ { 2 } \cdot \mathbf { 1 } \left( \mathrm { d i s t } ( y , \mathcal { M } ) \leq r _ { n } \right) \cdot p _ { \mathrm { d a t a } , \sigma } ( y ) \mathrm { d } y } \\ & { + \displaystyle \int _ { \mathbb { R } ^ { D } } \frac { ( p _ { 0 } ( y ) - p _ { \mathrm { d a t a } , \sigma } ( y ) ) ^ { 2 } } { p _ { \mathrm { d a t a } , \sigma } ( y ) } \cdot \mathbf { 1 } \left( \mathrm { d i s t } ( y , \mathcal { M } ) > r _ { n } \right) \mathrm { d } y } \\ & { = \displaystyle \int _ { \mathbb { R } ^ { D } } \left( \frac { n ^ { - 1 } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] } { \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] } \right) ^ { 2 } \cdot \mathbf { 1 } \left( \mathrm { d i s t } ( y , \mathcal { M } ) \leq r _ { n } \right) \cdot p _ { \mathrm { d a t a } , \sigma } ( y ) . } \end{array}
$$

$$
+ \int _ { \mathbb { R } ^ { D } } ( 2 \pi \sigma ^ { 2 } ) ^ { - \frac { D } { 2 } } \cdot \frac { \left( n ^ { - 1 } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \right) ^ { 2 } } { \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] } \cdot \mathbf { 1 } \left( \mathrm { d i s t } ( y , M ) > r _ { n } \right) \mathrm { d }
$$

We first bound term $( B )$ . For any $y \in \mathbb { R } ^ { D }$ , denote $\mathrm { P r o j } _ { \mathcal { M } } ( y )$ as an arbitrary point inside $\mathrm { a r g m i n } _ { y ^ { \prime } \in \mathcal { M } } \| y ^ { \prime } - y \|$ Then we have

$$
\begin{array} { r l } { \mathbb { E } \left[ \exp ( - \displaystyle \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \geq \int _ { \{ 1 : - \mathrm { P r o j } _ { \lambda \times } ( y ) \} \bigcup \atop | x - \mathrm { P r o j } _ { \lambda \times } ( y ) } \exp ( - \displaystyle \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) f ( X ) \mathrm { d } \mathrm { v o l } _ { \mathcal { M } } ( X ) } & { } \\ { \gtrsim \sigma ^ { d } \exp \left( - \displaystyle \frac { ( \mathrm { d i s t } ( y , \mathcal { M } ) + \sigma ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right) } & { } \\ { \gtrsim \sigma ^ { d } \cdot \exp \left( - \frac { 3 \cdot \mathrm { d i s t } ( y , \mathcal { M } ) ^ { 2 } } { 4 \sigma ^ { 2 } } \right) , } & { } \\ { \mathbb { E } \left[ \exp ( - \displaystyle \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \leq \exp \left( - \frac { \mathrm { d i s t } ( y , \mathcal { M } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right) , } & { } \\ { \quad \quad \pi ^ { - 1 } \displaystyle \sum _ { i = 1 } ^ { n } \exp ( - \displaystyle \frac { \| X _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \leq \exp \left( - \frac { \mathrm { d i s t } ( y , \mathcal { M } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right) . } \end{array}
$$

Without loss of generality, we assume $\mathcal { M } \subset \mathbb { B } _ { 1 } ( 0 _ { D } )$ , then we have

$$
\begin{array} { r l } & { ( B ) \lesssim \displaystyle \int _ { \mathbb R ^ { D } } \sigma ^ { - ( D + d ) } \cdot \exp \left( - \frac { \operatorname { d i s t } ( y , \mathcal { M } ) ^ { 2 } } { 4 \sigma ^ { 2 } } \right) \cdot \mathbf { 1 } \left( \operatorname { d i s t } ( y , \mathcal { M } ) > r _ { n } \right) \mathrm { d } y } \\ & { \quad \quad \leq \displaystyle \int _ { \| y \| \leq 2 } \exp ( - \frac { r _ { n } ^ { 2 } } { 4 \sigma ^ { 2 } } ) \cdot \sigma ^ { - ( D + d ) } \mathrm { d } y _ { n } + \displaystyle \int _ { \| y \| > 2 } \exp \left( - \frac { ( \| y \| - 1 ) ^ { 2 } } { 4 \sigma ^ { 2 } } \right) \cdot \sigma ^ { - ( D + d ) } \mathrm { d } y _ { n } , } \end{array}
$$

where we use $\mathrm { d i s t } ( y , \mathcal { M } ) \geq \| y \| - 1$ in the last inequality. Therefore, by choosing $r _ { n } = \Theta ( \sigma \sqrt { \log n } )$ , we have

$$
( B ) \lesssim { \frac { 1 } { n } } .
$$

Then for the term ( $A$ ), let $N _ { \sigma / \sqrt { \log n } }$ be a $\sigma / { \sqrt { \log n } }$ cover of $\mathcal { M }$ . By Lemma C.2, we have $J = | N _ { \sigma / \sqrt { \log n } } | \lesssim$ $\textstyle ( { \frac { \sqrt { \log n } } { \sigma } } ) ^ { d }$ . Denote $N _ { \sigma / \sqrt { \log n } } = \{ Y _ { 1 } , Y _ { 2 } , \cdot \cdot \cdot , Y _ { J } \}$ and

$$
\begin{array} { l } { \displaystyle 4 _ { k , j } = \left\{ y \in \mathbb { R } ^ { D } : ( k - 1 ) \frac { \sigma } { \sqrt { \log n } } \leq \mathrm { d i s t } ( y , \mathcal { M } ) \leq k \frac { \sigma } { \sqrt { \log n } } , \quad \| \mathrm { P r o j } _ { \mathcal { M } } ( y ) - Y _ { j } \| \leq \frac { \sigma } { \sqrt { \log n } } \right\} , } \\ { \displaystyle \in \{ 1 , 2 , \cdots , K \} , \quad j \in { 1 , 2 , \cdots , J } . } \end{array}
$$

Notice that since $\mathcal { M }$ has a reach $\tau _ { \mathcal { M } }$ that is lower bounded away from zero, $\mathrm { P r o j } _ { \mathcal { M } } ( y )$ is uniquely defined when $\mathrm { d i s t } ( y , \mathcal { M } ) \leq \tau _ { \mathcal { M } } > 0$ . Then set $K = \Theta ( \log n )$ , we have

$$
\begin{array} { r } { \{ y \in \mathbb { R } ^ { D } : \operatorname { d i s t } ( y , { \mathcal { M } } ) \leq r _ { n } \} \subset \cup _ { k = 1 } ^ { K } \cup _ { j = 1 } ^ { J } { \mathcal { A } } _ { k , j } . } \end{array}
$$

Consider an arbitrary $k \in [ K ]$ and $j \in [ J ]$ , we aim to bound

$$
\operatorname* { s u p } _ { y \in \mathcal { A } _ { k , j } } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \right| .
$$

Denote $y ^ { * } = Y _ { j }$ and $\begin{array} { r } { \underline { { r } } = ( k - 1 ) \frac { \sigma } { \sqrt { \log n } } } \end{array}$ σ For any $y \in A _ { k , j }$ and $x \in \mathcal { M }$ so that $\begin{array} { r } { \| x - y ^ { * } \| > 2 { \underline { { r } } } + { \frac { 2 \sigma } { \sqrt { \log n } } } + \sigma \sqrt { d \log { \frac { 1 } { \sigma } } } } \end{array}$ we have

$$
\begin{array} { r } { \| x - y \| \geq \| x - y ^ { * } \| - \| y ^ { * } - \operatorname { P r o j } _ { \mathcal { M } } ( y ) \| - \| y - \operatorname { P r o j } _ { \mathcal { M } } ( y ) \| \geq \underline { { r } } + \sigma \sqrt { d \log \frac { 1 } { \sigma } } . } \end{array}
$$

Therefore, for any $y , y ^ { \prime } \in \mathcal { A } _ { k , j }$ , we have

$$
\begin{array} { r l r } {  { n ( y , y ^ { \prime } ) = \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \exp ( - \frac { \| x _ { i } - y ^ { \prime } \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \exp ( - \frac { \| x _ { i } - y ^ { \prime } \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) ) ^ { 2 } } } } \\ & { } & { \leq \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \exp ( - \frac { \| x _ { i } - y ^ { \prime } \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) ) ^ { 2 } \cdot 1 } ( \| x _ { i } - y ^ { * } \| > 2 x + \frac { 2 \sigma } { \sqrt { \log } }  } \\ & { } & { + \sqrt { \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \exp ( - \frac { \| x _ { i } - y ^ { \prime } \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) ) ^ { 2 } \cdot 1 } ( \| x _ { i } - y ^ { * } \| \leq 2 _ { L } + \frac { 2 \sigma } { \sqrt { \log } } , } \\ & { } & { \leq \exp ( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } } ) \cdot \sqrt { \sigma ^ { d } + \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( \| x _ { i } - y ^ { * } \| \leq 2 _ { L } + \frac { 2 \sigma } { \sqrt { \log } n } + \sigma \sqrt { d \log } \frac { 1 } { \sigma } ) } . } \end{array}
$$

Furthermore, since for any $y , y ^ { \prime } \in \mathcal { A } _ { k , j }$ ,

$$
d _ { n } ( y , y ^ { \prime } ) \lesssim \frac { \| y - y ^ { \prime } \| } { \sigma ^ { 2 } } ,
$$

denote ωn = 1n Pni=1 1 ∥xi − y∗∥ ≤ 2r + √2σlog n , for any $\epsilon \leq \exp \bigl ( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } } \bigr ) \cdot \sqrt { \sigma ^ { d } + \omega _ { n } }$ , the $\epsilon$ -covering number of $\boldsymbol { \mathcal { A } _ { k , j } }$ under pseudo-metric $d _ { n }$ is upper bounded by $\exp ( \mathcal { O } ( \log \frac { n } { \epsilon } ) )$ ). Therefore, by standard symmetrization and Dudleys entropy integral bound (see for example, Theorem 5.22 of Wainwright (2019)), let $\{ \varepsilon _ { i } \} _ { i = 1 } ^ { n }$ be

i.i.d . Rademacher random variables, we have

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { \mathrm { d a t a s } } \theta ^ { n } } \left[ \displaystyle { \operatorname* { s u p } _ { y \in \mathcal { A } _ { k } , \infty } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp \left( - \frac { \left\| x _ { i } - y \right\| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) - \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \frac { \left\| X - y \right\| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] \right|}  \right] } \\ & { \le \mathbb { E } \left[ \displaystyle { \operatorname* { s u p } _ { y \in \mathcal { A } _ { k } , \infty } \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \epsilon \exp \left( - \frac { \left\| X _ { i } - y \right\| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right|}  \right] } \\ & { \lesssim \mathbb { E } _ { p _ { \mathrm { d a t a } } \theta ^ { n } } \left[ \displaystyle { \frac { 1 } { \sqrt { n } } \int _ { 0 } ^ { \infty \nu ( - \frac { \sigma ^ { 2 } } { 2 \sigma ^ { 2 } } ) \cdot \sqrt { \sigma ^ { d + } \omega _ { n } } } \sqrt { \log \frac { n } { \epsilon } } \mathrm { d } \epsilon } \right] } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \sqrt { \log n } \epsilon \exp ( - \frac { \frac { \sigma ^ { 2 } } { 2 \sigma ^ { 2 } } } { 2 \sigma ^ { 2 } } ) \mathbb { E } _ { p _ { \mathrm { d a t a } } \theta ^ { n } } \left[ \sqrt { \sigma ^ { d } + \omega _ { n } } \right] } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \sqrt { \log n } \exp ( - \frac { \lambda ^ { 2 } } { 2 \sigma ^ { 2 } } ) ( \sigma \sqrt { \log n } ) ^ { \frac { \lambda } { 2 } } . } \end{array}
$$

Moreover, for any $y \in A _ { k , j }$ and $x \in \mathcal { M }$ ,

$$
\exp \left( - \frac { \| x - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \leq \exp ( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } } ) ,
$$

and

$$
\begin{array} { r l } & { \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \displaystyle \frac { \| X - y \| ^ { 2 } } { \sigma ^ { 2 } } \right) \right] } \\ & { \leq \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \displaystyle \frac { \| X - y \| ^ { 2 } } { \sigma ^ { 2 } } \right) \cdot \mathbf { 1 } \left( \| X - \mathrm { P r o j } _ { \mathcal { M } } ( y ) \| \leq 2 { _ { \overline { { r } } } } + \sqrt { 2 } \sigma \sqrt { d \log \frac { 1 } { \sigma } } + \frac { \sigma } { \sqrt { \log n } } \right) \right] } \\ & { + \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \displaystyle \frac { \| X - y \| ^ { 2 } } { \sigma ^ { 2 } } \right) \cdot \mathbf { 1 } \left( \| X - \mathrm { P r o j } _ { \mathcal { M } } ( y ) \| > 2 { _ { \overline { { r } } } } + \sqrt { 2 } \sigma \sqrt { d \log \frac { 1 } { \sigma } } + \frac { \sigma } { \sqrt { \log n } } \right) \right] } \\ & { \lesssim ( \sigma \sqrt { \log n } ) ^ { d } \exp ( - \frac { { r ^ { 2 } } } { \sigma ^ { 2 } } ) . } \end{array}
$$

So by Talagrand concentration inequality (see, for example, Theorem 3.27 of Wainwright (2019)), it holds with probability at least $1 - n ^ { - ( \delta _ { 1 } d + 2 ) }$ that

$$
\begin{array} { r l } {  { \operatorname* { s u p } _ { y \in \mathcal { A } _ { k , j } } | \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } [ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) ] | } } \\ & { \lesssim \frac { 1 } { \sqrt { n } } \sqrt { \log n } \exp ( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } } ) ( \sigma \sqrt { \log n } ) ^ { \frac { d } { 2 } } + \frac { \log n } { n } \exp ( - \frac { r ^ { 2 } } { 2 \sigma ^ { 2 } } ) . } \end{array}
$$

Moreover, notice that for any $y \in A _ { k , j }$ ,

$$
\begin{array} { r l } & { \mathrm { \Lambda } _ { ^ { \ p } \mathrm { d a t a } } ^ { \prime } \left[ \exp \left( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] \geq \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \cdot \mathbf { 1 } \left( \| X - \mathrm { P r o j } _ { \mathcal { M } } ( y ) \| \leq \frac { \sigma } { \sqrt { \log n } } \right) \right] } \\ & { \qquad \gtrsim \exp \left( - \frac { ( { \underline { { r } } } + \frac { 2 \sigma } { \sqrt { \log n } } ) ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \cdot \sigma ^ { d } ( \log n ) ^ { - \frac { d } { 2 } } , } \end{array}
$$

we have

$$
\operatorname* { s u p } _ { \in A _ { k , j } } \frac { \left| \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \right| } { \mathbb { E } _ { p _ { \mathrm { d a t s } } } \left[ \exp \left( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] } \lesssim \frac { 1 } { \sqrt { n } } ( \sigma ) ^ { - \frac { d } { 2 } } ( \log n ) ^ { \frac { 3 d } { 4 } + \frac { 1 } { 2 } } + \frac { 1 } { n } ( \sigma ) ^ { - d } ( \log n )
$$

Then use the fact that $K J \lesssim ( \log n ) ^ { { \frac { d } { 2 } } + 1 } \sigma ^ { - d } \lesssim ( \log n ) ^ { { \frac { d } { 2 } } + 1 } n ^ { \delta _ { 1 } d }$ , we have it holds with probability at least $1 - { \textstyle { \frac { 1 } { n } } }$ that

$$
\operatorname { \rho } _  y , M ) \leq r _ { n } \} \frac { \bigg \vert \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \exp ( - \frac { \| x _ { i } - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) - \mathbb { E } \left[ \exp ( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } ) \right] \bigg \vert } { \mathbb { E } _ { p _ { \mathrm { d a t a } } } \left[ \exp \left( - \frac { \| X - y \| ^ { 2 } } { 2 \sigma ^ { 2 } } \right) \right] } \lesssim \frac { 1 } { \sqrt { n } } ( \sigma ) ^ { - \frac { d } { 2 } } ( \log n ) ^ { \frac { 3 d } { 4 } + \frac { 1 } { 2 } } + \frac { 1 } { n } ( \sigma ) ^ { - d } ( \log n ) ^ { \frac { d - 1 } { 4 } } ,
$$

Therefore, we have

$$
( A ) \lesssim \frac { 1 } { n } ( \sigma ) ^ { - d } ( \log n ) ^ { \frac { 3 d } { 2 } + 1 } + \frac { 1 } { n ^ { 2 } } ( \sigma ) ^ { - 2 d } ( \log n ) ^ { d + 2 } .
$$

We can then obtain the desired result by combining all pieces.

# References

Bakry, D., Gentil, I., Ledoux, M. et al. (2014) Analysis and geometry of Markov diffusion operators, vol. 103. Springer.   
Chen, S., Chewi, S., Li, J., Li, Y., Salim, A. and Zhang, A. R. (2022) Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions. arXiv preprint arXiv:2209.11215.   
Chewi, S., Erdogdu, M. A., Li, M. B., Shen, R. and Zhang, M. (2021) Analysis of langevin monte carlo from poincaré to log-sobolev.   
Divol, V. (2022) Measure estimation on manifolds: an optimal transport approach. Probability Theory and Related Fields, 183, 581–647.   
Oko, K., Akiyama, S. and Suzuki, T. (2023) Diffusion models are minimax optimal distribution estimators. arXiv preprint arXiv:2303.01861.   
Tang, R. and Yang, Y. (2023) Supplement to “minimax rate of distribution estimation on unknown submanifolds under adversarial losses”.   
Vincent, P. (2011) A connection between score matching and denoising autoencoders. Neural computation, 23, 1661–1674.   
Wainwright, M. J. (2019) High-dimensional statistics: A non-asymptotic viewpoint, vol. 48. Cambridge university press.