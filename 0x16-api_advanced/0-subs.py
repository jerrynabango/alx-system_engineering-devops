#!/usr/bin/python3
"""Checks number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries reddit API & returns the number of subscribers
    (not active users, total subscribers) for a given subreddit,
    else returns None.
    """
    subscribers = 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    custom = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    req = requests.get(url=url, custom=custom, allow_redirects=False)

    if req.status_code == 200:
        response = req.json()
        subscribers = response['data']['subscribers']
    return subscribers
