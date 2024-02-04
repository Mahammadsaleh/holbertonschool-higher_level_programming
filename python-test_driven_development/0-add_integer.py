#!/usr/bin/python3
"""Addition func"""


def add_integer(a, b=98):
    """
    adds an integer
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
