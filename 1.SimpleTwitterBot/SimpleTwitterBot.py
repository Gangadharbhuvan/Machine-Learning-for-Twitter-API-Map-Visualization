import tweepy

#Enter the access Tokens from Twitter Developer Account
#Visit http://developer.twitter.com/
ACCESS_TOKEN = "****"          
ACCESS_TOKEN_SECRET = "****" 
API_KEY = "****" 
API_SECRET_KEY = "****" 


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status(status="I'm a Twitter ML Bot ")   #Type the Tweet which you want to post on Twitter
