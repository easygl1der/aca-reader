# Positivity in equivariant Schubert calculus

William Graham1

# 1 Introduction

Let $X ~ = ~ G / B$ be the flag variety of a complex semisimple group $G$ with $B \supset T$ a Borel subgroup and maximal torus, respectively. The homology $H _ { * } ( X )$ has as a basis the fundamental classes $[ X _ { w } ]$ of Schubert varieties $X _ { w } ~ \subset ~ X$ ; if $\{ x _ { w } \} \subset H ^ { * } ( X )$ is the corresponding dual basis for cohomology, the cup product, expressed in this basis, has nonnegative coefficients:

$$
x _ {u} x _ {v} = \sum a _ {u v} ^ {w} x _ {w} \tag {1.1}
$$

where $a _ { u v } ^ { w }$ are nonnegative integers.

The $T$ -equivariant cohomology and Chow groups of the flag variety have been described by [A], [KK], [Br]. One reason to study these groups is that they provide a way to compute the coefficients in the multiplication in ordinary cohomology. In addition, the equivariant groups are related to degeneracy loci in algebraic geometry (see [F2], [F3], [P-R], [G]), which in turn are related to the double Schubert polynomials first defined in combinatorics by [L-S].

Peterson [P] recently conjectured that the equivariant cohomology groups of the flag variety have a positivity property generalizing (1.1). The $T$ -equivariant cohomology $H _ { T } ^ { * } ( X )$ is a free module over $H _ { T } ^ { * } ( p t )$ with a basis dual (in a suitable sense; see Section 2) to the equivariant fundamental classes $[ X _ { w } ] _ { T }$ ; again we call this basis $\{ x _ { w } \}$ . Now $H _ { T } ^ { * } ( p t )$ is isomorphic to the polynomial ring $S ( \hat { T } ) = \mathbb { Z } [ \lambda _ { 1 } , \ldots , \lambda _ { n } ]$ , where $\lambda _ { 1 } , \ldots , \lambda _ { n }$ is a basis for the free abelian group $\hat { T }$ of characters of $T$ . Let $\alpha _ { 1 } , \ldots , \alpha _ { n }$ denote the simple roots in $\hat { T }$ (chosen so that the roots of ${ \mathfrak { b } } = \operatorname { L i e } B$ are positive). In the equivariant setting, we can again expand the product $x _ { u } x _ { v }$ in the form (1.1), but now the $a _ { u v } ^ { w }$ are in $H _ { T } ^ { * } ( p t ) - \mathrm { i n }$ other words, they are polynomials. Peterson’s conjecture is that when each $a _ { u v } ^ { w }$ is written as a sum of monomials in the $\alpha _ { i }$ , the coefficients are all nonnegative. In this paper we prove the conjecture, not just for finite-dimensional flag varieties, but in the general Kaˇc-Moody setting. An immediate corollary is a conjecture of Billey [Bi].

The methods of this paper are those used by Kumar and Nori [KN]. In that paper, the authors prove the nonnegativity result (1.1) in ordinary cohomology for the flag variety of a Kaˇc-Moody group. As they observe, the difficulty in proving this result is that in the Kaˇc-Moody case, unlike the finite dimensional case, the flag variety is not in general

a homogeneous space. However, it is approximated by finite-dimensional varieties, each of which has an action of a unipotent group with finitely many orbits. The main result of [KN] is that for such varieties, the cup product has nonnegative coefficients (with respect to a suitable basis); the result for the flag variety follows. A similar problem arises in equivariant cohomology. The equivariant cohomology of $X$ is by definition the cohomology of a “mixed space” $X _ { T }$ , which, although infinite-dimensional, can be approximated by finite-dimensional varieties. As in the situation considered by Kumar and Nori, the space $X _ { T }$ is not a homogeneous space. But unlike their situation, the finite-dimensional approximations to $X _ { T }$ do not (as far as I know) have actions of unipotent groups with finitely many orbits, so we cannot apply their result. Instead, by adapting their proof to the equivariant setting, and using a relation in equivariant cohomology (or Chow groups) observed by Brion, we are able to deduce an equivariant analogue of the main result of [KN]. The equivariant nonnegativity result for the flag variety follows immediately.

Acknowledgements. I would like to thank Michel Brion and James Carrell for some useful e-mail.

# 2 Preliminaries

We will work with schemes over the ground field $\mathbb { C }$ and assume (to freely apply the results of [F, Ch.19]) that all schemes considered admit closed embeddings into nonsingular schemes. We use equivariant cohomology and Borel-Moore homology with integer coefficients as our main tools; $H _ { * } X$ will denote the Borel-Moore homology of $X$ . For smooth varieties, we could alternatively use equivariant Chow groups, but for nonsmooth varieties, the Chow “cohomology” theory is not as well understood and for this reason we use (equivariant) cohomology and Borel-Moore homology groups. In this section we recall some basic facts about these groups; for more background, see [Br2] or [E-G]. We also prove, for lack of a reference, equivariant versions of several familiar non-equivariant results.

Let $X$ be a scheme with an action of a linear algebraic group $G$ . Let $V$ be a representation of $G$ and $U$ an open subset of $V$ such that $G$ acts freely on $U$ and such that the (complex) codimension of $V - U$ in $V$ is greater than dim $X - i / 2$ . View $G$ as acting on the right on $U$ , and on the left on $X$ ; then $G$ acts on $U \times X$ by $g \cdot ( u , x ) = ( u g ^ { - 1 } , g x )$ . 1 Define $U \times ^ { G } X$ to be $( U \times X ) / G$ . The equivariant cohomology and Borel-Moore homology of $X$ are, by definition,

$$
H _ {G} ^ {i} (X) = H ^ {i} (U \times^ {G} X)
$$

$$
H _ {i} ^ {G} (X) = H _ {i + 2 (\dim V - \dim G)} (U \times^ {G} X).
$$

These groups are independent of the choice of $V$ and $U$ provided the codimension condition is satisfied. For this reason we often denote $U \times ^ { G } X$ by $X _ { G }$ (omitting $U$ from the notation). The quotient $U / G$ is a finite-dimensional approximation to the classifying space $_ { B G }$ introduced in Chow theory by Totaro [T]. We will frequently write $_ { B G }$ when we mean such a finite-dimensional approximation.

The equivariant cohomology of a point we denote by $H _ { G } ^ { * }$ . Both $H _ { G } ^ { * } ( X )$ and $H _ { * } ^ { G } ( X )$ are modules for $H _ { G } ^ { * }$ . $H _ { G } ^ { * } ( X )$ has a natural ring structure, and $H _ { * } ^ { G } ( X )$ is a module for this

ring. Any $G$ -stable closed subvariety $Y \subset X$ has a fundamental class $[ Y ] _ { G }$ in $H _ { 2 \dim Y } ^ { G } ( X )$ There is a natural map $\cap [ X ] _ { G } : H _ { G } ^ { * } ( X ) \to H _ { * } ^ { G } ( X )$ ; if $X$ is smooth this is an isomorphism. In particular, we will always identify $H _ { * } ^ { G } ( p t )$ with $H _ { G } ^ { * }$ .

Let $\pi ^ { X } : X \to p t$ denote the projection. If $X$ is proper, this induces an $H _ { G } ^ { * }$ -linear map $\pi _ { * } ^ { X } : H _ { * } ^ { G } ( X ) \to H _ { * } ^ { G } ( p t ) \cong H _ { G } ^ { * }$ . In this case, there is a pairing $( \ , \ ) : H _ { G } ^ { * } ( X ) \otimes H _ { * } ^ { G } ( X ) $ $H _ { G } ^ { * }$ taking $x \otimes C$ to $\pi _ { * } ^ { X } ( x \cap C )$ . We will sometimes write this pairing as $\textstyle { \int _ { C } } x$ , and if $C = [ Y ] _ { G }$ , we will abuse notation and write it as $\ j _ { Y } x$ . The pairing has the property that given $f : X _ { 1 } \to X _ { 2 }$ , we have

$$
\left(f ^ {*} x _ {2}, C _ {1}\right) = \left(x _ {2}, f _ {*} C _ {1}\right). \tag {2.2}
$$

(Proof: ( $\begin{array} { r } { f ^ { * } x _ { 2 } , C _ { 1 } ) = \pi _ { * } ^ { X _ { 1 } } ( f ^ { * } x _ { 2 } \cap C _ { 1 } ) = \pi _ { * } ^ { X _ { 2 } } f _ { * } ( f ^ { * } x _ { 2 } \cap C _ { 1 } ) = \pi _ { * } ^ { X _ { 2 } } ( x _ { 2 } \cap f _ { * } C _ { 1 } ) = ( x _ { 2 } , f _ { * } C _ { 1 } ) . } \end{array}$ )

