# GRAHAM POSITIVITY OF TRIPLE SCHUBERT CALCULUS

YIBO GAO AND RUI XIONG

Abstract. We prove Samuel’s conjecture on certain Graham positivity of the expansion coefficient of two double Schubert polynomials in three sets of variables by establishing a refined version of Graham’s positivity theorem. As a corollary, we prove Kirillov’s conjecture on the positivity of skew divided difference operators applied to Schubert polynomials.

# 1. Introduction

Double Schubert polynomials $\{ \mathfrak { S } _ { w } ( \mathbf { x } ; \mathbf { y } ) \mid w \in S _ { n } \}$ , indexed by permutations, are polynomial representatives of Schubert classes in the torus-equivariant cohomology ring of the flag variety $\operatorname { F l } _ { n } ( \mathbb { C } )$ , where $\mathbf { x } = ( x _ { 1 } , \ldots , x _ { n } )$ and $\mathbf { y } = ( y _ { 1 } , \dots , y _ { n } )$ are sequences of variables. They can be defined via divided difference operators, and enjoy rich algebraic and combinatorial properties. In particular, they can be computed via different combinatorial models including pipe dreams [4, 12] and bumpless pipe dreams [15].

In this paper, we focus on the coefficients $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { t } )$ from the expansion

$$
\mathfrak {S} _ {u} (\mathbf {x}; \mathbf {y}) \cdot \mathfrak {S} _ {v} (\mathbf {x}; \mathbf {t}) = \sum_ {w \in S _ {\infty}} c _ {u, v} ^ {w} (\mathbf {y}, \mathbf {t}) \cdot \mathfrak {S} _ {w} (\mathbf {x}; \mathbf {t}). \tag {1}
$$

In the case $\mathbf { y } = \mathbf { t } = \mathbf { 0 }$ , $c _ { u , v } ^ { w } : = c _ { u , v } ^ { w } ( \mathbf { 0 } , \mathbf { 0 } ) \in \mathbb { N }$ is the Schubert structure constant which is the core to Hilbert’s fifteenth problem, and finding combinatorial models for these coefficients has sparkled tremendous interest throughout the years in the community of algebraic combinatorics and algebraic geometry. In the case where $u$ and $\boldsymbol { v }$ are $k$ -Grassmannian permutations, $\mathfrak { S } _ { u } ( \mathbf { x } ; \mathbf { y } )$ and $\mathfrak { S } _ { v } ( \mathbf { x } ; \mathbf { t } )$ are the factorial Schur polynomials; Molev-Sagan [20] first provided a combinatorial formula for these coefficients and Knutson-Tao [13] provided geometric meanings to the expansion.

Our main result is the following:

Theorem 1.1 ([21, Conjecture 1.1]). For $u , v , w \in S _ { \infty }$ , $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { t } ) \in \mathbb { N } [ t _ { i } - y _ { j } ] _ { i , j \geq 1 } .$

Besides the above-mentioned situations, a well-studied case of Theorem 1.1 is that of separated descents ([9, 14]), i.e. max $\operatorname { D e s } ( u ) \leq \operatorname* { m i n } \operatorname { D e s } ( v )$ , where Samuel [21] established a positive formula, and Fan, Guo and the second author [6] found another formula using puzzles in the generality of double Grothendieck polynomials.

Setting $\mathbf y = \mathbf 0$ , we obtain Kirillov’s conjecture:

Corollary 1.2 ([11, Conjecture 1]). For $u , v , w \in S _ { n }$ , $\partial _ { w / v } \mathfrak { S } _ { u } ( \mathbf { x } ) \in \mathbb { N } [ \mathbf { x } ] .$ .

The skew divided difference operators $\partial _ { w / v }$ , first introduced by Macdonald [18], provide a method for computing Schubert structure constants. These operators have attracted significant attention due to their connections to Fomin-Kirillov algebras [7] . Their generalizations and positivity properties have been extensively studied in works including [2, 3, 17].

