from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.configs import Config
from app.models.test import TestModel

app = FastAPI()
templates = Jinja2Templates(directory="/app/templates")
config = Config()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#-----------------------------------
@app.post("/user_data")
async def user_data(request: Request, userid: str = Form(...)):
    test_model=TestModel(config)
    userdata = test_model.fetch_user_by_id(userid)
    return templates.TemplateResponse("userdata.html", {
        "request": request,
        "userdata": userdata
    })

@app.post("/users_list")
def users_list(request: Request, userid: str = Form(...)):
    test_model=TestModel(config)
    userslist = test_model.fetch_upper_list(userid)
    return templates.TemplateResponse("userslist.html", {
        "request": request,
        "userslist": userslist
    })

@app.post("/signup")
def signup(request: Request, username: str = Form(...), password: str = Form(...)):
    test_model = TestModel(config)
    test_model.signup(username, password)
    return {"username": username}

#-----------------------------------

# @app.get("/register")
# def register(request: Request):
#     """
#     新規登録ページ
#     :param request:
#     :return:
#     """
#     return templates.TemplateResponse("register.html", {"request": request})


# @app.post("/login")
# def login(request: Request, username: str = Form(...), password: str = Form(...)):
#     """
#     ログイン処理
#     :param request:
#     :param username:
#     :param password:
#     :return:
#     """
#     auth_model = AuthModel(config)
#     [result, user] = auth_model.login(username, password)
#     if not result:
#         # ユーザが存在しなければトップページへ戻す
#         return templates.TemplateResponse("index.html", {"request": request, "error": "ユーザ名またはパスワードが間違っています"})
#     response = RedirectResponse("/articles", status_code=HTTP_302_FOUND)
#     session_id = session.set("user", user)
#     response.set_cookie("session_id", session_id)
#     return response


# @app.post("/register")
# def create_user(username: str = Form(...), password: str = Form(...)):
#     """
#     ユーザ登録をおこなう
#     フォームから入力を受け取る時は，`username=Form(...)`のように書くことで受け取れる
#     :param username: 登録するユーザ名
#     :param password: 登録するパスワード
#     :return: 登録が完了したら/blogへリダイレクト
#     """
#     auth_model = AuthModel(config)
#     auth_model.create_user(username, password)
#     user = auth_model.find_user_by_name_and_password(username, password)
#     response = RedirectResponse(url="/articles", status_code=HTTP_302_FOUND)
#     session_id = session.set("user", user)
#     response.set_cookie("session_id", session_id)
#     return response
