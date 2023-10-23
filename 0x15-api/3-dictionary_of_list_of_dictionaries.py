#!/usr/bin/python3
"""
Records all tasks from all employees
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "employees").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            all.get("id"): [{
                "task": e.get("title"),
                "completed": e.get("completed"),
                "username": all.get("username")
            } for e in requests.get(url + "todos",
                                    params={"userId": all.get("id")}).json()]
            for all in employees}, jsonfile)
