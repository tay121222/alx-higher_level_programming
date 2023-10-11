#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        response_content = response.read().decode('utf-8')
        print(response_content)
