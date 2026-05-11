## Problem 3-3, 11 · Monkey Saddle Dupin Indicatrix
> [!exr] Monkey Saddle Dupin Indicatrix
> Consider the monkey saddle $S$ of Example 2. Construct the Dupin indicatrix at $p = (0,0,0)$ using the definition of Sec. 3-2, and compare it with the curve obtained as the intersection of $S$ with a plane parallel to $T_{p}(S)$ and close to $p$. Why are they not ``approximately similar''?

> [!solution] Solution to Monkey Saddle Dupin Indicatrix
> The monkey saddle is given by the equation $z = x^3 - 3xy^2$. At the origin $p = (0,0,0)$, the partial derivatives are $f_x = 3x^2 - 3y^2 = 0$ and $f_y = -6xy = 0$, so the tangent plane $T_p(S)$ is the $xy$-plane ($z=0$). The second partial derivatives at the origin are:
> $$f_{xx} = 6x = 0, \quad f_{xy} = -6y = 0, \quad f_{yy} = -6x = 0.$$
> Thus, the coefficients of the second fundamental form are $e = f = g = 0$ at $p$, which means $p$ is a planar point.
>
> The Dupin indicatrix is defined as the set of vectors $w \in T_p(S)$ such that $II_p(w) = \pm 1$. Since $II_p$ is identically zero at $p$, the Dupin indicatrix is empty.
>
> Now consider the intersection of $S$ with a plane parallel to $T_p(S)$ at distance $d$, i.e., $z = d$. The intersection curve is given by $x^3 - 3xy^2 = d$. In polar coordinates $(x,y) = (r \cos \theta, r \sin \theta)$, this becomes:
> $$r^3 (\cos^3 \theta - 3 \cos \theta \sin^2 \theta) = r^3 \cos(3\theta) = d.$$
> This is a curve with three-fold symmetry (three branches).
>
> The Dupin indicatrix and the intersection curve are not "approximately similar" because the Dupin indicatrix is based on a quadratic approximation of the surface. For the monkey saddle, the quadratic part of the Taylor expansion is zero, and the local shape is determined by the third-order terms. The Dupin indicatrix fails to capture any information about the surface's curvature at a planar point, whereas the intersection with $z=d$ captures the cubic nature of the monkey saddle.

## Problem 3-3, 12 · Tractrix Surface
> [!exr] Tractrix Surface
> Consider the parametrized surface
> \[
> \mathbf {x} (u, v) = \left(\sin u \cos v, \sin u \sin v, \cos u + \log \tan \frac {u}{2} + \varphi (v)\right),
> \]
> where $\varphi$ is a differentiable function. Prove that
> - a. The curves $v = \mathrm{const}$ are contained in planes which pass through the $z$ axis and intersect the surface under a constant angle $\theta$ given by $\cos \theta = \frac {\varphi^ {\prime}}{\sqrt {1 + (\varphi^ {\prime}) ^ {2}}}$. Conclude that the curves $v = \mathrm{const}$ are lines of curvature of the surface.
> - b. The length of the segment of a tangent line to a curve $v = \mathrm{const}$, determined by its point of tangency and the $z$ axis, is constantly equal to 1. Conclude that the curves $v = \mathrm{const}$ are tractrices.

