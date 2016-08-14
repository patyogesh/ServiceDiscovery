'''
1. Arguments : kafka url : localhost : topic;
'''

from kafka import KafkaConsumer
import threading
import sys

KAFKA_SERVER_IP = 'localhost'
KAFKA_SERVER_PORT = '9092'
TOPIC = 'Trump'

def createConsumer():
    KAFKA_SERVER = KAFKA_SERVER_IP + ":" + KAFKA_SERVER_PORT
    cons = KafkaConsumer(bootstrap_servers=KAFKA_SERVER,
                         auto_offset_reset='earliest')
    cons.subscribe([TOPIC])
    for msg in cons:
        print msg

def main():
    t = threading.Thread(target=createConsumer)
    t.start()

if __name__ == "__main__":
    try:
        KAFKA_SERVER_IP = sys.argv[1]
        KAFKA_SERVER_PORT = sys.argv[2]
        TOPIC = sys.argv[3]
    except IndexError as e:
        print("Error taking arguments : ", e)
    except Exception as e:
        print("Unlnown error : ", e)
    createConsumer()
