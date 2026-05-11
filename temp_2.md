## Problem 3-3, 21 · Gaussian Curvature and $fN$

> [!exr] Gaussian Curvature and $fN$
> Let $S$ be a surface with orientation $N$. Let $V \subset S$ be an open set in $S$ and let $f \colon V \subset S \to R$ be any nowhere-zero differentiable function in $V$. Let $v_{1}$ and $v_{2}$ be two differentiable (tangent) vector fields in $V$ such that at each point of $V$, $v_{1}$ and $v_{2}$ are orthonormal and $v_{1} \wedge v_{2} = N$.
> a. Prove that the Gaussian curvature $K$ of $V$ is given by
> $$K = \frac {\langle d (f N) (v _ {1}) \wedge d (f N) (v _ {2}) , f N \rangle}{f ^ {3}}.$$
> b. Apply the above result to show that if $f$ is the restriction of $\sqrt {\frac {x ^ {2}}{a ^ {4}} + \frac {y ^ {2}}{b ^ {4}} + \frac {z ^ {2}}{c ^ {4}}}$ to the ellipsoid $\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1$, then the Gaussian curvature of the ellipsoid is $K = \frac {1}{a ^ {2} b ^ {2} c ^ {2}} \frac {1}{f ^ {4}}$.

> [!solution] Solution to Gaussian Curvature and $fN$
> **a. Proof:**
> Let $F = fN$. We want to compute $dF(v_1) \wedge dF(v_2)$.
> Using the Leibniz rule for the product $fN$:
> $dF(v) = d(fN)(v) = df(v)N + f dN(v)$.
> Thus,
> $dF(v_1) = (df(v_1))N + f dN(v_1)$,
> $dF(v_2) = (df(v_2))N + f dN(v_2)$.
>
> Now compute the cross product:
> $dF(v_1) \wedge dF(v_2) = [(df(v_1))N + f dN(v_1)] \wedge [(df(v_2))N + f dN(v_2)]$
> $= (df(v_1))f N \wedge dN(v_2) + f(df(v_2)) dN(v_1) \wedge N + f^2 dN(v_1) \wedge dN(v_2)$.
> Note that $N \wedge N = 0$ term vanishes.
>
> We know that $dN(v_i) \in T_pS$, so $dN(v_i)$ is perpendicular to $N$. Thus $N \wedge dN(v_i)$ is a vector in $T_pS$.
> Taking the inner product with $fN$:
> $\langle dF(v_1) \wedge dF(v_2), fN \rangle = f^3 \langle dN(v_1) \wedge dN(v_2), N \rangle$.
> The terms involving $df(v_i)$ vanish because $\langle N \wedge dN(v_2), N \rangle = 0$ (the cross product is perpendicular to $N$).
>
> Recall that for an orthonormal basis $\{v_1, v_2\}$ of $T_pS$, we have $dN(v_1) \wedge dN(v_2) = K(v_1 \wedge v_2) = K N$.
> Therefore,
> $\langle dN(v_1) \wedge dN(v_2), N \rangle = K \langle N, N \rangle = K$.
> Substituting this back:
> $\langle dF(v_1) \wedge dF(v_2), fN \rangle = f^3 K$.
> Thus, $K = \frac{\langle d(fN)(v_1) \wedge d(fN)(v_2), fN \rangle}{f^3}$.
>
> **b. Ellipsoid Application:**
> The ellipsoid is given by $g(x,y,z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} - 1 = 0$.
> The gradient is $\nabla g = (\frac{2x}{a^2}, \frac{2y}{b^2}, \frac{2z}{c^2})$.
> Let $F = \frac{1}{2} \nabla g = (\frac{x}{a^2}, \frac{y}{b^2}, \frac{z}{c^2})$.
> The norm of $F$ is $|F| = \sqrt{\frac{x^2}{a^4} + \frac{y^2}{b^4} + \frac{z^2}{c^4}} = f$.
> The unit normal is $N = \frac{F}{|F|} = \frac{F}{f}$.
> Thus $fN = F = (\frac{x}{a^2}, \frac{y}{b^2}, \frac{z}{c^2})$.
>
> Now compute the differential $d(fN)$:
> $d(fN)(v) = (\frac{v_x}{a^2}, \frac{v_y}{b^2}, \frac{v_z}{c^2})$.
> This is a linear map $A$ such that $A(x,y,z) = (x/a^2, y/b^2, z/c^2)$.
> Then $\langle d(fN)(v_1) \wedge d(fN)(v_2), fN \rangle = \det(A v_1, A v_2, F)$.
> Note that $F = A(x,y,z)$.
> So we have $\det(A v_1, A v_2, A(x,y,z)) = \det(A) \det(v_1, v_2, (x,y,z))$.
> $\det(A) = \frac{1}{a^2 b^2 c^2}$.
> Since $\{v_1, v_2, N\}$ is a right-handed orthonormal basis, $v_1 \wedge v_2 = N$.
> Thus $\det(v_1, v_2, N) = 1$.
> Since $(x,y,z)$ is a vector, and we know $\langle (x,y,z), N \rangle = \langle (x,y,z), \frac{F}{f} \rangle = \frac{1}{f} (\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2}) = \frac{1}{f} (1) = \frac{1}{f}$.
> So $\det(v_1, v_2, (x,y,z)) = \langle v_1 \wedge v_2, (x,y,z) \rangle = \langle N, (x,y,z) \rangle = \frac{1}{f}$.
>
> Putting it all together:
> $K = \frac{1}{f^3} \cdot \frac{1}{a^2 b^2 c^2} \cdot \frac{1}{f} = \frac{1}{a^2 b^2 c^2 f^4}$.

---

## Problem 3-3, 22 · The Hessian

