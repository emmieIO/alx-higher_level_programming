#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class."""


class LockedClass:
    """
    Prevens the instantiation of new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
