#!/bin/bash
# Compile Tang & Yang review notes (standalone mode via wrapper)

FILE="tang-rong-review"
WRAPPER="tang-rong-review-compile.tex"

# Create wrapper that defines \STANDALONE before inputting the real file
cat > "$WRAPPER" << 'EOF'
\def\STANDALONE{}
\input{tang-rong-review.tex}
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
