#!/usr/bin/python3
"""Square Class."""

class Square:
     """main square class."""
    def __init__(self, size=0):
        """init constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of square"""
        return (self.__size * self.__size)
