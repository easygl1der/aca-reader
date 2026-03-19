# On Reproducing Kernel Banach Spaces: Generic Definitions and Unified Framework of Constructions

Rongrong Lin*, Haizhang Zhang† and Jun Zhang‡

# Abstract

Recently, there has been emerging interest in constructing reproducing kernel Banach spaces (RKBS) for applied and theoretical purposes such as machine learning, sampling reconstruction, sparse approximation and functional analysis. Existing constructions include the reflexive RKBS via a bilinear form, the semi-inner-product RKBS, the RKBS with $\ell^1$ norm, the $p$ -norm RKBS via generalized Mercer kernels, etc. The definitions of RKBS and the associated reproducing kernel in those references are dependent on the construction. Moreover, relations among those constructions are unclear. We explore a generic definition of RKBS and the reproducing kernel for RKBS that is independent of construction. Furthermore, we propose a framework of constructing RKBSs that leads to new RKBSs based on Orlicz spaces and unifies existing constructions mentioned above via a continuous bilinear form and a pair of feature maps. Finally, we develop representer theorems for machine learning in RKBSs constructed in our framework, which also unifies representer theorems in existing RKBSs.

Keywords: Reproducing kernel Banach spaces, feature maps, reproducing kernels, machine learning, the representer theorem

# 1 Introduction

In this paper, we aim at the construction of reproducing kernel Banach spaces (RKBSs), which serve as a generalization of reproducing kernel Hilbert spaces (RKHSs) [33]. The notion of RKBS was originally introduced in machine learning in 2009 [46]. Since then, various RKBSs [13, 16, 37, 38, 43, 45, 46, 48] have been constructed for different applied and theoretical purposes. They are used in a wide variety of fields such as machine learning [43, 45, 46, 48, 49], sampling reconstruction [14, 15, 18, 27, 28], sparse approximation [37, 38, 43, 45], and functional analysis [9, 35, 47]. The definitions of existing RKBSs and the associated reproducing kernels in the literature are dependent on the construction. To address this issue and to further promote research in the subject, it is helpful to understand the essence of RKBS and to propose a framework of constructing RKBSs that unifies existing constructions.

RKHSs are Hilbert spaces of functions on which point evaluation functionals are continuous [33]. In machine learning, RKHSs have been viewed as ideal spaces for kernel-based learning algorithms. Thanks to the existence of an inner product, Hilbert spaces are well-understood in functional analysis. Many applications require that the sampling process to be stable. In other words, the point evaluations should be bounded. Most importantly, an RKHS has a reproducing kernel, which measures similarity between input data and gives birth to the "kernel trick" in machine learning that significantly saves computations. Successful and important machine learning methods based on RKHSs include support vector machines and the regularization networks [33, 36].

There are many reasons that justify the need of RKBSs. We mention three here. First of all, Banach spaces possess richer geometrical structures and norms. It is well-known that any two Hilbert spaces over $\mathbb{C}$ of the same dimension are isometrically isomorphic. By contrast, for $1 \leq p \neq q \leq +\infty$ , $L^p([0,1])$ and $L^q([0,1])$ are not isomorphic to each other (see, [12], page 180). Secondly, kernel functions play the role of measuring similarity of inputs in machine learning. They are defined by inner product through a feature map and therefore are inherently symmetric. In some applications such as psychology [51], asymmetric kernels are desired, which can only be obtained via Banach spaces. Thirdly, machine learning schemes in Banach spaces have received considerable attention recently [1, 10, 25, 26, 37, 38, 43, 45, 46, 48, 49]. Many important problems such as $p$ -norm coefficient-based regularization [34, 38, 40, 42], large-margin classification [10, 45, 46], lasso in statistics [39] and compressed sensing [4] had better be studied in Banach spaces. It suggests the need of extending Hilbert space type arguments to Banach spaces.

Under these considerations, different definitions and constructions of RKBSs have been proposed in the literature. In 2009, Zhang et al. [46] proposed the new concept of RKBS for machine learning. Reflexive RKBSs were constructed by the bilinear form between a reflexive Banach space and its dual. The semi-inner-product RKBS was also studied in [46] and [47, 48] based on the tool of semi-inner products [17, 22]. For the multi-task learning, Zhang et al. [49] developed the notion of semi-inner-product vector-valued RKBS. In 2013, Song et al. [38] constructed a class of RKBSs with the $\ell^1$ norm via admissible kernels targeting at sparse learning. In those spaces, the representer theorem for regularized learning schemes is satisfied. In 2014, Georgiev et al. [16] constructed a class of RKBSs with the $p$ -norm $(1 \leq p \leq +\infty)$ without the representer theorem. In 2015, Fasshauer et al. [13] constructed a class of RKBSs with positive definite functions. More recently, the $p$ -norm $(1 \leq p \leq +\infty)$ RKBSs were systematically developed by Xu and Ye in [43] via generalized Mercer kernels.

The definitions of RKBSs and the associated reproducing kernels in the above references are dependent on the construction. Moreover, the relation among those constructions is unclear. Limitations also persist. For instance, the Banach space $C([0,1])$ of all continuous functions on the interval [0,1] does not satisfy those definitions. However, $C([0,1])$ should be an RKBS as point evaluations are clearly continuous in the space. We hope to propose a framework of constructing RKBSs that unifies existing constructions, and leads further to new constructions that accept $C([0,1])$ as a particular example. The main purpose of this paper is two-fold:

(i) to give a generic definition of RKBS that naturally generalizes the classical RKHS and is independent of construction;   
(ii) to propose a unified framework of constructing RKBSs that covers all existing constructions in the literature and also leads to new RKBSs.

The outline of the paper is as follows. In Section 2, we first give a generic definition of RKBSs, and then propose a novel framework of constructing RKBSs via a pair of feature maps. Furthermore, we are able to construct a new class of Orlicz RKBSs. In Section 3, we justify that our framework does unify existing RKBSs in the literature. In particular, $C([0,1])$ is included. In the last section, we develop a representative theorem for regularization networks in RKBSs constructed in our framework.

# 2 Generic definitions and constructions

In this section, we first present a generic definition of RKBS and the reproducing kernel for RKBS. Then, we propose a novel framework of constructing RKBSs via a pair of feature maps. Finally, we construct new RKBSs based on Orlicz spaces.

# 2.1 Generic definitions of RKBSs

We describe our generic definition of RKBSs as follows.

Definition 2.1 (Reproducing Kernel Banach Spaces (RKBS)) A reproducing kernel Banach space $\mathcal{B}$ on a prescribed nonempty set $X$ is a Banach space of certain functions on $X$ such that every point evaluation functional $\delta_x$ , $x \in X$ on $\mathcal{B}$ is continuous, that is, there exists a positive constant $C_x$ such that

$$
\left| \delta_ {x} (f) \right| = \left| f (x) \right| \leq C _ {x} \| f \| _ {\mathcal {B}} f o r a l l f \in \mathcal {B}.
$$

Note that a normed vector space $V$ on $X$ is called a Banach space of functions if it is a Banach space whose elements are functions on $X$ and for each $f \in V$ , $\| f \|_V = 0$ if and only if $f$ , as a function, vanishes everywhere on $X$ . By definition, $L^p([0,1])$ , $1 \leq p \leq +\infty$ , is not a Banach space of functions as it consists of equivalent classes of functions with respect to the Lebesgue measure.

Definition 2.1 naturally generalizes the classical definition of RKHS. We should point out that such a definition was implicitly mentioned in some papers on sampling theorems [5, 14, 18], although no reproducing kernels were defined or even mentioned therein. We also point out that the authors in [46] had also intended to use this definition for RKBSs, but eventually gave it up due to the example $C([0,1])$ . A semi-inner-product structure was imposed in [46] to ensure the existence of a reproducing kernel.

By Definition 2.1, $C([0,1])$ is an RKBS. We shall see what its reproducing kernels look like in Subsection 3.5. The only requirement on RKBSs in our definition is continuity of point evaluations. Definitions of RKBSs in existing literature [38, 43, 46, 47] all impose other requirements to ensure the existence of a reproducing kernel that is not a generalized function. Those requirements more or less seem unnatural. We are able to remove them by exploiting the definition of reproducing kernels via continuous bilinear forms.

A bilinear form between two normed vector spaces $V_{1}, V_{2}$ is a function $\langle \cdot, \cdot \rangle_{V_1 \times V_2}$ from $V_{1} \times V_{2}$ to $\mathbb{C}$ that is linear about both arguments. It is said to be continuous if there exists a positive constant $C$ such that

$$
| \langle f, g \rangle_ {V _ {1} \times V _ {2}} | \leq C \| f \| _ {V _ {1}} \| g \| _ {V _ {2}} \text {f o r a l l} f \in V _ {1}, g \in V _ {2}.
$$

Definition 2.2 (Reproducing Kernels for RKBS) Let $\mathcal{B}_1$ be an RKBS on a set $\Omega_1$ . If there exists a Banach space $\mathcal{B}_2$ of functions on another set $\Omega_2$ , a continuous bilinear form $\langle \cdot, \cdot \rangle_{\mathcal{B}_1 \times \mathcal{B}_2}$ and a function $K$ on $\Omega_1 \times \Omega_2$ such that $K(x, \cdot) \in \mathcal{B}_2$ for all $x \in \Omega_1$ and

$$
f (x) = \langle f, K (x, \cdot) \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} \text {f o r a l l} x \in \Omega_ {1} \text {a n d a l l} f \in \mathcal {B} _ {1}, \tag {2.1}
$$

then we call $K$ a reproducing kernel for $\mathcal{B}_1$ . If, in addition, $\mathcal{B}_2$ is also an RKBS on $\Omega_2$ and it holds $K(\cdot, y) \in \mathcal{B}_1$ for all $y \in \Omega_2$ and

$$
g (y) = \left\langle K (\cdot , y), g \right\rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} f o r a l l y \in \Omega_ {2} a n d a l l g \in \mathcal {B} _ {2}, \tag {2.2}
$$

then we call $\mathcal{B}_2$ an adjoint RKBS of $\mathcal{B}_1$ and call $\mathcal{B}_1$ and $\mathcal{B}_2$ a pair of RKBSs. In this case, $\widetilde{K}(x,y) := K(y,x)$ , $x \in \Omega_2$ , $y \in \Omega_1$ , is a reproducing kernel for $\mathcal{B}_2$ .

We call (2.1) and (2.2) the reproducing properties for the kernel $K$ in RKBSs $\mathcal{B}_1$ and $\mathcal{B}_2$ , respectively.

Although there are many conditions in the definition, we shall see that RKBSs and reproducing kernels satisfying the conditions can be easily constructed via a pair of feature maps.

# 2.2 Constructions via a pair of feature maps

We shall propose a unified framework of constructing RKBSs via a pair of feature maps. We shall discuss in the next section that all existing constructions of RKBSs fall into the framework.

Let $\langle \cdot, \cdot \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ be a continuous bilinear form $\langle \cdot, \cdot \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ on Banach spaces $\mathcal{W}_1$ and $\mathcal{W}_2$ . We call the linear span span $A$ of a set $A \subseteq \mathcal{W}_1$ dense in $\mathcal{W}_1$ with respect to the bilinear form $\langle \cdot, \cdot \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ if for any $v \in \mathcal{W}_2$ ,

$$
\langle a, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = 0 \text {f o r a \in A}
$$

implies $v = 0$ . Similarly, we can define denseness in $\mathcal{W}_2$ with respect to the bilinear form.

Our construction is described below.

# Constructions of RKBSs

Let $\mathcal{W}_1, \mathcal{W}_2$ be two Banach spaces, and $\langle \cdot, \cdot \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ be a continuous bilinear form on $\mathcal{W}_1 \times \mathcal{W}_2$ . Suppose there exist two nonempty sets $\Omega_1$ and $\Omega_2$ , and mappings

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}
$$

such that with respect to the bilinear form

$$
\operatorname {s p a n} \Phi_ {1} \left(\Omega_ {1}\right) \text {i s d e n s e i n} \mathcal {W} _ {1}, \operatorname {s p a n} \Phi_ {2} \left(\Omega_ {2}\right) \text {i s d e n s e i n} \mathcal {W} _ {2}. \tag {2.3}
$$

We construct

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}: v \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\} \tag {2.4}
$$

with norm

$$
\| f _ {v} \| _ {\mathcal {B} _ {1}} := \| v \| _ {\mathcal {W} _ {2}}
$$

and

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}: u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\} \tag {2.5}
$$

with norm

$$
\left\| g _ {u} \right\| _ {\mathcal {B} _ {2}} := \left\| u \right\| _ {\mathcal {W} _ {1}}.
$$

The construction can be simplified when $\mathcal{W}_2$ is a closed subspace of $\mathcal{W}_1^*$ , the dual space of continuous linear functionals on $\mathcal{W}_1$ . In this case, we always use the natural continuous bilinear form

$$
\langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \langle u, v \rangle_ {\mathcal {W} _ {1}} := v (u), \quad u \in \mathcal {W} _ {1}, v \in \mathcal {W} _ {2}.
$$

The denseness condition (2.3) is satisfied if

$$
\mathcal {W} _ {1} = \overline {{\operatorname {s p a n}}} \Phi_ {1} (\Omega_ {1}), \mathcal {W} _ {1} ^ {*} = \overline {{\operatorname {s p a n}}} \Phi_ {2} (\Omega_ {2}) \tag {2.6}
$$

