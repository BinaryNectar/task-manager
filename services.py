from database import SessionLocal
from models import Task

class TaskNotFoundError(Exception):
    """Raised when a Task with given ID does not exist."""
    pass

class TaskService:
    """Pure business-logic layer: all ORM calls live here."""

    def get_all_tasks(self):
        session = SessionLocal()
        try:
            return session.query(Task).all()
        finally:
            session.close()

    def get_task(self, task_id: int):
        session = SessionLocal()
        try:
            task = session.get(Task, task_id)
            if task is None:
                raise TaskNotFoundError(f"No task with id {task_id}")
            return task
        finally:
            session.close()

    def create_task(self, title: str, completed: bool = False):
        session = SessionLocal()
        try:
            task = Task(title=title, completed=completed)
            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        finally:
            session.close()

    def update_task(self, task_id: int, title: str = None, completed: bool = None):
        session = SessionLocal()
        try:
            task = session.get(Task, task_id)
            if task is None:
                raise TaskNotFoundError(f"No task with id {task_id}")
            if title is not None:
                task.title = title
            if completed is not None:
                task.completed = completed
            session.commit()
            return task
        finally:
            session.close()

    def delete_task(self, task_id: int):
        session = SessionLocal()
        try:
            task = session.get(Task, task_id)
            if task is None:
                raise TaskNotFoundError(f"No task with id {task_id}")
            session.delete(task)
            session.commit()
        finally:
            session.close()
