#!/usr/bin/python3
"""Exports data in json format"""

from json import dump
from requests import get
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    todos = response.json()
    todos_info = {user_id: []}

    for item in todos:
        todos_info[user_id].append({
                                    "task": item.get('title'),
                                    "completed": item.get('completed'),
                                    "username": username,
                                    })
    with open("{}.json".format(user_id), 'w') as f:
        dump(todos_info, f)
