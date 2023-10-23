#!/usr/bin/python3
"""Gathers dummy data from 'https://jsonplaceholder.typicode.com/' API
"""

import requests
import sys

if __name__ == "__main__":
    # Define root url for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Send a GET request to the /users endpoint
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Send a GET request to the /todos endpoint
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter a user's todos by completed tasks
    completed = [i.get("title") for i in todos if i.get("completed") is True]

    # Print employees name and todo list progress
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the titles of completed tasks with tabulation and space
    [print("\t {}".format(i)) for i in completed]
