#!/usr/bin/python3
"""
contains the defination of function(number_of_subscribers)
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    return the number of total subscribers for given
    subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Linux arm; rv:99.0"}
    response = get(url, headers=headers)
    if response.status_code == 200:
        jsonified_response = response.json()
        response_data = jsonified_response['data']
        subscribers = response_data['subscribers']
        return subscribers
    return 0
