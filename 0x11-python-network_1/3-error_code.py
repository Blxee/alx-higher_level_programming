#!/usr/bin/python3
""" 3. Error code #0 """
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            text = response.read()
            print(text.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
