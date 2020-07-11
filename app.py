# Import Libraries 
from os.path import join, dirname
from dotenv import load_dotenv
import tweepy
import os

from datetime import datetime
from threading import Timer

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
 
# Load file from the path.
load_dotenv(dotenv_path)

# Accessing variables.
status = os.getenv('CONSUMER_KEY')

# Fetch quuotes from Fortune Program
def fetch_fortune():
    category = os.getenv('CATEGORY')
    quote=os.popen('fortune ' + category).read()
    return quote

# Upload fortune tweet to twitter
def tweet_fortune():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    quote = fetch_fortune()
    while (len(quote) >= 236):
        quote = fetch_fortune()

    api.update_status(status = quote +'\n' + os.getenv('HASHTAGS'))


tweet_fortune()









