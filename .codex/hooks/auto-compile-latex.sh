#!/bin/bash
# Auto-compile LaTeX after Edit tool modifies .tex files
# Data comes via stdin as JSON

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Check if it's a .tex file
if [[ "$FILE_PATH" != *.tex ]]; then
  exit 0
fi

# Find which notes directory this file belongs to
case "$FILE_PATH" in
  */notes/A-First-Course-in-Causal-Inference/*)
    NOTES_DIR="notes/A-First-Course-in-Causal-Inference"
    ;;
  */notes/Schubert-Polynomials/*)
    NOTES_DIR="notes/Schubert-Polynomials"
    ;;
  */notes/differential-geometry/*)
    NOTES_DIR="notes/differential-geometry"
    ;;
  */notes/bayesian/*)
    NOTES_DIR="notes/bayesian"
    ;;
  */notes/information-geometry/*)
    NOTES_DIR="notes/information-geometry"
    ;;
  */notes/mathematical-statistics/*)
    NOTES_DIR="notes/mathematical-statistics"
    ;;
  *)
    # Not in a known notes directory
    exit 0
    ;;
esac

PROJECT_DIR="$CLAUDE_PROJECT_DIR"
FULL_PATH="$PROJECT_DIR/$NOTES_DIR/compile.sh"

if [[ -f "$FULL_PATH" ]]; then
  echo "Auto-compiling $NOTES_DIR..."
  cd "$PROJECT_DIR/$NOTES_DIR" || exit 1
  bash compile.sh > /dev/null 2>&1
  if [[ $? -eq 0 ]]; then
    echo "Done: $NOTES_DIR compiled successfully"
  else
    echo "Warning: $NOTES_DIR compilation failed" >&2
  fi
fi

exit 0
