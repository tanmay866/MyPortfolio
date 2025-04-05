import http.server
import socketserver
import socket
import webbrowser
import os
import time
from threading import Timer
import sys

# Define port and handler
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Check if index.html exists
if not os.path.exists('index.html'):
    print("\n❌ ERROR: index.html file not found in the current directory.")
    print("Make sure you are running this script from the portfolio directory.")
    print("Current directory:", os.getcwd())
    input("\nPress Enter to exit...")
    sys.exit(1)

# List important files for diagnostics
important_files = ['index.html', 'js/main.js', 'css/style.css']
missing_files = [f for f in important_files if not os.path.exists(f)]

if missing_files:
    print("\n⚠️ WARNING: Some important files are missing:")
    for file in missing_files:
        print(f"  - {file}")
    print("\nThe website may not function correctly.")
    choice = input("\nDo you want to continue anyway? (y/n): ")
    if choice.lower() != 'y':
        sys.exit(1)

# Get local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's DNS
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"  # Fallback to localhost

# Get local IP
local_ip = get_local_ip()

# Check if port is in use
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# Find available port if 8000 is in use
if is_port_in_use(PORT):
    print(f"\n⚠️ Port {PORT} is already in use. Trying another port...")
    for test_port in range(8001, 8100):
        if not is_port_in_use(test_port):
            PORT = test_port
            print(f"✅ Using port {PORT} instead.")
            break
    else:
        print("❌ Could not find an available port. Please close other applications and try again.")
        input("\nPress Enter to exit...")
        sys.exit(1)

# Create server with better error handling
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        local_url = f"http://{local_ip}:{PORT}"
        localhost_url = f"http://localhost:{PORT}"
        
        print("\n" + "="*70)
        print(f"🚀 Portfolio running at:")
        print(f"- Local:   {localhost_url}")
        print(f"- Network: {local_url}")
        print("\n📱 Share the Network URL to access this portfolio from any device on your network.")
        print("🌐 To access from outside your network, consider using a service like ngrok.")
        print("=" * 70)
        print("\n📂 Serving files from:", os.getcwd())
        print("📄 Found index.html:", os.path.getsize('index.html'), "bytes")
        print("\n⌨️  Press Ctrl+C to stop the server")
        print("="*70 + "\n")
        
        # Open browser after short delay to ensure server is ready
        def open_browser():
            print("🌐 Opening browser...")
            # Try 3 times to open the browser
            for _ in range(3):
                try:
                    webbrowser.open(localhost_url)
                    print("✅ Browser opened successfully")
                    break
                except:
                    time.sleep(1)
            else:
                print("❌ Failed to open browser automatically. Please open this URL manually:")
                print(f"   {localhost_url}")
        
        Timer(2, open_browser).start()
        
        # Start server
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped manually. Thank you for using the portfolio server!")
        except Exception as e:
            print(f"\n❌ Server error: {str(e)}")
            input("\nPress Enter to exit...")
except Exception as e:
    print(f"\n❌ Failed to start server: {str(e)}")
    print("\nPossible reasons:")
    print("1. Another program is using port", PORT)
    print("2. You may need to run this script as administrator")
    print("3. Your firewall might be blocking the connection")
    input("\nPress Enter to exit...") 