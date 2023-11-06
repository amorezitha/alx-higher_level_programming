#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add attribute(obj, att, value):
    """Add a new attribute to an object if possible"""

    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
