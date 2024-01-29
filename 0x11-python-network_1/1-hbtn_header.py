#!/usr/bin/python3
"""0-hbtn_header.py"""
import sys
import urllib.request


url = sys.argv[1]
reguest = urllib.request.Request(url)
with urllib.request.urlopen(reguest) as response:
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
