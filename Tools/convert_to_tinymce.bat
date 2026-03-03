@echo off
REM Markdown to TinyMCE HTML Converter - Batch Wrapper
REM Usage: convert_to_tinymce.bat [options]
REM   convert_to_tinymce.bat --all              Convert all chapters
REM   convert_to_tinymce.bat Chapter_01.md      Convert single chapter

python "%~dp0convert_to_tinymce.py" %*
