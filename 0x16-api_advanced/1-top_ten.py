#!/usr/bin/python3
"""
    Prints the titles of the first 10 hot posts
"""
from requests import get


def top_ten(subreddit):
    url = 'https://www.reddit.com/'
    path = 'r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent':
              'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'}
    res = get('{}{}'.format(url, path), headers=header)

    if res.status_code == 200:
        data = res.json().get('data')
        child = data.get('children')
        for title in child:
            print(title.get('data').get('title'))
    else:
        print('None')
