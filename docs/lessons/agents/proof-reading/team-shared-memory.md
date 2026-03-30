# Proof-Reading Team: Shared Memory

**Shared Standards and Lessons for All Proof-Reading Agents**

**Last Updated**: 2026-03-30

---

## Proof-Reading Standards

### Critical Issue Types

| Issue Type | Description | Example |
|------------|-------------|---------|
| Logical Error | Invalid inference step | Assuming what needs to be proven |
| Mathematical Mistake | Incorrect calculation/algebra | Wrong sign in derivation |
| Unstated Assumption | Required premise not mentioned | Using continuity without stating |
| Type Error | Using wrong mathematical object | Treating set as element |
| Circular Reasoning | Conclusion used in premise | Proving A by assuming A |

### Major Issue Types

| Issue Type | Description | Example |
|------------|-------------|---------|
| Structure Problem | Improper proof architecture | Jumping between cases without transition |
| Technique Mismatch | Wrong proof technique for claim | Using induction on non-recursive statement |
| Insufficient Detail | Key step omitted | "Clearly..." when not clear |
| Overly Detailed | Unnecessary steps obscure main argument | Proving basic arithmetic |
| Premature Generalization | Concluding too much from partial result | Extending n=3 to all n |

### Minor Issue Types

| Issue Type | Description | Example |
|------------|-------------|---------|
| Notation Inconsistency | Symbol used for multiple meanings | $\epsilon$ for both error and epsilon-delta |
| Undefined Symbol | Symbol used without definition | Using $\delta$ without introducing |
| Formatting Issue | LaTeX syntax error | Missing brace in `\cref{}` |
| Style Deviation | Not following house style | Using `\bm` instead of `\mathbf` |

---

## Common Proof Patterns to Check

### 1. Direct Proof
```
✓ Check: Clear statement of assumption (Given)
✓ Check: Logical sequence of deductions
✓ Check: Explicit final conclusion (Goal met)
✗ Warning: Hidden assumptions often appear in "obviously"
```

### 2. Proof by Contradiction
```
✓ Check: Negation is correctly formed
✓ Check: Derivation leads to genuine contradiction
✓ Check: Contradiction is recognized explicitly
✗ Warning: Assuming the negation of what needs to be proven
```

### 3. Proof by Induction
```
✓ Check: Base case explicitly verified (n=0 or n=1)
✓ Check: Induction hypothesis clearly stated
✓ Check: Induction step uses hypothesis correctly
✓ Check: Conclusion follows from base + step
✗ Warning: Assuming P(k) for all k < n, not just P(n-1)
```

### 4. Existence Proof (Constructive)
```
✓ Check: Construction is explicit and well-defined
✓ Check: Verification that constructed object satisfies claim
✗ Warning: Proving "there exists" without actually constructing
```

### 5. Existence Proof (Non-Constructive)
```
✓ Check: Correct use of existence principle (e.g., Zorn's lemma)
✓ Check: Conditions of applied theorem are satisfied
✗ Warning: Using non-constructive method when constructive required
```

### 6. Uniqueness Proof
```
✓ Check: Existence proven separately
✓ Check: Assumption of two objects leads to equality
✗ Warning: Forgetting to prove uniqueness (only proving existence)
```

### 7. Equivalence Proof (iff)
```
✓ Check: Forward direction proved
✓ Check: Backward direction proved
✓ Check: Each direction uses appropriate technique
✗ Warning: Proving only one direction for "if and only if"
```

---

## Known Issues / Lessons from Past Sessions

### Lesson PR001: "Clearly" and "Obviously" Often Hide Problems

**Date**: 2026-03-30

**Issue**: Steps marked as "clearly" or "obviously" frequently contain non-obvious steps that are actually incorrect or unjustified.

**Correct Approach**:
```latex
% Wrong ❌
Since $a$ is clearly divisible by $b$, we have...

% Correct ✅
Since $a = kb$ for some integer $k$ (by definition of divisibility), we have...
```

**Prevention**: Flag all "clearly"/"obviously" instances for verification.

