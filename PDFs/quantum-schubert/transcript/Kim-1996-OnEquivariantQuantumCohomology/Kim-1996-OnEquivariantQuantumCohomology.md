# On Equivariant Quantum Cohomology

Bumsig Kim∗

8-2-96

# 1 Introduction

There is exactly one straight line passing through any two given distinct points; there is exactly one quadratic curve on the complex projective plane passing through 5 given generic points ... One can formulate many similar enumerative problems about compact holomorphic curves in K¨ahler manifolds, and some of such problems have been subject to intensive study by algebraic geometers since the last century. Recently it was found that answers to these questions give rise to symplectic invariants of the manifolds. First, Gromov [11] suggested to use pseudo-holomorphic curves in symplectic manifolds in order to distinguish equivalence classes of symplectic structures. Then Floer [7] applied this idea to Arnold’s fixed point conjecture [1] and introduced what is called now the quantum cohomology algebra of a symplectic manifold. Eventually, when the ideas of symplectic topology merged with those of conformal field theory, it became clear that various Gromov – Witten invariants of symplectic manifolds responsible for enumeration of holomorphic curves can be actually calculated within the quantum cohomology algebras. Thus numerous enumerative questions were reduced to computation of the quantum cohomology algebras themselves.

The quantum cohomology algebra of a given compact K¨ahler manifold $X$ is, by definition, the cohomology space of the manifold provided with a new multiplication. Given three cohomology classes represented by cycles $a , b , c$ Poincar´e-dual to them, one can think of the structural constants <

$a \cdot b , c >$ of the ordinary cup-product as of the number of points of transversal intersection $a \cap b \cap c$ counted with appropriate signs. Similarly, the structural constant $< a * b , c >$ of the quantum multiplication can be understood as the algebraic number of isolated solutions to the following enumerative problem:

find the number of holomorphic maps $\mathbb { C P } ^ { \mathbb { k } } \to \mathbb { X }$ with the points $0 , 1 , \infty \in$ $\mathbb { C P } ^ { \mu \mathrm { \sf } }$ mapped to the given cycles $a , b , c$ , respectively.

Here the maps of different degrees should be counted separately, and the degree $d$ maps contribute to the structural constant by $\pm q ^ { d }$ (so that the “constants” are polynomials in $q$ ). Since the degree 0 holomorphic maps are constant, the quantum multiplication turns out to be a deformation of the ordinary cup-product: $< a * b , c > | _ { q = 0 } = < a \cdot b , c >$ . The number of parameters of the deformation is equal to the rank $l$ of the second homotopy group of the target K¨ahler manifold: the homotopy class $d = : ( d _ { 1 } , . . . , d _ { l } ) \in \mathbb { Z } ^ { < }$ of the holomorphic map is represented by the monomial $q ^ { d } : = q _ { 1 } ^ { d _ { 1 } } . . . q _ { l } ^ { d _ { l } }$ .

The quantum multiplication provides a machinery for answering various enumerative problems. In particular, the algebraic numbers of holomorphic maps $( \mathbb { C P } ^ { k } , F _ { k } , . . . , F _ { \mathbb { N } } ) \to ( \mathbb { X } , \supset _ { k } , . . . , \supset _ { \mathbb { N } } )$ of all degrees are coefficients in the $q$ -polynomial $( a _ { 1 } * \ldots * a _ { N } , [ X ] )$ . This follows from the structural properties of Gromov-Witten invariants (called sometimes the composition rules) which originate from the axioms of Topological Field Theory (TFT) [3].

A rigorous construction of quantum cohomology algebras of general compact symplectic manifolds including a proof of the axioms of TFT constitutes a highly non-trivial mathematical problem whose solution took several years (see [19, 17, 13, 5, 4, 15, 20]).

In the present paper we study quantum cohomology algebras of flag manifolds.

Let $F _ { s _ { 0 } , \ldots , s _ { l } }$ be the manifold of all flags

$$
0 \subset \mathbb {C} ^ {\sim_ {\mathbb {K}}} \subset \dots \subset \mathbb {C} ^ {\sim_ {\leqslant - \mathbb {K}}} \subset \mathbb {C} ^ {\sim_ {\leqslant}} = \mathbb {C} ^ {\mathbb {K}}
$$

of complex linear subspaces in $\mathbb { C } ^ { \ltimes }$ of dimensions $0 < s _ { 0 } < s _ { 1 } . . . < s _ { l }$ . For an $m$ -dimensional complex vector bundle with Chern classes $c _ { 1 } , . . . , c _ { m }$ introduce the Chern polynomial $x ^ { m } + c _ { 1 } x ^ { m - 1 } + . . . + c _ { m }$ . Denote $P _ { 0 } , . . . , P _ { l }$ the Chern polynomials of the tautological bundles of dimensions $k _ { 0 } = s _ { 0 } , k _ { 1 } = s _ { 1 } – s _ { 0 } , . . . , k _ { l } =$ $s _ { l } - s _ { l - 1 }$ over the flag manifold with the fibers $\mathbb { C } ^ { \sim _ { \kappa } } , \mathbb { C } ^ { \sim _ { \kappa } } / \mathbb { C } ^ { \sim _ { \kappa } } , . . . , \mathbb { C } ^ { \sim _ { < } } / \mathbb { C } ^ { \sim _ { < - k } }$ ,

respectively. The cohomology algebra $H ^ { * } ( F _ { s _ { 0 } , \ldots , s _ { l } } , \mathbb { Q } )$ of the flag manifold is multiplicatively generated by the Chern classes $( c _ { j } ^ { ( i ) } ) , i = 0 , . . . , l , j = 1 , . . . , k _ { i }$ of these bundles. A complete set of relations between these multiplicative generators can be written in the elegant form of a single relation between the Chern polynomials:

