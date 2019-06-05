# Install Python3 and pip3

(Installing Pytho3)[https://realpython.com/installing-python/]
Installing Pip3:
- (Windows)[https://www.liquidweb.com/kb/install-pip-windows/]
- Mac: `brew install python3` Comes with `pip3` installed.

# Install PRAW

Documentation: (PRAW python Reddit API Wrapper)[https://praw.readthedocs.io/en/v3.6.0/index.html?highlight=install#installation]

Pip Install: `pip3 install praw`

# Create Reddit OAUTH account

> This is used to updated this section from the code (lines 12-15). (Reddit OAUTH)[https://github.com/reddit-archive/reddit/wiki/oauth2]

Please update this section in the file `collect_and_add.py`.
> reddit = praw.Reddit(client_id='<your_user_api_client_id>',
                 client_secret='<client_secret_code',
                 user_agent='commentExtracterApp:v0.1.0 (by /u/<reddit_user>)',
                 username='your_username', password='<your_password>')


# Run script by running following command:

`python3 collect_and_add.py`

Then answer the questions that are asked.

Examples:
- Enter the /r/sub_name without the "/r/"
`Please enter Subname to submit users & hit Enter: OldSchoolCool`
- Enter full url of sub you want to add users to
`Enter comment thread url to scrape users from: https://www.reddit.com/r/AskReddit/`

Please contact me on reddit u/edwcarr17 if you have any questions.
