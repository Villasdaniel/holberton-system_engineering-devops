#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         params={"id": argv[1]}).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]}).json()
    for u_name in users:
        USERNAME = u_name.get('name')
        USER_ID = u_name.get('id')
    with open('{:s}.csv'.format(argv[1]), mode='w') as f:
        csv = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos:
            TASK_STATUS = tasks.get("completed")
            TASK_TITLE = tasks.get("title")
            csv.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
