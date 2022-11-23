from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

# @app.get('/')
# def index():
#     return "A1"

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
    final[label] = data
    return final

ports = [7001, 7002]
label = 'B3'
if __name__ == '__main__':
	uvicorn.run(app, port = 8002, host = '127.0.0.1')
