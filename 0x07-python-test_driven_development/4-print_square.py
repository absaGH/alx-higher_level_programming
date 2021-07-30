#!/usr/bin/python3

"""Defines a function that prints a square pattern"""


def print_square(size):
    """Prints out a square pattern with # character

    Args:
        size (int): The dimension of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
