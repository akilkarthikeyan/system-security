from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

constructors = {
    1 : {
        "driver_name": "David",
        "races_participated": 18,
        "races_won": 3
    }, 
    2 : {
        "driver_name": "Chris",
        "races_participated": 12,
        "races_won": 5
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
    uvicorn.run(app, port = 9000, host='127.0.0.1')