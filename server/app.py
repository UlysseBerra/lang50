from fastapi import FastAPI
import uvicorn
from src.db import initialize_database
from src.routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    initialize_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)