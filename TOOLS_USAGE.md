# TOOL USAGE RULES

> **MANDATORY**: Always use the provided project tools for specific tasks. Do not invent your own PowerShell commands if a tool exists.

---

## Word Count

**ALWAYS** use the `count-words.bat` script to check word counts.

```powershell
.\Tools\count-words.bat "Path/To/File.md"
```

**Reason**: This script contains specific logic for excluding metadata, comments, and non-story text that raw `Measure-Object` misses.

---

## Git Operations

**ALWAYS** use the `git-commit.bat` script for commits.

```powershell
.\Tools\git-commit.bat
```

**Reason**: Handles specific project configuration and logging.

---

**Last Updated**: 2026-01-04
