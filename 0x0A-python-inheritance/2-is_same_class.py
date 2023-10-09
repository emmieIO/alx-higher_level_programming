#!/usr/bin/python3
"""Program to check instance"""


def is_same_class(obj, a_class):
    """Check if is instance of class
    

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
