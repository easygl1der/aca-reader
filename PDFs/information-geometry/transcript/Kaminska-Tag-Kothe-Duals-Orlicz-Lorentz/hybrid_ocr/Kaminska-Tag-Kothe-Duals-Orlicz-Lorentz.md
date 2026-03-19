# ON KÖTHE DUALS OF ORLICZ-LORENTZ SPACES

ANNA KAMINSKA AND HYUNG-JOON TAG

ABSTRACT. In this article, we study a number of properties of the Kothe duals $\mathcal{M}_{\varphi ,w}$ of Orlicz-Lorentz spaces. An explicit description of the order-continuous subspace of $\mathcal{M}_{\varphi ,w}$ is provided. Moreover, the separability of these spaces are characterized by the growth condition $\Delta_{2}$ . Consequently, the Kothe dual space $\mathcal{M}_{\varphi ,w}$ has the Radon-Nikodym property if and only if the N-function at infinity $\varphi$ satisfies the appropriate $\Delta_2$ -condition. The comparison between $\mathcal{M}_{\varphi ,w}$ spaces is characterized via standard orders between Orlicz functions. As applications of these results, we provide sufficient conditions for M-embedded order-continuous subspaces of Orlicz-Lorentz spaces equipped with the Luxemburg norm and prove the existence of a unique norm-preserving extension on Orlicz-Lorentz spaces equipped with the Orlicz norm.

# 1. INTRODUCTION

In this article, we investigate basic properties of the Köthe duals $\mathcal{M}_{\varphi ,w}$ of Orlicz-Lorentz spaces and their applications to M-embeddedness and the uniqueness of norm-preserving extensions of bounded linear functionals on Orlicz-Lorentz spaces. The Orlicz-Lorentz spaces appeared as a natural generalization of both Orlicz and Lorentz spaces [11]. Since then, some geometrical properties e.g. separability, rotundity or nonsquareness [7,11] of these spaces have been studied. However, comparing to Orlicz spaces, many properties of Orlicz-Lorentz spaces have not been investigated because the explicit description of their Kothe duals was not available until later. Moreover, these Kothe duals exhibit different behaviors from those in the case of Orlicz spaces. It is well-known that the modular functionals for both Orlicz spaces and their Kothe duals have the same structure, so we can study those spaces within the same framework. However, as it turns out, the analogous claim does not hold for Orlicz-Lorentz spaces.

To elaborate this more, in 2013, the first author and Raynaud introduced a new modular $P_{\varphi,w}$ [17] and proved, with Lesnik, that the class of Banach function spaces defined by $P_{\varphi,*w}$ is actually the Köthe dual spaces of Orlicz-Lorentz spaces $\Lambda_{\varphi,w}$ [12]. The modular $\rho_{\varphi,w}(f)$ of Orlicz-Lorentz space is based on the decreasing rearrangement $f^*$ of $f$ , while the modular $P_{\varphi,w}(f)$ is defined via $f^* / v$ where $v$ is a decreasing function submajorized by a weight function $w$ (i.e. $v \prec w$ ), or the level function $f^0$ of $f$ with respect to $w$ . This major difference shows us that the modular $\rho_{\varphi,w}$ exhibits a different behavior from the modular $P_{\varphi,w}$ . As a matter of fact, while the modular $\rho_{\varphi,w}$ is orthogonally subadditive, the modular $P_{\varphi,w}$ is orthogonally superadditive, and so constructing suitable functions to verify certain properties of the space $\mathcal{M}_{\varphi,w}$ requires different approaches from Orlicz-Lorentz spaces. The space $\mathcal{M}_{\varphi,w}$ has also been studied in a spirit of abstract Lorentz spaces. For interested readers, we refer to [16].

From the fact that the space $\mathcal{M}_{\varphi, w}$ is not an Orlicz-Lorentz space, the properties of this space needs to be studied separately. Such attempts have been done partially in the past. For instance, a sufficient condition for the order-continuity of $\mathcal{M}_{\varphi, w}$ has been provided in [8]. In the same paper, it is shown that the space $\mathcal{M}_{\varphi, w}$ is never rotund unless $w$ is a constant function. This consequently shows that Orlicz-Lorentz spaces are never smooth if its complementary

function satisfies the appropriate $\Delta_2$ -condition. Moreover, the explicit description of the space $\mathcal{M}_{\varphi,w}$ allows us to explore geometrical and ideal structures of Orlicz-Lorentz spaces $\Lambda_{\varphi,w}$ . It is well-known that the order-continuous subspaces of Orlicz-Lorentz spaces equipped with the Luxemburg norm are M-ideals [13]. Moreover, the Orlicz-Lorentz spaces with the diameter two properties can be characterized by the $\Delta_2$ -condition [14]. For the diameter two properties, it was essential to compute the fundamental function of the space $\mathcal{M}_{\varphi,w}$ in full generality. Since the space $\mathcal{M}_{\varphi,w}$ has appeared recently, many properties have not been investigated yet. We attempt to study some of those in the article.

The paper consists of seven parts. In sections 2 and 3 we recall necessary facts on Orlicz-Lorentz spaces and their Kőthe duals. In section 4, from an explicit description of the order-continuous subspace of $\mathcal{M}_{\varphi,w}$ (Theorem 4.7), we show that the separability of the space $\mathcal{M}_{\varphi,w}$ is characterized via the $\Delta_2$ -condition (Theorem 4.15). This consequently provides a sufficient condition for a class of $\mathcal{M}_{\varphi,w}$ to have the Radon-Nikodym property (Theorem 4.16). In section 5, we characterize the inclusion operators between the spaces $\mathcal{M}_{\varphi,w}$ defined by different Orlicz functions (Theorem 5.1). In section 6, we identify an interval for the Orlicz norm on $\mathcal{M}_{\varphi,w}$ that attains its value (Theorem 6.4). As applications in section 7, we study the M-embeddedness of the order-continuous subspaces of Orlicz-Lorentz spaces (Theorem 7.4) and the uniqueness of norm-preserving extensions of bounded linear functionals on Orlicz-Lorentz spaces equipped with the Orlicz norm (Theorem 7.10, 7.11, and 7.12).

# 2. PRELIMINARIES

Here we recall some facts from the theory of Banach function lattices. Let us denote $(\Omega, \Sigma, \mu)$ as a measure space $\Omega$ where $\Sigma$ is a $\sigma$ -algebra defined on $\Omega$ and $\mu$ a $\sigma$ -finite measure. The space of all $\mu$ -measurable functions over a measure space $\Omega$ is denoted by $L_0(\Omega)$ . The notation “ $\mu$ -a.e.” stands for almost everywhere convergence with respect to a measure $\mu$ , but we simply denote “a.e.” when $\mu$ is the Lebesgue measure $m$ . A Banach space $(X, \| \cdot \|_X) \subset L_0(\Omega)$ is said to be a Banach function lattice if for any $f \in L_0(\Omega)$ and $g \in X$ , if $0 \leq |f| \leq |g|$ $\mu$ -a.e. then $f \in X$ and $\| f \|_X \leq \| g \|_X$ . We say a Banach function lattice has the Fatou property if for every sequence $(f_n)_{n=1}^{\infty} \subset X$ such that $0 \leq |f_n| \uparrow |f|$ $\mu$ -a.e. and $\sup \| f_n \|_X < \infty$ we have $f \in X$ and $\| f_n \|_X \to \| f \|_X$ .

For a Banach function lattice $X$ , a function $f \in X$ is said to be order-continuous if $\| f_n \|_X \downarrow 0$ for every sequence $(f_n)_{n=1}^{\infty}$ of measurable functions such that $f_n \leq |f|$ for every $n \in \mathbb{N}$ and $f_n \downarrow 0$ for $\mu$ -a.e. [2, Proposition 1.3.5]. In this article, the term simple function stands for a function that has finitely many values and support of finite measure. The set of all order-continuous elements in $X$ is denoted by $X_a$ . The closure of the set of all simple functions is denoted by $X_b$ . In general, we have $X_a \subset X_b$ [2, Theorem 1.3.11]. A measure $\mu$ is separable if there exists a countable family $\mathcal{F}$ of measurable subsets such that for every $\epsilon > 0$ and $E \in \Sigma$ with $\mu E < \infty$ , there exists a measurable subset $A \in \mathcal{F}$ such that $\mu(A\Delta E) < \epsilon$ , where $A\Delta E$ is the symmetric difference between $A$ and $E$ . It is well-known that $X_a$ is separable if and only if the measure $\mu$ is separable [2, Theorem 1.5.5]. Hence, under our assumption on the measure space in this article, the order-continuous Banach function lattices are always separable.

The Kőthe dual $X' \subset L_0(\Omega)$ of a Banach function lattice $X$ is the set of $\mu$ -measurable functions such that for each $g \in X'$ the associated norm $\| g \|_{X'}$ defined by

$$
\left\| g \right\| _ {X ^ {\prime}} = \sup  \left\{\left| \int_ {\Omega} g f \right|: \| f \| _ {X} \leq 1 \right\}
$$

is finite. When the order-continuous subspace $X_{a}$ contains all simple functions, we have $X_{a} = X_{b}$ and the Köthe dual $X^{\prime}\simeq (X_{a})^{*}$ [2, Corollary 1.4.2]. For sequence spaces, $X_{a} = X_{b}$ always holds [2, Theorem 1.3.13].

For $\lambda > 0$ , the distribution function $d_{f}(\lambda)$ of $f \in L_0(\Omega)$ is defined by $d_{f}(\lambda) = \mu \{t \in \Omega : |f(t)| > \lambda\}$ . If $d_{f}(\lambda) = d_{g}(\lambda)$ for all $\lambda > 0$ , then we say $f$ and $g$ are equimeasurable. For $f \in L_0(\Omega)$ , the function $f^{*}(t) = \inf \{\lambda > 0 : d_{f}(\lambda) \leq t\}$ is called the decreasing rearrangement of $f$ , and $f^{*}$ is a Lebesgue measurable function on interval $[0, \mu(\Omega))$ . For any sequence $x$ , the decreasing rearrangement $x^{*}$ of $x$ is defined by $x^{*}(i) = \inf \{\lambda > 0 : d_{x}(\lambda) < i\}$ , where $\mu$ is the counting measure on $\mathbb{N}$ . In this article, the term "decreasing" refers to non-increasing. The functions $f$ and $f^{*}$ are equimeasurable, and the same fact also holds for sequences $x$ and $x^{*}$ .

Let $f$ and $g$ be Lebesgue measurable functions on $I = [0, \gamma)$ , $\gamma \leq \infty$ . We say that $f$ is submajorized by $g$ if $\int_0^t f \leq \int_0^t g$ for every $t \in I$ . By using the Hardy-Littlewood-Pólya relation [2, Definition 2.3.5], we denote this submajorization by $f \prec g$ . We will also use this notation for sequences analogously. The following facts will be useful later.

Lemma 2.1. (Hardy's Lemma) [2, Proposition 2.3.6] Let $f_{1}$ and $f_{2}$ be non-negative Lebesgue measurable functions on $[0,\gamma)$ , $0 < \gamma \leq \infty$ , and suppose $\int_0^t f_1(s)ds\leq \int_0^t f_2(s)ds$ for all $t\in [0,\gamma)$ . Let $g$ be any non-negative decreasing function on $[0,\gamma)$ . Then $\int_0^\gamma f_1(s)g(s)ds\leq \int_0^\gamma f_2(s)g(s)ds$ .

Lemma 2.2. [20, pg 67] Let $f \in L_0(\Omega)$ be such that $d_f(\lambda) < \infty$ for all $\lambda > 0$ and $(f_n)$ be a sequence of measurable functions such that $|f_n| \leq |f|$ $\mu$ -a.e. for every $n \in \mathbb{N}$ . If $f_n \to f$ $\mu$ -a.e. then $(f - f_n)^* \to 0$ a.e. The same result remains true for sequences.

For a Banach function lattice $X$ , if all equimeasurable functions $f, g \in X$ satisfies $\| f \|_X = \| g \|_X$ , then we say $X$ is rearrangement-invariant (r.i.). Not only Orlicz-Lorentz spaces but also their Köthe dual spaces are known to be r.i. and to have the Fatou property [16, Theorem 4.7]. The fundamental function of r.i. Banach function lattice $X$ is defined by $\phi_X(t) = \| \chi_{E_t} \|_X$ where $E_t$ is a set of measure $t \in [0, \infty)$ . For a r.i. Banach function space $X$ over a nonatomic $\sigma$ -finite measure space, if $\lim_{t \to 0+} \phi_X(t) = 0$ , then we have $X_a = X_b$ [2, Theorem 2.5.5]. For a r.i. Banach sequence space, this relationship always holds [2, Theorem 2.5.4]. We refer to [2, 30] for more details on the theory of Banach function lattices.

Throughout the article, the notation $\operatorname{supp} f$ stands for the support of a $\mu$ -measurable function $f$ . When a Banach space $X$ is isometrically isomorphic to another Banach space $Y$ , we will use the notation $X \simeq Y$ . From now on, unless specified, we will only consider $\Omega = I = [0, \gamma)$ , $\gamma \leq \infty$ with the Lebesgue measure $\mu = m$ and $\Omega = \mathbb{N}$ with the counting measure. Accordingly, we denote $L_0 = L_0(I)$ for Lebesgue measurable functions on $I$ , and $\ell_0 = L_0(\mathbb{N})$ for sequences.

# 3. ORLICZ-LORENTZ SPACES AND THEIR KÖTHE DUALS

In this section, we provide basic information on Orlicz-Lorentz spaces and their Kőthe dual spaces $\mathcal{M}_{\varphi ,w}$ . Also, a few facts about level functions will be presented here.

An Orlicz function $\varphi : \mathbb{R}^+ \to [0, \infty)$ is a convex function such that $\varphi(0) = 0$ and $\varphi(u) > 0$ for all $u > 0$ . The complementary function $\varphi_*$ of an Orlicz function $\varphi$ is defined by $\varphi_*(v) = \sup \{uv - \varphi(u) : u > 0\}$ , $v \geq 0$ . Even though the function $\varphi_*$ is also convex and $\varphi_*(0) = 0$ , we can have $\varphi_*(v) = 0$ for some $v > 0$ and $\varphi_*(v) = \infty$ for some $v < \infty$ . For instance, the complementary function $\varphi_*$ of $\varphi(u) = u$ has value 0 on the interval $[0, 1]$ and $\infty$ outside of $[0, 1]$ . An Orlicz function $\varphi$ and its complementary function $\varphi_*$ satisfies Young's inequality, that is, $uv \leq \varphi(u) + \varphi_*(v)$ for all $u, v \in \mathbb{R}^+$ . An Orlicz function $\varphi$ is said to be an $N$ -function at zero if $\lim_{u \to 0} \frac{\varphi(u)}{u} = 0$ and an $N$ -function at infinity if $\lim_{u \to \infty} \frac{\varphi(u)}{u} = \infty$ . An Orlicz function is $N$ -function at infinity if and only if its complementary function is finite [14]. When an Orlicz function $\varphi$ is both $N$ -function at zero and at infinity, we say $\varphi$ is an $N$ -function. An Orlicz function $\varphi$ satisfies $\Delta_2^0$ -condition if there exist $K > 2$ and $u_0 > 0$ such that $\varphi(2u) \leq K\varphi(u)$ for all $0 \leq u \leq u_0$ . Analogously, $\varphi$ satisfies $\Delta_2^\infty$ -condition if there exist $K > 2$ and $u_0 \geq 0$ such

that $\varphi(2u) \leq K\varphi(u)$ for all $u \geq u_0$ . If $\varphi$ satisfies both $\Delta_{2}^{0}$ - and $\Delta_{2}^{\infty}$ -conditions, we say that $\varphi$ satisfies the $\Delta_{2}$ -condition. In this article, the "appropriate" $\Delta_{2}$ -condition means $\Delta_{2}^{\infty}$ -condition for $\gamma < \infty$ , $\Delta_{2}$ -condition for $\gamma = \infty$ , and $\Delta_{2}^{0}$ -condition for the sequence spaces. We have the following lemma that will be useful in Section 4.

Lemma 3.1. [5, Theorem 1.13] An Orlicz function $\varphi$ satisfies the $\Delta_{2-}$ (resp., $\Delta_{2}^{\infty}-$ ; $\Delta_{2}^{0}-$ ) condition if and only if there exist $l > 1$ and $K > 1$ (resp., $l > 1$ , $K > 1$ , $u_0 \geq 0$ ; $l > 1$ , $K > 1$ , $u_0 > 0$ ) such that $\varphi(lu) \leq K\varphi(u)$ for all $u \geq 0$ (resp., $u \geq u_0$ ; $0 \leq u \leq u_0$ ).

Let the weight function $w: I \to [0, \gamma)$ be a decreasing and locally integrable function. Then $W(t) := \int_0^t w < \infty$ for all $t \in I$ . In this article we always assume that $W(\infty) = \int_0^\infty w = \infty$ . The modular for Orlicz-Lorentz function spaces $\rho_{\varphi, w}(\cdot): L_0 \to [0, \infty]$ on $f \in L_0$ is defined by

$$
\rho_ {\varphi , w} (f) = \int_ {I} \varphi (f ^ {*}) w,
$$

and the modular for Orlicz-Lorentz sequence spaces $\alpha_{\varphi ,w}(\cdot):\ell_0\to [0,\infty ]$ on $x\in \ell_0$ by

$$
\alpha_ {\varphi , w} (x) = \sum_ {i = 1} ^ {\infty} \varphi (x ^ {*} (i)) w (i).
$$

The modular $\rho_{\varphi, w}$ is convex and orthogonally subadditive, that is for $f \wedge g = 0$ , $\rho_{\varphi, w}(f + g) \leq \rho_{\varphi, w}(f) + \rho_{\varphi, w}(g)$ . If $0 \leq |f| \leq |g|$ a.e., then $\rho_{\varphi, w}(f) \leq \rho_{\varphi, w}(g)$ . Similarly, these facts are also true for the modular $\alpha_{\varphi, w}$ .

The Orlicz-Lorentz function and sequence space $\Lambda_{\varphi ,w}$ and $\lambda_{\varphi ,w}$ are defined respectively by

$$
\Lambda_ {\varphi , w} = \left\{f \in L _ {0}: \rho_ {\varphi , w} (k f) <   \infty \text {f o r s o m e} k > 0 \right\},
$$

$$
\lambda_ {\varphi , w} = \{x \in \ell_ {0}: \alpha_ {\varphi , w} (k x) <   \infty \mathrm {f o r s o m e} k > 0 \}.
$$

Notice that we get the Orlicz space $L_{\varphi}$ (resp. $\ell_{\varphi}$ ) if $w \equiv 1$ and the Lorentz space $\Lambda_{p,w}$ for $1 \leq p < \infty$ (resp. $\lambda_{p,w}$ ) if $\varphi(u) = u^p$ .

We consider the Luxemburg norm $\| \cdot \|_{\varphi ,w}$ on $\Lambda_{\varphi ,w}$ defined by

$$
\| f \| _ {\varphi , w} = \inf  \left\{\epsilon > 0: \rho_ {\varphi , w} \left(\frac {f}{\epsilon}\right) \leq 1 \right\},
$$

and the Orlicz norm $\| \cdot \|_{\varphi ,w}^{0}$ on $\Lambda_{\varphi ,w}$ defined by

$$
\| f \| _ {\varphi , w} ^ {0} = \inf _ {k > 0} \left(\frac {1}{k} (1 + \rho_ {\varphi , w} (k f))\right).
$$

The analogous norms for the sequence space $\lambda_{\varphi ,w}$ can be defined by replacing $\rho_{\varphi ,w}$ with $\alpha_{\varphi ,w}$ . These norms are known to be equivalent to each other, precisely,

$$
\| f \| _ {\varphi , w} \leq \| f \| _ {\varphi , w} ^ {0} \leq 2 \| f \| _ {\varphi , w},
$$

$$
\| x \| _ {\varphi , w} \leq \| x \| _ {\varphi , w} ^ {0} \leq 2 \| x \| _ {\varphi , w}.
$$

From now on, we denote an Orlicz-Lorentz function (resp. sequence) space equipped with the Luxemburg norm by $\Lambda_{\varphi ,w}$ (resp. $\lambda_{\varphi ,w}$ ) and with the Orlicz norm by $\Lambda_{\varphi ,w}^{0}$ (resp. $\lambda_{\varphi ,w}^{0}$ ), respectively. For more information on Orlicz-Lorentz spaces and their properties, we refer to [11].

An explicit description of the Kőthe dual spaces $\mathcal{M}_{\varphi, w}$ and $\mathfrak{m}_{\varphi, w}$ of Orlicz-Lorentz function and sequence spaces has been given and studied in [8, 12]. In [17], the more abstract and general

approach clarifies and completes the studies. There are two modulars $P_{\varphi, w}$ and $Q_{\varphi, w}$ for $f \in L_0$ defined by

$$
P _ {\varphi , w} (f) = \inf \left\{\int_ {I} \varphi \left(\frac {f ^ {*}}{v}\right) v: v \prec w, v \downarrow \right\}, \mathrm {a n d} Q _ {\varphi , w} (f) = \int_ {I} \varphi \left(\frac {(f ^ {*}) ^ {0}}{w}\right) w = \int_ {I} \varphi \left(\frac {f ^ {*}}{w ^ {f ^ {*}}}\right) w ^ {f ^ {*}},
$$

and $\mathfrak{p}_{\varphi ,w}$ and $\mathfrak{q}_{\varphi ,w}$ for $x\in \ell_0$ defined by

$$
\mathfrak {p} _ {\varphi , w} (x) = \inf  \left\{\sum_ {i = 1} ^ {\infty} \varphi \left(\frac {x ^ {*} (i)}{v (i)}\right) v (i): v \prec w, v \downarrow \right\}, \text {a n d}
$$

$$
\mathfrak {q} _ {\varphi , w} (x) = \sum_ {i = 1} ^ {\infty} \varphi \left(\frac {(x ^ {*}) ^ {0} (i)}{w (i)}\right) w (i) = \sum_ {i = 1} ^ {\infty} \varphi \left(\frac {x ^ {*} (i)}{w ^ {x ^ {*}} (i)}\right) w ^ {x ^ {*}} (i).
$$

Here $f^0$ (resp. $x^0$ ) denotes the level function of $f$ (resp. $x$ ) in the sense of Halperin [9] and $w^{f^*}$ (resp. $w^{x^*}$ ) is the inverse level function with respect to $f^*$ (resp. $x^*$ ) [12, 17]. If an Orlicz function is an $N$ -function, then $P_{\varphi, w}(f) = Q_{\varphi, w}(f)$ (resp. $\mathfrak{p}_{\varphi, w}(x) = \mathfrak{q}_{\varphi, w}(x)$ ) for every $f \in L_0$ (resp. $x \in L_0$ ). However, without the assumption, we only know $P_{\varphi, w}(f) \leq Q_{\varphi, w}(f)$ (resp. $\mathfrak{p}_{\varphi, w}(f) \leq \mathfrak{q}_{\varphi, w}(f)$ ) in general [17, Theorem 8.9]. With these moduli, the function and sequence spaces $\mathcal{M}_{\varphi, w}$ and $\mathfrak{m}_{\varphi, w}$ [17, Corollary 7.7] are given by

$$
\begin{array}{r l} & {\mathcal {M} _ {\varphi , w} = \{f \in L _ {0}: P _ {\varphi , w} (k f) <   \infty \mathrm {f o r s o m e} k > 0 \} = \{f \in L _ {0}: Q _ {\varphi , w} (k f) <   \infty \mathrm {f o r s o m e} k > 0 \},} \\ & {\mathfrak {m} _ {\varphi , w} = \{x \in \ell_ {0}: \mathfrak {p} _ {\varphi , w} (k x) <   \infty \mathrm {f o r s o m e} k > 0 \} = \{x \in \ell_ {0}: \mathfrak {q} _ {\varphi , w} (k x) <   \infty \mathrm {f o r s o m e} k > 0 \}.} \end{array}
$$

The Luxemburg norm $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}$ and the Orlicz norm $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}^0$ [17, Theorem 8.8] are defined by

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} = \inf  \left\{\epsilon > 0: P _ {\varphi , w} \left(\frac {f}{\epsilon}\right) \leq 1 \right\} = \inf  \left\{\epsilon > 0: Q _ {\varphi , w} \left(\frac {f}{\epsilon}\right) \leq 1 \right\},
$$

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = \inf _ {k > 0} \left(\frac {1}{k} (1 + P _ {\varphi , w} (k f))\right) = \inf _ {k > 0} \left(\frac {1}{k} (1 + Q _ {\varphi , w} (k f))\right).
$$

