from sqlmodel import SQLModel, Field, Relationship,Date
from datetime import date
from .user import User

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    done: bool = False
    created_at: date = Field(default_factory=date.today)
    user_id: int | None = Field(foreign_key="user.id")
    user: User | None = Relationship(back_populates="tasks")