The map $X \times ^ { G } U \to U / G$ is a fibration with fiber $X$ , and pullback to a fiber yields a map $H _ { G } ^ { * } ( X ) \to H ^ { * } ( X )$ . There is also a Gysin morphism $H _ { * } ^ { G } ( X ) \to H _ { * } ( X )$ .

A variety $X$ is said to be paved by affines if it can be written as a finite disjoint union $X = \coprod X _ { i } ^ { \mathrm { 0 } }$ where $X _ { i } ^ { 0 }$ is isomorphic to affine space $\mathbb { A } ^ { d _ { i } }$ for some $d _ { i }$ . As is well known (see e.g. [KN]) the Borel-Moore homology $H _ { * } ( X )$ is the free $\mathbb { Z }$ -module generated by the fundamental classes $[ X _ { i } ]$ (where $X _ { i }$ is the closure of $X _ { i } ^ { 0 }$ ); the odd-dimensional Borel-Moore homology vanishes.

Part (b) of the next proposition and the remark following are from [A] (Prop. 2.5.1 and 2.4.1), with a somewhat different proof.

Proposition 2.1 Suppose the $G$ -variety $X$ has a pairing by $G$ -invariant affines $X _ { i } ^ { 0 }$ . Then

(a) $H _ { * } ^ { G } ( X )$ is a free $H _ { G } ^ { * }$ -module with basis $\{ [ X _ { i } ] _ { G } \}$ .   
(b) Suppose in addition that $X$ is complete and that $H _ { G } ^ { * }$ is torsion-free. Then there exist classes $x _ { i }$ (of degree dim $X _ { i }$ ) in $H _ { G } ^ { * } ( X )$ which form a basis for $H _ { G } ^ { * } ( X )$ as $H _ { G } ^ { * }$ -module, such that the bases $\{ [ X _ { i } ] _ { G } \}$ and $\{ x _ { i } \}$ are dual in the sense that $\textstyle { \int _ { X _ { i } } x _ { j } = \delta _ { i j } }$ .

Proof: (a) Let $X _ { k } ^ { 0 }$ be open in $X$ , and $Y = X - X _ { k } ^ { 0 }$ ; then there is a long exact sequence of $H _ { G } ^ { * }$ -modules

$$
\rightarrow H _ {i + 1} ^ {G} (X _ {k} ^ {0}) \rightarrow H _ {i} ^ {G} (Y) \rightarrow H _ {i} ^ {G} (X) \rightarrow H _ {i} ^ {G} (X _ {k} ^ {0}) \rightarrow \dots
$$

Since $X _ { k } ^ { 0 }$ is isomorphic to affine space, $H _ { * } ^ { G } ( X _ { k } ^ { 0 } )$ is a free $H _ { G } ^ { * }$ -module of rank 1, generated by $[ X _ { k } ^ { 0 } ] _ { G }$ . Hence all the odd equivariant homology of $X _ { k } ^ { 0 }$ vanishes, by induction the same holds for $Y$ , and then by the long exact sequence it holds for $X$ . Thus we have a short exact sequence of $H _ { G } ^ { * }$ -modules:

$$
0 \to H _ {*} ^ {G} (Y) \to H _ {*} ^ {G} (X) \to H _ {*} ^ {G} (X _ {k} ^ {0}) \to 0.
$$

This is split by the $H _ { G } ^ { * }$ -linear map $H _ { * } ^ { G } ( X _ { k } ^ { 0 } ) \to H _ { * } ^ { G } ( X )$ taking $[ X _ { k } ^ { 0 } ] _ { G }$ to $[ X _ { k } ] _ { G }$ . Induction implies (a).

(b) Because the odd ordinary cohomology of $X$ vanishes, the pullback to a fiber $H _ { G } ^ { * } ( X ) \to H ^ { * } ( X )$ is surjective (this is because the spectral sequence of the fibration $X _ { G }  B _ { G }$ degenerates at $E _ { 2 }$ ). If $\{ y _ { i } \}$ are any classes of pure degree in $H _ { G } ^ { * } ( X )$ which pull back to a basis of $H ^ { * } ( X )$ (we may assume $\deg y _ { i } = \dim X _ { i }$ ), then by the Leray-Hirsch theorem [Sp], $H _ { G } ^ { * } ( X )$ is a free $H _ { G } ^ { * }$ -module with basis $\{ y _ { i } \}$ . Claim: The matrix $A = \left( a _ { i j } \right)$ with

entries $a _ { i j } \in H _ { G } ^ { * }$ defined by $a _ { i j } = \textstyle { \int _ { X _ { i } } y _ { j } }$ is invertible. This can be seen by slightly modifying the arguments of [G, Theorem 4.1]. For, we may assume that the $X _ { i }$ are numbered so that the dimension increases as $i$ increases. Now, $\ j _ { X _ { i } } y _ { j } = 0$ unless $\deg y _ { j } \geq \dim X _ { i }$ . This implies that the matrix $( a _ { i j } )$ is block upper triangular (here a block of the matrix corresponds to the set of $( i , j )$ with $\dim X _ { i } = d$ , $\dim X _ { j } = e$ , for fixed $d$ and $e$ ). Moreover, the diagonal blocks are invertible matrices of scalars (as, for any fixed $d$ , the entries in the corresponding diagonal block are just the values $( [ X _ { i } ] , y _ { j } ^ { \prime } )$ , where $y _ { j } ^ { \prime }$ is the pullback to a fiber of $y _ { j }$ ; $\{ \left[ X _ { i } \right] \}$ is a basis for $H _ { 2 d } ( X )$ and $\{ y _ { j } ^ { \prime } \}$ a basis for $H ^ { 2 d } ( X )$ ). Hence the matrix $A$ is invertible, as claimed.

Let $B = A ^ { - 1 } = ( b _ { i j } )$ and define $\begin{array} { r } { x _ { j } = \sum _ { i } b _ { i j } y _ { i } } \end{array}$ . Then $\{ x _ { j } \}$ is a basis of $H _ { G } ^ { * } ( X )$ dual to $\{ [ X _ { i } ] _ { G } \}$ . Indeed,

$$
\int_ {X _ {i}} x _ {j} = \sum_ {k} \int_ {X _ {i}} b _ {k j} y _ {k} = \sum_ {k} b _ {k j} \int_ {X _ {i}} y _ {k} = \sum_ {k} b _ {k j} a _ {i k} = \delta_ {i j}. \tag {2.3}
$$

Note that the dual basis is uniquely determined by (2.3), as can be seen by expressing one dual basis in terms of another. Because the $[ X _ { i } ] _ { G }$ have pure degree $\dim X _ { i }$ , the elements $x _ { j }$ of the dual basis must have degree $\dim X _ { j }$ . For, if $Y$ is an irreducible closed subvariety of $X$ , and $y \in H _ { G } ^ { k } ( X )$ , then $\textstyle \int _ { Y } y$ has degree $k - \dim Y$ . Hence if we replace each $x _ { j }$ by its component in degree $\dim X _ { j }$ , we still have a dual basis. As the dual basis is unique, each $x _ { j }$ must have degree $\operatorname { d i m } X _ { j }$ . 

Remarks. (1) The conditions $\int _ { X _ { i } } x _ { j } \ = \ \delta _ { i j }$ imply that under the map $H _ { G } ^ { * } ( X ) \to$ $H ^ { * } ( X )$ , the images $x _ { i } ^ { \prime }$ of $x _ { i }$ form a basis of $H ^ { * } ( X )$ dual to the basis $\{ \left[ X _ { i } \right] \}$ of $H _ { * } ( X )$ .

(2) This result and the next are also valid with coefficients in a field; then $H _ { G } ^ { * }$ is automatically torsion-free.

For a variety $X$ paved by $G$ -invariant affines as above, we have the following description of the product on $H _ { G } ^ { * } ( X )$ in terms of the diagonal morphism. The non-equivariant version of this result was used by [KN]. The equivariant version was mentioned in [P] for the flag variety; the general proof is the same. Note that the diagonal morphism $\delta : X  X \times X$ is $G$ -equivariant ( $G$ acting diagonally on $X \times X$ ).

