from aiohttp import web 
import jinja2 
import aiohttp_jinja2 
from db import Base, engine

def setup_routes(application):
   from app.github.routes import setup_routes
   setup_routes(application) 

def setup_external_libraries(application: web.Application) -> None:
   aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))

def setup_app(application):
   setup_external_libraries(application)
   setup_routes(application)

app = web.Application() 

if __name__ == "__main__": 
   setup_app(app) 
   Base.metadata.create_all(bind = engine)
   web.run_app(app, port=11002)
