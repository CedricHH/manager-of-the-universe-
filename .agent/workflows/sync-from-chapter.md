---
description: Sync character, world, and outline files based on chapter content
---

// turbo-all

# Workflow: Sync From Chapter

> Updates Characters/, World/, Plot_Outline, and Chapter-Outline based on events in a written chapter

---

## Prerequisites

- Written chapter exists in `Story/Chapters/`
- Character profiles exist in `Characters/`
- `Story/Plot_Outline.md` exists
- `Story/Chapter-Outline/` exists

---

## When to Run

Run this workflow AFTER completing a chapter that contains:

- Character status changes
- New items/equipment acquired
- Injuries or physical changes
- Relationship developments
- Emotional revelations
- New world lore introduced
- New locations discovered
- **Deviations from Chapter-Outline**
- **Deviations from Plot_Outline**

---

## PHASE 1: Analyze Chapter

### Step 1.1: Read the Chapter

Load the completed chapter from `Story/Chapters/Chapter_XX_[Name].md`

### Step 1.2: Compare with Outlines

Load and compare against:
1. `Story/Chapter-Outline/Chapter_XX_[Name].md` - Did events match the outline?
2. `Story/Plot_Outline.md` - Does the chapter match the planned plot beats?

### Step 1.3: Identify ALL Changes

Extract changes in these categories:

| Category | Examples |
|----------|----------|
| **Status** | Level up, class change, new title |
| **Items** | New equipment, lost items, upgrades |
| **Injuries** | Wounds, scars, disabilities |
| **Relationships** | New allies, enemies, romantic developments |
| **Emotions** | Revelations, trauma, character growth |
| **Skills** | New abilities learned, skill improvements |
| **World** | New locations, lore, factions |
| **Plot Deviations** | Events that differ from outlines |

---

## PHASE 2: Update Character Files

### Step 2.1: Locate Character Profile

Find the relevant file in `Characters/`:
- `Characters/[Character_Name].md`

### Step 2.2: Add/Update Sections

For each change, update the appropriate section:

```markdown
## Current Status (as of Chapter XX)

| Attribute | Value |
|-----------|-------|
| Level | X |
| HP | X |
| Gold | X |
| Location | [Current Location] |

## Inventory

- [Item 1]
- [Item 2] ← NEW (Chapter XX)

## Injuries/Conditions

- [Injury] - acquired Chapter XX

## Relationships

| Character | Relationship | Status |
|-----------|--------------|--------|
| [Name] | [Type] | [Current State] |

## Recent Developments (Chapter XX)

- [What happened this chapter]
```

### Step 2.3: Add Chapter Reference

Always note WHICH chapter introduced the change:
> `← NEW (Chapter XX)` or `- acquired Chapter XX`

---

## PHASE 3: Update World Files (if needed)

### Step 3.1: Check for World Changes

If the chapter introduced:
- New locations → Update `World/` location files
- New lore → Update relevant world docs
- New factions/NPCs → Create or update files

### Step 3.2: Update World Files

Add new information with chapter reference.

---

## PHASE 4: Sync Outline Deviations (CRITICAL)

> If the written chapter deviated from the outline, the outlines MUST be updated!

### Step 4.1: Update Chapter-Outline

If the chapter differed from `Story/Chapter-Outline/Chapter_XX_[Name].md`:

1. Mark outline as `[WRITTEN]`
2. Add section documenting deviations:

```markdown
## Written vs Planned

| Planned | Actually Written |
|---------|------------------|
| [Original beat] | [What actually happened] |

**Reason for deviation**: [Why the change was made]
```

### Step 4.2: Update Plot_Outline.md

If the deviation affects the overall plot:

1. Update the chapter summary in `Story/Plot_Outline.md`
2. Check if subsequent chapters need adjustment
3. Add note: `[REVISED based on Chapter XX]`

### Step 4.3: Cascade Check

Ask yourself:
- Does this deviation affect later chapters?
- Do other outlines need updating?
- Are there now continuity issues?

If YES → Flag for user review

---

## PHASE 5: Log the Sync

### Step 5.1: Create Sync Report

Save to: `Story/Sync_Reports/Sync_Chapter_XX.md`

```markdown
# Sync Report: Chapter XX

**Date**: [Current Date]

## Character Updates

| Character | Change Type | Description | File Updated |
|-----------|-------------|-------------|--------------|
| [Name] | Inventory | Acquired [Item] | Characters/[Name].md |
| [Name] | Relationship | Allied with [X] | Characters/[Name].md |

## World Updates

| Element | Change | File Updated |
|---------|--------|--------------|
| [Location] | Discovered | World/[File].md |

## Outline Deviations

| Outline | Planned | Actual | Updated |
|---------|---------|--------|---------|
| Chapter-Outline | [X event] | [Y event] | ✓ |
| Plot_Outline | [Beat] | [New beat] | ✓ |

## Cascade Effects

- [ ] Later chapters affected: [List]
- [ ] Requires user review: YES/NO

## Summary

[Brief summary of all changes made]
```

---

## Quick-Start

```
/sync-from-chapter 5
```

This will:
1. Read Chapter 5
2. Compare against outlines for deviations
3. Identify all character/world changes
4. Update Characters/, World/, and Outlines
5. Create sync report

---

**Version:** 4.0 (With Outline Sync)
