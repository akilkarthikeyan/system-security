from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    1 : {
        "car_name": "Aston Martin",
        "no. of cars":6
    }, 
    2 : {
        "car_name": "Ford",
        "no. of cars":10
    }
}

class Constructor(BaseModel):
    name: str
    races: int
    drivers: int
    wins: int

@app.get('/')
def index():
    return "DB4"

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
    uvicorn.run(app, port = 11000, host='127.0.0.1')