$$
P _ {0} (x) \dots P _ {l} (x) = x ^ {n}.
$$

We describe below the quantum deformation of this formula.

The fraction

$$
P _ {0} + \frac {(- 1) ^ {k _ {0} + 1} q _ {1}}{P _ {1} + \frac {(- 1) ^ {k _ {1} + 1} q _ {2}}{P _ {2} + \frac {…}{… + \frac {(- 1) ^ {k _ {l} - 1 + 1} q _ {l}}{P _ {l}}}}}
$$

can be written unambiguously as the ratio $P ( x ) / Q ( x )$ of polynomials of degree $n$ and $n - s _ { 0 }$ , respectively. The coefficients of the polynomial

$$
P = x ^ {n} + \Sigma_ {1} x ^ {n - 1} + \ldots + \Sigma_ {n}
$$

are polynomial expressions in the letters $( c _ { j } ^ { ( i ) } )$ and $q _ { 1 } , . . . , q _ { l }$ . The quantum deformation of the above relation reads $P = x ^ { n }$ .

Theorem 1 The quantum cohomology algebra of the flag manifold $F _ { s _ { 0 } , \ldots , s _ { l } }$ is multiplicatively generated by the n Chern classes $( c _ { j } ^ { ( i ) } )$ and the $l$ parameters $q _ { 1 } , . . . , q _ { l }$ satisfying the relations $\Sigma _ { 1 } = 0 , . . . , \Sigma _ { n } = 0$ . The Poincar´e intersection index $( a , b )$ between two cohomology classes represented in the quantum cohomology algebra by the polynomials $a ( c , q ) , b ( c , q )$ of these $n + l$ generators is given by the $n$ -dimensional residue

$$
<   a, b > (q) = (\frac {1}{2 \pi \sqrt {- 1}}) ^ {n} \oint_ {| \Sigma_ {i} | = \epsilon_ {i}} a (c, q) b (c, q) \frac {d c _ {1} ^ {(1)} \wedge \ldots \wedge d c _ {k _ {l}} ^ {(l)}}{\Sigma_ {1} (c , q) . . . \Sigma_ {n} (c , q)}.
$$

CorollaryFor $N$ given generic cycles $a _ { 1 } , . . . , a _ { N }$ of real codimension 2 in the flag manifold, the number of degree d holomorphic maps

$$
\left(\mathbb {C P} ^ {\mathbb {1}}, \curvearrowright , \dots , \curvearrowright_ {\mathbb {N}}\right) \to \left(\mathbb {F} _ {\sim_ {\mathbb {1}}, \dots , \sim_ {\mathbb {<  }}} , \partial_ {\mathbb {1}}, \dots , \partial_ {\mathbb {N}}\right)
$$

is equal to the above residue with $a = a _ { 1 } ( c ) a _ { 2 } ( c ) . . . a _ { N } ( c )$ and $b = 1$ where $a _ { \alpha } ( c )$ is the linear combination of classes $c _ { 1 } ^ { ( i ) }$ Poincar´e-dual to the cycle $a _ { \alpha }$ .

Remarks. 1) Denote $p _ { i } , i = 1 , . . . , l$ , the 1st Chern class $c _ { 1 } ^ { ( i ) } + \ldots + c _ { 1 } ^ { ( l ) }$ of the tautological quotient bundle with the fiber $\mathbb { C } ^ { \times } / \mathbb { C } ^ { \sim \beth - \psi }$ . The geometrical following convention: the monomial meaning of the parameters $q _ { i }$ in the above formulation is determined by the $q _ { 1 } ^ { d _ { 1 } } . . . q _ { k } ^ { d _ { k } }$ represents holomorphic curves $C$ in the flag manifold with $\int _ { C } p _ { i } = d _ { i }$ .

2) The statement of theorem 1 was conjectured independently by Astashkevich – Sadov [2] and Kim [12] and first proven by Ciocan-Fontanine [6] for the case of complete flag manifolds $F _ { 1 , 2 , \dots n }$ . In the special case of manifolds $F _ { 1 , 2 , \dots n }$ of complete flags in $\mathbb { C } ^ { \ltimes }$ it was conjectured by Givental – Kim [10] in the form of a surprising relation with complete integrable systems. Namely, the polynomials $\Sigma _ { 1 } ( c , q ) , . . . , \Sigma _ { n } ( c , q )$ turn out to be Poisson-commuting conservation laws of the Toda lattice (see [10] for details). The statement of theorem 1 in the case of Grassmannians $F _ { k , n }$ is due to Witten and Siebert – Tian [22, 21] and was conjectured by Gepner. For complex projective spaces $F _ { 1 , n }$ the first computation of the quantum cohomology algebra can be found in [9].

The heuristic proof of theorem 1 suggested in [10] (for complete flags), [12] and (with slight modification) in [2] was based on several natural hypotheses about existence and general properties of an equivariant generalization of the quantum cohomology theory. Given a fibration $E  B$ of compact manifolds with the compact K¨ahler manifold $X$ in the role of the fiber, one can formulate various enumerative questions about holomorphic curves in the fibers passing by marked points through given cycles in the total space $E$ of the fibration. In particular, such a parametric enumerative geometry can be associated, in particular, with any principal $G$ -bundle over $B$ where $G$ is a compact Lie group of automorphisms of $X$ . The enumerative information about all such bundles can be encoded by structural constants of the $G$ -equivariant quantum cohomology algebra of $X$ which is accountable, by definition, for enumeration of fiber-wise holomorphic spheres in the $X$ -bundle $X _ { G }  B G$ associated with the universal principal $G$ -bundle $E G \to B G$ . Like the non-equivariant quantum cohomology algebra, the equivariant one is a deformation of the multiplicative structure in the “classical” equivariant cohomology $H _ { G } ^ { * } ( X ) : = H ^ { * } ( X _ { G } )$ in the category of algebras over the ring $H ^ { * } ( B G )$ of characteristic classes of principal $G$ -bundles.

