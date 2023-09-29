#!/usr/bin/python3
""" 4. What's my status? #1 """
from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        text = response.read().decode('utf-8')
        print('Body response:')
        print('\t- type:', type(text))
        print('\t- content:', text)
