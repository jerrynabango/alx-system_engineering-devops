#!/usr/bin/python3
"""recursion"""

import requests

after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    global after
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = results.json().get("data").get("children")
        for title_ in titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
