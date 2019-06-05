import time
import praw
from praw.models import MoreComments


reddit = praw.Reddit(client_id='LWJFQdtre7sMUw',
                     client_secret='CpLeDHNaUL_AwcUB4-9_v-GIO1M',
                     user_agent='commentExtracterMomo:v0.1.0 (by /u/edwcarra17)',
                     username='edwcarra17', password='EE?!01477410ee')

sub = "MomokunButWithoutWK"
uniq_comment = "bpdt2m/temporary_return_comment_now/"
new_sub = reddit.subreddit('EGirlSafeHaven')
submission = reddit.submission(url='https://www.reddit.com/r/'+sub+'/comments/'+uniq_comment)
author_list = []
time.sleep(5)
submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
   #if isinstance(top_level_comment, MoreComments):
    #    continue
    author = top_level_comment.author
    if not author:
        continue
    else:
        author_list.append(author)
        print(author)
#for users in author_list:
   #    print(author_list)
#    time.sleep(5)
#    new_sub.contributor.add(users)
#print("All users from"+sub)
for users in author_list:
    with open("reddit_users.txt", "a") as file:
        file.write("{}\n".format(users))
