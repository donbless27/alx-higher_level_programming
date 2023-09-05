#!/usr/bin/python3
"""Print My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    Check if  (<first name> <last name>)are strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    #Print name
    print(f"My name is {first_name} {last_name}")
