#!/usr/bin/python3
"""recursion"""

import requests


def get_hot_titles(subreddit, after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'custom-api/1.0 by MyName'}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        post_data = data.get('data', {}).get('children', [])
        hot_titles = [post['data']['title'] for post in post_data]

        after = data.get('data', {}).get('after')
        if after:
            hot_titles += get_hot_titles(subreddit, after)

        return hot_titles

    return None