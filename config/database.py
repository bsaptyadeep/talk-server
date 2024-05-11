from pymongo.mongo_client import MongoClient
from decouple import config

MONGO_DB_CONNECTION_STRING=config("MONGO_DB_CONNECTION_STRING")
client = MongoClient(MONGO_DB_CONNECTION_STRING)

db = client.talkitive_ai

collection_name = db["wait_list"]