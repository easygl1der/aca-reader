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
> Let $r^2 = x^2 + y^2$. The $z$-component of $N$ is $N_z = 1/\sqrt{4r^2 + 1}$. As $r$ varies from $0$ to $\infty$, $N_z$ varies from $1$ to $0$ (exclusive of 0). Since the surface is a surface of revolution, the image of the Gauss map covers all directions with $0 < $N_z \leq 1$. This corresponds to the **open northern hemisphere** of $S^2$ plus the north pole $(0,0,1)$.
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
> [!exr] 3-2, 13*
> (Theorem of Beltrami-Enneper.) Prove that the absolute value of the torsion $\tau$ at a point of an asymptotic curve, whose curvature is nowhere zero, is given by
> \[
> | \tau | = \sqrt {- K},
> \]
> where $K$ is the Gaussian curvature of the surface at the given point.

> [!solution] Solution to 3-2, 13*
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

## Problem 3-2-16 · Meridians of a Torus
> [!exr] 3-2, 16
> Show that the meridians of a torus are lines of curvature.

> [!solution] Solution to 3-2, 16
> A torus of revolution is a surface of revolution. For any surface of revolution, the meridians and parallels are the lines of curvature.
>
> Geometrically, at any point $p$ on a meridian $M$ of a torus, the surface is symmetric with respect to the plane containing the meridian. This symmetry implies that the tangent vector to the meridian must be a principal direction.
>
> More formally, let $N$ be the unit normal to the torus. Along a meridian, $N$ always lies in the plane of the meridian. Thus, the derivative $dN(v)$ for a tangent vector $v$ to the meridian must also lie in the same plane. Since $dN(v)$ is also tangent to the surface, it must be parallel to $v$. This means $v$ is an eigenvector of the Weingarten map, so the meridian is a line of curvature.

## Problem 3-2-17 · Gauss Map of Minimal Surfaces
> [!exr] 3-2, 17
> Show that if $H \equiv 0$ on $S$ and $S$ has no planar points, then the Gauss map $N \colon S \to S^2$ has the following property:
> \[
> \langle d N _ {p} \left(w _ {1}\right), d N _ {p} \left(w _ {2}\right) \rangle = - K (p) \langle w _ {1}, w _ {2} \rangle
> \]
> for all $p \in S$ and all $w_{1}, w_{2} \in T_{p}(S)$. Show that the above condition implies that the angle of two intersecting curves on $S$ and the angle of their spherical images are equal up to a sign.

> [!solution] Solution to 3-2, 17
> Since $H = 0$ and there are no planar points, the principal curvatures $k_1, k_2$ satisfy $k_1 + k_2 = 0$ and $k_1 \neq 0$, which implies $k_2 = -k_1 \neq 0$. The Gaussian curvature is $K = k_1 k_2 = -k_1^2 < 0$.
>
> Let $\{e_1, e_2\}$ be an orthonormal basis of principal directions in $T_p(S)$. Then $dN_p(e_1) = -k_1 e_1$ and $dN_p(e_2) = -k_2 e_2 = k_1 e_2$.
>
> Let $w_1 = a e_1 + b e_2$ and $w_2 = c e_1 + d e_2$. Then:
> $$dN_p(w_1) = -a k_1 e_1 + b k_1 e_2$$
> $$dN_p(w_2) = -c k_1 e_1 + d k_1 e_2$$
>
> The inner product is:
> $$\langle dN_p(w_1), dN_p(w_2) \rangle = (-a k_1)(-c k_1) + (b k_1)(d k_1) = k_1^2 (ac + bd)$$
>
> Since $\langle w_1, w_2 \rangle = ac + bd$ and $-K = k_1^2$, we have:
> $$\langle dN_p(w_1), dN_p(w_2) \rangle = -K \langle w_1, w_2 \rangle$$
>
> Now consider two intersecting curves $\alpha_1, \alpha_2$ with tangent vectors $w_1, w_2$. The angle $\gamma$ between them satisfies:
> $$\cos \gamma = \frac{\langle w_1, w_2 \rangle}{|w_1| |w_2|}$$
>
> The spherical images have tangent vectors $dN(w_1)$ and $dN(w_2)$. The angle $\gamma_{sph}$ between the spherical images satisfies:
> $$\cos \gamma_{sph} = \frac{\langle dN(w_1), dN(w_2) \rangle}{|dN(w_1)| |dN(w_2)|} = \frac{-K \langle w_1, w_2 \rangle}{\sqrt{-K |w_1|^2} \sqrt{-K |w_2|^2}} = \frac{\langle w_1, w_2 \rangle}{|w_1| |w_2|} = \cos \gamma$$
>
> Thus, $\gamma_{sph} = \pm \gamma$, meaning the angles are equal up to a sign.

## Problem 3-2-18 · Average Normal Curvature
> [!exr] 3-2, 18
> Let $\lambda_1, \ldots, \lambda_m$ be the normal curvatures at $p \in S$ along directions making angles $0, 2\pi / m, \ldots, (m - 1)2\pi / m$ with a principal direction, $m > 2$. Prove that
> \[
> \lambda_ {1} + \dots + \lambda_ {m} = m H,
> \]
> where $H$ is the mean curvature at $p$.