The analogous norms for the sequence space $\mathfrak{m}_{\varphi, w}$ can be defined by replacing $P_{\varphi, w}$ (resp. $Q_{\varphi, w}$ ) with $\mathfrak{p}_{\varphi, w}$ (resp. $\mathfrak{q}_{\varphi, w}$ ). From now on, we denote the function (resp. sequence) space $\mathcal{M}_{\varphi, w}$ (resp. $\mathfrak{m}_{\varphi, w}$ ) equipped with the Luxemburg norm and the space $\mathcal{M}_{\varphi, w}^{0}$ (resp. $\mathfrak{m}_{\varphi, w}^{0}$ ) equipped with the Orlicz norm, respectively. We recall the relationship between the Orlicz-Lorentz spaces and the spaces $\mathcal{M}_{\varphi, w}$ .

Theorem 3.2. [8,12,17] Let $\varphi$ be an Orlicz function and $w$ be a locally integrable, non-negative decreasing weight function on $I = [0,\gamma)$ . Then the Kothe dual spaces of the Orlicz-Lorentz spaces $\Lambda_{\varphi,w}$ and $\Lambda_{\varphi,w}^{0}$ are given by $\Lambda_{\varphi,w}^{\prime} \simeq \mathcal{M}_{\varphi,*w}^{0}$ and $(\Lambda_{\varphi,w}^{0})^{\prime} \simeq \mathcal{M}_{\varphi,*w}$ . The similar facts are also true for the sequence spaces.

As we have seen earlier, working with the modulars $Q_{\varphi,w}$ and $\mathfrak{q}_{\varphi,w}$ involves Halperin's level functions. Let $f \in L_0$ where $f \geq 0$ and set $F(t_1,t_2) = \int_{t_1}^{t_2}f(x)dx$ , and $W(t_{1},t_{2}) = \int_{t_{1}}^{t_{2}}w(x)dx$ , where $0 \leq t_1 \leq t_2 \leq \gamma$ . An interval $(a,b]$ is said to be a level interval of $f$ if $\frac{F(a,t)}{W(a,t)} \leq \frac{F(a,b)}{W(a,b)}$ for every $t \in (a,b]$ . We say a level interval is maximal if it is not contained in other level intervals. Then the level function $f^0$ of $f$ is defined by

$$
f ^ {0} (t) = \left\{ \begin{array}{l l} \frac {F (a , b)}{W (a , b)} w (t), & t \in (a, b) \mathrm {f o r e a c h m a x i m a l l e v e l i n t e r v a l} (a, b), \\ f (t), & t \notin \cup (a, b). \end{array} \right.
$$

The level sequences can be also defined in a similar way. There are countably many maximal level intervals, and if $f^0$ is a non-negative, locally integrable function, we can express $f^0 = Dw$ where $D$ is a decreasing function [8, 9, 22].

Let $w$ be a weight function. A non-negative function $L$ on $I$ is $w$ -affine if $L(t) = cW(t) + d$ for $c, d \in \mathbb{R}$ . An increasing positive function $F$ on $I$ is said to be $w$ -concave if $L(t) \leq F(t)$ for all $t \in (a, b)$ , where $L$ is a $w$ -affine function such that $L(a) = F(a)$ and $L(b) = F(b)$ for all $0 \leq a < b < \gamma$ . If a function $F(t) = \int_0^t f$ is $w$ -concave, we can express the function $f$ as $f = Dw$ with some decreasing function $D$ [8, Theorem 2.1.(iii)]. For a positive function $f$ , consider $FW(t) = \int_0^t f(s)w(s)ds$ for $t \in I$ and its least $w$ -concave majorant denoted by $F^b$ . Then there exists $f^s$ such that $F^b(t) = \int_0^t f^s(s)w(s)ds$ because of the $w$ -concavity of $F^b$ . The function $f^s$ is called the level function in the sense of Sinnamon [25]. It is well-known that if $0 \leq f \leq g$ a.e. then $f^s \leq g^s$ a.e., and if $0 \leq f_n \uparrow f$ a.e. then $f_n^s \uparrow f^s$ a.e. [26]. We mention that such monotonicity and convergence properties were not explicitly stated for Halperin's level functions in the literature. However, the following relationship stated in [8] between Halperin's level functions and Sinnamon's level functions

$$
\frac {f ^ {0}}{w} = \left(\frac {f}{w}\right) ^ {s} a. e. \tag {1}
$$

provides us with the similar properties for the level functions defined by Halperin. Consequently,

Proposition 3.3. Let $f, f_n, g \in L_0$ be non-negative, locally integrable functions on $I$ and $w$ be a weight function. If $0 \leq f \leq g$ a.e., then $f^0 \leq g^0$ a.e. If $0 \leq f_n \uparrow f$ a.e., then $f_n^0 \uparrow f^0$ a.e. The analogous statement also holds for sequences.

Since the level function takes average values of $f$ over each maximal level intervals with respect to a weight function $w$ , the corresponding values of $f$ and $f^0$ may differ on these intervals. Hence, it is natural to ask when these two functions can be the same. Based on our observation so far, we can identify a certain type of functions which level functions are identical to themselves. These functions turn out to be useful in the next section.

Proposition 3.4. Let $f \in L_0$ be a decreasing, non-negative function and $w$ be a weight function. Then, $(fw)^0 = fw$ a.e. The analogous statement also holds for sequences.

Proof. First, we consider a decreasing simple function $f = \sum_{i=1}^{n} c_n \chi_{[t_{i-1}, t_i)}$ where $t_0 = 0$ and $c_1 > c_2 > \dots > c_n > 0$ . Denote $FW(t_{i-1}, t_i) = \int_{t_{i-1}}^{t_i} f w$ and $W(t_{i-1}, t_i) = \int_{t_{i-1}}^{t_i} w$ , $i = 1, \ldots, n$ . We claim that each subinterval $(t_{i-1}, t_i)$ is a maximal level interval. Observe that

$$
\frac {F W (0 , t)}{W (0 , t)} = \frac {c _ {1} W (0 , t)}{W (0 , t)} = c _ {1}
$$

for every $t \in (0, t_1)$ . So the interval $(0, t_1)$ is a level interval. Moreover, for every $t \in (t_{i-1}, t_i)$ , where $i = 2, 3, \ldots, n$ , notice that

$$
\frac {F W (0 , t)}{W (0 , t)} = \frac {c _ {1} W (0 , t _ {1}) + \cdots + c _ {i} W (t _ {i - 1} , t)}{W (0 , t)} <   c _ {1}.
$$

Hence, there is no level interval that contains $(0,t_{1})$ , and so the level interval $(0,t_{1})$ is maximal. By the similar procedure, we can also show that each subinterval $(t_{i - 1},t_i)$ is a maximal level interval. Thus, from the fact that

$$
(f w) ^ {0} (t) = \frac {F W (t _ {i - 1} , t _ {i})}{W (t _ {i - 1} , t _ {i})} w (t) = c _ {i} w (t) \text {f o r e v e r y} t \in (t _ {i - 1}, t _ {i}),
$$

we obtain

$$
\frac {(f w) ^ {0}}{w} = \sum_ {i = 1} ^ {n} c _ {i} \chi_ {[ t _ {i - 1}, t _ {i})} = f a. e.
$$

Now, let $f \in L_0$ be a non-negative, decreasing function. Then there exists a sequence of decreasing simple functions $(f_m)_{m=1}^{\infty}$ such that $f_m \uparrow f$ a.e. Since $f_m w \uparrow fw$ a.e., we see that $(f_m w)^0 = f_m w \uparrow fw$ a.e. But then, in view of Proposition 3.3, we have $(f_m w)^0 \uparrow (fw)^0$ a.e. Therefore, $(fw)^0 = fw$ a.e.

In this article, we always assume that $\varphi$ is an Orlicz function and that $w$ is a weight function. If there are results that only hold for $N$ -functions (at infinity), we will state them explicitly.

# 4. SEPARABILITY OF $\mathcal{M}_{\varphi, w}$ AND $\mathfrak{m}_{\varphi, w}$

In this section, we study the separability of the spaces $\mathcal{M}_{\varphi,w}$ and $\mathfrak{m}_{\varphi,w}$ . The results in this section will play an important role to study of M-embeddedness of Orlicz-Lorentz spaces. We mention that the same facts also hold for $\mathcal{M}_{\varphi,w}^{0}$ and $\mathfrak{m}_{\varphi,w}^{0}$ due to the equivalence of the Luxemburg and the Orlicz norms [12].

For convenience, we provide the explicit computation of $\frac{(c\chi_{[0,s)})^0}{w}$ , where $c > 0$ and $s \in I$ . Since the mapping $t \mapsto \frac{t}{W(t)}$ is increasing, notice that

$$
\frac {\left(c \chi_ {(0 , s)}\right) ^ {0} (t)}{w (t)} = \frac {c \cdot s}{W (s)} \chi_ {(0, s)} (t). \tag {2}
$$

Using (2) and the definition of $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}$ , we can directly compute the fundamental function $\phi_{\mathcal{M}_{\varphi ,w}}$ .

Lemma 4.1. [16, Proposition 4.9] (c.f. [14, Theorem 2.3] and [18, Proposition 2.2]) The fundamental function $\phi_{\mathcal{M}_{\varphi,w}}$ is expressed by

$$
\phi_ {\mathcal {M} _ {\varphi , w}} (t) = \frac {t}{W (t)} \Big / \frac {1}{\varphi^ {- 1} (1 / W (t))},
$$

where $\varphi^{-1}$ is the inverse function of $\varphi$ . Consequently, $\lim_{t\to 0 + }\phi_{\mathcal{M}_{\varphi ,w}}(t) = 0$

Now, we observe the relationship between $f \in \mathcal{M}_{\varphi, w}$ and its distribution function $d_f(\lambda)$ .

Proposition 4.2. If $f \in \mathcal{M}_{\varphi, w}$ , then the distribution function $d_f(\lambda) < \infty$ for all $\lambda > 0$ . The similar result holds for the sequence space $\mathfrak{m}_{\varphi, w}$ .

Proof. Let $f \in \mathcal{M}_{\varphi, w}$ . Then $Q_{\varphi, w}(kf) < \infty$ for some $k > 0$ . Since $f^*$ is equimeasurable to $f$ , we have $d_{f^*}(\lambda) = d_f(\lambda)$ for all $\lambda > 0$ . Given $\lambda > 0$ , define $g = \lambda \chi_{[0, a)}$ where $a = d_{f^*}(\lambda)$ . Notice that $g \leq f^*$ a.e. Then $\frac{g^0}{w} \leq \frac{(f^*)^0}{w}$ a.e. by Proposition 3.3. From (2), we see that

$$
\begin{array}{l} (3) \quad \varphi \left(\frac {k \lambda a}{W (a)}\right) W (a) = Q _ {\varphi , w} (k g) = \int_ {I} \varphi \left(\frac {k \lambda \left(\chi_ {(0 , a)}\right) ^ {0}}{w}\right) w \\ \leq \int_ {I} \varphi \left(\frac {k (f ^ {*}) ^ {0}}{w}\right) w = Q _ {\varphi , w} (k f) <   \infty . \\ \end{array}
$$

Since the function $t \mapsto \frac{t}{W(t)}$ is increasing, there exists $a_0 \in (0, a)$ such that $M_0 = \frac{a_0}{W(a_0)} \leq \frac{a}{W(a)}$ . Then we have

$$
\varphi (k \lambda M _ {0}) W (a) \leq \varphi \left(\frac {k \lambda a}{W (a)}\right) W (a).
$$

Now suppose that there exists $\lambda > 0$ such that $d_{f}(\lambda) = d_{f^{*}}(\lambda) = \infty$ . From the assumption that $W(\infty) = \infty$ , we see that $\varphi(k\lambda M_0)W(a) = \infty$ . This is a contradiction because $Q_{\varphi, w}(kf) < \infty$ . Therefore, $d_{f}(\lambda) < \infty$ for all $\lambda > 0$ .

Also we need to examine the relationship between the norm $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}$ and the modular $P_{\varphi ,w}$

Proposition 4.3. If $\|f\|_{\mathcal{M}_{\varphi, w}} \leq 1$ , then $P_{\varphi, w}(f) \leq Q_{\varphi, w}(f) \leq \|f\|_{\mathcal{M}_{\varphi, w}}$ . The analogous statement for the space $\mathfrak{m}_{\varphi, w}$ also holds.

Proof. Let $f \in \mathcal{M}_{\varphi, w}$ . From the definition of the Luxemburg norm, there exists a sequence of real numbers $(\lambda_n) \downarrow \|f\|_{\mathcal{M}_{\varphi, w}}$ such that $Q_{\varphi, w}\left(\frac{f}{\lambda_n}\right) \leq 1$ . Then $\frac{f^*}{\|\mathbf{f}\|_{\mathcal{M}_{\varphi, w}}} \uparrow \frac{f^*}{\|\mathbf{f}\|_{\mathcal{M}_{\varphi, w}}}$ a.e. Furthermore, $\frac{(f^*)^0}{\lambda_n} \uparrow \frac{(f^*)^0}{\|\mathbf{f}\|_{\mathcal{M}_{\varphi, w}}}$ a.e. from Proposition 3.3. So $\varphi\left(\frac{(f^*)^0}{\lambda_n}\right)w \uparrow \varphi\left(\frac{(f^*)^0}{\|\mathbf{f}\|_{\mathcal{M}_{\varphi, w}}}\right)w$ a.e. By the Monotone Convergence Theorem,

