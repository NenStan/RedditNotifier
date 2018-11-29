import praw
import datetime
import os
reddit = praw.Reddit(client_id='', client_secret="",
                     password='', user_agent='',
                     username='')
for submission in reddit.subreddit("hardwareswap").stream.submissions():
	date = datetime.datetime.fromtimestamp(submission.created_utc)
	if "Ryzen".lower() in submission.title.lower():
		print(submission.title)
		print("\t\t\t" + date.strftime("%I:%M%p") + "\t\t\t")
		print("-----  %s -----\n" % submission.url)
		os.system('say -v Ting-Ting -r 1000 "Boing"')
	else:
		print("\033[37m%s\033[0m" % submission.title)
		print("\t\t\t\t\t\033[37m" + date.strftime("Created At:\t%I:%M%p") + "\033[0m")
		print("\033[92m\t\t\033[4m%s\033[0m\t\t\033[0m\n" % submission.url)
		os.system('say -v Ting-Ting -r 600 "bing"')