We study the $U _ { n }$ -equivariant quantum cohomology algebras of the flag manifolds with respect to the natural action of the unitary group on $\mathbb { C } ^ { \ltimes }$ and

deduce theorem 1 from its equivariant generalization.

Denote $c _ { 1 } , . . . , c _ { n }$ the universal Chern classes of principal $U _ { n }$ bundles.

Theorem 2 The $U _ { n }$ -equivariant quantum cohomology $\mathbb { Q } [ \nu , . . . , \nu ]$ - algebra of the flag manifold $F _ { s _ { 0 } , \ldots , s _ { l } } ^ { \prime }$ is isomorphic to

$$
\mathbb {Q} [ \mathbf {\Sigma} _ {\mathbb {1}} ^ {(\mathbb {1})}, \dots , \mathbf {\Sigma} _ {\mathbb {7} _ {\leqslant}} ^ {(\ll)}, \mathbf {\Sigma} _ {\mathbb {1} \mathbb {1}}, \dots , \mathbf {\Sigma} _ {\mathbb {1} \ll}, \mathbf {\Sigma} _ {\mathbb {1}}, \dots , \mathbf {\Sigma} _ {\mathbb {k}} ] / (\Sigma_ {\mathbb {1} \mathbb {1}} (, \mathbb {1}) - \mathbf {\Sigma} _ {\mathbb {1}}, \dots , \Sigma_ {\mathbb {1} \mathbb {k}} (, \mathbb {1}) - \mathbf {\Sigma} _ {\mathbb {k}})
$$

The equivariant Poincar´e pairing is given by the residue

$$
(a, b) (q, c _ {1}, \dots , c _ {n}) = (\frac {1}{2 \pi \sqrt {- 1}}) ^ {n} \oint_ {| \Sigma_ {i} - c _ {i} | = \epsilon_ {i}} a b \frac {\wedge_ {i = 0} ^ {l} \wedge_ {j = 1} ^ {k _ {i}} d c _ {j} ^ {(i)}}{\Pi_ {m = 1} ^ {n} (\Sigma_ {m} (c , q) - c _ {m})}.
$$

Remark. 1). In section 3 and 4 we construct equivariant quantum cohomology theory for simply connected homogeneous K¨ahler spaces, prove the appropriate composition rule and the other general properties of equivariant quantum cohomology assumed in the heuristic computation in [10], deduce theorem 2 and obtain theorem 1 as its specialization at $c _ { 1 } = 0 , . . . , c _ { n } = 0$ .

2). Constructing “vertical quantum cohomology” introduced in [2], Lu also proved theorem 2 in [16].

# 2 Lemma

In [10, 2, 12] the computations of quantum cohomology of flag varieties were established with an assumption. The assumption was that there is a $\mathbb { Z }$ -graded equivariant quantum cohomology with the properties of product, induction, and restriction for flag varieties. Namely,

Lemma Let $G$ be a connected compact Lie group continuously acting on a generalized flag variety $X$ . Then there is a $\mathbb { Z }$ -graded equivariant quantum cohomology algebra $Q H _ { G } ^ { * } ( X , \mathbb { Q } )$ which is $H ^ { * } ( X _ { G } , \mathbb { Q } ) \otimes _ { \mathbb { Q } } \mathbb { Q } [ ! ! ]$ as a free $H ^ { * } ( B G , \mathbb { Q } ) \otimes _ { \mathbb { Q } } \mathbb { Q } [ ! ! ]$ -module, and $q = \left( q _ { i } \right)$ is a formal multi-variable for a suitable basis of $H _ { 2 } ( X , \mathbb { Z } )$ . The grading is given by the usual grading on classes and the Chern number $2 c _ { 1 } ( T X ) [ q _ { i } ]$ on each $q _ { i }$ . When $G$ is the trivial group, $Q H _ { G } ^ { * } ( X , \mathbb { Q } )$ becomes the ordinary quantum cohomology algebra.1 It has the following properties.

Product: Let $G ^ { \prime }$ and $G ^ { \prime \prime }$ be connected compact Lie groups with actions on $X ^ { \prime }$ and $X ^ { \prime \prime }$ , respectively. Then

$$
Q H _ {G ^ {\prime} \times G ^ {\prime \prime}} ^ {*} (X ^ {\prime} \times X ^ {\prime \prime}, \mathbb {Q}) \cong \mathbb {Q} \mathrm {H} _ {\mathbb {G} ^ {\prime}} ^ {*} (\mathbb {X} ^ {\prime}, \mathbb {Q}) \otimes_ {\mathbb {Q}} \mathbb {Q} \mathrm {H} _ {\mathbb {G} ^ {\prime \prime}} ^ {*} (\mathbb {X} ^ {\prime \prime}, \mathbb {Q}).
$$

Restriction: Let $G ^ { \prime }$ be a connected Lie subgroup of a connected compact Lie group $G$ with a $G$ -space $X$ . Then, as $H ^ { * } ( B G ^ { \prime } , \mathbb { Q } )$ -algebras,

$$
Q H _ {G ^ {\prime}} ^ {*} (X, \mathbb {Q}) \cong \mathbb {Q} \mathrm {H} _ {\mathbb {G}} ^ {*} (\mathbb {X}, \mathbb {Q}) \otimes_ {\mathbb {H} ^ {*} (\mathbb {B G}, \mathbb {Q})} \mathbb {H} ^ {*} (\mathbb {B G} ^ {\prime}, \mathbb {Q}).
$$