$$
Q _ {\varphi , w} \left(\frac {f}{\| f \| _ {\mathcal {M} _ {\varphi , w}}}\right) = \int_ {I} \varphi \left(\frac {(f ^ {*}) ^ {0}}{\| f \| _ {\mathcal {M} _ {\varphi , w}}}\right) w = \lim  _ {n \rightarrow \infty} \int_ {I} \varphi \left(\frac {(f ^ {*}) ^ {0}}{\lambda_ {n}}\right) w \leq 1.
$$

Hence by the convexity of $\varphi$ , we obtain

$$
\frac {P _ {\varphi , w} (f)}{\| f \| _ {\mathcal {M} _ {\varphi , w}}} \leq \frac {Q _ {\varphi , w} (f)}{\| f \| _ {\mathcal {M} _ {\varphi , w}}} \leq Q _ {\varphi , w} \left(\frac {f}{\| f \| _ {\mathcal {M} _ {\varphi , w}}}\right) \leq 1.
$$

![](images/6397784d669018ed11109c5a29325c0423a9cc7665bab98ed090226a34c1e91c.jpg)

Proposition 4.4. Let $(f_n)_{n=1}^{\infty}$ be a sequence in $\mathcal{M}_{\varphi, w}$ . Then, $\lim_{n \to \infty} \| f_n \|_{\mathcal{M}_{\varphi, w}} = 0$ if and only if $\lim_{n \to \infty} P_{\varphi, w}(k f_n) = \lim_{n \to \infty} Q_{\varphi, w}(k f_n) = 0$ for every $k > 0$ . The analogous statement holds for the space $\mathfrak{m}_{\varphi, w}$ .

Proof. Suppose that $\lim_{n\to \infty}\| f_n\|_{\mathcal{M}_{\varphi ,w}} = 0$ and fix $k > 0$ . Then for every $c > \max \{1,\frac{1}{k}\}$ , there exists $N(c)\in \mathbb{N}$ such that for every $n\geq N(c)$ , $\| ckf_n\|_{\mathcal{M}_{\varphi ,w}}\leq 1$ . By Proposition 4.3, this implies that $Q_{\varphi ,w}(ckf_n)\leq 1$ for every $n\geq N(c)$ . Now by the convexity of $\varphi$ , we see that $cP_{\varphi ,w}(kf_n)\leq cQ_{\varphi ,w}(kf_n)\leq Q_{\varphi ,w}(ckf_n)\leq 1$ , and so $P_{\varphi ,w}(kf_n)\leq Q_{\varphi ,w}(kf_n)\leq \frac{1}{c}$ for every $n\geq N(c)$ . Since $c > \max \{1,\frac{1}{k}\}$ is arbitrary, we obtain $\lim_{n\to \infty}P_{\varphi ,w}(kf_n) = \lim_{n\to \infty}Q_{\varphi ,w}(kf_n) = 0$ for every $k > 0$ .

To show the converse, suppose that for every $k > 0$ , $\lim_{n\to \infty}P_{\varphi ,w}(kf_n) = \lim_{n\to \infty}Q_{\varphi ,w}(kf_n) = 0$ . Then for every $c > \max \{1,\frac{1}{k}\}$ , there exists $N(c)$ such that for every $n\geq N(c)$ , $Q_{\varphi ,w}(kf_n)\leq \frac{1}{c}$ . By the convexity of $Q_{\varphi ,w}$ and the definition of $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}$ , this implies that $\| f_n\|_{\mathcal{M}_{\varphi ,w}}\leq \frac{1}{ck}$ for every $n\geq N(c)$ . Since $c > \max \{1,\frac{1}{k}\}$ is arbitrary, we have $\lim_{n\to \infty}\| f_n\|_{\mathcal{M}_{\varphi ,w}} = 0$ .

The sequence case can be proven by the similar argument, so we omit the proof.

Proposition 4.5. Let $f \in L_0$ be a bounded function with support of finite measure. Then $P_{\varphi, w}(kf) \leq Q_{\varphi, w}(kf) < \infty$ for every $k > 0$ . The analogous statement also holds for a sequence $x \in \ell_0$ with finite entries.

Proof. Let $f \in L_0$ be a bounded function with support of finite measure, that is $|f(t)| \leq c$ a.e. on $I$ for some $c > 0$ , and let $k > 0$ . Since $f$ is equimeasurable to $f^*$ , we see that $f^* \leq c$ a.e. on $(0, m(\operatorname{supp} f^*))$ where both $c$ and $m(\operatorname{supp} f^*)$ are finite. By Proposition 3.3, we have $\varphi\left(\frac{k(f^*)^0}{w}\right) w \leq \varphi\left(\frac{kc(\chi_{(0,m(\operatorname{supp} f^*))})^0}{w}\right) w$ a.e. Hence, we have from (2) that

$$
\begin{array}{l} P _ {\varphi , w} (k f) \leq Q _ {\varphi , w} (k f) = \int_ {I} \varphi \left(\frac {k \left(f ^ {*}\right) ^ {0}}{w}\right) w \leq \int_ {I} \varphi \left(\frac {k c \left(\chi_ {\left(0 , m (\operatorname {s u p p} f ^ {*})\right)}\right) ^ {0}}{w}\right) w \\ = \varphi \left(\frac {k c (m (\operatorname {s u p p} f ^ {*}))}{W (m (\operatorname {s u p p} f ^ {*}))}\right) W (m (\operatorname {s u p p} f ^ {*})) <   \infty , \\ \end{array}
$$

and so $P_{\varphi, w}(kf) \leq Q_{\varphi, w}(kf) < \infty$ for every $k > 0$ .

We recall the following auxiliary lemma that will be useful later.

Lemma 4.6. [8, Lemma 6.5] If $0 \leq f_n \leq f = f^* \in \mathcal{M}_{\varphi, w}$ such that $f_n = f_n^*$ for every $n \in \mathbb{N}$ , $m(\operatorname{supp} f_n) < \infty$ , and $f_n \to 0$ a.e., then $f_n^0 \to 0$ a.e. The same result holds for the sequence case.

We are ready to provide an explicit description of the order-continuous subspace of $\mathcal{M}_{\varphi, w}$ .

Theorem 4.7. For the function space $\mathcal{M}_{\varphi, w}$ ,

$$
\begin{array}{l} \left(\mathcal {M} _ {\varphi , w}\right) _ {a} = \left(\mathcal {M} _ {\varphi , w}\right) _ {b} = \{f \in L _ {0}: P _ {\varphi , w} (k f) <   \infty \text {f o r a l l} k > 0 \} \\ = \{f \in L _ {0}: Q _ {\varphi , w} (k f) <   \infty \text {f o r a l l} k > 0 \}. \\ \end{array}
$$

For the sequence space $\mathfrak{m}_{\varphi ,w}$

$$
\begin{array}{l} \left(\mathfrak {m} _ {\varphi , w}\right) _ {a} = \left(\mathfrak {m} _ {\varphi , w}\right) _ {b} = \{x \in \ell_ {0}: \mathfrak {p} _ {\varphi , w} (k x) <   \infty \text {f o r a l l} k > 0 \} \\ = \{x \in \ell_ {0}: \mathfrak {q} _ {\varphi , w} (k x) <   \infty \text {f o r a l l} k > 0 \}. \\ \end{array}
$$

Proof. We already have $(\mathcal{M}_{\varphi, w})_a = (\mathcal{M}_{\varphi, w})_b$ from Lemma 4.1 and [2, Theorem 2.5.5], so we only have to show the second and third equalities of the statement. Let $f \in (\mathcal{M}_{\varphi, w})_b$ . Then there exists a sequence $(f_n)_{n=1}^{\infty}$ of simple functions with supports of finite measure such that $\| f - f_n \|_{\mathcal{M}_{\varphi, w}} \to 0$ . From Proposition 4.4, we see that $Q_{\varphi, w}(2k(f - f_n)) \to 0$ for every $k > 0$ . Hence for given $\epsilon > 0$ , there exists $n \in \mathbb{N}$ such that $Q_{\varphi, w}(2k(f - f_n)) < \epsilon$ . By the convexity of $Q_{\varphi, w}$ and Proposition 4.5, we obtain

$$
\begin{array}{l} P _ {\varphi , w} (k f) \leq Q _ {\varphi , w} (k f) = Q _ {\varphi , w} \left(\frac {2 k f _ {n} + 2 k (f - f _ {n})}{2}\right) \leq \frac {1}{2} Q _ {\varphi , w} (2 k f _ {n}) + \frac {1}{2} Q _ {\varphi , w} (2 k (f - f _ {n})) \\ <   \frac {1}{2} Q _ {\varphi , w} (2 k f _ {n}) + \epsilon <   \infty . \\ \end{array}
$$

Thus,

$$
\begin{array}{l} \left(\mathcal {M} _ {\varphi , w}\right) _ {a} = \left(\mathcal {M} _ {\varphi , w}\right) _ {b} \subset \{f \in L _ {0}: Q _ {\varphi , w} (k f) <   \infty \text {f o r a l l} k > 0 \} \\ \subset \{f \in L _ {0}: P _ {\varphi , w} (k f) <   \infty \text {f o r a l l} k > 0 \}. \\ \end{array}
$$

Now, suppose $f \in L_0$ such that $Q_{\varphi, w}(kf) < \infty$ for every $k > 0$ . Define $f_n = f \chi_{\{\frac{1}{n} < |f| < n\}}$ . From Proposition 4.2, $m\{\frac{1}{n} < |f| < n\} \leq m\{|f| > \frac{1}{n}\} < \infty$ , so $f_n \in (\mathcal{M}_{\varphi, w})_b$ for all $n \in \mathbb{N}$ . Since $|f_n| \leq |f|$ a.e. and $f - f_n \to 0$ a.e., we have $(f - f_n)^* \to 0$ a.e. by Theorem 2.2. Moreover, $(f - f_n)^* \leq f^*$ a.e. [2, Proposition 1.7] and so $((f - f_n)^*)^0 \to 0$ a.e. and $((f - f_n)^*)^0 \leq (f^*)^0$ a.e. in view of Lemma 4.6 and Proposition 3.3. Hence for every $k > 0$ , $\varphi\left(\frac{k((f - f_n)^*)^0}{w}\right)w \to 0$ a.e. and $\varphi\left(\frac{k((f - f_n)^*)^0}{w}\right)w \leq \varphi\left(\frac{k((f^*)^0)}{w}\right)w$ a.e. By the Lebesgue Dominated Convergence Theorem, we have $Q_{\varphi, w}(k(f - f_n)) = \int_I \varphi\left(\frac{k((f - f_n)^*)^0}{w}\right)w \to 0$ . Then $\| f - f_n \|_{\mathcal{M}_{\varphi, w}} \to 0$ by Proposition 4.4, and this shows that $\{f \in L_0 : Q_{\varphi, w}(kf) < \infty \text{ for all } k > 0\} \subset (\mathcal{M}_{\varphi, w})_a = (\mathcal{M}_{\varphi, w})_b$ .

For $f \in L_0$ such that $P_{\varphi, w}(kf) < \infty$ for every $k > 0$ , we define the functions $f_n \in (\mathcal{M}_{\varphi, w})_b$ as before. Then for every $\epsilon > 0$ , there exists $v_\epsilon \prec w$ such that

$$
\int_ {I} \varphi \left(\frac {k f ^ {*}}{v _ {\epsilon}}\right) v _ {\epsilon} \leq P _ {\varphi , w} (k f) + \epsilon <   \infty .
$$

From the fact that $|f - f_n| \leq |f|$ a.e., we have $(f - f_n)^* \leq f^*$ a.e. [2, Proposition 1.7], and so $\int_I \varphi \left( \frac{k(f - f_n)^*}{v_\epsilon} \right) v_\epsilon \leq \int_I \varphi \left( \frac{k f^*}{v_\epsilon} \right) v_\epsilon < \infty$ . Since $\varphi \left( \frac{k(f - f_n)^*}{v_\epsilon} \right) v_\epsilon \to 0$ a.e. as $n \to \infty$ , by the

Lebesgue Dominated Convergence Theorem, $\int_{I}\varphi \left(\frac{k(f - f_n)^*}{v_\epsilon}\right)v_\epsilon \to 0$ as $n\to \infty$ . This implies that

$$
P _ {\varphi , w} (k (f - f _ {n})) \leq \int_ {I} \varphi \left(\frac {k (f - f _ {n}) ^ {*}}{v _ {\epsilon}}\right) v _ {\epsilon} \rightarrow 0,
$$

as $n\to \infty$ . Thus by Proposition 4.4, $\| f - f_n\|_{\mathcal{M}_{\varphi ,w}}\to 0$ , and so we have $\{f\in L_0:P_{\varphi ,w}(kf) < \infty$ for all $k > 0\} \subset (\mathcal{M}_{\varphi ,w})_a = (\mathcal{M}_{\varphi ,w})_b$

For the sequence spaces, we always have $(\mathfrak{m}_{\varphi ,w})_a = (\mathfrak{m}_{\varphi ,w})_b$ [2, Theorem 2.5.4]. By replacing $P_{\varphi ,w}$ with $\mathfrak{p}_{\varphi ,w}$ and $Q_{\varphi ,w}$ with $\mathfrak{q}_{\varphi ,w}$ , we can prove the second equality by the similar argument.

The following observation will be useful.

Corollary 4.8. If $f \in (\mathcal{M}_{\varphi, w})_a$ such that $\|f\|_{\mathcal{M}_{\varphi, w}} = 1$ , then $P_{\varphi, w}(f) = Q_{\varphi, w}(f) = 1$ . The analogous statement holds for the sequence $x \in (\mathfrak{m}_{\varphi, w})_a$ with $\|x\|_{\mathfrak{m}_{\varphi, w}} = 1$ .

Proof. In view of Theorem 4.7, for $f \in (\mathcal{M}_{\varphi,w})_a$ , the mapping $k \mapsto P_{\varphi,w}(kf)$ is continuous on $[0,\infty)$ , and $\lim_{k \to \infty} P_{\varphi,w}(kf) = \infty$ . Hence, there exists $k_0$ such that $P_{\varphi,w}(k_0f) = 1$ . By the definition of the Luxemburg norm of $\mathcal{M}_{\varphi,w}$ , we must have $k_0 = \|f\|_{\mathcal{M}_{\varphi,w}} = 1$ . By considering the continuous mapping $k \mapsto Q_{\varphi,w}(kf)$ on $[0,\infty)$ with $\lim_{k \to \infty} Q_{\varphi,w}(kf) = \infty$ , we can also show that $Q_{\varphi,w}(f) = 1$ .

Before presenting the main results of this section, we need the following auxiliary results.

Lemma 4.9. If $\varphi$ does not satisfy the appropriate $\Delta_2$ -condition, there exists $f \in \mathcal{M}_{\varphi,w}$ such that $Q_{\varphi,w}(f) \leq 1$ but $Q_{\varphi,w}(rf) = \infty$ for $r > 1$ . The similar result holds for the space $\mathfrak{m}_{\varphi,w}$ .

Proof. Since the proof for the infinite Lebesgue measure space is similar to the finite Lebesgue measure space case, we only consider when $\gamma < \infty$ . In this case, we have $\int_0^\gamma w = W(\gamma) < \infty$ . Assume that $\varphi$ does not satisfy the $\Delta_2^\infty$ -condition. Then by Lemma 3.1, there exists an increasing sequence of real numbers $(u_n)_{n=1}^\infty$ with $u_n \uparrow \infty$ such that

$$
\varphi \left(\left(1 + \frac {1}{n}\right) u _ {n}\right) > 2 ^ {n} \varphi (u _ {n}) \quad \text {f o r e v e r y} n \in \mathbb {N}. \tag {4}
$$

Choose $u_{1}$ that satisfies $\frac{1}{\varphi(u_1)} < W(\gamma)$ . Since $\sum_{n=1}^{\infty} \frac{1}{2^n \varphi(u_n)} \leq \frac{1}{\varphi(u_1)} < W(\gamma)$ , there exists $t_0 \in (0, \gamma)$ such that $W(t_0) = \sum_{n=1}^{\infty} \frac{1}{2^n \varphi(u_n)}$ . Hence we can choose $t_n \downarrow 0$ such that $\frac{1}{2^n \varphi(u_n)} = \int_{t_n}^{t_{n-1}} w$ for every $n \in \mathbb{N}$ . Let $(t_{n_i})_{i=1}^{\infty}$ be a subsequence of $(t_n)_{n=1}^{\infty}$ such that $\sum_{i=0}^{\infty} t_{n_i} < \gamma$ , where $t_{n_0} = t_0$ . For $k \in \mathbb{N}$ , define

$$
f _ {k} = \sum_ {n = n _ {k} + 1} ^ {\infty} u _ {n} w \chi_ {[ t _ {n} + \sum_ {i = 0} ^ {k - 1} t _ {n _ {i}}, t _ {n - 1} + \sum_ {i = 0} ^ {k - 1} t _ {n _ {i}}) ].}
$$

Notice that $\operatorname{supp} f_k \subset \left[\sum_{i=0}^{k-1} t_{n_i}, \sum_{i=0}^k t_{n_i}\right)$ and that $\operatorname{supp} f_k$ 's are pairwise disjoint.

Due to our choice of $u_{n}$ and $w$ being decreasing, we see that $f_{k}^{*} = \sum_{n = n_{k} + 1}^{\infty}u_{n}w\chi_{[t_{n},t_{n - 1})}$ and $\frac{f_k^*}{w} = \sum_{n = n_k + 1}^{\infty}u_n\chi_{[t_n,t_{n - 1})}$ are decreasing functions, so $f_{k}^{*} = (f_{k}^{*})^{0}$ by Proposition 3.4. Hence we obtain

$$
Q _ {\varphi , w} (f _ {k}) = \int_ {I} \varphi \left(\frac {(f _ {k} ^ {*}) ^ {0}}{w}\right) w = \sum_ {n = n _ {k} + 1} ^ {\infty} \varphi (u _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} w = \frac {1}{2 ^ {n _ {k}}} \leq \frac {1}{2 ^ {k}}.
$$

Now, let $s > 1$ . Then there exists $j_0$ such that for all $n > j_0$ , $1 + \frac{1}{n} < s$ . Let $k \in \mathbb{N}$ and $N = \max \{j_0, n_k + 1\}$ . For every $n \geq N$ , by (4), we have

$$
Q _ {\varphi , w} (s f _ {k}) = \sum_ {n = n _ {k} + 1} ^ {\infty} \varphi (s u _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} w \geq \sum_ {n = N} ^ {\infty} \varphi \left(\left(1 + \frac {1}{n}\right) u _ {n}\right) \int_ {t _ {n}} ^ {t _ {n - 1}} w > \sum_ {n = N} ^ {\infty} \frac {2 ^ {n} \varphi (u _ {n})}{2 ^ {n} \varphi (u _ {n})} = \infty .
$$

