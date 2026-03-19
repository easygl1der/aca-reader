# Quantum Orlicz Spaces in Information Geometry

R.F. Streater

Dept of Mathematics

King's College London

Strand, WC2R 2LS

9 June 2004

# Abstract

Let $H_0$ be a selfadjoint operator such that $\mathrm{Tr}e^{-\beta H_0}$ is of trace class for some $\beta < 1$ , and let $\mathcal{X}_{\epsilon}$ denote the set of $\epsilon$ -bounded forms, i.e. $\| (H_0 + C)^{-1 / 2 - \epsilon}X(H_0 + C)^{-1 / 2 + \epsilon}\| < C$ for some $C > 0$ . Let $\mathcal{X} \coloneqq \operatorname{Span} \cup_{\epsilon \in (0,1 / 2]} \mathcal{X}_{\epsilon}$ . Let $\mathcal{M}$ denote the underlying set of the quantum information manifold of states of the form $\rho_{X} = e^{-H_{0} - X - \psi_{X}}$ , $X \in \mathcal{X}$ . We show that if $\mathrm{Tr}e^{-H_0} = 1$ ,

1. the map $\Phi$

$$
\Phi (X) = \frac {1}{2} \operatorname {T r} \left(e ^ {- H _ {0} + X} + e ^ {- H _ {0} - X}\right) - 1
$$

is a quantum Young function defined on $\mathcal{X}$

2. The Orlicz space defined by $\Phi$ is the tangent space of $\mathcal{M}$ at $\rho_0$ ; its affine structure is defined by the $(+1)$ -connection of Amari   
3. The subset of a 'hood of $\rho_0$ , consisting of $p$ -nearby states (those $\sigma \in \mathcal{M}$ obeying $C^{-1}\rho_0^{1 + p} \leq \sigma \leq C\rho_0^{1 - p}$ for some $C > 1$ ) admits a flat affine connection known as the $(-1)$ connection, and the span of this set is part of the cotangent space of $\mathcal{M}$ .   
4. These dual structures extend to the completions in the Luxemburg norms.

# 1 Introduction

# 1.1 The need for an Orlicz topology

Let $\mathcal{H}$ be a separable Hilbert space of infinite dimension, and $\mathcal{B}(\mathcal{H})$ the $W^{*}$ -algebra of all bounded operators on $\mathcal{H}$ . The set $\Sigma$ of all normal states can be furnished with the trace norm. However, the associated metric is not a good measure of the distance between states. For example, if $\rho_0 \in \Sigma$ has finite entropy:

$$
S \left(\rho_ {0}\right) := \operatorname {T r} \rho_ {0} \log \rho_ {0} <   \infty , \tag {1}
$$

any trace-norm 'hood of $\rho_0\in \Sigma$ contains a dense set of states of infinite entropy. These states cannot be near $\rho_0$ in any physical sense. Moreover, if $\{\rho (t),t\geq 0\}$ is the dynamics of a system, then we expect that $S(\rho (t)|\rho (0)) < \infty$ for all $t\geq 0$ , where

$$
S (\sigma | \rho) := \operatorname {T r} \rho (\log \rho - \log \sigma) \tag {2}
$$

is the relative entropy of Umegaki. This, which is related to the free energy, should be finite for physical states. We need a stronger topology, such that a 'hood of $\rho_0$ contains only

states $\rho$ for which $S(\rho|\rho_0) < \infty$ . In this paper we show that this goal can be achieved by a norm topology, by developing an analogue of the $L$ log $L$ space: the unwanted states near a given state $\rho_0$ are outside the space of finite norm. The norm is a limiting case of the Schatten cross norms on spaces of compact operators, which can be regarded as quantum version of Orlicz spaces. Orlicz spaces were first introduced into information geometry in the classical case by Pistone and Sempi [15].

# 1.2 The work of Pistone and Sempi

These authors are statisticians, who developed a theory of best estimators (of minimum variance) among all locally unbiased estimators in non-parametric estimation for classical statistical theory.

Let $(\mathcal{X},\mu)$ be a measure space, and $f$ the density of a probability measure equivalent to $\mu$ . Thus,

$$
f (x) > 0 \quad \mu \text {a l m o s t e v e r y w h e r e , a n d} \mathbf {E} _ {\mu} [ f ] := \int_ {\mathcal {X}} f (x) \mu (d x) = 1. \tag {3}
$$

Let $f_0$ be such a density; we seek a useful family of sets $N$ containing $f_0$ , designed to exclude the states of infinite entropy, and which can be taken to define neighbourhoods of $f_0$ . We then do the same for each point of $N$ , and so on, thus constructing a topological space.

Consider the class of measures of the form

$$
f = f _ {0} \exp \left\{u - \psi_ {f _ {0}} (u) \right\} \tag {4}
$$

in which $\psi$ , called the free energy, is finite, for all states of a one-parameter exponential family:

$$
\psi_ {f _ {0}} (\lambda u) := \log \mathbf {E} _ {f _ {0} \mu} \left[ e ^ {- \lambda u} \right] <   \infty \text {f o r a l l} \lambda \in [ - \epsilon , \epsilon ]. \tag {5}
$$

This implies that all moments of $u$ exist in the probability measure $\nu = \mu f_0$ , and the moment generating function is analytic in a 'hood of $\lambda = 0$ . The random variables $u$ satisfying (5) for some $\epsilon$ are said to lie in the Cramér class, after the statistician Harald Cramér.

The Cramér class of random variables was shown by Pistone and Sempi to be a Banach space, and so, to be complete, when furnished with the Luxemburg norm

$$
\left\| u \right\| _ {L} := \inf  \left\{r > 0: \mathbf {E} _ {\mu} \left[ f _ {0} \cosh \frac {u}{r} \right] - 1 \right\}. \tag {6}
$$

The map

$$
u \mapsto \exp \left\{u - \psi_ {f _ {o}} (u) \right\} f _ {0} := f _ {0} (u) \tag {7}
$$

maps the unit ball in the Cramér class into the class of probability distributions that are absolutely continuous relative to $\mu$ . The identification of $\psi$ as the free energy can be seen when we write $f_0 = \exp \{-h_o\}$ , so that $f = \exp \{-h_{o} - u - \psi_{f}(u)\}$ ; then $h_o$ appears as the 'free Hamiltonian', and $u$ as the perturbing potential, of the Gibbs state $\mu f$ . Random variables $u$ and $v$ differing by a constant give rise to the same distribution. The map (7) becomes bijective if we fix $u$ such that $\mathbf{E}_{\mu}[f_0u] = 0$ , that is, $u$ has zero mean in the measure $f_{0}\mu$ . Such a $u$ is called a score in statistics. The corresponding family of measures $\mu f_0(\lambda u)$ , for $\lambda \in [-\epsilon ,\epsilon ]$ , is called a one-parameter exponential family. Pistone and Sempi define the neighbourhood $N$ of $f_0$ to consist of all distributions in some exponential family,

