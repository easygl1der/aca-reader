# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This is an empty project directory. No code has been initialized yet.

## Getting Started

To start developing in this repository:

1. **Initialize a project** - Run the appropriate package manager init command for your chosen language/framework
2. **Add dependencies** - Install required packages
3. **Create source files** - Begin writing your application code

## Common Commands

Commands will depend on the chosen technology stack. After initializing a project, common commands include:

- **Install dependencies**: `npm install` / `pip install` / `go mod tidy`, etc.
- **Run development server**: `npm run dev` / `python main.py`, etc.
- **Build**: `npm run build` / `go build`, etc.
- **Test**: `npm test` / `pytest`, etc.
- **Lint**: `npm run lint` / `golangci-lint run`, etc.

## Next Steps

Once you have code in this repository, update this CLAUDE.md to reflect:
- The actual project structure and architecture

## LaTeX Label Format (IMPORTANT!)

**ALWAYS use this format:**
```latex
\label{name}
```

**NEVER use these formats (they are wrong!):**
- `\label_name}` - WRONG
- `\label{name}` - CORRECT
- `\label:name}` - WRONG

When creating labels:
- Theorem: `\label{name}`
- Lemma: `\label{name}`
- Definition: `\label{name}`
- Reference: `\cref{name}` (requires cleveref package)

**IMPORTANT: All references must use `\cref{}` format!** This includes:
- Sections: `\cref{sec:SectionName}`
- Subsections: `\cref{sec:SubsectionName}`
- Theorems: `\cref{def:TheoremName}`
- Lemmas: `\cref{def:LemmaName}`
- Definitions: `\cref{def:DefinitionName}`
- Conjectures: `\cref{conj:ConjectureName}`
- Equations: `\cref{eq:EquationName}`

Never write plain text like "see the theorem above" or "as shown in section 2". Always use `\cref{}` with proper labels.
- Specific commands for building, testing, and running
- Technology stack details
- Any project-specific conventions
