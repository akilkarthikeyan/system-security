from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    1 : {
        "driver_name": "David",
        "experience":7
    }, 
    2 : {
        "driver_name": "Chris",
        "experience":3
    }
}

class Constructor(BaseModel):
    name: str
    races: int
    drivers: int
    wins: int

@app.get('/')
def index():
    return "DB5"

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
    uvicorn.run(app, port = 13000, host='127.0.0.1')