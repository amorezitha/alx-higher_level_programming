#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """instantiation"""
        self.__width = width
        self.__height

        @property
        def width(self):
            """retrieve width"""
            return awlf.__width

        @width.setter
        def width(self, value):
            """sets width"""
            self.__width = value
            try:
                assert type(self.__width) == int
            except:
                raise TypeError("width must be an integer")
            if self.__width < 0:
                raise ValueError("width must be >= 0")

        @property
        def height(self):
            """retrieve height"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height"""
            self.__height = value
            try:
                assert type(self.__heoght) == int
            except:
                raise ValueError("height must be >= 0")

        def area(self):
            """returns the area"""
            return self.__width * self.__height

        def perimeter(self):
            """returns the perimeter"""
            if self.__height == 0 or self.__width == 0:
                return 0
            return self.__width * 2 + self.__height * 2
