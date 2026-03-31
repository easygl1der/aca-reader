# A MOLEV-SAGAN TYPE FORMULA FOR DOUBLE SCHUBERT POLYNOMIALS

MATTHEW J. SAMUEL

Abstract. We give a Molev-Sagan type formula for computing the product $\mathfrak { S } _ { u } ( x ; y ) \mathfrak { S } _ { v } ( x ; z )$ of two double Schubert polynomials in different sets of coefficient variables where the descents of $^ { u }$ and $_ { v }$ satisfy certain conditions that encompass Molev and Sagan’s original case and conjecture positivity in the general case. Additionally, we provide a Pieri formula for multiplying an arbitrary double Schubert polynomial ${ \mathfrak { S } } _ { u } ( x ; y )$ by a factorial elementary symmetric polynomial $E _ { p , k } ( x ; z )$ . Both formulas remain positive in terms of the negative roots when we set $y = z$ , so in particular this gives a new equivariant Littlewood-Richardson rule for the Grassmannian, and more generally a positive formula for multiplying a factorial Schur polynomial $s _ { \lambda } ( x _ { 1 } , \dots , x _ { m } ; y )$ by a double Schubert polynomial $\mathfrak { S } _ { v } ( x _ { 1 } , \dots , x _ { p } ; y )$ such that $m \geq p$ . An additional new result we present is a combinatorial proof of a conjecture of Kirillov of nonnegativity of the coefficients of skew Schubert polynomials, and we conjecture a weight-preserving bijection between a modification of certain diagrams used in our formulas and RC-graphs/pipe dreams arising in formulas for double Schubert polynomials.

# 1. Introduction

Schubert polynomials were originally defined by Lascoux and Sch¨utzenberger in [19], and double Schubert polynomials are a generalization found in [21]. The double Schubert polynomials are polynomials in two infinite sets of variables $\{ x _ { i } : i \in \mathbb { N } \}$ and $\{ y _ { i } : i \in \mathbb { N } \}$ with integer coefficients and are denoted by $\mathfrak { S } _ { u } ( x ; y )$ for permutations $u$ . Double Schubert polynomials are linearly independent and in fact form a basis of the polynomial ring over the coefficient ring $\mathbb { Z } [ y ]$ . Double Schubert polynomials are interesting first and foremost because they represent Schubert classes in the torus-equivariant cohomology ring of the complete flag variety. If we introduce a third infinite set of variables $\{ z _ { i } : i \in \mathbb { N } \}$ , we may write the product of two double Schubert polynomials with different sets of coefficient variables, defining coefficients $c _ { u v } ^ { w } ( y ; z )$ as follows:

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; z) = \sum_ {w \in S _ {\infty}} c _ {u v} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

We have the following conjecture:

Conjecture 1.1. For all $u , v , w$ we have that $c _ { u v } ^ { w } ( y ; z )$ is a polynomial in the differences $y _ { i } - z _ { j }$ with nonnegative integer coefficients.

At the time of this writing, we have computationally verified this conjecture for all $u , v \in S _ { 5 }$ for all $w \in S _ { \infty }$ . The truth of this conjecture was demonstrated for factorial Schur functions in [23] via a Littlewood-Richardson rule. $c _ { u v } ^ { w } ( 0 ; 0 )$ is known to be nonnegative as these are the structure constants in the ordinary cohomology of the complete flag variety, which count points in triple intersections of Schubert varieties. No combinatorial proof is known of this in general, but several widely applicable combinatorial results are known; the full proof is obtained using algebraic geometry. It is also known [9] via another algebraic geometry proof that $c _ { u v } ^ { w } ( y ; y )$ is a polynomial in the differences $y _ { i + 1 } - y _ { i }$ with nonnegative integer coefficients, which was shown combinatorially for the Grassmannian in [14] and for the two-step flag variety in [5]. It was conjectured by Kirillov [12] (essentially) that $c _ { u v } ^ { w } ( y ; 0 )$ is a polynomial in $y$ with nonnegative integer coefficients for all $u , v , w$ and proved in the same article that the conjecture holds when $\ell ( u , w ) = 1$ . This is clearly a special case of Conjecture 1.1. We have verified Kirillov’s conjecture, which is easier to test, for $u , v \in S _ { 7 }$ for all $w \in S _ { \infty }$ . Kirillov’s conjecture was presented in an alternative form by the author on MathOverflow [10], and in a comment Dave Anderson suggested that we likely have the tools to prove this with the current state of

knowledge, though as far as we know this has not yet been done. We present a combinatorial proof of an additional special case (conjectured separately in Kirillov’s article) in Theorem 5.2.

This article has two main results. The first, Theorem 3.1, is a positive combinatorial formula for $c _ { u v } ^ { w } ( y ; z )$ where there exists a positive integer $p$ such that $\ell ( u s _ { i } ) > \ell ( u )$ whenever $i < p$ and $\ell ( v s _ { i } ) > \ell ( v )$ whenever $i > p$ . Equivalently, it is a positive formula as a polynomial in the differences $y _ { i } - z _ { j }$ for coefficients of ${ \mathfrak { S } } _ { w } ( x ; y )$ in the expansion of the product

$$
\mathfrak {S} _ {u} (x _ {1}, \ldots , x _ {m}; y) \mathfrak {S} _ {v} (x _ {1}, \ldots , x _ {p}; z)
$$

where $\mathfrak { S } _ { u } ( x _ { 1 } , \dots , x _ { m } ; y )$ is symmetric in the variables $x _ { 1 } , \ldots , x _ { p }$ . The formula when substituting to obtain $c _ { u v } ^ { w } ( y ; y )$ is also nonnegative (though some terms are $0$ ) in the sense of [9], which we show in Theorem 6.1, thus also giving a positive formula for ordinary double Schubert polynomial multiplication for these pairs of permutations; all of the nonzero terms in the formula for $c _ { u v } ^ { w } ( y ; y )$ are visibly polynomials in $y _ { i + 1 } - y _ { i }$ with nonnegative integer coefficients.

The second main result, Theorem 7.1, is a Pieri formula for computing $c _ { u v } ^ { w } ( y ; z )$ when $v$ is a cycle of the form $c _ { p , k } = s _ { k - p + 1 } s _ { k - p + 2 } \cdot \cdot \cdot s _ { k }$ , in which case ${ \mathfrak { S } } _ { c _ { p , k } } ( x ; z )$ is a factorial elementary symmetric polynomial, for which we introduce the alternative notation $E _ { p , k } ( x ; z )$ . This generalizes the main result of [27] and is closely related to the equivariant Pieri formula in [25]. Via the formula in [23, (4)] applied to a column shape, which we state here as an explicit formula for $E _ { p , k } ( x ; z )$ (Proposition 7.10), our Pieri formula is positive in the sense of Conjecture 1.1 and also positive for $c _ { u v } ^ { w } ( y ; y )$ in the sense of [9].

In Section 8 we state a more general result than Theorem 3.1 (Theorem 8.1) that differs only in the choices of the permutations $u$ and $v$ ; the formula is the same as that of the main result. Theorem 8.1 is the most general case to which our method applies.

# 2. Preliminaries

Definition 2.1 (The symmetric group). There are many references regarding the algebraic combinatorics of symmetric groups as Coxeter groups, for which we will cite [4]. We use the notation $S _ { \infty }$ for the infinite symmetric group of bijections $\Nu \to \mathbb N$ fixing all but finitely many elements, with function composition in the usual order being the operation, and $S _ { n } < S _ { \infty }$ is the subgroup of all $u \in S _ { \infty }$ such that $u ( i ) = i$ if $i > n$ . We think of elements of $S _ { \infty }$ as sequences and refer to them as permutations. Every element $u \in S _ { \infty }$ is in $S _ { n }$ for some $n$ , and if $u \in S _ { n }$ we may write

$$
u = [ u (1), u (2), \dots , u (n) ]
$$

(this is known as “window notation”). Clearly if $u \in S _ { n }$ then $u \in S _ { N }$ for all $N > n$ as well.

$s _ { i } \in S _ { \infty }$ is the adjacent transposition (also known as a simple reflection) exchanging the values $_ i$ and $i + 1$ , and $t _ { a b }$ for positive integers $a \neq b$ is the (not necessarily adjacent) transposition exchanging $a$ and $b$ and fixing everything else. Note that we do not impose an order on $a$ and $b$ in the definition of a transposition, so $t _ { a b } = t _ { b a }$ . Every element of $S _ { \infty }$ can be written as a product of adjacent transpositions. For $u \in S _ { \infty }$ , $u s _ { i }$ is $u$ with the indices $i$ and $i + 1$ flipped, and $s _ { i } u$ exchanges the values instead. The length $\ell ( u )$ is the number of inversions of $u$ , the pairs of indices $( i , j )$ with $i < j$ such that $u ( i ) > u ( j )$ . For elements $u , w$ with $\ell ( u ) \leq \ell ( w )$ we define $\ell ( u , w ) = \ell ( w ) - \ell ( u )$ . A word for an element $u \in S _ { \infty }$ is a sequence of simple reflections

$$
\left(s _ {i _ {1}}, \dots , s _ {i _ {m}}\right)
$$

such that

$$
s _ {i _ {1}} \dots s _ {i _ {m}} = u
$$

and the word is said to be reduced if it is as short as possible. It is well known that a reduced word for $u$ is of length exactly $\ell ( u )$ . If $u ( i ) > u ( i + 1 )$ , then $\ell ( u s _ { i } ) = \ell ( u ) - 1$ , and if $u ( i ) < u ( i + 1 )$ then $\ell ( u s _ { i } ) = \ell ( u ) + 1$ . Indices $i$ with $u ( i ) > u ( i + 1 )$ are called (right) descents of $u$ .

The (right) weak Bruhat order $\leq$ on permutations is the partial ordering that is the reflexive, transitive closure of the relation $v \leq v s _ { i }$ whenever $\ell ( v s _ { i } ) = \ell ( v ) + 1$ . In general, if $v \leq w$ , then $\ell ( v ^ { - 1 } w ) = \ell ( w ) - \ell ( v )$ .

We denote by $w _ { 0 } ( n )$ the longest element (element with the most inversions) of $S _ { n + 1 }$ . This is easily seen to be

$$
w _ {0} (n) (i) = \left\{ \begin{array}{l l} n + 2 - i & \text {i f} i \leq n + 1 \\ i & \text {i f} i > n + 1 \end{array} \right.
$$

Definition 2.2 (Double Schubert polynomials, $\partial ^ { w }$ , $\partial _ { u } ^ { w }$ ). A simple definition of double Schubert polynomials is through divided difference operators as defined in [3]. $S _ { \infty }$ acts on the polynomial ring by extending via automorphisms the rule

$$
u (x _ {j}) = x _ {u (j)}
$$

We also insist that $u ( y _ { j } ) = y _ { j }$ and $u ( z _ { j } ) = z _ { j }$ for all $j$ . We define the divided difference operator $\partial ^ { s _ { i } }$ by

$$
\partial^ {s _ {i}} (P) = \frac {P - s _ {i} (P)}{x _ {i} - x _ {i + 1}}
$$

It is well known that applying divided difference operators to a polynomial yields a polynomial; this is proved, for example, in [26].

The divided difference operators can be composed to yield operators indexed by the symmetric group, $\partial ^ { u }$ for $u \in S _ { \infty }$ , defined by

$$
\partial^ {u} = \partial^ {s _ {i _ {1}}} \dots \partial^ {s _ {i _ {\ell (u)}}}
$$

where $( s _ { i _ { 1 } } , \ldots , s _ { i _ { \ell ( u ) } } )$ is a reduced word for $u$ . This does not depend on the choice of reduced word. If $\ell ( u s _ { i } ) > \ell ( u )$ , then

$$
\partial^ {u} \partial^ {s _ {i}} = \partial^ {u s _ {i}}
$$

If $\ell ( u s _ { i } ) < \ell ( u )$ , then

$$
\partial^ {u} \partial^ {s _ {i}} = 0
$$

Divided difference operators satisfy the Leibniz formula

$$
\partial^ {s _ {i}} (P Q) = \partial^ {s _ {i}} (P) s _ {i} (Q) + P \partial^ {s _ {i}} (Q) \tag {2.1}
$$

which can be seen by direct computation. There exist skew divided difference operators $\partial _ { u } ^ { w }$ (the same as those defined in [26], differing by a permutation from those in [21] and [12]) defined by the more general Leibniz formula

$$
\partial^ {w} (P Q) = \sum_ {u} \partial^ {u} (P) \partial_ {u} ^ {w} (Q)
$$

We identify divided difference operators, group elements, and skew divided difference operators with the corresponding elements of the nil-Hecke ring [18], which is a free left module over $\mathbb { Z } [ x ]$ with basis $\{ \partial ^ { u } \mid u \in$ $S _ { \infty } \}$ . For example,

$$
s _ {i} = 1 + (x _ {i + 1} - x _ {i}) \partial^ {s _ {i}}
$$

It is shown in [26] that

$$
\partial_ {u} ^ {w} = \sum_ {v} c _ {u v} ^ {w} (x; x) \partial^ {v}
$$

More usefully for this article, skew divided difference operators satisfy the following recurrence relation. For the base case,

$$
\partial_ {1} ^ {1} = 1
$$

and if $u \in S _ { \infty }$ satisfies $u \neq 1$ then

$$
\partial_ {u} ^ {1} = 0
$$

Suppose $\ell ( w s _ { i } ) < \ell ( w )$ . If $\ell ( u s _ { i } ) < \ell ( u )$ , then

$$
\partial_ {u} ^ {w} = \partial_ {u} ^ {w s _ {i}} \partial^ {s _ {i}} + \partial_ {u s _ {i}} ^ {w s _ {i}} s _ {i}
$$

and if $\ell ( u s _ { i } ) > \ell ( u )$ then

$$
\partial_ {u} ^ {w} = \partial_ {u} ^ {w s _ {i}} \partial^ {s _ {i}}
$$

We define, for any $n > 0$ ,

$$
\mathfrak {S} _ {w _ {0} (n)} (x; y) = \prod_ {i + j \leq n + 1} \left(x _ {i} - y _ {j}\right)
$$

Then the double Schubert polynomial $\mathfrak { S } _ { u } ( x ; y )$ for $u \in S _ { n + 1 }$ is given by

$$
\mathfrak {S} _ {u} (x; y) = \partial^ {u ^ {- 1} w _ {0} (n)} \left(\mathfrak {S} _ {w _ {0} (n)} (x; y)\right)
$$

This definition is shown to yield a well-defined polynomial (i.e., not depending on the choice of $n$ ) by Macdonald in [21].

Note that if $\ell ( u s _ { i } ) > \ell ( u )$ , then $\mathfrak { S } _ { u } ( x ; y )$ is symmetric in the variables $x _ { i }$ and $x _ { i + 1 }$ and

$$
\partial^ {s _ {i}} \left(\mathfrak {S} _ {u} (x; y)\right) = 0
$$

If $\ell ( u s _ { i } ) < \ell ( u )$ , then

$$
\partial^ {s _ {i}} \left(\mathfrak {S} _ {u} (x; y)\right) = \mathfrak {S} _ {u s _ {i}} (x; y)
$$

We also have the vanishing formula [21, (6.4)]

$$
\mathfrak {S} _ {u} (y; y) = \delta_ {1, u}
$$

The collection of $\mathfrak { S } _ { u } ( x ; y )$ for $u \in S _ { \infty }$ forms a basis for $\mathbb { Z } [ x , y , z ]$ as a module over $\mathbb { Z } [ y , z ]$ , and by the vanishing formula, applying the divided difference $\partial ^ { w }$ then setting allows us to pull out the coefficient $x = y$ of ${ \mathfrak { S } } _ { w } ( x ; y )$ in the expansion of any polynomial in $\mathbb { Z } [ x , y , z ]$ .

The skew divided difference operators allow us to obtain coefficients of products of arbitrary polynomials with double Schubert polynomials in $x$ and $y$ as follows. Using the Leibniz formula, for an arbitrary polynomial $P$ and a permutation $u$ we obtain

$$
\partial^ {w} (P \mathfrak {S} _ {u} (x; y)) = \sum_ {v} \partial_ {v} ^ {w} (P) \partial^ {v} (\mathfrak {S} _ {u} (x; y))
$$

Again applying the vanishing formula, we obtain the result that substituting $x = y$ in the polynomial $\partial _ { u } ^ { w } ( P )$ extracts the coefficient of ${ \mathfrak { S } } _ { w } ( x ; y )$ in the expansion of $P { \mathfrak { S } } _ { u } ( x ; y )$ . In particular, setting $P = \mathfrak { S } _ { v } ( x ; z )$ , we obtain

$$
c _ {u v} ^ {w} (x; z) = \partial_ {u} ^ {w} (\mathfrak {S} _ {v} (x; z))
$$

for all $u , v , w \in S _ { \infty }$

Definition 2.3 (Factorial Schur polynomials, Grassmannian permutations). A permutation $u \in S _ { \infty }$ is said to be Grassmannian if it has at most one descent. A factorial Schur polynomial is a double Schubert polynomial corresponding to a Grassmannian permutation [6, Theorem 4]. Factorial Schur polynomials are indexed by partitions and denoted by $s _ { \lambda } ( x _ { 1 } , \dots , x _ { m } ; y )$ . The partition $\lambda$ together with the value of $m$ determine the permutation for the double Schubert polynomial to which $s _ { \lambda } ( x _ { 1 } , \dots , x _ { m } ; y )$ corresponds. Specifically, we define a Grassmannian permutation $w _ { \lambda ; m }$ corresponding to the partition $\lambda$ with descent at position $m$ as follows. Let

$$
\lambda = \left(\lambda_ {1}, \dots , \lambda_ {p}\right)
$$

and suppose $m \geq p$ . Define $\lambda _ { i } = 0$ if $i > p$ , then let $w _ { \lambda ; m } ( i ) = i + \lambda _ { m + 1 - i }$ if $1 \leq i \leq m$ . The remainder of $w _ { \lambda ; m }$ is the complement of $w _ { \lambda ; m } ( [ m ] )$ arranged in increasing order. For example,

$$
w _ {(3, 1, 1); 4} = [ 1, 3, 4, 7, 2, 5, 6 ]
$$

Given this definition of $w _ { \lambda ; m }$ , we have the formula

$$
s _ {\lambda} \left(x _ {1}, \dots , x _ {m}; y\right) = \mathfrak {S} _ {w _ {\lambda ; m}} (x; y)
$$

The factorial elementary symmetric polynomial $E _ { p , k } ( x ; y )$ is the special case $s _ { ( 1 ^ { p } ) } ( x _ { 1 } , \ldots , x _ { k } ; y )$ , about which we go into much more detail below.

Molev and Sagan’s Littlewood-Richardson rule [23] computes the product of two factorial Schur polynomials $s _ { \lambda } ( x _ { 1 } , \dots , x _ { m } ; y ) s _ { \mu } ( x _ { 1 } , \dots , x _ { m } ; z )$ where the corresponding permutations have the same descent, i.e. the polynomials have the same number of $x$ variables.

Definition 2.4 (The code ${ \mathfrak { c } } ( v )$ , dominant permutations, the dominant approximation $\mu _ { v }$ , and the partition $\lambda ( v )$ ). We define the code ${ \mathfrak { c } } ( v )$ of a permutation $v \in S _ { \infty }$ , a sequence indexed by $i \geq 1$ , as follows:

$$
\mathfrak {c} _ {i} (v) = \# \{j > i \mid v (i) > v (j) \}
$$

Note that if $v \in S _ { n + 1 }$ , then $\mathfrak { c } _ { i } ( v ) \leq n + 1 - i$ , and it is not hard to see that

$$
\ell (v) = \sum_ {i = 1} ^ {\infty} \mathfrak {c} _ {i} (v)
$$

Also, $\ell ( v s _ { i } ) = \ell ( v ) + 1$ if and only if $\mathfrak { c } _ { i } ( v ) \leq \mathfrak { c } _ { i + 1 } ( v )$ , in which case $\mathfrak { c } _ { i } ( v s _ { i } ) = \mathfrak { c } _ { i + 1 } ( v ) + 1$ , $\mathfrak { c } _ { i + 1 } ( v s _ { i } ) = \mathfrak { c } _ { i } ( v )$ , and $\mathfrak { c } _ { j } ( v s _ { i } ) = \mathfrak { c } _ { j } ( v )$ for $j \not \in \{ i , i + 1 \}$ .

A permutation $v$ is said to be dominant if ${ \mathfrak { c } } ( v )$ is a partition. For $v \in S _ { \infty }$ , we define a dominant permutation $\mu _ { v }$ , the dominant approximation of $\boldsymbol { v }$ , as follows. If $v$ is dominant, let $\mu _ { v } ~ = ~ v$ . If $v$ is not

dominant, let $i$ be the maximal index such that $\mathfrak { c } _ { i } ( v ) < \mathfrak { c } _ { i + 1 } ( v )$ , and define $\mu _ { v } = \mu _ { v s _ { i } }$ . It is clear that this recursion terminates in a unique dominant permutation. Note that at each step $\ell ( v s _ { i } ) = \ell ( v ) + 1$ , so that $v \leq \mu _ { v }$ and hence $\ell ( v ^ { - 1 } \mu _ { v } ) = \ell ( \mu _ { v } ) - \ell ( v )$ . Define a partition $\lambda ( v )$ to be the conjugate of the code of $\mu _ { v }$ meaning

$$
\lambda_ {i} (v) = \# \left\{j \mid \mathfrak {c} _ {j} (\mu_ {v}) \geq i \right\}
$$

Example 2.1. Let $v = [ 1 , 3 , 5 , 2 , 4 ]$ . Then

$$
\mathfrak {c} (v) = (0, 1, 2)
$$

In the recursion computing the dominant approximation, the first reflection to apply is at index 2. We have that

$$
v s _ {2} = [ 1, 5, 3, 2, 4 ]
$$

and

$$
\mathfrak {c} (v s _ {2}) = (0, 3, 1)
$$

Continuing in this manner, we obtain that the remaining reflections are $s _ { 1 } , s _ { 2 }$ , and hence $\mu _ { v } = v s _ { 2 } s _ { 1 } s _ { 2 }$ . We have

$$
\mu_ {v} = [ 5, 3, 1, 2, 4 ]
$$

$$
\mathfrak {c} (\mu_ {v}) = (4, 2)
$$

which is a partition. $\lambda ( v )$ is the conjugate partition, namely

$$
\lambda (v) = (2, 2, 1, 1)
$$

Definition 2.5 ( $\xrightarrow { k }$ , $P _ { k } ( u , w )$ , $\operatorname { P a t h } _ { \lambda } ( u , w )$ , $\mathrm { w e i g h t } _ { P , \lambda } ( y ; z ) )$ . We define a relation $\xrightarrow { k }$ on pairs of permutations, introduced by Sottile [27], which was used originally to indicate when the coefficient of a Schubert polynomial is nonzero in a suitable application of the Pieri formula. In the generalization to double Schubert polynomials in [25], the same relation applies to all nonzero coefficients in the expansion of the generalized Pieri formula. The relation plays the same role in our case.

Given $u , u ^ { \prime } \in S _ { \infty }$ and a positive integer $k$ , we declare that $u \stackrel { k } {  } u ^ { \prime }$ if there exists a $p$ with $0 \leq p \leq k$ such that there are transpositions ${ t _ { a _ { 1 } b _ { 1 } } , \ldots , t _ { a _ { p } b _ { p } } }$ satisfying

(1) $a _ { i } \leq k < b _ { i }$ for all $i$   
(2) $a _ { i } \neq a _ { j }$ whenever $i \neq j$   
(3) $\ell ( u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { i } b _ { i } } ) = \ell ( u ) + i { \mathrm { ~ f o r ~ a l l ~ } } $ i   
(4) $u ^ { \prime } = u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot \cdot t _ { a _ { p } b _ { p } }$

