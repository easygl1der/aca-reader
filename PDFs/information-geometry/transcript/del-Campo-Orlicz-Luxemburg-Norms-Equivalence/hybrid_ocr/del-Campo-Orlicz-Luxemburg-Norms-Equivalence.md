# When and where the Orlicz and Luxemburg (quasi-) norms are equivalent?

![](images/4a257c6fe1770309c574cab84847adf23408dac707d77c3da00ecd8e703cbc2c.jpg)

Ricardo del Campo<sup>a</sup>, Antonio Fernández<sup>b,*</sup>, Fernando Mayoral<sup>b</sup>, Francisco Naranjo<sup>b</sup>, Enrique A. Sánchez-Pérez<sup>c</sup>

a Dpto. Matemática Aplicada I, Universidad de Sevilla, EUITA, Ctra. de Utrera Km. 1, 41013-Sevilla, Spain   
b Dpto. Matemática Aplicada II, Escuela Técnica Superior de Ingeniería, Camino de los Descubrimientos, s/n, 41092-Sevilla, Spain   
c Instituto Universitario de Matematica Pura y Aplicada, Universitat Politècnica de València, Camino de Vera, s/n, 46022-Valencia, Spain

# ARTICLE INFO

Article history:

Received 12 November 2019

Available online 9 June 2020

Submitted by J. Maly

Keywords:

Banach function space

Vector measure

Orlicz space

Orlicz norm

Luxemburg norm

Strictly monotone norm

# ABSTRACT

We study the equivalence between the Orlicz and Luxemburg (quasi-) norms in the context of the generalized Orlicz spaces associated to an N-function $\Phi$ and a (quasi-) Banach function space $X$ over a positive finite measure $\mu$ . We show that the Orlicz and the Luxemburg spaces do not coincide in general, and also that under mild requirements ( $\sigma$ -Fatou property, strictly monotone renorming) the coincidence holds. We use as a technical tool the classes $L_w^\Phi(m)$ , $L^\Phi(m)$ and $L^\Phi(||m||)$ of Orlicz spaces of scalar integrable functions with respect to a Banach-space-valued countably additive vector measure $m$ , providing also some new results on these spaces.

© 2020 Elsevier Inc. All rights reserved.

# 1. Introduction

It is well-known that classical Orlicz spaces allow a double metric description: the so-called Orlicz and Luxemburg norms give equivalent formulas for norming the space. This provides some fundamental tools for the analysis of these spaces, and is one of the reasons why the theory of Orlicz spaces is so fruitful ([12,14,17-19]). The same construction that produces this class of spaces allows also to create a well characterized class of lattices of (classes of) measurable functions. Indeed, if $X$ is a quasi-Banach function space over a measure $\mu$ and

$\Phi$ is a Young function, we can define the Luxemburg space as $X_{L}^{\Phi} \coloneqq \left\{f \in L^{0}(\mu) : \exists c > 0 : \Phi\left(\frac{|f|}{c}\right) \in X\right\}$ (see for example [12,17]). If $f \in X_{L}^{\Phi}$ , the Luxemburg (lattice) quasi-norm is given by

$$
\| f \| _ {X _ {L} ^ {\Phi}} := \inf \left\{c > 0: \Phi \left(\frac {| f |}{c}\right) \in X \mathrm {w i t h} \left\| \Phi \left(\frac {| f |}{c}\right) \right\| _ {X} \leq 1 \right\}.
$$

If $\Phi$ is an N-function and $\hat{\Phi}$ is the complementary function of $\Phi$ , the Orlicz space is defined as

$$
X _ {O} ^ {\Phi} := \left\{f \in L ^ {0} (\mu): \| f \| _ {X _ {O} ^ {\Phi}} <   \infty \right\},
$$

where the Orlicz quasi-norm is defined by

$$
\left\| f \right\| _ {X _ {O} ^ {\Phi}} := \sup  \left\{\left\| f g \right\| _ {X}: \hat {\Phi} (| g |) \in X, \left\| \hat {\Phi} (| g |) \right\| _ {X} \leq 1 \right\}.
$$

In the case of the classical Orlicz spaces —when the space $X$ is $L^1(\mu)$ —, the inequalities

$$
\| f \| _ {L ^ {1} (\mu) _ {L} ^ {\Phi}} \leq \| f \| _ {L ^ {1} (\mu) _ {O} ^ {\Phi}} \leq 2 \| f \| _ {L ^ {1} (\mu) _ {L} ^ {\Phi}}, \quad f \in L ^ {\Phi} (\mu) \tag {1}
$$

provide the double way of describing the classical space $L^{\Phi}(\mu)$ . That is, $L^{1}(\mu)_{L}^{\Phi} = L^{1}(\mu)_{O}^{\Phi} \eqqcolon L^{\Phi}(\mu)$ with equivalent norms.

The aim of this paper is to analyze up to which point the same can be said for the general case. That is, to what extent it can be said that the quasi-norms $\| \cdot \|_{X_L^\Phi}$ and $\| \cdot \|_{X_O^\Phi}$ are equivalent and in which space this occurs. The main problem that arises when facing this issue is to know in which spaces these quasi-norms can be compared. One of our main results states that the spaces $X_O^\Phi$ and $X_L^\Phi$ are in general different (Example 4.1), and so the quasi-norms can only be compared in the smallest one. Under some natural assumptions on the function $\Phi$ , coincidence of these spaces and equivalence of the quasi-norms is assured with the hypotheses of the $\sigma$ -Fatou property for the space $X$ and the existence of a suitable strictly monotone renorming for it (Theorem 5.12). If the $\sigma$ -Fatou property is not assumed, again the existence of a strictly monotone renorming gives the equivalence of both quasi-norms in the smallest space $X_L^\Phi$ (Theorem 5.13). It must be said that the issue that we face in the present paper was previously studied in [10], in which the $\sigma$ -Fatou property is assumed in the definition of quasi-Banach function space. In [10, Theorem 5.1] the authors prove that the norms are in general equivalent, but it is implicitly assumed that the spaces $X_L^\Phi$ and $X_O^\Phi$ (in our notation) coincide, what is not in general true, as we show in the present paper.

Our results are presented in six sections. After two introductory parts, we present in Section 3 the basics on the Luxemburg and Orlicz (quasi-) Banach function spaces associated to a quasi-Banach function space $X$ . In particular, the continuous inclusion $X_{L}^{\Phi} \subseteq X_{O}^{\Phi}$ is proved for general $X$ and $\Phi$ . We will use the general representation of (quasi-) Banach function spaces provided by the vector measure integration as a central technical tool. Essentially, this integration theory allows us to write any order continuous Banach function space with a weak order unit as a space of integrable functions $L^{1}(m)$ with respect to a countably additive vector measure $m$ (see for example [16, Ch. 3]). These spaces will be explained in Section 4. Besides, Orlicz spaces of integrable functions with respect to a vector measure are introduced also as an auxiliary tool in Subsection 4.3. The counterexample that shows that in general $X_{L}^{\Phi}$ and $X_{O}^{\Phi}$ are not equal is presented there. In Section 5 we introduce the notion of strictly monotone (quasi-) norm, and using it we prove broad sufficient conditions for the equality $X_{L}^{\Phi} = X_{O}^{\Phi}$ and the equivalence of the corresponding quasi-norms. Finally, we present in Section 6 some positive results in which the condition of having an equivalent strictly monotone renorming for the space $X$ is fulfilled. Concretely, we prove that every L-convex quasi-Banach function space $X$ —that is, spaces with some $r$ -convexity— with the $\sigma$ -Fatou property satisfies that the associated Orlicz and Luxemburg spaces coincide. This covers all the usual cases of quasi-Banach function

spaces. However, some additional information is also provided: for any quasi-Banach function space $X$ with the $\sigma$ -Fatou property and some $(r,1)$ -concavity, equality $X_{L}^{\Phi} = X_{O}^{\Phi}$ is also satisfied for every N-function $\Phi$ .

# 2. Preliminaries and notation

Throughout this paper, we shall always assume that $\Omega$ is a nonempty set, $\Sigma$ is a $\sigma$ -algebra of subsets of $\Omega$ , $\mu$ is a finite positive measure defined on $\Sigma$ and $L^0(\mu)$ is the space of ( $\mu$ -a.e. equivalence classes of) measurable functions $f: \Omega \longrightarrow \mathbb{R}$ equipped with the topology of convergence in measure.

Recall that a quasi-normed space is any vector space $X$ equipped with a quasi-norm, that is, a function $\| \cdot \|_X : X \longrightarrow [0, \infty)$ which satisfies the following axioms:

(Q1) $\| f\|_{X} = 0$ if and only if $f = 0$   
(Q2) $\| \alpha f\| _X = |\alpha |\| f\| _X$ , for $\alpha \in \mathbb{R}$ and $f\in X$   
(Q3) There exists $K \geq 1$ such that $\|f + g\|_X \leq K (\|f\|_X + \|g\|_X)$ , for all $f, g \in X$ .

The constant $K$ in (Q3) is called a quasi-triangle constant of $X$ . Of course if we can take $K = 1$ , then $\| \cdot \|_X$ is a norm and $X$ is a normed space. A quasi-normed function space over $\mu$ is any quasi-normed space $X$ satisfying the following properties:

(a) $X$ is an ideal in $L^0 (\mu)$ and a quasi-normed lattice with respect to the $\mu$ -a.e. order, that is, if $f\in L^{0}(\mu)$ , $g\in X$ and $|f|\leq |g|$ $\mu$ -a.e., then $f\in X$ and $\| f\| _X\leq \| g\| _X$ .   
(b) The characteristic function of $\Omega$ , $\chi_{\Omega}$ , belongs to $X$ .

If, in addition, the quasi-norm $\| \cdot \| _X$ happens to be a norm, then $X$ is called a normed function space. Note that, with this definition, any quasi-normed function space over $\mu$ is continuously embedded into $L^0 (\mu)$ , as it is proved in [16, Proposition 2.2].

