#!/bin/bash
# Auto-commit script for aca-workflow notes
# Usage: ./scripts/commit_notes.sh "commit message"

cd "$(dirname "$0")/.." || exit 1

MSG="${1:-$(date '+%Y-%m-%d %H:%M:%S') update}"

# Add notes and progress files
git add notes/ \
       .claude/skills/reading-progress/progress.json \
       .claude/skills/reading-progress/progress.md \
       2>/dev/null

# Commit with message
git commit -m "$MSG"

echo "Committed: $MSG"
