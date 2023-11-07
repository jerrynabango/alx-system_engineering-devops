#!/usr/bin/python3
"""Top Ten titles"""

from requests import get


def top_ten(subreddit):
    """
    Function that queries Reddit API & prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    parameter = {'limit': 10}

    response = get(url, headers=headers, parameter=parameter)
    results = response.json()

    try:
        list = results.get('data').get('children')

        for title in list:
            print(title.get('data').get('title'))

    except Exception:
        print("None")
