#!/usr/bin/env python3
with open('chapter5.tex', 'r') as f:
    content = f.read()

old = """The two key conjectures in this framework are:

\\begin{Theorem}[Classical Double Schubert Positivity {\\cite[Theorematical]{GX2025}}]
\\label{thrm:ClassicalDoublePositivity}
For $u, v, w \\in S_{\\infty}$, the product of double Schubert polynomials satisfies:
\\[
\\mathfrak{S}_u(\\mathbf{x}; \\mathbf{y}) \\cdot \\mathfrak{S}_v(\\mathbf{x}; \\mathbf{z}) = \\sum_{w \\in S_n} c_{u,v}^w(\\mathbf{y}; \\mathbf{z}) \\cdot \\mathfrak{S}_w(\\mathbf{x}; \\mathbf{z})
\\]
with coefficients $c_{u,v}^w(\\mathbf{y}; \\mathbf{z}) \\in \\mathbb{N}[y_i - z_j]_{i,j \\geq 1}$.
\\end{Theorem}

\\begin{Proof}
The proof follows the strategy of \\cite[Section 2]{GX2025}\\footnote{See \\cref{sec:GX2025-Section2} (\\cite[Section 2]{GX2025})}, which extends Graham's positivity framework \\cite{Gr}\\footnote{See \\cref{def:GrahamPositivity} (\\cite[Section 2.2]{Gr})} to the double Schubert setting.

\\subsection{Step 1: Geometric set-up}
\\label{sec:GX2025-Section2}
Let $G = \\mathrm{GL}_{2n}(\\mathbb{C})$, and let $B$, $B^-$, $T$ denote the standard Borel subgroup, opposite Borel subgroup, and maximal torus, respectively. Consider the special involution
\\[
\\tau \\in S_{2n}, \\qquad \\tau(i) = n + i, \\quad \\tau(n + i) = i \\quad (1 \\leq i \\leq n).
\\]
This element plays a key role in relating the two parameter sets $\\mathbf{y}$ and $\\mathbf{z}$.

For $w \\in S_\\infty$, denote the opposite Schubert variety by $X_w^\\circ = B^- w B / B$ and its closure by $X_w = \\overline{B^- w B / B}$. The $T$-equivariant cohomology class of $X_w$ is represented by the double Schubert polynomial $\\mathfrak{S}_w(\\mathbf{x}; \\mathbf{y})$\\footnote{The definition of double Schubert polynomials appears in \\cref{def:DoubleSchubertPolynomial}. We refer to \\cite[Section 1.3]{GX2025} for the precise conventions.}

\\subsection{Step 2: Normally transversal intersection}
The following geometric lemma is the engine of the proof. It is proved in \\cite[Lemma 2.5]{GX2025} using the action of the opposite unipotent group $N^- = B^- \\cap \\tau B^- \\tau^{-1}$ on $G/B$.

\\begin{Lemma}[{\\cite[Lemma 2.5]{GX2025}}]
\\label{Lem:NormalTransversalIntersection}
The intersection
\\[
\\tau \\cdot X_u \\cap X_v
\\]
is \\emph{normally transversal} at every point of the scheme-theoretic intersection.
\\end{Lemma}

Here $\\tau \\cdot X_u$ denotes the left translate of $X_u$ by $\\tau$. The geometric meaning of normal transversality is that the intersection product in $T$-equivariant cohomology is given by the cup product of the corresponding characteristic classes; see \\cite[Section 16.5]{AndersonFulton} for the general formalism.

\\subsection{Step 3: Application of Graham positivity}
The key input is Graham's refined positivity theorem \\cite{Gr}\\footnote{See \\cref{th:GrahamPositivityRefined} (\\cite[Corollary 2.4]{GX2025})}, which computes the $T$-equivariant cohomology expansion coefficients in terms of the moment graph of $G/B$.

\\begin{Theorem}[Graham positivity, {\\cite[Corollary 2.4]{GX2025}}]
\\label{th:GrahamPositivityRefined}
Let $w \\in S_n$ and let $I(w) = \\{\\alpha \\in \\Delta^+ \\mid w(\\alpha) \\in \\Delta^-\\}$ be the set of positive roots sent to negative roots by $w$. Then
\\[
[X_w]_T = \\sum_{v \\leq w} c_{v,w} \\cdot [\\overline{B^- v B / B}]_T, \\qquad c_{v,w} \\in \\mathbb{N}[-\\alpha]_{\\alpha \\in I(w)}.
\\]
\\end{Theorem}

Applying \\cref{th:GrahamPositivityRefined} to the normally transversal intersection $\\tau X_u \\cap X_v$ and using the projection formula, we obtain
\\[
[\\tau X_u \\cap X_v]_T = \\sum_{w \\in S_n} c_{u,v}^w(\\mathbf{y}, \\mathbf{z}) \\cdot [X_w]_T,
\\]
where the coefficients $c_{u,v}^w(\\mathbf{y}, \\mathbf{z})$ are the structure constants of the double Schubert polynomial multiplication.

Since the intersection $\\tau X_u \\cap X_v$ is normally transversal, it is in particular \\emph{compatibly $N^-(\\tau)$-split} in the sense of \\cite[Section 19.3]{AndersonFulton}, where $N^-(\\tau) = N^- \\cap \\tau N^- \\tau^{-1}$. By \\cite[Corollary 2.4]{GX2025}, the coefficients $c_{u,v}^w$ therefore lie in
\\[
\\mathbb{N}[-\\alpha]_{\\alpha \\in I(\\tau)}.
\\]

\\subsection{Step 4: Computing the root set}
It remains to identify the set $I(\\tau)$. Since $\\tau$ swaps the first $n$ indices with the last $n$ indices, the roots sent to negative roots are precisely
\\[
I(\\tau) = \\{\\, y_j - z_i \\mid 1 \\leq i, j \\leq n \\,},
\\]
where $y_1, \\ldots, y_n$ are the weights of the first set of variables and $z_1, \\ldots, z_n$ are the weights of the second set. Consequently
\\[
c_{u,v}^w(\\mathbf{y}, \\mathbf{z}) \\in \\mathbb{N}[y_j - z_i \\mid 1 \\leq i,j \\leq n]_{i,j \\geq 1},
\\]
which proves \\cref{thrm:ClassicalDoublePositivity} and hence \\cref{conj:QuantumDoubleSchubertPositivity}.

Finally, by the stability of Schubert polynomials \\cite[Section 2.4]{Mihalcea}, the finite-$n$ statement extends to all $u, v, w \\in S_\\infty$ without modification. \\qedhere
\\end{Proof}"""

