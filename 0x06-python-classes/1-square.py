#!/usr/bin/python3

class Square:
    """
    A class representing a square with a given size.

    Attributes:
        __size (int): The size of the square, which is a private attribute.

    Methods:
        __init__(self, size):
            Initializes a new Square object with the specified size.

    """

    def __init__(self, size):
        """
        Initializes a new Square object with the specified size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
