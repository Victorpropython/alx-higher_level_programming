#!/usr/bin/python3
""" To define a square """


class Square:
    """
    Function to define a size
    :size: a private instance attribute of class square
    and instantiation with size (no value/type verification)
    """

    def __init__(self, size):
        self.__size = size
