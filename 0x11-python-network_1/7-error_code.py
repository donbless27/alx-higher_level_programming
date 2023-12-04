#!/usr/bin/python3
"""
Sends a request to the specified URL and
displays the body of the response.
"""
import requests
from sys import argv

def handle_http_error(url):
    """
    Manages urllib.error.HTTPError exceptions and
    prints: Error code: followed by the HTTP status code
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")

def main():
    if len(argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = argv[1]
        handle_http_error(url)

if __name__ == "__main__":
    main()

