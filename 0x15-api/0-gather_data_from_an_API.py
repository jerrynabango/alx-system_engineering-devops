#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
import sys


def employee_info(uid):
    """
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    base = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base + "users/" + uid).json()
    read_data = requests.get(base + "todos", params={"userId": uid}).json()
    completed = [_.get("title") for _ in read_data if _.get("completed")]
    details = "Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(read_data))
    print("\n\t ".join([details] + completed))


if __name__ == "__main__":
    employee_info(sys.argv[1])