If $u \stackrel { k } {  } w$ , define

$$
P _ {k} (u, w) = \{u (i) \mid i \leq k \text {a n d} u (i) = w (i) \}
$$

For an integer $j$ we define the weight of this interval by

$$
\operatorname {w e i g h t} _ {u, k} ^ {w} (y; z _ {j}) = \prod_ {i \in P _ {k} (u, w)} \left(y _ {i} - z _ {j}\right)
$$

where by convention the empty product is 1.

Given $u , w \in S _ { \infty }$ and a partition $\lambda$ of length $m$ , define $\operatorname { P a t h } _ { \lambda } ( u , w )$ to be the set of sequences defined by

$$
\operatorname {P a t h} _ {\lambda} (u, w) = \left\{\left(u _ {0}, u _ {1}, \dots , u _ {m}\right) \mid u = u _ {0} \xrightarrow {\lambda_ {1}} u _ {1} \xrightarrow {\lambda_ {2}} \dots \xrightarrow {\lambda_ {m}} u _ {m} = w \right\}
$$

Then given such a path $P$ and the partition $\lambda$ we define

$$
\operatorname {w e i g h t} _ {P, \lambda} (y; z) = \prod_ {i = 1} ^ {m} \operatorname {w e i g h t} _ {u _ {i - 1}, \lambda_ {i}} ^ {u _ {i}} (y; z _ {i})
$$

For illustration in examples, we will represent the elements of $\operatorname { P a t h } _ { \lambda } ( u , w )$ with certain diagrams of numbers. In the diagrams, the permutations $\left( u _ { 0 } , \ldots , u _ { m } \right)$ in the paths will be written vertically in each column, with the columns progressing according to the permutations in the path from left to right. More specifically, the element $u _ { j } ( i )$ at the $i$ th index in the permutation $u _ { j }$ will be in row $_ i$ and column $j$ , with the column numbers starting at 0 and row numbers starting at 1. In column $j$ , a horizontal line will be drawn below row $\lambda _ { j }$ . The entries that contribute factors to the weight are those where $u _ { j - 1 } ( i ) = u _ { j } ( i )$ for rows $i$ above the horizontal line in column $j$ , meaning the number is the same as the number in the same row

in the column immediately to the left. These entries will be circled in the diagram. The circled entries in column $j$ represent elements of $P _ { \lambda _ { j } } ( u _ { j - 1 } , u _ { j } )$ . If the circled number is $_ i$ (the value, not the row number) in column $j$ , a term of $y _ { i } - z _ { j }$ will occur as a factor in the product computing the weight of the path. The weight weight $_ { P , \lambda } \mathopen { } \mathclose \bgroup \left( y ; z \aftergroup \egroup \right)$ will be written beneath the diagram.

Example 2.2. Let $\lambda = ( 3 , 2 , 2 )$ . Then

$$
P = ([ 1, 3, 4, 2 ], [ 1, 3, 5, 2, 4 ], [ 3, 5, 1, 2, 4 ], [ 4, 5, 1, 2, 3 ])
$$

is in $\operatorname { P a t h } _ { \lambda } ( [ 1 , 3 , 4 , 2 ] , [ 4 , 5 , 1 , 2 , 3 ] )$ . This corresponds to the following diagram.

$$
\begin{array}{c c c c} 1 & \text {\framebox {1}} & 3 & 4 \\ 3 & \text {\framebox {3}} & 5 & \text {\framebox {5}} \\ 4 & \text {\framebox {5}} & \text {\framebox {1}} & \text {\framebox {1}} \\ 2 & \text {\framebox {2}} & 2 & 2 \\ 5 & \text {\framebox {4}} & 4 & 3 \end{array}
$$

$$
(y _ {1} - z _ {1}) (y _ {3} - z _ {1}) (y _ {5} - z _ {3})
$$

weight $P , \lambda \left( y ; z \right)$ is written beneath the diagram. $( y _ { 1 } - z _ { 1 } ) ( y _ { 3 } - z _ { 1 } )$ corresponds to the circled 1 and 3 in column 1 and $y _ { 5 } - z _ { 3 }$ corresponds to the circled 5 in column 3.

# 3. The first formula

Definition 3.1 $( d _ { u , \lambda } ^ { w } ( y ; z )$ , ewuv(y; z)). Given permutations $u , w \in S _ { \infty }$ and a partition $\lambda$ we define a polynomial $d _ { u , \lambda } ^ { w } ( y ; z )$ with nonnegative integer coefficients in terms of products of linear terms of the form $y _ { i } - z _ { j }$ as follows:

$$
d _ {u, \lambda} ^ {w} (y; z) = \sum_ {P \in \operatorname {P a t h} _ {\lambda} (u, w)} \operatorname {w e i g h t} _ {P, \lambda} (y; z)
$$

We define coefficients $e _ { u v } ^ { w } ( y ; z )$ as follows. If $u , v , w \in S _ { \infty }$ , define

$$
e _ {u v} ^ {w} (y; z) = 0
$$

unless $\ell ( w v ^ { - 1 } \mu _ { v } ) = \ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ , in which case define

$$
e _ {u v} ^ {w} (y; z) = d _ {u, \lambda (v)} ^ {w v ^ {- 1} \mu_ {v}} (y; z)
$$

Theorem 3.1. Let $u , v \in S _ { \infty }$ be such that there exists a $p > 0$ for which $\ell ( u s _ { i } ) > \ell ( u )$ for all $i < p$ and $\ell ( v s _ { i } ) > \ell ( v )$ for all $i > p$ . Then

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; z) = \sum_ {w \in S _ {\infty}} e _ {u v} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

The condition on $u$ and $v$ in the statement of Theorem 3.1 is referred to as $u$ and $v$ having “separated descents” in [15], for which a puzzle rule is found for the coefficients $c _ { u v } ^ { w } ( 0 ; 0 )$ , a case that is also covered in [11]. In a more recent paper, [16] extends this to equivariant K-theory. The main result of [8] is a similar formula for double Grothendieck polynomials, which also gives a positive formula for the $z = 0$ case in the coefficients we consider.

We illustrate this with some examples.

Example 3.1. We compute the example using factorial Schur functions in [14, 6.4]. Let $u = v = [ 1 , 3 , 2 ]$ , and we first let $w = \left\lfloor 1 , 3 , 2 \right\rfloor$ . Then

$$
\mu_ {v} = [ 3, 1, 2 ]
$$

$$
\mathfrak {c} \left(\mu_ {v}\right) = (2)
$$

$$
\lambda (v) = (1, 1)
$$

$$
v ^ {- 1} \mu_ {v} = [ 2, 1 ]
$$

$$
w v ^ {- 1} \mu_ {v} = [ 3, 1, 2 ]
$$

Then $c _ { u v } ^ { w } ( y ; z ) = ( y _ { 3 } - z _ { 2 } ) + ( y _ { 1 } - z _ { 1 } )$ , as witnessed by the following paths.

![](images/fb3a614855ad3d1138c1132c1077b06ec811c9496a34b284dabf55126f036a35.jpg)

The reference computes the result as $\left( y _ { 3 } - z _ { 1 } \right) + \left( y _ { 1 } - z _ { 2 } \right)$ instead, which of course yields the same result but differs from our formula in the terms produced by the combinatorial elements. As we show in Theorem 6.1, our formula has the advantage that it yields a positive formula in equivariant cohomology when $y$ is substituted for $z$ ; this is not the case for $\left( y _ { 3 } - y _ { 1 } \right) + \left( y _ { 1 } - y _ { 2 } \right)$ , as $y _ { 1 } - y _ { 2 }$ is not a positive term in the sense of [9]. Our formula gives $\left( y _ { 3 } - y _ { 2 } \right) + \left( y _ { 1 } - y _ { 1 } \right)$ , and both terms are nonnegative. We note that Molev in [22] provides a positive formula stemming from Molev and Sagan’s rule.

For the remaining paths we write $w$ at the top of the diagram to save space.

![](images/9a2b53fe0239d93936f6180c6ee312e4d949c4713b4adae7f670ad9cf830580b.jpg)

Thus

$$
\mathfrak {S} _ {[ 1, 3, 2 ]} (x; y) \mathfrak {S} _ {[ 1, 3, 2 ]} (x; z) = ((y _ {3} - z _ {2}) + (y _ {1} - z _ {1})) \mathfrak {S} _ {[ 1, 3, 2 ]} (x; y) + \mathfrak {S} _ {[ 1, 4, 2, 3 ]} (x; y) + \mathfrak {S} _ {[ 2, 3, 1 ]} (x; y)
$$

which agrees with [14].

Example 3.2. We compute the product of two factorial Schur polynomials with different numbers of $x$ variables, namely $s _ { ( 2 , 1 ) } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ; y ) s _ { ( 2 ) } ( x _ { 1 } , x _ { 2 } ; z )$ . This is the product $\mathfrak { S } _ { [ 1 , 3 , 5 , 2 , 4 ] } ( x ; y ) \mathfrak { S } _ { [ 1 , 4 , 2 , 3 ] } ( x ; z )$ . Notice that in this level of generality our formula cannot compute the product in the opposite order.

$$
\mu_ {v} = [ 4, 1, 2, 3 ]
$$

$$
\mathfrak {c} \left(\mu_ {v}\right) = (3)
$$

$$
\lambda (v) = (1, 1, 1)
$$

$$
v ^ {- 1} \mu_ {v} = [ 2, 1 ]
$$

![](images/4308e180880ca305a74f115356b7eec021f415b3b7c0f6bd2fddd17259e7e960.jpg)

$$
(y _ {3} - z _ {2}) (y _ {3} - z _ {3})
$$

![](images/26941de0c8a1e5c5e9900e21dab8e811b698a41bcdfea2a0e22af15cbf0cc902.jpg)

$$
\left(y _ {1} - z _ {1}\right) \left(y _ {3} - z _ {3}\right)
$$

![](images/b393552e8839a35fa2824a1fe73e130f6650d35a65bf956cb26bb93a382f4d24.jpg)

$$
(y _ {1} - z _ {1}) (y _ {1} - z _ {2})
$$

$$
\left(\left(y _ {3} - z _ {2}\right) \left(y _ {3} - z _ {3}\right) + \left(y _ {1} - z _ {1}\right) \left(y _ {3} - z _ {3}\right) + \left(y _ {1} - z _ {1}\right) \left(y _ {1} - z _ {2}\right)\right) \mathfrak {S} _ {[ 1, 3, 5, 2, 4 ]} (x; y)
$$

![](images/3c3636b0556faa179a1c3a7bddfb7ee5a2476acc8db7be955468769ab3f390db.jpg)

$$
y _ {3} - z _ {2}
$$

![](images/dbb7a330ac53aa884463f4f5d2b4d8300b7b0aa1df06ae60fcc99cd27a26c0b8.jpg)

$$
y _ {4} - z _ {3}
$$

![](images/f8d9c85363ce3d6aa013e91961cd52be43aae64988798e161f6917737dc1ee8f.jpg)

$$
y _ {1} - z _ {1}
$$

$$
\left(\left(y _ {3} - z _ {2}\right) + \left(y _ {4} - z _ {3}\right) + \left(y _ {1} - z _ {1}\right)\right) \mathfrak {S} _ {[ 1, 4, 5, 2, 3 ]} (x; y)
$$

![](images/51638386256c620fc138e704dab6ed8067828e110217ee0430b5cdd072da3c16.jpg)

$$
y _ {1} - z _ {1}
$$

![](images/4840ca5254dc89e7ea57f6fe7c9cbe5954093f5ccb5b1d342939407fa04194e1.jpg)

$$
y _ {2} - z _ {2}
$$

![](images/f292d81bb76d20a6964e8443cb109c829693a8c151036ac74850d6082ad091d0.jpg)

$$
y _ {3} - z _ {3}
$$

$$
\left(\left(y _ {1} - z _ {1}\right) + \left(y _ {2} - z _ {2}\right) + \left(y _ {3} - z _ {3}\right)\right) \mathfrak {S} _ {[ 2, 3, 5, 1, 4 ]} (x; y)
$$

$$
\begin{array}{c c c c} [ 1, 5, 3, 2, 4 ] & [ 1, 5, 3, 2, 4 ] & [ 1, 5, 3, 2, 4 ] \\ \hline 1 & ① & 3 & 5 \\ 3 & 3 & 1 & 1 \\ 5 & 5 & 5 & 3 \\ 2 & 2 & 2 & 2 \\ 4 & 4 & 4 & 4 \\ y _ {1} - z _ {1} & y _ {5} - z _ {3} & y _ {3} - z _ {2} \end{array}
$$

$$
\begin{array}{c c c c} ((y _ {1} - z _ {1}) + (y _ {5} - z _ {3}) + (y _ {3} - z _ {2})) \mathfrak {S} _ {[ 1, 5, 3, 2, 4 ]} (x; y) \\ [ 1, 5, 4, 2, 3 ] & [ 2, 4, 5, 1, 3 ] & [ 2, 5, 3, 1, 4 ] \\ 1 \underbrace {3} _ {3} & 1 \underbrace {2} _ {3} & 4 \\ 1 & 2 & 3 \\ 3 & 2 & 4 \\ 5 & 5 & 5 \\ 5 & 5 & 5 \\ 5 & 5 & 5 \\ 5 & 5 & 5 \\ 2 & 1 & 1 \\ 4 & 4 & 4 \\ 4 & 4 & 3 \\ 1 & 1 & 1 \end{array} \qquad \begin{array}{c c c c} [ 2, 4, 5, 1, 3 ] & [ 2, 5, 3, 1, 4 ] \\ 1 \underbrace {2} _ {3} & 1 \underbrace {2} _ {3} & 3 \\ 3 & 3 & 2 & 2 \\ 5 & 5 & 5 & 3 \\ 2 & 1 & 1 & 1 \\ 4 & 4 & 4 & 4 \end{array}
$$

$$
\begin{array}{c c c c} [ 1, 6, 3, 2, 4, 5 ] \\ 1 & 3 & 5 & 6 \\ 3 & 1 & 1 & 1 \\ 5 & 5 & 3 & 3 \\ 2 & 2 & 2 & 2 \\ 4 & 4 & 4 & 4 \\ 6 & 6 & 6 & 5 \\ & & 1 \end{array}
$$

$$
\mathfrak {S} _ {[ 1, 5, 4, 2, 3 ]} (x; y) + \mathfrak {S} _ {[ 2, 4, 5, 1, 3 ]} (x; y) + \mathfrak {S} _ {[ 2, 5, 3, 1, 4 ]} (x; y) + \mathfrak {S} _ {[ 1, 6, 3, 2, 4, 5 ]} (x; y)
$$

Example 3.3. Our formula computes the product of the double Schubert polynomial $\mathfrak { S } _ { [ 1 , 4 , 3 , 2 ] } ( x ; y )$ , which is not a factorial Schur polynomial, with the factorial Schur polynomial $s _ { ( 2 , 1 ) } ( x _ { 1 } , x _ { 2 } ; z )$ . We set $u = [ 1 , 4 , 3 , 2 ]$ , $v = \left\lfloor 2 , 4 , 1 , 3 \right\rfloor$ . We compute the coefficient where $w = \left\lfloor 3 , 4 , 1 , 2 \right\rfloor$ . We have

$$
\mu_ {v} = [ 4, 2, 1, 3 ]
$$

$$
\mathfrak {c} (\mu_ {v}) = (3, 1)
$$

$$
\lambda (v) = (2, 1, 1)
$$

$$
v ^ {- 1} \mu_ {v} = [ 2, 1 ]
$$

$$
w v ^ {- 1} \mu_ {v} = [ 4, 3, 1, 2 ]
$$

$$
\begin{array}{c c c c} 1 & \boxed {①} & 3 & 4 \\ 4 & \boxed {④} & 4 & 3 \\ 3 & 3 & 1 & 1 \\ 2 & 2 & 2 & 2 \end{array}
$$

$$
(y _ {1} - z _ {1}) (y _ {4} - z _ {1})
$$

$$
\begin{array}{c c c c} 1 & 3 & ③ & 4 \\ 4 & ④ & 4 & 3 \\ 3 & 1 & 1 & 1 \\ 2 & 2 & 2 & 2 \end{array}
$$

$$
(y _ {3} - z _ {2}) (y _ {4} - z _ {1})
$$

$$
\begin{array}{c c c c} 1 & \framebox {3} & 4 & \text {\scriptsize ④} \\ 4 & \framebox {\text {\scriptsize ④}} & \framebox {3} & 3 \\ 3 & \framebox {1} & \framebox {1} & 1 \\ 2 & \framebox {2} & \framebox {2} & 2 \end{array}
$$

$$
(y _ {4} - z _ {1}) (y _ {4} - z _ {3})
$$

Thus

$$
c _ {u v} ^ {w} (y; z) = \left(y _ {1} - z _ {1}\right) \left(y _ {4} - z _ {1}\right) + \left(y _ {3} - z _ {2}\right) \left(y _ {4} - z _ {1}\right) + \left(y _ {4} - z _ {1}\right) \left(y _ {4} - z _ {3}\right)
$$

Now we compute the coefficient for $w = [ 3 , 5 , 1 , 2 , 4 ]$ . We have $w v ^ { - 1 } \mu _ { v } = [ 5 , 3 , 1 , 2 , 4 ]$ .

$$
\begin{array}{c} 1 \\ 4 \\ 3 \\ 2 \\ 5 \end{array} \begin{array}{c} \text {①} \quad 3 \quad 5 \\ \text {5} \quad \text {5} \quad 3 \\ 3 \quad 1 \quad 1 \\ 2 \quad 2 \quad 2 \quad 2 \\ 4 \quad 4 \quad 4 \quad 4 \\ y _ {1} - z _ {1} \end{array}
$$

$$
\begin{array}{c} 1 \\ 4 \\ 3 \\ 2 \\ 5 \end{array} \begin{array}{c c c} 3 & ③ & 5 \\ 5 & 5 & 3 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \\ 4 & 4 & 4 \\ y _ {3} - z _ {2} \end{array}
$$

$$
\begin{array}{c} 1 \quad \left\lfloor \begin{array}{c c c} 3 & 4 & 5 \\ \text {④} \end{array} \right. \\ 3 \quad 1 \quad 1 \quad 1 \\ 2 \quad 2 \quad 2 \quad 2 \\ 5 \quad 5 \quad 5 \quad 4 \\ y _ {4} - z _ {1} \end{array}
$$

$$
\begin{array}{c} 1 \\ 4 \\ 3 \\ 2 \\ 5 \end{array} \begin{array}{c c c} 3 & 5 & \text {\textcircled {5}} \\ 5 \hline 3 & 3 \\ 1 & 1 & 1 \\ 2 & 2 & 2 \\ 4 & 4 & 4 \\ y _ {5} - z _ {3} \end{array}
$$

Thus

$$
c _ {u v} ^ {w} (y; z) = \left(y _ {1} - z _ {1}\right) + \left(y _ {3} - z _ {2}\right) + \left(y _ {4} - z _ {1}\right) + \left(y _ {5} - z _ {3}\right)
$$

# 4. Proof of Theorem 3.1