as $u$ runs over the Cramér class. They add similar 'hoods for each $f \in N$ , and show that the Luxemburg norms are equivalent on overlapping 'hoods. They thus construct the information manifold $\mathcal{M}$ , which is modelled on the Banach space of functions of Cramér class; this Banach space is identified with the tangent space at any $f \in \mathcal{M}$ . The manifold is furnished with a Riemannian metric, the Fisher metric, which at $f \in \mathcal{M}$ is the second Fréchet differential of $\psi_f(u)$ . The Cramér class is a special case of an Orlicz space; we now review this.

# 1.3 Young functions and Orlicz spaces

A Young function is a convex map $\Phi : \mathbf{R} \to \mathbf{R}^{+} \cup \infty$ such that

1. $\Phi (x) = \Phi (-x)$   
2. $\Phi (0) = 0$   
3. $\lim_{x\to \infty}\Phi (x) = +\infty$

The epigraph of $\Phi$ is the set of points $\{(x,y):y\geq \Phi (x)\}$ ; it is closed and convex. Then $\Phi$ is lower semicontinuous, and $\lambda \mapsto \Phi (\lambda X)$ is continuous on any open set on which it is finite [6].

Examples

$$
\begin{array}{l} \begin{array}{r l} \Phi_ {1} (x) & := \cosh x - 1 \end{array} \\ \Phi_ {2} (x) := e ^ {| x |} - | x | - 1 \\ \Phi_ {3} (x) := \left(1 + | x |\right) \log (1 + | x |) - | x | \\ \Phi^ {p} (x) \quad := \quad | x | ^ {p} \text {d e f i n e d f o r} 1 \leq p <   \infty . \\ \end{array}
$$

Let $\Phi$ be a Young function; then its Legendre-Fenchel dual,

$$
\Phi^ {*} (y) := \sup  \left\{x y - \Phi (x) \right\} \tag {8}
$$

is also a Young function. From Legendre theory, we see that $\Phi^{**} = \Phi$ . For example, $\Phi_2 = \Phi_3^*$ , and $\Phi^p = \Phi^{q^*}$ if $p^{-1} + q^{-1} = 1$ .

Equivalence.

We say that two Young functions $\Phi$ and $\Psi$ are equivalent if there exists $0 < c < C < \infty$ and $x_0 > 0$ such that

$$
\Phi (c x) \leq \Psi (x) \leq \Phi (C x) \tag {9}
$$

for all $x \geq x_0$ . We then write $\Phi \equiv \Psi$ . The scale of $x$ is not relevant. Duality is an operation on the equivalence classes:

$$
\Phi \equiv \Psi \Longrightarrow \Phi^ {*} \equiv \Psi^ {*}. \tag {10}
$$

For example, $\Phi_1 \equiv \Phi_2$ .

The $\Delta_{2}$ -class.

We say that a Young function satisfies the $\Delta_2$ -condition iff there exists $\kappa > 0$ and $x_0 > 0$ such that

$$
\Phi (2 x) \leq \kappa \Phi (x) \text {f o r} x \geq x _ {0}. \tag {11}
$$

For example, $\Phi^p$ and $\Phi_3$ satisfy $\Delta_2$ , but not $\Phi_1$ or $\Phi_2$ .

The Orlicz class and the Orlicz space

Let $(\Omega, \mathcal{B}, \nu)$ be a measure space obeying some mild conditions, and let $\Phi$ be a Young function. The Orlicz class defined by $(\Omega, \mathcal{B}, \nu)$ and $\Phi$ is the set $\hat{L}^{\Phi}(\nu)$ of real-valued measurable functions $u$ on $\Omega$ obeying

$$
\int_ {\Omega} \Phi (u (x)) \nu (d x) <   \infty . \tag {12}
$$

It is a convex space of random variables, and is a vector space iff $\Phi \in \Delta_2$ . The Orlicz space associated with $\Phi$ and $\nu$ is

$$
L ^ {\Phi} := \left\{u: \Omega \rightarrow \mathbf {R}, \text {m e a s u r a b l e ,} \int_ {\Omega} \Phi (\alpha u (x)) \nu (d x) <   \infty \text {f o r s o m e} \alpha > 0 \right\} \tag {13}
$$

It is a vector space of random variables, and is the span of the Orlicz class. Up to sets of measure zero, $L^{\Phi}$ is a Banach space when furnished with the Orlicz norm

$$
\left\| u \right\| _ {\Phi} := \sup  _ {v} \left\{\int | u v | d \nu : v \in L ^ {\Phi^ {*}}, \int \Phi^ {*} (v (x)) d \nu \leq 1 \right\}, \tag {14}
$$

or with the equivalent gauge norm, also known as a Luxemburg norm, for any $a > 0$ :

$$
\left\| u \right\| _ {L, a} := \inf  \left\{r > 0: \int \Phi (r ^ {- 1} u (x)) \nu (d x) \right\} <   a \}. \tag {15}
$$

By the Luxemburg norm, denoted $\| u\| _L$ we shall mean the case when $a = 1$ . Equivalent Young functions give equivalent norms, and $L^{\Phi}$ is separable iff $\Phi \in \Delta_2$ .

Analogue of Hölder's inequality

We have the inequality

$$
\int | u v | \nu (d x) \leq 2 \| u \| _ {L} \| v \| _ {L}. \tag {16}
$$

This leads to

$$
L ^ {\Phi} \subseteq \left(L ^ {\Phi^ {*}}\right) ^ {*}.
$$

Examples. For $\Phi^p (x)\coloneqq |x|^p$ , the Orlicz space is the Lebesgue space $L^p$ , and the dual Orlicz space is $L^q$ , where $p^{-1} + q^{-1} = 1$ . For $\Phi_1$ we get a non-separable space, sometimes called the Zygmund space when $\Omega = \mathbf{R}$ . It is the dual of $L^{\Phi_3}$ , also known as the $L\log L$ space of distributions of finite differential entropy.

See [16, 9] for classical Orlicz theory.

# Squeezing in logarithms

When $\nu$ is discrete with countable support, the Orlicz spaces associated with $\Phi^p$ are the $p$ -summable sequences $\ell^p$ , $1 \leq p \leq \infty$ . These form a nested family of Banach spaces, with $\ell^1$ the smallest and $\ell^\infty$ the largest. However, this is not the best way to look at Orlicz spaces. Legendre transforms come into their own in the context of a manifold, as a transform between the tangent space and the cotangent space at each point. There is only one manifold, but many coordinatizations. For the information manifold $\mathcal{M}$ of Pistone and Sempi, the points of the manifold are the probability measures $\nu$ equivalent to $\mu$ , and these form a positive cone inside $L^1(\Omega, \mu)$ . This cone can be coordinatized by the Radon-Nikodym derivatives $f = d\nu / d\mu$ . The linear structure of $L^1(\Omega, d\mu)$ provides the tangent space with

an affine structure, which is called the (-1)-affine structure in Amari's notation. Amari has suggested that we may also use the coordinates

$$
\ell_ {\alpha} (f) := f ^ {(1 - \alpha) / 2} \quad - 1 <   \alpha <   1, \tag {17}
$$

known as the Amari embeddings of the manifold into $L^p$ , where $p = 2(1 - \alpha)^{-1}$ , (since $f \in L^1$ , we have $u = f^{(1 - \alpha) / 2} \in L^p$ ). Thus, the Orlicz spaces of all the Young functions $|u|^p$ give the same topology on the manifold, namely, that of $L^1$ . So they do not help in eliminating states of infinite relative entropy. These coordinates do provide us with an interesting family of connections, $\nabla_{\alpha} \coloneqq \partial/\partial \ell_{\alpha}$ , which define the Amari affine structures.