or

$$
\mathcal {W} _ {1} = \overline {{\operatorname {s p a n}}} \Phi_ {1} (\Omega_ {1}), \text {a n d} \operatorname {s p a n} \Phi_ {2} (\Omega_ {2}) \text {i s} \tag {2.7}
$$

We show that such constructed spaces $\mathcal{B}_1$ and $\mathcal{B}_2$ indeed form a pair of RKBSs, and present the associated reproducing kernel.

Theorem 2.3 Let $\mathcal{B}_1$ and $\mathcal{B}_2$ be constructed as in (2.4) and (2.5), respectively. Then with the bilinear form on $\mathcal{B}_1 \times \mathcal{B}_2$

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} \text {f o r a l l} f _ {v} \in \mathcal {B} _ {1} \text {a n d a l l} g _ {u} \in \mathcal {B} _ {2}, \tag {2.8}
$$

$\mathcal{B}_1$ is an RKBS on $\Omega_1$ with the adjoint RKBS $\mathcal{B}_2$ on $\Omega_2$ . Moreover,

$$
K (x, y) := \left\langle \Phi_ {1} (x), \Phi_ {2} (y) \right\rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}, x \in \Omega_ {1}, y \in \Omega_ {2}, \tag {2.9}
$$

is a reproducing kernel for $\mathcal{B}_1$ .

Proof: First note that the denseness condition (2.3) guarantees that the $v, u$ in $f_v$ and $g_u$ are both unique. The definition is hence well-defined. We next prove that $\mathcal{B}_1$ and $\mathcal{B}_2$ are RKBSs. By assumption, there exists a positive constant $C$ such that

$$
\left| \langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} \right| \leq C \| u \| _ {\mathcal {W} _ {1}} \| v \| _ {\mathcal {W} _ {2}} \text {f o r a l l} u \in \mathcal {W} _ {1} \text {a n d a l l} v \in \mathcal {W} _ {2}. \tag {2.10}
$$

By (2.4) and (2.10), we have for all $f_v \in \mathcal{B}_1$ and all $x \in \Omega_1$

$$
| f _ {v} (x) | = | \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} | \leq C \| \Phi_ {1} (x) \| _ {\mathcal {W} _ {1}} \| v \| _ {\mathcal {W} _ {2}} = C \| \Phi_ {1} (x) \| _ {\mathcal {W} _ {1}} \| f _ {v} \| _ {\mathcal {B} _ {1}}.
$$

Similarly, by (2.5) and (2.10), we have for all $g_{u} \in \mathcal{B}_{2}$ and all $y \in \Omega_{2}$

$$
| g _ {u} (y) | = | \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} | \leq C \| \Phi_ {2} (y) \| _ {\mathcal {W} _ {2}} \| u \| _ {\mathcal {W} _ {1}} = C \| \Phi_ {2} (y) \| _ {\mathcal {W} _ {2}} \| g _ {u} \| _ {\mathcal {B} _ {2}}.
$$

Thus, point evaluation functionals are continuous on both $\mathcal{B}_1$ and $\mathcal{B}_2$ . By Definition 2.1, $\mathcal{B}_1$ and $\mathcal{B}_2$ are RKBSs on $\Omega_1$ and $\Omega_2$ , respectively.

Next, $\langle \cdot ,\cdot \rangle_{\mathcal{B}_1\times \mathcal{B}_2}$ is a continuous bilinear form as

$$
| \langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} | = | \langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} | \leq C \| u \| _ {\mathcal {W} _ {1}} \| v \| _ {\mathcal {W} _ {2}} = C \| f _ {v} \| _ {\mathcal {B} _ {1}} \| g _ {u} \| _ {\mathcal {B} _ {2}}.
$$

Finally, by (2.3), (2.4), (2.8) and (2.9), we have

$$
K (x, \cdot) = g _ {\Phi_ {1} (x)} \in \mathcal {B} _ {2}, f _ {v} (x) = \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \langle f _ {v}, g _ {\Phi_ {1} (x)} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} = \langle f _ {v}, K (x, \cdot) \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}}
$$

for all $x\in \Omega_1$ and all $f_{v}\in \mathcal{B}_{1}$ . Similarly,

$$
K (\cdot , y) = f _ {\Phi_ {2} (y)} \in \mathcal {B} _ {1}, g _ {u} (y) = \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \langle f _ {\Phi_ {2} (y)}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} = \langle K (\cdot , y), g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}}
$$

for all $y \in \Omega_2$ and all $g_u \in \mathcal{B}_2$ . The proof is complete.

We call $\Phi_1: \Omega_1 \to \mathcal{W}_1$ and $\Phi_2: \Omega_2 \to \mathcal{W}_2$ in Theorem 2.3 a pair of feature maps for the reproducing kernel $K$ , and $\mathcal{W}_1$ and $\mathcal{W}_2$ a pair of feature spaces for $K$ . The feature spaces and feature maps for an RKBS might not be unique. Different choices of them will lead to different reproducing kernels for the RKBS.

Below we prove the existence of a reproducing kernel for a general RKBS under the mild condition that it is separable.

Theorem 2.4 Every separable RKBS admits a reproducing kernel.

Proof: Let $\mathcal{B}$ be a separable RKBS on $X$ . Thus, there exist $f_{n} \in \mathcal{B}$ , $n \in \mathbb{N}$ such that $\operatorname{span}\{f_n : n \in \mathbb{N}\}$ is dense in $\mathcal{B}$ . We construct a pair of feature maps and feature spaces for $\mathcal{B}$ as follows. Let

$$
\mathcal {W} _ {1} = \overline {{\mathrm {s p a n}}} \{\delta_ {x}: x \in X \} \mathrm {i n} \mathcal {B} ^ {*}, \Omega_ {1} = X, \mathrm {a n d} \Phi_ {1} (x) = \delta_ {x}.
$$

Also, set

$$
\mathcal {W} _ {2} = \mathcal {B}, \Omega_ {2} = \mathbb {N}, \text {a n d} \Phi_ {2} (n) = f _ {n} (x).
$$

Clearly, the denseness condition (2.3) is satisfied. We observe that the space $\mathcal{B}_1$ followed from the construction is exactly $\mathcal{B}$ . By Theorem 2.3,

$$
K (x, n) = \langle \delta_ {x}, f _ {n} \rangle = f _ {n} (x), x \in \Omega_ {1}, n \in \mathbb {N}
$$

is a reproducing kernel for $\mathcal{B}$ .

We remark that the reproducing kernel given in the above theorem is of little use in practice. The purpose of the theorem is to verify that Definition 2.1 is indeed generic for RKBSs. Under the definition, reproducing kernels for RKBSs exist under a very mild condition, namely, separability.

# 2.3 Orlicz RKBSs

To show the advantages of our framework, we construct a new class of RKBSs based on Orlicz spaces. Orlicz spaces constitute an important generalization of $L^p$ -spaces. To this end, we shall briefly review the basic theory of Orlicz spaces [29, 30].

Set $\mathbb{R}_+ := [0, +\infty)$ . Let $\varphi: \mathbb{R}_+ \to \mathbb{R}_+$ be a strictly increasing and continuous function with $\varphi(0) = 0$ and $\lim_{t \to +\infty} \varphi(t) = +\infty$ . Besides $\varphi$ , the following three functions are central to our discussions:

$$
\psi (t) := \varphi^ {- 1} (t), \Phi (t) := \int_ {0} ^ {t} \varphi (s) d s, \Psi (t) := \int_ {0} ^ {t} \psi (s) d s, t \in \mathbb {R} _ {+}.
$$

We call $\Phi$ and $\Psi$ a pair of conjugated nice Young functions. Then

$$
x y \leq \Phi (x) + \Psi (y), x, y \in \mathbb {R} _ {+},
$$

where equality holds if $x = \psi(y)$ , or equivalently $y = \varphi(x)$ . The nice Young function $\Psi$ complementary to $\Phi$ can equally be defined by $\Psi(t) = \sup \{x|t| - \Phi(x): x \in \mathbb{R}_+\}$ , $t \in \mathbb{R}$ .

Let $(\Omega, \mathcal{F}, \mu)$ be a measure space. The Orlicz space [30] $\mathcal{L}^{\Phi}$ consists of all the $\mathcal{F}$ -measurable functions $f: \Omega \to \mathbb{C}$ such that

$$
\int_ {\Omega} \Phi (\alpha | f |) d \mu <   + \infty \text {f o r s o m e} \alpha > 0.
$$

It is a linear vector space with two equivalent norms $\| \cdot \|_{\Phi}$ , the Gauge norm (Luxemburg norm), and $|\cdot |_{\Phi}$ , the Orlicz norm. They are respectively defined by

$$
\| f \| _ {\Phi} := \inf  \left\{\alpha > 0: \int_ {\Omega} \Phi \left(\frac {| f |}{\alpha}\right) d \mu \leq \Phi (1) \right\}, \quad f \in \mathcal {L} ^ {\Phi}
$$

and

$$
| f | _ {\Phi} := \sup  \left\{\int_ {\Omega} | f g | d \mu : g \in \mathcal {L} ^ {\Psi}, \| g \| _ {\Psi} \leq 1 \right\}, f \in \mathcal {L} ^ {\Phi}.
$$

They indeed are equivalent as $\Phi(1) \| f \|_{\Phi} \leq |f|_{\Phi} \leq 2 \| f \|_{\Phi}$ , $f \in \mathcal{L}^{\Phi}$ . If $\varphi(t) = t^{p-1}$ and $\psi(t) = t^{q-1}$ , $t \in \mathbb{R}_+$ , where $1 < p, q < +\infty$ with $1/p + 1/q = 1$ , then

$$
\Phi (t) = t ^ {p} / p, \Psi (t) = t ^ {q} / q, t \in \mathbb {R} _ {+}.
$$

In this case, $\mathcal{L}^{\Phi}$ is the usual space $L_{\mu}^{p}(\Omega)$ and both the Gauge norm and Orlicz norm equal

$$
\| f \| _ {p} := \left(\int_ {\Omega} | f (x) | ^ {p} d \mu (x)\right) ^ {1 / p}, f \in L _ {\mu} ^ {p} (\Omega).
$$

If $\Phi$ and $\Psi$ are a pair of conjugated nice Young functions then $(\mathcal{L}^{\Psi},|\cdot |_{\Psi}) = (\mathcal{L}^{\Phi},\| \cdot \|_{\Phi})^{*}$ (see, Theorem 13 in Section 1.2, [30]) in the sense that for each continuous linear functional $T$ on $(\mathcal{L}^{\Phi},\| \cdot \|_{\Phi})$ there exists a unique $g\in \mathcal{L}^{\Psi}$ such that

$$
T (f) = \int_ {\Omega} f g d \mu , f \in \mathcal {L} ^ {\Phi} \mathrm {a n d} \| T \| = | g | _ {\Psi}.
$$

There is a unique semi-inner product ([23], pp. 101-104) on $(\mathcal{L}^{\Phi},\| \cdot \|_{\Phi})$ given by

$$
[ f, g ] = \| g \| _ {\Phi} ^ {2} \frac {\int_ {\Omega} f \operatorname {s g n} (\bar {g}) \varphi \Big (\frac {| g |}{\| g \| _ {\Phi}} \Big) d \mu}{\int_ {\Omega} | g | \varphi \Big (\frac {| g |}{\| g \| _ {\Phi}} \Big) d \mu}, f, g \in \mathcal {L} ^ {\Phi},
$$

where $\operatorname{sgn}(t) \coloneqq t / |t|$ if $t \in \mathbb{C} \setminus \{0\}$ and $\operatorname{sgn}(0) \coloneqq 0$ . It implies that the standard duality mapping $J_{\Phi} : (\mathcal{L}^{\Phi}, \| \cdot \|_{\Phi}) \to (\mathcal{L}^{\Psi}, |\cdot|_{\Psi})$ has the form

$$
J _ {\Phi} (f) = \frac {\| f \| _ {\Phi} ^ {2} \operatorname {s g n} (\bar {f}) \varphi \left(\frac {| f |}{\| f \| _ {\Phi}}\right)}{\int_ {\Omega} | f | \varphi \left(\frac {| f |}{\| f \| _ {\Phi}}\right) d \mu}, f \in \mathcal {L} ^ {\Phi}.
$$

Particularly, when $\mathcal{L}^{\Phi} = L_{\mu}^{p}(\Omega)$ , we observe that

$$
J _ {p} (f) = \frac {\mathrm {s g n} (\bar {f}) | f | ^ {p - 1}}{| | f | | _ {p} ^ {p - 2}}, f \in L _ {\mu} ^ {p} (\Omega),
$$

which is the usual duality mapping from $L_{\mu}^{p}(\Omega)$ to $L_{\mu}^{q}(\Omega)$ first discovered by Giles [17].

Another interesting example ([30], page 9) is when $\varphi(t) = \log(1 + t)$ and $\psi(t) = e^t - 1$ , $t \in \mathbb{R}_+$ . In this case,

$$
\Phi (t) = (1 + t) \log (1 + t) - t, \quad \Psi (t) = e ^ {t} - t - 1, \quad t \in \mathbb {R} _ {+}. \tag {2.11}
$$

