#!/usr/bin/python3
"""
this script uses recursive function
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: A list to store the titles of hot articles (default is an empty list).
    :return: A list containing the titles of hot articles or None if no results are found.
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            # Extract titles and add them to the hot_list
            hot_list.extend(post['data']['title'] for post in data['data']['children'])

            # Recursive call with the updated hot_list
            next_after = data['data']['after']
            if next_after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None  # No results found

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
        return None