We show in this section that if $u$ and $v$ satisfy the hypotheses of Theorem 3.1, then we may reduce multiplying $\mathfrak { S } _ { u } ( x ; y )$ by ${ \mathfrak { S } } _ { v } ( x ; z )$ to multiplying $\mathfrak { S } _ { u } ( x ; y )$ by the double Schubert polynomial corresponding to $v$ ’s dominant approximation, ${ \mathfrak { S } } _ { \mu _ { v } } ( x ; z )$ . We then show that a double Schubert polynomial corresponding to a dominant permutation is a product of factorial elementary symmetric polynomials, which will allow us to reduce the computation to applying the Pieri formula. The special case of the Pieri formula that we will need is Proposition 4.4, which we will prove in Section 7.

Lemma 4.1. Let $u , v , w \in S _ { \infty }$ , and suppose $i ~ > ~ 0$ is such that $\ell ( w s _ { i } ) < \ell ( w )$ . If $\ell ( u s _ { i } ) > \ell ( u )$ and $\ell ( v s _ { i } ) > \ell ( v )$ , then $c _ { u v } ^ { w } ( y ; z ) = 0$ .

Proof. Recall that

$$
c _ {u v} ^ {w} (x; z) = \partial_ {u} ^ {w} \left(\mathfrak {S} _ {v} (x; z)\right)
$$

Since $\ell ( u s _ { i } ) > \ell ( u )$ we have that

$$
\partial_ {u} ^ {w} = \partial_ {u} ^ {w s _ {i}} \partial^ {s _ {i}}
$$

Since $\partial ^ { s _ { i } } ( \mathfrak { S } _ { v } ( x ; z ) ) = 0$ , we have the result.

![](images/745d8b350aa36dbecb70d7e8e38232b975ca817880eb60a3fe40c58c9e54a483.jpg)

Lemma 4.2. Let $u , v , w \in S _ { \infty }$ and let $i > 0$ be such that $\ell ( u s _ { i } ) > \ell ( u )$ , $\ell ( v s _ { i } ) > \ell ( v )$ , and $\ell ( w s _ { i } ) > \ell ( w )$ Then

$$
c _ {u v} ^ {w} (y; z) = c _ {u, v s _ {i}} ^ {w s _ {i}} (y; z)
$$

Proof. We have that

$$
\partial_ {u} ^ {w s _ {i}} = \partial_ {u} ^ {w} \partial^ {s _ {i}}
$$

Hence

$$
\partial_ {u} ^ {w s _ {i}} \left(\mathfrak {S} _ {v s _ {i}} (x; z)\right) = \partial_ {u} ^ {w} \left(\partial^ {s _ {i}} \left(\mathfrak {S} _ {v s _ {i}} (x; z)\right)\right) = \partial_ {u} ^ {w} \left(\mathfrak {S} _ {v} (x; z)\right)
$$

and the result follows.

![](images/47a689806fd1aff8519c34549ff3c258b24e0fc7acf6e3d0a57f45cae4cd4452.jpg)

Proposition 4.3. Suppose $p$ is a positive integer, $u \in S _ { \infty }$ satisfies $\ell ( u s _ { i } ) > \ell ( u )$ for all $i < p$ , and $v \in S _ { \infty }$ satisfies $\ell ( v s _ { i } ) > \ell ( v )$ for all $i > p$ . Then $c _ { u v } ^ { w } ( y ; z ) = 0$ unless $\ell ( w v ^ { - 1 } \mu _ { v } ) = \ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ , in which case

$$
c _ {u v} ^ {w} (y; z) = c _ {u, \mu_ {v}} ^ {w v} ^ {- 1} ^ {\mu_ {v}} (y; z)
$$

Proof. Note that for any permutation $i > p$ . use e res and induction on . Otherwise, $v$ we have that $\ell ( \mu _ { v } ) - \ell ( v )$ $\ell ( v s _ { i } ) > \ell ( v )$ . If  the $\ell ( \mu _ { v } ) - \ell ( v ) = 0$ for all $i > p$ , then uch th if and only if $c _ { u v } ^ { w } ( y ; z ) = c _ { u , \mu _ { v } } ^ { w v ^ { - 1 } \mu _ { v } } ( y ; z )$ $\mathfrak { c } _ { i } ( v ) = 0$ for all $v ^ { - 1 } \mu _ { v } = 1$ $v = \mu _ { v }$ $i$ $\mathfrak { c } _ { i } ( v ) < \mathfrak { c } _ { i + 1 } ( v )$ $\mathfrak { c } _ { i + 1 } ( v ) \ne 0$ , we must have that $i < p$ . Therefore, by assumption $\ell ( u s _ { i } ) > \ell ( u )$ . Also, since $\mathfrak { c } _ { j } ( v ) = \mathfrak { c } _ { j } ( v s _ { i } ) = 0$ for all $j > p$ , it follows that $\ell ( v s _ { i } s _ { j } ) > \ell ( v s _ { i } )$ for all $j > p$ .

We split the argument into whether or not $\ell ( w s _ { i } ) \ < \ \ell ( w )$ . Assume first that $\ell ( w s _ { i } ) < \ell ( w )$ . Note that ${ \boldsymbol { v } } ^ { - 1 } { \boldsymbol { \mu } } _ { v }$ has a specific expression as a product of $\ell ( \mu _ { v } ) - \ell ( v )$ simple reflections (the ones that occur in the recursion passing from $\boldsymbol { v }$ to $\mu _ { v }$ ), with the first being $s _ { i }$ , and in order for $w ( v ^ { - 1 } \mu _ { v } )$ to have length $\ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ each of these must successively increase the length by 1 in the multiplication of $w$ on the right by ${ \boldsymbol { v } } ^ { - 1 } { \boldsymbol { \mu } } _ { v }$ . Since the length decreases upon multiplication by the first reflection $s _ { i }$ , we must have that $\ell ( w v ^ { - 1 } \mu _ { v } ) < \ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ . By Lemma 4.1 we also have that $c _ { u v } ^ { w } ( y ; z ) = 0$ since both $\ell ( u s _ { i } ) > \ell ( u )$ and $\ell ( v s _ { i } ) > \ell ( v )$ . Thus, if $\ell ( w s _ { i } ) < \ell ( w )$ then $c _ { u v } ^ { w } ( y ; z ) = 0$ and $\ell ( w v ^ { - 1 } \mu _ { v } ) < \ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ , so the result follows in that case.

Assume then that $\ell ( w s _ { i } ) > \ell ( w )$ . In that case, by Lemma 4.2, $c _ { u v } ^ { w } ( y ; z ) = c _ { u , v s _ { i } } ^ { w s _ { i } } ( y ; z )$ . We have that $\mu _ { v s _ { i } } = \mu _ { v }$ by definition, and $\ell ( \mu _ { v } ) - \ell ( v s _ { i } ) < \ell ( \mu _ { v } ) - \ell ( v )$ . Note that

$$
w v ^ {- 1} \mu_ {v} = w \left(s _ {i} s _ {i}\right) v ^ {- 1} \mu_ {v} = w s _ {i} \left(v s _ {i}\right) ^ {- 1} \mu_ {v}
$$

By the induction hypothesis, we have that $c _ { u , v s _ { i } } ^ { w s _ { i } } ( y ; z ) = 0$ unless

$$
\ell (w v ^ {- 1} \mu_ {v}) = \ell (w s _ {i} (v s _ {i}) ^ {- 1} \mu_ {v}) = \ell (w s _ {i}) + \ell ((v s _ {i}) ^ {- 1} \mu_ {v}) = \ell (w) + \ell (v ^ {- 1} \mu_ {v})
$$

In the case where the length condition is satisfied (where there is a possibility that $c _ { u , v s _ { i } } ^ { w s _ { i } } ( y ; z ) \neq 0$ ), by the induction hypothesis we have that

$$
c _ {u v} ^ {w} (y; z) = c _ {u, v s _ {i}} ^ {w s _ {i}} (y; z) = c _ {u, \mu_ {v s _ {i}}} ^ {w s _ {i} (v s _ {i}) ^ {- 1} \mu_ {v s _ {i}}} (y; z) = c _ {u, \mu_ {v}} ^ {w v ^ {- 1} \mu_ {v}} (y; z)
$$

and it follows that Having verified $c _ { u v } ^ { w } ( y ; z ) = 0$ unless hausti $\ell ( w v ^ { - 1 } \mu _ { v } ) = \ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ ase  th $c _ { u v } ^ { w } ( y ; z ) = c _ { u , \mu _ { v } } ^ { w v ^ { - 1 } \mu _ { v } } ( y ; z )$ $\ell ( w s _ { i } ) < \ell ( w )$ $\ell ( w s _ { i } ) > \ell ( w )$ the increase in length difference from the induction hypothesis, we have the result by induction. 

Definition 4.1 (Factorial elementary symmetric polynomials $E _ { k } ( x ; z )$ , $E _ { p , k } ( x ; z ) )$ . Let $E _ { k } ( x ; z )$ be the factorial elementary symmetric polynomial defined by

$$
E _ {k} (x; z) = \prod_ {i = 1} ^ {k} \left(x _ {i} - z _ {1}\right)
$$

This is the double Schubert polynomial ${ \mathfrak { S } } _ { c _ { k , k } } ( x ; z )$ where

$$
c _ {p, k} = s _ {k + 1 - p} s _ {k + 2 - p} \dots s _ {k}
$$

We define more generally

$$
E _ {p, k} (x; z) = \mathfrak {S} _ {c _ {p, k}} (x; z)
$$

so that $E _ { k } ( x ; z ) = E _ { k , k } ( x ; z )$ . If $p < 0$ or $p > k$ , we define

$$
E _ {p, k} (x; z) = 0
$$

Since exactly one $z$ variable occurs in the product for $E _ { k } ( x ; z )$ , namely $z _ { 1 }$ , we use the notation $E _ { k } ( x ; z _ { j } )$ for any $j$ to substitute $z _ { j }$ for $z _ { 1 }$ .

Proposition 4.4. Let $j , k$ be positive integers and suppose $u \in S _ { \infty }$ . Then

$$
\mathfrak{S}_{u}(x;y)E_{k}(x;z_{j}) = \sum_{\substack{k\\ u\to w}}\mathrm{weight}^{w}_{u,k}(y;z_{j})  \mathfrak{S}_{w}(x;y)
$$

We postpone the proof of this to Section 7.

The next lemma, for which we cite [21, (6.14)], expresses the double Schubert polynomial corresponding to a dominant permutation as a product of these factorial elementary symmetric polynomials.

Lemma 4.5. Suppose $v \in S _ { \infty }$ . Then

$$
\mathfrak {S} _ {\mu_ {v}} (x; z) = \prod_ {i = 1} ^ {\infty} E _ {\lambda_ {i} (v)} (x; z _ {i})
$$

Proof. In [21, (6.14)] there is a formula for the double Schubert polynomial corresponding to a dominant permutation $\mu$ in terms of the coordinates of the boxes in the Young diagram of ${ \mathfrak { c } } ( \mu )$ . The formula is

$$
\mathfrak {S} _ {\mu_ {v}} (x; z) = \prod_ {(i, j) \in Y _ {c (\mu_ {v})}} \left(x _ {i} - z _ {j}\right)
$$

If we fix $j$ and consider the terms involving $z _ { j }$ in this product, the terms that occur are $x _ { i } - z _ { j }$ where $1 \leq i \leq \lambda _ { j } ( v )$ , since the length of this column in the diagram is the value at the corresponding index in the conjugate partition of the code. The product of these terms is therefore equal to $E _ { \lambda _ { j } ( v ) } ( x ; z _ { j } )$ . Iterating over $j$ , we obtain the result. 

From this we may derive the following.

Proposition 4.6. Suppose $u , v \in S _ { \infty }$ . Then

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {\mu_ {v}} (x; z) = \sum_ {w \in S _ {\infty}} d _ {u, \lambda (v)} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

Proof. Assume the length of the partition $\lambda ( v )$ is $m$ . To shorten notation, for an integer $0 \leq p \leq m$ define a partition $\lambda ^ { p }$ a s

$$
\lambda^ {p} = \left(\lambda_ {1} (v), \dots , \lambda_ {p} (v)\right)
$$

We note by Lemma 4.5 that

$$
\mathfrak {S} _ {\mu_ {v}} (x; z) = \prod_ {i = 1} ^ {m} E _ {\lambda_ {i} (v)} (x; z _ {i})
$$

We apply Proposition 4.4 and induction to successively multiply by the factors of ${ \mathfrak { S } } _ { \mu _ { v } } ( x ; z )$ . The statement we will prove is that for $0 \leq p \leq m$ we have

$$
\mathfrak {S} _ {u} (x; y) E _ {\lambda_ {1} (v)} (x; z _ {1}) \dots E _ {\lambda_ {p} (v)} (x; z _ {p}) = \sum_ {w} d _ {u, \lambda^ {p}} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

For the base case, multiplying by none of the factors, the product is $\mathfrak { S } _ { u } ( x ; y )$ . Assume the induction hypothesis that for some $p$ with $p - 1 < m$ we have

$$
\mathfrak {S} _ {u} (x; y) E _ {\lambda_ {1} (v)} (x; z _ {1}) \dots E _ {\lambda_ {p - 1} (v)} (x; z _ {p - 1}) = \sum_ {w} d _ {u, \lambda^ {p - 1}} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

We multiply both sides by the additional factor $E _ { \lambda _ { p } ( v ) } ( x ; z _ { p } )$ , applying Proposition 4.4:

$$
\mathfrak{S}_{u}(x;y)E_{\lambda_{1}(v)}(x;z_{1})\dots E_{\lambda_{p}(v)}(x;z_{p}) = \sum_{w}\sum_{\substack{\lambda_{p}(v)\\ w^{\prime}:w\longrightarrow w^{\prime}}}d^{w}_{u,\lambda^{p - 1}}(y;z)\mathrm{weight}^{w^{\prime}}_{w,\lambda_{p}(v)}(y;z_{p})\mathfrak{S}_{w^{\prime}}(x;y)
$$

Interchange the order of summation on the right hand side to obtain that the coefficient of ${ \mathfrak { S } } _ { w ^ { \prime } } ( x ; y )$ is, fixing $w ^ { \prime }$ and summing over all $w$ ,

$$
\sum_{\substack{\lambda_{p}(v)\\ w:w\longrightarrow w^{\prime}}}d^{w}_{u,\lambda^{p - 1}}(y;z)\mathrm{weight}^{w^{\prime}}_{w,\lambda_{p}(v)}(y;z_{p})
$$

We claim that this is equal to $d _ { u , \lambda ^ { p } } ^ { w ^ { \prime } } ( y ; z )$ . Recall that $d _ { u , \lambda ^ { p - 1 } } ^ { w } ( y ; z )$ is a sum over paths

$$
u = u _ {0} \xrightarrow {\lambda_ {1} (v)} u _ {1} \xrightarrow {\lambda_ {2} (v)} \dots \xrightarrow {\lambda_ {p - 1} (v)} u _ {p - 1} = w
$$

of the product

$$
\prod_ {i = 1} ^ {p - 1} \mathrm {w e i g h t} _ {u _ {i - 1}, \lambda_ {i} (v)} ^ {u _ {i}} (y; z _ {i})
$$

We are extending each path by an additional edge $w \xrightarrow { \lambda _ { p } ( v ) } w ^ { \prime }$ λp(v)−−−→ w′. As this ranges over all w (the penultimate $w$ element in the path), we obtain exactly the paths that occur in the sum for $d _ { u , \lambda ^ { p } } ^ { w ^ { \prime } } ( y ; z )$ with the desired extra factor occurring in the weight, obtaining the result by induction. 

Proof of Theorem 3.1. By Proposition 4.3, we have under the conditions that $c _ { u v } ^ { w } ( y ; z ) = 0$ unless $\ell ( w v ^ { - 1 } \mu _ { v } ) =$ $\ell ( w ) + \ell ( v ^ { - 1 } \mu _ { v } )$ , in which case we have

$$
c _ {u v} ^ {w} (y; z) = c _ {u, \mu_ {v}} ^ {w v ^ {- 1} \mu_ {v}} (y; z)
$$

By Proposition 4.6 we have that

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {\mu_ {v}} (x; z) = \sum_ {w ^ {\prime} \in S _ {\infty}} d _ {u, \lambda (v)} ^ {w ^ {\prime}} (y; z) \mathfrak {S} _ {w ^ {\prime}} (x; y)
$$

Picking out the coefficient of $\mathfrak { S } _ { w ^ { \prime } } ( x ; y )$ with $w ^ { \prime } = w v ^ { - 1 } \mu _ { v }$ we obtain the result.

# 5. Positive formula for (skew) double Schubert polynomials

Theorem 3.1 yields a nontrivial formula even when $u$ is the identity. In that case, $\partial _ { u } ^ { w } \ = \ \partial ^ { w }$ , hence $c _ { u v } ^ { w } ( x ; y ) = \partial ^ { w } ( \mathfrak { S } _ { v } ( x ; y ) )$ . Thus

$$
c _ {1, v} ^ {1} (x; y) = \mathfrak {S} _ {v} (x; y)
$$

and hence our formula yields a positive formula for double Schubert polynomials. We record this as a theorem.

Theorem 5.1. For all $v \in S _ { \infty }$ we have

$$
\mathfrak {S} _ {v} (x; y) = e _ {1, v} ^ {1} (x; y)
$$

and hence $\mathfrak { S } _ { v } ( x ; y )$ is a polynomial in the differences $x _ { i } - y _ { j }$ with nonnegative integer coefficients.

Example 5.1. We use the formula to obtain $\mathfrak { S } _ { [ 1 , 4 , 3 , 2 ] } ( x ; y )$ . We set $u = 1$ , $v = [ 1 , 4 , 3 , 2 ]$ , and $w = 1$ . Then

$$
\mu_ {v} = [ 4, 3, 1, 2 ]
$$

$$
\mathfrak {c} (\mu_ {v}) = (3, 2)
$$

$$
\lambda (v) = (2, 2, 1)
$$

$$
v ^ {- 1} \mu_ {v} = [ 2, 3, 1 ]
$$

$$
w v ^ {- 1} \mu_ {v} = [ 2, 3, 1 ]
$$

We iterate over the paths to obtain the polynomial.

$$
\begin{array}{c} 1 \\ 2 \\ 3 \end{array} \begin{array}{c c c} \underline {{①}} & \underline {{①}} & 2 \\ \underline {{②}} & 3 & \underline {{3}} \\ 3 & 2 & 1 \end{array}
$$

$$
(x _ {1} - y _ {1}) (x _ {1} - y _ {2}) (x _ {2} - y _ {1})
$$

$$
\begin{array}{c} 1 \\ 2 \\ 3 \end{array} \begin{array}{c c c} \text {①} & \text {①} & 2 \\ \text {3} & \text {③} & \text {3} \\ 2 & 2 & 1 \end{array}
$$

$$
(x _ {1} - y _ {1}) (x _ {1} - y _ {2}) (x _ {3} - y _ {2})
$$

$$
\begin{array}{c} 1 \\ 2 \\ 3 \end{array} \begin{array}{c c c} \text {\textcircled {1}} & 2 & \text {\textcircled {2}} \\ \text {\textcircled {2}} & 3 & \text {\textcircled {3}} \\ \text {\textcircled {3}} & 1 & \text {\textcircled {1}} \end{array}
$$

$$
(x _ {1} - y _ {1}) (x _ {2} - y _ {1}) (x _ {2} - y _ {3})
$$

$$
\begin{array}{c} 1 \\ 2 \\ 3 \end{array} \begin{array}{c c c} \text {①} & 2 & \text {②} \\ \text {3} & \text {③} \hline 3 \\ \text {2} & 1 & 1 \end{array}
$$

$$
(x _ {1} - y _ {1}) (x _ {2} - y _ {3}) (x _ {3} - y _ {2})
$$

$$
\begin{array}{c} 1 \\ 2 \\ 3 \end{array} \begin{array}{c c c} 2 & ② & ② \\ 3 & ③ & 3 \\ 1 & 1 & 1 \end{array}
$$

$$
(x _ {2} - y _ {2}) (x _ {2} - y _ {3}) (x _ {3} - y _ {2})
$$

Thus

$$
\begin{array}{l} \mathfrak {S} _ {[ 1, 4, 3, 2 ]} (x; y) = \left(x _ {1} - y _ {1}\right) \left(x _ {1} - y _ {2}\right) \left(x _ {2} - y _ {1}\right) + \left(x _ {1} - y _ {1}\right) \left(x _ {2} - y _ {1}\right) \left(x _ {2} - y _ {3}\right) + \left(x _ {1} - y _ {1}\right) \left(x _ {1} - y _ {2}\right) \left(x _ {3} - y _ {2}\right) \\ + (x _ {1} - y _ {1}) (x _ {2} - y _ {3}) (x _ {3} - y _ {2}) + (x _ {2} - y _ {2}) (x _ {2} - y _ {3}) (x _ {3} - y _ {2}) \\ \end{array}
$$

While our formula for double Schubert polynomials derived in this way is new, it is not the first positive formula for double Schubert polynomials in terms of $x _ { i } - y _ { j }$ . For example, see the formula in [13] using the pipe dreams (or equivalently RC-graphs) in [1]. We suspect from empirical evidence, though have not proved, that a modification of our formula for Sv(x; y) to computing cv w0(n)1,w0(n) $\mathfrak { S } _ { v } ( x ; y )$ $c _ { 1 , w _ { 0 } ( n ) } ^ { v ^ { - 1 } w _ { 0 } ( n ) } ( x ; y )$ but applying Proposition 4.4 in increasing order of degree instead of decreasing order yields the same terms as the definition of pipe dream polynomials with the corresponding RC-graph obtained directly by sorting the columns of our diagram. It would be interesting to establish this correspondence in general. We give an example.

