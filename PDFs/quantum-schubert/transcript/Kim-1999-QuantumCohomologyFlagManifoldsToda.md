# ON A NORMALIZATION OF A GRASSMANN MANIFOLD

Maks A. Akivis and Vladislav V. Goldberg

Abstract. On the Grassmann manifold $G ( m , n )$ of $m$ -dimensional subspaces of an $_ n$ -dimensional projective space $P ^ { n }$ , a certain supplementary construction called the normalization is considered. By means of this normalization, one can construct the structure of a Riemannian or semi-Riemannian manifold or an affine connection on $G ( m , n )$ .

1. Let $U$ be an open domain of the Grassmann manifold $G ( m , n )$ of dimension $\rho = ( m + 1 ) ( n - m )$ coinciding with the dimension of $G ( m , n )$ . This domain can coincide with the entire manifold $G ( m , n )$ or can be its proper subset. The domain $U$ is said to be normalized if to each of its -dimensional subspaces $m$ $p$ there corresponds a chosen subspace $p ^ { * }$ of dimension $n - m - 1$ in the projective space $P ^ { n }$ , such that $p ^ { * }$ does not have common points with $p$ . The subspace $p ^ { * }$ is called the normalizing subspace for the subspace $p$ . We will denote a normalized domain $U \subseteq G ( m , n )$ by $U ^ { \nu }$ .

Since the subspace $p ^ { * }$ belongs to the Grassmannian $G ( n - m - 1 , n )$ , a normalization of the manifold $G ( m , n )$ is defined by a normalizing mapping

$$
\nu : G (m, n) \rightarrow G (n - m - 1, n) \tag {1}
$$

given in the domain $U \subseteq G ( m , n )$ and having a domain or a submanifold $U ^ { * }$ of the Grassmannian $G ( n - m - 1 , n )$ as its image. We assume that the mapping $\nu$ is differentiable.

The number $r = \dim U ^ { * }$ coincides with the rank of the mapping $\nu$ . Since $\dim G ( n - m - 1 , n ) = \rho = ( m + 1 ) ( n - m )$ , we have $0 \le r \le \rho$ . If $r = \rho$ , then $U ^ { * }$ is an open domain of the manifold $G ( n - m - 1 , n )$ . If $0 < r < \rho$ , then $U ^ { * }$ is a proper submanifold of $G ( n - m - 1 , n )$ . If $r = 0$ , then $U ^ { * }$ consists of one fixed subspace $p ^ { * }$ of dimension $n - m - 1$ in the projective space $P ^ { n }$ .

If $r ~ = ~ \rho$ , the normalization is called nondegenerate. In this case, there is a one-to-one differentiable correspondence between the domains $U$ and $U ^ { * }$ . If $0 < r < \rho$ , then the complete preimage $\nu ^ { - 1 } ( p ^ { * } )$ of the normalizing subspace $p ^ { * }$ is a differentiable submanifold of dimension $\rho - r$ on the Grassmannian $G ( m , n )$ . If $r = 0$ , then the complete preimage $\nu ^ { - 1 } ( p ^ { * } )$ coincides with the entire domain $U$ .

For $m = 0$ , we arrive at the normalization of the projective space $P ^ { n }$ considered in [N 50], §60.

2. In this paper we will use the following index ranges:

$$
0 \leq \xi , \eta , \zeta \leq n; 0 \leq \alpha , \beta , \gamma , \delta , \epsilon \leq m; m + 1 \leq i, j, k, l \leq n.
$$

Let us write the equations of the normalizing mapping $\nu$ using differential forms. To this end, with the pair of subspaces $p$ and $p ^ { * }$ we associate a family of

point frames $\{ A _ { \xi } \}$ in such a way that $A _ { \alpha } \in p$ and $A _ { i } \in p ^ { * }$ . For each frame of this family, we have

$$
d A _ {\alpha} = \omega_ {\alpha} ^ {\beta} A _ {\beta} + \omega_ {\alpha} ^ {i} A _ {i}, \quad d A _ {i} = \omega_ {i} ^ {\alpha} A _ {\alpha} + \omega_ {i} ^ {j} A _ {j}. \tag {2}
$$

The forms $\omega _ { \xi } ^ { \prime \prime }$ satisfy the structure equations of the projective space $P ^ { n }$ :

$$
d \omega_ {\xi} ^ {\eta} = \omega_ {\xi} ^ {\zeta} \wedge \omega_ {\zeta} ^ {\eta}. \tag {3}
$$

