# Ding-Style Homework Template Notes

This note summarizes the local writing style to use when preparing homework
templates based on Peng Ding's *A First Course in Causal Inference*. Read this
file before editing `homework5_prep_template.tex`.

## Document Structure

- Use a book-like mathematical exposition rather than a worksheet layout.
- Keep the main sections sparse:
  - `Notation and Basic Results`
  - `Homework problems`
  - `Additional problems from Problem Set 5`
- Put each problem under `\paragraph{Problem title}\label{...}`.
- Use theorem-like environments for assumptions, definitions, theorems, remarks,
  and examples.
- Use labels in Ding's style, such as `problem::...`, `hw::...`,
  `thm::...`, `assume::...`, and `def::...`.

## Prose Style

- Prefer concise explanatory paragraphs.
- State the setting first, then define notation, then state the target result.
- Use transitional phrases like:
  - "We first recall the following notation."
  - "The relevant identification result is as follows."
  - "The following facts are useful for the proof."
  - "I leave the proof below."
- Use "Remark:" for short guidance, caveats, or proof hints.
- Avoid solution language. Do not write "Proof" unless the user asks for the
  solution. Use a placeholder environment instead.

## Mathematical Style

- Inline math should use `\(...\)`.
- Display math should use `\[ ... \]`.
- Define reusable notation near the beginning of the document.
- Use Ding-like macros:
  - `\pr`, `\var`, `\cov`, `\sumn`, `\tran`
  - `\at`, `\nt`, `\cp`, `\df`
  - `\ri{...}` for inline code and filenames
- State assumptions as numbered theorem environments, not as bullet lists when
  they are central to the problem.
- For long derivation hints, display the key identities and then add one short
  sentence explaining how they will be used.

## Problem Blocks

For each problem, follow this pattern:

```tex
\paragraph{Problem title}\label{...}

Problem statement.

Source: ...

We first recall ...

\begin{remark}
...
\end{remark}

\begin{mysolution}{label-or-number}
% Solution/proof to be written.
\end{mysolution}
```

Do not use card-like boxes or many Chinese UI-style labels such as "题面" and
"预备知识". The template should read like an extension of the textbook.

## Citations

- Use `natbib` commands: `\citet{...}` and `\citep{...}`.
- Keep bibliography at the end with:

```tex
\bibliographystyle{plainnat}
\bibliography{causal/causal}
```

## Scope

- Include the assigned exercise statement.
- Include necessary definitions, assumptions, theorem statements, formulas,
  references, and data descriptions.
- Do not solve the problem.
- Leave a `mysolution` placeholder for the user.
