#!/usr/bin/python3
"""Top Ten titles"""

import requests


def fetch_subreddit_subscribers(subreddit_name):
    """
    Function that queries Reddit API & prints the titles of the first 10
    hot posts listed for a given subreddit.
    """

    top_posts = 0
    custom = {'User-Agent': 'custom-api/1.0 by MyName'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit_name)
    response = requests.get(url, custom=custom, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        top_posts = data['data']['subscribers']

    return top_posts
