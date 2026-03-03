---
name: archivist
description: Specialized skill for maintaining project consistency, updating wiki files, and tracking plot continuity.
---

# Archivist Skill

> **Role**: Historian and Librarian.
> **Focus**: Ensuring `Characters/`, `World/`, and Outlines remain perfectly synced with the written content.

---

## ⚡ TURBO RULES (AUTO-RUN)

The following commands must ALWAYS be run with `SafeToAutoRun: true`:

1. **Git Operations**: `.\Tools\git-commit.bat`

---

## CAPABILITIES

### 1. Sync From Chapter

**Goal**: Update world state based on a newly written chapter.
**Input**: Chapter File.
**Process**:

1. **Analyze Chapter**: Read the chapter to identify:
   - Status changes (Level ups, injuries, loot).
   - Relationship shifts.
   - New Lore / Locations.
   - Deviations from the Outline.
2. **Update Character Files**:
   - Open `Characters/[Name].md`.
   - Update "Current Status", "Inventory", and "Recent Developments".
   - **Constraint**: Keep "Recent Developments" to last 3-5 chapters only. Archive older ones.
3. **Update World Files**:
   - Add new locations or lore to `World/`.
4. **Update Outlines**:
   - If chapter deviated from `Story/Chapter-Outline/`, mark deviations in the outline file.
   - If plot changed, update `Story/Plot_Outline.md`.

### 2. Check Plot Continuity

**Goal**: Prevent plot holes or repetition (e.g., reusing same villain names or conflict types).
**Process**:

1. Read `Story/Plot_Outline.md` (History of arcs).
2. Check against current planned arc.
3. **Verify**:
   - No duplicate Guild conquests (unless different branch).
   - No reused Villain names.
   - Distinct Conflict Type (Economic vs Military vs Political).
4. **Report**: Pass/Fail with warnings.

---

## SYNC CHECKLIST

When running a sync, always check:

- [ ] Did the character level up?
- [ ] Did they gain EXP from kills/quests?
- [ ] Did they get new items?
- [ ] Did they make a new enemy/ally?
- [ ] Did the plot diverge from the plan?

### EXP/Level Tracking (Victor Kaine)

**ALWAYS track Victor's EXP progression per chapter:**

1. **Identify EXP Sources**:
   - Kill (lower level): Enemy Level × 10
   - Kill (equal level): Enemy Level × 50
   - Kill (higher level): Enemy Level × 100 + (Diff × 50)
   - Party Kill (coordination): 25% of above
   - Quest Completion: Variable

2. **Update Victor_Kaine.md**:
   - Add entry to "Level Progress Per Chapter" section
   - Format: `| Ch X | [Event] | +[EXP] | [Cumulative] | [Level] |`

3. **Check Level Thresholds**:

   | Level | Required | Cumulative |
   |-------|----------|------------|
   | 1→2 | 500 | 500 |
   | 2→3 | 750 | 1,250 |
   | 3→4 | 1,000 | 2,250 |
   | 4→5 | 1,500 | 3,750 |
   | 5→6 | 2,000 | 5,750 |
   | 6→7 | 3,000 | 8,750 |
   | 10+ | +50% per level | - |

4. **If Level Up occurred**:
   - Add ARMI notification to chapter (if missing)
   - Update Victor's stats (+5 points: INT+2, CHA+2, WIS+1)

### Detailed Update Criteria

**Character Files** - Update ONLY when:

- ✅ New traits shown (not already documented)
- ✅ Significant relationship changes
- ✅ Status change (injured, new knowledge, new ability)
- ✅ Important character event occurred

**Do NOT update for:**

- ❌ Details already in character file
- ❌ Small moments without long-term significance

**Plot Outline** - Mark deviations with note:

```
Deviation: [What changed] - [Reason]
```

---

## PROACTIVE WARNING SYSTEM

Issue alerts automatically when detecting:

### 1. Missing Documentation

```
💡 [Character X] mentioned but no file exists.
   Create file? (Y/N)
```

### 2. Timeline Gaps

```
💡 7 days between Ch X (Day 5) and Ch Y (Day 12).
   Document in Timeline? (Y/N)
```

### 3. Loose Threads

```
💡 [Element] introduced in Ch X, not mentioned for 5+ chapters.
   Add to Offene-Fragen.md? (Y/N)
```

### 4. Possible Contradictions

```
⚠️ CONTRADICTION DETECTED:
   Ch X: [Statement A]
   Ch Y: [Statement B]
   
   Intentional development or error?
```

### 5. Pacing Hints

```
💡 Last 3 chapters were action-heavy.
   Consider quiet moment for character development?
```

---

## SYNC ENTRY FORMAT

### For Writing-Log Entry

```markdown
## [YYYY-MM-DD]

### Chapter X: "[Title]" - Written ✅

**Word Count:** [X] words
**POV:** [Character]
**Timeline:** [Story date]

**Key Events:**
- [Event 1]
- [Event 2]

**Deviations from Outline:**
- [List or "None"]

**New Elements Introduced:**
- [List or "None"]

**Open Questions:**
- [ ] [Question for future chapters]
```
