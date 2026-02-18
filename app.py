
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = int(os.getenv("APP_PORT", 8000))
MESSAGE = os.getenv("APP_MESSAGE", "Default message")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = f"<h1>{MESSAGE}</h1>"
        self.wfile.write(response.encode())

server = HTTPServer(("0.0.0.0", PORT), MyHandler)
print(f"Server running on port {PORT}")
server.serve_forever()