To emphasize the importance of Orlicz spaces in applications, we give an illustrating example that shows the Orlicz space with the nice Young functions (2.11) can approximate the $\ell^2$ or $\ell^1$ space. Consider the following sequence of nice Young functions

$$
\Phi_ {k} (t) := \Phi (k t) = (1 + k t) \log (1 + k t) - k t, \quad t \geq 0, k > 0.
$$

Let $\Omega := \{1, 2, \dots, n\}$ and $\mu$ be the counting measure on $\Omega$ . Then for each $y := (y_1, y_2, \dots, y_n) \in \mathbb{C}^n$ , $\|y\|_{\Phi_k}$ equals the smallest nonnegative number $\alpha$ such that

$$
\sum_ {j = 1} ^ {n} \left(1 + k \frac {| y _ {j} |}{\alpha}\right) \log \left(1 + k \frac {| y _ {j} |}{\alpha}\right) - \frac {k}{\alpha} \sum_ {j = 1} ^ {n} | y _ {j} | \leq (1 + k) \log (1 + k) - k.
$$

Hence, the semi-inner-product for the corresponding Orlicz space $\mathcal{L}^{\Phi_k}$ has the form

$$
[ x, y ] = \alpha^ {2} \frac {\sum_ {j = 1} ^ {n} x _ {j} \operatorname {s g n} \left(\overline {{y _ {j}}}\right) \log \left(1 + k \frac {| y _ {j} |}{\alpha}\right)}{\sum_ {j = 1} ^ {n} | y _ {j} | \log \left(1 + k \frac {| y _ {j} |}{\alpha}\right)}, x, y \in \mathbb {C} ^ {n}.
$$

Thus, on the unit sphere where $\alpha = 1$ , we see that

$$
\lim _ {k \to 0} [ x, y ] = \lim _ {k \to 0} \frac {\sum_ {j = 1} ^ {n} x _ {j} \operatorname {s g n} (\overline {{y _ {j}}}) \log (1 + k | y _ {j} |) ^ {1 / k}}{\sum_ {j = 1} ^ {n} | y _ {j} | \log (1 + k | y _ {j} |) ^ {1 / k}} = \frac {\sum_ {j = 1} ^ {n} x _ {j} \operatorname {s g n} (\overline {{y _ {j}}}) | y _ {j} |}{\sum_ {j = 1} ^ {n} | y _ {j} | ^ {2}} = \frac {\sum_ {j = 1} ^ {n} x _ {j} \overline {{y _ {j}}}}{\sum_ {j = 1} ^ {n} | y _ {j} | ^ {2}},
$$

which is the inner product on the $\ell^2$ space, and by the L'Hôpital's rule that

$$
\lim _ {k \to + \infty} [ x, y ] = \lim _ {k \to + \infty} \frac {\sum_ {j = 1} ^ {n} x _ {j} \operatorname {s g n} (\overline {{y _ {j}}}) \frac {| y _ {j} |}{1 + k | y _ {j} |}}{\sum_ {j = 1} ^ {n} | y _ {j} | \frac {| y _ {j} |}{1 + k | y _ {j} |}} = \frac {\sum_ {j = 1} x _ {j} \operatorname {s g n} (\overline {{y _ {j}}})}{\sum_ {j = 1} ^ {n} | y _ {j} |}, x, y \in \mathbb {C} ^ {n},
$$

which is the semi-inner product on the $\ell^1$ space.

We describe our construction of Orlicz RKBSs as follow.

Theorem 2.5 Let $\Phi, \Psi$ be a pair of nice Young functions. Choose

$$
\mathcal {W} _ {1} := \left(\mathcal {L} ^ {\Phi}, \| \cdot \| _ {\Phi}\right) a n d \mathcal {W} _ {2} := \left(\mathcal {L} ^ {\Psi}, | \cdot | _ {\Psi}\right)
$$

as a pair of feature spaces. Suppose that there exist feature maps $\Phi_1: \Omega_1 \to \mathcal{W}_1, \Phi_2: \Omega_2 \to \mathcal{W}_2$ satisfying the denseness condition (2.3). Then $\mathcal{B}_1$ defined by (2.4) is an RKBS on $\Omega_1$ with the adjoint RKBS $\mathcal{B}_2$ defined by (2.5) on $\Omega_2$ endowed with the bilinear form (2.8). Moreover, a reproducing kernel for $\mathcal{B}_1$ is

$$
K (x, y) := \left\langle \Phi_ {1} (x), \Phi_ {2} (y) \right\rangle_ {\mathcal {L} ^ {\Phi}}, x \in \Omega_ {1}, y \in \Omega_ {2}.
$$

# 3 Existing examples of RKBSs

In this section, we aim at justifying that our construction in the previous section covers existing RKBSs in the literature, including the reflexive RKBS [46], the semi-inner-product RKBS [46, 47], the RKBS constructed by Borel measures [37], the RKBS with the $\ell^1$ norm [38], the RKBS with positive definite functions [13], and the $p$ -norm RKBS [43]. In particular, $C([0,1])$ is included in our framework. Hence, we are able to write out three reproducing kernels for $C([0,1])$ .

We shall primarily use Theorem 2.3 to fulfill this task. Let us keep in mind that a pair of RKBSs contain the following eleven ingredients:

$$
\Omega_ {1}, \Omega_ {2}, \mathcal {W} _ {1}, \mathcal {W} _ {2}, \Phi_ {1}, \Phi_ {2}, \langle \cdot , \cdot \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}, \mathcal {B} _ {1}, \mathcal {B} _ {2}, \langle \cdot , \cdot \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}}, K.
$$

# 3.1 Reproducing kernel Hilbert spaces

Our construction must include RKHSs. To show this, we shall briefly review basic theory of RKHSs [2, 3, 8, 19, 33, 36, 41, 50].

An RKHS $\mathcal{H}$ on a nonempty set $X$ is a Hilbert space of certain functions on $X$ such that point evaluation functionals are continuous on $\mathcal{H}$ . By the Riesz representation theorem, there exists a unique reproducing kernel $K$ on $X\times X$ such that

$$
K (\cdot , x) \in \mathcal {H} \text {f o r a l l} x \in X, \overline {{\operatorname {s p a n}}} \{K (\cdot , x): x \in X \} = \mathcal {H}
$$

and

$$
f (x) = \left(f, K (\cdot , x)\right) _ {\mathcal {H}} \text {f o r a l l} f \in \mathcal {H} \text {a n d a l l} x \in X \tag {3.12}
$$

where $(\cdot, \cdot)_{\mathcal{H}}$ denotes the inner product on $\mathcal{H}$ . Equation (3.12) is called the reproducing property in machine learning. A function $K$ on $X \times X$ is a reproducing kernel of an RKHS if and only if there exists a feature map $\Phi$ from $X$ to a Hilbert space $\mathcal{W}$ such that

$$
K (x, y) = (\Phi (x), \Phi (y)) _ {\mathcal {W}}, x, y \in X.
$$

Another well-known characterization of a reproducing kernel is for it to be positive semi-definite. There is a bijective correspondence between RKHSs and reproducing kernels. For this sake, the RKHS corresponding to a reproducing kernel $K$ is denoted by $\mathcal{H}_K$ . The feature map $\Phi$ and feature space $\mathcal{W}$ of a reproducing kernel may not be unique. In particular, we say $\Phi$ is the canonical feature map of $K$ if $\Phi(x) = K(\cdot, x)$ . In this case, $\mathcal{W} = \mathcal{H}_K$ and

$$
K (x, y) = (K (\cdot , x), K (\cdot , y)) _ {\mathcal {H} _ {K}}, x, y \in X.
$$

A reproducing kernel can be easily identified through its feature map. The following result is well-known in machine learning community [44, 50].

Lemma 3.1 [44] If $K: X \times X \to \mathbb{C}$ is a reproducing kernel with a feature map $\Phi$ from $X$ to a Hilbert space $\mathcal{W}$ , then $\mathcal{H}_K = \{ (\Phi(\cdot), u)_{\mathcal{W}} : u \in \mathcal{W} \}$ with the inner product

$$
\left(\left(\Phi (\cdot), u\right) _ {\mathcal {W}}, \left(\Phi (\cdot), v\right) _ {\mathcal {W}}\right) _ {\mathcal {H} _ {K}} = \left(\mathbb {P} _ {\Phi} v, \mathbb {P} _ {\Phi} u\right) _ {\mathcal {W}}, u, v \in \mathcal {W},
$$

where $\mathbb{P}_{\Phi}$ denotes the orthogonal projection from $\mathcal{W}$ onto $\overline{\operatorname{span}}\Phi(X)$ . If $\mathcal{W} = \overline{\operatorname{span}}\Phi(X)$ , then $\mathcal{H}_K$ is isometrically isomorphic to $\mathcal{W}$ through the linear mapping $(\Phi(\cdot), u)_{\mathcal{W}} \to u$ .

Note that the dual space of $\mathcal{H}_K$ is $\mathcal{H}_K^* = \overline{\mathcal{H}_K} \coloneqq \{\bar{f} : f \in \mathcal{H}_K\}$ . By Theorem 2.3 and Lemma 3.1, we obtain the following result.

Example 3.2 Let $\mathcal{H}_K$ be an RKHS on $X$ with the reproducing kernel $K$ , and let $\Phi$ from $X$ to a Hilbert space $\mathcal{W}$ be a feature map of $K$ such that $\mathcal{W} = \overline{\operatorname{span}}\Phi(X)$ . Choose

$$
\Omega_ {1} = \Omega_ {2} := X, \mathcal {W} _ {1} := \mathcal {W}, \mathcal {W} _ {2} := \overline {{\mathcal {W}}},
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := \Phi (x), x \in \Omega_ {1},
$$

$$
\Phi_ {2}: \Omega_ {2} \rightarrow \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := \overline {{\Phi (y)}}, y \in \Omega_ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \langle \Phi (x), v \rangle_ {\mathcal {W}} = (\Phi (x), \bar {v}) _ {\mathcal {W}}: v \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\} = \mathcal {H} _ {K}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| \bar{v}\|_{\mathcal{W}}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle u, \overline {{\Phi (y)}} \rangle_ {\mathcal {W}} = (u, \Phi (y)) _ {\mathcal {W}} = \overline {{(\Phi (y) , u) _ {\mathcal {W}}}}: u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\} = \overline {{\mathcal {H} _ {K}}}
$$

with norm $\| g_u\|_{\mathcal{B}_2}\coloneqq \| u\|_{\mathcal{W}}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is given by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle (\Phi (x), \bar {v}) _ {\mathcal {W}}, \overline {{(\Phi (y) , u) _ {\mathcal {W}}}} \rangle_ {\mathcal {H} _ {K}} = \big ((\Phi (x), \bar {v}) _ {\mathcal {W}}, (\Phi (y), u) _ {\mathcal {W}} \big) _ {\mathcal {H} _ {K}} = (u, \bar {v}) _ {\mathcal {W}}.
$$

Moreover,

$$
\langle \Phi_ {1} (x), \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle \Phi (x), \overline {{\Phi (y)}} \rangle_ {\mathcal {W}} = (\Phi (x), \Phi (y)) _ {\mathcal {W}} = K (x, y)
$$

is a reproducing kernel for $\mathcal{B}_1$ .

Proof: The denseness condition (2.6) is satisfied. By Theorem 2.3, the proof is complete.

![](images/42554ace3e45e64ea0df13254266b7c331e24001f2270bf7e10f3ce9daa8c0be.jpg)

Therefore, we have showed that an RKHS is an RKBS with the same reproducing kernel.

# 3.2 Reflexive RKBSs

Learning in Banach spaces has received considerable attention in the past two decades. The notion of reproducing kernel Banach spaces was introduced in machine learning in 2009, [46]. Reflexive RKBSs constructed in [46] are the first class of RKBSs with reproducing kernels.

A normed vector space $V$ is reflexive if $(V^{*})^{*} = V$ , that is, every continuous linear functional $T$ on $V^{*}$ must be of the form

$$
T (v ^ {*}) = v ^ {*} (u), \quad v ^ {*} \in V ^ {*}
$$

for some $u \in V$ . A Banach space is reflexive if and only if its dual is reflexive, [24].

The definition and construction of reflexive RKBSs in [46] are described below.

Definition of Reflexive RKBSs in [46]. An RKBS on $X$ is a reflexive Banach space $\mathcal{B}$ of functions on $X$ for which $\mathcal{B}^*$ is isometrically isomorphic to a Banach space $\mathcal{B}^\#$ of functions on $X$ and the point evaluation is continuous on both $\mathcal{B}$ and $\mathcal{B}^\#$ .

Construction of Reflexive RKBSs in [46]. Let $\mathcal{W}$ be a reflexive Banach space. Suppose

that there exists $\Phi : X \to \mathcal{W}$ , and $\Phi^* : X \to \mathcal{W}^*$ such that $\overline{\operatorname{span}}\Phi(X) = \mathcal{W}$ , $\overline{\operatorname{span}}\Phi^*(X) = \mathcal{W}^*$ . Then

$$
\mathcal {B} := \left\{\langle u, \Phi^ {*} (\cdot) \rangle_ {\mathcal {W}}: u \in \mathcal {W} \right\} w i t h n o r m \| \langle u, \Phi^ {*} (\cdot) \rangle_ {\mathcal {W}} \| _ {\mathcal {B}} := \| u \| _ {\mathcal {W}}
$$

is an RKBS on $X$ with the dual space

