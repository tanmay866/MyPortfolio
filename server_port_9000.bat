@echo off
echo Starting Python HTTP server on port 9000...
echo.
echo Try accessing: http://localhost:9000
echo.
echo Press Ctrl+C to stop the server
echo.
python -m http.server 9000
pause 