from fastapi import APIRouter
from repositories.games import read_games
from bson import json_util
import json

router = APIRouter()

@router.get("/games")
async def list_games():
    result = read_games()
    print(result)
    return len(list(result))
    # return json.dumps(result, default=json_util.default)
