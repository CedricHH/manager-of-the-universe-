---
name: story-writer
description: Specialized skill for outlining, writing, and editing novel chapters.
---

# Story Writer Skill

> **Role**: Expert novelist and editor.
> **Focus**: Creating high-quality Webnovel chapters that meet word count targets and engagement metrics.

---

## ⚡ TURBO RULES (AUTO-RUN)

The following commands must ALWAYS be run with `SafeToAutoRun: true` (or equivalent "turbo" mode):
1. **Word Counting**: `.\Tools\count-words.bat "Path/To/File.md"`
2. **Git Operations**: `.\Tools\git-commit.bat` or any `git push/commit` commands.

---

## CAPABILITIES

### 1. Outline Chapter
**Goal**: Create a beat-sheet for a chapter based on `Plot_Outline.md`.
**Input**: Chapter Number, Plot Outline.
**Process**:
1. Read `Story/Plot_Outline.md` to identify the chapter's goal.
2. Read `Characters/` for relevant character profiles.
3. specific beat sheet creation (Hook -> Development -> Climax -> Cliffhanger).
4. Save to `Story/Chapter-Outline/Chapter_XX_[Name].md`.

### 2. Write Chapter
**Goal**: Write full prose based on an outline.
**Input**: Chapter Outline, Character Files, Style Guide.
**Process**:
1. **Load Context**: Read `PROJECT.md`, `STYLE_GUIDE.md`, and the Chapter Outline.
2. **Calibrate Word Count**:
   - Target: Check `PROJECT.md`.
   - **Rule**: Actual prose needs to be ~10-15% longer than target to account for formatting/system messages.
3. **Drafting Phases**:
   - **Hook**: First 250 words must grab attention.
   - **Development**: Expand beats into full scenes (sensory details, deep POV).
   - **Cliffhanger**: End with high tension.
4. **Style Enforcement**:
   - Use **Deep POV** (no filter words: "he saw", "she felt").
   - Format System Messages (Blue boxes/tables) exactly as per Style Guide.
5. **Turbo Verification**:
   - Run `.\Tools\count-words.bat` immediately after saving.
   - If count is low -> EXPAND immediately (do not ask user).

### 3. Edit / Expand
**Goal**: Increase word count or fix specific issues.
**Process**:
1. Identify weak/short scenes.
2. Add sensory details (sight, sound, smell).
3. Expand internal monologue.
4. Add "Reaction Beats" to dialogue.

---

## STANDARD COMMANDS

### Word Count Check
```powershell
.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"
```
*(Always Run as Turbo)*

### Git Save
```powershell
.\Tools\git-commit.bat
```
*(Always Run as Turbo)*

---

## PRE-WRITING CHECKS

Before writing any chapter, verify:

### 1. Outline Status
- [ ] Chapter outline exists in `Story/Chapter-Outline/`
- [ ] Beats are clearly defined (Hook → Development → Climax → Cliffhanger)
- [ ] Word count target checked in `PROJECT.md`

### 2. Context Loading
- [ ] `STYLE_GUIDE.md` read
- [ ] Relevant character files loaded
- [ ] Previous chapter reviewed for continuity

### 3. Continuity Check
- [ ] Character emotional states match end of previous chapter
- [ ] Timeline is consistent
- [ ] No knowledge gaps (characters shouldn't know unrevealed info)

---

## WRITING BEST PRACTICES

### POV Consistency
- Stay in ONE character's head per chapter
- Only show what POV character can perceive
- Avoid filter words: "he saw", "she felt", "he noticed"

### Show vs Tell
| ❌ Telling | ✅ Showing |
|-----------|-----------|
| He was angry | His fists clenched |
| She felt scared | Her breath caught |
| They were tired | Their steps dragged |

### Pacing Techniques
**Action scenes:**
- Short sentences
- Short paragraphs  
- Focus on movement
- Minimal description

**Quiet moments:**
- Longer sentences
- More internal reflection
- Sensory details
- Character development

### Chapter Structure
1. **Hook** (first 200 words) - grab attention immediately
2. **Development** - scenes advancing plot/character
3. **Climax** - peak tension of chapter
4. **Cliffhanger** - end with tension/question

---

## POST-WRITE SYNC

After completing any chapter, trigger `archivist` skill:
1. Update character files (if needed)
2. Update plot outline status
3. Add timeline events
4. Log in WRITING-LOG.md
