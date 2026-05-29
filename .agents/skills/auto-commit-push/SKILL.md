---
name: auto-commit-push
description: Automatically git add, git commit, and git push all changes. For the aca-workflow project. Use when user says "帮我 commit 并 push", "commit and push", "自动提交", or after completing a task that requires saving progress.
argument-hint: "[commit message]"
---

# Auto Commit Push

Automatically stage, commit, and push all changes to the repository.

## Arguments

$ARGUMENTS contains the commit message. If empty, use a default message.

## Steps

### 1. Check git status

Use `Bash` to check for changes:
```bash
git status --short
```

If there are no changes, report "Nothing to commit" and stop.

### 2. Stage all changes

```bash
git add -A
```

### 3. Commit with message

```bash
git commit -m "$ARGUMENTS

Co-Authored-By: Codex Opus 4.6 <noreply@anthropic.com>"
```

If no message provided, use: "chore: auto-save progress"

### 4. Push to remote

```bash
git push origin main
```

### 5. Report result

Report the commit hash and what was pushed.

## Error Handling

If push fails:
- **Large file error**: Stop and report the error. DO NOT attempt git filter-repo or git lfs.
- **Network error**: Report and suggest retry.
- **Rejected (non-fast-forward)**: Report and suggest `git pull` first.

## Notes

- Always verify git status before adding
- Default branch is `main`
- Include Co-Authored-By header in all commits
- Check file sizes before commit to avoid large file issues
