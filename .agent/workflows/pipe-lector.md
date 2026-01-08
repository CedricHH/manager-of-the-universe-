---
description: Combined quality loop - analyze, implement fixes, and sync content
---
# Workflow: Pipe Lector

> Unifies the quality assurance process for a chapter.
> Combines Analysis, Implementation, and Synchronization.

---

## Prerequisites

- Chapter exists in `Story/Chapters/`
- `PROJECT.md` and `LECTOR_GUIDE.md` exist

---

## // turbo-all

// turbo-all

## PHASE 1: Analyze

### Step 1.1: Run Analysis

Use the `/lector-analyze` workflow for the target chapter.

- Source: `Story/Chapters/Chapter_XX.md`
- Output: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`

## PHASE 2: Implement & Sync

### Step 2.1: Apply Approved Changes

Use the `/lector-implement` workflow to process the pending report.

- Source: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`
- Action: Applies `APPROVED` changes to the chapter file.

### Step 2.2: Character & World Sync - Important!

Use the `/sync-from-chapter-report` workflow to update EACH character profiles and world logs based on the revised chapter content every time!

- Updates: `Characters/`, `World/`, `Story/Plot_Outline.md`

---

## Quick-Start

```
/pipe-lector 1
```

## Batch Mode

```
/pipe-lector 1-5
```

---

**Version:** 2.0 (Unified Pipeline)
