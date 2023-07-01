#!/usr/bin/python3
def safe_print_division(a, b):
    value_div = None
    try:
        value_div = a / b
        return value_div
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(value_div)) \
                if value_div is not None \
                else print("Inside result: None")