Induction: Let $G ^ { \prime }$ be a connected Lie subgroup of a connected compact Lie group $G$ , and let $G ^ { \prime }$ act on Y. Define $X : = G \times _ { G ^ { \prime } } Y$ , which has the induced $G$ -action. Suppose $X$ becomes another generalized flag manifold with the holomorphic quotient maps $X  Y$ and $X \to G / G ^ { \prime }$ , then, as $H ^ { * } ( B G , \mathbb { Q } )$ - algebras,

$$
Q H _ {G} ^ {*} (X, \mathbb {Q}) \otimes_ {\mathbb {Q} [ \sqcup , \sqcup^ {\prime} ]} \mathbb {Q} [ \sqcup ] \cong \mathbb {Q} \mathbb {H} _ {\mathbb {G} ^ {\prime}} ^ {*} (\mathbb {Y}, \mathbb {Q})
$$

where $q$ (resp. $q ^ { \prime }$ ) is a formal multi-variable for a suitable basis of $H _ { 2 } ( Y , \mathbb { Z } )$ (resp. $H _ { 2 } ( G / G ^ { \prime } , \mathbb { Z } ) )$ ). Here $q ^ { \prime }$ acts trivially on $q$ in $\mathbb { Q } [ | | , | | ^ { \prime } ]$ -module $\mathbb { Q }$ [q].

This lemma needs some explanations:

1. Here a suitable basis of $H _ { 2 } ( X , \mathbb { Z } )$ is a basis of consisting of elements represented by rational curves in $X$ . Let $X = G / P$ , $G$ a complex Lie group (not $G$ in the lemma), $P$ a parabolic subgroup containing a Borel subgroup $B$ , $P ^ { \prime }$ a parabolic subgroup containing $P$ and having one more roots than $P$ . Then the fibers of $G / P \to G / P ^ { \prime }$ are rational curves, representing an element of $H _ { 2 } ( X , \mathbb { Z } )$ . Varying $P ^ { \prime }$ provides the basis.   
2. The induced map $B G ^ { \prime } \to B G$ from the inclusion $G ^ { \prime }  G$ provides a natural $H ^ { * } ( B G )$ -module structure on $H ^ { * } ( B G ^ { \prime } )$ . This module structure is used in the restriction and the induction.   
3. According to a degenerating Leray spectral sequence of homology of the fibration $X : = G \times _ { G ^ { \prime } } Y \to Y$ in the induction, $H _ { 2 } ( X , \mathbb { Z } ) \cong \mathbb { H } _ { k } ( \mathbb { Y } , \mathbb { Z } ) \oplus$ $\mathbb { H } _ { \sf k } ( \mathbb { G } / \mathbb { G } ^ { \prime } , \mathbb { Z } )$ . In this identification the suitable basis of $H _ { 2 } ( X )$ decomposes into the suitable basis of $H _ { 2 } ( Y )$ and a basis of $H _ { 2 } ( G / G ^ { \prime } )$ .

We can prove theorem 1, using this lemma, computations of equivariant quantum cohomology of Grassmannians, and two additional relationships: (a) the equivariant quantum cohomology algebra modulo $G$ -characteristic

classes becomes the non-equivariant quantum cohomology, and (b) the equivariant quantum cohomology algebra modulo $q$ ’s becomes the usual equivariant cohomology. The proof of (a) follows from the restriction rule stated in the lemma, and the proof of (b) follows from the definition of equivariant quantum cohomology algebras given in subsection 3.3. The computation of equivariant quantum cohomology of Grassmannians can be obtained using Sibert-Tian’s proof [21, 22], (a), and (b). Details are in [12].

In 3.1 and 3.2, we collect all the facts that we are going to use to prove the lemma. Those facts are due to Kontsevich, Behrend and Manin, and Pandharipande [13, 5, 18]. The proof of the lemma is presented in 3.3 except for proofs of its rules, which are in section 4.

# 3 Definition and associativity

# 3.1 Gromov-Witten classes

For a compactification of moduli space of rational maps, the notion of stable maps was introduced [14, 13]. Let $C$ be a connected, compact, reduced, arithmetic genus zero curve $C$ with $n$ ordered marked points at regular points and with at most ordinary double singular points. A stable map is a pair $( C , f )$ consisting of $C$ and a holomorphic map $f$ from $C$ to $X$ , such that every irreducible component of $C$ that maps to a constant point must have at least three special points. Marked points and singular points are called special points. Let ${ \overline { { \mathcal { M } } } } _ { n } ( X , d )$ denote the moduli space of equivalent classes of stable maps of degree $d \in H _ { 2 } ( X )$ . Two stable maps $( C , f )$ and $( C ^ { \prime } , f ^ { \prime } )$ will be called equivalent if there is an isomorphism $h$ from $C$ to $C ^ { \prime }$ such that $f = f ^ { \prime } \circ h$ , and $h$ preserves the ordered marked points. The stable maps are defined to ensure that the automorphism group of $( C , f )$ is discrete. When $X$ is a point, the moduli space becomes the Deline-Mumford compactification ${ \overline { { \mathcal { M } } } } _ { n }$ of stable $n$ -pointed curves of genus 0. Note that in this case $n$ should be greater than or equal to 3.

Let $X$ be a generalized flag variety. It is then shown that the moduli space ${ \overline { { \mathcal { M } } } } _ { n } ( X , d )$ of stable maps is an irreducible (projective) variety with finite quotient singularities, and the complex dimension of the space ${ \overline { { \mathcal { M } } } } _ { n } ( X , d )$ is $\begin{array} { r } { \int _ { d } c _ { 1 } ( T _ { X } ) + \dim X + n - 3 } \end{array}$ , the “right” dimension [13, 5, 18]. Therefore we need not go into the difficulty of finding a ‘virtual fundamental class’.

