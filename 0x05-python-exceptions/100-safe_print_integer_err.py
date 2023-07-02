#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        return True
        print("{:d}".format(int(value)))
    except Exception as e:
        return False
        sys.stderr.write("Exception: {}\n".format(e))
