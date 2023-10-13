#!/usr/bin/python3
"""Define a class representing a rectangle"""

class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - width (int): represent the width of the rectangle.
    - height (int): represent the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializing the rectangle with the given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting rectangle's width.

        Parameters:
        - value (int): The width value to be set.

        Raises:
        - TypeError: If the width is not an integer.
        - ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
        - value (int): The height value to be set.

        Raises:
        - TypeError: If the height is not an integer.
        - ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        else:
            self.__height = value

