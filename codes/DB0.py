from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from faker import Faker
import uvicorn

app = FastAPI()
fake = Faker()

@app.get('/')
def index():
    return label

@app.get('/getNodeInfo')
def nodeInfo():
    return {
        label : name
    }

name = fake.name()

label = 'DB0'
if __name__ == '__main__':
	uvicorn.run(app, port = 7001, host = '127.0.0.1')
