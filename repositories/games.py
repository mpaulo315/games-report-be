from db.sessions import get_session

def read_games(no_id: bool = True):
    return get_session().find({}, {"_id" : 0} if no_id else {}) #.limit(5)

