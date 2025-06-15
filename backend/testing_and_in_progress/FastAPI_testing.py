
from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# Define a simple route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to the In Progress API!"}