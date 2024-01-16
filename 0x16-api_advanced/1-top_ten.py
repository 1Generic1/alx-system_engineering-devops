#!/usr/bin/python3
"""
this script prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: No
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children'][:10]:
                post_title = post['data']['title']
                print(post_title)
        else:
            print(None)
    except Exception as e:
        print(f"An error occurred: {e}")
