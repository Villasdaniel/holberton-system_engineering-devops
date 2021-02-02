#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()
    user_name = users.get("username")
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": user_name} for i in todos]}, jsonfile)
