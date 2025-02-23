from db.sessions import get_session

def list_games(no_id: bool = True):
    return get_session().find({}, {"_id" : 0} if no_id else {}).to_list()

def count_games():
    return get_session().count_documents({}, hint="_id_")

