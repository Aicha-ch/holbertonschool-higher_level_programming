#!/usr/bin/python3
""" Module containing class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return representation of string"""
        return ("[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value
