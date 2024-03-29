from fastapi import APIRouter, HTTPException, Depends
from src.db import register_user, verify_user, revoke_refresh_token, is_refresh_token_revoked, is_email_registered, get_user_id_by_email, update_user_password, get_language_family, get_language_name, get_language_text, get_points, add_points
from src.tokens import *
from pydantic import EmailStr
from src.email import send_mail
import random

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
@router.post("/reset-request/")
def password_reset_request(email: EmailStr, newPassword: str):
    if not is_email_registered(email):
        raise HTTPException(status_code=400, detail="Email not registered")

    user_id = str(get_user_id_by_email(email))
    reset_token = create_reset_token({"sub": str(user_id)})
    
    # Send password reset email
    subject = "Password Reset"  # No tuple wrapping here
    recipient = email  # No tuple wrapping here
    body = "Click the link to reset your password: http://0.0.0.0:8000/reset/" + reset_token + "?new_password="+newPassword

    send_mail(subject, recipient, body)

    return {"message": "Password reset email sent"}

# Password Reset
@router.get("/reset/{reset_token}")
def password_reset(reset_token: str, new_password: str):
    if is_refresh_token_revoked(reset_token):
        raise HTTPException(status_code=401, detail="Reset token has been revoked")
    
    payload = decode_reset_token(reset_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    user_id = int(payload.sub)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    update_user_password(user_id, new_password)
    
    revoke_refresh_token(reset_token)
    return {"message": "Password reset successful"}

@router.get("/language/")
def get_language():
    id = random.randint(1, 156)
    
    return {
        "lang_id": id,
        "lang_name": get_language_name(id),
        "lang_family": get_language_family(id),
        "lang_text": get_language_text(id)
    }

# Protected Routes
@router.get("/get_points/")
def protected_route(user_id: int = Depends(get_user_id_from_token)):
    return {"user_id": user_id, "points": get_points(user_id)}

@router.post("/add_points/")
def protected_route(points: int, user_id: int = Depends(get_user_id_from_token)):
    add_points(user_id, points)
    return {"user_id": user_id, "points": get_points(int(user_id))}