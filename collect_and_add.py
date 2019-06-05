import time
from datetime import datetime
import praw
from praw.models import MoreComments

#++++++++++++ Collect Users From Comments ========+++++++

new_sub_name = input("Please enter Subname to submit users & hit Enter: ")
comment_thread_url = input("Enter comment thread url to scrape users from: ")
num = 0

reddit = praw.Reddit(client_id='<your_user_api_client_id>',
                 client_secret='<client_secret_code',
                 user_agent='commentExtracterApp:v0.1.0 (by /u/<reddit_user>)',
                 username='your_username', password='<your_password>')

new_sub = reddit.subreddit(new_sub_name)
submission = reddit.submission(url=comment_thread_url)
author_list = []
time.sleep(5)
submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    author = top_level_comment.author
    if not author:
        continue
    else:
        author_list.append(author)
        print(author)
for users in author_list:
    with open("reddit_users.txt", "a") as file:
        file.write("{}\n".format(users))
file.close()

#++++++++++++ ADD Users ========+++++++

with open('reddit_users.txt', 'r') as f:
    author_list = f.readlines()
for users in author_list:
    users = users.replace("\n", "")
    try:
        if num == 20:
            time.sleep(40)
            num -= 20
            continue
        else:
            reddit.subreddit(new_sub_name).contributor.add(users)
            num += 1
            print(num)
            print("{} added to {}".format(users,new_sub_name))
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        for k,v in reddit.auth.limits.items():
            if k == 'reset_timestamp':
                ts = int(v)
                print("Resetting at: " + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        pass
print("All users from reddit_users.txt added.")
