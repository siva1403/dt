# from fastapi import FastAPI

# app = FastAPI()

# users = [{"siva" :"krishna"}]

# @app.post("/users")
# def create_user(user: dict):
#     users.append(user)
#     return {"message": "User created", "user": user}

# @app.get("/users")
# def get_users():
#     return users



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = []

@app.post("/users")
def create_user(user: User):
    users.append(user.model_dump())
    return {
        "message": "User created",
        "user": user
    }

@app.get("/users")
def get_users():
    return users
