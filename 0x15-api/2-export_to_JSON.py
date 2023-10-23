#!/usr/bin/python3
"""
Export to JSON
"""

import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    read_data = requests.get(url + "users/{}".format(user_id)).json()
    employee = read_data.get("employee")
    read_data = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{
                "task": do.get("title"),
                "completed": do.get("completed"),
                "employee": employee
            } for do in read_data]}, jsonfile)
