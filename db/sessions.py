from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
load_dotenv()

URI = getenv('CLUSTER_URI')
DATABASE = getenv('DATABASE')
COLLECTION = "games"


class ReadOnlyCollection:
    def __init__(self, collection):
        self.__collection = collection
    
    def find(self, *args, **kwargs):
        return self.__collection.find(*args, **kwargs)

    def find_one(self, *args, **kwargs):
        return self.__collection.find_one(*args, **kwargs)
    
    def aggregate(self, *args, **kwargs):
        return self.__collection.aggregate(*args, **kwargs)

    def distinct(self, *args, **kwargs):
        return self.__collection.distinct(*args, **kwargs)
    
    def count_documents(self, *args, **kwargs):
        return self.__collection.count_documents(*args, **kwargs)
    
    
def get_session():
    with MongoClient(URI) as client:
        client = MongoClient(URI)
        client[DATABASE].command('ping')
        return ReadOnlyCollection(client[DATABASE][COLLECTION])

def get_migration_session():
    with MongoClient(URI) as client:
        client = MongoClient(URI)
        return client[DATABASE][COLLECTION]