We do better with the formal limit as $p \to \infty$ . In the discrete case, the relative entropy is the limit as $\alpha \to 1$ of the Hasegawa-Petz $\alpha$ -entropies

$$
\begin{array}{l} S (g | f) := \sum_ {x} f (x) (\log f (x) - \log g (x)) (18) \\ = \sum_ {x} \lim  _ {\alpha \rightarrow 1} (1 - \alpha) ^ {- 1} \left(f (x) - f (x) ^ {\alpha} g (x) ^ {1 - \alpha}\right). (19) \\ \end{array}
$$

It turns out that $S_{\alpha}(f|g)$ is the 'divergence' of the Fisher metric along the $\alpha$ -geodesics. The relative entropy $S(g|f)$ arises as the divergence along the geodesics provided by the embedding

$$
\ell_ {1} (f) := \log f.
$$

Thus the affine structure corresponds to the linear structure of the random variables $u$ where $f = f_0 e^u$ , as in the theory of Pistone and Sempi. The topology given by the corresponding Young function $\Phi_3$ is not equivalent to that of $L^1$ , but gives rise to the smaller space $L \log L$ , as wanted.

Is there a quantum analogue to this theory?

# 2 The quantum information manifold

# 2.1 The underlying set of the manifold

Let $\mathcal{H}$ be a separable Hilbert space, with $\mathcal{B}(\mathcal{H})$ denoting the algebra of bounded operators on $\mathcal{H}$ , and denote by $\Sigma_{+}$ the set of faithful normal states on $\mathcal{B}(\mathcal{H})$ . In [17] it was suggested that the quantum information manifold $\mathcal{M}$ in infinite dimensions should consist of $\rho \in \Sigma_{+}$ with the property that there exists $\beta_0 \in [0,1)$ such that $\rho^{\beta}$ is of trace class for all $\beta > \beta_0$ . That is, states $\rho \in \mathcal{M}$ are a bit smoother than general density operators, in that some fractional power of $\rho$ is also of trace class. This condition is satisfied by the temperature states of the harmonic oscillator (for which $\beta_0 = 0$ ) and most elementary systems, as well as quantum field theory, in a box with periodic boundary conditions. Thus, for given $\beta$ , the state must lie in the class $\mathcal{C}_{\beta}$ of Schatten, in the unfashionable case $\beta < 1$ ; this is a complete metrisable space of compact operator furnished with the quasi-norm $\rho \mapsto \left(\mathrm{Tr} \rho^{\beta}\right)^{1/\beta}$ [14]. In [17] we took the underlying set of the quantum infomanifold to be

$$
\mathcal {M} := \bigcup_ {0 <   \beta <   1} \mathcal {C} _ {\beta} \cap \Sigma_ {+}. \tag {20}
$$

All these states have finite von Neumann entropy. In limiting the theory to faithful states, we are imitating the decision of Pistone and Sempi that the probability measures of the

information manifold should be equivalent to the guiding measure $\mu$ , rather than say, merely absolutely continuous; here, the trace is the quantum analogue of the measure $\mu$ . Given a point $\rho_0 \in \mathcal{M}$ , we seek an analogue of the Cramér class at $\rho_0$ .

# 2.2 The quantum Cramér class

Let us write an arbitrary state $\rho_0\in \mathcal{M}$ as

$$
\rho_ {0} = \exp \left\{- H _ {0} - \psi_ {0} \right\}. \tag {21}
$$

This is always possible, since $\rho_0$ is faithful. The choice of $H_0$ is ambiguous up to a multiple of the identity, since this can be absorbed into $\psi$ , defined by

$$
\psi_ {0} = \log \operatorname {T r} \exp \{- H _ {0} \} = \log Z _ {0}.
$$

Thus there is no loss in generality by taking $Z_0 = 1$ .

We perturb a given state $\rho_0$ by adding a potential to $H_0$ , in analogy with the classical theory, where the potential is $u$ as in (4). Suppose that $X$ is a quadratic form such that $\operatorname{Dom} X \supseteq \operatorname{Dom} H_0^{1/2}$ and there exist positive $a, b$ such that

$$
| X (\varphi , \varphi) | \leq a \left\langle H _ {0} ^ {1 / 2} \varphi , H _ {0} ^ {1 / 2} \right\rangle + b \| \varphi \| ^ {2} \tag {22}
$$

for all $\varphi \in \operatorname{Dom} H_0^{1/2}$ . Then we say that $X$ is form-bounded relative to $H_0$ . The infimum of all $a$ satisfying (22) is called the $H_0$ -form bound of $X$ ; we shall denote the form bound by $\|X\|_K$ , in honour of T. Kato. It is a semi-norm on the linear set of forms bounded relative to $H_0$ . It is well known that if $\|X\|_K < 1$ , then $H_0 + X$ defines a semibounded self-adjoint operator. More, if $\|X\|_K$ is small enough, less that $a(\beta_0)$ say, depending on $\beta_0$ , then [17], we have

$$
\rho_ {X} := e ^ {- H _ {0} - X - \psi_ {X}} \in \mathcal {M}. \tag {23}
$$

To prove that $\rho_{X}$ is of trace class, write $-H_0 - X = -\beta H_0 - (1 - \beta)H_0 - X$ ; then by the Golden-Thompson inequality, taking $\beta_0 < \beta < 1$

$$
\begin{array}{l} \operatorname {T r} \rho_ {X} \leq \operatorname {T r} e ^ {- \beta H _ {0}} e ^ {- (1 - \beta) H _ {0} - X} \\ \leq \left\| \rho_ {0} ^ {\beta} \right\| _ {1} \left\| e ^ {- (1 - \beta) H _ {0} - X} \right\| _ {\infty} \\ <   \infty . \\ \end{array}
$$

More is true [17]; $\rho_{X}$ inherits the properties of $\rho_0$ with a new $\beta_0$ nearer 1, and lies in $\mathcal{M}$ . In [8], we added a further condition on the quadratic form, called $\epsilon$ -boundedness:

Definition 1 For any $\epsilon \in (0,1/2]$ we say that a quadratic form $X$ is $\epsilon$ -bounded by $H_0$ if there exists a constant $C$ such that

$$
\left(H _ {0} + C\right) ^ {- 1 / 2 - \epsilon} X \left(H _ {0} + C\right) ^ {- 1 / 2 + \epsilon} \leq C I.
$$

The set of states satisfying (1) is obviously $(+1)$ -convex; that is, if $X_{1}$ and $X_{2}$ satisfy (1), then so does $\lambda X_{1} + (1 - \lambda)X_{2}$ . We showed [8] that the free energy is an analytic function of the perturbation parameter in a small 'hood of zero. This, then, is an analogue of the Cramér condition. Here, we use this condition to specify the tangent space of $\mathcal{M}$ at $\rho_0$ .

For the cotangent space, we replace (1) by a (possibly) different set, of states $\rho_{X}$ that are $p$ -nearby $\rho_0$ , defined and used in [19]: for some $C > 1$ , and $p \in (0,1)$ ,

