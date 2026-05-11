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
> For small $x, y$, the term $12y^2 + 2x^2$ dominates and is strictly positive for $(x,y) \neq (0,0)$. Thus, $K > 0$ in a punctured neighborhood of the origin, meaning there are no other parabolic points (where $K=0$) nearby. Thus, the origin is an isolated parabolic point.
