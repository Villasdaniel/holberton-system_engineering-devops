#!/usr/bin/python3
"""  using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username} for i in todos]}, jsonfile)