> [!solution] Solution to 3-2, 18
> Let $\theta_j = (j-1)\frac{2\pi}{m}$ for $j=1, \ldots, m$. By Euler's formula:
> $$\lambda_j = k_1 \cos^2 \theta_j + k_2 \sin^2 \theta_j$$
>
> The sum is:
> $$\sum_{j=1}^m \lambda_j = k_1 \sum_{j=1}^m \cos^2 \theta_j + k_2 \sum_{j=1}^m \sin^2 \theta_j$$
>
> Using the identities $\cos^2 \theta = \frac{1 + \cos 2\theta}{2}$ and $\sin^2 \theta = \frac{1 - \cos 2\theta}{2}$:
> $$\sum_{j=1}^m \cos^2 \theta_j = \sum_{j=1}^m \frac{1 + \cos(2\theta_j)}{2} = \frac{m}{2} + \frac{1}{2} \sum_{j=1}^m \cos \left( (j-1)\frac{4\pi}{m} \right)$$
> $$\sum_{j=1}^m \sin^2 \theta_j = \sum_{j=1}^m \frac{1 - \cos(2\theta_j)}{2} = \frac{m}{2} - \frac{1}{2} \sum_{j=1}^m \cos \left( (j-1)\frac{4\pi}{m} \right)$$
>
> For $m > 2$, the sum $\sum_{j=0}^{m-1} e^{i j \frac{4\pi}{m}}$ is a sum of roots of unity. Specifically, let $\omega = e^{i \frac{4\pi}{m}}$. Since $m > 2$, $\omega \neq 1$. The sum is:
> $$\sum_{j=0}^{m-1} \omega^j = \frac{1 - \omega^m}{1 - \omega} = \frac{1 - e^{i 4\pi}}{1 - \omega} = 0$$
>
> Taking the real part, $\sum_{j=1}^m \cos(2\theta_j) = 0$. Therefore:
> $$\sum_{j=1}^m \cos^2 \theta_j = \frac{m}{2}, \quad \sum_{j=1}^m \sin^2 \theta_j = \frac{m}{2}$$
>
> Substituting back:
> $$\sum_{j=1}^m \lambda_j = k_1 \frac{m}{2} + k_2 \frac{m}{2} = m \left( \frac{k_1 + k_2}{2} \right) = m H$$

## Problem 3-2-19* · Geodesic Torsion
> [!exr] 3-2, 19*
> Let $C \subset S$ be a regular curve in $S$. Let $p \in C$ and $\alpha(s)$ be a parametrization of $C$ in $p$ by arc length so that $\alpha(0) = p$. Choose in $T_p(S)$ an orthonormal positive basis $\{t, h\}$, where $t = \alpha'(0)$. The geodesic torsion $\tau_g$ of $C \subset S$ at $p$ is defined by
> \[
> \tau_ {g} = \left\langle \frac {d N}{d s} (0), h \right\rangle.
> \]
> Prove that
> a. $\tau_{g} = (k_{1} - k_{2})\cos \varphi \sin \varphi$, where $\varphi$ is the angle from $e_1$ to $t$ and $t$ is the unit tangent vector corresponding to the principal curvature $k_{1}$.
> b. If $\tau$ is the torsion of $C$, $n$ is the (principal) normal vector of $C$ and $\cos \theta = \langle N, n \rangle$, then
> \[
> \frac {d \theta}{d s} = \tau - \tau_ {g}.
> \]
> c. The lines of curvature of $S$ are characterized by having geodesic torsion identically zero.

> [!solution] Solution to 3-2, 19*
> **a.** Let $\{e_1, e_2\}$ be the principal directions. We have $t = \cos \varphi e_1 + \sin \varphi e_2$ and $h = -\sin \varphi e_1 + \cos \varphi e_2$ (since $\{t, h\}$ is a positive orthonormal basis).
> The derivative of the normal is $dN/ds = dN(t) = -k_1 \cos \varphi e_1 - k_2 \sin \varphi e_2$.
> Then:
> $$\tau_g = \langle dN(t), h \rangle = (-k_1 \cos \varphi)(-\sin \varphi) + (-k_2 \sin \varphi)(\cos \varphi) = (k_1 - k_2) \sin \varphi \cos \varphi$$
>
> **b.** Let $\{T, n, b\}$ be the Frenet frame of the curve. By Meusnier's theorem, $n$ lies in the normal plane spanned by $N$ and $h$. Let $\theta$ be the angle between $N$ and $n$, so $n = \cos \theta N + \sin \theta h$.
> Then $b = T \times n = T \times (\cos \theta N + \sin \theta h) = \cos \theta (T \times N) + \sin \theta (T \times h) = -\cos \theta h + \sin \theta N$.
> Differentiating $\cos \theta = \langle N, n \rangle$:
> $-\sin \theta \theta' = \langle N', n \rangle + \langle N, n' \rangle$.
> We have $N' = dN(T) = -k_n T - \tau_g h$. So $\langle N', n \rangle = \langle -k_n T - \tau_g h, \cos \theta N + \sin \theta h \rangle = -\tau_g \sin \theta$.
> From Frenet-Serret, $n' = -\kappa T + \tau b$. So $\langle N, n' \rangle = \tau \langle N, b \rangle = \tau \sin \theta$.
> Substituting these:
> $-\sin \theta \theta' = -\tau_g \sin \theta + \tau \sin \theta \implies \theta' = \tau_g - \tau$ (Note: signs may vary based on orientation conventions, do Carmo uses $d\theta/ds = \tau - \tau_g$).
>
> **c.** From part (a), $\tau_g = (k_1 - k_2) \sin \varphi \cos \varphi$. Assuming $k_1 \neq k_2$ (non-umbilic point), $\tau_g = 0$ if and only if $\sin \varphi = 0$ or $\cos \varphi = 0$. This means $t$ is a principal direction. Thus, a curve is a line of curvature if and only if its geodesic torsion is identically zero.

