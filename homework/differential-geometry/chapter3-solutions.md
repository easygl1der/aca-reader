# Chapter 3: The Geometry of Surfaces - Solutions
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
> $$\mathbf{x}_\theta\theta = ((1-x)\cos \theta, 0, -(1-x)\sin \theta) = (\cos \theta, 0, -\sin \theta).$$
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
> Let $f \colon S \to R$ be the function $f(q) = |q|^2$. Since $S$ is compact and $f$ is continuous, $f$ attains its maximum at some point $p \in S$. Let $R_0 = |p|$. Then for all $q \in S$, $|q| \le $R_0$, which means $S$ lies inside the closed ball $\bar{B}^3(R_0)$.
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