According to Behrend and Manin[5], it has morphisms, a contraction $\pi ^ { X }$ , and evaluations at marked points:

$$
\begin{array}{l} \overline {{\mathcal {M}}} _ {n} (X, d) \stackrel {e v ^ {X}} {\longrightarrow} X ^ {n} \stackrel {p r _ {i} ^ {X}} {\longrightarrow} X \\ \frac {\downarrow_ {\pi} {} ^ {x}}{\mathcal {M} _ {n}}. \tag {1} \\ \end{array}
$$

After [14, 13] let us define Gromov-Witten classes $I _ { n , d } ^ { X } : H ^ { * } ( X ) ^ { \otimes n } \to H ^ { * } ( { \overline { { \mathcal { M } } } } _ { n } )$ in the following way:

$$
I _ {n, d} ^ {X} \left(a _ {1} \otimes \dots \otimes a _ {n}\right) := \left(\pi^ {X}\right) _ {*} \left(e v ^ {X}\right) ^ {*} \left(a _ {1} \otimes \dots \otimes a _ {n}\right).
$$

In particular, this defines $I _ { 3 , d } ^ { X }$ , which gives a quantum multiplication structure on $H ^ { * } ( X ) \otimes _ { \mathbb { Q } } \mathbb { Q } [ | | . |$ ]: there is a unique multiplication such that

$$
<   a _ {1} \cdot a _ {2}, a _ {3} > = \sum_ {d \in H _ {2} (X)} \Pi_ {i} q _ {i} ^ {\gamma_ {i} (d)} I _ {3, d} ^ {X} (a _ {1}, a _ {2}, a _ {3}),
$$

where $q = ( q _ { 1 } , . . . )$ is a formal multi-variable for a basis $\{ \gamma _ { i } \}$ in the closed K¨ahler cone, and $< , >$ is the $q$ -linear expansion of the ordinary Poincar´e pairing. Let us choose $\{ \gamma _ { i } \}$ as the dual basis of the suitable basis of $H _ { 2 } ( X , \mathbb { Z } )$ explained in section 2. So $\gamma _ { i } ( d ) ~ \geq ~ 0$ for $d$ which can be represented by rational curves. In [14], instead of formal $q ^ { d }$ , $\exp ( - \int _ { d } \omega )$ is used for a fixed K¨ahler class $\omega$ . In next section we will see the associativity of this quantum multiplication.

# 3.2 The splitting axiom

Let $\varphi _ { S } : \overline { { \mathcal { M } } } _ { n _ { 1 } + 1 } \times \overline { { \mathcal { M } } } _ { n _ { 2 } + 1 } \to \overline { { \mathcal { M } } } _ { n }$ be the morphism associated with ordered partition $S ~ = ~ ( S _ { 1 } , S _ { 2 } )$ , $S _ { 1 } \coprod S _ { 2 } = \{ 1 , . . . , n = n _ { 1 } + n _ { 2 } \}$ , and $\varphi _ { S }$ combines two stable curves at the $n _ { 1 } + 1$ -th marked point and the first marked point, respectively. Let $\begin{array} { r } { \sum _ { i , j } \eta ^ { i , j } \alpha _ { i } \otimes \beta _ { j } } \end{array}$ be the Poincar´e-dual class of the diagonal $\Delta \subset X \times X$ . The splitting axiom reads:

$$
\begin{array}{l} \varphi_ {S} ^ {*} \left(I _ {n, d} ^ {X} \left(a _ {1} \otimes \dots \otimes a _ {n}\right)\right) \\ = \sum_ {d = d _ {1} + d _ {2}} \sum_ {i, j} I _ {n _ {1} + 1, d _ {1}} ^ {X} \left(\left(\bigotimes_ {k _ {1} \in S _ {1}} a _ {k _ {1}}\right) \otimes \alpha_ {i}\right) \eta^ {i, j} \otimes I _ {n _ {2} + 1, d _ {2}} ^ {X} \left(\beta_ {j} \otimes \left(\bigotimes_ {k _ {2} \in S _ {2}} a _ {k _ {2}}\right)\right). \\ \end{array}
$$

This axiom is proven by Behrend and Manin [5]. In particular, the splitting axiom for $n = 4$ verifies

$$
\begin{array}{l} \sum_ {d = d _ {1} + d _ {2}} \sum_ {i, j} I _ {3, d _ {1}} ^ {X} (a \otimes b \otimes \alpha_ {i}) \eta^ {i, j} I _ {3, d _ {2}} ^ {X} (\beta_ {j} \otimes c \otimes d) \\ = \sum_ {d = d _ {1} + d _ {2}} \sum_ {i, j} I _ {3, d _ {1}} ^ {X} (b \otimes c \otimes \alpha_ {i}) \eta^ {i, j} I _ {3, d _ {2}} ^ {X} (\beta_ {j} \otimes a \otimes d), \\ \end{array}
$$

which gives the associativity of quantum multiplications. Here one use the fact $\overline { { \mathcal { M } } } _ { 4 } = \mathbb { C P } ^ { \sharp }$ .

We would like to “recall” a proof of the splitting axiom when $n = 4$ : Note that we have

