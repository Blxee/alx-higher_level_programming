#!/usr/bin/python3
""" 8. Search API """
import requests
from sys import argv
import json

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) >= 2 else ''
    data = {'q': letter}
    response = requests.get(url, data=data)
    try:
        dict = json.loads(response.text)
        if len(dict) == 0:
            print('No result')
        else:
            id, name = dict.get('id'), dict.get('name')
            print(f'[{id}] {name}')
    except json.JSONDecodeError:
        print('Not a valid JSON')
