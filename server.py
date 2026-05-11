from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
