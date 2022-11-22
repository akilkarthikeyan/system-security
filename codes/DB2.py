from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    3 : {
        "name": "Pagani",
        "races": 18,
        "drivers": 2,
        "wins": 101 
    }, 
    4 : {
        "name": "Bugatti",
        "races": 91,
        "drivers": 31,
        "wins": 0 
    }
}

class Constructor(BaseModel):
    name: str
    races: int
    drivers: int
    wins: int

@app.get('/')
def index():
    return "DB2"

@app.get('/getConstructorInfo')
def constructorInfo():
    return constructors

if __name__ == '__main__':
    uvicorn.run(app, port = 7002, host='127.0.0.1')
