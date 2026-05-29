#!/bin/bash
# Auto-commit and push after Edit or Bash (compile.sh)
# Skips if: no changes, git conflicts, or large files in notes/

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_SUCCESS=$(echo "$INPUT" | jq -r '.tool_response.success // true')

# Only proceed if tool succeeded
if [[ "$TOOL_SUCCESS" != "true" && "$TOOL_SUCCESS" != "null" ]]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR" || exit 1

# Check if there are actual changes (only tracked files matter)
CHANGES=$(git status --short -- '*.tex' '*.md' '*.json' '*.sh' 'docs/' 'notes/')
if [[ -z "$CHANGES" ]]; then
  echo "No changes to commit"
  exit 0
fi

# Check for large files (>50MB) in notes/ and docs/ only - skip if found
LARGE_FILES=$(find notes/ docs/ -type f -size +50M 2>/dev/null | head -5)
if [[ -n "$LARGE_FILES" ]]; then
  echo "Skipping: large files in notes/:"
  echo "$LARGE_FILES"
  exit 0
fi

# Stage all changes (only what we care about)
git add -A -- '*.tex' '*.md' '*.json' '*.sh' 'docs/' 'notes/' '.claude/settings.json'

# Get a descriptive commit message
if [[ "$TOOL_NAME" == "Edit" ]]; then
  FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // "unknown"')
  BASENAME=$(basename "$FILE" .tex)
  COMMIT_MSG="chore: update $BASENAME"
elif [[ "$TOOL_NAME" == "Bash" ]]; then
  COMMIT_MSG="chore: compile and save"
else
  COMMIT_MSG="chore: auto-save"
fi

git commit -m "$COMMIT_MSG

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Try to push
if git push origin main 2>&1; then
  HASH=$(git rev-parse --short HEAD)
  echo "✓ Auto-pushed: $HASH"
else
  echo "⚠ Auto-push failed (check git status)" >&2
fi

exit 0
