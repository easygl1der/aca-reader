#!/bin/bash
cd "/Users/yueyh/Projects/aca-workflow/notes/information-geometry/tang-rong"
xelatex -interaction=nonstopmode -synctex=1 \
    '\PassOptionsToPackage{quiet}{xeCJK}' \
    '\input{tang-rong-review.tex}' > /dev/null 2>&1
xelatex -interaction=nonstopmode -synctex=1 \
    '\PassOptionsToPackage{quiet}{xeCJK}' \
    '\input{tang-rong-review.tex}' > /dev/null 2>&1
xelatex -interaction=nonstopmode -synctex=1 \
    '\PassOptionsToPackage{quiet}{xeCJK}' \
    '\input{tang-rong-review.tex}' > /dev/null 2>&1
open -a Skim tang-rong-review.pdf
