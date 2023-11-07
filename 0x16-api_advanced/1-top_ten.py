#!/usr/bin/python3
"""Top Ten tiles"""

import requests


def fetch_subreddit_subscribers(subreddit_name):
    """
    Function that queries Reddit API & prints the titles of the first 10
    hot posts listed for a given subreddit.
    """

    subscriber_count = 0
    custom = {'User-Agent': 'custom-api/1.0 by MyName'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit_name)
    response = requests.get(url, custom=custom, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscriber_count = data['data']['subscribers']

    return subscriber_count