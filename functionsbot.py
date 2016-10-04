import os
import time
from twython import Twython 
from twython import TwythonStreamer
import tweepy
from PIL import Image

APP_KEY = "YT0n4XhQ3KqpuXw8IWSSh7jKV"
APP_SECRET = "mh6fE1IzH4FoztO2hycfqTVAn95P7twwRCIIZmqyy3hN72eFpL"
OAUTH_TOKEN = "709596278359896064-GwOOw4Ggy5gRWbZojIiSxEROEPhdwuX"
OAUTH_TOKEN_SECRET = "z2twAX2MypbGZvCRZqSRE2uSFUyShqYzTScqVNLFvtE4O"


def publicphoto(photo):
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter.update_status_with_media(status='status for photo', media=photo)
    time.sleep(4)

def config():
	auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
	auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	api = tweepy.API(auth)

def status(String status)
	config()
	api.update_status(status)

#bname = @nametwitter
def message(String bname, String btext)
	api.send_direct_message(screen_name = bname, text = btext)

#show tweets
def tweets():
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
    	print tweet.text

#2 form for upload media
def media(photo)
	f = Image.open(photo)
	api.update_with_media(status = 'status',media = f)
