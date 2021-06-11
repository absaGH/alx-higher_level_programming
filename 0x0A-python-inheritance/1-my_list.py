#!/usr/bin/python3
"""implementation of MyList class"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """display a list in sorted ascending order"""
        print(sorted(self))
