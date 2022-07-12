from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
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

@app.post("/loginpage")
async def post_test(request: Request, username: str=Form(...), password: str=Form(...)):
    return templates.TemplateResponse("loginpage.html", {
        "request": request, 
        "username": username, 
        "password": password
        })

@app.post("/register")
def register_(request: Request,):
    """
    新規登録ページ
    :param request:
    :return:
    """
    return templates.TemplateResponse("register.html", {
        "request": request
        })

@app.post("/input")
def input(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})
