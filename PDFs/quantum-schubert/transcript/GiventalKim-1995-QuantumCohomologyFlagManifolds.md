# QUANTUM COHOMOLOGY OF FLAG MANIFOLDS AND TODA LATTICES

Alexander GIVENTAL ∗

UC Berkeley

Bumsig KIM

UC Berkeley

December 12, 1993

# Abstract

We discuss relations of Vafa’s quantum cohomology with Floer’s homology theory, introduce equivariant quantum cohomology, formulate some conjectures about its general properties and, on the basis of these conjectures, compute quantum cohomology algebras of the flag manifolds. The answer turns out to coincide with the algebra of regular functions on an invariant lagrangian variety of a Toda lattice.

# 1 Introduction

Quantum cohomology of compact complex Kahler manifolds was introduced by C.Vafa [V] in connection with the theory of mirror manifolds.

By Vafa’s definition, the quantum cohomology $Q H ^ { * } ( X )$ of a compact Kahler manifold $X$ is a certain deformation of the cup-product multiplication in the ordinary cohomology of $X$ . Let $a , b , c$ be three cycles in $X$ representing three given cohomology classes by Poincare duality. One defines the quantum cup-product $a * b$ by specifying its intersection indices with all $c$ . Namely

$$
\langle a * b, c \rangle = \sum \quad \pm q ^ {d}.
$$

degree $d$ discrete holomorphic maps: (CP 1,0,1,∞)→(X,a,b,c)

In other words, the intersection index takes in account rational parametrized curves in $X$ with the three marked points — images of 0,1 and $\infty$ — on the three cycles $a$ , $b$ and $c$ respectively.

This definition needs some explanations.

1. First of all, a rational curve contributes to the intersection index only if it is “discrete” which means, by definition, that

$$
c (d) + \dim X = \operatorname {c o d i m} a + \operatorname {c o d i m} b + \operatorname {c o d i m} c
$$

where $c ( d )$ is the first Chern class $c$ of (the tangent bundle to) $X$ evaluated on the homology class $d$ of the curve, $\mathrm { d i m } X$ is the complex dimension of $X$ , and codim on the RHS stand for

degrees of the cohomology classes represented by $a , b , c$ , also counted in complex units (so that a real hypersurface has codimension $1 / 2$ ). The meaning of the LHS is the dimension of the parameter space of such curves predicted by the classical Riemann–Roch formula, while the RHS is the number of constraints imposed at 0,1 and $\infty$ . Thus in the situation of “general position”, when the Riemann–Roch prediction is correct (and under some further transversality assumptions) the “discrete” curves can really be treated as isolated intersections and contribute to $\langle a * b , c \rangle$ by $\pm q ^ { d }$ each.

2. Here “ $\boldsymbol q ^ { d } ^ { * }$ is, formally speaking, the homology class of the rational curve and therefore the intersection index as a whole is an element of a group ring of the lattice $H _ { 2 } ( X , \mathbb { Z } ) \cap H _ { 1 , 1 } ( X , \mathbb { C } )$ . The notation $q ^ { d }$ is chosen simply to “tame” the group ring by means of coordinates on the lattice. If we choose a basis of Kahler forms $\omega _ { 1 } , . . . , \omega _ { k }$ in $H ^ { 2 } ( X , \mathbb { Z } ) \cap H ^ { 1 , 1 } ( X , \mathbb { C } )$ and express the homology class of a rational curve $S$ by the string $d = ( d _ { 1 } , . . . , d _ { k } )$ of its coordinates in the dual basis (so that $\begin{array} { r } { d _ { i } = \int _ { S } \omega _ { i } \ge 0 , } \end{array}$ ) then the element $q ^ { d }$ of the group ring can be identified with the monomial qd11 ...qdkk $q _ { 1 } ^ { d _ { 1 } } . . . q _ { k } ^ { d _ { k } }$ of the formal variables $( q _ { 1 } , . . . , q _ { k } )$ , and the intersection index $\langle a * b , c \rangle$ becomes a formal series in $q$ .   
3. The constant term of this series counts constant rational curves with the marked points in the cycles $a , b , c$ , i. e. it counts ordinary intersection points. The signs $\pm$ should be chosen in such a way that this term is the ordinary triple intersection index $\langle a \cap b , c \rangle$ of the cycles.   
4. About the higher degree terms (they are called “instanton corrections” to the classical intersection index) we only tell here that their signs $\pm$ are defined to be pluses only in the case when the cycles $a , b , c$ are complex submanifolds in $X$ (while the general case will be briefly discussed in 2.3). In any way, the instanton corrections provide a $q$ -deformation of the classical triple intersection index.   
5. The double intersection index $\langle a , c \rangle$ of any two cycles, by definition, coincides with the ordinary non-degenerate Poincare pairing, and one can recover the quantum cup-product $a * b$ from the triple pairings as an element of $H ^ { * } ( X , \mathbb { Z } [ [ q ] ] )$ .

The above construction of the quantum cohomology ring is lacking of many ingredients which could possibly make it mathematically rigorous, and we will touch some mathematical aspects of the problem in the next section. On the other hand, Vafa’s construction is strongly supported by general ideology of Conformal Topological Field Theory and provides mathematicians with a bunch of interrelated conjectures. In particular, according to these conjectures, the quantum cup-product

• can be defined rigorously;   
• is associative and skew-commutative;   
• is a $q$ -deformation of the classical cup-product;   
• respects the usual grading in the cohomology provided that one assigns the following nontrivial degrees to the parameters of the deformation: $\deg q ^ { d } = c ( d )$ (in complex units).

In this paper, we do not have any intention to justify these properties mathematically. Instead, our objective is to compute the quantum cohomology algebras of the classical flag manifolds in the assumption that their properties expected on the basis of Topological Field Theory are valid. Therefore the results obtained in this way, while “physical theorems”, have the status of mathematical conjectures, or better to say conditional theorems contingent to the general conjectures about quantum cohomology of Kahler manifolds. With this reservation in mind we formulate below the results of our computation as theorems.

Let $F _ { n + 1 }$ denote the manifold of complete flags

$$
\mathbb {C} ^ {1} \subset \ldots \subset \mathbb {C} ^ {n}
$$

in $\mathbb { C } ^ { n + 1 }$ . The cohomology algebra $H ^ { * } ( F _ { n + 1 } )$ is known to be canonically isomorphic to the quotient of the polynomial algebra $\mathbb { Z } [ u _ { 0 } , . . . , u _ { n } ]$ in $n + 1$ indeterminates by the ideal generated by the elementary symmetric polynomials $\sigma _ { 1 } ( u ) , . . . , \sigma _ { n + 1 } ( u )$ . The generators $u _ { i }$ are in fact the 1-st Chern classes of the tautological line bundles over the flag manifold with the fiber $\mathbb { C } ^ { \ i + 1 } / \mathbb { C } ^ { \ i }$ . They are constrained by $u _ { 0 } + . . . + u _ { n } = 0$ and can be expressed through another basis as $u _ { i } = p _ { i } - p _ { i + 1 }$ . The generators $( p _ { 1 } , . . . , p _ { n } )$ are 1-st Chern classes of the determinant line bundles with the fiber $\Lambda ^ { * } \mathbb { C } ^ { i }$ over a point $\mathbb { C } ^ { 1 } \subset \ldots \subset \mathbb { C } ^ { n }$ of the flag manifold. These determinant line bundles are non-negative and the classes $p _ { i }$ span the edges of the (simplicial) Kahler cone in the 2-nd cohomology of $F _ { n + 1 }$ . For a rational curve $S \subset F _ { n + 1 }$ we define its degree $d = ( d _ { 1 } , . . . , d _ { n } )$ with respect the coordinates $p _ { i }$ as $d _ { i } = \langle p _ { i } , [ S ] \rangle \geq 0$ . Now the homology class of the curve is represented by the monomial $q ^ { d } = q _ { 1 } ^ { d _ { 1 } } . . . q _ { n } ^ { d _ { n } }$ .

In order to describe the quantum cohomology algebra $Q H ^ { * } ( F _ { n + 1 } )$ it suffices therefore to exhibit the corresponding deformation of elementary symmetric polynomials of $u _ { 0 } , . . . , u _ { n }$ by the parameters $q _ { 1 } , . . . , q _ { n }$ . Notice that while the degrees of $u _ { i }$ are equal 1, the degrees of all $q _ { i }$ are equal 2 (since the 1-st Chern class of the flag manifold is $c = 2 ( p _ { 1 } + . . . + p _ { n } ) )$ , and the deformation should be homogeneous with respect to this grading.

Consider the diagonal matrix with $u _ { 0 } , . . . , u _ { n }$ on the diagonal. Then the coefficients of its characteristic polynomial are elementary symmetric functions of $u$ .

Consider another $( n + 1 ) \times ( n + 1 )$ matrix, denoted $A _ { n }$ ,

$$
A _ {n} = \left[ \begin{array}{c c c c c} u _ {0} & q _ {1} & 0 & \dots & 0 \\ - 1 & u _ {1} & q _ {2} & \dots & 0 \\ 0 & - 1 & u _ {3} & \dots & 0 \\ & . & . & . \\ 0 & \dots & 0 & - 1 & u _ {n} \end{array} \right]
$$

with $u _ { i }$ on the diagonal, $q _ { i }$ — right above, and $^ { - 1 }$ ’s — right under the diagonal. Then the coefficients of its characteristic polynomial are the deformations in question of the elementary symmetric functions:

Theorem 1. The quantum cohomology algebra $Q H ^ { * } ( F _ { n + 1 } )$ of the flag manifold is canonically isomorphic to the quotient of the polynomial algebra $\mathbb { Z } [ u _ { 0 } , . . . , u _ { n } , q _ { 1 } , . . . , q _ { n } ]$ by the ideal generated by coefficients of the characteristic polynomial of the matrix $A _ { n }$ .

Specialists on complete integrable systems will recognize in this answer something very familiar: in fact the coefficients of $\operatorname* { d e t } ( A _ { n } + \lambda )$ are conservation laws of a Toda lattice.

Namely, introduce “configuration” variables $( x _ { 0 } , . . . , x _ { n } )$ of $n + 1$ consequtive unit masses on the line with $q _ { i } = \exp ( x _ { i } - x _ { i - 1 } )$ in the role of potential energy of neighbors. Then

$$
\frac {1}{2} \operatorname {t r} (A _ {n} ^ {2}) = \frac {1}{2} \sum u _ {i} ^ {2} - \sum e ^ {x _ {i} - x _ {i - 1}}
$$

is the Hamiltonian of the classical Toda lattice (with incorrect sign of the potential however), and $\operatorname { t r } ( A _ { n } ^ { \ i } ) , \ i = 1 , . . . , n + 1$ , is the complete set of commuting first integrals.

Corollary.The quantum cohomology algebra of the flag manifold $F _ { n + 1 }$ is isomorphic to the algebra of functions on the common zero level of the first integrals of the classical Toda lattice.

Making comments on the theme “How much surprising is the result?” we should say that one might not expect quantum cohomology of flag manifolds to have no connections with other known objects attributed to flag manifolds. Moreover, Topological Field Theory predicts deep relations (see for instance [D],[W]) of moduli spaces of rational curves in Kahler manifolds with hierarchies of integrable systems. Moreover, Toda lattices have already occurred [CV] — in a “less surprising” manner — in some dynamical problem related to quantum cohomology of projective spaces. Nevertheless the authors should confess they did not foresee this particular relation when started the computation, and they do not know now how the answer can be predicted. However some partial explanations should be given right away.

First of all, it can be viewed accidental that the relations in quantum cohomology of flag manifolds Poisson-commute. What is not accidental at all is that they Poisson-commute modulo the relations themselves. Indeed, according to general theory (see 2.4) quantum cohomology algebra of a Kahler manifold in some sense always is (or at least related to) the algebra of functions on some lagrangian variety in the cotangent bundle of some torus. The parameters $q _ { i }$ of the quantum deformation are multiplicative coordinates on the torus. In the case of $F _ { n + 1 }$ the cotangent bundle provided with the coordinates $q _ { 1 } , . . . , q _ { n } \neq 0 , p _ { 1 } , . . . , p _ { n }$ (in above notations) has the canonical symplectic form

$$
d p _ {1} \wedge \frac {d q _ {1}}{q _ {1}} + \ldots + d p _ {n} \wedge \frac {d q _ {n}}{q _ {n}},
$$

and the algebra $Q H ^ { * } ( F _ { n + 1 } , \mathbb { C } )$ must be the algebra of regular functions on some quasi - homogeneous lagrangian subvariety $L$ . In view of the group-theoretic nature of Toda lattices [R], our theorem leads to the following geometrical description of $L$ .

Let $G = S L _ { n + 1 } ( \mathbb { C } )$ , $N _ { + }$ and $N _ { - }$ be its strictly lower- and upper-triangular subgroups. Make $N _ { + }$ and $N _ { - }$ act respectively by left and right translations on the cotangent bundle $T ^ { * } G$ of the group and consider the momentum map $J : T ^ { * } G \to L i e ^ { * } ( N _ { + } \times N _ { - } )$ of the action. The trace inner product $\mathrm { t r } A B$ on the matrix algebra identifies the dual of the Lie algebra of $N _ { + } \times N _ { - }$ with the quotient of the space of all square $( n + 1 )$ -matrices by the subspace of all diagonal matrices. Pick

the value of the momentum map as specified by the matrix

$$
P = \left[ \begin{array}{c c c c c} * & 1 & 0 & 0 & \ldots \\ 1 & * & 1 & 0 & \ldots \\ 0 & 1 & * & 1 & \ldots \\ & . & . & . \\ \ldots & 0 & 0 & 1 & * \end{array} \right]
$$

( $0$ ’s everywhere except 1’s right above and under the diagonal) and make the symplectic reduction on this level of the momentum map. The reduced phase space

$$
M _ {P} = T ^ {*} G / / _ {P} \left(N _ {+} \times N _ {-}\right) = J ^ {- 1} (P) / \left(N _ {+} \times N _ {-}\right)
$$

can be naturally identified with the cotangent bundle of the maximal torus in $G$ . Now, consider the cone $C \subset L i e G$ of all nilpotent traceless matrices. The product

$$
C \times G \subset (L i e G) \times G = T ^ {*} G
$$

is a bi-invariant involutive subvariety. Its symplectic reduction

$$
L = \left[ J ^ {- 1} (P) \cap (C \times G) \right] / \left(N _ {+} \times N _ {-}\right) \subset M _ {P}
$$

is in fact a lagrangian subvariety in the reduced phase space.

Corollary. The quantum cohomology algebra $Q H ^ { * } ( F _ { n + 1 } , \mathbb { C } )$ is isomorphic to the algebra of regular functions on the lagrangian variety $L$ .

We should augment this corollary with an open question: Why the quantum cohomology algebra of the flag manifold $G / B _ { - }$ is isomorphic to the algebra of regular functions on the lagrangian variety $L$ ? We would expect that a natural answer to this question will come along with a better understanding of the general mirror symmetry phenomena (cf. [G3]).

The second argument that partially explains the theorem comes from its proof. Our computation of quantum cohomology of flag manifolds is based in fact on induction on $n$ . It turns out however that the induction assumption that quantum cohomology of $F _ { m + 1 }$ with $m < n$ is known, is insufficient for our purpose. What we really need is an equivariant version of quantum cohomology of flag manifolds considered as homogeneous spaces of unitary groups. Similarly to ordinary equivariant cohomology of a $U$ -space $X$ , quantum equivariant cohomology can be defined (with similar reservations) as a skew-commutative associative algebra over the ring of characteristic classes of the compact Lie group $U$ .

In the case of $U ~ = ~ U _ { n + 1 }$ (acting on the flag manifold $F _ { n + 1 }$ ), we deal with the algebra $\mathbb { Z } [ c _ { 1 } , . . . , c _ { n + 1 } ]$ of usual Chern classes, and the ordinary equivariant cohomology of the flag manifold is known to coincide with the polynomial algebra $\mathbb { Z } [ u _ { 0 } , . . . , u _ { n } ]$ of characteristic classes of the maximal torus $T ^ { n + 1 } \subset U _ { n + 1 }$ considered however as a module over the subalgebra of Chern classes

$$
c _ {i} = \sigma_ {i} (u _ {0}, \dots , u _ {n}), i = 1, \dots , n + 1
$$

— elementary symmetric functions of $u$ .

