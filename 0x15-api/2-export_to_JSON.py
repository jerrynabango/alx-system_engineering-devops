#!/usr/bin/python3
"""
Export to JSON
"""

import json
import requests
import sys


def data_export():
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    read_data = requests.get(url + "users/{}".format(user_id)).json()
    username = read_data.get("username")
    read_data = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{
                "task": do.get("title"),
                "completed": do.get("completed"),
                "username": username
            } for do in read_data]}, jsonfile)


if __name__ == "__main__":
    data_export(sys.arg[1])
