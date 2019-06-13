#!/usr/local/bin/python3 import praw import urllib.request as req import datetime

# configure here
bot_username = "fakeUsername"
image_directory = "fake/path"
subreddits = ['spaceporn', 'cabinporn'] #list subreddits here
time_period = 'day' # day, week, month
max_images = 50
min_width = 1920
min_height = 1080


reddit = praw.Reddit(client_id='fakeClientID',
     client_secret='fakeClientSecret',
     username=bot_username,
     password='fakePass',  # this is not my actual password
     user_agent='botName')


for subreddit in subreddits:
    reddit_obj = reddit.subreddit(subreddit)

    # change time_filter to all, day, week etc. to change the parameters
    # change limit to however many images you want to download
    top_submissions = reddit_obj.top(time_filter=time_period,
                                  limit=max_images)

    for submission in top_submissions:
        if submission.preview['images'][0]['source']['width'] >= min_width and submission.preview['images'][0]['source']['height'] >= min_height:
            req.urlretrieve(submission.preview['images'][0]['source']['url'],
                            image_directory + "/" + submission.preview['images'][0]['id'] + "_" + str(datetime.datetime.date(datetime.datetime.now())) + ".jpg")
