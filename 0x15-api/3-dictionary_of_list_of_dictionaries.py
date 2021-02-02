#!/usr/bin/python3
""" script to export data in the JSON format."""
import json
import requests


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    with open("todo_all_employees.json", "w") as jsonfile:
        for user in users:
            for task in requests.get(
                    'https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(str(user.get('id')))).json():
                json.dump({
                    user.get("id"): [{
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username")
                    }]}, jsonfile)
