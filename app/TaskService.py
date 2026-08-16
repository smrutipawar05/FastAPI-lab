from app.task import Task
from app.SqliteRepository import SqliteRepository

class TaskService:
    def __init__(self,repository):
        self.repository=repository
    def create_task(self,title,priority,completed):
        task=Task(None,title,priority,completed,None,None)
        return self.repository.save(task)
    def get_task(self,task_id):
        return self.repository.find(task_id)
    def get_tasks(self,completed=None):
        return self.repository.find_all()
    def update_task(self,task_id,title,priority,completed):
        task=self.get_task(task_id)
        task.title=title
        task.priority=priority
        task.completed=completed
        return self.repository.update(task)
    def delete_task(self,task_id):
        return self.repository.delete(task_id)
# repository=SqliteRepository(":memory:")
# service=TaskService(repository)
# task=service.create_task("Study","High",False)
# print(task.__dict__)
# found_task=service.get_task(1)
# print(found_task.__dict__)
# found_tasks=service.get_tasks()
# for task in found_tasks:
#     print(task.__dict__)
# updated_task=service.update_task(1,"FASTAPI","LOW",False)
# print(updated_task.__dict__)
# deleted_task=service.delete_task(1)
# print(deleted_task.__dict__)
# # check=service.get_task(1)
# # print(check.__dict__)
