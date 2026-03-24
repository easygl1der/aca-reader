---
name: beamer-chinese-presentation
description: Use when creating academic presentations with LaTeX Beamer involving Chinese content, SYPSTLE-type documents, or CambridgeUS-themed slides
---

# Beamer Chinese Presentation

## Overview

LaTeX Beamer template for academic presentations with Chinese (xeCJK) support, CambridgeUS theme, and custom color blocks.

## Template

```latex
\documentclass[]{beamer}
\usetheme{CambridgeUS}
\usecolortheme{dolphin}
\usefonttheme{serif,professionalfonts}
\usefonttheme{structurebold}
\usepackage{tikz}
\usetikzlibrary{cd}
\usepackage{graphicx,pstricks,listings,stackengine}
\usepackage{xeCJK,amsfonts,amssymb,bm,amsthm,mathrsfs,latexsym,geometry,fancyhdr,mathtools}
\usepackage{ctex, hyperref}
\usepackage[T1]{fontenc}

% Custom colors
\definecolor{myblue}{rgb}{0.2, 0.5, 0.8}
\definecolor{mygreen}{rgb}{0.3, 0.7, 0.3}
\definecolor{myred}{rgb}{0.8, 0.2, 0.2}

% Block styles
\setbeamercolor{block title}{bg=myblue!80!black, fg=white}
\setbeamercolor{block body}{bg=myblue!10!white}
\setbeamercolor{alertblock title}{bg=myred!80!black, fg=white}
\setbeamercolor{alertblock body}{bg=myred!10!white}

\renewenvironment{alertblock}[1]{%
  \setbeamercolor{block title}{use=alertblock title,fg=alertblock title.fg,bg=alertblock title.bg}%
  \setbeamercolor{block body}{use=alertblock body,fg=alertblock body.fg,bg=alertblock body.bg}%
  \begin{block}{#1}}{\end{block}%
}

\setbeamercovered{transparent}
\setbeamertemplate{navigation symbols}{}

% Chinese fonts
\newcommand{\song}{\CJKfamily{song}}
\newcommand{\hei}{\CJKfamily{hei}}
\setCJKmainfont{Source Han Serif SC}[AutoFakeBold=true, AutoFakeSlant=true]
\setCJKmonofont{Source Han Sans CN}[AutoFakeBold=true, AutoFakeSlant=true]

% === SLIDE CONTENT BELOW ===
\begin{document}

\maketitle

\begin{frame}
    \tableofcontents
\end{frame}

\section{Section Name}

\begin{frame}
    \begin{block}{Block Title}content\end{block}
    \begin{alertblock}{Alert Title}important content\end{alertblock}
\end{frame}

\end{document}
```

## Quick Reference

| Element | Command |
|---------|---------|
| Title slide | `\maketitle` |
| TOC | `\tableofcontents` |
| Section | `\section{name}` |
| Frame | `\begin{frame}\end{frame}` |
| Block | `\begin{block}{title}content\end{block}` |
| Alert block | `\begin{alertblock}{title}content\end{alertblock}` |
| Columns | `\begin{columns}\begin{column}{.5\textwidth}...\end{column}\end{columns}` |
| Table | `\begin{table}\resizebox{\textwidth}{!}{\begin{tabular}...\end{tabular}}\end{table}` |
| Bold text | `\textbf{text}` |
| Italic/alert | `\alert{text}` |

## Common Mistakes

- **Missing `\end{document}`** - template won't compile
- **Chinese font not found** - ensure Source Han fonts installed or change `\setCJKmainfont`
- **Table overflow** - use `\resizebox{\textwidth}{!}{...}` wrapper
- **Alert block not defined** - ensure the `\renewenvironment{alertblock}` is before use

## Customization

Change theme: `\usetheme{Warsaw}` (替换 CambridgeUS)
Change colors: modify `myblue`, `mygreen`, `myred` RGB values
Change title font size: modify `\Large` in title definition
