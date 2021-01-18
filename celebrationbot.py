# Twitter Bot = DailyReasonToCelebrate

import tweepy as tp
from datetime import date
import time
import os
from os import environ
import pandas as pd

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
Date_Today = date.today()

Holidays_df = pd.read_excel("DailyHolidays.xlsx")
today_holidays_df = Holidays_df.loc[Holidays_df["Date"] == str(Date_Today)]
today_holidays_days = today_holidays_df["Holiday"]

Holidays = ""
i = 1
for item in today_holidays_days:
    Holidays = Holidays + str(i) + "]" + item + ", "
    i += 1

while True:
    try:
        api.update_status("Today's opportunities to celebrate include: " + Holidays)
        print("Successful Twitter status update")
    except:
        pass
    print("Starting new hour")
    time.sleep(3600)
