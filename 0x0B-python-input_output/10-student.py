#!/usr/bin/python3
"""Function that defines a class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Studenr"""
        self.first_name = first_name
        srlf.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(wle) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
