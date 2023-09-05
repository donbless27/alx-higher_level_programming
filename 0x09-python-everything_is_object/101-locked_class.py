#!/usr/bin/python3
"""Defines a lockedclass"""


class LockedClass:
    """
    Prevent new attributes except it is called 'first_name'
    """

    __slots__ = ["first_name"]
