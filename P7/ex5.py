import http.client
import json
import Seq1

GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "NSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362",
}
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
