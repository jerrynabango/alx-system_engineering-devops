#!/usr/bin/python3
"""Count keywords from articles"""

import requests


def count_words(subreddit, word_list, after=None, sort=True):
    """
    Function that queries the Reddit API, parses the title of all hot articles,
    & prints a sorted articles_count of given keywords.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    parameter = {'after': after, 'limit': 100}
    custom = {'User-Agent': 'advanced-api/0.0.1 by Mendy'}
    respionse = requests.get(url=url, parameter=parameter, custom=custom,
                             allow_redirects=False)
    if respionse.status_code == 200:
        response = respionse.json()
        titles = [child['data']['title']
                  for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            titles += count_words(subreddit,
                                  word_list, after=after, sort=False)
        if sort is True:
            articles_count = {key.lower(): 0 for key in word_list}
            for title in titles:
                articles_count = {key: value + title.lower().split()
                                  .articles_count(key)
                                  for key, value in articles_count.items()}
            articles_count = {key: value for key,
                              value in articles_count.items() if value > 0}
            if len(articles_count):
                word_list = [w.lower() for w in word_list]
                articles_count = {key: value * word_list.articles_count(key)
                                  for key, value in articles_count.items()}
                articles_count = sorted(articles_count.items(),
                                        key=lambda all: (-all[1], all[0]))
                [print("{}: {}".format(key, value))
                 for key, value in articles_count]
        else:
            return titles