In the same manner as $H ^ { * } ( F _ { n + 1 } )$ is obtained from the equivariant cohomology $H _ { U _ { n + 1 } } ^ { * } ( F _ { n + 1 } )$ by specialization $c _ { 1 } = . . . = c _ { n + 1 } = 0$ , we deduce our theorem on quantum cohomology of flag manifolds from a more general result describing their equivariant quantum cohomology.

Theorem 2. The equivariant quantum cohomology algebra $Q H _ { U _ { n + 1 } } ^ { * } ( F _ { n + 1 } )$ is canonically isomorphic to the quotient of the polynomial algebra

$$
\mathbb {Z} [ u _ {0}, \dots , u _ {n}, q _ {1}, \dots , q _ {n}, c _ {1}, \dots , c _ {n + 1} ]
$$

by the ideal of relations obtained by equating the coefficients of the following polynomials in $\lambda$ :

$$
\det  (A _ {n} + \lambda) = \lambda^ {n + 1} + c _ {1} \lambda^ {n} + \ldots + c _ {n} \lambda + c _ {n + 1}.
$$

In other words, it is the free polynomial algebra in $u$ and $q$ but the subalgebra of Chern classes, instead of symmetric functions of $u$ , consists of their “quantum deformations” from the previous theorem — first integrals of the Toda lattice.

Now we can figure out, why one might a priori expect quantum cohomology of flag manifolds to be related with at least some integrable system.

According to our general theory (see 3.8), equivariant quantum cohomology of a compact Kahler $U$ -manifold $X$ is an algebra of functions on a lagrangian subvariety $\mathcal { L }$ in a Poisson manifold with $U$ -characteristic classes in the role of Casimir functions. Poisson structure lives in the space with coordinates (q1, ..., qn, p1, ..., pn, $c _ { 1 } , . . . , c _ { n + 1 }$ ) and is given by the formula

$$
q _ {1} \frac {\partial}{\partial p _ {1}} \wedge \frac {\partial}{\partial q _ {1}} + \dots + q _ {n} \frac {\partial}{\partial p _ {n}} \wedge \frac {\partial}{\partial q _ {n}}
$$

so that the symplectic leaves ${ \vec { c } } = c o n s t$ are in fact all isomorphic to the cotangent bunle of the $q$ -torus described above.

Our point now is that although equating Chern classes to non-zero constants makes little “cohomological” sense, the ideal of $\mathcal { L }$ is a priori a Poisson ideal, and therefore intersections of $\mathcal { L }$ with the symplectic leaves can be interpreted as a $\vec { c }$ -parametric family of lagrangian submanifolds in the same symplectic space — the cotangent bundle of the torus.

Moreover, since the ideal of relations is generated by quasi-homogeneous $q$ -deformations of the classical relations $c _ { i } = \sigma _ { i } ( u )$ , equations of the lagrangian submanifolds have the following triangular form

$$
c _ {i} = C _ {i} (u, q, c _ {1}, \dots , c _ {i - 1}), i = 1, \dots , n + 1
$$

and can be resolved with respect to $c _ { i }$ as $c _ { i } = c _ { i } ( u , q )$ .

This means that the lagrangian submanifolds fit nicely into the phase space as leaves of a lagrangian foliation — common levels of the functions $c _ { i } ( u , q ) , i = 1 , . . . , n + 1$ , which are therefore in involution, — and the lagrangian variety $L$ is a singular zero leaf of this foliation.

Our description of quantum (equivariant) cohomology of flag manifolds would be incomplete without a formula for the intersection pairing (see 3.4)

$$
\langle \cdot , \cdot \rangle : Q H _ {U _ {n + 1}} ^ {*} (F _ {n + 1}, \mathbb {C}) \otimes_ {\mathbb {C} [ c ]} Q H _ {U _ {n + 1}} ^ {*} (F _ {n + 1}, \mathbb {C}) \to \mathbb {C} [ c ].
$$

Denote $\Sigma _ { i } ( u _ { 0 } , . . . , u _ { n } , q _ { 1 } , . . . , q _ { n } )$ , $i = 1 , . . . , n + 1$ , the quantum deformation of elementary symmetric functions $\sigma _ { i } ( u )$ from Theorem 1 (i. e. the first integrals of the Toda lattice). Let $\varphi , \psi \in \mathbb { C } [ u , q , c ]$ be two polynomials considered as representatives of cohomology classes from $H _ { U _ { n + 1 } } ^ { * } ( F _ { n + 1 } )$ .

# Theorem 3.

$$
\langle [ \varphi ], [ \psi ] \rangle (c, q) = \frac {1}{(2 \pi i) ^ {n + 1}} \int \frac {\varphi (u , q , c) \psi (u , q , c) d u _ {0} \wedge \ldots \wedge d u _ {n}}{(\Sigma_ {1} (u , q) - c _ {1}) . . . (\Sigma_ {n + 1} (u , q) - c _ {n + 1})}.
$$

The integral here can be replaced by the total sum of $( n + 1 )$ ! residues in the $u$ -space. In order to obtain the intersection pairing in non-equivariant cohomology $Q H ^ { * } ( F _ { n } )$ it suffices to put $c _ { 1 } = . . . = c _ { n + 1 } = 0$ in this formula.

Consider the basis $p _ { 1 } , . . . , p _ { n }$ of non-negative $( 1 , 1 )$ -classes on $F _ { n + 1 }$ , $u _ { i } = p _ { i } - p _ { i + 1 }$ . Then $( z , p ) = z _ { 1 } p _ { 1 } + . . . + z _ { n } p _ { n }$ with $z _ { i } > 0$ is represented by a Kahler form, and $\exp ( z , p )$ can be considered as a non-homogeneous differential form whose degree $( k , k )$ term measures $k$ -dimensional Kahler volume. The corresponding quantum generating volume function (see 2.3):

$$
V (z, q) = \frac {1}{(2 \pi i) ^ {n}} \int \frac {\exp (z , p) d p _ {1} \wedge \ldots \wedge d p _ {n}}{\Pi_ {j = 1} ^ {n} (\Sigma_ {j + 1} (u (p) , q))}
$$

has the geometrical meaning of the total Kahler volume of the ‘ $q$ -weighted’ space

$$
\mathcal {M} = \cup_ {d} q ^ {d} \mathcal {M} _ {d}
$$

of holomorphic maps $\mathbb { C } P ^ { 1 } \to F _ { n + 1 }$ of all degrees $d$ . The volume is computed in fact with respect to the Kahler form induced by $( z , p )$ on the loop space $L F _ { n + 1 }$ where $\mathcal { M }$ can be naturally embedded. Combining our conjectures about general properties of quantum cohomology with the ‘conditional’ Theorem 3 we come to the following ‘unconditional’ prediction.

Conjecture. Kahler volume of the space of parametrized rational curves of degree $d \digamma =$ $( d _ { 1 } , . . . , d _ { n } )$ with respect to the Kahler form with periods $z _ { 1 } , . . . , z _ { n }$ on the flag manifold $F _ { n + 1 } ^ { \prime }$ equals

$$
\mathrm {V o l} _ {z} (\mathcal {M} _ {d}) = \frac {1}{d _ {1} ! . . . d _ {n} !} (\frac {\partial}{\partial q _ {1}}) ^ {d _ {1}}... (\frac {\partial}{\partial q _ {n}}) ^ {d _ {n}} | _ {q = 0} V (z, q).
$$

At $d = 0$ this formula reduces to the total volume of the flag manifold itself and coincides with the fundamental anti-invariant of the permutation group. The equivariant analogue $V _ { G } ( z , q , c )$ of the generating volume function at $q = 0$ , $c = \sigma ( x _ { 0 } , . . . , x _ { n } )$ turns into the asymptotic character of irreducible representations of $G = U _ { n + 1 }$ with ‘large highest weights’ proportional to $z$ (it can be found using Duistermaat – Heckmann formula [AB]). It would be interesting to figure out the meaning of such generating volume functions with non-zero $q$ and the role of Toda lattices in representation theory of loop groups. The last question seems to be closely related to the recent paper [FF] on Toda Field Theory.

Structure of this paper. In Section 2 we give a more detailed review of quantum cohomology theory. Although one can find a number of approaches to the general theory in the available

literature (see for instance [W] or a recent preprint [S] where in particular the quantum cohomology of $F _ { 3 }$ has been computed), we hope that our point of view is up to certain extent complementary to them. It also should help to clarify our construction of equivariant quantum cohomology (Section 3) as well as those conjectures about its general properties which we exploit in our inductive proof (Section 4) of the theorems formulated in this Introduction.

Conventions. Throughout this paper, we will assume for convenience that all dimensions are counted in complex units, and — for the sake of simplicity — that all considered compact Kahler manifolds are simply-connected.

Thanks. We would like to express our sincere gratitude to all participants of the seminar on mirror symmetry at the Department of Mathematics at UC Berkeley for their stimulating enthusiasm, and especially to Dmitry Fuchs, Dusa McDuff, Nikolai Reshetikhin, Albert Schwartz, Vera Serganova and Alan Weinstein for numerous instructive discussions.

# 2 Quantum cohomology and Floer homology

The objective of this section is to interpret Vafa’s construction of quantum cohomology of a compact Kahler manifold as Floer homology of its loop space (to be more precise — of the universal covering of the loop space) provided with multiplication induced by composition of loops.

# 2.1 Additive structure

Let $X$ be a compact manifold provided with a complex structure $J$ and a riemannian metric $( \cdot , \cdot )$ compatible with the complex structure in the sense that the differential form $\boldsymbol \omega = ( J \cdot , \cdot )$ is symplectic.

The space $L X$ of contractible (say, smooth) loops $S ^ { 1 } \to X$ inherits from $X$ the same structures:

• the complex structure $\mathcal { I }$ which transforms a tangent vector (= a vector field $t \mapsto v ( t )$ along the loop $t \mapsto \gamma ( t )$ ) to $t \mapsto J ( \gamma ( t ) ) v ( t )$ ;   
• the $\mathcal { I }$ -compatible riemannian and symplectic forms

$$
(v, w) = \oint (v (t), w (t)) d t, \Omega (v, w) = \oint \omega (v (t), w (t)) d t;
$$

and additionally carries

• the action of the reparametrization group $D i f f ( S ^ { 1 } )$ and in particular the circle action generated by the vector field $V : \gamma \mapsto \dot { \gamma }$ on $L X$ ; and

the action functional $\mathcal { A } : L \overset { \sim } { X }  \mathbb { R }$ :

$$
\mathcal {A} (\gamma) = \int_ {D} \varphi^ {*} \omega
$$

which assigns to a loop $\gamma$ the symplectic area of a disk ( $\varphi : D  X : \varphi | _ { S ^ { 1 } = \partial D } = \gamma ,$ ) contracting the loop, and thus is well defined only on the universal covering of $L X$ .

There is a remarkable relation between these structures, namely

1. the circle action is hamiltonian with respect to the symplectic form $\Omega$ and the hamilton function is $\mathcal { A }$ ;   
2. the gradient vector field of the action functional relative to the riemannian metric equals $\mathcal { T V }$ and thus the gradient “flow” consists in analytic continuation of loops from the unit real circle $S ^ { 1 } \subset \mathbb { C } - 0$ to its neighborhood in the complex circle.

By definition, Floer homology $F H _ { * } ( X )$ is Morse-theoretic homology of the loop space $L X$ constructed by means of the “Morse function” $\mathcal { A }$ in the spirit of Witten’s approach [W2] to the Morse theory, i. e. using bounded gradient trajectories joining critical points.

historically Floer homology has been introduced [F1] in order to prove Arnold’s symplectic fixed point conjecture and deals with Morse theory of action functionals perturbed by a hamiltonian term. However the homology itself is simpler to compute for the unperturbed action functional $\mathcal { A }$ .

In fact the functional $\mathcal { A }$ is a perfect Morse–Bott–Novikov function on $L X$

Here

“Novikov” means that it is multiple-valued and thus the Morse–Smale complex should be constructed from the critical points on a covering $L \tilde { X }$ and treated as a module over the group of covering transformations.   
• The critical points are in fact constant loops and thus the critical locus of $\mathcal { A }$ on the covering consists of copies of the manifold $X$ itself duplicated as many times as many elements are in the covering transformation group. The critical components are transversally nondegenerate so that $\mathcal { A }$ is a Morse–Bott function.   
• The group of covering transformations is in fact the lattice $\mathbb { Z } ^ { k } \ : = \ : \pi _ { 2 } ( X ) \cap H _ { 2 } ( X , \mathbb { R } )$ of spherical periods of closed 2-forms on $X$ and thus the Morse–Smale–Bott–Novikov complex can be identified with the homology group $H _ { * } ( X , \mathbb { Z } [ q , q ^ { - 1 } ] )$ of $X$ where the coefficient ring is a group ring of the lattice (in the first approximation it can be taken as the ring of Laurent polynomials in $k$ generators $q = ( q _ { 1 } , . . . , q _ { k } ) )$ ).   
• Finally, “perfect” means that the boundary operator in the complex is zero so that $F H _ { * } ( X )$ $\cong H _ { * } ( X , \mathbb { Z } [ q ^ { \pm 1 } ] )$ as a $\mathbb { Z } [ q ^ { \pm 1 } ]$ -module.

The latter statement is due to the fact that $\mathcal { A }$ is the Hamiltonian of a circle action. The Atiyah convexity theorem [A] says in particular that the Hamiltonian of a torus action on a compact symplectic manifold is a perfect Morse–Bott function. A “scientific” explanation [G]

is that the same manifold is the critical set of a function (which leads to the Morse inequality) and the fixed set of a sircle action (which leads to the opposite Smith inequality in equivariant cohomology, see also [G1] where locally hamiltonian torus actions are considered). A geometrical argument behind this property works pretty well in the infinite-dimensional Morse theory if one deals with only bounded trajectories of the gradient flow.

Now we can describe geometrically the Morse–Bott cycles of Floer homology theory. They are enumerated by ordinary cycles in the components of the critical locus. Pick such a component $X$ and a cycle $a \subset X$ . The corresponding Morse–Bott (co)cycle $A \subset L X$ is the union of all the gradient trajectories outgoing (resp. ingoing) the critical set $a$ when time $\quad \to \ - \infty$ ( $+ \infty$ respectively). Since the gradient flow of $\mathcal { A }$ consists in analytic continuation, we come to the following description of the cycle $A$ :

