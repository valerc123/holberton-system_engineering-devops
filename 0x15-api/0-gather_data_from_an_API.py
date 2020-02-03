#!/usr/bin/python3

"""
"""

import requests
from sys import argv

if __name__ == "__main__":

    employee_id = argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    employee_name = res.name
    print(res.text)
    print('Name: {}'.format(employee_name))
    #for r in res:
    #    EMPLOYEE_NAME = r.name
    #    print(EMPLOYEE_NAME)
         #   NUMBER_OF_DONE_TASKS
        #print("Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
