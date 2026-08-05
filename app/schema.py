from pydantic import BaseModel
class TaskCreateRequest(BaseModel):
    title: str
    priority: str
    completed: bool
