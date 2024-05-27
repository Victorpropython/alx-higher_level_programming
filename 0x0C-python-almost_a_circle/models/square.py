#!/usr/bin/python3
"""A square to inherint from the Rectangle class

    Args:
        size (int): The new Square Size
        x (int): The new Square x coordinate
        y (int): The new Square y coordinate
        id (int): The new Square identity
"""
import os
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """For the Args Above """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get Square size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    @property
    def size(self):
        """Get Square size"""
        return self.height

    @size.setter
    def size(self, value):
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attributes values (id, width, height, x, y)
            **kwargs (dict): New dct of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif k == "size":
                    self.size = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