$A = \left\{ \begin{array} { r l r l } \end{array} \right.$ { boundary values of holomorphic maps of the unit disk $D \subset \mathbb { C }$ to $X$ with the center in $a \subset X \}$ .

# 2.2 Multiplication

After such an informal description of the additive structure in Floer homology it is time to discuss multiplication. There are at least two reasons why analogue of usual cup-product may not exist in Floer’s theory:

1. intersections in general position of Morse–Bott cycles in $L X$ which have “semi-infinite” dimension would give rise to the cycles of finite dimension rather than to “semi-infinite” cycles again;   
2. finite-dimensional Novikov’s cohomology is cohomology with local coefficients determined by periods $\log { q }$ of the closed 1-form; cup-product of such cohomology is accompanied by tensor multiplication of the local coefficient systems and would give rise to $q ^ { 2 }$ in the product, instead of $q$ again.

In fact the multiplicative structure in Floer homology is analogous to the convolution in the homology of a Lie group induced by multiplication in the group. The “group” operation on $L X$ consists in composing parametrized loops at the marked point $t = 0$ on the circle $S ^ { 1 }$ . This operation is ill-defined since the loops we consider are free. However this operation considered as a correspondence can be described by its graph in $L X ^ { 3 }$ , and the convolution multiplication $A * B$ of Morse–Bott cycles can be defined through intersection indices $\langle A * B , C \rangle$ of the products $A \times B \times C \subset L X ^ { 3 }$ with the graph.

By some technical analytical reasons it is more convenient to perturb the graph and consider instead the cycle in $L X ^ { 3 }$ which consists of triples of loops which are boundary values of a holomorphic map of “pants” to $X$ . More generally, one can define multiple products $A _ { 1 } * \ldots * A _ { N }$ through intersection indices $\langle A _ { 1 } * \ldots * A _ { N } , C \rangle$ in $L X ^ { N + 1 }$ considering compositions of pants and their holomorphic maps to $X$ .

In more detail, denote $\Pi _ { N }$ the standard Riemann sphere $\mathbb { C } P ^ { 1 }$ with $N$ disks detached and their boundaries left oriented and parametrized by the standard unit circle $S ^ { 1 }$ . Denote $\Gamma _ { N }$ the cycle in $L X ^ { N }$ which consists of $N$ -tuples of boundary values of holomorphic maps $\Pi _ { N }  X$ . For

$N$ given Morse–Bott cycles $A _ { 1 } , . . . , A _ { N }$ in $L X$ define their $\langle A _ { 1 } | . . . | A _ { N } \rangle$ as the intersection index of “semi-infinite cycles” $A _ { 1 } \times . . . \times A _ { N } \subset L X ^ { N }$ and $\Gamma _ { N }$ .

We should make a correction here: the intersection index should be defined as Novikov’s one. This means that the product $A _ { 1 } \times \ldots \times A _ { N }$ should be considered as a cycle on the diagonal $\mathbb { Z } ^ { k }$ -covering $( L X ^ { N } )$ . An important property of $\Gamma _ { N }$ is that it has a canonical lifting to this covering: an $N$ -tuple of the boundary values is provided with the homotopy type of the map $\Pi _ { N }  X$ . Novikov’s intersection index of two transversal cycles $A$ and $B$ on the covering, by definition, assumes values in the group ring of the covering and counts isolated intersection points of the cycles projected to the base, with signs and “weights” $q ^ { d } \in \mathbb { Z } [ q ^ { \pm 1 } ]$ , where $d \in \mathbb { Z } ^ { k }$ is the covering transformation that transforms the preimages in $A$ and $B$ of the intersection point into one another.

Now we can describe geometrically an intersection event of $A _ { 1 } \times \ldots \times A _ { N }$ with $\Gamma _ { N }$ . The Morse– Novikov cycles $A _ { i }$ correspond to some finite-dimensional cycles $a _ { i }$ in $X$ . An intersection point, on one hand, is an $N$ -tuple of loops which are boundary values of $N$ parametrized holomorphic disks in $X$ with centers respectively in $a _ { 1 } , . . . , a _ { N }$ . On the other hand it is the $N$ -tuple of boundary values of a holomorphic map $\Pi _ { N }  X$ . Due to the uniqueness of analytic continuation, the disks and $\Pi _ { N }$ glue up to a single holomorphic map $\varphi : \mathbb { C } P ^ { 1 } \to X$ with the centers $x _ { 1 } , . . . , x _ { N }$ of the (formerly detached) disks being mapped to the cycles $a _ { 1 } , . . . , a _ { N }$ respectively. The group element $d$ in the definition of Novikov’s intersection index, in our situation measures the difference of homotopy types of the two holomorphic films attached to the $N$ -tuple of loops and equals the homotopy type of the map $\varphi$ , i. e. the degree of the rational curve $\varphi ( \mathbb { C } P ^ { 1 } )$ . Thus we come to Vafa’s formula:

$$
\langle A _ {1} | \dots | A _ {N} \rangle = \sum_ {\text {i s o l a t e d h o l o m o r p h i c m a p s}} \qquad \pm q ^ {\deg \varphi}.
$$

$$
\varphi : (\mathbb {C} P ^ {1}, x _ {1}, \dots , x _ {N}) \rightarrow (X, a _ {1}, \dots , a _ {N})
$$

The assumption that the intersected cycles are transversal means that the number of independent holomorphic sections of the induced tangent bundle $\varphi ^ { ! } T _ { X }$ equals the Euler characteristic $c ( d ) + \dim X$ prescribed by the Riemann–Roch formula, and the constraints $\varphi ( x _ { i } ) \in a _ { i }$ are nondegenerate (in the sense of implicit function theorem). Thus the isolatedness implies

$$
c (d) + \dim_ {\mathbb {C}} X = \sum_ {i} \operatorname {c o d i m} _ {\mathbb {C}} a _ {i}.
$$

Notice that holomorphic spheres constrained at two points are never isolated (circle action! By the way it is that geometrical argument that makes $\mathcal { A }$ perfect) and thus the double intersection index $\langle A , B \rangle$ coincides with the non-degenerate Poincare pairing of cycles $a , b$ in $X$ . One can identify a cycle $a$ of codimension $\alpha$ in $X$ with the Poincare-dual cohomology class of degree $\alpha$ . The above formula means that $\langle A _ { 1 } | . . . | A _ { N } \rangle$ defines in this way a “quantum” $q$ -valued intersection pairing $H ^ { * } ( X ) ^ { \otimes N } \to \mathbb { Z } [ q ^ { \pm 1 } ]$ which respects the usual grading in cohomology provided that $\deg q ^ { d } = c ( d )$ :

$$
\deg \langle a _ {1} | \dots | a _ {N} \rangle = \deg_ {\mathbb {C}} a _ {1} + \dots + \deg_ {\mathbb {C}} a _ {N} - \dim_ {\mathbb {C}} X.
$$

The triple “pairing” can be used in order to define the “quantum multiplication” $a * b$ :

$$
\forall c \langle a * b, c \rangle = \langle a | b | c \rangle .
$$

The fact that this multiplication is associative as well as that the multiple pairings can be expressed through $^ *$ -operation and Poincare pairing with the fundamental cycle [1] as

$$
\langle a _ {1} | \dots | a _ {N} \rangle = \langle a _ {1} * \dots * a _ {N}, \mathbf {1} \rangle ,
$$

reduces to the principal axiom of Topological Field Theory: i

If the surface $\Pi _ { N }$ is cut by a circle into a union of two surfaces $\Pi _ { M + 1 }$ and $\Pi _ { N - M + 1 }$ then the corresponding intersections satisfy

$$
\langle a _ {1} | \dots | a _ {N} \rangle = \sum_ {j} \langle a _ {1} | \dots | a _ {M} | b _ {j} \rangle \langle c _ {j} | a _ {M + 1} | \dots | a _ {N} \rangle
$$

where $\begin{array} { r } { \sum _ { j } b _ { j } \otimes c _ { j } \in H ^ { * } ( X \times X ) } \end{array}$ is Poincare-dual to the class of the diagonal $X \subset X \times X$ ).

Rigorous justification of this axiom as well as of correctness of the above definitions is obstructed by a number of highly non-trivial problems.

First of all, in order to bring the cycles in $L X ^ { N }$ to transversal position one needs, in general, to perturb the complex structure on $X$ toward almost complex structures, and the whole story begins to depend on Gromov’s theory [Gr] of pseudo-holomorphic curves in symplectic manifolds and compactifications of their moduli space.

Even in the additive Floer theory some difficulties (with multiple coverings of holomorphic curves) has not been overcome so far. The situation seems to be simpler, and the difficulty resolved, in the case of almost Kahler manifolds with positive first Chern class $c$ and almost complex structure close to an integrable one (see [O]). The case of zero first Chern class which also has been worked out [HS], requires Novikov’s completion of the group ring $\mathbb { Z } [ q ^ { \pm 1 } ]$ (Vafa’s formula may contain infinite sums).

In the cases when the additive theory can be completed successfully, correctness of the definitions of multiple intersection indices, their skew-commutativity, independence on moduli of surfaces $\Pi _ { N }$ , on the choice of cycles in the homology classes, and so on, does not seem to exhibit further complications (see [R]).

At the same time, associativity of the quantum multiplication and the axioms of Topological Field Theory have been verified, as far as we know, only in the simplest case of manifolds $X$ with $\pi _ { 2 } ( X ) = 0$ (M.Schwartz) where instanton corrections do not occur at all.

# 2.3 Alternative approaches

We briefly review here some other constructions of quantum cohomology algebras. Later they will be described in more detail in connection with equivariant theory.

First of all, instead of the ill-defined composition map $L X \times L X \to L X$ one can consider a well-defined evaluation map $L X \to L X \times X$ :

$$
\left(\operatorname {a l o o p} t \mapsto \gamma (t)\right) \mapsto (\gamma \in L X, \gamma (t _ {0}) \in X).
$$

It induces a linear map

$$
H ^ {*} (X) \otimes F H ^ {*} (X) \to F H ^ {*} (X)
$$

and thus makes cohomology classes of $X$ act on the Floer cohomology $H ^ { \ast } ( X , \mathbb { Z } [ [ q ^ { \pm 1 } ] ] )$ of the loop space by $\mathbb { Z } [ [ q ^ { \pm 1 } ] ]$ -linear operators. These operators, along with operators of multiplication by $q$ , generate some associative skew-commutative operator algebra. Composition of such operators differs in fact from ordinary cup-product in $H ^ { * } ( X )$ . It is not obvious from this point of view even that they should form an algebra closed with respect to composition. However interpretation of matrix elements of such operators in terms of rational curves in $X$ leads directly to Vafa’s definition of quantum cup-product. Such a module structure in Floer homology of $L X$ over cohomology of $X$ itself has been exploited many times in the literature on symplectic topology [FW], [Oh], [F2], [H], [G1], [G2] (and in a recent paper [S] on quantum cohomology).

A similar approach, based however on differential forms, was studied in [V]. A closed differential $r$ -form $p$ on $X$ and a density $\rho$ on the unit circle determine a closed differential $r$ -form $P$ on the loop space $L X$ :

$$
P | _ {\gamma} (v _ {1}, \dots , v _ {r}) = \oint p | _ {\gamma (t)} (v _ {1} (t), \dots , v _ {r} (t)) \rho (t) d t.
$$

The ordinary cohomology class of $P$ on $L X$ depends, by the Stokes theorem, only on the class of $p$ on $X$ and on the total “mass” $\oint \rho ( t ) d t$ . However we are going to integrate $P$ over non-compact cycles in $L X$ , so that the Stokes theorem does not apply literally. The cycle we need is denoted $\mathcal { M } _ { d }$ and consists of algebraic loops of degree $d$ in $X$ , i. e. degree $d$ holomorphic maps $\mathbb { C } P ^ { 1 } \to X$ which can be considered as elements of the loop space if we restrict them to the unit circle in $\mathbb { C } - 0$ . The cycle $\mathcal { M } _ { d }$ — a “moduli space” of rational curves — can be compactified, after Gromov [G], by reducible curves, and this is a reason to expect that the integral converge. The reducible curves however do not correspond to any loops, and the compactification can not be done inside $L X$ .

One can define quantum intersection pairings as

$$
\langle p _ {1} | \dots | p _ {N} \rangle = \sum_ {d} \pm q ^ {d} \oint_ {\mathcal {M} _ {d}} P _ {1} \wedge \dots \wedge P _ {N}.
$$

assuming the corresponding densities $\rho _ { i } , \ i = 1 , . . . , N$ , being of unit total mass each and generic. The integrals in this sum can be non-zero only if the total degree $r _ { 1 } + \ldots + r _ { N }$ of the differential form equals the dimension $2 ( c ( d ) + \dim X )$ of the cycle $\mathcal { M } _ { d }$ and reduces to $\int _ { X } p _ { 1 } \wedge \ldots \wedge p _ { N }$ for $d = 0$ .

The coincidence of such intersection pairings with previously defined ones becomes “obvious” if we interpret them in the spirit of integral geometry. Imagine that the densities $\rho _ { i }$ has been chosen as Dirak $\delta$ -functions concentrated at $N$ generic marked points $x _ { 1 } , . . . , x _ { N }$ on the unit circle. Then

$$
\int_ {\mathcal {M} _ {d}} P _ {1} \wedge \ldots \wedge P _ {N} = \int_ {\bar {\mathcal {M}} _ {d}} \bar {p} _ {1} \oplus \ldots \oplus \bar {p} _ {N}
$$

where $p _ { i }$ is a differential form on $X ^ { N }$ obtained as the pull-back of of $p _ { i }$ on the $i$ -th factor, and $\mathcal { M } _ { d }$ is the closure in $X ^ { N }$ of the image of the evaluation map

$$
\left(\mathcal {M} _ {d} \subset L X\right) \to X ^ {N}: \gamma \mapsto \left(\gamma (x _ {1}), \dots , \gamma (x _ {N})\right).
$$

The fundamental class of the complex variety $\mathcal { M } _ { d }$ in $H ^ { * } ( X ^ { d } )$ is the same for generic marked points. Taking the average value of such integrals, defined by means of $\delta$ -densities, over the torus $( S ^ { 1 } ) ^ { N }$ in the configuration space $( \mathbb { C } - 0 ) ^ { N }$ of marked points we conclude that the quantum intersection pairing of closed forms depends only on their cohomology classes in $H ^ { * } ( X )$ and does not depend on the densities provided that they are, say, continuous. On the other hand, replacing the forms $p _ { i }$ by their Poincare-dual cycles we find the integral equal to an intersection index in $X ^ { N }$ with the “moduli space” $\mathcal { M } _ { d }$ , and this leads back to the original Vafa’s construction — counting rational curves constrained at marked points. Notice that this construction of $\langle p _ { 1 } | . . . | p _ { N } \rangle$ as intersection indices in $X ^ { N }$ also explains how the signs in Vafa’s formula should be chosen.

The last construction of quantum cohomology algebras — via generating volume functions is most convenient in the case when the ordinary cohomology algebra $H ^ { * } ( X )$ is generated (as an algebra) by Kahler classes, and will be described below under this assumption. Let $p _ { 1 } , . . . , p _ { k }$ be an integer basis of non-negative $( 1 , 1 )$ -forms in $H ^ { 2 } ( X )$ , $p ( z ) = z _ { 1 } p _ { 1 } + . . . + z _ { k } p _ { k }$ be a general linear combination. If $p ( z )$ is a Kahler form on $X$ the corresponding form $P ( z )$ is a Kahler form on the loop space $L X$ , and the following formal series

$$
V (z, q) = \sum_ {d} q ^ {d} \int_ {\mathcal {M} _ {d}} \exp (P (z))
$$

represents the Kahler volume of the “weighted moduli space”

$$
\mathcal {M} = \cup_ {d} q ^ {d} \mathcal {M} _ {d},
$$

since the terms of the exponential series

$$
\exp P = \sum_ {r} \frac {1}{r !} P \wedge \dots \wedge P (r \mathrm {t i m e s})
$$

represent $r$ -dimensional Kahler volumes with respect to $P$ .

We call $V ( z , q )$ generating volume function (in fact it is a simplified version of the generating correlation function $\Phi$ from CTFT [W],[D],[K]).

It has the following properties:

1. $V ( z , q )$ becomes quasi-homogeneous of degree $- \dim X$ if we put $\deg z _ { i } = - 1$ , $\deg q _ { i } = D _ { i }$ where $c = D _ { 1 } p _ { 1 } + \ldots + D _ { k } p _ { k }$ represents the 1-st Chern class of $X$ in the basis $( p _ { 1 } , . . . , p _ { k } )$ ;   
2. $\begin{array} { r } { V ( z , 0 ) = \int _ { X } \exp ( p ( z ) ) } \end{array}$ is the volume function of $X$ ;   
3. quantum intersection indices of the generators $p 1 , . . . , p _ { k }$ can be expressed in terms of $V ( z , q )$ as

$$
\langle p _ {i _ {1}} | \dots | p _ {i _ {N}} \rangle = \frac {\partial^ {N}}{\partial z _ {i _ {1}} \dots \partial z _ {i _ {N}}} | _ {z = 0} V (z, q)
$$

(this is due to the very property of the exponential function).

This last formula implies that one can define the quantum cohomology algebra $Q H ^ { * } ( X )$ as the quotient of the polynomial algebra $\mathbb { Z } [ p , q ]$ by the ideal $I$ of all polynomials $R ( p , q )$ such that

$$
R (\partial / \partial z _ {1},..., \partial / \partial z _ {k}, q _ {1},..., q _ {k}) V (z, q) = 0.
$$

Example: $Q H ^ { * } ( \mathbb { C } P ^ { 1 } )$ . A holomorphic map $\mathbb { C } P ^ { 1 } \to \mathbb { C } P ^ { 1 }$ of degree $d$ is given by the ratio $f / g$ of two homogeneous polynomials

$$
f = \sum a _ {i} x ^ {i} y ^ {d - i}, g = \sum b _ {i} x ^ {i} y ^ {d - i}
$$

in two variables. This means that the space $\mathcal { M } _ { d }$ of such maps compactifies to the complex projective space $\mathbb { C } P ^ { 2 d + 1 }$ . Let $p$ be the Fubini Kahler form on the target $\mathbb { C } P ^ { 1 }$ . It is obtained from the form

$$
\partial \bar {\partial} \log (f \bar {f} + g \bar {g})
$$

in homogeneous coordinates $( f , g )$ . The corresponding Kahler form $P$ on $\mathcal { M } _ { d } ~ \subset ~ L ( \mathbb { C } P ^ { 1 } )$ is similarly obtained from