The 1-forms $\omega _ { \alpha } ^ { i }$ are basis forms of the frame bundle associated with the Grassmannian $G ( m , n )$ . The 1-forms $\omega _ { i } ^ { \alpha }$ defining displacements of the subspace $p ^ { * }$ are expressed in terms of the basis forms $\omega _ { i } ^ { \alpha }$ by the relations

$$
\omega_ {i} ^ {\alpha} = \lambda_ {i j} ^ {\alpha \beta} \omega_ {\beta} ^ {j}. \tag {4}
$$

These relations are differential equations of the normalizing mapping (1). The coefficients $\lambda _ { i j } ^ { \alpha \beta }$ form a square matrix of order $\rho = ( m + 1 ) ( n - m )$ , whose rank $r$ is equal to the rank of the mapping $\nu$ : rank $( \lambda _ { i j } ^ { \alpha \beta } ) = r$ .

Next, taking exterior derivatives of equations (4) by means of (3) and applying Cartan’s lemma to the exterior quadratic equations obtained, we find that

$$
\nabla \lambda_ {i j} ^ {\alpha \beta} = \lambda_ {i j k} ^ {\alpha \beta \gamma} \omega_ {\gamma} ^ {k}, \tag {5}
$$

where $\lambda _ { i j k } ^ { \alpha \beta \gamma } = \lambda _ { i k j } ^ { \alpha \gamma \beta }$ and ∇λαβij $\nabla { \lambda } _ { i j } ^ { \alpha \beta } = d { \lambda } _ { i j } ^ { \alpha \beta } - { \lambda } _ { i k } ^ { \alpha \beta } { \omega } _ { j } ^ { k } - { \lambda } _ { k j } ^ { \alpha \beta } { \omega } _ { i } ^ { k } + { \lambda } _ { i j } ^ { \alpha \gamma } { \omega } _ { \gamma } ^ { \beta } + { \lambda } _ { i j } ^ { \gamma \beta } { \omega } _ { \gamma } ^ { \alpha }$ . If we fix an $m$ –pair $( p , p ^ { * } )$ , then equations (5) take the form $\nabla _ { \delta } \lambda _ { i j } ^ { \alpha \beta } = 0$ , where ∇δλαβij $\nabla _ { \delta } \lambda _ { i j } ^ { \alpha \beta } = \nabla \lambda _ { i j } ^ { \alpha \beta } ( \delta )$ αβ and $\delta = d _ { \omega _ { \alpha } ^ { i } = 0 }$ . The last relations show that the coefficients $\lambda _ { i j } ^ { \alpha \beta }$ form a tensor connected with a first order differential neighborhood of the $m$ -pair $( p , p ^ { * } )$ . It is called the fundamental tensor of the normalized domain $U ^ { \nu }$ .

The object $\lambda _ { i j k } ^ { \alpha \beta \gamma }$ occurring in equations (5) is also a tensor connected with a second order differential neighborhood of the normalized Grassmann manifold.

3. In the domain $U ^ { \nu } \subseteq G ( m , n )$ , we consider the quadratic differential form $g = \omega _ { i } ^ { \alpha } \omega _ { \alpha } ^ { i }$ . Substituting the values (4) of the forms $\omega _ { i } ^ { \alpha }$ into the form $g$ , we obtain

$$
g = g _ {i j} ^ {\alpha \beta} \omega_ {\alpha} ^ {i} \omega_ {\beta} ^ {j}, \tag {6}
$$

where the coefficients gαβij $g _ { i j } ^ { \alpha \beta }$ are obtained if one symmetrizes the tensor $\lambda _ { i j } ^ { \alpha \beta }$ simultaneously with respect to both lower and upper pairs of indices: gij $\begin{array} { r } { g _ { i j } ^ { \alpha \beta } = \frac { 1 } { 2 } ( \lambda _ { i j } ^ { \alpha \beta } + \lambda _ { j i } ^ { \beta \alpha } ) } \end{array}$ (λαβij aβ βα). Hence the quantities gαβij $g _ { i j } ^ { \alpha \beta }$ themselves form a tensor which is symmetric with respect to these pairs of indices. In view of this the quadratic differential form $g$ is invariant in the domain $U ^ { \nu }$ .

Denote the rank of the matrix of coefficients of the quadratic form by $\widetilde { r }$ . If $g$ $\widetilde { r } = \rho$ , then the quadratic form $g$ is nondegenerate and defines a Riemannian (or pseudo-Riemannian) metric in the domain $U ^ { \nu }$ . If $\widetilde r < \rho$ , then the form $g$ defines a semi-Riemannian metric in the domain $U ^ { \nu }$ for which the equation gij $g _ { i j } ^ { \alpha \beta } \omega _ { \beta } ^ { j } = 0$ defines an isotropic distribution of dimension $\rho - \widetilde r$ .

