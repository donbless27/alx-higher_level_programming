#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
    obj (object): The object to check.
    a_class (class): The class to compare with.

    Returns: True if the object is exactly an instance of the specified class,
    otherwise False.
    """
    return (type(obj) == a_class)
