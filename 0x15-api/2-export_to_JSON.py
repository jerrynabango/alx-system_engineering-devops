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
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    Todos = requests.get(url + "todos", params={"userId": user_id}).json()
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{
                "task": do.get("title"),
                "completed": do.get("completed"),
                "username": username
            } for do in Todos]}, jsonfile)
