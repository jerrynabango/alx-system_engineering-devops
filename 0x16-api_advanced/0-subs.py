#!/usr/bin/python3
"""Checks number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries reddit API & returns the number of subscribers
    (not active users, total subscribers) for a given subreddit,
    else returns None.
    """
    number_subscribers = 0

    custom = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = requests.get(url=url, custom=custom, allow_redirects=False)

    if request.status_code == 200:
        response = request.json()
        number_subscribers = response['data']['subscribers']
    return number_subscribers
