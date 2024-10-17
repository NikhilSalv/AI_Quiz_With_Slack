from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Create a model to accept user input
class User(BaseModel):
    name: str

# Define route to accept POST request with a username
@app.post("/greet/")
def greet_user(user: User):
    return {"message": f"Hello {user.name}!"}