Proposition 2.2 Let $X$ be a $G$ -variety with a paving by $G$ -invariant affines $X _ { i } ^ { 0 }$ ; assume $H _ { G } ^ { * }$ is torsion-free. Let $X _ { i }$ and $x _ { i }$ be as in the previous proposition. We can write $\begin{array} { r } { \delta _ { * } [ X _ { k } ] _ { G } = \sum _ { i , j } a _ { i j } [ X _ { i } \times X _ { j } ] _ { G } } \end{array}$ , where $a _ { i j } \in H _ { G } ^ { * }$ . The product in $H _ { G } ^ { * } ( X )$ is given by

$$
x _ {i} x _ {j} = \sum_ {k} a _ {i j} ^ {k} x _ {k}.
$$

Proof: We can write $\delta _ { * } [ X _ { k } ] _ { G }$ in the form claimed because the classes $[ X _ { i } \times X _ { j } ] _ { G }$ form a basis for $H _ { * } ^ { G } ( X \times X )$ as $H _ { G } ^ { * }$ -module.

Let $q _ { i } : X \times X \to X$ denote the $i$ -th projection. As in the non-equivariant case, the product on $H _ { G } ^ { * } ( X )$ is given by

$$
c _ {1} \cdot c _ {2} = \delta^ {*} \left(q _ {1} ^ {*} c _ {1} \cdot q _ {2} ^ {*} c _ {2}\right)
$$

for $c _ { 1 } , c _ { 2 } \in H _ { G } ^ { * } ( X \times X )$ . (This can be seen by considering the composition

$$
X _ {G} \stackrel {\delta_ {G}} {\to} (X \times X) _ {G} \cong X _ {G} \times_ {B G} X _ {G} \stackrel {i} {\hookrightarrow} X _ {G} \times X _ {G}
$$

and noting that the product on $H ^ { * } ( X _ { G } )$ is given by

$$
\zeta_ {1} \cdot \zeta_ {2} = (i \circ \delta_ {G}) ^ {*} (p r _ {1} ^ {*} \zeta_ {1} \cdot p r _ {2} ^ {*} \zeta_ {2})
$$

where $p r _ { i } : X _ { G } \times X _ { G }  X _ { G }$ is the projection and $\zeta _ { i } \in H ^ { * } ( X _ { G } )$ . Choosing $\zeta _ { i }$ to represent $c _ { i } \in H _ { G } ^ { * } ( X )$ , the assertion follows easily.)

The preceding proposition shows that if $X$ is paved by invariant affines, then $H _ { G } ^ { * } ( X )$ and $H _ { * } ^ { G } ( X )$ are free $H _ { G } ^ { * }$ -modules, with a perfect pairing

$$
\left(\mathbf {\Omega}, \mathbf {\Omega}\right): H _ {G} ^ {*} (X) \otimes_ {H _ {G} ^ {*}} H _ {*} ^ {G} (X) \to H _ {G} ^ {*}.
$$

Using this, we can identify

$$
H _ {G} ^ {*} (X) = \mathrm {H o m} _ {H _ {G} ^ {*}} (H _ {*} ^ {G} (X), H _ {G} ^ {*}).
$$

Therefore, to show that $\begin{array} { r } { x _ { i } x _ { j } = \sum _ { k } a _ { i j } ^ { k } x _ { k } } \end{array}$ , it is enough to show that for all $\nu \in H _ { * } ^ { G } ( X )$ , we have

$$
(x _ {i} x _ {j}, \nu) = (\sum_ {k} a _ {i j} ^ {k} x _ {k}, \nu) = \sum_ {k} a _ {i j} ^ {k} (x _ {k}, \nu).
$$

In fact, it is enough to check this when $\nu$ is one of the basis elements $\lfloor X _ { k } \rfloor _ { G }$ , i.e., it is enough to show

$$
(x _ {i} x _ {j}, [ X _ {k} ] _ {G}) = a _ {i j} ^ {k}.
$$

Now

$$
\begin{array}{l} \left(x _ {i} x _ {j}, \left[ X _ {k} \right] _ {G}\right) = \left(\delta^ {*} \left(q _ {1} ^ {*} x _ {i} \cdot q _ {2} ^ {*} x _ {j}\right), \left[ X _ {k} \right] _ {G}\right) \\ = \left(q _ {1} ^ {*} x _ {i} \cdot q _ {2} ^ {*} x _ {j}, \delta_ {*} \left[ X _ {k} \right] _ {G}\right) \\ = \sum_ {m, n} a _ {k} ^ {m n} \left(q _ {1} ^ {*} x _ {i} \cdot q _ {2} ^ {*} x _ {j}, [ X _ {m} \times X _ {n} ] _ {G}\right). \\ \end{array}
$$

By definition of the pairing, $\begin{array} { r } { ( q _ { 1 } ^ { * } x _ { i } \cdot q _ { 2 } ^ { * } x _ { j } , [ X _ { m } \times X _ { n } ] _ { G } ) = \pi _ { * } ^ { X \times X } ( q _ { 1 } ^ { * } x _ { i } \cdot q _ { 2 } ^ { * } x _ { j } \cap [ X _ { m } \times X _ { n } ] _ { G } ) } \end{array}$ . This is computed using the fibrations $X _ { G }  B _ { G }$ and $( X \times X ) _ { G } = X _ { G } \times _ { B _ { G } } X _ { G } \stackrel { \pi _ { G } } {  } B _ { G }$ . By the next lemma, the result is equal to

$$
\pi_ {*} ^ {X} (x _ {i} \cap [ X _ {m} ] _ {G}) \cdot \pi_ {*} ^ {X} (x _ {j} \cap [ X _ {n} ] _ {G})
$$

which is 1 if $i = m$ and $j = n$ , and 0 otherwise. We conclude $( x _ { i } x _ { j } , [ X _ { k } ] _ { G } ) = a _ { k } ^ { i j }$ , as desired. 

Lemma 2.3 Let $\rho _ { i } : X _ { i } \to Y$ $( i = 1 , 2$ ) be fibrations with $\rho _ { i }$ proper, $\pi : X _ { 1 } \times _ { Y } X _ { 2 } \to Y$ , $q _ { i } : X _ { 1 } \times _ { Y } X _ { 2 }  X _ { i }$ the projections. Let $Z _ { i } \subset X _ { i }$ be closed subvarieties and $\alpha _ { i } \in H ^ { * } ( X _ { i } )$ . Assume $Y$ is smooth, and identify $H _ { * } ( Y )$ with $H ^ { * } ( Y )$ . Then

$$
\pi_ {*} \left(q _ {1} ^ {*} \alpha_ {1} \cdot q _ {2} ^ {*} \alpha_ {2} \cap [ Z _ {1} \times_ {Y} Z _ {2} ]\right) = \rho_ {1 *} \left(\alpha_ {1} \cap [ Z _ {1} ]\right) \cdot \rho_ {2 *} \left(\alpha_ {2} \cap [ Z _ {2} ]\right)
$$

where on the right hand side the product is taken in $H ^ { * } ( Y )$ .

Proof: We have a Cartesian diagram

$$
X _ {1} \times_ {Y} X _ {2} \xrightarrow {\Delta} X _ {1} \times X _ {2}
$$

$$
\begin{array}{c c} \downarrow \pi & \downarrow \Pi \end{array}
$$

$$
Y \qquad \stackrel {{\delta}} {{\to}} \quad Y \times Y
$$

Because $Y$ is smooth, $\delta$ (and hence $\Delta$ ) are regular embeddings, so there are Gysin maps $\delta ^ { * }$ and $\Delta ^ { * }$ on homology. Claim: In $H _ { * } ( X _ { 1 } \times _ { Y } X _ { 2 } )$ ,

$$
q _ {1} ^ {*} \alpha_ {1} \cdot q _ {2} ^ {*} \alpha_ {2} \cap [ Z _ {1} \times_ {Y} Z _ {2} ] = \Delta^ {*} \left(\left(\alpha_ {1} \cap [ Z _ {1} ]\right) \times \left(\alpha_ {2} \cap [ Z _ {2} ]\right)\right).
$$

To prove this, first note that (with $p r _ { i } : X _ { 1 } \times X _ { 2 }  X _ { i }$ denoting the projection) $q _ { 1 } ^ { * } \alpha _ { 1 } \cdot$ $q _ { 2 } ^ { * } \alpha _ { 2 } = \Delta ^ { * } ( p r _ { 1 } ^ { * } \alpha _ { 1 } \cdot p r _ { 2 } ^ { * } \alpha _ { 2 } ) = \Delta ^ { * } ( \alpha _ { 1 } \times \alpha _ { 2 } )$ (cf. [Mu, p. 351]). Next, $[ Z _ { 1 } \times _ { Y } Z _ { 2 } ] = \Delta ^ { * } [ Z _ { 1 } \times Z _ { 2 } ]$ , since $Z _ { 1 } \times Z _ { 2 }$ and $\Delta ( X \times _ { Y } X )$ are subvarieties of $X _ { 1 } \times X _ { 2 }$ whose intersection at smooth points is transverse. Hence (noting that $[ Z _ { 1 } \times Z _ { 2 } ] = [ Z _ { 1 } ] \times [ Z _ { 2 } ]$ by [F, p. 377])

