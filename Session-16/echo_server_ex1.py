import http.server
import socketserver
import termcolor
from jinja2 import Template
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Define the Server's port
PORT = 8080
HTMLS = "./html/"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read(filename):
    return Path(filename).read_text()


def read_template(filename):
    return Template(Path(filename).read_text())


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if self.path == "/":
            contents = read(HTMLS + 'form-ex1.html')
        elif self.path.startswith("/echo"):
            message = parse_qs(urlparse(self.path).query)["msg"][0]
            termcolor.cprint(message, "yellow")
            contents = read_template(HTMLS + "template.html").render(msg=message)
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        # noinspection PyTypeChecker
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
