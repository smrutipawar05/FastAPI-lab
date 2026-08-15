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
        pass
    def update(self,task):
        pass
    def delete(self,task_id):
        pass
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
repo=SqliteRepository(":memory:")
task=Task(None,"Study","High",False,None,None)
saved_task=repo.save(task)
print(saved_task.__dict__)
task_find=repo.find(1)
print(task_find)