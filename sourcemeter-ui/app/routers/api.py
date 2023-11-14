from typing import List
from kafka import KafkaProducer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..models.task import TaskStatus
from ..schemas.task import Task, TaskCreate
from ..constants import KAFKA_HOST, KAFKA_PORT
from ..crud.tasks import create_task, get_failed_tasks, get_non_success_tasks, get_tasks

producer = KafkaProducer(bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}')

router = APIRouter(prefix='/api')


@router.post('/tasks', response_model=Task)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = create_task(db, task)
    producer.send('tasks', str(db_task.id).encode())

    return db_task


@router.get('/tasks', response_model=List[Task])
def list_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)


@router.post('/tasks/restart/failed', response_model=List[Task])
def restart_failed(db: Session = Depends(get_db)):
    failed_tasks = get_failed_tasks(db)
    for task in failed_tasks:
        task.status = TaskStatus.waiting
        db.commit()
        db.refresh(task)
        producer.send('tasks', str(task.id).encode())

    return failed_tasks


@router.post('/tasks/restart/non-success', response_model=List[Task])
def restart_non_success(db: Session = Depends(get_db)):
    failed_tasks = get_non_success_tasks(db)
    for task in failed_tasks:
        task.status = TaskStatus.waiting
        db.commit()
        db.refresh(task)
        producer.send('tasks', str(task.id).encode())

    return failed_tasks
