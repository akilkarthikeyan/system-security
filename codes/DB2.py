from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

data = {
    "DB2" : "beqiobvceqoi"
}

@app.get('/')
def index():
    return "DB2"

@app.get('/getNodeInfo')
def nodeInfo():
    return data

if __name__ == '__main__':
    uvicorn.run(app, port = 7002, host='127.0.0.1')