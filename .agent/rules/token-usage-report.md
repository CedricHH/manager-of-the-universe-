# Token Management & Transparency Rule
---
trigger: always_on
---
## Mandatory Token Reporting

After completing ANY workflow, task, or response, the agent MUST provide a token usage report in the following format:
```
📊 TOKEN USAGE REPORT
─────────────────────
Input Tokens:     [number]
Output Tokens:    [number]
Total Used:       [number]
Context Window:   [number] / [max_capacity]
Utilization:      [percentage]%

Breakdown by Operation:
- [operation_name]: [tokens]
- [operation_name]: [tokens]
- ...

Efficiency Notes:
[Brief analysis of token efficiency and suggestions for optimization if applicable]
```

## Reporting Triggers

The agent must generate this report:

1. **After every completed task** (regardless of size)
2. **After multi-file operations** (with per-file breakdown)
3. **After context-heavy operations** (worldbuilding queries, cross-referencing)
4. **When approaching 70% context capacity** (with warning)
5. **Upon explicit user request** ("show tokens", "token report")

## Token Optimization Guidelines

When token usage exceeds 60% of context window:

- **Suggest**: "Context window is at [X]%. Consider breaking this task into smaller operations."
- **Offer**: Chunking strategies, file prioritization, or caching suggestions
- **Flag**: Which files/operations consumed the most tokens

## Format Requirements

- Use consistent formatting (emoji + separator lines)
- Include percentage calculations
- Provide actionable efficiency notes
- Be concise (report itself should be <100 tokens)

## Example in Practice

**Bad Response:**
```
Task completed. [no token info]
```

**Good Response:**
```
Task completed successfully. Character consistency check revealed 2 minor issues in Chapter 7.

📊 TOKEN USAGE REPORT
─────────────────────
Input Tokens:     45,231
Output Tokens:    3,847
Total Used:       49,078
Context Window:   49,078 / 2,000,000
Utilization:      2.45%

Breakdown by Operation:
- Reading /characters/*.md: 12,400 tokens
- Reading /manuscript/chapters/*.md: 28,600 tokens
- Analysis & comparison: 4,231 tokens
- Report generation: 3,847 tokens

Efficiency Notes:
Low utilization - context window well within limits. All character files loaded successfully for comprehensive analysis.
```

## Critical Threshold Warnings

When context utilization reaches certain levels, add urgency indicators:

- **70-85%**: ⚠️ Warning - Consider optimization
- **85-95%**: 🚨 High usage - Recommend task splitting
- **95%+**: 🔴 Critical - Must reduce context load

## Exception Handling

The agent may skip detailed breakdown (but not the report) for:
- Simple queries (<1000 total tokens)
- Emergency/critical tasks where speed is essential

In these cases, use shortened format:
```
📊 Quick Token Report: 892 tokens used (0.04%)
```

---

**Purpose**: This rule ensures transparency in resource usage, helps users understand computational costs, and enables better project planning for large-scale creative works.

**Last Updated**: [Date when rule was added]