Our proof relies on a refined version of Graham’s positivity theorem [8] (Theorem 2.3). To apply this result, we establish a new geometric interpretation (Section 2.3) for the coefficients $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { t } )$ , distinct from the one given by Knutson-Tao [13]. A byproduct of this theorem is a geometric explanation for the positivity in Billey’s formula (Section 2.2).

We end our discussion with a conjecture for Grothendieck polynomials (Section 2.4).

# 2. Proof of the main theorem

2.1. A refined Graham positivity. Let $G$ be a connected, complex, reductive algebraic group, $B \subset G$ be a Borel subgroup, $B ^ { - }$ be its opposite Borel subgroup, $T = B \cap B ^ { - }$ be a maximal torus, $N$ (resp., $N ^ { - }$ ) be the unipotent radical of $B$ (resp., $B ^ { - }$ ), $W = N _ { G } ( T ) / T$ be the Weyl group and $\Phi$ be the associated root system, with positive roots $\Phi ^ { + }$ and simple roots $\Delta = \{ \alpha _ { 1 } , \ldots , \alpha _ { r } \}$ . For $\alpha \in \Phi$ , write $s _ { \alpha }$ for the corresponding reflection, and write $s _ { i }$ for $s _ { \alpha _ { i } }$ for simplicity. For $w \in W$ , its (left) inversion set is $I ( w ) : = \{ \alpha \in \Phi ^ { + } | w ^ { - 1 } \alpha \in \Phi ^ { - } \}$ and its non-inversion set is $J ( w ) : = \{ \alpha \in \Phi ^ { + } \mid w ^ { - 1 } \alpha \in \Phi ^ { + } \} = I ( w w _ { 0 } )$ , where $w _ { 0 }$ is the longest element in $W$ . For each $w \in W$ , we pick a representative of it in $N _ { G } ( T )$ , and also denote it by $w$ , slightly abusing notation.

The flag variety $G / B$ admits a Bruhat decomposition $\textstyle { \bigsqcup _ { w \in W } B ^ { - } w B / B }$ into Schubert cells. Their closures $B ^ { - } w B / B \subseteq G / B$ are the Schubert varieties. The Schubert classes $\{ [ \overline { { B ^ { - } w B / B } } ] _ { T } \mid w \in W \}$ form an $H _ { T } ^ { * } ( \mathsf { p t } )$ -basis of $H _ { T } ^ { * } ( \operatorname { F l } _ { m } ( \mathbb { C } ) )$ .

We define the following closed subgroups of $G$ .

Definition 2.1. For $w \in W$ , define $N ^ { - } ( w ) : = N ^ { - } \cap w N ^ { - } w ^ { - 1 }$ and $B ^ { - } ( w ) = T \cdot N ^ { - } ( w )$

By [10, Section 28], as a variety, $N ^ { - } ( w )$ is isomorphic to the Schubert cell $B ^ { - } w B / B \cong$ $\mathbb { C } ^ { \ell ( w _ { 0 } ) - \ell ( w ) }$ via $x \mapsto x w B / B$ . In particular, $N ^ { - } ( w )$ is connected. Its Lie algebra is

$$
\mathfrak {n} ^ {-} (w) = \operatorname {s p a n} \left(F _ {\alpha} \mid \alpha \in J (w)\right) \subseteq \mathfrak {g} := \operatorname {L i e} G
$$

where $F _ { \alpha }$ is a root vector of weight $- \alpha$ .

Lemma 2.2. If $w s _ { i } > w$ , then $N ^ { - } ( w s _ { i } )$ is a normal subgroup of $N ^ { - } ( w )$ .