We say that a quasi-normed function space $X$ has the $\sigma$ -Fatou property if for any positive increasing sequence $(f_n)_n$ in $X$ with $\sup_n \| f_n \|_X < \infty$ and converging $\mu$ -a.e. to a function $f$ , we have that $f \in X$ and $\| f \|_X = \sup_n \| f_n \|_X$ . A quasi-normed function space $X$ is said to be $\sigma$ -order continuous if for any positive increasing sequence $(f_n)_n$ in $X$ converging $\mu$ -a.e. to a function $f \in X$ , we have that $\| f - f_n \|_X \to 0$ .

A complete quasi-normed function space is called a quasi-Banach function space. If, in addition, the quasi-norm happens to be a norm, then $X$ is called a Banach function space. It is known that if a quasi-normed function space has the $\sigma$ -Fatou property, then it is complete and hence a quasi-Banach function space (see [16, Proposition 2.35]) and that inclusions between quasi-Banach function spaces are automatically continuous (see [16, Lemma 2.7]). However, in this work we will also consider function spaces without the $\sigma$ -Fatou property.

# 3. Luxemburg and Orlicz (quasi-) Banach function spaces

Recall that a Young function is any function $\Phi : [0, \infty) \longrightarrow [0, \infty)$ which is strictly increasing, convex (hence continuous), $\Phi(0) = 0$ and $\lim_{x \to \infty} \Phi(x) = \infty$ . A Young function $\Phi$ satisfies the following useful inequalities (which we will use later) for all $x \geq 0$ :

$$
\Phi (\alpha x) \leq \alpha \Phi (x) \quad \text {i f} \quad 0 \leq \alpha \leq 1, \tag {2}
$$

$$
\Phi (\alpha x) \geq \alpha \Phi (x) \quad \text {i f} \quad \alpha \geq 1. \tag {3}
$$

A Young function $\Phi$ is called an $N$ -function if $\Phi$ satisfies the limit conditions $\lim_{x \to 0} \frac{\Phi(x)}{x} = 0$ and $\lim_{x \to \infty} \frac{\Phi(x)}{x} = \infty$ . N-functions are a useful nice class of Young functions for which its complementary functions are also N-functions (see [17, p. 13]).

A Young function $\Phi$ has the $\Delta_2$ -property, written $\Phi \in \Delta_2$ , if there exists a constant $C > 1$ such that $\Phi(2x) \leq C\Phi(x)$ for all $x \geq 0$ .

Next we introduce the Luxemburg and Orlicz quasi-Banach function spaces whose relations will be the aim of our work. See [4] for detailed study about these spaces that have also been considered in [10] in the setting of Banach function spaces with the $\sigma$ -Fatou property.

Let $\Phi$ be a Young function. Given a quasi-normed function space (respectively, normed function space) $X$ over $\mu$ , the corresponding (generalized) Orlicz class $\widetilde{X}^{\Phi}$ is defined as the following set:

$$
\widetilde {X} ^ {\Phi} := \left\{f \in L ^ {0} (\mu): \Phi (| f |) \in X \right\}.
$$

The Orlicz class $\widetilde{X}^{\Phi}$ is a solid convex set in $L^0 (\mu)$ . Moreover, $\widetilde{X}^{\Phi}\subseteq X$ .

The (generalized) Luxemburg space $X_L^\Phi$ is defined as the following set:

$$
X _ {L} ^ {\Phi} := \left\{f \in L ^ {0} (\mu): \exists c > 0: \frac {| f |}{c} \in \widetilde {X} ^ {\Phi} \right\}.
$$

The Luxemburg space $X_{L}^{\Phi}$ is a linear space, an ideal in $L^0 (\mu)$ and $\widetilde{X}^{\Phi}\subseteq X_{L}^{\Phi}\subseteq X$ (see [4, Proposition 4.4]). Given $f\in X_L^\Phi$ , we define the Luxemburg lattice quasi-norm (respectively, norm) of $f$ by

$$
\| f \| _ {X _ {L} ^ {\Phi}} := \inf  \left\{c > 0: \frac {| f |}{c} \in \widetilde {X} ^ {\Phi} \text {w i t h} \left\| \Phi \left(\frac {| f |}{c}\right) \right\| _ {X} \leq 1 \right\}. \tag {4}
$$

The Luxemburg space $X_{L}^{\Phi}$ equipped with the Luxemburg quasi-norm, is really a quasi-normed (respectively, normed) function space over $\mu$ with the same quasi-triangle constant as the one of the quasi-norm of $X$ . Moreover, properties as completeness, $\sigma$ -Fatou, and $\sigma$ -order continuity (in that case the Young function $\Phi$ must have additionally the $\Delta_2$ -property) are transferred from $X$ to $X_{L}^{\Phi}$ . See [4] for details.

Consider the complementary function of the Young function $\Phi$ , defined as

$$
\hat{\Phi} (y):= \sup_{x\geq 0}\{xy - \Phi (x)\} ,
$$

for all $y \geq 0$ . From the definition of $\hat{\Phi}$ it is clear that $\Phi$ and $\hat{\Phi}$ satisfy the Young inequality

$$
x y \leq \Phi (x) + \hat {\Phi} (y), \quad x, y \geq 0. \tag {5}
$$

It is well known (see [12, Theorem 1.1] or [17, Theorem 1.3.1]) that for a Young function $\Phi$ there exists a non-decreasing, right continuous function $\varphi :[0,\infty)\longrightarrow [0,\infty)$ , with $\varphi (0) = 0$ , such that $\Phi (x) = \intop_{0}^{x}\varphi (t)dt$ for all $x\in [0,\infty)$ . Such function $\varphi$ is called the right derivative of the function $\Phi$ . This function $\varphi$ satisfies the following equality (see [12, (2.7)] or [17, Theorem 1.3.3]) that we will use later

$$
x \varphi (x) = \Phi (x) + \hat {\Phi} (\varphi (x)), \quad x \geq 0. \tag {6}
$$

Let $\Phi$ be an N-function. Given a quasi-normed function space (respectively, normed function space) $X$ over $\mu$ , the corresponding (generalized) Orlicz space $X_{O}^{\Phi}$ is defined as the following set:

$$
X _ {O} ^ {\Phi} := \left\{f \in L ^ {0} (\mu): \| f \| _ {X _ {O} ^ {\Phi}} <   \infty \right\},
$$

where $\| \cdot \|_{X_O^\Phi}$ is the Orlicz quasi-norm (respectively, norm) defined by

$$
\left\| f \right\| _ {X _ {O} ^ {\Phi}} := \sup  \left\{\| f g \| _ {X}: g \in \widetilde {X} ^ {\hat {\Phi}}, \left\| \hat {\Phi} (| g |) \right\| _ {X} \leq 1 \right\}. \tag {7}
$$

The Orlicz space $X_O^\Phi$ is a linear space, an ideal in $L^0(\mu)$ and $\widetilde{X}^\Phi \subseteq X_O^\Phi \subseteq X$ . In fact, the following inequalities hold

$$
\begin{array}{l} \| f \| _ {X _ {O} ^ {\Phi}} \leq K \left(\| \Phi (| f |) \| _ {X} + 1\right), \quad f \in \widetilde {X} ^ {\Phi} \\ \| f \| _ {X} \leq \frac {1}{\hat {\Phi} ^ {- 1} \left(\frac {1}{\| \chi_ {\Omega} \| _ {X}}\right)} \| f \| _ {X _ {O} ^ {\Phi}}, \quad f \in X _ {O} ^ {\Phi}, \tag {8} \\ \end{array}
$$

where $K$ is a quasi-triangle constant of $X$ . Moreover, $X_{O}^{\Phi}$ equipped with the Orlicz quasi-norm, is really a quasi-normed (respectively, normed) function space over $\mu$ with the same quasi-triangle constant as the one of the quasi-norm of $X$ . Moreover, as we will see next, properties as completeness or $\sigma$ -Fatou are transferred from $X$ to $X_{O}^{\Phi}$ . However, the Orlicz space $X_{O}^{\Phi}$ does not have to be $\sigma$ -order continuous even if the space $X$ has that property and $\Phi \in \Delta_2$ (see the next Example 4.1).

Proposition 3.1. Let $\Phi$ be an $N$ -function and $X$ be a quasi-Banach function space over $\mu$ . Then $X_{O}^{\Phi}$ is a quasi-Banach function space over $\mu$ .

Proof. We are going to prove only the completeness of $X_{O}^{\Phi}$ . To do this we will use the Amemiya's theorem for quasi-normed lattices (see [4, Theorem 3.2]). It is enough to prove that for every positive increasing Cauchy sequence $(f_n)_n$ in $X_{O}^{\Phi}$ there exists $\sup_{n} f_n \in X_{O}^{\Phi}$ . By applying (8) it is easy to see that $(f_n)_n$ is Cauchy in $X$ , and so there exists $f \in X$ such that $\|f - f_n\|_X \to 0$ as $n \to \infty$ . Consequently $f = \sup_{n} f_n$ . Now take $g \in \tilde{X}^{\hat{\Phi}}$ with $\left\|\hat{\Phi}(|g|)\right\|_X \leq 1$ . Then $0 \leq f_n |g| \uparrow f |g|$ a.e. On the other hand, $(f_n g)_n$ is Cauchy in $X$ because $\|f_m g - f_n g\|_X \leq \|f_m - f_n\|_{X_O^{\Phi}}$ for all $m, n = 1, 2, \ldots$ . Then there exists a function $h_g \in X$ such that $\|f_n g - h_g\|_X \to 0$ as $n \to \infty$ . Convergence on $X$ implies convergence for subsequences a.e. Consequently $h_g = f |g|$ a.e. and $\|f_n g - f |g\|_X \to 0$ as $n \to \infty$ . Take $n \geq 1$ such that $\|f_n g - f |g\|_X \leq 1$ , and denote by $K$ the quasi-triangle constant of $X$ . Then

$$
\| f g \| _ {X} = \| f | g | \| _ {X} \leq K \| f | g | - f _ {n} g \| _ {X} + K \| f _ {n} g \| _ {X} \leq K + K \| f _ {n} \| _ {X _ {O} ^ {\Phi}} \leq K \left(1 + \sup  _ {n} \| f _ {n} \| _ {X _ {O} ^ {\Phi}}\right) <   \infty
$$

because $(f_n)_n$ is bounded in $X_O^\Phi$ . Thus $f \in X_O^\Phi$ as we wanted to see.

