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

    midpt = int(size / 2)
    peakelt = list_of_integers[midpt]
    if peakelt > list_of_integers[midpt - 1] and peakelt > list_of_integers[midpt + 1]:
        return peakelt
    elif peakelt < list_of_integers[midpt - 1]:
        return find_peak(list_of_integers[:midpt])
    else:
        return find_peak(list_of_integers[midpt + 1:])
