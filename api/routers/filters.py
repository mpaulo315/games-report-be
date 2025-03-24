from fastapi import APIRouter
from repositories.filters import get_developers, get_publishers, get_genres, get_consoles, get_date_range

router = APIRouter(
    prefix="/filters",
    tags=["filters"]
)

@router.get("/developers")
async def list_developers():
    return list(get_developers())

@router.get("/publishers")
async def list_publishers():
    return list(get_publishers())

@router.get("/genres")
async def list_genres():
    return list(get_genres())

@router.get("/consoles")
async def list_consoles():
    return list(get_consoles())

@router.get("/release_date/range")
async def list_date_range():
    result = get_date_range().to_list()[0]
    del result["_id"]
    return result