Proposition 3.2. Let $\Phi$ be an $N$ -function and $X$ be a quasi-normed function space over $\mu$ with the $\sigma$ -Fatou property. Then $X_{O}^{\Phi}$ has the $\sigma$ -Fatou property.

Proof. Take an increasing positive sequence $(f_n)_n \subseteq X_O^\Phi$ converging $\mu$ -a.e. to a function $f$ such that $M := \sup_n \| f_n \|_{X_O^\phi} < \infty$ . By applying (8) we get $\sup_n \| f_n \|_X \leq \frac{M}{\hat{\Phi}^{-1}\left(\frac{1}{\|X_\Omega \|_X}\right)}$ , and having in mind that $X$ has the $\sigma$ -Fatou property, it follows that $f \in X$ . Now take $g \in \tilde{X}^{\hat{\Phi}}$ with $\left\| \hat{\Phi}(|g|) \right\|_X \leq 1$ . Then we have $0 \leq f_n |g| \uparrow f |g|$ $\mu$ -a.e. and also that $\| fg \|_X \leq \| f_n \|_{X_O^\Phi} \leq M$ . Consequently $f |g| \in X$ and moreover

$\| fg\|_{X} = \sup_{n}\| f_{n}g\|_{X}\leq M$ by the $\sigma$ -Fatou property of $X$ . Taking suprema on $g$ it follows that $f\in X_O^\Phi$ and $\| f\|_{X_O^\Phi}\leq M = \sup_n\| f_n\|_{X_O^\Phi}$ . The converse inequality is obvious.

Proposition 3.3. Let $\Phi$ be an $N$ -function and $X$ be a quasi-normed function space over $\mu$ with quasi-triangle constant $K \geq 1$ . Then $X_L^\Phi \subseteq X_O^\Phi$ holds and

$$
\left\| f \right\| _ {X _ {O} ^ {\Phi}} \leq 2 K \left\| f \right\| _ {X _ {L} ^ {\Phi}}, \quad f \in X _ {L} ^ {\Phi}. \tag {9}
$$

Proof. Take a function $f \in X_L^\Phi$ and let $c > 0$ be such that $\frac{f}{c} \in \widetilde{X}^\Phi$ with $\left\| \Phi \left( \frac{|f|}{c} \right) \right\|_X \leq 1$ . By the Young inequality (5) we have $\frac{|f|}{c} |g| \leq \Phi \left( \frac{|f|}{c} \right) + \hat{\Phi}(|g|)$ for all $g \in \widetilde{X}^{\hat{\Phi}}$ with $\left\| \hat{\Phi}(|g|) \right\|_X \leq 1$ , and taking quasi-norm

$$
\frac {1}{c} \left\| f g \right\| _ {X} = \left\| \frac {f}{c} g \right\| _ {X} \leq K \left(\left\| \Phi \left(\frac {| f |}{c}\right) \right\| _ {X} + \left\| \hat {\Phi} (| g |) \right\| _ {X}\right) \leq 2 K.
$$

Thus $\| f\|_{X_O^\Phi}\leq 2Kc$ , and finally taking infimum in $c$ we obtain $\| f\|_{X_O^\Phi}\leq 2K\| f\|_{X_L^\Phi}$ as we wanted to prove. $\square$

# 4. Integrable function spaces and Orlicz spaces respect to a vector measure

In this section we will describe a class of Banach function spaces $X$ for which the corresponding Orlicz and Luxemburg spaces do not match, that is, $X_{L}^{\Phi} \subsetneq X_{O}^{\Phi}$ .

# 4.1. Lebesgue spaces with respect to a vector measure

Given a countably additive vector measure $m:\Sigma \to Y$ with values in a real Banach space $Y$ , there are several ways of constructing (quasi-) Banach function spaces of integrable functions. Let us recall them briefly. The semivariation of $m$ is the finite subadditive set function defined on $\Sigma$ by

$$
\left\| m \right\| (A) := \sup  \left\{\left| \langle m, y ^ {*} \rangle \right| (A): y ^ {*} \in B _ {Y ^ {*}} \right\},
$$

where $|\langle m, y^{*} \rangle|$ denotes the variation of the scalar measure $\langle m, y^{*} \rangle : \Sigma \to \mathbb{R}$ given by $\langle m, y^{*} \rangle(A) := \langle m(A), y^{*} \rangle$ for all $A \in \Sigma$ , and $B_{Y^{*}}$ is the unit ball of $Y^{*}$ , the dual space of $Y$ . A set $A \in \Sigma$ is called $m$ -null if $\| m \|(A) = 0$ . A measure $\mu := |\langle m, y^{*} \rangle|$ , where $y^{*} \in B_{Y^{*}}$ , that is equivalent to $m$ (in the sense that $\| m \|(A) \to 0$ if and only if $\mu(A) \to 0$ ) is called a Rybakov control measure for $m$ . Such a measure always exists (see [7, Theorem 2, p. 268]). Let $L^0(m)$ be the space of (m-a.e. equivalence classes of) measurable functions $f: \Omega \longrightarrow \mathbb{R}$ . Thus, $L^0(m)$ and $L^0(\mu)$ are just the same whenever $\mu$ is a Rybakov control measure for $m$ , and allows to define equivalence classes of $m$ -a.e. functions as the ones that are equal $\mu$ -a.e.

A measurable function $f: \Omega \longrightarrow \mathbb{R}$ is called weakly integrable (with respect to $m$ ) if $f$ is integrable with respect to $|\langle m, y^* \rangle|$ for all $y^* \in Y^*$ . A weakly integrable function $f$ is said to be integrable (with respect to $m$ ) if, for each $A \in \Sigma$ there exists an element (necessarily unique) $\int_{A} f dm \in Y$ , satisfying

$$
\left\langle \int_ {A} f d m, y ^ {*} \right\rangle = \int_ {A} f d \langle m, y ^ {*} \rangle , \quad y ^ {*} \in Y ^ {*}.
$$

Let $L_w^1(m)$ be the space of all (m-a.e. equivalence classes of) weakly integrable functions, and let $L^1(m)$ the space of all (m-a.e. equivalence classes of) integrable functions. Letting $\mu$ be any Rybakov control measure

for $m$ , we have that $L_w^1(m)$ becomes a Banach function space over $\mu$ with the $\sigma$ -Fatou property when endowed with the norm

$$
\| f \| _ {L _ {w} ^ {1} (m)} := \sup  \left\{\int_ {\Omega} | f | d | \langle m, y ^ {*} \rangle |: y ^ {*} \in B _ {Y ^ {*}} \right\}.
$$

Moreover, $L^1(m)$ is a closed $\sigma$ -order continuous ideal of $L_w^1(m)$ . In fact, it is the closure of $\mathcal{S}(\Sigma)$ , the space of simple functions supported on $\Sigma$ . Thus, $L^1(m)$ is a $\sigma$ -order continuous Banach function space over $\mu$ endowed with the same norm (see [16, Theorem 3.7] and [16, p. 138]).

We will denote by $L^{\infty}(m)$ the Banach function space of all ( $m$ -a.e. equivalence classes of) essentially bounded functions equipped with the essential sup-norm.

# 4.2. Choquet spaces with respect to the semivariation

Given a measurable function $f: \Omega \longrightarrow \mathbb{R}$ , we will also consider its distribution function (with respect to the semivariation of the vector measure $m$ )

$$
\left\| m \right\| _ {f}: t \in [ 0, \infty) \longrightarrow \left\| m \right\| _ {f} (t) := \left\| m \right\| \left(\left[ \left| f \right| > t \right]\right) \in [ 0, \infty),
$$

where $|f| > t \coloneqq \{w \in \Omega : |f(w)| > t\}$ . This distribution function is bounded, non-increasing and right-continuous.

Let $L^1(\|m\|)$ be the space of all (m-a.e. equivalence classes of) measurable functions $f$ such that its distribution function $\|m\|_f$ is Lebesgue integrable in $(0, \infty)$ . It is known that $L^1(\|m\|)$ equipped with the quasi-norm

$$
\| f \| _ {L ^ {1} (\| m \|)} := \int_ {0} ^ {\infty} \| m \| _ {f} (t) d t
$$

is a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property (see [2, Proposition 3.1]) and it is also $\sigma$ -order continuous (see [2, Proposition 3.6]).

Finally note that the following inclusions

$$
L ^ {\infty} (m) \subseteq L ^ {1} (\| m \|) \subseteq L ^ {1} (m) \subseteq L _ {w} ^ {1} (m) \subseteq L ^ {0} (m) \tag {10}
$$

are all continuous. See for instance [8, Proposition 3.4], particularly for the second inclusion. In general, all these inclusions are strict inclusions. Sufficient conditions for the equality $L^{1}(m) = L_{w}^{1}(m)$ were given in [13].

# 4.3. Orlicz spaces with respect to a vector measure

First of all observe that classical Orlicz spaces $L^{\Phi}(\mu)$ with respect to a positive finite measure $\mu$ and an N-function $\Phi$ are obtained applying the constructions $X_{L}^{\Phi}$ and $X_{O}^{\Phi}$ of Section 3 to the Banach function space $X = L^{1}(\mu)$ , that is, $L^{1}(\mu)_{L}^{\Phi} = L^{1}(\mu)_{O}^{\Phi} = L^{\Phi}(\mu)$ equipped with the norm $\| \cdot \|_{L^{\Phi}(\mu)} \coloneqq \| \cdot \|_{L^{1}(\mu)_{L}^{\Phi}}$ which results in equivalent to $\| \cdot \|_{L^{1}(\mu)_{O}^{\Phi}}$ as it is well known. Using these classical spaces $L^{\Phi}(\mu)$ , new Orlicz spaces $L_w^\Phi (m)$ and $L^{\Phi}(m)$ with respect to a vector measure $m:\Sigma \to Y$ were introduced in [6] in the following way:

$$
L _ {w} ^ {\Phi} (m) := \left\{f \in L ^ {0} (m): f \in L ^ {\Phi} (| \langle m, y ^ {*} \rangle |), \forall y ^ {*} \in Y ^ {*} \right\},
$$

equipped with the norm

$$
\| f \| _ {L _ {w} ^ {\Phi} (m)} := \sup \left\{\| f \| _ {L ^ {\Phi} (| \langle m, y ^ {*} \rangle |)}: y ^ {*} \in B _ {Y ^ {*}} \right\},
$$