$$
\partial \bar {\partial} \log (f \bar {f} + g \bar {g}) | _ {(x, y) = (e ^ {i t}, 1)}
$$

as their mean value over $t$ . At $t = 0$ this gives

$$
\partial \bar {\partial} \log [ | \sum a _ {i} | ^ {2} + | \sum b _ {i} | ^ {2} ]
$$

and leads to a non-negative $( 1 , 1 )$ -form which extends to $\mathbb { C } P ^ { 2 d + 1 }$ and represents there a generator of $H ^ { 2 } ( \mathbb { C } P ^ { 2 d + 1 } ) \cong \mathbb { Z }$ . The same properties hold for all $t$ , and thus $P$ represents the class the of Fubini form on $\mathbb { C } P ^ { 2 d + 1 }$ . We conclude that

$$
V (z, q) = \sum_ {d = 0} ^ {\infty} \frac {z ^ {2 d + 1}}{(2 d + 1) !} q ^ {d}.
$$

It is easy to see that the ideal $I$ of polynomials $F ( \partial / \partial z , q )$ annihilating $V$ is generated by $( \partial / \partial z ) ^ { 2 } -$ $q$ and therefore

$$
Q H ^ {*} (\mathbb {C} P ^ {1}) = \mathbb {Z} [ p, q ] / (p ^ {2} - q).
$$

We find a posteriori that it is indeed a $q$ -deformation of the classical cohomology ring $H ^ { * } ( \mathbb { C } P ^ { 1 } ) =$ $\mathbb { Z } [ p ] / ( p ^ { 2 } )$ .

# 2.4 Characteristic lagrangian variety

Keeping the assumption, that cohomology algebra of $X$ is generated by Kahler classes, and the notations introduced in the end of 2.3, we describe here $Q H ^ { * } ( X , \mathbb { C } )$ as the algebra of functions on some lagrangian variety.

Since the quantum cohomology algebra is now identified with the quotient $\mathbb { C } [ p , q ] / I$ , its spectrum is a subvariety $L$ in the space $\mathbb { C } ^ { 2 k }$ with coordinates $( p _ { 1 } , . . . , p _ { k } , q _ { 1 } , . . . , q _ { k } )$ with the ideal $I ( L ) = I$ (strictly speaking, the variety can be defined only over formal series if the 1-st Chern class $c$ of $X$ is not positive). In any case, it is quasi-homogeneous with $\deg p _ { i } = 1 , \deg q _ { i } = D _ { i }$ . The space $\mathbb { C } ^ { 2 k }$ has the canonical Poisson structure

$$
\sum_ {i = 1} ^ {k} q _ {i} \frac {\partial}{\partial p _ {i}} \wedge \frac {\partial}{\partial q _ {i}}
$$

which is nothing but extension of the canonical symplectic structure

$$
\sum d p _ {i} \wedge \frac {d q _ {i}}{q _ {i}}
$$

on the cotangent bundle

$$
T ^ {*} B = H _ {2} (X, \mathbb {C}) \times [ H ^ {2} (X, \mathbb {C}) / 2 \pi \sqrt {- 1} \mathbb {Z} ^ {k} ]
$$

of the torus $B$ dual to the 2-nd homology lattice $\mathbb { Z } ^ { k }$ . We claim that the variety $L$ is lagrangian with respect to this symplectic form.

Indeed, interpret the Floer cohomology space

$$
F H ^ {*} (X, \mathbb {C}) = H ^ {*} (X, \mathbb {C}) \otimes \mathbb {C} [ q ^ {\pm 1} ]
$$

as the space of vector-functions of $q$ with values in the vector space $W = H ^ { * } ( X , \mathbb { C } )$ and introduce the following operator-valued 1-form

$$
A = \sum A _ {i} (q) \frac {d q _ {i}}{q _ {i}} = (p _ {1} *) \frac {d q _ {1}}{q _ {1}} + \ldots + (p _ {k} *) \frac {d q _ {k}}{q _ {k}}.
$$

Here $A _ { i } = p _ { i } *$ is understood as the operator on $W$ of quantum multiplication by $p _ { i }$ computed at a particular value of $q$ . First of all, we claim that this 1-form satisfies:

$$
A \wedge A = 0, d A = 0
$$

(which means in fact that $\varepsilon d + A \wedge$ is a flat connection operator for all $\varepsilon$ ). The 1-st identity simply means that the operators $A _ { i }$ commute so as $p _ { i } *$ do. The 2-nd identity means that the matrix elements of $A$ are closed 1-forms and does not follow from any formal properties of quantum multiplication which have been discussed so far. It can be reformulated, in terms of matrix elements of $A _ { i }$ , as follows:

For any two cycles $a$ and $b$ in $X$ the quantum intersection indices $\langle a | p _ { i } | b \rangle$ are partial derivatives qi ∂S∂q $q _ { i } \frac { \partial S } { \partial q _ { i } }$ of a single (locally defined) function $S = S _ { a , b } ( q )$ .

Put

$$
S _ {a, b} = \sum_ {i} \left\langle a, p _ {i}, b \right\rangle \log \left(q _ {i}\right) +
$$

$$
+ \sum_ {\text {r a t i o n a l c u r v e s i n} X} \quad \pm q ^ {d}.
$$

$$
\text {w i t h} 0 \in a, \infty \in b \text {o f d e g r e e} d > 0
$$

$$
\text {a n d w i t h} c (d) + \dim X = \operatorname {c o d i m} _ {\mathbb {C}} a + \operatorname {c o d i m} _ {\mathbb {C}} b + 1
$$

The 1-st sum is a potential for the constant terms in $\langle a | p _ { i } | b \rangle$ and involves classical intersection indices. The 2-nd sum counts non-constant rational curves, constrained at two points, as if they were discrete. If such a curve contributes by $\pm q ^ { d }$ to $S _ { a , b }$ then it contributes by $\pm d _ { i } q ^ { d }$ to $q _ { i } \partial S _ { a , b } / \partial q _ { i }$ . Here $d _ { i }$ is exactly the intersection index of a complex hypersurface Poincare-dual to $p _ { i }$ with this rational curve. This means that there are exactly $d _ { i }$ ways to parametrize the curve in such a fasion that $0 \in a$ , $\infty \in b$ and $1 \in p _ { i }$ , and hence the curve contributes to $\langle a | p _ { i } | b \rangle$ with the same weight $\pm d _ { i } q ^ { d }$ . This proves our assertion (modulo our usual reservations). In fact this $S _ { a , b }$ is one of the “higher order” pairings considered in Conformal Field Theory (actually it is the lower order pairing).

Now the lagrangian property of $L$ follows from a general lemma (which we learned from N.Reshetikhin).

Lemma. Let

$$
A = \sum_ {i} A _ {i} (t) d t _ {i}
$$

be a matrix-valued differential 1-form satisfying $A \land A = 0$ and $d A = 0$ . Let the scalar differential 1-form

$$
p = \sum_ {i} p _ {i} (t) d t _ {i}
$$

be its simple eigen-value. Then p is closed.

Proof. The assumption actually means that the commuting matrices $A _ { i } ( t )$ have a common eigen-vectors $w ( t )$ such that $A _ { i } ( t ) w ( t ) = p _ { i } ( t ) w ( t )$ . Being simple, the eigen-vectors can be chosen smooth in $t$ , and the transposed matrices $A _ { i } ^ { * }$ have a smooth field of eigen-covectors $w ^ { * } ( t )$ (with the same eigen-values) normalized in such a way that $\langle w , w ^ { * } \rangle = 1$ identically. Now we have

$$
\begin{array}{l} d (p d t) = d \left(\langle w, w ^ {*} \rangle (p d t)\right) = d \langle A w, w ^ {*} \rangle = \\ \langle (d A) w, w ^ {*} \rangle - \langle A \wedge d w, w ^ {*} \rangle - \langle A w, d w ^ {*} \rangle = \\ \langle d w, A ^ {*} w ^ {*} \rangle - \langle A w, d w ^ {*} \rangle = (d \langle w, w ^ {*} \rangle) \wedge (p d t) = 0. \\ \end{array}
$$

Applied to our quantum cohomology situation, this lemma shows that every non-singular local branch of $L$ over $B$ is a lagrangian section of $T ^ { * } B$ . This implies that $I$ is a Poisson ideal at least in the case if $I = { \sqrt { I } }$ .

Below we explain how intersection pairings and generating volume functions can be described in terms of geometry on $L$ assuming for simplicity that $I = { \sqrt { I } }$ and that the 1-st Chern class of $X$ is positive (so that $L$ is indeed a quasi-homogeneous affine algebraic subvariety in $\mathbb { C } ^ { 2 k }$ with coordinates $( p , q )$ ).

Consider the class in quantum cohomology algebra of $X \times X$ Poincare-dual to the diagonal $X \subset X \times X$ . It can be considered as a function on the characteristic lagrangian variety of $X \times X$ which is nothing but $L \times L$ . Restrict this function to the diagonal $L \subset L \times L$ and denote the restriction $\Delta \in \mathbb { C } [ L ]$ . Let $\varphi _ { 1 } , . . . , \varphi _ { N } \in \mathbb { C } [ L ]$ be some quantum cohomology classes. Then for generic $q \in B$

$$
\langle \varphi_ {1} | \dots | \varphi_ {N} \rangle (q) = \sum_ {p \in L \cap T _ {q} ^ {*} B} \frac {\varphi_ {1} (p) \dots \varphi_ {N} (p)}{\Delta (p)}
$$

and

$$
V (z, q) = \sum_ {p \in L \cap T _ {q} ^ {*} B} \frac {\exp (z _ {1} p _ {1} + \ldots z _ {k} p _ {k})}{\Delta (p)}.
$$

The last remark: since $L$ is lagrangian, the action 1-form on $T ^ { * } B$ restricted to $L$ is exact,

$$
\sum p _ {i} \frac {d q _ {i}}{q _ {i}} | _ {L} = d C, C \in \mathbb {C} [ L ].
$$

Using quasi-homogeneity of $L$ and Cartan’s homotopy formula one can easily show that $C =$ $D _ { 1 } p _ { 1 } + \ldots + D _ { k } p _ { k }$ is the 1-st Chern class of $X$ understood as a function on $L$ .

# 3 Equivariant quantum cohomology

# 3.1 Why “equivariant”?

In our inductive computation of quantum cohomology of flag manifolds we will encounter the following kind of problems. With a vector bundle over some base $B$ one can associate a fiber bundle $E  B$ whose fibers are flag manifolds — they consist of flags in the fibers of the vector bundle. Consider the maps of $\mathbb { C } P ^ { 1 }$ with $N$ marked points to $E$ whose composition with the projection to $B$ maps $\mathbb { C } P ^ { 1 }$ to a point and which are holomorphic if considered as maps to the fiber flag manifolds. We will call such holomorphic curves vertical.

One may pick $N$ cycles in $E$ and ask how many of such vertical parametrized rational curves of certain homotopy type have the 1-st marked point on the 1-st cycle, the 2-nd marked point — on the 2-nd cycle, and so on.

When the base $B$ is a point, the problem (properly understood of course in terms of intersection indices) becomes a question about structural constants of the quantum cohomology algebra of the flag manifold. Our more general problem about rational curves in flag bundles will not arise in its full generality — we will rather need a sequence of special bundles of flag manifolds over Grassmannians and holomorphic hypersurfaces in the role of the cycles.

On the other hand, this sequence of problems can be understood better in the context of vector bundles over arbitrary finite cellular bases since in such generality it can be replaced by a universal problem about the universal vector bundle over the classifying space $_ { B G }$ . The total space of the universal flag bundle $E \to B G$ is nothing but the homotopic quotient $E G \times _ { G } F$ of the flag manifold $F$ by the unitary group $G$ . Therefore our universal problem reduces to the question about structural constants of what should be called the equivariant quantum cohomology algebra of the flag manifold.

# 3.2 “Classical” equivariant cohomology

Recall some standard facts [Hs], [AB] about equivariant cohomology.

Let $X$ be a manifold provided with a left action of a compact Lie group $G$ . Consider the universal principal $G$ -bundle $E G \to B G$ — a principal $G$ -bundle with contractible total space $_ { E G }$ , and define the homotopic quotient $X _ { G }$ of $X$ by $G$ as $E G \times _ { G } X = ( E G \times X ) / G$ .

Examples. 1) If $X$ is a point then $X _ { G } = E G / G = B G$ .

2) If $H \subset G$ is a Lie subgroup, $X$ is the homogeneous space $G / H$ then $( G / H ) _ { G } = E G \times _ { G }$ $\ ( G / H ) = ( E G \times _ { G } G ) / H = E G / H = B H$ . For instance, if $G$ is the unitary group $U _ { n }$ and $H$ is its maximal torus $T ^ { n }$ so that $X$ is the flag manifold $F _ { n }$ then $X _ { G } = B T ^ { n } = ( \mathbb { C } P ^ { \infty } ) ^ { n }$ .

The equivariant cohomology $H _ { G } ^ { * } ( X )$ of a $G$ -space $X$ is defined as the ordinary cohomology $H ^ { * } ( X _ { G } )$ of its homotopic quotient. The natural fibration $X _ { G }  B G$ (with fiber $X$ ), induced by the projection of $E G \times X$ on the first factor, along with Example 1), provide the equivariant cohomology with a module structure over the coefficient algebra $H _ { G } ^ { * } ( p t )$ of the equivariant theory which is nothing but the characteristic class algebra $H ^ { * } ( B G )$ of the group $G$ .

Example. For the flag manifold $F _ { n }$ its $U _ { n }$ -equivariant cohomology can be identified with the polynomial ring in $n$ generators $\left( u _ { 1 } , . . . , u _ { n } \right)$ since $H ^ { * } ( \mathbb { C } P ^ { \infty } ) = \mathbb { C } [ u ]$ where $u$ is the 1-st Chern

class of the universal Hopf circle bundle. The module structure over the algebra of universal Chern classes $H ^ { * } ( B U _ { n } ) = \mathbb { C } [ c _ { 1 } , . . . , c _ { n } ]$ becomes more “visible” if we represent the equivariant cohomology of the flag manifold as the quotient of the polynomial algebra $\mathbb { C } [ u , c ]$ by the ideal of relations $c _ { i } = \sigma _ { i } ( u )$ , $i = 1 , . . . , n$ , where $\sigma _ { i }$ are elementary symmetric polynomials of $( u _ { 1 } , . . . , u _ { n } )$ .

Similarly, equivariant cohomology of cartesian products of flag manifolds are tensor products of equivariant cohomology of factors and they are modules over characteristic class algebras of products of unitary groups. Of course, this is a general property of products $\Pi X _ { i }$ of $G _ { i }$ -spaces.

# 3.3 Equivariant intersection indices

Consider a $D$ -dimensional compact oriented $G$ -manifold $X$ and the associate $X$ -bundle $\pi : X _ { G } $ $_ { B G }$ . Since we are actually going to apply our general constructions to homogeneous complex manifolds it is convenient to make a convention right now that all the dimensions are complex ones, and therefore dimensions of real manifolds or cycles can be half-integral. With this convention in force, let us consider equivariant cohomology classes $\rho _ { 1 } , . . . , p _ { N }$ of $X$ of total degree $M$ and define their intersection index $\langle p _ { 1 } , . . . , p _ { N } \rangle$ with values in the structural ring $H _ { G } ^ { * } ( p t )$ of equivariant theory.

If $C$ is a homology class of $_ { B G }$ of degree $K$ one can construct its inverse image $\pi ^ { - 1 } ( C )$ which is geometrically the preimage of the cycle $C$ in the bundle $\pi : X _ { G }  B G$ and represents a homology class of degree $K + D$ in $X _ { G }$ . By definition,

$$
\langle p _ {1}, \dots , p _ {N} \rangle [ C ] = (p _ {1} \dots p _ {N}) [ \pi^ {- 1} (C) ].
$$

This formula describes the intersection cohomology class through its evaluation on homology classes and may give rise to a non-zero result only if $M = K + D$ of course. In the case when an infinite-dimensional manifold has been chosen on the role of the classifying space $_ { B G }$ one may also think of $p _ { 1 } , . . . , p _ { n }$ as cycles of finite total codimension $M$ , and of $\langle . . . \rangle [ C ]$ as the mutual intersection index of $\rho _ { 1 } , . . . , p _ { N }$ and $\pi ^ { - 1 } ( C )$ . In the case if $C$ is a point our definition reduces to the ordinary intersection index in $X$ of cycles Poincare-dual to the restrictions of the cohomology classes $p _ { i }$ to the fiber of $\pi$ .

