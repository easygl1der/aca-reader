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

## Problem 3-2-11 · Minimum Angle of Conjugate Directions
> [!exr] 3-2, 11
> Let $p$ be an elliptic point of a surface $S$, and let $r$ and $r'$ be conjugate directions at $p$. Let $r$ vary in $T_p(S)$ and show that the minimum of the angle of $r$ with $r'$ is reached at a unique pair of directions in $T_p(S)$ that are symmetric with respect to the principal directions.

> [!solution] Solution to 3-2, 11
> Let $e_1, e_2$ be the principal directions with principal curvatures $k_1, k_2$. Since $p$ is elliptic, $k_1$ and $k_2$ have the same sign. Assume $k_1 \geq k_2 > 0$ without loss of generality. A direction $r$ can be represented by the angle $\theta$ it makes with $e_1$. The conjugate direction $r'$ making an angle $\theta' satisfies the conjugacy condition:
> $$k_1 \cos \theta \cos \theta' + k_2 \sin \theta \sin \theta' = 0 \implies \tan \theta \tan \theta' = -\frac{k_1}{k_2}$$
>
> Let $c = k_1/k_2 \geq 1$. Then $\tan \theta' = -c / \tan \theta$. Since the product of tangents is negative, $\theta$ and $\theta'$ lie in different quadrants (e.g., $\theta \in (0, \pi/2)$ and $\theta' \in (-\pi/2, 0)$). The angle $\alpha$ between $r$ and $r'$ is given by:
> $$\tan \alpha = \left| \frac{\tan \theta - \tan \theta'}{1 + \tan \theta \tan \theta'} \right| = \left| \frac{\tan \theta + c/\tan \theta}{1 - c} \right| = \frac{\tan \theta + c/\tan \theta}{c - 1}$$
>
> To minimize the angle $\alpha$ (which is equivalent to minimizing $\tan \alpha$ for acute $\alpha$), we minimize the function $f(t) = t + c/t$ where $t = \tan \theta > 0$. Taking the derivative:
> $$f'(t) = 1 - \frac{c}{t^2} = 0 \implies t = \sqrt{c}$$
>
> Thus, the minimum angle is reached when $\tan \theta = \sqrt{k_1/k_2}$. The corresponding conjugate direction has $\tan \theta' = -c/\sqrt{c} = -\sqrt{c}$.
>
> So the directions are given by $\theta = \arctan(\sqrt{k_1/k_2})$ and $\theta' = -\arctan(\sqrt{k_1/k_2})$. These two directions are symmetric with respect to the principal direction $e_1$ (and also $e_2$). The pair $\{r, r'\}$ is unique up to the choice of principal axis.

## Problem 3-2-12 · Geometric Construction of Conjugate Directions
> [!exr] 3-2, 12
> Let $p$ be a hyperbolic point of a surface $S$, and let $r$ be a direction in $T_{p}(S)$. Describe and justify a geometric construction to find the conjugate direction $r'$ of $r$ in terms of the Dupin indicatrix.

> [!solution] Solution to 3-2, 12
> **Geometric Construction:**
> 1. Draw the Dupin indicatrix at $p$, which consists of two hyperbolas $k_1 x^2 + k_2 y^2 = \pm 1$ in $T_p(S)$.
> 2. Draw the line through the origin in direction $r$. If $r$ is not an asymptotic direction, it will intersect one of the hyperbolas at two points. Let $P$ be one such intersection point.
> 3. The conjugate direction $r'$ is the direction parallel to the tangent line of the indicatrix at $P$.
> 4. If $r$ is an asymptotic direction, it is its own conjugate direction (the line in direction $r$ is an asymptote to the hyperbolas).
>
> **Justification:**
> Let the principal directions be the coordinate axes. The indicatrix is defined by $f(x, y) = k_1 x^2 + k_2 y^2 = \pm 1$. The direction $r$ is given by the vector $(x_0, y_0)$ where $P = (x_0, y_0)$ lies on the indicatrix.
> The gradient of $f$ at $P$ is $\nabla f = (2k_1 x_0, 2k_2 y_0)$. The tangent line at $P$ is perpendicular to $\nabla f$, so its direction vector $(X, Y)$ satisfies:
> $$k_1 x_0 X + k_2 y_0 Y = 0$$
> This is exactly the condition for directions $(x_0, y_0)$ and $(X, Y)$ to be conjugate with respect to the second fundamental form $II_p(v, w) = k_1 v_1 w_1 + k_2 v_2 w_2$. Thus, the direction of the tangent line is the conjugate direction $r'$.

