from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = ''
csecret = ''
atoken = ''
asecret = ''

class Listener(StreamListener):

    def on_data(self, raw_data):
        print raw_data
        return True

    def on_error(self, status_code):
        print status_code



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterstream = Stream(auth, Listener())
twitterstream.filter(track=['Yogesh'])