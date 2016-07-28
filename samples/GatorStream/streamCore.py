from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


## Array of 4 elements
# keys[0] : ckey
# keys[1] : csecret
# keys[2] : atoken
# keys[3] : asecret
keys = []

def key_file_io():
    file = open('/home/yogesh/.twit_keys', 'r+')
    for i in range(1,5):
        l = file.readline()
        keys.append(l.split(" = ")[1])

    print "ckey - " + keys[0]
    print "csecret - " + keys[1]
    print "atoken - " + keys[2]
    print "asecret - " + keys[3]

    file.close()

class Listener(StreamListener):

    def on_data(self, raw_data):
        print raw_data
        return True

    def on_error(self, status_code):
        print status_code

key_file_io()

auth = OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

twitterstream = Stream(auth, Listener())
twitterstream.filter(track=['Yogesh'])