Proof. Recall that $[ F _ { \alpha } , F _ { \beta } ] \in \mathbb { C } ^ { \times } F _ { \alpha + \beta }$ if $\alpha + \beta$ is a root, and $[ F _ { \alpha } , F _ { \beta } ] = 0$ otherwise. As $w s _ { i } > w$ , we have $J ( w ) = J ( w s _ { i } ) \cup \{ w \alpha _ { i } \}$ and thus ${ \mathfrak { n } } ^ { - } ( w s _ { i } ) \subset { \mathfrak { n } } ^ { - } ( w )$ , $N ^ { - } ( w s _ { i } )$ is a closed subgroup of $N ^ { - } ( w )$ by [10, Theorem 13.1]. In fact, $\mathfrak { n } ^ { - } ( w s _ { i } )$ is an ideal of $\mathfrak { n } ^ { - } ( w )$ . To check this, take any $\alpha \in J ( w s _ { i } )$ and $\beta \in J ( w )$ , and it suffices to show $[ F _ { \alpha } , F _ { \beta } ] \in \mathfrak { n } ^ { - } ( w s _ { i } )$ . If $\alpha + \beta \notin \Phi$ , $[ F _ { \alpha } , F _ { \beta } ] = 0$ . Thus, consider $\gamma = \alpha + \beta \in \Phi ^ { + }$ . If $\beta \in J ( w s _ { i } )$ , then $\gamma \in J ( w s _ { i } )$ as well; and if $\beta = w \alpha _ { i }$ , $\gamma \neq w \alpha _ { i } \in J ( w )$ , so $\gamma \in J ( w s _ { i } )$ . Indeed, $\mathfrak { n } ^ { - } ( w s _ { i } )$ is an ideal of $\mathfrak { n } ^ { - } ( w )$ and by [10, Theorem 13.3], $N ^ { - } ( w s _ { i } )$ is a normal subgroup of $N ^ { - } ( w )$ . □

We are now in a position to state a refined version of Graham positivity theorem.

Theorem 2.3. Let $B ^ { - }$ act on a non-singular variety $X$ , and let $Y$ be a $B ^ { - } ( w )$ -invariant effective cycle in $X$ . Then there exist $B ^ { - }$ -invariant effective cycles $Z _ { 1 } , \ldots , Z _ { m }$ such that

$$
[ Y ] _ {T} \in \sum_ {i = 1} ^ {m} \mathbb {N} [ - \alpha ] _ {\alpha \in I (w)} \cdot [ Z _ {i} ] _ {T}
$$

in $H _ { T } ^ { * } ( X )$ .

Proof. We use induction on $\ell ( w )$ . When $w = \mathrm { i d }$ , $B ^ { - } ( w ) = B ^ { - }$ , so there is nothing to prove. Assume the theorem holds for $w$ . Let us prove the statement for $w s _ { i } > w$ . By Lemma 2.2, the pair $B ^ { - } ( w s _ { i } ) \subset B ^ { - } ( w )$ satisfies the condition (see [1, p. 384]) of [1, Proposition 19.4.4] with $\chi = - w \alpha _ { i }$ . So there exists $B ^ { - } ( w )$ -invariant effective cycles $Z _ { 1 }$ and $Z _ { 2 }$ such that $[ Y ] _ { T } = [ Z _ { 1 } ] _ { T } + \chi [ Z _ { 2 } ] _ { T }$ . Since $I ( w s _ { i } ) = I ( w ) \cup \{ w \alpha _ { i } \}$ , the inductive step is now established. □

Corollary 2.4. Let $X = G / B$ be the flag variety. Under the above setting, we have

$$
[ Y ] _ {T} = \sum_ {w \in W} \mathbb {N} [ - \alpha ] _ {\alpha \in I (w)} \cdot \left[ \overline {{B ^ {-} w B / B}} \right] _ {T}
$$

in $H _ { T } ^ { * } ( G / B )$ .

Proof. Since flag variety has finite many $B ^ { - }$ -orbits, any $B ^ { - }$ -invariant effective cycle over $G / B$ must be a non-negative combination of Schubert classes $[ \overline { { B ^ { - } w B / B } } ] _ { T }$ . □