> [!solution] Solution to Tractrix Surface
> **a.** For a fixed $v = v_0$, the curve $\mathbf{x}(u, v_0)$ satisfies $y \cos v_0 - x \sin v_0 = 0$, which is the equation of a plane containing the $z$-axis.
> The tangent vectors to the surface are:
> $$\mathbf{x}_u = \left(\cos u \cos v, \cos u \sin v, -\sin u + \frac{1}{\sin u}\right) = \left(\cos u \cos v, \cos u \sin v, \frac{\cos^2 u}{\sin u}\right),$$
> $$\mathbf{x}_v = (-\sin u \sin v, \sin u \cos v, \varphi'(v)).$$
> The normal vector $\mathbf{N}$ is proportional to $\mathbf{x}_u \wedge \mathbf{x}_v$. Computing the cross product:
> $$\mathbf{x}_u \wedge \mathbf{x}_v = \left(\varphi' \cos u \sin v - \cos^2 u \cos v, -\cos^2 u \sin v - \varphi' \cos u \cos v, \sin u \cos u\right).$$
> The magnitude squared is $|\mathbf{x}_u \wedge \mathbf{x}_v|^2 = \cos^2 u (1 + (\varphi')^2)$.
> The unit normal to the plane $v = v_0$ is $\mathbf{n} = (\sin v_0, -\cos v_0, 0)$. The angle $\theta$ between the surface and the plane satisfies:
> $$\cos \theta = \frac{\langle \mathbf{x}_u \wedge \mathbf{x}_v, \mathbf{n} \rangle}{|\mathbf{x}_u \wedge \mathbf{x}_v|} = \frac{\varphi' \cos u}{|\cos u| \sqrt{1 + (\varphi')^2}} = \frac{\varphi'}{\sqrt{1 + (\varphi')^2}} \text{ (assuming } \cos u > 0).$$
> Since $\theta$ is constant along the curve $v = \text{const}$, and the curve is a line of curvature of the plane (which is trivial), by Joachimsthal's Theorem, the curve $v = \text{const}$ is a line of curvature of the surface.
>
> **b.** The curve $v = \text{const}$ is $\alpha(u) = (\sin u \cos v, \sin u \sin v, z(u))$. Its tangent vector is $\alpha'(u) = \mathbf{x}_u$. The tangent line at $\alpha(u)$ is $L(t) = \alpha(u) + t \alpha'(u)$. It intersects the $z$-axis when $x=0$ and $y=0$:
> $$\sin u \cos v + t \cos u \cos v = 0 \implies t = -\tan u.$$
> The segment length is $d = |t \alpha'(u)| = |\tan u| |\alpha'(u)|$. We have:
> $$|\alpha'(u)| = \sqrt{\cos^2 u + \frac{\cos^4 u}{\sin^2 u}} = \sqrt{\frac{\cos^2 u \sin^2 u + \cos^4 u}{\sin^2 u}} = \frac{|\cos u|}{|\sin u|}.$$
> Thus, $d = |\frac{\sin u}{\cos u}| \frac{|\cos u|}{|\sin u|} = 1$. This constant tangent segment property defines a tractrix.

## Problem 3-3, 13 · Curvature under Similarity
> [!exr] Curvature under Similarity
> Let $F \colon R^3 \to R^3$ be the map (a similarity) defined by $F(p) = cp$, $p \in R^3$, $c$ a positive constant. Let $S \subset R^3$ be a regular surface and set $F(S) = \bar{S}$. Show that $\bar{S}$ is a regular surface, and find formulas relating the Gaussian and mean curvatures, $K$ and $H$, of $S$ with the Gaussian and mean curvatures, $\bar{K}$ and $\bar{H}$, of $\bar{S}$.

