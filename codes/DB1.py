from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

data = {
    "DB1" : "abcdefghijkl"
}

@app.get('/')
def index():
    return "DB1"

@app.get('/getNodeInfo')
def nodeInfo():
    return data

if __name__ == '__main__':
    uvicorn.run(app, port = 7001, host='127.0.0.1')