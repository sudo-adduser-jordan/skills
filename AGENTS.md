# User Generated

## Tools
- never use sleep

## Ask

- Always use the ask feature when presenting options, choices, or decisions to the user.
- Never present options as plain text, markdown lists, or chat output when the ask tool is available.

## Comments

- No comments in source code.
- Do not create comments in the codebase.
- Documentation lives in the project's markdown files.

## Logging

Reference: https://loggingsucks.com/

- Default log paths under `./logs/`:
  - `./logs/test`
  - `./logs/errors`
- Use JSONL for log files.
- Pretty print logs.
- Color logs, keys, values, and value types.

## Task Automation

Reference: https://taskfile.dev/docs/reference/schema

- Do not use external scripts.
- Use default command set:
  - `install`
  - `update`
  - `remove`
  - `setup`
  - `migrate`
  - `start`
  - `stop`
  - `dev`

- add colored logging
- [command] content

## Commits

- never write descriptions
- use user defined commit message format
- `tag: statement of change`
```sh
add: 
update: 
remove: 
move: 
feature:
fix:
```
- if a tag does not exist in the above list, suggest one

# End User Generated
