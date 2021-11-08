#!/usr/bin/python3
"""Defines  base geometry class"""


class BaseGeometry:
    """Describes the base geometry"""

    def area(self):
        """Goint to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the parameters"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
