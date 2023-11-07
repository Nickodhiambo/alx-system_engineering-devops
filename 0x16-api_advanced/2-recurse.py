#!/usr/bin/python3
"""
Contains a function that recursively calls a reddit API,
retrieving all hot posts to a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of all hot posts on a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # set up appropriate headers
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    # set up params
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    # Send a GET request to API and store response
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None
    # Extract part of the response
    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for item in results.get('children'):
        hot_list.append(item.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
