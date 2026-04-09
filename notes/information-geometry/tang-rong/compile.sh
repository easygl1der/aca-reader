#!/bin/bash
# Compile Tang & Yang review notes

FILE="tang-rong-review"

echo "Compiling $FILE.tex (3 passes)..."

for i in 1 2 3; do
    echo "Pass $i..."
    xelatex -interaction=nonstopmode -synctex=1 "$FILE.tex" > /dev/null 2>&1
done

echo "Done! Output: $FILE.pdf"
open -a Skim "$FILE.pdf"
