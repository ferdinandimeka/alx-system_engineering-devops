#!/usr/bin/python3
"""script to have employee information and work status list"""

import requests
from sys import argv


def todo(userid):
    """doc stringed"""
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            userid)).json().get('name')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            userid)).json()
    tasksDone = ['\t {}\n'.format(dic.get('title')) for dic in tasks
                 if dic.get('completed')]
    if name and tasks:
        print("Employee {} is done with tasks({}/{}):".format
              (name, len(tasksDone), len(tasks)))
        print(''.join(tasksDone), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))

        # Using params I can filter 🎯
        # emplo = requests.get('https://jsonplaceholder.typicode.com/users',
        #                         params={'id':  user_id})
        # tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
        #                      params={'userId':  user_id})
