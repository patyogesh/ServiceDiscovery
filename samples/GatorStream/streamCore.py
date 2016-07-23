from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'j1M1cZsXDTqAwWWv0DB5chDur'
csecret = 'G1NHq11Yl98a8WxsPejUzLoHSImLKJsTVfHL2NXJFVGQyFWrP0'
atoken = '86263640-FYHAaNicl9Ejj9te8AI37f6tTvVtFjYWCUBy7X9vJ'
asecret = 'XsFSTRUsaGvmEiaP7fWc43TeBArZj5l7ihT01ozoGFOpo'

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