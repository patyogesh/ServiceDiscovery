from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

secret_keys = []
# secret_keys[0] : ckey = '<comsumer_key>'
# secret_keys[1] : csecret = '<consumer_secret>'
# secret_keys[2] : atoken = '<authorization_token>'
# secret_keys[3] : asecret = '<authorization_secret>'

def keys_io():
    key_file = open('/home/yogesh/.twit_keys', 'r+')
    for key in range(1,5):
        secret_keys.append(key_file.readline().split(" = ")[1])

    for i in secret_keys:
        print i

keys_io()

class Listener(StreamListener):

    def on_data(self, raw_data):
        print raw_data
        return True

    def on_error(self, status_code):
        print status_code



auth = OAuthHandler(secret_keys[0], secret_keys[1])
auth.set_access_token(secret_keys[2], secret_keys[3])

twitterstream = Stream(auth, Listener())
twitterstream.filter(track=['Yogesh'])
