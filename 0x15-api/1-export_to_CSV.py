#!/usr/bin/python3
"""
Gather data from API and store it in csv file
    API: https://jsonplaceholder.typicode.com/
"""


from requests import get
from sys import argv
from csv import writer


if __name__ == "__main__":
    params = {"userId": argv[1]}
    base_url = "https://jsonplaceholder.typicode.com/"
    user = get(base_url + "users/{}".format(argv[1]))
    user = user.json()
    todos = get(base_url + "todos", params=params)
    todos = todos.json()

    for t in todos:
        id = '"{}"'.format(argv[1])
        user_name = '"{}"'.format(user['username'])
        comp = '"{}"'.format(t['completed'])
        title = '"{}"'.format(t['title'])
        task = [id, user_name, comp, title]
        with open("{}.csv".format(argv[1]), 'a') as f:
            write = writer(f)
            write.writerow(task)
            f.close()
