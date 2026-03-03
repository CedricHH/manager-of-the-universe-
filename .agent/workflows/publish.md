---
description: Convert and publish a chapter to Royal Road
---

# Publish Workflow

Use this workflow when the user wants to publish a chapter to Royal Road (e.g., `/publish Chapter 49`).

## Steps

1. **Verify Chapter Existence**
    - Run `.\Tools\count-words.bat "Story/Chapters/Chapter_XX_[Name].md"` to confirm the file exists and is ready.

2. **Convert to HTML**
    - Run `python Tools/convert_to_tinymce.py "Story/Chapters/Chapter_XX_[Name].md"`
    - Verify the output HTML file exists in `Story/Chapters-HTML/`.

3. **Upload to Royal Road**
    - Run `python Tools/RR_uploader.py --start XX --end XX --mode Y ...`

    **Modes**:
    - `1`: Draft (Save as draft)
    - `2`: Publish Now (Default)
    - `3`: Schedule

    **Scheduling Example**:
    - `python Tools/RR_uploader.py --start 50 --end 55 --mode 3 --date 2026-02-20 --time 8 --gap 1`
    - This schedules chapters 50-55 starting Feb 20th at 8 AM, one per hour.

4. **User Interaction**
    - Notify the user that the browser is open and they need to log in.
    - Monitor the script output until completion.