$$
\mathcal {B} ^ {\#} := \left\{\langle \Phi (\cdot), u ^ {*} \rangle_ {\mathcal {W}}: u ^ {*} \in \mathcal {W} ^ {*} \right\} e n d o w e d w i t h n o r m \| \langle \Phi (\cdot), u ^ {*} \rangle_ {\mathcal {W}} \| _ {\mathcal {B} ^ {\#}} := \| u ^ {*} \| _ {\mathcal {W} ^ {*}}
$$

and the bilinear form

$$
\left\langle \left\langle u, \Phi^ {*} (\cdot) \right\rangle_ {\mathcal {W}}, \left\langle \Phi (\cdot), u ^ {*} \right\rangle_ {\mathcal {W}} \right\rangle_ {\mathcal {B} \times \mathcal {B} ^ {\#}} := \left\langle u, u ^ {*} \right\rangle_ {\mathcal {W}}, u \in \mathcal {W}, u ^ {*} \in \mathcal {W} ^ {*}.
$$

Moreover, $K(x,y)\coloneqq \langle \Phi (x),\Phi^{*}(y)\rangle_{\mathcal{W}}$ is a reproducing kernel for $\mathcal{B}$

We show that the above construction of reflexive RKBSs falls within our framework.

Example 3.3 Assume the same conditions as in the above construction of reflexive RKBSs. Choose

$$
\begin{array}{l} \Omega_ {1} = \Omega_ {2} := X, \mathcal {W} _ {1} := \mathcal {W} ^ {*}, \mathcal {W} _ {2} := \mathcal {W}, \\ \Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := \Phi^ {*} (x), x \in \Omega_ {1}, \\ \Phi_ {2}: \Omega_ {2} \rightarrow \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := \Phi (y), y \in \Omega_ {2} \\ \end{array}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \langle \Phi^ {*} (x), v \rangle_ {\mathcal {W} ^ {*}} = \langle v, \Phi^ {*} (x) \rangle_ {\mathcal {W}}: v \in \mathcal {W} _ {2} = \mathcal {W}, x \in \Omega_ {1} \right\} = \mathcal {B}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\mathcal{W}}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle u, \Phi (y) \rangle_ {\mathcal {W} ^ {*}} = \langle \Phi (y), u \rangle_ {\mathcal {W}}: u \in \mathcal {W} _ {1} = \mathcal {W} ^ {*}, y \in \Omega_ {2} \right\} = \mathcal {B} ^ {\#}
$$

with norm $\| g_u\|_{\mathcal{B}_2} \coloneqq \| u\|_{\mathcal{W}^*}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ takes the form

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} = \langle v, u \rangle_ {\mathcal {W}}.
$$

Moreover, a reproducing kernel of $\mathcal{B}_1$ is

$$
\langle \Phi_ {1} (x), \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle \Phi^ {*} (x), \Phi (y) \rangle_ {\mathcal {W} ^ {*}} = \langle \Phi (y), \Phi^ {*} (x) \rangle_ {\mathcal {W}} f o r a l l x \in \Omega_ {1}, y \in \Omega_ {2}.
$$

Proof: Note that $\mathcal{W}$ is a reflexive Banach space. The denseness condition (2.6) is hence satisfied. By Theorem 2.3, the proof is complete.

# 3.3 Semi-inner-product RKBSs

As mentioned in [46], the lack of an inner product may cause arbitrariness in the properties of the associated reproducing kernel of an RKBS. To overcome this, the authors also proposed the second class of RKBSs, namely, semi-inner-product RKBSs. Thanks to the tool of semi-inner-products, existence, uniqueness and representer theorems for the standard learning schemes in semi-inner-product RKBSs were established therein.

For a uniformly convex and uniformly Fréchet differentiable Banach space $\mathcal{B}$ , there exists a unique semi-inner product $[\cdot, \cdot]_{\mathcal{B}}: \mathcal{B} \times \mathcal{B} \to \mathbb{C}$ such that for all $f, g, h \in \mathcal{B}$ and $\alpha \in \mathbb{C}$ ,

(i) $[f + g,h]_{\mathcal{B}} = [f,h]_{\mathcal{B}} + [g,h]_{\mathcal{B}}, [\alpha f,g]_{\mathcal{B}} = \alpha [f,g]_{\mathcal{B}},$   
(ii) $[f,f]_{\mathcal{B}} > 0$ for $f\neq 0$   
(iii) (The Cauchy-Schwartz inequality) $|[f,g]_{\mathcal{B}}|^{2} \leq [f,f]_{\mathcal{B}}[g,g]_{\mathcal{B}}$ .

We refer to Section 2 in [48] or Section 5.5 in [24], and [10, 17, 22, 46] for more details on seminner products. By the Cauchy-Schwartz inequality, for each $g \in \mathcal{B}$ , $f \to [f,g]_{\mathcal{B}}$ is a bounded linear functional on $\mathcal{B}$ , which is denoted by $g^{*} \in \mathcal{B}^{*}$ and called the dual element of $g$ . Following this definition, we have

$$
[ f, g ] _ {\mathcal {B}} = \langle f, g ^ {*} \rangle_ {\mathcal {B}}.
$$

Giles [17] proved that if $\mathcal{B}$ is a uniformly convex and uniformly Fréchet differentiable Banach space $\mathcal{B}$ , then the duality mapping $f\to f^{*}$ is bijective from $\mathcal{B}$ to $\mathcal{B}^*$ . Moreover,

$$
[ f ^ {*}, g ^ {*} ] _ {\mathcal {B} ^ {*}} = [ g, f ] _ {\mathcal {B}} \text {f o r a l l} f, g \in \mathcal {B}
$$

is a semi-inner product on $\mathcal{B}^*$ .

The following definition of the semi-inner-product RKBS (s.i.p. RKBS) comes from [46].

Definition of s.i.p. RKBS in [46]. We call a uniformly convex and uniformly Fréchet differentiable Banach space of functions on $X$ an s.i.p. RKBS.

Note that a uniformly convex Banach space is reflexive. It follows that an s.i.p. RKBS is also a reflexive RKBS. We are able to construct the s.i.p. RKBS in our framework.

Example 3.4 Let $\mathcal{W}$ be a uniformly convex and uniformly Fréchet differentiable Banach space, and $\Phi : X \to \mathcal{W}$ and $\Phi^* : X \to \mathcal{W}^*$ be such that $\overline{\operatorname{span}}\Phi(X) = \mathcal{W}$ and $\overline{\operatorname{span}}\Phi^*(X) = \mathcal{W}^*$ . Choose

$$
\Omega_ {1} = \Omega_ {2} := X, \mathcal {W} _ {1} := \mathcal {W} ^ {*}, \mathcal {W} _ {2} := \mathcal {W},
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := \Phi^ {*} (x), x \in \Omega_ {1},
$$

$$
\Phi_ {2}: \Omega_ {2} \rightarrow \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := \Phi (y), y \in \Omega_ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \langle \Phi^ {*} (x), v \rangle_ {\mathcal {W} ^ {*}} = [ \Phi^ {*} (x), v ^ {*} ] _ {\mathcal {W} ^ {*}} = [ v, \Phi (x) ] _ {\mathcal {W}}: v \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\mathcal{W}}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle u, \Phi (y) \rangle_ {\mathcal {W} ^ {*}} = [ u, \Phi (y) ^ {*} ] _ {\mathcal {W} ^ {*}} = [ \Phi (y), u ^ {*} ] _ {\mathcal {W}}: u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\}
$$

with norm $\| g_{u^*}\|_{\mathcal{B}_2} \coloneqq \| u^*\|_{\mathcal{W}^*}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is given by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} = \langle v, u \rangle_ {\mathcal {W}} = [ v, u ^ {*} ] _ {\mathcal {W}}.
$$

Moreover, a reproducing kernel for $\mathcal{B}_1$ is

$$
\langle \Phi_ {1} (x), \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \langle \Phi^ {*} (x), \Phi (y) \rangle_ {\mathcal {W} ^ {*}} = [ \Phi^ {*} (x), \Phi^ {*} (y) ] _ {\mathcal {W} ^ {*}} = [ \Phi (y), \Phi (x) ] _ {\mathcal {W}} f o r a l l x \in \Omega_ {1}, y \in \Omega_ {2}.
$$

Proof: By assumptions, $\mathcal{W}$ is a reflexive Banach space. The denseness condition (2.6) is hence satisfied. By Theorem 2.3, the proof is complete.

Here, we shall point out in Example 3.4 that

$$
\mathcal {B} _ {2} = \left\{\left[ \Phi (y), u ^ {*} \right] _ {\mathcal {W}}: u \in \mathcal {W} _ {1} = \mathcal {W} ^ {*}, y \in \Omega_ {2} \right\} = \left\{\left[ \Phi (y), u \right] _ {\mathcal {W}}: u \in \mathcal {W}, y \in X \right\}.
$$

We remark that $\mathcal{B}_1$ and $\mathcal{B}_2$ in Example 3.4 are exactly the $\mathcal{B}$ and $\mathcal{B}^*$ constructed in (Theorem 10, [46]). They also have the same reproducing kernel.

# 3.4 RKBSs by Borel measures

In order to improve the learning rate estimate of the $\ell_1$ -regularized least square regression, a class of RKBSs by Borel measures was constructed in [37] to have the $\ell_1$ norm and satisfy the linear representer theorem.

Suppose that $X$ is a locally compact Hausdorff space and denote by $C_0(X)$ the Banach space of continuous functions $f: X \to \mathbb{C}$ such that for all $\varepsilon > 0$ , the set $\{x \in X : |f(x)| \geq \varepsilon\}$ is compact. Its dual space is isometrically isomorphic to the space $\mathcal{M}(X)$ of all the regular complex-valued Borel measures on $X$ (see, Theorem 6.19 in [31]). The norm of each measure $v \in \mathcal{M}(X)$ is its total variation $\| v \|_{TV}$ .

We are able to construct the RKBSs by Borel measures in our framework.

Example 3.5 Let $X$ be a locally compact Hausdorff space, and let $K: X \times X \to \mathbb{C}$ be a continuous function such that $\overline{\operatorname{span}}\{K(\cdot, x): x \in X\} = C_0(X)$ . Choose

$$
\Omega_ {1} = \Omega_ {2} := X, \mathcal {W} _ {1} := C _ {0} (X), \mathcal {W} _ {2} = \mathcal {M} (X),
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := K (\cdot , x), x \in \Omega_ {1},
$$

$$
\Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) = \delta_ {y}, y \in \Omega_ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \int_ {X} K (t, x) d v (t): v \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{TV}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = u (y): u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\} = C _ {0} (X)
$$

with norm $\| g_u\|_{\mathcal{B}_2}\coloneqq \sup_{y\in \Omega_2}|u(y)|$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is given by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} = \int_ {X} u (t) d v (t).
$$

Moreover, $K$ is a reproducing kernel for $\mathcal{B}_1$ .

Proof: As $\Phi_2(X) = \{\delta_y : y \in X\}$ is dense in $\mathcal{M}(X) = (C_0(X))^*$ under the weak* topology, the denseness condition (2.7) holds true. By Theorem 2.3, the proof is complete.

# 3.5 RKBSs with the $\ell^1$ norm

The RKBS with the $\ell^1$ norm was developed in [38] for sparse learning. The construction starts directly with a kernel function satisfying the following two requirements:

(i) $K$ is bounded,   
(ii) for all pairwise distinct sampling points $x_{j} \in X$ , $j \in \mathbb{N}$ and $c = (c_{j} : j \in \mathbb{N}) \in \ell^{1}(\mathbb{N})$ , $\sum_{j \in \mathbb{N}} c_{j} K(x_{j}, x) = 0$ for all $x \in X$ implies $c = 0$ .

Denote for any nonempty set $X$ by

$$
\ell^ {1} (X) := \left\{u := \left(u _ {x} \in \mathbb {C}: x \in X\right): \| u \| _ {\ell^ {1} (X)} := \sum_ {x \in X} | u _ {x} | <   + \infty \right\}
$$

the Banach space of functions on $X$ that is integrable with respect to the counting measure on $X$ . Note that $X$ might be uncountable but for any $u \in \ell^1(X)$ , $\operatorname{supp} u := \{x \in X : u_x \neq 0\}$ must be at most countable. Note that $\ell^1(X)$ can be imbedded into $\mathcal{M}(X)$ .

Construction of RKBSs with the $\ell^1$ Norm in [38]. Let $K: X \times X \to \mathbb{C}$ be a kernel satisfying aforementioned two requirements (i) and (ii). Then

$$
\mathcal {B} := \left\{f _ {u} := \sum_ {x \in \operatorname {s u p p} u} u _ {x} K (x, \cdot): u \in \ell^ {1} (X) \right\}
$$

with norm $\| f_u\|_{\mathcal{B}}\coloneqq \| u\|_{\ell^1}$ , and $\mathcal{B}^\#$ the completion of the vector space of functions $\sum_{j = 1}^{n}v_{j}K(\cdot ,y_{j})$ , $y_{j}\in X$ under the supremum norm

