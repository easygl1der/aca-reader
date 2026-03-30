# Proof-Reading Team

**Team Purpose**: Proof-reading mathematical proofs in academic documents (LaTeX notes, papers, textbooks)

**Last Updated**: 2026-03-30

---

## Agent Roles

| Agent | Role | Key Responsibilities |
|-------|------|---------------------|
| `proof-reader-lead` | Team Lead | Coordinates workflow, routes proofs, ensures quality |
| `logic-reviewer` | Logic Specialist | Checks logical flow, validity of inferences, gap analysis |
| `notation-checker` | Notation Specialist | Verifies consistent notation, symbol definitions |
| `structure-analyst` | Structure Specialist | Analyzes proof structure, technique usage |
| `latex-checker` | LaTeX Specialist | Validates LaTeX syntax, formatting, cross-references |

---

## Hexagonal Collaboration Architecture

```
                    ┌─────────────────────┐
                    │   Intake & Routing   │
                    │  (proof-reader-lead) │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
     │    Logic    │  │   Notation  │  │  Structure  │
     │   Reviewer  │  │   Checker   │  │  Analyst    │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                    ┌─────────────────────┐
                    │ Convergence &       │
                    │ Discussion          │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │      Delivery       │
                    │   (latex-checker)   │
                    └─────────────────────┘
```

**Port Interfaces**:
- `intake-port`: Receives raw proof content for review
- `logic-port`: Handles logical structure analysis
- `notation-port`: Handles notation consistency checks
- `structure-port`: Handles proof technique analysis
- `output-port`: Delivers finalized proof assessment

---

## Workflow Phases

### Phase 1: Intake & Routing

1. Receive proof content (LaTeX snippet or full document)
2. Parse proof structure (theorem, lemma, proposition, corollary, etc.)
3. Identify key claims, assumptions, and conclusion
4. Route to appropriate specialists based on proof type:
   - **Direct proof** → Logic + Structure
   - **Proof by contradiction** → Logic + Structure
   - **Inductive proof** → Logic + Structure
   - **Combinatorial proof** → Logic + Structure
   - **Existence proof** → Logic + Existence technique check
   - **Formal derivation** → Notation + Logic

### Phase 2: Parallel Investigation

Specialists work independently and concurrently:

| Specialist | Investigation Focus |
|------------|-------------------|
| Logic Reviewer | Validity of each inference step, premises, conclusions, hidden assumptions |
| Notation Checker | Consistent use of symbols, defined terms, notation conflicts |
| Structure Analyst | Proof technique correctness, logical flow, structure gaps |

### Phase 3: Convergence & Discussion

1. Specialists report findings to proof-reader-lead
2. Consolidate issues by severity:
   - **Critical**: Logical errors, mathematical mistakes
   - **Major**: Structural issues, technique misuse
   - **Minor**: Notation inconsistencies, formatting issues
3. Resolve conflicting assessments through discussion
4. Draft consolidated feedback

### Phase 4: Delivery

1. Compile final assessment report
2. Categorize issues by type and severity
3. Provide specific line references for each issue
4. Suggest corrections where applicable
5. Deliver via `latex-checker` for format validation

---

## Directory Structure

```
proof-reading/
├── README.md                    # This file
├── team-shared-memory.md       # Shared standards and lessons
├── agents/                     # Agent-specific memory files
├── templates/                   # Proof templates and patterns
└── lessons/                    # Historical proof-reading lessons
```

---

## Quality Standards

1. **Accuracy First**: Mathematical correctness is non-negotiable
2. **Specificity**: Issue reports must include exact location and nature
3. **Constructive**: Provide actionable correction suggestions
4. **Explanatory**: Explain why something is an issue
5. **Balanced**: Acknowledge correct aspects, not just problems

---

## Reference Materials

- LaTeX Style Guide: `docs/latex-style.md`
- Stein Writing Style: `docs/stein-writing-style.md`
- Label Reference: `docs/label-reference.md`
- PUA Skill (for behavior protocols): `skills/pua/SKILL.md` *(if available)*
