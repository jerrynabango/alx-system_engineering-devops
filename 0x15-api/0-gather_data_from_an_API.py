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
    base = "https://jsonplaceholder.typicode.com/"
    read_user = requests.get(base + "users/" + uid).json()
    create = requests.get(base + "create", params={"userId": uid}).json()
    completed = [_.get("title") for _ in create if _.get("completed")]
    result = "Employee {} is done with tasks({}/{}):".format(
        read_user.get("name"), len(completed), len(create))
    print("\n\t ".join([result] + completed))


if __name__ == "__main__":
    data(sys.argv[1])
