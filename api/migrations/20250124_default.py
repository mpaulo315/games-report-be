from ijson import items
from decimal import Decimal

from db.sessions import get_migration_session

BATCH_SIZE = 10000

def __type_cast_object__(obj: dict):
    if isinstance(obj, dict):
        return {k: __type_cast_object__(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [__type_cast_object__(v) for v in obj]
    elif isinstance(obj, str):
        return obj.strip()
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj

def __migrate__():
    try:
        games = get_migration_session()
        if not games.count_documents({}):
            batch = []
            with open("data/data.json", "rb") as file:
                for record in items(file, "item"):
                    record = __type_cast_object__(record)
                    if len(batch) == BATCH_SIZE:
                        games.insert_many(batch, )
                        print(f"Inserted {len(batch)} records")
                        batch = []
                    batch.append(record)
                else:
                    print(f"Inserted {len(batch)} remaining records")
                    games.insert_many(batch)
        else:
            print("Collection already created and populated")   
    except Exception as e:
        print(f"Error happened: {e.__class__.__name__}: {e}")

def __rollback__():
    try:
        games = get_migration_session()
        games.drop()
        print("Collection dropped")        
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