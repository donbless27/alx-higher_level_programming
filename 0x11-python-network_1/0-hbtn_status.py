#!/usr/bin/python3
"""Retrieves the status from https://alx-intranet.hbtn.io."""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Response Body:")
        print("\t- Data Type: {}".format(type(content)))
        print("\t- Content: {}".format(content))
        print("\t- UTF-8 Content: {}".format(content.decode("utf-8")))

