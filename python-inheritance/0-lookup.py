#!/usr/bin/python3
"""
    This script defines a function that retrieves the list of attributes and methods available in a given object.
"""


def lookup(obj):
    """
    Function to obtain the list of attributes and methods of a specified object.
    """
    return dir(obj)
