#!/usr/bin/python3
"""Exports all data to json format"""

from json import dump
from requests import get

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    user_info = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos'
        response = get(url)
        todos = response.json()
        user_info[user_id] = []
        for item in todos:
            user_info[user_id].append({
                                        "username": username,
                                        "task": item.get('title'),
                                        "completed": item.get('completed'),
                                        })
    with open('todo_all_employees.json', 'w') as f:
        dump(user_info, f)
