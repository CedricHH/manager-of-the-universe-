---
trigger: always_on
description: Webnovel writing rules - reads project-specific settings from PROJECT.md and STYLE_GUIDE.md
---

# WEBNOVEL PROJECT RULES

> **Generic rules for any Webnovel project**
> Project-specific settings are loaded from `PROJECT.md` and `STYLE_GUIDE.md`

---

## PROJECT STRUCTURE

### Core Documents (ALWAYS LOAD FIRST)

1. **`./PROJECT.md`** - Project settings (name, language, word count, GitHub URL)
2. **`./STYLE_GUIDE.md`** - Tone, voice, POV rules, dialogue examples, banned phrases
3. **`./Story/Plot_Outline.md`** - Chapter structure and plot beats

### Content Directories

| Directory | Content |
|-----------|---------|
| `./Characters/` | Character profiles |
| `./World/` | Worldbuilding, magic systems |
| `./Story/Chapters/` | Written chapters |
| `./Story/Chapter-Outline/` | Chapter outlines |

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

## WORKFLOW (ENFORCED)

### Before Writing Any Chapter:
1. LOAD `PROJECT.md` - Get word count target, language
2. LOAD `STYLE_GUIDE.md` - Get tone, POV, banned phrases
3. CHECK Character profiles for appearing characters
4. CHECK Previous chapter for continuity

### After Writing Any Chapter:
1. VERIFY word count against PROJECT.md target
2. UPDATE Character files if new info revealed
3. UPDATE World files if new lore introduced
4. CROSS-CHECK for contradictions

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

**IF YES TO #4**: STOP. Revise or consult user.

**CONSISTENCY IS PARAMOUNT.**
