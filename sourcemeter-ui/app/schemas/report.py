from typing import List
from pydantic import BaseModel


class ReportLink(BaseModel):
    url: str
    text: str


class Report(BaseModel):
    id: int
    links: List[ReportLink]
    download_link: str
