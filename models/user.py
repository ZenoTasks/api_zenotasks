from sqlmodel import SQLModel, Field, Relationship
from typing import List

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    tasks: List["Task"] = Relationship(back_populates="user")

from .task import Task