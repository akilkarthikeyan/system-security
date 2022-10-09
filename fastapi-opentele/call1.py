from fastapi import FastAPI,Path
import requests
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


app2=FastAPI()

@app2.get("/get_student_and_clg/{std}/{clg}")
def get_student_clg(std:int,clg:int):
    URL = "http://127.0.0.1:3000/get-student-clg/"+str(std)+"/"+str(clg)
    r = requests.get(url = URL)
    data = r.json()
    return data
FastAPIInstrumentor.instrument_app(app2)
#opentelemetry-instrument --traces_exporter console --metrics_exporter console uvicorn call1:app2 --host 127.0.0.1 --port 4000