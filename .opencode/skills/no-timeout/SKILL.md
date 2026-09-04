---
name: no-timeout
description: Use ALWAYS when invoking the bash tool. Never set the timeout parameter—always let the system default apply.
---

# Do Not Use Timeout

This skill prohibits the agent from ever setting the `timeout` parameter when using the bash tool.

## Rule

When calling the bash tool, **never** include the `timeout` parameter. Always omit it and let the system default timeout apply.

### Incorrect (DO NOT DO THIS)
```json
{
  "command": "npm run build",
  "timeout": 60000,
  "description": "Build the project"
}
```

### Correct (DO THIS)
```json
{
  "command": "npm run build",
  "description": "Build the project"
}
```

## Why

- The system default timeout is configured by the operator via `OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS` or the default 2-minute timeout
- The agent should never override the operator's timeout configuration
- If a command times out, the agent should inform the user and let them decide how to proceed

## Exceptions

- None. This rule applies to all bash tool invocations without exception.
