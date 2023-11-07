#!/usr/bin/python3
"""Count keywords """

import requests


def count_words(subreddit, word_list, after=None, sort=True):
    """
    Function that queries the Reddit API, parses the title of all hot articles,
    and prints sorted count of given keywords.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    custom = {'User-Agent': 'advanced-api/0.0.1 by MyName'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    parameter = {'after': after, 'limit': 100}
    response = requests.get(url=url, parameter=parameter,
                            custom=custom, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        title_articles = [child['data']['title']
                          for child in response['data']['children']]
        after = response['data']['after']
        if after is not None:
            title_articles += count_words(subreddit,
                                          word_list, after=after, sort=False)
        if sort is True:
            count = {key.lower(): 0 for key in word_list}
            for title in title_articles:
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
            return title_articles
