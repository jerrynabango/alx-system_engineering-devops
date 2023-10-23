#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import sys
import requests


def data(uid):
    """
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    todos = requests.get(base + "todos", params={"userId": uid}).json()
    completed = [_.get("title") for _ in todos if _.get("completed")]
    output = "Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos))
    print("\n\t ".join([output] + completed))


if __name__ == "__main__":
    data(sys.argv[1])
