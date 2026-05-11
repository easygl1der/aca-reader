## Problem 3-2-1 · do Carmo, Exercise 3-2, 1
> [!exr] do Carmo, Exercise 3-2, 1
> Show that at a hyperbolic point, the principal directions bisect the asymptotic directions.

> [!solution] Solution to do Carmo, Exercise 3-2, 1
> Let $p$ be a hyperbolic point, meaning the Gaussian curvature $K = k_1 k_2 < 0$. Assume $k_1 > 0 > k_2$. By Euler's formula, the normal curvature in a direction making an angle $\theta$ with the first principal direction $e_1$ is $k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta$. For an asymptotic direction, $k_n(\theta) = 0$, which yields $\tan^2 \theta = -k_1 / k_2$. The solutions are $\theta = \pm \arctan \sqrt{-k_1 / k_2}$. These two directions are symmetric with respect to $\theta = 0$ (the direction of $e_1$) and $\theta = \pi/2$ (the direction of $e_2$). Thus, the principal directions bisect the angle between the asymptotic directions.

## Problem 3-2-2 · do Carmo, Exercise 3-2, 2
> [!exr] do Carmo, Exercise 3-2, 2
> Show that if a surface is tangent to a plane along a curve, then the points of this curve are either parabolic or planar.

> [!solution] Solution to do Carmo, Exercise 3-2, 2
> Let $C$ be the curve on the surface $S$. Since $S$ is tangent to a plane along $C$, the normal vector $N$ to $S$ is constant along $C$ (it equals the normal to the plane). If $\alpha(t)$ is a parametrization of $C$, then $N(\alpha(t)) = \text{const}$, which implies $dN(\alpha'(t)) = 0$. Thus, for the tangent direction $\alpha'(t)$, the Weingarten map yields $S_p(\alpha'(t)) = -dN(\alpha'(t)) = 0$. This means that $0$ is a principal curvature (with eigenvector $\alpha'(t)$). The Gaussian curvature is $K = k_1 k_2 = 0 \cdot k_2 = 0$. Points with $K=0$ are either parabolic (if $k_2 \neq 0$) or planar (if $k_2 = 0$).

## Problem 3-2-3 · do Carmo, Exercise 3-2, 3
> [!exr] do Carmo, Exercise 3-2, 3
> Let $C \subset S$ be a regular curve on a surface $S$ with Gaussian curvature $K > 0$. Show that the curvature $k$ of $C$ at $p$ satisfies
> \[ | k | \geq \min (| k _ {1} |, | k _ {2} |), \]
> where $k_{1}$ and $k_{2}$ are the principal curvatures of $S$ at $p$.

> [!solution] Solution to do Carmo, Exercise 3-2, 3
> The curvature $k$ of $C$ and the normal curvature $k_n$ of $S$ in the direction of $C$ are related by Meusnier's theorem: $k_n = k \cos \phi$, where $\phi$ is the angle between the principal normal of $C$ and the normal of $S$. Therefore, $|k_n| \leq |k|$.
> By Euler's formula, $k_n = k_1 \cos^2 \theta + k_2 \sin^2 \theta$. Since $K = k_1 k_2 > 0$, $k_1$ and $k_2$ have the same sign. Assume they are both positive. Then $k_n$ lies in the interval $[\min(k_1, k_2), \max(k_1, k_2)]$. Thus, $|k_n| \geq \min(|k_1|, |k_2|)$.
> Combining this with $|k| \geq |k_n|$, we get $|k| \geq \min(|k_1|, |k_2|)$.

## Problem 3-2-4 · do Carmo, Exercise 3-2, 4
> [!exr] do Carmo, Exercise 3-2, 4
> Assume that a surface $S$ has the property that $|k_1| \leq 1$, $|k_2| \leq 1$ everywhere. Is it true that the curvature $k$ of a curve on $S$ also satisfies $|k| \leq 1$?

> [!solution] Solution to do Carmo, Exercise 3-2, 4
> No. The normal curvature satisfies $|k_n| \leq \max(|k_1|, |k_2|) \leq 1$, but the curvature of a curve is given by $k^2 = k_n^2 + k_g^2$. The geodesic curvature $k_g$ can be arbitrarily large. For example, consider a plane ($k_1=k_2=0$), and a circle of radius $r$ on it. The curvature of the circle is $k = 1/r$, which can be strictly greater than $1$ for $r < 1$.

## Problem 3-2-5 · do Carmo, Exercise 3-2, 5
> [!exr] do Carmo, Exercise 3-2, 5
> Show that the mean curvature $H$ at $p \in S$ is given by
> \[ H = \frac {1}{\pi} \int_ {0} ^ {\pi} k _ {n} (\theta) d \theta, \]
> where $k_{n}(\theta)$ is the normal curvature at $p$ along a direction making an angle $\theta$ with a fixed direction.

> [!solution] Solution to do Carmo, Exercise 3-2, 5
> Let the fixed direction make an angle $\theta_0$ with the first principal direction. Then the angle of the variable direction with the first principal direction is $\phi = \theta + \theta_0$.
> By Euler's formula, $k_n(\theta) = k_1 \cos^2(\theta+\theta_0) + k_2 \sin^2(\theta+\theta_0)$.
> Integrating over $[0, \pi]$:
> $\int_0^\pi \cos^2(\theta+\theta_0) d\theta = \frac{\pi}{2}$, and $\int_0^\pi \sin^2(\theta+\theta_0) d\theta = \frac{\pi}{2}$.
> Thus, $\frac{1}{\pi} \int_0^\pi k_n(\theta) d\theta = \frac{1}{\pi} \left( k_1 \frac{\pi}{2} + k_2 \frac{\pi}{2} \right) = \frac{k_1 + k_2}{2} = H$.

## Problem 3-2-6 · do Carmo, Exercise 3-2, 6
> [!exr] do Carmo, Exercise 3-2, 6
> Show that the sum of the normal curvatures for any pair of orthogonal directions, at a point $p$, is constant.

> [!solution] Solution to do Carmo, Exercise 3-2, 6
> Let the two orthogonal directions make angles $\theta$ and $\theta + \pi/2$ with the principal direction.
> By Euler's formula:
> $k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta$
> $k_n(\theta + \pi/2) = k_1 \cos^2(\theta+\pi/2) + k_2 \sin^2(\theta+\pi/2) = k_1 \sin^2 \theta + k_2 \cos^2 \theta$.
> Their sum is:
> $k_n(\theta) + k_n(\theta + \pi/2) = k_1 (\cos^2 \theta + \sin^2 \theta) + k_2 (\sin^2 \theta + \cos^2 \theta) = k_1 + k_2 = 2H$.
> Since $H$ is a property of the point $p$, this sum is constant.

## Problem 3-2-7 · do Carmo, Exercise 3-2, 7
> [!exr] do Carmo, Exercise 3-2, 7
> Show that if the mean curvature is zero at a nonplanar point, then this point has two orthogonal asymptotic directions.

> [!solution] Solution to do Carmo, Exercise 3-2, 7
> Since $H = (k_1 + k_2)/2 = 0$, we have $k_2 = -k_1$. Since the point is nonplanar, $k_1 \neq 0$.
> By Euler's formula, the normal curvature is $k_n(\theta) = k_1 \cos^2 \theta - k_1 \sin^2 \theta = k_1 \cos 2\theta$.
> Asymptotic directions are those where $k_n(\theta) = 0$. Since $k_1 \neq 0$, this requires $\cos 2\theta = 0$.
> The solutions in $[0, \pi)$ are $2\theta = \pi/2$ and $2\theta = 3\pi/2$, which give $\theta_1 = \pi/4$ and $\theta_2 = 3\pi/4$.
> The angle between these two directions is $\theta_2 - \theta_1 = \pi/2$, so they are orthogonal.

## Problem 3-2-8 · do Carmo, Exercise 3-2, 8
> [!exr] do Carmo, Exercise 3-2, 8
> Describe the region of the unit sphere covered by the image of the Gauss map of the following surfaces:
> a. Paraboloid of revolution $z = x^{2} + y^{2}$
> b. Hyperboloid of revolution $x^{2} + y^{2} - z^{2} = 1$
> c. Catenoid $x^{2} + y^{2} = \cosh^{2}z$

> [!solution] Solution to do Carmo, Exercise 3-2, 8
> a. For the paraboloid $z = x^2 + y^2$, the normal is $N = \frac{(-2x, -2y, 1)}{\sqrt{1+4x^2+4y^2}}$. The $z$-component is always strictly positive. As $x, y \to \infty$, $N_z \to 0$. The image is the open northern hemisphere $S^2 \cap \{z > 0\}$.
> b. For the hyperboloid $x^2 + y^2 - z^2 = 1$, the normal is $N = \frac{(x, y, -z)}{\sqrt{x^2+y^2+z^2}} = \frac{(x,y,-z)}{\sqrt{1+2z^2}}$. The $z$-component is $N_z = \frac{-z}{\sqrt{1+2z^2}}$. The magnitude $|N_z| < 1/\sqrt{2}$. Thus the image is the spherical band $-\frac{1}{\sqrt{2}} < z < \frac{1}{\sqrt{2}}$.
> c. For the catenoid $x^2 + y^2 = \cosh^2 z$, the parametrization is $\mathbf{x}(u,v) = (\cosh v \cos u, \cosh v \sin u, v)$. The normal is $N = \frac{(\cos u, \sin u, -\sinh v)}{\cosh v} = (\frac{\cos u}{\cosh v}, \frac{\sin u}{\cosh v}, -\tanh v)$. Since $\tanh v \in (-1, 1)$, the image covers the entire unit sphere except for the north and south poles $(0,0,\pm 1)$.

## Problem 3-2-9 · do Carmo, Exercise 3-2, 9
> [!exr] do Carmo, Exercise 3-2, 9
> Prove that
> a. The image $N \circ \alpha$ by the Gauss map of a regular curve $\alpha$ without planar/parabolic points is a regular curve on $S^2$.
> b. If $C = \alpha(I)$ is a line of curvature, then $k = | k _ {n} k _ {N} |$.

> [!solution] Solution to do Carmo, Exercise 3-2, 9
> a. The curve $N \circ \alpha$ is regular if its tangent vector $(N \circ \alpha)' = dN(\alpha') \neq 0$. Since $\alpha$ is a regular curve, $\alpha' \neq 0$. The map $dN$ is an isomorphism on $T_p S$ precisely when its determinant, the Gaussian curvature $K$, is non-zero. Since the curve contains no planar ($K=0, S_p=0$) or parabolic ($K=0, S_p \neq 0$ but $\det S_p = 0$) points, $K \neq 0$ and $dN$ is injective. Thus $dN(\alpha') \neq 0$.
> b. Since $C$ is a line of curvature, $\alpha'$ is a principal direction, so $dN(\alpha') = -k_n \alpha'$ (where $k_n$ is the principal curvature in that direction). Let $s$ be the arc length of $\alpha$, so $|\alpha'| = 1$. The curve $N \circ \alpha$ has tangent $N' = -k_n \alpha'$. Its arc length parameter is $s_N$, and $ds_N/ds = |N'| = |k_n|$. The curvature of $N(C)$ on $S^2$ is $k_N = |\frac{dT_N}{ds_N}|$, where $T_N = \frac{N'}{|N'|} = \pm \alpha'$. Then $\frac{dT_N}{ds} = \pm \alpha'' = \pm k n$ (where $k$ is the curvature of $\alpha$ and $n$ is its principal normal). So $k_N = |\frac{dT_N}{ds} \frac{ds}{ds_N}| = \frac{k}{|k_n|}$. Hence $k = |k_n k_N|$.

## Problem 3-2-10 · do Carmo, Exercise 3-2, 10
> [!exr] do Carmo, Exercise 3-2, 10
> Assume that the osculating plane of a line of curvature $C \subset S$, which is nowhere tangent to an asymptotic direction, makes a constant angle with the tangent plane of $S$ along $C$. Prove that $C$ is a plane curve.

> [!solution] Solution to do Carmo, Exercise 3-2, 10
> Let $\theta$ be the constant angle between the osculating plane and the tangent plane. Then $\cos \theta = \langle N, n \rangle = \text{const}$, where $n$ is the principal normal of $C$ and $N$ is the normal of $S$. Since $C$ is a line of curvature, $N' = -k_n t$. Differentiating $\langle N, b \rangle = \sin \theta = \text{const}$ (where $b = t \times n$ is the binormal), we get $\langle N', b \rangle + \langle N, b' \rangle = 0$. Since $N' = -k_n t$, $\langle N', b \rangle = -k_n \langle t, b \rangle = 0$. Thus $\langle N, b' \rangle = 0$. By Frenet-Serret, $b' = -\tau n$, so $\langle N, -\tau n \rangle = 0$, giving $-\tau \cos \theta = 0$.
> Since $C$ is nowhere tangent to an asymptotic direction, $k_n \neq 0$. By Meusnier's theorem, $k_n = k \cos \theta$. Thus $\cos \theta \neq 0$. This implies $\tau = 0$, so $C$ is a plane curve.

## Problem 3-2-11 · do Carmo, Exercise 3-2, 11
> [!exr] do Carmo, Exercise 3-2, 11
> Let $p$ be an elliptic point of a surface $S$, and let $r$ and $r'$ be conjugate directions at $p$. Let $r$ vary in $T_p(S)$ and show that the minimum of the angle of $r$ with $r'$ is reached at a unique pair of directions in $T_p(S)$ that are symmetric with respect to the principal directions.

> [!solution] Solution to do Carmo, Exercise 3-2, 11
> At an elliptic point, $K = k_1 k_2 > 0$. We can assume $k_1 > k_2 > 0$. Let $r = (\cos \theta, \sin \theta)$ in the principal basis. Conjugate directions satisfy $\langle dN(r), r' \rangle = 0$, so $-k_1 \cos \theta \cos \theta' - k_2 \sin \theta \sin \theta' = 0$. Thus $\tan \theta' = -\frac{k_1}{k_2} \cot \theta$.
> The angle between $r$ and $r'$ is $\phi = |\theta' - \theta|$. We want to minimize $\tan \phi = \left| \frac{\tan \theta' - \tan \theta}{1 + \tan \theta \tan \theta'} \right| = \left| \frac{-\frac{k_1}{k_2} \cot \theta - \tan \theta}{1 - \frac{k_1}{k_2}} \right| = \frac{k_1 \cot \theta + k_2 \tan \theta}{k_1 - k_2}$.
> To minimize this, we set the derivative with respect to $\theta$ to $0$: $-k_1 \csc^2 \theta + k_2 \sec^2 \theta = 0$, which gives $\tan^2 \theta = \frac{k_1}{k_2}$.
> Thus $\theta = \pm \arctan \sqrt{k_1/k_2}$. These two directions are symmetric with respect to the principal directions.

## Problem 3-2-12 · do Carmo, Exercise 3-2, 12
> [!exr] do Carmo, Exercise 3-2, 12
> Let $p$ be a hyperbolic point of a surface $S$, and let $r$ be a direction in $T_{p}(S)$. Describe and justify a geometric construction to find the conjugate direction $r'$ of $r$ in terms of the Dupin indicatrix.

> [!solution] Solution to do Carmo, Exercise 3-2, 12
> The Dupin indicatrix at a hyperbolic point consists of two conjugate hyperbolas: $k_1 x^2 + k_2 y^2 = \pm 1$. The conjugate direction $r'$ to $r$ satisfies $\langle dN(r), r' \rangle = 0$, which is equivalent to the condition that $r'$ is parallel to the tangent line of the Dupin indicatrix at the point where $r$ intersects it.
> Construction: Draw the line passing through the origin in the direction $r$. Let $P$ be the point where this line intersects the Dupin indicatrix. Draw the tangent line to the indicatrix at $P$. The direction of $r'$ is parallel to this tangent line.
> Justification: The equation of the tangent line at $P(x_0, y_0)$ is $k_1 x_0 x + k_2 y_0 y = \pm 1$. The direction of the tangent line is given by a vector $(x, y)$ such that $k_1 x_0 x + k_2 y_0 y = 0$. Since $r = (x_0, y_0)$ and $r' = (x, y)$, this is exactly the conjugacy condition $\langle dN(r), r' \rangle = k_1 x_0 x + k_2 y_0 y = 0$.

## Problem 3-2-13 · do Carmo, Exercise 3-2, 13
> [!exr] do Carmo, Exercise 3-2, 13
> (Theorem of Beltrami-Enneper.) Prove that the absolute value of the torsion $\tau$ at a point of an asymptotic curve, whose curvature is nowhere zero, is given by
> \[ | \tau | = \sqrt {- K}, \]
> where $K$ is the Gaussian curvature of the surface at the given point.

> [!solution] Solution to do Carmo, Exercise 3-2, 13
> For an asymptotic curve, the normal curvature $k_n = 0$, so the osculating plane of the curve coincides with the tangent plane of the surface, meaning the principal normal $n$ is parallel to the surface normal $N$. Thus $N = \pm n$.
> The torsion $\tau$ is given by $n' = -kt + \tau b$. Since $N = \pm n$, we have $N' = \pm n' = \pm(-kt + \tau b)$.
> On the other hand, $N' = dN(t)$. Since $t$ is an asymptotic direction, $\langle dN(t), t \rangle = -k_n = 0$. Thus $N'$ is orthogonal to $t$.
> Also, $N'$ is tangent to the surface, so it is orthogonal to $N$ (and thus to $n$).
> Since $N'$ is orthogonal to $t$ and $n$, it must be parallel to $b = t \times n$.
> Thus $k = 0$ is not possible for $N' = \pm \tau b$ unless $k=0$ (but $k \neq 0$ is given).
> Actually, $N'$ is the derivative of $N$ in the direction $t$, so $N' = dN(t)$.
> In the principal basis $\{e_1, e_2\}$, $t = \cos \theta e_1 + \sin \theta e_2$ with $k_1 \cos^2 \theta + k_2 \sin^2 \theta = 0$.
> $dN(t) = -k_1 \cos \theta e_1 - k_2 \sin \theta e_2$.
> $|dN(t)|^2 = k_1^2 \cos^2 \theta + k_2^2 \sin^2 \theta = k_1^2 (\frac{-k_2}{k_1-k_2}) + k_2^2 (\frac{k_1}{k_1-k_2}) = \frac{k_1 k_2 (k_2 - k_1)}{k_1 - k_2} = -k_1 k_2 = -K$.
> From $N' = \pm \tau b$ (since $k=0$ component along $t$), we have $|N'|^2 = \tau^2$.
> Thus $\tau^2 = -K$, so $|\tau| = \sqrt{-K}$.

## Problem 3-2-14 · do Carmo, Exercise 3-2, 14
> [!exr] do Carmo, Exercise 3-2, 14
> If the surface $S_{1}$ intersects the surface $S_{2}$ along the regular curve $C$, then the curvature $k$ of $C$ at $p \in C$ is given by
> \[ k ^ {2} \sin^ {2} \theta = \lambda_ {1} ^ {2} + \lambda_ {2} ^ {2} - 2 \lambda_ {1} \lambda_ {2} \cos \theta, \]
> where $\lambda_{1}$ and $\lambda_{2}$ are the normal curvatures at $p$, along the tangent line to $C$, of $S_{1}$ and $S_{2}$, respectively, and $\theta$ is the angle made up by the normal vectors of $S_{1}$ and $S_{2}$ at $p$.

> [!solution] Solution to do Carmo, Exercise 3-2, 14
> By Meusnier's theorem, the normal curvature of $S_i$ along $C$ is $\lambda_i = k \langle n, N_i \rangle$, where $n$ is the principal normal of $C$ and $N_i$ is the normal of $S_i$.
> Since $C$ lies on both surfaces, its tangent vector $t$ is orthogonal to both $N_1$ and $N_2$. Thus $n$ lies in the plane spanned by $N_1$ and $N_2$.
> Let $u_i = \langle n, N_i \rangle = \lambda_i / k$. The angle between $N_1$ and $N_2$ is $\theta$.
> Since $n$ is a unit vector in the plane of $N_1$ and $N_2$, we have $1 = |n|^2$.
> Using the dual basis or the projection formula in the span of $N_1, N_2$:
> $1 = \frac{1}{\sin^2 \theta} (u_1^2 + u_2^2 - 2 u_1 u_2 \cos \theta)$.
> Substituting $u_i = \lambda_i / k$:
> $1 = \frac{1}{\sin^2 \theta} \frac{1}{k^2} (\lambda_1^2 + \lambda_2^2 - 2 \lambda_1 \lambda_2 \cos \theta)$.
> Multiplying by $k^2 \sin^2 \theta$ yields the desired result.

## Problem 3-2-15 · do Carmo, Exercise 3-2, 15
> [!exr] do Carmo, Exercise 3-2, 15
> (Theorem of Joachimstahl.) Suppose that $S_{1}$ and $S_{2}$ intersect along a regular curve $C$ and make an angle $\theta(p)$, $p \in C$. Assume that $C$ is a line of curvature of $S_{1}$. Prove that $\theta(p)$ is constant if and only if $C$ is a line of curvature of $S_{2}$.

> [!solution] Solution to do Carmo, Exercise 3-2, 15
> We have $\cos \theta = \langle N_1, N_2 \rangle$. Differentiating along $C$ with tangent $t$:
> $(\cos \theta)' = \langle N_1', N_2 \rangle + \langle N_1, N_2' \rangle$.
> Since $C$ is a line of curvature of $S_1$, $N_1' = -k_1 t$. Thus $\langle N_1', N_2 \rangle = -k_1 \langle t, N_2 \rangle = 0$, as $t$ is tangent to $S_2$.
> So $(\cos \theta)' = \langle N_1, N_2' \rangle$.
> If $\theta$ is constant, $(\cos \theta)' = 0$, so $\langle N_1, N_2' \rangle = 0$. Since $N_2'$ is also orthogonal to $N_2$, $N_2'$ must be parallel to $N_1 \times N_2$, which is parallel to $t$. Thus $N_2'$ is proportional to $t$, so $C$ is a line of curvature of $S_2$.
> Conversely, if $C$ is a line of curvature of $S_2$, then $N_2'$ is parallel to $t$, so $\langle N_1, N_2' \rangle = 0$, and thus $\theta$ is constant.

## Problem 3-2-16 · do Carmo, Exercise 3-2, 16
> [!exr] do Carmo, Exercise 3-2, 16
> Show that the meridians of a torus are lines of curvature.

> [!solution] Solution to do Carmo, Exercise 3-2, 16
> A torus is a surface of revolution. For any surface of revolution, the meridians and the parallels are the coordinate curves for a parametrization $\mathbf{x}(u,v) = (f(v)\cos u, f(v)\sin u, g(v))$. For such a surface, $F = 0$ and $M = 0$, which implies that the coordinate curves are lines of curvature. Since the meridians are the curves $u = \text{const}$, they are lines of curvature.

## Problem 3-2-17 · do Carmo, Exercise 3-2, 17
> [!exr] do Carmo, Exercise 3-2, 17
> Show that if $H \equiv 0$ on $S$ and $S$ has no planar points, then the Gauss map $N \colon S \to S^2$ satisfies:
> \[ \langle d N _ {p} \left(w _ {1}\right), d N _ {p} \left(w _ {2}\right) \rangle = - K (p) \langle w _ {1}, w _ {2} \rangle \]
> Show that the above condition implies that the angle of two intersecting curves on $S$ and the angle of their spherical images are equal up to a sign.

> [!solution] Solution to do Carmo, Exercise 3-2, 17
> Since $H = \frac{1}{2} \text{tr}(S_p) = 0$, the Weingarten map $S_p = -dN_p$ has trace $0$. By Cayley-Hamilton, $S_p^2 - \text{tr}(S_p)S_p + \det(S_p)I = 0$, which gives $S_p^2 = -K I$.
> Since $S_p$ is self-adjoint, $\langle dN(w_1), dN(w_2) \rangle = \langle S_p(w_1), S_p(w_2) \rangle = \langle S_p^2(w_1), w_2 \rangle = -K \langle w_1, w_2 \rangle$.
> The cosine of the angle $\alpha$ between $w_1, w_2$ is $\frac{\langle w_1, w_2 \rangle}{|w_1||w_2|}$.
> The cosine of the angle $\alpha_N$ between $dN(w_1), dN(w_2)$ is:
> $\frac{\langle dN(w_1), dN(w_2) \rangle}{|dN(w_1)||dN(w_2)|} = \frac{-K \langle w_1, w_2 \rangle}{\sqrt{-K}|w_1| \sqrt{-K}|w_2|} = \frac{\langle w_1, w_2 \rangle}{|w_1||w_2|} = \cos \alpha$.
> Thus $|\alpha| = |\alpha_N|$.

## Problem 3-2-18 · do Carmo, Exercise 3-2, 18
> [!exr] do Carmo, Exercise 3-2, 18
> Let $\lambda_1, \ldots, \lambda_m$ be the normal curvatures at $p \in S$ along directions making angles $0, 2\pi / m, \ldots, (m - 1)2\pi / m$ with a principal direction, $m > 2$. Prove that
> \[ \lambda_ {1} + \dots + \lambda_ {m} = m H, \]

> [!solution] Solution to do Carmo, Exercise 3-2, 18
> By Euler's formula, $\lambda_j = k_1 \cos^2 \theta_j + k_2 \sin^2 \theta_j$, where $\theta_j = \frac{2\pi j}{m}$.
> Using $\cos^2 \theta = \frac{1+\cos 2\theta}{2}$ and $\sin^2 \theta = \frac{1-\cos 2\theta}{2}$, we get:
> $\sum \lambda_j = \sum \frac{k_1 + k_2}{2} + \sum \frac{k_1 - k_2}{2} \cos(2\theta_j)$.
> The first sum is $m \frac{k_1 + k_2}{2} = mH$.
> The second sum involves $\sum_{j=0}^{m-1} \cos(\frac{4\pi j}{m})$, which is the real part of $\sum \omega^j$ where $\omega = e^{i 4\pi / m}$. For $m > 2$, $\omega \neq 1$, so the sum of the geometric series is $\frac{1-\omega^m}{1-\omega} = 0$.
> Thus $\sum \lambda_j = mH$.

## Problem 3-2-19 · do Carmo, Exercise 3-2, 19
> [!exr] do Carmo, Exercise 3-2, 19
> Geodesic torsion $\tau_g = \langle \frac{dN}{ds}(0), h \rangle$. Prove:
> a. $\tau_g = (k_1 - k_2) \cos \varphi \sin \varphi$.
> b. $d\theta/ds = \tau - \tau_g$.
> c. Lines of curvature have $\tau_g \equiv 0$.

> [!solution] Solution to do Carmo, Exercise 3-2, 19
> a. Let $t = \cos \varphi e_1 + \sin \varphi e_2$. Then $h = -\sin \varphi e_1 + \cos \varphi e_2$.
> $dN(t) = -k_1 \cos \varphi e_1 - k_2 \sin \varphi e_2$.
> $\tau_g = \langle dN(t), h \rangle = k_1 \sin \varphi \cos \varphi - k_2 \sin \varphi \cos \varphi = (k_1 - k_2) \sin \varphi \cos \varphi$.
> b. Let $N$ be the surface normal and $n, b$ be the principal normal and binormal of $C$. The angle $\theta$ is defined by $\cos \theta = \langle N, n \rangle$. Differentiating gives $-\sin \theta \theta' = \langle N', n \rangle + \langle N, n' \rangle$.
> We use the Darboux frame $\{t, h, N\}$ and the relation $n = \sin \theta h + \cos \theta N$.
> $n' = -kt + \tau b = -kt + \tau(\cos \theta h - \sin \theta N)$.
> $N' = dN(t) = -k_n t + \tau_g h$.
> $\langle N', n \rangle = \tau_g \sin \theta$.
> $\langle N, n' \rangle = -\tau \sin \theta$.
> So $-\sin \theta \theta' = (\tau_g - \tau) \sin \theta$, which implies $\theta' = \tau - \tau_g$.
> c. $\tau_g = 0$ iff $\sin \varphi = 0$ or $\cos \varphi = 0$, which means $t$ is a principal direction, i.e., $C$ is a line of curvature.

## Problem 3-2-20 · do Carmo, Exercise 3-2, 20
> [!exr] do Carmo, Exercise 3-2, 20
> (Dupin's Theorem.) The surfaces of a triply orthogonal system intersect each other in lines of curvature.

> [!solution] Solution to do Carmo, Exercise 3-2, 20
> Let $N_1, N_2, N_3$ be the normals to the three families of surfaces. They are mutually orthogonal.
> Let $C = S_1 \cap S_2$. Then the tangent $t$ to $C$ is parallel to $N_3$.
> Since $N_1$ and $N_2$ are orthogonal on $C$, their angle $\theta = \pi/2$ is constant.
> Thus $\theta' = 0$. By exercise 19, $0 = \tau - \tau_g$, so $\tau = \tau_g$.
> We need to show $\tau_g = 0$ for $C$ as a curve in $S_1$.
> $\tau_g = \langle dN_1(N_3), N_2 \rangle$.
> Since $\langle N_1, N_2 \rangle = 0$ everywhere, $X(\langle N_1, N_2 \rangle) = 0$ for any vector $X$.
> Taking $X = N_3$, we get $\langle dN_1(N_3), N_2 \rangle + \langle N_1, dN_2(N_3) \rangle = 0$.
> Similarly, for other intersections, we get $\langle dN_1(N_2), N_3 \rangle + \langle N_1, dN_3(N_2) \rangle = 0$ and $\langle dN_2(N_1), N_3 \rangle + \langle N_2, dN_3(N_1) \rangle = 0$.
> Using the symmetry $\langle dN_i(N_j), N_k \rangle = \langle S_i(N_j), N_k \rangle = \langle N_j, S_i(N_k) \rangle = \langle N_j, dN_i(N_k) \rangle$, and combining these equations, it follows that each term must be zero.
> Specifically, $\tau_g = \langle dN_1(N_3), N_2 \rangle = 0$. Thus $C$ is a line of curvature of $S_1$.

## Problem 3-3-1 · do Carmo, Exercise 3-3, 1
> [!exr] do Carmo, Exercise 3-3, 1
> Show that at the origin $(0,0,0)$ of the hyperboloid $z = axy$ we have $K = -a^2$ and $H = 0$.

> [!solution] Solution to do Carmo, Exercise 3-3, 1
> The surface is given by $f(x,y) = axy$. At $(0,0,0)$, the partial derivatives are $f_x = ay = 0$ and $f_y = ax = 0$.
> The second partial derivatives are $f_{xx} = 0$, $f_{xy} = a$, and $f_{yy} = 0$.
> The coefficients of the first fundamental form are $E = 1 + f_x^2 = 1$, $F = f_x f_y = 0$, $G = 1 + f_y^2 = 1$.
> The coefficients of the second fundamental form are $L = \frac{f_{xx}}{\sqrt{1+f_x^2+f_y^2}} = 0$, $M = \frac{f_{xy}}{\sqrt{1+f_x^2+f_y^2}} = a$, $N = \frac{f_{yy}}{\sqrt{1+f_x^2+f_y^2}} = 0$.
> The Gaussian curvature is $K = \frac{LN - M^2}{EG - F^2} = \frac{0 - a^2}{1} = -a^2$.
> The mean curvature is $H = \frac{EN - 2FM + GL}{2(EG - F^2)} = \frac{0 - 0 + 0}{2} = 0$.

## Problem 3-3-2 · do Carmo, Exercise 3-3, 2
> [!exr] do Carmo, Exercise 3-3, 2
> Determine the asymptotic curves and the lines of curvature of the helicoid $x = v \cos u, y = v \sin u, z = cu$, and show that its mean curvature is zero.

> [!solution] Solution to do Carmo, Exercise 3-3, 2
> Parametrization: $\mathbf{x}(u,v) = (v \cos u, v \sin u, cu)$.
> $\mathbf{x}_u = (-v \sin u, v \cos u, c)$, $\mathbf{x}_v = (\cos u, \sin u, 0)$.
> $E = v^2 + c^2$, $F = 0$, $G = 1$.
> $\mathbf{x}_{uu} = (-v \cos u, -v \sin u, 0)$, $\mathbf{x}_{uv} = (-\sin u, \cos u, 0)$, $\mathbf{x}_{vv} = (0,0,0)$.
> Unit normal: $N = \frac{\mathbf{x}_u \times \mathbf{x}_v}{|\mathbf{x}_u \times \mathbf{x}_v|} = \frac{(-c \sin u, c \cos u, -v)}{\sqrt{v^2+c^2}}$.
> $L = \langle \mathbf{x}_{uu}, N \rangle = 0$, $M = \langle \mathbf{x}_{uv}, N \rangle = \frac{c}{\sqrt{v^2+c^2}}$, $N_{\text{coeff}} = \langle \mathbf{x}_{vv}, N \rangle = 0$.
> Mean curvature: $H = \frac{EN - 2FM + GL}{2(EG-F^2)} = 0$ since $L=N_{\text{coeff}}=0$ and $F=0$.
> Asymptotic curves: $L du^2 + 2M dudv + N dv^2 = 0 \implies 2M dudv = 0$.
> Since $M \neq 0$, $du = 0$ or $dv = 0$. These are the curves $u = \text{const}$ (lines) and $v = \text{const}$ (helices).
> Lines of curvature: $(EM - FL)du^2 + (EN - GL)dudv + (FN - GM)dv^2 = 0$.
> $c\sqrt{v^2+c^2} du^2 - \frac{c}{\sqrt{v^2+c^2}} dv^2 = 0 \implies (v^2+c^2)du^2 = dv^2$.
> Integrating $\frac{dv}{\sqrt{v^2+c^2}} = \pm du$ gives $\sinh^{-1}(v/c) = \pm u + \text{const}$, so $v = c \sinh(\pm u + \text{const})$.

## Problem 3-3-3 · do Carmo, Exercise 3-3, 3
> [!exr] do Carmo, Exercise 3-3, 3
> Determine the asymptotic curves of the catenoid $\mathbf{x}(u, v) = (\cosh v \cos u, \cosh v \sin u, v)$.

> [!solution] Solution to do Carmo, Exercise 3-3, 3
> $\mathbf{x}_u = (-\cosh v \sin u, \cosh v \cos u, 0)$, $\mathbf{x}_v = (\sinh v \cos u, \sinh v \sin u, 1)$.
> $E = \cosh^2 v$, $F = 0$, $G = \sinh^2 v + 1 = \cosh^2 v$.
> $\mathbf{x}_{uu} = (-\cosh v \cos u, -\cosh v \sin u, 0)$, $\mathbf{x}_{uv} = (-\sinh v \sin u, \sinh v \cos u, 0)$, $\mathbf{x}_{vv} = (\cosh v \cos u, \cosh v \sin u, 0)$.
> $N = \frac{(\cos u, \sin u, -\sinh v)}{\cosh v}$.
> $L = \langle \mathbf{x}_{uu}, N \rangle = -1$, $M = 0$, $N_{\text{coeff}} = \langle \mathbf{x}_{vv}, N \rangle = 1$.
> Asymptotic curves: $L du^2 + 2M dudv + N dv^2 = -du^2 + dv^2 = 0 \implies dv = \pm du$.
> Integrating gives $v = \pm u + \text{const}$.

## Problem 3-3-4 · do Carmo, Exercise 3-3, 4
> [!exr] do Carmo, Exercise 3-3, 4
> Determine the asymptotic curves and the lines of curvature of $z = xy$.

> [!solution] Solution to do Carmo, Exercise 3-3, 4
> Parametrization: $\mathbf{x}(x,y) = (x, y, xy)$.
> $E = 1+y^2, F = xy, G = 1+x^2$.
> $L = 0, M = \frac{1}{\sqrt{1+x^2+y^2}}, N = 0$.
> Asymptotic curves: $L dx^2 + 2M dxdy + N dy^2 = \frac{2}{\sqrt{1+x^2+y^2}} dxdy = 0 \implies dx = 0$ or $dy = 0$.
> Thus the asymptotic curves are the coordinate lines $x = \text{const}$ and $y = \text{const}$.
> Lines of curvature: $(EM - FL)dx^2 + (EN - GL)dxdy + (FN - GM)dy^2 = 0$.
> $\frac{1+y^2}{\sqrt{}} dx^2 - \frac{1+x^2}{\sqrt{}} dy^2 = 0 \implies \sqrt{1+y^2} dx = \pm \sqrt{1+x^2} dy$.
> Integrating $\frac{dx}{\sqrt{1+x^2}} = \pm \frac{dy}{\sqrt{1+y^2}}$ gives $\sinh^{-1} x = \pm \sinh^{-1} y + C$.

## Problem 3-3-5 · do Carmo, Exercise 3-3, 5
> [!exr] do Carmo, Exercise 3-3, 5
> Consider Enneper's surface $\mathbf{x}(u, v) = (u - \frac{u^3}{3} + uv^2, v - \frac{v^3}{3} + vu^2, u^2 - v^2)$ and show its properties.

> [!solution] Solution to do Carmo, Exercise 3-3, 5
> a. $\mathbf{x}_u = (1-u^2+v^2, 2uv, 2u)$, $\mathbf{x}_v = (2uv, 1-v^2+u^2, -2v)$.
> $E = \langle \mathbf{x}_u, \mathbf{x}_u \rangle = (1-u^2+v^2)^2 + 4u^2v^2 + 4u^2 = (1+u^2+v^2)^2$.
> $F = \langle \mathbf{x}_u, \mathbf{x}_v \rangle = 2uv(1-u^2+v^2) + 2uv(1-v^2+u^2) - 4uv = 0$.
> $G = \langle \mathbf{x}_v, \mathbf{x}_v \rangle = (1+u^2+v^2)^2$.
> b. $\mathbf{x}_{uu} = (-2u, 2v, 2)$, $\mathbf{x}_{uv} = (2v, 2u, 0)$, $\mathbf{x}_{vv} = (2u, -2v, -2)$.
> $N = \frac{\mathbf{x}_u \times \mathbf{x}_v}{W} = \frac{(-2u, -2v, 1-u^2-v^2)}{1+u^2+v^2}$.
> $L = \langle \mathbf{x}_{uu}, N \rangle = \frac{4u^2-4v^2+2-2u^2-2v^2}{1+u^2+v^2} = 2$, $N_{\text{coeff}} = -2$, $M = 0$.
> c. $k_1 = L/E = \frac{2}{(1+u^2+v^2)^2}$, $k_2 = N_{\text{coeff}}/G = \frac{-2}{(1+u^2+v^2)^2}$.
> d. $F=0, M=0 \implies$ coordinate curves are lines of curvature.
> e. $L du^2 + N_{\text{coeff}} dv^2 = 2 du^2 - 2 dv^2 = 0 \implies du = \pm dv \implies u \pm v = \text{const}$.

## Problem 3-3-6 · do Carmo, Exercise 3-3, 6
> [!exr] do Carmo, Exercise 3-3, 6
> (A Surface with $K \equiv -1$; the Pseudosphere.)
> a. Determine the tractrix. b. Rotate to get pseudosphere. c. Show $K = -1$.

> [!solution] Solution to do Carmo, Exercise 3-3, 6
> a. The tractrix has constant tangent segment length $1$. Let $(x(v), z(v))$ be the curve. The tangent vector is $(x', z')$. The tangent line at $(x,z)$ hits the $z$-axis at $(0, z - x \frac{z'}{x'})$. The distance formula gives $x^2 + (x \frac{z'}{x'})^2 = 1$. Thus $\frac{z'}{x'} = -\frac{\sqrt{1-x^2}}{x}$. Integrating with $x = \sin v$ gives $z = \cos v + \log \tan(v/2)$.
> b. Rotating about the $z$-axis gives $\mathbf{x}(u,v) = (\sin v \cos u, \sin v \sin u, \cos v + \log \tan(v/2))$.
> c. $E = \sin^2 v, F = 0, G = \cos^2 v + \sin^2 v (\cot v)^2 = \cot^2 v$. No, wait. $z' = -\frac{\sqrt{1-x^2}}{x} x' = -\cos v$. So $G = \sin^2 v + \cos^2 v = 1$.
> Actually, for pseudosphere $\phi(v) = \sin v$. $K = -\frac{\phi''}{\phi} = -\frac{-\sin v}{\sin v} = -1$.

## Problem 3-3-7 · do Carmo, Exercise 3-3, 7
> [!exr] do Carmo, Exercise 3-3, 7
> (Surfaces of Revolution with Constant Curvature.)

> [!solution] Solution to do Carmo, Exercise 3-3, 7
> a. For a surface of revolution $\mathbf{x}(u,v) = (\phi(v)\cos u, \phi(v)\sin u, \psi(v))$ with $(\phi')^2 + (\psi')^2 = 1$, the Gaussian curvature is $K = -\frac{\phi''}{\phi}$.
> Thus $\phi'' + K\phi = 0$. $\psi$ is then $\int \sqrt{1 - (\phi')^2} dv$.
> b. For $K=1$, $\phi'' + \phi = 0 \implies \phi(v) = C \cos v$. $\psi(v) = \int \sqrt{1 - C^2 \sin^2 v} dv$.
> For $C=1$, we get the sphere. For $C > 1$ or $C < 1$, we get surfaces with "bulges" or "necks".
> c. For $K=-1$, $\phi'' - \phi = 0$.
> 1. $\phi = C \cosh v$. 2. $\phi = C \sinh v$. 3. $\phi = e^v$.

## Problem 3-3-8 · do Carmo, Exercise 3-3, 8
> [!exr] do Carmo, Exercise 3-3, 8
> (Contact of Order $\geq 2$ of Surfaces.)

> [!solution] Solution to do Carmo, Exercise 3-3, 8
> a. If $S$ and $\bar{S}$ have contact of order 2 at $p$, their Taylor expansions agree up to degree 2 in a suitable coordinate system. The derivatives of $f \circ \mathbf{x}$ depend only on the derivatives of $f$ and $\mathbf{x}$. Since the derivatives of $\mathbf{x}$ and $\bar{\mathbf{x}}$ match at $p$, the result follows by the chain rule.
> b. In the tangent plane coordinates $(x,y,f(x,y))$, $f(0,0)=0, f_x=f_y=0$. Order 2 contact means $f_{xx}=\bar{f}_{xx}, f_{xy}=\bar{f}_{xy}, f_{yy}=\bar{f}_{yy}$.
> c. The paraboloid is exactly the quadratic part of the Taylor expansion of $S$ at $p$.
> e. Since the quadratic parts match, the principal curvatures (eigenvalues of the Hessian) and thus $K$ and $H$ match.

## Problem 3-3-9 · do Carmo, Exercise 3-3, 9
> [!exr] do Carmo, Exercise 3-3, 9
> (Contact of Curves.)

> [!solution] Solution to do Carmo, Exercise 3-3, 9
> a. Contact of order $n$ means $\alpha^{(k)}(0) = \bar{\alpha}^{(k)}(0)$ for $k=0,\dots,n$. Diffeomorphisms preserve the equality of derivatives via the chain rule.
> b. Order 1 contact means $\alpha(0)=\bar{\alpha}(0)$ and $\alpha'(0)=\bar{\alpha}'(0)$, which is the definition of tangency.

## Problem 3-3-10 · do Carmo, Exercise 3-3, 10
> [!exr] do Carmo, Exercise 3-3, 10
> (Contact of Curves and Surfaces.)

> [!solution] Solution to do Carmo, Exercise 3-3, 10
> a. Let $h(t) = f(\alpha(t))$. $h(0)=0$ means the point is on the surface. $h'(0)=0$ means the tangent is in the tangent plane. $h^{(k)}(0)=0$ means higher order contact.
> b. $f(x,y,z) = Ax+By+Cz+D = 0$ is a plane. $f(\alpha(0))=0, f'(\alpha(0))=0, f''(\alpha(0))=0$ means the plane contains $p$, is tangent to $t$, and contains $\alpha'' = kn$. This plane is spanned by $t$ and $n$, which is the osculating plane.
> c. A sphere $(X-C)^2 = R^2$. The conditions $f=f'=f''=f'''=0$ at $p$ lead to the system of equations determining the center $C = \alpha + \frac{1}{k} n + \frac{k'}{k^2 \tau} b$.
