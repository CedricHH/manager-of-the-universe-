# TOOL USAGE RULES

---

trigger: always_on
description: KEINE ABWEICHUNGEN
-------------------------------

> **MANDATORY**: Always use the provided project tools for specific tasks. Do not invent your own PowerShell commands if a tool exists.

---

## Word Count

**ALWAYS** use the `count-words.bat` script to check word counts.

```powershell
.\Tools\count-words.bat "Path/To/File.md"
```

**Reason**: This script contains specific logic for excluding metadata, comments, and non-story text that raw `Measure-Object` misses.

---

## Chapter Footers

**ALWAYS** use the `add-chapter-footers.ps1` script to update footers across multiple chapters.

```powershell
.\Tools\add-chapter-footers.ps1 -StartChapter [num] -EndChapter [num]
```

**Reason**: Ensures consistent footers with word counts and "Next Chapter" links.

---

## HTML Conversion

**ALWAYS** use `convert_to_tinymce.bat` to prepare chapters for Royal Road.

```powershell
.\Tools\convert_to_tinymce.bat "Story\Chapters\Chapter_XX.md"
```

**Reason**: Corrects CSS for ARMI messages and preserves German special characters.

---

## Royal Road Upload

**ALWAYS** use `RR_uploader_scheduled.py` for scheduled releases.

```python
python Tools\RR_uploader_scheduled.py
```

**Reason**: Automates the upload process with realistic delays and scheduling.

---

## eBook Creation

Use the following tools for book assembly and conversion:

- **Full Pipeline**: `.\Tools\generate_ebook.bat`
- **Assembly**: `python Tools\assemble_book.py` (merges chapters)
- **EPUB**: `python Tools\convert_to_epub.py`
- **DOCX**: `python Tools\convert_to_docx.py`

**Reason**: Specialized scripts for handling metadata stripping and proper ebook formatting.

---

**Last Updated**: 2026-01-04
