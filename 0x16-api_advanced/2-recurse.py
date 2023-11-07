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

    custom = {'User-Agent': 'custom-api/1.0 by MyName'}
    parameter = {'after': after, 'limit': 100}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, parameter=parameter, custom=custom,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_articles = data.get('data', {}).get('children', [])
        hot_list = [post['data']['title'] for post in hot_articles]

        after = data.get('data', {}).get('after')
        if after:
            hot_list += recurse(subreddit, after)
        return hot_list

    return None
