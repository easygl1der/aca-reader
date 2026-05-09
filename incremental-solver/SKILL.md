---
name: incremental-solver
description: Solves exercises or problems in a file incrementally, adding solutions one by one. Use when the user wants to process a list of problems (in LaTeX, Markdown, etc.) and have the agent solve and insert the solutions immediately after each problem, turn by turn, to maintain high quality and context efficiency.
---

# Incremental Solver

This skill guides the agent through an incremental workflow for solving exercises or problems within a document. By processing one item at a time, the agent maintains focus, minimizes context usage, and allows for surgical edits.

## Workflow

1.  **Identify Target**: Locate the file and the section containing the exercises.
2.  **Determine Format**: Identify the syntax for exercises and solutions (e.g., LaTeX `\begin{exercise}`, Markdown `### Exercise`).
3.  **Find Unsolved Items**: Scan the file to identify exercises that do not yet have an accompanying solution block.
4.  **Process Incrementally**:
    *   **Read**: Retrieve the text of a single exercise.
    *   **Solve**: Generate a detailed, step-by-step solution.
    *   **Insert**: Use the `replace` tool to insert the solution immediately after the exercise block.
    *   **Verify**: Check that the insertion was successful and the document structure is preserved.
5.  **Repeat**: Move to the next unsolved item until the task is complete or the user interrupts.

## Best Practices

*   **Surgical Edits**: Use `replace` with enough context to ensure a unique match. Avoid overwriting other exercises.
*   **Context Efficiency**: Do not read the entire file at once if it's large. Read only the relevant exercise and a few lines of surrounding context.
*   **Incremental Feedback**: Update the user via `update_topic` at the start of each solve-insert cycle.
*   **Format Consistency**: Match the existing style, language, and mathematical notation of the document.

## Reference Patterns

For common exercise/solution block patterns, see [references/patterns.md](references/patterns.md).
