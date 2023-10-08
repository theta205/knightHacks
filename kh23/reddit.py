import praw
from dotenv import load_dotenv

def count_mentions_in_subreddit(keyword, subreddit_name):
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_CLIENT_SECRET,
                         user_agent=REDDIT_USER_AGENT)

    subreddit = reddit.subreddit(subreddit_name)

    mentions_count = 0

    for submission in subreddit.search(keyword, sort='new', time_filter='all'):
        title_count = submission.title.lower().count(keyword.lower())
        body_count = submission.selftext.lower().count(keyword.lower())

        mentions_count += title_count + body_count

    return mentions_count