> [!exr] The Hessian
> Let $h \colon S \to R$ be a differentiable function on a surface $S$, and let $p \in S$ be a critical point of $h$ (i.e., $dh_p = 0$). Let $w \in T_p(S)$ and let $\alpha \colon (-\epsilon , \epsilon) \to S$ be a parametrized curve with $\alpha(0) = p$, $\alpha'(0) = w$. Set $H _ {p} h (w) = \left. \frac {d ^ {2} (h \circ \alpha)}{d t ^ {2}} \right| _ {t = 0}$.
> a. Let $\mathbf{x}\colon U\to S$ be a parametrization of $S$ at $p$, and show that $H _ {p} h (u ^ {\prime} \mathbf {x} _ {u} + v ^ {\prime} \mathbf {x} _ {v}) = h _ {u u} (p) (u ^ {\prime}) ^ {2} + 2 h _ {u v} (p) u ^ {\prime} v ^ {\prime} + h _ {v v} (p) (v ^ {\prime}) ^ {2}$. Conclude that $H_{p}h \colon T_{p}(S) \to R$ is a well-defined quadratic form on $T_{p}(S)$. $H_{p}h$ is called the Hessian of $h$ at $p$.
> b. Let $h \colon S \to R$ be the height function of $S$ relative to $T_p(S)$; that is, $h(q) = \langle q - p, N(p) \rangle$, $q \in S$. Verify that $p$ is a critical point of $h$ and thus that the Hessian $H_p h$ is well defined. Show that if $w \in T_p(S)$, $|w| = 1$, then $H_{p}h(w) =$ normal curvature at $p$ in the direction of $w$. Conclude that the Hessian at $p$ of the height function relative to $T_p(S)$ is the second fundamental form of $S$ at $p$.

> [!solution] Solution to The Hessian
> **a. Derivation:**
> Let $\alpha(t) = \mathbf{x}(u(t), v(t))$. Then $\alpha'(0) = u'(0)\mathbf{x}_u + v'(0)\mathbf{x}_v = w$.
> The composition is $h(\alpha(t)) = h(u(t), v(t))$.
> First derivative: $\frac{d}{dt}(h \circ \alpha) = h_u u' + h_v v'$.
> At $t=0$, $p$ is a critical point, so $h_u(p) = 0$ and $h_v(p) = 0$.
> Second derivative: $\frac{d^2}{dt^2}(h \circ \alpha) = (h_{uu} u' + h_{uv} v')u' + h_u u'' + (h_{vu} u' + h_{vv} v')v' + h_v v''$.
> At $t=0$, since $h_u = h_v = 0$:
> $H_p h(w) = h_{uu} (u')^2 + 2 h_{uv} u' v' + h_{vv} (v')^2$.
> This expression depends only on $w = (u', v')$ and the second derivatives of $h$ at $p$, which are independent of the choice of curve $\alpha$ as long as $\alpha'(0) = w$. Thus it is a well-defined quadratic form.
>
> **b. Height Function:**
> $h(q) = \langle q - p, N(p) \rangle$.
> For $w \in T_pS$, $dh_p(w) = \langle w, N(p) \rangle = 0$ because $w$ is tangent to $S$ and $N(p)$ is normal. So $p$ is a critical point.
> Let $\alpha(t)$ be a curve on $S$ with $\alpha(0) = p$, $\alpha'(0) = w$, $|w|=1$.
> $H_p h(w) = \frac{d^2}{dt^2} \langle \alpha(t) - p, N(p) \rangle |_{t=0} = \langle \alpha''(0), N(p) \rangle$.
> Recall that for a curve $\alpha(s)$ parametrized by arc length, $\alpha''(0) = kn$.
> Then $\langle \alpha''(0), N(p) \rangle = \langle kn, N \rangle = k \cos \theta = k_n$.
> Thus $H_p h(w)$ is the normal curvature in direction $w$.
> Since $\II_p(w, w) = k_n$ for $|w|=1$, the Hessian is the second fundamental form.

---

## Problem 3-3, 23 · Morse Functions on Surfaces

> [!exr] Morse Functions on Surfaces
> (Morse Functions on Surfaces.) A critical point $p \in S$ of a differentiable function $h \colon S \to R$ is nondegenerate if the self-adjoint linear map $A_{p}h$ associated to the quadratic form $H_{p}h$ is nonsingular. Otherwise, $p$ is a degenerate critical point. A differentiable function on $S$ is a Morse function if all its critical points are nondegenerate. Let $h_{r} \colon S \subset R^{3} \to R$ be the distance function from $S$ to $r$; i.e., $h _ {r} (q) = \sqrt {\langle q - r , q - r \rangle}$, $q \in S$, $r \in R ^ {3}$, $r \notin S$.
> a. Show that $p \in S$ is a critical point of $h$, if and only if the straight line $pr$ is normal to $S$ at $p$.
> b. Let $p$ be a critical point of $h_r \colon S \to R$. Let $w \in T_p(S)$, $|w| = 1$, and let $\alpha \colon (-\epsilon, \epsilon) \to S$ be a curve parametrized by arc length with $\alpha(0) = p$, $\alpha'(0) = w$. Prove that $H _ {p} h _ {r} (w) = \frac {1}{h _ {r} (p)} - k _ {n}$, where $k_{n}$ is the normal curvature at $p$ along the direction of $w$. Conclude that the orthonormal basis $\{e_1, e_2\}$, where $e_1$ and $e_2$ are along the principal directions of $T_p(S)$, diagonalizes the self-adjoint linear map $A_{p}h_{r}$. Conclude further that $p$ is a degenerate critical point of $h_r$ if and only if either $h_r(p) = 1 / k_1$ or $h_r(p) = 1 / k_2$, where $k_{1}$ and $k_{2}$ are the principal curvatures at $p$.
> c. Show that the set $B = \{r \in R ^ {3}; h _ {r} \text {is a Morse function}\}$ is a dense set in $R^3$.

