import http.server
import socketserver
import webbrowser
from threading import Timer

# Use a different port
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Simple diagnostic message
print(f"Starting server on port {PORT}...")
print(f"Try accessing: http://localhost:{PORT}")

def open_browser():
    try:
        webbrowser.open(f"http://localhost:{PORT}")
        print("Browser opened")
    except:
        print("Failed to open browser, please navigate to the URL manually")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    Timer(1, open_browser).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped") 