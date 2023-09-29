#!/usr/bin/python3
""" 10. Time for an interview! """
from urllib import request
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    with request.urlopen(url) as response:
        data = response.readlines()
        print(data)
        for i in range(10):
            sha = data[2 + i * 79][12:-3]
            name = data[6 + i * 79][17:-3]
            print(sha, name, sep=': ')