The equivariant intersection indices $H _ { G } ^ { * } ( X ) ^ { \otimes N }  H _ { G } ^ { * } ( p t )$ have the following more or less obvious properties:

1. They are homogeneous of degree $- \dim X$ (with our convention in force);   
2. They are $H ^ { * } ( p t )$ -multi-linear;   
3. They are totally anti-symmetric (notice that $H ^ { * } ( p t )$ happened to be commutative);   
4. They are determined by cup-multiplication in $H _ { G } ^ { * } ( X )$ and by the “intersection index” $H _ { G } ^ { * } ( X ) \to H _ { G } ^ { * } ( p t )$ with $N \ = \ 1$ which is nothing but the direct image operation π! : $H ^ { * } ( X _ { G } )  H ^ { * } ( B G )$ dual to the inverse image in homology.

In terms of differential forms the direct image operation consists in fiberwise integration.

Our objective for the moment is to describe explicitly the direct image for equivariant cohomology of flag manifolds.

Proposition. For the flag manifold $F _ { n }$ the direct image $\pi _ { ! } : \mathbb { C } [ u ] \to \mathbb { C } [ c ]$ is given by the following Cauchy formula:

$$
(\pi_ {!} f) (c) = (\frac {1}{2 \pi i}) ^ {n} \int_ {T ^ {n}} \frac {f (u) d u _ {1} \wedge \ldots \wedge d u _ {n}}{(\sigma_ {1} (u) - c _ {1}) \ldots (\sigma_ {n} (u) - c _ {n})}.
$$

The integral equals the total sum of residues in $\mathbb { C } ^ { n }$ . In other words, in order to find the direct image of a polynomial $f ( u )$ one first constructs its total alternation

$$
\operatorname {A l t} f (u) = \sum_ {w \in S _ {n}} (- 1) ^ {\varepsilon (w)} f (w u),
$$

then divides it by the “fundamental anti-invariant” (= Vandermond)

$$
\Delta_ {n} (u) = \det (\frac {\partial \sigma_ {i} (u)}{\partial u _ {j}})
$$

and expresses the ratio $\operatorname { A l t } f / \Delta _ { n }$ as a polynomial $\hat { f } ( \sigma ( u ) )$ of elementary symmetric functions: $\hat { f } ( c _ { 1 } , . . . , c _ { n } )$ is then the direct image of $f$ .

The main argument in the proof of this formula is “what else can it be?”

Indeed, due to linearity property the direct image operation is completely determined by its action on generators of $\mathbb { C } [ u ]$ as a $\mathbb { C } [ c ]$ -module. The generators can be chosen as homogeneous representatives of a linear basis in the ordinary cohomology $\mathbb { C } [ u ] / ( \sigma _ { 1 } ( u ) , . . . , \sigma _ { n } ( u ) )$ of the flag manifold (Nakayama lemma!). Due to the degree reasons these representatives all have zero direct images except the generator Poincare dual to the fundamental cycle. The latter has constant direct image, and the constant can be easily found equal 1 (evaluate the direct image at a point). The residue formula (and the operation $\Delta _ { n } ^ { - 1 }$ Alt) do have all there properties since $\deg \Delta _ { n }$ “accidentally” equals $\dim { F _ { n } }$ .

One more example. Consider the subgroup $G ^ { \prime } = U _ { m } \times U _ { n - m } \subset U _ { n } = G$ and the bundle $B G ^ { \prime }  B G$ with the fiber $G / G ^ { \prime } = G r ( n , m )$ . The direct image operation

$$
\text {D i r e c t} H ^ {*} (B G ^ {\prime}) = \mathbb {Z} \left[ c _ {1} ^ {\prime}, \dots , c _ {m} ^ {\prime}, c _ {1} ^ {\prime \prime}, \dots , c _ {n - m} ^ {\prime \prime} \right]\rightarrow \mathbb {Z} \left[ c _ {1}, \dots , c _ {n} \right] = H ^ {*} (B G)
$$

in this bundle somehow transforms partially symmetric polynomials of $( u ^ { \prime } , u ^ { \prime \prime } ) = ( ( u _ { 1 } , . . . , u _ { m } ) , ( u _ { m + 1 } , . . . , u _ { n } ) )$ to totally symmetric ones, since

$$
c _ {i} ^ {\prime} = \sigma_ {i} (u ^ {\prime}), c _ {j} ^ {\prime \prime} = \sigma_ {j} (u ^ {\prime \prime}), c _ {r} = \sum_ {i = 0} ^ {r} \sigma_ {i} (u ^ {\prime}) \sigma_ {r - i} (u ^ {\prime \prime}) = \sigma_ {r} (u)
$$

(where $\sigma _ { 0 } = 1$ ).

Corollary.

$$
[ D i r e c t i m a g e f ] (\sigma (u)) = \frac {A l t [ \Delta_ {m} (u ^ {\prime}) \Delta_ {n - m} (u ^ {\prime \prime}) f (\sigma (u ^ {\prime}) , \sigma (u ^ {\prime \prime})) ]}{m ! (n - m) ! \Delta_ {n} (u)}.
$$

Proof. We can represent $f ( c ^ { \prime } , c ^ { \prime \prime } )$ as the direct image $\Pi _ { ! } g ( u ^ { \prime } , u ^ { \prime \prime } )$ of some $g ( u )$ in the product of bundles $\Pi : B T ^ { m } \times B T ^ { n - m }  B U _ { m } \times B U _ { n - m }$ and thus identify $[ D i r e c t i m a g e f ]$ with $\pi _ { ! } g$ .

# 3.4 Instanton corrections

Let $X$ be a complex Kahler manifold of dimension $\boldsymbol { D }$ provided with a holomorphic action of the complexified compact Lie group $G \subset G _ { \mathbb { C } }$ . We will assume for simplicity that $X$ that $H ^ { 1 , 1 } ( X ) =$ $H ^ { 2 } ( X )$ . Notice that the lattice $\mathbb { Z } ^ { k }$ is a sublattice in the second homology group of the homotopic quotient $X _ { G }$ and thus classes of vertical rational curves in the total space of the bundle $X _ { G } \to B G$ are canonically identified with elements of $\mathbb { Z } ^ { k }$ .

We define quantum equivariant intersection indices as follows.

Let $p _ { 1 } , . . . , p _ { N }$ be cycles in $X _ { G }$ of finite codimensions which add up to $M$ . Their quantum intersection index $\langle p _ { 1 } | . . . | p _ { N } \rangle$ will be an element of the algebra $H _ { G } ^ { * } ( p t , \mathbb { Z } [ [ q ] ] )$ . Given a $K$ -dimensional cycle $C \subset B G$ , we define the value $\langle p _ { 1 } | . . . | p _ { N } \rangle [ C ]$ as the sum of contributions of rational parametrized curves $\varphi : \mathbb { C } P ^ { 1 } \to \pi ^ { - 1 } ( C )$ in the fibers of the bundle $\pi : X _ { G }  B G$ restricted to $C$ such that $N$ marked points $x _ { 1 } , . . . , x _ { N }$ in $\mathbb { C } P ^ { 1 }$ map to the cycles $p _ { 1 } , . . . , p _ { N }$ respectively: $\varphi ( x _ { i } ) \in p _ { i }$ . The contribution of $\varphi$ is non-zero only if $c ( d ) + D + K = M$ and equals $\pm q ^ { d }$ in the assumptions of course that the cycles $p _ { i }$ are in general position with respect to the family of vertical rational curves of degree $d$ , that the family indeed has the dimension $c ( d ) + D + K$ $\varphi$ predicted by the Riemann–Roch formula, and that the contributing curves are regular points in this family:

$$
\langle p _ {1} | \dots | p _ {N} \rangle [ C ] = \sum \quad \pm q ^ {d}.
$$

vertical discrete holomorphic maps:

$$
\left(\mathbb {C} P ^ {1}, x _ {1}, \dots , x _ {N}\right)\rightarrow \left(\pi^ {- 1} (C), p _ {1}, \dots , p _ {N}\right)
$$

of degree d

The sign $\pm$ in this formula can be defined naturally in terms of intersection indices in moduli space; it is “plus” at least in the case if all the cycles $p _ { i }$ and $C$ are holomorphic (the latter assumes that a complex manifold is taken on the role of $_ { B G }$ ), and will be described in 3.5 for arbitrary $C$ .

Rigorous justification of this construction, and in particular — verification that the intersection indices actually depend only on the (co)homology classes represented by the cycles $p _ { i }$ and $C$ , encounters the same difficulties as in the case of the quantum non-equivariant intersection indices. In particular, bringing to general position may involve perturbations of the complex structure towards almost complex ones which in our case should be done fiberwise in the bundle $X _ { G } \to B G$ and do not have to be the same on all fibers.

Intersection indices $\langle \left. \ldots \right. \rangle$ have the following obvious properties relating them with “classical” intersection indices $\langle , . . . , \rangle$ :

1. they are multi-linear and skew-symmetric;   
2. $\langle p _ { 1 } | . . . | p _ { N } | [ 1 ] \rangle = \langle p _ { 1 } | . . . | p _ { N } \rangle$ , where [1] represents the fundamental cycle in $X _ { G }$ ;   
3. $\langle p _ { 1 } | . . . | p _ { N } \rangle | _ { q = 0 } = \langle p _ { 1 } , . . . , p _ { n } \rangle$ — they are $q$ -deformations of classical intersection indices;   
4. $\langle p _ { 1 } | p _ { 2 } \rangle = \langle p _ { 1 } , p _ { 2 } \rangle$ so that $\langle p \vert \vert 1 \vert \rangle$ coincides with the classical direct image operation; and a less obvious

5. $H _ { G } ^ { * } ( p t )$ -multi-linearity property (where ‘·’ stands for the cap-product, Poincare dual to the ordinary multiplication of cohomology classes represented by finite codimension cycles)

$$
\langle \pi^ {*} (p) \cdot p _ {1} | \dots \rangle [ C ] = \langle p _ {1} | \dots \rangle [ p \cap C ] = (p \cdot \langle p _ {1} | \dots \rangle) [ C ]
$$

which means that a vertical rational curve in $X _ { G }$ which has a common point with the preimage $\pi ^ { - 1 } ( p )$ of a finite codimension cycle $p \subset B G$ in the base, is entirely contained in this preimage.

Similarly to ordinary quantum cohomology, quantum equivariant intersection indices have a few other interpretations.

# 3.5 Intersections in ‘moduli spaces’

Consider the product $X ^ { N }$ of $N$ copies of $X$ as a $G$ -manifold provided with the diagonal $G$ - action. The homotopic quotient $X _ { G } ^ { N }$ has $N$ canonical projections $X _ { G } ^ { N }  X _ { G }$ compatible with the projections $X _ { G } ^ { N }  B G$ , $X _ { G }  B G$ to the classifying space. Let $p _ { 1 } , . . . , p _ { N }$ be equivariant cohomology classes of $X$ . One may think of them as represented by finite codimension cycles in $X _ { G }$ , one in each of $N$ copies. Pulled back to $X _ { G } ^ { N }$ they define $N$ equivariant cohomology classes of $X ^ { N }$ which we denote $p _ { 1 } , . . . , p _ { N }$ too.

Let $\mathcal { M } _ { d }$ denote the space of parametrized rational curves $\varphi : \mathbb { C } P ^ { 1 } \to X$ of certain degree (= homology class) $d$ . Evaluation map $\mathcal { M } _ { d } \to X ^ { N } , \ \varphi \mapsto \varphi ( x _ { 1 } ) , . . . , \varphi _ { N } ( x _ { N } )$ at $N$ generic points in $\mathbb { C } P ^ { 1 }$ defines a $G$ -invariant complex subvariety in $X ^ { N }$ . Its fundamental cycle $\mathcal { M } _ { d }$ determines an equivariant cohomology class of $X ^ { N }$ : it is Poincare-dual to

$$
E G \times_ {G} \bar {\mathcal {M}} _ {d} \subset E G \times_ {G} X ^ {N}.
$$

We denote this equivariant class $[ \mathcal { M } _ { d } ]$ .

One defines the quantum equivariant intersection index using classical equivariant indices in $H _ { G } ^ { * } ( X ^ { N } )$ as

$$
\langle p _ {1} | \dots | p _ {N} \rangle = \sum_ {d} \langle p _ {1}, \dots , p _ {N}, [ \mathcal {M} _ {d} ] \rangle q ^ {d}.
$$

It is easy to see what is the meaning of the RHS, evaluated at a cycle $C \subset B G$ : it counts the numbers of discrete rational maps $\varphi$ to the fibers of the bundle $\pi ^ { - 1 } ( C ) \to C$ such that $\varphi ( x _ { i } )$ is in the cycle representing $p _ { i }$ in $X _ { G }$ . The maps are “weighted” by the factors $q ^ { d }$ and are counted with the signs prescribed by (co)orientations of the cycles. In particular, this construction (being at least morally equivalent to the first one) specifies how the signs $\pm$ in the previous definition should be chosen.

# 3.6 Integrals in loop spaces

The quantum intersection indices defined by means of evaluation maps are (expected to be) independent on the choice of evaluation points $x _ { 1 } , . . . , x _ { N }$ on the projective line provided that the points are generic (and in particular distinct). Therefore one can replace $\langle p _ { 1 } , . . . , p _ { N } , [ \mathcal { M } _ { d } ( x ) ] \rangle$ by its average value

$$
\int_ {T ^ {N}} \langle p _ {1}, \dots , p _ {N}, [ \mathcal {M} _ {d} (x) ] \rangle d x _ {1} \dots d x _ {N}
$$

where $T ^ { N }$ is a torus in the configuration space $( \mathbb { C } P ^ { 1 } ) ^ { N }$ of $N$ points ${ \boldsymbol x } = ( x _ { 1 } , . . . , x _ { N } )$ , namely the product of $N$ standard unit circles in $\mathbb { C } P ^ { 1 } = \mathbb { C } \cap \infty$ (notice that $T ^ { N }$ is dense in Zarissky topology on $( \mathbb { C } P ^ { 1 } ) ^ { N } .$ ). This formula allows us to interpret the intersection indices as some integrals of differential forms on loop spaces.

Suppose that the classifying space $_ { B G }$ is chosen in the form of infinite-dimensional manifold and that the equivariant cohomology classes $p _ { 1 } , . . . , p _ { N }$ are represented by closed differential forms on $X _ { G }$ . Such a differential form determines a differential form of the same degree on the space of free loops in $X _ { G }$ . Namely, if $t \mapsto \gamma ( t )$ is a loop, the average $\oint p _ { t } d t$ is an exterior form on the space of vector fields along the loop, and thus $P = \oint p _ { d } t$ is a differential form on the loop space, closed if $p$ is closed on $X _ { G }$ .

Furthermore, we interpret a (vertical) rational curve $\varphi : \mathbb { C } P ^ { 1 } \to X _ { G }$ as an “algebraic loop” restricting the map $\varphi$ to the unit circle $T \subset \mathbb { C } - 0 \subset \mathbb { C } P ^ { 1 }$ . Now on we may think of the spaces $\mathcal { M } _ { d }$ of rational maps, as well as of the spaces $\mathcal { M } _ { d } | C |$ of such vertical rational maps to the fibers of the bundle $X _ { G } \to B G$ over a given cycle $C \subset B G$ , as subsets (chains, cycles) in the loop space.

The above integral over the torus immediately turns into the integral in the loop space,

$$
\langle p _ {1}, \dots , p _ {N}, [ \mathcal {M} _ {d} ] \rangle [ C ] = \int_ {\mathcal {M} _ {d} [ C ]} P _ {1} \wedge \dots \wedge P _ {N}.
$$

As usual, this formula assumes that the integral equals zero unless the total degree $M$ of the wedge product equals the dimension $c ( d ) + D + K$ of the chain $\mathcal { M } _ { d } | C |$ .

We will make use of this construction in the special case when the equivariant cohomology algebra $H _ { G } ^ { * } ( X )$ is generated (as algebra) by the classes of degree 2 — that is of degree 1 taking into account our convention that all the dimensions and degrees are complex. Let $p _ { 1 } , . . . , p _ { n }$ now denote a set of such generators, i. e. a basis in $H _ { G } ^ { 2 } ( X )$ . We prefer to think of $p _ { i }$ as of closed differential 2-forms on the infinite-dimensional manifold $X _ { G }$ , or even as of symplectic (or Kahler) forms, taking into account our assumptions about $X$ and the fact that classifying spaces of compact Lie groups have Kahler models. Denote

