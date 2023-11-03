#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_ok = {'email': email}
    response = requests.post(url, data=data_ok)
    print(response.text)
