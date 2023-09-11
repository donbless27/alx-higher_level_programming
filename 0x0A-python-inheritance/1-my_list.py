#!/usr/bin/python3
"""Defines an subclass or child list class MyList."""


class MyList(list):
    """A subclass of the list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
