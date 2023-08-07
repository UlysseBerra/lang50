from fastapi import FastAPI
import uvicorn
from src.db import initialize_database
from src.routes import router
from fastapi_mail import ConnectionConfig, FastMail
from os import environ

app = FastAPI()

# Configure email settings
conf = ConnectionConfig(
    MAIL_USERNAME = environ.get(email_address),
    MAIL_PASSWORD = environ.get(email_password),
    MAIL_FROM = environ.get(email_address),
    MAIL_PORT = environ.get(email_port),
    MAIL_SERVER = environ.get(email_server),
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)

mail = FastMail(conf)

app.include_router(router)

if __name__ == "__main__":
    initialize_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)