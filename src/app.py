from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pathlib


app = FastAPI()

BASE_DIR = pathlib.Path(__file__).parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# @app.get("/")
# def home_view():
#     return {"message": "Hello World"}

@app.get("/",response_class=HTMLResponse)
def home_post_view(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})