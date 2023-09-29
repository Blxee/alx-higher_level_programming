#!/usr/bin/python3
# 0. What's my status? #0
from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    text = response.read()
    print('Body response:')
    print('\t- type:', type(text))
    print('\t- content:', text)
    print('\t- utf8 content:', text.decode('utf-8'))
