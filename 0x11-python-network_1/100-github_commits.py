#!/usr/bin/python3
""" 10. Time for an interview! """
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url).text
    import json
    data = json.loads(response)
    for commit in data[:10]:
        print(commit.get('sha'),
              commit.get('commit').get('author').get('name'),
              sep=': ')
