from fastapi import APIRouter, HTTPException, Depends
from db import register_user, verify_user
from tokens import get_user_id_from_token, create_access_token

router = APIRouter()

# User Registration (Signup)
@router.post("/register/")
def user_registration(username: str, email: str, password: str):
    register_user(username, email, password)
    return {"message": "User registered successfully."}

# User Login
@router.post("/token/")
def login_for_access_token(username: str, password: str):
    user_id = verify_user(username, password)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user_id)})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected Route
@router.get("/protected/")
def protected_route(user_id: int = Depends(get_user_id_from_token)):
    return {"message": f"Welcome, User ID {user_id}!"}