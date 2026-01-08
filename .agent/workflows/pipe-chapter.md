---
description: Complete chapter pipeline with continuity check and sync (all-in-one)
---
// turbo-all

# Workflow: Full Chapter Pipeline

> **Complete automation**: Continuity Check → Outline → Write → Analyze → Implement → Sync
> All workflows combined into one seamless production pipeline

---

## Prerequisites

- `PROJECT.md` and `STYLE_GUIDE.md` exist
- `Story/Plot_Outline.md` exists
- Character profiles exist in `Characters/`
- `LECTOR_GUIDE.md` exists (optional)

---

# PHASE 0: PLOT CONTINUITY CHECK

> **MANDATORY for new arcs (Chapter 101, 201, 301...) or new antagonists**
> Prevents repeating conquered guilds, reusing antagonist names, or duplicating conflict types

## Step 0.1: Determine If Check Needed

- Starting new arc (Chapter X01)? → **RUN FULL CHECK**
- Introducing major new antagonist? → **RUN FULL CHECK**
- Planning guild/faction conflict? → **RUN FULL CHECK**
- Regular chapter in same arc? → **SKIP to Phase 1**

## Step 0.2: Load Arc Summary

// turbo

```powershell
rg "conquered|acquired|defeated|under.*control" "Story/Plot_Outline.md" --context 1
```

## Step 0.3: Check Conquered Guilds

Review Plot_Outline.md and create/update this checklist:

| Guild/Faction    | Status       | Arc Conquered    |
| ---------------- | ------------ | ---------------- |
| Alchemist Guild  | ✅ Conquered | Arc 1 (Ch 78-79) |
| Mercenary Guild  | ✅ Conquered | Arc 1 (Ch 79)    |
| Church of Light  | ⚠️ Truce   | Arc 1 (Ch 71-75) |
| Merchant Guild   | ❌ Available | -                |
| Adventurer Guild | ❓ Check     | -                |

**If target guild is ✅ Conquered → STOP and choose different guild**

## Step 0.4: Search Character Names

// turbo

```powershell
Get-ChildItem "Characters/*.md" | Select-Object Name | Sort-Object Name
```

Before creating new antagonist, verify:

- [ ] Name doesn't exist in Characters/
- [ ] Name doesn't sound similar to existing characters (e.g., Groll/Kroll/Grall)
- [ ] Title (Guildmaster, Guild Master) doesn't duplicate

**If name conflict found → STOP and choose different name**

## Step 0.5: Conflict Type Diversity

Verify conflict type differs from previous arcs:

| Arc   | Conflict Type Used                              |
| ----- | ----------------------------------------------- |
| Arc 1 | Economic warfare (Bank, Guild debt acquisition) |
| Arc 1 | Regulatory capture (Church audit)               |
| Arc 1 | Political intrigue (Sterling family)            |

**Arc 2+ MUST use different type:**

- Trade licensing / Market access
- Territorial expansion
- Consortium politics
- Magical research conflict

**If identical conflict type → MODIFY approach**

## Step 0.6: Document Decision (for new arcs)

Add to arc planning:

```markdown
## Arc [X] Differentiation

- **Arc [X-1] Main Conflict**: [Type]
- **Arc [X] Main Conflict**: [NEW Type]
- **New Antagonist**: [Name] (verified unique)
- **New Guild/Faction**: [Name] (verified not conquered)
- **Continuity Check Date**: [DATE]
```

---

# PHASE 1: CHECK FOR OUTLINE

## Step 1.1: Locate Chapter Outline

Check if outline exists in `Story/Chapter-Outline/Chapter_XX_[Name].md`

## Step 1.2: Create Outline if Missing

If no outline exists, create one:

### 1.2.1: Load Context

1. Read `./PROJECT.md` for word count target and format
2. Read `./Story/Plot_Outline.md` for chapter overview
3. Read relevant character profiles from `./Characters/`
4. Read relevant world files from `./World/`

### 1.2.2: Run Continuity Checks

// turbo

```powershell
rg "[GUILD_NAME]" "Story/Plot_Outline.md" --context 2
```

// turbo

```powershell
Get-ChildItem "Characters/" | Where-Object { $_.Name -match "[ANTAGONIST_NAME]" }
```

**If guild was conquered or name exists → STOP and choose different**

### 1.2.3: Create Beat-Sheet

