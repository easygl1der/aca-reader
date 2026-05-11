# Chapter 3: The Geometry of Surfaces - Solutions

## Problem 3-2-1 · Principal and Asymptotic Directions
> [!exr] 3-2, 1
> Show that at a hyperbolic point, the principal directions bisect the asymptotic directions.

> [!solution] Solution to 3-2, 1
> At a hyperbolic point $p$, the Gaussian curvature $K = k_1 k_2 < 0$. This implies that the principal curvatures $k_1$ and $k_2$ have opposite signs. Let $e_1, e_2$ be the principal directions corresponding to $k_1$ and $k_2$. In the orthonormal basis $\{e_1, e_2\}$ of $T_pS$, the normal curvature in a direction making an angle $\theta$ with $e_1$ is given by Euler's formula:
> $$k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta$$
>
> Asymptotic directions are defined as directions where the normal curvature $k_n$ is zero. Setting $k_n(\theta) = 0$, we get:
> $$k_1 \cos^2 \theta + k_2 \sin^2 \theta = 0 \implies \tan^2 \theta = -\frac{k_1}{k_2}$$
>
> Since $k_1$ and $k_2$ have opposite signs, $-k_1/k_2$ is a positive real number. Let $A = \sqrt{-k_1/k_2}$. The two asymptotic directions are given by:
> $$\theta = \pm \arctan(A)$$
>
> Let $\theta_1 = \arctan(A)$ and $\theta_2 = -\arctan(A)$. The principal direction $e_1$ corresponds to $\theta = 0$. Since $0 = \frac{\theta_1 + \theta_2}{2}$, the direction $e_1$ bisects the angle between the two asymptotic directions.
>
> The other principal direction $e_2$ corresponds to $\theta = \pi/2$. Since the principal directions are orthogonal and the asymptotic directions are symmetric with respect to $e_1$, $e_2$ also bisects the supplementary angle between the asymptotic directions.

## Problem 3-2-2 · Tangency along a Curve
> [!exr] 3-2, 2
> Show that if a surface is tangent to a plane along a curve, then the points of this curve are either parabolic or planar.

> [!solution] Solution to 3-2, 2
> Let $S$ be a surface tangent to a plane $P$ along a curve $C$. For any point $p \in C$, the tangent plane $T_pS$ coincides with $P$. This implies that the unit normal vector $N(p)$ to the surface is constant along $C$ (assuming the surface is oriented and $N$ is chosen continuously).
>
> Let $\alpha(s)$ be a parametrization of $C$ by arc length. Since $N(\alpha(s))$ is constant, its derivative along the curve is zero:
> $$\frac{d}{ds} N(\alpha(s)) = dN_p(\alpha'(s)) = 0$$
>
> The differential of the Gauss map $dN_p$ acts as a linear operator on the tangent space $T_pS$. The existence of a non-zero vector $\alpha'(s) \in T_pS$ such that $dN_p(\alpha'(s)) = 0$ implies that 0 is an eigenvalue of $dN_p$.
>
> The eigenvalues of $dN_p$ are $-k_1$ and $-k_2$, where $k_1, k_2$ are the principal curvatures. Thus, at least one principal curvature must be zero at every point $p \in C$.
>
> If $k_1 = 0$ and $k_2 \neq 0$ (or vice versa), the point is **parabolic**.
> If $k_1 = k_2 = 0$, the point is **planar**.
> In either case, the Gaussian curvature $K = k_1 k_2$ is zero.

## Problem 3-2-3 · Bound for Curve Curvature
> [!exr] 3-2, 3
> Let $C \subset S$ be a regular curve on a surface $S$ with Gaussian curvature $K > 0$. Show that the curvature $k$ of $C$ at $p$ satisfies
> $$| k | \geq \min (| k _ {1} |, | k _ {2} |),$$
> where $k_{1}$ and $k_{2}$ are the principal curvatures of $S$ at $p$.