Example 5.2 (Illustration of the conjectural relation to RC-graphs). An example RC-graph for the permutation $v = [ 3 , 1 , 4 , 6 , 5 , 2 ]$ is given in Figure (3.1) in [1]. Namely, the example is

The corresponding term in the double Schubert polynomial given by the formula in [13] (each plus sign gives a factor of $x _ { r } - y _ { c }$ , where $r$ is the row and $c$ is the column) would be

$$
(x _ {1} - y _ {1}) (x _ {1} - y _ {2}) (x _ {1} - y _ {5}) (x _ {2} - y _ {2}) (x _ {3} - y _ {2}) (x _ {5} - y _ {1})
$$

Applying Proposition 4.4 to

$$
\mathfrak {S} _ {w _ {0} (5)} (x; y) = E _ {1} (x; y _ {5}) E _ {2} (x; y _ {4}) E _ {3} (x; y _ {3}) E _ {4} (x; y _ {2}) E _ {5} (x; y _ {1})
$$

to compute cv w0(5)1,w0(5) $c _ { 1 , w _ { 0 } ( 5 ) } ^ { v ^ { - 1 } w _ { 0 } ( 5 ) } ( x ; y )$ we obtain for one of the terms the following diagram, multiplying in increasing order of degree, beginning the path in the diagram from the right:

![](images/6c67de8a919d7f101c809292d466c6699d37d5afd512453f33315812f2a47abb.jpg)

This diagram yields the same term as the RC-graph. Sorting the columns in this diagram, we obtain

![](images/7d4b64899e5db96eac61a781f131641e3cd59a4fcff659042ae2ec267c35f8d3.jpg)

which coincides with the RC-graph. The interested reader may wish to verify that the remaining 14 diagrams all coincide with other RC-graphs for $\boldsymbol { v }$ in the same way.

While one might initially expect that any formula should involve the same term at some point, this specific term does not occur at all in the formula for $e _ { 1 , v } ^ { 1 } ( x ; y )$ , which uses a different dominant permutation and uses multiplication in decreasing order of degree (with increasing order of indices). Expressions of double Schubert polynomials $\mathfrak { S } _ { v } ( x ; y )$ for permutations $\boldsymbol { v }$ as polynomials in $x _ { i } - y _ { j }$ are generally not at all unique. This is easily seen in the simple example of the polynomial

$$
\mathfrak {S} _ {s _ {2}} (x; y) = \left(x _ {1} - y _ {1}\right) + \left(x _ {2} - y _ {2}\right) = \left(x _ {1} - y _ {2}\right) + \left(x _ {2} - y _ {1}\right)
$$

and in general for the linear double Schubert polynomials in $n$ variables there are $n$ ! ways to group the terms.

equivalently that there ar Kirillov in [12] defines skew Schubert polynomials as polynomials of the form $u ^ { - 1 } ( c _ { u , w _ { 0 } ( n ) } ^ { w } ( x ; 0 ) )$ , and conjectures that they have nonnegative integer coefficients. We note skew Schubert polynomials, for example in [7], [2], [20], and [28]. Using our $u ^ { - 1 } \partial _ { u } ^ { w } ( \mathfrak { S } _ { w _ { 0 } ( n ) } ( x ) )$ , or formulas, we have been able to prove Kirillov’s conjecture.

Theorem 5.2. The skew Schubert polynomials defined by Kirillov in [12] have nonnegative integer coefficients.

Proof. We have that $c _ { u , w _ { 0 } ( n ) } ^ { w } ( x ; 0 ) = e _ { u , w _ { 0 } ( n ) } ^ { w } ( x ; 0 )$ since $w _ { 0 } ( n )$ is dominant, hence any permutation of this polynomial has nonnegative integer coefficients. 

The polynomials $c _ { u , w _ { 0 } ( n ) } ^ { w } ( 0 ; - y )$ seem to be closely related to the skew Schubert polynomials in [20] and [2] in that they are nonnegative linear combinations of ordinary Schubert polynomials via Littlewood-Richardson coefficients, and it would be worthwhile to investigate the connection between them, which we will not do here. The “double skew Schubert polynomials” $c _ { u , w _ { 0 } ( n ) } ^ { w } ( x ; - y )$ would then seem to connect Kirillov’s skew Schubert polynomials and polynomials similar to Lenart’s/Bergeron’s/Sottile’s.

Example 5.3. We compute, using our positive formula, the skew Schubert polynomial computed in Example 3 of [12], up to a permutation. Specifically, the polynomial being computed is $c _ { u , w _ { 0 } ( 3 ) } ^ { w } ( x ; 0 )$ , where $u =$ [3, 1, 2, 4] and $w = \left\lfloor 4 , 3 , 1 , 2 \right\rfloor$ .

![](images/b9488ad12a3dc7097980d16f7eaf37f39944fae6d7b724704f2c2d652a21d588.jpg)

Setting $y = 0$ , we obtain $( x _ { 3 } ^ { 2 } + x _ { 3 } x _ { 4 } + x _ { 4 } ^ { 2 } ) x _ { 1 }$ , which is the desired permutation of the result given in the article, $( x _ { 1 } ^ { 2 } + x _ { 1 } x _ { 4 } + x _ { 4 } ^ { 2 } ) x _ { 2 }$ .

# 6. Equivariant positivity

The order of multiplication by factorial elementary symmetric polynomials in computation of $e _ { u v } ^ { w } ( y ; z )$ may seem arbitrary, and indeed any order will of course give the same overall result. Example 5.2 illustrates that different choices can result in interesting combinatorial consequences. The particular choice of multiplying in decreasing order of degree (with increasing order of indices) is advantageous in that it gives a positive formula for $c _ { u v } ^ { w } ( y ; y )$ for the relevant $u$ and $\boldsymbol { v }$ , as we show in this section.

Definition 6.1 (Graham-nonnegative). The negative roots are the linear polynomials of the form $y _ { j } - y _ { i }$ with $j > i$ , and the simple negative roots are the polynomials $\alpha _ { i } = y _ { i + 1 } - y _ { i }$ . It is easy to see that the negative roots have nonnegative coefficients when expressed in terms of the simple negative roots. A polynomial $P ( y )$ is said to be Graham-nonnegative if $P ( y )$ can be expressed as a polynomial in the simple negative roots with nonnegative integer coefficients.

Theorem 6.1. Let $u , w \in S _ { \infty }$ , let $\lambda$ be a partition, and suppose $P \in \operatorname { P a t h } _ { \lambda } ( u , w )$ . Then weight ${ } _ { P , \lambda } ( \boldsymbol { y } ; \boldsymbol { y } )$ is Graham-nonnegative.

This requires some setup.

Definition 6.2 (Factors of a path). Let $\lambda$ be a partition and let $P = ( u _ { 0 } , \dots , u _ { m } ) \in \operatorname { P a t h } _ { \lambda } ( u , w )$ . Then if $a , q$ are integers we say that $( a , q )$ is a factor of $P$ if $1 \leq q \leq m$ , $1 \leq a \leq \lambda _ { q }$ , and

$$
u _ {q - 1} (a) = u _ {q} (a)
$$

This factor is said to be in row $a$ and column $q$ . If $( a , q )$ is a factor of $P$ , then $( a , q )$ is said to be a negative factor if $u _ { q } ( a ) < q$ , a zero factor if $u _ { q } ( a ) = q$ , and a positive factor if $u _ { q } ( a ) > q$ .

Lemma 6.2. Let be permutations, let $\lambda$ be a partition, and let $P \in \operatorname { P a t h } _ { \lambda } ( u , w )$ . If $( j , k )$ is a negative $u , w$ factor of $P$ , then there exists a zero factor $( a , q )$ of $P$ with $q \leq k$ .

Proof. Let $P = ( u _ { 0 } , \ldots , u _ { m } ) $ . We note that it is a consequence of the definition of that for each $1 \leq q \leq m$ we have that if $j \le \lambda _ { q }$ then $u _ { q - 1 } ( j ) \leq u _ { q } ( j )$ . We prove by induction on $q$ that if there are no integers $j , k$ with $k \leq q$ such that $( j , k )$ is a zero factor of $P$ , then for all factors $( j , k )$ of $P$ with $1 \leq k \leq q$ we have that $( j , k )$ is a positive factor of $P$ . For $q = 1$ this is clear, as in that case any factor is either a positive factor or a zero factor. Otherwise, suppose it holds for all $q ^ { \prime } < q$ for some $q > 1$ . Then if there are no zero factors to the left of column $q$ , since $u _ { q - 1 } ( j ) \geq q$ for all $j \le \lambda _ { q - 1 }$ by the induction hypothesis we have that $u _ { q } ( j ) \geq q$ for all $j \le \lambda _ { q }$ . If $u _ { q } ( a ) = q$ for some $a \leq \lambda _ { q }$ then $u _ { q } ( a ) = u _ { q - 1 } ( a ) = q$ and it follows that $( a , q )$ is a zero factor of $P$ . Otherwise we have that $u _ { q } ( j ) > q$ for all $j \le \lambda _ { q }$ , so that there can only be positive factors of $P$ in column $q$ and the result follows by induction. 

Proof of Theorem 6.1. Let $u , w \in S _ { \infty }$ , let $\lambda$ be a partition, and let $P = ( u _ { 0 } , \ldots , u _ { m } ) \in \operatorname { P a t h } _ { \lambda } ( u , w )$ . We show that weight $P , \lambda { \big ( } y ; y )$ is Graham-nonnegative. Recall the definition

$$
\operatorname {w e i g h t} _ {P, \lambda} (y; y) = \prod_ {i = 1} ^ {m} \operatorname {w e i g h t} _ {u _ {i - 1}, \lambda_ {i}} ^ {u _ {i}} (y; y _ {i})
$$

In this product, for each $j$ the factor weigh $_ { u _ { j - 1 } , \lambda _ { j } } ^ { u _ { j } } ( y ; y _ { j } )$ can only fail to be Graham-nonnegative if there exists at least one negative factor $( i , j )$ of $P$ , which would contribute $y _ { u _ { j } ( i ) } - y _ { j }$ to the product with $u _ { j } ( i ) < j$ . However, by Lemma 6.2, if there is such a factor then there exists a zero factor $( a , q )$ with $q \le j$ ; this contributes $y _ { q } \mathrm { ~ - ~ } y _ { q } \mathrm { ~ = ~ } 0$ to $\mathrm { w e i g h t } _ { u _ { q - 1 } , \lambda _ { q } } ^ { u _ { q } } ( y ; y _ { q } )$ , hence $\mathrm { w e i g h t } _ { P , \lambda } ( y ; y ) = 0$ . Therefore if there are any negative factors in the product the entire product vanishes, and it follows that $\mathrm { w e i g h t } _ { P , \lambda } ( y ; y )$ is Grahamnonnegative. 

While Theorem 3.1 fails to be symmetric in that the roles of $u$ and $\boldsymbol { v }$ cannot be interchanged, in the equivariant case it is. Some general results include a positive formula for multiplying a double Schubert polynomial $\mathfrak { S } _ { u } ( x ; y )$ by a factorial Schur polynomial $s _ { \lambda } ( x ; y )$ where the factorial Schur polynomial has at least as many $x$ variables as the double Schubert polynomial, which is an equivariant analog of the formula of Kohnert in [17] (though not in the sense of using the same combinatorial elements). In particular this also

gives a Littlewood-Richardson rule for equivariant cohomology of the Grassmannian, and for multiplying pairs of factorial Schur functions that have different numbers of variables, which is an equivariant analog of the main result of [24]. Most generally, the separated descents case in [15] and [11] is covered in equivariant cohomology.

Example 6.1 (Grassmannian case). This computes the example in Figure 8 of [14]. Let $u = \left\lfloor 2 , 4 , 1 , 3 \right\rfloor$ , let $v = [ 1 , 3 , 2 ]$ , and let $w = \left\lfloor 2 , 4 , 1 , 3 \right\rfloor$ . Then

$$
\mu_ {v} = [ 3, 1, 2 ]
$$

$$
\mathfrak {r} \left(\mu_ {v}\right) = (2)
$$

$$
\lambda (v) = (1, 1)
$$

$$
v ^ {- 1} \mu_ {v} = [ 2, 1 ]
$$

$$
w v ^ {- 1} \mu_ {v} = [ 4, 2, 1, 3 ]
$$

Then $c _ { u v } ^ { w } ( y ; y ) = y _ { 4 } - y _ { 1 }$ , as witnessed by the following paths.

<table><tr><td>2</td><td>②</td><td>4</td><td></td><td>2</td><td>4</td><td>④</td></tr><tr><td>4</td><td>4</td><td>2</td><td></td><td>4</td><td>2</td><td>2</td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>3</td><td>3</td><td></td><td>3</td><td>3</td><td>3</td></tr><tr><td>y2</td><td>- y1</td><td></td><td></td><td>y4</td><td>- y2</td><td></td></tr></table>

The formula in [14] also has two terms that combine to yield the $y _ { 4 } - y _ { 1 }$ , but the weight of the two terms is $y _ { 4 } - y _ { 3 }$ and $y _ { 3 } - y _ { 1 }$ , which are different from the elements of our formula.

Now let $w = [ 3 , 4 , 1 , 2 ]$ . Then $w v ^ { - 1 } \mu _ { v } = [ 4 , 3 , 1 , 2 ]$ and $c _ { u v } ^ { w } ( y ; y ) = 1$ , as witnessed by the following path:

<table><tr><td>2</td><td>3</td><td>4</td></tr><tr><td>4</td><td>4</td><td>3</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>2</td><td>2</td></tr><tr><td></td><td>1</td><td></td></tr></table>

There is a third term in the expansion of the product, but in [14] this is 0 because it falls outside the cohomology ring of the chosen Grassmannian.

Example 6.2. We multiply a double Schubert polynomial by a factorial Schur polynomial that has more $x$ variables. Namely, we multiply the factorial Schur polynomial $s _ { ( 2 , 1 ) } ( x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 } ; y )$ , which is equal to $\mathfrak { S } _ { [ 1 , 2 , 4 , 6 , 3 , 5 ] } ( x ; y )$ , by $\mathfrak { S } _ { [ 3 , 1 , 4 , 2 ] } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ; y )$ . Hence we set $u = [ 1 , 2 , 4 , 6 , 3 , 5 ]$ , $v = \left\lfloor 3 , 1 , 4 , 2 \right\rfloor$ . Then

$$
\mu_ {v} = [ 3, 4, 1, 2 ]
$$

$$
\mathfrak {c} (\mu_ {v}) = (2, 2)
$$

$$
\lambda (v) = (2, 2)
$$

$$
v ^ {- 1} \mu_ {v} = [ 1, 3, 2 ]
$$

We write $w$ on top of the diagram to save space.

<table><tr><td colspan="3">[3,1,4,6,2,5]</td><td colspan="3">[3,1,5,6,2,4]</td><td colspan="3">[3,1,6,4,2,5]</td><td colspan="3">[3,2,4,6,1,5]</td><td colspan="3">[4,1,6,2,3,5]</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>4</td></tr><tr><td>2</td><td>4</td><td>④</td><td>2</td><td>4</td><td>5</td><td>2</td><td>4</td><td>6</td><td>2</td><td>3</td><td>4</td><td>2</td><td>4</td><td>6</td></tr><tr><td>4</td><td>1</td><td>1</td><td>4</td><td>1</td><td>1</td><td>4</td><td>1</td><td>1</td><td>4</td><td>4</td><td>2</td><td>4</td><td>1</td><td>1</td></tr><tr><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>4</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>2</td></tr><tr><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>1</td><td>1</td><td>3</td><td>3</td><td>3</td></tr><tr><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td colspan="3">y4-y2</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr></table>

For $w = [ 3 , 1 , 4 , 6 , 2 , 5 ]$ there are two paths, but the weight of one of them is $y _ { 1 } - z _ { 1 }$ which specializes to 0. There are several other paths for other values of $w$ that specialize to 0 when we set $z = y$ which we do not include in the calculation.

Thus

$$
\begin{array}{l} s _ {(2, 1)} (x _ {1}, x _ {2}, x _ {3}, x _ {4}; y) \mathfrak {S} _ {[ 3, 1, 4, 2 ]} (x; y) = (y _ {4} - y _ {2}) \mathfrak {S} _ {[ 3, 1, 4, 6, 2, 5 ]} (x; y) + \mathfrak {S} _ {[ 3, 1, 5, 6, 2, 4 ]} (x; y) \\ + \mathfrak {S} _ {[ 3, 1, 6, 4, 2, 5 ]} (x; y) + \mathfrak {S} _ {[ 3, 2, 4, 6, 1, 5 ]} (x; y) \\ + \mathfrak {S} _ {[ 4, 1, 6, 2, 3, 5 ]} (x; y) \\ \end{array}
$$

Example 6.3. We give an example which does not involve factorial Schur functions. Set $u = [ 1 , 3 , 5 , 4 , 2 ]$ , $v = \left[ 3 , 1 , 4 , 2 \right]$ . Then

$$
\mu_ {v} = [ 3, 4, 1, 2 ]
$$

$$
\mathfrak {c} (\mu_ {v}) = (2, 2)
$$

$$
\lambda (v) = (2, 2)
$$

$$
v ^ {- 1} \mu_ {v} = [ 1, 3, 2 ]
$$

[3, 1, 5, 4, 2]

$$
\begin{array}{c c c} 1 & 3 & ③ \\ 3 & 5 & ⑤ \\ 5 & 1 & 1 \\ 4 & 4 & 4 \\ 2 & 2 & 2 \end{array}
$$

$$
(y _ {3} - y _ {2}) (y _ {5} - y _ {2})
$$

[3, 2, 5, 4, 1]

$$
\begin{array}{c c c} 1 & 2 & 3 \\ 3 & \underline {{\textcircled {3}}} & 5 \\ 5 & 1 & 1 \\ 4 & 4 & 4 \\ 2 & 2 & 2 \end{array}
$$

$$
y _ {3} - y _ {1}
$$

[3, 2, 5, 4, 1]

$$
\begin{array}{c c c} 1 & 2 & 3 \\ 3 & 5 & ⑤ \\ 5 & 3 & 2 \\ 4 & 4 & 4 \\ 2 & 1 & 1 \end{array}
$$

$$
y _ {5} - y _ {2}
$$

$$
\left(y _ {3} - y _ {2}\right) \left(y _ {5} - y _ {2}\right) \mathfrak {S} _ {[ 3, 1, 5, 4, 2 ]} (x; y) + \left(\left(y _ {3} - y _ {1}\right) + \left(y _ {5} - y _ {2}\right)\right) \mathfrak {S} _ {[ 3, 2, 5, 4, 1 ]} (x; y)
$$

[3, 4, 5, 1, 2]

$$
\begin{array}{c c c} 1 & 3 & \text {\textcircled {3}} \\ 3 & 4 & 5 \\ 5 & 5 & 4 \\ 4 & 1 & 1 \\ 2 & 2 & 2 \end{array}
$$

$$
y _ {3} - y _ {2}
$$

[4, 1, 5, 3, 2]

$$
\begin{array}{c c c} 1 & 3 & 4 \\ 3 & 5 & \textcircled {5} \\ 5 & 1 & 1 \\ 4 & 4 & 3 \\ 2 & 2 & 2 \end{array}
$$

$$
y _ {5} - y _ {2}
$$

[3, 1, 6, 4, 2, 5]

$$
\begin{array}{c c c} 1 & 3 & \text {\textcircled {3}} \\ 3 & 5 & 6 \\ 5 & 1 & 1 \\ 4 & 4 & 4 \end{array}
$$

$$
\begin{array}{c c c} 2 & 2 & 2 \\ 6 & 6 & 5 \end{array}
$$

$$
y _ {3} - y _ {2}
$$

$$
\left(y _ {3} - y _ {2}\right) \mathfrak {S} _ {[ 3, 4, 5, 1, 2 ]} (x; y) + \left(y _ {5} - y _ {2}\right) \mathfrak {S} _ {[ 4, 1, 5, 3, 2 ]} (x; y) + \left(y _ {3} - y _ {2}\right) \mathfrak {S} _ {[ 3, 1, 6, 4, 2, 5 ]} (x; y)
$$

[3, 4, 5, 2, 1]

$$
\begin{array}{c c c} 1 & 2 & 3 \\ 3 & 4 & 5 \\ 5 & 5 & 4 \\ 4 & 3 & 2 \\ 2 & 1 & 1 \end{array}
$$

1

[4, 2, 5, 3, 1]

$$
\begin{array}{c c c} 1 & 2 & 4 \\ 3 & 4 & 5 \\ 5 & 5 & 2 \\ 4 & 3 & 3 \\ 2 & 1 & 1 \end{array}
$$

1

[4, 3, 5, 1, 2]

$$
\begin{array}{c c c} 1 & 3 & 4 \\ 3 & 4 & 5 \\ 5 & 5 & 3 \\ 4 & 1 & 1 \\ 2 & 2 & 2 \end{array}
$$

1

$$
\mathfrak {S} _ {[ 3, 4, 5, 2, 1 ]} (x; y) + \mathfrak {S} _ {[ 4, 2, 5, 3, 1 ]} (x; y) + \mathfrak {S} _ {[ 4, 3, 5, 1, 2 ]} (x; y)
$$

