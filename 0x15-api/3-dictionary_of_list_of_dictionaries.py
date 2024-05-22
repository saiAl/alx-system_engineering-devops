#!/usr/bin/python3
"""2. Export to JSON"""
import json
import requests


if __name__ == "__main__":
    def fetch(url=None):
        """fetch a information from endpoint"""
        r = requests.get(url)
        return r.json()

    tasks = fetch(
            f"https://jsonplaceholder.typicode.com/todos/"
            )
    users = fetch(
            f"https://jsonplaceholder.typicode.com/users/"
            )

    new_dict = {}
    new = []
    """
    seq = [ user['id'] for user in users ]
    new_dict = dict.fromkeys(tuple(seq), None)
    for key, value in new_dict.items():
        for task in tasks:
            if key == task["userId"]:
                print(task)
        print(key, value)
    """
    new = []
    for user in users:
        for task in tasks:
            if user['id'] == task['userId']:
                new.append(
                        {
                            "username": user["username"],
                            "task": task["title"],
                            "completed": task["completed"]
                            }
                        )

        new_dict.update({user["id"]: new})
        new = []

    with open("todo_all_employees.json", 'w') as file:
        json.dump(new_dict, file)
