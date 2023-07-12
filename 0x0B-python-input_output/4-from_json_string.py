#!/usr/bin/python3
"""contains function that returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