---

### Lesson PR002: Induction Hypothesis Scope Errors

**Date**: 2026-03-30

**Issue**: Induction step incorrectly assumes the statement for all values up to n, rather than just for n-1 → n.

**Correct Approach**:
```latex
% Wrong ❌
By induction hypothesis, $P(1), P(2), ..., P(k)$ all hold...

% Correct ✅
By induction hypothesis, we assume $P(k-1)$ holds. Now we prove $P(k)$...
```

**Prevention**: Explicitly state which specific instance the IH gives you.

---

### Lesson PR003: Negation Errors in Contradiction Proofs

**Date**: 2026-03-30

**Issue**: The negation of conditional statements is often incorrectly formed.

**Correct Approach**:
```latex
% Statement to negate: "If A, then B"
% Correct negation: "A and not B"

% Wrong ❌
Assume it is not the case that "if A then B"
→ This does NOT mean "A and not B" clearly

% Correct ✅
Assume A and not B, then derive contradiction
```

**Prevention**: When negating conditional statements, always write out the negation explicitly before proceeding.

---

### Lesson PR004: Epsilon-Delta Quantifier Order

**Date**: 2026-03-30

**Issue**: In $\epsilon$-$\delta$ proofs, the quantifier order $(\forall \epsilon > 0)(\exists \delta > 0)$ is often reversed or not explicitly stated.

**Correct Approach**:
```latex
% Wrong ❌
We can find a $\delta$ such that for all $\epsilon$...

% Correct ✅
Given $\epsilon > 0$, we can find $\delta > 0$ such that for all $x$...
```

**Prevention**: Always explicitly state the quantifier structure at the start of $\epsilon$-$\delta$ arguments.

---

### Lesson PR005: LaTeX Theorem Environment Syntax

**Date**: 2026-03-29

**Issue**: Generated LaTeX files sometimes have malformed theorem environments.

**Correct Approach**:
```latex
% Wrong ❌
\begin theorem}[...]
\end theorem}
\begin definition}[...]

% Correct ✅
\begin{theorem}[...]
...
\end{theorem}
\begin{definition}[...]
...
\end{definition}
```

**Prevention**: Use `grep -n "begin theorem\|end theorem\|begin definition\|end definition"` to check.

---

## Severity Classification Guide

### Critical (Must Fix)
- Logical errors that invalidate the proof
- Mathematical mistakes in calculations
- Assuming the conclusion (circular reasoning)
- Missing necessary conditions

### Major (Should Fix)
- Structural issues that make proof hard to follow
- Missing key justifications
- Incorrect proof technique for the claim type
- Unstated assumptions that affect validity

### Minor (Nice to Fix)
- Notation inconsistencies
- Formatting/style deviations
- Unnecessary verbosity
- "Clearly" steps that are actually correct but should be shown

---

## Reference to PUA Skill Paths

**⚠️ Note**: PUA (Protocol for Agent Behavior) skill path references:

- Primary skill: `skills/pua/SKILL.md`
- P7 mode references: `skills/pua/references/p7-protocol.md`

*If PUA skill is not yet configured in this project, agents should follow the general behavior protocols defined in `docs/team-lead-protocol.md`.*

---

## Issue Report Format

When reporting issues, use this structure:

```markdown
### Issue #[N]: [Brief Title]

**Severity**: Critical | Major | Minor
**Location**: Line X or Theorem X.Y
**Type**: Logical Error | Structure | Notation | Formatting

**Description**:
[What the issue is]

**Why It's a Problem**:
[Impact on proof validity or readability]

**Suggested Correction**:
```latex
[If applicable, show the corrected version]
```
```

---

## Collaboration Protocol

1. **Issue Triage**: proof-reader-lead assigns severity
2. **Investigation**: Specialists investigate assigned issue types
3. **Discussion**: All findings converge to proof-reader-lead
4. **Resolution**: proof-reader-lead drafts final assessment
5. **Validation**: latex-checker validates formatting corrections
6. **Delivery**: Consolidated report delivered to requester
