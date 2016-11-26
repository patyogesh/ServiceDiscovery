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


@app.route('/<user>/filter/<source>/<attr>/<text>', methods=[ 'GET' ])
def launchFilterInstance(user, source, attr, text):

    #STEP -1
    #Register request with mongo-db
    client = MongoClient('10.0.2.1', 27017)
    mydb = client['test_database']
    my_collection = mydb['test-collection']
    myrecord = {
                "user_name": user,
                "source": source,
                "type": attr,
                "text" : text,
                "state" : False,
                "container_type" : "producer",
                "date": datetime.utcnow()
                }
    record_id = my_collection.insert(myrecord)
    print "inserted with record-id " + str(record_id)

    print my_collection.find({"text": text}).limit(1)
    print my_collection.find({"_id": str(record_id)}).limit(1)

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
    os.system("eval $(docker-machine env --swarm master)")

    print "DOCKER POINTING TO COMPOSE"
    # inspect docker-compose to get # of containers running and scale up by 1
    #os.system("docker-compose inspect --format {{}}")

    # docker scale to increase container count
    os.system("docker ps")
    os.system("docker-compose scale producer=2")
    os.system("docker ps")

    # point docker back to local
    os.system("eval $(docker-machine env -u)")

    return "started producer!"

@app.route('/process/<source>', methods=[ 'GET' ])
def launchProcessInstance(source):
    # launch consumer instances
    return "launch Process Instance"



if __name__ == "__main__":
    app.run(debug=True)
