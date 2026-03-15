#!/bin/bash
# Compile LaTeX notes three times for proper cross-references

FILE="differential-geometry-notes"

echo "Compiling $FILE.tex (3 passes)..."

for i in 1 2 3; do
    echo "Pass $i..."
    xelatex -interaction=nonstopmode "$FILE.tex" > /dev/null 2>&1
done

echo "Done! Output: $FILE.pdf"
open -a Skim "$FILE.pdf"
