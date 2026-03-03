---
name: illustrator
description: Specialized skill for generating consistent visual assets like cover art and character portraits.
---

# Illustrator Skill

> **Role**: Art Director.
> **Focus**: Generating high-quality, consistent visual assets for the novel.

---

## CAPABILITIES

### 1. Generate Cover
**Goal**: Create a book cover or chapter cover.
**Input**: Chapter content or specific prompt.
**Style Guide**:
- **Genre**: Webnovel / Fantasy / Sci-Fi.
- **Aesthetic**: High contrast, vibrant, "Manhwa" or "Light Novel" style.
- **Format**: 2:3 aspect ratio (typically) or Square for social.

### 2. Generate Character Portrait
**Goal**: Visualize a character based on their profile.
**Input**: `Characters/[Name].md`.
**Process**:
1. meaningful visual descriptors from profile (Hair, Eyes, Key Items).
2. Construct prompt: `[Style] [Character Description] [Action/Pose] [Background]`.
3. Use `generate_image` tool.

---

## PROMPT TEMPLATES

**Standard Cover Style**:
> "Anime style digital art, high quality, 4k, detail, cinematic lighting. [Subject] in center, [Action], [Background with magical elements]."

**Character Portrait**:
> "Character design sheet, [Name], [Age], [Appearance], [Clothing], white background, high fidelity."
