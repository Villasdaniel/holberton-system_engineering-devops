#!/usr/bin/python3
"""  using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(str(argv[1]))).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos', params={
                         'userId': argv[1]}).json()
    username = users.get("username")
    with open("{}.json".format(argv[1]), "w") as jsonfile:
        for i in todos:
            json.dump({argv[1]: [{
                    "task": i.get("title"),
                    "completed": i.get("completed"),
                    "username": username}]}, jsonfile)
