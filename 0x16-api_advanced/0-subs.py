#!/usr/bin/python3
"""Checks number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the funcrtion returns None./
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    custom = {'User-Agent': 'custom-agent/1.0 by MyName'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, custom=custom)

    if response.status_code == 200:
        data = response.json()
        check_subscribers = data.get('data', {}).get('check_subscribers', 0)
        return check_subscribers

    return 0
