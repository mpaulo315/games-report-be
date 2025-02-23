from db.sessions import get_session

def get_developers():
    return get_session().distinct("developer")

def get_publishers():
    return get_session().distinct("publisher")

def get_genres():
    return get_session().distinct("genre")

def get_consoles():
    return get_session().distinct("console")

def get_date_range():
    return get_session().aggregate([
        {
            "$group": {
                "_id": None,
                "min": {"$min": "$release_date"},
                "max": {"$max": "$release_date"}
            }
        }
    ])