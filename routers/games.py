from fastapi import APIRouter
from repositories.games import read_games

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("/")
async def list_games():
    result = read_games()
    return list(result)
