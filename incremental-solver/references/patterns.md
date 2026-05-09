# Exercise/Solution Patterns

Use these patterns to identify where to insert solutions in various document formats.

## LaTeX (Standard)

**Exercise Block:**
```latex
\begin{exercise}{ID — Label}
Problem text here...
\end{exercise}
```

**Insertion Point:** Immediately after `\end{exercise}`.

**Solution Block:**
```latex
\begin{solution}
\textbf{解答}：
Solution text here...
\end{solution}
```

## Markdown

**Exercise Block:**
```markdown
### Exercise 1.1
Problem text here...
```

**Insertion Point:** Before the next header or at the end of the section.

**Solution Block:**
```markdown
**Solution**:
Step-by-step reasoning...
```

## Custom Environments

Always check for custom LaTeX environments defined in the preamble or `GEMINI.md`. Common ones include:
- `\begin{problem}` / `\end{problem}`
- `\begin{exer}` / `\end{exer}`
- `\begin{sol}` / `\end{sol}`
