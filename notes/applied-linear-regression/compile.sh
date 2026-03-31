#!/bin/bash
# Applied Linear Regression Notes - Compile Script
# Must use xelatex 3 times for proper cross-references

cd "$(dirname "$0")"

echo "Compiling applied-linear-regression-notes.tex..."
xelatex -interaction=nonstopmode applied-linear-regression-notes.tex
xelatex -interaction=nonstopmode applied-linear-regression-notes.tex
xelatex -interaction=nonstopmode applied-linear-regression-notes.tex

echo "Done! Output: applied-linear-regression-notes.pdf"
