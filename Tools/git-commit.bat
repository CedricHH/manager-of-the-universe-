@echo off
chcp 65001 >nul
cd /d "g:\Meine Ablage\EBOOKS\Der Manager des Universums"

echo === Git Commit Pipeline ===
echo.

git add "Story/Chapters/"
git add "Story/LECTOR_LOGS/"
git add "Story/Sync_Reports/"
git add "Characters/"
git add "World/"

git commit -m "written, analyzed, synced"
git push origin main

echo.
echo === Done ===
pause