$$
C ^ {- 1} \rho_ {0} ^ {1 - p} \leq \rho_ {X} \leq C \rho_ {0} ^ {1 - p}. \tag {24}
$$

The set of states $\rho_{X}$ satisfying (24) is obviously (-1)-convex: if $\rho_{1} = \rho_{X_{1}}$ and $\rho_{2} = \rho_{X_{2}}$ are both $p$ -nearby $\rho_{0}$ , then so is $\lambda \rho_{1} + (1 - \lambda)\rho_{2}$ . It is not known whether it is (+1)-convex unless $p = 0$ . It is not hard to show that (24) implies that for small enough $p$ , $\rho_{X} \in \mathcal{M}$ [19]. It is easy to show that the intersection of the sets

$$
\left[ \bigcup_ {\epsilon > 0} \{\rho_ {X}: X \mathrm {i s} \epsilon \mathrm {b o u n d e d} \} \right] \cap \left[ \bigcup_ {p \in (0, 1)} \{\mathrm {s t a t e s} p \mathrm {- n e a r b y} \rho_ {0} \} \right]
$$

contains the set of states with finite Araki norm [19]; this set carries both affine structures.

Our strategy in furnishing $\mathcal{M}$ with a topology is a quantum version of [15]. We parametrise states near $\rho_0$ by the potential $X$ , and can adjust $X$ and $\psi_X$ so that the generalised mean $\rho_0 \cdot X$ of $X$ in the state $\rho_0$ , proved to be finite in [17], is zero:

$$
\rho \cdot X := \operatorname {T r} \int_ {0} ^ {1} \rho^ {t} X \rho^ {1 - t} d t = 0. \tag {25}
$$

These are the quantum scores. The $(+1)$ affine structure on forms satisfying (1) gives, by transfer of structure, an affine structure to the corresponding part of $\mathcal{M}$ . Thus we get a piece $N$ of a flat manifold modelled on a vector space. When furnished with the $\epsilon$ -norms, with any point of $N$ replacing $\rho_0$ , the norms on overlapping 'hoods are equivalent. We thus get a Banach manifold. It has the interesting property that there are no global linear coordinates, even though the coordinate patches are linear with linear transition functions. To see this, consider perturbations of the form $X = (k - 1)H_{0}$ , which is $H_{0}$ -small enough if $k$ is close to 1. We cannot use the perturbation if $k = 0$ , as then $X = -H_{0}$ , and $\exp \{-(H_0 + X)\} = I$ , which is not of trace class. Roughly speaking, the manifold is a convex cone pointing in the general direction of $H_{0}$ . This suggests that the correct Orlicz space must fail to satisfy the (technical) $\Delta_{2}$ -condition. The Orlicz class at $\rho_0$ , which is always convex but might not itself be linear, should allow only perturbations $X$ with sufficiently small norm. Then the Orlicz space, the linear span of the Orlicz class, parametrises the tangent space of $\mathcal{M}$ at $\rho_0$ but the scores will not provide a valid parametrization of the whole manifold. Our suggested Young function, below, shows these features.

# 2.3 The category of partially ordered Riemannian manifolds

Amari has posed the question [2], what properties, extra to being a Riemannian manifold, characterise information manifolds? Obviously, such a manifold must possess the Amari family of affine connections, $\{\nabla_{\alpha}\}$ , with $\nabla_{\alpha}$ dual to $\nabla_{-\alpha}$ relative to the metric. One could ask the same question for quantum information manifolds. These affine connections are associated with the embeddings (17), which can be extended to weights (non-normalised probabilities) and have quantum versions

$$
\ell_ {\alpha} (\rho) := \rho^ {2 / (1 - \alpha)}, \quad - 1 <   \alpha <   1. \tag {26}
$$

The quantum versions of the limit cases, $\alpha \rightarrow \pm 1$ , are

$$
\ell_ {+} (\rho) := \log \rho \text {a n d} \ell_ {-} (\rho) := \rho . \tag {27}
$$

It is a fact that all these maps are operator monotone; they preserve the partial order between operators. We say $A > B$ if $A - B$ is a positive (semidefinite) operator. Let us say that a coordinate system $\rho \mapsto \ell(\rho)$ for the set of weights is a monotone coordinate system if this partial ordering is preserved. An allowed coordinate system for the quantum case must be monotone, and a morphism between two information manifolds must involve monotone maps. This differs from Chentsov's definition of morphism; it allows non-linear changes of coordinates, which transform one monotone metric to another [10]. This suggests the following definition:

Definition 2 Let $\mathcal{M}_1$ and $\mathcal{M}_2$ be Riemannian manifolds with partial orders $\leq_1$ and $\leq_2$ . A map $T: \mathcal{M}_1 \to \mathcal{M}_2$ is called a morphism of partially ordered Riemannian manifolds if $T$ is a morphism of Riemannian manifolds and maps any two comparable points of $\mathcal{M}_1$ into comparable points of $\mathcal{M}_2$ , and the order is preserved.

This defines the category of partially ordered Riemannian manifolds. For example, in finite dimensions consider the set of faithful weights in $M^n$ furnished with the BKM metric, $g_B$ . Then an operator monotone bijection on this set transforms $g_B$ to another monotone metric, $g$ . According to [10], by this means we can get any of the monotone metrics as classified by Petz [13]. Thus all the models are isomorphic when regarded as partially ordered Riemannian manifolds.

# 2.4 The quantum Young function

In some recent work [1] on quantum Orlicz spaces, use was made of classical Young functions. Thus, if $X$ is a self-adjoint operator, and $\Phi$ is a Young function, one can take as the quantum Young function the map $A \mapsto \operatorname{Tr} \Phi(|\tilde{A}|)$ , where $\tilde{A}$ is the rearranged operator. For the cases $-1 < \alpha < 1$ , this gives us back the trace-norm topology, as explained in the classical case above, when we put $A = \rho$ . In the limit case $\ell_{+}$ , we encounter $\cosh X$ , which does not make sense for forms, and also does not correspond the perturbation by a potential. In the classical case, $f_0 e^{-u} = e^{-h_o - u}$ , but in the quantum case, $\rho_0 e^{-X}$ is not hermitian, even if $X$ is a bounded operator, unless $[H_0, X] = 0$ . The Young function $\Phi_1 = \cosh x - 1$ gets multiplied by $f_0$ in the classical theory (c.f. (5)), but the quantum analogue of this would be $\operatorname{Tr}(\rho_0 (\cosh |X| - 1))$ which is not positive. We therefore take a different choice of ordering for the non-commuting variables, and suggest [17] that the quantum Young function at $\rho_0$ should be

$$
\Phi (X) = \frac {1}{2} \operatorname {T r} \left(e ^ {- H _ {0} - \psi_ {o} - X} + e ^ {- H _ {0} - \psi_ {o} + X}\right) - 1. \tag {28}
$$

If $H_0$ commutes with $X \in \mathcal{B}(\mathcal{H})$ , this reduces to $\operatorname{Tr} \rho_0 \Phi_1(X)$ . Since this already includes the factor $\rho_0$ , we must omit this factor in the analogues of (5) and the rest. For $p$ -nearby states, we can take the analysis of [17] further:

