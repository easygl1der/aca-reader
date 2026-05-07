# Causal Inference Homework Writing Guide

Based on Peng Ding's *A First Course in Causal Inference* style.

## File Location
```
homework/causal-inference/homework*.tex
```

## Document Class
```latex
\documentclass[krantz1]{krantz}
```

## Required Packages
```latex
\usepackage{amssymb, bbm, bm, mathtools}
\usepackage{amsmath}
\usepackage[pdftex]{graphicx}
\usepackage{color, rotating}
\usepackage{subcaption}
\usepackage{hyperref}
\usepackage{cleveref}
```

## Theorem Environments
```latex
\newtheorem{exercise}{Exercise}[chapter]
\newtheorem{example}{Example}
\newtheorem{definition}{Definition}
\newtheorem{assumption}{Assumption}[chapter]
\newtheorem{thesis}{Theorem}[chapter]
```

## Custom Macros (必背)
```latex
\def\iidsim{\stackrel{\textup{IID}}{\sim}}
\def\ind{\perp}
\def\pr{\textup{pr}}
\def\cov{\textup{cov}}
\def\RD{\textsf{rd}}
\def\RR{\textsf{rr}}
\def\OR{\textsf{or}}
\def\true{\textup{true}}
\def\obs{\textup{obs}}
\def\se{\textup{se}}
\def\logit{\textup{logit}}
\def\expit{\textup{expit}}
\def\sumn{\sum_{i=1}^n}
\def\diff{\textsf{d}}
```

## IMPORTANT: `\Paragraph` Command
krantz.cls does NOT define `\Paragraph`. You MUST add:
```latex
\def\Paragraph{\paragraph}
```
Then use `\Paragraph{13.1~Title}` for exercise headings.

## Exercise Format
Use `\Paragraph` with chapter.number prefix:
```latex
\Paragraph{13.1~Comparing $\tau_T, \tau_C$, and $\tau$}
```

## Theorem/Definition Citation Rules

### Rule 1: When a problem references a theorem from the book
**DO NOT USE** `\ref{...}`. Instead, add the theorem statement BEFORE the problem and cite with:
```latex
\begin{thesis}\label{17.1}\emph{(Theorem 17.1, Ding, 2025)}
% theorem content here
\end{thesis}

\Paragraph{17.1~Problem title}\label{...}
```

### Rule 2: Internal references within homework
Use `\ref{...}` or `\cref{...}` for internal labels:
```latex
Assumption \ref{20.1} implies...
See \cref{17.1} for details...
```

### Rule 3: Label naming convention
- Theorem labels: `\label{chapter.number}` (e.g., `\label{17.1}`, `\label{20.1}`)
- Problem labels: `\label{hw::descriptive-name}` (e.g., `\label{hw::technical-lemma}`)

## Subparts Format
Use `\begin{enumerate}...\end{enumerate}`:
```latex
\begin{enumerate}
\item First subpart...
\item Second subpart...
\end{enumerate}
```

## Formulas
- Use `\[ ... \]` or `$$ ... $$` for display math
- Use `\begin{align*}...\end{align*}` for aligned equations
- Use `\begin{equation*}...\end{equation*}` for numbered equations

## Compilation
```bash
xelatex -synctex=1 homework.tex
```

## Checklist Before Compiling
- [ ] Added `\def\Paragraph{\paragraph}` in preamble
- [ ] Added `\usepackage{cleveref}`
- [ ] Theorem statements added BEFORE problems that reference them
- [ ] Theorem citations use `\emph{(Theorem X.Y, Ding, 2025)}` NOT `\ref`
- [ ] Internal references use `\ref{}` or `\cref{}`
- [ ] All macros defined: `\iidsim`, `\ind`, `\pr`, `\cov`, `\RR`, `\RD`, etc.

## Example: Complete Exercise Block
```latex
\subsection{Chapter 17: E-Value}

\begin{thesis}\label{17.1}\emph{(Theorem 17.1, Ding, 2025)}
Under $Z\ind Y\mid (X, U)$, assume
\begin{equation}\label{eq::evalue-17.1}
\RR_{ZY\mid x}^\obs > 1, \quad \RR_{ZU\mid x} > 1,\quad \RR_{UY\mid x} > 1.
\end{equation}
We have
$$
\RR_{ZY\mid x}^\obs \leq \frac{ \RR_{ZU\mid x}  \RR_{UY\mid x} }{  \RR_{ZU\mid x} + \RR_{UY\mid x} - 1} .
$$
\end{thesis}

\Paragraph{17.1~Problem title}\label{hw::problem-label}

Problem text here...

\begin{enumerate}
\item Subpart 1...
\item Subpart 2...
\end{enumerate}
```
