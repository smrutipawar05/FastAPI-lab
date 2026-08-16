
from fastapi import FastAPI,Depends
from app.schema import TaskCreateRequest
from app.schema import TaskResponse
from app.SqliteRepository import SqliteRepository
from app.TaskService import TaskService
app=FastAPI()
print("Creating fastAPI application.")
@app.get("/")
def home():
    return {
        "status":"running"
    }

def get_task_service():
    repository=SqliteRepository("tasks.db")
    return TaskService(repository)
@app.post("/tasks",response_model=TaskResponse)
def create_task(task: TaskCreateRequest, service:TaskService=Depends(get_task_service)):
    return service.create_task(task.title,task.priority,task.completed)

@app.get("/tasks/{task_id}",response_model=TaskResponse)
def get_task(task_id:int,service:TaskService=Depends(get_task_service)):
    return service.get_task(task_id)

@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks(
    completed: bool|None=None,
    service:TaskService=Depends(get_task_service)
):
    return service.get_tasks()
@app.put("/tasks/{task_id}",response_model=TaskResponse)
def update_task(task_id:int,task:TaskCreateRequest, service:TaskService=Depends(get_task_service)):
    return service.update_task(task_id,task.title,task.priority,task.completed)
@app.delete("/tasks/{task_id}",status_code=204)
def delete_task(task_id:int,service:TaskService=Depends(get_task_service)):
    service.delete_task(task_id)