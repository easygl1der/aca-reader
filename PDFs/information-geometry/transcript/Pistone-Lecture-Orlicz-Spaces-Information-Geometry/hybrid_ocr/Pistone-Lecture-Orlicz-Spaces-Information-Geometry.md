# A LECTURE ABOUT THE USE OF ORLICZ SPACES IN INFORMATION GEOMETRY

GIOVANNIPISTONE

ABSTRACT. This chapter is a revised version of a tutorial lecture that I presented at the École de Physique des Houches on July 26-31 2020. Topics include: Non-parametric Information Geometry, the Statistical bundle, exponential Orlicz spaces, and Gaussian Orlicz-Sobolev spaces

# 1. INTRODUCTION

This chapter is a revision of the lecture and the related hand-out which I presented to the École de Physique des Houches on July 26-31 2020. Due to its strictly tutorial character, I shall not give detailed primary references. I shall mention some references that expand and support specific points, and I shall add some in a final section to point to further developments.

I aim to review the basics of a peculiar setting for Information Geometry (IG) in the sense of [3]. This setting has the following peculiarities.

- It is non-parametric and infinite-dimensional.   
- It provides an affine manifold modeled on a Banach space in the sense of [15], the Banach space being an Orlicz space as defined [1, Ch. 8].   
- It focuses on a particular expression of the tangent bundle, called Statistical Bundle (ST).   
- It allows for the use of (weakly) differentiable densities when the reference measure is Gaussian as in [19, Ch. V].

A previous tutorial paper [32] presents this non-parametric construction in the case of finite state space. A general presentation of the finite case is in [4, Ch. 2]. Here, I will focus on the preliminaries of the infinite state space case. A comprehensive modern introduction to the whole topic is found in [23].

There are many other successful presentations of IG which are indeed non-parametric. I will give a few relevant references in the concluding section. Any useful presentation should explain and include its historical development elements below 1 to 5.

1. The starting point to consider is the now classical work of R. Fisher, see, for example, [10, Ch. 4]. A regular statistical model is a mapping from a set of parameters $\Theta$ which is an open domain of $\mathbb{R}^d$ to probability densities on a given measured sample space $\mathcal{P}(X,\mathcal{X},\mu)$ , $\theta \mapsto p(\theta)$ , such that the following computation is feasible. If $f$ is a given random variable, one wants to compute the variation of

the expectation (assuming its existence), as

$$
\begin{array}{l} \frac {\partial}{\partial \theta_ {i}} \mathbb {E} _ {p (\theta)} [ f ] = \frac {\partial}{\partial \theta_ {i}} \int f p (\theta) d \mu = \frac {\partial}{\partial \theta_ {i}} \langle f, p (\theta) \rangle_ {\mu} = \\ \left\langle f, \frac {\partial}{\partial \theta_ {i}} p (\theta) \right\rangle_ {\mu} = \left\langle f, \frac {\frac {\partial}{\partial \theta_ {i}} p (\theta)}{p (\theta)} p (\theta) \right\rangle_ {\mu} = \left\langle f, \frac {\partial}{\partial \theta_ {i}} \log p (\theta) \right\rangle_ {p (\theta)} = \\ \left\langle f - \mathbb {E} _ {p (\theta)} [ f ], \frac {\partial}{\partial \theta_ {i}} \log p (\theta) \right\rangle_ {p (\theta)}. \\ \end{array}
$$

The random vector with components $\frac{\partial}{\partial\theta_i}\log p(\theta)$ is the Fisher score of the model at $\theta$ . Its expected value with respect to $p(\theta)$ is 0 and its variance matrix with respect to $p(\theta)$ is the Fisher information matrix,

$$
I (\theta) = \left[ \mathbb {E} _ {p (\theta)} \left[ \frac {\partial}{\partial \theta_ {i}} \log p (\theta) \frac {\partial}{\partial \theta_ {j}} \log p (\theta) \right] \right] _ {i j} = \left[ \int \frac {\frac {\partial}{\partial \theta_ {i}} p (\theta) \frac {\partial}{\partial \theta_ {j}} p (\theta)}{p (\theta)} d \mu \right] _ {i j}. \tag {1}
$$

The computations above show many peculiar features:

- One computes the variation of the expectation as a function of the statistical model. Moreover, a moving inner product $\theta \mapsto \langle \cdot, \cdot \rangle_{p(\theta)}$ appears naturally.   
- The score $\partial_i\log p(\theta)$ represents the velocity of variation of the statistical model, while $f - \mathbb{E}_{p(\theta)}[f]$ represents the gradient of the expectation function.   
- The velocity at $\theta$ lives in the space of random variables centred at $p(\theta)$ .   
- The information matrix provides squared norms and scalar products of the velocities in the moving inner product.

2. One explanation of the Fisher computations results from the assumption of an exponential model,

$$
p (\theta) = \mathrm {e} ^ {\sum_ {i} \theta_ {i} u _ {i} - \kappa (\theta)},
$$

where $u_{i}$ are the sufficient statistics and $\kappa(\theta)$ is the cumulant of $\sum_{i} \theta_{i} u_{i}$ , see, for example, [10, Ch. 5]. In such a case, the score is the centered sufficient statistics,

$$
\partial_ {i} \log p (\theta) = u _ {i} - \partial_ {i} \kappa (\theta) = u _ {i} - \mathbb {E} _ {p (\theta)} [ u _ {i} ],
$$

and the information matrix equals the Hessian of the convex function $\theta \mapsto \kappa(\theta)$ ,

$$
I (\theta) = \left[ \partial_ {i} \partial_ {j} \kappa (\theta) \right] _ {i j}.
$$

See [6, Ch. 2] for a full account of analytic properties of exponential families.

3. C. R. Rao has been the first statistician to remark that the Fisher information matrix is positive definite and smooth in an adequately defined regular model. Hence it defines a Riemannian metric on the space of parameters. Moreover, he provided an embedding argument for the resulting manifold. What possibly inspired him in his construction was Differential Geometry use in Physics. The original presentation of IG in [3] can be considered the full unfolding of this approach.

The mapping

$$
\Theta \ni \theta \mapsto 2 \sqrt {p (\theta)} = P (\theta)
$$

maps the parameters' space $\Theta$ into the $L^2 (\mu)$ -sphere of radius 2. The vectors

$$
\partial_ {i} P (\theta) = \partial_ {i} 2 \sqrt {p (\theta)} = \frac {\partial_ {i} p (\theta)}{\sqrt {p (\theta)}}
$$

are in the tangent space at $P(\theta)$ of the sphere, and the inner product between tangent vector is

$$
\int \partial_ {i} P (\theta) \partial_ {j} P (\theta) d \mu = \int \frac {\partial_ {i} p (\theta) \partial_ {j} (x , \theta)}{p (x ; \theta)} d \mu ,
$$

that is, the $(i,j)$ element of the Fisher information matrix.

The Rao's computations above reproduce all the metric structure of the Fisher computations but in one point. That is, now the velocity is not expressed by the logarithmic derivative $\partial_i\log p(\theta) = \partial_ip(\theta) / p(\theta)$ , but it is expressed by $\partial_i2\sqrt{p(\theta)} = \partial_ip(\theta) / \sqrt{p(\theta)}$ .

It is possible to make sense, at least formally, of the apparent contradiction by considering that there are here three different expressions of the same object.

