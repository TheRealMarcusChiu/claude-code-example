from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000

class PlainTextHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = b"Hello, world!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message)

if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), PlainTextHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
