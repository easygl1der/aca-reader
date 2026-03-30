# Trace Analysis Template

## Trace Info
**Task**: {brief description}
**Date**: {ISO date}
**Agents Involved**: {agent-1}, {agent-2}, ...

---

## Step-by-Step Trace

| Step # | Agent | Action | Logical Validity | Issues Found | Improvement Suggestion |
|--------|-------|--------|-------------------|--------------|------------------------|
| 1 | {agent-name} | {description of what was done} | ✅ Valid / ⚠️ Questionable / ❌ Invalid | {issue description or none} | {suggestion} |
| 2 | {agent-name} | {description} | ✅ Valid / ⚠️ Questionable / ❌ Invalid | {issue description or none} | {suggestion} |
| 3 | {agent-name} | {description} | ✅ Valid / ⚠️ Questionable / ❌ Invalid | {issue description or none} | {suggestion} |
| 4 | {agent-name} | {description} | ✅ Valid / ⚠️ Questionable / ❌ Invalid | {issue description or none} | {suggestion} |
| 5 | {agent-name} | {description} | ✅ Valid / ⚠️ Questionable / ❌ Invalid | {issue description or none} | {suggestion} |
| ... | ... | ... | ... | ... | ... |

---

## Detailed Issue Log

### Issue {N}: {Brief Title}
- **Step #**: {N}
- **Agent**: {who made the call}
- **Problem**: {detailed description}
- **Evidence**: {why this is an issue}
- **Suggested Fix**: {concrete recommendation}

---

## Pattern Identification

### Pattern 1: {Title}
**Description**: {what pattern was observed}
**Frequency**: {how often it occurred}
**Impact**: {how it affected the outcome}
**Mitigation**: {how to prevent in future}

### Pattern 2: {Title}
...

---

## Summary

### Statistics
- **Total Steps**: {N}
- **Valid Steps**: {N} ({%})
- **Questionable Steps**: {N} ({%})
- **Invalid Steps**: {N} ({%})

### Root Cause Analysis
{analysis of why issues occurred}

### Recommendations for Future Traces
1. **{Priority 1}**: {recommendation}
2. **{Priority 2}**: {recommendation}
3. **{Priority 3}**: {recommendation}

---

## Example Section

### Example: Trace Analysis

**Task**: Review Theorem 3.2.1 (Poisson Approximation to Binomial)
**Date**: 2026-03-29

| Step # | Agent | Action | Logical Validity | Issues Found | Improvement Suggestion |
|--------|-------|--------|-------------------|--------------|------------------------|
| 1 | causal-expert | Stated theorem: $\lim_{n\to\infty} \binom{n}{k}p_n^k(1-p_n)^{n-k} = e^{-\lambda}\lambda^k/k!$ | ✅ Valid | None | None |
| 2 | causal-expert | Set $np_n = \lambda$ | ✅ Valid | None | Clarify this is a scaling assumption |
| 3 | causal-expert | Expanded binomial coefficient $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | ✅ Valid | None | None |
| 4 | causal-expert | Took limit of $\frac{n(n-1)\cdots(n-k+1)}{n^k} \to 1$ | ✅ Valid | None | Add justification for fixed $k$ |
| 5 | gemini-expert | Claimed the limit equals $e^{-\lambda}\lambda^k/k!$ | ⚠️ Questionable | Missing intermediate step showing $(1-p_n)^n \to e^{-\lambda}$ | Add explicit step |
| 6 | gemini-expert | Concluded proof | ❌ Invalid | Gap at step 5 propagates | Fix step 5 before concluding |

### Pattern Identification

### Pattern 1: Unstated Limit Assumptions
**Description**: Multiple agents took limits without explicitly stating which variable is going to infinity
**Frequency**: 3 times in this trace
**Impact**: Caused one invalid step
**Mitigation**: Add a "Limit Assumption Checklist" as a pre-flight step

### Recommendations
1. **High**: Require explicit identification of limiting variable before starting proof
2. **Medium**: Add intermediate step for $(1-p_n)^n \to e^{-\lambda}$
3. **Low**: Consider using LaTeX macro for limit notation consistency
