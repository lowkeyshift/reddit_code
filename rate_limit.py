import time
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='LWJFQdtre7sMUw',
                 client_secret='CpLeDHNaUL_AwcUB4-9_v-GIO1M',
                 user_agent='commentExtracterMomo:v0.1.0 (by /u/edwcarra17)',
                 username='edwcarra17', password='EE?!01477410ee')
for k,v in reddit.auth.limits.items():
    try:
        if k == 'reset_timestamp':
            print("{}:{}".format(k,v))
    except:
        raise
