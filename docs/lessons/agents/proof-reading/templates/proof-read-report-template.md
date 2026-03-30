# Proof-Reading Report Template

## Proof ID
`PROOF-{YYYY}-{SEQ}`

**Date**: {ISO date}
**Reviewer**: {agent-name}
**Status**: ⏳ Pending / ✅ Verified / ❌ Flawed

---

## Original Claim

> {Copy the exact claim, theorem, or statement being reviewed}

**Source**: {file-path:line-number or reference}

---

## Analysis

### Logic Flow
```
Step 1: {description}
  └─> Assumption: {what is assumed}
  └─> Implication: {what follows}

Step 2: {description}
  └─> ...
```

### Assumptions Identified
- [ ] {assumption 1}
- [ ] {assumption 2}

### Dependencies
- {dependency 1} (line XX)
- {dependency 2} (line XX)

---

## Issues Found

### Issue 1: {Brief Title}
- **Type**: ☐ Logical Gap / ☐ Mathematical Error / ☐ Unstated Assumption / ☐ Notation Issue / ☐ Other
- **Severity**: 🔴 Critical / 🟠 Major / 🟡 Minor / ⚪ Cosmetic
- **Location**: {file}:{line}
- **Description**: {what is wrong}
- **Impact**: {how this affects the overall proof}

### Issue 2: {Brief Title}
- **Type**: ...
- **Severity**: ...
- ...

---

## Recommendations

1. **{Priority 1}**: {action needed}
2. **{Priority 2}**: {action needed}

---

## Confidence Level

- **Overall**: {High / Medium / Low}
- **Reasoning**: {brief explanation}

---

## Example Section

### Example: Sample Proof Review

**Original Claim**:
> If $X$ is a random variable with $\mathbb{E}[X] = \mu$ and $\text{Var}(X) = \sigma^2$, then $\mathbb{E}[X^2] = \mu^2 + \sigma^2$.

**Analysis**:
```
Step 1: Definition of variance
  └─> Assumption: Var(X) = E[(X - E[X])^2]
  └─> Implication: σ² = E[(X - μ)²]

Step 2: Expand the square
  └─> (X - μ)² = X² - 2μX + μ²
  └─> E[X² - 2μX + μ²] = E[X²] - 2μE[X] + μ²
  └─> = E[X²] - 2μ² + μ² = E[X²] - μ²

Step 3: Solve for E[X²]
  └─> σ² = E[X²] - μ²
  └─> E[X²] = μ² + σ² ✓
```

**Issues Found**: None

**Confidence Level**: High
