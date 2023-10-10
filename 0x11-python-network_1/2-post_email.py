#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
