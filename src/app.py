import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

from . import airtable

# import os


app = FastAPI()

BASE_DIR = pathlib.Path(__file__).parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@lru_cache()
def cached_dotenv():
    """ """
    load_dotenv()


cached_dotenv()

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")
AIRTABLE_URL = os.environ.get("AIRTABLE_URL")


@app.get("/")
def home_post_view(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def home_signup_view(request: Request, email: str = Form(...)):
    """
    TODO add CSRF for security
    """
    # Send email to Airtable
    airtable_client = airtable.Airtable(
        base_id=AIRTABLE_BASE_ID,
        api_key=AIRTABLE_API_KEY,
        table_name=AIRTABLE_TABLE_NAME,
        url=AIRTABLE_URL,
    )
    successful_send = airtable_client.create_records({"email": email})
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "successful_send": successful_send,
            "submitted_email": email,
        },
    )