## Problem 3-2-13* · Theorem of Beltrami-Enneper
> [!exr] 3-2, 13
> (Theorem of Beltrami-Enneper.) Prove that the absolute value of the torsion $\tau$ at a point of an asymptotic curve, whose curvature is nowhere zero, is given by
> \[
> | \tau | = \sqrt {- K},
> \]
> where $K$ is the Gaussian curvature of the surface at the given point.

> [!solution] Solution to 3-2, 13
> Let $\alpha(s)$ be an asymptotic curve on $S$. By definition, the normal curvature is zero: $k_n = \langle \alpha'', N \rangle = 0$, where $N$ is the surface normal. Since the curvature $k = |\alpha''| \neq 0$, the principal normal $n = \alpha''/k$ of the curve must be tangent to the surface ($n \perp N$).
>
> Consider the Frenet frame $\{T, n, b\}$ of the curve. Since both $T = \alpha'$ and $n$ are tangent to $S$ and are orthogonal unit vectors, they form an orthonormal basis for $T_p(S)$. The binormal $b = T \times n$ must then be the surface normal, i.e., $N = \pm b$.
>
> Differentiating $N = \pm b$ with respect to arc length $s$:
> $$dN(T) = \frac{dN}{ds} = \pm \frac{db}{ds} = \pm (-\tau n) = \mp \tau n$$
>
> Thus, $dN(T)$ is a vector in $T_p(S)$ proportional to $n$. In the basis $\{T, n\}$, we have:
> $$\langle dN(T), T \rangle = \langle \mp \tau n, T \rangle = 0$$
> $$\langle dN(T), n \rangle = \langle \mp \tau n, n \rangle = \mp \tau$$
>
> Since the Weingarten map $dN$ is self-adjoint, the matrix of $dN$ in the basis $\{T, n\}$ is:
> $$[dN] = \begin{pmatrix} \langle dN(T), T \rangle & \langle dN(n), T \rangle \\ \langle dN(T), n \rangle & \langle dN(n), n \rangle \end{pmatrix} = \begin{pmatrix} 0 & \mp \tau \\ \mp \tau & \langle dN(n), n \rangle \end{pmatrix}$$
>
> The Gaussian curvature $K$ is the determinant of $dN$:
> $$K = \det(dN) = 0 \cdot \langle dN(n), n \rangle - (\mp \tau)^2 = -\tau^2$$
>
> Therefore, $\tau^2 = -K$, which implies $|\tau| = \sqrt{-K}$.

## Problem 3-2-14 · Curvature of Intersection Curve
> [!exr] 3-2, 14
> If the surface $S_{1}$ intersects the surface $S_{2}$ along the regular curve $C$, then the curvature $k$ of $C$ at $p \in C$ is given by
> \[
> k ^ {2} \sin^ {2} \theta = \lambda_ {1} ^ {2} + \lambda_ {2} ^ {2} - 2 \lambda_ {1} \lambda_ {2} \cos \theta,
> \]
> where $\lambda_{1}$ and $\lambda_{2}$ are the normal curvatures at $p$, along the tangent line to $C$, of $S_{1}$ and $S_{2}$, respectively, and $\theta$ is the angle made up by the normal vectors of $S_{1}$ and $S_{2}$ at $p$.

