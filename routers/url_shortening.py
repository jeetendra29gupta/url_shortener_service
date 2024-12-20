from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from database import get_shorten_url_from_memory, save_shorten_url_into_memory, get_original_url_from_memory
from helpers import is_string_an_url, generate_url_hash
from models import URLItem

router = APIRouter()


@router.post("/shorten")
def shorten_url_endpoint(item: URLItem, request: Request):
    original_url = item.url
    if not is_string_an_url(original_url):
        raise HTTPException(status_code=400, detail="URL is not valid")

    shorten_url = get_shorten_url_from_memory(original_url)
    if shorten_url:
        shorten_url = shorten_url[0]  # If already shortened, use the stored one
    else:
        shorten_url = generate_url_hash(original_url)  # Generate a new shortened URL
        save_shorten_url_into_memory(original_url, shorten_url)  # Save it in the database

    return {"original_url": original_url, "shorten_url": f"{request.base_url}{shorten_url}"}


@router.get("/{shorten_url}")
def redirect_to_original(shorten_url: str):
    original_url = get_original_url_from_memory(shorten_url)
    if original_url:
        original_url = original_url[0]  # Retrieve the original URL
        return RedirectResponse(url=original_url)  # Redirect to the original URL
    else:
        raise HTTPException(status_code=404, detail="URL not found")
