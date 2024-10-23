from fastapi import APIRouter, Depends
from auth import get_current_user

tasksRouter = APIRouter(
    prefix="/api",
    tags=["tasks"],
    dependencies=[Depends(get_current_user)],
)

@tasksRouter.get("/user")
def get_user(user: dict = Depends(get_current_user)):
    return {"message": "Protected tasks endpoint", "user": user}
