from typing import List
from datetime import datetime, timedelta

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.tasks = []

    def create_task(self, task: 'Task') -> None:
        self.tasks.append(task)

    def update_task(self, task: 'Task') -> None:
        for i, t in enumerate(self.tasks):
            if t.id == task.id:
                self.tasks[i] = task
                break

    def delete_task(self, task: 'Task') -> None:
        self.tasks = [t for t in self.tasks if t.id != task.id]

    def get_tasks(self) -> List['Task']:
        return self.tasks


class Task:
    def __init__(self, title: str, description: str, start_time: datetime, end_time: datetime, assignee: User):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.assignee = assignee

    def get_duration(self) -> timedelta:
        return self.end_time - self.start_time
