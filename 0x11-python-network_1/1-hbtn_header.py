#!/usr/bin/python3
"""Python script that takes in a URL and sends a request"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
