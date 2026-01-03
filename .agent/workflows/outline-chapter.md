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

## Step 3: Load Character Context

Read relevant character profiles from `./Characters/`

## Step 4: Load World Context

Read relevant World for the Arc from `./World/`

## Step 5: Create Beat-Sheet

Create outline based on word target from PROJECT.md:

```markdown
# Outline: Chapter XX - [Title]

**Word Target**: [from PROJECT.md]

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
```

## Step 6: Save Outline

Save to: `Story/Chapter-Outline/Chapter_XX_[Name].md`

## Step 7: User Review

Present outline for approval before `/write-chapter`

---

## Quick-Start

```
/outline-chapter 1
```

---

**Version:** 3.0 (Generic)
