# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi


# upi="mongodb://localhost:27017/"

# # Create a new client and connect to the server
# client = MongoClient(upi, server_api=ServerApi('1'))


# # Create a new database and collection
# db = client["hrmsDb"]
# users_collection = db["users"]


# from pymongo import MongoClient

# uri = "mongodb://localhost:27017/"
# client = MongoClient(uri)

# db = client["hrmsDb"]
# collection = db["users"]


from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client["hrmsDb"]
collection = db["users"]