- $T\mathcal{P}_{>}$ is the tangent bundle of the set of positive densities $\mathcal{P}_{>}$ ; the tangent vectors $\dot{p}$ satisfy $\int \dot{p} d\mu = 0$ .   
- $TS_{2}$ is the tangent bundle of the $L^2 (\mu)$ sphere $S_{2}$ .   
- $SP_{>}$ is the Fisher's statistical bundle consisting of all couples $(p.u)$ such that $p \in \mathcal{P}_{>}$ and $\mathbb{E}_p[u] = 0$ .

The Rao's embedding $p \mapsto 2\sqrt{p}$ provides the identification of $T\mathcal{P}$ with $TS_2$ . In fact, the computation of the tangent mapping of $s \colon P \mapsto P^2 / 4 = p$ gives $ds(P)[\dot{P}] = \sqrt{p}\dot{P}$ .

The identification of $TS_{2}$ with $\mathcal{SP}$ is provided by

$$
T S _ {2} \ni (P, \dot {P}) \mapsto \left(\frac {1}{4} P ^ {2}, 2 \frac {\dot {P}}{P}\right) = (p, u) \in S \mathcal {P}.
$$

In fact,

$$
\int p d \mu = \frac {1}{4} \int P ^ {2} d \mu = 1,
$$

$$
\int u p d \mu = \frac {1}{2} \int \frac {\dot {P}}{P} P ^ {2} d \mu = \frac {1}{2} \int P \dot {P} d \mu = 0,
$$

$$
\int u _ {1} u _ {2} p d \mu = \int \frac {\dot {P} _ {1}}{P} \frac {\dot {P} _ {2}}{P} P ^ {2} d \mu = \int \dot {P} _ {1} \dot {P} _ {2} d \mu .
$$

A large part of the literature in IG uses the expressions $T\mathcal{P}$ and $TS_{2}$ . Still, my own choice is to use $S\mathcal{P}$ . It fits well with the statistical picture and the exponential representation of strictly positive densities.

The choice of the exponential expression and Fisher's score might seem arbitrary, but the following argument shows is not, see [4, Ch. 3]. Assume $t \mapsto \mu(t)$ is a one-dimensional smooth model of probability measures and assume the mapping $t \mapsto \mu(A; t)$ is smooth for all measurable $A$ . Fix a value $\bar{t}$ of the parameter $t$ . If a measurable set $A$ is a zero set for $\mu(\bar{t})$ , then $t \mapsto \mu(A, t)$ is minimum at $t = \bar{t}$ then the derivative is zero at $\bar{t}$ , namely $\dot{\mu}(\bar{t}) = 0$ . It follows that the measure $\dot{\mu}(\bar{t})$ is absolutely continuous with respect to $\mu(\bar{t})$ . The resulting logarithmic derivative $d\dot{\mu}(\bar{t}) / d\mu(\bar{t})$ is clearly a generalization of the Fisher's score.

4. The Riemannian approach by C. R. Rao can lead to a more in-depth study of the second-order properties of the manifold, namely the Levi-Civita connection

and the curvature. Several authors, notably S-I. Amari, B. Efron, Ph. Dawid, S. Lauritzen have promoted a more general perspective in studying the geometry of statistical models. In modern terminology, a statistical manifold consists of a metric and a couple of flat connections, in duality for the given inner product. This set-up nicely solves the divide between Fisher's and Rao's approach by producing a unified theory. Moreover, the specific type of affine manifold relevant for IG is a Hessian manifold. That is, all its structure depends on a master convex functional. 5. Both theoretical and applied research have recently shown interest in a particular type of non-parametric statistical models. Namely, models where the real space $\mathbb{R}^n$ is a model for the sample space, the reference measure is either the Lebesgue measure or the Gaussian measure and the densities are required to have some level of smoothness.

For example, there is the statistical estimation method based on Hyvarinen's divergence,

$$
\mathrm {D H} (p | q) = \frac {1}{2} \int \left| \nabla \log p (x) - \nabla \log q (x) \right| ^ {2} p (x) d x, \tag {2}
$$

see [2, §13.6.2], where $p, q$ are positive probability densities of the $n$ -dimensional Lebesgue space. It is assumed that the log-densities are smooth and the integral exists. If we define the Otto's inner product by

$$
\langle \langle f, g \rangle \rangle_ {p} = \int \nabla f (x) \cdot \nabla g (x) p (x) d x, \tag {3}
$$

where $p$ is a probability density and $f, g$ are smooth random variables such that $\mathbb{E}_p[f] = \mathbb{E}_p[g] = 0$ , then the development of the square in the Hyvarinen divergence produces the term

$$
\left\langle \left\langle \log p - \mathbb {E} _ {p} \left[ \log p \right], \log q - \mathbb {E} _ {p} \left[ \log q \right] \right\rangle \right\rangle_ {p}.
$$

Notice that the equation above with $p = q$ reminds of the Fisher information of eq. (1), with parameter derivative replaced by spatial derivatives. In particular, parameter and spatial derivatives coincide in the case of translation models, that is, when $p(x,\theta) = p(x + \theta)$ .

In the Gaussian case, the celebrated log-Sobolev inequality, see [16, Ch. 5], can be written as

$$
\begin{array}{l} \operatorname {E n t} (p) = \int p (x) \log p (x) \gamma (x) d x \leq \\ 2 \int \left| \nabla \sqrt {p (x)} \right| ^ {2} \gamma (x) d x = \frac {1}{2} \langle \langle \log p - \mathrm {E n t} (p), \log p - \mathrm {E n t} (p) \rangle \rangle_ {p}, \\ \end{array}
$$

where $\gamma$ is the standard Gaussian density, $p$ is a density with respect to $\gamma$ and $|\cdot|$ is the Euclidean norm.

In the following, I shall focus on the exponential representation of positive densities $p = \mathrm{e}^{u - K(u)}$ . The reference measure is specialised to be $\mu(dx) = \gamma(x)dx$ where $\gamma$ is the standard Gaussian density of $\mathbb{R}^n$ . The sufficient statistics $u$ is assumed to belong to an exponential Orlicz space, to be defined next, and such that $\int u(x)\gamma(x)dx = 0$ . The normalizing constant $u \mapsto K(u)$ is a convex function defined on the exponential Orlicz space. The interior of the proper domain of $K$ is the parameter set of a maximal exponential Gaussian space model. Here, maximal means that the model contains all possible finite dimensional exponential families. I will aim to sketch a theory in which all concerns of items 1 to 5 meet a solution of a sort.

# 2. ORLICZ SPACES

First, let us review a few elements of the theory of Orlicz spaces and fix a convenient notation. I do not not aim to full generality, cf. [1, Ch. 8]. If $\phi \in C[0, +\infty[$ satisfies:

(1) $\phi (0) = 0$   
(2) $\phi$ is strictly increasing, and   
(3) $\lim_{u\to +\infty}\phi (u) = +\infty$

then its primitive function

$$
\Phi (x) = \int_ {0} ^ {x} \phi (u) d u, x \geq 0,
$$

is strictly convex. The function $\Phi$ is extended to $\mathbb{R}$ by symmetry, $\Phi(x) = \Phi(|x|)$ , and is called Young function.

The inverse function $\psi = \phi^{-1}$ has the same properties 1) to 3) as $\phi$ , so that its primitive

