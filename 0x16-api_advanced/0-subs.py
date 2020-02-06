#!/usr/bin/python3

import requests

"""
    Request that return the number of subscribers
"""


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/'
    path = 'r/{}/about.json'.format(subreddit)
    header = {'User-Agent':
              'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'}
    res = requests.get('{}{}'.format(url, path), headers=header)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
