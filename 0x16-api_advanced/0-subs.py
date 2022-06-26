#!/usr/bin/python3
"""
contains the number of subscriber function
"""
import requests


def number_of_subscribers(subreddit):

    # returns the number of subscribers for a given subreddit
    if subreddit is None or type(subreddit) is not str:
        return 0
    else:
        r = requests.get(
            "http://www.reddit.com/r/{}/about.json".format(subreddit, end=""),
            headers={
                "User-agent": "Python/requests:APIproject:\v1.0.0 (by /u/aaor\
rico23)"
            },
        ).json()
        subs = r.get("data", {}).get("subscribers", 0)
        return subs