$$
\Psi (y) = \int_ {0} ^ {y} \psi (v) d v, y \geq 0,
$$

is again a Young function. The couple $(\Phi, \Psi)$ , is a couple of conjugate Young functions. The relation is symmetric and we write both $\Psi = \Phi_*$ and $\Phi = \Psi_*$ . The Young inequality holds true,

$$
\Phi (x) + \Psi (y) \geq x y, \quad x, y \geq 0,
$$

and the Legendre equality holds true,

$$
\Phi (x) + \Psi (\phi (x)) = x \phi (x), \quad x \geq 0.
$$

Here are the specific cases I am going to use. The sub-2 index denotes the 2nd Taylor remainder.

(4) $\Phi_{\alpha}(x) = \frac{x^{\alpha}}{\alpha}, \quad \Psi_{\beta}(y) = \frac{y^{\beta}}{\beta}, \quad \alpha, \beta > 1, \quad \frac{1}{\alpha} + \frac{1}{\beta} = 1;$   
(5) $\exp_2(x) = \mathrm{e}^x - 1 - x, \quad (\exp_2)_*(y) = (1 + y)\log (1 + y) - y;$   
(6) $\cosh_2(x) = \cosh x - 1, \quad (\cosh_2)_*(y) = \int_0^y \sinh^{-1}(v) \, dv;$   
(7) $\mathrm{gauss}_2(x) = \exp \left(\frac{1}{2} x^2\right) - 1.$

Given a Young function $\Phi$ and a probability measure $\mu$ , the Orlicz space $L_{\Phi}(\mu)$ is the Banach space whose closed unit ball is $\left\{f \in L^0(\mu) \mid \int \Phi(|f|) d\mu \leq 1\right\}$ . This defines the Luxemburg norm, characterized by

$$
\| f \| _ {L _ {\Phi} (\mu)} \leq \rho \quad \text {i f , a n d o n l y i f ,} \quad \int \Phi \left(\rho^ {- 1} | f |\right) d \mu \leq 1.
$$

Because of the Young inequality, it holds

$$
\int | u v | d \mu \leq \int \Phi (| u |) d \mu + \int \Phi_ {*} (| v |) d \mu .
$$

This provides a separating duality $\langle u,v\rangle_{\mu} = \int uv  d\mu$ of $L_{\Phi}(\mu)$ and $L_{\Phi_{*}}(\mu)$ such that

$$
\left\langle u, v \right\rangle_ {\mu} \leq 2 \left\| u \right\| _ {L _ {\Phi} (\mu)} \left\| v \right\| _ {L _ {\Phi *} (\mu)}.
$$

From the conjugation between $\Phi$ and $\Psi$ , an equivalent norm can be defined, namely, the Orlicz norm

$$
\left\| f \right\| _ {L _ {\Phi} (\mu) ^ {*}} = \sup  \left\{\langle f, g \rangle_ {\mu} \Big | \| f \| _ {L _ {\Psi} (\mu)} \leq 1 \right\}.
$$

The domination relation between Young functions imply continuous injection properties for the corresponding Orlicz spaces. We will say that $\Phi_2$ eventually dominates $\Phi_1$ , written $\Phi_1 < \Phi_2$ , if there is a constant $k$ such that $\Phi_1(x) \leq \Phi_2(kx)$ for all $x$ larger than some $\bar{x}$ . As, in our case, $\mu$ is a probability measure, the continuous embedding $L_{\Phi_2}(\mu) \to L_{\Phi_1}(\mu)$ holds if, and only if, $\Phi_1 < \Phi_2$ . If $\Phi_1 < \Phi_2$ , then $(\Phi_2)_* < (\Phi_1)_*$ .

A special case occurs when there exists a function $C$ such that $\Phi(ax) \leq C(a)\Phi(x)$ for all $a \geq 0$ , which is the case, for example, for a power function and in the case of the functions $(\exp_2)_*$ and $(\cosh -1)_*$ . In such a case, the dual couple is a couple of reflexive Banach spaces, and bounded functions are a dense set. I will return to this important topic below.

The spaces corresponding to power case (4) coincide with the ordinary Lebesgue spaces. The norm are related by

$$
\left\| f \right\| _ {L _ {\Phi_ {\alpha}} (\mu)} = \alpha^ {1 / \alpha} \left\| f \right\| _ {L ^ {\alpha} (\mu)}.
$$

With reference to our examples (5) and (6), we see that $\exp_2$ and $(\cosh -1)$ are equivalent. They both are eventually dominated by $\mathrm{gauss}_2$ (7) and eventually dominate all powers (4). The cases (5) and (6) provide isomorphic B-spaces $L_{(\cosh -1)}(\mu)\leftrightarrow L_{\exp_2}(\mu)$ which are of special interest for us as they provide the model spaces for our non-parametric version of IG, see section 4 below.

Clearly, a function belongs to the space $L_{\cosh_2}(\mu)$ if, and only if, its moment generating function $\lambda \mapsto \int \mathrm{e}^{\lambda f}$ is finite in a neighborhood of 0. In turn, this implies that the moment generating function is analytic at 0, see [6, Ch. 2].

The same property is equivalent to a large deviation inequality, see [39, Ch. 2]. A function $f$ belongs to $L_{\cosh -1}(\mu)$ if, and only if, it is sub-exponential, that is, there exist constants $C_1, C_2 > 0$ such that

$$
\mu \big (| f | \geq t \big) \leq C _ {1} \exp \left(- C _ {2} t\right), \quad t \geq 0.
$$

Let us check the equivalence above. If $\| f\|_{L_{\cosh_2}(\mu)} = \rho$ , then $\int \mathrm{e}^{\rho^{-1}|f|}d\mu \leq 4$ . It follows that

$$
\mu \big (| f | > t \big) = \mu \left(\mathrm {e} ^ {\rho^ {- 1} | f |} > \mathrm {e} ^ {\rho^ {- 1} t}\right) \leq \left(\int \mathrm {e} ^ {\rho^ {- 1} | f |} d \mu\right) \mathrm {e} ^ {- \rho^ {- 1} t} \leq 4 \mathrm {e} ^ {- \rho^ {- 1} t}.
$$

The sub-exponential inequality holds with $C_1 = 4$ and $C_2 = \| f\|_{L_{\cosh_2}(-\mu)}^{-1}$ . Conversely, for all $\lambda >0$ ,

$$
\int \mathrm {e} ^ {\lambda f} d \mu \leq \int_ {1} ^ {\infty} \mu \left(\mathrm {e} ^ {\lambda f ^ {+}} > t\right) d t \leq C _ {1} \int_ {0} ^ {\infty} \mathrm {e} ^ {- (C _ {2} \lambda^ {- 1} - 1) s} d s.
$$

The right-hand side is finite if $\lambda < C_2$ and the same bound holds for $-f$ .

A sub-exponential random variable is of particular interest in applications because they admit an explicit exponential bound in the Law of Large Numbers. Another class of interest consists of the sub-Gaussian random variables, that is, those random variables whose square is sub-exponential.

The theory of sub-exponential random variables provides an equivalent norm for the space $L_{\cosh_2}(\mu)$ , namely the norm

$$
f \mapsto \operatorname * {s u p} _ {k} \left((2 k)! ^ {- 1} \int f ^ {2 k} d \mu\right) ^ {1 / 2 k} = \left| f \right| _ {\cosh_ {2}}.
$$

