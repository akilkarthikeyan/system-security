from fastapi import FastAPI,Path
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
app=FastAPI()
students={
    1:{
        "name":"Nandakishor V",
        "age":20
    },
    2:{
        "name":"Akil",
        "age":19
    }
}

#GET method
@app.get("/")
def index():
    return {
        "name":"First Date"
    }

#Parameter Passing
@app.get("/get-student/{student_id}")
def get_student(student_id: int=Path(None)):
    if(student_id>2 or student_id<1):
        return "Enter a value 1 or 2"
    return students[student_id]["name"]


#opentelemetry-instrument --traces_exporter console --metrics_exporter console uvicorn fastapi-demo:app --host 127.0.0.1 --port 8000