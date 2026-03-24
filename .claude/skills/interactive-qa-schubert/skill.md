# Interactive Q&A Skill for Schubert Calculus Notes

## Purpose
When the user asks a question about a paper they're reading (Schubert calculus), this skill:
1. Answers the question conversationally
2. Saves the Q&A to `appendix/qa.tex`
3. Updates the corresponding location in the main text if a formal definition is needed
4. Recompiles the PDF

## Workflow

### Step 1: Answer Conversationally
- Provide a clear, educational answer in Chinese (or the user's language)
- Use smooth language flow, avoid abrupt or choppy sentences
- Focus on the "why" and intuition before technical details
- Add `★ Insight` blocks for key takeaways

### Step 2: Save to qa.tex
- Location: `notes/<topic>/appendix/qa.tex`
- Format:
```latex
\section{Question Title}
\label{sec:LabelKey}

\subsection{问题}
[User's question]

\subsection{回答}
[Answer content]
```

### Step 3: Update Main Text (if needed)
- If the answer contains a formal definition that should be in the main text
- Add the definition to the appropriate section in `chapters/`
- Use smooth narrative that doesn't break the existing structure
- Avoid duplicating content already in the main text

### Step 4: Recompile
- Run `compile.sh` in the notes directory
- Report success/failure

## Symbol Convention
- Always use the paper's original notation
- If multiple papers have conflicting notation, ask the user which to use
- Record the chosen convention in notes

## Quality Guidelines
- Language should be smooth and educational, like Stein's writing style
- Focus on motivation and intuition
- Connect new concepts to existing knowledge
- Keep the structure intact - don't break existing sections
