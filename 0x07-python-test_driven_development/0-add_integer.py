#!/usr/bin/python3
"""This is an example, please disragard"""

def add_integer(a, b=98):
    # Check if a and b are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    # Perform the addition and return the result
    result = a + b
    return result

