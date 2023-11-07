#!/usr/bin/python3
"""Count keywords """

import requests


def count_words(subreddit, word_list, after=None):
    """
    Function that queries the Reddit API, parses the title of all hot articles,
    and prints sorted count of given keywords.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    custom = {'User-Agent': 'custom-api/1.0 by MyName'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    response = requests.get(url, params=params, custom=custom,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        title_articles = [post['data']['title']
                          for post in data.get('data', {}).get('children', [])]
        keyword_count = {keyword: 0 for keyword in word_list}

        for title in title_articles:
            words = title.lower().split()
            for keyword in word_list:
                keyword_count[keyword] += words.count(keyword.lower())

        for keyword, count in sorted(keyword_count.items(),
                                     key=lambda x: (-x[1], x[0])):
            if count > 0:
                print(f"{keyword}: {count}")
    else:
        return None
