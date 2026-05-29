---
name: digital-garden-publisher
description: "Publish Markdown files to Digital Garden and update the homepage. Use this skill when the user asks to publish, upload, or deploy a note/markdown file to the Digital Garden website. Triggered by: 'publish to digital garden', '上传到 digital garden', '发布到数字花园', 'deploy to digital garden', '更新首页'."
---

This skill handles publishing Markdown files from Obsidian to Digital Garden hosted on GitHub Pages.

## When to Use This Skill

Use this skill when the user wants to:
- Publish a new Markdown note to the Digital Garden
- Update an existing published note
- Update the homepage with new links
- Deploy any content to https://easygl1der.github.io/digital-garden/

## Environment

**Key Paths:**
- Obsidian Vault: `/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring`
- Digital Garden Repo: `/tmp/digital-garden-test`
- GitHub Repo: `https://github.com/easygl1der/digital-garden`
- Published Site: `https://easygl1der.github.io/digital-garden/`

## Publishing Steps

### Step 1: Ensure the Markdown File Has Correct Frontmatter

The note MUST have this frontmatter at the top:

```yaml
---
dg-publish: true
title: 你的笔记标题
---
```

**For Homepage (index):**
```yaml
---
dg-publish: true
dg-home: true
tags: gardenEntry
title: 首页标题
---
```

### Step 2: Copy File to Digital Garden Repository

Copy from Obsidian Vault to the notes folder:

```bash
cp "/path/to/your/note.md" /tmp/digital-garden-test/src/site/notes/
```

**Note:** If the file is already in the Obsidian Vault, the source path would be like:
`/Users/yueyh/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/你的笔记.md`

### Step 3: Git Add, Commit, and Push

```bash
cd /tmp/digital-garden-test

# Add all changes
git add -A

# Commit with descriptive message
git commit -m "Add/Update: 你的笔记标题"

# Push to GitHub
git push
```

**If push fails** (remote has new changes):
```bash
git pull --rebase origin main && git push
```

### Step 4: Wait for Build

GitHub Actions will automatically build the site (1-2 minutes).

---

## Updating Homepage Links

When adding new content, update the homepage to link to it:

1. Edit `/tmp/digital-garden-test/src/site/notes/index.md`
2. Add a new row to the table:
   ```markdown
   | 03-11 | 新内容 | [查看](/digital-garden/你的笔记slug/) |
   ```
3. Commit and push

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Homepage shows "Nothing here" | Add `tags: gardenEntry` to the note's frontmatter |
| Note not published | Ensure `dg-publish: true` is in frontmatter |
| Build failed | Check GitHub Actions logs in the repo |
| Push rejected | Run `git pull --rebase origin main && git push` |

---

## Quick Reference Commands

```bash
# Enter repo
cd /tmp/digital-garden-test

# Check status
git status

# Commit and push
git add -A && git commit -m "描述" && git push

# If conflict
git pull --rebase origin main && git push
```

## Result

After successful push, the note will be available at:
- `https://easygl1der.github.io/digital-garden/你的笔记slug/`

The homepage will be at:
- `https://easygl1der.github.io/digital-garden/`
