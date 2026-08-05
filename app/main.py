from fastapi import FastAPI
from app.schema import TaskCreateRequest
app=FastAPI()
print("Creating fastAPI application.")
@app.get("/")
def home():
    return {
        "status":"running"
    }
@app.post("/tasks")
def create_task(task: TaskCreateRequest):
    print(task)
    return {task}   