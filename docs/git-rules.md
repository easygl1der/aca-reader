# Git 规范

## Git 提交习惯

**原则**: 每次更新了能跑通的内容就 commit

- **LaTeX 笔记**: 编译成功后就 commit
- **规范文档**: 更新了 docs/ 就 commit
- **commit 风格**: 简洁，说明改了啥

## Git Worktree 安全规则

**当遇到以下情况时，必须使用 git worktree 隔离操作**：
- 处理大文件（>50MB）
- 执行破坏性操作（如 `filter-repo`、`rebase`、`reset --hard`）
- 不确定操作是否安全
- 任何可能影响主分支的操作

**使用方法**：
```bash
# 创建隔离的 worktree
git worktree add ../workspace-backup -b backup-branch

# 在 worktree 中操作
cd ../workspace-backup
# 执行危险操作...

# 确认安全后，合并回主分支
git merge backup-branch

# 不安全则直接删除 worktree
git worktree remove ../workspace-backup
git worktree prune
```

## Git 大文件处理禁止规则

**禁止使用 git 处理大文件（>50MB）**，包括但不限于：

- ❌ `git filter-repo` 重写历史
- ❌ `git lfs track` / `git lfs install` / 任何 git lfs 命令
- ❌ `git add` 大文件后配合 commit
- ⚠️ **绝对禁止使用 git-lfs**

**原因（2026-03-19 血泪教训）**：

1. `git filter-repo --path A --path B` 是**白名单模式**，会删除 A、B 之外所有文件的 git 历史
2. `git lfs` 在 `git add` 后会**删除本地大文件**，只保留 134 bytes 的指针
3. 超过 100MB 的文件**无法 push 到 GitHub**（会被 pre-receive hook 拒绝）
4. push 失败后，如果执行了 `git add` + `git commit`，本地大文件已被 lfs 删除，无法恢复

**正确做法**：
- 超大 PDF（>50MB）**不要提交到 git**
- 单独备份到 Google Drive 或其他外部存储
- 或使用 GitHub LFS（需付费，免费额度仅 1GB）
- 如果必须处理，**先问用户**，获得明确同意后再操作
