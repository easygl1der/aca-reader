#!/bin/bash
# Compile chapter0.tex standalone

FILE="chapter0"
WRAPPER="${FILE}-compile.tex"

cat > "$WRAPPER" << 'EOF'
\documentclass[12pt]{amsbook}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{xeCJK}
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{geometry}
\usepackage{natbib}
\bibliographystyle{plainnat}
\geometry{margin=1in}
\def\STANDALONE{}
\begin{document}
\bibliography{../tang-rong}
\makeatletter
\def\noteinfo#1{\begin{noteinfo}\itshape #1\end{noteinfo}}
\makeatother
\input{chapter0.tex}
\makeatletter
\renewenvironment{noteinfo}{\begin{tcolorbox}[colback=yellow!15,colframe=orange!50,boxrule=0.3pt,left=8pt,right=8pt,top=6pt,bottom=6pt]}{\end{tcolorbox}}
\makeatother
\end{document}
EOF

echo "Compiling $FILE.tex (3 passes, standalone)..."

for i in 1 2 3; do
    echo "Pass $i..."
    xelatex -interaction=nonstopmode -synctex=1 \
        '\PassOptionsToPackage{quiet}{xeCJK}' \
        '\input{'"$WRAPPER"'}' > /dev/null 2>&1
done

rm -f "$WRAPPER"
echo "Done! Output: $FILE.pdf"
open -a Skim "$FILE.pdf"
