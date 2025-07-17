@echo off
echo Generating file list...

:: Create file_list.txt in the current directory
dir /b /a-d > file_list.txt

echo ✅ File list saved to file_list.txt
pause
