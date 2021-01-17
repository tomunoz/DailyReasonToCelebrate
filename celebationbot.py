# Twitter Bot = DailyReasonToCelebrate

import tweepy as tp
import DateTime
import time
import os
from os import environ

#print("This is a Twitter bot named 'DailyReasonToCelebrate' 1")
# credentials to login to twitter api
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']

ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth, wait_on_rate_limit=True)

#print("This is a Twitter bot named 'DailyReasonToCelebrate'")

Holidays = {"2021-01-16":"Teachers Day : Thailand"}
Date_Today = date.today()
#print("Today's date is ", Date_Today)

#print(Holidays["2021-01-16"])

api.update_status(Holidays["2021-01-16"])
