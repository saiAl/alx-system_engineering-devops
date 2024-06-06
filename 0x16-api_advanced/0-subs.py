#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
        function that queries the Reddit API for a given subreddit.

        Attributes:
            subreddit (str): The target subreddit.
        Returns:
            returns the number of subscribers on Success
            otherwise return 0.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
            }

    response = requests.get(
            url, headers=headers, allow_redirects=False
            )

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]

    return 0
