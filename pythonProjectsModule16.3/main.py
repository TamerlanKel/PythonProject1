from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_users():
    return users

@app.post("/users/{username}/{age}")
async def post_users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
               age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/users/{user_id}/{username}/{age}")
async def put_message(user_id: str, username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
               age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.delete("/users/{user_id}")
async def delete_message(user_id: str) -> str:
    users[user_id] = "Имя: {username}, возраст: {age}"
    return f"The user {user_id} is deleted"