The normalization $\nu$ is said to be harmonic if the coefficients in equations (4) are symmetric with respect to the vertical pairs of indices:

$$
\lambda_ {i j} ^ {\alpha \beta} = \lambda_ {j i} ^ {\beta \alpha}. \tag {7}
$$

If this is the case, then gij $g _ { i j } ^ { \alpha \beta } = \lambda _ { i j } ^ { \alpha \beta }$ αβ = λαβij and $\widetilde r = r$ . If $r \ < \ \rho$ , and the normalization $\nu$ is harmonic, then the isotropic distribution defined by the form $g$ is integrable, and its integral manifolds coincide with the complete preimages $\nu ^ { - 1 } ( p ^ { * } )$ of the normalizing subspaces $p ^ { * }$ .

4. Now we will establish a geometric meaning for the quadratic form (6). Consider the subspaces $p = A _ { 0 } \land A _ { 1 } \land \dotsc \land A _ { m }$ and

$$
p ^ {\prime} = \left(A _ {0} + d A _ {0}\right) \wedge \left(A _ {1} + d A _ {1}\right) \wedge \dots \wedge \left(A _ {m} + d A _ {m}\right).
$$

Their matrix coordinates $X$ and $Y$ (see [R 96], Sect. 2.4.1) are rectangular matrices whose columns consist of the coordinates of points, determining the subspaces $p$ and $p ^ { \prime }$ , with respect to the frame ${ \mathcal { R } } = \{ A _ { 0 } , A _ { 1 } , . . . , A _ { n } \}$ . These matrices are

$$
X = \left( \begin{array}{c} I _ {m + 1} \\ O _ {(n - m) \times (m + 1)} \end{array} \right) \quad \text {a n d} \quad Y = \left( \begin{array}{c} \delta_ {\beta} ^ {\alpha} + \omega_ {\beta} ^ {\alpha} \\ \omega_ {\beta} ^ {i} \end{array} \right) \sim \left( \begin{array}{c} \delta_ {\beta} ^ {\alpha} \\ \omega_ {\beta} ^ {i} \end{array} \right), \tag {8}
$$

where $I _ { m + 1 }$ is the identity matrix of order $m + 1$ , $O ( n { - } m ) \times ( m { + } 1 )$ is the rectangular zero $( n - m ) \times ( m + 1 )$ matrix, and the symbol $\sim$ denotes the equivalence of matrices with respect to multiplication from the right by a nondegenerate square matrix $( \delta _ { \beta } ^ { \alpha } - \omega _ { \beta } ^ { \alpha } )$ and discarding second order terms with respect to the entries of the matrix $\left( \omega _ { \xi } ^ { \prime \prime } \right)$ .

Consider further the normalizing subspaces $p ^ { * } = A _ { m + 1 } \land \ldots \land A _ { n }$ and

$$
p ^ {* \prime} = (A _ {m + 1} + d A _ {m + 1}) \wedge \dots \wedge (A _ {n} + d A _ {n}).
$$

It is easy to show that the tangential matrix coordinates $U$ and $V$ of $p$ and $p ^ { * ^ { \prime } }$ , which are defined by the coefficients of linear equations which the coordinates of points determining the subspaces $p *$ and $p ^ { * ^ { \prime } }$ satisfy, can be reduced to the forms:

$$
U = \left( \begin{array}{l l} I _ {m + 1} & O _ {(m + 1) \times (n - m)} \end{array} \right) \quad \text {a n d} \quad V = \left( \begin{array}{l} \delta_ {\beta} ^ {\alpha}, - \omega_ {k} ^ {\alpha} \end{array} \right). \tag {9}
$$

In [R 96] (Sect. 2.4.4) the cross-ratio $W$ of two $m$ -pairs, whose matrix and tangential matrix coordinates are $X , Y$ and $U , V$ , respectively, was defined, and the following formula for its calculation was derived:

$$
W = X (U X) ^ {- 1} (U Y) (V Y) ^ {- 1} V. \tag {10}
$$

From the forms $X , Y , U$ and $V$ , which we already calculated, we find that

