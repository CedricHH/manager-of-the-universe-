---
description: Run quality analysis on a chapter using generic Webnovel criteria
---
# Workflow: Lector Analyze

> Generic quality analysis for Webnovel chapters
> Applies universal Webnovel quality standards

---

## Prerequisites

- Chapter exists in `Story/Chapters/`
- `PROJECT.md` exists (for word count validation)
- `LECTOR_GUIDE.md` exists (for project-specific criteria, optional)

---

## Universal Webnovel Criteria

These apply to ANY Webnovel project:

### 1. Hook Quality (First 200 Words)

- Does the chapter grab attention immediately?
- Is there tension, action, or intrigue?

### 2. Pacing

- Are paragraphs mobile-optimized (1-3 sentences)?
- Is there action/progress every 200 words?
- No walls of text or info-dumps?

### 3. Protagonist Voice

- Is the voice consistent and distinctive?
- Would you recognize the character without the name?

### 4. Cliffhanger (Last 200 Words)

- Does the chapter end with a hook?
- Would readers click "Next Chapter" immediately?

### 5. Verify Word Count

// turbo

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```

Compare against word target from PROJECT.md.

### 6. Competence Display

- Does the protagonist DO something clever?
- Is there a "face-slapping" or win moment?

---

## Analysis Process

### Step 1: Load Chapter

Read from `Story/Chapters/Chapter_XX_[Name].md`

### Step 2: Score Each Criterion

Rate 1-10 for each of the 6 criteria

### Step 3: Generate Report

Save to: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`

```markdown
# Lector Analysis: Chapter XX

## Quick Score
| Criterion | Score |
|-----------|-------|
| Hook | X/10 |
| Pacing | X/10 |
| Voice | X/10 |
| Cliffhanger | X/10 |
| Word Count | X/10 |
| Competence | X/10 |

**Verdict**: PASS / REVISE / REWRITE

## Issues

| Line | Problem | Fix | Status |
|------|---------|-----|--------|
| ... | ... | ... | PENDING |

## Summary
[One sentence verdict]
```

### Step 4: User Review

Notify user to review. Changes remain PENDING.

---

## Quick-Start

```
/lector-analyze 1
```

---

**Version:** 3.0 (Generic)
