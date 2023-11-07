#!/usr/bin/python3
"""Count Keywords"""

import requests


def count_words(subreddit, word_list, after='',
                words_dict={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces.
    """
    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)

    response = requests.get("https://www.reddit.com/r/{}/hot.json".
                            format(subreddit),
                            headers={'User-Agent': 'Custom'},
                            parameter={'after': after}, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        response = response.json().get('data', None)
        if response is None:
            return
    except ValueError:
        return

    data = response.get('data', [])

    for count in data:
        title = count.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    after = response.get('after', None)
    if after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for all in sorted_dict:
            if all[1] != 0:
                print("{}: {}".format(all[0], all[1]))
        return

    return count_words(subreddit, word_list,
                       after, words_dict)