$$
U X = U Y = (\delta_ {\beta} ^ {\alpha}), V Y = (\delta_ {\beta} ^ {\alpha} - \omega_ {i} ^ {\alpha} \omega_ {\beta} ^ {i}), (V Y) ^ {- 1} = (\delta_ {\beta} ^ {\alpha} + \omega_ {i} ^ {\alpha} \omega_ {\beta} ^ {i}).
$$

Thus, by applying formula (10), we find that the cross-ratio $W$ of two $m$ -pairs $( p , p ^ { * } )$ and $( p ^ { \prime } , p ^ { * \prime } )$ has the form:

$$
W = \left( \begin{array}{c} \delta_ {\beta} ^ {\alpha} + \omega_ {i} ^ {\alpha} \omega_ {\beta} ^ {i} - \omega_ {k} ^ {\alpha} \\ O _ {(n - m) \times (n + 1)} \end{array} \right). \tag {11}
$$

In the above calculations, we retain the terms of second order with respect to the elements of the matrix $\left( \omega _ { \xi } ^ { \prime I } \right)$ . Since such terms are principal, we discard the terms of order higher than two.

To compute the quadratic form (6), we find the trace of the matrix $W$ . It is: tr $W = m + 1 + \omega _ { i } ^ { \alpha } \omega _ { \alpha } ^ { i }$ . Since for small $x$ we have $\log ( 1 + x ) \sim x$ , it follows that

$$
\mathrm {p r .} \mathrm {p .} \log \Big (1 + \frac {1}{m + 1} \omega_ {i} ^ {\alpha} \omega_ {\alpha} ^ {i} \Big) = \frac {1}{m + 1} \omega_ {i} ^ {\alpha} \omega_ {\alpha} ^ {i},
$$

where pr. p. denotes the principal part of decomposition of the corresponding expression, and as a result, we find that

$$
g = \omega_ {i} ^ {\alpha} \omega_ {\alpha} ^ {i} = (m + 1) \operatorname {p r}. \mathrm {p}. \left[ \log \left(1 + \frac {1}{m + 1} \operatorname {t r} W\right) \right]. \tag {12}
$$

Thus we have proved the following result.

Theorem 1 The quadratic form $g$ is expressed in terms of the cross-ratio of two infinitesimally close $m$ -pairs $( p , p ^ { * } )$ and $( p ^ { \prime } , p ^ { \ast \prime } )$ by formula (12).

5. A normalization of the Grassmann manifold $G ( m , n )$ defines an affine connection on it. In fact, taking the exterior derivatives of the basis forms $\omega _ { \alpha } ^ { i }$ of the manifold $G ( m , n )$ and applying structure equations (3), we obtain

$$
d \omega_ {\alpha} ^ {i} = \omega_ {\alpha} ^ {\beta} \wedge \omega_ {\beta} ^ {i} + \omega_ {\alpha} ^ {j} \wedge \omega_ {j} ^ {i} = \omega_ {\beta} ^ {j} \wedge \left(\delta_ {\alpha} ^ {\beta} \omega_ {j} ^ {i} - \delta_ {j} ^ {i} \omega_ {\alpha} ^ {\beta}\right). \tag {13}
$$

Consider the 1-forms

$$
\omega_ {\alpha j} ^ {i \beta} = \delta_ {\alpha} ^ {\beta} \omega_ {j} ^ {i} - \delta_ {j} ^ {i} \omega_ {\alpha}. \tag {14}
$$

These forms are expressed in terms of the fiber forms $\omega _ { \alpha } ^ { \beta }$ and $\omega _ { j } ^ { i }$ of the frame bundle associated with a domain $U ^ { \nu } \subseteq G ( m , n )$ . In the tangent space $T _ { p } ( \Omega )$ , to the manifold $\Omega ( m , n )$ , which is the image of the manifold $G ( m , n )$ under the Grassmann mapping, these forms define a subgroup of the general linear group whose transformations preserve the cone of asymptotic directions of $G ( m , n )$ determined by the equations $\omega _ { \alpha } ^ { i } \omega _ { \beta } ^ { j } - \omega _ { \alpha } ^ { j } \omega _ { \beta } ^ { i } = 0$ .

Exterior differentiation of equations (14) leads to the exterior equations:

$$
d \omega_ {\alpha j} ^ {i \beta} - \delta_ {\alpha} ^ {\beta} \omega_ {j} ^ {k} \wedge \omega_ {k} ^ {i} + \delta_ {j} ^ {i} \omega_ {\alpha} ^ {\gamma} \wedge \omega_ {\gamma} ^ {\beta} = \delta_ {\alpha} ^ {\beta} \lambda_ {j l} ^ {\gamma \epsilon} \omega_ {\epsilon} ^ {l} \wedge \omega_ {\gamma} ^ {i} - \delta_ {j} ^ {i} \lambda_ {k l} ^ {\beta \epsilon} \omega_ {\alpha} ^ {k} \wedge \omega_ {\epsilon} ^ {l}. \tag {15}
$$

