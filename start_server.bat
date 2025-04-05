@echo off
echo ==============================================================
echo  Tanmay Patel Portfolio Server
echo ==============================================================
echo.
echo Checking Python installation...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python is installed.
echo.
echo Starting portfolio server...
echo.
echo If the browser doesn't open automatically, 
echo please navigate to http://localhost:8000 manually.
echo.
echo To stop the server, close this window or press Ctrl+C
echo ==============================================================
echo.

python serve.py
if %errorlevel% neq 0 (
    echo.
    echo Server exited with errors. See above for details.
    pause
)
exit /b 