See [7] or [37]. Let us prove the equivalence. If $\| f\|_{L_{\cosh_2}(\mu)}\leq 1$ , then

$$
1 \geq \int \cosh_ {2} f d \mu \geq \frac {1}{(2 k) !} \int f ^ {2 k} d \mu \quad \text {f o r a l l} k = 1, 2, \dots ,
$$

so that $1 \geq |f|_{\cosh_2}$ . Conversely, if the latter inequality holds, then

$$
\int \cosh_ {2} (f / \sqrt {2}) d \mu = \sum_ {k = 1} ^ {\infty} \frac {1}{(2 k) !} \int f ^ {2 k} d \mu \left(\frac {1}{2}\right) ^ {k} \leq 1,
$$

so that $\| f\|_{L_{\cosh_2}(\mu)}\leq \sqrt{2}$

It is convenient to introduce a further notation. For each Young function $\Phi$ , the function $\overline{\Phi}(x) = \Phi(x^2)$ is again a Young function such that $\|f\|_{L_{\overline{\Phi}}(\mu)} \leq \lambda$ if, and only if, $\left\| |f|^2 \right\|_{L_{\Phi}(\mu)} \leq \lambda^2$ . We will denote the resulting space by $L_{\Phi}^2(\mu)$ . For example, $\mathrm{gauss}_2$ and $\overline{\cosh - 1}$ are $\prec$ -equivalent, hence the isomorphism $L_{\mathrm{gauss}_2}(\mu) \leftrightarrow L_{(\cosh - 1)}^2(\mu)$ . As an application of this notation, consider that for each increasing convex $\Phi$ it holds $\Phi(fg) \leq \Phi((f^2 + g^2)/2) \leq (\Phi(f^2) + \Phi(g^2))/2$ . It follows that when the $L_{\Phi}^2(\mu)$ -norm of $f$ and of $g$ is bounded by one, the $L_{\Phi}(\mu)$ -norm of $f$ , $g$ , and $fg$ , are all bounded by one. The space $L_{\mathrm{cosh}_2}(\mu)$ has a continuous injection in the Fréchet space $L^{\infty - 0}(\mu) = \cap_{\alpha > 1} L^\alpha(\mu)$ , which is an algebra. When we need the product, we can either assume the factor are both sub-Gaussian, or, move up the functional frawork to the intersection of the Lebesgue spaces.

Let us now discuss specific issues of the Gaussian exponential Orlicz spaces $L_{\cosh_2}(\gamma)$ , $\gamma$ the standard $n$ -variate Gaussian density. Dominated convergence does not hold in this space. The squared-norm function $f(x) = |x|^2$ belongs to the Gaussian exponential Orlicz space $L_{\cosh_2}(\gamma)$ because

$$
\int \cosh_ {2} (\lambda f (x)) \gamma (x) d x <   \infty \quad \text {f o r a l l} \quad \lambda <   1 / 2.
$$

The sequence $f_{N}(x) = f(x)(|x|\leq N)$ converges to $f$ point-wise and in all $L^{\alpha}(\gamma)$ , $1\leq \alpha < \infty$ . However, the convergence does not hold in the Gaussian exponential Orlicz space. In fact, for all $\lambda \geq 1 / 2$ ,

$$
\int \cosh_ {2} (\lambda (f (x) - f _ {N} (x))) \gamma (x) d x = \int_ {| x | > N} \cosh_ {2} (\lambda f (x)) \gamma (x) d x = \infty ,
$$

but convergence would imply

$$
\lim  _ {N \rightarrow \infty} \sup  _ {\lambda > 0} \int \cosh_ {2} \left(\lambda \left(f (x) - f _ {N} (x)\right)\right) \gamma (x) d x \leq 1 \quad \text {f o r a l l} \lambda > 0.
$$

The closure in $L_{\cosh_2}(\gamma)$ of the vector space of bounded functions is called Orlicz class and it is denoted by $M_{\cosh_2}(\gamma)$ . One can prove that $f \in M_{\cosh_2}(\gamma)$ if, and only if, the moment generating function $\lambda \mapsto \int \mathrm{e}^{\lambda f(x)} \gamma(x) dx$ is finite for all $\lambda$ , see [29]. An example is $f(x) = x$ . Bounded convergence holds in the Orlicz

class. Assume $f \in M_{\cosh_2}(\gamma)$ and consider the sequence $f_N(x) = (|x| \leq N)f(x)$ . Now,