$$
P (z) = z _ {1} P _ {1} + \dots + z _ {n} P _ {n}
$$

a general linear combination of the differential (symplectic, Kahler) 2-forms $P _ { i }$ on the loop space of $X _ { G }$ corresponding to the forms $p _ { i }$ on $X _ { G }$ . Let us define the generating volume function $V \in$ $H _ { G } ^ { * } ( p t , \mathbb { Z } [ [ z , q ] ] )$ — a formal series in $q$ and $z$ with coefficients in the ring of characteristic classes, such that the value of $V$ on a homology class represented by the cycle $C \subset B G$ is equal to the weighted oriented volume

$$
V | _ {[ C ]} = \sum_ {d} q ^ {d} \int_ {\mathcal {M} _ {d} [ C ]} \exp (P (z))
$$

of the space $\mathcal { M } [ C ] = \cup _ { d } q ^ { d } \mathcal { M } _ { d } [ C ]$ of vertical rational curves over $C$ . Here $\exp \left( P \right)$ stands for

$$
\sum_ {k = 0} ^ {\infty} \frac {1}{k !} P \wedge \ldots \wedge P (k \mathrm {t i m e s})
$$

so that the integral $\int _ { \mathcal { M } } \exp \left( P \right)$ really represents the symplectic $k$ -dimensional volume of a $k$ -cycle $\mathcal { M }$ if the form $P$ is symplectic (we should notice however that orientation of $C$ contributes the sign of the “volume”).

The generating volume function has not so many non-zero terms as one could think: due to dimension reasons it is weighted-homogeneous of degree $- D$ when the degrees of the variables are assigned as

$$
\deg q ^ {d} = c (d), \deg z _ {i} = - 1
$$

and characteristic classes from $H _ { G } ^ { * } ( p t )$ have their natural degrees.

One of applications of this function describes quantum intersection indices of the generators $p _ { i }$ :

$$
\langle p _ {i _ {1}} | \dots | p _ {i _ {N}} \rangle = \frac {\partial^ {N}}{\partial z _ {i _ {1}} \dots \partial z _ {i _ {N}}} | _ {z = 0} V (z)
$$

(it is just the property of the exponential series).

Another property of the volume generating functions, that we are going to exploit, is their simple behavior under product, restriction and induction operations.

Product. Let $X ^ { \prime }$ , $X ^ { \prime \prime }$ be compact Kahler $G ^ { \prime }$ - and $G ^ { \prime \prime }$ -spaces respectively, and $V ^ { \prime } ( z ^ { \prime } , q ^ { \prime } ) \in$ $H _ { G ^ { \prime } } ^ { * } ( p t )$ $ \mathsf { \Gamma } _ { \mathsf { Y } ^ { \prime } } ( p t ) , \mathsf { \Gamma } _ { { \mathsf { V } } ^ { \prime \prime } } ( z ^ { \prime \prime } , q ^ { \prime \prime } ) \ \in \ H _ { G ^ { \prime \prime } } ^ { * } ( p t )$ be the corresponding generating volume functions. Then the generating volume function $V$ for the $G ^ { \prime } \times G ^ { \prime \prime }$ -space $X ^ { \prime } \times X ^ { \prime \prime }$ is

$$
V \left(\left(z ^ {\prime}, z ^ {\prime \prime}\right), \left(q ^ {\prime}, q ^ {\prime \prime}\right)\right) = V ^ {\prime} \left(z ^ {\prime}, q ^ {\prime}\right) V ^ {\prime \prime} \left(z ^ {\prime \prime}, q ^ {\prime \prime}\right).
$$

Indeed, the homotopic quotient of $X ^ { \prime } \times X ^ { \prime \prime }$ is the product of $X _ { G ^ { \prime } } ^ { \prime }$ and $X _ { { G ^ { \prime \prime } } } ^ { \prime \prime }$ fibered over the product $B G ^ { \prime } \times B G ^ { \prime \prime }$ of classifying spaces. A holomorphic map to $X ^ { \prime } \times X ^ { \prime \prime }$ is a pair of holomorphic maps to $X ^ { \prime }$ and $X ^ { \prime \prime }$ respectively and hence the chain $\mathcal { M } _ { d ^ { \prime } , d ^ { \prime \prime } }$ factors:

$$
\mathcal {M} _ {d ^ {\prime}, d ^ {\prime \prime}} \left[ C ^ {\prime} \times C ^ {\prime \prime} \right] = \mathcal {M} _ {d ^ {\prime}} \left[ C ^ {\prime} \right] \times \mathcal {M} _ {d ^ {\prime \prime}} \left[ C ^ {\prime \prime} \right].
$$

Its volume with respect to $P ( z ) = P ^ { \prime } ( z ^ { \prime } ) \oplus P ^ { \prime \prime } ( z ^ { \prime \prime } )$ is the product of corresponding volumes and therefore

$$
\sum_ {\left(d ^ {\prime}, d ^ {\prime \prime}\right)} \left(q ^ {\prime}\right) ^ {d ^ {\prime}} \left(q ^ {\prime \prime}\right) ^ {d ^ {\prime \prime}} \int_ {\mathcal {M} _ {d ^ {\prime}} \left[ C ^ {\prime} \right] \times \mathcal {M} _ {d} ^ {\prime \prime} \left[ C ^ {\prime \prime} \right]} \exp (P (z)) =
$$

$$
[ \sum_ {d ^ {\prime}} (q ^ {\prime}) ^ {d ^ {\prime}} \int_ {\mathcal {M} _ {d ^ {\prime}} [ C ^ {\prime} ]} \exp (P ^ {\prime} (z ^ {\prime})) ] \cdot [ \sum_ {d ^ {\prime \prime}} (q ^ {\prime \prime}) ^ {d ^ {\prime \prime}} \int_ {\mathcal {M} _ {d} ^ {\prime \prime} [ C ^ {\prime \prime} ]} \exp (P ^ {\prime \prime} (z ^ {\prime \prime})) ].
$$

Restriction. Let $X$ be a compact Kahler $G$ -space and $G ^ { \prime } \subset G$ be a Lie subgroup. Considering $X$ as a $G ^ { \prime }$ -space, we obtain an $X$ -bundle $X _ { G ^ { \prime } }  B G ^ { \prime }$ (induced, as a bundle, from $X _ { G } \to B G$ by means of the natural map $\pi : B G ^ { \prime } \to B G$ of classifying spaces) and the corresponding map of total spaces $\zeta : X _ { G ^ { \prime } } \to X _ { G }$ with the fiber $G / G ^ { \prime }$ . Then for the generating volume functions $V ( z , q )$ and $V ^ { \prime } ( z ^ { \prime } , q )$ we have

$$
V ^ {\prime} \left(\zeta^ {*} (z), q\right) = \pi^ {*} V (z, q).
$$

Indeed, for a cycle $C ^ { \prime } \subset B G ^ { \prime }$ the bundle $\mathcal { M } _ { d } [ C ^ { \prime } ]  C ^ { \prime }$ is induced by $\pi$ from $\mathcal { M } _ { d } [ \pi _ { * } C ^ { \prime } ]   \pi ( C ^ { \prime } )$ and therefore

$$
\int_ {\mathcal {M} _ {d} [ C ^ {\prime} ]} \exp (\zeta^ {*} (P (z)) = \int_ {\mathcal {M} _ {d} [ \pi_ {*} C ^ {\prime} ]} \exp (P (z)).
$$

In particular, if $G ^ { \prime }$ is trivial so that $\pi$ is $E G \to B G$ and $X _ { G ^ { \prime } } = E G \times X$ , then the homomorphism $\zeta ^ { * } : H ^ { 2 } ( X _ { G } ) \to H ^ { 2 } ( X ) , z \mapsto z ^ { \prime }$ , is onto, and the generating volume function $V ^ { \prime } ( z ^ { \prime } , q )$ coincides with the non-equivariant one and can be computed from $V ( z , q )$ as its reduction $H _ { G } ^ { * } ( p t ) \to \mathbb { Z }$ modulo $G$ -characteristic classes of positive degree.

This implies that non-equivariant quantum intersection indices $\langle p _ { i _ { 1 } } | . . . | p _ { i _ { N } } \rangle$ are obtained by such a reduction from the corresponding quantum equivariant intersection indices.

Induction. Let $G ^ { \prime } \subset G$ be a subgroup with a simply-connected compact Kahler quotient $G / G ^ { \prime }$ , and $Y$ be a compact Kahler $G ^ { \prime }$ -space. We construct a compact Kahler $G$ -space $X = G \times _ { G ^ { \prime } } Y$ and call it induced from $Y$ (like induced representations). In fact $X$ is fibered over $G / G ^ { \prime }$ with the fiber $Y$ . The homotopic quotient spaces of $X$ and $Y$ coincide:

$$
X _ {G} = E G \times_ {G} (G \times_ {G ^ {\prime}} Y) = E G \times_ {G ^ {\prime}} Y = Y _ {G ^ {\prime}},
$$

and thus their equivariant cohomology is the same, but the module structure in $H _ { G } ^ { * } ( X )$ is induced from the module structure in $H _ { G ^ { \prime } } ^ { * } ( Y )$ by the natural map $B G ^ { \prime }  B G$ .

Let $p ^ { \prime \prime }$ be a basis of non-negative classes in $H ^ { 2 } ( G / G ^ { \prime } )$ lifted to $X$ , and $p = ( p ^ { \prime } , p ^ { \prime \prime } )$ be its extension to such a basis in $H ^ { 2 } ( X )$ . Encoding the homology class of a rational curve in $X$ by the string $( d ^ { \prime } , d ^ { \prime \prime } ) = ( d _ { 1 } , . . . , d _ { k } )$ of its degrees with respect to the dual basis in $H _ { 2 } ( X )$ , we find that the curves vertical in the bundle $X \to G / G ^ { \prime }$ have $d ^ { \prime \prime } = 0$ and vice versa.

This means that the quantum deformation ring $\mathbb { Z } [ q ^ { \prime } ]$ for $Y$ can be considered as a quotient of the corresponding ring for $X$ :

$$
\mathbb {Z} [ q ^ {\prime} ] = \mathbb {Z} [ q ^ {\prime}, q ^ {\prime \prime} ] / (q ^ {\prime \prime}).
$$

Remark. This identification may seem confusing, since the group algebra $\mathbb { C } [ q ^ { \prime \pm 1 } ]$ is a subalgebra in $\mathbb { C } [ q ^ { \pm 1 } ]$ . In fact, replacing the algebra $\mathbb { C } [ q ^ { \pm 1 } ]$ of functions on the torus by the polynomial algebra $\mathbb { C } [ q ]$ defines, in geometrical terms, partial compactification of the torus to $\mathbb { C } ^ { k }$ . Our description of $\mathbb { C } [ q ^ { \prime } ]$ as a quotient corresponds to the embedding of such a compactified torus $\mathbb { C } ^ { k ^ { \prime } }$ for $Y$ into the “boundary” $\mathbb { C } ^ { k } - ( \mathbb { C } - 0 ) ^ { k }$ of the torus for $X$ .

Denote $V ^ { \prime } ( z , q ^ { \prime } )$ and $V ( z , q )$ the generating volume functions for quantum equivariant cohomology of $Y$ and $X$ respectively. Then

$$
V (z, \left(q ^ {\prime}, 0\right)) = \text {D i r e c t} V ^ {\prime} (z, q ^ {\prime})
$$

where the direct image operation refers to the bundle $\pi : B G ^ { \prime } \to B G$ .

Indeed, when we evaluate $V ( z , q )$ on some cycle $C \subset B G$ at $q ^ { \prime \prime } = 0$ we simply calculate weighted volume of the space of vertical algebraic loops in $X _ { G }$ over $C$ but throw away contributions of all rational curves with $d ^ { \prime \prime } \ne 0$ . But a rational curve in $X$ with $d ^ { \prime \prime } = 0$ projects to $G / G ^ { \prime }$ to a point. This means that the LHS actually computes weighted volume of the space of vertical algebraic loops in $Y _ { G ^ { \prime } } \longrightarrow B G ^ { \prime } \longrightarrow B G$ over the preimage $C ^ { \prime } = \pi ^ { - 1 } C$ . Therefore

$$
V (z, (q ^ {\prime}, 0)) [ C ] = V ^ {\prime} (z, q ^ {\prime}) [ C ^ {\prime} ] = [ \mathrm {D i r e c t i m a g e} V ^ {\prime} (z, q ^ {\prime}) ] [ C ]
$$

by the very definition of the direct image operation.

# 3.7 Equivariant Floer homology

We briefly discuss here quantum equivariant cohomology from the point of view of Morse-Floer theory on loop spaces. This discussion is supposed to motivate our conjecture that the general properties expected from quantum cohomology can be naturally generalized to the equivariant case.

Let $X$ , as above, be a compact simply-connected Kahler manifold provided with a holomorphic action of the complexified compact Lie group $G _ { \mathbb { C } }$ and and with a $G$ -invariant Kahler form. The group $G _ { \mathbb { C } }$ also acts by holomorphic transformations on the loop space $L X$ and its universal covering. Since the action functional $\mathcal { A }$ on the covering is $G$ -invariant one can try to construct the equivariant Floer (co)homology $F H _ { G } ^ { * } ( X )$ by means of equivariant Morse-Witten theory for $\mathcal { A }$ .

Usually one defines an equivariant Morse chain complex using finite-dimensional approximations $E G _ { N }  B G _ { N }$ of the universal $G$ -bundle. For example, if $G$ is the unitary group $U _ { n }$ one can choose the complex Grassmann manifold $G r ( N , n )$ on the role of $_ { B G }$ and the corresponding Stiefel manifold on the role of $E G _ { N }$ . Mimicking this approach, we can extend the functional $\mathcal { A }$ to the space $E G _ { N } \times L X$ in the trivial manner and thus construct a functional $A _ { N }$ on the manifold $L _ { N } = E G _ { N } \times _ { G } L X$ approximating the homotopic quotient space $( L X \ ) _ { G }$ . Now we can apply Floer’s semi-infinite Morse theory to the functionals $\mathcal { A } _ { N }$ . Notice that the homotopic quotient $( L X ) _ { G }$ is nothing but the space of vertical loops in the bundle $X _ { G } \to B G$ , and $L _ { N }$ is simply its restriction to $B G _ { N } \subset B G$ .

Taking care of the riemannian metric, add a $G$ -invariant riemannian metric on $E G N$ as a direct summand to the Kahler $G$ -invariant metric on $L X$ induced from that on $X$ . Then the gradient vector field of $\mathcal { A }$ on $E G _ { N } \times L X$ is tangent to the second factor and is invariant with respect to the diagonal action of $G$ . This means that the gradient vector field of $A _ { N }$ relative to the factor-metric on $L _ { N }$ is just the projection of that $G$ -invariant field, and the corresponding gradient flow consists in fiberwise analytic continuation of vertical loops in the $X$ -bundle $L _ { N } \to B G _ { N }$ . In particular, Floer cohomology of $L _ { N }$ will carry a module structure over the ordinary cohomology algebra of $B G N$ .

Notice that the $G$ -action on $L X$ commutes with both the circle action (= reparametrization of loops) and the action of the covering transformation group $\mathbb { Z } ^ { k }$ (so that both actions survive on $L _ { N }$ ). The first implies that $\mathcal { A } _ { N }$ is a perfect Morse-Bott function on $L _ { N }$ (see [G],[G1]). The second describes the action of the group ring $\mathbb { Z } [ q ^ { \pm 1 } ]$ on the Floer cohomology of $L _ { N }$ , which is therefore additively isomorphic to the cohomology $H ^ { * } ( ( X _ { G } ) _ { N } , \mathbb { Z } [ q ^ { \pm 1 } ] )$ of the critical point set.

Passing to the limit $N \to \infty$ , we conclude that $G$ -equivariant Floer cohomology $F H _ { G } ^ { * } ( X )$ of $L X$ should be a $H _ { G } ^ { * } ( p t , \mathbb { Z } [ q ^ { \pm 1 } ] )$ -module canonically isomorphic to the equivariant cohomology of $X$ with coefficients in the group ring $\mathbb { Z } [ q ^ { \pm 1 } ]$ .

A multiplicative structure in equivariant quantum cohomology of $L X$ can be defined by means of the evaluation map at the point $1 \in S ^ { 1 }$ :

$$
L X \to (L X \times X), (\gamma : S ^ {1} \to X) \mapsto (\gamma , \gamma (1)).
$$

This map is $G$ -equivariant and induces an action of equivariant cohomology classes of $X$ by module endomorphisms on equivariant Floer cohomology $F H _ { G } ^ { * } ( X )$ of the loop space $L X$ . Using

our explicit description of the gradient flow on $( L X ) _ { G }$ as fiberwise analytic continuation of loops, one can compute this action in terms of vertical holomorphic curves and quantum equivariant intersection indices $\langle | \ldots | \rangle$ introduced in 3.3. Namely the action of $p \in H _ { G } ^ { * } ( X )$ on $a \in F H _ { G } ^ { * } ( X )$ satisfies

$$
\langle p * a, b \rangle = \langle a | p | b \rangle
$$

for any $b \in F H _ { G } ^ { * } ( X )$ where the pairing on the LHS is the classical equivariant intersection index on $H _ { G } ^ { * } ( X , \mathbb { Z } [ q ^ { \pm 1 } ] )$ with values in $H _ { G } ^ { * } ( p t , \mathbb { Z } [ q ] )$ .

The multiple quantum equivariant intersection indices $\langle a | p _ { 1 } | . . . | p _ { r } | b \rangle$ can be expressed in a similar manner in terms of evaluation maps $L X \to L X \times X ^ { r }$ at $r$ distinct points $x _ { 1 } , . . . , x _ { r }$ on the circle $S ^ { 1 }$ . We conjecture that they satisfy the “principal axiom” of Topological Field Theory (see 2.2). This conjecture implies that the multiple intersection indices represent matrix elements of compositions of the endomorphisms corresponding to $p _ { 1 } , . . . , p _ { r } \in H _ { G } ^ { * } ( X )$ . Finally, if one defines quantum equivariant cohomology of $Q H ^ { * } ( X )$ as the algebra generated by these endomorphisms and operators of multiplication by $q$ , then our conjecture means that this algebra

• is additively isomorphic to $H _ { G } ^ { * } ( X , \mathbb { Z } [ q ] )$ (or may be “[[q]]”),   
• provides a “quantum” deformation of the classical equivariant cohomology algebra $H _ { G } ^ { * } ( X )$   
• inherits the module structure over $H _ { G } ^ { * } ( p t ) \otimes \mathbb { Z } [ q ]$ , and   
• allows to express the multiple pairings through quantum multiplication and the classical direct image functional:

$$
\langle p _ {1} | \dots | p _ {r} \rangle = \langle p _ {1} \dots p _ {r}, [ 1 ] \rangle .
$$

It is difficult to say now whether a rigorous justification of these hypotheses should be even more sophisticated than in the non-equivariant case. One one hand, general position arguments should require introducing almost complex structures on $X$ which are not $G$ -invariant. The most natural way to handle this problem — by considering the space $\mathcal { I }$ of all almost complex structures and constructing $G$ -equivariant Floer cohomology of $L X \times \mathcal { I }$ — involves one more “infinity” and seems to raise the level of technical difficulty. On the other hand, the finite-dimensional approximations $B G N$ of classifying spaces have Kahler models, and quantum equivariant cohomology of $X$ seem to be expressible in terms of non-equivariant quantum cohomology of the approximations $( X _ { G } ) _ { N }  B G _ { N }$ : it suffices to “throw away” contributions of non-vertical rational curves in $( X _ { G } ) _ { N }$ , i. e. put some of $q$ ’s equal zero. This approach can possibly reduce the problem back to the axioms of non-equivariant Topological Field Theory.

We are not ready to discuss further this problem here. We also leave for the reader to think out the parallel construction of equivariant quantum multiplication which is based on composition of loops.

# 3.8 Characteristic classes as Casimir functions

Here we interpret the quantum equivariant cohomology algebra $Q H _ { G } ^ { * } ( X )$ as the algebra of functions on some lagrangian variety in the assumption that the ordinary cohomology algebra $H ^ { * } ( X )$ of the simply-connected Kahler manifold $X$ is generated by non-negative $( 1 , 1 )$ -classes $p 1 , . . . , p _ { k }$ (in

notations of 2.3). This assumption along with the spectral sequence of the $X$ -bundle $X _ { G } \to B G$ implies that the equivariant cohomology algebra $H _ { G } ^ { * } ( X )$ is additively isomorphic to $H ^ { * } ( B G ) \otimes$ $H ^ { * } ( X )$ and is generated, as an $H _ { G } ^ { * } ( p t )$ -algebra, by $k$ elements representing $1 \otimes p _ { i }$ which we will denote $p 1 , . . . , p _ { k }$ again.

Its quantum deformation $Q H _ { G } ^ { * } ( X )$ has been defined in 3.7 by means of the identity

$$
\langle a * b, c \rangle = \langle a | b | c \rangle .
$$

Considered as $H _ { G } ^ { * } ( p t )$ -algebra, it is generated by $( p _ { 1 } , . . . , p _ { k } , q _ { 1 } , . . . , q _ { k } )$ and is therefore isomorphic to the quotient of the polynomial algebra $H _ { G } ^ { * } ( p t ) [ p , q ] ]$ by some ideal of relations.

