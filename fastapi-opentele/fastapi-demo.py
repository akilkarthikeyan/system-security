from fastapi import FastAPI,Path
from fastapi_opentracing import get_opentracing_span_headers
from fastapi_opentracing.middleware import OpenTracingMiddleware

app=FastAPI()
app.add_middleware(OpenTracingMiddleware)
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
