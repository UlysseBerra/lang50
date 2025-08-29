from fastapi import APIRouter, HTTPException, Depends
from src.db import register_user, verify_user, revoke_refresh_token, is_refresh_token_revoked, is_email_registered, get_user_id_by_email, update_user_password, get_language_family, get_language_name, get_language_text, get_language_iso
from src.tokens import *
from pydantic import EmailStr
from src.email import send_mail
import random

router = APIRouter()

# User registration (signup)
@router.post("/register/")
def user_registration(username: str, email: str, password: str):
    message = register_user(username, email, password)
    if "successfully" in message:
        return {"message": message}
    else:
        raise HTTPException(status_code=409, detail=message)

# User login (with refresh token)
@router.post("/token/")
def login_for_access_token(username: str, password: str):
    user_id = verify_user(username, password)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user_id)})
    refresh_token = create_refresh_token({"sub": str(user_id)})
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}

# Refresh access token
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

# Logout (revoke refresh token)
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

# Password reset request
@router.post("/reset-request/")
def password_reset_request(email: EmailStr):
    if not is_email_registered(email):
        raise HTTPException(status_code=400, detail="Email not registered")

    user_id = str(get_user_id_by_email(email))
    reset_token = create_reset_token({"sub": str(user_id)})

    # Send password reset email
    subject="Password Reset",
    recipient=email,
    body="Click the link to reset your password: http://0.0.0.0:8000/reset/" + reset_token,

    send_mail(subject, recipient, body)

    return {"message": "Password reset email sent"}

# Password reset
@router.post("/reset/{reset_token}")
def password_reset(reset_token: str, refresh_token: str, new_password: str):
    if is_refresh_token_revoked(reset_token):
        raise HTTPException(status_code=401, detail="Reset token has been revoked")

    payload = decode_reset_token(reset_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    user_id = int(payload.sub)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid reset token")

    update_user_password(user_id, new_password)

    payload = decode_refresh_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    revoke_refresh_token(refresh_token)
    revoke_refresh_token(reset_token)
    return {"message": "Password reset successful"}

# Routes for the game
@router.get("/language/")
def get_random_language():
    lang_id = random.randint(1, 156)
    return get_language_dict(lang_id)

@router.get("/language/all")
def get_all_languages():
    return [get_language_dict(i) for i in range(1, 157)]

@router.get("/language/{lang_id}")
def get_language_by_id(lang_id: int):
    if lang_id < 1 or lang_id > 156:
        raise HTTPException(status_code=404, detail="Language not found")
    return get_language_dict(lang_id)

def get_language_dict(lang_id: int):
    return {
        "id": lang_id,
        "lang_id": str(lang_id).zfill(3),
        "lang_iso": get_language_iso(lang_id),
        "lang_name": get_language_name(lang_id),
        "lang_family": get_language_family(lang_id),
        "lang_text": get_language_text(lang_id),
        "audio_file": f"/audio/{lang_id:03}.mp3"
    }

# Protected route
@router.get("/protected/")
def protected_route(user_id: int = Depends(get_user_id_from_token)):
    return {"message": f"Welcome, User ID {user_id}!"}
