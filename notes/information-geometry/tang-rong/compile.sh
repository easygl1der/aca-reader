#!/bin/bash
cd "/Users/yueyh/Projects/aca-workflow/notes/information-geometry/tang-rong"
FILE="tang-rong-review"
echo "=== Pass 1 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex > /dev/null 2>&1
echo "=== BibTeX ==="
bibtex ${FILE}.aux > /dev/null 2>&1
echo "=== Pass 2 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex > /dev/null 2>&1
echo "=== Pass 3 ==="
xelatex -interaction=nonstopmode -synctex=1 ${FILE}.tex > /dev/null 2>&1
echo "Done! $(ls -lh ${FILE}.pdf)"
open -a Skim ${FILE}.pdf