Theorem 3 Suppose that $\rho_{X}$ is $p$ -nearby $\rho_0$ , for some $p < 1 - \beta_{X}$ . Then BKM regularised metric

$$
\langle X, X \rangle_ {B} := \frac {1}{2} \int_ {0} ^ {1} d \alpha \operatorname {T r} \left\{\rho_ {0} ^ {\alpha / 2} X \rho_ {0} ^ {1 - \alpha} X \rho_ {0} ^ {\alpha / 2} \right\} \tag {29}
$$

is well-defined.

PROOF: Since $X = H_{X} - H_{0}$ , it is enough to consider the case where each $X$ is replaced by $H_{X}$ , as the remaining terms involve $H_{0}$ and are easily bounded. We suppose that

$\rho_0 \leq C \rho_X^{1 - p}$ ; since $x \mapsto x^\alpha$ is operator monotone for $0 < \alpha < 1$ , we see that

$$
\rho_ {X} ^ {\frac {- \alpha (1 - p)}{2}} \rho_ {0} ^ {\alpha} \rho_ {X} ^ {\frac {- \alpha (1 - p)}{2}}
$$

is a bounded operator; the same goes if $\alpha$ is replaced by $1 - \alpha$ . We write the integrand as the product

$$
\begin{array}{l} \rho_ {0} ^ {\alpha} H _ {X} \rho_ {0} ^ {1 - \alpha} = \rho_ {X} ^ {\alpha (1 - p) / 2} \left(\rho_ {X} ^ {- \alpha (1 - p) / 2} \rho_ {0} ^ {\alpha} \rho_ {X} ^ {- \alpha (1 - p) / 2}\right) \rho_ {X} ^ {\alpha (1 - p) / 2} X \\ \rho_ {X} ^ {(1 - p) (1 - \alpha) / 2} \left(\rho_ {X} ^ {- (1 - p) (1 - \alpha) / 2} \rho_ {0} ^ {1 - \alpha} \rho_ {X} ^ {- (1 - p) (1 - \alpha) / 2}\right) \rho_ {X} ^ {- (1 - p) (1 - \alpha) / 2} H _ {X} \\ \end{array}
$$

