from TaskRepository import TaskRepository
import sqlite3
from task import Task
class SqliteRepository(TaskRepository):
    def __init__(self,database):
        self.connection=sqlite3.connect(database)
        self.connection.row_factory=sqlite3.Row
        self.cursor=self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            task_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            priority TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            created_at DEFAULT CURRENT_TIMESTAMP,
            updated_at DEFAULT CURRENT_TIMESTAMP
        )
    ''')
        self.connection.commit()
    def find(self,task_id):
        SQL='''SELECT * FROM tasks 
        WHERE task_id=?
'''
        self.cursor.execute(SQL,(task_id,))
        row=self.cursor.fetchone()
        if row:
            row_data=dict(row)
            return Task(row_data["task_id"],row_data["title"],row_data["priority"]
                      ,row_data["completed"],row_data["created_at"],row_data["updated_at"])
        return None
    def find_all(self):
        SQL='''SELECT * FROM tasks'''
        self.cursor.execute(SQL)
        rows=self.cursor.fetchall()
        rows_returned=[]
        for row in rows:
            row_data=dict(row)
            task=Task(row_data["task_id"],row_data["title"],row_data["priority"]
                      ,row_data["completed"],row_data["created_at"],row_data["updated_at"])
            rows_returned.append(task)
        return rows_returned
            
    def update(self,task):
        SQL='''UPDATE tasks
        SET title=?,
            priority=?,
            completed=?,
            updated_at=CURRENT_TIMESTAMP
        WHERE task_id=?
        RETURNING *'''
        self.cursor.execute(SQL,(task.title,task.priority,task.completed,task.task_id))
        row=self.cursor.fetchone()
        if row:
            row_data=dict(row)
            task.title=row_data["title"]
            task.priority=row_data["priority"]
            task.completed=row_data["completed"]
            task.updated_at=row_data["updated_at"]
            self.connection.commit()
        return task
    def delete(self,task_id):
        task=self.find(task_id)
        if task:
            SQL='''DELETE FROM tasks 
            WHERE task_id=?'''
            self.cursor.execute(SQL,(task_id,))
            self.connection.commit()
        return task
    def save(self,task):
        SQL='''INSERT INTO tasks(title,priority,completed)
            VALUES(?,?,?)
            RETURNING *;'''
        self.cursor.execute(SQL,(task.title,task.priority,task.completed))  
        row=self.cursor.fetchone()
        if row:
            row_data=dict(row)
            task.task_id=row_data["task_id"]
            task.created_at=row_data["created_at"]
            task.updated_at=row_data["updated_at"]
            self.connection.commit()
        return task
# repo=SqliteRepository(":memory:")
# task=Task(None,"Study","High",False,None,None)
# task2=Task(None,"Gym","Medium",False,None,None)
# saved_task=repo.save(task)
# repo.save(task2)
# print("SAVED")
# print(saved_task.__dict__)
# task_find=repo.find(1)
# print("FIND")
# print(task_find.__dict__)
# tasks=repo.find_all()
# print("ALL:")
# for task in tasks:
#     print(task.__dict__)    
# task.title="FastAPI"
# task.priority="Medium"
# task.completed=True
# repo.update(task)
# print("UPDATED:")
# print(task.__dict__)
# deleted=repo.delete(1)
# print("DELETED:")
# print(deleted.__dict__)
# tasks=repo.find_all()
# print("ALL:")
# for task in tasks:
#     print(task.__dict__)  