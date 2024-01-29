#!/usr/bin/python3
"""0-hbtn_status.py """
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode('utf-8'))
