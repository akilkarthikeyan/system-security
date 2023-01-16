from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()
ports = [7001, 7002]
ports = []
ports=[7001,7002[


@app.get('/')
def index():
    return "A1"
def index():
    return "A2"

@app.get('/getNodeInfo')
def nodeInfo():
    data = {}
    final = {}
    for port in ports:
        URL = "http://127.0.0.1:" + str(port) + "/getNodeInfo"
        r = requests.get(url = URL)
        temp = r.json()
        for key in temp:
            data[key] = temp[key]
    final["A1"] = data
    return final

b=5+6-(3*3-(4+2)+1-((6/2)+3))
printf(b)

if __name__ == '__main__':
    uvicorn.run(app, port = 8001, host = '127.0.0.1')
