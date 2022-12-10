from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import requests
import uvicorn
import random

app = FastAPI()

@app.get('/')
def index():
    return "A1"

ports=["8000","9000","10000","11000","12000"]

@app.get('/getConstructorInfo/{constructorID}')
def constructorInfo(constructorID: int):
    URL = "http://127.0.0.1:"+random.choice(ports)+"/getConstructorInfo/" + str(constructorID)
    r = requests.get(url = URL)
    data = r.json()
    return data

@app.get('/getConstructorInfo')
def constructorInfo(name: Optional[str] = None):
    URL = "http://127.0.0.1:"+random.choice(ports)+"/getConstructorInfo?name=" + name
    r = requests.get(url = URL)
    data = r.json()
    return data

if __name__ == '__main__':
    uvicorn.run(app, port = 8001, host='127.0.0.1')