The right-hand sides of equations (15) are expressed only in terms of the basis forms $\omega _ { \alpha } ^ { i }$ of the domain $U ^ { \nu }$ . By the facts from the theory of spaces with affine connection (see, for example, [KN 63], Ch. III), these equations show that the forms $\omega _ { \alpha j } ^ { i \beta }$ define an affine connection on $U ^ { \nu }$ , and the forms occurring in the right-hand sides of (15) are the curvature forms of this connection. Denote this connection by $\Gamma ^ { \nu }$ . The connection $\Gamma ^ { \nu }$ is uniquely determined by the normalization $\nu$ . Note that affine connections on normalized Grassmannians were studied in [Ne 76].

Let us write the curvature forms of the connection $\Gamma ^ { \nu }$ in the form

$$
\Omega_ {\alpha j} ^ {i \beta} = \left(\delta_ {\alpha} ^ {\beta} \delta_ {k} ^ {i} \lambda_ {j l} ^ {\gamma \epsilon} + \delta_ {\alpha} ^ {\gamma} \delta_ {j} ^ {i} \lambda_ {k l} ^ {\beta \epsilon}\right) \omega_ {\epsilon} ^ {l} \wedge \omega_ {\gamma} ^ {k}. \tag {16}
$$

The alternated coefficients occurring in the right-hand sides of the last equations form the curvature tensor of the constructed connection. Equations (16) imply that this tensor has the following form:

$$
R _ {\alpha j k l} ^ {i \beta \gamma \epsilon} = \frac {1}{2} \left(\delta_ {\alpha} ^ {\beta} \delta_ {k} ^ {i} \lambda_ {j l} ^ {\gamma \epsilon} + \delta_ {\alpha} ^ {\gamma} \delta_ {j} ^ {i} \lambda_ {k l} ^ {\beta \epsilon} - \delta_ {\alpha} ^ {\beta} \delta_ {l} ^ {i} \lambda_ {j k} ^ {\epsilon \gamma} - \delta_ {\alpha} ^ {\epsilon} \delta_ {j} ^ {i} \lambda_ {l k} ^ {\beta \gamma}\right), \tag {17}
$$

i.e. this tensor is expressed only in terms of the components of the fundamental tensor of the normalized domain $U ^ { \nu }$ .

Equations (13) show that the affine connection $\Gamma ^ { \nu }$ is torsion-free. In view of this, the following theorem holds:

Theorem 2 The normalization ν of a normalized domain $U ^ { \nu } \subseteq G ( m , n )$ uniquely determines a torsion-free affine connection $\Gamma ^ { \nu }$ with the connection forms (14) on it. The curvature tensor of this connection is linearly expressed in terms of the fundamental tensor of the normalization ν by formulas (17).

Contracting the tensor (17) with respect to the indices $i , l$ and $\alpha , \epsilon$ , we obtain the following expression for the Ricci tensor of the connection $\Gamma ^ { \nu }$ :

$$
R _ {j k} ^ {\beta \gamma} = R _ {\alpha j k i} ^ {i \beta \gamma \alpha} = \frac {1}{2} \left(\lambda_ {j k} ^ {\gamma \beta} + \lambda_ {k j} ^ {\beta \gamma} - (n + 1) \lambda_ {j k} ^ {\beta \gamma}\right). \tag {18}
$$

Equations (18) imply the following result.

Theorem 3 The Ricci tensor of the connection $\Gamma ^ { \nu }$ is symmetric if and only if the normalization ν of the normalized domain $U ^ { \nu }$ is harmonic. $-$

6. It is well-known that a Grassmann manifold $G ( m , n )$ is a homogeneous space. However, in general, a normalized domain $U ^ { \nu }$ is not a homogeneous space. In fact, even two $m$ -pairs $( p , p ^ { * } )$ and $( q , q ^ { * } )$ have a matrix invariant $W$ —their cross-ratio. Thus, in general, there is no projective transformation superposing two neighborhoods $U ( p , p ^ { * } )$ and $\widetilde U ( \widetilde p , \widetilde p ^ { * } )$ of two $m$ -pairs belonging to a normalized domain $U ^ { \nu }$ .

