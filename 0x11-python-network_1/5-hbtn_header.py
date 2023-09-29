#!/usr/bin/python3
""" 5. Response header value #1 """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    headers = response.headers
    print(headers.get('X-Request-Id'))
