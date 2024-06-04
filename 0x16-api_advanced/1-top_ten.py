#!/usr/bin/python3
""" 1. Top Ten """
import requests


def top_ten(subreddit):
    """
        function that queries the Reddit API and prints
        the titles of the first 10 hot posts listed for a given subreddit.

        Attributes:
            subreddit (str): The target subreddit
    """

    if not isinstance(subreddit, str):
        print("None")
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(
                url, headers=headers, allow_redirects=False
                )
        try:
            for x in response.json()["data"]["children"]:
                print(x["data"]["title"])
        except Exception as e:
            print("None")
