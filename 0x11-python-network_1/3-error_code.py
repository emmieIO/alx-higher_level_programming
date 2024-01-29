#!/usr/bin/python3
"""2-post_email.py"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
