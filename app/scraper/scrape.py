from dotenv import load_dotenv
import logging
from typing import Optional
from scrapesome import async_scraper

load_dotenv()

async def scrape_url(url: str, output_format_type: Optional[str] = "html", allow_redirects: Optional[bool] = True, force_playwright: Optional[bool] = False, timeout: Optional[int]=None, headers: Optional[dict]=None):
    try:
        result = await async_scraper(url=url, output_format_type=output_format_type, allow_redirects=allow_redirects, force_playwright=force_playwright, timeout=timeout, headers=headers)
        return result
    except Exception as e:
        logging.exception(e)
        return {"error":str(e)}