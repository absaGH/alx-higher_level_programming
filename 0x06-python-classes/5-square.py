#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        """
        self.size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
                self.__size = value
    
    def my_print(self):
            """Print the square with the # character"""
            if self.__size == 0:
                print()
                return
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
