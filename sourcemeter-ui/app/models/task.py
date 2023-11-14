import enum
from sqlalchemy import Column, Integer, String, Enum

from ..database import Base


@enum.unique
class TaskStatus(str, enum.Enum):
    waiting = "waiting"
    in_progress = "in_progress"
    success = "success"
    failure = "failure"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    repo_url = Column(String)
    status = Column(Enum(TaskStatus))
