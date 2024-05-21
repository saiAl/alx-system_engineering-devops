#!/usr/bin/python3
"""1. Export to CSV"""
import json
import requests
import sys


if __name__ == "__main__":
    def fetch(url=None):
        """fetch a information from endpoint"""
        r = requests.get(url)
        return r.json()

    emplyeeId = int(sys.argv[1])
    tasks = fetch(
            f"https://jsonplaceholder.typicode.com/users/{emplyeeId}/todos"
            )
    user = fetch(
            f"https://jsonplaceholder.typicode.com/users/{emplyeeId}"
            )

    name = user.get("name").split(' ')[0]
    with open(f"{emplyeeId}.json", 'w') as file:
        data = {
                emplyeeId: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username")
                        }
                    for task in tasks
                    ]
                }
        json.dump(data, file)
