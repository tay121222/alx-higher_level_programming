#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: {} is not an integer".format(value), file=sys.stderr)
        return False
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