new = r"""The two key conjectures in this framework are:

\begin{Lemma}[Special Involution {\cite[Lemma 2.1]{GX2025}}]
\label{Lem:SpecialInvolution}
Let $G = \mathrm{GL}_{2n}(\mathbb{C})$, and let $B$, $B^-$, $T$ denote the standard Borel subgroup, opposite Borel subgroup, and maximal torus, respectively. Consider the special involution
\[
\tau \in S_{2n}, \qquad \tau(i) = n + i, \quad \tau(n + i) = i \quad (1 \leq i \leq n).
\]
This element plays a key role in relating the two parameter sets $\mathbf{y}$ and $\mathbf{z}$.
\end{Lemma}

For $w \in S_\infty$, denote the opposite Schubert variety by $X_w^\circ = B^- w B / B$ and its closure by $X_w = \overline{B^- w B / B}$. The $T$-equivariant cohomology class of $X_w$ is represented by the double Schubert polynomial $\mathfrak{S}_w(\mathbf{x}; \mathbf{y})$.

\begin{Lemma}[Normal Transversality {\cite[Lemma 2.5]{GX2025}}]
\label{Lem:NormalTransversality}
The intersection
\[
\tau \cdot X_u \cap X_v
\]
is \emph{normally transversal} at every point of the scheme-theoretic intersection.
\end{Lemma}

Here $\tau \cdot X_u$ denotes the left translate of $X_u$ by $\tau$. The geometric meaning of normal transversality is that the intersection product in $T$-equivariant cohomology is given by the cup product of the corresponding characteristic classes; see \cite[Section 16.5]{AndersonFulton} for the general formalism.

\begin{Corollary}[Compatibly $N^-(\tau)$-Split]
\label{Cor:CompatiblyNSplit}
Since the intersection $\tau X_u \cap X_v$ is normally transversal, it is in particular \emph{compatibly $N^-(\tau)$-split} in the sense of \cite[Section 19.3]{AndersonFulton}, where $N^-(\tau) = N^- \cap \tau N^- \tau^{-1}$.
\end{Corollary}

\begin{Theorem}[Graham Positivity {\cite[Corollary 2.4]{GX2025}}]
\label{th:GrahamPositivityRefined}
Let $w \in S_n$ and let $I(w) = \{\alpha \in \Delta^+ \mid w(\alpha) \in \Delta^-\}$ be the set of positive roots sent to negative roots by $w$. Then
\[
[X_w]_T = \sum_{v \leq w} c_{v,w} \cdot [\overline{B^- v B / B}]_T, \qquad c_{v,w} \in \mathbb{N}[-\alpha]_{\alpha \in I(w)}.
\]
\end{Theorem}

Applying \cref{th:GrahamPositivityRefined} to the normally transversal intersection $\tau X_u \cap X_v$ and using the projection formula, we obtain:

\begin{Proposition}[Intersection Coefficients]
\label{Prop:IntersectionCoefficients}
The intersection product expands as
\[
[\tau X_u \cap X_v]_T = \sum_{w \in S_n} c_{u,v}^w(\mathbf{y}, \mathbf{z}) \cdot [X_w]_T,
\]
where the coefficients $c_{u,v}^w(\mathbf{y}, \mathbf{z})$ are the structure constants of the double Schubert polynomial multiplication.
\end{Proposition}

By \cref{Cor:CompatiblyNSplit} and \cite[Corollary 2.4]{GX2025}, the coefficients $c_{u,v}^w$ lie in $\mathbb{N}[-\alpha]_{\alpha \in I(\tau)}$:

\begin{Corollary}[Coefficient Positivity]
\label{Cor:CoefficientPositivity}
The structure constants satisfy
\[
c_{u,v}^w(\mathbf{y}, \mathbf{z}) \in \mathbb{N}[-\alpha]_{\alpha \in I(\tau)}.
\]
\end{Corollary}

It remains to identify the set $I(\tau)$:

\begin{Lemma}[Root Set of the Special Involution]
\label{Lem:RootSetInvolution}
Since $\tau$ swaps the first $n$ indices with the last $n$ indices, the roots sent to negative roots are precisely
\[
I(\tau) = \{\, y_j - z_i \mid 1 \leq i, j \leq n \,\},
\]
where $y_1, \ldots, y_n$ are the weights of the first set of variables and $z_1, \ldots, z_n$ are the weights of the second set.
\end{Lemma}

\begin{Theorem}[Classical Double Schubert Positivity {\cite[Theorematical]{GX2025}}]
\label{th:ClassicalDoublePositivity}
For $u, v, w \in S_{\infty}$, the product of double Schubert polynomials satisfies:
\[
\mathfrak{S}_u(\mathbf{x}; \mathbf{y}) \cdot \mathfrak{S}_v(\mathbf{x}; \mathbf{z}) = \sum_{w \in S_n} c_{u,v}^w(\mathbf{y}; \mathbf{z}) \cdot \mathfrak{S}_w(\mathbf{x}; \mathbf{z})
\]
with coefficients $c_{u,v}^w(\mathbf{y}; \mathbf{z}) \in \mathbb{N}[y_i - z_j]_{i,j \geq 1}$.
\end{Theorem}

Combining \cref{Cor:CoefficientPositivity} with \cref{Lem:RootSetInvolution}, we obtain
\[
c_{u,v}^w(\mathbf{y}, \mathbf{z}) \in \mathbb{N}[y_j - z_i \mid 1 \leq i,j \leq n]_{i,j \geq 1},
\]
which proves \cref{th:ClassicalDoublePositivity}.

Finally, by the stability of Schubert polynomials \cite[Section 2.4]{Mihalcea}, the finite-$n$ statement extends to all $u, v, w \in S_\infty$ without modification.

\begin{Remark}[Connection to Open Conjecture]
\Cref{th:ClassicalDoublePositivity} establishes the case $q = 0$ of \cref{conj:QuantumDoublePositivity}. The full quantum double case — where coefficients lie in $\mathbb{N}[y_i - z_j, q_k]$ — remains open and is the subject of ongoing research.
\end{Remark}"""

if old in content:
    content = content.replace(old, new)
    with open('chapter5.tex', 'w') as f:
        f.write(content)
    print("SUCCESS: Replacement made")
else:
    print("ERROR: Old string not found")
    # Debug: show first 200 chars of what we're looking for
    print("Looking for:")
    print(repr(old[:200]))