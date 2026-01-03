---
description: Apply approved changes from a Lector report to the chapter file.
---
# Workflow: Lector Implement

> Applies PENDING changes from a Lector analysis report

## Prerequisites

- Lector report exists: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`

---

## Step 1: Load Report

Read the Lector report from `Story/LECTOR_LOGS/`

## Step 2: Filter Approved Changes

From the Change Log table, extract only rows where Status = `APPROVED`

## Step 3: Apply Changes

For each approved change:

| Action      | Implementation                                |
| ----------- | --------------------------------------------- |
| `REPLACE` | Find "Original" text, replace with "New" text |
| `DELETE`  | Remove the "Original" text entirely           |

## Step 4: Save Updated Chapter

Overwrite the chapter file with applied changes.

## Step 5: Archive Report

Move report from `Pending_Report_` to `Applied_Report_`:

- From: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`
- To: `Story/LECTOR_LOGS/Applied_Report_Chapter_XX.md`

## Step 6: Confirm

Report to user:

```
✅ Applied X changes to Chapter XX
   Deleted: Y lines
   Replaced: Z phrases
```

## Step 7: sync-content

use workflow /sync-from-chapter for the chapter to keep content updated

---

## Quick-Start

```
/lector-implement 1
```

---

**Version**: 2.0 (Webnovel Edition)
