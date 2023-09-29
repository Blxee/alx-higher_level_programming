#!/usr/bin/python3
""" 4. What's my status? #1 """
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    text = response.text
    print('Body response:')
    print('\t- type:', type(text))
    print('\t- content:', text)
