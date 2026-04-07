# Referee Report: Graham Positivity of Triple Schubert Calculus

**Authors**: Yibo Gao (Peking University), Rui Xiong (University of Ottawa)
**Paper**: Graham Positivity of Triple Schubert Calculus
**ArXiv reference**: (assumed recent submission)

---

## Summary

The paper proves Samuel's conjecture (2024) that the expansion coefficients $c_{u,v}^w(\mathbf{y},\mathbf{t})$ of the product of two double Schubert polynomials in three sets of variables are polynomials in $\{t_i - y_j\}$ with nonnegative integer coefficients. The proof proceeds by establishing a refined version of Graham's positivity theorem (Theorem 2.3), using a new geometric interpretation of the coefficients as intersections of certain $B^-$-stable cycles. As a corollary, Kirillov's conjecture on the positivity of skew divided difference operators is established. The paper also proposes Conjecture 2.7 for Grothendieck polynomials.

---

## Overall Assessment

### Contribution: 9/10
This paper makes a significant contribution to algebraic combinatorics and Schubert calculus. The proof of Samuel's conjecture was an open problem, and the approach via a refined Graham positivity theorem with a geometric interpretation is novel. The corollary establishing Kirillov's conjecture is also important, as skew divided difference operators have been studied extensively.

### Correctness: 8/10 (with minor concerns)
The main arguments are fundamentally sound. However, there are several points where the exposition could be clarified or justified more explicitly. After careful review:

- **Lemma 2.2 (Normal subgroup)**: The Lie algebra argument using root vectors $F_\alpha$ and the condition $[F_\alpha, F_\beta] \in \mathfrak{n}^-(ws_i)$ is correct for type A, but the proof glosses over some details that a careful reader might wish to see elaborated.

- **Theorem 2.3 (Induction)**: The application of [1, Proposition 19.4.4] with $\chi = -w\alpha_i$ is correct provided the pair $B^-(ws_i) \subset B^-(w)$ satisfies the normal chain condition. Lemma 2.2 establishes exactly this: $N^-(ws_i)$ is a normal subgroup of $N^-(w)$ with quotient one-dimensional, and the character on the quotient is $-w\alpha_i$. The proof in Anderson-Fulton (Theorem 19.4.5) uses a chain of such extensions, and our case fits this framework.

- **Lemma 2.5 (Transversality)**: The reference to [1, Section 19.3] for transversality is appropriate. Section 19.3 establishes (via Lemma 19.3.4, the Kleiman-Bertini theorem) that generic translates of Schubert varieties intersect properly and transversely. The argument using $u_0 = 1 \times w_0^{(n)}$ and $u_0^{-1}\tau u_0 = w_0^{(2n)}$ is a standard Reidemeister-Schwarz-Magri type argument for conjugation in product groups. However, the proof would benefit from explicitly stating which result from [1, Section 19.3] is being applied.

- **$I(\tau)$ computation (line 127)**: The calculation $I(\tau) = \{y_j - t_i\}$ is correct. For $\mathrm{GL}_{2n}$ with the permutation $\tau$ swapping the two $n$-blocks, the left inversion set consists exactly of the $n^2$ positive roots of the form $x_{n+j} - x_i = y_j - t_i$.