Hence $\| f_k\|_{\mathcal{M}_{\varphi ,w}} = 1$

Lemma 4.10. If $\varphi$ does not satisfy the appropriate $\Delta_{2}$ -condition, there exists $f\in \mathcal{M}_{\varphi ,w}$ such that $P_{\varphi ,w}(f)\leq 1$ but $P_{\varphi ,w}(rf) = \infty$ for $r > 1$ . The similar result holds for the space $\mathfrak{m}_{\varphi ,w}$ .

Proof. Since the proof for the infinite Lebesgue measure space is similar to the finite Lebesgue measure space case, we only consider when $\gamma < \infty$ . Fix a decreasing function $v \prec w$ . In this case, we have $\int_0^\gamma v = V(\gamma) \leq W(\gamma) < \infty$ . Assume that $\varphi$ does not satisfy the $\Delta_2^\infty$ -condition. Then by Lemma 3.1, there exists an increasing sequence of real numbers $(u_n)_{n=1}^\infty$ with $u_n \uparrow \infty$ such that

$$
\varphi \left(\left(1 + \frac {1}{n}\right) u _ {n}\right) > 2 ^ {n} \varphi \left(u _ {n}\right) \quad \text {f o r e v e r y} n \in \mathbb {N}. \tag {5}
$$

Choose $u_{1}$ that satisfies $\frac{1}{\varphi(u_1)} < V(\gamma)$ . Since $\sum_{n=1}^{\infty} \frac{1}{2^n \varphi(u_n)} \leq \frac{1}{\varphi(u_1)} < V(\gamma)$ , there exists $t_0 \in (0, \gamma)$ such that $V(t_0) = \sum_{n=1}^{\infty} \frac{1}{2^n \varphi(u_n)}$ . Hence we can choose $t_n \downarrow 0$ such that $\frac{1}{2^n \varphi(u_n)} = \int_{t_n}^{t_{n-1}} v$ for every $n \in \mathbb{N}$ . Let $(t_{n_i})_{i=1}^{\infty}$ be a subsequence of $(t_n)_{n=1}^{\infty}$ such that $\sum_{i=0}^{\infty} t_{n_i} < \gamma$ , where $t_{n_0} = t_0$ . For $k \in \mathbb{N}$ , define

$$
f _ {k} = \sum_ {n = n _ {k} + 1} ^ {\infty} u _ {n} v \chi_ {[ t _ {n} + \sum_ {i = 0} ^ {k - 1} t _ {n _ {i}}, t _ {n - 1} + \sum_ {i = 0} ^ {k - 1} t _ {n _ {i}}) ].}
$$

Notice that $\operatorname{supp} f_k \subset \left[\sum_{i=0}^{k-1} t_{n_i}, \sum_{i=0}^k t_{n_i}\right)$ and that $\operatorname{supp} f_k$ 's are pairwise disjoint.

Due to our choice of $u_{n}$ and $v$ being decreasing, we see that $f_{k}^{*} = \sum_{n = n_{k} + 1}^{\infty}u_{n}v\chi_{[t_{n},t_{n - 1})}$ and $\frac{f_k^*}{v} = \sum_{n = n_k + 1}^{\infty}u_n\chi_{[t_n,t_{n - 1})}$ . Hence we obtain

$$
P _ {\varphi , w} (f _ {k}) \leq \int_ {I} \varphi \left(\frac {f _ {k} ^ {*}}{v}\right) v = \sum_ {n = n _ {k} + 1} ^ {\infty} \varphi (u _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} v = \frac {1}{2 ^ {n _ {k}}} \leq \frac {1}{2 ^ {k}}.
$$

Now, let $s > 1$ . Then there exists $j_0$ such that for all $n > j_0$ , $1 + \frac{1}{n} < s$ . Let $k \in \mathbb{N}$ and $N = \max \{j_0, n_k + 1\}$ . For $n \geq N$ , by (5), we have

$$
\sum_ {n = n _ {k} + 1} ^ {\infty} \varphi (s u _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} v \geq \sum_ {n = N} ^ {\infty} \varphi \left(\left(1 + \frac {1}{n}\right) u _ {n}\right) \int_ {t _ {n}} ^ {t _ {n - 1}} v > \sum_ {n = N} ^ {\infty} \frac {2 ^ {n} \varphi (u _ {n})}{2 ^ {n} \varphi (u _ {n})} = \infty .
$$

Since this is true for every decreasing $v \prec w$ , $P_{\varphi, w}(sf_k) = \infty$ for every $s > 1$ . Therefore, $\| f_k \|_{\mathcal{M}_{\varphi, w}} = 1$ .

Theorem 4.11. If $\varphi$ does not satisfy the appropriate $\Delta_2$ -condition, there exists a sequence of non-negative functions $f_{k} \in \mathcal{M}_{\varphi,w}$ with pairwise disjoint supports such that $\| f_k \|_{\mathcal{M}_{\varphi,w}} = 1$ and $\| \sum_{k=1}^{\infty} f_k \|_{\mathcal{M}_{\varphi,w}} = 1$ for every $k \in \mathbb{N}$ . The similar result holds for the space $\mathfrak{m}_{\varphi,w}$ .

Proof. Let $(f_k)_{k=1}^{\infty}$ be the sequence of pairwise disjoint functions constructed in Lemma 4.9. In order to show $\| \sum_{k=1}^{\infty} f_k \|_{\mathcal{M}_{\varphi, w}} = 1$ , observe that $1 = \| f_k \|_{\mathcal{M}_{\varphi, w}} \leq \left\| \sum_{k=1}^{\infty} f_k \right\|_{\mathcal{M}_{\varphi, w}}$ . Let $r > 1$ . Since $Q_{\varphi, w}(rf_k) = \infty$ for all $k$ , we have

$$
Q _ {\varphi , w} \left(r \sum_ {k = 1} ^ {\infty} f _ {k}\right) \geq Q _ {\varphi , w} (r f _ {k}) = \infty .
$$

Thus, $\| \sum_{k=1}^{\infty} f_k \|_{\mathcal{M}_{\varphi, w}} = 1$ . The same statement can be proven by using the sequence of $(f_k)_{k=1}^{\infty}$ constructed in Lemma 4.10 if one wishes to prove it in terms of the modular $P_{\varphi, w}$ .

Since the analogous result for the space $\mathfrak{m}_{\varphi, w}$ can be shown with the similar method, we omit the proof.

Now, we are ready to prove the main result of this section. Even though the implication (ii) $\Rightarrow$ (i) of the next theorem was already shown in [8, Theorem 6.7], we prove this with a different method. More importantly, we can see that the reverse implication also holds.

Theorem 4.12. The following statements are equivalent:

(i) $\mathcal{M}_{\varphi, w} = \{f \in L_0 : Q_{\varphi, w}(kf) < \infty \text{ for all } k > 0\} = \{f \in L_0 : P_{\varphi, w}(kf) < \infty \text{ for all } k > 0\}$ .   
(ii) $\varphi$ satisfies the appropriate $\Delta_{2}$ -condition.

Proof. Assume to the contrary that $\varphi$ does not satisfy the appropriate $\Delta_{2}$ -condition. Then by Lemma 4.10, there exists $f \in \mathcal{M}_{\varphi,w}$ such that $P_{\varphi,w}(f) \leq 1$ and $P_{\varphi,w}(2f) = \infty$ . Hence $f \notin \{f \in L_0 : P_{\varphi,w}(kf) < \infty \text{ for all } k > 0\}$ . Moreover, since $\{f \in L_0 : Q_{\varphi,w}(kf) < \infty \text{ for all } k > 0\} \subset \{f \in L_0 : P_{\varphi,w}(kf) < \infty \text{ for all } k > 0\}$ in general, we also see that $f \notin \{f \in L_0 : Q_{\varphi,w}(kf) < \infty \text{ for all } k > 0\}$ . This shows (i) $\Rightarrow$ (ii).

To prove (ii) $\Rightarrow$ (i), we only present the proof in regards to finite measure spaces because the proof for infinite measure spaces can be modified easily. Suppose that $\varphi$ satisfies the $\Delta_2^\infty$ -condition. Then there exist $K > 0$ and $u_0 \geq 0$ such that $\varphi(2u) \leq K\varphi(u)$ for every $u \geq u_0$ .

Let $f \in \mathcal{M}_{\varphi, w}$ . Then $Q_{\varphi, w}(kf) < \infty$ for some $k > 0$ . It is enough to show that $P_{\varphi, w}(2kf) < \infty$ . Define a set $A = \left\{\frac{(f^*)^0}{w} \geq \frac{u_0}{k}\right\}$ . There exists $0 < c \leq \gamma$ such that $A = (0, c) \subset I$ because $\frac{(f^*)^0}{w}$ is decreasing. From the fact that $\frac{(f^*)^0}{w} < \frac{u_0}{k}$ on $(c, \gamma)$ and the $\Delta_2^\infty$ -condition of $\varphi$ , we have

$$
\begin{array}{l} {Q _ {\varphi , w} (2 k f) = \int_ {I} \varphi \left(\frac {2 k (f ^ {*}) ^ {0}}{w}\right) w} = {\int_ {0} ^ {c} \varphi \left(\frac {2 k (f ^ {*}) ^ {0}}{w}\right) w + \int_ {c} ^ {\gamma} \varphi \left(\frac {2 k (f ^ {*}) ^ {0}}{w}\right) w} \\ \leq K \int_ {0} ^ {c} \varphi \left(\frac {k (f ^ {*}) ^ {0}}{w}\right) w + \varphi (2 u _ {0}) (W (\gamma) - W (c)) \\ \leq K Q _ {\varphi , w} (k f) + \varphi (2 u _ {0}) (W (\gamma) - W (c)) <   \infty . \\ \end{array}
$$

Hence, $P_{\varphi ,w}(2kf) <   \infty$

![](images/ac9c618c59c191e429379584ad57b75de153acc13cac67d69de29126cb541e6d.jpg)

We have the analogous result for the sequence spaces.

Theorem 4.13. The following statements are equivalent:

(i) $\mathfrak{m}_{\varphi ,w} = \{x\in \ell_0:\mathfrak{p}_{\varphi ,w}(\lambda x) <   \infty \text{for all}\lambda >0\} = \{x\in \ell_0:\mathfrak{q}_{\varphi ,w}(\lambda x) <   \infty \text{for all}\lambda >0\}$   
(ii) $\varphi$ satisfies $\Delta_2^0$ -condition.

Hence we have the following consequence of Theorem 4.12 and Theorem 4.13.

Corollary 4.14. The function space $\mathcal{M}_{\varphi, w}$ is separable if and only if $\varphi$ satisfies the appropriate $\Delta_2$ -condition. The sequence space $\mathfrak{m}_{\varphi, w}$ is separable if and only if $\varphi$ satisfies the $\Delta_2^0$ -condition.

Proof. From Corollary 4.12, $\varphi$ satisfies the appropriate $\Delta_{2}$ -condition if and only if $\mathcal{M}_{\varphi,w} = \{f \in L_0 : P_{\varphi,w}(\lambda f) < \infty \text{ for all } \lambda > 0\} = \{f \in L_0 : Q_{\varphi,w}(\lambda f) < \infty \text{ for all } \lambda > 0\}$ . In view of Theorem 4.7, $\mathcal{M}_{\varphi,w} = (\mathcal{M}_{\varphi,w})_a = (\mathcal{M}_{\varphi,w})_b$ , so the space $\mathcal{M}_{\varphi,w}$ is order-continuous. Since the Lebesgue measure $m$ is separable, the space $\mathcal{M}_{\varphi,w}$ is also separable [2, Theorem 1.5.5].

For the space $\mathfrak{m}_{\varphi, w}$ , from Theorem 4.13, $\varphi$ satisfies the $\Delta_2^0$ -condition if and only if $\mathfrak{m}_{\varphi, w} = \{x \in \ell_0 : \mathfrak{p}_{\varphi, w}(\lambda x) < \infty \text{ for all } \lambda > 0\} = \{x \in \ell_0 : \mathfrak{q}_{\varphi, w}(\lambda x) < \infty \text{ for all } \lambda > 0\}$ . By Theorem 4.7, $\mathfrak{m}_{\varphi, w} = (\mathfrak{m}_{\varphi, w})_a = (\mathfrak{m}_{\varphi, w})_b$ is separable.

A Banach function lattice $X$ is a $KB$ -space if the space is order-continuous and has the Fatou property [24, Definition 5.1, pg 84]. In addition, we mention that a Banach function lattice $X$ is a $KB$ -space if and only if $X$ does not have an isomorphic copy of $c_{0}$ [1, Theorem 4.60].

Theorem 4.15. The following statements are equivalent:

(i) $\varphi$ satisfies the $\Delta_2$ -condition when $\gamma = \infty$ or $\varphi$ satisfies the $\Delta_2^\infty$ -condition when $\gamma < \infty$ (resp. $\varphi$ satisfies the $\Delta_2^0$ -condition);   
(ii) $\mathcal{M}_{\varphi ,w}$ (resp. $\mathfrak{m}_{\varphi ,w})$ does not have an isometric copy of $l^{\infty}$   
(iii) $\mathcal{M}_{\varphi ,w}$ (resp. $\mathfrak{m}_{\varphi ,w}$ ) does not have an isometric copy of $c_{0}$ ;   
(iv) $\mathcal{M}_{\varphi ,w}$ (resp. $\mathfrak{m}_{\varphi ,w})$ does not have an isomorphic copy of $c_{0}$   
(v) $\mathcal{M}_{\varphi ,w}$ (resp. $\mathfrak{m}_{\varphi ,w})$ is a KB-space;   
(vi) $\mathcal{M}_{\varphi ,w}$ (resp. $\mathfrak{m}_{\varphi ,w})$ is separable.

Proof. (iv) $\Rightarrow$ (iii) $\Rightarrow$ (ii) is clear. Since the Lebesgue measure $m$ is separable, the order-continuity of the space is equivalent to the separability of that space [2, Theorem 1.5.5]. Moreover, from the fact that the spaces $\mathcal{M}_{\varphi,w}$ and $\mathfrak{m}_{\varphi,w}$ have the Fatou property [16, Theorem 4.7], we obtain (v) $\Longleftrightarrow$ (vi). The implication (iv) $\Longleftrightarrow$ (v) is from [1, Theorem 4.60]. The implication (i) $\Longleftrightarrow$ (vi) was shown in Corollary 4.14.

Hence, we only have to show (ii) $\Rightarrow$ (i). Let $\varphi$ be an Orlicz function which does not satisfy the appropriate $\Delta_2$ -condition. In view of Theorem 4.11, let $(f_k)_{k=1}^{\infty}$ be a sequence of non-negative functions in $\mathcal{M}_{\varphi,w}$ with pairwise disjoint supports such that $\|f_k\|_{\mathcal{M}_{\varphi,w}} = 1$ and $\|\sum_{k=1}^{\infty} f_k\|_{\mathcal{M}_{\varphi,w}} = 1$ for every $k \in \mathbb{N}$ . Define an operator $T: l^{\infty} \to \mathcal{M}_{\varphi,w}$ such that $Tx = \sum_{k=1}^{\infty} |x(k)| f_k$ , where $x = (x(k))_{k=1}^{\infty} \in \ell_{\infty}$ . Then we get

$$
\| T x \| _ {\mathcal {M} _ {\varphi , w}} = \left\| \sum_ {k = 1} ^ {\infty} | x (k) | f _ {k} \right\| _ {\mathcal {M} _ {\varphi , w}} \leq \| x \| _ {\infty} \left\| \sum_ {k = 1} ^ {\infty} f _ {k} \right\| _ {\mathcal {M} _ {\varphi , w}} = \| x \| _ {\infty}.
$$

Observe that for any $0 < \lambda < 1$ , there exists $|x(k_0)|$ such that $\frac{|x(k_0)|}{\lambda \| x \|_{\infty}} > 1$ . Hence by Lemma 4.9, we have

$$
Q _ {\varphi , w} \left(\frac {\sum_ {k = 1} ^ {\infty} | x (k) | f _ {k}}{\lambda \| x \| _ {\infty}}\right) > Q _ {\varphi , w} \left(\frac {| x (k _ {0}) | f _ {k _ {0}}}{\lambda \| x \| _ {\infty}}\right) = \infty ,
$$

which shows that $\| Tx\|_{\mathcal{M}_{\varphi ,w}} = \| x\|_{\infty}$ . Thus, the space $\mathcal{M}_{\varphi ,w}$ contains an isometric copy of $l^{\infty}$ if $\varphi$ does not satisfy the appropriate $\Delta_2$ -condition. The proof is finished.

To show (ii) $\Rightarrow$ (i) for the space $\mathfrak{m}_{\varphi, w}$ , the similar argument from the function case is applied in view of Theorem 4.11 and Lemma 4.9.

We finish this section with an observation. A Banach space $X$ is said to have the Radon-Nikodym property with respect to $(\Omega, \Sigma, \mu)$ if for every $\mu$ -continuous vector measure $G: \Sigma \to X$ of bounded variation, there exists a Bochner integrable function $g: \Omega \to X$ such that $G(A) = \int_{A} g d\mu$ for every $A \in \Sigma$ . If this holds for every finite measure space $(\Omega, \Sigma, \mu)$ , then we say the space $X$ has the Radon-Nikodym property (RNP).

It is well-known that every separable dual space has the RNP, which in turn implies that the space has slices of arbitrarily small diameter (c.f. [6]). This property is in the opposite spectrum of Banach spaces with the Daugavet property and the diameter two properties, which have been active research areas in geometry of Banach spaces. In view of Theorem 4.14, we obtain the following consequence.

Theorem 4.16. Let $\varphi$ be an Orlicz $N$ -function at infinity that satisfies the appropriate $\Delta_2$ -condition. Then the space $\mathcal{M}_{\varphi, w}$ has the RNP. As a consequence, the unit ball of $\mathcal{M}_{\varphi, w}$ has slices of arbitrarily small diameters.

Proof. We claim that $\mathcal{M}_{\varphi, w}$ is a separable dual space. Since $\varphi$ is an $N$ -function at infinity, the complementary function $\varphi_*$ is finite [15], and so the inverse function $\varphi_*^{-1}$ is well-defined on $\mathbb{R}^+$ . It is well-known that the fundamental function of $\Lambda_{\varphi_*, w}$ equipped with the Luxemberg norm is

$$
\phi_ {\Lambda_ {\varphi_ {*}, w}} (t) = \| \chi_ {[ 0, t ]} \| _ {\Lambda_ {\varphi_ {*}, w}} = \frac {1}{\varphi_ {*} ^ {- 1} (1 / W (t))},
$$

where $W(t) = \int_0^t w(s)ds, t \in (0,\gamma)$ [14, 16]. Since the Luxemburg norm and the Orlicz norm are equivalent for Orlicz-Lorentz spaces (see pg 4), we have

$$
\lim  _ {t \to 0 +} \phi_ {\Lambda_ {\varphi_ {*}, w} ^ {0}} (t) \leq 2 \lim  _ {t \to 0 +} \phi_ {\Lambda_ {\varphi_ {*}, w}} (t).
$$

