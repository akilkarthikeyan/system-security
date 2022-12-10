from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    1 : {
        "car_name": "Aston Martin",
        "races": 186,
        "drivers": 23,
        "wins": 10 
    }, 
    2 : {
        "car_name": "Ford",
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

@app.get('/getConstructorInfo/{constructorID}')
def constructorInfo(constructorID: int):
    if constructorID in constructors:
        return constructors[constructorID]
    return {"data": "not found"}

@app.get('/getConstructorInfo')
def constructorInfo(name: Optional[str] = None):
    for constructorID in constructors:
        if(constructors[constructorID]["name"] == name):
            return constructors[constructorID]
    return {"data": "not found"}

if __name__ == '__main__':
    uvicorn.run(app, port = 8000, host='127.0.0.1')