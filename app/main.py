import os
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
from app.scraper.scrape import scrape_url

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="static")

@app.get("/status")
async def get_health():
    return {"status":"ok"}


class Scraper(BaseModel):
    url: str
    headers: Optional[dict]=None
    force_playwright: Optional[bool] = False
    allow_redirects: Optional[bool] = True
    output_format_type: Optional[str] = "html"
    timeout: Optional[int] = None


@app.post("/api/scrape")
async def scrape_page(scraper: Scraper):
    try:
        url = scraper.url
        timeout = scraper.timeout
        force_playwright = scraper.force_playwright
        headers = scraper.headers
        allow_redirects = scraper.allow_redirects
        output_format_type = scraper.output_format_type
        result = await scrape_url(url=url, output_format_type=output_format_type, headers=headers, timeout=timeout, allow_redirects=allow_redirects, force_playwright=force_playwright)
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        return JSONResponse(content=result, status_code=400)
        

@app.get("/{file_path:path}")
async def serve_static_files(file_path: str):
    """
    Serve static files from the 'static' directory based on the requested file path.
    If the requested file does not exist, serve the SPA's index.html as a fallback.

    Args:
        file_path (str): The path of the requested file relative to the 'static' directory.
                         This is captured as a path parameter, allowing nested file paths.

    Returns:
        FileResponse: The file content of the requested static file if it exists,
                      otherwise the 'index.html' file for SPA routing.

    Behavior:
        - Checks if the requested file exists inside the 'static' folder.
        - If yes, returns the file as a response.
        - If not, returns 'index.html' to allow client-side routing in single page applications (SPA).
    """
    file_location = os.path.join("static", file_path)
    if os.path.isfile(file_location):
        return FileResponse(file_location)
    # Catch-all route for SPA
    index_file_path = os.path.join("static", "index.html")
    return FileResponse(index_file_path)