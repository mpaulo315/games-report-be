from fastapi import APIRouter
from repositories import games

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/")
async def list_games():
    return games.list_games()

@router.get("/count")
async def count_games():
    return games.count_games()
