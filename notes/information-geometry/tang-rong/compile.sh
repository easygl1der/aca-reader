#!/bin/bash
# Compile Tang & Yang review notes (standalone mode via wrapper)
# Wrapper provides full document environment so main file can always compile

FILE="tang-rong-review"
WRAPPER="${FILE}-compile.tex"

cat > "$WRAPPER" << 'OUTER_EOF'
\documentclass[12pt]{amsbook}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{xeCJK}
\setCJKmainfont{Source Han Serif SC VF}[BoldFont={Source Han Serif SC VF:Bold},AutoFakeBold=true]
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{natbib}
\bibliographystyle{plainnat}
\geometry{margin=1in}
\begin{document}
\def\STANDALONE{}
\bibliography{tang-rong}
\input{tang-rong-review.tex}
\end{document}
OUTER_EOF

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
