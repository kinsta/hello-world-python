import os
import http.server
from os import curdir, sep
import socketserver

from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        full_file = curdir + sep + 'index.html'
        f = open(full_file)
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read().encode())

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()