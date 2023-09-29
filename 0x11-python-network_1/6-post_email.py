#!/usr/bin/python3
""" 2. POST an email #0 """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    requests.options(url, data=data)
    response = requests.get(url, data)
    text = response.text
    print(text)