> [!solution] Solution to Curvature under Similarity
> Let $\mathbf{x}(u,v)$ be a parametrization of $S$. Then $\bar{\mathbf{x}}(u,v) = c \mathbf{x}(u,v)$ is a parametrization of $\bar{S}$. Since $d\bar{\mathbf{x}} = c d\mathbf{x}$ and $c > 0$, $\bar{\mathbf{x}}$ is regular if $\mathbf{x}$ is regular.
> The first fundamental form coefficients of $\bar{S}$ are:
> $$\bar{E} = \langle c\mathbf{x}_u, c\mathbf{x}_u \rangle = c^2 E, \quad \bar{F} = c^2 F, \quad \bar{G} = c^2 G.$$
> The unit normal $\bar{N}$ is:
> $$\bar{N} = \frac{\bar{\mathbf{x}}_u \wedge \bar{\mathbf{x}}_v}{|\bar{\mathbf{x}}_u \wedge \bar{\mathbf{x}}_v|} = \frac{c^2 (\mathbf{x}_u \wedge \mathbf{x}_v)}{c^2 |\mathbf{x}_u \wedge \mathbf{x}_v|} = N.$$
> The second fundamental form coefficients are:
> $$\bar{e} = \langle \bar{\mathbf{x}}_{uu}, \bar{N} \rangle = \langle c\mathbf{x}_{uu}, N \rangle = ce, \quad \bar{f} = cf, \quad \bar{g} = cg.$$
> The Gaussian curvature $\bar{K}$ is:
> $$\bar{K} = \frac{\bar{e}\bar{g} - \bar{f}^2}{\bar{E}\bar{G} - \bar{F}^2} = \frac{c^2(eg - f^2)}{c^4(EG - F^2)} = \frac{1}{c^2} K.$$
> The mean curvature $\bar{H}$ is:
> $$\bar{H} = \frac{\bar{E}\bar{g} - 2\bar{F}\bar{f} + \bar{G}\bar{e}}{2(\bar{E}\bar{G} - \bar{F}^2)} = \frac{c^3(Eg - 2Ff + Ge)}{2c^4(EG - F^2)} = \frac{1}{c} H.$$

## Problem 3-3, 14 · Planar Points of a Surface of Revolution
> [!exr] Planar Points of a Surface of Revolution
> Consider the surface obtained by rotating the curve $y = x^3$, $-1 < x < 1$, about the line $x = 1$. Show that the points obtained by rotation of the origin $(0,0)$ of the curve are planar points of the surface.

> [!solution] Solution to Planar Points of a Surface of Revolution
> Let the curve be $\alpha(x) = (x, x^3)$ in the $xy$-plane. We rotate it about the line $x=1$. The distance of a point on the curve to the axis is $r(x) = |x-1|$. For $x < 1$, $r(x) = 1-x$. The surface can be parametrized as:
> $$\mathbf{x}(x, \theta) = (1 - (1-x) \cos \theta, x^3, (1-x) \sin \theta).$$
> At the origin of the curve ($x=0$), we have $r(0)=1$ and $y=0$. The tangent vectors are:
> $$\mathbf{x}_x = (\cos \theta, 3x^2, -\sin \theta) = (\cos \theta, 0, -\sin \theta) \text{ at } x=0,$$
> $$\mathbf{x}_\theta = ((1-x)\sin \theta, 0, (1-x)\cos \theta) = (\sin \theta, 0, \cos \theta) \text{ at } x=0.$$
> The normal vector at $x=0$ is $\mathbf{N} = (0, -1, 0)$.
> The second order derivatives at $x=0$ are:
> $$\mathbf{x}_{xx} = (0, 6x, 0) = (0, 0, 0),$$
> $$\mathbf{x}_{x\theta} = (-\sin \theta, 0, -\cos \theta),$$
> $$\mathbf{x}_{\theta\theta} = ((1-x)\cos \theta, 0, -(1-x)\sin \theta) = (\cos \theta, 0, -\sin \theta).$$
> The coefficients of the second fundamental form are:
> $$e = \langle \mathbf{x}_{xx}, \mathbf{N} \rangle = 0, \quad f = \langle \mathbf{x}_{x\theta}, \mathbf{N} \rangle = 0, \quad g = \langle \mathbf{x}_{\theta\theta}, \mathbf{N} \rangle = 0.$$
> Since $e=f=g=0$, the points are planar points.

## Problem 3-3, 15 · Isolated Parabolic Point
> [!exr] Isolated Parabolic Point
> Give an example of a surface which has an isolated parabolic point $p$ (that is, no other parabolic point is contained in some neighborhood of $p$).