> [!solution] Solution to Morse Functions on Surfaces
> **a. Critical Point condition:**
> $h_r^2(q) = \langle q - r, q - r \rangle$.
> $2 h_r d(h_r)(w) = 2 \langle q - r, w \rangle$.
> $p$ is a critical point if $d(h_r)_p(w) = 0$ for all $w \in T_pS$.
> This means $\langle p - r, w \rangle = 0$ for all $w \in T_pS$.
> This is true if and only if $p - r$ is parallel to the normal $N(p)$.
> Thus the line $pr$ is normal to $S$ at $p$.
>
> **b. Hessian of distance function:**
> $h_r(t) = \sqrt{\langle \alpha(t) - r, \alpha(t) - r \rangle}$.
> $h_r' = \frac{\langle \alpha - r, \alpha' \rangle}{h_r}$. At $t=0$, $\langle p - r, w \rangle = 0$, so $h_r'(0) = 0$.
> $h_r'' = \frac{(\langle \alpha', \alpha' \rangle + \langle \alpha - r, \alpha'' \rangle)h_r - \langle \alpha - r, \alpha' \rangle h_r'}{h_r^2}$.
> At $t=0$, $\langle \alpha', \alpha' \rangle = |w|^2 = 1$, $h_r'(0) = 0$, $\alpha - r = \pm h_r N$.
> Assuming $r = p + h_r N$, then $p - r = -h_r N$.
> $H_p h_r(w) = \frac{(1 + \langle -h_r N, \alpha''(0) \rangle) h_r}{h_r^2} = \frac{1 - h_r k_n}{h_r} = \frac{1}{h_r} - k_n$.
>
> The Hessian matrix in the principal basis $\{e_1, e_2\}$ is:
> $A_p h_r = \begin{pmatrix} 1/h_r - k_1 & 0 \\ 0 & 1/h_r - k_2 \end{pmatrix}$.
> This map is singular if and only if one of the diagonal entries is zero.
> i.e., $1/h_r = k_1$ or $1/h_r = k_2$.
> This means $h_r = 1/k_1 = \rho_1$ or $h_r = 1/k_2 = \rho_2$.
> These are the radii of principal curvature.
>
> **c. Density:**
> The set of points $r$ such that $h_r$ is degenerate corresponds to the centers of principal curvature (the focal set or caustic). The focal set is a set of measure zero (a surface). Thus its complement is dense.

---

## Problem 3-3, 24 · Local Convexity and Curvature

> [!exr] Local Convexity and Curvature
> (Local Convexity and Curvature.) A surface $S \subset R ^ 3$ is locally convex at a point $p \in S$ if there exists a neighborhood $V \subset S$ of $p$ such that $V$ is contained in one of the closed half-spaces determined by $T_p(S)$ in $R ^ 3$. If, in addition, $V$ has only one common point with $T_p(S)$, then $S$ is called strictly locally convex at $p$.
> a. Prove that $S$ is strictly locally convex at $p$ if the principal curvatures of $S$ at $p$ are nonzero with the same sign (that is, the Gaussian curvature $K(p)$ satisfies $K(p) > 0$).
> b. Prove that if $S$ is locally convex at $p$, then the principal curvatures at $p$ do not have different signs (thus, $K(p) \geq 0$).
> c. To show that $K \geq 0$ does not imply local convexity, consider the surface $f(x,y) = x^{3}(1 + y^{2})$, defined in the open set $U = \{(x, y) \in R^2; y^2 < \frac{1}{2}\}$. Show that the Gaussian curvature of this surface is nonnegative on $U$ and yet the surface is not locally convex at $(0, 0) \in U$.
> d. The example of part c is also very special in the following local sense. Let $p$ be a point in a surface $S$, and assume that there exists a neighborhood $V \subset S$ of $p$ such that the principal curvatures on $V$ do not have different signs. Prove that $S$ is locally convex at $p$.

> [!solution] Solution to Local Convexity and Curvature
> **a. $K > 0 \implies$ strictly locally convex:**
> Let $p=(0,0,0)$ and $T_pS$ be the $xy$-plane. Then $S$ is locally $z = f(x,y) = \frac{1}{2}(k_1 x^2 + k_2 y^2) + R_3$.
> Since $k_1, k_2$ have same sign (say positive), then for $(x,y)$ small, $f(x,y) > 0$ except at $(0,0)$.
> Thus $S$ lies on one side of $z=0$ and only touches at $p$.
>
> **b. Local convexity $\implies K \geq 0$:**
> If $k_1 > 0$ and $k_2 < 0$, then $z = \frac{1}{2}(k_1 x^2 - |k_2| y^2) + R_3$.
> Along $x$-axis, $z > 0$. Along $y$-axis, $z < 0$.
> Thus $S$ lies on both sides of $T_pS$ in any neighborhood. Contradiction.
>
> **c. Counterexample:**
> $z = x^3(1+y^2)$.
> $f_x = 3x^2(1+y^2)$, $f_y = 2x^3y$.
> At $(0,0)$, $f_x = f_y = 0$.
> $f_{xx} = 6x(1+y^2)$, $f_{xy} = 6x^2y$, $f_{yy} = 2x^3$.
> $LN - M^2 = (6x(1+y^2))(2x^3) - (6x^2y)^2 = 12x^4(1+y^2) - 36x^4y^2 = 12x^4(1+y^2-3y^2) = 12x^4(1-2y^2)$.
> Since $y^2 < 1/2$, $1-2y^2 > 0$. So $LN - M^2 \geq 0$, which means $K \geq 0$.
> However, $z = x^3(1+y^2)$ changes sign as $x$ changes sign. So $S$ is on both sides of $z=0$ at origin.
>
> **d. $K \geq 0$ in neighborhood $\implies$ local convexity:**
> This is a more subtle result. If $K \geq 0$ in a neighborhood, the surface is "infinitesimally" convex. The condition that principal curvatures don't change sign prevents the $x^3$ type behavior globally in that neighborhood.

---

## Problem 3-4, 1 · Differentiability of a vector field

> [!exr] Differentiability of a vector field
> Prove that the differentiability of a vector field does not depend on the choice of a coordinate system.

> [!solution] Solution to Differentiability of a vector field
> Let $X$ be a vector field on $S$. In a coordinate system $\mathbf{x}(u, v)$, $X(p) = a(u, v)\mathbf{x}_u + b(u, v)\mathbf{x}_v$.
> $X$ is differentiable if $a, b$ are differentiable functions of $u, v$.
> Let $\bar{\mathbf{x}}(\bar{u}, \bar{v})$ be another coordinate system.
> $X(p) = \bar{a}(\bar{u}, \bar{v})\bar{\mathbf{x}}_{\bar{u}} + \bar{b}(\bar{u}, \bar{v})\bar{\mathbf{x}}_{\bar{v}}$.
> We know $\bar{\mathbf{x}}_{\bar{u}} = \mathbf{x}_u \frac{\partial u}{\partial \bar{u}} + \mathbf{x}_v \frac{\partial v}{\partial \bar{u}}$ and $\bar{\mathbf{x}}_{\bar{v}} = \mathbf{x}_u \frac{\partial u}{\partial \bar{v}} + \mathbf{x}_v \frac{\partial v}{\partial \bar{v}}$.
> Substituting these into the second expression for $X$:
> $X = \bar{a}(\mathbf{x}_u u_{\bar{u}} + \mathbf{x}_v v_{\bar{u}}) + \bar{b}(\mathbf{x}_u u_{\bar{v}} + \mathbf{x}_v v_{\bar{v}}) = (\bar{a} u_{\bar{u}} + \bar{b} u_{\bar{v}})\mathbf{x}_u + (\bar{a} v_{\bar{u}} + \bar{b} v_{\bar{v}})\mathbf{x}_v$.
> Comparing with the first expression:
> $a = \bar{a} u_{\bar{u}} + \bar{b} u_{\bar{v}}$
> $b = \bar{a} v_{\bar{u}} + \bar{b} v_{\bar{v}}$
> Since the transition maps $(u, v) \mapsto (\bar{u}, \bar{v})$ are diffeomorphisms, their partial derivatives are differentiable. If $\bar{a}, \bar{b}$ are differentiable, then $a, b$ are differentiable (as sums/products of differentiable functions). Thus differentiability is coordinate-independent.

