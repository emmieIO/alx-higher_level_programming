#!/usr/bin/python3
"""0-hbtn_status.py """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
reguest = urllib.request.Request(url)
with urllib.request.urlopen(reguest) as response:
    x_request_id = response.headers.get()
    print(x_request_id)