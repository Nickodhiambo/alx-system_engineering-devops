#!/usr/bin/python3
"""Querries a reddit API"""

import requests


def top_ten(subreddit):
    """Retrieves the top 10 posts from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom user agent
    headers = {'User-Agent': 'My Custom User Agent 1.0'}
    # Send a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for n in range(10):
                print(children[n].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
