#!/usr/bin/python3
"""Queries a reddit API"""

import requests


def number_of_subscribers(subreddit):
    """ Retrieves total no of subscribers from a subreddit"""
    # Define the endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom user agent header to handle multiple requests error
    headers = {'User-Agent': 'My Custom User Agent 1.0'}
    # Send a GET request to the endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        # Parse the response body as JSON
        data = response.json().get('data', {})
        total_subs = data.get('subscribers', 0)
        return total_subs
    else:
        return 0
