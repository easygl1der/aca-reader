## Problem 3-5, 6 · Tangent Plane of a Developable Surface
> [!exr] Tangent Plane of a Developable Surface
> Let $\mathbf{x} (t, v) = \alpha (t) + v w (t)$ be a developable surface. Prove that at a regular point we have $\langle N _ {v}, \mathbf{x} _ {v} \rangle = \langle N _ {v}, \mathbf{x} _ {t} \rangle = 0$. Conclude that the tangent plane of a developable surface is constant along (the regular points of) a fixed ruling.

> [!solution] Solution to Tangent Plane of a Developable Surface
> A ruled surface $\mathbf{x}(t, v) = \alpha(t) + v w(t)$ is developable if and only if its Gaussian curvature $K = 0$ at all regular points. Let $N(t, v)$ be the unit normal vector of the surface.
> 
> First, since $\mathbf{x}_v = w(t)$, the normal vector $N$ is perpendicular to $w(t)$, so $\langle N, w \rangle = 0$. Differentiating this with respect to $v$, and noting that $w$ depends only on $t$ (so $w_v = 0$), we get:
> $$ \langle N_v, w \rangle + \langle N, w_v \rangle = \langle N_v, w \rangle = 0 $$
> Since $\mathbf{x}_v = w$, it follows that $\langle N_v, \mathbf{x}_v \rangle = 0$.
> 
> Second, the coefficients of the second fundamental form for a ruled surface satisfy $n = \langle \mathbf{x}_{vv}, N \rangle = \langle w_v, N \rangle = 0$. The Gaussian curvature is given by $K = \frac{ln - m^2}{EG - F^2}$. For a developable surface, $K = 0$, which implies $m^2 = 0$, so $m = 0$. The coefficient $m$ is given by:
> $$ m = \langle \mathbf{x}_{tv}, N \rangle = -\langle \mathbf{x}_t, N_v \rangle = 0 $$
> Thus, $\langle N_v, \mathbf{x}_t \rangle = 0$.
> 
> Since $\langle N_v, \mathbf{x}_t \rangle = 0$ and $\langle N_v, \mathbf{x}_v \rangle = 0$, and the vectors $\mathbf{x}_t, \mathbf{x}_v$ span the tangent plane at any regular point, $N_v$ must be normal to the tangent plane. Therefore, $N_v$ is parallel to $N$. However, since $|N|^2 = 1$, we have $\langle N_v, N \rangle = 0$. This implies $N_v = 0$ at all regular points.
> 
> Because $N_v = 0$, the normal vector $N(t, v)$ is independent of $v$. This means that along a fixed ruling (where $t$ is constant), the unit normal vector $N$ is constant. Consequently, the tangent plane, which is the plane orthogonal to $N$, is constant along the regular points of the ruling.

## Problem 3-5, 7 · Envelope of Tangent Planes
> [!exr] Envelope of Tangent Planes
> Let $S$ be a regular surface and let $C \subset S$ be a regular curve on $S$, nowhere tangent to an asymptotic direction. Consider the envelope of the family of tangent planes of $S$ along $C$. Prove that the direction of the ruling that passes through a point $p \in C$ is conjugate to the tangent direction of $C$ at $p$.

