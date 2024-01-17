#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    :param subreddit: The name of the subreddit.
    :param word_list: A list of keywords to count.
    :param after: The 'after' parameter for pagination (default is None).
    :param word_counts: A dictionary to store word counts (default is None).
    :return: No return value. Results are printed.
    """
    if word_counts is None:
        word_counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0\
            (by /u/firdaus_cartoon_jr)'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if keyword_lower in title:
                        word_counts[keyword_lower] = word_counts.\
                                get(keyword_lower, 0) + 1
            next_after = data['data']['after']
            if next_after:
                count_words(subreddit, word_list,
                            after=next_after, word_counts=word_counts)
            else:
                print_results(word_counts)
        else:
            print("No posts match or the subreddit is invalid.")

    except requests.exceptions.HTTPError:
        return None


def print_results(word_counts):
    """
    Print the sorted count of keywords.

    :param word_counts: A dictionary containing keyword counts.
    :return: No return value. Results are printed.
    """
    sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")
