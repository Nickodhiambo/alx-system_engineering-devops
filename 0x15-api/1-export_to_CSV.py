#!/usr/bin/python3
"""Exports user details to a CSV file"""

from requests import get
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = get(url)
    username = response.json().get("username")

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    todos = response.json()

    # Create a CSV file with user info
    with open("{}.csv".format(user_id), 'w') as f:
        for item in todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, item.get("completed"), item.get("title")))
