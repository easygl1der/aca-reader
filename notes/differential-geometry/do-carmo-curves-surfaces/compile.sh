#!/bin/bash
# Compile script for do Carmo - Differential Geometry

FILE="do-carmo-curves-surfaces-notes"

# Compile 3 times for proper cross-references
for i in 1 2 3; do
    xelatex -interaction=nonstopmode -synctex=1 "$FILE.tex" > /dev/null 2>&1
done

# Open PDF in Skim
open -a Skim "$FILE.pdf"
