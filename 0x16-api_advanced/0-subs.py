#!/usr/bin/python3
"""Checks number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the funcrtion returns None./
    """
    subscribers_count = 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    req = requests.get(url=url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        subscribers_count = response['data']['subscribers_count']
    return subscribers_count
