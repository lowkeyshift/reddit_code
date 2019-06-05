import time
from datetime import datetime
import praw


import time
from datetime import datetime
import praw

#++++++++++++ Collect Users From Comments ========+++++++
num = 0
with open('reddit_users.txt', 'r') as f:
    author_list = f.readlines()
for users in author_list:
    users = users.replace("\n", "")
    reddit = praw.Reddit(client_id='LWJFQdtre7sMUw',
                     client_secret='CpLeDHNaUL_AwcUB4-9_v-GIO1M',
                     user_agent='commentExtracterMomo:v0.1.0 (by /u/edwcarra17)',
                     username='edwcarra17', password='EE?!01477410ee')

    sub = 'EGirlSafeHaven'
    try:
        if num == 20:
            time.sleep(40)
            num -= 20
            continue
        else:
            reddit.subreddit(sub).contributor.add(users)
            num += 1
            print(num)
            print("{} added to {}".format(users,sub))
            f.close()
            with open("reddit_users.txt", "w") as writeF:
                for line in lines:
                    if line.strip("\n") == users:
                        writeF.write(line)
                        writeF.close()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        for k,v in reddit.auth.limits.items():
            if k == 'reset_timestamp':
                ts = int(v)
                print("Resetting at: " + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        pass
print("All users from reddit_users.txt added.")



#++++++++++++ ADD Users ========+++++++
num = 0
with open('reddit_users.txt', 'r') as f:
    author_list = f.readlines()
for users in author_list:
    users = users.replace("\n", "")
    reddit = praw.Reddit(client_id='LWJFQdtre7sMUw',
                     client_secret='CpLeDHNaUL_AwcUB4-9_v-GIO1M',
                     user_agent='commentExtracterMomo:v0.1.0 (by /u/edwcarra17)',
                     username='edwcarra17', password='EE?!01477410ee')

    sub = 'EGirlSafeHaven'
    try:
        if num == 20:
            time.sleep(40)
            num -= 20
            continue
        else:
            reddit.subreddit(sub).contributor.add(users)
            num += 1
            print(num)
            print("{} added to {}".format(users,sub))
            f.close()
            with open("reddit_users.txt", "w") as writeF:
                for line in lines:
                    if line.strip("\n") == users:
                        writeF.write(line)
                        writeF.close()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        for k,v in reddit.auth.limits.items():
            if k == 'reset_timestamp':
                ts = int(v)
                print("Resetting at: " + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        pass
print("All users from reddit_users.txt added.")