and $L^{\Phi}(m)$ is the closure of simple functions $\mathcal{S}(\Sigma)$ in $L_w^\Phi (m)$ . These Orlicz spaces $L_{w}^{\Phi}(m)$ and $L^{\Phi}(m)$ can be obtained as generalized Orlicz spaces $X_{L}^{\Phi}$ by taking $X$ to be $L_w^1 (m)$ and $L^{1}(m)$ , respectively. In fact, if $\Phi$ is an N-function, then $L_{w}^{\Phi}(m) = L_{w}^{1}(m)_{L}^{\Phi}$ and $\| f\|_{L_w^\Phi (m)} = \| f\|_{L_w^1 (m)_L^\Phi}$ , for all $f\in L_w^\Phi (m)$ . In general the inclusion $L^{\Phi}(m)\subseteq L^{1}(m)_{L}^{\Phi}$ holds, but if we also assume $\Phi \in \Delta_2$ , then $L^{\Phi}(m) = L^{1}(m)_{L}^{\Phi} = \widetilde{L^{1}(m)}^{\Phi}$ . See [4, Proposition 5.1] and [4, Theorem 4.13].

Example 4.1. Let $Y$ be a real Banach space and let $m: \Sigma \to Y$ a countably additive vector measure such that the spaces $L^1(m)$ and $L_w^1(m)$ are different. It is worth noting that there are many vector measures $m$ for which $L^1(m) \subsetneq L_w^1(m)$ . See [13] for details on the equality $L^1(m) = L_w^1(m)$ . Let's choose such a measure $m$ with $L^1(m) \neq L_w^1(m)$ . Then, for every N-function $\Phi \in \Delta_2$ such that $\hat{\Phi} \in \Delta_2$ we have

$$
L _ {w} ^ {1} (m) _ {L} ^ {\Phi} = L _ {w} ^ {\Phi} (m) = L _ {w} ^ {1} (m) _ {O} ^ {\Phi}, \tag {11}
$$

$$
L ^ {1} (m) _ {L} ^ {\Phi} = L ^ {\Phi} (m) \subsetneq L _ {w} ^ {\Phi} (m) = L ^ {1} (m) _ {O} ^ {\Phi}. \tag {12}
$$

First let us note that $L^{\Phi}(m) \subsetneq L_w^{\Phi}(m)$ since the function $\Phi$ has the $\Delta_2$ property and we have chosen the measure $m$ so that $L^{1}(m) \subsetneq L_{w}^{1}(m)$ . As we have said before, the equality $L_w^1 (m)_L^\Phi = L_w^\Phi (m)$ has been proved in [4, Proposition 5.1]). The other equality, that is $L_w^\Phi (m) = L_w^1 (m)_O^\Phi$ , will be obtained as a consequence of the next Theorem 5.12 (see also Example 6.1) since the space $L_w^1 (m)$ has the $\sigma$ -Fatou property.

It is also clear the equality $L^1(m)_L^\Phi = L^\Phi(m)$ because the function $\Phi$ has the $\Delta_2$ property. It only remains to establish the equality $L_w^\Phi(m) = L^1(m)_O^\Phi$ . Let us suppose $f \in L_w^\Phi(m)$ and take $g \in \widetilde{L^1(m)}^\hat{\Phi} = L^\hat{\Phi}(m)$ (for this equality we have used that $\hat{\Phi} \in \Delta_2$ ) such that $\left\| \hat{\Phi}(|g|) \right\|_{L^1(m)} \leq 1$ . In this case $\| g \|_{L_w^\hat{\Phi}(m)} \leq 1$ (see [9, Lemma 2.4]). By applying [9, Proposition 4.5] we know that $fg \in L^1(m)$ , and moreover

$$
\| f g \| _ {L ^ {1} (m)} \leq 2 \| f \| _ {L _ {w} ^ {\Phi} (m)} \| g \| _ {L _ {w} ^ {\dot {\Phi}} (m)} \leq 2 \| f \| _ {L _ {w} ^ {\Phi} (m)} <   \infty .
$$

Thus $f \in L^{1}(m)_{O}^{\Phi}$ . For the opposite inclusion let us take now $f \in L^{1}(m)_{O}^{\Phi}$ , that is,

$$
\sup \Bigl \{\| f g \| _ {L ^ {1} (m)}: g \in L ^ {\hat {\Phi}} (m), \left\| \hat {\Phi} (| g |) \right\| _ {L ^ {1} (m)} \leq 1 \Bigr \} <   \infty .
$$

This means in the terminology of [9] that the function $f$ belongs to the multipliers space $\mathcal{M}\left(L^{\hat{\Phi}}(m),L^{1}(m)\right)$ . In the same paper (see [9, Theorem 4.8]) it is proved the equality $\mathcal{M}\left(L^{\hat{\Phi}}(m),L^{1}(m)\right) = L_w^\Phi (m)$ . Thus $f\in L_w^\Phi (m)$ as we wanted to see.

A simpler special case of this general situation appears when we take the N-function $\Phi(x) := \frac{x^p}{p}$ , with $p > 1$ . Then we have $\hat{\Phi}(x) = \frac{x^q}{q}$ , where $\frac{1}{p} + \frac{1}{q} = 1$ . In [1] it is proved that $\mathcal{M}\left(L^p(m), L^1(m)\right) = L_w^q(m)$ . Thus

$$
L ^ {1} (m) _ {L} ^ {\Phi} = L ^ {p} (m) \subsetneq L _ {w} ^ {p} (m) = L ^ {1} (m) _ {O} ^ {\Phi}
$$

that shows again (12).

The Orlicz spaces $L^{\Phi}(m)$ have been recently employed in [3] to locate the compact subsets of $L^{1}(m)$ . Motivated by the idea of studying compactness in $L^{1}(\| m\|)$ in a forthcoming paper [5], we introduced the Orlicz spaces $L^{\Phi}(\| m\|)$ as the Orlicz spaces $X_{L}^{\Phi}$ associated to the quasi-Banach function space $X = L^{1}(\| m\|)$ . For further reference, we collect together some information of [4] about $L^{\Phi}(\| m\|)$ .

Proposition 4.2. Let $\Phi$ be a Young function, $m:\Sigma \to Y$ a vector measure and $\mu$ any Rybakov control measure for $m$ . Then,

(i) $L^{\Phi}(\| m\|)$ is a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property.   
(ii) $L^{\Phi}(\| m\|)\subseteq L^{1}(\| m\|)$ with continuous inclusion.

Moreover, if $\Phi \in \Delta_2$ , then

(iii) $L^{\Phi}(\| m\|)$ is $\sigma$ -order continuous, and   
(iv) $L^{\Phi}(\| m\|) = \big\{f\in L^{0}(m):\Phi (|f|)\in L^{1}(\| m\|)\big\} .$

# 5. Sufficient conditions for the equality $\mathbf{X}_{\mathrm{L}}^{\Phi} = \mathbf{X}_{\mathrm{O}}^{\Phi}$

In this section we will show sufficient conditions for the equality of the spaces $X_{L}^{\Phi}$ and $X_{O}^{\Phi}$ . Since we already know that the inclusion $X_{L}^{\Phi} \subseteq X_{O}^{\Phi}$ is always true for every N-function $\Phi$ , we look for sufficient conditions that guarantee the inequality $\| \cdot \|_{X_{L}^{\Phi}} \leq \| \cdot \|_{X_{O}^{\Phi}}$ of the Luxemburg and Orlicz quasi-norms. For this we need a couple of technical results (Proposition 5.3 and Proposition 5.4) which are the analogues to [12, Lemma 9.1] and [12, Lemma 9.2] for our context.

Lemma 5.1. Let $X$ be a quasi-Banach function space over $\mu$ . If $f \in X_{O}^{\Phi}$ and $g \in \widetilde{X}^{\Phi}$ , then

$$
\left\| f g \right\| _ {X} \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}} \cdot \max  \left\{1, \left\| \hat {\Phi} (| g |) \right\| _ {X} \right\}. \tag {13}
$$

Proof. If $\left\| \hat{\Phi}(|g|)\right\|_X \leq 1$ , from the definition of the Orlicz quasi-norm (7) it follows that

$$
\| f g \| _ {X} \leq \| f \| _ {X _ {O} ^ {\Phi}} = \| f \| _ {X _ {O} ^ {\Phi}} \cdot \max \left\{1, \left\| \hat {\Phi} (| g |) \right\| _ {X} \right\}.
$$

If $\left\| \hat{\Phi} (|g|)\right\|_{X} > 1$ , it follows from inequality (2) that

$$
\hat {\Phi} \left(\frac {| g |}{\left\| \hat {\Phi} (| g |) \right\| _ {X}}\right) \leq \frac {\hat {\Phi} (| g |)}{\left\| \hat {\Phi} (| g |) \right\| _ {X}}.
$$

Then, by the ideal property of the quasi-norm we obtain that

$$
\left\| \hat {\Phi} \left(\frac {| g |}{\left\| \hat {\Phi} (| g |) \right\| _ {X}}\right) \right\| _ {X} \leq \frac {\left\| \hat {\Phi} (| g |) \right\| _ {X}}{\left\| \hat {\Phi} (| g |) \right\| _ {X}} = 1.
$$

Now, from the definition of the Orlicz quasi-norm (7) it follows that

$$
\frac {\left\| f g \right\| _ {X}}{\left\| \hat {\Phi} (| g |) \right\| _ {X}} = \left\| f \frac {g}{\left\| \hat {\Phi} (| g |) \right\| _ {X}} \right\| _ {X} \leq \| f \| _ {X _ {O} ^ {\Phi}},
$$

and from this last inequality we get that

$$
\left\| f g \right\| _ {X} \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}} \cdot \left\| \hat {\Phi} (| g |) \right\| _ {X} = \| f \| _ {X _ {O} ^ {\Phi}} \cdot \max  \left\{1, \left\| \hat {\Phi} (| g |) \right\| _ {X} \right\}.
$$

