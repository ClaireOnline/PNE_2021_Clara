import http.client
import json
import Seq1
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
        if path_name == "/":
            context["n_seq"] = len(LIST_SEQ)
            context["list_genes"] = LIST_GENES
            context["ops"] = LIST_OPS
            contents = utils.read_template(HTMLS + 'Index.html').render(context=context)
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
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"

conn = http.client.HTTPConnection(SERVER)
for gen in GENES:
    gene_id = GENES[gen]
    conn.request("GET", ENDPOINT + gene_id + PARAMS)
    res = conn.getresponse()
    print("Response received!", res.status, res.reason)
    if res.status == 200:
        res = json.loads(res.read().decode())
        # print(json.dumps(res, indent=4, sort_keys=True))
        print("Gene:", gen)
        print("Description:", res["desc"])
        sequence = Seq1.Seq(res["seq"])
        s_length = Seq1.Seq.len(sequence)
        print("Total length:", s_length)
        count_dict = Seq1.Seq.counts(sequence)
        a, c, g, t = Seq1.Seq.percentage_base(count_dict, s_length)
        print("A:", sequence.count_base("A"), "(" + a + ")")
        print("C:", sequence.count_base("C"), "(" + c + ")")
        print("G:", sequence.count_base("G"), "(" + g + ")")
        print("T:", sequence.count_base("T"), "(" + t + ")")
        print("Most frequent base:", Seq1.Seq.most_freq(Seq1.Seq.counts(sequence)))
    elif res.status == 404:
        print("Check if the ENDPOINT was correctly written!!")
