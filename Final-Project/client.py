def client(ENDPOINT, PARAMS):
    conn.request("GET", ENDPOINT + PARAMS)
    res = conn.getresponse()
    print("Response received!", res.status, res.reason)
    decod_res = res.read().decode()
    dict_res = json.loads(decod_res)
    return dict_res