Remark. When $w ~ = ~ w _ { 0 }$ is the longest element, $B ^ { - } ( w _ { 0 } ) ~ = ~ T$ and Theorem 2.3 gives Graham’s positivity theorem [8, Theorem 3.2]. Our assumption is stronger than that of Graham’s, since a $B ^ { - } ( w )$ -invariant cycle is necessarily $T$ -invariant, yielding a stronger positivity result where roots are restricted to $I ( w )$ rather than all positive roots.

2.2. A geometric explanation of positivity in Billey’s formula. As an application of Theorem 2.3, we give a geometric explanation of positivity in Billey’s formula [5]. See [22] for a great survey on this subject.

The $T$ -fixed points of $G / B$ are $( G / B ) ^ { T } = \{ w B / B \mid w \in W \}$ . Define the localization to be the restriction map · $| { \bf { \Psi } } _ { w } : H _ { T } ^ { * } ( G / B )  H _ { T } ^ { * } ( w B / B ) \simeq H _ { T } ^ { * } ( \mathsf { p t } )$ . Billey’s formula [5] is a combinatorial formula of the localization of Schubert classes $[ \overline { { B ^ { - } u B / B } } ] _ { T } | _ { w }$ for any $u , w \in W$ . From its explicit form, which we do not provide here, we see that

$$
[ \overline {{B ^ {-} u B / B}} ] _ {T} | _ {w} \in \mathbb {N} [ \alpha ] _ {\alpha \in I (w)}. \tag {2}
$$

We provide a geometric explanation of this positivity using Corollary 2.4.

Recall that the point $w _ { 0 } B / B = B ^ { - } w _ { 0 } B / B$ is invariant under $B ^ { - }$ . So the torus fixed point $w w _ { 0 } B / B$ is invariant under $w B ^ { - } w ^ { - 1 }$ . This implies that $w w _ { 0 } B / B$ is invariant under $B ^ { - } ( w )$ . By Corollary 2.4, we have

$$
[ w w _ {0} B / B ] _ {T} \in \sum_ {u \in W} \mathbb {N} [ - \alpha ] _ {\alpha \in I (w)} \cdot [ \overline {{B ^ {-} u B / B}} ] _ {T}.
$$

Following [19, Section 3] and [1, Section 16.5], for a Weyl group element $w \in W$ , the automorphism $g B \mapsto w g B / B$ induces a left action $w ^ { L } : H _ { T } ^ { * } ( G / B ) \to H _ { T } ^ { * } ( G / B )$ . We remark that $w ^ { L }$ is not $H _ { T } ^ { * }$ (pt)-linear unless $w = \mathrm { i d }$ , but it is semilinear with respect to the automorphism of $H _ { T } ^ { * } ( \mathsf { p t } )$ induced by $w$ . Applying $w _ { 0 } ^ { L }$ to the above, we get

$$
[ w _ {0} w w _ {0} B / B ] _ {T} \in \sum_ {u \in W} \mathbb {N} [ - w _ {0} \alpha ] _ {\alpha \in I (w)} \cdot [ \overline {{B w _ {0} u B / B}} ] _ {T}.
$$

As $I ( w _ { 0 } w w _ { 0 } ) = \{ - w _ { 0 } \alpha | \alpha \in I ( w ) \}$ , replacing $w _ { 0 } w w _ { 0 }$ by $w$ and $w _ { 0 } u$ by $u$ , we can rewrite

$$
[ w B / B ] _ {T} \in \sum_ {u \in W} \mathbb {N} [ \alpha ] _ {\alpha \in I (w)} \cdot \left[ \overline {{B u B / B}} \right] _ {T}. \tag {3}
$$

Now let us take the Poincar´e pairing with $[ \overline { { B ^ { - } u B / B } } ] _ { T }$ on both sides. The left-hand side is $[ \overline { { B ^ { - } u B / B } } ] _ { T } | _ { w }$ , and the right-hand side is the coefficient of $[ \overline { { B u B / B } } ] _ { T }$ in (3) by [1, Proposition 7.3]. This gives (2).

