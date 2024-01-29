#!/usr/bin/python3
"""2-post_email.py"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, email)
    print(response.text)