On the other hand, if a normalized domain $U ^ { \nu }$ is homogeneous, then its fundamental tensor determining the location of an $m$ -pair $( p ^ { \prime } , p ^ { * \prime } )$ , which is infinitesimally close to the $m$ -pair $( p , p ^ { * } )$ , must be covariantly constant, i.e. it must satisfy the condition

$$
\nabla \lambda_ {i j} ^ {\alpha \beta} = 0, \tag {19}
$$

where $\nabla$ is the operator of covariant differentiation with respect to the affine connection $\Gamma ^ { \nu }$ .

structure equations (3) and excluding the differentials dλαβij , we arrive at the sys- Taking the exterior derivatives of the system of equations (19) by means of $d \lambda _ { i j } ^ { \alpha \beta }$ tem of relations:

$$
\begin{array}{l} \lambda_ {i k} ^ {\alpha \beta} \lambda_ {j l} ^ {\gamma \epsilon} + \lambda_ {k j} ^ {\alpha \beta} \lambda_ {i l} ^ {\gamma \epsilon} + \lambda_ {i j} ^ {\alpha \gamma} \lambda_ {k l} ^ {\beta \epsilon} + \lambda_ {i j} ^ {\gamma \beta} \lambda_ {k l} ^ {\alpha \epsilon} \\ - \lambda_ {i l} ^ {\alpha \beta} \lambda_ {j k} ^ {\epsilon \gamma} - \bar {\lambda} _ {l j} ^ {\alpha \beta} \lambda_ {i k} ^ {\epsilon \gamma} - \bar {\lambda} _ {i j} ^ {\alpha \epsilon} \lambda_ {l k} ^ {\beta \gamma} - \bar {\lambda} _ {i j} ^ {\epsilon \beta} \lambda_ {l k} ^ {\alpha \gamma} = 0. \\ \end{array}
$$

Thus, the following theorem is valid.

Theorem 4 For the normalization ν of the normalized domain $U ^ { \nu }$ with the fundamental tensor $\lambda _ { i j } ^ { \alpha \beta }$ to be homogeneous it is necessary and sufficient that the tensor $\lambda _ { i j } ^ { \alpha \beta }$ satisfies the conditions (19) and (20).

7. To find a solution of the system of equations (19) and (20), first we consider a polar normalization, i.e. a normalization of the Grassmann manifold $G ( m , n )$ by means of a nondegenerate hyperquadric $Q$ of the space $P ^ { n }$ (see [N 50], §§72–73).

Let $p _ { 0 }$ be an $m$ -dimensional subspace of the space $P ^ { n }$ which is not tangent to $Q$ , and let $p _ { 0 } ^ { * }$ be an $( n - m - 1 )$ -dimensional subspace of $P ^ { n }$ which is polarconjugate to $p _ { 0 }$ with respect $Q$ . The subspaces $p _ { 0 }$ and $p _ { 0 } ^ { * }$ form a nondegenerate $m$ -pair $( p _ { 0 } , p _ { 0 } ^ { * } )$ . The set of subspaces $p$ , located in the same manner with respect to $Q$ as $p _ { 0 }$ (we will clarify below the meaning of the expression “in the same manner”), form an open domain $U$ , and the subspaces $p ^ { * }$ polar-conjugate to the subspaces $p$ with respect to $Q$ define the polar normalization of this domain.

If the hyperquadric $Q$ is imaginary, then the domain $U$ coincides with the entire Grassmann manifold $G ( m , n )$ . Essentially, this case was studied in detail in [L 61] where the Riemannian geometry of the Grassmann manifold of subspaces of an Euclidean vector space was under investigation.

Let us associate a family of projective frames $\{ A _ { \xi } \}$ with an $m$ -pair $( p , p ^ { * } )$ in such a way that the points $A _ { \alpha } \in p$ and $A _ { i } \in p ^ { * }$ . We denote by $( A _ { \xi } , A _ { \eta } )$ the scalar product of the points $A _ { \xi }$ and $A _ { \eta }$ with respect to the hyperquadric $Q$ . Since the points $A _ { \alpha }$ and $A _ { i }$ are polar-conjugate with respect to this hyperquadric, we have

$$
g _ {i \alpha} = \left(A _ {i}, A _ {\alpha}\right) = 0. \tag {21}
$$

The scalar products

$$
\left(A _ {i}, A _ {j}\right) = g _ {i j} \text {a n d} \left(A _ {\alpha}, A _ {\beta}\right) = g _ {\alpha \beta} \tag {22}
$$

