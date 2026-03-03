@echo off
echo ================================================================
echo   eBook Generation for "The Manager of the Universe" Arc 1
echo   Chapters 1-100
echo ================================================================
echo.
echo Step 1: Assembling manuscript from chapters 1-100...
echo ----------------------------------------------------------------
python "Tools\assemble_book.py"
if errorlevel 1 (
    echo ERROR: Assembly failed!
    pause
    exit /b 1
)
echo.
echo Step 2: Converting manuscript to EPUB...
echo ----------------------------------------------------------------
python "Tools\convert_to_epub.py"
if errorlevel 1 (
    echo ERROR: EPUB conversion failed!
    pause
    exit /b 1
)
echo.
echo ================================================================
echo   SUCCESS! eBook generation complete.
echo ================================================================
echo.
echo Output files:
echo   - Manuscript: Manager_of_Universe_Arc1_Manuscript.md
echo   - EPUB: Manager_of_Universe_Arc1.epub
echo.
pause