Hence, $\lim_{t\to 0 + }\phi_{\Lambda_{\varphi *,w}^0}(t) = 0$ , and so $(\Lambda_{\varphi *,w}^0)_a = (\Lambda_{\varphi *,w}^0)_b$ by [2, Theorem 2.5.5]. Moreover, from the fact that $\varphi = \varphi_{**}$ , we have $((\Lambda_{\varphi *,w}^0)_a)^* = (\Lambda_{\varphi *,w}^0)' = \mathcal{M}_{\varphi ,w}$ because $\mathcal{M}_{\varphi ,w}$ has the Fatou property. Therefore, the space $\mathcal{M}_{\varphi ,w}$ is a dual space. The separability is a direct consequence of Theorem 4.14. Thus the conclusion is proved.

Remark 4.17. For an arbitrary Orlicz function, in particular not being an $N$ -function at infinity, the analogous statement in Theorem 4.16 does not hold. For instance, if $\varphi(u) = ku$ for some $k > 0$ , then the space $\mathcal{M}_{\varphi,w}$ becomes $L_1$ . Since $L_1$ has the Daugavet property, the space does not have the RNP.

# 5. COMPARISON BETWEEN THE SPACES $\mathcal{M}_{\varphi, w}$

In this section, we study the comparison between $\mathcal{M}_{\varphi, w}$ spaces given by different Orlicz functions $\varphi$ . For this purpose, a certain order between Orlicz functions plays an important role. For two Orlicz functions $\varphi$ and $\psi$ , we denote the order $\varphi \prec \psi$ (resp. $\varphi \prec_{\infty} \psi$ ) if there exists $b > 0$ (resp. there exist $b > 0$ and $u_0 \geq 0$ ) such that $\varphi(u) \leq \psi(bu)$ for every $u \geq 0$ (resp. $u \geq u_0$ ) [23, Definition 2.2.1]. Using this order relation, the comparison results on Orlicz-Lorentz spaces were studied in [3, 11].

Theorem 5.1. Let $\varphi_{1}$ and $\varphi_{2}$ be Orlicz functions. Then the following statements are equivalent:

(i) $\varphi_1\prec \varphi_2$ (resp. $\varphi_{1}\prec_{\infty}\varphi_{2})$ when $\gamma = \infty$ (resp. $\gamma <  \infty$   
(ii) $\mathcal{M}_{\varphi_2,w}\hookrightarrow \mathcal{M}_{\varphi_1,w}.$

Proof. We only show the proof of the statement when $\gamma < \infty$ . Suppose that $\varphi_1 \prec_{\infty} \varphi_2$ . Let $f \in \mathcal{M}_{\varphi_2, w}$ . There exist $b > 0$ and $u_0 \geq 0$ such that $\varphi_1(u) \leq \varphi_2(bu)$ for every $u \geq u_0$ . Define a set $E = \{t \in I : (f^*)^0(t) \leq u_0 b \| f \|_{\mathcal{M}_{\varphi_2, w}} w(t)\}$ . From the fact that $\frac{(f^*)^0}{w}$ is a decreasing function, the set $E$ is actually the interval $[\gamma - mE, \gamma]$ . Let $M = \varphi_1(u_0)(W(\gamma) - W(\gamma - mE)) + 1$ . Since $Q_{\varphi, w}$ is a convex modular and $Q_{\varphi_2, w}\left(\frac{f}{\|f\|_{\mathcal{M}_{\varphi_2, w}}}\right) \leq 1$ ,

$$
\begin{array}{l} Q _ {\varphi_ {1}, w} \left(\frac {f}{M b \| f \| _ {\mathcal {M} _ {\varphi_ {2} , w}}}\right) = \int_ {I} \varphi_ {1} \left(\frac {(f ^ {*}) ^ {0}}{M b \| f \| _ {\mathcal {M} _ {\varphi_ {2} , w}}} w\right) w \\ \leq \frac {1}{M} \left(\int_ {\gamma - m E} ^ {\gamma} \varphi_ {1} \left(\frac {(f ^ {*}) ^ {0}}{b \| f \| _ {\varphi_ {2} , w} w}\right) w + \int_ {I} \varphi_ {1} \left(\frac {(f ^ {*}) ^ {0}}{b \| f \| _ {\varphi_ {2} , w} w}\right) w\right) \\ \leq \frac {1}{M} \left(\varphi_ {1} (u _ {0}) (W (\gamma) - W (\gamma - m E)) + \int_ {I} \varphi_ {2} \left(\frac {(f ^ {*}) ^ {0}}{\| f \| _ {\varphi_ {2 , w}} w}\right) w\right) \\ \leq \frac {1}{M} \cdot M = 1. \\ \end{array}
$$

Thus, we obtain $\| f\|_{\mathcal{M}_{\varphi_2,w}}\leq b\| f\|_{\mathcal{M}_{\varphi_1,w}}$ by the definition of the Luxemburg norm $\| \cdot \|_{\mathcal{M}_{\varphi ,w}}$ , and so $\mathcal{M}_{\varphi_2,w}\subset \mathcal{M}_{\varphi_1,w}$ . This shows (i) $\Rightarrow$ (ii).

For (ii) $\Rightarrow$ (i), assume to the contrary that $\varphi_{1} \not\prec_{\infty} \varphi_{2}$ . Then for every $\epsilon > 0$ , there exists a sequence of real numbers $(a_{n})_{n=1}^{\infty}\uparrow \infty$ such that $\varphi_{1}(a_{n}) > \varphi_{2}(2^{n}n^{2}a_{n})$ for every $n \in \mathbb{N}$ . We see from the convexity of the Orlicz function $\varphi_{2}$ that $\varphi_{1}(a_{n}) > \varphi_{2}(2^{n}n^{2}a_{n}) \geq 2^{n}\varphi_{2}(n^{2}a_{n})$ for all $n \in \mathbb{N}$ .

Passing to a subsequence if necessary, we can choose the sequence $(a_{n})_{n = 1}^{\infty}$ such that

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n} \varphi_ {2} \left(n ^ {2} a _ {n}\right)} <   \int_ {0} ^ {\gamma} w.
$$

Let $t_0$ be a positive real number such that

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n} \varphi_ {2} (n ^ {2} a _ {n})} = \int_ {0} ^ {t _ {0}} w.
$$

Then, there exists a sequence of real numbers $(t_n)_{n=1}^{\infty} \downarrow 0$ such that

$$
\frac {1}{2 ^ {n} \varphi_ {2} (n ^ {2} a _ {n})} = \int_ {t _ {n}} ^ {t _ {n - 1}} w.
$$

Now, define

$$
f := \sum_ {n = 1} ^ {\infty} n a _ {n} w \chi_ {[ t _ {n}, t _ {n - 1})}.
$$

By Proposition 3.4, we see that $f = f^{*} = (f^{*})^{0}$ . Hence,

$$
Q _ {\varphi_ {2}, w} (f) = \sum_ {n = 1} ^ {\infty} \varphi_ {2} (n a _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} w = \sum_ {n = 1} ^ {\infty} \frac {\varphi_ {2} (n a _ {n})}{2 ^ {n} \varphi_ {2} (n ^ {2} a _ {n})} <   \sum_ {n = 1} ^ {\infty} \frac {1}{2 ^ {n}} = 1.
$$

This shows that $f \in \mathcal{M}_{\varphi_2, w}$ . On the other hand, for every $\epsilon > 0$ there exists $n_0 \in \mathbb{N}$ such that $n_0 \epsilon > 1$ , so

$$
Q _ {\varphi_ {1}, w} (\epsilon f) \geq \sum_ {n = n _ {0} + 1} ^ {\infty} \varphi_ {1} (\epsilon n a _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} w \geq \sum_ {n = n _ {0} + 1} ^ {\infty} \varphi_ {1} (a _ {n}) \int_ {t _ {n}} ^ {t _ {n - 1}} w \geq \sum_ {n = n _ {0} + 1} ^ {\infty} \frac {2 ^ {n} \varphi_ {2} (n ^ {2} a _ {n})}{2 ^ {n} \varphi_ {2} (n ^ {2} a _ {n})} = \infty .
$$

Therefore, $f \notin \mathcal{M}_{\varphi_1,w}$ and so $\mathcal{M}_{\varphi_2,w} \not\subset \mathcal{M}_{\varphi_1,w}$ .

# 6. THE ORLICZ NORM IN $\mathcal{M}_{\varphi, w}$

From Theorem 3.2 and the fact that $\mathcal{M}_{\varphi, w}$ is r.i. [16, Theorem 4.7], we can also look at the Orlicz norm for $\mathcal{M}_{\varphi, w}$ as the Kőthe dual norm of $\Lambda_{\varphi_{*}, w}$ given by (6)

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = \sup  \left\{\int_ {I} | f g |: \rho_ {\varphi_ {*}, w} (g) \leq 1 \right\} = \sup  \left\{\int_ {I} f ^ {*} g ^ {*}: \rho_ {\varphi_ {*}, w} (g) \leq 1 \right\} = \inf  _ {k > 0} \left(\frac {1}{k} (1 + P _ {\varphi , w} (k f))\right).
$$

Now, we want to see when the infimum in (6) is achieved. If $\varphi$ is an $N$ -function, then $\varphi_*$ is also an $N$ -function [19] and its right-derivative $p(t) = \varphi_+^\prime(t) \to \infty$ as $t \to \infty$ . Also, we have $P_{\varphi, w}(f) = Q_{\varphi, w}(f)$ for every $f \in L_0$ [12, Theorem 4.7]. First, we define the interval $\bar{K}(f) = [\bar{k}^*, \bar{k}^{**}]$ and the constant $\bar{\theta}(f)$ for $f \in \mathcal{M}_{\varphi, w}$ by

$$
\bar {k} ^ {*} = \bar {k} ^ {*} (f) = \inf  \left\{k > 0: \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right) \geq 1 \right\},
$$

$$
\bar {k} ^ {* *} = \bar {k} ^ {* *} (f) = \sup  \left\{k > 0: \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right) \leq 1 \right\},
$$

$$
\bar {\theta} = \bar {\theta} (f) = \inf  \left\{\lambda > 0: P _ {\varphi , w} \left(\frac {f}{\lambda}\right) <   \infty \right\},
$$

In general, for $f \in \mathcal{M}_{\varphi, w}^{0} \setminus \{0\}$ we see that $0 < \bar{k}^{*} \leq \bar{k}^{**} \leq \infty$ . However, under our assumption on $\varphi$ , the interval $\bar{K}(f)$ is always bounded, as we show in the next result.

Lemma 6.1. If $\varphi$ is an $N$ -function, then $\bar{k}^{**}(f) < \infty$ for every $f \in \mathcal{M}_{\varphi, w}$ .

Proof. Assume to the contrary that $\bar{k}^{**} = \infty$ . Then $\rho_{\varphi_{*},w}\left(p\left(\frac{k(f^{*})^{0}}{w}\right)\right) \leq 1$ for every $k > 0$ . Let $\tilde{f} = \sum_{i=1}^{n} c_{n} \chi_{[t_{i-1}, t_{i})}$ , where $t_{0} = 0 < t_{1} < t_{2} < \dots < t_{n} < \infty$ be a decreasing simple function with support of finite measure such that $\tilde{f} \leq f^{*}$ a.e. Denote $\tilde{F}(a,b) = \int_{a}^{b} \tilde{f}$ . Then

$$
(\tilde {f}) ^ {0} (t) = \sum_ {j = 1} ^ {m} \frac {\tilde {F} \left(t _ {i _ {j - 1} , t _ {i _ {j}}}\right)}{W \left(t _ {i _ {j - 1} , t _ {i _ {j}}}\right)} w \chi_ {[ t _ {i _ {j - 1}, t _ {i _ {j}}})} (t),
$$

where $t_{i_0} = t_0 = 0$ and $t_{i_j} = t_s$ for some $s \in \{1, \dots, n\}$ , and $t_{i_1} < t_{i_2} < \dots < t_{i_m}$ . From Proposition 3.3, we have $p\left(\frac{k(\tilde{f})^0}{w}\right) \leq p\left(\frac{k(f^*)^0}{w}\right)$ a.e., and so

$$
\begin{array}{l} \int_ {0} ^ {t _ {i _ {1}}} \varphi_ {*} \left(p \left(\frac {k (\tilde {f}) ^ {0}}{w}\right)\right) w = \varphi_ {*} \left(p \left(\frac {k \tilde {F} (t _ {i _ {1}})}{W (t _ {i _ {1}})}\right)\right) W (t _ {i _ {1}}) \\ \leq \sum_ {j = 1} ^ {m} \varphi_ {*} \left(p \left(\frac {\tilde {F} (t _ {i _ {j - 1}} , t _ {i _ {j}})}{W (t _ {i _ {j - 1}} , t _ {i _ {j}})}\right)\right) W (t _ {i _ {j - 1}}, t _ {i _ {j}}) \\ = \int_ {I} \varphi_ {*} \left(p \left(\frac {k (\tilde {f}) ^ {0}}{w}\right)\right) w \\ \leq \int_ {I} \varphi_ {*} \left(p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right) w \leq 1, \\ \end{array}
$$

where $(0, t_{i_1})$ is the first maximal level interval of $\tilde{f}$ . Therefore,

$$
\varphi_ {*} \left(p \left(\frac {k \tilde {F} \left(t _ {i _ {1}}\right)}{W \left(t _ {i _ {1}}\right)}\right)\right) / p \left(\frac {k \tilde {F} \left(t _ {i _ {1}}\right)}{W \left(t _ {i _ {1}}\right)}\right) \leq 1 / \left(p \left(\frac {k \tilde {F} \left(t _ {i _ {1}}\right)}{W \left(t _ {i _ {1}}\right)}\right) W \left(t _ {i _ {1}}\right)\right).
$$

Since $\varphi$ is an $N$ -function, the complementary function $\varphi_*$ is also an $N$ -function. So $\lim_{u \to \infty} \frac{\varphi_*(u)}{u} = \infty$ . Moreover, $\lim_{t \to \infty} p(t) = \infty$ . Hence the left-hand side goes to infinity as $k \to \infty$ , but the right-hand side goes to 0 as $k \to \infty$ , which is a contradiction.

Lemma 6.2. Let $f \in \mathcal{M}_{\varphi, w}$ and $k > 0$ , $n \in \mathbb{N}$ . If $f_n = f \chi_{\{\frac{1}{n} < |f| \leq n\}}$ , then $\rho_{\varphi_*, w}\left(p\left(\frac{k(f_n^*)^0}{w}\right)\right) < \infty$ .

Proof. Let $f \in \mathcal{M}_{\varphi, w}$ and define $f_n = f \chi_{\{\frac{1}{n} < |f| \leq n\}}$ , $n \in \mathbb{N}$ . Since $f$ is equimeasurable to $f^*$ , by Proposition 4.2, $m\{\frac{1}{n} < f^* \leq n\} \leq m\{f^* > \frac{1}{n}\} < \infty$ for all $n \in \mathbb{N}$ . Let $c = m\{\frac{1}{n} < f^* \leq n\}$ . Hence each function $f_n$ is bounded with support of finite measure. Furthermore, notice that $f_n^* \leq n \chi_{(0, c)}$ a.e., so $(f_n^*)^0 \leq (n \chi_{(0, c)})^0$ a.e. by Proposition 3.3. Since $p$ is an increasing function, for $k > 0$ we have $p\left(\frac{k(f_n^*)^0}{w}\right) \leq p\left(\frac{k(n \chi_{(0, c)})^0}{w}\right)$ a.e. Hence

$$
\rho_ {\varphi_ {*}, w} \left(p \left(\frac {k (f _ {n} ^ {*}) ^ {0}}{w}\right)\right) = \int_ {I} \varphi_ {*} \left(p \left(\frac {k (f _ {n} ^ {*}) ^ {0}}{w}\right)\right) w \leq \int_ {I} \varphi_ {*} \left(p \left(\frac {k (n \chi_ {(0 , c)}) ^ {0}}{w}\right)\right) w.
$$

Moreover,

$$
\int_ {I} \varphi_ {*} \left(p \left(\frac {k (n \chi_ {(0 , c)}) ^ {0}}{w}\right)\right) w = \int_ {I} \varphi_ {*} \left(p \left(k n \frac {c}{W (c)} \chi_ {(0, c)}\right)\right) w = \varphi_ {*} (M) W (c),
$$

where $M = p\left(kn\frac{c}{W(c)}\right)$ . Since $W(c) < \infty$ , we have $\rho_{\varphi_{*},w}\left(p\left(\frac{k(f_{n}^{*})^{0}}{w}\right)\right) < \infty$ .

Before presenting a few basic properties of the Orlicz norm in $\mathcal{M}_{\varphi, w}$ , we start with an auxiliary lemma. The similar fact with respect to simple functions was shown in [13], which was essential to prove the M-ideal properties in Orlicz-Lorentz spaces. Here we present a quick proof based on properties of level functions.

Lemma 6.3. Let $\varphi$ be an $N$ -function and $f \in L_0$ such that $P_{\varphi, w}(f) < \infty$ . Then the inverse level function $w^{f^*}$ satisfies $w^{f^*} \prec w$ and

$$
P _ {\varphi , w} (f) = Q _ {\varphi , w} (f) = \int_ {I} \varphi \left(\frac {(f ^ {*}) ^ {0}}{w}\right) w = \int_ {I} \varphi \left(\frac {f ^ {*}}{w ^ {f ^ {*}}}\right) w ^ {f ^ {*}},
$$

$$
\rho_ {\varphi_ {*}, w} \left(p \left(\frac {(f ^ {*}) ^ {0}}{w}\right)\right) = \int_ {I} \varphi_ {*} \left(p \left(\frac {f ^ {*}}{w ^ {f ^ {*}}}\right)\right) w ^ {f ^ {*}}
$$

Proof. The first part and the fact that $w^{f^*} \prec w$ are well-known [12, 17]. The second part comes from the definition of the inverse level function. Indeed, if we denote a countable family of maximal level intervals by $\{(a_i, b_i) : i \in \mathbb{N}\}$ , we see that

$$
\begin{array}{l} \int_ {I} \varphi_ {*} \left(p \left(\frac {f ^ {*}}{w ^ {f _ {*}}}\right)\right) w ^ {f ^ {*}} = \int_ {I \backslash \cup (a _ {i}, b _ {i})} \varphi_ {*} \left(p \left(\frac {f ^ {*}}{w}\right)\right) w + \sum_ {i = 1} ^ {\infty} \varphi_ {*} \left(p \left(\frac {F (a _ {i} , b _ {i})}{W (a _ {i} , b _ {i})}\right)\right) W (a _ {i}, b _ {i}) \\ = \int_ {I} \varphi_ {*} \left(p \left(\frac {(f ^ {*}) ^ {0}}{w}\right)\right) w = \rho_ {\varphi_ {*}, w} \left(p \left(\frac {(f ^ {*}) ^ {0}}{w}\right)\right) \\ \end{array}
$$