of which the trace (by Hölder's inequality for traces) is bounded by

$$
C ^ {\alpha} \left\| H _ {X} \rho_ {X} ^ {(1 - p) / 2} \right\| _ {2} C ^ {1 - \alpha} \left\| H _ {X} \rho_ {X} ^ {(1 - p) / 2} \right\| _ {2}.
$$

The Hilbert-Schmidt norm is finite:

$$
\rho_ {X} ^ {(1 - p) / 2} H _ {X} = \rho_ {X} ^ {(1 - p - \delta) / 2} \left(\rho_ {X} ^ {\delta / 2} H _ {X}\right)
$$

for any small $\delta > 0$ is the product of a Hilbert-Schmidt operator and a bounded operator with norms independent of $\alpha$ ; thus the integral is finite. QED

Corollary 4 The usual proof of the Bogoliubov-Peierls inequality holds, to arrive at the inequality

$$
\log \operatorname {T r} e ^ {- H _ {0} + X} \geq \log \operatorname {T r} e ^ {- H _ {0}} + \rho_ {0} \cdot X
$$

Definition 5 Let us say that a map $\Phi$ , from a linear subspace $\mathcal{X}$ of the space of $H_0$ -bounded quadratic forms, to $\mathbf{R}^+ \cup \{\infty\}$ is a quantum Young function for $\mathcal{X}$ if

1. $\Phi(X)$ is finite for all forms $X$ with sufficiently small Kato bound   
2. $X\mapsto \Phi (X)$ is convex   
3. $\Phi (-X) = \Phi (X)$ for all $X\in \mathcal{X}$   
4. $\Phi(0) = 0$ , and if $X \neq 0$ , $\Phi(X) > 0$ , including $\infty$ as a possible value.

Theorem 6 For each $\rho \in \mathcal{M}$ , the map $\Phi$ of (28) is a quantum Young function.

PROOF Lemma (4) of [17] gives the proof of (1).

For (2), it is known [11] that for self-adjoint $A$ , the map $A \mapsto \operatorname{Tr} e^A$ is convex, so that

$$
\operatorname {T r} e ^ {\lambda A + (1 - \lambda) B} \leq \lambda \operatorname {T r} e ^ {A} + (1 - \lambda) \operatorname {T r} e ^ {B}.
$$

Put $A = -H_0 - X$ and $B = -H_0 - Y$ , where $X$ and $Y$ are sufficiently $H_0$ -small forms. Then $\lambda X + (1 - \lambda)Y$ is also a sufficiently small form, and

$$
\operatorname {T r} e ^ {- H _ {0} - \lambda X - (1 - \lambda) Y} = \operatorname {T r} e ^ {\lambda A + (1 - \lambda) B} \leq \lambda \operatorname {T r} e ^ {- H _ {0} - X} + (1 - \lambda) \operatorname {T r} e ^ {- H _ {0} - Y}.
$$

Then $\Phi$ , being the sum of two convex functions, is convex.

Items (3) and (4) are obvious. $QED$

# 2.5 The Luxemburg norm

We now specialize to the Young function of interest, associated with a point $\rho_0\in \mathcal{M}$ . Thus, $\rho_0 = \exp \{-H_0 - \psi_0\}$ , and $e^{-\beta H_0}$ is of trace class for some $\beta < 1$ . Let $Q_{0}$ be the quadratic form

$$
Q _ {0} (\phi) := \left\| H _ {0} ^ {1 / 2} \phi \right\| ^ {2}, \tag {30}
$$

and let $X$ be a $Q_0$ -bounded quadratic form. If $\|X\|_K > 1$ , then $\Phi(X)$ is put equal to $\infty$ , since either $H_0 + X$ or $H_0 - X$ is not bounded below. It might be that even when $\|X\|_K < 1$ , $\Phi(X)$ is still $\infty$ , because although $H_{\pm} := H_0 \pm X$ are both self-adjoint and bounded below, $e^{-H_{\pm}}$ might not be of trace class. Let us denote by $\|X\|_k$ the infimum of the $Q_0$ -bounds of $X$ such that $e^{-H_{\pm}} \notin \mathcal{C}_1$ , or $\infty$ if $X$ is $Q_0$ -tiny. We showed in [17] that $\|X\|_k > 0$ . Then we can define a lower semi-continuous Young function on the one-dimensional set of forms $\{\lambda X : \lambda \in \mathbf{R}\}$ by $\Phi(\lambda X)$ for small enough $\lambda$ , and by

$$
\Phi (X) := \left\{\begin{array}{c l}\lim  _ {\lambda \rightarrow 1} \Phi (\lambda X)&\text {i f} \| X \| _ {K} = \| X \| _ {k}\\\infty&\text {i f} \| X \| _ {K} > \| X \| _ {k}\end{array}\right. \tag {31}
$$

Theorem 7 With $\Phi$ given by (31), we have

(i)

$$
\left\| X \right\| _ {L a} := \inf  _ {r} \left\{r: \Phi \left(\frac {X}{r}\right) <   a \right\}
$$

defines a norm on $\operatorname{Span}_{\mathbf{R}}\mathcal{X}$ .

(ii) All these norms, for various $a > 0$ , are equivalent.

# PROOF

(i) Obviously, $\| \cdot \|_{L_a} \geq 0$ , and for $\lambda \neq 0$

$$
\begin{array}{l} \left\| \lambda X \right\| _ {L a} = \inf  \left\{r > 0: \Phi \left(\frac {\lambda X}{r}\right) <   a \right\} \\ = \inf  \left\{\left| \lambda \right| s > 0: \Phi \left(\frac {X}{s}\right) <   a \right\} \\ = | \lambda | \| X \| _ {L a}. \\ \end{array}
$$

Also, if $X = 0$

$$
\left\| X \right\| _ {L a} = \inf  \{r > 0: \Phi (0) <   a \} = \inf  \{r > 0 \} = 0.
$$

Conversely, if $X$ is such that $\| X \|_{L,a} = 0$ , then there must exist a sequence $r_n \to 0$ such that

$$
\Phi \left(\frac {X}{r _ {n}}\right) <   a. \tag {32}
$$

But by assumption, if $X \neq 0$ , $\Phi(sX) > 0$ for some $s > 0$ ; convexity then shows that $\Phi(sX) \to \infty$ at least as fast as linear in $s$ , contradicting (32); this shows that $X = 0$ .

Finally, for the triangle inequality, put $r = s + t$ , $\lambda = s / r$ , $1 - \lambda = t / r$ . Then the set

$$
A := A (a) := \left\{r: \Phi \left(\frac {X + Y}{r}\right) <   a \right\}
$$

contains the set

$$
A _ {0} = \left\{s + t: \lambda \Phi \left(\frac {X}{s}\right) + (1 - \lambda) \Phi \left(\frac {Y}{t}\right) <   a \right\}.
$$

For suppose that $r = s + t \in A_0$ . Then

$$
\begin{array}{l} \Phi \left(\frac {X + Y}{r}\right) = \Phi \left(\lambda \frac {X}{s} + (1 - \lambda) \frac {Y}{t}\right) \\ \leq \lambda \Phi \left(\frac {X}{s}\right) + (1 - \lambda) \Phi \left(\frac {Y}{t}\right) \\ <   a, \\ \end{array}
$$

showing that $r \in A$ , and so $A_0 \subseteq A$ . The set $A_0$ contains the set

$$
A _ {0 0} := \left\{s + t: \Phi \left(\frac {X}{s}\right) <   a \text {a n d} \Phi \left(\frac {Y}{t}\right) <   a \right\}.
$$

For suppose $r \in A_{00}$ . Then there exist $s, t$ such that $s + t = r$ and $\Phi(X / s) < a$ and $\Phi(Y / t) < a$ . Then there exists $s + t$ such that

$$
\lambda \Phi \left(\frac {X}{s}\right) + (1 - \lambda) \Phi \left(\frac {Y}{t}\right) \leq (\lambda + (1 - \lambda)) a = a,
$$

so $r \in A_0$ . This shows that $A_{00} \subseteq A_0 \subseteq A$ . Since the infimum of a larger set of real numbers is not greater than the infimum of a smaller set, we have

$$
\begin{array}{l} \left\| X + Y \right\| _ {L a} = \inf  A \leq \inf  A _ {0 0} \\ = \inf  \left\{s + t: \Phi \left(\frac {X}{s}\right) <   a \text {a n d} \Phi \left(\frac {Y}{t}\right) <   a \right\} \\ = \inf  \left\{s: \Phi \left(\frac {X}{s}\right) <   a \right\} + \inf  \left\{t: \Phi \left(\frac {Y}{t}\right) <   a \right\} \\ = \| X \| _ {L a} + \| Y \| _ {L a}. \\ \end{array}
$$

This proves (i).

(ii) We may assume that $a > b$ ; then

$$
\left\| X \right\| _ {L a} \leq \left\| X \right\| _ {L b}
$$

so $\| X \|_{L_b}$ is the stronger norm. It remains to show that $\| X \|_{L_b}$ is also weaker. If $X$ is $Q_0$ tiny, when the Kato seminorm $\| X \|_K$ vanishes, then $\Phi(\lambda X)$ is finite and continuous, increasing in $\lambda$ to infinity (by convexity). It therefore passes $a$ and $b$ at points $\lambda = a'$ and $b'$ , where

$$
a ^ {\prime} = \| X \| _ {L a} ^ {- 1} \qquad \text {a n d} \qquad b ^ {\prime} = \| X \| _ {L b} ^ {- 1}
$$

respectively. From convexity,

$$
\Phi \left(b ^ {\prime} X\right) = \Phi \left(\frac {b ^ {\prime}}{a ^ {\prime}} X + \left(1 - \frac {b ^ {\prime}}{a ^ {\prime}}\right) 0\right) \leq \frac {b ^ {\prime}}{a ^ {\prime}} \Phi \left(a ^ {\prime} X\right).
$$

Thus

$$
b \leq \frac {\| X \| _ {L a}}{\| X \| _ {L b}}. a
$$

giving

$$
\left\| X \right\| _ {L b} \leq \frac {a}{b} \left\| X \right\| _ {L a}, \tag {33}
$$

showing equivalence in this case. This set-up, in which the infimum of the sets $A(a)$ and $A(b)$ are both achieved in $0 < r < \| X\|_k^{-1}$ , could also arise if $\| X\|_K > 0$ , and leads to the same conclusion.

Now suppose that $\| X\| _K = 1$ , and consider $\Phi (\lambda X)$ as a function of $\lambda$ . It is possible that $b$ is not reached by any $\Phi (\lambda X)$ before $\lambda = \| X\| _k$ , in which case $\| X\|_{Lb} = \| X\|_{k}^{-1}$ . In that case $a$ is also not reached by $\Phi (\lambda X)$ before it becomes infinite, and $\| X\|_{La} = \| X\|_{k}^{-1}$ too, and the norms are equal, and so equivalent.

The only remaining possibility is that $\Phi(b'X) = b$ for some $b' < \|X\|_k$ , giving $\|X\|_{Lb} = 1/b'$ , while $a$ is not reached by $\Phi(\lambda X)$ before $\lambda = a'' := \|X\|_k$ , so that $\|X\|_{La} = \|X\|_k^{-1} = 1/a''$ . Then by convexity,

$$
\begin{array}{l} b = \Phi (b ^ {\prime} X) = \Phi \left(\frac {b ^ {\prime}}{a ^ {\prime \prime}} a ^ {\prime \prime} X + \left(1 - \frac {b ^ {\prime}}{a ^ {\prime \prime}}\right). 0\right) \\ \leq \frac {b ^ {\prime}}{a ^ {\prime \prime}} \Phi (a ^ {\prime \prime} X) = \frac {b ^ {\prime}}{a ^ {\prime \prime}} a. \\ \end{array}
$$

This can be rearranged to give (33), which completes the proof of (ii).

In view of (ii), we can take $a = 1$ , and use the notation $\| \cdot \|_L$ for the Luxemburg norm $\| \cdot \|_{L^1}$ . It is clear that $\| X \|_L \geq \| X \|_k$ : by our convention, $\Phi(X / r)$ is infinite for $r < \| X \|_k$ . This convention is inevitable; for, if both $\exp\{-H_0 \pm X\}$ are of trace class, there exists $C$ such that $\operatorname{Tr} \exp\{-H_0 \pm X\} \leq C$ . But the state is a positive operator, so its trace is its trace norm, which is larger than its operator norm. Hence

$$
0 \leq \exp \{- H _ {0} \pm X \} \leq C I.
$$

Taking logs (an operator monotone operation, also valid for forms) gives

$$
\pm X \leq H _ {0} + \log C.
$$

Thus $X$ must be $Q_0$ -bounded with bound $\leq 1$ : no larger $\| X\|_{K}$ can give finite $\Phi$ .

It is likely that in our situation, $\Phi(X / r)$ goes smoothly to infinity as $r \to 0$ , passing through all positive values, and diverging to infinity at $r = \|X\|_k^{-1}$ . If this were known to be true, then the proof of (ii) would be the same as the easy case when $X$ is $Q_0$ -tiny.

# 2.6 Duality

In [5], the authors associate with a Banach manifold $\mathcal{M}$ a whole bundle of tangent spaces, coming from the various Amari embeddings, $\rho \mapsto \ell_{\alpha}(\rho) = \rho^{1 / p}$ . This elegant point of view actually contains the fact that there is only one tangent space and one cotangent space, each of which is furnished with a family of affine connections.

We adopt a more concrete version, mainly because we do not yet know whether our space is complete, uniformly convex etc. as required by [5]. Let $\rho_0\in \mathcal{M}$ . The set of states

$$
\mathcal {X} := \left\{\rho_ {X}: X \text {i s} H _ {0} - \epsilon \text {- b o u n d e d} \right\}
$$

can be furnished with $(+1)$ -affine structure and with the Luxemburg norm. This space might not be complete. We parametrisse the space by the scores, $X$ . The topological dual

$\mathcal{X}^d$ of the completed space of scores will contain density operators with finite entropy, and possibly unwanted non-normal states and weights. We take the subset $\mathcal{X}^* \subset \mathcal{X}^d$ being the $(-1)$ -linear span of density operators obeying (24) for some $p$ , which, as remarked, carries the $(-1)$ -affine connection. The pair $\mathcal{X}, \mathcal{X}^*$ is generated by the Amari embeddings of the set of states near $\rho_0$ :

$$
\rho \mapsto \ell_ {+} (\rho) := \log \rho \text {a n d i t s d u a l} \rho \mapsto \ell_ {-} (\rho) := \rho
$$

and their associated affine connections, $(+1)$ and $(-1)$ . We may then write

$$
S (\rho_ {0} | \rho_ {X}) + S (\rho_ {X} | \rho_ {0}) = \mathrm {T r} \left[ (\log \rho_ {X} - \log \rho_ {0}) (\rho_ {Y} - \rho_ {0}) \right].
$$

We take the limit so that the differences define tangent vectors, to get the second Gateaux derivative of the l.h.s. This is known to be the BKM metric

$$
\left\langle X, Y \right\rangle_ {B} = \mathrm {T r} \left(d \ell_ {+} (\rho) d \ell_ {-} (\rho)\right).
$$

This shows that the duality between $\mathcal{X}$ and $\mathcal{X}^*$ , given by the trace form, can be expressed in terms of the $BKM$ metric.

Given a Young function $\Phi$ defined on $\mathcal{X}$ , we define the dual Young function $\Phi^{*}$ on the dual space $\mathcal{X}^*$ by

$$
\Phi^ {*} \left(\rho_ {Y}\right) := \sup  _ {X \in \mathcal {X}} \left\{\langle X, Y \rangle_ {B} - \Phi (X) \right\}, \quad \rho_ {Y} - \rho_ {0} \in \mathcal {X} ^ {*}. \tag {34}
$$

Theorem 8 $\Phi^{*}$ is a Young function, it is lower semi-continuous in the $BKM$ metric, and Young's inequality

$$
\Phi (X) + \Phi^ {*} (\rho_ {Y}) \geq \langle X, Y \rangle_ {B} \tag {35}
$$

holds for all $X,Y$

PROOF Clearly, $\Phi^*$ is even and vanishes at $Y = 0$ . For convexity, let $\rho_1$ denote $\rho_{Y_1}$ etc., so that $\rho_1 - \rho_0$ is the cotangent vector $d\ell_{-}(\rho_1)$ . Then

$$
\begin{array}{l} \Phi^ {*} (\lambda \rho_ {1} + (1 - \lambda) \rho_ {2}) = \sup  _ {X} \left\{\lambda \operatorname {T r} \left(X d \ell_ {-} (\rho_ {1})\right) + (1 - \lambda) \operatorname {T r} \left(X d \ell_ {-} (\rho_ {2})\right) - \Phi (X) \right\} \\ \leq \lambda \sup  _ {X} \left\{\left\langle X, Y _ {1} \right\rangle_ {B} - \Phi (X) \right\} + (1 - \lambda) \sup  _ {X} \left\{\left\langle X, Y _ {2} \right\rangle_ {B} - \Phi (X) \right\} \\ = \lambda \Phi^ {*} (\rho_ {1}) + (1 - \lambda) \Phi^ {*} (\rho_ {2}). \\ \end{array}
$$

It follows from $\Phi^{*}(\rho_{0}) = 0$ and convexity that $\Phi^{*}(\rho_{Y})\geq 0$ or is $\infty$

$\Phi^{*}$ , being the supremum of a family of continuous function (indeed, continuous linear functions) is lower semi-continuous. For Young's inequality, $\Phi^{*}(\rho_{Y})$ being the supremum of $\langle X,Y\rangle_{B} - \Phi (X)$ , cannot be smaller than any example. QED

The double dual obeys $\Phi^{**} \leq \Phi$ ; for,

$$
\begin{array}{l} \Phi^ {* *} (X) = \sup  _ {Y} \left\{\langle X, Y \rangle_ {B} - \Phi^ {*} (\rho_ {Y}) \right\} \\ = \sup  _ {Y} \left\{\langle X, Y \rangle_ {B} - \sup  _ {X ^ {\prime}} \left\{\langle X ^ {\prime}, Y \rangle_ {B} - \Phi (X ^ {\prime}) \right\} \right\} \\ = \sup  _ {Y} \inf  _ {X ^ {\prime}} \left\{\langle X - X ^ {\prime}, Y \rangle_ {B} + \Phi \left(X ^ {\prime}\right) \right\} \\ \leq \sup  _ {Y} \left\{\left\langle X - X ^ {\prime}, Y \right\rangle_ {B} + \Phi \left(X ^ {\prime}\right) \right\} \\ \end{array}
$$

for all $X^{\prime}$ . Choosing $X^{\prime} = X$ gives the inequality.

It follows that $(\Phi^{*})^{**} \leq \Phi^{*}$ . But we also have the inequality the other way round:

$$
\begin{array}{l} \left(\Phi^ {*}\right) ^ {* *} \left(\rho_ {Y}\right) = \left(\Phi^ {* *}\right) ^ {*} \left(\rho_ {Y}\right) = \sup  _ {X} \left\{\left\langle X, Y \right\rangle_ {B} - \Phi^ {* *} (X) \right\} \\ \geq \sup  _ {X} \left\{\left\langle X, Y \right\rangle_ {B} - \Phi (X) \right\} \\ = \Phi^ {*} (\rho_ {Y}), \\ \end{array}
$$

so $(\Phi^{*})^{**} = \Phi^{*}$ . This duality occurs because $\Phi^{*}$ is lower semi-continuous. Indeed, $\Phi^{**}$ is the lower semi-continuous version of $\Phi$ [4]. From now on, we shall assume that $\Phi$ is lower semi-continuous, so that $\Phi^{**} = \Phi$ .

We now consider the quantum analogue of the inequality (16): the classical Young function $\lambda \rightarrow \Phi (\lambda X)$ is continuous and increasing where finite. It follows that the infimum in theorem (7) is achieved at $r = \| X\| _L^{-1}$ . Similarly for the dual Luxemburg norm. Now let $\| X\| _L = 1$ and $\| \rho_Y - \rho_0\|_{L^*} = 1$ . Then $\Phi (X) = 1$ and $\Phi^{*}(\rho_{Y}) = 1$ , and by Young's inequality (35),

$$
2 \| X \| _ {L} \left\| \rho_ {X} - \rho_ {0} \right\| _ {L ^ {*}} = 2 = \Phi (X) + \Phi^ {*} (\rho_ {Y}) \geq \operatorname {T r} \left[ X \left(\rho_ {Y} - \rho_ {0}\right) \right]
$$

which multiplies up to give for tangent and cotangent vectors

$$
\langle X, Y \rangle_ {B} \leq 2 \| X \| _ {L} \| \rho_ {Y} - \rho_ {0} \| _ {L ^ {*}}. \tag {36}
$$

# 3 Conclusion

We have argued that the information manifold in quantum theory should consist of density operators $\rho$ , some fractional power of which is still of trace class. The topology on the manifold should not be given by the trace norm. Instead, a 'hood of a given state $\rho_0$ should be given by $\epsilon$ -bounded quadratic forms; these were shown [8] to make up a possible analogue of the Cramér class of random variables, in that their Kubo-Mori expansion is analytic. This set of states carries the $(+1)$ affine structure of Amari. A possible Young function, related to the free energy, was introduced. The dual Young function was shown to be finite on a set, the union of all $p$ -nearby states, and this carries the $(-1)$ -affine structure of Amari. The beginnings of Young theory (the BKM-metric, the Luxemburg norms, Young's inequality and the Hölder-Orlicz inequality) were derived.

Let us now complete $\mathcal{X}$ in the Luxemburg norm, and $\mathcal{X}^*$ in the dual Luxemburg norm. The quantum Hölder-Orlicz inequality (36) then shows that the bilinear form between the spaces remains finite; we can therefore extend the definition of the $BKM$ -metric to the completions. The two Banach spaces thus obtained contain only normal states. The tangent and cotangent spaces are then complete and dual relative to the Hilbert-Schmidt scalar product, and are furnished with the $(\pm 1)$ -affine structures. The tangent space then contains the set of operators with finite Araki norm, and the cotangent space contains the states which are perturbations of $\rho_0$ by such operators.

The Luxemburg norm becomes large when we add a perturbation such that one of $e^{-H_0 \pm X}$ nearly ceases to be of trace class. In this way, the manifold consists of points that are in the interior of some one-parameter exponential model. All states in the manifold have finite entropy, and states near $\rho_0$ have finite relative entropy to $\rho_0$ .

One important property of the theory remains unproved: the equivalence of the Luxemburg norms based on points $\rho_0$ and $\rho_{X}$ for perturbations $Y$ lying in the overlaps of any

'hoods of $\rho_0$ with any 'hood of $\rho_{X}$ . It would also be nice for the dual affine structures to be defined on the same space. In the classical case, this was resolved by Grasselli [7] in the subtheory obtained by completing the space of bounded perturbations in the Luxemburg norm, to obtain the (separable) Banach space $M$ . Then the information manifold becomes a Banach manifold modelled on $M$ . In the quantum case, the analogue of this space seems to be the completion in the Luxemburg norm of the linear space consisting of perturbations of finite Araki norm. One can ask whether this completion consists of only tiny forms.

# References

[1] Al-Rashed, and Zegarinski, B., Noncommutative Orlicz Spaces associated with a State, to appear in STUDIA MATHEMATICA   
[2] Amari, S.-I., Differential-Geometric Methods in Statistics, Berlin, Springer-Verlag, 1985 (Lecture Notes in Statistics, vol. 28)   
[3] Amari, S.-I., and Nagaoka, Methods of Information Geometry, Amer. Math. Soc., Providence, R.I., translated from Japanese by D. Harada, 1993.   
[4] Ekeland, i., and Temam, R., Convex Analysis and Variational Problems, North Holland, 1976.   
[5] Gibilisco, P., and Isola, T., Connections on Statistical Manifolds of Density Opertators by Geometry of Noncommutative $L^p$ -Spaces, Infinite Dim. Anal., Quant. Prob. and Rel. Topics, 2, 169-178, 1999   
[6] Hiriart-Urruty, J.-P. and Lermaréchal, C., Convex Analysis and Minimisation Algorithms I, Springer-Verlag, 1993   
[7] Grasselli, M.R., Ph.D. Thesis, 2002, King's College, London.   
[8] Grasselli, M. R., and Streater, R. F., The quantum information manifold for $\epsilon$ -bounded forms, Rep. Mathematical Phys., 46, 325-335, 2000   
[9] Krasnoselski, M. A., and Ruticki, Ya. B., Convex Functions and Orlicz Spaces, P. Noordhoff, 1961.   
[10] Leszniewski, A. and Ruskai, M. B., Monotone Riemannian metrics and relative entropy on noncommutative probability spaces, J. Mathematical Phys., 40, 5702-5724, 1999   
[11] Lieb, E.H., Convex trace functions and the Wigner-Yanase-Dyson conjecture, Advances in Math., 11, 267-288, 1973.   
[12] Musielak, J., Orlicz Spaces and Modular Spaces, Lecture Notes in Math. 1034, Springer-Verlag, 1980, §13.11.   
[13] Petz, D., Monotone Metrics on Matrix Spaces, Linear Alg. and Appl. 244, 81-96, 1996   
[14] Pietsch, A., Nuclear Locally Convex Spaces, Springer-Verlag, 1972.   
[15] Pistone, G., and Sempi, C., An infinite-dimensional geometric structure on the space of all the probability measures equivalent to the given one, Ann. Stat., 23, 1543-1561, 1995

[16] Rao, M. M., and Ren, Z. D., Theory of Orlicz Spaces, Marcel Dekker, 1992.   
[17] Streater, R. F., The Information Manifold for Relatively Bounded Potentials, Proc. Steklov Institute of Mathematics, 228, 205-223, 2000.   
[18] Streater, R. F., The analytic quantum information manifold, Conference Proc., Canadian Math. Soc. 29, 603-611, 2000   
[19] Streater, R. F., Duality in Quantum Information Geometry, Open Systems and Information Dynamics, 11, 71-77, 2004