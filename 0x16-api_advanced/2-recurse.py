#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and returns a list containing the titles"""
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'User-agent': 'your bot 0.1'}, params={'after': after})

    if not response:
        return None
    else:
        rr = response.json().get('data').get('children')
        for json_dict in rr:
            hot_list.append(json_dict.get('data').get('title'))
        if response.json().get('data').get('after') is not None:
            after = response.json().get('data').get('after')
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
