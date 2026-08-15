from task import Task
from fastapi import FastAPI
from schema import TaskCreateRequest
from schema import TaskResponse
from SqliteRepository import SqliteRepository
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
        return task 
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    return {
        "status":task_id
    }
@app.get("/tasks")
def get_tasks(
    completed: bool,
    page: int,
    sort: str
):
    return {
        "completed":completed,
        "page": page,
        "sort": sort
    }
@app.post("/tasks", response_model= TaskResponse)
def post_response(task: TaskCreateRequest):
    return task

