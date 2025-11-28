from typing import Optional
from pathlib import Path

from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/search",
)

# Get the template directory relative to the package root
# From /packages/api/src/api/features/search/router.py -> /packages/api/src/templates
template_dir = Path(__file__).parent.parent.parent.parent / "templates"
templates = Jinja2Templates(directory=str(template_dir))


@router.get("/", response_class=HTMLResponse)
async def search_page(
    request: Request, q: Optional[str] = Query(None, description="Search query")
):
    """
    Search page endpoint that renders the search template.
    """
    results = []

    if q:
        # TODO: Implement actual search logic
        # For now, return mock results
        results = [
            {
                "title": f"Result 1 for '{q}'",
                "description": "This is a mock search result description for the first item.",
            },
            {
                "title": f"Result 2 for '{q}'",
                "description": "This is a mock search result description for the second item.",
            },
        ]

    return templates.TemplateResponse(
        "search.html", {"request": request, "query": q, "results": results}
    )
