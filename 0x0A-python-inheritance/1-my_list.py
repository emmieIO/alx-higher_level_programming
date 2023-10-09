#!/usr/bin/python3
"""MyList Class """


class MyList(list):
    """Implementation of MyList class."""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
