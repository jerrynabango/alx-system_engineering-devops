#!/usr/bin/python3
"""
Export to CSV.
"""

import requests
import sys


def data(uid):
    """
    Records all tasks that are owned by this employee
    """
    base = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base + "users/" + uid).json()
    read_data = requests.get(base + "todos", params={"userId": uid}).json()
    with open("{}.csv".format(uid), 'w') as w:
        for _ in read_data:
            row = '"{}","{}","{}","{}"\n'.format(
                uid, employee.get("username"), _.get("completed"),
                _.get("title"))
            w.write(row)


if __name__ == "__main__":
    data(sys.argv[1])
