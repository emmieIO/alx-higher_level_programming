#!/usr/bin/python3
"""Define Read file function"""


def read_file(filename="", encoding="utf-8"):
    """Representation of read file function"""
    with open(filename, 'r') as f:
        data = f.read()
        print(data, end="");