$$
\left\| \sum_ {j = 1} ^ {n} v _ {j} K (\cdot , y _ {j}) \right\| _ {\mathcal {B} ^ {\#}} := \sup  _ {x \in X} \left| \sum_ {j = 1} ^ {n} v _ {j} K (x, y _ {j}) \right|,
$$

are both Banach space of functions on $X$ where point evaluations are continuous linear functionals. In addition, the bilinear form

$$
\left\langle \sum_ {j = 1} ^ {n} u _ {j} K (x _ {j}, \cdot), \sum_ {k = 1} ^ {m} v _ {k} K (\cdot , y _ {k}) \right\rangle_ {\mathcal {B} \times \mathcal {B} ^ {\#}} := \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {m} u _ {j} v _ {k} K (x _ {j}, y _ {k}), x _ {j}, y _ {k} \in X,
$$

can be extended to $\mathcal{B} \times \mathcal{B}^{\#}$ such that

$$
| \langle f, g \rangle_ {\mathcal {B} \times \mathcal {B} ^ {\#}} | \leq \| f \| _ {\mathcal {B}} \| g \| _ {\mathcal {B} ^ {\#}} f o r a l l f \in \mathcal {B}, g \in \mathcal {B} ^ {\#}
$$

and

$$
\langle f, K (\cdot , y) \rangle_ {\mathcal {B} \times \mathcal {B} ^ {\#}} = f (y), \langle K (x, \cdot), g \rangle_ {\mathcal {B} \times \mathcal {B} ^ {\#}} = g (x) f o r a l l x, y \in X, f \in \mathcal {B}, g \in \mathcal {B} ^ {\#}.
$$

We show below that RKBSs with the $\ell^1$ norm fall into our framework.

Example 3.6 Let $X$ be a locally compact Hausdorff space, and let $K: X \times X \to \mathbb{C}$ be bounded and continuous such that $C_0(X) = \overline{\operatorname{span}}\{K(\cdot, x): x \in X\}$ . Choose

$$
\Omega_ {1} = \Omega_ {2} := X, \mathcal {W} _ {1} := C _ {0} (X), \mathcal {W} _ {2} := \ell^ {1} (X),
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := K (\cdot , x), \quad x \in \Omega_ {1},
$$

$$
\Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) = \delta_ {y}, \quad y \in \Omega_ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \sum_ {t \in \operatorname {s u p p} v} v _ {t} K (t, x): v \in \mathcal {W} _ {2} = \ell^ {1} (X), x \in \Omega_ {1} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\ell^1 (X)}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = u (y): u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\} = C _ {0} (X)
$$

with norm $\| g_u\|_{\mathcal{B}_2}\coloneqq \sup_{y\in X}|u(y)|$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is given by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} := \sum_ {t \in \operatorname {s u p p} v} v _ {t} u (t).
$$

Moreover, $K$ is a reproducing kernel for $\mathcal{B}_1$ .

Proof: The boundedness of $K$ guarantees that $f_{v}$ in $\mathcal{B}_1$ is well-defined. The set $\Phi_2(X) = \{\delta_y : y \in X\}$ is dense in $\mathcal{M}(X) = (C_0(X))^*$ under the weak* topology. The denseness condition (2.7) is hence satisfied. By Theorem 2.3, the proof is complete.

In the rest of this subsection, we discuss the particular and interesting space $C([0,1])$ . We shall show that $C([0,1])$ is an RKBS in our framework and shall present several explicit reproducing kernels for the space. Non-uniqueness of the reproducing kernel is caused by existence of many feature maps $\Phi_1: [0,1] \to C([0,1])$ satisfying the denseness condition $\overline{\operatorname{span}} \Phi_1(X) = C([0,1])$ .

Example 3.7 Choose

$$
\Omega_ {1} = \Omega_ {2} := [ 0, 1 ], \mathcal {W} _ {1} := C ([ 0, 1 ]), \mathcal {W} _ {2} := \ell^ {1} ([ 0, 1 ]),
$$

$$
\Phi_ {1}: \Omega_ {1} \rightarrow \mathcal {W} _ {1}, \quad \Phi_ {1} (x) (t) = 1 - | t - x |, x \in \Omega_ {1}, t \in [ 0, 1 ],
$$

$$
\Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) = \delta_ {y}, y \in \Omega_ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \sum_ {t \in \operatorname {s u p p} v} v _ {t} (1 - | t - x |): v \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{TV}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = u (y): u \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\} = C ([ 0, 1 ])
$$

with norm $\| g_u\|_{\mathcal{B}_2}:= \sup_{y\in [0,1]}|u(y)|$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is given by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} := \int_ {0} ^ {1} u (t) d v (t).
$$

Moreover, $K(x,y)\coloneqq \langle \Phi_1(x),\Phi_2(y)\rangle_{\mathcal{W}_1} = 1 - |x - y|$ $x,y\in [0,1]$ is a reproducing kernel for $\mathcal{B}_1$

Proof: Note that every continuous function on $[0,1]$ can be approximated uniformly by piecewise linear functions. Thus, we have $\mathcal{W}_1 = \overline{\operatorname{span}}\Phi_1([0,1]) = \overline{\operatorname{span}}\{1 - |\cdot -x|:x\in [0,1]\}$ . The denseness condition (2.7) is hence satisfied. By Theorem 2.3, the proof is complete.

We can also take $\Phi_1(x)(t) \coloneqq (1 + t)^x$ or $\Phi_1(x)(t) \coloneqq e^{tx}$ in Example 3.7 and they all satisfy the denseness condition (2.6). This is true by the fact in complex analysis that zeros of a nontrivial holomorphic function are isolated. Correspondingly,

$$
K (x, y) = (1 + y) ^ {x} \mathrm {o r} K (x, y) = e ^ {x y} \mathrm {f o r a l l} x, y \in [ 0, 1 ]
$$

can be viewed as reproducing kernels for $\mathcal{B}_1$ as well. By Definition 2.2, $\widetilde{K}(x,y) = K(y,x)$ is a reproducing kernel of $\mathcal{B}_2 = C([0,1])$ . Thus, we obtain three reproducing kernels for $C([0,1])$ :

$$
1 - | x - y |, (1 + x) ^ {y}, e ^ {x y}, x, y \in [ 0, 1 ].
$$

# 3.6 RKBSs with positive definite functions

The relationship between generalized Sobolev spaces and RKHSs was established by developing a connection between Green functions and reproducing kernels. Motivated by this, the authors in [13] used Fourier transform techniques to construct RKBSs with positive definite functions. Furthermore, Ye in [45] developed numerical algorithms for support vector machines in those RKBSs.

Let $\phi \in L^{1}(\mathbb{R}^{d})\cap C(\mathbb{R}^{d})$ be positive definite, that is, for all finite distinct points $x_{1},x_{2},\ldots ,x_{n}\in$ $\mathbb{R}^d$ , the matrix $[\phi (x_j - x_k):j,k = 1,2,\dots ,n]$ is strictly positive-definite. It has been known that $\phi$ is positive definite if and only if it is bounded, its Fourier transform $\hat{\phi}$ is nonnegative, and

$$
S _ {\hat {\phi}} := \left\{\xi \in \mathbb {R} ^ {d}: \hat {\phi} (\xi) \neq 0 \right\}
$$

has positive Lebesgue measure (see, for instance, Section 6.2 in [41]). In this paper, we use the following form of the Fourier transform

$$
\hat {f} (\xi) = \int_ {\mathbb {R} ^ {d}} f (x) e ^ {- i 2 \pi x \cdot \xi} d x, \xi \in \mathbb {R} ^ {d}, f \in L ^ {1} (\mathbb {R} ^ {d})
$$

and the inverse Fourier transform

$$
\check {f} (\xi) = \int_ {\mathbb {R} ^ {d}} f (x) e ^ {i 2 \pi x \cdot \xi} d x, \xi \in \mathbb {R} ^ {d}, f \in L ^ {1} (\mathbb {R} ^ {d}).
$$

We show below that RKBSs (Theorem 4.1 in [13] or Theorem 1 in [45]) with positive definite functions fall into our framework.

Example 3.8 Let $1 < q \leq 2 \leq p < +\infty$ and $1/p + 1/q = 1$ . Suppose that $\phi \in L^{1}(\mathbb{R}^{d}) \cap C(\mathbb{R}^{d})$ is a positive definite, even function on $\mathbb{R}^d$ and that $\hat{\phi}^{q-1} \in L^{1}(\mathbb{R}^{d})$ . Choose

$$
\Omega_ {1} = \Omega_ {2} := \mathbb {R} ^ {d},
$$

$$
\mathcal {W} _ {1} := \left\{u \in L ^ {q} (\mathbb {R} ^ {d}) \cap C (\mathbb {R} ^ {d}): S _ {\check {u}} \subseteq S _ {\hat {\phi}}, \check {u} / \hat {\phi} ^ {1 / p} \in L ^ {p} (\mathbb {R} ^ {d}) \right\} w i t h n o r m \| u \| _ {\mathcal {W} _ {1}} = \left(\int_ {\mathbb {R} ^ {d}} \frac {| \check {u} (\xi) | ^ {p}}{\hat {\phi} (\xi)} d \xi\right) ^ {1 / p}
$$

$$
\mathcal {W} _ {2} := \left\{v \in L ^ {p} (\mathbb {R} ^ {d}) \cap C (\mathbb {R} ^ {d}): S _ {\hat {v}} \subseteq S _ {\hat {\phi}}, \hat {v} / \hat {\phi} ^ {1 / q} \in L ^ {q} (\mathbb {R} ^ {d}) \right\} w i t h n o r m \| v \| _ {\mathcal {W} _ {2}} = \left(\int_ {\mathbb {R} ^ {d}} \frac {| \hat {v} (\xi) | ^ {q}}{\hat {\phi} (\xi)} d \xi\right) ^ {1 / q}
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := \phi (\cdot - x), x \in \Omega_ {1},
$$

$$
\Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := \phi (\cdot - y), y \in \Omega_ {2}
$$

and define the following continuous bilinear form on $\mathcal{W}_1\times \mathcal{W}_2$

$$
\langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} := \int_ {\mathbb {R} ^ {d}} \frac {\check {u} (\xi) \hat {v} (\xi)}{\hat {\phi} (\xi)} d \xi , \quad u \in \mathcal {W} _ {1}, v \in \mathcal {W} _ {2}
$$

in Theorem 2.3. Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \int_ {\mathbb {R} ^ {d}} \frac {\check {\phi} (\xi) e ^ {i 2 \pi x \cdot \xi} \hat {v} (\xi)}{\hat {\phi} (\xi)} d \xi = \int_ {\mathbb {R} ^ {d}} \frac {\hat {\phi} (\xi) e ^ {i 2 \pi x \cdot \xi} \hat {v} (\xi)}{\hat {\phi} (\xi)} d \xi = v (x): v \in \mathcal {W} _ {2} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\mathcal{W}_2}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \int_ {\mathbb {R} ^ {d}} \frac {\check {u} (\xi) \hat {\phi} (\xi) e ^ {- i 2 \pi y \cdot \xi}}{\hat {\phi} (\xi)} d \xi = u (y): u \in \mathcal {W} _ {1} \right\}
$$

with norm $\| g_u\|_{\mathcal{B}_2} := \| u\|_{\mathcal{W}_1}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is defined by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}. \tag {3.13}
$$

Moreover, $\phi (x - y)$ is a reproducing kernel for $\mathcal{B}_1$

Proof: To begin with, we shall check the denseness condition (2.3). Since $\phi \in L^{1}(\mathbb{R}^{d})\cap C(\mathbb{R}^{d})$ is positive definite, we have $\hat{\phi}\in L^{1}(\mathbb{R}^{d})\cap C(\mathbb{R}^{d})$ and $\hat{\phi}^{p - 1}\in L^1 (\mathbb{R}^d)$ for $p\geq 2$ . Observe that $\check{\phi} = \hat{\phi}$ as $\phi$ is an even function on $\mathbb{R}^d$ . For each $x\in \mathbb{R}^d$ , we compute

$$
\| \phi (\cdot - x) \| _ {\mathcal {W} _ {1}} = \left(\int_ {\mathbb {R} ^ {d}} \frac {| \hat {\phi} (\xi) e ^ {i 2 \pi x \cdot \xi} | ^ {p}}{\hat {\phi} (\xi)} d \xi\right) ^ {1 / p} = \int_ {\mathbb {R} ^ {d}} | \hat {\phi} (\xi) | ^ {p - 1} d \xi <   + \infty ,
$$

which implies $\phi (\cdot -x)\in \mathcal{W}_1$ for all $x\in \mathbb{R}^d$ . Furthermore, for any $v\in \mathcal{W}_2$

