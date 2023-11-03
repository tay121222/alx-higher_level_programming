#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    data_ok = urllib.parse.urlencode(param).encode('utf-8')
    req = urllib.request.Request(url, data=data_ok, method='POST')

    with urllib.request.urlopen(req) as res:
        response_content = res.read().decode('utf-8')
        print(response_content)
