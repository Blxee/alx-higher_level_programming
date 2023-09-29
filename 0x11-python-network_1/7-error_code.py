#!/usr/bin/python3
""" 7. Error code #1 """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response.status_code // 100 <= 3:
        print(response.text)
    else:
        print('Error code:', response.status_code)
