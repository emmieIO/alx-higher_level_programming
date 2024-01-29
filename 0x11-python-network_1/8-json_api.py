#!/usr/bin/python3
"""2-post_email.py"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    url_param = "" if len(sys.argv) == 1 else sys.argv[1]
    param = {'q': url_param }
    r= requests.get(url,param)
    
    try:
       res = r.json()
       if res == {}:
           print("No result")
       else:
           print("[{<id>}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
