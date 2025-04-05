# Portfolio Website Troubleshooting Guide

## Quick Solutions

1. **Try a different port**: 
   ```
   python -c "import http.server, socketserver; PORT = 9000; Handler = http.server.SimpleHTTPRequestHandler; httpd = socketserver.TCPServer(('', PORT), Handler); print(f'Serving at http://localhost:{PORT}'); httpd.serve_forever()"
   ```

2. **Try a different browser**: Sometimes issues are browser-specific.

3. **Run as administrator**: Right-click on Command Prompt or PowerShell and select "Run as administrator".

4. **Disable firewall temporarily**: Only do this if you're on a trusted network.

## Common Issues and Solutions

### "Website is not open on this link"

#### 1. Check if the server is running

Look for messages in your terminal confirming the server is running.
You should see something like:
```
Portfolio running at:
- Local:   http://localhost:8000
- Network: http://192.168.x.x:8000
```

#### 2. Port is already in use

If port 8000 is already in use:

- Try using a different port (e.g., 8080, 9000)
- Kill the process using port 8000:
  ```
  # For Windows:
  netstat -ano | findstr :8000
  taskkill /PID <PID> /F
  ```

#### 3. Firewall is blocking the connection

- Temporarily disable your firewall to test
- Add an exception for Python or the specific port in your firewall settings
- Run the command prompt or PowerShell as administrator

#### 4. Antivirus is blocking Python

Some antivirus programs block Python from running servers. Try:
- Adding an exception in your antivirus
- Temporarily disabling your antivirus (be careful)

#### 5. Using incorrect URL

- Make sure you're using `http://` not `https://`
- URL should be exactly `http://localhost:8000` (or whatever port you're using)
- Try accessing specific files directly, like `http://localhost:8000/index.html`

### "Missing resources (images, CSS, JS)"

Check that your directory structure is correct:
```
Portfolio/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
└── assets/
    ├── favicon.png
    ├── icon-192.png
    ├── icon-512.png
    └── Tanmay.jpg
```

### "Particles animation not working"

- Check if particles.js library is correctly included
- Check browser console for JavaScript errors (F12 → Console)

## Advanced Troubleshooting

### Check if server can bind to the port

```python
import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8000))
    print("Port is available")
    s.close()
except:
    print("Port is in use or unavailable")
```

### Check network settings

```
ipconfig /all
```

### Check running Python processes

```
tasklist | findstr python
```

### Other Tools for Testing

1. **Python http.server on specific IP**:
   ```
   python -m http.server 8000 --bind 127.0.0.1
   ```

2. **Minimal HTML test file**:
   Create a file `minimal.html` with just:
   ```html
   <!DOCTYPE html>
   <html>
   <body>
     <h1>Test Successful</h1>
   </body>
   </html>
   ```
   And try accessing `http://localhost:8000/minimal.html`

3. **Check using different device on same network**:
   If your computer shows `http://192.168.x.x:8000` as the network URL, try accessing that from a phone or another computer on the same network.

## Getting More Help

If all else fails:
- Take screenshots of any error messages
- Note the exact steps you're taking
- Describe your operating system and browser versions
- Post questions on StackOverflow with these details

## Additional Resources

- [Python http.server documentation](https://docs.python.org/3/library/http.server.html)
- [Windows Firewall configuration guide](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26)
- [Networking troubleshooting in Windows](https://support.microsoft.com/en-us/windows/fix-wi-fi-connection-issues-in-windows-9424a1f7-6a3b-65a6-4d78-7f07eee84d2c) 