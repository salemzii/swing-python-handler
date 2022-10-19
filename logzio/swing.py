from jsonrpcclient import parse, request
import requests 

def CreateRecords(records: list[dict]):
    params = {"records":records}
    res = requests.post("http://localhost:8080", json=request("rpc.records.create.many", params=params), 
                        headers={"Content-type": "application/json"})

    return res.json()