![](images/5236f11acb6a290786021f0014e1eeba4754cf102265002ba27b4b065433492e.jpg)

Now, we provide some results on the Orlicz norm for $\mathcal{M}_{\varphi ,w}$ that are similar to those for Orlicz-Lorentz spaces [27, 28].

Theorem 6.4. Let $\varphi$ be an $N$ -function. For $f \in \mathcal{M}_{\varphi, w}$ ,

(i) $\| f\|_{\mathcal{M}_{\varphi ,w}}\leq \| f\|_{\mathcal{M}_{\varphi ,w}}^{0}\leq 2\| f\|_{\mathcal{M}_{\varphi ,w}}.$   
(ii) If there exists $k > 0$ such that $\rho_{\varphi_*,w}\left(p\left(\frac{k(f^*)^0}{w}\right)\right) = 1$ , then $\| f\|_{\mathcal{M}_{\varphi ,w}}^0 = \int_I f^* p\left(\frac{k(f^*)^0}{w}\right) = \frac{1}{k} (1 + P_{\varphi ,w}(kf))$ .   
(iii) $\tilde{k} \in \bar{K}(f)$ if and only if $\| f \|_{\mathcal{M}_{\varphi, w}}^0 = \frac{1}{k} (1 + P_{\varphi, w}(kf))$ .

Proof. (i): For $g \in \Lambda_{\varphi_{*},w}$ , we have $\| g \|_{\Lambda_{\varphi_{*},w}} \leq \| g \|_{\Lambda_{\varphi_{*},w}}^{0} \leq 2 \| g \|_{\Lambda_{\varphi_{*},w}}$ [27]. Hence

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} = \sup \left\{\int_ {I} | f g |: \| g \| _ {\Lambda_ {\varphi_ {*}, w}} ^ {0} \leq 1 \right\} \leq \sup \left\{\int_ {I} | f g |: \| g \| _ {\Lambda_ {\varphi_ {*}, w}} \leq 1 \right\} = \| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0}.
$$

By Proposition 4.3, we see that $P_{\varphi ,w}\left(\frac{f}{\|f\|\mathcal{M}_{\varphi,w}}\right)\leq 1$ . Then we have

$$
\left\| \frac {f}{\| f \| _ {\mathcal {M} _ {\varphi , w}}} \right\| _ {\mathcal {M} _ {\varphi , w}} ^ {0} \leq 1 + P _ {\varphi , w} \left(\frac {f}{\| f \| _ {\mathcal {M} _ {\varphi , w}}}\right) \leq 2.
$$

Therefore, $\| f\|_{\mathcal{M}_{\varphi ,w}}\leq \| f\|_{\mathcal{M}_{\varphi ,w}}^{0}\leq 2\| f\|_{\mathcal{M}_{\varphi ,w}}$

(ii): We will use the inverse level functions to show our claim. Denote the inverse level function of $f^{*}$ by $w^{f^{*}}$ . Assume $k > 0$ such that $\rho_{\varphi_{*},w}\left(p\left(\frac{k(f^{*})^{0}}{w}\right)\right) = 1$ . By Lemma 6.3 we see that

$$
\int_ {I} \varphi_ {*} \left(p \left(\frac {k f ^ {*}}{w ^ {f ^ {*}}}\right)\right) w ^ {f ^ {*}} = \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right) = 1. \tag {7}
$$

Observe that

$$
\int_ {I} f ^ {*} p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right) = \int_ {I} f ^ {*} p \left(\frac {k f ^ {*}}{w ^ {f ^ {*}}}\right) = \frac {1}{k} \int_ {I} \frac {k f ^ {*}}{w ^ {f ^ {*}}} p \left(\frac {k f ^ {*}}{w ^ {f ^ {*}}}\right) w ^ {f ^ {*}}.
$$

From Young's equality [5, pp. 8, formula (3)],

$$
(8) \qquad \frac {1}{k} \int_ {I} \frac {k f ^ {*}}{w ^ {f *}} p \left(\frac {k f ^ {*}}{w ^ {f *}}\right) w ^ {f *} = \frac {1}{k} \left(\int_ {I} \varphi \left(\frac {k f ^ {*}}{w ^ {f *}}\right) w ^ {f *} + \int_ {I} \varphi_ {*} \left(p \left(\frac {k f ^ {*}}{w ^ {f *}}\right)\right) w ^ {f *}\right),
$$

and by Lemma 6.3 and (7), we obtain

$$
\int_ {I} f ^ {*} p \left(\frac {k \left(f ^ {*}\right) ^ {0}}{w}\right) = \frac {1}{k} \left(1 + P _ {\varphi , w} (k f)\right). \tag {9}
$$

From the definition of the Orlicz norm for $\mathcal{M}_{\varphi ,w}$ and from the fact that $\rho_{\varphi_*,w}\left(p\left(\frac{k(f^*)^0}{w}\right)\right) = 1,$ we have

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} \geq \int_ {I} f ^ {*} p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right).
$$

To show the reverse inequality, since $\mathcal{M}_{\varphi ,w}$ is r.i., we have

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = \sup  \left\{\int_ {I} f ^ {*} g ^ {*}: \rho_ {\varphi_ {*}, w} (g) \leq 1 \right\} = \frac {1}{k} \sup  \left\{\int_ {I} k f ^ {*} g ^ {*}: \rho_ {\varphi_ {*}, w} (g) \leq 1 \right\}.
$$

In addition, by Young's inequality and by Lemma 6.3, we see that

$$
\int_ {I} k f ^ {*} g ^ {*} = \int_ {I} \frac {k f ^ {*} g ^ {*}}{w ^ {f ^ {*}}} w ^ {f ^ {*}} \leq \int_ {I} \varphi \left(\frac {k f ^ {*}}{w ^ {f ^ {*}}}\right) w ^ {f ^ {*}} + \int_ {I} \varphi_ {*} (g ^ {*}) w ^ {f ^ {*}} \leq P _ {\varphi , w} (k f) + \rho_ {\varphi_ {*}, w} (g).
$$

Hence for $g\in \Lambda_{\varphi_{*},w}$ such that $\rho_{\varphi_{*},w}(g)\leq 1$ , by (9),

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = \frac {1}{k} \sup \left\{\int_ {I} k f ^ {*} g ^ {*}: \rho_ {\varphi_ {*}, w} (g) \leq 1 \right\} \leq \frac {1}{k} (P _ {\varphi , w} (k f) + 1)) = \int_ {I} f ^ {*} p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right),
$$

and this proves our claim.

(iii): For $f \in \mathcal{M}_{\varphi, w}^{0}$ , define a function $T(k) = \frac{1}{k} (1 + P_{\varphi, w}(kf))$ . Let $\bar{\theta} = \bar{\theta}(f)$ . The function $T(k)$ is continuous on the interval $(0, 1/\bar{\theta})$ . We first want to show that $\bar{k}^{**} < 1/\bar{\theta}$ . Notice that for every $k < \bar{k}^{**}$ , $\rho_{\varphi_{*}, w}\left(p\left(\frac{k(f^{*})^{0}}{w}\right)\right) \leq 1$ . In view of (8),

$$
\int_ {I} k f ^ {*} p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right) = P _ {\varphi , w} (k f) + \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right).
$$

Hence

$$
T (k) = \frac {1}{k} (1 + P _ {\varphi , w} (k f)) \leq \frac {1}{k} \left(1 + \int_ {I} k f ^ {*} p \left(\frac {k (f ^ {*}) ^ {0}}{w}\right)\right) \leq \frac {1}{k} (1 + \| k f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0}),
$$

and this shows that $T(k) \leq \frac{1}{k} + \| f \|_{\mathcal{M}_{\varphi, w}}^{0}$ for every $k < \bar{k}^{**}$ . Let $(k_n)_{n=1}^{\infty}$ be a sequence of real numbers such that $k_n \uparrow \bar{k}^{**}$ . Then by Fatou's lemma, we obtain

$$
T (\bar {k} ^ {* *}) \leq \lim _ {n} \inf \frac {1}{k _ {n}} (1 + P _ {\varphi , w} (k _ {n} f)) \leq \lim _ {n \to \infty} \frac {1}{k _ {n}} + \| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = 1 / \bar {k} ^ {* *} + \| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0}.
$$

Since $\varphi$ is an $N$ -function, $\bar{k}^{**} < \infty$ by Lemma 6.1. Hence by the statement (i),

$$
P _ {\varphi , w} (\bar {k} ^ {* *} f) \leq \| \bar {k} ^ {* *} f \| _ {\mathcal {M} _ {\varphi , w}} \leq \| \bar {k} ^ {* *} f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} <   \infty .
$$

Thus, we get $\bar{k}^{**} < 1 / \bar{\theta}$ .

Now, let $k_{1}, k_{2} \in (0, 1 / \bar{\theta})$ such that $k_{1} > k_{2}$ . Define $f_{n} = f\chi_{\{\frac{1}{n} < |f| \leq n\}}$ . Then by Young's inequality, for every $n \in \mathbb{N}$ ,

$$
\begin{array}{l} \int_ {I} k _ {1} f _ {n} ^ {*} p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right) = \int_ {I} \frac {k _ {1} f _ {n} ^ {*}}{w f _ {n} ^ {*}} p \left(\frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right) w ^ {f _ {n} ^ {*}} \leq \int_ {I} \varphi \left(\frac {k _ {1} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right) w ^ {f _ {n} ^ {*}} + \int_ {I} \varphi_ {*} \left(p \left(\frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right)\right) w ^ {f _ {n} ^ {*}} \\ = P _ {\varphi , w} (k _ {1} f _ {n}) + \rho_ {\varphi *, w} \left(p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right)\right). \\ \end{array}
$$

Since $\rho_{\varphi_{*},w}\left(p\left(\frac{k_2(f_n^*)^0}{w}\right)\right) < \infty$ by Lemma 6.2,

$$
P _ {\varphi , w} \left(k _ {1} f _ {n}\right) \geq \int_ {I} k _ {1} f _ {n} ^ {*} p \left(\frac {k _ {2} \left(f _ {n} ^ {*}\right) ^ {0}}{w}\right) - \rho_ {\varphi *, w} \left(p \left(\frac {k _ {2} \left(f _ {n} ^ {*}\right) ^ {0}}{w}\right)\right). \tag {10}
$$

In addition by Young's equality and Lemma 6.3, we see that

$$
\begin{array}{l} \int_ {I} k _ {2} f _ {n} ^ {*} p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right) = \int_ {I} \frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}} p \left(\frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right) w ^ {f _ {n} ^ {*}} = \int_ {I} \varphi \left(\frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right) w ^ {f _ {n} ^ {*}} + \int_ {I} \varphi_ {*} \left(p \left(\frac {k _ {2} f _ {n} ^ {*}}{w f _ {n} ^ {*}}\right)\right) w ^ {f _ {n} ^ {*}} \\ = P _ {\varphi , w} (k _ {2} f _ {n}) + \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right)\right). \\ \end{array}
$$

Then we obtain

$$
P _ {\varphi , w} \left(k _ {2} f _ {n}\right) = \int_ {I} k _ {2} f _ {n} ^ {*} p \left(\frac {k _ {2} \left(f _ {n} ^ {*}\right) ^ {0}}{w}\right) - \rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {2} \left(f _ {n} ^ {*}\right) ^ {0}}{w}\right)\right). \tag {11}
$$

Observe that

$$
\frac {1}{k _ {1}} (1 + P _ {\varphi , w} (k _ {1} f _ {n})) - \frac {1}{k _ {2}} (1 + P _ {\varphi , w} (k _ {2} f _ {n})) = \frac {k _ {2} - k _ {1}}{k _ {1} k _ {2}} + \frac {1}{k _ {1}} P _ {\varphi , w} (k _ {1} f _ {n}) - \frac {1}{k _ {2}} P _ {\varphi , w} (k _ {2} f _ {n}).
$$

By adding and subtracting by $\frac{1}{k_1} P_{\varphi, w}(k_2 f_n)$ ,

$$
\begin{array}{l} \frac {k _ {2} - k _ {1}}{k _ {1} k _ {2}} + \frac {1}{k _ {1}} P _ {\varphi , w} (k _ {1} f _ {n}) - \frac {1}{k _ {2}} P _ {\varphi , w} (k _ {2} f _ {n}) \\ = \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(- 1 + \frac {k _ {2}}{k _ {1} - k _ {2}} \left(P _ {\varphi , w} (k _ {1} f _ {n}) - P _ {\varphi , w} (k _ {2} f _ {n})\right) - P _ {\varphi , w} (k _ {2} f _ {n})\right). \\ \end{array}
$$

From (10) and (11),

$$
\begin{array}{l} \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(- 1 + \frac {k _ {2}}{k _ {1} - k _ {2}} (P _ {\varphi , w} (k _ {1} f _ {n}) - P _ {\varphi , w} (k _ {2} f _ {n})) - P _ {\varphi , w} (k _ {2} f _ {n})\right) \\ \geq \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(- 1 + \frac {k _ {2}}{k _ {1} - k _ {2}} \left(\int_ {I} (k _ {1} - k _ {2}) f _ {n} p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right)\right) - P _ {\varphi , w} (k _ {2} f _ {n})\right) \\ = \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(\rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {2} (f _ {n} ^ {*}) ^ {0}}{w}\right)\right) - 1\right). \\ \end{array}
$$

Hence, we have

$$
\frac {1}{k _ {1}} \left(1 + P _ {\varphi , w} \left(k _ {1} f _ {n}\right)\right) - \frac {1}{k _ {2}} \left(1 + P _ {\varphi , w} \left(k _ {2} f _ {n}\right)\right) \geq \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(\rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {2} \left(f _ {n} ^ {*}\right) ^ {0}}{w}\right)\right) - 1\right).
$$

From the fact that $(f_n^*)^0 \uparrow (f^*)^0$ a.e. by Proposition 3.3 and by the Monotone Convergence Theorem, notice that for $k_1 > k_2$ ,

$$
T \left(k _ {1}\right) - T \left(k _ {2}\right) \geq \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(\rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {2} \left(f ^ {*}\right) ^ {0}}{w}\right)\right) - 1\right). \tag {12}
$$

By the same argument, if $k_{1} < k_{2}$ , we can also show that

$$
T \left(k _ {1}\right) - T \left(k _ {2}\right) \geq \frac {k _ {1} - k _ {2}}{k _ {1} k _ {2}} \left(\rho_ {\varphi_ {*}, w} \left(p \left(\frac {k _ {1} \left(f ^ {*}\right) ^ {0}}{w}\right)\right) - 1\right). \tag {13}
$$

For $0 < k_{1} < k_{2} < \bar{k}^{*}$ , $\frac{k_{1} - k_{2}}{k_{1}k_{2}} < 0$ and $\rho_{\varphi_{*},w}\left(p\left(\frac{k_1(f^*)^0}{w}\right)\right) < 1$ . So from (13), $T(k)$ is decreasing on $(0,\bar{k}^{*})$ . Moreover, since $\frac{k_1 - k_2}{k_1k_2} > 0$ and $\rho_{\varphi_{*},w}\left(p\left(\frac{k_2(f^*)^0}{w}\right)\right) > 1$ for $\bar{k}^{**} < k_{1} < k_{2} < 1 / \bar{\theta}$ , the function $T(k)$ is increasing on $(\bar{k}^{**},1 / \bar{\theta})$ by (12). Notice from the definitions of $\bar{k}^{*}$ and $\bar{k}^{**}$ that $\rho_{\varphi_{*},w}\left(p\left(\frac{k(f^{*})^{0}}{w}\right)\right) = 1$ for any $k \in (\bar{k}^{*},\bar{k}^{**})$ . Hence,

$$
\| f \| _ {\mathcal {M} _ {\varphi , w}} ^ {0} = \inf  _ {l > 0} T (l) = \frac {1}{k} (1 + P _ {\varphi , w} (k f))
$$

by Theorem 6.4.(ii). Observe that $T(l) > T(\bar{k}^{*})$ for every $l < \bar{k}^{*}$ and $T(l) > T(\bar{k}^{**})$ for every $l > \bar{k}^{**}$ . Since $T(l)$ is continuous on the interval $(0,1 / \bar{\theta})$ and $\bar{k}^{*},\bar{k}^{**}\in (0,1 / \bar{\theta})$ , $\| f\|_{\mathcal{M}_{\varphi ,w}}^0 = \inf_{l > 0}T(l) = T(\bar{k}^*) = T(\bar{k}^{**})$ . Hence, if $k\in \bar{K} (f) = [\bar{k}^{*},\bar{k}^{**}]$ , then $\| f^0\|_{\mathcal{M}_{\varphi ,w}} = \frac{1}{k} (1 + P_{\varphi ,w}(kf))$ .

To show the converse, define $T(k)$ and $\bar{\theta}$ as before. Recall the fact that $T(k)$ is continuous on the interval $(0, 1 / \bar{\theta})$ . Let $k_0 > 0$ be such that $\| f\|_{\mathcal{M}_{\varphi ,w}}^0 = T(k_0) = \inf_{k > 0}T(k)$ . If $k_0 \in (0,\bar{k}^*)$ , $T(k_0) > T(\bar{k}^*)$ because $T(k)$ is decreasing on the interval $(0,\bar{k}^{*})$ by (13). Also, $T(k_0) > T(\bar{k}^{**})$ for $k_0 \in (\bar{k}^{**},1 / \bar{\theta})$ since $T(k)$ is increasing on the interval $(\bar{k}^{**},1 / \bar{\theta})$ by (12). Hence $T(k_0) = \| f\|_{\mathcal{M}_{\varphi ,w}}^0$ only when $k_0 \in \bar{K}(f)$ .

# 7. APPLICATIONS TO ORLICZ-LORENTZ SPACES

The characterization of separable $\mathcal{M}_{\varphi, w}$ spaces in Section 4 allows us to explore various properties in Orlicz-Lorentz spaces. First, we can characterize the reflexivity of Orlicz-Lorentz spaces and their Kothe duals.

Theorem 7.1. The following statements are equivalent:

(i) An Orlicz-Lorentz space $\Lambda_{\varphi ,w}$ is reflexive.   
(ii) $\varphi$ and its complementary function $\varphi_{*}$ satisfy the appropriate $\Delta_2$ -condition.

The analogous statement for $\lambda_{\varphi, w}$ also holds.

Proof. An Orlicz function $\varphi$ satisfies the appropriate $\Delta_{2}$ -condition if and only if $\Lambda_{\varphi, w}$ is order-continuous by [11, Theorem 2.4]. Also the complementary function $\varphi_*$ satisfies the appropriate $\Delta_{2}$ -condition if and only if $(\Lambda_{\varphi, w})' \simeq \mathcal{M}_{\varphi*, w}^0$ is order-continuous by Theorem 4.15, Theorem 3.2, and the equivalence between the Orlicz norm and the Luxemburg norm. From the fact that a Banach function lattice $X$ is reflexive if and only if both $X$ and $X'$ are order-continuous [2, Corollary 1.4.4], we obtain the desired result.