$$
\int \cosh_ {2} (\lambda (f (x) - f _ {N} (x)) \gamma (x) d x = \int_ {| x | \geq N} \cosh_ {2} (\lambda f (x)) \gamma (x) d z
$$

converges to 0 as $N\to \infty$

# 3. CALCULUS OF THE GAUSSIAN SPACE

I will review here a few simple facts about the analysis of the Gaussian space, the so-called Malliavin's calculus, see [19, Ch. V].

Let us denote by $C_{\mathrm{poly}}^k(\mathbb{R}^n)$ , $k = 0,1,\ldots$ , the vector space of functions which are differentiable up to order $k$ and which are bounded, together with all derivatives, by a polynomial. This class of functions is dense in $L^2(\gamma)$ . For each couple $f,g\in C_{\mathrm{poly}}^1(\mathbb{R}^n)$ , we have

$$
\int f (x) \partial_ {i} g (x) \gamma (x) d x = \int \delta_ {i} f (x) g (x) \gamma (x) d x,
$$

where the divergence operator $\delta_{i}$ is defined by $\delta_{i}f(x) = x_{i}f(x) - \partial_{i}f(x)$ . Multi-dimensional notations will be used, for example,

$$
\int \nabla f (x) \cdot \nabla g (x) \gamma (x) d x = \int f (x) \delta \cdot \nabla g (x) \gamma (x) d x, \quad f, g \in C _ {\text {p o l y}} ^ {2} \left(\mathbb {R} ^ {n}\right),
$$

with $\delta \cdot \nabla g(x) = x\cdot \nabla g(x) - \Delta g(x)$

For example, in this notation, the Hyvarinen divergence of eq. (2) with $P = p \cdot \gamma$ , $Q = q \cdot \gamma$ , and $p, q \in C_{\mathrm{poly}}^2(\mathbb{R}^n)$ , becomes

$$
\frac {1}{2} \int | \nabla \log p (x) - \nabla \log q (x) | ^ {2} p (x) \gamma (x) d x,
$$

while the Otto's inner product of eq. (3) becomes, with $P = p \cdot \gamma$ and $f, g, p \in C_{\mathrm{poly}}^2(\mathbb{R}^n)$ , gives

$$
\int \nabla f (x) \cdot \nabla g (x) p (x) \gamma (x) d x = \int f (x) \delta \cdot \nabla (g (x) p (x)) \gamma (x) d x.
$$

Hermite polynomials $H_{\alpha} = \delta^{\alpha}1$ provide an orthogonal basis for $L^{2}(\gamma)$ such that $\partial_i H_\alpha = \alpha_i H_{\alpha - e_i}$ . Fourier expansion in Hermite polynomials provides proof of the closure of both operator $\partial_i$ and $\delta_i$ on a domain which is an Hilbert subspace of $L^{2}(\gamma)$ . Moreover, the closure of $\partial_i$ is the translation operator's infinitesimal generator.

# 4. EXPONENTIAL STATISTICAL BUNDLE

In this section, I will very briefly review and slightly generalize my construction of the statistical manifold as a Banach manifold modeled on the exponential Orlicz space $L_{\cosh_2}(\gamma)$ . For a detailed presentation, see [27] and [29]. The general set-up is specialized to the Gaussian space.

The support of the manifold is the maximal exponential model $\mathcal{E}(\gamma)$ consisting of probability densities on $(\mathbb{R}^n,\gamma)$ of the form

$$
q = \exp \left(u - K _ {1} (u)\right), \quad u \in B _ {1} = L _ {\cosh_ {2}} (\gamma) \cap \left\{u \middle | \int u (x) \gamma (x) d x = 0 \right\}.
$$

The quantity $K_{1}(u) = \log \int \mathrm{e}^{u(x)}\gamma (x)dx$ is the unique normalising constant (log-partition function) of $\mathrm{e}^u$ and is assumed to be finite. A further restriction is needed

to avoid the border of the set $\{K_1(u) < \infty\}$ . We can easily prove that the mapping $K_1 \colon L_{\cosh_2}(\gamma) \to \mathbb{R}$ is convex and that the topological interior of its proper domain in non-empty because it contains the open unit ball of $B_1$ . We restrict the model to all $u$ in such domain. The mapping

$$
s _ {1} \colon \mathcal {E} (\gamma) \ni q \mapsto u = \log q - \mathbb {E} _ {\gamma} [ \log q ] \in B _ {1}
$$

provides a global chart to the manifold. If we chose to express the velocity of a curve $t \mapsto \mathcal{E}(\gamma)$ by the Fishers score $\frac{d}{dt} \log q(t)$ , then the tangent bundle of the manifold is expressed by the statistical bundle $S\mathcal{E}(\gamma)$ consisting of all the couples $(q, v)$ such that $q$ is a density of the maximal exponential model and $v$ is a $q$ -centered random variable in the exponential Orlicz space.

The following statement is crucial to prove consistency in infinite dimensions. It shows that the statistical bundle fibers are isomorphic as Banach spaces.

For all $p, q \in \mathcal{E}(\gamma)$ it holds $q = \mathrm{e}^{u - K_p(u)} \cdot p$ , where $u \in L_{(\cosh - 1)}(\gamma)$ , $\mathbb{E}_p[u] = 0$ , and $u$ belongs to the interior of the proper domain of the convex function $K_p$ . This property is equivalent to any of the following:

(1) $p$ and $q$ are connected by an open exponential arc;   
(2) $L_{\cosh_2}(p) = L_{\cosh_2}(q)$ and the norms are equivalent;   
(3) $p / q\in \cup_{a > 1}L^{a}(q)$ and $q / p\in \cup_{a > 1}L^{a}(p)$

See [35, 36] for a detailed proof. The following argument is a generalization of the proof of item $1 \Rightarrow$ item 2. Let $F$ be logarithmically convex on $\mathbb{R}$ and such that $\Phi = F - 1$ is a Young function. For example, the assumption holds for both $F(x) = \cosh x$ and $F(x) = \mathrm{e}^{x^2 /2}$ . For all real $A$ and $B$ , the function

$$
\mathbb {R} ^ {2} \ni (\lambda , t) \mapsto F (\lambda A) \mathrm {e} ^ {t B} = \exp \left(\log F (\lambda A) + t B\right)
$$

is convex and so is

$$
C (\lambda , t) = \int F (\lambda f (x)) \mathrm {e} ^ {t u (x)} \gamma (x) d x,
$$

where $f \in L_{\Phi}(\gamma)$ with and $u \in L_{\cosh_2}(\gamma)$ with $\int u(x) \, \gamma(x) dx = 0$ . Without restriction of generality, assume $\|f\|_{L_{\Phi}(\gamma)} = 1$ . Let us derive two marginal inequalities. First, for $t = 0$ , the definition of Luxemburg norm gives

$$
C (\lambda , 0) = \int F (\lambda f) \gamma (x) d x \leq 2, - 1 \leq \lambda \leq 1.
$$

Second, for $\lambda = 0$ , consider $K_{1}(tu) = \log \int \mathrm{e}^{tu}\gamma (x)dx$ , where $t$ belongs to an open interval $I$ containing $[0,1]$ and such that $K_{1}(tu) < +\infty$ . It follows that

$$
C (0, t) = \int \mathrm {e} ^ {t u} \gamma (x) d x = \mathrm {e} ^ {K _ {1} (t u)} <   + \infty .
$$

Choose a $t > 1$ in $I$ and consider the convex combination

$$
\left(\frac {t - 1}{t}, 1\right) = \frac {t - 1}{t} (1, 0) + \frac {1}{t} (0, t)
$$

and the inequality

$$
C \left(\frac {t - 1}{t}, 1\right) \leq \frac {t - 1}{t} C (1, 0) + \frac {1}{t} C (0, t) \leq 2 \frac {t - 1}{t} + \frac {1}{t} \mathrm {e} ^ {K _ {1} (t u)}.
$$

Now,

$$
\begin{array}{l} \int \Phi \left(\frac {t - 1}{t} f (x)\right) \mathrm {e} ^ {u (x) - K _ {1} (u)} \gamma (x) d x = \\ \int F \left(\frac {t - 1}{t} f (x)\right) \mathrm {e} ^ {u (x) - K _ {1} (u)} \gamma (x) d x - 1 = \\ \mathrm {e} ^ {- K _ {1} (u)} C \left(\frac {t - 1}{t}, 1\right) - 1 \leq \mathrm {e} ^ {- K _ {1} (u)} \left(2 \frac {t - 1}{t} + \frac {1}{t} \mathrm {e} ^ {K _ {1} (t u)}\right) - 1 \\ \end{array}
$$

As the right-hand-side is finite, we have proved that $f \in L_{\Phi}(p)$ for $p = \mathrm{e}^{u - K_1(u)}$ . Conversely, a similar argument shows the other implication. We have proved that all Orlicz spaces $L_{\Phi}(p), p \in \mathcal{E}(\gamma)$ are equal. In turn, equality of spaces implies the equivalence norms. It is possible to derive explicit bounds by choosing a $t$ such that the right-hand-side is smaller or equal to 1, see [37].

# 5. GAUSSIAN ORLICZ-SOBOLEV SPACES

In this final section, I plan to extend the exponential statistical bundle's construction to allow for differentiable densities in the Gaussian space. Namely, I suggest a model with sub-exponential random variables of the Gaussian space whose weak derivatives are sub-Gaussian random variables. The presentation focuses on functional analytic properties, see [1] and [5] as a general reference.

As a model of the statistical manifold, let us define the function space

$$
\left. W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (\gamma) = \left\{f \in L _ {\cosh_ {2}} ^ {1} (\gamma) \mid \partial_ {i} f \in L _ {\cosh_ {2}} ^ {2} (\gamma), i = 1, \dots , n \right\}, \right. \tag {8}
$$

where the weak partial derivative $\partial_j f$ exists if

$$
\left\langle \partial_ {j} f, \phi \right\rangle_ {\gamma} = \left\langle f, \delta_ {j} \phi \right\rangle_ {\gamma} \quad \text {f o r a l l} \quad \phi \in C _ {0} ^ {1} \left(\mathbb {R} ^ {n}\right).
$$

The above definition of weak derivative coincides this the usual definition of derivative in the sense of Schwartz distributions because $\phi \leftrightarrow \phi \cdot \gamma$ is a bijection of $C_0^\infty (\mathbb{R}^n)$ and

$$
\left\langle f, \delta_ {i} \phi \right\rangle_ {\gamma} = - \int f (x) \frac {\partial}{\partial x _ {i}} \left(\phi (x) \gamma (x)\right) d x.
$$

Weak derivatives do not provide tools for non-linear computations. Hence we want to recall the relation between translation and weak derivative, the weak version of Calculus's fundamental theorem. Let be given a locally integrable real mapping $G \in L_{\mathrm{loc}}^1(\mathbb{R})$ , and assume there exists a locally integrable function $G'$ which is the weak derivative of $G$ , that is,

$$
\int G (x) \phi^ {\prime} (x) d x = - \int G ^ {\prime} (x) \phi (x) d x, \quad \phi \in C _ {0} ^ {\infty} (\mathbb {R}). \tag {9}
$$

Define the translation $\tau_h G$ , $h \in \mathbb{R}$ , by $t_h G(x) = G(x - h)$ , $h \in \mathbb{R}$ . It follows immediately that $\tau_h G \in L_{\mathrm{loc}}^1(\mathbb{R})$ and

$$
\begin{array}{l} \int (\tau_ {- h} G (x) - G (x)) \phi (x) d x = \int G (x + h) \phi (x) d x - \int G (x) \phi (x) d x \\ = \int G (x) (\phi (x - h) - \phi (x)) d x \\ = \int G (x) \phi (x - s h) | _ {s = 0} ^ {s = 1} d x \\ = - h \int G (x) \int_ {0} ^ {1} \phi^ {\prime} (x - s h) d s d x \\ = - h \int_ {0} ^ {1} \int G (x) \phi^ {\prime} (x - s h) d x d s \\ = h \int_ {0} ^ {1} \int G ^ {\prime} (x) \phi^ {\prime} (x - s h) d x d s = \\ = h \int_ {0} ^ {1} \int G ^ {\prime} (x + s h) \phi^ {\prime} (x) d x d s = \\ = \int \left(h \int_ {0} ^ {1} G ^ {\prime} (x + s h) d s\right) \phi (x) d x \\ \end{array}
$$

As $\phi$ is any function in $C_0^\infty (\mathbb{R})$ , we have proved that

$$
\tau_ {- h} G - G = h \int_ {0} ^ {1} \tau_ {- s h} G ^ {\prime} d s = h G ^ {\prime} + h \int_ {0} ^ {1} \left(\tau_ {- s h} G ^ {\prime} - G ^ {\prime}\right) d s \tag {10}
$$

in $L_{\mathrm{loc}}^{1}(\mathbb{R})$ . In particular, if $G'$ is bounded by a constant $K$ , then $G$ is almost surely $K$ -Lipschitz, $|G(x - h) - G(x)| \leq K|h|$ .

Conversely, if eq. (10) holds, then eq. (9) holds, see, for example, [5, Lemma 8.1-2].

The argument above extends to $n$ -variate functions $f \in W_{\mathrm{loc}}^{1,1}(\mathbb{R}^n)$ , that is, $f, \partial_i f \in L_{\mathrm{loc}}^1 (\mathbb{R}^n)$ , $i = 1,\dots ,n$ , by considering, for each $h \in \mathbb{R}^n$ , the univariate function $t \mapsto \tau_{th} f$ defined by $\tau_{th} f(x) = f(x - th)$ . We obtain

$$
\tau_ {- t h} f - f = t \nabla f \cdot h + t \int_ {0} ^ {1} \left(\tau_ {- s t h} \nabla f - \nabla f\right) \cdot h d s, \tag {11}
$$

where the equality holds in $L_{\mathrm{loc}}^{1}(\mathbb{R}^{n})$ . The same equality holds in all function space whose elements are locally integrable.

The result about the functional differentiability of translations is the following. For all $f \in W^{1}L_{\cosh_{2}}^{1,2}(\gamma)$ the following first increment equation holds,

$$
\left(\tau_ {- t h} f - f\right) - t \nabla f \cdot h = t \int_ {0} ^ {1} \left(\tau_ {- s t h} \nabla f - \nabla f\right) \cdot h d s,
$$

and differentiability holds in $L^{\infty - 0}(\gamma) = \cap_{\alpha > 1} L^{\alpha}(\gamma)$ . In fact, the translations are continuous in all $L^{\alpha}(\gamma)$ .

It is possible to extend the previous result to a property of the derivative of the composite function $G \circ f$ . The increment of the composition expands as

$$
G (f (x + t h)) - G (f (x)) = G (f (x) + (f (x + t h) - f (x)) = \tag {12}
$$

$$
(f (x + t h) - f (x)) G ^ {\prime} (f (x)) +
$$

$$
\left(f (x + t h) - f (x)\right) \int_ {0} ^ {1} \left(G ^ {\prime} (f (x) + s (f (x + t h) - f (x))) - G ^ {\prime} (f (x))\right) d s,
$$

and the weak derivative of the composite function exists if $G'$ is bounded and $f \in W^{1}L_{\cosh_2}^{1,2}(\gamma)$ . However, differentiability holds in $L^{\infty - 0}(\gamma)$ .

An interesting example of application is the neuron of a neural network [10, Ch. 18]. If $f_{1},\ldots ,f_{k}\in W^{1}L_{\cosh_{2}}^{1,2}(\gamma)$ , $G$ is an activation function with linear growth, for example, the linear rectifier $G(x) = x^{+}$ , and $a_{i},w_{ij},b_{i}$ are given constants, then

$$
\sum_ {i = 1} ^ {h} a _ {i} G \left(\sum_ {j = 1} ^ {k} w _ {i j} f _ {j} - b _ {i}\right) \in W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (\gamma).
$$

A crucial feature of the space defined in eq. (8) is the fact that each element of $W^{1}L_{\cosh_{2}}^{1,2}(\gamma)$ has a continuous version. The embedding

$$
L _ {\cosh_ {2}} ^ {1} (\gamma), L _ {\cosh_ {2}} ^ {2} (\gamma) \subset \cap_ {\alpha \geq 1} L ^ {\alpha} (\gamma)
$$

allows to use the standard Sobolev inequalities to our case. $W_{\mathrm{loc}}^{1,\alpha}(\mathbb{R}^n)$ denotes the space of functions whose restriction to each open ball $B_{\rho} = \{x\in \mathbb{R}^n ||x| < \rho \}$ is $\alpha$ -integrable, together with all weak partial derivatives. $C^\lambda (\overline{B}_\rho)$ denotes $\lambda$ -Hölder functions on the closed ball.

(1) The following restriction and embedding hold true and are continuous,

$$
W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (\gamma) \rightarrow W ^ {1, \alpha} (\overline {{B}} _ {\rho}) \subset C ^ {\lambda} (\overline {{B}} _ {\rho}), \quad \rho > 0, \quad 0 <   \lambda <   1.
$$

(2) The following inclusions hold true and are continuous:

$$
W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (\gamma) \subset \cap_ {\alpha \geq 1} W _ {\mathrm {l o c}} ^ {1, \alpha} \cap L _ {\cosh_ {2}} ^ {1} (\gamma) \subset C (\mathbb {R} ^ {n}) \cap L _ {\cosh_ {2}} ^ {1} (\gamma),
$$

where the space of continuous functions $C(\mathbb{R})$ is endowed with the uniform convergence on compact sets.

The embedding are easily verified. If $f \in L_{\cosh^{-1}}^{1}(\gamma)$ , then, for all $k \in \mathbb{N}$ , the inequalities $x^{2k} / (2k)! \leq \cosh_2(x)$ and $(2\pi)^{-n/2}\mathrm{e}^{-\rho^2/2} \leq \gamma(x)$ for $x \in B_\rho$ imply the inequality

$$
\begin{array}{l} \frac {(2 \pi) ^ {- n / 2} \mathrm {e} ^ {- \rho^ {2} / 2}}{(2 k) !} \int_ {B _ {\rho}} \left(\frac {f (x)}{\| f \| _ {L _ {\cosh_ {2}} ^ {1} (\gamma)}}\right) ^ {2 k} d x \leq \\ \int \cosh_ {2} \left(\frac {f (x)}{\| f \| _ {L _ {\cosh_ {2}} ^ {1} (\gamma)}}\right) \gamma (x) d x \leq 1, \\ \end{array}
$$

so that

$$
\| f \| _ {L ^ {2 k} (B _ {\rho})} ^ {2 k} \leq (2 \pi) ^ {n / 2} (2 k)! \mathrm {e} ^ {\rho^ {2} / 2} \| f \| _ {L _ {\cosh_ {2}} ^ {1} (\gamma)}.
$$

A similar argument applies to the weak partial derivatives. Now we can use the Sobolev embedding theorem, see [1, Th. 4.12].

Let us conclude by explicitly reviewing the main properties of our space.

(1) The space $W^{1}L_{\cosh_{2}}^{1,2}(\gamma)$ contains the constants and all polynomial up to order 2.   
(2) Each element has a continuous version.   
(3) If $G: \mathbb{R} \to \mathbb{R}$ is the primitive of a bounded function, then $G \circ f \in W^{1}L_{\cosh_{2}}^{1,2}(\gamma)$ .

(4) $\min (f,g),\max (f,g)\in W^1 L_{\cosh_2}^{1,2}(\gamma).$

Moreover, our space is a Banach space: The mapping

$$
W ^ {1} L _ {\Phi} ^ {1, 2} (\gamma) \ni f \mapsto \| f \| _ {L _ {\Phi} ^ {1} (\gamma)} + \sum_ {i = 1} ^ {n} \| \partial_ {i} f \| _ {L _ {\Phi} ^ {2} (\gamma)}
$$

is a complete norm and thus defines a Banach space. The argument is a standard one in Functional Analysis. The weak gradient $\nabla$ is a closed operator from $L_{\Phi}^{1}(\gamma) \to (L_{\Phi}^{2}(\gamma))^{n}$ , that is, the graph of $\nabla$ is closed in $L_{\Phi}^{1}(\gamma) \times (L_{\Phi}^{2}(\gamma))^{n}$ . In fact, given a converging sequence in the graph, say $f_{n} \to f$ and $\partial_{i}f \to f^{i}$ , it holds

$$
\left\langle \partial_ {i} f, \phi \right\rangle_ {\gamma} = \left\langle f, \delta_ {i} \phi \right\rangle_ {\gamma} = \lim _ {n} \left\langle f _ {n}, \delta_ {i} \phi \right\rangle_ {\gamma} = \lim _ {n} \left\langle \partial_ {i} f, \phi \right\rangle_ {\gamma} = \left\langle f ^ {i}, \phi \right\rangle_ {\gamma}.
$$

The identification of the space $W^{1}L_{\Phi}^{1,2}(\gamma)$ with the graph of $\nabla$ provides a complete norm.

Finally, all exponential Orlicz spaces are isomorphic in a maximal exponential model. This, in turn implies the isomorphism

$$
W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (\gamma) \leftrightarrow W ^ {1} L _ {\cosh_ {2}} ^ {1, 2} (p \cdot \gamma) \quad p \in \mathcal {E} (\gamma) .
$$

It follows that this space is suitable as a model of the fibers of a statistical bundle.

# 6. SELECTED BIBLIOGRAPHY

General monograph on IG are [13], [3], and [4]. The type of analytic framework I suggest to use in IG is that of Banach manifolds as in [15]. A first version of this project has been developed in [34, 11, 33, 8]. In a series of papers [26], [17], [28], and [30], we have explored a version of the non-parametric Information Geometry (IG) for smooth densities on $\mathbb{R}^n$ . Especially, we have considered the IG associated to Orlicz spaces on the Gaussian space. The analysis of the Gaussian space is discussed, for example, in [20], and [24].

This set-up provides a way to construct a statistical manifold modelled on functional spaces of smooth densities, but other modelling options are in fact available, for example the global analysis methods of [14] and the approach based on deformed exponentials [22]. For the two examples involving derivatives, see [12], [17], [25], and [18].

We have worked with a restricted type of Young functions. See the more general cases in [21, Ch. II] and [1, Ch. VII]. There is a large literature about sub-exponential random variables, for example, [7], [38], [39]. Application to IG is discussed in [37]. The need to control the product of two random variables in $L_{(\cosh - 1)}(\mu)$ appears, notably, in the study of the covariant derivatives of the statistical bundle, see [11], [18], [31], and [9].

See [27], and [30] for all details about the construction of the statistical bundle that are missing here. In particular the isomorphism of fibers is discussed in detail in [35] and [36]. For Malliavin's calculus, see [20] and [19]. General references about the functional background used in the construction of the Gaussian Orlicz-Sobolev space are [1], and [5].

acknowledgements. The author acknowledges the support by de Castro Statistics, Collegio Carlo Alberto, Turin, Italy. He is a member of GNAMPA-INDAM. The author thanks an anonymous reviewer and L. Malagò for their helpful comments.

# REFERENCES

[1] Adams, R.A., Fournier, J.J.F.: Sobolev spaces, Pure and Applied Mathematics (Amsterdam), vol. 140. Elsevier/Academic Press, Amsterdam, second edn. (2003)   
[2] Amari, S.i.: Information geometry and its applications, Applied Mathematical Sciences, vol. 194. Springer, [Tokyo] (2016), https://doi.org/10.1007/978-4-431-55978-8   
[3] Amari, S., Nagaoka, H.: Methods of information geometry. American Mathematical Society (2000), translated from the 1993 Japanese original by Daishi Harada   
[4] Ay, N., Jost, J., Lé, H.V., Schwachhöfer, L.: Information geometry, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics], vol. 64. Springer, Cham (2017). https://doi.org/10.1007/978-3-319-56478-4, https://doi.org/10.1007/978-3-319-56478-4   
[5] Brezis, H.: Functional analysis, Sobolev spaces and partial differential equations. Universitext, Springer, New York (2011)   
[6] Brown, L.D.: Fundamentals of statistical exponential families with applications in statistical decision theory. No. 9 in IMS Lecture Notes. Monograph Series, Institute of Mathematical Statistics (1986)   
[7] Buldygin, V.V., Kozachenko, Y.V.: Metric characterization of random variables and random processes, Translations of Mathematical Monographs, vol. 188. American Mathematical Society, Providence, RI (2000), translated from the 1998 Russian original by V. Zaiats   
[8] Cena, A.: Geometric structures on the non-parametric statistical manifold. Ph.D. thesis, Università degli Studi di Milano (2002)   
[9] Chirco, G., Malagò, L., Pistone, G.: Lagrangian and hamiltonian mechanics for probabilities on the statistical manifold (2020), arXiv:2009.09431   
[10] Efron, B., Hastie, T.: Computer age statistical inference, Institute of Mathematical Statistics (IMS) Monographs, vol. 5. Cambridge University Press, New York (2016), https://doi.org/10.1017/CB09781316576533, algorithms, evidence, and data science   
[11] Gibilisco, P., Pistone, G.: Connections on non-parametric statistical manifolds by Orlicz space geometry. IDAQP 1(2), 325-347 (1998)   
[12] Hyvarinen, A.: Estimation of non-normalized statistical models by score matching. J. Mach. Learn. Res. 6, 695-709 (2005)   
[13] Kass, R.E., Vos, P.W.: Geometrical foundations of asymptotic inference. Wiley Series in Probability and Statistics: Probability and Statistics, John Wiley & Sons, Inc., New York (1997). https://doi.org/10.1002/9781118165980, http://dx.doi.org/10.1002/9781118165980, a Wiley-Interscience Publication   
[14] Kriegl, A., Michor, P.W.: The convenient setting of global analysis, Mathematical Surveys and Monographs, vol. 53. American Mathematical Society, Providence, RI (1997). https://doi.org/10.1090/surv/053, https://doi.org/10.1090/surv/053   
[15] Lang, S.: Differential and Riemannian manifolds, Graduate Texts in Mathematics, vol. 160. Springer-Verlag, third edn. (1995)   
[16] Ledoux, M.: The concentration of measure phenomenon, Mathematical Surveys and Monographs, vol. 89. American Mathematical Society, Providence, RI (2001). https://doi.org/10.1090/surv/089, https://doi.org/10.1090/surv/089   
[17] Lods, B., Pistone, G.: Information geometry formalism for the spatially homogeneous Boltzmann equation. Entropy 17(6), 4323-4363 (2015)   
[18] Lott, J.: Some geometric calculations on Wasserstein space. Comm. Math. Phys. 277(2), 423-437 (2008). https://doi.org/10.1007/s00220-007-0367-3, https://doi.org/10.1007/s00220-007-0367-3   
[19] Malliavin, P.: Integration and probability, Graduate Texts in Mathematics, vol. 157. Springer-Verlag (1995), with the collaboration of Hélène Airault, Leslie Kay and Gérard Letac, Edited and translated from the French by Kay, With a foreword by Mark Pinsky   
[20] Malliavin, P.: Stochastic analysis, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 313. Springer-Verlag (1997)   
[21] Musielak, J.: Orlicz spaces and modular spaces, Lecture Notes in Mathematics, vol. 1034. Springer-Verlag (1983)

[22] Newton, N.J.: Sobolev statistical manifolds and exponential models. In: Geometric science of information, Lecture Notes in Comput. Sci., vol. 11712, pp. 443-452. Springer, Cham (2019)   
[23] Nielsen, F.: An elementary introduction to information geometry. Entropy 22(10) (2020). https://doi.org/10.3390/e22101100, https://www.mdpi.com/1099-4300/22/10/1100   
[24] Nourdin, I., Peccati, G.: Normal approximations with Malliavin calculus, Cambridge Tracts in Mathematics, vol. 192. Cambridge University Press, Cambridge (2012). https://doi.org/10.1017/CBO9781139084659, http://dx.doi.org/10.1017/CBO9781139084659, from Stein's method to universality   
[25] Otto, F.: The geometry of dissipative evolution equations: the porous medium equation. Comm. Partial Differential Equations 26(1-2), 101-174 (2001), ../publications/Riemann.ps   
[26] Pistone, G.: Examples of the application of nonparametric information geometry to statistical physics. Entropy 15(10), 4042-4065 (2013). https://doi.org/10.3390/e15104042, http://dx.doi.org/10.3390/e15104042   
[27] Pistone, G.: Nonparametric information geometry. In: Nielsen, F., Barbaresco, F. (eds.) Geometric science of information, Lecture Notes in Comput. Sci., vol. 8085, pp. 5-36. Springer, Heidelberg (2013), first International Conference, GSI 2013 Paris, France, August 28-30, 2013 Proceedings   
[28] Pistone, G.: Translations in the exponential Orlicz space with Gaussian weight. In: Nielsen, F., Barbaresco, F. (eds.) Geometric Science of Information. pp. 569-576. No. 10589 in LNCS, Springer (2017), third International Conference, GSI 2017, Paris, France, November 7-9, 2017, Proceedings   
[29] Pistone, G.: Information geometry of the Gaussian space. In: Information geometry and its applications, Springer Proc. Math. Stat., vol. 252, pp. 119-155. Springer, Cham (2018)   
[30] Pistone, G.: Information geometry of the Gaussian space. In: Information geometry and its applications, Springer Proc. Math. Stat., vol. 252, pp. 119-155. Springer, Cham (2018)   
[31] Pistone, G.: Lagrangian function on the finite state space statistical bundle. Entropy 20(2), 139 (2018). https://doi.org/10.3390/e20020139, http://www.mdpi.com/1099-4300/20/2/139   
[32] Pistone, G.: Information geometry of the probability simplex: A short course. Nonlinear Phenomena in Complex Systems 23(2), 221-242 (2020), arXiv:1911.01876   
[33] Pistone, G., Rogantin, M.: The exponential statistical manifold: mean parameters, orthogonality and space transformations. Bernoulli 5(4), 721-760 (August 1999)   
[34] Pistone, G., Sempi, C.: An infinite-dimensional geometric structure on the space of all the probability measures equivalent to a given one. Ann. Statist. 23(5), 1543-1561 (October 1995)   
[35] Santacroce, M., Siri, P., Trivellato, B.: New results on mixture and exponential models by Orlicz spaces. Bernoulli 22(3), 1431-1447 (2016). https://doi.org/10.3150/15-BEJ698, https://doi.org/10.3150/15-BEJ698   
[36] Santacroce, M., Siri, P., Trivellato, B.: Exponential models by Orlicz spaces and applications. J. Appl. Probab. 55(3), 682-700 (2018). https://doi.org/10.1017/jpr.2018.45, https://doi.org/10.1017/jpr.2018.45   
[37] Siri, P., Trivellato, B.: Robust concentration inequalities in maximal exponential models. Statist. Probab. Lett. 170, 109001 (2021). https://doi.org/10.1016/j.spl.2020.109001, https://doi.org/10.1016/j.spl.2020.109001   
[38] Vershynin, R.: High-dimensional probability: an introduction with applications in data science, Cambridge Series in Statistical and Probabilistic Mathematics, vol. 47. Cambridge University Press, Cambridge (2018). https://doi.org/10.1017/9781108231596, https://doi.org/10.1017/9781108231596, with a foreword by Sara van de Geer   
[39] Wainwright, M.J.: High-dimensional statistics: a non-asymptotic viewpoint. Cambridge Series in Statistical and Probabilistic Mathematics, Cambridge University Press, Cambridge (2019). https://doi.org/10.1017/9781108627771

DE CASTRO STATISTICS, COLLEGIO CARLO ALBERTO, TORINO, ITALY  
Email address: giovanni.pistone@carloalberto.org  
URL: https://www.giannidiorestino.it