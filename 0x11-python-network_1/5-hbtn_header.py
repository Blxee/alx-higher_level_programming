#!/usr/bin/python3
""" 5. Response header value #1 """
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
