from flask import Flask, request
from enum import Enum
import subprocess
import urllib2
from pymongo import MongoClient
from datetime import datetime
import os, subprocess

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
                "text" : text,
                "date": datetime.datetime.utcnow()
                }

    record_id = my_collection.insert(myrecord)
    print "inserted with record-id " + record_id
    print my_collection.find_one()

    # STEP-2
    # read /etc/hosts to find master IP
    master_ip=""
    f = open("/etc/hosts")
    for line in f :
        if line.__contains__("master") :
            print line.split(" ")[0]
            master_ip = line.split(" ")[0]
    print "MASTER IP FOUND : " + master_ip
    # point docker to master
    var=os.system("docker-machine env --swarm " + master_ip)
    os.system("eval " + var)
    print "DOCKER POINTING TO COMPOSE"
    # inspect docker-compose to get # of containers running
    #os.system("docker-compose inspect --format {{}}")

    # docker scale to increase container count

    # point docker back to local

    os.system("")
    return "Done!"

@app.route('/process/<source>', methods=[ 'GET' ])
def launchProcessInstance(source):
    # launch consumer instances
    return "launch Process Instance"



if __name__ == "__main__":
    app.run(debug=True)