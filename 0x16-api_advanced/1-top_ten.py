#!/usr/bin/python3
"""module which contains a function to bring information of Reddit API"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and
    returns the titles of the first hot posts of a given subreddit
    """
    response = requests.get('https://reddit.com/r/{}/hot.json\
?limit=10'.format(subreddit), headers={'User-agent': 'botardo'})
    dataList = response.json().get('data').get('children\
') if response.status_code != 404 else None
    if dataList is None:
        return print("None")
    i = 0
    if len(response.json().get('data').get('children')) == 0:
        return print("None")
    for item in dataList:
        print(item.get('data').get('title'))
