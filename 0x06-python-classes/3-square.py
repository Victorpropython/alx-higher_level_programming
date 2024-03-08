#!/usr/bin/python3
""" To return current Square area"""


class Square:
    """
    Function to calculate the area of a square
    using a private class attribute
    :size: is the private class attribute
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
