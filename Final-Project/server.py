import http.server
import http.client
import json
import socketserver
import termcolor
import final_server_utils as utils
from urllib.parse import urlparse, parse_qs

PORT = 8080
HTMLS = "./html/"
SERVER = "127.0.0.1"


def client(ENDPOINT):
    SERV = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    conn = http.client.HTTPConnection(SERV)
    conn.request("GET", ENDPOINT + PARAMS)
    res = conn.getresponse()
    print("Response received!", res.status, res.reason)
    decod_res = res.read().decode()
    dict_res = json.loads(decod_res)
    return dict_res


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
        content_type = "text/html"
        try:
            if path_name == "/":
                contents = utils.read_template(HTMLS + 'Index.html').render(context=context)
            elif path_name == "/listSpecies":
                res_dict = client("/info/species")
                val_dict = res_dict.values()
                list_spc = []
                for dict in val_dict:
                    for val in dict:
                        spc = val["common_name"]
                        list_spc.append(spc)
                if "limit" in arguments:
                    limit = arguments["limit"][0]
                    context["limit"] = limit
                    i_limit = int(limit)
                    fin_spc_list = str(list_spc[:i_limit])
                else:
                    fin_spc_list = str(list_spc)
                context["tot_len"] = len(list_spc)
                context["fin_spc_list"] = fin_spc_list.replace("'", "").strip("[]").capitalize()
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = utils.read_template(HTMLS + 'list.html').render(context=context)
            elif path_name == "/karyotype":
                spec = arguments["species"][0]
                spec = spec.lower().replace(" ", "_")
                res_dict = client("/info/assembly/"+spec)
                kar = res_dict["karyotype"]
                context["kar"] = str(kar).replace("'", "").replace(", ", "\n").strip("[]")
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = utils.read_template(HTMLS + 'karyo.html').render(context=context)
            elif path_name == "/chromosomeLength":
                spec = arguments["species"][0]
                name = arguments["chromosome"][0]
                spec = spec.lower().replace(" ", "_")
                res_dict = client("/info/assembly/"+spec)
                res_list = res_dict["top_level_region"]
                for dict in res_list:
                    for val in dict.values():
                        if val == name:
                            length = dict["length"]
                            break
                context["len"] = str(length)
                if "json" in arguments:
                    contents = json.dumps(context)
                    content_type = "application/json"
                else:
                    contents = utils.read_template(HTMLS + 'c_length.html').render(context=context)
            else:
                contents = utils.read_template(HTMLS + 'Error.html').render()
        except:
            contents = utils.read_template(HTMLS + 'Error.html').render()

        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', content_type)

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
