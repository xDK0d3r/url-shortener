from fastapi import FastAPI
from database import Database
from pydantic import BaseModel
import string
import random

# app object creation and calling
app = FastAPI()

# db object creation and calling
db_obj = Database()
db_obj.db_initialize()

class ShortenRequest(BaseModel) :
   original_url : str

# Generate Short Codes
def generate_short_code() :
   characters = string.ascii_letters + string.digits
   short_code = "".join(random.choice(characters)for _ in range(6))
   return short_code

# root route
@app.get("/")
def home() :
   return {"message" : "Site is Working"}

# post route
@app.post("/shorten")
def shorten_url(request : ShortenRequest ) :
   short_code = generate_short_code()
   db_obj.add_url(short_code,request.original_url)
   return {"Original URL":request.original_url,
           "Short_Code" :short_code }
