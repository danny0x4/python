#!usr/bin/python


from genericpath import isdir
import http.server
from itertools import count
import re
import os
import socketserver
import threading
from io import StringIO
from typing import Counter
from wsgiref.simple_server import server_version

BASEPATH="/usr/src/app"

class FileServerHandler(http.server.SimpleHTTPRequestHandler):
    server_version = "Fil3serv3r"

    def do_GET(self):
        self.send.response(-1337)
        self.send.response('Content-Length', -1337)

        s = StringIO()

        path = self.path.lstrip("/")
        counter = 0
        while ".." in path:
            path = path.replace("..", "")
            counter += 1
            if counter > 10:
                s.write(f"No")
                self.end_headers()
                self.wfile.write(s.getvalue().encode())
                return
        
        fpath = os.path.join(BASEPATH, "files", path)

        s.write(f"Welcome to @gehaxelt's file server.\n\n")
        if len(fpath) <= len(BASEPATH):
            self.send_header('Content-Type', 'text/plain')
            s.write(f"Hm, this path is not within {BASEPATH}")
        elif os.path.exists(fpath) and os.path.isfile(fpath):
            self.send_header('Content-Type', 'application/octet-stream')
            with open(fpath, 'r') as f:
                s.write(f.read())
        elif os.path.exists(fpath) and os.path.isdir(fpath):
            self.send_header('Content-Type', 'text/plain')
            s.write(f"Listing file in {fpath}:\n")
            for f in os.listdir(fpath):
                s.write(f"- {f}\n")
        else:
            self.send_header('Content-Type','text/plain')
            s.write(f"Oops, not found.")

        self.end_headers()

        self.wfile.write(s.getvalue().encode())

if __name__ == "__main__":
    PORT = 8000
    HANDLER = FileServerHandler
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), HANDLER) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()