from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

client = MongoClient()
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2')

db = client['taskDatabase']
collection = db['taskCollection']

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

#collection.insert_one(post).inserted_id

documents = collection.find({})
for x in documents:
    print(x)

#collection.delete_one({"author": "Mike"})
#collection.update_one({"author": "Mike"},{"$set":{"author": "Alejandro"}})

