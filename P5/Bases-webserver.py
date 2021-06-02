import http.server
import socketserver
import termcolor
import json
from pathlib import Path

# Define the Server's port
PORT = 8080
HTML_FILES = "./html"
answer = {'Name': 'Adenine', 'Letter': 'A', 'Link': 'https://en.wikipedia.org/wiki/Adenine', 'Formula': 'C5H5N5'}


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read(filename):
    return Path(filename).read_text()


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        file_name = self.path
        contents = None
        if self.path == "/":
            file_name += "index.html"
        elif "info/A" in self.path:
            contents = json.dumps(answer)
        elif "info" in self.path and "info/A" not in self.path:
            file_name = file_name[5:]
        print(file_name)
        if not contents:
            try:
                contents = read(HTML_FILES + file_name)
            except FileNotFoundError:
                contents = read(HTML_FILES + "/Error.html")

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        if "info/A" in self.path:
            self.send_header('Content-Type', 'application/json')
        else:
            self.send_header('Content-Type', 'text/html')
        # noinspection PyTypeChecker
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
