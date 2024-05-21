#!/usr/bin/python3
"""1. Export to CSV"""
import csv
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
    with open(f"{emplyeeId}.csv", 'w', newline='') as file:
        data = csv.writer(
                file, delimiter=',', quoting=csv.QUOTE_ALL
                )
        for task in tasks:
            data.writerow(
                    [str(emplyeeId), str(name),
                        task.get("completed"), task.get("title")]
                    )
