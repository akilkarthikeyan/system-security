import requests
from fastapi import FastAPI,Path

app1=FastAPI()

college={
    1:{
        "name":"SSN College of Engineering",
        "location":"Kalavakkam"
    },
    2:{
        "name":"ANNA UNIVERSITY",
        "location":"Guindy"
    },
    3:{
        "name":"VIT",
        "location":"Vellore"
    }
}

@app1.get("/")
def index():
    return {
        "name":"second date"
    }

@app1.get("/get-student-clg/{stud}/{clg}")
def get_student_clg(stud:int,clg:int):
    if(stud>2 or stud<1):
        return "StudentID should be 1/2"
    if(clg>3 or clg<1):
        return "ClgID should be 1/2/3 "
    URL = "http://127.0.0.1:8000/get-student/"
    URL=URL+str(stud)
    r = requests.get(url = URL)
    data = r.json()
    return data,college[clg]["name"]

print(get_student_clg(2,2))
print(get_student_clg(1,1))
print(get_student_clg(1,3))