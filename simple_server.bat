@echo off
echo Starting simple Python HTTP server...
echo.
echo Try accessing: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8000
pause 