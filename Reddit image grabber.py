import praw
import urllib.request as req
import datetime

reddit = praw.Reddit(client_id='EefyTKRTsjD9Lg',
                     client_secret='sV8ASsVbBfj9zT5JTX8eegBb8sM',
                     username='prawspaceporn',
                     password='password',  # this is not my actual password
                     user_agent='prawspacepornbot')

spaceporn = reddit.subreddit('spaceporn')

# change time_filter to all, day, week etc. to change the parameters
# change limit to however many images you want to download
top_spaceporn = spaceporn.top(time_filter='day',
                              limit=5)

for submission in top_spaceporn:
    if submission.preview['images'][0]['source']['width'] >= 1920 and submission.preview['images'][0]['source']['height'] >= 1080:
        req.urlretrieve(submission.preview['images'][0]['source']['url'],
                        # change 'space-images/' to the name of the directory you want to send the images
                        "Z:\space-images\\" + submission.preview['images'][0]['id'] + " " + str(datetime.datetime.date(datetime.datetime.now())) + ".jpg")