$$
\begin{array}{c c c} 1 & 2 & 3 \\ 3 & 5 & 6 \\ 5 & 3 & 2 \\ 4 & 4 & 4 \\ 2 & 1 & 1 \\ 6 & 6 & 5 \end{array}
$$

$$
\begin{array}{c c c} 1 & 3 & 4 \\ 3 & 5 & 6 \\ 5 & 1 & 1 \\ 4 & 4 & 3 \\ 2 & 2 & 2 \\ 6 & 6 & 5 \end{array}
$$

1

$$
\mathfrak {S} _ {[ 3, 2, 6, 4, 1, 5 ]} (x; y) + \mathfrak {S} _ {[ 4, 1, 6, 3, 2, 5 ]} (x; y)
$$

# 7. The Pieri formula

Definition 7.1. Suppose $A$ is a finite set of positive integers, and suppose the distinct elements of $A$ are $a _ { 1 } , \ldots , a _ { m }$ in increasing order. If $P ( y ; z )$ is a polynomial in $y$ and $z$ , we write $P ( y _ { A } ; z )$ to mean

$$
P \left(y _ {a _ {1}}, y _ {a _ {2}}, \dots , y _ {a _ {m}}; z\right)
$$

The case where $m$ is smaller than the actual number of $y$ variables occurring in $P ( y ; z )$ will not happen in the exposition, and as such we do not define the notation in this case.

Theorem 7.1 (The Pieri formula). Let $u \in S _ { \infty }$ and $p \leq k$ . Then

$$
\mathfrak{S}_{u}(x;y)E_{p,k}(x;z) = \sum_{\substack{u\overset {k}{\underset{w} {\to}}}}E_{p - \ell (u,w),k - \ell (u,w)}(y_{P_{k}(u,w)};z)\mathfrak{S}_{w}(x;y)
$$

Example 7.1. Let $u = [ 4 , 3 , 5 , 1 , 2 ]$ , let $p = 3$ , and let $k = 4$ . Then

$$
\begin{array}{l} \mathfrak {S} _ {u} (x; y) E _ {p, k} (x; z) = E _ {3, 4} \left(y _ {1}, y _ {3}, y _ {4}, y _ {5}; z\right) \mathfrak {S} _ {[ 4, 3, 5, 1, 2 ]} (x; y) \\ + E _ {2, 3} \left(y _ {3}, y _ {4}, y _ {5}; z\right) \mathfrak {S} _ {[ 4, 3, 5, 2, 1 ]} (x; y) \\ + E _ {2, 3} \left(y _ {1}, y _ {3}, y _ {4}; z\right) \mathfrak {S} _ {[ 4, 3, 6, 1, 2, 5 ]} (x; y) \\ + E _ {1, 2} \left(y _ {3}, y _ {4}; z\right) \mathfrak {S} _ {[ 4, 3, 6, 2, 1, 5 ]} (x; y) \\ + E _ {1, 2} \left(y _ {1}, y _ {4}; z\right) \mathfrak {S} _ {[ 4, 5, 6, 1, 2, 3 ]} (x; y) \\ + E _ {1, 2} \left(y _ {1}, y _ {3}; z\right) \mathfrak {S} _ {[ 5, 3, 6, 1, 2, 4 ]} (x; y) \\ + \mathfrak {S} _ {[ 4, 5, 6, 2, 1, 3 ]} (x; y) + \mathfrak {S} _ {[ 5, 3, 6, 2, 1, 4 ]} (x; y) + \mathfrak {S} _ {[ 5, 4, 6, 1, 2, 3 ]} (x; y) \\ \end{array}
$$

The Pieri formula will be derived from Proposition 4.4, the proof of which will require extensive setup. First, we give a formula for multiplication by $x _ { i } - z _ { j }$ for general $i , j$ .

Lemma 7.2. Let $u \in S _ { \infty }$ and let $i , j \geq 1$ . Then

$$
(x_{i} - z_{j})\mathfrak{S}_{u}(x;y) = (y_{u(i)} - z_{j})\mathfrak{S}_{u}(x;y) + \sum_{\substack{q\neq i\\ \ell (ut_{iq}) = \ell (u) + 1}}\operatorname {sign}(q - i)\mathfrak{S}_{ut_{iq}}(x;y)
$$

Proof. It can be shown by the recurrence relation for $\partial _ { u } ^ { w }$ that $\partial _ { u } ^ { u } = u$ . Thus we have

$$
\partial_ {u} ^ {u} \left(x _ {i} - z _ {j}\right) = x _ {u (i)} - z _ {j}
$$

Substituting $y$ for $x$ , we obtain that the coefficient of $\mathfrak { S } _ { u } ( x ; y )$ is $y _ { u ( i ) } - z _ { j }$

To compute the constant coefficients we use the equivariant Chevalley formula

$$
\mathfrak{S}_{u}(x;y)\mathfrak{S}_{s_{i}}(x;y) = (\mathfrak{S}_{s_{i}}(u(x);y))|_{x = y}\mathfrak{S}_{u}(x;y) + \sum_{\substack{i\\ u\overset {i}{\to}u^{\prime}\\ \ell (u^{\prime}) = \ell (u) + 1}}\mathfrak{S}_{u^{\prime}}(x;y)
$$

We have that

$$
x _ {i} - z _ {j} = \mathfrak {S} _ {s i} (x; y) - \mathfrak {S} _ {s i - 1} (x; y) + y _ {i} - z _ {j}
$$

with the negative term ${ \mathfrak { S } } _ { s _ { i - 1 } } ( x ; y )$ excluded if $i = 1$ . Thus the terms occurring with constant coefficients in the expansion of $( x _ { i } - z _ { j } ) \mathfrak { S } _ { u } ( x ; y )$ are

$$
\sum_{\substack{u\overset {i}{\longrightarrow}u^{\prime}\\ \ell (u,u^{\prime}) = 1}}\mathfrak{S}_{u^{\prime}}(x;y) - \sum_{\substack{u\overset {i - 1}{\longrightarrow}u^{\prime \prime}\\ \ell (u,u^{\prime \prime}) = 1}}\mathfrak{S}_{u^{\prime \prime}}(x;y)
$$

The overlap in the two sums is when $u ^ { \prime } = u ^ { \prime \prime } = u t _ { q k }$ where $i \not \in \{ q , k \}$ , which cancel, and what remains is the negative terms $u t _ { q i }$ where $q < i$ and the positive terms $u t _ { i q }$ where $q > i$ . Therefore,

$$
\partial_ {u} ^ {u t _ {q k}} \left(x _ {i} - z _ {j}\right) = 0
$$

if $i \not \in \{ q , k \}$ , and if $q \neq i$ then

$$
\partial_ {u} ^ {u t _ {i q}} \left(x _ {i} - z _ {j}\right) = \operatorname {s i g n} (q - i)
$$

The result follows.



Definition 7.2 (Cycles, cycle length, disjoint cycles). Recall that a cycle or cyclic permutation is a permutation $c$ written with alternative notation (not window notation) as $c = ( a _ { 1 } , \ldots , a _ { m } ) $ for positive integers $a _ { i }$ such that $a _ { i } \neq a _ { j }$ if $i \neq j$ characterized by the fact that $c ( a _ { i } ) = a _ { i + 1 }$ for all $1 \leq i \leq m$ , with the index wrapping around so that $u _ { m + 1 } = u _ { 1 }$ , and $c ( j ) = j$ if $j \not \in \{ a _ { 1 } , \ldots , a _ { m } \}$ . Cycles $c$ have a cycle length which is equal to the value $m$ , most often distinct from their length $\ell ( c )$ as a permutation. A cycle of cycle length $m$ is called an $m$ -cycle. Note that ${ t _ { a b } = ( a , b ) }$ is a 2-cycle. We refer to the “elements” of the cycle $c$ as the integers $a _ { i }$ and say that c contains $a _ { i }$ as though it were a set.

For an $m$ -cycle $( a _ { 1 } , \ldots , a _ { m } )$ with $m > 2$ we have for any $1 < j < m$ that

$$
(a _ {1}, \dots , a _ {m}) = (a _ {1}, \dots , a _ {j}) (a _ {j}, \dots , a _ {m})
$$

and we also have that

$$
\left(a _ {1}, \dots , a _ {m}\right) = \left(a _ {m}, a _ {1}, \dots , a _ {m - 1}\right)
$$

hence the cycle is unchanged by cyclic permutation of the indices in its representation in this form. Two cycles $c _ { 1 } = ( a _ { 1 } , \ldots , a _ { p } )$ and $c _ { 2 } = ( b _ { 1 } , \ldots , b _ { q } )$ are said to be disjoint if $a _ { i } \neq b _ { j }$ for all $i , j$ . It is a basic fact proved in an undergraduate abstract algebra course that every permutation has a unique decomposition as a product of pairwise disjoint cycles (up to commutation).

We present here in Lemma 7.3 an alternative characterization of the Pieri relation $\xrightarrow { k }$ in terms of cycles that is used as the definition in [25]. Satisfaction of these conditions is usually easier to check than Definition 2.5 since it is a characterization in terms of the unique disjoint cycle decomposition of $u ^ { - 1 } w$ . We note, and leave the proof to the reader, that in the Pieri relation $u \stackrel { k } {  } w$ if we have a sequence of reflections $t _ { a _ { 1 } b _ { 1 } } , \ldots$ , $t _ { a _ { p } b _ { p } }$ realizing this then we may assume by rearranging the reflections that $b _ { i } \leq b _ { j }$ whenever $i \leq j$ .

Lemma 7.3. Suppose $u , w \in S _ { \infty }$ and let $k > 0$ be an integer. Then $u \stackrel { k } {  } w$ if and only if there exist pairwise disjoint cyclic permutations $c _ { 1 } , \ldots , c _ { n }$ of respective cycle lengths $p _ { 1 } + 1 , \dotsc , p _ { n } + 1$ such that

$$
w = u c _ {1} \dots c _ {n}
$$

and

$$
\ell (u, w) = p _ {1} + \dots + p _ {n}
$$

such that for each i there exist pairwise distinct positive integers $a _ { 1 } , \ldots , a _ { p _ { i } }$ and b (different for each i) such that we may write the cycle $c _ { i }$ as

$$
c _ {i} = \left(a _ {p _ {i}}, a _ {p _ {i} - 1}, \dots , a _ {1}, b\right)
$$

where $a _ { j } \leq k$ for all $1 \le j \le p _ { i }$ , $b > k$ , and

$$
u \left(a _ {p _ {i}}\right) <   \dots <   u \left(a _ {1}\right) <   u (b)
$$

Proof. Suppose first that $u \stackrel { k } {  } w$ . Then there exist reflections ${ t _ { a _ { 1 } b _ { 1 } } , \ldots , t _ { a _ { m } b _ { m } } }$ for some $m$ with $a _ { i } \neq a _ { j }$ if $i \neq j$ , $a _ { i } \leq k < b _ { i }$ for all $i$ , $\ell ( u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { i } b _ { i } } ) = \ell ( u ) + i$ for all $_ i$ , $b _ { i } \leq b _ { j }$ if $i \leq j$ , and $w = u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { m } b _ { m } } .$ . Fix $b$ such that there is an index $1 \leq q \leq m$ such that $b = b _ { q }$ and let $i$ and $p$ be such that $a _ { i } , \ldots , a _ { i + p }$ is the maximal portion of the sequence such that $b _ { j } = b$ for all $i \leq j \leq i + p$ . Let

$$
c = t _ {a _ {i} b _ {i}} \dots t _ {a _ {i + p} b _ {i + p}}
$$

Given $j$ with $i \leq j \leq i + p$ we claim that if we define a permutation $c ^ { ( j ) }$ with

$$
c ^ {(j)} = t _ {a _ {i} b} \dots t _ {a _ {j} b}
$$

then

$$
c ^ {(j)} = \left(a _ {j}, a _ {j - 1}, \dots , a _ {i}, b\right)
$$

and that

$$
u (a _ {j}) <   \dots <   u (a _ {i}) <   u (b)
$$

This is clear if $j = i$ . Otherwise, suppose

$$
c ^ {(j - 1)} = t _ {a _ {i} b} \dots t _ {a _ {j - 1} b} = (a _ {j - 1}, \dots , a _ {i}, b)
$$

Then

$$
c ^ {(j - 1)} t _ {a _ {j} b} = (a _ {j - 1}, \ldots , a _ {i}, b) (b, a _ {j}) = (a _ {j - 1}, \ldots , a _ {i}, b, a _ {j}) = (a _ {j}, \ldots , a _ {i}, b)
$$

as desired. We have that

$$
u (a _ {j}) = u c ^ {(j - 1)} (a _ {j}) <   u c ^ {(j - 1)} (b) = u (a _ {j - 1})
$$

and hence the desired claim follows by induction. Hence,

$$
c = c ^ {(i + p)} = (a _ {i + p}, \dots , a _ {i}, b)
$$

and

$$
u \left(a _ {i + p}\right) <   \dots <   u \left(a _ {i}\right) <   u (b)
$$

Ranging over all $b$ , these cycles, which we index in order of increasing $b$ as $c _ { 1 } , \ldots , c _ { n }$ , are the ones that occur in the disjoint cycle decomposition of $u ^ { - 1 } w$ , which we can see by the fact that the cycles are pairwise disjoint and $w = u c _ { 1 } \ldots c _ { n }$ . Letting $p _ { i } + 1$ be the cycle length of each cycle $c _ { i }$ , we have that there are $p _ { 1 } + \cdot \cdot \cdot + p _ { n } = m$ reflections, and hence

$$
\ell \left(u c _ {1} \dots c _ {n}\right) = \ell (u) + p _ {1} + \dots + p _ {n}
$$

and we have the result.

We prove the converse now. Suppose the cycles $c _ { 1 } , \ldots , c _ { n }$ of cycle length $p _ { i } + 1$ for each $i$ exist satisfying the conditions, fixing $k$ . Write $c _ { 1 }$ as

$$
c _ {1} = \left(a _ {p _ {1}}, \dots , a _ {1}, b\right)
$$

with $u ( a _ { p 1 } ) < \cdot \cdot \cdot < u ( a _ { 1 } ) < u ( b )$ . Then

$$
c _ {1} = t _ {a _ {1} b} \dots t _ {a _ {p _ {1}} b}
$$

We claim that $\ell ( u t _ { a _ { 1 } b } \cdot \cdot \cdot t _ { a _ { i } b } ) > \ell ( u t _ { a _ { 1 } b } \cdot \cdot \cdot t _ { a _ { i - 1 } b } )$ for all $i$ (not yet claiming that the length increases by exactly 1). We prove this by induction on $i$ . For $i = 1$ , we note that $u ( a _ { 1 } ) < u ( b )$ by assumption, hence $\ell ( u t _ { a _ { 1 } b } ) > \ell ( u )$ . Assume now that the result holds for $i - 1$ . Then

$$
u t _ {a _ {1} b} \dots t _ {a _ {i - 1} b} (b) = u (a _ {i - 1}) > u (a _ {i}) = u t _ {a _ {1} b} \dots t _ {a _ {i - 1} b} (a _ {i})
$$

since $a _ { j } \neq a _ { i }$ if $j \neq i$ . Thus multiplying on the right by $t _ { a _ { i } b }$ increases the length by at least 1. Applying this argument for each disjoint cycle $c _ { i }$ to $\ell ( u c _ { 1 } \cdots c _ { i } )$ and expanding the cycles into reflections, we obtain that successively multiplying on the right by each reflection increases the length by at least 1 per reflection. Since there are $p _ { 1 } + \cdots + p _ { n }$ reflections and this is equal to $\ell ( u , w )$ , each reflection must increase the length by exactly 1 and we have the result. 

Note that it is not sufficient in Lemma 7.3 to require only that $\ell ( u c _ { i } ) = \ell ( u ) + p _ { i }$ for all $i$ , as it could occur that, for example in the case of two cycles, $\ell ( u c _ { 1 } ) = \ell ( u ) + p _ { 1 }$ and $\ell ( u c _ { 2 } ) = \ell ( u ) + p _ { 2 }$ but $\ell ( u c _ { 1 } c _ { 2 } ) \neq$ $\ell ( u ) + p _ { 1 } + p _ { 2 }$ . This can even happen if $p _ { 1 } = p _ { 2 } = 1$ , so that the cycles are reflections.

Lemma 7.4. Let $u , w \in S _ { \infty }$ , let $k > 0$ be an integer, and suppose $u \stackrel { k } {  } w$ . Then $u ( i ) \leq w ( i )$ for all $i \leq k$ , and $u ( i ) \geq w ( i )$ for all $i > k$ .

Proof. Let $t _ { a _ { 1 } b _ { 1 } } , \ldots , t _ { a _ { p } b _ { p } }$ be a sequence of reflections realizing $u \stackrel { k } {  } w$ , with $a _ { i } \leq k < b _ { i }$ for all $i$ and $a _ { i } \neq a _ { j }$ if $i \neq j$ , by which we mean $\ell ( u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { i } b _ { i } } ) = \ell ( u ) + i$ for all $i$ and $w = u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { p } b _ { p } }$ . We prove the statement by induction on $p$ . If $p = 0$ , then $u ( i ) = w ( i )$ for all $i$ , so the result is clear. Otherwise, suppose the result holds for some $p \geq 0$ ; we show the result holds for $p + 1$ , considering a reflection $t _ { a _ { p + 1 } b _ { p + 1 } }$ such that $a _ { p + 1 } \leq k < b _ { p + 1 }$ and $\ell ( w t _ { a _ { p + 1 } b _ { p + 1 } } ) = \ell ( w ) + 1$ , with $a _ { i } \neq a _ { p + 1 }$ for all $1 \leq i \leq p$ . By the induction hypothesis, $u ( i ) \leq w ( i )$ for all $i \leq k$ , and $u ( i ) \geq w ( i )$ for all $i > k$ . The only two positions that $w t _ { a _ { p + 1 } b _ { p + 1 } }$ and $w$ differ are $a _ { p + 1 }$ and $b _ { p + 1 }$ . Since $\ell ( w t _ { a _ { p + 1 } b _ { p + 1 } } ) = \ell ( w ) + 1$ , we have that $w ( a _ { p + 1 } ) < w ( b _ { p + 1 } )$ , hence

$$
u \left(a _ {p + 1}\right) \leq w \left(a _ {p + 1}\right) <   w \left(b _ {p + 1}\right) = w t _ {a _ {p + 1} b _ {p + 1}} \left(a _ {p + 1}\right)
$$

Similarly,

$$
u \left(b _ {p + 1}\right) \geq w \left(b _ {p + 1}\right) > w \left(a _ {p + 1}\right) = w t _ {a _ {p + 1} b _ {p + 1}} \left(b _ {p + 1}\right)
$$

The result follows by induction.

The following is easy to see, but we will be required to refer back to it and hence we state it as a lemma.

Lemma 7.5. Suppose $u , w \in S _ { \infty }$ , $k > 0$ is an integer, and suppose $u \stackrel { k } {  } w$ . Then

$$
\left| P _ {k} (u, w) \right| = k - \ell (u, w)
$$

Proof. Let $p = \ell ( u , w )$ . Then there are reflections ${ t _ { a _ { 1 } b _ { 1 } } , \ldots , t _ { a _ { p } b _ { p } } }$ such that $a _ { i } \leq k < b _ { i }$ for all $_ i$

$$
\ell \left(u t _ {a _ {1} b _ {1}} \dots t _ {a _ {i} b _ {i}}\right) = \ell (u) + i
$$

for all $i$ , and $w = u t _ { a _ { 1 } b _ { 1 } } \cdot \cdot \cdot t _ { a _ { p } b _ { p } }$ , with $a _ { i } \neq a _ { j }$ whenever $i \neq j$ . By this last condition, the number of indices $i \leq k$ such that $u ( i ) \neq w ( i )$ is exactly $p$ ; specifically, these indices are the values $a _ { j }$ . Thus $u ( i ) = w ( i )$ for exactly $k - p = k - \ell ( u , w )$ values of $_ i$ such that $i \leq k$ . 

Parts of the statements of the below lemmas are presented in [25] (the results are stated for multiplying $w$ by a reflection instead of $u$ , which is equivalent via applying our lemmas to the interval $[ w _ { 0 } ( n ) w , w _ { 0 } ( n ) u ] )$ , but we will include proofs here in order to be complete. The purpose of the lemmas is to determine which terms remain and which terms cancel in an expansion of the Pieri product in the proof of Proposition 4.4.

Lemma 7.6. Suppose $u , w \in S _ { \infty }$ and let $k > 1$ be an integer. If $u \stackrel { k } {  } w$ but $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ , then there is a unique $q ^ { \prime } > k$ such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . Furthermore, in that case there does not exist a $q < k$ such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ .

Proof. Suppose $u \stackrel { k } {  } w$ but $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ . Let $c _ { 1 } , \ldots , c _ { n }$ be the pairwise disjoint cycles in the decomposition of $u ^ { - 1 } w$ , with the cycle length of $c _ { i }$ being $p _ { i } + 1$ . Some such cycle must contain $k$ , as otherwise we would have $u \xrightarrow { k - 1 } w$ by Lemma 7.3. Assume that $\boldsymbol { c } _ { 1 } = ( a _ { p _ { 1 } } , \ldots , a _ { 1 } , b )$ is the cycle that contains $k$ and set $q ^ { \prime } = b$ . We claim that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ and $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ . Note that $u = ( u t _ { k q ^ { \prime } } ) t _ { k q ^ { \prime } }$ and hence

