import io
import os
import zipfile
from pathlib import Path
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request, Response

from ..schemas.task import Task, TaskTemplate
from ..crud.tasks import get_task, get_tasks
from ..schemas.report import Report, ReportLink
from ..models.task import TaskStatus
from ..dependencies import get_db

BASE_DIR = Path(__file__).resolve().parent.parent

router = APIRouter(prefix='/downloads')


@router.get('/all')
def zip_all(request: Request, db: Session = Depends(get_db)):
    reports_path = Path(BASE_DIR.parent, "reports")

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for report in os.listdir(reports_path):
            report_path = Path(reports_path, report)
            for file in os.listdir(report_path):
                zip_file.write(f'{report_path}/{file}', f'{report}/{file}')

    headers = {
        'Content-Disposition': f'attachment; filename="reports.zip"'
    }
    return Response(content=zip_buffer.getvalue(), media_type="application/zip", headers=headers)


@router.get('/{id}')
def zip_report(request: Request, id: int, db: Session = Depends(get_db)):
    task = get_task(db, id)
    report_folder = Path(task.repo_url).name
    report_path = Path(BASE_DIR.parent, "reports", report_folder)

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file in os.listdir(report_path):
            zip_file.write(f'{report_path}/{file}', file)

    headers = {
        'Content-Disposition': f'attachment; filename="{report_folder}.zip"'
    }
    return Response(content=zip_buffer.getvalue(), media_type="application/zip", headers=headers)
