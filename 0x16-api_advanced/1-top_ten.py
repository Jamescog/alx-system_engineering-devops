#!/usr/bin/python3
"""
contain defination for top_ten(subreddit) function
"""


from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Linux arm; rv:99.0"}
    params = {'limit': '10'}
    response = get(url, headers=headers, params=params)
    if response.status_code == 404:
        print("None")
        return
    children = response.json().get('data').get('children')

    for child in children:
        print(child.get('data').get('title'))
