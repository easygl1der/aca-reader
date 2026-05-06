#!/bin/bash
set -e

cd "$(dirname "$0")"

xelatex -synctex=1 -interaction=nonstopmode main.tex > /dev/null
xelatex -synctex=1 -interaction=nonstopmode main.tex > /dev/null
xelatex -synctex=1 -interaction=nonstopmode main.tex > /dev/null

echo "Compiled successfully"
