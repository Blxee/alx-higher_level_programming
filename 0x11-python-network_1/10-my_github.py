#!/usr/bin/python3
""" 9. My GitHub! """
import requests
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    url = f'https://api.github.com/user'
    response = requests.get(url, auth=(usr, pwd))
    data = response.json()
    print(data.get('id'))
