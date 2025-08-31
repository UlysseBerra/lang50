from fastapi import APIRouter, HTTPException, Depends
from src.db import get_language_family, get_language_name, get_language_text, get_language_iso
import random

router = APIRouter()

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