Passing to complex coefficients and introducing temporary notations $c _ { i }$ , $i = 1 , . . . , r$ , for generators of the polynomial algebra $H ^ { * } ( p t , \mathbb { C } ) = \mathbb { C } [ c ]$ of $G$ -characteristic classes, we interpret the quantum equivariant cohomology algebra $Q H _ { G } ^ { * } ( X , \mathbb { C } )$ as the algebra of regular functions on a (quasi-homogeneous) subvariety $\mathcal { L }$ determined by the ideal of relations $\mathcal { T }$ in the complex space with coordinates

$$
\left(p _ {1}, \dots , p _ {k}, q _ {1}, \dots , q _ {k}, c _ {1}, \dots , c _ {r}\right).
$$

This complex space has a natural Poisson structure

$$
q _ {1} \frac {\partial}{\partial q _ {1}} \wedge \frac {\partial}{\partial p _ {1}} + \dots + q _ {k} \frac {\partial}{\partial q _ {k}} \wedge \frac {\partial}{\partial p _ {k}}
$$

due to the constant coefficient pairing between $H ^ { 2 } ( X ) = H ^ { 2 } ( X _ { G } ) / H ^ { 2 } ( B G )$ and $\mathbb { Z } ^ { k } = H _ { 2 } ( X ) \subset$ $H _ { 2 } ( X _ { G } )$ (we assume of course that the basis in the lattice $\mathbb { Z } ^ { k }$ is dual to the basis $( p _ { 1 } , . . . , p _ { k } )$ in $H ^ { 2 } ( X )$ ).

We observe that the characteristic classes $c _ { i }$ play the role of Casimir functions of such a Poisson structure and claim that the characteristic variety $\mathcal { L }$ is lagrangian in the sense of Poisson geometry, i. e. its intersections with the symplectic leaves ${ \vec { c } } = c o n s t$ , $q _ { 1 } . . . q _ { k } \neq 0$ are lagrangian at their regular points.

Similarly to the non-equivariant case 2.3, this statement is based on the properties of the matrix-valued differential 1-form $A = \textstyle \sum ( p _ { i } * ) ( d q _ { i } ) / q _ { i }$ to satisfy $d A = 0 , A \land A = 0$ , but now the Casimir functions $c _ { i }$ are treated by the differential $d$ and by the operators $p _ { i } *$ as constants. Mimicking 2.3, we introduce a $\mathbb { C } [ [ c , q ] ]$ -valued bilinear form on $H _ { G } ^ { * } ( X , \mathbb { C } [ [ q ] ] )$ by the formula

$$
S _ {a, b} | _ {[ C ]} = \sum \quad \pm q ^ {d}
$$

degree $d$ isolated vertical rational curves

in $X _ { G } \to B G$ restricted to $C \subset B G$

with two marked points in a and b

which evaluates the bilinear form of two finite codimension cycles $a , b \subset X _ { G }$ on a finite-dimensional cycle $C \subset B G$ .

Thinking of $c _ { i }$ as of the preimage in $X _ { G }$ of a finite-codimension cycle in $_ { B G }$ we immediately conclude that $S$ is $\mathbb { C } [ c ]$ -bilinear:

$$
S _ {c _ {i} a, b} | _ {[ C ]} = S _ {a, b} | _ {[ c _ {i} \cap C ]} = (c _ {i} S _ {a, b}) | _ {[ C ]}.
$$

Thinking of $p _ { i }$ as a complex hypersurface in $X _ { G }$ we find, as in 2.3, that

$$
S _ {a, b} + \sum \langle a, p _ {i}, b \rangle \log (q _ {i})
$$

is a potential for the $( a , b )$ -matrix element of the 1-form $A$ :

$$
q _ {i} \frac {\partial}{\partial q _ {i}} S _ {a, b} = \langle a | p _ {i} | b \rangle - \langle a, p _ {i}, b \rangle .
$$

This is equivalent to $d A = 0$ and together with commutativity $A \land A = 0$ and the lemma in 2.3 implies that each non-singular branch of $\mathcal { L } \cap \{ \vec { c } = c o n s t \}$ over the torus with coordinates $q$ is lagrangian in the cotangent bundle of this torus (= the symplectic leaf with coordinates $p , q$ ).

# 4 Computation of $Q H _ { U _ { n } } ^ { * } ( F _ { n } )$

In this section, we compute quantum (equivariant) cohomology of flag manifolds. The results here are mathematically rigorous corollaries of the following conjectures about general properties of quantum cohomology of Kahler manifolds:

Quantum equivariant cohomology is a skew-commutative associative algebra over the characteristic class ring;   
• It is a weighted-homogeneous $q$ -deformation of the classical equivariant cohomology;   
• Equivariant generating volume functions satisfy the product, restriction and induction properties from 3.6.

# 4.1 Root systems

The structure of the 2-nd (co)homology lattice of flag manifolds can be understood better in terms of root systems. The flag manifold $F _ { n }$ is the space $G _ { \mathbb { C } } / B$ of all Borel subalgebras in ${ \mathfrak { g } } _ { \mathbb { C } } = { \mathfrak { s l } } _ { \mathfrak { n } } ( \mathbb { C } )$ . Therefore its tangent bundle splits canonically into the direct sum of line bundles $\mathbb { \oplus _ { \alpha } } L _ { \alpha }$ indexed by positive roots $\alpha$ of the root system $A _ { n - 1 }$ . Recall that this root system can be described as the set of linear functions $x _ { i } - x _ { j }$ on the lattice $\mathbb { Z } ^ { n }$ with coordinates $x _ { 1 } , . . . , x _ { n }$ , and the positive roots are those with $i < j$ . The $n - 1$ -dimensional lattice spanned by the roots can be identified with a finite index sublattice in the 2-nd cohomology group $H ^ { 2 } ( F _ { n } )$ by the map

a line bundle $\longmapsto$ its 1-st Chern class.

Therefore the 1-st Chern class of the flag manifold is represented by the total sum $2 \rho$ of positive roots. According to Borel-Weil theory, finite-dimensional representations of $S U _ { n }$ can be realized in spaces of holomorphic sections of non-negative line bundles over $F _ { n }$ and correspond in a $1 -$ 1 fashion to their 1-st Chern classes. This theory implies that the Kahler cone of $F _ { n }$ is the Weyl chamber spanned by the 1-st Chern classes $p _ { 1 } , . . . , p _ { n - 1 }$ of the fundamental line bundles $\operatorname* { d e t } ^ { * } \Lambda ^ { i } \mathbb { C } ^ { n } , i = 1 , . . . , n - 1$ , called — in terms of the root system — fundamental weights.

The fundamental weights $p _ { i } = x _ { 1 } + . . . + x _ { i } , i = 1 , . . . , n - 1$ , form a basis in the lattice $H ^ { 2 } ( F _ { n } )$ . The vectors $\alpha _ { 1 } , . . . , \alpha _ { n - 1 }$ of the dual basis and their non-negative integer combinations represent, in

the homology group $H _ { 2 } ( F _ { n } )$ , classes of holomorphic curves in $F _ { n }$ . Identifying the space $H ^ { * } ( F _ { n } , \mathbb { Q } )$ with its dual by means of the Weyl-invariant inner product (the Cartan matrix is its matrix in the basis of fundamental weights) we find that $\left( \alpha _ { 1 } , . . . , \alpha _ { n - 1 } \right)$ becomes the basis of simple roots $\alpha _ { i } = x _ { i } - x _ { i + 1 }$ under this identification.

Now the famous identity

$$
\sum_ {\alpha > 0} \alpha = 2 \rho = 2 (p _ {1} + \ldots + p _ {n - 1})
$$

along with $\langle p _ { i } , \alpha _ { j } \rangle = \delta _ { i j }$ means that in our representation of classes $\sum d _ { i } \alpha _ { i }$ of rational curves by monomials $q _ { 1 } ^ { d _ { 1 } } . . . q _ { n - 1 } ^ { d _ { n - 1 } }$ the degrees of the variables $q _ { i }$ are

$$
\deg q _ {i} = c (\alpha_ {i}) = \langle 2 \rho , \alpha_ {i} \rangle = 2.
$$

# 4.2 Auxiliary bundle

According to general theory,

$$
Q H _ {U _ {N}} ^ {*} (F _ {n}) = \mathbb {Z} [ u _ {1}, \dots , u _ {n}, q _ {1}, \dots , q _ {n - 1}, c _ {1}, \dots , c _ {n} ] / I _ {U _ {n}}
$$

where the ideal $I _ { U _ { n } }$ is generated by some quasi-homogeneous $q$ -deformation of the relations

$$
c _ {i} = \sigma_ {i} (u), i = 1, \dots , n, \quad \deg u _ {i} = 1, \deg c _ {i} = i, \deg q _ {i} = 2
$$

which can be written (using a formal variable $\lambda$ of degree 1) as a single quasi-homogeneous identity of degree $n$ :

$$
(u _ {1} + \lambda) \dots (u _ {n} + \lambda) = \lambda^ {n} + \sigma_ {1} \lambda^ {n - 1} + \dots + \sigma_ {n}.
$$

We find this deformation by induction on $n = 2 , 3 , 4 . . .$ ., based on the following obvious

Lemma 1. For $n > 2$ , suppose that a quasi-homogeneous relation of the form

$$
(u _ {0} + \lambda) \dots (u _ {n} + \lambda) - [ \lambda^ {n} + \sigma_ {1} \lambda^ {n - 1} + \dots + \sigma_ {n} ] = O (q _ {1}, \dots , q _ {n - 1}) [ \lambda , q, u, \sigma ]
$$

is satisfied in quantum equivariant cohomology algebra of the flag manifold $F _ { n }$ modulo $q _ { i }$ for each $i = 1 , . . . , n - 1$ . Then this relation holds identically (i. e. for all $q$ ).

Proof. Indeed, since the LHS of the relation in question is homogeneous of degree $n$ , the hypothesis of Lemma 1 means that the difference $L H S - R H S$ is divisible by $q _ { 1 } . . . q _ { n - 1 }$ . But $\deg q _ { i } = 2$ and

$$
\deg q _ {1} \dots q _ {n - 1} = 2 n - 2 > n \text {f o r} n > 2.
$$

This implies that $L H S - R H S = 0$ .

Remark. This lemma is the only place in our proof where we use some specificity of the group $U _ { n }$ . It also holds for flag manifolds of series $C$ and $D$ but fails for other compact simple Lie groups. For their flag manifolds one can easily give a hypothetical description of the quantum equivariant cohomology algebras in terms of generalized Toda lattices, but a proof should involve some additional argument.

Our inductive step will make use of the following construction. Consider the subgroup $G ^ { \prime } =$ $U _ { m } \times U _ { n - m } \subset U _ { n } = G$ and the $G ^ { \prime }$ -space $Y = F _ { m } \times F _ { n - m }$ . The induced $G$ -space (in the sense of 3.6) is nothing but the flag manifold $F _ { n }$ . Its fibration over $G / G ^ { \prime } = G r ( n , m )$ sends a flag in $\mathbb { C } ^ { n }$ to its $m$ -dimensional component.

Let $V _ { m }$ denote generating volume function for quantum equivariant cohomology of $F _ { m }$ .

# Lemma 2.

