from fastapi import APIRouter, HTTPException, Depends
from src.db import register_user, verify_user, revoke_refresh_token, is_refresh_token_revoked, is_email_registered, get_user_id_by_email, update_user_password
from src.tokens import *
from pydantic import EmailStr
from app import mail
from fastapi_mail import MessageSchema
from os import environ

router = APIRouter()

# User Registration (Signup)
@router.post("/register/")
def user_registration(username: str, email: str, password: str):
    message = register_user(username, email, password)
    if "successfully" in message:
        return {"message": message}
    else:
        raise HTTPException(status_code=409, detail=message)

# User Login (with refresh token)
@router.post("/token/")
def login_for_access_token(username: str, password: str):
    user_id = verify_user(username, password)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user_id)})
    refresh_token = create_refresh_token({"sub": str(user_id)})
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}

# Refresh Access Token
@router.post("/refresh/")
def refresh_access_token(refresh_token: str):
    payload = decode_refresh_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    if is_refresh_token_revoked(refresh_token):
        raise HTTPException(status_code=401, detail="Refresh token has been revoked")

    access_token = create_access_token({"sub": user_id})
    return {"access_token": access_token, "token_type": "bearer"}

# Logout (Revoke Refresh Token)
@router.post("/logout/")
def logout(refresh_token: str):
    payload = decode_refresh_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    revoke_refresh_token(refresh_token)
    return {"message": "Logout successful"}

# Password Reset Request
@router.post("/reset/request/")
def password_reset_request(email: EmailStr):
    if not is_email_registered(email):
        raise HTTPException(status_code=400, detail="Email not registered")

    user_id = get_user_id_by_email(email)
    reset_token = create_reset_token({"sub": user_id})
    
    # Send password reset email
    message = MessageSchema(
        subject="Password Reset",
        recipients=[email],
        body=f"Click the link to reset your password: http://{environ.get(base_url)}/reset/{reset_token}"
    )

    mail.send_message(message)

    return {"message": "Password reset email sent"}

# Password Reset
@router.post("/reset/{reset_token}")
def password_reset(reset_token: str, new_password: str):
    payload = decode_reset_token(reset_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    update_user_password(user_id, new_password)

    return {"message": "Password reset successful"}

# Protected Route
@router.get("/protected/")
def protected_route(user_id: int = Depends(get_user_id_from_token)):
    return {"message": f"Welcome, User ID {user_id}!"}