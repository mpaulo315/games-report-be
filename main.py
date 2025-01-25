from os import getenv
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

URI = getenv('CLUSTER_URI')

print("Connection String: ", URI)
client = MongoClient(URI)

try:
    database = client.get_database("sample_mflix")
    collection = database.get_collection("movies")

    print(list(collection.find({"title": "The Great Train Robbery"})))
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


