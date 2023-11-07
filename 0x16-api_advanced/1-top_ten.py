#!/usr/bin/python3
"""Top Ten titles"""

import requests


def top_ten(subreddit):
    """
    Function that queries Reddit API & prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    headers = {'User-Agent': 'advanced-api/0.0.1 by User'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    request = requests.get(url=url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        response = request.json()
        titles = [child['data']['title']
                  for child in response['data']['children'][:10]]
        for title in titles:
            print(title)
    else:
        print(None)
