from fastapi import HTTPException
from NyaaPy import Nyaa
from . import app


@app.get("/")
async def root(q: str, category: int = 0, subcategory: int = 0, page: int = 1):
    if page not in range(1, 1000 + 1):
        raise HTTPException(400, "Page must be an integer number between 1 and 1000")

    return Nyaa.search(
        keyword=q,
        category=category,
        subcategory=subcategory,
        page=page,
    )
