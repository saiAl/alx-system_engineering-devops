#!/usr/bin/python3
"""0. Gather data from an API"""
import requests
import sys


def fetch(url=None):
    """fetch a information from endpoint"""
    r = requests.get(url)
    return r.json()


def main():
    """information about employee TODO list progress."""
    emplyeeId = int(sys.argv[1])
    done = 0
    total = 0
    completed = []

    tasks = fetch("https://jsonplaceholder.typicode.com/todos")
    user = fetch(f"https://jsonplaceholder.typicode.com/users/{emplyeeId}")

    name = user.get("name")
    for task in tasks:
        if task.get("userId") == emplyeeId:
            if task.get("completed") is True:
                completed.append(task.get("title"))
                done += 1
            total += 1

    print(f"Employee {name} is done with tasks({done}/{total}):")
    for x in completed:
        print(f"\t {x}")


if __name__ == "__main__":
    main()
