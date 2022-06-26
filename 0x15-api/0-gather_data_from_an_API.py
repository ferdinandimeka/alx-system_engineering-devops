#!/usr/bin/python3
"""
using the https://jsonplaceholder.typicode.com/ API with the requests module
"""


import requests
from sys import argv


if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))  # noqa
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))  # noqa
    todos = todos.json()
    user = user.json()
    totalTasks = 0
    completed = 0
    completedList = []

    for item in todos:
        totalTasks += 1
        if item.get('completed') is True:
            completed += 1
            completedList.append(item.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), completed  totalTasks))  # noqa

    for line in completedList:
        print("\t {}".format(line, end=""))
