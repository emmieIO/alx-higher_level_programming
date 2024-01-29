#!/usr/bin/python3
"""Starting out with request module"""
import requests


if __name__ == "__main__":
    x = requests.get('https://alx-intranet.hbtn.io/status')
    body = x.text
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", x.text)