$$
\langle \phi (\cdot - x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \int_ {\mathbb {R} ^ {d}} \frac {\hat {\phi} (\xi) e ^ {i 2 \pi x \cdot \xi} \hat {v} (\xi)}{\hat {\phi} (\xi)} d \xi = v (x) = 0 \text {f o r a l l} x \in \mathbb {R} ^ {d}
$$

implies $v = 0$ . Thus, span $\Phi_1(\Omega_1) = \operatorname{span}\{\phi(\cdot - x) : x \in \mathbb{R}^d\}$ is dense in $\mathcal{W}_1$ with respect to the bilinear form $\langle \cdot, \cdot \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ . That span $\Phi_2(\Omega_2)$ is dense in $\mathcal{W}_2$ with respect to the bilinear form can be proved in a similar manner. The denseness condition (2.3) is hence satisfied.

Let $K(x,y)\coloneqq \langle \Phi_1(x),\Phi_2(y)\rangle_{\mathcal{W}_1\times \mathcal{W}_2} = \langle \phi (\cdot -x),\phi (\cdot -y)\rangle_{\mathcal{W}_1\times \mathcal{W}_2}$ . By (3.13), we have

$$
K (x, y) = \int_ {\mathbb {R} ^ {d}} \frac {\hat {\phi} (\xi) e ^ {i 2 \pi x \cdot \xi} \hat {\phi} (\xi) e ^ {- i 2 \pi y \cdot \xi}}{\hat {\phi} (\xi)} d \xi = \int_ {\mathbb {R} ^ {d}} \hat {\phi} (\xi) e ^ {i 2 \pi (x - y) \cdot \xi} d \xi = \phi (x - y), x, y \in \mathbb {R} ^ {d}.
$$

The proof is complete.

We remark that the space

$$
\mathcal {B} _ {1} = \mathcal {W} _ {2} = \left\{v \in L ^ {p} (\mathbb {R} ^ {d}) \cap C (\mathbb {R} ^ {d}): S _ {\hat {v}} \subseteq S _ {\hat {\phi}}, \hat {v} / \hat {\phi} ^ {1 / q} \in L ^ {q} (\mathbb {R} ^ {d}) \right\}
$$

in Example 3.8 is $\mathcal{B}_{\Phi}^{p}(\mathbb{R}^{d})$ , $2 \leq p < +\infty$ in Theorem 1 of [45].

# 3.7 $p$ -norm RKBSs

The use of semi-inner products in the construction of RKBSs has its limitations. To overcome this issue and for the sake of sparse learning, Xu and Ye [43] constructed a class of $p$ -norm RKBSs via generalized Mercer kernels.

The generalized Mercer kernel used in [43] takes the following form

$$
K (x, y) = \sum_ {n \in \mathbb {Z}} \phi_ {n} (x) \psi_ {n} (y), x \in \Omega_ {1}, y \in \Omega_ {2} \tag {3.14}
$$

where $\{\phi_n : n \in \mathbb{Z}\}$ and $\{\psi_n : n \in \mathbb{Z}\}$ are sequences of functions on $\Omega_1$ and $\Omega_2$ , respectively. For instance, the Gaussian kernel and the Brownian bridge kernel are generalized Mercer kernels. Denote by $c_0$ the Banach space of sequences on $\mathbb{Z}$ that vanish at infinity and are endowed with the supremum norm. We show below that $p$ -norm RKBSs fall into our framework.

Example 3.9 Let $1 < p < +\infty$ , $1/p + 1/q = 1$ . Choose

$$
\begin{array}{l} \mathcal {W} _ {1} := \ell^ {q}, \quad \mathcal {W} _ {2} := \ell^ {p}, \\ \Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := (\phi_ {n} (x): n \in \mathbb {Z}), \\ \Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := (\psi_ {n} (y): n \in \mathbb {Z}) \\ \end{array}
$$

in Theorem 2.3 such that $\mathcal{W}_1 = \overline{\mathrm{span}}\Phi_1(\Omega_1)$ and $\mathcal{W}_2 = \overline{\mathrm{span}}\Phi_2(\Omega_2)$ . Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} v _ {n} \phi_ {n} (x): x \in \Omega_ {1}, v := (v _ {n}: n \in \mathbb {Z}) \in \mathcal {W} _ {2} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\ell^p}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} u _ {n} \psi_ {n} (y): y \in \Omega_ {2}, u := (u _ {n}: n \in \mathbb {Z}) \in \mathcal {W} _ {1} \right\}
$$

with norm $\| g_u\|_{\mathcal{B}_2}\coloneqq \| u\|_{\ell^q}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is defined by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} u _ {n} v _ {n}.
$$

Moreover, $K$ defined as in (3.14) is a reproducing kernel for $\mathcal{B}_1$ .

Proof: Note that $\ell^p = (\ell^q)^*$ , where $1/p + 1/q = 1$ , $1 < p < +\infty$ . The denseness condition (2.6) is hence satisfied. The claim follows from Theorem 2.3.

The RKBSs $\mathcal{B}_1$ and $\mathcal{B}_2$ in Example 3.9 are exactly $\mathcal{B}_K^p (\Omega_1)$ and $\mathcal{B}_{K'}^q (\Omega_2)$ defined as in (3.5) and (3.6) of [43], respectively. Here, $K^{\prime}(x,y)\coloneqq K(y,x)$ , $x\in \Omega_2,y\in \Omega_1$ .

Example 3.10 Choose

$$
\mathcal {W} _ {1} = c _ {0}, \quad \mathcal {W} _ {2} = \ell^ {1},
$$

$$
\Phi_ {1}: \Omega_ {1} \to \mathcal {W} _ {1}, \quad \Phi_ {1} (x) := (\phi_ {n} (x): n \in \mathbb {Z}),
$$

$$
\Phi_ {2}: \Omega_ {2} \to \mathcal {W} _ {2}, \quad \Phi_ {2} (y) := (\psi_ {n} (y): n \in \mathbb {Z})
$$

in Theorem 2.3 such that $\mathcal{W}_1 = \overline{\mathrm{span}}\Phi_1(\Omega_1)$ and $\mathcal{W}_2 = \overline{\mathrm{span}}\Phi_2(\Omega_2)$ . Then

$$
\mathcal {B} _ {1} := \left\{f _ {v} (x) := \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} v _ {n} \phi_ {n} (x): v := (v _ {n}: n \in \mathbb {Z}) \in \mathcal {W} _ {2}, x \in \Omega_ {1} \right\}
$$

with norm $\| f_v\|_{\mathcal{B}_1} \coloneqq \| v\|_{\ell^1}$ is an RKBS on $\Omega_1$ . Its adjoint RKBS is

$$
\mathcal {B} _ {2} := \left\{g _ {u} (y) := \langle u, \Phi_ {2} (y) \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} u _ {n} \psi_ {n} (y): u := (u _ {n}: n \in \mathbb {Z}) \in \mathcal {W} _ {1}, y \in \Omega_ {2} \right\}
$$

with norm $\| g_u\|_{\mathcal{B}_2}\coloneqq \| u\|_{c_0}$ . The bilinear form on $\mathcal{B}_1\times \mathcal{B}_2$ is defined by

$$
\langle f _ {v}, g _ {u} \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} := \langle u, v \rangle_ {\mathcal {W} _ {1}} = \sum_ {n \in \mathbb {Z}} u _ {n} v _ {n}.
$$

Moreover, $K$ defined as in (3.14) is a reproducing kernel for $\mathcal{B}_1$ .

Proof: Note that $\mathcal{W}_2 = \ell^1 = \mathcal{W}_1^* = c_0^*$ . The denseness condition (2.6) is hence satisfied. By Theorem 2.3, the proof is complete.

The RKBSs $\mathcal{B}_1$ and $\mathcal{B}_2$ in Example 3.10 are exactly $\mathcal{B}_K^1 (\Omega_1)$ and $\mathcal{B}_{K'}^\infty (\Omega_2)$ defined as in (3.14) and (3.15) of [43], respectively.

# 4 Representer theorems for machine learning in RKBSs

Most machine learning tasks boil down to a regularized minimization problem. When kernel methods are used, a representative theorem asserts that the minimizer is a linear combination of the kernel functions at the sampling points. This is key to the mathematical analysis of kernel methods in machine learning [7, 8, 33]. The classical representative theorem in RKHSs was first established by Kimeldorf and Wahba [21]. The result was generalized to non-quadratic loss functions in [6], and to general regularizers in [32]. Recent references [38, 43, 45, 46, 48] developed representative theorems for various RKBSs introduced in the previous section. The primary purpose of this section is to present a representative theorem for RKBSs constructed in our framework, thus unifying the representative theorems in the references.

Let $\mathcal{B}_1$ be an RKBS constructed as in Theorem 2.3 via a continuous bilinear form and a pair of feature maps. We shall establish a representative theorem for the regularization network in $\mathcal{B}_1$ . We begin the analysis with the related minimal norm interpolation in $\mathcal{B}_1$ .

# 4.1 Minimal norm interpolation

The problem of minimal norm interpolation is to find a function with the smallest norm in $\mathcal{B}_1$ that interpolates a prescribed set of sampled data. Let $\mathbb{N}_m\coloneqq \{1,2,\ldots ,m\}$ , $\mathbf{x}\coloneqq \{x_{j}:j\in \mathbb{N}_{m}\} \subseteq \Omega_{1}$ be a set of $m$ pairwise distinct inputs, and $\mathbf{t}\coloneqq \{t_j:j\in \mathbb{N}_m\} \subseteq \mathbb{C}$ be the corresponding outputs.

The minimal norm interpolation problem looks for the minimizer

$$
f _ {\inf } := \arg \inf  _ {f \in S _ {\mathbf {x}, \mathbf {t}}} \| f \| _ {\mathcal {B} _ {1}} \text {w h e r e} S _ {\mathbf {x}, \mathbf {t}} = \left\{f \in \mathcal {B} _ {1}: f \left(x _ {j}\right) = t _ {j}, j \in \mathbb {N} _ {m} \right\} \tag {4.15}
$$

provided that it exists and is unique. By (2.4) and the denseness condition (2.3), (4.15) can be equivalently reformulated as

$$
f _ {\mathrm {i n f}} = \langle \Phi_ {1} (\cdot), v _ {\mathrm {i n f}} \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}
$$

where

$$
v _ {\text {i n f}} := \arg \inf  _ {v \in V _ {\mathbf {x}, \mathbf {t}}} \| v \| _ {\mathcal {W} _ {2}} \tag {4.16}
$$

with

$$
V _ {\mathbf {x}, \mathbf {t}} := \left\{v \in \mathcal {W} _ {2}: \langle \Phi_ {1} (x _ {j}), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = t _ {j}, j \in \mathbb {N} _ {m} \right\}. \tag {4.17}
$$

In the special case when $t_j = 0$ for every $1 \leq j \leq m$ ,

$$
V _ {\mathbf {x}, 0} = \left\{v \in \mathcal {W} _ {2}: \langle \Phi_ {1} (x _ {j}), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = 0: j \in \mathbb {N} _ {m} \right\} = \left(\Phi_ {1} (\mathbf {x})\right) ^ {\vdash}, \tag {4.18}
$$

where $\Phi_1(\mathbf{x})\coloneqq \{\Phi_1(x_1),\Phi_1(x_2),\ldots ,\Phi_1(x_m)\}$ . Here, for a subset $A\subseteq \mathcal{W}_1$

$$
A ^ {\vdash} := \left\{v \in \mathcal {W} _ {2}: \langle a, v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = 0 \text {f o r a l l} a \in A \right\}.
$$

Recall that for a subset $A$ in a normed vector space $V$ ,

$$
A ^ {\perp} := \left\{w \in V ^ {*}: w (a) = 0 \text {f o r a l l} a \in A \right\}.
$$

When $\mathcal{W}_2\subseteq \mathcal{W}_1^*$ , $A^{\perp}\subseteq A^{\perp}$ for $A\subseteq \mathcal{W}_1$

Next, we shall explore the condition ensuring that $V_{\mathbf{x},\mathbf{t}}$ is nonempty.

Lemma 4.1 The set $V_{\mathbf{x},\mathbf{t}}$ defined by (4.17) is nonempty for any $\mathbf{t} \in \mathbb{C}^m$ if and only if $\{\Phi_1(x_j) : j \in \mathbb{N}_m\}$ is linearly independent in $\mathcal{W}_1$ .

Proof: One sees that $V_{\mathbf{x},\mathbf{t}}$ is nonempty for any $\mathbf{t} \in \mathbb{C}^m$ if and only if $\operatorname{span}\{(f(x_j):j \in \mathbb{N}_m):f \in \mathcal{B}_1\}$ is dense in $\mathbb{C}^m$ . Note that for each $f \in \mathcal{B}_1$ , there exists a unique $v \in \overline{\operatorname{span}}\{\Phi_2(y):y \in \Omega_2\}$ such that $f(x) := f_v(x) = \langle \Phi_1(x),v\rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ , $x \in \Omega_1$ . Using the reproducing property, we have for each $(c_j:j \in \mathbb{N}_m) \in \mathbb{C}^m$ that

$$
\sum_ {j = 1} ^ {m} c _ {j} f (x _ {j}) = \sum_ {j = 1} ^ {m} c _ {j} \langle f _ {v}, K (\cdot , x _ {j}) \rangle_ {\mathcal {B} _ {1} \times \mathcal {B} _ {2}} = \sum_ {j = 1} ^ {m} c _ {j} \langle \Phi_ {1} (x _ {j}), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}} = \left\langle \sum_ {j = 1} ^ {m} c _ {j} \Phi_ {1} (x _ {j}), v \right\rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}.
$$

By the denseness condition (2.3), the above equation implies that $\{\Phi_1(x_j):j\in \mathbb{N}_m\}$ is linearly independent in $\mathcal{W}_1$ if and only if $\operatorname {span}\{(f(x_j):j\in \mathbb{N}_m):f\in \mathcal{B}_1\}$ is dense in $\mathbb{C}^m$ . The proof is complete.

