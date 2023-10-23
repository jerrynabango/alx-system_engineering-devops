#!/usr/bin/python3
"""
Export to CSV
"""

import sys
import requests


def employee_data(uid):
    """
    extend your Python script to export data in the CSV format.
    """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    todos = requests.get(base + "todos", params={"userId": uid}).json()
    
    with open("{}.csv".format(uid), "w") as w:
        for _ in todos:
            row = '"{}","{}","{}","{}"\n'.format(
                uid, user.get("username"), _.get("completed"), _.get("title"))
            w.write(row)


if __name__ == "__main__":
    employee_data(sys.argv[0])