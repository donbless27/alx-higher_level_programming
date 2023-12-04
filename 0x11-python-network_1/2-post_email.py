#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter
"""
import urllib.request
import urllib.parse
from sys import argv

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: {} <url> <email>".format(argv[0]))
    else:
        url = argv[1]
        email = argv[2]
        send_post_request(url, email)

