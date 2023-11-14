import os
from pathlib import Path
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request

from ..schemas.task import Task, TaskTemplate
from ..crud.tasks import get_task, get_tasks
from ..schemas.report import Report, ReportLink
from ..models.task import TaskStatus
from ..dependencies import get_db

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
router = APIRouter(prefix='')


@router.get('/')
def index_template(request: Request, db: Session = Depends(get_db)):
    def map_task(task: Task) -> TaskTemplate:
        status = ""
        status_text = ""
        if task.status == TaskStatus.waiting:
            status = "warning"
            status_text = "waiting"
        elif task.status == TaskStatus.in_progress:
            status = "secondary"
            status_text = "running"
        elif task.status == TaskStatus.success:
            status = "success"
            status_text = "success"
        elif task.status == TaskStatus.failure:
            status = "danger"
            status_text = "failure"

        return TaskTemplate(
            id=task.id,
            repo_url=task.repo_url,
            status=status,
            status_text=status_text,
            report_link=f'/reports/{task.id}'
        )

    tasks = [map_task(task) for task in get_tasks(db)]

    return templates.TemplateResponse("tasks.html.j2", {"request": request, "tasks": tasks})


@router.get('/reports/{id}')
def report_template(request: Request, id: int, db: Session = Depends(get_db)):
    task = get_task(db, id)
    links = []
    report_folder = Path(task.repo_url).name
    report_path = Path(BASE_DIR.parent, "reports", report_folder)

    for file in os.listdir(report_path):
        links.append(
            ReportLink(
                url=f'/reports/{report_folder}/{file}', text=file
            )
        )

    report = Report(
        id=task.id,
        links=links,
        download_link=f'/downloads/{id}'
    )

    return templates.TemplateResponse("report.html", {"request": request, "report": report})
