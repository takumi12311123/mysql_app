from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title='Simple Blog',
    description='Blog using FastAPI',
    version='0.1'
)
templates = Jinja2Templates(directory="/app/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test")
def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})
    