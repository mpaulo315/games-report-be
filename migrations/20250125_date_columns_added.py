from db.sessions import get_migration_session
from datetime import datetime as dt, timezone as tz

def __migrate__():
    try:
        games = get_migration_session()

        documents = games.find({})
        updated_count = 0

        for doc in documents:
            if "release_date" in doc and doc["release_date"] is not None:
                release_date = dt.fromtimestamp(doc["release_date"]/1000, tz= tz.utc)
                
                games.update_one({
                    "_id": doc["_id"]
                }, {
                    "$set": 
                         {
                            "year": release_date.year,
                            "month": release_date.month,
                            "day": release_date.day
                        }
                    
                })
                print(f"Updated document {doc['_id']}")
                updated_count += 1
        print(f"Date columns added for {updated_count} documents.")
        print(f"{len(documents) - updated_count} documents have no release date.")
    except Exception as e:
        print(f"Error happened: {e.__class__.__name__}: {e}")

def __rollback__():
    try:
        games = get_migration_session()
        games.update_many({}, {
            "$unset": {
                "year": "",
                "month": "",
                "day": ""
            }
        })
        print("Date aditional columns removed")
    except Exception as e:
        print(f"Error happened: {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "migrate":
            __migrate__()
        elif sys.argv[1] == "rollback":
            __rollback__()
        else:
            print("Invalid argument. Use 'migrate' or 'rollback'")
    else:
        print("No argument provided. Use 'migrate' or 'rollback'")