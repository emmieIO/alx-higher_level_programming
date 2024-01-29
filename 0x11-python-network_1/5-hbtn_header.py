#!/usr/bin/python3
"""Starting out with request module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    x = requests.get(url)
    print(x.headers.get('X-Request-Id'))
