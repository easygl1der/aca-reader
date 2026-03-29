#!/bin/bash
# Check for undefined label/cite references after compile
# Trigger: PostToolUse on Bash(compile.sh)

INPUT=$(cat)
TOOL_SUCCESS=$(echo "$INPUT" | jq -r '.tool_response.success // true')

# Only check if compile succeeded
if [[ "$TOOL_SUCCESS" != "true" ]]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR" || exit 1

# Find which notes directory was compiled
NOTES_DIR=""
for dir in notes/*/compile.sh; do
  if [[ -f "$dir" ]]; then
    DIR_PATH=$(dirname "$dir")
    if git status --short "$DIR_PATH" 2>/dev/null | grep -q "\.tex"; then
      NOTES_DIR="$DIR_PATH"
      break
    fi
  fi
done

if [[ -z "$NOTES_DIR" ]]; then
  exit 0
fi

# Check .log file for undefined references
LOG_FILE="$NOTES_DIR"/*.log
if [[ ! -f "$LOG_FILE" ]]; then
  # Try glob pattern
  LOG_FILE=$(find "$NOTES_DIR" -maxdepth 1 -name "*.log" 2>/dev/null | head -1)
fi

if [[ -n "$LOG_FILE" && -f "$LOG_FILE" ]]; then
  # Extract undefined references
  UNDEFINED=$(grep -E "Reference.*undefined|Citation.*undefined" "$LOG_FILE" 2>/dev/null | head -10)
  if [[ -n "$UNDEFINED" ]]; then
    echo "⚠️ Undefined references found:"
    echo "$UNDEFINED" | sed 's/^/  /'
    echo ""
    echo "Run: cd $NOTES_DIR && grep -n '\\cref{' *.tex | grep -E '(eq:|thm:|lem:|def:|cor:)'"
  fi
fi

# Check for undefined cites (look for \cite without corresponding entry)
TEX_FILES=$(find "$NOTES_DIR" -maxdepth 1 -name "*.tex" 2>/dev/null)
if [[ -n "$TEX_FILES" ]]; then
  # Get all \cite{...} keys
  CITES=$(grep -hRo '\\cite{[^}]*}' "$TEX_FILES" 2>/dev/null | sed 's/\\cite{\([^}]*\)}/\1/g' | sort -u)

  # Get all bibliography keys from .bbl or \bibitem entries
  BBL_FILE=$(find "$NOTES_DIR" -maxdepth 1 -name "*.bbl" 2>/dev/null | head -1)
  if [[ -n "$BBL_FILE" && -f "$BBL_FILE" ]]; then
    BIB_KEYS=$(grep -hE '^\\bibitem\{' "$BBL_FILE" 2>/dev/null | sed 's/.*\\bibitem{\([^}]*\)}.*/\1/' | sort -u)
  else
    # Fallback: look in main tex file for bibliography
    MAIN_TEX=$(find "$NOTES_DIR" -maxdepth 1 -name "*-notes.tex" 2>/dev/null | head -1)
    if [[ -n "$MAIN_TEX" ]]; then
      BIB_KEYS=$(grep -hE '^\\bibitem\{' "$MAIN_TEX" 2>/dev/null | sed 's/.*\\bibitem{\([^}]*\)}.*/\1/' | sort -u)
    fi
  fi

  # Check each cite key exists
  MISSING=""
  for CITE in $CITES; do
    if [[ -n "$BIB_KEYS" ]]; then
      if ! echo "$BIB_KEYS" | grep -qF "$CITE"; then
        MISSING="$MISSING $CITE"
      fi
    fi
  done

  if [[ -n "$MISSING" ]]; then
    echo "⚠️ Missing bibliography entries:$MISSING"
  fi
fi

exit 0
