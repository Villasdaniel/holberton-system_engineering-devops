#!/usr/bin/python3
"""
Queries external API for user todo task information
"""
import json
import requests
import sys

if __name__ == '__main__':
    user = get('https://jsonplaceholder.typicode.com/users/{:s}'.format(
        argv[1]))
    todo = get('http://jsonplaceholder.typicode.com/todos?userId={:s}'.format(
        argv[1]))
    employee = user.json()
    tasks = todo.json()
    completed = [item['title'] for item in tasks if item['completed']]
    print('Employee {:s} is done with tasks({:d}/{:d}):'.format(
        employee['name'], len(completed), len(tasks)))
    for item in completed:
        print('\t ' + item)
