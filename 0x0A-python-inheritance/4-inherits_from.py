#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to
    Returns:
        If obj is an inherited instance of a_class - True
        Otherwise - False
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
