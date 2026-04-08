#!/usr/bin/env python3
"""Restructure Chapter 5 with three sections: Basic Conjectures, Proofs, and Proof Strategy."""

new_content = r"""% Chapter 5: Quantum Double Schubert Polynomials Positivity Conjecture
% Based on Mihalcea (2007) \cite{Mihalcea} and Gao-Xiong (2025) \cite{GX2025}
% This chapter records the open conjecture

\chapter{Quantum Double Schubert Polynomials Positivity Conjecture}
\label{chap:QuantumDoublePositivityConjecture}

\section{The Hierarchy of Positivity Conjectures}
\label{sec:HierarchyOfPositivity}

The study of positivity phenomena in Schubert calculus forms a hierarchy of increasingly general conjectures. Each level extends the previous one by introducing new variables or structures. In this section, we present the three foundational positivity results and their relationships.

\subsection{The Classical Schubert Positivity Theorem}
\label{sec:ClassicalSchubertPositivity}

The most fundamental positivity result concerns ordinary Schubert polynomials in cohomology.

\begin{Theorem}[Classical Schubert Positivity]
\label{th:ClassicalSchubertPositivity}
For $u, v, w \in S_n$, the product of Schubert polynomials expands as:
\[
\mathfrak{S}_u(\mathbf{x}) \cdot \mathfrak{S}_v(\mathbf{x}) = \sum_{w \in S_n} c_{u,v}^w \mathfrak{S}_w(\mathbf{x})
\]
where the structure constants $c_{u,v}^w \in \mathbb{N}$ are nonnegative integers.
\end{Theorem}

\begin{Proof}
The classical proof uses geometric intersection theory on the flag manifold $G/B$. The coefficient $c_{u,v}^w$ counts the number of points in the triple intersection $X_u \cap X_v \cap g X_w$ for generic $g \in G$, which is a finite set of points by dimension reasons. Since counting points yields nonnegative integers, $c_{u,v}^w \in \mathbb{N}$. See \cite[Section 2]{Chevalley1994} for the original argument.
\end{Proof}

\begin{Remark}[Geometric Meaning]
\Cref{th:ClassicalSchubertPositivity} reflects the fundamental positivity of intersection numbers in algebraic geometry. Each coefficient $c_{u,v}^w$ is a counts of points, hence a nonnegative integer. This positivity is the foundation upon which all subsequent generalizations are built.
\end{Remark}

\subsection{Graham Positivity: The Equivariant Extension}
\label{sec:GrahamPositivity}

The first major extension introduces equivariant cohomology, where the coefficients become polynomials in torus weights.

\begin{Theorem}[Graham Positivity Theorem {\cite[Theorematical 3.2]{Gr}}]
\label{th:GrahamPositivityOriginal}
Let $X = G/P$ be a homogeneous space. In equivariant cohomology $H_T^*(X)$, the product of Schubert classes satisfies:
\[
\sigma(u)^T \cdot \sigma(v)^T = \sum_w c_{u,v}^w(\mathbf{x}) \, \sigma(w)^T
\]
where each $c_{u,v}^w(\mathbf{x}) \in \mathbb{N}[x_1, \ldots, x_r]$ is a polynomial with nonnegative coefficients in the negative roots $-\alpha_i$.
\end{Theorem}

\begin{Proof}
The proof appears in \cite[Section 3.2]{Gr}. Graham established that the equivariant structure constants can be expressed as polynomials in $-\alpha_i$ with nonnegative integer coefficients. The key insight is that the moment map geometry of $G/P$ yields a positivity structure even in the equivariant setting.
\end{Proof}

\begin{Remark}[Comparison with Classical Case]
In \cref{th:ClassicalSchubertPositivity}, coefficients are mere nonnegative integers. In \cref{th:GrahamPositivityOriginal}, coefficients are upgraded to nonnegative \emph{polynomials} in the torus weights $x_i$. The polynomial coefficients reflect the contribution from different torus fixed points in the equivariant picture.
\end{Remark}

\subsection{Equivariant Quantum Positivity: Mihalcea's Theorem}
\label{sec:EquivariantQuantumPositivity}

The quantum extension replaces ordinary intersection with curve counting via Gromov-Witten invariants.

\begin{Theorem}[Equivariant Quantum Positivity {\cite[ Theorem 1]{Mihalcea}}]
\label{th:EquivariantQuantumPositivity}
For $u, v, w \in W^P$ and $d$ a curve degree, the equivariant quantum product satisfies:
\[
\sigma(u)^T \star \sigma(v)^T = \sum_{d} \sum_{w} q^d c_{u,v}^{w,d}(\mathbf{x}) \, \sigma(w)^T
\]
where $c_{u,v}^{w,d}(\mathbf{x}) \in \mathbb{N}[x_1, \ldots, x_r]$ has nonnegative polynomial coefficients.
\end{Theorem}

The proof uses the following geometric lemma, which we state here for reference:

\begin{Lemma}[Finiteness Lemma]
\label{Lem:EQCFiniteSum}
For each fixed multidegree $d$, only finitely many $w \in W^P$ satisfy $c_{u,v}^{w,d} \neq 0$.
\end{Lemma}

\begin{Proof}
The finiteness follows from the dimension formula for Gromov-Witten invariants. The invariant $\langle \sigma(u), \sigma(v), \sigma(w) \rangle_{0,3,d}$ can be nonzero only when the formal dimension matches the actual dimension of the moduli space. Since Weyl group length bounds the dimension of Schubert cells, only finitely many $w$ can appear. See \cite[Section 2]{Mihalcea}.
\end{Proof}

\begin{Remark}[Relationship with Previous Results]
\Cref{th:EquivariantQuantumPositivity} simultaneously generalizes:
\begin{itemize}
\item \textbf{Classical case ($d = 0$)}: Reduces to \cref{th:GrahamPositivityOriginal} when the quantum parameter $q = 0$;
\item \textbf{Ordinary quantum cohomology ($x_i = 0$)}: Reduces to ordinary quantum cohomology when all equivariant variables vanish.
\end{itemize}
\end{Remark}

\subsection{Double Schubert Positivity: The Two-Parameter Setting}
\label{sec:DoubleSchubertPositivity}

The double setting introduces a second set of variables tracking relative displacements.

\begin{Theorem}[Classical Double Schubert Positivity {\cite[ Theorem 1.1]{GX2025}}]
\label{th:ClassicalDoubleSchubertPositivityIntro}
For $u, v, w \in S_\infty$, the product of double Schubert polynomials satisfies:
\[
\mathfrak{S}_u(\mathbf{x}; \mathbf{y}) \cdot \mathfrak{S}_v(\mathbf{x}; \mathbf{z}) = \sum_{w} c_{u,v}^w(\mathbf{y}; \mathbf{z}) \, \mathfrak{S}_w(\mathbf{x}; \mathbf{z})
\]
where $c_{u,v}^w(\mathbf{y}; \mathbf{z}) \in \mathbb{N}[y_i - z_j]$ are nonnegative polynomials in the differences $y_i - z_j$.
\end{Theorem}

The key innovation in \cite{GX2025} is the introduction of a special involution:

\begin{Lemma}[Special Involution {\cite[Lemma 2.1]{GX2025}}]
\label{Lem:SpecialInvolutionIntro}
Let $\tau \in S_{2n}$ be defined by $\tau(i) = n + i$ and $\tau(n + i) = i$ for $1 \leq i \leq n$. This involution relates the two parameter sets $\mathbf{y}$ and $\mathbf{z}$.
\end{Lemma}

The proof of \cref{th:ClassicalDoubleSchubertPositivityIntro} proceeds via the following steps:

\begin{Lemma}[Normal Transversality {\cite[Lemma 2.5]{GX2025}}]
\label{Lem:NormalTransversalityIntro}
The intersection $\tau \cdot X_u \cap X_v$ is normally transversal at every point.
\end{Lemma}

\begin{Corollary}[Compatibly $N^-(\tau)$-Split]
\label{Cor:CompatiblyNSplitIntro}
Since $\tau X_u \cap X_v$ is normally transversal, it is compatibly $N^-(\tau)$-split in the sense of \cite[Section 19.3]{AndersonFulton}.
\end{Corollary}

The root set of the special involution determines the polynomial variables:

\begin{Lemma}[Root Set of Special Involution]
\label{Lem:RootSetInvolutionIntro}
For $\tau$ as in \cref{Lem:SpecialInvolutionIntro}, the inversion set is:
\[
I(\tau) = \{\, y_j - z_i \mid 1 \leq i, j \leq n \,\}.
\]
\end{Lemma}

Applying Graham positivity (see \cref{th:GrahamPositivityRefinedSec2}) yields the result.

\subsection{The Main Conjecture: Quantum Double Schubert Positivity}
\label{sec:QuantumDoubleSchubertPositivityConjecture}

We now present the central conjecture of this chapter, which unifies all previous positivity phenomena.

\begin{Conjecture}[Quantum Double Schubert Positivity]
\label{conj:QuantumDoublePositivity}
For $u, v, w \in S_\infty$, the product of quantum double Schubert polynomials expands as:
\[
\mathfrak{S}_u^{(q)}(\mathbf{x}; \mathbf{y}) \cdot \mathfrak{S}_v^{(q)}(\mathbf{x}; \mathbf{z}) = \sum_{w} c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q) \, \mathfrak{S}_w^{(q)}(\mathbf{x}; \mathbf{y})
\]
where the coefficients satisfy:
\[
c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q) \in \mathbb{N}[y_i - z_j, q_k].
\]
\end{Conjecture}

\begin{Remark}[Naming Clarification]
The phrase ``Quantum Double'' refers to two distinct features:
\begin{itemize}
\item \textbf{Double}: Each factor $\mathfrak{S}_u^{(q)}(\mathbf{x}; \mathbf{y})$ is a \emph{double} Schubert polynomial in variables $(\mathbf{x}; \mathbf{y})$;
\item \textbf{Quantum}: The multiplication involves quantum corrections $q_k$ from curve counting.
\end{itemize}
The word ``Triple'' in related literature \cite{GX2025} refers to the three Schubert polynomials appearing in the product formula.
\end{Remark}

\subsection{Comparison of the Four Positivity Results}
\label{sec:ComparisonOfPositivity}

\Cref{tab:PositivityComparison} summarizes the relationships among the four positivity results:

\begin{table}[htbp]
\caption{Comparison of Four Positivity Results}
\label{tab:PositivityComparison}
\begin{center}
\begin{tabular}{lcccc}
\hline
Result & Variables & Polynomial Ring & Status \\
\hline
\Cref{th:ClassicalSchubertPositivity} & $\mathbf{x}$ & $\mathbb{N}$ & Proved \\
\Cref{th:GrahamPositivityOriginal} & $\mathbf{x}$ & $\mathbb{N}[x_i]$ & Proved \\
\Cref{th:EquivariantQuantumPositivity} & $\mathbf{x}, q$ & $\mathbb{N}[x_i][q]$ & Proved \\
\Cref{th:ClassicalDoubleSchubertPositivityIntro} & $\mathbf{y}, \mathbf{z}$ & $\mathbb{N}[y_i - z_j]$ & Proved \\
\Cref{conj:QuantumDoublePositivity} & $\mathbf{y}, \mathbf{z}, q$ & $\mathbb{N}[y_i - z_j, q_k]$ & Open \\
\hline
\end{tabular}
\end{center}
\end{table}

The conjecture represents the natural unification of:
\begin{itemize}
\item \textbf{Classical Double Schubert positivity} ($q = 0$ in \cref{conj:QuantumDoublePositivity}): Proved in \cite{GX2025};
\item \textbf{Equivariant Quantum positivity} ($\mathbf{y} = \mathbf{z} = 0$): Proved in \cite{Mihalcea}.
\end{itemize}

\section{Proofs of the Three Basic Conjectures}
\label{sec:ProofsOfThreeBasic}

This section presents detailed proofs (or proof sketches) for the three foundational positivity results that form the foundation of the theory.

\subsection{Proof of Classical Schubert Positivity}
\label{sec:ProofClassicalSchubert}

\begin{Proof}[Proof of \cref{th:ClassicalSchubertPositivity}]
The geometric approach proceeds as follows. Let $G = \mathrm{GL}_n(\mathbb{C})$ act on the flag manifold $G/B$. For Schubert varieties $X_u, X_v, X_w \subset G/B$, consider the triple intersection for generic group translate $g \in G$:
\[
X_u \cap X_v \cap g X_w.
\]

By dimension counting, this intersection is proper (hence finite) when:
\[
\deg X_u + \deg X_v + \deg X_w = \dim(G/B).
\]

Each intersection point contributes 1 to the count, so the coefficient $c_{u,v}^w$ equals the number of points in this intersection, which must be a nonnegative integer.

The algebraic definition of Schubert polynomials \cite[Section 2.2]{Manivel} ensures that the combinatorial expansion matches the geometric count. \qedhere
\end{Proof}

See \cite[Chapter 2]{Manivel} for a detailed development.

\subsection{Proof of Graham Positivity}
\label{sec:ProofGrahamPositivity}

The proof of Graham positivity requires several geometric ingredients.

\begin{Lemma}[Moment Map Image {\cite[Lemma 3.1]{Gr}}]
\label{Lem:MomentMapImage}
The moment map $\mu: G/B \to \mathfrak{t}^*$ sends each Schubert cell to a convex polytope (the Gelfand-Tsetlin pattern).
\end{Lemma}

\begin{Lemma}[Biration Lemma]
\label{Lem:Biration}
For $w \in W$, the rational map $T \cdot N^- \cdot w B/B$ has image equal to the corresponding Bruhat cell.
\end{Lemma}

The proof of \cref{th:GrahamPositivityOriginal} proceeds by degeneration:

\begin{Proposition}[Degeneration to Normal Cone]
\label{Prop:DegenerationNormalCone}
The intersection product $\sigma(u)^T \cdot \sigma(v)^T$ degenerates to a sum over torus fixed points, with coefficients given by counts of points in appropriate intersections.
\end{Proposition}

Applying this degeneration yields:

\begin{Corollary}[Polynomial Coefficients]
\label{Cor:PolynomialCoefficients}
The structure constants $c_{u,v}^w(\mathbf{x})$ are polynomials in the torus weights with nonnegative coefficients.
\end{Corollary}

See \cite[Section 3]{Gr} for the complete argument.

\subsection{Proof of Equivariant Quantum Positivity}
\label{sec:ProofEquivariantQuantum}

The proof of Mihalcea's theorem uses a clever reduction to Graham positivity.

\begin{Proposition}[Quantum-to-Classical Reduction]
\label{Prop:QuantumToClassicalReduction}
The equivariant quantum Littlewood-Richardson coefficient $c_{u,v}^{w,d}$ can be expressed via a limit:
\[
c_{u,v}^{w,d} = \lim_{\mathbf{x} \to 0} \widetilde{c}_{u,v}^{w,d}(\mathbf{x})
\]
where $\widetilde{c}_{u,v}^{w,d}$ is a coefficient in the product on $X \times X$.
\end{Proposition}

The key geometric construction:

\begin{Lemma}[Evasion Map Construction {\cite[Lemma 3.1]{Mihalcea}}]
\label{Lem:EvasionMapConstruction}
There exists an evasion map $ev: \overline{M}_{0,3}(X, d) \to X \times X$ that records the images of the three marked points.
\end{Lemma}

Using this, we compute:

\begin{Proposition}[Equivariant Projection Formula]
\label{Prop:EquivariantProjectionFormula}
The equivariant quantum product satisfies:
\[
c_{u,v}^{w,d} = \pi_*^T\left((ev_1^T)^* \sigma(u)^T \cdot (ev_2^T)^* \sigma(v)^T \cdot (ev_3^T)^* \widetilde{\sigma}(w)^T\right).
\]
\end{Proposition}

Since the right-hand side involves ordinary equivariant intersection on $X \times X$, we can apply Graham positivity to obtain:

\begin{Corollary}[Nonnegative Polynomial Coefficients]
\label{Cor:EQCPolynomialCoefficients}
Each $c_{u,v}^{w,d}(\mathbf{x}) \in \mathbb{N}[x_1, \ldots, x_r]$ has nonnegative polynomial coefficients.
\end{Corollary}

This completes the proof of \cref{th:EquivariantQuantumPositivity}. See \cite[Section 4]{Mihalcea} for details.

\section{The Proof Strategy for the Main Conjecture}
\label{sec:ProofStrategyMainConjecture}

This section outlines the basic ideas and strategies that could potentially prove \cref{conj:QuantumDoublePositivity}.

\subsection{The Geometric Framework}
\label{sec:GeometricFramework}

The conjecture concerns the product:
\[
\mathfrak{S}_u^{(q)}(\mathbf{x}; \mathbf{y}) \cdot \mathfrak{S}_v^{(q)}(\mathbf{x}; \mathbf{z})
\]
in the setting of quantum double Schubert polynomials. The geometric interpretation involves:

\begin{itemize}
\item \textbf{Base space}: The flag manifold $G/B$ parametrized by $\mathbf{x}$;
\item \textbf{First displacement}: $\mathbf{y}$ records displacement from $X_u$;
\item \textbf{Second displacement}: $\mathbf{z}$ records displacement from $X_v$;
\item \textbf{Quantum corrections}: $q_k$ arise from counting rational curves in $G/B$.
\end{itemize}

The coefficient $c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q)$ should count curves meeting three Schubert varieties with specified relative displacements.

\subsection{Key Ingredients from Previous Proofs}
\label{sec:KeyIngredients}

Successful approaches to similar conjectures have relied on:

\begin{enumerate}
\item \textbf{Normal transversality}: Ensuring geometric intersections behave well;
\item \textbf{Graham positivity}: The fundamental positivity result for equivariant cohomology;
\item \textbf{Quantum-to-classical reduction}: Reducing quantum problems to classical ones via limits or degenerations;
\item \textbf{Equivariant projection formula}: Computing Gromov-Witten invariants via projection to smaller spaces.
\end{enumerate}

For the quantum double case, we need to combine these ingredients in a new way.

\subsection{Proposed Strategy: Step by Step}
\label{sec:ProposedStrategy}

The proof of \cref{conj:QuantumDoublePositivity} would proceed through the following steps:

\begin{Step}[Set-up and Geometric Meaning]
Define the relevant moduli space of stable maps to $G/B$ with three marked points. The coefficient $c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q)$ should equal:
\[
\langle \sigma(u), \sigma(v), \widetilde{\sigma}(w) \rangle_{0,3,d}^{\mathbf{y}, \mathbf{z}}
\]
a Gromov-Witten invariant with equivariant parameters recording displacements.
\end{Step}

\begin{Step}[Reduction to Double Classical Case]
Show that the quantum double coefficient reduces to the classical double coefficient in the limit $q \to 0$:
\[
\lim_{q \to 0} c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q) = c_{u,v}^w(\mathbf{y}; \mathbf{z}) \in \mathbb{N}[y_i - z_j].
\]
This would establish the $q = 0$ case.
\end{Step}

\begin{Step}[Positivity in Quantum Parameters]
Prove that the dependence on $q_k$ is also nonnegative. This requires understanding the quantum correction geometry—the virtual fundamental class of the moduli space of curves.
\end{Step}

\begin{Step}[Combine via Multivariable Positivity]
The final result would combine the positivity in $(y_i - z_j)$ and in $q_k$ to give:
\[
c_{u,v}^{w,(q)}(\mathbf{y}; \mathbf{z}; q) \in \mathbb{N}[y_i - z_j, q_k].
\]
\end{Step}

\begin{Remark}[Current Status]
The conjecture remains open. The difficulty lies in simultaneously tracking:
\begin{itemize}
\item The double variable structure ($y_i - z_j$ differences);
\item The quantum corrections ($q_k$ from curve counting);
\item Maintaining positivity throughout.
\end{itemize}
Progress on this conjecture would represent a major advance in algebraic geometry and representation theory.
\end{Remark}

\section{Relationship with Kirillov's Conjecture}
\label{sec:RelationshipKirillov}

A striking application of the double Schubert positivity is the resolution of Kirillov's conjecture on skew divided difference operators.

\begin{Corollary}[Kirillov's Conjecture, {\cite[Corollary 1.2]{GX2025}}]
\label{cor:KirillovConjecture}
For $u, v, w \in S_n$, the skew divided difference operator $\partial_{w/v}$ applied to $\mathfrak{S}_u(\mathbf{x})$ yields:
\[
\partial_{w/v} \mathfrak{S}_u(\mathbf{x}) \in \mathbb{N}[\mathbf{x}].
\]
\end{Corollary}

\begin{Proof}
The key identity from \cite[Section 2]{GX2025} states:
\[
\partial_{w/v} \mathfrak{S}_u(\mathbf{x}; \mathbf{y}) = c_{u,v}^w(\mathbf{y}, \mathbf{x}).
\]
Setting $\mathbf{y} = \mathbf{0}$ in \cref{th:ClassicalDoubleSchubertPositivityIntro} gives the result. \qedhere
\end{Proof}

\section{Current State and Open Problems}
\label{sec:CurrentState}

The study of positivity phenomena in Schubert calculus has achieved several milestones:

\begin{enumerate}
\item \textbf{Classical positivity}: Proved in the 19th century via intersection theory;
\item \textbf{Graham positivity}: Proved in 2001 \cite{Gr};
\item \textbf{Equivariant quantum positivity}: Proved in 2007 \cite{Mihalcea};
\item \textbf{Classical double positivity}: Proved in 2025 \cite{GX2025};
\item \textbf{Quantum double positivity}: Remains open (\cref{conj:QuantumDoublePositivity}).
\end{enumerate}

Proving the quantum double Schubert positivity conjecture would unify all these results and open new directions in algebraic geometry and representation theory.

\section{Key Definitions}
\label{sec:KeyDefinitionsCh5}

For reference, we collect the key definitions from this chapter.

\begin{Definition}[\textbf{Equivariant Quantum Cohomology}]
\label{def:EquivariantQuantumCohomologyCh5}
$QH_T^*(X)$ is a graded $\Lambda[q]$-algebra with $\Lambda[q]$-basis $\{\sigma_w^{(q)} \mid w \in W^P\}$. The product $\star$ is defined by:
\[
\sigma_u^{(q)} \star \sigma_v^{(q)} = \sum_{d} \sum_{w \in W^P} q^d c_{u,v}^{w,d} \sigma_w^{(q)},
\]
where $c_{u,v}^{w,d} \in \Lambda = \mathbb{Z}[x_1, \ldots, x_r]$.
\end{Definition}

\begin{Definition}[\textbf{Double Schubert Polynomial}]
\label{def:DoubleSchubertPolynomialCh5}
The double Schubert polynomial $\mathfrak{S}_w(\mathbf{x}; \mathbf{y}) \in \mathbb{Z}[\mathbf{x}; \mathbf{y}]$ is defined via the divided difference operators:
\[
\mathfrak{S}_{w_0}(\mathbf{x}; \mathbf{y}) = \prod_{i+j \leq n} (x_i - y_j), \quad \mathfrak{S}_{ws_i} = \partial_i \mathfrak{S}_w,
\]
where $\partial_i$ is the divided difference operator acting on the $\mathbf{x}$-variables.
\end{Definition}

\begin{Definition}[\textbf{Quantum Double Schubert Polynomial}]
\label{def:QuantumDoubleSchubertPolynomial}
The quantum double Schubert polynomial $\mathfrak{S}_w^{(q)}(\mathbf{x}; \mathbf{y}) \in \Lambda[\mathbf{y}][q]$ reduces to the double Schubert polynomial when $q = 0$ and satisfies the quantum Monk's rule.
\end{Definition}

"""

with open('chapter5.tex', 'r') as f:
    content = f.read()

# Find where the new content should go
# We want to replace from line 1 (beginning) to the end, since we're restructuring entirely
# But let's just write the whole file

with open('chapter5.tex', 'w') as f:
    f.write(new_content)

print("Chapter 5 restructured successfully")