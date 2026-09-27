from fastapi import FastAPI,HTTPException,Form,Request
from database import Database
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import string
import random

# app object creation and calling
app = FastAPI()

# template object creation and calling
templates = Jinja2Templates(directory="templates")

# db object creation and calling
db_obj = Database()
db_obj.db_initialize()

# Generate Short Codes
def generate_short_code() :
   characters = string.ascii_letters + string.digits
   short_code = "".join(random.choice(characters)for _ in range(6))
   return short_code

# root route
@app.get("/")
def home(request : Request) :
   return templates.TemplateResponse(
      request = request,
      name = "index.html",
      context = {"short_url" : None}
   )

# post route
@app.post("/shorten")
def shorten_url(request : Request, original_url : str = Form(...)) :
   short_code = generate_short_code()
   
   db_obj.add_url(short_code,original_url)
   
   short_url = "http://127.0.0.1:8000/" + short_code
   
   return templates.TemplateResponse(
      request = request,
      name = "index.html",
      context = {"short_url" : short_url}
   )
   
# get route
@app.get("/{short_code}")
def get_original_url(short_code):
   url_response = db_obj.get_url(short_code)
   
   if url_response is None:
    raise HTTPException(status_code=404, detail="Short URL not found")

   return RedirectResponse(url_response)