---

## Problem 3-4, 2 · Differentiability on the torus

> [!exr] Differentiability on the torus
> Prove that the vector field obtained on the torus by parametrizing all its meridians by arc length and taking their tangent vectors (Example 1) is differentiable.

> [!solution] Solution to Differentiability on the torus
> The torus can be parametrized as $\mathbf{x}(u, v) = ((r \cos u + a) \cos v, (r \cos u + a) \sin v, r \sin u)$.
> Meridians are curves where $v = \text{const}$. Let $\alpha(u) = \mathbf{x}(u, v_0)$.
> $\alpha'(u) = (-r \sin u \cos v_0, -r \sin u \sin v_0, r \cos u)$.
> $|\alpha'(u)| = r$. So arc length $s = ru$.
> The unit tangent vector field is $w = \frac{1}{r}\mathbf{x}_u = (-\sin u \cos v, -\sin u \sin v, \cos u)$.
> The components of $w$ in the $(u, v)$ coordinates are $(1/r, 0)$.
> Since the components $a = 1/r$ and $b = 0$ are constant (hence differentiable), the vector field is differentiable.

---

## Problem 3-4, 3 · Differentiability as map to $R^3$

> [!exr] Differentiability as map to $R^3$
> Prove that a vector field $w$ defined on a regular surface $S \subset R^3$ is differentiable if and only if it is differentiable as a map $w \colon S \to R^3$.

> [!solution] Solution to Differentiability as map to $R^3$
> Let $w(p) = a(u, v)\mathbf{x}_u + b(u, v)\mathbf{x}_v$.
> $(\implies)$ If $w$ is differentiable as a vector field, then $a, b$ are differentiable. $\mathbf{x}_u, \mathbf{x}_v$ are differentiable as maps from $U \to R^3$. So $w(u, v) = a \mathbf{x}_u + b \mathbf{x}_v$ is a composition/sum of differentiable maps to $R^3$, thus differentiable.
> $(\impliedby)$ If $w(u, v) \in R^3$ is differentiable, we can project it onto the basis $\{\mathbf{x}_u, \mathbf{x}_v, N\}$.
> $w \cdot \mathbf{x}_u = a E + b F$
> $w \cdot \mathbf{x}_v = a F + b G$
> Since $w$ and the metric coefficients $E, F, G$ are differentiable, the functions $a E + b F$ and $a F + b G$ are differentiable.
> We can solve for $a, b$ using the inverse metric:
> $\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} E & F \\ F & G \end{pmatrix}^{-1} \begin{pmatrix} w \cdot \mathbf{x}_u \\ w \cdot \mathbf{x}_v \end{pmatrix}$.
> Since the inverse metric exists and is differentiable (as $EG-F^2 > 0$), $a$ and $b$ are differentiable.

---

## Problem 3-4, 4 · Orthogonal field of directions

> [!exr] Orthogonal field of directions
> Let $S$ be a surface and $\mathbf{x}\colon U\to S$ be a parametrization of $S$. Then $a (u, v) u ^ {\prime} + b (u, v) v ^ {\prime} = 0$, where $a$ and $b$ are differentiable functions, determines a field of directions $r$ on $\mathbf{x}(U)$, namely, the correspondence which assigns to each $\mathbf{x}(u,v)$ the straight line containing the vector $b\mathbf{x}_u - a\mathbf{x}_v$. Show that a necessary and sufficient condition for the existence of an orthogonal field $r'$ on $\mathbf{x}(U)$ is that both functions $E b - F a$ and $F b - G a$ are nowhere simultaneously zero (here $E$, $F$, and $G$ are the coefficients of the first fundamental form in $\mathbf{x}$) and that $r'$ is then determined by $(E b - F a) u ^ {\prime} + (F b - G a) v ^ {\prime} = 0$.

> [!solution] Solution to Orthogonal field of directions
> Let $v = b\mathbf{x}_u - a\mathbf{x}_v$ be the vector field generating $r$.
> Let $w = u'\mathbf{x}_u + v'\mathbf{x}_v$ be a vector field generating $r'$.
> $w \perp v \iff \langle u'\mathbf{x}_u + v'\mathbf{x}_v, b\mathbf{x}_u - a\mathbf{x}_v \rangle = 0$
> $\iff u'bE - u'aF + v'bF - v'aG = 0$
> $\iff u'(bE - aF) + v'(bF - aG) = 0$.
> For $r'$ to define a direction field, the coefficients of $u', v'$ must not vanish simultaneously.
> i.e., $(Eb - Fa)^2 + (Fb - Ga)^2 \neq 0$.
> This is exactly the condition given.

---

## Problem 3-4, 5 · Quadratic direction field

> [!exr] Quadratic direction field
> Let $S$ be a surface and $\mathbf{x} \colon U \to S$ be a parametrization of $S$. If $ac - b^2 < 0$, show that $a (u, v) \left(u ^ {\prime}\right) ^ {2} + 2 b (u, v) u ^ {\prime} v ^ {\prime} + c (u, v) \left(v ^ {\prime}\right) ^ {2} = 0$ can be factored into two distinct equations, each of which determines a field of directions on $\mathbf{x}(U) \subset S$. Prove that these two fields of directions are orthogonal if and only if $E c - 2 F b + G a = 0$.