Definition 5.2. Let $X$ be a quasi-normed function space over the measure $\mu$ . We say that the quasi-norm $\| \cdot \|_X$ of $X$ is strictly monotone if $\| f \|_X < \| g \|_X$ for all $0 \leq f < g \in X$ . As it is usual $f < g$ means that $f \leq g$ and $f \neq g$ in $X$ . In particular, if $f < g$ , then $\mu([f \neq g]) > 0$ .

Proposition 5.3. Let $X$ be a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property and strictly monotone quasi-norm, and let $\varphi$ be the right derivative of the $N$ -function $\Phi$ . If $\| f \|_{X_{\mathcal{O}}^{\Phi}} \leq 1$ , then $g := \varphi(|f|) \in \widetilde{X}^{\hat{\Phi}}$ and satisfies that $\left\| \hat{\Phi}(|g|) \right\|_{X} \leq 1$ .

Proof. Suppose that $\| f \|_{X_O^\Phi} \leq 1$ and denote by $f_n \coloneqq f \chi_{[|f| \leq n]}$ for all $n = 1, 2, \ldots$ . Since $f_n \in L^\infty(\mu)$ it follows that $\varphi(|f_n|) \in L^\infty(\mu) \subseteq \widetilde{X}^{\hat{\Phi}}$ , and so $\hat{\Phi}(\varphi(|f_n|)) \in X$ for all $n = 1, 2, \ldots$ . Moreover $\hat{\Phi}(\varphi(|f_n|)) \uparrow \hat{\Phi}(\varphi(|f|))$ a.e. since $|f_n| \uparrow |f|$ a.e.

Suppose on the contrary that the conclusion of the statement is not satisfied. Then two possibilities appear:

a) $g\coloneqq \varphi (|f|)\notin \widetilde{X}^{\Phi}$ , or   
b) $g\coloneqq \varphi (|f|)\in \widetilde{X}^{\hat{\Phi}}$ but $\left\| \hat{\Phi} (|g|)\right\|_{X} > 1.$

In both cases $a)$ or $b)$ , the $\sigma$ -Fatou property of $X$ ensures that there exists $n_0 \geq 1$ such that $\left\| \hat{\Phi}(\varphi(|f_{n_0}|)) \right\|_X > 1$ . In particular, $|f_{n_0}| > 0$ . In view of (6) we have

$$
\hat {\Phi} \left(\varphi \left(| f _ {n _ {0}} |\right)\right) <   \Phi \left(| f _ {n _ {0}} |\right) + \hat {\Phi} \left(\varphi \left(| f _ {n _ {0}} |\right)\right) = | f _ {n _ {0}} | \varphi \left(| f _ {n _ {0}} |\right).
$$

Taking quasi-norm and having in mind the strict monotonicity property of $X$ together with the inequality (13), we conclude that

$$
\begin{array}{l} \left\| \hat {\Phi} (\varphi (| f _ {n _ {0}} |)) \right\| _ {X} <   \| | f _ {n _ {0}} | \varphi (| f _ {n _ {0}} |) \| _ {X} \leq \| f _ {n _ {0}} \| _ {X _ {O} ^ {\Phi}} \left\| \hat {\Phi} (\varphi (| f _ {n _ {0}} |)) \right\| _ {X} \\ \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}} \left\| \hat {\Phi} \left(\varphi \left(| f _ {n _ {0}} |\right)\right) \right\| _ {X} \leq \left\| \hat {\Phi} \left(\varphi \left(| f _ {n _ {0}} |\right)\right) \right\| _ {X}. \\ \end{array}
$$

This contradiction proves the result.

Proposition 5.4. Let $X$ be a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property and strictly monotone quasi-norm, and let $\Phi$ an $N$ -function.

1) If $\| f \|_{X_{\phi}^{\sigma}} \leq 1$ , then $\| \Phi(|f|) \|_X \leq \| f \|_{X_{\phi}^{\sigma}}$ .   
2) If $0 \neq f \in X_{O}^{\Phi}$ , then

$$
\left\| \Phi \left(\frac {| f |}{\| f \| _ {X _ {O} ^ {\Phi}}}\right) \right\| _ {X} \leq 1. \tag {14}
$$

In particular $f \in X_L^\Phi$ .

Proof. 1) Consider the function $g \coloneqq \varphi(|f|) \geq 0$ , where $\varphi$ is the right derivative of the N-function $\Phi$ . The above Proposition 5.3 tells us that $\left\| \hat{\Phi}(|g|) \right\|_X \leq 1$ . Now, from (6) we have

$$
| f | g = | f | \varphi (| f |) = \Phi (| f |) + \hat {\Phi} (\varphi (| f |)) = \Phi (| f |) + \hat {\Phi} (| g |). \tag {15}
$$

Noting that $\Phi(|f|) \leq \Phi(|f|) + \hat{\Phi}(|g|)$ , taking quasi-norm and using the equality (15) we conclude that

$$
\| \Phi (| f |) \| _ {X} \leq \left\| \Phi (| f |) + \hat {\Phi} (| g |) \right\| _ {X} = \| f g \| _ {X} \leq \| f \| _ {X _ {O} ^ {\Phi}},
$$

as we wanted to see.

2) If $f \neq 0$ , then $\left\| \frac{|f|}{\|f\|_{X_O^\Phi}} \right\|_{X_O^\Phi} = 1$ . From item 1) it follows that

$$
\left\| \Phi \left(\frac {| f |}{\| f \| _ {X _ {O} ^ {\Phi}}}\right) \right\| _ {X} \leq \left\| \frac {| f |}{\| f \| _ {X _ {O} ^ {\Phi}}} \right\| _ {X _ {O} ^ {\Phi}} = 1. \quad \square
$$

Theorem 5.5. Let $X$ be a quasi-Banach function space over $\mu$ , with quasi-triangle constant $K \geq 1$ , with the $\sigma$ -Fatou property and strictly monotone quasi-norm, and let $\Phi$ an $N$ -function. Then $X_{L}^{\Phi} = X_{O}^{\Phi}$ and the Orlicz quasi-norm is equivalent to the Luxemburg quasi-norm. In fact,

$$
\left\| f \right\| _ {X _ {L} ^ {\Phi}} \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}} \leq 2 K \left\| f \right\| _ {X _ {L} ^ {\Phi}}, \quad f \in X _ {L} ^ {\Phi} = X _ {O} ^ {\Phi}. \tag {16}
$$

Proof. From the definition of the Luxemburg quasi-norm (4) together with the inequality (14) we obtain the following important first inequality

$$
\| f \| _ {X _ {L} ^ {\Phi}} \leq \| f \| _ {X _ {O} ^ {\Phi}}, \quad f \in X _ {O} ^ {\Phi}.
$$

The second inequality has been established in (9) of Proposition 3.3. $\square$

Remark 5.6. Let $\mu$ be a finite positive measure. Then the Lebesgue space $X\coloneqq L^{1}(\mu)$ is a Banach function space over $\mu$ with the $\sigma$ -Fatou property and its norm $\| \cdot \|_{L^1 (\mu)}$ is clearly strictly monotone. Thus, the inequalities in (16) give a generalization of the well known equivalence between the Orlicz and Luxemburg norms in classical context (1). Moreover, the proof we have presented of Theorem 5.5 is essentially the only known proof in the literature, as far as we know, of the inequalities (16) and (1).

The $\sigma$ -Fatou assumption for the (quasi-) Banach function space $X$ is essential for the equality $X_{L}^{\Phi} = X_{O}^{\Phi}$ as the strict inclusion (12) of the Example 4.1 points out. Without the $\sigma$ -Fatou property we only have the inclusion $X_{L}^{\Phi} \subseteq X_{O}^{\Phi}$ . In this case, with an strictly monotone quasi-norm on $X$ , we will see that the Orlicz and Luxemburg quasi-norms are still equivalent in the smallest space $X_{L}^{\Phi}$ if we add the hypothesis $\Delta_{2}$ to the N-function $\Phi$ .

The following results are variants of Propositions 5.3, 5.4 and Theorem 5.9, respectively, under this new hypothesis.

Proposition 5.7. Let $X$ be a quasi-Banach function space over $\mu$ with strictly monotone quasi-norm, let $\Phi$ and $N$ -function with the $\Delta_2$ -property and let $\varphi$ be the right derivative of the function $\Phi$ . Suppose that $f \in X_L^\Phi$ with $\| f \|_{X_O^\Phi} \leq 1$ . Then the function $g \coloneqq \varphi(|f|) \in \widetilde{X}^{\hat{\Phi}}$ and satisfies that $\left\| \hat{\Phi}(|g|) \right\|_X \leq 1$ .

Proof. First of all let us check that the product $fg \in X$ . Since $\Phi \in \Delta_2$ there exist $c > 1$ and $x_0 \geq 0$ such that $x\varphi(x) \leq c\Phi(x)$ for all $x \geq x_0$ (see [12, Theorem 4.1] or [17, Theorem 2.2.3]). Then

$$
\left| f g \right| = \left| f \right| \varphi (\left| f \right|) \leq c \Phi (\left| f \right|) + \left| f (x _ {0}) \right| \Phi (\left| f (x _ {0} \right|) \chi_ {\Omega} \in X
$$

because $\Phi(|f|) \in X$ and $|f(x_0)|\Phi(|f(x_0)|)\chi_{\Omega} \in L^{\infty}(\mu) \subseteq X$ . Thus $fg \in X$ .

Now, from (6) we have $|f|\varphi(|f|) = \Phi(|f|) + \hat{\Phi}(\varphi(|f|))$ , that is,

$$
| f g | = \Phi (| f |) + \hat {\Phi} (| g |). \tag {17}
$$

Then $\hat{\Phi}(|g|) \leq |fg| \in X$ , and so $\hat{\Phi}(|g|) \in X$ , that is, $g \in \widetilde{X}^{\Phi}$ . Suppose on the contrary that the second conclusion of the statement is not satisfied, that is, suppose that $\left\| \hat{\Phi}(|g|) \right\|_{X} > 1$ . Since $f \neq 0$ , from (17) we have

$$
\hat {\Phi} (| g |) <   \Phi (| f |) + \hat {\Phi} (| g |) = | f g |.
$$

Taking into account that the quasi-norm is strictly monotone and the inequality (13) of Lemma 5.1 we conclude that

$$
\left\| \hat {\Phi} (| g |) \right\| _ {X} <   \| f g \| _ {X} \leq \| f \| _ {X _ {O} ^ {\Phi}} \cdot \max \left\{1, \left\| \hat {\Phi} (| g |) \right\| _ {X} \right\} = \| f \| _ {X _ {O} ^ {\Phi}} \cdot \left\| \hat {\Phi} (| g |) \right\| _ {X} \leq \left\| \hat {\Phi} (| g |) \right\| _ {X}.
$$

This contradiction proves the result.

Proposition 5.8. Let $X$ be a quasi-Banach function space over $\mu$ with strictly monotone quasi-norm and let $\Phi$ an $N$ -function with the $\Delta_2$ -property.

1) If $f \in X_L^\Phi$ , with $\| f \|_{X_O^\Phi} \leq 1$ , then $\| \Phi(|f|) \|_X \leq \| f \|_{X_O^\Phi}$ .   
2) If $0 \neq f \in X_L^\Phi$ , then