Theorem 7.2. The following statements are equivalent:

(i) The space $\mathcal{M}_{\varphi, w}$ is reflexive.   
(ii) $\varphi$ and its complementary function $\varphi_{*}$ satisfy the appropriate $\Delta_2$ -condition.

The analogous statement for $\mathfrak{m}_{\varphi, w}$ also holds.

Proof. An Orlicz function $\varphi$ satisfies the appropriate $\Delta_{2}$ -condition if and only if $(\mathcal{M}_{\varphi_{*},w})^{\prime} \simeq \Lambda_{\varphi, w}^{0}$ is order-continuous by [11, Theorem 2.4], Theorem 3.2, and the equivalence between the Orlicz norm and the Luxemburg norm. Also the complementary function $\varphi_{*}$ satisfies the appropriate $\Delta_{2}$ -condition if and only if $\mathcal{M}_{\varphi_{*},w}$ is order-continuous by Theorem 4.15. From the fact that a Banach function lattice $X$ is reflexive if and only if both $X$ and $X^{\prime}$ are order-continuous [2, Corollary 1.4.4], we obtain the desired result.

7.1. M-embedded Orlicz-Lorentz spaces. A closed subspace $Y$ of $X$ is said to be an $M$ -ideal if there exists a projection $P: X^* \to X^*$ such that the $P(X^*) = Y^\perp$ and $\| x^* \| = \| P x^* \| + \| (I - P) x^* \|$ . A Banach space $X$ is said to be $M$ -embedded if $X$ is an $M$ -ideal in its bidual $X^{**}$ . Assuming that $X$ is an $M$ -ideal in its bidual $X^{**}$ , if $Y$ is a separable closed subspace of $X$ , then $Y^*$ is separable [21, Theorem 2.6].

The dual $X^{*}$ of a Banach function lattice $X$ is isometrically isomorphic to the Köthe dual space $X'$ if and only if $X$ is order-continuous [2, Corollary 1.4.3]. For the case of Orlicz spaces equipped with the Luxemburg norm, it is shown that the order-continuous subspace $(L_{\varphi})_a$ is $M$ -embedded if $\varphi_*$ satisfies the appropriate $\Delta_2$ -condition [10]. As a matter of fact, the analogous statement is also true for $(\Lambda_{\varphi,w})_a$ and $(\lambda_{\varphi,w})_a$ .

Now, we are ready to provide sufficient conditions for M-embeddedness of $(\Lambda_{\varphi ,w})_a$

Theorem 7.3. (i) If both $\varphi$ and $\varphi_*$ satisfy the appropriate $\Delta_2$ -condition, then the order-continuous subspace $(\Lambda_{\varphi,w})_a$ is an $M$ -ideal in its bidual $((\Lambda_{\varphi,w})_a)^{**} \simeq \Lambda_{\varphi,w}$ .

(ii) If neither $\varphi$ nor $\varphi_*$ satisfies the appropriate $\Delta_2$ -condition, then the order-continuous subspace $(\Lambda_{\varphi,w})_a$ is not an $M$ -ideal in its bidual.   
(iii) If $\varphi$ does not satisfy the appropriate $\Delta_{2}$ -condition while $\varphi_*$ does, then the order-continuous subspace $(\Lambda_{\varphi, w})_a$ is an $M$ -ideal in its bidual $((\Lambda_{\varphi, w})_a)^{**} \simeq \Lambda_{\varphi, w}$ .

Proof. (i): In view of Theorem 7.1, $(\Lambda_{\varphi ,w})_a = \Lambda_{\varphi ,w}\simeq (\Lambda_{\varphi ,w})_a^{**}$ . Hence, the statement holds trivially.

(ii): Suppose that both $\varphi$ and $\varphi_{*}$ does not satisfy the appropriate $\Delta_2$ -condition and assume to the contrary that $(\Lambda_{\varphi ,w})_a$ is an $M$ -ideal in its bidual $((\Lambda_{\varphi ,w})_a)^{**}$ . In view of [21, Theorem 2.6], the dual of $(\Lambda_{\varphi ,w})_a$ has to be separable. From the fact that $X^{*}$ is isometrically isomorphic to $X^{\prime}$ for order-continuous Banach function spaces, we have $((\Lambda_{\varphi ,w})_a)^*\simeq (\Lambda_{\varphi ,w})'\simeq \mathcal{M}_{\varphi_{*},w}^0$ by Theorem 3.2. However, the space $\mathcal{M}_{\varphi_{*},w}^{0}$ is not separable by Corollary 4.14, which is a contradiction.   
(iii): It was shown in [14, Theorem 3.10] that the order-continuous subspace $(\Lambda_{\varphi ,w})_a$ is an $M$ -ideal in $\Lambda_{\varphi ,w}$ . Since $((\Lambda_{\varphi ,w})_a)^{**}\simeq (\mathcal{M}_{\varphi *,w}^0)^* \simeq \Lambda_{\varphi ,w}$ by [2, Corollary 1.4.3] and Theorem 3.2, the claim holds.

The sequence analogue of Theorem 7.3 can be obtained by a similar argument. Hence we only provide the statement here. For the proof of 7.4.(iii), we refer to [14, Theorem 3.11].

Theorem 7.4. (i) If both $\varphi$ and $\varphi_{*}$ satisfy the $\Delta_2^0$ -condition, then the order-continuous subspace $(\lambda_{\varphi ,w})_a$ is an $M$ -ideal in its bidual $((\lambda_{\varphi ,w})_a)^{**} \simeq \lambda_{\varphi ,w}$ .

(ii) If both $\varphi$ and $\varphi_{*}$ do not satisfy the $\Delta_2^0$ -condition, then the order-continuous subspace $(\lambda_{\varphi ,w})_a$ is not an $M$ -ideal in its bidual $((\lambda_{\varphi ,w})_a)^{**}$ .   
(iii) If $\varphi$ does not satisfy the $\Delta_2^0$ -condition while $\varphi_*$ does, then the order-continuous subspace $(\lambda_{\varphi,w})_a$ is an $M$ -ideal in its bidual $((\lambda_{\varphi,w})_a)^{**} \simeq \lambda_{\varphi,w}$ .

7.2. Uniqueness of norm-preserving extension on Orlicz-Lorentz spaces equipped with the Orlicz norm. By the Hahn-Banach extension theorem, any bounded linear functional on a subspace of a Banach space has a norm-preserving extension to the whole space. In this section, we study the uniqueness of such extension from $(\Lambda_{\varphi ,w}^{0})_{a}$ to $\Lambda_{\varphi ,w}^{0}$ . In view of [10, Proposition 1.12], we can deduce that every integral functional $H\in (\Lambda_{\varphi ,w})_a^*$ has a unique norm-preserving extension to $\Lambda_{\varphi ,w}$ because $(\Lambda_{\varphi ,w})_a$ is an $M$ -ideal in $\Lambda_{\varphi ,w}$ . Hence, we only consider when the space is equipped with the Orlicz norm.

Let us recall the interval $K(f) = [k^{*}, k^{**}]$ for $f \in \Lambda_{\varphi, w}^{0}$ [27], where

$$
k ^ {*} = k ^ {*} (f) = \inf  \{k > 0: \rho_ {\varphi_ {*}, w} (p (k f)) \geq 1 \}, \text {a n d}
$$

$$
k ^ {* *} = k ^ {* *} (f) = \sup  \{k > 0: \rho_ {\varphi_ {*}, w} (p (k f)) \leq 1 \}.
$$

In general, it is well-known that $0 \leq k^{*} \leq k^{**} \leq \infty$ . By the similar reasoning as Lemma 6.1, we can show that $k^{**} < \infty$ when $\varphi$ is an Orlicz $N$ -function. We can also define $k^{*}(x)$ , $k^{**}(x)$ , and $K(x)$ for $x \in \lambda_{\varphi, w}$ by replacing $\rho_{\varphi, w}$ with $\alpha_{\varphi, w}$ .

Notice that $k^*$ and $k^{**}$ for $\Lambda_{\varphi, w}^0$ as well as $k^*$ and $k^{**}$ for $\mathcal{M}_{\varphi, w}^0$ in section 6 are defined by the same modular $\rho_{\varphi_*, w}$ . Such confusion comes from the fact that investigation on the space $\mathcal{M}_{\varphi, w}$ was initiated much later than [27, 28]. For Orlicz spaces $L_{\varphi}^0$ , this is not an issue because the Köthe dual space of $L_{\varphi}^0$ is $L_{\varphi_*}$ , which is another Orlicz space. However, as we mentioned earlier, the Köthe dual space of an Orlicz-Lorentz space is not precisely an Orlicz-Lorentz space, and its modular shows different behaviors from the one for Orlicz-Lorentz spaces. Now, in view of Proposition 3.4, we see that

$$
\rho_ {\varphi_ {*}, w} (p (k f)) = \rho_ {\varphi_ {*}, w} (p (k f ^ {*})) = P _ {\varphi_ {*}, w} (p (k f ^ {*}) w).
$$

Hence, we provide equivalent definitions of $k^*$ and $k^{**}$ in terms of the modular $P_{\varphi,w}$ to be consistent with the Köthe duality between Orlicz-Lorentz spaces and the spaces $\mathcal{M}_{\varphi,w}$ as follows.

$$
k ^ {*} = k ^ {*} (f) = \inf  \{k > 0: P _ {\varphi_ {*}, w} (p (k f ^ {*}) w) \geq 1 \}, \text {a n d}
$$

$$
k ^ {* *} = k ^ {* *} (f) = \sup  \{k > 0: P _ {\varphi_ {*}, w} (p (k f ^ {*}) w) \leq 1 \}.
$$

With the modular $\mathfrak{p}_{\varphi_{*},w}$ , we can similarly define the constants $k^{*}$ and $k^{**}$ for Orlicz-Lorentz sequence space $\lambda_{\varphi ,w}^0$ .

The following results show when the infimum for the Orlicz norm $\| \cdot \|_{\varphi ,w}^{0}$ is attained.

Theorem 7.5. [27, pg 133] (c.f. [28, Proposition 1.5 and 1.8] for the sequence case) Let $\varphi$ be an $N$ -fucntion.

(i) If there exists $k > 0$ such that $\rho_{\varphi, w}(p(k|f|)) = 1$ , then $\| f \|_{\varphi, w}^0 = \int_0^\gamma f^* p(kf^*)w = \frac{1}{k} (1 + \rho_{\varphi, w}(kf))$ .   
(ii) $k\in K(f)$ if and only if $\| f\|_{\varphi ,w}^0 = \frac{1}{k} (1 + \rho_{\varphi ,w}(kf))$

The analogous statements occur in Orlicz-Lorentz sequence space when the modular $\rho_{\varphi, w}$ is replaced by the modular $\alpha_{\varphi, w}$ .

In order to study the existence of a unique norm-preserving extension of a bounded linear functional on $(\Lambda_{\varphi ,w}^{0})_{a}$ to $\Lambda_{\varphi ,w}^{0}$ , we need to know when a bounded linear functional is normattaining. A bounded linear functional $F\in X^{*}$ on $X$ is said to be norm-attaining if $|F(f)| = \| F\|_{X^*}$ for some $f\in X$ such that $\| f\| _X = 1$ . For Orlicz-Lorentz spaces, it is useful to know an explicit formula for the norm of a bounded linear functional to characterize its norm-attainment.

Theorem 7.6. [13, Theorem 3.6] (c.f. [13, Theorem 3.7] for the sequence case) Let $\varphi$ be an $N$ -function and $F$ be a bounded linear functional on $\Lambda_{\varphi, w}^{0}$ . Then $F = H + S$ , where $H(f) = \int_{I} f h$ for some $h \in \mathcal{M}_{\varphi, w}$ , $\|H\| = \|h\|_{\mathcal{M}_{\varphi, w}}$ , $S(f) = 0$ for all $f \in (\Lambda_{\varphi, w})_{a}$ , and $\|F\| = \inf \{\lambda > 0 : P_{\varphi, w}(\frac{h}{\lambda}) + \frac{1}{\lambda} \|S\| \leq 1\}$ . The similar formula also holds for the sequence space $\lambda_{\varphi, w}$ .

Theorem 7.7. [13, Theorem 2.2] For any singular functional $S$ of $\Lambda_{\varphi,w}$ equipped with the Luxemburg norm or the Orlicz norm, $\| S \| = \| S \|_{(\Lambda_{\varphi,w})^*} = \| S \|_{(\Lambda_{\varphi,w}^0)^*} = \sup \{S(f): \rho_{\varphi,w}(f) < \infty\} = \sup \{\frac{S(f)}{\theta(f)}: f \in \Lambda_{\varphi,w} \setminus (\Lambda_{\varphi,w})_a\}$ . The analogous formulas hold for Orlicz-Lorentz sequence spaces.

Now, we are ready to provide a characterization for the norm-attaining functionals on $\Lambda_{\varphi ,w}^{0}$ and $\lambda_{\varphi ,w}^{0}$ .

Theorem 7.8. Let $\varphi$ be an $N$ -function and let $F = H + S$ be a bounded linear functional on $\Lambda_{\varphi, w}^{0}$ , where $H(f) = \int_{I} f h$ for some $h \in \mathcal{M}_{\varphi_{*}, w}$ and $S(f) = 0$ at $f \in (\Lambda_{\varphi, w}^{0})_{a}$ . Then $F$ is norm-attaining if and only if there exists $f \in \Lambda_{\varphi, w}^{0}$ with $\|f\|_{\varphi, w}^{0} = 1$ such that for some $k \in K(f)$ , the following conditions are satisfied

(i) $P_{\varphi_{*},w}(\frac{h}{\|F\|}) + \frac{\|S\|}{\|F\|} = 1,$   
(ii) $\| S\| = S(kf)$   
(iii) $\int_{I}h f = \int_{I}k h^{*}f^{*} = \int_{I}(h^{*})^{0}f^{*}$ and $\int_{I}\frac{k(h^{*})^{0}f^{*}}{\|F\|} = \rho_{\varphi ,w}(kf) + P_{\varphi_{*},w}(\frac{h}{\|F\|}).$

Proof. Let $f \in \Lambda_{\varphi, w}^0$ be such that $\|f\|_{\varphi, w}^0 = 1$ , $\|F\| = F(f)$ and $k \in K(f)$ . Then we have $\rho_{\varphi, w}(kf) < \infty$ . Indeed, notice that $1 = \|f\|^0 = \frac{1}{k} (1 + \rho_{\varphi, w}(kf))$ for $k \in K(f)$ from Theorem 7.5. Hence $\rho_{\varphi, w}(kf) = k - 1 < k^{**}(f) < \infty$ . Let $h \in \mathcal{M}_{\varphi*, w}$ . From the fact that $h^* \prec (h^*)^0$ , the Young's inequality and Lemma 2.1 give us

$$
\begin{array}{l} 1 = \frac {F (f)}{\| F \|} = \frac {H (f)}{\| F \|} + \frac {S (f)}{\| F \|} \leq \frac {\int_ {I} h ^ {*} f ^ {*}}{\| F \|} + \frac {S (f)}{\| F \|} \leq \frac {\int_ {I} \left(h ^ {*}\right) ^ {0} f ^ {*}}{\| F \|} + \frac {S (f)}{\| F \|} \\ = \frac {1}{k} \left(\int_ {I} \frac {k \left(h ^ {*}\right) ^ {0} f ^ {*}}{w \| F \|} w + \frac {S (k f)}{\| F \|}\right) \\ \leq \frac {1}{k} \left(\int_ {I} \varphi (k f ^ {*}) w + \int_ {I} \varphi_ {*} \left(\frac {(h ^ {*}) ^ {0}}{w \| F \|}\right) w + \frac {S (k f)}{\| F \|}\right) \\ = \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right) + \frac {S (k f)}{\| F \|}\right). \\ \end{array}
$$

Now, we claim that

$$
P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right) + \frac {\| S \|}{\| F \|} \leq 1. \tag {14}
$$

Indeed, in view of Theorem 7.6, let $(\lambda_{n})$ be a sequence of real numbers such that $(\lambda_{n}) \downarrow \|F\|$ and $P_{\varphi_{*},w}\left(\frac{h}{\lambda_{n}}\right) + \frac{\|S\|}{\lambda_{n}} \leq 1$ for every $n \in \mathbb{N}$ . Let $g(k) = P_{\varphi_{*},w}(kh) + k\|S\|$ for $k > 0$ . The function $g(k)$ is increasing and continuous on the interval $(0,1/\bar{\theta})$ , where $\bar{\theta} = \bar{\theta}(h) = \inf \left\{\lambda > 0 : P_{\varphi_{*},w}\left(\frac{h}{\lambda}\right) < \infty \right\}$ . Notice that $P_{\varphi_{*},w}\left(\frac{h}{\lambda_{n}}\right) + \frac{\|S\|}{\lambda_{n}} \leq 1$ for every $n \in \mathbb{N}$ . Hence

$$
\lim _ {n \to \infty} P _ {\varphi_ {*}, w} \left(\frac {h}{\lambda_ {n}}\right) + \frac {\| S \|}{\| F \|} = \lim _ {n \to \infty} \left(P _ {\varphi_ {*}, w} \left(\frac {h}{\lambda_ {n}}\right) + \frac {\| S \|}{\lambda_ {n}}\right) \leq 1.
$$

Since $\frac{1}{\lambda_n} \uparrow \frac{1}{\|F\|}$ , we have $\varphi_*\left(\frac{(h^*)^0}{\lambda_n w}\right) w \uparrow \varphi_*\left(\frac{(h^*)^0}{\|F\| w}\right) w$ a.e. So by the Monotone Convergence Theorem,

$$
\lim _ {n \to \infty} P _ {\varphi_ {*}, w} \left(\frac {h}{\lambda_ {n}}\right) = \lim _ {n \to \infty} \int_ {I} \varphi_ {*} \left(\frac {(h ^ {*}) ^ {0}}{\lambda_ {n} w}\right) w = \int_ {I} \varphi_ {*} \left(\frac {(h ^ {*}) ^ {0}}{\| F \| w}\right) w = P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right),
$$

and this proves inequality (14).

Since $\rho_{\varphi, w}(kf) < \infty$ , $S(kf) \leq \| S\|$ by Theorem 7.7. Now, from (14) we obtain

$$
\begin{array}{l} \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right) + \frac {S (k f)}{\| F \|}\right) \leq \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right) + \frac {\| S \|}{\| F \|}\right) \\ \leq \frac {1}{k} (\rho_ {\varphi , w} (k f) + 1). \\ \end{array}
$$

Notice that $1 = \| f\|_{\varphi ,w}^{0} = \frac{1}{k}\bigl (\rho_{\varphi ,w}(kf) + 1\bigr)$ from Theorem 7.5.(ii). This consequently shows that

