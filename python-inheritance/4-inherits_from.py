#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """chack if the object is an instance"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
