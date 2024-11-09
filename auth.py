from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
import os
from google.oauth2 import id_token
from google.auth.transport import requests
from models import User
from crud import getUser,createUser
from sqlmodel import Session
from database import get_session
from settings import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_google_id_token(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.google_client_id)
        return idinfo
    except ValueError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
    
    
async def get_current_user(token: str = Depends(oauth2_scheme),session: Session = Depends(get_session)) -> User:
    token = token.replace("Bearer ", "")
    payload = verify_google_id_token(token)
    user = getUser(user_email=payload["email"],session=session)
    if user == None:
        user = createUser(user=User(email=payload["email"]),session=session)
    return user