$$
\left\| \Phi \left(\frac {| f |}{\| f \| _ {X _ {O} ^ {\Phi}}}\right) \right\| _ {X} \leq 1. \tag {18}
$$

Proof. The same proof of Proposition 5.4 works by applying now Proposition 5.7 instead of Proposition 5.3. $\square$

Theorem 5.9. Let $X$ be a quasi-Banach function space over $\mu$ with strictly monotone quasi-norm and let $\Phi$ an $N$ -function with the $\Delta_2$ -property. Then the Orlicz quasi-norm is equivalent to the Luxemburg quasi-norm on $X_L^\Phi$ . In fact,

$$
\left\| f \right\| _ {X _ {L} ^ {\Phi}} \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}} \leq 2 K \left\| f \right\| _ {X _ {L} ^ {\Phi}}, \quad f \in X _ {L} ^ {\Phi}. \tag {19}
$$

Proof. From the definition of the Luxemburg quasi-norm (4) together with the inequality (18) we obtain the following inequality

$$
\left\| f \right\| _ {X _ {L} ^ {\Phi}} \leq \left\| f \right\| _ {X _ {O} ^ {\Phi}}, \quad f \in X _ {L} ^ {\Phi}.
$$

The second inequality has been established in (9) of Proposition 3.3. $\square$

Next we will see that the hypothesis of strict monotonicity for the quasi-norm can be strongly relaxed. Recall that the norm of the spaces $L^1(m)$ and $L_w^1(m)$ will not be in general a strictly monotone norm.

Proposition 5.10. Let $\Phi$ be an $N$ -function and let $X$ an ideal of $L^0(\mu)$ . Consider two equivalent quasi-norms $\| \cdot \|_1$ and $\| \cdot \|_2$ on $X$ , and denote by $X_1 := (X, \| \cdot \|_1)$ and $X_2 := (X, \| \cdot \|_2)$ the corresponding quasi-normed function spaces. Then

1) the Luxemburg quasi-norms $\| \cdot \|_{X_{L}^{\Phi}}$ and $\| \cdot \|_{X_{L}^{\Phi}}$ are also equivalent, and   
2) the Orlicz quasi-norms $\| \cdot \|_{X_{10}^{\Phi}}$ and $\| \cdot \|_{X_{20}^{\Phi}}$ are equivalent too.

Proof. Let $M \geq 1$ be such that $\frac{1}{M} \| \cdot \|_1 \leq \| \cdot \|_2 \leq M \| \cdot \|_1$ . Note that $\widetilde{X}_1^\Phi = \widetilde{X}_2^\Phi = \widetilde{X}^\Phi$ and also that $X_{1L}^\Phi = X_{2L}^\Phi = X_L^\Phi$ .

1) Given $f \in X_L^\Phi$ , let $c > 0$ be such that $\left\| \Phi \left(\frac{|f|}{c}\right) \right\|_{X_2} \leq 1$ . Then, since $\frac{1}{M} \leq 1$ , accordingly to (2), we have

$$
\left\| \Phi \left(\frac {1}{M} \frac {| f |}{c}\right) \right\| _ {X _ {1}} \leq \left\| \frac {1}{M} \Phi \left(\frac {| f |}{c}\right) \right\| _ {X _ {1}} = \frac {1}{M} \left\| \Phi \left(\frac {| f |}{c}\right) \right\| _ {X _ {1}} \leq \left\| \Phi \left(\frac {| f |}{c}\right) \right\| _ {X _ {2}} \leq 1.
$$

By the definition of the Luxemburg quasi-norm (4) it follows that $\| f\|_{X_{1L}^{\Phi}}\leq Mc$ . Using again the definition of the Luxemburg quasi-norm (4) we also get $\| f\|_{X_{1L}^{\Phi}}\leq M\| f\|_{X_{2L}^{\Phi}}$ . To obtain this last inequality we have only used the inequality $\| \cdot \| _1\leq M\| \cdot \| _2$ . Now, by using this other inequality $\| \cdot \| _2\leq M\| \cdot \| _1$ , we also deduce that $\| f\|_{X_{2L}^{\Phi}}\leq M\| f\|_{X_{1L}^{\Phi}}$ . From both inequalities together we conclude that

$$
\frac {1}{M} \left\| f \right\| _ {X _ {1 L} ^ {\Phi}} \leq \left\| f \right\| _ {X _ {2 L} ^ {\Phi}} \leq M \left\| f \right\| _ {X _ {1 L} ^ {\Phi}}, \quad f \in X ^ {\Phi}.
$$

2) Given $f \in X_{O}^{\Phi}$ , let $g \in \widetilde{X_1}^{\hat{\Phi}}$ be such that $\left\| \hat{\Phi}(|g|) \right\|_{X_1} \leq 1$ . Then, since $\frac{1}{M} \leq 1$ , accordingly to (2), we have

$$
\left\| \hat {\Phi} \left(\frac {| g |}{M}\right) \right\| _ {X _ {2}} \leq \left\| \frac {1}{M} \hat {\Phi} (| g |) \right\| _ {X _ {2}} = \frac {1}{M} \left\| \hat {\Phi} (| g |) \right\| _ {X _ {2}} \leq \left\| \hat {\Phi} (| g |) \right\| _ {X _ {1}} \leq 1.
$$

By the definition of the Orlicz quasi-norm (7) and taking into account the above inequality we obtain that

$$
\left\| f g \right\| _ {X _ {1}} \leq M \left\| f g \right\| _ {X _ {2}} = M ^ {2} \left\| f \frac {g}{M} \right\| _ {X _ {2}} \leq M ^ {2} \left\| f \right\| _ {X _ {2 O} ^ {\Phi}}
$$

and taking suprema we deduce that $\| f\|_{X_{1O}^{\Phi}}\leq M^{2}\| f\|_{X_{2O}^{\Phi}}$ . To obtain this last inequality we have only used the inequality $\| \cdot \| _2\leq M\| \cdot \| _1$ . Now, by using this other inequality $\| \cdot \| _1\leq M\| \cdot \| _2$ , we also deduce that $\| f\|_{X_{2O}^{\Phi}}\leq M^{2}\| f\|_{X_{1O}^{\Phi}}$ . From both inequalities together we conclude that

$$
\frac {1}{M ^ {2}} \left\| f \right\| _ {X _ {1 O} ^ {\Phi}} \leq \left\| f \right\| _ {X _ {2 O} ^ {\Phi}} \leq M ^ {2} \left\| f \right\| _ {X _ {1 O} ^ {\Phi}}, \quad f \in X ^ {\Phi}.
$$

Motivated by Theorem 5.5 and the above Proposition 5.10 we introduce the following definition.

Definition 5.11. We say that a quasi-normed function space $X$ , with quasi-norm $\| \cdot \| _X$ , has a strictly monotone $q$ -renorming if there exist another strictly monotone quasi-norm $\| \cdot \| _X$ which makes $X$ a quasi-normed function space and two positive constants $C_1$ and $C_2$ such that $C_1\| f\| _X\leq \| f\| _X\leq C_2\| f\| _X$ , for all $f\in X$ .

Theorem 5.12. Let $X$ be a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property which has a strictly monotone $q$ -renorming, and let $\Phi$ an $N$ -function. Then $X_{L}^{\Phi} = X_{O}^{\Phi}$ and the Orlicz quasi-norm is equivalent to the Luxemburg quasi-norm.

Theorem 5.13. Let $X$ be a quasi-Banach function space over $\mu$ which has a strictly monotone $q$ -renorming, and let $\Phi$ an $N$ -function with the $\Delta_2$ -property. Then the Orlicz quasi-norm and the Luxemburg quasi-norm are equivalent on the smallest space $X_L^\Phi$ .

Proof. Apply now Theorem 5.9 and Proposition 5.10 again. $\square$

# 6. Quasi-Banach functions spaces with a strictly monotone renorming

In this section we will show sufficient conditions for a quasi-Banach function space to have a strictly monotone q-renorming. We will also present concrete examples of Banach and quasi-Banach spaces that possess such a q-renorming. Let's start with the last one.

Example 6.1. Let $m:\Sigma \to Y$ a vector measure with values on a Banach space $Y$ and let $\mu \coloneqq |\langle m,y^{*}\rangle |$ a Rybakov control measure for $m$ . We can consider a new norm on $L_w^1 (m)$ defined by

$$
\| | f \| | _ {L _ {w} ^ {1} (m)} := \| f \| _ {L _ {w} ^ {1} (m)} + \| f \| _ {L ^ {1} (\mu)}, \quad f \in L _ {w} ^ {1} (m).
$$

Note that $\| f\|_{L_w^1 (m)}\leq \| |f||_{L_w^1 (m)}\leq 2\| f\|_{L_w^1 (m)}$ for all $f\in L_w^1 (m)$ and, moreover, $\| \cdot \|_{L_w^1 (m)}$ is a strictly monotone norm (because $\| \cdot \|_{L^1 (\mu)}$ is) on $L_w^1 (m)$ . Recall that $L_w^1 (m)$ has the $\sigma$ -Fatou property. Thus we have the equality $L_w^1 (m)_L^\Phi = L_w^1 (m)_O^\Phi$ , and consequently the second equality of (11).

Example 6.2. Let $m: \Sigma \to Y$ a vector measure with values into a Banach space $Y$ . In general the quasi-norm of $L^1(\|m\|)$ is not strictly monotone. Nevertheless, it can be proved that the following conditions are equivalent:

