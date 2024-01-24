from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import shortuuid
from urllib.parse import quote
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse

app = FastAPI()


class ShortUrl(BaseModel):
    full: str
    clicks: int = 0

short_urls = {}

@app.post("/shortUrls")
async def create_short_url(full_url: str = Form(...)):
    short_url = shortuuid.uuid()[:8]
    # short_url = ShortUrl(full=full_url)
    short_urls.update({"short_url": short_url})
    short_urls.update({"full_url": full_url})
    return {"short_url": short_url, "full_url": full_url}

@app.get("/{short_url}")
async def redirect_to_full_url(short_url: str):
    print(short_urls["full_url"])
    return RedirectResponse(short_urls["full_url"])

# Serve the HTML file and static assets
app.mount("/", StaticFiles(directory="static", html=True), name="static")
