#!/bin/bash
set -e

NAME="Causalinference"

# First pass: xelatex to generate aux files
echo "=== Pass 1/4: xelatex (generating aux files) ==="
xelatex -synctex=1 -interaction=nonstopmode "${NAME}.tex"

# Bibliography pass
echo "=== Pass 2/4: bibtex ==="
bibtex "${NAME}.aux" || true

# Second pass: resolve citations and references
echo "=== Pass 3/4: xelatex (resolving refs) ==="
xelatex -synctex=1 -interaction=nonstopmode "${NAME}.tex"

# Third pass: final resolution
echo "=== Pass 4/4: xelatex (final pass) ==="
xelatex -synctex=1 -interaction=nonstopmode "${NAME}.tex"

echo "=== Done: ${NAME}.pdf ==="