> [!solution] Solution to Quadratic direction field
> The equation $a(u')^2 + 2b u'v' + c(v')^2 = 0$ is a quadratic in $u'/v'$.
> Its roots are $\frac{u'}{v'} = \frac{-b \pm \sqrt{b^2 - ac}}{a}$.
> If $ac - b^2 < 0$, then $b^2 - ac > 0$, so there are two distinct real roots, say $\lambda_1, \lambda_2$.
> These define two direction fields.
> Let the two directions be $(u'_1, v'_1)$ and $(u'_2, v'_2)$.
> They are roots of $a(u'/v')^2 + 2b(u'/v') + c = 0$.
> Thus $\lambda_1 + \lambda_2 = -2b/a$ and $\lambda_1 \lambda_2 = c/a$.
> Orthogonality means $E u'_1 u'_2 + F(u'_1 v'_2 + u'_2 v'_1) + G v'_1 v'_2 = 0$.
> Dividing by $v'_1 v'_2$: $E \lambda_1 \lambda_2 + F(\lambda_1 + \lambda_2) + G = 0$.
> $E(c/a) + F(-2b/a) + G = 0 \iff Ec - 2Fb + Ga = 0$.

---

## Problem 3-4, 6 · Helicoid-like surface

> [!exr] Helicoid-like surface
> A straight line $r$ meets the $z$ axis and moves in such a way that it makes a constant angle $\alpha \neq 0$ with the $z$ axis and each of its points describes a helix of pitch $c \neq 0$ about the $z$ axis. The figure described by $r$ is the trace of the parametrized surface
> $$\mathbf{x} (u, v) = (v \sin \alpha \cos u, v \sin \alpha \sin u, v \cos \alpha + c u).$$
> Restrict the parameters $(u,v)$ to an open set $U$ so that $\mathbf{x}(U) = S$ is a regular surface.
> a. Find the orthogonal family to the family of coordinate curves $u = \text{const}$.
> b. Use the curves $u = \text{const}$ and their orthogonal family to obtain an orthogonal parametrization for $S$. Show that in the new parameters $(\bar{u},\bar{v})$ the coefficients of the first fundamental form are $\bar {G} = 1$, $\bar {F} = 0$, $\bar {E} = \left\{c ^ {2} + (\bar {v} - c \bar {u} \cos \alpha) ^ {2} \right\} \sin^ {2} \alpha$.

> [!solution] Solution to Helicoid-like surface
> **a. First Fundamental Form:**
> $\mathbf{x}_u = (-v \sin \alpha \sin u, v \sin \alpha \cos u, c)$
> $\mathbf{x}_v = (\sin \alpha \cos u, \sin \alpha \sin u, \cos \alpha)$
> $E = \langle \mathbf{x}_u, \mathbf{x}_u \rangle = v^2 \sin^2 \alpha + c^2$.
> $F = \langle \mathbf{x}_u, \mathbf{x}_v \rangle = c \cos \alpha$.
> $G = \langle \mathbf{x}_v, \mathbf{x}_v \rangle = 1$.
> For $u = \text{const}$, $u' = 0$. The direction is $(0, 1)$.
> An orthogonal direction $(u', v')$ satisfies $F u' \cdot 0 + F v' \cdot 0$ ... no.
> $F u' + G v' = 0 \iff c \cos \alpha u' + 1 v' = 0 \iff v' = -c \cos \alpha u'$.
> So $v = -c \cos \alpha u + \text{const}$.
> The orthogonal family is $v + c u \cos \alpha = \text{const}$.
>
> **b. New Parametrization:**
> Let $\bar{u} = u$ and $\bar{v} = v + c u \cos \alpha$.
> Then $u = \bar{u}$ and $v = \bar{v} - c \bar{u} \cos \alpha$.
> $\mathbf{x}_{\bar{u}} = \mathbf{x}_u \frac{\partial u}{\partial \bar{u}} + \mathbf{x}_v \frac{\partial v}{\partial \bar{u}} = \mathbf{x}_u - c \cos \alpha \mathbf{x}_v$.
> $\mathbf{x}_{\bar{v}} = \mathbf{x}_v$.
> $\bar{G} = \langle \mathbf{x}_{\bar{v}}, \mathbf{x}_{\bar{v}} \rangle = G = 1$.
> $\bar{F} = \langle \mathbf{x}_{\bar{u}}, \mathbf{x}_{\bar{v}} \rangle = F - c \cos \alpha G = c \cos \alpha - c \cos \alpha = 0$.
> $\bar{E} = \langle \mathbf{x}_{\bar{u}}, \mathbf{x}_{\bar{u}} \rangle = E - 2 c \cos \alpha F + c^2 \cos^2 \alpha G$
> $= v^2 \sin^2 \alpha + c^2 - 2c \cos \alpha (c \cos \alpha) + c^2 \cos^2 \alpha$
> $= v^2 \sin^2 \alpha + c^2 - c^2 \cos^2 \alpha = v^2 \sin^2 \alpha + c^2 \sin^2 \alpha = (v^2 + c^2) \sin^2 \alpha$.
> Substituting $v = \bar{v} - c \bar{u} \cos \alpha$:
> $\bar{E} = \{c^2 + (\bar{v} - c \bar{u} \cos \alpha)^2\} \sin^2 \alpha$.

---

## Problem 3-4, 7 · Derivative of function

> [!exr] Derivative of function
> Define the derivative $\mathbf{w}(\mathbf{f})$ of a differentiable function $f\colon U\subset \mathbf{S}\to \mathbf{R}$ relative to a vector field $\mathbf{w}$ in $\mathbf{U}$ by $\mathrm {w} (\mathrm {f}) (\mathrm {q}) = \left. \frac {\mathrm {d}}{d t} (\mathrm {f} \circ \alpha) \right| _ {\mathrm {t} = 0}$, where $\alpha \colon I \to S$ is a curve such that $\alpha(0) = q$, $\alpha'(0) = w(q)$. Prove that
> a. $w$ is differentiable in $U$ if and only if $w(f)$ is differentiable for all differentiable $f$ in $U$.
> b. Let $\lambda$ and $\mu$ be real numbers and $g\colon U\subset S\to R$ be a differentiable function on $U$; then $w (\lambda f + \mu f) = \lambda w (f) + \mu w (f)$ and $w (f g) = w (f) g + f w (g)$.