```markdown
# Outline: Chapter XX - [Title]

**Word Target**: [from PROJECT.md]

## Continuity Verification
- [x] Guild/faction NOT previously conquered
- [x] Antagonist name is unique
- [x] Conflict type differs from previous arcs

## Hook
[How chapter starts - 250-350 words]

## Development
### Beat 1: [Setup]
### Beat 2: [Complication]
### Beat 3: [Escalation]

## Cliffhanger
[How chapter ends - 250-350 words]

## Checklist
- [ ] Protagonist demonstrates competence
- [ ] Genre-specific elements present
- [ ] Cliffhanger creates urgency
```

### 1.2.4: Save Outline

Save to: `Story/Chapter-Outline/Chapter_XX_[Name].md`

**Continue only if**: Outline exists and approved

---

# PHASE 2: WRITE CHAPTER

## Step 2.1: Load Project Context

1. Read `./PROJECT.md` for word count target, language, file locations
2. Read `./STYLE_GUIDE.md` for tone, voice, POV, banned phrases
3. Read `./Story/Plot_Outline.md` for overall story arc
4. Read chapter outline from `Story/Chapter-Outline/`
5. Read relevant character profiles from `Characters/`
6. Check previous chapter for continuity

## Step 2.2: Word Count Calibration

> **CRITICAL**: ARMI system messages create "visual length" but fewer actual words

| PROJECT.md Target | Actual Writing Target       | Reason                                               |
| ----------------- | --------------------------- | ---------------------------------------------------- |
| 1,500-1,800 words | **1,700-1,900 words** | System messages count as ~50% fewer words than prose |

**Word Count Distribution** (for 1,700 target):

- Hook: 250-350 words
- Development: 1,100-1,300 words
- Cliffhanger: 250-350 words

**Prose Density Rules**:

- Every chapter needs at least 4-5 paragraphs of 4+ sentences each
- Expand character thoughts and environmental descriptions

## Step 2.3: Write with Structure

Follow STYLE_GUIDE.md structure:

1. **Hook** → Start with tension/action (250-350 words)
2. **Development** → Main content (1,100-1,300 words)
3. **Cliffhanger** → End with hook for next chapter (250-350 words)

## Step 2.4: Apply Style Rules

- Follow POV rules from STYLE_GUIDE
- Use system message format from STYLE_GUIDE
- Avoid banned phrases from STYLE_GUIDE

## Step 2.5: Quality Check Before Saving

Run through the checklist in STYLE_GUIDE.md

## Step 2.6: Save & Verify

Save to: `Story/Chapters/Chapter_XX_[Name].md`

// turbo

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```

**If < 1,500 words:**

1. Identify 2-3 sections to expand
2. Add ~50-75 words per section
3. Re-verify until target met

---

# PHASE 3: LECTOR ANALYSIS

## Step 3.1: Load Chapter

Read from `Story/Chapters/Chapter_XX_[Name].md`

## Step 3.2: Score Universal Webnovel Criteria

Rate 1-10 for each:

| Criterion              | Check                                         |
| ---------------------- | --------------------------------------------- |
| **Hook Quality** | First 200 words grab attention?               |
| **Pacing**       | Paragraphs mobile-optimized (1-3 sentences)?  |
| **Voice**        | Consistent and distinctive protagonist voice? |
| **Cliffhanger**  | Last 200 words create urgency?                |
| **Word Count**   | Meets PROJECT.md target?                      |
| **Competence**   | Protagonist demonstrates skill?               |

// turbo

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```

## Step 3.3: Generate Report

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
| ... | ... | ... | APPROVED |

## Summary
[One sentence verdict]
```

---

# PHASE 4: LECTOR IMPLEMENTATION

## Step 4.1: Load Report

Read from `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`

## Step 4.2: Filter & Apply Changes

For Status = `APPROVED`:

| Action      | Implementation                                |
| ----------- | --------------------------------------------- |
| `REPLACE` | Find "Original" text, replace with "New" text |
| `DELETE`  | Remove the "Original" text entirely           |

## Step 4.3: Save Updated Chapter

Overwrite the chapter file with applied changes.

## Step 4.4: Archive Report

Move report:

- From: `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`
- To: `Story/LECTOR_LOGS/Applied_Report_Chapter_XX.md`

## Step 4.5: Confirm Changes

```
✅ Applied X changes to Chapter XX
   Deleted: Y lines
   Replaced: Z phrases