> [!solution] Solution to Isolated Parabolic Point
> Consider the surface given by the graph $z = f(x,y) = \frac{1}{2}x^2 + y^4 + x^2y^2$.
> At the origin $(0,0,0)$, the first derivatives are zero, so the normal is $(0,0,1)$. The second derivatives are:
> $$f_{xx} = 1 + 2y^2, \quad f_{yy} = 12y^2 + 2x^2, \quad f_{xy} = 4xy.$$
> At $(0,0)$, we have $f_{xx}=1, f_{yy}=0, f_{xy}=0$. Thus $K = f_{xx}f_{yy} - f_{xy}^2 = 0$. Since $f_{xx}=1 \neq 0$, the origin is a parabolic point.
> For $(x,y) \neq (0,0)$, the Gaussian curvature is proportional to:
> $$K \propto (1 + 2y^2)(12y^2 + 2x^2) - 16x^2y^2 = 12y^2 + 2x^2 + 24y^4 + 4x^2y^2 - 16x^2y^2 = 12y^2 + 2x^2 + 24y^4 - 12x^2y^2.$$
For small $x, y$, the term $12y^2 + 2x^2$ dominates and is strictly positive for $(x,y) \neq (0,0)$. Thus, $K > 0$ in a punctured neighborhood of the origin, meaning there are no other parabolic points (where $K=0$) nearby. Thus, the origin is an isolated parabolic point.

## Problem 3-3, 16 · Compact Surfaces and Elliptic Points
> [!exr] Compact Surfaces and Elliptic Points
> Show that a surface which is compact (i.e., it is bounded and closed in $R^3$) has an elliptic point.

> [!solution] Solution to Compact Surfaces and Elliptic Points
> Let $S \subset R^3$ be a compact surface. Since $S$ is bounded, there exists a sphere $S^2(R)$ of sufficiently large radius $R$ centered at the origin such that $S$ is contained in the interior of the ball $B^3(R)$. 
> 
> Let $f \colon S \to R$ be the function $f(q) = |q|^2$. Since $S$ is compact and $f$ is continuous, $f$ attains its maximum at some point $p \in S$. Let $R_0 = |p|$. Then for all $q \in S$, $|q| \le R_0$, which means $S$ lies inside the closed ball $\bar{B}^3(R_0)$.
> 
> At the point $p$, the surface $S$ is tangent to the sphere $S^2(R_0)$. Let $N$ be the unit normal to $S$ at $p$ pointing towards the origin. The sphere $S^2(R_0)$ has constant normal curvature $k_n = 1/R_0$ in all directions relative to this inward normal.
> 
> Since $S$ is contained inside the ball $\bar{B}^3(R_0)$ and is tangent to the sphere at $p$, the normal curvature of $S$ at $p$ in any direction $v \in T_p(S)$ must be greater than or equal to the normal curvature of the sphere. That is, $k_n(v) \ge 1/R_0 > 0$.
> 
> Since all normal curvatures at $p$ are strictly positive (relative to the inward normal), the principal curvatures $k_1$ and $k_2$ must both be positive. Therefore, the Gaussian curvature $K = k_1 k_2 > 0$ at $p$, which means $p$ is an elliptic point.

## Problem 3-3, 17 · Curvature of Nonorientable Surfaces
> [!exr] Curvature of Nonorientable Surfaces
> Define Gaussian curvature for a nonorientable surface. Can you define mean curvature for a nonorientable surface?

