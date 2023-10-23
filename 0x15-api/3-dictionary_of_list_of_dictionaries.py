#!/usr/bin/python3
"""
Records all tasks from all employees
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees_tasks = requests.get(url + "employees_tasks").json()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(
            {
                all_tasks.get("id"): [
                    {
                        "task": records.get("title"),
                        "completed": records.get("completed"),
                        "username": all_tasks.get("username")
                    }
                    for records in requests.get(
                        url + "todos",
                        params={"userId": all_tasks.get("id")}
                    ).json()
                ]
                for all_tasks in employees_tasks
            },
            jsonfile
        )
