from pydantic import BaseModel


from ..models.task import TaskStatus


class Task(BaseModel):
    id: int
    repo_url: str
    status: TaskStatus

    class Config:
        orm_mode = True
        use_enum_values = True


class TaskCreate(BaseModel):
    repo_url: str


class TaskTemplate(BaseModel):
    id: int
    repo_url: str
    status: str
    status_text: str
    report_link: str
