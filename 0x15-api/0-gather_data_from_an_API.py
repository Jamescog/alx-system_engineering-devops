#!/usr/bin/python3
"""
Gather data from an API
        API - https://jsonplaceholder.typicode.com/
"""


from requests import get
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = get(base_url + "users/{}".format(argv[1]))
    user = user.json()
    parmas = {"userId": argv[1]}
    todos = get(base_url + "todos", params=parmas).json()

    tasks = [t['title'] for t in todos if t['completed']]
    print("Employee {} is done with tasks ({}/{}):".format(
        user['name'], len(tasks), len(todos)
    ))
    for task in tasks:
        print("\t{}".format(task))