2.3. Application to triple Schubert calculus. We restrict to the case of $G = \mathrm { G L } _ { m } ( \mathbb { C } )$ . By [1, Theorem 10.6.4], the class $[ B ^ { - } \pi B / B ] _ { T }$ is represented by the double Schubert polynomial $\mathfrak { S } _ { \pi } ( \mathbf { x } ; \mathbf { t } )$ . We will not be working with the algebraic definition of $\mathfrak { S } _ { \pi } ( \mathbf { x } ; \mathbf { t } )$ ’s. For any permutation $\pi \in S _ { m }$ , we naturally identify it as $\pi \in S _ { m } \hookrightarrow S _ { \infty }$ via $\pi ( k ) = k$ for all $k > m$ .

Fix permutations $u , v$ . By picking $n \gg 0$ , we can assume Equation (1) only involves those $w \in S _ { n }$ . Let $G : = { \mathrm { G L } } _ { 2 n } ( \mathbb { C } )$ and $B , B ^ { - } , T$ be as above. We identify $H _ { T } ^ { * } ( \mathsf { p t } ) \ =$ $\mathbb { Z } [ t _ { 1 } , \ldots , t _ { 2 n } ]$ with $t _ { i } = - \epsilon _ { i } : = - c _ { 1 } ( \mathbb { C } _ { \epsilon _ { i } } )$ , where $\epsilon _ { i }$ is the character of $T$ corresponding to the $i$ -th diagonal entry. We rename the variables $t _ { n + i } = y _ { i }$ for all $i \in [ n ] : = \{ 1 , 2 , . . . , n \}$ . Consider a special permutation $\tau \in S _ { 2 n }$ such that $\tau ( i ) = n + i$ , $\tau ( n + i ) = i$ for all $i \in [ n ]$ . By [1, Section 16.5], $[ \tau \overline { { B ^ { - } u B / B } } ] _ { T }$ is represented by $\mathfrak { S } _ { u } ( \mathbf { x } ; \tau \mathbf { t } ) = \mathfrak { S } _ { u } ( \mathbf { x } ; \mathbf { y } )$ .

Lemma 2.5. The intersection $\tau \overline { { B ^ { - } u B / B } } \cap \overline { { B ^ { - } v B / B } }$ is proper and transverse at the generic point.

Proof. Let $w _ { 0 } ^ { ( m ) } \in S _ { m }$ be the longest permutation $m \ m { - } 1 \cdots 1$ . For permutations $w , \pi \in$ $S _ { n }$ , write $w \times \pi \in S _ { 2 n }$ as the direct sum of $w$ and $\pi$ ; that is, $w \times \pi ( i )$ is $w ( i )$ if $i \leq n$ , and is $\pi ( i - n ) + n$ if $i > n$ . Since $v \in S _ { n }$ , $s _ { i } v \ > \ v$ for $n \leq i < 2 n$ , and thus $B ^ { - } v B / B$ is invariant under $s _ { i }$ , where $s _ { i } = ( i \ i + 1 )$ is the simple transposition. Therefore, we have $\overline { { B ^ { - } v B / B } } = u _ { 0 } \overline { { B ^ { - } v B / B } }$ where $u _ { 0 } = 1 \times w _ { 0 } ^ { ( n ) }$ . Similarly, $\tau \overline { { B ^ { - } u B / B } } = \tau u _ { 0 } \overline { { B ^ { - } u B / B } }$ . As $u _ { 0 } ^ { - 1 } \tau u _ { 0 } = w _ { 0 } ^ { ( 2 n ) }$ , the lemma follows from [1, Section 19.3]. □

We are now ready to prove our main theorem.

Proof of Theorem 1.1. By Lemma 2.5, we can rewrite the coefficients of interest via

$$
[ \tau \overline {{B ^ {-} u B / B}} \cap \overline {{B ^ {-} v B / B}} ] _ {T} = \sum_ {w \in S _ {n}} c _ {u, v} ^ {w} (\mathbf {y}, \mathbf {t}) \cdot [ \overline {{B ^ {-} w B / B}} ] _ {T}.
$$

