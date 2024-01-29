#!/usr/bin/python3
"""0-hbtn_header.py"""
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({
    "email" : email
}).encode("utf-8")
reguest = urllib.request.Request(url, data)
with urllib.request.urlopen(reguest) as response:
    x_request_id = (dict(response.headers).get("X-Request-Id"))
    print(x_request_id)
