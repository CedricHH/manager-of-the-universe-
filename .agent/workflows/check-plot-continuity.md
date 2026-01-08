---
description: Verify no plot/character duplication before new arc
---

# Workflow: Check Plot Continuity

> Run BEFORE starting any new arc (Ch 101, 201, 301, etc.)
> Prevents repeating conquered guilds, reusing antagonist names, or duplicating conflict types

---

## When to Use

- Before starting new arc (Chapter 101, 201, 301...)
- When introducing major new antagonist
- When planning guild/faction conflicts

---

## Step 1: Load Arc Summary

// turbo
```powershell
# View Arc 1 completion status
rg "conquered|acquired|defeated|under.*control" "Story/Plot_Outline.md" --context 1
```

## Step 2: Check Conquered Guilds

Create checklist from Plot_Outline.md:

| Guild/Faction | Status | Arc Conquered |
|--------------|--------|---------------|
| Alchemist Guild | ✅ Conquered | Arc 1 (Ch 78-79) |
| Mercenary Guild | ✅ Conquered | Arc 1 (Ch 79) |
| Church of Light | ⚠️ Truce | Arc 1 (Ch 71-75) |
| Merchant Guild | ❌ Available | - |
| Adventurer Guild | ❓ Check | - |

**Update this table before each new arc!**

## Step 3: Search Character Names

// turbo
```powershell
# List all character files
Get-ChildItem "Characters/*.md" | Select-Object Name | Sort-Object Name
```

Before creating new antagonist, verify:
- [ ] Name doesn't exist in Characters/
- [ ] Name doesn't sound similar to existing characters
- [ ] Title (Guildmaster, Guild Master) doesn't duplicate

## Step 4: Conflict Type Diversity

**Arc 1 Conflict Types Used**:
- Economic warfare (Bank, Guild debt acquisition)
- Regulatory capture (Church audit)
- Political intrigue (Sterling family)

**Arc 2 Must Use Different Type**:
- Trade licensing / Market access
- Territorial expansion
- Consortium politics
- Magical research conflict

## Step 5: Document Decision

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

## Quick Reference

### Forbidden (Already Used):
- ❌ Alchemist Guild as antagonist
- ❌ Name "Groll" or similar
- ❌ Debt acquisition as primary tactic

### Allowed:
- ✅ Merchant Guild as new antagonist
- ✅ Licensing/regulatory conflict
- ✅ Cross-city expansion

---

## Quick-Start

```
/check-plot-continuity 101
```

---

**Version:** 1.0
