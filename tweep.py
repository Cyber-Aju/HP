Python code to fetch data from Twitter using the 
Tweepy library:

import tweepy

# Set up Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Fetch tweets containing a certain keyword
search_query = "HP printer, HP laptop, HP Computer, HP PC"
tweets = tweepy.Cursor(api.search_tweets, q=search_query).items(100)

# Print tweet text and user info
for tweet in tweets:
    print("Tweet text: ", tweet.text)
    print("User info: ", tweet.user.name, tweet.user.screen_name)
