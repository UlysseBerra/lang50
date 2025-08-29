from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.db import initialize_database
from src.routes import router
import uvicorn
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "src")

app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")

# origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["http://localhost:5173"], # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    initialize_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)
