# Summary: Towards a category-theoretic foundation of Classical and Quantum Information Geometry

**Authors:** F. M. Ciaglia, F. Di Cosmo, L. González-Bravo  
**Date:** September 15, 2025  
**arXiv:** 2509.10262v1 [math-ph]

## 1. Motivation

The primary motivation of this work is to provide a unified and structurally robust framework for **Information Geometry** that encompasses both classical and quantum theories, while also extending to infinite-dimensional settings.

### The Problem with Existing Frameworks
*   **Classical Case:** Čencov's theorem characterizes the **Fisher-Rao metric tensor** as the unique metric invariant under congruent embeddings (Markov maps). However, this was originally formulated for **finite probability spaces** (simplexes $\Delta_n$) and leaves out important models with continuous outcome spaces (e.g., multivariate normal distributions).
*   **Quantum Case:** Čencov's ideas were extended to the quantum setting (Petz's theorem), where the invariance condition is replaced by **monotonicity** under completely positive trace-preserving (CPTP) maps. While Petz classified all monotone metrics for finite-dimensional quantum states (via operator monotone functions), this classification excludes **infinite-dimensional algebras** and **non-faithful states** (e.g., pure states).
*   **Generalization Gaps:** Previous attempts to generalize Čencov's theorem to continuous spaces often abandon the original categorical framework or use techniques ill-suited for quantum adaptation.

### The Proposed Solution
The authors propose using **Operator Algebras (W\*-algebras)** as a common language, treating probability distributions and quantum states as distinct realizations of normal states on W\*-algebras (Abelian for classical, non-Abelian for quantum). Since the set of states on an infinite-dimensional W\*-algebra is not a smooth manifold, the authors shift from a manifold-oriented approach to a **category-theoretic approach**, introducing the category **NCP** (Non-Commutative Probabilities).

---

## 2. Theoretical Construction

The core contribution is the construction of the category **NCP** and the redefinition of geometric structures (metrics) as functors.

### 2.1 The Category NCP
The category **NCP** serves as a "universal model" or ambient space for all statistical models.

*   **Objects:** Pairs $(\mathcal{A}, \rho)$, where:
    *   $\mathcal{A}$ is a **W\*-algebra**.
    *   $\rho$ is a **normal state** on $\mathcal{A}$.
*   **Morphisms:** A morphism $\Phi: (\mathcal{A}, \rho) \to (\mathcal{B}, \sigma)$ exists if there is a **state-preserving CPU map** (unital completely positive map) $\phi: \mathcal{B} \to \mathcal{A}$ such that:
    $$\phi^*(\rho) = \sigma$$
    This effectively captures the idea of "coarse-graining" or statistical processing in the reverse direction of the algebraic map.

### 2.2 Fields of Covariances
Instead of defining Riemannian metric tensors on tangent bundles (which is problematic in infinite dimensions without manifold structure), the authors introduce **Fields of Covariances** as **contravariant functors** from NCP to the category of Hilbert spaces (**Hilb**).

*   **GNS Functor ($\mathcal{G}$):**
    *   Assigns to each object $(\mathcal{A}, \rho)$ the **GNS Hilbert space** $\mathcal{H}_\rho$ (from the Gelfand-Naimark-Segal construction).
    *   On morphisms, it acts via the contraction determined by the CPU map.
*   **Field of Covariances ($\mathcal{C}$):**
    *   A functor $\mathcal{C}: \mathrm{NCP} \to \mathrm{Hilb}$ such that $\mathcal{C}_0(\mathcal{A}, \rho) = (\mathcal{K}_\rho, C_\rho)$.
    *   **Condition:** It must satisfy $\mathcal{F} \circ \mathcal{C} = \mathcal{F} \circ \mathcal{G}$, where $\mathcal{F}$ is the forgetful functor. This implies the underlying vector space is always the GNS space $\mathcal{H}_\rho$, but the inner product (covariance) $C_\rho$ may differ.
*   **Monotonicity:** The functoriality of $\mathcal{C}$ automatically encodes the **monotonicity property** (contractivity of morphisms), which is the central requirement in quantum information geometry:
    $$C_\rho(\Phi(\xi), \Phi(\xi)) \leq C_\sigma(\xi, \xi)$$

### 2.3 Statistical Models as Subcategories
A statistical model is no longer a manifold but a **Statistical Subcategory** of NCP.
*   **Embedding:** A classical manifold $M$ (e.g., Gaussian distributions) is embedded into NCP via an injective functor $i$.
*   **Symmetries:** Geometric structures like Lie group actions on the model are encoded as functors from the action groupoid $G \ltimes M$ to NCP.
    *   *Example:* For univariate normal distributions, the affine group action on $\mathbb{R}$ is lifted to automorphisms of the algebra $L^\infty(\mathbb{R})$, defining a subcategory of NCP.

---

## 3. Connection to Classical and Quantum Information Geometry

The framework unifies existing geometries by deriving them from fields of covariances on the ambient category NCP.

### 3.1 Classical Connection
*   **Fisher-Rao Metric:** In the classical commutative case (e.g., $\mathcal{A} = L^\infty(\Omega, \nu)$), the GNS functor $\mathcal{G}$ reduces to the standard **statistical covariance**. Since the Fisher-Rao metric is essentially the inverse of the covariance matrix, the GNS functor naturally recovers the Fisher-Rao geometry.
*   **Čencov's Theorem:** The classification of fields of covariances on NCP is framed as the generalized Čencov problem. The authors suggest that for tracial states on finite-dimensional algebras, the GNS functor is the *unique* field of covariance (mirroring Čencov's uniqueness result).

### 3.2 Quantum Connection
*   **Petz's Classification:** The problem of classifying fields of covariances on NCP encompasses Petz's classification of monotone quantum metrics. Different operator monotone functions correspond to different functors $\mathcal{C}$ satisfying the field of covariance condition.
*   **Bures-Helstrom Metric:** The authors mention that specific fields of covariances will lead to the **Bures-Helstrom metric tensor** when applied to the subcategory of faithful states on $\mathcal{B}(\mathcal{H})$.
*   **Fubini-Study Metric:** This can also be recovered for pure states, addressing a case often excluded by standard monotone metric classifications.

### 3.3 Summary of Unification
| Concept | Classical / Standard | Category-Theoretic (NCP) |
| :--- | :--- | :--- |
| **Space** | Manifold $M$ | Category NCP (or subcategory) |
| **Point** | Distribution $p_\theta$ / State $\rho$ | Object $(\mathcal{A}, \rho)$ |
| **Map** | Markov / CPTP Map | Morphism (Dual of CPU map) |
| **Metric** | Riemannian Tensor $g$ | Field of Covariances Functor $\mathcal{C}$ |
| **Geometry** | Fisher-Rao / Bures | Induced by $\mathcal{C}$ (e.g., GNS functor) |

This work sets the stage for a purely categorical derivation of information geometric structures, independent of the specific model implementation (classical vs. quantum, finite vs. infinite).

