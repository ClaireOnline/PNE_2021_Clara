import http.server
import socketserver
import termcolor
import server_utils as utils
from urllib.parse import urlparse, parse_qs

PORT = 8080
HTMLS = "./html/"
LIST_SEQ = ["ACCAGATTTAACAAG", "ACAGAACTTAACTTA", "GCTAGAGACTACAGA", "ACTAGATAATAACCG", "TACGGCTTAAACCAT"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_169P", "U5"]
LIST_OPS = ["Info", "Comp", "Rev"]

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)

        context = {}
        contents = None
        if path_name == "/":
            context["n_seq"] = len(LIST_SEQ)
            context["list_genes"] = LIST_GENES
            context["ops"] = LIST_OPS
            contents = utils.read_template(HTMLS + 'form1.html').render(context=context)
        elif path_name == "/ping":
            contents = utils.read_template(HTMLS + 'ping.html').render()
        elif path_name == "/get":
            num_seq = arguments["sequence"][0]
            contents = utils.get(LIST_SEQ, num_seq)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = utils.gene(gene)
        elif path_name == "/operation":
            seq = arguments["seq"][0]
            op = arguments["op"][0]
            if op == "Info":
                contents = utils.info(seq)
            elif op == "Comp":
                contents = utils.comp(seq)
            elif op == "Rev":
                contents = utils.rev(seq)
        else:
            contents = utils.read_template(HTMLS + 'Error.html').render()

        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', 'text/html')

        # noinspection PyTypeChecker
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

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