$$
V _ {n} (z, q, c) | _ {q _ {m} = 0} = D i r e c t i m a g e \left[ V _ {m} (z ^ {\prime}, q ^ {\prime}, c ^ {\prime}) \cdot V _ {n - m} (z ^ {\prime \prime}, q ^ {\prime \prime}, c ^ {\prime \prime}) \right]
$$

where

$\boldsymbol { z } ~ = ~ ( z _ { 1 } , . . . , z _ { n } )$ are coordinates on $H ^ { 2 } ( ( F _ { n } ) _ { G } )$ with respect to the basis $u _ { 1 } , . . . , u _ { n }$ (see 3.2), $z ^ { \prime } = ( z _ { 1 } , . . . , z _ { m } ) , z ^ { \prime \prime } = ( z _ { m + 1 } , . . . , z _ { n } )$ ,

$$
q = \left(q ^ {\prime}, q _ {m}, q ^ {\prime \prime}\right) = \left(q _ {1},..., q _ {m},..., q _ {n - 1}\right),
$$

c, $c ^ { \prime }$ and $c ^ { \prime \prime }$ are Chern classes of $U _ { n }$ , $U _ { m }$ and $U _ { n - m }$ respectively, and “Direct image” refers to the direct image operation $\mathbb { Z } [ c ^ { \prime } , c ^ { \prime \prime } ] = H ^ { * } ( B G ^ { \prime } )  H ^ { * } ( G ) = \mathbb { Z } [ c ]$ for the bundle $B G ^ { \prime }  B G$ with the fiber $G r ( n , m )$ (see 3.3).

Proof. It is a straightforward corollary of the product and induction formulas: factorization $( F _ { n } ) _ { U _ { n } } = ( F _ { m } ) _ { U _ { m } } \times ( F _ { n - m } ) _ { U _ { n - m } }$ identifies the basis $\left( u _ { 1 } , . . . , u _ { n } \right)$ in the 2-nd equivariant cohomology of the product with the union $( u _ { 1 } ^ { \prime } , . . . , u _ { m } ^ { \prime } , u _ { 1 } ^ { \prime \prime } , . . . , u _ { n - m } ^ { \prime \prime } )$ of such basises of factors since both are the standard generator sets in the cohomology of $( \mathbb { C } P ^ { \infty } ) ^ { n }$ , and $p _ { m } \in H ^ { 2 } ( F _ { n } )$ is represented by the 1-st Chern class of the determinant line bundle over $G r ( n , m )$ and therefore the vertical rational curves in $F _ { n } \longrightarrow G r ( n , m )$ are exactly those with $d _ { m } = 0$ .

# 4.3 Theorem 2 implies Theorem 1

Indeed, according to the restriction property of equivariant generating volume functions (applied to the trivial subgroup in $U _ { n }$ ), if a relation

$$
R (\partial / \partial z, q, c) V (z, q, c) = 0
$$

is satisfied, then $R ( \partial / \partial z , q , 0 )$ annihilates the non-equivariant generating volume function $V ( z , q , 0 )$ and thus the relation $R ( u , q , 0 ) = 0$ holds in $Q H ^ { * } ( F _ { n } )$ . This proves

Lemma 3.

$$
Q H ^ {*} (F _ {n}) = Q H _ {U _ {n}} ^ {*} (F _ {n}) / (c _ {1}, \dots , c _ {n}).
$$

# 4.4 Equivariant quantum cohomology of $\mathbb { C } P ^ { 1 }$

Lemma 4.

$$
Q H _ {G} ^ {*} (\mathbb {C} P ^ {1}) = \mathbb {Z} [ u _ {1}, u _ {2}, q, c _ {1}, c _ {2} ] / (u _ {1} + u _ {2} = c _ {1}, u _ {1} u _ {2} + q = c _ {2})
$$

Proof. Quantum equivariant cohomology of the projective line $F _ { 2 }$ is isomorphic to the quotient algebra of $\mathbb { Z } [ u _ { 1 } , u _ { 2 } , q , c _ { 1 } , c _ { 2 } ]$ by the ideal generated by quantum deformations of the relations $u _ { 1 } + u _ { 2 } = c _ { 1 } , u _ { 1 } u _ { 2 } = c _ { 2 }$ in the classical equivariant cohomology. These deformations can be taken

quasi-homogeneous and since $\deg q = 2$ , the only possible deformation should replace the RHS in $u _ { 1 } u _ { 2 } - c _ { 2 } = 0$ with a scalar multiple of $q$ .

In order to determine the scalar it suffices to reduce the relations modulo $( c _ { 1 } , c _ { 2 } )$ , i. e. to compare, by Lemma 3, with relations in the ordinary, non-equivariant quantum cohomology of $F _ { 2 } = \mathbb { C } P ^ { 1 }$ . Then $u _ { 2 } = - u _ { 1 }$ represents the 1-st Chern class of the “hyperplane” bundle over $\mathbb { C } P ^ { 1 }$ , i. e. simply a point. Since the relation $u _ { 2 } ^ { 2 } = q$ holds in the quantum cohomology of $\mathbb { C } P ^ { 1 }$ (see 2.7), the scalar coefficient we are looking for equals 1.

# 4.5 Step of induction

Denote

$$
D _ {n} (u, q, \lambda) = \det  (A _ {n - 1} + \lambda)
$$

the characteristic polynomial of the $n \times n$ -matrix with $u _ { 1 } , . . . , u _ { n }$ on the diagonal, $q _ { 1 } , . . . , q _ { n - 1 }$ right above and $- 1 , . . . , - 1$ right under the diagonal.

Lemma 5. Suppose that the relation

$$
D _ {k} (u, q, \lambda) = \lambda^ {k} + c _ {1} \lambda^ {n - 1} + \dots + c _ {k}
$$

is satisfied identically in $\lambda$ in the equivariant quantum cohomology of flag manifolds $F _ { k }$ for all $k < n$ . Then the relation with $k = n$ is also satisfied modulo $q _ { m }$ for every $m = 1 , . . . , n - 1$ .

Proof. First of all, notice that $D _ { n } | _ { q _ { m } = 0 } = D _ { m } ( u ^ { \prime } , q ^ { \prime } , \lambda ) D _ { n - m } ( u ^ { \prime \prime } , q ^ { \prime \prime } , \lambda )$ where $( u ^ { \prime } , u ^ { \prime \prime } ) =$ $u , ( q ^ { \prime } , 0 , q ^ { \prime \prime } ) = q$ .

Denote

$$
\Sigma_ {n} = \lambda^ {n} + c _ {1} \lambda^ {n - 1} + \dots + c _ {n} = (x _ {1} + \lambda) \dots (x _ {n} + \lambda)
$$

the RHS of the above relation with the Chern classes $c _ { 1 } , . . . , c _ { n }$ written for convenience as elementary symmetric functions of the formal variables $x _ { 1 } , . . . , x _ { n }$ . The conclusion of Lemma 5 means that

$$
\left[ D _ {n} (\partial / \partial z, q, \lambda) - \Sigma_ {n} (x, \lambda) \right] V _ {n} (z, q, \sigma (x)) | _ {q _ {m} = 0} = 0.
$$

It is the same as

$$
[ D _ {m} (\frac {\partial}{\partial z ^ {\prime}}, q ^ {\prime}, \lambda) D _ {n - m} (\frac {\partial}{\partial z ^ {\prime \prime}}, q ^ {\prime \prime}, \lambda) - \Sigma_ {n} (x, \lambda) ] [ V _ {n} ((z ^ {\prime}, z ^ {\prime \prime}), (q), \sigma (x)) | _ {q _ {m} = 0} ] = 0.
$$

By Lemma 2, the function ${ \cal V } _ { n } | _ { q _ { m } = 0 }$ in the last formula can be replaced with the Direct image of

$$
V _ {m} \left(z ^ {\prime}, q ^ {\prime}, \sigma \left(x ^ {\prime}\right)\right) \cdot V _ {n - m} \left(z ^ {\prime \prime}, q ^ {\prime \prime}, \sigma \left(x ^ {\prime \prime}\right)\right),
$$

explicitly described in 3.3.

Since the derivations in $D _ { m } D _ { n - m }$ are with respect to $z ^ { \prime } , z ^ { \prime \prime }$ which are not involved into permutations in the operation $A l t$ , and the variables $x ^ { \prime } , x ^ { \prime \prime }$ which are involved do not show up in coefficients of the operators $D _ { m } , D _ { n - m }$ , the Direct image operation commutes with our differential operator.

Applying the inductive assumption we find that the conclusion of the proposition is equivalent to the identity

$$
\Sigma_ {n} (x, \lambda) \text {D i r e c t i m a g e} \left[ V _ {m} \left(x ^ {\prime}\right) V _ {n - m} \left(x ^ {\prime \prime}\right) \right] =
$$

$$
= \mathrm {D i r e c t i m a g e} [ (\Sigma_ {m} (x ^ {\prime}, \lambda) V _ {m} (x ^ {\prime})) (\Sigma_ {n - m} (x ^ {\prime \prime}, \lambda) V _ {n - m} (x ^ {\prime \prime})) ].
$$

But

$$
\Sigma_ {m} (x ^ {\prime}, \lambda) \Sigma_ {n - m} (x ^ {\prime \prime}, \lambda) = (x _ {1} + \lambda)... (x _ {n} + \lambda) = \Sigma_ {n} (x, \lambda)
$$

is totally symmetric in $( x _ { 1 } , . . . , x _ { n } ) !$ .

Since multiplication by a symmetric function commutes with the alternation operation, we conclude that the required identity does hold.

Combining Lemma 5 with Lemma 1 completes the proof of Theorem 2 from Introduction.

# 4.6 Volume functions

We have found the relations in quantum cohomology of flag manifolds using general properties of generating volume function. Now we compute the quantum volume functions using our knowledge of the relations and of the classical volume functions.

Proposition.The quantum equivariant generating volume function $V _ { n } ( z , q , c )$ of the flag manifold $F _ { n }$ equals

$$
W _ {n} = \frac {1}{(2 \pi i) ^ {n}} \int \frac {\exp (z , u) d u _ {1} \wedge \ldots \wedge d u _ {n}}{(\Sigma_ {1} (u , q) - c _ {1}) . . . (\Sigma_ {n} (u , q) - c _ {n})}
$$

where $\Sigma _ { i } ( u , q )$ are the quantum deformations of elementary symmetric functions i. e. the coefficients of the polynomial $\operatorname* { d e t } ( A _ { n - 1 } + \lambda )$ .

Proof. By the deformation property and Proposition in 3.2, the formula holds for $q = 0$ . We will prove the formula using the homogeneity property $\deg V _ { n } = - \dim F _ { n }$ (where $\deg z _ { i } =$ $- 1 , \deg q _ { i } = 2 , \deg c _ { i } = i ,$ ) and the differential equations

$$
\Sigma_ {i} (\partial / \partial z, q) V _ {n} (z, q, c) = c _ {i} V _ {n} (z, q, c), i = 1, \dots , n.
$$

First of all, the function $W _ { n }$ does satisfy the homogeneity condition and the differential equations (due to the famous property of residues).

Due to another property of residues (see [GH]) $W _ { n }$ is an analytic function of its variables and can be expanded into a power series ( $V _ { n }$ is a formal series by definition). Represent the difference $V _ { n } - W _ { n }$ as a sum $\begin{array} { r } { \sum _ { d \geq 0 , l \geq 0 } R _ { d , l } ( z ) q ^ { d } c ^ { l } } \end{array}$ . The coefficient $R _ { d , l }$ is a homogeneous polynomial in $z$ of degree (in the usual sense) $\dim { F _ { n } } + \sum 2 d _ { i } + \sum j l _ { j }$ and $R _ { 0 , 0 } = 0$ since $V _ { n }$ coincides with $W _ { n }$ at $q = 0$ .

Let us pick $R$ as the coefficient of minimal degree among non-zero $R _ { d , l }$ . The differential equations for $V - W$ mean that

$$
\sigma_ {i} (\partial / \partial z) R (z) = \mathrm {s o m e o p e r a t o r s a p p l i e d t o} R _ {d, l} \mathrm {w i t h s m a l l e r} d, l
$$

and hence that $\sigma _ { i } ( \partial / \partial z ) R ( z ) = 0 , i = 1 , . . . , n$ , since all those $R _ { d , l }$ are zeroes. Now the following lemma completes the proof.

Lemma 6.If all symmetric differential polynomials $S ( \partial / \partial z )$ in n variables annihilate a polynomial $R ( z )$ , then $\deg R \leq \dim F _ { n }$ .

Proof. The quotient of the algebra of all differential polynomials $S ( \partial / \partial z )$ by the ideal generated by elementary symmetric functions is canonically isomorphic to the cohomology algebra $H ^ { * } ( F _ { n } )$ . This implies that the ideal containes the power $\mathfrak { m } ^ { \dim \mathfrak { F } _ { \mathfrak { n } } + \mathbf { 1 } }$ of the maximal ideal ${ \mathfrak { m } } = ( \partial / \partial _ { 3 1 } , . . . , \partial / \partial _ { \mathfrak { z } { \mathfrak { n } } } )$ . This means that all derivatives of $R$ of order $> \dim { F _ { n } }$ $>$ vanish and thus $\deg R \leq \dim F _ { n }$ .

Proposition also implies Theorem 3 from Introduction (describing quantum intersection indices), since by definition of $V _ { n }$

$$
\langle f | g \rangle = [ f (\partial / \partial z) g (\partial / \partial z) V _ {n} (z, q, c) ] | _ {z = 0}.
$$

# References

[A] M.Atiyah, Convexity and commuting hamiltonians. Bull. Lond. Math. Soc. 23 (1982), 1–15.   
[AB] M.Atiyah, R.Bott, The moment map and equivariant cohomology. Topology 23 (1984), 1–28.   
[CV] S.Cecotti, C.Vafa, Exact results for supersymmetric sigma models. Preprint HUTP-91/A062.   
[D] B.Dubrovin, Integrable systems in topological field theory. Nucl. Phys. B379 (1992), 627– 685.   
[FF] B.Feigin, E.Frenkel, Integrals of motion and quantum groups. Preprint, 1993.   
[F1] A.Floer, Morse theory and lagrangian intersections. J. Diff. Geom. 28 (1988), 513–547.   
[F2] A.Floer,Symplectic fixed points and holomorphic spheres. Commun.Math.Phys. 120 (1989), 575–611.   
[G] V.A.Ginsburg Equivariant cohomology and Kahler geometry. Funct. Anal. Appl. 21:4 (1987), 271–283.   
[G1] A.Givental, Periodic mappings in symplectic topology. Funct. Anal. Appl. 23:4 (1989), 287–300.   
[G2] A.Givental, A symplectic fixed point theorem for toric manifolds. To appear in: Progress in Math., v. 93, Birhauser, Basel.   
[G3] A.Givental, A mirror theorem for complex projective spaces., in preparation.   
[GH] P.Griffits, J.Harris, Principles of algebraic geometry. Wiley, N.Y., 1978.   
[Gr] M.Gromov, Pseudo-holomorphic curves in almost complex manifolds. Invent. Math. 82:2 (1985), 307–347.   
[HS] H.Hofer, D.Salamon, Floer homology and Novikov rings. Preprint, 1992.

[K] M.Kontsevich, $A ^ { \infty }$ -algebras in mirror symmetry. Preprint, 1993.   
[O] K.Ono, On the Arnold conjecture for weakly monotone symplectic manifolds. Preprint, 1993.   
[R] A.Reyman, Hamiltonian systems related to graded Lie algebras. in: Diff. Geom., Lie groups and Mechanics, III Zapiski Nauchn. Sem. LOMI, v. 95, Nauka, 1980 (in Russian).   
[Ru] Y.Ruan, Topological sigma model and Donaldson type invariants in Gromov theory. Preprint.   
[S] V.Sadov, On equivalence of Floer’s and quantum cohomology. Preprint HUTP-93/A027.   
[V] C.Vafa,Topological mirrors and quantum rings. in: S.-T. Yau (Ed.), Essays on mirror manifolds. International Press Co., Hong Kong, 1992.   
[Vt] C.Viterbo, The cup-product on the Thom–Smale–Witten complex, and Floer cohomology. To appear in: Progress in Math., v. 93, Birkhauser, Basel.   
[W] E.Witten, Two-dimensional gravity and intersection theory on moduli space. Surveys in Diff. Geom. 1 (1991), 243–310.   
[W2] E.Witten, Supersymmetry and Morse theory. J. Diff. Geom. 17 (1982), 661–692.