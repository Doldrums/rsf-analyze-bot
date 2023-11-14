from typing import List
from kafka import KafkaProducer
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..constants import KAFKA_HOST, KAFKA_PORT
from ..dependencies import get_db
from ..crud.tasks import create_task, get_tasks
from ..schemas.task import Task, TaskCreate

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
