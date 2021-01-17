# Twitter Bot = DailyReasonToCelebrate

import tweepy as tp
import time
import os
from os import environ

# credentials to login to twitter api
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']

access_token = environ['access_tokey']
access_token_secret = environ['access_tokey_secret']


bearer_token ="AAAAAAAAAAAAAAAAAAAAAClmLwEAAAAAx%2F92IVuD3faWlrnq8UDsNfhCzVI%3DBwCY2APCY0bOeXy84y7bPKf9qE0ISnsqkhJemY5iiJvvnhgj6r"


auth = tp.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth, wait_on_rate_limit=True)

print("This is a Twitter bot named 'DailyReasonToCelebrate'")