Since $\tau \overline { { B ^ { - } u B / B } }$ is closed under $\tau N ^ { - } \tau ^ { - 1 }$ and $B ^ { - } v B / B$ is closed under $N ^ { - }$ , the intersection is closed under $N ^ { - } \cap \tau N ^ { - } \tau ^ { - 1 } = : N ^ { - } ( \tau )$ . By Corollary 2.4, we conclude that $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { t } ) \in$ $ { \mathbb { N } } \mathrm { ! } -  { \alpha } \mathrm { J } _ { \alpha \in I ( \tau ) }$ , where we compute $I ( \tau ) = \{ y _ { j } - t _ { i } \mid 1 \leq i , j \leq n \}$ . □

Next we recall some definitions on (skew) divided difference operators.

Definition 2.6 ([18]). The skew divided difference operator $\partial _ { w / u }$ is characterized by

$$
\partial_ {w} (f g) = \sum_ {v} \partial_ {w / v} (f) \partial_ {v} (g)
$$

for all polynomials $f$ and $g$ . Here, $\partial _ { w } : = \partial _ { i _ { 1 } } \cdot \cdot \cdot \partial _ { i _ { \ell } }$ for any reduced word $w = s _ { i _ { 1 } } \cdot \cdot \cdot s _ { i _ { \ell } }$ , and $\partial _ { i } ( f ) = ( f - s _ { i } f ) / ( x _ { i } - x _ { i + 1 } )$ is the divided difference operator.

See [11, Definition 4] for a more explicit definition of $\partial _ { w / u }$ .

Proof of Corollary 1.2. By [21, Section 2 p. 5] or [6, Proposition 6.4], $\partial _ { w / v } \mathfrak { S } _ { u } ( \mathbf { x } ; \mathbf { y } ) =$ $c _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { x } )$ . Setting $\mathbf y = \mathbf 0$ , we obtain that $\partial _ { w / v } \mathfrak { S } _ { u } ( \mathbf { x } ) = c _ { u , v } ^ { w } ( \mathbf { 0 } , \mathbf { x } ) \in \mathbb { N } [ \mathbf { x } ]$ by Theorem 1.1. □

2.4. A positivity Conjecture for Grothendieck polynomials. Let $\beta$ be a formal variable and let ${ \mathfrak { G } } _ { w } ( \mathbf { x } ; \mathbf { y } )$ be the double Grothendieck polynomial for $w \in S _ { n }$ . We use the convention consistent with that of [16]. Consider the expansion

$$
\mathfrak {G} _ {u} (\mathbf {x}; \mathbf {y}) \cdot \mathfrak {G} _ {v} (\mathbf {x}; \mathbf {t}) = \sum_ {w \in S _ {\infty}} \tilde {c} _ {u, v} ^ {w} (\mathbf {y}, \mathbf {t}) \cdot \mathfrak {G} _ {w} (\mathbf {x}; \mathbf {t}).
$$

We propose the following conjecture, inspired by Theorem 1.1.

Conjecture 2.7. For $u , v , w \in S _ { \infty }$ , $\widetilde { c } _ { u , v } ^ { w } ( \mathbf { y } , \mathbf { t } ) \in \mathbb { N } [ \beta ] [ t _ { i } \ominus y _ { j } ] _ { i , j \ge 1 }$ , where $\textstyle a \ominus b : = { \frac { a - b } { 1 + \beta b } }$ .

# Acknowledgements

We thank Hai Zhu for enlightening conversations. Y.G. is partially supported by NSFC Grant No. 12471309.

# References

