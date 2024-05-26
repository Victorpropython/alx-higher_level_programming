#!/usr/bin/python3
""" A rectangle that inherits from a base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle representation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The id of the rectangle.
    """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """Set/get the new REctangle width"""
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    
    @property
    def height(self):
        """Set/get the new Rectangle width"""
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value 

    @property
    def x(self):
        """Set/get the new Rectangle width"""
        return self.__x
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the new Rectangle width"""
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
    
    def area(self):
        """Return Rectangle area"""
        return self.width * self.height
    
    def display(self):
        """Use the '#' character to print the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for u in range(self.width)]
            print("")
    
    def update(self, *args,**kwargs):
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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif k == "width":
                    self.width = j
                elif k == "height":
                    self.height = j
                elif k == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """ for the dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }

    def __str__(self):
        """Method to print() and str() rectangle representationd"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
