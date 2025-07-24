from pymongo import MongoClient


client = MongoClient('mongodb://192.168.0.244:27017/')
# equivalent to
# client = MongoClient('mongodb://localhost:27017/')

database = client.mydatabase

user_collection = database['users']