1) The quasi-norm $\| \cdot \|_{L^1 (\| m\|)}$ is strictly monotone.   
2) If $A \subseteq B \in \Sigma$ and $\|m\| (B \setminus A) \neq 0$ , then $\|m\| (A) < \|m\| (B)$ .

In any case, following the same way of the above example, we can consider a new quasi-norm on $L^1(\|m\|)$ defined by

$$
\| \| f \| _ {L ^ {1} (\| m \|)} := \| f \| _ {L ^ {1} (\| m \|)} + \| f \| _ {L ^ {1} (\mu)}, \quad f \in L ^ {1} (\| m \|)
$$

which turns out to be equivalent to the quasi-norm $\| \cdot \|_{L^1 (\| m\|)}$ and, moreover, $\| \cdot \|_{L^1 (\| m\|)}$ is a strictly monotone quasi-norm. Then we have the equality $L^{1}(\| m\|)_{L}^{\Phi} = L^{1}(\| m\|)_{O}^{\Phi}$ and the quasi-norms $\| \cdot \|_{L^1 (\| m\|)_L^\Phi}$ and $\| \cdot \|_{L^1 (\| m\|)_O^\Phi}$ are equivalent for every vector measure $m$ .

Necessary conditions and sufficient conditions that for a given Riesz $(=)$ lattice) norm there is an equivalent strictly monotone Riesz norm are investigated in [15]. We translate the general result [15, Theorem 1] into our context as follows. If a quasi-Banach function space $X$ over the measure $\mu$ with quasi-norm $\| \cdot \| _X$ possesses a bounded strictly positive linear functional (hence continuous) $T:f\in X\longrightarrow T(f)\in \mathbb{R}$ , then

$$
\| | f \| | _ {X} := \| f \| _ {X} + T (| f |), \quad f \in X
$$

defines a strictly monotone quasi-norm $\| \cdot \| _X$ on $X$ that is equivalent to $\| \cdot \| _X$ . This is exactly the case of the previous Example 6.1 and Example 6.2, where $T(f)\coloneqq \int_{\Omega}fd\mu$ define a strictly positive linear functional on $L_{w}^{1}(m)$ and therefore also in $L^1 (\| m\|)$ .

On the other hand if $X$ is a countably generated Banach function space with a strictly monotone norm, then it must possess a bounded strictly positive linear functional. The proof of this last statement depends strongly on the Hahn-Banach theorem. Unfortunately this essential tool is not available in the quasi-Banach context. Moreover, this is not the case in the setting of quasi-Banach function spaces as the spaces $L^p(\mu)$ , with $0 < p < 1$ , point out. All these spaces have a strictly monotone quasi-norm (as they have all $L^p$ -spaces with $p < \infty$ ) but, as it is well known, they have no non-zero bounded linear functionals.

Although we do not know to what extent it is possible to find a strictly monotone equivalent quasi-norm for a quasi-Banach function space, we can show some sufficient conditions that allow to prove that such an equivalent quasi-norm exists in a broad class of quasi-Banach function spaces (including all Banach function spaces). According to this, in the rest of the section we present several sufficient conditions for a quasi-Banach function space to have an equivalent strictly monotone quasi-norm.

Given $0 < r < \infty$ and a quasi-Banach function space $X$ over $\mu$ , consider its $r$ -th power

$$
X _ {[ r ]} := \left\{h \in L ^ {0} (\mu): | h | ^ {\frac {1}{r}} \in X \right\}
$$

with the quasi-norm

$$
\left\| h \right\| _ {X _ {[ r ]}} := \left\| \left| h \right| ^ {\frac {1}{r}} \right\| _ {X} ^ {r}, \quad h \in X _ {[ r ]}.
$$

For details on $r$ -th powers of quasi-Banach function spaces see [16, Section 2.2]. In particular note that $X_{[r]}$ is again a quasi-Banach function space over $\mu$ , and what is most important to us (see [16, Proposition 2.23]): If $X$ is $r$ -convex, then $X_{[r]}$ admits a lattice norm, namely,

$$
\| \| h \| _ {X _ {[ r ]}} := \inf  \left\{\sum_ {k = 1} ^ {n} \| h _ {k} \| _ {X _ {[ r ]}}: | h | \leq \sum_ {k = 1} ^ {n} | h _ {k} |, h _ {k} \in X _ {[ r ]}, k = 1, \dots , n, n \geq 1 \right\}
$$

which is equivalent to $\| \cdot \|_{X_{[r]}}$ . Accordingly, if $X$ is $r$ -convex, then $X_{[r]}$ is a Banach function space over $\mu$ . We recall that $X$ is called $r$ -convex if there exists $C \geq 1$ such that

$$
\left\| \left(\sum_ {k = 1} ^ {n} | f _ {k} | ^ {r}\right) ^ {\frac {1}{r}} \right\| _ {X} \leq C \left(\sum_ {k = 1} ^ {n} \| f _ {k} \| _ {X} ^ {r}\right) ^ {\frac {1}{r}}, \quad f _ {1}, \dots , f _ {n} \in X.
$$

Moreover, as we always assume that the characteristic function $\chi_{\Omega} \in X$ , the Banach function space $X_{[r]}$ is saturated in the sense of [20]. Recall that a quasi-Banach function space $X$ is saturated if and only if there is a positive measurable function $f$ , that is, $f \geq 0$ and $\mu([f = 0]) = 0$ , that belongs to $X$ . Clearly, if $X$ is saturated then $X_{[r]}$ is too far from $r > 0$ .

Proposition 6.3. Let $X$ be a quasi-Banach function space over $\mu$ which is $r$ -convex for some $0 < r < \infty$ . Then $X$ possesses a strictly monotone $q$ -renorming.

Proof. Consider the saturated Banach function space $X_{[r]}$ with the lattice norm $\| \cdot \|_{X_{[r]}}$ , and denote by $E\coloneqq X_{[r]}$ and $F\coloneqq L^{\infty}(\mu)$ . Since, as we have explained before, the product $E\cdot F = X_{[r]}\cdot L^{\infty}(\mu) = X_{[r]}$ is normable, we can apply the implication (i) $\Rightarrow$ (ii) of [20, Proposition 1.1] to get a function $0\leq g\in L^{0}(\mu)$ with $\mu ([g = 0]) = 0$ , such that $g\cdot L^{\infty}(\mu)\subseteq X_{[r]}^{\prime}$ . Definitely we found a positive function $g\in X_{[r]}^{\prime}$ , the Kőthe dual of $X_{[r]}$ , which means that $\left|\int \limits_{\Omega}hgd\mu \right|\leq \int \limits_{\Omega}|h|g d\mu \leq \| h\|_{X_{[r]}}\| g\|_{X_{[r]}^{\prime}}\leq \| h\|_{X_{[r]}}\| g\|_{X_{[r]}^{\prime}}$ , for all $h\in X_{[r]}$ .

Then it is not difficult to see that $\left[\int_{\Omega}|f|^r gd\mu \right]^{\frac{1}{r}}\leq \| f\| _X\| g\|_{X_{[r]}^{\prime}}^{\frac{1}{r}}$ , for all $f\in X$ , and consequently, the formula

$$
\| f \| _ {X} := \| f \| _ {X} + \left[ \int_ {\Omega} | f | ^ {r} g d \mu \right] ^ {\frac {1}{r}}, \qquad f \in X
$$

defines a strictly monotone quasi-norm on $X$ that is equivalent to $\| \cdot \| _X$ .

Remark 6.4. If $X$ is a Banach function space over $\mu$ then it is certainly 1-convex. Trivially $X_{[1]} = X$ and $\| \cdot \|_{X_{[1]}} = \| \cdot \|_X$ on $X$ . This means that every Banach function space satisfies the conclusion of Proposition 6.3. Thus every Banach function space possesses a strictly monotone renorming.

Quasi-Banach function spaces not satisfying the $r$ -convexity condition for any $r > 0$ are not the most naturally arising quasi-Banach function spaces; in fact, to find examples of such spaces is rather difficult even in the setting of quasi-Banach lattices. However, this class has been studied, because of their importance from the theoretical point of view. In [11], Kalton described the class of quasi-Banach lattices that are $r$ -convex for some $r > 0$ , and provided an example ([11, Example 2.4]) of a quasi-Banach lattice not satisfying this property. It is worth noting that this example falls outside the context of quasi-Banach functions spaces in which we are working on. It is shown in this paper ([11, Theorem 2.2]) that being $r$ -convex for some $r > 0$ is equivalent to being L-convex. It is said that quasi-Banach lattice $X$ is L-convex if there exists $0 < \varepsilon < 1$ so that if $0 \leq g \in X$ with $\|g\|_X = 1$ and $0 \leq f_k \leq g$ ( $1 \leq k \leq n$ ) satisfy $\frac{1}{n} (f_1 + \dots + f_n) > (1 - \varepsilon)g$ , then $\max_{1 \leq k \leq n} \|f_k\|_X > \varepsilon$ .

Thus, because of the quoted counterexample, our feeling is that we cannot use the argument we have shown in Proposition 6.3 for the whole class of quasi-Banach function spaces without any assumption of convexity.

On the other hand, it is possible to find easy examples of spaces that cannot be renormed with an strictly monotone norm (see [15, Example 4]). However, it remains open the question about if there is a non-L-convex quasi-Banach function space over a finite measure which cannot be renormed with a strictly monotone quasi-norm. As far as we know, the answer is not known, or at least we have not been able to find it in the literature. This justifies the following result, which shows that $r$ -convexity can be substituted by $(r,1)$ -concavity as a sufficient condition for having an equivalent strictly monotone norm.

Let $r > 0$ . A quasi-Banach function space $X$ is called $(r,1)$ -concave if there exists $C \geq 1$ such that $\left(\sum_{k=1}^{n} \|f_k\|_X^r\right)^{\frac{1}{r}} \leq C \left\| \sum_{k=1}^{n} |f_k| \right\|_X$ , for all $f_1, \ldots, f_n \in X$ . The $(r,1)$ -concavity constant is the infimum of all such constants $C$ . Note that $r$ -concave function spaces (see [16, Definition 2.46]) are $(r,1)$ -concave for $r \geq 1$ .

