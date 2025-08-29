from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

# JWT Configurations
ACCESS_TOKEN_SECRET_KEY = os.getenv("ACCESS_SECRET")
REFRESH_TOKEN_SECRET_KEY = os.getenv("REFRESH_SECRET")
RESET_TOKEN_SECRET_KEY = os.getenv("RESET_SECRET")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30
RESET_TOKEN_EXPIRE_HOURS = 1

class ResetTokenData(BaseModel):
    sub: str

def get_user_id_from_token(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    try:
        payload = jwt.decode(token, ACCESS_TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user_id

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, ACCESS_TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_refresh_token(token: str):
    try:
        payload = jwt.decode(token, REFRESH_TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        return None

def create_reset_token(data: dict):
    to_encode = ResetTokenData(**data).model_dump()
    expire = datetime.utcnow() + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, RESET_TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_reset_token(token: str):
    try:
        payload = jwt.decode(token, RESET_TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        return ResetTokenData(**payload)
    except jwt.JWTError:
        return None