from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

users = []

templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get_request(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_users(request: Request, user_id: int):
    @app.get("/user/{user_id}", response_class=HTMLResponse)
    async def get_users(request: Request, user_id: int):
        user = next((user for user in users if user.id == user_id), None)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post("/user/{username}/{age}", response_class=HTMLResponse)
async def add_user(request: Request, username: str, age: int) -> HTMLResponse:
    new_id = 1 if not users else users[-1].id + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.put("/user/{user_id}/{username}/{age}", response_class=HTMLResponse)
async def update_user(request: Request, user_id: int, username: str, age: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return templates.TemplateResponse("users.html", {"request": request, "user": users})
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}", response_class=HTMLResponse)
async def delete_user(request: Request, user_id: int) -> HTMLResponse:
    for index, user in enumerate(users):
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": users})
    raise HTTPException(status_code=404, detail="User not found")