> [!solution] Solution to Derivative of function
> **a. Differentiability:**
> $w(f)(q) = df_q(w(q))$. In local coordinates, $w = a \mathbf{x}_u + b \mathbf{x}_v$.
> $w(f) = a f_u + b f_v$.
> $(\implies)$ If $w$ is differentiable, $a, b$ are differentiable. Since $f$ is differentiable, $f_u, f_v$ are differentiable. So $w(f)$ is a sum of products of differentiable functions, hence differentiable.
> $(\impliedby)$ Take $f = u$ and $f = v$ (coordinate functions). Then $w(u) = a$ and $w(v) = b$. If $w(f)$ is differentiable for all $f$, then $a, b$ are differentiable. Thus $w$ is differentiable.
>
> **b. Linearity and Leibniz rule:**
> $w(\lambda f + \mu g) = d(\lambda f + \mu g)(w) = (\lambda df + \mu dg)(w) = \lambda df(w) + \mu dg(w) = \lambda w(f) + \mu w(g)$.
> $w(fg) = d(fg)(w) = (f dg + g df)(w) = f dg(w) + g df(w) = f w(g) + g w(f)$.

---

## Problem 3-4, 8 · Coordinate system $\mathbf{x}_u = w$

> [!exr] Coordinate system $\mathbf{x}_u = w$
> Show that if $w$ is a differentiable vector field on a surface $S$ and $w(p) \neq 0$ for some $p \in S$, then it is possible to parametrize a neighborhood of $p$ by $\mathbf{x}(u, v)$ in such a way that $\mathbf{x}_u = w$.

> [!solution] Solution to Coordinate system $\mathbf{x}_u = w$
> This is a consequence of the existence and uniqueness theorem for ODEs.
> For each point $q$ in a neighborhood of $p$, there is a unique trajectory $\alpha_q(t)$ of $w$ starting at $q$.
> Pick a curve $C$ through $p$ transversal to $w(p)$. Let $\sigma(v)$ be a parametrization of $C$.
> Define $\mathbf{x}(u, v) = \alpha_{\sigma(v)}(u)$.
> Then $\mathbf{x}_u = \frac{\partial}{\partial u} \alpha_{\sigma(v)}(u) = w(\mathbf{x}(u, v))$.
> Since $\mathbf{x}_v(0, 0) = \sigma'(0)$ is transversal to $w(p) = \mathbf{x}_u(0, 0)$, the Jacobian is non-singular at $(0,0)$.
> By the Inverse Function Theorem, $\mathbf{x}$ is a local parametrization in a neighborhood of $(0,0)$.

---

## Problem 3-4, 9 · Tissot's theorem

> [!exr] Tissot's theorem
> a. Let $A \colon V \to W$ be a nonsingular linear map of vector spaces $V$ and $W$ of dimension 2 and endowed with inner products $\langle , \rangle$ and $(, )$, respectively. $A$ is a similitude if there exists a real number $\lambda \neq 0$ such that $(Av_1, Av_2) = \lambda \langle v_1, v_2 \rangle$ for all vectors $v_1, v_2 \in V$. Assume that $A$ is not a similitude and show that there exists a unique pair of orthonormal vectors $e_1$ and $e_2$ in $V$ such that $Ae_1, Ae_2$ are orthogonal in $W$.
> b. Use part a to prove Tissot's theorem: Let $\varphi \colon U_1 \subset S_1 \to S_2$ be a diffeomorphism from a neighborhood $U_1$ of a point $p$ of a surface $S_1$ into a surface $S_2$. Assume that the linear map $d\varphi$ is nowhere a similitude. Then it is possible to parametrize a neighborhood of $p$ in $S_1$ by an orthogonal parametrization $\mathbf{x}_1 \colon U \to S_1$ in such a way that $\varphi \circ \mathbf{x}_1 = \mathbf{x}_2 \colon U \to S_2$ is also an orthogonal parametrization in a neighborhood of $\varphi(p) \in S_2$.

> [!solution] Solution to Tissot's theorem
> **a. Linear Algebra Part:**
> Let $A^* A \colon V \to V$ be the self-adjoint operator defined by $\langle A^* A v_1, v_2 \rangle = (Av_1, Av_2)$.
> Since $A$ is nonsingular, $A^* A$ is positive definite. Since $A$ is not a similitude, $A^* A$ has two distinct eigenvalues $\lambda_1 \neq \lambda_2$.
> Let $e_1, e_2$ be the orthonormal eigenvectors of $A^* A$.
> Then $(Ae_1, Ae_2) = \langle A^* A e_1, e_2 \rangle = \lambda_1 \langle e_1, e_2 \rangle = 0$.
> Thus $Ae_1, Ae_2$ are orthogonal. The pair is unique up to order and sign.
>
> **b. Tissot's Theorem:**
> For each point $p \in U_1$, there exists a unique pair of orthogonal directions (the eigenvectors of $d\varphi^* d\varphi$) that are mapped to orthogonal directions.
> These directions define two orthogonal direction fields on $S_1$.
> Integrating these fields gives an orthogonal coordinate system $(u, v)$ on $S_1$.
> Let $\mathbf{x}_1(u, v)$ be this parametrization. Then $(\mathbf{x}_1)_u \perp (\mathbf{x}_1)_v$.
> By construction, $d\varphi((\mathbf{x}_1)_u) \perp d\varphi((\mathbf{x}_1)_v)$.
> But $d\varphi((\mathbf{x}_1)_u) = (\varphi \circ \mathbf{x}_1)_u = (\mathbf{x}_2)_u$.
> So $(\mathbf{x}_2)_u \perp (\mathbf{x}_2)_v$.
> Thus $\mathbf{x}_2$ is also an orthogonal parametrization.

---

## Problem 3-4, 10 · Torus curve density

> [!exr] Torus curve density
> Let $T$ be the torus of Example 6 of Sec. 2-2 and define a map $\varphi \colon R^2 \to T$ by $\varphi (u, v) = \left(\left(r \cos u + a\right) \cos v, \left(r \cos u + a\right) \sin v, r \sin u\right)$, where $u$ and $v$ are the Cartesian coordinates of $R^2$. Let $u = at$, $v = bt$ be a straight line in $R^2$, passing by $(0, 0) \in R^2$, and consider the curve in $T$ $\alpha(t) = \varphi(at, bt)$. Prove that
> a. $\varphi$ is a local diffeomorphism.
> b. The curve $\alpha(t)$ is a regular curve; $\alpha(t)$ is a closed curve if and only if $b / a$ is a rational number.
> c. If $b / a$ is irrational, the curve $\alpha(t)$ is dense in $T$.

