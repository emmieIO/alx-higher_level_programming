#!/usr/bin/python3
"""0-hbtn_header.py"""
import sys
import urllib.request


url = sys.argv[1]
reguest = urllib.request.Request(url)
with urllib.request.urlopen(reguest) as response:
    print(dict(response.headers).get("X-Request-Id"))