$$
\left(u t _ {k q ^ {\prime}}\right) t _ {k q ^ {\prime}} c _ {1} \dots c _ {n} = w
$$

Let $j$ be the index such that $a _ { j } = k$ . Then we have

$$
\begin{array}{l} t _ {k q ^ {\prime}} \left(a _ {p _ {1}}, \dots , a _ {j + 1}, k, a _ {j - 1}, \dots , a _ {1}, q ^ {\prime}\right) = t _ {k q ^ {\prime}} \left(q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}, k, a _ {j - 1}, \dots , a _ {1}\right) \\ = t _ {k q ^ {\prime}} \left(q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}, k\right) \left(k, a _ {j - 1}, \dots , a _ {1}\right) \\ = t _ {k q ^ {\prime}} (k, q ^ {\prime}) \left(a _ {p _ {1}}, \dots , a _ {j + 1}, q ^ {\prime}\right) \left(a _ {j - 1}, \dots , a _ {1}, k\right) \\ = \left(a _ {p _ {1}}, \dots , a _ {j + 1}, q ^ {\prime}\right) \left(a _ {j - 1}, \dots , a _ {1}, k\right) \\ \end{array}
$$

Note that $u t _ { k q ^ { \prime } } ( k ) = u ( q ^ { \prime } )$ , $u t _ { k q ^ { \prime } } ( q ^ { \prime } ) = u ( k )$ , and otherwise $u t _ { k q ^ { \prime } } ( a ) = u ( a )$ for all $a \not \in \{ k , q ^ { \prime } \}$ . Thus,

$$
u t _ {k q ^ {\prime}} \left(a _ {p _ {1}}\right) <   \dots <   u t _ {k q ^ {\prime}} \left(a _ {j + 1}\right)
$$

since the same is true for $u$ , and

$$
u t _ {k q ^ {\prime}} \left(a _ {j + 1}\right) = u \left(a _ {j + 1}\right) <   u (k) = u t _ {k q ^ {\prime}} \left(q ^ {\prime}\right)
$$

hence the first cycle is valid for $\xrightarrow { k - 1 }$ . Furthermore, if $j > 1$ then

$$
u t _ {k q ^ {\prime}} \left(a _ {j - 1}\right) <   \dots <   u t _ {k q ^ {\prime}} \left(a _ {1}\right)
$$

for the same reason, and

$$
u t _ {k q ^ {\prime}} (a _ {1}) = u (a _ {1}) <   u (q ^ {\prime}) = u t _ {k q ^ {\prime}} (k)
$$

hence the second cycle is valid for $\xrightarrow { k - 1 }$ as well, whereas if $j = 1$ then there is no second cycle. Since the (up to) two new cycles together with $c _ { 2 } , \ldots , c _ { n }$ are all pairwise disjoint and $\ell ( u t _ { k q ^ { \prime } } , w ) = \ell ( u , w ) - 1$ , the cycle lengths sum up correctly and we have that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ by Lemma 7.3, as desired.

To show that the $q ^ { \prime }$ we have chosen is unique, let $r > k$ be any index other than $q ^ { \prime }$ such that $\ell ( u t _ { k r } ) =$ $\ell ( u ) + 1$ . Suppose first that $r$ is not in any of the cycles $c _ { i }$ . Recall that $c _ { 1 }$ is the cycle that contains $k$ . Then $t _ { k r } c _ { 1 }$ is a cycle in the disjoint cycle decomposition of $( u t _ { k r } ) ^ { - 1 } w$ containing both $k$ and $r$ , which are both larger than $k - 1$ . This violates the condition of Lemma 7.3 that in order for $u t _ { k r } \ \xrightarrow { k - 1 } w$ we must have that each cycle contains exactly one element larger than $k - 1$ , hence we have $u t _ { k r } \ \xrightarrow { k - 1 } w$ . If $r$ is in one of the cycles, since $r > k$ and $r \neq q ^ { \prime }$ this cycle cannot be $c _ { 1 }$ . Say the cycle containing $r$ is $c _ { 2 } = ( a _ { p _ { 2 } } ^ { \prime } , \ldots , a _ { 1 } ^ { \prime } , r )$ . Then

$$
\begin{array}{l} t _ {k r} c _ {1} c _ {2} = t _ {k r} \left(r, a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}\right) \left(a _ {p _ {1}}, \dots , a _ {1}, q ^ {\prime}\right) \\ = \left(r, a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}, k\right) \left(k, a _ {j - 1}, \dots , q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}\right) \\ = \left(r, a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}, k, a _ {j - 1}, \dots , q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}\right) \\ \end{array}
$$

is a single cycle disjoint from all the others containing both $k$ and $r$ , which are both greater than $k - 1$ hence we have $u t _ { k r } \ \xrightarrow { k - 1 } w$ by Lemma 7.3. The uniqueness of $q ^ { \prime }$ follows.

To prove the nonexistence of $q$ , consider the same cycle decomposition $c _ { 1 } , \ldots , c _ { n }$ . Let $q < k$ be such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ . If $c _ { 1 }$ (the cycle that contains $k$ ) does not contain $q$ , then $t _ { q k } c _ { 1 }$ is a cycle containing both $k$ and some integer larger than $k$ . If some other cycle $c _ { 2 }$ contains $q$ , $t _ { q k } c _ { 1 } c _ { 2 }$ is disjoint from all the other cycles and contains both $k$ and some integer larger than $k$ , similarly to the calculation above. Thus if $c _ { 1 }$ does not contain $q$ then the disjoint cycle decomposition of $( u t _ { q k } ) ^ { - 1 } w$ contains the cycle $t _ { q k } c _ { 1 }$ or $t _ { q k } c _ { 1 } c _ { 2 }$ which implies that $u t _ { q k } \xrightarrow { k \mathrm { \Delta } } w$ by Lemma 7.3 since the cycle contains two elements larger than $k - 1$ . To handle the case where $c _ { 1 }$ contains $q$ , in that case $t _ { q k }$ splits $c _ { 1 }$ into two disjoint cycles as follows. Assume $c _ { 1 } = ( a _ { p 1 } , \ldots , q ^ { \prime } )$ with $a _ { j } = k$ and $a _ { j ^ { \prime } } = q$ . We must have that $j ^ { \prime } > j$ since $u ( q ) < u ( k )$ . Then

$$
\begin{array}{l} t _ {q k} c _ {1} = t _ {q k} \left(a _ {p _ {1}}, \dots , q, \dots , k, \dots , q ^ {\prime}\right) \\ = t _ {q k} (q, \dots , k, \dots , q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j ^ {\prime} + 1}) \\ = t _ {q k} \left(q, a _ {j ^ {\prime} - 1}, \dots , k\right) \left(k, \dots , q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j ^ {\prime} + 1}\right) \\ = \left(q, a _ {j ^ {\prime} - 1}, \dots , a _ {j + 1}\right) \left(a _ {p _ {1}}, \dots , a _ {j ^ {\prime} + 1}, k, \dots , q ^ {\prime}\right) \\ \end{array}
$$

The cycle $( a _ { p 1 } , \dotsc , k , \dotsc , q ^ { \prime } )$ contains two elements larger than $k - 1$ , implying that $u t _ { q k } \xrightarrow { k - 1 } w$ by Lemma 7.3, as desired.

Example 7.2. Let $\boldsymbol { u } = [ 3 , 1 , 6 , 5 , 2 , 4 ]$ , let $w = \left. 4 , 2 , 7 , 6 , 1 , 3 , 5 \right.$ , and let $k = 4$ . We have that

$$
u ^ {- 1} w = (1, 6) (2, 5) (4, 3, 7)
$$

Thus $u \stackrel { k } {  } w$ , but $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ because of the third cycle containing two elements greater than $k - 1$ . We set $q ^ { \prime } = 7$ according to the proof. Then

$$
u t _ {k q ^ {\prime}} = [ 3, 1, 6, 7, 2, 4, 5 ]
$$

Then we see the cycle splits by

$$
t _ {k q ^ {\prime}} u ^ {- 1} w = (1, 6) (2, 5) t _ {k q ^ {\prime}} (4, 3, 7) = (1, 6) (2, 5) t _ {k q ^ {\prime}} (4, 7) (3, 4) = (1, 6) (2, 5) (3, 4)
$$

and indeed we have that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ k−1−−→ w.

Lemma 7.7. Suppose $u , w \in S _ { \infty }$ and let $k > 1$ be an integer. If $u \stackrel { k } {  } w$ and $u \xrightarrow { k - 1 } w$ , then there is no $q < k$ such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ and there is no $q ^ { \prime } > k$ such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ .

Proof. Let $c _ { 1 } , \ldots , c _ { n }$ be the pairwise disjoint cycles with $c _ { i }$ a $( p _ { i } + 1 )$ -cycle in the decomposition of $u ^ { - 1 } w$ These cycles, since the disjoint cycle decomposition is unique, must realize both $u \stackrel { k } {  } w$ and $u \xrightarrow { k - 1 } w$ . Thus none of these cycles can contain $k$ ; if one of them did, it would be impossible that $u \xrightarrow { k - 1 } w$ because the cycle would have two elements larger than $k - 1$ .

We show first that element $q ^ { \prime } > k$ cannot exist. Suppose $q ^ { \prime } > k$ is such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ . If none of the cycles $c _ { i }$ contains $q ^ { \prime }$ , then $( k , q ^ { \prime } )$ is a free cycle in the disjoint cycle decomposition of $( u t _ { k q ^ { \prime } } ) ^ { - 1 } w$ . Since both elements are greater than $k - 1$ , we then cannot have that $u t _ { k q ^ { \prime } } \ \xrightarrow { k - 1 } \ w$ . If one of the cycles does contain $q ^ { \prime }$ , say $c _ { 1 }$ , then since $c _ { 1 }$ does not contain $k$ we have that $t _ { k q ^ { \prime } } c _ { 1 }$ is a $( p _ { 1 } + 2 )$ -cycle containing both $k$ and $q ^ { \prime }$ ; again, this implies that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ because both elements are greater than $k - 1$ . It follows that no $q ^ { \prime }$ exists with $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ .

Now we consider $q$ . Suppose $q < k$ is such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ . Then $u ( q ) < u ( k ) \leq w ( k )$ , the second inequality by Lemma 7.4 since $u \stackrel { k } {  } w$ . We then have that $u t _ { q k } ( k ) = u ( q ) < w ( k )$ , hence by Lemma 7.4 we cannot have that $u t _ { q k } \xrightarrow { k - 1 } w$ since this would require that $u t _ { q k } ( k ) \geq w ( k )$ . The result follows. 

Lemma 7.8. Suppose $u , w \in S _ { \infty }$ and let $k > 1$ be an integer. If $u \xrightarrow { k - 1 } w$ and $u \stackrel { k _ { \langle } } { \phi } w$ , then there is a unique $q < k$ such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ . When this is the case, then $P _ { k - 1 } ( u t _ { q k } , w ) =$ $P _ { k - 1 } ( u , w ) \cup \{ u ( k ) \}$ , and for any $q ^ { \prime } > k$ such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ we have that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ .

Proof. Let ${ t _ { a _ { 1 } b _ { 1 } } , \ldots , t _ { a _ { p } b _ { p } } }$ be a sequence of reflections realizing $u \xrightarrow { k - 1 } w$ k−1−−→ w, and assume bi ≤ bj whenever i ≤ j. $b _ { i } \leq b _ { j }$ $i \leq j$ Since $u \stackrel { k _ { \langle } } {  } w$ , we must have that $b _ { i } = k$ for some $i$ . Let $i$ be minimal with this property and set $q = a _ { i }$ . Then $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ . Let $c _ { 1 } , \ldots , c _ { n }$ be the pairwise disjoint cycles in the decomposition of $u ^ { - 1 } w$ with $c _ { i }$ having cycle length $p _ { i } + 1$ , and suppose the cycle with $q$ is $c _ { 1 }$ . $c _ { 1 }$ then also must contain $b _ { i } = k$ . We then have that $t _ { q k } c _ { 1 }$ is the $p _ { 1 }$ -cycle we obtain by deleting $q$ . We can see this by writing $c _ { 1 } = ( a _ { p 1 } ^ { \prime } , \ldots , q , k )$ , then cyclically permuting to obtain $( q , k , a _ { p _ { 1 } } ^ { \prime } , \ldots , a _ { 2 } ^ { \prime } ) = ( q , k ) ( a _ { p _ { 1 } } ^ { \prime } , \ldots , a _ { 2 } ^ { \prime } , k )$ , and multiplying this on the left by $t _ { q k }$ cancels the $( q , k )$ . We have that $u t _ { q k } ( k ) = u ( q )$ , hence

$$
u t _ {k q} \left(a _ {p _ {1}} ^ {\prime}\right) <   \dots <   u t _ {k q} \left(a _ {2} ^ {\prime}\right) <   u t _ {q k} (k)
$$

hence $u t _ { q k } \xrightarrow { k - 1 } w$ k−1−−→ w.

To show uniqueness of $q$ , let $r < k$ be such that $r \neq q$ and $\ell ( u t _ { r k } ) = \ell ( u ) + 1$ , and let the cycle $c _ { 1 }$ be as in the previous paragraph. If $r$ is not in any of the cycles, then $t _ { r k } c _ { 1 }$ has cycle length $p _ { 1 } + 2$ , hence the length condition is not satisfied in Lemma 7.3, implying that $u t _ { r k } \xrightarrow { k \mathrm { - } 1 } w$ . A similar length argument applies when $r$ is in a cycle other than $c _ { 1 }$ , say $c _ { 2 }$ , with $t _ { r k } c _ { 1 } c _ { 2 }$ being a single cycle that is too long. Suppose instead that $r$ is in $c _ { 1 }$ , say $a _ { j } ^ { \prime } = r$ with $j \geq 2$ . Write

$$
c _ {1} = (k, a _ {p _ {1}} ^ {\prime}, \ldots , a _ {j + 1} ^ {\prime}, a _ {j} ^ {\prime}) (a _ {j} ^ {\prime}, a _ {j - 1} ^ {\prime}, \ldots , a _ {2} ^ {\prime}, q) = (a _ {j} ^ {\prime}, k) (k, a _ {p _ {1}} ^ {\prime}, \ldots , a _ {j + 1} ^ {\prime}) (a _ {j} ^ {\prime}, a _ {j - 1} ^ {\prime}, \ldots , a _ {2} ^ {\prime}, q)
$$

The $( a _ { j } ^ { \prime } , k ) = ( r , k )$ cancels in $t _ { r k } c _ { 1 }$ and we obtain two cycles, one of which is nontrivial (because it contains both $r$ and $q$ ) and contains only elements less than or equal to $k - 1$ , contradicting $u t _ { r k } \xrightarrow { k - 1 } w$ . Uniqueness of $q$ follows.

Now we prove that $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u , w ) \cup \{ u ( k ) \}$ . Note that $u ( i ) = u t _ { q k } ( i )$ if $i < k$ and $i \neq q$ . Thus, if $u ( i ) \in P _ { k - 1 } ( u , w )$ and $i \neq q$ , then $u ( i ) \in P _ { k - 1 } ( u t _ { q k } , w )$ . Since $P _ { k - 1 } ( u t _ { q k } , w )$ must have exactly one more element than $P _ { k - 1 } ( u , w )$ by Lemma 7.5, this element must occur at index $q$ . Thus $u t _ { q k } ( q ) = w ( q ) = u ( k )$ , hence the claim follows.

Suppose finally that $q ^ { \prime } > k$ is such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ ; we show that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . This is due to the fact that, again assuming $c _ { 1 }$ contains $k$ , $t _ { k q ^ { \prime } } c _ { 1 }$ contains both $k$ and $q ^ { \prime }$ . If in addition there is a cycle $c _ { 2 }$ containing $q ^ { \prime }$ , then $t _ { k q ^ { \prime } } c _ { 1 } c _ { 2 }$ is again a single cycle containing both $k$ and $q ^ { \prime }$ . In either case, since both $k$ and $q ^ { \prime }$ are larger than $k - 1$ , this contradicts the conditions in Lemma 7.3, implying that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . The result follows. 

Example 7.3. Let $u = [ 3 , 1 , 6 , 5 , 2 , 4 ]$ , let $w = [ 5 , 3 , 6 , 1 , 2 , 4 ]$ , and let $k = 4$ . We have that

$$
u ^ {- 1} w = (2, 1, 4)
$$

Then $u \xrightarrow { k - 1 } w$ because $u ( 2 ) < u ( 1 ) < u ( 4 )$ , but $u \stackrel { k _ { \langle } } { \phi } w$ because there is no element greater than 4 in the cycle. We also have

$$
u t _ {1, 4} t _ {2, 4} = w
$$

Thus we choose $q = 1$ , since this is the first index such that the higher index is $k$ . Then

$$
u t _ {q k} = [ 5, 1, 6, 3, 2, 4 ]
$$

and

$$
t _ {q k} (2, 1, 4) = (1, 4) (1, 4) (2, 4) = (2, 4)
$$

Hence $u t _ { q k } \xrightarrow { k - 1 } w$ . We have that $P _ { k - 1 } ( u , w ) = \{ 6 \}$ , and $P _ { k - 1 } ( u t _ { q k } , w ) = \{ 5 , 6 \} = P _ { k - 1 } ( u , w ) \cup \{ u ( k ) \} .$

Lemma 7.9. Suppose $u , w \in S _ { \infty }$ and let $k > 1$ be an integer. Suppose also that $u \stackrel { k _ { \langle } } { \phi } w$ and $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ . Then there exists a $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ $q ^ { \prime } > k$ and such that $u t _ { q k } \xrightarrow { k - 1 } w$ $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ . If either exists, then each is unique, and and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ if and only if there exists a $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ $q < k$ such that

Proof. Let $q ^ { \prime } > k$ be such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \ \xrightarrow { k - 1 } w$ . Suppose also that $u \stackrel { k _ { \langle } } { \phi } w$ . We find a $q < k$ with $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ k−1−−→ w and afterwards show that q′ is unique. Let c1, . . . , cn be $q ^ { \prime }$ $c _ { 1 } , \ldots , c _ { n }$ the pairwise disjoint cycles in the decomposition of $( u t _ { k q ^ { \prime } } ) ^ { - 1 } w$ , with $c _ { i }$ of cycle length $p _ { i } + 1$ . We claim that there must be some such cycle that contains $k$ . If neither $k$ nor $q ^ { \prime }$ were present, then we would have that $u \stackrel { k } {  } w$ by adding this disjoint cycle $( k , q ^ { \prime } )$ to the decomposition of $( u t _ { k q ^ { \prime } } ) ^ { - 1 } w$ , which we assumed is not

the case. The same is true if $q ^ { \prime }$ is present but not $k$ . To see this, say $c _ { 2 }$ is the $( p _ { 2 } + 1 )$ -cycle containing $q ^ { \prime }$ . Then $t _ { k q ^ { \prime } } c _ { 2 }$ is a $( p _ { 2 } + 2 )$ -cycle satisfying the conditions of Lemma 7.3 for $u$ , $w$ , and $k$ (which we can see from the fact that this is a sequence of reflections of the form $t _ { a q ^ { \prime } }$ , each increasing the length by 1 and the lower indices being pairwise distinct), and we assumed that $u \stackrel { k _ { \langle } } { \phi } w$ .

In the case where $k$ is present but not $q ^ { \prime }$ , say in the cycle $c _ { 1 }$ , suppose

$$
c _ {1} = \left(a _ {p _ {1}}, \dots , a _ {1}, k\right)
$$

Then we have

$$
t _ {k q ^ {\prime}} c _ {1} = \left(q ^ {\prime}, k\right) \left(k, a _ {p _ {1}}, \dots , a _ {1}\right) = \left(q ^ {\prime}, k, a _ {p _ {1}}, \dots , a _ {1}\right) = \left(k, a _ {p _ {1}}, \dots , a _ {1}, q ^ {\prime}\right)
$$

If $u ( k ) < u ( a _ { p 1 } )$ , then $u \stackrel { k } {  } w$ , which we assumed is not the case. Therefore $u ( k ) > u ( a _ { p 1 } )$ . Choose the minimal $j$ such that $u ( a _ { j } ) < u ( k )$ , and write $t _ { k q ^ { \prime } } c _ { 1 }$ as

$$
(k, a _ {p _ {1}}, \dots , a _ {j}) (a _ {j}, \dots , q ^ {\prime}) = (a _ {j}, k) (k, a _ {p _ {1}}, \dots , a _ {j + 1}) (a _ {j}, \dots , q ^ {\prime}) = (a _ {j}, k) (a _ {p _ {1}}, \dots , a _ {j + 1}, k) (a _ {j}, \dots , q ^ {\prime})
$$

and set $q = a _ { j }$ . Then $u t _ { q k } \xrightarrow { k - 1 } w$ because $u t _ { q k } ( a _ { p _ { 1 } } ) < \dots < u t _ { q k } ( k ) = u t _ { k q ^ { \prime } } ( a _ { j } )$ , and if $j > 1$ then

$$
u t _ {q k} (a _ {j}) = u (k) <   u (a _ {j - 1}) = u t _ {q k} (a _ {j - 1}) <   \dots <   u t _ {q k} (q ^ {\prime}),
$$

whereas if $j = 1$ then $u t _ { q k } ( q ) = u ( k ) < u ( q ^ { \prime } ) = u t _ { q k } ( q ^ { \prime } )$ since $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$

Finally consider the case where both $k$ and $q ^ { \prime }$ are present. Suppose

