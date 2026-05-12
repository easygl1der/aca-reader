#!/bin/bash
# Compile LaTeX document (run three times for cross-references)
#
# xelatex: XeLaTeX compiler, supports Unicode
# -interaction=nonstopmode: continue on errors
# -synctex=1: enable SyncTeX for PDF-source sync

FILE="stochastic-processes-notes"

echo "=== First compilation ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== Second compilation ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== Third compilation ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex

echo "=== Done ==="
ls -la ${FILE}.pdf
