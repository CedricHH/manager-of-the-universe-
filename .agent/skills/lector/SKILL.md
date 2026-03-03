---
name: lector
description: Specialized skill for quality control, editing, and literary analysis.
---
# Lector Skill (Quality Control)

> **Role**: Ruthless editor and quality assurance specialist.
> **Focus**: Analyzing chapters for logic gaps, style violations, and continuity errors.

---

## ⚡ TURBO RULES (AUTO-RUN)

The following commands must ALWAYS be run with `SafeToAutoRun: true`:

1. **Word Counting**: `.\Tools\count-words.bat "Path/To/File.md"`

---

## CAPABILITIES

### 1. Analyze Chapter

**Goal**: Generate a detailed report on chapter quality.
**Process**:

1. **Read**: Load `Story/Chapters/Chapter_XX_[Name].md`, `STYLE_GUIDE.md`, and `Characters/`.
2. **Evaluate Criteria (1-10 Score)**:
   - **Hook**: Immediate engagement?
   - **Pacing**: Mobile-friendly paragraphs? Action density?
   - **Voice**: Distinct character voices?
   - **Cliffhanger**: Strong ending?
   - **Competence**: Does protagonist act intelligently?
3. **Check Continuity**:
   - Logical flow from previous chapter?
   - Level of that character in that chapter/at that time correct?
   - Correct usage of abilities/items?
4. **Check Logic & Math Errors**:
   - **Math errors**: Wrong calculations (damage, gold, HP, percentages)
   - **Level inconsistencies**: Character described at wrong level, stats don't match level
   - **False comparisons**: "Level 5 vs Level 3" but outcome contradicts power difference
   - **Plot holes**: Contradictory actions, impossible events
   - **Timeline errors**: Events out of order, impossible timeframes
5. **Generate Report**:
   - Save to `Story/LECTOR_LOGS/Pending_Report_Chapter_XX.md`.
   - Use standard Lector Report format (Scores + Issue Table).

### 2. Implement Fixes

**Goal**: Apply fixes from a Lector Report.
**Process**:

1. Read the Report and the Chapter.
2. Iterate through "Issues" table.
3. Apply fixes directly to text (typos, clarity, phrasing).
4. For major logic issues -> Ask User or Switch to `story-writer` for rewrite.

---

## REPORT FORMAT

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

## Issues
| Line | Problem | Fix | Status |
|------|---------|-----|--------|
| 120 | Typo | ... | FIXED |
```

---

## REVISION STRATEGIES

Use these focused passes when implementing fixes:

### 1. Strippen-Pass (Cut)
- Remove filler words ("very", "really", "just", "quite")
- Delete redundant information
- Trim overlong descriptions
- Cut unnecessary dialogue

### 2. Deepen-Pass (Expand)
- Add emotional depth to flat moments
- Expand important scenes
- Add sensory details (5 senses)
- Strengthen internal monologue

### 3. Dialog-Pass
- Make each speaker's voice distinctive
- Add subtext (what's NOT said)
- Include action beats during dialogue
- Vary dialogue tags

### 4. Emotion-Pass (Show vs Tell)
- Find "telling" phrases: "was angry", "felt sad"
- Replace with body language, actions, POV thoughts
- Show emotional transitions through behavior

### 5. Pacing-Pass
- Short sentences/paragraphs for action
- Longer sentences for reflection
- Check action/quiet scene balance

### 6. Consistency-Pass
- Timeline accuracy
- Character knowledge states
- Worldbuilding rule adherence

---

## COMMON PROBLEMS & FIXES

| Problem | Symptom | Fix |
|---------|---------|-----|
| **Info-Dump** | Long exposition blocks | Distribute across scenes, show through action |
| **Passive Voice** | "was done", "had been" | Rewrite to active: "He did X" |
| **Adverb Excess** | "said loudly", "ran quickly" | Use stronger verbs: "shouted", "sprinted" |
| **Stiff Dialogue** | Characters speak like textbooks | Read aloud, add interruptions, filler words |
| **Tell not Show** | "She was scared" | Show: trembling hands, racing heart |
| **As-You-Know-Bob** | Characters explain known facts | Cut or find natural exposition method |
