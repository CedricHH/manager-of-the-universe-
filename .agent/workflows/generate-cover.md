---
description: generate consistent cover art for a specific chapter
---

1.  **Read Chapter Content**
    *   Read the target chapter file: `Story/Chapters/Chapter_XX_[Name].md`.
    *   Identify the **Hook** (opening), the **Core Conflict** (middle), or the **Cliffhanger** (end).
    *   Select the most visually striking scene that represents the chapter's theme.

2.  **Identify & Load Character Visuals**
    *   List which characters appear in the selected scene.
    *   **CRITICAL**: Consult `VISUAL_STYLE_GUIDE.md` for their "Corporate Fantasy" specific look (e.g. Victor's suit, Asterion's vest, Sniv's tie).
    *   If a character is NOT in the style guide, read their profile in `Characters/[Name].md` to extract visual details.

3.  **Draft Art Prompt**
    *   Consult `VISUAL_STYLE_GUIDE.md` for the base aesthetic.
    *   **Template**:
        > A digital painting of [SCENE DESCRIPTION] in a "Corporate Fantasy" style.
        > **Subject**: Victor Kaine (modern business suit, calm, analytical) interacting with [FANTASY ELEMENT].
        > **Visuals**: High contrast between gritty fantasy environment (warm lighting, dirt, stone) and clean corporate elements (cool blue holographic ARMI interface).
        > **UI Element**: A floating blue hologram with the text "[SHORT PHRASE LIKE 'ASSET ACQUIRED' OR 'LIQUIDATION']".
        > **Style**: Detailed, cinematic, dramatic lighting, book cover art.
    *   *Refine the prompt to ensure specific details from the chapter are included.*

3.  **Generate Image**
    *   Use `generate_image` with the drafted prompt.
    *   Name: `chapter_xx_cover`

4.  **Save & Organize**
    *   Create directory: `Story/Covers/Chapter_XX_[Name]/`
    *   Save file: Copy the generated artifact to `Story/Covers/Chapter_XX_[Name]/cover.png` using `run_command`.

5.  **Critique & Iterate (Optional)**
    *   Check if the image follows the "Corporate Fantasy" juxtaposition rules.
    *   If not, refine prompt and regenerate.
