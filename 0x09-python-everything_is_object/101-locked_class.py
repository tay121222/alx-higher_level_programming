#!/usr/bin/python3
"""Locked_Class"""


class LockedClass:
    """
    that prevents the user from creating new instance attributes
    """
    __slots__ = ["first_name"]
