#1. Arguments : kafka url : localhost; topic;
#2.
from kafka import KafkaConsumer
import threading
import sys


KAFKA_SERVER = 'localhost:9092'
TOPIC = 'Trump'

def createConsumer():
    print 'Starting Consumer for ' + TOPIC + ' topic. Connecting to kafka at : ' + KAFKA_SERVER
    cons = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
                             auto_offset_reset='earliest')
    cons.subscribe([TOPIC])
    for msg in cons:
        print msg

def main():
    t = threading.Thread(target=createConsumer)
    t.start()

if __name__ == "__main__":
    TOPIC = sys.argv[1]
    createConsumer()