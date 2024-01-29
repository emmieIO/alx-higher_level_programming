#!/usr/bin/python3
"""2-post_email.py"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print("Error code: ", response.status_code)
