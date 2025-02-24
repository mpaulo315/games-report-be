from db.sessions import get_session

def list_games():
    projection = {
        "_id": 0,
        "title": 1,
        "console": 1,
        "genre": 1,
        "publisher": 1,
        "developer": 1,
        "critic_score": 1,
        "total_sales": 1,
        "na_sales": 1,
        "jp_sales": 1,
        "pal_sales": 1,
        "other_sales": 1,
        "release_date": 1
    }

    return get_session().find({}, projection).to_list(100)

def count_games():
    return get_session().count_documents({}, hint="_id_")

