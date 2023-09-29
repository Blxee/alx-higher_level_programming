#!/usr/bin/python3
""" 9. My GitHub! """
import requests
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    url = f'https://api.github.com/users/{usr}'
    headers = {'Authorization': f'{usr} {pwd}'}
    response = requests.get(url, headers=headers).text
    import json
    data = json.loads(response)
    print(data.get('id'))
