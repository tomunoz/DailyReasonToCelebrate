# Twitter Bot = DailyReasonToCelebrate

import tweepy as tp
import datetime
from datetime import date, datetime
import time
import os
from os import environ
import pandas as pd
import xlrd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

#print("This is a Twitter bot named 'DailyReasonToCelebrate' 1")
# credentials to login to twitter api
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']

ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth, wait_on_rate_limit=True)

# define image to be used and image output files
image_in_file = "CelebrationIMGOriginal.png"
image_out_file = "CelebrationIMGOriginalOutput.png"

# today's date
Date_Today = date.today()
date_reformat = datetime.today().strftime('%Y-%b-%d')

# read the csv file with the holidays (Date, Holiday, Location)
Holidays_df = pd.read_csv("DailyHolidays.csv")

# retrieve only today's holidays
today_holidays_df = Holidays_df.loc[Holidays_df["Date"] == str(Date_Today)]

# iterate through today's holidays and create text string to add to image
text = ""
i = 1
for index, row in today_holidays_df.iterrows(): 
    text = text + str(i) + "]" + row["Holiday"] + " (" + row["Location"] + ")\n"
    i += 1

# create image and add the text to the image
img = Image.open(image_in_file)
draw = ImageDraw.Draw(img)
#font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', size=10)
#this_font = "arial.ttf"
font = ImageFont.truetype(".fonts/arial.ttf", 75)
draw.text((20, 20), text, (0, 0, 0), font=font)
draw.text((20, 1150), str(date_reformat), (0, 0, 0), font=font)
img.save(image_out_file)

# create the image file with text that will be posted to twitter
media = api.media_upload(image_out_file)

# post the image to twitter
while True:
    try:
        api.update_status(status="Today's holidays " + "(" + str(date_reformat) + ") " + "to celebrate and commemorate include: ", media_ids=[media.media_id])
        print("Successful Twitter status update")
    except:
        pass
    print("Waiting for next day")
    time.sleep(86400)