$$
\begin{array}{l} 1 = \frac {H (f)}{\| F \|} + \frac {S (f)}{\| F \|} = \frac {\int_ {I} h ^ {*} f ^ {*}}{\| F \|} + \frac {S (f)}{\| F \|} = \frac {\int_ {I} \left(h ^ {*}\right) ^ {0} f ^ {*}}{\| F \|} + \frac {S (f)}{\| F \|} \\ = \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi *, w} \left(\frac {h}{\| F \|}\right) + \frac {S (k f)}{\| F \|}\right) \\ = \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi *, w} \left(\frac {h}{\| F \|}\right) + \frac {\| S \|}{\| F \|}\right) \\ = \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + 1\right). \\ \end{array}
$$

The sixth and seventh expressions above give us condition (i). Condition (ii) comes from the fifth and sixth expressions. From the second, third, and fourth expressions gives us the first part of condition (iii), and the fourth and fifth expressions show the second part of condition (iii). The proof is finished.

To show the converse, let $f \in \Lambda_{\varphi, w}^{0}$ such that $\|f\|_{\varphi, w}^{0} = 1$ and $k \in K(f)$ . Suppose that the conditions (i), (ii) and (iii) are satisfied. Then $1 = \|f\|^{0} = \frac{1}{k} (1 + \rho_{\varphi, w}(kf))$ by Theorem 7.5. Let $F = H + S$ be a bounded linear functional on $\Lambda_{\varphi, w}^{0}$ where $H(f) = \int_{I} f h$ for some $h \in \mathcal{M}_{\varphi*, w}$ and $S(f) = 0$ for every $f \in (\Lambda_{\varphi, w}^{0})_{a}$ . Hence

$$
1 = \frac {1}{k} (1 + \rho_ {\varphi , w} (k f)) \stackrel {\text {(i)}} {=} \frac {1}{k} \left(\rho_ {\varphi , w} (k f) + P _ {\varphi_ {*}, w} \left(\frac {h}{\| F \|}\right) + \frac {\| S \|}{\| F \|}\right) \stackrel {\text {(i i), (i i i)}} {=} \frac {1}{k} \left(\int_ {I} \frac {k h f}{\| F \|} + \frac {S (k f)}{\| F \|}\right).
$$

So $1 = \frac{1}{k}\left(\int_{I}\frac{khf}{\|F\|} +\frac{S(kf)}{\|F\|}\right) = \frac{H(f)}{\|F\|} +\frac{S(f)}{\|F\|} = \frac{F(f)}{\|F\|}$ , and the proof is finished.

![](images/7b89df79ce53f8570ed4f680f6f7556076a5cb195a657ad2595b1f5c4b65e2cd.jpg)

By the similar argument, we have the sequence analogue of Theorem 7.8.

Theorem 7.9. Let $\varphi$ be an $N$ -function and let $F = H + S$ be a bounded linear functional on $\lambda_{\varphi, w}^0$ , where $H(x) = \sum_{i=1}^{\infty} x(i) h(i)$ for some $h \in \mathfrak{m}_{\varphi_*, w}$ and $S(x) = 0$ at $x \in (\lambda_{\varphi, w}^0)_a$ . Then $F$ is norm-attaining if and only if there exists $x \in \lambda_{\varphi, w}^0$ with $\|x\|_{\varphi, w}^0 = 1$ such that for some $k \in K(x)$ , the following conditions are satisfied

(i) $p_{\varphi_{*},w}(\frac{h}{\|F\|}) + \frac{\|S\|}{\|F\|} = 1,$   
(ii) $\| S\| = S(kx)$   
(iii) $\sum_{i=1}^{\infty} \frac{kh(i)x(i)}{\|F\|} = \alpha_{\varphi, w}(kx) + p_{\varphi_{*}, w}\left(\frac{h}{\|F\|}\right)$ .

Proposition 7.10. Let $\varphi$ be an $N$ -function. If $H$ is a bounded linear functional on $(\Lambda_{\varphi, w}^{0})_{a}$ , then it has a norm-preserving extension to the whole space $\Lambda_{\varphi, w}^{0}$ , which is also regular. The analogous statement holds for $\lambda_{\varphi, w}^{0}$ .

Proof. Since the sequence case can be proven by a similar argument, we only prove for the function case. Let $H$ be a bounded linear functional on $(\Lambda_{\varphi ,w}^{0})_{a}$ . Then, there exists $h\in \mathcal{M}_{\varphi *,w}$ such that $H(f) = \int hf$ for $f\in (\Lambda_{\varphi ,w}^{0})_{a}$ . Without loss of generality, assume $h\geq 0$ . Denote by $\tilde{H}$ an extension of $H$ to $\Lambda_{\varphi ,w}^{0}$ . Then letting $\tilde{H} (f) = \int_Ihf$ for $f\in \Lambda_{\varphi ,w}^{0}$ , we have $|\tilde{H} (f)| = |\int_Ihf|\leq \| h\|_{\mathcal{M}_{\varphi ,w}}\| f\|^0$ by the Hölder's inequality, so $\tilde{H}$ is well-defined and bounded on $\Lambda_{\varphi ,w}^{0}$ .

Now, for every $\epsilon > 0$ , we can choose $f \in \Lambda_{\varphi, w}^{0}$ with $\| f \|_{\varphi, w}^{0} \leq 1$ such that $\|\tilde{H}\| - \frac{\epsilon}{2} < \int_{I} |hf|$ . Define $f_{n} = |f| \chi_{\{\frac{1}{n} \leq |f| \leq n\}}$ , $n \in \mathbb{N}$ . Since $(\Lambda_{\varphi, w}^{0})_{a} = (\Lambda_{\varphi, w}^{0})_{b}$ , we see that $f_{n} \in (\Lambda_{\varphi, w}^{0})_{a}$ . Notice also that $f_{n} \uparrow |f|$ a.e., and so $\lim_{n \to \infty} \int_{I} h f_{n} = \int_{I} h |f|$ by the Monotone Convergence Theorem. Hence, for all $\epsilon > 0$ , there exists $N$ such that for every $n \geq N$ , $\int_{I} |hf| < \int_{I} |h f_{n}| + \frac{\epsilon}{2}$ , and this shows that $\| \tilde{H} \| < \int_{I} h f_{n} + \epsilon$ . Since $f_{n} \in (\Lambda_{\varphi, w}^{0})_{a}$ has norm less than or equal to 1, we have $\| \tilde{H} \| \leq \| H \|$ . Therefore, $\| H \| = \| \tilde{H} \|$ .

Theorem 7.11. Let $\varphi$ be an $N$ -function. If $H$ is a bounded linear functional on $(\Lambda_{\varphi, w}^{0})_{a}$ which attains its norm on the unit ball of $(\Lambda_{\varphi, w}^{0})_{a}$ , then $H$ has a unique norm-preserving extension to $\Lambda_{\varphi, w}^{0}$ , which is also regular. The analogous statement holds for $\lambda_{\varphi, w}^{0}$ .

Proof. The proof will be given only for function space. The existence of a norm-preserving extension of a bounded linear functional $H$ on $(\Lambda_{\varphi ,w}^{0})_{a}$ to the whole space $\Lambda_{\varphi ,w}^{0}$ , denoted by $\tilde{H}$ , has been shown in Proposition 7.10.

First we show that this extension is unique among regular functionals. Indeed, suppose that we have another norm-preserving extension of $H$ , say $\tilde{G}$ . Then for $f \in (\Lambda_{\varphi, w}^{0})_{a}$ , we have $0 = H(f) - H(f) = (\tilde{H} - \tilde{G})(f)$ . Since $\tilde{H}$ and $\tilde{G}$ are regular functionals, the only possibility is when $\tilde{H} = \tilde{G}$ .

Now we show that none of the functionals $H + S$ , where $H$ is a regular part and a singular part $S \neq 0$ , is a norm-preserving extension. Without loss of generality, assume that $\|H\| = \|h\|_{\mathcal{M}_{\varphi,*},w} = 1$ for some $h \in \mathcal{M}_{\varphi,*}, w$ . Since $H$ attains its norm there exists $f \in (\Lambda_{\varphi,w}^0)_a$ with $\|f\|_{\varphi,w} = 1$ such that $H(f) = \int_I hf = \|h\|_{\mathcal{M}_{\varphi,*},w}$ . In view of Theorem 7.8, we have $P_{\varphi,*}, w(h) = 1$ . Now, define the function $g(\lambda) = P_{\varphi,*}, w(\frac{h}{\lambda}) + \frac{1}{\lambda} \|S\|, \lambda > 0$ . Note that the function $g(\lambda)$ is decreasing and continuous on the interval $(1,\infty)$ and right-continuous at $\lambda = 1$ . From the fact that $g(1) = P_{\varphi,*}, w(h) + \|S\| = 1 + \|S\| > 1$ , there exists $\lambda_0 > 1$ such that $P_{\varphi,*}, w(\frac{h}{\lambda_0}) + \frac{1}{\lambda_0} \|S\| > 1$ . But then, this implies that $\|H + S\| \geq \lambda_0 > 1 = \|H\|$ by Theorem 7.6. Thus, if $S \neq 0$ , $H + S$ is not norm-preserving, so $\tilde{H}$ is the only norm-preserving extension of $H$ to $\Lambda_{\varphi,w}^0$ .

Theorem 7.12. Let $\varphi$ be an $N$ -function. The following statements are equivalent:

(i) Every bounded linear functional $H$ on $(\Lambda_{\varphi ,w}^{0})_{a}$ has a unique norm-preserving extension to $\Lambda_{\varphi ,w}^{0}$   
(ii) $\varphi$ or $\varphi_{*}$ satisfies the appropriate $\Delta_2$ -condition.

The analogous statement holds for $\lambda_{\varphi ,w}^{0}$

Proof. Since the proof for the sequence case is almost identical, we only provide the proof for the function space.

(i) $\Rightarrow$ (ii) Assume that $\varphi$ and $\varphi_{*}$ do not satisfy the appropriate $\Delta_2$ -condition. By the first assumption, there is a bounded linear functional $F = H + S$ on $\Lambda_{\varphi ,w}^{0}$ , where $S\neq 0$ , and $H$ is a regular functional. Now, from the fact that $\varphi_{*}$ does not satisfy $\Delta_2$ -condition, we can choose $H$ generated by $h\in \mathcal{M}_{\varphi_{*},w}$ such that $\| H\| = \| h\|_{\mathcal{M}_{\varphi_{*},w}} = 1$ and $P_{\varphi_{*},w}(h) < 1$ by Lemma 4.9. Choose $S\neq 0$ such that $\| S\| = 1 - P_{\varphi_{*},w}(h)$ . Then we obtain $P_{\varphi_{*},w}(h) + \| S\| = 1$ . Define the function $f(\lambda) = P_{\varphi_{*},w}(\frac{h}{\lambda}) + \frac{1}{\lambda}\| S\|$ , $\lambda >0$ . The function $f(\lambda)$ is strictly decreasing, continuous on $(1,\infty)$ , right-continuous at $\lambda = 1$ , and $f(1) = 1$ . In view of Theorem 7.6, observe that $1\geq f(\| H + S\|)\geq f(1) = f(\| H\|) = 1$ . Hence we have $\| H + S\| = \| H\|$ . Let $\tilde{H}$ be an extension of a bounded linear functional $H$ on $(\Lambda_{\varphi ,w}^{0})_{a}$ to the whole space, as given in Proposition 7.10. Then $\| H + S\| = \| H\| = \| \tilde{H}\|$ . However, $H + S\neq \tilde{H}$ because $S\neq 0$ , so we have two distinct norm-preserving extensions of $H$ in this case.   
(ii) $\Rightarrow$ (i) If $\varphi$ satisfies the appropriate $\Delta_{2}$ -condition, we have $(\Lambda_{\varphi,w}^{0})_{a} = \Lambda_{\varphi,w}^{0}$ , so there is nothing to prove [11]. Hence we only consider when $\varphi$ does not satisfy appropriate $\Delta_{2}$ -condition but $\varphi_{*}$ does. Assume that $H$ is a bounded linear functional on $(\Lambda_{\varphi,w}^{0})_{a}$ such that $\|H\| = \|h\|_{\mathcal{M}_{\varphi*,w}} = 1$ . Let $\tilde{H}$ be an extension of $H$ to $\Lambda_{\varphi,w}^{0}$ as given in Proposition 7.10. From such an extension, we also have $\| \tilde{H}\| = \| h\|_{\mathcal{M}_{\varphi*,w}} = 1$ . Now, we show that $P_{\varphi*,w}(h) = 1$ . Assume for the contrary that $P_{\varphi*,w}(h) < 1$ . Define a function $g(\lambda) = P_{\varphi*,w}(\frac{h}{\lambda})$ . In view of Theorem 4.12 and from the fact that $\varphi_{*}$ satisfies the appropriate $\Delta_{2}$ -condition, the function

$g$ is continuous on $(0,\infty)$ . Note that $g(\lambda)$ is a strictly decreasing function. Then there exists $\lambda_0 < 1$ such that $P_{\varphi_{*},w}(\frac{h}{\lambda_0}) = 1$ , which is a contradiction to the fact that $\| h\|_{\mathcal{M}_{\varphi ,w}} = 1$ .

If $S \neq 0$ , we have $1 < P_{\varphi_{*},w}(h) + \|S\| = 1 + \|S\|$ . The function $f(\lambda) = P_{\varphi_{*},w}\left(\frac{h}{\lambda}\right) + \frac{1}{\lambda}\|S\|$ is continuous on $(0,\infty)$ by Theorem 4.12 and by the fact that $\varphi_{*}$ satisfies the appropriate $\Delta_{2}$ -condition. Since $f(1) > 1$ , there exists $\lambda_0 > 1$ such that $P_{\varphi_{*},w}\left(\frac{h}{\lambda_0}\right) + \frac{1}{\lambda_0}\|S\| > 1$ . But then, this implies $\|H + S\| \geq \lambda_0 > 1 = \|H\|$ by Theorem 7.6. Thus, $\tilde{H}$ is the only norm-preserving extension of $H$ to $\Lambda_{\varphi,w}^{0}$ .

# REFERENCES

[1] C. D. Aliprantis and O. Burkinshaw, Positive operators, Springer, Netherlands, 2006.   
[2] C. Bennett and R. Sharpley, Interpolation of Operators, Academic Press, 1988.   
[3] L. Bernal-González, D. Rodriguez-Vidanes, J. Seoane-Sepulveda, and H. Tag, New results in analysis of Orlicz-Lorentz spaces, arXiv preprint, arXiv:2312.13903.   
[4] J. Cerda, H. Hudzik, A. Kamińska, M. Mastylo, Geometric properties of symmetric spaces with application to Orlicz-Lorentz spaces, Positivity, 2 (1998), 311-337.   
[5] S. Chen, Geometry of Orlicz Spaces, Dissertationes Math., Warszawa, 1996.   
[6] J. Diestel and J. J. Uhl, Vector Measures, Mathematical Surveys, No. 15. American Mathematical Society, Providence, R.I., 1977.   
[7] P. Foralewski, H. Hudzik, and P. Kolwicz, Non-squareness properties of Orlicz-Lorentz function spaces, J. Inequal. and Appl., (2013), Article No. 32.   
[8] P. Foralewski, K. Lesnik and L. Maligranda, Some remarks on level functions and their applications, Comment. Math., 56 (2016), no. 1, 55-86.   
[9] I. Halperin, Function spaces, Canad. J. Math., 5, 1953, 273-288.   
[10] P. Harmard, D. Werner and W. Werner, M-ideals in Banach Spaces and Banach Algebras, Lecture Notes in Mathematics 1547, Springer-Verlag 1993.   
[11] A. Kamińska, Some remarks on Orlicz-Lorentz spaces, Math. Nachr. 147 (1990), 29-38.   
[12] A. Kamińska, K. Lesnik and Y. Raynaud, *Dual spaces to Orlicz-Lorentz spaces*, Studia Math., **222** (2014), no. 3, 229–261.   
[13] A. Kamińska, H. J. Lee, and H. Tag, M-ideal properties in Orlicz-Lorentz spaces, Houston J. of Math. 45 (2019), no. 1, 213–232.   
[14] A. Kamińska, H. J. Lee, and H. Tag, Daugavet and diameter two properties in Orlicz-Lorentz spaces, J. Math. Anal. and Appl., 529 (2024), issue 2, 127289.   
[15] A. Kamińska, H. J. Lee, and H. Tag, Diameter two properties and Radon-Nikodym property in Orlicz spaces, Indag. Math. (N.S.), 31 (2020), issue 5, 848-862.   
[16] A. Kamińska and Y. Raynaud, New formulas for decreasing rearrangements and a class of Orlicz-Lorentz spaces, Rev. Mat. Complut. 27 (2014), no. 2, 587-621.   
[17] A. Kamińska and Y. Raynaud, Abstract Lorentz spaces and Kothe duality, Indag. Math. (N.S.), 30 (2019), issue 4, 553-595.   
[18] A. Kamińska and H. Tag, Diameter of Weak Neighborhoods and the Radon-Nikodym Property in Orlicz-Lorentz spaces, J. Convex. Anal. 24 (2017), issue 3, 969-985.   
[19] M. A. Krasnoselskii and Ya. B. Rutickii, Convex Functions and Orlicz Spaces, Groningen 1961.   
[20] S. G. Krein, Ju. I. Petunin and E. M. Semenov, Interpolation of Linear Operators, AMS Translations of Math. Monog. 54, Providence, 1982.   
[21] A. Lima, On M-ideals and best approximation, Indiana. Univ. Math. J. 31 (1982), 27-36.   
[22] G. G. Lorentz, Bernstein Polynomials, Univ. of Toronto Press, Toronto, 1953.   
[23] M. Rao and Z. Ren, Theory of Orlicz spaces, Decker Inc., New York, 1991.   
[24] H.-U. Schwarz, Banach lattices and operators, Teubner-Texte in Math. 71, Leipzig, 1984.   
[25] G. Sinnamon, Spaces defined by the level function and their duals, Studia Math. 111 (1994), no. 1, 19-52.   
[26] G. Sinnamon, The level function in rearrangement invariant spaces, Publ. Math. 45 (2001), no. 1, 175-198.   
[27] J. Wang and Y. Chen, Rotundity and uniform rotundity of Orlicz-Lorentz spaces with the Orlicz norm, Houston J. Math., 38 (2012), no. 1, 131-151.   
[28] J. Wang and Z. Ning, Rotundity and uniform rotundity of Orlicz-Lorentz sequence spaces equipped with the Orlicz norm, Math. Nachr., 284 (2011), 2297-2311.

[29] C. X. Wu and L. W. Ren, Strict convexity of Orlicz-Lorentz spaces with the Orlicz norm, J. of Math. 19 (1999), 235-240, in Chinese.   
[30] A. C. Zaanen, Integration, North-Holland Publishing Co., Amsterdam, 1967.

DEPARTMENT OF MATHEMATICAL SCIENCES, THE UNIVERSITY OF MEMPHIS, TN 38152-3240  
Email address: kaminska@memphis.edu

DEPARTMENT OF MATHEMATICS EDUCATION, DONGGUK UNIVERSITY, SEOUL, REPUBLIC OF KOREA  
Email address: hjtag4@gmail.com