import tweepy
from textblob import TextBlob

# Keys from twitter
consumer_key = 'HwIFBMBswrI0mmelBwgiZ2DBH'
consumer_secret = 'thEwDEPcZtwqU4s2Vps4HhXaAuvNGPM916GzPPy5tv7o3vwyrP'

access_token = '34707694-XrgabGuLUgNb9gkiNehKha3K7sD7GsJARAYqGtMWh'
access_token_secret = 'xp0fW7ERROZbLpzk7DjcpE1rA6tGO660t2Z3wyOYT34cG'

# Authenticate with keys and method inside tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)   # Can now do stuff like create tweet, delete tweet, search for users

# Search for tweets, collect tweets that contain a certain keyword
public_tweets = api.search('Lebron')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)