#!/usr/bin/python3
"""
Records all tasks from all employees
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "employees").json()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump({
            a.get("id"): [{
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": a.get("username")
            } for a in requests.get(url + "todos",
                                    params={"userId": a.get("id")}).json()]
            for a in employees}, jsonfile)
