from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
load_dotenv()

from .classes import ReadOnlyCollection

URI = getenv('CLUSTER_URI')
DATABASE = getenv('DATABASE')
DEFAULT_COLLECTION = "games"
    
def get_database_conn():
    return MongoClient(URI)[DATABASE]

def get_session():
    with MongoClient(URI) as client:
        client = MongoClient(URI)
        return ReadOnlyCollection(client[DATABASE][DEFAULT_COLLECTION])

def get_migration_session():
    with MongoClient(URI) as client:
        client = MongoClient(URI)
        return client[DATABASE][DEFAULT_COLLECTION]