form nondegenerate symmetric matrices $\left( g _ { \alpha \beta } \right)$ and (gij ). With respect to any chosen frame, the equation of the hyperquadric $Q$ can be written as

$$
g _ {\alpha \beta} x ^ {\alpha} x ^ {\beta} + g _ {i j} x ^ {i} x ^ {j} = 0. \tag {23}
$$

Moreover, the signature of each of the quadratic forms $g _ { \alpha \beta } x ^ { \alpha } x ^ { \beta }$ and $g _ { i j } x ^ { i } x ^ { j }$ is not changed when the subspace $p$ moves in the normalized domain $U \subseteq G ( m , n )$ . This condition clarifies the meaning of the expression “in the same manner” which we used above to characterize the domain $U$ .

Differentiating equations (21) and (22) by means of equations (2), we find that

$$
\omega_ {i} ^ {\alpha} = - g ^ {\alpha \beta} g _ {i j} \omega_ {\beta} ^ {j}, \nabla g _ {i j} = 0, \nabla g ^ {\alpha \beta} = 0,
$$

where $g ^ { \alpha \beta }$ is the inverse tensor of the tensor $g _ { \alpha \beta }$ . Comparing these with equations (4), we obtain the fundamental tensor of the polar normalization:

$$
\lambda_ {i j} ^ {\alpha \beta} = - g ^ {\alpha \beta} g _ {i j}. \tag {24}
$$

Since the tensors $g ^ { \alpha \beta }$ and $g _ { i j }$ are symmetric, this fundamental tensor satisfies condition (7), and the polar normalization is harmonic. Since the tensors $g ^ { \alpha \beta }$ and $g _ { i j }$ are nondegenerate, the fundamental tensor of the polar normalization is also nondegenerate.

From relations (24) it follows that for the polar normalization we have

$$
\nabla \lambda_ {i j} ^ {\alpha \beta} = 0, \tag {25}
$$

i.e. its fundamental tensor is covariantly constant with respect to the connection $\Gamma ^ { \nu }$ . Hence the polar normalization of the Grassmann manifold is homogeneous.

For the polar normalization, the form (6) can be written as $g = - g ^ { \alpha \beta } g _ { i j } \omega _ { \alpha } ^ { i } \omega _ { \beta } ^ { j }$ Thus, it is nondegenerate and defines a Riemannian (or pseudo-Riemannian) metric on the normalized domain $U ^ { \nu }$ with a polar normalization $\nu$ . By relation (25), the connection $\Gamma ^ { \nu }$ is the Levi-Civita connection defined by this metric.

Substituting values (24) of the fundamental tensor of the polar normalization into expressions (17), we obtain the following expression for the curvature tensor:

$$
R _ {i j k l} ^ {\alpha \beta \gamma \epsilon} = \frac {1}{2} \left(g ^ {\alpha \beta} g ^ {\gamma \epsilon} \left(g _ {i l} g _ {j k} - g _ {i k} g _ {j l}\right) + \left(g ^ {\alpha \epsilon} g ^ {\beta \gamma} - g ^ {\alpha \gamma} g ^ {\beta \epsilon}\right) g _ {i j} g _ {k l}\right). \tag {26}
$$

Substituting values (24) of the components of the fundamental tensor of the polar normalization $\nu$ into (18), we fi that $R _ { j k } ^ { \beta \gamma } = \textstyle { \frac { 1 } { 2 } } ( n - 1 ) g ^ { \beta \gamma } g _ { j k }$ , i.e. the Ricci tensor of a polar-normalized domain $U ^ { \nu }$ is proportional to its metric tensor. But this means that such a polar-normalized Grassmann manifold is an Einstein space.

8. In conclusion, we consider the case when the normalizing mapping $\nu$ has zero rank: $r = 0$ . Then the set of normalizing subspaces consists of a single subspace $p ^ { * }$ of dimension $n - m - 1$ , and the normalized domain $U ^ { \nu } \subseteq G ( m , n )$ consists of the $m$ -dimensional subspaces $p$ not intersecting the normalizing subspace $p ^ { * }$ .

A projective space $P ^ { n }$ , in which a subspace $p ^ { * }$ of dimension $n - m - 1$ is fixed, is called the $m$ -quasiaffine space (see [R 59] and [D 88]) and is denoted by $A _ { m } ^ { n }$ . The basis element of this space is a subspace $p$ , and the entire space coincides with the domain $U ^ { \nu }$ considered above. The stationary subgroup of the element $p$ is the group ${ \cal H } = { \bf G } { \bf L } ( m + 1 ) \times { \bf G } { \bf L } ( n - m )$ .

