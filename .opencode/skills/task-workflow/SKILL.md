---
name: task-workflow
description: Use when starting any coding task, feature implementation, or bug fix. Automatically creates a git branch, generates a todos.md tracker, implements changes, and stages them.
---

# Task Workflow

When the user asks to implement a feature, fix a bug, or complete any coding task, follow this workflow in order.

## 1. Create a Branch

Derive a lowercase, hyphen-separated branch name from the task:

- Features: `feature/<short-description>`
- Bugs: `fix/<short-description>`
- Refactors: `refactor/<short-description>`
- Other: `task/<short-description>`

Run:
```bash
git checkout -b <branch-name>
```

If the branch already exists, append `-2`, `-3`, etc.

## 2. Create todos.md

Create a `todos.md` file at the project root listing every concrete subtask required to complete the user's request. Use this format:

```markdown
# Task: <short title>

- [ ] Subtask 1
- [ ] Subtask 2
- [ ] Subtask 3
```

Keep items specific and actionable. One checkbox per discrete unit of work.

## 3. Implement the Changes

Work through each item in `todos.md`:

- Mark a task as in-progress (mentally or via todowrite)
- Make the code changes for that task
- Mark it complete in `todos.md` when done
- Move to the next task

Do not skip ahead. Complete tasks in order.

## 4. Stage the Changes

After all tasks are complete, stage every changed and new file:
```bash
git add -A
```

Do not commit. The user will commit when ready. Leave `todos.md` in the repo.
