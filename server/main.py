from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Simulated database
db = {}

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str or None = None
    
class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str or None = None
    disabled: bool or None = None
    password: str
    
class UserInDB(User):
    hashed_password: str
    email_verified: bool
    email_verification_token: str or None = None
    password_reset_token: str or None = None
    refresh_tokens: list[str]
    role: str or None = None
    
class PasswordResetRequest(BaseModel):
    email: EmailStr
    
class PasswordReset(BaseModel):
    token: str
    new_password: str
    
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    
    user = get_user(username)
    if user is None:
        raise credential_exception
    
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    return current_user

def send_email(subject: str, recipient: str, body: str):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = EMAIL_HOST_USER
    message["To"] = recipient
    
    part = MIMEText(body, "html")
    
    message.attach(part)
    
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, recipient, message.as_string())

def send_verification_email(email: str, verification_token: str):
    subject = "Email Verification"
    body = f"""
    <html>
      <body>
        <p>Thank you for signing up! Please click the link below to verify your email:</p>
        <p><a href="{verification_token}">Verify Email</a></p>
      </body>
    </html>
    """
    
    send_email(subject, email, body)

def send_password_reset_email(email: str, password_reset_token: str):
    subject = "Password Reset"
    body = f"""
    <html>
      <body>
        <p>You have requested to reset your password. Please click the link below to reset your password:</p>
        <p><a href="{password_reset_token}">Reset Password</a></p>
      </body>
    </html>
    """
    
    send_email(subject, email, body)

def store_user(user: UserInDB):
    db[user.username] = user.model_dump()

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    refresh_token = str(uuid.uuid4())
    user.refresh_tokens.append(refresh_token)
    store_user(user)
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}

@app.post("/signup", response_model=User)
async def signup(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")
    
    if any(existing_user.email == user.email for existing_user in db.values()):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    user_data["refresh_tokens"] = []
    user_data["email_verification_token"] = str(uuid.uuid4())
    user_data["email_verified"] = False
    db[user.username] = UserInDB(**user_data)
    
    send_verification_email(user.email, user_data["email_verification_token"])
    
    return user

@app.post("/refresh-token", response_model=Token)
async def refresh_token(refresh_token: str, current_user: UserInDB = Depends(get_current_user)):
    if refresh_token not in current_user.refresh_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": current_user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logout")
async def logout(refresh_token: str, current_user: UserInDB = Depends(get_current_user)):
    if refresh_token in current_user.refresh_tokens:
        current_user.refresh_tokens.remove(refresh_token)
    return {"message": "Logged out successfully"}

@app.post("/password-reset-request")
async def password_reset_request(password_reset_request: PasswordResetRequest):
    for user in db.values():
        if user.email == password_reset_request.email:
            user.password_reset_token = str(uuid.uuid4())
            store_user(user)
            send_password_reset_email(user.email, user.password_reset_token)
            return {"message": "Password reset email sent"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/password-reset")
async def password_reset(password_reset: PasswordReset):
    for user in db.values():
        if user.password_reset_token == password_reset.token:
            hashed_password = get_password_hash(password_reset.new_password)
            user.hashed_password = hashed_password
            user.password_reset_token = None
            store_user(user)
            return {"message": "Password reset successful"}
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password reset token")

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/verify-email/{verification_token}")
async def verify_email(verification_token: str):
    for user in db.values():
        if user.email_verification_token == verification_token:
            user.email_verified = True
            user.email_verification_token = None
            store_user(user)
            return {"message": "Email verification successful"}
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email verification token")