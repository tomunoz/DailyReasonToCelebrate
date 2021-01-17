# Twitter Bot = DailyReasonToCelebrate

import tweepy as tp
from datetime import date
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

Holidays = {"2021-01-16":"Jan 16 : Teachers Day : Thailand",
            "2021-01-17":"Jan 17 : National Hot Buttered Rum Day : Unknown Location",
            "2021-01-18":"Jan 18 : Winnie The Pooh Day : Where Winnie The Pooh Is Loved"}

Date_Today = date.today()

try:
    api.update_status(Holidays[Date_Today])
except:
    pass
