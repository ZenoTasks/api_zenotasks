from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
import os
from google.oauth2 import id_token
from google.auth.transport import requests

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_google_id_token(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        print(idinfo)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
    
async def get_current_user(token: str = Depends(oauth2_scheme)):
    print("token",token)
    token = token.replace("Bearer ", "")
    payload = verify_google_id_token(token)
    return payload