$$
\begin{array}{l} q _ {1} ^ {*} \alpha_ {1} \cdot q _ {2} ^ {*} \alpha_ {2} \cap \left[ Z _ {1} \times_ {Y} Z _ {2} \right] = \Delta^ {*} \left(\alpha_ {1} \times \alpha_ {2}\right) \cap \Delta^ {*} \left[ Z _ {1} \times Z _ {2} \right] \\ = \Delta^ {*} \left(\left(\alpha_ {1} \times \alpha_ {2}\right) \cap \left(\left[ Z _ {1} \right] \times \left[ Z _ {2} \right]\right)\right) \\ = \Delta^ {*} \left(\left(\alpha_ {1} \cap [ Z _ {1} ]\right) \times \left(\alpha_ {2} \cap [ Z _ {2} ]\right)\right) \\ \end{array}
$$

proving the claim.

To complete the proof of the lemma, we compute:

$$
\begin{array}{l} \pi_ {*} \left(q _ {1} ^ {*} \alpha_ {1} \cdot q _ {2} ^ {*} \alpha_ {2} \cap [ Z _ {1} \times_ {Y} Z _ {2} ]\right) = \pi_ {*} \Delta^ {*} \left(\left(\alpha_ {1} \cap [ Z _ {1} ]\right) \times \left(\alpha_ {2} \cap [ Z _ {2} ]\right)\right) \\ = \delta^ {*} \Pi_ {*} \left(\left(\alpha_ {1} \cap [ Z _ {1} ]\right) \times \left(\alpha_ {2} \cap [ Z _ {2} ]\right)\right) \\ = \delta^ {*} \left(\rho_ {1 *} \left(\alpha_ {1} \cap [ Z _ {1} ]\right) \times \rho_ {2 *} \left(\alpha_ {2} \cap [ Z _ {2} ]\right)\right) \\ = \rho_ {1 *} \left(\alpha_ {1} \cap [ Z _ {1} ]\right) \cdot \rho_ {2 *} \left(\alpha_ {2} \cap [ Z _ {2} ]\right). \\ \end{array}
$$

This proves the lemma. 

# 3 The positivity theorem

In this section we prove the positivity result about multiplication in equivariant cohomology (Theorem 3.1). As in the non-equivariant case considered by Kumar and Nori, it is deduced from a result about invariant cycles (Theorem 3.2). In the non-equivariant setting, Hirschowitz [Hi] proved that for a projective scheme with an action of a connected solvable group $B$ , any effective cycle is rationally equivalent to a $B$ -invariant effective cycle. Kumar and Nori gave a different proof of this result (without assuming projectivity) in the special case of unipotent groups, and the proof of Theorem 3.2 is adapted from their proof.

In this section, $T$ will denote an algebraic torus (i.e. product of multiplicative groups $\mathbb { G } _ { m }$ ) with Lie algebra $\mathbf { t } = \operatorname { L i e } \boldsymbol { T }$ , and $\hat { T } \subset { \mathfrak { t } } ^ { * }$ the group of characters of $T$ . The equivariant cohomology group $H _ { T } ^ { * }$ can be identified with the polynomial ring $S ( \hat { T } )$ , the symmetric algebra on the free abelian group $\hat { T }$ .

Theorem 3.1 Let $B$ be a connected solvable group with unipotent radical $N$ and Levi decomposition $B = T N$ . Let $\alpha _ { 1 } , \ldots , \alpha _ { d } \in \hat { T }$ denote the weights of $T$ on $\mathfrak { n } = L i e \ N$ . Let $X$

be a complete $B$ -variety on which $N$ acts with finitely many orbits $X _ { 1 } ^ { 0 } , \ldots , X _ { n } ^ { 0 }$ . These are a paving of $X$ by $B$ -stable affines; let $X _ { 1 } \ldots , X _ { n }$ denote the closures, so $\{ [ X _ { 1 } ] _ { T } , \dots , [ X _ { n } ] _ { T } \}$ are a basis for $H _ { * } ^ { T } ( X )$ . Let $\{ x _ { 1 } , \ldots , x _ { n } \}$ denote the dual basis of $H _ { T } ^ { * } ( X )$ . Write

$$
x _ {i} x _ {j} = \sum_ {k} a _ {i j} ^ {k} x _ {k}
$$

with $a _ { i j } ^ { k } \in H _ { T } ^ { * } = S ( \hat { T } )$ . Then each $a _ { i j } ^ { k }$ can be written as a sum of monomials $\alpha _ { 1 } ^ { i _ { 1 } } \cdot \cdot \cdot \alpha _ { d } ^ { i _ { d } }$ · · · αd , id with nonnegative integer coefficients.

Note that the constant term in each $a _ { i j } ^ { k }$ (i.e., the coefficient of $\alpha _ { 1 } ^ { 0 } \cdots \alpha _ { d } ^ { 0 }$ ) is nonnegative by the above theorem. This is the coefficient that occurs in the multiplication in the ordinary cohomology $H ^ { * } ( X )$ . The reason is that our hypotheses imply $H ^ { * } ( X ) =$ $H _ { T } ^ { * } ( X ) / H _ { T } ^ { > 0 } \cdot H _ { T } ^ { * } ( X )$ (see [GKM]).

The next result is the key ingredient in the proof of Theorem 3.1. In this theorem, $N$ is not assumed to act with finitely many orbits. The result also holds with equivariant Chow groups in place of equivariant Borel-Moore homology.

Theorem 3.2 Let $B$ be a connected solvable group with unipotent radical $N$ , and let $T \subset B$ be a maximal torus, so $B = T N$ . Let $\alpha _ { 1 } , \dotsc , \alpha _ { d } \in \hat { T }$ denote the weights of $T$ acting on $\mathfrak { n } = L i e \ N$ . Let $X$ be a scheme with a $B$ -action and $Y$ a $T$ -stable subvariety of $X$ . Then there exist $B$ -stable subvarieties $D _ { 1 } , \ldots , D _ { r }$ of $X$ such that in $H _ { * } ^ { T } ( X )$ ,

$$
[ Y ] _ {T} = \sum f _ {i} [ D _ {i} ] _ {T}
$$

where each $f _ { i } \in H _ { T } ^ { * }$ can be written as a linear combination of monomials in $\alpha _ { 1 } , \ldots , \alpha _ { d }$ with nonnegative integer coefficients.

The following lemma was pointed out to me by Michel Brion.

Lemma 3.3 Suppose the connected solvable group $B = T N$ acts on $X$ and that $N$ has finitely many orbits on $X$ . Then each $N$ -orbit is $B$ -stable (in fact, the $B$ -orbit of a $T$ -fixed point).

Proof: $B$ has finitely many orbits on $X$ (as the subgroup $N$ does); as each $N$ -orbit is $N$ -stable, it is a finite union of $N$ -orbits. Let $\boldsymbol { B } \cdot \boldsymbol { x } ^ { \prime } \simeq \boldsymbol { B } / B ^ { \prime }$ be an orbit, where $B ^ { \prime }$ is the stabilizer of $x ^ { \prime }$ . As each $N$ -orbit is isomorphic to affine space (see e.g. [KN]), the odd cohomology of $B \cdot x ^ { \prime }$ vanishes, so $B ^ { \prime }$ must contain a maximal torus of $B$ . As all maximal tori of $B$ are conjugate [Bo, Corollary 11.3], there is some $b \in B$ such that $B ^ { \prime } = b B _ { 1 } b ^ { - 1 }$ , where $B _ { 1 } \supset T$ . Then $\boldsymbol { B } \cdot \boldsymbol { x } ^ { \prime } = \boldsymbol { B } \cdot \boldsymbol { x }$ where $x = b ^ { - 1 } x ^ { \prime }$ ; moreover $B _ { 1 }$ is the stabilizer of $x$ . Hence $B \cdot x$ is the $N$ -orbit of the $T$ -fixed point $x$ . 