Before moving on, we need several concepts from the theory of Banach spaces (see, for instance, Sections 1.11, 5.1 and 5.4 in [24]). A normed vector space $V$ is strictly convex (rotund) if $\|tf + (1 - t)g\|_V < 1$ whenever $\|f\|_V = \|g\|_V = 1$ , $f \neq g$ , and $0 < t < 1$ , and is Gâteaux differentiable if for all $f, h \in V \setminus \{0\}$ , $\lim_{\tau \to 0} \frac{\|f + \tau h\|_V - \|f\|_V}{\tau}$ exists. For each $f \neq 0$ in a Gâteaux differentiable normed vector space $V$ , there exists a bounded linear functional, denoted by $\mathcal{G}(f) \in V^*$ and called a Gâteaux derivative of $f$ , such that

$$
\langle h, \mathcal {G} (f) \rangle_ {V} = \lim  _ {\tau \rightarrow 0} \frac {\| f + \tau h \| _ {V} - \| f \| _ {V}}{\tau} \text {f o r a l l} h \in V.
$$

We make a convention that $\mathcal{G}(f) = 0$ if $f = 0$ .

Reflexivity and strict convexity of a Banach space ensure existence and uniqueness of the best approximation in the space (see, Corollary 5.1.19 in [24]).

Lemma 4.2 [24] If $V$ is a reflexive and strictly convex Banach space, then for any nonempty closed convex subset $A \subseteq V$ and any $x \in V$ there exists a unique $x_0 \in A$ such that

$$
\| x - x _ {0} \| _ {V} = \inf  \left\{\| x - a \| _ {V}: a \in A \right\}.
$$

The last lemma needed is about orthogonality in normed vector spaces (see, page 272, [20]). Let $V$ be a normed vector space. We say that $f \in V$ is orthogonal to $g \in V$ if $\| f + \tau g \|_V \geq \| f \|_V$ for all $\tau \in \mathbb{C}$ . We call $f \in V$ orthogonal to a subspace $\mathcal{N}$ of $V$ if it is orthogonal to every vector in $\mathcal{N}$ .

Lemma 4.3 [20] If a normed vector space $V$ is Gâteaux differentiable, then $f \in V$ is orthogonal to $g \in V$ if and only if $\langle g, \mathcal{G}(f) \rangle_V = 0$ .

We are now ready to develop a representative theorem for the minimal norm interpolation in RKBSs constructed in our framework.

Theorem 4.4 (Representer theorem) Assume the same assumptions as in Theorem 2.3. In addition, suppose that $\mathcal{W}_2$ is reflexive, strictly convex and Gâteaux differentiable, and the set $\{\Phi_1(x_j):j\in \mathbb{N}_m\}$ is linearly independent in $\mathcal{W}_1$ . Then the minimal norm interpolation problem (4.16) has a unique solution $v_{\mathrm{inf}}\in \mathcal{W}_2$ and it satisfies

$$
\mathcal {G} \left(v _ {\inf }\right) \in \left(\left(\Phi_ {1} (\mathbf {x})\right) ^ {\vdash}\right) ^ {\perp}. \tag {4.19}
$$

Proof: By Lemma 4.1, linear independence of $\{\Phi_1(x_j):j\in \mathbb{N}_m\}$ in $\mathcal{W}_1$ implies that $V_{\mathbf{x},\mathbf{t}}$ is nonempty. Clearly, $V_{\mathbf{x},\mathbf{t}}$ is closed and convex in $\mathcal{W}_2$ . By Lemma 4.2, there exists a unique $v\in V_{\mathbf{x},\mathbf{t}}$ , denoted by $v_{\mathrm{inf}}$ , such that

$$
\| v _ {\mathrm {i n f}} \| _ {\mathcal {W} _ {2}} = \inf  _ {v \in V _ {\mathbf {x}, \mathbf {t}}} \| v \| _ {\mathcal {W} _ {2}}.
$$

If $v_{\mathrm{inf}} = 0$ in $\mathcal{W}_2$ , then (4.19) holds. Observe that $v_{\mathrm{inf}} + V_{\mathbf{x},0} = V_{\mathbf{x},\mathbf{t}}$ , where $V_{\mathbf{x},0}$ is defined by (4.18). Since $v_{\mathrm{inf}}$ is the minimizer for the minimal norm interpolation problem (4.16) and $v_{\mathrm{inf}} + v \in V_{\mathbf{x},\mathbf{t}}$ for each $v \in V_{\mathbf{x},0}$ , we have

$$
\left\| v _ {\inf } + v \right\| _ {\mathcal {W} _ {2}} \geq \left\| v _ {\inf } \right\| _ {\mathcal {W} _ {2}} \text {f o r a l l} v \in V _ {\mathbf {x}, 0}.
$$

By Lemma 4.3, $\langle v,\mathcal{G}(v_{\mathrm{inf}})\rangle_{\mathcal{W}_2} = 0$ for all $v\in V_{\mathbf{x},0}$ , which implies $\mathcal{G}(v_{\mathrm{inf}})\in V_{\mathbf{x},0}^{\perp}$ . The proof is complete.

When $\mathcal{W}_2 = \mathcal{W}_1^*$ , the above result can be simplified.

Corollary 4.5 Assume the same assumptions as in Theorem 4.4. If, in addition, $\mathcal{W}_2 = \mathcal{W}_1^*$ , then the minimal norm interpolation problem (4.16) has a unique solution $v_{\mathrm{inf}} \in \mathcal{W}_2$ and it satisfies

$$
\mathcal {G} (v _ {\text {i n f}}) \in \operatorname {s p a n} \Phi_ {1} (\mathbf {x}).
$$

Proof: Since $\mathcal{W}_2 = \mathcal{W}_1^*$ and $\mathcal{W}_2$ is reflexive, by Theorem 4.4, we have

$$
\mathcal {G} (v _ {\mathrm {i n f}}) \in ((\Phi_ {1} (\mathbf {x})) ^ {\perp}) ^ {\perp} = \operatorname {s p a n} \Phi_ {1} (\mathbf {x}).
$$

The proof is complete.

We shall make some comments on the assumptions of Corollary 4.5. Firstly, note that the constructed spaces $\mathcal{B}_1$ and $\mathcal{B}_2$ are isomorphic to $\mathcal{W}_2$ and $\mathcal{W}_1$ , respectively. Therefore, $\mathcal{W}_2 = \mathcal{W}_1^*$ is equivalent to $\mathcal{B}_2 = \mathcal{B}_1^*$ (in the sense of isomorphism). By the discussion in Section 3, the condition $\mathcal{W}_2 = \mathcal{W}_1^*$ is satisfied by RKHSs, Orlicz RKBSs, reflexive RKBSs, semi-inner-product RKBSs, RKBSs with Borel measures, RKBSs with positive definite functions, and the $p$ -norm RKBSs ( $1 < p < +\infty$ ), but not satisfied by RKBSs with the $\ell^1$ norm or the 1-norm RKBSs. Secondly, for $1 < p < +\infty$ , $\ell^p$ and $L^p$ are reflexive, strictly convex, and Gâteaux differentiable. It is also well-known that $\ell^1$ is non-reflexive. As a result, the properties of reflexivity, strict convexity, and Gâteaux differentiability are satisfied by the semi-inner product RKBSs, the $p$ -norm RKBSs ( $1 < p < +\infty$ ), and RKBSs with positive definite functions, but are not satisfied by the RKBSs with Borel measures, RKBSs with the $\ell^1$ norm, or the 1-norm RKBSs [43]. Consequently, additional requirements have to be imposed to ensure a linear representative theorem in the latter three spaces. For instance, a uniform boundedness of the Lebesgue constant condition on the reproducing kernel was imposed in [38] for the RKBS with the $\ell^1$ -norm.

In addition, we remark that when an RKBS reduces to an RKHS, the above results recover the classical representer theorem for minimal norm interpolation in RKHSs.

# 4.2 Regularization networks

We consider learning a function from a prescribed set of finite sampling data

$$
\mathbf {z} := \left\{\left(x _ {j}, t _ {j}\right): j \in \mathbb {N} _ {m} \right\} \subseteq \Omega_ {1} \times \mathbb {C}.
$$

Let $L_{\mathbf{t}}:\mathbb{C}^{m}\to \mathbb{R}_{+}$ be a loss function that is continuous and convex. For each $f\in \mathcal{B}_1$ , we set

$$
\mathcal {E} _ {\mathbf {z}, \lambda} (f) := L _ {\mathbf {t}} (f (\mathbf {x})) + \lambda \phi (\| f \| _ {\mathcal {B} _ {1}}),
$$

where $f(\mathbf{x}) \coloneqq (f(x_{j}): j \in \mathbb{N}_{m})$ , and the regularization function $\phi: \mathbb{R}_{+} \to \mathbb{R}_{+}$ is continuous, convex and strictly increasing with $\lim_{t \to +\infty} \phi(t) = +\infty$ . A regularization network in an RKBS $\mathcal{B}_1$ takes the form:

$$
\inf  _ {f \in \mathcal {B} _ {1}} \mathcal {E} _ {\mathbf {z}, \lambda} (f). \tag {4.20}
$$

Note that each $f \in \mathcal{B}_1$ corresponds to a unique $v \in \overline{\operatorname{span}}\{\Phi_2(y):y \in \Omega_2\}$ such that

$$
f (x) := f _ {v} (x) = \langle \Phi_ {1} (x), v \rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}, x \in \Omega_ {1}.
$$

Thus, (4.20) reduces to

$$
\mathbf {v} _ {\inf } := \arg \inf  _ {v \in \mathcal {W} _ {2}} L _ {\mathbf {t}} \left(\left(\left\langle \Phi_ {1} \left(x _ {j}\right), v \right\rangle_ {\mathcal {W} _ {1} \times \mathcal {W} _ {2}}: j \in \mathbb {N} _ {m}\right)\right) + \lambda \phi (\| v \| _ {\mathcal {W} _ {2}}). \tag {4.21}
$$

In order to prove the existence of the minimizer for the regularization network, we need the following result (see, Proposition 6, page 75, [11]).

Lemma 4.6 [11] Let $V$ be a reflexive Banach space and $F: V \to \mathbb{R} \cup \{+\infty\}$ be convex and lower semi-continuous. If there is an $M \in \mathbb{R}$ such that the set $\{v \in V : F(v) \leq M\}$ is nonempty and bounded, then $F$ attains its minimum on $V$ .

Next, we establish a representative theorem for the regularization network.

Theorem 4.7 (Representer theorem) Assume the same assumptions as in Theorem 4.4. Then the regularization network (4.20) possesses a unique solution $f_{\mathbf{v}_{\mathrm{inf}}}$ where $\mathbf{v}_{\mathrm{inf}} \in \mathcal{W}_2$ satisfies

$$
\mathcal {G} (\mathbf {v} _ {\inf }) \in \left(\left(\Phi_ {1} (\mathbf {x})\right) ^ {\vdash}\right) ^ {\perp}.
$$

Proof: We first prove the uniqueness by contradiction. Assume that there are two different minimizers $f_1, f_2 \in \mathcal{B}_1$ for (4.20). Let $f_3 := \frac{1}{2}(f_1 + f_2)$ . Since $\mathcal{W}_2$ is reflexive, strictly convex and Gâteaux differentiable, $\mathcal{B}_1$ is reflexive, strictly convex and Gâteaux differentiable as well. By the strict convexity of $\mathcal{B}_1$ , we have

$$
\mathcal {E} _ {\mathbf {z}, \lambda} (f _ {3}) = L _ {\mathbf {t}} \Big (\frac {1}{2} f _ {1} (\mathbf {x}) + \frac {1}{2} f _ {2} (\mathbf {x}) \Big) + \lambda \phi \Big (\left\| \frac {1}{2} f _ {1} + \frac {1}{2} f _ {2} \right\| _ {\mathcal {B} _ {1}} \Big) <   L _ {\mathbf {t}} \Big (\frac {1}{2} f _ {1} (\mathbf {x}) + \frac {1}{2} f _ {2} (\mathbf {x}) \Big) + \lambda \phi \Big (\frac {\| f _ {1} \| _ {\mathcal {B} _ {1}}}{2} + \frac {\| f _ {2} \| _ {\mathcal {B} _ {1}}}{2} \Big).
$$

By assumptions on $L_{\mathbf{t}}$ and $\phi$ , it follows that

$$
\mathcal {E} _ {\mathbf {z}, \lambda} (f _ {3}) <   \frac {1}{2} L _ {\mathbf {t}} (f _ {1} (\mathbf {x})) + \frac {1}{2} L _ {\mathbf {t}} (f _ {2} (\mathbf {x})) + \frac {\lambda}{2} \phi (\| f _ {1} \| _ {\mathcal {B} _ {1}}) + \frac {\lambda}{2} \phi (\| f _ {2} \| _ {\mathcal {B} _ {1}}) = \frac {1}{2} \mathcal {E} _ {\mathbf {z}, \lambda} (f _ {1}) + \frac {1}{2} \mathcal {E} _ {\mathbf {z}, \lambda} (f _ {2}) = \mathcal {E} _ {\mathbf {z}, \lambda} (f _ {1}),
$$

contradicting that $f_{1}$ is a minimizer.

Next, we shall show the existence. If $f \in \mathcal{B}_1$ satisfies $\| f \|_{\mathcal{B}_1} > \phi^{-1} \left( \frac{\mathcal{E}_{\mathbf{z}, \lambda}(0)}{\lambda} \right)$ then

