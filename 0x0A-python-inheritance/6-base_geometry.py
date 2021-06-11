#!/usr/bin/python3
"""
implementation of the BaseGeometry class
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when invoked"""
        raise Exception("area() is not implemented")
