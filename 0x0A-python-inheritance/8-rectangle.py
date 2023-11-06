#!/usr/bin/python3
"""Defines a class Rectangle that inherites from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle

        Args:
            width (int): the width of the new Rectangle
            height (int): the height of the new Rectangle
        """
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
