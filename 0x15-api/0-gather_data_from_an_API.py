#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         params={"id": argv[1]})
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]})
    data = todos.json()
    employee = users.json()
    for u_name in employee:
        EMPLOYEE_NAME = u_name.get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task.get('completed'):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task.get("title"))
        TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in TASK_TITLE:
        print("\t {}".format(i))
