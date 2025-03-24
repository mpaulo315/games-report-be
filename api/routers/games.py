from fastapi import APIRouter
from repositories import games
from type.games import GameChart

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/")
async def list_games() -> list[GameChart]:
    return games.list_games()

@router.get("/list")
async def list_games_pg(page: int = 1, limit : int = 100) -> list[GameChart]:
    return games.list_games_pg(limit=limit, skip=(page - 1) * limit)

@router.get("/count")
async def count_games() -> int:
    return games.count_games()
