@echo off 
setlocal enabledelayedexpansion 
 
rem Specify the input file 
set "inputFile=TXT.txt" 
 
rem Check if the file exists 
if not exist "%inputFile%" ( 
    echo File not found: %inputFile% 
    exit /b 
) 
 
rem Read the file line by line 
for /f "usebackq delims=" %%a in ("%inputFile%") do ( 
    echo %%a 
) 
 
endlocal 