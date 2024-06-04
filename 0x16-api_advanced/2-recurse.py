#!/usr/bin/python3
""" 2. Recurse it! """
count = 0


def recurse(subreddit, hot_list=[], after=None):
    """
        recursive function that queries the Reddit API
        and returns a list containing the titles
        of all hot articles for a given subreddit
    """
    import requests
    global count

    if not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    response = requests.get(
            url, headers=headers,
            allow_redirects=False, params=params
            )

    data = response.json()['data']
    children = data['children']
    after = data["after"]

    if after:
        try:
            hot_list.append(children[count]['data']['title'])
        except Exception as e:
            return hot_list
        count += 1
        return recurse(subreddit, hot_list, after)
