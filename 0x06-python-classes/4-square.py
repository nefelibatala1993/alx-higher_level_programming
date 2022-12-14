#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square Class
    Attributes:
        __size: Size of the square
    """
    def __init__(self, size=0):
        """Initialization Method / Default Constructor
        :param size: Size of the square to be instantiated
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for __size Attribute
        :return: Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size Attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Finds area of the square
        :return: The area of the square
        """
        return self.__size ** 2
