#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed and displays the body of the response
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
