from pydantic import BaseModel
class TaskCreateRequest(BaseModel):
    title: str
    priority: str
    completed: bool
class TaskResponse(BaseModel):
    tasks_id: int
    title: str
    priority: str
    completed: bool
    created_at: str
    updated_at: str