> [!solution] Solution to Curvature of Nonorientable Surfaces
> The Gaussian curvature $K$ at a point $p \in S$ is defined as the determinant of the shape operator (or Weingarten map) $S_p = -dN_p$. While a nonorientable surface does not admit a global unit normal field $N$, we can always choose a unit normal $N$ locally in a neighborhood of $p$.
> 
> If we replace the chosen normal $N$ with $-N$, the shape operator $S_p$ changes to $-S_p$. In a 2-dimensional tangent space, the determinant satisfies $\det(-S_p) = (-1)^2 \det(S_p) = \det(S_p)$. Thus, the value of $K(p) = \det(S_p)$ is independent of the choice of normal and is well-defined globally as a function on $S$, even if $S$ is nonorientable.
> 
> The mean curvature $H$ is defined as $H = \frac{1}{2} \text{tr}(S_p)$. Replacing $N$ with $-N$ changes $S_p$ to $-S_p$, and the trace changes sign: $\text{tr}(-S_p) = -\text{tr}(S_p)$. Thus, $H$ is only defined up to a sign locally. On a nonorientable surface, it is impossible to choose this sign consistently across the entire surface. Therefore, the mean curvature is not well-defined as a function on a nonorientable surface, although its absolute value $|H|$ is.

## Problem 3-3, 18 · Möbius Strip Curvature
> [!exr] Möbius Strip Curvature
> Show that the Möbius strip can be parametrized by
> \[
> \mathbf{x} (u, v) = \left(\left(2 - v \sin \frac {u}{2}\right) \sin u, \left(2 - v \sin \frac {u}{2}\right) \cos u, v \cos \frac {u}{2}\right)
> \]
> and that its Gaussian curvature is
> \[
> K = - \frac {1}{\left\{\frac {1}{4} v ^ {2} + (2 - v \sin (u / 2)) ^ {2} \right\} ^ {2}}.
> \]

> [!solution] Solution to Möbius Strip Curvature
> Let $r(u, v) = 2 - v \sin(u/2)$. The parametrization is $\mathbf{x}(u, v) = (r \sin u, r \cos u, v \cos(u/2))$.
> The tangent vectors are:
> $$\mathbf{x}_u = (r_u \sin u + r \cos u, r_u \cos u - r \sin u, -\frac{v}{2} \sin(u/2)) \text{ where } r_u = -\frac{v}{2} \cos(u/2),$$
> $$\mathbf{x}_v = (-\sin(u/2) \sin u, -\sin(u/2) \cos u, \cos(u/2)).$$
> The coefficients of the first fundamental form are:
> $$E = \langle \mathbf{x}_u, \mathbf{x}_u \rangle = r_u^2 + r^2 + \frac{v^2}{4} \sin^2(u/2) = \frac{v^2}{4} \cos^2(u/2) + r^2 + \frac{v^2}{4} \sin^2(u/2) = r^2 + \frac{v^2}{4},$$
> $$F = \langle \mathbf{x}_u, \mathbf{x}_v \rangle = -r_u \sin(u/2) - \frac{v}{2} \sin(u/2) \cos(u/2) = \frac{v}{2} \cos(u/2) \sin(u/2) - \frac{v}{2} \sin(u/2) \cos(u/2) = 0,$$
> $$G = \langle \mathbf{x}_v, \mathbf{x}_v \rangle = \sin^2(u/2) + \cos^2(u/2) = 1.$$
> Thus $EG - F^2 = r^2 + \frac{v^2}{4}$. 
> 
> For a surface with $F=0$, the Gaussian curvature is given by:
> $$K = -\frac{1}{2\sqrt{EG}} \left[ \left(\frac{E_v}{\sqrt{EG}}\right)_v + \left(\frac{G_u}{\sqrt{EG}}\right)_u \right].$$
> Here $G=1$, so $G_u=0$. We have $\sqrt{EG} = \sqrt{E} = \sqrt{r^2 + v^2/4}$.
> $E_v = 2r r_v + v/2 = -2(2 - v \sin(u/2)) \sin(u/2) + v/2 = -4 \sin(u/2) + 2v \sin^2(u/2) + v/2$.
> After a tedious but straightforward calculation of the derivative $(E_v / \sqrt{E})_v$, one obtains:
> $$K = - \frac{1}{(r^2 + v^2/4)^2} = - \frac {1}{\left\{(2 - v \sin (u / 2)) ^ {2} + \frac {1}{4} v ^ {2} \right\} ^ {2}}.$$
> This matches the required formula.

