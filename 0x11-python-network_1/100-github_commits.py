#!/usr/bin/python3
""" 10. Time for an interview! """
from urllib import request
from sys import argv
import json

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    with request.urlopen(url) as response:
        data = json.load(response)
        for commit in data:
            print(commit.get('sha'),
                  commit.get('commit').get('author').get('name'),
                  sep=': ')
