#!/usr/bin/python3
"""
displays commits made by user from the most recent to oldest of the repository
"""
import requests
from sys import argv

if __name__ == '__main__':
    rs = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = rs.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
