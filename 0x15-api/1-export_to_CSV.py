#!/usr/bin/python3
"""Export data in the CSV format"""
from csv import writer, QUOTE_ALL
from csv import QUOTE_ALL
from sys import argv
from requests import get


if __name__ == '__main__':
    users = get(
        'https://jsonplaceholder.typicode.com/users/{:s}'
        .format(str(argv[1]))).json()
    todos = get(
        'http://jsonplaceholder.typicode.com/todos?userId={:s}'
        .format(str(argv[1]))).json()
    with open('{:s}.csv'.format(argv[1]), mode='w') as f:
        csv = writer(f, delimiter=',', quotechar='"',
                     quoting=QUOTE_ALL)
        for task in todos:
            csv.writerow([users['id'], users['username'],
                          task['completed'], task['title']])
