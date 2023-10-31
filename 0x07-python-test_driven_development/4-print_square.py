#!/usr/bin/python3
"""Defines a square-printing function"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number
        ValueError: If size is < 0


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
       [print("#", end="") for j in range(size)]
       print("")