$$
\mathcal {E} _ {\mathbf {z}, \lambda} (f) \geq \lambda \phi (\| f \| _ {\mathcal {B} _ {1}}) > \mathcal {E} _ {\mathbf {z}, \lambda} (0).
$$

Thus,

$$
\inf  _ {f \in \mathcal {B} _ {1}} \mathcal {E} _ {\mathbf {z}, \lambda} (f) = \inf  _ {f \in E} \mathcal {E} _ {\mathbf {z}, \lambda} (f), \text {w h e r e} E := \left\{f \in \mathcal {B} _ {1}: \| f \| _ {\mathcal {B} _ {1}} \leq \phi^ {- 1} \left(\frac {\mathcal {E} _ {\mathbf {z} , \lambda} (0)}{\lambda}\right) \right\}.
$$

Clearly, $E$ is nonempty and bounded in the reflexive Banach space $\mathcal{B}_1$ . Observe that $\mathcal{E}_{\mathbf{z},\lambda}$ is convex and continuous on $\mathcal{B}_1$ . By Lemma 4.6, $\mathcal{E}_{\mathbf{z},\lambda}$ attains its minimum on $\mathcal{B}_1$ .

Finally, suppose that $f_{v} = \langle \Phi_{1}(\cdot), v \rangle_{\mathcal{W}_{1} \times \mathcal{W}_{2}} \in \mathcal{B}_{1}$ is the minimizer for (4.20). We set

$$
D := \left\{\left(x _ {j}, f _ {v} \left(x _ {j}\right)\right): j \in \mathbb {N} _ {m} \right\}.
$$

By Theorem 4.4, there exists a unique solution $v_{\mathrm{inf}} \in \mathcal{W}_2$ for the minimal norm interpolation (4.15) with the samples $D$ , and it satisfies (4.19). It follows that $f_{v_{\mathrm{inf}}} = \langle \Phi_1(\cdot), v_{\mathrm{inf}} \rangle_{\mathcal{W}_1 \times \mathcal{W}_2}$ interpolates the sample data $D$ and for all $v \in \mathcal{W}_2$

$$
\| v _ {\inf } \| \mathcal {W} _ {2} \leq \| v \| \mathcal {W} _ {2}.
$$

Thus, $f_{v_{\mathrm{inf}}}(\mathbf{x}) = f_v(\mathbf{x})$ and

$$
\left\| f _ {v _ {\inf }} \right\| _ {\mathcal {B} _ {1}} = \left\| v _ {\inf } \right\| _ {\mathcal {W} _ {2}} \leq \left\| v \right\| _ {\mathcal {W} _ {2}} = \left\| f _ {v} \right\| _ {\mathcal {B} _ {1}}.
$$

As $\phi$ is increasing, we get

$$
\mathcal {E} _ {\mathbf {z}, \lambda} (f _ {v _ {\mathrm {i n f}}}) = L _ {\mathbf {t}} (f _ {v _ {\mathrm {i n f}}} (\mathbf {x}) + \lambda \phi (\| f _ {v _ {\mathrm {i n f}}} \| _ {\mathcal {B} _ {1}}) \leq L _ {\mathbf {t}} (f _ {v} (\mathbf {x})) + \lambda \phi (\| f _ {v} \| _ {\mathcal {B} _ {1}}) = \mathcal {E} _ {\mathbf {z}, \lambda} (f _ {v}).
$$

By uniqueness of minimizer, $f_{v_{\mathrm{inf}}} = f_v$ . As a consequence, $\mathbf{v}_{\mathrm{inf}}$ defined by (4.21) satisfies (4.19). The proof is complete.

When $\mathcal{W}_2 = \mathcal{W}_1^*$ , the above result can be simplified.

Corollary 4.8 Assume the same assumptions as in Theorem 4.4. If, in addition, $\mathcal{W}_2 = \mathcal{W}_1^*$ then the regularization network (4.20) possesses a unique solution $f_{\mathbf{v}_{\mathrm{inf}}}$ where $\mathbf{v}_{\mathrm{inf}} \in \mathcal{W}_2$ satisfies

$$
\mathcal {G} (\mathbf {v} _ {\mathrm {i n f}}) \in \operatorname {s p a n} \Phi_ {1} (\mathbf {x}).
$$

The above result covers representative theorems in existing RKBSs [43, 46, 48]. Especially, it covers the classical representative theorem for regularization networks in an RKHS.

# References

[1] A. Argyriou, C. A. Micchelli, and M. Pontil, On spectral learning, J. Mach. Learn. Res. 11 (2010), 935-953.   
[2] N. Aronszajn, Theory of reproducing kernels, Trans. Amer. Math. Soc. 68 (1950), 337-404.   
[3] M. Buhmann, *Radial Basis Functions: Theory and Implementations*, Cambridge Monographs on Applied and Computational Mathematics, 12, Cambridge University Press, Cambridge, 2003.   
[4] E. J. Candés, J. Romberg, and T. Tao, Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information, IEEE Trans. Inform. Theory 52 (2006), 489-509.   
[5] J. G. Christensen, Sampling in reproducing kernel Banach spaces on Lie groups, J. Approx. Theory 164 (2012), 179-203.   
[6] D. Cox and F. O'Sullivan, Asymptotic analysis of penalized likelihood and related estimators, Ann. Statist. 18 (1990), 1676-1695.   
[7] F. Cucker and S. Smale, On the mathematical foundations of learning, Bull. Amer. Math. Soc. 39 (2002), 1-49.   
[8] F. Cucker and D. X. Zhou, Learning Theory: An Approximation Theory Viewpoint, Cambridge Monographs on Applied and Computational Mathematics, 24, Cambridge University Press, Cambridge, 2007.   
[9] B. Dastourian and M. Janfada, Frames for operators in Banach spaces via semi-inner products, Int. J. Wavelets Multiresolut. Inf. Process. 14 (2016), no. 3, 1650011, 17 pp.   
[10] R. Der and D. Lee, Large-margin classification in Banach spaces, JMLR Workshop and Conference Proceedings 2 (2007), AISTATS: 91-98.   
[11] I. Ekeland and T. Turnbull, Infinite-dimensional Optimization and Convexity, University of Chicago Press, Chicago, IL, 1983.   
[12] M. Fabian, P. Habala, P. Hajek et al., Functional Analysis and Infinite-Dimensional Geometry, Springer, New York, 2001.   
[13] G. E. Fasshauer, F. J. Hickernell, and Q. Ye, Solving support vector machines in reproducing kernel Banach spaces with positive definite functions, Appl. Comput. Harmon. Anal. 38 (2015), 115-139.   
[14] A. G. García and P. Alberto, Sampling in reproducing kernel Banach spaces, Mediterr. J. Math. 10 (2013), 1401-1417.   
[15] A. G. García, M. A. Hernández-Medina, and M. J. Muñnoz-Bouzo, The Kramer sampling theorem revisited, Acta Appl. Math. 133 (2014), 87-111.   
[16] P. G. Georgiev, L. Sánchez-González, and P. M. Pardalos, Construction of pairs of reproducing kernel Banach spaces, Constructive Nonsmooth Analysis and Related Topics 87 (2014), 39-57.

[17] J. R. Giles, Classes of semi-inner-product spaces, Trans. Amer. Math. Soc. 129 (1967), 436-446.   
[18] D. Han, M. Z. Nashed, and Q. Sun, Sampling expansions in reproducing kernel Hilbert and Banach spaces, Numer. Funct. Anal. Optim. 30 (2009), 971-987.   
[19] T. Hastie, R. Tibshirani, and J. Friedman, The Elements of Statistical Learning: Data Mining, Inference and Prediction, Second edition, Springer-Verlag, New York, 2009.   
[20] R. C. James, Orthogonality and linear functionals in normed linear spaces, Trans. Amer. Math. Soc. 61 (1947), 265-292.   
[21] G. Kimeldorf and G. Wahba, Some results on Tchebycheffian spline functions, J. Math. Anal. Appl. 33 (1971), 82-95.   
[22] G. Lumer, Semi-inner-product spaces, Trans. Amer. Math. Soc. 100 (1961), 29-43.   
[23] G. Lumer, On the isometries of reflexive Orlicz spaces, Ann. Inst. Fourier (Grenoble) 13 (1963), 99-109.   
[24] R. E. Megginson, An Introduction to Banach Space Theory, Springer-Verlag, New York, 1998.   
[25] C. A. Micchelli and M. Pontil, A function representation for learning in Banach spaces, Proceeding of the 17th Annual Conference on Learning Theory, pp. 255-269, Lecture Notes in Computer Science 3120, Springer, Berlin, 2004.   
[26] C. A. Micchelli and M. Pontil, Feature space perspectives for learning the kernel, Mach. Learn. 66 (2007), 297-319.   
[27] M. Z. Nashed and Q. Sun, Sampling and reconstruction of signals in a reproducing kernel subspace of $L^p(\mathbb{R}^d)$ , J. Funct. Anal. 258 (2010), 2422-2452.   
[28] M. Z. Nashed, Q. Sun, and J. Xian, Convolution sampling and reconstruction of signals in a reproducing kernel subspace, Proc. Amer. Math. Soc. 141 (2013), 1995-2007.   
[29] M. M. Rao and Z. D. Ren, Theory of Orlicz Spaces, Marcel Dekker, New York, 1991.   
[30] M. Rao and Z. Ren, Applications of Orlicz Spaces, Monographs and Textbooks in Pure and Applied Mathematics, 250, Marcel Dekker, Inc., New York, 2002.   
[31] W. Rudin, Real and Complex Analysis, Third edition, McGraw-Hill Book Co., New York, 1987.   
[32] B. Schölkopf, R. Herbrich, and A. J. Smola, A generalized representer theorem, Proceeding of the Fourteenth Annual Conference on Computational Learning Theory and the Fifth European Conference on Computational Learning Theory, pp. 416-426, Springer-Verlag, London, UK, 2001.   
[33] B. Schölkopf and A. J. Smola, Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond, MIT Press, Cambridge, Massachusetts, 2002.   
[34] L. Shi, Y.-L. Feng, and D.-X. Zhou, Concentration estimates for learning with $\ell^1$ -regularizer and data dependent hypothesis spaces, Appl. Comput. Harmon. Anal. 31 (2011), 286-302.   
[35] B. Sriperumbudur, K. Fukumizu, and G. Lanckriet, Learning in Hilbert vs. Banach spaces: A measure embedding viewpoint, Adv. Neural Inf. Process. Syst. 24 (2011), 1773-1781.   
[36] I. Steinwart and A. Christmann, Support Vector Machines, Springer-Verlag, New York, 2008.   
[37] G. Song and H. Zhang, Reproducing kernel Banach spaces with the $\ell^1$ norm II: Error analysis for regularized least square regression, Neural Comput. 23 (2011), 2713-2729.   
[38] G. Song, H. Zhang, and F. J. Hickernell, Reproducing kernel Banach spaces with the $\ell^1$ norm, Appl. Comput. Harmon. Anal. 34 (2013), 96-116.   
[39] R. Tibshirani, Regression shrinkage and selection via the lasso, J. Roy. Statist. Soc. Ser. B 58 (1996), 267-288.

[40] H. Tong, D.-R. Chen, and F. Yang, Least square regression with $\ell^p$ -coefficient regularization, Neural Comput. 22 (2010), 3221-3235.   
[41] H. Wendland, Scattered Data Approximation, Cambridge Monographs on Applied and Computational Mathematics 17, Cambridge University Press, Cambridge, 2005.   
[42] Q. W. Xiao and D. X. Zhou, Learning by nonsymmetric kernels with data dependent spaces and $\ell_1$ -regularizer, Taiwanese J. Math. 14 (2010), 1821-1836.   
[43] Y. Xu and Q. Ye, Generalized Mercer kernels and reproducing kernel Banach spaces, Mem. Am. Math. Soc. 258 (2019), no. 1243, 122 pp.   
[44] Y. Xu and H. Zhang, Refinable kernels, J. Mach. Learn. Res. 8 (2007), 2083-2120.   
[45] Q. Ye, Support vector machines in reproducing kernel Hilbert spaces versus Banach spaces, Approximation Theory XIV: San Antonio 2013, 377-395.   
[46] H. Zhang, Y. Xu, and J. Zhang, Reproducing kernel Banach spaces for machine learning, *J. Mach. Learn.* Res. **10** (2009), 2741-2775.   
[47] H. Zhang and J. Zhang, Frames, Riesz bases, and sampling expansions in Banach spaces via semi-inner products, Appl. Comput. Harmon. Anal. 31 (2011), 1-25.   
[48] H. Zhang and J. Zhang, Regularized learning in Banach spaces as an optimization problem: representer theorems, J. Global Optim. 54 (2012), 235-250.   
[49] H. Zhang and J. Zhang, Vector-valued reproducing kernel Banach spaces with applications to multi-task learning, J. Complexity 29 (2013), 195-215.   
[50] H. Zhang and L. Zhao, On the inclusion relation of reproducing kernel Hilbert spaces, Anal. Appl. (Singap.) 11 (2013), no. 2, 1350014, 31 pp.   
[51] J. Zhang and H. Zhang, Categorization Based on Similarity and Features: The Reproducing Kernel Banach Space Approach. In W. Batchelder, H. Colonius, E.N. Dzhafarov, and J. Myung (Eds.) New Handbook of Mathematical Psychology, Volume 2, Springer, 2018.