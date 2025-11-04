import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor iniciado en http://localhost:" + str(PORT))
    httpd.serve_forever()
