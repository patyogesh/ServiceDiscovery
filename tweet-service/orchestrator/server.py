from flask import Flask, request
from enum import Enum
import subprocess
import urllib2
from pymongo import MongoClient
from datetime import datetime

class ServiceTypes(Enum):
    tweet_text = 1
    hashtags = 2
    user_mentions = 3
    coordinates = 4
    created_at = 5
    retweet_count = 6
    user = 7
    track_place = 8

app = Flask(__name__)

@app.route('/')
def index():
    return "This is Home"

@app.route('/filter/<source>/<type>/<text>', methods=[ 'GET' ])
def launchFilterInstance(source, type, text):

    #STEP -1
    #Register request with mongo-db

    client = MongoClient('mongodb', 27017)
    mydb = client['test_database_1']  # get database
    my_collection = mydb['test-database']  # get collection

    myrecord = {
                "user-name": "Duke",
                "source": source,
                "type": type,
                "Text" : text,
                "date": datetime.datetime.utcnow()
                }

    record_id = my_collection.insert(myrecord)
    print "inserted with record-id " + record_id
    #print mydb.collection_names()
    #print my_collection.find_one()

    # STEP-2
    #Spawn new container to run this Filter

    return "Done!"

@app.route('/process/<source>', methods=[ 'GET' ])
def launchProcessInstance(source):
    # launch consumer instances
    return "launch Process Instance"



if __name__ == "__main__":
    app.run(debug=True)
