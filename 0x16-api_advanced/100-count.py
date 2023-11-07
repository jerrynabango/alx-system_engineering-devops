#!/usr/bin/python3
"""Count Keywords"""

import requests


def count_words(subreddit, word_list, after=None, sort=True):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    req = requests.get(url=url,
                       params=params, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        response = req.json()
        titles = [child['data']['title']
                  for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            titles += count_words(subreddit,
                                  word_list, after=after, sort=False)
        if sort is True:
            count = {key.lower(): 0 for key in word_list}
            for title in titles:
                count = {key: value + title.lower().split().count(key)
                         for key, value in count.items()}
            count = {key: value for key, value in count.items() if value > 0}
            if len(count):
                word_list = [w.lower() for w in word_list]
                count = {key: value * word_list.count(key)
                         for key, value in count.items()}
                count = sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))
                [print("{}: {}".format(key, value)) for key, value in count]
        else:
            return titles
