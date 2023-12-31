from typing import List
from sqlalchemy.orm import Session

from ..models.task import Task
from ..schemas.task import TaskCreate, Task as TaskScheme, TaskStatus


def get_tasks(db: Session) -> List[TaskScheme]:
    return db.query(Task).order_by(Task.id).all()


def get_failed_tasks(db: Session) -> List[TaskScheme]:
    return db.query(Task).filter_by(status=TaskStatus.failure).order_by(Task.id).all()


def get_non_success_tasks(db: Session) -> List[TaskScheme]:
    return db.query(Task).filter(Task.status != TaskStatus.success).order_by(Task.id).all()


def get_task(db: Session, id: int) -> TaskScheme:
    return db.get(Task, id)


def create_task(db: Session, task: TaskCreate) -> TaskScheme:
    db_task = Task(repo_url=task.repo_url, status=TaskStatus.waiting)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task