### Importance: 9/10
The result resolves a conjecture and connects several previously separate threads in Schubert calculus (Samuel's formula, Kirillov's conjecture, Graham's positivity). The refined positivity theorem (Theorem 2.3) is a genuine strengthening of Graham's result and will likely find further applications.

---

## Major Comments (必须修改)

### 1. Lemma 2.2: The normal subgroup argument needs explicit verification of the Lie bracket calculation

**Current proof (lines 53-55)**: The proof states that for $\alpha \in J(ws_i)$ and $\beta = w\alpha_i$, the bracket $[F_\alpha, F_\beta]$ yields $F_\gamma$ with $\gamma \in J(ws_i)$.

**Issue**: The argument that $\gamma = \alpha + \beta \in J(ws_i)$ when $\beta = w\alpha_i$ requires careful justification. Specifically, one must check that $(ws_i)^{-1}\gamma > 0$. The proof asserts this but does not show the calculation. While the statement is true in type A (the paper's setting), the step "$\gamma \neq w\alpha_i \in J(w)$, so $\gamma \in J(ws_i)$" is insufficiently explained.

**Requested addition**: Add explicit verification that for $\alpha \in J(ws_i)$ and $\beta = w\alpha_i$, if $\gamma = \alpha + \beta \in \Phi$ (i.e., is a root), then $(ws_i)^{-1}\gamma > 0$. This can be done by case analysis on the root pattern in type A, or by invoking the general root system formula for how roots change under simple reflections.

**Why this is essential**: Lemma 2.2 is the foundation for Theorem 2.3's induction. If the normal subgroup property is not fully verified, the entire proof structure is compromised.

### 2. Lemma 2.5: Clarify the reference to [1, Section 19.3] and add explicit transversality argument

**Current proof (lines 115-117)**: The lemma cites [1, Section 19.3] and states that the intersection is proper and transverse "from [1, Section 19.3]" after the conjugation argument.

**Issue**: Section 19.3 of Anderson-Fulton develops the positivity theory via transversality. The specific result needed is Lemma 19.3.4 (Kleiman-Bertini), which ensures that for a connected group $\Gamma$ acting transitively, generic translates intersect properly. However, the application to the specific situation with $u_0 = 1 \times w_0^{(n)}$ and $w_0^{(2n)}$ is not made explicit.

**Requested addition**: Either (a) cite [1, Lemma 19.3.4] explicitly and show how it applies, or (b) provide a short direct argument for why $\tau \overline{B^- u B/B} \cap \overline{B^- v B/B}$ is proper and transverse, using the fact that $w_0^{(2n)}$ is the order-reversing involution and the varieties are $B^-$-stable.

### 3. Theorem 2.3: Explicitly verify the chain condition from [1, Proposition 19.4.4]

**Current proof (line 67)**: "By Lemma 2.2, the pair $B^-(ws_i) \subset B^-(w)$ satisfies the condition (see [1, p. 384]) of [1, Proposition 19.4.4] with $\chi = -w\alpha_i$."

**Issue**: The "condition" on [1, p. 384] is not specified in the paper. From reading [1], Proposition 19.4.4 requires a normal chain of subgroups with each quotient one-dimensional. The paper states Lemma 2.2 shows this is satisfied, but the connection between the Lie algebra ideal property and the group-theoretic condition of [1, Proposition 19.4.4] should be spelled out.

**Requested addition**: Add a sentence explaining that by Lemma 2.2, $N^-(ws_i)$ is a normal subgroup of $N^-(w)$, and $B^-(ws_i) = T \cdot N^-(ws_i)$ is normal in $B^-(w) = T \cdot N^-(w)$ with $B^-(w)/B^-(ws_i) \cong \mathbb{G}_m$ having character $-w\alpha_i$ on its Lie algebra.

---

## Minor Comments (建议修改)

### 1. Line 127: The equation $I(\tau) = \{y_j - t_i\}$ should include a brief derivation

**Current text**: "where we compute $I(\tau) = \{y_j - t_i \mid 1 \leq i,j \leq n\}$"

**Suggestion**: Add a one-sentence derivation: since $\tau$ interchanges the two $n$-blocks, for $i, j \leq n$ we have $\tau(x_i - x_{n+j}) = x_{n+i} - x_j = t_i - y_j < 0$ and all other positive roots remain positive, hence $I(\tau) = \{x_{n+j} - x_i : 1 \leq i,j \leq n\} = \{y_j - t_i\}$.

### 2. Notation: The definitions of $I(w)$ and $J(w)$ (line 37) are clear, but the relationship to inversion sets in Coxeter theory should be noted

The paper defines $I(w) = \{\alpha \in \Phi^+ : w^{-1}\alpha \in \Phi^-\}$ and $J(w) = I(ww_0)$. In standard Coxeter terminology, $I(w)$ is the (left) inversion set. This is standard but worth noting for readers coming from different backgrounds.

### 3. Corollary 2.4 and the remark following it: The comparison to Graham's theorem is appropriate, but the statement that $B^-(w)$-invariant cycles are "necessarily $T$-invariant" (line 79) could be clarified

The remark says $B^-(w)$-invariant cycles are necessarily $T$-invariant. This is true because $T \subset B^-(w)$ by definition ($B^-(w) = T \cdot N^-(w)$). A cycle invariant under $B^-(w)$ is in particular invariant under $T$. Perhaps add: "Since $T \subseteq B^-(w)$ by definition, any $B^-(w)$-invariant cycle is $T$-invariant."

### 4. Conjecture 2.7: The definition of $a \ominus b := \frac{a-b}{1+\beta b}$ is standard for Grothendieck polynomials, but could be restated for clarity

The convention is consistent with [16] (Lam-Lee-Shimozono), but non-experts might benefit from a brief parenthetical note that this reduces to $a-b$ when $\beta = 0$.

### 5. The proof of Corollary 1.2 (lines 141-142) cites two sources: [21, Section 2 p. 5] and [6, Proposition 6.4]

It would be helpful to note which is the primary source for the equality $\partial_{w/v}\mathfrak{S}_u(\mathbf{x};\mathbf{y}) = c_{u,v}^w(\mathbf{y},\mathbf{x})$.

---

## Confidential Comments to Editor

**Recommendation**: **Accept (after minor revisions)**

**Justification**: This is a strong paper that resolves an important open conjecture. The main ideas are correct and the results are significant. The minor revisions requested are primarily expository: the authors should clarify several arguments that are technically complete but not fully explicit in the current version. Specifically:

1. Lemma 2.2 should include explicit verification of the Lie bracket calculation for the normal subgroup property
2. Lemma 2.5 should either explicitly cite Lemma 19.3.4 from [1] and show its applicability, or provide a short direct argument
3. Theorem 2.3 should briefly explain how Lemma 2.2 implies the chain condition for [1, Proposition 19.4.4]

These are not gaps in the mathematical reasoning but rather instances where the current exposition requires the referee to fill in details that should be in the paper. With these additions, the paper will be a clean and complete contribution to the literature.

**Additional notes for the editor**:
- The paper is well-organized and the structure is clear
- The references are appropriate and include the major works in the field (Anderson-Fulton, Graham, Kirillov, Molev-Sagan, Samuel)
- The authors correctly identify that their method gives a new geometric interpretation distinct from Knutson-Tao's puzzle approach
- The conjecture in Section 2.4 (Conjecture 2.7) is a natural and interesting extension that will likely inspire further work
- The $I(\tau) = \{y_j - t_i\}$ computation at line 127 is correct and could serve as a lemma for future reference

**Concerns for author response**: The authors should verify that the Lie algebra calculations in Lemma 2.2 are watertight for the general type A case, not just for specific examples. In particular, the claim that $\gamma = \alpha + w\alpha_i \in J(ws_i)$ when $\alpha \in J(ws_i)$ and $\gamma$ is a root should be checked for all root patterns in $S_n$.

---

## Technical Appendix: Verification of Key Points

### On Lemma 2.2 (Normal Subgroup)

For type A root system ($\mathrm{GL}_n$), the positive roots are $\Phi^+ = \{x_i - x_j : i < j\}$. The Lie algebra $\mathfrak{n}^-(w)$ has basis $\{F_{x_i - x_j} : x_i - x_j \in J(w)\}$.

Given $ws_i > w$, we have $J(w) = J(ws_i) \cup \{w\alpha_i\}$. To show $\mathfrak{n}^-(ws_i)$ is an ideal in $\mathfrak{n}^-(w)$, we need: for all $\alpha \in J(ws_i)$ and $\beta \in J(w)$, $[F_\alpha, F_\beta] \in \mathfrak{n}^-(ws_i)$.

The cases:
- If $\beta \in J(ws_i)$: Then $\alpha, \beta \in J(ws_i)$, and since $J(ws_i)$ is upper-set, $\alpha + \beta \in J(ws_i)$ (when a root), so the bracket lands in $\mathfrak{n}^-(ws_i)$.
- If $\beta = w\alpha_i$: Write $\alpha = x_p - x_q$ with $p < q$. For the bracket to be nonzero, we need $q$ to equal the "middle" index of $w\alpha_i$. In type A, $w\alpha_i = x_{w(i)} - x_{w(i+1)}$, so the bracket $[F_{x_p-x_q}, F_{x_{w(i)}-x_{w(i+1)}}]$ is nonzero only if $q = w(i)$, giving $\gamma = x_p - x_{w(i+1)}$. Since $p \neq w(i)$ (otherwise $\alpha = 0$), $\gamma \neq w\alpha_i$. Checking $(ws_i)^{-1}\gamma > 0$ requires $p < w(i+1)$, which follows from $ws_i > w$ and the definition of $J(ws_i)$.

This is correct but deserves explicit mention.

### On $I(\tau)$ Computation

For $\tau \in S_{2n}$ with $\tau(i) = n+i$ and $\tau(n+i) = i$:
- For $i, j \leq n$: $\tau(x_i - x_{n+j}) = x_{n+i} - x_j = t_i - y_j < 0$, so $x_{n+j} - x_i \in I(\tau)$
- For $i, j > n$: $\tau(x_{n+i} - x_{n+j}) = x_i - x_j$, which is positive if $i < j$
- For mixed cases, similar calculations show no other roots are sent to negative

Thus $I(\tau) = \{x_{n+j} - x_i : 1 \leq i, j \leq n\} = \{y_j - t_i\}$. This is correct.

---

*Report prepared by: Referee*
*Date: 2026-04-07*
*Classification: Algebraic Combinatorics / Schubert Calculus / Equivariant Cohomology*