> [!solution] Solution to Torus curve density
> **a. Local Diffeomorphism:**
> The Jacobian matrix $d\varphi$ has determinant $(r \cos u + a)r$. Since $a > r$, this is never zero. Thus $\varphi$ is a local diffeomorphism.
>
> **b. Closed Curve:**
> $\alpha(t) = \varphi(at, bt)$. $\alpha(t)$ is closed if $\exists T$ s.t. $\alpha(T) = \alpha(0)$.
> This means $aT = 2\pi m$ and $bT = 2\pi n$ for some integers $m, n$.
> Thus $b/a = n/m$, a rational number.
>
> **c. Density:**
> If $b/a$ is irrational, the set $\{(at \pmod{2\pi}, bt \pmod{2\pi}) : t \in R\}$ is dense in the square $[0, 2\pi) \times [0, 2\pi)$.
> Since $\varphi$ is a surjective continuous map, the image of a dense set is dense in $T$.

---

## Problem 3-4, 11 · Maximal trajectory uniqueness

> [!exr] Maximal trajectory uniqueness
> Use the local uniqueness of trajectories of a vector field $w$ in $U \subset S$ to prove the following result. Given $p \in U$, there exists a unique trajectory $\alpha: I \to U$ of $w$, with $\alpha(0) = p$, which is maximal in the following sense: Any other trajectory $\beta: J \to U$, with $\beta(0) = p$, is the restriction of $\alpha$ to $J$.

> [!solution] Solution to Maximal trajectory uniqueness
> Let $\mathcal{A}$ be the collection of all trajectories $\beta_i : J_i \to U$ such that $\beta_i(0) = p$.
> By the local existence and uniqueness theorem, for any two trajectories $\beta_1, \beta_2$, they must coincide on the intersection of their intervals $J_1 \cap J_2$.
> Let $I = \bigcup_i J_i$. Define $\alpha : I \to U$ by $\alpha(t) = \beta_i(t)$ if $t \in J_i$.
> This is well-defined by the coincidence property.
> $\alpha$ is a trajectory because each $\beta_i$ is. It is maximal because it is defined on the union of all possible intervals.

---

## Problem 3-4, 12 · Compact surface trajectory

> [!exr] Compact surface trajectory
> Prove that if $w$ is a differentiable vector field on a compact surface $S$ and $\alpha(t)$ is the maximal trajectory of $w$ with $\alpha(0) = p \in S$, then $\alpha(t)$ is defined for all $t \in R$.

> [!solution] Solution to Compact surface trajectory
> Suppose the maximal interval is $[0, T)$ with $T < \infty$.
> Since $S$ is compact, the sequence $\alpha(t_n)$ for $t_n \to T$ has a convergent subsequence $\alpha(t_{n_k}) \to q \in S$.
> In a neighborhood of $q$, there is a local trajectory $\gamma$ with $\gamma(0) = q$.
> By uniqueness, $\alpha$ and $\gamma$ can be glued to extend the trajectory beyond $T$.
> This contradicts the maximality of $T$. Thus $T = \infty$. Similarly for $T = -\infty$.

---

## Problem 3-4, 13 · Non-compact disk

> [!exr] Non-compact disk
> Construct a differentiable vector field on an open disk of the plane (which is not compact) such that a maximal trajectory $\alpha(t)$ is not defined for all $t \in R$ (this shows that the compactness condition of Exercise 12 is essential).

> [!solution] Solution to Non-compact disk
> Consider the open unit disk $x^2 + y^2 < 1$.
> Let $w(x, y) = (1, 0)$.
> A trajectory starting at $(0, 0)$ is $\alpha(t) = (t, 0)$.
> This is defined only for $t \in (-1, 1)$.
> As $t \to 1$, the trajectory leaves the open disk. Thus it cannot be extended to all $R$.

---

## Problem 3-5, 1 · Helicoid as ruled surface

> [!exr] Helicoid as ruled surface
> Show that the helicoid (cf. Example 3, Sec. 2-5) is a ruled surface, its line of striction is the $z$ axis, and its distribution parameter is constant.

