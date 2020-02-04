#!/usr/bin/python3
"""
    Export to CSV
"""
import csv
from requests import get
from sys import argv

if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    user = get('{}users/{}'.format(url, argv[1])).json()
    todo = get('{}todos?userId={}'.format(url, argv[1])).json()

    # Export data to CSV
    file_csv = "{}.csv".format(argv[1])
    with open(file_csv, "w") as csvfile:
        f = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        for row in todo:
            if row['userId'] == argv[1]:
                f.writerow([row.get('id'), user['username'], todo['completed'], todo['title']])



