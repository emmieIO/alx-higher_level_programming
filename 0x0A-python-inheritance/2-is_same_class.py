#!/usr/bin/python3
"""Program to check instance"""

def is_same_class(obj, a_class):
    """Check if is instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
