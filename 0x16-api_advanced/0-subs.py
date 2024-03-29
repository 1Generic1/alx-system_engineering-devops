#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: The number of subscribers or 0 if the subreddit is invalid.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}
    response = requests.get(url, headers=headers)
    data = response.json()
    # Extract the number of subscribers
    subscribers_count = data.get("data", {}).get("subscribers", 0)
    return subscribers_count
