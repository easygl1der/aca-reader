# A correspondence dual to McKay’s

Jean-Luc Brylinski*

# 1. Introduction

It is well-known from the work of DuVal [DuVal1] and M. Artin $\lfloor \mathbf { A } \rfloor$ that there is a one-to-one correspondence between finite subgroups $G$ of $S U ( 2 )$ and Coxeter-Dynkin diagrams $\Delta$ of type $A , D , E$ . This involves a minimal resolution of singularities $\tilde { X }$ of the singular algebraic surface $\mathbb { C } ^ { 2 } / G$ . Around 1980 McKay found a deep correspondence between vertices of the affine Coxeter-Dynkin diagram and irreducible representations of the group [McKay1] [Mckay2]. Several systematic representation-theoretic proofs were given by Kostant [Ko], Steinberg [St2], Springer [Sp]. A geometric interpretation of the correspondence was given by Gonzalez-Sprinberg and Verdier [GS-V] and also by Kn¨orrer $\left[ \mathbf { K n } \right]$ .

There is also a dual correspondence, this time between vertices of $\Delta$ and non-trivial conjugacy classes of $G$ . This dual correspondence was introduced by Ito and Reid [I-R] in the more general context of a finite subgroup of $S U ( n )$ . The construction is in fact very simple topologically: we interpret $G$ as the fundamental group of the complement of the exceptional divisor in $\tilde { X }$ . Then each vertex of $\Delta$ corresponds to a component of this divisor, and there is an associated class of a small loop encircling said component. The dual correspondence was studied by Ito and Reid from the point of view of valuations on function fields. From the description of the fundamental group due to Mumford [Mu] one sees that this gives a one-to-one correspondence between vertices of the diagram and non-trivial conjugacy classes. This result amounts to the dimension 2 case of a more general theorem proved by Ito and Reid [I-R]. The dual correspondence has a number of interesting further properties, which are detailed in Theorem 4.1. These properties involve the three (or two) so-called special conjugacy classes corresponding to ends of the diagram, and the description of the edges of the diagram involve pairs of commuting elements $x , y$ such that $y$ is special; then the conjugacy classes of $x$ and $x y$ are joined by an edge.

There seem to be intriguing connections between the McKay correspondence and the dual correspondence. We prove a determinantal formula concerning an element $g _ { j }$ of $G$ associated to a vertex $v _ { j }$ of $\Delta$ and the irreducible representation $E _ { k }$ associated to a vertex $v _ { k }$ :

$$
d e t (g _ {j}, E _ {k}) = e x p (- 2 \pi i (C ^ {- 1}) _ {j k}),
$$

where $C ^ { - 1 }$ is the inverse of the Cartan matrix. One tool we use in proving this formula is the geometric description of the McKay correspondence in [GS-V] by means of the first Chern class of the vector bundle associated to a representation of $G$ . We also use the properties of vector bundles with integrable connections admitting logarithmic poles, in particular the computation of the first Chern class from the residues of the connection.

The paper ends with some remarks on the matrix-valued Fourier transform which results from comparing the two correspondences.