$$
c _ {1} = \left(a _ {p _ {1}}, \dots , a _ {1}, k\right)
$$

and

$$
c _ {2} = \left(a _ {p _ {2}} ^ {\prime}, \ldots , a _ {1} ^ {\prime}, q ^ {\prime}\right)
$$

Then

$$
t _ {k q ^ {\prime}} c _ {1} c _ {2} = (k, a _ {p _ {1}}, \ldots , a _ {1}, q ^ {\prime}) (q ^ {\prime}, a _ {p _ {2}} ^ {\prime}, \ldots , a _ {1} ^ {\prime}) = (k, a _ {p _ {1}}, \ldots , a _ {1}, q ^ {\prime}, a _ {p _ {2}} ^ {\prime}, \ldots , a _ {1} ^ {\prime})
$$

Since $u \ \stackrel { k _ { \langle } } { \phi } \ w$ , we have that $u ( a _ { 1 } ^ { \prime } ) > u ( k )$ or $u ( k ) > u ( a _ { p 1 } )$ by the conditions in Lemma 7.3, and since $u ( k ) = u t _ { k q ^ { \prime } } ( q ^ { \prime } ) > u t _ { k q ^ { \prime } } ( a _ { 1 } ^ { \prime } )$ given that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ it follows that $u ( k ) > u ( a _ { p _ { 1 } } )$ . Choose the minimal $j$ such that $u ( a _ { j } ) < u ( k )$ . Then we obtain

$$
(k, a _ {p _ {1}}, \dots , a _ {j + 1}, a _ {j}) (a _ {j}, \dots , a _ {1}, q ^ {\prime}, a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}) = (a _ {j}, k) (k, a _ {p _ {1}}, \dots , a _ {j + 1}) (a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}, a _ {j}, \dots , a _ {1}, q ^ {\prime})
$$

and we may set $q = a _ { j }$ as before, since then

$$
u t _ {q k} \left(a _ {1} ^ {\prime}\right) = u t _ {k q ^ {\prime}} \left(a _ {1} ^ {\prime}\right) <   u t _ {k q ^ {\prime}} \left(q ^ {\prime}\right) = u (k) = u t _ {q k} \left(a _ {j}\right)
$$

and if $j > 1$ then

$$
u t _ {q k} (a _ {j}) = u (k) <   u t _ {k q ^ {\prime}} (a _ {j - 1}) = u t _ {q k} (a _ {j - 1})
$$

whereas if $j = 1$ then

$$
u t _ {q k} \left(a _ {1}\right) = u (k) <   u \left(q ^ {\prime}\right) = u t _ {q k} \left(q ^ {\prime}\right)
$$

since $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ , so that $u t _ { q k } \xrightarrow { k - 1 } w$ k−1−−→ w. Thus, given such a q′, we have identified an integer q < k $q ^ { \prime }$ $q < k$ such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ . To see that $q ^ { \prime }$ is unique, we note that $q ^ { \prime }$ is the unique element contained in the cycle containing $k$ in the disjoint cycle decomposition of $u ^ { - 1 } w$ that is larger than $k$ .

We show now that if $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ , then if $q < k$ is such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ then there exists a $q ^ { \prime } > k$ such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \ \xrightarrow { k - 1 } \ w$ , and we show that $q$ is unique assuming additionally that $u \stackrel { k _ { \langle } } { \phi } w$ . Let $q < k$ be such that $\ell ( u t _ { q k } ) = \ell ( u ) + 1$ and $u t _ { q k } \xrightarrow { k - 1 } w$ 1 , and assume $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ Let the pairwise disjoint cycles in the decomposition of $( u t _ { q k } ) ^ { - 1 } w$ be $c _ { 1 } , \ldots , c _ { n }$ , with $c _ { i }$ having length $p _ { i } + 1$ (note that we have redefined the cycles here, and they are not the same as the previous paragraph). If there were no cycle that contained $q$ , then we claim that we would then have that $u \xrightarrow { k - 1 } w$ , which we assumed is not the case. To see this, suppose no cycle contains $q$ and no cycle contains $k$ . Then $t _ { q k }$ is a free cycle in the decomposition of $u ^ { - 1 } w$ and its existence implies $u \xrightarrow { k - 1 } w$ by Lemma 7.3. If instead no cycle contained $q$ but some cycle contained $k$ , then say this cycle containing $k$ is $c _ { 2 }$ . Then $t _ { q k } c _ { 2 }$ can be written as a product of reflections of the form $t _ { a k }$ for pairwise distinct choices of $a$ that are less than $k$ , and we can deduce that this forms a $( p _ { 2 } + 2 )$ -cycle $t _ { q k } c _ { 2 }$ that together with $c _ { 1 } , c _ { 3 } , \ldots , c _ { n }$ imply that $u \xrightarrow { k - 1 } w$ by Lemma 7.3. Thus as claimed some cycle must contain $q$ .

Assume without loss of generality that $c _ { 1 }$ is the cycle containing $q$ . Then $c _ { 1 }$ cannot contain $k$ because $u t _ { q k } ( q ) > u t _ { q k } ( k )$ . Thus assume

$$
c _ {1} = \left(a _ {p _ {1}}, \dots , a _ {1}, q ^ {\prime}\right)
$$

with $q ^ { \prime } > k$ and let $j$ be such that $a _ { j } = q$ . We have

$$
\begin{array}{l} t _ {q k} c _ {1} = t _ {q k} \left(a _ {j}, \dots , q ^ {\prime}\right) \left(q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}\right) \\ = (k, a _ {j}, \dots , a _ {1}, q ^ {\prime}) \left(q ^ {\prime}, a _ {p _ {1}}, \dots , a _ {j + 1}\right) \\ = (k, q ^ {\prime}) \left(a _ {j}, \dots , a _ {1}, k\right) \left(a _ {p _ {1}}, \dots , a _ {j + 1}, q ^ {\prime}\right) \\ = t _ {k q ^ {\prime}} \left(a _ {j}, \dots , a _ {1}, k\right) \left(a _ {p _ {1}}, \dots , a _ {j + 1}, q ^ {\prime}\right) \\ \end{array}
$$

Since $u t _ { q k } ( a _ { 1 } ) < u t _ { q k } ( q ^ { \prime } )$ , we have that $u t _ { k q ^ { \prime } } ( a _ { 1 } ) < u t _ { k q ^ { \prime } } ( k )$ if $j > 1$ , and in that case

$$
u t _ {k q ^ {\prime}} (a _ {j}) = u (q) <   u (k) = u t _ {q k} (a _ {j}) <   u t _ {q k} (a _ {j - 1}) = u t _ {k q ^ {\prime}} (a _ {j - 1})
$$

We also have, if $j = 1$ ,

$$
u t _ {k q ^ {\prime}} (a _ {1}) = u (q) <   u (k) <   u \left(q ^ {\prime}\right) = u t _ {k q ^ {\prime}} (k)
$$

Thus

$$
u t _ {k q ^ {\prime}} (a _ {j}) <   \dots <   u t _ {k q ^ {\prime}} (a _ {1}) <   u t _ {k q ^ {\prime}} (k)
$$

so that the first cycle is valid for $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ ′ k−1−−→ w. Since utqk(aj+1) < utqk(q) = u(k), we have that utkq′ (aj+1) < $u t _ { q k } ( a _ { j + 1 } ) < u t _ { q k } ( q ) = u ( k )$ $u t _ { k q ^ { \prime } } ( a _ { j + 1 } ) <$ $u t _ { k q ^ { \prime } } ( q ^ { \prime } ) = u ( k )$ . If there is no other $c _ { i }$ containing $k$ , then we obtain that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ by Lemma 7.3. If there exists a nontrivial cycle containing $k$ , say $c _ { 2 } = ( a _ { p _ { 2 } } ^ { \prime } , \ldots , a _ { 1 } ^ { \prime } , k )$ , then $t _ { q k } c _ { 1 }$ combines with $c _ { 2 }$ to obtain

$$
\begin{array}{l} t _ {q k} c _ {1} c _ {2} = t _ {k q ^ {\prime}} \left(a _ {j}, \dots , a _ {1}, k, a _ {p _ {2}} ^ {\prime}, \dots , a _ {1} ^ {\prime}\right) \left(a _ {p _ {1}}, \dots , a _ {j + 1}, q ^ {\prime}\right) \\ = t _ {k q ^ {\prime}} (a _ {p _ {2}} ^ {\prime}, \ldots , a _ {1} ^ {\prime}, a _ {j}, \ldots , a _ {1}, k) (a _ {p _ {1}}, \ldots , a _ {j + 1}, q ^ {\prime}). \\ \end{array}
$$

Since $u t _ { q k } ( a _ { 1 } ^ { \prime } ) < u t _ { q k } ( k )$ , we have $u t _ { k q ^ { \prime } } ( a _ { 1 } ^ { \prime } ) < u t _ { k q ^ { \prime } } ( q ) = u t _ { k q ^ { \prime } } ( a _ { j } )$ , hence $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . Hence, given $q$ , we have identified a $q ^ { \prime } > k$ such that $\ell ( u t _ { k q ^ { \prime } } ) = \ell ( u ) + 1$ and $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ .

Assume now that $u \stackrel { k _ { \langle } } { \phi } w$ ; in that case, we know that the $q ^ { \prime }$ we have identified is unique. Since

$$
u (k) = u t _ {q k} \left(a _ {j}\right) <   u t _ {q k} \left(a _ {j - 1}\right) = u \left(a _ {j - 1}\right)
$$

we have that $q$ is the rightmost element in the cycle containing $k$ , with $k$ held fixed as the rightmost element of the cycle, in the disjoint cycle decomposition of $( u t _ { k q ^ { \prime } } ) ^ { - 1 } w$ such that $u ( q ) < u ( k )$ , hence $q$ is unique. Thus, if $u \stackrel { k _ { \langle } } { \phi } w$ and $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ , then $q ^ { \prime }$ exists if and only if $q$ does, and each is unique, as desired.

For the last part we show that $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ if $q$ and $q ^ { \prime }$ exist. We have that $u t _ { q k } ( i ) =$ $u t _ { k q ^ { \prime } } ( i )$ if $i \neq q$ and $i < k$ , and the cardinalities of $P _ { k - 1 } ( u t _ { q k } , w )$ and $P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ are the same by Lemma 7.5. If $u t _ { q k } ( q ) \in P _ { k - 1 } ( u t _ { q k } , w )$ , then $u t _ { k q ^ { \prime } } ( q ) \notin P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ , and vice versa, because the values at these indices are not equal and hence they cannot both be equal to $w ( q )$ . Hence, neither $u t _ { q k } ( q )$ nor $u t _ { k q ^ { \prime } } ( q )$ is equal to $w ( q )$ , for if one of them were then one of the two sets $P _ { k - 1 } ( u t _ { q k } , w )$ and $P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ would have more elements than the other. We must therefore have that $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ , as stated. 

Example 7.4. Let $u = [ 3 , 1 , 2 , 5 , 6 , 4 ]$ , let $w = [ 5 , 1 , 6 , 2 , 3 , 4 ]$ , and let $k = 4$ . We have that

$$
u ^ {- 1} w = (1, 4, 3, 5)
$$

Thus $u \stackrel { k _ { \langle } } { \phi } w$ because $u ( 3 ) < u ( 4 )$ , and $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ because both 4 and 5 are present in the cycle. However, if we let $q ^ { \prime } = 5$ , then

$$
u t _ {k q ^ {\prime}} = [ 3, 1, 2, 6, 5, 4 ]
$$

and

$$
\left(u t _ {k q ^ {\prime}}\right) ^ {- 1} w = (1, 5) (3, 4)
$$

and hence $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . Since $u ^ { - 1 } w = ( 1 , 4 , 3 , 5 )$ , this is the case where both $k$ and $q ^ { \prime } = 5$ are present. Thus we should be able to pick $q = 3$ to have $u t _ { q k } \xrightarrow { k - 1 } w$ , since this is the minimal (only) element in the cycle after $k$ such that $u ( q ) < u ( k )$ . Calculating this, we get

$$
u t _ {q k} = [ 3, 1, 5, 2, 6, 4 ]
$$

and

$$
(u t _ {q k}) ^ {- 1} w = (1, 3, 5)
$$

Thus $u t _ { q k } \ \xrightarrow { k - 1 } \ w$ k−1−−→ w. One can check that this is the only index that satisfies the condition. Going in the opposite direction, since $( u t _ { q k } ) ^ { - 1 } w = ( 1 , 3 , 5 )$ we would have picked $q ^ { \prime } = 5$ via the proof. Additionally note that $P _ { k - 1 } ( u t _ { q k } , w ) = \{ 1 \} = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ .

Proof of Proposition 4.4. We are trying to prove that

$$
\mathfrak{S}_{u}(x;y)E_{k}(x;z_{j}) = \sum_{\substack{k\\ u\to w}}\mathrm{weight}^{w}_{u,k}(y;z_{j})  \mathfrak{S}_{w}(x;y)
$$

We note that

$$
\operatorname {w e i g h t} _ {u, k} ^ {w} (y; z _ {j}) = E _ {k - \ell (u, w)} \left(y _ {P _ {k} (u, w)}; z _ {j}\right) = \prod_ {i \in P _ {k} (u, w)} \left(y _ {i} - z _ {j}\right)
$$

so, re-expressing the desired result, we want to prove that

$$
\mathfrak{S}_{u}(x;y)E_{k}(x;z_{j}) = \sum_{u\stackrel {k}{\rightarrow}w}\left(\prod_{i\in P_{k}(u,w)}(y_{i} - z_{j})\right)\mathfrak{S}_{w}(x;y)
$$

We prove this by induction on $k$ . For $k = 1$ , the result is covered by Lemma 7.2, where there are no negative terms. Otherwise, assume the result holds for $k - 1$ . Note that

$$
E _ {k} (x; z _ {j}) = E _ {k - 1} (x; z _ {j}) \left(x _ {k} - z _ {j}\right)
$$

We apply Lemma 7.2 to multiply $\mathfrak { S } _ { u } ( x ; y )$ by $x _ { k } - z _ { j }$ . Namely, the computation of $\mathfrak { S } _ { u } ( x ; y ) E _ { k } ( x ; z _ { j } )$ becomes

$$
\mathfrak {S} _ {u} (x; y) (x _ {k} - z _ {j}) E _ {k - 1} (x; z _ {j}) = \left(y _ {u (k)} - z _ {j}\right) \mathfrak {S} _ {u} (x; y) E _ {k - 1} (x; z _ {j}) + \sum_ {\ell \left(u t _ {k q}\right) = \ell (u) + 1} \operatorname {s i g n} (q - k) \mathfrak {S} _ {u t _ {k q}} (x; y) E _ {k - 1} (x; z _ {j})
$$

Applying the induction hypothesis to expand the terms on the right hand side by multiplying the double Schubert polynomial by the factor $E _ { k - 1 } ( x ; z _ { j } )$ , we obtain

$$
\sum_ {w: u \xrightarrow {k - 1} w} \left(y _ {u (k)} - z _ {j}\right) \left(\prod_ {i \in P _ {k - 1} (u, w)} \left(y _ {i} - z _ {j}\right)\right) \mathfrak {S} _ {w} (x; y) \tag {7.1}
$$

as well as

$$
\sum_ {\substack {q ^ {\prime} > k \\ \ell \left(u t _ {k q ^ {\prime}}\right) = \ell (u) + 1}} \sum_ {w: u t _ {k q ^ {\prime}} \xrightarrow {k - 1} w} \left(\prod_ {i \in P _ {k - 1} \left(u t _ {k q ^ {\prime}}, w\right)} \left(y _ {i} - z _ {j}\right)\right) \mathfrak {S} _ {w} (x; y) \tag{7.2}
$$

and

$$
- \sum_ {\substack {q <   k \\ \ell (u t _ {q k}) = \ell (u) + 1}} \sum_ {w: u t _ {q k} \xrightarrow {k - 1} w} \left(\prod_ {i \in P _ {k - 1} (u t _ {q k}, w)} \left(y _ {i} - z _ {j}\right)\right) \mathfrak {S} _ {w} (x; y) \tag{7.3}
$$

The terms we want to eliminate are as follows

(1) Terms in (7.1) such that $w ( k ) \neq u ( k )$   
(2) Terms in (7.2) such that $u \stackrel { k _ { \langle } } { \phi } w$   
(3) All terms in (7.3).

For all arguments here we assume that $\ell ( u t _ { a b } ) = \ell ( u ) + 1$ for all reflections $t _ { a b }$ we consider. For each $w$ occurring in a term of type (1), we identify a term in the sum (7.3) that cancels it. Assume then that $w$ is such that $u \xrightarrow { k - 1 } w$ but $u ( k ) \neq w ( k )$ . Then $u ( k ) > w ( k )$ by Lemma 7.4; by the same lemma, this makes it impossible that $u \stackrel { k } {  } w$ . By Lemma 7.8, there exists a unique $q < k$ such that $u t _ { q k } \xrightarrow { k - 1 } w$ k−1−−→ w. Since $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u , w ) \cup \{ u ( k ) \}$ by the same lemma, the term corresponding to $w$ in (7.3) corresponding to the permutation $u t _ { q k }$ cancels the term corresponding to $w$ in (7.1), applying the induction hypothesis. Thus for each term of type (1) we have identified a unique term in (7.3) that cancels it.

Let $q ^ { \prime } > k$ be a positive integer and let $w$ be an index such that there is a term corresponding to $u t _ { k q ^ { \prime } }$ and $w$ of type (2) in (7.2), meaning that $u \stackrel { k _ { \langle } } { \phi } w$ . By definition we have that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ . We cannot have that $u \xrightarrow { k - 1 } w$ u k−1−−→ w by Lemma 7.8 since the existence of the index q′ > k contradicts the conclusion of the lemma, so $q ^ { \prime } > k$ we have that $u \stackrel { k _ { \langle } } { \phi } w$ , $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ , and $q ^ { \prime } > k$ is such that $u t _ { k q ^ { \prime } } \xrightarrow { k - 1 } w$ k− . Therefore, by Lemma 7.9, $q ^ { \prime }$ is unique and there is a unique $q < k$ such that $u t _ { q k } \xrightarrow { k - 1 } w$ . By the same lemma, $P _ { k - 1 } ( u t _ { q k } , w ) = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ , so the two terms corresponding to these indices have the same weight with opposite signs by the induction hypothesis, hence they cancel. Thus all terms of type (2) are canceled from the sum with a term from (7.3) that was not canceled in the previous paragraph by a term of type (1) since $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ .

$q < k$ We claim that at this point all terms in (7.3) have been canceled. Fix such that $u t _ { q k } \xrightarrow { k - 1 } w$ , then by Lemma 7.7 we cannot have that both $w$ . Note first that if there is a $u \stackrel { k } {  } w$ and $u \xrightarrow { k - 1 } w$ . Thus either $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ or $u \stackrel { k _ { \langle } } { \phi } w$ . In the case where both are true we identified a unique corresponding $q ^ { \prime } > k$ such that $u t _ { k q ^ { \prime } } \ \xrightarrow { k - 1 } w$ and we showed that the corresponding term has the same coefficient with the opposite sign. Thus all terms with $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ and $u \stackrel { k _ { \langle } } { \phi } w$ have been canceled. If $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ but $u \stackrel { k } {  } w$ , by Lemma 7.6 ${ \mathfrak { S } } _ { w } ( x ; y )$ has a coefficient of 0 in (7.3). Finally, suppose $u \xrightarrow { k - 1 } w$ but $u \stackrel { k _ { \langle } } { \phi } w$ . Then the $q < k$ corresponding to the term in the sum such that $u t _ { q k } \xrightarrow { k - 1 } w$ is the unique index with this property by Lemma 7.8, and as argued previously it has been canceled. The claim follows.

At this point the only terms that remain are those such that $u \stackrel { k } {  } w$ in (7.1) and (7.2). The weight in (7.1) is correct by the induction hypothesis because we canceled the terms with $u ( k ) \neq w ( k )$ , and for (7.2), fixing $q ^ { \prime } > k$ , since $u t _ { k q ^ { \prime } }$ differs from $u$ only at $k$ and $q ^ { \prime }$ we have that $P _ { k } ( u , w ) = P _ { k - 1 } ( u t _ { k q ^ { \prime } } , w )$ . By Lemma 7.7, no one $q ^ { \prime } > k$ $w$ that occurs in (7.1) also occurs in (7.2). By Lemma 7.6, if such that $u t _ { k q ^ { \prime } } \ \xrightarrow { k - 1 } \ w$ , so all ${ \mathfrak { S } } _ { w } ( x ; y )$ such that $u \stackrel { k } {  } w$ $u \xrightarrow { k \xrightarrow { 1 } 1 } w$ occur exactly once and we have the and $u \stackrel { k } {  } w$ there is exactly result. 

Proof of Theorem 7.1. This follows from Proposition 4.4 coupled with the Cauchy formula for double Schubert polynomials [21]. Let $e _ { i , k } ( x )$ be the usual elementary symmetric polynomial $e _ { i } ( x _ { 1 } , \dots , x _ { k } )$ and let $h _ { i , k } ( x ) = h _ { i } ( x _ { 1 } , . . . , x _ { k } )$ be the complete homogeneous symmetric polynomial of degree $_ i$ in $x _ { 1 } , \ldots , x _ { k }$ . Note that when we expand the product in the definition of $E _ { k } ( x ; z _ { 1 } )$ we obtain

