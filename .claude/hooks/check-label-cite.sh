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

# Find all notes directories and check their logs
for NOTES_DIR in notes/*/; do
  if [[ ! -d "$NOTES_DIR" ]]; then
    continue
  fi

  LOG_FILE=$(find "$NOTES_DIR" -maxdepth 1 -name "*.log" -mmin -10 2>/dev/null | head -1)

  if [[ -z "$LOG_FILE" || ! -f "$LOG_FILE" ]]; then
    continue
  fi

  # Check for undefined references (LaTeX format: "LaTeX Warning: There were undefined references")
  UNDEF_REF=$(grep -i "undefined reference" "$LOG_FILE" 2>/dev/null | head -5)
  UNDEF_CITE=$(grep -i "undefined citation" "$LOG_FILE" 2>/dev/null | head -5)

  if [[ -n "$UNDEF_REF" ]]; then
    echo "⚠️ [$NOTES_DIR] Undefined references:"
    echo "$UNDEF_REF" | sed 's/^/  /'
    echo ""
  fi

  if [[ -n "$UNDEF_CITE" ]]; then
    echo "⚠️ [$NOTES_DIR] Undefined citations:"
    echo "$UNDEF_CITE" | sed 's/^/  /'
    echo ""
  fi
done

exit 0
