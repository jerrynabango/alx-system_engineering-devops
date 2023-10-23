#!/usr/bin/python3
"""
Gather data from an API
"""

import sys
import requests


def data(uid):
    """
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    Todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in Todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(Todos)))
    [print("\t {}".format(c)) for c in completed]


if __name__ == "__main__":
    data(sys.argv[1])