> [!solution] Solution to 3-2, 3
> By Meusnier's theorem, the normal curvature $k_n$ of a curve $C$ at point $p$ is related to its curvature $k$ by the formula:
> $$k_n = k \cos \phi$$
> where $\phi$ is the angle between the principal normal vector $n$ of the curve and the unit normal vector $N$ of the surface. Taking absolute values, we have:
> $$|k_n| = |k| |\cos \phi| \leq |k|$$
>
> From Euler's formula, the normal curvature in any direction satisfies $\min(k_1, k_2) \leq k_n \leq \max(k_1, k_2)$ if we assume $k_1, k_2$ are ordered. Since $K = k_1 k_2 > 0$, the principal curvatures $k_1$ and $k_2$ have the same sign.
>
> Case 1: $k_1, k_2 > 0$. Then $k_n > 0$ and $|k_n| = k_n \geq \min(k_1, k_2) = \min(|k_1|, |k_2|)$.
> Case 2: $k_1, k_2 < 0$. Then $k_n < 0$ and $|k_n| = -k_n \geq \min(|k_1|, |k_2|)$ because $k_n$ lies between two negative numbers.
>
> In both cases, $|k_n| \geq \min(|k_1|, |k_2|)$. Combining this with $|k| \geq |k_n|$, we obtain:
> $$|k| \geq \min(|k_1|, |k_2|)$$

## Problem 3-2-4 · Curvature Bounds Counter-example
> [!exr] 3-2, 4
> Assume that a surface $S$ has the property that $|k_1| \leq 1$, $|k_2| \leq 1$ everywhere. Is it true that the curvature $k$ of a curve on $S$ also satisfies $|k| \leq 1$?

> [!solution] Solution to 3-2, 4
> No, it is not true.
>
> Consider a plane $S = \mathbb{R}^2 \subset \mathbb{R}^3$. For a plane, the principal curvatures are $k_1 = k_2 = 0$ at all points. Thus, the condition $|k_1| \leq 1$ and $|k_2| \leq 1$ is satisfied everywhere.
>
> However, we can consider a circle $C$ of radius $r$ lying in this plane. The curvature of such a circle is $k = 1/r$. By choosing $r$ to be sufficiently small (e.g., $r = 0.1$), we can obtain a curvature $k = 10$, which clearly violates $|k| \leq 1$.
>
> This demonstrates that while the *normal* curvature of any curve is bounded by the principal curvatures, the *total* curvature of a curve can be arbitrarily large due to the geodesic curvature component (bending within the surface).

## Problem 3-2-5 · Mean Curvature Integral Formula
> [!exr] 3-2, 5
> Show that the mean curvature $H$ at $p \in S$ is given by
> $$H = \frac {1}{\pi} \int_ {0} ^ {\pi} k _ {n} (\theta) d \theta,$$
> where $k_{n}(\theta)$ is the normal curvature at $p$ along a direction making an angle $\theta$ with a fixed direction.