[1] David Anderson and William Fulton. Equivariant cohomology in algebraic geometry, volume 210 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2024.   
[2] Christoph B¨arligea. Skew divided difference operators in the Nichols algebra associated to a finite Coxeter group. J. Algebra, 517:19–77, 2019.   
[3] Arkady Berenstein and Edward Richmond. Littlewood-Richardson coefficients for reflection groups. Adv. Math., 284:54–111, 2015.   
[4] Nantel Bergeron and Sara Billey. RC-graphs and Schubert polynomials. Experiment. Math., 2(4):257– 269, 1993.   
[5] Sara C. Billey. Kostant polynomials and the cohomology ring for $G / B$ . Duke Math. J., 96(1):205–224, 1999.   
[6] Neil J. Y. Fan, Peter L. Guo, and Rui Xiong. Bumpless pipe dreams meet puzzles. Adv. Math., 463:Paper No. 110113, 29, 2025.   
[7] Sergey Fomin and Anatol N. Kirillov. Quadratic algebras, Dunkl elements, and Schubert calculus. In Advances in geometry, volume 172 of Progr. Math., pages 147–182. Birkh¨auser Boston, Boston, MA, 1999.   
[8] William Graham. Positivity in equivariant Schubert calculus. Duke Math. J., 109(3):599–614, 2001.   
[9] Daoji Huang. Schubert products for permutations with separated descents. Int. Math. Res. Not. IMRN, (20):17461–17493, 2023.

[10] James E. Humphreys. Linear algebraic groups, volume No. 21 of Graduate Texts in Mathematics. Springer-Verlag, New York-Heidelberg, 1975.   
[11] Anatol N. Kirillov. Skew divided difference operators and Schubert polynomials. SIGMA Symmetry Integrability Geom. Methods Appl., 3:Paper 072, 14, 2007.   
[12] Allen Knutson and Ezra Miller. Gr¨obner geometry of Schubert polynomials. Ann. of Math. (2), 161(3):1245–1318, 2005.   
[13] Allen Knutson and Terence Tao. Puzzles and (equivariant) cohomology of Grassmannians. Duke Math. J., 119(2):221–260, 2003.   
[14] Allen Knutson and Paul Zinn-Justin. Schubert puzzles and integrability iii: separated descents. arXiv preprint arXiv:2306.13855, 2023.   
[15] Thomas Lam, Seung Jin Lee, and Mark Shimozono. Back stable Schubert calculus. Compos. Math., 157(5):883–962, 2021.   
[16] Thomas Lam, Seung Jin Lee, and Mark Shimozono. Back stable $K$ -theory Schubert calculus. Int. Math. Res. Not. IMRN, (24):21381–21466, 2023.   
[17] Ricky Ini Liu. Positive expressions for skew divided difference operators. J. Algebraic Combin., 42(3):861–874, 2015.   
[18] I. G. Macdonald. Schubert polynomials. In Surveys in combinatorics, 1991 (Guildford, 1991), volume 166 of London Math. Soc. Lecture Note Ser., pages 73–99. Cambridge Univ. Press, Cambridge, 1991.   
[19] Leonardo C. Mihalcea, Hiroshi Naruse, and Changjian Su. Left Demazure-Lusztig operators on equivariant (quantum) cohomology and K-theory. Int. Math. Res. Not. IMRN, (16):12096–12147, 2022.   
[20] Alexander I. Molev and Bruce E. Sagan. A Littlewood-Richardson rule for factorial Schur functions. Trans. Amer. Math. Soc., 351(11):4429–4443, 1999.   
[21] Matthew J. Samuel. A Molev-Sagan type formula for double Schubert polynomials. J. Pure Appl. Algebra, 228(7):Paper No. 107636, 39, 2024.   
[22] Julianna Tymoczko. Billey’s formula in combinatorics, geometry, and topology. In Schubert calculus— Osaka 2012, volume 71 of Adv. Stud. Pure Math., pages 499–518. Math. Soc. Japan, [Tokyo], 2016.

Beijing International Center for Mathematical Research, Peking University, Beijing 100871, China

Email address: gaoyibo@bicmr.pku.edu.cn

Department of Mathematics and Statistics, University of Ottawa, 150 Louis-Pasteur, Ottawa, ON, K1N 6N5, Canada

Email address: rxion043@uOttawa.ca