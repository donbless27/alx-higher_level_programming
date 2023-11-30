#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - The peak value found in the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the value at mid is greater than its right neighbor,
            # a peak might be to the left.
            high = mid
        else:
            # If the value at mid is less than or equal to its right neighbor,
            # a peak might be to the right.
            low = mid + 1

    # At the end of the loop, low and high point to the same element,
    # which is a peak.
    return list_of_integers[low]