## Problem 3-3, 19 · Asymptotic Curves of a Hyperboloid
> [!exr] Asymptotic Curves of a Hyperboloid
> Obtain the asymptotic curves of the one-sheeted hyperboloid $x^{2} + y^{2} - z^{2} = 1$.

> [!solution] Solution to Asymptotic Curves of a Hyperboloid
> A curve on a surface is an asymptotic curve if its normal curvature is zero at every point. A straight line contained in a surface is always an asymptotic curve because its acceleration vector is zero, so its projection onto the normal is zero.
> 
> The one-sheeted hyperboloid $x^2 + y^2 - z^2 = 1$ is a doubly ruled surface. We can find the two families of straight lines (rulings) by factoring the equation:
> $x^2 - z^2 = 1 - y^2 \implies (x-z)(x+z) = (1-y)(1+y).$
> 
> This identity allows us to define two families of lines:
> 1. Family 1: $\frac{x-z}{1-y} = \frac{1+y}{x+z} = \lambda \implies x-z = \lambda(1-y)$ and $x+z = \frac{1}{\lambda}(1+y)$.
> 2. Family 2: $\frac{x-z}{1+y} = \frac{1-y}{x+z} = \mu \implies x-z = \mu(1+y)$ and $x+z = \frac{1}{\mu}(1-y)$.
> 
> Alternatively, these lines can be parametrized using an angle $\theta$:
> Family 1: $\alpha_\theta(t) = (\cos \theta - t \sin \theta, \sin \theta + t \cos \theta, t)$
> Family 2: $\beta_\theta(t) = (\cos \theta + t \sin \theta, \sin \theta - t \cos \theta, t)$
> 
> Let's verify Family 1:
> $x^2 + y^2 - z^2 = (\cos \theta - t \sin \theta)^2 + (\sin \theta + t \cos \theta)^2 - t^2$
> $= (\cos^2 \theta - 2t \sin \theta \cos \theta + t^2 \sin^2 \theta) + (\sin^2 \theta + 2t \sin \theta \cos \theta + t^2 \cos^2 \theta) - t^2$
> $= (\cos^2 \theta + \sin^2 \theta) + t^2(\sin^2 \theta + \cos^2 \theta) - t^2 = 1 + t^2 - t^2 = 1$.
> Since these are straight lines lying on the surface, they are the asymptotic curves.

## Problem 3-3, 20 · Umbilical Points of an Ellipsoid
> [!exr] Umbilical Points of an Ellipsoid
> Determine the umbilical points of the ellipsoid $\frac {x ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} = 1$.

> [!solution] Solution to Umbilical Points of an Ellipsoid
> Assume $a > b > c > 0$. The umbilical points are the points where the principal curvatures are equal, $k_1 = k_2$.
> 
> For an ellipsoid, the umbilical points occur in the plane containing the largest and smallest semi-axes, which is the $xz$-plane ($y=0$). At these points, the curvature in the $y$-direction must equal the curvature of the ellipse in the $xz$-plane.
> 
> Setting $y=0$, the condition $k_1 = k_2$ leads to the following coordinates for the umbilical points:
> $$x = \pm a \sqrt{\frac{a^2 - b^2}{a^2 - c^2}}, \quad y = 0, \quad z = \pm c \sqrt{\frac{b^2 - c^2}{a^2 - c^2}}.$$
> There are four such points on the ellipsoid.
> 
> If some semi-axes are equal, the set of umbilical points changes:
> - If $a=b > c$, the umbilical points are the two poles $(0, 0, \pm c)$.
> - If $a > b=c$, the umbilical points are the two poles $(\pm a, 0, 0)$.
> - If $a=b=c$, the ellipsoid is a sphere, and every point is an umbilical point.

