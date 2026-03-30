# PROOF-001: Logical Gap Detection

**Date**: 2026-03-30
**Type**: Proofreading Pattern
**Agent**: proof-reading

---

## Context

Mathematical proofs are particularly prone to logical gaps when:
- The proof relies on intuitive steps without explicit justification
- The author assumes background knowledge that readers may not share
- Complex algebraic manipulations skip intermediate steps
- Claims are made based on "obvious" but unstated assumptions

---

## Pattern: Common Logical Gap Types

### 1. Unjustified Steps
The proof jumps from one statement to the next without explaining **why** the transition is valid.

**Example**: "Since $f$ is continuous, $f(x_n) \to f(x)$" without referencing the definition of continuity.

### 2. Circular Reasoning
The proof assumes what it needs to prove, either explicitly or implicitly.

**Example**: Using the result being proved as an intermediate step.

### 3. Hidden Assumptions
Unstated conditions are used without verification.

**Example**: Assuming a function is differentiable when only continuity is given.

### 4. Unchecked Edge Cases
The proof covers the general case but ignores boundary conditions.

**Example**: Proving a property for $n \geq 1$ but not checking $n = 0$.

---

## Detection Method

1. **Trace each logical step**: Ask "Why does this follow from the previous step?"
2. **Identify assumptions**: List all assumptions at each transition point
3. **Check definitions**: Verify that prerequisite conditions are satisfied
4. **Test edge cases**: Verify the proof works for boundary values

---

## Example

**Claim**: If $f: \mathbb{R} \to \mathbb{R}$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.

**Gap**: Many proofs state this as "obvious" from the definition of differentiability without explicitly showing how the limit computation ensures continuity.

**Fix**: Show that $\lim_{h \to 0} f(x_0 + h) - f(x_0) = \lim_{h \to 0} h \cdot \frac{f(x_0 + h) - f(x_0)}{h} = 0$.

---

## Mitigation

- **Explicit transitions**: Add "Since..." or "Because..." phrases
- **Verify conditions**: State which definition/theorem justifies each step
- **State assumptions**: Make implicit assumptions explicit
- **Check boundaries**: Include explicit checks for edge cases

---

## Cross-Reference

- Stein writing style: `docs/stein-writing-style.md` — proofs should include full justification, not skip "obvious" steps
- Label/reference: `docs/label-reference.md` — use `\cref{}` to reference theorems being invoked

---

## Related Lessons

- PROOF-002: Notation Consistency
- PROOF-003: Scope and Quantifier Awareness