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
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers
            subscribers_count = data['data']['subscribers']
            return subscribers_count
        elif response.status_code == 404:
            return 0
        else:
            print(f"An error occurred: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
