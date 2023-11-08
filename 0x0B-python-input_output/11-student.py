#!/usr/bin/python3
"""Function that defines a class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Grts a dictionary representation of a Student.
        If attrs is a list of strings, represent only those attribute
        included on the list"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) gor k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""
        for k, v in json.items():
            serattr(self, k, v)