Proof of Theorem 3.1: The group $\tilde { B } = T \cdot ( N \times N )$ (semi-direct product) acts on $X \times X$ by $t \cdot ( n _ { 1 } , n _ { 2 } ) ( p _ { 1 } , p _ { 2 } ) = ( t n _ { 1 } p _ { 1 } , t n _ { 2 } p _ { 2 } )$ . The unipotent radical $N \times N$ has finitely many orbits $X _ { i } ^ { 0 } \times X _ { j } ^ { 0 }$ on $X \times X$ , with closures $X _ { i } \times X _ { j }$ , so $H _ { * } ^ { T } ( X \times X )$ is a free $H _ { T } ^ { * }$ -module with basis $[ X _ { i } \times X _ { j } ] _ { T }$ . By Proposition 2.2, if $\begin{array} { r } { x _ { i } x _ { j } = \sum _ { k } a _ { i j } ^ { k } x _ { k } } \end{array}$ then $\delta _ { * } [ X _ { k } ] _ { T } = [ \delta ( X _ { k } ) ] _ { T } =$

$\begin{array} { r } { \sum _ { i j } a _ { i j } ^ { k } [ X _ { i } \times X _ { j } ] _ { T } } \end{array}$ . The coefficients $a _ { i j } ^ { k }$ are uniquely determined by the expansion of $\delta _ { * } | X _ { k } | _ { T }$ because the classes $[ X _ { i } \times X _ { j } ]$ are linearly independent over $H _ { T } ^ { * }$ . By Theorem 3.2, these coefficients can be written as monomials in $\alpha _ { 1 } , \ldots , \alpha _ { d }$ with nonnegative integer coefficients, where $\alpha _ { 1 } , \ldots , \alpha _ { d }$ are the weights of $T$ on Lie $( N \times N )$ (which are the same as the weights of $T$ on $\mathfrak { n }$ ). 

Proof of Theorem 3.2: First consider the case where $\dim N = 1$ ; then $B / T \stackrel { \sim } { \to } N \stackrel { \varphi } { \to } \mathbb { G } _ { a }$ , where $\mathbb { G } _ { a } \cong \mathbb { A } ^ { 1 }$ is the additive group. Write $\alpha ~ = ~ \alpha _ { 1 }$ . We have $B \ = \ N T$ , and the map $B / T \ { \stackrel { \sim } { \to } } \ N$ sends $n T  n$ . Now, $B$ acts on $B / T$ by left multiplication. Via the isomorphism of $B / T$ with $N$ , we obtain an action of $B$ on $N$ ; the subgroup $T \subset B$ acts on $N$ by conjugation, and the subgroup $N$ acts by left multiplication. The action of $T$ by conjugation on $N$ corresponds under $\varphi$ to an action of $T$ on $\mathbb { A } ^ { 1 }$ with weight $\alpha$ . Embed $B / T \hookrightarrow \mathbb { P } ^ { 1 }$ by $n T \mapsto [ \varphi ( n ) : 1 ]$ . The action of $B$ on $B / T$ extends to an action on $\mathbb { P } ^ { 1 }$ : the element $t n \in B$ acts by the matrix

$$
\left( \begin{array}{c c} {\alpha (t)} & {\varphi (n)} \\ {0} & {1} \end{array} \right).
$$

The point $\infty = [ 1 : 0 ]$ is fixed by $B$ , while the point $0 = [ 0 : 1 ]$ is fixed by $T$

Now, $B$ acts on $B \times ^ { T } \ : X$ by left multiplication: $b \cdot ( b ^ { \prime } , x ) = ( b b ^ { \prime } , x )$ . Under the isomorphism $\theta : B \times ^ { T } X  B / T \times X$ taking $( b , x )$ to $( b T , b x )$ , the $B$ -action corresponds to the product action on $B / T \times X$ . This extends to a $B$ -action on $\mathbb { P } ^ { 1 } \times X$ . The projections $\pi : \mathbb { P } ^ { 1 } \times X \to \mathbb { P } ^ { 1 }$ and $\rho : \mathbb { P } ^ { 1 } \times X  X$ are $B$ -equivariant.

If $Y \subset X$ is a $T$ -invariant subvariety then $B \times ^ { T } Y$ is a $B$ -invariant subvariety of $B \times ^ { T } X$ . Let $Z$ be the Zariski closure of $\theta ( B \times ^ { T } Y )$ in $\mathbb { P } ^ { 1 } \times X$ ; $\theta ( B \times ^ { T } Y )$ and $Z$ are $B$ -invariant subvarieties of $\mathbb { P } ^ { 1 } \times X$ . Let $\pi z$ denote the restriction of $\pi$ to $Z$ .

Let $[ w _ { 0 } : w _ { 1 } ]$ be projective coordinates on $\mathbb { P } ^ { 1 }$ , and $w$ the rational function $\frac { w _ { 0 } } { w _ { 1 } }$ . Let $g = \pi _ { Z } ^ { * } w$ ; then $w$ (and hence $g$ ) are rational functions which are $T$ -eigenvectors of weight $- \alpha$ . By [Br, Theorem 2.1]2 we have in $H _ { * } ^ { T } ( \mathbb { P } ^ { 1 } \times X )$ the relation $[ \mathrm { d i v } _ { Z } g ] _ { T } = \alpha [ Z ] _ { T }$ . Therefore, in $H _ { * } ^ { T } X$ we have the relation

$$
\rho_ {*} [ \operatorname {d i v} _ {Z} g ] _ {T} = \alpha \rho_ {*} [ Z ] _ {T} \tag {3.4}
$$

Now, $\pi _ { Z } ^ { - 1 } ( 0 ) = \{ 0 \} \times Y$ (cf. [KN]). Also, $\pi _ { Z } ^ { - 1 } ( \infty ) = \{ \infty \} \times D$ where $D$ is a subscheme of $X$ . Therefore (3.4) yields

$$
[ Y ] _ {T} = [ D ] _ {T} + \alpha \rho_ {*} [ Z ] _ {T}
$$

As $\pi z$ is $B$ -equivariant, and $\infty \in \mathbb { P } ^ { 1 }$ is $B$ -fixed, it follows that $\{ \infty \} \times D$ , and hence $D$ , are $B$ -invariant. Each irreducible component $D _ { i }$ $i = 1 , \ldots , r$ ) of $D$ is therefore $B$ -invariant (as $B$ is connected) and if $m _ { i }$ is the multiplicity of $D _ { i }$ in $D$ then $\begin{array} { r } { [ D ] _ { T } = \sum _ { i = 1 } ^ { r } m _ { i } [ D _ { i } ] _ { T } } \end{array}$ . Likewise, is $B$ -equivariant and $Z$ is $B$ -invariant. If $Z _ { i }$ is a component of $Z$ then the map $\rho$ $\rho | _ { Z _ { i } }$ of $Z _ { i }$ onto its image in $X$ is finite if and only if the map $\rho _ { T } | _ { Z _ { i T } }$ of $Z _ { i T }$ onto its image in $X _ { T }$ is finite, and the degrees of the maps are the same. If we list the components of $\rho ( Z )$ which are finite images of components of $Z$ as $D _ { r + 1 } , \ldots , D _ { s }$ , it follows that each of

these components is $B$ -invariant and that $\begin{array} { r } { \rho _ { * } [ Z ] _ { T } = \sum _ { i = r + 1 } ^ { s } m _ { i } [ D _ { i } ] _ { T } } \end{array}$ where $m _ { i }$ are positive integers. We conclude that

$$
[ Y ] _ {T} = \sum_ {i = 1} ^ {r} m _ {i} [ D _ {i} ] _ {T} + \sum_ {i = r + 1} ^ {s} m _ {j} \alpha [ D _ {i} ] _ {T} \tag {3.5}
$$

where the $D _ { i }$ are $B$ -invariant. This proves the result if $\dim N = 1$ .

To prove the result in general, we can find a subgroup $N ^ { \prime } ~ \subset ~ N$ such that $N ^ { \prime }$ is normal in $B$ and $\dim N / N ^ { \prime } \ = \ 1$ . Let $\alpha$ be the weight of $T$ on Lie $( N / N ^ { \prime } )$ . Define $B ^ { \prime } = N ^ { \prime } T \subset B = N T$ . By induction, we may assume the result is true for $B ^ { \prime }$ . It is enough to show that given a $B ^ { \prime }$ -invariant subvariety $Y \subset X$ , we can write $[ Y ] _ { T }$ as in (3.5), with $B$ -invariant $D _ { i }$ . For this we modify the above proof, as follows. Replace $B / T$ , $B \times ^ { T } X$ , and $B \times ^ { T } Y$ by $B / B ^ { \prime }$ , $B \times ^ { B ^ { \prime } } X$ , and $B \times ^ { B ^ { \prime } } Y$ ; the map $\theta$ now takes $B \times ^ { B ^ { \prime } } X$ to $B / B ^ { \prime } \times X$ . Again $\varphi : B / B ^ { \prime } \stackrel { \cong } { \to } \mathbb { G } _ { a } = \mathbb { A } ^ { 1 }$ and $T$ acts by weight $\alpha$ on $\mathbb { A } ^ { 1 }$ . We can embed $B / B ^ { \prime } \hookrightarrow \mathbb { P } ^ { 1 }$ as before; the point $\infty = [ 1 : 0 ]$ is fixed by $B$ , and $[ 0 : 1 ]$ is fixed by $B ^ { \prime }$ . With these modifications, (3.5) is proved as above. This proves the theorem. 

