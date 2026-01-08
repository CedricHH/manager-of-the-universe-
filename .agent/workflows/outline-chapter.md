---
description: Create a chapter outline based on the plot structure
---
# Workflow: Outline Chapter

> Generic workflow for creating chapter outlines
> Reads project-specific settings from PROJECT.md

---

## Prerequisites

- `PROJECT.md` exists in project root
- `Story/Plot_Outline.md` exists
- Character profiles in `Characters/`

---

## Step 1: Load Project Context

1. Read `./PROJECT.md` for word count target and format
2. Read `./Story/Plot_Outline.md` for chapter overview

## Step 2: Identify Target Chapter

Extract from Plot_Outline.md:

- Chapter number
- Title
- Core action/event
- Planned cliffhanger

## Step 3: Plot Continuity Check (MANDATORY)

> **CRITICAL**: Prevents repeating conquered guilds/factions or reusing antagonist names

### 3.1: Guild/Faction Check

Search Plot_Outline.md for any guild/faction mentioned in this chapter:

// turbo

```powershell
rg "[GUILD_NAME]" "Story/Plot_Outline.md" --context 2
```

**If guild was "conquered", "acquired", "defeated" in previous arc → STOP**

- Choose DIFFERENT guild/faction
- Document reason in outline

### 3.2: Character Name Check

Search Characters/ for antagonist name conflicts:

// turbo

```powershell
Get-ChildItem "Characters/" | Where-Object { $_.Name -match "[ANTAGONIST_NAME]" }
```

**If similar name exists → STOP**

- Choose completely different name
- No similar-sounding names (e.g., Groll/Kroll/Grall)

### 3.3: Conflict Type Check

Identify conflict type for this chapter/arc. Verify it differs from previous arcs:

| Arc   | Conflict Type               | Example                            |
| ----- | --------------------------- | ---------------------------------- |
| Arc 1 | Economic warfare            | Bank, Alchemist Guild              |
| Arc 1 | Regulatory capture          | Church                             |
| Arc 2 | **Must be different** | (e.g., Trade licensing, Political) |

**If conflict type is identical to previous arc → MODIFY**

---

## Step 4: Load Character Context

Read relevant character profiles from `./Characters/`

## Step 5: Load World Context

Read relevant World for the Arc from `./World/`

## Step 6: Create Beat-Sheet

Create outline based on word target from PROJECT.md:

```markdown
# Outline: Chapter XX - [Title]

**Word Target**: [from PROJECT.md]

## Continuity Verification
- [x] Guild/faction NOT previously conquered
- [x] Antagonist name is unique
- [x] Conflict type differs from previous arcs

## Characters

| Character | Role | Start State | Expected Changes |
|-----------|------|-------------|------------------|
| [Name] | Protagonist/Ally/Antagonist | [Current status, mood, goals] | [Development in this chapter] |
| [Name] | ... | ... | ... |

> **Note**: After writing, use `/sync-from-chapter` to update Character profiles with actual changes.

## Hook
[How chapter starts]

## Development
### Beat 1: [Setup]
### Beat 2: [Complication]
### Beat 3: [Escalation]

## Cliffhanger
[How chapter ends]

## Checklist
- [ ] Protagonist demonstrates competence
- [ ] Genre-specific elements present
- [ ] Cliffhanger creates urgency
- [ ] Character changes documented
```

## Step 7: Save Outline

Save to: `Story/Chapter-Outline/Chapter_XX_[Name].md`

## Step 8: Sync with Plot_Outline.md

Update `Story/Plot_Outline.md` with the new outline details:

1. Locate the chapter entry in Plot_Outline.md
2. Update/add the following fields:
   - Title (if refined)
   - Core action/event
   - Key beats from outline
   - Cliffhanger summary
3. Mark chapter status as `[OUTLINED]`

---

## Quick-Start

```
/outline-chapter 1
```

---

**Version:** 6.0 (Continuity Check + Plot_Outline Sync + Character Tracking)
