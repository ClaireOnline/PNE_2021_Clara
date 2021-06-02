import http.client
import json

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
ID = GENES["MIR633"]
PARAMS = "?content-type=application/json"
TO_GET = ENDPOINT + ID + PARAMS


conn = http.client.HTTPConnection(SERVER)
conn.request("GET", TO_GET)
res = conn.getresponse()
print("Response received!", res.status, res.reason)
if res.status == 200:
    res = json.loads(res.read().decode())
    # print(json.dumps(res, indent=4, sort_keys=True))
    print("Gene", ID)
    print("Description:", res["desc"])
    print("Bases:", res["seq"])
elif res.status == 404:
    print("Check if the ENDPOINT was correctly written!!")

