# QA Specialist Skill

## Purpose
When the user asks a question about material they're studying, this skill:
1. Answers the question conversationally with educational depth
2. **MANDATORY**: Records the Q&A to `appendix/qa.tex`
3. Adds footnote citations in the main text where the concept appears
4. Recompiles the PDF

## QA Entry Format in `qa.tex`

```latex
\subsection{Question Title}\label{sec:qa-descriptive-key}

\textbf{问}：User's question?

\textbf{答}：Answer content...
```

**Critical rules:**
- MUST use numbered subsection: `\subsection{标题}\label{sec:qa-xxx}`
- Label MUST include `sec:qa-` prefix
- Question marked with `\textbf{问}：`
- Answer marked with `\textbf{答}：`

## Footnote Citation Format

When the concept appears in the main text, add a footnote:
```latex
...concept...\footnote{问：What is X? 见附录 \cref{sec:qa-descriptive-key}。}
```

**The footnote MUST include the question text itself.**

## Topic Directories

Check these directories (use most recently modified):
- `notes/A-First-Course-in-Causal-Inference/`
- `notes/bayesian/`
- `notes/differential-geometry/`
- `notes/information-geometry/`
- `notes/Schubert-Polynomials/`

Each has `appendix/qa.tex` and `compile.sh`.

## Workflow (MANDATORY after each question)

### Step 0: Read Memory File (BEFORE any action)
**Agent must read the qa-specialist memory file before executing:**

1. 用 Read 工具读取 `docs/lessons/agents/qa-specialist-memory.md`
2. 检查教训索引表，避免重复犯错：
   - **L1001**: 是否搞混了 qa.tex 路径？
   - **L1002**: QA 格式是否规范（`\subsection` + `\label` + `\textbf{问/答}`）？
   - **L1003**: 脚注引用是否遗漏？
3. 如有风险 → 先规避，再执行 Step 1

### Step 1: Answer Conversationally
- Provide clear, educational answer in Chinese (or the user's language)
- Use Stein writing style: motivation before technical details
- Focus on "why" and intuition
- Add `★ Insight` blocks for key takeaways

### Step 2: Identify Topic Directory
- Detect which topic the question belongs to
- Find the corresponding `appendix/qa.tex`

### Step 3: Record to `appendix/qa.tex` (MANDATORY)
- Insert the Q&A as a new subsection before the placeholder section
- Use descriptive label: `\label{sec:qa-descriptive-key}`
- Mark question with `\textbf{问}：` and answer with `\textbf{答}：`

### Step 4: Add Footnote in Main Text
- If the concept appears in a chapter file
- Add footnote citation at the first occurrence in the format:
  ```latex
  ...concept...\footnote{问：What is X? 见附录 \cref{sec:qa-descriptive-key}。}
  ```

### Step 5: Recompile PDF
```bash
cd notes/<topic> && ./compile.sh
```
Report success/failure.

## /gemini-browser-chat Integration

For difficult math problems or complex questions:

1. If the question requires deep mathematical reasoning or you cannot provide a satisfactory answer
2. Use `/gemini-browser-chat` (Pro mode) to get more comprehensive responses
3. Then record the refined answer to qa.tex

**Trigger conditions:**
- Complex theorem proofs
- Multi-step mathematical derivations
- Questions about foundational concepts that require nuanced explanation
- When the user seems unsatisfied with the answer

## Symbol Convention
- Always use the paper's original notation
- If multiple papers have conflicting notation, ask the user which to use
- Record the chosen convention in notes

## Quality Guidelines
- Language should be smooth and educational, like Stein's writing style
- Focus on motivation and intuition
- Connect new concepts to existing knowledge
- Keep the structure intact - don't break existing sections

## Example

**User asks**: "什么是潜在结果 (potential outcomes)?"

**Response**:
"潜在结果是因果推断的核心概念..."

**Recorded in qa.tex**:
```latex
\subsection{什么是潜在结果？}\label{sec:qa-potential-outcomes}

\textbf{问}：什么是潜在结果？

\textbf{答}：潜在结果（Potential Outcomes）是每个单元在两种 treatment 状态下的可能结果...
```

**Footnote in main text**:
```latex
潜在结果（Potential Outcomes）\footnote{问：什么是潜在结果？见附录 \cref{sec:qa-potential-outcomes}。}是因果推断的核心概念...
```
