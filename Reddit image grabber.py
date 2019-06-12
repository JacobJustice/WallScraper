#!/usr/local/bin/python3

import praw
import urllib.request as req
import datetime

# configure here
bot_username = "atfumbel"
image_directory = "/users/andrewthorp/Pictures/space/"
subreddit = 'spaceporn'

reddit = praw.Reddit(client_id='5BKiG_ZYwqNIzg',
                     client_secret='VnTkWOOT1TcVVnM92ikmWAYp4HU',
                     username=bot_username,
                     password='Spizzero1',  # this is not my actual password
                     user_agent='bot')

reddit_obj = reddit.subreddit(subreddit)

# change time_filter to all, day, week etc. to change the parameters
# change limit to however many images you want to download
top_submissions = reddit_obj.top(time_filter='day',
                              limit=5)

for submission in top_submissions:
    if submission.preview['images'][0]['source']['width'] >= 1920 and submission.preview['images'][0]['source']['height'] >= 1080:
        req.urlretrieve(submission.preview['images'][0]['source']['url'],
                        image_directory + submission.preview['images'][0]['id'] + "_" + str(datetime.datetime.date(datetime.datetime.now())) + ".jpg")