> [!solution] Solution to 3-2, 14
> Let $\alpha(s)$ be the arc-length parametrization of $C$. Let $n_1$ and $n_2$ be the unit normal vectors of $S_1$ and $S_2$ at $p$, respectively. The angle $\theta$ satisfies $\cos \theta = \langle n_1, n_2 \rangle$. The curvature vector of $C$ is $\alpha'' = k n$, where $n$ is the principal normal of the curve.
>
> The normal curvatures of $S_1$ and $S_2$ along the tangent $v = \alpha'$ are:
> $$\lambda_1 = \langle \alpha'', n_1 \rangle = k \langle n, n_1 \rangle$$
> $$\lambda_2 = \langle \alpha'', n_2 \rangle = k \langle n, n_2 \rangle$$
>
> Since $n, n_1, n_2$ are all unit vectors perpendicular to the tangent $v$, they lie in the normal plane of the curve. Let $\phi_1$ and $\phi_2$ be the angles that $n$ makes with $n_1$ and $n_2$ in this plane. Then:
> $$\lambda_1 = k \cos \phi_1, \quad \lambda_2 = k \cos \phi_2$$
> The angle between $n_1$ and $n_2$ is $\theta = |\phi_1 - \phi_2|$ (or $2\pi - |\phi_1 - \phi_2|$). In any case, $\cos \theta = \cos(\phi_1 - \phi_2) = \cos \phi_1 \cos \phi_2 + \sin \phi_1 \sin \phi_2$.
>
> We want to eliminate $\phi_1, \phi_2$. We have:
> $$(\lambda_2 - \lambda_1 \cos \theta)^2 = (k \cos \phi_2 - k \cos \phi_1 (\cos \phi_1 \cos \phi_2 + \sin \phi_1 \sin \phi_2))^2$$
> $$= k^2 (\cos \phi_2 (1 - \cos^2 \phi_1) - \cos \phi_1 \sin \phi_1 \sin \phi_2)^2$$
> $$= k^2 (\cos \phi_2 \sin^2 \phi_1 - \cos \phi_1 \sin \phi_1 \sin \phi_2)^2 = k^2 \sin^2 \phi_1 (\sin \phi_1 \cos \phi_2 - \cos \phi_1 \sin \phi_2)^2$$
> $$= k^2 \sin^2 \phi_1 \sin^2(\phi_1 - \phi_2) = k^2 \sin^2 \phi_1 \sin^2 \theta$$
>
> Also, $(\lambda_1 \sin \theta)^2 = k^2 \cos^2 \phi_1 \sin^2 \theta$. Adding these two:
> $$\lambda_2^2 + \lambda_1^2 \cos^2 \theta - 2 \lambda_1 \lambda_2 \cos \theta + \lambda_1^2 \sin^2 \theta = k^2 \sin^2 \theta (\sin^2 \phi_1 + \cos^2 \phi_1)$$
> $$\lambda_1^2 + \lambda_2^2 - 2 \lambda_1 \lambda_2 \cos \theta = k^2 \sin^2 \theta$$
> This is the desired formula.

## Problem 3-2-15 · Theorem of Joachimstahl
> [!exr] 3-2, 15
> (Theorem of Joachimstahl.) Suppose that $S_{1}$ and $S_{2}$ intersect along a regular curve $C$ and make an angle $\theta(p)$, $p \in C$. Assume that $C$ is a line of curvature of $S_{1}$. Prove that $\theta(p)$ is constant if and only if $C$ is a line of curvature of $S_{2}$.

> [!solution] Solution to 3-2, 15
> Let $\alpha(s)$ be the arc-length parametrization of $C$, and $v(s) = \alpha'(s)$ its tangent vector. Let $n_1(s)$ and $n_2(s)$ be the unit normal vectors to $S_1$ and $S_2$ along $C$. The angle $\theta$ satisfies $\cos \theta = \langle n_1, n_2 \rangle$.
>
> Differentiating with respect to $s$:
> $$-\sin \theta \frac{d\theta}{ds} = \langle n_1', n_2 \rangle + \langle n_1, n_2' \rangle$$
>
> Since $C$ is a line of curvature of $S_1$, we have $n_1' = \lambda_1 v$. Because $v$ is tangent to $S_2$, it is perpendicular to $n_2$, so $\langle n_1', n_2 \rangle = \lambda_1 \langle v, n_2 \rangle = 0$. Thus:
> $$-\sin \theta \frac{d\theta}{ds} = \langle n_1, n_2' \rangle$$
>
> **$\implies$ Direction:** If $C$ is a line of curvature of $S_2$, then $n_2' = \lambda_2 v$. Since $v$ is tangent to $S_1$, it is perpendicular to $n_1$, so $\langle n_1, n_2' \rangle = \lambda_2 \langle n_1, v \rangle = 0$. This implies $d\theta/ds = 0$ (assuming $\sin \theta \neq 0$), so $\theta$ is constant.
>
> **$\impliedby$ Direction:** If $\theta$ is constant, then $\langle n_1, n_2' \rangle = 0$. We also know $\langle n_2, n_2' \rangle = 0$ because $n_2$ is a unit vector. Thus $n_2'$ is perpendicular to both $n_1$ and $n_2$.
>
> In the tangent space $T_p(S_2)$, $n_2'$ is a vector perpendicular to $n_2$. Since $v$ is also in $T_p(S_2)$ and is perpendicular to both $n_1$ and $n_2$ (as $v$ is the intersection direction), the vector $n_2'$ must be proportional to $v$ (provided $n_1$ and $n_2$ are not parallel, i.e., $\sin \theta \neq 0$).
>
> Thus $n_2' = \mu v$ for some scalar $\mu$. This means $C$ is a line of curvature of $S_2$. (If $\sin \theta = 0$, the surfaces are tangent along $C$).