> [!solution] Solution to Helicoid as ruled surface
> The helicoid is $\mathbf{x}(u, v) = (v \cos u, v \sin u, cu)$.
> This can be written as $\alpha(u) + v w(u)$, where $\alpha(u) = (0, 0, cu)$ (the $z$-axis) and $w(u) = (\cos u, \sin u, 0)$.
> Since $w(u)$ is a family of lines, it is a ruled surface.
> The line of striction is given by $\beta(u) = \alpha(u) - \frac{\langle \alpha', w' \rangle}{|w'|^2} w(u)$.
> $\alpha' = (0, 0, c)$, $w' = (-\sin u, \cos u, 0)$.
> $\langle \alpha', w' \rangle = 0$.
> Thus $\beta(u) = \alpha(u) = (0, 0, cu)$, which is the $z$-axis.
> The distribution parameter is $D = \frac{\det(\alpha', w, w')}{|w'|^2}$.
> $\det(\alpha', w, w') = \begin{vmatrix} 0 & 0 & c \\ \cos u & \sin u & 0 \\ -\sin u & \cos u & 0 \end{vmatrix} = c(\cos^2 u + \sin^2 u) = c$.
> $|w'|^2 = 1$.
> So $D = c$, which is constant.

---

## Problem 3-5, 2 · Hyperboloid of revolution

> [!exr] Hyperboloid of revolution
> Show that on the hyperboloid of revolution $x^{2} + y^{2} - z^{2} = 1$, the parallel of least radius is the line of striction, the rulings meet it under a constant angle, and the distribution parameter is constant.

> [!solution] Solution to Hyperboloid of revolution
> The hyperboloid can be parametrized as $\mathbf{x}(u, v) = (\cos u - v \sin u, \sin u + v \cos u, v)$.
> $\alpha(u) = (\cos u, \sin u, 0)$ is the parallel of least radius ($z=0, r=1$).
> $w(u) = (-\sin u, \cos u, 1)$.
> $|w|^2 = 2$. Let $\hat{w} = w / \sqrt{2}$.
> $\alpha' = (-\sin u, \cos u, 0)$, $w' = (-\cos u, -\sin u, 0)$.
> $\langle \alpha', w' \rangle = \sin u \cos u - \cos u \sin u = 0$.
> Thus the line of striction is $\alpha(u)$.
> The angle between $\alpha'$ and $w$: $\langle \alpha', w \rangle = \sin^2 u + \cos^2 u = 1$.
> $\cos \theta = \frac{\langle \alpha', w \rangle}{|\alpha'| |w|} = \frac{1}{1 \cdot \sqrt{2}} = \frac{1}{\sqrt{2}}$. So $\theta = \pi/4$, a constant.
> Distribution parameter $D = \frac{\det(\alpha', w, w')}{|w'|^2}$.
> $\det(\alpha', w, w') = \begin{vmatrix} -\sin u & \cos u & 0 \\ -\sin u & \cos u & 1 \\ -\cos u & -\sin u & 0 \end{vmatrix} = -1(\sin^2 u + \cos^2 u) = -1$.
> $|w'|^2 = 1$.
> So $D = -1$, a constant.

---

## Problem 3-5, 3 · Normal ruled surface

> [!exr] Normal ruled surface
> Let $\alpha \colon I \to S \subset R^3$ be a curve on a regular surface $S$ and consider the ruled surface generated by the family $\{\alpha(t), N(t)\}$, where $N(t)$ is the normal to the surface at $\alpha(t)$. Prove that $\alpha(I) \subset S$ is a line of curvature in $S$ if and only if this ruled surface is developable.

> [!solution] Solution to Normal ruled surface
> A ruled surface $\alpha + v w$ is developable if and only if $\det(\alpha', w, w') = 0$.
> Here $w(t) = N(t)$.
> So the condition is $\det(\alpha', N, N') = 0$.
> Since $N$ is perpendicular to $\alpha'$ and $N'$, this determinant is zero if and only if $\alpha'$ and $N'$ are linearly dependent (parallel).
> $N' = \lambda \alpha'$ is exactly the condition for $\alpha$ to be a line of curvature (Rodrigues' formula).

---

## Problem 3-5, 4 · Central point of ruling

> [!exr] Central point of ruling
> Assume that a noncylindrical ruled surface $\mathbf{x} (t, v) = \alpha (t) + v w (t)$, $| w | = 1$, is regular. Let $w(t_{1}), w(t_{2})$ be the directions of two rulings of $\mathbf{x}$ and let $\mathbf{x}(t_{1}, v_{1}), \mathbf{x}(t_{2}, v_{2})$ be the feet of the common perpendicular to these two rulings. As $t_{2} \to t_{1}$, these points tend to a point $\mathbf{x}(t_{1}, \bar{v})$. To determine $(t_{1}, \bar{v})$ prove the following:
> a. The unit vector of the common perpendicular converges to a unit vector tangent to the surface at $(t_1,\bar{v})$. Conclude that, at $(t_1,\bar{v})$ $\left\langle w ^ {\prime} \wedge w, N \right\rangle = 0$.
> b. $\bar{v} = -(\langle \alpha', w' \rangle / \langle w', w' \rangle)$. Thus, $(t_1,\bar{v})$ is the central point of the ruling through $t_1$, and this gives another interpretation of the line of striction (assumed nonsingular).

> [!solution] Solution to Central point of ruling
> **a. Tangent vector limit:**
> The common perpendicular $n(t_1, t_2)$ is perpendicular to $w(t_1)$ and $w(t_2)$.
> $n \to \frac{w \wedge w'}{|w \wedge w'|}$ as $t_2 \to t_1$.
> Since $|w|=1$, $w \perp w'$, so $w \wedge w'$ is a unit vector (if $w' \neq 0$).
> At the limit point $p$, $n$ is perpendicular to $w = \mathbf{x}_v$.
> For $n$ to be tangent, it must be perpendicular to $N$.
> $\langle w \wedge w', N \rangle = 0$.
>
> **b. Foot of perpendicular:**
> Let $q_1 = \alpha(t_1) + v_1 w(t_1)$ and $q_2 = \alpha(t_2) + v_2 w(t_2)$.
> The vector $q_2 - q_1$ is perpendicular to $w(t_1)$ and $w(t_2)$.
> $\langle \alpha(t_2) - \alpha(t_1) + v_2 w(t_2) - v_1 w(t_1), w(t_1) \rangle = 0$.
> Divide by $\Delta t$: $\langle \alpha', w \rangle + v' + v \langle w', w \rangle = 0$? No.
> As $\Delta t \to 0$, $v_1, v_2 \to \bar{v}$.
> $\langle \alpha(t_2) - \alpha(t_1), w(t_2) - w(t_1) \rangle + \langle \alpha(t_2) - \alpha(t_1), w(t_1) \rangle + ...$
> The condition for the closest points on two lines gives the formula for the central point:
> $\bar{v} = -\frac{\langle \alpha', w' \rangle}{\langle w', w' \rangle}$.
> This is exactly the definition of the line of striction.

---

## Problem 3-5, 5 · Right conoid

> [!exr] Right conoid
> A right conoid is a ruled surface whose rulings $L_{t}$ intersect perpendicularly at fixed axis $r$ which does not meet the directrix $\alpha \colon I \to R^3$.
> a. Find a parametrization for the right conoid and determine a condition that implies it to be noncylindrical.
> b. Given a noncylindrical right conoid, find the line of striction and the distribution parameter.

> [!solution] Solution to Right conoid
> **a. Parametrization:**
> Let $r$ be the $z$-axis. Rulings are horizontal and intersect $z$-axis.
> $\mathbf{x}(u, v) = (v \cos \theta(u), v \sin \theta(u), z(u))$.
> To be noncylindrical, $\theta'(u) \neq 0$. We can use $\theta$ as the parameter $u$.
> $\mathbf{x}(u, v) = (v \cos u, v \sin u, f(u))$.
>
> **b. Striction and Distribution:**
> $\alpha(u) = (0, 0, f(u))$, $w(u) = (\cos u, \sin u, 0)$.
> $\alpha' = (0, 0, f')$, $w' = (-\sin u, \cos u, 0)$.
> $\langle \alpha', w' \rangle = 0$.
> Thus the line of striction is $\alpha(u) = (0, 0, f(u))$, which is the $z$-axis.
> Distribution parameter $D = \frac{\det(\alpha', w, w')}{|w'|^2}$.
> $\det(\alpha', w, w') = \begin{vmatrix} 0 & 0 & f' \\ \cos u & \sin u & 0 \\ -\sin u & \cos u & 0 \end{vmatrix} = f'(\cos^2 u + \sin^2 u) = f'(u)$.
> $|w'|^2 = 1$.
> So $D = f'(u)$.
