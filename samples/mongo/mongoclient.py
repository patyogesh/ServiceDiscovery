# pip install pymongo
from pymongo import MongoClient
import datetime

client = MongoClient()
client = MongoClient('localhost', 27017)
mydb = client['test_database_1'] # get database
my_collection = mydb['test-database'] # get collection

myrecord = {"author": "Duke", "title" : "PyMongo 101", "tags" : ["MongoDB", "PyMongo", "Tutorial"], "date" : datetime.datetime.utcnow() }

#record_id = my_collection.insert(myrecord)
print mydb.collection_names()
print my_collection.find_one()

# docker run -it -p 27017:27017 -v /Users/bhavneshgugnani/Documents/mongo_test:/mongo_test --name mon5 mongo /usr/bin/mongod --dbpath /mongo_test/db