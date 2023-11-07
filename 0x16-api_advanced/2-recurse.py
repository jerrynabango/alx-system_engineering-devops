#!/usr/bin/python3
"""Recursing through the directory tree and collecting all files"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Function that queries the Reddit API & returns  a list containing the title
    of all hot articles for a given subreddit, else returns None.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    headers = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    req = requests.get(url, params=params,
                       headers=headers, allow_redirects=False)

    if req.status_code == 200:
        response = req.json()
        hot_list = [child['data']['title']
                    for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            hot_list += recurse(subreddit, after=after)
        return hot_list
    return None
