from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from kafka import KafkaProducer
from kafka import KafkaConsumer
import threading
import json

'''
This is an array of strings in which OAuth keys/tokens are read into
secret_keys[0] : <comsumer_key>
secret_keys[1] : <consumer_secret>
secret_keys[2] : <authorization_token>
secret_keys[3] : <authorization_secret>
'''

secret_keys = []

'''
@keys_io:
    This method is to read OAuth keys/tokens from file
'''
def keys_io():
    key_file = open('/home/yogesh/.twit_keys', 'r+')

    for key in range(1,5):
        secret_keys.append(key_file.readline().split("=")[1].strip())


class Listener(StreamListener):
    prod = KafkaProducer(bootstrap_servers='localhost:9092')
    def on_data(self, raw_data):
        #print raw_data
        tweet_text = json.loads(raw_data)
        json.dumps(tweet_text, sort_keys=True, indent=4)
        print "Tweet: ", tweet_text['text']
        self.prod.send('topic1', b'msg1')
        return True

    def on_error(self, status_code):
        print status_code


def consumer():
    print 'starting consumer'
    cons = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')

    cons.subscribe(['topic1'])

    for msg in cons:
        print msg


def main():
    keys_io()
    auth = OAuthHandler(secret_keys[0], secret_keys[1])
    auth.set_access_token(secret_keys[2], secret_keys[3])

    twitterstream = Stream(auth, Listener())
    twitterstream.filter(track=['DonaldTrump'])

    t = threading.Thread(target=consumer)
    t.daemon = True
    t.start()


if __name__ == "__main__":
    main()