```

---

# PHASE 5: SYNC FROM CHAPTER (MANDATORY)

> Updates Characters/, World/, Plot_Outline, and Chapter-Outline based on chapter events

## Step 5.1: Analyze Chapter

Load the completed chapter and compare against:

1. `Story/Chapter-Outline/Chapter_XX_[Name].md` - Did events match outline?
2. `Story/Plot_Outline.md` - Does chapter match planned plot beats?

## Step 5.2: Identify ALL Changes

Extract changes in these categories:

| Category                  | Examples                                   |
| ------------------------- | ------------------------------------------ |
| **Status**          | Level up, class change, new title          |
| **Items**           | New equipment, lost items, upgrades        |
| **Injuries**        | Wounds, scars, disabilities                |
| **Relationships**   | New allies, enemies, romantic developments |
| **Emotions**        | Revelations, trauma, character growth      |
| **Skills**          | New abilities learned, skill improvements  |
| **World**           | New locations, lore, factions              |
| **Plot Deviations** | Events that differ from outlines           |

## Step 5.3: Update Character Files

For each character change, update `Characters/[Character_Name].md`:

```markdown
## Current Status (as of Chapter XX)

| Attribute | Value |
|-----------|-------|
| Level | X |
| Location | [Current Location] |

## Inventory
- [Item] ← NEW (Chapter XX)

## Recent Developments (Chapter XX)
- [What happened this chapter]
```

### Consolidation Rule (CRITICAL)

1. **Limit**: Keep only last **3-5 chapters** in "Recent Developments"
2. **Archive**: Move older events into "History" section
3. **Summarize**: Combine multiple bullets into narrative sentence

## Step 5.4: Update World Files (if needed)

If chapter introduced:

- New locations → Update `World/` location files
- New lore → Update relevant world docs
- New factions/NPCs → Create or update files

## Step 5.5: Sync Outline Deviations (CRITICAL)

If chapter differed from outlines:

1. Mark Chapter-Outline as `[WRITTEN]`
2. Add deviation documentation:

```markdown
## Written vs Planned

| Planned | Actually Written |
|---------|------------------|
| [Original beat] | [What actually happened] |

**Reason for deviation**: [Why the change was made]
```

3. Update Plot_Outline.md if deviation affects overall plot
4. Add note: `[REVISED based on Chapter XX]`

## Step 5.6: Cascade Check

Ask yourself:

- Does this deviation affect later chapters?
- Do other outlines need updating?
- Are there now continuity issues?

**If YES → Flag for user review**

---

# PHASE 6: TOKEN USAGE FEEDBACK

Report token usage for the pipeline:

```
📊 TOKEN USAGE REPORT
─────────────────────
Context-Tokens used: [number]
Free-Tokens: [number]
Output-Tokens of last file: [number]
Utilization: [percentage]%

Efficiency Notes:
[Brief analysis and suggestions]
```

**If approaching 70% context → Recommend new chat**

---

# PHASE 7: GIT COMMIT

If context window usage is high or pipeline complete:

// turbo

```powershell
.\Tools\git-commit.bat "feat: Complete Chapter XX pipeline"
```

---

## Output Summary

After pipeline completion, you will have:

| File                 | Location                                           |
| -------------------- | -------------------------------------------------- |
| Chapter Outline      | `Story/Chapter-Outline/Chapter_XX_[Name].md`     |
| Written Chapter      | `Story/Chapters/Chapter_XX_[Name].md`            |
| Lector Report        | `Story/LECTOR_LOGS/Applied_Report_Chapter_XX.md` |
| Updated Characters   | `Characters/*.md`                                |
| Updated World        | `World/*.md` (if applicable)                     |
| Updated Plot Outline | `Story/Plot_Outline.md` (if deviations)          |

---

## Quick-Start

```
/pipe-chapter-full 1
```

This runs the complete pipeline for Chapter 1.

---

## Batch Mode (Multiple Chapters)

```
/pipe-chapter-full 1-5
```

Runs pipeline for Chapters 1 through 5 sequentially.

---

## Workflow Checklist Summary

| Phase | Description           | Status          |
| ----- | --------------------- | --------------- |
| 0     | Plot Continuity Check | ⬜ (if new arc) |
| 1     | Check/Create Outline  | ⬜              |
| 2     | Write Chapter         | ⬜              |
| 3     | Lector Analysis       | ⬜              |
| 4     | Lector Implementation | ⬜              |
| 5     | Sync From Chapter     | ⬜              |
| 6     | Token Usage Report    | ⬜              |
| 7     | Git Commit            | ⬜              |

---

**Version:** 1.0 (Complete Unified Pipeline)
