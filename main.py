from fastapi import FastAPI
from database import Database

# app object creation and calling
app = FastAPI()


# db object creation and calling
db_obj = Database()
db_obj.db_initialize()


# root route
@app.get("/")
def home() :
   return {"message" : "Site is Working"}