#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -d "user_id=98" -H "Origin: School" -L 0.0.0.0:5000/catch_me