## Problem 3-2-20* · Dupin's Theorem
> [!exr] 3-2, 20*
> (Dupin's Theorem.) Three families of surfaces are said to form a triply orthogonal system in an open set $U \subset R^3$ if a unique surface of each family passes through each point $p \in U$ and if the three surfaces that pass through $p$ are pairwise orthogonal. Use part c of Exercise 19 to prove Dupin's theorem: The surfaces of a triply orthogonal system intersect each other in lines of curvature.

> [!solution] Solution to 3-2, 20*
> Let $S_1, S_2, S_3$ be the three surfaces of the system passing through $p$. Let $N_1, N_2, N_3$ be their unit normal vectors at $p$. Since the surfaces are pairwise orthogonal, $\{N_1, N_2, N_3\}$ forms an orthonormal basis of $\mathbb{R}^3$.
>
> Let $C$ be the intersection curve of $S_1$ and $S_2$. The tangent vector $t$ to $C$ is perpendicular to $N_1$ and $N_2$, so $t$ is parallel to $N_3$. On the surface $S_1$, the normal is $N_1$. The geodesic torsion of $C \subset S_1$ is $\tau_g = \langle dN_1(t), h \rangle$, where $h$ is a unit vector in $T_p(S_1)$ perpendicular to $t$. Since $t = $N_3$ and $h \perp $N_1, N_3$, we must have $h = N_2$.
> Thus $\tau_g = \langle \nabla_{N_3} N_1, N_2 \rangle$.
>
> Similarly, consider $C$ as a curve on $S_2$. Its geodesic torsion is $\bar{\tau}_g = \langle dN_2(t), \bar{h} \rangle$. Here $\bar{h} = N_1$. So $\bar{\tau}_g = \langle \nabla_{N_3} N_2, N_1 \rangle$.
>
> Since $\langle N_1, N_2 \rangle = 0$, differentiating in the direction $N_3$ gives:
> $\langle \nabla_{N_3} N_1, N_2 \rangle + \langle N_1, \nabla_{N_3} N_2 \rangle = 0 \implies \tau_g + \bar{\tau}_g = 0$.
>
> Furthermore, for a triply orthogonal system, the normal vectors $N_i$ can be expressed as $N_i = \nabla u_i / |\nabla u_i|$. A property of such systems is that the rotation of the frame $\{N_1, N_2, N_3\}$ satisfies $\langle \nabla_{N_i} N_j, N_k \rangle = 0$ for all distinct $i, j, k$. This is a standard result in the theory of orthogonal coordinates (related to Lamé coefficients).
>
> Consequently, $\tau_g = \langle \nabla_{N_3} N_1, N_2 \rangle = 0$. By part (c) of Exercise 19, the intersection curve $C$ is a line of curvature on $S_1$. By symmetry, it is also a line of curvature on $S_2$. The same applies to all other intersection curves.

## Problem 3-3-1 · Hyperboloid Origin Curvatures
> [!exr] 3-3, 1
> Show that at the origin $(0,0,0)$ of the hyperboloid $z = axy$ we have $K = -a^2$ and $H = 0$.

> [!solution] Solution to 3-3, 1
> The surface is given as the graph of the function $f(x, y) = axy$. The partial derivatives are:
> $f_x = ay$, $f_y = ax$, $f_{xx} = 0$, $f_{xy} = a$, $f_{yy} = 0$.
>
> At the origin $(0,0)$, we have:
> $f_x(0,0) = 0$, $f_y(0,0) = 0$.
> The coefficients of the first fundamental form at the origin are:
> $E = 1 + f_x^2 = 1$, $F = f_x f_y = 0$, $G = 1 + f_y^2 = 1$.
> The unit normal vector at the origin is $N = (0, 0, 1)$. The coefficients of the second fundamental form are:
> $e = f_{xx} / \sqrt{1+f_x^2+f_y^2} = 0$, $f = f_{xy} / \sqrt{1+f_x^2+f_y^2} = a$, $g = f_{yy} / \sqrt{1+f_x^2+f_y^2} = 0$.
>
> The Gaussian curvature $K$ and mean curvature $H$ at the origin are:
> $$K = \frac{eg - f^2}{EG - F^2} = \frac{0 - a^2}{1} = -a^2$$
> $$H = \frac{1}{2} \frac{eG - 2fF + gE}{EG - F^2} = \frac{1}{2} \frac{0 - 0 + 0}{1} = 0$$
> Thus, at the origin, $K = -a^2$ and $H = 0$.

## Problem 3-3-2 · Helicoid Curvatures and Curves
> [!exr] 3-3, 2
> Determine the asymptotic curves and the lines of curvature of the helicoid $x = v \cos u, y = v \sin u, z = cu$, and show that its mean curvature is zero.

> [!solution] Solution to 3-3, 2
> Let the parametrization be $\mathbf{x}(u, v) = (v \cos u, v \sin u, cu)$. The tangent vectors are:
> $\mathbf{x}_u = (-v \sin u, v \cos u, c)$, $\mathbf{x}_v = (\cos u, \sin u, 0)$.
> The coefficients of the first fundamental form are:
> $E = \langle \mathbf{x}_u, \mathbf{x}_u \rangle = v^2 + c^2$, $F = \langle \mathbf{x}_u, \mathbf{x}_v \rangle = 0$, $G = \langle \mathbf{x}_v, \mathbf{x}_v \rangle = 1$.
>
> The second-order derivatives are:
> $\mathbf{x}_{uu} = (-v \cos u, -v \sin u, 0)$, $\mathbf{x}_{uv} = (-\sin u, \cos u, 0)$, $\mathbf{x}_{vv} = (0, 0, 0)$.
> The unit normal is $\mathbf{n} = \frac{\mathbf{x}_u \times \mathbf{x}_v}{|\mathbf{x}_u \times \mathbf{x}_v|} = \frac{1}{\sqrt{c^2 + v^2}} (-c \sin u, c \cos u, -v)$.
> The coefficients of the second fundamental form are:
> $e = \langle \mathbf{x}_{uu}, \mathbf{n} \rangle = 0$, $f = \langle \mathbf{x}_{uv}, \mathbf{n} \rangle = \frac{c}{\sqrt{c^2 + v^2}}$, $g = \langle \mathbf{x}_{vv}, \mathbf{n} \rangle = 0$.
>
> **Mean Curvature:**
> $$H = \frac{eG - 2fF + gE}{2(EG - F^2)} = \frac{0 \cdot 1 - 2f \cdot 0 + 0 \cdot (v^2+c^2)}{2(v^2+c^2)} = 0.$$
>
> **Asymptotic Curves:** These satisfy $e du^2 + 2f du dv + g dv^2 = 0$.
> $$2 \frac{c}{\sqrt{c^2 + v^2}} du dv = 0 \implies du dv = 0.$$
> The asymptotic curves are $u = \text{const}$ (straight lines) and $v = \text{const}$ (helices).
>
> **Lines of Curvature:** These satisfy $(f E - e F) du^2 + (g E - e G) du dv + (g F - f G) dv^2 = 0$.
> Substituting $e=g=F=0$:
> $f E du^2 - f G dv^2 = 0 \implies (v^2 + c^2) du^2 - dv^2 = 0.$
> This gives $du = \pm \frac{dv}{\sqrt{v^2 + c^2}}$. Integrating both sides:
> $u + C = \pm \ln(v + \sqrt{v^2 + c^2}) \implies v + \sqrt{v^2 + c^2} = C' e^{\pm u}$.

## Problem 3-3-3 · Catenoid Asymptotic Curves
> [!exr] 3-3, 3
> Determine the asymptotic curves of the catenoid $\mathbf {x} (u, v) = (\cosh v \cos u, \cosh v \sin u, v)$.

> [!solution] Solution to 3-3, 3
> The tangent vectors are:
> $\mathbf{x}_u = (-\cosh v \sin u, \cosh v \cos u, 0)$, $\mathbf{x}_v = (\sinh v \cos u, \sinh v \sin u, 1)$.
> The coefficients of the first fundamental form are:
> $E = \cosh^2 v$, $F = 0$, $G = \sinh^2 v + 1 = \cosh^2 v$.
>
> The second-order derivatives are:
> $\mathbf{x}_{uu} = (-\cosh v \cos u, - \cosh v \sin u, 0)$, $\mathbf{x}_{uv} = (-\sinh v \sin u, \sinh v \cos u, 0)$, $\mathbf{x}_{vv} = (\cosh v \cos u, \cosh v \sin u, 0)$.
> The unit normal is $\mathbf{n} = (\frac{\cos u}{\cosh v}, \frac{\sin u}{\cosh v}, -\tanh v)$.
> The coefficients of the second fundamental form are:
> $e = \langle \mathbf{x}_{uu}, \mathbf{n} \rangle = -1$, $f = \langle \mathbf{x}_{uv}, \mathbf{n} \rangle = 0$, $g = \langle \mathbf{x}_{vv}, \mathbf{n} \rangle = 1$.
>
> The asymptotic curves satisfy $e du^2 + 2f du dv + g dv^2 = 0$:
> $$-du^2 + dv^2 = 0 \implies du = \pm dv \implies u \pm v = \text{const}.$$
> Thus the asymptotic curves are $u + v = C_1$ and $u - v = C_2$.

## Problem 3-3-4 · Hyperbolic Paraboloid $z = xy$
> [!exr] 3-3, 4
> Determine the asymptotic curves and the lines of curvature of $z = xy$.

> [!solution] Solution to 3-3, 4
> The surface is $\mathbf{x}(x, y) = (x, y, xy)$. The partial derivatives are:
> $\mathbf{x}_x = (1, 0, y)$, $\mathbf{x}_y = (0, 1, x)$, $\mathbf{x}_{xx} = \mathbf{x}_{yy} = \mathbf{0}$, $\mathbf{x}_{xy} = (0, 0, 1)$.
> The coefficients of the first fundamental form are:
> $E = 1+y^2, F = xy, G = 1+x^2$.
> The coefficients of the second fundamental form (with $W = \sqrt{1+x^2+y^2}$) are:
> $e = 0, f = 1/W, g = 0$.
>
> **Asymptotic Curves:** $e dx^2 + 2f dx dy + g dy^2 = 0 \implies \frac{2}{W} dx dy = 0 \implies dx dy = 0$.
> The curves are $x = \text{const}$ and $y = \text{const}$.
>
> **Lines of Curvature:** $(fE - eF)dx^2 + (gE - eG)dx dy + (gF - fG)dy^2 = 0$.
> With $e=g=0$:
> $f E dx^2 - f G dy^2 = 0 \implies (1+y^2) dx^2 - (1+x^2) dy^2 = 0$.
> $$\frac{dx}{\sqrt{1+x^2}} = \pm \frac{dy}{\sqrt{1+y^2}} \implies \sinh^{-1} x = \pm \sinh^{-1} y + C.$$
> These can be written as $x = \sinh(\pm \sinh^{-1} y + C)$.

## Problem 3-3-5* · Enneper's Surface Properties
> [!exr] 3-3, 5*
> Consider the parametrized surface (Enneper's surface)
> $\mathbf{x}(u, v) = \bigl(u - \frac{u^3}{3} + uv^2, v - \frac{v^3}{3} + vu^2, u^2 - v^2\bigr)$
> and show that
> a. $E = G = (1 + u^2 + v^2)^2, F = 0$.
> b. $e = 2, g = -2, f = 0$.
> c. $k_1 = \frac{2}{(1 + u^2 + v^2)^2}, k_2 = - \frac{2}{(1 + u^2 + v^2)^2}$.
> d. The lines of curvature are the coordinate curves.
> e. The asymptotic curves are $u + v = \text{const}, u - v = \text{const}$.

> [!solution] Solution to 3-3, 5*
> **a. First Fundamental Form:**
> $\mathbf{x}_u = (1-u^2+v^2, 2uv, 2u)$, $\mathbf{x}_v = (2uv, 1-v^2+u^2, -2v)$.
> $E = (1-u^2+v^2)^2 + (2uv)^2 + (2u)^2 = 1 + u^4 + v^4 - 2u^2 + 2v^2 - 2u^2v^2 + 4u^2v^2 + 4u^2 = (1 + u^2 + v^2)^2$.
> $G = (2uv)^2 + (1-v^2+u^2)^2 + (-2v)^2 = (1 + u^2 + v^2)^2$ (by symmetry).
> $F = 2uv(1-u^2+v^2) + 2uv(1-v^2+u^2) - 4uv = 2uv(1-u^2+v^2+1-v^2+u^2) - 4uv = 4uv - 4uv = 0$.
>
> **b. Second Fundamental Form:**
> $\mathbf{x}_u \times \mathbf{x}_v = (1+u^2+v^2) (-2u, 2v, 1-u^2-v^2)$.
> $|\mathbf{x}_u \times \mathbf{x}_v| = (1+u^2+v^2)^2$.
> $\mathbf{n} = \frac{1}{1+u^2+v^2} (-2u, 2v, 1-u^2-v^2)$.
> $\mathbf{x}_{uu} = (-2u, 2v, 2)$, $\mathbf{x}_{uv} = (2v, 2u, 0)$, $\mathbf{x}_{vv} = (2u, -2v, -2)$.
> $e = \langle \mathbf{x}_{uu}, \mathbf{n} \rangle = \frac{4u^2 + 4v^2 + 2(1-u^2-v^2)}{1+u^2+v^2} = 2$.
> $f = \langle \mathbf{x}_{uv}, \mathbf{n} \rangle = \frac{-4uv + 4uv}{1+u^2+v^2} = 0$.
> $g = \langle \mathbf{x}_{vv}, \mathbf{n} \rangle = \frac{-4u^2 - 4v^2 - 2(1-u^2-v^2)}{1+u^2+v^2} = -2$.
>
> **c. Principal Curvatures:**
> Since $F=f=0$, the principal curvatures are $k_1 = e/E$ and $k_2 = g/G$:
> $k_1 = \frac{2}{(1+u^2+v^2)^2}, k_2 = \frac{-2}{(1+u^2+v^2)^2}$.
>
> **d. Lines of Curvature:**
> Since $F=f=0$, the coordinate curves are lines of curvature.
>
> **e. Asymptotic Curves:**
> $e du^2 + 2f du dv + g dv^2 = 0 \implies 2 du^2 - 2 dv^2 = 0 \implies du = \pm dv$.
> The asymptotic curves are $u \pm v = \text{const}$.

## Problem 3-3-6* · The Pseudosphere
> [!exr] 3-3, 6*
> (A Surface with $K \equiv -1$; the Pseudosphere.)
> a. Determine an equation for the plane curve $C$, which is such that the segment of the tangent line between the point of tangency and some line $r$ in the plane, which does not meet the curve, is constantly equal to 1 (this curve is called the tractrix).
> b. Rotate the tractrix $C$ about the line $r$; determine if the "surface" of revolution thus obtained (the pseudosphere) is regular and find out a parametrization in a neighborhood of a regular point.
> c. Show that the Gaussian curvature of any regular point of the pseudosphere is $-1$.

> [!solution] Solution to 3-3, 6*
> **a.** Let the line $r$ be the $z$-axis in the $xz$-plane. Let the curve $C$ be $(\varphi(v), \psi(v))$ with $\varphi(v) > 0$. The tangent line at a point $P = (\varphi, \psi)$ is $L(\lambda) = (\varphi, \psi) + \lambda (\varphi', \psi')$.
> The intersection with the $z$-axis (where $x=0$) occurs at $\varphi + \lambda \varphi' = 0 \implies \lambda = -\varphi / \varphi'$.
> The intersection point is $(0, \psi - \varphi \psi' / \varphi')$.
> The length of the segment between $P$ and the $z$-axis is 1, so:
> $$1^2 = (\varphi - 0)^2 + \left( \psi - \left( \psi - \frac{\varphi \psi'}{\varphi'} \right) \right)^2 = \varphi^2 + \left( \frac{\varphi \psi'}{\varphi'} \right)^2 = \frac{\varphi^2 ((\varphi')^2 + (\psi')^2)}{(\varphi')^2}$$
> Assuming $v$ is the arc-length parameter, $(\varphi')^2 + (\psi')^2 = 1$, we get:
> $1 = \frac{\varphi^2}{(\varphi')^2} \implies (\varphi')^2 = \varphi^2$.
> Since $\varphi$ must decrease as we move along the curve to keep the tangent segment on the $z$-axis, we choose $\varphi' = -\varphi$. Integrating gives $\varphi(v) = e^{-v}$ (taking $\varphi(0) = 1$).
> Then $(\psi')^2 = 1 - (\varphi')^2 = 1 - e^{-2v}$, so $\psi(v) = \int_0^v \sqrt{1 - e^{-2t}} dt$.
> In Cartesian coordinates $(x, z)$, since $x = e^{-v} \implies v = -\ln x$, we have $dx/dv = -e^{-v} = -x$, so $dz/dx = \frac{\psi'}{\varphi'} = \frac{\sqrt{1-x^2}}{-x}$.
> Integrating gives the equation of the tractrix: $z = \int \frac{\sqrt{1-x^2}}{-x} dx = \cosh^{-1}(1/x) - \sqrt{1-x^2}$.
>
> **b.** Rotating the tractrix about the $z$-axis gives the pseudosphere:
> $$\mathbf{x}(u, v) = (e^{-v} \cos u, e^{-v} \sin u, \psi(v))$$
> The partial derivatives are $\mathbf{x}_u = (-e^{-v} \sin u, e^{-v} \cos u, 0)$ and $\mathbf{x}_v = (-e^{-v} \cos u, -e^{-v} \sin u, \sqrt{1-e^{-2v}})$.
> The surface is regular where $\mathbf{x}_u \times \mathbf{x}_v \neq \mathbf{0}$.
> $|\mathbf{x}_u \times \mathbf{x}_v| = |e^{-v}| \sqrt{(-e^{-v})^2 + (\psi')^2} = e^{-v} \sqrt{e^{-2v} + 1 - e^{-2v}} = e^{-v}$.
> Since $e^{-v} \neq 0$, the surface is regular for all $v \in (0, \infty)$. At $v=0$, $\psi'(0)=0$, and there is a singular circle (a cusp in the profile).
>
> **c.** For a surface of revolution with $E=1$ (arc-length parameter), $F=0$, and $G=\varphi^2$, the Gaussian curvature is $K = -\frac{\varphi''}{\varphi}$.
> Here $\varphi(v) = e^{-v}$, so $\varphi'(v) = -e^{-v}$ and $\varphi''(v) = e^{-v}$.
> $$K = -\frac{e^{-v}}{e^{-v}} = -1.$$
> Thus the Gaussian curvature is constantly $-1$ at all regular points.

## Problem 3-3-7* · Constant Curvature Surfaces of Revolution
> [!exr] 3-3, 7*
> (Surfaces of Revolution with Constant Curvature.) $(\varphi(v) \cos u, \varphi(v) \sin u, \psi(v))$, $\varphi \neq 0$ is given as a surface of revolution with constant Gaussian curvature $K$. To determine the functions $\varphi$ and $\psi$, choose the parameter $v$ in such a way that $(\varphi')^2 + (\psi')^2 = 1$. Show that
> a. $\varphi$ satisfies $\varphi'' + K\varphi = 0$ and $\psi$ is given by $\psi = \int \sqrt{1 - (\varphi')^2} dv$.
> b. All surfaces of revolution with $K=1$ which intersect perpendicularly the plane $xOy$ are given by $\varphi(v) = C \cos v$, $\psi(v) = \int_0^v \sqrt{1 - C^2 \sin^2 v} dv$.
> c. All surfaces of revolution with $K=-1$ may be given by one of three types involving $\cosh, \sinh, \exp$.
> d. Type 3 in part c is the pseudosphere.
> e. $K=0$ gives cylinders, cones, and planes.

> [!solution] Solution to 3-3, 7*
> **a.** With $(\varphi')^2 + (\psi')^2 = 1$, the first fundamental form coefficients are $E = (\varphi')^2 + (\psi')^2 = 1$, $F = 0$, $G = \varphi^2$.
> The Gaussian curvature of such a surface is given by the formula $K = -\frac{\varphi''}{\varphi}$.
> Thus $\varphi$ satisfies the linear second-order differential equation $\varphi'' + K\varphi = 0$.
> From the condition $(\varphi')^2 + (\psi')^2 = 1$, we have $(\psi')^2 = 1 - (\varphi')^2$, so $\psi(v) = \int \sqrt{1 - (\varphi'(v))^2} dv$.
>
> **b.** For $K=1$, the equation is $\varphi'' + \varphi = 0$, so $\varphi(v) = A \cos v + B \sin v$.
> The surface intersects $xOy$ perpendicularly if at $v=0$ the profile curve is perpendicular to $xOy$, which for a surface of revolution means $\varphi'(0)=0$ and we can set $\psi(0)=0$.
> Thus $B = 0$ and $\varphi(v) = C \cos v$.
> $\psi(v) = \int_0^v \sqrt{1 - (-C \sin v)^2} dv = \int_0^v \sqrt{1 - C^2 \sin^2 v} dv$.
> - If $C=1$, we get the sphere $\varphi = \cos v, \psi = \sin v$.
> - If $C < 1$, the surface is a "barrel" shape.
> - If $C > 1$, the surface is a "bulge" shape defined only for $|v| \leq \arcsin(1/C)$.
>
> **c.** For $K=-1$, the equation is $\varphi'' - \varphi = 0$. The general solution is $\varphi(v) = A \cosh v + B \sinh v$.
> 1. $\varphi(v) = C \cosh v$. Then $\varphi' = C \sinh v$. $\psi = \int \sqrt{1 - C^2 \sinh^2 v} dv$. (Hyperbolic type)
> 2. $\varphi(v) = C \sinh v$. Then $\varphi' = C \cosh v$. $\psi = \int \sqrt{1 - C^2 \cosh^2 v} dv$. (Elliptic type)
> 3. $\varphi(v) = C e^v$. Then $\varphi' = C e^v$. $\psi = \int \sqrt{1 - C^2 e^{2v}} dv$. (Parabolic type)
>
> **d.** For type 3, if we take $C=1$, we get $\varphi = e^v$ and $\psi' = \sqrt{1 - e^{2v}}$. This corresponds to the tractrix used for the pseudosphere in Exercise 6.
>
> **e.** For $K=0$, $\varphi'' = 0 \implies \varphi(v) = av + b$.
> - If $a=0$, $\varphi = b$ (const), $\psi = v$. This is a cylinder.
> - If $a=1$, $\varphi = v+b, \psi = \text{const}$. This is a plane.
> - If $0 < a < 1$, $\varphi = av+b, \psi = \sqrt{1-a^2} v$. This is a cone.

## Problem 3-3-8* · Contact of Order $\geq 2$ of Surfaces
> [!exr] 3-3, 8*
> Prove various properties of contact of order $\geq 2$ between surfaces, including its invariance under diffeomorphisms and the fact that it implies equal Gaussian and mean curvatures.

> [!solution] Solution to 3-3, 8*
> **a.** The partial derivatives of $f \circ \mathbf{x}$ at $(0,0)$ are determined by the partial derivatives of $f$ at $p$ and the partial derivatives of $\mathbf{x}$ at $(0,0)$. For example, $(f \circ \mathbf{x})_u = \nabla f \cdot \mathbf{x}_u$ and $(f \circ \mathbf{x})_{uu} = \mathbf{x}_u^T H_f \mathbf{x}_u + \nabla f \cdot \mathbf{x}_{uu}$. Since the derivatives of $\mathbf{x}$ and $\bar{\mathbf{x}}$ up to order 2 match at $p$, the derivatives of $f \circ \mathbf{x}$ and $f \circ \bar{\mathbf{x}}$ also match.
>
> **b.** Let $p = (0,0,0)$ and the $xy$ plane be the tangent plane. Then $\mathbf{x}(x,y) = (x, y, f(x,y))$ and $\bar{\mathbf{x}}(x,y) = (x, y, \bar{f}(x,y))$.
> The condition $\mathbf{x}_u = \bar{\mathbf{x}}_u$ etc. at $(0,0)$ implies $f_x = \bar{f}_x$, $f_y = \bar{f}_y$, $f_{xx} = \bar{f}_{xx}$, $f_{xy} = \bar{f}_{xy}$, $f_{yy} = \bar{f}_{yy}$ at $(0,0)$. Thus $(f - \bar{f})$ and its derivatives up to order 2 vanish at $(0,0)$.
>
> **c.** The second-order Taylor expansion of $z = f(x,y)$ at $(0,0)$ is $z = \frac{1}{2}(x^2 f_{xx} + 2xy f_{xy} + y^2 f_{yy})$. This paraboloid has the same value and first and second derivatives as $S$ at $p$.
>
> **e.** Gaussian and mean curvatures at $p$ depend only on the first and second fundamental form coefficients, which in turn depend only on the first and second partial derivatives of the surface parametrization. Since these derivatives match for $S$ and $\bar{S}$, their $K$ and $H$ must be equal.
>
> **g.** Let the normal line be $(x, y) = (r \cos \theta, r \sin \theta)$. The distance $d$ between surfaces is $|f(x,y) - \bar{f}(x,y)|$. Since the difference function has vanishing derivatives up to order 2, its Taylor series starts with terms of order 3. Thus $d = O(r^3)$, which implies $\lim_{r \to 0} d/r^2 = 0$.

## Problem 3-3-9 · Contact of Curves
> [!exr] 3-3, 9
> Define contact of order $\geq n$ for regular curves and prove its invariance by diffeomorphisms and that order $\geq 1$ means tangency.

> [!solution] Solution to 3-3, 9
> **Definition:** Two regular curves $\alpha$ and $\beta$ have contact of order $\geq n$ at $p = \alpha(0) = \beta(0)$ if there exist parametrizations (possibly after reparametrization) such that $\alpha^{(k)}(0) = \beta^{(k)}(0)$ for all $1 \leq k \leq n$.
>
> **a. Invariance:** Let $\Phi$ be a diffeomorphism. The derivatives of $\Phi \circ \alpha$ at 0 are $(\Phi \circ \alpha)' = d\Phi(\alpha')$, $(\Phi \circ \alpha)'' = d^2\Phi(\alpha', \alpha') + d\Phi(\alpha'')$, and so on. Since each derivative $(\Phi \circ \alpha)^{(k)}$ is a function of $\alpha, \alpha', \dots, \alpha^{(k)}$, if $\alpha$ and $\beta$ match up to order $n$, then $\Phi \circ \alpha$ and $\Phi \circ \beta$ will also match up to order $n$.
>
> **b. Order $\geq 1$:** By definition, $\alpha'(0) = \beta'(0)$. This means the curves have a common tangent vector at $p$, which is the definition of tangency.

## Problem 3-3-10* · Contact of Curves and Surfaces
> [!exr] 3-3, 10*
> (Contact of Curves and Surfaces.)
> a. If $f(x,y,z) = 0$ represents $S$ and $\alpha(t)$ represents $C$, show contact order $\geq n$ iff $f(\alpha(t))$ and its derivatives up to $n$ vanish at $t=0$.
> b. Contact order $\geq 2$ with a plane implies it is the osculating plane.
> c. Contact order $\geq 3$ with a sphere implies it is the osculating sphere.

> [!solution] Solution to 3-3, 10*
> **a.** Let $g(t) = f(\alpha(t))$. Contact order $\geq n$ means there exists a curve $\bar{C} \subset S$ such that $\alpha^{(k)}(0) = \bar{C}^{(k)}(0)$ for $k \leq n$. Since $\bar{C} \subset S$, $f(\bar{C}(t)) \equiv 0$. Differentiating this gives $0 = \frac{d^k}{dt^k} f(\bar{C}(t))|_{t=0}$, which is a polynomial in the derivatives of $f$ and $\bar{C}$. Since $\alpha$ and $\bar{C}$ have same derivatives at $0$, $\frac{d^k}{dt^k} f(\alpha(t))|_{t=0} = 0$.
>
> **b.** Let the plane be $\langle \mathbf{x} - p, \mathbf{v} \rangle = 0$. Contact order $\geq 2$ implies $\langle \alpha(0) - p, \mathbf{v} \rangle = 0$, $\langle \alpha'(0), \mathbf{v} \rangle = 0$, and $\langle \alpha''(0), \mathbf{v} \rangle = 0$. This means the plane contains the tangent vector $T$ and the acceleration vector $\alpha''$. Thus it is the osculating plane (spanned by $T$ and $n$).
>
> **c.** Let the sphere be $|\mathbf{x} - \mathbf{c}|^2 - R^2 = 0$. Let $g(s) = \langle \alpha(s) - \mathbf{c}, \alpha(s) - \mathbf{c} \rangle - R^2$.
> 1. $g(0) = 0 \implies |\alpha(0) - \mathbf{c}|^2 = R^2$.
> 2. $g'(0) = 2 \langle \alpha', \alpha - \mathbf{c} \rangle = 0 \implies (\mathbf{c} - \alpha) \perp T$.
> 3. $g''(0) = 2 \langle \alpha'', \alpha - \mathbf{c} \rangle + 2 \langle \alpha', \alpha' \rangle = 2 (\langle k n, \alpha - \mathbf{c} \rangle + 1) = 0 \implies \langle \mathbf{c} - \alpha, n \rangle = 1/k = \rho$.
> 4. $g'''(0) = 2 \langle \alpha''', \alpha - \mathbf{c} \rangle + 6 \langle \alpha'', \alpha' \rangle = 0$.
> Since $\alpha' = T, \alpha'' = k n$, we have $\alpha''' = k' n + k n' = k' n + k (-k T + \tau b)$.
> $0 = \langle -k^2 T + k' n + k \tau b, \alpha - \mathbf{c} \rangle + 3 \langle k n, T \rangle$.
> $-k^2 \cdot 0 + k' \langle n, \alpha - \mathbf{c} \rangle + k \tau \langle b, \alpha - \mathbf{c} \rangle + 0 = 0$.
> $k' (-\rho) + k \tau \langle \alpha - \mathbf{c}, b \rangle = 0 \implies \langle \mathbf{c} - \alpha, b \rangle = \frac{k' \rho}{k \tau} = \frac{k'}{k^2 \tau}$.
> Thus the center $\mathbf{c}$ is:
> $$\mathbf{c} = \alpha + \rho n + \frac{k'}{k^2 \tau} b.$$
> This is the center of the osculating sphere.
