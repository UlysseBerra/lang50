from fastapi import FastAPI
import uvicorn
from db import initialize_database
from routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    initialize_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)