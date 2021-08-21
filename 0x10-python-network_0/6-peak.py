#!/usr/bin/python3
"""Implements a peak-finding algorithm"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    pkelt = list_of_integers[mid]
    if pkelt > list_of_integers[mid - 1] and pkelt > list_of_integers[mid + 1]:
        return pkelt
    elif pkelt < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
