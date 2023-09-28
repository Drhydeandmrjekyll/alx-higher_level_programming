#!/usr/bin/python3
"""
Module defines function find_peak that finds peak in list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find peak in list of unsorted integers.

    Args:
        list_of_integers (list): The list of integers to search for peak.

    Returns:
        int or None: The peak integer if found, None if list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
