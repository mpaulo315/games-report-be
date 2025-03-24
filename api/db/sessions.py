from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DATABASE = getenv('DATABASE')
COLLECTION = getenv("COLLECTION")
    
def get_session():
    QUERY_URI = getenv('QUERY_URI')
    print(QUERY_URI)
    with MongoClient(QUERY_URI) as client:
        client = MongoClient(QUERY_URI)
        return client[DATABASE][COLLECTION]

def get_migration_session():
    MIGRATION_URI = getenv('MIGRATION_URI')
    with MongoClient(MIGRATION_URI) as client:
        client = MongoClient(MIGRATION_URI)
        return client[DATABASE][COLLECTION]
