import json 
import tweepy as tw

class MyStreamListener(tw.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        #print(f"{tweet.user.name}:{tweet.text}")
        print(f"{tweet.user.name} --> ")
        print(f"{tweet.text}")
        
        print("\n\n")
        
    def on_error(selt, tweet):
        print("Error detected")
        
auth = tw.OAuthHandler('token', 'token')
auth.set_access_token('token', 'token')
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = MyStreamListener(api)
stream = tw.Stream(api.auth, tweets_listener)
stream.filter(track=["pkk", "pyd", "hdp"], languages=["tr"])
