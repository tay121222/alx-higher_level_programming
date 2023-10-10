#!/usr/bin/python3
"""Python script that takes in a URL, sends a request"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