> [!solution] Solution to 3-2, 5
> Let the fixed direction correspond to the first principal direction $e_1$. According to Euler's formula, the normal curvature in a direction making an angle $\theta$ with $e_1$ is:
> $$k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta$$
>
> We compute the average value of $k_n(\theta)$ over the interval $[0, \pi]$:
> $$\frac{1}{\pi} \int_0^\pi k_n(\theta) d\theta = \frac{1}{\pi} \int_0^\pi (k_1 \cos^2 \theta + k_2 \sin^2 \theta) d\theta$$
>
> Using the trigonometric identities $\cos^2 \theta = \frac{1 + \cos 2\theta}{2}$ and $\sin^2 \theta = \frac{1 - \cos 2\theta}{2}$, we evaluate the integrals:
> $$\int_0^\pi \cos^2 \theta d\theta = \int_0^\pi \frac{1 + \cos 2\theta}{2} d\theta = \left[ \frac{\theta}{2} + \frac{\sin 2\theta}{4} \right]_0^\pi = \frac{\pi}{2}$$
> $$\int_0^\pi \sin^2 \theta d\theta = \int_0^\pi \frac{1 - \cos 2\theta}{2} d\theta = \left[ \frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^\pi = \frac{\pi}{2}$$
>
Substituting these results back into the integral expression:
$$\frac{1}{\pi} \left( k_1 \frac{\pi}{2} + k_2 \frac{\pi}{2} \right) = \frac{k_1 + k_2}{2}$$

By definition, the mean curvature $H$ is $\frac{k_1 + k_2}{2}$. Thus:
$$H = \frac{1}{\pi} \int_0^\pi k_n(\theta) d\theta$$

## Problem 3-2-6 · Sum of Normal Curvatures
> [!exr] 3-2, 6
> Show that the sum of the normal curvatures for any pair of orthogonal directions, at a point $p$, is constant.

> [!solution] Solution to 3-2, 6
> Let $e_1, e_2$ be the principal directions at $p$ with principal curvatures $k_1, k_2$. Any direction in $T_p(S)$ can be represented by an angle $\theta$ with respect to $e_1$. By Euler's formula, the normal curvature in this direction is:
> $$k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta$$
>
> A pair of orthogonal directions is given by $\theta$ and $\theta + \pi/2$. The sum of the normal curvatures in these directions is:
> $$k_n(\theta) + k_n(\theta + \pi/2) = (k_1 \cos^2 \theta + k_2 \sin^2 \theta) + (k_1 \cos^2(\theta + \pi/2) + k_2 \sin^2(\theta + \pi/2))$$
>
> Since $\cos(\theta + \pi/2) = -\sin \theta$ and $\sin(\theta + \pi/2) = \cos \theta$, we have:
> $$k_n(\theta) + k_n(\theta + \pi/2) = k_1 \cos^2 \theta + k_2 \sin^2 \theta + k_1 \sin^2 \theta + k_2 \cos^2 \theta$$
> $$= k_1(\cos^2 \theta + \sin^2 \theta) + k_2(\sin^2 \theta + \cos^2 \theta) = k_1 + k_2 = 2H$$
>
> Since $k_1 + k_2 = 2H$ depends only on the point $p$ and not on $\theta$, the sum of the normal curvatures for any pair of orthogonal directions is constant and equal to $2H$.

## Problem 3-2-7 · Asymptotic Directions at Minimal Points
> [!exr] 3-2, 7
> Show that if the mean curvature is zero at a nonplanar point, then this point has two orthogonal asymptotic directions.

> [!solution] Solution to 3-2, 7
> The mean curvature $H = (k_1 + k_2)/2$. If $H = 0$, then $k_2 = -k_1$. Since the point is nonplanar, the principal curvatures are not both zero, which implies $k_1 \neq 0$ and $k_2 \neq 0$.
>
> The normal curvature in a direction $\theta$ relative to the first principal direction is:
> $$k_n(\theta) = k_1 \cos^2 \theta + k_2 \sin^2 \theta = k_1(\cos^2 \theta - \sin^2 \theta) = k_1 \cos(2\theta)$$
>
> Asymptotic directions are directions where $k_n(\theta) = 0$. Since $k_1 \neq 0$, we must have:
> $$\cos(2\theta) = 0 \implies 2\theta = \frac{\pi}{2} + m\pi$$
>
> For $m=0$, we get $\theta_1 = \pi/4$. For $m=1$, we get $\theta_2 = 3\pi/4$.
>
> The angle between these two directions is $\theta_2 - \theta_1 = \pi/2$, which means the two asymptotic directions are orthogonal.

## Problem 3-2-8 · Gauss Map Images
> [!exr] 3-2, 8
> Describe the region of the unit sphere covered by the image of the Gauss map of the following surfaces:
> a. Paraboloid of revolution $z = x^{2} + y^{2}$
> b. Hyperboloid of revolution $x^{2} + y^{2} - z^{2} = 1$
> c. Catenoid $x^{2} + y^{2} = \cosh^{2}z$

> [!solution] Solution to 3-2, 8
> The Gauss map $N \colon S \to S^2$ maps each point $p \in S$ to its unit normal vector $N(p)$.
>
> **a. Paraboloid of revolution $z = x^2 + y^2$:**
> Let $f(x, y, z) = x^2 + y^2 - z = 0$. The gradient is $\nabla f = (2x, 2y, -1)$. The upward unit normal is:
> $$N(x, y) = \frac{(-2x, -2y, 1)}{\sqrt{4x^2 + 4y^2 + 1}}$$
> Let $r^2 = x^2 + y^2$. The $z$-component of $N$ is $N_z = 1/\sqrt{4r^2 + 1}$. As $r$ varies from $0$ to $\infty$, $N_z$ varies from $1$ to $0$ (exclusive of 0). Since the surface is a surface of revolution, the image of the Gauss map covers all directions with $0 < N_z \leq 1$. This corresponds to the **open northern hemisphere** of $S^2$ plus the north pole $(0,0,1)$.
>
> **b. Hyperboloid of revolution $x^2 + y^2 - z^2 = 1$:**
> Let $f(x, y, z) = x^2 + y^2 - z^2 - 1 = 0$. The gradient is $\nabla f = (2x, 2y, -2z)$. The unit normal is:
> $$N(x, y, z) = \frac{(x, y, -z)}{\sqrt{x^2 + y^2 + z^2}} = \frac{(x, y, -z)}{\sqrt{1 + 2z^2}}$$
> The $z$-component is $N_z = -z/\sqrt{1 + 2z^2}$. As $z \to \pm \infty$, $N_z \to \mp 1/\sqrt{2}$. As $z = 0$, $N_z = 0$.
> Thus, $|N_z| < 1/\sqrt{2}$. The image is the **equatorial belt** between the latitudes $-45^\circ$ and $+45^\circ$, i.e., $\{ (x, y, z) \in S^2 : -1/\sqrt{2} < z < 1/\sqrt{2} \}$.
>
> **c. Catenoid $x^2 + y^2 = \cosh^2 z$:**
> Let $f(x, y, z) = x^2 + y^2 - \cosh^2 z = 0$. The gradient is $\nabla f = (2x, 2y, -2\cosh z \sinh z)$. The unit normal is:
> $$N = \frac{(x, y, -\cosh z \sinh z)}{\sqrt{\cosh^2 z + \cosh^2 z \sinh^2 z}} = \frac{(x, y, -\cosh z \sinh z)}{\cosh^2 z} = \left( \frac{x}{\cosh^2 z}, \frac{y}{\cosh^2 z}, -\tanh z \right)$$
> The $z$-component $N_z = -\tanh z$ covers the interval $(-1, 1)$ as $z$ varies from $-\infty$ to $+\infty$. However, $N_z$ only approaches $\pm 1$ as $z \to \mp \infty$. Thus, the image is the **entire unit sphere minus the north and south poles**.

## Problem 3-2-9 · Spherical Image and Curvature
> [!exr] 3-2, 9
> Prove that
> a. The image $N \circ \alpha$ by the Gauss map $N \colon S \to S^2$ of a parametrized regular curve $\alpha \colon I \to S$ which contains no planar or parabolic points is a parametrized regular curve on the sphere $S^2$ (called the spherical image of $\alpha$).
> b. If $C = \alpha(I)$ is a line of curvature, and $k$ is its curvature at $p$, then
> $$k = | k _ {n} k _ {N} |,$$
> where $k_{n}$ is the normal curvature at $p$ along the tangent line of $C$ and $k_{N}$ is the curvature of the spherical image $N(C) \subset S^2$ at $N(p)$.

> [!solution] Solution to 3-2, 9
> **a.** Let $\alpha(t)$ be a regular curve on $S$, so $\alpha'(t) \neq 0$. The derivative of the spherical image is $(N \circ \alpha)'(t) = dN_{\alpha(t)}(\alpha'(t))$. The differential of the Gauss map $dN_p$ has eigenvalues $-k_1, -k_2$. If $p$ is neither planar nor parabolic, then $k_1 \neq 0$ and $k_2 \neq 0$, so $dN_p$ is a non-singular linear map. Therefore, $dN_p(\alpha'(t)) \neq 0$ for any $\alpha'(t) \neq 0$. Thus, $N \circ \alpha$ is a regular curve on $S^2$.
>
> **b.** Let $\alpha(s)$ be parametrized by arc length, so $|\alpha'|=1$ and $k = |\alpha''|$. Since $C$ is a line of curvature, $\alpha'(s)$ is a principal direction, and $dN(\alpha') = -k_n \alpha'$, where $k_n$ is the principal curvature.
> The spherical image is $\beta(s) = N(\alpha(s))$. Its velocity is $\beta'(s) = -k_n \alpha'(s)$. The speed of the spherical image is $\sigma = |\beta'(s)| = |k_n|$.
> Let $s_N$ be the arc length of the spherical image. Then $ds_N/ds = |k_n|$. The unit tangent vector to the spherical image is $T_N = \frac{\beta'}{|k_n|} = \pm \alpha'$.
> The curvature $k_N$ of the spherical image in $S^2$ is the magnitude of the derivative of $T_N$ with respect to $s_N$:
> $$k_N = \left| \frac{dT_N}{ds_N} \right| = \left| \frac{dT_N}{ds} \frac{ds}{ds_N} \right| = \left| \pm \alpha'' \frac{1}{|k_n|} \right| = \frac{|\alpha''|}{|k_n|} = \frac{k}{|k_n|}$$
> Rearranging gives $k = |k_n k_N|$.

## Problem 3-2-10 · Osculating Plane of Line of Curvature
> [!exr] 3-2, 10
> Assume that the osculating plane of a line of curvature $C \subset S$, which is nowhere tangent to an asymptotic direction, makes a constant angle with the tangent plane of $S$ along $C$. Prove that $C$ is a plane curve.

> [!solution] Solution to 3-2, 10
> Let $\alpha(s)$ be the arc-length parametrization of $C$. Let $T = \alpha'$, $N$ be the surface normal, and $n$ be the principal normal of the curve $C$. Since $C$ is a line of curvature, $N' = -k_n T$.
> The osculating plane is spanned by $\{T, T'\}$. Since $T' = k n = k_g (N \times T) + k_n N$, the normal to the osculating plane (the binormal $B$) is:
> $$B = T \times n = \frac{T \times T'}{|T'|} = \frac{T \times (k_g (N \times T) + k_n N)}{k} = \frac{k_g N - k_n (N \times T)}{k}$$
> The angle $\theta$ between the osculating plane and the tangent plane is the angle between their normals $B$ and $N$. Thus:
> $$\cos \theta = |B \cdot N| = \frac{|k_g|}{k} = \frac{|k_g|}{\sqrt{k_g^2 + k_n^2}}$$
> This implies that $\tan^2 \theta = (k_n/k_g)^2$, so $k_g/k_n$ is constant. Let $k_g = c k_n$ for some constant $c$.
>
> We check if the torsion $\tau$ is zero. Recall $B = \frac{1}{k}(k_g N - k_n (N \times T))$.
> Differentiating $B$ with respect to $s$:
> $$B' = \left( \frac{k_g}{k} \right)' N + \frac{k_g}{k} N' - \left( \frac{k_n}{k} \right)' (N \times T) - \frac{k_n}{k} (N' \times T + N \times T')$$
> Since $k_g/k$ and $k_n/k$ are constant (as $k_g/k_n$ is constant and $k^2 = k_g^2 + k_n^2$), their derivatives are zero. Also $N' = -k_n T$, so $N' \times T = 0$.
> $$B' = \frac{k_g}{k} (-k_n T) - \frac{k_n}{k} (N \times (k_g (N \times T) + k_n N))$$
> $$= -\frac{k_g k_n}{k} T - \frac{k_n}{k} (k_g (-T) + 0) = -\frac{k_g k_n}{k} T + \frac{k_g k_n}{k} T = 0$$
> Since $B' = -\tau n$, $B' = 0$ implies $\tau = 0$ (as $n$ is well-defined since $C$ is not tangent to an asymptotic direction, so $k_n \neq 0 \implies k \neq 0$). Thus $C$ is a plane curve.

