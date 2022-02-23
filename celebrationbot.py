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
import sqlite3
from contextlib import closing


def create_api():
    # credentials to login to twitter api
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    
    # create the api
    auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tp.API(auth, wait_on_rate_limit=True)
    return api


def get_text():
    # connect to the db or create and connect to the db if it does not exist
    connection = sqlite3.connect("holidays.db")
    # create the db table for holidays
    cursor = connection.cursor()
    Date_Today = date.today().strftime('%Y-%m-%d')
    """ Date_Today = date.today().strftime('%-m/%-d/%-y') """
    """ Date_Today = date.today() """
    rows = cursor.execute("SELECT * FROM holidays WHERE date = ?", (Date_Today,)).fetchall()
    text = ""
    i = 1
    for item in rows:
        text = text + str(i) + "] " + item[1] + "\n"
        i += 1
    # close the db connections
    with closing(sqlite3.connect("holidays.db")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
    return text


def get_media(text, api):
    # define image to be used and image output files
    image_in_file = "CelebrationIMGOriginal.png"
    image_out_file = "CelebrationIMGOriginalOutput.png"
    # create image and add the text to the image
    img = Image.open(image_in_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(".fonts/arial.ttf", 75)
    draw.text((20, 20), text, (0, 0, 0), font=font)
    date_reformat = datetime.today().strftime('%Y-%b-%d')
    draw.text((20, 1150), str(date_reformat), (0, 0, 0), font=font)
    img.save(image_out_file)
    # create the image file with text that will be posted to twitter
    media = api.media_upload(image_out_file)
    return media


def main():
    while True:
        api = create_api()
        text = get_text()
        media = get_media(text, api)
        date_reformat = datetime.today().strftime('%Y-%b-%d')
        try:
            # post the image to twitter
            api.update_status(status="Today's holidays " + "(" + str(date_reformat) + ") " + "to celebrate and commemorate include: ", media_ids=[media.media_id])
            print("Successful Twitter status update")
        except:
            pass
        print("Waiting for next day")
        # wait a day
        #time.sleep(31536000)
        break
    exit()



if __name__ == '__main__':
    main()