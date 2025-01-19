from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Главная страница"}


@app.get("/user/admin")
async def root():
    return {"Вы вошли как администратор}"}

@app.get("/user/{user_id}")
async def root(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def root(username: str, age: int):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}