This work was written in May-June 1996 as I was visiting Harvard University. I thank David Kazhdan and the Harvard Mathematics Department for their hospitality. I am grateful to H´el`ene Esnault for correspondence and information about her work [E-V] and for her useful remarks on a first draft of this paper. I thank Victor Batyrev for pointing out to me the paper [I-R]. I am grateful to Igor Dolgachev and to John McKay for reading a first version of this paper and making many valuable comments.

# 2. The McKay correspondence

There is a by now classical correspondence between conjugacy classes of finite subgroups of $S U ( 2 )$ (or equivalently, of $S L ( 2 , \mathbb { C } )$ ) and simply-laced Coxeter-Dynkin diagrams (thus of type $A _ { n }$ , $D _ { n }$ or $E _ { n }$ ). The correspondence was constructed by DuVal [DuVal1] using algebraic geometry. It may be phrased as follows. Given a finite subgroup $G \subset S U ( 2 )$ one can construct the singular algebraic surface $X = \mathbb { C } ^ { 2 } / G$ , quotient of the affine plane by the action of $G$ . Let $f : \mathbb { C } ^ { 2 } \to X$ be the quotient map; the point $o = f ( 0 )$ is called the origin of $X$ . The singular locus of $X$ is reduced to $o$ , unless $G = 1$ , in which case $X = \mathbb { C } ^ { 2 }$ is smooth. $X$ is a normal affine surface, whose algebra of regular functions is the algebra $\mathbb { C } [ x , y ] ^ { G }$ of invariants in the polynomial algebra on two generators. There is a minimal resolution of singularities $p : \tilde { X } \to X$ , so

- $\tilde { X }$ is a smooth algebraic surface;

- $p$ is a proper regular mapping, which induces an isomorphism over the open subset $U = X \backslash \{ o \}$ of $X$ ;   
- the minimality of the resolution means that $\tilde { X }$ does not contain any rational curve of self-intersection $^ { - 1 }$ .

Then the reduced fiber $D = p ^ { - 1 } ( o ) _ { r e d }$ is a curve, which is a union of smooth rational curves $D _ { 1 } , \cdots , D _ { r }$ . Any two curves $D _ { i }$ and $D _ { j }$ intersect transversally at at most one point of $\tilde { X }$ . One can then construct a graph $\Delta$ such that the vertices $v _ { 1 } , \cdots , v _ { r }$ of $\Delta$ correspond to the curves $D _ { j }$ , and where one joins the vertices $v _ { i }$ and $v _ { j }$ by an edge whenever the divisors $D _ { i }$ and $D _ { j }$ intersect.

One associates to the system of curves $( D _ { j } )$ a square matrix $A = A ( G )$ of size $r$ , called the intersection matrix, such that $A _ { i j }$ is the intersection number $D _ { i } \cdot D _ { j }$ on the smooth surface $\tilde { X }$ . On the other hand the graph $\Delta$ has an incidence matrix $M$ . Since any $D _ { i }$ has self-intersection $- 2$ we have $A = - 2 I d + M$ .

We then have

Theorem 2.1. (Du Val [DuVal1], M. Artin [A]) (1) For any finite subgroup $G$ o f $S U ( 2 )$ , the graph $\Gamma$ is a simply-laced Coxeter-Dynkin diagram.

(2) The Cartan matrix $C$ of the Coxeter-Dynkin diagram ∆ is the opposite of the intersection matrix $A$ .   
(3) This construction induces a one-to-one correspondence between conjugacy classes of finite subgroups of $S L ( 2 , \mathbb { C } )$ and simply-laced Coxeter-Dynkin diagrams.

We give the table showing the simply-laced diagrams and the corresponding finite subgroups of $S U ( 2 )$ . For a regular polyhedron, we have the corresponding symmetry group $H \subset S O ( 3 )$ . Its inverse image $G$ in the double cover $S U ( 2 )$ is the corresponding binary polyhedral group.

Table of subgroups of $S U ( 2 )$   

<table><tr><td colspan="3">FINITE SUBGROUPS OF SU(2)</td></tr><tr><td>Δ</td><td>order of G</td><td>G</td></tr><tr><td>An</td><td>n+1</td><td>cyclic</td></tr><tr><td>Dn,n≥3</td><td>4n-8</td><td>binary dihedral</td></tr><tr><td>E6</td><td>24</td><td>binary tetrahedral</td></tr><tr><td>E7</td><td>48</td><td>binary octahedral</td></tr><tr><td>E8</td><td>120</td><td>binary icosahedral</td></tr></table>

The McKay correspondence on the other hand involves simply-laced affine Coxeter-Dynkin diagrams [McKay1] [McKay2]. Given a simply-laced Coxeter-Dynkin diagram $\Delta$ , there is a corresponding affine diagram $\tilde { \Delta }$ , which is obtained by adding one vertex $v _ { 0 }$ to $\Delta$ . We need to explain for which $i \in \{ 1 , \cdots , r \}$ the vertex $v _ { 0 }$ and $v _ { i }$ are linked by an edge. This requires introducing the root system $R$ corresponding to $\Delta$ . This a finite subset of an euclidean vector space $E$ of dimension $r$ , consisting of vectors of length 2. The vertices $v _ { 1 } , \cdots , v _ { r }$ correspond to the simple roots $\alpha _ { 1 } , \cdots , \cdots , \alpha _ { r }$ , with respect to system $R _ { + }$ of positive roots. The Cartan matrix is given by $C _ { i j } = \left( \alpha _ { i } , \alpha _ { j } \right)$ . There is a longest root $\theta$ (so that $\theta$ is a positive root, and $\theta + \alpha _ { i }$ is not a root for $j = 1 , \cdots , r$ ). Then the new vertex $v _ { 0 }$ of $\tilde { \Delta }$ corresponds to $\alpha _ { 0 } : = - \theta$ . There is an edge in $\tilde { \Delta }$ between the vertices $v _ { 0 }$ and $v _ { i }$ if and only if $( \alpha _ { 0 } , \alpha _ { i } ) \neq 0$ .

$\textstyle \sum _ { j = 1 0 } ^ { r } m _ { i } \alpha _ { i } = 0$ Each vertex $v _ { i }$ of Equivalently we have $\tilde { \Delta }$ is labeled by a positive integer $\begin{array} { r } { \theta = \sum _ { j = 1 } ^ { r } \ m _ { j } \alpha _ { j } } \end{array}$ $m _ { i }$ in such a way that $m _ { 0 } = 1$ and

We can now state the McKay correspondence.

Theorem 2.2. (Mckay [McKay]) Let $G$ be a finite subgroup of $S L ( 2 , \mathbb { C } )$ and let $\tilde { \Delta }$ be the corresponding affine Coxeter-Dynkin diagram. (1) There is a one-to-one correspondence $i \mapsto R _ { i }$ between vertices of $\tilde { \Delta }$ and equivalence classes of irreducible representations of $G$ . The dimension of $R _ { i }$ is equal to $m _ { i }$ .

(2) Let $E$ be the two-dimensional representation of $G$ in $\mathbb { C } ^ { 2 }$ . Then for any $i \in$ $\{ 0 , \cdots , r \}$ we have

$$
R _ {i} \otimes E \tilde {\rightarrow} \oplus_ {j \text {i n c i d e n t t o} i} R _ {j} \tag {2}
$$

This correspondence was constructed empirically by McKay. Coherent proofs were given in [St2] [Sp]. The representation-theoretic and invariant-theoretic aspects of the

correspondence were developed further in [Ko]. A geometric construction was given by Gonzalez-Sprinberg and Verdier [GS-V]; this will be used in §5.

# 3. The special conjugacy classes.

We will use a well-known topological interpretation of the group $G \subset S L ( 2 , \mathbb { C } )$ .

Lemma 3.1. We have

$$
G \xrightarrow {\sim} \pi_ {1} (X \setminus \{o \}) = \pi_ {1} (\tilde {X} \setminus D) \tag {3-1}
$$

We did not specify a base point in Lemma 3.1. This is because we only need the isomorphism $G { \tilde { \to } } \pi _ { 1 } ( { \tilde { X } } \setminus D )$ up to conjugation.

Proof. The space $X \setminus \{ o \}$ is the quotient of the simply-connected space $\mathbb { C } ^ { 2 } \setminus \{ 0 \}$ by the action of $G$ . Because $G \subset S L ( 2 , \mathbb { C } )$ , the action of $G$ on $\mathbb { C } ^ { 2 } \setminus \{ 0 \}$ is fixed point free. Thus $\mathbb { C } ^ { 2 } \setminus \{ 0 \}  X \setminus \{ o \}$ is a Galois covering with group $G$ .

For any component $D _ { i }$ of $D$ ( $1 \leq i \leq r$ ), there is a well-defined conjugacy class in $\pi _ { 1 } ( \tilde { X } \backslash D )$ which corresponds to a small oriented loop $\gamma _ { i }$ around the divisor $D _ { i }$ . Of course the precise construction of this loop depends on the base point but the conjugacy class is well-defined. Using the isomorphism 3-1, this defines a conjugacy class in $G$ , which will be denoted by $O _ { i }$ .

Definition 3.2. The dual McKay correspondence is the map

$$
\{\mathrm {v e r t i c e s o f} \Delta \} \rightarrow G / c o n j
$$

which maps $v _ { i }$ to $O _ { i }$ .

This is a more topological version of the construction of Ito and Reid [I-R], which is phrased in terms of valuations and is purely algebraic i.e., invariant under automorphisms of the field $\mathbb { C }$ .

The main properties of the dual correspondence will be given in §4. These will involve some special conjugacy classes in $G$ , which are indexed by the ends of the graph $\Delta$ . There are two ends for the graph $A _ { n }$ and three ends for the graph $D _ { n }$ and $E _ { n }$ .

For this purpose we consider the induced action of $G$ on the projective line $\mathbb { C P } ^ { 1 }$ of lines in $\mathbb { C } ^ { 2 }$ . This action factors through an effective action of the image $H$ of $G$ in the quotient group $P G L ( 2 , \mathbb { C } ) = S L ( 2 , \mathbb { C } ) / \pm 1$ . The quotient $\mathbb { C P } ^ { 1 } / H$ is isomorphic to the projective line, so we have a ramified covering $\pi : \mathbb { C P } ^ { 1 } \to \mathbb { C P } ^ { 1 } / H$ , which is a Galois covering of group $H$ . We note the well-known lemma

Lemma 3.3. (1) If $\Delta$ is of type $A _ { n }$ for $n$ odd, we have: $G { \xrightarrow { \sim } } H$ .

(2) In every other case we have an exact sequence

$$
1 \rightarrow \pm \{1 \} \rightarrow G \rightarrow H \rightarrow 1 \tag {3-2}
$$

There are three ramification points of $\pi$ in $\mathbb { C P } ^ { 1 } / H$ , except in case $A _ { n }$ , when there are only two. We will give a bijection between the ramification set of $\pi$ and the set of ends of $\Delta$ .

For each ramification point $q \in \mathbb { C P } ^ { 1 } / H$ pick a point $\tilde { q } \in \pi ^ { - 1 } ( q )$ which corresponds to a line $l \subset \mathbb { C } ^ { 2 }$ . We have a natural mapping $l  \mathbb { C } ^ { 2 } \to \mathbb { C } ^ { 2 } / G$ . The inclusion $l \backslash \{ 0 \} \hookrightarrow \mathbb { C } ^ { 2 } \backslash \{ 0 \}$ gives a regular mapping

$$
l \setminus \{0 \} \rightarrow X \setminus \{0 \} = \tilde {X} \setminus D. \tag {3-3}
$$

Because the map ${ \tilde { X } }  X$ is proper, it follows that we can extend the mapping (3-3) to a regular mapping $\phi : l  { \tilde { X } }$ . The point $\phi ( 0 )$ of $\tilde { X }$ is independent of the choice of $\tilde { q } \in \pi ^ { - 1 } ( q )$ . Thus to $\tilde { q }$ we have attached the point $x = \phi ( 0 )$ of $\tilde { X }$ . Let $C _ { q }$ be the image of $\phi$ , which only depends on $q$ , not on the choice of $\tilde { q }$ . The map $l \to C _ { q }$ is a ramified Galois covering with Galois group equal to the stabilizer $G _ { l }$ of $l$ in $G$ .

Proposition 3.4. (1) For a ramification point $q \in \mathbb { C P } ^ { 1 } / H$ , the corresponding point $x$ of $\tilde { X }$ belongs to only one divisor $D _ { j }$ . The curve $C _ { q } \subset \tilde { X }$ is a smooth curve which meets $D _ { j }$ transversally.

(2) The vertex $v _ { j }$ is an end of the graph $\Delta$ .   
(3) The map $q \mapsto v _ { j }$ gives a bijection between the set $S$ of ramification points of $\pi : \mathbb { C P } ^ { 1 } \to \mathbb { C P } ^ { 1 } / H$ and the set of ends of $\Delta$ .

Proof. In case of a cyclic group $G$ of order $_ n$ , the statement is easy to prove using the explicit description of $\tilde { X }$ given in $\left[ \mathbf { B r } \right]$ or in [GS-V]. In that case one of the lines $l$ is the line $x = 0$ . There is a covering of $\dot { X }$ by $n - 1$ affine open sets, each of them isomorphic to the affine plane $\mathbb { C } ^ { 2 }$ . Consider the first open set $U _ { 1 }$ with coordinates $( u , v )$ . These can be chosen so that $x = v ^ { n } u ^ { n - 1 }$ and $y = u$ . Then the point $\phi ( 0 )$ is the point $u = 0 , v = 0$ which verifies the statement, as the divisor $v = 0$ is the divisor $D _ { j }$ corresponding to an end of the graph. A similar argument can be applied to the line $y = 0$ . For the other cases one can use the results of Brieskorn $\left[ \mathbf { B r } \right]$ to deduce them from the cyclic case. First we make a preliminary observation concerning the natural action of $\mathbb { C } ^ { * }$ on $\mathbb { C } ^ { 2 }$ by dilations, which induces an algebraic $\mathbb { C } ^ { * }$ -action on $X$ and on $\tilde { X }$ . The punctured lines $l \setminus \{ 0 \} \subset \mathbb { C } ^ { 2 }$ are $\mathbb { C } ^ { * }$ -orbits. Their images $C _ { l } \ \backslash \ \{ \phi ( 0 ) \}$ in $X$ are therefore also $\mathbb { C } ^ { * }$ -orbits, and this describes all the 1-dimensional orbits. Among the orbits of dimension 1, those corresponding to ramification points of $\pi$ are characterized by the fact that the action of $\mathbb { C } ^ { * }$ is not free (the $m$ -th roots of unity act trivially, if $_ { m }$ is the order of $G _ { l }$ ). Now let $Y$ be the blow-up of $o \in X$ . According to $\left[ \mathbf { B r } \right]$ $Y$ has only isolated singularities (as many as the ends of $\Delta$ ) which are rational surface singularities of type $A _ { n }$ . The isomorphism between the germ of $Y$ at such a point $q$ and the germ of $\mathbb { C } ^ { 2 } / \mu _ { n + 1 }$ at $o$ can be made $\mathbb { C } ^ { * }$ -equivariant. Now for the line $l$ corresponding to ramification point, the corresponding limiting point in $Y$ is a fixed point of $\mathbb { C } ^ { * }$ , so it is one of the singular. Furthermore, the corresponding germ of

orbit in the singular surface $\mathbb { C } ^ { 2 } / \mu _ { n + 1 }$ is a special orbit on which $\mathbb { C } ^ { * }$ does not act freely. This special orbit itself corresponding to a line $x = 0$ or $y = 0$ . Now the resolution of singularities $\tilde { X }$ is obtained from $Y$ by minimally resolving each singular point. The effect of this operation is already understood.

Now for any ramification point $q \in S \subset \mathbb { C P } ^ { 1 } / H$ there is a well-defined conjugacy class $V _ { i }$ in $H$ , which is defined as follows. There is a group homomorphism $f : \pi _ { 1 } ( [ \mathbb { C P } ^ { 1 } / H ] \backslash S ) $ $H$ , which is only well-defined up to conjugacy. Take a small loop in $[ \mathbb { C P } ^ { 1 } / H ] \setminus S$ encircling the point $q$ , and let $h _ { i }$ be its image in $G$ . Then $V _ { i }$ is the conjugacy class of $h _ { i }$ . We can now state

Lemma 3.5. The conjugacy class $V _ { i } \subset H$ is the image of the conjugacy class $O _ { i } \subset G$ under the canonical homomorphism $G  H$ .

Proof. Clearly a representative $h _ { i }$ of $V _ { i }$ is the image in $H$ of the generator of the stabilizer $G _ { l }$ of $l$ which admits $e ^ { \frac { 2 \pi i } { s } }$ as an eigenvalue, where $s$ is the order of $G _ { l }$ . This is the same as the image under the group homomorphism

$$
\pi_ {1} ([ l \setminus \{0 \} ] / G _ {l}) \to \pi_ {1} ([ \mathbb {C} ^ {2} \setminus \{0 \} ] / G) \tilde {\to} G \to H
$$

of a small loop in $[ l \setminus \{ 0 \} ] / G _ { l }$ which turns once around the point 0. On the other hand the curve $C _ { q } = \phi ( l ) \subset X$ is the closure of $[ l \setminus \{ 0 \} ] / G _ { l } \subset \tilde { X } \setminus D$ . From Proposition 3.3 we see that the conjugacy class $O _ { i } \subset G$ is represented by a small loop inside this curve which turns once around the point $x = \phi ( 0 )$ .

In case there are three ramification points $q _ { 1 } , q _ { 2 } , q _ { 3 }$ we can choose representatives $h _ { 1 } , h _ { 2 } , h _ { 3 }$ of the three corresponding conjugacy classes in $H$ such that $h _ { 1 } h _ { 2 } h _ { 3 } = 1$ (indeed this relation holds among the conjugacy classes in $\pi _ { 1 } ( [ \mathbb { C P } ^ { 1 } / H ] \setminus S )$ corresponding to the three punctures). it is natural to ask what relation exists among the conjugacy classes in $G$ .

Lemma 3.6. (1) In cases $D _ { n }$ and $E _ { n }$ , the conjugacy classes $C _ { 1 } , C _ { 2 } , C _ { 3 }$ corresponding to the ends $v _ { 1 } , v _ { 2 } , v _ { 3 }$ of the graph $\Delta$ have representatives $g _ { 1 } , g _ { 2 } , g _ { 3 }$ which satisfy

$$
g _ {1} g _ {2} g _ {3} = - 1 \tag {3-4}.
$$

(2) In the case $A _ { n }$ the conjugacy classes $g _ { 1 }$ and $g _ { 2 }$ corresponding to the two ends of ∆ satisfy

$$
g _ {1} g _ {2} = 1 \tag {3-5}.
$$

Proof. This is easily checked using the explicit description of the group $G$ given for instance in [Coxeter] or in [DuVal2].

We state the following result only in the case of a graph with three ends (the case of two ends is simpler and is left to the reader).

Proposition 3.7. (Coxeter) (1) The group H is isomorphic to the abstract group with generators h1,h2, $h _ { 3 }$ and defining relations

$$
h _ {j} ^ {m _ {j}} = 1, h _ {1} h _ {2} h _ {3} = 1 \tag {3-6}
$$

where $m _ { j }$ is the order of $h _ { j }$ in $H$ , which is also equal to the length from $v _ { j }$ to the central vertex $v _ { c e n }$ .

(2) The group $G$ is isomorphic to the abstract group with generators $g _ { 1 } , g _ { 2 }$ , $g _ { 3 }$ and defining relations

$$
g _ {1} ^ {m _ {1}} = g _ {2} ^ {m _ {2}} = g _ {3} ^ {m _ {3}} = g _ {1} g _ {2} g _ {3}, \left(g _ {1} g _ {2} g _ {3}\right) ^ {2} = 1 \tag {3-7}.
$$

Of course the central element $c = g _ { 1 } g _ { 2 } g _ { 3 }$ is of order 2 and corresponds to $- 1 \in$ $S L ( 2 , \mathbb { C } )$ .

# 4. The dual McKay correspondence.

The dual McKay correspondence was introduced in Definition 3.2. It associates to a vertex $v _ { i }$ of $\Delta$ a conjugacy class $O _ { i }$ in $G$ , which is defined topologically as the class of a small loop in $\tilde { X } \setminus D$ encircling the divisor $D _ { i }$ .

The main properties of this correspondence are given in Theorem 1 below. Except in case $A _ { n }$ there is a central vertex $v _ { c e n }$ of $\Delta$ , and there are three branches.

We will use the notion of canonical numbering of the vertices of the tree $\Delta$ . This means that the vertices are numbered $1 , \cdots , r$ and that for any $2 \leq k \leq r$ the corresponding vertices $v _ { 1 } , \cdots v _ { k }$ are the vertices of a subtree. Any canonical numbering gives an ordering of the set of vertices. Such an ordering will be called canonical. This notion was used by vonRandow [vR].

Theorem 4.1. (1) The correspondence $v _ { i } \mapsto C _ { i }$ gives a bijection between the set of vertices of $\Delta$ and the set of non-trivial conjugacy classes of $G$ .

(2) The ends of $\Delta$ correspond to the special conjugacy classes of $G$ .   
(3) (cases $D _ { n }$ , $E _ { n }$ ) The conjugacy class corresponding to the central vertex $v _ { c e n }$ consists of the central element $- 1$ .   
(4) $A$ branch $v _ { 1 } , \cdots , v _ { m }$ of $\Delta$ corresponds to a “geometric progression” $g , g ^ { 2 } , \cdots , g ^ { m }$ .   
(5) Two vertices $v _ { i }$ and $v _ { j }$ belong to the same branch if and only if the corresponding conjugacy classes $C _ { i }$ , $C _ { j }$ have representatives $g _ { i }$ and $g _ { j }$ which commute.   
(6) Two vertices $v _ { i }$ and $v _ { j }$ are joined by an edge if and only there exists a representative $g _ { i }$ of $C _ { i }$ and a representative u of some special conjugacy class such that u commutes with $g _ { i }$ and such that ugi belongs to $C _ { j }$ .

(7) Pick a canonical ordering of the vertices of $\Delta$ . Let $v _ { i }$ be any vertex of $\Delta$ , and let $v _ { j } , v _ { k } , \cdots$ be the ordered set of neighbors of $v _ { i }$ . Then there are representatives $g _ { i } , g _ { j } , \cdots ~ c$ f the corresponding conjugacy classes such that

$$
g _ {i} ^ {2} = g _ {j} g _ {k} \cdot \cdot \cdot . (4 - 1)
$$

(8) For any canonical ordering of the vertices of $\Delta$ , once can choose an element $g _ { i }$ o f each conjugacy class $C _ { i }$ such that (4-1) holds for any vertex, and such that

$g _ { i }$ and $g _ { j }$ commute whenever the vertices $v _ { i }$ and $v _ { j }$ are joined by an edge. (4-2)

Then $G$ is described as an abstract group as the group generated by these elements $g _ { i }$ subject to these two types of relations.

Proof. We have again $G = \pi _ { 1 } ( { \tilde { X } } \setminus D )$ . The fundamental group $\pi _ { 1 } ( \tilde { X } \setminus D )$ has been described by Mumford [Mu] in terms of precisely chosen loops around $D _ { i }$ with class $g _ { i } \in G$ . Mumford proved statement (8). Now by Proposition 3.6 an end $v _ { j }$ of $\Delta$ corresponds to the conjugacy class of some $g _ { j }$ whose order is exactly the length $m _ { j }$ of the branch which ends at $v _ { j }$ . Index the vertices on the branch by $1 , \cdots , m _ { j }$ . Then applying (4-1) inductively, we see that the vertex labeled by $k$ , $1 \leq k \leq m _ { j }$ corresponds to the conjugacy class of $g _ { j } ^ { k }$ . In case $A _ { n - 1 }$ , $G = \mu _ { n }$ , with the vertices labeled linearly by $\{ 1 , \cdots , n - 1 \}$ , we see that the vertex labeled by $k$ corresponds to $e ^ { \frac { 2 \pi i k } { n } }$ , and all statements of the theorem are clear. So we now assume that we are in the case $D _ { n }$ or $E _ { n }$ , which means there is a central vertex $v _ { c e n }$ . Now for $k = m _ { j }$ , we have the other end of the branch, which is the central vertex; the corresponding conjugacy class is represented by $g _ { j } ^ { m _ { j } } = - 1$ mj (cf. Proposition 3.6 (2)). At this point we can describe graphically the dual correspondence.

$$
\begin{array}{c c c c c c} x & & x ^ {2} & & \dots & \\ & & & & & y \\ & & & & & y x \end{array} \qquad (D _ {n})
$$

where $G$ is generated by $x$ and $y$ with defining relations:

$$
x ^ {n - 1} = y ^ {n - 1} = c, c ^ {2} = 1, y x y ^ {- 1} = x ^ {- 1} \tag {4-3}
$$

$$
\begin{array}{c c c c c} x & x ^ {2} & c & y ^ {2} & y \\ & & z \end{array} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad (E _ {6})
$$

where $G$ is generated by $x , y , z$ with defining relations

$$
x ^ {3} = y ^ {3} = z ^ {2} = c, c ^ {2} = 1, x y z = - 1 \tag {4-4}
$$

$$
\begin{array}{c c c c c c c} x & x ^ {2} & x ^ {3} & c & y ^ {2} & y \\ & & z \end{array} \tag {E7}
$$

where $G$ is generated by $x , y , z$ with defining relations

$$
x ^ {4} = y ^ {3} = z ^ {2} = c, c ^ {2} = 1, x y z = - 1 \qquad (4 - 5)
$$

$$
\begin{array}{c c c c c c c c c} x & & x ^ {2} & & x ^ {3} & & x ^ {4} & & c & & y ^ {2} & & y \\ & & & & & & & z & & & \\ & & & & & & & \end{array} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad (E _ {8})
$$

where $G$ is generated by $x , y , z$ with defining relations

$$
x ^ {5} = y ^ {3} = z ^ {2} = c, c ^ {2} = 1, x y z = - 1 \tag {4-6}
$$

The remaining statements can then be checked directly. Since the number of conjugacy classes of $G$ is equal to the number of vertices of $\Delta$ , (1) will follow if we show that distinct vertices $v _ { i } , v _ { j }$ correspond to distinct conjugacy classes. This is easy to see if $v _ { i }$ and $v _ { j }$ are on the same branch. Then the trace of $g ^ { i }$ in the two-dimensional representation $\mathbb { C } ^ { 2 }$ of $G$ i s equal to $2 c o s ( \frac { \pi i } { m } )$ and for $i \neq j$ , $1 \leq i , j \leq m$ we have $\begin{array} { r } { 2 c o s ( \frac { \pi i } { m } ) \ne 2 c o s ( \frac { \pi j } { m } ) } \end{array}$ . Then there are some cases to be considered where vertices on different branches correspond to conjugacy classes of elements of the same order. In case $D _ { n }$ it is easy to see that $y$ and $y x$ are not conjugate. In case $E _ { 6 }$ one checks that $x ^ { 2 }$ and $y ^ { 2 }$ are not conjugate (this is related to the fact that there are two distinct conjugacy classes of rotations of order 3 in the symmetry group of the tetrahedron). This implies that $x$ and $y$ are not conjugate. In case $E _ { 7 }$ one checks that $x ^ { 2 }$ and $y$ are not conjugate, as their images in the symmetry group of the cube are not conjugate: the first is a flip whose axis goes through the center of two faces, the second one a flip whose axis goes through the middle of two edges. Statement (5) is easy to check, and then (6) follows directly.

Part (1) of the theorem is due to Ito and Reid [I-R, Theorem 1.4]. In fact, for an arbitary finite subgroup $G$ of $S U ( n )$ , they establish a bijection between non-trivial conjugacy classes in $G$ and so-called crepant discrete valuations of the quotient variety $\mathbb { C } ^ { n } / G$ .

Statements (3) and (4) were observed by Steinberg [St2]. We note that there is an a priori proof by vonRandow $[ \mathbf { v R } ]$ that the group defined by generators and relations in statement (8) of Theorem 4.1 is indeed independent of the canonical ordering of the vertices of $\Delta$ . Equation (4-1) may be viewed as saying that the assignment $v _ { i } \mapsto g _ { i }$ is a “non-commutative harmonic map”.

# 5. Relation with the McKay correspondence

Gonzalez-Sprinberg and Verdier [GS-V] gave a geometric construction of the McKay corerspondence in terms of the first Chern class of some vector bundles on $\tilde { X }$ . Given any representation of $G$ in a a finite-dimensional vector space $E$ , there is a natural algebraic vector bundle $\mathcal { E }$ over ${ \tilde { X } } \setminus D = X \setminus \{ o \}$ . In terms of locally free sheaves, the locally free sheaf $f _ { * } \mathcal { O } _ { \mathbb { C } ^ { 2 } \backslash \{ 0 \} }$ has an action of $G$ hence it admits a decomposition into irreducible representations of $G$ :

$$
f _ {*} \mathcal {O} _ {\mathbb {C} ^ {2} \backslash \{0 \}} = \oplus_ {E \in I r r (G)} E ^ {\prime} \otimes \mathcal {F} _ {E} \tag {5-1}
$$

where each $\mathcal { F } _ { E }$ is a locally free sheaf. Then $\mathcal { E }$ is the algebraic vector bundle corresponding to $\mathcal { F } _ { E }$ .

We then want to extend the vector bundle $\mathcal { E }$ to $\tilde { X }$ . For this it is enough to extend the locally free sheaf $\mathcal { F } _ { E }$ to $\tilde { X }$ . Giving such an extension for any $E \in I r r ( G )$ amounts to giving an extension of $f _ { * } \mathcal { O } _ { \mathbb { C } ^ { 2 } \backslash \{ 0 \} }$ to a locally free sheaf over $\tilde { X }$ . Let $j : \tilde { X } \setminus D \hookrightarrow \tilde { X }$ be the inclusion. The extension given in [GS-V] and $\left[ \mathbf { K n } \right]$ is the sheaf $\mathcal { A }$ of subalgebras of $j _ { * } f _ { * } \mathcal { O } _ { \mathbb { C } ^ { 2 } \backslash \{ 0 \} }$ generated by $f _ { * } \mathcal { O } _ { \mathbb { C } ^ { 2 } }$ and by $\mathcal { O } _ { \tilde { X } }$ . It is proved in [GS-V] $\left[ \mathbf { K n } \right]$ that this is actually locally free. The McKay correspondence is essentially given by the first Chern class of the vector bundle $\mathcal { E }$ . We have the following

Proposition 5.1. (1) The group $H _ { 2 } ( \tilde { X } , \mathbb { Z } )$ is the free abelian group of rank r generated by the homology classes $[ D _ { i } ]$ of the divisors $D _ { i }$ , for $1 \leq i \leq r$ .

(2) The Picard group $P i c ( \tilde { X } )$ is isomorphic to $H ^ { 2 } ( { \tilde { X } } , \mathbb { Z } )$ , hence to the Z-dual of $H _ { 2 } ( X , \mathbb { Z } ) = \mathbb { Z } ^ { r }$ . The isomorphism $P i c ( { \tilde { X } } ) \to \mathbb { Z } ^ { r }$ maps a line bundle $L$ to the vector $( d e g ( L _ { / D _ { i } } ) )$ .

We identify both $H _ { 2 } ( \tilde { X } , \mathbb { Z } )$ and $H ^ { 2 } ( { \tilde { X } } , \mathbb { Z } )$ with $\mathbb { Z } ^ { r }$ . Let $( e _ { 1 } , \cdots , e _ { r } )$ denote the standard basis of $H ^ { 2 } ( \tilde { X } , \mathbb { Z } ) = \mathbb { Z } ^ { r }$ .

Let $\Lambda$ be the image of the natural injection Since $H _ { 2 } ( \tilde { X } , \mathbb { Z } )$ identifies by Poincar´e duality with the cohomology group $H _ { c } ^ { 2 } ( \tilde { X } , \mathbb { Z } )$ with compact supports, there is a natural map $\kappa : H _ { 2 } ( \tilde { X } , \mathbb { Z } ) \hookrightarrow H ^ { 2 } ( \tilde { X } , \mathbb { Z } )$ .

Then we have

Lemma 5.2. (1) The matrix of $\kappa$ is the opposite of the Cartan matrix $C$ .

(2) $\Lambda$ is a lattice in $H ^ { 2 } ( { \tilde { X } } , \mathbb { Z } )$ . Its index is equal to the connection index of the root system.

For each divisor $D _ { i }$ the class $\kappa [ D _ { i } ] \in H ^ { 2 } ( \tilde { X } , \mathbb { Z } )$ will again be denoted by $[ D _ { i } ]$ . It is the first Chern class of the locally free sheaf $\mathcal { O } ( D _ { i } )$ . It follows from Lemma 5.2 that the classes $[ D _ { i } ]$ form a basis of the $\mathbb { Q }$ -vector space $H ^ { 2 } ( X , \mathbb { Q } )$ . and that we have

$$
e _ {i} = - \sum_ {j} (C ^ {- 1}) _ {i j} [ D _ {j} ] \tag {5-2}
$$

The theorem of [GS-V] can be stated as follows:

Theorem 5.3. (Gonzalez-Sprinberg [GS-V], see also [Kn]) Let $E _ { i }$ be the irreducible representation of $G$ corresponding to the vertex $v _ { i }$ of $\Delta$ . Then the first Chern class of the vector bundle $\mathcal { E } _ { i }$ is equal to the standard vector $e _ { i }$ of $\mathbb { Z } ^ { r }$ .

Theorem 5.3 indeed gives a geometric construction of the McKay correspondence. The proofs of the theorem in [GS-V] and $\mathbf { \left[ K n \right] }$ involve a case by case computation, but there is a uniform proof in [A-V], which furthermore applies in arbitrary characteristic.

Now we will relate the vector bundles $\mathcal { E }$ to vector bundles with integrable connection. We recall the notion of a Deligne vector bundle with meromorphic integrable connection over an algebraic manifold $Z$ with respect to divisor $Y \subset Z$ with normal crossings. Let $V$ be a an algebraic vector bundle over $Z$ . Assume we have an integrable meromorphic connection $\nabla$ on $Z$ , which is holomorphic over $Z \backslash Y$ . Then we say that $( V , \nabla )$ is a Deligne vector bundle with connection if

(1) for any germ of holomorphic section $s$ of $V$ , $\nabla ( s )$ is a holomorphic section of $\Omega _ { Z } ^ { 1 } ( l o g Y ) \otimes V$ , where $\Omega _ { Z } ^ { 1 } ( l o g Y )$ is the sheaf of 1-forms with logarithmic poles (so $\nabla$ has at worst logarithmic poles along $Y$ );   
(2) for any component $Y _ { j }$ of $Y$ , and any eigenvalue $\alpha$ of the residue of $\nabla$ along $Y _ { j }$ , we have:

$$
0 \leq R e (\alpha) <   1 \tag {5-3}
$$

The first Chern class of the vector bundle $V$ is computable in terms of the residues of the connection along the components $Y _ { j }$ of $Y$ . For each $j$ , we have the cohomology class $[ Y _ { j } ] \in H ^ { 2 } ( Z , \mathbb { C } )$ . The residue $R e s _ { Y _ { j } } ( \nabla )$ is a complex number. Then we have:

Proposition 5.4. (Esnault-Verdier, see Appendix B of [E-V]) Assume the vector bundle $V$ with integrable meromorphic connection $\nabla$ satisfies (1) above. Then we have:

$$
c _ {1} (V) = - \sum_ {j} T r R e s _ {Y _ {j}} (\nabla) [ Y _ {j} ] \in H ^ {2} (Z, \mathbb {C}) \qquad \qquad (5 - 4)
$$

In fact, the result is proved in [E-V] for a proper algebraic variety. However, consider an algebraic vector bundle $V$ over $Z$ with integrable meromorphic connection satisfying (1). There exists a smooth compactification $X$ of $X$ such that $( { \bar { X } } \setminus X ) \cup { \bar { Y } }$ is a divisor with normal crossings. Then it follows from the theory of $\mathbf { [ D e ] }$ that $V$ can be extended to a vector bundle over $\bar { X }$ satisfying (1) with respect to the divisor $( { \bar { X } } \setminus X ) \cup { \bar { Y } }$ . The equality (5-4) for $V$ implies the corresponding equality for $V$ .

Here is an important class of examples of Deligne vector bundles with integrable connection.

Lemma 5.5. Let $Y$ be a divisor with normal crossings in the smooth complex algebraic variety $Z$ . Let $S$ be a normal algebraic variety and let $h : S \to Z$ be a proper morphism such that

(1) $h$ is an ´etale morphism over $Z \backslash Y$ .   
(2) $h _ { * } \mathcal { O } _ { S }$ is a locally free sheaf over $Z$ .

Then the vector bundle associated to $h _ { * } \mathcal { O } _ { S }$ has the natural structure of a Deligne line bundle with integrable connection.

Proof. Over $Z \backslash Y$ we have a unique connection $\nabla$ on $h _ { * } \mathcal { O } _ { S }$ which is compatible with the algebra structure. For any section $u$ of $h _ { * } \mathcal { O } _ { S }$ over an open subset of $Z \backslash Y$ , we can find a polynomial equation $P ( u ) = 0$ , where $\textstyle P ( x ) = x ^ { n } + \sum _ { i = 0 } ^ { n - 1 } a _ { i } x ^ { i }$ is a monic polynomial with coefficients in $O _ { Z }$ such that $P ^ { \prime } ( u )$ is nowhere vanishing. Then we have:

$$
\nabla (u) = \alpha \otimes \frac {1}{P ^ {\prime} (u)},
$$

where $\textstyle \alpha = \sum _ { i } \ d a _ { i } x ^ { i }$ . To prove properties (1)-(2) we work with holomorphic sheaves. Now near a point of $Y$ where $Y$ has local equation $x _ { 1 } \cdots x _ { l } = 0$ , the locally free sheaf $h _ { * } \mathcal { O } _ { S }$ is a direct factor of the sheaf of algebras $\mathcal { O } _ { Z } [ x _ { 1 } ^ { \frac { 1 } { m } } , \cdots , x _ { l } ^ { \frac { 1 } { m } } ]$ for some $m$ . Indeed it is obtained as the subsheaf of invariants under some subgroup of $( \mu _ { m } ) ^ { l }$ . It is therefore enough to treat the case of the sheaf of algebras $\mathcal { O } _ { Z } [ x _ { 1 } ^ { \frac { 1 } { m } } , \cdots , x _ { l } ^ { \frac { 1 } { m } } ]$ . This has a basis consisting of functions of the type $u = x _ { 1 } ^ { \frac { q _ { 1 } } { m } } \cdot \cdot \cdot x _ { l } ^ { \frac { q _ { l } } { m } }$ m · · · x ml for $0 \leq q _ { j } \leq m - 1$ . Then we have

$$
\nabla u = \sum_ {j} \frac {q _ {j}}{m} \frac {d x _ {j}}{x _ {j}} \otimes u,
$$

which makes (1) and (2) apparent.

This however does not directly apply to our bundle of algebras over $\tilde { X }$ , because the corresponding sheaf of algebras $\mathcal { A }$ is not integrally closed. We need to introduce the integral closure $\tilde { \cal A }$ . This satisfies all the assumptions of proposition 5.3, at least on $\tilde { X } \setminus T$ , where $T \subset { \tilde { X } }$ is a finite set. Since we are interested in the first Chern class, we may neglect the effect of deleting this finite set. We then have an exact sequence of $G$ -equivariant coherent sheaves on $\tilde { X }$ :

$$
0 \rightarrow \mathcal {A} \rightarrow \tilde {\mathcal {A}} \rightarrow \mathcal {F} \rightarrow 0 \tag {5-5}
$$

for some sheaf $\mathcal { F }$ supported on $Y$ . For the isotypic components associated to $E \in I r r ( G )$ this yields an exact sequence

$$
0 \rightarrow \mathcal {E} \rightarrow \tilde {\mathcal {E}} \rightarrow \mathcal {H} \rightarrow 0 \tag {5-6}
$$

for some coherent sheaf $\mathcal { H }$ supported on $Y$ . For the first Chern classes we obtain

$$
c _ {1} (\mathcal {E}) = c _ {1} (\tilde {\mathcal {E}}) - \sum_ {j = 1} ^ {r} m _ {j} [ D _ {j} ] \tag {5-7}
$$

where $m _ { j } \geq 0$

We can state

Proposition 5.6. Let E be the vector bundle over $\tilde { X }$ associated to an irreducible representation $E$ of $G$ . We have

$$
c _ {1} (\mathcal {E}) = - \sum_ {j = 1} ^ {r} q _ {j} [ D _ {j} ] \text {w i t h} q _ {j} \geq 0 \tag {5-8}
$$

Proof. The vector bundle $\tilde { E }$ has an integrable connection, and is a direct factor of the vector bundle with integrable connection $\mathcal { A }$ . We have from Proposition 5.4 the equality

$$
c _ {1} (\tilde {E}) = - \sum_ {j} \lambda_ {j} [ D _ {j} ],
$$

where $\lambda _ { j }$ is the trace of the residue of the integrable connection along $D _ { j }$ . By Lemma 5.5 all the eigenvalues of the residue have real part $\geq 0$ , so that $R e ( \lambda _ { j } ) \geq 0$ . Thus we get the equality

$$
c _ {1} (\tilde {E}) = - \sum_ {j} (\lambda_ {j} + q _ {j}) [ D _ {j} ],
$$

with $R e ( \lambda _ { j } + q _ { j } ) \geq 0$ . Since the $\lfloor D _ { j } \rfloor$ are linearly independent, it follows that the $\lambda _ { j } + q _ { j }$ are positive rational numbers.

On the other hand we know from Theorem 5.3 that the $q _ { j }$ are (up to sign) equal to the coefficients of the inverse of the Cartan matrix. Therefore we conclude

Corollary 5.7. The coefficients $( C ^ { - 1 } ) _ { i j }$ of the inverse $C ^ { - 1 }$ of the Cartan matrix are all ≥ 0.

This can of course be easily read off the tables in Bourbaki [Bo]. Indeed $( C ^ { - 1 } ) _ { j k }$ is the coefficient of $\alpha _ { j }$ in the fundamental weight $\omega _ { k }$ . This was pointed out to me by Dolgachev. We note the graph-theoretic interpretation of $C ^ { - 1 }$ given by Lusztig and Tits [L-T].

It is actually easy to prove directly that all coefficients of $C ^ { - 1 }$ are positive. Recall that $C = 2 I - A$ where $A$ is the matrix of $\Delta$ . Now the operator norm of $A$ is the norm of the largest eigenvalue, which is well-known to be smaller than 2. Thus we have a convergent series:

$$
C ^ {- 1} = (2 I - A) ^ {- 1} = \frac {1}{2} \sum_ {n \geq 0} 2 ^ {- n} (A ^ {n}) _ {i j} \tag {5-9}
$$

The coefficient $( A ^ { n } ) _ { i j }$ is the number of paths of length $_ n$ from $v _ { i }$ to $v _ { j }$ in $\Delta$ . So it is always $\geq 0$ and given $( i , j )$ there exists $n$ such that $( A ^ { n } ) _ { i j } > 0$ . In fact we have an estimate:

$$
(C ^ {- 1}) _ {i j} \geq \frac {2 ^ {1 - n}}{3} \tag {5-10}
$$

where $_ { n }$ is the distance between the vertices $v _ { i }$ and $v _ { j }$ . This estimate is sharp for the $A _ { 2 }$ case.

Our final result involves both the McKay correspondence and the dual correspondence. Let $g _ { j }$ be a representative of the conjugacy class associated to the divisor $D _ { j }$ . Then we have:

Proposition 5.8. For the irreducible representation $E _ { k }$ of $G$ associated to the vertex $v _ { k }$ of $\Delta$ we have

$$
\det  \left(g _ {j}, E _ {k}\right) = \exp \left(- 2 \pi i \left(C ^ {- 1}\right) _ {j k}\right) \tag {5-11}
$$

Proof. The conjugacy class of the monodromy operator $g _ { j }$ on $E _ { k } ^ { \prime }$ is represented by the operator $e x p ( - 2 \pi i R e s _ { D _ { j } } \nabla )$ , where $\nabla$ is the meromorphic connection on the Deligne vector bundle $\tilde { \mathcal { E } } _ { k }$ ; this is a general property of the residue in the case of semisimple monodromy, proved in $\mathbf { [ D e ] }$ . So we have:

$$
d e t (g _ {j}, E _ {k}) = e x p (- 2 \pi i T r R e s _ {D _ {j}} \nabla).
$$

Now by Proposition 5.4 the trace of the residue is the opposite of the coefficient of $c _ { 1 } ( { L } _ { j } )$ in $c _ { 1 } ( \tilde { \mathcal { E } } _ { k } )$ . This coefficient is congruent modulo $\mathbb { Z }$ to the similar coefficient for $c _ { 1 } ( \mathcal { E } _ { k } )$ . The latter coefficient is the opposite of the coefficient $( C ^ { - 1 } ) _ { j k }$ of $C ^ { - 1 }$ .

Recall that the connection index of $\Delta$ is equal to the determinant of the Cartan matrix.

Corollary 5.9. The exponent of the abelianization $G ^ { a b }$ of $G$ is equal to the connection index of $\Delta$ .

Proof. Indeed if $_ n$ is the connection index, then all coefficients $( C ^ { - 1 } ) _ { i j }$ belong to $\textstyle { \frac { 1 } { n } } \mathbb { Z }$ . It then follows from (5-11) that any character $G \to \mathbb { C } ^ { * }$ takes values in the $n$ -th roots of unity. So the exponent $_ { m }$ of $G ^ { a b }$ divides $n$ . Now let $n = m q$ ; i it follows from (5-11) that for each coefficient $( C ^ { - 1 } ) _ { i j }$ we have $m ( C ^ { - 1 } ) _ { i j } \in \mathbb { Z }$ . But it is easy to see that the g.c.d of the integers $n ( C ^ { - 1 } ) _ { i j }$ is equal to 1. This implies $q = 1$ and $m = n$ .

This result in fact follows easily from the presentation of the group $G$ in terms of the Cartan matrix given in [H-N-K].

For instance, the connection index of the diagram $E _ { 8 }$ is equal to 1, which implies that the binary icosahedral group is perfect (a well-known fact, of course).

This gives evidence for the idea that the matrix-valued Fourier transform obtained by combining the two types of correspondences should be very significant geometrically. One easily checks in the $A _ { n }$ case that $( C ^ { - 1 } ) _ { j k }$ is congruent to $\frac { - j k } { n + 1 }$ modulo $\mathbb { Z }$ . Therefore we get an automorphism $F ^ { \prime }$ of the space of functions on $G$ , whose matrix is

$$
F _ {j k} = e x p (\frac {- 2 \pi i j k}{n + 1}) (5 - 1 2).
$$

This is of course the usual Fourier transform on the cyclic group $\mu _ { n + 1 }$ . For $G$ non-abelian, we obtain a matrix-valued Fourier transform; by taking the trace of a representation, we

obtain an automorphism of the space of central functions on $G$ ; however, this is not of finite order, already in the case of the binary octahedral group (case $D _ { 4 }$ ).

This strongly suggests that the main object of interest should be the matrix-valued Fourier transform, not just the scalar-valued Fourier transform.

# REFERENCES

[A] M.Artin, On isolated rational singularities of surfaces, Amer. J. Math. 88 (1966), 129-136   
[A-V] M. Artin and J-L. Verdier, Reflexive modules over rational double points, Math. Ann. 270 (1985), 79-82   
[Bo] N. Bourbaki, Lie Groups and Lie Algebras, Chapters 4,5,6   
[Br] E. Brieskorn, Rationale singularit¨aten komplexer Fl¨achen, Invent. Math. 4 (1968), 336-358   
[Co] H. S. M. Coxeter, Regular Complex Polytopes, Cambridge Univ. Press (1974)   
[De] P. Deligne, Equations Diff´erentielles `a Points Singuliers R´eguliers, Lecture Notes on Math vol. 163 (1970), Springer Verlag   
[Du Val1] P. Du Val, On isolated singularities which do not affect the condition of adjunction, Proc. Cambridge Phil. Soc. 30 (1934), 453-465   
[Du Val2] P. Du Val, Homographies, Quaternions and Rotations, Clarendon Press (1964)   
[E-V] H. Esnault and E. Viewhweg, Logarithmic de Rham complexes and vanishing theorems, Invent. Math. 86 (1986), 161-194   
[GS-V] G. Gonzalez-Sprinberg and J-L. Verdier, Construction g´eom´etrique de la correspondence de McKay, Ann. Sc. ec. Norm. Sup. 16 (1983), 409-449   
[H1] F. Hirzebruch, Uber vierdimensionale Riemmansche Fl¨achen mehr- ¨ -deutiger analytischer Funktionen von zwei komplexer Ver¨anderlichen, Math. Ann. 126 (1953), 1-22   
[H-N-K] F. Hirzebruch, W. D. Neumann and S. S. Koch, Differentiable manifolds and Quadratic Forms, Lecture Notes in Pure and Applied Math. vol 4 , Marcel Dekker (1971)   
[I-R] Y. Ito and M. Reid, The Mckay correspondence for finite subgroups of $S L ( 3 , \mathbb { C } )$ , preprint (1994), al-geom/9411010   
[Kn] H. Kn¨orrer, Group representations and the resolution of rational double points, Contemp. Math. vol. 45 91985), 175-221   
[Ko] B. Kostant, On finite subgroups of $S U ( 2 )$ , simple Lie algebras and the McKay correspondence, Ast´erisque vol. Hors-S´erie (1985), 109-255   
[L-T] G. Lusztig and J. Tits, The inverse of a Cartan matrix, Ann. Univ. Timi¸soara Ser S¸tiint¸. Mat. 30 (1992), no. 1, 17-23   
[McKay1] J. McKay, Graphs, singularities and finite groups, Proc. Symp. Pure Math. 37 (1980), 183-186   
[McKay2] J. McKay, Cartan matrices, finite groups of quaternions, and kleinian singularities, Proc. Amer. Math. Soc. (1981), 153-154   
[Mu] D. Mumford, The topology of normal singularities of an algebraic surface and a criterion for simplicity, Publ. Math. IHES 9 (1961), 23-64

[St1] R. Steinberg, Kleinian singularities and unipotent elements, Proc. Symp. Pure Math. 37 (1980), 265-270   
[St2] R. Steinberg, Subgroups of $S U _ { 2 }$ , Dynkin diagrams and affine Coxeter elements, Pacific Jour. Math. 118 (1985), 587-598   
[vR] R. von Randow, Zur Topologie von dreidimensionalen Baummannifal--tigkeiten, Bonner Math. Schriften 14 (1962)

Penn State University

Department of Mathematics

305 McAllister

University Park, PA. 16802

USA

e-mail:jlb@math.psu.edu