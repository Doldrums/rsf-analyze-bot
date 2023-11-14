from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import api, views, downloads
from .database import Base, engine

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
app.include_router(views.router)
app.include_router(downloads.router)

app.mount("/reports", StaticFiles(directory="reports"), name="reports")

Base.metadata.create_all(bind=engine)
