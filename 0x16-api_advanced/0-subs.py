#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit), headers={'User-agent': 'hola'})
    if not response:
        return 0
    return(response.json().get('data').get('subscribers'))
