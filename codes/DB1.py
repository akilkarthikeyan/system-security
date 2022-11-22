from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    1 : {
        "name": "Aston Martin",
        "races": 186,
        "drivers": 23,
        "wins": 10 
    }, 
    2 : {
        "name": "Ford",
        "races": 121,
        "drivers": 3,
        "wins": 1 
    }
}

class Constructor(BaseModel):
    name: str
    races: int
    drivers: int
    wins: int

@app.get('/')
def index():
    return "DB1"

@app.get('/getConstructorInfo')
def constructorInfo():
    return constructors

if __name__ == '__main__':
    uvicorn.run(app, port = 7001, host='127.0.0.1')
