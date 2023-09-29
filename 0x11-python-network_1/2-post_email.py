#!/usr/bin/python3
""" 1. Response header value #0 """
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    data = parse.urlencode(data)
    data = data.encode('utf-8')
    with request.urlopen(url, data) as response:
        text = response.read()
        print(text)
