#!/usr/bin/python3
# 0. What's my status? #0
from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    text = response.read()
    print('Body response:')
    print('    - type:', type(text))
    print('    - content:', text)
    print('    - utf8 content:', text.decode('utf-8'))
