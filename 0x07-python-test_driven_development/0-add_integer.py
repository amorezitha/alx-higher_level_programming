#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integee addition of a and b

    Float arguments are typecasted to ints before addition is performed

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer/float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer"))
    return (int(a) + int(b))