$$
\begin{array}{c c c} \overline {{\mathcal {M}}} _ {3} (X, d _ {1}) \times \overline {{\mathcal {M}}} _ {3} (X, d _ {2}) & \overline {{\mathcal {M}}} _ {3} (X, d) & \stackrel {{e v}} {{\to}} X ^ {3} \\ \downarrow_ {\pi_ {d _ {1}} \times \pi_ {d _ {2}}} & \downarrow_ {\pi} & \\ \overline {{\mathcal {M}}} _ {3} \times \overline {{\mathcal {M}}} _ {3} & \stackrel {{\varphi_ {S}}} {{\to}} & \overline {{\mathcal {M}}} _ {4} \end{array} .
$$

For $d = d _ { 1 } + d _ { 2 }$ , let $e v _ { i , d _ { 1 } }$ (resp. $e v _ { i , d _ { 2 } }$ ) denote the evaluation maps from ${ \overline { { \mathcal { M } } } } _ { 3 } ( X , d _ { 1 } )$ (resp. $\overline { { \mathcal { M } } } _ { 3 } ( X , d _ { 2 } ) )$ at the $i$ -th marked point, where $i = { 1 , 2 , 3 }$ . Let $\Delta$ be the diagonal in $X \times X$ . Then, from the ordered partition $S$ , we have the associated map $\Delta _ { d _ { 1 } , d _ { 2 } }$ from $( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { - 1 } ( \Delta )$ to ${ \overline { { \mathcal { M } } } } _ { 4 } ( X , d )$ , combining the third marked ‘point’ from ${ \overline { { \mathcal { M } } } } _ { 3 } ( X , d _ { 1 } )$ with the first marked ‘point’ from ${ \overline { { \mathcal { M } } } } _ { 3 } ( X , d _ { 2 } )$ . The variety $( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { - 1 } ( \Delta )$ should be considered a fibered product, and it is also an orbifold because $e v _ { i }$ is a smooth morphism (submersion if one would like differentiable orbifold languages). In summary, we have the following commutative diagram of morphisms

$$
\begin{array}{ccc}(ev_{3,d_{1}}\times ev_{1,d_{2}})^{-1}(\Delta) & \stackrel {\Delta_{d_{1},d_{2}}}{\to} & \mathrm{Im}\Delta_{d_{1},d_{2}}\\ \downarrow & & \downarrow_{\pi}\\ \overline{\mathcal{M}}_{3}\times \overline{\mathcal{M}}_{3} & \stackrel {\varphi_{S}}{\to} & \mathrm{Im}\varphi_{S} \end{array} .
$$

The horizontal maps are isomorphisms because the associated trees for stable maps are simply connected, marked by points, and labeled by degrees. Note that, as analytic fundamental classes, $\begin{array} { r } { \sum _ { d _ { 1 } + d _ { 2 } = d } [ \mathrm { I m } \Delta _ { d _ { 1 } , d _ { 2 } } ] = [ \pi ^ { - 1 } ( \mathrm { I m } \varphi _ { S } ) ] } \end{array}$ . Hence, keeping in mind that $\begin{array} { r } { \sum _ { i , j } \eta ^ { i , j } ( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { * } ( \alpha _ { i } \otimes \beta _ { j } ) } \end{array}$ is the Poincar´edual class of $( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { - 1 } ( \Delta )$ in $\overline { { \mathcal { M } } } _ { 3 } ( X , d _ { 1 } ) \times \overline { { \mathcal { M } } } _ { 3 } ( X , d _ { 2 } )$ , we conclude the proof.

# 3.3 Equivariant Gromov-Witten classes

Let $X$ have a continuous $G$ -action, $G$ being connected and compact. Then we have maps

$$
\overline {{\mathcal {M}}} _ {n} (X, d) \times_ {G} E G \stackrel {e v ^ {X _ {G}}} {\rightarrow} X ^ {n} \times_ {G} E G
$$

$$
\begin{array}{c} \downarrow_ {\pi^ {X _ {G}}} \\ \overline {{\mathcal {M}}} _ {n} \times B G \end{array} ,
$$

the equivariant version of the diagram (1). Recall that $H _ { G } ^ { * } ( X ^ { n } )$ is $H _ { G } ^ { * } ( X ) ^ { \otimes n }$ , equivariant Gromov-Witten classes due to the projections $( X ^ { n } ) _ { G } \to X _ { G }$ $I _ { n , d } ^ { X _ { G } } : H _ { G } ^ { * } ( X ) ^ { \otimes n }  H ^ { * } ( \overline { { \mathcal { M } } } _ { n } ) \otimes _ { \mathbb { Q } } H ^ { * } ( B G )$ , so that they can be identified. Define by

$$
I _ {n, d} ^ {X _ {G}} (a _ {1} \otimes \dots \otimes a _ {n}) := \pi_ {*} ^ {X _ {G}} (e v ^ {X _ {G}}) ^ {*} (a _ {1} \otimes \dots \otimes a _ {n}),
$$

where $a _ { i } \in H _ { G } ^ { * } ( X )$ .

The module $H _ { G } ^ { * } ( X ) \otimes _ { \mathbb { Q } } \mathbb { Q } [ | | ]$ has a unique multiplication by the characterization

$$
<   a _ {1} \cdot a _ {2}, a _ {3} > = \sum_ {d} q ^ {d} I _ {3, d} ^ {X _ {G}} (a _ {1}, a _ {2}, a _ {3}),
$$

where $< , >$ is the $q$ -linear expansion of the equivariant Poincar´e pairing. For the equivariant Poincar´e-dual class $\textstyle \sum _ { i , j } \eta ^ { i , j } \alpha _ { i } \otimes \beta _ { j }$ of the diagonal $\Delta _ { G } \subset$ $( X \times X ) _ { G }$ the equivariant version of the splitting axiom holds, namely,

$$
\begin{array}{l} \varphi_ {S} ^ {*} \left(I _ {4, d} ^ {X _ {G}} \left(a _ {1} \otimes \dots \otimes a _ {n}\right)\right) \\ = \sum_ {d = d _ {1} + d _ {2}} \sum_ {i, j} I _ {3, d _ {1}} ^ {X _ {G}} \left(\left(\bigotimes_ {k _ {1} \in S _ {1}} a _ {k _ {1}}\right) \otimes \alpha_ {i}\right) \eta^ {i, j} \otimes I _ {3, d _ {2}} ^ {X _ {G}} \left(\beta_ {j} \otimes \left(\bigotimes_ {k _ {2} \in S _ {2}} a _ {k _ {2}}\right)\right), \\ \end{array}
$$

where all tensor products are from $H ^ { * } ( B G )$ -module structures. The point is that all maps in the proof of the splitting axiom for the nonequivariant version are (diagonally) equivariant. Just as in the nonequivariant case, let us keep in mind that we have $\Delta _ { d _ { 1 } , d _ { 2 } } : ( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { - 1 } ( \Delta )  \overline { { \mathcal { M } } } _ { n } ( X , d )$ , its equivariant version, and that $\begin{array} { r } { \sum _ { i , j } \eta ^ { i , j } ( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { * } ( \alpha _ { i } \otimes \beta _ { j } ) } \end{array}$ is the equivariant Poincar´edual class of $( e v _ { 3 , d _ { 1 } } \times e v _ { 1 , d _ { 2 } } ) ^ { - 1 } ( \Delta ) ) _ { G }$ in $\left( \mathcal { M } _ { 3 } ( X , d _ { 1 } ) \times \overline { { \mathcal { M } } } _ { 3 } ( X , d _ { 2 } ) \right) _ { G }$ . Then the proof follows from the parallel argument of the proof of the ordinary splitting property given in the previous section.

Definition/Theorem Analogous to the one defining the quantum cohomology, we define the equivariant quantum cohomology multiplication $Q H _ { G } ( X )$ .

The associativity can be proven by the equivariant version of the splitting property when $n = 4$ . The ring is graded as stated in the lemma.

When $G$ is the trivial group, obviously the equivariant quantum cohomology is the ordinary quantum cohomology. Since $H ^ { * } ( X )$ and $H ^ { * } ( B G )$ are generated by even degree classes, $H _ { G } ^ { * } ( X ) = H ^ { * } ( X ) \otimes _ { \mathbb { Q } } H ^ { * } ( B G )$ as linear spaces, and $Q H _ { G } ^ { * } ( X )$ is a free $H ^ { * } ( B G ) \otimes _ { \mathbb { Q } } \mathbb { Q } [ | | ]$ -module.

# 4 Rules

# A proof of product rule:

Suppose $G ^ { \prime }$ and $G ^ { \prime \prime }$ are connected compact Lie groups. Let $X ^ { \prime }$ be a $G ^ { \prime }$ space, and let $X ^ { \prime \prime }$ be a $G ^ { \prime \prime }$ space, then we have the induced $G ^ { \prime } \times G ^ { \prime \prime }$ space, $X ^ { \prime } \times X ^ { \prime \prime }$ and, as $H ^ { * } ( B G ^ { \prime } \times B G ^ { \prime \prime } ) = H ^ { * } ( B G ^ { \prime } ) \otimes _ { \mathbb { Q } } H ^ { * } ( B G ^ { \prime \prime } )$ -modules, $H _ { G ^ { \prime } \times G ^ { \prime \prime } } ^ { * } ( X ^ { \prime } \times X ^ { \prime \prime } ) \cong H _ { G ^ { \prime } } ^ { * } ( X ^ { \prime } ) \otimes _ { \mathbb { Q } } H _ { G ^ { \prime \prime } } ^ { * } ( X ^ { \prime \prime } )$ . Since the complement to the subset ${ \overline { { \mathcal { M } } } } _ { 3 } ^ { 0 } ( X , d )$ consisting of “smooth” curve is a divisor (with normal crossings), $\overline { { { \mathcal { M } } } } _ { 3 } ( X ^ { \prime } , d _ { 1 } ) \times \overline { { { \mathcal { M } } } } _ { 3 } ( X ^ { \prime \prime } , d _ { 2 } )$ and $\overline { { { \mathcal { M } } } } _ { 3 } ( X ^ { \prime } \times X ^ { \prime \prime } , d )$ are birational, so that $I _ { 3 , d _ { 1 } } ^ { X ^ { \prime } } \cdot I _ { 3 , d _ { 2 } } ^ { X ^ { \prime \prime } } = I _ { 3 , ( d _ { 1 } , d _ { 2 } ) } ^ { X ^ { \prime } \times X ^ { \prime \prime } }$ ′ I X ′′ . Let $C$ and $D$ be finite cycles of $B G ^ { \prime }$ and $B G ^ { \prime \prime }$ respectively. Then integrating fibers over $C \times D$ , we conclude $I _ { 3 , d _ { 1 } } ^ { X _ { G ^ { \prime } } ^ { \prime } } \otimes _ { \mathbb { Q } } I _ { 3 , d _ { 2 } } ^ { X _ { G ^ { \prime \prime } } ^ { \prime \prime } } =$ NQ I 3, d2 X ′′G′′ IX′×X′′G′×G′′3,(d1,d2) . Hence we have the proof of the product property stated in the $I _ { 3 , ( d _ { 1 } , d _ { 2 } ) } ^ { X ^ { \prime } \times X _ { G ^ { \prime } \times G ^ { \prime \prime } } ^ { \prime \prime } }$ theorem.

# A proof of restriction rule:

Let $G ^ { \prime } \subset G$ be a Lie subgroup and $X$ be a $G$ -space. Consider $X$ a $G ^ { \prime }$ - space for $X _ { G }$ . Let $p : B G ^ { \prime } \to B G$ be the map induced from the inclusion $G ^ { \prime } \subset G$ . We have natural induced morphisms and a diagram

$$
\begin{array}{c c c} H ^ {*} (\overline {{\mathcal {M}}} _ {n} (X, d) _ {G ^ {\prime}}) & \leftarrow & H ^ {*} (\overline {{\mathcal {M}}} _ {n} (X, d) _ {G}) \\ \downarrow & & \downarrow \end{array}
$$

$$
H ^ {*} (B G ^ {\prime}) \quad \stackrel {p ^ {*}} {\leftarrow} \quad H ^ {*} (B G).
$$

The diagram is commutative, since for any finite cycle $C$ in $B G ^ { \prime }$ , $\overline { { \mathcal { M } } } _ { n } ( X , d ) \times _ { G }$ $p ( C )$ induces $\overline { { { \mathcal { M } } } } _ { n } ( X , d ) \times _ { G ^ { \prime } } C$ by the map $p$ . The restriction rule follows.

# A proof induction rule:

Let $G ^ { \prime } \subset G$ be a Lie subgroup. For induction consider a generalized flag manifold $Y$ with a $G ^ { \prime }$ -action and let $X = G \times _ { G ^ { \prime } } Y$ . For $d \in H _ { 2 } ( Y ) \subset H _ { 2 } ( X )$ ,

there are natural identifications $Y _ { G ^ { \prime } } = X _ { G }$ and $\overline { { { \mathcal { M } } } } _ { n } ( Y , d ) _ { G ^ { \prime } } = \overline { { { \mathcal { M } } } } _ { n } \left( X , d \right) _ { G }$ . From the commutative diagram

$$
\begin{array}{r l r} \overline {{\mathcal {M}}} _ {n} (Y, d) _ {G ^ {\prime}} & = & \overline {{\mathcal {M}}} _ {n} (X, d) _ {G} \\ \downarrow & & \downarrow \\ B G ^ {\prime} & \stackrel {{p}} {{\to}} & B G, \end{array}
$$

$I _ { n , d } ^ { X _ { G } } = p _ { * } I _ { n , d } ^ { Y _ { G ^ { \prime } } }$ = p∗I and the induction rule follows.

Acknowledgement. I would like to thank A. Givental for valuable suggestions, and H. Chang for a discussion on the splitting axiom. This paper is a part of my thesis.

# References

[1] V. Arnold, Mathematical methods of classical mechanics, (Appendix 9), English translation, Springer, Berlin, 1978.   
[2] A. Astashkevich and V. Sadov, Quantum cohomology of partial flag manifolds $F _ { n _ { 1 } , \ldots , n _ { k } }$ , Commun. Math. Phys. 170 (1995), 503-528.   
[3] M. Atiyah, Topological quantum field theories, Publ. Math. Inst. Hautes Etudes Sci. Paris 68 (1989), 175-186.   
[4] K. Behrend, Gromov-Witten invariants in algebraic geometry, Preprint 1996, alg-geom/9601011   
[5] K. Behrend and Yu. Manin, Stacks of Stable Maps and Gromov-Witten Invariants. Preprint 1995, alg-geom/9506023.   
[6] I. Ciocan-Fontanine, Quantum cohomology of flag varieties, IMRN, 1995, No. 6, 263-277.   
[7] A. Floer, Proof of the Arnold conjecture for surfaces and generalizations for certain Kahler manifolds, Duke Math. J. 53 (1986), no 1, 1-32.   
[8] S. Fomin, S. Gelfand, and A. Posnikov, Quantum Schubert polynomials, Preprint 1996.   
[9] B. Fortune and A. Weinstein, A symplectic fixed point theorem for complex projective spaces, Bull. Amer. Math. Soc. New Series 12 (1985), no. 1, 128-130.

[10] A. Givental and B. Kim, Quantum cohomology of flag manifolds and Toda lattices, Commun. Math. Phys. 168 (1995), 609-641.   
[11] M. Gromov, Pseudo-holomorphic curves in symplectic manifolds, Inventiones Mathematicae 82 (1985), 307-347.   
[12] B. Kim, Quantum cohomology of partial flag manifolds and a residue formula for their intersection pairings, IMRN 1995, No.1, 1-16.   
[13] M. Kontsevich, Enumeration of rational curves via torus actions, Preprint 1994, hep-th/9405035.   
[14] M. Kontsevich and Yu. Manin, Gromov-Witten classes, quantum cohomology and enumerative geometry, Commun. Math. Phys. 164 (1994), 525-562.   
[15] J. Li and G. Tian, Virtual Moduli Cycles and GW-invariants, alggeom/9602007.   
[16] P. Lu, In preparation.   
[17] D. McDuff and D. Salamon, J-holomorphic curves and quantum cohomology, American Mathematical Society, c1994. University lecture series (Providence, R.I.) ; 6.   
[18] R. Pandharipande, Notes on Kontsevich’s compactification of the space of maps, Preprint 1995.   
[19] Y. Ruan and G. Tian, Mathematical theory of quantum cohomology, Preprint 1994.   
[20] –, Higher genus symplectic invariants and sigma model coupled with gravity. Preprint 1996, alg-geom/9601005.   
[21] B. Siebert and G. Tian, On quantum cohomology rings of Fano manifolds and a formula of Vafa and Intriligator, Preprint 1994.   
[22] E. Witten, The Verlinde algebra and the cohomology of the Grassmannian, Preprint 1993.

Department of Mathematics, University of California, Berkeley, CA 94720, USA E-mail: bumsig@math.berkeley.edu