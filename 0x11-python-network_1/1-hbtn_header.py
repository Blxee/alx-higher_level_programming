#!/usr/bin/python3
""" 1. Response header value #0 """
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as response:
    headers = response.headers
    print(headers['X-Request-Id'])