If we associate a family of point frames with the subspace $p \in U ^ { \nu }$ in the manner indicated in Section 2, then it is easy to prove that $\omega _ { i } ^ { \alpha } = 0$ , and thus $\lambda _ { i j } ^ { \alpha \beta } = 0$ . It addition, it follows from (6) that ows from (17) that $g = 0$ , and the form $_ { g }$ defines no metric in the domain , and the connection is flat. Thus, $U ^ { \nu }$ . In $R _ { \alpha j k l } ^ { i \beta \gamma \epsilon } = 0$ $\Gamma ^ { \nu }$ $U ^ { \nu }$ $A ^ { \rho }$ $\rho = ( m + 1 ) ( n - m )$ . But in this space the stationary subgroup $H$ leaves invariant the Segre cone $S C _ { p }$ with plane generators of dimensions $m + 1$ and $n - m$ . This is the reason that this space is called the Segre-affine space and is denoted by $S A ^ { \rho }$ .

Thus we have proved the following result.

Theorem 5 Let $U ^ { \nu }$ be the domain of the Grassmann manifold $G ( m , n )$ formed by its $m$ -dimensional subspaces $p$ not having common points with a fixed subspace $p ^ { * }$ of dimension $n - m - 1$ (the normalizing subspace). Then the domain $U ^ { \nu }$ admits a mapping onto a Segre-affine space $S A ^ { \rho }$ which preserves the structure of $U ^ { \nu }$ .

The mapping $s \colon U ^ { \nu } \to S A ^ { \rho }$ described in Theorem 5 is called the stereographic projection of the Grassmann manifold $G ( m , n )$ . The stereographic projection of the Grassmann manifold $G ( 1 , 3 )$ was considered in [SR 85], and for the general Grassmann manifold $G ( m , n )$ , it was considered in [S 32] (see also [D 88]). Since the Grassmann manifold $G ( 1 , 3 )$ is equivalent to the pseudoconformal space $C _ { 2 } ^ { 4 }$ , it admits the stereographic projection onto the pseudo-Euclidean space $R _ { 2 } ^ { 4 }$ which is equivalent to the Segre-affine space $S A ^ { 4 }$ .

# References

[D 88] V. A. Dobromyslov, On the geometry of the k-quasiaffine space, Webs and Quasigroups, Kalinin. Gos. Univ., Kalinin, 1988, 147–155.   
[KN 63] S. Kobayashi and K. Nomizu, Foundations of differential geometry, vol. 1, Wiley–Interscience, New York-London-Sydney, 1963, xi+329 pp.   
[L 61] K. Leichtweiss, Zur Riemannschen Geometrie in Grassmannschen Mannigfaltigkeiten, Math. Z. 76 (1961), 334–336.   
[Ne 76] E. G. Neifel’d, Affine connections on a normalized manifold of planes of a projective space, Izv. Vyssh. Uchebn. Zaved. Mat. 1976, no. 11 (174), 48–55 (Russian); English transl. in Soviet Math. (Iz. VUZ) 20 (1976), no. 11.   
[N 50] A. P. Norden, Affinely connected spaces, Gosudarstv. Izdat. Tehn.-Teor. Lit., Moscow-Leningrad, 463 pp. (Russian.) 2d ed., Izdat. “Nauka”, Moscow, 1976, 432 pp.   
[R 59] B. A. Rosenfeld, Quasielliptic spaces, Trudy Moskov. Mat. Obshch. 8 (1959), 49–70 (Russian.)   
[R 96] Rosenfeld, B. A., Geometry of Lie groups, Kluwer Academic Publishers, Dordrecht-Boston-London, 1996 (to appear).   
[S 32] J. G. Semple, On representation of the $S _ { k }$ ’s of $S _ { n }$ and of the Grassmann manifolds $G ( k , n )$ , Proc. London Math. Soc. (2) 32 (1931), 200–221.   
[SR 85] J. G. Semple and L. Roth, Introduction to algebraic geometry, Oxford: Clarendon Press, New York, 1985, xvii+454 pp.

Authors’ addresses:

M. A. Akivis, Department of Mathematics, Ben-Gurion University of the Negev, P.O. Box 653, Beer-Sheva 84105, Israel

E-mail address: akivis@black.bgu.ac.il

V. V. Goldberg, Department of Mathematics, New Jersey Institute of Technology, University Heights, Newark, NJ 07102, U. S. A.

E-mail address: vlgold@numerics.njit.edu