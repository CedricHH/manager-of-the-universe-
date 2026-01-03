@echo off
powershell -ExecutionPolicy Bypass -File "%~dp0count-words.ps1" %*
