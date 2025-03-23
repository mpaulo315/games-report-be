from db.sessions import get_session
from type.games import GameChart

default_projection = {
        "_id": 0,
        "title": 1,
        "console": 1,
        "genre": 1,
        "publisher": 1,
        "developer": 1,
        "critic_score": 1,
        "total_sales": 1,
        "release_date": 1
}

default_filter =  {"release_date": {"$ne": None}, "developer": {"$ne": None}}

def list_games() -> list[GameChart]:    
    return get_session().find(default_filter, default_projection).to_list()

def list_games_pg(limit: int, skip : int ) -> list[GameChart]:
    return get_session().find(default_filter, default_projection)\
        .skip(skip).limit(limit).to_list()

def count_games() -> int:
    return get_session().count_documents(default_filter, hint="_id_")

