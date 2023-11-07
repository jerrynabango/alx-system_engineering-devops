#!/usr/bin/python3
"""recursion"""

import requests

after = None


def recurse(subreddit, hot_list=[]):
    """Function that queries the Reddit API &
    returns a list containing the titles of all hot
    articles for a given subreddit, else return None.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        list = results.json().get("data").get("after")
        if list is not None:
            after = list
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
