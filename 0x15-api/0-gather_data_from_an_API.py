#!/usr/bin/python3
"""
    Consume data from an api
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = get('{}users/{}'.format(url, employee_id)).json()
    employee_name = user['name']
    todo = get('{}todos/'.format(url)).json()
    total_task = len(todo)
    task_complete = get('{}todos?userId={}&&completed=true'
                        .format(url, employee_id)).json()
    num_task_done = len(task_complete)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_task_done, total_task))

    for t in task_complete:
        print('\t {}'.format(t['title']))
