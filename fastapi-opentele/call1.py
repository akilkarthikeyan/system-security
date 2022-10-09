from fastapi import FastAPI,Path
import requests
from fastapi_opentracing import get_opentracing_span_headers
from fastapi_opentracing.middleware import OpenTracingMiddleware

app2=FastAPI()

app2.add_middleware(OpenTracingMiddleware)
@app2.get("/get_student_and_clg/{std}/{clg}")
def get_student_clg(std:int,clg:int):
    URL = "http://127.0.0.1:3000/get-student-clg/"+str(std)+"/"+str(clg)
    r = requests.get(url = URL)
    data = r.json()
    return data
#opentelemetry-instrument --traces_exporter console --metrics_exporter console uvicorn call1:app2 --host 127.0.0.1 --port 4000