$$
E _ {k} (x; z _ {1}) = \sum_ {i = 0} ^ {k} e _ {i, k} (x) (- z _ {1}) ^ {k - i}
$$

By Proposition 4.4, we have

$$
\begin{array}{l} \sum_ {i = 0} ^ {k} \mathfrak {S} _ {u} (x; y) e _ {i, k} (x) (- z _ {1}) ^ {k - i} = \mathfrak {S} _ {u} (x; y) E _ {k} (x; z _ {1}) \\ = \sum_ {u \xrightarrow {k} w} E _ {k - \ell (u, w)} (y _ {P _ {k} (u, w)}; z) \mathfrak {S} _ {w} (x; y) \\ = \sum_ {u \xrightarrow {k} w} \sum_ {i = \ell (u, w)} ^ {k} e _ {i - \ell (u, w), k - \ell (u, w)} \left(y _ {P _ {k} (u, w)}\right) \mathfrak {S} _ {w} (x; y) (- z _ {1}) ^ {(k - \ell (u, w)) - (i - \ell (u, w))} \\ \end{array}
$$

Equating the coefficients of powers of $- z _ { 1 }$ in the above equation we obtain that

$$
\mathfrak{S}_{u}(x;y)e_{i,k}(x) = \sum_{\substack{k\\ u\to w}}e_{i - \ell (u,w),k - \ell (u,w)}(y_{P_{k}(u,w)})  \mathfrak{S}_{w}(x;y)
$$

By the Cauchy formula in [21] we have that

$$
E _ {p, k} (x; z) = \sum_ {i = 0} ^ {p} e _ {i, k} (x) h _ {p - i, k + 1 - p} (- z)
$$

Therefore the coefficient of ${ \mathfrak { S } } _ { w } ( x ; y )$ in $\mathfrak { S } _ { u } ( x ; y ) E _ { p , k } ( x ; z )$ is, replacing the index $i$ with $j + \ell ( u , w )$ ,

$$
\sum_ {j = 0} ^ {p - \ell (u, w)} e _ {j, k - \ell (u, w)} \left(y _ {P _ {k} (u, w)}\right) h _ {p - \ell (u, w) - j, (k - \ell (u, w)) + 1 - (p - \ell (u, w))} (- z)
$$

which is exactly $E _ { p - \ell ( u , w ) , k - \ell ( u , w ) } ( y _ { P _ { k } ( u , w ) } ; z )$ , and we have the result.

Via the following formula, our Pieri formula is also positive in the sense of Conjecture 1.1 as well as the equivariant specialization.

Proposition 7.10. Let $p , k$ with $1 \leq p \leq k$ be integers. Let $S _ { p , k }$ be the set of sequences $( a _ { 0 } , \dotsc , a _ { p - 1 } )$ such that $1 \leq a _ { i } \leq k + 1 - p$ for all $_ i$ and $a _ { i } \leq a _ { i + 1 }$ for all $0 \leq i < p - 1$ . Then

$$
E _ {p, k} (x; z) = \sum_ {(a _ {0}, \dots , a _ {p - 1}) \in \mathcal {S} _ {p, k}} \prod_ {i = 0} ^ {p - 1} (x _ {a _ {i} + i} - z _ {a _ {i}})
$$

Proof. This follows from the formula [23, (4)]. A term in a factorial Schur function is written as the product of linear factors $x _ { T ( \alpha ) } - z _ { T ( \alpha ) + c - r }$ , where $T$ is a tableau, $\alpha$ ranges over all boxes, and $\alpha$ is in column $c$ and row $r$ . For $E _ { p , k } ( x ; z )$ , this tableau is on a single column, so that $c = 1$ and $1 \leq r \leq p$ , and $T$ is strictly increasing along the rows. 

Example 7.5. We select some of the coefficients in Example 7.1 to see that they are nonnegative when substituting $z = y$ .

$$
\begin{array}{l} E _ {3, 4} \left(y _ {1}, y _ {3}, y _ {4}, y _ {5}; z\right) = \left(y _ {1} - z _ {1}\right) \left(y _ {3} - z _ {1}\right) \left(y _ {4} - z _ {1}\right) + \left(y _ {1} - z _ {1}\right) \left(y _ {3} - z _ {1}\right) \left(y _ {5} - z _ {2}\right) \\ + \left(y _ {1} - z _ {1}\right) \left(y _ {4} - z _ {2}\right) \left(y _ {5} - z _ {2}\right) + \left(y _ {3} - z _ {2}\right) \left(y _ {4} - z _ {2}\right) \left(y _ {5} - z _ {2}\right) \\ \Rightarrow \left(y _ {3} - y _ {2}\right) \left(y _ {4} - y _ {2}\right) \left(y _ {5} - y _ {2}\right) \\ \end{array}
$$

$$
\begin{array}{l} E _ {2, 3} \left(y _ {3}, y _ {4}, y _ {5}; z\right) = \left(y _ {3} - z _ {1}\right) \left(y _ {4} - z _ {1}\right) + \left(y _ {3} - z _ {1}\right) \left(y _ {5} - z _ {2}\right) + \left(y _ {4} - z _ {2}\right) \left(y _ {5} - z _ {2}\right) \\ \Rightarrow \left(y _ {3} - y _ {1}\right) \left(y _ {4} - y _ {1}\right) + \left(y _ {3} - y _ {1}\right) \left(y _ {5} - y _ {2}\right) + \left(y _ {4} - y _ {2}\right) \left(y _ {5} - y _ {2}\right) \\ \end{array}
$$

$$
\begin{array}{l} E _ {1, 2} \left(y _ {1}, y _ {3}; z\right) = \left(y _ {1} - z _ {1}\right) + \left(y _ {3} - z _ {2}\right) \\ \Rightarrow y _ {3} - y _ {2} \\ \end{array}
$$

# 8. A more general result

We note that in Theorem 3.1 the value of $p$ is unimportant as long as the condition is satisfied; the computation of the coefficient $e _ { u v } ^ { w } ( y ; z )$ has nothing to do with $p$ . Indeed, Theorem 3.1 is not the most general possible result that comes out of this method. The most general result is the following.

Theorem 8.1. Let $u , v \in S _ { \infty }$ and suppose $v ^ { - 1 } \mu _ { v } = s _ { i _ { 1 } } \cdot \cdot \cdot s _ { i _ { m } }$ with $\ell ( u s _ { i _ { j } } ) > \ell ( u )$ for all j. Then

$$
\mathfrak {S} _ {u} (x; y) \mathfrak {S} _ {v} (x; z) = \sum_ {w \in S _ {\infty}} e _ {u v} ^ {w} (y; z) \mathfrak {S} _ {w} (x; y)
$$

The proof of this result is virtually identical and we will not include it. One obvious case where this works is where $u$ is arbitrary and $\boldsymbol { v }$ is dominant, so that $v = \mu _ { v }$ and $v ^ { - 1 } \mu _ { v }$ is the identity. We illustrate a less trivial case, computing all of the coefficients that occur in the product.

Example 8.1. Let $u = [ 4 , 1 , 3 , 2 ]$ and let $v = \left[ 3 , 1 , 4 , 2 \right]$ . Then $u$ and $\boldsymbol { v }$ do not satisfy the conditions of Theorem 3.1, but Theorem 8.1 applies. We have

$$
\begin{array}{l} \mu_ {v} = [ 3, 4, 1, 2 ] \\ \mathfrak {c} (\mu_ {v}) = (2, 2) \\ \lambda (v) = (2, 2) \\ v ^ {- 1} \mu_ {v} = [ 1, 3, 2 ] \\ \end{array}
$$

$$
\begin{array} { c } \left[ \begin{array} { c } 4 , 1 , 3 , 2 \\ 4 \\ 1 \\ 3 \\ 2 \\ 2 \end{array} \right] & \left[ \begin{array} { c } 4 , 1 , 3 , 2 \\ 4 \\ 1 \\ 3 \\ 2 \end{array} \right] \\ \left[ \begin{array} { c } 4 \\ 1 \\ 3 \\ 2 \end{array} \right] & \left[ \begin{array} { c } 4 \\ 1 \\ 3 \\ 2 \end{array} \right] \\ ( y _ { 1 } - z _ { 1 } ) ( y _ { 4 } - z _ { 1 } ) ( y _ { 4 } - z _ { 2 } ) & ( y _ { 3 } - z _ { 2 } ) ( y _ { 4 } - z _ { 1 } ) ( y _ { 4 } - z _ { 2 } ) \\ ( y _ { 1 } - z _ { 1 } ) ( y _ { 4 } - z _ { 1 } ) ( y _ { 4 } - z _ { 2 } ) + ( y _ { 3 } - z _ { 2 } ) ( y _ { 4 } - z _ { 1 } ) ( y _ { 4 } - z _ { 2 } ) ) & \mathfrak { S } _ { [ 4 , 1 , 3 , 2 ] } ( x ; y ) + ( y _ { 4 } - z _ { 1 } ) ( y _ { 4 } - z _ { 2 } )   \mathfrak { S } _ { [ 4 , 2 , 3 , 1 ] } ( x ; y ) \\ [ 5 , 1 , 3 , 2 , 4 ] & \left[ \begin{array} { c } 5 , 1 , 3 , 2 , 4 \\ 4 \\ 1 \\ 3 \\ 2 \\ 5 \end{array} \right] \\ \left[ \begin{array} { c } 4 \\ 1 \\ 3 \\ 2 \\ 5 \end{array} \right] & \left[ \begin{array} { c } 4 \\ 1 \\ 3 \\ 2 \\ 5 \end{array} \right] \\ ( y _ { 3 } - z _ { 2 } ) ( y _ { 4 } - z _ { 1 } ) & ( y _ { 1 } - z _ { 1 } ) ( y _ { 4 } - z _ { 1 } ) \\ ( y _ { 1 } - z _ { 1 } ) ( y _ { 4 } - z _ { 1 } ) & ( y _ { 1 } - z _ { 1 } ) ( y _ { 5 } - z _ { 1 } ) + ( y _ { 3 } - z _ { 2 } ) ( y _ { 5 } - z _ { 2 } )   \mathfrak { S } _ { [ 5 , 1 , 3 , 2 , 4 ] } ( x ; y ) \\ [ 4 , 1 , 5 , 2 , 3 ] & \left[ \begin{array} { c } 5 , 1 , 4 , 2 , 3 \\ 4 \\ 1 \\ 3 \\ 2 \\ 5 \end{array} \right] \\ \left[ \begin{array} { c } \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text  ~ \bf ~ \mathrm { ~ \delta ~ ~ d ~ a l p h a ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ ~ d ~ a l p h a ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text  ~ \bf ~ \mathrm { ~ d ~ a l p h a ~ } ^  \text { ~ \bf ~ \delta ~ } ^  \text { ~ \bf ~ d ~ a l p h a ~ } ^  \text { ~ \bf ~ d ~ a l p h a ~ } ^  \text { ~ \bf ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ } ^  \text { ~ d ~ a l p h a ~ d e l t a } ^  \text { ~ d ~ a l p h a ~ d e l t a } ^  \text { ~ d ~ a l p h a ~ d e l t a } ^  \text { ~ d ~ a l p h a ~ d e l t a } ^  \text { ~ d ~ a l p h a ~ d e l t a } ^  \text  ~ d ~ a l p h a ~ d e l t o m o n e r m s i n g u l a r m u l t i m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t o f t h e r e f o r m o n e n t O E M A L T H A N D F I G U T E ] \\ [ 5 , 2 , 3 , 1 , 4 ] & [ 5 , 2 , 3 , 1 , 4 ] \\ [ 4 \\ [ 5 \\ [ 6 , 1 , 3 , 2 , 4 , 5 ] & [ 6 , 1 , 3 , 2 , 4 , 5 ] \\ [ 4 \\ [ 5 \\ [ 6 ] & [ 7 , 1 , 3 , 2 , 4 , 5 ] \\ [ [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [     [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [   [
\[ (y _ {1 } - z _ {1 }) + (y _ \frac {1}{3}, - z _ {\frac{3}{1}}) + (y _ \frac{3}{3},- z _ {\frac{3}{3}}) + (y _ \frac{3}{3},-z _ {\frac{3}{3}}) + (y _ \frac{3}{3},-z _ {\frac{3}{3}}) + (y _ \frac{3}{3},-z _ {\frac{3}{3}}) + (y _ \frac{3}{3},-z _ {\frac{3}{3}}) + (y _ \frac{3}{3},-z _ {\frac{3}{3}}) + (x ; y) + (\mathfrak S _ {[6 ,1,3,2,4,5 ]}) + (\mathfrak S _ {[6 ,1,3,2,4,5 ]}) + (\mathfrak S _ {[6 ,1,3,2,4,5 ]}) + (\mathfrak S _ {[6 ,1,3,2,4,5 ]}) + (\mathfrak S _ {[6 ,1,3,2,4,5 ]}) + (\mathfrak S _ {[6 ,1,3,2,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak Z)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathfrak S _ {[6 ,1,3,\mathfrak X)} + (\mathbb Y)) ] ] & ] & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ & & \\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\ &&\\
$$

# 9. Python package for computing Schubert products

We have written a python package schubmult that is available in the central python package repository which requires python 3.9 or higher that allows one to compute products of ordinary Schubert polynomials, products of double Schubert polynomials in the same set of variables, and products of double Schubert polynomials in different sets of variables. When one installs the package with

# pip install schubmult

this installs three executables on the user’s system: schubmult_py for ordinary Schubert polynomials (so named so as not to conflict with existing software named schubmult), schubmult_double for double Schubert polynomials in the same set of variables, with the result expressed with nonnegative coefficients in terms of the negative roots, and schubmult_yz for computing Molev-Sagan products of double Schubert polynomials. It

is entirely platform independent, provided the python installation can be configured properly on the system. We have tested it on both Linux and Windows.

It is recommended you periodically check for new versions, which you can do directly by running

# pip install schubmult --upgrade

when you already have schubmult.

The method of calculation is to express one of the (double) Schubert polynomials in the product in terms of (factorial) elementary symmetric polynomials and apply the Pieri formula. There’s no choice of which one to express in this way in the Molev-Sagan case, but for schubmult_py and schubmult_double it picks the one that is closest to being dominant. Even in the ordinary Schubert polynomial case it is faster than currently existing software in most cases, sometimes dramatically.

All three executables have the same command line syntax, which is the same as the command line syntax for schubmult from lrcalc. An instructive example is to compute

```txt
schubmult.py 1 2 4 9 11 6 8 12 3 5 7 10 - 6 8 1 2 3 4 7 10 12 14 5 9 11 13 
```

The number of permutations on the command line is not limited to two, so we could for example compute the product of three Schubert polynomials as

```batch
schubmult.py 614325-7635124-51432 
```

For an example Molev-Sagan product, one could execute

```txt
schubmult_yz 134625-2157346 
```

and the same product in equivariant cohomology can be computed as

```txt
schubmult-double 134625-2157346 
```

where some terms will vanish.

For all three executables, one can specify the input as the code of the permutation instead of the permutation itself with the command line argument -code. For example,

```txt
schubmult_yz -code 0 1 1 2 - 1 0 2 3 
```

The output will then express the permutations as codes as well.

The coefficients in schubmult_yz are expressed in terms of $y _ { i } - z _ { j }$ . If desired, the coefficients can be displayed positively as polynomials in $y _ { i } \mathrm { ~ - ~ } z _ { j }$ using the command line option --display-positive, for example

```txt
schubmult_yz 134625-2157346--display-positive 
```

Feasibility of displaying the result positively varies, and one should expect to run into some cases such that the computation will not finish in a reasonable amount of time. As this is still only always possible conjecturally, it is conceivable one could run into a counterexample; if one is found, please email the counterexample to the author.

The coefficients in schubmult_double are subjected to a change of variables in order for them to visibly have nonnegative coefficients.

Though the package was primarily intended to be used through the installed executables, it can also be imported into your own python script and the function schubmult used programmatically. For example,

from schubmult.schubmult_yz import schubmult

```txt
coeff_dict = schubmult((1, 3, 4, 6, 2, 5): 1), (2, 1, 5, 7, 3, 4, 6)) 
```

The return value is a python dict where the keys are permutations, which are expressed as tuples of ints, and the values are either ints (for schubmult.schubmult_py) or symengine objects (which can be polynomials). The dict representation is intended to represent a linear combination of (double) Schubert polynomials with the values as the coefficients. Note that there may be values of 0 in the resulting dict, or values that simplify to 0 but do not appear immediately to be 0 if they are symengine objects. No 0 values will be displayed in schubmult_py or schubmult_double, but there may be coefficients displayed in schubmult_yz that simplify to 0. Simplifying a polynomial is an expensive calculation, and in the interest of saving time this is not done in the output, except in schubmult_double.

In addition to python, schubmult is also functional in Sage.

Visit the pypi page at

for updates on the latest version.

# References

[1] Bergeron, N., and Billey, S. RC-graphs and Schubert polynomials. Experimental Math. 2, 4 (1993), 257–269.   
[2] Bergeron, N., and Sottile, F. Skew Schubert functions and the Pieri formula for flag manifolds. Trans. Amer. Math. Soc. 354, 2 (2001), 651–673.   
[3] Bernstein, I. N., Gelfand, I. M., and Gelfand, S. I. Schubert cells and the cohomology of the spaces G/P. Russian Math. Surveys 28 (1973), 1–26.   
[4] Bjorner, A., and Brenti, F. ¨ Combinatorics of Coxeter Groups. Springer, 2005.   
[5] Buch, A. S. Mutations of puzzles and equivariant cohomology of two-step flag varieties. Ann. of Math. (2015), 173–220.   
[6] Bump, D., McNamara, P. J., and Nakasuji, M. Factorial Schur functions and the Yang-Baxter equation. arXiv preprint arXiv:1108.3087 (2011).   
[7] Chen, W. Y., Yan, G.-G., and Yang, A. L. The skew Schubert polynomials. European J. Combin. 25, 8 (2004), 1181–1196.   
[8] Fan, N. J., Guo, P. L., and Xiong, R. Bumpless pipe dreams meet Puzzles. arXiv preprint arXiv:2309.00467 (2023).   
[9] Graham, W. Positivity in equivariant Schubert calculus. Duke Math. J. 109, 3 (2001), 599–614.   
[10] (https://mathoverflow.net/users/62135/matt samuel), M. S. Product of a Schubert polynomial and a double Schubert polynomial. MathOverflow. URL:https://mathoverflow.net/q/212762 (version: 2016-09-06).   
[11] Huang, D. Schubert products for permutations with separated descents. International Mathematics Research Notices (November 2022).   
[12] Kirillov, A. N. Skew divided difference operators and Schubert polynomials. SIGMA. Symmetry, Integrability and Geometry: Methods and Applications 3 (2007), 072.   
[13] Knutson, A. Schubert polynomials, pipe dreams, equivariant classes, and a co-transition formula. arXiv.org:1909.13777 (2019).   
[14] Knutson, A., and Tao, T. Puzzles and (equivariant) cohomology of Grassmannians. Duke Math. J. 119, 2 (2003), 221–260.   
[15] Knutson, A., and Zinn-Justin, P. Schubert calculus and quiver varieties. https://pi.math.cornell.edu/allenk/boston2019.pdf, 2019. Accessed 2023-06-10.   
[16] Knutson, A., and Zinn-Justin, P. Schubert puzzles and integrability III: separated descents. arXiv preprint arXiv:2306.13855 (2023).   
[17] Kohnert, A. Multiplication of a Schubert polynomial by a Schur polynomial. Ann. Comb. 1, 1 (1997), 367–375.   
[18] Kostant, B., and Kumar, S. The nil Hecke ring and cohomology of G/P for a Kac-Moody group G. Proceedings of the National Academy of Sciences 83, 6 (1986), 1543–1545.   
[19] Lascoux, A., and Schutzenberger, M. ¨ Polynˆomes de Schubert. Comptes Rendus de l’Acad´emie des Sciences, S´erie I 294, 13 (1982), 447–450.   
[20] Lenart, C., and Sottile, F. Skew Schubert polynomials. Proc. Amer. Math. Soc. 131, 11 (2003), 3319–3328.   
[21] Macdonald, I. G. Notes on Schubert Polynomials. Universit´e Du Qu´ebec `a Montr´eal, D´ep. de math´ematiques et d’informatique, 1991.   
[22] Molev, A. Littlewood–Richardson polynomials. Journal of Algebra 321, 11 (2009), 3450–3468.   
[23] Molev, A., and Sagan, B. A Littlewood-Richardson rule for factorial Schur functions. Trans. Amer. Math. Soc. 351, 11 (1999), 4429–4443.   
[24] Purbhoo, K., and Sottile, F. A Littlewood-Richardson rule for Grassmannian permutations. Proc. Am. Math. Soc. 137 (2009), 1875–1882.   
[25] Robinson, S. A Pieri-Type Formula for $H ^ { * } T ( S L _ { n } ( C ) / B )$ . J. Algebra 249, 1 (2002), 38–58.   
[26] Samuel, M. J. The Leibniz formula for divided difference operators associated to Kac-Moody root systems. PhD thesis, Rutgers, The State University of New Jersey, 2014.   
[27] Sottile, F. Pieri’s rule for flag manifolds and Schubert polynomials. Ann. Inst. Fourier 46, 1 (1996), 89–110.   
[28] Tamvakis, H. Tableau formulas for skew Schubert polynomials. arXiv preprint arXiv:2008.07034 (2020).

Monroe Township, Middlesex County, New Jersey, United States

Email address: matthematics@gmail.com