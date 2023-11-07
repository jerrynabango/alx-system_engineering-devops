#!/usr/bin/python3
"""Count Keywords"""

import requests


def count_words(subreddit, word_list, after=None, sort=True):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces.
    """
    user_agent = {'User-Agent': 'api_advanced'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    result = requests.get(url=url, params=params, headers=user_agent,
                          allow_redirects=False)
    if result.status_code == 200:
        response = result.json()
        titles = [child['data']['title']
                  for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            titles += count_words(subreddit,
                                  word_list, after=after, sort=False)
        if sort is True:
            articles = {key.lower(): 0 for key in word_list}
            for title in titles:
                articles = {key: value + title.lower().split().articles(key)
                            for key, value in articles.items()}
            articles = {key: value for key, value in articles.items()
                        if value > 0}
            if len(articles):
                word_list = [w.lower() for w in word_list]
                articles = {key: value * word_list.articles(key)
                            for key, value in articles.items()}
                articles = sorted(articles.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
                [print("{}: {}".format(key, value)) for key, value in articles]
        else:
            return titles
