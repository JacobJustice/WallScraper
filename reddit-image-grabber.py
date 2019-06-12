#!/usr/local/bin/python3

import praw
import urllib.request as req
import datetime

# configure here
bot_username = "username"
image_directory = "path"
subreddit = 'subreddit'

reddit = praw.Reddit(client_id='fake_client_id',
                     client_secret='fake_client_secret',
                     username=bot_username,
                     password='fake_password',  # this is not my actual password
                     user_agent='fake_bot_name')

reddit_obj = reddit.subreddit(subreddit)

# change time_filter to all, day, week etc. to change the parameters
# change limit to however many images you want to download
top_submissions = reddit_obj.top(time_filter='day',
                              limit=5)

for submission in top_submissions:
    if submission.preview['images'][0]['source']['width'] >= 1920 and submission.preview['images'][0]['source']['height'] >= 1080:
        req.urlretrieve(submission.preview['images'][0]['source']['url'],
                        image_directory + submission.preview['images'][0]['id'] + "_" + str(datetime.datetime.date(datetime.datetime.now())) + ".jpg")