# 4 Schubert varieties

# 4.1 Peterson’s conjecture

Let $G$ be a complex semisimple group and $B \supset T$ a Borel subgroup and maximal torus, respectively. Let $N$ be the unipotent radical of $B$ ; let $B ^ { - } = T N ^ { - }$ be the opposite Borel. Choose a system of positive roots so that the roots in $\mathfrak { n }$ are positive. Let $W = N ( T ) / T$ denote the Weyl group; we abuse notation and write $w$ for an element of $W$ and also for a representative in $N ( T )$ . Let $X = G / B$ the flag variety. The $T$ -fixed points are $\{ w B \} _ { w \in W }$ ; let $X _ { w } ^ { \mathrm { 0 } } = N \cdot w B \subset X$ and $Y _ { w } ^ { 0 } = N ^ { - } \cdot w B$ . Then $\begin{array} { r } { X = \coprod _ { w } X _ { w } ^ { 0 } } \end{array}$ (resp $\begin{array} { r } { X = \coprod _ { w } Y _ { w } ^ { 0 } ) } \end{array}$ is a decomposition of $X$ as a disjoint union of finitely many $N$ (resp. $N ^ { - }$ )-orbits. Let $X _ { w }$ and $Y _ { w }$ denote the closures of $X _ { w } ^ { 0 }$ and $Y _ { w } ^ { 0 }$ , and $\{ x _ { w } \}$ and $\{ y _ { w } \}$ the bases of $H _ { T } ^ { * } X$ dual (in the sense of Proposition 2.1) to $\{ [ X _ { w } ] _ { T } \}$ and $\{ [ Y _ { w } ] _ { T } \}$ .

Let $\alpha _ { 1 } , \ldots , \alpha _ { \ell }$ denote the simple roots. Any weight of $T$ on $\mathfrak { n }$ (resp. $\mathfrak { n } ^ { - }$ ) is a nonnegative (resp. nonpositive) linear combination of the simple roots. Therefore, the next corollary is an immediate consequence of Theorem 3.1.

Corollary 4.1 With notation as above, write $\begin{array} { r } { x _ { u } x _ { v } = \sum _ { w } a _ { u v } ^ { w } x _ { w } } \end{array}$ and $\begin{array} { r } { y _ { u } y _ { v } = \sum _ { v } b _ { u v } ^ { w } y _ { w } } \end{array}$ with $a _ { u v } ^ { w }$ and $b _ { u v } ^ { w }$ in $H _ { T } ^ { * }$ . Then $a _ { u v } ^ { w }$ (resp. $b _ { u v } ^ { w }$ ) is a linear combination of monomials in the $\alpha _ { i }$ , with nonnegative (resp. nonpositive) coefficients. 

Remark. Theorem 3.1 can be applied to the varieties $X _ { w }$ and $Y _ { w }$ , which are in general singular, to yield an analogue of Corollary 4.1 for $H _ { T } ^ { * } ( X _ { w } )$ and $H _ { T } ^ { * } ( Y _ { w } )$ . The analogous result also holds for partial flag varieties.

Because $X$ is smooth, the map $H _ { T } ^ { * } ( X ) \stackrel { \cap [ X ] _ { T } } {  } H _ { * } ^ { T } ( X )$ is an isomorphism. The next lemma is known (cf. [P]) but for lack of reference we give a proof.

Lemma 4.2 The map $H _ { T } ^ { * } ( X ) \stackrel { \cap [ X ] _ { T } } {  } H _ { * } ^ { T } ( X )$ takes $y _ { w }$ to $[ X _ { w } ] _ { T }$

Proof: We can identify $H _ { T } ^ { * } ( X )$ with $\mathrm { H o m } _ { H _ { T } ^ { * } } ( H _ { * } ^ { T } ( X ) , H _ { T } ^ { * } )$ (see the proof of Proposition 2). Hence, any $\gamma \in H _ { T } ^ { * } ( X )$ is uniquely determined by the values $\pi _ { * } ^ { T } ( \gamma \cap h ^ { \prime } )$ as $h ^ { \prime }$ ranges over the basis $\{ [ Y _ { w ^ { \prime } } ] _ { T } \}$ of $H _ { * } ^ { T } ( X )$ .

Now, if $\gamma \in H _ { T } ^ { * } ( X )$ satisfies $\gamma \cap [ X ] _ { T } = h$ , then $\gamma \cap h ^ { \prime } = h \cdot h ^ { \prime }$ . Indeed, the intersection product on $H _ { * } ^ { T } ( X )$ satisfies: if $\gamma ^ { \prime } \cap [ X ] _ { T } = h ^ { \prime }$ , then $\gamma \cdot \gamma ^ { \prime } \cap [ X ] _ { T } = h \cdot h ^ { \prime }$ ; but $\gamma \cdot \gamma ^ { \prime } \cap [ X ] _ { T } =$ $\gamma \cap ( \gamma ^ { \prime } \cap [ X ] _ { T } ) = \gamma \cap h ^ { \prime }$ .

Combining these facts, we see that to show $y _ { w } \cap [ X ] _ { T } = [ X _ { w } ] _ { T }$ , it suffices to show

$$
\pi_ {*} ^ {X} \big ([ X _ {w} ] _ {T} [ Y _ {w ^ {\prime}} ] _ {T} \big) = \pi_ {*} ^ {X} \big (y _ {w} \cap [ Y _ {w ^ {\prime}} ] _ {T} \big) = \delta_ {w w ^ {\prime}}.
$$

Now, for any $w , w ^ { \prime }$ , the intersection $X _ { w } \cap Y _ { w ^ { \prime } }$ is $T$ -invariant, and is known to satisfy codim $X _ { w } \cap Y _ { w ^ { \prime } } = \mathrm { c o d i m }$ Xw + codim $Y _ { w ^ { \prime } }$ . (Indeed, by [KL], $X _ { w } \cap Y _ { w ^ { \prime } } ^ { 0 }$ is irreducible and of dimension $\dim X - \dim X _ { w } - \dim Y _ { w ^ { \prime } }$ , but by [F, p. 137], each component of $X _ { w } \cap Y _ { w ^ { \prime } }$ has at least that dimension. It follows that $X _ { w } \cap Y _ { w ^ { \prime } } ^ { 0 }$ is dense in $X _ { w } \cap Y _ { w ^ { \prime } }$ .) Hence $[ X _ { w } ] _ { T } [ Y _ { w ^ { \prime } } ] _ { T }$ is a multiple of $[ X _ { w } \cap Y _ { w ^ { \prime } } ] _ { T }$ . If $\dim X _ { w } \cap Y _ { w ^ { \prime } } > 0$ , then $\dim ( X _ { w } \cap Y _ { w ^ { \prime } } ) _ { T } > \dim B T$ , so $\pi _ { \ast } ^ { X } ( [ X _ { w } \cap Y _ { w ^ { \prime } } ] _ { T } ) = 0$ . If $\dim X _ { w } \cap Y _ { w ^ { \prime } } = 0$ , then $w = w ^ { \prime }$ and $X _ { w }$ and $Y _ { w }$ intersect with multiplicity 1 at the point $w B$ [C, Prop. 2]. Hence $\pi _ { T } ^ { X } : X _ { T }  B T$ maps $( X _ { w } \cap Y _ { w } ) _ { T }$ isomorphically onto $B T$ , and therefore $\pi _ { * } ^ { X } ( [ X _ { w } ] _ { T } [ Y _ { w } ] _ { T } ) = \pi _ { * } ^ { X } ( [ X _ { w } \cap Y _ { w } ] _ { T } ) = 1$ . This proves the lemma. 

The intersection product on $H _ { \ast } ^ { T } ( X )$ is induced by the product on $H _ { T } ^ { * } ( X )$ , via the isomorphism $\cap [ X ] _ { T }$ . The above lemma and Corollary 4.1 therefore imply:

Corollary 4.3 The intersection product on $H _ { * } ^ { T } ( X )$ is given by $\begin{array} { r } { [ Y _ { u } ] _ { T } [ Y _ { v } ] _ { T } = \sum _ { w } a _ { u v } ^ { w } [ Y _ { w } ] _ { T } } \end{array}$ (resp. $\begin{array} { r } { [ X _ { u } ] _ { T } [ X _ { v } ] _ { T } = \sum _ { w } b _ { u v } ^ { w } [ X _ { w } ] _ { T } ) } \end{array}$ , where each $a _ { u v } ^ { w }$ (resp. $b _ { u v } ^ { w }$ ) in $H _ { T } ^ { * }$ is a sum of monomials in the $\alpha _ { 1 } , \ldots , \alpha _ { \ell }$ , with nonnegative (resp. nonpositive) coefficients. 

Corollaries 4.1 and 4.3 were conjectured by Dale Peterson.

Example. As a concrete example, we work out the case of the flag variety of $S L _ { 2 }$ . Here, we take $B$ (resp. $B ^ { - }$ , $T$ ) to be the upper triangular (resp. lower triangular, diagonal) matrices; we identify $X$ with $\mathbb { P } ^ { 1 }$ , acting as usual. Then $W = \{ 1 , s \}$ and the Schubert varieties are $X _ { 1 } = \left\lfloor 1 : 0 \right\rfloor$ , $X _ { s } = X$ , $Y _ { 1 } = X$ , $Y _ { s } = | 0 : 1 |$ . The character group of $T$ is ${ \hat { T } } = \mathbb { Z } \cdot x \cong \mathbb { Z }$ , and the positive root is $\alpha = 2 x$ . The ring $H _ { T } ^ { * } = \mathbb { C } [ x ]$ . The action of $T$ on $\mathbb { P } ^ { 1 }$ is with weights $\pm 1$ , so $H _ { T } ^ { * } X = \mathbb { C } [ x , h ] / ( h + x ) ( h - x )$ . We will identify $H _ { T } ^ { * } X$ with $H _ { * } ^ { T } X$ via $\cap [ X ] _ { T }$ . Under this isomorphism, $[ X _ { s } ] _ { T } = [ Y _ { 1 } ] _ { T } = 1$ . If $[ z _ { 0 } : z _ { 1 } ]$ are projective coordinates on $\mathbb { P } ^ { 1 }$ , then $z _ { 0 }$ may be viewed as a section of $\mathcal { O } ( 1 )$ which is a $T$ -eigenvector of weight $^ { - 1 }$ . Then $z _ { 0 } \otimes 1$ is a $T$ -invariant section of $\mathcal { O } ( 1 ) \otimes \mathbb { C } _ { 1 }$ (here $\mathbb { C } _ { 1 }$ is the trivial line bundle with $T$ with weight 1). The zero-scheme of $z _ { 0 } \otimes 1$ is $[ 0 : 1 ]$ , so we conclude $[ Y _ { s } ] _ { T } = [ 0 : 1 ] _ { T } = c _ { 1 } ^ { T } ( { \mathcal { O } } ( 1 ) \otimes \mathbb { C } _ { 1 } ) = h + x$ . Similarly, $[ X _ { 1 } ] _ { T } = h - x$ . The only interesting multiplication among the classes $[ X _ { w } ] _ { T }$ is

$$
[ X _ {1} ] _ {T} \cdot [ X _ {1} ] _ {T} = (h - x) ^ {2} = h ^ {2} - 2 h x + x ^ {2} = 2 x ^ {2} - 2 h x = - 2 x (h - x) = - \alpha [ X _ {1} ] _ {T}.
$$

Similarly, the only interesting multiplication among the classes $[ Y _ { w } ] _ { T }$ is

$$
[ Y _ {s} ] _ {T} [ Y _ {s} ] _ {T} = \alpha [ Y _ {s} ] _ {T}.
$$

These agree with Corollaries 4.1 and 4.3.

# 4.2 Billey’s conjecture

Kostant and Kumar [KK] defined functions (for each $w \in W$ ) $\xi ^ { w } : W \to S ( \hat { T } ) \subset S ( { \sf t ^ { * } } )$ , and showed that for any $u , v \in W$ , one can write

$$
\xi^ {u} \xi^ {v} = \sum_ {w} p _ {w} ^ {u v} \xi^ {w}
$$

for unique $p _ { w } ^ { u v } \in S ( { \sf t ^ { * } } )$ . Billey [Bi] observed in examples that that if $\nu \in { \mathfrak { t } }$ satisfies $\alpha ( \nu ) > 0$ for all positive roots $\alpha$ , then $p _ { w } ^ { u v } ( \nu ) \geq 0$ , and asked if a geometric proof was possible.

Arabia [A] proved the following relation of the functions $\xi ^ { w }$ to the $T$ -equivariant equivariant cohomology of the flag variety. We use the notation of the preceding subsection: thus, $i _ { w } : w B \to G / B = X$ denotes the inclusion, and $i _ { w } ^ { * } : H _ { T } ^ { * } ( X )  H _ { T } ^ { * } ( w B ) = H _ { T } ^ { * }$ the pullback. As usual, we identify $H _ { T } ^ { * } ( X )$ with $H _ { * } ^ { T } ( X )$ .

Theorem 4.4 (1) $i _ { u } ^ { * } x _ { w } = \xi ^ { w ^ { - 1 } } ( u ^ { - 1 } )$ .

(2) pw−1 $p _ { w ^ { - 1 } } ^ { u ^ { - 1 } , v ^ { - 1 } } = a _ { u v } ^ { w }$ u−1,v−1 a u v .

This is proved (in the general Kaˇc-Moody case) in [A, Theorem 4.2.1]. We have stated this theorem using the conventions of [KK] for the functions $\xi ^ { w }$ ; below we explain the relationship between the conventions of [A] and [KK]. Note that (2) follows immediately from (1), since (as noted by Arabia) the pullback $\oplus i _ { w } ^ { * } : H _ { T } ^ { * } ( X ) \to \oplus H _ { * } ^ { I } ^ { \prime }$ is injective.

As a consequence, we obtain Billey’s conjecture:

Corollary 4.5 If ν ∈ t satisfies $\alpha ( \nu ) > 0$ for all positive roots $\alpha$ , then $p _ { w } ^ { u v } ( \nu ) \geq 0$ .

Proof: This follows immediately from the preceding corollary and Corollary 4.3.

We now discuss the conventions of [A] and [KK]. Let $\mathbb { C } \lfloor W \rfloor$ denote the group algebra over $\mathbb { C }$ of $W$ ; let $Q$ be the quotient field of $S ( \mathrm { t ^ { * } } )$ . Kostant and Kumar set $Q _ { W } = \mathbb { C } [ W ] \otimes Q$ ; Arabia defines $Q$ and $Q _ { W }$ with rational rather than complex coefficients, but we will ignore this difference. Both [KK] and [A] define elements $\xi ^ { w } \in \operatorname { H o m } _ { Q } ( Q _ { W } , Q )$ , but with different conventions: if we use $\xi ^ { w }$ for the elements defined in [KK] and $\xi _ { A } ^ { w }$ for the elements defined in [A], then $\xi ^ { w } = \xi _ { A } ^ { w ^ { - 1 } }$ .

Let $F ( W , Q )$ denote the set of functions from $W$ to $Q$ . Both [KK] and [A] use identifications ${ \cal F } ( W , Q ) \stackrel { \simeq } { \to } \mathrm { H o m } _ { Q } ( Q _ { W } , Q )$ ; we will denote their respective identifications by

$$
f \mapsto f _ {K}, \quad \text {w h e r e} f _ {K} \left(\delta_ {u} \otimes 1\right) = f (u) \quad [ \mathrm {K K}, (4. 1 7) ]
$$

$$
f \mapsto f _ {A}, \quad \text {w h e r e} f _ {A} \left(\delta_ {u} \otimes 1\right) = f \left(u ^ {- 1}\right) \quad [ A, \text {S e c t i o n} 4. 1 ].
$$

If we define $f ^ { w }$ and $g ^ { w }$ in $F ( W , Q )$ by $f _ { K } ^ { w } = \xi ^ { w }$ , $g _ { A } ^ { w } = \xi _ { A } ^ { w }$ , then $f ^ { w } ( u ) = g ^ { w ^ { - 1 } } ( u ^ { - 1 } )$ .

Arabia uses the injection

$$
\oplus i _ {u} ^ {*}: H _ {T} ^ {*} (X) \hookrightarrow \oplus H _ {T} ^ {*} \simeq F (W, S (\mathfrak {t} ^ {*})) \subset F (W, Q)
$$

