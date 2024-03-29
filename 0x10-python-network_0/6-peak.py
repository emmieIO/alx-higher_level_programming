#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""

    if list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the middle element is greater than the
            # next element, a peak is likely on the left side
            high = mid
        else:
            # If the middle element is less than
            # or equal to the next element, a peak
            # is likely on the right side
            low = mid + 1

    # At the end of the loop,
    # 'low' and 'high' will converge
    # to the peak element
    return list_of_integers[low]
