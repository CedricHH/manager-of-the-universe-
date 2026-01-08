---
trigger: always_on
description: Webnovel writing rules - reads project-specific settings from PROJECT.md and STYLE_GUIDE.md
---
# WEBNOVEL PROJECT RULES

> **Generic rules for any Webnovel project**
> Project-specific settings are loaded from `PROJECT.md` and `STYLE_GUIDE.md`

---

## PROJECT STRUCTURE

### Core Documents (ALWAYS LOAD AND READ FIRST)

1. **`./PROJECT.md`** - Project settings (name, language, word count, GitHub URL)
2. **`./STYLE_GUIDE.md`** - Tone, voice, POV rules, dialogue examples, banned phrases
3. **`./Story/Plot_Outline.md`** - Chapter structure and plot beats

### Content Directories

| Directory                    | Content                      |
| ---------------------------- | ---------------------------- |
| `./Characters/`            | Character profiles           |
| `./World/`                 | Worldbuilding, magic systems |
| `./Story/Chapters/`        | Written chapters             |
| `./Story/Chapter-Outline/` | Chapter outlines             |

---

## CONSISTENCY RULES (MANDATORY)

### 1. Character Consistency

- **CHECK** `Characters/` profiles before writing interactions
- Maintain established personality, speech patterns, abilities
- Never contradict backstory without documentation

### 2. World Consistency

- **CHECK** `World/` files before introducing new elements
- All abilities must align with established magic system
- Locations must match prior descriptions

### 3. Plot Consistency

- **CHECK** `Story/Plot_Outline.md` for current chapter goals
- Cliffhangers must lead logically to next chapter
- Track story threads across chapters

---

## PLOT CONTINUITY RULES (MANDATORY)

> **Added after Groll duplication incident (Ch 101-104)**
> Prevents repeating conquered guilds/factions or reusing antagonist names

### Before Writing NEW ARC:

1. **RUN** `/check-plot-continuity [CHAPTER]` workflow
2. **CHECK** `Plot_Outline.md` for conquered guilds/factions
3. **SEARCH** `Characters/` for antagonist name conflicts
4. **VERIFY** conflict type differs from previous arcs
5. **DOCUMENT** differentiation in outline

### Guild Reuse Policy:

| Status | Meaning |
|--------|---------|
| ✅ ALLOWED | Revisit conquered guild as ally/resource |
| ❌ FORBIDDEN | Repeat conquest of same guild type |
| ✅ ALLOWED | Different branch of organization (e.g., Merchant Guild Oakhaven vs. Capital) |

### Character Name Policy:

| Status | Rule |
|--------|------|
| ❌ FORBIDDEN | Reuse antagonist names (even as different characters) |
| ✅ ALLOWED | Callback references to defeated antagonists |
| ⚠️ CAUTION | Similar-sounding names (e.g., Groll/Kroll/Grall) |

### Conflict Type Tracking:

**Arc 1 Used**:
- Economic warfare (Bank, Alchemist Guild)
- Regulatory warfare (Church)
- Political intrigue (Sterling)

**Arc 2+**: Must use **different** primary conflict type

---

## WORKFLOW (ENFORCED)

### Before Writing Any Chapter:

1. LOAD `PROJECT.md` - Get word count target, language
2. LOAD and READ `STYLE_GUIDE.md` - Get tone, POV, banned phrases
3. LOAD and READ Plot_Outline.md
4. CHECK Character profiles for appearing characters
5. CHECK Previous chapter for continuity
6. **NEW**: RUN Plot Continuity Check if starting new arc

### After Writing Any Chapter:

1. VERIFY word count against PROJECT.md target
2. **RUN WORKFLOW** `@[/sync-from-chapter]` to update Character/World files
3. This is **REQUIRED** for every chapter to maintain continuity
4. CROSS-CHECK for contradictions

### Verify Word Count

// turbo

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```

Compare against word target from PROJECT.md. If content needs more words, it is okay to do a bit more for a better quality.

---

## QUALITY STANDARDS

### Universal Webnovel Requirements

- **Hook**: First 200 words must grab attention
- **Pacing**: Mobile-optimized (1-3 sentence paragraphs)
- **Cliffhanger**: Every chapter ends with tension
- **Competence**: Protagonist demonstrates skill/intelligence

### Check Against STYLE_GUIDE.md For:

- Voice consistency
- Banned phrases
- System message formatting
- Dialogue style per character

---

## FINAL MANDATE

**BEFORE EVERY OUTPUT**, verify:

1. Does this match PROJECT.md settings?
2. Does this follow STYLE_GUIDE.md rules?
3. Is this consistent with Characters/ and World/?
4. Will this create a plothole?
5. **NEW**: Does this duplicate a previous arc's conflict?

**IF YES TO #4 or #5**: STOP. Revise or consult user.

**CONSISTENCY IS PARAMOUNT.**

---

## Version History

- **v1.0**: Original rules
- **v2.0**: Added Plot Continuity Rules (2026-01-06) - Prevents guild/antagonist duplication
