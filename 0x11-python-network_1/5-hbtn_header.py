#!/usr/bin/python3
"""Starting out with request module"""
import requests
import sys


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    x_req_id = x.headers['X-Request-Id']
    print(x_req_id)
