#!/usr/bin/python3
"""
    Returns a list containing the titles of all hot articles for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = 'https://www.reddit.com/'
        path = 'r/{}/hot.json?limit=100'.format(subreddit)
        header = {'User-Agent':
                  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)'}
        res = get('{}{}'.format(url, path), headers=header)
        data = res.json().get('data')
        childrens = data.get('children')

        hot_list = []
        for children in childrens:
            hot_list.append(children.get('data')['title'])
            recurse(subreddit, hot_list, data('after'))
        return hot_list

    else:
        res = get('{}{}'.format(url, path), headers=header)
        data = res.json().get('data')
    if subreddit is None:
        return None
