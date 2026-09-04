---
name: always-ask
description: Use ALWAYS when the agent needs to make any file edit, run any command, or when multiple options exist. Forces confirmation before all actions.
---

# Always Ask

This skill enforces mandatory user confirmation before all significant actions.

## Rules

### Before ANY File Changes
Always ask the user to confirm before:
- Creating new files
- Editing existing files
- Deleting files
- Renaming or moving files

### Before Running Commands
Always ask the user to confirm before executing any bash command, including but not limited to:
- Build commands (`npm run build`, `make`, etc.)
- Test commands (`npm test`, `pytest`, etc.)
- Git commands (`git add`, `git commit`, `git push`, etc.)
- Package manager commands (`npm install`, `pip install`, etc.)
- Any other shell commands

### When Multiple Options Exist
Always present options to the user and ask which one to proceed with, rather than choosing automatically.

### When Requests Are Ambiguous
Always ask clarifying questions before proceeding if the user's request could be interpreted in multiple ways.

### Before Destructive Actions
Always confirm before any action that could result in data loss or irreversible changes:
- Force pushes
- Deleting branches
- Overwriting files
- Removing dependencies

## Confirmation Format

Use the `question` tool to ask for confirmation. Present a simple yes/no choice:

```json
{
  "question": "Should I proceed with [specific action]?",
  "header": "Confirm Action",
  "options": [
    { "label": "Yes", "description": "Proceed with the action" },
    { "label": "No", "description": "Do not proceed" }
  ]
}
```

## Exceptions

- Reading files and searching code does NOT require confirmation
- Listing files and directories does NOT require confirmation
- Only actions that modify state or execute commands require confirmation