> [!solution] Solution to Envelope of Tangent Planes
> Let $\alpha(t)$ be a parametrization of the curve $C$ on the surface $S$. The family of tangent planes along $C$ is given by the pairs $\{\alpha(t), N(t)\}$, where $N(t)$ is the unit normal vector of $S$ at $\alpha(t)$. 
> 
> The envelope of a one-parameter family of planes is a developable surface. The ruling direction $w(t)$ of this envelope at the point $\alpha(t)$ is the direction of the intersection of the plane $\langle p - \alpha(t), N(t) \rangle = 0$ and its infinitesimally close neighbor. This intersection is determined by the system:
> $$ \begin{cases} \langle p - \alpha(t), N(t) \rangle = 0 \\ \langle p - \alpha(t), N'(t) \rangle = 0 \end{cases} $$
> (where we use the fact that $\langle \alpha'(t), N(t) \rangle = 0$ for a curve on a surface). The direction $w(t)$ of this intersection is orthogonal to both $N(t)$ and $N'(t)$, so $w(t)$ is parallel to $N(t) \wedge N'(t)$.
> 
> Two directions $v_1, v_2$ in the tangent plane $T_p S$ are conjugate if $\langle dN_p(v_1), v_2 \rangle = 0$. Let $v_1 = \alpha'(t)$ be the tangent direction of $C$. Then $dN_p(\alpha'(t)) = N'(t)$. We check the conjugacy condition for $v_2 = w(t)$:
> $$ \langle dN_p(\alpha'(t)), w(t) \rangle = \langle N'(t), N(t) \wedge N'(t) \rangle $$
> By the properties of the vector triple product, the vector $N \wedge N'$ is orthogonal to $N'$. Thus:
> $$ \langle N'(t), N(t) \wedge N'(t) \rangle = 0 $$
> This proves that the ruling direction $w(t)$ is conjugate to the tangent direction $\alpha'(t)$ of the curve $C$ at point $p$.

## Problem 3-5, 8 · Envelope of Tangent Planes of a Parallel
> [!exr] Envelope of Tangent Planes of a Parallel
> Show that if $C \subset S^2$ is a parallel of unit sphere $S^2$, then the envelope of tangent planes of $S^2$ along $C$ is either a cylinder, if $C$ is an equator, or a cone, if $C$ is not an equator.

> [!solution] Solution to Envelope of Tangent Planes of a Parallel
> On the unit sphere $S^2$, the unit normal at a point $p$ is $N(p) = p$. Let $C$ be a parallel of $S^2$. We can parametrize $C$ by:
> $$ \alpha(t) = (\sin \theta \cos t, \sin \theta \sin t, \cos \theta) $$
> where $\theta \in (0, \pi)$ is constant. Then the normal vector along $C$ is $N(t) = \alpha(t)$. Its derivative is:
> $$ N'(t) = (\sin \theta (-\sin t), \sin \theta \cos t, 0) $$
> The ruling direction $w(t)$ of the envelope is given by $N(t) \wedge N'(t)$:
> $$ w(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \sin\theta\cos t & \sin\theta\sin t & \cos\theta \\ -\sin\theta\sin t & \sin\theta\cos t & 0 \end{vmatrix} = (-\sin\theta\cos\theta\cos t, -\sin\theta\cos\theta\sin t, \sin^2\theta) $$
> This can be simplified to $w(t) = \sin\theta (-\cos\theta\cos t, -\cos\theta\sin t, \sin\theta)$.
> 
> **Case 1: $C$ is the equator ($\theta = \pi/2$).**
> In this case, $\cos\theta = 0$ and $\sin\theta = 1$. The ruling direction becomes $w(t) = (0, 0, 1)$. Since the ruling direction is constant, the developable surface is a cylinder (specifically, the cylinder $x^2 + y^2 = 1$).
> 
> **Case 2: $C$ is not the equator ($\theta \neq \pi/2$).**
> The rulings are lines $L_t(v) = \alpha(t) + v w(t)$. We look for a common intersection point (vertex):
> $$ \alpha(t) + v w(t) = (\sin\theta\cos t(1 - v\cos\theta), \sin\theta\sin t(1 - v\cos\theta), \cos\theta + v\sin^2\theta) $$
> For the $x$ and $y$ coordinates to be zero for all $t$, we must have $1 - v\cos\theta = 0$, so $v = 1/\cos\theta$. Substituting this into the $z$ coordinate:
> $$ z = \cos\theta + \frac{\sin^2\theta}{\cos\theta} = \frac{\cos^2\theta + \sin^2\theta}{\cos\theta} = \frac{1}{\cos\theta} $$
> Thus, all rulings pass through the fixed point $(0, 0, 1/\cos\theta)$. This shows that the envelope is a cone with this vertex.

## Problem 3-5, 9* · Focal Surfaces
> [!exr] Focal Surfaces
> Let $S$ be a regular surface without parabolic or umbilical points. Let $\mathbf{x} \colon U \to S$ be a parametrization of $S$ such that the coordinate curves are lines of curvature. The parametrized surfaces $\mathbf{y} (u, v) = \mathbf{x} (u, v) + \rho_ {1} N (u, v)$ and $\mathbf{z} (u, v) = \mathbf{x} (u, v) + \rho_ {2} N (u, v)$, where $\rho_{1} = 1 / k_{1}$, $\rho_{2} = 1 / k_{2}$, are called focal surfaces of $\mathbf{x}(U)$. Prove that
> - a. If $(k_{1})_{u}$ and $(k_{2})_{v}$ are nowhere zero, then $\mathbf{y}$ and $\mathbf{z}$ are regular parametrized surfaces.
> - b. At the regular points, the directions on a focal surface corresponding to the principal directions on $\mathbf{x}(U)$ are conjugate.
> - c. A focal surface, say $\mathbf{y}$, can be constructed as follows: Consider the line of curvature $\mathbf{x}(u,\mathrm{const.})$ on $\mathbf{x}(U)$, and construct the developable surface generated by the normals of $\mathbf{x}(U)$ along the curve $\mathbf{x}(u,\mathrm{const.})$. The line of striction of such a developable lies on $\mathbf{y}(U)$, and as $\mathbf{x}(u,\mathrm{const.})$ describes $\mathbf{x}(U)$, this line describes $y(U)$.

> [!solution] Solution to Focal Surfaces
> Since coordinate curves are lines of curvature, we have $F=0, M=0$, and the Rodrigues formula $N_u = -k_1 \mathbf{x}_u$, $N_v = -k_2 \mathbf{x}_v$.
> 
> **Part a:** Differentiating $\mathbf{y}(u, v) = \mathbf{x} + \rho_1 N$ gives:
> $$ \mathbf{y}_u = \mathbf{x}_u + (\rho_1)_u N + \rho_1 N_u = \mathbf{x}_u + (\rho_1)_u N + \frac{1}{k_1}(-k_1 \mathbf{x}_u) = (\rho_1)_u N $$
> $$ \mathbf{y}_v = \mathbf{x}_v + (\rho_1)_v N + \rho_1 N_v = \mathbf{x}_v + (\rho_1)_v N - \frac{k_2}{k_1} \mathbf{x}_v = \left(1 - \frac{k_2}{k_1}\right) \mathbf{x}_v + (\rho_1)_v N $$
> Then $\mathbf{y}_u \wedge \mathbf{y}_v = (\rho_1)_u \left(1 - \frac{k_2}{k_1}\right) (N \wedge \mathbf{x}_v)$. Since $(k_1)_u \neq 0 \implies (\rho_1)_u \neq 0$, and $k_1 \neq k_2$ (no umbilics), and $N \wedge \mathbf{x}_v \neq 0$, it follows that $\mathbf{y}_u \wedge \mathbf{y}_v \neq 0$. Thus $\mathbf{y}$ is regular.
> 
> **Part b:** The normal $\bar{N}$ to $\mathbf{y}$ is parallel to $\mathbf{y}_u \wedge \mathbf{y}_v \propto N \wedge \mathbf{x}_v$, which is parallel to $\mathbf{x}_u$ (since $\mathbf{x}_u, \mathbf{x}_v, N$ are orthogonal). We check the conjugacy of directions $\mathbf{y}_u, \mathbf{y}_v$ by calculating $\langle \bar{N}, \mathbf{y}_{uv} \rangle$:
> $$ \mathbf{y}_{uv} = \frac{\partial}{\partial v} [(\rho_1)_u N] = (\rho_1)_{uv} N + (\rho_1)_u N_v = (\rho_1)_{uv} N - (\rho_1)_u k_2 \mathbf{x}_v $$
> Since $\bar{N} \propto \mathbf{x}_u$, and $\langle \mathbf{x}_u, N \rangle = 0$, $\langle \mathbf{x}_u, \mathbf{x}_v \rangle = 0$, we have $\langle \bar{N}, \mathbf{y}_{uv} \rangle = 0$. Thus the directions are conjugate.
> 
> **Part c:** The ruled surface generated by normals along $\alpha(u) = \mathbf{x}(u, v_0)$ is $w(u, v) = \alpha(u) + v N(u, v_0)$. This is developable because $\alpha$ is a line of curvature. The line of striction is $\beta(u) = \alpha(u) - \frac{\langle \alpha', N' \rangle}{\langle N', N' \rangle} N$. With $\alpha' = \mathbf{x}_u$ and $N' = N_u = -k_1 \mathbf{x}_u$:
> $$ \beta(u) = \mathbf{x}_u - \frac{\langle \mathbf{x}_u, -k_1 \mathbf{x}_u \rangle}{k_1^2 |\mathbf{x}_u|^2} N = \mathbf{x} + \frac{k_1}{k_1^2} N = \mathbf{x} + \frac{1}{k_1} N = \mathbf{y}(u, v_0) $$
> Thus the line of striction describes the focal surface $\mathbf{y}$.

## Problem 3-5, 10* · Generalized Envelopes
> [!exr] Generalized Envelopes
> A family $\{\alpha(t), N(t)\}$, $t \in I$, is said to be a family of tangent planes if $\alpha'(t) \neq 0$, $N'(t) \neq 0$, and $\langle \alpha'(t), N(t) \rangle = 0$ for all $t \in I$.
> - a. Give a proof that a differentiable one-parameter family of tangent planes determines a developable surface $\mathbf{x} (t, v) = \alpha (t) + v \frac {N \wedge N ^ {\prime}}{| N ^ {\prime} |}$.
> - b. Prove that if $\alpha'(t) \wedge (N(t) \wedge N'(t)) \neq 0$, then the envelope is regular in a neighborhood of $v = 0$, and the unit normal vector is $N(t)$.
> - c. Prove that the family of osculating planes $\{\alpha(s), b(s)\}$ of a curve $\alpha$ with $k, \tau \neq 0$ is a family of tangent planes and its envelope is the tangent surface to $\alpha(s)$.

> [!solution] Solution to Generalized Envelopes
> **Part a:** The envelope is the intersection of $\langle p - \alpha, N \rangle = 0$ and $\langle p - \alpha, N' \rangle = 0$. Since $\langle \alpha', N \rangle = 0$, $\alpha(t)$ always lies in the intersection. The intersection of two planes is a line with direction $w \propto N \wedge N'$. Since $N$ is unit, $N \perp N'$, so $N, N', N \wedge N'$ are orthogonal. The surface $\mathbf{x}(t, v) = \alpha + v w$ is developable because the rulings are formed by intersections of consecutive planes in a one-parameter family.
> 
> **Part b:** At $v=0$, $\mathbf{x}_t = \alpha'$ and $\mathbf{x}_v = \frac{N \wedge N'}{|N'|}$. The condition $\alpha' \wedge (N \wedge N') \neq 0$ ensures regularity. The normal vector is:
> $$ \mathbf{x}_t \wedge \mathbf{x}_v \propto \alpha' \wedge (N \wedge N') = \langle \alpha', N' \rangle N - \langle \alpha', N \rangle N' = \langle \alpha', N' \rangle N $$
> (since $\langle \alpha', N \rangle = 0$). Thus the unit normal is $\pm N(t)$.
> 
> **Part c:** For the osculating plane, the normal is the binormal $b(s)$. 
> 1. $\alpha'(s) = t(s) \neq 0$.
> 2. $N'(s) = b'(s) = -\tau n(s) \neq 0$ (since $\tau \neq 0$).
> 3. $\langle \alpha'(s), N(s) \rangle = \langle t(s), b(s) \rangle = 0$.
> This is a family of tangent planes. The ruling direction is $w \propto N \wedge N' = b \wedge (-\tau n) = \tau t(s)$. The envelope is $\mathbf{x}(s, v) = \alpha(s) + v t(s)$, which is the tangent surface.

## Problem 3-5, 11 · Parallel Surfaces
> [!exr] Parallel Surfaces
> Let $\mathbf{x} = \mathbf{x}(u, v)$ be a regular parametrized surface. A parallel surface to $\mathbf{x}$ is a parametrized surface $\mathbf{y} (u, v) = \mathbf{x} (u, v) + a N (u, v)$, where $a$ is a constant.
> - a. Prove that $y_{u} \wedge y_{v} = (1 - 2Ha + Ka^{2})(\mathbf{x}_{u} \wedge \mathbf{x}_{v})$, where $K$ and $H$ are the Gaussian and mean curvatures of $\mathbf{x}$, respectively.
> - b. Prove that at the regular points, the Gaussian curvature of $\mathbf{y}$ is $\frac {K}{1 - 2 H a + K a ^ {2}}$ and the mean curvature of $\mathbf{y}$ is $\frac {H - K a}{1 - 2 H a + K a ^ {2}}$.
> - c. Let a surface $\mathbf{x}$ have constant mean curvature equal to $c \neq 0$ and consider the parallel surface to $\mathbf{x}$ at a distance $1/2c$. Prove that this parallel surface has constant Gaussian curvature equal to $4c^2$.

> [!solution] Solution to Parallel Surfaces
> **a.** Differentiating $\mathbf{y}(u, v) = \mathbf{x}(u, v) + a N(u, v)$ with respect to $u$ and $v$ gives:
> $$\mathbf{y}_u = \mathbf{x}_u + a N_u, \quad \mathbf{y}_v = \mathbf{x}_v + a N_v.$$
> Using the Weingarten equations $N_u = a_{11} \mathbf{x}_u + a_{21} \mathbf{x}_v$ and $N_v = a_{12} \mathbf{x}_u + a_{22} \mathbf{x}_v$, we have:
> $$\mathbf{y}_u = (1 + a a_{11}) \mathbf{x}_u + a a_{21} \mathbf{x}_v, \quad \mathbf{y}_v = a a_{12} \mathbf{x}_u + (1 + a a_{22}) \mathbf{x}_v.$$
> Then the cross product is:
> $$\mathbf{y}_u \wedge \mathbf{y}_v = \left[ (1 + a a_{11})(1 + a a_{22}) - a^2 a_{12} a_{21} \right] (\mathbf{x}_u \wedge \mathbf{x}_v)$$
> $$= \left[ 1 + a(a_{11} + a_{22}) + a^2(a_{11} a_{22} - a_{12} a_{21}) \right] (\mathbf{x}_u \wedge \mathbf{x}_v).$$
> Recall that for the shape operator $S = -dN$, the trace is $2H$ and the determinant is $K$. Since $dN$ is represented by the matrix $(a_{ij})$, we have $\text{tr}(dN) = a_{11} + a_{22} = -2H$ and $\det(dN) = a_{11} a_{22} - a_{12} a_{21} = K$. Substituting these:
> $$\mathbf{y}_u \wedge \mathbf{y}_v = (1 - 2Ha + Ka^2) (\mathbf{x}_u \wedge \mathbf{x}_v).$$
>
> **b.** The normal $N_y$ to the parallel surface is the same as the normal $N$ to the original surface (or its opposite). The shape operator $S_y$ of $\mathbf{y}$ is related to $S$ by $S_y = S (I - aS)^{-1}$. If $k_1, k_2$ are the principal curvatures of $\mathbf{x}$, the principal curvatures of $\mathbf{y}$ are $\bar{k}_i = \frac{k_i}{1 - ak_i}$.
> The Gaussian curvature $K_y$ is:
> $$K_y = \bar{k}_1 \bar{k}_2 = \frac{k_1 k_2}{(1 - ak_1)(1 - ak_2)} = \frac{K}{1 - a(k_1 + k_2) + a^2 k_1 k_2} = \frac{K}{1 - 2Ha + Ka^2}.$$
> The mean curvature $H_y$ is:
> $$H_y = \frac{1}{2}(\bar{k}_1 + \bar{k}_2) = \frac{1}{2} \left( \frac{k_1}{1 - ak_1} + \frac{k_2}{1 - ak_2} \right) = \frac{1}{2} \frac{k_1 + k_2 - 2ak_1 k_2}{1 - 2Ha + Ka^2} = \frac{H - Ka}{1 - 2Ha + Ka^2}.$$
>
> **c.** Given $H = c$ and $a = 1/2c$. The Gaussian curvature of the parallel surface is:
> $$K_y = \frac{K}{1 - 2c(1/2c) + K(1/2c)^2} = \frac{K}{1 - 1 + K/4c^2} = \frac{K}{K/4c^2} = 4c^2.$$
> This is a constant independent of the point on the surface.

## Problem 3-5, 12 · No Compact Minimal Surfaces
> [!exr] No Compact Minimal Surfaces
> Prove that there are no compact (i.e., bounded and closed in $R^3$) minimal surfaces.

> [!solution] Solution to No Compact Minimal Surfaces
> A minimal surface is defined by having mean curvature $H = \frac{1}{2}(k_1 + k_2) = 0$ at all points. This implies $k_1 = -k_2$, and thus the Gaussian curvature $K = k_1 k_2 = -k_1^2 \le 0$ everywhere on a minimal surface.
>
> However, a well-known result (Exercise 3-3, 16) states that every compact surface in $R^3$ must have at least one elliptic point, where the Gaussian curvature $K$ is strictly positive.
>
> Since a minimal surface must have $K \le 0$ everywhere, it cannot contain any elliptic points. Therefore, a minimal surface in $R^3$ cannot be compact.

## Problem 3-5, 13 · Gauss Map and Minimal Surfaces
> [!exr] Gauss Map and Minimal Surfaces
> - a. Let $S$ be a regular surface without umbilical points. Prove that $S$ is a minimal surface if and only if the Gauss map $N \colon S \to S^2$ satisfies, for all $p \in S$ and all $w_1, w_2 \in T_p(S)$, $\langle d N _ {p} (w _ {1}), d N _ {p} (w _ {2}) \rangle_ {N (p)} = \lambda (p) \langle w _ {1}, w _ {2} \rangle_ {p}$, where $\lambda(p) \neq 0$.
> - b. Let $\mathbf{x}$: $U\to S^2$ be a parametrization of the unit sphere $S^2$ by stereographic projection. Consider a neighborhood $V$ of a point $p$ of the minimal surface $S$ in part a such that $N\colon S\to S^2$ restricted to $V$ is a diffeomorphism. Prove that the parametrization $y = N^{-1}\circ \mathbf{x}$: $U\rightarrow S$ is isothermal.

> [!solution] Solution to Gauss Map and Minimal Surfaces
> **a.** The condition $\langle dN_p(w_1), dN_p(w_2) \rangle = \lambda(p) \langle w_1, w_2 \rangle$ states that $dN_p$ is a similarity transformation (a homothety) on the tangent space. In a principal basis, $dN_p$ is represented by the matrix $\text{diag}(-k_1, -k_2)$. The condition implies:
> $$k_1^2 = k_2^2 = \lambda(p).$$
> This means $k_1 = \pm k_2$. If $k_1 = k_2$, the point is an umbilical point. Since $S$ has no umbilical points, we must have $k_1 = -k_2$, which is equivalent to $H = (k_1 + k_2)/2 = 0$. Thus, $S$ is a minimal surface.
>
> **b.** The stereographic projection $\mathbf{x} \colon U \to S^2$ is a conformal map. The condition in part (a) implies that the Gauss map $N \colon S \to S^2$ is a conformal map (since it preserves angles and scales all vectors by $\sqrt{\lambda(p)}$). Consequently, its inverse $N^{-1} \colon S^2 \to S$ is also conformal. 
> The parametrization $y = N^{-1} \circ \mathbf{x}$ is the composition of two conformal maps, and is therefore itself conformal. A parametrization is conformal if and only if its first fundamental form satisfies $E = G$ and $F = 0$, which is the definition of an isothermal parametrization.

## Problem 3-5, 14 · Conjugate Minimal Surfaces
> [!exr] Conjugate Minimal Surfaces
> Let $\mathbf{x}$ and $\mathbf{y}$ be isothermal parametrizations of minimal surfaces such that their component functions are pairwise harmonic conjugate; then $\mathbf{x}$ and $\mathbf{y}$ are called conjugate minimal surfaces. Prove that
> - a. The helicoid and the catenoid are conjugate minimal surfaces.
> - b. Given two conjugate minimal surfaces, $\mathbf{x}$ and $\mathbf{y}$, the surface $\mathbf{z} = (\cos t) \mathbf{x} + (\sin t) \mathbf{y}$ is again minimal for all $t \in R$.
> - c. All surfaces of the one-parameter family have the same fundamental form: $E = \langle \mathbf{x}_u, \mathbf{x}_u \rangle = \langle \mathbf{y}_v, \mathbf{y}_v \rangle$, $F = 0$, $G = \langle \mathbf{x}_v, \mathbf{x}_v \rangle = \langle \mathbf{y}_u, \mathbf{y}_u \rangle$.

> [!solution] Solution to Conjugate Minimal Surfaces
> **a.** Let the catenoid be $\mathbf{x}(v, u) = (\cosh v \cos u, \cosh v \sin u, v)$ and the helicoid be $\mathbf{y}(v, u) = (\sinh v \sin u, -\sinh v \cos u, u)$.
> Computing the derivatives:
> $\mathbf{x}_v = (\sinh v \cos u, \sinh v \sin u, 1), \quad \mathbf{y}_u = (\sinh v \cos u, \sinh v \sin u, 1) \implies \mathbf{x}_v = \mathbf{y}_u.$
> $\mathbf{x}_u = (-\cosh v \sin u, \cosh v \cos u, 0), \quad \mathbf{y}_v = (\cosh v \sin u, -\cosh v \cos u, 0) \implies \mathbf{x}_u = -\mathbf{y}_v.$
> These are the Cauchy-Riemann equations for the pairs of components, showing they are conjugate.
>
> **b.** Since $\mathbf{x}$ and $\mathbf{y}$ are conjugate, they satisfy $\mathbf{x}_u = \mathbf{y}_v$ and $\mathbf{x}_v = -\mathbf{y}_u$. Then for $\mathbf{z} = (\cos t) \mathbf{x} + (\sin t) \mathbf{y}$:
> $\mathbf{z}_u = \cos t \mathbf{x}_u + \sin t \mathbf{y}_u = \cos t \mathbf{x}_u - \sin t \mathbf{x}_v,$
> $\mathbf{z}_v = \cos t \mathbf{x}_v + \sin t \mathbf{y}_v = \cos t \mathbf{x}_v + \sin t \mathbf{x}_u.$
> Since $\mathbf{x}$ is isothermal ($|\mathbf{x}_u|^2 = |\mathbf{x}_v|^2$ and $\mathbf{x}_u \cdot \mathbf{x}_v = 0$), we find:
> $|\mathbf{z}_u|^2 = \cos^2 t |\mathbf{x}_u|^2 + \sin^2 t |\mathbf{x}_v|^2 = |\mathbf{x}_u|^2,$
> $|\mathbf{z}_v|^2 = \cos^2 t |\mathbf{x}_v|^2 + \sin^2 t |\mathbf{x}_u|^2 = |\mathbf{x}_u|^2,$
> $\mathbf{z}_u \cdot \mathbf{z}_v = \cos t \sin t (|\mathbf{x}_u|^2 - |\mathbf{x}_v|^2) = 0.$
> Thus $\mathbf{z}$ is isothermal. Furthermore, $\Delta \mathbf{z} = \cos t \Delta \mathbf{x} + \sin t \Delta \mathbf{y} = 0$ because components of $\mathbf{x}$ and $\mathbf{y}$ are harmonic. An isothermal harmonic parametrization defines a minimal surface.
>
> **c.** From part (b), we have $E = |\mathbf{z}_u|^2 = |\mathbf{x}_u|^2$ and $G = |\mathbf{z}_v|^2 = |\mathbf{x}_v|^2$. Since $\mathbf{x}$ is isothermal, $E = G = |\mathbf{x}_u|^2$. Also $F = \mathbf{z}_u \cdot \mathbf{z}_v = 0$. Since $\mathbf{x}_u = \mathbf{y}_v$ and $\mathbf{x}_v = -\mathbf{y}_u$, we have $|\mathbf{x}_u|^2 = |\mathbf{y}_v|^2$ and $|\mathbf{x}_v|^2 = |\mathbf{y}_u|^2$, confirming the requested formulas.