to identify $H _ { T } ^ { * } ( X )$ with a subset of $F ( W , Q )$ . In his paper, he proves that under this identification, $g ^ { w }$ corresponds to what we have denoted by $x _ { w } \in H _ { T } ^ { * } ( X )$ . In [KK] there is no separate notation introduced for the $f ^ { w }$ , but rather they are identified with $\xi ^ { w }$ , i.e., the $\xi ^ { w }$ are viewed as elements of $F ( W , Q )$ . If we return to their notation, we see $\xi ^ { w ^ { - 1 } } ( u ^ { - 1 } ) = i _ { u } ^ { * } x _ { w }$ , as stated in Theorem 4.4.

Note that if we let $\xi _ { B } ^ { w }$ denote the functions used by Billey, then $\xi _ { B } ^ { w } ( u ) = \xi ^ { w ^ { - 1 } } ( u ^ { - 1 } )$

# 4.3 The Kaˇc-Moody case

The analogues of Corollaries 4.1 and 4.5 are also valid for flag varieties (complete or partial) of Kaˇc-Moody groups. The key point is that such a flag variety, although in general infinite dimensional, can be approximated by finite dimensional varieties for which the hypotheses of Theorem 3.1 are satisfied. Indeed, this was exactly the geometric motivation of Kumar and Nori. We will briefly sketch how this works in equivariant cohomology. The basic facts we need can be found in [Sl], to which we refer for a more detailed explanation of the notation. Let $G$ be a Kaˇc-Moody group and $B$ a Borel subgroup; let $X = G / B$ denote the flag variety. The group $B$ is a proalgebraic group (inverse limit of algebraic groups), and it has a Levi decomposition $B = T N$ , where $N$ is a proalgebraic prounipotent group (denoted by $U$ in [Sl] and [KN]) and $T$ is a finite dimensional torus. The space $X$ has the structure of ind-variety: it is realized as a union $X = \cup _ { k > 0 } X _ { k }$ , where each $X _ { k }$ is a finite dimensional variety embedded as a closed subvariety of $X _ { k + 1 }$ . Here $X _ { k }$ is defined as follows. We have $X = \coprod X _ { w } ^ { 0 }$ , realizing $X$ as a disjoint union of Schubert cells $X _ { w } ^ { 0 } = B \cdot w B$ . The union is over all elements of the Weyl group $W$ ; each $X _ { w } ^ { 0 }$ is isomorphic to the affine space $\mathbb { A } ^ { l ( w ) }$ , where $l ( w )$ is the length of $w$ . By definition, $\begin{array} { r } { X _ { k } = \coprod _ { l ( w ) \leq k } X _ { w } ^ { 0 } } \end{array}$ ; this is a finite dimensional projective variety which is paved by affines. Moreover, each $X _ { k }$ is $B$ -stable, and there exists a subgroup $N _ { k } \subset N$ , normal in $B$ , such that $B _ { k } = B / N _ { k }$ is a finite dimensional solvable group, and the action of $B$ on $X _ { k }$ factors through the map $B  B _ { k }$ . Each $X _ { k }$ therefore satisfies the hypotheses of Theorem 3.1. As in the finite case, there is a set of simple roots $\alpha _ { 1 } , \ldots , \alpha _ { l }$ in $\mathrm { t ^ { * } }$ , and moreover, for any $k$ , every weight in Lie $( N / N _ { k } )$ is a nonnegative linear combination of simple roots.

Now, for any fixed $i$ , the pullback $H _ { T } ^ { i } ( X )  H _ { T } ^ { i } ( X _ { k } )$ is a canonical isomorphism for $k$ sufficiently large (as the decomposition of $X$ into Schubert cells makes $X$ a CW-complex, and $X _ { k }$ contains all cells in $X$ of dimension $\leq ~ 2 k$ , and similarly for the mixed spaces $X _ { k T }$ and $X _ { T }$ ). There is a basis $\{ x _ { w } \}$ of $H _ { T } ^ { * } ( X )$ dual to the fundamental classes $[ X _ { w } ] _ { T }$ , in the sense that the pullbacks to $H _ { T } ^ { * } ( X _ { k } )$ form a basis dual to the $[ X _ { w } ] _ { T } \in H _ { * } ^ { T } ( X _ { k } )$ , for $l ( w ) \leq k$ . This basis does not depend on $k$ , as can be seen using property (2.2) of the pairing, applied to the inclusion map of $X _ { k }$ into $X _ { k + 1 }$ . Theorem 3.1 therefore implies the following corollary, also conjectured by Peterson.

Corollary 4.6 With notation as above, if $X$ is the flag variety of a Kaˇc-Moody group, with basis $\{ x _ { w } \}$ of $H _ { T } ^ { * } ( X )$ , then $\begin{array} { r } { x _ { u } x _ { v } = \sum _ { w } a _ { u v } ^ { w } x _ { w } } \end{array}$ , with $a _ { u v } ^ { w } \in H _ { T } ^ { * }$ a linear combination of monomials in the $\alpha _ { i }$ , with nonnegative coefficients. 

# References

[A] A. Arabia, Cohomologie $T$ -´equivariant de la vari´et´e de drapeaux d’un groupe de Kaˇc-Moody, Bull. Math. Soc. France 117 (1989), 129-165.   
[Bi] S. Billey, Kostant polynomials and the cohomology ring of $G / B$ , Duke Math. J. 96 (1999), 205-224.   
[Bo] A. Borel, Linear Algebraic Groups, second enlarged edition, Springer-Verlag, 1991.

[Br] M. Brion, Equivariant Chow groups for torus actions, J. Transformation Groups 2 (1997), 225-267.   
[Br2] M. Brion, Equivariant cohomology and equivariant intersection theory, in: A. Broer and A. Daigneault (eds.), Representation theories and algebraic geometry, Kluwer, 1998.   
[C] C. Chevalley, Invariants of finite groups generated by reflections, Amer. J. Math 77 (1955), 778-782.   
[E-G] D. Edidin, W. Graham, Equivariant intersection theory, Invent. Math. 131 (1998), 595-634.   
[F] W. Fulton, Intersection Theory, Springer, 1984.   
[F2] W. Fulton, Flags, Schubert polynomials, degeneracy loci and determinantal formulas, Duke Math. J. 65 (1992), 381-420.   
[F3] W. Fulton, Determinantal formulas for orthogonal and symplectic degeneracy loci, J. Diff. Geom. 43 (1996), 276-290.   
[GKM] M. Goresky, R. Kottwitz, R. MacPherson, Equivariant cohomology, Koszul duality, and the localization theorem, Invent. Math. 131 (1998), 25-83.   
[G] W. Graham, The class of the diagonal in flag bundles, J. Diff. Geom. 45 (1997), 471-487.   
[Hi] A. Hirschowitz, Le groupe de Chow ´equivariant, C. R. Acad. Sci. Paris S´erie I, Math. 298 (1984), 87-89.   
[KL] D. Kazhdan, G. Lusztig, Schubert varieties and Poincar´e duality, Proc. of Symposia in Pure Math. 32 (1980), 185-203.   
[KK] B. Kostant, S. Kumar, The nil Hecke ring and cohomology of G/P for a Kaˇc-Moody group, Adv. Math. 62 (1986), 187-237.   
[KN] S. Kumar, M. Nori, Positivity of the cup product in cohomology of flag varieties associated to Kaˇc-Moody groups, International Math. Res. Notices 14 (1998), 757- 763.   
[L-S] A. Lascoux, M.-P. Sch¨utzenberger, Interpolation de Newton `a plusieurs variables, in Seminare D’Algebra, Lecture Notes in Math. 1146 (1983-4), 161-175.   
[Mu] J. Munkres, Elements of Algebraic Topology, Addison-Wesley, 1984.   
[P] D. Peterson, lectures, 1997.   
[P-R] P. Pragacz, J. Ratajski, Formulas for Lagrangian and orthogonal degeneracy loci: the $\tilde { Q }$ -polynomials approach, Compositio Math.

[Sl] P. Slodowy, On the geometry of Schubert varieties attached to Kaˇc-Moody Lie algebras, in: J. Carrell, A. Geramita, P. Russell, eds., Proceedings of the 1984 Vancouver Conference in Algebraic Geometry, Can. Math. Soc. Conf. Proc. 6, Amer. Math. Soc., (1986), 405-442.   
[Sp] E. Spanier, Algebraic Topology, McGraw-Hill, 1966.   
[T] B. Totaro The Chow ring of a classifying space, Contemp. Math., to appear.