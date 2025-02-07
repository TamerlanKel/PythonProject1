from app.models.user import User
from app.models.task import Task
from app.backend.db import engine, Base
from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
print(CreateTable(User.__table__))