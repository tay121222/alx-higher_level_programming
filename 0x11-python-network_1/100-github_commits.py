#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge
"""
import requests
import sys

if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    if response.status_code == 200:
        for commit in response.json()[:10]:
            print("{}: {}".format(commit['sha'],
                  commit['commit']['author']['name']))
    else:
        print("Error: {}".format(response.status_code))
