import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
res = conn.getresponse()
decod_res = res.read().decode()
print(type(decod_res), decod_res)
dict_res = json.loads(decod_res)
print(type(dict_res), dict_res)
if dict_res["ping"] == 1:
    print("PING OK! The database is running")
else:
    print("Database is down")



