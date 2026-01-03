---
description: Complete chapter pipeline - write, analyze, fix, sync (all-in-one)
---

// turbo-all

# Workflow: Chapter Pipeline

> **Full automation**: Write → Analyze → Implement → Sync
> Runs all four workflows in sequence with automatic command execution

---

## Prerequisites

- Chapter outline exists in `Story/Chapter-Outline/`
- `PROJECT.md` and `STYLE_GUIDE.md` exist
- Character profiles exist in `Characters/`

---

## PHASE 1: Write Chapter

**Execute**: `/write-chapter X`

1. Load context (PROJECT.md, STYLE_GUIDE.md, Plot_Outline.md)
2. Load chapter outline from `Story/Chapter-Outline/`
3. Write chapter (target: 1,700-1,900 words for 1,500-1,800 final)
4. Save to `Story/Chapters/Chapter_XX_[Name].md`
5. Verify word count

```powershell
powershell -Command "(Get-Content 'Story/Chapters/Chapter_XX_[Name].md' | Measure-Object -Word).Words"
```

**Continue only if**: Word count ≥ 1,500

---

## PHASE 2: Lector Analysis

**Execute**: `/lector-analyze X`

1. Load the written chapter
2. Score against 6 criteria:
   - Hook Quality
   - Pacing
   - Voice Consistency
   - Cliffhanger
   - Word Count
   - Competence Display
3. Generate report: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`

**Decision Point**:
- If PASS (all scores ≥ 7): Skip to Phase 4
- If REVISE: Continue to Phase 3
- If REWRITE: Return to Phase 1

---

## PHASE 3: Lector Implementation

**Execute**: `/lector-implement X`

1. Load pending report
2. Apply all APPROVED changes to chapter
3. Archive report as `Applied_Report_Chapter_XX.md`
4. Re-verify word count (must stay ≥ 1,500)

---

## PHASE 4: Sync Content

**Execute**: `/sync-from-chapter X`

1. Compare chapter to outlines (detect deviations)
2. Update `Characters/` files with:
   - Status changes
   - New items/equipment
   - Relationship developments
3. Update `World/` files if new lore introduced
4. Update `Chapter-Outline` if deviations occurred
5. Update `Plot_Outline.md` if needed
6. Create sync report: `Story/Sync_Reports/Sync_Chapter_XX.md`

---

## PHASE 5: Git Commit

```powershell
git add "Story/Chapters/Chapter_XX_[Name].md"
git add "Story/LECTOR_LOGS/"
git add "Story/Sync_Reports/"
git add "Characters/"
git add "World/"
git commit -m "Chapter XX: written, analyzed, synced"
git push origin main
```

---

## Output Summary

After pipeline completion, you will have:

| File | Location |
|------|----------|
| Written Chapter | `Story/Chapters/Chapter_XX_[Name].md` |
| Lector Report | `Story/LECTOR_LOGS/Applied_Report_Chapter_XX.md` |
| Sync Report | `Story/Sync_Reports/Sync_Chapter_XX.md` |
| Updated Characters | `Characters/*.md` |
| Updated World | `World/*.md` (if applicable) |

---

## Quick-Start

```
/chapter-pipeline 1
```

This runs the complete pipeline for Chapter 1.

---

## Batch Mode (Multiple Chapters)

```
/chapter-pipeline 1-5
```

Runs pipeline for Chapters 1 through 5 sequentially.

---

**Version:** 1.0
