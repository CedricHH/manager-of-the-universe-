---
description: Write a complete chapter from an outline (Webnovel format)
---
// turbo-all

# Workflow: Write Chapter

> Generic workflow for writing Webnovel chapters
> Reads project-specific settings from PROJECT.md and STYLE_GUIDE.md

---

## Prerequisites

- `PROJECT.md` exists in project root
- `STYLE_GUIDE.md` exists in project root
- Chapter outline exists in `Story/Chapter-Outline/`
- Character profiles exist in `Characters/`

---

## PHASE 1: Load Project Context

### Step 1.1: Read Project Config

Load `./PROJECT.md` to get:

- Word count target
- Language
- File locations

### Step 1.2: Read Style Guide

Load `./STYLE_GUIDE.md` to get:

- Tone and voice rules
- POV guidelines
- System message formatting
- Banned phrases
- Quality checklist

### Step 1.3: Load Chapter Context

1. Read `./Story/Plot_Outline.md` for overall story arc and chapter goals
2. Read chapter outline from `Story/Chapter-Outline/Chapter_XX_[Name].md`
3. Read relevant character profiles from `Characters/`
4. Check previous chapter for continuity

---

## PHASE 2: Write Chapter

### Step 2.1: Word Count Calibration

> **CRITICAL**: ARMI system messages and mobile-optimized formatting create "visual length" but fewer actual words.

**Target Calibration**:

| PROJECT.md Target | Actual Writing Target       | Reason                                               |
| ----------------- | --------------------------- | ---------------------------------------------------- |
| 1,500-1,800 words | **1,700-1,900 words** | System messages count as ~50% fewer words than prose |

**Word Count Distribution** (for 1,700 target):

- Hook: 250-350 words
- Development: 1,100-1,300 words
- Cliffhanger: 250-350 words

**Prose Density Rules**:

- Every ARMI message block = write 50 extra words of prose nearby
- Every chapter needs at least 4-5 paragraphs of 4+ sentences each
- Expand character thoughts and environmental descriptions

### Step 2.2: Structure

Follow the structure defined in STYLE_GUIDE.md:

1. **Hook** → Start with tension/action (250-350 words)
2. **Development** → Main content (1,100-1,300 words)
3. **Cliffhanger** → End with hook for next chapter (250-350 words)

### Step 2.3: Apply Style Rules

- Follow POV rules from STYLE_GUIDE
- Use system message format from STYLE_GUIDE
- Avoid banned phrases from STYLE_GUIDE

### Step 2.4: Quality Check

Run through the checklist in STYLE_GUIDE.md before saving.

---

## PHASE 2.5: Word Count Adjustment (If Needed)

### Step 2.5.1: Check Count Before Saving

After writing the full chapter content but BEFORE saving, estimate:

- If visual length seems "short" compared to outline beats, expand now
- Add internal monologue, environmental detail, or extended ARMI analysis

### Step 2.5.2: Post-Save Adjustment Cycle

If word count verification shows < 1,500 words:

1. Identify 2-3 sections that can be expanded
2. Add ~50-75 words per section:
   - More Victor internal analysis
   - Environmental/sensory details
   - Extended dialogue beats
3. Re-verify until target met

---

## PHASE 3: Save & Verify

### Step 3.1: Save Chapter

Save to: `Story/Chapters/Chapter_XX_[Name].md`

### Step 3.2: Verify Word Count

// turbo

```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```

Compare against word target from PROJECT.md.

---

## Quick-Start

```
/write-chapter Chapter 1
```

---

**Version:** 3.0 (Generic)
