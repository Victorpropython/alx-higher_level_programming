#!/usr/bin/python3
""" To access a private instance size"""


class Square:
    """
    Function to access th private attribute class square
    :size: the attribute to be accessed privately and it can be 
    updated, retrieve and validates.
    """


    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