Proposition 6.5. Let $X$ be a $(r,1)$ -concave quasi-Banach function space over $\mu$ . Then $X$ possesses a strictly monotone $q$ -renorming.

Proof. Suppose that the quasi-norm $\| \cdot \| _X$ has quasi-triangle constant $K$ . If $X$ is $(r,1)$ -concave, the following formula gives an equivalent quasi-norm with quasi-triangle constant $CK$ , where $C$ is the $(r,1)$ -concavity constant for $X$ . Indeed, if $f\in X$ ,

$$
\| f \| _ {X} := \sup  \left\{\left(\sum_ {k = 1} ^ {n} \| f _ {k} \| _ {X} ^ {r}\right) ^ {\frac {1}{r}}: \sum_ {k = 1} ^ {n} | f _ {k} | = | f |, f _ {1}, \dots , f _ {n} \in X \right\},
$$

clearly satisfies that

$$
\| f \| _ {X} \leq \| | f | \| _ {X} = \sup  \left(\sum_ {k = 1} ^ {n} \| f _ {k} \| _ {X} ^ {r}\right) ^ {\frac {1}{r}} \leq C \sup  \left\| \sum_ {k = 1} ^ {n} | f _ {k} | \right\| _ {X} = C \| f \| _ {X},
$$

where the supremum is computed for all representations $\sum_{k=1}^{n} |f_k| = |f|$ , with $f_1, \ldots, f_n \in X$ , and so $\| \cdot \|_X$ and $\| \cdot \|_X$ are equivalent on $X$ .

Note also that, if $f, g \in X$ , using the inequality above we have that

$$
\| | f + g \| | _ {X} \leq C \| f + g \| _ {X} \leq C K \left(\| f \| _ {X} + \| g \| _ {X}\right) \leq C K \left(\| | f \| | _ {X} + \| | g \| | _ {X}\right).
$$

Let us now check that $\| \cdot \| _X$ is strictly monotone. Indeed, if there are two functions $0\leq f < g\in X$ we have that there is a non-negative non-zero function $h = g - f\in X$ , that is, $\| h\| _X^r >\varepsilon >0$ for some $\varepsilon$ . Take a decomposition of $|f|$ as $|f| = \sum_{k = 1}^{n}|f_k|$ such that $\| |f||_X^r < \sum_{k = 1}^n\| f_k\| _X^r +\varepsilon$ . Then, taking into account that $|g| = g = f + h = |f| + |g - f| = \sum_{k = 1}^{n}|f_k| + |g - f|$ , we get

$$
\| | f \| | _ {X} ^ {r} <   \sum_ {k = 1} ^ {n} \| f _ {k} \| _ {X} ^ {r} + \varepsilon <   \sum_ {k = 1} ^ {n} \| f _ {k} \| _ {X} ^ {r} + \| h \| _ {X} ^ {r} \leq \| | g \| | _ {X} ^ {r}.
$$

Then we obtain that $\| f\| _X <   \| g\| _X$

To have equivalence between the Orlicz and Luxemburg quasi-norms the hypothesis that the quasi-Banach function space $X$ has a strictly monotone q-renorming seems to be necessary. As we have pointed out with the different types of results of this section, this hypothesis is certainly very general. In fact, to be honest, we have not been able to build a quasi-Banach function space without this property. Certainly there exist Banach lattices (see [15, Example 4]) without a strictly monotone renorming but these examples fall outside the context in which we are working on.

We conclude this section by gathering the three positive results where we can ensure that the spaces $X_{O}^{\Phi}$ and $X_{L}^{\Phi}$ coincide and/or the corresponding Orlicz and Luxemburg quasi-norms are equivalent. They follow from Theorem 5.12 and Theorem 5.13 respectively.

Corollary 6.6. Let $X$ be a quasi-Banach function space over $\mu$ with the $\sigma$ -Fatou property and let $\Phi$ an $N$ -function. If at least one of the following two conditions:

a) $X$ is $r$ -convex for some $0 < r < \infty$ , or   
b) $X(r,1)$ -concave for some $0 < r < \infty$

is satisfied, then $X_O^\Phi = X_L^\Phi$ and the corresponding Orlicz and Luxemburg quasi-norms are equivalent.

Corollary 6.7. Let $X$ be a quasi-Banach function space over $\mu$ and let $\Phi$ an $N$ -function with the $\Delta_2$ -property. If at least one of the following two conditions:

a) $X$ is $r$ -convex for some $0 < r < \infty$ , or   
b) $X(r,1)$ -concave for some $0 < r < \infty$

is satisfied, then the Orlicz quasi-norm and the Luxemburg quasi-norm are equivalent on the smallest space $X_L^\Phi$ .

Remark 6.8. A special case of item a) in the above Corollaries 6.6 and 6.7 appears if the space $X$ is a Banach function space over $\mu$ . In that case:

i) If $X$ has the $\sigma$ -Fatou property and $\Phi$ is an N-function, then $X_{O}^{\Phi} = X_{L}^{\Phi}$ and the corresponding Orlicz and Luxemburg quasi-norms are equivalent.   
ii) If $\Phi$ is an N-function with the $\Delta_2$ -property, then the Orlicz quasi-norm and the Luxemburg quasi-norm are equivalent on the smallest space $X_L^\Phi$ .

# References

[1] R. del Campo, A. Fernández, I. Ferrando, F. Mayoral, F. Naranjo, Multiplication operators on spaces on integrable functions with respect to a vector measure, J. Math. Anal. Appl. 343 (1) (2008) 514-524, https://doi.org/10.1016/j.jmaa.2008.01.080, MR2412146.   
[2] R. del Campo, A. Fernández, F. Mayoral, F. Naranjo, Reflexivity of function spaces associated to a $\sigma$ -finite vector measure, J. Math. Anal. Appl. 438 (1) (2016) 339-350, https://doi.org/10.1016/j.jmaa.2016.01.076, MR3462581.   
[3] R. del Campo, A. Fernández, F. Mayoral, F. Naranjo, The de la Vallée-Poussin theorem and Orlicz spaces associated to a vector measure, J. Math. Anal. Appl. 470 (1) (2019) 279-291, https://doi.org/10.1016/j.jmaa.2018.10.001, MR3865136.   
[4] R. del Campo, A. Fernández, F. Mayoral, F. Naranjo, Orlicz spaces associated to a quasi-Banach function space. Applications to vector measures and interpolation, preprint arXiv:1910.13183 [math.FA], 2019. To appear in Collect. Math. (2020), https://doi.org/10.1007/s13348-020-00295-1.   
[5] R. del Campo, A. Fernández, F. Mayoral, F. Naranjo, Compactness in quasi-Banach function spaces with applications to $L^1$ of the semivariation of a vector measure, Rev. R. Acad. Cienc. Exactas Fís. Nat., Ser. A Mat. 114 (112) (2020), https://doi.org/10.1007/s13398-020-00840-4.   
[6] O. Delgado, Banach function subspaces of $L^1$ of a vector measure and related Orlicz spaces, Indag. Math. (N.S.) 15 (4) (2004) 485-495, https://doi.org/10.1016/S0019-3577(05)00004-2, MR2114932.   
[7] J. Diestel, J.J. Uhl Jr., Vector Measures, Mathematical Surveys, vol. 15, American Mathematical Society, Providence R.I., 1977, MR0453964.   
[8] A. Fernández, F. Mayoral, F. Naranjo, Bartle-Dunford-Schwartz integral versus Bochner, Pettis and Dunford integrals, J. Convex Anal. 20 (2) (2013) 339-353, MR3098470.   
[9] I. Ferrando, F. Galaz-Fontes, Multiplication operators on vector measure Orlicz spaces, Indag. Math. (N.S.) 20 (1) (2009) 57–71, https://doi.org/10.1016/S0019-3577(09)80003-7, MR2566152.   
[10] P. Jain, L.E. Persson, P. Upreti, Inequalities and properties of some generalized Orlicz classes and spaces, Acta Math. Hung. 117 (1-2) (2007) 161-174, https://doi.org/10.1007/s10474-007-6083-9, MR2356192.   
[11] N.J. Kalton, Convexity conditions for nonlocally convex lattices, Glasg. Math. J. 25 (2) (1984) 141-152, https://doi.org/10.1017/S0017089500005553, MR752808.   
[12] M.A. Krasnosel'skii, Ja.B. Ruticki, Convex Functions and Orlicz Spaces, translated from the first Russian edition by Leo F. Boron, P. Noordhoff Ltd., Groningen, 1961, MR0126722.   
[13] D.R. Lewis, On integrability and summability in vector spaces, Ill. J. Math. 16 (1972) 294-307, MR0291409.   
[14] L. Maligranda, Orlicz Spaces and Interpolation, Seminários de Matemática (Seminars in Mathematics), vol. 5, Universidade Estadual de Campinas, Departamento de Matemática, Campinas, 1989, MR2264389.   
[15] L.C. Moore Jr., Strictly increasing Riesz norms, Pac. J. Math. 37 (1971) 171-180, MR306866.   
[16] S. Okada, W.J. Ricker, E.A. Sánchez Pérez, Optimal Domain and Integral Extension of Operators Acting in Function Spaces, Operator Theory: Advances and Applications, vol. 180, Birkhäuser Verlag, Basel, 2008, MR2418751.   
[17] M.M. Rao, Z.D. Ren, Theory of Orlicz Spaces, Monographs and Textbooks in Pure and Applied Mathematics, vol. 146, Marcel Dekker, Inc., New York, 1991, MR1113700.   
[18] S.K. Roy, N.D. Chakraborty, Orlicz spaces for a family of measures, Anal. Math. 12 (3) (1986) 229–235, https://doi.org/10.1007/BF01907709 (in English, with Russian summary), MR856304.   
[19] B.A. Rubshtein, G.Ya. Grabarnik, M.A. Muratov, Y.S. Pashkova, Foundations of Symmetric Spaces of Measurable Functions, Developments in Mathematics, vol. 45, Springer, Cham, 2016, MR3525091.   
[20] A.R. Schep, Products and factors of Banach function spaces, Positivity 14 (2) (2010) 301-319, https://doi.org/10.1007/s11117-009-0019-2, MR2657636.