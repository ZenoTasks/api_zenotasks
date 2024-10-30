from sqlmodel import select
from models import Task, User
from sqlmodel import Session

def getTask(task_id: int,session:Session) -> Task:
    task = session.get(Task, task_id)
    return task

def createTask(task: Task,session:Session,user:User) -> Task:
    task.user = user
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def getTasks(offset: int,limit: int,session:Session,user:User) -> Task:
    tasks = session.exec(select(Task).where(Task.user == user).offset(offset).limit(limit)).all()
    return tasks

def createUser(user: User,session:Session) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def getUser(user_email: str,session:Session) -> User:
    user = session.exec(select(User).where(User.email == user_email)).first()
    return user